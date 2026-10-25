# TOOL-dWitnessedBar-64 — the seed reads HEAD as unborn only when it names a branch that does not exist, so a HEAD git cannot resolve takes the no-HEAD path

**Status:** OPEN · rev-2 · 2026-10-25 · node d · Tier-2 · base cdfbd1cf · streams tooling · order 36 · advances TOOL-dWitnessedBar-31

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md) | journal | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-54 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 TOOL-dWitnessedBar-58 TOOL-dWitnessedBar-59 TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-61 TOOL-dWitnessedBar-62 TOOL-dWitnessedBar-63 TOOL-dWitnessedBar-65 TOOL-dWitnessedBar-66 TOOL-dWitnessedBar-67 TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-71 TOOL-dWitnessedBar-72 TOOL-dWitnessedBar-73 TOOL-dWitnessedBar-74 TOOL-dWitnessedBar-75 TOOL-dWitnessedBar-76 TOOL-dWitnessedBar-77 TOOL-dWitnessedBar-78 TOOL-dWitnessedBar-79 TOOL-dWitnessedBar-80 TOOL-dWitnessedBar-81 TOOL-dWitnessedBar-82 TOOL-dWitnessedBar-83 TOOL-dWitnessedBar-84 TOOL-dWitnessedBar-85 TOOL-dWitnessedBar-86 TOOL-dWitnessedBar-87 TOOL-dWitnessedBar-88 TOOL-dWitnessedBar-89 TOOL-dWitnessedBar-90 TOOL-dWitnessedBar-91 TOOL-dWitnessedBar-92 |
| [2026-10-25-build-TOOL-dWitnessedBar-64-round5-fix-return.md](../build/2026-10-25-build-TOOL-dWitnessedBar-64-round5-fix-return.md) | research | TOOL-dWitnessedBar-65 |
| [2026-10-25-prompt-TOOL-dWitnessedBar-64-1-spec-writer.md](../prompts/2026-10-25-prompt-TOOL-dWitnessedBar-64-1-spec-writer.md) | journal | TOOL-dWitnessedBar-1 |
| [2026-10-25-prompt-TOOL-dWitnessedBar-64-round5-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dWitnessedBar-64-round5-fix-brief.md) | research | TOOL-dWitnessedBar-65 |
| [2026-10-25-review-TOOL-dWitnessedBar-64-spec-audit-round1.md](../reviews/2026-10-25-review-TOOL-dWitnessedBar-64-spec-audit-round1.md) | spec-audit | TOOL-dWitnessedBar-65 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of unit 63
(`memory/builds/dWitnessedBar/reviews/2026-10-25-review-TOOL-dWitnessedBar-63-spec-audit-round1.md`)
confirmed finding **id 20 at HIGH**, its item **H1**, which it shares with no other id.
`TOOL-dWitnessedBar-63` S8 defines an unborn HEAD as `git rev-parse --verify --quiet HEAD` exiting 1
with empty stdout and empty stderr. A repository whose branch ref is broken gives the same result, so
the seed stamps the null SHA, which means "seeded before any commit", into a tree git cannot read.
This unit replaces that predicate with one that names the class, a HEAD git cannot resolve to a
commit, and holds it with one corrupt-state fixture beside each clean one. It repairs
`TOOL-dWitnessedBar-63` and builds one step after it (order 36).

## 2. Scope (IN)

- **S1** — The HEAD probe asks for a commit. The seed's HEAD read becomes
  `git rev-parse --verify --quiet HEAD^{commit}`. A branch whose ref names a missing object then exits
  1 with nothing printed, where the bare `HEAD` form printed that object's SHA and exited 0.
  Observed by AC1 and AC3.
- **S2** — The unborn predicate. After S1's probe exits 1 with empty stdout and empty stderr, HEAD is
  unborn only when both further probes agree:
  - `git symbolic-ref -q HEAD` exits 0, prints exactly one line starting `refs/`, and prints nothing
    on stderr;
  - `git for-each-ref <that ref>` exits 0 and prints nothing on stdout and nothing on stderr.

  Only then does the seed stamp the null SHA, as unit 61's rule table states. Observed by AC1 and AC2.
