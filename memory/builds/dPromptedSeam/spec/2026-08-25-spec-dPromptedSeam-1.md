**Serves:** spec TOOL-dPromptedSeam-1

# TOOL-dPromptedSeam-1 — a refused name carries a reuse prompt

**Status:** OPEN · rev-4 · 2026-08-25 · node d · Tier-1 · base 671e953d · streams tooling

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-25-review-TOOL-dPromptedSeam-1-2-spec-audit-round-1.md](../reviews/2026-08-25-review-TOOL-dPromptedSeam-1-2-spec-audit-round-1.md) | spec-audit | TOOL-dPromptedSeam-2 |
| [2026-08-25-review-TOOL-dPromptedSeam-1-2-spec-audit-round-2.md](../reviews/2026-08-25-review-TOOL-dPromptedSeam-1-2-spec-audit-round-2.md) | spec-audit | TOOL-dPromptedSeam-2 |
| [2026-08-25-review-TOOL-dPromptedSeam-1-spec-audit.md](../reviews/2026-08-25-review-TOOL-dPromptedSeam-1-spec-audit.md) | spec-audit | — |

<!-- /gen:spec-records -->

## 1. Goal

When the lexicon refuses a name, the author should also learn that the thing may not need writing.
rev-1 tried to deliver that by having `lexicon.py` call `codebase-map`; the spec audit refuted the
mechanism on three independent grounds. rev-2 delivers the same goal through the rendered Skill,
which is where both tools' agent-facing instructions already live and where no cross-kit call is
needed at all.

## 2. Scope (IN)

- **S1 — one rung on an existing ladder.** `tools/lexicon/SKILL.template.md` already carries a
  "When a name genuinely will not fit" section. It gains a step: when the refusal suggests the
  function may not need to exist, describe the BEHAVIOUR to `reuse_lookup.py` — a sentence, not the
  name you picked — and read what comes back before writing.
- **S2 — the instruction is phrased against the callee's own contract.** It must tell the reader to
  write a behavioural phrase, because `reuse-lookup.agent.md` says a picked name is the wrong input
  and rev-1 was refuted for supplying exactly that.
- **S3 — UNCONDITIONAL, and worded to survive a map-less adopter.** rev-3 made the rung conditional
  on `codebase-map` and claimed the renderer already had a mechanism for that. It does not:
  `render_skill()` is six literal `${out//{{KEY}}/…}` substitutions and holds no fence parser, while
  the `kit:`/`when:` dropper lives in `render_playbook.py`, which renders the CHARTER and never sees
  `SKILL.template.md`. Rather than build a fence pass for one rung, the step ships to everyone and
  names the tool as one an adopter may or may not have — which is true, costs nothing, and is what a
  reader needs either way.
- **S4 — the human-facing doc follows.** `tools/lexicon/LEXICON.md`'s delivery section gains the
  same step in prose, so the Skill and the doc do not disagree.

## 3. Non-goals (OUT)

- **No call from `lexicon.py` into `codebase-map`, in any form.** rev-1's subprocess is withdrawn.
  `.lexicon.conf` declares `tools/lexicon/* -> tools/codebase-map/*` forbidden and states
  self-containment as the reason; P3 grades imports and could not have seen an exec, which makes
  routing around it worse rather than better.
- **No auto-rename.** Unchanged from rev-1 and still the load-bearing OUT: the table's value is
  SCOPING, and rewriting the identifier silences the signal it exists to produce.
- **No object-token query.** Measured over 326 live offenders, a bare object surfaces a real seam
  16.6% of the time. The Skill asks for a behavioural sentence instead.
- **No new conf key, timeout, discovery logic or outcome taxonomy.** All four existed in rev-1 to
  serve a subprocess that no longer happens.
- **No new gate leg.** `lexicon wiring` already byte-compares the rendered Skill.

## 4. Design

**D1 — the integration point is the INSTRUCTION, not the code.** Both kits already ship agent-facing
instructions: `.claude/skills/lexicon/SKILL.md` and `tools/codebase-map/reuse-lookup.agent.md`. The
gap rev-1 tried to close with a subprocess is a gap between two documents that never mention each
other. Closing it there costs a few lines and no coupling.

