**Serves:** spec-audit TOOL-dLinkedLibrary-83@rev-1 TOOL-dLinkedLibrary-84@rev-1 TOOL-dLinkedLibrary-85@rev-1 TOOL-dLinkedLibrary-81@rev-1 TOOL-dLinkedLibrary-82@rev-1 TOOL-dLinkedLibrary-86@rev-1

# Tier-2 spec audit: dLinkedLibrary, the round-5 promotions (units 81 to 86), round 1

Provenance: an adversarial review with five finder lenses (gov-spec-reviewer) and five skeptic batches (gov-skeptic), synthesized by gov-synthesizer on 2026-10-27.

Reviewed: memory/builds/dLinkedLibrary/spec/2026-10-27-spec-TOOL-dLinkedLibrary-83.md@003d63fd25988b81a118c8e892960f2fcd270933, memory/builds/dLinkedLibrary/spec/2026-10-27-spec-TOOL-dLinkedLibrary-84.md@419f03e8199d98a74b5615d94630468ddeac43c4, memory/builds/dLinkedLibrary/spec/2026-10-27-spec-TOOL-dLinkedLibrary-85.md@add28fc70e6d96bd9307b854fcbdfc3e062e316a, memory/builds/dLinkedLibrary/spec/2026-10-27-spec-TOOL-dLinkedLibrary-81.md@09080462bac999b8cce21c69fd8fc9325eb2c633, memory/builds/dLinkedLibrary/spec/2026-10-27-spec-TOOL-dLinkedLibrary-82.md@59f1277c869981db1671ba41e2f1413ff8c1d1f6, memory/builds/dLinkedLibrary/spec/2026-10-27-spec-TOOL-dLinkedLibrary-86.md@6dae38f4984ff1aa5bdcf4d95e4fa5da78483a94
ROUND 1

## Verdict: BLOCKED

No blocker stands. Four high items stand, each one raw high finding (ids 1, 27, 30, 33). The audit reports 28 items: 0 blocker, 4 high, 15 medium, 9 low. By raw confirmed finding it is 0 blocker, 4 high, 19 medium, 11 low (34 in all). The specs are not ready to build until the high items are fixed.

## Review shape

Intensity full, raw 37, confirmed 34, refuted 3, unverified 0 (0 uncertain), precision 0.92.

| lens | returned | raw | confirmed | refuted | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|
| coherence | yes | 12 | 11 | 1 | 0 | 0 | 0.92 |
| grounding | yes | 5 | 5 | 0 | 0 | 0 | 1.00 |
| reuse | yes | 3 | 2 | 1 | 0 | 0 | 0.67 |
| blast-radius | yes | 6 | 6 | 0 | 0 | 0 | 1.00 |
| failure-envelope | yes | 11 | 10 | 1 | 0 | 0 | 0.91 |

Run integrity: all 5 lenses returned and none died. All 5 skeptic batches returned and none died. No verdict was demoted for contradiction or as an orphaned duplicate refutation. No spurious verdict was discarded, and there were no duplicates. The skeptic judged all 34 fixes on confirmed findings sound. None was judged unsound, none was missing and none went unjudged. No confirmed finding was left ungraded by the skeptic. The skeptic re-graded 6 (ids 4, 7, 13, 25, 32, 34). No unverified finding remains. No lens notes were supplied, so every lens ran on the kit's generic brief.

Roles: finders gov-spec-reviewer, skeptic batches gov-skeptic, synthesis gov-synthesizer. Intent: 70 spec documents supplied as `specs`, as sibling context. Checklist: 49 items, each assigned to exactly one of 5 lenses (coherence 10, grounding 10, reuse 10, blast-radius 10, failure-envelope 9). By design: 1 invariant from the checklist's by-design block. Move check: no checked subject moved.

Every fix below was judged SOUND by the skeptic.

## High

### H1. 81's deny-by-default branch has no plant (id 1)

- **Where:** 81 §2 S2, S3 and S4; §6 AC3.
- **What is wrong:** S4 plants only `${{`-led items (`- ${{ if }}`, a `${{ if }}` key, `- ${{ each }}`) and a `- name:` control. Nothing plants an unknown plain first key (`- foo: bar`), a scalar `variables: ${{ parameters.vars }}`, or a `- template:` item for S3's interim refusal. AC3's "unknown form" clause therefore checks an empty population.
- **Consequence:** A builder who catches only `${{` passes AC1 to AC3 and the new arm. The census then grades `- someNewForm:` or a scalar expression `importable`, which is the class §1 says this unit closes, and the arm certifies a deny-by-default it never runs.
- **Fix (skeptic: sound):** Add three S4 plants with criteria. (1) `- foo: bar` at pipeline level, whose jobs read `refused: unreadable variables item foo`. (2) `variables: ${{ parameters.vars }}`, whose jobs read `refused: unreadable variables item expression`. (3) A `- template:` item graded in either 81/82 order. Point S2's and S3's "Observed by" at them. Stage the red by dropping the unknown-key branch.
- **Related:** M13 (id 28) is the same gap seen through the observed-by claim. It keeps its own medium grade.
- **Left-shift gate:** a spec-lint rule that every refusal branch S2 names has at least one S4 plant whose criterion quotes that branch's reason string.

### H2. 81's closed set of shapes leaves Azure flow style unread (id 27)

- **Where:** 81 §2 S1 and S2.
- **What is wrong:** S1 reads block lists and block mappings. S2 refuses unknown keys, `${{` items and keys, and a scalar. Nothing covers `variables: [ { group: release-vars } ]`, `variables: { NUGET_API_KEY: $(k) }` or a `- { group: x }` item, and the last has no "first key" for `<form>`. Only 83 S1 reads flow style, and only for GitLab `default:`. 82's `- template:` has the same hole.
- **Consequence:** A job with a flow-style variable group grades `importable`. That is a wrong security result on a narrow path.
- **Fix (skeptic: sound):** In S2, refuse with `<form>` `flow` any `variables:` whose value opens `[` or `{`, and any list item that opens `{`. Alternatively, read flow items as 83 S1 does and then apply S1's item test. Add the plant `variables: [ { group: release-vars } ]` beside two plain jobs, with an AC requiring both jobs refused.
- **Left-shift gate:** a bug-class checklist entry: every closed-set YAML reader names its flow-style handling, and its plants include one flow-style member.

### H3. 84's class of job-wide blocks omits GitLab's `spec: inputs:` header (id 30)

- **Where:** 84 §2 S1; §4 Evidence.
- **What is wrong:** S1 claims to close "every top-level block that reaches every job" but leaves out the `spec:` header document. Its `inputs:` defaults reach job text through `$[[ inputs.<name> ]]`. No census spec reads `inputs` or `$[[`.
- **Consequence:** Take a header `spec: inputs: cmd: default: npm publish`, then `---`, then a job running `"$[[ inputs.cmd ]]"`. The job runs `npm publish` but grades `importable`, because its text holds no refusal substring, no indirection token and no credential name.
- **Fix (skeptic: sound):** Add `spec:` (the header document before `---`) to S1. State that a job line holding `$[[` refuses with `refused: opaque step inputs <name>`. Plant a header-document file whose input default is `npm publish` and whose job runs `$[[ inputs.cmd ]]`, with an AC requiring the refusal. Cite GitLab's "Header keywords: spec" in §4 Evidence.
- **Left-shift gate:** a checklist entry: a spec claiming a class of upstream keywords cites the upstream keyword index in full, header keywords included.

### H4. 86 S2 normalises only the CR, not a UTF-8 BOM, and plants no Azure CRLF (id 33)

