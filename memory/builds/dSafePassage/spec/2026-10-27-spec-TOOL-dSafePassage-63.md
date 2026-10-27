# TOOL-dSafePassage-63 — `update` proves an edit to a rendered file from the sha256 its install recorded, when the row has no `oid`

**Status:** DEFERRED · rev-1 · 2026-10-27 · node d · Tier-2 · base 60d90cb7 · streams tooling · order 5 · advances TOOL-dSafePassage-14

**Derived:** TOOL-dSafePassage-5

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

TOOL-dSafePassage-5's third build pass (`wf_0d024041-1eb`, HEAD `29665dd17`) planted one adopter
line in `.claude/skills/lexicon/SKILL.md` over a release-0 install, and the first `update` rendered
over it with no order: the edit was lost. `check_render_edited` (TOOL-dSafePassage-9 S5) proves an
edit only against a row's `oid`, and `apply` writes no `oid` on a `rendered` row, then or now. This
unit lets the check prove the edit from the `output_sha256` that `apply` records on every such row,
so an install whose render no `update` has re-measured keeps the adopter's edit, holds its kit and
receives the order TOOL-dSafePassage-9 promises.

## 2. Scope (IN)

- **S1** — The fallback. `check_render_edited` (`tools/govkit/govkit.py:9382-9393`) grades a row that
  carries no `oid` and does carry `output_sha256`: it is edited when `output_sha256` equals none of
  three hashes of the working file's raw bytes, `_sha` (`:8800-8801`) of the bytes as read, of those
  bytes with every CRLF folded to LF, and of the folded bytes with every LF written as CRLF (§8 F1).
  A row with an `oid` is graded by it as today, and a row with neither field, or no file, is False as
  today. Observed by AC1 and AC2.
- **S2** — The plants. `tools/govkit/fixtures/retired_edits.py` gains `render-edited-no-oid`: the
  target edits the render `apply` left, with no `update` between, so its row carries `output_sha256`
  and no `oid`; gov moves the template; `update --write` runs. It gains `render-eol-no-oid`: the same,
  with the render's line endings rewritten as CRLF and nothing else changed. It gains the stub
  `oid-only`, which grades a row with no `oid` False, as the check did before S1. Observed by AC1
  and AC2.
- **S3** — The docs. The paragraph "A rendered file you edited since its last render" of
  `help/update-edits.md` says that a row whose receipt recorded only the bytes its install left is
  compared with those bytes, line endings aside, in place of its sentence that such a row cannot
  show an edit. Observed by AC3.

## 3. Non-goals (OUT)

- Stamping `oid` on `rendered` rows at `apply`. It would mend installs made after it lands and none
  in the field, whose `apply` already ran; the fallback reads a field both vintages wrote (§4).
- Any role other than `rendered`, and any verdict other than `render-edited`.
- The upgrade-walk leg and its `edited-render` plant, which TOOL-dSafePassage-5 owns.

### Edges

- **hands-off** `TOOL-dSafePassage-5` — the `plants` case's `edited-render` plant read `ordered`, and the `down`, `reup` and `kill` digests at the lexicon Skill, which differ from release-0's and from `up`'s only because the first `update` rendered over the planted edit

Read and closed, so named here rather than joined: TOOL-dSafePassage-9's `check_render_edited`, its
`render-edited` verdict, the held kit and the ordered arm that writes the order.

## 4. Design

### Why the edit was lost

`apply` observes every rendered destination after its adopters run and records
`row["output_sha256"] = hashlib.sha256(dp.read_bytes()).hexdigest()`, the raw bytes on disk, before
any filter: `tools/govkit/govkit.py:8387` at `29665dd17`, and `:8162` at the pin `60d90cb7`, the
same line. It reads `oid` only for `LANDABLE_ROLES` (`:8136-8152`, `:8504-8513`), which `:3920`
derives as the roles of kind `write`, and `rendered` is `side-effect` (`:3896`). So a `rendered`
row leaves `apply` with no `oid`. Only `measure_rendered_rows` (`:9338-9379`) stamps one, and only
`update` calls it (`:12802`), after its render ran. Its first run therefore reaches
`check_render_edited` (`:10445`) with no `oid`, the check answers False, the row is capped at
`re-rendered` (`:10448-10449`), and the kit's regenerate writes over the edit.

