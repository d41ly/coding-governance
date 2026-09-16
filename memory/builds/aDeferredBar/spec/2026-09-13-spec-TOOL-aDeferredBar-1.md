# TOOL-aDeferredBar-1 — the instruction: no bar and no suite inside a pass, at every carrier a build agent reads

**Status:** CLOSED · rev-4 · 2026-09-14 · node a · Tier-2 · base b2a330be · streams tooling · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-13-build-TOOL-aDeferredBar-1-1-research-bar-in-a-pass.md](../build/2026-09-13-build-TOOL-aDeferredBar-1-1-research-bar-in-a-pass.md) | research | TOOL-aDeferredBar-2 TOOL-aDeferredBar-3 |
| [2026-09-14-build-TOOL-aDeferredBar-1-2-acceptance-ledger.md](../build/2026-09-14-build-TOOL-aDeferredBar-1-2-acceptance-ledger.md) | journal | — |
| [2026-09-13-prompt-TOOL-aDeferredBar-1-0-run-mandate.md](../prompts/2026-09-13-prompt-TOOL-aDeferredBar-1-0-run-mandate.md) | journal | — |
| [2026-09-13-prompt-TOOL-aDeferredBar-1-1-spec-brief.md](../prompts/2026-09-13-prompt-TOOL-aDeferredBar-1-1-spec-brief.md) | journal | — |
| [2026-09-14-prompt-TOOL-aDeferredBar-1-2-build-brief.md](../prompts/2026-09-14-prompt-TOOL-aDeferredBar-1-2-build-brief.md) | journal | — |
| [2026-09-14-review-TOOL-aDeferredBar-1-closing-diff-round1.md](../reviews/2026-09-14-review-TOOL-aDeferredBar-1-closing-diff-round1.md) | diff-review | TOOL-aDeferredBar-2 TOOL-aDeferredBar-3 |
| [2026-09-14-review-TOOL-aDeferredBar-1-closing-diff-round2.md](../reviews/2026-09-14-review-TOOL-aDeferredBar-1-closing-diff-round2.md) | diff-review | TOOL-aDeferredBar-2 TOOL-aDeferredBar-3 |
| [2026-09-14-review-TOOL-aDeferredBar-1-closing-diff-round3.md](../reviews/2026-09-14-review-TOOL-aDeferredBar-1-closing-diff-round3.md) | diff-review | TOOL-aDeferredBar-2 TOOL-aDeferredBar-3 |
| [2026-09-14-review-TOOL-aDeferredBar-1-spec-audit-round1.md](../reviews/2026-09-14-review-TOOL-aDeferredBar-1-spec-audit-round1.md) | spec-audit | TOOL-aDeferredBar-2 TOOL-aDeferredBar-3 |
| [2026-09-14-review-TOOL-aDeferredBar-1-spec-audit-round2.md](../reviews/2026-09-14-review-TOOL-aDeferredBar-1-spec-audit-round2.md) | spec-audit | TOOL-aDeferredBar-2 TOOL-aDeferredBar-3 |

<!-- /gen:spec-records -->

## 1. Goal

A build pass runs no merge bar and no self-test suite; it verifies with the one direct check its
spec names, and the bar runs once, at the main loop, after every unit is terminal. This unit states
that rule at each of the five carriers a build agent actually reads, changes each at its SOURCE and
re-renders, so the instruction stops being re-derived per brief by a writer who cannot see the
gate ledger. The research record under `build/` measured the cost the rule removes: one unit spent
68 minutes on a diff whose direct checks take seconds, and 204 of the 408 plain-bar invocations in
the operator's transcript store came from inside a sidechain.

## 2. Scope (IN)

- **S1** — The child prompt in `tools/workflows/unattended-unit.js` gains the ban and its
  substitute, in the register of its existing driver-step sentences: the five invocation forms it
  may not run, the direct check it verifies with instead, and the rule that a criterion only a suite
  can observe is returned to the parent in `summary` rather than run. The engine identity on line 44
  moves from `1.0` to `1.1` in both tokens of that line. Observed by AC1, AC2 and AC8.
- **S2** — `GROUND` in `tools/workflows/unattended-build.js` gains ONE sentence, because it prefixes
  every stage agent and the unit child alike: no stage of this program runs the merge bar or a
  self-test suite. The SPEC-stage writer prompt gains the acceptance rule: every criterion names a
  direct observation, never a bar or a suite. The marker on line 3 moves from `1.0` to `1.1`.
  Observed by AC3, AC4 and AC8.
- **S3** — M6 of `tools/memory-tree/BUILD-METHOD.template.md` REPLACES the sentence that starts
  "Then the diff-scoped gates" with the rule in §4, rendered to `memory/guides/BUILD-METHOD.md`
  under M1's unraised budget. `KIT_MEMORY_TREE_VERSION` in `tools/memory-tree/check-memory-hygiene.sh`
  moves `2.74` to `2.75`, and every live carrier of the `gov:kit memory-tree@` marker moves with it.
  Observed by AC5, AC6, AC7, AC9 and AC15.
- **S4** — One bullet under "While it runs" in `tools/unattended/SKILL.template.md`, rendered to
  `.claude/skills/unattended/SKILL.md`. `KIT_UNATTENDED_VERSION` in `tools/unattended/unattended.sh`
  moves `1.19` to `1.20`, and every live carrier of the `gov:kit unattended@` marker moves with it.
  Observed by AC10, AC11 and AC15.
