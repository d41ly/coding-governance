**Serves:** spec-audit TOOL-dGroundRules-35@rev-1 TOOL-dGroundRules-36@rev-1 TOOL-dGroundRules-37@rev-1 TOOL-dGroundRules-38@rev-1 TOOL-dGroundRules-39@rev-1 TOOL-dGroundRules-40@rev-1 TOOL-dGroundRules-41@rev-1 TOOL-dGroundRules-42@rev-1 TOOL-dGroundRules-43@rev-1

# Tier-2 spec audit — dGroundRules, the round-5 disposal units (TOOL-dGroundRules-35 to -43)

Provenance: this is an adversarial review. Five finder lenses (gov-spec-reviewer) and five skeptic batches (gov-skeptic) ran, and gov-synthesizer wrote the synthesis. The build README is the mandate, because no run-mandate prompt exists. The round-5 spec audit's disposal promoted units 35 to 43.

Reviewed: memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-35.md@ae644fbad3fdd4fd3db9100f0962d28be6710bbf, memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-36.md@c221c3f628d71dc35fb95f00b8a615774ed393bf, memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-37.md@87694dd28a644288a60ad4092493521b2fefd913, memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-38.md@e5a5e97d6e8988f1be2414581373756ba6262c5b, memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-39.md@0caf786b10717e99aa1404b3bb2e7d09ab85d67e, memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-40.md@1aa642bb6103a7b1f5b02fb1a94513a71f6c891b, memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-41.md@af6801091f3f580d6cbfd1f75beae8883019919a, memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-42.md@1e6f12665a49d54a4c9527bee6400d1e1dcf319b, memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-43.md@720f7f770f62166e0bc2f8322c0dd3a816ffda37

ROUND 1

## Verdict: BLOCKED

One blocker was confirmed, so the build must not dispatch until spec 40 is fixed.
B1: spec 40's string-prefix row is not a string-prefix pair, so the arm cannot tell a raw startswith from containment.
Three high items repeat the stripped-literal class that units 40, 41 and 43 were promoted to close: PAIRS_SH (H1), the bare `policy.md` (H2) and the root-README EVIDENCE (H3).
By item, the adjudicated tally is 1 blocker, 3 high, 13 medium and 9 low, for 26 items.
By raw confirmed finding, the tally is 1 blocker, 7 high, 16 medium and 9 low, for 33 findings.
Every confirmed finding is in exactly one item, and none is counted twice.
Three fixes were judged unsound (ids 1, 16 and 35). Each of those items gives the skeptic's corrected fix.
Every binding grade is kept. The skeptic re-graded four findings: ids 12, 30 and 31 from high to medium, and id 34 from medium to low.
Ids 30, 31, 3, 12 and 25 describe the same defects as H1, H2 and H3. They are kept apart only because their binding grade differs. Items M1, M2 and M3 say so.
Ids 7 and 14 are one defect split across two grades, kept apart in L1 and M5 for the same reason.

## Review shape

Intensity full, raw 38, confirmed 33, refuted 5, unverified 0 (0 uncertain), precision 0.87.

| lens | returned | raw | confirmed | refuted | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|
| coherence | yes | 9 | 9 | 0 | 0 | 0 | 1.00 |
| grounding | yes | 9 | 9 | 0 | 0 | 0 | 1.00 |
| reuse | yes | 4 | 4 | 0 | 0 | 0 | 1.00 |
| blast-radius | yes | 6 | 2 | 4 | 0 | 0 | 0.33 |
| failure-envelope | yes | 10 | 9 | 1 | 0 | 0 | 0.90 |

## Run integrity

- Lenses: 5/5 returned, 0 died.
- Skeptic batches: 5/5 returned, 0 died.
- Demotions: 0 contradictory verdicts and 0 orphaned duplicate refutations were demoted to unverified.
- Discards: 0 spurious verdicts were discarded, and 0 duplicates.
- Fixes on confirmed findings: 30 judged sound, 3 judged unsound, 0 none proposed, 0 not judged.
- Severity on confirmed findings: 0 ungraded by the skeptic, 4 re-graded by the skeptic.
- Unverified findings: 0 answered uncertain, 0 with no usable verdict.
- Lens notes: none supplied, so every lens ran on the kit's generic brief.
- Roles: finders gov-spec-reviewer, skeptic batches gov-skeptic, synthesis gov-synthesizer.
- Intent: 34 spec documents supplied as `specs`, as sibling context.
- Checklist: 18 items, each assigned to exactly one of 5 lenses (coherence 4, grounding 4, reuse 4, blast-radius 3, failure-envelope 3).
- By design: none supplied, no caller byDesign and a block of 0.
- Move check: no checked subject moved.

Every integrity count is zero, so this run is complete.
The refuted findings are 23, 24 and 32 (duplicates of 20, 22 and 25), 27 (the foreign-prefix premise was false on re-probe) and 28 (a preference with no graded defect).

## Blocker

### B1 — Spec 40's string-prefix row is not a string-prefix pair (id 29)

- **Where:** `memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-40.md`, section 2 S1, section 4 The arm (OVERLAP_PAIRS), section 6 AC3.
- **What is wrong:** the row labelled string-prefix, `tools/policy/a.py` against `tools/policy/ab.py`, is not one. Neither string starts with the other. A raw startswith answers False for it, which is the right answer by accident.
- **Consequence:** the arm passes a `check_writes_intersect` or `covers` staged to a raw startswith. That is the exact regression the unit's goal says it catches, so the arm certifies what it does not check. AC3 expects `True then True` / `0 then 0` under RAW_BOTH, which cannot happen, so it is also red on a correct build.
- **Fix (judged sound by the skeptic):** make the disjoint row a real string-prefix trap where containment and raw startswith disagree, such as `tools/policy/a` with `tools/policy/ab.py`, or `tools/pol` with `tools/policy/x.py`. Spell the pair the same way in OVERLAP_PAIRS, PAIRS_PY, PAIRS_SH and AC3. The build must run the staged RAW_BOTH break in a scratch copy and see the arm go red.
- **Left-shift gate:** a check that every staged-break criterion's fixture row actually differs under the staged and real rules. A cheaper form is a checklist entry: "a trap row must be shown to separate the two rules before it is written".

## High

### H1 — Spec 40's PAIRS_SH is the stripped AC16 probe it exists to repair (ids 1, 10, 20)

- **Where:** `memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-40.md`, section 6, the PAIRS_SH literal (lines 125-126, AC2 and AC3). TOOL-dGroundRules-43 section 6 AC1 (line 253) runs the same literal.
- **What is wrong:** PAIRS_SH sources a bare `lib-unattended.sh` and probes `overlaps tools/policy/ x.py` and `overlaps a.py ab.py`. S3 promises AC16 "restated whole", and PAIRS_PY in the same block spells its paths whole.
- **Consequence:** from the repository root the source fails, so it prints `127 127`. With the library sourced, the stripped first pair answers 1 where AC2 expects 0. AC2, the PAIRS_SH half of AC3, and spec 43 AC1 can never pass on a correct build. The pass either cannot close or respells the probe a third time.
- **Fix:** id 1's fix was judged unsound. The skeptic's corrected fix, which ids 10 and 20 also give as sound, is to spell PAIRS_SH whole: `bash -c '. tools/unattended/lib-unattended.sh; overlaps tools/policy/ tools/policy/x.py; echo $?; overlaps tools/policy/a.py tools/policy/ab.py; echo $?'`. Also restate AC3: under a raw-startswith staging, give it a pair where one path is a raw string prefix of the other, such as `tools/policy/a` and `tools/policy/ab`. That pair should read True/0 under RAW_BOTH and False/1 on the built tree, because the a.py/ab.py pair is not a raw prefix pair (see B1). Re-run the literal from the repository root before committing the spec.
- **Left-shift gate:** a spec-tokens leg that runs every section-6 literal that is a pure read-only probe from the repository root, and reds on exit 127 or "No such file". Where no gate fits, add the bug-class checklist entry "a fenced literal is re-run verbatim from the root before commit".

