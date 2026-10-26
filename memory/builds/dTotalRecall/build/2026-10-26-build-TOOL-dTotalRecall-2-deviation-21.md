# TOOL-dTotalRecall-2 deviation 21 — a build with neither a claim nor a lease mints under the per-session rule

**Serves:** deviation TOOL-dTotalRecall-2

- **Departs from:** `cl-dClosedLoop-0213@09982ca6`
- **Hand-off:** design-to-spec
- **Before:** the clause's `record` command mints ids "under the build's claim or lease", and names no case for a build that has neither.
- **After:** the one `record` write command, `gov_record.py new`, which mints ids under the build's lease, then its slug claim, refusing another holder of either, and for a build with neither, which is every build opened before TOOL-dTotalRecall-3's slug claim lands, this one included, under the charter's per-session `[ids]` rule, printing `minted under the session rule: no claim or lease for <slug>`, is idempotent and content-addressed, renders templates and refuses invalid values
- **Cause:** design defect
- **Reason:** No build in the tree holds a claim ref, since none exists before TOOL-dTotalRecall-3, and leases arrive with dPlacedRequest; refusing would leave the door unable to write any existing build's records, this build's own deviation records included. The per-session rule is the one those builds' ids were minted under, so the door keeps it for them and names it on every such write.
- **Evidence:** TOOL-dTotalRecall-2 §4 "Minting", §6 AC5 and §8 F3; `layer-memory.md:316-335` (the claim and lease rule); `memory/HYGIENE.md:172-185` (the per-session ids rule)
- **Risk:** loosening
- **Approver:** spec writer, the gov-spec-writer role of dTotalRecall's spec run, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** amends cl-dClosedLoop-0213@09982ca6
- **Caused-by:** TOOL-dTotalRecall-2
