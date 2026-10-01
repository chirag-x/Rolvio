# ROLVIO — SECURITY & PRIVACY

## 1. Goal

Rolvio handles highly sensitive user information.

Security must be part of the architecture from the beginning.

---

# 2. Sensitive Information

Sensitive data includes:

- Full name.
- Email.
- Phone.
- Location.
- Resume.
- Education.
- Employment.
- Salary.
- Work authorization.
- Application answers.
- Email credentials.
- Browser sessions.
- Cookies.
- NORVI Authentication Key.
- NORVI authentication tokens.
- Recruiter emails.

---

# 3. NORVI Authentication Security

Rolvio login requires:

- Email.
- Password.
- Authentication Key.

The desktop application must authenticate through the NORVI backend/API.

The desktop application must never contain production agency-database credentials.

The desktop application must never directly connect to the production authentication database.

---

# 4. Password Policy

Raw user passwords must:

- Never be stored locally.
- Never be written to logs.
- Never be included in diagnostics.
- Never be cached in plaintext files.

Password fields should be cleared from memory/UI state when practical after authentication.

---

# 5. Authentication Key Security

The Authentication Key is sensitive.

It must:

- Never appear in normal logs.
- Never be committed to Git.
- Never be included in exported diagnostics.
- Be transmitted only over secure HTTPS to the NORVI backend.

If local retention is required by a future design, it must use protected credential storage.

---

# 6. Authentication Tokens

Access/session/refresh tokens should use OS-backed secure storage.

On Windows:

Use Windows Credential Manager or another approved protected-storage abstraction.

Do not store tokens as normal plaintext SQLite values.

---

# 7. Secrets Policy

Never commit:

- Passwords.
- Authentication Keys.
- API keys.
- Tokens.
- Cookies.
- Email credentials.
- Browser session files.
- Private license data.

---

# 8. Environment Files

Real environment files must be ignored by Git.

Only `.env.example` should be committed.

---

# 9. Ollama Installation Security

Rolvio may install Ollama automatically when missing.

Requirements:

- Download from an approved official source.
- Validate expected installer/source where practical.
- Do not execute arbitrary downloaded binaries.
- Avoid visible command windows.
- Respect Windows UAC/security requirements.
- Record installation failures safely.

---

# 10. Ollama Process Security

Rolvio must never indiscriminately terminate every Ollama process.

Track process ownership.

If Rolvio started the runtime:

It may stop the Rolvio-owned process during shutdown.

If Ollama already existed:

Leave it running.

---

# 11. Ollama Cloud Privacy

Production model:

`gemma4:cloud`

This is cloud-hosted AI inference.

Therefore relevant AI content may leave the local PC for processing by Ollama's cloud service.

Rolvio must minimize what is sent.

Only send context needed for the current operation.

Possible required context:

- Relevant candidate-profile fields.
- Relevant resume-derived information.
- Job description.
- Application question.
- Relevant email excerpt for classification.

Do not send unrelated:

- Local files.
- Email history.
- Entire database.
- Unrelated resume sections.
- Secrets.

---

# 12. No Silent AI Provider Changes

Rolvio must not silently move user data to a different AI provider.

Changing AI provider/model behavior requires an explicit documented product decision.

---

# 13. Browser Sessions

Browser sessions may grant access to job accounts.

Requirements:

- Never commit session files.
- Never print cookies.
- Store under private application data.
- Protect appropriately.
- Provide logout/removal.
- Detect expiration.

---

# 14. Local Database

SQLite contains private candidate information.

Requirements:

- Store locally.
- Never commit DB.
- Use repositories.
- Use migrations.
- Use transactions.
- Enable foreign keys.

---

# 15. Resume Security

Validate uploads:

- File type.
- Extension.
- Size.
- Filename.

Do not execute uploaded files.

Store documents only under controlled application directories.

---

# 16. Email Security

Email credentials must use secure credential storage.

Use TLS-protected IMAP.

TLS certificate validation must remain enabled.

Do not store app passwords as plaintext database fields.

---

# 17. Job Platform Login

Prefer user-controlled interactive login.

Do not ask users to paste raw browser cookies as the normal authentication experience.

---

# 18. CAPTCHA

Rolvio does not bypass CAPTCHA automatically.

Pause and request user action.

---

# 19. Logging

Never log full:

- Passwords.
- Authentication Keys.
- API keys.
- Access tokens.
- Cookies.
- Authorization headers.
- Resume contents.
- Private email bodies.

Use redaction.

---

# 20. Diagnostics

Diagnostics may include website content.

Before export/sharing, redact sensitive information where practical.

Never include stored credentials.

---

# 21. NORVI Backend Privacy Boundary

NORVI authentication may receive data required for:

- Account authentication.
- Authentication Key validation.
- Product access validation.
- Security/session validation.

Normal authentication must not upload:

- Resume.
- Job history.
- Application history.
- Email content.
- Full CandidateProfile.

---

# 22. URL Validation

Validate browser navigation where needed.

Expected external schemes:

- HTTPS.
- Controlled HTTP for local development only.

Reject unsafe/unexpected schemes unless explicitly required.

---

# 23. File Path Safety

Prevent:

- Path traversal.
- Unsafe filenames.
- Unexpected directories.
- Arbitrary execution.

---

# 24. Dependency Security

Before release:

- Review dependencies.
- Remove unused libraries.
- Pin stable versions where appropriate.
- Review known security advisories where practical.

---

# 25. Least Privilege

Normal Rolvio operation should not require Windows Administrator access.

Installation may require OS elevation when unavoidable.

---

# 26. Application Data Integrity

Incorrect application information can harm users.

Unknown factual information must never be guessed.

This is a security and data-integrity requirement.

---

# 27. User-Facing Errors

User-facing errors must not expose:

- Passwords.
- Authentication Keys.
- Tokens.
- Cookies.
- Secret file contents.
- Full stack traces.

Technical details belong in diagnostics.

---

# 28. Security Review Before Release

Review:

- NORVI authentication.
- Credential storage.
- Ollama installer.
- Ollama runtime control.
- Ollama cloud data boundary.
- Browser sessions.
- Database.
- Resumes.
- Email.
- Network destinations.
- Logs.
- Diagnostics.
- Installer.

---

# 29. Security Incident Process

If a security problem is discovered:

1. Stop affected functionality.
2. Determine scope.
3. Protect affected user data.
4. Fix root cause.
5. Add regression test.
6. Update documentation if architecture changes.
7. Release corrected version.