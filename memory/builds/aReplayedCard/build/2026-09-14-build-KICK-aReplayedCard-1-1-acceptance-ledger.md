# Acceptance ledger — KICK-aReplayedCard-1, the card verbs

**Serves:** journal KICK-aReplayedCard-1

Every observation below was made at the dispatched base tree (`b0d7ffd4`, the branch tip the unit
was handed) with the unit's working-tree changes applied, by running the self-test whole and by
running its card section against staged mutants of the checker. No figure is copied from the brief
or the design record; where a figure the brief stated was not reproduced, this record says so.

## What was built

- `skills/session-kickoff/manifest-check.sh`: the `--card --write`, `--card --replay` and
  `--card --path` verbs, consumed by a pre-pass before the manifest-path catch-all, answered after
  the repo probe and the manifest discovery loop and before the no-manifest refusal, so an absent
  manifest is a `node — UNKNOWN: no registry` cell and not an exit 2. Four spec'd names —
  `render_card`, `derive_node_tag`, `write_card`, `print_replay` — plus two helpers the inventory
  did not list, `read_session_id` and `read_block`; the second replaces the audit-block read the
  C2 check used to spell inline, so the block has one reader. One constant, `CARD_CAP_BYTES`.
  `KIT_MANIFEST_VERSION` 1.3 → 1.4 with its marker; the C2 retrofit string gains the `registry`
  step. Zero new `fail` call sites: every refusal is the `MANIFEST env ERROR — …; exit 2` shape.
  This is the copy every adopter installs: on their next pull the verbs are inert until a hook
  calls them, and the version bump turns into one WARN on every check run until the adopter adds
  the key by the retrofit's step 5b — a warning, not a red, which is the contract change S4 priced.
- `skills/session-kickoff/manifest-check.test.sh`: 48 arms across AC1–AC11 plus two dispatch arms,
  all in a scratch clone of the repository that hosts the checker, inside a linked worktree of
  that clone; three helpers `run_card`, `check_eq`, `read_cell`; `write_manifest` takes an eighth
  argument (an extra audit-block line); fixture marker v1.3 → v1.4; scenario 23's retrofit literal
  follows; `FLOOR_ASSERTIONS` 62 → 109.
- `skills/session-kickoff/MANIFEST-TEMPLATE.md`: `registry: {{REGISTRY_PATH}}` in the seed's
  audit block, the marker at v1.4, the placeholder's customize note.
- `memory/guides/SESSION-KICKOFF.md`: `registry: AGENTS.md`, marker v1.4, `last-audit`
  re-stamped at the merge-base (`c4f02308`, the stamp rule on a branch); `last-body-change` stays
  at that same merge-base because the commit that changes the body cannot name itself.
- `WIRE-INTO-PROJECT.md` §4: the key in the manifest recipe's step 2, a retrofit step 5b, step 6
  and the tree diagram at v1.4.
- `memory/map/features/session-kickoff.md`: the card paragraph under "Shared seams".

## The wall, measured

`--card --write` in the linked worktree of the scratch clone: **9 s** inside the first full
self-test run on 2026-09-14 and 7.2 s in a hand smoke run an hour earlier, both on node `a` with
49 bash processes and 13 harness sessions resident (`ps -W`); **4 s** in the third full run two
hours later, when the host had quietened (the whole suite fell from 21m37s to 11m17s between those
two runs with no change to the arms). The design record's verdict 35 budgeted 1.6 s quiet and
5–6 s loaded; the verb spawns about ten git processes, which the memory note "a git spawn costs
751 ms" prices at roughly the loaded wall. Not measured on a quiet host: none existed during the
pass.

## RED before it landed — how each arm was staged

The card section was extracted into a partial suite (fixture helpers + the card arms, the floor
zeroed) and run against four scratch checkers. Every card arm went red in at least one run, and
the run names the mutation that made it red:

- **Run A — the checker as committed at HEAD, no card verbs at all.** Every arm that asks the verb
  for anything went red the way AC1 predicts: `--card` fell into the manifest-path catch-all and
  the script reported `'--card' not found`. 38 of the 47 arms then present; the nine that stayed
  green are the absence-shaped ones (nothing written, refs unchanged, no FETCH_HEAD, the common
  dir clean, one line of output), staged in run B.
