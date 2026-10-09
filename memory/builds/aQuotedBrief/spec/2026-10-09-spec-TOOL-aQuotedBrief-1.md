# TOOL-aQuotedBrief-1 — the prompt record carries a self-contained brief, its session sources, and the owner's confirmation

**Status:** SPECCED · rev-2 · 2026-10-09 · node a · Tier-2 · base fa68a767 · streams tooling · order 1 · ratified 2026-10-09

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

A prompt-mode run's prompt record holds only the bytes the owner typed, so a prompt fired mid-session
("yes, spec it as a build") authorizes a run whose scope lives in the conversation and nowhere on
disk. This unit makes the record stand alone: the run writes a brief that states the build in full,
quotes every session passage the brief relied on, and records the owner's confirmation whenever it
relied on one. Preflight refuses a prompt-mode record that lacks them, so a resumed session, a
compaction or a later reader holds the whole scope.

## 2. Scope (IN)

- **S1** — The prompt path in `tools/unattended/VERBS.template.md` (section `Start a run from a
  PROMPT`) gains the brief at step 3. The prompt record keeps `## The prompt` verbatim and adds three
  `##` sections after it, in this order: `## The brief`, `## Drawn from the session` and
  `## Owner confirmation`. Their shapes are §4 "The record". Observed by AC1.
- **S2** — Step 2 of the same path becomes mandatory when `## Drawn from the session` holds a quote.
  The one `AskUserQuestion` then carries the brief and asks the owner to accept it, edit it or cancel
  the run; a cancel writes nothing, and an edit is folded into the brief before the commit. The gap
  questions step 2 already asks ride the same call. A brief quoting nothing keeps today's rule: ask
  only for gaps. Observed by AC2.
- **S3** — `tools/unattended/SKILL.template.md` section `Start a run from a PROMPT` names the brief
  at its step 3 and the conditional confirmation at its step 2, as pointers into the verbs file.
  NOT OBSERVED by a criterion of its own: the skill size and wiring legs grade the render, and S1's
  text is the rule.
- **S4** — `--preflight` refuses a prompt-mode run whose README `opened:` date is on or after
  `PROMPT_BRIEF_CUTOFF` when no record under `prompts/` at the pinned BASE carries `## The prompt`,
  or when any record that does fails §4 "The structural rule". The refusal is a new numbered check in
  `verb_preflight`, after the authorization read sets the mode and before the write gate, so a
  refusal writes no run-state file. It is not placed in `check_authorization`, which `--close`
  re-runs as `authorization-reachable`: that item has no override, and BASE is pinned, so a second
  reading could only strand a run. Observed by AC1, AC3, AC4 and AC5.
- **S5** — `PROMPT_BRIEF_CUTOFF` is a new date key, BLANK meaning off and announced on stderr, on the
  terms the sibling date keys use. It is declared in `.unattended.conf` at the date the unit lands,
  shipped blank in `tools/unattended/.unattended.conf.example`, given a row in the protocol's §8
  table, and added to the driver's contiguous key-initialiser block. Observed by AC6.
- **S6** — `read_audit_ask_record` keeps reading `## The prompt` and nothing else, so a spec-audit
  ask that appears only in `## The brief` or `## Drawn from the session` opts nothing in. Observed by
  AC7.

## 3. Non-goals (OUT)

- Detecting that a brief relied on the session without quoting it. That is the run's honesty, and no
  machine sees a conversation; the check's header says so.
- A second confirmation after an edit. The prompt path has one owner turn, and the record carries the
  edit verbatim.
- Grading the brief's content. The check is structural: a hollow but non-empty sub-section passes.
- Each item's disposition and its grading at close. That is `TOOL-aQuotedBrief-3`.
- Retrofitting landed prompt records. The cutoff grades by README `opened:` date.

### Edges

- **hands-off** `TOOL-aQuotedBrief-3` — the numbered `### Items` sub-section and the cutoff key,
  which that unit extends with a disposition per item and grades at close.

## 4. Design

### Evidence

Read at `fa68a767` on 2026-10-09.

- The prompt path writes the record at step 3 and states that "the prompt goes to a RECORD, never
  into the README", under `builds/<slug>/prompts/` with a `**Serves:**` line
  (`memory/guides/UNATTENDED-VERBS.md`, section `Start a run from a PROMPT`).
- `read_audit_ask_record` (`tools/unattended/unattended.sh:3066`) is the only driver reader of a
  prompt record. It anchors on a line that is exactly `## The prompt` and reads the `> ` lines up to
  the next `## ` heading, so new `##` sections after it do not change what it reads.
