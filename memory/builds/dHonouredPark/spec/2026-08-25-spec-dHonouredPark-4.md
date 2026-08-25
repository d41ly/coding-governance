# TOOL-dHonouredPark-4 — `--plan` takes its unit SET and its ORDER from the rendered region, so both verbs answer from one source

**Status:** SPECCED · rev-4 · 2026-08-25 · node d · Tier-2 · base 60ba1d60 · order 4 · streams tooling

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-25-review-TOOL-dHonouredPark-1-spec-audit-round1.md](../reviews/2026-08-25-review-TOOL-dHonouredPark-1-spec-audit-round1.md) | spec-audit | TOOL-dHonouredPark-1 TOOL-dHonouredPark-2 TOOL-dHonouredPark-3 |
| [2026-08-25-review-TOOL-dHonouredPark-1-spec-audit-round2.md](../reviews/2026-08-25-review-TOOL-dHonouredPark-1-spec-audit-round2.md) | spec-audit | TOOL-dHonouredPark-1 TOOL-dHonouredPark-2 TOOL-dHonouredPark-3 |

<!-- /gen:spec-records -->

## 1. Goal

Since the roster sorts by build order, `--status` and `--plan` volunteer different units as next.
`--status` reads the generated units region and names the first non-terminal row in build order;
`--plan` re-derives from tracked specs in `git ls-files` order — which is LEXICAL PATH order, not id
order as rev-1 claimed. `unattended.sh:1578` has no sort anywhere, and path order coincides with id
order only while dates and unpadded ordinals happen to agree; on a build with more than nine units it
gives 1, 10, 11, …, 2, 20.

Neither verb is wrong about STATUS, and that is what makes the disagreement expensive — two verbs
answering one question differently, with nothing to say which is authoritative. The owner ruled
`--plan` reads the rendered region.

## 2. Scope (IN)

- **S1** — `--plan`'s unit enumeration takes its SET and its ORDER from the `gen:build-units` region.
  This EXTENDS an existing read rather than adding one: `verb_plan` already opens that region at
  `unattended.sh:1572-1573` for its malformed-pair refusal. A row resolves to its unit **by ID, not by
  link** — `unit_rows` (`:1538-1541`) pattern-matches `^\| \[.*\]\(spec/` and never opens the target,
  and eleven arms plus `UNATTENDED-PROTOCOL.md:423` describe the output; resolving by link would break
  them, because the `readme()` fixture links to a bare `one.md` under its `spec/` dir while `mkspec`
  writes a dated filename.
- **S2** — `--plan` reports units in the region's own order, which is build order, so its "next" and
  `--status`'s "next" are the same unit **over the SPECCED set** by construction rather than by
  coincidence.
- **S3** — the MISSING join is UNCHANGED and still reads the authored `roster:units` pair. That
  question — which units are planned but unspecced — cannot be answered from a region rendered out of
  the specs that exist, and pointing it there was tried and reverted at `TOOL-aBoundedVerdict-11`.
- **S4** — the residual divergence S3 preserves is DOCUMENTED rather than claimed away. On a build
  whose specced units are all terminal AND whose roster names an unspecced id, `verb_plan` falls
  through to `next="$miss (MISSING - spec it first)"` (`:1614-1618`) while `verb_status` prints
  `(no non-terminal unit)` (`:2226-2227`). The verbs then name different things because they are
  answering different questions, and `--plan` is the one with the more complete answer. rev-1's
  "the same unit by construction" was false in that state; this unit scopes the claim and pins the
  exception with an arm instead of leaving it as an unverified sentence.
- **S5** — a REFUSAL when the region is ABSENT, naming the file and the marker, rather than a silent
  fallback to the old derivation. The MALFORMED case already refuses with `fail 42` at `:1572-1576`
  and is already armed at `unattended.test.sh:1601-1611`; `units_refusal` at `:1557` already spells the
  message. Only the truly-absent case falls through today, guarded away by the outer
  `grep -qF -- "$UNITS_OPEN"`. This unit changes that guard's condition — which rev-1 did not
  acknowledge, having treated the whole refusal as new code.
