# ROLVIO — ARCHITECTURE DECISIONS

This file contains long-term decisions.

---

# ADR-001 — Clean Rebuild

Decision:

Build new Rolvio from a clean architecture.

Reason:

The old implementation proved the concept but accumulated architectural problems.

The old project may be consulted as reference but must not dictate the new architecture.

---

# ADR-002 — Python 3.13.15

Decision:

Use Python 3.13.15.

---

# ADR-003 — Standard `.venv`

Decision:

Use standard Python virtual environments.

---

# ADR-004 — PySide6 Desktop UI

Decision:

Use PySide6.

Reason:

Rolvio is intended to be a professional Windows desktop product.

---

# ADR-005 — Playwright Browser Automation

Decision:

Use Playwright directly.

Reason:

Rolvio requires control over:

- Browser lifecycle.
- Tabs.
- Frames.
- Forms.
- Screenshots.
- Uploads.
- Navigation.
- Browser state.

---

# ADR-006 — Mandatory NORVI Authentication

Decision:

Main Rolvio access requires:

- Email.
- Password.
- Authentication Key.

Authentication must be performed through the NORVI backend/API.

The desktop application must not connect directly to the production agency database.

---

# ADR-007 — Secure Authentication Storage

Decision:

Raw passwords are never stored.

Authentication tokens use OS-backed secure credential storage.

Authentication Keys are treated as sensitive secrets.

---

# ADR-008 — Ollama Production Runtime

Decision:

Use Ollama as Rolvio's production AI runtime/client.

---

# ADR-009 — Production Model

Decision:

Use:

`gemma4:cloud`

for Rolvio AI functionality.

This is a cloud-hosted Ollama model accessed through the local Ollama runtime.

---

# ADR-010 — No Silent AI Model Fallback

Decision:

Rolvio does not silently switch to another model or provider.

Reason:

Behavior, privacy and product expectations must remain predictable.

---

# ADR-011 — Automatic Ollama Setup

Decision:

Rolvio automatically detects whether Ollama is installed.

If missing, Rolvio performs the approved installation flow.

Normal setup must not display command windows.

OS-required UAC/security prompts may appear.

---

# ADR-012 — One-Time Ollama Cloud Authentication

Decision:

If Ollama Cloud authentication is unavailable, Rolvio prompts the user to complete the required Ollama sign-in.

After valid authentication, normal Rolvio launches should not repeatedly show this setup unless authentication becomes invalid.

---

# ADR-013 — Automatic Model Preparation

Decision:

Rolvio ensures `gemma4:cloud` is available/prepared automatically.

Model preparation should run in the background.

---

# ADR-014 — Ollama Health Monitoring

Decision:

Rolvio monitors Ollama while running.

If Ollama crashes or is accidentally closed, Rolvio attempts a silent restart.

Retries must have limits.

---

# ADR-015 — Ollama Process Ownership

Decision:

Rolvio must track whether it started Ollama.

If Ollama existed before Rolvio:

Rolvio does not stop it on exit.

If Rolvio started the runtime:

Rolvio may stop the Rolvio-owned runtime during graceful shutdown.

---

# ADR-016 — Cloud AI Privacy

Decision:

Production AI processing is not described as fully local because `gemma4:cloud` is cloud-hosted.

Rolvio minimizes information sent to AI and only sends task-relevant context.

---

# ADR-017 — One Generic Application Engine

Decision:

Build one generic shared application engine.

Do not create independent application bots for each platform.

---

# ADR-018 — Platform Adapters

Decision:

Platform-specific behavior belongs in adapters.

Initial adapters:

- LinkedIn.
- Naukri.
- Internshala.
- Indeed.
- Wellfound.

---

# ADR-019 — Canonical CandidateProfile

Decision:

Use one CandidateProfile everywhere.

---

# ADR-020 — Canonical Job Model

Decision:

Normalize all jobs before downstream use.

---

# ADR-021 — Application State Machine

Decision:

Every application follows explicit states.

---

# ADR-022 — Verification Controls Success

Decision:

Only VerificationEngine may produce:

`VERIFIED_APPLIED`

Clicking Submit does not prove success.

---

# ADR-023 — Structured Internal Results

Decision:

Subsystems communicate through structured objects.

Console text is never business state.

---

# ADR-024 — Unknown Facts Require User Input

Decision:

Important unknown factual information must not be invented.

---

# ADR-025 — AI Does Not Directly Control Browser

Decision:

AI may reason and produce structured output.

Deterministic code executes browser actions.

---

# ADR-026 — SQLite

Decision:

Use local SQLite for Rolvio product data.

---

# ADR-027 — SQLAlchemy Repositories

Decision:

Use SQLAlchemy through repository/service layers.

---

# ADR-028 — Alembic Migrations

Decision:

Use Alembic for database schema changes.

---

# ADR-029 — Secure Credentials Outside Ordinary SQLite Fields

Decision:

Email passwords, authentication tokens and similar secrets use secure credential storage rather than plaintext database fields.

---

# ADR-030 — CAPTCHA Requires Human Action

Decision:

Rolvio does not automate CAPTCHA bypass.

---

# ADR-031 — Diagnostics Are Core Functionality

Decision:

Browser failure screenshots, traces and page evidence are part of the architecture.

---

# ADR-032 — Fake Application Sites

Decision:

Use local fake application pages for deterministic browser testing.

---

# ADR-033 — Real Platform Smoke Tests

Decision:

Fake tests do not replace controlled real-platform validation.

---

# ADR-034 — Structured Background Task Manager

Decision:

Use persistent task state.

Do not use PID files as the primary business-state mechanism.

---

# ADR-035 — Packaging

Decision:

Use PyInstaller initially.

---

# ADR-036 — Initial Application Adapter Order

Implementation order:

1. LinkedIn.
2. Internshala.
3. Naukri.
4. Indeed.
5. Wellfound.

Generic application infrastructure must exist before these phases.2
3.