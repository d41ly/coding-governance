# TOOL-aBriskPreflight-1 — the A/B: check-wiring's four batched sites, before and after

**Serves:** research TOOL-aBriskPreflight-1

Node `a`, 2026-10-11, the rebuild pass. Spec rev-2. The built checker is blob `3682d846a7fe`, the
`tools/check-wiring.sh` the pass commit carries; BASE's is blob `231fef8cd486`, unchanged from
`b726385f` to the spec commit `ac9e6afb2`. Every run below names the host state it ran under.

## The fixture

A throwaway clone, `git clone --local` of this repository under `%TEMP%/bp1r`, checked out at
`ac9e6afb2`. `bp1r`, not `bp1`: the killed first pass left a `bp1` of unknown state, so this pass
did not reuse it. One `--fix` ran there first with BASE's script; it set `core.hooksPath`,
`merge.rows.driver` and `merge.ours.driver` in the clone's own git config. Then `--check` ran once
with BASE's script and once with the built one written over it, each under the build's instrument
`2026-10-11-build-TOOL-aBriskPreflight-1-run-traced.sh`, and each trace was read by
`2026-10-11-build-TOOL-aBriskPreflight-1-trace-spawns.py` with that run's script as the span source.
Fixture repositories for the sliced arms went under `%TEMP%/bp1s` and `%TEMP%/bp1t`.

## Host state, one line beside each traced run

| Run | At (UTC) | Five spawns | Fork | Pool Paged | Pool Nonpaged | CPU |
|---|---|---|---|---|---|---|
| `cw-base-traced-r` | 06:11:54 | 1.19 s | 0.03 s | 17916 MB | 6242 MB | 43% |
| `cw-built-traced` | 06:13:53 | 0.21 s | 0.02 s | 17915 MB | 6243 MB | 50% |

The spawn cost moved almost sixfold between the two lines, and two sliced suite arms were running
on the host while this pass started the clone's `--fix`. The counts below do not depend on load;
the walls, 113.7 s and 52.6 s traced, are not a comparison.

## The spawn counts (AC3)

Both runs exit 1 on the `skill` arm only, the machine's installed kickoff engine differing from the
clone's tracked one, which no site of this unit reaches. Their outputs are byte-identical.

| Run | Forks | Execs | `sed` | `grep` | `git` | `tail` | `awk` |
|---|---|---|---|---|---|---|---|
| BASE `cw-base-traced-r` | 357 | 388 | 182 | 56 | 37 | 2 | 5 |
| built `cw-built-traced` | 333 | 246 | 58 | 43 | 33 | 0 | 6 |

The populations, read from the clone at observation time: 120 `merge=rows` indexes, 4 families
(`PLAY KICK TOOL DEPL`), and 5 eol candidate paths that `git ls-files` and the `grep -E` hand to
`git check-attr`. BASE's tree holds the same 5, and the BASE trace shows five `git check-attr eol`
calls, one per path; the "10" the baseline and the spec carried matches its 5 `git` and 5 `sed`.

- `sed` is lower by 124, against a floor of 120 + 5 − 1 = 124: the harvest's 120 become 1, the eol
  population's 5 become 1, and the audit line's 2 become 1.
- `grep` is lower by 13, against a floor of 3 × 4 = 12: the smoke's twelve `grep -c` and the
  harvest's `grep .`.
- `git` is lower by 4, against a floor of 5 − 1 = 4.
- `tail` is lower by 2. `awk` is higher by 1, the smoke's count.

The "before" of the brief, `cw-base-traced` at 355 forks and 387 execs, was BASE's script over
BASE's tree. This pass re-traced BASE in the same clone so both rows read one tree.

## The other criteria

- **AC1** — the `merge` and `eol` lines of the two traced runs are byte-identical, and both runs
  print `ok       merge` twice, rows and ours, and `ok       eol`.
- **AC2** — with `FAMILIES="playbook:ZZZA kickoff:ZZZB tooling:ZZZC deployer:ZZZD"` in the clone,
  both scripts print one identical `UNWIRED  merge` line reading `does not declare DEPL KICK PLAY
  TOOL`, which is every family the indexes lead with. The driver accepted the renamed conf, so the
  four-run fallback was not needed.
- **AC4** — state 5d, sliced: the built script passes `does not declare TOOL`; a copy with the
  harvest's post-loop `sed` replaced by `:` fails it and prints `ok       merge`.
- **AC5** — the new state 5f, sliced: the built script passes; BASE's prints the identical
  `missing or duplicated: TOOL-002 TOOL-003 PLAY-002 PLAY-003 (`, compared with `cmp`; a copy whose
  `awk` prints nothing fails, reading instead as the missing audit line.
- **AC6** — state 5e, sliced: the built script passes `HASHED`; a copy with the `K` and `H` tags
  swapped fails it and prints `ok       merge`.
- **AC7** — the AC9 block, sliced: all fourteen assertions pass and the `note     eol` line names
  `.claude/skills/my skill/SKILL.md`; a copy with `tr ' ' '\n'` before `git check-attr --stdin`
  fails `a Skill path with a space is still seen`, and `--fix repairs a spaced path` with it.
- **AC8** — `python tools/codebase-map/gen_map.py --check` exits 0 after the slice scripts were
  deleted; the pass adds no function, so `symbols.json` does not move.

The chunk split is the one branch no criterion reaches, because this tree's paths fit in one
invocation. A probe cut the harvest's block out of the built script with the bound as a parameter
and `sed` wrapped to count its calls, and ran it in the clone: bound 8000 made 1 call, 300 made 17,
and 1 made 120, the old per-file shape. All three printed `DEPL KICK PLAY TOOL`, compared with `cmp`.

Each staged break was its own copy of the built script beside it under `tools/`, differing by one
line, so "restored" is the unchanged built script, which ran first in every slice.