- **S6** — the two `NOT A UNIT` diagnostics are PRESERVED. `render_region` emits rows only from
  specs whose status header parsed, so the region cannot carry either. `verb_plan`'s spec walk reports
  them, and they are:
  1. **no status header** — the file has no `**Status:**` line at all. FIVE tracked specs produce this
     row today: `aDeployScout`, `aKitHardener`, `aLeanRework`, `aPortableWarden`, `aRatchetForge`.
  2. **heading id does not parse** — the `# ` heading's first token is not id-shaped. **ZERO tracked
     specs produce this row**, which the driver's own comment beside the branch already states.

  rev-2 described the second as "a spec whose heading and status header disagree". That is not what
  the branch tests and could not be: the status header carries no id, so there is nothing for a
  heading to disagree with. Round 2 parsed all 277 tracked specs with the driver's own two awk
  programs to establish both counts.

  Moving the enumeration onto the region would drop both signals, so `--plan` keeps a spec-file walk
  for this purpose alone. rev-1's "otherwise identical" is withdrawn.
- **S7** — a region row whose id has NO tracked spec is classified, rather than falling through. Today
  the set comes from `git ls-files`, so such a row cannot arise and the harness's empty-plan build
  reaches its refusal only for that reason; once S1 makes the region the SET, the row is representable
  and needs a name. It reports as a unit whose spec is missing — distinct from the authored pair's
  MISSING, which is about a PLANNED unit — and §4's "otherwise identical" is qualified accordingly.
- **S8** — this unit prices its own read-path charge and moves `READ_PATH_CEILING` by it, per owner
  ruling 2 and this build's rules slot. It charges `memory/guides/UNATTENDED-PROTOCOL.md`, a capped
  member, and its own `memory/DECISIONS.md` row. rev-2 claimed both were "priced" and recorded no
  measurement anywhere in the file — the round-1 finding WAS the missing measurement, and the fold
  wrote the word instead of doing the work. The before/after totals go in the commit message.
- **S9** — arms: both verbs name the same next unit on a build with order values; both name the same
  on a build with none; an absent region refuses; a malformed region still refuses; the MISSING join
  still fires from the authored pair with the region present; the S4 divergence is pinned; a region row
  with no tracked spec is classified; and each of the two `NOT A UNIT` conditions still reports.

## 3. Non-goals (OUT)

- No change to what `--status` reads. It is already the region and is the verb the other is being
  brought into line with.
- No change to the MISSING join or to `roster_ids`. S3 states the boundary;
  `TOOL-dHonouredPark-1` is the unit that changes anything about the authored pair.
- No sorting of `--plan` by the order verb directly. That was the other option and it couples the
  unattended driver to a grammar the memory-tree kit owns, which is the cross-kit dependency this
  repo's stream rules exist to avoid. Reading the region gets the same order without the coupling.
- No new region and no new marker. The units region already has an address.
- No shared enumerator for the two verbs. See §8 F2 — it stays conditional on falling out of S1.

## 4. Design

### Data model

Unchanged. `--plan` stops parsing spec files for the unit LIST and parses the region instead; both
carry id, status and title. The spec-file walk survives for S6's two diagnostics and for
`plan_state`'s THIN/FORKED/READY classification, which the region does not carry.

### Inventory

The units region has more readers than rev-1 counted, and `verb_plan` is already among them. Call
sites of `UNITS_OPEN`, `unit_rows`, `unit_ids_of` and `nonterminal_units` sit at `unattended.sh:1251`,
`:1572`, `:1874`, `:2041`, `:2226`, `:2693-2722` and `:3522`; the driver's own comment at `:1864`
already calls `unit_rows` the THIRD reader before this unit adds anything. rev-1's "three readers after
this unit" was wrong in both direction and count.

### Migration

One commit. `--plan`'s output changes ORDER for any build carrying order values and is otherwise
identical **except** for S6 and S7, which it preserves and adds deliberately.

