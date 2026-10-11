# Brief — dRemeasuredRender: gov's suites scrub their probes, and update re-measures what it rendered

**Serves:** research TOOL-dRemeasuredRender-1 DEPL-dRemeasuredRender-1 DEPL-dRemeasuredRender-2

The owner's prompt, verbatim, as handed to `/unattended --prompt` on node `d`, 2026-10-11. The value
was a path that named a readable file, so the file's content is the prompt. It came from
`C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-practical-borg-90829d/72a45fd5-0f33-45d8-8195-7c980ea738b9/scratchpad/prompt.txt`,
which holds the text below the rule of the inCMS record
`memory/builds/dCoiledTether/prompts/2026-10-11-prompt-ARCH-dCoiledTether-1-gov-handoff.md` on inCMS
branch `branch/gov-repull-tool-wiring-6bda54`. The bytes travel here, because the build folder is
the authorization and may not point at a file that can change after the run starts.

## The prompt

> Three defects an adopter pull exposed, found by the inCMS and NicoCares pull from gov 40a8b8c3 to b726385f on 2026-10-11. Repo: C:/projects/coding-governance (gov). Fetch first and start from the tip origin/main advertises; fad16fd3 when this was written. Each defect is gov's to fix: the adopters carry workarounds that each fix lets them delete.
>
> DEFECT 1 (tooling, gate-lint). The location-probe leg reds every adopter on gov's own shipped suites. The gate-lint spec that added this leg scoped it as "every bare site in the population is scrubbed in place". At fad16fd3 `python3 tools/gate-lint/sh_hygiene.py --location-probes`, with no registry and no pathspecs, reports 58 bare sites in 30 files, and ALL 30 are *.test.sh suites (tools/unattended/unattended.test.sh alone holds 8). Gov's own bar never sees them, because its row in tools/gate-legs.json passes memory/project/location-probe-waivers.txt and the pathspecs ":!*.test.sh" ":!memory/". The row tools/gate-lint/kit.toml emits for adopters passes neither. So every adopter that receives gov suites reds on gov's bytes, which it may not edit. inCMS and nc each receive six of them (check-wiring.test.sh, manifest-check.test.sh, marker-contract.test.sh, push-main.test.sh, unattended/check-unattended.test.sh, unattended/unattended.test.sh: 18 sites). Each adopter now declares those 18 in its own memory/project/location-probes.txt.
> Scope: scrub every bare site in place with the scrub the leg names, `(unset GIT_DIR GIT_WORK_TREE; ...)` opening the substitution. Then drop ":!*.test.sh" from gov's own row, so gov grades the class it ships. Keep ":!memory/". Do not change the registry grammar or the adopter row's argv.
> Acceptance: the no-registry, no-pathspec run above reports 0 GATED over gov's tree outside memory/. Gov's own row is green without the suite exclusion. Every touched suite passes when run directly, with GATE_SELFTESTS=1 where it is a held leg.
>
> DEFECT 2 (deployer, govkit update). A rendered row's receipt is never re-measured. When a row's kit renders it (`how == "adopter"`), update caps a diverged or stale verdict to "re-rendered" ("CAP at report; the adopter owns these bytes"). It then runs the [[regenerate]] argv, which rewrites the file. But the row's sha256, oid, commit and version, and its install.sums line, keep the PRE-pull bytes: only rows update writes itself go through the branch that sets sha256 from "the bytes that LANDED". Measured: after the pull, nc held 17 rendered rows (lexicon and unattended Skills, HYGIENE.md, TEMPLATE-SPEC.md, the BUILD-METHOD, ANNOTATION-STYLE and UNATTENDED-* guides, PLAYBOOK-TEMPLATE.md, the workflow renders, the playbook fixtures) whose install.sums named bytes git no longer stored. nc's wiring check reds on exactly that, and it had to be re-recorded by hand, twice now (once per pull). inCMS's rendered sums are stale the same way, ungated.
> Scope: after the regenerate argv runs, update re-measures each rendered row from the bytes that landed. It records sha256, oid and the install.sums line, plus commit and version for the vintage whose template rendered them, as written rows do. gov_oid stays gov's. A row whose render did not run, or refused, keeps its old record and says so.
> Acceptance: a fixture adopter with one rendered row. After `update --write`, install.json's sha256 and oid and install.sums name the rendered file's bytes, and `govkit check` agrees. The fixture reds on today's update.
>
> DEFECT 3 (deployer, govkit update). A hole whose probe grades a rendered artifact is reported undischarged by the run that is about to discharge it. update probes [[hole]] discharges BEFORE the regenerate, deliberately: the hole runner's docstring says it exists to "name an undischarged hole BEFORE it runs a regenerate that is bound to refuse on it". But lexicon's lexicon-ratified probe is `adopt-lexicon.sh --check`, which byte-compares .claude/skills/lexicon/SKILL.md. Probed between the engine write and the re-render, it fails. Measured in both adopters: update printed "HOLE lexicon: 'lexicon-ratified' is undischarged (probe exit 1)". The same run's verify said "lexicon: adopted -> adopted · exit 0 -> 0", and `govkit check --run-discharge` right after exits 0. An operator reads a false red.
> Scope: keep the early probe, since that early naming is its purpose. A hole that probed undischarged before the regenerate is probed again after it, and the run's report says which verdict stands. Only a hole still undischarged after the regenerate is reported as undischarged.
> Acceptance: a fixture hole whose probe passes only after regeneration is not reported undischarged at the end of `update --write`. One that still fails after it is. Both arms are observed red against today's update.
>
> Decided, so the run asks nothing: units are one per defect, plus whatever the method's discovery rule adds. Defect 1 drops ":!*.test.sh" rather than shipping the exclusion to adopters, because the leg's own header bans a spelling, not a population. Defects 2 and 3 both write govkit.py, so they are sequenced.
>
> Out of scope: the adopter side. inCMS and nc each delete their location-probes.txt rows, and stop re-recording rendered rows, at their next pull, as their own units. Also out: check-wiring's treatment of a live stale hooks copy as "ok" with a DIVERGES note, the registry grammar, and .githooks/pre-push.
>
> Lessons carried from gov's last runs: every pass commit stages memory/builds/<slug>/RUN.md with its --dispatch and --brief rows. Run python tools/codebase-map/gen_map.py --write after any rename or new function. Bump each touched kit version once, after the last move, and check the carriers with tools/check-kit-versions.sh and `govkit epoch --base <BASE>`. Re-stamp the kickoff manifest's last-audit when a watched path moves. New function names lead with a declared verb (`lexicon.py --suggest`), or the two-sided verb pin moves. Land through tools/push-main.sh, never --no-verify.

