# TOOL-aMendedFleet-11 — the review protocol and the review harness point reviewers at the filtered asks call

**Status:** SPECCED · rev-1 · 2026-10-04 · node a · Tier-1 · base 7af5f564 · streams tooling · ratified 2026-10-04 · order 11

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

Two carriers tell a reviewer to read the open asks through the whole `--asks --json` projection:
the review protocol's Tier-2 pattern, which tells the caller what to feed the finders, and the
review harness's prior-art spec lens, which adds `--all`. That output is 175,183 bytes for the live
asks and 312,033 with `--all`, PINNED, re-measured 2026-10-04 with `wc -c`, and
the report found that builds cited 0 and 1 of the 58 and 37 asks targeting the files they edited.
This unit repoints both carriers at the `--asks --json --path` call `TOOL-aMendedFleet-10` adds, so
a reviewer reads the ranked, capped asks about the files under review and nothing else.

## 2. Scope (IN)

- **S1** — The review protocol's Tier-2 pattern paragraph names the filtered call for the open
  backlog it tells the caller to feed the finders: `gen_build_index.py --asks --json --path`
  followed by every path the reviewed diff touches, says the rows come ranked by severity and capped
  with `--limit 0` lifting the cap, and keeps the backlog-shards fallback on the `mode` field. The
  edit is made in the kit template `tools/workflows/REVIEW-PROTOCOL.template.md` and reaches
  `memory/guides/REVIEW-PROTOCOL.md` through the kit's own render, never by hand. Observed by AC1
  and AC3.
- **S2** — The prior-art brief in `SPEC_LENSES` names `gen_build_index.py --asks --json --all --path`
  followed by every path the audited spec's §4 `### Files touched (estimate)` names, keeping
  `--all` because prior art includes decided asks, and keeping the shards fallback. The edit is made
  in `tools/workflows/tier2-review.template.js` and reaches `tools/workflows/tier2-review.js` through
  the same render. Observed by AC2, AC3 and AC5.
- **S3** — Both named calls run on this tree once `TOOL-aMendedFleet-10` is built: neither combines
  a flag that unit refuses. Observed by AC4.

## 3. Non-goals (OUT)

- Building `--path`, `--limit`, the ranking or the cap. That is `TOOL-aMendedFleet-10`.
- A harness-side fetch of the asks for a DIFF review. The harness is a workflow script with no
  shell at run time, the protocol already routes the asks through the caller's `byDesign` argument,
  and the by-design source is unit 45's ground. This unit repoints the two sentences that exist.
- The three other carriers that read `--asks --json` whole: the drift-audit Skill's priming list,
  the recall Skill's fallback and the state-audit workflow. Each reads asks for a whole area or for
  every decided ask, not for a path list, and the brief names only the two carriers above.
- The kickoff step that points at the same call, unit 78, and the close-time list, unit 66.
- The kit version bump. The review-harness kit moves in several units of this build, so the bump is
  owed once, at the close, after the last move.

### Edges

- **consumes-from** `TOOL-aMendedFleet-10` — the `--path` option and its JSON envelope; without
  it the call both carriers name exits 2 as an unknown option.
- **hands-off** external — the review-harness kit version bump, owed once by this build's close.

## 4. Design

### Evidence

Read at base `7af5f564`, re-verified 2026-10-04 at `6a88fbf7`, whose `tools/` and
`memory/guides/` bytes equal base.

- `memory/guides/REVIEW-PROTOCOL.md` lines 188-190 and the same lines of its template carry the
  sentence; the report's line numbers still hold. The template line holds no render token, so the
  edited sentence renders byte-identically.
- `tools/workflows/tier2-review.js` line 480 is the `prior-art` entry of `SPEC_LENSES`, a spec-audit
  lens; the report's line number still holds. No `DIFF_LENSES` brief names the asks: a diff review's
  finders get them only through `byDesign`, which the harness's own comment records no caller
  supplies today.
- `tools/workflows/kit.toml` declares both files `rendered`, from the two templates, by the
  `[[regenerate]]` argv `check-protocol-parity.test.sh --render --tracked-only`; the
  `review-protocol parity (kit vs dogfood)` leg grades the pair. `tier2-review.test.sh` pins the four
  spec-lens KEYS and none of their brief text, so the edit moves no arm.

### The two sentences, as they will read

Protocol, Tier-2 pattern: "Feed the finders the security model, the open asks on the files under
review — the rows `gen_build_index.py --asks --json --path <every path the diff touches>` prints,
ranked by severity and capped, with `--limit 0` lifting the cap, or the backlog shards when its
`mode` field says `shards` — and what is by-design, so they hunt NEW issues instead of re-reporting
known ones."

Harness, prior-art lens: "…and read the asks, decided ones included, through
`gen_build_index.py --asks --json --all --path <every path the spec's Files touched estimate names>`,
falling back to the backlog shards when its `mode` field says `shards`, before accepting a design
as new."

### Files touched (estimate)

