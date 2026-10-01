# ROLVIO — PRODUCT REQUIREMENTS DOCUMENT

## Product Name

Rolvio

## Product Type

Autonomous AI Job Search, Matching, Application and Career Tracking Agent

## Brand

NORVI

## Platform

Windows 11 Desktop Application

## Primary Language

Python 3.13.15

---

# 1. Product Vision

Rolvio is a personal AI career agent designed to manage the complete job-search workflow for a single user.

The user should configure Rolvio once with their professional information and then use one application to manage:

Job Discovery
→ Job Matching
→ Approval
→ Automatic Application
→ Submission Verification
→ Email Tracking
→ Assessment
→ Interview
→ Offer / Rejection
→ Analytics

Rolvio must not behave like a simple auto-clicker.

It should behave like an intelligent career operator that understands the user, understands jobs, understands application forms, executes applications safely, verifies results, and tracks what happens afterward.

---

# 2. Main User Problems

Job searching is repetitive and fragmented.

Users normally have to:

- Search multiple websites.
- Read hundreds of job descriptions.
- Decide whether jobs fit their profile.
- Fill the same information repeatedly.
- Upload resumes repeatedly.
- Answer the same questions repeatedly.
- Track applications manually.
- Monitor emails.
- Track assessments.
- Track interviews.
- Track offers and rejections.

Many existing auto-apply systems are unreliable because they:

- Depend on fragile selectors.
- Fill incorrect answers.
- Invent candidate information.
- Cannot handle dynamic forms.
- Cannot recover when websites change.
- Mark applications successful without verification.
- Cannot track the full recruitment lifecycle.

Rolvio must solve these problems as one integrated product.

---

# 3. Target Users

Rolvio is designed for:

- Students.
- Fresh graduates.
- Entry-level candidates.
- Software developers.
- Engineers.
- Technology professionals.
- Remote job seekers.
- Professionals changing companies.
- Users applying to many jobs.
- Users who want to reduce repetitive job-search work.

Rolvio must be usable without programming knowledge.

---

# 4. Core Product Principles

## 4.1 Verification Before Success

Clicking a Submit button does not prove an application succeeded.

Only the Verification Engine may mark an application:

`VERIFIED_APPLIED`

If submission happened but success cannot be confirmed, use:

`SUBMITTED_UNVERIFIED`

Rolvio must prefer uncertainty over false success.

---

## 4.2 Never Invent Important Candidate Information

Rolvio must never fabricate:

- Experience.
- Employment history.
- Salary.
- Education.
- Certifications.
- Citizenship.
- Visa status.
- Sponsorship.
- Security clearance.
- Notice period.
- Work authorization.

If important factual information is unknown, Rolvio should ask the user.

---

## 4.3 Observe Before Acting

Important browser operations must follow:

Observe
→ Understand
→ Act
→ Verify

Rolvio must not blindly execute a fixed sequence of clicks.

---

## 4.4 Recover Instead of Guessing

When the page differs from what Rolvio expected:

1. Inspect the actual page.
2. Capture useful evidence.
3. Determine the current state.
4. Attempt safe recovery.
5. Re-observe.
6. Continue when confidence is sufficient.
7. Ask the user when autonomous recovery is unsafe.

---

# 5. NORVI Authentication

Rolvio requires authentication before the user can access the main application.

The login screen must collect:

- Email.
- Password.
- Authentication Key.

The desktop application must NOT connect directly to the NORVI production database.

Authentication must happen through the NORVI backend/API.

The NORVI backend may access the agency database internally.

The desktop application sends authentication information only to the official NORVI authentication endpoint over secure HTTPS.

---

# 6. Authentication Startup Behavior

When Rolvio starts:

1. Check whether a valid secure Rolvio authentication session already exists.
2. If a valid session exists, verify it with the NORVI backend when required.
3. If no valid session exists, display the Rolvio Login screen.
4. User enters:
   - Email.
   - Password.
   - Authentication Key.
5. Rolvio sends the authentication request to the NORVI backend.
6. Backend validates:
   - Account.
   - Password.
   - Authentication Key.
   - Product access.
   - Account/key status.
7. If valid, continue startup.
8. If invalid, deny access and show a clear error.

The raw password must never be stored locally.

The Authentication Key must be handled as sensitive information and must never appear in normal logs.

Secure authentication tokens may be stored using protected Windows credential storage.

---

# 7. Authentication Failure States

Possible authentication states include:

- AUTH_REQUIRED
- AUTHENTICATING
- AUTHENTICATED
- INVALID_CREDENTIALS
- INVALID_AUTH_KEY
- KEY_EXPIRED
- KEY_REVOKED
- ACCOUNT_DISABLED
- SERVER_UNAVAILABLE
- NETWORK_UNAVAILABLE
- AUTH_ERROR

Authentication errors must not corrupt local Rolvio data.

