# TOOL-dWitnessedBar-43 — a peer-node verdict stands only under the source pin and from a tag its node signed

**Status:** OPEN · rev-2 · 2026-10-25 · node d · Tier-2 · base cdfbd1cf · streams tooling · order 29 · advances TOOL-dWitnessedBar-31

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md) | journal | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-54 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 |
| [2026-10-25-review-TOOL-dWitnessedBar-40-spec-audit-round1.md](../reviews/2026-10-25-review-TOOL-dWitnessedBar-40-spec-audit-round1.md) | spec-audit | TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-51 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit (`memory/builds/dWitnessedBar/reviews/2026-10-25-review-TOOL-dWitnessedBar-1-spec-audit-round1.md`)
confirmed finding **id 63 at HIGH**, its item **H4**, alone in that item. `TOOL-dWitnessedBar-6` S6 and
S9 apply the source rule, the pin over `verdict.remote.pin-scope`'s files, to `remote-ci` alone; it
answers gap-test-11, a verdict whose definition sits in the tree it judges. `verify-peer` (S5) runs the
candidate's own runner and manifest, and the tag it pushes carries a free-text `node` line any holder of
the push grant can write. Under `verdict = peer-node`, also `TOOL-dWitnessedBar-2`'s off-node witness for
`hooks.bypass = refused`, a candidate that empties `tools/gate-legs.json` gets a peer GREEN, and a landing
node can push its own `refs/gov/verdict/<sha>` naming another node. This unit takes the report's fix. It
repairs `TOOL-dWitnessedBar-6`.

## 2. Scope (IN)

- **S1** — The source rule for `peer-node`. `read_peer_verdict` applies the same source check
  `read_remote_verdict` applies (S6 of unit 6): each file `verdict.remote.pin-scope` names has a blob at
  the SHA equal to its entry in `verdict.remote.pin`, as `verdict.remote.trust` says. The check is one
  function, `check_pin_source(sha, trust)` in `tools/run-gates/remote_verdict.py`, which both readers
  call; a differing blob reads `HELD` naming the file, no pin reads `HELD` with `no pin`, and `app-only`
  skips it with witness `claimed`. Observed by AC1.
- **S2** — The signer table. A policy key `verdict.peer.signers`, a table of `<node tag> = "<ssh public
  key>"`, joins `OWNER_ONLY_KEYS` (unit 6 S9), so only the owner's guarded command writes it. Its catalogue
  row in `tools/policy/catalogue.toml` has default none, `summary` and `usage`. Observed by AC3.
- **S3** — The signed tag. `verify-peer` creates `refs/gov/verdict/<sha>` with `git tag -s` under the
  operator's own signing configuration, `gpg.format = ssh` and `user.signingkey`, and exits 2 naming the
  missing key when `user.signingkey` is unset. Observed by AC2.
- **S4** — The reader verifies the signer. `read_peer_verdict` writes the signer table read at the
  remote's advertised default-branch tip to a temp allowed-signers file and runs
  `git -c gpg.ssh.allowedSignersFile=<file> verify-tag --raw refs/gov/verdict/<sha>`. The verdict stands
  only when that exits 0, the `Good "git" signature for <principal>` line names a principal equal to the
  tag's `node` line, and that principal is not the reading node's tag. An unsigned tag, an unknown key or
  a principal that differs from `node` reads `NONE` naming why. Observed by AC2 and AC4.

## 3. Non-goals (OUT)

- The registry, the five states, `verify-peer`'s fetch and bar, and the lander: `TOOL-dWitnessedBar-6`'s.
- Writing the signer table or the pin: the owner's, through `policy_edit.py set`.
- Distributing keys between nodes: each operator registers their node's public key with the owner.
- A verdict-backend conformance arm over every off-node backend, the report's left-shift: AC1's
  `peer-swapped-manifest` plant is that arm for the two backends this build declares.

### Edges