- **S5** — Line 263 of `memory/guides/SESSION-KICKOFF.md` is qualified in place so the "run the
  full bar, never a list" trap reads as the push-boundary sentence it is, and the manifest is
  re-stamped in the same commit: `last-audit` and `last-body-change`, with a `manifest-audit: delta`
  line in the commit message. The manifest sat 14 bytes under `manifest-check.sh` C7's 25600-byte
  file cap before this unit, so the qualification is paid for by deleting the one traps bullet
  that restated a §B bullet — the retired read-path budget, `TOOL-dSpentCeiling-1`, which §B
  still records. Observed by AC12 and AC13.
- **S6** — This spec obeys the rule it states: no criterion in §6 names a bar, a `GATE_*=` prefix
  or a `*.test.sh` suite as its observation, and its §7 leg line resolves against the manifest.
  Observed by AC14 for the joins and by AC16 for the bar-token absence. This file is OUTSIDE the
  population of the gate `TOOL-aDeferredBar-2` lands, by that gate's cutoff: `SPEC_DATE` reads the
  filename date, 2026-09-13, which never changes, and the cutoff sits strictly past it. So the
  acceptance-ledger check AC16 spells is the observation there will ever be, not a stopgap. AC1's
  greps carry two banned spellings as grep ARGUMENTS, with `grep` at command position; the `BAR`
  regex unit 2 §4 spells matches none of §6's backticked tokens, probed 2026-09-14 on that regex
  typed from the section, which is the probe AC16 runs.

## 3. Non-goals (OUT)

- `tools/unattended/PROTOCOL.template.md` gains NO rule. Its render `memory/guides/UNATTENDED-PROTOCOL.md`
  measures 57815 bytes against the 61440-byte guide cap `GUIDE_CAP_BYTES` declares in
  `check-memory-hygiene.sh:84` — 3625 bytes of headroom, PINNED 2026-09-13 at `e3d0f68c` — and the
  rule is a method rule rather than a contract term: M1 says a rule that appears both in the method
  and in a carrier is a defect in the method. The protocol's marker moves with the kit bump and
  nothing else in it does.
- `tools/run-gates/run-gates.sh` gains no leg-selection flag. The plain bar's manifest guards ARE
  the scoped form, which is the build README's ruling and §8's second resolved fork.
- No adopter tree is touched, and no `[[render]]` row is added to any `kit.toml`.
- No refusal mechanism. Nothing here reads a command or denies a tool call; that is
  `TOOL-aDeferredBar-3`. No spec gate; that is `TOOL-aDeferredBar-2`.
- The twenty live-or-landed specs the research record counts as naming a bar in §6 or §7 are not
  rewritten. A terminal spec is frozen, and a live one is graded by unit 2 only when its filename
  date is at or after that unit's cutoff — which none of them is, this build's own three included,
  because the cutoff sits strictly past every spec date on any ref. Their bar tokens are COUNTED on
  unit 2's report line and not graded.
- No ceiling in `tools/gate-legs.json` moves, and no `*.test.sh` leaves the manifest.
- M1's byte budget is not raised and its `**Budget:**` prose line is untouched, so
  `check-template-size.sh`'s exit-6 parity arm keeps reading the same figure on both sides.
- The charter's §1 sentence "After each merge run a diff-scoped gate" is a landing rule at the main
  loop and agrees with the rule stated here; the charter and its template are governance carriers
  M3 veto 2 keeps out of a delegated run's reach, and they are not touched.
- `tools/workflows/unattended-unit.js` keeps its shape: one top-level definition, no loop, no array
  method, no arrow. S1 adds string literals to an existing concatenation and nothing else.

### Edges

- **consumes-from** external — the research record `build/2026-09-13-build-TOOL-aDeferredBar-1-1-research-bar-in-a-pass.md`,
  which resolved the three forks §8 marks and measured the corpus; and the byte headroom of
  `memory/guides/BUILD-METHOD.md` at the base, which S3 spends and AC6 observes. No criterion in §6
  rests on anything a sibling unit builds.
- **hands-off** `TOOL-aDeferredBar-2` — grading a spec's §6 observations and §7 leg tokens for a
  bar or suite invocation. S2's writer-prompt sentence is the INSTRUCTION and deliberately does not
  claim a gate refuses the token, because no gate does until that unit lands; that unit may add the
  gate's name to the sentence when it exists.
- **hands-off** `TOOL-aDeferredBar-3` — refusing the act at the tool call. The five forms S1's
  sentence enumerates are the forms that unit's predicate reads, and "the plain bar with no flag, at
  the main loop" is the one it admits before `VERIFYING`. One consequence is that unit's to price:
  the render verb S3 names, `bash tools/memory-tree/kit-dogfood-parity.test.sh --render`, is an
  invocation of a `*.test.sh`-named script that runs no suite, and AC6's `sed` render is the
  flag-free alternative if the predicate is textual.

## 4. Design

### The chain, verified against source

A unit child is prefixed with `cfg.ground`, which is the parent's `GROUND` constant at
`tools/workflows/unattended-build.js:335`, then handed its brief and spec
(`tools/workflows/unattended-unit.js:144`). Nothing in either prompt mentions gates. The instruction
to run one arrives through three carriers the child reads next, and the research record names each:
the spec's own §6 and §7, which the SPEC-stage writer (`unattended-build.js:403`) fills with the
invocation it knows; M6 of `memory/guides/BUILD-METHOD.md:180`, whose "diff-scoped gates" has no
spelling narrower than the bar because `run-gates.sh` has no leg filter; and the kickoff manifest's
trap at `memory/guides/SESSION-KICKOFF.md:263`, front-loaded at the hand-back. The Skill under
`.claude/skills/unattended/SKILL.md` instructs the MAIN LOOP and today says nothing about what a
pass may run. Five carriers, and the rule goes into each at its source.