- **S3** — Every other outcome takes `TOOL-dWitnessedBar-63` S6's no-HEAD path: no home is written,
  stdout carries `unarmed <name> no HEAD: <reason>`, and the reason goes to stderr. The reason is the
  first stderr line of the probe that ended the predicate. Where that probe printed no stderr, the
  reason is `git <verb> exit <rc>`, naming the probe's git verb and its exit code. Observed by AC1.
- **S4** — The corrupt-state fixtures. Section `2l` of `tools/lib/resolve-python.test.sh` gains four
  scratch repositories beside its clean commitless `git init`, each built as unit 61's AC1 fixture
  builds its registration:

  | fixture | how it is made | what the seed reads |
  |---|---|---|
  | broken branch ref | the branch file under `.git/refs/heads/` holds `garbage` | no HEAD |
  | missing object | the branch file holds forty `1` characters | no HEAD |
  | symbolic loop | the branch file holds `ref: refs/heads/other`, which points back | no HEAD |
  | detached, missing | `.git/HEAD` holds forty `1` characters | no HEAD, `git symbolic-ref exit 1` |

  Observed by AC1 and AC3.

## 3. Non-goals (OUT)

- `TOOL-dWitnessedBar-63` S6's no-HEAD route and its line shape. This unit routes more states onto
  it and changes neither.
- What the seed does when a git call cannot be spawned or times out. That is the round-1 audit's id 23
  item, held by the minors batch of that audit. S2's probes run through the same call S1's probe uses,
  so they get whatever handling that call has, in whichever order the two units build.
- The `--sha` existence check: the same audit's id 24 item, in the same batch.
- The report's left-shift text, a checklist entry for "a git state predicate defined by exit code
  and silence alone". No clause of this build names that gate. S4's fixtures are the regression arm
  this unit builds.

### Edges

- **consumes-from** `TOOL-dWitnessedBar-63` — S6's no-HEAD route and S8's exit-1-and-silent precondition, which S2 narrows to a branch that does not exist
- **hands-off** `TOOL-dWitnessedBar-67` — the round-1 audit of units 64 and 65's minors on this unit: fixtures built files-backed and config-proof, both files of the symbolic loop, a one-file chain held unborn, a reason for a probe that exits 0, a timeout on each probe, and a `seed --all` run in a corrupt fixture (ids 4, 13, 15, 16, 21, 22)

## 4. Design

### Evidence

All of these were probed with git 2.54.0.windows.1 in scratch repositories under `%TEMP%/wb64`, on
2026-10-25:

| state | `rev-parse --verify -q HEAD` | `HEAD^{commit}` form | `symbolic-ref -q HEAD` | `for-each-ref <ref>` |
|---|---|---|---|---|
| clean `git init` | 1, silent | 1, silent | 0, `refs/heads/master` | 0, silent |
| branch file `garbage` | 1, silent | 1, silent | 128, `fatal: No such ref: HEAD` | 0, `warning: ignoring broken ref refs/heads/master` |
| branch file names a missing object | 0, prints the object | 1, silent | 0, `refs/heads/master` | 128, `fatal: missing object 1111… for refs/heads/master` |
| symbolic loop | 1, silent | 1, silent | 128, `fatal: No such ref: HEAD` | 0, silent |
| detached HEAD naming a missing object | — | 1, silent | 1, silent | not reached |
| one commit, detached | 0, the SHA | 0, the SHA | not reached | not reached |

- Today's S8 reads the second row as unborn. That is the finding.
- The bare `HEAD` form also passes the third row's dangling SHA through as a stamp. That is the same
  class one probe earlier, which is why S1 asks for `^{commit}`.
- Git versions differ on the second row. 2.54 refuses at `symbolic-ref`. The report's reproduction
  found `symbolic-ref` succeeding and `for-each-ref` warning. S2 needs both probes silent, so either
  refusal ends the predicate.
- In the second row, `git add` stages a `kit.toml`, `git ls-files` lists it, and
  `git rev-parse --show-toplevel` resolves. So the registration and the home both resolve, and the
  seed reaches its HEAD read in the corrupt fixtures as it does in the clean one.
