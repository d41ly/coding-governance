**Serves:** spec-audit TOOL-aQuenchedHarness-1 TOOL-aQuenchedHarness-2 TOOL-aQuenchedHarness-3 TOOL-aQuenchedHarness-4 TOOL-aQuenchedHarness-5 TOOL-aQuenchedHarness-6 TOOL-aQuenchedHarness-7

# aQuenchedHarness — spec audit of the seven-unit set, round 1

*Node `a`, 2026-09-06, unattended (authorized-by: prompt). A Tier-2 adversarial pass over the seven
specs as DESIGNS, graded against `memory/TEMPLATE-SPEC.md`, `memory/guides/BUILD-METHOD.md` M2/M3/M12
and `AGENTS.md`: a primed finder fan, a skeptic stage prompted to REFUTE each finding, one synthesis.
Every claim a finding makes about the existing tree was re-run at source before it was written here;
where a sub-claim did not survive that re-check it is named inside the finding that carried it.*

**Round: 1.** Subjects, each pinned at the blob it was read at:

- `memory/builds/aQuenchedHarness/spec/2026-09-06-spec-TOOL-aQuenchedHarness-1.md@af58516071a635f0bc29f626554d932e0b0767cf`
- `memory/builds/aQuenchedHarness/spec/2026-09-06-spec-TOOL-aQuenchedHarness-2.md@d86c7fc534534cc5c9e577a6bf4f00199ae560a7`
- `memory/builds/aQuenchedHarness/spec/2026-09-06-spec-TOOL-aQuenchedHarness-3.md@87ddf6f2e9d5f70fed48aaa81680d569e9e023c3`
- `memory/builds/aQuenchedHarness/spec/2026-09-06-spec-TOOL-aQuenchedHarness-4.md@4feee0d13bb31072d7954bc983e6e7810a83cddd`
- `memory/builds/aQuenchedHarness/spec/2026-09-06-spec-TOOL-aQuenchedHarness-5.md@13fae72641db14dfe6bc5026847785dd6dba01df`
- `memory/builds/aQuenchedHarness/spec/2026-09-06-spec-TOOL-aQuenchedHarness-6.md@9f5f81001f8dadfdd710202ceeadf2a4ebd2a767`
- `memory/builds/aQuenchedHarness/spec/2026-09-06-spec-TOOL-aQuenchedHarness-7.md@af52b8fcce36cf709cca3302b17945c80b2084f1`

Unit 8 was added mid-build and is NOT in this round's subject set.

## Verdict: BLOCKED

Six blockers stand, and five of them are the same shape: a scope item whose population was never run
over the real tree, paired with an acceptance criterion that cannot see the miss. Unit 3's filename
predicate silently removes four repository checks from every bar and from every adopter manifest,
one of them the codebase-map coverage gate `AGENTS.md` §7 forbids exempting. Unit 4 derives its
runner's population from held manifest legs and then delegates to it a script whose ten suites
contain not one held leg, so the delegation matches nothing. Unit 5 places a shared harness in
`tools/lib/`, which a landed `tools/govkit/registry.toml` declaration says ships nothing, while unit
3 keeps shipping the suites that would source it. Unit 2's declared band is derived from a per-leg
spread the ledger provably cannot hold, because that file keeps exactly one row per leg. Unit 6
picks its port set from that same untracked, partial file, so its majority-share criterion is
computed against whatever happened to run in the porting worktree. And unit 3's stated seam — a
shared manifest reader — does not exist: one consumer holds in bash, the other parses in python.
Nothing here is a matter of taste. Each blocker is a statement about the tree that was measured, and
the measurements are reproduced inline.

## Review shape

Raw 52, confirmed 29, refuted 22, unverified 1, precision 0.57.

The 29 confirmed findings consolidate to 16 distinct defects in this report, because independent
lenses landed on the same seam repeatedly: three found unit 3's predicate false positives, four
found unit 4's empty delegation population, three found the `tools/lib` placement, two each found
the ledger's single-row shape, the ledger-absence contradiction, the `WALL_LIVE` mismatch and the
nested pools, and three found the budget-versus-ceiling join. Every contributing finding id is cited
on the defect it merged into, so nothing is lost by the consolidation. The pipeline's own dedup
stage discarded none of them — the merging below is this report's editorial act, disclosed here so
the two counts can be reconciled.

## Run integrity

- Lenses: 4/4 returned, 0 DIED.
- Skeptic batches: 5/5 returned, 0 DIED.
- 0 contradictory verdicts demoted to unverified, 0 spurious verdicts discarded, 0 duplicates
  discarded by the pipeline.

Every integrity counter is zero, so the finding set is complete for the lens set that ran, and a
zero count in any dimension below is evidence rather than an artefact of a dead agent.

## Findings

