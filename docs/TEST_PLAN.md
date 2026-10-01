# ROLVIO — TEST PLAN

## Purpose

This document defines what "working" means.

Code running without crashing does not mean the product works correctly.

---

# 1. Test Levels

Rolvio should use:

1. Unit tests
2. Integration tests
3. Browser fixture tests
4. End-to-end tests
5. Platform regression tests
6. Real-platform smoke tests
7. Clean-machine production tests

---

# 2. Candidate Tests

Test:

- Profile creation
- Profile update
- Save/load
- Skills
- Experience
- Education
- Salary
- Authorization
- Notice period
- Personal statement
- Standard answers

All information must survive database round-trips.

---

# 3. Resume Tests

Test:

- Valid PDF
- Invalid PDF
- Text extraction
- Structured parsing
- Original resume storage
- File retrieval
- Browser upload
- Invalid file type
- Invalid filename

---

# 4. Job Normalization Tests

For each platform:

Verify:

- Job ID
- Platform
- Title
- Company
- URL
- Description
- Location
- Work type
- Salary
- Apply type

Test duplicates.

---

# 5. Matching Tests

Test:

- Strong skill match
- Missing skills
- Experience mismatch
- Location mismatch
- Work authorization mismatch
- Appropriate score structure
- Invalid AI response
- AI timeout

---

# 6. Approval Policy Tests

Manual:

Never automatically apply.

Smart:

Respect configured thresholds.

Autonomous:

Respect all configured restrictions.

Test:

- Minimum score
- Platform restrictions
- Company blacklist
- Location restrictions
- Daily application limit

---

# 7. Fake Application Forms

Create fake browser pages covering:

## Simple Text

Name
Email
Phone

## Number

Years of experience

## Textarea

Why do you want this role?

## Dropdown

Notice period

## Radio

Work authorization

## Checkbox

Consent

## Checkbox Group

Skills

## Custom Dropdown

React-style control

## Combobox

Searchable option

## Autocomplete

Location

## Date

Available start date

## File

Document upload

## Resume

Resume upload

## Multi-Step

Next
Next
Review
Submit

## Iframe

Application inside iframe

## New Tab

Application opens in new tab

## Validation Error

Required field missing

## Unexpected Modal

Additional confirmation

Every form type must be detected correctly.

---

# 8. Answer Engine Tests

Test:

- Name from profile
- Email from profile
- Phone from profile
- Experience from profile
- Salary from profile
- Sponsorship from profile
- Saved answer
- Equivalent previous question
- AI writing answer
- Unknown factual question

Unknown factual question should return:

NEEDS_USER

It must never fabricate a value.

---

# 9. Form Filling Tests

After filling:

Verify actual browser value.

Test:

- Text
- Number
- Select
- Radio
- Checkbox
- Custom dropdown
- Date
- File
- Resume
- Multi-select

---

# 10. Application State Tests

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

Invalid example:

CREATED
→ VERIFIED_APPLIED

must fail.

---

# 11. Verification Tests

Critical test:

Submit button clicked but form shows validation error.

Expected:

NOT VERIFIED.

Submit clicked and success page appears.

Expected:

VERIFIED_APPLIED.

Submit clicked but result unclear.

Expected:

SUBMITTED_UNVERIFIED.

Already applied detected.

Expected:

ALREADY_APPLIED.

Console says:

Application submitted successfully.

Expected:

No effect on application status.

---

# 12. Recovery Tests

Simulate:

- Popup
- New tab
- Iframe
- Expired session
- Validation error
- Missing required field
- Network timeout
- Removed DOM element
- Browser crash
- Job closed
- Unexpected application step

Verify:

- Retry limit
- Recovery attempt
- Correct state
- Failure diagnostics
- No infinite loop

---

# 13. CAPTCHA Test

Expected:

- Detect CAPTCHA
- Pause application
- Set CAPTCHA_REQUIRED
- Ask user
- Do not bypass CAPTCHA
- Resume after manual completion

---

# 14. Session Tests

Test:

- Login
- Save session
- Restore session
- Detect expired session
- Detect login redirect
- Clear session

A session file alone must not count as valid login.

---

# 15. Email Tests

Test:

- First scan
- New email scan
- UID persistence
- Old email ignored
- Application confirmation
- Assessment
- Interview
- Rejection
- Offer
- Irrelevant email

Test ambiguous matching.

Rolvio must not modify the wrong application.

---

# 16. Database Tests

Test:

- Fresh database
- Migration
- Foreign keys
- Transactions
- Restart
- Application event persistence
- Task persistence

---

# 17. Dashboard Tests

Verify metrics reflect real database state.

Failed application must not count as Verified Applied.

Submitted Unverified must not count as Verified Applied.

---

# 18. LinkedIn Tests

Test real controlled examples for:

- Already applied
- Easy Apply
- Multi-step
- Radio question
- Dropdown
- Resume
- Review
- Successful verification

---

# 19. Internshala Tests

Test:

- Eligible
- Not eligible
- Resume/profile step
- Custom questions
- Cover letter
- Submit

Critical:

Not Eligible must never become Applied.

---

# 20. Naukri Tests

Test:

- Native apply
- External redirect
- Form fields
- Custom questions
- Verification

Do not fill unrelated website inputs.

---

# 21. Indeed Tests

Test:

- Indeed Apply
- Iframe
- Multi-step
- Resume
- Required questions
- Human verification
- Submission verification

Important exceptions must never be silently ignored.

---

# 22. Wellfound Tests

Test:

- Apply
- Interest question
- URLs
- Multi-step
- New field after Next
- Verification

Every new step must be observed again.

---

# 23. Failure Diagnostics Test

Force a failure.

Verify generation of:

- Screenshot
- Metadata
- URL
- Visible text
- Trace
- Page HTML when appropriate

---

# 24. Security Tests

Check:

- No secrets in Git
- Email password not plaintext DB value
- Logs redact secrets
- Sessions protected
- File validation works

---

# 25. Fresh Windows Test

On clean Windows environment:

1. Install.
2. Launch.
3. Database initializes.
4. Playwright works.
5. UI works.
6. Profile saves.
7. Resume uploads.
8. Platform login works.
9. Job search works.
10. Controlled application works.

---

# 26. Release Blocking Issues

Release must stop if:

- False application success occurs.
- Candidate information is fabricated.
- Plaintext secrets exist.
- Fresh installation fails.
- Critical tests fail.
- Browser failures provide no diagnostics.
- Supported platform application is fundamentally broken.

---

# 27. Definition of Tested

A feature is tested only when:

- Happy path passes.
- Failure path passes.
- Edge cases pass.
- Regression tests pass where relevant.
- Actual user outcome is verified.