// Package models defines all domain entities.
// Each model is a plain data structure — no business logic here (separation of concerns).
package models

import (
	"time"
)

// User represents a registered user of BitsToBytes.
type User struct {
	ID              string    `json:"id"`
	Email           string    `json:"email"`
	PasswordHash    string    `json:"-"`           // never expose in JSON
	IsVerified      bool      `json:"is_verified"`
	VerificationToken string  `json:"-"`           // internal only
	CreatedAt       time.Time `json:"created_at"`
	UpdatedAt       time.Time `json:"updated_at"`
}

// AuthRequest represents login/signup request body.
type AuthRequest struct {
	Email    string `json:"email"`
	Password string `json:"password"`
}

// VerifyRequest represents email verification request.
type VerifyRequest struct {
	Token string `json:"token"`
}

// AuthResponse is returned on successful auth.
type AuthResponse struct {
	Token string `json:"token"`
	User  User   `json:"user"`
}

// Progress represents a user's topic progress.
type Progress struct {
	ID        string    `json:"id"`
	UserID    string    `json:"user_id"`
	TopicID   string    `json:"topic_id"`
	Status    string    `json:"status"` // "todo", "learning", "done", "review"
	CreatedAt time.Time `json:"created_at"`
	UpdatedAt time.Time `json:"updated_at"`
}
