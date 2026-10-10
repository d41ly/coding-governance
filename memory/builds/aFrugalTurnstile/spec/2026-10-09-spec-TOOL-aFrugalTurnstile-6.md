# TOOL-aFrugalTurnstile-6 — `post-merge.sh` runs the full bar on a landed sha and publishes its verdict as a remote ref

**Status:** CLOSED · rev-2 · 2026-10-09 · node a · Tier-2 · base bef97330 · streams tooling · order 4

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-09-build-TOOL-aFrugalTurnstile-1-1-design.md](../build/2026-10-09-build-TOOL-aFrugalTurnstile-1-1-design.md) | research | TOOL-aFrugalTurnstile-1 TOOL-aFrugalTurnstile-2 TOOL-aFrugalTurnstile-3 TOOL-aFrugalTurnstile-4 TOOL-aFrugalTurnstile-5 TOOL-aFrugalTurnstile-7 TOOL-aFrugalTurnstile-8 TOOL-aFrugalTurnstile-9 TOOL-aFrugalTurnstile-10 PLAY-aFrugalTurnstile-1 DEPL-aFrugalTurnstile-1 |
| [2026-10-09-build-TOOL-aFrugalTurnstile-6-1-acceptance-ledger.md](../build/2026-10-09-build-TOOL-aFrugalTurnstile-6-1-acceptance-ledger.md) | journal | — |
| [2026-10-09-prompt-TOOL-aFrugalTurnstile-1-1-spec-brief.md](../prompts/2026-10-09-prompt-TOOL-aFrugalTurnstile-1-1-spec-brief.md) | journal | TOOL-aFrugalTurnstile-1 TOOL-aFrugalTurnstile-2 TOOL-aFrugalTurnstile-3 TOOL-aFrugalTurnstile-4 TOOL-aFrugalTurnstile-5 TOOL-aFrugalTurnstile-7 TOOL-aFrugalTurnstile-8 TOOL-aFrugalTurnstile-9 TOOL-aFrugalTurnstile-10 PLAY-aFrugalTurnstile-1 DEPL-aFrugalTurnstile-1 |
| [2026-10-09-prompt-TOOL-aFrugalTurnstile-1-2-build-brief.md](../prompts/2026-10-09-prompt-TOOL-aFrugalTurnstile-1-2-build-brief.md) | journal | TOOL-aFrugalTurnstile-1 TOOL-aFrugalTurnstile-2 TOOL-aFrugalTurnstile-3 TOOL-aFrugalTurnstile-4 TOOL-aFrugalTurnstile-5 TOOL-aFrugalTurnstile-7 TOOL-aFrugalTurnstile-8 TOOL-aFrugalTurnstile-9 TOOL-aFrugalTurnstile-10 PLAY-aFrugalTurnstile-1 DEPL-aFrugalTurnstile-1 |
| [2026-10-09-prompt-TOOL-aFrugalTurnstile-1.md](../prompts/2026-10-09-prompt-TOOL-aFrugalTurnstile-1.md) | research | TOOL-aFrugalTurnstile-1 TOOL-aFrugalTurnstile-2 TOOL-aFrugalTurnstile-3 TOOL-aFrugalTurnstile-4 TOOL-aFrugalTurnstile-5 TOOL-aFrugalTurnstile-7 TOOL-aFrugalTurnstile-8 TOOL-aFrugalTurnstile-9 TOOL-aFrugalTurnstile-10 PLAY-aFrugalTurnstile-1 DEPL-aFrugalTurnstile-1 |

<!-- /gen:spec-records -->

## 1. Goal

Implements design D7. A new script in the run-gates kit runs the bar a landed sha declares, with
`GATE_FULL=1`, in a detached scratch worktree, through the host turnstile. It publishes a red as the
remote ref `refs/gov/bar-red`, deletes that ref when a later green descends from it, and keeps a
local copy of the last verdict. It is the after-the-merge half of the scoped-then-full landing path:
the push boundary reads the ref (TOOL-aFrugalTurnstile-7), the lander starts the script
(TOOL-aFrugalTurnstile-8), and an adopter's remote CI may run it instead.

