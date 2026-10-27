**Serves:** spec-audit TOOL-dLinkedLibrary-54@rev-1 TOOL-dLinkedLibrary-55@rev-1 TOOL-dLinkedLibrary-56@rev-1 TOOL-dLinkedLibrary-62@rev-1 TOOL-dLinkedLibrary-61@rev-1 TOOL-dLinkedLibrary-60@rev-1 TOOL-dLinkedLibrary-63@rev-1 TOOL-dLinkedLibrary-57@rev-1 TOOL-dLinkedLibrary-58@rev-1 TOOL-dLinkedLibrary-59@rev-1 TOOL-dLinkedLibrary-64@rev-1

# Tier-2 spec audit: dLinkedLibrary, the round-2 promotions (units 54 to 64), round 1

Provenance: an adversarial review with five finder lenses (gov-spec-reviewer) and five skeptic batches (gov-skeptic), synthesized by gov-synthesizer on 2026-10-27.

Reviewed: memory/builds/dLinkedLibrary/spec/2026-10-27-spec-TOOL-dLinkedLibrary-54.md@60b090a8b4534ed2d765256b02556c706ddfa7dc, memory/builds/dLinkedLibrary/spec/2026-10-27-spec-TOOL-dLinkedLibrary-55.md@51e47d7e22e91099906371bdc79a4016a57027fc, memory/builds/dLinkedLibrary/spec/2026-10-27-spec-TOOL-dLinkedLibrary-56.md@81b9a69717b2266594794a805a8ce2c297a2f6a2, memory/builds/dLinkedLibrary/spec/2026-10-27-spec-TOOL-dLinkedLibrary-62.md@7b55f45148c3c9ae35d47b6ae46a9b719c1518a6, memory/builds/dLinkedLibrary/spec/2026-10-27-spec-TOOL-dLinkedLibrary-61.md@a34bbeb0756f974c2b1eb4864d3b992ebf9d483d, memory/builds/dLinkedLibrary/spec/2026-10-27-spec-TOOL-dLinkedLibrary-60.md@7d4a4c661aed24bd852544fdcfc52cf9c1cac52a, memory/builds/dLinkedLibrary/spec/2026-10-27-spec-TOOL-dLinkedLibrary-63.md@37214666d38d6a5c0825247910b351421c4729fe, memory/builds/dLinkedLibrary/spec/2026-10-27-spec-TOOL-dLinkedLibrary-57.md@054fc8b269262ec7427c8d6e854c62f521a9a3aa, memory/builds/dLinkedLibrary/spec/2026-10-27-spec-TOOL-dLinkedLibrary-58.md@e1957ad09f0fb80495bcbd90cf043a98bec44478, memory/builds/dLinkedLibrary/spec/2026-10-27-spec-TOOL-dLinkedLibrary-59.md@575830a16351445cbbd69947f83faa0ef7fd6272, memory/builds/dLinkedLibrary/spec/2026-10-27-spec-TOOL-dLinkedLibrary-64.md@c269c5a4ace8f0370edb4a485345222e2475512b
ROUND 1

## Verdict: BLOCKED

