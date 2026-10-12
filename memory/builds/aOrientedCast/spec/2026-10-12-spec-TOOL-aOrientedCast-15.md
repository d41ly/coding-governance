# TOOL-aOrientedCast-15 — the closing review's minors: oracles that rot, readers that disagree, a verdict over a broken index

**Status:** OPEN · rev-1 · 2026-10-12 · node a · Tier-2 · base 646d4a73 · streams tooling · order 15 · ratified 2026-10-12

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-12-prompt-TOOL-aOrientedCast-12-1-spec-brief.md](../prompts/2026-10-12-prompt-TOOL-aOrientedCast-12-1-spec-brief.md) | journal | TOOL-aOrientedCast-12 TOOL-aOrientedCast-13 TOOL-aOrientedCast-14 |

<!-- /gen:spec-records -->

## 1. Goal

This unit closes review items M4, M5, L1, L2 and L3 of
[the closing review, round 1](../reviews/2026-10-12-review-TOOL-aOrientedCast-1-closing-diff-round1.md),
batched into one unit as BUILD-METHOD M4 orders for the medium and low findings of an exit. Each
item is a second answer to one question: a test oracle read from a commit the harness has moved past,
a renderer whose agreement with the spawn guard nothing runs and whose labels are typed beside their
source, two parsers of one card field and of one conf key, and a wiring verdict that says ok over an
index every hook refuses. Its write set does not meet `TOOL-aOrientedCast-14`'s.

## 2. Scope (IN)

- **S1** — M4. In `tools/workflows/unattended-build.test.sh`, the OC4 untyped arms stop comparing
  with harnesses read out of `git show 646d4a73:…` (`:2596-2601`, and the three guarded `same` arms
  at `:2609-2612`, `:2665-2668` and `:2690-2693`). Three kinds of assertion stand in their place:
  each untyped-only span is present in the untyped output, each typed-only span is absent from it, and
  a run with no `roles` key prints the same prompts and result, byte for byte, as a run with
  `"roles":{}` under the current harness. §4 "The spans" lists them. Observed by AC1.
  **Readers:**
  by name: `tools/workflows/unattended-build.test.sh`, the only file spelling `OC_BASE`, `OC_BF`,
  `OC_BC` and `OC_PFX`.
  by value: the `run_wf` calls in `tools/workflows/unattended-build.test.sh` that take `OC_BF` or
  `OC_BC` as their harness, and the `OC_BASE` tests guarding them.
- **S2** — M4's class enters the bug-class catalogue: a new `memory/gotchas/` record, kind `class`,
  for a test oracle read from a literal historical sha, which reds on every later legitimate edit of
  its subject; `memory/gotchas/INDEX.md` is regenerated. NOT OBSERVED by a criterion: a record,
  graded by the gotchas checks of the memory hygiene leg.
- **S3** — M5, the labels. `tools/roles/handoff.py` derives the eight task labels from the kickoff
  checker's `--task-skeleton` output, the checker it already locates through
  `resolve_kickoff_checker` (`:170-180`), parsing each skeleton field line by the same line grammar
  `extract_task_fields` applies to a card. `TASK_LABELS` (`:54-56`) gives way to `TASK_FIELDS`, the
  eight field keys alone in interface 6's order, zipped with the derived labels. A checker that
  cannot be resolved, exits non-zero, or yields a label count other than eight refuses, naming it.
  Observed by AC2.
  **Readers:**
  by name: `tools/roles/handoff.py`, the only file spelling `TASK_LABELS`.
  by value: `extract_task_fields` in `tools/roles/handoff.py`, which maps each card label to its
  field.
- **S4** — M5, the agreement arm. `tools/roles/adopt-roles.test.sh` gains arm 6: in its scaffolded
  fixture, `handoff.py render --part task` writes a `gov-researcher` prompt file under the fixture's
  build `prompts/` folder and prints its task part; that part, as an `Agent` payload's prompt, is
  admitted by the hooks kit's `agent-cap.js` with exit 0 and empty stderr; and `handoff.py check`
  over the file re-derives the marker's `task-sha`. The hooks kit is located through
  `roles_lib.resolve_kit_dir`, and the arm prints a `SKIP` line naming what is absent when the hooks
  kit or `node` cannot be found. Observed by AC3.