Downstream readers exist and are not counted here. `unattended.test.sh` asserts on `--plan` output in
several places and the protocol describes it in prose; the exact number is a derived population and
rev-2 authored it as "eleven assertions", which round 2 found wrong under every reading. Derive it
with a grep when you make the change. rev-1's "nothing downstream parses it" was overstated either
way; they parse the id, which S1 keeps as the join key.

### The fixture this unit has to build, and why it is not a small job

`grep -n Order tools/unattended/unattended.test.sh` returns nothing. The `readme()` fixture renders a
four-column units region (Unit · Status · Rev · Last change) while the live corpus renders six, with
Order second. **AC1 quantifies over a build whose units carry order values, and no such build exists in
the harness.**

The fixture work is NOT additive, which rev-2 implied by naming only the column mismatch. `readme()`
writes a single hardcoded row with status `OPEN`; `mkspec()` always writes the same `-1` filename; and
`units()` only APPENDS a second marker pair, which trips the malformed refusal rather than adding a
row. AC1 and AC8 need two or more units carrying order, and AC6 needs every row terminal — so each
requires changing SHARED helpers that every `--plan`, `--status` and `--preflight` arm in the file
depends on. Budget the regression risk accordingly; that is the real cost of this unit.

The column mismatch itself is harmless and must not be "fixed" as a side effect: `nonterminal_units`
and `unit_rows` both select with column-count-agnostic patterns.

### Alternatives rejected

**Sort `--plan` by the order verb.** Smallest diff. Rejected by the owner and on the coupling: the
driver would have to read a status-header grammar the memory-tree kit defines and can change, and the
two kits are separate streams.

**Document the divergence.** Zero code, and it leaves two verbs volunteering different next units —
the two-answers-to-one-question class this build's parent spent itself removing. Note that S4 does
document a divergence, but a strictly narrower one that survives by design rather than by neglect.

### THREE copies of the sentence this unit falsifies, and only one is editable

`--plan`'s behaviour is described in three tracked places, and two of them are RENDERS that a drift
check refuses to see edited directly:

- `tools/unattended/PROTOCOL.template.md` — the SOURCE. `memory/guides/UNATTENDED-PROTOCOL.md` is a
  byte-identical copy of it (verified: same size, `diff` of both CR-stripped is empty), and
  `adopt-unattended.sh` exits 1 on any divergence. That refusal is the `unattended skill wiring` leg
  §7 names, so editing the rendered guide alone REDS a gate this spec lists as green.
- `tools/unattended/SKILL.template.md` — the SOURCE for `.claude/skills/unattended/SKILL.md`, which
  carries the same description at the same line and is diffed by the same check.

So the edit is: change both TEMPLATES, re-render, and never touch a rendered copy. This is the same
edit-the-template-first rule `TOOL-dHonouredPark-2` carries for `BUILD-METHOD.md`; rev-2 named only the
rendered guide, and round 2 found both source files absent from every list.

### Files touched (estimate)

`tools/unattended/unattended.sh` · `tools/unattended/unattended.test.sh` including the new
order-bearing fixture and the shared-helper changes it forces · `tools/unattended/PROTOCOL.template.md`
and `tools/unattended/SKILL.template.md` with their two renders · the kit version sites ·
`.memory-tree.conf` for S8 · `memory/DECISIONS.md` for this unit's ruling row.

## 5. Production-readiness checklist

- security — N/A.
- perf / scale — strictly cheaper for the list; the S6 walk keeps one pass over the spec files.
- a11y — N/A.
- i18n — N/A.
- error / empty / loading states — an absent region REFUSES by S5, a malformed one already does. A
  build with no units renders the region's own empty-case sentence and `--plan` reports no next unit,
  which is existing behaviour and stays.
- observability — the refusal names the file and the marker, so a stale render is distinguishable from
  an empty build. S6 is the other half: the two `NOT A UNIT` conditions keep reporting.
- risks — the silent fallback, removed by S5. Second risk: S6. Reading the region is the obvious
  simplification and it silently drops a diagnostic that fires on five tracked specs today, which is
  precisely the kind of loss a green test suite would not notice.
