# TOOL-aSurfacedLexicon-11 — the canon overlay and its stamp

**Status:** SPECCED · rev-2 · 2026-09-04 · node a · Tier-2 · base d0a18683 · streams tooling · order 6

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

Give the frozen canon a door the owner can open, where opening it is visible on every run and refused
without a written reason. Owner ruling R2 is that the canon ships FROZEN and the owner CAN unfreeze it;
today there is no door at all, so the posture is welded rather than frozen and an adopter who disagrees
with a cluster has no supported move.

## 2. Scope (IN)

- **S1** — A `CANON:` block key in the declaration and a `canon_unfrozen=` scalar beside it. The scalar
  format is a date, a node tag and a reason. `tools/lexicon/lexicon_conf.py:34`'s `_SCALAR_RE` accepts
  any identifier key already, so the scalar needs no reader work; only the block key does.
- **S2** — The overlay merges inside `build_form_index()` at `tools/lexicon/canon.py:84`, which is
  already the one place every consumer resolves a form. Measured three callers at base `d0a18683`:
  `tools/lexicon/lexicon.py:1065`, `tools/lexicon/scaffold_lexicon.py:121` and
  `tools/lexicon/selftest.py:686`, the last being the kit's own suite rather than a product caller.
  Only two of the three survive to this unit's landing: `:1065` sits inside `run_probe`, whose AST span
  is `tools/lexicon/lexicon.py:1053-1136` and which `TOOL-aSurfacedLexicon-3` deletes at build order 1.
  The engine-side caller this unit's overlay must reach is therefore the one
  `TOOL-aSurfacedLexicon-7` grafts into `run_suggest` and the offender line at build order 5, which is
  the same substitution that unit's §4 Inventory is written to force. Resolve the site from that graft,
  not from `:1065`.
- **S3** — Row semantics, all three directions. A row naming an existing representative REPLACES that
  cluster's alternatives; a row naming a new representative ADDS a cluster; a leading minus DELETES a
  shipped cluster.
- **S4** — VISIBLE. `tools/lexicon/lexicon.py` prints the unfrozen posture above the counts on every
  run, green as well as red. A run that prints nothing means the canon is frozen, and there is no state
  in which it is quietly overridden.
- **S5** — RECORDED. A `CANON:` block with an empty `canon_unfrozen` is a REFUSAL, on the
  `lexicon wiring` leg, which carries `guard: []` in `tools/gate-legs.json` so a conf-only diff fires
  it. The stamp must carry a date, a node AND a reason; a date alone records that it happened, not why.
- **S6** — CRLF-hardened, using the shape `tools/lexicon/adopt-lexicon.sh:226` already proves out for
  the `ratified` arm: strip carriage returns FIRST, then unquote. An anchored quote-strip alone leaves
  a lone carriage return as a non-empty value, so a CRLF conf would pass the refusal exactly when it
  should fire.
- **S7** — A STRUCTURAL GUARD: `tools/lexicon/scaffold_lexicon.py` may never emit a `CANON:` header, so
  the mirror cannot return through the proposal path. Asserted on the `lexicon naming predicates` leg,
  which the push bar runs, and deliberately not on the kit selftest, which it does not.
- **S8** — The honest limit, written into the conf comment and the kit README rather than left for a
  reader to discover.

## 3. Non-goals (OUT)

- **No `role = "seed"` flip on `tools/lexicon/canon.py`.** See §4's rejected alternatives; the flip
  buys an override with an upgrade regression.
- **No unfreeze machinery for the surface-by-convention default table.** That table is exogenous by the
  same argument the clusters are, has no ranking step in it to corrupt, and is read by
  `tools/lexicon/scaffold_lexicon.py` alone, so it cannot become a mirror.
- **No overlay effect on what is LEGAL.** The canon grades nothing. It decides what a machine may
  propose and how an offender is labelled as debt or unruled. Only a `VERBS` row a human wrote
  legalises a name, and `tools/lexicon/lexicon.py:503-511` reds a row carrying no negative, so a
  hand-written row is born failing the gate until somebody writes the boundary word.
- **No automatic re-pinning.** An overlay moves definitions between the debt and unruled buckets, and
  under owner ruling Q2 both pins are two-sided, so the run reds until the `PINS:` block is re-pasted.
  That is the design working; this unit does not paper over it.
