# TOOL-aLightenedLoop-7 — the tracked idle-wake cadence retired: its conf key removed everywhere, `--wake` naming the base cadence, and the idle-wake help page's block marked not to run

**Status:** SPECCED · rev-1 · 2026-11-15 · node a · Tier-2 · base 5701fafd · streams tooling · order 7

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-14-prompt-TOOL-aLightenedLoop-7-cadence-drop.md](../prompts/2026-11-14-prompt-TOOL-aLightenedLoop-7-cadence-drop.md) | research | — |
| [2026-11-15-prompt-TOOL-aLightenedLoop-7-1-spec-writer.md](../prompts/2026-11-15-prompt-TOOL-aLightenedLoop-7-1-spec-writer.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

The merge bar at `9347f5848` redded two legs on TOOL-aLightenedLoop-2's changes. Its new
`.unattended.conf` key `KEEPALIVE_TRACKED_INTERVAL` is a new legacy home, and that list is
shrink-only. Its help page runs the driver by gov's path in a scratch adopter. The owner chose to
drop the tracked cadence rather than move the key to the policy catalogue
(`prompts/2026-11-14-prompt-TOOL-aLightenedLoop-7-cadence-drop.md`). This unit removes the key and
the job-replacement rule that existed only for it. It keeps `--wake`'s verdicts, reasons and their
order, and marks the page's block `run: no`. Unit 2's spec is CLOSED and frozen, so this unit
corrects its built code on top.

## 2. Scope (IN)

- **S1** — The key removed. `KEEPALIVE_TRACKED_INTERVAL` leaves the driver's init block and its one
  reader in `print_wake`, `tools/unattended/.unattended.conf.example`, `tools/unattended/kit.toml`'s
  `optional_keys`, this repo's `.unattended.conf`, the protocol §8 row in its template and render,
  the verbs carrier's `<c>` line in its template and render, `help/idle-wake.md`, `help/README.md`
  and the comment above the protocol's row in `tools/template-size-limits.txt`. Afterwards no
  tracked path outside `memory/builds/` spells it. Observed by AC1, AC4 and AC5.
  **Readers:**
  by name: `tools/unattended/unattended.sh` (the init block, `print_wake`'s comment and its `cad`
  test), `tools/unattended/unattended.test.sh` (the AC3 block), `tools/unattended/.unattended.conf.example`,
  `tools/unattended/kit.toml`, `.unattended.conf`, `tools/unattended/PROTOCOL.template.md`,
  `memory/guides/UNATTENDED-PROTOCOL.md`, `tools/unattended/VERBS.template.md`,
  `memory/guides/UNATTENDED-VERBS.md`, `help/idle-wake.md`, `help/README.md` and
  `tools/template-size-limits.txt`, each found by a git grep for the key at the base commit.
  by value: `print_wake` alone tests and assigns it
  (`tools/unattended/unattended.sh@8a6a0fc85d6a:8830`). `tools/policy/policy.py#derive_legacy_homes`
  derives one row from every key `.unattended.conf` assigns, which is the row the bar redded on, and
  it reads no key by name.
- **S2** — The cadence field. `--wake`'s line keeps §4's grammar, and `<cadence>` is always
  `KEEPALIVE_INTERVAL`, or `undeclared` when that is blank. The open-task count no longer moves it.
  The verdicts, the reasons and their order are unit 2's, byte for byte. Observed by AC1, AC2, AC3
  and AC4.
- **S3** — The job-replacement rule retired. Its three carriers lose it: the Skill's sentence on a
  differing cadence, the verbs carrier's idle-wake step bullet on it, and the help page's paragraph
  on it. The rule has no case left, because the job is created at `KEEPALIVE_INTERVAL` and the field
  now always prints that value. Observed by AC6 and AC7.
  **Readers:**
  by name: `tools/unattended/SKILL.template.md`, `.claude/skills/unattended/SKILL.md`,
  `tools/unattended/VERBS.template.md`, `memory/guides/UNATTENDED-VERBS.md` and
  `help/idle-wake.md`, the only tracked paths outside the build records that spell the rule.
  by value: NO VALUE READERS, because the rule is an instruction to the agent, and no gate, suite
  or script compares, counts or derives anything from its text.
- **S4** — The help page. `help/idle-wake.md`'s "The cadence" section states the base cadence, and
  its example block carries the `run: no` marker the other pages use for a block that runs a kit by
  its path in gov's checkout. The example's printed cadence becomes this repo's
  `KEEPALIVE_INTERVAL`. `help/README.md`'s entry stops naming the key. The page's anchor line is not
  touched. Observed by AC6.
- **S5** — The suite. The `--wake` AC3 block of `tools/unattended/unattended.test.sh` is rewritten to
  the base-cadence answer: four `hit` lines replace four. The assertion floor moves by the net
  count, which is 0. NOT OBSERVED by a criterion: a pass runs no suite. The main loop observes the
  `New arm:` line RED and then GREEN at the close.
- **S6** — The records the edit owes. The kickoff manifest's `last-audit` is re-stamped, because its
  `watch:` list names `.unattended.conf`. No size row moves. Observed by AC7 and AC8.

## 3. Non-goals (OUT)

- No change to `--wake`'s verdicts, reasons or their order, nor to `--wake`'s header line, its
  `VERB_REQUIRES` row or its exit codes.
- No new key anywhere, and no catalogue key. `KEEPALIVE_INTERVAL` stays as it is: its conf line, its
  example line, its protocol row and its Skill render are untouched.
- No size row lowered. The protocol and Skill rows TOOL-aLightenedLoop-2 raised keep 68216 and
  10744, and the headroom this unit frees stays. Lowering a row is the owner's
  (`tools/template-size-limits.txt@73d15c74e2da:16-24`).
- No edit to unit 2's spec, ledger or red-fix record. They are frozen records.
- No kit version. The lander mints them.
- No change to the feature dossier. `memory/map/features/unattended.md@8332be62424e:83-85` names
  `--wake` and the pair, and neither the key nor the replacement rule, so it is already true.
- Nothing under `memory/builds/dDeclaredLoop/`.

### Edges

- **consumes-from** external — TOOL-aLightenedLoop-2's built `--wake` at `5701fafd3`, its probe
  fixture and its first acceptance ledger. Its spec is CLOSED, so this unit reads it and never
  edits it.

## 4. Design

### Evidence

Read at `5701fafd3`, the base. Blob ids are of that commit.

- The driver declares the key blank in its init block
  (`tools/unattended/unattended.sh@8a6a0fc85d6a:686`). `print_wake` sets
  `cad=${KEEPALIVE_INTERVAL:-undeclared}` at `:8829`, then overrides it at `:8830` with the tracked
  key when the open count is above 0. Its comment names the key at `:8778-8779` and the agent's job
  replacement at `:8785-8786`, and `:8821` says the tasks are counted because "the cadence reads the
  count". The header's `--wake` line at `:10` says "then the cadence due", which stays true.
- `KEEPALIVE_INTERVAL` is not on the init block and is read only through the `:-undeclared`
  expansion. Unit 2's ledger records a conf with no `KEEPALIVE_INTERVAL` line at all exiting 0
  under `set -u` (`build/2026-11-14-build-TOOL-aLightenedLoop-2-1-acceptance-ledger.md`, AC3).
- `tools/policy/policy.py#derive_legacy_homes` yields one `owner-policy` row per key assigned in each
  tracked root `.*.conf`. `tools/policy/policy.py#check_legacy_homes` reports a derived row the
  committed list lacks as "stale list" and one the base's list lacks as "a new legacy home". Both of
  the bar's `arm_legacy_homes` lines come from `.unattended.conf@97de12ed4c29:135`, so removing that
  assignment clears both. The conf example is not a home, since only tracked root confs are read.
- `tools/govkit/docs_leg.py#run_page_commands` skips a block whose marker line matches
  `RUN_NO_RE` and counts it as marked. `tools/govkit/docs_leg.py#check_page_runs` exits 2 with a
  `REFUSED` line when the pages it was given ran no command at all. The marker string is the one
  `help/agent-limit.md@3146e0d3103f:26` carries. Probed on 2026-11-15 at the base,
  `python tools/govkit/docs_leg.py --run --page help/idle-wake.md` printed the bar's finding,
  `docs: RUN help/idle-wake.md:61 ... exited 127`.
- `python tools/govkit/docs_leg.py --fingerprints` printed `verb:unattended.sh:--wake ef8efa49
  help/idle-wake.md` on 2026-11-15. This unit edits neither the driver's header nor the page's anchor
  line, `help/idle-wake.md@430123ef74db:14`.
- The job-replacement rule lives in three carriers: `tools/unattended/SKILL.template.md@5f555a882c8e:19-20`,
  `tools/unattended/VERBS.template.md@f68d5efd8798:472-474` and
  `help/idle-wake.md@430123ef74db:55-57`. `git grep` finds no gate or suite line that reads any of
  them: neither `tools/unattended/check-unattended.sh` nor `tools/unattended/unattended.test.sh`
  spells "cadence" outside the `--wake` block.
- The suite's AC3 block is `tools/unattended/unattended.test.sh@b15f24c75c99:9859-9871`, four `hit`
  lines, inside shard region 4 (opened at `:8035`). Unit 2 raised no floor for its `--wake` arms:
  `FLOOR_ASSERTIONS` at `:19680` and `FLOOR_SHARD_4` at `:19900` carry no TOOL-aLightenedLoop-2 line.
- Unit 2's commit `817cda253` is on this branch alone (`git branch -a --contains 817cda253`), so no
  install has the key and no upgrade step is owed.
- The renders measured 10744 bytes for the Skill and 68216 for the protocol, CR-stripped, and 97882 <!-- PINNED 2026-11-14 -->
  for the verbs carrier (PINNED, 2026-11-15). The templates and their renders compare equal with
  `cmp` for the verbs and the protocol.

### Data model

The one stdout line keeps unit 2's grammar:

```text
unattended-wake: <slug> · HEALTHY · tasks <n> open · cadence <cadence>
unattended-wake: <slug> · FULL · <reason> · tasks <n> open · cadence <cadence>
```

- `<cadence>` is the value of `KEEPALIVE_INTERVAL`, or the literal `undeclared` when that is blank or
  unset. It is the same for every `<n>`, `unknown` included.
- `<n>`, `<reason>`, the reason order and the exit codes are unit 2's, unchanged.

### The driver

- `:686` loses `KEEPALIVE_TRACKED_INTERVAL="";` and nothing else. `ANCHOR_SCOPE` stays on that line,
  which the source-level arm reads with `-A1` from the line above (`:683-684`).
- `:8830` is deleted. `:8829` stays as written.
- `:8778-8779` read: "The same line names the cadence due: KEEPALIVE_INTERVAL, or `undeclared` when
  that is blank, whatever the registry holds (TOOL-aLightenedLoop-7). It writes nothing; the claim
  read refreshes the private claim cache only, as `--resume`'s does."
- `:8785-8786` read: "WHAT IT DOES NOT CHECK: which units are open (an idle tree reads FULL with
  none)."
