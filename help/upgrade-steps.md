# Upgrade steps and retired kits

**What it is.** An upgrade step is a declared, reversible move of something an installed repository
holds — a conf key, a file — to where gov keeps it now. Each step is one `[[upgrade]]` row: in the
descriptor (`kit.toml`) of the kit that owns the surface, or in `tools/govkit/steps.toml` for a
surface no kit owns. The row names three commands, `up`, `down` and `witness`, the `surfaces` it
moves, and whether it runs the target's own code (`needs-target`). The commit that introduced a row
is never written in it: it is the first commit on the default branch's first-parent line that holds
the row, and a row the default branch has not landed reads `unlanded`. A kit that leaves gov gets a
`[[retired]]` row in `tools/govkit/registry.toml` naming its `successor`, another kit, or `none`.

## How to use it

- **See every step, in the order they run:**

  ```sh
  python tools/govkit/upgrade_steps.py list
  ```

  One line per row: its position, its id, its introducing commit (or `unlanded`) and the file that <!-- usage: script:tools/govkit/upgrade_steps.py#list 0be9734d -->
  declares it, then one line per `[[retired]]` row. Rows that landed in the same commit run with
  `steps.toml` first, then each kit in registry order. A malformed row exits 2 naming its file, row
  and key.
- **See which old homes a step still has to empty:** `python tools/govkit/upgrade_steps.py list
  --window` prints each home a step's `surfaces` names, `open` until that step lands, then `closed by
  <step id>`.
- **Correct a landed step:** add a new step under a new id. A landed row is frozen: the
  `step-rows-frozen` leg, `python tools/govkit/upgrade_steps.py frozen`, fails when a branch edits a <!-- usage: script:tools/govkit/upgrade_steps.py#frozen ae4d6ce6 -->
  landed row's `up`, `down`, `witness`, `resume`, `reverted` or `surfaces`, edits a byte of a
  program a landed row runs, or removes a landed row with no `[[retired]]` row naming it. It does
  not check what a step program imports.

## What a step can reach

A step is gov's code run over your repository, so it runs under one contract, whichever command
starts it:

- **From gov's checkout**, never yours: a relative path in a step names gov's file.
- **A clean environment.** Only the names a process needs to start (`PATH`, `SYSTEMROOT`, `LANG`
  and the like) are copied in; everything else, every token and credential variable included, is
  left out. Home and temp point at a fresh scratch directory that is removed after the step.
- **No git config of yours or the machine's, no hooks, no credentials.** Git reads no system or
  global config and never prompts, and three settings passed through `GIT_CONFIG_COUNT`, which
  outrank your repository's own config, point `core.hooksPath` at an empty directory, set
  `credential.helper` to nothing, and set `protocol.ext.allow` to `never`. A step's `git add` or
  `git mv` fires none of your hooks, and a step can never use the `ext::` transport, whose remote
  URL is a command: whatever your `protocol.allow`, `url.<base>.insteadOf` or `remote.<x>.url`
  says, git itself refuses it inside the step with `transport 'ext' not allowed`. Two settings
  follow from gov's side, `core.autocrlf` and `core.eol`, where they are set where `update` runs:
  so a step hashes and stages a file with the line endings `update` itself would.
- **Python runs isolated (`-I`)**: it ignores `PYTHONPATH` and imports nothing from your tree or
  the working directory.
- **Your repository's own config is read first, and can refuse the step.** Git has no switch that
  drops a repository's config, and a step editing your repository needs it, so before every phase
  gov reads it, `include.path` files included, and refuses the step, spawning nothing, when it
  declares a key git runs as a program or sends as a credential. The check reads the config of
  every repository git can enter from yours, each submodule's included: a `git status` in your
  repository runs a submodule's own filters, so every directory under `modules/` in your
  worktree's own git directory, checked out or not, and every checked-out submodule, nested ones
  too, is read the same way, and a refusal names the submodule's path beside the key. The check
  reads the submodules of the target's own worktree: in a linked worktree (`git worktree add`)
  that is `.git/worktrees/<name>/modules/`, never the main worktree's `.git/modules/`, which a step
  run in the linked worktree never enters. The refused keys are the class the check names among
  the keys `git help --config` lists: every key whose name says it runs something (a `program`,
  `command`, `cmd`, `editor`, `path`, `driver`, `helper`, `pager`, a name ending in `hook` and
  the like), and
  gov's self-test re-reads that list on every run, so a key a later git adds fails the test until
  gov classifies it. Among them: `filter.<x>.clean`, `smudge` or `process`,
  `core.fsmonitor` set to anything but false, `diff.external`, `diff.<x>.textconv` or `command`,
  `core.sshCommand`, `core.askPass`, `http.extraheader` or `http.<url>.extraheader` (which
  actions/checkout persists), any `credential.<anything>`, `gpg.program` (run by a signed commit),
  `core.editor`, `sequence.editor`, `core.gitProxy`, `remote.<x>.uploadpack` and `receivepack`,
  `hook.<x>.command`, `gc.recentObjectsHook` (run by `gc` and the auto-gc a commit or fetch
  starts), a `submodule.<x>.update` or `alias.<x>` beginning with `!`, and the trailer,
  difftool, mergetool, browser, man, guitool and send-email commands. Credentials in a value are
  refused too: a `remote.<x>.url`, `remote.<x>.pushurl`, `http.proxy` or `remote.<x>.proxy` that
  is a `<scheme>://` URL carrying a user or password before its host, and any `http.sslKey`,
  `http.sslCert` or `http.cookieFile`, or its `http.<url>.` form. An scp-form remote such as
  `git@host:repo` carries no credential and is not refused. The refusal names each key
  and the file declaring it, and never prints its value. A repository with a filter it relies on, Git LFS's say, in its own
  config or a submodule's, or a local `core.editor` or difftool, has every step refused: remove
  the key for the run, or run the step attended. Nine keys of that shape are not refused: `merge.<driver>.driver`, since a step never
  merges and gov's own checkout declares two; `core.hooksPath`, since the setting gov passes
  outranks it; `core.pager`, since git pages only to a terminal and a step's output is captured;
  `color.pager` and `column.clean`, which run nothing; and `include.path` and
  `includeIf.<condition>.path`, since the files they include are read and graded themselves;
  `advice.ignoredHook`, a switch that runs nothing; and `uploadpack.packObjectsHook`, which git
  honours only from system, global or command-line config, none of which a step sets.

