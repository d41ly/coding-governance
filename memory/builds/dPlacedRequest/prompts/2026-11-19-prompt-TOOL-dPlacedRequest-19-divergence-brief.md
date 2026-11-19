**Serves:** research TOOL-dPlacedRequest-19

# Brief — dPlacedRequest: TOOL-dPlacedRequest-19's divergence, resolved

## The prompt

> /unattended dPlacedRequest

## The brief

### Goal

TOOL-dPlacedRequest-19's builder returned a DIVERGENCE (run `wf_a2854136-6ae`) and committed nothing: at rev-6 the
spec's second `New arm:` line names `tools/loop/selftest.py`, a file not in the tree that no leg in
`tools/gate-legs.json` runs, so the AC1/AC7 arm would be a check the bar never runs; §5 says no help page describes the
driver's verbs while §4 Files touched names `help/loop.md`; and S4's "the same bounded fetch" reads two ways. Revise
the spec to the main loop's three rulings so it can be built as written.

### Items

1. F-arm, the loop arm's home. Add to §8, resolved: "Where do the AC1/AC7 plants run, when the loop kit has no `selftest.py`?" (a) `tools/loop/request.py --selftest`, run by a new gov leg (a name such as `loop request fixtures`, chunk `selftests`, subject `kit`, as the leg `loop claims fixtures` runs `claims.py --selftest`); (b) the plants move into an existing loop module's self-test. Mark `RESOLVED (agent, 2026-11-19, delegated): (a), rung 3; the loop kit's one convention is a module carrying its own self-test run by its own leg, and request.py is a new module. widens: none · relaxes: none`. Amend the second `New arm:` line to `tools/loop/request.py`, add `tools/loop/selftest.py` nowhere, and add to §4 Files touched every path a new leg registers in, as the tree's existing loop legs show them: `tools/gate-legs.json`, `tools/govkit/registry.toml`, `tools/govkit/subject-pins.tsv`, `memory/map/features/loop.md` and `tools/run-gates/selftest-budgets.txt` (verify each against how `loop claims fixtures` is registered, and name any further registry that leg has). Add one scope item for the leg, and name the leg in §7's gate list.
2. F-read, S4's existence check. Resolved: the request record's existence is confirmed by a separate bounded read of `refs/gov/requests/<key>` alone, never by widening `tools/unattended/unattended.sh#read_claims`' fetch (which would sight every request record into the feed on every claim read). Mark `RESOLVED (agent, 2026-11-19, delegated): a separate bounded read, rung 3; the claim read stays the size it is, and the §4 table already says bounded read. widens: none · relaxes: none`. Amend S4 and §4 to say so.
3. F-help: §5's line that no page under `help/` describes the driver's verbs is false; `help/loop.md` carries the `--lease` paragraph (its `verb:unattended.sh:--lease` usage anchor) listing the kinds and the refusal causes. Amend §5, and make S6 name that paragraph's revision for the `request` kind and its causes.
4. The builder found that the request kind also reaches `read_claims`' awk tail classifier, `derive_claim_keys`' case and the `check_cross_run_overlap` call in `tools/unattended/unattended.sh`; name them in S4 or §4 so the build covers them.
5. Replace every stale line citation in the revised sections with a `path#symbol` citation (for example `tools/memory-tree/row_grammar.py#derive_content_key`, `tools/unattended/unattended.sh#write_claim`).

### Acceptance

Spec 19 at rev-7 carries the two resolved forks, the amended `New arm:` line, S4, S6, §4 and §5, the leg's registry
paths in Files touched, `path#symbol` citations, and one §9 line naming this brief and the divergence;
`check-memory-hygiene.sh --only 12,25 --spec` and the spec-token checker over it report nothing.

### Gates

The memory hygiene gate (`--only 12,25 --spec`), the spec-token checker and the naming lexicon; no other.

### Non-goals

No product code, no commit, no index render, no status flip (it stays INPROGRESS), no spec other than
TOOL-dPlacedRequest-19. Pin every figure you write with DERIVED or PINNED, never let a section sign stand before a
unit word, and never quote a check's hit literally in prose.
