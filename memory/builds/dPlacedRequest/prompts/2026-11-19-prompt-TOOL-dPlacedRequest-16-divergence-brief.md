**Serves:** research TOOL-dPlacedRequest-16

# Brief — dPlacedRequest: TOOL-dPlacedRequest-16's divergence, resolved

## The prompt

> /unattended dPlacedRequest

## The brief

### Goal

TOOL-dPlacedRequest-16's builder returned a DIVERGENCE (run `wf_8d80f1b3-f05`) and committed nothing: at rev-7 the
spec rests on a hold staleness TOOL-dPlacedRequest-17 excludes, wraps the draw in a file with no lease seam, omits the
kickoff card's closed verdict set, and leaves the new classes' order against the write table's identity rows
unstated. Revise the spec to the main loop's four rulings so it can be built as written.

### Items

1. F6, the draw hold's judge. Add to §8, resolved: "Who reads a draw's hold stale, when TOOL-dPlacedRequest-17 S3 keeps `held` out of its age verdict?" (a) this unit judges it with `check_deadline_passed` and `read_lease_bound expiry`, aging the renewing beat TOOL-dPlacedRequest-17's walk finds on the hold's chain; (b) the same, aging the hold's tip; (c) a hold never expires. Mark `RESOLVED (agent, 2026-11-19, delegated): (a), rung 3; it is the beat every other lease ages by (one rule, TOOL-dPlacedRequest-17 F5), (b) lets a holder's plain `renews: no` beat keep a dead hold alive, (c) blocks every later draw for a dead holder. widens: none · relaxes: none`. Amend S4, §4 "The draw" and AC4 to it.
2. F7, the draw's site and its refused acquire. Resolved: the acquire and release wrap the patch draw at `tools/unattended/unattended.sh#run_budget_draw`, where `check_patch_peers` already reads the claims; `tools/loop/budget.py` leaves §4 Files touched unless something else in the spec still writes it. With `RUN_CLAIMS` off the draw runs unguarded as today (the switch every lease sits behind, TOOL-dPlacedRequest-1 F2); an acquire that refuses, queues offline, or prints `lease not written` refuses the draw with that reason and draws nothing. Mark `RESOLVED (agent, 2026-11-19, delegated): the driver's run_budget_draw, a non-zero acquire refusing the draw, rung 3; deny by default, and the only call site that already holds a claim read. widens: none · relaxes: none`. Add one acceptance criterion observing both halves (the wrapped draw, and a refused acquire drawing nothing).
3. F8, the kickoff card. Resolved: the card's claims reader in `skills/session-kickoff/manifest-check.sh` (its closed verdict set `live held unknown stale terminal`) ranks `released` beside `terminal` and hides it under the same `CARD_CLAIMS_HIDE_S` rule, so a landed build's lease never blanks the claims section. Add `skills/session-kickoff/manifest-check.sh` and `skills/session-kickoff/manifest-check.test.sh` to §4 Files touched, a scope item, and one criterion observing a card over a `released` row.
4. F9, the class order. Resolved: `foreign-released` and `foreign-tombstone` are classified BEFORE the identity rows `mine` and `same` for a released record and a true tombstone, so even the releaser takes a released lease at its epoch plus one and nobody, its releaser included, revives a tombstone; a draw's hold (status `held`) stays AFTER the identity rows, so its holder reads it `mine` to renew and release it. A refused tombstone cell exits 1 with the existing claim refusal check those columns already use (name it by number from the tree) and a message carrying the word `tombstone`, for every column §2 S3 names, `--hold`, the landing writes and `--settle` included. Amend §4's table and the GC_CELLS clause to say so.
5. The stale line citations in §1, §2 S2 and §10: replace each with a `path#symbol` citation.

### Acceptance

Spec 16 at rev-8 carries F6 to F9 resolved, S4 and §4 amended to them, the new criteria for the draw wrap and the
card, the class order stated, the card paths in Files touched, `path#symbol` citations, and one §9 line naming this
brief and the divergence; `check-memory-hygiene.sh --only 12,25 --spec` and the spec-token checker over it report
nothing.

### Gates

The memory hygiene gate (`--only 12,25 --spec`), the spec-token checker and the naming lexicon; no other.

### Non-goals

No product code, no commit, no index render, no status flip (it stays INPROGRESS), no spec other than
TOOL-dPlacedRequest-16. Pin every figure you write on its line with DERIVED or PINNED, never let a section sign stand
before a unit word, and cite code as `path#symbol`.