- **S5** — L1. `value()` in `skills/session-kickoff/manifest-check.sh` (`:1071-1081`) trims `r`
  after the paren strip and before its `:` test, as `extract_task_fields`'s `v.strip()` does at that
  step (`handoff.py:126-134`). Observed by AC4.
- **S6** — L2. `tools/roles/adopt-roles.sh` reads `MEMORY_ROOT` through `roles_lib.read_conf_key`,
  the call it already makes for `CHARTER` (`:168-171`), so its inline `resolve_python` block and the
  `PY` assignment move above the read at `:65`. `adopt-roles.test.sh` reads its `MR` and `CH` the
  same way (`:31-32`). Observed by AC5.
- **S7** — L3. In `check_roles` of `tools/check-wiring.sh`, an index the python read cannot parse
  (`:1584-1586`) reports `UNWIRED  roles     — .claude/roles.json does not parse as the role index;
  re-render it with bash <kit>/adopt-roles.sh --scaffold`, adds one to `unwired` and returns. The
  `note` stays only for a host with no usable python. Observed by AC6.

## 3. Non-goals (OUT)

- No edit of `tools/hooks/`: the agreement arm calls the hook, and the stale comment at
  `agent-cap.test.sh:2220` is `TOOL-aOrientedCast-14`'s to reword.
- No new function, shell or Python, anywhere in this write set, so the map's symbol index is not in
  it and `TOOL-aOrientedCast-14`, which regenerates that index, shares no file with this unit.
- No widening of a gate leg's `guard`. The arm sits in the roles adopter's self-test, whose leg runs
  unguarded, so a `handoff.py` or `agent-cap.js` edit already reaches it.
- No change to the card grammar itself, to the kickoff refusal text, or to `--task-skeleton`.
- No change to the typed OC4 arms or to the harnesses.
- No kit-version bump for workflows, roles, kickoff-manifest or check-wiring; each moves once at the
  close.

### Edges

- **consumes-from** `TOOL-aOrientedCast-2` — `handoff.py`'s render, check and kickoff-checker
  resolution, which S3 and S4 extend.
- **consumes-from** `TOOL-aOrientedCast-4` — the OC4 arms of `unattended-build.test.sh`, which S1
  rewrites.
- **consumes-from** `TOOL-aOrientedCast-8` — the adopter, its self-test's fixture and `check_roles`
  in `check-wiring.sh`.
- **consumes-from** `KICK-aOrientedCast-1` — the card's task grammar in `manifest-check.sh`, which
  S5 corrects.
- **hands-off** `TOOL-aOrientedCast-14` — rewording the `agent-cap.test.sh` comment at `:2220` to
  name arm 6 of the roles adopter's self-test, whose label §4 fixes.

## 4. Design

### The spans (S1)

| Span | Where it stands | Untyped prompts | Read from |
|---|---|---|---|
| `stalls for hours` | spec writer, criterion craft | present | `prompt:spec:` lines |
| `DO NOT WRITE PRODUCT CODE` | spec writer | present | `prompt:spec:` lines |
| `real probe rather than a claim` | spec writer, reuse craft | present | `prompt:spec:` lines |
| `the whole reason that join exists` | disposal, edge-join rationale | present | `prompt:dispose:` lines |
| `CHANGE THE SPEC FIRST` | child builder | present | the child's untyped output |
| `reuses every lens` | an untyped durable deferral | present | its `RESULT` line |
| `This stage runs as the` | every typed stamp | absent | every untyped prompt line |
| `a why that opens DIVERGENCE:` | typed child builder | absent | the child's untyped output |
| `changes nothing else in the spec` | typed child builder | absent | the child's untyped output |

The first four and the deferral's span are the spans the typed arms at `:2628-2636` and `:2688`
assert ABSENT from a typed run, so each typed `hasnt_` gains an untyped `has` twin and the pair
cannot pass by both sides losing the text. The byte comparison keeps the intent of
`TOOL-aOrientedCast-4` AC1 and AC7, that a stage with no role runs exactly as the harness does
without `roles`, measured against the CURRENT harness: for run 0 of the build harness and for each
child mode, `promptjson:` from a run with no `roles` key equals `promptjson:` from the same run with
`"roles":{}`, and the untyped durable deferral's `RESULT` line compares the same way. Both harnesses
refuse a `roles` value that is not a plain object and name each unknown key
(`unattended-build.template.js:445-475`, `unattended-unit.js:150-160`), so an empty object passes
both and types no stage; the builder confirms that by the first run of the arm. The arm labels keep
their `OC4 AC1` and `OC4 AC7` prefixes.