## 2. Scope (IN)

- **S1 — the invocation and its refusals.** `post-merge.sh <sha> [--remote <name>]`. Exit 0 is a
  green whose publication completed, exit 1 is a red or any verdict whose publication failed, and
  exit 2 is a refusal before any bar ran. Exit 2 covers: a missing or extra argument, an unknown
  option, a `<sha>` that is not a commit, no work tree, and a `<sha>` that is not an ancestor of
  `refs/remotes/<remote>/<default>` as the ladder in S2 names them. The last refusal is the
  safety half: a green on an unlanded sha descending from a red would clear the red before the fix
  reached the default branch. Observed by AC7 and AC10.
- **S2 — the remote, by the lander's ladder.** The script carries the `remote_ladder_sh` block from
  `tools/lib/resolve-remote.sh` inline and byte-identical, as every probe asking which ref landed
  does since TOOL-dLadderedRemote-1. `--remote <name>` is passed to that block as `GOV_REMOTE`, so
  an unknown name is the ladder's own refusal. No remote, or a ladder refusal, exits 2 with the
  ladder's `RR_WHY`. No remote name is spelled as a literal. Observed by AC9.
- **S3 — the bar, read at the sha and never sourced.** The script reads `.githooks/gate-env.sh` as
  committed at `<sha>` with its own copy of the hook's `read_policy_key`, and applies three keys:
  `GOV_GATE_CMD`, `GATE_SELFTESTS` and `GOV_PYTHON`.
  - A non-comment line naming `GOV_GATE_CMD` in any other shape, such as `export GOV_GATE_CMD=…`,
    exits 2 naming the line, because the hook would source it and this script would miss it.
  - A declared value whose executing word is not a repo path tracked at `<sha>` exits 2. The word
    rule is the hook's: word 1, or word 2 after `bash` or `sh`, with no option between them.
  - With no declaration the bar is `bash <kit-rel>/run-gates.sh`, the string the hook builds from
    its resolved runner, so the green record names the bar a later push vets. A runner absent at
    `<sha>` exits 2.
  - The environment is scrubbed of every knob listed in §4 "The scrub", and the knobs that were set
    are named on one `post-merge: not honoured from the environment:` line.

  Observed by AC2, AC5 and AC8.
- **S4 — the run.** A detached worktree of `<sha>` is made at `<common-dir>/gate-pm.<pid>` through
  `add_scratch_worktree`, sourced from the kit's own `lib-attribute.sh`. The bar runs with that
  worktree as its cwd as `<own kit dir>/run-gates.sh --hold -- <bar words>`. `GATE_FULL=1` is
  exported, and `GATE_RUN_ID` is pinned to `post-merge-<digits>-<pid>`. The verdict is the hold
  command's exit status, with two corrections.
  - When the bar is the runner, an exit 0 counts GREEN only when the run record the pinned id names
    reads `verdict GREEN`, the hook's envelope from TOOL-dDerivedDocket-26 S6. Otherwise it counts
    RED, and a line says so.
  - When the scratch worktree's HEAD is not `<sha>` after the bar, the verdict is REFUSED and
    nothing is published. This exits 2.

  Observed by AC1, AC2 and AC5. The runner's no-verdict arm is NOT OBSERVED: staging a runner that
  exits 0 without writing its verdict needs `GATE_VERDICT_FAULT`, which S3 scrubs. The hook carries
  the same check, and `.githooks/pre-push.test.sh` arms it there.
