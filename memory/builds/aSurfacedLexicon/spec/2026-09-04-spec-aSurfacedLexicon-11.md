# TOOL-aSurfacedLexicon-11 — the canon overlay and its stamp

**Status:** SPECCED · rev-5 · 2026-09-05 · node a · Tier-2 · base 6c670b02 · streams tooling · order 6

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-05-review-TOOL-aSurfacedLexicon-8-spec-audit-round1.md](../reviews/2026-09-05-review-TOOL-aSurfacedLexicon-8-spec-audit-round1.md) | spec-audit | TOOL-aSurfacedLexicon-8 TOOL-aSurfacedLexicon-12 |
| [2026-09-05-review-TOOL-aSurfacedLexicon-8-spec-audit-round2.md](../reviews/2026-09-05-review-TOOL-aSurfacedLexicon-8-spec-audit-round2.md) | spec-audit | TOOL-aSurfacedLexicon-8 TOOL-aSurfacedLexicon-12 |

<!-- /gen:spec-records -->

## 1. Goal

Give the frozen canon a door the owner can open, where opening it is visible on every run and refused
without a written reason. The ruling is that the canon ships FROZEN and the owner CAN unfreeze it;
today there is no door at all, so the posture is welded rather than frozen and an adopter who disagrees
with a cluster has no supported move.

The label `R2` for that ruling is the RESEARCH record's, not the rulings record's, and rev-3 corrects
the cite. In `memory/builds/aSurfacedLexicon/build/`, the file
`2026-09-04-build-TOOL-aSurfacedLexicon-1-rebuild-research.md:510` is `### R2 — the canon door`, and
the owner's own words are
`memory/builds/aSurfacedLexicon/README.md:47-49`. The canonical rulings record,
`memory/builds/aSurfacedLexicon/build/2026-09-04-build-TOOL-aSurfacedLexicon-1-owner-rulings.md`,
tabulates Q1 through Q10 and carries no canon row at all — `grep -n 'canon\|frozen\|unfreeze\|R2'`
over it returns nothing. Two records label rulings under two schemes; this spec now says which one it
is quoting.

## 2. Scope (IN)

- **S1** — A `CANON:` block key in the declaration and a `canon_unfrozen=` scalar beside it. The scalar
  format is a date, a node tag and a reason. `tools/lexicon/lexicon_conf.py:34`'s `_SCALAR_RE` accepts
  any identifier key already, so the scalar needs no reader work; only the block key does.
- **S2** — The overlay merges at the CLUSTER TABLE, not inside `build_form_index()`. `canon.py` gains
  one function, `build_clusters(overlay_rows, clusters=CLUSTERS)`, returning the merged tuple, and
  `build_form_index`, `read_gloss` and `render_negative` each grow an optional `clusters=CLUSTERS`
  parameter. A caller that has a declaration merges once and passes the merged tuple to every accessor
  it reads; a caller that has none passes nothing and gets today's answer.
- **S2a** — Merging inside `build_form_index()` is what rev-1 and rev-2 specified and it is WRONG, so
  the correction is recorded rather than quietly applied. Two of the canon's three accessors never call
  that function: `read_gloss` iterates `CLUSTERS` itself at `tools/lexicon/canon.py:100` and
  `render_negative` at `:115`. Re-measured at base `6c670b02` with
  `grep -rn "canon\.\|build_form_index\|CLUSTERS\|read_gloss\|render_negative" tools/ --include=*.py`,
  the product path reads TWO of them — `TOOL-aSurfacedLexicon-7`'s S3 grafts both
  `canon.build_form_index()` and `canon.read_gloss()` into `run_suggest` and into the offender line at
  build order 5 — so an overlay merged only in the index would resolve a form to an owner-declared
  representative and then print the SHIPPED gloss for it, or the empty string. The defect is inherited
  verbatim from the research record's R2 section, whose own words are that `build_form_index()` "is
  already the one place every consumer resolves a form" — a sentence that spans two lines there, so
  this spec cites the CLAIM rather than a line number that lands on its middle. It is not, and rev-2's §10 could not see it because it re-ran
  `grep -rn build_form_index tools/` — a probe that by construction cannot find a `CLUSTERS`-direct
  reader. §10 now greps the DATA.
