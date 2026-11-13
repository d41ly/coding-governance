# TOOL-dDeclaredLoop-23 — the commit node and its kind, and one trailer reader with both views

**Status:** DEFERRED · rev-3 · 2026-11-13 · node d · Tier-2 · base ed497191 · streams tooling · order 3 · advances TOOL-dDeclaredLoop-35

**Carries:** cl-dClosedLoop-0108@df656363 whole
**Carries:** node:record-kind.commit

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md) | journal | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 TOOL-dDeclaredLoop-68 TOOL-dDeclaredLoop-69 TOOL-dDeclaredLoop-70 TOOL-dDeclaredLoop-71 TOOL-dDeclaredLoop-72 TOOL-dDeclaredLoop-73 TOOL-dDeclaredLoop-74 TOOL-dDeclaredLoop-75 TOOL-dDeclaredLoop-76 TOOL-dDeclaredLoop-77 TOOL-dDeclaredLoop-78 TOOL-dDeclaredLoop-79 TOOL-dDeclaredLoop-80 TOOL-dDeclaredLoop-81 TOOL-dDeclaredLoop-82 TOOL-dDeclaredLoop-83 TOOL-dDeclaredLoop-84 TOOL-dDeclaredLoop-85 TOOL-dDeclaredLoop-86 TOOL-dDeclaredLoop-87 TOOL-dDeclaredLoop-88 TOOL-dDeclaredLoop-89 TOOL-dDeclaredLoop-90 TOOL-dDeclaredLoop-91 TOOL-dDeclaredLoop-92 TOOL-dDeclaredLoop-93 TOOL-dDeclaredLoop-94 TOOL-dDeclaredLoop-95 TOOL-dDeclaredLoop-96 TOOL-dDeclaredLoop-97 TOOL-dDeclaredLoop-98 TOOL-dDeclaredLoop-99 TOOL-dDeclaredLoop-100 |
| [2026-10-24-build-TOOL-dDeclaredLoop-1-reuse-scout-b.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-reuse-scout-b.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 |
| [2026-10-24-build-TOOL-dDeclaredLoop-1-spec-stage-returns.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-spec-stage-returns.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 |
| [2026-11-13-build-TOOL-dDeclaredLoop-23-deviation-232.md](../build/2026-11-13-build-TOOL-dDeclaredLoop-23-deviation-232.md) | deviation | — |
| [2026-10-24-prompt-TOOL-dDeclaredLoop-1-spec-brief.md](../prompts/2026-10-24-prompt-TOOL-dDeclaredLoop-1-spec-brief.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 |
| [2026-11-13-prompt-TOOL-dDeclaredLoop-23-1-spec-writer.md](../prompts/2026-11-13-prompt-TOOL-dDeclaredLoop-23-1-spec-writer.md) | journal | — |
| [2026-11-13-prompt-TOOL-dDeclaredLoop-23-reground-brief.md](../prompts/2026-11-13-prompt-TOOL-dDeclaredLoop-23-reground-brief.md) | research | — |
| [2026-10-24-review-TOOL-dDeclaredLoop-1-spec-audit.md](../reviews/2026-10-24-review-TOOL-dDeclaredLoop-1-spec-audit.md) | spec-audit | TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-33 |

<!-- /gen:spec-records -->

## 1. Goal

A commit becomes a node with its own kind: the `commit` native-id class is registered, every trailer key
gov reads is registered with it, and one reader parses them, offering the two views today's readers
answer, the union of subject and trailer ids and the trailer replacing the subject, each consumer naming
its view. Today `Pass:` has two readings that disagree (`gap-spine-09`), and no commit names the item,
act or session that made it, with the trailer schema declared for the edge adapter alone
(`gap-spine-08`): `git log` over HEAD finds a `Gov-Unit`, `Gov-Item`, `Gov-Act` or `Gov-Session` trailer
on 0 of 8,623 commits, PINNED, measured 2026-11-13.

## 2. Scope (IN)

- **S1** — The `commit` native-id class: a `[[native]]` row in `tools/playbook/namespaces.toml`, beside
  the rows `family-id` and `clause-id`, with `class = "commit"`, `owner = "dDeclaredLoop"`,
  `pattern = "commit_trailers:SHA_RE"` and `resolver = "commit_trailers:--print-commits"`, the script
  form `tools/playbook/edge_grammar.py#read_native_members` already runs (§8 F6). Observed by AC6 and
  AC7.
- **S2** — The commit kind's keys, in the `[[trailer]]` table of `tools/playbook/edges.toml`. Its rows
  `Gov-Unit`, `Gov-Item` and `Pass` mapped to `serves`, `Gov-Act` to `made-by`, `Gov-Session` to
  `runs-in` and `Decided` to `decides` are read and asserted here, never re-added. This build adds
  rows with no `type`: `Gov-Transition` and `Gov-Policy`, the keys TOOL-dDeclaredLoop-3 and
  TOOL-dDeclaredLoop-2 write (shared interface I7, §8 F2), and `Red-fix`, the key
  `tools/memory-tree/routed_commits.py#read_routed_commits` reads in its one log pass (§8 F7).
  `tools/playbook/edge_grammar.py#read_trailer_keys` passes over a row with no `type` and still refuses
  a key named twice (§8 F5). Observed by AC6 and AC7.
- **S3** — The one reader, `tools/lib/commit_trailers.py`: `read_commits(repo, revs, keys, files=False,
  run=None)`, one `git log` call per read, git's own `%(trailers:key=…,valueonly)` parse;
  `derive_attribution(commit, view, id_re=None)` for the views `union` and `replace`;
  `read_message_ids(text)` for a commit message not yet committed; `SHA_RE`; and a CLI with the verbs
  `tokens` and `message` for the shell consumers, `--print-commits` for the native class and
  `--fixture`. The token rule is today's one rule: ids split on any character outside `[A-Za-z0-9-]`,
  and a `none` anywhere attributes the commit to nothing
  (`tools/unattended/lib-unattended.sh#pass_commit`). Observed by AC1, AC2 and AC4.
- **S4** — The copies, whole files that carry the canonical's block between `# >>> commit_trailers_py --
  canonical copy: commit_trailers.py in the gov lib dir (byte-identical; gated)` and
  `# <<< commit_trailers_py`, under one `commit_trailers_py` row of `PARITY_ROWS` in
  `tools/lib/resolve-python.test.sh`: `tools/memory-tree/commit_trailers.py` and
  `tools/unattended/commit_trailers.py`, the pattern `tools/memory-tree/coverage_join.py` sets for its
  canonical `tools/lib/coverage_join.py`. Each file also carries the `resolve_kit_dir` block under that
  block's existing row, through which the reader finds the key table. Observed by AC5.
- **S5** — The re-points, one unit, each consumer naming its view (§4 "### The consumers"):
  `routed_commits.py` (`union`), `deviation_join.py` and the unattended kit's four readers
  (`replace`). The legs `check-pass-order.sh` and `check-brief-recorded.sh`, which call
  `read_attribution_tokens` and resolve no interpreter today, each carry the `resolve_python` block
  (§8 F9). Observed by AC2, AC3, AC4 and AC8.
- **S6** — The planted commits `Pass: none`, `Pass: <id>` and a subject id with `Pass: none`, read
  identically by `routed_commits.py`'s attribution and by `read_attribution_tokens` before and after
  the re-point. Observed by AC2 and AC3.
- **S7** — The position engine reads commits through this reader: the hand-off of S3's API to
  TOOL-dDeclaredLoop-7. NOT OBSERVED here: that engine does not exist at this unit's order; its own
  spec observes the read.
- **S8** — The pages that name the registered classes and keys say what is registered:
  `help/tags.md`, `tools/playbook/README.md` and the header comment of `tools/playbook/edges.toml`
  name the `commit` class and the keys that carry no edge. Observed by AC9.

## 3. Non-goals (OUT)

- The writers of `Gov-Unit`, `Gov-Item`, `Gov-Act` and `Gov-Session`: dWellOiledMachine's commit queue
  and `prepare-commit-msg` filler (memory-plan `[sites]`). This build writes only `Gov-Transition`
  (TOOL-dDeclaredLoop-3) and `Gov-Policy` (TOOL-dDeclaredLoop-2).
- The commit adapter's own parse, `tools/playbook/edge_grammar.py#read_trailer_edges`, and the
  `[[trailer]]` table's typed rows: PLAY-dOrderedCharter-28's. This unit changes
  `read_trailer_keys` by S2's one rule and nothing else in that file.
- The runlog reader, `tools/runlog/model.py#read_git_range`, and a `commit_trailers_py` block in
  `tools/runlog/model.py`: TOOL-dDeclaredLoop-56 S19's, with the format arms that read needs (§8 F8).
- A floor for an install with no playbook kit: TOOL-dDeclaredLoop-40's. Here `read_commits` refuses
  with the resolver's own line.
- The trace checks over act-made commits (memory-plan `commits:` arm): dWellOiledMachine's.
- The `transition_audit.py` merge audit and the commit-msg hook's backlog arm, which read no `Pass:`.
- Test suites that read `Pass:` to assert fixtures (`tools/push-main.test.sh`,
  `tools/workflows/unattended-build.test.sh`): a suite reading a fixture's trailer is not a reader
  of record.
- A new gate leg, a guard edit in `tools/gate-legs.json`, a usage row, a registry row and a subject
  pin: the copies ship under each kit's `include = "**"`, no page shows the CLI, and the kickoff
  manifest's watch list names no file this unit writes.

### Edges

- **hands-off** `TOOL-dDeclaredLoop-2` — `commit_trailers.py`, which reads the `Gov-Policy` trailer its policy command writes
- **hands-off** `TOOL-dDeclaredLoop-3` — `commit_trailers.py`, which reads the `Gov-Transition` trailer its record writes
- **hands-off** `TOOL-dDeclaredLoop-7` — `commit_trailers.py`, the one reader the position engine reads commits through
- **hands-off** `TOOL-dDeclaredLoop-37` — the re-points' call-site observations, red at base, which that unit adds (the round-1 spec audit's id 8)
- **hands-off** `TOOL-dDeclaredLoop-38` — the trailer CLI's line endings, which that unit makes LF only (the round-1 spec audit's id 18)
- **hands-off** `TOOL-dDeclaredLoop-39` — the git pins of the reader's own runner, the one its CLI spawns git through, which that unit carries over from the readers it serves (the round-1 spec audit's id 19)
- **hands-off** `TOOL-dDeclaredLoop-40` — the reader's floor where no playbook kit resolves, which that unit specifies; the table's lookup lands here (the round-1 spec audit's id 47)
- **hands-off** `TOOL-dDeclaredLoop-56` — the minors of the round-1 spec audit that land on this unit, ids 20, 65, 66, each a scope item of that unit; id 20 is the runlog reader's whole re-point

## 4. Design

### The reader

```python
SHA_RE = re.compile(r"[0-9a-f]{40}")
VIEWS = ("union", "replace")

def read_commits(repo, revs, keys, files=False, run=None):   # -> [{sha, parents, date, subject, trailers[, paths]}]
def derive_attribution(commit, view, id_re=None):            # -> list of ids, in token order, deduplicated
def read_message_ids(text):                                  # -> the line the `message` verb prints
```

`read_commits` builds one format string, `%x1e%H%x1f%P%x1f%cI%x1f%s`, then one
`%x1f%(trailers:key=<k>,valueonly,unfold,separator=%x1d)` per requested key and a closing `%x1f`, so a
consumer pays for the keys it reads. `revs` is the caller's `git log` revision arguments, passed
through, so `-1 <sha>`, `--no-merges <range>` and `--reverse <range>` all read. `subject` is `%s`, the
first paragraph joined, which is what every reader reads today. `trailers` maps each requested key to
the list of its values.

`files=True` adds `-z --root --no-renames --name-only` and returns each commit's `paths`, the argv and
the split `read_routed_commits` runs today, moved. `run` is the consumer's own git runner, called as
`run(repo, argv)` and returning stdout bytes; with none given the reader spawns `git -C <repo>`
itself, which is the CLI's case. A Python consumer passes its runner, so its pins and its spawn count
hold (§8 F7).

| View | A commit with a `Pass:` trailer | A commit with none |
|---|---|---|
| `union` | the subject's ids, plus the trailer's ids; `Pass: none` adds none and keeps the subject's | the subject's ids |
| `replace` | the trailer's ids alone; a `none` anywhere attributes nothing | the subject's ids |

The ids are the whole tokens matching `id_re` when given, else every token of the token rule. A commit
is trailered when a `Pass` value holds a non-blank character.

The CLI:

| Verb | Prints |
|---|---|
| `tokens <revs>` | the bytes `read_attribution_tokens` prints today, one line per commit: `<sha> PASSTRAILER <ids>` for a trailered commit, else `<sha> <subject>`, every character outside `[A-Za-z0-9-]` and the newline turned into a space, runs of spaces kept |
| `message <file>` | one line: `PASSTRAILER <ids>` for a message whose `Pass:` values hold a token, else the subject's tokens, after the comment and CR stripping `check_commit_message` does today, the trailers read with `git interpret-trailers --parse` as it does |
| `--print-commits` | every sha `git rev-list HEAD` names in the working directory's repository, one per line; exit 3 where HEAD names no commit, which `read_native_members` reads as not armed here |
| `--fixture` | builds AC1's repository under the system temp directory and prints both views per commit |

A `Pass:` value of punctuation alone reads two ways today, and both stay: `tokens` prints
`PASSTRAILER` with no id, as the awk does, and `message` prints the subject's tokens, as
`check_commit_message` falls to its subject test.

### The consumers

| Consumer | Today | View | Re-point |
|---|---|---|---|
| `tools/memory-tree/routed_commits.py#read_routed_commits` | its own format string over `Pass` and `Red-fix`, with the paths | `union` | `read_commits(repo, rev_args, ("Pass", RED_FIX_TRAILER), files=True, run=…)`; each dict keeps `trailer` and `red_fix` beside the reader's keys, since `build_records.py`, `deviation_join.py` and `gen_build_index.py` read them |
| `tools/memory-tree/routed_commits.py#check_routed_commits` | `extract_unit_ids` over subject plus trailer | `union` | `derive_attribution(c, "union", id_re)` |
| `tools/memory-tree/routed_commits.py#read_newest_unit` | a second format string | `union` | `read_commits(repo, ["--no-merges", rev_range], ("Pass",), run=…)` and `derive_attribution(c, "union", id_re)` |
| `tools/memory-tree/deviation_join.py#read_first_passes` | the trailer in place of the subject, by hand | `replace` | `derive_attribution(c, "replace")`, its routed-path test kept on the untrailered branch |
| `tools/unattended/lib-unattended.sh#read_attribution_tokens` | awk over `git log` | `replace` | the kit's `commit_trailers.py tokens "$@"`, the file found beside the library through `BASH_SOURCE`, as `resolve_index_generator` finds its sibling |
| `tools/unattended/lib-unattended.sh#pass_commit` | its own `git log` and token rule | `replace` | `read_attribution_tokens --reverse "$_pa..$_pto"` into its scratch file, the unit matched as a whole token of the line |
| `tools/unattended/check-unattended.sh`, check 23's `dshitsub` read | one commit's subject and trailer, by hand | `replace` | `read_attribution_tokens -1 "$dshit"`, the sha and `PASSTRAILER` cut off |
| `tools/unattended/unattended.sh#check_commit_message` | `git interpret-trailers` and its own token rule | `replace` | the kit's `commit_trailers.py message "$msg"`, `PASSTRAILER` telling its trailer branch from its subject branch |

Each Python consumer imports its kit's copy and passes its `run_git`. Each shell consumer runs its
kit's copy with the launcher its caller resolves: `read_attribution_tokens` asks `resolve_python`
where the function is defined, as `resolve_index_generator` does, and with none defined or none
resolved it prints `lib-unattended: read_attribution_tokens found no python launcher, so no commit
is attributed` to stderr and returns 2. `unattended.sh` and `check-unattended.sh` carry the
`resolve_python` block today; `check-pass-order.sh` and `check-brief-recorded.sh` gain it (§8 F9).

`tools/runlog/model.py#read_git_range` stays on its own format string: it reads `%ct`, the body and
a name-status list in one counted call, and its module binds its own `SHA_RE` (§8 F8).

### The trailer table

```toml
# the playbook kit's edges.toml, beside PLAY-dOrderedCharter-28's typed rows
[[trailer]]
key = "Gov-Transition"     # value: <from> -> <to>, written by TOOL-dDeclaredLoop-3

[[trailer]]
key = "Gov-Policy"         # value: the policy change's record, written by TOOL-dDeclaredLoop-2

[[trailer]]
key = "Red-fix"            # value: one gate leg's name, read by the routed-commit gate
```

A row with no `type` registers a key that carries a value and no edge. `read_trailer_keys` returns the
typed rows alone, so the commit adapter never sees the others, and it refuses a key any two rows name.
`read_commits` reads every row's key through `resolve_kit_dir("playbook", "edges.toml", here)`, `here`
the copy's own directory, and refuses a requested key the table does not register, naming it, so a
consumer cannot read an unregistered trailer. The lookup is the resolver's and never a spelled sibling
path, which the install-prefix ban refuses.

### The native class

`read_native_classes` imports the pattern's module from the memory-tree kit's directory, so the
`commit` row reads `SHA_RE` from `tools/memory-tree/commit_trailers.py`, and `read_native_members`
runs that file with `--print-commits` in the graded repository. The pattern is the full sha, which
is what `read_trailer_edges` writes as a `Decided:` edge's target; an abbreviated sha is no member.
With the row in place such a target resolves where it reads `unarmed` today, and
`check_native_classes` prints the class with its member count.

### Inventory

Minted: `tools/lib/commit_trailers.py` with `SHA_RE`, `VIEWS`, `read_commits`, `derive_attribution`,
`read_message_ids`, the CLI verbs `tokens` and `message` and the flags `--print-commits` and
`--fixture`; the parity marker `commit_trailers_py`; the native class `commit`; the trailer rows
`Gov-Transition`, `Gov-Policy` and `Red-fix`. Naming cells: `python tools/lexicon/lexicon.py --suggest
<name> --as py.function` answers OK for `read_commits`, `derive_attribution` and `read_message_ids`,
asked 2026-11-13; `attribute`, the name rev-2 minted, leads with no declared verb.

### Migration

None: no reader's answer moves, and no trailer is rewritten. A row with no `type` is additive to
PLAY-dOrderedCharter-28's table.

### Rollout

Live at landing; every consumer's output is byte-identical on the planted commits (AC2, AC3).

### Files touched (estimate)

- `tools/lib/commit_trailers.py`
- `tools/lib/resolve-python.test.sh`
- `tools/memory-tree/commit_trailers.py`
- `tools/memory-tree/routed_commits.py`
- `tools/memory-tree/deviation_join.py`
- `tools/unattended/commit_trailers.py`
- `tools/unattended/lib-unattended.sh`
- `tools/unattended/check-unattended.sh`
- `tools/unattended/unattended.sh`
- `tools/unattended/check-pass-order.sh`
- `tools/unattended/check-brief-recorded.sh`
- `tools/playbook/namespaces.toml`
- `tools/playbook/edges.toml`
- `tools/playbook/edge_grammar.py`
- `tools/playbook/README.md`
- `help/tags.md`
- `memory/map/generated/symbols.json`, re-rendered by the codebase-map kit's generator
- `memory/project/fork-ceilings.txt`, only where a re-pointed shell reader moves its row's count

### Alternatives rejected

- **A shell canonical beside the Python one**, as `remote_ladder_sh` is: two implementations of one
  token rule, which is the disagreement this unit closes.
- **Re-pointing only the readers the clause names**: the others apply `replace` by hand, and one
  reader means every reader.

## 5. Production-readiness checklist

- security — read-only over git history and a message file; no network, no write. The resolver's
  answer rests on the working-tree receipt, as every `resolve_kit_dir` caller's does.
- perf / scale — one `git log` per read, as today; the shell readers trade an awk for one interpreter
  start per call, which the `spawn budget (forks per hot entrypoint)` leg grades and
  TOOL-dDeclaredLoop-56 S42 bounds for the per-commit caller.
- error / empty / loading states — an empty range returns no commits; an unregistered key is refused
  by name; no playbook kit is the resolver's `LookupError` line; no launcher is the library's named
  stderr line and status 2; a truncated stream is refused, as `read_routed_commits` refuses one today.
- observability — the CLI prints the same lines its shell consumers read today.
- risks — the unattended kit's suites are waived for this landing by the build README's rule on them,
  so the commit check's reading is observed by scratch probes (AC3, AC4), not by its suite. Until
  TOOL-dDeclaredLoop-38 lands, the CLI's lines end as the platform's `print` ends them. Until
  TOOL-dDeclaredLoop-40 lands, an install with no playbook kit refuses every read.
- testing — AC1 to AC9 by probes and fixtures under the system temp directory; the arms in §7 are
  observed RED then GREEN by the main loop at the close.
- migration — none.
- user docs — `help/tags.md` names the `commit` class beside the others and says a `[[trailer]]` row
  may carry no type (S8).

## 6. Acceptance criteria

- **AC1** — When `python commit_trailers.py --fixture` runs in `tools/lib/`, it builds a scratch
  repository under the system temp directory with three commits, a subject naming `TOOL-tFix-1` with
  no trailer, a subject naming `TOOL-tFix-1` with `Pass: none`, and a subject naming none with
  `Pass: TOOL-tFix-2`, and prints `union` as `TOOL-tFix-1`, `TOOL-tFix-1`, `TOOL-tFix-2` and `replace`
  as `TOOL-tFix-1`, nothing, `TOOL-tFix-2`.
  Red when: `replace` keeps the subject's id beside `Pass: none`, so the second commit reads
  `TOOL-tFix-1`.
  figure: PINNED, the fixture's own three commits.
- **AC2** — When a scratch probe imports the working tree's `routed_commits`, reads the AC1
  repository with `read_routed_commits(repo, ["HEAD"])` and prints `derive_attribution(c, "union",
  build_id_re(["TOOL"]))` per commit, it prints `TOOL-tFix-1`, `TOOL-tFix-1`, `TOOL-tFix-2`; and each
  commit's `sha`, `parents`, `date`, `subject`, `trailer`, `red_fix` and `paths` equal what the file
  at the pass's parent commit, read out with `git show` and imported with the kit's directory on
  `PYTHONPATH`, returns over the same repository.
  Red when: the re-pointed reader passes `replace`, so the `Pass: none` commit loses its subject id.
- **AC3** — When the same probe sources `tools/unattended/lib-unattended.sh` from the pass's parent
  commit and from the working tree, with gov's `resolve_python` defined, and writes
  `read_attribution_tokens HEAD` over the AC1 repository to one file per tree, `cmp` finds the files
  identical once `tr -d '\r'` has passed over each.
  Red when: the CLI squeezes the runs of spaces the awk leaves, or prints no `PASSTRAILER`.
- **AC4** — When `python commit_trailers.py message <file>` runs in `tools/unattended/` over the AC1
  commits' messages written to files, it prints `TOOL-tFix-1` among the first subject's tokens,
  `PASSTRAILER` with no id, and `PASSTRAILER TOOL-tFix-2`; and a copy of the first message with CRLF
  line ends and a `#` comment line prints the first line again.
  Red when: the comment line's words join the subject's tokens.
- **AC5** — When `git grep -c "commit_trailers_py" -- tools/lib/resolve-python.test.sh` runs, it counts
  the `PARITY_ROWS` row, and `git grep -l "^# >>> commit_trailers_py" -- tools` lists the canonical and
  the memory-tree and unattended copies; a one-byte edit to one copy makes the parity extract of that
  row differ.
  Red when: a copy carries no marker, so the parity population misses it.
- **AC6** — When `grep -n 'class = "commit"' namespaces.toml` and `grep -nE 'key =
  "(Gov-Transition|Gov-Policy|Red-fix)"' edges.toml` run in `tools/playbook/`, each finds its rows, and
  `read_commits` asked for a key `Gov-Nope` refuses naming the key.
  Red when: the reader reads any key it is handed, so an unregistered trailer is readable.
- **AC7** — When `python edge_grammar.py --list` runs in `tools/playbook/`, it exits 0 and its
  `edges: trailer` lines name the typed keys `Gov-Unit`, `Gov-Item`, `Gov-Act`, `Gov-Session`, `Pass`
  and `Decided` and no other; and `python gov_tag.py check` prints a line opening
  `tags: native · commit (owner dDeclaredLoop) ·` that ends in a member count.
  Red when: `read_trailer_keys` still demands a type of every row, so `--list` exits 2 on the first
  key that carries none.
- **AC8** — When `git grep -c "^# >>> resolve_python" -- tools/unattended/check-pass-order.sh
  tools/unattended/check-brief-recorded.sh` runs, it counts one block in each; and a scratch shell
  that sources the working tree's `lib-unattended.sh` with no `resolve_python` defined gets status 2
  and the named stderr line from `read_attribution_tokens HEAD`, with nothing on stdout.
  Red when: the library falls back to an empty answer, so a leg with no launcher reads every unit as
  unbuilt.
- **AC9** — When `grep -n 'commit' help/tags.md` runs, the native-ids paragraph names the `commit`
  class with its owner dDeclaredLoop, and the sentence listing the words no row registers yet no
  longer lists `commit`.
  Red when: the page still says two classes are registered.

## 7. Gates

`routed-commits selftest` · `routed commits name a specced unit` · `python resolver (behaviour + inline parity + idiom ban)` · `unattended kit gate` · `pass-order history` · `brief-recorded` · `spawn budget (forks per hot entrypoint)` · `scratch-guard self-test` · `tier2-review self-test` · `policy fixtures` · `recall floor` · `recall floor arms` · `playbook render selftest` · `govkit acceptance matrix` · `edges (every declared edge parses, is registered and resolves)` · `tags (the resolver's checks)` · `install-prefix (shipped surface)` · `help reference pages` · `codebase-map coverage + freshness` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

No leg is added and no guard moves, so `tools/gate-legs.json` and the kickoff manifest's stamp stay as
they are.

New arm: tools/memory-tree/routed_commits.py · covers AC2 · its union arms re-run through the re-pointed reader, the failing case staged by passing `replace` · none
New arm: tools/lib/resolve-python.test.sh · covers AC5 · the `commit_trailers_py` parity row, its failing case staged by a one-byte edit to the unattended copy · none
New arm: tools/playbook/edge_grammar.py · covers AC7 · a fixture registry holding a `[[trailer]]` row with no `type`, its failing case staged by restoring the type demand · none

## 8. Open questions

- **FACT-QUESTION · F1 — The brief gives this spec's status header the token `DRAFT`; is that a legal
  status?** Probe: `STATUS_TOKENS` in `tools/memory-tree/tree_lib.py`. Observation, 2026-10-24:
  `DRAFT` is not in the tuple. Liveness: the tuple would carry it if the vocabulary admitted it.
  RESOLVED (agent, 2026-10-24, delegated): `OPEN`, rung 2. widens: none · relaxes: none
- **F2 — Where are `Gov-Transition` and `Gov-Policy` registered, keys that carry a value and no edge?**
  Options: (a) `[[trailer]]` rows with no `type`, beside PLAY-dOrderedCharter-28's; (b) a constant in
  the reader; (c) a row typed with an existing edge. (b) splits the key register into two places and
  (c) types a transition as an edge it is not. RESOLVED (agent, 2026-10-24, delegated): (a), rung 3, one
  table for every key, shared interface I7's "all registered with the `commit` kind". widens: none ·
  relaxes: none
- **FACT-QUESTION · F3 — Which product files read the `Pass:` trailer?** Probe: `git grep -n
  "key=Pass\|interpret-trailers" -- tools skills .githooks` and the callers of
  `routed_commits.read_routed_commits`, reading each hit. Observation, 2026-10-24: seven product sites,
  the table of §4, beside two test suites. Liveness: a reader using git's trailer parse shows the key.
  RESOLVED (agent, 2026-10-24, delegated): all seven re-pointed, rung 2; the clause's "the three" are
  named among them. widens: none · relaxes: none
- **F4 — One canonical in Python, or one per language?** Options: (a) Python only, the shell readers
  calling its CLI; (b) Python and shell canonicals held to one answer, as the remote ladder is. (b) keeps
  two implementations of one rule. RESOLVED (agent, 2026-10-24, delegated): (a), rung 3, the clause's
  "one reader". widens: none · relaxes: none
- **F5 — How does the landed adapter take a `[[trailer]]` row with no `type`?** At HEAD
  `read_trailer_keys` raises on any row whose `type` is not of the set, so F2's pick (a) turns the
  edge check's every run into an exit 2. Options: (a) `read_trailer_keys` passes over a row with no
  `type`, returns the typed rows and keeps its named-twice refusal over all rows; (b) a second table
  in `edges.toml` that the adapter never reads; (c) a new edge type that means no edge. (b) puts the
  keys in two tables, against F2's reason, and (c) adds a type to a closed set to say nothing.
  Recommendation: (a), a one-condition change in the function F2's table already belongs to. The
  body is written on (a).
  RESOLVED (agent, 2026-11-13, delegated): (a), rung 3: the adapter passes over a typeless row and keeps its named-twice refusal.
  widens: none · relaxes: none
- **F6 — What resolves the `commit` class?** At HEAD `read_native_members` takes a resolver as a
  `--flag` script whose lines are the members, or as the one function `read_design_view`, which it
  calls with the design view; rev-2's `commit_trailers:resolve_commit` falls into the second branch
  and is called with the design view's path. Options: (a) the script form,
  `commit_trailers:--print-commits`, the class's members the full shas of HEAD's history and its
  pattern the full sha; (b) a third call shape in `read_native_members` for a per-token resolver that
  expands an abbreviation. (b) changes the member contract `resolve_edge` reads, a whole population
  asked once, for a target form no adapter writes: `read_trailer_edges` writes the full sha.
  Recommendation: (a). The body is written on (a), so `resolve_commit` is not minted.
  RESOLVED (agent, 2026-11-13, delegated): (a), rung 3: the script form resolves the commit class, so no resolver function is minted.
  widens: none · relaxes: none
- **F7 — How does `read_routed_commits` read through the one reader?** At HEAD it reads `Pass`,
  `Red-fix` and each commit's paths in one pinned, counted `git log`. Options: (a) `read_commits`
  takes `files=True` and the consumer's runner, and `Red-fix` is registered as a key with no type;
  (b) `read_routed_commits` keeps its own `git log` and only its attribution moves; (c)
  `read_commits` spawns git itself and a second call reads the paths. (b) leaves a second format
  string over `Pass`, which TOOL-dDeclaredLoop-37 S1 reds, and (c) breaks the constant spawn count
  the routed-commits arm holds and sheds `run_git`'s pins until TOOL-dDeclaredLoop-39.
  Recommendation: (a). The body is written on (a).
  RESOLVED (agent, 2026-11-13, delegated): (a), rung 3: the consumer hands the one reader its own runner, and Red-fix is a third typeless row.
  widens: none · relaxes: none
- **F8 — Does the runlog reader move at this order?** At HEAD `read_git_range` reads `%ct`, the body
  and a name-status list in one call `GIT_CALLS` counts, and the round-1 spec audit's id 20, confirmed,
  says `read_commits` cannot serve it without the format arms TOOL-dDeclaredLoop-56 S19 adds. Options:
  (a) re-point here with a second, uncounted spawn; (b) hand the re-point and the runlog block to
  TOOL-dDeclaredLoop-56 S19, this unit landing neither; (c) land the block here unread and re-point
  there. (a) doubles a read the runlog prices, and (c) ships a block nothing calls, whose `SHA_RE`
  would rebind `tools/runlog/model.py#SHA_RE`. Recommendation: (b). The body is written on (b), so
  rev-2's `decided` view and its criterion over `read_git_range` are not here.
  RESOLVED (agent, 2026-11-13, delegated): (b), rung 3: the runlog re-point goes to unit 56, which adds the format arms it needs.
  widens: none · relaxes: none
- **F9 — Where does a leg with no interpreter get one?** At HEAD `check-pass-order.sh` and
  `check-brief-recorded.sh` call `read_attribution_tokens` and carry no `resolve_python`. Options:
  (a) each carries the block inline under its existing parity row, as `unattended.sh` and
  `check-unattended.sh` do; (b) the library carries it once. (b) defines the function a second time
  in the two scripts that source the library and already carry it. Recommendation: (a). The body is
  written on (a).
  RESOLVED (agent, 2026-11-13, delegated): (a), rung 3: each of the two legs carries the interpreter block inline, as the scripts beside them do.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, from the packet's Items 23, the brief's shared interface I7,
  scout B's row for cl-0108, PLAY-dOrderedCharter-28 S2 and S5, and the readers read at base `ed497191`.
- rev-2 · 2026-10-24 · §3 · the Edges block gains a hands-off TOOL-dDeclaredLoop-37, a hands-off TOOL-dDeclaredLoop-38, a hands-off TOOL-dDeclaredLoop-39, a hands-off TOOL-dDeclaredLoop-40, a hands-off TOOL-dDeclaredLoop-56, the mirror of each unit the round-1 spec audit
  promoted (reviews/2026-10-24-review-TOOL-dDeclaredLoop-1-spec-audit.md); no scope moved.
- rev-3 · 2026-11-13 · §1 · S1 S2 S3 S4 S5 S6 S8 · §3 · §4 · §5 · AC1 to AC9 · §7 · §8 F5 F6 F7 F8 F9
  · §10 · re-grounded on `804ef34a` by the brief
  `prompts/2026-11-13-prompt-TOOL-dDeclaredLoop-23-reground-brief.md`. Moved by landed code: the
  adapter refuses a row with no type (S2, F5); a function resolver is called with the design view
  (S1, F6); `read_routed_commits` reads `Red-fix` and the paths in its one pinned call (S3, F7);
  `attribute` leads with no declared verb, so the view function is `derive_attribution`. Moved by
  reading HEAD: the runlog re-point and its block go to TOOL-dDeclaredLoop-56 S19 (F8), so rev-2's
  AC4 is the `message` verb's; the legs that resolve no interpreter gain the block (S5, F9, AC8); the
  table's lookup is the resolver's, since the install-prefix ban refuses a spelled sibling path; the
  pages that name the classes join the write set (S8, AC9); line citations became symbol citations.

## 10. Reuse audit

The seams extended are PLAY-dOrderedCharter-28's `[[native]]` and `[[trailer]]` tables, the script
resolver form of `tools/playbook/edge_grammar.py#read_native_members`, the whole-file canonical copy
`tools/memory-tree/coverage_join.py` is of `tools/lib/coverage_join.py` under its `PARITY_ROWS` row,
the sibling-kit resolver `tools/lib/resolve_kit_dir.py`, and each Python consumer's own git runner.
`python tools/codebase-map/reuse_lookup.py "read commit trailers with one parser offering union and
replace attribution views"` ranked `read`, `read_text`, `parse` and `build_commit` (name stems) and
named no trailer seam, run 2026-10-24. Source at HEAD shows these readers of a commit trailer, read
2026-11-13 from `git grep -n -E "key=Pass|interpret-trailers|trailers:key|PASSTRAILER" -- tools skills
.githooks`: the consumers of §4, `read_git_range` and the adapter's `read_trailer_edges`.

Recall terms used: `python tools/memory-recall/query.py "how do the two Pass trailer readers disagree on attribution" --terms "Pass trailer union replace read_attribution_tokens routed_commits Decided read_git_range attribution view"`