- `TOOL-aEvidencedLens-22` admits a prompt-mode `spec-audit:` when the record at BASE quotes the owner
  asking. The brief is run-authored, which is why S6 keeps that reader off it.
- `verb_preflight` (`unattended.sh:6371`) reads the authorization at `:6540-6543`, runs
  `check_waiver_scope` at `:6569` as the first consumer of `AUTH_MODE`, and gates the write at
  `:6595`. `AUTH_MODE` is empty when `trusted_base` refused, so the new check skips on empty, as
  `check_waiver_scope` does.
- A new conf key is joined by leg check 22 (`tools/unattended/check-unattended.sh:3083`): the §8 key
  column of the protocol must match the `KEY=` lines of the example conf in both directions, and the
  driver's initialiser block at `unattended.sh:493-499` is asserted by an arm of
  `unattended.test.sh` for every example key the driver reads.
- New fail sites need a positive assertion of their literal text in `unattended.test.sh`, read by
  `tools/memory-tree/check-arms.py`, so each message puts its interpolations last.

### The record

```markdown
## The prompt

> <the owner's bytes, verbatim>

## The brief

### Goal
<the build, in one or two sentences, readable with no conversation>

### Items
1. <one thing the owner asked for>
2. <...>

### Acceptance
<how the run will know each item is done>

### Gates
<the gate legs the run keeps green>

### Non-goals
<what the run must not build>

## Drawn from the session

> <a passage the brief relied on, verbatim>
— owner, <turn or time>

## Owner confirmation

Asked: <the question, verbatim>
Answer: <the owner's answer, verbatim>
```

`## Drawn from the session` is the single line `none` when the brief relied on nothing outside the
prompt. Each quote names its speaker, `owner` or `agent`, because a brief may rest on the agent's own
earlier proposal ("spec it" points at one). `## Owner confirmation` is then the single line
`not asked — the brief draws on nothing outside the prompt`.

### The structural rule

A record carrying `## The prompt` passes when all of these hold:

1. `## The brief` exists and holds the five `###` sub-heads above, in that order, each non-empty.
2. `### Items` holds at least one line opening with a number and a period.
3. `## Drawn from the session` exists and is non-empty.
4. `## Owner confirmation` exists and is non-empty.
5. When `## Drawn from the session` is anything but `none`, `## Owner confirmation` carries an
   `Asked:` line and an `Answer:` line, each with text after the colon.

A record failing any of them is named with the first rule it fails. Records without `## The prompt`,
such as `--brief` records under the same folder, are not graded.

### Inventory

| Identifier | Kind | Cell |
|---|---|---|
| `check_prompt_brief` | function | `sh.function`; `python tools/lexicon/lexicon.py --suggest check_prompt_brief --as sh.function` answered OK |
| `PROMPT_BRIEF_CUTOFF` | conf key | none: conf keys carry no naming cell |

### Files touched (estimate)

`tools/unattended/unattended.sh` · `tools/unattended/unattended.test.sh` · `tools/unattended/VERBS.template.md` · `tools/unattended/SKILL.template.md` · `tools/unattended/PROTOCOL.template.md` · `tools/unattended/.unattended.conf.example` · `memory/guides/UNATTENDED-VERBS.md` · `memory/guides/UNATTENDED-PROTOCOL.md` · `.claude/skills/unattended/SKILL.md` · `.unattended.conf` · `memory/map/generated/symbols.json`

### Alternatives rejected

- **Writing the brief into the build README.** Its heading canon is closed and its slots carry byte
  ceilings, and the verbs file already routes the prompt to a record for those reasons.
- **Linking the session transcript instead of quoting it.** A transcript is machine-local and
  editable, and the authorization may not point at a file editable after the run starts.
- **Detecting context-dependent prompts by wording.** A pronoun list is a heuristic that misses
  "do the second one" and fires on prose that quotes "it"; the run states what it used instead.
- **Confirming every brief.** Owner ruling 2026-10-09: a self-contained prompt needs no question.

## 5. Production-readiness checklist

- security — no new write path. The check narrows what preflight admits; it grants nothing.
- perf / scale — one `git show` per prompt record at BASE, read once at preflight.
- error / empty / loading states — a prompt-mode build with no `## The prompt` record refuses
  instead of passing over an empty population.
- observability — the refusal names the record path and the first rule it fails; a blank cutoff is
  announced on stderr.