### The sentences, verbatim

The build copies these. Each grep phrase AC1–AC5 and AC10 name sits on ONE source line, because a
grep cannot match across a JavaScript string concatenation or a markdown wrap.

**Carrier 1 — `tools/workflows/unattended-unit.js`, inside `PROMPT`, after `DRIVER_STEPS +` and
before the `'Commit with the unit id in the subject. …'` literal:**

```
'RUN NO MERGE BAR AND NO SELF-TEST SUITE in this unit: not run-gates.sh in any form, not a ' +
'GATE_FULL= or GATE_SELFTESTS= prefix, not run-selftests.sh, not run-unattended-gates.sh, not any ' +
'*.test.sh suite. Verify with the DIRECT check the spec\'s acceptance names — a checker run on a ' +
'staged break, a `--selftest` flag, a fixture. A criterion only a suite can observe is not run ' +
'here: name it in `summary` and the main loop runs the owed bar once, after every unit is terminal.\n' +
```

Line 44 becomes `version: '1.1', // gov:kit unattended-unit@1.1 — engine identity (deployed verbatim)`.
The six spellings are basenames and prefixes, never `tools/…` paths: `check-install-prefix.sh:63`
matches a kit-directory path with an extension, and the file's header rule that it spells no path
holds.

**Carrier 2 — `tools/workflows/unattended-build.js`.** `GROUND` gains, after the sentence ending
`it is the procedure you are bound by. `:

```
'No stage of this program runs the merge bar or a self-test suite, and neither does any agent it ' +
'spawns; a unit verifies with the direct check its spec names, and the bar runs once at the main ' +
'loop after the last unit is terminal. ' +
```

The SPEC-stage writer prompt gains, after `give its status header the \`order\` verb this roster
names. `:

```
'Every acceptance criterion names a DIRECT observation with its command — a checker on a staged ' +
'break, a `--selftest` flag, a fixture, a grep over a rendered file — never the merge bar, a ' +
'GATE_*= prefix or a *.test.sh suite: a unit whose criterion names one runs it and stalls for hours. ' +
```

Line 3 becomes `version: '1.0'` → `version: '1.1', // gov:kit unattended-build@1.1 — engine identity (deployed verbatim)`.
Both engine markers are paired against no constant — `TOOL-aHoistedPass-33` records it — so AC8
observes them by grep, not by a gate; they move because the prompt text an adopter receives moved.

**Carrier 3 — `tools/memory-tree/BUILD-METHOD.template.md`, M6.** The sentence run from "Then the
diff-scoped gates" through "commits nothing and says so." is REPLACED by:

> **A pass runs no merge bar and no self-test suite.** Its verification is the direct check its
> spec's acceptance names — a checker run on a staged break, a `--selftest` flag, a fixture — and a
> pass that needs a suite verdict returns that need to the main loop rather than running one. The
> bar runs ONCE, after the last unit is terminal: at the close under a mandate, at the push boundary
> otherwise. Where a pass touched files a leg guards and the MAIN LOOP judges a bar necessary, the
> plain bar with no flag is the scoped form — at the main loop, never in a child. A pass whose check
> is red is not followed by another: fix it, or park it with the reason. A pass that produced no
> change commits nothing and says so.

Measured before writing: the old run is 248 bytes and the new one 719, a delta of +471. The render
is 26439 bytes and 336 lines today, so it lands at about 26910 bytes against the 27648 cap and
about 341 lines against 350 — PINNED, measured 2026-09-13 at `e3d0f68c` with `wc -c` and a Python
`len(.encode())` over both runs; the build re-measures with AC6. That is also 31 bytes under the
26941 high-water in `tools/template-size-highwater.txt`, so no `--bump` is owed; a breach there is
advisory and would print `TEMPLATE-SIZE WARN`, not red. The replacement spells no path: M1 already
names the bar by `{{TOOL_ROOT}}run-gates/run-gates.sh`, and M6 says "the bar". Render with
`bash tools/memory-tree/kit-dogfood-parity.test.sh --render`, which rewrites the four live copies
from their templates — see the §3 edge on that verb's name — or apply the two substitutions AC6
spells by hand; the result is byte-identical either way.

**Carrier 4 — `tools/unattended/SKILL.template.md`, the FIRST bullet under `## While it runs`:**

> - **No merge bar and no self-test suite inside a pass — yours or any agent you dispatch.** A pass
>   verifies with the direct check its spec names; a unit that needs a suite verdict returns the
>   need in its `summary` and does not run one. The bar runs ONCE, at `VERIFYING`, after the last
>   unit is terminal: `--close` runs the plain bar for `gates-green`, and kit work owes the
>   `GATE_SELFTESTS=1` form too, run by you at `VERIFYING` and nowhere earlier. Where a pass touched
>   files a leg guards and you judge a bar necessary, the plain bar with no flag is the scoped form,
>   at the main loop and never in a child. The rule is the build method's M6; this bullet points at
>   it.

Rendered by `bash tools/unattended/adopt-unattended.sh`, which also re-copies the three guides and
the fixture. `check-unattended.sh` check 16 reads the Skill's non-overridable paragraph and nothing
this bullet touches; `check-method-carriers.sh` arm 5 reds only a `## M<n>` heading, and the bullet
carries none.

