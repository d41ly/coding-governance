# TOOL-dIndexedDesign-6 — agreement and tier checks: the interface and scope axes, the tier rule as a predicate, and sibling specs read from unmerged refs

**Status:** OPEN · rev-2 · 2026-10-28 · node d · Tier-2 · base 57bc3b91 · streams tooling · order 7 · advances TOOL-dIndexedDesign-17

**Carries:** cl-dClosedLoop-0388@deaac21c whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-28-build-TOOL-dIndexedDesign-1-agent-ledger.md](../build/2026-10-28-build-TOOL-dIndexedDesign-1-agent-ledger.md) | journal | TOOL-dIndexedDesign-1 TOOL-dIndexedDesign-2 TOOL-dIndexedDesign-3 TOOL-dIndexedDesign-4 TOOL-dIndexedDesign-5 TOOL-dIndexedDesign-7 TOOL-dIndexedDesign-8 TOOL-dIndexedDesign-9 TOOL-dIndexedDesign-10 TOOL-dIndexedDesign-11 TOOL-dIndexedDesign-12 TOOL-dIndexedDesign-13 TOOL-dIndexedDesign-14 TOOL-dIndexedDesign-15 TOOL-dIndexedDesign-16 TOOL-dIndexedDesign-20 TOOL-dIndexedDesign-31 TOOL-dIndexedDesign-32 TOOL-dIndexedDesign-33 TOOL-dIndexedDesign-34 TOOL-dIndexedDesign-35 TOOL-dIndexedDesign-36 TOOL-dIndexedDesign-37 TOOL-dIndexedDesign-38 |
| [2026-10-28-build-TOOL-dIndexedDesign-1-reuse-scout-a.md](../build/2026-10-28-build-TOOL-dIndexedDesign-1-reuse-scout-a.md) | research | TOOL-dIndexedDesign-1 TOOL-dIndexedDesign-2 TOOL-dIndexedDesign-3 TOOL-dIndexedDesign-16 |
| [2026-10-28-build-TOOL-dIndexedDesign-1-spec-stage-returns.md](../build/2026-10-28-build-TOOL-dIndexedDesign-1-spec-stage-returns.md) | research | TOOL-dIndexedDesign-1 TOOL-dIndexedDesign-2 TOOL-dIndexedDesign-3 TOOL-dIndexedDesign-4 TOOL-dIndexedDesign-5 TOOL-dIndexedDesign-7 TOOL-dIndexedDesign-8 TOOL-dIndexedDesign-9 TOOL-dIndexedDesign-10 TOOL-dIndexedDesign-11 TOOL-dIndexedDesign-12 TOOL-dIndexedDesign-13 TOOL-dIndexedDesign-14 TOOL-dIndexedDesign-15 TOOL-dIndexedDesign-16 |
| [2026-10-28-prompt-TOOL-dIndexedDesign-1-spec-brief.md](../prompts/2026-10-28-prompt-TOOL-dIndexedDesign-1-spec-brief.md) | research | TOOL-dIndexedDesign-1 TOOL-dIndexedDesign-2 TOOL-dIndexedDesign-3 TOOL-dIndexedDesign-4 TOOL-dIndexedDesign-5 TOOL-dIndexedDesign-7 TOOL-dIndexedDesign-8 TOOL-dIndexedDesign-9 TOOL-dIndexedDesign-10 TOOL-dIndexedDesign-11 TOOL-dIndexedDesign-12 TOOL-dIndexedDesign-13 TOOL-dIndexedDesign-14 TOOL-dIndexedDesign-15 TOOL-dIndexedDesign-16 |
| [2026-10-28-review-TOOL-dIndexedDesign-9-spec-audit-round1.md](../reviews/2026-10-28-review-TOOL-dIndexedDesign-9-spec-audit-round1.md) | spec-audit | TOOL-dIndexedDesign-9 TOOL-dIndexedDesign-12 TOOL-dIndexedDesign-16 TOOL-dIndexedDesign-1 TOOL-dIndexedDesign-7 TOOL-dIndexedDesign-2 TOOL-dIndexedDesign-8 TOOL-dIndexedDesign-13 TOOL-dIndexedDesign-20 TOOL-dIndexedDesign-5 TOOL-dIndexedDesign-4 TOOL-dIndexedDesign-14 TOOL-dIndexedDesign-10 TOOL-dIndexedDesign-11 TOOL-dIndexedDesign-15 TOOL-dIndexedDesign-3 |