- **Run B — nine independent mutations, each red on its own arm(s):** `now —` appended to the file
  on replay → the byte-identical arm and the second-replay-prints-one arm; a row-wide user match →
  both fixture registries (REG1's three Remote cells hit; REG2 too) and the replay-written node
  cell; the `tree —` cell from the normalised `pwd` → AC2 tree; the cap comparison disabled → AC7;
  `--path` touching the file → AC6 wrote-no-card; a `git fetch` inside the verb → AC9's refs and
  FETCH_HEAD arms; an absent conf refusing → AC10 and AC9's card line; a guessed `null` id → the
  no-id arm, the empty `--session` arm, and the refused-ids-wrote-nothing arm (a `null.md`
  appeared); the replay-written header claiming `--card --write` → AC5's writer arm; and a stray
  `mfcstageB-stray.md` placed in this repository's real common dir before the run → AC11.
- **Run C — the table walk not stopping at the first table nor at the next heading, and
  `primary` hardcoded:** REG1 resolved two rows (`q` and the decoy `z` under `## §2`), and AC2's
  tree arm read `primary` in the linked worktree.
- **Run D — backticks not stripped:** REG1's backticked cell matched nothing, and the real
  `AGENTS.md` arm read a backticked tag.
- **The seed arm** was run by hand against a copy of `MANIFEST-TEMPLATE.md` with the `registry:`
  line deleted, and against HEAD's seed, which has no such line: FAIL both times.

The two arms the first full run found red were the suite's own defects, not the verb's: the
`recent —` extractor required a trailing space the bare `recent —` line does not carry, and a CR
count written as `grep -c $'\r'` matched every line of a LF card under MSYS grep (12 of 12; `tr -dc`
counts bytes and reads 0). Both fixed; neither moved the checker.

**Evidences:** KICK-aReplayedCard-1

- AC1 — `manifest-check.test.sh` — in the clone's linked worktree, the write verb run as
  `--card --write --session <nonce>-t1` exited 0; `<nonce>-t1.md` existed under the clone's
  common dir in `orientation`; `cmp` found stdout byte-equal to the file. Run A (HEAD checker)
  reds all three with `'--card' not found`.
- AC2 — `manifest-check.test.sh` — the `tree —` line equalled the line the suite composed from
  `git rev-parse --show-toplevel`, the word `worktree`, `branch card-wt`, `git rev-parse HEAD` as
  BASE and the dirty count; `worktrees — 2` equalled `git worktree list | wc -l`; the live cell
  read `live — LIVE.md · 21 non-terminal builds` and equalled `grep -c '^| \['` over the clone's
  `memory/LIVE.md`; the `recent —` block equalled `git log --oneline -5`; the last line was
  `READY — none yet`; the header matched the session, an ISO time and
  `by manifest-check.sh --card --write`; CR bytes 0. Wall 9 s and 4 s, see above. Red in run B
  (pwd spelling) and run C (`primary` in the linked worktree).
- AC3 — `manifest-check.test.sh` — stdin at `/dev/null` and no `--session`: exit 2 naming the
  JSON on stdin (the SessionStart hook's channel) and `--session <sid>`; `<nonce>-..-t3`,
  `<nonce>/t3` and an empty value: exit 2 naming the id; the `orientation/` entry count unchanged
  across the four; a piped `{"session_id":"<nonce>-t2"}` with no `--session` wrote
  `<nonce>-t2.md`. Red in run B (a guessed `null` wrote `null.md`).
- AC4 — `manifest-check.test.sh` — the clone's manifest naming `registry: AGENTS.md` gave
  `node — a · daily-agent` on this node (the arm runs on `USERNAME=daily-agent` only and announces
  its skip elsewhere); REG1 — Remote repeating the user on every row, the matching cell backticked,
  a decoy `other @ <user>` row, a matching table before the heading and another after the first —
  gave `node — q · daily-agent`; REG2 gave `node — UNKNOWN` with the reason
  `no Machine/user cell in REG2.md matches daily-agent`; `registry: NOPE.md` gave
  `UNKNOWN: registry NOPE.md is not a file in this tree` with the card still written; no key gave
  `node — UNKNOWN: no registry`. Red in runs B, C and D for the three predicates the criterion
  names.
- AC5 — `manifest-check.test.sh` — `--card --replay --session <nonce>-t1` printed the stored bytes
  then one line `now — HEAD <sha> · card-wt · dirty <n>`; `cmp` found the file unchanged; a second
  replay printed one `now —` line; `--card --replay --session <nonce>-t5` with no card wrote one
  whose header ends `by manifest-check.sh --card --replay`, whose node cell read
  `node — q · daily-agent` against REG1, followed by one `now —` line. Red in run B on all four
  predicates.
- AC6 — `manifest-check.test.sh` — the verb the criterion spells as `--card --path --session t1`,
  run with the suite's nonce id, printed one line ending `/orientation/<nonce>-t6.md`, exit 0, and
  no such file existed after. Red in run B (path wrote).
- AC7 — `manifest-check.test.sh` — `CARD_CAP_BYTES=100` gave exit 2, a message naming
  `over the 100-byte cap`, and no `<nonce>-t7.md`; a second arm reads the shipped default line
  `CARD_CAP_BYTES=${CARD_CAP_BYTES:-8192}` from the checker, because the first substitutes its own
  value. Red in run B (comparison disabled); the second arm red by hand against a copy defaulting
  to 4096.
- AC8 — `manifest-check.test.sh` — `PASS (110 assertions)` on node `a` against
  `FLOOR_ASSERTIONS=109`, the floor being every arm that runs on every node (the exact-tag arm
  against the real `AGENTS.md` runs on node `a` alone); `check-arms.py --check` exit 0 with
  `ARMS_FLOORS` untouched at `manifest-check.sh:28:28`, because no refusal is a `fail` call.
- AC9 — `manifest-check.test.sh` — a clone of a template repo whose origin then took one more
  commit: `git rev-parse HEAD` and `origin/main` byte-equal before and after `--card --write`, no
  `FETCH_HEAD`, the card read `node — UNKNOWN: no registry` (no manifest at all) and a tree line
  of `<toplevel> · primary · branch main · BASE <sha> · clean`. Red in run B (a fetch in the verb
  moved `origin/main` and wrote FETCH_HEAD).
- AC10 — `manifest-check.test.sh` — a template repo with a manifest and no `.memory-tree.conf`:
  exit 0 and `live — skipped: no .memory-tree.conf in this tree`. Red in run B (an absent conf
  refusing with exit 2).
- AC11 — `manifest-check.test.sh` — after the whole suite, this repository's real common dir
  held no `orientation/` entry with the suite's nonce (the suite's cards all lived under the
  scratch clone's common dir, removed with `$TMP`); the seed arm found `registry:` in the shipped
  template's audit block. Red in run B (a stray `mfcstageB-stray.md` placed there beforehand) and
  by hand against a seed without the key.
