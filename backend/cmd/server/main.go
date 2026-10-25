// Package main is the entry point for the BitsToBytes Go backend.
//
// Architecture:
//   - handlers:   HTTP layer (thin — parses request, calls service, returns JSON)
//   - services:   Business logic layer (depends on repository interfaces)
//   - repositories: Data access layer (PostgreSQL implementation of interfaces)
//   - models:     Plain data structures (no logic)
//   - middleware:  HTTP middleware (CORS, logging, JWT auth)
//   - config:     Configuration from environment variables
//
// SOLID Principles:
//   - Single Responsibility: Each package has one job
//   - Open/Closed: New features can be added without modifying existing code
//   - Liskov Substitution: Repository interfaces can be swapped
//   - Interface Segregation: Small, focused interfaces
//   - Dependency Inversion: Services depend on interfaces, not concrete types
//
// Functional Programming:
//   - Pure functions where possible (no side effects)
//   - Higher-order functions for middleware
//   - Immutability: models are read-only after creation
package main

import (
	"database/sql"
	"fmt"
	"log"
	"net/http"
	"time"

	"github.com/bittobytes/backend/internal/config"
	"github.com/bittobytes/backend/internal/handlers"
	"github.com/bittobytes/backend/internal/middleware"
	"github.com/bittobytes/backend/internal/repositories"
	"github.com/bittobytes/backend/internal/services"
	"github.com/bittobytes/backend/internal/utils"
	_ "github.com/lib/pq"
	"github.com/gorilla/mux"
)

func main() {
	// Load configuration
	cfg, err := config.Load()
	if err != nil {
		log.Fatalf("Failed to load config: %v", err)
	}

	// Connect to database
	db, err := sql.Open("postgres", cfg.Database.ConnectionString())
	if err != nil {
		log.Fatalf("Failed to connect to database: %v", err)
	}
	defer db.Close()

	// Test connection
	if err := db.Ping(); err != nil {
		log.Printf("Warning: database ping failed: %v (running without DB?)", err)
	}

	// Run migrations (in production, use a tool like golang-migrate)
	if err := runMigrations(db); err != nil {
		log.Printf("Warning: migrations failed: %v", err)
	}

	// Create email sender
	mailer := utils.NewSMTPMailer(
		cfg.Email.SMTPHost,
		cfg.Email.SMTPPort,
		cfg.Email.FromEmail,
		cfg.Email.FromPassword,
		"http://localhost:3000", // frontend URL for verification links
	)

	// Create repositories (data access layer)
	userRepo := repositories.NewUserRepository(db)
	progressRepo := repositories.NewProgressRepository(db)

	// Create services (business logic layer)
	authService := services.NewAuthService(
		userRepo,
		cfg.JWT.Secret,
		cfg.JWT.ExpirationHours,
		mailer,
	)
	progressService := services.NewProgressService(progressRepo)

	// Create handlers (HTTP layer)
	authHandler := handlers.NewAuthHandler(authService)
	progressHandler := handlers.NewProgressHandler(progressService)

	// Create router
	r := mux.NewRouter()

	// Apply global middleware
	r.Use(middleware.CORS)
	r.Use(middleware.Logging)

	// Health check endpoint
	r.HandleFunc("/api/health", func(w http.ResponseWriter, r *http.Request) {
		w.Header().Set("Content-Type", "application/json")
		w.Write([]byte(`{"status":"ok","service":"BitsToBytes API","time":"` + time.Now().Format(time.RFC3339) + `"}`))
	}).Methods("GET")

	// Register route groups
	authHandler.RegisterRoutes(r)
	progressHandler.RegisterRoutes(r, middleware.JWTAuth(cfg.JWT.Secret))

	// Create HTTP server
	srv := &http.Server{
		Addr:         fmt.Sprintf(":%s", cfg.Server.Port),
		Handler:      r,
		ReadTimeout:  time.Duration(cfg.Server.ReadTimeout) * time.Second,
		WriteTimeout: time.Duration(cfg.Server.WriteTimeout) * time.Second,
	}

	log.Printf("BitsToBytes API server starting on :%s", cfg.Server.Port)
	log.Printf("  DSA Fundamentals | Database Fundamentals | Networking Fundamentals | OS Fundamentals")
	log.Printf("  Email verification: %s", func() string {
		if cfg.Email.FromEmail == "" {
			return "DEV MODE (links printed to console)"
		}
		return "SMTP: " + cfg.Email.SMTPHost
	}())

	if err := srv.ListenAndServe(); err != nil {
		log.Fatalf("Server failed: %v", err)
	}
}

// runMigrations creates database tables if they don't exist.
// In production, use a proper migration tool like golang-migrate.
func runMigrations(db *sql.DB) error {
	migrations := []string{
		`CREATE TABLE IF NOT EXISTS users (
			id VARCHAR(36) PRIMARY KEY,
			email VARCHAR(255) UNIQUE NOT NULL,
			password_hash TEXT NOT NULL,
			is_verified BOOLEAN DEFAULT FALSE,
			verification_token TEXT DEFAULT '',
			created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
			updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
		)`,
		`CREATE TABLE IF NOT EXISTS progress (
			id VARCHAR(36) PRIMARY KEY,
			user_id VARCHAR(36) NOT NULL REFERENCES users(id) ON DELETE CASCADE,
			topic_id VARCHAR(100) NOT NULL,
			status VARCHAR(20) DEFAULT 'todo',
			created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
			updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
			UNIQUE(user_id, topic_id)
		)`,
	}

	for _, m := range migrations {
		if _, err := db.Exec(m); err != nil {
			return fmt.Errorf("migration failed: %w", err)
		}
	}
	log.Println("Database migrations completed successfully")
	return nil
}