- **Where:** 86 §2 S2; §6 AC2.
- **What is wrong:** S2 strips only the trailing CR. No census spec says how a CI file is decoded, so a leading U+FEFF survives. AC2 plants CRLF in the GitLab and GitHub files but never in `azure-pipelines.yml`.
- **Consequence:** A BOM-led first line such as `before_script: [npm publish]`, `variables: *creds`, `default: *base` or `include:` no longer matches its key. The file-wide and global-key refusals do not fire, and jobs grade `importable`.
- **Fix (skeptic: sound):** State in S2 that every CI file, in every dialect, is decoded with `utf-8-sig` (or a leading U+FEFF is stripped) and the trailing CR is stripped from every line. Extend AC2 with a BOM-led CRLF `.gitlab-ci.yml` whose first line is `before_script: [npm publish]`, and a CRLF `azure-pipelines.yml` with a `- bash: |` block holding `npm publish`. Every job must read `refused: npm publish`.
- **Left-shift gate:** a shared CI-file reader in adopt_program.py that every dialect calls, with a selftest case for BOM plus CRLF on each dialect.

## Medium

### M1. 81's expression plants nest credential carriers that 79 already refuses (id 2)

- **Where:** 81 §2 S4 (trees 1 and 2); §6 AC1.
- **What is wrong:** The plants nest `- group: release-vars` and `NUGET_API_KEY`, which 79 S2 refuses at any level. No spec says which reason wins when 79 and 81 S2 both fire, yet AC1 demands exactly `refused: unreadable variables item expression`.
- **Consequence:** A correct 79 reader can turn AC1 red. The plants also cannot show that the expression refusal works on harmless nested content.
- **Fix (skeptic: sound):** Nest only non-credential content, e.g. `- name: CONFIG` and `CONFIG: Release`. Alternatively, state the reason a job carries when 79 and S2 both hit, and grade AC1 on that.
- **Left-shift gate:** a checklist entry: a plant meant to exercise one rule carries no content that an earlier unit's rule also refuses.

### M2. 84's indirection test is planted for only two of its eight blocks (ids 3, 32)

- **Where:** 84 §2 S1, S2 and S5; §6 AC1, AC3 and AC4.
- **What is wrong:** S1 names eight job-wide blocks. Indirection plants exist only for `variables: *creds` and the `workflow:` `rules:` `!reference`, and 86 S9 adds `after_script:`. `image:`, `services:` and `cache:` have no token plant, and `before_script:` has only a plain script line. AC4's row-name list leaves out `services`, `cache` and `after_script`.
- **Consequence:** A walk hardcoded to `variables:` and `workflow:` passes every criterion. `cache: *c` or `services: !reference [...]` then reaches every job unread.
- **Fix (skeptic: sound, both findings):** Add S5 plants `image: *img`, `services: !reference [.svc, services]`, `cache: *c` and `before_script: !reference [.p, script]`. Each needs a criterion reading `refused: opaque step <key> <block>:` for both plain jobs. Widen AC4 to all eight S1 blocks.
- **Note:** id 32 was graded low by its finder. The skeptic re-graded it medium because it is a gap in a security check.
- **Left-shift gate:** a spec-lint rule that a §2 item naming a class lists one plant per class member, or names the members it leaves unplanted.

### M3. 85's AC3 plant cannot tell a key-measured extent from a dash-measured one (id 5)

- **Where:** 85 §2 S2 and S4 (third plant); §6 AC3.
- **What is wrong:** The follow-on step `      - run: echo done` sits at column 6, the dash's own column. A dash-measured extent also ends there, so AC3's "Red when: measured from the dash" cannot fire.
- **Consequence:** S2's key-column rule, the reason this unit exists, ships unverified. A dash-measured reader would take sibling keys at column 8 (`env:`, `with:`, `name:`) as script.
- **Fix (skeptic: sound):** Follow the `- run: |` block with a sibling key at the key's column, e.g. `        name: npm publish`, and have AC3 require `importable`. Stage the red by measuring from the dash.
- **Left-shift gate:** the build's staged-red step must show that the named "Red when" break actually turns the criterion red before the criterion is accepted.

### M4. 83's multi-line and unclosed flow reads have no plant (ids 6, 29)

- **Where:** 83 §2 S1 and S4; §5 error states; §6 AC1 to AC4.
- **What is wrong:** S1 reads a flow collection across continuation lines, and §5 reads an unclosed one to end of file. Both claim "Observed by AC1 to AC4", but every S4 plant is a one-line `default:` value.
- **Consequence:** A reader confined to the `default:` line passes every criterion. Take `default: {` followed by `  before_script: !reference [.publish, script] }`: the jobs can stay `importable` whenever 76's below-the-line walk misses the continuation.
- **Fix (skeptic: sound, both findings):** Add a `default:` flow mapping split over three lines with `!reference` on the middle line, and one left unclosed at EOF holding `*base`. Add an AC requiring `refused: opaque step !reference default:before_script` (and the alias refusal) for both plain jobs. Stage the red with a single-line read, and name these ACs in S1's "Observed by".
- **Left-shift gate:** the same observed-by spec-lint as M13: every "Observed by" names a criterion whose plant holds the stated shape.

### M5. 86 AC6's `opaque step` grep cannot see a second refusal loop (id 8)

- **Where:** 86 §2 S7; §6 AC6.
- **What is wrong:** AC6 greps `opaque step` to prove that one function assigns every file-wide refusal. The grep prints only the lines that build reason text. It cannot see the function definition, and it cannot see a second loop over a file's jobs, which is AC6's own "Red when".
- **Consequence:** A build that keeps a separate loop for 76's `default:` or 84's blocks passes AC6, and S7's single-path claim ships unchecked.
- **Fix (skeptic: sound):** Observe the structure. A `python -I -c` ast walk over adopt_program.py counts the functions that assign a file-wide refusal (exactly 1) and lists the call sites for `include:`, `default:` and 84's blocks. Alternatively, stage a scratch-copy break that inlines a second loop and show the probe turns red.
- **Left-shift gate:** a checklist entry: a structural claim (one function, one path) is observed by a structural probe (ast or call graph), never by grepping a string.

### M6. 86 S25 has no slice rule for Python blocks hosted in `"$PYBIN" -c '...'` strings (ids 13, 34)

- **Where:** 86 §2 S24 and S25; §4 Evidence; §6 AC21.
- **What is wrong:** S25 names two containers only, a shell heredoc body and the runbook's fenced block. Four `resolve_prefix_token` hosts sit in `-c` strings: tools/run-gates/run-gates.sh:2740 and :4972, and tools/run-gates/run-gates.test.sh:631 and :669. The program at run-gates.sh:2711 is `"$RKD_PROGRAM"'...'`, and its literal calls `resolve_kit_dir`, which only the `<<'RKD'` heredoc at :176-178 defines.
- **Consequence:** The free-name read either skips these four hosts, so AC21 certifies a population it never read, or slices the literal alone and may report a false unbound name.
- **Fix (skeptic: sound, both findings):** Add a third container to S25. A `-c '...'` argument is sliced from its opening quote to its closing quote. A `"$VAR"` concatenated before it is replaced by that variable's heredoc in the same file (RKD_PROGRAM → the `<<'RKD'` body). Alternatively, name these hosts as refused with a reason. Name the four hosts in §4 Evidence. AC21's staged red should cover a `-c` host: a scratch run-gates.sh whose `resolve_prefix_token` literal loses an import must be named.
- **Note:** both findings were graded high by their finders. The skeptic re-graded both medium: built as written, AC21's own "Red when" goes red, so the gap blocks the build rather than shipping a false pass. The skeptic also judged the false-unbound half weaker than claimed, since 80 S11 counts only names the block references.
- **Left-shift gate:** the parity loop in tools/lib/resolve-python.test.sh reports any host whose container shape the slicer does not recognise, instead of skipping it.

### M7. 84 AC3's `<child>` contradicts the definition it borrows (ids 14, 23)

