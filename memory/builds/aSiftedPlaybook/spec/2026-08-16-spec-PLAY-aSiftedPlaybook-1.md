# PLAY-aSiftedPlaybook-1 — the template's claims reconverge with the kits they describe

**Status:** SPECCED · rev-5 · 2026-08-16 · node a · Tier-2 · base 91ef1b05 · streams playbook · ratified 2026-08-16

## 1. Goal

Eight statements in `parallel-coding-governance.template.md` describe the enforcement machinery
inaccurately. Two of them make the template prescribe behaviour the machinery actually refuses, so
an agent following the ruleset verbatim is denied by this repo's own hook. Correct all eight against
source, so the operating ruleset and the code that enforces it agree.

## 2. Scope (IN)

Every defect below was reproduced against source at BASE `91ef1b05`. D1–D5 come from the
2026-08-16 audit; D6 and D7 were found while writing this spec.

- **S1 (D6) — the lens-array bound stops prescribing a denied script.** Template `:150` says "an
  array LITERAL of ≤6 elements (the lens fan) passes unmarked". The enforced bound is
  `const MAX_LENSES = 5` at `tools/hooks/agent-cap.js:119`. A 6-element lens array is DENIED.
  `memory/guides/REVIEW-PROTOCOL.md:145` records why: 6 was never a decision, it was a
  trailing-comma miscount that made every prettier-formatted 5-lens array measure 6, and the owner
  ratified 5 once the miscount was found. `agent-cap.js:231` carries the same history in a comment.
  Correct ≤6 to ≤5. **This is the highest-severity item in the unit** — it is the only one that
  makes a compliant reader's script fail.
- **S2 (D1) — the hook matcher value is the one that works.** Template `:150` says the hook has
  "(matcher `Workflow`)". The wired value is `"matcher": "Workflow|Agent"`
  (`.claude/settings.json:5`). `REVIEW-PROTOCOL.md:58-60` states that `check-wiring.sh` asserts that
  VALUE rather than the filename, "because a group left at `Workflow` alone still contains the
  string `agent-cap.js` and used to report the tree correctly wired". An adopter wiring per the
  template's parenthetical gets a hook blind to the entire `Agent` modality.
- **S3 (D2) — the two undescribed hook rules get one clause each.** `agent-cap.js` carries four
  rules; the template describes two. Missing: **RULE 3** (`:346`) — the hook RESOLVES the bound
  wherever it is written, at the call site, in the helper's default parameter, and in a
  `gov:bounded-fanout` slice width, denying any `K` it cannot resolve to an integer ≤5; and
  **RULE 4** (`:549`) — a direct `Agent` spawn carries no script, so it is COUNTED at runtime, five
  per user prompt, via atomic slot claims. RULE 4 is the only enforcement that reaches a fan-out
  made outside a `Workflow` script, which is what §0's "never more than 5 agents" actually depends
  on.
- **S4 (D3) — the hygiene check count stops being a hardcoded ratchet.** Template `:107` says "a
  **19-check** hygiene gate". The true count is 20. **The authority is not the engine**: grepping
  `check-memory-hygiene.sh` for its own `fail` numbers returns only 1-12, because 13-16 delegate to
  `corpus_ids.py`, 17-19 to `gotchas.py` and 20 to `row_grammar.py` (`:713`). The count is
  single-sourced by the gate-leg name in `tools/gate-legs.json:3` and the kit README's table row at
  `tools/memory-tree/README.md:18`. **Delete the number rather than incrementing it** — see §4
  Alternatives rejected. That a correct count cannot be derived from the engine it describes is
  itself the argument for deleting it.
- **S8 (D8) — the enforcement-reach sentence stops describing the pre-1.3 hook.** Template `:157`
  says the cap "is enforced at the `Workflow` tool-call (where a main-loop `PreToolUse` fires),
  never inside the script where no hook reaches". Since `agent-cap` 1.3 it is enforced at the
  `Agent` tool call too, which is RULE 4's whole point.
  `memory/guides/REVIEW-PROTOCOL.md:62-70` is careful about this distinction, noting the old wording
  "used to read as" a blanket claim that runtime counting is impossible. Same staleness as S2, one
  line below it, and it must not be fixed by half.