- **S2b** — An ADD row must carry at least one alternative, refused at merge time when it does not.
  `tools/lexicon/canon.py:117` renders a negative from `others[0]`, and
  `tools/lexicon/lexicon.py:504-509` reds a `VERBS` row carrying no negative, so a representative with
  no alternatives is a cluster that can never render one. An ADD row carries no GLOSS either — a
  `CANON:` row is a cluster and a gloss is a `VERBS` row's job — so `read_gloss` returns `""` for an
  added representative and the advice half prints the negative alone. That is a limit, not a bug, and
  S8 records it.
- **S3** — Row semantics, all three directions. A row naming an existing representative REPLACES that
  cluster's alternatives; a row naming a new representative ADDS a cluster; a leading minus DELETES a
  shipped cluster. A minus row naming NO shipped cluster RAISES; it is not a silent no-op. A no-op
  would let an owner's typo count as an owner declaration on the posture line while changing nothing,
  which is a posture that lies in the one place this unit exists to make honest.
- **S4** — VISIBLE. `tools/lexicon/lexicon.py` prints the unfrozen posture above the counts on every
  run, green as well as red. A run that prints nothing means the canon is frozen, and there is no state
  in which it is quietly overridden.
- **S5** — RECORDED. A `CANON:` block with an empty `canon_unfrozen` is a REFUSAL, on the
  `lexicon wiring` leg, which carries `guard: []` in `tools/gate-legs.json` so a conf-only diff fires
  it. The stamp must carry a date, a node AND a reason; a date alone records that it happened, not why.
  The refusal is CONDITIONAL on a block being present, and the detection route is named rather than
  left to the implementer: `lexicon_conf.py` gains `--print-canon <conf>` beside its existing
  `--print-verbs` and `--print-rows` (`tools/lexicon/lexicon_conf.py:154-181`), printing one overlay
  row per line and exiting 0 with NO output when no block is declared. Not a grep:
  `tools/lexicon/adopt-lexicon.sh:216-217` already rules a second parser in this script out by name,
  and `:218` is the shell-out it rules in. This repo declares no block, so the false-refusal branch —
  every kit-less adopter redding an unguarded leg — is exercised by the real bar on every run, and AC10
  names it.
- **S6** — CRLF-hardened, using the shape `tools/lexicon/adopt-lexicon.sh:226` already proves out for
  the `ratified` arm: strip carriage returns FIRST, then unquote. An anchored quote-strip alone leaves
  a lone carriage return as a non-empty value, so a CRLF conf would pass the refusal exactly when it
  should fire.
- **S7** — A STRUCTURAL GUARD: `tools/lexicon/scaffold_lexicon.py` may never emit a `CANON:` header, so
  the mirror cannot return through the proposal path. Asserted on the `lexicon naming predicates` leg,
  which the push bar runs, and deliberately not on the kit selftest, which it does not.
- **S8** — The honest limit, written into the conf comment and the kit README rather than left for a
  reader to discover, and graded by AC12 rather than left to a reviewer's eye.
- **S9** — THE UNFREEZE IS OBSERVED ON A LEG THE PUSH BOUNDARY RUNS.
  `bash tools/lexicon/adopt-lexicon.sh --check`
  gains one SELF-EXERCISING arm that does not depend on this repo declaring anything: it makes a
  scratch tree with `mktemp -d` plus `git init -q`, writes a conf carrying a stamped one-row `CANON:`
  block, runs the product CLI's `--suggest` there, and asserts BOTH that the posture line prints and
  that the answer names the OVERLAY's representative rather than the shipped one. The idiom is the
  kit's own — `tools/lexicon/selftest.py` stands up a scratch `git init -q` tree seven times, at
  `:94`, `:439`, `:595`, `:710`, `:730`, `:756` and `:974` — and it is the same scratch-declaration
  discipline `TOOL-aSurfacedLexicon-5`, `-7` and `-13` use for armed cells. Without this arm every
  criterion that exercises the merge sits on `lexicon selftest`, chunk `selftests`, which
  `GATE_FULL=1` does NOT reach and no boundary sets: the unit whose whole subject is a behaviour
  change would ship its behaviour-change evidence on a leg nobody runs. Cost is bounded by
  construction — `run_suggest`'s docstring at `tools/lexicon/lexicon.py:786-790` forbids a corpus
  pass, so the arm is one `git init` and one declaration read against the leg's declared 330 s.

## 3. Non-goals (OUT)

- **No `role = "seed"` flip on `tools/lexicon/canon.py`.** See §4's rejected alternatives; the flip
  buys an override with an upgrade regression.
