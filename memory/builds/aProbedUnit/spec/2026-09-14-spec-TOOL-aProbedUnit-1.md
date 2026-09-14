# TOOL-aProbedUnit-1 — no gate, suite or bar runs inside a unit pass; the bar runs once, at the close

**Status:** SPECCED · rev-1 · 2026-09-14 · node a · Tier-2 · base 1b000d1a · streams tooling · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-14-prompt-TOOL-aProbedUnit-1-0-run-mandate.md](../prompts/2026-09-14-prompt-TOOL-aProbedUnit-1-0-run-mandate.md) | journal | — |
| [2026-09-14-prompt-TOOL-aProbedUnit-1-1-spec-briefs.md](../prompts/2026-09-14-prompt-TOOL-aProbedUnit-1-1-spec-briefs.md) | journal | TOOL-aProbedUnit-2 TOOL-aProbedUnit-3 TOOL-aProbedUnit-4 TOOL-aProbedUnit-5 TOOL-aProbedUnit-6 TOOL-aProbedUnit-7 |
| [2026-09-14-review-TOOL-aProbedUnit-1-spec-audit-round1.md](../reviews/2026-09-14-review-TOOL-aProbedUnit-1-spec-audit-round1.md) | spec-audit | TOOL-aProbedUnit-2 TOOL-aProbedUnit-3 TOOL-aProbedUnit-4 TOOL-aProbedUnit-5 TOOL-aProbedUnit-6 TOOL-aProbedUnit-7 |

<!-- /gen:spec-records -->

## 1. Goal

A harnessed unit agent reads its spec's section 7 and template §1's "gates green" and runs the merge
bar, self-test suites included, inside its pass: one pass ran five hours stacking suites
(`memory/builds/aRatifiedRulings/README.md`, build-level rules, owner 2026-09-13) and another
twelve hours on node `d`. The owner's rule in `memory/builds/aProbedUnit/prompts/2026-09-14-prompt-TOOL-aProbedUnit-1-0-run-mandate.md`
is that in one session the gates run ONCE, pre-merge, when every finding is fixed. That rule has
lived only in build briefs and one build README's rules slot, and a sidechain child reads neither.
This unit puts it in the four carriers a child and a spec writer actually read: the child prompt in
`tools/workflows/unattended-unit.js`, the parent's `GROUND` preamble, M6 of the build method, and
the unattended Skill's harness bullet. The pass then verifies with the one check that exercises its
change, and the bar is `--close`'s.

## 2. Scope (IN)

- **S1** — The child `PROMPT` in `tools/workflows/unattended-unit.js` gains one binding paragraph,
  placed after `DRIVER_STEPS` and before the commit sentence, with the text section 4 pins: no gate,
  suite or bar runs inside the pass; verify with the single smallest check that exercises the
  change; say in `summary` which check ran and which gate it stands in for; a section 7 or a brief
  that says otherwise is overridden. It spells no path. Observed by AC1 and AC6.
- **S2** — `GROUND` in `tools/workflows/unattended-build.template.js` gains one sentence, in both
  modes, after the mode ternary: a unit pass runs no gate, suite or bar, the bar runs ONCE at the
  close, so a spec's section 7 lists what the close runs and a pass verifies with the one check
  that exercises its change. The render `tools/workflows/unattended-build.js` is re-made by
  `bash tools/workflows/check-protocol-parity.test.sh --render` in the same commit. Observed by
  AC2 and AC3.
- **S3** — M6 of `tools/memory-tree/BUILD-METHOD.template.md`: the sentence pair "Then the
  diff-scoped gates for what the pass touched; the full bar runs ONCE, at the push boundary. A pass
  whose gate is red is not followed by another: fix it, or park it with the reason." becomes the
  text section 4 pins, within M1's byte and line budget. The render `memory/guides/BUILD-METHOD.md`
  is re-made by `bash tools/memory-tree/kit-dogfood-parity.test.sh --render` in the same commit.
  Observed by AC4 and AC5.
