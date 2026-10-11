# KICK-aOrientedCast-1 — the card's task gains To-do and Reuse, and a READY body lands only with every task field filled

**Status:** OPEN · rev-1 · 2026-10-11 · node a · Tier-2 · base 646d4a73 · streams kickoff · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-11-build-TOOL-aOrientedCast-1-cross-read.md](../build/2026-10-11-build-TOOL-aOrientedCast-1-cross-read.md) | research | KICK-aOrientedCast-2 PLAY-aOrientedCast-1 TOOL-aOrientedCast-1 TOOL-aOrientedCast-2 TOOL-aOrientedCast-3 TOOL-aOrientedCast-4 TOOL-aOrientedCast-5 TOOL-aOrientedCast-6 TOOL-aOrientedCast-7 TOOL-aOrientedCast-8 |
| [2026-10-11-prompt-TOOL-aOrientedCast-1-1-spec-brief.md](../prompts/2026-10-11-prompt-TOOL-aOrientedCast-1-1-spec-brief.md) | journal | KICK-aOrientedCast-2 PLAY-aOrientedCast-1 TOOL-aOrientedCast-1 TOOL-aOrientedCast-2 TOOL-aOrientedCast-3 TOOL-aOrientedCast-4 TOOL-aOrientedCast-5 TOOL-aOrientedCast-6 TOOL-aOrientedCast-7 TOOL-aOrientedCast-8 |
| [2026-10-11-prompt-TOOL-aOrientedCast-1-2-build-brief.md](../prompts/2026-10-11-prompt-TOOL-aOrientedCast-1-2-build-brief.md) | journal | KICK-aOrientedCast-2 PLAY-aOrientedCast-1 TOOL-aOrientedCast-1 TOOL-aOrientedCast-2 TOOL-aOrientedCast-3 TOOL-aOrientedCast-4 TOOL-aOrientedCast-5 TOOL-aOrientedCast-6 TOOL-aOrientedCast-7 TOOL-aOrientedCast-8 |
| [2026-10-11-prompt-TOOL-aOrientedCast-1-3-cross-read.md](../prompts/2026-10-11-prompt-TOOL-aOrientedCast-1-3-cross-read.md) | journal | KICK-aOrientedCast-2 PLAY-aOrientedCast-1 TOOL-aOrientedCast-1 TOOL-aOrientedCast-2 TOOL-aOrientedCast-3 TOOL-aOrientedCast-4 TOOL-aOrientedCast-5 TOOL-aOrientedCast-6 TOOL-aOrientedCast-7 TOOL-aOrientedCast-8 |
| [2026-10-11-prompt-TOOL-aOrientedCast-1.md](../prompts/2026-10-11-prompt-TOOL-aOrientedCast-1.md) | research | KICK-aOrientedCast-2 PLAY-aOrientedCast-1 TOOL-aOrientedCast-1 TOOL-aOrientedCast-2 TOOL-aOrientedCast-3 TOOL-aOrientedCast-4 TOOL-aOrientedCast-5 TOOL-aOrientedCast-6 TOOL-aOrientedCast-7 TOOL-aOrientedCast-8 |

<!-- /gen:spec-records -->

## 1. Goal

The orientation card is what every later handoff of this build is rendered from, and today its
`## task` section is checked only for being present: a kickoff can land a card whose fields are
missing, renamed, or still the skeleton's `…`. This unit adds the two fields the owner named,
To-do and Reuse, to the one sealed field set, and makes `--card --append` refuse a READY body unless
all eight fields are there, once each, and filled. It moves the manifest format to 1.5 so an adopter
whose manifest still carries the six-field region stays green through a normal `govkit update` and
is told how to upgrade.

## 2. Scope (IN)

- **S1** — `TASK_SKELETON` gains `**To-do:**` after the OUT field and `**Reuse:**` after To-do, each
  with a short parenthesized qualifier, in the shape §4 "The skeleton" prints. `--task-skeleton`
  prints eight field lines. Observed by AC1.
