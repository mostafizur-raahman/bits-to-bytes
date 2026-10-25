// Package services contains business logic.
// Each service depends on repository interfaces (dependency injection).
// This is the Single Responsibility Principle (S from SOLID) —
// services handle business rules, repositories handle data access.
package services

import (
	"errors"
	"fmt"
	"time"

	"github.com/bittobytes/backend/internal/models"
	"github.com/bittobytes/backend/internal/repositories"
	"github.com/golang-jwt/jwt/v5"
	"github.com/google/uuid"
	"golang.org/x/crypto/bcrypt"
)

var (
	ErrUserAlreadyExists   = errors.New("user already exists")
	ErrUserNotFound       = errors.New("user not found")
	ErrInvalidCredentials  = errors.New("invalid email or password")
	ErrEmailNotVerified    = errors.New("email not verified — please check your inbox")
	ErrInvalidToken        = errors.New("invalid or expired verification token")
	ErrEmailSendFailed     = errors.New("failed to send verification email")
)

// EmailSender is an interface for sending emails.
// This allows us to swap implementations (real SMTP, mock for tests).
type EmailSender interface {
	SendVerification(to, token string) error
}

// AuthService handles authentication business logic.
type AuthService struct {
	userRepo  repositories.UserRepository
	jwtSecret string
	jwtExpHrs int
	emailer   EmailSender
}

// NewAuthService creates a new AuthService.
// Dependencies are injected — this is the Dependency Inversion Principle.
func NewAuthService(
	userRepo repositories.UserRepository,
	jwtSecret string,
	jwtExpHrs int,
	emailer EmailSender,
) *AuthService {
	return &AuthService{
		userRepo:  userRepo,
		jwtSecret: jwtSecret,
		jwtExpHrs: jwtExpHrs,
		emailer:   emailer,
	}
}

// SignUp registers a new user and sends a verification email.
// Pure business logic — no HTTP concerns here.
func (s *AuthService) SignUp(email, password string) (*models.AuthResponse, error) {
	// Check if user already exists
	existing, _ := s.userRepo.FindByEmail(email)
	if existing != nil {
		return nil, ErrUserAlreadyExists
	}

	// Hash password
	hash, err := bcrypt.GenerateFromPassword([]byte(password), bcrypt.DefaultCost)
	if err != nil {
		return nil, fmt.Errorf("failed to hash password: %w", err)
	}

	// Create user
	user, err := s.userRepo.Create(email, string(hash))
	if err != nil {
		return nil, fmt.Errorf("failed to create user: %w", err)
	}

	// Generate verification token
	token := uuid.New().String()
	err = s.userRepo.UpdateVerification(user.ID, token)
	if err != nil {
		return nil, fmt.Errorf("failed to set verification token: %w", err)
	}

	// Send verification email
	err = s.emailer.SendVerification(email, token)
	if err != nil {
		return nil, ErrEmailSendFailed
	}

	// Generate JWT
	jwtToken, err := s.generateJWT(user.ID, user.Email)
	if err != nil {
		return nil, fmt.Errorf("failed to generate token: %w", err)
	}

	return &models.AuthResponse{
		Token: jwtToken,
		User:  *user,
	}, nil
}

// Login authenticates a user.
func (s *AuthService) Login(email, password string) (*models.AuthResponse, error) {
	user, err := s.userRepo.FindByEmail(email)
	if err != nil {
		return nil, ErrUserNotFound
	}

	// Verify password
	err = bcrypt.CompareHashAndPassword([]byte(user.PasswordHash), []byte(password))
	if err != nil {
		return nil, ErrInvalidCredentials
	}

	// Check if email is verified
	if !user.IsVerified {
		return nil, ErrEmailNotVerified
	}

	// Generate JWT
	jwtToken, err := s.generateJWT(user.ID, user.Email)
	if err != nil {
		return nil, fmt.Errorf("failed to generate token: %w", err)
	}

	return &models.AuthResponse{
		Token: jwtToken,
		User:  *user,
	}, nil
}

// VerifyEmail verifies a user's email using a verification token.
func (s *AuthService) VerifyEmail(token string) error {
	// In a real implementation, we'd look up the user by the token.
	// For simplicity, we'll just mark it as verified.
	// In production, add proper token validation + expiry.
	userID, err := s.parseVerificationToken(token)
	if err != nil {
		return ErrInvalidToken
	}

	return s.userRepo.MarkVerified(userID)
}

// generateJWT creates a JWT token for a user.
func (s *AuthService) generateJWT(userID, email string) (string, error) {
	claims := jwt.MapClaims{
		"user_id": userID,
		"email":   email,
		"exp":     time.Now().Add(time.Duration(s.jwtExpHrs) * time.Hour).Unix(),
		"iat":     time.Now().Unix(),
	}
	token := jwt.NewWithClaims(jwt.SigningMethodHS256, claims)
	return token.SignedString([]byte(s.jwtSecret))
}

// parseVerificationToken extracts the user ID from a verification token.
// In production, this would use a separate token mechanism with expiry.
func (s *AuthService) parseVerificationToken(token string) (string, error) {
	// Simplified: token is the UUID we generated during signup.
	// In production, use signed JWT tokens with expiry.
	if token == "" {
		return "", errors.New("empty token")
	}
	return token, nil
}

// ProgressService handles progress tracking business logic.
type ProgressService struct {
	progressRepo repositories.ProgressRepository
}

func NewProgressService(progressRepo repositories.ProgressRepository) *ProgressService {
	return &ProgressService{progressRepo: progressRepo}
}

func (s *ProgressService) UpdateProgress(userID, topicID, status string) (*models.Progress, error) {
	return s.progressRepo.Upsert(userID, topicID, status)
}

func (s *ProgressService) GetProgress(userID string) ([]models.Progress, error) {
	return s.progressRepo.FindByUser(userID)
}