- **S5 (D4) — the landing rule names the artifact the protocol defines.** Template `:51` says "a
  committed build plan". `memory/guides/UNATTENDED-PROTOCOL.md` says "build folder" five times and
  "build plan" zero; `AGENTS.md:182` and `parallel-coding-governance.domain-rules.md:25` also say
  folder. `parallel-coding-governance.customize.md:61` quotes the template's wording and moves with
  it.
- **S6 (D5) — the landing cross-reference stops pointing at itself.** Template `:51` cites
  "(companion §1, §8)" for the landing rule, but `:159` now reads "landing is §1's rule, not
  restated here". v2.7 turned §8 into a pointer at §1 and left §1's citation of §8 in place. Drop
  the `, §8`.
- **S7 (D7) — §0's summary of the cap covers both halves.** Template `:24` says "**Never run more
  than 5 agents concurrently**". Since `agent-cap` 1.3 the hook also enforces a TOTAL of 5 per
  verify stage and 5 direct spawns per prompt, and `REVIEW-PROTOCOL.md:12-13` states plainly that
  "concurrency is not a budget". §0 is a TL;DR and legitimately compresses, but it currently names
  the weaker of the two rules as if it were the rule. **Beyond the audit's eleven** — included
  because it is the same claim as S3 one section earlier, and excluded from the unit's blocker set.

## 3. Non-goals (OUT)

- **Changing any rule.** Every item restates what the code already enforces. If a correction would
  change what an agent is permitted to do, it is out of scope and becomes a fork in §8.
- **The `tools/workflows/tier2-review.js` path and the "install per WIRE §5" reference.** Both were
  suspected stale in the audit and both were REFUTED: the harness install genuinely sits inside
  WIRE §5 at lines 465-475, and `tools/<kit>/` is the declared install prefix. No edit.
- **`WIRE-INTO-PROJECT.md:463`, which calls agent-cap "the review protocol's TWO rules".** Same
  defect class, different file, outside the playbook trio this build scopes. Recorded as a follow-up
  row rather than fixed here.
- **The two other carriers of the stale "19-check"** — `tools/memory-tree/README.md:6` and root
  `README.md:33`. Both verified stale against the true 20. Same number, different products;
  follow-up row for the kit README. Root `README.md` is the adopter-facing front door and
  `TOOL-aSiftedPlaybook-1` S4 is separately editing it at `:12` in this same build, so **that unit
  is the cheaper home for `:33`** — recorded here as the cut-line rather than left in a revision
  log, which is nowhere a builder reads.
- **Making these claims machine-checked.** `TOOL-aSiftedPlaybook-3`.

## 4. Design

### Inventory

| Item | Template says | Source says | Source of truth |
|---|---|---|---|
| S1 lens array bound | `≤6` | `5` | `tools/hooks/agent-cap.js:119` |
| S2 hook matcher | `Workflow` | `Workflow\|Agent` | `.claude/settings.json:5` |
| S3 hook rules | 2 described | 4 implemented | `agent-cap.js:90,346,549` |
| S4 hygiene checks | `19` | `20` | `tools/gate-legs.json:3` · `tools/memory-tree/README.md:18` — **not** the engine, per §2 S4 |
| S5 landing artifact | "build plan" | "build folder" | `UNATTENDED-PROTOCOL.md` |
| S6 landing xref | `(companion §1, §8)` | §8 points back at §1 | template `:159` |
| S7 §0 cap summary | concurrency only | concurrency AND total | `REVIEW-PROTOCOL.md:12-13` |
| S8 enforcement reach | `Workflow` tool-call only | `Workflow` AND `Agent` tool-calls | `agent-cap.js:549` · `REVIEW-PROTOCOL.md:62-70` |