- **S5 — the publication.** One bounded `git ls-remote --exit-code <remote> refs/gov/bar-red` reads
  the ref first: rc 0 is present, rc 2 is absent, and anything else fails the publication.
  - RED, ref absent: push `<sha>:refs/gov/bar-red`. RED, ref an ancestor of `<sha>`: advance it to
    `<sha>`. RED, ref equal to `<sha>`: nothing to push. RED, any other ref: keep it.
  - GREEN, ref an ancestor of `<sha>` or equal to it: clear it with a push of the empty source.
    GREEN, no ref: nothing to do.
    GREEN, any other ref: keep it.
  - Every push is `git push --porcelain --force-with-lease=refs/gov/bar-red:<observed sha, empty
    when absent>`, so a ref that moved between the read and the write is a lost race, never an
    overwrite. The porcelain status line decides the outcome, as `write_claim` in
    `tools/unattended/unattended.sh` reads it.
  - Pushes run from the scratch worktree, by remote NAME, before the worktree is cleaned up. The
    tracked hook there sees a non-default ref and exits, or runs a branch bar the repository
    declares; its refusal file sits in the scratch worktree's git dir, so it never touches the
    verdict files the primary tree's lander reads.
  - A ref object missing locally is treated as not an ancestor, so the ref is kept. That is the
    safe direction: a red that is an ancestor of `<sha>` is always present wherever `<sha>` is.

  Observed by AC1, AC2, AC3, AC4 and AC6.
- **S6 — the records.**
  - On GREEN, `<common-dir>/gate-bar-green.shared` is written in design D3's grammar, key for key:
    `sha`, `tree`, `bar`, `bar_paths`, `kind`, `base`, `selftests`, `run_id`, `by`, `stamped`. The
    script fills `by post-merge`, `kind full` and an empty `base`. It is written with a temporary
    file and a rename. RED and REFUSED write none.
  - Always, once the common dir resolves, `<common-dir>/gate-post-merge` is written the same way:
    `sha`, `verdict` (`GREEN`, `RED` or `REFUSED`), `run_id`, `published` (`pushed`, `cleared`,
    `kept`, `none` or `failed`), `why` (empty unless refused or failed), `remote` (the NAME, never a
    URL) and `stamped`.
  - When the bar left a run record in the scratch worktree's git dir, that record is copied to
    `<common-dir>/gate-run/<run_id>/` before the worktree is cleaned up, so a red's leg output survives.

  Observed by AC1, AC2 and AC6.
- **S7 — the cleanup.** An EXIT trap set once the worktree exists takes it down through
  `remove_scratch_worktree`. It names the path on one line when that fails, and the exit status does
  not change. Observed by AC2.
- **S8 — the text.**
  - The script's header states what it does not check, in the sentence §4 gives.
  - The run-gates README gains a row in its pieces table and a section "The post-merge bar", which
    states the exits, the ref's rules, the two records and the remote-CI use.
  - The run-gates dossier gains the script's path under `[paths]`, which is digest-only, and the
    generated map is re-rendered so `symbols.json` carries the new functions.

  Observed by AC11 and AC12.
- **S9 — the arms.** The arms in §7 join `tools/run-gates/run-gates.evidence.test.sh`, whose header
  gains one sentence naming them. NOT OBSERVED in the pass, which runs no suite: the arms run at
  VERIFYING, and AC1 to AC10 observe the same behaviour directly on a scratch fixture.

## 3. Non-goals (OUT)

- Starting the script after a landing (TOOL-aFrugalTurnstile-8).
- Reading the ref at the boundary (TOOL-aFrugalTurnstile-7).
- Remote-CI wiring, which is each adopter's declaration (DEPL-aFrugalTurnstile-1).
- Retrying a failed bar or a failed publication. The exit status and the local record say what
  happened, and the next post-merge run or the next landing acts on it.
- Applying any `gate-env.sh` assignment beyond the three keys in S3.
- A `kit.toml` edit. Its `**` engine rule already ships the new file, and its `{kit}/*.sh` LF pin
  already covers it.
- A kit-version bump. One bump per touched kit happens after the last unit.

### Edges

- **consumes-from** `TOOL-aFrugalTurnstile-5` — the runner's hold verb and the holder nonce it
  exports. Without them S4 cannot run a bar through the host turnstile, and AC5 has nothing to see.
- **consumes-from** `TOOL-aFrugalTurnstile-4` — the lineage reuse that unit adds to the runner, and
  its ruling that this bar runs with `GATE_REUSE` unset so every leg re-executes. S3's scrub carries
  that ruling out, and AC5 observes it. Without the scrub, a lineage verdict carried forward could
  reach the one bar meant to catch it.
