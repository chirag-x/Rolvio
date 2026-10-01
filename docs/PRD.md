# ROLVIO — PRODUCT REQUIREMENTS DOCUMENT

## Product Name

Rolvio

## Product Type

Autonomous AI Job Search, Matching, Application and Career Tracking Agent

## Brand

NORVI

## Platform

Windows Desktop Application

---

# 1. Product Vision

Rolvio is a personal AI career agent designed to handle the complete job-search workflow for a single user.

The user should configure Rolvio once by providing:

- Personal information
- Resume
- Skills
- Education
- Work experience
- Projects
- Certifications
- Career preferences
- Salary preferences
- Work authorization
- Job preferences
- Standard application answers

After configuration, Rolvio should be able to:

1. Search for jobs across supported job platforms.
2. Read and understand job descriptions.
3. Compare jobs with the user's profile and resume.
4. Calculate job match scores.
5. Show suitable jobs to the user.
6. Automatically approve jobs according to user settings.
7. Apply for jobs on behalf of the user.
8. Correctly fill application forms.
9. Upload resumes and documents when required.
10. Handle multi-step application forms.
11. Detect when information is missing.
12. Ask the user instead of inventing important information.
13. Verify whether an application was actually submitted.
14. Track submitted applications.
15. Monitor job-related emails.
16. Detect assessments.
17. Detect interview invitations.
18. Detect rejections.
19. Detect offers.
20. Show everything in one beautiful dashboard.

Rolvio must not be designed as a simple script that blindly clicks Apply buttons.

Rolvio should behave like an intelligent job-search operator.

---

# 2. Problem

Job searching requires a large amount of repetitive work.

A typical user has to:

- Search multiple job platforms.
- Open many job listings.
- Read long job descriptions.
- Check whether they match the role.
- Fill the same information repeatedly.
- Upload resumes repeatedly.
- Answer common questions repeatedly.
- Track applications manually.
- Check emails for recruiter responses.
- Track assessments and interviews.

Most auto-apply tools are unreliable because they:

- Depend heavily on fixed CSS selectors.
- Cannot understand unexpected forms.
- Cannot recover from changed website layouts.
- Fill wrong answers.
- Cannot handle all form controls.
- Incorrectly report applications as successful.
- Cannot properly track the application after submission.

Rolvio must solve these problems.

---

# 3. Target Users

Rolvio is designed for:

- Students
- Fresh graduates
- Entry-level candidates
- Software developers
- Engineers
- Technology professionals
- Remote job seekers
- Professionals changing jobs
- Users applying to many jobs
- Users who want to automate repetitive job-search work

Rolvio should be usable by a normal user without requiring programming knowledge.

---

# 4. Main User Outcome

The user should be able to open Rolvio and manage the complete job lifecycle:

Job Search
→ Job Match
→ Approval
→ Automatic Application
→ Submission Verification
→ Email Tracking
→ Assessment
→ Interview
→ Offer / Rejection

All of this should be visible from one application.

---

# 5. Core Principles

## 5.1 Never Fake Success

Clicking a Submit button does not mean that an application succeeded.

Rolvio must verify the result.

Only verified applications should be counted as successful.

---

## 5.2 Never Invent Important User Information

Rolvio must never invent:

- Experience
- Salary
- Education
- Visa information
- Work authorization
- Certifications
- Employment history
- Security clearance
- Notice period

If information is missing, Rolvio should ask the user.

---

## 5.3 Observe Before Acting

Browser execution must follow:

Observe
→ Understand
→ Act
→ Verify

Rolvio should not blindly execute fixed click sequences.

---

## 5.4 Recover From Unexpected States

If Rolvio expects one page but sees something different:

1. Inspect the current page.
2. Capture useful information.
3. Determine the new state.
4. Attempt recovery.
5. Continue if safe.
6. Ask the user if necessary.

---

# 6. Candidate Profile

Rolvio must maintain one complete Candidate Profile.

The profile should contain:

## Personal Information

- Full name
- Email
- Phone
- Location
- Country

## Online Profiles

- LinkedIn
- GitHub
- Portfolio
- Personal website
- Other relevant URLs

## Career Information

- Current role
- Current company
- Total experience
- Expected salary
- Current salary
- Notice period
- Available start date

## Education

- Degree
- University / college
- Major
- Graduation year
- CGPA / GPA
- 12th information
- 10th information

## Skills

- Skill name
- Experience with skill
- Skill confidence
- Skill category

## Projects

- Name
- Description
- Technology stack
- URL

## Certifications

- Certification name
- Issuing organization
- Year

## Languages

- Language
- Proficiency

## Work Preferences

- Remote
- Hybrid
- On-site
- Preferred locations
- Willing to relocate
- Preferred job roles