### The labels (S3)

In `render_handoff`, when any `reads` key opens `task:`, before `extract_task_fields` is called:
`resolve_kickoff_checker(root)` and `resolve_bash()`, then the checker run with `--task-skeleton`,
stdin closed and the `CHECKER_BOUND_S` bound, as `resolve_card_path` runs it for `--card --path`.
Each line of its output is put through the card line grammar, and every field line's label, in
order, is zipped with `TASK_FIELDS`. `extract_task_fields(text, labels)` takes that `{label: field}`
map in place of building one from `TASK_LABELS`. A role that reads no `task:` key never runs the
checker for labels. The derivation is written inline in the two existing functions, so no symbol is
minted.

### The agreement arm (S4)

Arm 6 of `adopt-roles.test.sh`, after `build_fixture`:

1. Resolve the hooks kit: `roles_lib.resolve_kit_dir("hooks", "agent-cap.js", <this kit's dir>)`,
   the derived-path idiom `handoff.py` uses for the kickoff kit. No hooks kit, or no `node`, prints
   `SKIP arm 6 — <what is absent>` and adds no assertion.
2. `mkdir -p <fixture>/<MR>/builds/bx/prompts`, then from the fixture root:
   `handoff.py render --role gov-researcher --build bx --unit TOOL-bx-1 --input question=<text>
   --out <MR>/builds/bx/prompts/<date>-prompt-TOOL-bx-1-1-researcher.md --part task`, capturing
   stdout. The role reads `input:question` and two optional brief keys, so no card is needed.
3. Build the payload `{"tool_name":"Agent","cwd":<fixture, node's spelling>,"session_id":…,
   "prompt_id":…,"tool_use_id":…,"tool_input":{"subagent_type":"gov-researcher","prompt":<stdout>}}`
   with python's `json.dumps`, the shape `agent-cap.test.sh`'s `run_spawn` builds, and pipe it to
   `node <hooks kit>/agent-cap.js` from the scratch root under `env -u CLAUDE_PROJECT_DIR`.
   Assert exit 0 and empty stderr.
4. `handoff.py check <the file>` exits 0, and its printed `task-sha` equals the marker's in stdout.

The labels: `arm 6 the renderer's task part is admitted by the spawn guard` and `arm 6 check
re-derives the marker's task-sha`. The arm defines no shell function, so the test's python launcher
is found by an inline candidate loop rather than a helper. `FLOOR_ASSERTIONS` rises by the L2 arm's
assertions only, so a host that SKIPs arm 6 does not red the floor.

### The conf read (S6)

The fixture in `adopt-roles.test.sh` gains arm 7: the conf is written as
`export MEMORY_ROOT=<MR>  # note` beside `CHARTER=<CH>`, then `--scaffold` and `--check` each exit 0,
the rendered Skill carries no `# note`, and the Skill and every agent type name the same `<MR>/`
root. Against the base adopter the scaffold exits 2, "MEMORY_ROOT is blank or absent".

### The kickoff stamp

`manifest-check.sh` is in the kickoff manifest's `watch:` list, so this unit re-stamps
`memory/guides/SESSION-KICKOFF.md`'s `last-audit` with a delta line in its commit message.

### Inventory

No function, class or constant is minted, except `TASK_FIELDS`, a module constant in
`tools/roles/handoff.py`, which no naming cell grades. The new gotcha record's name is
`test-oracle-read-from-a-historical-sha`, checked against the catalogue for a collision by the
gotchas checks.

### Files touched (estimate)

`tools/workflows/unattended-build.test.sh`
`tools/roles/handoff.py`
`tools/roles/adopt-roles.sh`
`tools/roles/adopt-roles.test.sh`
`skills/session-kickoff/manifest-check.sh`
`skills/session-kickoff/manifest-check.test.sh`
`tools/check-wiring.sh`
`tools/check-wiring.test.sh`
`memory/gotchas/`
`memory/guides/SESSION-KICKOFF.md`

### Alternatives rejected

