# Verdict backends

**What it is.** A landing stands on a verdict: a record that the merge bar passed on the commit
being pushed. The policy key `verdict` names which backend gives that verdict. Three backends are
registered:

- `local-hook`, the default. The bar this node's own pre-push hook runs. Nothing changes from a
  repository with no `verdict` key. A green record counts only where the hook itself would adopt it:
  no leg of its run came from the reuse cache, and the legs it held by a selection are the ones the
  landed revision selects. Otherwise the read is `NONE`.
- `peer-node`. A second fleet node runs the bar on the commit and publishes its verdict. Only a
  verdict from another node, for the commit's own tree, signed by that node's registered key and
  run from the pinned files, counts.
- `remote-ci`. A push run of the repository's remote CI workflow, `.github/workflows/remote-ci.yml`,
  read from GitHub's public API. It counts only under the witness rule below.

The backends are rows in a registry. Each kit that offers a backend declares it as a
`[[verdict_backend]]` row in its own `kit.toml`. The run-gates kit declares the three above. A
backend name declared twice is refused, naming both descriptors. The reader is
`<prefix>/run-gates/verdict_backends.py`, which is under `tools/run-gates/` in this repository.

## What a read answers

Every backend is read the same way, with `verdict_backends.py read --sha <sha>`. The read prints
one line:

    verdict: <backend> · <state> · <sha8> · <why>

| State | Meaning |
|---|---|
| `GREEN` | The backend's bar passed on this commit's tree. The only state a landing stands on. |
| `RED` | The backend's bar failed on this commit's tree. |
| `NONE` | The backend holds no verdict for this commit, or holds one that does not count. |
| `HELD` | `remote-ci` or `peer-node`: the bar passed, but the pinned files differ, no pin is set, or, for `peer-node`, `verdict.remote.pin-scope` is `workflow`. |
| `DEAD PROBE` | The read itself failed, so nothing is known. |

`NONE`, `HELD` and `DEAD PROBE` are never green. The read exits 0 on `GREEN`, 1 on any other state
and 2 when it refuses. With `--backend <name>` it reads that backend. Without it, it reads the
value of `verdict`, and a value no row declares is refused, naming it and the declared names.

## Choosing a backend

Set `verdict` in `.governance/policy.toml` and commit it. The key is read at the landed revision,
never from the commit being judged. The lander, `push-main.sh`, reads it before each landing push:

- Under `local-hook` it lands as it always has.
- Under `peer-node` it publishes the commit as `refs/gov/candidate/<sha>` on the remote. It lands
  only once a peer's verdict for that commit reads `GREEN`. Otherwise it exits 1, naming the state.
  It does not wait: run the landing again after the peer has published.
- Under `remote-ci` it lands only when the remote run reads `GREEN` for the commit it is about to
  push.

A `verdict` value the policy reader refuses, or one no row declares, stops the landing before any
push.

## Running the peer verifier

On a second node, with `GOV_NODE` set to that node's tag, run `verdict_backends.py verify-peer`. It
lists the remote's `refs/gov/candidate/*` refs and skips any that already carry a verdict. For each
of the rest, it fetches the commit and runs the bar on it with `GATE_FULL=1`, in a detached
worktree of the node's own clone. It then pushes an annotated tag `refs/gov/verdict/<sha>`. The
tag's message carries the bar's `verdict`, `tree` and `run_id`, and a `node` line. `--remote
<name>` names the remote; the default is `origin`. Nothing schedules it: the peer's operator runs
it, by hand or from its own cadence.

The tag is signed with the node's SSH key, `git -c gpg.format=ssh tag -s`, under the operator's
own `user.signingkey`. With `user.signingkey` empty, `verify-peer` refuses, exit 2, before it reads
the remote.

The reading node needs `GOV_NODE` set too, because a tag from its own node is `NONE`.

## Registering a node's key

A peer verdict counts only when the node that signed it is registered. `verdict.peer.signers` holds
one line per node, in git's allowed-signers form with no options field:

    verdict.peer.signers = ["b ssh-ed25519 AAAAC3Nza..."]

