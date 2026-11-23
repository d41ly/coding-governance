# KICK-dKeptSession-79 — acceptance ledger

**Serves:** journal KICK-dKeptSession-79

No merge bar, no self-test suite and no gate leg ran in this pass. The criteria were observed on win32
over the working tree at the pass base `5faf589e0`: by single plants of the loop kit's own CLI, each run
alone by direct CLI; by the spec's probe `p79.sh`, copied byte for byte into the run's scratch and run
over a bare origin and one clone under `%TEMP%`; by `python -I` import probes; by a sourced probe of the
driver; and by the greps the criteria state. Every RED-first observation of a `New arm:` line is the
close's, and so is every criterion only a gate observes.

## Reconciled at this base

The spec is rev-2, grounded at `c3ba5199`. `git diff --stat c3ba5199 HEAD -- tools help` printed
nothing at the pass base, so every line the spec cites reads as it says. What the build found:

- S3's sketch keeps the marker where `rc` is non-zero or `why` is set, but the fetched branch of
  `tools/unattended/unattended.sh#print_mail_notice` sets `why` to ` · fetched` too, so that test would
  keep the marker on a fetched notice and fail AC4's `refetched` line. The design's own sentence, a
  notice that tried the remote and did not rewrite the stamp, is what is built: a `fetched` flag set
  where the stamp is rewritten, the marker touched where `tried` is set and `fetched` is not.
- S1 keeps the refs that pass `check_slug_shape` in a second array, `kept`, rather than editing `refs`;
  an emptied list returns 0 as an empty cache does.
