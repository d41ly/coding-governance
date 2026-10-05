# TOOL-dThriftyLanding-3 — the push boundary recognises a doc-only push and scopes its bar to it

**Status:** CLOSED · rev-2 · 2026-10-05 · node d · Tier-2 · base c3ef6742 · streams tooling · order 3

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-05-build-TOOL-dThriftyLanding-1-runlog-58509c21.md](../build/2026-10-05-build-TOOL-dThriftyLanding-1-runlog-58509c21.md) | journal | TOOL-dThriftyLanding-1 TOOL-dThriftyLanding-2 TOOL-dThriftyLanding-4 TOOL-dThriftyLanding-5 TOOL-dThriftyLanding-6 TOOL-dThriftyLanding-8 TOOL-dThriftyLanding-9 TOOL-dThriftyLanding-10 TOOL-dThriftyLanding-11 TOOL-dThriftyLanding-12 |
| [2026-10-05-build-TOOL-dThriftyLanding-3-1-acceptance-ledger.md](../build/2026-10-05-build-TOOL-dThriftyLanding-3-1-acceptance-ledger.md) | journal | — |
| [2026-10-05-prompt-TOOL-dThriftyLanding-3-1-build-brief.md](../prompts/2026-10-05-prompt-TOOL-dThriftyLanding-3-1-build-brief.md) | journal | — |
| [2026-10-05-review-TOOL-dThriftyLanding-1-closing-diff-round1.md](../reviews/2026-10-05-review-TOOL-dThriftyLanding-1-closing-diff-round1.md) | diff-review | TOOL-dThriftyLanding-1 TOOL-dThriftyLanding-2 TOOL-dThriftyLanding-4 TOOL-dThriftyLanding-5 TOOL-dThriftyLanding-6 |

<!-- /gen:spec-records -->

## 1. Goal

`.githooks/pre-push` decides FULL or SCOPED from the recorded green alone. It never asks what the push
changes, so a one-line doc edit and a kit rewrite get the same decision, and a doc-only build landing
is forced FULL by predicate 5 because every landing here is a merge. This unit makes the hook classify
the push: when every path it carries past R, the remote tip, sits in the repository's declared doc
class, the push is doc-only, predicate 5 is waived, and the runner is handed `GATE_DOCS_BASE=R` so
that only the legs reading a changed doc path run (`TOOL-dThriftyLanding-1`).

## 2. Scope (IN)

- **S1** — The doc class is `GATE_DOC_PATHS`, a space-separated list of repo-relative paths, each a
  file or a directory ending in `/`, parsed out of `.githooks/gate-env.sh` AS COMMITTED AT R with
  `read_policy_key`, the parse the inherited-red policy already uses; R's bytes are never executed
  and the pushed tree's copy is never read. Absent or empty at R, there is no doc class. An element
  that starts with `:` or `/`, holds a glob character or a `..` segment, invalidates the whole value,
  and the hook says so. Observed by AC1, AC5 and AC6.
- **S2** — A push is doc-only when R is a sha that is an ancestor of the pushed tip, at least one path
  differs between them, and no path outside the doc class appears either in `git diff --no-renames
  --name-only R tip` or in the files any commit in `R..tip` touched, both read with git's literal
  exclude pathspecs. Any git call that fails reads as not doc-only. Observed by AC1 to AC3.
- **S3** — On a doc-only push, `check_green_record` is called with predicate 5 waived, for the full
  green and for the inherited green alike; every other predicate still forces. When the decision is
  then scoped, the hook also exports `GATE_DOCS_BASE` set to R, and the decision line carries
  `docs-only: <n> path(s) in GATE_DOC_PATHS at <R8>` after the pushed sha, so every reader that greps
  `gate on <branch> push` still matches. When a predicate still forces, the FULL line carries
  `doc-only, but` before the reason. Observed by AC1, AC4 and AC7.
- **S4** — An exported `GATE_DOCS_BASE` is cleared for EVERY bar, a STUB included, and named among
  the knobs not honoured; the hook sets it after that, on a doc-only decision only. It is not added to
  `BAR_SCRUBBED_KNOBS`, whose STUB exemption exists for fixture manifests this knob has no part in.
  Observed by AC8.

## 3. Non-goals (OUT)

- What the runner does with `GATE_DOCS_BASE`: `TOOL-dThriftyLanding-1`.
- Gov's own doc class and its legs' declarations: `TOOL-dThriftyLanding-5`.
- The lag bound, `GATE_FULL_MAX_LAG=10`, and predicates 1 to 4 and 6 to 8: unchanged.
- A branch push: it is gated only by the branch bar, as today.

### Edges

- **consumes-from** `TOOL-dThriftyLanding-1` — the runner reads `GATE_DOCS_BASE`.
- **consumes-from** `TOOL-dThriftyLanding-2` — the stamp candidates whose predicates S3 relaxes.
- **hands-off** `TOOL-dThriftyLanding-5` — gov declares `GATE_DOC_PATHS`.