- `:8821`'s reason becomes "because the line prints the count".

### The carriers' text

- Skill template: the sentence "A `cadence` other than your job's replaces the job, as the verbs
  file says." is deleted, and the paragraph re-wraps under 100 columns.
- Verbs template: `:146` reads "  `<c>`: `KEEPALIVE_INTERVAL`, or `undeclared` when it is blank." The
  three-line bullet at `:472-474` is deleted.
- Protocol template: the row at `:492` is deleted. §5's sentence at `:391` stays.
- The three renders are re-rendered with `bash tools/unattended/adopt-unattended.sh`, never edited by
  hand.
- `.unattended.conf`: the comment and assignment at `:132-135` and the blank line after them are
  deleted. The example loses `:137-139` and the blank line after them in the same way.
- `tools/unattended/kit.toml@b40dc2ff4c45:183`: `, "KEEPALIVE_TRACKED_INTERVAL"` leaves the list.
- `tools/template-size-limits.txt@73d15c74e2da:167` reads "`--wake` first, and section 8's row for
  its tracked-cadence key, which TOOL-aLightenedLoop-7 retired." wrapped at 100 columns as the file
  is. The row value under it does not move.

### The help page

- "The cadence" (`:49-57`) becomes one paragraph: "`tasks <n> open` counts the registered tasks
  (`--register-task`) not yet released, or reads `unknown` when a heartbeat could not be read. The
  cadence is `KEEPALIVE_INTERVAL` from `.unattended.conf`, the cadence the run's first act schedules
  the job at, or `undeclared` when that is blank. The task count does not move it."
