# TOOL-dDerivedDocket-20 — the carrier sweep

**Serves:** journal TOOL-dDerivedDocket-20

S9's record. Every sentence in `tools/unattended/PROTOCOL.template.md` and in
`tools/unattended/SKILL.template.md` that describes ids, slugs, the prompt path or backlog rows, read
against the driver as units 15 to 19 left it, with its verdict. The installed protocol and the
rendered Skill are byte copies of these two, so the verdicts hold for all four files. The reading
was done at this unit's commit; section numbers, not line numbers, locate each sentence, because
the lines moved under this unit's own edit.

Driver behaviours the verdicts cite, each read in `tools/unattended/unattended.sh` at this unit's
parent: every verb is addressed by SLUG, and a value that is id-shaped or carries whitespace is
refused under check 6 with the scaffold recipe, before the slug is even parsed (`is_ids_value`,
`print_scaffold_recipe`); a slug naming a folder that holds only a `BACKLOG.md` is refused under
check 6 with the recipe and that folder's live asks (`check_filing_home`); an `asks:` line is read in
the authorization scan and pinned with `m-base:` and `asks-ready:` at preflight, P5 and P6 refused
under checks 72 and 73, and a mandate whose every id grades `no` under check 75
(`check_ask_mandate`, `check_asks_pinned`); `--plan` prints a fifth `next:` shape,
`(UNDECIDED - plan a unit that closes it, or dispose it)`, for a mandated or self-filed ask nothing
answers (`build_ask_plan`); a `may:` grant is refused under checks 78 and 79 off a `slug` README
(`parse_grants`); the modes are `AUTH_MODES` and the second anchor admits `SECOND_ANCHOR_MODES`.

## The protocol

- §1, "The owner's act is `/unattended <slug>`, or ... an invocation carrying the authorizing
  parameter" — KEPT. Read against the check-6 id refusal: ids are not an owner act that starts a run,
  so the two acts named are still the only two.
- §1, the mode bullets, `prompt` / `recipe` admissible on the second anchor and a `slug` README
  refused there — KEPT. `SECOND_ANCHOR_MODES` is unchanged.
- §1, "its `slug:` names the build" and "absent is `slug`" — KEPT. The authorization scan reads the
  same keys plus `asks:` and `may:`.
- §1, the unit-set rule, "The ids in the GENERATED `gen:build-units` region" — KEPT. The units
  region is still the roster the shrink test compares; a folder's `unit` asks join `--plan`, not
  that region.
- §1, "the narrowing is the slug the owner types" — KEPT, and truer: a typed id list now narrows
  nothing until the owner lands the README the recipe scaffolds.
- §1, the `may:` paragraph, "honoured only from an owner-committed `slug` README" — KEPT, unit 19's
  own sentence, read against checks 78 and 79.
- §2, the run-state path `<MEMORY_ROOT>/builds/<slug>/RUN.md` — KEPT.
- §2, "Freezing the ids keeps a terminal record a record" — KEPT. `units-at-landing` still freezes
  unit ids; `asks-at-landing` is the ask twin, described in the guide.
- §2, the anchor ban, scoped to "a run-state file" and its "authored rows" — CHANGED to every tracked
  file under the run's build folder, citing a foreign id inline or through the link-wrapped
  `--asks --ready` paste. Read against unit 18's check 37, which already grades the whole folder of
  a mandated run, so the carrier was narrower than the leg.
- §2, "A planned unit is minted as a backlog row before the run-state file names it" — CHANGED to an
  ask in the run's own build. Read against design §2.3: a row is owed only by a unit planned before
  its spec, and in either backlog mode it carries the run's own folder slug.
- §2, none at the parent — ADDED: every ask, disposition and header verb a run writes sits in its own
  folder under the folder slug, a sequential pass may declare that folder's `BACKLOG.md`, and the
  pointer to `UNATTENDED-ASKS.md`. Read against `--dispatch`, which admits a build's `BACKLOG.md`
  alone because it overlaps neither the run-state file nor a declared shared record.
- §3, "a prompt-started run OCCUPIES them" and "every verb is slug-addressed" — KEPT, the second read
  against the check-6 id refusal, which is what makes it true of ids too.
- §4, the `keepalive-reaped` and `parked-decisions-surfaced` rows, `--attest <slug>` — KEPT.
- §4, the `asks-disposed` row — KEPT, unit 17's sentence; its terms are the guide's §6.
- §5, "A prompt-authorized run orients from prose" and "Where a start path refuses — a `--prompt`" —
  KEPT. The ids route refuses at preflight too and reaps, which the Skill's new section says.
- §8, the `REVIEW_ROUNDS`, `AUTH_PARAM`, `BRIEF_RECORDED_CUTOFF` and `DISPOSITION_CUTOFF` rows — KEPT.
- §8, the `ASKS_CMD` row, "in the shapes `UNATTENDED-ASKS.md` lists" — KEPT; the guide's §8 now lists
  them, which this row promised before the guide existed.
- §8, the `SHARED_RECORDS` row — CHANGED: it gains "No path may sit under both keys", the carrier of
  this unit's check 38 and conf-load refusal.
- §9, "a run that rewrites the harness child's prompt" — KEPT; a different prompt, the harness's.
- §10, the `prompt` directive scope — KEPT, `TOOL-aPromptedMandate-4`'s, and unchanged by asks.
- §11, "Fails 1 or 2 → a BACKLOG row naming what was seen" — CHANGED to an ask filed in the run's own
  build, carrying what was seen and why it was declined.
