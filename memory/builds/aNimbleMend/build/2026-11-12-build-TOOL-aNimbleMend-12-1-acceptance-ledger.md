# Acceptance ledger — TOOL-aNimbleMend-12

**Serves:** journal TOOL-aNimbleMend-12

Built against spec rev-2 in one pass commit. Each line is a probe the builder made in the pass: `run_pass_lane_case` called once per case through `python -c`, each over its own scratch target, and two read-only commands. No suite, gate leg or bar ran in the pass, and `--fixture` itself was not run, so the suite's count line and its guard trace were not printed. Owed to the close: the direct runs `A` and `G` of the spec's section 6, the legs of its Gates section, the new arm's RED-first and GREEN observations, and the two readings AC9 and AC10.

Where the built tree and the spec's text disagreed, the case asserts the tree as built, as the spec's flow section rules, and each such line is named here. The deployer emits no leg manifest into the fixture target, since `build_install_target` strips the `[gate_runner]` seed, so the case writes one row carrying no field as part of what the adopter writes by hand. The runner's freshness preflight refuses a typed pass-leg field with exit 2 before any leg runs, so every adapter call of both cases carries `GATE_REGEN_CHECK=0`, a knob the spec does not name. The adapter prints nothing with `pass.fast-legs` off, as TOOL-aNimbleMend-5 built it, so step 13 asserts no output where the spec expects one line naming the key. The conf keys the case adds are `ROUTED_PATHS`, `LEG_MANIFEST` and `ROUTED_COMMIT_CUTOFF`, the three the spec names.

**Evidences:** TOOL-aNimbleMend-12
- AC1 — `0 wrong` — the adopter case printed its step lines with no `WRONG:` and returned no wrong check; its `install` line quoted `pass-legs: 0 legs declared, nothing ran`. The suite's own count line was not printed, since the function was called directly; the close owes the run of `A`.
- AC2 — `planted pass leg` — step 3 read exit 1 with the run record and the ledger both `fail`, step 4 read exit 0 with one witness line naming the leg and `Red-fix:`, and step 8 read a refusal equal to R0.
- AC3 — `1 red-fix` — step 2 read the gate's refusal with no red open, step 10 read `1 fix commit(s) · 1 record(s) · 0 owed`, and step 11 read the pushed-range summary holding the count with no violation line naming the fix commit.
- AC4 — `names no unit` — step 5 read a refusal equal to R0 with the lane key off and the red open, and step 12 read the fix commit listed under those words, the grader exiting 1.
- AC5 — `pass.fast-legs` — step 13 read exit 0 and both hashes unchanged with the key off. NOT as the criterion words it: the adapter printed no line, which is what TOOL-aNimbleMend-5's spec states and its code does, so no stdout line names the key; the spec writer owes the criterion's wording.
- AC6 — `PASS_LEGS` — the gov case printed its step lines with no `WRONG:`; its `setup` line read the constant naming `bash`, the adapter under the tool root and `--base`; its g2 line read the gate refusing `gov-diff-reviewer` while the red was open; steps 4, 5, 8 and 13 read as in the adopter. The close owes the run of `G`.
- AC7 — `policy fixtures` — `check-spec-tokens.py --legs-for -` named the leg for each of the three paths, and `git ls-files` listed each.
- AC8 — `grep -c -e "pass-and-lane-adopter" -e "pass-and-lane-gov" tools/policy/README.md` — printed 2.
- AC9 — `PASS-BUDGET FAILED` — not observed in the pass: a reading of gov's own declared list, which the main loop owes at the close.
- AC10 — `gate-pass-legs.txt` — not observed in the pass: the main loop runs the adapter once in gov's tree at the close, and a role agent's hook refuses it.
