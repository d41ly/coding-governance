**Serves:** research TOOL-dFurnishedOrders-2 TOOL-dFurnishedOrders-3 TOOL-dFurnishedOrders-5 TOOL-dFurnishedOrders-6 TOOL-dFurnishedOrders-7 TOOL-dFurnishedOrders-8 TOOL-dFurnishedOrders-10 TOOL-dFurnishedOrders-11 TOOL-dFurnishedOrders-12 TOOL-dFurnishedOrders-14 TOOL-dFurnishedOrders-15 TOOL-dFurnishedOrders-16 TOOL-dFurnishedOrders-17 TOOL-dFurnishedOrders-18 TOOL-dFurnishedOrders-20 TOOL-dFurnishedOrders-29 TOOL-dFurnishedOrders-37 TOOL-dFurnishedOrders-42 TOOL-dFurnishedOrders-46 TOOL-dFurnishedOrders-48 TOOL-dFurnishedOrders-50 TOOL-dFurnishedOrders-58

# Brief: dFurnishedOrders' specs re-grounded against dBoundRoles' landed specs

## The prompt

> Have `gov-spec-writer` agents revise only the mismatched specs. The main loop never edits a spec.

— the dClosedLoop re-ground session's hand-off to this session, 2026-10-28, relaying the owner's hold
on the dependent spec runs until the third wave's children are re-grounded.

## The brief

### Goal

Revise the 22 dFurnishedOrders specs that the cross-check record names under "For the re-ground".
Each one should state its parents' surfaces the way their specs now spell them on origin/main at
`1a61f21a2`: dBoundRoles as its re-ground `ac8ab8d5f` left it, dTotalRecall as `794a0f5fb` left it,
dKeptSession as `ff44fb2a2` left it, and the rules dOrderedCharter, dDeclaredLoop, dWitnessedBar and
dPlacedRequest apply to every spec. Each spec keeps its own design, and only its assumptions about the
parents change.

### Items

Read the cross-check record first,
`memory/builds/dFurnishedOrders/build/2026-10-28-build-TOOL-dFurnishedOrders-1-parents-crosscheck.md`.
Its summary table numbers every assumption (rows 1 to 127). Section 2 of each group's return in
`memory/builds/dFurnishedOrders/build/2026-10-28-build-TOOL-dFurnishedOrders-1-crosscheck-returns.md`
quotes both sides of each MISMATCH and states its `Change:`. Read each parent spec the record cites, at
the lines it cites. This brief summarises them, and where the two differ, the specs win. Before you
edit for a row, re-read both sides. A row the parent's text does not bear out is not edited: return it
as refused, with the line that refutes it.

Facts every revision uses:

- **A catalogue-default read.** `read_policy_setting(key, root)` (br21 S1) is the roles kit's one
  runner of `policy.py get`, found through `resolve_kit_dir("policy", "policy.py", here)`; it returns
  None both for a key at its catalogue default and for no policy kit found, and its `with_default`
  argument is the form a read with a catalogue default takes (br21:41-50). br43 S21 makes every caller
  use `with_default` where it reads the catalogue default, and says no file under `tools/roles/` runs
  `get` outside it or imports the policy kit (br43:105-110); br43 AC21's predicate is
  `git grep -n -E "policy\.py.*get|from policy import|import policy" -- 'tools/roles/*.py'`
  (br43:427-429). With `with_default=True`, None means only that no policy kit was found: a spec keeps
  a typed value only as that fallback, with its note, and drops the roles-kit copy of the default.
- **A sibling kit.** A kit imports no sibling kit (TOOL-dGroundRules-1 §4; oc7:202-205). A by-file load
  (`importlib`, `spec_from_file_location`, `load_kit_module`) or a `sys.path` insert of another kit's
  directory is an in-process import. Code in one kit reaches another kit's verb by subprocess, found
  through the inline `resolve_kit_dir`; br12, br14, br20 and br43 are the precedents for adding a verb
  to the kit that owns the data. A hook spawns `node <policy kit>/policy-mirror.js get <key>` instead of
  `require`-ing it (ks8:62-66). Where the verb does not exist, write a §8 fork open for the owner: an
  ask to the owning build for the verb, or a declared `requires_if` row on `tools/roles/kit.toml`
  (today it holds one only for review-harness, `tools/roles/kit.toml:19`), with the reason the rule
  admits it. Recommend one.
