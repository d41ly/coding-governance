# TOOL-aRepatriatedFork-18 — the test suites that arm gov's gates reach adopters

**Status:** CLOSED · rev-3 · 2026-09-24 · node a · Tier-2 · base a7c78ad2 · streams tooling · order 4

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-24-build-TOOL-aRepatriatedFork-18-1-acceptance-ledger.md](../build/2026-09-24-build-TOOL-aRepatriatedFork-18-1-acceptance-ledger.md) | journal | — |
| [2026-09-23-prompt-TOOL-aRepatriatedFork-18-build-brief.md](../prompts/2026-09-23-prompt-TOOL-aRepatriatedFork-18-build-brief.md) | journal | — |
| [2026-09-24-review-TOOL-aRepatriatedFork-2-closing-diff-round1.md](../reviews/2026-09-24-review-TOOL-aRepatriatedFork-2-closing-diff-round1.md) | diff-review | DEPL-aRepatriatedFork-1 TOOL-aRepatriatedFork-2 TOOL-aRepatriatedFork-3 TOOL-aRepatriatedFork-4 TOOL-aRepatriatedFork-5 TOOL-aRepatriatedFork-6 TOOL-aRepatriatedFork-7 TOOL-aRepatriatedFork-8 TOOL-aRepatriatedFork-9 TOOL-aRepatriatedFork-10 TOOL-aRepatriatedFork-11 TOOL-aRepatriatedFork-12 DEPL-aRepatriatedFork-13 DEPL-aRepatriatedFork-14 TOOL-aRepatriatedFork-15 TOOL-aRepatriatedFork-16 DEPL-aRepatriatedFork-17 TOOL-aRepatriatedFork-19 DEPL-aRepatriatedFork-20 DEPL-aRepatriatedFork-21 TOOL-aRepatriatedFork-21 |

<!-- /gen:spec-records -->

## 1. Goal

gov ships `tools/memory-tree/check-arms.py` to every adopter as a `subject = "repo"` leg
(`tools/memory-tree/kit.toml:263-267`), and that gate demands a positive assertion for every `fail`
branch of every tracked gate in the adopter's tree, read from the gate's SIBLING `<stem>.test.sh`
(`tools/memory-tree/check-arms.py:133-150`, `:184-200`). gov also WITHHOLDS those siblings from
adopters (`TOOL-aQuenchedHarness-3`). So each pull ships gates with new branches and no arms for
them, and gate-arms stays red until someone hand-merges gov's suites into the adopter's stale copies.
This unit ships the arm-bearing suites with their gates, makes them runnable at an adopter's prefix,
and ships gov's own pins for its unarmable branches, so an update arrives armed.

## 2. Scope (IN)

- **S1** — The suites that are the check-arms sibling of a SHIPPED gate move from
  `role = "project-owned"` to `role = "engine"` in their descriptors, and their legs stay where
  `TOOL-aQuenchedHarness-3` S2 put them, as `[[exempt_leg]]` rows in `tools/govkit/registry.toml`.
  The adopter receives the FILE, which check-arms reads, and not the LEG, which the owner ruled off
  adopter bars on 2026-08-23. §4 `### Inventory` names the population. `check-microformats.test.sh`
  is the precedent: its descriptor already ships gate and suite together
  (`tools/govkit/entries/check-microformats.kit.toml`). The memory-tree, unattended and
  kickoff-manifest kits move their version constants, to 2.92, 1.32 and 1.7, and playbook-render
  moves to 1.6 because `tools/govkit/registry.toml` is in its shipped set. `govkit epoch --base
  f8fdd873` orders a bump after a kit's last move, so an earlier bump in this build does not cover
  this unit's. Observed by AC1, AC2 and AC9.