- **No unfreeze machinery for the surface-by-convention default table.** That table is exogenous by the
  same argument the clusters are, has no ranking step in it to corrupt, and is read by
  `tools/lexicon/scaffold_lexicon.py` alone, so it cannot become a mirror.
- **No overlay effect on what is LEGAL.** The canon grades nothing. It decides what a machine may
  propose and how an offender is labelled as debt or unruled. Only a `VERBS` row a human wrote
  legalises a name, and `tools/lexicon/lexicon.py:504-509` reds a row carrying no negative, so a
  hand-written row is born failing the gate until somebody writes the boundary word. rev-2 cited
  `:503-511`, which starts one line early on `neg = build_negatives(conf)` and runs two past the
  refusal into the next check's comment.
- **No automatic re-pinning.** An overlay moves definitions between the debt and unruled buckets, and
  under owner ruling Q2 both pins are two-sided, so the run reds until the `PINS:` block is re-pasted.
  That is the design working; this unit does not paper over it.
- **No new gate leg.** THREE existing legs gain arms, not two: `lexicon wiring` takes the stamp
  refusals and S9's self-exercising arm, `lexicon naming predicates` takes the S7 structural guard,
  and `lexicon selftest` takes the merge arms. §7 owns that list; rev-2's "two" was a count authored
  in §3 for a population §7 already enumerated.

## 4. Design

### Data model

`CANON:` rows are a representative followed by its alternatives, whitespace separated, matching the
shape the shipped clusters already have at `tools/lexicon/canon.py:55-80`. A leading minus on the
representative deletes the shipped cluster of that name and takes no alternatives.

`build_clusters(overlay_rows, clusters=CLUSTERS)` is the one merge, and `build_form_index`, `read_gloss`
and `render_negative` each grow an optional `clusters=CLUSTERS` parameter that defaults to the shipped
tuple. Every existing call site compiles unchanged and the frozen-by-default posture is the module's
default rather than a caller's discipline. Two survive to this unit's landing, not three:
`tools/lexicon/lexicon.py:1065` sits inside `run_probe`, whose AST span is `:1053-1136` and which
`TOOL-aSurfacedLexicon-3` deletes at build order 1, five orders before this unit. rev-2 corrected that
arithmetic in S2 and left this sentence saying three; rev-3 corrects the sentence.

`tools/lexicon/canon.py` imports nothing today and must keep importing nothing. The overlay reaches it
as plain rows, never as a conf object, so the canon does not gain a dependency on the reader and the
kit's own layering stays what it claims.

The disjointness property the function's docstring names at `tools/lexicon/canon.py:87-88` — a form in
two clusters would make the answer depend on iteration order — has to survive the merge. Post-merge
disjointness is asserted rather than assumed, because an overlay row is the first way a duplicate form
can enter at all. (`:86` is blank; rev-2 cited `:86-88`.)

### Consumers, and which of them the overlay reaches

Enumerated at THIS unit's landing order rather than at the run base, because two units move the set
before it. Re-derived at base `6c670b02` with
`grep -rn "canon\.\|build_form_index\|CLUSTERS\|read_gloss\|render_negative" tools/ --include=*.py`.

| Consumer | Canon entry points it reads | Overlay reaches it |
|---|---|---|
| `run_suggest`, `tools/lexicon/lexicon.py:785-852` | `build_form_index` and `read_gloss`, both grafted by `TOOL-aSurfacedLexicon-7`'s S3 at order 5 | YES |
| the DEBT/UNRULED offender line, same file, same graft | `build_form_index` and `read_gloss` | YES |
| `build_seed`, `tools/lexicon/scaffold_lexicon.py:121`, `:147`, `:192` | `build_form_index`, `CLUSTERS`, `read_gloss` + `render_negative` | NO |
| `tools/lexicon/selftest.py:686`, `:689`, `:696`, `:698` | all four | NO by default; its own arms pass one explicitly |
| `run_probe`, `tools/lexicon/lexicon.py:1065`, `:1101`, `:1114` | `build_form_index` and `CLUSTERS` | deleted at order 1 |

**Why the scaffold not receiving the overlay is acceptable, stated rather than assumed.** It has no
declaration to read. `scaffold_lexicon.py`'s `main` takes exactly one argument, a destination PATH
(`:98-105`), derives everything else from the corpus, and
`grep -n load_conf tools/lexicon/scaffold_lexicon.py` returns nothing.
The only supported route to it refuses to run where an overlay could exist:
`tools/lexicon/adopt-lexicon.sh:247-249` refuses `--scaffold` on an existing `.lexicon.conf`. So a
declaration carrying a `CANON:` block and a run of the scaffold are mutually exclusive states, and
there is no reachable case where the scaffold misses an overlay that exists. That also disposes of the
consequence a merge-point-only fix would have had to chase: `read_gloss` returning `""` for an ADD
representative, seeding a `VERBS` row that `tools/lexicon/lexicon.py:504-509` reds, cannot arise on a
path that never sees the row.

