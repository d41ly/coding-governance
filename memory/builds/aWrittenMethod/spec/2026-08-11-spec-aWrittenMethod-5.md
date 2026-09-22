# TOOL-aWrittenMethod-5 — the method in the manifest's watch set

**Status:** CLOSED · rev-3 · 2026-08-11 · node a · Tier-1 · base 7f614a17 · streams kickoff · review wf_eb978bb2-f98

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-11-review-TOOL-aWrittenMethod-1-1.md](../reviews/2026-08-11-review-TOOL-aWrittenMethod-1-1.md) | diff-review | TOOL-aWrittenMethod-1 TOOL-aWrittenMethod-2 TOOL-aWrittenMethod-3 TOOL-aWrittenMethod-4 TOOL-aWrittenMethod-6 |
| [2026-08-11-review-TOOL-aWrittenMethod-1-2.md](../reviews/2026-08-11-review-TOOL-aWrittenMethod-1-2.md) | diff-review | TOOL-aWrittenMethod-1 TOOL-aWrittenMethod-2 TOOL-aWrittenMethod-3 TOOL-aWrittenMethod-4 TOOL-aWrittenMethod-6 |
| [2026-08-11-review-TOOL-aWrittenMethod-1-3.md](../reviews/2026-08-11-review-TOOL-aWrittenMethod-1-3.md) | diff-review | TOOL-aWrittenMethod-1 TOOL-aWrittenMethod-2 TOOL-aWrittenMethod-3 TOOL-aWrittenMethod-4 TOOL-aWrittenMethod-6 |

<!-- /gen:spec-records -->

## 1. Goal

`memory/guides/BUILD-METHOD.md` is a governing document that binds every multi-pass build, and editing
it forces no manifest re-audit. **This unit sets a precedent rather than closing a gap:** the `watch:`
list holds nine pathspecs and none is under `memory/`, so none of the three BINDING guides — the
review protocol, the unattended protocol, or the method — is watched today. Rev-1 claimed every other
governing doc had this discipline, which is false.

## 2. Scope (IN)


**Landing order.** This unit is step five of five. The set lands `2 → 6 → 3 → 4 → 5`, fixed by the
audit `wf_eb978bb2-f98`: unit 6 rewrites the renderer unit 3 measures against, unit 3 creates a new
method carrier unit 4 must then enumerate, and unit 5 puts the method under a manifest ratchet that
would otherwise tax every earlier unit's commit. These are NOT parallel-safe under M6.

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

Note the ordering trap this unit walks into deliberately, stated correctly. `.claude/SESSION-KICKOFF.md`
is not itself a watched path, so editing it does not trip the ratchet directly. The real reason S4 is
mandatory is that adding a pathspec to `watch:` widens check 5's range RETROACTIVELY over
`$LA_SHA..HEAD`, and commits already in that range touched the method — so the audit claim goes stale
the moment the row lands, and only a re-stamp in the same commit makes it true again.

## 5. Acceptance criteria

- **AC1** — When `.claude/SESSION-KICKOFF.md` is read, `watch:` and `verify-paths:` both name
  `memory/guides/BUILD-METHOD.md`.
- **AC2** — When a diff touching `memory/guides/BUILD-METHOD.md` is staged without a re-stamp,
  `bash skills/session-kickoff/manifest-check.sh --staged` REDS naming that file. The `--staged` flag
  is required: the default invocation runs the committed-history leg over `$LA_SHA..HEAD` and cannot
  see a staged-only change, so rev-1's spelling asserted an observation its own command cannot make.
  The fixture must also leave the staged manifest's `last-audit` equal to HEAD's, since that is the
  condition the staged leg reds on.
- **AC3** — When the re-stamped manifest is checked, `bash skills/session-kickoff/manifest-check.sh`
  exits 0.

## 6. Gates

`skills/session-kickoff/manifest-check.sh` (+ its self-test) · `.githooks/pre-commit`.

## 7. Open questions

none — the two options considered (watch the render, or watch the template) are settled in §3 by the
parity coupling, and no other fork surfaced.

## 8. Revision log

- rev-3 · 2026-08-11 · BUILT on branch, unmerged (4c0fd31). AC2 armed by hand: with last-audit rolled
  back to HEAD's value and a one-byte edit to the method staged, manifest-check.sh --staged reds
  naming memory/guides/BUILD-METHOD.md and exits 1. Tree restored by re-rendering the guide. This
  status header was left at SPECCED for one commit after the work landed, which is the exact drift
  M7 tells a resuming agent to check the header for.
- rev-2 · 2026-08-11 · folded audit `wf_eb978bb2-f98`. AC2 named an invocation that cannot produce
  its own observation — the staged leg needs `--staged`. §1's justifying premise was false: no binding
  guide is watched today, so this sets a precedent. §4's stated mechanism for the re-stamp was also
  wrong; the real one is check 5's range widening retroactively.
- rev-1 · 2026-08-11 · initial draft. Raised by unit 1 as `TOOL-aWrittenMethod-5`.