- **Where:** 84 §2 S2; §6 AC3, against 83 S2 and 76 S2.
- **What is wrong:** 84 S2 takes `<child>` "as 83 S2 defines it". For block style, 83 S2 defers to 76 S2: "the key of `default:` that holds it", the block's direct child. For `workflow:` → `rules:` → `- variables: !reference`, that rule gives `workflow:rules`, but AC3 expects `workflow:variables`. 83's flow-style rule (the nearest key at the token's flow depth) gives the innermost key, so the same nesting yields different reasons in block and flow style.
- **Consequence:** A builder cannot meet both S2 and AC3. Making AC3 pass diverges from 76 S2 and 86 S5, so `default:` and the other blocks print reasons by different rules.
- **Fix (skeptic: sound, both findings):** State one `<child>` rule in 83 S2 for both block and flow style: either the key on the token's own line (innermost flow key) or the block's direct child. Align 84 AC3 and 86 S5 with it, and add a depth-2 block plant under `default:` that tells the two readings apart.
- **Related:** L1 (id 4) is the same defect at the skeptic's low grade. It stays a separate item because the binding grades differ.
- **Left-shift gate:** a checklist entry: a borrowed definition is planted at the depth the borrowing spec uses, not only at the depth of the spec that first defined it.

### M8. 86 AC19's argv lets bash exit before the bound (id 15)

- **Where:** 86 §2 S22; §6 AC19.
- **What is wrong:** The argv is described only as "a `bash -c` argv whose backgrounded grandchild sleeps 3 seconds". With no trailing `wait`, bash exits at once and `run_command` returns status 0 before the 1-second bound. No kill runs, so both scratch copies leave the marker. The skeptic confirmed this by running a scratch copy of regen.py's `run_command`.
- **Consequence:** A correct build goes red under the plain reading, which invites a builder to weaken the criterion.
- **Fix (skeptic: sound):** Spell the argv as `bash -c "(sleep 3; echo x > <marker>) & wait"`, and require the first run to report status TIMEOUT.
- **Left-shift gate:** a checklist entry: a timeout criterion asserts that the timeout actually fired before it reads any effect of the kill.

### M9. 86 S25 rebuilds a heredoc slicer the repo already has (id 18)

- **Where:** 86 §2 S25; §4 Files touched; §10.
- **What is wrong:** S25 has the builder write a new slicer. The repo already has `extract_heredoc_body` (tools/gate-lint/sh_hygiene.py:274), which fixed an early-terminator bug from `.strip()` and a CRLF terminator bug, and a fence reader, `unfenced_lines` (tools/memory-tree/tree_lib.py:149). §10's "no item mints a second implementation" is false for this item.
- **Consequence:** A rebuilt slicer can cut a body short, which hides a free name below the cut. That is the missing-`import` class AC21 exists to catch, so AC21 would stay green.
- **Fix (skeptic: sound):** Name and reuse `extract_heredoc_body` through a `python -I` call with sys.path set to tools/gate-lint. Use tree_lib's fence reader (or the parity loop's `blk()`) for the runbook's fenced block. If neither fits, record why in §10. Stage a heredoc host with an indented line that matches the tag and a CRLF terminator, and show that the slice still reaches a free name after that line.
- **Left-shift gate:** the reuse lens's codebase-map symbol lookup runs over every "slice", "extract" or "parse" verb in a spec's §2 before the spec is promoted.

### M10. 86 AC23 reads none of codebase-map's real version carriers (id 21)

- **Where:** 86 §2 S28; §6 AC23.
- **What is wrong:** The `gov:kit codebase-map@` grep matches only the comment beside the constant at tools/codebase-map/map_lib.py:47. The real carriers, memory/map/generated/{CARDS.md,MAP.md,inventories.json,symbols.json}, spell `codebase-map@1.30` with no `gov:kit` prefix and lie outside the pathspec.
- **Consequence:** AC23 certifies "every carrier equals its constant" without reading any carrier. The freshness leg still catches a stale artifact, so the effect is contained.
- **Fix (skeptic: sound):** Grep `codebase-map@[0-9][0-9.]*[0-9]` over `tools memory/map/generated` and require one distinct value equal to the constant. Stage the red by moving only the constant in a scratch clone.
- **Left-shift gate:** derive each kit's carrier set from govkit's `derive_marker_basis`, never from a hand-typed grep.

### M11. 86 S27's carrier selector takes in test fixtures and bypasses the carrier writer (id 22)

- **Where:** 86 §2 S27; §4 Evidence and Files touched.
- **What is wrong:** The unexcluded `git grep -l 'gov:kit memory-tree@'` lists 14 files, including fixtures in check-verdict-epoch.test.sh:118 and check-memory-hygiene.test.sh. Files touched lists 12. S27 never names `govkit.py selfcheck --fix` (`write_version_carriers`), whose basis already excludes `*.test.sh`.
- **Consequence:** Followed literally, S27 rewrites the decoy fixture and hollows out the "constant LINE without its VALUE" arm. A hand move instead bypasses the writer that check 5c grades against.
- **Fix (skeptic: sound):** Move the carriers with `python tools/govkit/govkit.py selfcheck --fix` and then the kit's `[[regenerate]]` `--render`. Define the population as `derive_marker_basis`, and add `':!*.test.sh'` to S27's grep so it matches Files touched.
- **Related:** L9 (id 37) is the same selector mismatch at a low binding grade.
- **Left-shift gate:** same as M10. Carrier populations come from `derive_marker_basis`.

### M12. 83's alias token search matches globs inside plain scalars (id 24)

- **Where:** 83 §2 S1, §4 Alternatives rejected and §5 risks, carried into 84 S2.
- **What is wrong:** S1 searches the whole value text for `*<name>`, plain scalars included, without saying where an alias may start. A glob such as `cp build/*.jar out` or `vendor/*.so` matches the search.
- **Consequence:** Any GitLab file with an unquoted glob in `default:`, global scripts or `cache:` has every job falsely refused as `opaque step alias`. The refusal fails safe, so the effect is contained.
- **Fix (skeptic: sound):** Define the alias token as YAML does: a `*` that opens a node, at the value's start or right after `[`, `{`, `,` or `- `. Plant `default: { before_script: [cp build/*.jar out] }` and, in 84, a top-level `cache: { paths: [vendor/*.so] }`, both graded `importable`.
- **Left-shift gate:** a checklist entry: every token search over YAML text carries a negative plant of the same characters in a scalar.

### M13. 81 claims refusals as observed with no plant behind them (id 28)

- **Where:** 81 §2 S2 to S4; §6 AC3.
- **What is wrong:** S2's "first key otherwise" branch has no plant. S3 says the pre-82 `- template:` refusal is "Observed by AC3", but AC3 exempts first key `template`, and 81 plants no template item.
- **Consequence:** In the 81-before-82 order, which the Rollout allows, a template item graded `importable` turns no criterion red.
- **Fix (skeptic: sound):** Plant `- foo: bar` with an AC requiring `refused: unreadable variables item foo`. Plant `- template: vars.yml` with an AC requiring `refused: unreadable variables item template` or 82's reason, never `importable`. Re-point S3's "Observed by" to that AC.
- **Related:** this is the same gap as H1 (id 1), seen through the observed-by claim. The one set of plants closes both.
- **Left-shift gate:** a spec-lint rule that each "Observed by ACn" names an ACn whose plant exhibits the claimed shape and is not exempted by that ACn's own text.

### M14. 86 S14 to S16 give no verdict when `/proc` exists but `/proc/<pid>/exe` is unreadable (id 35)

- **Where:** 86 §2 S14 to S16.
- **What is wrong:** S15's `ps` arm runs only where `/proc` is absent. S16's `cannot look` covers only no `/proc` with no runnable `ps`, or `ps` failing. A zombie, a reaped pid (ENOENT) or a denied readlink (EACCES) has no verdict.
- **Consequence:** `realpath` returns the unresolved path, which compares unequal and reads `grandchild not visible`, the misreading S16 exists to stop. Alternatively, an `OSError` escapes the pure function AC14 and AC15 call.
- **Fix (skeptic: sound):** State that an `OSError` on `/proc/<pid>/exe` falls back to S15's `ps` arm, and that a vanished pid or a failed arm returns `cannot look`. Add AC14 literal cases for exe absent with `comm` present, and for both absent.
- **Left-shift gate:** a checklist entry: every OS probe names its verdict for each errno its primary read can raise.

### M15. 86 AC19 waits on a clock instead of a rendezvous (id 36)