### Inventory

Identifiers this unit mints, each with the cell that grades it and its `--suggest` verdict:

| Identifier | Cell | Verdict | Role |
|---|---|---|---|
| `build_clusters` | `py.function` | OK, leads with the declared `build` | the one merge, in `tools/lexicon/canon.py` |

**Pin delta: ZERO.** `python tools/lexicon/lexicon.py --measure` at base `6c670b02` prints
`VERB_OFFENDER_PIN="461"`, matching `.lexicon.conf:164`, and `build` is a declared row, so the one
minted definition is not an offender. The `clusters` and `overlay_rows` parameters and the
`--print-canon` flag are not definitions and no cell grades them. The verdict above is
`python tools/lexicon/lexicon.py --suggest build_clusters`, run before this rev landed; `apply_overlay`
and `merge_overlay`, the two obvious names, both return `is not in the declared table` and would each
have raised the pin by one.

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

**SEQUENCING, because the generated build-order table will say otherwise.** This unit shares build
order 6 with `TOOL-aSurfacedLexicon-8`, which was opened and read rather than inferred: its own
status header reads `order 6`, its Files-touched paragraph names `tools/lexicon/lexicon.py` and
`tools/lexicon/selftest.py`, and its §4 says the block it replaces is `tools/lexicon/lexicon.py:837-846`
inside `run_suggest` at `:785-852`. This unit routes its overlay through the `build_form_index` and
`read_gloss` calls `TOOL-aSurfacedLexicon-7` grafts into that same function. So the write sets
intersect on two files and inside one function, BUILD-METHOD M6 requires the two units to be SEQUENCED,
and dispatching them together is forbidden. The README's generated table renders `Parallel: yes` for
this step, derived from the step holding two units and not from any disjointness it checked; that
over-claim is filed as `TOOL-aSurfacedLexicon-17` (OPEN, `memory/backlog/TOOL.md:341`). Read the write
sets, not the column. This spec does not assert that the sibling carries the matching sentence —
`TOOL-aSurfacedLexicon-8` is another unit's file and owes its own half of this pair.

### Files touched (estimate)

- `tools/lexicon/canon.py` — `build_clusters`, the `clusters=` parameter on all three accessors, the
  post-merge disjointness assertion, the ADD-row and absent-delete refusals.
- `tools/lexicon/lexicon_conf.py` — `CANON` in `BLOCK_KEYS` (`:32` today), its rows through the generic
  default parse that `TOOL-aSurfacedLexicon-4` adds, and the `--print-canon` output shape in `_main`.
- `tools/lexicon/lexicon.py` — the posture line, and the merged tuple reaching BOTH canon calls
  `TOOL-aSurfacedLexicon-7` grafts, not the `:1065` site inside the deleted `run_probe`.
- `tools/lexicon/adopt-lexicon.sh` — the empty-stamp and reasonless-stamp refusals beside the existing
  `ratified` arm at `:226-234`, and S9's self-exercising scratch-conf arm.
- `tools/lexicon/scaffold_lexicon.py` — no functional change; it is the SUBJECT of the S7 guard and, per
  the consumers table above, the one canon reader the overlay deliberately does not reach.
- `tools/lexicon/selftest.py` — the no-overlay equality arm (AC5), the three row-semantics arms (AC6),
  the three refusal arms (AC7), and the S7 guard's own failing case. §6 owns that population; no count
  is authored here.
- `.lexicon.conf` and `tools/lexicon/README.md` — the commented block and the honest limit.

`memory/map/generated/symbols.json` is NOT in this list and the omission is deliberate rather than
missed. `build_clusters` is a new public definition in an already-indexed module: that artifact
carries three rows for `tools/lexicon/canon.py`, one each for `build_form_index`, `read_gloss` and
`render_negative`, so the unguarded
`codebase-map coverage + freshness` leg selects the landing commit — verified in
`tools/gate-legs.json`, where that leg carries no guard key, chunk `declarations`, subject `repo`,
ceiling 300. The regenerated artifact rides in the same commit under §1's claim-edits-regen rule, and
the leg is listed in §7 rather than here because it is a gate obligation, not a hand edit.

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

