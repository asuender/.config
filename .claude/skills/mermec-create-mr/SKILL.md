---
name: mermec-create-mr
description: Create a merge request using the GitLab MR template for Mermec projects
context: fork
allowed-tools:
  - Read
  - Glob
  - Bash(glab mr:*)
  - Bash(glab auth:*)
  - Bash(git remote:*)
  - Bash(git branch:*)
  - Bash(git push:*)
  - Bash(git status)
  - Bash(git log:*)
  - Bash(git diff:*)
  - AskUserQuestion
---

# Create GitLab Merge Request

Create a GitLab merge request using the project's MR template.

## Workflow

### 1. Pre-flight Checks

Before creating the MR:
- Verify the current branch is not `main` or `master`
- Check for uncommitted changes
- Ensure the branch has been pushed to the remote

### 2. Template Discovery

Find available MR templates:

```
.gitlab/merge_request_templates/*.md
```

If multiple templates exist, ask the user which one to use. If none exist, proceed without a template.

### 3. Gather MR Details

Based on the conversation context and git history, determine:
- **Title**: concise summary of the changes
- **Description**: detailed explanation following the template structure
- **Labels**: appropriate labels
- **Assignee**: who should review
- **Related issues**: issues to link or close

Review the commits on the branch to understand the scope of changes:

```bash
glab mr diff
```

If critical information is missing, ask the user for clarification.

### 4. Create the Merge Request

Use the glab CLI:

```bash
glab mr create --title "..." --description "..." [--label "..."] [--assignee "..."]
```

## Best Practices

- Keep titles concise but descriptive (under 80 characters)
- Reference related issues with `Closes #123` or `Relates to #123`
- Fill all required template sections
- Request review from appropriate team members
- Ensure CI pipeline passes before requesting review

## Output

After creating the MR, provide:
1. The MR URL
2. A summary of what was created
3. Next steps (e.g., wait for CI, request review)
