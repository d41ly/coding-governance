**Serves:** research PLAY-dOrderedCharter-78

# Brief: spec 78 — the close's three parked fixes, as the owner picked them

## The prompt

> take forks' recommendations, land it

— owner, 2026-11-10. The picks are recorded in `memory/builds/dOrderedCharter/build/2026-11-10-build-PLAY-dOrderedCharter-1-owner-fork-picks.md`.

## The brief

### Goal

Write spec 78, a Tier-2 unit whose pass leaves the govkit acceptance matrix and the harness-arms leg green over the tree, and an
adopter's tags check green in a scratch install, by the three picks below.

### Items

1. **Where you write.** `memory/builds/dOrderedCharter/spec/2026-11-10-spec-PLAY-dOrderedCharter-78.md`; no builder is running. Header:
   `**Status:** DEFERRED · rev-1 · 2026-11-10 · node a · Tier-2 · base <HEAD's short sha> · streams playbook · order 37 · advances
   PLAY-dOrderedCharter-38`, plus the `**Derived:**` binding line every promoted unit of this build carries. Edges `none`, its
   dependencies on CLOSED units named in prose.
2. **The acceptance matrix.** A scratch install of the playbook kits cannot render the charter, because readers this build added look up
   the memory-tree and policy kits: `tools/govkit/govkit.py` or the readers it reaches print `looked in ... install.json, ... memory-tree`
   and `... policy` in the matrix's log. The pick: the playbook entry (`tools/govkit/entries/playbook.kit.toml`, and the playbook-render
   entry if it is the reader's owner) declares the kits it reads in `requires`, and `tools/govkit/matrix.py`'s scratch install carries
   them. Confirm which entry owns each lookup at HEAD before naming it.
3. **An adopter's tags check.** In a scratch install, `python tools/playbook/gov_tag.py check` reds where `tools/playbook/namespaces.toml`
   names `dOrderedCharter` as each namespace's owner, which the adopter's chain registry does not hold. The pick: the purpose arm skips
   an owner the target's own chain registry does not hold, printing an unarmed line, rather than each row being edited. Find the arm in
   `tools/playbook/tag_index.py` or its caller, state what it no longer checks, and give it a plant. Also say whether the family-id
   native's "resolves nothing" line in the same install is a red, and fix it by the same rule if it is.
4. **The A25r arm.** `tools/check-template-size.test.sh`'s arm for `tools/check-template-size.sh`'s check 8 branch 1 asserts the remedy
   sentence without the leading `).` that `python tools/memory-tree/check-arms.py --emit-pin` prints as the branch's signature. Assert the
   whole signature, and remove the pin row this build added for it to `memory/project/unarmed-branches.txt` in the same pass.
5. **The spec-token check grades a live spec's acceptance bullets word by word**: no acceptance command whose words include a path that
   is not a tracked file, never a test suite or the self-test runner as the observation, each backticked span on one line, every leg
   the files touched trip on the leg line. Cite code as `path#symbol` or a blob-pinned line, never a bare `path:line`.
6. Every section 8 fork carries a resolution mark; every new fact is pinned, keyed or marked DERIVED on its own line, outside backticks;
   every function name it mints passes `python tools/lexicon/lexicon.py --suggest <name> --as py.function`.

### Acceptance

- Spec 78 builds as written over HEAD and passes the pinned-facts check, memory hygiene's spec-shape check and the positional check.

### Gates

Run the pinned-facts check, memory hygiene's spec-shape check and the positional check over the spec, and report each.

### Non-goals

- No code. No edit to any other spec or file.