A second limit, smaller and concrete: an ADDED cluster has no GLOSS. A `CANON:` row declares a cluster
and a gloss is a `VERBS` row's job, so `read_gloss` returns `""` for an added representative and the
advice half prints the negative alone until the owner writes the matching `VERBS` row. The overlay
changes what may be proposed; it does not write the sentence that says what the verb means.

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
- error / empty / loading states — five refusals with distinct messages: an empty stamp, a stamp with
  no reason, a `CANON:` block whose merge would leave a form in two clusters, an ADD row carrying no
  alternative (S2b), and a minus row naming no shipped cluster (S3). The last two are rev-3 additions;
  rev-2 declared three and left the two undefined branches a small config grammar always grows.
  The NEGATIVE branch is a state, not a refusal, and it is graded too: a conf with no `CANON:` block
  must exit 0, which is this repo's own state on every bar (AC10).
- observability — the posture line on every run, green included, which is the whole S4 argument. Green
  output is where a reader stops looking, so that is where the fact sits.
- risks (concurrency, data-loss, rollback hazards) — the interaction with owner ruling Q2 is the real
  one. An overlay moves definitions between the debt and unruled buckets, both two-sided pins, so a
  stamped overlay reds the bar until the `PINS:` block is re-pasted. Rollback is deleting the block.
- testing + left-shift gates — the AC5, AC6 and AC7 arms in `tools/lexicon/selftest.py`, the S7 guard's
  failing case observed on the `lexicon naming predicates` leg, and S9's self-exercising arm on
  `lexicon wiring`.
  The staged breaks are AC1's empty stamp, AC8's staged `CANON:` header and AC11's suppressed merge —
  three, each named in its own criterion. The count here is derived from §6 rather than authored
  beside it.
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
  as well as one that exits non-zero. Both cases are observed, and the route to the exit-0 case is
  named rather than left for the implementer to find: an overlay moves definitions between the debt and
  unruled buckets, so the first run after declaring one reds on the two-sided pins; run
  `python tools/lexicon/lexicon.py --measure`, paste its emitted pin block back into `.lexicon.conf`,
  and the next run exits 0 with the posture line still printed. That command prints the three pins and
  nothing else — verified at base `6c670b02`, where it returns `VERB_OFFENDER_PIN="461"`,
  `SUFFIX_OFFENDER_PIN="0"` and `LAYER_OFFENDER_PIN="0"`.
- **AC5** — When no `CANON:` block is declared, no posture line is printed and every canon accessor
  called with no `clusters` argument returns exactly what it returns from the SHIPPED tuple, asserted
  by a `tools/lexicon/selftest.py` arm that compares against `canon.CLUSTERS` in the same process. The
  comparison is against the module's own constant, not against a remembered reading at a sha: rev-2
  pinned this criterion to base `d0a18683`, which is outside this run, and a pass condition anchored to
  a tree nobody has checked out is one a later reader must fetch to evaluate.
- **AC6** — When an overlay row names an existing representative its alternatives are replaced, when it
  names a new representative a cluster is added, and when it leads with a minus the cluster is deleted.
  Three `tools/lexicon/selftest.py` arms, one per direction, each asserting the change through
  `build_clusters(rows)` and then through ALL THREE accessors given that tuple — `build_form_index`,
  `read_gloss` and `render_negative` — because two of the three never call the index and an arm that
  checks only the index is the probe that missed this defect for two revisions.
- **AC7** — When an overlay row would put one form in two clusters, `build_clusters` raises rather than
  resolving by iteration order; when an ADD row carries no alternative it raises; when a minus row
  names no shipped cluster it raises. Three `tools/lexicon/selftest.py` arms, each asserting the raise
  and each asserting a message distinct from the other two.
- **AC8** — When a `CANON:` header is staged into the body `tools/lexicon/scaffold_lexicon.py` emits,
  `python tools/lexicon/lexicon.py` exits non-zero; when unstaged it exits 0. The predicate is NOT the
  bare `grep -c CANON tools/lexicon/scaffold_lexicon.py` the research record proposed: run at writing
  time on this worktree that command returns 1, matching
  `tools/lexicon/scaffold_lexicon.py:181`'s `# PROPOSED from the SHIPPED CANON` comment, so a guard
  asserting 0 would red the tree it shipped against.