### Migration

None. No adopter data, no generated artifact, no config key changes shape. An adopter re-pulls per
`customize.md`'s §-body diff procedure.

### Files touched (estimate)

| File | Items |
|---|---|
| `parallel-coding-governance.template.md` | S1, S2, S3 at `:150`; S8 at `:157`; S4 at `:107`; S5, S6 at `:51`; S7 at `:24` |
| `parallel-coding-governance.customize.md` | S5 only, at `:61`, which quotes the template's clause |
| `memory/guides/SESSION-KICKOFF.md` | `last-audit` re-stamp — the template is a watched pathspec, so §7's re-stamp is a file this unit touches, not a side effect |

### Rollout

**Not independent, and the earlier draft of this paragraph was wrong twice over.**

Ordering: this unit is FIRST in the template lane, before `PLAY-aSiftedPlaybook-2` and
`PLAY-aSiftedPlaybook-3`. Its anchors are BASE line numbers (`:24`, `:51`, `:107`, `:150`, `:157`),
and PLAY-3 inserts ~2 KB into §5, §6 and §7 — above and inside every one of them, including `:107`,
the very bullet PLAY-3 adds a sibling to. It also shares template `:51` with PLAY-2 (that line
carries both "a committed build plan" and two branch senses) and shares `customize.md` with PLAY-3
and PLAY-4.

Byte cost: **measure it by simulation before building**, and record the number here. S3 is not the
only adder — S7 adds to §0, S8 rewrites `:157`, S2 adds 6 bytes — against roughly 17 removed by S4
and S6. The earlier claim that the cost was "well under the 86 bytes available at BASE" was asserted
rather than measured, which is the one thing this unit is not allowed to do. If the measured cost
exceeds 86, the unit depends on `TOOL-aSiftedPlaybook-1` and must say so.

### Alternatives rejected

- **S4: increment 19 → 20 rather than delete the number.** Rejected. The count ratchets whenever the
  kit gains a check, and nothing in the repo can detect the template disagreeing with it. `AGENTS.md`
  already learned this for the memory-tree kit version, recording that "a version written in prose
  rots between bumps, and this one rotted twice in a day", and stopped spelling it. The count's only
  reader is a human sizing up the kit, and the kit README states it authoritatively one hop away.
- **S3: describe all four rules in full.** Rejected: the full predicate is ~2 KB and already lives in
  `REVIEW-PROTOCOL.md`, which the template cites. One clause each is enough for a reader to know the
  rule exists and where it binds; the template's job is to route, not to restate.
- **S7: leave §0 alone as an acceptable compression.** Rejected on narrow grounds. Compression that
  drops a qualifier is fine; compression that names the weaker of two rules teaches the wrong bound.
  The fix is three words.
- **Bundling these into one "template accuracy" commit with `PLAY-aSiftedPlaybook-3`.** Rejected per
  M2: that unit ADDS kit coverage while this one CORRECTS existing claims, and a closing diff could
  not attribute a finding to the right half.

## 5. Production-readiness checklist

- security — N/A. No write path or surface. S2 has a security-adjacent flavour (a blind hook is an
  unenforced cap) but the fix is a documentation correction, not a control.
- perf / scale — N/A.
- a11y — N/A.
- i18n — N/A.
- error / empty / loading states — N/A.
- observability — N/A.
- risks — the real risk is a **wrong correction**: this unit's whole value is that the new numbers
  match source, so every replacement value is re-derived from the named file at build time rather
  than copied from this spec. AC1 states that obligation as an acceptance item.
- testing + left-shift gates — S1 and S2 are left-shiftable and should be:
  `tools/workflows/check-verifier-fanout.sh` already feeds scripts to the hook, and a leg asserting
  the template's stated bound equals `MAX_LENSES` closes S1's class permanently. Scoped to
  `TOOL-aSiftedPlaybook-3` rather than built here, because it is a gate and M2 makes a gate its own
  unit. **Until it lands, S1 and S2 are documented checks and will drift again.** Stated rather
  than implied.