- **S4** — The "Drive the build as ONE program" bullet of `tools/unattended/SKILL.template.md`
  gains one sentence after "the method is what tells it what a pass is": the child is ordered to
  run no gate, suite or bar inside its pass, the bar is `--close`'s, once, and the child verifies
  with the one check that exercises its change. The render `.claude/skills/unattended/SKILL.md` is
  re-made by `bash tools/unattended/adopt-unattended.sh` in the same commit. Observed by AC7.
- **S5** — One `has` arm in `tools/workflows/unattended-build.test.sh`, beside the existing `F2`
  child-prompt arms, asserting the traced unattended child prompt carries the paragraph's opening
  phrase. Observed by AC6.
- **S6** — The obligations the method edit incurs, in the same commit: `memory/guides/BUILD-METHOD.md`
  is on the kickoff manifest's watch list, so `last-audit` in `memory/guides/SESSION-KICKOFF.md`
  is re-stamped with a delta line in the commit message; this spec's status header goes to CLOSED;
  the acceptance ledger is written under the build folder per `memory/HYGIENE.md`, "Acceptance
  ledger". Observed by AC8.

## 3. Non-goals (OUT)

- **No kit version moves.** Unattended 1.21, memory-tree 2.75 and the two workflow engine markers
  stay where they are; the closing pass bumps once per kit, per the build README's rules slot.
- **The child's return schema does not change.** `UNIT_SCHEMA` keeps its four required keys; the
  check that ran and the gate it stands in for are prose in `summary`, which the schema already
  requires.
- **No new directive, no new registry row.** `DIRECTIVES_CORE` in `tools/unattended/unattended.sh`
  is untouched; `passes-committed:M6` already points at the section this unit edits, and check 16
  arm B resolves the heading, not the sentence.
- **What the bar contains does not change.** `tools/gate-legs.json`, `--close`, `GATE_BOUND` and the
  push boundary's decision are as they were. This unit moves WHEN the bar runs relative to a pass,
  never what it runs.
- **The command bound is `TOOL-aProbedUnit-2`.** A pass that stalls on one unbounded command is not
  closed here; this unit closes the pass that stalls on a suite it was told to run.
- **No dossier edit.** `memory/map/features/unattended.md` claims `unattended-unit.js` and measures
  20470 bytes against a 20480-byte `DOSSIER_CAP_BYTES`; it describes the kit's gates and refusals,
  and a prompt paragraph is neither. The method is the carrier of the rule and M6 is where a
  reader finds it.
- **The attended-mode texts are untouched.** The new paragraph is mode-independent and sits outside
  the `DRIVER_STEPS` ternary; neither branch of that ternary changes.
- **The frozen record is not edited.** The 2026-09-13 rule in `memory/builds/aRatifiedRulings/README.md`
  says a pass runs the fast diff-scoped gates; this unit tightens it to none, and the record stands
  as written because a landed record is not rewritten.
- **No `--bump` of the high-water.** Section 4 measures the render at 95 bytes under the recorded
  high-water after this edit. Units 6 and 7 edit M4 after this unit lands; whether the three edits
  together cross 26941 is theirs to measure, and the WARN is advisory.

### Edges

- **hands-off** `TOOL-aProbedUnit-2` — the second child paragraph and the second clause of the Skill
  sentence, both positioned after this unit's text; that unit edits the same two files and the same
  bullet, so it is sequenced after this one and its grep anchors are this unit's lines.
- **hands-off** external — the kit version bumps across every carrier, once per kit, at the closing
  pass; and any `--bump` of `tools/template-size-highwater.txt` the closing pass finds owed once M4's
  two edits have landed beside this one.
- **consumes-from** external — the render direction of the three parity legs, template to live and
  never the reverse: `tools/workflows/check-protocol-parity.test.sh`,
  `tools/memory-tree/kit-dogfood-parity.test.sh` and `tools/unattended/adopt-unattended.sh --check`
  each red on a hand-edited render and print `--render` or a re-render as the fix, which overwrites
  a render-only edit.