- **AC9** — When the candidate guard predicate is run over the whole tracked tree from `git ls-files`
  before being wired, it prints its hits AND its near-misses, and the only near-miss it reports is
  `tools/lexicon/scaffold_lexicon.py:181`. NEAR-MISS is defined for this predicate rather than
  inherited as a word: a line the LOOSE form counts and the NARROWED form does not. The loose form is
  `grep -c CANON tools/lexicon/scaffold_lexicon.py`, re-run at base `6c670b02` and returning 1, at
  `:181`, which is `body.append(f"# PROPOSED from the SHIPPED CANON, …")`. The narrowed form matches an
  emitted BLOCK HEADER — a line the scaffold appends that begins `CANON:` — which `:181` is not,
  because what it appends begins with `#` and carries no colon.
- **AC10** — When `.lexicon.conf` declares NO `CANON:` block,
  `bash tools/lexicon/adopt-lexicon.sh --check` exits 0 and prints no stamp refusal. This is this
  repo's own state, so the real `lexicon wiring` leg observes it on every bar rather than a scratch
  fixture doing it once — which is the point: a refusal spec'd only on its firing path ships a false
  positive to every adopter who is not the author.
- **AC11** — When `bash tools/lexicon/adopt-lexicon.sh --check` runs on a tree that declares no block,
  S9's arm still stands up its scratch conf, and `python tools/lexicon/lexicon.py --suggest <form>`
  there ANSWERS with the overlay's representative for a form the shipped canon does not resolve, with
  the posture line above it. Staged break: suppress the merge in `build_clusters` and the same arm goes
  RED, observed before the arm is called landed. This is the criterion that puts the behaviour change
  on a leg the push boundary runs — `lexicon wiring` carries `guard: []`, so no diff scopes it off —
  and without it AC5 through AC7 all sit on `lexicon selftest`, chunk `selftests`, which `GATE_FULL=1`
  does not reach and no boundary sets.
- **AC12** — `grep` finds the honest-limit sentence in BOTH `.lexicon.conf` and
  `tools/lexicon/README.md`. S8 requires two carriers and rev-2 graded neither, so an implementation
  shipping the merge, the refusals and the posture line passed with the limit written nowhere.
- **AC13** — the attribution line F2 ratified, which would otherwise ship absent with nothing
  noticing. When a stamped `CANON:` overlay moves a P1 pin, the run prints a line naming the
  OVERLAY as the cause of the movement, and that line is asserted by a selftest arm that stages an
  overlay, observes the pin mismatch, and REDS if the report carries only the bare mismatch the
  ratchet already prints. Both states are observed: with the overlay staged the line is present,
  and with it unstaged the same run does not print it — an arm that only ever sees the line cannot
  tell the line from the ratchet. The arm rides `lexicon selftest`, which is chunk `selftests` and
  invisible to the push boundary, so this unit’s Definition of Done runs it explicitly under
  `GATE_SELFTESTS=1` rather than trusting the push bar — the same disclosure §7 makes for every
  other criterion in this spec.

## 7. Gates

Every value below was read out of `tools/gate-legs.json` at base `6c670b02`, not carried from rev-2.

- `lexicon wiring` — guard `[]`, chunk `wiring`, subject `repo`, ceiling 330, cmd
  `bash tools/lexicon/adopt-lexicon.sh --check`. Carries AC1, AC2, AC3, AC10 and AC11. Its EMPTY guard
  is the load-bearing property: nothing scopes it off any bar, so a conf-only diff fires it and a push
  runs it.
- `lexicon naming predicates` — guard `['tools/', 'skills/session-kickoff/', '.githooks/', '.claude/']`,
  chunk `declarations`, subject `repo`, ceiling 300, cmd `python tools/lexicon/lexicon.py`. Carries AC8
  and AC9, the S7 structural guard. Its guard names `tools/`, which every file this unit touches lives
  under, so the landing commit selects it.
- `codebase-map coverage + freshness` — NO guard key, chunk `declarations`, subject `repo`, ceiling
  300. Not named by rev-2 and it should have been: `build_clusters` is a new public definition in a
  module `memory/map/generated/symbols.json` already indexes, so this leg reds unless the artifact is
  regenerated in the same commit.
- `lexicon selftest` — guard `['tools/lexicon/']`, chunk `selftests`, subject `kit`, ceiling 880.
  Carries AC5, AC6 and AC7. Reachable ONLY under `GATE_SELFTESTS=1`, which `GATE_FULL=1` does not
  imply and no boundary sets, so nothing on this leg is evidence at a push. That is why AC11 exists.
