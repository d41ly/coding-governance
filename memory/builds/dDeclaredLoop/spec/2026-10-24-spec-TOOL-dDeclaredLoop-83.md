# TOOL-dDeclaredLoop-83 — 75 S27 states 81's exit table, so no merge-tree exit but 0 and 1 falls to the parents

**Status:** CLOSED · rev-5 · 2026-11-15 · node d · Tier-2 · base ed497191 · streams tooling · order 21 · advances TOOL-dDeclaredLoop-35

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md) | journal | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 TOOL-dDeclaredLoop-68 TOOL-dDeclaredLoop-69 TOOL-dDeclaredLoop-70 TOOL-dDeclaredLoop-71 TOOL-dDeclaredLoop-72 TOOL-dDeclaredLoop-73 TOOL-dDeclaredLoop-74 TOOL-dDeclaredLoop-75 TOOL-dDeclaredLoop-76 TOOL-dDeclaredLoop-77 TOOL-dDeclaredLoop-78 TOOL-dDeclaredLoop-79 TOOL-dDeclaredLoop-80 TOOL-dDeclaredLoop-81 TOOL-dDeclaredLoop-82 TOOL-dDeclaredLoop-84 TOOL-dDeclaredLoop-85 TOOL-dDeclaredLoop-86 TOOL-dDeclaredLoop-87 TOOL-dDeclaredLoop-88 TOOL-dDeclaredLoop-89 TOOL-dDeclaredLoop-90 TOOL-dDeclaredLoop-91 TOOL-dDeclaredLoop-92 TOOL-dDeclaredLoop-93 TOOL-dDeclaredLoop-94 TOOL-dDeclaredLoop-95 TOOL-dDeclaredLoop-96 TOOL-dDeclaredLoop-97 TOOL-dDeclaredLoop-98 TOOL-dDeclaredLoop-99 TOOL-dDeclaredLoop-100 TOOL-dDeclaredLoop-112 |
| [2026-10-24-build-TOOL-dDeclaredLoop-83-deviation-831.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-83-deviation-831.md) | deviation | — |
| [2026-10-24-build-TOOL-dDeclaredLoop-83-deviation-832.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-83-deviation-832.md) | deviation | — |
| [2026-11-15-build-TOOL-dDeclaredLoop-83-1-acceptance-ledger.md](../build/2026-11-15-build-TOOL-dDeclaredLoop-83-1-acceptance-ledger.md) | journal | — |
| [2026-11-15-build-TOOL-dDeclaredLoop-83-deviation-833.md](../build/2026-11-15-build-TOOL-dDeclaredLoop-83-deviation-833.md) | deviation | — |
| [2026-11-15-prompt-TOOL-dDeclaredLoop-83-1-spec-writer.md](../prompts/2026-11-15-prompt-TOOL-dDeclaredLoop-83-1-spec-writer.md) | journal | — |
| [2026-11-15-prompt-TOOL-dDeclaredLoop-83-build-brief.md](../prompts/2026-11-15-prompt-TOOL-dDeclaredLoop-83-build-brief.md) | journal | — |
| [2026-11-15-prompt-TOOL-dDeclaredLoop-83-reground-brief.md](../prompts/2026-11-15-prompt-TOOL-dDeclaredLoop-83-reground-brief.md) | research | — |
| [2026-10-24-review-TOOL-dDeclaredLoop-83-spec-audit.md](../reviews/2026-10-24-review-TOOL-dDeclaredLoop-83-spec-audit.md) | spec-audit | TOOL-dDeclaredLoop-84 TOOL-dDeclaredLoop-85 TOOL-dDeclaredLoop-86 |

<!-- /gen:spec-records -->

## 1. Goal

The round-6 spec audit (`memory/builds/dDeclaredLoop/reviews/2026-10-24-review-TOOL-dDeclaredLoop-80-spec-audit.md`)
confirmed finding **id 1 at HIGH**, in its item **H1**. Item H1 also holds id 7, which is its own unit,
`TOOL-dDeclaredLoop-84`. The medium grade of the same defect is item M1, id 18, batched into
`TOOL-dDeclaredLoop-86`.