- **consumes-from** `TOOL-dWitnessedBar-6` — `read_peer_verdict`, `verify-peer`, `read_remote_verdict`'s source check and `OWNER_ONLY_KEYS`, which this unit extends; without them there is no peer verdict to pin or sign
- **hands-off** `TOOL-dWitnessedBar-56` — `read_peer_verdict`, its plants and its AC3, whose failure map, signer stream, leg and guard observation the verdict-boundary minors batch settles (ids 11, 20, 35, 50)

## 4. Design

### Evidence

- Unit 6 S5: the reader stands when "the tag points at the SHA, `tree` equals the SHA's tree, `verdict`
  reads `GREEN`, and `node` is not the reading node's tag"; S6's **source** clause and S9's pin apply to
  `remote-ci` only.
- `git verify-tag --raw` over an SSH-signed annotated tag prints `Good "git" signature for <principal>
  with ED25519 key SHA256:<fp>` and exits 0, `<principal>` the first field of the allowed-signers line
  whose key signed it (measured on node d, git 2.54.0.windows.1, 2026-10-25, in a scratch repository
  under `%TEMP%` with a throwaway key); an allowed-signers line naming another principal for the same key
  prints that principal, so the principal comes from the owner's table and never from the tag.

### The read

```
read_peer_verdict(sha, tree):
  tag = fetch refs/gov/verdict/<sha>                      -> NONE when absent
  unit 6 S5's tag checks (points at sha, tree, verdict GREEN)
  signers = policy.py get verdict.peer.signers --rev <advertised tip>   -> NONE "no signer table"
  verify-tag --raw against signers                        -> NONE "unsigned" | "unknown key"
  principal == tag's node line, != this node's tag         -> NONE "signer <p> is not node <n>" | "own verdict"
  check_pin_source(sha, verdict.remote.trust)              -> HELD "<file>" | HELD "no pin" | witness claimed
  GREEN, witness witnessed
```

The signer table is read at the advertised tip, never from the working tree or the candidate, so a
landing node cannot add its own key by editing the tree it lands.

| Plant | State |
|---|---|
| `peer-swapped-manifest` | a signed GREEN from node b whose candidate's `tools/gate-legs.json` blob differs from the pin: `HELD` |
| `peer-self-tag` | a tag whose `node` line reads `b`, signed by node a's key: `NONE` |
| `peer-unsigned` | an unsigned tag from node b: `NONE` |
| `peer-signed` | a GREEN signed by node b's registered key, pinned blobs equal: `GREEN` on node a |

### Inventory

Minted: the policy key `verdict.peer.signers` and its catalogue row; `check_pin_source`; the plants of
the table. Naming cells: `check_pin_source` is asked of `python tools/lexicon/lexicon.py --suggest
check_pin_source --as py.function` at the pass.

### Migration

None under the default `verdict = local-hook`. Under `peer-node` every read is `NONE` until the owner
sets `verdict.peer.signers` and `HELD` until the owner pins, the same dark start `remote-ci` has.

### Rollout

Live at landing, dark by default.

### Files touched (estimate)

- `tools/run-gates/verdict_backends.py`
- `tools/run-gates/remote_verdict.py`
- `tools/run-gates/run-gates.gov.test.sh`
- `tools/loop/guard.py`
- `tools/policy/catalogue.toml`
- `help/verdict-backends.md`

### Alternatives rejected

- **The peer runs its own default-branch runner and manifest on the candidate.** The legs' scripts
  still come from the candidate, so the pin's file set would be bypassed by editing a leg's script; one
  source rule for both backends is one fact.
- **A signer list tracked as a plain file.** Any pusher can edit it in the tree it lands; a policy key
  under `OWNER_ONLY_KEYS`, read at the advertised tip, is written only through the terminal proof.
- **GPG signing.** It needs an install the fleet does not carry; SSH signing uses git's own verifier and
  the `ssh-keygen` Git for Windows ships.

## 5. Production-readiness checklist

- security — closes two fail-open paths: a candidate rewriting the bar's definition, and a self-declared
  node. Both checks read only the local object database and the owner's table at the advertised tip; the
  temp signer file is written under the clone's git dir and removed after the read.
- perf / scale — one `verify-tag` and one blob compare per pinned file per read.
- error / empty / loading states — no table: `NONE`; no pin: `HELD`; a verify that cannot run: `DEAD
  PROBE` naming it.