- **S2** — A new function `check_card_task` grades a body carrying a real READY line: its `## task`
  section must hold every field `TASK_SKELETON` names, each exactly once, none empty and none a
  placeholder, by the grammar §4 pins. A miss exits 1 naming every failing field and the skeleton
  verb, and the card stays byte-identical. The labels are read from `TASK_SKELETON` at run time.
  Observed by AC2, AC3, AC4, AC5 and AC6.
- **S3** — The refusal sits in `add_card_body` directly after the existing `## task` presence
  refusal, so DEAD PROBE, the presence refusal and the stale-BASE refusal keep their verdicts, and a
  body with no READY line is not graded by it. Observed by AC7.
- **S4** — `MANIFEST_FORMAT` moves to 1.5, and check 10 accepts the frozen 1.4 region only in a
  manifest whose marker is older than 1.5, printing a NOTE that names the re-paste; the format WARN
  already prints there. A 1.5 manifest must carry the new region. The `RETROFIT` text names 1.5.
  Observed by AC8.
- **S5** — Gov's own manifest and the shipped seed carry the new region and the `v1.5` marker in the
  same commit; gov's manifest re-stamps `last-audit` and `last-body-change`. Observed by AC9 and
  AC10.
- **S6** — `WIRE-INTO-PROJECT.md` §4's retrofit recipe gains the re-paste step and bumps its marker
  step to 1.5, and its result tree names 1.5. Observed by AC11.
- **S7** — The self-test moves with the contract: its fixture manifest takes its region from
  `--task-skeleton` and the `v1.5` marker; every arm whose body carries a real READY line takes a
  filled eight-field task from one helper, so each arm's own refusal still fires; new arms observe
  S1 to S4. NOT OBSERVED by a criterion in this pass: the `manifest-check self-test` leg runs them
  once, at the close.
- **S8** — The session-kickoff dossier's card prose names the field refusal, and
  `memory/map/generated/symbols.json` is regenerated for the new function. NOT OBSERVED by a
  criterion: the `codebase-map coverage + freshness` leg grades both at the close.

## 3. Non-goals (OUT)

- Any edit to the kickoff engine. Step 3 already asks the checker for the field set. Step 5's
  parenthetical that lists four of the fields by hand is stale after this unit, and Step 5 belongs
  to `KICK-aOrientedCast-2`.
- Grading a stored card. `--card --check` keeps its present rules, so a card written before this
  unit, this session's own included, still checks clean.
- Grading what a field says beyond present, single, non-empty and not a placeholder.
- A second, unbolded label grammar (§4 Alternatives rejected).
- The route and the brief skeleton, which are aRoutedQuill's and unchanged.
- A govkit step that rewrites an adopter's region (§8 F2).
- The kickoff-manifest kit's vintage, `KIT_MANIFEST_VERSION`. It moves once, after the build's last
  unit touching this kit. `MANIFEST_FORMAT` is a different number and moves here, because the format
  moves here.
- The card's `## reuse` section and the scout's opt-in, which are aScoutedSeam's.

### Edges

- **hands-off** `TOOL-aOrientedCast-2` — the eight labels and the field grammar of §4, by which the
  renderer reads every `task:` key, placeholder rule included.
- **hands-off** `KICK-aOrientedCast-2` — Step 5's hand-typed field list, and the engine byte headroom
  this unit leaves unspent.
- **hands-off** external — aScoutedSeam's later kickoff unit turns the interim `**Reuse:**` value
  into a pointer to its own `## reuse` card section.

## 4. Design

### Evidence

Read at `646d4a73` on 2026-10-11.

- `TASK_SKELETON` is a heredoc constant of six field lines inside the sealed markers
  (`skills/session-kickoff/manifest-check.sh:75-85`), printed by `--task-skeleton` before any
  repository probe (`:148-154`).
- `add_card_body` runs: the READY count, the citations, DEAD PROBE, the `## task` presence refusal,
  the stale-BASE refusal, the card's shape, the route rules, the cap
  (`skills/session-kickoff/manifest-check.sh:1023-1069`). The presence refusal is
  `:1034-1036`; it greps for `## task` and grades nothing under it.
- `check_card` refuses a real READY line with no `## task` and grades nothing under it either
  (`skills/session-kickoff/manifest-check.sh:1078-1096`).