**Carrier 5 — `memory/guides/SESSION-KICKOFF.md:263`.** The bullet becomes:

> - Adding ONE gate leg trips a SET of meta-gates that GROWS as new ones land — at the push boundary
>   run the full bar, never a list; inside a build pass run each meta-gate's own script by hand,
>   never the bar (BUILD-METHOD M6). A leg needs a `[[gate_leg]]` in its kit's `kit.toml`, else an
>   `[[exempt_leg]]`.

It sits in `### Environment traps worth front-loading`, where `manifest-check.sh` C11 caps a bullet
at 400 bytes; the new bullet is about 330 and AC12 observes the cap through the checker. C7 caps
the whole FILE at 25600 bytes and it measured 25586 at the base, so the bullet's +130 is paid for
by deleting the trap that began "A spent budget blocks RECORDING work" (271 bytes): its one fact,
that the read-path ceiling is retired under `TOOL-dSpentCeiling-1`, is the §B bullet two sections
up. C7 says trim and never raise, so no other disposition existed. The
manifest is WATCHED on `tools/memory-tree/check-memory-hygiene.sh` and `memory/guides/BUILD-METHOD.md`,
both of which S3 edits, so C5 and its staged form C5s demand the re-stamp in the SAME commit:
`last-audit` takes a datetime that advances and the sha of `git merge-base origin/main HEAD`,
because the run's branch is not the default branch; `last-body-change` takes the sha of the commit's
parent, the way `a4a512de` stamped `2661b66b`. The commit message carries one line of the shape
`manifest-audit: delta 1 qualification — <what moved>`.

### The version carriers, derived

Both populations are DERIVED by `git grep -l` and the figures below are what that printed on
2026-09-13 at `e3d0f68c`; AC7 and AC11 re-derive them.

| kit | constant | carriers of the marker today | count |
|---|---|---|---|
| memory-tree `2.74` → `2.75` | `check-memory-hygiene.sh:20` | the four `tools/memory-tree/*.template.md`, their renders `memory/HYGIENE.md`, `memory/TEMPLATE-SPEC.md`, `memory/guides/BUILD-METHOD.md`, `memory/guides/ANNOTATION-STYLE.md`, and the constant's own line | 9 |
| unattended `1.19` → `1.20` | `unattended.sh:42` | `unattended.sh`, `check-unattended.sh:40`, `check-pass-order.sh:38`, `check-brief-recorded.sh:49`, the five `tools/unattended/*.template.md`, `tools/unattended/README.md`, `tools/unattended/playbook.fixture.md`, and the renders `.claude/skills/unattended/SKILL.md`, `memory/guides/PLAYBOOK-TEMPLATE.md`, `memory/guides/UNATTENDED-PROTOCOL.md`, `memory/guides/UNATTENDED-VERBS.md` | 15 |

`check-kit-versions.sh:143` demands that EVERY tracked `tools/memory-tree/*.template.md` carry the
constant's value and `:185` the same of `tools/unattended/*.template.md`, and `kit/dogfood doc parity`
plus `adopt-unattended.sh --check` byte-compare the renders to the templates. So a bump is all
carriers or none, and the marker-only edits are the price of the two rule-bearing ones.
`tools/unattended/README.md` is graded by neither and moves because a stale README marker is the
hole `TOOL-cFinalBerth-3` recorded one file over.

### Data model

N/A — five prose carriers and two version constants; no schema, no record shape, no conf key.

### Inventory

No identifier is minted. No new file, leg name, conf key, function or gate arm, so no codebase-map
inventory key is claimed and no naming cell grades anything here.

### Migration

None. An adopter who copy-installs either kit receives the new sentences on the next install and the
version constant tells them so; the previous wording is not read by any machine.

### Rollout

One commit, on the run's branch, in this order: the two workflow scripts, the method template and
its render with the memory-tree bump, the Skill template and its renders with the unattended bump,
the manifest line with its stamps, this spec's status flip to `CLOSED`. Nothing ships dark: every
sentence is inert until an agent reads it, and the version bumps are the rollout signal.

### Files touched (estimate)

| path | change |
|---|---|
| `tools/workflows/unattended-unit.js` | the ban and substitute sentence; line 44 to `1.1` in both tokens |
| `tools/workflows/unattended-build.js` | one `GROUND` sentence; one writer-prompt sentence; line 3 to `1.1` |
| `tools/memory-tree/BUILD-METHOD.template.md` | the M6 replacement; marker to `2.75` |
| `memory/guides/BUILD-METHOD.md` | rendered |
| `tools/memory-tree/check-memory-hygiene.sh` | line 20, constant and same-line marker to `2.75` |
| `tools/memory-tree/ANNOTATION-STYLE.template.md` · `HYGIENE.template.md` · `SPEC-TEMPLATE.template.md` | marker only |
| `memory/HYGIENE.md` · `memory/TEMPLATE-SPEC.md` · `memory/guides/ANNOTATION-STYLE.md` | re-rendered, marker only |
| `tools/unattended/SKILL.template.md` | the bullet; marker to `1.20` |
| `.claude/skills/unattended/SKILL.md` | rendered |
| `tools/unattended/unattended.sh` · `check-unattended.sh` · `check-pass-order.sh` · `check-brief-recorded.sh` | constant and same-line marker to `1.20` |
| `tools/unattended/PLAYBOOK-TEMPLATE.template.md` · `PROTOCOL.template.md` · `VERBS.template.md` · `playbook.fixture.template.md` · `README.md` | marker only |
| `memory/guides/PLAYBOOK-TEMPLATE.md` · `UNATTENDED-PROTOCOL.md` · `UNATTENDED-VERBS.md` · `tools/unattended/playbook.fixture.md` | re-copied, marker only |
| `memory/guides/SESSION-KICKOFF.md` | line 263 qualified; one duplicate traps bullet deleted for C7; `last-audit` and `last-body-change` re-stamped |
| this spec | status to `CLOSED` in the build commit |

