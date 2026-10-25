// Package handlers contains HTTP handlers.
// Each handler is a thin layer — it parses the request, calls the service,
// and returns a JSON response. No business logic here (Single Responsibility).
package handlers

import (
	"encoding/json"
	"net/http"
	"strings"

	"github.com/bittobytes/backend/internal/models"
	"github.com/bittobytes/backend/internal/services"
	"github.com/gorilla/mux"
)

// AuthHandler handles authentication HTTP requests.
type AuthHandler struct {
	authService *services.AuthService
}

// NewAuthHandler creates a new AuthHandler.
func NewAuthHandler(authService *services.AuthService) *AuthHandler {
	return &AuthHandler{authService: authService}
}

// RegisterRoutes registers all auth routes on the router.
// This is a functional approach — routes are registered in one place.
func (h *AuthHandler) RegisterRoutes(r *mux.Router) {
	r.HandleFunc("/api/auth/signup", h.SignUp).Methods("POST")
	r.HandleFunc("/api/auth/login", h.Login).Methods("POST")
	r.HandleFunc("/api/auth/verify", h.VerifyEmail).Methods("POST")
}

// SignUp handles POST /api/auth/signup
// Request body: { "email": "...", "password": "..." }
// Response: { "token": "...", "user": { ... } }
func (h *AuthHandler) SignUp(w http.ResponseWriter, r *http.Request) {
	var req models.AuthRequest
	if err := json.NewDecoder(r.Body).Decode(&req); err != nil {
		writeError(w, http.StatusBadRequest, "invalid request body")
		return
	}

	if req.Email == "" || req.Password == "" {
		writeError(w, http.StatusBadRequest, "email and password are required")
		return
	}

	if len(req.Password) < 8 {
		writeError(w, http.StatusBadRequest, "password must be at least 8 characters")
		return
	}

	resp, err := h.authService.SignUp(req.Email, req.Password)
	if err != nil {
		switch err {
		case services.ErrUserAlreadyExists:
			writeError(w, http.StatusConflict, err.Error())
		case services.ErrEmailSendFailed:
			writeError(w, http.StatusBadGateway, err.Error())
		default:
			writeError(w, http.StatusInternalServerError, "failed to sign up")
		}
		return
	}

	writeJSON(w, http.StatusCreated, resp)
}

// Login handles POST /api/auth/login
func (h *AuthHandler) Login(w http.ResponseWriter, r *http.Request) {
	var req models.AuthRequest
	if err := json.NewDecoder(r.Body).Decode(&req); err != nil {
		writeError(w, http.StatusBadRequest, "invalid request body")
		return
	}

	if req.Email == "" || req.Password == "" {
		writeError(w, http.StatusBadRequest, "email and password are required")
		return
	}

	resp, err := h.authService.Login(req.Email, req.Password)
	if err != nil {
		switch err {
		case services.ErrUserNotFound, services.ErrInvalidCredentials:
			writeError(w, http.StatusUnauthorized, "invalid email or password")
		case services.ErrEmailNotVerified:
			writeError(w, http.StatusForbidden, err.Error())
		default:
			writeError(w, http.StatusInternalServerError, "failed to login")
		}
		return
	}

	writeJSON(w, http.StatusOK, resp)
}

// VerifyEmail handles POST /api/auth/verify
// Request body: { "token": "..." }
func (h *AuthHandler) VerifyEmail(w http.ResponseWriter, r *http.Request) {
	var req models.VerifyRequest
	if err := json.NewDecoder(r.Body).Decode(&req); err != nil {
		writeError(w, http.StatusBadRequest, "invalid request body")
		return
	}

	if req.Token == "" {
		writeError(w, http.StatusBadRequest, "token is required")
		return
	}

	err := h.authService.VerifyEmail(req.Token)
	if err != nil {
		writeError(w, http.StatusBadRequest, err.Error())
		return
	}

	writeJSON(w, http.StatusOK, map[string]string{"message": "email verified successfully"})
}

// ProgressHandler handles progress HTTP requests.
type ProgressHandler struct {
	progressService *services.ProgressService
}

func NewProgressHandler(ps *services.ProgressService) *ProgressHandler {
	return &ProgressHandler{progressService: ps}
}

func (h *ProgressHandler) RegisterRoutes(r *mux.Router, authMiddleware mux.MiddlewareFunc) {
	s := r.PathPrefix("/api/progress").Subrouter()
	s.Use(authMiddleware)
	s.HandleFunc("", h.GetProgress).Methods("GET")
	s.HandleFunc("/{topicId}", h.UpdateProgress).Methods("PUT")
}

func (h *ProgressHandler) GetProgress(w http.ResponseWriter, r *http.Request) {
	userID := r.Context().Value("user_id").(string)

	progress, err := h.progressService.GetProgress(userID)
	if err != nil {
		writeError(w, http.StatusInternalServerError, "failed to get progress")
		return
	}

	writeJSON(w, http.StatusOK, progress)
}

func (h *ProgressHandler) UpdateProgress(w http.ResponseWriter, r *http.Request) {
	userID := r.Context().Value("user_id").(string)
	vars := mux.Vars(r)
	topicID := vars["topicId"]

	var body struct {
		Status string `json:"status"`
	}
	if err := json.NewDecoder(r.Body).Decode(&body); err != nil {
		writeError(w, http.StatusBadRequest, "invalid request body")
		return
	}

	validStatuses := map[string]bool{"todo": true, "learning": true, "done": true, "review": true}
	if !validStatuses[body.Status] {
		writeError(w, http.StatusBadRequest, "status must be one of: todo, learning, done, review")
		return
	}

	progress, err := h.progressService.UpdateProgress(userID, topicID, body.Status)
	if err != nil {
		writeError(w, http.StatusInternalServerError, "failed to update progress")
		return
	}

	writeJSON(w, http.StatusOK, progress)
}

// --- Helpers ---

func writeJSON(w http.ResponseWriter, status int, data interface{}) {
	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(status)
	json.NewEncoder(w).Encode(data)
}

func writeError(w http.ResponseWriter, status int, message string) {
	writeJSON(w, status, map[string]string{"error": message})
}

// extractBearerToken extracts the token from an Authorization: Bearer <token> header.
func extractBearerToken(r *http.Request) string {
	auth := r.Header.Get("Authorization")
	if auth == "" {
		return ""
	}
	parts := strings.SplitN(auth, " ", 2)
	if len(parts) != 2 || strings.ToLower(parts[0]) != "bearer" {
		return ""
	}
	return strings.TrimSpace(parts[1])
}