- Check 10 byte-compares the manifest's sealed region with `TASK_SKELETON`, with three messages for
  three failure modes (`skills/session-kickoff/manifest-check.sh:1336-1350`). It runs only on a full
  run, never under `--staged` (`:1318-1324`). The format WARN compares the manifest's marker with
  `MANIFEST_FORMAT` (`:1126-1131`, `:48`), and that number is the only one an adopter's marker is
  compared with.
- The region is carried by gov's manifest (`memory/guides/SESSION-KICKOFF.md:34-42`), by the shipped
  seed (`skills/session-kickoff/MANIFEST-TEMPLATE.md:53-61`) and by the self-test's fixture writer
  (`skills/session-kickoff/manifest-check.test.sh:71-95`). The version gate compares the seed's marker
  with `MANIFEST_FORMAT` (`tools/check-kit-versions.sh:170-181`).
- The kickoff-manifest kit ships the checker as `engine`, overwritten on every update, and the
  manifest as `seed`, never touched again; the kit has no adopter and no regenerate step
  (`tools/govkit/entries/kickoff-manifest.kit.toml:16-32`, `:52-55`).
- Every self-test body that carries a real READY line holds a one-line `## task` such as
  `- AGENTS.md:1` (`skills/session-kickoff/manifest-check.test.sh:1104-1110`, `:1171`, `:1234`).
- The region's origin accepted that the seal reds an older adopter manifest on arrival, the WARN
  being the only signal, and the retrofit recipe gaining the paste step (KICK-cKeyedLaunchpad-4 §5).
- The engine is 18256 bytes, 113 under its recorded high-water of 18369 and 176 under its ceiling of
  18432 (`tools/template-size-limits.txt`, `tools/template-size-highwater.txt`). PINNED at
  `646d4a73` on 2026-10-11.
- The stored cards, measured on node `a` on 2026-10-11 by a probe applying §4's grammar to every file
  under the common dir's `orientation/`: 58 cards, 28 of them with a `## task` section and a real
  READY line. Eight write all six bold labels; twenty write no bold label at all, as `- Title:`,
  lowercase `scope in:` lines or one free line. None carries a To-do or a Reuse field. No value in
  the eight bold-label cards is empty, a placeholder, or under twelve characters. The skeleton's own
  six values all grade as placeholders, once the closing region marker is excluded from the last
  field's text, which a first run of the probe absorbed into it.

### The skeleton

`TASK_SKELETON` becomes, verbatim:

```markdown
<!-- kickoff:task -->
> - **Title:** …
> - **Goal (1–2 sentences):** …
> - **IN scope:** …
> - **OUT / non-goals** (explicit cut-line): …
> - **To-do:** (the steps in order, each naming what it changes) …
> - **Reuse:** (each seam this extends, by path, or "no seam fits" with the probe's evidence) …
> - **Acceptance check** (the observation that proves THIS change — a test it adds, a gate it
>   moves, an observed behavior; *not* an unrelated green check): …
> - **Gates it must pass:** …
<!-- /kickoff:task -->
```

The two labels are the build's interface 6 byte for byte. Their qualifiers sit after the label, so
the label a reader matches stays `**To-do:**` and `**Reuse:**`; the qualifier rule below strips them
from the value exactly as it strips OUT's and Acceptance's. The guidance lives in the skeleton rather
than in the engine because the session copies the skeleton, and the engine's headroom is
`KICK-aOrientedCast-2`'s.

### The field grammar

This is the one grammar for a card's task fields. `TOOL-aOrientedCast-2` reads `task:` keys by it.

1. **The section** is the lines after the last `## task` heading, up to the next `## ` heading, the
   next READY line, or the end.
2. **Each line** is stripped of leading whitespace and any run of `>` characters each followed by an
   optional space, then of one leading `- ` or `* ` marker. A line that then opens `<!--` or
   `UNVERIFIED — ` is not field text.
3. **A field line** opens `**`. Its label is the text after that opening up to the first `:**`, when
   one comes no later than the first closing `**`, and otherwise up to the first closing `**`,
   trimmed. The rest of the line, after the closing bytes, opens the field's raw text.
