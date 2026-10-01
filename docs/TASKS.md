# ROLVIO — MASTER DEVELOPMENT PHASES

## Rule

Complete one phase before moving to the next.

---

# PHASE 0 — PRODUCT & ARCHITECTURE

Goal:

Lock the new Rolvio design before coding.

Tasks:

- Finalize PRD.
- Finalize architecture.
- Finalize design.
- Finalize development rules.
- Finalize security plan.
- Finalize test strategy.
- Confirm supported platforms.
- Confirm application state system.
- Confirm success verification rules.

Done when:

The project documentation has no major contradictions.

---

# PHASE 1 — PROJECT FOUNDATION

Tasks:

- Create project structure.
- Python 3.13.15 setup.
- `.venv`.
- Requirements.
- Configuration.
- Logging.
- Basic launcher.
- Basic PySide6 app.
- pytest configuration.
- Application paths.

Done when:

Rolvio launches and test suite runs.

---

# PHASE 2 — DOMAIN MODELS

Build:

- CandidateProfile
- ResumeDocument
- Job
- JobMatch
- Application
- ApplicationEvent
- FormField
- ResolvedAnswer
- VerificationResult
- EmailEvent
- BackgroundTask
- Enums

Add validation tests.

---

# PHASE 3 — DATABASE

Build:

- SQLite
- SQLAlchemy
- Alembic
- Database initialization
- Candidate repository
- Job repository
- Application repository
- Email repository
- Answer repository
- Session repository
- Task repository

Test fresh database creation.

---

# PHASE 4 — CANDIDATE PROFILE

Build complete Candidate Profile system.

Include:

- Personal
- Career
- Skills
- Experience
- Education
- Projects
- Certifications
- Languages
- Compensation
- Preferences
- Authorization
- Standard answers

---

# PHASE 5 — DOCUMENT SYSTEM

Build:

- Resume upload
- PDF parser
- Resume text extraction
- Resume structured extraction
- Original resume storage
- Document manager
- Resume path management
- File validation

Test upload and later browser upload.

---

# PHASE 6 — SECURITY FOUNDATION

Build:

- Credential Store
- Secret manager
- Encryption
- Redaction
- Secure session storage
- Secure email credentials

---

# PHASE 7 — AI GATEWAY

Build:

- Provider interface
- Ollama provider
- Model configuration
- Structured responses
- Timeouts
- Retry logic
- Prompt system
- Guardrails
- Fake test provider

---

# PHASE 8 — UI FOUNDATION

Build:

- Main window
- Sidebar
- Navigation
- Theme
- Cards
- Buttons
- Tables
- Dialogs
- Badges
- Loading states
- Error states

---

# PHASE 9 — PROFILE UI

Build:

- Profile page
- Resume page
- Candidate sections
- Save/load
- Validation
- Documents view

---

# PHASE 10 — BROWSER RUNTIME

Build:

- Playwright Browser Manager
- Context management
- Tabs
- Frames
- Navigation
- Screenshots
- Browser modes
- Timeouts
- Artifact capture

---

# PHASE 11 — SESSION MANAGER

Build:

- Login workflow
- Session save
- Session restore
- Session verification
- Expired session detection
- Login required state
- Session UI

---

# PHASE 12 — PLATFORM ADAPTER FRAMEWORK

Build:

- PlatformAdapter interface
- Platform registry
- Platform capabilities
- Adapter loader

Register:

- LinkedIn
- Naukri
- Internshala
- Indeed
- Wellfound

---

# PHASE 13 — JOB NORMALIZATION

Build:

- RawPlatformJob
- Job normalization
- URL normalization
- Company normalization
- Location normalization
- Duplicate detection

---

# PHASE 14 — JOB DISCOVERY ENGINE

Build generic discovery service.

Include:

- Multiple platforms
- Search request
- Pagination
- Limits
- Cancellation
- Progress
- Errors
- Persistence

---

# PHASE 15 — JOB SEARCH ADAPTERS

Implement search for:

- LinkedIn
- Naukri
- Internshala
- Indeed
- Wellfound

Test real job discovery.

---

# PHASE 16 — JOB MATCHING ENGINE

Build:

- Skills comparison
- Experience comparison
- Location compatibility
- Education compatibility
- Authorization compatibility
- Semantic analysis
- Overall match
- Missing skills
- Explanation

---

# PHASE 17 — APPROVAL ENGINE

Build:

