// Package repositories handles database operations.
// Each repository is an interface — the concrete implementation uses PostgreSQL,
// but tests can mock it. This is the Dependency Inversion Principle (D from SOLID).
package repositories

import (
	"database/sql"
	"time"

	"github.com/bittobytes/backend/internal/models"
	"github.com/google/uuid"
)

// UserRepository defines the interface for user data operations.
// Using an interface means we can swap implementations (Postgres, in-memory, etc.)
type UserRepository interface {
	Create(email, passwordHash string) (*models.User, error)
	FindByEmail(email string) (*models.User, error)
	FindByID(id string) (*models.User, error)
	UpdateVerification(userID, token string) error
	MarkVerified(userID string) error
}

// postgresUserRepository is the concrete PostgreSQL implementation.
type postgresUserRepository struct {
	db *sql.DB
}

// NewUserRepository creates a new UserRepository with a PostgreSQL backend.
// This is a factory function — a functional approach to object creation.
func NewUserRepository(db *sql.DB) UserRepository {
	return &postgresUserRepository{db: db}
}

func (r *postgresUserRepository) Create(email, passwordHash string) (*models.User, error) {
	user := &models.User{
		ID:           uuid.New().String(),
		Email:        email,
		PasswordHash: passwordHash,
		IsVerified:   false,
		CreatedAt:    time.Now(),
		UpdatedAt:    time.Now(),
	}

	query := `
		INSERT INTO users (id, email, password_hash, is_verified, created_at, updated_at)
		VALUES ($1, $2, $3, $4, $5, $6)
		RETURNING id
	`
	err := r.db.QueryRow(
		query,
		user.ID, user.Email, user.PasswordHash,
		user.IsVerified, user.CreatedAt, user.UpdatedAt,
	).Scan(&user.ID)

	if err != nil {
		return nil, err
	}
	return user, nil
}

func (r *postgresUserRepository) FindByEmail(email string) (*models.User, error) {
	user := &models.User{}
	query := `
		SELECT id, email, password_hash, is_verified, verification_token, created_at, updated_at
		FROM users WHERE email = $1
	`
	err := r.db.QueryRow(query, email).Scan(
		&user.ID, &user.Email, &user.PasswordHash,
		&user.IsVerified, &user.VerificationToken,
		&user.CreatedAt, &user.UpdatedAt,
	)
	if err != nil {
		return nil, err
	}
	return user, nil
}

func (r *postgresUserRepository) FindByID(id string) (*models.User, error) {
	user := &models.User{}
	query := `
		SELECT id, email, password_hash, is_verified, created_at, updated_at
		FROM users WHERE id = $1
	`
	err := r.db.QueryRow(query, id).Scan(
		&user.ID, &user.Email, &user.PasswordHash,
		&user.IsVerified, &user.CreatedAt, &user.UpdatedAt,
	)
	if err != nil {
		return nil, err
	}
	return user, nil
}

func (r *postgresUserRepository) UpdateVerification(userID, token string) error {
	_, err := r.db.Exec(
		"UPDATE users SET verification_token = $1, updated_at = $2 WHERE id = $3",
		token, time.Now(), userID,
	)
	return err
}

func (r *postgresUserRepository) MarkVerified(userID string) error {
	_, err := r.db.Exec(
		"UPDATE users SET is_verified = true, verification_token = '', updated_at = $1 WHERE id = $2",
		time.Now(), userID,
	)
	return err
}

// ProgressRepository defines the interface for progress data operations.
type ProgressRepository interface {
	Upsert(userID, topicID, status string) (*models.Progress, error)
	FindByUser(userID string) ([]models.Progress, error)
}

type postgresProgressRepository struct {
	db *sql.DB
}

func NewProgressRepository(db *sql.DB) ProgressRepository {
	return &postgresProgressRepository{db: db}
}

func (r *postgresProgressRepository) Upsert(userID, topicID, status string) (*models.Progress, error) {
	progress := &models.Progress{
		ID:        uuid.New().String(),
		UserID:    userID,
		TopicID:   topicID,
		Status:    status,
		UpdatedAt: time.Now(),
	}

	query := `
		INSERT INTO progress (id, user_id, topic_id, status, updated_at)
		VALUES ($1, $2, $3, $4, $5)
		ON CONFLICT (user_id, topic_id) DO UPDATE
		SET status = $4, updated_at = $5
		RETURNING id
	`
	err := r.db.QueryRow(
		query, progress.ID, progress.UserID,
		progress.TopicID, progress.Status, progress.UpdatedAt,
	).Scan(&progress.ID)

	if err != nil {
		return nil, err
	}
	return progress, nil
}

func (r *postgresProgressRepository) FindByUser(userID string) ([]models.Progress, error) {
	rows, err := r.db.Query(
		"SELECT id, user_id, topic_id, status, created_at, updated_at FROM progress WHERE user_id = $1",
		userID,
	)
	if err != nil {
		return nil, err
	}
	defer rows.Close()

	var progresses []models.Progress
	for rows.Next() {
		var p models.Progress
		err := rows.Scan(&p.ID, &p.UserID, &p.TopicID, &p.Status, &p.CreatedAt, &p.UpdatedAt)
		if err != nil {
			return nil, err
		}
		progresses = append(progresses, p)
	}
	return progresses, nil
}