## 4. Design

### Evidence

Read at base `c3ef6742`. `.githooks/pre-push` reads the inherited-red keys at R with
`read_policy_at`, which runs `read_policy_key` over `git show "$sha:$_gate_env_rel"`. Predicate 5 in
`check_green_record` forces when the tip's second parent is not an ancestor of the recorded sha, and
its comment says it fires on every first-attempt landing. The decision block exports `GATE_BASE` or
`GATE_FULL` and prints one line; `BAR_SCRUBBED_KNOBS` is unset for every bar not labelled STUB just
before it. This clone's last records landing, `fd82e883`, ran the FULL bar for 258 s.

### Files touched (estimate)

- `.githooks/pre-push`
- `.githooks/pre-push.test.sh`

### Alternatives rejected

- **Read the doc class from the pushed tree.** A push could declare its own code a doc and skip the
  legs that would catch it. R is what the last gated push landed.
- **Waive every forcing predicate on a doc-only push.** The lag bound is how a too-narrow declaration
  is caught, and the owner set it at 10 on the record; a doc-only build of 13 commits still pays it.
- **Classify by file extension.** A kit's rendered guide, a Skill and the charter template are all
  markdown and all product; which paths are code is a per-repository answer, so it is declared.

## 5. Production-readiness checklist

- perf / scale — one `git show`, two `git diff` and one `git log` per default-branch push.
- security — the class is read at R and never executed; the runner knob is scrubbed from the
  environment; an invalid declaration is no declaration.
- error / empty / loading states — every failure reads as not doc-only, which is today's behaviour.
- observability — the decision line names the docs case, its path count and R.
- testing — the hook suite drives scratch clones; each arm RED against the base hook first.
- migration — none: without `GATE_DOC_PATHS` at R the hook decides as at base.
- user docs — the hook header, the gate-env notes and the charter section, in `TOOL-dThriftyLanding-6`.
- risks — an over-wide declaration, such as `tools/`, would scope code pushes; it is the owner's file.

## 6. Acceptance criteria

- **AC1** — When R declares `GATE_DOC_PATHS="notes/"` and the push changes only the fixture's notes/a.md with a
  usable full green, the hook prints `docs-only` and the bar receives `GATE_DOCS_BASE` equal to R.
  Red when: the base hook prints `scoped gate` with no docs case and exports no docs base.
- **AC2** — When the same push also changes the fixture's src/x.sh, the decision carries no `docs-only`.
  Red when: a mixed push is classified doc-only.
- **AC3** — When a commit in the range adds src/x.sh and a later one removes it, the decision line
  carries no `docs-only`.
  Red when: only the net diff is read.
- **AC4** — When the doc-only pushed tip is a merge whose second parent the record does not cover,
  the hook prints `scoped gate` with `docs-only`, not `FULL gate`.
  Red when: predicate 5 still forces the doc-only landing.
- **AC5** — When the doc class is declared only in the pushed tree, not at R, the decision
  line carries no `docs-only`.
  Red when: the pushed tree can declare its own doc class.
- **AC6** — When R declares `GATE_DOC_PATHS="notes/*"`, the hook names the value invalid and the push
  is not doc-only.
  Red when: a glob element is honoured or passes silently.
- **AC7** — When the record is more than `GATE_FULL_MAX_LAG` commits behind on a doc-only push, the
  hook prints `FULL gate` and `doc-only, but`.
  Red when: the lag bound is waived for a doc push.
- **AC8** — When `GATE_DOCS_BASE` is exported into a push that is not doc-only, the bar does not
  receive it, and the hook names it among the knobs it did not honour.
  Red when: the environment narrows the authoritative bar.

## 7. Gates

`pre-push self-test` · `push-main self-test` · `pre-push run-log line` · `spec tokens (a spec's own names resolve)`

New arm: .githooks/pre-push.test.sh · a doc-only push under a declared `GATE_DOC_PATHS` at R, run against the base hook · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-05 · initial draft, from the hook's decision block and this clone's push log.
- rev-2 · 2026-10-05 · S3 puts the docs clause after the pushed sha, because the suite's `decide` and
  the run log grep `gate on <branch> push`; S4 clears the knob for a STUB bar too, so AC8 is observable.

## 10. Reuse audit

The seams extended are `read_policy_key`, which already reads two keys at R without executing R,
`check_green_record`, which takes the waiver as an argument, and `BAR_SCRUBBED_KNOBS`, the knob scrub
that already keeps `GATE_LEGS` and `GATE_REUSE` from narrowing a vetted bar.
`python tools/codebase-map/reuse_lookup.py` cannot see `.sh`; the seams were found by reading the
hook. The recall query returned the inherited-red specs of `dDerivedDocket`, which state why a key
that decides a landing is read at R; that rule is followed here.

Recall terms used: pre-push GATE_FULL scoped gate full green stamp guard lag bound records-only landing push-main.sh leg manifest merge second parent