- Manual mode
- Smart mode
- Autonomous mode
- Match thresholds
- Company exclusion
- Platform rules
- Location rules
- Daily limits

---

# PHASE 18 — FORM FIELD MODEL

Build normalized types for:

- Text
- Number
- Textarea
- Select
- Radio
- Checkbox
- Combobox
- Autocomplete
- Multiselect
- Date
- File
- Resume
- Consent
- Unknown

---

# PHASE 19 — FORM OBSERVER

Build:

- Form detection
- Field extraction
- Labels
- Required fields
- Current values
- Options
- Validation state
- Stable field identification

Use fake websites for tests.

---

# PHASE 20 — ANSWER ENGINE

Build:

- CandidateProfile answers
- Saved answers
- Semantic answer matching
- Safe derivation
- Writing answers
- Unknown factual detection
- Confidence
- Batch answering

---

# PHASE 21 — ANSWER MEMORY

Build:

- Question memory
- Equivalent questions
- User-confirmed answers
- Reuse policy
- Edit/delete
- Confidence

---

# PHASE 22 — FORM FILLER

Implement:

- Text
- Number
- Textarea
- Select
- Radio
- Checkbox
- Custom dropdown
- Combobox
- Autocomplete
- Date
- File upload
- Resume upload
- Multiselect

Verify values after filling.

---

# PHASE 23 — APPLICATION STATE MACHINE

Build:

- States
- Valid transitions
- Persistence
- Pause
- Resume
- Cancel
- Needs-user states
- Failure states

---

# PHASE 24 — APPLICATION ORCHESTRATOR

Build generic application workflow:

Job
→ Session
→ Application Open
→ Observe
→ Fill
→ Validate
→ Next
→ Review
→ Submit

Test on local fake sites.

---

# PHASE 25 — VERIFICATION ENGINE

Build:

- Success message detection
- URL verification
- Applied state
- Platform signals
- Verification confidence
- VERIFIED_APPLIED
- SUBMITTED_UNVERIFIED
- ALREADY_APPLIED

Critical rule:

Submit click alone must never equal success.

---

# PHASE 26 — RECOVERY ENGINE

Build:

- Page snapshot
- Popup recovery
- New tab recovery
- Iframe recovery
- Validation recovery
- Session recovery
- Retry limits
- User intervention
- Failure diagnostics

---

# PHASE 27 — LINKEDIN APPLICATION ADAPTER

Build LinkedIn-specific:

- Easy Apply detection
- Already applied
- Application state signals
- Platform navigation
- Verification signals

Use generic form engine.

Run controlled real tests.

---

# PHASE 28 — INTERNSHALA APPLICATION ADAPTER

Build:

- Apply detection
- Eligibility detection
- Resume/profile step
- Application state signals
- Success verification

Critical regression:

Not Eligible must never be counted as Applied.

---

# PHASE 29 — NAUKRI APPLICATION ADAPTER

Build:

- Apply detection
- Native application
- External redirect detection
- Application form state
- Verification

---

# PHASE 30 — INDEED APPLICATION ADAPTER

Build:

- Indeed Apply
- Iframe support
- Multi-step navigation
- Resume upload
- CAPTCHA pause
- Verification

Important:

Do not silently swallow errors.

---

# PHASE 31 — WELLFOUND APPLICATION ADAPTER

Build:

- Apply
- Questions
- Multi-step forms
- Re-observe after every Next
- Resume behavior
- Verification

---

# PHASE 32 — EMAIL TRACKER

Build:

- Multiple email accounts
- Secure credentials
- IMAP
- UID state
- New email detection
- Classification
- Application matching
- Timeline updates
- Ambiguous match review

---

# PHASE 33 — DASHBOARD, CRM & ANALYTICS

Build:

- Dashboard
- Activity feed
- Application tracker
- Kanban
- Email tracker UI
- Analytics
- Platform metrics
- Interview statistics
- Failure statistics

---

# PHASE 34 — NORVI LICENSING

Build:

- NORVI account
- Activation
- Device authorization
- Signed lease
- Offline grace period
- Account screen
- Safe failure

---

# PHASE 35 — PRODUCTION RELEASE

Perform:

- Full unit tests
- Integration tests
- E2E tests
- Platform regression
- Security review
- Fresh install
- Playwright install
- Database bootstrap
- PyInstaller
- Clean Windows test
- Packaging
- Final production validation

Rolvio is complete only after real end-to-end validation succeeds.