A step that needs your repository's own code or hooks declares `needs-target = true`. The runner
spawns nothing for such a step and reads it `attended`: a person runs it. The `update` walk still
runs its witness, under this same contract, to see whether that person already has. On gov's own
tree, where the target's code is gov's, the runner itself runs such a step's witness, so gov's own
landing passes the step once its witness holds. To check a step's declaration,
gov runs it beside planted hooks and modules in a scratch copy and reads one verdict:

- `isolated` — it ran clean and touched none of your code;
- `needs-target` — it failed and touched none of your code, so it needs it: declare
  `needs-target = true`;
- `breach` — it ran your code anyway, named in the line; fix the step;
- `attended` — it already declares `needs-target = true`, and nothing ran.

To see the contract hold on this machine: <!-- usage: script:tools/govkit/upgrade_steps.py#fixture 8e855cf3 -->

```sh
python tools/govkit/upgrade_steps.py fixture isolation                  # exit 0
python tools/govkit/upgrade_steps.py fixture isolation --plant hook     # hook canary: absent
```

The contract is not a sandbox: a step that opens a path into your tree on purpose is not stopped,
which is what `breach` reports.

## What the receipt records about steps

The receipt, `.governance/install.json`, declares its `schema`. Schema 4 adds `steps`, one row per
step that has run on this repository: its `id`, the commit that `introduced` it (`null` for a step
that ran before its row landed), and its `state`, one of `applied`, `failed` (with the `failure`
text) or `rolled-back` (with none). An `applied` row carries a `failure` only where a rollback's
down stopped on it, and that text opens with `down interrupted:`, `down exit `, `witness still holds
after down` or `reverted check exits `. An `applied` row the walk recorded because the step's witness
already held, its up never run, carries `"via": "witness"`, set only when the receipt held no record
of the step as the walk began and no before-image of it existed; a row with any earlier record, or
with an image on disk, carries none, since either says an up ran. A row whose up ran carries no
`via`, and `via` is legal on no other state. The last `applied` row is the last step completed.
`govkit.py check` reports a malformed `steps` field as a problem naming the row.

