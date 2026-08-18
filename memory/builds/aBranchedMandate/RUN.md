# aBranchedMandate - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id, the pinned BASE
with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
units-at-landing: TOOL-aBranchedMandate-1 TOOL-aBranchedMandate-2 TOOL-aBranchedMandate-3 TOOL-aBranchedMandate-4 TOOL-aBranchedMandate-12 TOOL-aBranchedMandate-13
witness: a4f3b4cacf5ed0a98fde596c967a76c7b2bf2ae6
phase: LANDED
keepalive: 3ff2b805
anchor-url: https://github.com/d41ly/coding-governance.git
anchor-sha: 401416faebff58c4527abef9f1a4ae80d244c4f2
anchor-ref: refs/heads/main
base: 401416faebff58c4527abef9f1a4ae80d244c4f2
keepalive-reaped: yes
parked-surfaced: yes

## Parked

Unit 4 of the roster, spec id TOOL-aBranchedMandate-3, is PARKED and DEFERRED rather than built.
The question refused: does the owner's ratification of that rule change still stand now that the
protocol carrying its three-cost price list has changed underneath it? Options seen: re-derive S6b
and S4 against the merged leg and build it; build only the mechanical parts and leave S6b; or park
and hand the re-pricing back. The third was taken, because S6b's obligation is to state the
disposition of five assertions inside a loop that no longer exists — re-specifying a security
predicate rather than re-pointing a citation — and because M3 delegates fork resolution, not scope.
The full drift table is in that spec's rev-5 and the question, options and refusal are in the build
README. Both reached the wrap-up, which is what the attestation above claims.

Recorded by hand, and that is worth naming: no verb writes a park. `park()` is reachable only from
`--close --override` and `--abort`, so a run that parks a unit WITHOUT needing an override and
without aborting has no sanctioned way to put it here, even though protocol section 2 makes this
file the home of parked decisions. Row minted for it.

Also recorded: this run re-ran `--preflight` against its own live slug to observe an acceptance
criterion, and preflight OVERWROTE the live run-state file — keepalive id and anchor pin both. It
was restored from the commit that preceded it, so the pin-time evidence above is the original
observation. Upstream's record rotation retires a TERMINAL record; a non-terminal one is still
overwritten in place. Row minted for that too.

2026-08-17T13:46:06Z decision · item unit 4 re-pricing · reason Owner re-priced 2026-08-17 and chose to build TOOL-aBranchedMandate-3. The earlier park's main reason was a measurement error: the S6b loop exists at check-unattended.sh:295; the grep pattern lacked the quote the source carries. Premises re-derived in spec rev-6.

2026-08-18T00:19:54Z decision · item gates-green is red for upstream reasons · reason MEASURED on a clean origin/main checkout at 43eb6b1: lexicon 450 offenders over pin 417, none of the 7 offender files touched by this diff. drift-audit reports ORPHAN_ID_PIN 0->5 only because local main is stale at 6678260 while origin/main is 43eb6b1; the value is 5 on both. Options seen: (A) fast-forward local main, which desyncs the primary worktree another session may be using, and clears only drift; (B) --override gates-green, which spends the one check standing between an unattended run and an unverified landing; (C) stop and let main's owner clear the lexicon pin. REFUSED to pick: B is the owner's call because the reds are not this build's to fix and an override here buys a landing at the cost of the bar's meaning.

2026-08-18T02:05:52Z override · item gates-green · reason Owner instructed 2026-08-18 to land and disregard this red. MEASURED: the only failing leg is drift-audit records, and it fails solely because LOCAL main is stale at 6678260 while origin/main is 31d0831 -- running the same tool with --base-ref origin/main yields zero WEAKENED complaints. ORPHAN_ID_PIN is 5 on this branch and 5 on origin/main; only the stale local ref reads 0. No signal about this branch's own content is being overridden.

2026-08-18T02:08:16Z decision · item landing needs a call on 41 unpushed commits on main · reason push-main.sh lands main FROM the primary tree, and that tree's main is 41 commits ahead of origin/main. Any push of main therefore publishes all 41 alongside this build's 6 units. They are this repo's own commits, not a third party's -- git author is the same owner throughout -- but they were produced by OTHER agent sessions, this run did not write or verify them, and publishing is not reversible. Options: (A) owner pushes those 41 first, then this branch merges into main and lands; (B) owner says land all together and the bar validates the merged result; (C) leave the branch unlanded. REFUSED to pick: 'land everything on main' plausibly means only this build's work, and the difference between the readings is 41 commits reaching a shared remote. Separately RESOLVED: the drift-audit red was the stale local main and nothing else -- with main current in the primary tree that leg exits 0, so the gates-green override recorded earlier was not needed on the merits.
