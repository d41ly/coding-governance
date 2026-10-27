**Serves:** spec-audit TOOL-dLinkedLibrary-1@rev-1 TOOL-dLinkedLibrary-10@rev-1 TOOL-dLinkedLibrary-11@rev-1 TOOL-dLinkedLibrary-12@rev-1 TOOL-dLinkedLibrary-13@rev-1 TOOL-dLinkedLibrary-14@rev-1 TOOL-dLinkedLibrary-15@rev-1 TOOL-dLinkedLibrary-16@rev-1 TOOL-dLinkedLibrary-17@rev-1 TOOL-dLinkedLibrary-18@rev-1 TOOL-dLinkedLibrary-19@rev-1 TOOL-dLinkedLibrary-2@rev-1 TOOL-dLinkedLibrary-20@rev-1 TOOL-dLinkedLibrary-21@rev-1 TOOL-dLinkedLibrary-22@rev-1 TOOL-dLinkedLibrary-23@rev-1 TOOL-dLinkedLibrary-24@rev-1 TOOL-dLinkedLibrary-25@rev-1 TOOL-dLinkedLibrary-3@rev-1 TOOL-dLinkedLibrary-4@rev-1 TOOL-dLinkedLibrary-5@rev-1 TOOL-dLinkedLibrary-6@rev-1 TOOL-dLinkedLibrary-7@rev-1 TOOL-dLinkedLibrary-8@rev-1 TOOL-dLinkedLibrary-9@rev-1

# Tier-2 spec audit — dLinkedLibrary, the 25 unit specs, round 1

Provenance: adversarial review by five finder lenses (gov-spec-reviewer) and five skeptic batches (gov-skeptic), synthesized by gov-synthesizer on 2026-10-26.

Reviewed: memory/builds/dLinkedLibrary/spec/2026-10-26-spec-TOOL-dLinkedLibrary-1.md@7b7415bd50957dc80197363aea7ee14942ea1ef4, memory/builds/dLinkedLibrary/spec/2026-10-26-spec-TOOL-dLinkedLibrary-10.md@ff884d4115e894783cd7c0775746f23213929b72, memory/builds/dLinkedLibrary/spec/2026-10-26-spec-TOOL-dLinkedLibrary-11.md@4b8e7039c2f28e48c30f4d08f9bf24c6aa405d2e, memory/builds/dLinkedLibrary/spec/2026-10-26-spec-TOOL-dLinkedLibrary-12.md@8c4383751c0c9f155e5bbb2fc1c2b3d68b97afb8, memory/builds/dLinkedLibrary/spec/2026-10-26-spec-TOOL-dLinkedLibrary-13.md@3f798758204692b87c533ae138a068a0e0738535, memory/builds/dLinkedLibrary/spec/2026-10-26-spec-TOOL-dLinkedLibrary-14.md@21e91651ac985612066177e0822d2da4d7a6a241, memory/builds/dLinkedLibrary/spec/2026-10-26-spec-TOOL-dLinkedLibrary-15.md@a99b23e76f295ac5c8c76de9409fc4148e585eab, memory/builds/dLinkedLibrary/spec/2026-10-26-spec-TOOL-dLinkedLibrary-16.md@7c101435d2cbf0a5d5bc7f6edb54c676be19da7f, memory/builds/dLinkedLibrary/spec/2026-10-26-spec-TOOL-dLinkedLibrary-17.md@ad06fb5d7f187283f78dfb3a994623e48213b4d8, memory/builds/dLinkedLibrary/spec/2026-10-26-spec-TOOL-dLinkedLibrary-18.md@4fc9cdc4cc824d0071e0818a946c3ee99c887ef7, memory/builds/dLinkedLibrary/spec/2026-10-26-spec-TOOL-dLinkedLibrary-19.md@99f10e918e0fc9b40c65e4c8a1d4f231b6dce0e1, memory/builds/dLinkedLibrary/spec/2026-10-26-spec-TOOL-dLinkedLibrary-2.md@b0f4cbf7087ea19e30cdd377480f19c1432aa72d, memory/builds/dLinkedLibrary/spec/2026-10-26-spec-TOOL-dLinkedLibrary-20.md@28f93c5c65a7baeda74315757f55f780915c8690, memory/builds/dLinkedLibrary/spec/2026-10-26-spec-TOOL-dLinkedLibrary-21.md@b27ad15715a4521878799caec9bcdb29662a6fbe, memory/builds/dLinkedLibrary/spec/2026-10-26-spec-TOOL-dLinkedLibrary-22.md@5536733d87d9bb8cb8728e6e0031545621141940, memory/builds/dLinkedLibrary/spec/2026-10-26-spec-TOOL-dLinkedLibrary-23.md@94b03b06fe50877febaf4adcceb78cd5f58fb92f, memory/builds/dLinkedLibrary/spec/2026-10-26-spec-TOOL-dLinkedLibrary-24.md@a4c5d0feb28a694eee6a77925f9279cacf96e08b, memory/builds/dLinkedLibrary/spec/2026-10-26-spec-TOOL-dLinkedLibrary-25.md@d1aa99b58dc5845ebdc95dfae74214e856df3156, memory/builds/dLinkedLibrary/spec/2026-10-26-spec-TOOL-dLinkedLibrary-3.md@455f52769efb6b40835d0f03c0d0e9513d7d99a1, memory/builds/dLinkedLibrary/spec/2026-10-26-spec-TOOL-dLinkedLibrary-4.md@340fbdb7470dffdb09507e9307edb770b0c5efec, memory/builds/dLinkedLibrary/spec/2026-10-26-spec-TOOL-dLinkedLibrary-5.md@36e2e6cf3833d824cf8c6afe454312c1248a14d8, memory/builds/dLinkedLibrary/spec/2026-10-26-spec-TOOL-dLinkedLibrary-6.md@e205ee07a0ba1a748733ef458243db696bdd4d64, memory/builds/dLinkedLibrary/spec/2026-10-26-spec-TOOL-dLinkedLibrary-7.md@0f90c266b796c83ead9ad350d73aefa5a5a30c6b, memory/builds/dLinkedLibrary/spec/2026-10-26-spec-TOOL-dLinkedLibrary-8.md@f14349f50bef7e4a2b96a88f215cb2049d2c8ee7, memory/builds/dLinkedLibrary/spec/2026-10-26-spec-TOOL-dLinkedLibrary-9.md@2b3a75e49486c7e0f3ce0cb819f111215d1059ba
ROUND 1

## Verdict: BLOCKED

One blocker (R1) holds: unit 9's `record origin` leg reds every record the adopt program writes.
The tally by item is 1 blocker, 14 high, 44 medium and 12 low, 71 items in all.
The tally by raw confirmed finding is 1 blocker, 14 high, 50 medium and 14 low, 79 findings in all.
Eight items merge two or three findings that describe one defect, and each lists all of its ids.

## Review shape

Intensity full, raw 81, confirmed 79, refuted 2, unverified 0 (0 uncertain), precision 0.98.

| lens | returned | raw | confirmed | refuted | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|
| coherence | yes | 19 | 19 | 0 | 0 | 0 | 1.00 |
| grounding | yes | 10 | 10 | 0 | 0 | 0 | 1.00 |
| reuse | yes | 13 | 13 | 0 | 0 | 0 | 1.00 |
| blast-radius | yes | 15 | 14 | 1 | 0 | 0 | 0.93 |
| failure-envelope | yes | 24 | 23 | 1 | 0 | 0 | 0.96 |

## Run integrity

- Lenses 5/5 returned, 0 died. Skeptic batches 5/5 returned, 0 died.
- 0 contradictory verdicts demoted, 0 orphaned duplicate refutations demoted, 0 spurious verdicts discarded, 0 duplicates.
- Fixes on confirmed findings: 74 judged sound, 5 judged unsound (ids 5, 24, 58, 67, 76), 0 none proposed, 0 not judged. Each unsound fix is replaced below by the skeptic's corrected fix.
- Severity: 0 ungraded, 13 re-graded by the skeptic. Each item states the binding grade.
- Unverified findings: none.
- Lens notes: none supplied, so every lens ran on the kit's generic brief.
- Roles: finders gov-spec-reviewer, skeptic batches gov-skeptic, synthesis gov-synthesizer.
- Intent: 1 spec document supplied as `specs`, as sibling context.
- By design: none supplied.
- Move check: no checked subject moved.
- Checklist: none swept, because none exists. A zero count here is not evidence that the project's recurring bug classes are absent.

## Blocker

### R1 — Unit 9's origin derivation reds every adopt-program record [blocker] (id 58)

- **Where:** spec 9 §4 "The derivation" steps 2-5 and its table, against spec 8 S3, S6 and §4 "The kinds", and spec 23 S7.
- **What:** Step 2 takes the landing build from the record's folder. Step 4 takes the subject build from the served unit. For every routing record (`reconstructed@…`) and every instruction ruling (`imported:…`), the adopt program writes into the adoption build's own `build/` folder serving the adoption unit. So both steps land on the adoption build, step 5 answers `written`, and the table reds the record. The `reconstructed-but-written` plant encodes that red as correct.
- **Consequence:** The unguarded `record origin` leg is permanently red for every adopter that runs `adopt decisions` or `adopt instructions --rule`. The `reconstructed` value can never be green on the path that writes it.
- **Fix (finder's fix judged UNSOUND, skeptic's correction):** Ground green for `reconstructed@<sha8>` on provenance: `<sha8>` is an ancestor of L and each source is a blob there. Ground green for `imported:<path>` on `<path>` being a blob at L^ outside the memory root. Both hold whatever build folder the record sits in. Rewrite or retire the `reconstructed-but-written` plant, which becomes an exit-0 case. Add plants that mint a routing record and an instruction ruling through the real `adopt` program in the adoption build's own folder, each expecting exit 0.
- **Left-shift gate:** a cross-spec probe in the spec audit that runs each writer spec's record shape through each checker spec's derivation, so a value no writer can make green is caught at spec time.

## High

### R2 — Unit 19's per-seam reuse parts cannot exist under unit 1's part model [high] (id 1)

- **Where:** spec 19 §2 S3, with spec 1 §2 S1-S3.
- **What:** Unit 19 proposes `propose --feature <feature> --name <feature>-<ordinal>`, several entries per dossier. Unit 1 makes `--feature` a bare flag and a part exactly `<feature>.reuse.toml` beside `<feature>.md`, with tag `unit.reuse.<stem>` and `reuse.tag` `feature.<stem>`.
- **Consequence:** The 82 seam proposals cannot exist as unit 1 defines a part. An accepted `alpha-1.reuse.toml` is red under `check_reuse_entries`, because it has no `alpha-1.md` and its tag `feature.alpha-1` is not the feature node. The reuse view and the anchor join then read entries under the wrong feature tag.
- **Fix (judged sound):** Pick one model in both specs. Either unit 1 allows several parts per feature (`<feature>.<n>.reuse.toml`, with the check keyed on the stem before the first dot), or unit 19 merges a dossier's seams into one part. Spell `--feature` the same way in both specs.
- **Left-shift gate:** a spec-tokens arm that resolves every CLI invocation a spec writes against the owning spec's verb grammar.

### R3 — Unit 4's anchor arm reds unit 19's 82 proposals [high] (id 2)

- **Where:** spec 4 §2 S8 and §6 AC11, with spec 19 S3 and S6.
- **What:** S8 reds every `accepted` or `proposed` entry whose `anchors` string no line in the tree carries. Unit 19 (order 10) files 82 proposals with anchor `gov:feature <feature>`, and no unit writes a `gov:feature` line into code.
- **Consequence:** AC11 (`check --only feature` exits 0) cannot pass. Once unit 7 lands the unguarded `annotations` leg, every bar is red until someone weakens the arm or writes 32 unscoped anchors.
- **Fix (judged sound):** Choose one and state it in both specs: (a) S8 joins only `accepted` entries, printing proposed ones without red; (b) unit 19 proposes without `--anchor`; or (c) unit 19 or 4 writes each dossier's `gov:feature` line and lists the files in Files touched.
- **Left-shift gate:** a build-order replay in the spec audit that evaluates each AC against the tree state left by the earlier-ordered units.

### R4 — Unit 23 registers `gov:legacy` in the wrong registry [high] (id 3)

- **Where:** spec 23 §2 S9, §4 Files touched, §6 AC8.
- **What:** Unit 23 registers `marker.legacy` as a member row in `tools/playbook/namespaces.toml`. The member registry `check_marker_words` reads is unit 12's `tools/memory-tree/marker-words.toml` `[[marker]]` rows, and unit 12 rejected a members column on the namespace row. Unit 23 never names `marker-words.toml`.
- **Consequence:** `gov:legacy`, written by `adopt_instructions.py`, the render gate, the help page and `WIRE-INTO-PROJECT.md`, has no registry row. The `markers` arm reds `unregistered gov: word legacy` on every bar, and AC8 certifies a row the check never reads.
- **Fix (judged sound):** S9 adds a `[[marker]]` row (`word = "legacy"`, `kind = "pair"`, `reader = "tools/playbook/render_playbook.py"`, `owner = "TOOL-dLinkedLibrary-23"`) to `marker-words.toml`, lists the file in Files touched, and AC8 greps it there. Drop the `namespaces.toml` edit.
- **Note:** the reuse lens found the same defect at medium; it is R34 (id 35). The two are kept apart only because their binding grades differ, and one edit fixes both.
- **Left-shift gate:** a spec-tokens arm that checks every registry a spec writes to is the registry its owning spec names.

### R5 — Units 17 and 18 disagree on `iter_family`'s depth origin and lead grammar [high] (id 4)

- **Where:** spec 17 §2 S5 and §4 "The pairing walk", with spec 18 S2 and AC2.
- **What:** Unit 18 numbers a top-level span depth 1 (nested `b` is depth 2). Unit 17 refuses depth 1 or more as `nested` and reads a well-formed pair as depth 0. Unit 18's grammar puts the name directly after the lead, but unit 17 passes `"gov:note"`/`"gov:end"` while its lines carry a space before the tag.
- **Consequence:** The span arm either refuses every well-formed `gov:note`…`gov:end` pair as `nested`, or recognizes no marker at all and passes every malformed pairing. The second case is a check that certifies what it does not check.
- **Fix (judged sound):** Fix the depth origin in unit 18 S2 and make unit 17's table and S5 match it. Make unit 17's tuple `("gov:note ", "gov:end ", None)`, or let unit 18's grammar admit one space after the lead. Add a unit 18 AC2 case pinning a top-level span's depth.
- **Left-shift gate:** a shared-interface table in the spec brief that pins each primitive's return conventions (origin, delimiter) and is diffed against each consuming spec.

### R6 — Unit 3 points `MAP_CLI` at a file that exists only on a `win` verdict [high] (id 8)

- **Where:** spec 3 §2 S3 and S6, with spec 14 §8 F1.
- **What:** Unit 3 points `MAP_CLI`, and the adopter upgrade step, at `tools/memory-tree/gov_map.py`. TOOL-dTotalRecall-14 builds that file only on TOOL-dTotalRecall-17's `win`. Unit 14 handles the `lose` route, and unit 3 does not.
- **Consequence:** On `lose`, `MAP_CLI` names a missing file, `reuse-probed` always takes its announced skip, and reuse evidence is never graded at close. The upgrade witness passes while every adopter's `MAP_CLI` points at nothing.
- **Fix (judged sound):** State the `lose` route. Either point `MAP_CLI` at a CLI that exists under both verdicts (`gov_code.py` or `house_index.py`), or gate S3 and S6 on the verdict record as TOOL-dTotalRecall-14 AC1 does, with a deviation record on `lose`.
- **Left-shift gate:** a spec-audit arm that lists every path a spec depends on that another spec builds conditionally, and requires a stated route for each verdict.

### R7 — Unit 18's census query does not match its 18-row table [high] (id 20)

- **Where:** spec 18 §4 "The population", §2 S7, AC8.
- **What:** Run at HEAD, the census queries return many sites outside the table and miss `format-guard.js`, whose indented `const FENCE_OPEN =` the leading `^[A-Z_]*` cannot match. Real region parsers are among the extras: `check-microformats.sh:49` slices with awk `$0 == o`, and the run-gates suite slices `mempause_sh`.
- **Consequence:** AC8's `0 site(s) outside the factory` cannot be reached. The standing census arm stays red or gets narrowed by ad hoc exclusions, and real parsers stay outside the factory, against the clause's "every region parser".
- **Fix (judged sound):** Re-run the queries and make the table match. For each extra hit, either list it as a site to re-point (check-microformats.sh, run-gates.test.sh:3600, merge-rows.test.sh:396, unattended.test.sh:3220-3221, resolve-python.test.sh:550/600/678, check-unattended.test.sh:3705) or name a written exclusion rule (for example a heading constant read with `==`, or a comment line such as pyrun.sh:15). Widen the first query to find indented JS constants. State the census predicate exactly.
- **Left-shift gate:** a spec-tokens arm that re-runs every query a spec pins with its row count and diffs the output against the stated table.

### R8 — Unit 4's default resolve population is empty [high] (id 22)

