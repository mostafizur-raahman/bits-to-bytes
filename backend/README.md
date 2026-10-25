# BitsToBytes Go Backend

> **SOLID principles + Functional programming + Email verification auth**

## Architecture

```
backend/
├── cmd/
│   └── server/
│       └── main.go          ← Entry point — wires everything together
├── internal/
│   ├── config/              ← Configuration (env vars, typed)
│   ├── handlers/            ← HTTP layer (thin — parses request, calls service, returns JSON)
│   ├── middleware/          ← HTTP middleware (CORS, logging, JWT auth)
│   ├── models/              ← Plain data structures (no logic)
│   ├── repositories/        ← Data access (PostgreSQL, implements interfaces)
│   ├── services/            ← Business logic (depends on repo interfaces)
│   └── utils/               ← Pure utility functions (email, validation)
├── go.mod
└── .env.example
```

## SOLID Principles

| Principle | How it's applied |
|-----------|-----------------|
| **S**ingle Responsibility | Each package has one job: handlers=HTTP, services=logic, repos=data |
| **O**pen/Closed | Add new features by creating new services/handlers, not modifying existing |
| **L**iskov Substitution | UserRepository interface — swap PostgreSQL with any implementation |
| **I**nterface Segregation | Small focused interfaces (UserRepository, ProgressRepository) |
| **D**ependency Inversion | Services depend on repository interfaces, not concrete types |

## Functional Programming

- **Pure functions** — utils.ValidateEmail, config.getEnv (no side effects)
- **Higher-order functions** — middleware.JWTAuth(secret) returns a middleware function
- **Immutability** — models are read-only after creation
- **Factory functions** — NewAuthService(), NewUserRepository() instead of constructors

## API Endpoints

| Method | Path | Description | Auth |
|--------|------|-------------|------|
| GET | `/api/health` | Health check | No |
| POST | `/api/auth/signup` | Register new user + send verification email | No |
| POST | `/api/auth/login` | Login (requires verified email) | No |
| POST | `/api/auth/verify` | Verify email with token | No |
| GET | `/api/progress` | Get user's topic progress | JWT |
| PUT | `/api/progress/:topicId` | Update topic progress | JWT |

## Setup

```bash
# 1. Copy .env.example to .env and fill in values
cp .env.example .env

# 2. Install Go 1.22+
# 3. Install PostgreSQL and create database
createdb bittobytes

# 4. Run the server
go run cmd/server/main.go

# 5. Server starts on :8080
# Health check: http://localhost:8080/api/health
```

## Email Verification Flow

1. User signs up with email + password
2. Backend creates user (is_verified=false) + generates verification token
3. Backend sends email with verification link: `http://localhost:3000/verify?token=<token>`
4. In dev mode (no SMTP configured), link is printed to console
5. User clicks link → frontend sends POST /api/auth/verify with token
6. Backend marks user as verified
7. User can now login

## Frontend Integration

The Next.js frontend connects to this backend via API calls:

```typescript
// Example: signup
const response = await fetch('http://localhost:8080/api/auth/signup', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ email, password }),
});
const { token, user } = await response.json();
```