- migration / rollback — N/A; `git revert`.
- user docs — these files ARE the docs.

## 6. Acceptance criteria

- **AC1** — When each corrected value is re-derived from its source file at build time with a
  single `grep`, it equals the value written into `parallel-coding-governance.template.md`. The derivations are the §4 Inventory table's third column;
  each is a single grep and none may be taken from this spec. **S4 is exempt** — its fix is a
  DELETION, so there is no value to re-derive; AC5 is its observation.
- **AC1b** — When template `:157` is read, it names both the `Workflow` and the `Agent` tool-call as
  points where the cap is enforced, and no longer says the cap is never enforced outside a script.
  S8 needs its own observation because AC2 exercises the lens bound and nothing else reads `:157`.
- **AC2** — Modelled on the `js()` helper at `tools/hooks/agent-cap.test.sh:27-35`, which builds a
  PreToolUse JSON payload and pipes it to the hook on fd 0. A fixture that **actually fans out over**
  the lens array — `boundedParallel(LENSES.map(d => () => agent(d)), 5)` — exits **0** with a
  5-element literal and **2** with a 6-element one.

  Three things this phrasing exists to avoid, all reproduced: piping raw script text passes the
  allow arm for the wrong reason, because the hook exits 0 on unparseable stdin by design; a script
  that merely DECLARES the array exits 0 at both 5 and 6, since the bound is only read at a fan-out;
  and "DENIED" is unanchored against the hook's 0/2 exit contract.
- **AC3** — When `grep -c 'build plan' parallel-coding-governance.template.md
  parallel-coding-governance.customize.md` runs, it returns 0 for both.
- **AC4** — When template `:51` is read, it cites companion §1 and not §8; when `:159` is read, it
  still points at §1. The pointer is one-directional.
- **AC5** — When `grep -oE '[0-9]+-check' parallel-coding-governance.template.md` runs, it returns
  nothing.
- **AC6** — When `bash tools/check-template-size.sh` runs, it exits 0 and reports the measured byte
  count, read FROM the gate.
- **AC7** — When `bash tools/run-gates.sh` runs at the integration boundary, every leg is green.

## 7. Gates

- `bash tools/check-template-size.sh` — the template is edited; re-measure, never assume.
- `bash tools/workflows/check-verifier-fanout.sh` and `bash tools/hooks/agent-cap.test.sh` — S1 and
  S2 make claims about the hook; these are the legs that exercise it.
- `bash tools/memory-tree/check-memory-hygiene.sh`.
- `python tools/memory-tree/gotchas.py --for-diff <base>..<head>` — after the commit, per M6.
- `bash skills/session-kickoff/manifest-check.sh` — `parallel-coding-governance.template.md` IS in
  the manifest's `watch:` list, so this unit re-stamps `last-audit` with a delta line.
- `python tools/drift-audit/drift_report.py --check` — the template is in `PRODUCT_GLOBS`. This unit must not
  cite its own non-terminal spec id from the template as provenance; the signal sits at pin 2,
  tolerance 0. Note the tension with template §6's "non-obvious rules carry provenance inline" —
  provenance may only be added once this spec is CLOSED.
- No new gate. See §5 for the left-shift that is owed and where it lives.

## 8. Open questions

none — the fork below is RESOLVED (owner, 2026-08-16).

- **F1 — does S3's RULE 4 clause belong in §8, or in §0?**
  **RESOLVED (owner, 2026-08-16): §0.** RULE 4 binds any fan-out, not only a review, so it goes
  where every session reads it. S7 carries the clause; §8 keeps RULE 3 and the mechanism detail, and
  does not restate RULE 4. The original framing:

  RULE 4 governs direct `Agent` spawns,
  which are not a review-protocol concern at all; a session fanning out for any reason meets it.
  §8 is the review section, so a reader doing non-review work may never load it.
  **Recommendation: state it in §8 with §0's S7 clause carrying the pointer.** §0 already names the
  cap and is always read; duplicating the mechanism in both would violate the single-statement rule
  the template applies elsewhere. Owner's call, because it is a routing decision about the ruleset's
  shape rather than a correctness fix.

