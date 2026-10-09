# KICK-aRoutedQuill-1 — the kickoff writes a brief the owner confirms, and the card routes the session to its units

**Status:** SPECCED · rev-4 · 2026-10-09 · node a · Tier-2 · base 6473ae38 · streams kickoff · order 2 · closes TOOL-aReplayedCard-11 · ratified 2026-10-09

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-09-prompt-KICK-aRoutedQuill-1-build-brief.md](../prompts/2026-10-09-prompt-KICK-aRoutedQuill-1-build-brief.md) | journal | — |
| [2026-10-09-prompt-TOOL-aRoutedQuill-1-0-run-handoff.md](../prompts/2026-10-09-prompt-TOOL-aRoutedQuill-1-0-run-handoff.md) | journal | TOOL-aRoutedQuill-1 TOOL-aRoutedQuill-2 TOOL-aRoutedQuill-3 TOOL-aRoutedQuill-4 TOOL-aRoutedQuill-5 PLAY-aRoutedQuill-1 TOOL-aRoutedQuill-6 TOOL-aRoutedQuill-7 |

<!-- /gen:spec-records -->

## 1. Goal

A kickoff leaves the owner's prompt in the conversation and tells no machine which unit the session
builds. This unit makes the kickoff of a code build write that prompt as a committed brief record the
owner confirmed with "go". It gives the orientation card a `## route` section naming the build, each
unit with its spec, and the brief, which `--card --append` refuses unless every one of them resolves.
The write gate and the subagent hand-off read that section; this unit writes and verifies it.

## 2. Scope (IN)

- **S1** — `manifest-check.sh --brief-skeleton` prints the `BRIEF_SKELETON` constant: the brief
  record's skeleton, then the card's `## route` skeleton, each under one comment line saying where it
  goes and when. It answers before the repository probe and exits 0 with no fail branch, as
  `--task-skeleton` does. Observed by AC1.
- **S2** — Engine Step 3 gains one sentence: a task that writes product code also gets a brief,
  drafted from the skeleton. It carries no backticked `git` span. Observed by AC9.
- **S3** — Engine Step 5 gains one clause: the owner's answer to the hand-back is quoted under the
  brief's `## Owner confirmation`, and the skeleton says when to append its `## route`. The clause is
  mode-blind, so Step 5b's "as Step 5 does" carries it into an unattended run. Observed by AC9.
- **S4** — `--card --append` grades a body's `## route` section by §4 "The route rules" and refuses
  a miss with exit 1, naming the line and the rule, the card byte-identical. The route's paths and
  ids ride the two spawns the citation check already makes. Observed by AC4, AC5 and AC10.
- **S5** — A route lands only on an oriented card: a body carrying `## route` and no real READY line
  is refused while the stored card's READY line still reads `READY — none yet`. Observed by AC6.
- **S6** — A card holds at most one `## route` section. A READY body overwrites the card's tail as
  today; a later body carrying `## route` and no READY line takes the stored section's place, above
  the READY line. Observed by AC2 and AC3.
- **S7** — An unarmed route check refuses rather than passes: a route in a tree whose
  `.memory-tree.conf` declares no `MEMORY_ROOT`, or whose id reader yields no id set, exits 2 naming
  what is missing. The conf read inside `render_card` moves into `read_memory_root`, which both
  callers use, and the `live —` cell's three forms stay byte-identical. Observed by AC8.
- **S8** — `--card --append` refuses, exit 1, a body carrying a real READY line and no `## task`
  section. The refusal sits after the DEAD PROBE check, so a token-free body keeps that verdict. This
  is the write-boundary refusal TOOL-aReplayedCard-11 asks for. Observed by AC7.
- **S9** — The manifest's §B card bullet in `memory/guides/SESSION-KICKOFF.md` names the route, and
  its `last-audit` and `last-body-change` stamps move. The session-kickoff dossier's card prose names
  the route, and `memory/map/generated/symbols.json` is regenerated for the two new functions.
  NOT OBSERVED by a criterion: the `kickoff-manifest ratchet` and `codebase-map coverage + freshness`
  legs grade these records.

## 3. Non-goals (OUT)

