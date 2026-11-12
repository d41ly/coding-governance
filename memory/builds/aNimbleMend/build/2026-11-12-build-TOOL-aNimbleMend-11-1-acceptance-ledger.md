# Acceptance ledger — TOOL-aNimbleMend-11

**Serves:** journal TOOL-aNimbleMend-11

Built against spec rev-3 in this record's own commit, which holds scope items S1 to S6 and leaves the unit INPROGRESS.
S7 and S8, the protocol's paragraph and its size row, were held out of that commit because S9's decision row was not yet in `memory/DECISIONS.md`; a second pass built them once commit b443d7081 held that row, observed AC8 and AC9 below, and closed the unit.
Each line is a probe the builder made in the pass. No suite, gate leg or bar ran in the pass. Owed to the close: the legs of the spec's Gates section. The spec declares no new arm.

**Evidences:** TOOL-aNimbleMend-11
- AC1 — `python tools/govkit/docs_leg.py --list` — the row for `policy:pass.fast-legs` ended `help/pass-legs.md:134`, the row for `policy:bar.inline-red-fixes` ended `help/red-fix-lane.md:120`, and the `--undocumented` listing printed neither id.
- AC2 — `python tools/govkit/docs_leg.py --fingerprints` — each of the ten rows naming one of the three pages carried a fingerprint its page's anchor holds once, the `build_records.py#new` row among them at its moved fingerprint, and each new page holds one `run: no` mark for its one `bash` fence.
- AC3 — `pass_leg` — each of the seven tokens printed at least 1 over the pass-leg page, every one as the spec spells it, and the method's file name printed 0.
- AC4 — `Pass: none` — each of the seven tokens printed at least 1 over the lane page, every one as the spec spells it, and the method's file name printed 0.
- AC5 — `Every other key has no consumer yet` — the index grep printed 2, and the two keys sit on lines 24 and 25 of the policy page, above that sentence on line 29.
- AC6 — `Documented on` — after the re-render the line under each key's heading on the reference page reads it, linking the key's page by its path from the root to the page one folder up.
- AC7 — `grep -c "never in a child"` — printed 1 for the render and 1 for the template, as did the greps for the two new phrases, and the render measures 30709 bytes CR-stripped against a row of 30720. (PINNED, 2026-11-12)
- AC8 — `nextAction` — `cmp` of the render and the template printed nothing and exited 0, each of the four greps over the render printed 1, and the paragraph opens on line 722, between the `## 12.` heading on line 694 and the `## 13.` heading on line 730.
- AC9 — `grep -c "RAISED 67361 -> " tools/template-size-limits.txt` — printed 1, on line 162, which names this unit; the row's second field reads 68022 and the render measures 68022 bytes CR-stripped; the pickaxe over `memory/DECISIONS.md` named b443d7081, an ancestor of the commit that moves the row. (PINNED, 2026-11-12)