No blocker stands, but six high items do (nine raw high findings), and the owner's mandate (`2026-10-27-prompt-TOOL-dLinkedLibrary-1-owner-review-until-no-high.md`) has reviewing stop only once no HIGH is left.
By item, the tally is 0 blocker, 6 high, 16 medium and 10 low: 32 items.
By raw confirmed finding, the tally is 0 blocker, 9 high, 19 medium and 10 low: 38 findings.
Six items merge findings of one grade that describe one defect, and each lists all its ids: H1 (24, 33), H4 (19, 35), H5 (15, 40), M1 (1, 34), M2 (3, 23) and M3 (4, 38).
Four defects carry findings that the skeptics bound at different grades. Findings may only merge within one grade, so each of these defects appears as one item per grade, cross-referenced: H1 with M1 (the staged break), H2 with M4 (61's bare `bash`), H3 with M3 (59's row grammar), and M8 with L10 (57's before-image conf entry). For the fix, read each such pair as one defect at the higher grade.
No spec-62 finding was confirmed.

## Review shape

Intensity full, raw 46, confirmed 38, refuted 8, unverified 0 (0 uncertain), precision 0.83.

| lens | returned | raw | confirmed | refuted | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|
| coherence | yes | 7 | 7 | 0 | 0 | 0 | 1.00 |
| grounding | yes | 10 | 6 | 4 | 0 | 0 | 0.60 |
| reuse | yes | 6 | 4 | 2 | 0 | 0 | 0.67 |
| blast-radius | yes | 9 | 7 | 2 | 0 | 0 | 0.78 |
| failure-envelope | yes | 14 | 14 | 0 | 0 | 0 | 1.00 |

Seven of the eight refutations are duplicates of a confirmed finding (ids 8, 9, 10, 14, 20, 25, 27). The eighth, id 21, was refuted on a re-probe: `taskkill /T` does reach AC1's native-python grandchild.

## Run integrity

- Lenses: 5/5 returned, 0 died.
- Skeptic batches: 5/5 returned, 0 died.
- 0 contradictory verdicts demoted to unverified, 0 orphaned duplicate refutations demoted, 0 spurious verdicts discarded, 0 duplicates.
- Fixes on confirmed findings: 37 judged sound, 1 judged unsound (id 1), 0 none proposed, 0 not judged. The skeptic's corrected fix replaces the unsound one in M1.
- Severity: 0 ungraded, 8 re-graded by the skeptic (ids 1, 26, 34 and 38 high to medium; ids 7 and 43 low to medium; ids 28 and 36 medium to low). Each item states its binding grade.
- Unverified findings: none. 0 answered uncertain, 0 with no usable verdict.
- Lens notes: none were supplied, so every lens ran on the kit's generic brief.
- Roles: the finders were gov-spec-reviewer, the skeptic batches gov-skeptic, and the synthesis gov-synthesizer.
- Intent: 43 spec documents were supplied as `specs`, as sibling context.
- Checklist: 42 items, each assigned to exactly one of the 5 lenses: coherence 9, grounding 9, reuse 8, blast-radius 8, failure-envelope 8.
- By design: 1 invariant from the checklist's by-design block.
- Move check: no checked subject moved.

## High

### H1: The staged lib-source break never makes the micro-format gate fail, so the shipped arm is red on a correct gate [high] (ids 24, 33)

- **Where:** spec 55 §2 S2, §6 AC1 and §7 New arm; spec 54 §6 AC3. See M1 for the same defect at medium grade.
- **What:** The arm's failing case is a gate copy with `. "$(dirname "$0")/lib/region.sh"` inserted after `set -u`. The gate (`tools/check-microformats.sh:23`) runs `set -u` with no `set -e`, so a `.` of a missing file prints an error and the script carries on. The copy still carries its inline `region` and exits 0. Reproduced on the base gate: `No such file or directory`, then `microformats OK`, rc=0.
- **Consequence:** 55 S2's non-zero assertion fails on every correct gate. The `micro-format gate selftest` leg ships with the gate, so it is red at the close, in gov and in every default adopter. A builder chasing the red improvises a break the spec never priced, and the arm loses its claim to tell an isolated gate from one that sources `lib/`.
- **Fix (judged sound):** Stage the real defect, the shape unit 43 wrote: delete the copy's `# >>> region_sh` … `# <<< region_sh` block and put the single source line in its place. `region` is then undefined, `block=$(region …) || exit 2` fires, and the gate exits 2. Alternatively insert `. "$(dirname "$0")/lib/region.sh" || exit 2`. Assert exit 2 and that the output names the block. Reword 54 AC3, 55 S2 and 55 AC1 to this break. The build must run the arm against both copies and show it red on the stripped one and green on the inline one.
- **Left-shift gate:** a spec-audit rule that every staged break in an AC or arm carries an observed red at authoring time (the command and its non-zero exit recorded in the spec), so an unobserved break cannot be promoted.

### H2: 61's `observe-tree-hang` plant leads with a bare `bash`, which reaches WSL at its own pass [high] (id 2)

- **Where:** spec 61 §6 AC1 and §3 Non-goals, against spec 64 S6. See M4 for the same defect at medium grade.
- **What:** AC1's planted argv is `bash -c '...'`. On this node Popen resolves a bare `bash` to the System32 WSL launcher (`subprocess.run(['bash','-c','uname -s'])` printed `Linux`), which is why `regen.py:273-279` rewrites it. 61 defers that resolution to 64 S6, ordered at 29, while 61 runs at order 7.
- **Consequence:** At 61's own pass the grandchild runs inside WSL. Its pidfile holds a Linux pid, and the Windows-side liveness check is true whatever happens to it, so AC1 certifies a tree kill it never observed. On a node whose WSL holds no python, bash returns at once and the case reds on a correct build.
- **Fix (judged sound):** In 61 S2, have `--observe` resolve a leading `bash` through `resolve_bash` (`tools/memory-tree/corpus_ids.py:390`) and a leading python to `sys.executable`, landing at order 7. In the plant, run the grandchild as `sys.executable`, not a bare `python`. Retire 64 S6 and its AC5, or have them only re-observe. The build must run the `observe-tree-hang` case on a Windows node with WSL installed.
- **Left-shift gate:** a spec-tokens arm that reds any planted argv in a spec whose leading word is a bare `bash` or `python`.

### H3: Unit 59's log-diff classifier keys `rotated` on one row spelling and a literal archive name, bypassing the kit's row grammar [high] (id 18)

- **Where:** spec 59 §2 S1, §4 'The classification' and §10. See M3 for the same defect at medium grade.
- **What:** S1 and the §4 table write their own grammar: a rotated row is 'a row `<id> · …`', and the archive is the literal `memory/archive/DECISIONS.<date>.md`. At base, 72 of the log's 213 rows are bold-led (`- **ID** —` or `- **ID** -`). The archive literal drops the same-day suffix (`DECISIONS.2026-08-17b.md`) that check 10 admits. `tools/memory-tree/row_grammar.py` already has `derive_row_re` (:204-212) and `build_rotated_re` (:225-240).
- **Consequence:** Every bold row unit 1 S8 rotates classes as `departure`, so AC1 is red on a correct build. A builder chasing that red would restore rotated rows and undo unit 1, the very defect this unit exists to close. A second row predicate is the duplicate-copy class `derive_row_re`'s own selftest counts.
- **Fix (judged sound):** Read removed rows through `row_grammar.derive_row_re(conf)` and the archive set through `row_grammar.row_docs` or `build_rotated_re`, never a literal. Name both in §10 as the seam. Add an AC2 plant tip that rotates a `- **ID** — …` row into a `<date>b` archive and must read `rotated`.
- **Left-shift gate:** a reuse arm in the spec audit that reds a spec defining a DECISIONS row or archive pattern in prose when `row_grammar.py` exports one.

### H4: Unit 57's MAP_CLI reader is narrower than the bash `source` the driver uses, so the witness certifies a stale conf [high] (ids 19, 35)

- **Where:** spec 57 §2 S1 and §10.
- **What:** S1 reads `MAP_CLI` as 'the last `MAP_CLI=` line winning, a value in double quotes or bare'. `.unattended.conf` is sourced by `unattended.sh` (`. "$CONF"`), so single quotes, an `export` prefix, a trailing `# comment`, a BOM and a CR are all legal. `govkit.parse_conf_assignment` (`tools/govkit/govkit.py:5139-5170`) already reads a conf line by bash's word rule, pinned by a parity selftest.
- **Consequence:** `MAP_CLI='tools/codebase-map/reuse_lookup.py'` reads as a foreign value, so `up` does not re-point it, and S2's 'names any other file' row passes the witness once the lookup is deleted. The witness certifies a retirement while the conf names a deleted file. The driver then silently treats the map as not adopted (`unattended.sh:12035/:12053`).
- **Fix (judged sound):** Read the before-image's conf bytes and the current conf line by line through `govkit.parse_conf_assignment`, last assignment winning as `read_conf_key_gaps` does, with BOM and CR stripped. Apply the same reader to `up`'s 'names the lookup' test. Name it in §10. Add AC rows for a single-quoted lookup value that `up` must re-point, and for a blank value with a trailing comment.
- **Left-shift gate:** a reuse arm that reds a spec describing a conf-line parse in prose when it does not name `parse_conf_assignment`.

### H5: Unit 63 reads no GitLab or Azure indirection key, so an inherited publishing job grades `importable` [high] (ids 15, 40)

- **Where:** spec 63 §2 S1 table and S2.
- **What:** S2's opaque list holds only GitLab `trigger:` or `include:` 'inside a job' and Azure `task:` or `template:` steps. GitLab's `include:` is top-level and imports jobs from other files and projects. Jobs also take their `script` from `extends:`, YAML anchors and merge keys (`<<: *x`) and `!reference`. Azure pulls jobs through a top-level `extends: template:` and stage- or job-level `template:`. None is read or refused. No GitLab or Azure file is tracked, so S4's plants are the whole population, and none covers these keys.
- **Consequence:** `release: extends: .publish`, with `npm publish` in the hidden `.publish`, has no lines of its own and reads `importable`. So does a job arriving by top-level `include: remote:`. Deny by default fails on the security surface §5 prices.
- **Fix (judged sound):** Widen S2 to every indirection key per dialect. GitLab: job-level `extends:`, any `!reference` tag, any YAML alias or merge key, and a top-level `include:`, which refuses every job in the file, unless the referenced hidden job is resolved in-file and its lines are read. Azure: `template:` at any level and the top-level `extends:`. Each reads `refused: opaque step <key> <value>`. Add S4 plants for `extends:`, `!reference` and top-level `include:`.
- **Left-shift gate:** a fixture-coverage arm for the CI census that requires one plant per indirection keyword in each dialect's keyword list.

### H6: Unit 63's block-scalar rule ends at the first blank line and misses `- |` items [high] (id 39)

- **Where:** spec 63 §2 S1.
- **What:** S1 reads a block scalar 'up to the first line indented no deeper than the key'. A blank line has indent 0, so the read stops at the first blank line inside a `|` or `>` block, which YAML allows. S1 is also silent on a list item that is itself a block scalar (`- |` under `script:`), the common GitLab multi-line form.
- **Consequence:** `script: |` holding `npm ci`, a blank line, then `npm publish` reads only `npm ci`, and the job grades `importable`. The same holds for a `- |` item holding the publish verb. An ordinary YAML layout bypasses the unit's refusal.
- **Fix (judged sound):** State that blank and whitespace-only lines inside a block scalar belong to it, and that the block ends at the first non-blank line indented no deeper than the key (or the list dash for a `- |` item). Name the `- |` and `- >` forms. Add `ci-census` plants: a blank line before `npm publish` in a `script: |` block, and a `- |` item holding `cargo publish`.
- **Left-shift gate:** a bug-class checklist entry, "hand-rolled YAML block reader", requiring blank-line and list-item block-scalar plants in any census that reads YAML by indentation.

## Medium

### M1: 54 AC3 and 55 S2/AC1 stage a break that exits 0 [medium] (ids 1, 34)

- **Where:** spec 55 §2 S2 and §6 AC1; spec 54 §6 AC3, second half. This is H1's defect, bound here at medium. Id 1 was re-graded high to medium because the result is a loud red on a correct build; id 34 because it is confined to 54's acceptance probe.
- **What:** Under `set -u` without `set -e`, a `.` of a missing `lib/region.sh` is not fatal, and the inline `region_sh` block still defines `region`. The staged copy exits 0.
- **Consequence:** AC1 and 54 AC3's 'exits non-zero' half cannot pass on a correct build. A builder may weaken the arm, switch the gate to `set -e`, or drop the inline block to make it pass.
- **Fix (id 1's fix judged UNSOUND; the skeptic's corrected fix):** Stage the break as 43 would ship it. In the copy, delete the inline `region_sh` block and insert `. "$(dirname "$0")/lib/region.sh"` after `set -u`. At a lib-less prefix `region` is undefined, the `block=$(region ...) ||` branch fires and the gate exits 2. A copy that is not isolated still finds `lib/region.sh` and exits 0, which reds the arm. Equivalently, insert `. "$(dirname "$0")/lib/region.sh" || exit 2`. Rewrite 55 S2, 55 AC1 and 54 AC3 to this break and observe the staged copy exit non-zero. For id 34 (judged sound): expect exit 2 with the 'not one open above one close' or no-definition message, and keep AC3's green half as written.
- **Left-shift gate:** as H1.

### M2: Unit 54's AC1 forbids the `lib/` token that S4's required header contains [medium] (ids 3, 23)

- **Where:** spec 54 §6 AC1 against §2 S4 and S1.
- **What:** S4 requires the gate's header to say the reader is inline 'because `<prefix>/lib/` travels to nobody'. AC1 requires `grep -c "lib/" tools/check-microformats.sh` to print 0, and S1 says no line names a path under `lib/`. AC1 is already 0 at base, so it cannot catch the absence it was meant for.
- **Consequence:** A correct build prints at least 1. The builder must break AC1 or drop the header sentence that records why the block is inline, which invites the next change to source the lib again.
- **Fix (judged sound):** Narrow AC1 and S1 to a source line naming `lib/`, e.g. `grep -cE '^[[:space:]]*(\.|source)[[:space:]].*lib/' tools/check-microformats.sh` prints 0. Or phrase S4's header without the literal token. The behavioural proof stays with AC3 once its staged break is fixed (M1).
- **Left-shift gate:** a spec-audit arm that evaluates each grep-count AC against the literal strings the same spec's scope items require the file to contain.

### M3: Unit 59's §4 table and S1 give two answers on which lines are rows [medium] (ids 4, 38)

- **Where:** spec 59 §4 'The classification' table against §2 S1, and S2's order check. This is H3's defect, bound here at medium. Id 38 was re-graded high to medium because AC1 reds at the pass.
- **What:** The table classes a removed line as `rotated` only when it is 'a row `<id> · …`'. S1's prose has no format restriction. At base, 141 rows use the `·` form and 72 the bold form. S2's order check must find rows by id with the same gap.
- **Consequence:** Rotated bold rows (KICK-aReplayedCard-1 among them) read `departure`, so AC1 ('0 departure(s)') reds on a correct build.
- **Fix (judged sound):** Read a removed line's id through `row_grammar.derive_row_re` (`tools/memory-tree/row_grammar.py:204`). State in the §4 table that both spellings are rows. Add a bold-format row to the `log-diff` plant's rotated tip so AC2 observes it.
- **Left-shift gate:** as H3.

### M4: 61 AC1's bare `bash` plant writes no pidfile under WSL at order 7 [medium] (id 12)

- **Where:** spec 61 §3 (resolution deferred to unit 64) against §6 AC1. This is H2's defect, bound here at medium.
- **What:** AC1's plant starts with a bare `bash` and passes a Windows pidfile path. At 61's pass, before 64 S6 resolves bash, WSL's python cannot write that path, crashes and exits 0 at once.
- **Consequence:** AC1 records a clean exit 0 instead of `unobservable: past 2s`, no pidfile exists, and the criterion and the `observe-tree-hang` arm red on a WSL node. With a long-running WSL child, `taskkill /T` reaches only the Windows launcher.
- **Fix (judged sound):** Move 64 S6's resolution (`resolve_bash` for a leading `bash`, `sys.executable` for python) into 61 S2, or land 64 S6 before order 7. At minimum, plant with the resolved bash executable.
- **Left-shift gate:** as H2.

### M5: 61 AC1's grandchild is a bare `python`, which the MS-Store stub answers with 9009 [medium] (id 42)

- **Where:** spec 61 §6 AC1.
- **What:** The plant runs `python -c …` inside `bash -c '...; true'`. `regen.py:273-274` maps only a leading python to `sys.executable`, so the nested name resolves through PATH. `resolve_python` tries `python3 python py`, so a node where only `py` works is supported.
- **Consequence:** On such a node the grandchild exits 9009 at once, `; true` makes bash exit 0 before the 2s bound, and the case reds the `gotchas selftest` leg for an environmental reason. The tree kill is never exercised there.
- **Fix (judged sound):** Build the planted argv with a shlex-quoted `sys.executable` in place of the bare `python`. Assert the pidfile exists before judging liveness, so a grandchild that never started reads as a harness failure, not a pass or fail of the kill.
- **Left-shift gate:** the H2 spec-tokens arm, extended to bare interpreter names nested inside a `-c` string.

### M6: 61 AC2's slice diff does not strip CR, and `gotchas.py` is checked out CRLF [medium] (id 11)

- **Where:** spec 61 §6 AC2.
- **What:** AC2 compares raw awk slices of `regen.py` and `gotchas.py` with `diff`. `git ls-files --eol` shows `gotchas.py` as `w/crlf attr/text=auto` and `regen.py` as `w/lf attr/text eol=lf`.
- **Consequence:** Every line differs by a trailing CR, so AC2 reds on a correct build in this working copy.
- **Fix (judged sound):** Pipe both slices through `tr -d '\r'` before `diff`, as `blk` does (`resolve-python.test.sh:221`), or compare index blobs.
- **Left-shift gate:** a spec-audit rule that any AC comparing working-tree text across files must strip CR or read index blobs.

### M7: Gotchas.py's inline `tree_kill_py` copy needs `signal`, which the module does not import [medium] (id 26)

- **Where:** spec 61 §2 S2 and §4 Files touched. Re-graded high to medium: POSIX only, a crash plus an orphan rather than a wrong certification.
- **What:** S2 copies the block body unchanged. On POSIX it calls `os.killpg(proc.pid, signal.SIGKILL)`. `regen.py` imports `signal` at :39, outside the wrapped block (:249-267). `gotchas.py` does not import it, and S2 never says it must.
- **Consequence:** On POSIX, the first `--observe` timeout raises a NameError that `except (OSError, subprocess.SubprocessError)` does not catch. The verb crashes, no group is killed, and the grandchild keeps running. Every CI job runs on windows-latest, so no leg sees it.
- **Fix (judged sound):** Add to S2 that `gotchas.py` gains `import signal` (and any other global the block names) outside the block. Add a POSIX-runnable selftest case, or a static check that every global name the block uses is imported in each copy. Run the observe-tree-hang case on a POSIX shell once.
- **Left-shift gate:** a parity-block check that every free name in a `# >>>` Python block is bound by an import in each host file.

### M8: Unit 57's before-image holds no `.unattended.conf` on the rows `up` does not write [medium] (id 13)

- **Where:** spec 57 §2 S1 and §10, and spec 58 §2 S1. See L10 for the same defect at low grade.
- **What:** 57 S1 and §10 assume the before-image always holds the conf's prior bytes, and 58 S1 assumes it records an absent conf as `null`. TOOL-dSafePassage-1 §4 images only 'every path it will write or remove'. On the blank, foreign and absent rows, `up` writes no conf.
- **Consequence:** The witness cannot tell 'no `MAP_CLI` line' from 'not recorded', and cannot compute S2's 'MAP_CLI is unchanged'. The rejected-alternative rationale fails on the rows it was written for.
- **Fix (judged sound):** State in 57 S1 that `up` always records `.unattended.conf` in its before-image, as bytes or `null`, whether or not it rewrites it. Add an AC reading the image's conf entry after an `up` over a blank `MAP_CLI` and over an absent conf (58 AC1).
- **Left-shift gate:** a spec-audit arm that, for every witness reading a path from the before-image, checks the step's `up` images that path on every row of its table.

### M9: Unit 58's `down` refuses once a map-only adopter later gains a conf [medium] (id 37)

- **Where:** spec 58 §2 S3.
- **What:** S3 states `down` only for a target that still holds no conf. §5 names the case where a map-only adopter later adopts the unattended kit and gains a conf. The image records the conf as `null`, and the down contract (dSafePassage-1:239-241) exits 1 on any path whose bytes match neither image. AC2 plants that state but never runs `down`.
- **Consequence:** The rollback refuses, naming a file the step never wrote, so the two lookup files are never restored.
- **Fix (judged sound):** Add a sentence and an AC: where the image records the conf `null` and a conf exists now, `down` leaves it untouched, restores the two lookup files and exits 0. Alternatively, have `up` not image an absent conf, and make the witness's absent-file row read the conf only from the tree.
- **Left-shift gate:** a spec-audit rule that every state a spec's §5 names must appear in an AC that runs both `up` and `down`.

### M10: Unit 64's AC12 greps one dossier for a leg the playbook dossier claims [medium] (id 5)

- **Where:** spec 64 §6 AC12 against §2 S15.
- **What:** S15 requires each leg of 52's S33 to S36 to have a row in 'the claiming dossier'. AC12 greps only `memory/map/features/memory-tree-hygiene.md`. 52 S35's `adopt instructions selftest` is declared in `tools/playbook/kit.toml` and claimed by `memory/map/features/playbook.md`.
- **Consequence:** AC12 is red on a correct build, or the builder writes the playbook leg's row into the wrong dossier.
- **Fix (judged sound):** Make AC12 per leg: grep each leg in `tools/run-gates/ceiling-evidence.txt` and in its claiming dossier (`playbook.md` for S35, `memory-tree-hygiene.md` for the memory-tree legs). Or derive the dossier from the map.
- **Left-shift gate:** a spec-tokens arm that resolves each leg named in an AC to its declaring kit and reds a dossier path that does not claim it.

### M11: Unit 60's duplicate-proposal refusal is keyed on a dated file name [medium] (id 7)

- **Where:** spec 60 §2 S3 and §5 risks. Re-graded low to medium.
- **What:** `propose` refuses only when `<date>-build-<unit id>-reuse-proposal-<feature>-<n>.md` exists. The §5 risk line ('the second call refuses') holds only within one day.
- **Consequence:** Re-running unit 19's migration, or 64 S7's re-file, on a later date appends a second live proposal for one part. Only 64 S8's end-of-build count notices, and the owner's queue holds the duplicate meanwhile.
- **Fix (judged sound):** Refuse when any record under the build carries a live proposal (no `- **Disposition:**` line) for `<feature>.<n>`, whatever its date. Add a plant that files the part, changes the date and files again, expecting exit 2.
- **Left-shift gate:** a bug-class checklist entry, "append keyed on a dated name", for every record-writing verb.

### M12: Unit 56's inline `region_nth` copy is outside the region census's factory exclusion [medium] (id 22)

- **Where:** spec 56 §2 S1-S3 and §3; no census item.
- **What:** 56 makes `region_nth` a parity block and inlines it in `tools/run-gates/run-gates.test.sh`. The census exclusion (43 S1 :42-43, 18 §4 :122-123) names only `tools/lib/region.*` and the `region_py`, `region_sh`, `gen_region_awk` and `region_js` blocks. The house idiom `index(ln,o)==1` matches the census regex.
- **Consequence:** `region.py --census` counts the inline copy as a site and exits 1 at the close. The builder edits the census ad hoc or reverts the copy.
- **Fix (judged sound):** Add a scope item that adds `region_nth` to the census's factory-block list, so the census and PARITY_ROWS share one stem set. Add an AC: `python tools/lib/region.py --census` prints no site in `run-gates.test.sh`.
- **Left-shift gate:** derive the census's factory-block list from PARITY_ROWS rather than a typed list.

### M13: Unit 64 S13 changes every `region_py` copy but names only the canonical [medium] (id 29)

- **Where:** spec 64 §2 S13, §4 Files touched and §7 Gates.
- **What:** S13 and AC10 change `splice_region` in `tools/lib/region.py` and every `region_py` copy. Files touched names only `region.py` and `marker-contract.test.sh`, and the version line names only memory-tree, codebase-map and govkit. Copies sit in the roles, playbook, runlog and drift-audit kits and in `gen_build_index.py` (18 §4).
- **Consequence:** Editing only the canonical reds the `region_py` parity row. Editing all copies leaves four kits' version carriers unbumped, and §7 omits `roles catalogue`, `roles render selftest`, `playbook render selftest`, `runlog selftest`, `drift-audit selftest`, `drift-audit records` and `build-index selftest`.
- **Fix (judged sound):** Name every `region_py` copy site in Files touched (18 §4's table, re-derived by `git grep -l '^# >>> region_py'` at the pass). Add KIT_ROLES_VERSION, KIT_PLAYBOOK_RENDER_VERSION, KIT_RUNLOG_VERSION and KIT_DRIFT_AUDIT_VERSION, and the seven legs, to §7.
- **Left-shift gate:** a spec-audit arm that expands any spec naming a parity block to its copy sites and checks each site's kit, version constant and legs are listed.

### M14: Unit 56 proves the canary's lib-less start only by grep [medium] (id 30)

- **Where:** spec 56 §6 AC3 and §7 Gates.
- **What:** AC3 is `grep -c "lib/region"` prints 0, plus an in-gov slice compare. No arm runs the canary at a prefix without `lib/`. Unit 55 §4 rejects exactly this grep-only proof for the sibling gate.
- **Consequence:** A later re-point of the canary to another lib helper, or a path built at run time, goes green in gov and fails only on the copy-install path.
- **Fix (judged sound):** Add a scope item and New-arm line: run the canary's `mempause_sh` slice, or a cheap early slice, from a copy of the run-gates kit dir with no `lib/` sibling, and stage the failing case with the `source` of `lib/region.sh` put back. Or record why this suite needs no such arm.
- **Left-shift gate:** a foreign-prefix leg variant that runs every shipped suite from a lib-less copy.

### M15: Unit 63 S3's credential rule reads only script lines and denies GitLab grants exist [medium] (id 41)

- **Where:** spec 63 §2 S3.
- **What:** S3 rests on 'GitLab and Azure jobs carry no grant the census can read', but GitLab jobs declare credentials with `secrets:` and `id_tokens:`. 'Any of whose lines' most naturally means S1's script lines. Nothing names `variables:`, Azure step `env:`, `secrets:` or `id_tokens:`. S4's plant puts `$CI_DEPLOY_TOKEN` in the script line, so it cannot catch the narrow reading.
- **Consequence:** A job whose credential arrives through `env:`, `variables:`, `secrets:` or `id_tokens:` and whose script runs `./release.sh` reads `importable`. Unit 51 §3 relies on this fallback.
- **Fix (judged sound):** Name the lines S3 reads: every line of the job, including `variables:`, Azure step `env:`, and GitLab `secrets:` and `id_tokens:`. A GitLab job carrying `secrets:` or `id_tokens:` reads `refused: unreadable credentials <key>`. Plant an Azure `env:`-mapped secret with a script that never names it.
- **Left-shift gate:** as H5's fixture-coverage arm, extended to each dialect's credential keys.

### M16: Unit 61's observer writes its output file inside the clone it grades [medium] (id 43)

- **Where:** spec 61 §2 S2. Re-graded low to medium: behaviour changes, contained.
- **What:** S2 sends each run's output to 'one temporary file under the scratch clone', the working tree the observed leg grades. The cited precedent, `regen.py:290`, uses `tempfile.TemporaryFile()` outside the tree.
- **Consequence:** The leg sees an untracked file the observer planted, and the clean run's leftover is still there for the planted run. A leg reading untracked files (`gate-fingerprint.sh:61`, check-wiring's porcelain read) can fail on it, or record `unobservable` for a class it would observe.
- **Fix (judged sound):** Put the output outside the clone, as regen.py does: `tempfile.TemporaryFile()` or a sibling of the clone under the temp root, one file per run.
- **Left-shift gate:** an observe-harness assertion that the scratch clone's `git status --porcelain --untracked-files=all` is empty before each run.

## Low

### L1: Unit 19's Destinations table still spells the tag `unit.reuse.<feature>-<n>` [low] (id 6)

- **Where:** spec 60 §2 S2 and §3 Edges (hands-off to TOOL-dLinkedLibrary-19).
- **What:** 60 S2 and 38 S1 give `unit.reuse.<feature>.<n>`. Spec 19:145 still states the hyphenated tag, and 60's hands-off to 19 re-reads only S3's call.
- **Consequence:** Unit 19's builder may write the hyphenated tag, which 38 calls red, into plan output or checks.
- **Fix (judged sound):** Have 60's hands-off to 19 say its Destinations row reads `unit.reuse.<feature>.<n>` from this unit on, and fold the same correction into 19's table.
- **Left-shift gate:** a spec-tokens arm that reds two spellings of one tag template across the build's live specs.

### L2: Unit 56 grounds the canary's shipping in a runbook `cp -r` step that does not exist [low] (id 16)

- **Where:** spec 56 §1 para 2 and §4 Evidence (`kit.toml:35-41`).
- **What:** WIRE-INTO-PROJECT.md has no `cp -r` step for run-gates; it appears only at :869, :935 and :937. 56 relays the kit.toml comment, which has no matching runbook step.
- **Consequence:** The next change will read this unit as evidence that the canary ships by `cp -r`. Behaviour is unaffected.
- **Fix (judged sound):** Ground §1 in the canary's header (`run-gates.test.sh:30-31`, 'this harness SHIPS with the kit') and drop the runbook claim, or name the step that copies run-gates.
- **Left-shift gate:** a grounding check that every runbook claim a spec cites resolves to a line in WIRE-INTO-PROJECT.md.

### L3: Unit 64 S19 leaves an orphan replay-harness comment in `tools/codebase-map/kit.toml` [low] (id 17)

- **Where:** spec 64 §2 S19.
- **What:** S19 deletes :44-57, but the replay-harness comment starts at :39. AC16 greps `rank_harness|replay-phrases`, which :39-43 do not contain.
- **Consequence:** A stale comment survives in a shipped descriptor while AC16 reads green.
- **Fix (judged sound):** Give the range as :39-57, or as 'the comments above each deleted `[[files]]` row'. Make AC16 also grep `replay harness`.
- **Left-shift gate:** a spec-audit rule that a line-range deletion is checked against the enclosing comment block at the spec's pinned base.

### L4: Units 54, 56 and 61 add indexed symbols without the codebase-map re-render [low] (id 28)

- **Where:** spec 56 §7 and §4; spec 54 and spec 61, same sections. Re-graded medium to low: the leg reds and prints its regen command.
- **What:** 54 adds `region` and `splice` to `check-microformats.sh`, 56 adds `region_nth` to `run-gates.test.sh`, and 61 adds `run_tree_kill` to `gotchas.py`. None lists `memory/map/generated/symbols.json` or the `codebase-map coverage + freshness` leg, which has no guard.
- **Consequence:** Each pass leaves the committed render stale and the always-run leg red until someone re-renders.
- **Fix (judged sound):** Add `memory/map/generated/symbols.json` (regenerated by the map's regen command) to Files touched in 54, 56 and 61, and the leg to each §7. Or name the close's shared-render step as its owner.
- **Left-shift gate:** a spec-audit arm that adds `symbols.json` and the freshness leg to any spec defining a new function in a tracked file.

### L5: Unit 61 edits `regen.py` but omits the `run-gates canary` leg [low] (id 31)

- **Where:** spec 61 §7 Gates.
- **What:** S1 wraps `run_tree_kill` in `regen.py` in markers. `run-gates canary` exercises regen.py's bounded run (`run-gates.test.sh:512`), and its guard covers regen.py, but §7 omits it.
- **Consequence:** If the edit breaks regen.py's kill path, no gate in this spec catches it before the close.
- **Fix (judged sound):** Add `run-gates canary` to 61 §7.
- **Left-shift gate:** derive each spec's §7 from the guards in `tools/gate-legs.json` that match its Files touched.

### L6: The new canonical openers lack the `canonical copy:` label [low] (id 32)

- **Where:** spec 56 §2 S1 and spec 61 §2 S1.
- **What:** `# >>> region_nth` in `tools/lib/region.sh` and `# >>> tree_kill_py` in `regen.py` are spelled bare. `_scan_install_sites` (`map_lib.py:864-901`) skips a file only when its opener carries `canonical copy: <basename>`.
- **Consequence:** Each helper's install count in the generated map is off by one, a small ranking skew.
- **Fix (judged sound):** Spell each canonical opener with the label, e.g. `# >>> region_nth — canonical copy: region.sh in the gov lib dir (byte-identical; gated)`, likewise for `tree_kill_py`, with the inline copies carrying the same opener byte for byte.
- **Left-shift gate:** a marker-contract check that every canonical parity opener carries `canonical copy: <own basename>`.

### L7: Unit 64's slug and id checks use `$`, which admits a trailing newline [low] (id 44)

- **Where:** spec 64 §2 S14.
- **What:** `SLUG_RE` (`backlog.py:129`) and `GRANT_ID_RE` (:453) end in `$`, and `re.match` accepts `dLinkedLibrary\n` and `TOOL-x-1\n`. AC11 plants only `..` and `/`.
- **Consequence:** A trailing-newline value reaches the path join, contradicting 'validated before any path join'. It is not traversal.
- **Fix (judged sound):** Use `fullmatch` (or `\Z`) in `dossier_move.py apply`, and add a trailing-newline value to the `bad-values` plant.
- **Left-shift gate:** a lint that reds `re.match` with a `$`-anchored pattern used as a validator.

### L8: Unit 56's absent-block path is masked by the `tr` pipeline's status [low] (id 45)

- **Where:** spec 56 §5 'error / empty / loading states'.
- **What:** §5 says an absent `mempause_sh` block is reported. S3's slice is `$( region_nth … | tr -d '\r' )`, and the canary sets no `pipefail`, so the status is `tr`'s and the empty `_mpb` runs.
- **Consequence:** An absent block reds as a `127 127 …` value mismatch, naming the wrong cause.
- **Fix (judged sound):** Capture `region_nth`'s output and status before `tr` (`_mpb=$(region_nth …) || fail …; _mpb=$(printf '%s' "$_mpb" | tr -d '\r')`), or check `[ -n "$_mpb" ]` and fail naming the missing block.
- **Left-shift gate:** a bug-class checklist entry, "status lost through a pipe in `$( )`", for suites without `pipefail`.

### L9: Unit 54 S3 names one exit-3 cause where `region_sh` has two [low] (id 46)

- **Where:** spec 54 §2 S3.
- **What:** `region_sh` also sets `bad` on any line that begins with the marker but is not equal to it. The `grep -cxF` count does not see such a line. S3 names only 'a close above its open'.
- **Consequence:** A charter with the exact pair plus `<!-- microformats --> (see below)` now exits 2 claiming the pair is reversed. The exit is defensible but the message misleads.
- **Fix (judged sound):** Have S3 name both causes, or have the message say 'a malformed or reversed fence pair' with the offending line numbers. Add a suite arm with a prefixed extra marker line.
- **Left-shift gate:** a spec-audit rule that a spec adopting a parity reader lists every exit code the reader's body can produce.

### L10: Unit 57 never says what the witness does on a missing conf entry [low] (id 36)

- **Where:** spec 57 §2 S1 and S2 (the table's first and third rows). This is M8's defect, bound here at low; re-graded medium to low because AC1 forces resolution during the pass.
- **What:** S1 reads `MAP_CLI` from 'the `.unattended.conf` bytes its before-image keeps', but under S3 `up` writes, and so images, no conf on the blank or foreign rows. A missing entry is neither 'no `MAP_CLI=` line' nor 58's `null`.
- **Consequence:** The witness meets a missing key and, per §5, exits 1 or raises, so the blank-`MAP_CLI` adopter 57 exists for fails every update.
- **Fix (judged sound):** State that `up` always images `.unattended.conf` (bytes, or `null` when absent), and that the witness reads a missing entry as an error naming the step's contract. Or define a missing entry as the first row. Add an AC inspecting `before.json` after a blank-`MAP_CLI` up.
- **Left-shift gate:** as M8.

review-shape kind=spec-audit round=1 intensity=full at=synth raw=46 confirmed=38 refuted=8 unverified=0 blocker=0 high=9 medium=19 low=10 agents=11 out-tokens=230128

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes |
|---|---|---|---|---|---|---|---|---|
| 1 | coherence | memory/builds/dLinkedLibrary/spec/2026-10-27-spec-TOOL-dLinkedLibrary-55.md:section 2 S2, section 6 AC1 (and TOOL-dLinkedLibrary-54 section 6 AC3, second half) | high | medium | confirmed | Re-probed. tools/check-microformats.sh:23 is `set -u`, and grep finds no `set -e` or `set -o` anywhere in the file. In verify-1 I ran a script holding `set -u`, then `. "$(dirname "$0")/lib/region.sh"`, then `echo continued`. It printed `No such file or directory`, then `continued`, and exited 0. So the staged copy in 55 S2/AC1 and in 54 AC3's red half still exits 0, and the 'asserts a non-zero exit' half fails on a correct build. Graded medium: the result is a loud red on a correct build, not a silent false pass. | unsound | fixture-passes-by-finding-nothing |
| 2 | coherence | memory/builds/dLinkedLibrary/spec/2026-10-27-spec-TOOL-dLinkedLibrary-61.md:section 6 AC1, section 3 Non-goals (bash resolution deferred to TOOL-dLinkedLibrary-64 S6) | high | high | confirmed | Re-probed. Python `subprocess.run(['bash','-c','uname -s; command -v python'])` returned `0 b'Linux\n/usr/bin/python\n'`, even though shutil.which('bash') names Git Bash, so a bare `bash` in a Popen argv reaches WSL on this node. regen.py:273-279 rewrites bash before Popen for exactly this reason. 61 S2 carries only the kill, and its section 3 defers bash resolution to 64 S6. README build order puts 61 at step 7 and 64 at step 29. So 61's AC1 plant (`bash -c 'python -c ...'`) runs under WSL at its own pass. Its pid-liveness check, run from Windows, then does not observe the grandchild's tree kill. That is a check certifying what it did not check, on a narrow path (a Windows node with WSL). | sound | subprocess-resolves-a-different-shell |
| 3 | coherence | memory/builds/dLinkedLibrary/spec/2026-10-27-spec-TOOL-dLinkedLibrary-54.md:section 6 AC1 against section 2 S4 (and S1) | medium | medium | confirmed | Spec-54 S4 (lines 52-54) requires the header to say the reader is inline 'because `<prefix>/lib/` travels to nobody'. AC1 (line 121) requires `grep -c "lib/" tools/check-microformats.sh` to print 0. S1 (line 43) also says no line names a path under `lib/`. grep for lib/ in the gate at HEAD found no match, so AC1 is green at base and turns red once S4's sentence lands. The ACs are unsatisfiable together. | sound | - |
| 4 | coherence | memory/builds/dLinkedLibrary/spec/2026-10-27-spec-TOOL-dLinkedLibrary-59.md:section 4 'The classification' table against section 2 S1 | medium | medium | confirmed | Spec-59's section 4 table classes a removed line as `rotated` only for 'a row `<id> · …`', and everything else falls to `departure`. On re-probe, DECISIONS.md holds 141 rows in the `- <id> · ` form and 72 in the `- **<id>**` form. So a bold row that unit 1 rotates reads as a departure under the table, and AC1 ('0 departure(s)') reds on a correct build. S1's prose has no format restriction, so S1 and the table disagree. row_grammar.py:204 defines derive_row_re. | sound | - |
| 5 | coherence | memory/builds/dLinkedLibrary/spec/2026-10-27-spec-TOOL-dLinkedLibrary-64.md:section 6 AC12 against section 2 S15 | medium | medium | confirmed | 64 S15 (lines 89-91) requires a row in 'the claiming dossier' for each leg of 52's S33 to S36. AC12 (line 250) greps only ceiling-evidence.txt and memory/map/features/memory-tree-hygiene.md for every leg. 52 S35 (lines 151-152) declares `adopt instructions selftest` in tools/playbook/kit.toml with 'the playbook dossier's claim', and memory/map/features/playbook.md exists. A correct build therefore prints 0 for that leg in the named file. | sound | - |
| 6 | coherence | memory/builds/dLinkedLibrary/spec/2026-10-27-spec-TOOL-dLinkedLibrary-60.md:section 2 S2 and section 3 Edges (hands-off to TOOL-dLinkedLibrary-19) | low | low | confirmed | grep shows spec-19:145 `unit.reuse.<feature>-<n>`, while spec-38:38 and spec-60:46 give `unit.reuse.<feature>.<n>`. 60's hands-off to 19 (line 69) re-reads only S3's call as the part `<feature>.<n>`. It does not mark 19's Destinations row as superseded, so the hyphenated tag stays stated in 19. | sound | two-answers-to-one-question |
| 7 | coherence | memory/builds/dLinkedLibrary/spec/2026-10-27-spec-TOOL-dLinkedLibrary-60.md:section 2 S3 and section 5 risks | low | medium | confirmed | 60 S3 (lines 48-52) names the record `<date>-build-<unit id>-reuse-proposal-<feature>-<n>.md` and refuses only on an existing record of that name. The risk line (lines 117-118) claims the second spelling 'refuses', which holds only for the same date and unit id. A re-file on another date writes a second live proposal. Only 64 S8's end-of-build count notices it. Refusing on a live record for the part fits 64 S7/S8, which re-file only seams that have no live or accepted record. | sound | append-without-an-idempotence-key |
| 8 | grounding | memory/builds/dLinkedLibrary/spec/2026-10-27-spec-TOOL-dLinkedLibrary-55.md:section 2 S2, section 6 AC1, section 7 New arm | high | - | refuted | duplicate of id=1: it is the same defect in 55 S2/AC1. I re-observed it: `.` of a missing file under `set -u` continued and exited 0. Its fix is unsound: after 54 the gate already calls `region` from the inline block, so sourcing a missing lib and calling `region` still succeeds unless the inline block is also deleted. | unsound | - |
| 9 | grounding | memory/builds/dLinkedLibrary/spec/2026-10-27-spec-TOOL-dLinkedLibrary-54.md:section 6 AC3 | medium | - | refuted | duplicate of id=1: id=1 already names 54 AC3's broken red half. I re-observed the same bash behaviour: a missing `.` under `set -u` continues and exits 0. | sound | - |
| 10 | grounding | memory/builds/dLinkedLibrary/spec/2026-10-27-spec-TOOL-dLinkedLibrary-54.md:section 2 S4 against section 6 AC1 | medium | - | refuted | duplicate of id=3: it is the same S4-versus-AC1 contradiction in spec-54 (lines 52-54 against line 121), confirmed there. | sound | - |
| 11 | grounding | memory/builds/dLinkedLibrary/spec/2026-10-27-spec-TOOL-dLinkedLibrary-61.md:section 6 AC2 | medium | medium | confirmed | I re-ran `git ls-files --eol` on the two files. It printed `i/lf w/crlf attr/text=auto` for tools/memory-tree/gotchas.py and `i/lf w/lf attr/text eol=lf` for tools/run-gates/regen.py. AC2 in spec 61 section 6 slices both working-tree files with a bare awk and compares them with `diff`, and nothing strips CR. In this checkout every line of the gotchas.py slice ends in a CR, so AC2 reds on a correct build. The effect stays inside this one criterion. | sound | - |
| 12 | grounding | memory/builds/dLinkedLibrary/spec/2026-10-27-spec-TOOL-dLinkedLibrary-61.md:section 3 (resolution deferred to unit 64) against section 6 AC1 | medium | medium | confirmed | I ran `subprocess.run(['bash','-c','uname -s; command -v python'])` from Python on this node. It printed `Linux` and `/usr/bin/python`, so a bare `bash` reaches WSL (/c/Windows/System32/bash.exe exists). Spec 61 section 3 defers resolving a leading bash to unit 64 S6, which is at order 29, while unit 61 is at order 7. AC1's plant starts with a bare `bash` and passes a Windows pidfile path. At 61's own pass WSL's python therefore cannot write that path, and AC1 cannot observe `unobservable: past 2s` with a pidfile. The non-goal defers resolution inside --observe, but the minimal fix of planting with a resolved bash does not depend on what the non-goal withholds. | sound | - |
| 13 | grounding | memory/builds/dLinkedLibrary/spec/2026-10-27-spec-TOOL-dLinkedLibrary-57.md:section 2 S1, section 10 (and unit 58 section 2 S1) | medium | medium | confirmed | TOOL-dSafePassage-1 section 4 (spec lines 230-238) says the image records 'every path it will write or remove'. Spec 57 S3 says up leaves a blank or foreign MAP_CLI 'byte for byte', so on those rows up writes no conf. Unit 58 S1 says up 'writes no .unattended.conf' on the absent row. Nothing in 57 S1 tells up to record the conf anyway. Section 10's claim that the image 'already holds .unattended.conf's prior bytes' is therefore true only on the lookup-naming row. On the other rows the witness has no prior value to compare for 'MAP_CLI is unchanged'. tools/govkit/steps does not exist at base, so no code settles which reading a builder would take. | sound | - |
| 14 | grounding | memory/builds/dLinkedLibrary/spec/2026-10-27-spec-TOOL-dLinkedLibrary-59.md:section 4 'The classification' table, section 2 S1 | medium | - | refuted | duplicate of id=18. Same defect: spec 59's `<id> · …` row predicate misses the bold-led rows. I re-counted at 5fede642: 213 `- ` rows, of which 141 use the `·` shape, 48 use `**ID** —` and 24 use `**ID** -`. | sound | parser-drops-rows-it-cannot-place |
| 15 | grounding | memory/builds/dLinkedLibrary/spec/2026-10-27-spec-TOOL-dLinkedLibrary-63.md:section 2 S1 table and S2 | high | high | confirmed | Spec 63 lines 44-56 read only `script`, `before_script`, `after_script` and `default:` for GitLab. The only opaque keys are a GitLab `trigger:` or `include:` inside a job and an Azure `task:` or `template:` step. Nothing reads or refuses `extends:`, `<<: *anchor`, `!reference`, a top-level GitLab `include:`, or a top-level Azure `extends:`. Take a job `release: extends: .publish` whose `npm publish` lives in the hidden job: release has no lines of its own, so no refusal rule fires and it reads importable. That is the publishing job the unit exists to refuse. `git ls-files` shows no tracked .gitlab-ci.yml or azure-pipelines.yml, so S4's plants are the whole population and none of them covers these keys. | sound | - |
| 16 | grounding | memory/builds/dLinkedLibrary/spec/2026-10-27-spec-TOOL-dLinkedLibrary-56.md:section 1 para 2, section 4 Evidence (kit.toml:35-41) | low | low | confirmed | `grep -n 'cp -r' WIRE-INTO-PROJECT.md` lists memory-tree, drift-audit, process-monitor, codebase-map, memory-recall, lexicon and branch-reconcile. run-gates appears only at :869, :935 and :937, none of them a copy step. Spec 56 section 1 accurately relays the comment at tools/run-gates/kit.toml:35-37, but that comment's claim has no matching runbook step. The canary's own header (run-gates.test.sh:30-31, 'this harness SHIPS with the kit') supports the unit without it. Only the grounding is affected; behaviour is not. | sound | - |
| 17 | grounding | memory/builds/dLinkedLibrary/spec/2026-10-27-spec-TOOL-dLinkedLibrary-64.md:section 2 S19 | low | low | confirmed | `sed -n 36,58p tools/codebase-map/kit.toml` shows the replay-harness comment running from :39 ('The replay harness is GOV-ONLY') to :47, above the replay-phrases.py row at :48. Spec 64 S19 deletes :44-57, so :39-43 survive as a comment about a deleted harness. AC16 greps only `rank_harness\|replay-phrases`, and none of :39-43 contains either word, so AC16 would still read 0. | sound | - |
| 18 | reuse | memory/builds/dLinkedLibrary/spec/2026-10-27-spec-TOOL-dLinkedLibrary-59.md:section 2 S1 and section 4 'The classification' (and section 10) | high | high | confirmed | In spec 59, S1 and the section 4 table key `rotated` on 'a row `<id> · …`', and the archive name is the literal DECISIONS.<date>.md. At 5fede642, 72 of the 213 `- ` rows are bold-led: 48 `- **ID** —` and 24 `- **ID** -`, for example `- **KICK-aReplayedCard-1** —`. These are ordinary decision rows, so unit 1 S8 rotates them like any other. A rotated bold row then reads as a departure and AC1 reds on a correct build. The spec itself says this red leads a builder to restore the rows and undo unit 1. tools/memory-tree/row_grammar.py:204-212 (derive_row_re, which admits optional emphasis) and :225-240 (build_rotated_re, with the `[a-z0-9]*` same-day suffix) are the existing seams the spec bypasses. | sound | - |
| 19 | reuse | memory/builds/dLinkedLibrary/spec/2026-10-27-spec-TOOL-dLinkedLibrary-57.md:section 2 S1 (and section 10) | high | high | confirmed | Spec 57 S1 reads MAP_CLI as 'the last `MAP_CLI=` line winning, a value in double quotes or bare'. tools/govkit/govkit.py:5139-5170 already has parse_conf_assignment, which handles an `export` prefix, single quotes and a trailing `# comment` the way bash `source` does; its docstring warns that a value read any other way grades a value the kit never sees. Under 57's rule, `MAP_CLI='tools/codebase-map/reuse_lookup.py'` keeps its quotes and falls to the 'names any other file' row. up then leaves it in place and the witness passes it as 'unchanged', certifying a retirement while the conf still names the deleted lookup. Section 10 does not name this reader. | sound | - |
| 20 | reuse | memory/builds/dLinkedLibrary/spec/2026-10-27-spec-TOOL-dLinkedLibrary-61.md:section 2 S2, section 6 AC1 (and section 10) | medium | - | refuted | duplicate of id=12. Same defect: AC1's bare `bash` plant at order 7 runs before unit 64 S6 (order 29) resolves bash. I re-read regen.py:269-281 and confirmed run_command resolves run[0] through BASH or sys.executable, which 61 S2 omits. Both findings have the same consequence and the same remedy. | sound | - |
| 21 | reuse | memory/builds/dLinkedLibrary/spec/2026-10-27-spec-TOOL-dLinkedLibrary-61.md:section 8 F2, section 6 AC1 | medium | low | refuted | The premise does not hold on re-probe. In the scratch dir verify-b3 I ran AC1's own plant three times. Each run was Popen of Git bash -c 'python -c "...write pid...; sleep(10)"; true' with output to a TemporaryFile, wait(timeout=2), then run_tree_kill's exact steps: taskkill /F /T /PID, proc.kill, proc.wait. All three returned in 2.19-2.2 s, and one second later tasklist showed the grandchild's pid dead (22756, 29736, 24896). For AC1's plant, a native python under bash -c, taskkill /T does reach the grandchild, so AC1 does not assert something the chosen seam fails to deliver. The cases reap.py:11-13 measured are MSYS fork trees, not this plant. Section 5's caveat about an escaped orphan covers those other trees. That F2 does not weigh reap.py is a preference, not a graded defect. | unsound | - |
| 22 | reuse | memory/builds/dLinkedLibrary/spec/2026-10-27-spec-TOOL-dLinkedLibrary-56.md:section 2 S1-S3 (no census item), section 3 | medium | medium | confirmed | Both 43 S1 (:42-43) and 18 §4 (:122-123) limit the factory to tools/lib/region.* and to the region_py, region_sh, gen_region_awk and region_js blocks. Running grep for census or region_nth over 56, 43, 18 and 64 finds no line that adds region_nth to that list. 56 S3 puts an inline region_nth copy into tools/run-gates/run-gates.test.sh, which is outside tools/lib. The house body for this reader (check-unattended.sh:211-216) uses `index(ln,o)==1`, which the census regex `index\(ln, ?[oc]\) ?== ?1` matches. A copy written in that idiom becomes a site outside the factory, and the census exits 1 at the close. The damage is contained: it shows up as a red census at the close. | sound | - |
| 23 | reuse | memory/builds/dLinkedLibrary/spec/2026-10-27-spec-TOOL-dLinkedLibrary-54.md:section 2 S4 vs section 6 AC1 | medium | medium | confirmed | 54 S4 (:52-54) requires the header to say the reader is carried inline "because `<prefix>/lib/` travels to nobody". AC1 (:121) requires `grep -c "lib/" tools/check-microformats.sh` to print 0. A header that follows S4 contains `lib/`, so AC1 prints at least 1. I ran grep -n "lib/" on the gate at HEAD and it printed nothing, so the first half of AC1 is already green at base. The two clauses contradict each other: the builder has to break one of them. | sound | - |
| 24 | blast-radius | memory/builds/dLinkedLibrary/spec/2026-10-27-spec-TOOL-dLinkedLibrary-54.md:section 6 AC3 (and TOOL-dLinkedLibrary-55 section 2 S2, section 6 AC1) | high | high | confirmed | Reproduced. A scratch script (`set -u`, then `. "$(dirname "$0")/lib/region.sh"`, then `echo after`) printed 'lib/region.sh: No such file or directory', then 'after', and exited rc=0. A failed `.` is not fatal in bash's default mode, and the gate has no `set -e` (it starts with `set -u` at :23). So the staged break in 54 AC3, 55 S2 and 55 AC1 still exits 0, while 55 S2 asserts non-zero. The suite that ships with the gate would carry an assertion that fails on every run, in gov and in every adopter. | sound | criterion-asserts-what-its-own-command-cannot-show |
| 25 | blast-radius | memory/builds/dLinkedLibrary/spec/2026-10-27-spec-TOOL-dLinkedLibrary-54.md:section 2 S4 against section 6 AC1 | medium | - | refuted | duplicate of id=23. It is the same contradiction between S4's header text containing `<prefix>/lib/` and AC1's `grep -c "lib/"` printing 0, and I confirmed it there by reading 54:52-54 and :121. | sound | criterion-asserts-what-its-own-command-cannot-show |
| 26 | blast-radius | memory/builds/dLinkedLibrary/spec/2026-10-27-spec-TOOL-dLinkedLibrary-61.md:section 2 S2 (and section 4 Files touched) | high | medium | confirmed | `grep -n '^import\\|^from' tools/memory-tree/gotchas.py` lists __future__, os, pathlib, re, subprocess, sys, tempfile and tree_lib, with no signal import. regen.py:257 calls `os.killpg(proc.pid, signal.SIGKILL)` inside `except (OSError, subprocess.SubprocessError)`, and regen.py imports signal at :39, which is outside the block S1 wraps (:249-267). 61 S2 says the block body is copied unchanged and never mentions the import. On POSIX the first timeout raises a NameError that this except clause does not catch. remote-ci.yml has runs-on: windows-latest four times, so no leg would ever reach that path. The defect only shows on POSIX, and its effect is an --observe crash plus an orphaned process, not a wrong certification. | sound | - |
| 27 | blast-radius | memory/builds/dLinkedLibrary/spec/2026-10-27-spec-TOOL-dLinkedLibrary-56.md:section 2 S1/S3, section 4 Files touched | medium | - | refuted | duplicate of id=22. It is the same gap: the census factory exclusion omits the inline region_nth copy in run-gates.test.sh, per 43:42-43 and 18:122-123. | sound | - |
| 28 | blast-radius | memory/builds/dLinkedLibrary/spec/2026-10-27-spec-TOOL-dLinkedLibrary-56.md:section 7 Gates, section 4 Files touched (also 2026-10-27-spec-TOOL-dLinkedLibrary-54.md and -61.md, same sections) | medium | low | confirmed | memory/map/generated/symbols.json indexes shell functions by file: line 9253 lists `fail` in tools/check-microformats.sh, and `region` appears for check-unattended.sh, unattended.sh and manifest-check.sh. `run_tree_kill` is listed only for tools/run-gates/regen.py (:21201-21203). test_codebase_map.py:330-331 asserts `committed == expected, f"STALE ..."`. The codebase-map coverage + freshness leg has no guard. Grepping 54, 56 and 61 for symbols or 'codebase-map coverage' finds nothing, while sibling specs 11 and 52 do list symbols.json. The effect is contained: the leg goes red, its message prints the regen command, and the Files touched lists are only estimates. | sound | - |
| 29 | blast-radius | memory/builds/dLinkedLibrary/spec/2026-10-27-spec-TOOL-dLinkedLibrary-64.md:section 2 S13, section 4 Files touched, section 7 Gates | medium | medium | confirmed | 64 S13 (:83-85) and AC10 (:243-244) cover the canonical and every region_py copy. Yet Files touched (:179) names only tools/lib/region.py and marker-contract.test.sh, and the version line (:187) names only memory-tree, codebase-map and govkit. In 18 §4, region_py sites are listed in render_playbook.py, check_roles.py, roles_lib.py, runlog/prose.py and drift_report.py. Those kits carry version_from roles_lib.py, render_playbook.py, runlog_lib.py and drift_report.py, according to grep over their kit.toml files. All seven legs the finder names exist in gate-legs.json, and none of them appears in 64 §7. | sound | - |
| 30 | blast-radius | memory/builds/dLinkedLibrary/spec/2026-10-27-spec-TOOL-dLinkedLibrary-56.md:section 6 AC3, section 7 Gates | medium | medium | confirmed | 56 AC3 (:118-121) is a grep for `lib/region` plus an in-gov slice compare. 56 §7's new arm runs the canary in gov, where lib/ is present. 55 §4 (:88-91) rejects exactly this grep-only proof for the sibling gate and says foreign-prefix parity runs with lib/ present. The install-prefix header (:58-61) says it does not check a path assembled at run time. Nothing runs the canary from a lib-less kit dir. The gap is a regression guard on the cp -r path only, so its effect is contained. | sound | fixture-lacks-a-gate-the-consumer-has |
| 31 | blast-radius | memory/builds/dLinkedLibrary/spec/2026-10-27-spec-TOOL-dLinkedLibrary-61.md:section 7 Gates | low | low | confirmed | Spec 61's section 7 names `gotchas selftest`, `policy fixtures`, `python resolver`, `kit version markers`, `memory hygiene` and `spec tokens`. It does not name `run-gates canary`, but S1 edits tools/run-gates/regen.py. In tools/gate-legs.json, `run-gates canary` (run-gates.test.sh) has the guard ["{prefix}/", "{prefix}/gate-legs.json", "{prefix}/lib/"], which covers regen.py. `grep -n regen.py tools/run-gates/run-gates.test.sh` printed :414, :422, :423, :432, :512 (GATE_REGEN_BOUND=2 ... --check), :525, :534, :543 and :558. The edit only adds comment markers around an unchanged body, so the risk is small and the grade is low. | sound | - |
| 32 | blast-radius | memory/builds/dLinkedLibrary/spec/2026-10-27-spec-TOOL-dLinkedLibrary-56.md:section 2 S1 (and 2026-10-27-spec-TOOL-dLinkedLibrary-61.md section 2 S1) | low | low | confirmed | tools/codebase-map/map_lib.py:864-901 `_scan_install_sites` skips a file only when its opener carries `canonical copy: <basename>` matching its own name. Without that, it counts the canonical file as an install. Every lib canonical carries the label: `grep '^# >>>'` over tools/lib/*.sh, tools/lib/*.py and run-gates.sh shows labelled openers, mempause_sh at run-gates.sh:564 among them. Spec 56 S1 spells `# >>> region_nth` bare, and spec 61 S1 spells `# >>> tree_kill_py` bare. reuse_lookup.py:391/:427 looks up installs by candidate name. For `region_nth` the block name equals the function name, so its installs count is one too high. For `tree_kill_py` only the install totals move. The effect is a small skew in ranking (a bare precedent, kickoff_region at check-unattended.sh:210, already exists), so the grade is low. | sound | - |
| 33 | failure-envelope | memory/builds/dLinkedLibrary/spec/2026-10-27-spec-TOOL-dLinkedLibrary-55.md:section 2 S2, section 6 AC1, section 7 New arm | high | high | confirmed | Reproduced in scratch (verify-b/mf). I wrote the base 5fede642 gate to pfx/kits/ beside the suite's fixture. `bash pfx/kits/check-microformats.sh charter.md` printed `microformats OK — 3 definition(s) graded` with rc=0. The sed-inserted source-line copy printed `line 24: pfx/kits/lib/region.sh: No such file or directory`, then `microformats OK`, with rc=0. The gate has `set -u` and no `set -e`, so a failed `.` does not stop it. Unit 54's gate defines `region` inline and continues the same way. So S2's non-zero assertion and AC1's red half are false on a correct gate, and the shipped arm would be red at the close. | sound | staged-break-substitutes-a-synthetic-value |
| 34 | failure-envelope | memory/builds/dLinkedLibrary/spec/2026-10-27-spec-TOOL-dLinkedLibrary-54.md:section 6 AC3 | high | medium | confirmed | The same scratch probe applies. With the source line inserted after `set -u` and lib/ absent, bash printed `No such file or directory` and went on to rc=0. Spec 54 AC3 keeps the inline region_sh block, so `region` still resolves and the gate exits 0. AC3's 'exits non-zero' half cannot hold on a correct build. The defect is confined to an acceptance probe, not a shipped arm, so the grade is medium. | sound | staged-break-substitutes-a-synthetic-value |
| 35 | failure-envelope | memory/builds/dLinkedLibrary/spec/2026-10-27-spec-TOOL-dLinkedLibrary-57.md:section 2 S1 | high | high | confirmed | tools/unattended/unattended.sh sources the conf with `. "$CONF"`, about 38 lines after :548, so single quotes, `export`, trailing comments and CRs are all legal there. Spec 57 S1 limits the reader to 'a value in double quotes or bare'. A single-quoted lookup value would therefore read as foreign, `up` would not re-point it, and S2's 'names any other file' row would exit 0 while MAP_CLI names the deleted lookup. unattended.sh:12035/:12053 then silently treats the map as not adopted. That is a witness certifying a migration on a narrow path, so the grade is high. | sound | - |
| 36 | failure-envelope | memory/builds/dLinkedLibrary/spec/2026-10-27-spec-TOOL-dLinkedLibrary-57.md:section 2 S1 and S2 (the table's first and third rows) | medium | low | confirmed | dSafePassage-1:236-238 has the image hold 'every path it will write or remove'. Spec 57 S3 has `up` leave a blank or foreign value byte for byte, so on those rows nothing requires `up` to image the conf. Even so, S1 reads MAP_CLI from 'the .unattended.conf bytes its before-image keeps'. The spec never says `up` images the conf when it does not write it. AC1 (blank MAP_CLI, then witness exits 0) would force a builder to resolve this during the pass, which contains the effect, so the grade is low. | sound | - |
| 37 | failure-envelope | memory/builds/dLinkedLibrary/spec/2026-10-27-spec-TOOL-dLinkedLibrary-58.md:section 2 S3 | medium | medium | confirmed | dSafePassage-1:239-241 says a down 'restores each path only where its bytes are the image's after-hash or before bytes, else exits 1 naming the path'. Spec 58 S1 images the conf as null. Its section 5 names the case where a map-only adopter later adopts the unattended kit, so a conf appears. In that case down's contract refuses on the conf. S3 says only 'leaves .unattended.conf absent' and does not cover this state, and AC2 plants it but never runs down. S3's 'deleting nothing up did not write' rules out the data-loss reading. What remains is a rollback that refuses on a narrow path, so the grade is medium. | sound | - |
| 38 | failure-envelope | memory/builds/dLinkedLibrary/spec/2026-10-27-spec-TOOL-dLinkedLibrary-59.md:section 2 S1 and section 4 'The classification' | high | medium | confirmed | I re-ran the counts on `git show 5fede642:memory/DECISIONS.md`. The bold-id shape gave 48, the `<id> · ` shape 141, and `^- ` 213. Spec 59's classification table defines a rotated row only as 'a row `<id> · …`', so a rotated bold row falls to `departure`. tools/memory-tree/row_grammar.py exists as a reusable row reader. AC1 would go red at the pass, which exposes the defect before it ships, so the grade is medium rather than high. | sound | - |
| 39 | failure-envelope | memory/builds/dLinkedLibrary/spec/2026-10-27-spec-TOOL-dLinkedLibrary-63.md:section 2 S1 | high | high | confirmed | Spec 63 S1 reads a block scalar 'up to the first line indented no deeper than the key'. A blank line inside the block has indent 0 and ends the read under that literal rule, although YAML allows blank lines there. S1 also names scalars, lists of scalars and block scalars, but not a list item that is itself a block scalar (`- \|`). Either layout lets `npm publish` go unread, and the job grades importable on the security surface section 5 prices. That is a wrong census result on an ordinary path, so the grade is high. | sound | - |
| 40 | failure-envelope | memory/builds/dLinkedLibrary/spec/2026-10-27-spec-TOOL-dLinkedLibrary-63.md:section 2 S2 | high | high | confirmed | Spec 63 S2 lists only GitLab `trigger:`/`include:` 'inside a job' and Azure `task:`/`template:` steps. It has nothing for GitLab job-level `extends:`, `!reference`, YAML anchors or merge keys, or a top-level `include:`. It also has nothing for Azure stage- or job-level `template:` or top-level `extends:`. A job built from `extends: .publish` or from an included file has no publish line of its own and reads importable, which contradicts F2's 'deny by default'. The S4 plants cover none of these forms, and the repository tracks no GitLab or Azure files, so nothing else would catch them. | sound | - |
| 41 | failure-envelope | memory/builds/dLinkedLibrary/spec/2026-10-27-spec-TOOL-dLinkedLibrary-63.md:section 2 S3 | medium | medium | confirmed | I re-read spec 63 at lines 41-56. S1's table is headed 'Keys whose lines a job runs' and lists only script, before_script, after_script for GitLab and script, bash, pwsh, powershell for Azure. S3 then says 'any of whose lines', which most naturally means those S1 lines. Nothing in spec 63 names variables:, Azure step env:, or GitLab secrets:/id_tokens:; a grep for env\|variables\|secrets\|id_tokens found no such key. Unit 51 §3 (lines 62-63) leans on the grant and secret rules to refuse a publishing verb the list misses. So a job whose credential arrives only through env: or variables: and whose script runs `./release.sh` reads `importable`. The S4 plant puts $CI_DEPLOY_TOKEN in the script line itself, so a builder who reads only script lines still passes AC3. GitLab's job-level secrets: and id_tokens: are real credential keys, which makes S3's premise 'carry no grant the census can read' at best incomplete. | sound | - |
| 42 | failure-envelope | memory/builds/dLinkedLibrary/spec/2026-10-27-spec-TOOL-dLinkedLibrary-61.md:section 6 AC1 | medium | medium | confirmed | Spec 61 AC1 (line ~111) has the planted argv run a bare `python -c` inside `bash -c '...; true'`. regen.py:273-274 maps only a leading python/python3 to sys.executable, so the nested name resolves through PATH. tools/gate-legs.json runs the `gotchas selftest` leg as `python3 ...`, and run-gates.sh:145 resolve_python tries `python3 python py`. That means a node where python3 and python are the MS-Store stub and only `py` works is a supported path. On such a node the grandchild exits 9009 at once, `; true` makes bash exit 0 before the 2s ceiling, `unobservable: past 2s` is never recorded, and the case reds for an environmental reason. The fix is sound: put a shlex-quoted sys.executable in the inner string, so backslashes in a Windows path stay literal inside single quotes, and assert the pidfile exists before judging liveness. | sound | - |
| 43 | failure-envelope | memory/builds/dLinkedLibrary/spec/2026-10-27-spec-TOOL-dLinkedLibrary-61.md:section 2 S2 | low | medium | confirmed | Spec 61 S2 (line 42) says stdout and stderr go to 'one temporary file under the scratch clone'. Unit 24 S3 (spec 24:48) defines the scratch clone as the clone of HEAD in which the leg's argv runs, so the file is an untracked file inside the tree being graded. The cited precedent, regen.py:290, uses `tempfile.TemporaryFile()` outside the tree. gate-fingerprint.sh:61 reads `git status --porcelain --untracked-files=all`, so a leg that reads untracked files does see the planted file. That can change the clean run's verdict or push a class to `unobservable`. This changes behaviour (contained), not just cosmetics, so I grade it medium rather than the finder's low. | sound | - |
| 44 | failure-envelope | memory/builds/dLinkedLibrary/spec/2026-10-27-spec-TOOL-dLinkedLibrary-64.md:section 2 S14 | low | low | confirmed | backlog.py:129 is `^(?=.*[A-Z])[A-Za-z0-9]+$` and :453 is `^[A-Za-z][A-Za-z0-9]*-[A-Za-z0-9]+-\d+$`. I ran `python -I -c` with both patterns: `.match` printed True for 'dLinkedLibrary\n' and True for 'TOOL-x-1\n'. backlog.py:459 uses GRANT_ID_RE.match. Spec 64 S14 (lines 86-88) says only 'checks against SLUG_RE ... GRANT_ID_RE', and AC11 (246-249) plants only `..` and `/` values. A builder who reuses `.match` therefore lets a trailing-newline value reach the join, which contradicts 'validated before any path join'. It is not traversal and the effect is contained. | sound | - |
| 45 | failure-envelope | memory/builds/dLinkedLibrary/spec/2026-10-27-spec-TOOL-dLinkedLibrary-56.md:section 5 'error / empty / loading states' | low | low | confirmed | `grep -n pipefail tools/run-gates/run-gates.test.sh` printed nothing. Spec 56 S3 (lines 45-47) writes `_mpb=$( region_nth ... \| tr -d '\r' )`, and the existing arm at run-gates.test.sh:3600-3605 runs `bash -c "$_mpb"...` without checking the slice's status or that it is non-empty. The pipeline's status is tr's, so an absent block gives an empty _mpb. check_dispatch_pause is then undefined, the output is a '127 127 ...' value mismatch, and spec 56 §5's claim that 'the canary's arm reports it' is false. The impact is a misleading diagnostic in a test only. | sound | - |
| 46 | failure-envelope | memory/builds/dLinkedLibrary/spec/2026-10-27-spec-TOOL-dLinkedLibrary-54.md:section 2 S3 | low | low | confirmed | region_sh's body, the canonical code at check-unattended.sh:211-216 per spec 18 S3, sets bad=1 on `index(ln,o)==1 && ln!=o`. That means a line beginning with '<!-- microformats -->' plus trailing text forces exit 3. check-microformats.sh:40-41 counts with `grep -cxF`, whole lines only, so it admits that file as 1/1. Spec 54 S3 (lines 49-51) names only 'a close above its open' as the exit-3 case on a pair the count admits. Today's awk at :48 uses `$0 == o` and grades such a file. So the second exit-3 cause goes unspecified, and the message may mislead the person fixing it. The exit-2 outcome itself is defensible. | sound | - |
