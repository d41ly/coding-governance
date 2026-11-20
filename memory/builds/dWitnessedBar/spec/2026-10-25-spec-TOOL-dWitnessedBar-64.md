# TOOL-dWitnessedBar-64 — the seed reads HEAD as unborn only when it names a branch that does not exist, so a HEAD git cannot resolve takes the no-HEAD path

**Status:** INPROGRESS · rev-3 · 2026-11-21 · node d · Tier-2 · base cdfbd1cf · streams tooling · order 36 · advances TOOL-dWitnessedBar-31

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md) | journal | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-54 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 TOOL-dWitnessedBar-58 TOOL-dWitnessedBar-59 TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-61 TOOL-dWitnessedBar-62 TOOL-dWitnessedBar-63 TOOL-dWitnessedBar-65 TOOL-dWitnessedBar-66 TOOL-dWitnessedBar-67 TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-71 TOOL-dWitnessedBar-72 TOOL-dWitnessedBar-73 TOOL-dWitnessedBar-74 TOOL-dWitnessedBar-75 TOOL-dWitnessedBar-76 TOOL-dWitnessedBar-77 TOOL-dWitnessedBar-78 TOOL-dWitnessedBar-79 TOOL-dWitnessedBar-80 TOOL-dWitnessedBar-81 TOOL-dWitnessedBar-82 TOOL-dWitnessedBar-83 TOOL-dWitnessedBar-84 TOOL-dWitnessedBar-85 TOOL-dWitnessedBar-86 TOOL-dWitnessedBar-87 TOOL-dWitnessedBar-88 TOOL-dWitnessedBar-89 TOOL-dWitnessedBar-90 TOOL-dWitnessedBar-91 TOOL-dWitnessedBar-92 TOOL-dWitnessedBar-93 TOOL-dWitnessedBar-94 TOOL-dWitnessedBar-95 TOOL-dWitnessedBar-96 TOOL-dWitnessedBar-97 |
| [2026-10-25-build-TOOL-dWitnessedBar-64-deviation-641.md](../build/2026-10-25-build-TOOL-dWitnessedBar-64-deviation-641.md) | deviation | — |
| [2026-10-25-build-TOOL-dWitnessedBar-64-round5-fix-return.md](../build/2026-10-25-build-TOOL-dWitnessedBar-64-round5-fix-return.md) | research | TOOL-dWitnessedBar-65 |
| [2026-10-25-prompt-TOOL-dWitnessedBar-64-1-spec-writer.md](../prompts/2026-10-25-prompt-TOOL-dWitnessedBar-64-1-spec-writer.md) | journal | TOOL-dWitnessedBar-1 |
| [2026-10-25-prompt-TOOL-dWitnessedBar-64-round5-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dWitnessedBar-64-round5-fix-brief.md) | research | TOOL-dWitnessedBar-65 |
| [2026-11-19-prompt-TOOL-dWitnessedBar-64-build-brief.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-64-build-brief.md) | journal | — |
| [2026-11-19-prompt-TOOL-dWitnessedBar-64-reground-brief.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-64-reground-brief.md) | journal | — |
| [2026-11-19-prompt-TOOL-dWitnessedBar-64-reground-spec-writer.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-64-reground-spec-writer.md) | journal | — |
| [2026-10-25-review-TOOL-dWitnessedBar-64-spec-audit-round1.md](../reviews/2026-10-25-review-TOOL-dWitnessedBar-64-spec-audit-round1.md) | spec-audit | TOOL-dWitnessedBar-65 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of unit 63
(`memory/builds/dWitnessedBar/reviews/2026-10-25-review-TOOL-dWitnessedBar-63-spec-audit-round1.md`)
confirmed finding **id 20 at HIGH**, its item **H1**, which it shares with no other id.
`TOOL-dWitnessedBar-63` S8 defines an unborn HEAD as `git rev-parse --verify --quiet HEAD` exiting 1
with empty stdout and empty stderr, and it landed so in `tools/lib/legacy_ledger.py#read_head_sha`,
whose docstring names the gap as what it does not check. A repository whose branch ref is broken gives
the same result, so the seed stamps the null SHA, which means "seeded before any commit", into a tree
git cannot read. This unit replaces that predicate with one that names the class, a HEAD git cannot
resolve to a commit, and holds it with one corrupt-state fixture beside each clean one. It repairs
`TOOL-dWitnessedBar-63` and builds one step after it (order 36).