A first install, by `apply` or `adopt`, is born at schema 4 with an empty `steps`. An existing
receipt at schema 4 keeps its schema and its `steps` across a re-apply, an `adopt --re-adopt` or an
`update`; one below 4 is never raised past 3 by them, and an existing receipt
reaches 4 only by the step `govkit/receipt-schema-4`, the first row of `steps.toml`. Its up takes
a schema-3 receipt to 4 with an empty `steps` (a receipt below 3 is refused: run `update` first,
which lifts it to 3); its down takes the field out again and refuses while any other step reads
`applied`.

Below schema 4 no step row is persisted: a step's failure or interruption on such a receipt shows
only in `update`'s output and findings. The `govkit/receipt-schema-4` row itself is written once
that step's re-read of the receipt shows schema 4, like any other row. A row is recorded only on a
receipt whose `schema` is a number of 4 or more and whose `steps` is a list; anything else is
refused. Until the deployer runs steps itself, run the step by hand: <!-- usage: script:tools/govkit/steps/receipt_schema_4.py#up 051ba178 --> <!-- usage: script:tools/govkit/steps/receipt_schema_4.py#witness f462d008 --> <!-- usage: script:tools/govkit/steps/receipt_schema_4.py#down a555ef91 -->

```sh
python tools/govkit/steps/receipt_schema_4.py up <repo>       # schema 3 -> 4
python tools/govkit/steps/receipt_schema_4.py witness <repo>  # exit 0 at schema 4
python tools/govkit/steps/receipt_schema_4.py down <repo>     # schema 4 -> 3
```

## What `update` does with steps

`govkit.py update --target <repo> --write` walks the steps after it lands the files and before it
re-renders, so a step meets the new files and the renders meet the moved ones:

- **The order.** Every step row in `--to`'s tree, in the order `list` prints, minus each step the
  receipt's `steps` records `applied`. A step landed after `--to` is not walked.
- **The skip.** Each step's witness runs first. Where it holds, the step is recorded `applied` and
  its up never runs: `step <id> · skipped (witness holds)`. It carries `"via": "witness"` only where
  the receipt held no record of it and no before-image of it exists, so a walk killed after an up
  wrote leaves a re-run that records the row with no `via`.
- **A step that runs** is recorded `failed`, `interrupted: started <utc>, no exit recorded`, before
  its up starts, and `applied` once the up exits 0 and the witness holds. Its writes and its
  before-image under `.governance/steps/` are staged, never committed. The image is written
  whole or not at all. An image cut short by an older writer counts as absent when none of the
  paths it lists changed after it, and is written again. Where one did change, the up stops with
  exit 1 and names the image: its before bytes are gone, so put those paths back by hand and
  remove the image.
- **A stopped walk.** An up that exits non-zero (`exit <rc>: <its last stderr line>`, or a line
  saying it wrote nothing on stderr and giving its last stdout line), or a witness
  that still fails after it (`witness does not hold after up`), stops the walk. The steps before it
  stay applied, no down runs, the run exits 1, and the receipt's `gov_commit` does not move.
- **An attended step** (`needs-target = true`) stops the walk before its up, recorded `failed` with
  `attended: the step needs the target's code`, and writes
  `.governance/outbox/update-attended-step-<slug>.md`, naming the step and the command to run. Run
  it yourself; the next `update --write` skips the step once its witness holds.
- **Read-only, and `--kits`.** Without `--write`, `update` prints `would walk <id>` for each pending
  step and runs none of them, witnesses included. A `--kits` run walks none and prints `steps: not
  walked` with the pending count; the next run without `--kits` walks them.

Every write run prints one line with every count, zeros included:
`govkit update — steps: <n> pending · <a> applied · <s> skipped · stopped at <id|none>`.