### H2 — Spec 41's INSTALL_LINES and HELP_LEGS name a bare `policy.md` (ids 2, 11, 22)

- **Where:** `memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-41.md`, section 6, the INSTALL_LINES and HELP_LEGS literals (lines 119-120, AC4 and AC5), against section 2 S2 and S3.
- **What is wrong:** both literals name a bare `policy.md`. INSTALL_LINES is unit 34 AC36 copied byte for byte. The page lives at `help/policy.md`, and S3 promises AC36 "restated whole". This is the defect (review id 21) the unit was promoted to fix.
- **Consequence:** from the root, awk cannot open `policy.md`, so AC4 prints 0. `--legs-for policy.md` refuses with `REFUSING — no path given is tracked at HEAD` (exit 2), so AC5 never names `policy fixtures`. S2's guard line is then observed by no criterion that can pass.
- **Fix (judged sound by the skeptic):** spell both literals whole: `awk '/^## Install/{f=1;next} /^## /{f=0} f' help/policy.md | grep -c "mirror deferred"` and `python tools/check-spec-tokens.py --legs-for help/policy.md`. If the paths join reds the not-yet-tracked page, the cause is the join (open ask TOOL-aKeyedAnnotation-9). Leave the literal whole in the fenced block, as TOOL-dGroundRules-42 S3 prescribes.
- **Left-shift gate:** the same root-run literal leg as H1. Additionally, a check that every path named in a section-6 literal matches a path named in section 2 or section 4 of the same spec.

### H3 — Spec 43's EVIDENCE reads the root README (id 21)

- **Where:** `memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-43.md`, section 6, the EVIDENCE literal (line 227), AC3 and S3.
- **What is wrong:** EVIDENCE is `git show f4d31452a:README.md | grep -n gen:build-order`. That reads the repository-root README, which holds no build-order region. Section 4 Evidence (lines 129-131) cites `memory/builds/dGroundRules/README.md` for the same observation. This is the stripped path confirmed under review ids 17 and 25 for TOOL-dGroundRules-34 AC32.
- **Consequence:** the command prints nothing and exits 1, so AC3 (lines 165 and 179 expected) is red on a correct build. It contradicts the spec's own section 4.
- **Fix (judged sound by the skeptic):** spell EVIDENCE as `git show f4d31452a:memory/builds/dGroundRules/README.md | grep -n gen:build-order`.
- **Left-shift gate:** the root-run literal leg from H1 covers this, since the literal is read-only.

## Medium

### M1 — PAIRS_SH, graded medium (id 30)

- **Where:** `memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-40.md`, section 6 PAIRS_SH, AC2, and TOOL-dGroundRules-43 section 6 AC1.
- **What is wrong:** this is the H1 defect, seen through the failure-envelope lens. Line 118 says the probes are "spelled whole", but PAIRS_SH sources a bare library and probes stripped pairs.
- **Consequence:** AC2 cannot print `0 then 1`, and spec 43 AC1 is red too. The build ships no wrong result.
- **Fix (judged sound by the skeptic):** spell PAIRS_SH as `bash -c '. tools/unattended/lib-unattended.sh; overlaps tools/policy/ tools/policy/x.py; echo $?; overlaps <disjoint pair whole>; echo $?'`, using the disjoint pair from the corrected table in B1.
- **Grade note:** the skeptic re-graded this finding from high to medium, and medium binds. It is the same defect as H1 and is fixed by H1's fix. I judge high the right grade, to match ids 1, 10 and 20.
- **Left-shift gate:** as H1.

### M2 — Bare `policy.md`, graded medium (id 31)

- **Where:** `memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-41.md`, section 6 INSTALL_LINES and HELP_LEGS, AC4 and AC5.
- **What is wrong:** this is the H2 defect. Line 22 of the spec itself says a bare `policy.md` does not resolve from the root, yet the literals use it.
- **Consequence:** awk prints `fatal: cannot open file 'policy.md'` and the count is 0. `--legs-for` refuses with exit 2. AC4 and AC5 cannot pass, and the effect is contained to those two criteria.
- **Fix (judged sound by the skeptic):** spell `help/policy.md` in both literals, as H2 gives them. If the spec-tokens join rejects the path before the page exists, keep it whole inside the fenced block, as TOOL-dGroundRules-42 S3 prescribes.
- **Grade note:** the skeptic re-graded this finding from high to medium, and medium binds. It is the same defect as H2. I judge high the right grade, to match ids 2, 11 and 22.
- **Left-shift gate:** as H2.

### M3 — Root-README EVIDENCE, graded medium (ids 3, 12, 25)

- **Where:** `memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-43.md`, section 6, the EVIDENCE literal (AC3), against S3 and section 4 Evidence. Id 12 also cites AC1.
- **What is wrong:** this is the H3 defect. EVIDENCE greps the root `README.md` at `f4d31452a`, not the build README.
- **Consequence:** AC3 prints nothing, so S3's pinned citation is certified by no criterion that can pass. The effect stays inside an evidence check. AC1 also runs spec 40's PAIRS_SH and inherits H1's failure.
- **Fix (judged sound by the skeptic):** spell EVIDENCE as `git show f4d31452a:memory/builds/dGroundRules/README.md | grep -n gen:build-order`, and repair PAIRS_SH in unit 40 (H1).
- **Grade note:** these three findings bind at medium (id 12 was re-graded from high by the skeptic). Id 21 is the same defect at a binding high, in H3. I judge high the right grade for all four.
- **Left-shift gate:** as H3.

### M4 — Spec 35's AC1 and AC2 go vacuous once spec 36 lands (id 4)

- **Where:** `memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-35.md`, section 6 AC1 and AC2 (lines 131-137), against section 2 S2. Both units sit at order 12, which the README marks parallel.
- **What is wrong:** AC1 and AC2 observe S2 only through the absence of a `guard-trace` `WRONG`. Spec 36 S1 sets aside every kept path that `check-ignore` prints, and `.gitignore` ignores `__pycache__/` and `*.pyc`.
- **Consequence:** if 36 lands first, an unbuilt or broken mapping passes AC1 and AC2, because its `.pyc` paths are counted as ignored reads. Only AC3 still decides, and it covers the warm case alone. A regression of the cold-path digit-tail cut ships green.
- **Fix (judged sound by the skeptic):** observe the kept set directly. For example, a `python -c` probe imports check_policy, feeds `add_source_read` synthetic `open` events for `tools/govkit/__pycache__/govkit.cpython-314.pyc`, its `.pyc.<digits>` temporary and an `.opt-1` form, prints the kept set and expects only `tools/govkit/govkit.py`. Alternatively, have AC1 and AC2 also require the 36 line `0 ignored read(s) set aside` for budgets-ships-join, if that holds. Or order 35 before 36 explicitly.
- **Left-shift gate:** a checklist entry: "a criterion that passes on the absence of a WRONG must name the sibling unit that could hide the WRONG, and pin an order against it".

### M5 — ORDER_SHIFT does not name a unit whose order is shared, graded medium (id 14)

- **Where:** `memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-43.md`, section 6, the ORDER_SHIFT literal (line 231), AC6.
- **What is wrong:** ORDER_SHIFT changes "one unit spec's order" to an unused value, and AC6 expects ORDERS to print one more than the README's rows. That holds only when the chosen unit shares its order. Orders 10, 11 and 14 each have one holder (units 32, 33 and 43).
- **Consequence:** shifting a sole holder swaps one distinct value for another, so the count stays at 14. AC6 reds on a correct comparison, or the builder concludes that AC5 cannot see a missing step.
- **Fix (judged sound by the skeptic):** name the unit in ORDER_SHIFT, for example TOOL-dGroundRules-1 (order 1, held by two units), or state the precondition that the shifted unit's order has another holder.
- **Grade note:** id 7 is the same defect at a binding low, in L1. I judge medium the right grade for both, since a correct build can show a red criterion.
- **Left-shift gate:** a checklist entry: "a staging literal names its exact target; 'one unit' or 'any file' is not a staging".