`update` never writes `output_sha256`: `:8387` is its one writer. A row that has an `oid` is graded by
it, so the fallback reads `output_sha256` only on a row no re-measure has reached, where it still names
the bytes `apply` observed. A held kit's rows are not re-measured (`:12790-12799`), so a held row
keeps the field, and the next run holds it again until the adopter acts on the order.

### The comparison

```
check_render_edited(target, row):
  no file                     -> False                        (today)
  row["oid"]                  -> the clean blob differs from it  (today)
  row["output_sha256"]        -> raw = the file's bytes; lf = raw with CRLF folded to LF
                                 edited = output_sha256 not in {_sha(raw), _sha(lf), _sha(lf as CRLF)}
  neither                     -> False                        (today)
```

Like with like: both sides hash raw working-tree bytes with no filter. The two folded readings give the
fallback the answer the `oid` route gives on a re-checkout, which reads through the target's clean
filter and so sees no edit where only line endings moved.

### What it does not check

An edit that changes only line endings reads unedited, as it does through a clean filter. A render the
adopter regenerates by hand after `apply` reads edited, as it does through `oid`. A row whose
re-measure was KEPT because git would not hash its file keeps `apply`'s `output_sha256` over the bytes
that run rendered, and reads edited on the next run. A render with mixed line endings that a
re-checkout makes uniform matches no reading and reads edited: the kit is held and ordered, and no
byte is lost.

### Inventory

Minted: the fixture plants `render-edited-no-oid` and `render-eol-no-oid` and the stub `oid-only` in
`tools/govkit/fixtures/retired_edits.py`. No function, conf key, gate leg, policy key or receipt
field; `check_render_edited` keeps its name and signature.

### Migration

None. The check reads a field every `apply` already writes. A target whose render the adopter edited
before its first `update` is held and ordered on that run, where today the edit is written over.

### Rollout

Live at landing, in order 5 beside TOOL-dSafePassage-5, which consumes it and builds after it.

### Files touched (estimate)

- `tools/govkit/govkit.py`
- `tools/govkit/fixtures/retired_edits.py`
- `tools/govkit/selftest.py`
- `help/update-edits.md`

### Alternatives rejected

- **Compare with the target's committed blob.** The adopter commits the edit, so the committed blob
  holds it and the comparison sees nothing.
- **Raw bytes only.** A teammate's checkout under `core.autocrlf=true` would read every untouched
  render edited, hold its kit on every run and order a restore the adopter cannot make (§8 F1).
- **Edit TOOL-dSafePassage-9.** It is CLOSED; this unit extends its check as the seam.

## 5. Production-readiness checklist

- security: no new spawn, path or write; one more read of a file the check already reads.
- perf / scale: three sha256 hashes of one rendered file per row with no `oid`, a handful per run.
- error / empty / loading states: an absent file or a row with neither field answers False, as today.
- observability: the existing `render-edited` verdict line, `HELD BACK` line and order.
- risks: a false edit holds a kit and writes an order, and loses no byte; a missed edit loses one,
  which is why the fallback errs toward holding (§4 "### What it does not check").
- testing: the two plants and the stub through the arm of §7.
- migration: none.
- user docs: `help/update-edits.md` (S3).

## 6. Acceptance criteria

- **AC1** — When `python "tools/govkit/fixtures/retired_edits.py" --plant render-edited-no-oid` runs,
  it exits 0, printing the render's recorded `oid` absent before the run, its verdict
  `render-edited`, the `HELD BACK demo:` line, one `update-render-edited-` order, and the edited bytes
  kept.
  Red when: the row with no `oid` is graded False, as `--plant render-edited-no-oid --stub oid-only`
  stages: it exits 1 with the verdict `re-rendered` and the bytes overwritten.