- The repository already reads the branch HEAD names with `symbolic-ref --quiet HEAD`
  (`.githooks/pre-commit:36`, `.githooks/commit-msg:52`).

### Inventory

Minted: the reason form `git <verb> exit <rc>`. No function, constant, flag or file is minted.
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
  named no-HEAD outcome, never a null-SHA row.
- observability — S3's reason names the probe that refused, or its verb and exit code.
- risks — a git release that prints a new stderr line on a clean unborn branch would route it to
  no HEAD. AC2's clean fixture catches that loudly.
- testing — AC1 to AC3 by fixture. The arm under §7 at the close.
- migration — none.
- user docs — none under `help/`; the module docstring states the predicate.

## 6. Acceptance criteria

- **AC1** — When `python legacy_ledger.py seed --population p` runs in each of S4's four corrupt
  fixtures, stdout carries one line opening `unarmed p no HEAD: ` followed by a non-empty reason, no
  home is written, and `grep -rl 0000000000000000000000000000000000000000` and `grep -rl 1111111111111111111111111111111111111111`
  over the fixture with `.git` excluded each print nothing. In the detached-missing fixture the reason
  is `git symbolic-ref exit 1`.
  Red when: the seed prints `armed p` in any corrupt fixture, or writes a file holding the null SHA or
  the dangling SHA.
  fixture: four scratch repositories under `%TEMP%/<short-name>`, built by section `2l`.
- **AC2** — When the same seed runs in the clean commitless `git init` beside them, it prints
  `armed p 2`, stderr carries `HEAD is unborn`, and each row's SHA field is forty `0` characters.
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

## 7. Gates

`python resolver (behaviour + inline parity + idiom ban)` · `shell-hygiene selftest` · `memory-hygiene self-test` · `codebase-map adopter e2e` · `codebase-map kit selftest` · `drift-audit selftest` · `memory hygiene`

The four kit legs run the arms of units 46, 47 and 53, which seed on a fresh or commitless tree and
read the unborn path S2 narrows. They are held unless the main loop sets GATE_SELFTESTS at the close.

New arm: tools/lib/resolve-python.test.sh · covers AC1 AC2 AC3 · section `2l` gains the four corrupt-state fixtures beside its clean commitless `git init`, staged red by removing S2's probes, by removing the `for-each-ref` probe alone, and by setting `HEAD^{commit}` back to `HEAD` · none

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

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, promoted from the round-1 spec audit of unit 63, id 20 (HIGH,
  item H1).
- rev-2 · 2026-10-25 · §3 · §4 · §3 gains the hands-off edge to `TOOL-dWitnessedBar-67`. §4 Rollout
  states order 36 alone, since `TOOL-dWitnessedBar-67` S16 moved unit 65 to order 37 (id 14 of the
  round-1 audit of units 64 and 65). No scope item or criterion moves.

## 10. Reuse audit

The seam is the existing branch read, `symbolic-ref --quiet HEAD` (`.githooks/pre-commit:36`,
`.githooks/commit-msg:52`), together with unit 61's HEAD probe, which this unit narrows rather than
replaces. `python tools/codebase-map/reuse_lookup.py "tell an unborn branch from a broken branch ref"`
ranked `branches` (`tools/memory-tree/check-arms.py`), `resolve_base_ref` and
`branch_reconcile.read_inventory`. None of them reads an unborn or broken HEAD, so no existing seam
fits beyond the branch read named above. `git grep -n "symbolic-ref\|for-each-ref" -- tools .githooks`
found the hook reads and no `for-each-ref` caller that tests silence. The unborn reader
`read_worktree_head` (`tools/memory-recall/query.py:260-273`) treats every failure as unborn, which is
the conflation this unit removes, so it is not reused.

Recall terms used: `python tools/memory-recall/query.py "how does a tool tell an unborn HEAD from a broken branch ref" --terms "unborn HEAD broken ref symbolic-ref for-each-ref rev-parse verify quiet null sha seed legacy_ledger corrupt"`
