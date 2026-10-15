# Acceptance ledger — TOOL-aSparedSpawn-14

**Serves:** journal TOOL-aSparedSpawn-14

Node `a`, 2026-10-12, bash under MSYS. The pass ran no bar, no suite, no held leg and no slice of a
suite. The observations below come from three direct instruments, committed beside this ledger:
`check-arms.py --selftest` run directly; `2026-10-12-build-TOOL-aSparedSpawn-14-arm-breaks.py`, which
stages one break at a time into a copy of `check-arms.py` and runs that copy's `--selftest`; and
`2026-10-12-build-TOOL-aSparedSpawn-14-direct-checks.sh`, which invokes the changed driver directly and
runs the changed leg scoped to `--only 52` over a scratch copy of the kit with each break staged into
the copy's driver. Their output is the `-direct-checks.out` file. `check-arms.py --check`, `--report`
and `--emit-floors` were run directly over the tree, and over a `git archive` extract of the batch
parent `e98dee7f` for its census.

`bash -n` passed on `tools/unattended/unattended.sh`, `tools/unattended/check-unattended.sh`,
`tools/unattended/unattended.test.sh` and `tools/unattended/check-unattended.test.sh`. Every new and
changed suite arm was checked by `bash -n` and by reading, and is OWED at VERIFYING: the driver
suite's kept run-state arm, its usage-render arm, its `print_env_failure` arm and its converted
`--park --item` arm; the leg suite's six check-52 arms and the partition arm's list, 47 swapped for 52.
`check-arms-groups.sh` over the leg suite reports the same 25 findings at HEAD and on this tree, so
the new arms add none.

One recorded deviation. The row-15 replay step ran the leg's core over a conf staging the retired
key in place of its replacement; it passed the pass's 600 s bound, was stopped, and its processes were
reaped by pid. The conf was restored from its copy and `git diff --quiet .unattended.conf` read clean.
Twice a `python - <file>` call handed a shell file to the Python launcher, which tried to run it
through its shebang; bash died at startup each time (`child_copy`/`signal pipe`), nothing ran, and the
tree and the conf were checked clean after each.

Inherited, not this unit's: `check-arms.py --check` reds six `tools/run-gates/run-gates.sh` exit sites
on this tree and identically on the batch parent's extract.

**Evidences:** TOOL-aSparedSpawn-14
- AC1 — `check-arms.py --selftest` — a planted row whose survivor lacks its signature reds naming
  `(TOOL-tBudget-1)`, and the same row with the signature present passes; staged break
  `survivor signature` (`arm-breaks.py`) turns that arm red.
- AC2 — `check-arms.py --selftest` — a planted row missing its `survivor` field and one missing its
  `replay` field each red naming the field; staged breaks `survivor field` and `replay field` each
  turn their arm red.
- AC3 — `check-arms.py --selftest` — a fixture gate whose census is one above its ceiling (its
  `REFUSAL_CEILINGS` token) reds naming the gate and the retirement review; at the ceiling it
  passes; staged break `ceiling compare` turns the arm red.
- AC4 — `check-arms.py --selftest` — tokens lacking a date and lacking an id each red naming the
  token, an id the fixture decision log (`memory/DECISIONS.md`) does not carry reds, an id carried only as a prefix of a
  longer one is not carried, and a valid ceiling prints
  `ceiling <gate> 2/2 · 2026-10-12 · TOOL-tBudget-1`; staged breaks `ceiling date` and
  `ceiling id carried` each turn an arm red.
- AC5 — `check-arms.py --selftest` — one more site matching a family at its ceiling reds with
  `a new per-verb site: extend the family's shared table instead`, and the family at its ceiling
  passes printing its date and id; staged break `family over ceiling` turns the arm red.
- AC6 — `check-arms.py --check` — on this tree the two unattended ceilings print `318/318` and
  `264/264` with `2026-10-12 · TOOL-aSparedSpawn-14`, the three families print at their ceilings,
  the registry reads 5 rows, and the only reds are the six inherited `run-gates.sh` sites;
  `check-arms.py --report` lists 31 unbudgeted gates by name.
- AC7 — `check-arms.py --selftest` — a family pattern matching no site in the planted gate reds
  under `--check` naming the family; staged break `family dead pattern` turns the arm red.
- AC8 — `direct-checks.sh` — the driver on a slug with no run-state file prints
  `UNATTENDED check 10 FAILED — no run-state file, so there is no run to report on: memory/builds/aNoSuchRun/RUN.md`,
  rc 1; `check-arms.py --report` counts one `no run-state file` site, inside `check_run_state`; the
  leg scoped to 52 reds a scratch verb that tests its run-state file itself
  (`route c52probe() at line 13897`) and a per-site message under another number, and stays silent
  on the same test over a variable not named from `$_runmd`. The driver suite's kept arm is OWED at
  VERIFYING.
- AC9 — `direct-checks.sh` — `--park aSparedSpawn --reason …` prints
  `UNATTENDED check 112 FAILED — --park requires --item, because the verb's row in VERB_REQUIRES lists it, …`
  before any write; the usage render diffed against the `VERB_REQUIRES` source text reads
  `identical`; the leg scoped to 52 reds a listed pair whose call is gone and a call the table does
  not list. The suite's render and `--park` arms are OWED at VERIFYING.
- AC10 — `direct-checks.sh` — the leg scoped to 52 reds `claim mode scratch (an arm at line 2133)`,
  separately `claim class foreign-scratch (an arm at line 2133)`, and a caller passing
  `scratchmode`; `grep -c 'check 110\|check 111'` over the driver suite prints 0. The leg suite's
  arms are OWED at VERIFYING.
- AC11 — `direct-checks.sh` — a scratch call of `print_env_failure` from the sourced driver prints
  `UNATTENDED check 99 FAILED — a scratch environment failure the helper prints` and exits 2, never
  reaching the next line; the nine sites of checks 27, 29, 56, 69 and 88 call it,
  `check-arms.py --check` counts none of them, and `tools/unattended/unarmed-branches.txt` holds no
  row for checks 27, 29 or 56. The suite's arm is OWED at VERIFYING.
- AC12 — `grep -n 'is retired\|retired premise'` over the leg finds none of the three tombstone
  sites; its one hit is line 166, the `--emit-ceiling` argv refusal, which row 15 did not name and
  the batch left. The leg suite's check-47 and tombstone arms are gone.
- AC13 — `check-arms.py --check` and `--emit-floors` — the retirement pass reads five registry rows,
  each with R1 to R4, a survivor carrying its signature, a replay field and `TOOL-aSparedSpawn-14`,
  which `memory/DECISIONS.md` carries; the census fell 374:360 -> 318:309 on the driver and 266:258
  -> 264:256 on the leg, the driver's floor moved 362:348 -> 318:309 and the leg's stays 264:256 per
  rev-4, and both ceilings seed at the post-batch census. Row 15's replay is OWED at VERIFYING: the
  leg's core run it needs passed the 600 s bound.