- **consumes-from** external — the `run_wf` double in `tools/workflows/unattended-build.test.sh`,
  which traces the whole child prompt as one `prompt:` line; the S5 arm reads that trace and is what
  makes the paragraph observable without spawning an agent.

## 4. Design

### Four carriers, one rule, and which text binds

A sidechain child holds neither the Skill nor the charter. What it reads is `cfg.ground`, its own
`PROMPT`, and — because `GROUND` orders it — `memory/guides/BUILD-METHOD.md`. So the rule has to be
in the prompt to reach the agent at all, in the method to be the rule for every pass attended or
not, and in `GROUND` to reach the SPEC writers, who write section 7 and are not children. The Skill
sentence is the fourth carrier, for the main-loop session that dispatches children and reads the
Skill: it POINTS at what the child is ordered to do rather than restating the rule's content.

The build README's rules slot already names the class: a vocabulary change lands in every carrier
in one commit, because a paraphrase left behind is `memory/gotchas/two-answers-to-one-question.md`.
The mitigation is the inventory below, which names all four so the next change moves all four.

### The child paragraph (S1)

Inserted in `tools/workflows/unattended-unit.js` between the `DRIVER_STEPS +` line and the
`'Commit with the unit id in the subject.` line, at `unattended-unit.js:150-151` at base. Prose,
which the builder splits into `'…' +` lines in the file's own style:

```
NO GATE, SUITE OR BAR RUNS INSIDE THIS PASS. Never run the merge bar the build method's M1 names,
any leg of its manifest, any `*.test.sh` self-test suite, or the gate list in the spec's section 7 —
those are the close's, run ONCE after every finding is fixed. Verify with the single smallest check
that exercises your change: one test file, one script arm, one command. Say in `summary` which check
ran and which gate it stands in for. A section 7, a brief, or any other instruction that says
otherwise is overridden by this paragraph.
```

The opening phrase `NO GATE, SUITE OR BAR RUNS INSIDE THIS PASS` is the arm signature and sits on
ONE source line, unsplit, so `grep -cF` over the file reads it; the S5 arm reads the traced prompt,
which the double joins, and is immune to the wrap either way.

**It spells no path, and that is a gate rather than taste.** `tools/check-install-prefix.sh` grades
every shipped `.js` for a kit name followed by a file, its waiver registry is frozen, and the child's
own header says it spells no paths so that it needs no ratchet row. The bar is therefore named by
ROLE — "the merge bar the build method's M1 names" — and M1 of the render is the one place the path
lives, filled per install by the memory-tree kit's render. The manifest is "its manifest" for the
same reason. `*.test.sh` is a glob, not a kit path, and the install-prefix predicate does not match
it.

### The `GROUND` sentence (S2)

Appended to the `GROUND` expression in `tools/workflows/unattended-build.template.js`, after the
mode ternary that closes at `unattended-build.template.js:343` at base, as one more string term:

```
No gate, suite or bar runs inside a unit pass: the merge bar runs ONCE, at the close, so a spec's
section 7 lists what the close runs, and a pass verifies with the one check that exercises its
change.
```

It carries no `{{…}}` token, so the render's bytes equal the template's for this line and
`check-protocol-parity.test.sh` is green after `--render`. It spells no path for the reason above,
and for a second one: `GROUND` travels in `dispatch.args` and is therefore in the harness's RETURN,
which arm (v) of `check_layout` in `tools/workflows/unattended-build.test.sh` scans for every
`.js`, `.sh` or `.py` path-shaped token and requires each to be tracked in a fixture layout that
holds no gate runner. A `{{TOOL_ROOT}}run-gates/run-gates.sh` here would red that arm in all four
layouts.

The method-carriers registry row for both harness files reads "It states no rule the method does
not." That stays true because S3 lands in the same commit: the sentence is the method's own M6 rule
in the harness's words.

### The M6 sentence (S3)

