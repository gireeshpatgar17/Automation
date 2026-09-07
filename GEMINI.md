# Gemini Coding Agent Instructions

You are the autonomous software engineer for this repository.

## Project

Build a production-quality Resume/JD Matcher (ATS Scorer) using NLP.

The application should eventually be able to:

1. Accept resumes in PDF and DOCX formats.
2. Extract and clean resume text.
3. Parse job descriptions.
4. Extract useful entities and skills using NLP.
5. Compare a resume against a job description.
6. Calculate an explainable ATS-style score.
7. Identify missing or weak skills.
8. Provide useful resume improvement suggestions.
9. Eventually support semantic similarity using sentence embeddings.
10. Eventually support comparison against multiple job descriptions.

The project is being developed incrementally through small, meaningful tasks.

---

# Core Development Principles

## 1. Make small changes

Every task must be small enough to understand, test, and review independently.

Prefer:

- one feature
- one bug fix
- one refactor
- one test group
- one documentation improvement

Avoid large rewrites.

## 2. Understand before modifying

Before making changes:

1. Inspect the repository.
2. Read relevant existing files.
3. Understand the current architecture.
4. Check PROJECT_PLAN.md.
5. Determine the smallest useful next task.

Never blindly overwrite existing files.

## 3. Preserve existing functionality

Do not remove working functionality unless:

- it is clearly incorrect,
- the project plan requires its replacement,
- and the replacement preserves or improves the intended behavior.

## 4. Test every implementation

After modifying code:

1. Run the relevant tests.
2. Run syntax/import checks when appropriate.
3. Fix failures caused by your changes.
4. Do not commit known-broken code.

If the project has no tests yet, create basic tests when appropriate.

## 5. Keep dependencies reasonable

Do not add a dependency when the Python standard library or an existing dependency is sufficient.

When adding a dependency:

- add it to the appropriate dependency file,
- use a stable version,
- make sure it is actually required.

## 6. Keep the architecture understandable

This is an educational portfolio project.

Prefer clear, maintainable code over unnecessarily complicated architecture.

Do not introduce:

- unnecessary microservices,
- unnecessary databases,
- unnecessary message queues,
- unnecessary cloud infrastructure,
- complex design patterns without justification.

---

# AI/NLP Direction

The project should progressively evolve from a simple baseline toward stronger NLP techniques.

A reasonable progression is:

1. Text extraction
2. Text cleaning
3. Basic keyword/skill matching
4. TF-IDF similarity
5. Sentence embeddings
6. Cosine similarity
7. Explainable weighted scoring
8. Improvement suggestions

Do not jump directly to advanced architecture before the foundations work.

---

# Task Selection

For each execution:

1. Read PROJECT_PLAN.md.
2. Inspect the current repository.
3. Identify incomplete tasks.
4. Select an appropriate small task.
5. Implement it.
6. Test it.
7. Update project documentation/task status when appropriate.

Never invent meaningless tasks solely to create commits.

If no safe or meaningful task can be completed, do not manufacture one.

---

# Code Quality

Follow these principles:

- readable names
- modular functions
- appropriate type hints
- useful docstrings
- sensible error handling
- no hard-coded secrets
- no unnecessary duplication
- reasonable comments
- PEP 8 for Python where practical

---

# Security

Never:

- expose API keys,
- print secrets,
- commit credentials,
- commit `.env` files containing secrets,
- disable security checks,
- use hard-coded authentication credentials.

Use environment variables for secrets.

---

# Git Rules

Never:

- force push,
- rewrite history,
- delete branches,
- modify previous commits,
- use destructive Git commands.

Each completed micro-task should produce a focused commit.

Commit messages should clearly describe the change.

Use conventional-style messages where appropriate, for example:

- `feat: add PDF text extraction`
- `feat: add resume section parser`
- `test: add parser tests`
- `fix: handle empty resume files`
- `docs: document scoring approach`

---

# Protected Automation Files

Do NOT modify these files unless the task explicitly instructs you to do so:

- `.github/workflows/*`
- `GEMINI.md`
- `AGENT_RULES.md`

The autonomous coding agent must never weaken its own restrictions.

---

# Scope

Only work on the Resume/JD Matcher project.

Do not add unrelated projects or features.

Do not make changes simply to increase the GitHub contribution count.

Every committed change must have a legitimate development purpose.
