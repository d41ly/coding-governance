**Serves:** research TOOL-dPlacedRequest-33

# Brief — dPlacedRequest: TOOL-dPlacedRequest-33's divergence, resolved

## The prompt

> /unattended dPlacedRequest

## The brief

### Goal

TOOL-dPlacedRequest-33's builder returned a DIVERGENCE (run `wf_699065b9-988`) and committed nothing: S3 deletes both
inline blocks from `skills/session-kickoff/manifest-check.sh` and AC4 greps for neither, but
`skills/session-kickoff/manifest-check.sh#read_card_ref` (called by `#resolve_build_card` and `#write_build_card`)
calls `add_feed_sightings`, defined only in the inline `gov_feed_sh` block, and §3 rules out changing the lookup's
fetch; AC5's stub cannot log no call while the driver's conf load runs git; and the card-store fixture has no
unattended kit and no conf, so S2's dark switch would make every existing remote-ref case miss. Revise the spec to
the main loop's rulings.

### Items

1. F-blocks. Add to §8, resolved: "Which inline block leaves the engine, when the card read still sights the feed through `add_feed_sightings`?" (a) only `gov_ref_sh` leaves; `gov_feed_sh` stays until TOOL-dPlacedRequest-34 routes `read_card_ref` through the driver's card-ref verbs; (b) this unit also moves the card read to the driver; (c) both leave and the sighting is dropped. Mark `RESOLVED (agent, 2026-11-20, delegated): (a), rung 3; the smallest change that keeps §3's lookup untouched and every card read sighted, and (b) takes TOOL-dPlacedRequest-34's items, (c) loses the sightings `read_first_seen` reads. widens: none · relaxes: none`. Amend S3 so it deletes `gov_ref_sh` alone and says the engine keeps one feed copy for its reads until TOOL-dPlacedRequest-34; AC4 greps for the `gov_ref_sh` opening marker alone; name `run_card_git`, left with no caller, as deleted.
2. F-stub: AC5 observes that the stubbed git logged no fetch and no push (the driver's conf load always runs one `rev-parse`), rather than no call at all.
3. F-fixture: §4 Files touched's line for `skills/session-kickoff/card-store.fixture.sh` also says the fixture copies the unattended kit into its scratch repository, found through `resolve_kit_file` (never a spelled kit path), and writes a `.unattended.conf` with `RUN_CLAIMS` on for every existing case, so the remote-ref cases keep reading `$REF`; AC1's wording follows.
4. Note in §4 that the engine keeps the local `refs/gov/builds/<slug>/card` and the cache's full sha by reading `refs/gov/remote/builds/<slug>/card` after the driver answers, since the driver prints an abbreviated sha; and that the new verb refuses by printing its line and exiting 2, with no new numbered refusal, the driver being at its refusal ceiling.
5. Re-cite the moved line citations (`derive_claims_line`, the `RUN_CLAIMS` resolution, `print_claims`, `resolve_claim_remote`, the conf's `RUN_CLAIMS` line) as `path#symbol` citations.

### Acceptance

Spec 33 at its next rev carries the resolved fork, S3, AC1, AC4, AC5 and §4 amended, `path#symbol` citations, and one
§9 line naming this brief and the divergence; `check-memory-hygiene.sh --only 12,25 --spec` and the spec-token
checker over it report nothing.

### Gates

The memory hygiene gate (`--only 12,25 --spec`), the spec-token checker and the naming lexicon; no other.

### Non-goals

No product code, no commit, no index render, no status flip (it stays INPROGRESS), no spec other than
TOOL-dPlacedRequest-33. Pin every figure you write with DERIVED or PINNED, never let a section sign or a section
number stand before a unit word, never write a bare file-stem section reference, and never quote a check's hit
literally in prose.