- **Where:** spec 4 §2 S3 and S7, §4 Rollout, §5 perf.
- **What:** S3 limits scanned files to those `git grep -l "gov:(note|feature|end)"` returns, and S7 grades only comment lines of scanned files. Rollout says the default grades existing comment citations. At base no tracked file outside memory carries those words.
- **Consequence:** The default resolve arm grades nothing. Unit 11 seeds `annotation-resolve-legacy` from it (an empty seed) and deletes drift's `source_cited_ids_resolving_to_no_record`, which scans every tracked non-memory file and holds 2 findings today. A green gate over an empty population replaces a signal that read the citations. Spec 11 §5 assumes the opposite reading.
- **Fix (judged sound):** S7 states that `every-comment-ref` reads comment lines of every tracked file outside the memory root that the lexer can profile, with no `gov:` narrowing. Keep S3's narrowing for note rows only. Add a plant: a tree with no gov:note and one dangling id in a plain comment, the failing case being `unarmed` or 0 rows under the default.
- **Left-shift gate:** a rule that every replacement check states its population at base and must be non-empty where the retired signal's was.

### R9 — Unit 18's census cannot see govkit's `find_block`/`write_block` [high] (id 30)

- **Where:** spec 18 §4 "The population", S7 census query, §10.
- **What:** `tools/govkit/govkit.py` `find_block` (:5776) and `write_block` (:5806) reproduce the region contract by hand ("REPRODUCES the shipped splice's refusal table, deliberately"). Their markers come from `marker_pair()`, not module constants, so neither census query matches them.
- **Consequence:** AC8 and the standing census arm certify `0 site(s) outside the factory` while govkit splices adopter files with its own parser.
- **Fix (judged sound):** Add `find_block` and `write_block` to the population, re-pointed to `find_pair` and `splice_region`. Keep the zero-pair `None` return as a caller-side catch of `RegionError`. Widen the census predicate to parsers that take synthesized markers as arguments. Add a planted `find_block`-shaped parser with no marker constant to AC8's red case.
- **Left-shift gate:** a census whose predicate matches behaviour (a stripped line compared to a mark), with a planted constant-free parser as its red case.

### R10 — Units 14, 15 and 21 claim selftest coverage from a leg that runs no selftest [high] (id 49)

- **Where:** spec 14 §7 New arm line (also spec 15 :253 and spec 21 :232).
- **What:** The arm lines say `gov_code.py --selftest`, `code_enrich.py --selftest` and `code_ctags.py`'s arm run under the `code record` leg beside `code_record.py --selftest`. That leg (TOOL-dTotalRecall-8 S13) runs `code_record.py --check`, and no leg runs `code_record.py --selftest`. Neither spec 14 nor 15 touches `code_record.py` or `gate-legs.json`.
- **Consequence:** AC1-AC6 of units 14, 15 and 21 are recorded as re-observed by a leg that never invokes them. A regression in those modules passes every bar, a coverage claim nothing checks.
- **Fix (judged sound):** Give each selftest its own leg with its meta rows, or add a scope item for a selftest leg running `code_record.py --selftest` that calls the three modules' selftests. Name the leg truthfully on each arm line. Probe: break one plant in `gov_code.py` and confirm some leg reds.
- **Left-shift gate:** a spec-tokens arm that resolves each New arm line's named leg in `tools/gate-legs.json` and checks its argv invokes the named selftest.

### R11 — Unit 8 claims the `record-kinds` leg runs `adopt_program.py --selftest` [high] (id 50)

- **Where:** spec 8 §7 New arm line.
- **What:** The arm line says `adopt_program.py --selftest` runs under the `record-kinds` leg. That leg (TOOL-dTotalRecall-1 S3) runs `record_kinds.py --check`, and no scope item wires the call.
- **Consequence:** AC1-AC8 are recorded as re-observed by a leg that never runs them, so a router regression (for example writing a split candidate as major) passes every bar.
- **Fix (judged sound):** Add a leg `adopt program selftest` (argv `python {prefix}/memory-tree/adopt_program.py --selftest`) with its meta rows, or a scope item making an existing selftest leg call it. Correct the arm line.
- **Left-shift gate:** the same arm-line resolution gate as R10.

### R12 — Unit 12's marker registry ships gov's own rows to every adopter [high] (id 59)

- **Where:** spec 12 §2 S1 and S3, §4 "The census", §8 F1.
- **What:** `marker-words.toml` holds gov's 21 words with readers at gov paths and ships as `engine` (`include = "**"`). S1 refuses a row whose reader is untracked, and S3 refuses a registered word no file carries. The spec never addresses adopters, installs or `{prefix}`.
- **Consequence:** In an adopter without the unattended kit, or where gov-only tests (for example `tools/lib/resolve-python.test.sh`) are withheld, the `markers` arm and so the unguarded `annotations` leg are red from install on.
- **Fix (judged sound):** State the adopter envelope. Make the registry project-owned (shipped empty or seeded per installed kit), or key each row to its kit so a row whose kit is absent is skipped and announced. Resolve `reader` through `{prefix}` and read an absent reader as `not installed`. Add a plant: an adopter-shaped scratch tree holding only memory-tree, where the arm exits 0.
- **Left-shift gate:** a foreign-install probe that runs each new shipped check in a scratch adopter holding only its own kit.

### R13 — Unit 24's `--observe` certifies a class `gated` on any non-zero exit [high] (id 64)

- **Where:** spec 24 §2 S3, §4 "The derivation", §5.
- **What:** `--observe` records `refused` for any non-zero exit of the planted run, including crashes, exit-2 usage or environment errors and signals. No timeout is stated.
- **Consequence:** A plant that breaks the leg's script, a missing interpreter or a signal makes the class `gated`, and S5 then removes it from every review checklist: a gate claiming a refusal it never saw. A hanging run blocks `--observe` forever.
- **Fix (judged sound):** Record `refused` only when the planted run exits with the leg's failing status (1) and the clean run exits 0. Record exit 2 or more, a signal, or a run past a stated bound (for example the leg's `ceiling`) as `unobservable` with its reason. Add plants: a stub leg exiting 2 on the plant, and one sleeping past the bound, each expecting `unobservable` and `partly-gated`.
- **Left-shift gate:** a bug-class checklist entry: "a check that reads a child's exit must distinguish the failing status from error statuses and bound the run".

### R14 — Unit 19's `dossier_move.py apply` hard-codes gov's build and unit [high] (id 65)

- **Where:** spec 19 §2 S3, §4 Rollout.
- **What:** `apply` hard-codes `--build dLinkedLibrary --unit TOOL-dLinkedLibrary-19` and a record path under `memory/builds/dLinkedLibrary/`, yet Rollout makes `apply` every adopter's update step.
- **Consequence:** In an adopter, `propose --build dLinkedLibrary` refuses (no such build folder) or writes into a fake gov build folder, while the shipped prose test reds every dossier still holding prose. Every adopter updating codebase-map gets a red map gate and no working migration.
- **Fix (judged sound):** Make `--build` and `--unit` required arguments of `apply`, writing records and proposals under the caller's build. Add a fixture case with another build slug.
- **Left-shift gate:** a grep arm that refuses gov's own build slug or unit ids in any shipped kit file outside fixtures.

### R15 — Unit 8's CI census lets publishing jobs read `importable` [high] (id 67)

- **Where:** spec 8 §4 "The census", the `ci-job` row; §5 security.
- **What:** The census reads only `.github/workflows/*.yml`, parses YAML by indentation with no rule for block scalars, and refuses on six substrings. `.yaml` workflows are missed, and `git -C x push`, `yarn publish`, `pnpm publish`, `cargo publish` and `terraform apply` match no pattern. (The skeptic notes `gh release create` and `actions/deploy-pages` already match.)
- **Consequence:** An owner ruling `import` on such a job hands dShippedRelease a job that pushes or publishes as a gate leg, defeating the deny-by-default rule at the one place the spec prices it.
- **Fix (finder's fix judged UNSOUND, skeptic's correction):** Glob `.github/workflows/*.yml` and `*.yaml`. Read every line of a block-scalar `run:` and every job-level `uses:`. Normalise `git -C <dir>` and similar options before matching. Extend CI_REFUSE_PATTERNS to the publish and apply verbs of common package managers and IaC tools, and refuse any job granted `permissions: write` or `contents: write`, or referencing `secrets.`. Add plants for a `.yaml` workflow, a multi-line `run: |` with `npm publish` on line 3, `yarn publish` and `git -C x push`, each reading `refused`, plus a plain test job reading `importable`.
- **Left-shift gate:** a bug-class checklist entry: "a refusal list over free text needs plants for each input variant (extension, block scalar, option-prefixed verb)".

## Medium

### R16 — Unit 8 AC3's split plant cannot reach kappa 0.8 [medium] (ids 5, 24)

- **Where:** spec 8 §6 AC3.
- **What:** The four planted candidates (two agreed, two split) give Cohen's kappa 0.333 (p_o 0.5, p_e 0.25). Since kappa < p_o, the 0.8 floor can never be met. S6 exits 3 below 0.8 and writes no routing record.
- **Consequence:** AC3 cannot pass on a correct build, so the "a split is never major" rule goes unobserved and a builder will weaken the floor or rewrite the case. Id 5 was graded high by its finder and medium by the skeptic, and the binding grade is medium.
- **Fix (both finders' fixes judged UNSOUND, skeptic's correction):** Size the split plant to 20 candidates over the four classes: 18 agreed (5 major, 5 minor, 4 waiver, 4 process-rule) and 2 split ((major, minor) and (waiver, process-rule)). That gives p_o 0.9, p_e 0.25 and kappa 0.867. Pin `kappa 0.867 over 20 rows · pass` in AC3, keep both split rows' assertions (`Major` `no`), and restate the `--ratify` listings against the new count.
- **Left-shift gate:** a spec-audit arm that computes every pinned statistic in an AC from its planted rows.

### R17 — Unit 22's `decides` derivation misses three edited rows [medium] (id 6)

- **Where:** spec 22 §2 S6, §4 "The decision rows", §6 AC6.
- **What:** S6 matches each row's current text against added lines of one `git log --reverse -p`. TOOL-aMendedLedger-8, TOOL-aMendedLedger-9 and TOOL-aFoldedQuarry-9 were edited after landing or entered through a merge, so their current line was never added.
- **Consequence:** `row_grammar.py --decisions` reports `3 with no decides target` and exits 1, so AC6 cannot pass and a builder is tempted to loosen it.
- **Fix (judged sound):** Spec how such a row gets its target, for example the id's first-added line (`git log -S'<id> ·'`, with `-m` for merges) or the commit that introduced the id. Name the three rows in §4 as the measured population and add a plant for an edited row.
- **Left-shift gate:** the pinned-query re-run gate from R7, applied to every "0 with …" AC.

### R18 — Unit 11 deletes a signal that unit 25's guide names [medium] (id 7)

- **Where:** spec 11 §2 S6 Readers, §4 Files touched, §6 AC7, with spec 25 S7 and AC9.
- **What:** Unit 25 (order 1) writes `source_cited_ids_resolving_to_no_record` into `tools/memory-tree/ANNOTATION-STYLE.template.md` and `memory/guides/ANNOTATION-STYLE.md`. Unit 11 (order 14) deletes the signal but lists neither file.
- **Consequence:** AC7's `git grep … -- tools` fails on the template. If the builder leaves the guide, it names a deleted signal, the gap-mem-11 class unit 25 closes.
- **Fix (judged sound):** Add both guide files to S6's Readers and Files touched, and rewrite A1 to name the resolve arm and its ledger population. Alternatively unit 25 S7 names the signal conditionally. Unit 4 S12's amendment of A1 should name the end state.
- **Left-shift gate:** the build-order replay from R3, extended to Readers lists: a name deleted by a later unit must not be written by an earlier one without a listed reader.

### R19 — The instruction-paragraph `Ruling` values are spelled `drop` and `discard` [medium] (ids 9, 40, 63)

- **Where:** spec 23 §2 S7, §4 Inventory and Files touched (`record-kinds.toml`), against spec 8 §4 "The kinds".
- **What:** Unit 8, the kind's owner (order 20), closes the set as `unit`, `amend <tag>` or `drop`. Unit 23 (order 25) writes and parses `discard` and adds three values to the `ruling` row again. Unit 23 :30 itself says "a drop".
- **Consequence:** The door's field check refuses one spelling's records, so `--rule <key> discard` fails, or the row holds two words for one choice. Id 40 was graded low by its finder and medium by the skeptic, and the binding grade is medium.
- **Fix (judged sound):** Use `drop` in both specs (or amend spec 8 in one place). Unit 23 cites unit 8's values and drops the `record-kinds.toml` edit from its write set.
- **Left-shift gate:** a spec-tokens arm that checks every closed value a spec uses against the owning spec's registry row.

### R20 — Unit 1 AC10 is green before S10 is built [medium] (id 11)

- **Where:** spec 1 §2 S10, §6 AC10.
- **What:** AC10 runs check 3 "with a convention part tracked", but the unit tracks none: `propose` writes nothing under the map and `accept` needs the owner's proof.
- **Consequence:** Check 3 prints no `conventions` line with or without S10, so the change is unobserved.
- **Fix (judged sound):** Make AC10 a staged probe: a scratch clone tracking `memory/map/conventions/x.reuse.toml`, red before S10 and silent after, or a `reuse_entries.py --fixture` case running the hygiene arm.
- **Left-shift gate:** a rule that every AC names its red-before state, checked by the spec audit.

### R21 — Unit 3 AC1 reds on its own `[[retired]]` row [medium] (ids 12, 26)

- **Where:** spec 3 §4 "What keeps the name", §6 AC1, with S7.
- **What:** S7 adds a `[[retired]]` row to `tools/govkit/registry.toml` (id `codebase-map/reuse-lookup`, surfaces naming `reuse_lookup.py` and `reuse-lookup.agent.md`). AC1 allows hits only in files listed under "What keeps the name", which omits registry.toml.
- **Consequence:** A correct build fails AC1 on the unit's own row.
- **Fix (judged sound):** Add "S7's `[[retired]]` row in tools/govkit/registry.toml" to the list, and check whether `memory/map/generated/symbols.json` picks up `retire_reuse_lookup`.
- **Left-shift gate:** a spec-audit arm that evaluates each AC's grep against the spec's own Files touched writes.

### R22 — gap-mem-22 is owned but observed by no criterion [medium] (id 13)