The first field is the node's tag, its `GOV_NODE`. The rest is the node's public key, the first two
fields of its `.pub` file. Each node's operator sends that public key to the owner, and the owner
sets the list from a terminal, or through the loop kit's `policy_edit.py set` on a live run's
branch. The loop guard refuses an agent's change to the list anywhere else.

The reader takes the list at the landed revision, never from the commit being judged, so a landing
node cannot register its own key by editing what it lands. It runs `git verify-tag` against the
list. The verdict counts only when the key that signed the tag belongs to the node the tag's `node`
line names, and that node is not the reading one:

- An unsigned tag, or one signed by a key no line names, is `NONE`.
- A tag whose message was changed after it was signed has a bad signature, and is `NONE`, naming the
  bad signature. A verify that cannot run, such as one with no `ssh-keygen`, is `DEAD PROBE`.
- A tag whose `node` line names another node than its signer is `NONE`, naming the signer.
- With no list set, every peer read is `NONE`, `no signer table`.

## How the pin covers a peer verdict

A peer runs the candidate's own runner and leg manifest, so the source check `remote-ci` applies
applies to a peer verdict too: the pinned files, read at the commit, must derive
`verdict.remote.pin`. A candidate that empties `tools/gate-legs.json` reads `HELD`, naming the files.

`peer-node` needs `verdict.remote.pin-scope = "dispatch-closure"`. The default, `workflow`, pins
only `.github/workflows/remote-ci.yml`, which no peer runs, so under it a peer read is `HELD`,
naming `verdict.remote.pin-scope`. Under `verdict.remote.trust = "app-only"` the source check is
skipped and a passing peer read is `GREEN` with witness `claimed`.

## The remote-ci witness rule

A remote run stands as a verdict only when every field holds:

- **Key.** A push run whose `head_sha` is the commit judged. The commit's tree is resolved in the
  reading clone, and a commit the clone lacks is `DEAD PROBE`.
- **Writer.** The run's check suite was written by the `github-actions` app. Its `path` is the
  declared workflow and its event is `push`. It carries the declared job, `bar`.
- **Liveness.** The job's bar step concluded `success`. A `skipped` step is `NONE`.
- **Source.** The pinned files, read at the commit, derive the pin.

`verdict.remote.trust` decides what the source check does:

- `pinned-workflow` (the default): pinned files that differ read `HELD`. An owner item asks to
  re-pin or to refuse the change.
- `owner-reviews-workflow-change`: the owner item opens at the first differing read. The slot stays
  `HELD` until the owner re-pins.
- `app-only`: the source check is skipped. A passing run reads `GREEN` with witness `claimed`,
  never `witnessed`.

Under an unattended run, the driver's gates-green term reads the slot under `verdict = remote-ci`
and files a `HELD` read as one owner item, reused while it stays open.

## Setting the pin

`verdict.remote.pin-scope` names the pinned files, for `remote-ci` and `peer-node` alike. `workflow`, the default, pins
`.github/workflows/remote-ci.yml`. `dispatch-closure` adds `tools/run-gates/run-gates.sh`,
`tools/gate-legs.json` and `.githooks/gate-env.sh`.

`verdict.remote.pin` holds one object id: `git hash-object --stdin` over one `<path> <blob id>` line
per pinned file, sorted by path. `remote_verdict.py pin` prints those lines and the
`verdict.remote.pin = "<id>"` line the owner would set at HEAD. It writes nothing. Until a pin is
set, `remote-ci` reads `HELD` with the reason `no pin`.

The pin is the owner's. Set it from a terminal, or through the loop kit's `policy_edit.py set
verdict.remote.pin <id>` on a live run's branch. The loop guard refuses an agent's change to the pin
anywhere else, whatever `policy-file.guard` reads.

## What it does not check

- That a peer ran the bar its tag names, beyond the pinned files it ran it from.
- That `GOV_NODE` is unique across the fleet, or that a registered key is still held only by its
  node.
- That the pinned files are everything the bar job runs. `dispatch-closure` pins what decides the
  bar's dispatch, never the floor preflight or a leg's own script.
- A repository setting that makes the remote job a required check. That is the owner's.

The run-gates kit README's section "Verdict backends — `[[verdict_backend]]`" is the full reference.
