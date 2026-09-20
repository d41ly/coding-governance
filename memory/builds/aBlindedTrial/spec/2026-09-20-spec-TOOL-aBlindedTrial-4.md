# TOOL-aBlindedTrial-4 — the fan-out hook denies a direct spec-audit call the build README did not declare

**Status:** CLOSED · rev-5 · 2026-09-20 · node a · Tier-2 · base b7dee206 · streams tooling · order 2 · ratified 2026-09-20

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-21-build-TOOL-aBlindedTrial-2-opt-in-ledger.md](../build/2026-09-21-build-TOOL-aBlindedTrial-2-opt-in-ledger.md) | journal | TOOL-aBlindedTrial-2 TOOL-aBlindedTrial-3 TOOL-aBlindedTrial-5 |
| [2026-09-20-review-TOOL-aBlindedTrial-2-3-4-5-closing-diff-round1.md](../reviews/2026-09-20-review-TOOL-aBlindedTrial-2-3-4-5-closing-diff-round1.md) | diff-review | TOOL-aBlindedTrial-2 TOOL-aBlindedTrial-3 TOOL-aBlindedTrial-5 |
| [2026-09-20-review-TOOL-aBlindedTrial-2-3-4-5-closing-diff-round2.md](../reviews/2026-09-20-review-TOOL-aBlindedTrial-2-3-4-5-closing-diff-round2.md) | diff-review | TOOL-aBlindedTrial-2 TOOL-aBlindedTrial-3 TOOL-aBlindedTrial-5 |

<!-- /gen:spec-records -->

## 1. Goal

`tools/hooks/agent-cap.js` gains one rule: a `Workflow` tool call whose structured `args` carry
`kind: "spec-audit"` is denied unless the build README under the call's `repo` carries
`spec-audit: <date>` in its front matter. This is what makes the audit *forbidden* in an
attended session rather than merely not required.

## 2. Scope (IN)

- S1 — the rule reads `tool_input.args` as an object or as a JSON string (the Workflow tool
  delivers both; `tier2-review.js:54-63` parses the same way) and fires only when `kind ===
  'spec-audit'`; every other kind and an absent `kind` are not this rule's business. Observed by AC1,
  AC4.
- S2 — the README path is `<args.repo>/<dirname(args.reviewDir)>/README.md`; `repo` must be a
  string and `reviewDir` must sit under a `builds/<slug>/` segment, else the rule DENIES by name
  (fail closed — a call this rule cannot place cannot be admitted). The key is read from the
  worktree file's front matter through the front-matter reader `scratch-guard.js` already has for
  `authorized-by:`, lifted into a shared read rather than copied. Observed by AC2, AC3, AC5.
- S3 — the value must match `^\d{4}-\d{2}-\d{2}$`; `spec-audit: yes` reads as absent; a key inside
  the body (a fenced block) is not front matter. Observed by AC3.
- S4 — every throw inside the rule is caught and returned as a DENY string: a PreToolUse hook that
  exits 1 is non-blocking, so a crash would admit. Observed by AC6.
- S5 — the rule sits after the payload parse and before the `scriptPath` read (`agent-cap.js`, after
  `:1742`), so a `name:`-only or `scriptPath` invocation is judged too; the deny message names the
  decision id, the front-matter key and the README path, and spells no `tools/…` literal (the
  install-prefix count is pinned at 7). Observed by AC1, AC7.
- S6 — `tools/hooks/README.md` gains the rule under "What the hook DENIES" and, in the header
  section, the two limits: the nested `workflow()` inside a running harness is not a tool call and
  is enforced by `TOOL-aBlindedTrial-3`; the hook reads the worktree README while the driver reads
  BASE. `agent-cap@` moves 1.x → next in both halves of `agent-cap.js:66` and in
  `scratch-guard.js:73`. Observed by AC7.
- S7 — `agent-cap.test.sh` gains a section beside the `scriptPath` arms (`:658-673`): deny without
  the key, allow with it, args-as-string both ways, `diff-review` allowed, body-only key denied,
  unresolvable `repo` denied, and a `msg` arm on the deny text. Observed by AC1–AC6.

## 3. Non-goals (OUT)

- The hook does not read BASE and does not spawn git for this rule.
- No `--only=` member is added; the closed set stays `join`.
- The programmatic route — a harness's nested `workflow()` — is `TOOL-aBlindedTrial-3`'s; a sibling,
  not an edge.
- No change to `scratch-guard.js`'s behaviour; only the front-matter reader becomes shared, and its
  own arms keep passing.

### Edges

- **consumes-from** `TOOL-aBlindedTrial-2` — the key grammar `spec-audit: <date>`; a different
  spelling there makes this rule deny every declared build.

## 4. Design

### Inventory

- `checkSpecAuditDeclared(args, cwd)` — leads with the lexicon verb `check`; returns `null`
  (admit) or a deny string. `guard…` is refused by the verb table (verified with `lexicon.py
  --suggest`).
- `readFrontMatterKey(bytes, key)` — the shared reader, leading with `read`; `scratch-guard.js`'s
  `authorized-by` exemption becomes a caller of it. It takes BYTES, not a path (rev-2).

### Files touched (estimate)

`tools/hooks/agent-cap.js` · `tools/hooks/scratch-guard.js` (version marker; reader shared) ·
`tools/hooks/agent-cap.test.sh` · `tools/hooks/README.md` · `memory/map/features/` hooks dossier.

### Alternatives rejected

- Text-scanning the script for `spec-audit`: both harnesses spell it in comments and literals and
  would deny themselves — the class the hook's README already records.