- `read_mail_kinds` read 216 to 220 ms per call on this node (DERIVED, three calls of a sourced probe of
  the built driver in the probe's clone, 2026-11-23), not the spec's 87 to 90 ms (PINNED, its §4), which
  timed the loop kit's `--mail-kinds` alone; the resolver steps beside it are the rest. The budgets are
  priced from the 0.22s figure (DERIVED, the same probe).
- The suite's recorder writes `spawn.log` beside itself through `__dirname`, so no variable but
  `NT_PRELOAD` is added. The AC5 block's own origin-restore line is replaced by S3's rows, which restore
  the origin before the AC4 loop.
- The driver suite's effective floors read `FLOOR_ASSERTIONS` 4217 and `FLOOR_SHARD_8` 1434 at this base
  (DERIVED, the last assignment of each at `5faf589e0`), the spec's figures; they rise to 4223 and 1440
  (DERIVED, plus the six rows).
- `len(PLANTS)` read 40 in the transition module and 44 in the position engine at this base (DERIVED,
  a `python -I` import probe), the spec's figures.
- The refusal sites stay at the ceiling, `ceiling tools/unattended/unattended.sh 347/347` (DERIVED,
  `python tools/memory-tree/check-arms.py --report` after the edit): the kinds refusal is a `return 2`.
- Every `help/loop.md` anchor reads as before (DERIVED, `python tools/govkit/docs_leg.py --fingerprints`
  after the code edits): `script:tools/loop/loop_transition.py 930359dc`,
  `script:tools/loop/position.py c1931acf`, `hook:mail-notice d1c1243b` and
  `verb:unattended.sh:--mail 4c1a862e`.
- The verbs guide is the template copied, `cmp` exiting 0; the adopter was not run, since it writes more
  than this write set holds.
- `python tools/codebase-map/gen_map.py --write` rewrote `symbols.json`, `MAP.md`, `CARDS.md` and
  `inventories.json` under `memory/map/generated/`, all four in this write set.
- `python tools/lexicon/lexicon.py` exits 1 at this tree on standing debt: verb offenders 1432 over a pin
  of 1421 and six `sh.function.conv` rows (DERIVED, its output at the pass), none in a file this unit adds a
  name to; `--offenders` lists none of this unit's names, and `--suggest` answers OK for
  `read_mail_kinds`, `derive_conflicting_scenarios` and `write_unread_orders`.
- No driver mailbox read at the close's own tree was graded against a real record: this node's cache
  holds the probes' fixtures alone.

## The budget rows, re-priced

Each row names this unit and how it was read; `tools/gate-legs.json` is untouched, and the
`loop transition record` leg's ceiling of 120s (PINNED 2026-11-23, `tools/gate-legs.json`) stays the
owner's.

- `loop transition record` read 458 (PINNED, the row at `5faf589e0`) and now reads 510 (DERIVED, x1.5 of
  r 339.9s): the four plants alone at 3.28s, 3.29s, 3.53s and 2.45s (DERIVED, the probe's clock), plus
  22.0s, the kinds read at 0.22s times an ESTIMATE of 100 mailbox reads (DERIVED, the plant descriptions);
  `plants=44` (DERIVED, `len(PLANTS)`), 390s past the ceiling (DERIVED, 510 less 120).
- `loop position fixtures` stays 432 (PINNED, the row at `5faf589e0`): `mail-forged` alone read 5.1s
  (DERIVED, `time`), plus 3.7s for an ESTIMATE of 17 kinds reads, r 201.6s, x1.5 303 (DERIVED), under the
  row; `plants=45` (DERIVED, `len(PLANTS)`).
- `unattended driver selftest shard 8/8` read 6845 (PINNED, the row at `5faf589e0`) and now reads 6877
  (DERIVED, 6845 plus 32): the six rows' driver notices at 1.62s failed and 1.72s fetched and six hook
  calls at 0.05s each (DERIVED, the scratch probe `t79.sh` over p79's clone), 3.7s, plus 17.6s for an
  ESTIMATE of 80 kinds reads off the region's 70 mail-verb call sites (DERIVED, a grep of region 8).
- `loop claim fixtures` read 228 (PINNED, the row at `5faf589e0`) and now reads 233 (DERIVED, x1.5 of
  r 154.7s): one kinds read per plant's first move, 0.22s times its 15 plants (DERIVED, `plants=15`).
- `manifest-check self-test` read 5267 (PINNED, the row at `5faf589e0`) and now reads 5272 (DERIVED,
  x1.5 of r 3514.5s): an ESTIMATE of 16 kinds reads across the card-store plants that run with
  `RUN_CLAIMS` on, at 0.22s each (DERIVED, the sourced probe).
- `runlog selftest` stays 117 (PINNED, the row at `5faf589e0`): S7 changes two texts and no assertion,
  so the runlog suite's `ASSERTION_FLOOR` stays 1658 (PINNED, the task's probe at `5faf589e0`). The
  kickoff suite's `FLOOR_ASSERTIONS` stays 444 (PINNED, the same probe): no kickoff arm moves.

## Criteria

**Evidences:** KICK-dKeptSession-79
- AC1 — observed. `python tools/loop/position.py --fixture --plant mail-forged` printed the two
  `FX_OPEN_LINES` lines for the fetching read and again for the local read, then
  `position: fixture · mail-forged · held`, exit 0; no line held `IGNORE PRIOR RULES`, `obey-this`,
  `1a1b1c1d1e1f` or `2a2b2c2d2e2f`. Its RED, the base reader, is the close's.
- AC2 — observed. `grep -c 'loop_lib.py" --mail-kinds'` over the driver printed 1 (DERIVED); in p79's
  clone the driver's `--mail post tFix --to build:fy --kind bogus --subject s <body file>` printed
  `mail — not written · the kind 'bogus' is none of the closed set:` and the twelve kinds, exit 2. A
  copy of the driver beside a loop kit whose `loop_lib.py` exits 3 printed `mail — not read · the loop
  kit's mail kinds did not read:` for `--mail read tFix` and for `--mail read tFix --local`, exit 2 each.
- AC3 — observed. `acks-refused-witness`, `acks-refused-field` and `acks-refused-scenario` each printed
  its refusal, `loop: fixture · record · exit 2`, `loop: fixture · state a1a2a3a4a5a6 · open`,
  `loop: fixture · acks none` and a line ending `· held`, exit 0. `acks-landed`, `acks-failed`,
  `acks-withdrawn-question`, `mail-open` and the claim kit's `mail-held` plant, each run alone, still
  read as before over the reorder.
- AC4 — observed. `p79.sh` printed `failed · marker present 0s`, `local · marker absent` and
  `refetched · marker absent`.
- AC5 — observed. `p79.sh` printed `two calls · launches 0 0` and `aged marker · launches 1`.
- AC6 — observed. `notify-composition-unread` printed B5's `progress — tFix · transition · designing →
  building · item.design.exit` and `loop: composition · unread · the fixture's compose answered 1`, no
  `loop: progress · unread` line, and `loop: fixture · notify-composition-unread · held`, exit 0.
- AC7 — observed. `p79.sh` printed the `card` line holding
  `"additionalContext":"mail — 1 unread for tFix · a1b2c3d4e5f6`, `other []` and `launches 0`, and
  `grep -c '^same "KDS79 S5 '` over the driver suite printed 2 (DERIVED).
- AC8 — observed. `p79.sh` printed `stale · spawn windowsHide=true detached=true · driver
  tools/unattended/unattended.sh`, and `grep -c '^same "KDS79 S6 '` printed 1 (DERIVED).
- AC9 — observed. `git grep -n 'share, tokens, source' -- tools` printed nothing, exit 1, and the
  `(share, window, source)` count read 1 in each of the two files (DERIVED).
- AC10 — observed. `grep -c 'only to cover the tools'` over the hook printed 0 and
  `grep -c 'registered on every tool'` printed 1 (DERIVED).
- AC11 — the two `--for-paths` reads observed: the first named `docstring-misnames-a-returned-value`
  and the second `header-rationale-contradicts-the-registration`. `gotchas.py --check` and
  `gen_map.py --check` are the close's legs; both renders ran with `--write` after `git add`.
- AC12 — observed. `cmp` over the template and the verbs guide exited 0, and the plant-name count over
  `help/loop.md` printed 3 (DERIVED).
- AC13 — observed. The two floor greps printed 1 each and `grep -c '^same "KDS79 '` printed 6 (DERIVED).
- AC14 — observed. The import probe printed `44 45` (DERIVED); the two rows carry `plants=44` and
  `plants=45` and name this unit.

## Owed to the close

The six `New arm:` lines' RED-first observations, each on its staged break; the driver suite's shard 8
with the six `KDS79` rows; `loop transition record` and `loop position fixtures` whole; and every leg
§7 names, `gotchas selftest`, `codebase-map coverage + freshness` and `memory hygiene` among them.