- **A leg.** oc7 S3 reds a leg with no `enforces` (oc7:58-63). wb11 declares each leg once, in its kit's
  `[[gate_leg]]` row or a `tools/govkit/registry.toml` `[[exempt_leg]]` row holding every manifest key,
  `enforces` among them; `leg_factory.py --write` renders `tools/gate-legs.json`, and `--check` reds a
  manifest that differs (wb11:36-49, :154). `govkit selftest` is the `[[exempt_leg]]` row at
  `tools/govkit/registry.toml:439`: a spec that re-guards it edits that row and renders. The
  `answered-calls self-test` leg is declared once, by fo6 S9, with `leg_factory.py new` and a named
  `enforces`; fo29 S19 and fo37 S24 re-guard that declaration. An AC reads the rendered row or
  `leg_factory.py --check`. Where `leg_factory.py` is not built at the pass, the pass records that a
  hand edit stood in for it.
- **br3's `--item` render.** br3 S1 runs `loop_lib.py declaration --item <tag> --json` in a subprocess,
  and a tag the loop does not declare or no loop kit found refuses with exit 1 and writes nothing
  (br3:39-47). A stub `loop_lib.py` in a fixture answers `declaration` as well as `seed`. The verb
  itself is br3 F5's open ask to dDeclaredLoop.
- **An ask.** No dFurnishedOrders spec files a row in another build's `BACKLOG.md`. Where a fix needs a
  parent change, write a §8 fork open for the owner, with its options and a recommendation, and name
  the ask the build run would file.

Groups, one writer each. The spec your handoff's `input:spec` names leads one group. Revise every spec
of that group, and no other:

- **Group A, catalogue defaults, led by spec 2:** specs 2, 5, 8, 16 and 18.
- **Group B, policy reads and the loop render, led by spec 17:** specs 7, 11, 12, 17 and 20.
- **Group C, the roles kit's cross-kit loads and the `answered-calls` leg, led by spec 29:** specs 3,
  6, 10, 14, 29, 37 and 42.
- **Group D, the `govkit selftest` leg and the tester template, led by spec 46:** specs 15, 46, 48, 50
  and 58.

The spec files are `memory/builds/dFurnishedOrders/spec/2026-10-2?-spec-TOOL-dFurnishedOrders-<n>.md`.
Write probe copies, such as a `GIT_INDEX_FILE` index copy, only under
`C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-beautiful-lalande-23ce8b/a46c346a-6f74-4403-a01d-0c3480a8d930/scratchpad/fo-w<group letter>/`,
and delete nothing else there. Return, per spec: the rev it now reads; the sections moved; each fork
you added or re-resolved, with its mark; each record row you refused, and why; its byte count; and any
parent spec that looks wrong.

Per spec, by the record's rows; each row's `Change:` in the returns record is the starting point:

1. **Spec 2** (row 6). `prompts.batch` read with `with_default=True`; the roles-kit `per-batch` copy
   goes; F3 keeps its no-kit meaning.
2. **Spec 5** (row 19). Both keys read with `with_default=True`; `keyed` and `cold` stay only as the
   no-policy-kit fallback, with a note.
3. **Spec 8** (row 35). `instructions.slices` read with `with_default=True`; the typed `handed` goes.
4. **Spec 16** (row 63). `attendance` read with `with_default=True`; a no-kit None takes S1's
   `unread: <why>` path.
5. **Spec 18** (row 77). `annotations.delivery` read with `with_default=True`; the literal stays only
   for the no-kit None.
6. **Spec 7** (rows 32, 33). `roles.on-contradiction` through `read_policy_setting(...,
   with_default=True)`; the backlog rows rendered through a memory-tree verb by subprocess, or the fork.
7. **Spec 11** (rows 46, 47). Both keys through `read_policy_setting(..., with_default=True)`; the
   ledger registrations read through a memory-tree verb by subprocess, or the fork.
8. **Spec 12** (rows 50, 51). F1's probe re-pinned to a content-anchored grep over br1's roster table;
   both keys through `read_policy_setting(..., with_default=True)`.
9. **Spec 17** (rows 68, 71, 72, 73). The Edges bullet names asks TOOL-dTotalRecall-102 and -103 as what
   would make tr8 land the `neighbourhood` reader; AC2's stub answers `declaration --item`; the
   no-loop-kit branch goes from the `--item` path; both keys through `read_policy_setting(...,
   with_default=True)`, the AC1 fixture line reworded from `resolve` to `get`.
10. **Spec 20** (rows 86, 88). The no-loop-kit branch goes from the `--item` path; `read_claims` passes
    both `refs/gov/leases` and `refs/gov/runs` to a namespace reader that fetches a list in one bounded
    fetch (pr1:76-80).