## Work Authorization

- Citizenship
- Visa status
- Sponsorship requirement

## Application Answers

- Standard questions
- Custom questions
- User-confirmed answers

Every subsystem must use the same Candidate Profile.

---

# 7. Resume System

Rolvio must support resume upload.

Initial version:

- PDF resume
- Resume text extraction
- Structured resume parsing
- Skills extraction
- Experience extraction
- Education extraction
- Project extraction
- Original resume storage
- Resume upload during job applications

Future versions may support:

- Multiple resumes
- Role-specific resumes
- DOCX resumes
- Cover letters
- Certificates
- Portfolio documents

---

# 8. Job Platforms

Initial supported platforms:

1. LinkedIn
2. Naukri
3. Internshala
4. Indeed
5. Wellfound

Future platform architecture should support:

- Shine
- TimesJobs
- Hirist
- Freshersworld
- Glassdoor
- Remotive
- Other future job platforms
- External ATS systems

Adding a new platform should not require rewriting Rolvio's core system.

---

# 9. Job Search Engine

The user must be able to configure:

- Target job roles
- Keywords
- Location
- Remote preference
- Maximum jobs
- Platforms
- Minimum match score
- Experience level
- Job type

Rolvio should search all enabled platforms.

Every discovered job must be converted into a common format.

---

# 10. Normalized Job Model

Every job should contain:

- Internal ID
- Platform
- Platform job ID
- Job title
- Company
- Job description
- Job URL
- Location
- Work type
- Employment type
- Salary
- Required experience
- Required skills
- Posted date
- Application type
- Discovery date
- Raw platform metadata

Downstream systems should work with this normalized Job model.

---

# 11. Job Matching Engine

Rolvio must compare each job with the Candidate Profile.

Match analysis should consider:

- Skills
- Experience
- Education
- Location
- Work preference
- Salary
- Seniority
- Work authorization
- Job role
- Technologies

The result should contain:

- Overall match score
- Skill match score
- Experience match score
- Education match score
- Location compatibility
- Work authorization compatibility
- Strong matching points
- Missing skills
- Risks
- Reasoning summary

---

# 12. Application Approval Modes

Rolvio should support three modes.

## Manual Mode

Rolvio finds and matches jobs.

The user approves every application.

## Smart Mode

Example:

90%+ match
→ Automatically approve

75–89%
→ Ask user

Below 75%
→ Ignore

Thresholds must be configurable.

## Autonomous Mode

Rolvio may automatically apply according to user-defined rules.

Even Autonomous Mode must respect:

- Minimum score
- Maximum applications
- Platforms
- Location preferences
- Job roles
- Company blacklist
- Work type
- Salary expectations

---

# 13. Application Engine

The Application Engine must support:

- Opening a job
- Checking login session
- Detecting already-applied jobs
- Detecting closed jobs
- Opening application forms
- Detecting new tabs
- Detecting modals
- Detecting iframes
- Reading application forms
- Filling fields
- Uploading resumes
- Navigating form steps
- Handling validation errors
- Repeating observe/fill/validate until complete
- Reviewing
- Submitting
- Verifying submission

---

# 14. Supported Form Controls

Rolvio should eventually understand:

- Text fields
- Email fields
- Phone fields
- Number inputs
- Textareas
- URLs
- Radio buttons
- Checkboxes
- Checkbox groups
- Native dropdowns
- Custom dropdowns
- Comboboxes
- Autocomplete
- Multi-select controls
- Date fields
- File uploads
- Resume uploads
- Consent fields

---

# 15. Answer Intelligence

Answer priority:

1. Exact Candidate Profile value
2. Saved user answer
3. Previously confirmed equivalent answer
4. Safe deterministic derivation
5. AI-generated writing answer
6. Ask user

AI may generate content for questions such as:

- Why do you want to work here?
- Tell us about yourself.
- Why are you interested in this position?
- Cover letter.

AI must not invent factual qualifications.

---

# 16. Answer Memory

Rolvio should remember user-confirmed answers.

Example:

Question:

"Will you require visa sponsorship?"

User answers:

"No"

Rolvio should recognize similar future questions and reuse the confirmed answer.

The user should be able to edit remembered answers.

---

# 17. Application State Machine

Possible application states include:

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
- FAILED
- CANCELLED

Every important transition should be recorded.

---

# 18. Submission Verification

Rolvio must verify applications after submission.

Possible evidence:

- Success message
- Confirmation page
- URL change
- Applied button state
- Platform application history
- Platform-specific confirmation
- Application ID

Possible final results:

- VERIFIED_APPLIED
- ALREADY_APPLIED
- SUBMITTED_UNVERIFIED
- FAILED
- NEEDS_USER

