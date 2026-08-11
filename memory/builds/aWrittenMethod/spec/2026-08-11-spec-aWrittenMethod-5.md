# TOOL-aWrittenMethod-5 — the method in the manifest's watch set

**Status:** SPECCED · rev-1 · 2026-08-11 · node a · Tier-1 · base 7f614a17 · streams kickoff

## 1. Goal

`memory/guides/BUILD-METHOD.md` is a governing document that binds every multi-pass build, and editing
it forces no manifest re-audit. Every other governing doc in this repo has that discipline; this one
was landed without it.

## 2. Scope (IN)

- **S1** — add `memory/guides/BUILD-METHOD.md` to `watch:` in `.claude/SESSION-KICKOFF.md`, so a diff
  touching the method makes the pre-commit ratchet demand a re-stamp and a re-verification of the §B
  claims it feeds.
- **S2** — add it to `verify-paths:` as a tracked anchor.
- **S3** — one §B pointer line naming the method as the procedure a multi-pass build follows, so the
  manifest's own orientation section reaches it.
- **S4** — re-stamp `last-audit` in the same commit, per the manifest's own rule.

## 3. Non-goals (OUT)

No change to the ratchet's mechanics, its checker, or the watch grammar.

No addition of the SHIPPED template `tools/memory-tree/BUILD-METHOD.template.md` to `watch:`. The
render is derived from it and the parity leg already couples them; watching both would make one edit
demand two stamps for one change.

## 4. Design

`watch:` is a semicolon-separated pathspec list read by `skills/session-kickoff/manifest-check.sh`
check 5, which reds when a staged diff touches a watched file and `last-audit` did not move. The
method qualifies on the same grounds as `parallel-coding-governance.template.md` and
`skills/session-kickoff/SKILL.md`, both already listed: it states rules a session is expected to have
read, so a change to it invalidates a claim the manifest makes about what a session knows.

Note the ordering trap this unit walks into deliberately: adding a path to `watch:` edits
`.claude/SESSION-KICKOFF.md`, which is itself the file carrying `last-audit`. S4 is not optional
bookkeeping — without it in the same commit, the change reds its own gate.

## 5. Acceptance criteria

- **AC1** — When `.claude/SESSION-KICKOFF.md` is read, `watch:` and `verify-paths:` both name
  `memory/guides/BUILD-METHOD.md`.
- **AC2** — When a diff touching `memory/guides/BUILD-METHOD.md` is staged without a re-stamp,
  `bash skills/session-kickoff/manifest-check.sh` REDS naming that file. This is the arming assertion
  and it is verified by staging such a diff, observing the red, then unstaging.
- **AC3** — When the re-stamped manifest is checked, `bash skills/session-kickoff/manifest-check.sh`
  exits 0.

## 6. Gates

`skills/session-kickoff/manifest-check.sh` (+ its self-test) · `.githooks/pre-commit`.

## 7. Open questions

none — the two options considered (watch the render, or watch the template) are settled in §3 by the
parity coupling, and no other fork surfaced.

## 8. Revision log

- rev-1 · 2026-08-11 · initial draft. Raised by unit 1 as `TOOL-aWrittenMethod-5`.
