# TOOL-aBriskPreflight-11 — the ceilings instrument prices every fork at the worst host reading on record

**Status:** CLOSED · rev-2 · 2026-10-12 · node a · Tier-2 · base bb388384 · streams tooling · order 6 · ratified 2026-10-12

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-12-build-TOOL-aBriskPreflight-11-acceptance-ledger.md](../build/2026-10-12-build-TOOL-aBriskPreflight-11-acceptance-ledger.md) | journal | — |
| [2026-10-12-prompt-TOOL-aBriskPreflight-11-build-brief.md](../prompts/2026-10-12-prompt-TOOL-aBriskPreflight-11-build-brief.md) | research | — |
| [2026-10-12-prompt-TOOL-aBriskPreflight-11-spec-brief.md](../prompts/2026-10-12-prompt-TOOL-aBriskPreflight-11-spec-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

Promoted from the closing diff review's HIGH H1. The ceilings instrument of `TOOL-aBriskPreflight-7`
raises S_w and K_w only from the host row of an after-arm timed row with exit 0, so the 2.53 s fork
reading in the host row of `ab-AO-2` is never read. The shipped `WIRING_CEILING` of 570 s then
understates its own rule, "every K_m in the rows", and a healthy wiring check at a host state already
on record can be killed and refused at check 4. After this unit the instrument prices every spawn and
fork at the worst host reading it reads, says which figure it priced at, and proves it on a fixture.

## 2. Scope (IN)

- **S1** — In `memory/builds/aBriskPreflight/build/2026-10-11-build-TOOL-aBriskPreflight-7-ceilings.sh`,
  the `$1 == "host"` branch raises `sw` from that row's `spawn5` / 5 and `kw` from its `fork`, for
  every host row in both row files, whatever label, arm or exit status the timed row after it
  carries. The two raises in the timed-row branch move there, so one place raises each figure.
  Observed by AC1 and AC2.
- **S2** — Before it derives any subject, the instrument prints one pricing line on stderr:
  `ceilings: priced at S_w=<v> s per spawn and K_w=<v> s per fork, the worst of <n> host rows and the pinned floors`,
  both figures to two decimals. Stdout stays exactly the three constant lines, so the diff against
  the driver is unchanged in shape. Observed by AC2.
- **S3** — A `--selftest` flag runs the same awk program text over the fixture rows in §4 "The
  self-test fixture", fed on stdin, with its own GATE_BOUND, and reads neither `.unattended.conf` nor
  the repository, so a copy of the file outside the tree runs it. It asserts the pricing line names
  `K_w=9.00` and `S_w=4.00`, prints `ceilings selftest: ok — K_w=9.00 S_w=4.00 from the old-arm host
  row` and exits 0, or prints the pricing line it read and exits 1. Observed by AC1.
- **S6** — The instrument's refusal at or above `GATE_BOUND` grades the WIRING subject only, by the
  owner's ruling on §8 F2: `WIRING_CEILING` races `GATE_BOUND` on one child, while
  `PREFLIGHT_CEILING` kills nothing and compares preflight's whole wall, which no bound covers. The
  preflight subject is derived and printed whatever its relation to `GATE_BOUND`, and the instrument
  says so on stderr when it sits at or above it. Spec 7's AC8 takes the same rule in its rev line.
  Observed by AC6.
- **S4** — Once §8 F2 is resolved, the three constant lines of `tools/unattended/unattended.sh` take
  the instrument's stdout byte for byte, and `2026-10-11-spec-TOOL-aBriskPreflight-7.md` takes a
  rev line naming this unit, since its §4 says a later change to either value is a rev bump of that
  spec with new rows. Observed by AC3 and AC5.
- **S5** — Three prose sites state one rule for S_w and K_w, "every host row on record, any arm":
  the instrument's header comment, the driver comment above the constants, and the "values are
  derived" bullet of `tools/unattended/README.md`. Each says W, S_m and K_m come from after-arm rows
  and S_w and K_w from every host row. Observed by AC4.

## 3. Non-goals (OUT)

- No change to the formula of spec 7 §4 "The values" beyond which host rows set S_w and K_w: W, S_m,
  K_m, E, K, U, the floors of 2.5 s and 0.91 s and the round-up to 30 s keep their definitions.
- No change to `GATE_BOUND`, its default or `.unattended.conf`, and no conf key or environment read
  for any ceiling. The brief says so, and spec 7 §3 says so.
- No change to the instrument's refusal at or above `GATE_BOUND` for the wiring subject; S6 narrows
  it to that subject by the owner's ruling on §8 F2.
- No typed value. A constant that the instrument does not print is never written into the driver.
- No new row and no re-measurement. The worst reading on record stays on record: a new row can only
  raise a maximum.
- No gate leg runs `--selftest`. Wiring a records file into `tools/gate-legs.json` is a new leg with
  its own ceiling and guard. The self-test runs at every re-derivation, which is when the instrument
  runs at all.
- No change to the owner's ruling. A wiring check over its ceiling is killed and refused at check 4;
  a preflight over its own names the breach and still writes the record.
- The unattended kit's version bump. The main loop makes one bump per touched kit at the close.

### Edges

none

## 4. Design

### What the instrument does today

The timed-row branch at
`memory/builds/aBriskPreflight/build/2026-10-11-build-TOOL-aBriskPreflight-7-ceilings.sh:39` raises
`sw` and `kw` only after it has matched a subject label and passed `if (f["rc"] != 0) next`. The host
branch at
`memory/builds/aBriskPreflight/build/2026-10-11-build-TOOL-aBriskPreflight-7-ceilings.sh:29` stores
`hs` and `hk` and raises nothing. So the host rows of `ab-AO-1` (fork 0.59 s) and `ab-AO-2` (fork
2.53 s) in `2026-10-11-build-TOOL-aBriskPreflight-7-ab-rows.log` are read and never priced, and
`kw` ends at the larger of 0.91 and 1.06, the fork of `ab-AN-2`. Verified in source at writing.

### The change

The host branch gains the two raises and a counter, and the timed-row branch loses its two. The
pricing line of S2 prints first in `END`, after `if (bad) exit 1`, so a run that refuses on its rows
still says what it priced at. The awk program text lives in one shell variable, and the real run
and `--selftest` both pass that variable, so the self-test grades the program the real run uses and
not a copy of it. `--selftest` is handled before `ROOT` is resolved, because it reads no file.

### The self-test fixture

Fed on stdin through a here-document inside the instrument, under a GATE_BOUND of 999999 so no
subject refuses:

```
host label=ab-AO-9 spawn5=20.00 fork=9.00
label=ab-AO-9 rc=1 wall=100.0
host label=ab-AN-1 spawn5=1.00 fork=0.05
label=ab-AN-1 rc=0 wall=100.0
host label=ab-AN-2 spawn5=1.00 fork=0.05
label=ab-AN-2 rc=0 wall=100.0
host label=cw-after-1 spawn5=1.00 fork=0.05
label=cw-after-1 rc=0 wall=10.0
host label=cw-after-2 spawn5=1.00 fork=0.05
label=cw-after-2 rc=0 wall=10.0
host label=cw-after-3 spawn5=1.00 fork=0.05
label=cw-after-3 rc=0 wall=10.0
count label=t subject=wiring execs=1 forks=1 source=fixture
count label=t subject=preflight execs=1 forks=1 source=fixture
window label=t subject=wiring wait=w timeout=1 window=1 source=fixture
window label=t subject=preflight wait=w timeout=1 window=1 source=fixture
```

The `ab-AO-9` pair has the shape of the real `ab-AO-2` pair: an old-arm label no subject claims,
with exit 1. Its fork of 9.00 s is above every timed row's 0.05 s and the 0.91 s floor, and its
spawn5 / 5 of 4.00 s is above every timed row's 0.20 s and the 2.5 s floor. So the asserted figures
can only come from the host branch. With that branch's raise deleted, the pricing line reads
`K_w=0.91 S_w=2.50` and the self-test exits 1. The fixture's 9.00 is synthetic, so AC2 observes the
shipped 2.53 on the committed rows as well.

### The values this rule derives, and why F2 exists

Arithmetic over the committed rows, by spec 7 §4's formula, with K_w = 2.53 s and S_w = 2.50 s:

| Subject | W | S_m | K_m | E | K | U | value | today |
|---|---|---|---|---|---|---|---|---|
| wiring | 142.2 (`cw-after-1`) | 0.896 | 0.07 | 137 | 193 | 0 | 836.73, so 840 | 570 |
| preflight | 1041.7 (`ab-AN-1`) | 0.83 | 0.07 | 653 | 762 | 164.5 | 4171.23, so 4200 | 3060 |

`CEILING_SPAWN_MS` stays 2500: no host row's spawn5 / 5 reaches 2.5 s, the highest being 1.28 s for
`ab-AN-2`. With K_w = 1.06 the same arithmetic gives 570 and 3060, which is the shipped pair, so the
rows and the formula are read correctly. figure: every number in the table is DERIVED from
`2026-10-11-build-TOOL-aBriskPreflight-7-ab-rows.log` and
`2026-10-11-build-TOOL-aBriskPreflight-7-ceiling-rows.log` at writing, and the built instrument
re-derives them.

The preflight value, 4200 s, is at or above the 3600 s `GATE_BOUND` that `.unattended.conf`
declares, so the widened instrument exits 1 printing `ceilings: preflight: 4200 s is at or above the
declared 3600 s GATE_BOUND, so it could never fire first`. Spec 7 §4 says the unit then parks. That
is F2, and S4 cannot be built until it is answered.

### Inventory

| Identifier | Kind | Naming cell |
|---|---|---|
| `--selftest` | flag of a records file | none; the lexicon grades no records file without functions |
| `nh` | awk variable, the host-row count | none declared for awk variables |
| `PROG` | shell variable holding the awk program text | none declared for shell variables |

The instrument keeps no function definitions, so the lexicon leg has nothing to grade in it.

### Files touched (estimate)

`memory/builds/aBriskPreflight/build/2026-10-11-build-TOOL-aBriskPreflight-7-ceilings.sh`
`tools/unattended/unattended.sh`
`tools/unattended/README.md`
`memory/builds/aBriskPreflight/spec/2026-10-11-spec-TOOL-aBriskPreflight-7.md`

`TOOL-aBriskPreflight-12` holds the review's M1, which puts a `**Serves:**` line in this
instrument's first lines, and M2 and L1, which edit `tools/unattended/unattended.sh`. The two write
sets intersect, so the two passes are sequenced, never concurrent (M6 clause 1).

### Rollout

Live, with no flag, as spec 7's rollout says: a records instrument and three file constants, and
every dark form needs a conf key or an environment read, both non-goals.

### Alternatives rejected

§8 F1 (b) and every option of §8 F2, with the test or veto that rejected each; §10 lists them as
BUILD-METHOD M12 asks.

## 5. Production-readiness checklist

- security — no new write path or surface. The instrument is a records file that reads two row
  files and one conf line; the self-test reads nothing.
- perf / scale — the self-test is one awk run over sixteen lines. The driver gains no spawn; S4
  changes three literals.
- error / empty / loading states — a missing row, a timed row without its host row, and a value at
  the bound keep their refusals. The pricing line prints before any of the last kind, so a refusing
  run still names the figure it priced at.
- observability — the pricing line names S_w, K_w and how many host rows set them, which the
  instrument printed nowhere before.
- risks — a wider K_w raises `WIRING_CEILING` to 840 s, so a wiring check that regresses by less
  than the new margin is named later. That is the rule spec 7 chose: a healthy run breaches only on
  a host slower per process than any reading on record. Until F2 is answered the shipped 570 s
  stands, and a healthy wiring check at `ab-AO-2`'s recorded state can still be killed.
- testing — `--selftest` on a staged break in a copy, and the instrument over the committed rows.
- migration — none. Adopters receive the re-derived constants at the kit's next version.
- user docs — the "values are derived" bullet of `tools/unattended/README.md` (S5).

## 6. Acceptance criteria

- **AC1** — When
  `bash memory/builds/aBriskPreflight/build/2026-10-11-build-TOOL-aBriskPreflight-7-ceilings.sh --selftest`
  runs, it prints `ceilings selftest: ok — K_w=9.00 S_w=4.00 from the old-arm host row` and exits 0.
  A copy of the built file under the run's scratchpad, with the host branch's `kw` raise deleted,
  run with `--selftest`, prints a pricing line carrying `K_w=0.91` and exits 1; with the `sw` raise
  deleted instead, the line carries `S_w=2.50` and it exits 1.
  Red when: the raises stay in the timed-row branch only, so the old-arm host row is never priced
  and the self-test passes on neither copy, or the self-test reads a program text of its own.
  fixture: the here-document of §4 "The self-test fixture", inside the instrument; the tree holds
  none today.
- **AC2** — When
  `bash memory/builds/aBriskPreflight/build/2026-10-11-build-TOOL-aBriskPreflight-7-ceilings.sh 2>&1 >/dev/null`
  runs over the committed rows, its first line is the pricing line carrying `S_w=2.50`, `K_w=2.53`
  and `the worst of 7 host rows`.
  Red when: the host branch does not raise `kw`, so the line reads `K_w=1.06`.
  figure: 2.53 and 7 are DERIVED from
  `memory/builds/aBriskPreflight/build/2026-10-11-build-TOOL-aBriskPreflight-7-ab-rows.log` and
  `memory/builds/aBriskPreflight/build/2026-10-11-build-TOOL-aBriskPreflight-7-ceiling-rows.log`:
  the fork of `ab-AO-2`'s host row, and four plus three host rows.
- **AC3** — When the instrument's stdout is compared with
  `grep -E '^(WIRING_CEILING|PREFLIGHT_CEILING|CEILING_SPAWN_MS)=' tools/unattended/unattended.sh`
  by `diff`, the diff is empty and the instrument exits 0.
  Red when: a constant is typed, or `WIRING_CEILING` stays at 570 while the instrument prints 840.
  figure: DERIVED at the pass from the committed rows; by §4, `WIRING_CEILING="840"` and
  `CEILING_SPAWN_MS="2500"`, and the preflight line is whatever F2's answer lets the instrument
  print.
  permission: owed only after §8 F2 is resolved. Under the instrument's present bound rule it exits
  1 on the preflight subject, and the unit parks rather than writing a value it did not print.
- **AC4** — When `grep -n 'every host row' tools/unattended/README.md tools/unattended/unattended.sh memory/builds/aBriskPreflight/build/2026-10-11-build-TOOL-aBriskPreflight-7-ceilings.sh`
  runs, it prints at least one line from each of the three files.
  Red when: one of the three still says S_w and K_w come from after-arm rows, so two answers to one
  question ship.
- **AC6** — When the instrument runs over the committed rows, it exits 0 and prints a
  `PREFLIGHT_CEILING` line whatever its relation to `GATE_BOUND`, with one stderr line naming that
  relation when the value sits at or above it; a copy whose rows push the WIRING subject to
  `GATE_BOUND` or above still exits 1 naming that subject.
  Red when: the instrument refuses the preflight subject at the bound, or stops refusing the
  wiring one.
- **AC5** — When `git diff bb388384 -- .unattended.conf` runs, it prints nothing, and
  `grep -n 'TOOL-aBriskPreflight-11' memory/builds/aBriskPreflight/spec/2026-10-11-spec-TOOL-aBriskPreflight-7.md`
  prints a §9 rev line.
  Red when: the pass raised `GATE_BOUND` or added a ceiling key to fit the derivation, or changed
  spec 7's values without the rev bump its own §4 asks.

## 7. Gates

`unattended kit gate` · `kit version markers` · `kit epoch (shipped bytes move, the version moves)` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `recall floor` · `recall floor arms` · `shell hygiene (a loop fed by a command substitution)` · `shell hygiene (a location probe asked from a moved directory)`

The pass verifies with AC1 to AC5 only. The listed legs run once, at the close, after the last unit
is terminal.

New arm: memory/builds/aBriskPreflight/build/2026-10-11-build-TOOL-aBriskPreflight-7-ceilings.sh --selftest · covers AC1 · a copy whose host branch has its kw or sw raise deleted, which reads the floors instead of the old-arm host row · none

## 8. Open questions

- **F1 — Which host rows set S_w and K_w?** Options: (a) every host row in the rows the instrument
  reads, any arm and any exit status, as spec 7 §4's table says ("the larger of 0.91 s and every
  K_m in the rows"); (b) only the host rows of after-arm timed rows, with a recorded reason for
  leaving out the old-arm 2.53 s reading. A probe reads the arm out of the question:
  `memory/builds/aBriskPreflight/build/2026-10-11-build-TOOL-aBriskPreflight-1-host-state.sh:6`
  times one bare fork BEFORE the timed run starts, and `ab-AO-2`'s host row is stamped 17:50:50Z
  against a run start of 1791741062, 17:51:02Z. So the arm cannot reach the reading, and it is a
  reading of the host like every other. Nor does the row record foreign load: its cpu of 21 percent
  is the lowest of the four A/B host rows. So (b)'s selector differs from (a) only by leaving out the
  one reading that moves K_w, which is a selector chosen by its outcome, the class M3's counter-rule
  refuses. (b) also cannot carry the review's left-shift fixture, whose host row is priced only
  under (a). Recommendation: (a).
  RESOLVED (agent, 2026-10-12, delegated): (a).
- **F2 — Under (a), may `PREFLIGHT_CEILING` sit at or above `GATE_BOUND`?** The arithmetic of §4
  gives 4200 s against the declared 3600 s, so the instrument as spec 7 shipped it exits 1 on the
  preflight subject. Options: (i) the instrument's bound refusal applies to the wiring subject only,
  because `WIRING_CEILING` races `GATE_BOUND` on one child while `PREFLIGHT_CEILING` kills nothing and
  compares preflight's whole wall, which no bound covers, so 4200 s still names a total nothing else
  names; (ii) raise `GATE_BOUND` to at least 4230 s; (iii) write a value below 3600 s by hand;
  (iv) price the forks by after-arm rows only, which is F1 (b). (i) fails veto 1 on spec 7's AC8,
  "Both ceilings are below the declared GATE_BOUND", which the brief keeps ("as spec 7 intends"),
  and it is a second mechanism, which BUILD-METHOD M2 puts in a unit of its own. (ii) fails veto 1 on
  §3's second non-goal and the brief's "no raised GATE_BOUND". (iii) fails veto 1 on §3's typed-value
  non-goal and spec 7's AC8, which reds a typed constant. (iv) lost F1. No option survives, so by M3
  this is not the run's to choose: it is parked for the owner, and S4 and AC3 wait on it.
  Recommendation to the owner: (i), built as its own unit that this one consumes, because it keeps
  the worst-on-record rule, lifts `WIRING_CEILING` to 840 s and closes H1's impact, and changes no
  bound and no conf.
  RESOLVED (owner, 2026-10-12): (i), at the hand-off — "go with 'apply the below GATE_BOUND rule to
  the wiring ceiling only' and land". Built in THIS unit as S6, since the owner's answer is the
  one change the instrument needs and it touches no file outside this unit's write set.

## 9. Revision log

- rev-1 · 2026-10-12 · initial draft, from the spec brief
  `2026-10-12-prompt-TOOL-aBriskPreflight-11-spec-brief.md` and the closing review's H1.
- rev-2 · 2026-10-12 · §8 F2 RESOLVED by the owner as (i); S6 and AC6 added, the §3 non-goal on the
  bound refusal and the hands-off edge rewritten to match; S4 and AC3 no longer wait.

## 10. Reuse audit

The seam this unit extends is the ceilings instrument itself,
`memory/builds/aBriskPreflight/build/2026-10-11-build-TOOL-aBriskPreflight-7-ceilings.sh`, its host
branch at line 29, verified in source at writing. `python tools/codebase-map/reuse_lookup.py "derive
a wall-clock ceiling from committed host-state rows at the worst per-process cost on record"` named
no seam that derives a ceiling from host rows: it ranked name-stem neighbours such as `rows`,
`records` and `derive_scope`, and `check_gate_wall` in `tools/unattended/lib-unattended.sh`, which
compares a wall with a ceiling but takes the bar profile's inputs. The records file is not in the
map's inventory, so the probe could not have named it. `tools/run-gates/derive-ceilings.py` derives
leg ceilings from evidence and is cited, not reused: it admits only readings taken on a host free of
foreign work (`TOOL-aGraftedHelix-5`), because its ceilings are monotone hang bounds that a loaded
reading would raise for good. Here the worst reading loosens a kill, which is the point of spec 7's
rule, so the exclusion does not transfer.

The recall probe returned the H1 section of the closing review, spec 7 and its brief,
`TOOL-aThawedCorpus-3` (no wall-clock ceiling on this node), `TOOL-aGradedMandate-12` (a wall-clock
verdict must say whether it reads load or regression) and `TOOL-aGradedDialect-13`, whose evidence
file was not re-derived from a contended day because loaded maxima are readings of the host. That
last one is the same direction as `derive-ceilings.py` and does not transfer for the same reason.

Candidates rejected, with the test that rejected each (M12): F1 (b) by the host-state probe above,
which shows the arm cannot reach the reading, and by the counter-rule; F2 (i), (ii) and (iii) by veto
1, and (i) also by M2; F2 (iv) by F1.

Recall terms used: `python tools/memory-recall/query.py "what decided how a wall-clock ceiling is
derived from recorded host readings and which readings set the worst per-fork cost" --terms "ceiling
K_w fork host-state worst on record GATE_BOUND instrument derived pinned spawn cost preflight"`
