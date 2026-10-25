// Package utils contains utility functions.
// Each function is pure — no side effects (functional programming).
package utils

import (
	"fmt"
	"time"

	"gopkg.in/gomail.v2"
)

// SMTPMailer implements services.EmailSender using SMTP.
type SMTPMailer struct {
	host     string
	port     int
	email    string
	password string
	appURL   string // e.g., http://localhost:3000 for verification links
}

// NewSMTPMailer creates a new SMTP mailer.
func NewSMTPMailer(host string, port int, email, password, appURL string) *SMTPMailer {
	return &SMTPMailer{
		host:     host,
		port:     port,
		email:    email,
		password: password,
		appURL:   appURL,
	}
}

// SendVerification sends a verification email to the user.
func (m *SMTPMailer) SendVerification(to, token string) error {
	if m.email == "" || m.password == "" {
		// In development mode, just log instead of sending
		fmt.Printf("[DEV] Verification link for %s: %s/verify?token=%s\n", to, m.appURL, token)
		return nil
	}

	mailer := gomail.NewMessage()
	mailer.SetHeader("From", m.email)
	mailer.SetHeader("To", to)
	mailer.SetHeader("Subject", "BitsToBytes — Verify Your Email")

	body := fmt.Sprintf(`
<html>
<body style="font-family: sans-serif; background: #1f1f1f; color: #f0f0f0; padding: 40px;">
  <div style="max-width: 500px; margin: 0 auto; background: #2a2a2a; padding: 40px; border-radius: 10px;">
    <h1 style="color: #ccff00; font-size: 24px;">BitsToBytes</h1>
    <p style="color: #a0a0a0; font-size: 16px;">Welcome! Please verify your email address to complete registration.</p>
    <a href="%s/verify?token=%s" 
       style="display: inline-block; background: #ccff00; color: #1f1f1f; padding: 12px 24px; border-radius: 6px; text-decoration: none; font-weight: bold; margin: 20px 0;">
       Verify Email
    </a>
    <p style="color: #666; font-size: 12px;">If you didn't create an account, you can ignore this email.</p>
  </div>
</body>
</html>
`, m.appURL, token)

	mailer.SetBody("text/html", body)

	dialer := gomail.NewDialer(m.host, m.port, m.email, m.password)
	return dialer.DialAndSend(mailer)
}

// FormatTime formats a time.Time for display.
// Pure function — no side effects.
func FormatTime(t time.Time) string {
	return t.Format(time.RFC3339)
}

// ValidateEmail does a basic email format check.
// Pure function.
func ValidateEmail(email string) bool {
	if email == "" {
		return false
	}
	atCount := 0
	for _, c := range email {
		if c == '@' {
			atCount++
		}
	}
	return atCount == 1 && len(email) > 3
}
