# KICK-dKeptSession-13 — acceptance ledger

**Serves:** journal KICK-dKeptSession-13

No merge bar, no self-test suite and no gate leg ran in this pass, and the legs the spec's section 7
names were not run as commands. The criteria were observed on win32 at the pass's base `0d4cf1ea`.
AC1 to AC3, AC6, AC7 and AC11 ran through the unit's own fixture CLI, `bash card-store.fixture.sh
--plant <case>`, one plant at a time, each over its own scratch remote and repository under a short
temp directory; the suite that loops over `--list` was not run. The untouched plants `render`,
`follow-per-step`, `snapshot-terminal`, `follow-foreign-after-cached` and `replay-order`, whose cards
now carry the section, printed no `MISSED` row run the same way. AC4 ran through `position.py
--fixture --plant boundary`, that one case and never `--selftest`. AC5 ran as a `node -e` probe of
`checkItemBoundary` over a scratch repository and a stub checker; the hook's suite was not run. Every
new function was graded OK by `python tools/lexicon/lexicon.py --suggest <name> --as <cell>`, and
`python tools/lexicon/lexicon.py` exited 0 over the change.

Owed to the close: every leg the spec's section 7 names, the manifest-check and scratch-guard suites
whole, the `loop position fixtures` leg, and the three `New arm:` lines' RED-first observations: the
five `pointers-` plants staged against a crossing that leaves the ref's `item —` unchanged, the hook arm
staged against a step that starts the checker on an unchanged HEAD, and the `boundary` case staged
against an unchanged key reported as crossed.

**Evidences:** KICK-dKeptSession-13
- AC1 — `pointers-render` committed two journal records a day apart, one spec-audit record and a
  second spec, `TOOL-tFix-2`, planted the stub engine's key `item.build.base@TOOL-tFix-1#aaaa0001`
  and `forked=TOOL-tFix-2` (PINNED by the plant), appended, then ran `--card --pointers --build tFix
  --session t1`. The ref's card named the 2026-01-02 journal and the review and not the 2026-01-01
  journal, its `forks —` line read the `TOOL-tFix-2` spec and `§8` alone, its `item —` line read the
  key at the fixture's HEAD, and the section sat above the READY line, which was last; four rows held
  (DERIVED, that run).
- AC2 — `pointers-boundary`: a session card with no section crossed `none → K1`; with the stub at K2
  the verb printed `boundary — K1 → K2` and the ref's card read `item — K2`; after an empty commit the
  verb printed `none crossed · item K2`, the ref's commit was unchanged and the session card's `at`
  read the new HEAD; with `--out <file>` the captured stdout was empty and the file held the line; an
  `--out` in a directory that does not exist exited 2 (DERIVED, that run). Five rows held.
- AC3 — `pointers-at-transitions` under `card.pointers = at-transitions`: the crossing `none → K1`
  left the ref's commit unchanged and rewrote the session card's `item —` line to K1; `--card
  --follow --build tFix --to designing` then published step `designing` with `item — K1`. Two rows
  held (DERIVED, that run).
- AC4 — `python tools/loop/position.py --fixture --plant boundary` over six planted answers: the key
  held printed `boundary — none crossed`, another key `boundary — <old> → <new>`, `awaiting` `→ none`,
  `none` held while awaiting no crossing, `stale-remote` and `invalid-input` kept the pointer and
  named the answer, and every `forked —` line named `TOOL-tPos-2`, the unit planted `FORKED`; it
  printed `held` and exited 0 (DERIVED, that run). The CLI over this build, `position.py dKeptSession
  --boundary none`, printed `boundary — none crossed · item none` and `forked — none` in 7.2 s
  (DERIVED, that probe), the build's answer being `awaiting`; over a slug naming no build it printed
  the kept form ending `· invalid-input` and exited 2 (DERIVED, that probe).
- AC5 — the probe called `checkItemBoundary` with a PreToolUse Bash payload over a card file owned by
  its session: with `at` unequal to HEAD it returned `''` in 58 ms (DERIVED, that probe) while the stub,
  which sleeps 4 s (PINNED by the probe), was not done; the stub then recorded exactly one call,
  `--card --boundary --build tIb --session sgtest-ib --out <common dir>/orientation/sgtest-ib.boundary`.
  With `at` equal to HEAD and a `.boundary` file waiting, the step returned that file's text and the
  file was gone; with `agent_type` set, and with the session id another than the owner line's, it
  returned `''`; none of the three started a call (DERIVED, that probe).
- AC6 — `pointers-cap` set `CARD_CAP_BYTES` to the published card's bytes less its `## pockets` section
  and half its `## pointers` section, 1977 bytes that run (DERIVED); `--card --pointers` printed `card —
  pointers not written: <n> bytes over the cap` and the ref's commit was unchanged. Two rows held.
- AC7 — `pointers-replay` published with the stub at K1, cloned the bare remote, looked the card up as
  session t2 in the clone and replayed it there: the replay printed the `## pointers` section with its
  `records —` line and `item — K1` (DERIVED, that run), held.
- AC8 — `grep -n "## pointers" help/orientation-card.md` matched the new section "The card's
  pointers", which names `card.pointers`, `every-item` and `at-transitions` (DERIVED, that probe).
- AC9 — `python tools/policy/policy.py get card.pointers` printed `every-item` in this repository,
  whose policy file sets no `card.pointers`; `policy.py lists --write` printed `drained 1:
  card.pointers`, and `grep -c card.pointers tools/policy/unsummarised-keys.txt` then printed 0
  (DERIVED, that probe).
- AC10 — `python tools/memory-tree/gen_build_index.py --latest-records dKeptSession` printed five lines,
  one per kind (deviation, journal, red-fix, research, spec-audit), no kind twice, each the newest of its
  kind by filename against a sorted listing of the build's tracked records (DERIVED, that probe), in
  0.2 s (DERIVED). A slug `a/b` and a missing slug each exited 2 (DERIVED, that probe).
- AC11 — `pointers-render` ran `--card --check --session t1` over the card the pointers verb wrote: exit
  0; with its `forks —` line cut, exit 1 and a `POINTERS — … no 'forks —' line` row (DERIVED, that run).
- AC12 — after `render_playbook.py --reference`, `grep -c 'usage: policy:card.pointers '
  help/reference/policy.md` printed 1, `grep -cP '^policy:card\.pointers\t'
  memory/project/docs-undocumented.txt` printed 0, and `docs_leg.py --fingerprints` printed the row
  `policy:card.pointers` with `help/reference/policy.md` as its page (DERIVED, that probe).
- AC13 — `len(PLANTS)` read through `python -I -c` printed 32 with `boundary` a key, and the `loop
  position fixtures` row's grep printed `plants=32` (DERIVED, that probe). The `boundary` case read
  alone by direct CLI three times took 0.146 s, 0.138 s and 0.141 s (DERIVED), so the row's note
  re-reads its proxy at 68.5 s and the budget 432 stands over 103 (DERIVED from the row's 68.3 s).
- seen-red — `loop position fixtures` — red `45016a2c4` — green `45016a2c4` — `boundary`: an unchanged key reported as crossed
- seen-red — `manifest-check self-test` — red `f6a0d7aaf` — green `f6a0d7aaf` — `pointers-render`: the pointers section written empty
- seen-red — `manifest-check self-test` — red `f6a0d7aaf` — green `f6a0d7aaf` — `pointers-boundary`: a crossing that leaves the stored `item —` unchanged