| # | Sev | Unit | Address | Defect |
|---|---|---|---|---|
| B1 | BLOCKER | 3 | §2 S1/S2/S5, §3, §6 AC5 | The `is_selftest` predicate holds four `subject = repo` legs off every bar |
| B2 | BLOCKER | 4 | §2 S1/S4/S6, §6 AC6, §10 | The runner's held-legs population contains none of the suites S6 delegates to it |
| B3 | BLOCKER | 5 | §4 Inventory / Files touched, §8 F2 | The harness is placed in `tools/lib/`, which a landed declaration says ships nothing |
| B4 | BLOCKER | 2 | §4 Data model, §8 F1 | The ledger holds one row per leg, so the band's probe has an empty population |
| B5 | BLOCKER | 6 | §2 S1/S7, §6 AC4 | The port set and its majority share are computed from an untracked, partial ledger |
| B6 | BLOCKER | 3 | §4 Data model, §2 S1, §10 | The "shared manifest reader" the predicate lives beside does not exist |
| H1 | HIGH | 2 | §3 non-goal 3 vs §2 S5, §6 AC3 | The spec both forbids and requires an absent ledger to red a bar |
| H2 | HIGH | 2 | §2 S5, §5 risks | A merge-bar leg whose input is untracked, per-worktree, per-node state |
| H3 | HIGH | 1 | §2 S5, §4 Inventory (`WALL_LIVE`) | The wall's liveness flag is set by a probe of a mechanism the wall does not use |
| H4 | HIGH | 4, 5 | 4 §8 F1 with 5 §2 S3 | Two pools each read the same declared width, so the sweep runs it squared |
| H5 | HIGH | 7 | §2 S3, §6 AC4 | The budget/ceiling join contradicts units 2 and 4, and its carrier does not exist |
| H6 | HIGH | 6 | §2 S6 with §6 AC3 | The budget is set to the new reading and the AC asserts the reading is inside it |
| H7 | HIGH | 7 | §6 AC2, AC4 | No acceptance criterion names a floor, so a 1.01x change lands them all green |
| H8 | HIGH | 7 | §2 S4, §6 AC5 | The `check-pass-order.sh` rebuild S4 schedules already landed in this build's base |
| M1 | MEDIUM | 5 | §2 S1, §4 Inventory, §7 | Two of three declared verb names are lexicon offenders and the third is redefined |
| M2 | MEDIUM | 2 | §7 Gates | The `run-gates canary` is named as a bar gate, but it is held without `GATE_SELFTESTS` |
| U1 | unverified | 3 | §7 Gates | `govkit acceptance matrix` is described as running on every bar; it carries a guard |

---

### B1 — BLOCKER · unit 3 · §2 S1 and S2, with §3 non-goals, §5 risks, §6 AC3/AC5

*(confirmed by finding ids 1, 16, 42 — three independent lenses)*

S1's argv-derived `is_selftest` predicate — a path component matching `*.test.sh`, `test_*.py` or
`selftest.py`, or a `--selftest` argument — was run over `tools/gate-legs.json` at HEAD. It selects
53 of 94 legs. Exactly four of those are not held today, and all four carry `subject = repo`,
`chunk = declarations` on purpose:

- `kit/dogfood doc parity` — `bash tools/memory-tree/kit-dogfood-parity.test.sh`
- `review-protocol parity (kit vs dogfood)` — `bash tools/workflows/check-protocol-parity.test.sh`
- `codebase-map coverage + freshness` — `python3 tools/codebase-map/test_codebase_map.py`
- `marker contracts` — `bash tools/memory-tree/marker-contract.test.sh`

S2 ORs the predicate into the hold "in ADDITION" and widens only, so landing it removes all four
from every default bar. S3 then drops them from every emitted adopter manifest. One of them is the
codebase-map coverage gate, which `AGENTS.md` §5 and §7 name as a merge-bar leg never to be
exempted. It also contradicts unit 3's own §3 non-goal, "Not changing which legs run in THIS repo
today", and it re-decides by filename the exact four-leg population that `tools/run-gates/run-gates.sh`
lines 875-885 record as decided by what a FAILURE means (`TOOL-dUnstalledConvoy-30`: asking what a
leg TESTS "decided four legs wrongly").

Nothing in the spec can catch it. S5 and AC3 assert only held-implies-predicate, and that direction
is empty at HEAD, so both pass. AC5 asks only that the new held set be a SUPERSET of today's, which
four extra held legs satisfy. §5's stated mitigation — that a wrongly selected leg "is a leg this
repo would stop running and would notice" — is a hope, asserted in the one direction that cannot see
a false positive.

**Fix.** Add the converse assertion to S5: every leg the predicate selects must already carry
`subject = kit` or `chunk = selftests`, or appear in a declared, reasoned exception list. Change AC5
from superset to set EQUALITY against today's held set plus that list. Or restrict S2 so the
predicate governs the emit drop (S3) only and never widens the local hold, which is what §1's goal
actually needs.