## 2. Scope (IN)

- **S1** — The HEAD probe asks for a commit. The probe in `read_head_sha` becomes
  `git rev-parse --verify --quiet HEAD^{commit}`. A branch whose ref names a missing object then exits
  1 with nothing printed, where the bare `HEAD` form printed that object's SHA and exited 0.
  Observed by AC1 and AC3.
- **S2** — The unborn predicate. After S1's probe exits 1 with empty stdout and empty stderr, HEAD is
  unborn only when both further probes agree:
  - `git symbolic-ref -q HEAD` exits 0, prints exactly one line starting `refs/`, and prints nothing
    on stderr;
  - `git for-each-ref <that ref>` exits 0 and prints nothing on stdout and nothing on stderr.

  Only then does `read_head_sha` return `NULL_SHA`, as unit 61's rule table states. Its docstring's
  WHAT IT DOES NOT CHECK clause is rewritten to what this predicate leaves unchecked.
  Observed by AC1 and AC2.
- **S3** — Every other outcome takes `TOOL-dWitnessedBar-63` S6's no-HEAD path as it landed in
  `tools/lib/legacy_ledger.py#run_seed_cli`: no home is written, stdout carries
  `unarmed <name> no HEAD: <reason>`, stderr carries `legacy_ledger: <name>: no HEAD: <reason>;
  nothing written`, and the seed exits 1. The reason is the first stderr line of the probe that ended
  the predicate. Where that probe printed no stderr, the reason is `git <verb> exited <rc>`, naming the
  probe's git verb and its exit code: the fallback `read_head_sha` already writes for its one probe,
  `git rev-parse exited <rc>`, applied to all three (§8 F3). Observed by AC1 and AC4.
- **S4** — The corrupt-state fixtures. Section `2o` of `tools/lib/resolve-python.test.sh` gains a block
  after its unborn-seed block (unit 61 AC1 AC2), whose clean fixture is a commitless `git init`. The
  new block builds four scratch repositories, each a fresh `git init` holding the registration that
  block builds with `build_ll_seeded p`:

  | fixture | how it is made | what the seed reads |
  |---|---|---|
  | broken branch ref | the branch file under `.git/refs/heads/` holds `garbage` | no HEAD |
  | missing object | the branch file holds forty `1` characters | no HEAD |
  | symbolic loop | the branch file holds `ref: refs/heads/other`, which points back | no HEAD |
  | detached, missing | `.git/HEAD` holds forty `1` characters | no HEAD, `git symbolic-ref exited 1` |

  The unborn-seed block's WHAT THIS DOES NOT CHECK clause, "a git failure other than an unborn HEAD",
  and the no-HEAD block's "a real corrupt HEAD" are rewritten, since this block checks both.
  Observed by AC1 and AC3.

## 3. Non-goals (OUT)

- `TOOL-dWitnessedBar-63` S6's no-HEAD route and its line shape. This unit routes more states onto
  it and changes neither.
- What the seed does when a git call cannot be spawned or times out. That is the round-1 audit's id 23
  item, held by the minors batch of that audit. S2's probes run through
  `tools/lib/legacy_ledger.py#_run_git`, the call S1's probe uses, so they get whatever handling that
  call has, in whichever order the two units build.
- The `--sha` existence check: the same audit's id 24 item, in the same batch.
- The report's left-shift text, a checklist entry for "a git state predicate defined by exit code
  and silence alone". No clause of this build names that gate. S4's fixtures are the regression arm
  this unit builds.
- The other bare unborn readers, `tools/memory-recall/query.py#read_worktree_head` and
  `tools/playbook/overlay.py#check_born`, which `read_head_sha`'s docstring names. They sit outside
  this unit's population, the `legacy_ledger_py` block, and neither stamps a SHA into a home.
- Unit 28, deferred with three dOrderedCharter asks (TOOL-dWitnessedBar-101 to -103): no item here
  needs it.

### Edges

- **consumes-from** `TOOL-dWitnessedBar-63` — S6's no-HEAD route and S8's exit-1-and-silent precondition, which S2 narrows to a branch that does not exist
- **hands-off** `TOOL-dWitnessedBar-67` — the round-1 audit of units 64 and 65's minors on this unit: fixtures built files-backed and config-proof, both files of the symbolic loop, a one-file chain held unborn, a reason for a probe that exits 0, a timeout on each probe, and a `seed --all` run in a corrupt fixture (ids 4, 13, 15, 16, 21, 22)

