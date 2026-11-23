# TOOL-dQuietDisk-1 leg-tail 5 — build-index selftest failed in run unattended-179540992358805920005-2030153

**Serves:** leg-tail TOOL-dQuietDisk-1

- **Leg:** build-index selftest
- **Hash:** a2ef3669ab5d5ed2786aeca36eee07daa4e1a923
- **Run:** unattended-179540992358805920005-2030153
- **Sha:** 87fdd8497b08c75f63e601a265ac6f30eb285324
- **Cause:** run:dQuietDisk

```
arm ok    backlog: a hold on a target that is neither an ask nor a spec renders UNRESOLVED
arm ok    backlog: and that ask's V6 names the unresolvable target
arm ok    backlog: two asks blocked on each other both derive their TRUE token
arm ok    backlog: and V6 names the cycle
arm ok    backlog: a self-hold is V6
arm ok    backlog: a non-`unit` ask whose only closing spec reads WONTDO stays OPEN
arm ok    backlog: a `unit` ask whose same-id spec reads WONTDO derives WONTDO
arm ok    backlog: a `unit` ask whose same-id spec reads CLOSED derives CLOSED
arm ok    backlog: a REOPEN naming the closing spec leaves the ask live
arm ok    backlog: a second CLOSED row citing the SAME evidence stays cancelled
arm ok    backlog: a CLOSED row by a NEW sha re-closes it
arm ok    backlog: a REOPEN naming a folder slug cancels that folder's WONTDO
arm ok    backlog: a REOPEN of a record that closes nothing is V11
arm ok    backlog: every permutation of file and row order folds identically
arm ok    backlog: and the evidence it NAMES is the sorted minimum, not the first record found
arm ok    backlog: HIGH in one file and LOW in another reads HIGH
arm ok    backlog: an ask with no SEV row reads unlabelled
arm ok    backlog: an id-first legacy row
arm ok    backlog: a status-first legacy row
arm ok    backlog: an ASCII ` - ` separated legacy row
arm ok    backlog: the `CLOSED by` slot keeps its evidence in the body
arm ok    backlog: and the evidence prose is not thrown away
arm ok    backlog: WITHDRAWN folds to WONTDO and raises the flag
arm ok    backlog: a prose line returns nothing WITH its reason
arm ok    backlog: an unkeyable list row returns nothing WITH its reason
arm ok    backlog: a list row whose token is not a legacy status returns nothing
arm ok    backlog: the clean fixture reports NO verdict
arm ok    backlog: V1 — the ask's slug is not its folder
arm ok    backlog: V1 names the folder AND the slug
arm ok    backlog: V3 — two ask rows for one id, and nothing else
arm ok    backlog: V3's message names both files and both builds
arm ok    backlog: V5 — a derived token used as a verb
arm ok    backlog: V7 — a verb row targeting an ask nobody filed
arm ok    backlog: V7 — a `closes` naming an ask nobody filed
arm ok    backlog: V8 — a CLOSED row `by` a value that resolves to nothing
arm ok    backlog: a CLOSED row `by` a SHA is shape-checked only and is NOT V8
arm ok    backlog: V9 — a post-cutoff ask whose id is a spec H1 without the `unit` marker
arm ok    backlog: V9 names the ask's file AND the spec's
arm ok    backlog: V10 — a terminal build holding an OPEN ask nobody dispositioned
arm ok    backlog: a REOPEN counts as that ask's KEEP, so V10 does NOT fire
arm ok    backlog: V11 — a REOPEN naming no closing record
arm ok    backlog: V12 — a post-cutoff ask with no SEV row anywhere
arm ok    backlog: V13 — a SCOPE row carrying a `may` grant
arm ok    backlog: V13 — a SCOPE row carrying `may none` is the same finding
arm ok    backlog: V13 names the SCOPE row and the label it may not carry
arm ok    backlog: a SCOPE row carrying no `may` is not V13
arm ok    backlog: V15 — a blank cutoff under `builds`
arm ok    backlog: V16 — an unpadded cutoff under `builds`
arm ok    backlog: an absent BACKLOG_MODE reads shards
arm ok    backlog: a blank BACKLOG_MODE reads shards
arm ok    backlog: `shards` reads shards
arm ok    backlog: `builds` reads builds
arm ok    backlog: `shard` is a refusal naming the legal set
arm ok    backlog: `builds` with a blank cutoff returns V15
arm ok    backlog: `builds` with an unpadded cutoff returns V16 naming the key
arm ok    backlog: `builds` with a zero-padded cutoff returns neither
arm ok    backlog: under `shards` the cutoff is not read at all
arm ok    backlog: the disarming is real: V12 does not fire while V16 stands
arm ok    backlog: the fold returns the counts, and `verdicts` is None when nobody asked
FAIL — 2 arm(s) failed
```