The method is a RENDER: `tools/memory-tree/BUILD-METHOD.template.md` is the source, and
`memory/guides/BUILD-METHOD.md` is re-made from it by the `render_doc` block of
`tools/memory-tree/kit-dogfood-parity.test.sh`, whose `kit/dogfood doc parity` leg diffs the two and
prints `--render` as its fix — which OVERWRITES a render-only edit. Edit the template, render, commit
both.

At base the M6 paragraph that opens `**It takes a COMMITTED range` ends, at
`BUILD-METHOD.template.md:184-186`, with:

```
Then the diff-scoped
gates for what the pass touched; the full bar runs ONCE, at the push boundary. A pass whose gate is red is not
followed by another: fix it, or park it with the reason.
```

It becomes, in the template's own wrap style:

```
No gate, suite or bar runs
inside a pass — the full bar runs ONCE, at the close (`--close` under a mandate, the push boundary otherwise);
a pass verifies with the ONE check that exercises its change. A pass whose check is red is not followed by
another: fix it, or park it with the reason.
```

The sentence after it, "A pass that produced no change commits nothing and says so.", is unchanged.

**The bytes.** Measured on 2026-09-14 at base `1b000d1a` with Python over the bytes of both files,
LF throughout:

| File | Bytes at base | Lines | Bytes after | Lines after |
|---|---|---|---|---|
| `memory/guides/BUILD-METHOD.md` (the gated render) | 26743 | 340 | 26846 | 341 |
| `tools/memory-tree/BUILD-METHOD.template.md` (the source) | 26768 | 340 | 26871 | 341 |

The replacement is 291 bytes for 188, a growth of 103. M1 declares `≤27648 bytes, ≤350 lines`
and says the byte half binds first: the render lands 802 bytes and 9 lines under it, and 95 bytes
under the 26941 recorded in `tools/template-size-highwater.txt`, so the `build-method size` leg
prints no `TEMPLATE-SIZE WARN` and no `--bump` is owed by this unit. The figures are PINNED at that
date; AC5 derives the real ones. The widest changed line is 112 characters, inside M6's existing
116.

Why "at the close" carries a parenthesis. The method is "binding for any build of more than one
pass, attended or not" (M1), and `--close` is an unattended verb. An attended build has no close
verb and its bar binds at the push boundary, which is what the sentence said before. Naming both
keeps the method true in both modes and costs 51 of the 103 bytes; section 8 F1 records the choice.

Why the diff-scoped clause goes rather than shrinks. The owner's rule is "gates run ONCE"; the
2026-09-13 ruling allowed a pass "the fast diff-scoped gates and NOTHING held", and the mandate's
orientation records that this prompt tightens it: not even diff-scoped. A sentence that kept a
diff-scoped run beside "no gate runs" would be two answers in one paragraph.

What the child paragraph and M6 do not contradict. Template §1's Definition of Done says "gates
green" of a WORK-UNIT that lands on `main`; under the method a pass is finer than that unit and the
build's DoD is met by the bar at the close, once, before the lander. Template §8's "a check that
exercises THIS change" is the verification rule the pass now follows rather than a second one.

### The Skill sentence (S4)

In the "Drive the build as ONE program" bullet of `tools/unattended/SKILL.template.md`, whose body
opens at `SKILL.template.md:557` at base, inserted after the sentence ending "the method is what
tells it what a pass is." and before the blank line that precedes "Between dispatches":

```
**The child is ordered to run no gate, suite or bar inside its pass** — the bar is `--close`'s,
once, after every finding is fixed — and to verify with the one check that exercises its change.
```

No token, so the render `.claude/skills/unattended/SKILL.md` carries the same bytes; the
`unattended skill wiring` leg renders to a temp file and diffs, so a template edit without the
re-render reds it and a render-only edit reds it the other way. `bash tools/unattended/adopt-unattended.sh`
with no argument writes the render. Unit 2 appends a clause to this sentence, which is why the
sentence ends at a full stop the next unit can move.