- The agreement arm in `agent-cap.test.sh`, where the review's skeptic placed it: that file is in
  `TOOL-aOrientedCast-14`'s write set, and the brief requires the two sets not to meet. The roles
  adopter's self-test already builds a scaffolded fixture holding a rendered index, which the hook
  side would have to rebuild.
- A `handoff.py --selftest` holding the arm: the roles kit's shipped script would then locate and run
  a sibling kit's hook on every adopter's bar.
- Keeping the byte comparison against a sha, moved forward to the current tip: the same oracle,
  stale again at the next prompt edit.

## 5. Production-readiness checklist

- security — No new write path. The agreement arm runs the hook on a payload it builds itself.
- perf / scale — One more bounded checker run per render that reads a `task:` key; the arm adds one
  render and one hook spawn to a held suite.
- error / empty / loading states — A label derivation that fails refuses the render by name; a broken
  index reads UNWIRED; an absent hooks kit SKIPs arm 6 out loud.
- observability — The UNWIRED line names the index and the scaffold; the refusal names the checker.
- risks — The renderer now depends on the kickoff checker for any `task:` key, which it already did
  for the card's location when no `--card` is given.
- testing — The arms of §7, observed RED-first at the close; the direct probes of §6 in the pass.
- migration — None. No adopter holds the roles kit, which the base does not carry.
- user docs — None beyond the refusal and UNWIRED texts; no user-facing behaviour changes otherwise.

## 6. Acceptance criteria

No criterion runs a gate leg or a suite; each runs the unit's own code over a fixture, or reads a
file. The suite arms are under `New arm:` in §7.

- **AC1** — When `grep -c '646d4a73' tools/workflows/unattended-build.test.sh` runs it prints 0, and
  when the `unattended-build self-test` leg runs at the close, every `OC4 AC1` arm passes against the
  current harnesses.
  Red when: an untyped arm still reads its oracle from a historical commit, or a typed-only span
  leaks into an untyped prompt.
  permission: this run's builder may not execute the workflows suite; the main loop observes it.
- **AC2** — When `python tools/roles/handoff.py render --role gov-reuse-scout --build aOrientedCast
  --unit TOOL-aOrientedCast-15 --card <a scratch card> --input question=q --stdout --part task` runs
  over a card whose `## task` fills all eight fields, its `### task:in` block holds the card's IN
  scope value; and `grep -c 'Goal (1–2 sentences)' tools/roles/handoff.py` prints 0.
  Red when: the labels are typed into the renderer again, or a derived label fails to reach its
  card value.
  fixture: the scratch card is written by the pass outside the tree and deleted after it.
- **AC3** — When the `roles adopter self-test` leg runs at the close, arm 6 passes: the hook admits
  the rendered task part and `handoff.py check` re-derives the marker's `task-sha`.
  Red when: the renderer's task hash is staged to skip its CRLF fold or to hash the section without
  its last newline, so the hook refuses the prompt.
  permission: this run's builder may not execute the roles adopter's suite; the main loop observes
  it.
- **AC4** — When `bash skills/session-kickoff/manifest-check.sh --card --append --session <id>` reads,
  in a scratch clone, a READY body whose OUT field is written `**OUT / non-goals** (explicit
  cut-line) : …`, it exits 1 naming `OUT / non-goals` as a placeholder; written `(explicit
  cut-line) : the stored card`, it appends.
  Red when: the awk keeps the colon after a space and admits the placeholder, which the base does.
  fixture: a scratch clone under a short `%TEMP%` root, its card written by `--card --write`.
- **AC5** — When `bash tools/roles/adopt-roles.sh --scaffold` runs in a scratch repository whose
  conf reads `export MEMORY_ROOT=memory  # note`, it exits 0, and `grep -c '# note'
  .claude/skills/build/SKILL.md` prints 0 there.
  Red when: the adopter reads the key with a bare `sed`, which exits 2 on the `export` form and
  renders the comment into the Skill without it.
  fixture: a scratch repository holding a copy of the roles kit, built as `build_fixture` builds one.
- **AC6** — When `bash tools/check-wiring.sh --check` runs in a scratch repository holding the roles
  kit, every rendered file and a `.claude/roles.json` truncated to `{`, it exits 1 and prints one
  `UNWIRED  roles` line naming `.claude/roles.json` and `adopt-roles.sh --scaffold`, and no
  `ok       roles` line.
  Red when: a broken index still reads ok.
  fixture: the scratch repository the `check-wiring` suite's roles block builds, made in the pass.