11. **Spec 3** (rows 11, 12). `notices.record` read by `policy.py get` by subprocess; runlog reached
    through a runlog verb by subprocess, or a declared `requires_if` row.
12. **Spec 6** (rows 26, 27). `answered-calls self-test` declared once with `leg_factory.py new` and a
    named `enforces`, rendered by `--write`, with a `--check` criterion; `answered-calls.js` spawns
    `policy-mirror.js get roles.answered-calls`.
13. **Spec 10** (row 43). F3 re-resolved to a runlog verb run by subprocess; S7 reads the matrix
    through `loop_items.py matrix --json`.
14. **Spec 14** (row 55). Open repair asks read through a memory-tree verb by subprocess, or the fork.
15. **Spec 29** (rows 98, 99, 104, 105, 107). S9's five keys with `with_default=True`, and its end
    state restated as no `get` run or policy import outside `read_policy_setting`; AC7 takes br43
    AC21's predicate; AC8's stub logs its verb and counts `seed` lines; S6 and S11 reach runlog and the
    playbook kit by subprocess verbs or declared `requires_if` rows; S19's guard sits on fo6 S9's
    declaration and is rendered.
16. **Spec 37** (rows 113, 114). S2's check also flags by-file loads of another kit's file that no
    `requires_if` row admits; S24's guard sits on the declaration.
17. **Spec 42** (row 120). The cap read through a policy-kit verb by subprocess, or the fork; the
    `sys.path` insert goes.
18. **Spec 15** (row 60). The tester template keeps br2 F4's `answered` outcome and `answer:text?`
    beside `designed` and `judged`; the body returns `answered` for `test.reason`.
19. **Spec 46** (rows 122, 123). S8's guard files go on the `govkit selftest` `[[exempt_leg]]` row and
    are rendered; S5 runs the lexicon check through a lexicon verb by subprocess, or the fork.
20. **Specs 48, 50 and 58** (rows 124, 126, 127). Each guard or home-row edit goes on the `govkit
    selftest` `[[exempt_leg]]` row at `tools/govkit/registry.toml:439` and is rendered by
    `leg_factory.py --write`; Files touched gains the registry; fo58 S25 says the declaration, the
    render and the waiver rows land in one commit.

In every spec you revise:

- Bump the **Status:** line's `rev-N` to `rev-N+1`, dated 2026-10-28, the status kept `DEFERRED`.
- Add one §9 line naming the sections moved and the cross-check record, with its row numbers.
- Replace each now-false sentence where it stands.
- A resolved fork whose chosen option a parent now rules out is re-resolved on rung 1, naming the
  parent, and marked `RESOLVED (agent, 2026-10-28, delegated)`. A fork this brief tells you to leave
  open for the owner stays open, with its recommendation. Re-open no other fork.
- Spell a `tools/` path inside an acceptance criterion as the spec already does.
- Stay under the class cap of 49152 bytes; replace text rather than append where a spec is near it.

### Acceptance

- `wc -c <spec>` is under 49152.
- The **Status:** line reads `rev-<N+1>`, and §9 holds the new line.
- For each record row your spec answers, `grep -n` for the sentence the row quotes from `foN:L`
  prints nothing, or prints only the corrected sentence.
- `bash tools/memory-tree/check-memory-hygiene.sh --staged`, run over a copy of the index with only
  your specs staged into it through `GIT_INDEX_FILE`, names none of your specs. Delete the copy
  after. Findings that only a `gen_build_index.py --write` render cures belong to the main loop:
  name them and leave them.

### Gates

Only the memory hygiene gate and the naming lexicon, as the role allows. The main loop runs the rest
and renders the index.

### Non-goals

- No file outside the spec files of your group. No commit, no stage into the real index, no deviation
  record: the main loop writes those.
- No file of dBoundRoles, dTotalRecall, dKeptSession, dOrderedCharter, dDeclaredLoop, dWitnessedBar,
  dPlacedRequest, dSafePassage or dGroundRules. A parent spec that looks wrong is a line in your
  return, not an edit.
- No change to what a unit builds beyond what the re-ground forces.

### Reuse

The parents' specs as the interface. The cross-check record as the map of what moved. dBoundRoles'
re-ground brief,
`memory/builds/dBoundRoles/prompts/2026-10-26-prompt-TOOL-dBoundRoles-1-parents-reground.md`, and its
revised specs, as the precedent for how a revised spec reads.
