**Serves:** research PLAY-dOrderedCharter-38

# Brief: fold drift sweep A into specs 47, 48, 25 and 7

## The prompt

> execute keeping the build unattended

— owner, 2026-11-03, approving the run's drift sweep (`prompts/2026-11-03-prompt-PLAY-dOrderedCharter-38-owner-speedup.md`). The sweep's
reviewer read specs 47, 48, 25 and 7 against the tree at `06e612222` and returned the findings below, every one with a tree path
and line. This pass folds them before those units dispatch, so their builders do not hand back a divergence.

## The brief

### Goal

Revise specs 47, 48, 25 and 7 so each matches the tree at HEAD on every finding below.

### Items

1. Fold every finding below into its spec. Re-verify each cited path and line at HEAD before writing it: units may
   have landed since the sweep read the tree.
2. A finding marked NEW MECHANISM is a fork: decide it by M3, and record the loser and the observation that rejected
   it (M12) in §8, delegated.
3. **A new leg's own rows.** Every new leg's rows are written in its own pass, the way unit 26 rev-7 writes
   `tags positional selftest`'s. Those rows are the dossier claim in `memory/map/features/playbook.md` (with
   `memory/map/generated/*`, which the map generator rewrites), the `tools/govkit/subject-pins.tsv` row, and the claiming row.
   - For a leg an adopter cannot carry, the claiming row is an `[[exempt_leg]]` row in `tools/govkit/registry.toml`,
     as units 16, 19 and 28 wrote at `:707`, `:711` and `:715`.
   - Otherwise it is a `[[gate_leg]]` row in the kit's `kit.toml`.
   - Files touched lists those paths, and §7 names the legs they trip. Check them with
     `python tools/check-spec-tokens.py --legs-for <path>`.
4. **`enforces` into `principle.*`.** The main loop decided this across the sweep. Unit 7, at order 11, adds `principle` to the
   `enforces` row's `to` in `tools/playbook/edges.toml` in its own pass. Units 13 and 12 consume that through a §3 Edges line.

In every spec you revise:

- Bump the **Status:** rev by one, dated 2026-11-03, with the status kept `DEFERRED`.
- Add one §9 line naming this brief.
- §7's leg line names every leg whose guard a Files-touched path trips.
- No AC observes a suite, a bar or a gate leg.
- Stay under the 47000-byte authored budget.
- An H1 names another build's unit as "<build>'s unit N", never by its id.

For the run:

- Writes stay in specs 47, 48, 25 and 7 and the files `gen_build_index.py --write` rewrites.
- This is an unattended run and nobody answers a question. A fork that no option survives is written as an open §8 item
  with the options and the veto, and said in the return.
- Do not commit and run no check. The main loop re-renders the packet, renders the index and commits.
- Scratch files go under the session scratchpad
  `C:/Users/DAILY-~1/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unattended-dorderedcharter-725f52/0394fa33-012c-408f-a840-e6e4cfaac23f/scratchpad`.
- Return each spec's new rev, each §8 decision with its loser, and any finding you did not fold, with the reason.

**The findings.**

Cross-cutting: specs 25 and 7 add legs but omit the rows unit 50 says a new leg owes in its own pass (dossier claim in memory/map/features/playbook.md + memory/map/generated/, tools/govkit/subject-pins.tsv, tools/playbook/kit.toml [[gate_leg]], ceiling-evidence.txt) and the legs those paths trip (recall floor, recall floor arms, govkit selftest, govkit refusal join). Specs 47 and 48 aim their positional plants at the playbook-render selftest; unit 26 rev-7 runs them in its `tags positional selftest` leg.

**Spec 47.**
- 47-1 §7 New arm names tools/playbook/adopt-playbook.sh + playbook-render selftest for `positional-forked-before`; that file is not in Files touched; gov_tag plants run via `run_plant_rows tags` (adopt-playbook.sh:258) and PLANTS tuple (gov_tag.py:317). Unit 26 rev-7 §3 Edges places 47/48/53 positional plants in `tags positional selftest`. Re-point the arm there (or add the file).
- 47-2 §5 user docs edits tools/playbook/README.md, not in Files touched (its legs already on §7). Add it.
- 47-3 §5 risk says a re-added record is graded from its new add; tree_lib.py:303/:324 keeps the OLDEST add, so it is graded from the original add. Restate.

