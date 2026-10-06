# Acceptance ledger — TOOL-aGraftedHelix-9

**Serves:** journal TOOL-aGraftedHelix-9

Node `a`, 2026-10-05. The build commit is `573acd9d`, over the spec's rev-3 commit `13a6c65e` and
the dispatch records commit `1c0afdc1`. Rev-3 recorded the pass's divergences before the code: three
functions the inventory lacked, a `path` field, `row_docs` gaining `rev`, a lenient front-matter
parse, the replay's two walks and a copy-install fixture for every check-27 arm. No merge bar and no
self-test suite ran in this pass. The one direct check was the module's own `--selftest`, which went
from 115 arms to 148, all held. Each of the 33 new arms was observed RED: 32 breaks were staged one
at a time, each in an isolated copy of the two kits under the scratchpad with the working copy never
edited. Every break redded new arms only, and every new arm went red under at least one break.

**Evidences:** TOOL-aGraftedHelix-9
- AC1 — `check 27:` — the selftest's copy-install fixture printed
  `rc=1 check 27: ARCH-tNew-1 (memory/DECISIONS.md:9) near-matches ARCH-tBase-1 at` over a
  restated base row. A staged break that lifted the floor out of reach redded it.
- AC2 — `coexists-with` — the same row carrying the token, and separately naming `ARCH-tBase-1`,
  each printed `1 near match(es), 1 satisfied` at exit 0. Dropping the token from the regex redded
  the first arm, and dropping the names test redded the second.
- AC3 — `description` — an added gotcha whose description restates a base gotcha's printed a
  `check 27:` line naming `carriage-return-kills-the-interpreter-line` and
  `near-matches crlf-breaks-shebang-lines`. With the base stem named in its body it printed
  `1 satisfied`. Enumerating no gotchas redded the first arm, and reading only the description as
  the record's full text redded the second.
- AC4 — `WARN` — under `warn:0.125` the fixture printed
  `rc=0 WARN ARCH-tNew-1 (memory/DECISIONS.md:9) near-matches ARCH-tBase-1`. Exiting 1 on any
  finding redded it.
- AC5 — `NOT ARMED` — a blank key printed `rc=0 row-grammar: check 27 NOT ARMED`, and `red:1.5` and
  `amber:0.1` each printed `rc=1 row-grammar: NEAR_MATCH_GATE='<value>' is not` with no traceback.
  Three breaks redded the three arms: the blank branch deleted, the range check deleted and the
  mode set opened.
- AC6 — `bench.py` — a fixture with no recall kit printed the refusal naming `NEAR_MATCH_GATE` and
  the memory-recall kit's index builder, with no traceback. A stale `bench.py` and an unimportable
  one each refused by name. Five breaks redded these arms: resolution skipped, `LookupError`
  escaping, both age checks deleted and the import guard narrowed.
- AC7 — `no mainline base` — with `origin/main` deleted and `main` renamed, the fixture printed
  `rc=1 row-grammar: check 27 is armed and found no mainline base`. With the base equal to `HEAD`
  it printed `rc=0 row-grammar: check 27 graded 0 added record(s)`. Falling back to `HEAD` redded
  the first arm, and suppressing an empty summary redded the second.
- AC8 — `python tools/memory-tree/row_grammar.py --measure-relations 0.125 5266d22e` — at the build
  commit it printed `band 0.125 would flag 30 record(s): 23 rows, 7 gotchas`. Its 30 pairs, family
  prefixes elided, matched §4 "The graded pairs" exactly under a sorted `diff`. The 0.10 band read
  59 rows and 28 gotchas, F1's own figures.
- AC9 — `python tools/memory-tree/row_grammar.py --check-relations 5266d22e` — at the build commit
  it printed `graded 5 added record(s) in 5266d22e..HEAD against 354 at base`, exit 0. A scratch
  probe derived the figure independently from `git ls-tree` listings and `git show` reads at both
  revisions: 4 gotcha stems and 1 row id, `TOOL-aGraftedHelix-2`, so 5.
- AC10 — `RELATION_CHECK = 27` — `grep -n` printed one line, `889`, and `grep -n 'check-relations'`
  over the hygiene engine printed one line, `2497`.
- AC11 — `27 checks` — `grep -c '^27\. ' memory/HYGIENE.md` printed 1 and the README row reads
  `27 checks`. The example conf's `NEAR_MATCH_GATE=""` is at line 300, and this repository's
  `NEAR_MATCH_GATE="red:0.125"` at line 643.
- AC12 — `[superseded by` — in the copy-install fixture an added row naming only the successor
  printed `1 satisfied`, and without it the finding read
  `near-matches ARCH-tOld-1 [superseded by ARCH-tNext-1]`. A partial edge read
  `[partly superseded by ARCH-tWider-1]`. Not reading the successor redded the first arm, and
  inverting the whole-edge test redded both tag arms.
- AC13 — `tools/memory-tree/row_grammar.py` — its header lists four NOT-checked items: a near match
  BELOW THE TOP HIT, a PARAPHRASE UNDER THE FLOOR, a BARE RELATION TOKEN THAT NAMES NO RECORD and a
  ROW EDITED IN PLACE.
- AC14 — `GOV_DEFAULT_BRANCH=trunk` — with `origin/main` behind a local `main` that moved on, no
  argument printed the merge-base with the remote as `<base8>`, grading 1 record. With `origin/main`
  moved past the fork it still printed that merge-base. With only `trunk` and the variable set, it
  printed trunk's merge-base. Preferring local `main`, taking the remote tip and ignoring the
  variable each redded its arm.
- AC15 — `memory/guides/BUILD-METHOD.md` — `git diff 13a6c65e 573acd9d` over it printed one hunk
  changing line 1 alone, `memory-tree@2.119` to `memory-tree@2.120`, the adopter's re-render of the
  version marker.
