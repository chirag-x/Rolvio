# ROLVIO — ARCHITECTURE

## 1. Architecture Goal

Rolvio must be modular, testable and maintainable.

The most important architectural principle is:

One Rolvio Core
+
One Generic Application Engine
+
Platform Adapters

Do not build five completely separate job-application bots.

---

# 2. Technology Stack

## Operating System

Windows 11

## Language

Python 3.13.15

## Environment

Standard `.venv`

## Desktop UI

PySide6

## Browser Automation

Playwright

## Database

SQLite

## ORM

SQLAlchemy

## Database Migrations

Alembic

## Validation

Pydantic

## AI Runtime

AI Gateway architecture.

Initial/default AI runtime:

Ollama

Current preferred model:

Gemma 4 approximately 32B class.

The rest of Rolvio must not hard-code this model name.

## Document Parsing

- pypdf
- pdfplumber
- python-docx when needed

## Testing

pytest
pytest-asyncio
Playwright

## Packaging

PyInstaller initially

---

# 3. High-Level Architecture

```text
                         USER
                           │
                           ▼
                    ROLVIO DESKTOP UI
                           │
                           ▼
                   ROLVIO ORCHESTRATOR
                           │
     ┌─────────────────────┼──────────────────────┐
     │                     │                      │
     ▼                     ▼                      ▼
 Candidate System      Job Intelligence     Application System
     │                     │                      │
     │                     │                      ▼
     │                     │               State Machine
     │                     │                      │
     │                     │              Browser Runtime
     │                     │                      │
     │                     │               Form Engine
     │                     │                      │
     │                     │               Answer Engine
     │                     │                      │
     │                     │              Verification
     │                     │                      │
     │                     │                 Recovery
     │                     │
     └─────────────────────┼──────────────────────┐
                           │                      │
                           ▼                      ▼
                     Email Tracker          Analytics
                           │                      │
                           └──────────┬───────────┘
                                      ▼
                                 DATABASE