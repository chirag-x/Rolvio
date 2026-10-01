
---

# 5. `TASKS.md`

```markdown
# ROLVIO — MASTER DEVELOPMENT PHASES

## Development Rule

Complete one phase before moving to the next.

For each phase:

Read
→ Understand
→ Plan
→ Implement
→ Test
→ Review
→ Fix
→ Re-test
→ Report
→ Update Documentation

---

# PHASE 0 — PRODUCT & ARCHITECTURE

Goal:

Lock the complete Rolvio specification.

Tasks:

- Finalize PRD.
- Finalize architecture.
- Finalize design.
- Finalize rules.
- Finalize testing.
- Finalize security.
- Lock NORVI authentication behavior.
- Lock Ollama runtime behavior.
- Lock `gemma4:cloud`.
- Lock supported platforms.
- Lock application states.
- Lock submission verification.

Done when:

The ten documentation files have no major contradictions.

---

# PHASE 1 — PROJECT FOUNDATION

Build:

- Python 3.13.15 project.
- `.venv`.
- Requirements.
- Project paths.
- Configuration loader.
- Logging foundation.
- Error foundation.
- Basic launcher.
- pytest configuration.
- Basic PySide6 startup.

Done when:

Rolvio launches cleanly and the test suite runs.

---

# PHASE 2 — SECURITY & SECRET FOUNDATION

Build:

- CredentialStore abstraction.
- Windows secure credential integration.
- Secret handling.
- Token storage.
- Redaction.
- Secure configuration handling.
- Sensitive log filtering.

Done when:

Passwords, authentication tokens and email credentials do not require plaintext SQLite storage.

---

# PHASE 3 — NORVI AUTHENTICATION

Build:

- Auth models.
- NORVI API client.
- AuthService.
- Email/password/authentication-key login.
- Secure token/session handling.
- Session validation.
- Logout.
- Error mapping.
- Authentication tests.

Do NOT connect the desktop app directly to the production agency database.

Done when:

Valid users authenticate and invalid credentials/keys are handled correctly.

---

# PHASE 4 — OLLAMA RUNTIME MANAGER

Build:

- Ollama installation detection.
- Approved installer/downloader.
- Silent start.
- No CMD/PowerShell windows.
- Process detection.
- Process ownership.
- Health checks.
- Ollama sign-in requirement detection.
- One-time interactive Ollama sign-in flow.
- `gemma4:cloud` preparation/pull.
- Cloud-access health check.
- Crash/closure detection.
- Silent runtime restart.
- Graceful shutdown.
- Ownership-aware shutdown.
- Network failure handling.

Done when:

Ollama can be prepared automatically on a clean machine and recovered after an unexpected runtime failure.

---

# PHASE 5 — DOMAIN MODELS

Build:

- CandidateProfile.
- ResumeDocument.
- Job.
- JobMatch.
- Application.
- ApplicationEvent.
- FormField.
- ResolvedAnswer.
- VerificationResult.
- EmailEvent.
- BackgroundTask.
- PlatformSession.
- AuthSession.
- AIRuntimeState.
- Enums.

Add validation tests.

---

# PHASE 6 — DATABASE & REPOSITORIES

Build:

- SQLite.
- SQLAlchemy.
- Alembic.
- Database initialization.
- CandidateRepository.
- DocumentRepository.
- JobRepository.
- ApplicationRepository.
- AnswerRepository.
- EmailRepository.
- PlatformSessionRepository.
- TaskRepository.

Test fresh database initialization.

---

# PHASE 7 — AI GATEWAY

Build:

- AIGateway.
- OllamaProvider.
- `gemma4:cloud` configuration.
- Structured AI responses.
- Timeouts.
- Retries.
- Prompt registry.
- Validation.
- Guardrails.
- Fake AI provider for tests.

Done when:

Business modules never call Ollama directly.

---

# PHASE 8 — DESKTOP UI FOUNDATION

Build:

- Main window.
- Theme.
- Shared controls.
- Navigation system.
- Login view.
- Startup/preparation view.
- Sidebar.
- Cards.
- Tables.
- Badges.
- Dialogs.
- Loading states.
- Error states.

Connect Login UI to AuthService.

---

# PHASE 9 — BOOTSTRAP ORCHESTRATION

Build startup flow:

Application Start
→ Configuration
→ Authentication
→ Ollama Runtime
→ Database
→ Main UI

Implement:

- BootstrapManager.
- Service readiness.
- Startup progress.
- Startup failure handling.
- Graceful shutdown.
- Ollama ownership-aware shutdown.

---

# PHASE 10 — CANDIDATE PROFILE SYSTEM

Build:

- Personal details.
- Career data.
- Skills.
- Experience.
- Education.
- Projects.
- Certifications.
- Languages.
- Compensation.
- Preferences.
- Authorization.
- Standard answers.

Use one canonical CandidateProfile.

---

# PHASE 11 — RESUME & DOCUMENT SYSTEM

Build:

- PDF upload.
- PDF validation.
- Resume text extraction.
- Structured resume parsing.
- Original file retention.
- DocumentManager.
- Resume metadata.
- Upload-ready file path.

---

# PHASE 12 — PROFILE & DOCUMENT UI

Build:

- Profile sections.
- Save/load.
- Validation.
- Resume upload.
- Documents view.
- Standard answers.
- User-friendly errors.

---

# PHASE 13 — BROWSER RUNTIME

Build:

- Playwright BrowserManager.
- Chromium installation check.
- Browser context.
- Tabs.
- Frames.
- Navigation.
- Uploads.
- Screenshots.
- Browser mode.
- Timeouts.
- Artifact capture.

---

# PHASE 14 — JOB PLATFORM SESSION MANAGER

Build:

- Interactive platform login.
- Session save.
- Session restore.
- Session validation.
- Expired session detection.
- Login-required state.
- Platform session UI.

---

# PHASE 15 — PLATFORM ADAPTER FRAMEWORK

Build:

- PlatformAdapter interface.
- Platform registry.
- Capability model.
- Adapter loading.

Register:

- LinkedIn.
- Naukri.
- Internshala.
- Indeed.
- Wellfound.

---

# PHASE 16 — JOB NORMALIZATION

Build:

- RawPlatformJob.
- Canonical Job.
- URL normalization.
- Company normalization.
- Location normalization.
- Duplicate detection.

---

# PHASE 17 — JOB DISCOVERY ENGINE

Build generic discovery service:

- Search request.
- Multi-platform execution.
- Pagination.
- Search limits.
- Cancellation.
- Progress.
- Error isolation.
- Persistence.

---

# PHASE 18 — JOB SEARCH ADAPTERS

Implement job discovery for:

- LinkedIn.
- Naukri.
- Internshala.
- Indeed.
- Wellfound.

Run controlled search smoke tests.

---

# PHASE 19 — JOB MATCHING ENGINE

Build:

- Skill comparison.
- Experience comparison.
- Education comparison.
- Location compatibility.
- Authorization compatibility.
- Seniority compatibility.
- Semantic AI analysis.
- Overall match.
- Missing skills.
- Explanation.

---

# PHASE 20 — APPROVAL POLICY ENGINE

Build:

- Manual Mode.
- Smart Mode.
- Autonomous Mode.
- Match thresholds.
- Daily limits.
- Platform rules.
- Company blacklist.
- Location rules.
- Role rules.
- Salary rules.

---

# PHASE 21 — FORM FIELD MODEL

Create normalized types for:

- Text.
- Email.
- Phone.
- Number.
- Textarea.
- URL.
- Select.
- Custom Select.
- Radio.
- Checkbox.
- Checkbox Group.
- Combobox.
- Autocomplete.
- Multiselect.
- Date.
- File.
- Resume.
- Consent.
- Unknown.

---

# PHASE 22 — FORM OBSERVATION & EXTRACTION

Build:

- Form detection.
- Field extraction.
- Label extraction.
- Required-state detection.
- Current values.
- Options.
- Validation errors.
- Stable locator generation.

Build local fake application sites for testing.

---

# PHASE 23 — ANSWER ENGINE

Build:

- CandidateProfile lookup.
- Saved answer lookup.
- Semantic answer matching.
- Safe derivation.
- AI writing.
- Unknown factual detection.
- Confidence.
- User-confirmation requirement.
- Batch AI answering.

---

# PHASE 24 — ANSWER MEMORY

Build:

- Canonical question memory.
- Semantic aliases.
- User-confirmed answers.
- Confidence.
- Reuse policy.
- Edit/delete UI.

---

# PHASE 25 — FORM EXECUTION ENGINE

Implement:

- Text.
- Email.
- Phone.
- Number.
- Textarea.
- Select.
- Radio.
- Checkbox.
- Custom dropdown.
- Combobox.
- Autocomplete.
- Date.
- File upload.
- Resume upload.
- Multiselect.
- Consent.

Verify browser values after filling.

---

# PHASE 26 — APPLICATION STATE MACHINE

Build:

- States.
- Valid transitions.
- Persistence.
- Events.
- Pause.
- Resume.
- Cancel.
- Needs-user states.
- Failure states.

---

# PHASE 27 — APPLICATION ORCHESTRATOR

Build generic workflow:

Job
→ Session
→ Open Application
→ Observe
→ Resolve
→ Fill
→ Validate
→ Next
→ Review
→ Submit

Test against fake application sites.

---

# PHASE 28 — SUBMISSION VERIFICATION

Build:

- Generic success detection.
- URL signals.
- Confirmation text.
- Applied-state detection.
- Platform signals.
- Evidence model.
- VERIFIED_APPLIED.
- SUBMITTED_UNVERIFIED.
- ALREADY_APPLIED.

Critical rule:

Clicking Submit alone must never equal success.

---

# PHASE 29 — RECOVERY ENGINE

Build:

- PageSnapshot.
- Popup recovery.
- New-tab recovery.
- Iframe recovery.
- Validation recovery.
- Session-expired recovery.
- Retry budgets.
- User intervention.
- Failure diagnostics.

---

# PHASE 30 — LINKEDIN APPLICATION ADAPTER

Build:

- Easy Apply detection.
- Already-applied detection.
- Application state signals.
- Platform navigation.
- Verification signals.

Use generic form/application systems.

Run controlled real tests.

---

# PHASE 31 — INTERNSHALA APPLICATION ADAPTER

Build:

- Apply detection.
- Eligibility detection.
- Resume/profile step.
- Application signals.
- Verification.

Critical regression:

Not Eligible must never become Verified Applied.

---

# PHASE 32 — NAUKRI APPLICATION ADAPTER

Build:

- Apply detection.
- Native apply.
- External redirect detection.
- Form state.
- Verification.

---

# PHASE 33 — INDEED APPLICATION ADAPTER

Build:

- Indeed Apply.
- Iframe support.
- Multi-step navigation.
- Resume upload.
- Human-verification state.
- Verification.

Do not silently swallow errors.

---

# PHASE 34 — WELLFOUND APPLICATION ADAPTER

Build:

- Apply.
- Questions.
- Multi-step handling.
- Re-observe after Next.
- Resume behavior.
- Verification.

---

# PHASE 35 — EMAIL TRACKER

Build:

- Multiple email accounts.
- Secure credentials.
- IMAP.
- UID persistence.
- New-message processing.
- Classification.
- Application matching.
- Timeline updates.
- Ambiguous-match review.

---

# PHASE 36 — DASHBOARD, CRM & ANALYTICS

Build:

- Mission Control dashboard.
- Activity feed.
- Application tracker.
- Kanban.
- Email Tracker UI.
- Analytics.
- Platform metrics.
- Interview metrics.
- Failure metrics.

---

# PHASE 37 — PRODUCTION HARDENING & RELEASE

Perform:

- Unit suite.
- Integration suite.
- E2E suite.
- Authentication tests.
- Ollama lifecycle tests.
- Application regression tests.
- Real-platform smoke tests.
- Security review.
- Fresh Windows installation.
- Automatic Ollama installation test.
- Ollama sign-in test.
- Ollama crash recovery test.
- Database bootstrap.
- Playwright bootstrap.
- PyInstaller build.
- Clean Windows VM test.
- Graceful shutdown test.
- Final production validation.

Rolvio is complete only when real end-to-end validation succeeds.