- §11, "Record it with `--rescope <slug> --act add`" — KEPT.
- §11, the `Decide AT ONCE` paragraph — MOVED whole to the guide's §5; one sentence points there.
- §11, "a declined one leaves a backlog row" — CHANGED to "a filed ask", the same act as the
  disposition sentence above it.
- §12, "taken in `prompt` and `slug` mode" — KEPT; an ask mandate is `slug` mode.

## The Skill

- Keepalive section, every `--resume <slug>` / `--audit <slug>` form and "no slug exists" — KEPT;
  slug-addressed verbs.
- Which path, the section lead — CHANGED: four paths and one route that is not a run.
- Which path, the opening fence — ADDED: a value mixing a slug and ids is refused before any verb,
  read against check 6's whitespace rule, which refuses the same value at preflight.
- Which path, the first row — CHANGED: a folder that names its units OR carries an `asks:` line.
- Which path, the prompt and playbook rows — KEPT.
- Which path, the ids row — ADDED: ids, a range, a prompt naming ids, or a filing-home slug route to
  the scaffold, read against check 6's two refusals.
- Start a run, the directive table's `prompt` scope and step 1's anchor paragraph — KEPT.
- Start a run, step 3's `--preflight <slug>` — KEPT.
- Start a run, steps 5 and 6 — ADDED: the ask-mandate steps, each pointing into the guide, and the
  pre-flip park, read against preflight's `BACKLOG_MODE` notice.
- Ids go through the scaffold — ADDED, read against `print_scaffold_recipe` and `check_filing_home`.
- Start a run from a PROMPT, the `AUTH_PARAM` fence and the value table — KEPT.
- Start a run from a PROMPT, "A prompt that NAMES IDS is not this path" — ADDED, read against
  ruling D12-a: a prompt-mode folder is the run's own, so a mandate written there would be the run
  authorizing itself.
- Start a run from a PROMPT, steps 3 to 6, `builds/<slug>/`, the six keys including `ids`, and
  `authorized-by: prompt` — KEPT; `ids:` is the generated key the scaffold also writes empty.
- Playbook paths, their `--record-piece <slug>` / `--record-set <slug>` forms and "uses the PROMPT
  path" — KEPT.
- While it runs, every `--park`, `--propose`, `--brief`, `--rescope`, `--dispatch`, `--status` and
  `--audit` form addressed by slug — KEPT.
- While it runs, "One that fails the first two clauses is a BACKLOG row" — CHANGED to an ask filed in
  this build, matching protocol §11.
- While it runs, "branch on all four shapes it prints" — CHANGED to every shape, with the UNDECIDED
  shape oriented and never dispatched, read against `build_ask_plan` and the `next:` ladder.
- Record each review round, `--review <slug> --subject <id-or-slug>` and "the BUILD SLUG" — KEPT.
- Resume, Close, Land and Hold, every slug-addressed form and the scheduler name
  `unattended-resume-<slug in lower case>` — KEPT.
- If it cannot finish, "a mismatch worth a backlog row" — KEPT: a vocabulary gap is filed as a row of
  the build's own backlog in either mode, and the sentence names no location.

## Leg rules units 16 to 19 added, and the sentence that carries each

Each rule is named by what its refusal says, with the carrier sentence it is joined to.

- Unit 16, the check-22 key-table join, which now covers `ASKS_CMD` — protocol §8's `ASKS_CMD` row.
- Unit 17, the check-16 DoD-table join, which now covers `asks-disposed` — protocol §4's `asks-disposed`
  row, with the terms in `UNATTENDED-ASKS.md` §6.
- Unit 18, check 19: a mandate pinned under a mode admitting the second anchor — the guide's §1, "ONE
  authorization path for an ask-driven run: a build README the OWNER landed".
- Unit 18, check 19: a mandate pinned while `ASKS_CMD` is blank — the guide's §6 T1 and §8's
  "blank means the ask contract is not adopted".
- Unit 18, check 19: the pinned `asks:` against the README at the recorded BASE, and a live run's
  README changed at HEAD — the guide's §2 P6, "pinned once and never moves".
- Unit 18, check 19: an `m-base:` that does not resolve, is not the merge-base of the pinned anchor
  and the preflight tree, or is off the history — the guide's §2, "the merge-base of the observed
  anchor and `HEAD` that preflight pins once".
- Unit 18, check 19: a mandated ask with no filed row at `m-base:` — the guide's §2 P5.
- Unit 18, check 19: `asks-ready:` not what the producer says at the pinned tree — the guide's §2,
  "Preflight also pins `asks-ready:`", and §8's call shape 1.
- Unit 18, check 37: a foreign anchor in a mandated run's folder — protocol §2's anchor ban, now
  scoped to every tracked file under the run's build folder.
- Unit 18, check 15: a LANDED mandated record with no freeze, a freeze omitting an ask, or a freeze
  the producer disagrees with — the guide's §6, "The freeze", and §8's call shape 2.
- Unit 19, check 19: a `may:` pin the README at BASE does not declare, a `may:` under a second-anchor
  mode, and a run commit writing `may:` into any build README — protocol §1's `may:` paragraph, one
  clause each.
- This unit, check 38 and the driver's conf-load refusal — protocol §8's `SHARED_RECORDS` row.