### The arm (S5)

`tools/workflows/unattended-build.test.sh` already runs the child through `run_wf` with fixture
`CHILD_ARGS` at `unattended-build.test.sh:551-553` and greps the traced prompt with `has` for the
`F2` phrases. One line after those arms:

```
has "aProbedUnit-1 the child prompt forbids a gate, suite or bar inside the pass" "$childU" "NO GATE, SUITE OR BAR RUNS INSIDE THIS PASS"
```

`has` is positive by construction and counts itself in `n`; the suite prints `--- <n> arms` and
carries no floor, so nothing shrinks. The arm's failing case is the base child, which the probe in
section 10 already ran: the traced prompt at base holds the phrase zero times.

### Inventory

No identifier is minted: no function, no leg, no conf key, no file, no directive, no schema key.
The lexicon has nothing to grade; the child keeps exactly one top-level definition, `check`, so the
codebase-map JS liveness floor reads it as before.

### Rollout

The pass declares, through `--dispatch --writes`, every path it writes: the four carrier sources
`tools/workflows/unattended-unit.js`, `tools/workflows/unattended-build.template.js`,
`tools/memory-tree/BUILD-METHOD.template.md` and `tools/unattended/SKILL.template.md`; the three
renders `tools/workflows/unattended-build.js`, `memory/guides/BUILD-METHOD.md` and
`.claude/skills/unattended/SKILL.md`; the arm's home `tools/workflows/unattended-build.test.sh`;
`memory/guides/SESSION-KICKOFF.md` for the `last-audit` line; this spec; the build README; the
generated `memory/LIVE.md` and `memory/ledger/2026-09.md`, which hygiene check 9 re-renders whenever
a spec header moves; and its acceptance ledger under the build folder, declared by file.

The pass is SEQUENTIAL with unit 2, which writes three of the same files, and the roster's `order`
values already sequence them; nothing here derives an order. The one check the pass verifies with
is AC6's double, seconds, and nothing else runs inside it: not the parity legs, which are `--close`'s
and AC2, AC4 and AC7 name them for the close; not the harness suite whole.

Landing owes no data step. A run-state file, a spec or a brief written before this unit reads
identically after it; the only reader of the new text is an agent.

### Files touched (estimate)

| File | Change |
|---|---|
| `tools/workflows/unattended-unit.js` | one paragraph added to `PROMPT`, no path, no new definition |
| `tools/workflows/unattended-build.template.js` | one sentence appended to `GROUND` |
| `tools/workflows/unattended-build.js` | re-rendered from the template |
| `tools/memory-tree/BUILD-METHOD.template.md` | M6: 188 bytes out, 291 in, one line added |
| `memory/guides/BUILD-METHOD.md` | re-rendered from the template |
| `tools/unattended/SKILL.template.md` | one sentence added to the harness bullet |
| `.claude/skills/unattended/SKILL.md` | re-rendered from the template |
| `tools/workflows/unattended-build.test.sh` | one `has` arm beside the `F2` child arms |
| `memory/guides/SESSION-KICKOFF.md` | `last-audit` re-stamped, sha per the manifest's stamp rule |
| the acceptance ledger under `memory/builds/aProbedUnit/` | one row per criterion, declared by file |

### Alternatives rejected

- **Spell the bar's path in the child, `tools/run-gates/run-gates.sh`.** An install-prefix hit in a
  shipped `.js` with a frozen waiver registry, and a path that names nothing in an adopter installed
  at another prefix. M1 already holds the path, once, per install.
- **Spell it in `GROUND` as `{{TOOL_ROOT}}run-gates/run-gates.sh`.** Renders correctly, then reds
  arm (v) of the harness suite in every fixture layout, none of which holds a gate runner.
- **Put the rule only in M6 and have the child read the method.** The child already is told to read
  it, and the two stalls happened under a method that said "diff-scoped gates for what the pass
  touched"; the binding text has to be in the prompt the agent is executing, or a section 7 list
  outranks a sentence it read an hour ago.
