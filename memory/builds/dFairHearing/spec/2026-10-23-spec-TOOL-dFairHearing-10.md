# TOOL-dFairHearing-10 — the review records brought back in line with the code at their sources, each live copy re-rendered

**Status:** OPEN · rev-1 · 2026-10-23 · node d · Tier-2 · base 3708a705 · streams tooling · order 12 · advances TOOL-dFairHearing-19

**Carries:** cl-dClosedLoop-0077@58d0099e whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-prompt-TOOL-dFairHearing-1-spec-brief.md](../prompts/2026-10-23-prompt-TOOL-dFairHearing-1-spec-brief.md) | research | TOOL-dFairHearing-1 TOOL-dFairHearing-2 TOOL-dFairHearing-3 TOOL-dFairHearing-4 TOOL-dFairHearing-5 TOOL-dFairHearing-6 TOOL-dFairHearing-7 TOOL-dFairHearing-8 TOOL-dFairHearing-9 TOOL-dFairHearing-11 TOOL-dFairHearing-12 TOOL-dFairHearing-13 TOOL-dFairHearing-14 TOOL-dFairHearing-15 TOOL-dFairHearing-16 TOOL-dFairHearing-17 TOOL-dFairHearing-18 |

<!-- /gen:spec-records -->

## 1. Goal

Review records contradict the code (gap-review-09): `memory/guides/REVIEW-PROTOCOL.md` lists retired
lenses, allows three to six and calls skeptics default-refute; agent-cap's lens comment says
tier2-review has four lenses; the synthesizer's role says it is handed confirmed findings only. This
unit fixes each at its source, `tools/workflows/REVIEW-PROTOCOL.template.md`,
`tools/workflows/tier2-review.template.js` and `tools/roles/agents/gov-synthesizer.agent.md` with
agent-cap's comment, against the code as this build's harness units leave it, and re-renders every
live copy.

## 2. Scope (IN)

- **S1** — The protocol's lens list. The Tier-2 pattern's dimension list
  (`tools/workflows/REVIEW-PROTOCOL.template.md:192`) names no lens. It points at the lens catalogue
  TOOL-dFairHearing-13 lands, `tools/workflows/lenses.toml`, and its presets, so a lens added as a
  catalogue row leaves the protocol true. Observed by AC1.
- **S2** — The lens count. The default configuration (:199-201) and the lens allowance paragraph
  (:222-227) say a run fills five lens slots on either kind, the count the verifier fan-out gate
  holds as its slot count, and that an opt-in lens swaps a slot rather than adding one; neither cites
  `MAX_LENSES` in the hook unless the hook still holds it at dispatch. No sentence states the count as
  a bound word beside a digit and a lens noun. Observed by AC2.
- **S3** — The skeptic default. "Default-refute" (:199) gives way to the default the harness applies
  (`tools/workflows/tier2-review.template.js:1403-1405`): a finding a skeptic cannot establish is
  refuted when its finder graded it medium or low, and answered uncertain when blocker or high.
  Observed by AC3.
- **S4** — Where each review rule is enforced. The protocol's enforcement section (:36-117) and its
  predicate section (:118-157) name where TOOL-dFairHearing-16 left each rule: the verifier total and
  the loop markers in the merge bar's harness check over committed harnesses, the ref-keyed join ban
  in `check-review-join.sh` alone, and the spec-audit opt-in in the review kit's pack on Workflow
  calls; and the "where enforcement does NOT reach" list says an inline script's verifier total is not
  checked at the tool call. Observed by AC4.
- **S5** — Agent-cap's lens comment. The comment beside the lens allowance constant
  (`tools/hooks/agent-cap.js:493-497` at base) says both kinds run five lenses, wherever the constant
  lives at dispatch: in the hook, or in the verifier fan-out gate if TOOL-dFairHearing-13 or
  TOOL-dFairHearing-16 moved it. Observed by AC5.
- **S6** — The harness template's own prose. Every comment or `meta` string in
  `tools/workflows/tier2-review.template.js` that states the lens count, the skeptic default, or the
  agent-cap hook as the enforcer of a rule TOOL-dFairHearing-16 moved, states the code as it stands;
  at base these are :769-773 and :838-842. `tools/workflows/tier2-review.js` is re-rendered. Observed
  by AC6.
- **S7** — The synthesizer's input line. `tools/roles/agents/gov-synthesizer.agent.md` (:15-16, and the
  sentence at :18 that adds no finding a skeptic did not confirm) says what the harness hands it at
  dispatch: the confirmed findings, the unverified ones as outstanding, the refuted claims and
  same-address twins to flag (TOOL-dFairHearing-7), a twinned run's two finder runs
  (TOOL-dFairHearing-11), and the leg names and class slugs for one disposition per confirmed finding
  (TOOL-dFairHearing-8). `.claude/agents/gov-synthesizer.md` is re-rendered by
  `tools/roles/render_agents.py --write`, and the role body stays inside its ceiling in
  `tools/roles/check_roles.py`. Observed by AC7.