**After a kill.** A killed run leaves its write lock, `.governance/outbox/.update.lock`, which names
the holder's pid and host. The next writing run on that host reclaims it by itself once the pid is
gone from the process table, or names a process started after the lock, and prints `reclaimed`. A
lock from another host, one it cannot read, or one it cannot judge because the process census cannot
run is not reclaimed: the refusal names the holder, and you delete the lock by hand once you know
that run has ended. The lock also records the platform it was taken on and, on Linux, the kernel's
boot id; a lock from another platform is not reclaimed either, so a WSL run and a Windows run on one
tree, which share a host name, never take each other's live lock. A lock from this host and platform
whose boot id differs from this kernel's is reclaimed, because the reboot ended its holder; where one
of the two boot ids is missing it is not. Two kernels that share a host name and a tree are judged
one host, so give each its own host name. On Linux it records the
pid namespace too, `pid_ns`, because two WSL distros, or a distro and a Docker Desktop container,
share one kernel boot id; a lock from another pid namespace is not reclaimed, and neither is a lock
with no `pid_ns` judged on Linux, which a govkit older than this one leaves. A lock carrying the
boot clock's start reading is judged against a running pid's boot-clock age; where either boot
reading is missing, a pid that may have been reused is not reclaimed either. Before each index write a run appends the path and the blob it stages to
`.governance/outbox/.update.lock.staged`; the run that reclaims the lock reads that journal, so the
paths the killed run staged are not refused as dirty, while a different blob you staged at one of
them still is. The step the kill interrupted reads `failed` with its `interrupted:` text, and the
next walk runs it again, or runs the row's `resume` command where it declares one. A writing `update`
records the files its file pass moved in the receipt before its first step, with `gov_commit` left
unmoved, so `update --rollback --to <that gov_commit> --write` from a killed run's state returns
those files to the bytes they had. A kit the run held back, because it refused a row of it, is
put back before the first step, so a kill leaves that kit at the bytes it had before the run.

To see it on this machine:

```sh
python tools/govkit/upgrade_steps.py fixture walk                       # s1 to s4 applied, in order
python tools/govkit/upgrade_steps.py fixture walk --plant kill-step     # killed, re-run, converges
python tools/govkit/upgrade_steps.py fixture lock --plant lock-dead     # reclaimed
python tools/govkit/upgrade_steps.py fixture update --plant kill-walk   # update killed mid-step
```

## Rolling back

`update` refuses a `--to` older than the commit the receipt records: a downgrade is not an update.
When you do mean to go back, ask for it by name. A step's down may name that `--to` commit as
`{to}`, which resolves in a rollback's down and nowhere else; a row spelling `{to}` in any other
argv is refused when it is read: <!-- usage: verb:govkit.py:update c276c2e7 -->

```sh
python tools/govkit/govkit.py update --target <repo> --rollback --to <rev>          # preview
python tools/govkit/govkit.py update --target <repo> --rollback --to <rev> --write  # perform
```

- **When.** `<rev>` must be an ancestor of the receipt's `gov_commit`. A receipt with no
  `gov_commit`, a `<rev>` that is not an ancestor, `--rollback` with `--kits`, and a `<rev>` equal to
  the receipt's commit with no step to undo are each refused, naming why. Without `--to`,
  `--rollback` does nothing.
- **What runs, in what order.** Every step introduced after `<rev>` that the receipt records
  `applied` or `failed`, or records nowhere, runs its `down`, newest first, so
  `govkit/receipt-schema-4` comes last. A step recorded nowhere, or `rolled-back`, runs its witness
  first and is skipped where the witness does not hold: `step <id> · skipped (nothing applied)`. A
  step that runs its down is marked `down interrupted: started <utc>, no exit recorded` before it
  starts, where the receipt holds `steps`, and reads `rolled-back` once the down exits 0 and is judged to have taken effect; what
  the down restored is staged. All of this happens before any file moves; then the files return to
  `<rev>`'s bytes as any `update --to <rev>` moves them, and the receipt's `gov_commit` is set to
  `<rev>`, its `schema` left as the downs left it. Without `--write` it prints `would roll back
  <id>` for each step and runs none.
