# Brief — dRenderedAnchor: the closing review's round-2 findings on unit 2

**Serves:** research TOOL-dRenderedAnchor-3

## The brief

### Goal
Close every confirmed finding of the closing diff review's round 2, which read unit 2, as one batch unit, so the /build Skill's citation pass resolves only what it means to and cannot name a file outside the kits, every new arm reads a population it does not derive from what it guards, and the help text and docstrings state the predicates that ship.

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

## Drawn from the session

> A round re-arms only on a count STRICTLY SMALLER than the round before
— agent, citing `memory/guides/BUILD-METHOD.md` M4: round 2 confirmed 13 against round 1's 10, so the diff review exits and promotes.

## Owner confirmation

Asked: none — M4 promotes every medium and low at the exit by the owner's 2026-10-04 ruling, and the owner's go on this build stands.
Answer: none