- Grading the brief's content. The route check verifies the brief path is tracked inside the build
  folder. The sections of a prompt-mode record are graded by the structural rule TOOL-aQuotedBrief-1
  builds, and TOOL-aRoutedQuill-7 repoints that rule at this unit's skeleton.
- Machine-observing that the owner said go. No checker sees a conversation: the session quotes the
  answer, and the owner reads the brief before giving it.
- Reading a routed unit's status. Whether a unit is buildable is the write gate's question at write
  time, because the status moves after the append.
- Re-grading a stored route with `--card --check`. It keeps judging the route's paths and ids for
  existence, like any other token on the card.
- A route spanning two builds. A section carries one `- build:` line; a session switching builds
  appends a new route.
- The sealed task skeleton. `TASK_SKELETON` is untouched, so check 10 compares the same bytes it
  compares today.
- The engine split KICK-aReplayedCard-5 asks for. This edit fits the engine's headroom (§4 Rollout).
- The kickoff-manifest kit version. It moves once, after the build's last unit touching that kit.
- Retrofitting briefs or routes for landed builds or live cards.

### Edges

- **consumes-from** external — TOOL-aQuotedBrief-1's brief shape as specced: the four `##` sections,
  the five `###` sub-heads and the two single-line forms its §4 spells. This unit's skeleton spells
  them byte for byte, so a record written from it passes the five-sub-head rule that unit builds.
- **hands-off** `TOOL-aRoutedQuill-2` — the `## route` grammar in §4, and the guarantee that a stored
  route's ids, spec pairings and paths resolved at append time. The gate re-reads each routed spec's
  status at write time.
- **hands-off** `TOOL-aRoutedQuill-4` — the `## route` lines, at most one section per card, for the
  SubagentStart injection to carry verbatim.
- **hands-off** `TOOL-aRoutedQuill-7` — the `--brief-skeleton` verb, whose `### ` list under
  `## The brief` that unit's repointed prompt-brief rule reads as its required sub-heads.

## 4. Design

### Evidence

Read at `6473ae38` on 2026-10-09.

- `--locations` and `--task-skeleton` answer in a loop ahead of the repository probe, print, and exit
  0 with no fail branch (`skills/session-kickoff/manifest-check.sh:82-91`). The task field set is a
  heredoc constant (`skills/session-kickoff/manifest-check.sh:70-80`). A third such verb adds no site
  `check-arms.py` counts, because its pattern reads `fail <n> "` and the card verbs never call `fail`.
- `add_card_body` (`skills/session-kickoff/manifest-check.sh:884-919`) runs the body's READY count,
  the citation check, DEAD PROBE, the stale-BASE refusal, the card's shape, then the cap. A body with
  a real READY line overwrites the card's tail (`:905-908`); one without is inserted above the tail's
  READY line (`:910`).
- `check_card_citations` (`skills/session-kickoff/manifest-check.sh:798-857`) spawns one
  `git ls-files -- …` and one `corpus_ids.py --print-defined-ids`, and leaves the tracked set in
  `$CARD_TMP/tracked` and the defined set in `$CARD_TMP/ids`. A path token is a slash and an
  extension (`:768-792`), so every route path is already judged for existence. The script spells no
  id grammar of its own (`:620-621`).
- Only `--card --check` refuses a real READY line with no `## task`
  (`skills/session-kickoff/manifest-check.sh:931-934`). The self-test's K2 AC3 arm pipes a token-free
  body carrying a READY line and expects DEAD PROBE (`manifest-check.test.sh:1080-1083`).
- `render_card` reads `MEMORY_ROOT` from `.memory-tree.conf` inline
  (`skills/session-kickoff/manifest-check.sh:405-411`).
- Step 5 hands back with "say go" and forbids building before it
  (`skills/session-kickoff/SKILL.md:206-207`). The engine is 18087 bytes against a declared ceiling of
  18432 (`tools/template-size-limits.txt`) and a recorded high-water of 18369
  (`tools/template-size-highwater.txt`). PINNED at `6473ae38` on 2026-10-09: 282 bytes before the
  advisory WARN, 345 before the red.
