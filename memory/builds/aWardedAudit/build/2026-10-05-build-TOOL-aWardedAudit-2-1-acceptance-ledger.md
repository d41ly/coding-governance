# Acceptance ledger — TOOL-aWardedAudit-2

**Serves:** journal TOOL-aWardedAudit-2

Built at `0268517d` and `f28ff537`. Every verdict was driven through the hook directly against the
new and the base hook, then pinned as arms in the agent-cap self-test, which ran green whole.

**Evidences:** TOOL-aWardedAudit-2
- AC1 — `spec-audit` — a live RUN.md pinning no fact beside a dated worktree key: denied naming RUN.md; the base hook admitted
- AC2 — `spec-audit: 2026-10-05` — pinned in a live RUN.md beside a README with no key: admitted
- AC3 — `authorized-by: prompt` — no run-state file, a prompt README with a dated key: denied naming the mode; the base hook admitted
- AC4 — `LANDED` — a LANDED record beside a slug README's dated key: admitted
- AC5 — `spec-audit: 2026-09-20` — the base slug-README arm admits unchanged
- AC6 — `specAudit: 2026-10-05` — a harness call beside a live run pinning no fact denied, pinning `2026-10-05` admitted; the base hook admitted both
- AC7 — `2026-09-01` — a pinned fact differing from the harness's `2026-10-05` denied naming both dates
