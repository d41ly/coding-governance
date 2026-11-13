**Serves:** research TOOL-aBatchedPacket-1

# The dispatch declaration and the packet re-render: what each does, what its callers rely on, and where the time goes

Read and measured on node `a` on 2026-11-13, at `8db6f4bef`. Every timing below was taken on a frozen
clone, so no commit moved an input under it. The node was shared with the live dDeclaredLoop run
throughout, so wall times are an upper reading; the process counts do not depend on load.

## 1. The packet re-render and check

**What it does.** `packet.py --write <slug>` renders one chain build's packet from the tree and writes
it when the bytes differ. `--check <slug>` renders it again and compares the bytes, then runs the
completeness arms and the pin arm. Both start with `derive_sources(slug)`, which is where the time is.

**How.** `derive_sources` reads, in this order:

| Read | How it is made | Processes |
|---|---|---|
| the design: v2's `[chain]` rows, the owned nodes | `carries.design()`, in-process, which loads `map.py` | 6 git |
| the baseline clauses | one `git show <baseline>:<v2>` | 1 |
| the as-built view, the gap register, v2's sections | file reads | 0 |
| each parent's state | `schedule.tree_state("HEAD", …)`: one `git ls-tree` per parent, one `git show HEAD:<spec>` per parent spec | 2 + 125 for dDeclaredLoop, whose two parents hold 80 and 45 specs |
| the README roster, the decision row | file reads | 0 |
| the coverage field | a child: `carries.py --report <slug>` | 1 python, and see below |
| the open asks | a child: `gen_build_index.py --asks --build dClosedLoop --json` | 1 python |

The child `carries.py --report` runs `design()` again and then `real_specs(builds)`: for every `*.md`
under every chain build's `spec/` it runs one `git log --format=%H -- <path>` and one
`git show <sha>:<path>` per commit that log names. The tree holds 1543 chain specs in 22 builds.

**What the report reads of that.** Nothing. `main` calls `join(builds, nodes, retired, specs, b)` and
keeps only its second result, `carriers`, then prints `report(b, builds, nodes, specs, carriers)`
(`carries.py#main`). `join` builds `carriers` from `CARRY.findall(text)`, the working-tree text
(`:232-252`); the revision list is read once, under `if revs:`, and only appends to `findings`
(`:253-259`), which `--report` discards. `report` reads `specs` for `_, t, _`, the text alone, twice, and for a count. So the coverage field is a function of v2, the map's nodes and each chain spec's
working-tree text, and every `git log` and `git show` of `real_specs` is read and dropped.

**What its callers rely on.**

- The bytes of `memory/builds/<slug>/prompts/<date>-prompt-PLAY-dClosedLoop-1-packet.md`. `--check`
  compares them with a fresh render, and the driver's dispatch refuses a build whose packet is stale.
- `--write`'s two lines, `packet: wrote <path>` and `packet: <path> is current, nothing written`, and
  exit 0.
- `--check`'s summary line, which the spec-token checker quotes as a hit's reason, its finding lines,
  and its exit: 0 green, 1 on a finding or a refusal, 2 with nothing to check.
- The refusals: more than one packet, a packet with no pin, a non-UTF-8 packet, a first render inside
  a chain run, `carries.py --report` or `gen_build_index.py --asks` exiting non-zero, and v2 and
  `design()` naming different builds.
- The pin arm: each pinned instrument's blob against `git rev-parse HEAD:<path>`.

**Measured, `--check dDeclaredLoop`, the packet stale at this commit (exit 1, eight lines).**

| | Wall | Processes | Of which |
|---|---|---|---|
| the instrument | 845.5 s | 15,465 | `carries.py --report` 812.2 s: 13,901 `git show` 695.5 s, 1,543 `git log` 119.2 s; `--asks` 13.5 s |
| the prototype front door | 16.8 s | 20 | `--asks` 12.6 s; one `git cat-file --batch` |

