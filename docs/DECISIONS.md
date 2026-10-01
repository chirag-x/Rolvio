# ROLVIO — ARCHITECTURE DECISIONS

This document records important long-term decisions.

---

# ADR-001 — Rebuild Rolvio

Decision:

Build the new Rolvio from a clean architecture.

Reason:

The old implementation proved the concept but accumulated serious architectural problems.

Old code can be used as reference but should not dictate the new architecture.

---

# ADR-002 — Python

Decision:

Use Python 3.13.15.

---

# ADR-003 — Environment

Decision:

Use standard `.venv`.

---

# ADR-004 — Desktop Application

Decision:

Use PySide6.

Reason:

Rolvio is intended to be a professional Windows desktop product rather than a development-style Streamlit application.

---

# ADR-005 — Browser Automation

Decision:

Use Playwright directly.

Reason:

Rolvio requires direct access to:

- Browser lifecycle
- Tabs
- Frames
- Forms
- Screenshots
- Navigation
- Uploads
- Browser states

---

# ADR-006 — One Generic Application Engine

Decision:

Build one shared Application Engine.

Do not create completely independent application bots per platform.

---

# ADR-007 — Platform Adapters

Decision:

Platform-specific behavior belongs in adapters.

Initial:

- LinkedIn
- Naukri
- Internshala
- Indeed
- Wellfound

---

# ADR-008 — Canonical CandidateProfile

Decision:

Use one CandidateProfile everywhere.

Reason:

The old system stored important information in inconsistent places.

---

# ADR-009 — Canonical Job Model

Decision:

Normalize every job before using it downstream.

---

# ADR-010 — Application State Machine

Decision:

Every job application must follow explicit states.

Reason:

Rolvio must always know where it is in the application workflow.

---

# ADR-011 — Verification Controls Success

Decision:

Only Verification Engine may return VERIFIED_APPLIED.

Reason:

Clicking Submit does not prove success.

---

# ADR-012 — Structured Internal Results

Decision:

Subsystems communicate through structured objects.

Never use human console text as application state.

---

# ADR-013 — Unknown Facts Require User

Decision:

Important unknown factual information must not be invented.

---

# ADR-014 — AI Does Not Directly Control Browser

Decision:

AI may reason and produce structured recommendations.

Deterministic code performs browser actions.

---

# ADR-015 — Local Database

Decision:

Use SQLite.

---

# ADR-016 — SQLAlchemy

Decision:

Use SQLAlchemy repositories.

Reason:

Database logic should stay separate from UI and automation.

---

# ADR-017 — Database Migrations

Decision:

Use Alembic.

---

# ADR-018 — Local-First Privacy

Decision:

Candidate information should remain local whenever possible.

---

# ADR-019 — Secure Credential Storage

Decision:

Do not store email passwords or similar secrets as plaintext SQLite fields.

Use OS-backed credential storage.

---

# ADR-020 — AI Gateway

Decision:

All model calls use AIGateway.

No business module should depend directly on one AI SDK.

---

# ADR-021 — Ollama Initial Runtime

Decision:

Use Ollama as the current preferred AI runtime.

Current preferred model:

Gemma 4 approximately 32B.

The model remains configuration rather than core architecture.

---

# ADR-022 — CAPTCHA

Decision:

CAPTCHA requires human action.

Rolvio does not bypass it.

---

# ADR-023 — Diagnostics

Decision:

Failure diagnostics are mandatory.

Reason:

Supported websites can change.

---

# ADR-024 — Local Fake Application Sites

Decision:

Build fake application websites for testing.

Reason:

We need repeatable browser tests.

---

# ADR-025 — Real Website Smoke Testing

Decision:

Fake tests do not replace controlled testing on real supported platforms.

---

# ADR-026 — Background Task Manager

Decision:

Use structured task state.

Do not use PID files as the main application-state system.

---

# ADR-027 — Packaging

Decision:

Use PyInstaller initially.

---

# ADR-028 — Initial Platform Order

Implementation order:

1. LinkedIn
2. Internshala
3. Naukri
4. Indeed
5. Wellfound

Core application infrastructure must be completed before these platform phases.