## 4. Design

### Evidence

All of these were probed with git 2.54.0.windows.1 in scratch repositories under `%TEMP%` on
2026-10-25, and re-probed at HEAD `dc5d941a3` with the same results (PINNED 2026-11-21):

| state | `rev-parse --verify -q HEAD` | `HEAD^{commit}` form | `symbolic-ref -q HEAD` | `for-each-ref <ref>` |
|---|---|---|---|---|
| clean `git init` | 1, silent | 1, silent | 0, `refs/heads/master` | 0, silent |
| branch file `garbage` | 1, silent | 1, silent | 128, `fatal: No such ref: HEAD` | 0, `warning: ignoring broken ref refs/heads/master` |
| branch file names a missing object | 0, prints the object | 1, silent | 0, `refs/heads/master` | 128, `fatal: missing object 1111… for refs/heads/master` |
| symbolic loop | 1, silent | 1, silent | 128, `fatal: No such ref: HEAD` | 0, silent |
| detached HEAD naming a missing object | 0, prints the object | 1, silent | 1, silent | not reached |
| one commit, detached | 0, the SHA | 0, the SHA | not reached | not reached |

- `read_head_sha` at HEAD returns the null SHA in the garbage and loop fixtures and the `1111…` SHA
  in the missing-object and detached fixtures (PINNED 2026-11-21). That is the finding.
- The bare `HEAD` form passes a dangling SHA through as a stamp. That is the same class one probe
  earlier, which is why S1 asks for `^{commit}`.
- Git versions differ on the second row. 2.54 refuses at `symbolic-ref`. The report's reproduction
  found `symbolic-ref` succeeding and `for-each-ref` warning. S2 needs both probes silent, so either
  refusal ends the predicate.
- In each corrupt fixture, `git add` stages a `kit.toml`, `git ls-files` lists it, and
  `git rev-parse --show-toplevel` resolves (PINNED 2026-11-21). `run_seed_cli` resolves the SHA after
  the toplevel and before it reads registrations, so the seed reaches S2 and prints a line per
  population in the corrupt fixtures as it does in the clean one.
- The repository already reads the branch HEAD names with `symbolic-ref --quiet HEAD`
  (`.githooks/pre-commit@dc5d941a3:108`, `.githooks/commit-msg@dc5d941a3:52`).

### Inventory

Minted: none. S3's reason form `git <verb> exited <rc>` extends the fallback `read_head_sha` already
writes. No function, constant, flag or file is minted: the two probes sit inside `read_head_sha`.
Naming cells: none apply, since nothing in the lexicon's declared cells is minted.

### Migration

None: no population has been seeded under the factory yet.

### Rollout

Live at landing, one step after `TOOL-dWitnessedBar-63`. Order 36 holds this unit alone. The minors
batch of the same audit, `TOOL-dWitnessedBar-65`, writes the three `legacy_ledger.py` copies and the
resolver suite too, so `TOOL-dWitnessedBar-67` S16 moved it to order 37, applied in the commit that
lands that spec. Neither unit consumes from the other: each states its items against the seed's SHA
resolution by what it does, so either build order yields the same tree.

### Files touched (estimate)

The population is every copy of the `legacy_ledger_py` block, three files (DERIVED by
`git grep -l '>>> legacy_ledger_py' -- tools`), held identical by the resolver suite's parity part.

- `tools/lib/legacy_ledger.py`
- `tools/memory-tree/legacy_ledger.py`
- `tools/gate-lint/legacy_ledger.py`
- `tools/lib/resolve-python.test.sh`

### Alternatives rejected

- **Read the ref files directly**, checking that no loose file and no `packed-refs` line names the
  branch. That reimplements git's ref store, misses a reftable repository, and reads a dangling loose
  file as present.
- **Match `git log -1`'s message**, such as `does not have any commits yet`. That text is localised and
  changes between releases. A predicate built on a message is the shape this finding forbids.
- **`git show-ref --verify <ref>`** in place of `for-each-ref`. It exits 1 with
  `fatal: '<ref>' - not a valid ref` on a clean unborn branch. That reason is not empty, so it cannot
  tell absent from broken by silence.

## 5. Production-readiness checklist

- security — no new write path. The change narrows when the null SHA is written, so S3's route
  writes nothing where git cannot resolve HEAD.