<!-- /gen:spec-records -->

## 1. Goal

gap-design-09 (`memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-gap-register.md:357`):
sub-spec agreement, tier assignment and unpushed specs are prose or invisible. Check 12 already grades
M2's ordering axis and the mirror of every §3 edge (`tools/memory-tree/check-memory-hygiene.sh:2809-2816`),
so the record calling the whole check "prose only" overstates the gap (scout A, "Where a record and the
source disagree"). This unit adds the rest of the deterministic half the walkthrough's candidate 6 names
(`memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-walkthrough.md:425-426`): the
interface and scope axes of M2's cross-read (`memory/guides/BUILD-METHOD.md:66-71`), the tier rule as a
predicate over the change's class (`memory/guides/SESSION-KICKOFF.md:116-122`), and the same build's
specs read from other nodes' pushed, unmerged branches.

## 2. Scope (IN)

Build-run preconditions this unit calls and does not build: `read_spec_section(text, tag)` in
`tools/memory-tree/design_lib.py` and the tag `section.non-goals` (TOOL-dIndexedDesign-9, I1); the overlap
record's row grammar, its `**overlaps**` acknowledgement and its join (TOOL-dIndexedDesign-2, I7).

- **S1** — The axes, one function. `check_spec_agreement(specs)` in `tools/memory-tree/design_lib.py`
  takes one build's specs, each `{path, uid, tier, order, text}`, and returns findings
  `(axis, path, detail)`, axis one of `interface`, `scope`, `tier`, in a stable order. It reads section
  bodies only through `read_spec_section`, write sets only through `read_spec_writes` (:528), and edges
  only through `read_spec_edges` (:543); it adds no section walk, no write-set reader and no edge grammar
  (I16). Observed by AC1, AC2 and AC3.
- **S2** — The interface axis. For each `**hands-off**` bullet a Tier-2 spec declares to a sibling in
  the graded population, the bullet's backticked tokens other than unit ids are its handed names; when
  NONE of them appears backticked anywhere in the target's text, the pair is a finding naming the
  producer's path, the target id and the handed names. The mirror bullet itself is check 12's existing
  reciprocity join, not this axis. Observed by AC1.
- **S3** — The scope axis. A bullet in a Tier-2 spec's `section.non-goals` body above `### Edges` that
  names exactly one sibling id `C` and a backticked path `P` (`check_dir_shaped`, :579, or a token
  holding `/` and no trailing `/`) is a finding when some other sibling's write set holds `P` and `C`'s
  does not: the bullet hands `P`'s scope to a unit that does not write it. Observed by AC2.
- **S4** — The tier predicate. `derive_tier_classes(writes, root, conf)` in `design_lib.py` returns
  the change classes a write set falls in: `cross-kit`, its paths under two or more directories that
  hold a `kit.toml` in `root`; `kit-contract`, a path that is a `kit.toml`; and `declared`, a path
  equal to or under one of the `TIER2_PATHS` values in `.memory-tree.conf`. A Tier-1 spec whose classes
  are non-empty is a `tier` finding naming each class and the path that put it there. A Tier-2 spec is
  never a finding, because a stricter tier than the rule demands is legal. Observed by AC3.
- **S5** — The CLI. `python design_lib.py --agreement [<slug>] [--ref <sha>]...` grades every build, or
  the one named, over its specs whose filename date is on or after `SPEC_AGREEMENT_CUTOFF` and whose
  status is not `CLOSED` or `WONTDO`. It prints `design-lib: agreement <axis> <path> — <detail>` per
  finding, then one population line naming the specs graded, the refs read and what it does not check
  (§4 "What it does not check"); it exits 1 on a finding, 0 on none, 2 on a spec or ref it could not
  read. With the key blank it prints one `off` line and exits 0. Observed by AC4 and AC5.
- **S6** — The unmerged refs. Each `--ref <sha>` adds the named build's specs at that commit, read by
  `git ls-tree` and `git show`; a unit id present at HEAD keeps HEAD's text, and a unit id only on a ref
  joins the population with its path printed as `<sha8>:<path>`. The same call also announces, in the
  overlap record's row grammar, each pair between a ref's live spec and a live spec at HEAD, through
  TOOL-dIndexedDesign-2's join over that widened population; nothing is written to the record, which is
  unit 2's on the default branch. Observed by AC4.
- **S7** — Check 12 runs it. After the §3 edge joins, `check-memory-hygiene.sh` runs `"$_PY"
  "$HERE/design_lib.py" --agreement` when `SPEC_AGREEMENT_CUTOFF` is set, and a non-zero exit is
  `fail 12` with the printed findings. Under `--staged` it is held with one announce line, as the edge
  joins are held (:2782-2783), because the staged set is one end of a pair. Observed by AC6.
- **S8** — The driver reads unpushed specs. `check_cross_run_overlap` (`tools/unattended/unattended.sh:3409`),
  when it has a slug, passes every ref it read and did not age out to `design_lib.py --agreement <slug>
  --ref <sha>...`, resolved beside the generator `resolve_index_generator` finds, and prints each output
  line under the prefix `unattended: agreement — `. It never refuses: the walk's contract is that it
  always returns 0 (:3409, :3516). Observed by AC7.
- **S9** — The keys and the prose. `SPEC_AGREEMENT_CUTOFF` and `TIER2_PATHS` join the defaults block of
  `check-memory-hygiene.sh` (beside :122), `tools/memory-tree/.memory-tree.conf.example` (beside :104),
  both blank, and `.memory-tree.conf`, where gov sets the cutoff strictly ahead of its corpus and
  `TIER2_PATHS="coding-governance-agents.template.md skills/session-kickoff/manifest-check.sh"`. The
  Tiers section of `tools/memory-tree/SPEC-TEMPLATE.template.md` (:374) gains one paragraph naming
  `derive_tier_classes` and its three classes; its fleet-inventory note (:90-92) names `--agreement
  --ref` as the read of unmerged specs; check 12's catalogue entry in
  `tools/memory-tree/HYGIENE.template.md` (:300) names the three axes and the key. `memory/TEMPLATE-SPEC.md`
  and `memory/HYGIENE.md` re-render from them. Observed by AC8.

## 3. Non-goals (OUT)

- M2's acceptance axis ("the overview's is implied by the union of the sub-specs'"): a judgement no
  deterministic predicate makes, left to the spec audit.
- The scope axis against the build README: the README canon has no OUT slot, so there is nothing to
  join; only siblings are read.
- The cross-build overlap join, its record, kickoff cell and `design.overlap`: TOOL-dIndexedDesign-2.
  S6 widens its population for one announcement and adds no pair rule.
- The manifest template's tier prose (`skills/session-kickoff/MANIFEST-TEMPLATE.md:92`): another kit's
  carrier; the predicate's home is the spec template, and the kickoff prose stays a pointer-free
  summary.
- Retiring or re-tiering any landed spec: every axis grades only specs at or after the new cutoff.
- Specs no remote ref carries: a spec never pushed is unreadable from another node, and S6 says so in
  its population line rather than implying coverage.

### Edges

- **consumes-from** `TOOL-dIndexedDesign-9` — `read_spec_section` and the tag `section.non-goals`, the one section reader S1 and S3 read the Non-goals body through; without it the scope axis has no body to read
- **consumes-from** `TOOL-dIndexedDesign-2` — `record.overlap`, the row grammar and `**overlaps**` acknowledgement S6 announces ref pairs in, through unit 2's join; without it S6 announces agreement findings only
- **hands-off** `TOOL-dIndexedDesign-38` — the round-1 spec audit's minors that land on this spec, report ids 11, 25 and 30, each a scope item of that batch unit

## 4. Design

### Evidence

- The edge pass emits one `E` record per bullet with its verb, target and backticked prose
  (`check-memory-hygiene.sh:2575-2589`) and one `U` record per graded spec (:2600); the join reads
  them, refuses a missing mirror, and refuses an edge against the declared order (:2785-2829).
- The unit model already carries `tier`, `writes` and `consumes` (`tools/memory-tree/gen_build_index.py:544-551`);
  nothing compares tier with the write set.
- `check_cross_run_overlap` lists remote-tracking refs merged into neither the anchor nor HEAD, ages
  them out past `OVERLAP_AGE_DAYS` (`unattended.sh:3382`, 14), reads each ref's specs' Files touched
  through `read_files_touched` (:3389) and announces shared paths; it is called at preflight with the
  run's slug (:7492) and by `--overlaps` with none (:3537).
- The template's fleet inventory says unpushed specs on other nodes are invisible
  (`memory/TEMPLATE-SPEC.md:90-92`); the Tiers section is prose (:374-386).

### The predicates, measured over the tree before choosing

A read-only probe at HEAD `4bf0f400d` ran each candidate over every spec dated on or after the cutoff it
would grade (PINNED at that commit; re-derived by re-running the same predicates through S5 once built):

| Axis | Candidate | Population | Findings |
|---|---|---|---|
| interface | none of a hands-off bullet's names backticked in the target | 2032 bullets naming a sibling | 28 |
| interface | any one name missing | 2032 | 100 |
| scope | a non-goal path some sibling writes, the bullet not naming that writer | 1361 | 1299 |
| scope | S3: the bullet names one sibling, which does not write the path | 54 | 7 |
| tier | S4 over Tier-1 specs dated from `SPEC_TIER1_CUTOFF` | 80 | 19 (15 `cross-kit`) |

The 1299 is the vacuous shape: non-goals name other units' paths as a matter of course, so that
candidate measures the template, not a disagreement. The S3 hits are real misattributions, for example
a pre-push hook a bullet hands to one sibling while another writes it. One of the seven named the root
`tools/`, which S3's `check_dir_shaped` rule excludes.

### What it does not check

Stated on the population line and here: whether a handed name means the same thing in both specs; any
section but Non-goals for scope; the acceptance axis; a tier class the write set cannot show (a changed
signature inside one kit's file, which review owns); and specs on refs nobody passed or nobody pushed.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `check_spec_agreement`, `derive_tier_classes` | functions in `design_lib.py` | `py.function`, asked at the pass |
| `--agreement`, `--ref`, `--agreement-fixture`, `--plant` | flags of `design_lib.py` | `cli.flag`, asked at the pass |
| `SPEC_AGREEMENT_CUTOFF`, `TIER2_PATHS` | conf keys | none |
| `interface`, `scope`, `tier`; `cross-kit`, `kit-contract`, `declared` | finding axes and tier classes | none |

`--agreement-fixture <dir> --plant interface|scope|tier|ref|clean` writes a scratch repository holding a
fixture build `tAgree` with the planted case, its conf setting the cutoff, so a pass observes each axis
without the suite.

### Migration

None: the cutoff is set strictly ahead of the corpus, so no landed spec is graded.

### Rollout

Live at landing for specs dated from the cutoff. Check 12's announce line for an empty population
follows the edge arms' (`check-memory-hygiene.sh:2959-2962`), so an empty population is said aloud.

### Files touched (estimate)

- `tools/memory-tree/design_lib.py`: S1-S6
- `tools/memory-tree/check-memory-hygiene.sh`, `tools/memory-tree/check-memory-hygiene.test.sh`: S7, S9
- `tools/memory-tree/.memory-tree.conf.example`, `.memory-tree.conf`: S9
- `tools/memory-tree/SPEC-TEMPLATE.template.md`, render `memory/TEMPLATE-SPEC.md`: S9
- `tools/memory-tree/HYGIENE.template.md`, render `memory/HYGIENE.md`: S9
- `tools/unattended/unattended.sh`, `tools/unattended/unattended.test.sh`: S8

### Alternatives rejected

- **The axes in check 12's awk** — lost to the brief's interface rule and to I16: the awk would hold a
  second section walk and write-set read beside `design_lib`'s · `design_lib.py:528`, :543
- **Any handed name missing, for the interface axis** — lost to the probe: 100 findings against 28,
  the extra 72 being producers that list several names of which the consumer reads one · the table above
- **Every non-goal path a sibling writes, for the scope axis** — lost to the probe: 1299 of 1361, the
  vacuous selector M3's counter-rule refuses · the table above
- **Reading remote refs inside the hygiene check** — lost to determinism: the bar's verdict would turn
  on the last fetch; the driver's walk already owns that read and passes its refs · `unattended.sh:3409`

## 5. Production-readiness checklist

- security — reads tracked blobs by `git show` with argv lists; a ref sha is validated as 40 hex before
  any git call; nothing is written outside a fixture's scratch directory.
- perf / scale — one pass over the graded specs; empty at landing; per ref, one `ls-tree` and one
  batched `show`.
- error / empty / loading states — exit 2 naming an unreadable spec or ref; the `off` line; the
  population line on an empty population.
- observability — every finding names axis, path and detail; the population line names what is not
  checked.
- risks — a false interface finding where a consumer paraphrases a name; the cutoff confines it to new
  specs, whose writers can backtick the name.
- testing — each axis planted red and clean green, the ref read, the hygiene wiring and the walk.
- migration — none.
- user docs — the spec template's Tiers section and check 12's catalogue entry; `help/` has no page on
  spec checks.

## 6. Acceptance criteria

- **AC1** — When `python design_lib.py --agreement-fixture <dir> --plant interface` runs and then
  `python design_lib.py --agreement tAgree` runs in `<dir>`, it exits 1 with one `agreement interface`
  line naming the producer spec, its target and `fixture_token`, which the target spells only as
  `fixtureToken`; under `--plant clean` the target backticks `fixture_token` and it exits 0.
  Red when: the interface plant exits 0, or the clean plant prints a finding.
- **AC2** — When `design_lib.py --agreement tAgree` runs over `--plant scope`, it exits 1 with one
  `agreement scope` line naming the bullet's spec, the named sibling and the planted path `a.py`
  under the fixture's kit directory, which a third sibling writes; under `--plant clean`, where the
  named sibling writes it, it exits 0.
  Red when: the misattributed bullet passes, or a bullet naming the real writer is a finding.
- **AC3** — When `design_lib.py --agreement tAgree` runs over `--plant tier`, it exits 1 with `agreement
  tier` lines naming `cross-kit` for the Tier-1 spec writing under two `kit.toml` directories,
  `kit-contract` for the one writing a `kit.toml`, and `declared` for the one writing a `TIER2_PATHS`
  value; the Tier-1 spec writing inside one kit and the Tier-2 spec writing across two print nothing.
  Red when: any of the three classes is missed, or the one-kit or the Tier-2 spec is a finding.
- **AC4** — When `design_lib.py --agreement tAgree` runs over `--plant ref`, whose producer spec sits only
  on `refs/remotes/origin/other`, it exits 0; with `--ref <that sha>` it exits 1, the finding's path
  printed as `<sha8>:` and the spec's path, and an overlap row in the `record.overlap` grammar for the
  ref spec's shared path.
  fixture: the plant writes the ref; nothing in the tree holds one.
  Red when: the ref spec is invisible with `--ref`, or visible without it.
- **AC5** — When `design_lib.py --agreement tAgree` runs over the interface plant with
  `SPEC_AGREEMENT_CUTOFF` blanked in the fixture's conf, it prints one line holding `off` and exits 0;
  with the key set, its last line names the specs graded and the words `does not check`.
  Red when: a blank key grades, or the population line is missing.
- **AC6** — When `bash check-memory-hygiene.sh --only 12` runs in the interface plant's directory, it
  fails check 12 printing the `agreement interface` line; with `--staged` it prints the held line and
  no agreement finding.
  fixture: the plant's conf arms `SPEC_FORMAT_CUTOFF`, `SPEC_EDGES_CUTOFF` and `SPEC_AGREEMENT_CUTOFF`.
  Red when: the finding does not fail check 12, or the staged run grades it.
- **AC7** — When the driver's preflight overlap probe runs with the slug `tAgree` in the ref plant,
  fetched as a remote-tracking ref, its output carries an `unattended: agreement —` line naming the
  ref's sha8, and the probe still returns 0.
  cost: a fixture remote and a preflight-shaped call, under a minute.
  Red when: no agreement line prints, or the probe refuses.
- **AC8** — When `grep -n "SPEC_AGREEMENT_CUTOFF" TEMPLATE-SPEC.md HYGIENE.md .memory-tree.conf.example`
  runs over the renders and the kit's example conf, each names the key, and `grep -n
  "derive_tier_classes" TEMPLATE-SPEC.md` names the predicate in the Tiers section.
  Red when: a render or the example conf omits the key or the predicate.

## 7. Gates

`memory hygiene` · `memory-hygiene self-test` · `kit/dogfood doc parity` · `policy fixtures` · `recall floor` · `recall floor arms` · `transition-audit arms` · `straggler-guard arms` · `unattended kit gate` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates`

New arm: tools/memory-tree/check-memory-hygiene.test.sh · covers AC1 AC2 AC3 AC4 AC5 AC6 · each plant red under check 12 and clean green, staged by dropping the backtick on the consumer's name · none
New arm: tools/unattended/unattended.test.sh · covers AC7 · the overlap probe over a fixture remote whose unmerged ref carries the planted sibling, staged by withholding `--ref` · none

## 8. Open questions

- **F1 — Where do the new axes run?** Options: (a) one Python function in `design_lib.py`, called by
  check 12 and by the driver's walk; (b) new awk arms in check 12's pass, beside the edge records; (c) a
  new hygiene check number. (b) cannot be called by the driver and needs a second section and write-set
  reader; (c) splits M2's axes across two checks while check 12 holds the ordering axis.
  RESOLVED (agent, 2026-10-28, delegated): (a), rung 3, the most feature-rich survivor and the reuse of
  the readers I1 and I16 name.
  grants: PLAY-dClosedLoop-3 check 12 and the overlap walk gain the agreement call. widens: none · relaxes: none
- **F2 — How is a change's class declared?** Options: (a) derived from `kit.toml` positions for
  `cross-kit` and `kit-contract`, plus a conf list `TIER2_PATHS` for project files the rule names; (b)
  every class hard-coded to gov's paths; (c) a per-spec declared class field. (b) breaks an adopter,
  whose governance template has another name; (c) is typed beside what it describes, which `[derive]`
  refuses. RESOLVED (agent, 2026-10-28, delegated): (a), rung 3; the conf list ships blank in the
  example, so an adopter derives only the kit classes until it names its own.
  grants: PLAY-dClosedLoop-3 `.memory-tree.conf` gains `TIER2_PATHS`. widens: none · relaxes: none
- **F3 — Where are unpushed specs read?** Options: (a) the driver's walk passes the refs it read to
  `--agreement --ref`; (b) the hygiene check lists remote refs itself; (c) only the template's
  inventory note changes. (b) makes the bar depend on the last fetch; (c) leaves the specs invisible.
  RESOLVED (agent, 2026-10-28, delegated): (a), rung 3: one ref selection, the walk's, and a
  deterministic bar.
  grants: PLAY-dClosedLoop-3 the overlap walk announces agreement lines. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-28 · initial draft, from the packet's Items 6, gap-design-09, the walkthrough's
  candidate 6, BUILD-METHOD M2's four axes, scout A's row for this unit, and a read-only probe of each
  candidate predicate over the tree at `4bf0f400d`.
- rev-2 · 2026-10-28 · §3 · the Edges block gains the hands-off bullet mirroring the consumes-from edge of TOOL-dIndexedDesign-38,
  promoted by the round-1 spec audit of this build; nothing else moved.

## 10. Reuse audit

The seams extended are check 12's edge pass and joins (`tools/memory-tree/check-memory-hygiene.sh:2541-2600`,
:2782-2829), `read_spec_writes`, `read_spec_edges`, `check_dir_shaped` and `read_design_conf`
(`tools/memory-tree/design_lib.py:528`, :543, :579, :479), and the driver's unmerged-ref walk
(`tools/unattended/unattended.sh:3409-3517`), each line verified at `4bf0f400d`. Scout A's citations held
at that commit; its row's `check-memory-hygiene.sh:2555-2600` opens a few lines into the pass, which
begins at :2541. `python tools/codebase-map/reuse_lookup.py "check that sibling specs of one build agree
on interface tokens scope and tier"` ranked name stems (`check`, `build`, `scope`, `read_spec_revisions`,
`parse_spec_h1`); none compares two specs, so no existing seam fits the comparison itself and S1 adds it
beside the readers it calls. `derive_parallel_step` (`gen_build_index.py:1724`) pairs one step's write
sets for the order render and grades nothing, so it was not extended.

Recall terms used: `python tools/memory-recall/query.py "how do sibling specs of one build agree on interface scope and tier, and how are unpushed specs seen" --terms "sub-spec agreement interface axis scope axis tier rule check 12 edges reciprocal unpushed specs cross-run overlap"`