4. **A field's raw text** runs on through each following line, stripped as in rule 2, up to the next
   field line or the section's end.
5. **The value** is the raw text trimmed, then stripped of one leading parenthesized group,
   balanced, across lines, when the text opens with `(`, then of one leading `:`, then trimmed again.
6. **The verdict** reads the value with every whitespace run collapsed to one space. It is EMPTY when
   nothing is left. It is a PLACEHOLDER when it equals, ignoring case, one of `…`, `...`, `tbd`,
   `todo`, `n/a`, `none`, `-` and `?`; when it holds only `.` and `…` characters; or when it is one
   angle-bracket slot holding no further angle bracket.
7. **A field** is ABSENT when no field line carries its label exactly, and REPEATED when two do. A
   field line whose label is not one of the eight is ignored.

The eight labels are read from `TASK_SKELETON` by rules 2 and 3, so the refusal and the skeleton
cannot name different fields. A renderer keeps the value's line breaks; the verdict alone collapses
them.

### The refusal

```text
MANIFEST task REFUSED — the '## task' section has no To-do field; has no Reuse field; leaves Gates it must pass a placeholder ('…'); every field --task-skeleton prints is filled before a kickoff lands, and nothing was appended
```

One clause per failing field, in skeleton order, each `has no <label> field`, `carries <label>
twice`, `leaves <label> empty` or `leaves <label> a placeholder ('<value>')`. Exit 1, the card
byte-identical. `check_card_task` is one `awk` over the body, fed the skeleton on a second input; it
spawns no git and no id reader, so the spawn counts aRoutedQuill's arm pins hold.

The order in `add_card_body` becomes: the READY count, the citations, DEAD PROBE, the `## task`
presence refusal, the task fields, the stale-BASE refusal, the card's shape, the route rules, the cap.
A body with no real READY line is not graded by the task fields, so a route-only append is unchanged.

### Format 1.5 and the adopter contract

- `MANIFEST_FORMAT="1.5"`. A new constant `TASK_SKELETON_FORMAT_1_4` holds the previous region bytes,
  frozen; check 10 is its only reader.
- Check 10 passes a region equal to `TASK_SKELETON`. It passes a region equal to
  `TASK_SKELETON_FORMAT_1_4` only when the manifest's marker is older than 1.5, and then prints
  `NOTE: the sealed task region is format 1.4's; re-paste it from --task-skeleton, then bump the
  marker to v1.5`. Anything else is the existing "differs" failure. An absent or malformed region
  keeps its existing failure at every marker.
- What `govkit update` does to an adopter: it overwrites the checker and never touches the manifest.
  The adopter's ratchet leg stays green and prints the format WARN and the NOTE. Its sessions need
  the eight fields at once, because the engine asks the checker for the field set; the refusal names
  every missing label and the skeleton verb, so the remedy is one re-append.
- The upgrade, an adopter's own act: re-paste the region from `--task-skeleton`, then bump the
  marker to `v1.5` LAST. After the bump, check 10 demands the new region.
- Gov moves in the same commit: its manifest's region is re-pasted, its marker bumped to `v1.5`, and
  `last-audit` and `last-body-change` re-stamped with a delta line in the commit message, because the
  checker is in `watch:` and the body changed. The seed's region and marker move with it, which the
  version gate compares.
- `RETROFIT`'s step 6 names `v1.5`. `WIRE-INTO-PROJECT.md` §4 gains a step after 5b, "re-paste the
  sealed region from `--task-skeleton`", its step 6 bumps to `kickoff-manifest: v1.5`, and its result
  tree names 1.5.

### The self-test

- `write_manifest` takes the region from `bash "$CHECK" --task-skeleton` and defaults its marker to
  `kickoff-manifest: v1.5`, so the fixture cannot drift from the constant again.
- A helper `render_task_section` prints a `## task` section with all eight fields filled. Every arm
  whose body carries a real READY line uses it, so the stale-BASE, two-READY, route and annotation
  arms keep observing their own refusals.
