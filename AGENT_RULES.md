# Autonomous Agent Safety Rules

These rules apply to every autonomous development task.

## Repository Safety

The agent must never:

- force push
- rewrite Git history
- delete the repository
- delete branches
- modify GitHub repository settings
- modify GitHub secrets
- expose credentials
- commit API keys
- commit `.env` files containing secrets

## Automation Safety

The agent must not modify:

- `.github/workflows/`
- `GEMINI.md`
- `AGENT_RULES.md`

unless explicitly instructed by the repository owner.

The agent must never modify its own safety restrictions.

## Development Scope

All changes must relate directly to the Resume/JD Matcher project.

Do not create unrelated features.

## Task Size

A micro-task should normally:

- address one clear objective,
- modify a limited number of files,
- be understandable independently,
- be testable independently.

Avoid massive refactoring.

## Testing

Before committing:

1. Run relevant tests.
2. Verify imports.
3. Check for obvious errors.
4. Review the Git diff.

If tests fail because of the new changes:

- attempt to fix the problem,
- rerun tests.

If the problem cannot be safely fixed:

- revert the task,
- do not commit it.

## Dependency Safety

Before adding a dependency:

- verify that it is necessary,
- add it to the dependency file,
- avoid unnecessary packages.

## Git Commit Safety

Each commit must represent one completed micro-task.

Commit messages should be descriptive.

Never create meaningless commits simply to increase GitHub activity.

## Change Size

Avoid changes that:

- rewrite the entire project,
- modify unrelated files,
- remove large amounts of working code,
- introduce unnecessary architecture.

## Secrets

Never print, expose, or commit:

- API keys
- passwords
- access tokens
- private credentials

Use environment variables.

## Failure Behavior

If a task cannot be completed safely:

1. Revert uncommitted changes.
2. Do not push broken code.
3. Stop the current task.

A failed task must never be converted into a meaningless commit.