- **hands-off** `TOOL-aFrugalTurnstile-7` — reading the published red at the push boundary and
  forcing a full bar until a green descends from it.
- **hands-off** `TOOL-aFrugalTurnstile-8` — starting this script after a landing that succeeded,
  where the landed tip declares it.
- **hands-off** external — a byte-parity row for the copies of the hook's policy-key reader. This
  unit makes a third copy and pins its grammar with a behaviour arm (AC8), not a parity row.

No edge is declared to the two units whose code this script's record serves, the pre-push writer
and reader of design D3 and the unattended writer: no criterion here rests on their code, and S6
pins D3's key list, which both of them pin too. No edge is declared to the runbook unit either. It
sits at order 1, before this unit, so a hands-off to it would run against the declared build order.

## 4. Design

Read at base `bef97330`, whose `.githooks/` and `tools/` are byte-identical to `5a836bf0f`, the
design record's base.

- `.githooks/pre-push` vets its bar with `check_bar_command`, around line 803, and decides the
  default bar as `bash $GATE_RUNNER`, around line 1358. It reads keys at R with
  `read_policy_key`, around line 1095, and the comment there says the unattended driver keeps a
  byte-identical copy.
- `tools/run-gates/lib-attribute.sh` already owns `add_scratch_worktree` and
  `remove_scratch_worktree`. The runner places its own attribution worktree at
  `$gcd/gate-attr.$$`, around line 3481 of `run-gates.sh`. This script places its worktree beside
  that one, under the common dir, where a long scratch path cannot push it past MAX_PATH.
- The runner derives `ROOT` from the cwd, around line 98 of `run-gates.sh`, and derives its kit path
  separately when `KITDIR` lies outside that root, around line 214. Started with the scratch
  worktree as its cwd, this script's own sibling runner therefore takes the scratch worktree as the
  repository top level, and TOOL-aFrugalTurnstile-5's hold verb runs the bar from there. The
  sibling is used rather than the copy at `<sha>`, because a landed sha older than the hold verb
  has none. AC5 observes the cwd.
- The runner stamps `gate-full-green` and, from a linked worktree, copies it to
  `<common-dir>/gate-full-green.shared`, around lines 3878-3908. A runner bar run here therefore also
  leaves the runner's own shared stamp, with no code in this script.
- `write_claim` in `tools/unattended/unattended.sh`, around line 2150, is this repository's one
  compare-and-swap push of a `refs/gov/` ref. It pushes by remote name, leases on the observed sha,
  and reads the porcelain line rather than the exit alone. S5 follows it.
- `observe_remote` in the same file, around line 456, is the kit's bounded network call. It applies
  `timeout -k`, `GIT_TERMINAL_PROMPT=0`, `ssh -o ConnectTimeout -o BatchMode=yes`,
  `credential.interactive=never` and `http.lowSpeed*`, and it captures to a FILE, because a command
  substitution waits on the last inherited write end. `run_remote` below copies that shape and its
  source constants: a 60 s wall, a 20 s ssh connect and 1000 B/s low speed (PINNED, read from
  `unattended.sh` lines 144-149 at base). A host with no working `timeout -k` prints one line saying
  the wall clock is inert, as the driver does.

### Flow

1. Parse the arguments and resolve the work tree, the common dir and the kit's own directory, from
   `$0` and never from a literal prefix. Any failure exits 2.
2. Run the ladder (S2). Resolve `<sha>` to a full commit id. Refuse unless it is an ancestor of
   `refs/remotes/<remote>/<default>` (S1).
3. Read `gate-env.sh` at `<sha>` with `git show`. Resolve and vet the bar (S3). Apply the scrub.
4. Make the scratch worktree and set the cleanup trap (S4, S7).
5. In the worktree, run the bar through the hold verb. Read the verdict and the HEAD check (S4).
6. On GREEN or RED, publish (S5) from the worktree.
7. Write the records and copy the run record (S6). Exit as S1 states, and let the trap remove the
   worktree.

### The scrub