- **No new gate leg.** Two existing legs gain arms.

## 4. Design

### Data model

`CANON:` rows are a representative followed by its alternatives, whitespace separated, matching the
shape the shipped clusters already have at `tools/lexicon/canon.py:55-80`. A leading minus on the
representative deletes the shipped cluster of that name and takes no alternatives.

`build_form_index()` grows one optional parameter carrying the overlay rows and keeps today's behaviour
when it is absent, so `tools/lexicon/selftest.py:686` and the two other callers compile unchanged and the
frozen-by-default posture is the function's default rather than a caller's discipline.

`tools/lexicon/canon.py` imports nothing today and must keep importing nothing. The overlay reaches it
as plain rows, never as a conf object, so the canon does not gain a dependency on the reader and the
kit's own layering stays what it claims.

The disjointness property the function's docstring names at `tools/lexicon/canon.py:86-88` — a form in
two clusters would make the answer depend on iteration order — has to survive the merge. Post-merge
disjointness is asserted rather than assumed, because an overlay row is the first way a duplicate form
can enter at all.

### Inventory

What the unfrozen state has to be visible in, and where each carrier lives:

| Carrier | What it says |
|---|---|
| the run's own stdout | the posture, the owner row count and the stamp, on every run |
| `.lexicon.conf` | the block, the stamp, and the commented example that makes the door legible before use |
| `lexicon wiring` leg | the refusal when the stamp is empty or reasonless |
| `lexicon naming predicates` leg | the refusal when the scaffold emits a `CANON:` header |

### Migration

None. This repo declares no `CANON:` block and stamps nothing, so its form index is byte-identical and
every count is unchanged. The shipped conf carries the commented block so the capability is legible
from the file before it has ever been used.

### Rollout

The capability is inert until an owner writes both the block and the stamp, so there is nothing to land
dark and nothing to flip.

### Files touched (estimate)

- `tools/lexicon/canon.py` — the optional overlay parameter, the merge, the post-merge disjointness
  assertion.
- `tools/lexicon/lexicon_conf.py` — `CANON` in `BLOCK_KEYS`, its rows through the generic default parse
  that `TOOL-aSurfacedLexicon-4` adds.
- `tools/lexicon/lexicon.py` — the posture line, and the overlay reaching `build_form_index` at the
  call site `TOOL-aSurfacedLexicon-7` grafts, not at the `:1065` site inside the deleted `run_probe`.
- `tools/lexicon/adopt-lexicon.sh` — the empty-stamp and reasonless-stamp refusals beside the existing
  `ratified` arm.
- `tools/lexicon/scaffold_lexicon.py` — no functional change; it is the SUBJECT of the S7 guard.
- `tools/lexicon/selftest.py` — the three row-semantics arms, the no-overlay equality arm, the
  disjointness arm, and the guard's own failing case.
- `.lexicon.conf` and `tools/lexicon/README.md` — the commented block and the honest limit.

### Alternatives rejected

**`role = "seed"` on `tools/lexicon/canon.py`.** The obvious move and the wrong one.
`tools/lexicon/kit.toml:25-28` documents seed as copied once and thereafter owned by the target, so the
flip freezes an adopter's clusters at whatever kit version they first installed and silently ends canon
upgrades. It buys an override with an upgrade regression, hidden in a Python file nobody diffs as a
declaration, when the conf is the file the owner already curates.

**Re-roling `canon.py` per adopter.** Not available. `tools/lexicon/kit.toml:17-19` ships everything
under `include = "**"` with `role = "engine"`, and `kit.toml` is in that same pool, so an adopter cannot
even durably re-role the file. That is what makes today's posture welded rather than frozen.

**A stamp with a date and node but no reason.** Rejected because it records that an unfreeze happened
and not why, and why is the only thing separating a considered overlay from a mirror.

### The honest limit

No machine check can tell a considered overlay from a mirror. An owner may unfreeze the canon and fill
the block from their corpus's commonest spellings, reinstating precisely the defect
`tools/lexicon/canon.py` closes, and the difference is why the rows were chosen, which the tool cannot
see. What this unit buys is visibility and attribution, not proof: the choice is one tracked line, it
is attributed to a node and a date, it is refused without a reason, and it is printed on every single
run. The blast radius is bounded by the fact that the canon grades nothing — it only decides what may
be PROPOSED and how an offender is labelled — so an unfrozen canon cannot legalise a name by itself.
This paragraph is the record of that limit, and it belongs in the conf comment too.