- New arms: the eight-line skeleton; an accepted eight-field body; the six-field body refused naming
  To-do and Reuse; each placeholder form; the skeleton refused by its own rule; the quote-prefixed and
  colon-inside-bold variants accepted; plain labels refused; a repeated field; the verdict order; the
  three check 10 cases of AC8.

### Inventory

| Identifier | Kind | Cell |
|---|---|---|
| `**To-do:**`, `**Reuse:**` | task field labels | none: a label, the build's interface 6 |
| `check_card_task` | shell function | `sh.function`; `--suggest check_card_task --as sh.function` answered OK |
| `TASK_SKELETON_FORMAT_1_4` | shell constant | none: `sh.constant` is undeclared, as KICK-aRoutedQuill-1 recorded |
| `render_task_section` | self-test helper | `sh.function`; `--suggest render_task_section --as sh.function` answered OK |
| `MANIFEST task REFUSED` | refusal head | none |

### Files touched (estimate)

`skills/session-kickoff/manifest-check.sh` · `skills/session-kickoff/manifest-check.test.sh` · `skills/session-kickoff/MANIFEST-TEMPLATE.md` · `memory/guides/SESSION-KICKOFF.md` · `WIRE-INTO-PROJECT.md` · `memory/map/features/session-kickoff.md` · `memory/map/generated/symbols.json`

### Rollout

- Live at landing for this repository's sessions: a READY body without the eight filled fields is
  refused at the append. The refusal names the remedy.
- Built after `TOOL-aOrientedCast-1` inside order 1 (§8 F1).
- The pass commit carries the manifest re-stamps and runs `gen_map.py --write` first.
- This running session's stored card holds six fields. `--card --check` is unchanged, so it still
  checks clean; a later append from this session must carry eight.

### Alternatives rejected

- **Accepting unbolded labels as well.** Twenty of the twenty-eight measured cards write none, but
  their fields are not the skeleton's under another spelling: they write `scope in`, `scope out`,
  `slug` and one-line summaries. A second grammar would be a fuzzy matcher the renderer must mirror,
  and the build's interface 6 pins the bold labels.
- **Grading the stored card in `--card --check` too.** Every card written before this unit would
  red, this session's included, with no write to repair it short of a new kickoff.
- **Labels typed into the refusal code.** A second spelling of the field set beside the constant.
- **A placeholder rule over short values.** No measured value was short, but a short value can be a
  true answer; the closed list catches the skeleton and the forms a hurried session types.
- **Guidance for the two fields in the engine's Step 3.** It spends headroom another unit needs, and
  the session copies the skeleton, not Step 3.

## 5. Production-readiness checklist

- security — no new write path; the refusal narrows what the card accepts and grants nothing.
- perf / scale — one `awk` per append over a body of a few kilobytes; no new git or reader spawn.
- error / empty / loading states — every failing field is named in one refusal, so one fix cycle
  clears it; the card is byte-identical after any refusal; a body with no READY line is untouched.
- observability — the refusal names each field and its value; check 10's NOTE names the re-paste.
- risks — a session used to writing plain labels meets a refusal on its next kickoff; the refusal
  names the skeleton verb, which prints the exact shape. An adopter can stay on the 1.4 region
  indefinitely; the WARN and the NOTE print on every full run until it upgrades.
- testing — arms in the self-test beside the K2 block, observed RED against the base checker before
  they land; the suite runs once, at the close.
- migration — format 1.5 with the 1.4 region accepted under a 1.4 marker, as §4 states; gov and the
  seed move in the same commit.
- user docs — the skeleton is the field set's user doc; the retrofit recipe gains its step.

## 6. Acceptance criteria

The fixture for AC2 to AC8 is a `git clone --local` of the pass's HEAD under a short root,
`%TEMP%/k1c`, with a card written by `bash skills/session-kickoff/manifest-check.sh --card --write --session k1fx`
there. Each body below also carries a `## read` line citing `AGENTS.md`, so DEAD PROBE does not
answer first, and a READY line whose base is the clone's HEAD. "Byte-identical" means `cmp` against
a copy of the card taken before the append.