- The memory-tree hygiene leg, for this spec.

Read as a table: of twelve criteria, seven ride a leg a push runs (AC1, AC2, AC3, AC8, AC9, AC10,
AC11), three ride an on-demand leg (AC5, AC6, AC7), and two are landing observations with no leg (AC4
and AC12, the second of which is a `grep` any reviewer can re-run). Naming that split is the point:
rev-2 put every arm that exercises the merge on the on-demand leg and said so without noticing what it
meant.

No new bar leg, so no wall-clock ceiling and no `memory/project/testsuite-count-waivers.txt` row is
owed. `tools/check-testsuite-counts.sh:36` selects only the `*.test.sh` argv strings named in
`tools/gate-legs.json`, and `tools/lexicon/selftest.py` is not one. rev-2 cited `:35`, which is the
second line of that selection's comment.

## 8. Open questions

- **The canon-door ruling is not open.** RESOLVED (owner, 2026-09-04) — recorded in the build README
  and elaborated as `R2` in the research record. The third field of that mark is a CLOSED grammar,
  `delegated` or nothing; rev-3 put a provenance clause there, which both readers score as a
  non-conforming mark and therefore as no mark at all. The provenance now sits after the mark, where
  it costs nothing. The ruling: the canon ships frozen and the owner can unfreeze it, through a
  `CANON:` block plus a reason-bearing stamp rather than a `role = "seed"` flip.
- **F1 — what shape does the S7 guard predicate take? CLOSED at rev-3, by refutation rather than by
  signature.** The research record specified `grep -c CANON tools/lexicon/scaffold_lexicon.py` equal to
  0; re-run at base `6c670b02` that command returns 1, at `:181`. The fork offered two ways out and one
  of them is barred by a rule already in force, so it was never a live branch. Option B — reword
  `:181` so the bare grep holds — makes a COMMENT's wording the gate's pass condition, which is §7's
  gate-satisfied-by-its-own-prose class by name, and the wording it would have to bend is
  `# PROPOSED from the SHIPPED CANON`, a sentence that exists to explain the canon and would be
  degraded to avoid a substring. Option A stands alone: narrow the predicate to an emitted block
  header, leave the descriptive comment untouched, and pin the surviving near-miss in the guard's own
  header so a later reader knows the count is 1 by design. AC8 and AC9 state that as fact because it
  is now the only surviving branch; rev-2 stated it as fact while the fork was still open, which is
  the defect this bullet closes. No owner signature is claimed here and none is needed — a branch
  refused by the charter is not a choice.
- **F2 — when an overlay moves the pins, does the run say so?** Under owner ruling Q2 both P1 pins are
  two-sided, so a stamped overlay reds the bar on the next run with no indication that the overlay is
  why. The alternatives are a bare pin mismatch, which is what the ratchet already prints, or a targeted
  line naming the overlay as the cause. Recommendation: the targeted line. An owner who has just
  unfrozen the canon and is then handed a pin mismatch with no attribution will read it as a bug in the
  ratchet, and diagnosing it costs more than printing it.

  **RESOLVED (agent, 2026-09-05, delegated): F2 — the targeted line, naming the overlay as the cause
  of the pin movement.** Neither option is vetoed: no acceptance criterion observes this fork, no §3
  non-goal is touched, and a report line is not a dependency, an install location, a public surface or
  a write. So the pick is the feature-richness test and the targeted line wins it outright — the bare
  mismatch is what the ratchet ALREADY prints, so that option delivers nothing this unit is not
  getting for free, and it leaves the attribution question open for whoever meets the red.
  It also serves this unit’s own purpose better: the build rule is that the unfreeze must be VISIBLE
  on every run, and a pin mismatch with no attribution is precisely the quiet unfreeze that rule
  exists to prevent — the mirror defect with an extra step. The line owes an acceptance criterion,
  because a report line nobody observes is a report line that can ship absent.

## 9. Revision log

- rev-1 · 2026-09-04 · initial draft, written against owner ruling R2 of the same date.
- rev-2 · 2026-09-04 · cross-spec audit. Three source claims corrected: the `lexicon wiring` guard is
  declared in `tools/gate-legs.json`, not in `tools/lexicon/kit.toml`; the cluster shape sits at
  `tools/lexicon/canon.py:55-80`, not at `:52`, which is a blank line; and one of the three measured
  `build_form_index` callers is `tools/lexicon/selftest.py`, which is the kit's own suite. S2 and §4
  now also record that the `:1065` caller is deleted by `TOOL-aSurfacedLexicon-3` at build order 1,
  four orders before this unit lands.
