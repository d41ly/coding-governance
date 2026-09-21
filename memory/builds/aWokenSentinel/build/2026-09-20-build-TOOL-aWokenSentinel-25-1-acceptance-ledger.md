# TOOL-aWokenSentinel-25 — acceptance ledger

**Serves:** journal TOOL-aWokenSentinel-25

Every leg-shaped half below reads `observed at --close`: this pass ran no gate, no leg and no
suite. The pass verified with the direct checks the spec's section 7 names for it: the
`python3 -c`-shaped compare of AC1 (a script under the session scratchpad, `ca25/compare.py`, that
loads `tools/memory-tree/check-arms.py` by path with `importlib`, runs `classify()` over this tree
and compares each branch's `sig` and `stranded` against the `--report` row printed for it); the two
scratch-repo `--check` runs of AC2 over a fixture under `%TEMP%/ca25`; the `--selftest` run of AC3
at the tip and over two staged copies under the scratchpad, made by one `sed` each, with
`corpus_ids.py` copied beside them; and the greps of AC4. Those stand in for the `check-arms
selftest`, `harness arms`, `memory hygiene`, `spec tokens` and `install-prefix` legs, which run
once at the close. One spec fold was owed and taken as rev-2 before the code that follows it: the
rev-1 stranded read, run over this tree, named a SIBLING branch's whole arm as the stranded prefix
of three pinned branches whose messages share their first 24 characters (`check-unattended.sh`
check 2 branch 13 and check 16 branches 15 and 16, at test lines 536, 1437 and 1443), so the read
now excludes every line that arms some branch of the same gate, the selftest's `gate-c` gains a
second branch opening like the first, and the control arm is also that exclusion's arm.

**Evidences:** TOOL-aWokenSentinel-25
- AC1 — `python3 tools/memory-tree/check-arms.py --report` at the tip exited 0 and the compare printed `rows=504 branches=504 mismatched=0 stranded=1 longest_sig=361 over72=451 armed=489` and exited 0: every row's text after the ARMED column equals `signature()`'s whole return plus its `STRANDED` tail where set, and 451 of the 504 signatures on this tree are longer than the 72 characters the old row kept. `grep -c '\[:72\]' tools/memory-tree/check-arms.py` printed `1` at fa2fff81 and `0` at the tip. The one `STRANDED` row left is `check-unattended.sh` check 2 branch 13, pinned, at `check-unattended.test.sh:863`, whose `hit` quotes a message composed into a shell variable and passed as the tail of one `fail` — outside the population the tool signs, the gotcha's recorded second exclusion — so the line arms nothing the tool can see and shares its opening with the pinned branch; the spec's section 5 risks row states it as the bound. OBSERVED, logs `ca25/report-tip.log` and `ca25/report-base.log`; the legs are observed at --close.
- AC2 — over the fixture at `%TEMP%/ca25` (one gate, `tools/gate-c.sh`, whose message is 90 literal characters followed by `: $x`, measured by `printf '%s' | wc -c`, and `tools/gate-c.test.sh` quoting its first 40), `python3 <worktree>/tools/memory-tree/check-arms.py --check` run with the fixture as its working directory exited 1 with one line ending `and is not pinned in memory/project/unarmed-branches.txt — a STRANDED prefix at tools/gate-c.test.sh:1 stops short of the signature; copy the whole row --report prints`; with the test rewritten to quote the whole signature it exited 0 and printed nothing (`grep -c gate-c` over the output printed `0`); the file at fa2fff81, copied under the scratchpad as `ca25/base/check-arms.py` and run over the prefix fixture, exited 1 with the refusal ending at `unarmed-branches.txt` and `grep -c STRANDED` over it printed `0`. OBSERVED, logs `ca25/ac2-prefix.log`, `ca25/ac2-whole.log`, `ca25/ac2-base.log`; the legs are observed at --close.
- AC3 — `python3 tools/memory-tree/check-arms.py --selftest` printed `arm ok` on `20` lines at fa2fff81 and `23` at the tip (`grep -c '^arm ok'`), the three new labels being `a test quoting a prefix of a long message is named STRANDED at its line`, `...and --report prints that row's signature whole, with the STRANDED line` and `...and the same test quoting the whole signature reads ARMED with no STRANDED token`, and ended `PASS — check-arms: all arms held`. Over a copy with the `[:72]` slice restored (`sed "s/{b\['sig'\]}{tail}/{b['sig'][:72]}{tail}/"`) the report-row arm printed `arm FAIL` (the control failed with it, its row cut short) and the run ended `FAIL — 2 arm(s) failed`; over a copy with the sibling exclusion reverted to rev-1's `b["sig"] not in l` the control arm alone printed `arm FAIL` and the run ended `FAIL — 1 arm(s) failed`. OBSERVED, logs `ca25/selftest-base.log`, `ca25/selftest-tip.log`, `ca25/selftest-restored72.log`, `ca25/selftest-noexcl.log`; the leg is observed at --close.
- AC4 — `grep -c 'copy the row it prints' tools/memory-tree/check-arms.py` printed `0` at the tip and `grep -c 'STRANDED' memory/gotchas/arm-literal-strands-on-message-edit.md` printed `1`; `python tools/memory-tree/gotchas.py --check` exited 0 at the tip with `INDEX.md` untouched (the remedy paragraph adds no backticked path-like token, so the record's derived anchor count did not move). OBSERVED; the memory hygiene leg is observed at --close.
- checkers — `python3 tools/memory-tree/check-arms.py --check` over this tree exited 0 and printed nothing at fa2fff81 and at the tip, so no branch's verdict moved; the three edited files carry no CR byte (`grep -c $'\r'` printed `0` for each); `python3 tools/check-spec-tokens.py` run whole printed its three summary lines and no `HYGIENE` line, and this spec, CLOSED, is in its terminal set. No function, verb or file was minted, so no lexicon question was asked. OBSERVED; the legs are observed at --close.

## What this ledger does not evidence

No check-arms selftest leg, harness-arms leg, hygiene leg, spec-token leg, install-prefix leg or
`*.test.sh` suite ran inside this pass; every one is `--close`'s and each row above says so. The
build README's authored roster row for this unit moved `PLANNED` to `CLOSED` beside the spec
header; sibling rows were not touched. `memory/LIVE.md` and `memory/ledger/2026-09.md` were not
declared, for the reason unit 24's ledger records: unit 16's still-open dispatch row holds
`memory/LIVE.md`, and no unit pass of this build has moved either file.

The commit's pre-commit hook was let run once and refused: its staged hygiene leg and the
manifest ratchet printed no failure, and its codebase-map leg — which fires only when a staged
path is a `.py`, so units 22 to 24 never met it — failed
`test_every_inventory_key_is_claimed_or_baselined` on `gate-legs: unattended-build self-test`,
the key unit 21's leg row added and that `MAP.md` at fa2fff81 already lists `UNCLAIMED`; the
freshness test beside it passed, so nothing this pass changed moved the map. Claiming that key is
unit 27's mechanism and its write set, not this dispatch's, so the commit was made with
`--no-verify` as the charter's deliberate bypass, and this paragraph is its record. The close's bar
grades the claim on unit 27's pass.