- observability — the `verdict:` line names the principal, or why none stood.
- risks — a node whose key is not registered can no longer witness; the owner registers it once.
- testing — AC1 to AC4 by plant; the arm of §7 at the close.
- migration — §4.
- user docs — `help/verdict-backends.md` gains how a node registers its key and how the pin covers a
  peer verdict.

## 6. Acceptance criteria

- **AC1** — When `python verdict_backends.py --fixture --plant peer-swapped-manifest` runs in
  `tools/run-gates/`, `read --backend peer-node` prints `HELD` naming `tools/gate-legs.json`; under
  `verdict.remote.trust = "app-only"` it prints `GREEN` with witness `claimed`.
  Red when: `read_peer_verdict` skips `check_pin_source`, so a candidate that emptied the manifest stands.
- **AC2** — When `--plant peer-signed` runs, node a reads `GREEN`; under `--plant peer-unsigned` it reads
  `NONE` naming `unsigned`; and `verify-peer` in the plant's repository with `user.signingkey` unset
  exits 2 naming it.
  Red when: an unsigned tag stands.
  fixture: the plant generates throwaway SSH keys with `ssh-keygen -N ""` in its scratch directory.
- **AC3** — When `python guard.py --staged` runs in the loop kit's directory over a fixture staging a
  change to `verdict.peer.signers` with no `Gov-Policy:` trailer, it exits 1 naming the key.
  Red when: an agent can register a signer.
- **AC4** — When `--plant peer-self-tag` runs, a tag whose `node` line reads `b` but which node a's key
  signed reads `NONE` naming the principal `a`.
  Red when: the reader trusts the `node` line over the signature.

## 7. Gates

`run-gates wiring` · `push-main self-test` · `remote literals (kit code names no remote)` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/run-gates/run-gates.gov.test.sh · covers AC1 AC2 AC4 · the four peer plants of §4, staged red by removing the signature check and then the source check from `read_peer_verdict` · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec carrying nothing and derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of `TOOL-dWitnessedBar-6`'s clause. (b) reds the parts
  join; veto 1 discards it. RESOLVED (agent, 2026-10-25, delegated): (a), rung 3, the precedent
  `TOOL-dDeclaredLoop-36` §8 F1 set. widens: none · relaxes: none
- **F2 — How does a reader know which node wrote a peer verdict?** Options: (a) an SSH signature on the
  tag, verified against an owner-only signer table read at the advertised tip; (b) the tag's tagger
  identity; (c) the self-declared `node` line, as unit 6 has it. (b) and (c) are written by whoever holds
  the push grant. RESOLVED (agent, 2026-10-25, delegated): (a), rung 3 with veto 2 lifted by the README's
  `may:` grant, because the carried clause cl-0344 names the peer-node verifier and a verifier whose
  witness any pusher can forge does not witness. grants: PLAY-dClosedLoop-3 the policy key
  `verdict.peer.signers` and its `OWNER_ONLY_KEYS` entry. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, promoted from the round-1 spec audit's id 63 (HIGH, item H4).
- rev-2 · 2026-10-25 · §3 · the Edges block gains the hands-off bullet mirroring the consumes-from
  edges of TOOL-dWitnessedBar-56, promoted by the round-1 spec audit of units 40 to 51; nothing else
  moved.

## 10. Reuse audit

The seams extended are `read_remote_verdict`'s source check, extracted once as `check_pin_source` so both
off-node readers call one function, and unit 6's `OWNER_ONLY_KEYS`. `python
tools/codebase-map/reuse_lookup.py "verify a signed tag names the node that pushed a verdict"` ranked
`read_host_name`, `parse_verdicts`, `scan_landing_nodes`, `scan_verdicts` and `check_rule_tags`; none
verifies a signature, and the tree holds no signing code, so git's own `verify-tag` is the seam.

Recall terms used: `python tools/memory-recall/query.py "how is a peer node verdict authenticated" --terms "peer-node verify-peer refs/gov/verdict signed tag allowed signers node pin-scope verdict.remote.pin HELD"`
