# TOOL-dTotalRecall-3 deviation 35 — the claim CLI re-reads a write the remote refused, and refuses the slug `asks`

**Serves:** deviation TOOL-dTotalRecall-3

- **Departs from:** `TOOL-dTotalRecall-3@rev-4` [§4 "The verbs", "The slug claim", "The counter", "Inventory"]
- **Hand-off:** spec-to-code
- **Before:** §4 has a lost create read again as present and a push not completed exit 2 with `GOVREF_WHY`; `check_claim_args` admits any slug of the admit grammar; each verb's fetch is one bounded fetch of its ref; and the inventory mints three Python functions in `gen_build_index.py`.
- **After:** `tools/memory-tree/gov-claim.sh#run_slug_claim` and `#run_ask_mint` read a write `write_gov_ref` answers as not completed again once, a ref that then reads moved off the tip leased on being a lost race and an unmoved one the exit 2 refusal; `#check_claim_args` refuses the slug `asks` to the `slug` verb, since `refs/gov/claims/asks/` is the counters' subtree, and refuses a CLAUDE_CODE_SESSION_ID that is not letters, digits and dashes; each fetch names its ref by a one-star refspec with `--prune`, so an absent ref is an empty answer rather than a failed fetch, and the counter's also writes `refs/remotes/<remote>/<branch>`; the repository root is read by `git rev-parse --show-toplevel` after the shape checks and before the family and grammar checks. `gen_build_index.py` adds the constants `#CLAIM_CLI` and `#CLAIM_CACHE_NS` and the self-test function `#test_slug_claims`.
- **Cause:** builder discovery
- **Reason:** two creates racing on one ref leave the loser refused by the remote itself, `[remote rejected] (reference already exists)`, which `tools/lib/gov-ref.sh#write_gov_ref` reads as not completed, so AC1's loser exited 2 and never `taken` until the re-read; a slug claim `asks` would block every counter ref; a session id is written into the commit message; an exact refspec fails the whole fetch on an absent ref, which then reads as offline.
- **Evidence:** the pass commit of TOOL-dTotalRecall-3 and its acceptance ledger, `2026-11-22-build-TOOL-dTotalRecall-3-1-acceptance-ledger.md`
- **Risk:** stricter
- **Approver:** author, under the build's `author-recorded` value
- **Follow-through:** ask TOOL-dTotalRecall-27
- **Caused-by:** TOOL-dTotalRecall-3
