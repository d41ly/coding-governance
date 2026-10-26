# TOOL-dWellOiledMachine-39 — every act's minimal binding record pushed to `refs/gov/bindings`, and one reader over `<current default>..HEAD` that never passes a binding it cannot find

**Status:** OPEN · rev-1 · 2026-10-26 · node a · Tier-2 · base 0689e7fa · streams tooling · order 16 · advances TOOL-dWellOiledMachine-62

**Carries:** cl-dClosedLoop-0317@9d62f0b1 whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dWellOiledMachine-1-reuse-scout-a.md](../build/2026-10-26-build-TOOL-dWellOiledMachine-1-reuse-scout-a.md) | research | TOOL-dWellOiledMachine-1 TOOL-dWellOiledMachine-6 TOOL-dWellOiledMachine-7 TOOL-dWellOiledMachine-8 TOOL-dWellOiledMachine-9 TOOL-dWellOiledMachine-19 TOOL-dWellOiledMachine-25 TOOL-dWellOiledMachine-30 TOOL-dWellOiledMachine-32 TOOL-dWellOiledMachine-36 TOOL-dWellOiledMachine-37 TOOL-dWellOiledMachine-43 TOOL-dWellOiledMachine-45 TOOL-dWellOiledMachine-46 TOOL-dWellOiledMachine-47 TOOL-dWellOiledMachine-49 TOOL-dWellOiledMachine-53 TOOL-dWellOiledMachine-56 |
| [2026-10-26-build-TOOL-dWellOiledMachine-1-spec-stage-returns.md](../build/2026-10-26-build-TOOL-dWellOiledMachine-1-spec-stage-returns.md) | journal | TOOL-dWellOiledMachine-1 TOOL-dWellOiledMachine-2 TOOL-dWellOiledMachine-6 TOOL-dWellOiledMachine-10 TOOL-dWellOiledMachine-11 TOOL-dWellOiledMachine-12 TOOL-dWellOiledMachine-13 TOOL-dWellOiledMachine-14 TOOL-dWellOiledMachine-15 TOOL-dWellOiledMachine-16 TOOL-dWellOiledMachine-17 TOOL-dWellOiledMachine-20 TOOL-dWellOiledMachine-21 TOOL-dWellOiledMachine-22 TOOL-dWellOiledMachine-23 TOOL-dWellOiledMachine-31 TOOL-dWellOiledMachine-32 TOOL-dWellOiledMachine-33 TOOL-dWellOiledMachine-35 TOOL-dWellOiledMachine-36 TOOL-dWellOiledMachine-37 TOOL-dWellOiledMachine-38 TOOL-dWellOiledMachine-40 TOOL-dWellOiledMachine-55 TOOL-dWellOiledMachine-56 TOOL-dWellOiledMachine-57 TOOL-dWellOiledMachine-58 TOOL-dWellOiledMachine-60 TOOL-dWellOiledMachine-61 |
| [2026-10-26-prompt-TOOL-dWellOiledMachine-1-spec-brief.md](../prompts/2026-10-26-prompt-TOOL-dWellOiledMachine-1-spec-brief.md) | research | TOOL-dWellOiledMachine-1 TOOL-dWellOiledMachine-2 TOOL-dWellOiledMachine-3 TOOL-dWellOiledMachine-4 TOOL-dWellOiledMachine-5 TOOL-dWellOiledMachine-6 TOOL-dWellOiledMachine-7 TOOL-dWellOiledMachine-8 TOOL-dWellOiledMachine-9 TOOL-dWellOiledMachine-10 TOOL-dWellOiledMachine-11 TOOL-dWellOiledMachine-12 TOOL-dWellOiledMachine-13 TOOL-dWellOiledMachine-14 TOOL-dWellOiledMachine-15 TOOL-dWellOiledMachine-16 TOOL-dWellOiledMachine-17 TOOL-dWellOiledMachine-18 TOOL-dWellOiledMachine-19 TOOL-dWellOiledMachine-20 TOOL-dWellOiledMachine-21 TOOL-dWellOiledMachine-22 TOOL-dWellOiledMachine-23 TOOL-dWellOiledMachine-24 TOOL-dWellOiledMachine-25 TOOL-dWellOiledMachine-26 TOOL-dWellOiledMachine-27 TOOL-dWellOiledMachine-28 TOOL-dWellOiledMachine-29 TOOL-dWellOiledMachine-30 TOOL-dWellOiledMachine-31 TOOL-dWellOiledMachine-32 TOOL-dWellOiledMachine-33 TOOL-dWellOiledMachine-34 TOOL-dWellOiledMachine-35 TOOL-dWellOiledMachine-36 TOOL-dWellOiledMachine-37 TOOL-dWellOiledMachine-38 TOOL-dWellOiledMachine-40 TOOL-dWellOiledMachine-41 TOOL-dWellOiledMachine-42 TOOL-dWellOiledMachine-43 TOOL-dWellOiledMachine-44 TOOL-dWellOiledMachine-45 TOOL-dWellOiledMachine-46 TOOL-dWellOiledMachine-47 TOOL-dWellOiledMachine-48 TOOL-dWellOiledMachine-49 TOOL-dWellOiledMachine-50 TOOL-dWellOiledMachine-51 TOOL-dWellOiledMachine-52 TOOL-dWellOiledMachine-53 TOOL-dWellOiledMachine-54 TOOL-dWellOiledMachine-55 TOOL-dWellOiledMachine-56 TOOL-dWellOiledMachine-57 TOOL-dWellOiledMachine-58 TOOL-dWellOiledMachine-59 TOOL-dWellOiledMachine-60 TOOL-dWellOiledMachine-61 |