**Spec 48.**
- 48-1 Same as 47-1 for `positional-producer-new`/`-stale`; also tools/playbook/README.md missing from Files touched.
- 48-2 §4 cites tools/hooks/README.md:119; the file:line text now sits at :130.
- 48-3 §4 Evidence candidate lines moved: tools/workflows/README.md:489→:498, :522→:531; tools/workflows/REVIEW-PROTOCOL.template.md:193→:155; tools/workflows/check-review-join.test.sh:159→:279. Re-point or mark as base lines (41-hit count still holds at HEAD).

**Spec 25.**
- 25-1 S1/§4/§10: bundle reads "every inbound edge `gov tag refs` returns, grouped by edge type"; `refs` (gov_tag.py:98-106) returns only span citations {path,line}, no edge type. Typed edges come from edge_grammar.read_tree_edges (edge_grammar.py:560), derive_inverse_edges (:672), resolve_edge (:493). Re-point the read; refs supplies only the `cites` view.
- 25-2 S5/S6/§4/Files touched: unit 28 already ships both checks — check_edges (edge_grammar.py:396, unregistered type) and run_resolve (:537, unresolved target), under the `edges (...)` leg in the tags pack, plants from :731. Drop tools/playbook/edge_checks.py; the two `--only` arms call check_edges and run_resolve; mirror into unit 55's hands-off.
- 25-3 S5 "cites, derived, is never declared and never graded": a declared cites is red (edge_grammar.py:411-413, plant `declared-cites` :733). Restate as unit 24's rule.
- 25-4 AC1/AC7: edges.toml:54-58 registers `instructs` to=["selects"]; check_edges (:430) reds a target outside a selects namespace; doc is a describes namespace. Plants must address a selects-namespace tag.
- 25-5 AC1/AC6/AC7 name doc.fixture; unit 19's fixture defines doc.alpha (gov_tag.py:448,668; memory/guides/ALPHA.md :444). Use doc.alpha or state the guide the bundle cases add.
- 25-6 New leg `tags bundle selftest`: owed rows and legs per the cross-cutting note (unit 50 §4 at spec-50:131-136; playbook.md:11 shows units 19/28 claimed theirs in their own passes).
- 25-7 §4 Rollout "after units 19, 24 and 28" — §3 consumes tools/run-gates/owed_rows.py from unit 50 (absent at HEAD); add unit 50 to the ordering.

**Spec 7.**
- 7-1 S3/§3/§10: compute_coverage is not "inline under a PARITY_ROWS row" nor at map_lib.py:1404; canonical tools/lib/coverage_join.py:46, copy tools/memory-tree/coverage_join.py:49, parity row is a module copy (tools/lib/resolve-python.test.sh:370, :402-405); tag_index.py:984 does `from coverage_join import compute_coverage`. core.py imports it the same way.
- 7-2 S2 writes principle.p28/p16 into a leg's `enforces`; edges.toml:63-70 registers enforces to=["unit","practice"]. Widen `to` with principle in this pass (add edges.toml to Files touched).
- 7-3 Five new legs (core meta-check, core kinds, core skills conformance, core practices conformance, core selftest): owed rows and legs per the cross-cutting note.
- 7-4 §10 deviation_join.py lines: FIELD :145→:150, RECORD_NAME :160→:165, read_record :212→:217, read_records :268→:273.
- 7-5 §1 "142 rows of tools/gate-legs.json": 151 today; pin the count or re-derive.

### Acceptance

- Each finding above is either folded, or listed in the return with the reason it was not.
- Each revised spec's Status line is one rev higher, and its §9 holds the new line.

### Gates

The spec-token check, run over the tree by the next `--dispatch`.

### Non-goals

- No code.
- No spec outside the four above.
- No finding about another spec.

### Limitations

The items above, "For the run".

### Reuse

Unit 26 rev-7's owed-row shape (its Files touched, §7 and AC12). `tools/playbook/edge_grammar.py`'s readers and checks.
`tools/playbook/policy_value.py`.