## The brief

### Goal
Fix three gov defects an adopter pull exposed: gov's shipped suites carry bare location probes that
red every adopter, `govkit update` leaves a rendered row's receipt naming pre-render bytes, and it
reports a hole undischarged that its own render then discharges.

### Items
1. Scrub every bare location probe in gov's tree outside `memory/`, and drop `:!*.test.sh` from gov's own leg row. [planned TOOL-dRemeasuredRender-1]
2. After the regenerate, `update` re-measures each rendered row's sha256, oid, commit, version and `install.sums` line from the landed bytes. [planned DEPL-dRemeasuredRender-1]
3. A hole probed undischarged before the regenerate is probed again after it, and only one still failing is reported undischarged. [planned DEPL-dRemeasuredRender-2]

### Acceptance
Item 1: `sh_hygiene.py --location-probes` with no registry and no pathspec reports 0 GATED outside
`memory/`, and gov's own row is green without the suite exclusion. Item 2: a fixture adopter with
one rendered row, after `update --write`, holds a receipt and `install.sums` naming the rendered
bytes, `govkit check` agrees, and the fixture reds at BASE. Item 3: a fixture hole that passes only
after the render is not reported undischarged, one still failing is, and both arms red at BASE.

### Gates
`shell hygiene (a location probe asked from a moved directory)` · `govkit selftest` · the guarded
legs each spec's §7 names; no merge bar inside a pass, and the bar once at the close.

### Non-goals
The adopter side: inCMS and nc deleting their `location-probes.txt` rows and their hand re-records.
check-wiring's treatment of a live stale hooks copy, the registry grammar, and `.githooks/pre-push`.

### Limitations
The `tools/unattended/` self-test suites are not run, under the owner's standing instruction of
2026-08-23. Units 2 and 3 are sequenced, both writing `tools/govkit/govkit.py`. Never `--no-verify`.

### Reuse
The scanner's own printed remedy is the scrub for item 1. For items 2 and 3, the regenerate loop in
`_cmd_update`, the written-row stamping rule beside it, `run_hole_probes`, and the self-test's
`check_update_safety` fixture builders. The recall query returned `DEPL-aHalvedInstall-1` (the early
hole probe) and `TOOL-bQuiltedLantern-1` (the regenerate declarations).

## Drawn from the session

none

## Owner confirmation

not asked — the brief draws on nothing outside the prompt
