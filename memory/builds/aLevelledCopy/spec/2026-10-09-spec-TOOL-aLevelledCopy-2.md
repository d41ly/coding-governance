# TOOL-aLevelledCopy-2 — check-wiring sets core.sshCommand from push-main's keepalive string

**Status:** OPEN · rev-1 · 2026-10-09 · node a · Tier-2 · base ce9192c0 · streams tooling · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-09-prompt-TOOL-aLevelledCopy-1-1-spec-brief.md](../prompts/2026-10-09-prompt-TOOL-aLevelledCopy-1-1-spec-brief.md) | journal | TOOL-aLevelledCopy-1 TOOL-aLevelledCopy-3 DEPL-aLevelledCopy-1 |
| [2026-10-09-prompt-TOOL-aLevelledCopy-1.md](../prompts/2026-10-09-prompt-TOOL-aLevelledCopy-1.md) | research | TOOL-aLevelledCopy-1 TOOL-aLevelledCopy-3 DEPL-aLevelledCopy-1 |

<!-- /gen:spec-records -->

## 1. Goal

A pre-push gate runs inside `git push` after git has opened the SSH connection, so the socket idles
for the gate's whole duration and the remote drops it. `tools/push-main.sh` defends its own pushes
with an SSH keepalive in `GIT_SSH_COMMAND`; an ordinary branch push gets nothing, which is the
incident inCMS records as DPL-aQuietedFurrow-1. This unit gives every push from a wired tree the
same keepalive, through a repo-local `core.sshCommand` that `check-wiring.sh` sets only when no
scope sets one, with the option string spelled once in `push-main.sh` and derived by the checker.
NicoCares, which pushes over SSH and sets nothing today, then needs no per-node step.

## 2. Scope (IN)

- **S1 — one definition in `push-main.sh`.** The literal on the `GIT_SSH_COMMAND` default line
  becomes a one-line, single-quoted definition, `GOV_SSH_KEEPALIVE='ssh -o ServerAliveInterval=30
  -o ServerAliveCountMax=120 -o TCPKeepAlive=yes'` written on ONE line, followed by
  `: "${GIT_SSH_COMMAND:=$GOV_SSH_KEEPALIVE}"`. The `:=` still keeps a caller's own
  `GIT_SSH_COMMAND`. The comment block above stays accurate and gains one sentence saying the
  wiring checker derives `core.sshCommand` from this line, so the line's shape is a contract.
  Observed by AC8, AC9.