Twenty-eight files: five carry a rule, twenty-two carry a marker, one is this record. The count is
DERIVED from the two `git grep -l` populations above plus the five carriers and this file.

### Alternatives rejected

- **The rule in the protocol instead of the method.** Rejected by the research record and §8's
  first resolved fork: the protocol is a contract at 3625 bytes of headroom, and M1 makes a rule
  stated in two carriers a defect in the method. The Skill bullet points at M6 for the same reason.
- **A per-stage sentence in each of the parent's four prompts.** Rejected by §8's third fork:
  `GROUND` prefixes all of them and the unit child through `cfg.ground`, so one sentence there
  reaches five prompts, and a per-stage copy is four spellings to keep in step.
- **Deleting M6's verification sentence rather than replacing it.** A pass with no stated
  verification is worse than one told to run the bar: the child then decides, and the corpus says
  what it decides.
- **Leaving the engine markers of the two workflow scripts at `1.0`.** They are ungraded, and
  `TOOL-aHoistedPass-6` left them alone on that ground. Moved here anyway because the brief asks and
  because the text an adopter receives changed; the cost is two tokens.

## 5. Production-readiness checklist

- security — N/A. Prose in five carriers and two version constants; no write path, no input, no
  egress.
- perf / scale — the direct observations in §6 are greps, a `sed` render, AC16's token pipeline
  over this one file, `wc`, and nine leg scripts run by hand — the eight names on the §7 line plus `spec tokens` in AC14, with AC15
  carrying the two the round-1 audit found unrun — each of which finished in under 84 s on the
  last recorded bar (`<git-dir>/gate-ledger.tsv`, re-read 2026-09-14; `memory hygiene` 83 s,
  `method carriers` 14 s, the rest under 20 s). The rule itself is what removes minutes-to-hours
  from every later unit.
- error / empty / loading states — a grep count of `0` where `1` is expected is the red state of
  every carrier criterion, and a `git grep -l` over the OLD marker that prints anything is the red
  state of both bumps; AC7 and AC11 assert the old marker is gone and the new one has the derived
  count, so an empty result cannot pass by absence.
- observability — each sentence is greppable by a phrase §4 pins, and the acceptance ledger quotes
  the line it found. The kit versions are what a deployer greps in an adopting tree.
- risks — each with its remedy. (1) The M6 replacement overruns M1's budget: measured at +471 bytes
  against 1209 of headroom, and AC6 runs the size checker; if a later fold pushes it over, trim
  elsewhere in M6, never raise the cap. (2) A watched-file edit without the re-stamp reds C5s at
  pre-commit and C5 on the bar: S5 stamps in the same commit. (3) A half-bumped kit reds
  `kit version markers`: AC7 and AC11 derive both populations and assert the old marker is absent.
  (4) The verdict-epoch gate demands the memory-tree bump come at or after the engine's last
  behaviour-bearing change: the constant line is that change and the bump is in the same commit, so
  W equals S; AC9 observes it. (5) A grep phrase split across a concatenation matches nothing: §4
  pins each phrase to one source line. (6) `tools/workflows/unattended-build.test.sh` is a 21-arm
  suite on no bar (`TOOL-dBriefedPass-7`); it asserts on return shape and `scriptPath`, not on
  `GROUND` text, so the sentence cannot break it, and it is not run here in any case.
- testing — every criterion is a direct check; no suite and no bar is run by the pass that builds
  this unit. The kit self-tests that exercise the four `.sh` files whose constant moves are
  `chunk: selftests` legs the main loop owes at `VERIFYING` under the build README's rule, and the
  child returns that need in `summary`.
- migration — none; see §4.
- user docs — none. Agent-facing carriers only, and each is its own documentation; the build README
  states the owner's three sentences the carriers implement.

## 6. Acceptance criteria

- **AC1** — When `grep -c 'RUN NO MERGE BAR AND NO SELF-TEST SUITE' tools/workflows/unattended-unit.js`
  runs, it prints `1`, and one grep per pinned form prints `1` each, because the five forms span
  three source lines the header grep never reads:
  `grep -c 'not run-gates.sh in any form' tools/workflows/unattended-unit.js`,
  `grep -cE 'GATE_(FULL|SELFTESTS)= prefix' tools/workflows/unattended-unit.js`,
  `grep -c 'not run-selftests.sh, not run-unattended-gates.sh' tools/workflows/unattended-unit.js`,
  `grep -cF '*.test.sh suite' tools/workflows/unattended-unit.js`.
  Red when: any of the five prints `0` — a form dropped, respelled, or split across a
  concatenation so that no single line carries it.
- **AC2** — When `grep -c 'name it in .summary. and the main loop' tools/workflows/unattended-unit.js`
  runs, it prints `1`: the `summary` rule and the hand-off to the main loop sit on one source line,
  and the phrase is the one that says "return it" rather than "run it later".
  Red when: it prints `0` — the substitute tells the child to run the criterion later, drops the
  `summary` rule, or splits it from the hand-off across a concatenation.
