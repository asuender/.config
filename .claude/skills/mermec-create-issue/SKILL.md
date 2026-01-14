---
name: mermec-create-issue
description: Create an issue using the GitLab issue template for Mermec projects
context: fork
allowed-tools:
  - Read
  - Glob
  - Bash(glab issue:*)
  - Bash(glab auth:*)
  - Bash(git remote:*)
  - AskUserQuestion
---

# Create GitLab Issue

Create a GitLab issue using the project's issue template.

## Workflow

### 1. Template Discovery

First, find available issue templates:

```
.gitlab/issue_templates/*.md
```

If multiple templates exist, ask the user which one to use. If none exist, proceed without a template.

### 2. Gather Issue Details

Based on the conversation context, determine:
- **Title**: concise summary of the issue
- **Description**: detailed explanation following the template structure
- **Labels**: appropriate labels (bug, feature, enhancement, etc.)
- **Assignee**: if mentioned in the context

If any critical information is missing, ask the user for clarification.

### 3. Create the Issue

Use the glab CLI to create the issue:

```bash
glab issue create --title "..." --description "..." [--label "..."] [--assignee "..."]
```

## Best Practices

- Keep titles concise but descriptive (under 80 characters)
- Fill all required template sections
- Use appropriate labels for categorization
- Link related issues using `#issue_number` in the description
- Mention relevant team members with `@username` if needed

## Output

After creating the issue, provide:
1. The issue URL
2. A summary of what was created
