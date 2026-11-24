**Serves:** research KICK-dKeptSession-80

# dKeptSession — the close's red-first observations of the build's new arms, and the arms not observed

The main loop on node a observed each arm below in a detached scratch worktree of this branch: the arm run green, run
again red with one break staged in the file the arm holds, and run green once more with the break reverted. The arm's
own judgment decided: `run_selftest_cases` filtered to one plant for the loop kit, `check_policy.py --fixture <case>`,
the runlog suite's `main` over one `test_` function, `card-store.fixture.sh --plant`, and one line of
`actions-free.fixture.sh --plant`. No self-test suite ran whole, and no `tools/unattended/` suite ran at all. The lines
are in each unit's acceptance ledger, as `- seen-red` lines under its Evidences block.

Two early reds were thrown away and redone, since the break crashed the module before the arm ran: unit 63's
`test_extract_env_reads` and unit 65's `test_gov_remote_scrub`. Several breaks held green or missed their marker at first
and were replaced. `mail-boundary` was run again on an unloaded node, where it read the same.

A green run found a red of its own. `presets-core-only` printed `guard-trace · WRONG` before any break: the policy
fixtures guard missed `tools/playbook/layers.toml`, and `fixtures-guard-census` named two more files. `dcc7e30f8`
fixed all three.

## The unattended driver, observed by hermetic probes

Its arms resolve to no leg, so no seen-red line names one. Six functions were called from the sourced driver over
planted inputs, with no fetch and no write, healthy and then broken, and each read red:
- unit 28, `check_mail_recipient` with every recipient read as legal, and `check_mail_addressed` with a unit of any
  build read as addressed;
- unit 22, `derive_message_id` with the session joined in;
- unit 31, `derive_message_id` with the six-field id;
- unit 24, `check_mail_deadline` with the hours read twice over;
- unit 6, `run_mail_ring` with `mailbox-only` unread.

## Not observed red

Each of these needs its suite run whole, or a two-clone mailbox the suite alone builds:
- `tools/unattended/unattended.test.sh`, the posting, reading, landing, deadline-feed, progress and lease arms of units
  5, 7, 11, 21, 23, 24, 25, 27, 35, 44, 56, 61, 62, 63, 64, 65 and 79, and the rest of units 6, 22, 28 and 31;
- `tools/unattended/pass-tree.test.sh`, unit 67's K67 block;
- `tools/policy/adopt-policy.test.sh`, units 4 and 44, and `adopter-fresh-target` for units 1 and 4;
- `tools/lib/resolve-python.test.sh`, unit 62's parity rows, and `tools/hooks/scratch-guard.test.sh`, unit 13's
  boundary step;
- the manifest-check plants of unit 12 but `context-fixture-red`, of unit 13 but two, of unit 14 but three, of unit 15 but
  four, of unit 26 but two and of unit 38 but two, and unit 44's two pointers rows, where the one break staged held green;
- unit 44's notices plants under a parent region left unwritten, and unit 79's two notice-hook rows on S5 and S6.
KICK-dKeptSession-86 asks for them.