## 5. Production-readiness checklist

- security — the stamp and the block are the owner's own tracked file, edited under the owner's own
  uid. Nothing running there can stop an owner clearing a stamp, and the design does not claim to. The
  standard is the same one §9 holds the unattended kit to: make the move a visible edit rather than an
  invisible habit.
- perf / scale — one dictionary merge over a table of a few dozen rows, once per run. Negligible against
  the corpus walk.
- a11y — N/A, no user interface.
- i18n — N/A. Cluster forms are ASCII English verbs by construction, and the ASCII-only splitter is a
  different unit's exposure.
- error / empty / loading states — three refusals with distinct messages: an empty stamp, a stamp with
  no reason, and a `CANON:` block whose merge would leave a form in two clusters.
- observability — the posture line on every run, green included, which is the whole S4 argument. Green
  output is where a reader stops looking, so that is where the fact sits.
- risks (concurrency, data-loss, rollback hazards) — the interaction with owner ruling Q2 is the real
  one. An overlay moves definitions between the debt and unruled buckets, both two-sided pins, so a
  stamped overlay reds the bar until the `PINS:` block is re-pasted. Rollback is deleting the block.
- testing + left-shift gates — six arms in `tools/lexicon/selftest.py`, plus the S7 guard's failing case
  observed on the `lexicon naming predicates` leg before it is called landed.
- migration / rollback — nothing to migrate; deleting block and stamp restores the frozen posture
  exactly.
- user docs — the commented block in `.lexicon.conf`, the honest limit in `tools/lexicon/README.md`.
  The rendered Skill is unchanged: it routes naming questions and does not describe the canon.

## 6. Acceptance criteria

- **AC1** — When `.lexicon.conf` carries a `CANON:` block and `canon_unfrozen=""`,
  `bash tools/lexicon/adopt-lexicon.sh --check` exits non-zero naming the empty stamp; when the stamp is
  filled with a date, a node and a reason it exits 0. The RED is observed before the arm is called
  landed.
- **AC2** — When the stamp carries a date and a node but no reason,
  `bash tools/lexicon/adopt-lexicon.sh --check` exits non-zero with a message distinct from the
  empty-stamp one.
- **AC3** — When the conf is rewritten with CRLF line endings and an empty `canon_unfrozen=""`,
  `bash tools/lexicon/adopt-lexicon.sh --check` still exits non-zero, so a carriage return cannot
  launder an empty stamp into a non-empty value.
- **AC4** — When a stamped `CANON:` block declares one row, `python tools/lexicon/lexicon.py` prints the
  unfrozen posture line with the owner row count and the stamp ABOVE the counts, on a run that exits 0
  as well as one that exits non-zero. Both cases are observed.
- **AC5** — When no `CANON:` block is declared, no posture line is printed and
  `build_form_index()` called with no overlay returns a mapping equal to the one it returns at base
  `d0a18683`, asserted by a `tools/lexicon/selftest.py` arm.
- **AC6** — When an overlay row names an existing representative its alternatives are replaced, when it
  names a new representative a cluster is added, and when it leads with a minus the cluster is deleted.
  Three `tools/lexicon/selftest.py` arms, one per direction, each asserting membership in
  `build_form_index(overlay)`.
- **AC7** — When an overlay row would put one form in two clusters, `build_form_index` raises rather
  than resolving by iteration order, asserted by a `tools/lexicon/selftest.py` arm.
- **AC8** — When a `CANON:` header is staged into the body `tools/lexicon/scaffold_lexicon.py` emits,
  `python tools/lexicon/lexicon.py` exits non-zero; when unstaged it exits 0. The predicate is NOT the
  bare `grep -c CANON tools/lexicon/scaffold_lexicon.py` the research record proposed: run at writing
  time on this worktree that command returns 1, matching
  `tools/lexicon/scaffold_lexicon.py:181`'s `# PROPOSED from the SHIPPED CANON` comment, so a guard
  asserting 0 would red the tree it shipped against.
- **AC9** — When the candidate guard predicate is run over the whole tracked tree from `git ls-files`
  before being wired, it prints its hits AND its near-misses, and the only near-miss it reports is
  `tools/lexicon/scaffold_lexicon.py:181`.