- read path — `memory/guides/UNATTENDED-PROTOCOL.md` describes what `--plan` prints and is a capped
  member at 48838 B; this unit charges it and its own `memory/DECISIONS.md` row. S8 owns the
  measurement and AC9 the record. rev-1 named the file and never priced it; rev-2 said it was priced
  and still recorded no figure.
- testing + left-shift gates — S7's arms, plus the order-bearing fixture they need.
- migration / rollback — one commit, invertible.
- user docs — the protocol, at the line that describes the source.

## 6. Acceptance criteria

- **AC1** — When `--plan <slug>` and `--status <slug>` run over a build whose units carry order values
  **and which has a run-state file**, both name the SAME unit as next. The run-state clause is not
  decoration: `verb_status` fails 10 at `:2210` without one, so this criterion is unreachable on a bare
  build and rev-1 did not say so.
- **AC2** — When `bash tools/unattended/unattended.sh --plan <slug>` and `--status <slug>` run over a
  build carrying NO order values, with a run-state file present, both name the SAME unit as next.
- **AC3** — When the `gen:build-units` region is ABSENT, `--plan` exits non-zero naming the file and
  the marker, and does NOT fall back to the spec derivation. Observed RED first: at BASE the outer
  `grep -qF` guard makes this case fall through silently.
- **AC4** — When the region's markers are MALFORMED, `--plan` refuses. **Green at BASE** (`fail 42` at
  `:1572-1576`, armed at `:1601-1611`); kept as a regression guard, not as evidence.
- **AC5** — When a build's authored `roster:units` pair names an id no spec defines, `--plan` still
  reports it MISSING with the region present, proving S3's boundary held.
- **AC6** — On a build whose specced units are ALL terminal, whose roster names an unspecced id, and
  whose run-state file declares a phase,
  `--plan` names the missing unit and `--status` reports no non-terminal unit, and an arm asserts
  exactly that pair of outputs. This is S4's pinned exception: the divergence is intended and is
  therefore tested, not asserted away.
- **AC7** — When a tracked spec carries no status header, `--plan` still reports `NOT A UNIT (no
  status header)`. Observed against the five live instances.
- **AC8** — When `--plan` runs over a build carrying order values, its rows appear in build order.
- **AC9** — When `python tools/memory-tree/corpus_ids.py --report` runs before and after, both totals
  are recorded in the commit message and `.memory-tree.conf` carries this unit's own movement line.
- **AC10** — When a spec's `# ` heading carries no id-shaped first token, `--plan` still reports
  `NOT A UNIT (heading id does not parse)`. **This needs a staged fixture**: zero tracked specs produce
  that row, which the driver's own comment states, so the five live instances cover AC7 and nothing
  covers this one.
- **AC11** — When a region row names an id no tracked spec defines, `--plan` classifies it by S7 rather
  than falling through.
- **AC12** — When `bash tools/unattended/adopt-unattended.sh --check` runs, it is green: both templates
  and both renders agree. Observed RED first by editing a rendered copy alone, which is the state
  rev-2 would have landed in.

## 7. Gates

`unattended kit gate` · `memory hygiene` (incl. check 16) · `check-kit-versions.sh` ·
`check-verdict-epoch.sh` · `check-arms.py` floors — the driver gains `fail` branches ·
`unattended skill wiring`.

**Declared skip, with its compensating check.** The arms this unit adds live in
`tools/unattended/unattended.test.sh`, and **no leg on the bar runs that file**: `tools/gate-legs.json`
carries only `unattended kit gate`, `playbook validity gate` and `unattended skill wiring` for this
kit, so `GATE_FULL=1 GATE_SELFTESTS=1` does not reach them. That is deliberate — the kit's self-tests
were pulled off the bar at the owner's ruling of 2026-08-23 for costing 68% of it, and a standing owner
instruction forbids running them. rev-1's AC6 named `bash tools/unattended/check-unattended.sh` as the
runner that would observe an arm RED; that script never invokes `unattended.test.sh`, so the criterion
could not have been met as written.