- "Example" gains `<!-- run: no — runs a kit by its path in gov's checkout, absent from a scratch adopter -->`
  on the line directly above its fence. The block's comment line becomes
  `# unattended-wake: aBuild · HEALTHY · tasks 1 open · cadence every 10 minutes (cron 3-59/10 * * * *)`,
  this repo's `KEEPALIVE_INTERVAL` (`.unattended.conf@97de12ed4c29:130`).
- `help/README.md@f455dd8e7091:17` ends "... and the cadence it names." in place of the clause naming
  the key.

### The suite

The AC3 block becomes:

```bash
# AC3 — the cadence is KEEPALIVE_INTERVAL whatever the registry holds, and `undeclared` when that is
# blank; TOOL-aLightenedLoop-7 retired the tracked cadence.
build_wake_fixture
hit "$(run --wake tRun --keepalive-id k1)" "· tasks 1 open · cadence every 10 minutes"
run --release-task tRun --task wf >/dev/null
hit "$(run --wake tRun --keepalive-id k1)" "· tasks 0 open · cadence every 10 minutes"
build_wake_fixture
printf 'KEEPALIVE_INTERVAL=""\n' >> .unattended.conf
hit "$(run --wake tRun --keepalive-id k1)" "· tasks 1 open · cadence undeclared"
run --release-task tRun --task wf >/dev/null
hit "$(run --wake tRun --keepalive-id k1)" "· tasks 0 open · cadence undeclared"
```