## 7. Gates

- `lexicon wiring` — guard `[]`, chunk `wiring`, subject `repo`, declared ceiling 330 in
  `tools/gate-legs.json`. Carries the stamp refusals, and its empty guard is why a conf-only diff fires
  them.
- `lexicon naming predicates` — chunk `declarations`, subject `repo`, ceiling 300. Carries the S7
  structural guard, on the leg the push bar runs.
- `lexicon selftest` — chunk `selftests`, subject `kit`, ceiling 880. Holds the six arms, and is
  reachable only under `GATE_SELFTESTS=1`, which is why AC1 through AC4 are phrased as direct
  observations rather than as that leg going green.
- The memory-tree hygiene leg, for this spec.

No new bar leg, so no wall-clock ceiling and no `memory/project/testsuite-count-waivers.txt` row is
owed. `tools/check-testsuite-counts.sh:35` selects only the `*.test.sh` argv strings named in
`tools/gate-legs.json`, and `tools/lexicon/selftest.py` is not one.

## 8. Open questions

- **R2 is not open.** RESOLVED (owner, 2026-09-04): the canon ships frozen and the owner can unfreeze
  it, through a `CANON:` block plus a reason-bearing stamp rather than a `role = "seed"` flip.
- **F1 — what shape does the S7 guard predicate take?** The research record specified
  `grep -c CANON tools/lexicon/scaffold_lexicon.py` equal to 0, and measured at writing time that
  command returns 1 on this worktree. Two ways out. Narrow the predicate so it matches only an emitted
  block header, which leaves the descriptive comment alone and grades the thing the guard is actually
  about. Or reword `tools/lexicon/scaffold_lexicon.py:181` so the bare grep holds, which makes a
  comment's wording load-bearing and will be broken by the first person who edits it for clarity.
  Recommendation: narrow the predicate, and pin the surviving near-miss in the guard's own header so a
  later reader knows the count is 1 by design.
- **F2 — when an overlay moves the pins, does the run say so?** Under owner ruling Q2 both P1 pins are
  two-sided, so a stamped overlay reds the bar on the next run with no indication that the overlay is
  why. The alternatives are a bare pin mismatch, which is what the ratchet already prints, or a targeted
  line naming the overlay as the cause. Recommendation: the targeted line. An owner who has just
  unfrozen the canon and is then handed a pin mismatch with no attribution will read it as a bug in the
  ratchet, and diagnosing it costs more than printing it.

## 9. Revision log

- rev-1 · 2026-09-04 · initial draft, written against owner ruling R2 of the same date.
- rev-2 · 2026-09-04 · cross-spec audit. Three source claims corrected: the `lexicon wiring` guard is
  declared in `tools/gate-legs.json`, not in `tools/lexicon/kit.toml`; the cluster shape sits at
  `tools/lexicon/canon.py:55-80`, not at `:52`, which is a blank line; and one of the three measured
  `build_form_index` callers is `tools/lexicon/selftest.py`, which is the kit's own suite. S2 and §4
  now also record that the `:1065` caller is deleted by `TOOL-aSurfacedLexicon-3` at build order 1,
  four orders before this unit lands.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "merge an owner declaration overlay over a frozen shipped
cluster table and stamp the override"` returns no seam this unit can use. Its top ranked candidates are
`owners_of` in `tools/codebase-map/map_lib.py` at fan-in 3 and `merge` in `tools/settings-merge.py` at
fan-in 2, and neither is reachable: the first sits on the far side of the ratified direction that the
map may read the lexicon and the lexicon may not read the map, and the second merges settings JSON with
no cluster or representative semantics at all. No existing seam fits, and the evidence is that the
lookup's whole ranked list is other kits' helpers. The extension point this unit uses instead is
in-kit and was found by reading the source rather than the map: `build_form_index()` at
`tools/lexicon/canon.py:84` is the one place every consumer resolves a form, measured at three
non-test callers with `grep -rn build_form_index tools/`, which is exactly why the overlay merges there
and nowhere else. It sits below the map's own seam threshold, so the lookup could not have surfaced it.

Recall terms used: `python tools/memory-recall/query.py "why does the canon ship frozen and what makes
an owner override visible and recorded" --terms "canon CLUSTERS frozen mirror anti-mirror overlay
unfreeze stamp ratified declaration engine role visible every run refusal"`.