- The scratch-guard self-test feeds every backticked `git ` span between the engine's Step 0 and
  Step 5 to the commit deny on a sentinel card (`tools/hooks/scratch-guard.test.sh:609-614`).
- A record whose `**Serves:**` id no spec H1 defines prints a `B` row
  (`tools/memory-tree/gen_build_index.py:730-732`), and an unbound record counts against a
  shrink-only pin. A brief therefore commits with the specs it serves, never before them.
- The id-defining H1 is the first unfenced H1 whose first token is an id
  (`tools/memory-tree/tree_lib.py:202-225`).
- The unattended prompt path already points at the kickoff checker for its field set
  (`tools/unattended/VERBS.template.md:537`) and writes its record under `builds/<slug>/prompts/`
  (`:548`). The unattended kit's `requires` does not name `kickoff-manifest`
  (`tools/unattended/kit.toml:10`); the kickoff kit requires nothing
  (`tools/govkit/entries/kickoff-manifest.kit.toml:12`).

### Flow

The attended sequence:

1. Step 3 derives the task fields as today. When the task writes product code, the session also
   drafts the brief from `--brief-skeleton`. `## The prompt` quotes the message that asked for the
   build. `## The brief` restates the fields as Goal, numbered Items, Acceptance, Gates, Non-goals
   as the cut-line alone, Limitations as every constraint the build must respect, and Reuse from
   Step 4's two probes. `## Drawn from the session` quotes each earlier passage the brief relied on,
   naming its speaker.
2. Step 5 writes the brief to disk, untracked, and echoes it beside the READY card. The READY body
   does not cite the brief's path: the append would annotate an untracked path, and the repair commit
   that follows the append must not sweep the brief in (KICK-aReplayedCard-3).
3. The owner says go, or adjusts a field. Each hand-back adds an `Asked:` line and an `Answer:` line
   under `## Owner confirmation`, verbatim, and an adjustment is folded into the brief before the next
   one. The last pair is the go.
4. The spec pass writes the unit specs. The brief takes its final name from the first unit it
   serves, its `**Serves:**` line names every unit it serves, and it is committed with those specs.
5. The session pipes the skeleton's route section, filled, to `--card --append`. It appends again
   whenever the set of tracked specs it works changes, and each append takes the previous section's
   place.

An unattended run follows steps 4 and 5 with no owner turn. Its brief line names the run's prompt
record, or the build README where the owner committed the folder. A run whose unit specs already
exist may carry the route on its READY append, which the verb accepts.

### Data model

`--brief-skeleton` prints `BRIEF_SKELETON`, verbatim:

```markdown
<!-- the brief: <MEMORY_ROOT>/builds/<build>/prompts/<date>-prompt-<FAMILY>-<slug>-<seq>-brief.md, named for the first unit it serves; drafted at Step 3, written at Step 5, committed with that unit's spec after go -->
# Brief — <build>: <the build in a few words>

**Serves:** research <FAMILY-slug-seq> [<FAMILY-slug-seq> …]

## The prompt

> <the owner's words that asked for this build, verbatim>

## The brief

### Goal
<the build in one or two sentences, readable with no conversation>

### Items
1. <one thing the owner asked for>

### Acceptance
<the observation that proves each item>

### Gates
<the gate legs the build keeps green>

### Non-goals
<the cut-line: what the build must not build>

### Limitations
<every constraint the build must respect>

### Reuse
<the seam the reuse probe named and the records the recall query returned, or that none fits>

## Drawn from the session

> <a passage the brief relied on, verbatim>
— <owner|agent>, <turn or time>

## Owner confirmation

Asked: <the hand-back question, verbatim>
Answer: <the owner's reply, verbatim>

<!-- the card's route: once every spec it names is tracked, pipe from the heading down to --card --append --session <sid>; append again when that set changes -->
## route
- build: <build>
- unit: <FAMILY-slug-seq> · spec <repo-relative path>
- brief: <repo-relative path of the brief, or of the build README an unattended run was authorized by>
```

