# TOOL-dPlacedRequest-33 — acceptance ledger

**Serves:** journal TOOL-dPlacedRequest-33

The unit was built from its spec at rev-8 (PINNED) on base `64a6f71ec`. The driver gained
`tools/unattended/unattended.sh#write_card_ref` behind the `--card-ref write <slug> --message <file>`
dispatch arm, dark behind `RUN_CLAIMS`; the kickoff engine's
`skills/session-kickoff/manifest-check.sh#write_build_card` now calls it bounded, as
`skills/session-kickoff/manifest-check.sh#derive_claims_line` calls `--claims`, and the engine's inline
`gov_ref_sh` block and `run_card_git` are gone, its `gov_feed_sh` copy kept for
`skills/session-kickoff/manifest-check.sh#read_card_ref`'s sightings by the spec's F2.

No gate, suite or bar ran in this pass. Each criterion below was observed by the unit's own fixture,
`skills/session-kickoff/card-store.fixture.sh`, one plant per run with `TMPDIR` on the node's short temp
path, or by a probe calling the driver over a scratch bare origin and one clone with a minimal
`.unattended.conf`.

**Evidences:** TOOL-dPlacedRequest-33
- AC1 — `--plant publish-off` held: with the fixture's conf rewritten to `RUN_CLAIMS="off"`, `card.store` at
  its default and `card.snapshot` at `every-transition`, the append printed
  `card — remote-ref not written: RUN_CLAIMS is off`, the clone cache's first line read `# card-ref local`,
  the build folder held 1 card record (PINNED) and `git -C <bare> for-each-ref refs/gov/builds` printed
  nothing.
- AC2 — the same plant, the conf then back at `RUN_CLAIMS="on"` and the append run again: the bare remote
  held `refs/gov/builds/tFix/card`, `gov-feed.log` held a line naming that ref and its commit, and
  `refs/gov/remote/builds/tFix/card` in the clone named the same commit. The plant `publish` held too:
  the cache's `# card-ref` names the written commit and a second publish is parented on the first.
- AC3 — `--plant publish-hung` held: with the scratch repository's driver replaced by a stub whose
  `--card-ref` execs a sleep and `CARD_FETCH_BOUND=4` (PINNED), the append printed
  `card — remote-ref not written: no answer within 4s`, took 4 s (PINNED) over a control append whose
  stub answers `card-ref — off` at once, and the session card holds its READY line. No sleep outlived
  the plant. The clock is the excess over the control because the append alone took 4 s (PINNED) on
  this node, longer than the 3 s (PINNED) slack, so the whole append's wall cannot hold under any bound
  here; the excess is what the bound decides.
- AC4 — `git grep -n '^# >>> gov_ref_sh' -- skills/` and `git grep -n run_card_git -- skills/` each
  printed nothing and exited 1 (PINNED).
- AC5 — the driver over the probe clone with `RUN_CLAIMS="off"` and a one-line logging `git` stub first on
  `PATH` printed `card-ref — off`, exited 0 (PINNED), and the stub's log held 2 calls (PINNED), the conf
  load's `rev-parse --show-toplevel` and an `ls-files` of kit descriptors, neither a `fetch` nor a
  `push`. Liveness: the same stub under `RUN_CLAIMS="on"` logged 2 (PINNED) `fetch` or `push` calls.
- AC6 — `grep -n -- '--card-ref' tools/unattended/VERBS.template.md` prints the verb's row, which names
  the verb and `RUN_CLAIMS`; `memory/guides/UNATTENDED-VERBS.md` is a byte copy.
- S1's other answers, by probe: a write printed `card-ref — builds/tFix/card · <sha8>` and exited 0, a
  second write's commit was parented on the first's, and the form, a slug off the build-folder grammar,
  an unreadable and an empty message file, two remotes and an absent origin each printed
  `card-ref not written — <why>` and exited 2 (PINNED).
- Every other plant of the fixture held after the change, 22 (DERIVED from `--list` less the three
  above): the existing remote-ref cases read `$REF` through the driver now.

**Owed at the close.** The two `New arm:` lines of section 7. The fixture's `publish-off` and
`publish-hung` plants, which `skills/session-kickoff/manifest-check.test.sh` now runs beside the
existing five, RED-first against `TOOL-dPlacedRequest-2`'s inline publish. The region-eight block
`TOOL-dPlacedRequest-33` in `tools/unattended/unattended.test.sh`, 21 assertions (DERIVED: 15 `same`, 6
`hit`), RED-first for AC5 against a verb that reads the remote before it tests the switch; the suite is
waived for this build's landing by README rule 8. The floors rose by the same 21 (DERIVED):
`FLOOR_ASSERTIONS` and `FLOOR_SHARD_8`. The kit gate's check 26 joins the new verb to the Skill's verb
list, so `.claude/skills/unattended/SKILL.md`'s size row rose by the 55 bytes (DERIVED) of that line,
under the run-raise terms of `tools/template-size-limits.txt`; its decision row is the main loop's.