`TOOL-dDeclaredLoop-81` S2, at its committed rev-5, names each outcome of the clean re-merge. An exit 1
is `conflicted` and keeps 69 S2's parents branch, and so does `uncomputable`, an octopus merge or a
probed absence of the feature. Every other outcome but an exit 0 printing a tree id is `failed`, graded
by 81 S3 against every parent and never a fall to the parents.
`TOOL-dDeclaredLoop-75` S27 still ends "any other exit code grades against the parents alone with 59
S3's printed line". 75's own consumes-from edge to 81 states the narrowing, so 75's scope body and its
edge give opposite answers. 75 builds at order 39, after 81 at order 20, and a builder who follows S27
puts exit 128 back on the parent exemption: the untrailered unrelated-history fail-open 81 closes.

This unit rewrites S27's fallback clause to 81's outcomes, naming each case that does reach the
parents, and makes 75's own AC27 observe the `failed` route at 75's pass. It builds immediately after
81 and repairs `TOOL-dDeclaredLoop-81`, whose hands-off to 75 left S27's fallback standing.

## 2. Scope (IN)

- **S1** — 75 S27's last clause, from "any other exit code" to the clause's end, is rewritten to §4's
  "The clause S1 writes", as a rev bump of 75 with its §9 line. Three cases grade against the parents
  alone with 59 S3's printed line, as 69 S2 grades them: an exit 1 whose conflicted paths hold the
  policy path, an octopus merge, and a probed absence of `merge-tree --write-tree`. These are 81's
  `conflicted` and `uncomputable` states. Every other outcome is 81 S2's `failed` state, graded by 81 S3
  and refused untrailered, never a fall to the parents: an exit 0 printing no tree id, an exit other
  than 0 and 1, and a re-merge that cannot start. S27's exit-1 body, "its blob parses" included, stays
  as written, because `TOOL-dDeclaredLoop-82` S4 restates that body by that phrase. Each quoted phrase
  of the clause sits on one line of 75, since AC2 and `TOOL-dDeclaredLoop-88` AC1 grep lines.
  Observed by AC1, AC2.
  **Readers:**
  by name: `memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-75.md`, the fallback clause of its S27 scope item; `memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-84.md`, the clause's grep in its S2 and AC2; `memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-86.md`, the clause's grep in its AC1
  by value: `tools/loop/guard.py`, its re-merge reader and push arm, which grade each re-merge outcome as the clause states once 81 S2 and S3 are built
- **S2** — 75 AC27 gains a second observation in the same rev bump, written as §4's "AC27 after this
  unit": at 75's pass, `python guard.py --fixture --plant push-merge-tree-fatal` exits 1 printing
  `the clean re-merge failed: 128`, the plant 81 S5 adds. Its Red when gains a fatal exit falling to
  the parents. 75's `New arm: tools/loop/guard.py` line names the tree-fatal plant beside the
  conflict-elsewhere plant, in the descriptive form that line already uses, staged by routing `failed`
  back to the parents. Observed by AC3.

## 3. Non-goals (OUT)

- 78's states and 82's restatement of S27's exit-1 body, which restate the same rule elsewhere: id 7,
  `TOOL-dDeclaredLoop-84`.
- 59 S3's exit-129 sentence and 81 §4 Evidence's reading of S27: ids 15 and 18, scope items of
  `TOOL-dDeclaredLoop-86`; 81 rev-5's Evidence quotes no S27 clause.
- A computable C whose blob does not parse: 78 S3's finding, which 82 S4 writes into S27's exit-1 body.
- Any change to `tools/loop/guard.py`: 81 builds the states, and S2 only makes 75's pass re-observe one.
- The report's left-shift, a spec-lint check that a spec retiring a rule by quoting a sibling sentence
  bumps that sibling: the class is `memory/gotchas/amendment-leaves-its-other-half-standing.md`, already
  recorded, and AC1 is this instance's grep.