**D2 — the query is a SENTENCE, and that is the whole reason this shape wins.** rev-1 automated a
trigger and paid for it with the wrong input. The Skill's reader knows what they are about to build
and can describe it, which is the input `reuse_lookup` documents wanting. Automating a bad query is
not better than prompting for a good one.

**D3 — NO CONDITION AT ALL, which is the shape the tree actually supports.** rev-3 asserted the
lexicon renderer could drop a block per adopted kit. Verified against the source: it cannot, and the
mechanism it named belongs to a different renderer with a different subject. The three ways out were
to build a fence pass (new machinery, a new placeholder, a new leftover check, and its own staged
failure), to add a build-time presence probe (`discovery logic`, which §3 forbids by name), or to
drop the condition. The third is taken. An adopter without the map reads one sentence naming a tool
they do not have, which is the ordinary cost of a kit that mentions its siblings, and it keeps §9's
Tier-1 claim true — no renderer code path moves.

**D4 — what rev-2 does NOT claim.** It does not fire automatically. An agent that never reads the
Skill never sees the step. That is a real cost and the audit named it; it is accepted because the
alternative was a mechanism refuted on cost, query shape and declared architecture at once.

## 5. Production-readiness checklist

- **security** — N/A. No new execution, no new input, no new file read at run time.
- **perf / scale** — N/A at run time. The rendered Skill grows by a few lines; `--suggest` is
  untouched and keeps the "NO CORPUS PASS" property its docstring records.
- **a11y** — N/A.
- **i18n** — N/A.
- **error / empty / loading states** — N/A. Nothing executes.
- **observability** — N/A.
- **risks** — the only one is that the step is ignored, which D4 states plainly. There is no failure
  mode, no state and no rollback surface: reverting is deleting the lines and re-rendering.
- **testing + left-shift gates** — the render is byte-compared by an existing unguarded leg. AC2
  makes its failing case observed rather than assumed.
- **migration / rollback** — none.
- **user docs** — S4.

## 6. Acceptance criteria

- **AC1** — When `bash tools/lexicon/adopt-lexicon.sh --render` runs, `.claude/skills/lexicon/SKILL.md`
  contains the literal token `reuse_lookup.py` exactly once, and the surrounding sentence contains
  the word `behaviour` — the property S2 exists to enforce, not merely that a step was added.
- **AC2** — When that token is deleted from `.claude/skills/lexicon/SKILL.md` by hand,
  `bash tools/lexicon/adopt-lexicon.sh --check` exits non-zero naming `DRIFTED`; restoring it by
  re-rendering returns it to zero. The failing case is OBSERVED, per §7's rule for a new check.
- **AC3** — When `grep -c 'codebase-map' .claude/skills/lexicon/SKILL.md` runs, the rung's sentence
  names the sibling kit as one the reader may not have, so the instruction is READABLE by a map-less
  adopter rather than silently wrong for them. rev-3's AC3 named `deploy.toml` and a target-taking
  renderer; `adopt-lexicon.sh` accepts only `--scaffold|--check|--render`, takes no target and never
  reads that file, so the criterion had no subject and its absent-kit branch could never run on any
  bar.
- **AC4** — When `python tools/lexicon/lexicon.py --suggest fetch_conf` runs after this unit, its
  output is byte-identical to the same command's output at base `671e953d`, proving the engine was
  not touched.
- **AC5** — When `grep -c 'reuse_lookup' tools/lexicon/LEXICON.md` runs, it returns at least 1, and
  the sentence it appears in names a behavioural phrase rather than an identifier.

## 7. Gates

Adds no leg. Rides `lexicon wiring` (`bash tools/lexicon/adopt-lexicon.sh --check`), which is
unguarded and runs on every bar, and `lexicon naming predicates`. The codebase-map legs are
untouched, and `LAYER_OFFENDER_PIN` stays `0` because nothing crosses the declared layer.

## 8. Open questions

- **Q1 — does the Skill step name `reuse_lookup.py` directly, or point at
  `reuse-lookup.agent.md`?** RESOLVED: name the script and let its own agent doc own the how. Two
  documents describing one invocation is the class this repo names, and the agent doc is the copy
  that stays current.