- **Keep "diff-scoped gates" and add "never a suite".** The owner's word is ONCE; a pass that runs
  some gates is the state the 2026-09-13 ruling already allowed and the 12-hour stall still happened
  under.
- **A `skipped` or `verifiedBy` key in `UNIT_SCHEMA`.** A schema change is a contract change, and
  no reader of the key exists; `summary` is required already and the parent copies it through.
- **Trim M6 elsewhere to make the edit byte-neutral.** 95 bytes of headroom remain under the
  high-water and the WARN is advisory; a trim of prose other carriers point at is a second change.

## 5. Production-readiness checklist

- security — N/A. Prompt and guide text; no write path, no input boundary, no new surface.
- perf / scale — the method grows by 103 bytes against M7's whole-file re-read, 802 under the cap.
  The prompt grows by one paragraph per child spawn. The bar itself is unchanged; what falls is the
  pass-time cost that motivated the unit, from a suite stack to one check.
- error / empty / loading states — a child that cannot find a single check that exercises its
  change says so in `summary`; the paragraph tells it what to say and the schema already requires
  the field. The refusal shape of the harness is untouched.
- observability — THE COST STATED PLAINLY: a pass that ran no gate leaves no gate log under
  `<git-dir>/gate-logs/` for that pass, and the first bar over the whole build is the close's. A
  defect a per-pass diff-scoped run would have caught early is now caught at the close, later,
  which the owner priced against twelve-hour stalls and took. The check that ran is prose in the
  child's `summary`, not a key; the alternative is rejected above.
- risks — the same rule now lives in four carriers, which is the two-answers class; the inventory
  names all four and the build-level rule moves them together. A child under an old brief that
  names a suite is told the paragraph overrides the brief. A hand-edited render is erased by the
  parity leg's printed fix, named in section 4.
- testing — one `has` arm on the traced child prompt, its failing case the base file, observed by
  the section 10 probe as a zero count before the edit. The suite it lives in is on no bar and no
  budget row, so its whole-run cost is unmeasured here and AC6 names the one-arm invocation.
- migration — N/A. No row grammar, conf key or record format changes.
- user docs — the method and the Skill ARE the documents and both carry the sentence; the
  workflows README describes the render pairs, not the prompt text, and does not move.

## 6. Acceptance criteria

- **AC1** — When `grep -cF "NO GATE, SUITE OR BAR RUNS INSIDE THIS PASS" tools/workflows/unattended-unit.js`
  runs at the landed tip, it prints `1`, and `bash tools/check-install-prefix.sh` exits 0 with no
  hit naming that file.
  Red when: the count is `0`, or `2` because the phrase was duplicated into a comment; or the
  install-prefix leg names `unattended-unit.js`, which means the paragraph spelled a kit path.
- **AC2** — When `grep -cF "No gate, suite or bar runs inside a unit pass" tools/workflows/unattended-build.template.js`
  and the same grep over `tools/workflows/unattended-build.js` run at the landed tip, each prints
  `1`.
  Red when: either prints `0`; the render at `0` with the template at `1` is the render-only or
  template-only edit the parity leg reds.
- **AC3** — When `bash tools/workflows/check-protocol-parity.test.sh` runs at the landed tip, it
  prints `protocol-parity: in parity — 2 rendered pair(s) match their templates` and exits 0.
  Red when: it prints a drift line naming `unattended-build.js`, which is a template edit without
  `--render` or a render edited by hand.
  figure: the pair count is DERIVED by the leg from its `PAIRS` line; `2` is what it printed at base
  on 2026-09-14.
- **AC4** — When `grep -cF "No gate, suite or bar runs" memory/guides/BUILD-METHOD.md` and the same
  grep over `tools/memory-tree/BUILD-METHOD.template.md` run at the landed tip, each prints `1`,
  `grep -cF "Then the diff-scoped" memory/guides/BUILD-METHOD.md` prints `0`, and
  `bash tools/memory-tree/kit-dogfood-parity.test.sh` prints `shipped and installed docs agree`.
  Red when: the new phrase counts `0` in either file; the old phrase survives, which is two answers
  in one section; or the parity leg prints `DRIFT`, whose printed fix erases a render-only edit.