### Edges

- **consumes-from** `TOOL-dDeclaredLoop-81` — the exit table of S2 and S3, its `conflicted` and `uncomputable` states on the parents branch and every other outcome but a tree-printing exit 0 the `failed` state, which S1 writes into 75 S27
- **hands-off** `TOOL-dDeclaredLoop-75` — S27's fallback clause restated to 81's exit table and AC27 re-observing `push-merge-tree-fatal`, which that unit builds at order 39
- **hands-off** `TOOL-dDeclaredLoop-88` — S1's parent rows, §4's S27 table, its Evidence pins and Files touched, which this revision writes as that unit's ids 1, 15 and 27 ask, so its pass re-reads them (the round-7 spec audit's ids 1, 15, 27)
- **hands-off** `TOOL-dDeclaredLoop-90` — S1, which names the policy path that unit reads, and §3's first non-goal, which names 78's states without a count (the round-8 spec audit's ids 5, 26)

## 4. Design

### Evidence

Every claim below was read on `branch/unattended-declared-loop-d56bf0` at `27143aff6`, through
`git show` and `git archive`; this worktree is cut from main at `a76c6afe7`, which lacks the loop kit.
The 75 spec was read at blob `1a094c5b7` and is cited by anchor, never by line.

- 75 §2 S27 reads: "The clean re-merge C is taken from `git merge-tree --write-tree`'s first output line
  on exit 0 or exit 1, and used when the policy path is not among the conflicted paths and its blob
  parses; any other exit code grades against the parents alone with 59 S3's printed line"
  (`memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-75.md`, §2 S27).
- 75 §3's consumes-from edge to 81 reads "every other exit is the failed state, refused untrailered and
  never a fall to the parents", and its consumes-from edge to 83 names S27's fallback clause and AC27's
  re-observation of `push-merge-tree-fatal` (same file, §3 Edges).
- 75 §6 AC27 runs only `push-merge-conflict-elsewhere`, and 75 §7's `New arm: tools/loop/guard.py`
  line names only "the conflict-elsewhere plant", by description and not by plant key (same file, §6
  AC27, §7). The rev-3 text of S2 said that line named the plant key; it does not.
- 81 rev-5 S2 names `uncomputable` as an octopus merge or S1's probe answering false, `conflicted` as an
  exit 1 keeping 69 S2's parents branch "which `TOOL-dDeclaredLoop-75` S27 widens", and `failed` as
  every other outcome: an exit 0 printing no tree id, exit 128, a usage exit 129, a negative exit for a
  signal, or an `OSError` at start. 81 S3 grades `failed` against every parent, each differing key
  owing its trailer and record, and prints `the clean re-merge failed: <detail>`. 81 S5 adds
  `push-merge-tree-fatal`, owed exit 1 by `run_selftest`'s owed map, and 81 AC3 has it print
  `the clean re-merge failed: 128 fatal: fx stand-in`
  (`memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-81.md`, §2, §4 The plants, §6).
- 78 rev-6 S1 names C's states `present`, `absent` and `uncomputable`, and its hands-off to 75 reads
  "its blob parses" as 78 S3's refusal on a computable C that does not parse, never a fall to the
  parents (`memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-78.md`, §2 S1, §3).
- 69 rev-3 S2 keeps 59's grade on the parents branch, read only where 44's combined list names the
  policy file, printing 59 S3's `graded against its parents only` line
  (`memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-69.md`, §2 S2).
- 82 rev-5 S4 replaces S27's "its blob parses" with present, absent or refused, and 82 AC4 greps that
  phrase to 0 over 75 (`memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-82.md`, §2
  S4, §6 AC4). S1 keeps the phrase so 82's edit still has its target. 84 rev-3 S4 has 82 S4 keep S27's
  exit table "as `TOOL-dDeclaredLoop-83` writes it".
- 88 rev-5 S1 narrows the sentence rev-3 of this spec wrote, "Only 81's `uncomputable` C, an octopus
  merge or a probed absence of the feature, grades against the parents", by the exit 1 whose conflicted
  paths hold the policy path; 88 AC1 greps the S27 range of 75 for "conflicted paths hold the policy
  path", greps 75 for "Only 81's" to 0, and greps this spec's "S27 after this unit" range for "policy
  path", at least 2. 88 S31 and AC31 re-anchor this spec's Evidence off line numbers, and 88 S35 names
  the build README in its Files touched
  (`memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-88.md`, §2, §6).
- 90 rev-5 S11 has this spec's S1 name the policy path, and 90 AC22 greps this spec for the
  state-count phrase of 78's opening to 0
  (`memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-90.md`, §2, §6).
- 93 rev-2's exit-claim probe counts every "`--plant push-merge-tree-fatal`" claim across the build's
  specs and expects the set `{1}`; S2 and AC3 here state exit 1
  (`memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-93.md`, §4).
- `tools/loop/guard.py#read_remerge_policy`, built by `TOOL-dDeclaredLoop-59`, answers a parents-only
  reason for every exit but 0, `merge-tree --write-tree exited <n>` among them, and
  `tools/loop/guard.py#check_push_range` prints `graded against its parents only` for it.
  `tools/loop/guard.py#PLANTS` holds neither `push-merge-tree-fatal` nor
  `push-merge-conflict-elsewhere`: the first is 81's, the second 75's. The `loop guard fixtures` leg of
  `tools/gate-legs.json` runs `guard.py --selftest`.
- 69 is order 18, 78 order 19, 81 order 20, 84 and this unit order 21, 75 order 39, 82 order 41, 88
  order 44 and 90 order 45, read from each status header.
- The `gen:build-units` region of `memory/builds/dDeclaredLoop/README.md` renders each spec's rev and
  date, so a rev bump of 75 moves its row; `tools/memory-tree/gen_build_index.py` writes it with
  `--write`.
- `tools/memory-tree/deviation_join.py#derive_joins` joins a departure to the record departing from its
  address. A change to 75 past its audited rev-1, before its first pass, is an audit member at
  `TOOL-dDeclaredLoop-75@rev-1`, and `memory/builds/dDeclaredLoop/build/2026-10-24-build-TOOL-dDeclaredLoop-75-deviation-752.md`
  departs from that address.
- The 75 spec measured 38870 bytes, PINNED 2026-11-15, under the 49152-byte class cap PINNED 2026-11-15
  in `tools/template-size-limits.txt` for `memory/builds/*/spec/`.

### S27 after this unit

```
exit 0 or 1, policy path not among the conflicted paths, its blob parses -> C from the first output line  (82 S4 restates this body)
exit 1 whose conflicted paths hold the policy path                       -> 81 `conflicted`: parents, 69 S2, 59 S3's printed line
octopus merge, or a probed absence of the feature                        -> 81 `uncomputable`: parents, 69 S2, 59 S3's printed line
exit 0 printing no tree id, any other exit, or a re-merge that cannot start -> 81 S2 `failed`, graded by 81 S3, never a fall to the parents
```

### The clause S1 writes

S27 keeps its text through "its blob parses", where its first sentence now ends, and goes on with this
text, wrapped at the spec's width with each quoted phrase of S1 on one line:

```
A merge-tree exit 1 whose conflicted paths hold the policy path, an octopus merge and a probed
absence of `merge-tree --write-tree` grade against the parents alone with 59 S3's printed line, as
69 S2 grades them: 81's `conflicted` and `uncomputable` states. Every other outcome of the re-merge
is 81 S2's `failed` state, graded by 81 S3 and refused untrailered, never a fall to the parents: an
exit 0 printing no tree id, an exit other than 0 and 1, or a re-merge that cannot start.
Observed by AC27.
```

### AC27 after this unit

Both blocks below are indented two spaces here, so no line of this spec reads as its own criterion or
arm; 75 carries them at column 0.

```
  - **AC27** — When `python guard.py --fixture --plant push-merge-conflict-elsewhere` grades a merge whose
    merge-tree exits 1 on a non-policy file while the policy file's two-sided value merged cleanly, it
    exits 0; and `python guard.py --fixture --plant push-merge-tree-fatal` exits 1 printing
    `the clean re-merge failed: 128`.
    Red when: exit 1 drops the clean leg and the value is owed, or a fatal exit falls to the parents.
```

75's guard arm line becomes:

```
  New arm: tools/loop/guard.py · covers AC27 · the conflict-elsewhere plant, staged against the exit-0-only clean leg, and the tree-fatal plant, staged by routing `failed` back to the parents · none
```

### Files touched (estimate)

- `memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-75.md`
- `memory/builds/dDeclaredLoop/README.md`, its `gen:build-units` row for 75: the build README's regions
  are the generator's render, written with `gen_build_index.py --write` and never by hand.

### Alternatives rejected

- **Leaving S27 alone and relying on 81's plants.** The plants catch a literal rebuild only after the code
  is written, and the text keeps contradicting the code for the next change: the finding's consequence.
- **Rewriting S27 whole, the exit-1 body included.** That is 82 S4's edit, by the phrase it greps; doing it
  here moves 82's target and makes two units own one sentence.
- **Moving 75 to an order before 81.** 75 S27 widens 81's states, so 75 depends on 81; the order is right
  and the text is wrong.
- **Writing "Only 81's `uncomputable` C" and leaving the third parent row to 88.** That sentence
  contradicts 81 rev-5 S2, whose `conflicted` state keeps the parents branch, so 75 would carry a
  wrong clause from order 21 to order 44 (§8 F3).
- **Naming the plant key on 75's `New arm:` line.** The line names its plants by description, and the
  `covers` field is the one part a checker reads; S2 keeps the line's form.

## 5. Production-readiness checklist

- security — closes the text route by which exit 128 regains the parent exemption at 75's pass, and
  names the three cases that keep it.
- perf / scale — N/A — a spec text change and one more plant run at 75's pass, seconds.
- error / empty / loading states — N/A — no new state; S27 points at 81's `conflicted`, `uncomputable`
  and `failed`.
- observability — S2 makes 75's pass print `the clean re-merge failed: 128` from 81's plant.
- risks — 82 S4 edits the same scope item at order 41; S1 keeps 82's phrase, and AC2 checks it.
- testing — AC1 to AC3 as greps over the 75 spec; 81's plant is observed at 75's pass by 75 AC27.
- migration — none: 75 is unbuilt.
- user docs — none: no user-facing change; `help/policy.md` is 81's, by its S6.

### Dependencies on units built beside this one

- `TOOL-dDeclaredLoop-81` (order 20) builds first. S1 is written on its committed rev-5 states, and
  75 AC27 runs its `push-merge-tree-fatal` plant at order 39; this pass reads only its spec text.
- `TOOL-dDeclaredLoop-69` (order 18) and `TOOL-dDeclaredLoop-78` (order 19) are next; S1 cites 69
  rev-3 S2's parents branch and 78 rev-6's states as committed, and reads none of their code.
- `TOOL-dDeclaredLoop-82`, `TOOL-dDeclaredLoop-84`, `TOOL-dDeclaredLoop-86`, `TOOL-dDeclaredLoop-88`,
  `TOOL-dDeclaredLoop-90` and `TOOL-dDeclaredLoop-93` read or restate the text this unit writes, as §3's
  edges and §4 Evidence record.
- `TOOL-dDeclaredLoop-112`, `TOOL-dDeclaredLoop-14`, `TOOL-dDeclaredLoop-45`, `TOOL-dDeclaredLoop-4`,
  `TOOL-dDeclaredLoop-46` and `TOOL-dDeclaredLoop-6` are being built or are next; this unit reads none of
  the code they change.

### What the change could newly red

| Artifact | Why | What keeps it green |
|---|---|---|
| `memory/builds/dDeclaredLoop/README.md`, the `gen:build-units` row of 75 | it renders 75's rev and date | regenerated with `gen_build_index.py --write`, held by the `memory hygiene` leg's build-index drift check |
| the departures report, `deviations.py --report dDeclaredLoop` | the pass changes 75 past its audited rev-1 | an audit member at `TOOL-dDeclaredLoop-75@rev-1`, which 75's record 752 departs from, so `derive_joins` joins it and no record is owed |
| check 25 of the `memory hygiene` leg over 75 | the clause sits in a §2 item | it uses no retirement verb, so 75 owes no **Readers:** clause for it |
| the `spec tokens` leg over 75, its size join | 75 grows | 75 sits under the class cap by more than 10000 bytes, PINNED 2026-11-15, and the rewrite adds under 1000 bytes, PINNED 2026-11-15 |
| 82 AC4 and 84 AC3, at their passes | they read S27's "its blob parses" | S1 keeps the phrase |
| 88 AC1 and AC31, 90 AC11 and AC22, at their passes | they read 75 S27 and this spec | this revision writes the text each expects, so each reads green at its pass |
| 93's exit-claim probe | S2 adds a claim in 75 | the claim states exit 1, so the set stays `{1}` |
| `loop guard fixtures` | none: no code moves | 81's plant is re-observed only at 75's pass |

No registry row, usage row, subject pin, verdict-epoch delegate, kickoff manifest watch entry, map file
or install-prefix spelling moves: the pass writes spec text and a generated README region only. A grep
on that branch found no file under `tools/`, `skills/`, `.claude/` or `.githooks/` naming the 75 spec,
and the watch line of `memory/guides/SESSION-KICKOFF.md` names no spec path.

## 6. Acceptance criteria

- **AC1** — When `grep -c "any other exit code grades against the parents alone"` runs over
  `memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-75.md`, it prints 0.
  Red when: S27 still sends exits other than 0 and 1 to the parents.
  figure: it prints 1 at `27143aff6`, PINNED 2026-11-15.
- **AC2** — When `awk '/^- \*\*S27\*\*/,/^- \*\*S28\*\*/'` over the 75 spec is piped to
  `grep -c "never a fall to the parents"`, it prints at least 1; piped to
  `grep -c "conflicted paths hold the policy path"` and to `grep -c "no tree id"`, each prints at least
  1; and at this pass the same range piped to `grep -c "its blob parses"` prints 1.
  Red when: S27 names no `failed` route, leaves the conflicted exit 1 or the empty exit 0 unrouted, or
  the rewrite removed the phrase 82 S4 replaces.
  fixture: the last half holds at this pass only; 82 S4 removes the phrase at order 41, by design.
- **AC3** — When `awk '/^- \*\*AC27\*\*/,/^- \*\*AC28\*\*/'` over the 75 spec is piped to
  `grep -c "push-merge-tree-fatal"` and to `grep -c "the clean re-merge failed: 128"`, each prints at
  least 1, and `grep -c "^New arm: tools/loop/guard.py.*tree-fatal"` over the same file prints 1.
  Red when: 75's pass is never asked to re-observe exit 128 after it widens exit 1.

## 7. Gates

`recall floor` · `recall floor arms` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

This pass writes one spec and a generated README region, no code, and adds no arm. 75's own pass keeps
the `loop guard fixtures` leg green, a leg at HEAD that runs `guard.py --selftest`, where 81's plant is
owed exit 1.

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** RESOLVED (agent, 2026-10-24,
  delegated): `**Derived:** PLAY-dClosedLoop-2`, rung 3, as `TOOL-dDeclaredLoop-36` §8 F1 records.
  widens: none · relaxes: none
- **F2 — Which half of H1's fix is id 1's, and which is id 7's?** Both ids are one defect, and each takes
  a unit. (a) id 1 rewrites 75 S27, the sentence its coherence lens found contradicting 75's own edge;
  id 7 restates the other specs that carry the retired rule, 78 and 82. (b) one unit does both, the other
  only a criterion. (b) leaves one unit with no mechanism. (a) gives two disjoint write sets at one order.
  RESOLVED (agent, 2026-10-24, delegated): (a). widens: none · relaxes: none
- **F3 — Does this unit write S27's parent rows complete, or leave the third to 88?** rev-3 wrote "Only
  81's `uncomputable` C ... grades against the parents", and 88 S1 later adds the exit 1 whose
  conflicted paths hold the policy path.
  - (a) S1 writes all three parent rows and the `failed` outcomes 81 rev-5 names, in words 88 AC1 and
    90 AC11 already read: 75 carries one correct clause from order 21, and 88's S1, S31 and S35 find
    their text written at their pass.
  - (b) S1 keeps rev-3's sentence and 88 narrows it at order 44: 75 contradicts 81 rev-5 S2 between
    the two passes, the defect this unit exists to close.
  Recommendation: (a). The body is written on it.
  RESOLVED (agent, 2026-11-15, delegated): (a), rung 3: the clause matches 81's committed states at
  this pass, so no order carries a contradicted S27
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, promoted from the round-6 spec audit's id 1 (HIGH, item H1, shared
  with id 7).