## 7. Gates

`unattended-build self-test` · `tier2-review self-test` · `review-join self-test` · `verifier fan-out self-test` · `roles adopter self-test` · `roles render wiring` · `roles catalogue` · `manifest-check self-test` · `scratch-guard self-test` · `lexicon naming predicates` · `kickoff-manifest ratchet` · `check-wiring self-test` · `straggler-guard arms` · `transition-audit arms` · `gotchas selftest` · `recall floor` · `recall floor arms` · `install-prefix (shipped surface)` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/workflows/unattended-build.test.sh · covers AC1 · the span and empty-roles arms of §4, against an untyped spec prompt staged to carry the role stamp · `FLOOR_ASSERTIONS` moved to the count the rewritten block executes
New arm: tools/roles/adopt-roles.test.sh · covers AC3 · arm 6, against `handoff.py`'s task hash staged to skip the CRLF fold · none
New arm: tools/roles/adopt-roles.test.sh · covers AC5 · arm 7, against the base adopter's bare `sed` read of `MEMORY_ROOT` · `FLOOR_ASSERTIONS` raised by arm 7's assertions
New arm: skills/session-kickoff/manifest-check.test.sh · covers AC4 · a KC row whose OUT label is followed by a space before its colon, against the base `value()` · `FLOOR_ASSERTIONS` raised by the rows added
New arm: tools/check-wiring.test.sh · covers AC6 · a truncated `.claude/roles.json` in the roles block, against the base `check_roles` that falls through to ok · none

The main loop observes each arm RED on its staged break and GREEN once restored, at the close (M8).
No pass runs a leg above.

## 8. Open questions

- **F1 — Where does the renderer-against-hook arm live, when the review puts it in
  `agent-cap.test.sh` and the brief keeps this unit off `TOOL-aOrientedCast-14`'s files?**
  Options: (a) `agent-cap.test.sh`, sequencing this unit after `TOOL-aOrientedCast-14`; (b) the roles
  adopter's self-test, which already scaffolds a fixture with a rendered index; (c) a
  `handoff.py --selftest` arm.
  (a) breaks the brief's write-set rule. (c) ships a roles script that locates and runs a sibling
  kit's hook on every adopter's bar, a new shipped surface: M3 veto 2. (b) keeps both units
  disjoint, tests the shipped renderer against the shipped hook, and its leg is unguarded, so the
  review's guard widening is not needed.
  RESOLVED (agent, 2026-10-12, delegated): (b), as §4 "The agreement arm" states it.
- **F2 — Does the status header carry `closes M4 M5 L1 L2 L3`, as the spec brief asks?**
  `backlog.read_header_verbs` expands a `closes` value through the generator's id grammar, and none
  of the five is an id: a probe of `_read_backlog_verbs` on such a header raised "is not an id or an
  id range", which refuses every render of the build index. The build keeps no `BACKLOG.md`.
  Options: (a) write the verb; (b) name the review items in §1 and leave the verb out.
  RESOLVED (agent, 2026-10-12, delegated): (b). Option (a) fails the build-index leg, M3 veto 1.

## 9. Revision log

- rev-1 · 2026-10-12 · initial draft.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "derive card task field labels from the kickoff
skeleton"` ranked name-token neighbours, `field`, `render_cards_md` and `derive_scope`, none of which
reads a card. No new seam is built; the seams extended, found by reading, are
`resolve_kickoff_checker`, `resolve_card_path`'s bounded checker run, `extract_task_fields` and
`check_handoff` in `tools/roles/handoff.py`; `build_fixture` in `tools/roles/adopt-roles.test.sh`;
`roles_lib.read_conf_key` and `roles_lib.resolve_kit_dir`; `value()` in
`skills/session-kickoff/manifest-check.sh`; and `check_roles` in `tools/check-wiring.sh`. The recall
probe surfaced `TOOL-aOrientedCast-7`'s ledger, whose task-sha was observed by a hand probe, which is
the gap S4 closes, and this build's review and brief.

Recall terms used: `untyped byte identity base harness historical sha oracle handoff.py TASK_LABELS task-skeleton agreement arm conf parser`
