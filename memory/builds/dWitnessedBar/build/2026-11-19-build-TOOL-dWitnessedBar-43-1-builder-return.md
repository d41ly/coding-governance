**Serves:** journal TOOL-dWitnessedBar-43

# TOOL-dWitnessedBar-43 — builder return 1 (run `wf_a0729b11-8b2`), committed 5308f3c08e6c456920728c56d4f64e56515ff547

## Why

TOOL-dWitnessedBar-43 is built from its rev-5 spec as written. Before writing, I checked every claim the spec makes about current code against HEAD and all of them held: the inline source check in read_remote_verdict, read_remote_keys, read_scope_paths, derive_pin, read_remote_module, read_policy_value, run_git, write_peer_tag using git mktag, the guard's whole-leaf OWNER_ONLY_KEYS match, derive_leaf_changes treating an array as one leaf, the set/item grammar, and the git 2.54 verify-tag stderr lines (re-measured in a scratch repo). Unit 2's additions moved nothing this spec names. No divergence was found.

## Summary

I committed one pass commit, 5308f3c08 (subject names TOOL-dWitnessedBar-43; trailers are Decided lines, `Pass: TOOL-dWitnessedBar-43` and `Co-Authored-By: Claude Opus 5` as the charter fact says). The same commit sets the spec's status header to CLOSED (date already 2026-11-20), adds the acceptance ledger, includes RUN.md, and includes the files `gen_build_index.py --write` rewrote: the build README, memory/LIVE.md, memory/backlog/TOOL.md and the spec's generated records region. The pre-commit and commit-msg hooks passed.

**What changed**
- `C:/projects/coding-governance/.claude/worktrees/unattended-dwitnessedbar-2ed3b3/tools/run-gates/remote_verdict.py`: the source check is now one function, `check_pin_source(backend, sha, keys, repo=".")`. `read_remote_verdict` calls it for both its no-pin return and its source check, so no remote-ci state changes.
- `C:/projects/coding-governance/.claude/worktrees/unattended-dwitnessedbar-2ed3b3/tools/run-gates/verdict_backends.py`:
  - `run_git` gains `both=` (returns stderr too) and `read_policy_value` gains `every=` (returns every printed line).
  - New `read_signer_principal` writes the signer list to a temp file under the common git dir, runs `verify-tag --raw` against it, then deletes the file.
  - `read_peer_verdict` now refuses a peer verdict unless:
    - a signer table exists (otherwise NONE `no signer table`);
    - the tag is signed (otherwise NONE `unsigned`) by a key in the table (otherwise NONE, unknown key);
    - the signer is the node the tag names (otherwise NONE `signer <p> is not node <n>`).
  - After those checks, `read_peer_verdict` reads the scope:
    - `workflow` scope outside app-only reads HELD naming `verdict.remote.pin-scope`;
    - otherwise `check_pin_source` decides.
  - `write_peer_tag` signs with `git -c gpg.format=ssh tag -s` and deletes the local tag name after pushing.
  - `verify-peer` exits 2 naming `user.signingkey` when that setting is empty.
  - Four new plants (`peer-signed`, `peer-unsigned`, `peer-self-tag`, `peer-swapped-manifest`), and `peer` re-planted over the signed, pinned setup.
- `C:/projects/coding-governance/.claude/worktrees/unattended-dwitnessedbar-2ed3b3/tools/loop/guard.py`: `verdict.peer.signers` added to `OWNER_ONLY_KEYS`, plus a new plant `signers-owner-only`, also in the selftest owed map.
- `C:/projects/coding-governance/.claude/worktrees/unattended-dwitnessedbar-2ed3b3/tools/policy/catalogue.toml`: a new `verdict.peer.signers` row of type set. Its item pattern is node tag, key type, base64 key, with no options field. It is never empty and has a derived default.
- Also updated: run-gates.gov.test.sh (four plants added to its loop), the kit README, help/verdict-backends.md, help/reference/policy.md (re-rendered) and memory/map/generated/symbols.json (re-rendered).
- I asked the naming lexicon about every new name, including nested ones, and all came back OK.

**Checks that ran (each stands in for the gov canary's verdict-backend loop or the guard selftest)**
- `verdict_backends.py --fixture --plant` held every scenario for each plant:
  - `peer`: 3 of 3, exit 1.
  - `peer-signed`: 1 of 1, exit 0.
  - `peer-unsigned`: 2 of 2, exit 2.
  - `peer-self-tag`: 1 of 1, exit 1.
  - `peer-swapped-manifest`: 3 of 3, exit 0.
  - remote plants after the extraction: `remote-green`, `swapped-workflow` and `step-skipped` all held.
- `guard.py --fixture --plant signers-owner-only` exited 1 naming `verdict.peer.signers: owner-only`. `pin-owner-only` still holds.
- In-process probes:
  - `check_pin_source` returns HELD no pin, GREEN claimed under app-only, and raises DeadProbe for a SHA the clone lacks.
  - `read_policy_value(every=True)` on gov's tree passes on the derived-default refusal.
  - `write_peer_tag` leaves no local tag and pushes the ref.
  - The catalogue pattern refuses options, `cert-authority`, comma principals, `*` and `[]`.

**Owed at the close**
- Every section 7 leg: run-gates wiring, push-main self-test, remote literals, scratch-guard self-test, routed-commits selftest, policy fixtures, recall floor, recall floor arms, memory hygiene, spec tokens.
- New arm (`run-gates.gov.test.sh`, AC1 AC2 AC4): the four peer plants plus re-planted `peer`. Stage red by removing the signature check, then the source check, from `read_peer_verdict`.
- New arm (`guard.py`, AC3): `signers-owner-only` under `--selftest`. Stage red by dropping `verdict.peer.signers` from `OWNER_ONLY_KEYS`.

**For the main loop to decide**
1. `.governance/policy.json` is not re-rendered. `mirror --write` renders at HEAD and refuses an uncommitted catalogue, so it has to come after this commit, as unit 2's mirror did.
2. The catalogue summaries of `verdict.remote.pin-scope`, `verdict.remote.trust`, `verdict.remote.pin` and `verdict` still describe these keys as remote-ci only. They now cover peer-node too. The text is incomplete rather than wrong; if you fix it, do it before the mirror is rendered.
3. Like unit 6's three `verdict.remote.*` keys, `verdict.peer.signers` is read through `read_policy_value(repo, KEY)`. That is not one of `check_policy.py`'s READER_SHAPES. So `arm_reader_coverage` will likely red on these keys once dWitnessedBar lands and every spec in its build folder is terminal.

**Not mine, left unstaged:** help/reference/drive.md and help/reference/units.md were already modified (line endings only) when I started.

**Gotchas checklist:** I ran `gotchas.py --for-diff HEAD~1..HEAD` and reviewed it:
- every plant needs an exact exit plus a needle, so it cannot pass by finding nothing;
- the workflow-scope scenario pins the workflow alone, so removing that check reads GREEN, not a HELD that would mask it;
- each ledger token sits on one line and is spelled by its criterion;
- the hand-named plant list in the gov test lists all four new plants.

The only other things it surfaced are items 2 and 3 above.