**Left-shift gate.** A bar leg that recomputes both directions over `tools/gate-legs.json` and reds
naming any leg where `is_selftest(leg)` and the manifest's own `subject`/`chunk` hold disagree. Per
§7, run the candidate predicate over the real tree and print hits AND near-misses before wiring it;
the four rows above are the near-misses it must print today.

---

### B2 — BLOCKER · unit 4 · §2 S1, S4 and S6, with §6 AC6 and §10

*(confirmed by finding ids 2, 17, 33, 47 — four independent lenses)*

S1 derives the on-demand runner's population from `tools/gate-legs.json` "through the same hold
predicate", with "no list of suite names typed anywhere". S6 then reduces
`tools/unattended/run-unattended-gates.sh` to "a thin `--kit tools/unattended` call" into that
runner. The population and the delegation do not intersect, in either half of that script:

- Its four `--checks` rows are `unattended kit gate`, `playbook validity gate`, `unattended skill
  wiring` and `pass-order history`. All four are `subject = repo` (chunks `declarations` / `wiring`)
  in `tools/gate-legs.json`, so none is held. Verified: those are the only four unattended rows the
  manifest carries.
- Its six `--selftests` suites (`check-unattended.test.sh`, `unattended.test.sh`,
  `check-playbook.test.sh`, `cross-component.test.sh`, `adopt-unattended.test.sh`,
  `check-pass-order.test.sh`) are in neither `tools/gate-legs.json` nor `tools/unattended/kit.toml` —
  the 2026-08-23 owner ruling removed them from both. They exist only as literal `run_one` calls at
  `run-unattended-gates.sh` lines 219-224.

So `--kit tools/unattended` resolves to zero suites, S4's own liveness refusal fires on the very
filter S6 mandates, and AC6's "same verdicts as before" is unsatisfiable. AC6 exercises only
`--selftests`, so the silent loss of `--checks` and `--all` — and of `BUDGET_kit_gate`,
`BUDGET_playbook_validity_gate`, `BUDGET_skill_wiring`, `BUDGET_pass_order_history` — passes
acceptance. Unit 7 AC4 invokes `run-unattended-gates.sh --checks` and `BUDGET_kit_gate` by name, and
`tools/unattended/kit.toml` line 101 declares `--all` as this kit's compensating check, so the
delegation deletes two things a sibling spec and a landed descriptor depend on.

The same exclusion means the runner sold as covering every kit's self-tests misses the two most
expensive suites in the repo: `unattended gate selftest` (812 s) and `unattended driver selftest`
(853 s) sit in the ledger as orphan rows with no manifest leg to join to. §10's claim to "generalise
that file" rests on a seam whose population the manifest does not carry.

**Fix.** State the population as a union the spec names — held manifest legs PLUS suites a kit
declares outside the manifest — and say where the second half is declared, with an AC that the union
contains the six unattended suites by name. Or narrow S6 to the `--selftests` half, say
`run-unattended-gates.sh` keeps its `--checks` block and its four repo budgets, and extend AC6 to
compare `--checks` and `--all` verdicts too, not `--selftests` alone.

**Left-shift gate.** A leg that reds when a kit's declared self-test suites are not reachable from
the runner's derived population — i.e. an emptiness check per `--kit` filter, plus an assertion that
every `run_one` literal in a kit runner resolves to a row in whatever declaration the union names.

---

### B3 — BLOCKER · unit 5 · §4 Inventory and Files touched, §8 F2, §10; with unit 3 §3 and unit 6

*(confirmed by finding ids 5, 32, 41 — three independent lenses)*

F2 resolves that the harness "ships as part of whichever kit carries it". No kit carries it. The
Inventory places it at `tools/lib/lib-selftest.sh`, and `tools/govkit/registry.toml` carries a
permanent exemption for that path whose text is explicit: "Not a kit. It has no README, no version
constant and no adopter, and it ships nothing: it is gov-internal." `AGENTS.md` §12 says the same in
the charter's voice — `tools/lib/` is gov-internal and "every copy-installed kit carries its contents
inline instead". `tools/run-gates/kit.toml`'s header records what happens when a shipped file
ignores that: the runner "sourced `tools/lib/`, which is gov-internal and never travels, and with
that path absent it exited 2 having run ZERO legs", and the recorded fix was inlining, not sharing.

