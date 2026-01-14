# .claude

Claude Code configuration directory containing custom slash commands and session data.

## Custom Commands

### mermec (GitLab)

- `/mermec:create-issue` - Create GitLab issue from template
- `/mermec:create-mr` - Create GitLab merge request from template

### progr (R Programming)

- `/progr:evaluate` - Evaluate R script implementations

## Structure

- `commands/` - Slash command definitions
- `projects/` - Project-specific metadata
- `settings.json` - User preferences

See `CLAUDE.md` for detailed documentation.
