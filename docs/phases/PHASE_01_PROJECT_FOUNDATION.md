# PHASE 01 — PROJECT FOUNDATION

## Status

Completed

...

## Implementation Report

Completed during initial foundation setup.

### Files Added
- `src/rolvio/core/config.py`
- `src/rolvio/core/exceptions.py`
- `src/rolvio/core/lifecycle.py`
- `src/rolvio/observability/logging.py`
- `src/rolvio/ui/main_window.py`
- `tests/unit/test_foundation.py`

### Files Changed
- `main.py`
- Removed `launcher.py` (consolidated into main.py)

### Tests Executed
- `tests/unit/test_foundation.py` passed successfully.

### Results
Project foundation complete. Python 3.13 validated, PySide6 shell boots successfully with correct dark theme, structlog handles observability, config handles paths cleanly.

### Next Step
Proceed to Phase 02: Security & Secret Foundation

---

# 1. Purpose

Phase 01 creates the reliable technical foundation for the new Rolvio application.

This phase does NOT implement:

- NORVI authentication.
- Ollama installation/runtime management.
- Candidate Profile.
- Resume intelligence.
- Database business models.
- Job discovery.
- Job matching.
- Browser automation.
- Job-platform sessions.
- Application automation.
- Email tracking.
- Analytics.

Those systems belong to later phases.

The goal of this phase is to ensure that Rolvio has a clean, stable, testable application foundation before feature development begins.

At the end of this phase:

- The Python project must start correctly.
- Configuration must load correctly.
- Application paths must be reliable.
- Logging must work.
- The core exception foundation must exist.
- PySide6 must start correctly.
- The project must shut down cleanly.
- Tests must run successfully.
- The project must work from the real `main.py` entry point.

---

# 2. Mandatory Documents

Before writing or changing code, read these files completely:

1. `docs/PRD.md`
2. `docs/ARCHITECTURE.md`
3. `docs/DESIGN.md`
4. `docs/RULES.md`
5. `docs/TASKS.md`
6. `docs/DECISIONS.md`
7. `docs/MEMORY.md`
8. `docs/TEST_PLAN.md`
9. `docs/SECURITY.md`
10. `docs/README.md`
11. `docs/phases/PHASE_01_PROJECT_FOUNDATION.md`

Do not start implementation until the project requirements are understood.

Architecture and rules are mandatory.

---

# 3. Current Repository State

The repository already contains the planned folder scaffold.

Many Python files currently contain placeholder content such as:

`Implementation intentionally deferred to its assigned phase.`

Phase 01 should implement only the files required for the project foundation.

Do NOT start implementing files belonging to future phases simply because they already exist.

The current project already contains:

- `main.py`
- `launcher.py`
- `requirements.txt`
- `requirements-dev.txt`
- `.env.example`
- `.gitignore`
- `config/`
- `src/rolvio/`
- `tests/`
- `runtime/`
- `data/`
- `assets/`
- `migrations/`

Preserve the intended architecture.

---

# 4. Locked Technology for This Phase

Use:

- Windows 11 as the primary target.
- Python 3.13.15.
- Standard `.venv`.
- PySide6.
- Pydantic.
- python-dotenv.
- platformdirs.
- structlog.
- pytest.
- pytest-asyncio.

Do not introduce a different framework.

Do not replace `.venv` with `uv`, Conda, Poetry or another required environment manager.

---

# 5. Main Phase Objectives

Implement the following foundation systems:

1. Project environment validation.
2. Application path management.
3. Configuration loading.
4. Logging foundation.
5. Core exception hierarchy.
6. Application lifecycle skeleton.
7. Basic PySide6 application startup.
8. Basic main window shell.
9. Main entry point.
10. Launcher entry point.
11. Graceful application shutdown.
12. Foundation tests.
13. Developer smoke-test workflow.

---

# 6. Python Version Validation

Rolvio is designed for:

`Python 3.13.15`

The application should have a reusable Python-version validation mechanism.

It should:

- Detect the current Python version.
- Confirm that the runtime satisfies the project's supported Python version policy.
- Produce a clear developer-facing error if the runtime is unsupported.
- Avoid mysterious failures later during startup.

Do not hard-crash through obscure dependency errors.

The version validation should be reusable by:

- `main.py`
- Developer smoke tests.
- Packaging/bootstrap systems later.

Do not implement installer behavior here.

---

# 7. Virtual Environment Assumption

Development uses:

`.venv`

Phase 01 does not need to programmatically create the virtual environment during normal Rolvio startup.

The development setup should assume:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements-dev.txt