- **How a down is judged.** By default, by the step's witness: it must no longer hold after the
  down. A step with no before-image (`.governance/steps/<entry>/<slug>.before.json`) when its down
  starts that the receipt records `applied` with `"via": "witness"`, or records nowhere, wrote
  nothing to undo, so its down's exit 0 is the verdict instead. A missing before-image does not
  mean the step never ran when its up did run: an image lost after the up (an index discarded
  before the commit, say) leaves that step judged by its witness, and where the witness still holds
  the rollback stops at it with `witness still holds after down; before-image <path> absent`,
  naming the image. Restore the image, or undo the up's writes by hand, then run the rollback
  again. A row whose witness reads something no down
  changes, such as the node's own interpreter, declares `reverted = "down-exit"`, so its down's exit
  0 decides even where an image exists; `lib/python-floor-3.15` does. A row may instead declare
  `reverted` as a command, under the same rules as `up`, `down` and `witness`, whose exit 0 means
  the down took effect. A landed row's `reverted` is frozen, like its `down`.
- **A stopped rollback.** A down that exits non-zero (`down exit <rc>: <its last stderr line>`, or
  a line saying it wrote nothing on stderr and giving its last stdout line), a
  witness that still holds after it (`witness still holds after down`), or a `reverted` command that
  exits non-zero (`reverted check exits <rc>`), stops the rollback with that step's state kept: no
  file moves, `gov_commit` does not move, and the run exits 1. Fix the cause and run the same
  command again; it resumes at that step.
- **After a kill past the schema step.** A rollback killed after `govkit/receipt-schema-4`'s down
  leaves the receipt at schema 3 with no `steps`. Run the same command again: it witness-probes
  every step, runs the down again of each whose witness still holds, records nothing, since the
  receipt has no `steps`, and moves the files and the stamp. Its record names the schema step
  `skipped (nothing applied)`.
- **A failed `update` never rolls back by itself.** A stopped walk leaves the steps before it
  applied and runs no down; only `update --rollback` runs downs.
- **The record.** A `--write` rollback writes `.governance/outbox/update-reverted-<from8>-<to8>.md`
  before its first down, naming both commits and the start, and finishes it before it returns: each
  step's verdict, the file counts, and whether `gov_commit` moved. A rollback killed partway leaves
  the record of what it began, `not finished`.
- **Files gov added after `<rev>`** read as withdrawals, as for any `update`: reported, with an order
  under `.governance/outbox/`, and deleted only under `--write-withdrawals`. A kit the receipt
  gained after `<rev>` stays claimed.
- **Roles.** Each file is graded under the role `<rev>`'s descriptor gives it, not the one your gov
  checkout's working tree gives it, so a file recorded `retired-edited` that `<rev>` still ships
  returns to that role. A kit whose descriptor `<rev>` does not hold keeps the working tree's.

To see it on this machine:

```sh
python tools/govkit/upgrade_steps.py fixture rollback                         # s4 to s1 rolled back
python tools/govkit/upgrade_steps.py fixture rollback --plant down-fails      # stops at s3, resumes
python tools/govkit/upgrade_steps.py fixture rollback --plant witness-only    # no image: judged by the down
python tools/govkit/upgrade_steps.py fixture rollback --plant node-witness    # reverted = "down-exit"
python tools/govkit/upgrade_steps.py fixture rollback-update                  # update --rollback --to A
python tools/govkit/upgrade_steps.py fixture rollback-update --plant schema-step-kill-shipped-rows  # killed past the schema step, resumes
```

## What `update` does with a retired kit

`govkit.py update --target <repo>` reads the target's receipt. A claimed kit that is still a registry
entry is updated as always. One that is not, and has a `[[retired]]` row:

- **with a successor:** prints `retired <old>: claimed by its successor <new>`, classifies the kit's
  files under the successor's descriptor, and with `--write` the receipt claims `<new>` instead of
  `<old>`;
- **with `none`:** prints `retired <old>: released`, and each of its files reads `withdrawn`: with
  `--write` an order lands under `.governance/outbox/`, and nothing is deleted unless you also pass
  `--write-withdrawals`.

A claimed kit with no `[[retired]]` row still stops the whole run, naming the kit, before anything is
written. `govkit.py check` prints `<old>: retired, successor <new>` for a retired claim and counts no
problem for it.

## Where `.agent-cap.conf`'s value lives