- **AC5** — When `bash tools/check-template-size.sh memory/guides/BUILD-METHOD.md` runs at the
  landed tip, it prints `template-size OK` with a byte figure at or below 27648 and prints no
  `TEMPLATE-SIZE WARN` line, and `wc -l < memory/guides/BUILD-METHOD.md` prints at most 350.
  Red when: the render passes 27648, which is `fail 2`; passes 26941, which prints the WARN this
  spec says is not owed; or the line count passes 350, which only this criterion reads.
  figure: both bounds are DERIVED at observation from `tools/template-size-limits.txt` and
  `tools/template-size-highwater.txt`; the 26846 and 341 in section 4 are PINNED from the staged
  measurement of 2026-09-14.
- **AC6** — When the child is run through the `run_wf` double of
  `tools/workflows/unattended-build.test.sh` with its `CHILD_ARGS` fixture in `unattended` mode and
  the output is piped through `grep -c "NO GATE, SUITE OR BAR RUNS INSIDE THIS PASS"`, it prints `1`
  at the landed tip and `0` against the base child; and the new `has` arm reads `ok` on the landed
  child. This is the ONE check the pass verifies with.
  Red when: the landed count is `0`, meaning the paragraph is in the file but not in the prompt the
  agent receives — a comment, or a string term outside `PROMPT`; or the base count is not `0`,
  meaning the arm cannot fail.
  cost: seconds — one `node -e` evaluation with stub hooks, no agent spawned.
  fixture: the double is a function inside the suite; run it by sourcing the suite's `run_wf`
  definition and `CHILD_ARGS` into a shell, or by copying the `node -e` body, which is what the
  section 10 probe did at base. Never the suite whole inside the pass.
- **AC7** — When `grep -cF "ordered to run no gate, suite or bar inside its pass" tools/unattended/SKILL.template.md`
  and the same grep over `.claude/skills/unattended/SKILL.md` run at the landed tip, each prints `1`,
  and `bash tools/unattended/adopt-unattended.sh --check` prints `unattended: in sync` and exits 0.
  Red when: either count is `0`; or the wiring leg reports drift, which is the template edited
  without `bash tools/unattended/adopt-unattended.sh` re-rendering, or the reverse.
- **AC8** — When `bash skills/session-kickoff/manifest-check.sh` runs at the landed tip, its check 5
  reports no watched file changed since `last-audit`, because the commit that edits
  `memory/guides/BUILD-METHOD.md` re-stamps `last-audit` in `memory/guides/SESSION-KICKOFF.md` in the
  same commit with a delta line in its message; and `git grep -lE '^\*\*Status:\*\* CLOSED' -- memory/builds/aProbedUnit/spec/`
  lists this spec.
  Red when: check 5 names `memory/guides/BUILD-METHOD.md` as changed after the stamp, which is the
  render landing without the bundle; or the spec header still reads `SPECCED`, which leaves the
  driver's `--plan` naming this unit again.

## 7. Gates

`review-protocol parity (kit vs dogfood)` · `workflow script syntax` · `unattended skill wiring` · `kit/dogfood doc parity` · `build-method size` · `method carriers (every pointer declared)` · `install-prefix (shipped surface)` · `kickoff-manifest ratchet` · `codebase-map coverage + freshness` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