- risks — a run that relied on the session and quoted nothing still passes. S2 makes that a choice
  the run records, not a gap it falls into.
- testing — arms in `tools/unattended/unattended.test.sh` over the existing `readme`, `scope
  published` and `run --preflight` fixtures, run once at VERIFYING.
- migration — none: the cutoff grandfathers every landed README by its `opened:` date.
- user docs — the verbs file and the skill are the user docs for this path.

## 6. Acceptance criteria

- **AC1** — When `--preflight` runs over a prompt-mode README past the cutoff whose prompt record
  carries `## The prompt` and no `## The brief`, it refuses at the new check, naming the record and
  rule 1, and creates no `RUN.md`.
  Red when: the record is admitted, or a run-state file is written before the refusal.
- **AC2** — When `grep -n "Drawn from the session" memory/guides/UNATTENDED-VERBS.md` runs, the
  prompt path's step 2 states the confirmation is mandatory when that section holds a quote, and
  step 3 lists the three sections in order.
  Red when: the render still says to ask only for gaps, or lists the sections in another order.
- **AC3** — When the record quotes a session passage and `## Owner confirmation` reads
  `not asked — the brief draws on nothing outside the prompt`, `--preflight` refuses naming rule 5.
  Red when: a session-derived brief passes without an `Asked:` and an `Answer:` line.
- **AC4** — When the record conforms, with `## Drawn from the session` reading `none`,
  `--preflight` prints `preflight OK`.
  Red when: a self-contained brief is refused for having no confirmation.
- **AC5** — When the prompt-mode build carries no record with `## The prompt`, `--preflight` refuses
  naming the empty population.
  Red when: an absent record passes as nothing to grade.
- **AC6** — When `PROMPT_BRIEF_CUTOFF` is blank, `--preflight` over AC1's fixture prints
  `preflight OK` and announces the key is off; when the README's `opened:` precedes a declared
  cutoff, it admits the record without the announcement.
  Red when: a blank key refuses, or a grandfathered README is graded.
- **AC7** — When a prompt-mode README declares `spec-audit:` and its record carries the opt-in phrase
  only under `## Drawn from the session`, check 89 refuses as it does today.
  Red when: a run-authored section opts the build into the audit.

## 7. Gates

`unattended kit gate` · `unattended skill wiring` · `unattended protocol size` · `unattended skill size` · `harness arms (fail branches armed or pinned)` · `lexicon naming predicates` · `codebase-map coverage + freshness` · `spec tokens (a spec's own names resolve)` · `check-wiring self-test` · `recall floor` · `recall floor arms`

New arm: tools/unattended/unattended.test.sh · covers AC1 AC3 AC4 AC5 AC6 AC7 · the HEAD driver, which admits any prompt record · none

## 8. Open questions

- **F1 — Does the confirmation fire for every prompt-mode brief, or only a session-derived one?**
  Every brief is simpler; only session-derived spares a cold, self-contained prompt a question.
  RESOLVED (owner, 2026-10-09): only a brief whose `## Drawn from the session` holds a quote.
- **F2 — Should an owner edit at the confirmation get a second confirmation?**
  Recommendation: no. The prompt path has one owner turn by design, the answer is recorded verbatim,
  and the owner is present to interrupt before the push.
  RESOLVED (owner, 2026-10-09): no second confirmation.

## 9. Revision log

- rev-1 · 2026-10-09 · initial draft.
- rev-2 · 2026-10-09 · §8 · owner resolved F2: an edit at the confirmation is folded and recorded,
  with no second confirmation.

## 10. Reuse audit

`reuse_lookup.py "record a self-contained brief of an unattended prompt-mode run, quoting session
context, and refuse unrelated commits on the run branch"` returned no seam for a prompt record: its
ranked symbols are run-log and commit readers. The extended seam is `read_audit_ask_record` in
`tools/unattended/unattended.sh`, the one driver reader of the record, whose `## The prompt` anchor
this unit keeps. The record's own convention, a verbatim section plus orientation notes, is reused
from `memory/builds/aGroundedOrientation/prompts/`.

Recall terms used: `prompt record verbatim authorized-by prompt published anchor branch tip
self-authorization orientation AskUserQuestion owner turn build folder roster` — which surfaced
`TOOL-aPromptedMandate-5`, `TOOL-aNamedGesture-1`, `TOOL-dNarrowedAnchor-1` and
`TOOL-aEvidencedLens-22`.
