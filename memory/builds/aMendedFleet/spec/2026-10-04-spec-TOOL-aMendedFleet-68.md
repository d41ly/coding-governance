# TOOL-aMendedFleet-68 — the unattended Skill becomes a router of at most 10 KiB

**Status:** CLOSED · rev-3 · 2026-10-04 · node a · Tier-2 · base 7af5f564 · streams tooling · ratified 2026-10-04 · advances TOOL-aScouredKit-23 · order 68

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-04-build-TOOL-aMendedFleet-68-1-acceptance-ledger.md](../build/2026-10-04-build-TOOL-aMendedFleet-68-1-acceptance-ledger.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

The unattended Skill is the first file every unattended run loads, and it is 90,128 bytes rendered
and 1,299 lines in its template, beside a contract that is already four files and 136,111 bytes. It
calls itself the operating summary of that contract. The report found it the largest single item in
the 239 KB an unattended start owes before any code, and the owner ruled the full context diet in.
This unit moves every ORDERING and every rule the Skill states that no contract file states into the
contract's verbs companion, then cuts the Skill to a router: which path, which steps in which order
by pointer, the values only a render can supply, and the few blocks a gate reads from the Skill
itself. A ceiling and a leg keep it there, which is half of what `TOOL-aScouredKit-23` asks.

## 2. Scope (IN)

- **S1** — PORT FIRST. `tools/unattended/VERBS.template.md` gains one section, `## The paths, in
  order`, holding for each path the Skill names the ordered steps it prescribes: the verb, the
  condition that selects it, and the protocol section it answers to. It carries every step order and
  every rule the Skill states that neither `UNATTENDED-PROTOCOL.md` nor a companion states, written
  without a placeholder, since the companion is copied and never rendered: a conf KEY where the Skill
  had its rendered value. `memory/guides/UNATTENDED-VERBS.md` takes the same bytes. The port lands in
  the same commit as S2 or before it, never after. Observed by AC7, AC8, AC9.
- **S2** — THE ROUTER. `tools/unattended/SKILL.template.md` keeps its front matter, the opening
  paragraph naming the contract, the path table, and per path a short ordered list of rendered
  commands and pointers into S1's section and the protocol. Every other paragraph leaves it.
  Observed by AC1, AC6.
  **Readers:** by name: `tools/unattended/check-unattended.sh` checks 16, 31, 41 and 43, which read
  `SKILL.template.md`; `tools/unattended/adopt-unattended.sh` and its test's `hit` arms, which read
  the render; `memory/guides/SESSION-KICKOFF.md`, which names the Skill's directive table.
  by value: `tools/unattended/check-unattended.sh`, whose four checks compare the directive pairs,
  the no-override members, the process-ledger sentence and the hold paragraph's order, all of which
  S3 keeps; and `tools/unattended/adopt-unattended.test.sh`, whose arms read rendered values, which
  S4 keeps.
- **S3** — WHAT A GATE READS STAYS, byte for byte where a gate compares bytes: the directive table
  with its `M<n>` carriers and the scope rule beside it; the paragraph opening `TWO items have NO
  override`; the sentence that a process not in the ledger is never killed; and, under a `## Close`
  heading, the paragraph opening with the hold lead check 43 finds. Observed by AC2, AC3, AC4, AC5.
  The checker reads the Skill template in more places than those four, so each of these stays too:
  the first `unattended.sh --preflight` line above the first `/session-kickoff` line (check 18); the
  prompt path's `RUN the orientation probes`, `Write the build folder`, `AskUserQuestion`,
  `PUSH THE BRANCH` and bolded `Preflight` lines in that order under `## Start a run from a PROMPT`
  (check 20); the routing table's backticked modes under `## Which path` (check 24); `there is no
  machine half` and `ordinary code build` under `## Start a PLAYBOOK run` (check 25); an
  `unattended.sh <verb> ` invocation for every declared verb (check 26); and a `## Land` section
  naming `--prepare` and `--land` (check 44). The step leads the kit suite's fixtures mutate stay
  spelled as they are, so no arm becomes a fixture no-op.
- **S4** — EVERY PLACEHOLDER STAYS. Each `{{...}}` token the template carries at the pass's starting
  commit appears at least once in the router, because a placeholder is a value only the render can give a run and the
  companion cannot carry one. Observed by AC6.
- **S5** — THE CEILING. `tools/template-size-limits.txt` gains a row for
  `.claude/skills/unattended/SKILL.md` at 10240 bytes, and `tools/gate-legs.json` a leg
  `unattended skill size` running `check-template-size.sh` on it with a ceiling of 300 seconds and no
  guard, the shape of `unattended protocol size`. Observed by AC1, AC10.
- **S6** — `tools/unattended/README.md`'s row for the Skill says it is a router and names the verbs
  companion section it routes into. Observed by AC9.
- **S7** — Arms in `tools/unattended/adopt-unattended.test.sh` that `hit` a rendered string are kept
  pointing at strings the router still carries; any that cannot be are moved to the closest rendered
  string of the same placeholder. NOT OBSERVED by a criterion here: the suite runs once at the close,
  and the arm is declared under `New arm:` in §7.
- **S8** — THE MANIFEST STAMP. `tools/gate-legs.json` is on the kickoff manifest's `watch:` line, so
  the commit that adds S5's leg also re-stamps `last-audit:` in `memory/guides/SESSION-KICKOFF.md`
  with a delta line in its message; the staged manifest leg of `.githooks/pre-commit` refuses the
  commit otherwise. Observed by AC11.

## 3. Non-goals (OUT)

- Any change to `UNATTENDED-PROTOCOL.md`. It sits 418 bytes under its declared ceiling, so §8 F1 puts
  the port in the verbs companion, which the protocol already calls the second half of the contract.
- A new companion file, a new install destination or a new render step.
- Changing what any rule SAYS. A sentence moves or becomes a pointer; a rule the port finds stated
  two different ways is recorded in the unit's acceptance ledger and resolved in favour of the
  protocol, never rewritten here.
- The `WIRE-INTO-PROJECT.md` half of `TOOL-aScouredKit-23`, which this unit advances and does not
  close.
- Retargeting checks 16, 41 or 43 at the companion; S3 keeps their subjects in the Skill.

### Edges

- **consumes-from** external — the owner's third answer in the run mandate record, which grants the
  structural context diet and names this cut; without it the protocol companion is a governance
  carrier this run may not edit.
- **hands-off** external — the unattended kit version, minted at the lander by unit 65 or owed once at
  the close.

## 4. Design

### Evidence

Read at base `7af5f564`.

- `tools/unattended/SKILL.template.md` is 90,108 bytes and its render 90,128; its 21 `##` sections run
  from 212 to 13,631 bytes, the largest being While it runs, Start a run, Close and Start a run from a
  PROMPT. PINNED, measured with `wc -c` and an `awk` section sum on 2026-10-04.
- The four contract files total 136,111 bytes: the protocol 65,274, stops 35,806, verbs 22,478 and
  asks 12,553. The protocol's declared ceiling is 65,692; `GUIDE_CAP_BYTES` binds the companions at
  98,304. The verbs companion is 243 lines of verb bullets and carries no `##` heading today.
- The companions are byte-compared against their templates and carry no placeholder; the Skill
  carries twelve distinct placeholders, `{{KIT_DIR}}` 46 times.
- `check-unattended.sh` reads the Skill TEMPLATE in four places: check 16 arm A joins the directive
  table's `handle:M<n>` pairs to the driver's registry; check 16d joins the no-override paragraph's
  members to `DOD_NO_OVERRIDE`; check 41 needs the process-ledger sentence; check 43 reads the hold
  paragraph inside `## Close` and compares the order of its first occurrences. Check 31 grades route
  scripts the render names and is an announced skip when it names none.
- The `unattended kit gate` leg carries a 16,040-second ceiling and its checker takes no selector but
  check 28's, so no pass can run it; §6 observes each block directly instead.
- `tools/check-template-size.sh` gates any subject named on its command line against a row in
  `tools/template-size-limits.txt`, and exits 6 when a subject states its own budget in prose that
  disagrees with the row; the router therefore states no byte figure.

### The disposition rule, applied paragraph by paragraph at build time

1. A paragraph a gate reads from the Skill stays, per S3.
2. A paragraph restating a protocol or companion section becomes a pointer to that section.
3. A paragraph whose order of steps, or whose rule, no contract file states moves to S1's section,
   with each rendered value replaced by the conf key that supplies it.
4. A rendered command a step needs stays in the router beside the pointer, so every placeholder
   survives per S4.

### Inventory

- The section heading `## The paths, in order` in the verbs companion.
- The leg name `unattended skill size`.

### Files touched (estimate)

- `tools/unattended/SKILL.template.md`
- `.claude/skills/unattended/SKILL.md`
- `tools/unattended/VERBS.template.md`
- `memory/guides/UNATTENDED-VERBS.md`
- `tools/unattended/README.md`
- `tools/unattended/adopt-unattended.test.sh`
- `tools/template-size-limits.txt`
- `tools/gate-legs.json`
- `memory/guides/SESSION-KICKOFF.md`
- `tools/template-size-highwater.txt`, `tools/govkit/registry.toml`, `tools/govkit/subject-pins.tsv`
  and `memory/map/features/unattended.md` with its generated map: the new leg's high-water row, its
  `[[exempt_leg]]` row, its subject pin and its map claim, the four places the `unattended protocol
  size` leg was declared when it landed.

### Rollout

The render is regenerated with `bash tools/unattended/adopt-unattended.sh` in the same commit as the
template. A run already in flight reads the Skill once at its start, so the cut reaches the next run.

### Alternatives rejected

- **Port into `UNATTENDED-PROTOCOL.md`, as the report words it.** It has 418 bytes of headroom, so
  the port would first raise a declared ceiling, an owner call this mandate does not make.
- **A fifth contract file for the paths.** It needs an install destination, a byte-compare leg and an
  adopter step; the verbs companion is already the contract's half about what to run.
- **Generating the Skill from the companion.** The router's job is the rendered values and the path
  choice, which the companion cannot hold; a generator would have nothing to generate from.

## 5. Production-readiness checklist

- security — no executable surface moves; the rendered commands are the ones the Skill carries today.
- perf / scale — the point of the unit: a run's first read falls from about 90 KB to at most 10 KiB,
  and it reads the one path section it needs rather than every path.
- error / empty / loading states — N/A: a document, not a program.
- observability — the new leg prints the byte count and headroom on every bar.
- risks — a dropped instruction is the failure; AC7 and AC8 compare verbs and their order against
  the base Skill, and the closing diff review reads the cut.
- testing — AC1 to AC11 directly; the arm in S7.
- migration — an adopter re-renders with the kit's own adopter on the next kit update.
- user docs — S6.

## 6. Acceptance criteria

Every "base" below means the pass's starting commit, the tip the unit pass begins from, and not the
design base `7af5f564`: unit 63 edits `tools/unattended/SKILL.template.md` and its render first, so
a comparison against `7af5f564` would red on that unit's change.

- **AC1** — When `bash tools/check-template-size.sh .claude/skills/unattended/SKILL.md` runs at the
  unit's tip, it exits 0 against the 10240 row.
  Red when: the render exceeds the ceiling, or no row declares it.
- **AC2** — When check 16 arm A's `awk` row filter over `tools/unattended/SKILL.template.md` is run at
  base and at the tip, the two sorted lists of `handle:M<n>` pairs are identical.
  Red when: a directive row is lost or its carrier changes.
- **AC3** — When check 16d's paragraph filter, the lines from `items have NO override` to the next
  blank line, is run at base and at the tip, the backticked member sets are identical.
  Red when: a no-override member leaves the Skill.
- **AC4** — When the tip template is folded to one line with `tr` and searched with `grep -qiF` for
  `a process not in the ledger is never killed`, it is found.
  Red when: the sentence check 41 needs is gone.
- **AC5** — When check 43's extraction, the paragraph opening with the hold lead inside `## Close`,
  is run at base and at the tip, the two outputs are byte-identical.
  Red when: the hold routing moved, changed or left the Close section.
- **AC6** — When `grep -oE` extracts the distinct `{{NAME}}` tokens of
  `tools/unattended/SKILL.template.md` at base and at the tip, the two sets are equal, and
  `bash tools/unattended/adopt-unattended.sh --check` exits 0.
  Red when: a placeholder is lost, or the render is out of sync with its template.
- **AC7** — When the distinct `--verb` tokens are extracted from the base Skill template, every one
  appears in the tip's router or in the `## The paths, in order` section of
  `tools/unattended/VERBS.template.md`.
  Red when: a verb the Skill told a run to call is named nowhere a run now reads.
- **AC8** — When, for each path, the first-occurrence order of its `--verb` tokens is extracted from
  that path's base Skill section and from its subsection of the ported section, the two orders agree.
  Red when: a step moved relative to another.
  figure: the per-path orders are DERIVED at observation time.
- **AC9** — When `cmp tools/unattended/VERBS.template.md memory/guides/UNATTENDED-VERBS.md` runs it
  exits 0, `grep -c "{{" tools/unattended/VERBS.template.md` prints 0, and
  `grep -n "The paths, in order" tools/unattended/README.md tools/unattended/SKILL.template.md` hits
  both.
  Red when: the companion copies differ, carry a placeholder, or the router and README do not point
  at the section.
- **AC10** — When, in a scratch clone under a short `%TEMP%` path, 11,000 bytes are appended to
  `.claude/skills/unattended/SKILL.md` and `bash tools/check-template-size.sh .claude/skills/unattended/SKILL.md`
  runs, it exits 1. This is the staged break for the new leg.
  Red when: an oversized router passes.
- **AC11** — When `bash skills/session-kickoff/manifest-check.sh` runs after the unit's commit, it
  exits 0, and `git diff HEAD~1 HEAD -- memory/guides/SESSION-KICKOFF.md` shows the `last-audit:`
  line moved.
  Red when: check 5 reports unaudited drift on `tools/gate-legs.json`.

## 7. Gates

`unattended skill wiring` · `unattended kit gate` · `check-wiring self-test` · `lexicon naming predicates` · `recall floor` · `recall floor arms` · `run-gates canary` · `run-gates gov canary` · `kickoff-manifest ratchet` · `line length` · `kit epoch (shipped bytes move, the version moves)` · `spec tokens (a spec's own names resolve)`

The new leg S5 adds is not on the line above: the manifest names it only once this unit lands, and
from then on it is graded like its sibling `unattended protocol size`. AC10 is its staged break.

New arm: `tools/unattended/adopt-unattended.test.sh` · the rendered router read for each placeholder's value, against the base render, whose strings all exist · none

## 8. Open questions

- **F1 — Where does the Skill-only ordering go?**
  Options: `UNATTENDED-PROTOCOL.md`, as the report words it; the verbs companion; a new companion.
  The protocol has 418 bytes of headroom under an owner-declared ceiling; a new companion is a new
  install destination; the verbs companion is the contract's own second half and has about 75 KB of
  headroom under the guide cap.
  RESOLVED (agent, 2026-10-04, delegated): the verbs companion, per S1.
- **F2 — Do the four gate-read blocks stay, or do their checks move to the companion?**
  Options: keep them in the router; retarget checks 16, 41 and 43. Retargeting edits a 16,040-second
  checker no pass can run, and `SESSION-KICKOFF.md` names the Skill's table as the list a run reads.
  RESOLVED (agent, 2026-10-04, delegated): keep them, per S3.
- **F3 — Does the cut need an owner turn?**
  Options: an owner turn; the mandate's third answer. The owner answered "full diet too" and named
  the unattended Skill cut to a router as part of it.
  RESOLVED (owner, 2026-10-04): the cut is in scope, per the run mandate record's third answer.

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft, from a read of the Skill template's sections, the four contract
  files' sizes and headings, and the four Skill reads in `check-unattended.sh` at base.
- rev-2 · 2026-10-04 · S4 · S8 · §6 · AC11 · §7 · M2 cross-read: unit 63 edits the Skill template
  before this unit, so S4 and every base-against-tip criterion now compare against the pass's
  starting commit; and `tools/gate-legs.json` is a watched path, which unit 78 and unit 94 re-stamp
  for and this spec did not, so S8 re-stamps the manifest and AC11 observes it.
- rev-3 · 2026-10-04 · S3 · Files touched · build pass: the evidence named four Skill reads in
  `check-unattended.sh`, and the tree at the pass's base holds six more (checks 18, 20, 24, 25, 26
  and 44), each failing or going silent if its block left the Skill; S3 now keeps them. A new leg is
  also declared in the exempt-leg registry, the subject pins and the map, as its sibling's was.