## 9. Revision log

- rev-1 · 2026-08-16 · initial draft. D1–D5 carried from the 2026-08-16 audit and re-verified
  against source; D6 (the ≤6 lens bound) and D7 (§0's cap summary) found while writing §2 and
  reproduced before inclusion.
- rev-5 · 2026-08-16 · folded round-2 low L4. Root `README.md:33` carries the same stale "19-check"
  and had been declared out of scope only in a revision log — `memory/TEMPLATE-SPEC.md` makes §3 the
  cut-line, and a carrier cut nowhere a builder reads is not cut. Named in §3, and routed to
  `TOOL-aSiftedPlaybook-1` S4, which already edits that file.
- rev-4 · 2026-08-16 · owner resolved F1 (RULE 4's clause goes in §0), and the round-2 audit
  `wf_98677a7a-009` closed three findings. AC2 was **not runnable as written** — reproduced three
  ways: the hook exits 0 on unparseable stdin so piping script text passes the allow arm for the
  wrong reason, a script that merely declares the array exits 0 at both 5 and 6, and "DENIED" was
  unanchored against the hook's 0/2 contract. It now names the payload, the fixture and the exit
  codes. §4 Rollout's independence claim was false in two directions and is replaced by the real
  template-lane ordering and an instruction to MEASURE the byte cost rather than assert it. §4's S4
  row pointed at the engine that §2 S4 explicitly disqualifies as the authority for the count.
- rev-3 · 2026-08-16 · folded the spec audit `wf_4ed62ebb-cef`. S8 was in §2 but in nothing else:
  it had no §4 Inventory row, no source of truth, no Files-touched entry and no acceptance
  criterion, so a builder working the ACs would have shipped seven of eight fixes and passed.
  §1 still said "six statements" against §2's eight. Added the `.claude/SESSION-KICKOFF.md`
  re-stamp to Files touched, which §7 already mandated. Corrected the `drift_report.py` gate
  spelling to `--check`, without which it reports and cannot fail.
- rev-2 · 2026-08-16 · folded the `template-fixes` lens of discovery `wf_4e13d9e7-550`. Added S8
  (D8): template `:157` still says the cap is enforced at the `Workflow` tool-call "never inside the
  script", which is the same pre-`agent-cap`-1.3 staleness as S2 one line below it. Corrected S4's
  authority for the check count — it is NOT derivable from `check-memory-hygiene.sh`, whose own
  `fail` numbers stop at 12, but from the gate-leg name and the kit README table. Recorded that
  `tools/memory-tree/README.md:6` and root `README.md:33` carry the same stale 19 and are
  follow-ups, not scope.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "governance playbook template companions"` ranks
`agent-cap.topLevelArgs` first via the agent-cap affordance seam, which is the correct hit: S1, S2,
S3 and AC2 all wire through `tools/hooks/agent-cap.js` and its dossier
`memory/map/features/agent-cap.md`. **The seam this unit reads is `agent-cap.js`'s own constants**
(`MAX_LENSES`, the matcher assertion in `check-wiring.sh`), and the unit extends nothing — it
copies values OUT of that seam into prose, which is exactly the hand-kept-second-copy shape
domain-rules §10 warns about and is why §5 owes a left-shift.

Recall terms used, recorded per M5: `playbook template companion customize domain-rules agnostic
adopter stale externalize byte gate section stub kit wiring`. The binding prior record is
`PLAY-aCandidStub-1`, whose §2 S2 fixed this exact line for this exact reason — "§8 stops
prescribing a denied script", because the template named only one marker and a script written to it
"exits 2 under `tools/hooks/agent-cap.js`". S1 is that defect returning on the same line with a
different constant, which is the strongest single piece of evidence for `TOOL-aSiftedPlaybook-3`.