- Resolving the repo from `gitCommonDir(cwd)`: in a linked worktree that is the primary tree's
  `.git`, so the README read would be the wrong checkout's; `args.repo` is required by the harness
  and is the right root.

## 5. Production-readiness checklist

- security — fail closed on an unplaceable call; every exception becomes a deny
- perf / scale — one file read per spec-audit call; nothing on any other call
- error / empty / loading states — missing README, malformed value, body-only key, non-string
  `repo` all deny by name
- observability — the deny message; `tools/hooks/README.md`
- risks — an adopter with no `memory/builds/` layout gets a deny naming a path it does not have;
  the README bullet says the remedy is the key
- testing — `agent-cap.test.sh`, on the bar under `agent-cap self-test` (guard `tools/hooks/`)
- migration — none
- user docs — the hook README

## 6. Acceptance criteria

- **AC1** — When `node tools/hooks/agent-cap.js` reads a `Workflow` payload whose `args` object
  carries `kind: "spec-audit"`, a valid `repo` and a `reviewDir` under a fixture build `tSA`, and that
  build's `README.md` has no `spec-audit:` key, it exits 2 and stderr names `TOOL-aBlindedTrial-6`
  and `spec-audit:`.
  Red when: the call is admitted, or the message names a `tools/` path.
- **AC2** — When the same payload runs after the README gains `spec-audit: 2026-09-20` in its front
  matter, it exits 0.
  Red when: a declared build is denied.
- **AC3** — When the key reads `spec-audit: yes`, or sits only inside a fenced block in the body, the
  hook exits 2.
  Red when: a non-date or body-only value admits.
- **AC4** — When `args` is delivered as a JSON STRING carrying the same fields, AC1 and AC2 hold
  unchanged; when `kind` is `diff-review` or absent, the hook exits 0 on the rule.
  Red when: the string form bypasses the rule, or a diff review is denied.
- **AC5** — When `repo` is a number or `reviewDir` has no `builds/<slug>/` segment, the hook exits 2
  with a message naming the field.
  Red when: an unplaceable spec-audit call is admitted.
- **AC6** — When the README path is unreadable (a directory, or a permission failure),
  `agent-cap.js` exits 2 and prints a deny rather than a stack trace.
  Red when: a thrown error exits 1 and admits.
- **AC7** — When `bash tools/check-kit-versions.sh` runs, it exits 0 with both halves of the
  `agent-cap@` marker moved, and `grep -c 'tools/' tools/hooks/agent-cap.js` matches the
  install-prefix registry's pinned count.
  Red when: a version half is left behind, or the literal count rises.

## 7. Gates

`agent-cap self-test` · `scratch-guard self-test` · `verifier fan-out` · `kit version markers` · `install-prefix (shipped surface)` · `lexicon naming predicates` · `agent-cap restatement`

New arm: `tools/hooks/agent-cap.test.sh` · README with and without the key, args as object and as string · none

## 8. Open questions

- **F1 — fail open or fail closed on an unplaceable call.** RESOLVED (agent, 2026-09-20,
  delegated): closed, for `kind: spec-audit` only. The harness refuses a call without `repo`
  anyway, so nothing legitimate is lost, and "forbidden" cannot mean "admitted when the guard cannot
  see".

## 9. Revision log

- rev-1 · 2026-09-20 · initial draft from the scout of `agent-cap.js` at b7dee206.
- rev-2 · 2026-09-20 · §4 · AMEND: `readFrontMatterKey` takes BYTES, not a path. The `authorized-by`
  caller reads a STAGED BLOB through `git show`, which has no file on disk to name, so a path-taking
  reader could not make it a caller; the rule in `agent-cap.js` reads its file and hands the bytes
  over. No AC moves.
- rev-3 · 2026-09-20 · §3 / §7 · AMEND (closing review of units 2–5, F7): §3 claimed scratch-guard's
  "own arms keep passing" while `bash tools/hooks/scratch-guard.test.sh` was red at HEAD and at base
  b7dee206 alike — AC9 read 7 engine spans against a floor of 8, a pre-existing red from
  `KICK-aReplayedCard-3` that this unit's `tools/hooks/` edit brings onto the `GATE_SELFTESTS=1` run
  it owes. §7 gains `scratch-guard self-test`, the sibling leg the same `tools/hooks/` guard trips;
  the floor is re-pinned to 7 with a dated reason in the test, and the suite was re-run and
  observed at 165 passed, 0 failed, so the §3 claim is now observed rather than asserted. No AC moves.
- rev-4 · 2026-09-21 · §6 · CLOSED. All seven criteria observed; rounds 1 and 2 folded `String(kind)`,
  the subjects-to-build tie, the `..` and absolute-path denies, the win32-only MSYS fold.
- rev-5 · 2026-09-21 · §3 · the hands-off line to unit 3 becomes a non-goal sentence, for the same
  reason as unit 3's rev-4.

## 10. Reuse audit

Probe: `tools/codebase-map/reuse_lookup.py "deny a tool call from a PreToolUse hook based on a repository file"` returned no candidate in the layer this
unit edits — it reports `unscanned layers: .sh` and resolves no `.js` symbol either — so the seam below
was found by reading the source, not by the probe. The seam is `scratch-guard.js`'s README front-matter read for the `authorized-by:` exemption, lifted
to a shared reader; the deny plumbing is `agent-cap.js`'s existing rule shape and its `msg` arm
pattern. Recall terms used: agent-cap hook PreToolUse deny Workflow args kind spec-audit README
front matter authorized-by scratch-guard install-prefix lexicon verb.