- **AC1** — When `bash skills/session-kickoff/manifest-check.sh --task-skeleton` runs from a directory
  outside any repository, it exits 0 and prints eight field lines in the order Title, Goal, IN scope,
  OUT / non-goals, To-do, Reuse, Acceptance check, Gates it must pass, with `**To-do:**` and
  `**Reuse:**` spelled as interface 6 pins them.
  Red when: either label is missing, misspelled or out of order.
- **AC2** — When a body whose `## task` fills all eight fields with one sentence each is piped to
  `bash skills/session-kickoff/manifest-check.sh --card --append --session k1fx` in the fixture, it
  exits 0, prints its `appended —` line, and the card's tail carries the eight fields.
  Red when: a filled eight-field body is refused.
- **AC3** — When a body filling only the six fields the base skeleton names is appended with
  `--card --append --session k1fx`, the verb exits 1 naming To-do and Reuse as absent, in one
  refusal, and the card is byte-identical.
  Red when: a six-field body lands, or the refusal names only one of the two.
- **AC4** — When a body is appended whose Reuse value is `…`, whose To-do value is empty, whose Gates
  value is `TBD`, whose IN scope value is `<the scope>`, or whose OUT value is `none`, each in its own
  append, the verb exits 1 naming that field as empty or a placeholder, and the card is
  byte-identical.
  Red when: any of the five lands.
- **AC5** — When the output of `--task-skeleton` is appended as the body's task section, the verb
  exits 1 naming all eight fields.
  Red when: the shipped skeleton passes its own rule, which would make the rule unable to refuse.
- **AC6** — When the eight filled values are appended with `> ` quote prefixes and every qualifier
  kept, the Acceptance qualifier spanning two lines, and again with no quote prefix and the OUT label
  written `**OUT / non-goals:**`, each exits 0; when they are appended as plain `- Title: x` lines, the
  verb exits 1 naming every field absent; when the Reuse field line appears twice, it exits 1 naming
  Reuse as carried twice.
  Red when: a variant the grammar admits is refused, plain labels land, or a repeat lands.
- **AC7** — When a token-free body with a READY line is appended, it still exits 1 on DEAD PROBE; a
  body with a READY line and no `## task` still exits 1 on the presence refusal; a body with all eight
  fields and a READY line pinning a stale base still exits 2 on the stale-BASE refusal; and a body
  carrying no READY line and no `## task` appended to a card whose READY line is real still exits 0.
  Red when: the new refusal answers before another verdict, or grades a body with no READY line.
- **AC8** — When, in the fixture, `memory/guides/SESSION-KICKOFF.md` has its marker set to `v1.4` and
  its sealed region taken from that file as it stood at base `646d4a73`, then
  `bash skills/session-kickoff/manifest-check.sh` prints no `check 10 FAILED` line and prints both the
  format `WARN` naming v1.5 and the check 10 `NOTE`; with the marker then set to `v1.5`, it prints
  `check 10 FAILED` with the "differs" message; with the marker back at `v1.4` and one character of
  that region edited, it prints `check 10 FAILED` again.
  Red when: the 1.4 region passes under a 1.5 marker, an edited 1.4 region passes, or the untouched
  1.4 region reds under a 1.4 marker.
- **AC9** — When `bash skills/session-kickoff/manifest-check.sh` runs in the worktree after the pass
  commit, it exits 0 and prints no `WARN: manifest format` line.
  Red when: gov's manifest lags the format, or its region differs from the constant.
- **AC10** — When `bash tools/check-kit-versions.sh` runs after the pass, it exits 0, and
  `grep -c "kickoff-manifest: v1.5" skills/session-kickoff/MANIFEST-TEMPLATE.md` prints 1.
  Red when: the seed's marker and `MANIFEST_FORMAT` disagree.
- **AC11** — When `grep -n "v1.5" WIRE-INTO-PROJECT.md` runs, it finds the re-paste step, the marker
  step and the result tree; `grep -c "kickoff-manifest: v1.4" WIRE-INTO-PROJECT.md` prints 0.
  Red when: the recipe still bumps adopters to 1.4.

## 7. Gates