`GIT_DIR` and its family, which the hook also unsets; `GOV_GATE_CMD`, `GOV_GATE_CMD_TEST`,
`GOV_PYTHON` and every `*_PY`, the interpreter knobs the hook drops; `GATE_LEGS`, `GATE_REUSE`,
`GATE_BASE`, `GATE_DOCS_BASE`, `GATE_PUSH_BASE`, `GATE_ATTRIBUTE` and `GATE_INHERITED_RED*`; the arm
seams `GATE_SPAWN_CMD`, `GATE_SPAWN_FLOOR` and `GATE_VERDICT_FAULT`; `GATE_RUN_ID`; and
`GATE_TURNSTILE_HOLDER`, so an inherited nonce can never let this bar skip the queue.
`GATE_SELFTESTS` stays honoured from the environment, since it is the switch an owner sets, and the
declaration at `<sha>` may also turn it on. `GATE_TURNSTILE_DIR` stays honoured: it moves the queue
and never a verdict, and the arms need it to keep the host's real turnstile out of a fixture.

### Messages

Every line starts `post-merge: `. Each is one line per event.

- `post-merge: <sha8> on <remote>/<default> — bar: <bar> — through the host turnstile, GATE_FULL=1`
- `post-merge: GREEN at <sha8> — refs/gov/bar-red <cleared|absent, nothing to do|kept at <ref8>, which is not an ancestor>`
- `post-merge: RED at <sha8> — refs/gov/bar-red <pushed|advanced from <ref8>|already names it|kept at <ref8>, which is not an ancestor> — run record <path>`
- `post-merge: the runner exited 0 and its run record does not read verdict GREEN — treating it as RED`
- `post-merge: publish FAILED — <why>`, where `<why>` is git's porcelain reason, a lost race on
  the lease, the bound firing, or a refusal token the scratch worktree's hook wrote.
- `post-merge: REFUSING — <why>`
- `post-merge: the scratch worktree at <path> could not be removed — remove it by hand`

### The header sentence

> WHAT THIS DOES NOT CHECK: it grades the tree at `<sha>` alone, never the push that landed it; it
> trusts this clone's remote-tracking ref for "landed"; it applies three keys of the gate-env file
> and no other assignment in it; it retries nothing; and two runs racing on the ref are serialised by
> the lease, never ordered by when their shas landed, so a red that finishes after a descendant's
> green is still published and binds until the next green that descends from it.

### Inventory

Function names, each asked of `python tools/lexicon/lexicon.py --suggest <name> --as sh.function`
at writing time, cell `sh.function`. Every one answered OK.

| Name | What it does |
|---|---|
| `check_bar_value` | vets the declared bar's executing word against the tree at `<sha>` |
| `run_remote` | one bounded git network call, captured to a file; rc 124 when the wall fired |
| `read_remote_red` | the ls-remote of the red ref, into the observed sha and a state |
| `write_red_ref` | the leased push that creates or advances the red ref |
| `remove_red_ref` | the leased push that deletes it |
| `run_bar` | the hold-verb run in the worktree, then the envelope and HEAD checks |
| `write_bar_green` | the shared D3 record |
| `write_run_record` | copies the bar's run record into the common dir |
| `write_post_merge_record` | the local verdict record |
| `write_refusal` | prints the `REFUSING` line, writes the local record as `REFUSED`, and exits 2 (rev-2) |

Carried inline and not minted: `resolve_remote_sh`, inside the `remote_ladder_sh` markers;
`derive_self_rel`, inside its markers from `tools/lib/kit-rel.sh`; and `read_policy_key`, the hook's.
Sourced and not copied: `add_scratch_worktree` and `remove_scratch_worktree`.

Also minted: the script itself; the remote ref `refs/gov/bar-red`; the file
`<common-dir>/gate-post-merge`; the scratch path `<common-dir>/gate-pm.<pid>`; and the run-id prefix
`post-merge-`.

### Files touched (estimate)

- `tools/run-gates/post-merge.sh` (new)
- `tools/run-gates/README.md`
- `tools/run-gates/run-gates.evidence.test.sh`
- `memory/map/features/run-gates.md`
- `memory/map/generated/symbols.json`

