# TOOL-dTrueNorth-29 — the self-test arms this build turned red, each turned green at its cause

**Status:** CLOSED · rev-1 · 2026-10-22 · node d · Tier-2 · base 271aa59d · streams tooling · order 12

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-21-build-TOOL-dTrueNorth-29-ledger.md](../build/2026-10-21-build-TOOL-dTrueNorth-29-ledger.md) | journal | — |
| [2026-10-22-build-TOOL-dTrueNorth-29-arm-breaks.md](../build/2026-10-22-build-TOOL-dTrueNorth-29-arm-breaks.md) | journal | — |
| [2026-10-22-build-TOOL-dTrueNorth-29-deviation-31.md](../build/2026-10-22-build-TOOL-dTrueNorth-29-deviation-31.md) | deviation | — |
| [2026-10-22-build-TOOL-dTrueNorth-29-flagged-bar.md](../build/2026-10-22-build-TOOL-dTrueNorth-29-flagged-bar.md) | journal | — |
| [2026-10-21-prompt-TOOL-dTrueNorth-29-build-brief.md](../prompts/2026-10-21-prompt-TOOL-dTrueNorth-29-build-brief.md) | journal | — |
| [2026-10-22-prompt-TOOL-dTrueNorth-29-1-spec-writer.md](../prompts/2026-10-22-prompt-TOOL-dTrueNorth-29-1-spec-writer.md) | journal | — |
| [2026-10-22-prompt-TOOL-dTrueNorth-29-spec-brief.md](../prompts/2026-10-22-prompt-TOOL-dTrueNorth-29-spec-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

The flagged bar at `e583a7f42`, run at VERIFYING after every unit closed and the plain bar went green,
reds nine legs. Their red lines are excerpted in
`memory/builds/dTrueNorth/build/2026-10-22-build-TOOL-dTrueNorth-29-flagged-bar.md`. Five of those
legs carry arms this build's own diff broke. This unit turns each of those arms green by fixing its
cause, in code or in the suite's own fixture, and it loosens no assertion. Every line cited below was
read at `e583a7f42`.

| Leg | Arm | Cause in this build | Scope |
|---|---|---|---|
| `spec-tokens self-test` | the six AC6 staged breaks | each broken copy of the checker sits in a directory with no memory-tree kit beside it, so it refuses at the kit before it reaches `CLAIM_CANARY` (TOOL-dTrueNorth-16 S32) | S1 |
| `row-grammar selftest` | no sibling engine in this kit imports corpus_ids or gen_build_index | `deviation_join.py:473` imports the generator for its binding reader and header grammar (TOOL-dTrueNorth-4) | S2 |
| `tier2-review self-test` | spec-audit: a spec that is also a subject is refused, and the floor line | the arm passes `s.md` while the fixture's subject moved to a spec path (TOOL-dTrueNorth-13) | S3 |
| `unattended-build self-test` | TN5-AC3 a caller subject with no id is refused naming the field | the staged roster keeps a trailing comma, so the suite's runner cannot parse it (TOOL-dTrueNorth-5) | S4 |
| `memory-hygiene self-test` | the example conf's four `DESIGN_*` keys | the kit reads the keys out of a dict and the example declares none (TOOL-dTrueNorth-16 S37, TOOL-dTrueNorth-20 S1) | S5 |
| `memory-hygiene self-test` | check 21's two writer-test arms | the fixture plants its record under `build/`, outside the one pathspec the writer test reads (TOOL-dTrueNorth-19 S1) | S6 |
| `memory-hygiene self-test` | the partition arm | its pinned selection list lacks checks 29 and 30 (TOOL-dTrueNorth-3, TOOL-dTrueNorth-16) | S7 |

Three findings differ from the brief, each verified at source:

- The AC6 copies have refused since `fce3865a4`, TOOL-dTrueNorth-16 S32, which bound the spec
  filename date to the kit (`tools/check-spec-tokens.py:888`) and made the checker refuse when no kit
  resolves (`:1369-1373`). Before it the checker dated specs by its own pattern and needed no kit.
  TOOL-dTrueNorth-27 S5 changed how the kit is found (`:400-404`), not whether a lone copy finds one.
- The line `executed 342 assertions against a floor of 343` belongs to `tier2-review self-test`. The
  excerpt prints it under that leg and under its foreign-prefix run, and the unattended-build suite
  carries no assertion floor. The tier2-review suite reads `executed` from the runner's
  `---- <pass> passed` line (`tools/workflows/tier2-review.test.sh:2219`), so it counts passes: the one
  failing arm of S3 is the one assertion short, and no arm is unreachable.
- TN5-AC3's no-id arm has never been green. Its roster has carried the trailing comma since
  TOOL-dTrueNorth-5 added the arm at `e3603ff15`, whose pass ran no suite, and TOOL-dTrueNorth-27 S3's
  rewrite produces the same bytes as the `sed` it replaced, compared by probe.

## 2. Scope (IN)

- **S1** — The AC6 block of the spec-token suite (`tools/check-spec-tokens.test.sh:1116-1132`) writes
  its six broken copies into one directory, `$base/claims-break`, which also holds a copy of the
  resolved memory-tree kit under its resolved name, `${MEMORY_TREE_DIR##*/}`. Each copy's inline
  `resolve_kit_dir` then finds the kit by its probe rung, and the copy reaches `CLAIM_CANARY`. The six
  `sed` breaks, `check_break_refuses` and the six arms' messages are unchanged. The absolute kit
  directory `MEMORY_TREE`, assigned today at `:1634`, is assigned once beside `MEMORY_TREE_DIR`
  (`:194`), and both the AC6 block and the date-pattern arm at `:1635` read it. Observed by AC1.
- **S2** — `read_bindings` and `HDR_RE`, with the names `read_bindings` reads, move from
  `tools/memory-tree/gen_build_index.py` to `tools/memory-tree/tree_lib.py`, and the generator imports
  them back under the same names, the rule `tree_lib.py` states for a name two engines read
  (`:11-13`). `deviation_join.py` reads both from `tree_lib` at its existing import (`:135`), so
  `read_population` no longer imports the generator (`:473`). No record is classified differently and
  no output changes. The table in §4 lists every name that moves. Observed by AC2 and AC3.
- **S3** — The arm `spec-audit: a spec that is also a subject is refused`
  (`tools/workflows/tier2-review.test.sh:845-847`) passes `specs: [SPEC.subjects[0].path]`, the
  fixture subject's own path, so the arm follows the fixture wherever it moves. The harness is
  unchanged by this item. Whether it should also match a differently spelled path is §8 F1. Observed
  by AC4.
- **S4** — The TN5-AC3 no-id arm's pattern (`tools/workflows/unattended-build.test.sh:1758`) opens
  with the comma before the `id` field, `,"id":"A-tB-1","rev":1}`, so subject 0 stages as
  `{"path":"s1","blob":"abc1234"}`. That is JSON the runner's `JSON.parse` accepts (`:238`), and the
  harness reaches its pin refusal (`tools/workflows/unattended-build.template.js:1556-1569`). Observed
  by AC5.
- **S5** — `tools/memory-tree/.memory-tree.conf.example` declares `DESIGN_RECORD`, `DESIGN_BASELINE`,
  `DESIGN_VIEW` and `DESIGN_NODES`, each blank, under a comment giving its meaning, as it declares
  `LIVE_LANDED_UNCLOSED` and the other conditional keys. Blank is off under the key rule, so no
  adopter's behaviour moves. The eight sentences saying the keys are absent from the example are
  corrected in place, listed in §4. Observed by AC6.
- **S6** — The check 21 writer-test fixture (`tools/memory-tree/check-memory-hygiene.test.sh:3378-3415`)
  plants its older harness's record in the build's `reviews/` folder, named
  `2026-09-02-review-ARCH-tOne-1-w.md`, the folder the writer test's one pathspec reads
  (`tools/memory-tree/gen_build_index.py:874`, TOOL-dTrueNorth-19 S1). Its cleanup at `:3413` takes
  out the same path. Observed by AC7.
- **S7** — The partition arm's selection list (`check-memory-hygiene.test.sh:1133`) gains `29 30`, so
  it holds one id per `check_selected` call of `check-memory-hygiene.sh` again, the two calls sitting
  at `:1685` and `:1731`. Observed by AC8.
- **S8** — deviation-31, the record of this unit's addition to the roster, is written in this spec
  pass and reads with no malformed field. Observed by AC9.

## 3. Non-goals (OUT)

- `measure-legs selftest`, red at the base.
- `pre-push self-test`, green alone at HEAD in a scratch clone. Its one red arm, TOOL-aSparedSpawn-33
  AC1's bar reuse, ran beside four neighbours.
- `foreign-prefix parity (every self-test at three prefixes)`, which re-runs every self-test and so
  follows the others. Its fourth finding, `unattended gate selftest shard 8/8`, names a helper defined
  inside a shard region (`tools/unattended/check-unattended.test.sh:3805`, written by
  TOOL-dTrueNorth-7). That suite is the unattended kit's own, whose verdict the build README waives
  for this landing (`memory/builds/dTrueNorth/README.md:49`), owed with PLAY-dClosedLoop-11.
- `govkit selftest`, unless the base run says otherwise; the main loop adds it if so.
- The spec-token suite's two `parity:` arms, the measure-legs ceiling of 500 s above the 300 s bound,
  red at the base.
- The partition arm's other half, the check 26 `cache hits` count that differs between runs, red at
  the base.
- A change to the review harness for S3. §8 F1 asks it.
- A guard for the class S4 belongs to. A staged roster that is not JSON makes `run_wf`'s `JSON.parse`
  throw before the harness runs, so a `has` arm reds for the wrong reason and a `hasnt_` arm over it
  passes on a stack trace; the file holds 112 `hasnt_` arms. That guard is a separate mechanism
  (BUILD-METHOD M2) and is not built here.
- Declaring `SPEC_CARRIES_CUTOFF` in the example. No module reads it out of a dict literal, since the
  kit spells it through `CARRIES_KEY`, so the arm does not ask for it, and it stays gov's.
- A waiver row, a name added to `_pyexempt`, or a floor moved.
- Running any suite or the bar. They are the close's.

### Edges

- **consumes-from** external — the CLOSED units whose arms and code these fixes read: TOOL-dTrueNorth-4
  (the import), TOOL-dTrueNorth-5 (the TN5-AC3 arm), TOOL-dTrueNorth-13 (the fixture subject),
  TOOL-dTrueNorth-16 (the kit-dated checker, checks 29 and 30, the example wording), TOOL-dTrueNorth-19
  (the pathspec), TOOL-dTrueNorth-20 (the kit descriptor wording) and TOOL-dTrueNorth-27 (the inline
  resolver and the rewritten substitution); a frozen spec cannot write the mirroring hands-off line,
  so they are named here in prose

## 4. Design

### S1 — the copies beside a kit

The block after the `# AC6 — the staged breaks` comment becomes:

```bash
brk=$base/claims-break; mkdir -p "$brk"; cp -R "$MEMORY_TREE" "$brk/${MEMORY_TREE_DIR##*/}"
for a in active passive noun fronted; do sed "s|(\"$a\", r\"|(\"$a\", r\"(?!)|" "$LINT" > "$brk/claims-break-$a.py"; done
sed 's|CLAIM_PARTS), re\.I)|CLAIM_PARTS))|' "$LINT" > "$brk/claims-break-fold.py"
sed '/cleared by the space clause/d' "$LINT" > "$brk/claims-break-space.py"
```

and each of the six `check_break_refuses "$base/claims-break-<x>.py"` calls reads
`"$brk/claims-break-<x>.py"`. This assignment moves from `:1634` to the line after `:194`, unchanged:

```bash
MEMORY_TREE="$(unset GIT_DIR GIT_WORK_TREE; git -C "$HERE" rev-parse --show-toplevel)/$MEMORY_TREE_DIR"
```

Why it resolves. The copy's `HERE` is `$brk` (`tools/check-spec-tokens.py:262`). Neither `$brk` nor a
parent holds a `.git`, so the resolver's root is `$brk` and its receipt rung reads nothing; its probe
rung's first place, `$brk/memory-tree/design_lib.py`, holds the anchor (`:245-248`). The copy loads
`design_lib.py` and the `tree_lib.py` it imports from its own directory
(`tools/memory-tree/design_lib.py:103-108`), binds `SPEC_DATE`, passes the kit refusal at `:1369`, and
refuses at `CLAIM_CANARY` (`:1439-1443`) before any join reads the kit again. Probed at `e583a7f42`:
the active-arm copy alone prints `design_lib.py does not resolve`, and the same copy beside a copied
kit prints `REFUSING — CLAIM_CANARY does not hold`.

The whole kit is copied, not the two files the canary path loads today, because a partial copy
strands on the next import `design_lib.py` gains. It is 36 files, copied once per run into the
suite's own `mktemp` directory, which its `trap` takes away (`tools/check-spec-tokens.test.sh:243-244`).

What it does not cover: the probe rung looks for the gov name `memory-tree`, so in an install that
renames the kit's directory the copied directory carries the other name and all six arms red, the
loud direction. The bar's foreign-prefix legs move the tool root and never a kit's directory, as the
excerpt's `/g/scripts/unattended/` path shows. No spawn idiom is added: `${MEMORY_TREE_DIR##*/}` is
the no-fork form, and the file's rows in `memory/project/spawn-idiom-sites.txt` (`:94-95`) keep their
counts.

### S2 — the binding reader in tree_lib

Each name below moves verbatim from `tools/memory-tree/gen_build_index.py`, with its comments and its
docstring, into `tools/memory-tree/tree_lib.py`.

| Name | Line | Read by |
|---|---|---|
| `HDR_RE` | 199-203 | `deviation_join.py:573`, `:619`, and the generator |
| `read_bindings` | 686-794 | `deviation_join.py:526`, and the generator |
| `RECORD_KINDS` | 90 | `record_paths`, and the generator |
| `read_text` | 274-278 | `read_bindings`, and the generator |
| `unfenced` | 411-415 | `read_bindings`, and the generator |
| `BIND_HEAD_LINES`, `RECORD_KIND_TOKENS`, `BIND_RE`, `UNBOUND_RE` | 562-579 | `read_bindings`, and the generator |
| `_id_alternation` | 582-584 | `read_bindings`, the generator, `tools/check-spec-tokens.py:912` |
| `record_paths` | 636-640 | `read_bindings`, and the generator |
| `build_id_token_re`, `_expand_ids`, `read_id_pins` | 643-683 | `read_bindings`, the generator, and `backlog.py` through the `expand` the generator hands it |

`HDR_RE` reads `STATUS_TOKENS`, already in `tree_lib.py` (`:26`), and `read_bindings` reads `os` and
`re`, already imported there (`:19-22`). The generator's `from tree_lib import (...)` (`:186-189`)
gains every moved name, so a caller reaching one through the generator, the checker's
`gbi._id_alternation` among them, keeps working, and `read_text_or_none` keeps reading `read_text` as
a module global. The docstring's rule admits `read_bindings` and `HDR_RE`, which two engines read.
The other twelve names move because `read_bindings` reads them and `tree_lib.py` may import no engine;
the docstring gains one sentence saying a shared name's helpers live beside it.

In `tools/memory-tree/deviation_join.py`, `:135` becomes the line below, the import line at `:473`
goes with its comment, and `:526`, `:573` and `:619` read the two names bare.

```python
from tree_lib import HDR_RE, parse_conf, parse_spec_h1, read_adding_commits, read_bindings, read_blobs_at  # noqa: E402
``` The module docstring at `:32`
names `tree_lib.read_bindings`. The kit README's row for `tree_lib.py`
(`tools/memory-tree/README.md:25`) adds the record-binding reader and the status-header grammar.

The arm's population is unchanged: `ENGINE_OWNERS` (`tools/memory-tree/row_grammar.py:1750`) still
exempts the generator's own re-import, and `scan_engine_imports` grades every module of the kit
(`:1753-1785`).

### S3 — the arm reads the subject

```js
r = await runReview(Object.assign({}, SPEC, { specs: [SPEC.subjects[0].path] }), ALL_OK)
```

The harness compares paths exactly (`tools/workflows/tier2-review.template.js:516`). The fixture's
subject is `memory/builds/dX/spec/s.md` (`tools/workflows/tier2-review.test.sh:364`) since
`60919b0e7`, because a subject carrying `rev` must hold a `builds/<slug>/spec/` segment
(`tier2-review.template.js:317`, `:428-433`). With the arm naming that path, `find` returns it, the
throw names `specs`, and no agent is traced. `FLOOR_ASSERTIONS=343` (`tier2-review.test.sh:2218`) is
read against passes (`:2219`), so the arm's pass is the 343rd and no floor moves.

### S4 — the roster parses

```bash
TN5_P=',"id":"A-tB-1","rev":1}'; TN5_U=${UNITS/"$TN5_P"/"}"}
```

Probed at `e583a7f42` through the suite's own `run_wf` and `returns CONVERGED 0`: the present pattern
prints `SyntaxError: Expected double-quoted property name in JSON at position 165`, and the pattern
above prints the harness's `THROW unattended-build: subject 0's` refusal naming the `id` field and
`got undefined`. The rev arm's pattern (`:1761`) replaces the pair with the id alone, so its roster
parses, and it is unchanged.

### S5 — the four keys, declared blank

After `LIVE_LANDED_UNCLOSED=""` (`tools/memory-tree/.memory-tree.conf.example:463`) and its blank line:

```bash
# DESIGN_RECORD, DESIGN_BASELINE, DESIGN_VIEW, DESIGN_NODES — the design chain's four keys, gov's own:
# a frozen design record, the commit it was pinned at, the as-built view rendered from it and the
# owned-node deriver. `design_lib.read_design_keys` reads them, and the deviation join, the as-built
# view and the coverage read take their states from it. ALL FOUR BLANK OR ABSENT IS OFF: each reader
# prints one off line and reads nothing. Some set and some blank is refused, naming each blank key.
#   DESIGN_RECORD    the design record, read only at DESIGN_BASELINE
#   DESIGN_BASELINE  the commit the design was pinned at, 40 hex
#   DESIGN_VIEW      the as-built view, a dated record named <date>-build-<unit id>-as-built.md
#   DESIGN_NODES     the owned-node deriver, a tracked .py file loaded by path for its derive()
DESIGN_RECORD=""
DESIGN_BASELINE=""
DESIGN_VIEW=""
DESIGN_NODES=""
```

The eight sentences that say otherwise, each corrected to say the example declares the keys blank,
which is off:

| Site | Says today |
|---|---|
| `.memory-tree.conf:977-978` | the memory-tree kit's example conf declares none of them; it then says the example declares the four `DESIGN_*` keys blank and not `SPEC_CARRIES_CUTOFF` |
| `tools/memory-tree/README.md:27` | the keys are gov's, absent from the kit's example conf |
| `tools/memory-tree/README.md:28` | the same, for the view |
| `tools/memory-tree/design_lib.py:24-25` | absent from the kit's example conf |
| `tools/memory-tree/design_lib.py:90-91` | absent from the example conf |
| `tools/memory-tree/deviation_join.py:95-96` | absent from the kit's example conf |
| `tools/memory-tree/asbuilt_view.py:98-99` | absent from the kit's example conf |
| `tools/memory-tree/kit.toml:95-97` | so they stay absent from the example conf; it then says the example declares them blank, as it declares the list's other three |

This reverses the wording of TOOL-dTrueNorth-16 S37 and TOOL-dTrueNorth-20 S1, not their behaviour:
both rest on blank or absent being off, which holds. The other three `conditional_keys`
(`tools/memory-tree/kit.toml:98`) are already declared blank in the example (`:191`, `:194`, `:463`),
and `adopt-memory-tree.sh` copies the example only where no conf exists (`:98`).

### S6 — the record where the writer test reads

In `tools/memory-tree/check-memory-hygiene.test.sh`, `:3389` makes `memory/builds/tOne/reviews` in
place of `memory/builds/tOne/build`, `:3393` writes the record to
`memory/builds/tOne/reviews/2026-09-02-review-ARCH-tOne-1-w.md`, and `:3413` takes out that path. The
comment at `:3378-3384` says the record sits in the reviews folder because the writer test reads that
folder alone. The name follows the suite's other review fixtures (`:2529-2538`). `REVIEW_VERDICT_CUTOFF`
is blank in the fixture's conf (`write_pk_conf`, `:3044-3049`), so check 22 grades no verdict here.

Probed at `e583a7f42`: the arm's commit sequence in a scratch repository, with
`gen_build_index.derive_audit_writers` given a stand-in `resolve` naming the harness directory,
returns an empty set for the record under the build folder and the record itself under the reviews
folder. The harness reach is not the cause: in this tree the generator resolves the workflows kit to
the tree's own, whose repository-relative path is the one the suite's shell resolver gives `WF_KIT`
(`:3385`), so the generator reads the harness where the fixture plants it, also probed.

The audit-pin arms above it (`:3318-3376`) plant their records under `build/`, where no harness
exists, so those records are graded, which their arms expect. They are unchanged.

### S7 — the partition list

`:1133` reads `for _hs_s in 1 2 3 4 5 6 9 10 11 12 13 17 20 21 22 23 24 26 27 28 29 30; do`. With
`--only 29` or `--only 30` each check calls its verb on its own and prints the lines a full run reads
from check 9's process, the equality TOOL-dTrueNorth-27 AC5 observed.

### Inventory

No identifier is minted. `brk` is a local name of the spec-token suite's AC6 block, and the names S2
moves keep their spelling.

### Rollout

The pass changes code the as-built view renders through (`tools/memory-tree/README.md:28`), so its
commit runs `gen_build_index.py --write`; no view byte moves for code that changes no output. The
lander mints `KIT_MEMORY_TREE_VERSION` for the kit files this unit moves. Separately, the records
commit that adds deviation-31 moves the view's record count from 30 to 31
(`tools/memory-tree/asbuilt_view.py:131-133`), so that commit re-renders the view as well. The
`.memory-tree.conf` comment edit is a watched change for the kickoff manifest's ratchet and counts one
watched commit.

### Files touched (estimate)

- `tools/check-spec-tokens.test.sh`
- `tools/memory-tree/tree_lib.py`
- `tools/memory-tree/gen_build_index.py`
- `tools/memory-tree/deviation_join.py`
- `tools/memory-tree/design_lib.py`
- `tools/memory-tree/asbuilt_view.py`
- `tools/memory-tree/README.md`
- `tools/memory-tree/kit.toml`
- `tools/memory-tree/.memory-tree.conf.example`
- `tools/memory-tree/check-memory-hygiene.test.sh`
- `tools/workflows/tier2-review.test.sh`
- `tools/workflows/unattended-build.test.sh`
- `.memory-tree.conf` (one comment)
- `memory/builds/dTrueNorth/build/2026-10-22-build-TOOL-dTrueNorth-29-deviation-31.md` (new, this spec pass)

### Alternatives rejected

- **S1: write the copies beside the real checker.** It writes into the working tree while the bar runs,
  where a parallel leg reading `git status` sees them.
- **S1: copy `design_lib.py` and `tree_lib.py` alone.** A partial kit strands on the next import
  `design_lib.py` gains.
- **S2: load the generator by path.** The scan's docstring names that form NOT CHECKED
  (`tools/memory-tree/row_grammar.py:1762-1764`), so the arm would go green on its own blind spot.
- **S2: pass the reader in as a parameter.** The join's two callers, its CLI and
  `tools/memory-tree/routed_commits.py`, would each import the generator, the same sibling import.
- **S5: add the four keys to `_pyexempt`.** An exemption loosens the arm, which the goal forbids, and
  the kit already declares its other conditional keys blank.
- **S7: derive the loop's ids from the script at run time.** The partition arm already reds on a
  guarded check left out of the list whenever that check prints a line, and a check that prints none
  partitions trivially, so the arm the list feeds checks the list both ways.

## 5. Production-readiness checklist

- security — no write path and no surface. S5 adds blank keys, which are off; S1 copies the kit into
  the suite's own temporary directory.
- perf / scale — S1 adds one copy of a 36-file kit per suite run; S2 spares an armed deviation join
  the import of the generator.
- error / empty / loading states — S1's copies reach the canary refusal and S4's roster reaches the
  harness's named refusal, each the state its arm asserts; nothing reads as green on a stage that did
  not run.
- observability — no printed line changes; AC3 compares the join's output before and after S2.
- risks — S2 moves fourteen names, and a caller reaching one through the generator resolves through the
  re-import. S5 reverses a documented wording of two CLOSED units, not their behaviour.
- testing — AC1 to AC9 as probes; the arms under §7, observed RED and then GREEN at the close.
- migration — additive: an adopter's new conf carries four blank keys, which are off, and an existing
  conf is not touched.
- user docs — the kit README rows for `tree_lib.py`, `deviation_join.py` and `asbuilt_view.py`; no
  page under `help/` covers these engines.

## 6. Acceptance criteria

Every command runs from the repository root under bash 5.3. A scratch repository sits under the
session's temporary directory with no hook installed. AC1 observes S1, AC2 and AC3 S2, AC4 S3, AC5
S4, AC6 to AC8 the three findings of S5 to S7, and AC9 S8.

- **AC1** — When a probe copies the kit with `cp -R tools/memory-tree <dir>/memory-tree`, writes the
  active-arm break beside it with the block's `sed`, and runs that copy from a scratch repository
  built as the suite's `scratch` builds one, the copy exits non-zero printing
  `spec-tokens: REFUSING — CLAIM_CANARY does not hold` and no `spec-tokens: claims join` line; and
  `grep -c '"\$base/claims-break-' tools/check-spec-tokens.test.sh` prints 0.
  Red when: a copy sits where the inline `resolve_kit_dir` finds no kit, and prints
  `design_lib.py does not resolve` before the canary.
  fixture: none in the tree; the probe builds the scratch repository and the copy.
- **AC2** — When `python -c "import sys; sys.path.insert(0, 'tools/memory-tree'); import row_grammar; print(row_grammar.scan_engine_imports('tools/memory-tree')[0])"`
  runs, it prints `[]`; and
  `python -c "import sys; sys.path.insert(0, 'tools/memory-tree'); import gen_build_index as g, tree_lib as t; print(g.read_bindings is t.read_bindings, g.HDR_RE is t.HDR_RE)"`
  prints `True True`.
  Red when: the deviation join imports the generator again, or the generator keeps a definition of
  its own beside the moved one.
- **AC3** — When `python tools/memory-tree/deviation_join.py --approval author-recorded` runs before
  the S2 edit and after it, at one HEAD, the two outputs are equal under `diff`; and
  `python tools/memory-tree/gen_build_index.py --check` exits 0 after it.
  Red when: the moved reader classifies a record or reads a status header differently.
  cost: about a minute for each run.
- **AC4** — When `grep -n "specs: \[SPEC.subjects\[0\].path\]" tools/workflows/tier2-review.test.sh`
  runs, it prints the line above the label `spec-audit: a spec that is also a subject is refused`;
  and `grep -c "specs: \['s.md'\]" tools/workflows/tier2-review.test.sh` prints 0.
  Red when: the arm names a path the `SPEC` fixture's subject does not carry, so the harness's exact
  comparison finds no overlap and the run proceeds.
  figure: 342 passes against a floor of 343 at `e583a7f42`, PINNED from the flagged bar; this arm's
  pass is the 343rd, DERIVED by the close's run.
- **AC5** — When a probe sources `run_wf`, `rec`, `review_out`, `returns` and the fixture values they
  read from the unattended-build suite, applies the arm's `TN5_P` and `TN5_U` lines to its `UNITS`
  literal, and runs `run_wf` over the result with `returns CONVERGED 0`, the output carries
  `THROW unattended-build: subject 0's` with the field `id` named, and no `SyntaxError` line.
  Red when: the pattern leaves the comma before the cut fields, so `JSON.parse` in `run_wf` throws
  before the harness runs.
  fixture: the suite's own lines 160-294 at `e583a7f42`, sourced as §4 S4's probe sourced them.
- **AC6** — When `grep -cE '^DESIGN_(RECORD|BASELINE|VIEW|NODES)=""$' tools/memory-tree/.memory-tree.conf.example`
  runs, it prints 4; when a probe runs the hygiene suite's `_pykeys` and `_pyparity` functions, its
  lines 2821-2845, over the kit's directory, the example and the `_pyexempt` list of its line 2863,
  they print nothing; and
  `git grep -nE "absent from the (kit's )?example|example conf declares none" -- tools/memory-tree .memory-tree.conf`
  prints nothing.
  Red when: a module reads a conf key out of a dict that the example does not declare, or a sentence
  still says the keys are absent from it.
- **AC7** — When a probe replays the writer-test arm's commits in a scratch repository, a harness
  lacking `renderAuditBinding`, a branch committing an unpinned spec-audit record, the harness gaining
  the function, then the merge, and calls `gen_build_index.derive_audit_writers` with a stand-in
  `resolve` naming that harness's directory, it returns the record when it sits in the build's reviews
  folder; and `grep -c 'tOne/reviews/2026-09-02-review-ARCH-tOne-1-w.md' tools/memory-tree/check-memory-hygiene.test.sh`
  prints 2.
  Red when: the fixture plants the record outside the pathspec the writer test reads, where the same
  probe returns an empty set and the record is graded.
  fixture: none in the tree; the probe builds it, as §4 S6's probe did.
- **AC8** — When the ids of `grep -oE '^if check_selected [0-9]+' tools/memory-tree/check-memory-hygiene.sh`,
  sorted and unique, are compared with the ids on the line
  `grep -n 'for _hs_s in' tools/memory-tree/check-memory-hygiene.test.sh` prints, the two sets are
  equal.
  Red when: a `check_selected` call names an id the loop leaves out, whose lines the unscoped run
  prints and no scoped run does.
- **AC9** — When `python tools/memory-tree/deviation_join.py --approval author-recorded` runs after
  deviation-31 is committed, no `malformed:` or `refused:` line names
  `2026-10-22-build-TOOL-dTrueNorth-29-deviation-31`, and the rescope add member for
  `TOOL-dTrueNorth-29` joins it.
  Red when: the record falls outside the grammar, or the add member is recorded by nobody.

## 7. Gates

`spec-tokens self-test` · `row-grammar selftest` · `tier2-review self-test` · `unattended-build self-test` · `memory-hygiene self-test` · `verifier fan-out self-test` · `review-join self-test` · `build-index selftest` · `routed-commits selftest` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `install-prefix (shipped surface)` · `shell hygiene (a fork spent on builtin work)` · `shell hygiene (a loop fed by a command substitution)` · `kit/dogfood doc parity` · `recall floor` · `recall floor arms` · `transition-audit arms` · `straggler-guard arms` · `kickoff-manifest ratchet` · `govkit selfcheck` · `verdict epoch (kit version dates the engine)` · `remote literals (kit code names no remote)` · `dead-path carriers (deleted files still named)` · `lexicon naming predicates` · `python resolver (behaviour + inline parity + idiom ban)`

New arm: tools/check-spec-tokens.test.sh · covers AC1 · the six AC6 staged breaks, red at the flagged bar with each copy alone in the suite's temporary directory · none
New arm: tools/workflows/tier2-review.test.sh · covers AC4 · the spec-audit overlap arm, red at the flagged bar over the bare name s.md · none
New arm: tools/workflows/unattended-build.test.sh · covers AC5 · the TN5-AC3 no-id arm, red at the flagged bar over a roster carrying a trailing comma · none
New arm: tools/memory-tree/check-memory-hygiene.test.sh · covers AC7 · check 21's two writer-test arms, red at the flagged bar with the record in the build folder · none
New arm: tools/memory-tree/check-memory-hygiene.test.sh · covers AC8 · the partition arm, red at the flagged bar on the check 29 and check 30 lines · none

The five legs the flagged bar redded are graded by the bar at the close; each criterion above
observes its cause by a probe. The row-grammar arm and the example-conf arm are unchanged, and the
close sees them green. No assertion floor moves.

## 8. Open questions

- **F1 — Should the review harness's overlap refusal also match a `specs` member spelled differently
  from a subject's path?** It compares strings exactly (`tools/workflows/tier2-review.template.js:516`).
  The `specs` rule refuses an absolute, home-relative, drive-lettered or backslashed path, a `..`
  segment and a control character (`:505-513`), and accepts `./a.md`, `a//b.md` and a case variant,
  each naming the document `a.md` names on some filesystem. (a) No harness change. The one caller in
  this tree, the unattended stage, builds `specs` from the roster's spec paths less the subjects by
  the same exact comparison (`tools/workflows/unattended-build.template.js:1603-1606`) and refuses a
  resolved subject no roster path matches exactly, so both lists carry one spelling by construction.
  (b) The harness also refuses a `.` or empty segment in a `specs` member and in a subject path, so
  every accepted spelling of a path is one string and the exact comparison is sound for them; one new
  refusal and its arms, and a case variant still unmatched. (c) Fold both sides before comparing,
  which normalizes where the rule's comment chose to refuse rather than normalize (`:498-504`). (b)
  and (c) change the argument contract of a shipped harness, which veto 2 gives the owner if the
  harness counts as a governance carrier, and none of this unit's criteria needs either.
  Recommendation (a), with (b) the follow-up if a caller outside this tree is found spelling a
  variant. Rung 3. RESOLVED (agent, 2026-10-22, delegated): (a). widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-22 · initial draft, one scope item per cause of the five self-test legs the flagged bar at `e583a7f42` redded on this build's arms, with deviation-31.

## 10. Reuse audit

Every item extends a seam the tree already has, read at `e583a7f42`. S2 extends `tree_lib.py`, whose
docstring is the seam's rule, a name two engines read living there and re-imported by the module that
defined it (`tools/memory-tree/tree_lib.py:2-13`), as `read_adding_commits` moved there under
TOOL-dTrueNorth-20 S32. `python tools/codebase-map/reuse_lookup.py "a helper two memory-tree engines
share, moved out of the index generator so a sibling need not import it"` ranked name-stem neighbours,
`tree`, `note`, `need` and `engine`, none of them a shared-helper module, so the seam is the one the
kit's own docstring names, read at source. S1 extends the suite's own shell resolver and its
`MEMORY_TREE_DIR` (`tools/check-spec-tokens.test.sh:136-194`):
`python tools/codebase-map/reuse_lookup.py "run a staged broken copy of a checker beside the kit it
loads"` ranked `resolve_kit_dir`, 72 installs, the seam S1 relies on and does not copy. S3 reads the
fixture's own value instead of a second literal; S4, S6 and S7 edit their fixtures in place; S5
follows the example's own form for a conditional key (`tools/memory-tree/.memory-tree.conf.example:455-463`).
The recall query ranked TOOL-aRepatriatedFork-9's spec, which set the sibling-import rule and its
arm, and TOOL-aWokenSentinel-24, which builds a suite's staged-break copy in one helper; one block
writes all six copies here, so no helper is minted.

Recall terms used: `python tools/memory-recall/query.py "self-test arms a build turned red: a fixture
path moved, a sibling import, a staged broken copy, a conf example key" --terms "self-test arm fixture
staged copy kit resolver sibling import tree_lib conf example partition audit writer reviews
pathspec"`
