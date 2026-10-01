
---

# 4. `RULES.md`

```markdown
# ROLVIO — DEVELOPMENT RULES

These rules apply to every coding AI and every developer working on Rolvio.

---

# 1. Read Documentation First

Before coding, read:

- PRD.md
- ARCHITECTURE.md
- DESIGN.md
- RULES.md
- TASKS.md
- DECISIONS.md
- MEMORY.md
- TEST_PLAN.md
- SECURITY.md

Do not start coding before understanding the project.

---

# 2. Work Phase by Phase

Never attempt to build the complete Rolvio project in one prompt.

Use:

Understand
→ Plan
→ Implement
→ Test
→ Review
→ Fix
→ Test Again
→ Report
→ Update Documentation

---

# 3. Follow Architecture

ARCHITECTURE.md is mandatory.

Do not create another architecture simply because it is easier.

If architecture must change:

1. Explain why.
2. Update DECISIONS.md.
3. Update ARCHITECTURE.md.
4. Then implement.

---

# 4. Keep Responsibilities Separate

UI must not contain:

- SQL
- Playwright selectors
- Scraping
- AI prompts
- Email parsing

Browser modules must not contain:

- Dashboard code
- Analytics code
- Database schema logic

---

# 5. One Candidate Profile

There must be one canonical CandidateProfile.

Do not create different profile dictionaries for different runners.

---

# 6. One Job Model

Every platform must normalize jobs into the same Job model.

---

# 7. No Log Parsing

Never use console strings as business logic.

Forbidden:

if "Application submitted successfully" in output:
    application.status = "applied"

Use structured result objects.

---

# 8. Submit Does Not Equal Success

Clicking Submit means:

SUBMIT_REQUESTED

It does not mean:

VERIFIED_APPLIED

Only Verification Engine decides success.

---

# 9. Never Invent Candidate Information

Never fabricate:

- Experience
- Employment
- Salary
- Education
- Visa
- Sponsorship
- Certifications
- Security clearance

Ask the user when required information is unknown.

---

# 10. AI Writing Is Allowed

AI may create:

- Cover letters
- Motivation answers
- Why this role
- About yourself

It must use real information from the Candidate Profile.

---

# 11. No Unsafe Defaults

Never do:

Every Yes/No → Yes

Never do:

Dropdown failed → choose second option

Never do:

Radio failed → choose first option

Never do:

Unknown experience → invent value

---

# 12. Platform Logic Must Stay in Platform Adapters

LinkedIn-specific selectors belong only inside LinkedIn adapter files.

Same for other platforms.

---

# 13. Build Generic Systems First

Do not create separate full application systems per platform.

Build:

- Generic Form Engine
- Generic Answer Engine
- Generic Application State Machine
- Generic Verification Engine
- Generic Recovery Engine

Then create adapters.

---

# 14. Browser Rule

Every meaningful browser operation should follow:

Observe
→ Act
→ Verify

---

# 15. Avoid Fixed Sleeps

Prefer waiting for real conditions.

Avoid relying on:

wait_for_timeout(5000)

when Playwright can wait for:

- element
- navigation
- modal
- URL change
- state change

---

# 16. Never Silently Ignore Important Exceptions

Avoid:

except Exception:
    pass

Important errors must be recorded.

---

# 17. Retry Limits

Every retry loop requires:

- Maximum attempts
- Timeout
- Failure condition

No infinite loops.

---

# 18. User Intervention

When user action is needed:

Set:

NEEDS_USER

Do not simply sleep for several minutes.

---

# 19. CAPTCHA

Do not bypass CAPTCHA.

Pause and request user action.

---

# 20. Headless Mode

If user interaction is required, Rolvio must not keep waiting in an invisible browser.

Pause and make the browser visible or request user action.

---

# 21. Database

Database access must go through repositories/services.

No random SQL inside UI or platform code.

---

# 22. Migrations

Database schema changes require migrations.

---

# 23. AI Responses

Validate AI output before using it.

Prefer structured JSON/Pydantic schemas.

Do not allow malformed AI output to control the browser.

---

# 24. Model Names

Do not hard-code model names throughout the application.

Model configuration belongs in AIGateway.

---

# 25. Security

Never commit:

- Passwords
- API keys
- Cookies
- Email credentials
- Browser sessions
- User resumes

---

# 26. Logging

Do not log full:

- Passwords
- Tokens
- Cookies
- Resumes
- Email bodies

---

# 27. UI

Follow DESIGN.md.

Every page should have:

- Loading state
- Empty state
- Error state
- Success state

---

# 28. Testing

Important functionality requires tests.

Application automation changes require browser tests.

---

# 29. Real Platform Testing

A platform is not finished because local fake tests pass.

Controlled real-platform smoke testing is required.

---

# 30. Regression Tests

When a reproducible bug is fixed, add a regression test.

---

# 31. Failure Diagnostics

When application automation fails, save useful evidence.

Do not leave only:

Button not found.

Save:

- Screenshot
- URL
- Page title
- Visible text
- DOM where useful
- Application state
- Recent actions

---

# 32. No Unrelated Refactoring

Do not change unrelated systems while completing one task.

---

# 33. Git Commits

Use meaningful commit messages.

Good:

feat: add candidate profile service

fix: verify application confirmation

test: add radio-field regression

Bad:

fixing

done

update

---

# 34. Documentation

After phase completion:

Update:

- TASKS.md
- MEMORY.md

Update DECISIONS.md when permanent technical decisions change.

---

# 35. Definition of Done

A phase is only DONE when:

- Required code exists.
- Acceptance criteria pass.
- Tests pass.
- Important error cases pass.
- No critical bug remains.
- Documentation is updated.