### M6 — Spec 36's check-ignore call is not pinned to byte mode and `-z` (ids 13, 33)

- **Where:** `memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-36.md`, section 2 S1 and section 4 The set-aside (line 76: `stdin = "\n".join(kept)`, `ignored = set(out.splitlines())`).
- **What is wrong:** the set-aside writes newline-joined paths to `git check-ignore --stdin` with neither byte mode nor `-z`. On this node, Python's text-mode pipe writes each `\n` as `\r\n`, and git keeps the CR, so every path except the last goes unmatched. Without `-z`, git also C-quotes a path holding a non-ASCII byte, a double quote or a backslash, so the printed line never equals the kept path.
- **Consequence:** built in the house style (`subprocess.run(..., text=True, input=...)`), ignored paths reach the guard join and are reported as guard misses. Whether a planted `probe.pyc` is set aside depends on set iteration order, which changes with string-hash randomisation, so AC1 is flaky. A gitignored non-ASCII path is counted in n yet still joined, and comes out as a false `guard-trace` `WRONG`.
- **Fix (judged sound by the skeptic):** pin the call in S1 and the pseudocode to `git -C top check-ignore --stdin -z`, with input `b"\0".join(p.encode() for p in kept) + b"\0"` in byte mode and output split on NUL. Derive n from the paths that match, not from the raw line count. Add an AC1 variant that plants two ignored files, so a single correctly matched last line cannot pass it. Add a criterion that plants an ignored non-ASCII name, such as `tools/gövkit/__pycache__/x.pyc`, and expects no `WRONG` naming it.
- **Left-shift gate:** a lint over tools/ that reds any `--stdin` git call without `-z`. Alternatively, a checklist entry: "every path list piped to git is NUL-separated bytes".

### M7 — Spec 38 runs at the same step as the unit it consumes (id 5)

- **Where:** `memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-38.md`, section 3 Edges (line 55, `consumes-from TOOL-dGroundRules-34`) and section 1 order rationale (lines 25-27).
- **What is wrong:** 38 consumes 34's in-process copy of the exclude file, which S3 names as one of the two reads S2 keeps out. But it sits at order 12, the same step as 34, and section 1 justifies order 12 from unit 33 alone. The siblings 39, 40 and 41 also consume 34, and they sit at order 13.
- **Consequence:** the rendered order runs 38 concurrently with the unit it consumes. 38's builder may observe the trace before 34's exclude-file read exists, so S3's claim about that reader goes unverified. The ordering axis disagrees with the edges.
- **Fix (judged sound by the skeptic):** move 38 to order 13, above 34, and re-render the README order. Or drop the consumes-from 34 edge and S3's reference to 34's read, keeping only 26's index read, which AC2 actually observes.
- **Left-shift gate:** a build-order check that reds when a `consumes-from` edge points at a unit of the same or a higher order.

### M8 — Units in parallel steps 12 and 13 share write sets (id 6)

