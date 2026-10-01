# PHASE 00 — PRODUCT CONTRACT & ARCHITECTURE VALIDATION

## Status

Completed

---

# 1. Purpose

Phase 00 exists to validate and lock the complete Rolvio product contract before implementation begins.

This phase is primarily a documentation, architecture and consistency phase.

Do NOT begin production feature implementation during Phase 00.

The purpose of this phase is to make sure every future coding phase follows one consistent definition of Rolvio.

Rolvio is being rebuilt from scratch because the previous version accumulated architectural problems, especially around:

- Application execution.
- Platform-specific runners.
- Form filling.
- Candidate-profile consistency.
- Resume upload.
- Submission verification.
- Recovery.
- Session handling.
- Email tracking.
- AI runtime management.
- Authentication.
- Background task state.
- Security.

The new Rolvio must solve these problems structurally rather than repeatedly patching them later.

---

# 2. Required Reading

Before doing any work in this phase, read completely:

- `docs/PRD.md`
- `docs/ARCHITECTURE.md`
- `docs/DESIGN.md`
- `docs/RULES.md`
- `docs/TASKS.md`
- `docs/DECISIONS.md`
- `docs/MEMORY.md`
- `docs/TEST_PLAN.md`
- `docs/SECURITY.md`
- `docs/README.md`

Also inspect:

- `.env.example`
- `.gitignore`
- `requirements.txt`
- `requirements-dev.txt`
- `config/app.example.json`
- `config/platform_registry.json`
- Existing `src/`
- Existing `tests/`
- Existing `docs/phases/`

Do not assume that existing placeholder source files contain implementation.

---

# 3. Phase Objective

At the end of Phase 00, the complete Rolvio project specification must be internally consistent.

The following must be fully locked:

1. Product purpose.
2. Supported platforms.
3. Future platform architecture.
4. Technology stack.
5. NORVI authentication behavior.
6. Ollama runtime behavior.
7. Production model.
8. Candidate data architecture.
9. Job normalization architecture.
10. Job matching architecture.
11. Application automation architecture.
12. Generic form engine architecture.
13. Submission verification architecture.
14. Recovery architecture.
15. Email tracking architecture.
16. Security architecture.
17. Desktop UI direction.
18. Testing strategy.
19. Development phase order.
20. Definition of production readiness.

---

# 4. Locked Product Identity

Product:

`Rolvio`

Brand:

`NORVI`

Product type:

Autonomous AI Job Search, Matching, Application and Career Tracking Agent.

Primary target platform:

Windows 11 Desktop.

Primary language:

Python 3.13.15.

Environment:

Standard `.venv`.

Desktop UI:

PySide6.

Browser automation:

Playwright.

Database:

SQLite.

ORM:

SQLAlchemy.

Migrations:

Alembic.

Validation:

Pydantic.

Testing:

pytest + pytest-asyncio + Playwright browser tests.

Packaging:

PyInstaller initially.

---

# 5. Locked Authentication Contract

Rolvio requires NORVI authentication before the main application becomes available.

Login requires:

- Email.
- Password.
- Authentication Key.

Architecture:

Rolvio Desktop
→ NORVI Authentication API
→ NORVI Backend
→ Agency Database

The desktop application must NEVER directly connect to the production agency database.

The desktop application must NEVER contain production database credentials.

Raw passwords must not be stored locally.

Authentication Keys are sensitive and must not appear in normal logs.

Authentication tokens must use secure operating-system-backed storage.

NORVI authentication is separate from:

- Ollama authentication.
- LinkedIn authentication.
- Naukri authentication.
- Internshala authentication.
- Indeed authentication.
- Wellfound authentication.

Do not combine these authentication contexts.

---

# 6. Locked Ollama Contract

AI Runtime:

`Ollama`

Production model:

`gemma4:cloud`

Rolvio uses the local Ollama runtime/client to access the Ollama-hosted cloud model.

The main AI model does not depend on the user's local GPU for inference.

Rolvio must not silently switch to another model or provider.

---

# 7. Locked Ollama First-Run Behavior

When Rolvio is opened:

1. Check whether Ollama is installed.
2. If missing, perform the approved automatic installation flow.
3. Avoid showing CMD or PowerShell windows.
4. Windows UAC/security prompts may appear when required by Windows.
5. Detect whether Ollama is already running.
6. If not running, start it silently.
7. Track whether Rolvio started it.
8. Check Ollama Cloud authentication/access.
9. If sign-in is required, show the one-time Ollama sign-in experience.
10. After sign-in, recheck cloud access.
11. Ensure `gemma4:cloud` is available/prepared.
12. Perform an AI health check.
13. Mark AI runtime ready.
14. Continue Rolvio startup.

---

# 8. Locked Ollama Runtime Recovery

While Rolvio is running:

- Monitor Ollama health.
- Detect process/API failure.
- Detect accidental user closure.
- Pause AI-dependent tasks during failure.
- Attempt limited silent restart.
- Recheck API.
- Recheck cloud authentication.
- Recheck `gemma4:cloud`.
- Resume work after successful recovery.
- Enter a clear AI error state when recovery fails.

No infinite restart loops are allowed.

---

# 9. Locked Ollama Ownership Rule

Before Rolvio starts Ollama, determine whether Ollama was already running.

If Ollama was already running:

`owned_by_rolvio = false`

If Rolvio starts Ollama:

`owned_by_rolvio = true`

When Rolvio closes:

If:

`owned_by_rolvio = true`

Rolvio may stop the runtime instance it started.

If:

`owned_by_rolvio = false`

Rolvio must leave the existing Ollama runtime running.

Rolvio must never indiscriminately kill all Ollama processes.

---

# 10. Locked AI Privacy Contract

`gemma4:cloud` is cloud-hosted.

Production AI inference must not be described as fully local.

Rolvio should minimize information sent for AI processing.

Only task-relevant information may be sent.

Examples:

- Relevant resume-derived information.
- Relevant CandidateProfile fields.
- Job description.
- Application question.
- Relevant email excerpt.

Do not send unrelated:

- Local files.
- Database contents.
- Authentication secrets.
- Browser cookies.
- Entire email history.
- Unrelated CandidateProfile fields.

---

# 11. Locked Candidate Architecture

Rolvio must have one canonical:

`CandidateProfile`

It is used by:

- Profile UI.
- Resume intelligence.
- Job matching.
- Answer resolution.
- Application execution.
- Email context where relevant.

Do not create different candidate dictionaries for different platform runners.

CandidateProfile includes:

- Personal information.
- Contact information.
- Career information.
- Education.
- Experience.
- Skills.
- Projects.
- Certifications.
- Languages.
- Compensation.
- Job preferences.
- Work authorization.
- Application answers.
- Relevant URLs.

---

# 12. Locked Resume Architecture

The initial Rolvio release supports a primary resume.

Required capabilities:

- PDF upload.
- File validation.
- Text extraction.
- Structured parsing.
- Original file retention.
- Resume metadata.
- Browser-upload-ready path.
- Resume upload during job applications.

Architecture should allow future:

- Multiple resumes.
- Role-specific resumes.
- Cover letters.
- Certificates.
- Other documents.

---

# 13. Locked Job Platform Scope

Initial supported platforms:

1. LinkedIn.
2. Naukri.
3. Internshala.
4. Indeed.
5. Wellfound.

Future platform architecture should allow:

- Shine.
- TimesJobs.
- Hirist.
- Freshersworld.
- Glassdoor.
- Remotive.
- Other job platforms.
- External ATS systems.

Future platforms are not required for initial production release unless explicitly added later.

---

# 14. Locked Platform Architecture

Rolvio must NOT become:

LinkedIn Bot
+
Naukri Bot
+
Internshala Bot
+
Indeed Bot
+
Wellfound Bot

Correct architecture:

Rolvio Core
+
Generic Application Engine
+
Platform Adapters

Platform-specific selectors and signals belong only inside platform modules.

Generic systems must remain platform-independent.

---

# 15. Locked Job Architecture

Every discovered platform job must be normalized into one canonical:

`Job`

The Job model should represent:

- Internal ID.
- Platform.
- External platform ID.
- URL.
- Title.
- Company.
- Description.
- Location.
- Work type.
- Employment type.
- Salary where available.
- Required experience.
- Required skills.
- Apply type.
- Posted date.
- Discovery date.
- Raw metadata.

Generic downstream systems must not depend on platform-specific raw job structures.

---

# 16. Locked Matching Architecture

Matching flow:

CandidateProfile
+
Canonical Job
→ Deterministic Compatibility Checks
+
AI Semantic Analysis
→ Structured JobMatch
→ Approval Policy

The matching result should include:

- Overall score.
- Skill score.
- Experience compatibility.
- Education compatibility.
- Location compatibility.
- Authorization compatibility.
- Seniority compatibility.
- Strong matches.
- Missing skills.
- Risks.
- Explanation.

AI output must be structured and validated.

---

# 17. Locked Approval Modes

Rolvio supports:

## Manual Mode

Every application requires user approval.

## Smart Mode

User-configured thresholds determine:

- Auto approve.
- Ask user.
- Ignore.

## Autonomous Mode

Rolvio may automatically apply within explicit user-defined rules.

Even Autonomous Mode must respect:

- Minimum match score.
- Daily application limit.
- Platform rules.
- Role rules.
- Company exclusions.
- Location preferences.
- Work type.
- Salary rules.

---

# 18. Locked Application Architecture

Generic application flow:

Approved Job
→ Application Orchestrator
→ Application State Machine
→ Browser Runtime
→ Platform Adapter
→ Page Observation
→ Form Detection
→ Field Extraction
→ Answer Resolution
→ Form Filling
→ Form Validation
→ Navigation
→ Review
→ Submit
→ Verification
→ Final Structured Result

Recovery may interrupt this flow whenever reality differs from expected state.

---

# 19. Locked Browser Rule

Important browser interactions must follow:

Observe
→ Understand
→ Act
→ Verify

Do not rely on long blind click sequences.

Do not treat fixed sleeps as the primary synchronization mechanism.

Prefer actual conditions such as:

- Element state.
- Navigation.
- URL change.
- Modal state.
- Frame state.
- Browser state.

---

# 20. Locked Generic Form Engine

Rolvio uses one shared Form Engine.

Required components:

- FormDetector.
- FieldExtractor.
- AnswerResolver.
- FormFiller.
- FormValidator.

Supported normalized field types should include:

- TEXT
- EMAIL
- PHONE
- NUMBER
- TEXTAREA
- URL
- SELECT
- CUSTOM_SELECT
- COMBOBOX
- RADIO
- CHECKBOX
- CHECKBOX_GROUP
- MULTISELECT
- AUTOCOMPLETE
- DATE
- FILE
- RESUME
- CONSENT
- UNKNOWN

Platform adapters must not recreate the complete Form Engine.

---

# 21. Locked Answer Safety

Answer priority:

1. Exact CandidateProfile data.
2. User-confirmed saved answer.
3. Semantic answer memory.
4. Safe deterministic derivation.
5. AI-generated writing.
6. User input.

Never implement:

- Every Yes/No answer = Yes.
- Unknown dropdown = select first/second option.
- Unknown radio = select first option.
- Unknown experience = invent a value.

Unknown important facts must produce:

`MISSING_INFORMATION`

or:

`NEEDS_USER`

---

# 22. Locked AI Browser Boundary

The LLM must not directly control browser actions.

Correct pattern:

AI
→ Structured reasoning/output
→ Validation
→ Deterministic browser executor

Malformed or unvalidated model output must never directly click buttons or fill forms.

---

# 23. Locked Application State Machine

Required states may include:

- CREATED
- QUEUED
- STARTING
- JOB_OPENED
- SESSION_CHECKING
- SESSION_VALID
- SESSION_EXPIRED
- ALREADY_APPLIED
- JOB_CLOSED
- APPLICATION_OPENING
- APPLICATION_STARTED
- FORM_OBSERVING
- FORM_READY
- ANSWERS_RESOLVING
- FORM_FILLING
- FORM_VALIDATING
- NEXT_STEP
- REVIEWING
- SUBMIT_READY
- SUBMIT_REQUESTED
- VERIFYING
- VERIFIED_APPLIED
- SUBMITTED_UNVERIFIED
- NEEDS_USER
- CAPTCHA_REQUIRED
- MISSING_INFORMATION
- EXTERNAL_APPLICATION
- UNSUPPORTED_STATE
- FAILED
- CANCELLED

State transitions must be structured and persisted.

---

# 24. Locked Submission Verification

Clicking Submit does NOT mean success.

Only:

`VerificationEngine`

may produce:

`VERIFIED_APPLIED`

Possible results:

- VERIFIED_APPLIED
- ALREADY_APPLIED
- SUBMITTED_UNVERIFIED
- FAILED
- NEEDS_USER

Potential evidence includes:

- Confirmation page.
- Success message.
- URL transition.
- Applied-state button.
- Application history.
- Application identifier.
- Platform-specific confirmation signal.

Console text must never determine application status.

---

# 25. Locked Recovery Architecture

When an unexpected page state occurs, Rolvio should collect a PageSnapshot.

PageSnapshot may include:

- URL.
- Title.
- Visible text.
- Buttons.
- Inputs.
- Form fields.
- Validation errors.
- Frames.
- Tabs.
- Modal state.
- Screenshot.
- DOM artifact.
- Current application state.
- Recent actions.

Recovery may:

- Re-observe.
- Retry.
- Switch tab.
- Switch frame.
- Refill.
- Close unexpected modal where safe.
- Refresh where safe.
- Ask user.
- Fail safely.

Retry budgets are mandatory.

---

# 26. Locked CAPTCHA Policy

Rolvio must not automatically bypass CAPTCHA.

When CAPTCHA is detected:

1. Pause application.
2. Set `CAPTCHA_REQUIRED`.
3. Notify user.
4. Open visible browser when needed.
5. User completes verification.
6. Re-observe page.
7. Resume safely.

---

# 27. Locked Authentication Separation

Rolvio contains three separate authentication systems:

## NORVI Authentication

Controls product access.

## Ollama Authentication

Controls Ollama Cloud access.

## Job Platform Authentication

Controls LinkedIn, Naukri, Internshala, Indeed, Wellfound, etc.

These must remain independent.

---

# 28. Locked Job Platform Session Architecture

A platform session file existing does not mean the session is valid.

Session Manager must support:

- Interactive login.
- Session save.
- Session restore.
- Session validation.
- Expiration detection.
- Login-required state.
- Logout/removal.

---

# 29. Locked Email Architecture

Email flow:

IMAP
→ UID Store
→ New Message
→ Pre-filter
→ Classification
→ Application Matching
→ EmailEvent
→ Recruitment Timeline

UID state must be persisted correctly.

Emails must not be matched only by company name.

Use multiple matching signals such as:

- Company.
- Job title.
- Sender domain.
- Platform.
- Application date.
- Thread.
- Job identifier.

Low-confidence matches require review.

---

# 30. Locked Status Separation

Do not use one overloaded application status.

## Discovery Status

- DISCOVERED
- MATCHED
- IGNORED
- REJECTED_BY_USER

## Execution Status

- QUEUED
- RUNNING
- NEEDS_USER
- VERIFIED_APPLIED
- SUBMITTED_UNVERIFIED
- FAILED
- CANCELLED

## Recruitment Status

- AWAITING_RESPONSE
- ASSESSMENT
- INTERVIEW
- EMPLOYER_REJECTED
- OFFER
- WITHDRAWN

User rejection and employer rejection must never be represented as the same state.

---

# 31. Locked Background Task Architecture

Background tasks are structured persistent entities.

Possible task types:

- AUTH_REFRESH
- AI_HEALTH_CHECK
- JOB_DISCOVERY
- JOB_MATCHING
- JOB_APPLICATION
- EMAIL_SCAN
- ANALYTICS
- MAINTENANCE

Possible task states:

- QUEUED
- RUNNING
- PAUSED
- WAITING_FOR_USER
- COMPLETED
- FAILED
- CANCELLED

Raw PID files must not be the primary business-state system.

---

# 32. Locked Diagnostics Architecture

Significant browser failures must create useful evidence.

Recommended structure:

runtime/failures/{trace_id}/

- metadata.json
- screenshot.png
- page.html
- visible_text.txt
- trace.json

Diagnostics must avoid leaking secrets.

---

# 33. Locked UI Direction

Rolvio is a PySide6 Windows desktop application.

Primary navigation should eventually include:

- Dashboard.
- Profile.
- Documents.
- Job Discovery.
- Matches.
- Application Queue.
- Live Activity.
- Application Tracker.
- Email Tracker.
- Platforms.
- Analytics.
- Settings.

Main design direction:

- Dark.
- Premium.
- Modern.
- Minimal.
- Professional.
- NORVI-aligned.

UI must remain responsive while background work runs.

---

# 34. Locked Database Architecture