- **Where:** 86 §2 S22; §6 AC19.
- **What is wrong:** The arm uses fixed sleeps (a 3 s grandchild, a 1 s bound, a check 4 s later). Nothing confirms the grandchild started before the bound fired, though 80 S13 already uses a started-pidfile pattern for this.
- **Consequence:** On a loaded Windows/MSYS host the `proc.kill()` arm can go red for timing alone, and a grandchild that never starts passes the `run_tree_kill` arm vacuously.
- **Fix (skeptic: sound):** Have the grandchild write a `started` marker before it sleeps. Wait for that marker before the bound, failing with `harness: grandchild never started` if it never appears. Then poll for the `done` marker over a bounded window instead of a fixed 4 s.
- **Left-shift gate:** extend the rendezvous invariant (TOOL-cSteadyMetronome-1) into a checklist entry that covers every process-timing criterion, not only the run-gates canary.

## Low

### L1. 84 AC3 `<child>` spelling, at the skeptic's low grade (id 4)

- **Where:** 84 §2 S2; §6 AC3.
- **What is wrong:** This is the same conflict as M7: AC3 expects `workflow:variables`, while 76 S2's direct-child reading, which 83 S2 borrows, gives `workflow:rules`.
- **Consequence:** Under one reading AC3 fails on a correct build. The skeptic graded it low because only the key named in the reason string is affected, and AC3 forces one spelling at build time. This review keeps the binding grade. The same defect stands at medium under M7.
- **Fix (skeptic: sound):** Define `<child>` for a token two or more levels below the block, either as the deepest key on the token's line or as the direct child (with AC3 changed to `workflow:rules`). Plant a depth-2 `default:` case.
- **Left-shift gate:** as M7.

### L2. 81 (and 82) add a user-visible refusal with no help page line (ids 7, 25)

- **Where:** 81 §5 user docs and §4 Files touched; 82 §5 user docs.
- **What is wrong:** 81 adds `refused: unreadable variables item <form>`, which fires on a conditional item whether or not it holds a credential, and 82 adds `unreadable credentials template <path>`. Both say no `help/adopt.md` line is needed and lean on 79 S5's sentence, which covers credentials only. 86 S3 and AC4 grade exactly this as a defect for 78's refusal.
- **Consequence:** An adopter refused this way finds no page sentence explaining why. The charter's docs rule is missed. Census behaviour is unchanged.
- **Fix (skeptic: sound, both findings):** Add `help/adopt.md` to 81's Files touched, with one sentence naming the closed item set (`name`, `group`, `template`, plain mapping keys) and the refusal. Add a criterion that greps the page for `unreadable variables item`: present at the tip and absent at pass start, as 86 AC4 does. Have 82 do the same for `template <path>`, or have 81's sentence name it.
- **Note:** both findings were graded medium by their finders. The skeptic re-graded both low because only the page is missing.
- **Left-shift gate:** a hygiene check that every `refused: <reason>` string introduced in a spec's §2 appears in help/adopt.md, or in a §5 line naming the page sentence that covers it.

### L3. Half of 86 AC26 is green before the build (id 9)

- **Where:** 86 §6 AC26 (second half).
- **What is wrong:** `grep -c 'census refuse a ci'` over this spec's own §10 reads authored text that the build pass never writes.
- **Consequence:** That half can never fail. Only the ledger half carries signal.
- **Fix (skeptic: sound):** Drop the spec-text half, or move it to the ledger: no `query.py` line in the acceptance ledger may carry the CI-census query string.
- **Left-shift gate:** a spec-lint rule that a criterion's probe reads no file in its own spec's directory.

### L4. 81 and 82 land at 80's "last unit" order, and 82's arm leaves AC4 uncovered (id 11)

- **Where:** 82 §4 Rollout and §7 Gates; 81 §4 Rollout.
- **What is wrong:** 81 and 82 share order 32 with 80, which claims to build "after every unit" and re-renders the map. 81 and 82 then add functions to adopt_program.py after that re-render. 82 §7 also covers AC1 to AC3 but not AC4.
- **Consequence:** The map stays stale until 86's order-33 re-render, and 80's claim is false. AC4 is tied to no arm.
- **Fix (skeptic: sound):** In the 81 and 82 Rollouts, say that 86's order-33 re-render covers their new functions, or move both to order 33 ahead of 86. Add AC4 to 82's `covers` list.
- **Left-shift gate:** a hygiene check that flags any unit sharing the order of a unit whose text claims to be last, and any AC missing from every arm's `covers` list.

### L5. 84 consumes 83 at the same order (id 12)

- **Where:** 84 §4 Rollout; §3 Edges.
- **What is wrong:** 84 consumes from 83, yet both are order 25. check-memory-hygiene.sh:2813 tests consumes-from with a strict `>`, so equal orders pass. The required order lives only in Rollout prose.
- **Consequence:** A run can take 84 first, and 84's AC1 then needs 83's unbuilt whole-line read.
- **Fix (skeptic: sound):** Set 84 to order 26, or state the 83 → 84 sequence where the run reads step 25.
- **Left-shift gate:** change the consumes-from test at check-memory-hygiene.sh:2813 to `>=`, so a consumer must sit strictly after the unit it consumes.

### L6. 86 S20's Readers census is wrong in both directions (ids 16, 26)

- **Where:** 86 §2 S20, Readers line.
- **What is wrong:** `git grep -l 'lists no file under \`memory/\`'` prints the 75 spec-audit review, 86 itself and the build record 2026-10-27-build-TOOL-dLinkedLibrary-86-promoted-fix-return.md. The line omits that record. It also lists 80.md, which the grep misses because 80 AC1 wraps the phrase across :256-257.
- **Consequence:** A later change that trusts the list misses a reader, and the stated grep does not find 80 AC1's text.
- **Fix (skeptic: sound, both findings):** State the grep used, list every file it prints (the fix-return record included), and say that 80 AC1 carries the phrase wrapped across :256-257.
- **Left-shift gate:** a hygiene check that re-runs each Readers line's stated grep and compares the file set.

### L7. Stale line citations into sibling specs (id 17)

- **Where:** 84 §4 Evidence, plus 83 §4, 81 §4 and 86 §4.
- **What is wrong:** Several cites moved after the hands-off folds:

  | Cited in | Cites | Should be |
  |---|---|---|
  | 84 | 79.md:42 (the GitHub row, not GitLab) | 79.md:43 |
  | 83, 84 | 76.md:24-25 | 76.md:25-26 |
  | 86 | 76 AC2 at :121-123 | 76.md:125-127 |
  | 86 | 77 AC1 at :120-123 | 77.md:123-126 |
  | 81 | 79 S2 at :46-53 | 79.md:47-54 |

- **Consequence:** A reader who follows a cite lands on the wrong row or criterion. Behaviour does not change.
- **Fix (skeptic: sound):** Re-point each cite as in the table, or cite by section and criterion id instead of line number.
- **Left-shift gate:** a hygiene check that resolves `<spec>.md:<n>` cites and flags any whose target line does not carry the cited section or criterion id.

### L8. 84 names 76 as the file-wide refusal seam instead of 71 (id 19)

- **Where:** 84 §2 S2 and §10; the matching sentence in 83 S2.
- **What is wrong:** 84 routes hits "through 76 S2's file-wide path". The refusal itself is 71 S2's; 76 S2 only restates it for `default:`, and 86 S7 merges the loops only at order 33.
- **Consequence:** At order 25 a builder may extend a duplicate loop, which costs rework until 86 AC6 catches it.
- **Fix (skeptic: sound):** Have 84 S2, 84 §10 and 83 S2 name 71 S2's one file-wide function, with only the reason text supplied by the caller (86 S7's wording).
- **Left-shift gate:** the reuse lens checks that each §10 seam names the unit that first defines the function, not a unit that restates it.

### L9. 86 S27's selector disagrees with S28 and Files touched (id 37)