The agent limit is the policy key `runtime.agents-in-flight` in `.governance/policy.toml`
([the agent limit](agent-limit.md)). A `FANOUT_CAP=<n>` line in `.agent-cap.conf` only lowers it.
The step `agent-cap/fanout-cap-to-agents-in-flight` moves the line out: its up writes `<n>` into the
key when the line lowers it (and leaves the policy file alone when it does not), then takes every
`FANOUT_CAP` line out of the file. Other lines are kept. Its up removes the file when only blank
lines and comments are left. The limit reads the same before and after. Its down puts both files
back byte-for-byte.
`update --write` runs it as one of its steps; to run it by hand, from this checkout, against a
repository whose `.agent-cap.conf` and policy file are committed: <!-- usage: script:tools/govkit/steps/fanout_cap.py#up 4f94983b --> <!-- usage: script:tools/govkit/steps/fanout_cap.py#witness 052d667f --> <!-- usage: script:tools/govkit/steps/fanout_cap.py#down 3f5f9500 -->

```sh
python tools/govkit/steps/fanout_cap.py up <repo>       # exit 1, writing nothing, on a bad value
python tools/govkit/steps/fanout_cap.py witness <repo>  # exit 0 once no FANOUT_CAP is left
python tools/govkit/steps/fanout_cap.py down <repo>     # exit 1 if a file changed since the up
```

Then commit the result, `.governance/steps/agent-cap/` included: the before-image there is what the
down restores from.

## How gov proves a step before you meet it

Before a step reaches your repository, gov walks it over an install of an older vintage. The
`upgrade-walk` leg builds **release-0**: a scratch clone of gov, made without tags and checked out at
the commit `tools/govkit/fixtures/release-0/pin.txt` pins, runs its own `apply` into a scratch
repository with the kits and answers of the fixture's `deploy.toml`. The adopter edits in
`plants.toml` are committed on top, and the clone then moves to today's tip, so `update` walks every
declared step over that tree the way it would over yours. Every compare reads the tree outside `.git/`
and `.governance/outbox/`, with the index, and reads the receipt's re-measured fields the way the
records that own them declare. Run it from this checkout: <!-- usage: script:tools/govkit/upgrade_walk.py 0cfca8d3 -->

```sh
python tools/govkit/upgrade_walk.py                           # every case, then every arm
python tools/govkit/upgrade_walk.py --list                    # the pin, the steps in walk order, the rows
python tools/govkit/upgrade_walk.py --case kill --step lib/python-floor-3.15
python tools/govkit/upgrade_walk.py --case down --inject lossy-down   # watch a case go red
```

Each case starts from a fresh copy of release-0, and each prints one line per step:

- `up` — every step reads `applied` in the receipt and its witness exits 0 afterwards.
- `down` — after `up`, `update --rollback --to <pin> --write` leaves a tree equal to release-0.
- `reup` — walking up again from that rolled-back tree equals the first walk.
- `plants` — each adopter edit is carried (still there, or read back through the policy reader) or
  ordered (an order under `.governance/outbox/` names it).
- `skip` — each step, passed unrun, changes the outcome: a step that changes nothing is not
  load-bearing. A step that only matters under a condition, like the Python floor under an older
  interpreter, is proven under that condition.
- `kill` — each step's up is killed after its first write, leaving a dead holder's lock; the re-run
  equals `up`, and a rollback from the killed state equals release-0. A step whose witness already
  holds on release-0 is forced into its up, and the line says `forced`.
- `fail` — each step's up fails with exit 1: the walk stops there, every earlier step `applied`, that
  one `failed`, and nothing later recorded.
- `shims` — the tagless clone has no release, so no shim reads closable, and every installed
  forwarder is still in the walked tree; with none declared it prints `shims: 0 declared`.
- `isolation` — each step's up and witness, run beside planted canaries over a scratch copy, reach
  none of your code.

After the cases, the leg injects each defective step or plant of `arms.toml` and expects its case to
go red; one that stays green is a red. Exit 0 is green, 1 a red, and 2 when nothing could be measured:
the pin carries a step row, release-0 does not apply clean, a plant's path is absent at release-0, or
no step is declared. The whole leg takes over an hour, so it is held: it runs on demand and in remote
CI's self-test job, never on every push.