The record's filename follows check 5's grammar, and check 21 joins its id to the `**Serves:**` set;
a second brief for the same unit on one date takes the tail `-brief-2`. The four `##` sections and
the five sub-heads up to `### Non-goals` are TOOL-aQuotedBrief-1's §4 fence. `### Limitations` and
`### Reuse` are new and sit after the five, so a reader grading those five in order still finds them.

Four constraints keep the record TOOL-aQuotedBrief-1's:

- Every quote under `## Drawn from the session` names its speaker, `owner` or `agent`.
- The two single-line forms keep that unit's exact spellings. `## Drawn from the session` is the
  single line `none` when the brief relied on nothing outside the prompt, and `## Owner confirmation`
  is then the single line `not asked — the brief draws on nothing outside the prompt`.
- That unit's rule 5 makes the confirmation mandatory only when the session section holds a quote.
  An attended kickoff always asks, so its go is always recorded as the `Answer:` line and it never
  writes the `not asked` form.
- Nothing under `## The brief` opts a build into the spec audit. `read_audit_ask_record` reads only
  `## The prompt` (TOOL-aQuotedBrief-1 S6), so an ask written only in the brief opts nothing in.

The route grammar, which TOOL-aRoutedQuill-2 and TOOL-aRoutedQuill-4 read:

- The section is the line `## route` through the line before the next `## ` heading, the next READY
  line, or the end.
- `- build: <build>`, exactly once, the slug letters and digits only.
- `- unit: <id> · spec <path>`, one or more, with nothing after the path.
- `- brief: <path>`, exactly once.
- No other non-blank line and no backticks. Line order is free.

### The route rules

`check_card_route` runs over the body's section after the card's shape check. Each refusal names the
offending line and the rule, points at `--brief-skeleton` for the shape, and leaves the card
byte-identical.

| Rule | Refuses | Exit |
|---|---|---|
| R0 | a blank or absent `MEMORY_ROOT`, or no id set because the reader is absent or exited 3 | 2 |
| R1 | more than one `## route` section in the body | 1 |
| R2 | a line outside the grammar, or a missing or repeated `- build:` or `- brief:` line, or no `- unit:` line | 1 |
| R3 | a unit id absent from `$CARD_TMP/ids` | 1 |
| R4 | a spec path absent from `$CARD_TMP/tracked`, outside `<MEMORY_ROOT>/builds/<build>/spec/`, or carrying no unfenced H1 whose first token, backticks and asterisks stripped, is the unit id | 1 |
| R5 | a brief path absent from `$CARD_TMP/tracked`, or neither under `<MEMORY_ROOT>/builds/<build>/prompts/` nor that build's `README.md`, the unattended form | 1 |
| R6 | a body with no real READY line, appended to a card whose READY line is `READY — none yet` | 1 |

No rule spawns git or the reader. R3 to R5 read the two sets the citation check already holds, and
R4 reads at most one spec file per unit line. When the body carries a route and no READY line, the
write path filters the stored `## route` section out of the tail before inserting the body. The order
in `add_card_body` becomes: READY count, citations, DEAD PROBE, the `## task` refusal, stale BASE,
card shape, route rules, cap.

### Engine text

The engine grows by at most 282 bytes, so neither its ceiling nor its high-water moves. Measured
against the wording below, the two edits cost 211 bytes:

- Step 3, a new paragraph after the "split or clarify before any code" sentence: **A task that writes
  product code also gets a brief**, from `bash <check-script> --brief-skeleton`.
- Step 5, after "Do not start building until the user confirms.": Quote that answer under the
  brief's `## Owner confirmation`; its skeleton says when to append its `## route`.

### Inventory

| Identifier | Kind | Cell |
|---|---|---|
| `--brief-skeleton` | checker verb | none: a flag carries no naming cell |
| `BRIEF_SKELETON` | shell constant | none: `python tools/lexicon/lexicon.py --suggest BRIEF_SKELETON --as sh.constant` answered that `sh.constant` is undeclared |
| `KICKOFF_BRIEF_SKELETON` | heredoc delimiter | none |
| `check_card_route` | shell function | `sh.function`; `--suggest check_card_route --as sh.function` answered OK |
| `read_memory_root` | shell function | `sh.function`; `--suggest read_memory_root --as sh.function` answered OK |
| `## route` | card section | none: a heading, owned by this unit under the build's shared interface |

