# PLAY-dOrderedCharter-77 — the close bar's own product reds, each leg left green by the narrowest fix that leg demands

**Status:** CLOSED · rev-2 · 2026-11-10 · node a · Tier-2 · base 51cd8b402 · streams playbook · order 37 · advances PLAY-dOrderedCharter-38

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-PLAY-dOrderedCharter-1-agent-ledger.md](../build/2026-10-25-build-PLAY-dOrderedCharter-1-agent-ledger.md) | journal | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-5 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-10 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-16 PLAY-dOrderedCharter-17 PLAY-dOrderedCharter-18 PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-22 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-24 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-27 PLAY-dOrderedCharter-28 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-35 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-37 PLAY-dOrderedCharter-39 PLAY-dOrderedCharter-40 PLAY-dOrderedCharter-41 PLAY-dOrderedCharter-42 PLAY-dOrderedCharter-43 PLAY-dOrderedCharter-44 PLAY-dOrderedCharter-45 PLAY-dOrderedCharter-46 PLAY-dOrderedCharter-47 PLAY-dOrderedCharter-48 PLAY-dOrderedCharter-49 PLAY-dOrderedCharter-50 PLAY-dOrderedCharter-51 PLAY-dOrderedCharter-52 PLAY-dOrderedCharter-53 PLAY-dOrderedCharter-54 PLAY-dOrderedCharter-55 PLAY-dOrderedCharter-61 PLAY-dOrderedCharter-62 PLAY-dOrderedCharter-63 PLAY-dOrderedCharter-64 PLAY-dOrderedCharter-65 PLAY-dOrderedCharter-67 PLAY-dOrderedCharter-68 PLAY-dOrderedCharter-69 PLAY-dOrderedCharter-70 PLAY-dOrderedCharter-71 PLAY-dOrderedCharter-72 PLAY-dOrderedCharter-73 PLAY-dOrderedCharter-74 PLAY-dOrderedCharter-75 PLAY-dOrderedCharter-76 |
| [2026-11-10-build-PLAY-dOrderedCharter-77-1-builder-return.md](../build/2026-11-10-build-PLAY-dOrderedCharter-77-1-builder-return.md) | journal | — |
| [2026-11-10-build-PLAY-dOrderedCharter-77-deviation-771.md](../build/2026-11-10-build-PLAY-dOrderedCharter-77-deviation-771.md) | deviation | — |
| [2026-11-10-build-PLAY-dOrderedCharter-77-deviation-772.md](../build/2026-11-10-build-PLAY-dOrderedCharter-77-deviation-772.md) | deviation | — |
| [2026-11-10-build-PLAY-dOrderedCharter-77-ledger.md](../build/2026-11-10-build-PLAY-dOrderedCharter-77-ledger.md) | journal | — |
| [2026-11-10-prompt-PLAY-dOrderedCharter-77-1-spec-writer.md](../prompts/2026-11-10-prompt-PLAY-dOrderedCharter-77-1-spec-writer.md) | journal | — |
| [2026-11-10-prompt-PLAY-dOrderedCharter-77-2-spec-writer.md](../prompts/2026-11-10-prompt-PLAY-dOrderedCharter-77-2-spec-writer.md) | journal | — |
| [2026-11-10-prompt-PLAY-dOrderedCharter-77-3-spec-writer.md](../prompts/2026-11-10-prompt-PLAY-dOrderedCharter-77-3-spec-writer.md) | journal | — |
| [2026-11-10-prompt-PLAY-dOrderedCharter-77-4-spec-writer.md](../prompts/2026-11-10-prompt-PLAY-dOrderedCharter-77-4-spec-writer.md) | journal | — |
| [2026-11-10-prompt-PLAY-dOrderedCharter-77-build-brief.md](../prompts/2026-11-10-prompt-PLAY-dOrderedCharter-77-build-brief.md) | journal | — |
| [2026-11-10-prompt-PLAY-dOrderedCharter-77-pin-brief.md](../prompts/2026-11-10-prompt-PLAY-dOrderedCharter-77-pin-brief.md) | research | — |
| [2026-11-10-prompt-PLAY-dOrderedCharter-77-pin-lines-brief.md](../prompts/2026-11-10-prompt-PLAY-dOrderedCharter-77-pin-lines-brief.md) | research | — |
| [2026-11-10-prompt-PLAY-dOrderedCharter-77-spec-brief.md](../prompts/2026-11-10-prompt-PLAY-dOrderedCharter-77-spec-brief.md) | research | — |
| [2026-11-10-prompt-PLAY-dOrderedCharter-77-tokens-brief.md](../prompts/2026-11-10-prompt-PLAY-dOrderedCharter-77-tokens-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

The close's full bar over `3c63fe888` failed sixteen legs, and a read-only attribution found fifteen of
them this build's own. The main loop cleared the record-only offenders at `de36424bf` and `51cd8b402`.
This unit is the rest: every offender whose fix writes under `tools/`, `skills/` or `help/`, batched as
the build method batches minors, so that each leg in section 6's table reads green after one pass. It
changes no behaviour a leg does not demand, and it records the three acceptance observations other
CLOSED units still owe.

## 2. Scope (IN)

- **S1** — Shell hygiene. The fork idioms this branch added take their no-fork forms, so the
  `shell hygiene (a fork spent on builtin work)` scan measures each (file, class) at the count
  `memory/project/spawn-idiom-sites.txt` already declares, and the registry is not edited.
  `skills/session-kickoff/manifest-check.test.sh`: the four `$(dirname …)` at lines 1065, 1252, 1271
  and 1272 take `${CHECK%/*}` and `${mm_src%/*}`, the `printf` substitution at 1088 takes `printf -v`,
  and the `$(cat …)` at 1220 takes `$(<…)`. `tools/agent-instructions/adopt-agent-instructions.test.sh`:
  the `$(cat …)` at 82 takes `$(<…)` and the `echo … | grep -q` at 86 takes `[[ $out == *…* ]]`.
  `tools/check-template-size.test.sh`: the `$(dirname …)` at 229 takes `${_hp%/*}`. The scan's own
  per-file count is the arbiter: where a line named here proves to predate the branch, the branch's
  other site of that class converts instead. Observed by AC1.
- **S2** — Install prefix, the literal kit paths. Each kit path this branch spelled derives instead,
  by the form the file's neighbours already use:
  - `skills/session-kickoff/manifest-check.test.sh` lines 1254, 1272 and 1284, and the `mkdir` lines
    beside them, spell the fixture's kit through a variable holding its home, as `mp_kit` at line 1227
    does.
  - `tools/check-template-size.test.sh` line 225, and lines 229 and 230 that join the same home, spell
    the policy kit's home through one variable.
  - `tools/playbook/overlay.py`: `arm_adopter_key` computes the guarded list's path where it writes it,
    from `resolve_kit_dir("policy", "guard.py", KIT_DIR)` and `git rev-parse --show-prefix` there, the
    derivation `tools/policy/guard.py#read_guarded_paths` makes. The module holds no `FX_GUARDED`
    constant after the pass.
  - `tools/playbook/pins.py#arm_spelling` writes the map at `iu.derive_kit_rel(SPELLING_MAP)`.
  - `tools/playbook/practice_census.py#read_census_tree` reads the registry at
    `render_playbook.resolve_declaration_paths`'s answer and the agents under
    `resolve_kit_dir("roles", "check_roles.py", KIT_DIR)`, as `tools/playbook/load_sets.py` line 587
    does. Its `PLANTS` spell the fixture path under `fx/`, a root that is no prefix.
  - `tools/playbook/render_playbook.py#check_map_arms` spells its fixture documents under `agents/`,
    which is no kit's home.
  - `tools/roles/render_agents.py`'s arm 20 joins the fixture's playbook home through a variable.
  Observed by AC2.
- **S3** — Install prefix, the five Skill envelopes. `tools/check-install-prefix.sh`'s rule 3 already
  exempts a Skill directory, an operand with a dot-directory segment, and its operand split omits `[`,
  so an envelope line `[.claude/skills/<kit>/SKILL.md · …]` reads `[.claude` and counts. The split
  gains `[`. No template changes, and the gate gains no waiver (section 8 F1). The suite gains the arm
  section 7 names. Observed by AC3.
- **S4** — Harness arms. `tools/check-template-size.test.sh` gains an `expect_out` beside A25 asserting
  check 8 branch 1's own remedy sentence whole, the one opening `Lower the cap to CODEX_MAX or under`,
  over the 40960 cap A25 already builds. Observed by AC4.
- **S5** — Dead-path carriers. `tools/dead-path-waivers.txt` gains one row per line naming the harness's
  auto-memory index, eight in all: `skills/session-kickoff/manifest-check.test.sh` line 1276,
  `tools/playbook/memory_index.py` lines 9, 141, 165 and 188, and `tools/playbook/render_playbook.py`
  lines 2161, 2187 and 2196. Each row is `<path> TAB 1 TAB <line text> TAB <reason>`, the path through
  `{prefix}/` where it sits under the tool root, as the rows of `92e3bab9e` are. The reason states that
  the name is the agent harness's own index, written outside this repository, and not the file of that name this
  repository once tracked. Observed by AC5.
- **S6** — Remote literals. `tools/playbook/overlay.py` gains `FX_REMOTE = "ori" "gin"`, assembled as
  `tools/check-remote-literals.sh` assembles its `N`, and `arm_policy_at_head` spells the remote, its
  tracking ref and its `HEAD` ref through it at lines 678 to 680. Observed by AC6.
- **S7** — Govkit selfcheck. `tools/govkit/registry.toml` gains an `[[exempt]]` row for
  `skills/session-kickoff/card-compaction.fixture.sh`: the fixture drives two live headless sessions
  and a compaction, so the main loop runs it live and no target receives it.
  `tools/govkit/entries/push-main.kit.toml` line 93's comment names `adopter nc` and the record id
  `TOOL-aRepatriatedFork-5` in place of the adopter's name. Observed by AC7.
- **S8** — The three legs no target can carry. `core selftest`, `tags positional selftest` and
  `tags bundle selftest` move from `tools/playbook/kit.toml`'s `[[gate_leg]]` rows to gov-only
  `[[exempt_leg]]` rows of `tools/govkit/registry.toml`, each with its `why`, as
  `instruction units selftest` and `instruction edits selftest` sit (section 8 F2). Their rows in
  `tools/gate-legs.json` stay, so gov's bar runs them. Observed by AC8 and AC9.
- **S9** — The scratch install's stub answers. `tools/govkit/matrix.py` stubs each placeholder with
  `stated`, or `- stated` where its default is a bullet, in place of
  `stated for the scratch install`. Substituted, that phrase makes the `[land]` practice line 201
  characters, past the 200 a one-line rule may take where no policy kit answers, so `apply` refuses
  and renders no region (section 8 F4). Observed by AC9.
- **S10** — The render selftest's decode error. The cross-os arm of
  `tools/playbook/render_playbook.py#run_selftest`, lines 2625 to 2631, narrows the target's own
  `deploy.toml` by inserting `ci_file`, `gate_runner`, `id_families` and `memory_disciplines` after
  `[answers]`, and its loop prepends the block-exclusion key. A `deploy.toml` that already sets any of them, as the matrix's scratch install does,
  then fails to parse with `Cannot overwrite a value`, a traceback. The narrowing first takes out each
  line of that text setting a key it then sets. Observed by AC10.
- **S11** — The shipped render selftest at an install lacking a sibling kit.
  `tools/playbook/adopt-playbook.sh --selftest` gains `check_sibling_kit <home> <anchor>`, which exits 0
  where the kit's own `policy_value.resolve_kit_dir` finds the kit. Each of its four plant blocks first
  checks the kits its arms reach, and where one does not resolve prints
  `UNARMED — the <block> plants: no <home> kit in this install` and runs none of that block's arms. At
  HEAD the reaches are: the layer block, `memory-tree` (`tools/playbook/check_layers.py@b68f9e5c:106`, at import);
  the tag block, `memory-tree` (`tools/playbook/tag_index.py@0fea0fdf:479`); the edge block, `roles`
  (`tools/playbook/edge_grammar.py@82484637:372`); the load-set block, `roles` and `policy`
  (`tools/playbook/load_sets.py@ddcdb92d:132`, `tools/playbook/load_sets.py@ddcdb92d:339`). Observed by AC11 and AC9.
- **S12** — Docs. `tools/govkit/usage.toml` gains four `[[usage]]` rows of shape `verb`:
  `build_records.py#new`, `instruction_units.py#envelopes`, `instruction_units.py#drive` and
  `load_sets.py#derive`, each `id` `script:{prefix}/<kit>/<file>#<verb>` with its `entry`, `verb` and
  the flags its own parser declares, a value-taking flag spelled with a trailing `=`. `help/charter.md`
  and `help/roles.md` each gain the anchors of the rows their commands show, one page per row, outside
  a fence, at the fingerprint `python tools/govkit/docs_leg.py --fingerprints` prints. Observed by AC12.
- **S13** — Lexicon. Three names lead with a declared verb, each answered `OK` by
  `python tools/lexicon/lexicon.py --suggest` at design: `ask` in
  `skills/session-kickoff/card-compaction.fixture.sh` is renamed `run_claude`, and `fold_text` and
  `strip_text` in `tools/playbook/pins.py` are renamed `derive_folded_text` and `derive_stripped_text`,
  with every call site. Observed by AC13.
  **Readers:** by name: `tools/playbook/pins.py`, `tools/playbook/overlay_rows.py` and
  `skills/session-kickoff/card-compaction.fixture.sh`, the only files spelling the three names outside
  the builds folder (a `git grep` at 51cd8b402) · by value: `tools/lexicon/lexicon.py`, whose verb
  count the pin `VERB_OFFENDER_PIN` in `.lexicon.conf` bounds; the renames bring that count back to the
  pin.
- **S14** — Held legs budgeted. `tools/run-gates/selftest-budgets.txt` gains a row for each of
  `core selftest`, `instruction units selftest`, `instruction edits selftest`, `tags positional selftest`
  and `tags bundle selftest`: the leg, its budget, an empty argv field, and a reason naming the reading.
  The budget is the worst reading the main loop measured and hands the builder, times 1.5, floored at 60,
  the file's own calibration rule. Observed by AC14.
- **S15** — The tags leg's ceiling. The main loop's reading, 210 s (DERIVED at de36424bf) alone over the tree at `de36424bf`
  (PINNED), enters `tools/run-gates/ceiling-evidence.txt` through
  `python tools/run-gates/derive-ceilings.py --write --observed` with its `--how`, never by hand. The
  leg's `ceiling` in `tools/gate-legs.json` rises from 180 to 420, the reading plus the margin's
  `max(120, 1.0 x 210)` that `tools/run-gates/ceiling-margin.txt` declares (section 8 F3; PINNED).
  Observed by AC15.
- **S16** — Check 23's tokenizer. `tools/memory-tree/check-memory-hygiene.sh`'s check 23 prologue keeps
  each criterion bullet's text, its continuation lines joined to it with one space after their leading
  blanks, and extracts the backticked tokens once from the joined text, where today `altoks` reads one
  physical line at a time. A span that wraps a line then reads as one token. The suite gains the arm
  section 7 names. Observed by AC16.
- **S17** — Unit 76's unarmed refusal. `tools/govkit/docs_leg.py` gains the fixture plant
  `unit-usage-alone`, which registers the `unit-usage` class without the `unit` class, and the govkit
  selftest's `_docs_cases` gain its row, exit 2 with the refused state `check_unit_lines` returns.
  Observed by AC17.
- **S18** — Owed observations. The main loop runs PLAY-dOrderedCharter-18 AC3,
  PLAY-dOrderedCharter-65 AC3 and PLAY-dOrderedCharter-72 AC6 as each criterion says, and records each
  as one line in that unit's ledger in the OBSERVED form, its first token one the criterion carries.
  A line records what the run printed. Where that differs from the criterion's stated result, the line
  says so and claims no pass: unit 18's second query prints two keep rows at 51cd8b402, which
  PLAY-dOrderedCharter-49 S19 rewords its criterion to admit. Observed by AC18.

## 3. Non-goals (OUT)

- The record-only offenders the main loop owns: the kickoff-manifest ratchet, method carriers, the
  lexicon Skill render and the ledger lines fixed at `de36424bf` and `51cd8b402`.
- The `policy check` leg's five `review.*` reader-coverage findings, which `origin/main`'s dFairHearing
  owns (PLAY-dOrderedCharter-73's non-goals).
- Whether `playbook-render` requires the policy or memory-tree kit. Section 8 F2 takes an option that
  needs no new requirement, and the dependency question PLAY-dOrderedCharter-73 parked stays the owner's.
- The `[land]` and `[roles]` practice lines' text, a governance carrier (section 8 F4).
- Any change to `memory/project/spawn-idiom-sites.txt`: S1 converts sites, it raises no count.
- The matrix reading a leg as passing when one of its arms fails, the gap PLAY-dOrderedCharter-73's
  section 8 F1 records.
- The tags leg's own cost: S15 records a measurement and moves the bound; a faster check is a unit of
  its own.
- Any edit to the text of a CLOSED spec, PLAY-dOrderedCharter-18, -65 and -72 included; their ledgers
  are records and take S18's lines.

This unit rests on CLOSED units it does not declare as edges, since a consumes-from edge into a CLOSED
spec reds memory hygiene's edge check and a CLOSED spec's text is frozen. PLAY-dOrderedCharter-76 built
`tools/govkit/docs_leg.py#check_unit_lines`, whose refused state S17 arms. PLAY-dOrderedCharter-19
minted the tags leg and its 180 s ceiling at `9cb93347d` (PINNED), which S15 raises.
PLAY-dOrderedCharter-41 built the cross-os arm S10 repairs, and PLAY-dOrderedCharter-16, -19, -24 and
-11 the four plant blocks S11 gates. PLAY-dOrderedCharter-73 parked the matrix's dependency question
that section 8 F2 answers without taking its vetoed option. PLAY-dOrderedCharter-49, DEFERRED, holds the
reworded criterion S18's unit-18 line points at.

### Edges

none

## 4. Design

### Evidence

Read at `51cd8b402`; the bar's logs are its run over `3c63fe888`, and the commits between touch only
records, so every code offender below stands at HEAD.

- Shell hygiene: the scan measures `manifest-check.test.sh` at `cat-file` 4, `path-subst` 12 and
  `printf-subst` 11 against declared 3, 8 and 10; `adopt-agent-instructions.test.sh` at `cat-file` 4
  and `var-pipe` 6 against 3 and 5; `check-template-size.test.sh` at `path-subst` 5 against 4 (PINNED,
  the leg's log). The added lines S1 names are the branch's, by `git diff 8bec4cefd` (the merge base).
- Install prefix: 23 kit-path spellings on 22 lines (PINNED, the leg's log), every one S2 or S3 names.
  The counter at `tools/check-install-prefix.sh` lines 461 to 472 splits a rule-3 operand on
  whitespace, either quote, a backtick, `=`, `(` and `:`, and its comment there names the Skill dir as the case the dot-dir test exempts. The
  same literal `.claude/skills/lexicon/SKILL.md` at `tools/lexicon/kit.toml@c6ba7bc3:75` and
  `tools/lexicon/adopt-lexicon.sh@ff7c3635:246` is not counted; only the envelope's `[` lead is.
- Harness arms: `tools/check-template-size.sh@acbcf7c3:347`'s `fail 8` carries the remedy text, and A25 at
  `tools/check-template-size.test.sh@4fdc7fd0:240` asserts only its first clause.
- Dead paths: the eight carriers S5 lists are the leg's whole hit list (PINNED, its log). The file's
  header calls it shrink-only; `92e3bab9e` added two rows for fixture literals the same way.
- Remote literals: `tools/playbook/overlay.py@7d5aa983:679` and `tools/playbook/overlay.py@7d5aa983:680` (the leg's log).
- Govkit selfcheck: two problems, the unclaimed fixture and the adopter's name at
  `tools/govkit/entries/push-main.kit.toml@9250ba5c:93`, which the playbook kit now ships as
  `tools/playbook/push-main.kit.toml` (a scratch install at 51cd8b402 holds it).
- Matrix, reproduced by this writer in a scratch install shaped as `tools/govkit/matrix.py`'s shape 5:
  `apply` exits 1 with `render-playbook: REFUSED — line 104`, a rule in a one-line region at 201
  characters, quoting the `[land]` line under the 30-character stub (PINNED). The narrowed text the
  cross-os arm builds from that install's `deploy.toml` fails `tomllib.loads` at line 11, column 43, the
  matrix log's exact error, and at line 4, column 17 with `drop_blocks` prepended.
  `tools/govkit/registry.toml@77d73836:743` and `:755` hold `instruction edits selftest` and
  `instruction units selftest` as `[[exempt_leg]]` rows whose `why` reads "a descriptor row naming a leg
  the target cannot carry is what reds the deployer". PLAY-dOrderedCharter-65's Migration section
  records the core's legs as gov-only, and `tags (the resolver's checks)` is `[[exempt_leg]]` at
  `tools/govkit/registry.toml@77d73836:711`.
- Docs: seven `UNROWED` lines, five on `help/charter.md` and two on `help/roles.md` (PINNED, the leg's
  log). `tools/govkit/docs_leg.py#read_docs_state` counts a `script:` row as graded, so each new row
  owes an anchor or reds `UNDOCUMENTED`.
- Lexicon: `verb offenders 1212 over pin 1209` (PINNED, the leg's log); `.lexicon.conf` sets
  `VERB_OFFENDER_PIN="1209"`. `tools/playbook/overlay_rows.py@50335e34:203` calls `pins.fold_text`.
- Ceilings: the margin row is `120 1.0`, and `derive-ceilings.py --check` requires a ceiling at the
  reading plus `max(120, 1.0 x reading)`. The tags leg is absent from `tools/gate-legs.json` at the
  merge base `8bec4cefd` and arrives at `9cb93347d`.
- Check 23: `altoks(line)` per physical line at `tools/memory-tree/check-memory-hygiene.sh@66a9fc27:3441` and
  `:3442`. PLAY-dOrderedCharter-13 AC5 opens a backticked command on one line and closes it on the next,
  so the extractor pairs the closing backtick with the next span's opening one and yields two prose
  fragments, neither sharing anything with the ledger's `tools/govkit/registry.toml`.
- Docs refusal: `tools/govkit/docs_leg.py@2d99fa99:437` returns the refused state; no plant of `PLANTS` stages
  it and no `_docs_cases` row expects exit 2.

### The three install-day fixes, together

The matrix's scratch install fails five checks, and three causes are this branch's. The `[land]` line
grew to 175 characters at `main` (PINNED), and the 30-character stub pushes it past the cap; S9 shortens
the stub. The cross-os arm assumes gov's own `deploy.toml`, which sets none of the keys it inserts; S10
makes its narrowing replace them. The three new legs and four new plant blocks reach kits the
install lacks; S8 keeps the legs gov's, as the registry's rule says, and S11 announces each block
unarmed where its kit is absent. After the three, the scratch install's declared legs are the five
`SCRATCH_EXPECT` already states.

### The tokenizer, sketched

```awk
if (line ~ /<label>/) { labs[++nlab] = lab; labx[nlab] = line }
else if (nlab > 0 && line !~ /^[ \t]*$/) { t = line; sub(/^[ \t]+/, "", t); labx[nlab] = labx[nlab] " " t }
# at the print: labt[i] = altoks(labx[i])
```

The bullet's extent is unchanged: the label line and every non-blank line until the next label or
heading, the population the per-line form already read.

### The plant

```python
elif plant == "unit-usage-alone":
    # PLAY-dOrderedCharter-77: `unit-usage` registered and `unit` not, so no unit line can resolve: exit 2.
    write_edit(usage, "[[usage]]\n", '[[class]]\nclass = "unit-usage"\nusage = "none"\n'
               'why = "fixture units carrying a usage"\n\n[[usage]]\n')
    class_ids.append("unit-usage")
```

### Inventory

| Minted | Where | Cell |
|---|---|---|
| `run_claude` | `skills/session-kickoff/card-compaction.fixture.sh` | `sh.function`, `OK` by `--suggest` at design |
| `derive_folded_text`, `derive_stripped_text` | `tools/playbook/pins.py` | `py.function`, each `OK` by `--suggest` at design |
| `check_sibling_kit` | `tools/playbook/adopt-playbook.sh` | `sh.function`, `OK` by `--suggest` at design |
| `FX_REMOTE` | `tools/playbook/overlay.py` | no cell declares constants |
| the plant `unit-usage-alone` | `tools/govkit/docs_leg.py` | the fixture's `PLANTS` |
| four `[[usage]]` ids | `tools/govkit/usage.toml` | the docs leg's row checks |
| three `[[exempt_leg]]` rows and one `[[exempt]]` row | `tools/govkit/registry.toml` | govkit selfcheck |
| eight waiver rows, five budget rows, one evidence row | the three tool files S5, S14 and S15 name | their gates' row grammars |
| the line `UNARMED — the <block> plants: no <home> kit in this install` | `tools/playbook/adopt-playbook.sh` | none |

### Files touched (estimate)

- `skills/session-kickoff/manifest-check.test.sh` (S1, S2)
- `skills/session-kickoff/card-compaction.fixture.sh` (S13)
- `tools/agent-instructions/adopt-agent-instructions.test.sh` (S1)
- `tools/check-template-size.test.sh` (S1, S2, S4)
- `tools/check-install-prefix.sh`, `tools/check-install-prefix.test.sh` (S3)
- `tools/playbook/overlay.py` (S2, S6), `tools/playbook/pins.py` (S2, S13),
  `tools/playbook/overlay_rows.py` (S13)
- `tools/playbook/practice_census.py` (S2)
- `tools/playbook/render_playbook.py` (S2, S10)
- `tools/playbook/adopt-playbook.sh` (S11), `tools/playbook/kit.toml` (S8)
- `tools/roles/render_agents.py` (S2)
- `tools/dead-path-waivers.txt` (S5)
- `tools/govkit/registry.toml` (S7, S8), `tools/govkit/entries/push-main.kit.toml` (S7)
- `tools/govkit/matrix.py` (S9)
- `tools/govkit/usage.toml` (S12), `tools/govkit/docs_leg.py` (S17), `tools/govkit/selftest.py` (S17)
- `help/charter.md`, `help/roles.md` (S12)
- `tools/run-gates/selftest-budgets.txt` (S14), `tools/run-gates/ceiling-evidence.txt` (S15, generated),
  `tools/gate-legs.json` (S15)
- `tools/memory-tree/check-memory-hygiene.sh`, `tools/memory-tree/check-memory-hygiene.test.sh` (S16)
- `memory/builds/dOrderedCharter/build/2026-11-02-build-PLAY-dOrderedCharter-18-ledger.md`,
  `memory/builds/dOrderedCharter/build/2026-11-04-build-PLAY-dOrderedCharter-65-ledger.md`,
  `memory/builds/dOrderedCharter/build/2026-11-08-build-PLAY-dOrderedCharter-72-ledger.md` (S18)

### Rollout

Live at landing, order 37, in one pass commit, the main loop's S18 lines and S14's measured walls in
the records commit after it. Within the pass, S8 lands with S9 to S11, so no commit declares a leg the
scratch install cannot state; S12's rows land with their anchors, so no row is ever unanchored.

### Alternatives rejected

| Option | Why not |
|---|---|
| A render token for the five Skill envelopes | Five adopters and their parity copies taught a token for a path that is the same at every install; the counter already means to exempt it (section 8 F1) |
| `playbook-render` requires `policy` and `memory-tree` | A new install requirement, veto 2, parked for the owner by PLAY-dOrderedCharter-73 (section 8 F2) |
| Raising the registry counts in `memory/project/spawn-idiom-sites.txt` | The file's counts may fall and never rise; the sites are the branch's own and convert in place |
| Naming the auto-memory index once in `tools/playbook/memory_index.py` | Fewer rows, but a constructed name to dodge the gate, which the leg's waiver file exists to replace |
| `read_one_line_cap` warning when no policy kit answers | Types the catalogue's `warn` default in a second place, and reverses TOOL-dGroundRules-9's "refuses as before" (section 8 F4) |
| Adding the five legs to the docs list instead of rows | `memory/project/docs-undocumented.txt` holds a low-water and may not grow |

## 5. Production-readiness checklist

- security: N/A — no write path, input boundary or grant changes; S7 takes an adopter's name out of a
  shipped file.
- perf / scale: S11 adds four short `python -c` probes to one selftest run; S16 joins strings it
  already reads. S15 records the tags leg's real cost rather than reducing it.
- error / empty / loading states: S11's unarmed line names the block and the kit, and at gov every kit
  resolves, so gov's bar runs every arm. What S11 does not check: a block whose arms reach a kit only on
  some plants is unarmed whole where that kit is absent. What S3 does not check: an operand opened by `[`
  whose dot-dir segment names something other than a Skill directory is exempt too. What S16 does not
  check: a span wrapping across a blank line, outside the bullet's extent as before.
- observability: every leg prints its own verdict; S18's lines say what each run printed.
- risks: the harness-arms waivers for `card-compaction.fixture.sh` are line-keyed, so S13's rename
  keeps every line where it stands. The tags leg's positional arm may name a record citation of a line
  an insertion moved; the pass re-reads it before landing. A scratch install may red on an arm none of
  S8 to S11 names once these clear; the pass hands that back rather than widening.
- testing: AC1 to AC18, each a direct command, a fixture plant or a grep; the suite arms are the
  `New arm:` lines in section 7.
- migration: additive rows and in-place edits. Three legs move off the playbook-render descriptor, so
  an adopter's next `update` emits three selftest legs fewer into its manifest; none was ever landed on
  the default branch, so no adopter holds one.
- user docs: `help/charter.md` and `help/roles.md` gain their usage anchors (S12). S11's unarmed line is
  selftest output, documented beside the blocks in `tools/playbook/adopt-playbook.sh`.

## 6. Acceptance criteria

Each leg the bar failed, and the criterion that shows it green:

| Leg | Criteria |
|---|---|
| `shell hygiene (a fork spent on builtin work)` | AC1 |
| `install-prefix (shipped surface)` | AC2, AC3 |
| `harness arms (fail branches armed or pinned)` | AC4 |
| `dead-path carriers (deleted files still named)` | AC5 |
| `remote literals (kit code names no remote)` | AC6 |
| `govkit selfcheck` | AC7, AC8 |
| `govkit acceptance matrix` | AC9, with AC8, AC10 and AC11 |
| `docs` | AC12, AC17 |
| `lexicon naming predicates` | AC13 |
| `every held leg is budgeted, every budget row resolves` | AC14 |
| `tags (the resolver's checks)`, `leg ceilings clear their evidenced maximum` | AC15 |
| `memory hygiene` | AC16, AC18 |

A criterion that runs a leg's own checker is the main loop's at the close wherever the builder's role
may not run it. Each scratch clone is `git clone -q --shared . <tmp>`, run with the clone's own tools.

- **AC1** — When the `shell hygiene (a fork spent on builtin work)` leg's argv, as
  `tools/gate-legs.json` declares it, runs over the tree after the pass, `tools/gate-lint/sh_hygiene.py`
  exits 0, and no line holding `the scan measures` names any of the three files S1 converts; and
  `git diff 51cd8b402 -- memory/project/spawn-idiom-sites.txt` prints nothing.
  Red when: an added site keeps its fork, or a registry count rises to meet it.
  figure: PINNED, nine sites over the declared counts in the bar's log over 3c63fe888.
- **AC2** — When `bash tools/check-install-prefix.sh` runs after the pass, it exits 0; and
  `bash tools/check-install-prefix.sh --list` prints no hit naming `tools/playbook/overlay.py`,
  `tools/playbook/pins.py`, `tools/playbook/practice_census.py`, `tools/playbook/render_playbook.py`
  or `tools/roles/render_agents.py`, nor either of the two test files S2 lists.
  Red when: a kit path stays spelled, or a waiver of any shape lets one stand.
  figure: PINNED, 23 spellings on 22 lines in the bar's log over 3c63fe888.
- **AC3** — When `bash tools/check-install-prefix.sh --list` runs after the pass, it prints no line
  naming `SKILL.template.md`, while `git diff 51cd8b402 -- tools/drift-audit/SKILL.template.md tools/lexicon/SKILL.template.md tools/memory-recall/SKILL.template.md tools/runlog/SKILL.template.md tools/unattended/SKILL.template.md`
  prints nothing; and over the tree after the pass, the `--list` hit set read with the counter as at
  51cd8b402 and read with the pass's counter differs by the five envelope lines alone.
  Red when: an envelope line still counts, or the split exempts a hit that is no Skill directory.
- **AC4** — When `python3 tools/memory-tree/check-arms.py --check` runs after the pass, it prints no
  line naming `tools/check-template-size.sh`; and
  `git grep -c "a harness reading less than the charter drops its tail" -- tools/check-template-size.test.sh`
  counts 1.
  Red when: check 8 branch 1's remedy text stays unasserted and unpinned.
- **AC5** — When `bash tools/check-dead-paths.sh` runs after the pass, it exits 0; and
  `git grep -c "auto-memory index" -- tools/dead-path-waivers.txt` counts 8.
  Red when: a carrier stays unwaived, or a row's text no longer matches its carrier and reds stale.
  figure: PINNED, eight carriers in the bar's log over 3c63fe888.
- **AC6** — When `bash tools/check-remote-literals.sh` runs after the pass, it exits 0;
  `git grep -n "refs/remotes/origin" -- tools/playbook/overlay.py` prints nothing; and
  `python tools/playbook/overlay.py --fixture` exits 0.
  Red when: the fixture spells the remote, or the assembled name breaks `arm_policy_at_head`.
- **AC7** — When `python tools/govkit/govkit.py selfcheck` runs after the pass, it exits 0, printing no
  line naming `card-compaction.fixture.sh` and no line holding `names the adopter`; and
  `git grep -n "adopter nc" -- tools/govkit/entries/push-main.kit.toml` finds the comment.
  Red when: the fixture stays unclaimed, or a shipped file names an adopter.
- **AC8** — When `git grep -nE "^name = \"(core selftest|tags positional selftest|tags bundle selftest)\"" -- tools/playbook/kit.toml`
  runs after the pass, it prints nothing; the same grep over `tools/govkit/registry.toml` prints three
  lines, each under an `[[exempt_leg]]` header; and `python tools/govkit/govkit.py selfcheck` names none
  of the three legs.
  Red when: a target is still handed a leg it cannot carry, or a leg in `tools/gate-legs.json` is left
  neither claimed nor exempt.
- **AC9** — When `python tools/govkit/matrix.py` runs after the pass, it prints no line opening
  `FAIL scratch install:`, and it prints `ok` for
  `scratch install: apply RENDERS the region into the target's own charter`, for
  `scratch install: the declared leg set and the stated expectations are the same set`, and for both
  lines of each of `playbook render wiring` and `playbook render selftest`.
  Red when: `apply` refuses an over-length rule under the stub, the declared and stated leg sets differ,
  or a leg prints a traceback where it was installed.
  cost: one matrix run; its evidenced maximum is 218.8 s on node a (PINNED, `tools/run-gates/ceiling-evidence.txt`).
  permission: the main loop runs it at the close, since a role agent's scratch guard refuses a scratch
  install (PLAY-dOrderedCharter-72 AC6).
- **AC10** — When, in a scratch clone whose `.governance/deploy.toml` opens with `drop_blocks = []` and
  whose `[answers]` table gains `ci_file = "x"`, the clone's own
  `python tools/playbook/render_playbook.py --selftest` runs after the pass, it prints
  `render_playbook.selftest OK` and no `Traceback`; with the narrowing as at 51cd8b402 the same run
  prints `Cannot overwrite a value`. Over the tree, the same command prints
  `render_playbook.selftest OK`.
  Red when: the cross-os arm's narrowing duplicates a key its target's `deploy.toml` already sets.
- **AC11** — When `bash tools/playbook/adopt-playbook.sh --selftest` runs over the tree after the pass,
  it prints `PASS — the layer check's plants`, `PASS — the tag resolver's plants`,
  `PASS — the edge grammar's plants` and `PASS — the load sets' plants`, and no `UNARMED` line; and in
  AC9's scratch install the same leg prints one `UNARMED` line for each of the four blocks and no
  `Traceback`.
  Red when: a block runs where its kit is absent and dies, or a block goes unarmed at gov.
  cost: one `playbook render selftest` run over the tree, under its 300 s ceiling (PINNED, `tools/gate-legs.json`).
- **AC12** — When `python tools/govkit/docs_leg.py` runs after the pass, its summary reads
  `0 unrowed`, and it prints no `UNROWED`, `UNDOCUMENTED`, `TWICE` or `STALE` line; and
  `python tools/govkit/docs_leg.py --fingerprints` prints a row for each of `build_records.py#new`,
  `instruction_units.py#envelopes`, `instruction_units.py#drive` and `load_sets.py#derive`, each naming
  one page.
  Red when: a page shows a tracked entrypoint no row declares, or a new row is anchored nowhere.
- **AC13** — When `python tools/lexicon/lexicon.py` runs after the pass, it prints no line holding
  `over pin`; `git grep -nwE "fold_text|strip_text" -- tools/playbook/pins.py tools/playbook/overlay_rows.py`
  prints nothing; `git grep -n "^ask()" -- skills/session-kickoff/card-compaction.fixture.sh` prints
  nothing; and `python tools/lexicon/lexicon.py --suggest derive_folded_text --as py.function` opens
  with `OK`.
  Red when: a renamed function keeps an undeclared verb, or a call site still spells the old name.
  figure: DERIVED, the offender count at observation against the pin `.lexicon.conf` holds.
- **AC14** — When the `every held leg is budgeted, every budget row resolves` leg's argv, as
  `tools/gate-legs.json` declares it, runs over the tree after the pass, it exits 0 and prints no line
  holding `carry no budget row`; and
  `git grep -cE "^(core|instruction units|instruction edits|tags positional|tags bundle) selftest" -- tools/run-gates/selftest-budgets.txt`
  counts 5.
  Red when: a held leg's cost stays undeclared.
  figure: DERIVED, each budget from the main loop's handed reading by the file's rule.
- **AC15** — When `python tools/run-gates/derive-ceilings.py --check` runs after the pass, it exits 0;
  `git grep -n "^tags (the resolver's checks)" -- tools/run-gates/ceiling-evidence.txt` prints one row
  whose maximum is 210.0 and whose source is the `--how` text; and `python tools/playbook/gov_tag.py check`
  completes over the tree inside its 420 s ceiling (DERIVED, the value `tools/run-gates/ceiling-margin.txt` requires).
  Red when: the leg is killed at its bound, or its ceiling does not clear the evidenced maximum.
  figure: PINNED, 210 s measured by the main loop alone over the tree at de36424bf.
  permission: the main loop runs the tags leg at the close.
- **AC16** — When `bash tools/memory-tree/check-memory-hygiene.sh --only 23` runs after the pass, it
  prints no line naming `PLAY-dOrderedCharter-13/AC5`; and its check 23 offender set over the tree,
  read with the checker at 51cd8b402 and after the pass, differs by that member and AC18's three alone.
  Red when: a wrapped span still splits into prose fragments, or the join changes another unit's
  verdict.
- **AC17** — When `python tools/govkit/docs_leg.py --fixture --plant unit-usage-alone` runs after the
  pass, it exits 2, printing
  `docs: REFUSED · class unit-usage is registered and class unit is not, so no unit line can resolve`;
  and `python tools/govkit/docs_leg.py --fixture --plant unit-lines` still exits 1.
  Red when: the refused state passes unseen, or the leg grades unit lines with no class to resolve them.
- **AC18** — When `bash tools/memory-tree/check-memory-hygiene.sh --only 23` runs after the main loop's
  records commit, it names none of `PLAY-dOrderedCharter-18/AC3`, `PLAY-dOrderedCharter-65/AC3` and
  `PLAY-dOrderedCharter-72/AC6`; and the unit-18 line in
  `memory/builds/dOrderedCharter/build/2026-11-02-build-PLAY-dOrderedCharter-18-ledger.md` names
  `tools/memory-tree/backlog.py@ce13efbe:1808` and both keep rows its query printed.
  Red when: an owed criterion stays unrecorded, or a line claims a result its run did not print.
  permission: each of the three runs is the main loop's, as each criterion's own permission line says.

## 7. Gates

`shell hygiene (a fork spent on builtin work)` · `install-prefix (shipped surface)` · `install-prefix self-test` · `harness arms (fail branches armed or pinned)` · `dead-path carriers (deleted files still named)` · `remote literals (kit code names no remote)` · `govkit selfcheck` · `govkit acceptance matrix` · `govkit selftest` · `govkit refusal join` · `docs` · `help page commands` · `lexicon naming predicates` · `every held leg is budgeted, every budget row resolves` · `leg ceilings clear their evidenced maximum` · `tags (the resolver's checks)` · `memory hygiene` · `memory-hygiene self-test` · `template size gate selftest` · `playbook render selftest` · `playbook render wiring` · `roles render selftest` · `agent-instructions self-test` · `manifest-check self-test` · `scratch-guard self-test` · `policy fixtures` · `recall floor arms` · `measure-legs selftest` · `run-gates canary` · `run-gates gov canary` · `spec tokens (a spec's own names resolve)` · `recall floor`

The guarded legs on the line are those the files touched trip: the govkit legs and `recall floor arms`
for `tools/govkit/`, `recall floor` for the three ledgers under `memory/`, `policy fixtures` for the playbook, roles, govkit and hygiene files, the kickoff
legs and the lexicon for `skills/session-kickoff/`, and the run-gates legs and `measure-legs selftest`
for `tools/gate-legs.json`.

New arm: tools/check-install-prefix.test.sh · covers AC3 · a tracked template line `[.claude/skills/<kit>/SKILL.md · Level 4 · x]`, counted before S3's split change, beside a control `[x/<kit>/a.py` that still counts · none
New arm: tools/check-template-size.test.sh · covers AC4 · the 40960 cap A25 already builds, whose refusal must print check 8 branch 1's remedy text · none
New arm: tools/memory-tree/check-memory-hygiene.test.sh · covers AC16 · a fixture CLOSED Tier-2 spec whose criterion's backticked command wraps a line and a ledger line naming the path it closes on, red before S16, beside a control ledger line sharing nothing that stays red; the fixture conf arms ACCEPTANCE_LEDGER_CUTOFF and LEDGER_TOKEN_CUTOFF · none
New arm: tools/govkit/selftest.py · covers AC17 · a `_docs_cases` row on the `unit-usage-alone` plant, red before the plant exists · none

## 8. Open questions

- **F1 — How the five Skill envelope lines leave the install-prefix ban.** Each spells
  `[.claude/skills/<kit>/SKILL.md · …]`, a destination that is the same at every install and no kit
  path. Options: (a) a render token each template's adopter substitutes, in five adopters and the parity
  copies that re-render them; (b) the counter's rule-3 operand split admits `[`, so the dot-dir test the
  counter already applies to a Skill directory reads `.claude` and exempts the line; (c) a waiver, which
  the gate refuses to carry. (c) is barred by the gate's own header. (a) teaches five renderers a token
  for a value that never varies, a mechanism per kit for what one character of the counter fixes. (b)
  repairs the counter where its stated intent and its split disagree, and AC3 holds the hit set to the
  intended difference. RESOLVED (agent, 2026-11-10, delegated): (b), fewest open questions and the
  counter's own homonym seam. widens: none · relaxes: the install-prefix counter's rule 3, for an
  operand opened by `[` whose segment is a dot-directory
- **F2 — What lets the matrix's scratch install carry the playbook-render legs.** The install holds
  neither the policy nor the memory-tree nor the roles kit, and `core selftest`,
  `tags positional selftest` and `tags bundle selftest` refuse there for want of the policy kit
  (PLAY-dOrderedCharter-73's builder, rev-2). Options: (a) `tools/playbook/kit.toml` requires the kits
  and the matrix installs them; (b) every reader degrades where a sibling kit is absent, the three legs
  keep their descriptor rows, and `SCRATCH_EXPECT` states each one's degraded verdict; (c) the three
  legs move to gov-only `[[exempt_leg]]` rows, as the registry's rule for a leg a target cannot carry
  says and as `instruction units selftest` sits, and the shipped render selftest's four plant blocks
  announce themselves unarmed where their kit is absent (S8, S11). (a) adds an install requirement,
  veto 2, and is the option PLAY-dOrderedCharter-73 parked for the owner; this fork does not take it. (b)
  degrades three fixtures into suites that pass by reading less at every install lacking the policy
  kit, a follow-up per leg, against PLAY-dOrderedCharter-65's record that the core's legs are gov's. (c)
  writes declarations for the three legs and one guard per block, and leaves the requirement question
  open for the owner, unharmed. RESOLVED (agent, 2026-11-10, delegated): (c), the most feature-rich
  survivor, fewest follow-ups, and the registry's own seam. widens: none · relaxes: an adopter's
  manifest, which receives three selftest legs fewer; the render selftest's four plant blocks, unarmed
  at an install lacking their kit
- **F3 — Whether this unit may raise the tags leg's ceiling.** The main loop's reading is 210 s (DERIVED at de36424bf) against
  the 180 s bound (PINNED), so recording it alone reds `leg ceilings clear their evidenced maximum`
  and leaves the leg killed. Options: (a) the evidence row and a ceiling of 420, the reading plus the
  declared margin; (b) the evidence row alone; (c) a faster `gov_tag.py check`. (b) fails AC15. (c) is a
  performance unit of its own by the build method's M2. The build method reserves a declared ceiling to
  the owner, and this one is no owner's: the leg and its 180 were minted on this branch at `9cb93347d`
  by PLAY-dOrderedCharter-19 and never landed, so the number is this build's own design value, moved by
  M2's amend act. RESOLVED (agent, 2026-11-10, delegated): (a), the one option meeting AC15. widens:
  none · relaxes: the tags leg's hang bound, from 180 s to 420 s (PINNED)
- **F4 — How `apply` renders the region in the scratch install.** The `[land]` line is 201 characters
  under the matrix's stub, and with no policy kit the render refuses past 200 (PINNED). Options: (a)
  the stub shortened to `stated`; (b) the `[land]` practice line shortened; (c) `read_one_line_cap`
  warns rather than refusing when no policy kit answers. (b) edits a charter practice, a governance
  carrier, veto 2. (c) types the catalogue's `warn` default in a second place and reverses the stated
  "refuses as before" of TOOL-dGroundRules-9. (a) changes a fixture value that measures nothing, the
  class of fixture-induced red the matrix's own comment warns against. RESOLVED (agent, 2026-11-10,
  delegated): (a), the one survivor. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-10 · initial draft, from `2026-11-10-prompt-PLAY-dOrderedCharter-77-spec-brief.md`,
  every offender re-read at `51cd8b402` against the bar's logs over `3c63fe888`. The matrix's apply and
  decode failures were reproduced in a scratch install; the brief's two options for the policy lookups
  are F2's (a) and (b), and F2 takes a third.
- rev-2 · 2026-11-10 · S15 · AC15 · F3 · from `2026-11-10-prompt-PLAY-dOrderedCharter-77-pin-brief.md`:
  the tags leg's measured wall and its new ceiling each carry their provenance on their own line; no
  design text moved. AC1 · AC2 · AC14 · section 7 · from
  `2026-11-10-prompt-PLAY-dOrderedCharter-77-3-spec-writer.md`: the three criteria observe each leg's
  checker and name no suite, and the leg line gains the guarded leg the ledgers trip; no design text
  moved.
- rev-2 · 2026-11-10 · section 4's Evidence · S11 · AC18 · section 10 · from
  `2026-11-10-prompt-PLAY-dOrderedCharter-77-pin-lines-brief.md`: each unlisted file:line citation is
  a blob-pinned line, written by `python tools/playbook/positional.py pin --at 51cd8b402`, the base, and
  each pinned line read back as the line its prose names. AC18's bare backlog line, which the tool
  refuses as no path, is spelled `tools/memory-tree/backlog.py@ce13efbe:1808`, the form the unit-18
  ledger line it observes holds. Citation form only: no design text moved, and the rev stays.

## 10. Reuse audit

Every fix extends a seam the tree already holds, and no new mechanism is minted. The registry's
`[[exempt_leg]]` rule for a leg a target cannot carry, at `tools/govkit/registry.toml@77d73836:743` and `:755`,
is S8's. The install-prefix counter's own Skill-dir homonym rule is S3's. The playbook kit's inline
`resolve_kit_dir` in `tools/playbook/policy_value.py`, reached as `tools/playbook/load_sets.py` reaches
it, is S2's and S11's, and `tools/playbook/render_playbook.py#resolve_declaration_paths` is S2's
registry read. `iu.derive_kit_rel` is S2's fixture path, the docs leg's `PLANTS` and `_docs_cases` are
S17's, and `derive-ceilings.py --write --observed` is S15's. Run at `51cd8b402`,
`python tools/codebase-map/reuse_lookup.py "announce a selftest block unarmed when a sibling kit does not resolve in this install"`
ranked `resolve_kit_dir` the first seam with an install count, then `resolve_prefix_token` and
`derive_kit_rel`, and no unarmed-announcement helper, so `check_sibling_kit` is new code over that
seam. The recall query returned PLAY-dOrderedCharter-73's section 8 F1, the dependency question F2
answers without its vetoed option, and PLAY-dOrderedCharter-72's brief asking for the three legs'
install-day verdicts.

Recall terms used: `python tools/memory-recall/query.py "how does a shipped selftest or leg behave at a target that lacks a sibling kit, and which legs are gov-only" --terms "exempt_leg gov-only scratch install SCRATCH_EXPECT unarmed sibling kit resolve_kit_dir descriptor gate_leg policy memory-tree"`
