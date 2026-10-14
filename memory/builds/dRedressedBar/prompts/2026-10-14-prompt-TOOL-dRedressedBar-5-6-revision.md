# Revision — dRedressedBar: TOOL-dRedressedBar-5, the builder's third divergence (a delegated pin keyed by the line it converts)

**Serves:** research TOOL-dRedressedBar-5

## The brief

### Goal
DIVERGENCE: §4 "The adopters" tells me to convert `tools/branch-reconcile/adopt-branch-reconcile.sh:142` to `mkdir -p "${SKILL%/*}" || exit 1`. §7 says `harness arms (fail branches armed or pinned)` only reads the adopters' exit sites "this unit keeps in place". That is wrong for `:142`. `memory/project/unarmed-branches.txt:178` pins that exit as a DELEGATED refusal site, and a delegated site's key is its own source line with the whitespace squeezed (`tools/memory-tree/check-arms.py:551`). The row reads `mkdir -p "$(dirname "$SKILL")" || exit 1`, and those rows are graded because `ARMS_REFUSALS="graded"` is set at `.memory-tree.conf:639`.

Converting the line keeps the site on its line but changes its key, so `check-arms.py --check` would report two problems at the close: the pin "which no live site carries — the refusal was deleted, reworded" (`check-arms.py:867-871`), and the new `mkdir -p "${SKILL%/*}" || exit 1` site, which "has no POSITIVE assertion … and is not pinned" (`:863-865`). Confirmed with a probe calling check-arms' own `scan_refusal_sites`, ebce889c adopter against the converted one: the `:142` key disappears and a new one appears; row 178 matches a live site before the change and none after. All 10 other pins for that adopter stay live, and the roles adopter's 2 sites don't change. Leaving `:142` unconverted doesn't help either: the file would keep 1 `path-subst` site with no row, so the spawn-idiom leg stays red. No placement the spec gives turns both legs green.

The spec would have to choose: (a) re-key row 178 of `memory/project/unarmed-branches.txt` to the converted line's signature `mkdir -p "${SKILL%/*}" || exit 1`, keeping its gate, kind, occurrence (1) and reason, with that file in Files touched, an AC stating the registry keeps the same number of rows and only row 178's signature field changes, and §3 and §7 corrected; or (b) another form for `:142` that the spec writer probes against check-arms.

### Items
1. **TOOL-dRedressedBar-5** — bump the rev. First probe for (b): a no-fork spelling of `:142` whose squeezed source line still equals row 178's key. If none exists, take (a): re-key row 178 in the same pass commit, add `memory/project/unarmed-branches.txt` to §4 Files touched, add the AC above, and correct §3 and §7. State in §3 that re-keying a pin whose code moved is not raising one: the row count, gate, kind, occurrence and reason are unchanged. Nothing else in the spec moves; the builder found everything else in rev-4 correct.

### Acceptance
`bash tools/unattended/unattended.sh --plan dRedressedBar --paths` grades TOOL-dRedressedBar-5 READY. A probe calling `check-arms.py`'s own `scan_refusal_sites` over the converted adopter, with row 178 as the revised spec states it, reports every pin live and no unpinned site.

### Gates
`harness arms (fail branches armed or pinned)` · `shell hygiene (a fork spent on builtin work)` · `memory hygiene`

### Non-goals
- No code.
- No pin, ceiling or registry row raised to absorb a red that a code change can fix.
- No merge to local main and no push without the owner's ask.
