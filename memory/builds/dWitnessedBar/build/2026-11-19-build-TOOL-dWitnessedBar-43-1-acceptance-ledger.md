# TOOL-dWitnessedBar-43 — acceptance ledger

**Serves:** journal TOOL-dWitnessedBar-43

This pass ran no merge bar, no gate leg and no self-test suite. Every criterion below was checked on node
d on 2026-11-20 by probing the unit's own code: `verdict_backends.py --fixture --plant` for `peer`,
`peer-signed`, `peer-unsigned`, `peer-self-tag`, `peer-swapped-manifest`, `remote-green`,
`swapped-workflow` and `step-skipped`, each over a scratch repository under `%TEMP%` with throwaway keys
made by `ssh-keygen -N ""`; `guard.py --fixture --plant signers-owner-only` and `pin-owner-only`; an
in-process call of `check_pin_source` with no pin, under `app-only`, and over a SHA the clone lacks; and
`policy.py get verdict.peer.signers` through `read_policy_value(..., every=True)` on gov's tree, which
refused with the derived default. The close owes every leg of section 7 and the RED-first observation of
its two `New arm:` lines: the four peer plants and the re-planted `peer` plant in
`tools/run-gates/run-gates.gov.test.sh`'s verdict-backend loop, staged red by removing the signature
check and then the source check from `read_peer_verdict`; and the `signers-owner-only` plant in
`tools/loop/guard.py`, staged red by dropping `verdict.peer.signers` from `OWNER_ONLY_KEYS`.

**Evidences:** TOOL-dWitnessedBar-43
- AC1 — `peer-swapped-manifest` — the plant exited 0 with 3 of 3 scenarios held: under
  `dispatch-closure` `verdict: peer-node · HELD` naming `tools/gate-legs.json` among the pinned files
  and both ids; under `workflow`, the workflow alone pinned, `HELD` naming `verdict.remote.pin-scope =
  workflow pins only`; under `app-only` `GREEN · <sha8> · witness claimed`.
- AC2 — `peer-signed` — the plant read `verdict: peer-node · GREEN · <sha8> · witness witnessed` on node
  a, exit 0; `peer-unsigned` read `NONE` naming `is unsigned`, and `verify-peer` with
  `user.signingkey` empty printed `verify-peer refused · user.signingkey reads empty` and exited 2, the
  plant exiting 2 with 2 of 2 held.
- AC3 — `signers-owner-only` — `guard.py --fixture --plant signers-owner-only` in `tools/loop/` staged
  `verdict.peer.signers` with its change record and decision row under `agents-with-reason` on `main`,
  no run's branch: `--staged` exited 1 printing `verdict.peer.signers: owner-only, refused for every agent
  commit off a live run's branch`; the plant exited 1, 1 of 1 held.
- AC4 — `peer-self-tag` — a tag whose `node` line reads `b`, signed by node a's key, read on node a:
  `verdict: peer-node · NONE · <sha8> · signer a is not node b`, exit 1, 1 of 1 held.