<!-- /gen:spec-records -->

## 1. Goal

The commit-key leg, the causes check, Maintain's commit reading and the landing's `carries` read act
bindings that today would live on one node only (SA-10). Each act publishes a minimal binding record
(act id, epoch, node, task sha and, under `salted`, its digest) to `refs/gov/bindings`, and one reader
grades the act-made commits of `<current default>..HEAD` read with `--no-merges`: a binding missing
locally is read from the ref, and one the ref lacks is counted `not-local` and never passed.

## 2. Scope (IN)

- **S1** — The record and its ref (I16). `write_binding <act> <epoch> <node> <task-sha> [<digest>]` in
  the new `tools/runtime/bindings.sh` builds the commit through `build_gov_commit "" <message>` and
  writes it through `write_gov_ref refs/gov/bindings/<act> "" <commit>` (TOOL-dPlacedRequest-11 S1, S2),
  so each binding is one parentless commit over the empty tree under the fixed `gov-claim` identity.
  The message is `gov-binding <act>`, a blank line, then `act:`, `epoch:`, `node:`, `task-sha:` and,
  only under `salted`, `digest:`, one `key: value` line each. rc 0 written, 1 lost, 2 not completed with
  `GOVREF_WHY`; the expected tip is always empty, so a second write for one act is lost and a written
  binding never changes. It is the one function that writes a ref under `refs/gov/bindings`.
  Observed by AC1 and AC2.
- **S2** — Validation at the write boundary. `act` matches I15's `act-<12 hex>` (TOOL-dWellOiledMachine-32),
  `epoch` is a positive integer, `node` a fleet tag (`[a-z0-9][a-z0-9-]*`), `task-sha` 12 to 64 lowercase
  hex. `digest` is 64 lowercase hex, required when `trace.identity` resolves `salted` through
  `policy-shim.sh get trace.identity` (I31) and refused under any other value. A refused field exits 2
  before any commit is built, naming the field. Observed by AC2.
- **S3** — The act's committer identity. `derive_act_identity <act>` in the same file prints the two
  lines `GIT_COMMITTER_NAME=gov-act` and `GIT_COMMITTER_EMAIL=<act>@gov-act.invalid`, the identity an act
  session is launched with and every act-made commit is committed under, its author untouched.
  Observed by AC3.
- **S4** — The range. `derive_act_range(repo, default_tip=None)` in the new `tools/runtime/bindings.py`
  returns `<tip>..HEAD`, `<tip>` the commit `refs/remotes/<remote>/<branch>` names as this clone holds it,
  the remote and branch from the inline `remote_ladder_py` block (`tools/lib/resolve_remote.py:17`).
  A caller that has just read the remote's tip passes it as `default_tip`; nothing reads a base from a
  record, a conf or an environment value, so no frozen base exists to pass. No tracking ref and no
  `default_tip` is a refusal naming the ref, exit 2. Every read over the range carries `--no-merges`.
  Observed by AC4 and AC5.