The `rm -rf "$WK_REG" "$WK_DIR"` and `reset_tree` lines after it stay. Four `hit` lines replace four,
so neither `FLOOR_ASSERTIONS` nor `FLOOR_SHARD_4` moves. A builder whose block differs moves both by
its net count, with a comment line in the file's own shape. The block cannot spell the retired key,
so it cannot show the key being ignored. AC1 shows that in a fixture outside `tools/`.

### The probe fixture

The builder saves unit 2's `wakefix.sh` (`spec/2026-11-14-spec-TOOL-aLightenedLoop-2.md`, §4, "The
probe fixture") with one change: `846d51d39` becomes `5701fafd3`, so `u0/` holds this unit's base
driver. Unit 2's names `run`, `run0`, `<reg>`, `<age>`, `<stale-beat>`, `<orphan>`, `<remote>` and
`<rec>` stand as that section defines them.

### Inventory

This unit mints no identifier. It retires one conf key, S1's.

### Files touched (estimate)

- `tools/unattended/unattended.sh`
- `tools/unattended/unattended.test.sh`
- `tools/unattended/SKILL.template.md`
- `.claude/skills/unattended/SKILL.md`
- `tools/unattended/VERBS.template.md`
- `memory/guides/UNATTENDED-VERBS.md`
- `tools/unattended/PROTOCOL.template.md`
- `memory/guides/UNATTENDED-PROTOCOL.md`
- `tools/unattended/.unattended.conf.example`
- `tools/unattended/kit.toml`
- `.unattended.conf`
- `memory/guides/SESSION-KICKOFF.md`
- `tools/template-size-limits.txt`
- `help/idle-wake.md`
- `help/README.md`

`memory/guides/SESSION-KICKOFF.md` is touched for its `last-audit` re-stamp alone. Its `watch:` list
names `.unattended.conf` (`memory/guides/SESSION-KICKOFF.md@43b625791c20:7`).

### Alternatives rejected

- **Keep the job-replacement rule.** It would still fire if the owner edited `KEEPALIVE_INTERVAL`
  mid-run. But the Skill renders that key at adoption, so such an edit is a re-render, and the run's
  first act schedules the job from the render. The rule would be prose for a case the run does not
  meet. Brief item 1 also names the Skill as a carrier, and the switch sentence is the Skill's only
  cadence text.
- **Drop the `cadence` field from the line.** The brief keeps it, and dropping it would move every
  `--wake` byte that unit 2's arms and ledger pin.
- **Retire the AC3 block and lean on AC1's line.** AC1 pins only the open-task, declared case. The
  `undeclared` answer with a task open, the case the removed branch used to own, would go unpinned.
- **Keep the key in the suite as an ignored conf line.** It would keep the brief's grep over `tools`
  red, and an arm for a key no code reads guards nothing.

## 5. Production-readiness checklist