`kickoff-manifest ratchet` · `manifest-check self-test` · `scratch-guard self-test` · `lexicon naming predicates` · `install-prefix (shipped surface)` · `shell hygiene (a loop fed by a command substitution)` · `harness arms (fail branches armed or pinned)` · `kit version markers` · `kit epoch (shipped bytes move, the version moves)` · `govkit runbook parity` · `memory hygiene` · `codebase-map coverage + freshness` · `spec tokens (a spec's own names resolve)` · `recall floor` · `recall floor arms`

New arm: skills/session-kickoff/manifest-check.test.sh · covers AC1 AC2 AC3 AC4 AC5 AC6 AC7 AC8 · the base checker, whose skeleton has six fields and whose append lands a task section with any field missing or unfilled · `FLOOR_ASSERTIONS` rises by the assertions added

AC9, AC10 and AC11 are direct observations of this repository and add no arm.

## 8. Open questions

- **F1 — Order 1 is shared with `TOOL-aOrientedCast-1`, and the two write sets intersect.** Both
  commits re-stamp the kickoff manifest's audit block, because each touches a watched file, and both
  regenerate `memory/map/generated/symbols.json` with its generator, which M6's clause 3 names.
  (a) Keep order 1 for both and sequence them inside it, `TOOL-aOrientedCast-1` first. The value
  still says what is true, that neither consumes the other's output; M6's clause 1 already forbids
  running them together, and the harness dispatches one unit per call.
  (b) Move this unit to order 2 and every later unit up by one. That rewrites the `order` verb of
  nine sibling specs outside this group and changes nothing that runs.
  Recommendation: (a).
  RESOLVED (agent, 2026-10-11, delegated): (a). The order verbs stay as the roster names them, and
  each spec's Rollout records the sequence.
- **F2 — What does a normal `govkit update` do to an adopter whose manifest carries the six-field
  region?**
  (a) Red until re-pasted. The update overwrites the checker, check 10 reds the adopter's ratchet
  leg, and the WARN plus the retrofit recipe are the remedy. This is what the region's origin chose
  when it first sealed an absent region.
  (b) Format 1.5 with the 1.4 region accepted under a marker older than 1.5, a NOTE naming the
  re-paste, and the format WARN already printing; a 1.5 marker demands the new region.
  (c) A regenerate step in the kickoff-manifest descriptor that rewrites the adopter's region on
  update. It needs a new checker verb and a descriptor row in another kit.
  Recommendation: (b). The build's expected improvement says adopters get all of it through a
  normal update, and only (b) and (c) keep that update green.
  RESOLVED (agent, 2026-10-11, delegated): (b), by M3. (c) is discarded by veto 2, a new public
  surface; (b) satisfies more of the build's stated outcomes than (a) and needs nothing (c) needs.

## 9. Revision log

- rev-1 · 2026-10-11 · initial draft.

## 10. Reuse audit

`tools/codebase-map/reuse_lookup.py` over "refuse a kickoff card append whose task section leaves a
field empty or a placeholder" ranked no field grader; it surfaced the kickoff checker's own
SessionStart key and unrelated `*Refused` classes. The seam this unit extends, read directly, is
`add_card_body` in `skills/session-kickoff/manifest-check.sh`, whose existing `## task` presence
refusal the field rule sits beside, and `TASK_SKELETON`, which stays the one field set and now also
supplies the labels the rule grades. The format-WARN channel and check 10's region compare are reused
for the adopter contract instead of a new mechanism. The placeholder set was measured, not assumed:
the probe described in §4 Evidence ran this unit's grammar over the 28 stored cards and the skeleton,
recording the hits (the skeleton's eight values) and the near-misses (the closing marker absorbed
into the last field, and twenty cards with no bold label).

Recall terms used: `sealed task region TASK_SKELETON check 10 task-skeleton manifest format
MANIFEST_FORMAT card append READY retrofit seed` — which surfaced `KICK-cKeyedLaunchpad-4` (the
region's origin and its red-on-arrival precedent), `KICK-aRoutedQuill-1`, `TOOL-aReplayedCard-11`
(the write-boundary `## task` refusal), `KICK-aReplayedCard-3`, `TOOL-aReplayedCard-8` and
`TOOL-cMendedVintage-16` (the READY anchor's `- ` form).