## 10. Reuse audit

The seams extended are the verbs companion `tools/unattended/VERBS.template.md`, which the protocol
already names as the second half of the contract, and `tools/check-template-size.sh` with its limits
file, which the `unattended protocol size` leg already uses for the same shape of ceiling. `python
tools/codebase-map/reuse_lookup.py "route an agent to the protocol section for each run path instead of
restating it"` returned name-stem neighbours such as `build_run_model` and `derive_run_eras`, none a
document router; no existing seam renders a Skill from the contract, and the adopter's render is
template substitution only. Recall returned `TOOL-aScouredKit-23`, which measured the Skill as a
genuine re-derivation of the protocol rather than a copy and asked for its ceiling, which S5 supplies;
`TOOL-dUnstalledConvoy-17`, on a Skill claim that the protocol omitted verbs which it did carry, which
is why AC7 compares verbs mechanically; and `TOOL-dAlignedCarrier-3`, on scope prose living in the
directive table, which S3 keeps. Where the report and the tree disagree: the report measured 88,481
bytes; the render is 90,128 at base.

Recall terms used: `python tools/memory-recall/query.py "why is the unattended Skill so large, and what
in it is not stated in the protocol" --terms "unattended Skill router SKILL.template.md protocol
paraphrase pointer-not-copy companion VERBS ordering size cap diet"`