- **AC3** — When `grep -c 'No stage of this program runs the merge bar or a self-test suite' tools/workflows/unattended-build.js`
  runs, it prints `1`, and the match is inside the `GROUND` constant rather than a stage prompt.
  Red when: it prints `0`, or `2` or more because a stage prompt repeated it.
- **AC4** — When `grep -c 'names a DIRECT observation with its command' tools/workflows/unattended-build.js`
  runs, it prints `1`, inside the SPEC-stage writer prompt.
  Red when: it prints `0`, or the sentence claims a gate refuses the token.
- **AC5** — When `grep -c 'A pass runs no merge bar and no self-test suite' memory/guides/BUILD-METHOD.md`
  runs, it prints `1`, and `grep -c 'diff-scoped' memory/guides/BUILD-METHOD.md` prints `0`.
  Red when: either count is wrong, or the template carries the sentence and the render does not.
- **AC6** — When `sed -e 's#{{KIT_DIR}}#tools/memory-tree#g' -e 's#{{TOOL_ROOT}}#tools/#g' tools/memory-tree/BUILD-METHOD.template.md | diff - memory/guides/BUILD-METHOD.md`
  runs, it prints nothing; `bash tools/check-template-size.sh memory/guides/BUILD-METHOD.md`
  exits 0 with a byte figure at or under 27648; and `wc -l memory/guides/BUILD-METHOD.md` prints
  a count at or under 350, as its own observation, because the size checker grades bytes and
  reads no line figure (`tools/template-size-limits.txt` says so for this subject).
  Red when: the diff prints a hunk, the checker exits 1 on the budget, or `wc -l` prints 351 or
  more.
  figure: DERIVED at observation time by the checker and by `wc -l`; the 26910-byte and 341-line
  estimates in §4 are PINNED and are not the figures this criterion asserts.
- **AC7** — When `git grep -l 'gov:kit memory-tree@2.74' -- tools memory/HYGIENE.md memory/TEMPLATE-SPEC.md memory/guides`
  runs, it prints nothing, and the same command with `2.75` prints nine paths.
  Red when: any live carrier still spells `2.74`, or the count is not nine.
  figure: PINNED — nine, counted 2026-09-13 at `e3d0f68c` by the same `git grep -l` over `2.74`.
- **AC8** — When `grep -c "version: '1.1', // gov:kit unattended-unit@1.1" tools/workflows/unattended-unit.js`
  and `grep -c "version: '1.1', // gov:kit unattended-build@1.1" tools/workflows/unattended-build.js`
  run, each prints `1` — the whole line, so `meta.version` and the comment marker are read
  together and a half-moved line cannot pass — and
  `node tools/workflows/check-workflow-syntax.js tools/workflows/unattended-unit.js tools/workflows/unattended-build.js`
  exits 0.
  Red when: either prints `0`, which is an unmoved line or a half-moved one
  (`version: '1.0', // gov:kit unattended-unit@1.1`, or the reverse), or the syntax checker
  prints a file.
- **AC9** — When `bash tools/memory-tree/check-verdict-epoch.sh` runs after the build commit, it
  exits 0.
  Red when: it names `check-memory-hygiene.sh` as moved without a bump, which happens if the constant
  is bumped in an earlier commit than the one that edits the engine.
- **AC10** — When `grep -c 'No merge bar and no self-test suite inside a pass' tools/unattended/SKILL.template.md`
  and the same over `.claude/skills/unattended/SKILL.md` run, each prints `1`, and
  `bash tools/unattended/adopt-unattended.sh --check` exits 0.
  Red when: either count is `0`, or `--check` prints an out-of-sync diff.
- **AC11** — When `git grep -l 'gov:kit unattended@1.19' -- tools/unattended .claude/skills/unattended memory/guides`
  runs, it prints nothing, the same command with `1.20` prints fifteen paths, and
  `bash tools/check-kit-versions.sh` exits 0.
  Red when: any live carrier still spells `1.19`, the count is not fifteen, or the checker names a
  template whose marker disagrees with the constant.
  figure: PINNED — fifteen, counted 2026-09-13 at `e3d0f68c` by the same `git grep -l` over `1.19`.
- **AC12** — When `grep -c 'inside a build pass run each meta-gate' memory/guides/SESSION-KICKOFF.md`
  runs, it prints `1`, and `bash skills/session-kickoff/manifest-check.sh` exits 0.
  Red when: the count is `0`, C11 reports the bullet over 400 bytes, C7 reports the file over
  25600 bytes, or C5 reports a watched change with no re-stamp.
- **AC13** — When `git log -1 --format=%B | grep -c 'manifest-audit: delta'` runs at the build
  commit, it prints `1`, `grep -c "@ $(git merge-base origin/main HEAD)" memory/guides/SESSION-KICKOFF.md`
  prints `1`, and `grep -c "^last-body-change: $(git rev-parse HEAD~1)" memory/guides/SESSION-KICKOFF.md`
  prints `1` — the second stamp S5 owes, which `manifest-check.sh` grades only as non-empty and
  un-stalled, so nothing but this grep ties it to the body edit.
  Red when: the commit message carries no delta line, `last-audit` names a sha that is not the
  merge-base, or `last-body-change` still names `2661b66b`.