- perf / scale — two more `git` calls, made only on the path where S1's probe already failed.
- error / empty / loading states — a broken, dangling, looping or detached-missing HEAD becomes a
  named no-HEAD outcome, never a null-SHA or dangling-SHA row.
- observability — S3's reason names the probe that refused, or its verb and exit code.
- risks — a git release that prints a new stderr line on a clean unborn branch would route it to
  no HEAD. AC2's clean fixture catches that loudly.
- testing — AC1 to AC4 by fixture. The arm under §7 at the close.
- migration — none.
- user docs — none under `help/`, which names no unborn HEAD; the `read_head_sha` docstring states
  the predicate.

## 6. Acceptance criteria

- **AC1** — When `python legacy_ledger.py seed --population p` runs in each of S4's four corrupt
  fixtures, it exits 1, stdout carries one line opening `unarmed p no HEAD: ` followed by a non-empty
  reason, stderr carries that reason followed by `; nothing written`, no home is written, and
  `grep -rl 0000000000000000000000000000000000000000` and `grep -rl 1111111111111111111111111111111111111111`
  over the fixture with `.git` excluded each print nothing. In the detached-missing fixture the reason
  is `git symbolic-ref exited 1`.
  Red when: the seed prints `armed p` in any corrupt fixture, or writes a file holding the null SHA or
  the dangling SHA.
  fixture: four scratch repositories under `%TEMP%/<short-name>`, built by S4's block in section `2o`.
- **AC2** — When the same seed runs in the clean commitless `git init` of the unborn-seed block, its
  existing case `2o unborn AC1` holds: it prints `armed p 2`, `HEAD is unborn` appears once, and each
  row's SHA field is forty `0` characters.
  Red when: the predicate refuses a genuinely unborn HEAD, for instance by reading `for-each-ref`'s
  exit code alone or by requiring a branch file to exist.
- **AC3** — When the seed of a scratch copy of `legacy_ledger.py`, taken from `tools/lib/`, with S2's
  two probes removed runs in the broken-ref, missing-object and symbolic-loop fixtures, each prints
  `armed p`.
  With only the `for-each-ref` probe removed, the missing-object fixture prints `armed p`. With
  `HEAD^{commit}` set back to `HEAD`, the missing-object fixture stamps the `1111…` SHA.
  Red when: a staged break leaves every fixture reading no HEAD, so a probe the predicate names guards
  nothing.
  fixture: the same scratch repositories, and scratch copies of the module under `%TEMP%/<short-name>`.
- **AC4** — When section `2o`'s unit-63 case runs `read_head_sha` under a `_run_git` stand-in answering
  exit 128 with nothing printed, it prints `(None, 'no HEAD: git rev-parse exited 128')`.
  Red when: S3's fallback is spelled apart from the landed `git rev-parse exited <rc>`, or an exit
  other than 1 from S1's probe reaches S2's probes.

## 7. Gates

`python resolver (behaviour + inline parity + idiom ban)` · `shell-hygiene selftest` · `policy fixtures` · `memory-hygiene self-test` · `codebase-map adopter e2e` · `codebase-map kit selftest` · `drift-audit selftest` · `memory hygiene`

`policy fixtures` is owed by its guard on `tools/memory-tree/legacy_ledger.py`. Of the kit legs,
`memory-hygiene self-test` and `codebase-map adopter e2e` run the arms of units 46, 53 and 47, which
seed on a fresh or commitless tree and read the unborn path S2 narrows. Every leg here but
`memory hygiene` has subject `kit` in `tools/gate-legs.json`, so each is held unless the main loop sets
GATE_SELFTESTS at the close.

New arm: tools/lib/resolve-python.test.sh · covers AC1 AC2 AC3 AC4 · section `2o` gains S4's block of four corrupt-state fixtures after its unborn-seed block, staged red by removing S2's probes, by removing the `for-each-ref` probe alone, and by setting `HEAD^{commit}` back to `HEAD` · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec that carries nothing and is derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of the repaired unit's clause. Unit 63 is itself derived
  and carries no clause, so (b) has nothing to split; veto 1 discards it. RESOLVED (agent, 2026-10-25,
  delegated): (a), rung 3, the precedent `TOOL-dDeclaredLoop-36` §8 F1 set.
  widens: none · relaxes: none