- security — No new write path or surface. The change deletes one conf read and one branch.
- perf / scale — One fewer test per `--wake` call; no measurable change.
- error / empty / loading states — A blank or absent `KEEPALIVE_INTERVAL` prints `undeclared`, as
  before. A conf that still assigns the retired key is sourced and never read, so it changes
  nothing.
- observability — The `cadence` field still names the value the job runs at.
- risks — Removing the replacement rule leaves no carrier for a job whose cadence differs from the
  conf. The Alternatives say why that case does not arise. Editing the comment above a size row
  touches an owner-held file. The row value does not move, and AC8 shows it.
- testing — AC1 to AC8 run in the probe fixture or as greps. §7 declares the rewritten arm.
- migration — None owed. Unit 2's commit is on no other branch, so no install carries the key.
- user docs — `help/idle-wake.md` and `help/README.md`, S4.

## 6. Acceptance criteria

- **AC1** — When `echo 'KEEPALIVE_TRACKED_INTERVAL="every 30 minutes"' >> .unattended.conf` and `<reg>`
  run in a fresh probe fixture, `run --wake tWake --keepalive-id k1` exits 0 and prints exactly
  `unattended-wake: tWake · HEALTHY · tasks 1 open · cadence every 10 minutes`. The same call through
  `run0` prints `... cadence every 30 minutes`, which is the base's answer.
  Red when: the built driver still reads the retired key.
- **AC2** — When `<reg>` runs in a fresh probe fixture and then `run --release-task tWake --task wf`,
  `run --wake tWake --keepalive-id k1` prints a line ending `· tasks 0 open · cadence every 10 minutes`.
  When `sed -i 's/^KEEPALIVE_INTERVAL=.*/KEEPALIVE_INTERVAL=""/' .unattended.conf` runs in a fresh
  fixture before `<reg>`, the line ends `· tasks 1 open · cadence undeclared`, and after the release
  `· tasks 0 open · cadence undeclared`. Every call exits 0.
  Red when: the cadence depends on the task count, or a blank base cadence prints anything but
  `undeclared`.
- **AC3** — When unit 2's AC1 setup and each of its AC2 staged breaks are applied to a fresh probe
  fixture, `run0 --wake tWake --keepalive-id <id>` and `run --wake tWake --keepalive-id <id>` print
  the same line, byte for byte, and both exit 0. `<id>` is `k2` for the `holder` break and `k1`
  otherwise. The lines read `HEALTHY` for the setup and `FULL` with each break's reason, as unit 2's
  first acceptance ledger records them.
  Red when: a verdict, a reason, their order or any other byte of a line moved.
  cost: about three minutes, twelve fixtures.
- **AC4** — When `git diff -U0 5701fafd3 -- tools/unattended/unattended.sh | grep -E '^[-+]' | grep -vE '^(---|[+][+][+])' | grep -vE '^[-+][[:space:]]*#'`
  runs, it prints three lines: the init line at `:686` removed and re-added without
  `KEEPALIVE_TRACKED_INTERVAL="";`, and the `if` line at `:8830` removed.
  `python tools/govkit/docs_leg.py --fingerprints` still prints `verb:unattended.sh:--wake` with
  `ef8efa49` and `help/idle-wake.md`.
  Red when: a reason row, a `printf` line or the header line moved.
- **AC5** — When `git grep -n KEEPALIVE_TRACKED_INTERVAL -- tools help .claude .unattended.conf memory/guides memory/map`
  runs, it prints nothing, and `git grep -l KEEPALIVE_TRACKED_INTERVAL` lists only paths under
  `memory/builds/`. `python tools/policy/policy.py lists --check` prints no line holding
  `KEEPALIVE_TRACKED_INTERVAL`.
  Red when: a carrier still names the key, or `.unattended.conf` still assigns it.
- **AC6** — When `python tools/govkit/docs_leg.py --run --page help/idle-wake.md` runs, it prints one
  `docs: run · ` line naming the page, the marked block's line and
  `run: no — runs a kit by its path in gov's checkout, absent from a scratch adopter`, then a summary
  ending `0 findings`, and no `docs: RUN help/idle-wake.md` line. It exits 2 with its
  `REFUSED` line, because a page whose every block is marked runs nothing; the leg runs every page
  and does not refuse. `grep -c 'every 30 minutes' help/idle-wake.md` and
  `grep -c 'replaces\|deletes that job' help/idle-wake.md` each print 0.
  `grep -c '(idle-wake.md)' help/README.md` prints 1.
  Red when: the marker is absent or not directly above the fence, or the page still describes the
  switch.
  figure: the block's line number is DERIVED from the built page.