### Alternatives rejected

- **Publishing through a file in the repository.** A verdict committed to the default branch is a
  landing of its own, and it would pass through the very boundary it is meant to inform. A ref
  carries one sha and no tree.
- **Pushing with `--no-verify`.** The hook stays in the loop, and its run log records the verdict
  push. A branch bar a repository declares then runs over a push that carries no tree, which costs
  its time, and a refusal by it is reported as a failed publication. The precedent is `write_claim`,
  which pushes the same way.
- **Writing the common dir's own `gate-bar-green`.** A linked worktree's boundary reads its own git
  dir and then the shared copy, so a record in the primary's own slot is invisible to it. It could
  also displace a fresher record the primary tree wrote.
- **A fresh suite and leg for the arms.** A new leg owes a ceiling, a budget row, a `kit.toml`
  withholding and the foreign-prefix parity, the class `a-new-leg-trips-a-growing-set-of-meta-gates`.
  The evidence suite already drives the runner in scratch repos through `GATE_LEGS`.
- **The pre-landing post-merge run that `PLAY-aPrunedCeremony-1` retired.** That was a full bar
  BEFORE the push, a second bar over one integration. This one runs AFTER the push, in place of the
  boundary's full bar, so each landing pays one full bar.

## 5. Production-readiness checklist

- security — It pushes only `refs/gov/bar-red`, by lease, and never a branch. The bar and its python
  come from the committed tree at a landed sha, never from the environment. The URL is never printed
  or written. The landed-sha refusal stops an unlanded green from deleting a binding red.
- perf / scale — One full bar per landing, queued behind any other bar on the host. Two network
  calls at most, each bounded. The runner bar's cost is the bar's own.
- error / empty / loading states — Every exit writes the local record once the common dir resolves.
  A failed publication is exit 1 and names its reason. A worktree that cannot be removed is named.
- observability — One `post-merge:` line per event, the runner's run-log line under the common dir,
  the copied run record, and the hook's run-log line for the verdict push.
- risks — The third copy of the policy-key reader can drift from the hook's. AC8 pins the grammar
  on the forms gate-env files carry, and §3 Edges hands the parity row on. A branch bar declared by an
  adopter runs on every verdict push.
- testing — The arms in §7, staged in scratch repos under a short temp root, with the turnstile
  directory moved into the fixture.
- migration — None. A clone that never runs the script has no ref, and the boundary reads nothing
  unless a declaration asks it to.
- user docs — The README section in S8. The adopter declaration belongs to DEPL-aFrugalTurnstile-1.

## 6. Acceptance criteria

Every criterion runs on one scratch fixture under a short root in `%TEMP%`, never under the session
scratchpad, which is too long for a clone. The fixture holds a bare repository as the remote and a
clone. The clone carries the run-gates kit copied under `tools/run-gates/`, with the hold verb, and a
one-leg manifest whose leg reads `grep -qx green verdict.txt`. It also carries `GATE_TURNSTILE_DIR`
pointing into the fixture. Commits are pushed to the remote's `main` with a plain `git push`, and
the clone wires no hook. Before the script exists, the old behaviour is observed by
`git ls-remote <bare> refs/gov/bar-red`: a red landing leaves no ref, because nothing publishes one.

- **AC1** — When `post-merge.sh <c2>` runs on a landed commit whose `verdict.txt` reads `red`, it
  exits 1. `git ls-remote <bare> refs/gov/bar-red` then prints `<c2>`, and the local record reads
  `verdict RED` and `published pushed`. `<common-dir>/gate-run/<run_id>/` holds the failing leg's
  output after `git worktree list` no longer names the scratch tree. Red when: no ref appears, which
  is the base behaviour, or the run record went with the worktree.
  cost: one runner bar in the fixture, measured in tens of seconds on node a.