- **F2 — Which predicate tells an unborn HEAD from one git cannot resolve (id 20)?** Options:
  (a) `symbolic-ref` naming a branch and `for-each-ref` silent on it, after a `^{commit}` probe;
  (b) reading the ref store's files; (c) matching `git log -1`'s message; (d) `show-ref --verify`'s
  exit code. §4 Alternatives rejected gives the probe that rules out each of (b) to (d). (b) misses
  reftable and dangling files, (c) depends on localised text, and (d) is not silent on a clean unborn
  branch. Each fails AC2 or AC1 on a state §4's table holds; veto 1 discards them. RESOLVED (agent,
  2026-10-25, delegated): (a), rung 3, the one survivor. Its `^{commit}` half follows from the class
  rule, since the missing-object row is the same class one probe earlier.
  widens: none · relaxes: none
- **F3 — How is a silent refusal's reason spelled (forced by the re-ground)?** Unit 63 landed
  `read_head_sha`'s fallback as `git rev-parse exited <rc>`, and its section `2o` case asserts
  `no HEAD: git rev-parse exited 128`; rev-2 minted `git <verb> exit <rc>` before that landed.
  Options: (a) `git <verb> exited <rc>`, the landed form applied to all three probes; (b) rev-2's
  `git <verb> exit <rc>`, rewriting the landed fallback and the closed unit's assertion. (b) reds that
  assertion in the resolver leg §7 names, so veto 1 discards it. RESOLVED (agent, 2026-11-21,
  delegated): (a), the one survivor, which also reuses the landed seam. `TOOL-dWitnessedBar-65` S9
  and `TOOL-dWitnessedBar-67`, which spell rev-2's form after this unit's S3, follow it at their
  re-ground.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, promoted from the round-1 spec audit of unit 63, id 20 (HIGH,
  item H1).
- rev-2 · 2026-10-25 · §3 · §4 · §3 gains the hands-off edge to `TOOL-dWitnessedBar-67`. §4 Rollout
  states order 36 alone, since `TOOL-dWitnessedBar-67` S16 moved unit 65 to order 37 (id 14 of the
  round-1 audit of units 64 and 65). No scope item or criterion moves.
- rev-3 · 2026-11-21 · §1 §2 §3 §4 §5 §6 §7 §8 §10 · S2 S3 S4 · AC1 AC2 AC4 · re-grounded over unit 63
  as landed, per `2026-11-19-prompt-TOOL-dWitnessedBar-64-reground-brief`: the fixtures move from
  section `2l`, now the envelope's, to a block in section `2o`; S3 takes the landed
  `git <verb> exited <rc>` fallback (§8 F3) and AC4 holds it; the evidence is re-probed at HEAD;
  `policy fixtures` joins the leg line; citations move to `path#symbol` or blob-pinned lines.

## 10. Reuse audit

The seam is `tools/lib/legacy_ledger.py#read_head_sha`, unit 61's HEAD probe as unit 63 landed it,
which this unit narrows rather than replaces, together with the existing branch read
`symbolic-ref --quiet HEAD` (`.githooks/pre-commit@dc5d941a3:108`, `.githooks/commit-msg@dc5d941a3:52`,
`tools/branch-reconcile/branch_reconcile.py#resolve_remote`). S3 extends the probe's
`git rev-parse exited <rc>` fallback rather than minting a second form.
`python tools/codebase-map/reuse_lookup.py "tell an unborn branch from a broken branch ref"`, re-run on
2026-11-21, ranked `branches` (`tools/memory-tree/check-arms.py`), `resolve_base_ref`,
`resolve_landed_ref` and `branch_reconcile.read_inventory`. None of them reads an unborn or broken
HEAD, so no existing seam fits beyond the two named above. `git grep -n "symbolic-ref\|for-each-ref"
-- tools .githooks` found the branch reads and no `for-each-ref` caller that tests silence:
`tools/branch-reconcile/branch_reconcile.py#read_refs` lists refs by format. The unborn readers
`tools/memory-recall/query.py#read_worktree_head` and `tools/playbook/overlay.py#check_born` treat
every failure as unborn, the conflation this unit removes, so neither is reused.

Recall terms used: `python tools/memory-recall/query.py "how does a tool tell an unborn HEAD from a broken branch ref" --terms "unborn HEAD broken ref symbolic-ref for-each-ref rev-parse verify quiet null sha seed legacy_ledger corrupt"`