The two runs printed the same eight lines and the same exit status. A `git show` cost 0.050 s and a
`git log` 0.077 s here; an earlier note put a spawn at 0.75 s under Git-Bash, which is the cost from a
shell and not from Python, so the count is the stable figure and the wall time scales with load. At
0.1 s a spawn the walk is 26 minutes, which is what the builders reported.

## 2. The dispatch declaration

**What it does.** `unattended.sh --dispatch <slug> --pass <unit> --writes <paths>` proves a pass may
start and parks one row, `dispatch · item <anchor> <unit> · reason <paths>`, in the build's `RUN.md`,
staged. Every refusal writes no row.

**How**, in `verb_dispatch`'s order (`tools/unattended/unattended.sh`):

1. The slug, the run state and the unit id's shape.
2. `check_chain_dispatch`: the chain verdict gate, check 118.
3. M2's floor: the unit has a tracked spec, and it is not THIN.
4. The order gate, the edge refusal, the edge set's own shape, the hold gate.
5. The `--writes` paths: shape, the run-state file, the shared records, an index with its generator,
   and condition 1 against every open sibling pass.
6. `run_spec_token_check`: the spec-token checker over the live tree. It is last among the local
   refusals because it is the one that costs a tree-wide scan.
7. The claim, then the row.

Steps 1 to 5 and 7 read the run-state file, spec headers and a few git answers. Step 6 is the cost.

**The spec-token check.** `derive_spec_token_key` hashes the slug, the checker, the launcher, HEAD and
the working-tree fingerprint, and a key equal to the last admitted one skips the checker. A dispatch
row is committed, and any commit moves HEAD, so a second declaration by the same unit misses the key
and runs the checker again. The checker then runs its ten joins. Nine read specs and the tracked
tree; its own carries join reads every chain spec's history in two git processes through
`design_lib.read_spec_revisions`. The tenth, the packet join (`scan_live_packets`), runs
`packet.py --check <slug>` for every chain build whose `RUN.md` is at a live phase, which is section 1's
cost once per live chain run.

**What its callers rely on.**

- Exit 0 and the two lines `unattended: dispatch declared — …` and `dispatch effective — …`.
- The parked row, which `--check-commit`, the `disjoint-passes` leg and `--audit` read.
- Each refusal under check 49, 108 or 118 with no row written. For step 6: a red in this build's own
  specs refuses; a red only in other builds' specs is announced and admitted; a checker that did not
  grade refuses.
- The key record, written only after the verdict admits, so a refusal is never cached.

**Measured, the checker alone, no chain run live in the clone of `8db6f4bef`.** 45.9 s, 26 processes,
exit 0, `packet join · 0 live chain run(s)`. So the checker's own nine joins and its carries join cost
under a minute, and a dispatch inside a live chain run pays that plus section 1 for each live run.
Section 4 holds the reading over a clone of the live run's own tip.

## 3. The candidates, and the one taken

