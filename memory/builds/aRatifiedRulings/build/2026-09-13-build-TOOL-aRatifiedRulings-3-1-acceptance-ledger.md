# TOOL-aRatifiedRulings-3 — acceptance ledger

**Serves:** journal TOOL-aRatifiedRulings-3

Every observation below was made on node `a` on 2026-09-13 over the working tree this unit
commits. The owner's per-pass rule in the build README bound this pass to ONE run of the suite it
edits, alone, and nothing held, so this ledger carries one after reading and takes the before
reading from the spec's §4 traced row, measured on this node at `16da4c6a` — spec rev-4 logs that
substitution. The full bar the spec's AC3 observes is the closing pass's; its row is appended below
when `--close` buys it. The suite is `chunk: selftests`, `subject: kit`, guarded on
`tools/memory-tree/`, and no boundary runs it: every figure here came from a hand invocation, and
a green landing bar observes none of them.

## The two readings

Both traced, `PS4='+ ${EPOCHREALTIME} ${LINENO} ' bash -x tools/memory-tree/check-memory-hygiene.test.sh`
with stdout and stderr to their own files and `time` read in the calling shell. The invocation
count is the number of trace lines that run `check-memory-hygiene.sh` over the check-16 note tree:
at `16da4c6a` the one at line 2198 plus the 19 the project-key section made through `pk_rc` and
`pk_out` over its archive fixture; after, the one at line 2203 plus the twelve `pk_out` makes at
line 2229. A `git archive` count of 0 is the trace's own, not an absence assumed.

| reading | tree | real | user | sys | rc | invocations | `git archive` lines | `bash.exe` at start |
|---|---|---|---|---|---|---|---|---|
| before, §4 traced row | `16da4c6a` | 598.7 s | 168.1 s | 290.1 s | 1 | 20 | 1 | 3 and 2 (quiet) |
| after, this pass | `90348fde` + this diff | 775.682 s | 140.288 s | 320.709 s | 0 | 13 | 0 | 8 |

Ratio after over before on `real`: **1.296, ABOVE the 0.8 bound** AC2 derives from §4's 0.72. The
after run was NOT taken on a quiet box: 8 `bash.exe` at the start and 9 at the end against the
quiet reading's 3 and 2, and a sibling session's `run-gates.test.sh` self-test held five
`run-gates.sh` bars at the start and thirteen by 20:07Z, plus one `run-gates.turnstile.test.sh`,
all read with `ps -ef`; nothing of this pass's ran beside the suite. The deterministic claim is
the invocation count, which the box cannot move; the wall figure is evidence with its box state
beside it, which is what the brief settled. What the trace attributes, region by region against
the §4 table, is the evidence the wall figure alone cannot give — every region this unit did NOT
touch inflated under the load, and the one region it did touch fell anyway:

| region, after-file lines | before, §4 quiet | after, loaded | ratio |
|---|---|---|---|
| main fixture build 1-847 | 5.5 s | 50.6 s | 9.2 |
| main-tree assertions 848-1480 | 196.2 s | 253.6 s | 1.29 |
| scratch trees 1481-2172 | 164.4 s | 311.5 s | 1.89 |
| check-16 fixture and its clean run 2173-2211 | 10.9 s | 26.9 s | 2.47 |
| archive build + project-key arms, now 2212-2306 | 222.9 s | 131.9 s | **0.59** |

The section's share went 37% to 17%; its thirteen invocations cost 152.3 s in all, the seven that
proceed 13.6-29.4 s each against the §4 quiet floor of 8.0 s, the six aborts 0.1-1.3 s. The whole
trace holds 59 checker invocations where §4's held 66, which is the 19 to 12 cut and nothing else.
A paired quiet reading is the closing pass's, per spec rev-4; this row is not a verdict on the
ratio and does not claim one.

## The staged breaks

Each break was applied to a COPY of the suite by a driver that runs the check-16 fixture block and
the project-key section from the suite's own prologue, refuses a copy the break changed no byte
of, and REFUSES a run whose section printed other than 13 `ok`/`FAIL` lines or incremented `n` by
other than 13 — a break that reds nothing and a harness that never started must not print the
same empty list. Runs were sequential, never concurrent. The unbroken copy printed 13 `ok`, rc 0.

