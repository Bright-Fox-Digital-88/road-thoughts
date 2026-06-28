# road-thoughts

This is a repo for testing out what it's like to work on the road using voice dictation in Claude.

## Agent skills

### Issue tracker

Issues, PRDs, and triage live in this repo's **GitHub Issues** (via the `gh` CLI). External PRs are **not** a triage surface. See `docs/agents/issue-tracker.md`.

### Triage labels

Canonical label vocabulary (`needs-triage`, `needs-info`, `ready-for-agent`, `ready-for-human`, `wontfix`) — names used as-is. See `docs/agents/triage-labels.md`.

### Domain docs

**Multi-context** layout: a `CONTEXT-MAP.md` at the root points to per-context `CONTEXT.md` files (created lazily by `/domain-modeling`). See `docs/agents/domain.md`.