- **Where:** 86 §2 S27 against S28.
- **What is wrong:** S28 excludes `*.test.sh`, but S27's selector does not. It prints 14 files, including fixtures (check-verdict-epoch.test.sh:118, and check-memory-hygiene.test.sh at :3454, :3506 and :3563) and files that only mention the prefix (check-kit-versions.sh, adopt-memory-tree.sh, kit.toml).
- **Consequence:** A literal reading misleads the builder. AC23 excludes the fixtures, so no graded behaviour changes.
- **Fix (skeptic: sound):** Give S27's selector `':!*.test.sh'`, and define a carrier as a file holding `gov:kit memory-tree@<version>`, not the bare prefix.
- **Related:** this is the same mismatch as M11 (id 22), which stands at medium.
- **Left-shift gate:** as M10.

review-shape kind=spec-audit round=1 intensity=full at=synth raw=37 confirmed=34 refuted=3 unverified=0 blocker=0 high=4 medium=19 low=11 agents=11 out-tokens=203871
## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes |
|---|---|---|---|---|---|---|---|---|
| 1 | coherence | memory/builds/dLinkedLibrary/spec/2026-10-27-spec-TOOL-dLinkedLibrary-81.md:section 2 S2, S3 and S4; section 6 AC3 | high | high | confirmed | I read 81 at lines 52-60. S4 plants only a `- ${{ if }}` list item, a `${{ if }}` mapping key, a `- ${{ each }}` stage item and a `- name:` control. Nothing plants an item that opens with an unknown plain key (`- foo:`), a scalar `variables: ${{ ... }}` value, or a `- template:` item. S3 says 'Observed by AC3', but AC3 (lines 134-137) plants no template. Its 'unknown form' clause is satisfied only by the `${{`-led items, so a reader that catches `${{` alone passes AC1 to AC3. `git ls-files \| grep adopt_program` printed nothing, so no other plant exists in the tree. The deny-by-default rule that §1 says the unit exists for therefore ships with no plant behind it. | sound | fixture-passes-by-finding-nothing |
| 2 | coherence | memory/builds/dLinkedLibrary/spec/2026-10-27-spec-TOOL-dLinkedLibrary-81.md:section 2 S4 (trees 1 and 2); section 6 AC1 | medium | medium | confirmed | 81 S4 (lines 54-57) nests `- group: release-vars` under the `${{ if }}` item and `NUGET_API_KEY: $(nugetKey)` under the `${{ if }}` key. 79 S2 reads `- group: <name>` 'at any level S1 names or on the job', and its credential test matches the word `key`, ignoring case. 79 does not limit the read to the block's top-level items, so a line-based 79 reader can hit the nested lines. 81 §1 claims the reader 'never reaches' them, but that is 81's account, not 79's text. A grep for precedence, 'first hit' or 'one reason' over 51, 63, 74 and 79 printed nothing, so no spec says which reason wins. AC1 demands the exact string `refused: unreadable variables item expression`, so a correct 79 reader can turn it red. | sound | - |
| 3 | coherence | memory/builds/dLinkedLibrary/spec/2026-10-27-spec-TOOL-dLinkedLibrary-84.md:section 2 S1 and S2; section 6 AC1, AC3 and AC4 | medium | medium | confirmed | I read 84. S1 (lines 38-41) names eight blocks. The S5 plants test indirection only for `variables: *creds` and the `workflow:` `rules:` `!reference`. The `before_script: [npm publish]` plant tests S3's script read, not the token test, and `image: node:20` is the token-free control. AC4 names rows `variables`, `workflow`, `image` and `before_script` only. 86 S9 adds just an `after_script: !reference` plant. `services:`, `cache:` and an indirection in `image:` or `before_script:` have none, so a walk hardcoded to two or three blocks passes every criterion. | sound | - |
| 4 | coherence | memory/builds/dLinkedLibrary/spec/2026-10-27-spec-TOOL-dLinkedLibrary-84.md:section 2 S2; section 6 AC3 | medium | low | confirmed | 76 S2 defines `<child>` as 'the key of `default:` that holds it', which for a deep token is the block's immediate child. 83 S2 opens with 'the key that holds the token' but then says 'a block key below `default:` as 76 S2 states'. 84 S2 borrows 83's `<child>`. For `workflow:` -> `rules:` -> `- variables: !reference`, the immediate-child reading gives `workflow:rules`, while AC3 (84:140-141) demands `workflow:variables`. Every 76 plant has its token one level down, so the plants cannot tell the two readings apart. The effect is limited to which key the reason string names, and AC3 will force one spelling at build time, so I grade it low. | sound | - |
| 5 | coherence | memory/builds/dLinkedLibrary/spec/2026-10-27-spec-TOOL-dLinkedLibrary-85.md:section 2 S2 and S4 (third plant); section 6 AC3 | medium | medium | confirmed | 85 S4 (lines 46-49) puts the follow-on step `      - run: echo done` at column 6, the dash's own column, and the key `run` starts at column 8. 73 S2's dash-measured extent holds only lines 'indented deeper than the dash', so it also ends at that step. AC3's 'Red when: the block's extent is measured from the dash' therefore cannot fire. S2's key-column rule, the reason for this unit, is not discriminated by any criterion. | sound | fixture-passes-by-finding-nothing |
| 6 | coherence | memory/builds/dLinkedLibrary/spec/2026-10-27-spec-TOOL-dLinkedLibrary-83.md:section 2 S1 and S4; section 6 AC1-AC4 | medium | medium | confirmed | 83 S1 (lines 36-41) reads a flow collection 'to its closing bracket, across lines where the flow collection continues', and §5 (lines 115-116) reads an unclosed one to the end of the file. All four S4 plants (lines 50-55) are one-line `default:` values, and AC1 to AC4 grade only those. A reader confined to the `default:` line's own text passes every criterion. A `default: {` whose `!reference` sits on the next line would still pass. | sound | - |
| 7 | coherence | memory/builds/dLinkedLibrary/spec/2026-10-27-spec-TOOL-dLinkedLibrary-81.md:section 5 user docs (and 82 section 5 user docs) | medium | low | confirmed | 81 §5 (lines 122-123) says no `help/` line is needed and leans on 79 S5's sentence. That sentence names only credentials in `variables:` blocks, not a refusal for an unreadable item form. The build's convention is to name each census refusal on the page: 76 S5, 79 S5, 80 S30 for each key 71 refuses, and 86 S3/AC4, which grades 'the refusal ships with no line on the page' as red. 81's new `unreadable variables item <form>` reason has no page line. 82's template reason is a credential refusal, which 79 S5's sentence arguably covers. The gap is documentation only, with no effect on what the census does, so I grade it low. | sound | two-answers-to-one-question |
| 8 | coherence | memory/builds/dLinkedLibrary/spec/2026-10-27-spec-TOOL-dLinkedLibrary-86.md:section 2 S7; section 6 AC6 | medium | medium | confirmed | 86 S7 (lines 60-62) has the one file-wide function receive 'only the reason text' from its caller. AC6 (lines 286-289) greps `opaque step`, which prints only lines that spell the reason text. The definition holds no such text by S7's own terms, so it need not print. A second loop that builds the reason on one line and assigns it to each job on another prints the same kind of reason-construction line as a legitimate caller. The grep therefore cannot show AC6's own 'Red when' case of a second loop over a file's jobs. | sound | rule-stated-with-no-check-that-fails |
| 9 | coherence | memory/builds/dLinkedLibrary/spec/2026-10-27-spec-TOOL-dLinkedLibrary-86.md:section 6 AC26 (second half) | low | low | confirmed | I checked that 86.md matches its pinned blob 6dae38f. In it, AC26 (lines 371-373) greps for 'census refuse a ci' in this spec's own §10, cut with sed from '^## 10' to the end. Running that cut and grep on today's tree gives 0, and the §10 text is authored here, not written by the build pass. That half is green before the unit is built, so only the ledger half of AC26 can detect anything. | sound | - |
| 10 | coherence | memory/builds/dLinkedLibrary/spec/2026-10-27-spec-TOOL-dLinkedLibrary-81.md:section 2 S1 | low | - | refuted | The premise is false when 79 S2 is re-read. Lines 46-49 of 79.md do more than say '- name: <NAME>' names its variable. They also say a credential is a variable 'whose value references such a name in 63 S3's forms', which is the rule a list item's value: key falls under. So 81 S1's 'read as 79 S2 states' does lead a builder to a value-reference rule. The only key with no rule is readonly:, a boolean that holds no reference, so leaving it out has no effect on behaviour. | sound | - |
| 11 | coherence | memory/builds/dLinkedLibrary/spec/2026-10-27-spec-TOOL-dLinkedLibrary-82.md:section 4 Rollout; section 7 Gates (also 81 section 4 Rollout) | low | low | confirmed | The README build-order region (line 258) puts 80, 81 and 82 all at step 32. 80.md:30-31 still says it builds 'after every unit of the build (order 32)', and its S7 re-renders the map. The Rollouts of 81 and 82 (lines 97-99 and 86-88) only order the two of them against each other and say nothing about the map. 86's Rollout (line 217-219) re-renders at order 33, so the staleness ends there, but neither 81 nor 82 says so. Separately, 82 §7 line 137 lists 'covers AC1 AC2 AC3', and AC4 (line 129) is observed by the same plant but missing from the list. | sound | - |
| 12 | coherence | memory/builds/dLinkedLibrary/spec/2026-10-27-spec-TOOL-dLinkedLibrary-84.md:section 4 Rollout; section 3 Edges | low | low | confirmed | check-memory-hygiene.sh:2813 tests consumes-from with a strict '>', so equal orders pass. TEMPLATE-SPEC.md:83-84 says 'Units sharing a value are the parallel group'. 84.md:71 consumes from 83, yet both are order 25 (README line 251). The required order appears only as Rollout prose at 84.md:103-105 ('its pass follows 83's'), and the order field contradicts it. Moving 84 to order 26 is safe: its only downstream edge is the hands-off to 86 at order 33, and only 86 consumes 84. | sound | - |
| 13 | grounding | memory/builds/dLinkedLibrary/spec/2026-10-27-spec-TOOL-dLinkedLibrary-86.md:section 2 S24-S25, section 4 Evidence (S24, S25), section 6 AC21 | high | medium | confirmed | 86 S25 (lines 140-142) names only two containers, a shell heredoc body and the runbook's fenced block. git grep for '^# >>> resolve_prefix_token' prints run-gates.sh:2740 and :4972 and run-gates.test.sh:631 and :669. All four sit in -c strings: run-gates.sh:2711 is legs=$("$PYBIN" -c "$RKD_PROGRAM"' with RKD_PROGRAM read from the <<'RKD' heredoc at :176-178; :4959 is paths=$("$PYBIN" -c '; and test.sh:629 is "$PYBIN" -c '. Inside the :2711 program, the literal calls resolve_kit_dir (pm_d = resolve_kit_dir(*sys.argv[5:8])), so slicing the literal alone would report a false unbound name. §4 grounds S25 only on check-wiring.sh's heredoc. I grade it medium, not high: built as written, AC21's own Red-when ('a Python copy hosted in a shell file sits outside the read') goes red, so the gap blocks the build rather than shipping a false pass. | sound | - |
| 14 | grounding | memory/builds/dLinkedLibrary/spec/2026-10-27-spec-TOOL-dLinkedLibrary-84.md:section 2 S2, section 6 AC3 | medium | medium | confirmed | 76.md:38-40 defines <child> as 'the key of default: that holds it', which is the direct child. 83.md:43-44 defers block keys to 76 S2. 84.md:45 takes <child> 'as 83 S2 defines it'. 84's plant at :55-56 nests the token at workflow: > rules: > item > variables:. Under the direct-child rule that reads workflow:rules, but AC3 (84.md:140-141) expects workflow:variables. None of 76, 83 or 86 S5 gives a nested example that would settle it otherwise. A builder cannot meet both S2 and AC3. | sound | - |
| 15 | grounding | memory/builds/dLinkedLibrary/spec/2026-10-27-spec-TOOL-dLinkedLibrary-86.md:section 2 S22, section 6 AC19 | medium | medium | confirmed | regen.py:297 calls proc.wait(timeout=bound) on the bash process only. I ran a scratch copy of regen.py's run_command with ['bash','-c','(sleep 3; echo x > m1) &'] under a 1 s bound. It returned status 0 in 0 s, and after sleeping 4 s the marker existed, with run_tree_kill unchanged. A plain reading of AC19 (86.md:339-342, 'backgrounded grandchild', no wait) therefore leaves the marker on a correct build and AC19 goes red. The behaviour that tells the two copies apart needs bash kept alive past the bound. | sound | - |
| 16 | grounding | memory/builds/dLinkedLibrary/spec/2026-10-27-spec-TOOL-dLinkedLibrary-86.md:section 2 S20 Readers | low | low | confirmed | git grep -l for the phrase 'lists no file under `memory/`' printed three files: build/2026-10-27-build-TOOL-dLinkedLibrary-86-promoted-fix-return.md, the 75 spec-audit review and 86.md itself. It did not print 80.md, because 80.md:256-257 breaks the phrase across a line ('it lists no file' / 'under `memory/`'). The S20 Readers line (86.md:119-121), which claims these are the only files the grep prints, is wrong in both directions: it omits the build record and lists 80.md, which that grep does not find. | sound | - |
| 17 | grounding | memory/builds/dLinkedLibrary/spec/2026-10-27-spec-TOOL-dLinkedLibrary-84.md:section 4 Evidence (also 83 §4, 81 §4, 86 §4 S1 and S4-S6) | low | low | confirmed | Re-probed every cite. 79.md:42 reads the GitHub row (`.github/workflows/*.yml` → workflow-level `env:`) and :43 the GitLab row, but 84.md:80 cites :42 as '79 S1's GitLab row'. 83.md:76 cites 76 §1 at `:24-25`, but the `default: {` example sits on 76.md:25-26. 86.md:198 cites 76 AC2 at `:121-123`, but 76.md:121 is AC1 and AC2 opens at :125. 86.md:192 cites 77 AC1 at `:120-123`, but AC1 opens at 77.md:123. 81.md:76 cites 79 S2 at `:46-53`, but S2 opens at 79.md:47. These are wrong citations only, so nothing in behaviour changes. | sound | - |
| 18 | reuse | memory/builds/dLinkedLibrary/spec/2026-10-27-spec-TOOL-dLinkedLibrary-86.md:section 2 S25, section 4 Files touched, section 10 | medium | medium | confirmed | 86.md:140-142 (S25) has the builder slice 'a shell heredoc's body or the runbook's fenced block' and names no existing extractor. 86.md:402-409 (§10) says 'no item mints a second implementation of any', and its seam list names no heredoc slicer. tools/gate-lint/sh_hygiene.py:274 does define `extract_heredoc_body`, and its docstring records the `.strip()` early-terminator bug and the CRLF `\r` tolerance it fixed. So the §10 claim is false for this item, and S25 invites a rebuilt slicer that could repeat those bugs. A slice cut short would hide a free name below the cut, which is the class AC21 exists to catch. | sound | - |
| 19 | reuse | memory/builds/dLinkedLibrary/spec/2026-10-27-spec-TOOL-dLinkedLibrary-84.md:section 2 S2, section 10 | low | low | confirmed | 84.md:43-45 says 'A hit refuses every job in the file through 76 S2's file-wide path', and 84 §10 names '76 S1's indirection test and S2's file-wide refusal' as the seam. The file-wide refusal itself is 71 S2 (71.md:38-40). 76 S2 (76.md:38-41) only restates it for `default:` and names no shared function. 86 S7 (86.md:60-62) later says each 84 hit routes through 71 S2's one function, but 86 is order 33 and 84 is order 25 (README rows 160 and 178). 84's own text therefore names the wrong seam for eight orders. 86 AC6 reconciles it later, so the cost is contained rework. | sound | - |
| 20 | reuse | memory/builds/dLinkedLibrary/spec/2026-10-27-spec-TOOL-dLinkedLibrary-86.md:section 7 New arm lines for decision_rubric.py and reuse_entries.py | low | - | refuted | The cited section already says it, and the premise of a contradiction does not hold. S18 (86.md:106-109) states the case is 'run by the build-index selftest arm unit 1 declares; the module gains no `--selftest` mode', so a builder is told outright not to mint a runner. Naming the module that holds the fixture case as the `New arm:` path is this build's established convention: across the dLinkedLibrary specs, `New arm: tools/memory-tree/decision_rubric.py` appears 4 times and `reuse_entries.py` 7 times. TEMPLATE-SPEC.md:283-288 says only the `covers` field is machine-read and the rest is prose. The line names where the plant lives and does not contradict S18. This is a preference, not a graded defect. | sound | - |
| 21 | blast-radius | memory/builds/dLinkedLibrary/spec/2026-10-27-spec-TOOL-dLinkedLibrary-86.md:section 2 S28, section 6 AC23 | medium | medium | confirmed | Re-ran the grep: `git grep -n -o -E 'gov:kit codebase-map@...' -- tools help memory/HYGIENE.md memory/TEMPLATE-SPEC.md memory/guides` printed only `tools/codebase-map/map_lib.py:47:gov:kit codebase-map@1.30`, the comment beside the constant. The real carriers, memory/map/generated/{CARDS.md,MAP.md,inventories.json,symbols.json}, spell `codebase-map@1.30` with no `gov:kit` prefix and sit outside the pathspec. So AC23's codebase-map half reads none of the kit's carriers. The effect is contained because the `codebase-map coverage + freshness` leg byte-compares those artifacts against a fresh render, so a stale one is still caught elsewhere. | sound | - |
| 22 | blast-radius | memory/builds/dLinkedLibrary/spec/2026-10-27-spec-TOOL-dLinkedLibrary-86.md:section 2 S27, section 4 Evidence and Files touched | medium | medium | confirmed | The unexcluded S27 grep lists 14 files, including tools/memory-tree/check-memory-hygiene.test.sh and check-verdict-epoch.test.sh. 86 Files touched lists 12 for S27, and only S28/AC23 add `':!*.test.sh'`. S27's own wording ('every carrier ... lists moves with it') takes in the test.sh fixtures. check-verdict-epoch.test.sh:115-120 seds `# gov:kit memory-tree@1.5` beside `commit_engine "$K" 1.5`, so rewriting that marker would hollow out the decoy arm. govkit.py:767-775 `derive_marker_basis` already excludes `*.test.sh` for exactly this reason. S27 never names `selfcheck --fix`/`write_version_carriers` (govkit.py:1830-1848), the writer that check 5c grades against. Suite failure would catch a mistake, so the harm is contained. | sound | - |
| 23 | blast-radius | memory/builds/dLinkedLibrary/spec/2026-10-27-spec-TOOL-dLinkedLibrary-84.md:section 2 S2, section 6 AC3 (against 83 S2) | medium | medium | confirmed | 83 S2 (83.md:42-46) defines block-style `<child>` as 'a block key below `default:` as 76 S2 states'. 76 S2 (76.md:38-41) says '`<child>` the key of `default:` that holds it', which reads as the direct child. 84 S2 takes `<child>` 'as 83 S2 defines it'. 84 AC3 (84.md:140-141) expects `workflow:variables` for a token under `workflow:` → `rules:` → `variables:`, where the direct-child reading gives `workflow:rules`. 83's flow-style rule ('nearest key before the token at the token's own flow depth') gives the innermost key, so the same nesting yields different reasons in block and flow style. The definition and the criterion conflict. | sound | - |
| 24 | blast-radius | memory/builds/dLinkedLibrary/spec/2026-10-27-spec-TOOL-dLinkedLibrary-83.md:section 2 S1, section 4 Alternatives rejected, section 5 risks (carried into 84 S2) | medium | medium | confirmed | 83 S1 (83.md:36-41) widens the test to 'on each line the whole value text: ... a plain scalar, and a flow mapping ... or flow sequence', and §4 (Alternatives) defends 'a token search over the value text'. Neither defines where an alias token may start. 84 S1-S3 apply this to top-level `before_script:`/`after_script:`/`cache:`, where unquoted globs like `cp build/*.jar out` are common, and `*.jar` matches `*<name>` under a plain text search. 83 §5's risks name only the quoted-string case, and no plant in 83 S4 or 84 covers a glob. `git ls-files tools/memory-tree/adopt_program.py` printed nothing, so no code yet constrains it. The result would be false file-wide refusals. These fail safe, and the owner can rule a job in, so the effect is contained. | sound | - |
| 25 | blast-radius | memory/builds/dLinkedLibrary/spec/2026-10-27-spec-TOOL-dLinkedLibrary-81.md:section 5 user docs, section 4 Files touched | medium | low | confirmed | 81 S2 (:41-47) adds the new reason `refused: unreadable variables item <form>`, and 81 §5 (:122-123) says 'user docs — none under `help/`'. `git grep -n 'unreadable variables item'` matches only 81's own lines. 79 S5 (:67-69) only covers credentials in the named blocks, and an `${{ if }}` item holding a non-credential is refused anyway. The spec set treats this as a defect elsewhere: 78 §5 also said 'none under help/', and 86 S3 (id 29, M15) adds a page sentence for 78's refusal. help/adopt.md does not exist at this tip (`ls help` lists no adopt.md); 79 writes it before 81's pass. Graded low: only the page is missing, and the refusal behaves the same. | sound | - |
| 26 | blast-radius | memory/builds/dLinkedLibrary/spec/2026-10-27-spec-TOOL-dLinkedLibrary-86.md:section 2 S20 Readers | low | low | confirmed | I re-ran `git grep -l 'lists no file under \`memory/\`'`. It printed the 86-promoted-fix-return build record, the round-5 review (75-spec-audit) and the 86 spec. It did not print 80's spec: 80.md:256-257 splits the phrase across two lines ('it lists no file' / 'under `memory/`'). 86 S20's Readers line says 80 and the audit are the only other files the grep prints, so that line is wrong. | sound | - |
| 27 | failure-envelope | memory/builds/dLinkedLibrary/spec/2026-10-27-spec-TOOL-dLinkedLibrary-81.md:section 2 S1 and S2 | high | high | confirmed | 81 S1 (:36-40) reads only two shapes: a block list whose items open with `- name:`, `- group:` or `- template:`, and a block mapping. S2 (:41-47) lists what refuses: a list item opening with another key or `${{`, a mapping key opening `${{`, and a scalar value. A flow value such as `variables: [ { group: x } ]` or `{ NUGET_API_KEY: $(k) }` is not a scalar, a block item or a block key. A `- { group: x }` item has no first key for `<form>`. `grep -i flow` over 79/81/82 finds no flow rule. Flow reading exists only in 83 S1, for GitLab `default:`. The S2 heading says 'Every other form refuses', but the triggers it lists do not reach flow style, so a builder can grade a job with a flow-style variable group `importable`. The consequence is a wrong security result on a narrow path, which grades high. | sound | - |
| 28 | failure-envelope | memory/builds/dLinkedLibrary/spec/2026-10-27-spec-TOOL-dLinkedLibrary-81.md:section 2 S2-S4 / section 6 AC3 | medium | medium | confirmed | 81 S4 (:52-60) plants three trees whose unknown item opens `${{` and one tree with a plain `- name:` item. No plant has a non-expression unknown key such as `- foo:`, so S2's 'item's first key otherwise' branch is never observed. S3 (:48-51) says the `- template:` fallback is 'Observed by AC3', but AC3 (:134-136) only covers items whose first key is not `name`, `group` or `template`, and 81 plants no template item. The Rollout (:99) says neither unit reads the other's plant, so in the 81-before-82 order a template item graded `importable` turns no criterion red. | sound | observed-by-claim-no-arm-discharges |
| 29 | failure-envelope | memory/builds/dLinkedLibrary/spec/2026-10-27-spec-TOOL-dLinkedLibrary-83.md:section 2 S1 and S4 / section 5 error states | medium | medium | confirmed | 83 S1 (:36-41) reads a flow collection 'across lines where the flow collection continues'. §5 (:115-116) says an unclosed flow collection is read to the end of the file. Both are claimed as observed by AC1 to AC4, but the four S4 plants (:50-55) are all one-line `default:` values: `*base`, `!reference [.defaults]`, the one-line flow mapping and `{ image: node:20 }`. A staged break that drops the continuation read leaves AC1 to AC4 green. Indented continuation lines may still be caught by 76's below-the-line walk, but the claimed observation does not exist. The effect is contained, so medium. | sound | observed-by-claim-no-arm-discharges |
| 30 | failure-envelope | memory/builds/dLinkedLibrary/spec/2026-10-27-spec-TOOL-dLinkedLibrary-84.md:section 2 S1 (the class) / section 4 Evidence | high | high | confirmed | 84 S1 (:38-41) lists the class 'every top-level block that reaches every job' as default/variables/workflow/image/services/cache/before_script/after_script, and §4 Evidence (:84-87) cites only the global keywords. My grep for `inputs` or `$[[` over the census specs finds nothing; the only `inputs` hit is in unit 25, which has nothing to do with the census. A root `.gitlab-ci.yml` header `spec: inputs:` with a default interpolated through `$[[ inputs.x ]]` reaches a job's script. No refusal substring, indirection token or credential name appears in the job text, so no stated rule refuses the job. The census already misses plain `$VAR` substitution as well. Still, 84 claims to close the class and leaves this member out, which gives a wrong importable grade on a narrow path: high. | sound | - |
| 31 | failure-envelope | memory/builds/dLinkedLibrary/spec/2026-10-27-spec-TOOL-dLinkedLibrary-84.md:section 2 S2 vs section 6 AC3 | medium | - | refuted | The premise does not hold when re-read. 83 S2 (:42-46) defines `<child>` as 'the key that holds the token'. For a block it adds 'a block key below `default:`', which means below, not directly under. In flow context it is 'the nearest key before the token'. 86 S5 likewise reads 76's `<child>` as the key holding the token. For `workflow: rules: - variables: !reference [...]`, the key holding the token is `variables`, so 84 S2's 'as 83 S2 defines it' gives `workflow:variables`, exactly what AC3 (:140-141) expects. 76 S2's 'the key of `default:` that holds it' only had depth-one plants, and 83 S2 states the reading the later specs use. S2 and AC3 do not conflict. | unsound | - |
| 32 | failure-envelope | memory/builds/dLinkedLibrary/spec/2026-10-27-spec-TOOL-dLinkedLibrary-84.md:section 2 S5 / section 6 | low | medium | confirmed | 84 S1 names eight blocks, seven besides `default:`. The S5 plants (:52-57) carry an indirection token only in `variables: *creds` and in `workflow:` rules `!reference`. `before_script: [npm publish]` is a plain script line, and `image: node:20` holds no token. 86 S9 adds an `after_script: !reference` plant. `image:`, `services:` and `cache:` carry no token in any plant, so a builder who drops `services` or `cache` from the block list turns no AC red. The class claim goes unenforced for those members, which is a real but contained gap in a security check: medium. | sound | - |
| 33 | failure-envelope | memory/builds/dLinkedLibrary/spec/2026-10-27-spec-TOOL-dLinkedLibrary-86.md:section 2 S2 / section 6 AC2 | high | high | confirmed | The premise holds. 86 S2 (lines 47-49) normalises only the trailing CR. A grep for utf-8/BOM/FEFF/encoding/decode over the census specs (63, 70-79, 81-86) finds nothing except 70's conf-decode note and 86's §10 recall line about the conf reader (69/80). No census spec states how a CI file is decoded. tools/memory-tree/adopt_program.py does not exist at this tip, so no built code covers the case either. AC2 (lines 271-274) plants CRLF only in the GitLab and GitHub files and never in azure-pipelines.yml. If plain utf-8 decoding keeps a leading U+FEFF, a first line of `include:` (71 S2's file-wide refusal) or a global key (84) no longer matches its key, and jobs read importable. That is a wrong census verdict, but only on a narrow path: a BOM-led file whose first line is such a key. | sound | - |
| 34 | failure-envelope | memory/builds/dLinkedLibrary/spec/2026-10-27-spec-TOOL-dLinkedLibrary-86.md:section 2 S25 / section 6 AC21 | high | medium | confirmed | Re-probed. tools/run-gates/run-gates.sh:2711 opens `legs=$("$PYBIN" -c "$RKD_PROGRAM"'` and its block follows at about 2740. Line 4959 opens `"$PYBIN" -c '` and holds a resolve_prefix_token block. run-gates.test.sh has two more `-c '` openers holding resolve_prefix_token blocks (around 631/669). All four sit in hosts the parity loop at tools/lib/resolve-python.test.sh:221-241 reads ('*.sh' etc.). 86 S25 (lines 140-142) names only two slicing shapes, a heredoc body and the runbook's fenced block, so the rule leaves these hosts unspecified even though AC21 reaches every S24 host. The effect is limited to a lint arm over four copies, so medium rather than high. The false-unbound half is weaker than the finding says: 80 S11 counts only names the block references, and that resolve_prefix_token block may not use RKD_PROGRAM's bindings. | sound | - |
| 35 | failure-envelope | memory/builds/dLinkedLibrary/spec/2026-10-27-spec-TOOL-dLinkedLibrary-86.md:section 2 S14-S16 | medium | medium | confirmed | 86 S14 (lines 92-95) compares the realpath of /proc/<pid>/exe wherever /proc exists. S15 runs ps only 'where /proc is absent', and S16 (lines 100-102) covers only no /proc and no runnable ps, or ps exiting non-zero. Nothing says what happens when /proc exists but the exe readlink fails. 80 S12 decides liveness with os.kill(pid, 0) first, and that succeeds on a zombie whose exe link is unreadable. os.path.realpath of the unreadable link returns the path unchanged, which compares unequal and reads 'grandchild not visible'. AC14/AC15 (lines 318-326) have no case where exe is absent and comm is present. The effect is a wrong or confusing harness verdict on an edge path, which is contained. | sound | - |
| 36 | failure-envelope | memory/builds/dLinkedLibrary/spec/2026-10-27-spec-TOOL-dLinkedLibrary-86.md:section 2 S22 / section 6 AC19 | medium | medium | confirmed | 86 S22 (lines 127-130) and AC19 (lines 339-344) read only whether a marker exists, with fixed sleeps (3 s, a 1 s bound, a check 4 s later). Nothing confirms the grandchild was spawned before the bound fired. 80 S13 already uses that pattern (a pidfile poll that fails 'harness: grandchild never started'), and AC19 lacks it. If bash is slow to background the grandchild under load, the proc.kill() arm leaves no marker and goes red on timing alone. A start failure in the run_tree_kill run alone would pass that arm vacuously. The BY DESIGN rendezvous invariant covers only the run-gates canary, not this criterion, so it does not refute the finding. The effect is a flaky or vacuous criterion, which is contained. | sound | - |
| 37 | failure-envelope | memory/builds/dLinkedLibrary/spec/2026-10-27-spec-TOOL-dLinkedLibrary-86.md:section 2 S27 vs S28 | low | low | confirmed | Re-ran S27's selector `git grep -l 'gov:kit memory-tree@' -- tools help memory/HYGIENE.md memory/TEMPLATE-SPEC.md memory/guides`. It printed 14 files, including check-memory-hygiene.test.sh (fixture `memory-tree@0` at :3454, :3506, :3563) and check-verdict-epoch.test.sh (`memory-tree@1.5` at :118). S27 (lines 146-150) has no ':!*.test.sh' exclusion, while S28/AC23 do. The selector also prints check-kit-versions.sh:275, adopt-memory-tree.sh and kit.toml, which only mention the prefix and hold no version. Files touched lists 12 non-test files, so the spec and its selector disagree. AC23 excludes the fixtures, so the criterion itself is unaffected. The mismatch would mislead a literal reading but changes no graded behaviour. | sound | amendment-leaves-its-other-half-standing |