| break | what the copy changed | read | red arms |
|---|---|---|---|
| `pkset-noop` | `pk_set` redefined as `return 0` after the section header, so no key line reaches the conf | `pk_out` | violated-slug (`did not red check 4 naming memory/builds/tOne (rc=0)`), the six abort arms (`did not abort (rc=0)`), registry (`check 3 named the registry the key admits`): 8 FAIL, 5 ok |
| `pkout-127` | `pk_out` runs `$HERE/does-not-exist.sh` | `pk_out` | violated-slug value form (`(rc=127) — the key is not reaching check 4`), where the base rc-only form `[ "$r" != 0 ]` would print `ok`, plus every other `pk_out` arm at rc 127: 12 FAIL, 1 ok (the control, which reads line 2203) |
| `no-probe` | the `unlisted-probe.txt` write dropped | `pk_out` | registry probe half (`accepted a file it does not name — check 3 is disabled`): 1 FAIL, 12 ok |
| `no-ceiling` | the `READ_PATH_CEILING="135677"` line dropped from `pk_set`, so the fixture conf provokes no notice | line 2203 | control notice half (`the fixture is not clean unset (rc=0), or its clean run never reached check 16`) at rc 0: 1 FAIL in the section, 12 ok; the check-16 note arm above the section redded too |

**Evidences:** TOOL-aRatifiedRulings-3
- AC1 — `git archive` — the after trace holds 0 lines matching `git archive` and 13
  invocations of `check-memory-hygiene.sh` over the check-16 note tree: 1 at line 2203
  (the clean run the two note arms and the control share) and 12 at line 2229 (`pk_out`:
  six that proceed, six that abort at rc 2), every one with the fixture's `mktemp` root as cwd.
  The §4 trace at `16da4c6a` showed 19 over the archive fixture plus the separate clean run, and
  one `git archive` at its line 2227
- AC2 — amended rev-4 — one traced after run, alone, against the §4 traced before at `16da4c6a`:
  775.682 s over 598.7 s is 1.296, ABOVE 0.8, on the loaded box the table above records, with the
  section's own region at 0.59 of its §4 seconds by trace attribution; the after run exits 0 and prints
  `PASS (374 assertions)`, the `PASS (n assertions)` line; its count 13 is read from its own
  trace; the before count 20 is the §4 trace's. The interleaved second pair the criterion spells is
  the closing pass's if the owner wants the noise bounded, and the box state of this reading is in
  the table above
- AC3 — amended rev-4 — the `GATE_FULL=1 GATE_SELFTESTS=1` bar is the closing pass's under the
  owner's per-pass rule; its `.leg` row for `memory-hygiene self-test` is appended here when
  `--close` buys it, with the disposition §8 F3 states if it reads red
- AC4 — `PASS (n assertions)` — the after run prints `PASS (374 assertions)`;
  `grep -nE '^FLOOR_ASSERTIONS=' tools/memory-tree/check-memory-hygiene.test.sh` prints
  `FLOOR_ASSERTIONS=374`, equal to the printed `n`; the comparison against it is the statement
  immediately above the `PASS` line; and every `ok` label the section printed at `16da4c6a` — the
  nine literal prefixes `grep -oE 'echo "ok   [^"$]*'` reads off the section at BASE, expanding to
  thirteen lines — is in the after output, checked by prefix match
- AC5 — `HYGIENE check 4 FAILED` — the violated-slug arm's `case` reads `HYGIENE check 4 FAILED`
  and `memory/builds/tOne (bad folder name` from `pk_out`'s capture, and red under `pkout-127`
  where the rc-only form stayed `ok`; the registry arm commits `my-registry.txt` and
  `unlisted-probe.txt` and reads `HYGIENE check 3 FAILED` naming `memory/project/unlisted-probe.txt`
  and not `memory/project/my-registry.txt`, red under `pkset-noop` (registry named) and `no-probe`
  (probe absent); the control reads `_b1rc` and `_b1out` from line 2203, rc 0 and the
  `READ_PATH_CEILING is declared` notice, red under `no-ceiling` at rc 0
- AC6 — amended rev-4 — every break in the table above was observed RED through the section run
  from its own prologue, one observation per assertion, each naming the invocation the arm read,
  and the driver refused nothing because every run printed 13 section lines and incremented `n`
  by 13; the whole-invocation break is not taken because it is a third long run under a rule that
  allows two, and the after run's own output — thirteen section `ok` lines and the `PASS` line —
  is the proof the whole invocation reaches the section