Unit 3 §3 deliberately keeps shipping the suite FILES to adopters ("an adopter who edits a kit is
entitled to its suites"). Unit 6 then rewrites those suites to source `tools/lib/lib-selftest.sh`.
An adopter therefore receives `*.test.sh` files that source a path their tree never contains, and
every ported suite breaks on first invocation — reproducing a failure this repo already recorded.
Neither unit 5 nor unit 6 has an acceptance criterion that observes a ported suite running in a
copy-installed tree, and §10's "No existing seam fits, and that is the finding" is wrong on the one
seam the charter names for exactly this case: `resolve-python.sh`'s inline canon plus the parity gate
that the `python resolver (behaviour + inline parity + idiom ban)` leg enforces. M12's candidate set
was assembled without it.

**Fix.** Re-decide F2 against the registry exemption and §12. Either adopt the `resolve-python.sh`
disposition — canonical copy in `tools/lib/`, inlined into each shipping kit, joined by an
inline-parity leg — and say so in §4, or place the harness in a kit that actually ships and add its
registry entry and descriptor `[[files]]` claim to §4 Files touched. Add the inline-canon pattern to
§10 as prior art considered, with the test that rejected it if it is rejected.

**Left-shift gate.** Extend the existing inline-parity leg to cover the new harness, and add an
acceptance arm that runs one ported suite from a fixture tree containing only the kit's own installed
files — the copy-installed shape, which is the only place this failure appears.

---

### B4 — BLOCKER · unit 2 · §4 Data model and "The refusal", §8 F1

*(confirmed by finding ids 30, 43 — two independent lenses)*

§4 states that "the ledger records the same leg under load and idle", and F1's probe is the ratio
between each leg's slowest and fastest recorded seconds. `<git-dir>/gate-ledger.tsv` holds exactly
ONE row per leg, forever. `run-gates.sh` lines 1330-1338 rebuild it from this run's rows and `awk` in
only the cached rows this run did NOT measure, then `mv` over the file. Measured: the primary tree's
ledger is 96 rows / 96 unique names, this worktree's is 46 / 46. Its fields are `name, seconds,
status, input-key, ended-at` per the code's own comment, not §4's `name, seconds, verdict, sha,
timestamp`.

So F1's probe has an empty population by construction, now and later. Its own liveness assertion then
fires and yields NO band — and with no band, S2's `--check`, S4's derivation ("derived from the
ledger's own spread, not chosen"), S5's gate leg and AC1/AC2/AC4 all have nothing to compare against.
The unit has no acceptance path from its own data model.

`TOOL-dRetiredFork-40` also settles the shape in the opposite direction on measurement: the
memory-hygiene self-test ran 443 s under load against 583 s quiet, "so the relationship is not a
multiplier and cannot be guessed", and both legs were re-declared flat at 900 s. A ratio band
re-adopts the multiplier that record rejected.

**Fix.** State in §4 that the ledger is last-writer-wins with one row per leg, and correct the field
list. Then name a source that actually carries repeated readings — `<git-dir>/gate-run/*/*.leg` keeps
per-leg seconds across runs — or re-shape the declaration as an absolute margin above the maximum
recorded reading, `dRetiredFork-40`'s settled form, and record in §4 why the multiplier shape was
refused.

**Left-shift gate.** The derivation script REFUSES and prints DEAD PROBE when its input population is
empty or single-valued, per §7's liveness rule, rather than emitting a band from one reading.

---

### B5 — BLOCKER · unit 6 · §2 S1 and S7, §6 AC4

*(confirmed by finding id 18)*

S1 selects the port set as "held legs in descending recorded seconds" from `<git-dir>/gate-ledger.tsv`.
That file is untracked, per-worktree, and holds only legs that actually ran — and held legs run only
under `GATE_SELFTESTS`. Measured: 49 held legs; this worktree's ledger backs 7 of them (sum 5584 s),
the primary tree's backs 45 (sum 7969 s). AC4's "declared majority share, computed from
`<git-dir>/gate-ledger.tsv`" is therefore computed against whatever happened to run where the build
sits. Porting the top two suites in THIS worktree clears a majority of 5584 s while leaving
`govkit selftest` (1174 s), `memory-hygiene self-test` (658 s) and the rest untouched. That is an
acceptance criterion that passes without the change working.

The most expensive self-test in the tree compounds it: the unattended `gate selftest` at a recorded
3565 s is in no manifest at all (see B2), so it can never be selected by S1 and can never be named in
S7's remainder.

**Fix.** Add a liveness precondition mirroring `TOOL-aQuenchedHarness-2` S3: the selection REFUSES
unless the ledger holds a row for every leg in the population, naming the unbacked ones, and name
`GATE_SELFTESTS=1` as the step that produces those rows. State in S1 and S7 that the population is
every kit self-test suite rather than only those carrying a manifest row, or declare the non-leg
suites out of scope explicitly.

**Left-shift gate.** The selection tool reds when any leg in its declared population has no ledger
row, printing the unbacked names — the same refusal shape unit 2 S3 already uses, applied to the
denominator instead of the numerator.

---

### B6 — BLOCKER · unit 3 · §4 Data model, §2 S1, §10

*(confirmed by finding id 29)*

§4 says the predicate "lives beside the manifest reader that both consumers already share", and §10
calls that shared reader the seam. There is no shared reader. `tools/run-gates/run-gates.sh` parses
`tools/gate-legs.json` with a single-quoted python heredoc embedded inside the shell script (lines
845-901) that flattens the manifest into `\x1e`/`\x1f`-separated rows, then holds in BASH at line 947:
`{ [ "${subjects[$i]}" = kit ] || [ "${chunks[$i]}" = selftests ]; }`. `tools/govkit/govkit.py` does
its own `json.loads(legs_path.read_text())` at lines 1360 and 1497. Two languages, two readers, no
join. §10 names `check_target_reads_subject` as the seam, but that function (govkit.py:3336)
regex-matches `KIT_RUN_GATES_VERSION` out of a target's INSTALLED runner and never touches the
manifest. §4 Files touched lists no shared module.

S1's "one function, one definition, used by both readers" is therefore unimplementable through the
seam the spec names. The build will either spell the predicate twice in two languages — the exact
drift §4 claims a derivation makes impossible — or introduce a new shared artefact, which §10's "No
new mechanism" denies.

**Fix.** Correct §4 and §10 to say what the tree holds: run-gates' hold is bash, govkit's is python.
Then choose in §2 and carry the choice as new mechanism if it is one — either (a) declare a shared
artefact and list it in Files touched, or (b) express the predicate once in the run-gates python
heredoc that already emits the per-leg row, with govkit importing nothing and the S4/S5 both-direction
assertion being the only join.

**Left-shift gate.** If the predicate ends up spelled twice, a parity leg that runs both
implementations over `tools/gate-legs.json` and reds on any leg where the two disagree — the
single-source/parity shape §7 and §12 already require for a duplicated contract.

---

### H1 — HIGH · unit 2 · §3 non-goal 3 versus §2 S5 and §6 AC3

*(confirmed by finding ids 4, 19 — two independent lenses)*

§3 forbids turning the ledger into "a file whose absence reds a bar". S5 wires `--check` into
`tools/gate-legs.json` as a bar leg, and AC3 requires that same `--check` to report UNMEASURED and
exit non-zero when the ledger is absent. Both rules are in the document verbatim and the spec
arbitrates neither. Verified premise: `gate-ledger.tsv` lives under `<git-dir>` (run-gates.sh line
158), is untracked (0 hits in `git ls-files`) and is per-worktree, so a fresh clone or a new worktree
has none until a bar completes. Under S5 plus AC3, every fresh tree reds the merge bar on its first
run for a file no checkout carries — the failure mode the non-goal exists to prevent. A guard cannot
rescue it either: the run-gates canary refuses a guard naming an untracked path.

**Fix.** Decide it in §2. Either the leg reports UNMEASURED as a REPORTED skip with §16's `skipped`
shape and stays green, with an AC pinning that a fresh clone's bar is green; or the non-goal is
struck and §3 says the ledger is now bar-load-bearing. Then rewrite AC3 to match. Do not leave both
lines standing.

**Left-shift gate.** An acceptance arm that runs the bar in a freshly created worktree with no
ledger and asserts the chosen outcome — green-with-skip or red — by name.

---

### H2 — HIGH · unit 2 · §2 S5 and §5 risks

*(confirmed by finding id 36)*

S5 makes `--check` a `subject = repo` bar leg whose only input is `<git-dir>/gate-ledger.tsv`. For a
worktree that resolves to `.git/worktrees/<name>/gate-ledger.tsv`: untracked, node-local, and holding
only the legs that ran THERE. Measured on one node, same tree: 46 rows in this worktree against 96 in
the primary. Recorded seconds are node-relative by this repo's own record —
`run-unattended-gates.sh` notes "the same leg with check 30 removed costs about 70 s here against 28 s
there, a 2.5x ratio". A ratio band over a shared tracked `ceiling` and a node-local `recorded` gives
the same tree different verdicts on different nodes and different worktrees. §5's risk paragraph
covers only the ABSENT ledger (H1) and S3/AC5 cover a leg with no row; nothing covers a ledger that is
present but partial and node-local. AC4's "reproducible from `gate-ledger.tsv` alone" is reproducible
only where it was produced.

**Fix.** Say where the derivation's inputs live. Either the derived ratios become a tracked artefact
that `--check` compares against a live re-derivation (§12's parity shape), or S5's leg is dropped and
`--check` stays an operator verb run at `--write` time. A gate leg whose verdict is not a property of
the tree is not a gate.

**Left-shift gate.** If the tracked-artefact route is taken, the parity leg compares the committed
artefact against a LIVE re-derivation, never generated-against-generated (§12).

---

### H3 — HIGH · unit 1 · §2 S4 and S5, §4 "The wall" and Inventory (`WALL_LIVE`), §6 AC4

*(confirmed by finding ids 21, 46 — two independent lenses)*

§4 designs the wall as a background watcher that sleeps in short increments, writes a breach marker
and kills the process group of every outstanding leg. That invokes no `timeout`. S4 nonetheless says
the kill goes "through the same file-captured, kill-after path the per-leg ceiling already uses",
which is `timeout -k 5s "$bound" "${argv[@]}"` at run-gates.sh:1110 and wraps exactly one command,
not a pool. §4's Inventory then pins `WALL_LIVE` to "the same single probe rather than a second one"
— `timeout -k 1s 10 true` at run-gates.sh:363 — and AC4 codifies it by keying the INERT arm on
"`timeout -k` cannot run on the host".

The flag therefore certifies a mechanism the wall does not use. On a host with no `timeout`, a
perfectly functional sleep/kill watcher is declared INERT; on a host where the group kill cannot
reach a surviving grandchild — the condition
`memory/builds/aPacedTurnstile/reviews/2026-08-20-review-TOOL-aPacedTurnstile-2.md` blocker B1 records
for MSYS — the probe still reports the wall live. That is the reassuring-zero class §7 names, inside
the unit that cites it. (One qualifier: the stall narrative in the contributing finding, descendants
holding the capture open, is weaker than stated, because the runner now redirects leg output to
`$WORK/$i.raw` rather than the command substitution B1 measured. The liveness defect is independent
of that.)

**Fix.** Restate §4 and S4 as ONE mechanism, then make S5's probe exercise that mechanism end to end:
arm a sub-second wall over a sleeping child at startup, spawn a grandchild that outlives its parent,
and observe the group kill. Set `WALL_LIVE` from that observation, keep `CEILINGS_LIVE` separate, and
rewrite AC4 to name the condition under which the chosen mechanism cannot fire.

**Left-shift gate.** A run-gates canary arm for the wall itself, alongside the existing ceiling
canary: a fixture leg with a grandchild, asserted killed within the wall's own bound.

---

### H4 — HIGH · units 4 and 5 · unit 4 §8 F1 with unit 5 §2 S3

*(confirmed by finding ids 22, 35 — two independent lenses)*

F1 resolves that the on-demand runner runs SUITES concurrently at a width "read from the same
`gate-profiles.txt` row rather than declared again". Unit 5 S3 gives `arms_report` a pool at the width
"read from the same `tools/run-gates/gate-profiles.txt` row the bar reads". Neither spec composes
them. Node `a` (16 cores, 32693 MB) selects the `capable` row, width 8, so a sweep of ported suites is
8 suites x 8 arms = up to 64 concurrent processes, each copying a scratch fixture, on a host where a
bare `/usr/bin/true` costs 319 ms — during exactly the sweep this build exists to make affordable.
The profile row's own comment declares 8 for a SINGLE pool on resource grounds ("width 8 means up to
eight scratch git repos and eight interpreters resident at once") and records that at 16 "each leg
dilates under load faster than the extra worker repays". Unit 4's ledger-seeded budgets (F2) would
then breach for a reason that is not the suite's cost. Unit 5 §5 names concurrency as a hazard only
for fixture sharing, never for composition. Both specs believe they honour one declared width, which
is why neither notices it is applied twice.

**Fix.** State the composite bound in whichever unit owns the outer pool: the outer runner resolves W
and passes the inner pool `max(1, W / outer_width)` through a named exported variable, or only one
level is concurrent. Name the variable, and add an arm asserting the observed concurrent-process count
under a sweep.

**Left-shift gate.** An arm that counts live descendant processes during a sweep and reds when the
count exceeds the profile row's declared width.

---

### H5 — HIGH · unit 7 · §2 S3 and §6 AC4, against unit 2 §3 and unit 4 §3/§2 S1-S3/AC3

*(confirmed by finding ids 20, 40, 49 — three independent lenses)*

Three specs give three answers to one question, and the authoritative fourth is already on disk. S3
asks `BUDGET_kit_gate` and the leg's `ceiling` in `tools/gate-legs.json` to "stop being two answers to
one question", and AC4 requires them "joined rather than independently authored". Unit 2 §3 ("A
ceiling is a hang bound; conflating the two is what `run-unattended-gates.sh` already warns about")
and unit 4 §3 ("Not a hang bound: a budget is a COST verdict... the two figures must not be confused")
both refuse the conflation, and `run-unattended-gates.sh`'s own comment on the sibling budget says it
"does NOT match the gate-legs.json row, and must not — that row is a kill bound... and this one is a
cost verdict. The claim that they are one figure was deleted with this edit."

S3's fallback carrier does not exist either. It defers to "whichever declaration
`TOOL-aQuenchedHarness-4` gives repo legs", and unit 4 gives repo legs none: S1 is hold-only, S2
declares "one row per held leg", and AC3 makes a missing budget a failure only for held legs.
`unattended kit gate` is `subject = repo` and never held, so there is nowhere to write it. Neither
spec says whether an unmatched budget row is an error or is ignored. Compounding it, unit 4 S6 (B2)
dissolves the file that currently carries `BUDGET_kit_gate` into a delegation while unit 7 AC4 still
invokes `run-unattended-gates.sh --checks` and that variable by name.

**Fix.** Pick one in S3. Either declare the join as a DERIVATION with a declared multiple (ceiling =
budget x N, N declared with its reading, and unit 2's band file recording that ceilings for legs
carrying a budget are computed rather than authored), or drop the join and require each file to carry
a pointer to the other with the reason the two figures differ. Then name the actual file the repo-leg
budget row lives in, add that carrier to unit 4 §2 in the same revision, and state what an unmatched
budget row does.

**Left-shift gate.** A leg asserting that every budget row resolves to a leg the runner can actually
execute, and that every leg carrying both a budget and a ceiling satisfies the declared relation
between them — so a re-authored pair reds instead of drifting.

---

### H6 — HIGH · unit 6 · §2 S6 with §6 AC3

*(confirmed by finding id 3)*

S6 lowers each ported suite's budget row "to its new reading"; AC3 asserts each ported suite is inside
that same row. As an improvement criterion the pair cannot fail — a port that made a suite 2% faster
satisfies AC3 exactly as one that made it 20x faster. Unit 6 is the unit that OWNS the target
("minutes rather than hours", §1), and unlike unit 4 it withholds nothing by non-goal: its non-goals
cover porting-every-suite, not the target. The rest of §6 does not bind it either — AC1 is arm
preservation, AC2 the guard's failing case, AC4 the share arithmetic (see B5), AC5 the unextractable
report. S5 requires before/after seconds and spawns to be recorded but sets no floor. The build can
land every AC green with the sweep still costing hours, which is the owner's original complaint.

**Fix.** Add an acceptance criterion with a number that can fail: a declared minimum improvement
factor per ported suite, or a declared ceiling for the ported set's summed seconds, derived from the
ledger baseline S5 records.

**Left-shift gate.** The budget row for a ported suite is written by the porting step and asserted
against the recorded BEFORE reading, so a port that does not clear the declared factor reds at the
step that performed it.

---

### H7 — HIGH · unit 7 · §6 AC2 and AC4

*(confirmed by finding id 37)*

No acceptance criterion pins a magnitude. AC2 requires the spawn count to fall "by a factor the build
record states", and the build record is written by this build, so 1.01x satisfies it. AC4 requires
`kit gate` to be inside `BUDGET_kit_gate`, and S3 sanctions re-declaring that budget with a fresh
reading — the file that owns it says so: "that REDS gets either fixed or re-declared with a reason,
and both of those are progress" — so raising 240 satisfies AC4 with no speed-up at all. AC1, AC3 and
AC5 are verdict-preservation and regression-arm criteria that pass regardless of speed. §4's
Alternatives-rejected refuses a ceiling raise in prose, but prose is not a criterion: this is the
"gate satisfied by its own comment" shape §7 names, in the unit whose stated reason for existing is
that three sessions raised a ceiling instead of counting spawns.

The contributing finding's secondary claim is partly overstated and is recorded as such:
`BUDGET_kit_gate = 240` is calibrated IDLE (187 s on node `a`), and the 819 s here / 3837 s on node
`a` are 8-wide-pool readings the budget's own header expects to breach, so AC4's status at HEAD is
unproven rather than failing.

**Fix.** Add an AC pinning a target: the leg's recorded seconds after the change are below a figure
declared in §2 with its reading, and `BUDGET_kit_gate` is LOWER after the unit than before. State in
§3 what the before-state is, including that the idle budget is calibrated idle.

**Left-shift gate.** A regression arm asserting the spawn count is at or below the pinned post-change
figure, so a later change that reintroduces per-item spawns reds rather than being absorbed by a
re-declaration.

---

### H8 — HIGH · unit 7 · §2 S4 and §6 AC5

*(confirmed by finding id 44)*

The `check-pass-order.sh` spawn-removal S4 proposes ALREADY LANDED and is in this build's base.
`git merge-base --is-ancestor 4042505a faaea5f5` passes, and `274aa39b` ("docs(pass-order): the
rebuild's own header, measured") is likewise in the base: the 73-line rebuild — one pass over history
into a `_SUBJ` cache, the per-commit `git log -1` and `printf | tr` removed — is recorded there at
10184 s -> 591 s -> 510 s at the current tip, summary byte-identical, all seven counters, self-test
green at 72 arms. The ledger row reads `pass-order history 591.470 ok`. §4's own Alternatives-rejected
cites that completed result as history while S4 schedules the same work. AC5 ("likewise produces
byte-identical output and a lower spawn count") grades a transformation whose per-item spawns are
already gone — the one deliberately left is the `git show` the rebuild's message refuses to remove,
because translating the anchored exclusions into globs would risk the verdict to save about 70 s. So
S4 names no remaining observable and AC5 either passes vacuously or cannot be met, while the residual
question — `pass-order history` is now sixth by recorded cost, behind four held self-tests — goes
unasked.

**Fix.** Replace S4 with either nothing, deferring to the landed rebuild, or a narrow scope: pin the
landed spawn count (S5's job anyway) and re-derive `pass-order history`'s residual from the ledger.
Restate AC5 as a regression assertion against the pinned count rather than an improvement claim, and
cite `274aa39b` as the record of where the rebuild landed.

**Left-shift gate.** The pinned spawn count becomes a regression arm on `check-pass-order.sh`, so the
landed win cannot silently erode.

---

### M1 — MEDIUM · unit 5 · §2 S1, §4 Inventory, §7 Gates

*(confirmed by finding id 52)*

Two of the three declared verb names are lexicon offenders and the third redefines a declared row.
Checked against the tool rather than by eye: `python3 tools/lexicon/lexicon.py --suggest fixture_once
--as sh.function` and the same for `arms_report` both return refusals — `fixture` and `arms` are not
in the declared closed table (`add arm build check cmd derive extract init load main measure parse
print read remove render resolve run scan seed set test write`). `arm` IS declared, but glossed "make
a dormant check live; its opposite is a check that cannot fail", not "stage a break, run the subject,
compare". `.lexicon.conf` arms the shell cell (`sh:shell-tokens:parser`, `CELLS: sh.function snake`)
against a scalar `VERB_OFFENDER_PIN="978"`, which is a two-sided equality, so two new shell
definitions move the pin and red the leg. No spec in the set names the lexicon leg in §7 —
`grep -rln lexicon memory/builds/aQuenchedHarness/` returns nothing. The leg guards on `tools/` and
unit 5 creates `tools/lib/lib-selftest.sh`, so this reds on the branch bar, not only at the lander.

**Fix.** Resolve the three names before the build with `--suggest ... --as sh.function` and record the
returned spellings in §4 Inventory; if `arm` is kept, state in §4 that it is used in the declared
sense. Per §12 the fix is a rename, not a new VERBS row. Add the lexicon leg to §7 Gates in units 5
and 6.

**Left-shift gate.** None needed — the gate exists and already grades this. The left-shift is the §7
Gates line naming it, so the refusal surfaces at the branch bar rather than at the lander.

---

### M2 — MEDIUM · unit 2 · §7 Gates

*(confirmed by finding id 27)*

§7 lists `run-gates canary` as a gate for a unit that rewrites every `ceiling` in
`tools/gate-legs.json` via `--write`. That leg carries `"chunk": "selftests"` and is therefore HELD
off every default bar by run-gates.sh line 947 unless `GATE_SELFTESTS` is set. Units 1 and 3 both
name `GATE_SELFTESTS=1` for this same leg; unit 2 is the only spec of the set that omits it, and it is
the unit most dependent on the canary's pinned-key-set assertion.

**Fix.** Add `GATE_SELFTESTS=1` to unit 2 §7 for the `run-gates canary`, matching units 1 and 3, or
drop the canary and name the leg that does run on a default bar.

**Left-shift gate.** Nothing new. This is a spec-text correction; the canary already exists.

---

## Outstanding — not cleared

### U1 — unit 3 · §7 Gates *(finding id 28, low; no usable skeptic verdict returned)*

§7 says `govkit selfcheck` and `govkit acceptance matrix` are "both `subject = repo` and on every
bar". The matrix leg carries a guard (`tools/govkit/`, `tools/playbook/`, `tools/check-microformats.sh`,
`tools/check-line-length.sh`) and is skipped on any run touching none of them. A gate list that
overstates when a leg runs invites a later reader to read a green bar on an unrelated commit as
coverage of the emit path — the green-by-absence reading §7 warns about. Suggested wording:
"`govkit selfcheck` on every bar, `govkit acceptance matrix` when its guard fires, which this unit's
edits to `tools/govkit/govkit.py` do." This is the only finding in the set with no skeptic verdict,
so it is OUTSTANDING rather than cleared; the claim about the guard is cheap to check at source before
acting on it.

## The pattern under the blockers

Five of six blockers are one habit: a population was DESCRIBED rather than ENUMERATED. B1's predicate
was never run over `tools/gate-legs.json`; B2's derived population was never intersected with the
script it delegates to; B4's and B5's inputs were never counted; B6's shared reader was never opened.
Each is paired with an acceptance criterion asserted in the one direction that cannot see the miss —
superset instead of equality, held-implies-predicate instead of both, "same verdicts" over the one
verb that survives. §7 already states the remedy in general terms ("Run a candidate gate predicate
over the real tree before wiring it, and print hits AND near-misses"). Applying it to a spec's
population before the spec is ratified — running the predicate, counting the rows, opening the reader
— would have caught all five at design time, at the cost of the five commands reproduced in this
report.

The build's own §1 target survives all of it: the owner's two asks — self-tests off the default bar
and off adopters' bars, and the suites made affordable — are still the right shape. What is BLOCKED is
this rendering of them.