- **S2 — the arm, `check_ssh_keepalive`, called after `check_merge_ours`.** Observed by AC1 to AC7,
  AC10 and AC12.
  1. **Resolve** `push-main.sh` with the rungs every arm uses: `resolve_receipt_path "" push-main.sh`
     first, then the derived `${KIT_REL:+$KIT_REL/}push-main.sh`. Neither present prints
     `skip     ssh       — push-main is not adopted here, so no pre-push bar holds a push open`.
  2. **Derive** the value from the definition line with one anchored `sed`, after a `grep -c` of
     `^GOV_SSH_KEEPALIVE=` that must be exactly 1. Zero or several print `UNWIRED  ssh       —
     cannot derive the keepalive from <path>`, counted. A derivation that found nothing never reads
     as `ok`.
  3. **Remotes.** `git remote`, then `git remote get-url --push --all <r>` per remote, stopping at the
     first ssh-shaped URL; `get-url` applies `insteadOf` and `pushInsteadOf`. SSH-shaped is an
     `ssh://`, `git+ssh://` or `ssh+git://` URL, or the scp form `[user@]host:path` whose host is
     longer than one character and carries no `/`, so `C:/x` reads as a path. None prints
     `skip     ssh       — no remote pushes over ssh`.
  4. **Config states**, read once with `git config --show-scope --get core.sshCommand`, which reads
     EVERY scope. "Only when unset" means unset at any scope: a global operator value carrying an
     identity must not be shadowed by a repo-local one.
     - Unset, under `--fix` or `--session`: `git config core.sshCommand "$want"` at local scope, a
       `FIXED    ssh` line, and one health event (S3). Under `--check`: `UNWIRED  ssh       — … Fix:
       git config core.sshCommand '<want>'`, counted. That is dormant wiring, the class of an unset
       `core.hooksPath`.
     - Equal to the derived value: `ok       ssh       — core.sshCommand carries the keepalive`.
     - Any other value is NEVER overwritten. Carrying `ServerAliveInterval`, it is `ok` and named as
       the operator's. Otherwise it is `note     ssh       — core.sshCommand is the operator's
       (<scope>); NOT overwriting; it carries no keepalive, so a long pre-push bar can lose the
       socket`. That is `note`, not `UNWIRED`, by the header's severity vocabulary: a deliberate
       operator value is not dormant wiring.
- **S3 — the health event.** The set branch calls `add_health_event "$CW_HEALTH_LOG" check-wiring
  sshcommand-set "core.sshCommand -> push-main keepalive · mode $MODE"` exactly as the hookspath arm
  does, resolving `CW_HEALTH_LOG` the same way. The orientation card's counter keys on any
  `source event` pair and is not a closed set (`render_health_cell` in
  `skills/session-kickoff/manifest-check.sh`, read 2026-10-09), so nothing else is extended.
  Observed by AC1.
- **S4 — the header says it.** The usage line's auto-fix list, the health-event sentence, and the
  severity paragraph's `note` sentence each name the new arm. A new sentence states what the arm does
  NOT check: a `GIT_SSH_COMMAND` in someone's environment, which outranks `core.sshCommand`; HTTPS
  remotes; and whether the remote's own idle timeout is shorter than the keepalive's tolerated
  silence. Observed by AC11.
- **S5 — the pair is gated.** `tools/check-wiring.test.sh` gains arms over a fixture holding copies
  of both scripts and a remote `git@example.invalid:o/r.git`; no network is touched and nothing
  pushes. They mirror AC1 to AC8, each with its failing case staged. Observed by AC13.

## 3. Non-goals (OUT)

- **`push-main.sh`'s own precedence.** Its `:=` sets `GIT_SSH_COMMAND` when unset, and the
  environment outranks `core.sshCommand`, so a push-main push drops an identity an operator put in
  `core.sshCommand`. That predates this build, and fixing it changes who wins between two operator
  settings, which is not strictly beneficial. LEFT, as the §3 Edges hand-off.
- **HTTPS remotes.** They hold no SSH socket; gov's own tree pushes over HTTPS, so the arm skips
  there.
- **A third shared file for the option string.** The two scripts are separate kits with
  `requires = []`, and `tools/lib/` ships nothing (§4 Alternatives rejected).
- **The runbook.** `WIRE-INTO-PROJECT.md`'s wiring-health paragraph names what `--session`
  auto-sets. It is the governance template's companion, a carrier M3 veto 2 keeps from a delegated
  run, so its sentence is the §3 Edges hand-off.

### Edges

- **hands-off** external — `push-main.sh` honouring an operator's `core.sshCommand` before setting
  `GIT_SSH_COMMAND`; filed as an ask at the close.
- **hands-off** external — one sentence in `WIRE-INTO-PROJECT.md` naming `core.sshCommand` among
  what `--session` sets when unset; an owner turn, because the runbook is a governance carrier.

## 4. Design

### Why derive, and why this direction

`push-main` ships `.githooks/pre-push`, the gate that idles the socket, so the dependency already
points from the wiring arm to the lander: a tree without `push-main` has no pre-push bar to outlast,
and the arm skips there. Deriving from the lander keeps the lander self-contained, which it must be
because it runs as the push itself. The derivation reads a FILE and never sources it, so nothing in
`push-main.sh` executes during a SessionStart.

### Spawn budget

A git spawn costs about 0.75 s on node a (PINNED, measured 2026-10-02, memory note "A git spawn
costs 751ms"). The arm spends `git remote` plus one `get-url` per remote up to the first ssh one, and
one `git config` read: three spawns for a one-remote tree. The derivation is `grep` and `sed` over one
file. `check-wiring.sh --session` already measured 35 to 81 s per run (the runbook's figure), so the
arm adds about 2 s.

### Inventory

| Identifier | Kind | Cell |
|---|---|---|
| `check_ssh_keepalive` | function in `check-wiring.sh` | `sh.function` |
| `GOV_SSH_KEEPALIVE` | shell variable in `push-main.sh` | UNVERIFIED whether `.lexicon.conf` grades shell variables; checked with `lexicon.py --suggest` at build |
| `sshcommand-set` | health-log event token | `^[a-z][a-z0-9-]*$` (I3) |

`python tools/lexicon/lexicon.py --suggest check_ssh_keepalive --as sh.function` answered OK on
2026-10-09.

### Observed adopter state (read 2026-10-09)

| Adopter | push URL | `core.sshCommand` | the arm will print |
|---|---|---|---|
| inCMS | `git@github.com:d41ly/incms.git` | local, exactly this value, set by the installer being retired | `ok` |
| NicoCares | `git@github.com:d41ly/nc.git` | unset at every scope | `FIXED` under `--session` |
| gov | `https://github.com/d41ly/coding-governance.git` | unset | `skip` |

