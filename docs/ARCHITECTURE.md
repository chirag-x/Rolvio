# ROLVIO — SYSTEM ARCHITECTURE

## 1. Architecture Goal

Rolvio must be modular, testable, maintainable, secure and recoverable.

The central architectural principle is:

One Rolvio Core  
+  
One Generic Application Engine  
+  
Platform Adapters

Do not build five completely independent job-application bots.

All major systems must communicate through structured services, domain models and events.

The architecture must prevent the problems found in the previous Rolvio version:

- Platform runners becoming independent mini-applications.
- Candidate data using different formats in different modules.
- Application success being inferred from logs.
- Submit clicks being treated as successful applications.
- Resume uploads being skipped.
- Browser exceptions being silently ignored.
- Sessions being treated as valid simply because files exist.
- AI models being hard-coded throughout business logic.
- Browser automation hanging when an unexpected page appears.
- Credentials being stored insecurely.
- UI code directly containing business logic.

---

# 2. Locked Technology Stack

## Operating System

Windows 11

---

## Language

Python 3.13.15

---

## Environment

Standard Python `.venv`

Do not make `uv` a required dependency.

---

## Desktop UI

PySide6

Rolvio is a native Windows desktop product.

The production application must not depend on Streamlit.

---

## Browser Automation

Playwright for Python

Playwright is the deterministic browser execution layer.

---

## Database

SQLite

Rolvio is primarily a local desktop product.

---

## ORM

SQLAlchemy

---

## Database Migrations

Alembic

---

## Validation

Pydantic

All important internal data structures and AI responses should use validated models.

---

## AI Runtime

Ollama

---

## Production AI Model

`gemma4:cloud`

Rolvio uses the local Ollama application/runtime as the client for accessing the cloud-hosted model.

The main model inference does not depend on the user's local GPU.

Rolvio must not silently switch to another model or provider.

---

## Document Parsing

- pypdf
- pdfplumber
- python-docx when required

---

## Secure Credential Storage

Use an OS-backed credential abstraction.

Windows implementation should use Windows Credential Manager or another approved Windows-protected storage mechanism.

Libraries such as `keyring` may be used behind the abstraction.

---

## HTTP Client

Use a maintained asynchronous HTTP client such as:

- httpx

for NORVI API communication and other approved network services.

---

## Testing

- pytest
- pytest-asyncio
- Playwright browser tests

---

## Packaging

PyInstaller initially

---

# 3. Product Startup Architecture

```text
                        USER OPENS ROLVIO
                               │
                               ▼
                       Bootstrap Manager
                               │
              ┌────────────────┼─────────────────┐
              │                │                 │
              ▼                ▼                 ▼
        App Foundation    NORVI Auth       Ollama Runtime
              │                │                 │
              │          Session Check      Install Check
              │                │                 │
              │          Authentication     Runtime Check
              │                │                 │
              │                │              Start if needed
              │                │                 │
              │                │           Cloud Auth Check
              │                │                 │
              │                │            Model Check
              │                │                 │
              │                │            Health Check
              │                │                 │
              └────────────────┼─────────────────┘
                               │
                               ▼
                         Startup Ready?
                          /           \
                        NO             YES
                        │               │
                 Setup / Error          ▼
                                  Rolvio Main UI