These are `--close`'s. The pass runs NONE of them: it verifies with AC6's double alone, which is the
rule this unit writes, and the bar runs once at the close after every unit has landed. Chunks read
from `tools/gate-legs.json` on 2026-09-14: the two parity legs, `method carriers`, `codebase-map
coverage + freshness` and `spec tokens` are `chunk: declarations`; `workflow script syntax` and
`unattended skill wiring` are `chunk: wiring`; `build-method size` and `install-prefix` are
`chunk: product`; `kickoff-manifest ratchet` and `memory hygiene` are `chunk: records`. The
`kit/dogfood doc parity` leg is guarded on six paths including `memory/guides/BUILD-METHOD.md` and
`tools/memory-tree/`, which this diff touches, so a scoped bar cannot skip it. None is
`chunk: selftests`; the suite that holds the S5 arm is on no bar at all.

New arm: `tools/workflows/unattended-build.test.sh` · the base child traced through `run_wf`, whose
prompt holds the phrase zero times · no floor moves.

## 8. Open questions

- **F1 — does M6 say "at the close" alone, or name the attended point too?** The brief's words are
  "the bar runs ONCE at the close", and `--close` is an unattended verb, while M1 binds the method
  to attended builds as well. Option A, "at the close" alone: 52 bytes fewer, and an attended build
  reads a verb it does not have. Option B, "at the close (`--close` under a mandate, the push
  boundary otherwise)": the sentence stays true in both modes and keeps the push-boundary fact the
  old sentence carried. Recommendation: B.
  RESOLVED (agent, 2026-09-14, delegated): B. It satisfies every acceptance criterion the brief
  shapes, including AC4's grep, and A leaves the method contradicting M1's own scope line, which is
  the two-answers class inside one file. Veto 2 is not tripped: the carrier edit is the one the
  mandate names, and B adds 51 bytes to it under the same budget, 95 under the high-water. The mark
  is contestable at the spec audit.

## 9. Revision log

- rev-1 · 2026-09-14 · initial draft, from the brief in
  `memory/builds/aProbedUnit/prompts/2026-09-14-prompt-TOOL-aProbedUnit-1-1-spec-briefs.md` and
  the mandate's orientation.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "a unit pass never runs the merge bar or a self-test suite
inside itself; it verifies with the one check that exercises its change"`, run on 2026-09-14 at base
`1b000d1a`, reported `scan coverage: 71 files scanned | 0 parse skips | unscanned layers: .sh`. Its
ranked candidates are `run` and `check` by name-stem fan-in, and the one real hit among them is
`check` in `tools/workflows/unattended-unit.js` itself — the child's single definition, which this
unit keeps as the file's only one. The map is BLIND to the `.sh` Skill adopter and to Markdown, so
no claim about those carriers rests on it.

The seams were found by reading source and all four EXIST: the `PROMPT` string in
`tools/workflows/unattended-unit.js`, the `GROUND` expression in
`tools/workflows/unattended-build.template.js`, the M6 paragraph in
`tools/memory-tree/BUILD-METHOD.template.md`, and the "Drive the build as ONE program" bullet in
`tools/unattended/SKILL.template.md`; each is extended in place and none is duplicated. The test
seam is the `run_wf` double and the `F2` child arms in `tools/workflows/unattended-build.test.sh`,
and the section 4 arm mints nothing. The double was run against the base child on 2026-09-14 and
the phrase count read `0`, which is the arm's failing case observed before it exists.

The recall probe's live hits were the 2026-09-13 rule in `memory/builds/aRatifiedRulings/README.md`
("no self-test, no held leg, no bar inside a pass; the full bar is close's and the push boundary's")
and two build briefs under `aRatifiedRulings` and `aHoistedPass` saying the same to one unit each —
which is the finding: the rule existed only in records a sidechain child never reads. Where a hit was
STALE against source: `TOOL-aTimedTurnstile-2` describes a bar of 47 legs with one guard, and
`tools/gate-legs.json` at base carries guards on most self-test legs; nothing here rests on that
row.

Recall terms used: `python tools/memory-recall/query.py "what carrier tells a harnessed unit agent
which gates run inside its pass, and why do unit passes stall on the merge bar and self-test suites"
--terms "unit pass gates merge bar full bar push boundary diff-scoped run-gates unattended-unit
stall suite self-test close"`.