### Files touched (estimate)

`skills/session-kickoff/manifest-check.sh` · `skills/session-kickoff/manifest-check.test.sh` · `skills/session-kickoff/SKILL.md` · `memory/guides/SESSION-KICKOFF.md` · `memory/map/features/session-kickoff.md` · `memory/map/generated/symbols.json`

### Rollout

- The route is inert until TOOL-aRoutedQuill-2 reads it. Nothing requires one before then, and a
  card without one appends and checks as today. The one refusal an existing flow can meet is S8's,
  and Step 5's body always carries `## task`.
- If the engine edit cannot fit its 282 bytes, the unit trims engine prose in the same commit.
  Raising the declared ceiling is an owner decision, and the engine split is its own ask.
- The manifest owes `last-audit` and `last-body-change` with a delta line in the commit message,
  because `manifest-check.sh` and `SKILL.md` are in its `watch:`.
- `gen_map.py --write` runs before the push, because two new shell functions stale `symbols.json`.
- The kickoff-manifest kit version moves once, after the build's last unit touching that kit.

### Alternatives rejected

- **Annotating a route miss as `UNVERIFIED`**, as the citation check does for other tokens. A route
  is read by a gate and injected into subagents, so an annotated route hands both a line naming
  something that is not there; refusing at the append gives the remedy at the moment it is cheapest.
- **A route only on the READY append.** In an attended session the brief is untracked until go and
  the specs come after it, so a READY-only route could never name them.
- **A brief template shipped as its own file.** A new shipped file needs a descriptor row and a
  destination, while the checker is overwritten whole in every adopter and already hosts the sealed
  task field set the brief restates.
- **Spelling the two shapes in the engine.** The engine has 282 bytes of headroom, and a route shape
  there would be a second spelling beside the checker that parses it.
- **Requiring `## The brief` inside the brief file.** It refuses an unattended run whose brief is the
  README the owner committed.
- **Asking the id reader for id-to-path pairs.** It changes the reader's argv, which the K2 spawn arm
  pins, and a second kit, for one equality the spec's own H1 answers.
- **Grading the routed spec's status at the append.** The status moves after the append, and
  buildability is the write gate's question.

## 5. Production-readiness checklist

- security — no new write path: the route narrows what the card accepts and grants nothing. A brief
  quotes the owner verbatim, so a credential in a prompt is scrubbed before the commit (charter §5).
- perf / scale — no new git or reader spawn; the rules read the two sets already held, the conf, and
  at most one spec file per unit line. AC10 pins the spawn count.
- error / empty / loading states — a malformed route, an un-oriented card, an absent `MEMORY_ROOT`
  and an absent id set each refuse by name, the card byte-identical. A `/clear` rewrites the card and
  its route with it, so the session kicks off again.
- observability — the `appended —` line is unchanged; a refusal names the route line and the rule;
  the stored route is readable through `--card --replay`.
- risks — the attended go is recorded by the session, not observed by a machine. The route check is
  existence and pairing, never truth, and the gate reads a status the agent writes. The engine sits
  282 bytes under its high-water before this edit.
- testing — arms in `skills/session-kickoff/manifest-check.test.sh` beside the K2 block, in its
  scratch clone, each observed RED against the base checker before it lands; the suite runs once,
  after the build.
- migration — none: cards are per session, a card without a route keeps working, and the `## task`
  refusal meets only a body Step 5 never writes.
- user docs — the engine and the skeleton verb are this path's user docs; the manifest's §B card
  bullet names the route.

## 6. Acceptance criteria

- **AC1** — When `bash skills/session-kickoff/manifest-check.sh --brief-skeleton` runs from a
  directory outside any repository, it exits 0 and prints `## The prompt`, `## The brief`,
  `## Drawn from the session`, `## Owner confirmation` and `## route` in that order, with `### Goal`,
  `### Items`, `### Acceptance`, `### Gates`, `### Non-goals`, `### Limitations` and `### Reuse` in
  that order under the brief, and the three route line shapes.
  Red when: a heading is missing or out of order, or the verb exits 2 for want of a repository.