### Files touched (estimate)

- `tools/push-main.sh`
- `tools/check-wiring.sh`
- `tools/check-wiring.test.sh`

### Rollout

Both kits ship with a normal `govkit update`, and the SessionStart run of `check-wiring.sh
--session` sets the value on each node's next session, so no per-node step is owed. Kit-version
bumps happen once, after the last unit. `TOOL-aLevelledCopy-3` writes `check-wiring.sh` after this
unit lands, which is why it carries `order 2`.

### Alternatives rejected

- **A shared definition file both scripts source.** Rejected: `push-main` and `check-wiring` are
  separate kits with `requires = []`, so a third file would be a new install location for both
  (M3 veto 2), and `tools/lib/` is gov-internal and ships nothing.
- **`push-main.sh` reading the value from `check-wiring.sh`.** Rejected: the lander must not depend
  on the wiring kit, which an adopter may not install, and the pre-push dependency points the other
  way (above).
- **Spelling the string twice and gating equality.** Rejected: derivation makes disagreement
  impossible rather than detected, and AC2 proves the derivation is real.
- **Overwriting a value that carries no keepalive.** Rejected by the owner's prompt: an operator
  value may carry an identity or a proxy.

## 5. Production-readiness checklist

- security — writes one repo-local git config key, only when no scope sets it, to a value read from
  a tracked file of this tree. The value becomes the command git runs for SSH, so its source is the
  trust boundary: it is the same file `core.hooksPath` already trusts, a tracked kit file whose
  receipt row the receipt-sync leg grades. The derivation never sources or evaluates the file.
- perf / scale — about three spawns per SessionStart on a one-remote tree (§4).
- error / empty / loading states — no `push-main`: `skip`. No ssh remote: `skip`. Definition line
  missing or duplicated: `UNWIRED` naming the file. Not a git repo: the script's existing `skip`.
- observability — the `FIXED`, `ok`, `note` and `UNWIRED` lines name the value's scope; the set is
  logged as `sshcommand-set`.
- risks — an adopter whose `push-main.sh` predates S1 has no definition line and reads `UNWIRED`
  until its next update; both kits arrive in the same update, so this window is one partial update.
- testing — S5's arms, each failing case staged.
- migration — none; inCMS already holds the exact value and reads `ok`.
- user docs — `check-wiring.sh`'s header (S4); the runbook sentence is the §3 hand-off.

## 6. Acceptance criteria

Every fixture below is a git repository under a short `%TEMP%` directory, with
`GIT_CONFIG_GLOBAL` pointed at a file of the fixture's own and `GIT_CONFIG_NOSYSTEM=1`, so node a's
own config cannot decide a criterion. It holds copies of `tools/check-wiring.sh` and
`tools/push-main.sh` at the same prefix, and an `origin` whose URL is `git@example.invalid:o/r.git`
unless a criterion says otherwise.

- **AC1** — When `bash tools/check-wiring.sh --session` runs in the fixture with `core.sshCommand`
  unset, `git config --local core.sshCommand` prints exactly the value obtained by running the
  definition line alone in a subshell, the run prints a `FIXED    ssh` line, and the common dir's
  `health.log` gains one `sshcommand-set` line; a second `--session` run prints `ok       ssh` and
  appends nothing. Red when: the value differs by one byte, no event is logged, or the second run
  logs again.
- **AC2** — When the fixture's `push-main.sh` copy has `ServerAliveInterval=30` changed to `31` on
  its definition line and `--session` runs on an unset tree, `git config core.sshCommand` carries
  `ServerAliveInterval=31`. Red when: it carries `30`, which is a second literal rather than a
  derivation.
