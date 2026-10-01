# ROLVIO — PROJECT MEMORY

## Project

New Rolvio clean rebuild.

---

# Current Status

Planning and architecture stage.

No production application implementation has started.

---

# Why Rolvio Is Being Rebuilt

The old Rolvio proved the product concept but exposed important architectural problems.

Main lessons:

- Application execution was unreliable.
- Platforms had too much separate application logic.
- Candidate profile data was inconsistent.
- Resume upload was incomplete.
- Submission verification was weak.
- Some runners treated Submit clicks as success.
- Unexpected website states caused failures.
- Some exceptions were silently ignored.
- Session validation was weak.
- Email tracking contained bugs.
- Background state depended too much on logs/process behavior.

The new architecture is designed to remove these problems.

---

# Product Goal

Rolvio manages:

Job Search
→ Matching
→ Approval
→ Automatic Application
→ Verification
→ Email Tracking
→ Recruitment Tracking
→ Analytics

---

# Locked NORVI Authentication

Rolvio requires:

- Email.
- Password.
- Authentication Key.

Authentication is handled through the NORVI backend/API.

The desktop application must not connect directly to the agency production database.

Raw passwords must not be stored.

Authentication tokens must use secure storage.

---

# Locked AI Runtime

Runtime:

Ollama

Production model:

`gemma4:cloud`

This is an Ollama cloud-hosted model accessed through the local Ollama application/runtime.

Main AI inference therefore does not depend on the user's local GPU.

---

# Locked Ollama Startup Behavior

On startup:

1. Check Ollama installation.
2. Install automatically when missing.
3. Avoid visible command windows.
4. Start Ollama silently if not already running.
5. Track whether Rolvio started it.
6. Verify Ollama Cloud access.
7. Request one-time Ollama sign-in when needed.
8. Ensure `gemma4:cloud`.
9. Health-check AI before dependent tasks run.

---

# Locked Ollama Runtime Recovery

While Rolvio is running:

- Monitor Ollama health.
- Restart silently after unexpected crash/closure.
- Pause AI-dependent tasks during recovery.
- Use limited retries.
- Report failure if recovery cannot succeed.

---

# Locked Ollama Shutdown Behavior

If Ollama was already running before Rolvio:

Do not stop it when Rolvio closes.

If Rolvio started Ollama:

Rolvio may stop the runtime it owns during application shutdown.

---

# Initial Supported Platforms

- LinkedIn.
- Naukri.
- Internshala.
- Indeed.
- Wellfound.

---

# Future Platform Possibilities

- Shine.
- TimesJobs.
- Hirist.
- Freshersworld.
- Glassdoor.
- Remotive.
- External ATS systems.
- Other platforms.

---

# Locked Technology

- Windows 11.
- Python 3.13.15.
- `.venv`.
- PySide6.
- Playwright.
- Pydantic.
- SQLite.
- SQLAlchemy.
- Alembic.
- pytest.
- PyInstaller.
- Ollama.
- `gemma4:cloud`.

---

# Most Important Architecture Rule

Build:

One Generic Application Engine

and connect:

Platform Adapters

Do not build five independent autonomous application systems.

---

# Most Important Reliability Rule

Submit button clicked

does NOT mean:

Application successful.

Only VerificationEngine can produce:

`VERIFIED_APPLIED`

---

# Most Important Candidate Rule

Never invent important candidate facts.

Unknown important information must be requested from the user.

---

# Most Important Authentication Rule

NORVI account authentication, Ollama authentication and job-platform authentication are separate systems.

Do not mix them together.

---

# Most Important Privacy Rule

Rolvio is local-first for product data, but `gemma4:cloud` performs AI inference through Ollama Cloud.

Do not describe production AI inference as fully local.

---

# Current Phase

Phase 0 — Product & Architecture

---

# Completed

- Old Rolvio reviewed.
- Major old-system problems identified.
- Clean rebuild decision made.
- Product requirements defined.
- Authentication requirements locked.
- Ollama runtime requirements locked.
- `gemma4:cloud` selected.
- Architecture defined.
- Design defined.
- Development rules defined.
- Phase plan defined.
- Testing strategy defined.
- Security strategy defined.

---

# Immediate Next Step

1. Replace the ten documentation files with corrected versions.
2. Review for contradictions.
3. Mark Phase 0 complete.
4. Create the new Rolvio project architecture.
5. Begin Phase 1.
6. Do not begin LinkedIn/application adapters early.

---

# Known Future Decisions

These do not block Phase 1:

- Exact NORVI API endpoint contract.
- Exact final installer/update distribution mechanism.
- Multiple-resume feature timing.
- Future ATS implementation order.

The production AI model is no longer an open decision.