- **AC14** — When `python tools/check-spec-tokens.py` runs over the tree carrying this spec, it
  exits 0, and `python tools/check-spec-tokens.py --list` resolves every name on this spec's §7 leg
  line against `tools/gate-legs.json`.
  Red when: a §7 name resolves to no leg, or a §6 path-shaped token is untracked.
- **AC15** — When `bash tools/memory-tree/check-memory-hygiene.sh` and
  `bash tools/memory-tree/check-method-carriers.sh` run at the build commit, each exits 0: the
  hygiene engine caps the guide S3 grows, and the carriers checker's arm 5 reads the Skill bullet
  S4 adds. These are the two §7 names no other criterion runs, so without this bullet their first
  verdict on this unit's files would arrive at the close.
  Red when: either exits non-zero; the failing line that this unit can cause names
  `memory/guides/BUILD-METHOD.md` (the guide cap) or `.claude/skills/unattended/SKILL.md` (a
  `## M<n>` heading the bullet must not carry).
- **AC16** — When `sed -n '/^## 6\. Acceptance criteria/,/^## 7\./p' memory/builds/aDeferredBar/spec/2026-09-13-spec-TOOL-aDeferredBar-1.md | grep -oP '\x60[^\x60]+\x60' | tr -d '\140' | grep -cP '(?:^|&&|[;|(])\s*(?:\w+=\S*\s+)*(?:timeout\s+\S+\s+)?(?:bash\s+|sh\s+)?(?:\S*/)?(?:run-gates|run-selftests|run-unattended-gates|[^\s/*?]+\.test)\.sh(?=\s|$)|(?:^|\s)GATE_(?:FULL|SELFTESTS)=\S'`
  runs, it prints `0`: every backticked token of this file's acceptance section, one per line, run
  through unit 2's `BAR` regex typed verbatim from its §4, so `^` is the token start as the checker
  reads it and not a line start. It is a `grep -P`, not the `-E` the audit spelled, because ERE has
  neither `(?:` nor `(?=` and GNU grep 3.0 under `-E` printed `0` over a bar token rather than an
  error, probed 2026-09-14 — the could-not-fail shape this criterion exists to refuse. Liveness:
  `echo bash tools/run-gates/run-gates.sh | grep -cP '(?:^|&&|[;|(])\s*(?:\w+=\S*\s+)*(?:timeout\s+\S+\s+)?(?:bash\s+|sh\s+)?(?:\S*/)?(?:run-gates|run-selftests|run-unattended-gates|[^\s/*?]+\.test)\.sh(?=\s|$)|(?:^|\s)GATE_(?:FULL|SELFTESTS)=\S'`
  prints `1`, so the regex as typed can match, and a copy of this file with a runner token spliced
  into an AC bullet printed `1` on the same date. Heredoc-free, because the ledger cannot run one.
  Red when: the first command prints `1` or more — a §6 token became a bar or suite invocation —
  or the liveness command prints `0`, which is a regex typed wrong and never a clean section.

## 7. Gates

`build-method size` · `kit version markers` · `verdict epoch (kit version dates the engine)` · `unattended skill wiring` · `workflow script syntax` · `kickoff-manifest ratchet` · `memory hygiene` · `method carriers (every pointer declared)`

Each name resolved against `tools/gate-legs.json` with `python tools/check-spec-tokens.py --list`
on 2026-09-13 before this spec was returned. Every one is `subject: repo` and runs on an ordinary
bar; each is observed here by running its own script by hand, which is what §6 names, and the
bar itself is run once by the main loop after the last unit is terminal.

`kit/dogfood doc parity` also grades S3's template-to-render pair and is not on the line above
because its script is `*.test.sh`-named; AC6 observes the same parity with a `sed` render and a
`diff`, and the §3 edge to `TOOL-aDeferredBar-3` records why the name matters.

No `New arm:` line: this unit adds and moves no gate arm.

## 8. Open questions

All three forks were resolved by the research record before this spec was written, under the
mandate's delegated authority, and are marked here so the readers that grade this section see the
mark rather than the record.

- **Fork A — the carrier of the rule: protocol or method?** The protocol is the contract every
  directive points into and is what a resuming run re-reads; the method is the procedure and holds
  the pass loop the rule governs. Against the protocol: 3625 bytes of headroom under the guide cap,
  and M1's one-place rule.
  RESOLVED (agent, 2026-09-13, delegated): the method, M6. The protocol's marker moves with the
  kit bump and nothing else in it does.
- **Fork B — a leg-selection flag on the runner, so "scoped" has a spelling narrower than the
  bar?** For: a child could then run three legs by name. Against: the manifest guard already scopes
  a plain bar to the legs whose paths the branch touched, the runner's knob set has no leg filter
  today, and a flag is a new public surface on the bar — M3 veto 2.
  RESOLVED (agent, 2026-09-13, delegated): not built. The plain bar with no flag, at the main loop,
  is the scoped form; the build README states it as a build-level rule.
- **Fork C — one sentence in `GROUND`, or one per stage prompt?** Per-stage is four spellings of
  one rule in one file. `GROUND` prefixes every stage agent and travels to the unit child as
  `cfg.ground`.
  RESOLVED (agent, 2026-09-13, delegated): `GROUND`, once, plus the writer-prompt acceptance rule,
  which is a different sentence about a different reader.