Only VERIFIED_APPLIED and ALREADY_APPLIED count as confirmed.

---

# 19. Recovery Engine

If an application flow fails, Rolvio should inspect:

- URL
- Page title
- Visible text
- Buttons
- Inputs
- Validation errors
- Frames
- Tabs
- Screenshot
- Current application state
- Previous actions

Rolvio should then:

- Retry
- Re-observe
- Switch tab
- Switch iframe
- Fill missing fields
- Refresh when safe
- Ask user
- Fail safely

Rolvio must not loop forever.

---

# 20. CAPTCHA Handling

Rolvio must detect CAPTCHA.

Rolvio must not attempt to bypass CAPTCHA automatically.

Instead:

1. Pause application.
2. Mark CAPTCHA_REQUIRED.
3. Notify user.
4. Open visible browser if needed.
5. User solves CAPTCHA.
6. Rolvio rechecks page.
7. Continue.

---

# 21. Email Tracker

Users should be able to connect supported email accounts.

Rolvio should:

- Scan only new messages
- Detect job-related emails
- Classify email type
- Match email to application
- Update application timeline

Email classifications:

- Application confirmation
- Recruiter message
- Assessment
- Interview invitation
- Interview schedule
- Rejection
- Offer
- Other job-related
- Irrelevant

---

# 22. Email Matching

Emails should use multiple matching signals:

- Company
- Job title
- Sender domain
- Platform
- Application date
- Email thread
- Job ID when available

Rolvio should not update an application if match confidence is too low.

---

# 23. Dashboard

Dashboard should show:

- Jobs discovered
- High-match jobs
- Pending approvals
- Applications queued
- Applications running
- Verified applications
- Applications needing attention
- Assessments
- Interviews
- Offers
- Employer rejections
- Recent activity
- Platform performance
- Response rate
- Interview rate

---

# 24. Application Tracker

Applications should be trackable through:

Applied
→ Assessment
→ Interview
→ Offer

or:

Applied
→ Employer Rejected

User rejection of a job must be different from employer rejection.

---

# 25. Analytics

Analytics should include:

- Jobs discovered
- Applications per day
- Applications per week
- Applications by platform
- Verified application rate
- Response rate
- Interview rate
- Offer rate
- Average match score
- Best performing job roles
- Best performing platforms
- Common requested skills
- Missing skills
- Common failure reasons

---

# 26. Session Manager

Users should log into each platform manually.

Rolvio should store and reuse the session.

Rolvio must verify the session is actually still valid.

Possible session states:

- Connected
- Expired
- Login Required
- Error

The existence of a session file does not prove that the user is logged in.

---

# 27. Background Task Manager

Rolvio should manage background tasks.

Task types:

- Job Search
- Matching
- Application
- Email Scan
- Analytics
- Maintenance

Task states:

- queued
- running
- paused
- waiting_for_user
- completed
- failed
- cancelled

---

# 28. Failure Diagnostics

Every important application failure should save diagnostic evidence.

Possible files:

- Screenshot
- Page HTML
- Visible text
- Current URL
- Application state
- Execution trace
- Error information

This is required so bugs can be reproduced and fixed.

---

# 29. Privacy

Rolvio handles sensitive information.

User information should remain local whenever possible.

Sensitive information includes:

- Resume
- Email
- Phone
- Salary
- Application answers
- Browser sessions
- Email credentials
- Job history

These values must never be committed to Git.

---

# 30. NORVI Licensing

Commercial Rolvio builds may use NORVI activation.

Licensing may include:

- NORVI account
- Activation key
- Device authorization
- Signed lease
- Offline grace period

Licensing must be separate from core job automation.

Licensing failure must not damage local user data.

---

# 31. Out of Scope for First Production Version

Not required initially:

- Mobile application
- Social network
- Community
- Employer recruitment software
- CAPTCHA bypass
- Automatic acceptance of job offers
- Automatic salary negotiation
- Automatic interview answering
- Support for every ATS on the internet
- Full resume builder

---

# 32. Product Success Criteria

Rolvio is ready only when a user can:

1. Install Rolvio.
2. Open Rolvio.
3. Create a profile.
4. Upload a resume.
5. Connect a supported platform.
6. Search jobs.
7. Receive useful matches.
8. Approve a job.
9. Start application automation.
10. Correctly fill common form fields.
11. Upload resume.
12. Handle multi-step applications.
13. Ask user when information is unknown.
14. Submit an application.
15. Verify submission.
16. Save correct application state.
17. Monitor relevant emails.
18. Track interviews and offers.
19. See accurate dashboard analytics.

The project is not complete merely because the code runs.