- **S2** — One canonical block, `derive_self_rel`, in a new `tools/lib/kit-rel.sh`: the `.git`
  boundary walk `tools/check-wiring.sh:31-47` and `tools/unattended/adopt-unattended.sh:63-69`
  already carry, printing the file's OWN directory relative to the repo root. Each S1 suite carries
  it inline between `# >>> derive_self_rel` markers where it names its own directory
  repo-relatively, and the same byte-identity scan `tools/lib/resolve-python.test.sh:99` runs for
  `resolve_python` covers it. Every suite's `${KIT_REL:-tools}` or `${KIT_REL:-tools/<kit>}` default
  becomes that derived value, which settles `TOOL-dRetiredFork-39` for this population: the variable
  was "set by nothing" and carried two meanings. It means the kit's own directory everywhere now;
  `unattended.test.sh`, where it meant the tool root, derives `TOOL_REL` beside it. Five suites carry
  the block: the three unattended suites, `check-method-carriers.test.sh`, whose fixture now installs
  its leg at `$KIT_REL`, and `check-memory-hygiene.test.sh`, whose scaffolded-inside arm does the
  same. `check-line-length.test.sh` names its gate as `$HERE`'s sibling and
  `manifest-check.test.sh` finds its readers through its checker's own functions (S3), so neither
  names its own directory repo-relatively and neither carries a block. Observed by AC5.
- **S3** — Each S1 suite finds a SIBLING kit's file the way its checker does, never by a second
  spelling. `skills/session-kickoff/manifest-check.test.sh:684-688` clones the host repo and copies
  `tools/memory-tree/corpus_ids.py`, and `:1104-1106` hides `tools/memory-recall/extract.py`; both
  follow `resolve_id_reader` in `skills/session-kickoff/manifest-check.sh:351-357` instead. Observed
  by AC5.
- **S4** — A gov-only dependency in a shipped suite is an announced skip, never a FAIL. The one
  measured instance is `tools/unattended/unattended.test.sh:4481-4510`: it FAILs when
  `check-spec-tokens.py` is not beside the kit, while `tools/govkit/registry.toml` exempts that file
  from every adopter, so the arm is red at every adopter by construction. In gov the file is present
  and the arms run; a gov-side disappearance still reds, through a branch that FAILs when the suite sits in a kit source,
  one whose govkit registry is beside the kit. The assertion floor in
  `tools/check-testsuite-counts.sh` was the rev-1 answer and does not reach this suite, which is no
  leg in `tools/gate-legs.json`. Observed by AC6.
- **S5** — Gov's pins for branches no fixture can reach travel with their gates. check-arms reads,
  besides `<MEMORY_ROOT>/project/unarmed-branches.txt` (`check-arms.py:51`, `:203`), a sidecar
  `unarmed-branches.txt` in each gate's own directory, whose gate column is the path RELATIVE TO THAT
  DIRECTORY. gov moves its 15 rows for `tools/unattended/unattended.sh` and
  `tools/unattended/check-unattended.sh` into `tools/unattended/unarmed-branches.txt`, which ships as
  `engine`. Shrink-only, stale-signature and vanished-branch checks apply per file, and a branch
  pinned in both files is a refusal. Observed by AC3.
- **S6** — An adopter that forks a gate arms its OWN branches in `<stem>.local.test.sh`, which
  check-arms reads beside `<stem>.test.sh` and which no descriptor ever claims. The shipped suite
  then stays byte-identical to gov's. Observed by AC4.
- **S7** — The seven helper names in `tools/memory-tree/check-memory-hygiene.test.sh` (`ev`,
  `evterms`, `evonlyt`, `evskel`, `evwrap` at `:210-232`; `pk_set` at `:2512`; `pk_out` at `:2564`)
  are renamed to declared verbs through `python tools/lexicon/lexicon.py --suggest`, and gov's
  `VERB_OFFENDER_PIN` (`.lexicon.conf:195`) moves down by what `--measure` then reports. Observed
  by AC7.