- **AC2** — When `python "tools/govkit/fixtures/retired_edits.py" --plant render-eol-no-oid` runs, it
  exits 0, the verdict `re-rendered` and no `update-render-edited-` order.
  Red when: the fallback hashes the raw bytes alone, so a line-ending-only rewrite reads
  `render-edited` and holds the kit.
- **AC3** — When `git grep -n -e "recorded only the bytes" -- help/update-edits.md` runs, it prints
  the paragraph's sentence, and `python "tools/govkit/docs_leg.py"` exits 0.
  Red when: the page still says a row with no render blob cannot show an edit.

## 7. Gates

`govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `govkit selfcheck` · `recall floor arms` · `policy fixtures` · `encoding posture (text IO names its encoding)` · `lexicon naming predicates` · `docs` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/govkit/selftest.py · covers AC1 AC2 · the `_rte_cases` rows (`tools/govkit/selftest.py:18329-18337`) gain the two plants and `render-edited-no-oid --stub oid-only`, the stub staging the red · none

## 8. Open questions

- **F1 — Can a raw-byte record prove an edit across a re-checkout?** `output_sha256` hashes the bytes
  one checkout held; another checkout of the same commit may hold them with other line endings.
  Options: (a) the raw hash alone; (b) the raw hash and its two line-ending folds; (c) no fallback, a
  row with no `oid` never edited, as today. (a) reads every render edited on a checkout whose
  line endings differ, holds its kit on every run, and orders a restore the adopter cannot make,
  since a fresh checkout writes the same bytes again; (c) loses the edit, the measured defect; (b)
  misses an edit that changes only line endings, which the `oid` route misses too, since it reads
  through the target's clean filter, the rule DEPL-aRepatriatedFork-17 S2 sets for this file's own
  verify (`tools/govkit/govkit.py:5618-5622`). RESOLVED (agent, 2026-10-27, delegated): (b), rung 1,
  read from that record and the `oid` route it must agree with. widens: none · relaxes: none
- **F2 — How this unit binds to the clause.** The brief asks for `cl-dClosedLoop-0022` carried as
  TOOL-dSafePassage-62 carries it, and that spec, CLOSED, reads `part 2/2`. The carries join
  (`tools/check-spec-tokens.py:1019-1029`) requires one total across carriers and parts 1 to n, so a
  third carrier reds it until 62's line reads `part 2/4`, an edit to a CLOSED spec the brief's
  non-goals forbid. Options: (a) carry `part 3/4` and leave 62's line to the main loop; (b) bind
  `**Derived:** TOOL-dSafePassage-5`, as the README roster's row for 62 already reads.
  RESOLVED (agent, 2026-10-27, delegated): (b), rung 1, the brief's own non-goal deciding between
  two of its items. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, from TOOL-dSafePassage-5's third build-pass measurement of an
  edited render written over on the first `update`, by
  `2026-10-27-prompt-TOOL-dSafePassage-5-6-spec-writer.md`.

## 10. Reuse audit

The seam extended is TOOL-dSafePassage-9's `check_render_edited` (`tools/govkit/govkit.py:9382-9393`),
whose one caller (`:10445`) already holds the kit and routes the row to the ordered arm, and `_sha`
(`:8800-8801`), the hash `apply`'s `output_sha256` is spelled with. `python
tools/codebase-map/reuse_lookup.py "prove a rendered file was edited from the sha256 its install
recorded when no blob oid was stamped"` ranked `records`, `stamp`, `read_blobs_at` and `blob_oid`,
name-token matches: `blob_oid` hashes a git blob, not the raw bytes `output_sha256` names, and none
grades a rendered row, so no existing seam fits beyond the check itself. The recall probe found
DEPL-dRemeasuredRender-1, which stamps `oid` from the second run on, and DEPL-aLevelledCopy-1's
`eol-only` predicate, the line-ending rule §8 F1 follows.

Recall terms used: `python tools/memory-recall/query.py "how does update decide a rendered file was edited when its receipt row has no recorded blob" --terms "render-edited oid output_sha256 rendered row re-measure held kit regenerate edit lost apply receipt"`