- rev-3 · 2026-09-05 · spec audit round 1 fold, rows 3, 8, 9, 11, 20, 23, 24, 27, 30, 31, 32, 33, 34
  and 37. The blocker was a DESIGN defect, not a number: the merge point moved from inside
  `build_form_index()` to the cluster tuple itself, because two of the canon's three accessors iterate
  `CLUSTERS` directly and never call the index, and §4 now enumerates every consumer with whether the
  overlay reaches it and why the scaffold's exclusion is unreachable rather than merely tolerated. S9
  and AC11 put the behaviour-change evidence on `lexicon wiring`, guard `[]`, because every arm that
  exercised the merge sat on a leg no boundary runs. The base is re-pinned from `d0a18683` to
  `6c670b02` and every figure re-measured at it, which corrected four cites (`canon.py:87-88`,
  `lexicon.py:504-509`, `check-testsuite-counts.sh:36`, and the surviving-caller count in §4) and
  confirmed the rest. F1 is closed by refutation, the `R2` label is re-cited to the record that
  defines it, two undefined grammar branches got refusals, an Inventory mint table with a `--suggest`
  verdict and a measured pin delta of zero was added, and the order-6 write-set collision with
  `TOOL-aSurfacedLexicon-8` is sequenced — that sibling was opened and read, and carries its own half.
- rev-4 · 2026-09-05 · the research-record cite now names the CLAIM rather than a line number that lands on
  its middle — the quoted sentence spans two lines there. Cross-spec rev pins dropped, and the
  false clause saying the order-6 sibling still owes its half is corrected: it carries it.
- rev-5 · 2026-09-05 · §8 made READABLE by the two machine readers that grade it, and F2 RESOLVED.
  The canon-door mark carried a provenance clause in the third field, which is a closed grammar —
  `delegated` or nothing — so both readers scored a conforming-looking mark as no mark at all and
  the whole section read unresolved. F2 was genuinely open and is ratified as the targeted
  attribution line, with AC13 added because a report line nobody observes can ship absent.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "merge an owner declaration overlay over a frozen shipped
cluster table and stamp the override"` returns no seam this unit can use. Its top ranked candidates are
`owners_of` in `tools/codebase-map/map_lib.py` at fan-in 3 and `merge` in `tools/settings-merge.py` at
fan-in 2, and neither is reachable: the first sits on the far side of the ratified direction that the
map may read the lexicon and the lexicon may not read the map, and the second merges settings JSON with
no cluster or representative semantics at all. No existing seam fits, and the evidence is that the
lookup's whole ranked list is other kits' helpers. Both fan-in figures were re-run at base `6c670b02`
and both still read 3 and 2, with `owners_of` the only one over the printed
`SEAM_FANIN_THRESHOLD` of 3.

**The audit this section is grepped over is the DATA, not the accessor.** rev-2 re-ran
`grep -rn build_form_index tools/` and concluded that function was where every consumer resolves a
form. That probe cannot see a `CLUSTERS`-direct reader, so it could not have found the defect it was
run to rule out — a guard reading the same state the bug corrupts. rev-3 greps the data instead:
`grep -rn "canon\.\|build_form_index\|CLUSTERS\|read_gloss\|render_negative" tools/ --include=*.py`
returns 21 lines across four files. Eight of them sit outside `tools/lexicon/canon.py` and the kit's
own selftest, in exactly two files — three in `tools/lexicon/lexicon.py` and five in
`tools/lexicon/scaffold_lexicon.py`, two of the latter being prose comments — and §4's consumers table
is that output read straight.
What it shows is that the canon has THREE accessors, that `read_gloss` and `render_negative`
iterate `CLUSTERS` themselves at `tools/lexicon/canon.py:100` and `:115`, and that
`tools/lexicon/scaffold_lexicon.py` reads two of the three without ever touching the index. The
extension point is therefore the cluster tuple, reached through one new `build_clusters` and an
optional `clusters=` on all three accessors — in-kit, below the map's seam threshold, and invisible to
the lookup either way.

Recall terms used: `python tools/memory-recall/query.py "why does the canon ship frozen and what makes
an owner override visible and recorded" --terms "canon CLUSTERS frozen mirror anti-mirror overlay
unfreeze stamp ratified declaration engine role visible every run refusal"`.