- **AC7** — When `bash tools/unattended/adopt-unattended.sh --check` runs, it exits 0.
  `cmp tools/unattended/VERBS.template.md memory/guides/UNATTENDED-VERBS.md` and
  `cmp tools/unattended/PROTOCOL.template.md memory/guides/UNATTENDED-PROTOCOL.md` print nothing.
  `grep -c 'other than your job' .claude/skills/unattended/SKILL.md memory/guides/UNATTENDED-VERBS.md`
  prints 0 for each file. `grep -c 'unattended.sh --wake ' .claude/skills/unattended/SKILL.md` prints
  at least 1. `grep -c '<c>.: .KEEPALIVE_INTERVAL., or .undeclared. when it is blank[.]$' memory/guides/UNATTENDED-VERBS.md`
  prints 1. `bash skills/session-kickoff/manifest-check.sh` reports no stale `last-audit`.
  Red when: a render was hand-edited or not re-rendered, the switch survives in a carrier, or the
  conf moved without the manifest's re-stamp.
- **AC8** — When `git diff -U0 5701fafd3 -- tools/template-size-limits.txt | grep -E '^[-+][^-+#]'`
  runs, it prints nothing. `tr -d '\r' < .claude/skills/unattended/SKILL.md | wc -c` prints at most
  10744, and the same over `memory/guides/UNATTENDED-PROTOCOL.md` prints at most 68216.
  Red when: a row value moved, or a render grew past its row.
  figure: 10744 and 68216 are PINNED, the rows at `5701fafd3`.

## 7. Gates

`policy check` · `help page commands` · `docs` · `unattended kit gate` · `unattended skill wiring` · `unattended skill size` · `unattended protocol size` · `kickoff-manifest ratchet` · `memory hygiene` · `scratch-guard self-test` · `tier2-review self-test` · `check-wiring self-test` · `lexicon naming predicates` · `policy fixtures` · `recall floor` · `recall floor arms`

The first two are the bar's two reds this unit clears, and the next six grade its change directly.
The last eight are owed because a path of the estimate trips their guard, by
`python tools/check-spec-tokens.py --legs-for` at `5701fafd3`, less the broad guards. The driver
suite runs in the unattended kit's pooled tier, so the main loop runs it with the bar at the close.
No leg is added.

New arm: tools/unattended/unattended.test.sh · covers AC2 · the rewritten `--wake` AC3 block, staged with the `:-undeclared` default deleted from `print_wake`'s `cad=` line for its two `undeclared` hits, and with a line after it giving `cad` another value when `n` is above 0 for its two `tasks 1 open` hits · none

What this arm does not check: that the retired key is ignored, since the suite cannot spell it,
which AC1 observes once in a fixture; and the agent's scheduling, an act no script observes.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-15 · initial draft.

## 10. Reuse audit

No existing seam fits, and none is needed: the unit deletes a key, a branch and a rule, and edits
text in place. `python tools/codebase-map/reuse_lookup.py "retire an optional conf key from the
unattended kit and every carrier that names it"` ranked name stems only (`key`, `resolve_kit_dir`,
`load_conf`, `read_conf_key`), none a seam for a retirement. The rewritten arm extends
`build_wake_fixture` and `hit` in place, and the probe fixture is unit 2's `wakefix.sh` with its
base sha moved. Of the task's named seams, `check_staged_render`, `check_index_input`,
`derive_spec_token_key`, `runLiveness` and `DRIVER_STEPS` are not touched, since no item reaches the
index generator, the spec-token cache, the stop-guard or the unit driver. Recall's nearest records
were this unit's own brief, unit 2's bar-fix brief, and TOOL-aProbedUnit-6, whose `REVIEW_ROUNDS`
addition names the same five places a conf key lives: the conf, the example, `kit.toml`'s
`optional_keys`, the protocol row and the driver.

Recall terms used: `python tools/memory-recall/query.py "how was an optional unattended conf key
retired from the driver, the example, kit.toml and the carriers" --terms "retire conf key
optional_keys legacy home shrink-only catalogue KEEPALIVE_INTERVAL cadence idle-wake run: no"`