- **S8** — Every live copy re-rendered and every edit inside the restatement gate's rule.
  `memory/guides/REVIEW-PROTOCOL.md` is re-rendered by `check-protocol-parity.test.sh --render`. No
  edit adds a carrier `tools/check-agent-cap-restatement.sh` flags, and both rows of
  `tools/agent-cap-restatement-waivers.txt` still match a live line. The review-harness, roles and,
  where S5 edits the hook, agent-cap versions each move once against base `3708a705` if no earlier
  unit of this build moved them. Observed by AC8 and AC9.

## 3. Non-goals (OUT)

- A record another unit's change made stale where that unit owns the sentence: the resume file's name
  (TOOL-dFairHearing-4), the review harness README's argument and return sections (each harness unit),
  and the hooks kit README (TOOL-dFairHearing-16).
- `gap-review-03`'s agent count: the register already carries the measured 11 or 12 (section 8 F3).
- New content in the protocol for behaviour no named record describes, such as presets' lens briefs:
  the catalogue holds them.
- The charter's `[bound]` line and its checked digit, which `check-playbook-parity.sh` binds to the
  hook's `MAX_VERIFIERS`, unchanged by this build.
- The records units ordered after this one change: TOOL-dFairHearing-17's round state and
  TOOL-dFairHearing-18's walk tables. Each edit here is a pointer, so those units leave it true unless
  they change what it points at (section 4); neither declares an edge to this unit at this writing.
- Building what S1, S2 and S7 point at. S1 and S2 read TOOL-dFairHearing-13's catalogue and slot
  count, and S7 names TOOL-dFairHearing-7's refuted claims and twins; both are ordered before this
  unit and declare no edge to it at this writing, so none is declared here.

### Edges

- **consumes-from** `TOOL-dFairHearing-16` — the moved rules' homes S4 names; without it S4 would describe homes the code does not have
- **consumes-from** `TOOL-dFairHearing-11` — the twinned run S7 names among the synthesis's inputs
- **consumes-from** `TOOL-dFairHearing-8` — the leg names and class slugs S7 names among the synthesis's inputs

## 4. Design

### Evidence

- `tools/workflows/REVIEW-PROTOCOL.template.md:192` lists security, correctness, data-integrity,
  dead-code and integration-seams; the harness's diff lenses are security, correctness, seams,
  verification and intent (`tools/workflows/tier2-review.template.js:774-800`) and its spec lenses
  five others (:810-836).
- :199 reads "3–6 primed finder lenses → batched default-refute skeptics", while the harness fills a
  five-element literal (:842) and its skeptic default depends on the finder's grade (:1403-1405).
- :222-227 says agent-cap holds the lens allowance as `MAX_LENSES`; the hook's comment at
  `tools/hooks/agent-cap.js:495` says "tier2-review has four".
- `tools/roles/agents/gov-synthesizer.agent.md:15-16` says it is handed "the findings the skeptics
  confirmed", while the synthesis prompt carries the unverified findings too
  (`tools/workflows/tier2-review.template.js:1736-1744`).
- The review system record lists these edit sites (`memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-review-system.md`, section `[stale]`).
- The restatement gate keys on a bound word beside a digit and a noun such as `lens`, `skeptic` or
  `agents` (`tools/check-agent-cap-restatement.sh:90-95`); its waiver rows key on the measured table's
  row and the charter's checked digit (`tools/agent-cap-restatement-waivers.txt:7-8`).
- `tools/roles/check_roles.py` holds the synthesizer body at a 3072-byte ceiling, and the role file is
  1699 bytes whole at base (measured 2026-10-23).

### How each edit is written

Every edit states a pointer or a behaviour, never an inventory typed beside its source (charter
`[one-fact]`): the lens list names the catalogue, the count names the gate that holds it, and the
synthesizer line names input kinds rather than counts. A unit ordered after this one then leaves these
records true unless it changes what they point at, the reason section 3 gives for declaring no edge to them.

### Files touched (estimate)