- `tools/workflows/REVIEW-PROTOCOL.template.md`
- `memory/guides/REVIEW-PROTOCOL.md`
- `tools/workflows/tier2-review.template.js`
- `tools/workflows/tier2-review.js`

### Rollout

Two prose edits in templates, rendered. An adopter receives them on its next kit update, whose
default re-render writes both renders.

### Alternatives rejected

- **Editing the renders by hand.** The parity leg reds a render that differs from its template, and
  the kit README's rule is to edit the template, never the render.
- **Dropping `--all` from the prior-art lens.** Prior art is exactly the decided asks; the filter
  narrows by path, not by status.

## 5. Production-readiness checklist

- security — N/A — prose in two instructions; no new write path.
- perf / scale — a reviewer reads a capped feed instead of a 175 KB one, which is the point.
- error / empty / loading states — a path no ask targets returns an empty `asks` list, which the
  sentence does not misdescribe.
- observability — N/A — the feed's own `matched` and `cut` fields are unit 10's.
- risks — the named call is dead until unit 10 lands; build order 10 before 11 covers it, and AC4
  observes it.
- testing — direct greps over the four files and one run of each named call.
- migration — N/A — no stored state.
- user docs — N/A — the protocol IS the user doc.

## 6. Acceptance criteria

- **AC1** — When `grep -n -- "--asks --json" memory/guides/REVIEW-PROTOCOL.md tools/workflows/REVIEW-PROTOCOL.template.md`
  runs, every hit sits on a line that also names `--path`, and each file has at least one hit.
  Red when: a hit names the unfiltered call, or either file has none.
- **AC2** — When `grep -n -- "--asks --json --all --path" tools/workflows/tier2-review.js tools/workflows/tier2-review.template.js`
  runs, each file reports exactly one hit, inside the `prior-art` brief.
  Red when: either file still names `--asks --json --all` without `--path`.
- **AC3** — When the `--asks` lines of `tools/workflows/REVIEW-PROTOCOL.template.md` are compared
  with those of `memory/guides/REVIEW-PROTOCOL.md` (each read with `grep -- "--asks"` and the two
  outputs passed to `diff`), and the same comparison runs over `tools/workflows/tier2-review.template.js`
  and `tools/workflows/tier2-review.js`, both print nothing.
  Red when: a render was edited by hand away from its template, or a template edit was never
  rendered.
- **AC4** — When `python tools/memory-tree/gen_build_index.py --asks --json --path tools/workflows/tier2-review.js`
  and the same call with `--all` beside `--path` both run, each exits 0 and prints a JSON object
  carrying `paths`, `matched` and `cut`.
  Red when: either call exits 2, which is the carriers pointing at a flag combination unit 10
  refuses.
- **AC5** — When `node tools/workflows/check-workflow-syntax.js tools/workflows/tier2-review.js` runs,
  it exits 0.
  Red when: the edited brief string breaks the script's parse.

## 7. Gates

`review-protocol parity (kit vs dogfood)` · `workflow script syntax` · `verifier fan-out self-test` · `tier2-review self-test` · `unattended-build self-test` · `review-join self-test` · `recall floor` · `recall floor arms` · `kit epoch (shipped bytes move, the version moves)` · `spec tokens (a spec's own names resolve)`

The four self-test legs are owed by the `tools/workflows/` guard and run once, at the close.

## 8. Open questions

- **F1** — Does the diff review's harness gain its own asks fetch?
  Options: add a `DIFF_LENSES` instruction naming the call; leave the diff route as the protocol's
  caller-fed `byDesign`. The first is a second mechanism beside the repointing and overlaps unit 45.
  RESOLVED (agent, 2026-10-04, delegated): leave it; this unit repoints the two existing sentences.
- **F2** — Which of the five carriers that read `--asks --json` does this unit move?
  Options: all five; the two the report names. The other three ask for an area or for every
  decided ask, which a path list does not describe.
  RESOLVED (agent, 2026-10-04, delegated): the two the report and the brief name.

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft, from the two carriers and the review-harness descriptor at base.

## 10. Reuse audit

The seam is the kit's existing render pair: the two templates under `tools/workflows/`, rendered by
the `[[regenerate]]` argv in `tools/workflows/kit.toml` and graded by the protocol parity leg. No
code is added. `python tools/codebase-map/reuse_lookup.py "point review finders at the open asks for
the paths a diff touches"` returned `REVIEW-PROTOCOL.md` and `render_ask_row` by name stem and no
existing path-scoped asks feed, so the one to point at is `TOOL-aMendedFleet-10`'s. Recall named
`TOOL-dDerivedDocket-36`, the unit that wrote the current carrier wording and its shards fallback,
which this edit keeps. Where the report and the tree disagree: the report's 164 KB is now 175,183
bytes; its line numbers 188-190 and 480 still hold.

Recall terms used: `python tools/memory-recall/query.py "which record decides what the review
finders read as the open backlog asks feed" --terms "review protocol finders priming open backlog
asks gen_build_index --asks --json prior-art lens tier2-review byDesign shards mode"`
