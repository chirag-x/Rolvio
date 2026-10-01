# ROLVIO — PROJECT MEMORY

## Project

New Rolvio rebuild.

---

# Current Status

Planning and architecture.

No major application implementation has started yet.

---

# Why New Rolvio Is Being Built

The old Rolvio demonstrated that the product idea works, but several major issues were identified.

Main problems included:

- Application execution was unreliable.
- Different platforms had separate application logic.
- Candidate profile data was inconsistent.
- Resume upload was incomplete.
- Application success verification was weak.
- Some runners treated clicking Submit as success.
- Unexpected website states caused failures.
- Some errors were silently ignored.
- Session validation was weak.
- Email tracking had bugs.
- Background state depended too much on logs/processes.

The new Rolvio architecture is designed specifically to remove these problems.

---

# Product Goal

Rolvio should manage:

Job Search
→ Matching
→ Approval
→ Application
→ Verification
→ Email Tracking
→ Recruitment Tracking
→ Analytics

---

# Initial Platforms

- LinkedIn
- Naukri
- Internshala
- Indeed
- Wellfound

---

# Future Platforms

Possible future support:

- Shine
- TimesJobs
- Hirist
- Freshersworld
- Glassdoor
- Remotive
- Other platforms
- External ATS providers

---

# Locked Technology

- Windows 11
- Python 3.13.15
- `.venv`
- PySide6
- Playwright
- Pydantic
- SQLite
- SQLAlchemy
- Alembic
- pytest
- PyInstaller
- Ollama AI Gateway

---

# Most Important Architecture Rule

Build one:

Generic Application Engine

and connect:

Platform Adapters.

Do not build five separate autonomous application systems.

---

# Most Important Reliability Rule

Submit button clicked

does NOT mean:

Application successful.

Only Verification Engine can produce VERIFIED_APPLIED.

---

# Most Important Data Rule

Never invent important user facts.

Unknown important information must be requested from the user.

---

# Current Phase

Phase 0 — Product and Architecture

---

# Completed

- Old Rolvio reviewed.
- Major old-system problems identified.
- Decision made to rebuild.
- Product requirements defined.
- Architecture defined.
- Design direction defined.
- Development rules defined.
- Master phase plan defined.
- Testing strategy defined.
- Security strategy defined.

---

# Current Next Steps

1. Review all 10 project files.
2. Make sure there are no contradictions.
3. Mark Phase 0 complete.
4. Start Phase 1.
5. Build foundation only.
6. Do not start LinkedIn or other platform automation early.

---

# Important Development Reminder

The project should follow:

READ
→ UNDERSTAND
→ PLAN
→ IMPLEMENT
→ TEST
→ REVIEW
→ FIX
→ COMMIT
→ UPDATE DOCUMENTATION

Do not skip testing because code was generated successfully.

---

# Known Future Decisions

These do not need to block the first architecture phase:

- Final NORVI licensing API contract.
- Final updater system.
- Multiple resume support timing.
- Future ATS support.
- Exact production AI model configuration.

These should be decided in their relevant phases.