- **Fork D — the round-1 audit's M2: a criterion for the two §7 legs no criterion ran, or delete
  the §7 claim that every leg is hand-run?** `memory hygiene` and `method carriers` sat on the §7
  line with no §6 bullet running either script, so the claim was false. Against deletion: those two
  legs read exactly the files S3 and S4 change, and a unit whose first verdict on its own files
  arrives at the close is the shape this build exists to remove. Against the criterion: nothing —
  both are direct scripts, 83 s and 14 s on the last recorded bar, and neither is a suite.
  RESOLVED (agent, 2026-09-14, delegated): the criterion, AC15; the §7 sentence stands as written
  and is now true.
- **Fork E — the round-2 audit's M7: a criterion for the bar-token absence S6 claims, or the S6
  probe sentence alone?** Unit 2's gate never grades this file — its cutoff sits past every spec
  date on any ref and `SPEC_DATE` reads the filename, so the "until unit 2 lands" hand check rev-2
  called temporary was the only observation there would ever be. Against the sentence alone: a
  claim with no command beside it is the shape this build's audits keep finding. Against the
  criterion: only its cost, one `grep -P` over one file.
  RESOLVED (agent, 2026-09-14, delegated): the criterion, AC16, in the heredoc-free one-line form
  the audit asked for; S6 and the §3 population bullet reworded so neither waits for a verdict
  that cannot arrive.

## 9. Revision log

- rev-1 · 2026-09-13 · initial draft, authored in the SPEC stage of the `aDeferredBar` run from the
  brief `prompts/2026-09-13-prompt-TOOL-aDeferredBar-1-1-spec-brief.md` and the research record.
- rev-2 · 2026-09-14 · S3 · S4 · S6 · §5 · §6 · §8 · AC1 · AC2 · AC6 · AC8 · AC15 · folded round 1 of the
  spec audit, `reviews/2026-09-14-review-TOOL-aDeferredBar-1-spec-audit-round1.md`: M2 adds AC15
  (the hygiene engine and the method-carriers checker each exit 0 at the build commit), which makes
  §7's hand-run claim true, recorded as Fork D in §8 and named by S3 and S4; M3 makes AC8 grep the
  whole `version:` line so a half-moved marker reds; M4 gives AC1 one grep per pinned form and AC2
  the `summary` grep, so the red-whens the old header grep could not see are observable; M7 gives
  AC6 its own `wc -l` observation for the 350-line clause the size checker never reads. §5 perf
  counts nine hand-run leg scripts instead of seven; S6 records that AC1's grep arguments are not
  hits under unit 2's `BAR`.
- rev-3 · 2026-09-14 · S6 · §3 · §5 · §8 · AC13 · AC16 · folded round 2 of the spec audit,
  `reviews/2026-09-14-review-TOOL-aDeferredBar-1-spec-audit-round2.md`: M6 appends to AC13 the
  `last-body-change` grep against `HEAD~1`, so the second stamp S5 owes is observed rather than
  declared, with `2661b66b` named in its red-when; M7 rewords S6 and the §3 population bullet —
  this file is outside unit 2's population by that gate's cutoff, so the ledger check is the
  observation and not a stopgap, and no live spec is graded until one is dated at or after the
  cutoff — and adds AC16, unit 2's `BAR` regex typed from its §4 into one heredoc-free line over
  this file's acceptance tokens, printing `0`, with a liveness command printing `1`; recorded as
  Fork E in §8. AC16 is `grep -P` rather than the `-E` the audit spelled, because ERE has no
  `(?:` and printed `0` over a bar token when probed. §5 perf names the pipeline.
- rev-4 · 2026-09-14 · S5 · §4 · AC12 · the build pass: `manifest-check.sh` C7 redded at 25716
  bytes against its 25600-byte file cap once the S5 bullet was written, a cap rev-3 priced only
  per bullet (C11). C7 says trim and never raise, so the traps bullet restating the retired
  read-path budget (`TOOL-dSpentCeiling-1`, still recorded in §B) is deleted, 271 bytes, and S5,
  the §4 carrier-5 paragraph, the files table and AC12's red-when record it. Status to CLOSED in
  the build commit.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "tell a build agent not to run the merge bar or a
self-test suite inside a unit pass"` returned name-stem neighbours only — `run`, `build_*`,
`test_*` — and printed `unscanned layers: .sh`, so it is blind to the shell half of this write set
and names no seam for an instruction carrier. No existing seam fits as a MECHANISM, and the
evidence is the chain in §4: the instruction has no carrier today, and the seams this unit extends
are the five carriers themselves — `GROUND` at `unattended-build.js:335`, `PROMPT` at
`unattended-unit.js:144`, M6 of the method template, the "While it runs" list of the Skill
template, and the manifest's traps section — each an existing text the rule is added to rather
than a new file. The recall probe's hits [6], [8] and [12] are three earlier briefs under
`memory/builds/aHoistedPass/prompts/` that each re-derived "do not run the full bar" for one unit,
which is the per-brief re-derivation this unit retires by stating the rule once at each carrier.
Verified against source where a hit could be stale: the research record's line numbers for
`GROUND` and the M6 sentence still hold at `e3d0f68c`; its claim that `run-gates.sh` has no leg
filter was re-read in `tools/run-gates/run-gates.sh`'s knob set and holds.

Recall terms used: `python tools/memory-recall/query.py "where is a build agent told to run the
merge bar or a self-test suite inside a unit pass, and which carrier states the per-pass
verification rule" --terms "unattended unit pass full bar run-gates GATE_SELFTESTS GATE_FULL
self-test diff-scoped push boundary stall wall-clock child prompt carrier"`.