---

# 8. Ollama AI Runtime

Rolvio's production AI runtime is:

**Ollama**

The required model is:

**`gemma4:cloud`**

This is a cloud-hosted Ollama model accessed through the local Ollama application/runtime.

The model must not require the customer's GPU to perform main model inference.

Rolvio must not silently switch to another AI model or provider.

Changing the production model requires an explicit project decision and documentation update.

---

# 9. Ollama First-Run Setup

When Rolvio starts on a machine for the first time:

1. Check whether Ollama is installed.
2. If Ollama is not installed:
   - Download the approved Ollama installer.
   - Install Ollama automatically where permitted.
   - Do not display CMD or PowerShell windows.
   - Windows UAC/security prompts may appear if the operating system requires them.
3. Start Ollama silently in the background.
4. Check whether Ollama Cloud authentication is usable.
5. If the user must sign into Ollama:
   - Show a one-time setup message.
   - Open the required Ollama sign-in experience.
   - Allow the user to sign into Ollama.
6. After sign-in succeeds, continue Rolvio setup.
7. Ensure `gemma4:cloud` is available to Ollama.
8. If required, trigger the model pull/preparation in the background.
9. Run an AI health check.
10. Continue to the main Rolvio application only when required services are ready.

Technical console windows must not be shown to the user.

---

# 10. Ollama Normal Startup

On later launches:

1. Detect Ollama installation.
2. Detect whether Ollama is already running.
3. If not running, start it silently.
4. Verify Ollama API health.
5. Verify cloud-model access.
6. Verify `gemma4:cloud`.
7. Continue Rolvio startup.

The user should normally not see Ollama setup screens after the initial configuration.

---

# 11. Ollama Runtime Ownership

Rolvio must track whether Ollama was already running before Rolvio launched.

If Ollama was already running:

`owned_by_rolvio = false`

If Rolvio starts Ollama:

`owned_by_rolvio = true`

When Rolvio exits:

- If `owned_by_rolvio = true`, Rolvio may stop the Ollama process/runtime it started.
- If `owned_by_rolvio = false`, Rolvio must leave the user's existing Ollama runtime running.

Rolvio must never terminate an unrelated Ollama process merely because the Rolvio UI is closing.

---

# 12. Ollama Health Monitoring

While Rolvio is running, an Ollama Runtime Manager must periodically verify:

- Ollama process state.
- Ollama API health.
- Cloud authentication/access.
- `gemma4:cloud` accessibility.

If Ollama crashes or is accidentally closed while Rolvio is running:

1. Detect the failure.
2. Attempt a silent restart.
3. Re-check health.
4. Resume queued AI work when healthy.
5. If recovery fails, show a user-friendly AI Service error.

No CMD or PowerShell window should appear.

Retries must be limited.

---

# 13. Ollama Network Failure

Because the production model is cloud-hosted, internet access is required for AI inference.

Possible states:

- AI_READY
- AI_STARTING
- AI_AUTH_REQUIRED
- AI_NETWORK_UNAVAILABLE
- AI_MODEL_UNAVAILABLE
- AI_RUNTIME_ERROR

If internet access is unavailable:

- Do not fabricate AI results.
- Pause tasks requiring AI.
- Keep non-AI features available where practical.
- Retry according to policy.
- Inform the user clearly.

---

# 14. AI Privacy Boundary

`gemma4:cloud` is a cloud model.

Relevant AI prompts may leave the user's PC and be processed by the Ollama cloud service.

Rolvio must minimize AI payloads and send only information needed for the requested task.

Possible AI inputs include:

- Relevant resume-derived context.
- Relevant candidate profile fields.
- Job descriptions.
- Application questions.
- Relevant email excerpts when email classification requires AI.

Rolvio must not send unrelated local files or unrelated personal information.

---

# 15. Candidate Profile

Rolvio must maintain one canonical CandidateProfile.

The profile should contain:

## Personal Information

- Full name.
- Email.
- Phone.
- Location.
- Country.

## Online Presence

- LinkedIn.
- GitHub.
- Portfolio.
- Personal website.
- Other relevant URLs.

## Career Information

- Current role.
- Current company.
- Total experience.
- Current salary.
- Expected salary.
- Notice period.
- Available start date.

## Education

- Degree.
- College/university.
- Major.
- Graduation year.
- GPA/CGPA.
- 12th information.
- 10th information.

## Skills

- Skill name.
- Experience with skill.
- Skill category.

## Projects

- Name.
- Description.
- Technologies.
- URL.

## Certifications

- Certification.
- Issuing organization.
- Year.

## Languages

- Language.
- Proficiency.

## Work Preferences

- Remote.
- Hybrid.
- On-site.
- Preferred locations.
- Willingness to relocate.
- Preferred job roles.

## Work Authorization

