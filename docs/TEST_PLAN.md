# ROLVIO — TEST PLAN

## Purpose

This document defines what "working" means.

Code running without crashing does not prove correctness.

---

# 1. Test Levels

Rolvio uses:

1. Unit tests.
2. Integration tests.
3. Browser fixture tests.
4. End-to-end tests.
5. Platform regression tests.
6. Controlled real-platform smoke tests.
7. Clean-machine production tests.

---

# 2. NORVI Authentication Tests

Test:

- Valid email/password/authentication key.
- Invalid email.
- Invalid password.
- Invalid Authentication Key.
- Expired key.
- Revoked key.
- Disabled account.
- Product not authorized.
- Network unavailable.
- Backend timeout.
- Invalid backend response.
- Authentication retry.
- Secure token storage.
- Valid session reuse.
- Expired session.
- Logout.
- Restart after login.

Security assertions:

- Raw password is not persisted.
- Password never appears in logs.
- Authentication Key never appears in logs.
- Desktop application never contains production database credentials.

---

# 3. Ollama Installation Tests

Test:

- Ollama already installed.
- Ollama missing.
- Automatic installation succeeds.
- Installation failure.
- Installer missing/corrupt.
- Windows permission/UAC-required case.
- No visible CMD/PowerShell window from Rolvio.

---

# 4. Ollama Runtime Tests

Test:

- Ollama installed and already running.
- Ollama installed but stopped.
- Rolvio starts Ollama.
- API becomes healthy.
- Startup timeout.
- Ollama process crashes.
- User closes Ollama.
- Health monitor detects failure.
- Rolvio silently restarts runtime.
- Restart limit enforced.

---

# 5. Ollama Ownership Tests

Scenario A:

Ollama already running before Rolvio.

Expected:

- owned_by_rolvio = false.
- Rolvio shutdown does not stop Ollama.

Scenario B:

Ollama not running.

Rolvio starts it.

Expected:

- owned_by_rolvio = true.
- Rolvio shutdown stops Rolvio-owned runtime.

---

# 6. Ollama Cloud Authentication Tests

Test:

- Already signed in / cloud access ready.
- Sign-in required.
- One-time sign-in successful.
- Sign-in cancelled.
- Sign-in failure.
- Cloud authentication expired.
- Reauthentication.
- Network unavailable.

---

# 7. Model Tests

Required model:

`gemma4:cloud`

Test:

- Model available.
- Model not yet prepared.
- Automatic pull/preparation.
- Preparation failure.
- Health inference succeeds.
- Cloud network failure.
- Model unavailable.
- No silent fallback to different model.

---

# 8. Candidate Tests

Test:

- Profile creation.
- Profile update.
- Save/load.
- Skills.
- Experience.
- Education.
- Salary.
- Authorization.
- Notice period.
- Personal statement.
- Standard answers.

All information must survive persistence round-trips.

---

# 9. Resume Tests

Test:

- Valid PDF.
- Invalid PDF.
- Text extraction.
- Structured parsing.
- Original resume storage.
- File retrieval.
- Browser upload.
- Invalid file type.
- Invalid filename.

---

# 10. Job Normalization Tests

For every platform fixture verify:

- Job ID.
- Platform.
- Title.
- Company.
- URL.
- Description.
- Location.
- Work type.
- Salary.
- Apply type.

Test duplicate detection.

---

# 11. Matching Tests

Test:

- Strong skill match.
- Missing skills.
- Experience mismatch.
- Location mismatch.
- Authorization mismatch.
- Structured score.
- Invalid AI response.
- AI timeout.
- Ollama runtime unavailable.

---

# 12. Approval Policy Tests

Manual:

Never automatically apply.

Smart:

Respect configured thresholds.

Autonomous:

Respect all restrictions.

Test:

- Minimum score.
- Platform restrictions.
- Company blacklist.
- Location restrictions.
- Daily application limit.
- Role restrictions.

---

# 13. Fake Application Form Matrix

Build local fake pages for:

- Text.
- Email.
- Phone.
- Number.
- Textarea.
- Native select.
- Radio.
- Checkbox.
- Checkbox group.
- Custom dropdown.
- Combobox.
- Autocomplete.
- Date.
- File upload.
- Resume upload.
- Multiselect.
- Multi-step flow.
- Iframe.
- New tab.
- Validation error.
- Unexpected modal.

Every control must normalize correctly.

---

# 14. Answer Engine Tests

Test:

- Name from CandidateProfile.
- Email from CandidateProfile.
- Phone from CandidateProfile.
- Experience from CandidateProfile.
- Salary from CandidateProfile.
- Sponsorship from CandidateProfile.
- Saved answer.
- Equivalent prior question.
- AI-generated writing.
- Unknown factual question.

Unknown factual information must return:

`NEEDS_USER`

Never fabricate.

---

# 15. Form Filling Tests

Verify actual browser state after filling:

- Text.
- Number.
- Select.
- Radio.
- Checkbox.
- Custom select.
- Date.
- File.
- Resume.
- Multiselect.