- **S5** — The act-made commits. `read_act_commits(repo, rng)` reads the `Gov-Act` trailer of every
  commit in the range through `read_commits(repo, ["--no-merges", rng], ("Gov-Act",))`
  (TOOL-dDeclaredLoop-23 S3), and each commit's committer email by one `git log --no-merges --format`
  read over the same range. A commit is act-made when either mark is present; the two marks must name
  the same act, else the commit is `unmarked`. Observed by AC6.
- **S6** — The reader. `read_binding(repo, act)` returns the binding's fields and where they came from:
  `local` when `refs/gov/bindings/<act>` resolves in this clone, `ref` after one bounded fetch of
  `+refs/gov/bindings/*:refs/gov/bindings/*` from the ladder's remote, made once per run and only when
  some binding is missing locally, and `not-local` when the ref lacks it too. A binding commit whose
  message does not parse under S1's grammar reads `malformed`. Observed by AC4, AC5 and AC7.
- **S7** — The check, `python tools/runtime/bindings.py --check [--repo <dir>] [--default-tip <sha>]`.
  It prints `range — <remote>/<branch>@<sha8>..HEAD · --no-merges · <n> commit(s) · <m> act-made`,
  then one `act — <sha8> · <verdict> · <act or value>` line per act-made commit, the verdict one of
  `bound local`, `bound ref`, `not-local`, `no act`, `unmarked` and `malformed`, then
  `bindings — <k> bound · <j> not-local · <r> red`. `no act` is a `Gov-Act:` value that is empty or not
  act-id shaped. Exit 0 only when `j` and `r` are both 0, exit 1 otherwise, exit 2 on a refusal.
  `--read <act>` prints S6's answer for one act. Observed by AC4 to AC8.
- **S8** — The landing's `carries`. `tools/push-main.sh` gains `check_carry_bindings <R>`, called right
  after each of the two `check_carry_set "$R"` calls (`cmd_land` :962, `cmd_carry` :1022), which runs
  S7's check with `--default-tip "$R"`, the tip `resolve_tip` has just read, through the inline python
  resolver, and refuses the landing (`exit 1`) on any exit but 0, printing the check's lines.
  Observed by AC8.
- **S9** — The kit carries what it reads inline. `bindings.sh` carries the `gov_ref_sh` block and
  `bindings.py` carries the `remote_ladder_py` and `commit_trailers_py` blocks, each byte-identical, each
  a row of `PARITY_ROWS` in `tools/lib/resolve-python.test.sh`; `tools/runtime/kit.toml` (I1) lists both
  files. Observed by AC9.
- **S10** — The fixture and its leg. `python tools/runtime/bindings.py --fixture --plant <case>` builds
  a bare remote and its clones under `%TEMP%` with short names and prints the case's observation, exit 0
  when it holds; the leg `runtime bindings fixtures` in `tools/gate-legs.json` runs every case.
  Observed by AC1 to AC8.

## 3. Non-goals (OUT)

- Minting the act and its record: TOOL-dWellOiledMachine-32's `gov_record.py new act`. This unit
  publishes a subset of that record and invents no field of it.
- Deriving the salted digest and the per-node salt: TOOL-dWellOiledMachine-33's, under `trace.identity`.
  This unit validates the digest's shape and refuses `salted` without one.
- Calling `write_binding` at each act's launch and launching the act session under S3's identity:
  TOOL-dWellOiledMachine-6, the supervisor, which writes acts and pushes their bindings
  (memory plan `[doors]`).
- The commit-key leg itself and the `Gov-Act:` writers: TOOL-dWellOiledMachine-33. The leg calls S7.
- The causes check's read (TOOL-dTotalRecall-19 S8): an ask for dTotalRecall, §8 F4. Maintain's commit
  reading: dTendedCadence's, a child build.
- The act binding at a spawn (PermissionRequest): TOOL-dWellOiledMachine-7. The session node:
  TOOL-dWellOiledMachine-35.
- Pruning `refs/gov/bindings`: nothing prunes it in this build; a binding is a few hundred bytes.

### Edges