Use:

SQLite
+
SQLAlchemy
+
Alembic
+
Repository/Service Pattern

UI must not directly execute SQL.

Important state changes should use transactions.

Foreign keys must be enabled.

Schema changes require migrations.

---

# 35. Locked Security Principles

Never commit:

- Passwords.
- Authentication Keys.
- API keys.
- Tokens.
- Cookies.
- Email credentials.
- Browser sessions.
- User resumes.
- Private database files.

Sensitive credentials must not be stored as ordinary plaintext SQLite values.

Logs must redact sensitive values.

---

# 36. Locked Testing Strategy

Testing layers:

Unit
→ Integration
→ Fake Browser Application Tests
→ E2E
→ Platform Regression
→ Controlled Real-Platform Smoke Tests
→ Fresh Windows Production Test

Real websites must never be the only test environment.

---

# 37. Definition of Done Rule

A phase is not complete because:

- Files were created.
- Code compiled.
- An AI coding tool said "done."

A phase is complete only when:

- Required implementation exists.
- Acceptance criteria pass.
- Tests pass.
- Important failure cases pass.
- No unresolved critical bug remains.
- Security requirements pass.
- Documentation matches implementation.

---

# 38. Documentation Consistency Audit

During Phase 00, inspect all ten documentation files and identify contradictions.

Check specifically:

## PRD

Must describe:

- NORVI authentication.
- Ollama runtime.
- `gemma4:cloud`.
- Job discovery.
- Matching.
- Application engine.
- Verification.
- Recovery.
- Email tracking.

## ARCHITECTURE

Must agree with PRD.

## DESIGN

Must include:

- Login.
- Startup preparation.
- Main UI direction.
- User intervention.
- CAPTCHA.
- Dashboard.
- Platform/session states.

## RULES

Must enforce architecture and safety constraints.

## TASKS

Must represent the actual approved implementation sequence.

## DECISIONS

Must contain permanent locked architecture decisions.

## MEMORY

Must reflect current project state.

## TEST_PLAN

Must test all critical product contracts.

## SECURITY

Must accurately reflect cloud AI behavior and authentication security.

## README

Must match the current project rather than the old Rolvio.

---

# 39. Phase-File Consistency Audit

IMPORTANT:

The phase files inside:

`docs/phases/`

must match the current phase order defined in:

`docs/TASKS.md`

The current final master plan contains:

Phase 00
through
Phase 37

The coding agent must inspect existing phase filenames.

If they still follow an older phase order, do NOT silently implement according to the old numbering.

Generate/rename phase files so their names and purposes exactly match the current `TASKS.md`.

Do not delete useful content without review.

---

# 40. Documentation Formatting Cleanup

Inspect documentation for accidental chat-format wrappers such as:

- Extra `---` at the top when not intended.
- Text like `# 4. RULES.md`.
- Literal opening ````markdown` fences wrapping an entire Markdown file.
- Missing closing fences.
- Assistant-response text accidentally pasted into documentation.

Clean these formatting problems without changing approved requirements.

The actual Markdown files should contain only the document content.

---

# 41. Phase 00 Implementation Restrictions

During Phase 00:

DO NOT implement:

- NORVI Authentication code.
- Ollama runtime code.
- Database.
- Candidate Profile.
- Job discovery.
- Matching.
- Browser automation.
- Form Engine.
- Platform adapters.
- Email Tracker.
- Dashboard features.

Phase 00 is a specification-validation phase.

Small repository/document-structure corrections are allowed when required to align the project with the approved architecture.

---

# 42. Required Phase 00 Actions

The coding agent must:

1. Read all ten main documentation files.
2. Read current `TASKS.md`.
3. Inspect current `docs/phases/`.
4. Inspect current project tree.
5. Identify contradictions.
6. Identify old phase numbering.
7. Correct documentation formatting artifacts.
8. Make phase filenames consistent with final `TASKS.md`.
9. Ensure no implementation was accidentally introduced into placeholder files.
10. Verify `.gitignore` covers private runtime data.
11. Verify `.env.example` contains no secrets.
12. Verify requirements files contain no obvious inappropriate production secrets or local paths.
13. Verify the source tree is structurally ready for Phase 1.
14. Update MEMORY.md to show Phase 00 complete only after all checks pass.

---

# 43. Expected Final Phase File Order

The final `docs/phases/` architecture must correspond to the current master plan:

- PHASE_00_PRODUCT_ARCHITECTURE.md
- PHASE_01_PROJECT_FOUNDATION.md
- PHASE_02_SECURITY_SECRET_FOUNDATION.md
- PHASE_03_NORVI_AUTHENTICATION.md
- PHASE_04_OLLAMA_RUNTIME_MANAGER.md
- PHASE_05_DOMAIN_MODELS.md
- PHASE_06_DATABASE_REPOSITORIES.md
- PHASE_07_AI_GATEWAY.md
- PHASE_08_DESKTOP_UI_FOUNDATION.md
- PHASE_09_BOOTSTRAP_ORCHESTRATION.md
- PHASE_10_CANDIDATE_PROFILE_SYSTEM.md
- PHASE_11_RESUME_DOCUMENT_SYSTEM.md
- PHASE_12_PROFILE_DOCUMENT_UI.md
- PHASE_13_BROWSER_RUNTIME.md
- PHASE_14_JOB_PLATFORM_SESSION_MANAGER.md
- PHASE_15_PLATFORM_ADAPTER_FRAMEWORK.md
- PHASE_16_JOB_NORMALIZATION.md
- PHASE_17_JOB_DISCOVERY_ENGINE.md
- PHASE_18_JOB_SEARCH_ADAPTERS.md
- PHASE_19_JOB_MATCHING_ENGINE.md
- PHASE_20_APPROVAL_POLICY_ENGINE.md
- PHASE_21_FORM_FIELD_MODEL.md
- PHASE_22_FORM_OBSERVATION_EXTRACTION.md
- PHASE_23_ANSWER_ENGINE.md
- PHASE_24_ANSWER_MEMORY.md
- PHASE_25_FORM_EXECUTION_ENGINE.md
- PHASE_26_APPLICATION_STATE_MACHINE.md
- PHASE_27_APPLICATION_ORCHESTRATOR.md
- PHASE_28_SUBMISSION_VERIFICATION.md
- PHASE_29_RECOVERY_ENGINE.md
- PHASE_30_LINKEDIN_APPLICATION_ADAPTER.md
- PHASE_31_INTERNSHALA_APPLICATION_ADAPTER.md
- PHASE_32_NAUKRI_APPLICATION_ADAPTER.md
- PHASE_33_INDEED_APPLICATION_ADAPTER.md
- PHASE_34_WELLFOUND_APPLICATION_ADAPTER.md
- PHASE_35_EMAIL_TRACKER.md
- PHASE_36_DASHBOARD_CRM_ANALYTICS.md
- PHASE_37_PRODUCTION_HARDENING_RELEASE.md

The names may be adjusted slightly for readability, but numbering and purpose must exactly match `TASKS.md`.

---

# 44. Phase 00 Validation Checklist

Before marking Phase 00 complete, verify:

- [ ] All ten project documents exist.
- [ ] All ten documents have been fully read.
- [ ] No major product contradiction exists.
- [ ] NORVI authentication is consistently documented.
- [ ] Ollama lifecycle is consistently documented.
- [ ] `gemma4:cloud` is consistently defined as the production model.
- [ ] Cloud AI privacy is documented correctly.
- [ ] Ollama ownership behavior is documented.
- [ ] Five initial job platforms are consistently defined.
- [ ] CandidateProfile is canonical.
- [ ] Job is canonical.
- [ ] Generic Application Engine is mandatory.
- [ ] Platform Adapter architecture is mandatory.
- [ ] Form Engine is generic.
- [ ] Submit does not equal success.
- [ ] Verification Engine owns VERIFIED_APPLIED.
- [ ] Recovery architecture exists.
- [ ] CAPTCHA requires user intervention.
- [ ] Email architecture is defined.
- [ ] Status separation is defined.
- [ ] Security rules are defined.
- [ ] Test strategy is defined.
- [ ] Phase numbering matches TASKS.md.
- [ ] Documentation wrappers/formatting mistakes are removed.
- [ ] `.env.example` contains no real secrets.
- [ ] `.gitignore` protects private runtime data.
- [ ] Source tree is ready for Phase 1.
- [ ] No production feature work was prematurely implemented.

---

# 45. Required Validation Commands

Where applicable, run basic repository checks.

Examples:

```powershell
python --version
git status