---

# 16. Application State Tests

Valid example:

CREATED
→ QUEUED
→ STARTING
→ JOB_OPENED
→ SESSION_VALID
→ APPLICATION_STARTED
→ FORM_READY
→ FORM_FILLING
→ FORM_VALIDATING
→ REVIEWING
→ SUBMIT_REQUESTED
→ VERIFYING
→ VERIFIED_APPLIED

Invalid:

CREATED
→ VERIFIED_APPLIED

must be rejected.

---

# 17. Verification Tests

Submit clicked but validation error appears.

Expected:

NOT VERIFIED.

Submit clicked and confirmation page appears.

Expected:

VERIFIED_APPLIED.

Submit clicked but result is unclear.

Expected:

SUBMITTED_UNVERIFIED.

Already Applied detected.

Expected:

ALREADY_APPLIED.

Console contains:

`Application submitted successfully`

Expected:

No effect on business state.

---

# 18. Recovery Tests

Simulate:

- Popup.
- New tab.
- Iframe.
- Expired platform session.
- Validation error.
- Missing field.
- Network timeout.
- Element detached.
- Browser crash.
- Closed job.
- Unexpected application step.

Verify:

- Retry limits.
- Recovery attempt.
- Correct final state.
- Failure diagnostics.
- No infinite loop.

---

# 19. CAPTCHA Test

Expected:

- CAPTCHA detected.
- Application paused.
- State = CAPTCHA_REQUIRED.
- User notified.
- No bypass attempted.
- Application resumes after manual completion.

---

# 20. Job Platform Session Tests

Test:

- Login.
- Save session.
- Restore session.
- Detect expiration.
- Detect login redirect.
- Clear session.

Session-file existence must not automatically mean valid authentication.

---

# 21. Email Tests

Test:

- First scan.
- New email scan.
- UID persistence.
- Old emails ignored.
- Confirmation email.
- Assessment.
- Interview.
- Rejection.
- Offer.
- Irrelevant email.
- Ambiguous match.

Rolvio must not update the wrong application.

---

# 22. Database Tests

Test:

- Fresh database.
- Migration.
- Foreign keys.
- Transactions.
- Restart.
- Application-event persistence.
- Task persistence.

---

# 23. Dashboard Tests

Verify real state drives metrics.

Failed application must not count as Verified Applied.

Submitted Unverified must not count as Verified Applied.

---

# 24. LinkedIn Tests

Controlled real scenarios:

- Already applied.
- Easy Apply.
- Multi-step.
- Radio.
- Dropdown.
- Resume.
- Review.
- Verified submission.

---

# 25. Internshala Tests

Test:

- Eligible.
- Not eligible.
- Profile/resume step.
- Custom questions.
- Cover letter.
- Submit.

Critical:

Not Eligible must never become Verified Applied.

---

# 26. Naukri Tests

Test:

- Native apply.
- External redirect.
- Form fields.
- Custom questions.
- Verification.

Do not fill unrelated website controls.

---

# 27. Indeed Tests

Test:

- Indeed Apply.
- Iframe.
- Multi-step.
- Resume.
- Required questions.
- Human verification.
- Submission verification.

Important exceptions must never be silently ignored.

---

# 28. Wellfound Tests

Test:

- Apply.
- Interest question.
- URLs.
- Multi-step.
- New fields after Next.
- Verification.

Every step must be re-observed.

---

# 29. Failure Diagnostics Test

Force failure.

Verify creation of:

- Screenshot.
- Metadata.
- URL.
- Visible text.
- Trace.
- Page HTML where appropriate.

Ensure secrets are redacted.

---

# 30. Security Tests

Check:

- No secrets in Git.
- No raw password storage.
- Authentication Key absent from logs.
- Email password not plaintext DB data.
- Logs redact tokens.
- Browser sessions protected.
- File validation works.

---

# 31. Fresh Windows Test

On clean Windows:

1. Install Rolvio.
2. Launch.
3. Authenticate.
4. Detect missing Ollama.
5. Install Ollama.
6. Complete Ollama sign-in if needed.
7. Prepare `gemma4:cloud`.
8. Verify AI health.
9. Database initializes.
10. Playwright works.
11. UI works.
12. Profile saves.
13. Resume uploads.
14. Platform login works.
15. Job search works.
16. Controlled application works.
17. Close Rolvio.
18. Confirm only Rolvio-owned Ollama is stopped.

---

# 32. Release Blocking Issues

Release must stop if:

- Authentication can be bypassed unintentionally.
- Secrets leak.
- Ollama setup fails on clean machines.
- Ollama crash recovery is broken.
- Rolvio kills pre-existing Ollama.
- False application success occurs.
- Candidate facts are fabricated.
- Fresh installation fails.
- Critical tests fail.
- Browser failure generates no diagnostics.
- Supported platform application is fundamentally broken.

---

# 33. Definition of Tested

A feature is tested only when:

- Happy path passes.
- Failure path passes.
- Edge cases pass.
- Regression tests pass where relevant.
- Real user outcome is verified.