- **AC2** — When a body carrying a conforming `## route` and no READY line is piped to
  `manifest-check.sh --card --append` against a card whose READY line is real, in the K2 fixture clone
  extended with a tracked brief in its fixture build, it exits 0 and the card holds the section above
  its last line, the READY line.
  Red when: a conforming route is refused, or lands below the READY line.
- **AC3** — When a second conforming route body naming another tracked spec is appended to that card,
  `grep -c '^## route'` over the card reads 1 and the section is the second body's.
  Red when: the card holds two route sections, or keeps the first.
- **AC4** — When a route's unit line names an id no spec H1 defines, pairs an id with a spec whose H1
  defines another, or names an untracked spec or one outside the build's `spec/` folder, and when its
  brief line names a path outside the build folder, or a tracked path inside it that is neither under
  its `prompts/` folder nor its `README.md`, such as the unit's own spec, `--card --append` exits 1
  naming the line and the rule, and `cmp` finds the card byte-identical.
  Red when: any such route is appended, or annotated `UNVERIFIED` instead of refused.
- **AC5** — When a route body lacks its `- build:` line, carries no `- unit:` line, carries two
  `- brief:` lines, carries a stray line, or the body carries two `## route` sections,
  `--card --append` exits 1 naming the shape and `--brief-skeleton`, and the card is byte-identical.
  Red when: a malformed route lands.
- **AC6** — When a conforming route body with no READY line is appended to a card whose READY line
  still reads `READY — none yet`, `--card --append` exits 1 naming the missing kickoff, and the card
  is byte-identical.
  Red when: a route lands on a card no kickoff has appended to.
- **AC7** — When a body carrying a real READY line, a tracked path and no `## task` section is
  appended, `--card --append` exits 1 naming the missing `## task`, and the card is byte-identical;
  the token-free body of the K2 AC3 arm still exits 1 on `DEAD PROBE`.
  Red when: the task-less body is appended, or the K2 AC3 verdict changes.
- **AC8** — When a conforming route body is appended in a fixture whose `.memory-tree.conf` declares
  no `MEMORY_ROOT`, and again where the id reader exits 3, `--card --append` exits 2 naming the
  missing piece, and the card is byte-identical.
  Red when: a route is appended with its folder or its ids unchecked.
- **AC9** — When `grep -n -- '--brief-skeleton' skills/session-kickoff/SKILL.md` runs, it finds the
  Step 3 sentence, and Step 5 names `## Owner confirmation` and `## route`; then
  `bash tools/check-template-size.sh skills/session-kickoff/SKILL.md` prints `template-size OK` and
  no `WARN` line.
  Red when: the engine names neither, or grows past its recorded high-water.
  figure: the ceiling and the high-water are DERIVED at observation time from
  `tools/template-size-limits.txt` and `tools/template-size-highwater.txt`.
- **AC10** — When AC2's conforming route body is appended under the K2 spawn shims, `SPAWN_LOG` holds
  exactly one `ls-files -- ` line and one `corpus_ids.py --print-defined-ids` line.
  Red when: the route rules add a git spawn or a reader spawn.

## 7. Gates

`kickoff-manifest ratchet` · `kickoff engine size <=18KiB` · `manifest-check self-test` · `scratch-guard self-test` · `lexicon naming predicates` · `install-prefix (shipped surface)` · `shell hygiene (a loop fed by a command substitution)` · `memory hygiene` · `codebase-map coverage + freshness` · `spec tokens (a spec's own names resolve)` · `recall floor` · `recall floor arms`

New arm: skills/session-kickoff/manifest-check.test.sh · covers AC1 AC2 AC3 AC4 AC5 AC6 AC7 AC8 AC10 · the base checker, which has no skeleton verb and appends any route and any task-less READY body · `FLOOR_ASSERTIONS` rises by the arms added

## 8. Open questions

