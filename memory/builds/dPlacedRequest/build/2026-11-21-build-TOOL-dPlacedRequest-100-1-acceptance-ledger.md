# TOOL-dPlacedRequest-100 — acceptance ledger

**Serves:** journal TOOL-dPlacedRequest-100

The unit was built from its spec at rev-1 on base `71b119ca1`, after the red-fix commit `179180dd3`
that escapes `tools/loop/placement.py#read_build_lease`'s shell printf for Python formatting. Built:
S1, the constant `LEASE_STALE_HINT` beside `tools/unattended/unattended.sh#run_lease_verb`, read by its
refusal line, and the take-over branch in `tools/unattended/unattended.sh#run_entry_claim` with its
header comment; S2, the `stale-holder` plant in `tools/loop/claim.py#check_claim_plant` and its `PLANTS`
row, and the `loop claim fixtures` budget row re-priced; S3, the route named in `help/loop.md`,
`tools/unattended/VERBS.template.md` and `memory/guides/UNATTENDED-VERBS.md`. No gate, suite or bar ran.

**Evidences:** TOOL-dPlacedRequest-100
- AC1 — `stale-holder` — `python tools/loop/claim.py --fixture --plant stale-holder`, a forward-slashed `TMPDIR` under the system temp folder, exited 0 printing `claim: stale-holder · stale exit 0 · lease epoch 1 -> 2 · held`: the repeat's `--entry-claim` exited 0 printing `take-announced`, the remote lease's `epoch:` one above the planted one, and no claim commit holding `wait-since:`. Its RED-first reading, the tip's `claim.py` beside the driver of `2b4cc0bd4`, is the main loop's at the close. (DERIVED)
- AC2 — `LEASE_STALE_HINT` — over the tip the hint's grep printed 1 and the constant's grep printed 4, the definition, its comment, the refusal line and the entry claim's test; at `2b4cc0bd4` they printed 1 and 0, the RED-first reading. (DERIVED)
- AC3 — `a stale build lease is taken over` — over the tip the grep printed 1 for each of `help/loop.md`, `tools/unattended/VERBS.template.md` and `memory/guides/UNATTENDED-VERBS.md`; at `2b4cc0bd4` it printed 0 for each, the RED-first reading. (DERIVED)

## Readings beside the criteria

- The `live-holder` plant, run alone over the tip, still exited 0 held, its fresh lease waited on and then past `flow.wait-ceiling`, so the branch leaves an unhinted refusal on its old route. (DERIVED)
- A bash probe of the refusal line, the constant read from the driver, printed the same bytes as the inline hint it replaced, and the entry claim's suffix test matched it. (DERIVED)
- The `stale-holder` plant by direct CLI over base `179180dd3` took: (PINNED)
  10.9 s (PINNED)
- so the `loop claim fixtures` proxy, the row's earlier reading plus that, is: (DERIVED)
  130.9 s (DERIVED)
- and its budget at x1.5, under the leg's ceiling of `tools/gate-legs.json`, is: (DERIVED)
  197 (DERIVED)
- The row's `plants=` token reads the plant count `PLANTS` holds once `stale-holder` is added: (DERIVED)
  14 (DERIVED)
- The kit-epoch rule binds at the push boundary, where the lander mints each moved kit's version (`tools/govkit/govkit.py#cmd_epoch`), so no version carrier moved in this pass, as in this build's earlier driver and loop-kit passes. (DERIVED)

- The bug-class checklist over the pass commit `3b4afd7ce` selected `fixture-passes-by-finding-nothing`: the plant's no-`wait-since:` check passed over an empty claim log, so it now also misses where the claim ref holds no commit; re-run alone, the plant exited 0 held. Its sighting is live: unread, the acquire refuses with no hint and the claim waits, which the plant reads as a miss. (DERIVED)
- It selected `refusal-branch-with-no-arm`: the take-over refused and the take-over not written have no plant, the spec naming the one `stale-holder` plant and its row's token raised by one, so both are named for the close rather than built here. (DERIVED)
- It selected `usage-exit-list-lags-its-function`: the branch's one new return is the literal `return 2`, a code the usage line lists. (DERIVED)
- It selected `a-spelling-change-strands-its-readers` and `two-answers-to-one-question`: the refusal line prints the same bytes, a bash probe comparing it with the inline hint it replaced, and the unattended suite's two greps of the hint read those bytes unchanged. (DERIVED)
- It selected `budget-row-not-remeasured-after-added-arms` and `an-attested-count-must-count-what-the-grader-counts`: the row was re-read by the plant's own reading, and its token is the length of `PLANTS` imported from the module. (DERIVED)