- **consumes-from** `TOOL-dWellOiledMachine-32` — the `act` id grammar `act-<12 hex>` and the act record's `epoch`, `node` and `task-sha` the binding publishes; without them S2 has nothing to validate against
- **hands-off** `TOOL-dWellOiledMachine-33` — the commit-key leg reads `refs/gov/bindings` through `bindings.py --check`, and the `salted` digest value S2 validates
- **hands-off** `TOOL-dWellOiledMachine-7` — the epoch check at the PermissionRequest entry reads an act's binding from `refs/gov/bindings` through `read_binding`
- **hands-off** `TOOL-dWellOiledMachine-35` — the session node joins acts read from `refs/gov/bindings`
- **hands-off** `TOOL-dWellOiledMachine-11` — `derive_act_identity`, the committer identity the commit queue commits every act-made commit under
- **hands-off** `TOOL-dWellOiledMachine-6` — the supervisor calls `write_binding` at each act's launch and launches the act session with `derive_act_identity`'s committer identity
- **consumes-from** external — `write_gov_ref` and `build_gov_commit` (TOOL-dPlacedRequest-11 S1, S2) and `read_commits` (TOOL-dDeclaredLoop-23 S3), parent mechanisms built before this build's build run
- **hands-off** external — Maintain's commit reading, dTendedCadence's, reads act-made commits through `bindings.py --check`

## 4. Design

### Evidence

The one gov-ref writer at this base is `write_claim` (`tools/unattended/unattended.sh:2396`): a
parentless commit over the empty tree under the `gov-claim` identity, pushed with
`--force-with-lease=<ref>:<expected>`. TOOL-dPlacedRequest-11 S1 and S2 extract it as `write_gov_ref`
and `build_gov_commit`; this unit is their third caller and adds no copy. No reader of a binding,
of `Gov-Act:` or of a committer identity exists at this base (`git grep -n "refs/gov/bindings\|Gov-Act" --
tools .githooks skills` prints nothing). The `Gov-Act` trailer key is already a row of
PLAY-dOrderedCharter-28's `[[trailer]]` table, which TOOL-dDeclaredLoop-23 S2 asserts, so `read_commits`
reads it unregistered by this unit. The landing's range is already a current one: `cmd_land` and
`cmd_carry` resolve `R` with `resolve_tip` on every call (`tools/push-main.sh:955`, `:1013`) and grade
`R..HEAD` through `check_carry_set` (`:603`).

### The record

```
gov-binding act-3f9c0a1b2d4e

act: act-3f9c0a1b2d4e
epoch: 7
node: a
task-sha: 9b1c44e0a2f7
digest: <64 hex, present only under salted>
```

The order is fixed and the parser refuses a repeated, unknown or missing key. The binding never holds a
session id, a host name or a path: under `session` the session joins through the act record
(TOOL-dWellOiledMachine-32) on the node that holds it, and under `salted` only the digest travels.

### The verdicts

| Verdict | When | Counted as |
|---|---|---|
| `bound local` | the binding resolves in this clone | bound |
| `bound ref` | it resolved only after the one fetch | bound |
| `not-local` | well-formed act id, no binding here or on the remote | `not-local`, never passed |
| `no act` | `Gov-Act:` empty or not act-id shaped | red |
| `unmarked` | one mark missing, or trailer and committer name two acts | red |
| `malformed` | the binding commit's message fails S1's grammar | red |

A commit carrying neither mark is not act-made and is not graded: an owner's own commit is legal.

### Why the range is safe on a merge of main

`<current default>..HEAD` excludes every commit the default branch already holds, so a branch that merged
main carries none of main's act commits into the range, and `--no-merges` drops the merge commit itself.
A reader with a frozen base would include the act commits main gained after that base, whose bindings
another node may never have pushed; the `merge-main` plant has exactly such commits and is green only
under the current range.

### Inventory

| Identifier | Kind | Where |
|---|---|---|
| `refs/gov/bindings/<act>` | git ref namespace | the remote and every clone |
| `write_binding`, `derive_act_identity` | shell functions | `tools/runtime/bindings.sh` |
| `derive_act_range`, `read_act_commits`, `read_binding`, `check_bindings` | python functions | `tools/runtime/bindings.py` |
| `check_carry_bindings` | shell function | `tools/push-main.sh` |
| `gov-act`, `<act>@gov-act.invalid` | committer identity | S3 |
| `runtime bindings fixtures` | gate leg | `tools/gate-legs.json` |

### Files touched (estimate)

