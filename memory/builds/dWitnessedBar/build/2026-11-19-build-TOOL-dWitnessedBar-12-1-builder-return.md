**Serves:** journal TOOL-dWitnessedBar-12

# TOOL-dWitnessedBar-12 — builder return 1 (run `wf_c82b9ed0-6cc`), a divergence, nothing committed

## Why

DIVERGENCE: The spec does not design how `check` reds a duplicated leg tag, but AC3 needs it to. AC3 says that under `gov_tag.py --fixture --plant leg-dup` (two rows with one tag), `check` exits 1 naming the tag, and it is red when "a duplicate passes". Nothing in the design produces that red.

1. **No mechanism for AC3.** S3 adds only extractors: `extract_leg` yields one member per row's tag. §3 then rules the shape check, the index and the join factory out of scope. I read every red site `run_check` reaches in tools/playbook/gov_tag.py and tools/playbook/tag_index.py:
   - `check_tag_shape`, `check_namespace_joins`, `check_resolves`, `check_retired`, `check_owned`, `check_namespace_purpose` and `check_unclosed` grade shape, joins, resolution, retirement, ownership, purpose and fences. None of them compares one defining row's tag against another's.
   - `check_namespace_joins` keeps only the first declaration (`declared.setdefault`).
   - `run_name_check` collapses its input through `sorted(set(tags))`.
   - The `two-paths` plant shows one tag defined at two paths is legal in the index.
   So a manifest with two equal `tag` values reads green under `check`. To meet AC3 the spec has to name the mechanism. Options: a duplicate-definition arm in `check` (a change to the shape or join check, which §3 currently excludes, so §3 must admit it and say which namespaces it covers), or some other stated route. Otherwise AC3 should move its duplicate half to the gov canary arm S7 already owns (AC1 covers that canary), and §5's "a duplicate or malformed tag reds the gov canary" stays the only duplicate claim. Building around this would mean inventing a check the spec excludes, so I stopped.

2. **Files touched is missing `tools/playbook/adopt-playbook.sh`.** §7's third `New arm:` line puts the arm there: the playbook-render selftest running the four plants. Those plant rows go into its `run_plant_rows` heredoc, so the file must change, but §4 Files touched does not list it.

3. **§5 observability is not true of current code.** It says "`gov_tag.py check` prints each namespace's member count". `run_check` prints only totals (`N namespaces, N tags`), the `joins · N armed` line and `unarmed` lines. No unit item adds a per-namespace count, so either §5 is rewritten or an item is added.

For the dispatcher, not the spec: the declared write set (RUN.md line 107) leaves out the 27 descriptors that §4 Files touched lists and S1 needs. A re-dispatch should declare them.

What still holds against the tree at base cbad1ae7:
- 198 manifest rows with 0 tags; 70 `[[gate_leg]]` rows in 27 descriptors; 128 `[[exempt_leg]]` rows.
- The tag rule gives 198 unique tags, 6 cut, and only `leg.policy-kit.policy-check` needs F9's suffix. Both readings of the cut rule give identical tags.
- Both `KNOWN` literals are at tools/run-gates/run-gates.test.sh@20bb181a:409 and :830 with the 15 keys; `read_known_copies` and its "two KNOWN copies that differ" case exist; the four `*_FLOOR_RUN_GATES` constants exist; `KIT_RUN_GATES_VERSION=1.50`; `REGISTRY_FIELDS`, `ROW_TAG_KEYS`, `extract_command` and the 15 namespace rows match what the spec says.

Nothing was written, staged or committed. The brief was already recorded (a9485773206b).

## Summary

I built nothing on TOOL-dWitnessedBar-12: the spec can't be built as written, so I stopped before the first edit. The worktree is clean at base cbad1ae7192aba9b504d3fb03817b7317c815640 and there is no commit.

**The blocker:** AC3 requires `gov_tag.py check` to exit 1 when two leg rows share one tag (the `leg-dup` plant). No current check does that, and the spec neither designs one nor allows one: §3 puts the shape check, the index and the join factory out of scope. Two smaller spec problems go into the same divergence:
- §4 Files touched leaves out `tools/playbook/adopt-playbook.sh`, which §7's new arm has to edit.
- §5 says `check` prints each namespace's member count; it prints only totals.

Separately, the main loop's `--dispatch` write set left out the 27 descriptors the spec lists, so a re-dispatch should declare them.

**What ran:** only read-only probes. I read the build method, brief and spec in full and checked the spec's claims against the source with grep/sed. The tag-rule probe (a `python` script over `tools/gate-legs.json`, the govkit registry, the descriptors and `tools/playbook/namespaces.toml`) gave 70 descriptor-owned legs in 27 descriptors, 128 exempt, 198 unique tags, 6 cut, and one namespace-word owner (`policy`). That matches the spec's pinned figures and stands in for the shape and uniqueness part of AC1. A second probe confirmed both readings of the cut rule give the same tags.

**What didn't run:** no gate, suite or bar, by mandate. `gotchas.py --for-diff` didn't run either, since there is no commit for it to read.

**Owed to the close once the unit is rebuilt:** AC5's `owed_rows.py --selftest`, and the red-first observation of the four `New arm:` lines: `tools/run-gates/run-gates.test.sh`, `tools/run-gates/run-gates.gov.test.sh`, `tools/playbook/adopt-playbook.sh` and `tools/govkit/selftest.py`.

Files: C:/projects/coding-governance/.claude/worktrees/unattended-dwitnessedbar-2ed3b3/memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-12.md, C:/projects/coding-governance/.claude/worktrees/unattended-dwitnessedbar-2ed3b3/tools/playbook/gov_tag.py, C:/projects/coding-governance/.claude/worktrees/unattended-dwitnessedbar-2ed3b3/tools/playbook/tag_index.py.