- **AC2** — When `post-merge.sh <c3>` runs on a green descendant of `<c2>`, it exits 0 and
  `git ls-remote --exit-code <bare> refs/gov/bar-red` exits 2. `gate-bar-green.shared` in the common
  dir carries exactly the keys `sha tree bar bar_paths kind base selftests run_id by stamped`, with
  `kind full` and `by post-merge`. Its `bar` value is the default-bar string S3 states, which names
  the kit runner by its repo-relative path. The runner's
  `gate-full-green.shared` is present, and `git worktree list` names no `gate-pm.` tree. Red when:
  the ref survives, the key set differs from D3's, or the worktree is left behind.
- **AC3** — When the ref is staged at `<c2>` with `git push <bare> <c2>:refs/gov/bar-red`, and
  `post-merge.sh <c1>` runs on `<c2>`'s green parent, it exits 0. The ref still names `<c2>` and the
  record reads `published kept`. Red when: a green that does not descend from the red deletes it.
- **AC4** — When the ref is staged at `<c3>` and `post-merge.sh <c2>` runs red, the ref still names
  `<c3>`, the record reads `published kept`, and the exit is 1. Red when: the ref moves backwards to
  `<c2>`.
- **AC5** — When `.githooks/gate-env.sh` at the sha declares `GOV_GATE_CMD="bash bar.sh"`, a tracked
  script that writes its environment, `git rev-parse HEAD` and `pwd` to a probe file, the probe reads
  `GATE_FULL` as 1, a non-empty `GATE_TURNSTILE_HOLDER`, no `GATE_REUSE` even when the caller
  exported `GATE_REUSE=lineage`, HEAD equal to the sha, and a cwd under the common dir's `gate-pm.`
  path. The record's `bar` reads `bash bar.sh`. Red when: the bar ran outside the hold verb, so the
  holder is empty, ran with `GATE_FULL` unset, or inherited `GATE_REUSE`.
- **AC6** — When the bare repository carries a `pre-receive` hook rejecting `refs/gov/*` and a red
  runs, the script exits 1 and prints `post-merge: publish FAILED` naming the rejection. The local
  record still exists, with `published failed` and a non-empty `why`. Red when: the script exits 0
  or leaves no record.
- **AC7** — When `post-merge.sh` names a commit that exists only on a local feature branch, it exits
  2 with `post-merge: REFUSING`. No probe file is written, so no bar ran, and the remote gains no
  ref. Red when: a bar runs or a ref is pushed.
- **AC8** — When `gate-env.sh` at the sha carries `export GOV_GATE_CMD="bash bar.sh"`, the script
  exits 2 naming that line, and no bar runs. When it carries the hook's accepted forms instead, the
  bar is `bash bar.sh` each time: double quotes, single quotes, a trailing comment, a CRLF line end,
  and a later assignment overriding an earlier one. Red when: the export form runs the default
  runner, or any accepted form resolves to another value.
- **AC9** — When the clone has two remotes, a detached HEAD and no `GOV_REMOTE`, the script exits 2
  naming `GOV_REMOTE`. With `--remote <second>`, the ref lands on the second remote, and
  `git ls-remote` of the first shows none. Red when: the script picks a remote nobody named.
- **AC10** — When `post-merge.sh` runs with no argument, or with a `<sha>` that names no commit, it
  exits 2 and prints a usage line. Red when: it exits 0 or 1, or runs a bar.
- **AC11** — When `grep -n 'WHAT THIS DOES NOT CHECK' post-merge.sh` and
  `grep -n '^## The post-merge bar' README.md` run in the kit directory, each prints one line.
  Red when: either is absent.
- **AC12** — When `python tools/codebase-map/gen_map.py --check` runs after the symbols regeneration,
  it exits 0, and `grep -c post-merge.sh memory/map/generated/symbols.json` is non-zero. Red when:
  the map is stale, which the memory note on new shell functions predicts.

## 7. Gates

