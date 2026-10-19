# Revision — dRenderedAnchor: TOOL-dRenderedAnchor-3 spec rev-2, the builder's divergence

**Serves:** research TOOL-dRenderedAnchor-3

## The brief

### Goal
DIVERGENCE: spec rev-1 §4 "Section 2e's seventh row (S10)" says row 7's path is written as `str((root.parent / "out" / "y.js").absolute())`. S10, AC8 and §7's section-2e `New arm:` line depend on that. On Windows that value is a backslash path. The receipt join at tools/lib/resolve_kit_dir.py:39 (`str(row["path"]).split("/")[-1] == anchor`) splits on `/`, so it refuses the row before either escape term is read. Even with `root in hit.parents` cut from a copy of the canonical, the y.js query still prints LookupError. So on this Windows host the new arm cannot be seen RED, which is the fixture-passes-by-finding-nothing class the section says it avoids. A probe on 2e's fixture shape, with here at `p`, showed this. Written with `str()`: the canonical gives LookupError and the cut copy also gives LookupError. Written with `.as_posix()`: the canonical gives LookupError and the cut copy returns the `out` directory. To fix it, §4 has to say `<abs>` is `(root.parent / "out" / "y.js").absolute().as_posix()`, and that python writes it in posix form because the join splits `path` on `/`. A drive-letter posix path still reads as absolute in `root / <abs>` on Windows, and the change makes no difference on POSIX. AC8's "row 7 written as §4 says" then holds as stated. I checked the rest of the spec against the code at da01fe5d9 and found no other divergence. S8's root-install layout was probed against the current kit, and it behaves as §3 and §4 state.

### Items
1. M1 — the citation pass in `tools/roles/adopt-roles.sh` (`roles_lib.resolve_cited_paths`) resolves only citations that point inside a kit directory under the tool root (or only the workflow table's harnesses), never through a probe that reaches above the tool root, so `{{TOOL_ROOT}}run-gates/run-gates.sh` cannot name an adopter's repo-root file; it agrees with `derive_kit_paths` on the same citation.
2. M2 — arm 14 of `tools/roles/adopt-roles.test.sh` takes its harness population from the workflow table or a literal list, not from `TOOL_ROOT_CITE_RE`.
3. L1 — `help/roles.md` names all three tools that print the missing-harness note, the catalogue checker included, as `tools/roles/README.md` does.
4. L2 — a `tools/check-wiring.test.sh` fixture pins the remedy tail of check-wiring's absent-harness note.
5. L3 — the citation pass substitutes each held citation anchored at its boundary, so a shorter held citation never rewrites a longer one.
6. L4 — section 2e of `tools/lib/resolve-python.test.sh` reaches both escape terms, or its comment claims only the one it reaches.
7. L5 — arm 14's positive check matches the whole resolved path, not a substring.
8. L6 — an arm reaches `resolve_cited_paths`' exclusion of a held path outside the repository.
9. L7 — the help text and docstring describe a file beside neither mark without claiming it is the adopter's own.

### Acceptance
Each item's fix as the round-2 review record states it, with the skeptic's corrected fix where it judged the finder's UNSOUND; each new arm observed RED on a staged break before GREEN.

### Gates
The unit's spec §7 derives them; at least roles render selftest · roles adopter self-test · roles render wiring · python resolver (behaviour + inline parity + idiom ban) · check-wiring self-test · memory hygiene; then the full bar.

### Non-goals
Everything unit 2's spec §3 rules out, including the REVIEW-PROTOCOL and unattended Skill templates' plain citations and a shell twin of the namesake scan.

### Limitations
Scratch installs only under the system temp root; no write into an adopter repository. Kit versions move through the lander's `mint`. Merge and push wait for the owner's explicit ask.

### Reuse
The review record names each fix and the skeptic's verdict on it: `memory/builds/dRenderedAnchor/reviews/2026-10-19-review-TOOL-dRenderedAnchor-2-closing-diff-round2.md`. `derive_kit_paths` in `tools/lib/render-doc.sh` is the citation resolver the pass must agree with.