- `tools/workflows/REVIEW-PROTOCOL.template.md`
- `memory/guides/REVIEW-PROTOCOL.md` (its render, by `check-protocol-parity.test.sh --render`)
- `tools/workflows/tier2-review.template.js`
- `tools/workflows/tier2-review.js` (its render)
- `tools/hooks/agent-cap.js` (S5, only where the lens comment still lives there)
- `tools/workflows/check-verifier-fanout.js` (S5, only where the lens comment moved there)
- `tools/roles/agents/gov-synthesizer.agent.md`
- `.claude/agents/gov-synthesizer.md` (its render, by `render_agents.py --write`)
- `tools/roles/roles_lib.py` (the roles kit's version line only, if no earlier unit moved it)
- `tools/check-agent-cap-restatement.sh` (only where a header sentence states a rule's home the build
  moved; at the base read none does, section 8 F4)

### Alternatives rejected

- **Listing today's lens names in the protocol.** A typed list goes stale at the next catalogue row,
  which is gap-review-09's defect itself.
- **One pass over every record the build touched.** Each harness unit owns its own README sentences,
  and two units editing one sentence is the conflict the build order exists to avoid.

## 5. Production-readiness checklist

- security — no code path changes; the protocol is a binding governance carrier and its edit is named
  by this unit's clause (section 8 F5).
- perf / scale — N/A — records only.
- error / empty / loading states — N/A — no runtime behaviour.
- observability — N/A — no runtime behaviour.
- risks — a reader trusting a protocol sentence about where a rule is enforced; S4's grep criterion
  pins each home by name.
- testing — AC1 to AC9 as greps over the sources and their renders.
- migration — an adopter's update re-renders the protocol and the agent type; the parity leg and the
  roles render check red a stale copy.
- user docs — the protocol and the role file are themselves the documents; no page under `help/`
  states the lens list, the skeptic default or the synthesizer's inputs.

## 6. Acceptance criteria

- **AC1** — When `grep -n "data-integrity\|dead-code\|integration-seams" tools/workflows/REVIEW-PROTOCOL.template.md memory/guides/REVIEW-PROTOCOL.md`
  runs, it prints nothing, and `grep -n "lenses.toml" memory/guides/REVIEW-PROTOCOL.md` prints the
  pointer.
  Red when: a retired lens name survives in either copy, or the render lacks the pointer.
- **AC2** — When `grep -n "3–6\|3-6\|three to six" memory/guides/REVIEW-PROTOCOL.md` runs, it prints
  nothing, and the default-configuration paragraph names the slot count and the gate that holds it.
  Red when: the protocol still allows a range of lens counts.
- **AC3** — When `grep -n "default-refute" memory/guides/REVIEW-PROTOCOL.md tools/workflows/REVIEW-PROTOCOL.template.md`
  runs, it prints nothing, and the protocol states the medium-or-low and blocker-or-high defaults.
  Red when: the skeptic default is still described as refute.
- **AC4** — When `grep -n "check-verifier-fanout\|check-review-join\|spec-audit-optin" memory/guides/REVIEW-PROTOCOL.md`
  runs, it prints each of the three homes, and the where-enforcement-does-not-reach list names an
  inline script's verifier total.
  Red when: the protocol still names the hook as the enforcer of a moved rule.
- **AC5** — When `git grep -n "tier2-review has four" -- tools/` runs, it prints nothing, and the
  comment beside the lens allowance constant, wherever it lives, names five lenses on both kinds.
  Red when: the stale count survives at the constant's home.
- **AC6** — When `grep -n "agent-cap" tools/workflows/tier2-review.template.js` runs, every line it
  prints states a rule the hook still carries at dispatch, the raw-primitive ban or the bound it reads,
  and the same grep over `tools/workflows/tier2-review.js` prints the same count.
  Red when: a comment names the hook as the enforcer of the lens count or the verifier total, or the
  render lags its template.
- **AC7** — When `grep -n "confirmed" .claude/agents/gov-synthesizer.md` runs, the input sentence names
  the unverified findings, the refuted claims, a twinned run and the disposition inputs beside the
  confirmed ones, and `python -c "import pathlib; t=pathlib.Path( 'tools/roles/agents/gov-synthesizer.agent.md' ).read_text(encoding='utf-8').replace(chr(13),''); print(len(t.split('---',2)[2].encode()))"`
  prints a body size at or under 3072.
  Red when: the role still says it is handed confirmed findings only, or the render lags the source.
  figure: 3072 is pinned, read from `tools/roles/check_roles.py` at base `3708a705`.
- **AC8** — When the bound pattern of `tools/check-agent-cap-restatement.sh` is applied with
  `grep -nE` to the lines this pass changed in `tools/workflows/REVIEW-PROTOCOL.template.md`, it matches
  none, and `grep -c "≤5 batched skeptics (required)" memory/guides/REVIEW-PROTOCOL.md` prints 1.
  Red when: an edit restates the cap as a digit, or the measured table row the waiver keys on is gone.
- **AC9** — When `grep -m1 "version: " tools/workflows/tier2-review.template.js` and
  `grep -m1 "KIT_ROLES_VERSION = " tools/roles/roles_lib.py` run, each prints a version other than the
  same grep over `git show 3708a705:<file>` does.
  Red when: a kit's shipped bytes moved over the build with its version unmoved.
  figure: the base versions, review-harness `1.53` and roles `1.8`, are pinned, read at base
  `3708a705` on 2026-10-23.

## 7. Gates

`review-protocol parity (kit vs dogfood)` · `agent-cap restatement` · `roles catalogue` · `roles render selftest` · `roles render wiring` · `tier2-review self-test` · `verifier fan-out self-test` · `unattended-build self-test` · `review-join self-test` · `agent-cap self-test` · `scratch-guard self-test` · `hook destinations self-test` · `check-wiring self-test` · `lexicon naming predicates` · `recall floor` · `recall floor arms` · `kit version markers` · `kit epoch (shipped bytes move, the version moves)` · `memory hygiene`

No suite arm lands with this unit: every change is prose a render and the restatement gate already
grade, and AC1 to AC9 observe it.

## 8. Open questions

- **F1 — Does the protocol list the lens names or point at their source?** (a) Point at the catalogue.
  (b) List today's names. (b) is a second copy of the catalogue, the defect gap-review-09 names.
  Recommendation (a). Rung 1: v2's clause 13 makes the catalogue data in the review kit. RESOLVED
  (agent, 2026-10-23, delegated): (a). widens: none · relaxes: none
- **F2 — Which records does this unit bring in line?** (a) The ones the clause names, plus the
  protocol's enforcement and predicate sections TOOL-dFairHearing-16 makes stale. (b) Every record any
  unit of the build makes stale. (b) edits sentences each harness unit owns in its own README, two
  writers on one sentence. Recommendation (a). Rung 3. RESOLVED (agent, 2026-10-23, delegated): (a).
  widens: none · relaxes: none
- **FACT-QUESTION · F3 — Is `gap-review-03`'s agent count still stale?** Probe: read the register's
  row (`memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-gap-register.md:437`).
  Observation: it reads "11 or 12 agents (9 when this row was written)", the measured count the review
  system's `[stale]` section asked for. Liveness: a row still reading "about 9 agents" would have kept
  it in scope. RESOLVED (agent, 2026-10-23, delegated): already in line, nothing to edit. widens: none ·
  relaxes: none
- **FACT-QUESTION · F4 — Does the restatement gate's own header state a moved rule's home?** Probe:
  `grep -n "join\|spec-audit\|fixed-verifiers\|sequential\|arity\|lens" tools/check-agent-cap-restatement.sh`.
  Observation: its header names historical carriers and the hook as the owner of the number, which
  stays `MAX_VERIFIERS` in the hook after TOOL-dFairHearing-16; no sentence names the hook as the home
  of rule 0, 2 or 5. Liveness: a sentence sending a reader to the hook for one of those rules would
  have printed. RESOLVED (agent, 2026-10-23, delegated): no header edit is owed at the base read; the
  gate is in reach as the check every protocol edit passes. widens: none · relaxes: none
- **F5 — Does the grant cover editing the binding review protocol and the other sources?** The
  protocol, every path under `tools/` and `.claude/agents/gov-synthesizer.md` are governance carriers
  by `PLAY-dClosedLoop-10`'s list, and the clause names each source and its live copies. RESOLVED
  (agent, 2026-10-23, delegated): lifted by `PLAY-dClosedLoop-3`, rung 3. grants: PLAY-dClosedLoop-3
  the review protocol's lens list, lens count, skeptic default and the homes of the rules this build
  moved, agent-cap's lens comment, the harness template's prose and the synthesizer's input line, each
  live copy re-rendered · widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft.

## 10. Reuse audit

No existing seam fits beyond the sources themselves: each record is edited where it is authored, and
every live copy comes from the renderer that already owns it, `check-protocol-parity.test.sh --render`
for the protocol and the harness, `tools/roles/render_agents.py --write` for the agent type. `python
tools/codebase-map/reuse_lookup.py "bring a review protocol document back in line with the harness
code"` ranked only name-stem hits on "line" (`check_line`, `render_line`, `unfenced_lines`), none of
them a seam for prose, and did not surface the two renderers the source read found. The recall query
also returned TOOL-aDeclaredBound-6, the precedent for stale prose inside the harness itself, which
TOOL-dTieredTribunal-11 closed by deleting the disagreeing comment; S6 follows it.

Recall terms used: `python tools/memory-recall/query.py "which review records contradict the harness
code and must be brought back in line" --terms "REVIEW-PROTOCOL lens list default-refute skeptic
gov-synthesizer input line agent-cap four lenses stale gap-review-09"`