`run-gates evidence` · `run-gates turnstile` · `run-gates canary` · `run-gates gov canary` · `run-gates run-log line` · `run-gates adopter e2e` · `profile-bar selftest` · `pre-push run-log line` · `push-main self-test` · `python resolver (behaviour + inline parity + idiom ban)` · `check-wiring self-test` · `settings-merge selftest` · `foreign-prefix parity (every self-test at three prefixes)` · `install-prefix self-test` · `dead-path carriers self-test` · `lexicon naming predicates` · `spec-tokens self-test` · `kit-placeholders self-test` · `recall floor` · `recall floor arms` · `install-prefix (shipped surface)` · `dead-path carriers (deleted files still named)` · `remote literals (kit code names no remote)` · `codebase-map coverage + freshness` · `shell hygiene (a loop fed by a command substitution)` · `shell hygiene (a location probe asked from a moved directory)` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

The close runs these. A pass runs none of them. The python resolver leg is where the inline
`remote_ladder_sh` and `derive_self_rel` copies are compared byte for byte.

New arm: tools/run-gates/run-gates.evidence.test.sh · covers AC1 AC2 AC3 AC4 AC5 AC6 AC7 AC8 AC9 AC10 · a bare remote and a clone with a one-leg manifest, a red commit, a green descendant, staged refs, a rejecting pre-receive hook, an export-form declaration and a second remote · the suite's ceiling in tools/gate-legs.json and its row in selftest-budgets.txt, if the measured wall breaches them

## 8. Open questions

- **F1 — where do the arms live?** A fresh suite with its own leg, or the run-gates evidence suite.
  The fresh suite reads more cleanly but owes a leg's whole set of meta-gates. The evidence suite
  already builds scratch repos that drive the runner. Recommendation: the evidence suite, with one
  header sentence naming the new arms.
  RESOLVED (agent, 2026-10-09, delegated): the evidence suite. It is the option with the fewest open
  follow-ups and adds no leg, and §4 records the rejected one.
- **F2 — which file holds post-merge's green record?** The common dir's own `gate-bar-green`, or the
  shared copy. The boundary in a linked worktree reads its own git dir and then the shared copy, so
  only the shared copy is visible from every tree. Recommendation: the shared copy.
  RESOLVED (agent, 2026-10-09, delegated): `<common-dir>/gate-bar-green.shared`. The brief's "into
  the common dir" is satisfied, and the primary tree's own record is never displaced.

## 9. Revision log

- rev-1 · 2026-10-09 · initial draft, from design D7 and the spec brief.
- rev-2 · 2026-10-10 · §4 Inventory: `write_refusal` added. What disagreed: S1 names five exit-2
  refusals and S3, S4 and the flow add more, each owing the same three acts (the `REFUSING` line,
  the `REFUSED` record, exit 2), and spelling them inline at every site is the two-answers class.
  Asked of the lexicon, cell `sh.function`: OK.

## 10. Reuse audit

The seams are reused and none is re-implemented. `add_scratch_worktree` and
`remove_scratch_worktree` come from `tools/run-gates/lib-attribute.sh`: `reuse_lookup.py` ranked both
for the phrase "run the full bar on a landed commit in a detached scratch worktree and publish its
verdict to the remote". The `remote_ladder_sh` block is carried from `tools/lib/resolve-remote.sh`,
which `tools/lib/resolve-python.test.sh` parity-gates. The bounded-call shape comes from
`observe_remote` and the leased push from `write_claim`, both in `tools/unattended/unattended.sh`.
The probe did not rank either of those two, because it ranks by name and neither name says "bounded"
or "lease". They were found by reading, and the recall corpus confirms them through
`TOOL-aGraftedHelix-1`'s evidence section. `read_policy_key` is copied from `.githooks/pre-push`,
because the hook ships verbatim and sources no kit. No existing seam fits the publication itself.
`refs/gov/runs/<slug>` is the only other `refs/gov/` ref, and it is a claim record, not a verdict.
The recall hits that bind this unit are the design record D7, `TOOL-aSurfacedLexicon-25`, which is a
push that ran no bar while the hook said FULL, and `PLAY-aPrunedCeremony-1`, the retired
pre-landing run that §4 distinguishes.

Recall terms used: `python tools/memory-recall/query.py "how is a full bar run after a landing and its red recorded so the next push is blocked" --terms "post-merge full bar red ref remote scratch worktree landed sha publish verdict binding push boundary"`
