
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
- README.md

Do not start coding before understanding the product.

---

# 2. Work Phase by Phase

Never attempt to build complete Rolvio in one prompt.

Workflow:

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

# 3. Architecture Is Mandatory

Follow ARCHITECTURE.md.

Do not create alternative architecture simply because it is easier.

If architecture must change:

1. Explain why.
2. Update DECISIONS.md.
3. Update ARCHITECTURE.md.
4. Then implement.

---

# 4. NORVI Authentication Rules

Rolvio requires authentication using:

- Email.
- Password.
- Authentication Key.

The desktop app must never connect directly to the NORVI production database.

Use the NORVI backend/API.

Never:

- Embed agency DB credentials.
- Store raw password.
- Log password.
- Log Authentication Key.
- Store Authentication Key in plaintext application logs.

Authentication tokens must use secure OS-backed storage.

---

# 5. Ollama Runtime Rules

Production runtime:

`Ollama`

Production model:

`gemma4:cloud`

Do not silently switch models.

Do not silently switch AI providers.

No CMD or PowerShell window should appear during normal Ollama startup/install/model preparation.

Windows-required UAC/security prompts are allowed when unavoidable.

---

# 6. Ollama Ownership Rule

Always detect whether Ollama was running before Rolvio.

If Rolvio starts Ollama:

Track:

`owned_by_rolvio = true`

If it was already running:

Track:

`owned_by_rolvio = false`

On shutdown:

Only stop Rolvio-owned Ollama runtime.

Never kill unrelated/pre-existing Ollama processes.

---

# 7. Ollama Recovery Rule

While Rolvio is running:

- Monitor Ollama health.
- Detect unexpected shutdown.
- Attempt limited silent restart.
- Recheck health.
- Pause AI-dependent work during recovery.
- Report failure clearly if recovery cannot succeed.

No infinite restart loop.

---

# 8. Cloud AI Privacy Rule

`gemma4:cloud` is cloud-hosted.

Do not describe production AI processing as fully local.

Send only relevant information required for the task.

Do not send unrelated local files or unrelated user data.

---

# 9. Keep Responsibilities Separate

UI must not contain:

- SQL.
- Playwright selectors.
- Scraping logic.
- Ollama process management.
- NORVI API implementation.
- AI prompts.
- IMAP parsing.

---

# 10. One CandidateProfile

There must be one canonical CandidateProfile.

Do not create separate profile dictionaries for platform runners.

---

# 11. One Job Model

Every platform normalizes jobs into the same Job model.

---

# 12. No Log Parsing

Never use console text as business state.

Forbidden:

```python
if "Application submitted successfully" in output:
    application.status = "applied"