- **AC3** — When `core.sshCommand` is pre-set to `ssh -i ~/.ssh/id_test`, once at local scope and
  once in the fixture's global file, and `--fix` then `--session` run, `git config --show-scope
  --get-all core.sshCommand` prints exactly the pre-set value at its original scope and nothing else,
  and the run prints a `note     ssh` line naming that scope. Red when: the value changes, or a local
  value appears beside the global one.
- **AC4** — When the pre-set operator value carries `ServerAliveInterval=15`, `--check` prints
  `ok       ssh` naming it the operator's value. Red when: its `ssh` line is `note` or `UNWIRED`.
- **AC5** — When the fixture's only remote is an HTTPS URL on host example.invalid, and again when
  it has no remote, `--session` prints `skip     ssh` and `git config core.sshCommand` prints nothing.
  Red when: a value is set.
- **AC6** — When the definition line is deleted from the fixture's `push-main.sh` copy, and again
  when it is duplicated, `--check` prints `UNWIRED  ssh` naming that file and exits non-zero.
  Red when: either case prints `ok` or `skip`.
- **AC7** — When `--check` runs on an unset ssh fixture, it prints `UNWIRED  ssh` with a `Fix:`
  naming `git config core.sshCommand`, exits non-zero, and `git config core.sshCommand` still prints
  nothing. Red when: it exits 0 or writes the key.
- **AC8** — When `grep -c ServerAliveInterval tools/push-main.sh` runs, it prints 1 and that line
  begins `GOV_SSH_KEEPALIVE=`; `grep -c 'GIT_SSH_COMMAND:=\$GOV_SSH_KEEPALIVE' tools/push-main.sh`
  prints 1; and `grep -c ServerAliveInterval tools/check-wiring.sh` prints 0. Red when: a second
  literal exists in either file.
- **AC9** — When the two lines of S1 are extracted from `tools/push-main.sh` with `sed` and
  evaluated in a subshell with `GIT_SSH_COMMAND` unset, it holds the original three-option string;
  evaluated with `GIT_SSH_COMMAND=ssh -i k` preset, it still holds `ssh -i k`; and `bash -n
  tools/push-main.sh` exits 0. Red when: either value differs.
- **AC10** — When the fixture holds `tools/check-wiring.sh` and no `push-main.sh`, `--session`
  prints `skip     ssh` naming push-main. Red when: it prints `UNWIRED` or sets a value.
- **AC11** — When `grep -n sshcommand-set tools/check-wiring.sh` runs, it hits the header's
  health-event sentence and the arm's call, and the header's auto-fix list names `core.sshCommand`.
  Red when: the arm logs an event the header does not name.
- **AC12** — When `bash tools/check-wiring.sh --check` runs in gov's own worktree, its `ssh` line is
  `skip` naming no ssh remote. Red when: gov's HTTPS tree is reported `UNWIRED`.
- **AC13** — When each new arm of the kit's own self-test is run ALONE, as that suite's prologue
  plus the one block in a sliced copy inside the kit directory, under `bash <slice>`, it prints
  `ok` against the built checker
  and `FAIL` against a scratch copy of the checker carrying that arm's staged break. Red when: an
  arm prints `ok` against its break.
  cost: about 20 s a slice on node a; the whole suite is not run in this pass.

## 7. Gates

`check-wiring self-test` · `push-main self-test` · `transition-audit arms` · `straggler-guard arms` · `lexicon naming predicates` · `install-prefix (shipped surface)` · `memory hygiene`

New arm: tools/check-wiring.test.sh · covers AC1 AC2 AC3 AC4 AC5 AC6 AC7 AC8 AC10 · each arm's break staged in a scratch copy of the checker or of push-main per AC13 · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-09 · initial draft, from the build's spec brief.

## 10. Reuse audit

The seams are in `tools/check-wiring.sh` itself: the hookspath arm's set-when-unset branch in
`check_hooks`, whose `add_health_event` call S3 copies, and `check_merge_rows`'s config tail,
whose never-overwrite reading S2's config states follow. The file is resolved through
`resolve_receipt_path` and `first_of`, as `SMERGE` is. `python tools/codebase-map/reuse_lookup.py
"set a git config value only when unset and log a health event"` ranked `add_health_event` and
`resolve_health_log` as seams, which is what S3 reuses; it found no existing ssh or keepalive seam,
and `git grep ServerAliveInterval` confirms `tools/push-main.sh` holds the only literal.

Recall terms used: GIT_SSH_COMMAND ServerAliveInterval keepalive push-main pre-push SIGPIPE core.sshCommand check-wiring session fix health-log