- **F1 — Which file holds the one brief shape, and which unit lands first?**
  The other unit is TOOL-aQuotedBrief-1, SPECCED and not built.
  (a) Here. `--brief-skeleton` in the kickoff checker is the one copy: a default kit that requires
  nothing and is overwritten whole in every adopter. TOOL-aQuotedBrief-1 takes a rev before it is
  built. Its prompt path's step 3 points at the verb, as its step 2 already points at
  `--task-skeleton`, and its structural rule reads the `###` list from the verb's output at run time,
  so the two kits cannot drift. It gains `### Reuse`, and the unattended kit names `kickoff-manifest`
  in its `requires` or relies on the default set. This unit lands first, and its consumes-from edge
  becomes a hands-off at that rev.
  (b) There. Build after TOOL-aQuotedBrief-1 and consume its §4 fence. That home is the unattended
  kit, which is opt-in, so a default adopter's attended brief would need a second copy here, and
  `### Reuse` would have no home.
  Recommendation: (a). It costs one rev of a SPECCED spec that no code depends on yet.
  RESOLVED (owner, 2026-10-09): (a), the kickoff kit holds the one brief shape.
  The owner had the two sessions settle the sequencing. On 2026-10-09 the session building
  aQuotedBrief agreed that TOOL-aQuotedBrief-1 builds exactly as specced, with five hard-coded
  sub-heads, and that repointing its structural rule at `--brief-skeleton` is a new unit,
  TOOL-aRoutedQuill-7. So the rev of TOOL-aQuotedBrief-1 that option (a) describes does not happen,
  and the consumes-from edge in §3 stays as written.
- **F2 — Do limitations get a sub-head of their own?**
  The owner's list names limitations beside non-goals. Folding them into `### Non-goals` keeps the
  shape at the five sub-heads TOOL-aQuotedBrief-1 already grades plus `### Reuse`. A
  `### Limitations` sub-head would separate a constraint, such as a size ceiling, from a cut-line, at
  the cost of one more sub-head every reader and the structural rule carry.
  Recommendation: fold, and revisit only if briefs show the two being confused.
  RESOLVED (owner, 2026-10-09): own sub-head, `### Limitations`, after `### Non-goals` and before
  `### Reuse`; §4's skeleton holds the cut-line alone under `### Non-goals`.

## 9. Revision log

- rev-1 · 2026-10-09 · initial draft.
- rev-2 · 2026-10-09 · §3 · §4 · cross-read fold: order 1 to 2, because this unit and
  `TOOL-aRoutedQuill-1` each touch files the kickoff manifest watches, so both re-stamp it and
  cannot share a parallel step.
- rev-3 · 2026-10-09 · §3 · §4 · §8 · AC1 · owner resolved F1 to (a) and F2 to an own
  `### Limitations` sub-head; folded the aQuotedBrief session's sequencing (that unit builds as
  specced, TOOL-aRoutedQuill-7 repoints its rule) and its four record constraints; hands-off to
  TOOL-aRoutedQuill-7.
- rev-4 · 2026-10-09 · §4 · AC4 · the M2 cross-read of 2026-10-09 found R5 admitted any tracked path
  in the build folder as a brief, so a route naming the unit's own spec as its brief passed; R5 now
  admits only a path under the build's `prompts/` folder or the build's `README.md`, the unattended
  form the route grammar already allows, and AC4 adds the own-spec-as-brief refusal.

## 10. Reuse audit

`tools/codebase-map/reuse_lookup.py` over this unit's phrase ranked general `write`, `build` and
`records` symbols and no card seam, and a second phrase naming the card verbs surfaced none of them
either. The seam this unit extends, read directly, is `add_card_body` with `check_card_citations` in
`skills/session-kickoff/manifest-check.sh`, whose two held sets the route rules reuse without a new
spawn. The first probe also surfaced `parse_spec_h1` in `tools/memory-tree/tree_lib.py`, the H1
predicate the pairing rule mirrors rather than calls (§4 Alternatives rejected). The skeleton verb
reuses the `--task-skeleton` pattern in the same script.

Recall terms used: `orientation card append READY task sentinel brief prompt record confirmation
hand-back route spec-before-code` — which surfaced `TOOL-aQuotedBrief-1`, `KICK-aReplayedCard-1`,
`TOOL-aGraftedHelix-2`, `TOOL-aReplayedCard-11`, `KICK-aReplayedCard-3` and `TOOL-cMendedVintage-16`.