- `tools/runtime/bindings.sh` (new)
- `tools/runtime/bindings.py` (new)
- `tools/runtime/kit.toml` (the two files listed)
- `tools/push-main.sh`
- `tools/push-main.test.sh`
- `tools/lib/resolve-python.test.sh`
- `tools/gate-legs.json`

### Alternatives rejected

- **The binding in a tracked record file.** A file rides a branch, so another node reads it only after
  the branch lands, which is the gap SA-10 names; a ref is readable the moment it is pushed.
- **One ref per node holding every binding.** Two acts of one node would contend on one compare-and-swap
  chain; one ref per act never contends and needs no lock.
- **A base read from the run-state file or `GATE_PUSH_BASE`.** That is the frozen base the clause
  forbids; the push leg's base is the push's own old tip, not the default branch.

## 5. Production-readiness checklist

- security — a new write surface on the shared remote, written only through `write_gov_ref`; every
  field validated at the write; no session id, host or path published; the digest only under `salted`.
- perf / scale — one push per act; a check makes two `git log` reads over the range and at most one
  bounded fetch of the namespace.
- error / empty / loading states — no tracking ref is a refusal, exit 2; an unreachable remote leaves
  every missing binding `not-local`, which never passes; an empty range prints `0 act-made`, exit 0.
- observability — one `range —` line, one `act —` line per act-made commit and one `bindings —` total.
- risks — the population is empty until TOOL-dWellOiledMachine-33 and -6 write act-made commits, so a
  green check before then grades nothing, and its `0 act-made` says so.
- testing — the fixture plants under AC1 to AC8, the parity rows of AC9 and the arms in §7.
- migration — none: the namespace and the identity are new.
- user docs — `tools/runtime/README.md`, the kit's page, gains the binding and the check (I1).

## 6. Acceptance criteria

The fixture is a bare remote and clones under `%TEMP%` with short names, `trace.identity` planted per
case, `write_gov_ref` and `read_commits` installed from their parents.

- **AC1** — When `python bindings.py --fixture --plant write` runs, clone A's `write_binding` for one act
  leaves `refs/gov/bindings/<act>` on the remote naming a parentless commit over the empty tree whose
  message parses to the four keys, and a second `write_binding` for the same act returns 1.
  Red when: a binding commit has a parent, or a second write moves the ref.
- **AC2** — When `python bindings.py --fixture --plant fields` runs, a bad `epoch`, a 13-hex act id and,
  under `salted`, a missing `digest` each exit 2 naming the field with no ref written, and under
  `session` a supplied `digest` is refused the same way.
  Red when: any of the four reaches the remote.
- **AC3** — When `bash bindings.sh derive_act_identity act-3f9c0a1b2d4e` runs, it prints exactly
  `GIT_COMMITTER_NAME=gov-act` and `GIT_COMMITTER_EMAIL=act-3f9c0a1b2d4e@gov-act.invalid`.
  Red when: either line differs, or the author is named.
- **AC4** — When `python bindings.py --fixture --plant two-nodes` runs, clones A and B each push an act's
  binding and an act-made commit on their branches, clone C merges both and its `--check` prints two
  `bound ref` lines and `bindings — 2 bound · 0 not-local · 0 red`, exit 0.
  Red when: C reads either binding as `not-local`, or fetches more than once.
- **AC5** — When `python bindings.py --fixture --plant merge-main` runs, a branch that merged main, whose
  act commits have no binding on the remote, prints `0 act-made` from `--check` and exits 0, and the
  same plant graded from the branch's fork point as a frozen base exits 1 naming those commits.
  Red when: the range is computed from a base other than the current default tip.
- **AC6** — When `python bindings.py --fixture --plant unmarked` runs, a commit whose `Gov-Act:` names one
  act and whose committer names another, and a commit with the trailer under a human committer, each
  print `unmarked` and `--check` exits 1.
  Red when: a half-marked commit reads `bound`.
- **AC7** — When `python bindings.py --fixture --plant no-act` runs, a planted `Gov-Act:` naming no act
  prints `no act` and a well-formed act id the remote lacks prints `not-local`, and `--check` exits 1
  for each alone.
  Red when: either verdict leaves the exit 0.
- **AC8** — When `bash push-main.sh --carry --slug fx` runs in AC7's clone, it prints the check's lines
  after the carry lines and exits 1, and in AC4's clone C it exits 0.
  Red when: the landing passes over a `not-local` or `no act` commit.
