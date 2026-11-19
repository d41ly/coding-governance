# TOOL-dPlacedRequest-2 — acceptance ledger

**Serves:** journal TOOL-dPlacedRequest-2

The unit was built from its spec at rev-9 (PINNED) on base `4f6532a75`. The kickoff engine,
`skills/session-kickoff/manifest-check.sh`, gains the build card: `read_card_policy`, one literal
`policy.py get` line per key; `render_build_card`; `write_build_card`, the publish to each store
`card.store` selects, the ref written through the inline `gov_ref_sh` block's `write_gov_ref` with the
tip `read_card_ref` fetched; `write_card_snapshot`, the `card` record through the record factory's
`write_record`, its anchor the loop kit's `tools/loop/loop_transition.py#resolve_build_anchor`;
`write_card_follow`; `resolve_build_card`, the lookup; `derive_resume_lines`, the replay's resume; and
R7, `skills/session-kickoff/manifest-check.sh#check_card_terminal`, called by
`skills/session-kickoff/manifest-check.sh#check_card_route`. The verbs are `--card --publish`,
`--card --follow`, `--card --lookup` and `--card --path --build`; the append publishes at READY and
`skills/session-kickoff/manifest-check.sh#print_replay` runs the lookup and the resume lines. The
engine carries the `gov_ref_sh` and `gov_feed_sh` blocks inline. The loop kit's
`tools/loop/loop_transition.py#write_transition` ends with
`tools/loop/loop_transition.py#write_card_follow`. The record factory gains the `card` kind and
`tools/memory-tree/build_records.py#read_card`; `tools/memory-tree/tree_lib.py` lists it in
`TYPED_RECORD_KINDS`; the HYGIENE template and its render name it. The scratch guard's
`tools/hooks/scratch-guard.js#readCard` asks the checker's `--card --path` through
`tools/hooks/scratch-guard.js#resolveKickoffChecker`.

No gate, suite or bar ran in this pass. The criteria were observed by the unit's own fixture,
`bash skills/session-kickoff/card-store.fixture.sh --plant <case>`, each case once, after the last
engine edit, each building a bare remote and a scratch repository under the node's short temp path
and removing them: all 23 cases (PINNED) exited 0, printing 48 `held` lines (DERIVED) and no
`MISSED` line, and `lookup-offline` ran again after the lookup's last edit; and by the probes named
below.

**Evidences:** TOOL-dPlacedRequest-2
- AC1 — `card — tFix · step unrecorded` — the plant `render` printed `held` for the ref card's first
  line, for its `## pockets` and `## route` sections and for its READY line last.
- AC2 — `refs/gov/builds/tFix/card` — the plant `publish` printed `held` for the bare remote holding
  the ref, the cache's first line naming its commit and a second publish's commit parented on the first.
- AC3 — `card.store` — the plants `store-remote`, `store-local` and `store-folder` each printed `held`
  for that store alone written, under `card.snapshot` `every-transition` so an unselected build folder
  would show; `store-empty` printed `held` for no store written, the refusal named and the session
  card appended.
- AC4 — `step designing` — the plants `follow-rerender`, `follow-per-step` and `follow-fixed` printed
  `held` for the tail kept, for `READY — none yet` with no route, and for the ref unchanged with its
  `fixed-at-start` line; each printed `held` for a terminal follow publishing `step landed`, its
  message's third line `step: landed · terminal`.
- AC5 — `card snapshot(tFix): landed` — the plant `snapshot-terminal` printed `held` for one record
  and `snapshot-every` for two, `build_records.py read` grading each clean and the last committed alone.
- AC6 — `re-derived` — the plant `lookup` printed `held` for a planted stale cache not trusted, for
  `t2.md` holding the session's header and the build card's route, and for the cache rewritten to the
  ref; `lookup-offline` printed `held` for those and, with the remote moved away, `evidence` reading
  the cache.
- AC7 — `resume —` — the plants `context-idle`, `context-always-resume` and `context-always-fresh`
  printed `held` for fresh, resume and fresh over a transcript dated 1800 seconds back (PINNED), the
  stub `read_card_fixture_verdict` exported printing `pass`; `context-fixture-red` printed `held` for
  the override line with the import line in `CLAUDE.md` and the stub red, and again with no stub;
  `context-transcript-absent` printed `held` for `transcript absent` with no `transcript_path` and with
  one naming a deleted file.
- AC8 — `partial —` — the plants `partial-continue`, `partial-restart` and `partial-ask` printed
  `held` for `2 uncommitted path(s)` (DERIVED) and the value named; `partial-restart` printed `held`
  for `grep -q 'partial/<slug>/<sid8>'` over the kickoff skill.
- AC9 — `route R7 REFUSED` — the plant `terminal-route` printed `held` for the append exiting 1 with
  the refusal, the card byte-identical, and the replay printing `route — re-checked · R7`.
- AC10 — `'--card', '--path'` — `grep -n` over the hook found the call in `readCard`, and
  `grep -c "'orientation', sid"` printed 0 (DERIVED). Fed a recorded Edit payload of this session as
  gov-builder, the hook from this worktree exited 0; `readCard` over this repository's common dir read
  this session's card, a stub checker exiting 1 read as no card naming why, and a fixture under the
  `/tmp` mount read through `cygpath`.
- AC11 — the catalogue probe printed the five `card.*` and `resume.*` keys; `scan_reader_keys` over
  this worktree printed `['card.follows', 'card.snapshot', 'card.store']`; `git grep -n
  "read_card_policy card.store"` found the read.
- AC12 — `--print-bindings` — the plant `snapshot-terminal` printed `held` for an `S` row of the
  `-card-1.md` record, kind `card`, anchor `TOOL-tFix-1`, and no `A` row; the record factory's own
  plant, `build_records.py --fixture --plant typed-kinds`, printed the `card` kind `bound` and its PASS
  line over every typed kind.
- AC13 — `snapshot kept` — the plant `close-follow-twice` printed `held` for the second follow's line
  and one record whose `Step` reads `withdrawn`.
- AC14 — `scan_reader_keys` over a scratch repository holding the awk cut of `read_card_policy`
  printed the five keys, and over one holding only `read_card_policy card.store` printed `[]`.
- AC15 — over that cut, the `get card\.` and `get resume\.` grep printed 5 (DERIVED) and the
  variable-key grep printed 0 (DERIVED).

The loop kit's follow was probed by `python -c` over `tools/loop/loop_transition.py#write_card_follow`
with a stub engine: `--terminal` passed for `landed`, a member of the `terminal` set, and not for
`designing`; no engine printed `card — skipped: no kickoff engine`. Its fixture's plant `default`
recorded its move with that skip line printed.

Owed at the close, by the main loop: the `manifest-check self-test` leg's five card-store arms and
the `scratch-guard self-test` leg's three readCard arms, each with the RED-first observation its
`New arm:` line asks for (a lookup trusting a stale cache; a checker that does not answer read as a
card); the `resolve-python` parity rows and the gov_feed_sh carrier arm over the engine's two new
copies; the `routed-commits selftest`, `policy fixtures` and `codebase-map coverage + freshness` legs.