- **Where:** spec 3 §3 Non-goals, against README "The problem this build exists to solve".
- **What:** gap-mem-22 (recall's 477 MB cache) is one of the 23 owned gaps and the brief assigns it to unit 3. Unit 3 makes it a non-goal handed to TOOL-dTotalRecall-21, and no spec's criterion observes it.
- **Consequence:** The build can close with gap-mem-22 open while its goal bound says every owned gap is closed.
- **Fix (judged sound):** Add a unit 3 criterion measuring the cache after TOOL-dTotalRecall-21 lands, or record a deviation moving gap-mem-22 to dTotalRecall and update the owned-gap list.
- **Left-shift gate:** a coverage check that every owned gap id appears in at least one AC or one deviation record.

### R23 — Unit 12's AC1 and AC2 conflict over the planted fixture word [medium] (id 14)

- **Where:** spec 12 §6 AC1 against AC2 and §7 New arm.
- **What:** AC1 requires every `gov:` word the census prints from tracked files to have a row. If the selftest in tracked `annotations.py` spells `gov:planted-word` literally, AC1 forces a row, and AC2's scratch clone then inherits it so the plant passes.
- **Consequence:** A natural build makes AC1 and AC2 mutually exclusive, and the likely escape is exempting fixture words, which hides real unregistered words.
- **Fix (judged sound):** State in S3 or S5 that fixture words are composed at runtime (`"gov:" + "planted-word"`) so no tracked file spells them, and say so in AC1. Alternatively register fixture words with `kind = "fixture"` and plant a different word in AC2.
- **Left-shift gate:** a bug-class checklist entry: "a census over tracked files must not see its own selftest plants".

### R24 — Unit 7 has no `hybrid loses` route for its `span` arm [medium] (id 15)

- **Where:** spec 7 §6 AC1 and AC2, with spec 17 S6 and §8 F3.
- **What:** Unit 17 builds no `gov:end` half on `hybrid loses`, and that half is the `span` arm. Unit 7's AC1 and AC2 require a `span` summary and finding among six arms.
- **Consequence:** On that path AC1 and AC2 cannot pass, and the leg's arm contract is undefined.
- **Fix (judged sound):** Unit 7 states the route (five arms, or `span: not built — hybrid loses`), and unit 17 S6 names what remains of `check_note_spans`.
- **Left-shift gate:** the verdict-route gate from R6.

### R25 — Unit 6 AC7 compares two populations that differ by design [medium] (id 16)

- **Where:** spec 6 §6 AC7.
- **What:** AC7 equates the view's count (records declaring `kind: research-return`) with `research_returns.py --population HEAD` (a file-name predicate). Unit 13 makes them differ: post-cutoff research-named design records declare another kind, and unit 6's own example row is a reuse-scout record without `research` in its name.
- **Consequence:** AC7 fails on a correct build once one such record exists, and it measures agreement between two populations rather than the view against its source.
- **Fix (judged sound):** Compare the view's count to `len(read_research_returns(...))` or `git grep -l '^kind: research-return$'` over the record folders, and keep the 72 floor separately.
- **Left-shift gate:** a rule that an AC's comparison names one source predicate, checked in the spec audit.

### R26 — Stale copy-mode charter copies are captured with their region markers [medium] (ids 21, 60)

- **Where:** spec 23 §2 S1, §4 Evidence (`build_region`) and "The legacy pair", §5 security.
- **What:** S1 captures any harness file that is not wiring ("a pointer, a symlink or a copy of the charter") verbatim into the charter's tail. The installer's copy mode is a plain `cp` for every alias but claude, and a stale copy fails `cmp`, so it is captured with its `<!-- gov:playbook -->` pair. No body holding marker lines is refused or neutralised.
- **Consequence:** The charter then holds two `gov:playbook` regions. `build_region` and spec 18's `find_pair` refuse every later render and `--check-render`. A body holding `<!-- /gov:legacy … -->` would end its own pair early. Both findings were graded high by the finder and medium by the skeptic (narrow path, loud refusal), and the binding grade is medium.
- **Fix (judged sound):** Treat a file carrying the gov:playbook markers, or matching the charter at any revision, as stale wiring and re-wire it, or capture only the bytes outside its region. Refuse, naming the file and line, any captured body holding a line `is_marker_line` reads as a registered region marker, or escape it. Add a plant `stale-copy` (a CLAUDE.md or copilot alias that is an older charter copy) where the render gate stays green.
- **Left-shift gate:** the `stale-copy` plant becomes a standing case of the `adopt instructions selftest` leg.

### R27 — Unit 5's holds-now view links to builds that have no README [medium] (id 23)

- **Where:** spec 5 §4 Evidence third bullet, §2 S3 (the `<build>` cell).
- **What:** The spec asserts every build a log id names has a README. aTaperedSluice, aWarmedTether, aWidenedGuide (only BACKLOG.md) and bQuiltedLantern do not.
- **Consequence:** The first `--write` commits dead relative links under `memory/views/`, which check 2 does not exempt, and the `memory hygiene` leg reds.
- **Fix (judged sound):** Render the cell as a link only when the README is tracked, otherwise the bare slug. Alternatively AC6 asserts `check-memory-hygiene.sh --only 2` is clean over the view, with a fixture row whose slug has no README.
- **Left-shift gate:** the pinned-query re-run gate from R7, applied to every "exists for each" evidence claim.

### R28 — Unit 24 pins "7 class records" with no predicate [medium] (id 25)

- **Where:** spec 24 §1 Goal, §2 S8, §8 F4, AC10.
- **What:** The spec pins `7 class records whose prose names a manifest leg` with no predicate or list. Readings of the tree give 16, 12 or 10, never 7.
- **Consequence:** The backfill scope and AC10's pass condition cannot be reproduced, so classes can be left un-planted or over-planted undetected.
- **Fix (judged sound):** Name the predicate (for example a backticked leg name in a `gated by|in|at` sentence), list the class stems in §4, and pin the count it prints or mark the figure DERIVED with the command.
- **Left-shift gate:** a rule that every PINNED figure carries the command that prints it.

### R29 — Unit 25 misdescribes how check 27 grades re-keyed rows [medium] (id 28)

- **Where:** spec 25 §4 "The decision log after S3 and S4", the check-27 paragraph.
- **What:** The spec says check 27 finds each re-keyed row's old row at the base as its top hit. Check 27 ranks HEAD records whose ident exists at the base (row_grammar.py:1240-1286), and a re-keyed row's text exists only under its new, ineligible id.
- **Consequence:** If an eligible row of another slug ranks first and passes the Jaccard floor, check 27 reports an unsatisfied near match on the S3/S4 commit, a red the spec says cannot happen.
- **Fix (judged sound):** Restate the reasoning against the code, then add a pass probe running check 27 over the staged S3/S4 commit and recording that each of the five rows' top hits is own-slug. Otherwise add a relation token naming the old id in each note.
- **Left-shift gate:** a rule that a spec's claim about an existing check cites its code lines.

### R30 — Unit 4 mints a second defined-id predicate [medium] (id 31)

- **Where:** spec 4 §2 S7 (`derive_defined_ids`), §8 F2, §10.
- **What:** S7 moves drift's definitions half into a new `derive_defined_ids` (anchors under the memory root plus spec H1s). The corpus already has one owner, `corpus_ids.walk()['defs']` (spec H1s, backlog rows, decision rows), which `gotchas.load_defined_ids` reuses. KICK-aReplayedCard-2 and TOOL-aFoldedQuarry-5 settled "one id grammar", and F2 never weighs them.
- **Consequence:** The gating resolve arm marks citations red differently from `--card --append` and gotchas check 18. The finder graded high and the skeptic medium, since the effect is limited to which citations are red. The binding grade is medium.
- **Fix (judged sound):** Have `check_resolve` take its set from `corpus_ids` as `gotchas.load_defined_ids` (gotchas.py:160) does, and do not mint `derive_defined_ids`. Rewrite F2 to cite both decisions. Extend corpus_ids' walk if drift's anchors are needed. Honour the `missing:` citation form (`tree_lib.scan_missing_citations`).
- **Left-shift gate:** a reuse-scout check that greps for an existing owner before a spec mints a `derive_*` predicate.

### R31 — Two producers of the `Decided:`→`decides` edge, and an unowned re-point [medium] (id 32)

- **Where:** spec 22 §2 S5 (trailer rows), §10, and spec 17 §3.
- **What:** S5 derives `Decided:` trailers as decision rows, a second derivation of the edge PLAY-dOrderedCharter-28 S5's commit adapter already types (`read_trailer_edges`). Spec 17 §3 says spec 22 re-points that adapter at `commit_trailers.decided`, and no spec does.
- **Consequence:** Two producers can disagree on keys and targets, and the adapter can keep its own parse, the "third parse" I6 forbids.
- **Fix (judged sound):** Choose one producer: the trailer half reads `read_trailer_edges`, or the adapter calls `derive_decision_rows`. File an ask to dOrderedCharter for the adapter to read through `commit_trailers.decided`, and correct spec 17 §3's attribution.
- **Left-shift gate:** an edge-pair check in the spec brief that every "re-pointed by X" claim matches a scope item in X.

### R32 — Unit 24 restates dWitnessedBar's leg-tests edge and seen-red record [medium] (id 33)

- **Where:** spec 24 §2 S1 and S3, §10.
- **What:** The class→leg link (`gate:`) and the observation (`planted:`, `observed:` with a new `--observe` runner) restate TOOL-dWitnessedBar-22's leg-row `tests` edge and TOOL-dWitnessedBar-7's seen-red record (`read_seen_red_records`), neither cited.
- **Consequence:** Two spellings of one fact can drift: a leg's `tests` list can omit a class whose record says `gate:` it, and the reverse.
- **Fix (judged sound):** Derive the class→leg link from the inverse of a leg's `tests = ["class.<name>"]` (TOOL-dWitnessedBar-22 S1/S4, `class` namespace from TOOL-dTotalRecall-9 S1), and record the observation as a seen-red line. If neither fits, cite both in §10 with the reason and an ask to dWitnessedBar.
- **Left-shift gate:** the reuse-scout check from R30, run over sibling and parent build specs.

### R33 — Unit 25 re-sorts and re-keys landed decision rows [medium] (id 34)

- **Where:** spec 25 §2 S3 and S4, §3, §8 F1/F2.
- **What:** S3 moves 94 landed rows and relocates the DEPL section, and S4 rewrites five landed ids, against `memory/DECISIONS.md:6` ("never re-sorted and a landed row is never edited"), which F1/F2 never weigh. The cited TOOL-cSpliceWarden-4 covers archive repair. The `-5b`/`-1c` suffix means a revision row in `row_grammar.id_pattern`.
- **Consequence:** The log's governing rule is broken silently, and duplicates are mislabelled as amendments for every later reader.
- **Fix (judged sound):** Settle F1/F2 against `DECISIONS.md:5-6`. Prefer supersession or pointer rows (I26) that leave landed bytes in place, or record a deviation with an owner grant naming the lifted rule. Do not use the revision suffix for duplicates unless the grammar's meaning is amended.
- **Left-shift gate:** a check on the decision log that refuses any diff editing or moving a landed row without a deviation record.

### R34 — The reuse lens's finding of unit 23's misplaced `legacy` row [medium] (id 35)

- **Where:** spec 23 §2 S9, §4 Files touched.
- **What:** This is the defect of R4: `marker.legacy` registered in `tools/playbook/namespaces.toml` instead of a `[[marker]]` row in `tools/memory-tree/marker-words.toml`, the seam spec 12 builds and spec 4 S14 extends.
- **Consequence:** No `legacy` row lands, so `gov:legacy` in `adopt_instructions.py` is refused on every bar, and a members field enters a namespace row spec 12 kept free of it.
- **Fix (judged sound):** One `[[marker]]` row in `marker-words.toml` (`word = "legacy"`, `kind = "pair"`, `reader = "tools/playbook/render_playbook.py"`, `owner = "TOOL-dLinkedLibrary-23"`). Drop `namespaces.toml` from the write set.
- **Note:** this finding's binding grade is medium and R4's is high, so they are not merged. The reviewer's reading is that R4's high grade governs the defect, since the leg reds on every bar.
- **Left-shift gate:** as R4.

### R35 — New legs are hand-written into `gate-legs.json`, bypassing the leg factory [medium] (id 37)

- **Where:** spec 7 §2 S1 and S5, §10 (also spec 9 S4, spec 10 Files touched, spec 23 Files touched).
- **What:** Specs 7, 9, 10 and 23 add legs as rows written into `tools/gate-legs.json`. TOOL-dWitnessedBar-11, which lands first, renders that file from declarations and refuses a row no declaration produces.
- **Consequence:** Each hand row is STALE or refused at `leg_factory.py --check` and regen stage 1, and hand descriptors can omit required keys (`tag`, `purpose`, `enforces`).
- **Fix (judged sound):** In each spec add legs with `python tools/run-gates/leg_factory.py new` (TOOL-dWitnessedBar-11 S3) into the owning kit's descriptor, list `gate-legs.json` as its render, and cite TOOL-dWitnessedBar-11 as a precondition and in §10.
- **Left-shift gate:** a spec-tokens arm that refuses `tools/gate-legs.json` as a hand-edited file in Files touched once the factory exists.

### R36 — Unit 15's header reader is a third comment scanner [medium] (id 39)

- **Where:** spec 15 §2 S1 (`derive_source_purpose`), §10.
- **What:** The header reader scans "the contiguous `#` or `//` comment block" itself. Spec 4 S4's `extract_comment_spans(src, ext)` exists for this, excludes strings, and specs 11 and 17 reuse it.
- **Consequence:** A `#` line inside a string or heredoc is read as a purpose, and block boundaries differ from the annotation arms', so `gov_code.py show` and those arms disagree.
- **Fix (judged sound):** Derive the header from `extract_comment_spans`, taking the span ending at `line - 1`. Add a consumes-from edge on unit 4 for it and cite it in §10.
- **Left-shift gate:** the reuse-scout check from R30.

### R37 — Deleting five files trips the unguarded dead-path leg [medium] (id 43)

- **Where:** spec 3 §4 "What keeps the name" and Files touched, §7.
- **What:** Deleting reuse_lookup.py, reuse-lookup.agent.md, rank_harness.py, replay-phrases.py and scen-adversarial.json makes their basenames needles for `dead-path carriers (deleted files still named)`. Files the spec deliberately keeps still spell them (the receipt fixture `adopter-ic-2cff5855.receipt.json:64-69`, the check-hygiene test, the step program, the `[[retired]]` surfaces, the help page). The spec names neither the leg nor `tools/dead-path-waivers.txt`.
- **Consequence:** The first bar after the pass reds on files AC1 never inspects, since AC1 greps only `reuse_lookup|reuse-lookup`. The finder graded high and the skeptic medium because the bar reds before merge. The binding grade is medium.
- **Fix (judged sound):** Add the leg to §7. In §4 give each kept carrier a waiver row or rewrite it. Add WIRE-INTO-PROJECT.md:527-535, registry.toml:672, kit.toml's two `[[files]]` rows, selftest.py's arms and the dossier's replay-phrases lines to S1's readers. Widen AC1 to all five basenames. Probe: `bash tools/check-dead-paths.sh --list` after the deletion.
- **Left-shift gate:** a spec-tokens arm that, for every file a spec deletes, runs `check-dead-paths.sh --list` and requires §7 to name the leg.

### R38 — Unit 3's deletion omits the readers of the three other deleted files [medium] (ids 44, 74)

- **Where:** spec 3 §2 S1 Readers, §4 Files touched, §7.
- **What:** S1 lists only readers of `reuse_lookup`/`reuse-lookup`. `memory/project/encoding-posture-sites.txt:20-21` holds set-equality rows for rank_harness.py and replay-phrases.py ("a row the scan no longer finds fails"). `tools/codebase-map/kit.toml:48, :57` include the deleted files, and `tools/codebase-map/selftest.py:1905, :2129, :2535, :2577` load them by path. The spec never names the registry or the `encoding posture (text IO names its encoding)` leg.
- **Consequence:** The unguarded encoding-posture leg reds on every bar, and the kit descriptor and selftest are left stale or red.
- **Fix (judged sound):** List these readers in S1 by name and add them to Files touched. Drain the two encoding-posture rows in the deletion commit, remove the two kit.toml rows, and delete or re-point the selftest arms and runbook lines. Add the encoding-posture leg to §7. Extend AC1 to `reuse_lookup|reuse-lookup|rank_harness|replay-phrases|scen-adversarial`.
- **Left-shift gate:** the deletion probe from R37, extended to every registry keyed by path.

### R39 — Unit 9's two new legs owe meta-gate rows nobody writes [medium] (id 45)

- **Where:** spec 9 §2 S4, §4 Files touched, §7.
- **What:** `record origin (stored origin against history)` and `record origin selftest` have no chunk, subject or ceiling. Files touched names only `tools/gate-legs.json`.
- **Consequence:** Separate reds at govkit selfcheck (unclaimed leg), codebase-map coverage, run-selftests (held leg without budget) and foreign-prefix parity, none on §7. This is the class `memory/gotchas/a-new-leg-trips-a-growing-set-of-meta-gates.md` records.
- **Fix (judged sound):** Give each leg its chunk, subject and ceiling. List tools/memory-tree/kit.toml (`[[gate_leg]]`), tools/govkit/subject-pins.tsv, tools/run-gates/selftest-budgets.txt, tools/run-gates/ceiling-evidence.txt, foreign-prefix.gov.test.sh (WHOLE_RUN) or a FOREIGN_PREFIX_PROBE stop, the claiming dossier and memory/map/generated/*. Add `govkit selfcheck`, `codebase-map coverage + freshness`, `foreign-prefix parity (every self-test at three prefixes)` and `every held leg is budgeted, every budget row resolves` to §7.
- **Left-shift gate:** a spec-tokens arm that, for any leg a spec adds, requires each meta-row file to appear in Files touched.

### R40 — Unit 10's `retrofit progress selftest` leg is undefined [medium] (id 46)

- **Where:** spec 10 §4 Files touched, §7.
- **What:** The leg has no argv, chunk, subject, guard or ceiling, and only `gate-legs.json` is touched.
- **Consequence:** The leg lands unclaimed and reds govkit selfcheck, the budget check, foreign-prefix parity and codebase-map coverage, none on §7.
- **Fix (judged sound):** Add a scope item defining the row fully. List the kit.toml `[[gate_leg]]`, subject-pins.tsv, selftest-budgets.txt, the foreign-prefix entry or probe stop, the claiming dossier and the regenerated map artifacts, and add the meta legs to §7.
- **Left-shift gate:** as R39.

### R41 — Unit 23's `adopt instructions selftest` leg is undefined [medium] (id 47)

- **Where:** spec 23 §4 Files touched, §7.
- **What:** No scope item defines the row, and Files touched has no `[[gate_leg]]` in tools/playbook/kit.toml, no subject pin, budget, foreign-prefix entry or dossier claim.
- **Consequence:** The same meta-gate reds as any unclaimed leg, none on §7.
- **Fix (judged sound):** Add a scope item defining the row, add tools/playbook/kit.toml, subject-pins.tsv, selftest-budgets.txt, the foreign-prefix entry or probe stop, the playbook dossier claim and memory/map/generated/* to Files touched, and add the legs to §7.
- **Left-shift gate:** as R39.

### R42 — Unit 7's two selftest legs miss foreign-prefix and map artifacts [medium] (id 48)

- **Where:** spec 7 §2 S1 and S5, §4 Files touched.
- **What:** `annotations selftest` and `annotations-read self-test` have kit, pin, budget and dossier rows, but no foreign-prefix declaration and no regenerated map artifacts.
- **Consequence:** foreign-prefix.gov.test.sh reds an undeclared row printing no probe marker, and `codebase-map coverage + freshness` reds on stale MAP.md and inventories.json. Neither leg is on §7.
- **Fix (judged sound):** Add a WHOLE_RUN row per leg or a FOREIGN_PREFIX_PROBE stop in both suites, add memory/map/generated/* to Files touched, and add both meta legs to §7.
- **Left-shift gate:** as R39.

### R43 — Unit 6's `LIBRARY_VIEWS` is a new key in a shrink-only legacy home [medium] (id 52)

- **Where:** spec 6 §2 S2, §4 Files touched, §7 (and spec 5, which sets it).
- **What:** `LIBRARY_VIEWS` goes into `.memory-tree.conf`. policy.py makes each key there a legacy-home row and refuses growth. Neither spec 6 nor spec 5 lists `policy check` in §7, and spec 3 F1 rejects a conf key on this ground.
- **Consequence:** The unguarded `policy check` leg reds with "is a new legacy home and the list is shrink-only", and the switch's home must move, changing S2, AC4's plant and spec 5's Files touched.
- **Fix (judged sound):** Re-home it as a catalogue key (for example `memory.library-views`) in tools/policy/catalogue.toml read through `resolve`, update spec 5 to match, and add `policy check` to §7 of both specs.
- **Left-shift gate:** a spec-tokens arm that refuses a new `.*.conf` key in Files touched unless it ends `_CUTOFF` or `_PIN`.

### R44 — Unit 22's `GOTCHA_FIELDS` is a new key in a shrink-only legacy home [medium] (id 53)

- **Where:** spec 22 §2 S2, §4 Files touched, §7.
- **What:** S2 adds `GOTCHA_FIELDS` to `.memory-tree.conf`, which `policy check` refuses, and §7 omits that leg.
- **Consequence:** The bar reds on `policy check`, and S2, AC3's fixture and HYGIENE's prose in S7 must change.
- **Fix (judged sound):** Carry it as a catalogue key (for example `gotchas.fields`) read through `resolve`, add tools/policy/catalogue.toml, unsummarised-keys.txt and .governance/policy.json to Files touched, and add `policy check` to §7.
- **Left-shift gate:** as R43.

### R45 — Unit 19 S4 misses three live instructions to write `## Shared seams` prose [medium] (id 55)

- **Where:** spec 19 §2 S4 Readers.
- **What:** `tools/codebase-map/gen_map.py:121` (rendered at `memory/map/README.md:30`) and `tools/codebase-map/INVENTORY-DERIVATION.md:67, :105` still tell authors to document shared seams in dossier prose, which the new `test_dossier_holds_no_prose` refuses.
- **Consequence:** An agent following the map README's Rules writes a section the coverage gate reds.
- **Fix (judged sound):** Add those lines to S4's by-value readers, rewritten to point at the moved prose record or the reuse entries, and add INVENTORY-DERIVATION.md to Files touched.
- **Left-shift gate:** a rule that a spec retiring a shape greps for every instruction naming it and lists each hit as a reader.

### R46 — Unit 5's §7 omits `policy fixtures` [medium] (id 56)

- **Where:** spec 5 §7 leg line.
- **What:** Files touched names `tools/memory-tree/check-memory-hygiene.sh`, which trips the non-broad guard of `policy fixtures`, and §7 omits that leg.
- **Consequence:** Under SPEC_GUARD_LEGS_CUTOFF=2026-09-22, the `spec tokens` leg reports `policy fixtures <- tools/memory-tree/check-memory-hygiene.sh` against this spec and reds.
- **Fix (judged sound):** Add `policy fixtures` to spec 5's §7 leg line.
- **Left-shift gate:** already gated by `spec tokens (a spec's own names resolve)`. The writer should run `check-spec-tokens.py` before committing a spec.

### R47 — Unit 23 captures ignored, untracked or out-of-repo harness files [medium] (id 62)

- **Where:** spec 23 §2 S1, §5 security.
- **What:** S1 captures every harness file that exists, without asking whether it is tracked, gitignored or a symlink outside the repository. Unit 8's door refuses `--imported-from` for an untracked path.
- **Consequence:** A gitignored `.cursorrules` or an out-of-repo symlink target is published into the tracked charter, unpriced by §5. Its paragraphs cannot be ruled, which under `refuse` blocks landing. A dangling symlink is neither captured nor wiring, and S2 refuses it forever.
- **Fix (judged sound):** Bound S1 to tracked regular files, or symlinks resolving inside the repository. Refuse and name an ignored or untracked file, never capture it silently. Name the dangling-symlink case and S2's handling. Add plants for an ignored `.cursorrules` and a CLAUDE.md symlinked outside.
- **Left-shift gate:** a bug-class checklist entry: "a capture of adopter files states tracked, ignored and symlink cases".

### R48 — Identical paragraphs share a key, so a repeat can never be ruled [medium] (id 61)

- **Where:** spec 23 §4 "Paragraphs", §2 S3, S6 and S7.
- **What:** Identical paragraphs share one key and "share one ruling", but a ruling removes one paragraph and decrements the count by one, and a second ruling for that key exits 2.
- **Consequence:** A repeated `---` or heading stays in the pair forever, the count never reaches zero, and under `instructions.legacy = refuse` the install can never land. The finder graded high and the skeptic medium. The binding grade is medium.
- **Fix (judged sound):** Make the key unique per occurrence (an ordinal on a repeat), or let one ruling remove every paragraph sharing its key and decrement by their number. Add a plant with two identical `---` paragraphs under `refuse` that drains to zero.
- **Left-shift gate:** a bug-class checklist entry: "a content-hash key needs a stated duplicate rule and a duplicate plant".

### R49 — Unit 4's citation cut has no grammar [medium] (id 68)

- **Where:** spec 4 §2 S7 (`every-comment-ref`).
- **What:** Every `memory/` path a comment cites must be tracked, but no rule says how a path is cut from prose. The tree's comments cite globs, `<placeholder>` paths, directories, `:line` suffixes and trailing punctuation (41, 8, 5 and more lines respectively).
- **Consequence:** False dangling citations are seeded into unit 11's legacy, and every new comment in these ordinary shapes is an `undeclared site` red. The finder graded high and the skeptic medium. The binding grade is medium.
- **Fix (judged sound):** Define the grammar in S7: strip trailing punctuation and `:<line>[,<line>]`; skip tokens holding `*`, `<` or `{`; resolve a directory as tracked when `git ls-files <dir>/` lists anything. Add a plant per shape expecting no finding.
- **Left-shift gate:** a rule that a check over free text ships a plant per shape found by a census of the live tree.

### R50 — Units 11 and 4 do not say what happens with no compare base [medium] (id 69)

- **Where:** spec 11 §2 S1, and spec 4 S6 `required`.
- **What:** Both read touched blocks since `resolve_compare_base(root)`, which returns `(None, why)` with no remote or no fetched ref. Neither spec states that case.
- **Consequence:** A builder either grades every block (the whole tree reds) or none (an unarmed check reads green, against `[gate]`), on a leg that runs every bar.
- **Fix (judged sound):** Print `annotations: budget: unarmed — <why>` and exit 0, never as a green count, and do the same for `required`. Add a plant with a fixture repository with no remote.
- **Left-shift gate:** a bug-class checklist entry: "every call to `resolve_compare_base` states its `None` route".

### R51 — Unit 11's ordinal block key shifts on banner insertions [medium] (id 70)

- **Where:** spec 11 §2 S2 (`derive_block_anchor`).
- **What:** A block is keyed by the hash of its first line plus an ordinal among earlier blocks with the same opener. Banners such as `# ----` (547 lines under tools/) open many blocks.
- **Consequence:** Adding one banner block renumbers every later long-block row in the file, which reads as `unmeasured row` plus `undeclared site`, contradicting S2's "a block that moves keeps its key". AC2 inserts only plain lines.
- **Fix (judged sound):** Key a repeated opener by its first non-banner line or first N lines, or let `carry_renames`-style re-keying absorb ordinal shifts. Extend AC2 with a plant inserting a second `# ----` block above.
- **Left-shift gate:** the duplicate-key checklist entry from R48.

### R52 — `grep_words` has no empty-word guard [medium] (id 71)

- **Where:** spec 14 §2 S5 and S7 (`grep_words`).
- **What:** The lifted primitive drops the donor's `if ids:` guard. With empty stdin, git takes the first pathspec as the pattern, and a blank line matches every line.
- **Consequence:** `where ""` or any empty-set caller returns hits with exit 0, a wrong answer instead of `none` or a refusal.
- **Fix (judged sound):** Return `({}, None)` without calling git when the stripped word list is empty, and have `where` refuse an empty or whitespace word with exit 2. Add a plant `where ""` expecting exit 2.
- **Left-shift gate:** a reuse rule that a lifted primitive carries its donor's guards, checked by diffing the cited donor lines.

### R53 — `show <bare name>` answers `none` for unextracted languages [medium] (id 72)

- **Where:** spec 14 §2 S6, §4 "Targets".
- **What:** The not-extracted floor fires only when the target's file is known. A bare name defined only in an unextracted language resolves to no key, so `show Run` exits 1 with `none`.
- **Consequence:** An agent asking for a Go, Java or Rust symbol by name is told it does not exist, the false `none` the floor exists to prevent. AC5 tests only `x.go::Run`.
- **Fix (judged sound):** When a bare name resolves to nothing and `code_meta.languages` lists a language with extractor `none`, or the record is `degraded`, print the floor's line and `where`'s hits. Add `show Run` to AC5's plant.
- **Left-shift gate:** a rule that each degraded-mode floor has a plant for every target form the CLI accepts.

### R54 — Unit 7's read hook does not bound directory and root reads [medium] (id 73)

- **Where:** spec 7 §2 S3 (the read hook's paths).
- **What:** A directory argument's tracked files go into one launcher call as `--path` flags, with no file bound. A Grep with no `path` (the root) is not covered, and the spec does not say whether paths cut by the 2,048-byte cap are recorded as pushed.
- **Consequence:** A root Grep expands to about 8,400 paths (about 727 KB of argv), past Windows' 32 KB limit, so the spawn fails and nothing is pushed on the most common read. Capped rows may be marked pushed and never shown.
- **Fix (judged sound):** Cap files taken from a directory (nearest first), pass paths on stdin or in a file, treat a pathless Grep as its cwd, and append only emitted paths to the pushed list. Add an AC4 case with a pathless Grep on the fixture root.
- **Left-shift gate:** a bug-class checklist entry: "a spawn whose argv grows with the tree states a bound or uses stdin".

### R55 — Unit 10's `drained` counts renames as drains [medium] (id 75)

- **Where:** spec 10 §4 "The derivation", the `drained` row.
- **What:** A key gone since period start counts as wholly drained, but unit 11's `carry_renames` moves a renamed file's rows to new keys.
- **Consequence:** The card over-reports progress on any rename, the case unit 11's AC5 reds in the check.
- **Fix (judged sound):** Derive `drained` per key after applying `carry_renames` between the period-start blob and now, or as the sum of `max(0, start − now)`. Add a plant renaming a file with three rows expecting `drained 0`.
- **Left-shift gate:** a rule that every derivation keyed by path states its rename route.

### R56 — Unit 15's two new `memory/project` files have no merge driver [medium] (id 76)

- **Where:** spec 15 §2 S3, S6 and S7, §4 Files touched.
- **What:** `memory/project/code-purposes.tsv` (written by agent passes) and `code-purpose-pending.txt` (re-rendered at every landing) get no `.gitattributes` driver, while sibling unit 11 gives its homes `merge=rows`.
- **Consequence:** Concurrent landings across machines produce text conflicts on both files.
- **Fix (finder's fix judged UNSOUND, skeptic's correction):** Give `memory/project/code-purpose-pending.txt` `merge=ours`, since its `[[generated]]` row re-renders it at landing. For `memory/project/code-purposes.tsv`, either extend merge-rows.py with a class keying a row by its first TAB field and refusing two rows for one key (with merge-rows.test.sh cases), then add `merge=rows`, or state that a conflict is resolved by re-running S4's write. Add an AC grepping both lines in `.gitattributes`. The skeptic notes merge-rows.py keys by record id or backlog class today, so `merge=rows` alone does not fit the .tsv.
- **Left-shift gate:** a check that every tracked file a spec adds under `memory/project/` has a `.gitattributes` merge line.

### R57 — `splice_region` writes a body that holds its own marker [medium] (id 78)

- **Where:** spec 18 §2 S2 (`splice_region`), §5 security.
- **What:** The function refuses a malformed pair in the text, but not a `body` holding a line `is_marker_line` reads as the open or close marker.
- **Consequence:** One write leaves a file `find_pair` refuses on every later read. Unit 23 writes adopter bytes through it, and S5's security bullet claims the factory prevents this.
- **Fix (judged sound):** Raise `RegionError` naming the body line when any body line is a marker line for the call's marks, labelled or not, and add the case to AC3.
- **Left-shift gate:** the case added to AC3 becomes a standing factory selftest plant.

### R58 — Unit 21's ctags temp names lose parser-selecting file names [medium] (id 79)

- **Where:** spec 21 §2 S2 and S5.
- **What:** Each blob is written as `<blob><.ext>`, but ctags selects parsers by whole name or shebang (`Makefile`, `Dockerfile`, `CMakeLists.txt`, extensionless scripts).
- **Consequence:** Under `builtin+ctags` or `ctags`, those files silently stay at file level and are never listed with extractor `none`, so unit 14's floor never fires: the silent degrade the clause forbids.
- **Fix (judged sound):** Name the temp file `<blob>/<original basename>`, or pass `--language-force` per file. List any file ctags emitted no language for under extractor `none`. Add a `Makefile` with one rule to the S7 fixture.
- **Left-shift gate:** a fixture rule that a language-detection step carries an extensionless plant.

### R59 — Unit 25 turns an adopter-authored README into an overwritten artifact [medium] (id 80)

- **Where:** spec 25 §2 S1, §4 "The README as an artifact".
- **What:** `memory/map/README.md`, until now written once by `--scaffold`, becomes a `--write` render, and the spec does not address an adopter that edited it.
- **Consequence:** After the kit update, an edited README reads `STALE:` and the named remedy `--write` overwrites the authored text with no warning. Git can recover it, which keeps the effect contained.
- **Fix (judged sound):** Adopt the README as an artifact only where it equals a past render of the literal; otherwise print `README.md is authored — not rendered` and leave it. Or keep an authored tail below a generated region via unit 18's factory. Add a plant with an edited README that `--write` keeps.
- **Left-shift gate:** a bug-class checklist entry: "a file moving from scaffold-once to rendered states the adopter-edited case".

## Low

### R60 — Unit 25 S6 and AC8 observe nothing [low] (ids 10, 27)

- **Where:** spec 25 §2 S6, §6 AC8.
- **What:** At HEAD no README carrying `status:` belongs to a build with a parsed spec, and this build's README lost its key in 5a9183011 (18 carry it, not 19). AC8's loop already prints nothing, and S6's "this build's own README first" is already done.
- **Consequence:** The criterion cannot fail, so S6 is certified without change. Id 10 was graded medium by its finder and low by the skeptic. The binding grade is low.
- **Fix (judged sound):** Restate S6 at HEAD, then drop S6 as moot, or replace AC8 with a planted red: a scratch build with a parsed spec and a `status:` key, failing if `gen_build_index.py --check` does not print "Delete the 'status:' key". Mark the tree-level half `figure: DERIVED, 0 at base`.
- **Left-shift gate:** the red-before rule from R20.

### R61 — Unit 24 joins a `GOTCHA_FIELDS` admitted set nobody defines [low] (id 17)

- **Where:** spec 24 §2 S1, with spec 22 S2.
- **What:** Unit 24 adds `gate:`, `planted:` and `shape:` to `GOTCHA_FIELDS`' "admitted set", but unit 22 defines `GOTCHA_FIELDS` only as the required set.
- **Consequence:** The builder must invent where the admitted set lives, a second spelling of the field registry.
- **Fix (judged sound):** Unit 22 names the admitted set (for example `GOTCHA_KEYS` in `gotchas.py`, with `GOTCHA_FIELDS` its required subset), and unit 24 cites it.
- **Left-shift gate:** a spec-tokens arm resolving every interface name a spec cites to a definition in some spec.

### R62 — Unit 25's `kind: note` remedy points at prose unit 24 retires [low] (id 18)

- **Where:** spec 25 §2 S8, with spec 24 S4.
- **What:** The refusal's remedy names `kind: class` and `No machine gate`. Unit 24 (order 5) retires the `No machine gate` prose arm.
- **Consequence:** The message goes stale one unit later and misleads the next adopter.
- **Fix (judged sound):** Name `kind: class` alone, or have unit 24 S4's Readers list the remedy string in `gotchas.py` and rewrite it.
- **Left-shift gate:** the build-order Readers replay from R18.

### R63 — The `decides=` segment lead is spelled two ways [low] (id 19)

- **Where:** spec 1 §4 "The move", with spec 22 S6 and AC8.
- **What:** Unit 1's pointer row ends `… <routing record>. decides=record-kind.decision`, while unit 22 AC8 shows `· decides=feature.roles`. Unit 22, the owner, never states the delimiter.
- **Consequence:** A parser anchored on `· decides=` misses unit 1's row.
- **Fix (judged sound):** Unit 22 S6 states the lead (for example `· decides=<target>[,<target>]` at the row's end), and unit 1's example uses it.
- **Left-shift gate:** the shared-interface pin from R5.

### R64 — Unit 2's false import premise and overstated byte figure [low] (ids 29, 41)

- **Where:** spec 2 §10 Reuse audit and §4 "The index" Gate legs row; §4 Evidence (role body bytes).
- **What:** §10 says `gotchas.load_leg_names` and `gotchas.records` are functions "a codebase-map module may not import", but `tools/codebase-map/kit.toml:7` declares `requires = ["memory-tree"]` and spec 4 relies on that direction. So the house index re-reads `LEG_MANIFEST` itself. Separately, §4 says the scout role's body is 1057 bytes, which is the whole file. check_roles measures about 647 bytes.
- **Consequence:** A second manifest reader that skips `load_leg_names`' blank-key and malformed-manifest handling, so the two can list different legs. The byte figure overstates the role against its 1536 ceiling.
- **Fix (judged sound):** Correct §10, and call `gotchas.load_leg_names` (and the gotchas CLI for class stems) through `resolve_kit_dir("memory-tree", ...)`. Restate the body size as check_roles measures it.
- **Left-shift gate:** a spec-tokens arm that checks a stated import ban against the kit's `requires`.

### R65 — Unit 23 re-spells the shared pin normaliser [low] (id 36)

- **Where:** spec 23 §4 "Paragraphs".
- **What:** The paragraph key's "first eight hex of the SHA-256 … whitespace runs folded" is `derive_pin_hash` (PLAY-dOrderedCharter-24 S7), which spec 11 calls. Spec 23 never names it, and its text omits the end-strip.
- **Consequence:** Two normalisers that can drift, after which landed ruling keys stop matching recomputed ones. The finder graded medium and the skeptic low. The binding grade is low.
- **Fix (judged sound):** Spell the key as `<src>#p` + `derive_pin_hash(text)` (`tools/memory-tree/design_lib.py`) and cite it in §10 and the consumes-from edges.
- **Left-shift gate:** the reuse-scout check from R30.

### R66 — Unit 8 duplicates unit 1's labels parsing and settling [low] (id 38)

- **Where:** spec 8 §2 S6, §4 "The decisions" and Inventory (`route_candidates`).
- **What:** `adopt decisions --rate` reads the two labels files and settles candidates itself, reusing only `derive_kappa` from unit 1's `decision_rubric.py`.
- **Consequence:** Duplicated labels parsing and settling, where a fix lands in one router only. The skeptic notes the split and lifecycle differences are the clause's own, and graded low against the finder's medium. The binding grade is low.
- **Fix (judged sound):** Extend `decision_rubric.py` with a candidate mode, or factor `agree`/`route`'s labels reader and settler into exported functions (add them to I2). Have `--rate` call them with its `split`-never-major and lifecycle rules as parameters, and name them in §3 and §10.
- **Left-shift gate:** a shared-interface rule that a file form in I2 exports its reader with it.

### R67 — Specs 16 and 7 define "a shell read" by two hand lists [low] (id 42)

- **Where:** spec 16 §4 "The counts" (`read_files`).
- **What:** Spec 16 lists `cat, head, tail, sed, awk, less, wc`, spec 7 a different list, and neither extends runlog's segment classifier (`_derive_program`/`_derive_segment`, `tools/runlog/extract.py:479-566`).
- **Consequence:** The follow-through test and the code replay count reads differently, for example `git show <rev>:<path>` or `Get-Content`, and wrappers are handled in only one.
- **Fix (judged sound):** Add a `read` class with operand paths to runlog's classifier, or one shared read-path function in `extract.py`. Have both specs call it and cite it in §10.
- **Left-shift gate:** the reuse-scout check from R30.

### R68 — Unit 2's conf keys and workflow script trip policy and map gates [low] (id 54)

- **Where:** spec 2 §8 F1, §4 "The index" and Files touched.
- **What:** F1 adopts `HOUSE_INDEX_DIRS` and `HOUSE_INDEX_KINDS` in `.codebase-map.conf`, a shrink-only legacy home. The new `tools/workflows/reuse-bench.js` becomes a `workflow-scripts` inventory key no dossier claims.
- **Consequence:** The first tree declaring either key reds `policy check`, and the unclaimed script reds `codebase-map coverage + freshness`.
- **Fix (judged sound):** Re-home the two listings as catalogue keys read through `resolve`, with an ask on aScoutedSeam. Add `memory/map/features/review-harnesses.md` (its `workflow-scripts` claim) and memory/map/generated/* to Files touched.
- **Left-shift gate:** the conf-key gate from R43 and the meta-row gate from R39.

### R69 — Unit 3's protocol rewrite has no size bound [low] (id 57)

- **Where:** spec 3 §2 S5, §5 risks.
- **What:** S5 rewrites two rows of `tools/unattended/PROTOCOL.template.md`, whose render `memory/guides/UNATTENDED-PROTOCOL.md` is 66859 bytes against a 66860 budget.
- **Consequence:** Any net growth ships with only a BUDGET WARN under `budgets.enforce = warn`.
- **Fix (judged sound):** State in S5 or §5 that the rows must not grow the render net, or record the cap move with `check-template-size.sh --bump`, and add `unattended protocol size` to §7.
- **Left-shift gate:** a spec-tokens arm that flags a Files-touched render within N bytes of its budget.

### R70 — Unit 19's `apply` is not idempotent after a partial failure [low] (id 66)

- **Where:** spec 19 §2 S3 ("A second `apply` writes nothing"), §5 error states.
- **What:** `apply` makes 82 propose calls and 32 dossier rewrites, pre-checking only `parse_dossier` failures. Write order and mid-run failure are unspecified.
- **Consequence:** A re-run after a mid-run failure re-proposes seams whose dossier was not yet shrunk, giving the owner duplicates.
- **Fix (judged sound):** Write each dossier's proposals and record, then shrink it. On re-run skip a seam whose proposal exists, keyed by `<feature>-<ordinal>`. Add a plant with a stub `reuse_entries.py` failing on the third call, where a re-run writes no duplicate.
- **Left-shift gate:** a bug-class checklist entry: "an idempotency claim carries a mid-run failure plant".

### R71 — Unit 2's `matched` slot copies scout lines unbounded [low] (id 81)

- **Where:** spec 2 §2 S7 and S8, §4 "The slot", §5 security.
- **What:** The slot copies a scout record's `## Matches` lines verbatim into every work order, with no line cap, byte cap or S5 grammar check.
- **Consequence:** A large or malformed return inflates every work order and carries free agent text into other agents' instructions.
- **Fix (judged sound):** Keep only lines matching the S5 grammar, cap the block (for example 2 KiB or N lines, then `… <n> more`), and render a malformed return as `not searched — the Matches section is malformed`.
- **Left-shift gate:** a bug-class checklist entry: "agent text copied into another agent's prompt is grammar-filtered and capped".

## Refuted

- Id 51 (spec 25 S1, README freshness): refuted. The `[[generated]]` row and `regen.py --check` already enforce the README's freshness on every bar.
- Id 77 (spec 17 S4, inside-def note pairing): refuted. §4 "The span, by case" and S5 already exclude definition-derived notes from the pairing text.

review-shape kind=spec-audit round=1 intensity=full at=synth raw=81 confirmed=79 refuted=2 unverified=0 blocker=1 high=14 medium=50 low=14 agents=11 out-tokens=350264
## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes |
|---|---|---|---|---|---|---|---|---|
| 1 | coherence | memory/builds/dLinkedLibrary/spec/2026-10-26-spec-TOOL-dLinkedLibrary-19.md:section 2 S3 (with TOOL-dLinkedLibrary-1 section 2 S1-S3) | high | high | confirmed | Read unit 1:44-58. S1 defines the feature part as `memory/map/features/<feature>.reuse.toml` beside `<feature>.md`, and S2 reds a part whose tag is not `unit.reuse.<file stem>`, whose `reuse.tag` is not `feature.<stem>`, or that has no `<stem>.md` beside it. S3 spells the verb `--name <n> (--feature \| --convention)`, with `--feature` as a bare flag. Unit 19:47-50 calls `propose --feature <feature> --name <feature>-<ordinal>`, and its table at :139 names the entries `unit.reuse.<feature>-<n>`. Nothing in unit 1 allows several parts per feature. So an accepted `alpha-1.reuse.toml` has no `alpha-1.md` beside it and is red under S2. | sound | - |
| 2 | coherence | memory/builds/dLinkedLibrary/spec/2026-10-26-spec-TOOL-dLinkedLibrary-4.md:section 2 S8 and section 6 AC11 (with TOOL-dLinkedLibrary-19 S3, S6) | high | high | confirmed | Unit 4 S8 (:105-112) says every `accepted` or `proposed` entry's `anchors` string must be carried by a line in the tree. Unit 1 S3 makes a proposal with no disposition an entry in state `proposed`. Unit 19 S3 proposes with `--anchor "gov:feature <feature>"`, and the README build order puts it at step 10, before unit 4 at step 12. `git grep -n "gov:feature" -- . ':!memory'` printed nothing. Unit 19's Files touched names no code file that gains an anchor, and unit 4's Migration says no existing comment is rewritten. So AC11 (:347-350) reds on a correct build. | sound | - |
| 3 | coherence | memory/builds/dLinkedLibrary/spec/2026-10-26-spec-TOOL-dLinkedLibrary-23.md:section 2 S9, section 4 Files touched, section 6 AC8 | high | high | confirmed | Unit 23 S9 (:90-91) registers `marker.legacy` through namespace rows. Its Files touched (:187) lists `tools/playbook/namespaces.toml` and never `marker-words.toml`, and AC8 (:250-251) greps `namespaces.toml`. Unit 12 S1 (:35-40) makes `tools/memory-tree/marker-words.toml` `[[marker]]` rows the member registry that `check_marker_words` reads, and S3 reds an unregistered word. Unit 12 :64-66 says unit 23 adds its row there, and :160-161 rejects a members column on the namespace row. | sound | - |
| 4 | coherence | memory/builds/dLinkedLibrary/spec/2026-10-26-spec-TOOL-dLinkedLibrary-17.md:section 2 S5 and section 4 'The pairing walk' (with TOOL-dLinkedLibrary-18 S2, AC2) | high | high | confirmed | The two specs disagree on both points. Depth: unit 18 AC2 (:250-252) puts nested `b` at depth 2, which makes a top-level span depth 1. Unit 17 S5 (:82-83) refuses depth 1 or more as `nested`, and its table (:166-167) treats a well-formed pair as depth 0. Lead: unit 18 S2 (:45-47) defines a family marker as a lead followed by a name `[A-Za-z0-9_.-]+`. Unit 17 passes `("gov:note", "gov:end", None)` while its lines read `gov:note <first tag>` with a space before the tag, which that grammar does not admit. | sound | - |
| 5 | coherence | memory/builds/dLinkedLibrary/spec/2026-10-26-spec-TOOL-dLinkedLibrary-8.md:section 6 AC3 | high | medium | confirmed | Unit 1 :81 and :217 define `derive_kappa` as Cohen's kappa. In AC3's four planted rows (unit 8 :314-316) the raters agree on 2 of 4, so p_o = 0.5, p_e = 0.25 and kappa = 0.333. With p_o = 0.5 kappa can never reach 0.8. Unit 8 S6 (:97-99) exits 3 below 0.8 and writes no routing record, so AC3 cannot pass on a correct build. The effect is a loud criterion failure, contained to that check. | unsound | - |
| 6 | coherence | memory/builds/dLinkedLibrary/spec/2026-10-26-spec-TOOL-dLinkedLibrary-22.md:section 2 S6, section 4 'The decision rows', section 6 AC6 | high | medium | confirmed | Unit 22 S6 (:65-70) derives `decides` only by matching the row's current text against added lines of `git log --reverse -p`, with no fallback, and AC6 (:228-231) requires `0 with no decides target`. I re-ran the probe: added lines from that log over `memory/DECISIONS.md` and its archive, compared with the current rows. Three rows' exact lines were never added: TOOL-aMendedLedger-8, TOOL-aMendedLedger-9 and TOOL-aFoldedQuarry-9. My row regex counted 219 rows, not 292, but the three misses reproduce exactly. So AC6 fails on a correct build. | sound | - |
| 7 | coherence | memory/builds/dLinkedLibrary/spec/2026-10-26-spec-TOOL-dLinkedLibrary-11.md:section 2 S6 Readers, section 4 Files touched, section 6 AC7 (with TOOL-dLinkedLibrary-25 S7, AC9) | high | medium | confirmed | Unit 25 S7 (:72-79) and AC9 (:263-267) put `source_cited_ids_resolving_to_no_record` into `tools/memory-tree/ANNOTATION-STYLE.template.md` and its render. Unit 11 S6 (:80-97) deletes that signal. Its Readers list says the name is spelled nowhere else in `tools/` at base, and its Files touched (:178-188) omits both guide files. Unit 11 AC7 (:244-246) runs `git grep ... -- tools`, which matches the template. Unit 4 S12 amends A1 but never removes the signal's name. | sound | - |
| 8 | coherence | memory/builds/dLinkedLibrary/spec/2026-10-26-spec-TOOL-dLinkedLibrary-3.md:section 2 S3 and S6 (with TOOL-dLinkedLibrary-14 section 8 F1) | high | high | confirmed | Unit 3 S3 (:78-80) points `MAP_CLI` at `tools/memory-tree/gov_map.py`, and the S6 upgrade step re-points adopters the same way. Neither states a `lose` route, and grepping unit 3 for lose, win or verdict found none. TOOL-dTotalRecall-14:44 and :105 build `gov_map.py` only on TOOL-dTotalRecall-17's `win`. Unit 14 F1 handles the `lose` case explicitly. Unit 3 S4 keeps the announced skip when `MAP_CLI` is unreadable, so on a `lose` reuse evidence is never graded. That is a narrow path. | sound | - |
| 9 | coherence | memory/builds/dLinkedLibrary/spec/2026-10-26-spec-TOOL-dLinkedLibrary-23.md:section 2 S7, section 4 Inventory (with TOOL-dLinkedLibrary-8 section 4 'The kinds') | medium | medium | confirmed | Unit 8 :180-182 gives the instruction-paragraph `Ruling` values as `unit`, `amend <tag>` or `drop`, citing unit 23 S7. Unit 23 S7 (:76-83), its inventory (:166) and its Files touched (:189) use `discard` and add three values to `record-kinds.toml`. Unit 23 :30 itself says 'a drop'. | sound | - |
| 10 | coherence | memory/builds/dLinkedLibrary/spec/2026-10-26-spec-TOOL-dLinkedLibrary-25.md:section 2 S6, section 6 AC8 | medium | low | confirmed | I re-ran AC8's loop. It printed nothing, and 18 READMEs carry `status:`, so the criterion is green before S6 is built. S6 (:66-71) itself says that at base no README is in that state. The spec admits the zero but still uses a criterion that cannot fail to observe S6. The check is redundant and has no behavioural effect. | sound | - |
| 11 | coherence | memory/builds/dLinkedLibrary/spec/2026-10-26-spec-TOOL-dLinkedLibrary-1.md:section 2 S10, section 6 AC10 | medium | medium | confirmed | `ls memory/map` printed FOUNDATION.md, README.md, affordance-exempt.toml, baseline.toml, features and generated, with no `conventions/`. Check 3's map arm at check-memory-hygiene.sh:850 admits only those six. Unit 1 S3 writes nothing under the map, and `accept` needs the owner's proof. AC10 (:341-343) assumes a convention part is tracked 'at this unit's tip' but never says how one comes to exist. At the real tip it is green whether or not S10 is built. | sound | - |
| 12 | coherence | memory/builds/dLinkedLibrary/spec/2026-10-26-spec-TOOL-dLinkedLibrary-3.md:section 4 'What keeps the name', section 6 AC1 (with S7) | medium | medium | confirmed | Unit 3 S7 (:114-116) adds a `[[retired]]` row to `tools/govkit/registry.toml` with id `codebase-map/reuse-lookup`, whose surfaces name `reuse_lookup.py` and `reuse-lookup.agent.md`. Both match AC1's regex `reuse_lookup\|reuse-lookup`. The 'What keeps the name' list (:172-175) does not list registry.toml. AC1 excludes only `memory/builds`, `memory/archive` and `memory/research`. | sound | - |
| 13 | coherence | memory/builds/dLinkedLibrary/spec/2026-10-26-spec-TOOL-dLinkedLibrary-3.md:section 3 Non-goals (gap-mem-22) against README 'The problem this build exists to solve' | medium | medium | confirmed | The README (:15-19) lists gap-mem-22 among the 23 owned gaps and says closing every one is the goal bound. The brief (:323) assigns it to unit 3. A grep over all 25 specs finds gap-mem-22 only at unit 3:135, a non-goal that hands it to TOOL-dTotalRecall-21. No criterion observes it, and no deviation record in the build moves it. | sound | - |
| 14 | coherence | memory/builds/dLinkedLibrary/spec/2026-10-26-spec-TOOL-dLinkedLibrary-12.md:section 6 AC1 against AC2 and section 7 New arm | medium | medium | confirmed | AC1 (:181-184) requires every word printed by the census `git grep -ohE "gov:[a-z0-9][a-z0-9-]*" -- . ':!memory'` to have a row. The census table (:107) already registers the test fixture word `an-older-writer-mark` as kind `fixture`. The §7 selftest arm (:206) plants an unregistered word in `annotations.py`, which is tracked. If that fixture spells `gov:planted-word` literally, AC1 forces a row for it. A scratch clone for AC2 (:185-188) then inherits that row, and the plant passes. Nothing in S3 or S5 prevents the literal spelling. | sound | - |
| 15 | coherence | memory/builds/dLinkedLibrary/spec/2026-10-26-spec-TOOL-dLinkedLibrary-7.md:section 6 AC1, AC2 (with TOOL-dLinkedLibrary-17 S6, section 8 F3) | medium | medium | confirmed | Unit 17 S6 (:95-96) and F3 say a `hybrid loses` verdict builds no `gov:end` half of S4 and S5, and S5 is the `span` arm. Unit 7 :49-52 and AC1/AC2 (:232-239) require a `span` summary line and a `span` finding among six arms. A grep for 'hybrid' in unit 7 found nothing, so that route is unstated. | sound | - |
| 16 | coherence | memory/builds/dLinkedLibrary/spec/2026-10-26-spec-TOOL-dLinkedLibrary-6.md:section 6 AC7 | medium | medium | confirmed | AC7 (unit 6:224-228) equates the view's count with `research_returns.py --population HEAD`. Unit 13 S3 (:42-47) selects the view by declared kind `research-return`. Unit 13 S6 (:69-75) counts the population by file name containing `research` plus a research Serves binding. Unit 13 :133-136 has post-cutoff research-named design records declare `design-record`, so they are counted by `--population` but not shown in the view. Unit 6's own example row (:115) is a reuse-scout record whose name does not contain `research`. The two populations therefore differ by design. | sound | - |
| 17 | coherence | memory/builds/dLinkedLibrary/spec/2026-10-26-spec-TOOL-dLinkedLibrary-24.md:section 2 S1 (with TOOL-dLinkedLibrary-22 S2) | low | low | confirmed | Unit 22 S2 (:44-47) defines `GOTCHA_FIELDS` only as a `.memory-tree.conf` key listing the keys every class must carry, and names no admitted set. Unit 24 S1 (:36-39) adds its fields to '`GOTCHA_FIELDS`' admitted set (never its required set)', a set that no spec defines. | sound | - |
| 18 | coherence | memory/builds/dLinkedLibrary/spec/2026-10-26-spec-TOOL-dLinkedLibrary-25.md:section 2 S8 (with TOOL-dLinkedLibrary-24 S4) | low | low | confirmed | Spec 25 S8 (:83-84) has parse_front_matter refuse `kind: note` with a remedy naming `kind: class` and `No machine gate`. Spec 25's header reads `order 1` and spec 24's reads `order 5`. Spec 24 S4 retires 'the prose arm that asks a class to name a gate or say it has none' together with DECLARES_RE, declares() and --declares. After unit 24 lands, nothing reads the `No machine gate` sentence that unit 25's remedy points to. Spec 24 S4's Readers list does not include the remedy string. | sound | - |
| 19 | coherence | memory/builds/dLinkedLibrary/spec/2026-10-26-spec-TOOL-dLinkedLibrary-1.md:section 4 'The move' (with TOOL-dLinkedLibrary-22 S6, AC8) | low | low | confirmed | Spec 1:225 writes the pointer row as `…<routing record>. decides=record-kind.decision`, with a period before the segment. Spec 22 AC8 (:237) writes `· decides=feature.roles`. Spec 22 S6 (:65-69) and spec 17:64 only say `decides=<target>[,<target>]` segments and never state what delimits a segment. The two specs therefore spell the segment lead two ways, and the owning spec does not settle which is right. | sound | - |
| 20 | grounding | memory/builds/dLinkedLibrary/spec/2026-10-26-spec-TOOL-dLinkedLibrary-18.md:section 4 "The population" (the query and its 18-row table); section 2 S7; AC8 | high | high | confirmed | I re-ran both §4 queries at HEAD. The first returns sites that are not in the 18-row table: check-microformats.sh:28-29, gotchas.py:61, review_replay.py:64, check-unattended.test.sh:3705, unattended.sh:1279-1299 and the gen_build_index constants. check-microformats.sh:49 really is a region parser (`awk ... '$0 == o {f=1; next} $0 == c {f=0} f'`), and it is not re-pointed. The second query returns run-gates.test.sh:3600, merge-rows.test.sh:396, unattended.test.sh:3220-3221, resolve-python.test.sh:550/600/678 and pyrun.sh:15. Neither query returns format-guard.js: its line is `const FENCE_OPEN = ...` at :95, which the leading `^[A-Z_]*` cannot match, yet the table lists it. S6 and S7 say the census is 'the query of §4', so AC8's 0 cannot be reached as written, and real parsers stay outside the factory. | sound | - |
| 21 | grounding | memory/builds/dLinkedLibrary/spec/2026-10-26-spec-TOOL-dLinkedLibrary-23.md:section 2 S1 ("not already wiring (a pointer, a symlink or a copy of the charter)"), section 4 Evidence (build_region) | high | medium | confirmed | The installer evidence checks out. ALIASES defaults to 'claude gemini copilot' with MODE=pointer, and _wire_pointer_or_copy runs `cp "$CANON" "$p"` for every alias except claude. A copy counts as current only when `cmp -s` holds (:117). render_playbook.py:771-773 refuses a charter whose REGION_OPEN or REGION_CLOSE count is not 1. Spec 23 S1 defines 'not already wiring' only as 'a pointer, a symlink or a copy of the charter' and does not say how a drifted copy is treated. Its Migration section says that pre-existing adopters run the capture. AC6 tests only a current copy. A stale copilot copy carrying the gov:playbook pair can therefore be captured, which doubles the region and makes later renders refuse. I grade it medium rather than high because the path is narrow (the copy must be stale when the capture runs) and the failure is a loud refusal, not a silent wrong result. | sound | - |
| 22 | grounding | memory/builds/dLinkedLibrary/spec/2026-10-26-spec-TOOL-dLinkedLibrary-4.md:section 2 S3 and S7; section 4 Rollout; section 5 perf | high | high | confirmed | Spec 4 S3 (:65) limits candidate files to `git grep -l -I -E "gov:(note\|feature\|end)\b"`. S7 (:101-103) grades 'any comment line of the scanned files'. Rollout (:252) and Migration (:244-246) still say that the 6,540 existing id-bearing comment lines are graded. I ran `git grep -n -E "gov:(note\|feature\|end)\b" -- tools skills .githooks` and it printed nothing, so the default population is empty. drift_report.py:2236-2250 scans every tracked non-memory file, which is the signal that spec 11 deletes. The spec contradicts itself, and the replacement arm grades nothing. | sound | - |
| 23 | grounding | memory/builds/dLinkedLibrary/spec/2026-10-26-spec-TOOL-dLinkedLibrary-5.md:section 4 Evidence, third bullet; section 2 S3 (the `<build>` cell) | medium | medium | confirmed | Spec 5:97 states that memory/builds/<slug>/README.md exists for every build a row id names, and S3 renders `<build>` as a relative link to that README. `git ls-files memory/builds/<slug>` printed nothing for aTaperedSluice, aWarmedTether and bQuiltedLantern, and only BACKLOG.md for aWidenedGuide. Live rows exist for each slug in DECISIONS.md (lines 30-31, 64, 69, 143, 210-213). check-memory-hygiene.sh check 2 (:704-718) exempts only DECISIONS.md, decisions/ and archive/, so a view under memory/views/ with these links would fail link integrity. | sound | - |
| 24 | grounding | memory/builds/dLinkedLibrary/spec/2026-10-26-spec-TOOL-dLinkedLibrary-8.md:section 6 AC3 | medium | medium | confirmed | Spec 1:217 defines derive_kappa as Cohen's kappa, (p_o-p_e)/(1-p_e). AC3's labels are A=major,minor,waiver,major and B=major,minor,process-rule,minor. That gives p_o=0.5, p_e=0.25 and kappa=0.333. Since kappa < p_o=0.5 for any p_e>=0, the stated 0.8 floor can never be met, and S6 (:98) exits 3 below 0.8 and moves nothing. The criterion cannot go green as written. | unsound | - |
| 25 | grounding | memory/builds/dLinkedLibrary/spec/2026-10-26-spec-TOOL-dLinkedLibrary-24.md:section 1 Goal, section 2 S8, section 8 F4, AC10 ("figure: PINNED, 7 at 5fede642") | medium | medium | confirmed | Spec 24 (:22, :84, :235-238) pins '7 class records whose prose names a manifest leg' (figure PINNED, 7 at 5fede642) but gives no predicate and no list. My probe over memory/gotchas/*.md, with leg names taken from tools/gate-legs.json, found 65 records carrying 'gated by/in/at'. 16 class records contain any leg name, 12 contain a backtick- or quote-delimited leg name, and 10 contain a delimited leg name and also a gated phrase (the same 10 stems the finder lists). No reading I tried gives 7, so the backfill population and AC10's pass condition cannot be reproduced. | sound | - |
| 26 | grounding | memory/builds/dLinkedLibrary/spec/2026-10-26-spec-TOOL-dLinkedLibrary-3.md:section 4 "What keeps the name"; AC1 | medium | medium | confirmed | Spec 3 S7 (:114-116) writes a `[[retired]]` row in tools/govkit/registry.toml with id `codebase-map/reuse-lookup` and two file surfaces that name the retired files. S6's step row lives in tools/codebase-map/kit.toml (an `[[upgrade]]` row), not in registry.toml. §4 'What keeps the name' (:170-175) lists the receipt fixture, the check-12 branch and its suite case, S6's step program and row, and the help page, and does not list registry.toml. registry.toml has no hit for the name today (git grep printed nothing), so S7 is what introduces the hits. AC1 then requires every hit to sit in a listed file, so the unit's own row makes AC1 fail. | sound | - |
| 27 | grounding | memory/builds/dLinkedLibrary/spec/2026-10-26-spec-TOOL-dLinkedLibrary-25.md:section 2 S6; AC8 | low | low | confirmed | `git grep -l '^status:' 5fede642 -- 'memory/builds/*/README.md' \| wc -l` printed 19. At HEAD it printed 18, and dLinkedLibrary's README no longer matches. `git log -S'status:'` on that README shows 5a9183011, the spec commit. I ran AC8's loop at HEAD and it printed nothing. S6's 'this build's own README first' therefore describes an edit that has already been made, and AC8 is green before the unit is built. | sound | - |
| 28 | grounding | memory/builds/dLinkedLibrary/spec/2026-10-26-spec-TOOL-dLinkedLibrary-25.md:section 4 "The decision log after S3 and S4", the check-27 paragraph | medium | medium | confirmed | Spec 25:156-158 says check 27 'finds its old row at the base as its top hit'. In row_grammar.py:1243-1257, eligibility is a HEAD record whose (kind, ident) is present at the base. measure_near_match (:1262-1281) takes the first eligible BM25 hit over the HEAD index, and only a same-slug top hit counts as own. The re-keyed rows' texts differ from the rows that keep the original ids: DECISIONS.md:46 vs :50 for -5, :47 vs :51 for -6, and :58-61 for -1. After the re-key their own text exists only under the new, ineligible suffixed id. Nothing guarantees the top eligible hit is an own-slug row, so the spec's reason that these rows cannot be graded is unfounded. | sound | - |
| 29 | grounding | memory/builds/dLinkedLibrary/spec/2026-10-26-spec-TOOL-dLinkedLibrary-2.md:section 10 Reuse audit (scout A's gotchas readers) and section 4 Evidence (role body bytes) | low | low | confirmed | Spec 2:342-344 says gotchas.load_leg_names and gotchas.records are memory-tree functions 'a codebase-map module may not import'. tools/codebase-map/kit.toml:7 reads `requires = ["memory-tree"]`, and spec 4:202 relies on that same import direction. Spec 2:143 says the scout's 'body is 1057 bytes'. `wc -c` on gov-reuse-scout.agent.md printed 1057 for the whole file, while the front-matter-stripped, CR-removed body measures 647 bytes, which is what check_roles.py:222 measures (`len(body.encode("utf-8"))`). | sound | - |
| 30 | reuse | memory/builds/dLinkedLibrary/spec/2026-10-26-spec-TOOL-dLinkedLibrary-18.md:section 4 "The population" and S7 census query; section 10 | high | high | confirmed | govkit.py:5776 `find_block` has the docstring 'REPRODUCES the shipped splice's refusal table, deliberately' (column 0, one CR, exactly one pair, close after open), and write_block (:5806) splices through it. It is called at :5626, :7240, :7614, :7769 and :9924. Its markers come from marker_pair() (:5762, `f"# {block_id}"`), not from module constants, so neither §4 query can see it. Spec 18 mentions govkit.py only as a scout hit for marker_pair (:349), as a version file, and in scan_hold_region. find_block is not in the population table and not in any non-goal. The census would print 0 sites while this hand-written copy of the contract remains. | sound | - |
| 31 | reuse | memory/builds/dLinkedLibrary/spec/2026-10-26-spec-TOOL-dLinkedLibrary-4.md:section 2 S7 (`derive_defined_ids`); section 8 F2; section 10 | high | medium | confirmed | gotchas.py:160-186 load_defined_ids takes `corpus_ids.walk(...)['defs']` and states 'so there is still ONE id grammar'. corpus_ids.py:957-972 `_render_defined_ids` gives the defined set as spec H1, backlog row or decision row, and cites KICK-aReplayedCard-2 (DECISIONS.md:17). TOOL-aFoldedQuarry-5 is in archive/DECISIONS.2026-08-10.md:27. Drift's definition half (drift_report.py:2218-2232) is a different set: anchors anywhere under the memory root plus own-H1. Spec 4 S7 mints derive_defined_ids from drift's half, and F2 (:391-397) never weighs corpus_ids (`grep -c corpus_ids` printed 0). That creates a second defined-id predicate in memory-tree that can disagree with check 18 and --card --append. I grade it medium because the effect is limited to which citations are marked red. | sound | - |
| 32 | reuse | memory/builds/dLinkedLibrary/spec/2026-10-26-spec-TOOL-dLinkedLibrary-22.md:section 2 S5 (trailer rows); section 10; and spec 17 section 3 | medium | medium | confirmed | PLAY-dOrderedCharter-28:67 types a commit's `Decided:` as `decides` in its commit adapter. Spec 22 S5 (:60-64) separately derives trailer rows with `decides = [<sha12>]`. Spec 17:107-109 says the commit adapter is 're-pointed at commit_trailers.decided by TOOL-dLinkedLibrary-22'. A grep over the dLinkedLibrary specs finds no such re-point: spec 22 §10 (:294-299) only notes that its rows agree with the adapter. TOOL-dDeclaredLoop-23:67 leaves edge_grammar.py's commit adapter to dOrderedCharter. The re-point that spec 17 attributes to spec 22 is owned by no spec, and two producers of the same edge remain. | sound | - |
| 33 | reuse | memory/builds/dLinkedLibrary/spec/2026-10-26-spec-TOOL-dLinkedLibrary-24.md:section 2 S1 and S3; section 10 | medium | medium | confirmed | `grep -n "dWitnessedBar\|seen_red\|seen-red\|tests"` over spec 24 printed nothing. TOOL-dWitnessedBar-22 S1/S4 (:23-47) declares a leg's `tests` tags on the leg row and derives every inverse through read_leg_edges. TOOL-dWitnessedBar-7 defines the seen-red line and its reader read_seen_red_records (:40, :48). TOOL-dTotalRecall-9 registers a `class` namespace (:75). Spec 24's class-side `gate:` key and its `observed:` line restate those facts in a second shape and do not cite the existing seams. | sound | - |
| 34 | reuse | memory/builds/dLinkedLibrary/spec/2026-10-26-spec-TOOL-dLinkedLibrary-25.md:section 2 S3 and S4; section 3; section 8 F1/F2 | medium | medium | confirmed | memory/DECISIONS.md:6 reads 'the file is never re-sorted and a landed row is never edited'. Spec 25 S3 moves 94 rows and relocates the DEPL section, and S4 rewrites the ids of five landed rows. F1 (:284-291) and F2 (:292-298) weigh options against check 24 and the append position but never against :6. The spec brief's I26, which cites DECISIONS.md:5-6, allows changes 'by supersession or pointer rows only'. TOOL-cSpliceWarden-4 (DECISIONS.md:26) concerns repairing a ratified archive. row_grammar.py:194-200 describes the suffix as a revision row, i.e. an amendment. | sound | - |
| 35 | reuse | memory/builds/dLinkedLibrary/spec/2026-10-26-spec-TOOL-dLinkedLibrary-23.md:section 2 S9; section 4 Files touched (`tools/playbook/namespaces.toml: S9's member`) | medium | medium | confirmed | spec-23:90-91 S9 says marker.legacy is 'registered through TOOL-dLinkedLibrary-12's namespace rows', and Files touched :187 lists 'tools/playbook/namespaces.toml: S9's member'. Spec-12 S1 (:35-40) makes the member registry tools/memory-tree/marker-words.toml with one [[marker]] row per word. Its §3 (:64-66) says unit 23 adds its own row there, and its Alternatives (:161) rejects 'A members column on the namespace row'. Spec 23 therefore points at the wrong seam, and no legacy row lands in marker-words.toml. | sound | - |
| 36 | reuse | memory/builds/dLinkedLibrary/spec/2026-10-26-spec-TOOL-dLinkedLibrary-23.md:section 4 "Paragraphs" | medium | low | confirmed | spec-23:153 spells the paragraph key as '<src>#p<sha8>, the first eight hex of the SHA-256 of its text with whitespace runs folded to one space'. Spec 23 never names derive_pin_hash (grep found none). PLAY-dOrderedCharter-24 S7 (:61-65) factors exactly that normaliser, ends stripped, into derive_pin_hash, and says 'Every later pin calls derive_pin_hash'. Spec 11 S2 does call it. The two implementations already differ on the end-strip, but only spec 23 derives these keys, so the risk is drift. Graded low. | sound | - |
| 37 | reuse | memory/builds/dLinkedLibrary/spec/2026-10-26-spec-TOOL-dLinkedLibrary-7.md:section 2 S1 and S5; section 10 (also spec 9 S4, spec 10 Files touched, spec 23 Files touched) | medium | medium | confirmed | dWitnessedBar is a parent of dTotalRecall, which is dLinkedLibrary's parent, so it lands first. TOOL-dWitnessedBar-11 S2 renders tools/gate-legs.json from declarations and has a --check. Its S8 (:73-75) says any later leg 'is one declaration the factory renders; the factory refuses a manifest row no declaration produces'. Spec 7 S1 writes a row straight into gate-legs.json (it also adds a [[gate_leg]] table). Spec 9 S4, spec 10 :153 and spec 23 :191 add only gate-legs.json rows with no declaration. No spec in the set names leg_factory. | sound | - |
| 38 | reuse | memory/builds/dLinkedLibrary/spec/2026-10-26-spec-TOOL-dLinkedLibrary-8.md:section 2 S6; section 4 "The decisions" and Inventory (`route_candidates`) | medium | low | confirmed | Spec-8 S6 (:97-102) reads the two labels files 'in TOOL-dLinkedLibrary-1's form', settles candidates itself and mints route_candidates. Spec 1's I2 (S5) exports derive_kappa, CLASSES, RUBRIC and the labels form, but no labels reader, so each module parses that form on its own: a real duplication. Some of the stated impact does not hold. derive_kappa, including its refusal rules, is shared, so a kappa fix lands in both. The split and lifecycle differences are the clause's own, not drift (spec-8 :37 and the :221 table). Spec 1's route is also specific to log rows: it moves rows and handles homes. What remains is the duplicated labels parsing and settling. Graded low. | sound | - |
| 39 | reuse | memory/builds/dLinkedLibrary/spec/2026-10-26-spec-TOOL-dLinkedLibrary-15.md:section 2 S1 (`derive_source_purpose`); section 10 | medium | medium | confirmed | Spec-15 S1 (:40-43) defines the header for non-Python files as 'the contiguous # or // comment block ending on the line above line', a scanner of its own. Spec 4 S4 (:68-73) adds extract_comment_spans(src, ext), which excludes strings, to the lexer block. Specs 11 and 17 consume it. Spec 15 never names it, although it already has a consumes-from edge on unit 4, for parse_note_line. | sound | - |
| 40 | reuse | memory/builds/dLinkedLibrary/spec/2026-10-26-spec-TOOL-dLinkedLibrary-23.md:section 2 S7; section 4 Files touched (`record-kinds.toml`: "the `ruling` row's three added `Ruling` values") | low | medium | confirmed | Spec-8 :182 lists the instruction-paragraph Ruling values as 'unit, amend <tag> or drop (TOOL-dLinkedLibrary-23 S7)'. Spec-23 S7 (:78-83) uses 'unit\|amend <tag>\|discard' and its inventory (:166) mints 'discard'. Its Files touched :189 adds the values to the ruling row again. The two specs spell one value two ways, so the field check refuses one spelling's records. | sound | - |
| 41 | reuse | memory/builds/dLinkedLibrary/spec/2026-10-26-spec-TOOL-dLinkedLibrary-2.md:section 10 ("memory-tree functions a codebase-map module may not import"); section 4 "The index" Gate legs row | low | low | confirmed | Spec-2 :342-344 says gotchas.load_leg_names and gotchas.records are 'memory-tree functions a codebase-map module may not import', so the index reads LEG_MANIFEST itself. tools/codebase-map/kit.toml:7 reads requires = ["memory-tree"], and spec-4 :202 relies on that same edge to import annotations.py. The premise is false. load_leg_names (gotchas.py:191-202) handles a blank key and a malformed manifest, and spec 2's own reader would skip that handling. | sound | - |
| 42 | reuse | memory/builds/dLinkedLibrary/spec/2026-10-26-spec-TOOL-dLinkedLibrary-16.md:section 4 "The counts" (`read_files`) | low | low | confirmed | Spec-16 :118-120 defines a shell read as a cat/head/tail/sed/awk/less/wc segment, read by extract_segments. Spec-7 :76-77 types a different list (grep, rg, sed -n, git grep, git show, Get-Content, Select-String), and S6's 'shell read' has no single definition. runlog/extract.py:479-530 holds _derive_program, which handles wrappers and interpreters, and _derive_segment. It has no read class, and spec 16 does not cite them. The two measures count reads by different predicates. | sound | - |
| 43 | blast-radius | memory/builds/dLinkedLibrary/spec/2026-10-26-spec-TOOL-dLinkedLibrary-3.md:section 4 'What keeps the name' and Files touched; section 7 | high | medium | confirmed | The leg 'dead-path carriers (deleted files still named)' (gate-legs.json:1368) has no guard. check-dead-paths.sh:186-195 git-greps everything outside memory/, plus the dossiers and gotcha pages, for deleted basenames. Spec 3 keeps the receipt fixture, and git grep shows tools/govkit/fixtures/adopter-ic-2cff5855.receipt.json:64-69 spelling reuse_lookup.py and reuse-lookup.agent.md. The check-hygiene test spells reuse_lookup.py at :140 and :3451-3473. Spec 3 names neither the leg nor tools/dead-path-waivers.txt (no 'dead-path' in the spec set). AC1 greps only reuse_lookup\|reuse-lookup. One part is overstated: WIRE-INTO-PROJECT.md, kit.toml, selftest.py, registry.toml and the dossier ARE in spec 3's Files touched. Graded medium rather than high, because the bar reds before a merge and nothing wrong ships. | sound | - |
| 44 | blast-radius | memory/builds/dLinkedLibrary/spec/2026-10-26-spec-TOOL-dLinkedLibrary-3.md:section 2 S1 Readers; section 4 Files touched; section 7 | medium | medium | confirmed | memory/project/encoding-posture-sites.txt:20-21 carries rows for tools/codebase-map/rank_harness.py and replay-phrases.py. Its header (:9-11) states set equality in both directions, so 'a row the scan no longer finds fails'. gate-legs.json:243-253 runs the unguarded leg 'encoding posture (text IO names its encoding)' over that file. Spec 3 deletes both files in S1. It never names the registry (no 'encoding' in spec 3), and its §7 line omits the leg. | sound | - |
| 45 | blast-radius | memory/builds/dLinkedLibrary/spec/2026-10-26-spec-TOOL-dLinkedLibrary-9.md:section 2 S4; section 4 Files touched; section 7 | medium | medium | confirmed | Spec-9 S4 (:58-62) adds two legs and gives neither a chunk nor a subject, and the check leg no ceiling. Files touched lists only record_origin.py, tree_lib.py, record_find.py, gate-legs.json, README and the help pages. An existing selftest leg carries rows at kit.toml:289, subject-pins.tsv:44, selftest-budgets.txt:65, foreign-prefix.gov.test.sh:130, ceiling-evidence.txt:56 and the map baseline. govkit.py:2945 fails an unclaimed leg, run-selftests.sh:830-838 fails a held leg with no budget row, and foreign-prefix:48-50 reds an undeclared whole run. None of these legs is on spec 9's §7 line. | sound | - |
| 46 | blast-radius | memory/builds/dLinkedLibrary/spec/2026-10-26-spec-TOOL-dLinkedLibrary-10.md:section 4 Files touched; section 7 | medium | medium | confirmed | Spec 10 names the 'retrofit progress selftest' leg only at :136 (inventory), :153 (Files touched: gate-legs.json) and :214-217 (the arm line). No scope item gives its argv, chunk, subject, guard or ceiling. Files touched lacks the kit.toml [[gate_leg]], subject-pins, selftest-budgets, foreign-prefix and dossier rows that govkit.py:2945, run-selftests.sh:838 and foreign-prefix:48-50 require. §7 lists none of those meta legs. | sound | - |
| 47 | blast-radius | memory/builds/dLinkedLibrary/spec/2026-10-26-spec-TOOL-dLinkedLibrary-23.md:section 4 Files touched; section 7 | medium | medium | confirmed | Spec-23 Files touched (:181-192) names 'tools/gate-legs.json: the adopt instructions selftest leg' and, for kit.toml, only 'S4's project-owned rule'. It has no [[gate_leg]], subject-pins, selftest-budgets, foreign-prefix or dossier claim, and no scope item defines the row. Its §7 line omits govkit selfcheck, codebase-map coverage + freshness, foreign-prefix parity and the held-leg budget leg. | sound | - |
| 48 | blast-radius | memory/builds/dLinkedLibrary/spec/2026-10-26-spec-TOOL-dLinkedLibrary-7.md:section 2 S1 and S5; section 4 Files touched | medium | medium | confirmed | Spec-7 S1 (:58-61) and S5 (:92-97) name kit.toml, subject-pins.tsv, selftest-budgets.txt and the dossier claims. Files touched holds no foreign-prefix.gov.test.sh entry, no FOREIGN_PREFIX_PROBE stop in either suite, and no memory/map/generated/* artifacts. foreign-prefix.gov.test.sh:35 and :48-50 red an undeclared row that prints no marker. Leg names do appear in generated MAP.md:44 and inventories.json:37. §7 omits both foreign-prefix parity and codebase-map coverage + freshness. | sound | - |
| 49 | blast-radius | memory/builds/dLinkedLibrary/spec/2026-10-26-spec-TOOL-dLinkedLibrary-14.md:section 7 New arm line | high | high | confirmed | TOOL-dTotalRecall-8 S13 (:96) defines the 'code record' leg as argv code_record.py --check. --check (S8 :70) re-derives the record and runs no selftest, and no leg anywhere runs code_record.py --selftest: git grep found only the arm lines. The arm lines claim otherwise: spec-14 :245 says gov_code.py --selftest is 'run by the code record leg beside code_record.py --selftest'. Spec-15 :253 and spec-21 :232 make the same claim. Neither spec 14 nor spec 15 lists code_record.py or gate-legs.json in Files touched, so the coverage these lines claim runs on no bar. | sound | - |
| 50 | blast-radius | memory/builds/dLinkedLibrary/spec/2026-10-26-spec-TOOL-dLinkedLibrary-8.md:section 7 New arm line | high | high | confirmed | Spec-8 :363 says adopt_program.py --selftest 'runs every plant under the record-kinds leg'. TOOL-dTotalRecall-1 S3 (:65-69) defines that leg as record_kinds.py --check, a registry conformance check. Spec 8's Files touched lists record_kinds.py only for 'the ledger sentinel' and lists no gate-legs.json, so nothing wires AC1-AC8's plants onto any bar. | sound | - |
| 51 | blast-radius | memory/builds/dLinkedLibrary/spec/2026-10-26-spec-TOOL-dLinkedLibrary-25.md:section 2 S1; section 4 'The README as an artifact' and Files touched | high | - | refuted | The premise is false on re-probe. tools/codebase-map/kit.toml:148-156 declares a [[generated]] row with check = gen_map.py --check. Before the queue, run-gates.sh:1440-1458 runs regen.py --check, which runs every declared check, and a stale output exits the bar 2. The pre-push hook scrubs GATE_REGEN_CHECK from the bar that lands (run-gates.sh:1434). Once spec 25 S1 adds the README to _artifacts(), every bar compares it through gen_map.py --check. It is true that test_codebase_map.py's explicit list does not cover it, but the bar still enforces the guarantee the finding says is lost. | unsound | - |
| 52 | blast-radius | memory/builds/dLinkedLibrary/spec/2026-10-26-spec-TOOL-dLinkedLibrary-6.md:section 2 S2; section 4 Files touched; section 7 | medium | medium | confirmed | Spec 6 S2 (:41) puts `LIBRARY_VIEWS` in `.memory-tree.conf`, and spec 5 :33 and :158 set it there. `.memory-tree.conf` is a tracked root `.*.conf`. policy.py:1197-1214 turns each of its keys into a legacy-home row, exempting only keys that match RETROFIT_KEY `_(?:CUTOFF\|PIN)$` (:1125). At :1280-1284 it reports any grown row as 'is a new legacy home and the list is shrink-only'. legacy-homes.txt has no LIBRARY_VIEWS row. In gate-legs.json the `policy check` leg has no guard, so it runs on every bar. Neither spec's §7 names `policy check`: spec 6 :232 has `policy fixtures` only, and spec 5's §7 has neither. Spec 3 :158-160 already rejects a new conf key on exactly this ground. | sound | - |
| 53 | blast-radius | memory/builds/dLinkedLibrary/spec/2026-10-26-spec-TOOL-dLinkedLibrary-22.md:section 2 S2; section 4 Files touched; section 7 | medium | medium | confirmed | Spec 22 S2 (:44-47) adds `GOTCHA_FIELDS` to `.memory-tree.conf`, and :176 lists that file as touched. The key does not end in _CUTOFF or _PIN, and legacy-homes.txt has no GOTCHA_FIELDS row, so the unguarded `policy check` leg reds on it as a new legacy home. The §7 line (:248) names `policy fixtures` but not `policy check`. tools/policy/ holds catalogue.toml and unsummarised-keys.txt, and .governance/policy.json exists, so the fix's files are real. The catalogue already has `set` and `list` types. | sound | - |
| 54 | blast-radius | memory/builds/dLinkedLibrary/spec/2026-10-26-spec-TOOL-dLinkedLibrary-2.md:section 8 F1; section 4 'The index' and Files touched | low | low | confirmed | Spec 2 F1 (:311) adopts `HOUSE_INDEX_DIRS` and `HOUSE_INDEX_KINDS` as `.codebase-map.conf` keys (:151-152, :167). legacy-homes.txt lists six `.codebase-map.conf` keys and neither of these, so the first tree that declares one trips the shrink-only refusal. map_extractors.py:208-209 builds `workflow-scripts` from a glob over `*.js` in the workflows kit dir. test_codebase_map.py:141-151 reds an unclaimed key, and :155 reds a baseline that gains a key. review-harnesses.md:22-32 claims each workflow script by name. Spec 2's Files touched (:209-220) names no dossier and no memory/map/generated artifacts for the new `reuse-bench.js`. | sound | - |
| 55 | blast-radius | memory/builds/dLinkedLibrary/spec/2026-10-26-spec-TOOL-dLinkedLibrary-19.md:section 2 S4 Readers | medium | medium | confirmed | I re-ran the git grep. It prints memory/map/README.md:30, tools/codebase-map/INVENTORY-DERIVATION.md:67 and :105, and tools/codebase-map/gen_map.py:121, each still telling authors to document shared seams in dossiers' `## Shared seams` prose. Spec 19 S4's Readers (:66-72) name only gen_map.py:103-104 and its render, README.md:114-115 and replay-phrases.py:31. Files touched (:165-177) does not list INVENTORY-DERIVATION.md. After the move, these lines direct a dossier shape that `test_dossier_holds_no_prose` refuses. | sound | - |
| 56 | blast-radius | memory/builds/dLinkedLibrary/spec/2026-10-26-spec-TOOL-dLinkedLibrary-5.md:section 7 leg line | medium | medium | confirmed | `python tools/check-spec-tokens.py --legs-for tools/memory-tree/check-memory-hygiene.sh` printed `policy fixtures <- tools/memory-tree/check-memory-hygiene.sh [selftests/kit]`, with no `broad` tag. `.memory-tree.conf:356` holds SPEC_GUARD_LEGS_CUTOFF="2026-09-22". Spec 5 (dated 2026-10-26) lists check-memory-hygiene.sh under Files touched (:160), and its §7 line has no `policy fixtures`. check-spec-tokens.py:1589ff reports one hit for each missing guarded leg, so the spec-tokens leg reds on this spec. | sound | - |
| 57 | blast-radius | memory/builds/dLinkedLibrary/spec/2026-10-26-spec-TOOL-dLinkedLibrary-3.md:section 2 S5; section 5 risks | low | low | confirmed | `wc -c` printed 66859 for memory/guides/UNATTENDED-PROTOCOL.md, and template-size-highwater.txt:11 holds 66860. check-template-size.sh:19-25 says a breach under `warn` prints BUDGET WARN and exits 0, and the high-water ratchet is advisory. Spec 3 S5 rewrites the `reuse-probed` and `MAP_CLI` rows (:67, PROTOCOL.template.md :356, :515) and lists the render under Files touched (:207). It states no size constraint, and its §7 (:279) omits `unattended protocol size`. Any net growth therefore ships with only a warning. | sound | - |
| 58 | failure-envelope | memory/builds/dLinkedLibrary/spec/2026-10-26-spec-TOOL-dLinkedLibrary-9.md:section 4 "The derivation" steps 2-5 and its table; against TOOL-dLinkedLibrary-8 S3, S6 and section 4 "The kinds", and TOOL-dLinkedLibrary-23 S7 | blocker | blocker | confirmed | In spec 9 §4 (:119-128), step 2 takes the landing build from the folder P sits in. Step 3 takes the subject from P's served ids. Step 5 answers `written` when step 4 finds no earlier commit or that commit's build is a landing build. Spec 8 has the door mint every adopt record under the adoption build's `--build/--unit` (:76-78), in that build's `build/` folder (:183-184). The routing record carries `**Serves:** research <unit id>` and `**Origin:** reconstructed@…` in that same folder (:212-213). Spec 23 S7 (:79-81) writes rulings with `--imported-from` the same way. For each of these, steps 2 and 4 both land on the adoption build, so step 5 answers `written`. Under the table (:133-134) both `reconstructed@` and `imported:` are then red, and the `reconstructed-but-written` plant (:155) encodes exactly that. The `record origin` leg (S4) has no guard. So every adopter that uses the adopt program gets a check that reports a false disagreement on the very path that writes the value. | unsound | - |
| 59 | failure-envelope | memory/builds/dLinkedLibrary/spec/2026-10-26-spec-TOOL-dLinkedLibrary-12.md:section 2 S1 and S3; section 4 "The census"; section 8 F1 | high | high | confirmed | Spec 12 S1 (:35-40) refuses any row whose `reader` is neither `none` nor a tracked path. S3 (:44-51) refuses both ways, including 'registered and appears nowhere'. The census rows (:95-107) name gov-only paths and words, such as `argv-begin` in check-unattended.sh, `an-older-writer-mark` in unattended-build.test.sh and `literal-python` in tools/lib/resolve-python.test.sh. In tools/memory-tree/kit.toml the `include = "**"` rule is role `engine`, so the registry ships with the kit. The spec never mentions an adopter, an install or `{prefix}` (grep found none). Spec 7 runs `annotations.py check` as a gate leg. In an adopter without the unattended kit, or one where the gov-only tests are withheld, the markers arm reds. | sound | - |
| 60 | failure-envelope | memory/builds/dLinkedLibrary/spec/2026-10-26-spec-TOOL-dLinkedLibrary-23.md:section 2 S1; section 4 "The legacy pair"; section 5 security | high | medium | confirmed | Spec 23 S1 (:49-54) captures each existing harness file that is not already wiring ('a pointer, a symlink or a copy of the charter'), its body verbatim. The spec never says whether a stale copy counts as wiring, and never refuses a body that holds marker lines. The current installer's copy mode is `cp "$CANON" "$p"` ('drift re-syncs with --force', adopt-agent-instructions.sh:136, :144), and AGENTS.md carries `<!-- gov:playbook -->` and its close. A stale copy is therefore captured whole, which puts a second gov:playbook pair into the charter. Spec 18's single-pair `find_pair` contract then refuses it. The §3 non-goal only covers aliases from now on, not a stale copy already present. I grade this below the finder: the consequence is a loud render refusal on a narrow path, not a silent wrong result. | sound | - |
| 61 | failure-envelope | memory/builds/dLinkedLibrary/spec/2026-10-26-spec-TOOL-dLinkedLibrary-23.md:section 4 "Paragraphs"; section 2 S3, S6 and S7 | high | medium | confirmed | Spec 23 §4 Paragraphs (:152-154) gives identical paragraphs one key and says they 'share one ruling'. S7 (:83-85) has a ruling remove 'the paragraph' and drop the count by one, and a second ruling for one key exits 2. Built as S7 states, a repeated paragraph's second copy stays in the pair and cannot be ruled. The count never reaches zero, and under `refuse` (S6, :72-75) the install cannot land. The spec is internally inconsistent, which leaves the builder to guess. I grade it medium rather than high. | sound | - |
| 62 | failure-envelope | memory/builds/dLinkedLibrary/spec/2026-10-26-spec-TOOL-dLinkedLibrary-23.md:section 2 S1; section 5 security | medium | medium | confirmed | Spec 23 S1 (:51-52) captures any harness file 'that exists and is not already wiring'. It never asks whether the file is tracked, gitignored, or a symlink to an outside target. §5 security (:204-206) does not price copying ignored or out-of-repo bytes into the tracked charter. Spec 8 S2 (:69-70) admits `--imported-from <path>` only after checking that the path is tracked, so a ruling on a paragraph from an ignored `.cursorrules` is refused. Under `refuse` that blocks landing. | sound | - |
| 63 | failure-envelope | memory/builds/dLinkedLibrary/spec/2026-10-26-spec-TOOL-dLinkedLibrary-23.md:section 2 S7 and section 4 Inventory; against TOOL-dLinkedLibrary-8 section 4 "The kinds" | medium | medium | confirmed | Spec 8 :182 closes the instruction-paragraph `Ruling` set as `unit`, `amend <tag>` or `drop`. Spec 23 :77-83 and :166 use `discard` instead, and :189 says record-kinds.toml gains 'three added Ruling values'. Grep finds `drop` only in spec 8 and `discard` only in spec 23. The two specs disagree on one closed value set. | sound | - |
| 64 | failure-envelope | memory/builds/dLinkedLibrary/spec/2026-10-26-spec-TOOL-dLinkedLibrary-24.md:section 2 S3; section 4 "The derivation"; section 5 | high | high | confirmed | Spec 24 S3 (:46-52) records `refused` for any non-zero exit of the planted run. A clean run that fails is `unobservable`, but the spec names no crash, exit-2 refusal, signal or timeout case. A grep for timeout, ceiling, crash, signal and hang found none in the spec, and §5 (:190) names only a plant that does not apply. A planted run that crashes therefore certifies `gated`, and S5 (:65-70) drops gated classes from every checklist. That is a gate claiming a refusal it never saw, on a narrow path. | sound | - |
| 65 | failure-envelope | memory/builds/dLinkedLibrary/spec/2026-10-26-spec-TOOL-dLinkedLibrary-19.md:section 2 S3; section 4 Rollout | high | high | confirmed | Spec 19 S3 (:47-56) hard-codes `--build dLinkedLibrary --unit TOOL-dLinkedLibrary-19` and a record path under `memory/builds/dLinkedLibrary/build/`. Rollout (:159-163) makes `apply` the adopter's update step once `test_dossier_holds_no_prose` reaches them. Spec 1 S3 (:60-66) writes proposals under `memory/builds/<slug>/build/`, from the `--build` it is given. An adopter running `apply` therefore names gov's build, not its own, while the shipped prose test reds every dossier that still holds prose. | sound | - |
| 66 | failure-envelope | memory/builds/dLinkedLibrary/spec/2026-10-26-spec-TOOL-dLinkedLibrary-19.md:section 2 S3 ("A second `apply` writes nothing"); section 5 error states | low | low | confirmed | Spec 19 §5 (:194-195) pre-checks only `parse_dossier` failures before any write. S3 claims 'A second `apply` writes nothing' (:56) but never orders writes per dossier and never says what happens when a propose call fails midway. Spec 1 S3 names each proposal by date and `<n>`, so a re-run on a later date writes duplicate proposals for dossiers that were not yet shrunk. Idempotency holds only after a run that completed. | sound | - |
| 67 | failure-envelope | memory/builds/dLinkedLibrary/spec/2026-10-26-spec-TOOL-dLinkedLibrary-8.md:section 4 "The census", the `ci-job` row; section 5 security | high | high | confirmed | Spec 8 :201 censuses only `.github/workflows/*.yml`, reads jobs by indentation with no rule for block scalars, and refuses on six substrings. `.yaml` workflows are therefore missed. `git -C x push`, `yarn publish`, `pnpm publish`, `cargo publish` and `terraform apply` match none of the patterns. Two of the finder's examples are wrong: `gh release create` contains the substring `gh release`, and `actions/deploy-pages` contains `deploy`, so both already match. The core claim holds: a publishing job can read `importable`, and §5 (:284-286) prices this census as the refusal point. | unsound | - |
| 68 | failure-envelope | memory/builds/dLinkedLibrary/spec/2026-10-26-spec-TOOL-dLinkedLibrary-4.md:section 2 S7 (`every-comment-ref`) | high | medium | confirmed | Spec 4 S7 (:101-104) requires that, under the default `every-comment-ref`, every `memory/` path a comment line cites is tracked. It gives no rule for cutting a path out of the prose. I re-ran the greps over tools and skills: 41 comment lines end a memory/ path with punctuation, 8 cite a `<placeholder>` path (for example agent-cap.js:1490 `memory/builds/<slug>/reviews`), and 5 cite a glob. stop-guard.js:89 cites a path with a `:299,` suffix. Built literally, these become false dangling citations. I grade it medium rather than high: the effect is false reds the bar shows, and they are contained. | sound | - |
| 69 | failure-envelope | memory/builds/dLinkedLibrary/spec/2026-10-26-spec-TOOL-dLinkedLibrary-11.md:section 2 S1 (and TOOL-dLinkedLibrary-4 S6 `required`, which reads the same base) | medium | medium | confirmed | tools/lib/compare_base.py returns (None, ...) at :38, :40 ('no remote to compare against') and :44 ('never fetched'). Spec 11 S1 (:44-49) and spec 4 S6 (:91-94) both read touched blocks 'since resolve_compare_base(root)'. A grep of both specs for no remote, never fetched, no base or a None case finds nothing, so neither spec defines what the budget arm or `required` grading does when there is no base. | sound | - |
| 70 | failure-envelope | memory/builds/dLinkedLibrary/spec/2026-10-26-spec-TOOL-dLinkedLibrary-11.md:section 2 S2 (`derive_block_anchor`) | medium | medium | confirmed | Spec 11 S2 (:50-53) keys a block by derive_pin_hash of its first line plus '#<n>', its ordinal among earlier blocks with the same opener. Adding or removing a same-opener block earlier in the file shifts every later ordinal, and S3 keys the untouched-long-blocks rows by (path, anchor), so those rows turn into unmeasured row plus undeclared site. AC2 (:220-223) only inserts plain lines. The same git grep re-run printed 547 banner lines under tools/. | sound | - |
| 71 | failure-envelope | memory/builds/dLinkedLibrary/spec/2026-10-26-spec-TOOL-dLinkedLibrary-14.md:section 2 S5 and S7 (`grep_words`) | medium | medium | confirmed | Spec 14 S7 (:63-71) specifies one `git grep -o -z -w -F -f - -- <pathspecs>` call and gives no empty-word guard. The donor at drift_report.py:2116 guards with `if ids:`. Re-probed: `printf '' \| git grep -c -w -F -f - -- README.md` exited 0 and listed .claude/agents/*.md, so git took README.md as the pattern. `printf '\n'` also listed every file. S5's `where` therefore returns a wrong non-empty answer for an empty or blank word. | sound | - |
| 72 | failure-envelope | memory/builds/dLinkedLibrary/spec/2026-10-26-spec-TOOL-dLinkedLibrary-14.md:section 2 S6; section 4 "Targets" | medium | medium | confirmed | In spec 14, S6 (:57-62) fires the not-extracted floor only 'when the target's file is one whose language ... lists with the extractor none'. Targets (:134) resolve a bare name to keys whose last segment matches, and an unextracted language has no keys, so the name resolves to nothing. S1 (:41-43) then exits 1 with `none — <target>`. AC5 tests only `show x.go::Run`. | sound | - |
| 73 | failure-envelope | memory/builds/dLinkedLibrary/spec/2026-10-26-spec-TOOL-dLinkedLibrary-7.md:section 2 S3 (the read hook's paths) | medium | medium | confirmed | Spec 7 S3 (:75-86) takes 'a Grep's path' and 'a directory argument's tracked files nearest first' into one `annotations.py lookup --path ...` launcher call. It gives no bound on the number of files, does not cover a Grep with no path (the root), and does not say whether a path whose rows the 2,048-byte cap cut off is still appended as pushed. S2's lookup takes only repeated --path flags, so argv is the only channel. Re-probed: `git ls-files \| wc -l` printed 8374, so a root-level expansion overflows the Windows command line. The directory class is unspecified. | sound | - |
| 74 | failure-envelope | memory/builds/dLinkedLibrary/spec/2026-10-26-spec-TOOL-dLinkedLibrary-3.md:section 2 S1 Readers | medium | medium | confirmed | Spec 3 S1 (:41-67) deletes rank_harness.py, replay-phrases.py and scen-adversarial.json. Its Readers list names selftest.py, WIRE-INTO-PROJECT.md and features/codebase-map.md, but omits tools/codebase-map/kit.toml (:48 and :57 include the deleted files) and memory/project/encoding-posture-sites.txt (:20-21 hold rows for rank_harness.py and replay-phrases.py). That file's header says 'a row the scan no longer finds fails'. The selftest lines that load these files by path (:1905, :2129, :2535, :2577) are not cited by value either. The git grep re-run reproduced every hit. | sound | - |
| 75 | failure-envelope | memory/builds/dLinkedLibrary/spec/2026-10-26-spec-TOOL-dLinkedLibrary-10.md:section 4 "The derivation", the `drained` row | medium | medium | confirmed | Spec 10's derivation table (:110) says 'a key gone now counts its whole period-start count', and a grep of spec 10 for rename or carry_renames finds only an unrelated risk line (:175). A renamed file's rows move to new keys (spec 11 S4, carry_renames), so the card counts the old keys as drained while `now` holds the same rows, and `drained` over-reports. | sound | - |
| 76 | failure-envelope | memory/builds/dLinkedLibrary/spec/2026-10-26-spec-TOOL-dLinkedLibrary-15.md:section 2 S3, S6 and S7; section 4 Files touched | medium | medium | confirmed | Spec 15 S3, S6 and S7 add memory/project/code-purposes.tsv (authored by agent passes) and code-purpose-pending.txt (re-rendered at every landing), and the spec mentions no merge, gitattributes or conflict anywhere. `grep merge= .gitattributes` shows no memory/project file. Sibling spec 11 S5 gives its two homes merge=rows. Concurrent landings that re-render the pending file will produce text conflicts. The fix is unsound for the .tsv: tools/memory-tree/merge-rows.py (docstring :6-20) is the driver for id-anchored index files and keys rows by record id or backlog row class, not by a TAB-separated code key, so `merge=rows keyed by <key>` names a keying the driver does not have. | unsound | - |
| 77 | failure-envelope | memory/builds/dLinkedLibrary/spec/2026-10-26-spec-TOOL-dLinkedLibrary-17.md:section 2 S4; section 4 "The span, by case" | medium | - | refuted | The cited section already says it. Spec 17 §4 'The span, by case' (:147-155) shows exactly this case: an inside-def note tagged feature.roles with a later `gov:end feature.roles`, annotated 'inside a def: to its end_line'. The pairing-walk table says a note whose span derives from a definition 'never enters the text', and S5 builds the pairing text only from notes 'whose span S4 does not derive from a definition'. So the inside note never pairs with that close. | sound | - |
| 78 | failure-envelope | memory/builds/dLinkedLibrary/spec/2026-10-26-spec-TOOL-dLinkedLibrary-18.md:section 2 S2 (`splice_region`); section 5 security | medium | medium | confirmed | Spec 18 S2 (:42-43) has splice_region write `body` between the markers. The security bullet (:230-232) and AC3 (:258-260) cover only a malformed pair already in the text, and no line of the spec checks body lines against is_marker_line. A body holding a marker line produces a doubled pair that find_pair refuses on every later read. | sound | - |
| 79 | failure-envelope | memory/builds/dLinkedLibrary/spec/2026-10-26-spec-TOOL-dLinkedLibrary-21.md:section 2 S2 and S5 | medium | medium | confirmed | Spec 21 S2 (:43-45) writes each blob 'under its blob id and its path's extension', and its own rejected alternative (:169-170) says ctags picks a parser by file name. An extensionless file such as Makefile, Dockerfile or a shebang script gets a bare blob-id name that ctags matches by neither name nor extension. S5 (:66-70) lists the `none` extractor only under `builtin`, so under ctags such a file is silently left at file level with no `none` entry for spec 14's floor to read. | sound | - |
| 80 | failure-envelope | memory/builds/dLinkedLibrary/spec/2026-10-26-spec-TOOL-dLinkedLibrary-25.md:section 2 S1; section 4 "The README as an artifact" | medium | medium | confirmed | gen_map.py:236-244 writes README.md only at --scaffold, and the _README literal (:92-134) marks only generated/ as 'never hand-edit'. Spec 25 S1 and §4 (:164-167) make --write render the README and --check report STALE, with --write named as the remedy. F3 (:300-305) weighs only the changed check, not adopter-edited text, and no line of the spec addresses an adopter README that differs from the literal. --write then overwrites that text. Git can recover it, which keeps the effect contained. | sound | - |
| 81 | failure-envelope | memory/builds/dLinkedLibrary/spec/2026-10-26-spec-TOOL-dLinkedLibrary-2.md:section 2 S7 and S8; section 4 "The slot"; section 5 security | low | low | confirmed | Spec 2 §4 'The slot' (:176) renders the matched state as the record's lines 'verbatim', and S7 (:78-82) and the security bullet (:233-235) state no line cap, byte cap or S5 grammar check. Only the index carries HOUSE_INDEX_MAX_BYTES (:63). The effect is limited to work-order size and free text from a scout record. | sound | - |