- **S9** — check-arms drops a command substitution from a signature as it drops a variable. Found
  while building S5: `check-unattended.sh`'s check 21 branch 1 ends `repair with
  $(derive_index_repair)`, so its signature kept the call's SOURCE, which no run prints, and gov's
  own `--check` was red on it before this unit touched a pin. Observed by AC3's `--check` exiting 0.
- **S8** — The class gate. `python tools/govkit/govkit.py selfcheck` (`tools/govkit/govkit.py:1159`)
  asserts that every landable file check-arms' `discover()` predicate classifies as a gate has a
  landable sibling suite. A new gate shipped without its arms is then red in gov, before any adopter
  pulls it. Observed by AC1.

## 3. Non-goals (OUT)

- Running the shipped suites on an adopter's bar. The leg half of `TOOL-aQuenchedHarness-3` stands:
  an adopter that copy-installs a checker and never edits it gains nothing from re-running gov's
  suite, and gov's bar already runs it. inCMS runs none of `unattended.test.sh`,
  `check-unattended.test.sh` or `check-memory-hygiene.test.sh` as a leg today (its
  `scripts/gate-legs.json`, read 2026-09-23); those files exist there only as check-arms' arm corpus.
- `.githooks/pre-push.test.sh`. It is not in check-arms' population, which reads tracked `*.sh`
  only, and its gov-only red-first control (nc carve-out 25) is the pre-push unit's.
- `tools/check-wiring.test.sh` and `tools/push-main.test.sh`. Both already ship as `engine`; their
  `tools/` literals are fixed by the units that own their checkers, the first by consuming S2.
- `tools/unattended/check-brief-recorded.test.sh`'s silenced fixture `cp` (nc carve-out 30). It is
  diagnostic only (audit-C), shipped already, and not an arming defect.
- Arming gov's 15 pinned branches. Each row carries a reason no fixture can reach it
  (`memory/project/unarmed-branches.txt`); S5 moves them, and arming any is separate work.

### Edges

- **hands-off** `TOOL-aRepatriatedFork-19` — the check-wiring suite consumes S2's canonical block.
- **consumes-from** `TOOL-aRepatriatedFork-2` — S3 makes `manifest-check.test.sh` follow its
  checker's `resolve_id_reader`, which probes only `tools/memory-tree` and `memory-tree`
  (`skills/session-kickoff/manifest-check.sh:353`). At inCMS, where `corpus_ids.py` sits at
  `scripts/`, the checker prints "id citations unchecked" and the suite has nothing true to follow
  until that probe is derived.
- **consumes-from** `DEPL-aRepatriatedFork-17` — at an adopter the S1 suites are receipt rows whose
  role moves from `project-owned` to `engine`. Today such a `role-moved` row can be resolved only
  by `apply`, which overwrites; that unit's S6 resolves it where `update` reports it. AC8 rests on
  that.

## 4. Design

### Data model

The measured failure, with gov's own predicate: `discover()`, `branches()` and
`armed_signatures()` from `tools/memory-tree/check-arms.py` at a7c78ad2, run over inCMS's blobs at
6ca2d0b38's parent (old gate, old suite), at 6ca2d0b38 with the parent's suite (new gate, old suite),
and at 6ca2d0b38 (new gate, hand-merged suite). PINNED 2026-09-23:

| inCMS gate | old/old unarmed | new gate, old suite | new/new |
|---|---|---|---|
| `scripts/unattended/unattended.sh` | 6 of 194 | 28 of 213 | 7 of 213 |
| `scripts/unattended/check-unattended.sh` | 8 of 178 | 17 of 186 | 8 of 186 |
| `scripts/check-memory-hygiene.sh` | 1 of 32 | 1 of 32 | 0 of 32 |
| `scripts/manifest-check.sh` | 1 of 29 | 1 of 29 | 1 of 29, pinned by hand |

31 new unarmed branches arrived with the pull, and 6ca2d0b38 cleared them by hand-merging five
suites, 3,160 changed lines by `git show --numstat`; its message records `unattended.test.sh` at 53
failures before that. nc ran the same
hand merge (a1a81474, 898ebb67) and raised `VERB_OFFENDER_PIN` 1799 to 1806 at a9eaa34b for exactly
S7's seven names.

The sidecar pin is the same four-field row `parse_pin` reads (`check-arms.py:203-216`) with one
difference: the gate column is relative to the sidecar's directory, so
`unattended.sh	9	1	cannot stage the run-state file…` means the same branch at
`tools/unattended/` and at `scripts/unattended/`.

### Inventory

The S1 population, derived by `discover()` over gov's tree on 2026-09-23 and intersected with the
landable gates (PINNED; S8 re-derives it on every selfcheck):

| Suite | Gate branches | Rule today |
|---|---|---|
| `tools/memory-tree/check-memory-hygiene.test.sh` | 32 | `project-owned`, `tools/memory-tree/kit.toml:43` |
| `tools/memory-tree/check-method-carriers.test.sh` | 6 | same rule |
| `tools/unattended/unattended.test.sh` | 213 | `project-owned`, `tools/unattended/kit.toml:37` |
| `tools/unattended/check-unattended.test.sh` | 186 | same rule |
| `tools/unattended/check-playbook.test.sh` | 23 | same rule, plus its two fixture records at `:129-130` |
| `tools/check-line-length.test.sh` | 6 | `project-owned`, `tools/govkit/entries/check-line-length.kit.toml` |
| `skills/session-kickoff/manifest-check.test.sh` | 29 | `[[exempt]]`, `tools/govkit/registry.toml:275-276` |

Not in it: `check-playbook-parity.sh` and `check-template-size.sh`, whose gates are registry
exemptions that never ship.

Minted names: the file `tools/lib/kit-rel.sh`, the shell function `derive_self_rel` and its markers,
the sidecar name `unarmed-branches.txt`, and the suffix `.local.test.sh`. The repo's `.lexicon.conf`
declares no `sh` cell, so the function name is graded by the verb table only, and `derive` is a
declared verb. S7's replacement names come from `--suggest` at build time.

### Migration

gov: seven descriptor rules or rows change, the 15 pin rows move file, and gov's own check-arms run
must read identically before and after (AC3). No leg is added to or taken from gov's bar.

### Adopter deletions

inCMS, once update delivers the S1 suites as `engine`:

| Artefact | Where | Action |
|---|---|---|
| `KIT_UNATTENDED_TEST_DELTA` | kits.json divergence `scripts/unattended/unattended.test.sh` | deleted |
| `KIT_UNATTENDED_CHECK_TEST_DELTA` | kits.json divergence `scripts/unattended/check-unattended.test.sh` | deleted; its inCMS-only A2 arm for `--emit-index` moves to `check-unattended.local.test.sh`, and F2 to F5 are gov bugs to confirm fixed at the pull |
| `KIT_PLAYBOOK_TEST_DELTA` | kits.json divergence `scripts/unattended/check-playbook.test.sh` | deleted; its 48 repaths are S2 |
| `KIT_MANIFEST_TEST_DELTA` | kits.json divergence `scripts/manifest-check.test.sh` | deleted |
| `kits.unattended.files` suite rows | kits.json | `diverged` to `engine` |
| 15 rows for `scripts/unattended/*.sh`, 1 for `scripts/manifest-check.sh` | `scripts/unarmed-branches.txt` | deleted; the file keeps the 30 rows for inCMS's own `check-docs-hygiene.sh` |

nc: the 18 rows for `scripts/unattended/*.sh` in `memory/project/unarmed-branches.txt` shrink to the
branches nc's own fork adds; `VERB_OFFENDER_PIN` falls by seven; carve-out 6's check-90 arm moves out
of `scripts/check-memory-hygiene.test.sh` into `check-memory-hygiene.local.test.sh`.

### Files touched (estimate)

- `tools/lib/kit-rel.sh`
- `tools/lib/resolve-python.test.sh`
- `tools/memory-tree/check-arms.py`
- `tools/memory-tree/kit.toml`
- `tools/memory-tree/check-memory-hygiene.test.sh`
- `tools/memory-tree/check-method-carriers.test.sh`
- `tools/unattended/kit.toml`
- `tools/unattended/unattended.test.sh`
- `tools/unattended/check-unattended.test.sh`
- `tools/unattended/check-playbook.test.sh`
- `tools/unattended/unarmed-branches.txt`
- `tools/check-line-length.test.sh`
- `tools/govkit/entries/check-line-length.kit.toml`
- `tools/govkit/entries/kickoff-manifest.kit.toml`
- `tools/govkit/registry.toml`
- `tools/govkit/govkit.py`
- `skills/session-kickoff/manifest-check.test.sh`
- `memory/project/unarmed-branches.txt`
- `.lexicon.conf`

### Alternatives rejected

- **check-arms stands down on an unmodified vendored gate.** If the receipt says the gate is gov's
  engine at a recorded OID, gov's bar already armed it, and the adopter could skip it with an
  announcement. It needs no shipped suite. It fails the case that exists: inCMS's
  `unattended.sh` and `check-unattended.sh` are forks (6ca2d0b38 "merge a7c78ad2 into the lighter
  inCMS forks"), and a forked gate is exactly where arming matters. It also makes a memory-tree kit
  file read govkit's receipt. Worth revisiting once the other units in this build let adopters run
  these gates verbatim; §8 F1.
- **Ship suites and legs both.** Reverses the owner's 2026-08-23 ruling for no gain; check-arms
  reads the text and never runs it.
- **Keep the pins adopter-authored.** That is today, and inCMS re-keyed gov's rows by hand at
  6ca2d0b38 ("check 49 pins follow gov's renumbering").

## 5. Production-readiness checklist

- security — N/A: the change moves test files and pin rows; no new write path, input or egress.
- perf / scale — no adopter bar runs more. check-arms reads one more pin file per gate directory and
  one optional `.local.test.sh` per gate.
- error / empty / loading states — a `.local.test.sh` that exists and is empty arms nothing and is
  not an error; a sidecar row naming a gate that is not in its directory is the same stale-row
  refusal the central pin already raises (`check-arms.py:290-295`).
- observability — `check-arms.py --report` names which file armed or pinned each branch.
- risks — S1 ships 15,538 lines of suite text into every adopter that selects these kits (PINNED
  2026-09-23, `wc -l` over the §4 `### Inventory` suites). The alternative is those adopters
  writing them by hand every pull, which is what happened twice on 2026-09-23.
- testing — S8's selfcheck arm and check-arms' selftest arms for S5 and S6, each observed red first.
- migration — per §4 `### Migration` and `### Adopter deletions`; the role move needs the update
  handling the Edges name.
- user docs — `tools/memory-tree/README.md` states the sidecar and `.local.test.sh`; the two
  `kit.toml` comments explaining the withholding are rewritten to explain the new split of file
  and leg.

## 6. Acceptance criteria

- **AC1** — When `python tools/govkit/govkit.py selfcheck` runs it exits 0; with the unattended
  driver's suite staged back into `tools/unattended/kit.toml:37`'s `project-owned` rule, it exits
  non-zero naming `tools/unattended/unattended.sh` and its sibling.
  Red when: a shipped gate's suite is withheld and selfcheck is silent.
- **AC2** — When `python tools/govkit/govkit.py apply` installs `memory-tree`, `unattended` and
  `kickoff-manifest` at prefix `scripts` into a scratch target, every S1 suite is present there, and
  the installed `check-arms.py --check` run in the target exits 0 with no pin file authored by the
  target.
  Red when: a suite is withheld and check-arms raises "is missing, but its gate has `fail` branches".
  cost: one three-kit apply into a scratch target, about two minutes.
- **AC3** — When the 15 rows live in the sidecar under `tools/unattended/`,
  `python tools/memory-tree/check-arms.py --check` in gov exits 0 and `--report` lists the same 15
  pinned branches it listed at a7c78ad2; with one row staged into both files it exits 1 naming the
  duplicate.
  Red when: the sidecar is not read and the 15 branches report as unpinned.
  figure: 15 is PINNED 2026-09-23 from `memory/project/unarmed-branches.txt`.
- **AC4** — When `python tools/memory-tree/check-arms.py --selftest` runs, it carries an arm in which
  a fixture gate's branch is asserted only in the gate's local suite and reads armed, and the same
  fixture without that file names the branch.
  Red when: `armed_signatures` reads only the shipped sibling.
- **AC5** — When `git grep -nE 'KIT_REL:-tools|cp "\$GOVROOT/tools/memory-tree' -- <each S1 suite>`
  runs it prints nothing, and `git grep -c '^# >>> derive_self_rel'` counts one block in each of the
  five S1 suites S2 names as naming their own directory repo-relatively.
  Red when: a suite keeps gov's prefix as its default or copies a sibling kit from gov's layout.
- **AC6** — When `git grep -n 'the spec-token checker is not beside this kit' -- tools/unattended/`
  runs, the line it prints is a `skip` line naming the registry exemption, and no `FAIL` shares it.
  Red when: the branch still sets `st=1`.
- **AC7** — When `python tools/lexicon/lexicon.py --list` runs, none of the seven S7 names appears,
  and `--measure` prints the `VERB_OFFENDER_PIN` value `.lexicon.conf` declares.
  Red when: a helper keeps an unruled verb, or the pin was not lowered to match.
- **AC8** — When an inCMS shared clone takes the S1 suites through `govkit update` and drops the §4
  rows, inCMS's `gate-arms` leg command exits 0 with inCMS's pin file carrying no row for the
  unattended gates or `manifest-check.sh`.
  Red when: any of the 31 branches reads unarmed, which is the 6ca2d0b38-parent state.
  permission: inCMS is another repository; observed in a scratch clone, editing nothing there.
  fixture: needs `DEPL-aRepatriatedFork-17`'s role-move handling, and inCMS's forked `check-arms.py`
  must read the sidecar too, which is the check-arms convergence unit's work.
  carried (rev-2): observed by `DEPL-aRepatriatedFork-20`, the unit that converges inCMS's engines
  onto gov's. Until it lands inCMS's `gate-arms` leg runs inCMS's own fork, which reads neither the
  sidecar nor a `.local.test.sh`, so no build of this unit can make it pass.
  cost: one update plus one check-arms pass, a few minutes.
- **AC9** — When `bash tools/check-kit-versions.sh` runs it exits 0 after the memory-tree,
  unattended and kickoff-manifest descriptors change what they ship.
  Red when: a kit's shipped set grew and its version constant did not move.

## 7. Gates

`govkit selfcheck` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `harness arms (fail branches armed or pinned)` · `check-arms selftest` · `python resolver (behaviour + inline parity + idiom ban)` · `lexicon naming predicates` · `kit version markers` · `memory-hygiene self-test` · `method-carriers self-test` · `manifest-check self-test` · `line-length gate selftest` · `scratch-guard self-test` · `recall floor` · `recall floor arms` · `testsuite counts (every bar self-test prints one)`

New arm: `tools/govkit/selftest.py` · a descriptor fixture shipping a gate with `fail() {` while its
sibling suite is `project-owned` · none

New arm: `tools/memory-tree/check-arms.py --selftest` · a sidecar-pinned branch, a doubly pinned
branch and a `.local.test.sh`-only arm, each against the a7c78ad2 reader · none

New arm: `tools/run-gates/run-selftests.sh` budget row · installs the S1 suites at a `scripts/`
prefix in a scratch target and runs each there, so S2 to S4 are proven by execution rather than by
grep · the held-leg budget gains one row · PARKED at rev-2 in the run-state file: a unit pass runs
no suite, so this leg's red case could not be observed before it landed, and running the suites at
a foreign prefix also needs the fixture-internal kit paths inside them repathed, which only that
execution can verify

## 8. Open questions

- **F1 — ship the suites, or let check-arms stand down on unmodified vendored gates?** Option (a):
  S1 as specified. Option (b): §4's first rejected alternative. Recommendation: (a) now, because
  both adopters fork these gates today and (b) cannot arm a fork. Revisit (b) once the gates run
  verbatim at both adopters, when it would let S1's files leave again.
  RESOLVED (owner, 2026-09-23): (a), ship the suites now; revisit (b) once both adopters run the
  gates verbatim, as recommended.
- **F2 — does reversing the file half of `TOOL-aQuenchedHarness-3` need an owner ruling?** The
  2026-08-23 ruling withheld the files because a copy-installed adopter "never edits" the checker.
  check-arms makes the adopter READ the suite whether it edits the checker or not, which the ruling
  did not weigh; its spec never mentions check-arms. Recommendation: put S1 to the owner as a
  narrowing of that ruling to legs, not a reversal.
  RESOLVED (owner, 2026-09-23): S1 is ratified as a NARROWING of `TOOL-aQuenchedHarness-3` to legs
  only; the files ship, the legs stay withheld.
- **F3 — should the S1 suites' execution proof be a bar leg or a held leg?** Running
  `unattended.test.sh` and `check-unattended.test.sh` in a scratch adopter is minutes of wall.
  Recommendation: a held leg with a budget row, as the third `New arm:` states, run once per build.
  RESOLVED (owner, 2026-09-23): a held leg with a budget row, run once per build, as recommended.

## 9. Revision log

- rev-1 · 2026-09-23 · initial draft, from the brief's unit 18, audit-D §4, audit-C's nc rows, and
  the check-arms measurement over inCMS's 6ca2d0b38 blobs taken for this spec.
- rev-2 · 2026-09-24 · built. S1: no second version bump, because all three constants already
  moved since base `f8fdd873` and the epoch gate reads them clean. S2: five suites carry the block,
  not seven, and `unattended.test.sh` gains `TOOL_REL`; AC5 moved to match. S4: the gov-side red is
  a kit-source branch, since the counts floor does not reach that suite. S9 added, the
  command-substitution signature, found red at gov HEAD while building S5. AC8 carried to
  `DEPL-aRepatriatedFork-20`. Section 7's third `New arm:` parked.
- rev-3 · 2026-09-24 · S1 corrected: rev-2's "no second bump" read the epoch gate over an
  uncommitted tree, and once committed it named all four kits, because it orders a bump after the
  kit's last move. The four bump, and AC9's observation is taken after that.

## 10. Reuse audit

The seams are two existing mechanisms. For S2, the inline canonical block that `resolve_python`
established and `tools/lib/resolve-python.test.sh` gates: `derive_self_rel` is a second member of
that pattern, not a new one, and the walk it carries already exists twice. For S1, the
`project-owned` claim `TOOL-aQuenchedHarness-3` used is simply narrowed, and
`check-microformats.kit.toml` shows a suite shipping as `engine` beside its gate today.
`reuse_lookup.py` found no seam for arm distribution, returning `armed` in `corpus_ids.py` and
`check` families that do not touch pins or siblings, which is the evidence none fits for S5 and S6;
both extend `check-arms.py`'s own `parse_pin` and `armed_signatures`.

Recall terms used: `withheld`, `project-owned`, `self-test`, `sibling`, `check-arms`,
`unarmed-branches`, `ARMS_FLOORS`, `exempt_leg`, `LANDABLE_ROLES`, `silenced_legs`,
`aQuenchedHarness`, `pin`.