- Citizenship.
- Visa status.
- Sponsorship requirement.

## Application Answers

- Standard answers.
- Custom answers.
- User-confirmed answers.

Every subsystem must use this canonical CandidateProfile.

---

# 16. Resume & Document System

Initial version must support:

- PDF resume upload.
- Resume text extraction.
- Structured resume parsing.
- Skill extraction.
- Experience extraction.
- Education extraction.
- Project extraction.
- Original file retention.
- Resume upload during applications.

The architecture should support future:

- Multiple resumes.
- Role-specific resumes.
- DOCX.
- Cover letters.
- Certificates.
- Portfolio documents.

---

# 17. Supported Job Platforms

Initial supported platforms:

1. LinkedIn.
2. Naukri.
3. Internshala.
4. Indeed.
5. Wellfound.

Future adapter architecture should support:

- Shine.
- TimesJobs.
- Hirist.
- Freshersworld.
- Glassdoor.
- Remotive.
- Other job platforms.
- External ATS systems.

Adding a platform must not require rewriting Rolvio Core.

---

# 18. Job Discovery

The user must be able to configure:

- Target roles.
- Search keywords.
- Location.
- Remote preference.
- Platforms.
- Maximum jobs.
- Minimum match score.
- Experience level.
- Employment type.

Each platform adapter returns raw jobs.

The Job Normalizer converts raw jobs into one canonical Job model.

---

# 19. Canonical Job Model

A normalized job should include:

- Internal ID.
- Platform.
- Platform Job ID.
- Job URL.
- Title.
- Company.
- Description.
- Location.
- Remote/hybrid/on-site type.
- Employment type.
- Salary where available.
- Required experience.
- Required skills.
- Posted date.
- Application type.
- Discovery timestamp.
- Raw platform metadata.

---

# 20. Job Matching Engine

Rolvio compares the Job with CandidateProfile.

Matching should consider:

- Skills.
- Experience.
- Education.
- Location.
- Work preference.
- Salary.
- Seniority.
- Authorization.
- Job role.
- Technologies.

Match result should include:

- Overall score.
- Skill score.
- Experience score.
- Education score.
- Location compatibility.
- Authorization compatibility.
- Strong matches.
- Missing skills.
- Risks.
- Explanation.

The result must be structured.

---

# 21. Approval Modes

Rolvio supports:

## Manual Mode

Every application requires user approval.

## Smart Mode

User-configurable thresholds decide:

- Auto-approve.
- Request approval.
- Ignore.

## Autonomous Mode

Rolvio may automatically apply according to explicit user rules.

Even Autonomous Mode must respect:

- Minimum match score.
- Maximum applications.
- Allowed platforms.
- Location restrictions.
- Job roles.
- Company exclusions.
- Salary expectations.
- Work-type preference.

---

# 22. Application Engine

The Application Engine must support:

- Job-page opening.
- Session verification.
- Already-applied detection.
- Closed-job detection.
- Application opening.
- Modal detection.
- New-tab detection.
- Iframe detection.
- Multi-step forms.
- Form extraction.
- Answer resolution.
- Resume/document upload.
- Validation handling.
- Review step.
- Submit step.
- Submission verification.

---

# 23. Supported Form Controls

Rolvio should understand:

- Text.
- Email.
- Phone.
- Number.
- Textarea.
- URL.
- Native select.
- Custom select.
- Radio.
- Checkbox.
- Checkbox group.
- Combobox.
- Autocomplete.
- Multi-select.
- Date.
- File upload.
- Resume upload.
- Consent field.
- Unknown control.

---

# 24. Answer Resolution

Answer priority:

1. Exact CandidateProfile value.
2. Saved user answer.
3. Previously confirmed equivalent answer.
4. Safe deterministic derivation.
5. AI-generated writing answer.
6. Ask user.

AI-generated writing may be used for:

- Cover letters.
- Motivation answers.
- "Why this role?"
- "Tell us about yourself."

AI must never invent factual qualifications.

---

# 25. Answer Memory

Rolvio should store user-confirmed reusable answers.

Equivalent questions should map to the same semantic answer when confidence is sufficient.

The user must be able to review, edit and delete remembered answers.

---

# 26. Application State Machine

Application states may include:

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

Every meaningful transition must be recorded.

---

# 27. Submission Verification

Verification evidence may include:

- Confirmation page.
- Success message.
- URL change.
- Applied-state button.
- Application history.
- Application identifier.
- Platform-specific confirmation signal.

Possible final verification results:

- VERIFIED_APPLIED
- ALREADY_APPLIED
- SUBMITTED_UNVERIFIED
- FAILED
- NEEDS_USER

Only VERIFIED_APPLIED and ALREADY_APPLIED count as confirmed applications.

---

# 28. Recovery Engine

When execution fails, Rolvio should inspect:

- URL.
- Page title.
- Visible text.
- Buttons.
- Inputs.
- Validation errors.
- Frames.
- Tabs.
- Screenshot.
- Application state.
- Recent actions.

Recovery may:

- Retry.
- Re-observe.
- Switch tab.
- Switch iframe.
- Fill missing fields.
- Refresh when safe.
- Ask the user.
- Fail safely.

No infinite retry loops are allowed.

---

# 29. CAPTCHA Policy

Rolvio must not attempt to automatically bypass CAPTCHA.

When detected:

1. Pause application.
2. Set CAPTCHA_REQUIRED.
3. Notify user.
4. Open visible browser when needed.
5. User completes verification.
6. Rolvio re-observes.
7. Resume safely.

---

# 30. Job Platform Sessions

Job-platform authentication is separate from NORVI authentication and Ollama authentication.

Users manually log into supported job platforms.

Rolvio stores reusable browser sessions securely.

Session states include:

- CONNECTED
- EXPIRED
- LOGIN_REQUIRED
- ERROR

A session file existing does not prove the session is still valid.

---

# 31. Email Tracker

Rolvio should support multiple email accounts.

Requirements:

- Secure credential storage.
- IMAP.
- UID persistence.
- Process only new messages.
- Job-email filtering.
- AI classification.
- Application matching.
- Timeline updates.
- Ambiguous-match review.

Email categories:

- Application confirmation.
- Recruiter communication.
- Assessment.
- Interview invitation.
- Interview schedule.
- Rejection.
- Offer.
- Other job-related.
- Irrelevant.

---

# 32. Email Matching

Use multiple signals:

- Company.
- Job title.
- Sender domain.
- Platform.
- Application date.
- Email thread.
- Job identifiers.

Low-confidence matches must be shown for review rather than silently updating the wrong application.

---

# 33. Dashboard

The dashboard should show:

- Jobs discovered.
- Strong matches.
- Pending approvals.
- Applications queued.
- Applications running.
- Verified applications.
- Needs-attention applications.
- Assessments.
- Interviews.
- Offers.
- Employer rejections.
- Recent activity.
- Platform performance.
- Response rate.
- Interview rate.

---

# 34. Application Tracker

Recruitment flow should distinguish:

Applied
→ Assessment
→ Interview
→ Offer

and:

Applied
→ Employer Rejected

User rejection of a job must not use the same state as employer rejection.

---

# 35. Analytics

Analytics should include:

- Jobs discovered.
- Applications per day/week.
- Applications per platform.
- Verified application rate.
- Response rate.
- Interview rate.
- Offer rate.
- Average match score.
- Best-performing roles.
- Best-performing platforms.
- Common requested skills.
- Missing skills.
- Failure reasons.

---

# 36. Background Task Manager

Task types:

- Authentication refresh.
- AI runtime health.
- Job discovery.
- Matching.
- Application execution.
- Email scanning.
- Analytics.
- Maintenance.

Task states:

- QUEUED
- RUNNING
- PAUSED
- WAITING_FOR_USER
- COMPLETED
- FAILED
- CANCELLED

---

# 37. Diagnostics

Important browser failures should generate evidence such as:

- Screenshot.
- Page HTML.
- Visible text.
- Current URL.
- State.
- Trace.
- Error details.

Sensitive values should be redacted where practical.

---

# 38. Privacy

Sensitive data includes:

- Resume.
- Email.
- Phone.
- Salary.
- Application answers.
- Browser sessions.
- Email credentials.
- Authentication Key.
- Rolvio authentication tokens.
- Job history.

Sensitive data must never be committed to Git.

---

# 39. Out of Scope for First Production Release

Initial release does not require:

- Mobile app.
- Social network.
- Community.
- Employer-side recruitment system.
- CAPTCHA bypass.
- Automatic job-offer acceptance.
- Automatic salary negotiation.
- Automatic interview answering.
- Support for every ATS on the internet.
- Full resume builder.

---

# 40. Product Success Criteria

Rolvio is production-ready only when a user can:

1. Install Rolvio.
2. Open Rolvio.
3. Authenticate with NORVI.
4. Complete Ollama first-run setup if necessary.
5. Have Ollama run silently afterward.
6. Create a candidate profile.
7. Upload a resume.
8. Connect a job platform.
9. Search jobs.
10. Receive useful job matches.
11. Approve a job.
12. Start an application.
13. Correctly complete common form controls.
14. Upload the correct resume.
15. Navigate multi-step applications.
16. Ask the user for unknown important information.
17. Submit.
18. Verify submission.
19. Persist correct application state.
20. Monitor recruiter emails.
21. Track interviews/offers/rejections.
22. Display correct dashboard analytics.
23. Recover from Ollama runtime crashes.
24. Shut down Rolvio-owned Ollama cleanly when Rolvio exits.

The project is not complete merely because the code runs.