- **AC9** — When `bash resolve-python.test.sh` reads `PARITY_ROWS`, it holds rows for `bindings.sh`'s
  `gov_ref_sh` block and `bindings.py`'s `remote_ladder_py` and `commit_trailers_py` blocks.
  Red when: a block in either file drifts from its canonical copy and no row names it.

## 7. Gates

`push-main self-test` · `python resolver (behaviour + inline parity + idiom ban)` · `run-gates canary` · `run-gates gov canary` · `measure-legs selftest` · `policy fixtures` · `memory hygiene`

New arm: tools/runtime/bindings.py · covers AC1 AC2 AC3 AC4 AC5 AC6 AC7 · each plant staged against a reader with S4's range replaced by the branch's fork point and S6's fetch removed · none
New arm: tools/push-main.test.sh · covers AC8 · `--carry` over a planted `no act` commit, staged by a `check_carry_bindings` that returns 0 · none
New arm: tools/lib/resolve-python.test.sh · covers AC9 · one byte changed in `bindings.py`'s `remote_ladder_py` block · none

## 8. Open questions

- **F1 — Which writer publishes a binding before TOOL-dPlacedRequest-11 is built?** (a) `write_gov_ref`
  and `build_gov_commit`, this unit built after its parent; (b) a stand-in following `write_claim`'s
  pattern, as I16 permits. (b) is a fourth hand copy of the one writer the brief forbids copying, and the
  parent builds before this build's build run. Rung 3, the most capable option with no copy. RESOLVED (agent, 2026-10-26, delegated): (a). widens: none · relaxes: none
- **F2 — Is a well-formed act the ref lacks red, or only uncounted?** (a) Counted `not-local` and the
  check exits 1; (b) counted and the check exits 0. (b) passes a binding nobody can read, against the
  clause's "never passed". Rung 1, the clause's text. RESOLVED (agent, 2026-10-26, delegated): (a). widens: none · relaxes: none
- **F3 — Which reader is "the landing's `carries`"?** (a) `push-main.sh`'s carry grading, `check_carry_set`
  and its two call sites; (b) the chain's `carries.py` instrument. (b) is an instrument the packet's
  Non-goals freeze, and it reads specs, not commits. Rung 1, the clause's "the landing". RESOLVED (agent, 2026-10-26, delegated): (a). widens: none · relaxes: none
- **F4 — How does the causes check read bindings?** An ask for dTotalRecall, target build dTotalRecall,
  for TOOL-dTotalRecall-19 S8's `check_causes` to grade act-made commits through
  `bindings.py --check` over its range; accept line: `check_causes` over a commit whose `Gov-Act:` the
  ref lacks reports it `not-local` and never passes it. The main loop files it once. Rung 3: editing a
  parent spec is refused by the brief. RESOLVED (agent, 2026-10-26, delegated): file the ask. widens: none · relaxes: none
- **F5 — Does a commit need both marks?** (a) Both, naming the same act, else `unmarked`; (b) either one.
  (b) lets a hand-typed trailer mark an owner's commit act-made. Rung 1, the clause's "by its trailer and
  by the committer identity". RESOLVED (agent, 2026-10-26, delegated): (a). widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft.

## 10. Reuse audit

The seams extended are TOOL-dPlacedRequest-11's `write_gov_ref` and `build_gov_commit`, extracted from
`write_claim` (`tools/unattended/unattended.sh:2396`, namespace constant `:2087`); the remote ladder
`resolve_remote` (`tools/lib/resolve_remote.py:17`) for the current default; TOOL-dDeclaredLoop-23's
`read_commits` for the trailer; and push-main's carry grading (`tools/push-main.sh:603`, `:962`,
`:1022`) for the landing. `python tools/codebase-map/reuse_lookup.py "publish a per-act binding record
to a governance ref and read it back on another node"` ranked `read`, `read_text`, `records` and
`read_journal` by name stem only: none publishes or reads a ref, so it found no seam beyond those read
by hand. Scout A's row cites `UA:2396` and `:2077-2087`, which hold at this base; its range note cites
dPlacedRequest-51 for `--no-merges`, a spec this unit does not need, since the clause states the flag.

Recall terms used: `python tools/memory-recall/query.py "how do checks on another node read an act's
binding" --terms "act binding refs/gov/bindings not-local salted digest epoch task-sha Gov-Act trailer
commit-key range"`