- **Where:** `memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-36.md`, section 4 Files touched, across TOOL-dGroundRules-34, 35, 36, 37 and 38 (step 12) and 39 and 41 (step 13).
- **What is wrong:** all five step-12 units write `tools/policy/check_policy.py`, and 34, 36, 37 and 38 also write `memory/map/generated/symbols.json`. Units 35 and 38 edit the same function, `add_source_read`, and 36 and 37 add code after `check_guard_trace`. Units 39 and 41 both write check_policy.py at step 13. No edge sequences them, and the README marks both steps Parallel `yes`.
- **Consequence:** BUILD-METHOD M6 `parallel-when-disjoint` clauses 1 and 3 fail (BUILD-METHOD.md:209-214): write sets intersect, and a generated index is shared with its generator. Spec 43 section 1 (lines 156 and 198) invokes that same clause to refuse splitting its own writers. A dispatcher following the rendered order either refuses at `--dispatch --writes` or runs concurrent passes whose edits to one function conflict.
- **Fix (judged sound by the skeptic):** state the sequencing in the specs. Either give 35 to 38 distinct orders, or add hands-off and consumes-from edges among them (for example 35, then 38, then 36, then 37, matching 43's composed pseudocode), and do the same for 39 and 41. Then re-render gen:build-order so no step marked parallel shares a write set.
- **Left-shift gate:** make the gen:build-order renderer refuse to mark a step parallel when two of its units' Files-touched sets intersect.

### M9 — Spec 38's PRIMARY clone grades committed bytes only (id 15)

- **Where:** `memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-38.md`, section 6, the PRIMARY literal (line 126, AC1 and AC2), and section 7's arm line "a primary clone of the built tree" (line 156).
- **What is wrong:** PRIMARY is `git clone -q <this repository>`. A clone carries committed objects only, and it checks out the source's HEAD branch, not necessarily this worktree's branch. The spec never says AC1 and AC2 run after the unit's commit, though line 105 shows it knows this problem for unit 36.
- **Consequence:** observed before the pass commit, the case grades a `check_policy.py` without `read_source_git_dirs`. AC1 then reds and AC2 is meaningless, or the builder commits unverified code in order to verify it.
- **Fix (judged sound by the skeptic):** state that AC1 and AC2 run against the unit's commit (clone, then check out that commit). Otherwise, build the primary checkout from the working tree with the snapshot (`build_source_snapshot`, TOOL-dGroundRules-26), so uncommitted bytes are graded.
- **Left-shift gate:** a checklist entry: "a criterion that clones the repository names the revision it checks out".
- **Caveat:** the skeptic did not run a clone, which the probe policy bars; this item rests on git clone semantics.

### M10 — Spec 37 rebuilds the guard-liveness check that run-gates already runs (id 19)

- **Where:** `memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-37.md`, section 2 S1 to S3, section 3 second bullet, section 10.
- **What is wrong:** `check_guard_lines` rebuilds a checker that already exists. Arm 1b of `tools/run-gates/run-gates.test.sh` (lines 619-660) holds every row's guard and doc_reads pathspec to `git ls-files`. It resolves `{prefix}` through the inlined, parity-gated `resolve_prefix_token` block and matches at a path-component boundary. The `run-gates canary` leg's guard holds `{prefix}/gate-legs.json`, so it runs on every manifest edit. The spec does not mention the arm. Its section 4 hand-rolls `entry with "{prefix}" as troot` instead of inlining the canonical block, which `tools/lib/resolve_prefix_token.py:1-9` requires of every consumer.
- **Consequence:** built as written, the rule has two carriers with different matching rules. The next change to the rule, such as a boundary fix or a doc_reads extension, will edit one carrier and miss the other. AC1 and AC3 are already met by the canary, so the new check closes no open gap.
- **Fix (judged sound by the skeptic):** drop `check_guard_lines` and section 6 AC1 to AC4. In section 10, cite arm 1b of `tools/run-gates/run-gates.test.sh` (line 619 onward) as the seam that already holds every `policy fixtures` guard entry to the index. Replace the section 2 scope with one sentence for the S4 sweep of TOOL-dGroundRules-33: a path the sweep adds must keep the run-gates canary green. Keep a single criterion: in a scratch copy, append PYC_GUARD and observe that `bash tools/run-gates/run-gates.test.sh` prints `guard or doc_reads pathspec matches no tracked path`. If a check inside the policy kit is still wanted, it must inline `resolve_prefix_token` byte-identically and use the same boundary rule, and section 10 must say why the canary arm is not enough.
- **Caveat:** the build runs that criterion's probe; this review did not run it.
- **Left-shift gate:** extend the resolve_prefix_token parity gate to red on any hand-rolled `{prefix}` substitution outside the canonical block.

### M11 — Spec 39's staged breaks accept any WRONG (id 26)

- **Where:** `memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-39.md`, section 6 AC2 and AC3, with TOOL-dGroundRules-36 S1, -37 S2 and -38 S1.
- **What is wrong:** AC2 and AC3 count any `WRONG` as the staged break's red, in a "scratch copy" the spec never defines as a git repository. Units 36, 37 and 38 add three `--fixture` WRONGs that fire in a non-repository copy: check-ignore, the manifest/ls-files check, and rev-parse with no case run.
- **Consequence:** a builder who copies the tree with `cp -r` (no `.git`) sees `WRONG naming rev-parse` before any case runs. AC2 and AC3 go green with the window rule untouched, so the staged-break proof certifies nothing about the window's edges.
- **Fix (judged sound by the skeptic):** make AC2 and AC3 require a `WRONG` line that names `census-window-edge` and the answer it got. Define the scratch copy as a git clone, as unit 38's PRIMARY does. Also require that the same run prints no `WRONG` naming `rev-parse`, `check-ignore` or `policy fixtures`.
- **Left-shift gate:** a checklist entry: "a staged-break criterion names the check whose WRONG it expects". Also define "scratch copy" once in TEMPLATE-SPEC.

### M12 — Spec 35's mapping misses caches under `sys.pycache_prefix` (id 35)

- **Where:** `memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-35.md`, section 2 S1 and S2, section 4 The mapping (the `parent name == "__pycache__"` test).
- **What is wrong:** S2 promises `govkit.py` is recorded whether or not a cache exists. But the mapping fires only when the cache's parent directory is `__pycache__`. With PYTHONPYCACHEPREFIX or `-X pycache_prefix` set, the cache path is `<prefix>/<mirrored source dirs>/govkit.cpython-314.pyc`, with no `__pycache__` parent and outside the top level.
- **Consequence:** on a node configured with a prefix, a warm load records nothing for `govkit.py`. With its guard entry staged out, the trace stays silent, AC3's red case passes, and the trace certifies coverage of a read it never saw. Nothing in the env, .github, tools/run-gates or tools/policy sets a prefix today.
- **Fix:** the finder's fix was judged unsound. The skeptic's corrected fix is to have `--fixture` refuse to run, with a named `guard-trace` `WRONG`, when `sys.pycache_prefix` is set. Alternatively, normalise both the prefix and the cache path with `os.path.normpath` before calling `source_from_cache`. Either way, add a criterion that runs AC3 with PYTHONPYCACHEPREFIX set.
- **Left-shift gate:** a checklist entry: "a trace keyed on an interpreter layout names every environment knob that moves that layout".

### M13 — Spec 43 forwards a relative `core.excludesFile` unchanged (id 36)

- **Where:** `memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-43.md`, section 2 S10, section 6 EXCLUDES_REPO and AC10.
- **What is wrong:** S10 forwards `git config --type=path --get core.excludesFile` to the snapshot unchanged. `--type=path` expands only `~`, so a relative value such as `excl.txt` is read against the snapshot's top level, where it does not exist. EXCLUDES_REPO does not say whether its value is absolute.
- **Consequence:** a source whose local config names a relative excludes file gets a snapshot whose `add -A` commits the files that config hides, such as `secret.local`. That is the leak AC10 guards against, and AC10 can pass on a build with this hole. The snapshot is a scratch repository, so the leak is contained.
- **Fix (judged sound by the skeptic):** in S10, resolve a relative value against the source's top level before passing `-c core.excludesFile=<absolute>`. Have EXCLUDES_REPO spell the value as relative (`core.excludesFile excl.txt`) so AC10 exercises that case.
- **Left-shift gate:** a checklist entry: "a forwarded git path setting is resolved against its source's top level".

## Low

### L1 — ORDER_SHIFT does not name a unit whose order is shared, graded low (id 7)

- **Where:** `memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-43.md`, section 6, the ORDER_SHIFT staging (AC6).
- **What is wrong:** this is the M5 defect, seen through the coherence lens. Picking unit 32, 33 or 43 leaves the distinct count unchanged.
- **Consequence:** AC6 passes or fails depending on an unstated choice. A builder who stages it on unit 43's own spec (order 14) sees AC6 red and may conclude AC5's comparison is broken.
- **Fix (judged sound by the skeptic):** name the unit in ORDER_SHIFT, one whose order is shared (for example TOOL-dGroundRules-35, order 12 to 99). Or state "a unit whose order value another unit also holds".
- **Grade note:** low binds. I judge medium the right grade, as given in M5.
- **Left-shift gate:** as M5.

### L2 — Spec 38's rev-parse deny branch is observed by no criterion (id 8)

- **Where:** `memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-38.md`, section 2 S1 (lines 31-34) against section 6 AC3 and AC4 (lines 140-147).
- **What is wrong:** S1 says a failing `rev-parse` is the run's `WRONG` naming `rev-parse` with no case run, and cites AC3 and AC4 as its observers. AC3 only prints the two directories. AC4 compares verdicts from a non-repository working directory, with the kit named by its absolute path, so the source still resolves. Neither stages a failure.
- **Consequence:** a build where a failed `rev-parse` returns an empty tuple, which disables the git-directory exclusion and lets the case run, passes every criterion. That is the silent fallback S1 forbids.
- **Fix (judged sound by the skeptic):** add a criterion that stages `read_source_git_dirs` in a scratch copy to call an unresolvable program in place of `git`, as 36 AC4 does for `check-ignore`. It should expect a `WRONG` naming `rev-parse` and no case's `RED as planted` line.
- **Left-shift gate:** a checklist entry: "every deny branch a scope item names has a criterion that stages it".

### L3 — Spec 37's parse-failure branch is observed by no criterion (id 9)

- **Where:** `memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-37.md`, section 2 S2 (lines 37-39) against section 6 AC4.
- **What is wrong:** S2 promises that an unparsable manifest and a missing `policy fixtures` row are each a `WRONG`, both "Observed by AC2, AC4". The only manifest staging is NO_ROW, which respells the row name. AC2 runs on an unmodified copy.
- **Consequence:** a `check_guard_lines` that catches a JSON error and returns with zero lines read passes AC1 to AC4. It reads an unparsable manifest as zero dead guard lines. This is a coverage gap in a criterion, not wrong shipped behaviour.
- **Fix (judged sound by the skeptic):** add a staging, for example BAD_JSON (one trailing comma inserted into the copy's `tools/gate-legs.json`), and a criterion expecting a `guard-trace` `WRONG` naming `policy fixtures`. Or narrow S2's text to the missing-row case.
- **Note:** if M10's fix drops `check_guard_lines`, this item lapses with it.
- **Left-shift gate:** as L2.

### L4 — Spec 35's digit-tail arm goes dead once spec 43 lands (id 16)

- **Where:** `memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-35.md`, section 2 S1 (the `.pyc.<digits>` tail, lines 30-35) and AC1's "Red when". Class: guard-above-a-fold-makes-its-fallback-dead.
- **What is wrong:** spec 43 S9 (lines 78-80, pseudocode line 168) drops a mode-None `open` whose flags carry O_CREAT, O_WRONLY or O_RDWR before the path steps. importlib's atomic temporary is opened exactly that way. Unit 43 builds at order 14, after unit 35 at order 12, so from then on the digit-tail arm sees no input. Spec 35 never marks it interim. Separately, this node's shell sets PYTHONDONTWRITEBYTECODE=1, so no temporary is written at all.
- **Consequence:** a dead arm and a red path that cannot fire both read as coverage. The "cold" observation depends on an environment this node does not provide.
- **Fix:** the finder's fix was judged unsound. The skeptic's corrected fix is to mark the digit-tail arm interim in spec 35 S1, and say TOOL-dGroundRules-43 S9 removes it. Add a matching scope item to spec 43 that deletes the tail cut once S9 drops the temporary's open. Do not drop the tail in unit 35 itself: between orders 12 and 14, `source_from_cache` would raise ValueError on the temporary, the path would be kept as spelled, and AC1 would go red. Make AC1 state its precondition: bytecode writing on, meaning PYTHONDONTWRITEBYTECODE unset for the run and no `sys.dont_write_bytecode` on the load path.
- **Left-shift gate:** add guard-above-a-fold-makes-its-fallback-dead to the bug-class checklist with this case as its example: a later unit's guard that pre-empts an earlier unit's arm must name and retire that arm.

### L5 — Spec 40 claims `check_writes_intersect` answers correctly today (id 17)

- **Where:** `memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-40.md`, section 3, first non-goal.
- **What is wrong:** section 3 says "Both answer correctly today for both pairs (§4 Evidence)". `check_writes_intersect` does not exist in the tree; TOOL-dGroundRules-32 S9 has yet to add it, and the Evidence probes only `overlaps`.
- **Consequence:** the next reader takes the Python rule as verified when it has never run. AC1 is red until unit 32 is built, and the spec does not say so. The effect is prose only.
- **Fix (judged sound by the skeptic):** reword: `overlaps` answers correctly today; `check_writes_intersect` is TOOL-dGroundRules-32 S9's and is first graded by AC1 once that unit is built.
- **Left-shift gate:** a checklist entry: "an Evidence claim about 'today' names only symbols that `grep` finds at HEAD".

### L6 — Spec 43's AC13 is green at HEAD and not marked as evidence (id 18)

- **Where:** `memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-43.md`, section 6 AC13 (lines 291-292).
- **What is wrong:** AC13's count is already 0 at HEAD, so it cannot fail on the build. Unlike AC3, it carries no PINNED or evidence-check marking, though S13 makes it an evidence statement.
- **Consequence:** the criterion certifies nothing about the build. Its "Red when" can only fire if someone tracks a local-state file.
- **Fix (judged sound by the skeptic):** mark AC13 as an evidence check ("figure: PINNED, a check on evidence"), as AC3 is, or pair it with a staged break: a scratch copy that tracks `.claude/mailbox/x`, after which the count is 1.
- **Left-shift gate:** a spec-tokens check that every criterion either carries a staged break or a PINNED marking.

### L7 — Spec 35 converts a bytes path with `str()` (id 34)

- **Where:** `memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-35.md`, section 2 S1, section 4 The mapping (`p = str(path)`).
- **What is wrong:** the `open` audit event passes a bytes path through unchanged, and `str(b'README.md')` yields the literal text `b'README.md'`. Unit 33's resolve and relativise steps then treat that text as a real path.
- **Consequence:** an in-process read through a bytes path is recorded under a garbled name. With unit 43 S9 in place, it lands in the absent count, so a real read is hidden. No bytes-path open exists in tools/ today.
- **Fix (judged sound by the skeptic):** use `p = os.fsdecode(path)` (str and bytes; PathLike via `os.fspath` first). State in S1 that str, bytes and PathLike paths are handled, with a criterion that stages one `open(b'README.md')` and expects `guard-trace · WRONG README.md`.
- **Grade note:** the skeptic re-graded this finding from medium to low, and low binds.
- **Left-shift gate:** a lint over tools/ that reds `str(path)` on an audit-hook argument.

### L8 — Spec 37 reads an empty guard list as clean (id 37)

- **Where:** `memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-37.md`, section 2 S2, section 4 The check (lines 77-85).
- **What is wrong:** the check reports `WRONG` only for an unparsable manifest or a missing row. A `policy fixtures` row with an empty or absent `guard` list prints `0 guard line(s) checked` with no `WRONG`. That contradicts S2's "never zero lines read as a pass".
- **Consequence:** the check certifies a guard holding nothing as clean. The effect is contained, because unit 33's join would then red every traced path.
- **Fix (judged sound by the skeptic):** make a row whose guard list is empty or missing a `WRONG` naming `policy fixtures`. Add a staging to AC4 that empties the guard list.
- **Note:** if M10's fix drops `check_guard_lines`, this item lapses with it.
- **Left-shift gate:** add empty-population-read-as-coverage to the bug-class checklist, if it is not already there.

### L9 — Spec 35 says a refused cache name surfaces as a WRONG (id 38)

- **Where:** `memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-35.md`, section 2 S1 (lines 33-35) and section 5 error states (lines 107-108).
- **What is wrong:** both say a cache name that `source_from_cache` refuses is "kept as spelled, so the trace names it as a WRONG". Every such path sits under `__pycache__`, which `.gitignore` ignores. TOOL-dGroundRules-36's set-aside, built at the same order, drops it into the count line instead.
- **Consequence:** an unmappable cache read is hidden in an aggregate count, not named, and the next reader is misled about what surfaces it. No behaviour depends on the sentence.
- **Fix (judged sound by the skeptic):** restate section 5 to say the refused name is counted in TOOL-dGroundRules-36's set-aside line. Alternatively, have the refused case emit its own named line, so it is visible after the set-aside.
- **Left-shift gate:** as M4. An error state that a sibling unit's filter can swallow must name that unit.

review-shape kind=spec-audit round=1 intensity=full at=synth raw=38 confirmed=33 refuted=5 unverified=0 blocker=1 high=7 medium=16 low=9 agents=11 out-tokens=186285

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes |
|---|---|---|---|---|---|---|---|---|
| 1 | coherence | memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-40.md:section 6, the PAIRS_SH literal (AC2, AC3); also consumed by TOOL-dGroundRules-43 section 6 AC1 | high | high | confirmed | Lines 125-126 of spec-40 spell PAIRS_SH as `. lib-unattended.sh; overlaps tools/policy/ x.py; ... overlaps a.py ab.py`. The lib is at tools/unattended/lib-unattended.sh, so the bare source fails from the root. Even with the path fixed, the covers/overlaps code (lib-unattended.sh:741-746) returns 1 for `tools/policy/` against `x.py` and 1 for `a.py` against `ab.py`. AC2 expects `0` then `1`, so it cannot pass on a correct build. TOOL-dGroundRules-43 AC1 (:253) runs this same literal, so it inherits the failure. | unsound | - |
| 2 | coherence | memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-41.md:section 6, the INSTALL_LINES and HELP_LEGS literals (AC4, AC5) against section 2 S2 and S3 | high | high | confirmed | Lines 119-120 of spec-41 read `awk ... policy.md` and `--legs-for policy.md`, while S1, S2 and S3 name help/policy.md. When I ran `python tools/check-spec-tokens.py --legs-for policy.md` it printed `REFUSING — no path given is tracked at HEAD: policy.md` with rc=2. Nothing builds a policy.md at the repository root, so AC4 prints 0 and AC5 never names `policy fixtures`, even on a correct build. | sound | - |
| 3 | coherence | memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-43.md:section 6, the EVIDENCE literal (AC3) against section 2 S3 and section 4 Evidence | medium | medium | confirmed | Line 227 of spec-43 defines EVIDENCE as `git show f4d31452a:README.md \| grep -n gen:build-order`. When I ran it, it printed nothing (rc=1). The same grep over memory/builds/dGroundRules/README.md at that revision printed `165:` and `179:`, so AC3 as spelled cannot pass. | sound | - |
| 4 | coherence | memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-35.md:section 6 AC1, AC2 against section 2 S2; ordering against TOOL-dGroundRules-36 (both order 12, step 12 parallel) | medium | medium | confirmed | Spec-35 AC1 and AC2 (:131-137) pass only when no guard-trace WRONG appears. The only positive check is AC3, which runs warm. Spec-36 S1 (:30-34) sets aside, before the join, every kept path that check-ignore prints. .gitignore ignores __pycache__/ and *.pyc, and both specs sit at order 12, which the README marks parallel. If 36 lands first, a .pyc kept by an unbuilt or broken 35 is set aside and never shows as WRONG. AC1 and AC2 then pass vacuously, and the cold-path rule 'keeps no path ending in .pyc' goes unobserved. | sound | - |
| 5 | coherence | memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-38.md:section 3 Edges (consumes-from TOOL-dGroundRules-34) and section 1 order rationale | medium | medium | confirmed | Spec-38 line 55 declares `consumes-from TOOL-dGroundRules-34`, but its Status line says order 12, the same step as 34 in the README build-order (step 12, Parallel yes). Lines 25-27 justify order 12 from unit 33 alone. The siblings 39, 40 and 41 also consume 34, and they sit at order 13. That is the convention 38 breaks. 34 :270 has a matching hands-off edge to 38. | sound | - |
| 6 | coherence | memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-36.md:section 4 Files touched, across TOOL-dGroundRules-34/35/36/37/38 (step 12) and 39/41 (step 13) | medium | medium | confirmed | The 'Files touched' sections show these overlaps: - 35, 36, 37 and 38 all list tools/policy/check_policy.py, and 36, 37 and 38 also list memory/map/generated/symbols.json. - 34 writes check_policy.py as well; spec-43 :156 and :198 itself says the writers fail M6's first clause. - 39 and 41 both list check_policy.py and sit at step 13. The README marks steps 12 and 13 Parallel `yes`. BUILD-METHOD.md:209-214 requires disjoint write sets and forbids a shared generated index together with its generator. No edge sequences these units. | sound | - |
| 7 | coherence | memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-43.md:section 6, the ORDER_SHIFT staging (AC6) | low | low | confirmed | `grep ... \| sort \| uniq -c` over the spec Status lines printed a count of 1 for orders 10, 11 and 14, held by units 32, 33 and 43. Shifting one of those to an unused value leaves the distinct count unchanged, so AC6 (:269) would fail. ORDER_SHIFT (:231) does not say which unit to pick. | sound | - |
| 8 | coherence | memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-38.md:section 2 S1 against section 6 AC3, AC4 | low | low | confirmed | Spec-38 S1 (:31-34) says a failing rev-parse is a WRONG naming rev-parse with no case run, and cites AC3 and AC4 as its observers. AC3 (:140-143) only prints the directories, from a worktree and a clone. AC4 (:144-147) compares verdicts from a non-repository working directory, with the kit named by its absolute path, so the source still resolves. Neither stages a rev-parse failure, so no criterion observes the deny branch. | sound | - |
| 9 | coherence | memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-37.md:section 2 S2 against section 6 AC4 | low | low | confirmed | I re-read spec-37. At lines 37-39, S2 makes two promises: a manifest that does not parse is a WRONG, and a missing `policy fixtures` row is a WRONG. It says both are 'Observed by AC2, AC4'. The only manifest staging in the section-6 block is NO_ROW, which respells the row name, and AC4 stages only NO_ROW. AC2 runs on an unmodified copy. So no criterion exercises the parse-failure branch, and a builder could catch the JSON error and return zero lines while still passing AC1 to AC4. This is a coverage gap in a criterion, not wrong shipped behaviour. | sound | - |
| 10 | grounding | memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-40.md:section 6, the PAIRS_SH literal (AC2, AC3) | high | high | confirmed | Spec-40 lines 125-126 read `PAIRS_SH = bash -c '. lib-unattended.sh; overlaps tools/policy/ x.py; echo $?; overlaps a.py ab.py; echo $?'`. Spec-34:509 has the same stripped form. Spec-40's own Goal (line 23) names this as the H3 defect the unit exists to remove, and S3 promises AC16 'restated whole'. I ran it from the repository root after sourcing tools/unattended/lib-unattended.sh. `overlaps tools/policy/ tools/policy/x.py` gave 0, `overlaps tools/policy/a.py tools/policy/ab.py` gave 1, and `overlaps tools/policy/ x.py` gave 1. With the bare source path the function is not defined at all. So AC2, the PAIRS_SH half of AC3, and spec-43 AC1, which reuses PAIRS_SH, can never pass on a correct build. PAIRS_PY in the same block spells its paths whole. | sound | - |
| 11 | grounding | memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-41.md:section 6, the INSTALL_LINES and HELP_LEGS literals (AC4, AC5) | high | high | confirmed | Spec-41 lines 119-120 spell INSTALL_LINES as `awk ... policy.md` and HELP_LEGS as `--legs-for policy.md`. S1, S2, S3 and line 66 all place the page at help/policy.md, and S3 promises AC36 'restated whole'. Spec-34:586 has the same bare form. I ran `python tools/check-spec-tokens.py --legs-for policy.md` and it printed `legs-for: REFUSING — no path given is tracked at HEAD: policy.md` with rc=2. No root-level policy.md exists. So AC5 can never name `policy fixtures`, and on the built tree, where help/policy.md exists, AC4's awk cannot open `policy.md`. | sound | - |
| 12 | grounding | memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-43.md:section 6, the EVIDENCE literal (AC3); AC1 | high | medium | confirmed | Spec-43:227 reads `EVIDENCE = git show f4d31452a:README.md \| grep -n gen:build-order`. Line 129 cites memory/builds/dGroundRules/README.md instead. I ran the literal and it printed nothing (rc=1). `git show f4d31452a:memory/builds/dGroundRules/README.md \| grep -n gen:build-order` printed 165 and 179, the lines AC3 expects. So AC3 can never pass. The defect is confined to an evidence criterion; AC1's inherited failure is the same defect as id=10. | sound | - |
| 13 | grounding | memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-36.md:section 2 S1 and section 4 'The set-aside' (stdin = "\n".join(kept), ignored = set(out.splitlines())) | medium | medium | confirmed | Spec-36:76 pins `run(git -C top check-ignore --stdin, stdin = "\n".join(kept))` and sets neither -z nor byte mode. In a scratch repository with `*.pyc` ignored I ran `git check-ignore --stdin` from Python three ways. Text-mode input 'a.pyc\nb.pyc\n' gave rc 1 and empty output. The same input as bytes gave rc 0 and both paths. Input 'a.pyc\né.pyc' gave rc 0 with only '"\\303\\251.pyc"', a C-quoted path that will never equal the kept path. Under the house-style text-mode call, ignored paths other than the last are not set aside, and non-ASCII paths are never set aside. | sound | - |
| 14 | grounding | memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-43.md:section 6, the ORDER_SHIFT literal (AC6) | medium | medium | confirmed | Spec-43:231 makes ORDER_SHIFT change 'one unit spec's "· order <n>"' without naming a unit, and AC6 expects ORDERS to print one more than ORDER_ROWS. I counted Status-line orders across spec/*.md: orders 10, 11 and 14 each have a single holder. Shifting a sole holder swaps one distinct value for another, so `sort -u \| wc -l` stays the same and AC6 fails on a correct comparison. | sound | - |
| 15 | grounding | memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-38.md:section 6, the PRIMARY literal (AC1, AC2); section 7 arm line 'a primary clone of the built tree' | medium | medium | confirmed | Spec-38:126 reads `PRIMARY = git clone -q <this repository> "$TEMP/gr38"`. The arm line (:156) calls the clone 'a primary clone of the built tree', and nothing in the spec says AC1 and AC2 run after the unit's commit. A clone carries committed objects only. Cloning this repository also checks out the source's HEAD branch, not necessarily this worktree's branch. So before the commit, the clone grades a check_policy.py without read_source_git_dirs. Line 105 shows the spec knows about the before-commit problem for unit 36 but does not apply it here. I did not run a clone, which the probe policy bars; this rests on git clone semantics. | sound | - |
| 16 | grounding | memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-35.md:section 2 S1 (the `.pyc.<digits>` tail) and AC1's 'Red when' | low | low | confirmed | Spec-35 S1 (lines 30-35) adds a `.pyc.<digits>` tail cut for importlib's atomic-write temporary. Its evidence (:65) says that temporary arrives as an open event with mode None. Spec-43 S9 (:78-80, pseudocode :168) drops a mode-None open whose flags carry O_WRONLY, O_RDWR or O_CREAT, which is how importlib's _write_atomic opens the temporary. Unit 43 builds at order 14, after unit 35 at order 12, so from then on the tail arm sees no input, and spec-35 never marks it interim. Separately, `env \| grep PYTHON` on this node printed PYTHONDONTWRITEBYTECODE=1. With that set no temporary is written, so the 'temporary write is kept' half of AC1's Red-when cannot fire. The effect is a dead arm and an unfireable red path, so low. The fix is unsound only because of its 'drop the tail' alternative: between orders 12 and 14, source_from_cache would raise ValueError on the temporary, the path would be kept as spelled, and AC1 would go red until unit 43 lands. The interim-marking alternative and the bytecode precondition are sound. | unsound | guard-above-a-fold-makes-its-fallback-dead |
| 17 | grounding | memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-40.md:section 3, first non-goal | low | low | confirmed | Spec-40 §3, first non-goal, reads 'Both answer correctly today for both pairs (§4 Evidence)'. I ran `grep -rn check_writes_intersect tools \| wc -l` and it printed 0, so the function does not exist yet. §4 Evidence itself only places it under TOOL-dGroundRules-32 S9 and records a probe of `overlaps` only. The claim is false for the Python rule, but it is prose with no effect on behaviour. | sound | - |
| 18 | grounding | memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-43.md:section 6 AC13 | low | low | confirmed | At HEAD, `git ls-files .claude \| grep -cE '^\.claude/(worktrees/\|scheduled_tasks\.lock\|mailbox/)'` printed 0, so AC13 (spec-43 :291-292) is green before the build. It carries no PINNED or 'check on evidence' figure line, unlike AC3 (:262). S13 makes it an evidence statement, so the marking is the gap. The effect is contained. | sound | - |
| 19 | reuse | memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-37.md:section 2 S1-S3, section 3 second bullet, section 10 | medium | medium | confirmed | tools/run-gates/run-gates.test.sh:619-660 (arm 1b) already holds every row's guard and doc_reads entry to `git ls-files`. It resolves {prefix} through the inlined, parity-gated resolve_prefix_token block and matches at a path-component boundary. The `run-gates canary` leg's guard is ['{prefix}/', '{prefix}/gate-legs.json', '{prefix}/lib/'], so any edit to the manifest runs that arm. Spec-37 AC1 (an untracked .pyc appended) and AC3 (an unstaged new file reds, then passes once staged) are exactly what the arm already catches. The §10 reuse audit never names the arm. §4 hand-rolls `entry with "{prefix}" as troot` instead of inlining the canonical block, which tools/lib/resolve_prefix_token.py:1-9 requires of every consumer. That makes a second carrier of the same rule. | sound | - |
| 20 | reuse | memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-40.md:section 6 PAIRS_SH, AC2 (and TOOL-dGroundRules-43 section 6 AC1, which names PAIRS_SH) | high | high | confirmed | Spec-40 lines 125-126 spell PAIRS_SH with a bare `. lib-unattended.sh` and the stripped pairs. I ran it from the repository root and it printed `No such file or directory`, then 127 and 127. With tools/unattended/lib-unattended.sh sourced, `overlaps tools/policy/ x.py` gave 1 and `overlaps a.py ab.py` gave 1, where AC2 expects 0 then 1. `overlaps tools/policy/ tools/policy/x.py` gave 0 and `overlaps tools/policy/a.py tools/policy/ab.py` gave 1. AC2 cannot pass on a correct build, and spec-43 AC1 (:253), which names PAIRS_SH, inherits the failure. This contradicts §1's promise that its own criteria spell the pairs whole. | sound | - |
| 21 | reuse | memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-43.md:section 6 EVIDENCE, AC3 (S3) | high | high | confirmed | Spec-43 :227 reads `EVIDENCE = git show f4d31452a:README.md \| grep -n gen:build-order`. I re-ran it and it printed nothing (rc=1). The whole path, `git show f4d31452a:memory/builds/dGroundRules/README.md \| grep -n gen:build-order`, printed 165 and 179, which matches §4 Evidence (:129-131). AC3 is red on a correct build. | sound | - |
| 22 | reuse | memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-41.md:section 6 INSTALL_LINES, HELP_LEGS, AC4, AC5 | high | high | confirmed | Spec-41 :119-120 spell INSTALL_LINES over a bare `policy.md` and HELP_LEGS as `--legs-for policy.md`. `ls policy.md` printed 'cannot access'. I ran `--legs-for policy.md` and it printed 'REFUSING — no path given is tracked at HEAD' (rc=2), and the bare name stays untracked on any build. So AC4 prints 0 and AC5 never names `policy fixtures`, even though S1-S3 spell help/policy.md. The fix is sound: on the built tree, help/policy.md exists (TOOL-dGroundRules-1 S8) and S2 adds it to the guard. | sound | - |
| 23 | blast-radius | memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-40.md:section 6, PAIRS_SH and AC2 (and TOOL-dGroundRules-43 section 6 AC1, which reuses PAIRS_SH) | high | - | refuted | duplicate of id=20. Same PAIRS_SH literal (spec-40 :125-126), same AC2 and spec-43 AC1. I re-observed it: 127 and 127 with the bare source, and 1 and 1 with the stripped pairs once the library is sourced. | sound | - |
| 24 | blast-radius | memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-41.md:section 6, INSTALL_LINES and HELP_LEGS (AC4, AC5) | high | - | refuted | duplicate of id=22. Same INSTALL_LINES and HELP_LEGS literals (spec-41 :119-120) and the same AC4 and AC5. I re-observed `--legs-for policy.md`: REFUSING, rc=2. | sound | - |
| 25 | blast-radius | memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-43.md:section 6, EVIDENCE and AC3 | medium | medium | confirmed | Unit 43 §6 line 227 reads `EVIDENCE = git show f4d31452a:README.md \| grep -n gen:build-order`, but §4 Evidence (line 129) names `memory/builds/dGroundRules/README.md`. I re-ran it: the root-README form printed nothing (rc=1), and `git show f4d31452a:memory/builds/dGroundRules/README.md \| grep -n gen:build-order` printed `165:<!-- gen:build-order -->` and `179:<!-- /gen:build-order -->`. AC3 (line 260) is red on a correct build. The effect stays inside an evidence check. | sound | - |
| 26 | blast-radius | memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-39.md:section 6 AC2, AC3 (with TOOL-dGroundRules-36 S1, -37 S2, -38 S1) | medium | medium | confirmed | Unit 39 §6 AC2 and AC3 say only that the run 'prints `WRONG`' in 'a scratch copy'. Nothing in unit 39, TEMPLATE-SPEC, BUILD-METHOD or the sibling specs defines a scratch copy as a git repository; a grep found only unit 15:153. Unit 38 runs at order 12, before unit 39 at order 13. Its S1 (lines 31-34) makes a failed `rev-parse` the run's `WRONG` with no case run, and unit 36 S1 makes a check-ignore failure a `WRONG`. So a scratch copy that is not a repository prints a `WRONG` that is not `census-window-edge`'s, and both staged-break criteria go green without the window being probed. Unit 38's own PRIMARY uses `git clone` (line 127), which shows the gap is real. | sound | - |
| 27 | blast-radius | memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-40.md:section 4 'The arm' and section 7 | medium | - | refuted | The premise is false on re-probe. tools/check-spec-tokens.test.sh:250-251 stops the suite after its first arm when FOREIGN_PREFIX_PROBE=1 and prints `foreign-prefix-probe: stopped after 1 arm`. The foreign-prefix leg runs every suite that way (foreign-prefix.gov.test.sh header, step 5). The arm unit 40 adds goes into an existing suite after that first arm, so it never runs at a foreign prefix. Neither the arm nor the foreign-prefix parity leg can red as claimed. At gov's own `tools/` prefix, where the bar runs the arm, `. tools/unattended/lib-unattended.sh` resolves (I sourced it from the root and it returned 0/1). The spelling differs from the suite's resolve_kit_dir convention at line 194, but the consequence the finding claims does not occur. | sound | - |
| 28 | blast-radius | memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-42.md:section 2 S4 and section 4 | low | - | refuted | This is a preference with no graded defect. gotchas.py:684-690 shows that a tier over CHECKLIST_FULL_BUDGET=12 prints one line per class. That is the budget's designed behaviour, and line 78 says no class ever leaves the checklist, so selection does not change. S4 states that selecting every spec commit is the intent. Measured over this spec set (units 35-43), `gotchas.py --for-paths` printed `0 path · 6 directory · 3 basename`; one more directory-tier class makes 10, which is under 12, so nothing compacts. The 4/6/2 harness checklist the finder cites is not reproducible here. In the for-diff case the finder cites, the basename tier is already compacted before this unit. | unsound | - |
| 29 | failure-envelope | memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-40.md:section 2 S1, section 4 The arm (OVERLAP_PAIRS), section 6 AC3 | blocker | blocker | confirmed | Unit 40 §4 OVERLAP_PAIRS (lines 76-77) labels `tools/policy/a.py` / `tools/policy/ab.py` the string-prefix row. I re-ran `python -c` on it: `a.startswith(b) or b.startswith(a)` printed False, because neither string prefixes the other. A raw startswith gives the same answer as containment on both rows: True on the directory row and False on this one. The arm therefore passes a check_writes_intersect or covers staged to a raw startswith, which is the regression its goal and the Alternatives-rejected section (lines 100-101) say it catches. AC3 (lines 136-137) expects `True then True` / `0 then 0` under RAW_BOTH, which cannot happen. The finder's replacement pair works: `overlaps tools/policy/a tools/policy/ab.py` returned 1 under the real covers (disjoint), while a raw startswith answers True. | sound | - |
| 30 | failure-envelope | memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-40.md:section 6 PAIRS_SH, AC2 (and TOOL-dGroundRules-43 section 6 AC1, which reuses it) | high | medium | confirmed | Unit 40 §6 lines 125-126 spell PAIRS_SH as `bash -c '. lib-unattended.sh; overlaps tools/policy/ x.py; echo $?; overlaps a.py ab.py; echo $?'`, a bare source with stripped pairs, although line 118 says the probes are 'spelled whole'. I ran it from the root: `lib-unattended.sh: No such file or directory`, then `overlaps: command not found` and `127` twice. With the full path, `overlaps tools/policy/ tools/policy/x.py` printed 0, and the stripped `overlaps tools/policy/ x.py` printed 1. AC2 cannot print `0 then 1` on a correct build, and unit 43 AC1, which reuses PAIRS_SH, is red too. The effect is that two criteria stay red; the build ships no wrong result. | sound | - |
| 31 | failure-envelope | memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-41.md:section 6 INSTALL_LINES and HELP_LEGS, AC4 and AC5 | high | medium | confirmed | Unit 41 §6 lines 119-120 spell INSTALL_LINES with `... f' policy.md` and HELP_LEGS with `--legs-for policy.md`, both bare, although S1-S3 and §4 name `help/policy.md` and line 22 itself says a bare `policy.md` does not resolve from the root. I re-ran both: awk printed `fatal: cannot open file 'policy.md'` and the count was 0. `check-spec-tokens.py --legs-for policy.md` printed `REFUSING — no path given is tracked at HEAD: policy.md` with rc=2. AC4 and AC5 cannot pass on a correct build. The effect is contained to two red criteria. | sound | - |
| 32 | failure-envelope | memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-43.md:section 6 EVIDENCE, AC3 | high | - | refuted | duplicate of id=25. It is the same defect: unit 43 §6 line 227 EVIDENCE reads the root README.md, so AC3 cannot print 165 and 179. My re-probe printed nothing for the root README and printed lines 165/179 for memory/builds/dGroundRules/README.md, as id=25 records. | sound | - |
| 33 | failure-envelope | memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-36.md:section 2 S1, section 4 The set-aside (`ignored = set(out.splitlines())`) | medium | medium | confirmed | Spec 36 §4 runs `git -C top check-ignore --stdin` without -z and builds `ignored = set(out.splitlines())`, then keeps `p not in ignored` and returns len(ignored). I re-ran the probe: `git check-ignore --stdin` over `tools/gövkit/__pycache__/x.pyc` printed `"tools/g\303\266vkit/__pycache__/x.pyc"` with rc=0, and core.quotepath is unset, so the default quoting applies. The quoted line never equals the kept path. That path is counted in n and still sent to the --legs-for join, where it comes out as a false guard-trace WRONG. The input class is narrow and the error is a false red, so the effect is contained. | sound | - |
| 34 | failure-envelope | memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-35.md:section 2 S1, section 4 The mapping (`p = str(path)`) | medium | low | confirmed | Spec 35 §4 adds `p = str(path)` ahead of unit 33's resolve, and neither spec deals with bytes paths. I re-probed: an audit hook recorded `('open','bytes',b'README.md','r')` for `open(b'README.md')`, and `repr(str(b'x'))` printed `"b'x'"`. So the kept name is garbled to `b'README.md'`. With unit 43 S9 in place, `(top/p).exists()` is false for that name, so the read lands in the absent count, not a WRONG. The real read is hidden either way. A grep of tools/ for fsencode or `open(b'` found no bytes-path opens, so nothing in the tree reaches this path today, which is why I grade it low. | sound | - |
| 35 | failure-envelope | memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-35.md:section 2 S1 and S2, section 4 The mapping (the `parent name == "__pycache__"` test) | medium | medium | confirmed | Spec 35 S1 maps a cache read only when its parent directory is named `__pycache__`. I re-probed with PYTHONPYCACHEPREFIX set: the cache opened as `<pfx>\Users\...\kit\m.cpython-314.pyc`, whose parent is `kit`, and the path sits outside the top level. A warm load therefore records nothing for the source. Nothing in the env, .github, tools/run-gates or tools/policy sets a prefix, so the false green only happens on a node configured that way. | unsound | - |
| 36 | failure-envelope | memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-43.md:section 2 S10, section 6 EXCLUDES_REPO and AC10 | medium | medium | confirmed | Spec 43 S10 passes the `--type=path` value through unchanged, and EXCLUDES_REPO does not say whether that value is absolute. I re-probed: in r1 with `core.excludesFile excl.txt`, `--get` printed `excl.txt` and status hid secret.local. `git -C r2 -c core.excludesFile=excl.txt status --porcelain` listed `?? secret.local`. So a relative value is read against the snapshot's top level, and AC10 can pass on a build where an absolute fixture value hides the hole. The snapshot is a scratch repository, so the leak is contained. | sound | - |
| 37 | failure-envelope | memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-37.md:section 2 S2, section 4 The check | low | low | confirmed | Spec 37 §4 (lines 77-85) reports WRONG only when JSON parsing fails or the row is absent. It then prints `len(row guard)` and loops over the entries. An empty guard list prints `0 guard line(s) checked` with no WRONG, which contradicts S2's 'never zero lines read as a pass'. The effect is contained: as the finder notes, unit 33's join would red every traced path. | sound | - |
| 38 | failure-envelope | memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-35.md:section 2 S1 and section 5 error states | low | low | confirmed | Spec 35 S1 (lines 33-35) and §5 (lines 107-108) say a cache name that source_from_cache refuses is kept so the trace names it as a WRONG. Every such name sits under `__pycache__`. I re-ran check-ignore and it echoes such a path with rc=0, and `.gitignore` holds `__pycache__/`. Spec 36's set-aside therefore drops it into the count line. Unit 43's absent filter does not change this, because the file exists. The stated outcome is wrong, but no behaviour depends on it. | sound | - |