- **Q2 — should `--suggest`'s output mention the Skill step?** RESOLVED (agent, 2026-08-25,
  delegated): NO. Mentioning it fails AC4, which pins the engine's output byte-identical to base —
  so the option is discarded by M3's veto 1 before any preference is needed, and a veto is not a
  licence to take the vetoed option. It would also put a pointer to a document inside a command's
  output, which is the coupling D1 exists to avoid. Revisit only if the Skill step is MEASURED to go
  unread; that measurement does not exist and inventing one here would be a fork resolved by
  assertion.

## 9. Revision log

- rev-1 · 2026-08-25 · node d · OPEN. Proposed a subprocess from `lexicon.py` into
  `reuse_lookup.py` on the refusal path, keyed on `read_object()`.
- rev-4 · 2026-08-25 · node d · OPEN. Spec audit round 1 returned BLOCKED and four of its six
  blockers were this unit's, all tracing to one undecided question: whether the rung is conditional.
  It is not. S3, D3, AC3 and §10 each asserted a conditional-block mechanism in a renderer that has
  none — `render_skill()` is six literal substitutions, and the fence dropper belongs to
  `render_playbook.py`, which renders the charter. Dropping the condition retires all four rather
  than building a fence pass, a placeholder, a leftover check and a staged failure for one sentence.
- rev-3 · 2026-08-25 · node d · OPEN. §8 Q2 RESOLVED under the standing mandate: discarded by veto
  1 for failing AC4, not chosen on preference. §10 gains the recall terms M5 requires, which rev-2
  omitted — the probes were run for the set and their terms were not written down, which is the half
  M7 re-runs.
- rev-2 · 2026-08-25 · node d · OPEN, Tier-2 → Tier-1. **rev-1's MECHANISM is withdrawn; its GOAL is
  kept.** A three-lens spec audit refuted it on three independent grounds, each re-verified by hand
  before acceptance. First, the 1.85 s cost that D4 called "the binding constraint" does not
  reproduce — two lenses measured ~0.19 s and re-running the author's own command gives 0.197 s;
  the original was a single wall reading taken while a full bar and three subagents were running,
  which is the error `process-creation-is-the-suite-cost` warns about and the author had read.
  Second, `reuse-lookup.agent.md:14` says "Describe the behaviour, not a name you already picked",
  and rev-1's object query supplied precisely a picked name; measured over 326 live offenders it
  surfaces a real seam 16.6% of the time, against the "three for three" rev-1 claimed from three
  objects of the file its author was reading. Third, `.lexicon.conf` forbids this exact layer
  direction and P3 grades imports only, so the subprocess satisfied the gate while defeating the
  declaration. The audit also found four of eight acceptance criteria unfalsifiable, one of them
  repeating a defect the same author had fixed hours earlier in the same file. Tier drops to 1
  because rev-2 changes no code path.

## 10. Reuse audit

- `tools/lexicon/SKILL.template.md` — EXTENDED. The "When a name genuinely will not fit" ladder
  exists; this adds a rung rather than a section.
- `tools/codebase-map/reuse-lookup.agent.md` — POINTED AT, not restated. It already turns a
  shortlist into a decision, and duplicating that guidance in the lexicon's Skill would be two
  answers to one question.
- The renderer's conditional-block mechanism — NOT reused, because it is not in this renderer.
  rev-3 claimed it was. `render_skill()` (`tools/lexicon/adopt-lexicon.sh:95-123`) substitutes six
  placeholders and parses no fences; `remove_fenced`/`OPEN_RE` (`tools/playbook/render_playbook.py`)
  render the charter. Two renderers, one sentence, and the audit caught it.
- `read_object()` — NOT used by this unit. rev-1's use of it is withdrawn, and its own defects are
  `TOOL-dPromptedSeam-2` rather than this unit's business.

**Recall terms used**, recorded because composing them is the expensive half and M7 re-runs the
query: `lexicon subtokens port self-contained layers import ban codebase-map map_lib kit
independence adopter reuse seam`. The behaviour phrase for the map probe was *"reduce an identifier
to the concept it names, dropping the leading verb"*. What came back that MATTERS: `leading_verb`
(`tools/lexicon/subtokens.py`, fan-in 3, SEAM) is the only seam in this area, and
`TOOL-aRootedPrefix-1` records that `codebase-map` once hardcoded its `<root>/codebase-map/` install
convention — which is exactly the discovery problem rev-2 no longer has to solve, because it makes
no cross-kit call at all.