The compensating check: each arm is observed RED against a staged break at authoring time and the
observation recorded in the unit's build record with the staged diff, and the owner is handed the one
command — `bash tools/unattended/run-unattended-gates.sh` — rather than having `--selftests` added to
this list. An exemption is not coverage, so the exemption is written down with what stands in for it.

## 8. Open questions

- **F1 — does `--plan` keep reading the spec files at all?** RESOLVED (agent, 2026-08-25, delegated) —
  yes, for two things the region does not carry: `plan_state`'s THIN/FORKED/READY classification, and
  S6's two `NOT A UNIT` conditions. The region supplies the SET and its ORDER. One source per question,
  which is the rule rather than a compromise between two.
- **F2 — should `--status` and `--plan` share one enumerator function?** RESOLVED (agent, 2026-08-25, delegated)
  — NO, not in this unit. It would make divergence structurally impossible rather than merely tested,
  which is the better end state; but it widens a scoped change into a refactor of two verbs with
  different output contracts, and S4 establishes that one INTENDED divergence survives it anyway, so
  the refactor would not even close the question it is for. S9's arms are the guard. The refactor is
  its own backlog row, filed with this resolution rather than left as a conditional nobody decides.

## 9. Revision log

- rev-4 · 2026-08-25 · M3 fork sweep. F1 restated as a question and resolved; F2 resolved NO rather
  than left conditional, with the shared-enumerator refactor filed as its own backlog row.
- rev-1 · 2026-08-25 · initial draft, from the owner's ruling on `dFramedEntrypoint`'s third park —
  the one park that was still unruled when the build landed.
- rev-3 · 2026-08-25 · round-2 fold. Corrected S6's second diagnostic — the branch tests whether the
  heading's id parses, not whether heading and status header disagree, which they cannot, since the
  status header carries no id — and split AC7 in two after round 2 measured ZERO live instances of that
  condition against five of the other. Added the three-copies section: the protocol guide and the
  installed skill are RENDERS whose drift check refuses a direct edit, so both TEMPLATES are the
  subject and rev-2 named neither. Took the read-path charge as declared scope with a real measurement
  (S8, AC9) rather than the word "priced". Added S7 for a region row with no tracked spec, which S1
  makes representable. Extended AC1/AC2/AC6's run-state precondition to the phase fact the verb also
  demands, and recorded that the fixture work forces changes to shared helpers. Replaced the authored
  downstream-reader count with a derivation, and dropped line-number citations.
  AC numbering was RESEQUENCED in this revision; AC labels in the entries below refer to the
  numbering of the revision that wrote them, not to this one.

- rev-2 · 2026-08-25 · spec-audit fold. Corrected §1: `--plan` orders by lexical PATH, not by id. S1
  now records that `verb_plan` ALREADY reads the region and that rows join by id, not by link. Added
  S4 and AC6 for the divergence rev-1 claimed away, and S6 and AC7 for the two `NOT A UNIT`
  diagnostics the move would have dropped. Narrowed S5 to the absent case after finding the malformed
  refusal already ships and is armed. Added the missing run-state clause to AC1. Took the
  order-bearing fixture into scope — no such fixture exists. Replaced rev-1's AC6 runner, which cannot
  run the file it names, with a declared skip and its compensating check. Priced the read-path charge.

## 10. Reuse audit

Memory-recall terms for the regrounding read: `plan status next unit units region rendered derived
divergence build order id order driver verbs not a unit`.

The seam is the `gen:build-units` region and its existing readers, enumerated in §4. `verb_plan` is
already one of them, which rev-1 missed and which changes S1 from "add a reader" to "extend a read" —
the smaller and safer framing.

The negative findings worth recording: there is no shared enumerator today, which is why two verbs
could drift at all (F2 asks whether creating one falls out of this change); and there is no
order-bearing fixture in the harness, so the arm that would have caught this divergence when it was
introduced could not have been written without building one first.
