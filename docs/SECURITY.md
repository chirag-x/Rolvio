# ROLVIO — SECURITY

## 1. Goal

Rolvio handles highly sensitive candidate information.

Security must be part of the design from the beginning.

---

# 2. Sensitive Information

Sensitive information includes:

- Full name
- Email
- Phone
- Location
- Resume
- Education
- Employment
- Salary
- Work authorization
- Application answers
- Email credentials
- Browser sessions
- Cookies
- Authentication tokens
- Recruiter emails

---

# 3. Secrets

Never commit:

- API keys
- Passwords
- Tokens
- Cookies
- Email credentials
- License tokens
- Session states

---

# 4. Environment Files

Real `.env` files must be ignored by Git.

Only `.env.example` should be committed.

---

# 5. Credential Storage

Use secure operating-system-backed storage.

On Windows:

Use Windows Credential Manager or another approved protected storage system.

Do not store email app passwords in plaintext SQLite fields.

---

# 6. Browser Sessions

Browser sessions may provide access to job accounts.

Requirements:

- Never commit session files
- Never print cookies in logs
- Store sessions under private application data
- Provide logout/remove session
- Protect session files appropriately

---

# 7. Database

SQLite contains private candidate information.

Requirements:

- Store locally
- Never commit DB
- Use repository layer
- Use migrations
- Use transactions
- Enable foreign keys

---

# 8. Resume Security

Validate uploads.

Check:

- File type
- File extension
- File size
- Filename

Do not execute uploaded files.

---

# 9. AI Privacy

If using local Ollama:

Candidate AI processing should remain local.

If a remote AI provider is added:

The user must know that relevant information may be transmitted externally.

Rolvio must never silently change from local to remote AI.

---

# 10. NORVI Licensing Privacy

Licensing may use:

- Account identity
- Activation key
- Device authorization
- License state

Normal licensing must not upload:

- Resume
- Application history
- Job history
- Email content
- Full candidate profile

---

# 11. Logs

Never log full:

- Passwords
- API keys
- Tokens
- Cookies
- Authorization headers
- Resume contents
- Private email bodies

Use redaction.

---

# 12. Diagnostics

Diagnostics may contain page content.

Before exporting diagnostics:

Sensitive values should be redacted where possible.

---

# 13. Email Security

Use secure IMAP.

TLS certificate verification must remain enabled.

Email credentials must use secure credential storage.

---

# 14. Login

Prefer user-controlled interactive login to job platforms.

Avoid asking users to manually paste raw session cookies as the standard login method.

---

# 15. CAPTCHA

Do not bypass CAPTCHA automatically.

Ask the user.

---

# 16. URL Validation

Browser navigation should validate URLs where necessary.

Allow expected web schemes:

https

and carefully controlled http where required for local development.

Reject unsafe schemes unless specifically needed.

---

# 17. File Paths

Never trust external filenames directly.

Prevent:

- Path traversal
- Unexpected directories
- Unsafe filenames

---

# 18. Dependencies

Before release:

- Review dependencies
- Remove unused libraries
- Pin appropriate versions
- Check security advisories where practical

---

# 19. Least Privilege

Rolvio should run without administrator rights during normal operation.

Administrator rights should only be needed if the installer specifically requires them.

---

# 20. Licensing

License tokens must:

- Be validated
- Expire
- Be securely stored
- Be independently verified

The existence of a local lease file must not automatically mean it is valid.

---

# 21. Application Data Integrity

Incorrect application information can harm users.

Therefore:

Unknown important information must never be guessed.

This is considered a security/data-integrity requirement.

---

# 22. Error Messages

User-facing errors must not reveal:

- Passwords
- Tokens
- Cookies
- Secret file contents
- Full stack traces

Technical details belong in diagnostics.

---

# 23. Security Review Before Release

Review:

- Credentials
- Sessions
- Database
- Resumes
- Email
- AI providers
- Network requests
- Licensing
- Logs
- Diagnostics
- Installer

---

# 24. Security Incident Process

If a security issue is discovered:

1. Stop affected functionality.
2. Determine affected data.
3. Protect users.
4. Fix root cause.
5. Add regression test.
6. Update documentation.
7. Release corrected version.