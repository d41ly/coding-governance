**Serves:** research PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-49

# Brief: unit 19's divergence — which text the citation check grades

## The prompt

> dOrderedCharter

— owner, 2026-11-02, invoking `/unattended` for the build run. Unit 19's builder (run wf_63e33fb3-61f) returned
`DIVERGENCE:` before writing code. §4 "The index" scans every tracked .md, .py, .sh, .js, .toml and .json file for any
`TAG_RE` token in a registered namespace; S7 `resolves` reds every one that resolves to no row, with no base
restriction; §4 Rollout makes the leg live over gov's tree at landing. At HEAD `394fc76f6` a grep of that shape finds
103 `doc.*` tokens in 30 files no `doc` row resolves (code such as `doc.get(` in `tools/policy/policy.py`, planted or
planned tags in frozen build records, dClosedLoop instrument blobs), and about 200 `unit.*` tokens in a namespace S3
prints `unarmed`.

## The brief

### Goal

Revise spec 19 so its `tags` leg is green over gov's tree at landing and still reds a bad citation in new text, and
fold the builder's three side findings.

### Items

1. **Which text is graded (§4 "The index", S7, Rollout, §7).** Decide by M3 between at least: (a) a citation is only
   a token in citation syntax (a backticked or bracketed token in Markdown; never a code identifier); (b) `resolves`
   grades only citations absent from the base tree `resolve_compare_base` reads, as `retired` already does; (c) both.
   Ratify the most feature-rich survivor; record the loser and the observation that rejected it (M12) in §8 as a
   resolved fork, delegated. Run the candidate predicate over the real tree and write the count it leaves red into
   §6 (it must be 0 for the leg to land green; the `doc.no-such-doc` plant of §7's first `New arm:` must still red).
2. **An unarmed namespace (S3, S7).** Say whether a citation into a namespace S3 prints `unarmed` is graded or
   skipped, and how the skip is printed (a count, never silence: charter `[gate]`).
3. **`derive_baseline_additions` (S9).** It calls codebase-map's `map_root` and `load_conf` (`map_lib.py:214`) and
   raises `MapError`, so moved as written the core would read an optional kit's conf. Fold PLAY-dOrderedCharter-49's
   S38 and AC29 into spec 19's S9 and its ACs now (BUILD-METHOD M4: a repair corrects an unbuilt sibling's spec), and
   revise spec 49 to drop S38 and AC29 with a §9 line pointing at spec 19, keeping its id and every other item.
4. **`resolve_compare_base`'s home (S9).** Its canonical is `tools/lib/compare_base.py`, carried in map_lib as the
   `compare_base_py` copy; say that `coverage_join.py` carries a `compare_base_py` copy, not that it is canonical.
5. **Stale citations.** map_lib's `resolve_compare_base` is at `:1507` and `derive_baseline_additions` at `:1544`; the
   run-gates canary's known-key sets are at `run-gates.test.sh:364` and `:700`. Re-verify every other line spec 19
   cites at HEAD.

In every spec you revise:

- Bump the **Status:** rev by one, dated 2026-11-03, the status kept `DEFERRED`, and add one §9 line naming this brief.
- Verify every path, count and line you cite against the tree at HEAD.
- Stay under the 47000-byte authored budget.

For the run:

- Writes stay in specs 19 and 49 and the files `gen_build_index.py --write` rewrites.
- This is an unattended run and nobody answers a question: a fork no option survives is written as an open §8 item
  with the options and the veto, and said in the return.
- Do not commit and run no check: the main loop re-renders the packet, runs the spec-token check, renders the index
  and commits.
- Scratch files go under the session scratchpad
  `C:/Users/DAILY-~1/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unattended-dorderedcharter-725f52/0394fa33-012c-408f-a840-e6e4cfaac23f/scratchpad`.
- Return each spec's new rev, the §8 decision with its loser, and the red count item 1's predicate leaves over the tree.

### Acceptance

- Spec 19's §6 carries the red count of item 1's predicate over the tree, and it is 0.
- `grep -n 'S38\|AC29'` over spec 49 prints only its §9 line and any pointer to spec 19.
- Each revised Status line is one rev higher, and §9 holds the new line.

### Gates

The spec-token check, run by the main loop before the commit.

### Non-goals

No code; no spec but 19 and 49; no edit of a frozen record or a dClosedLoop instrument to make the tree green.

### Limitations

The items above, "For the run".

### Reuse

`retired`'s base comparison through `resolve_compare_base`; `tools/lib/compare_base.py`; `TAG_RE` as spec 19 defines it.