- rev-2 · 2026-10-24 · §3 · the Edges block gains the bullet mirroring the edge of
  TOOL-dDeclaredLoop-88, written by the round-7 spec audit's disposal; nothing else moved.
- rev-3 · 2026-10-24 · §3 · the Edges block gains the bullet mirroring the edge of
  TOOL-dDeclaredLoop-90, written by the round-8 spec audit's disposal; nothing else moved.
- rev-4 · 2026-11-15 · §1 · S1 S2 · §3 · §4 · §5 · AC1 AC2 AC3 · §7 · §8 · §10 · re-grounded on
  branch/unattended-declared-loop-d56bf0 at `27143aff6` by the brief
  2026-11-15-prompt-TOOL-dDeclaredLoop-83-1-spec-writer; mechanism, carries, order and status kept.
  Written on TOOL-dDeclaredLoop-81 rev-5 and TOOL-dDeclaredLoop-78 rev-6: S1 names the three parent
  cases, the conflicted exit 1 among them, and the `failed` outcomes, an empty exit 0 included (F3);
  S2 names the tree-fatal plant in the descriptive form 75's arm line uses; §4 cites 75 by anchor
  and gives the clause and AC27 as written; §5 names the dependencies and what could red; the Files
  touched gain the build README's generated region.
- rev-5 · 2026-11-15 · §2 S1 · S1's Readers clause names the grep in TOOL-dDeclaredLoop-84's S2 and AC2, where that unit's rev-4 moved it; nothing else moved.

## 10. Reuse audit

The seam is 75 S27 itself, amended in place as a rev bump; no new spec text duplicates 81's table, which
S1 points at. The class is `memory/gotchas/amendment-leaves-its-other-half-standing.md`, whose fixture is
a grep-0 criterion over the sibling, which AC1 is. The `supersede` join of
`tools/check-spec-tokens.py#scan_supersede` refuses a spec overriding a sibling's text from outside; this
unit rewrites the sibling itself, the remedy that join names, so it extends nothing there.
`python tools/codebase-map/reuse_lookup.py "amend a sibling spec scope item so a retired rule has no stale reader"`,
run on this worktree's main tree on 2026-11-15, ranked `read_text`, `read`, `read_bytes`, `scope` and
`read_policy_value`, none of which edits or checks a sibling spec, so no existing seam fits beyond the
spec itself. The memory-recall query returned the gotcha above, `TOOL-dDeclaredLoop-84`'s and this
spec's own §10, and `TOOL-dTieredTribunal-24`, an open ask for mechanical arms for the class, which
this unit does not build.

Recall terms used: amendment other half standing sibling spec stale clause rev bump grep-0 criterion retired rule