| Candidate | Reading |
|---|---|
| One batched git read inside `carries.py` | The root cure, and ask `TOOL-dGroundRules-112` already files it. It moves a pinned instrument's blob, so every chain packet reds until the owner's `packet.py --repin`, which refuses inside a live chain run, and the edit lands alone in an owner-asked landing (the execution plan's retirement table). Not this build's to take. |
| A cache keyed on the blobs each stage reads | The key would cover v2, the map's inputs, 1543 spec texts, the README, the backlog and HEAD. Every spec or record commit moves one of them, and the task's own premise is that a commit precedes each re-render, so it would miss when it matters. |
| The dispatch reading a recorded packet verdict | The same miss: the dispatch follows a commit. It also puts a verdict between the instrument and its reader, which is where a red could be lost. |
| `--write` skipping the completeness and pin arms | `--write` runs neither arm today. Both `--write` and `--check` pay `derive_sources`, and the arms cost nothing measurable. |
| **Answer the instrument's two per-spec reads in-process, its bytes untouched** | Taken. 845.5 s to 16.8 s with the same output. No stored state, so nothing to invalidate. |

**The design.** A front door in `tools/` loads the tracked `packet.py` as a module and runs its own
`main`. Before that it replaces two reads:

- the child `carries.py --report <slug>`, by the carries instrument's own `design`, `join` and
  `report` called in-process over `(path, working-tree text, [])` for every chain spec;
- `schedule.git("show", "HEAD:<path>")`, by one `git cat-file --batch` process.

It is bound to content. It carries the blob id of `packet.py`, `carries.py` and `schedule.py` as read
for this analysis, and compares each with the file before loading anything. Any mismatch runs the
instrument as it stands, as a child, and says so on stderr. A re-pinned instrument, a stub or a local
edit is therefore graded the slow way, never by a shortcut read against other bytes.

## 4. Measured before and after, the prototype front door

All on node `a`, 2026-11-13, the dDeclaredLoop run live on the node throughout. `fc` is the frozen
clone of `8db6f4bef`; `fd` is a frozen clone of the live run's tip `f75d11d47`, whose `RUN.md` reads
`phase: BUILDING` and whose packet was stale at that commit.

| Step | Clone | Before | After | Same output |
|---|---|---|---|---|
| `packet.py --check dDeclaredLoop`, packet stale | fc | 845.5 s, 15,465 processes, exit 1 | 16.8 s, 20 processes, exit 1 | the eight lines, by `diff` |
| `packet.py --write dDeclaredLoop` | fc | 859.3 s, 15,459 processes, exit 0 | 16.2 s, 14 processes, exit 0 | the packet, 73,446 bytes, by `cmp`; sha1 `3f79a259` both |
| `--check dDeclaredLoop` after that write | fc | not run | 17.5 s, exit 0, byte compare green | |
| `check-spec-tokens.py`, no live chain run | fc | 45.9 s, 26 processes, exit 0 | unchanged path | |
| `check-spec-tokens.py`, one live chain run | fd | 1,062.1 s, 15,509 processes, exit 1 | 57.9 s, 46 processes, exit 1 | every line, the `[packet]` hit included, by `diff` |

The last row is the dispatch declaration's cost: `run_spec_token_check` runs that command, and the
rest of `verb_dispatch` reads the run-state file and spec headers. Its "after" was taken with the
checker's packet join pointed at the prototype in the clone, the one-line change the unit makes.

The instrument's fixture, through the prototype on `fc`, each about 20 s: the unplanted fixture exits
0; the plants `clause`, `gap`, `parent`, `owed`, `roster`, `ask`, `hand-edit` and `pin` exit 1, each
with its one finding; `run-live`, `run-unpushed`, `run-dirty`, `run-live-agent` and
`run-live-detached` exit 1 refused; `run-landed`, `run-pushed` and `run-live-owner` exit 0; the pin
plant's controls `no-pin-arm` and `repin` exit 0. Those are the exits the instrument's docstring
states for each. The fixture was not also run the instrument's way: each run costs the 14-minute
walk, and the plants damage the render and the arms, which the front door does not touch.

The three instrument blobs are the same in both clones: `packet.py` `cab3bff1`, `carries.py`
`0b5fab9c`, `schedule.py` `5aa5421e`.

## 5. What the design does not check

- A chain spec revision in history that is not UTF-8. The instrument's `real_specs` fails on one, and
  the packet then refuses naming `carries.py --report`. The front door never reads history, so it
  renders. No tracked chain spec revision is in that state; the product's own carries join decodes
  every one of them with `replace`.
- The carries child failing to start. The instrument refuses on the child's exit status; the front
  door has no child to fail. Git itself is run by both paths before the report.
- The Design-exit join, `carries.py --build <slug> --exit`, which reads every revision for its
  dropped-clause arm. It is not on either measured path and stays as it is.
- Whether the instrument's own reading is right. The front door changes how two inputs are fetched and
  nothing about what is done with them.
- A builder who runs `packet.py` directly, as a chain build's README words it. That call is unchanged
  and as slow as before; the bytes it writes are the bytes the front door writes.
