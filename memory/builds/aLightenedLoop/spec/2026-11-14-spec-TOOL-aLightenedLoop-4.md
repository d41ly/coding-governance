# TOOL-aLightenedLoop-4 — a builder checks its spec can be built before its first edit, a spec cites where it read the code, and a watched path brings its manifest re-stamp

**Status:** SPECCED · rev-1 · 2026-11-14 · node a · Tier-2 · base 846d51d3 · streams tooling · order 4

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-14-build-TOOL-aLightenedLoop-1-analysis.md](../build/2026-11-14-build-TOOL-aLightenedLoop-1-analysis.md) | research | TOOL-aLightenedLoop-1 TOOL-aLightenedLoop-2 TOOL-aLightenedLoop-3 TOOL-aLightenedLoop-5 |
| [2026-11-14-prompt-TOOL-aLightenedLoop-1-brief.md](../prompts/2026-11-14-prompt-TOOL-aLightenedLoop-1-brief.md) | research | TOOL-aLightenedLoop-1 TOOL-aLightenedLoop-2 TOOL-aLightenedLoop-3 TOOL-aLightenedLoop-5 |

<!-- /gen:spec-records -->

## 1. Goal

In dSafePassage 23 unit runs diverged, and builders ran 50 to 100 minutes before they did. By run,
about 9 diverged on a spec that contradicts itself, about 5 on a claim the current code does not
bear out, and about 4 on a fix that needs a file outside the declared list, a manifest re-stamp
among them. This unit moves those discoveries to the start of the pass and upstream into the spec.
The builder role checks the spec can be built before its first product edit. The spec format says
how a claim about code is cited, and that a watched path brings its kickoff manifest's re-stamp into
the files-touched list. It changes prompt and format text only, so no check's verdict, refusal text
or rendered byte moves except the rendered prose itself.

## 2. Scope (IN)

- **S1** — `tools/roles/agents/gov-builder.agent.md` gains the feasibility paragraph of §4, after
  the paragraph on divergence. Observed by AC1 and AC2.
- **S2** — The untyped arm of the divergence ternary in `tools/workflows/unattended-unit.js` gains
  the feasibility sentence of §4 ahead of its `CHANGE THE SPEC FIRST` order, with one comment line
  saying why the typed arm does not. The typed prompt is unchanged byte for byte. Observed by AC3.
- **S3** — The spec format's writing rule on verifying code claims, in
  `tools/memory-tree/SPEC-TEMPLATE.template.md`, names the two citation forms. Observed by AC4.
- **S4** — The same file gains the watched-path bullet of §4 under its recurring §4 sub-heads.
  Observed by AC4.
- **S5** — `tools/roles/agents/gov-spec-writer.agent.md` points at the spec format's citation rule
  instead of restating its forms. Observed by AC5.
- **S6** — The three rendered copies are regenerated from their sources: `.claude/agents/gov-builder.md`,
  `.claude/agents/gov-spec-writer.md` and `memory/TEMPLATE-SPEC.md`. Observed by AC1, AC4 and AC5.
- **S7** — No new or changed line in the four source files spells a line citation without a stable
  form. Observed by AC6.
- **S8** — Three assertions in `tools/workflows/unattended-build.test.sh` pin S2. NOT OBSERVED by a
  criterion of this pass: a role agent runs no suite, so the main loop observes the arm RED and then
  GREEN at the close, as §7's `New arm:` line declares.

## 3. Non-goals (OUT)

- No gate, join or hygiene arm grades the new rules. A check-spec-tokens join reading a spec's
  files-touched list against the manifest's `watch:` line is a follow-up, filed only if the prose
  rule proves insufficient. The owner scoped this unit to prompts (brief, Acceptance).
- No change to the typed builder prompt, the `DIVERGENCE:` hand-back, the return schema or the
  `diverged` field.
- No change to `DRIVER_STEPS`. TOOL-aLightenedLoop-3 edits it at order 3, in the same file; this
  unit edits only the divergence ternary and finds it by its text, so it builds on whatever unit 3
  leaves.
- No change to any role's house overlay under `tools/roles/house/`, to any other role, or to the
  build method.
- No kit version moved by hand: `roles`, `workflows` and `memory-tree` move only through the
  lander's mint (build README, Build-level rules).
- No `help/` page. The change adds no command, flag, key or surface; the spec format is itself the
  page its rules live on, and no page under `help/` restates role bodies (grep for `gov-builder` and
  `DIVERGENCE` over `help/`, 2026-11-14, finds only handoff commands in `help/roles.md`).
- No timing figure. A divergence's saving shows only across a later run's units, so the brief
  exempts this unit from the measured timing (brief, Acceptance).

### Edges

none

## 4. Design

### Evidence

Read at `846d51d39`. Every blob cited here is the one at that commit, and the worktree matched it.

- The builder role's divergence paragraph is `tools/roles/agents/gov-builder.agent.md@062f8fad387c:19-22`.
  It says to return on a disagreement, and nothing in it says when to look for one.
- The harness's divergence ternary is `tools/workflows/unattended-unit.js@71852dc0917e:284-290`. The
  typed arm hands a divergence back, and the untyped arm orders `CHANGE THE SPEC FIRST`. The untyped
  prompt also carries the reading craft the role carries for a typed builder (`:282`), as the header
  comment states (`:53-61`). Every governed caller passes `roles` (`.claude/skills/build/SKILL.md`,
  "Every harness call carries `roles`"), so the role is what dSafePassage's builders read.
- The roles kit's rule: a base block points at the document that owns a rule and never restates
  it, and stage protocol stays in the harness (`tools/roles/README.md@2491a1ac49ab:25-28`). The
  feasibility check is craft, so it goes in the role. The hand-back it ends in is protocol, and it
  already lives in the harness.
- A role body may not spell a protocol file's name, and `TEMPLATE-SPEC.md` is one: the catalogue
  checker's R5 (`tools/roles/check_roles.py@db628e9ae396:227-229`). The role names "the spec format"
  instead. The builder's body ceiling is 4096 bytes (`:93-97`). The handoff render reported its body <!-- PINNED 2026-11-14 -->
  at 2257 bytes at `846d51d39`. <!-- PINNED 2026-11-14 -->
- The spec writer's citation rule already names both forms, at
  `tools/roles/agents/gov-spec-writer.agent.md@043e61df0427:30-31`, since PLAY-dOrderedCharter-48.
  The spec format's writing rule names neither: `tools/memory-tree/SPEC-TEMPLATE.template.md@1e45ee10d546:107`.
  The format is the document that owns the rule and reaches every author, so the forms move there,
  and the role points at it.
- The citation forms are fixed by the positional check. Its producers limb reds a line in a
  directive source that matches `PRODUCER_RE` and names no stable form. The pattern is the three
  spellings `file:line`, `path and line` and `<path>:<line>`, case-insensitive. The directive sources
  include `tools/roles/agents/`, `tools/workflows/` and every `tools/*/*.template.md`
  (`tools/playbook/positional.py@35ec5e223df9:67-74`). So the brief's "cite the file:line" is
  written as `path#symbol` or the blob-pinned line, and no new line uses any of those three spellings.
- The manifest's `watch:` line is `memory/guides/SESSION-KICKOFF.md@c353dcd9417c:7`. The pre-commit
  hook runs the manifest check's staged leg (`.githooks/pre-commit@468b13e420e3:256-257`). That leg
  refuses a commit that stages a watched path unless the same commit moves the `last-audit` stamp
  (`skills/session-kickoff/manifest-check.sh@4d3d63c0fad1:1973-1987`). A builder that may write only
  its declared paths cannot commit such a unit unless the spec declared the manifest. The analysis
  record counts this among the four out-of-list divergences, and recall hit
  `2026-10-14-build-TOOL-dRedressedBar-1-2-agent-returns` is one instance.

### The role paragraph (S1)

Inserted in `tools/roles/agents/gov-builder.agent.md` as its own paragraph, after the one ending
"never resolved by editing the spec or by building the intersection." and before "How you build:":

```text
Before your first product edit, check that the spec can be built as written, and spend minutes on
it, not the pass. Probe each claim it makes about current code against the tree: every path,
symbol, flag, line and behaviour it cites. Cross-read its scope, design and acceptance for two
statements that cannot both hold. Check that its files-touched list holds every path the change and
the commit hooks will need, such as a sibling's spec, a decision record or a kickoff manifest's
re-stamp. Report every check that fails in one divergence, never one per dispatch.
```

The last sentence matters for the number of rounds. dSafePassage unit 5 took six dispatches and six
spec rounds, so a builder that stops at its first failed check costs one round per check.

### The harness sentence (S2)

In the untyped arm of the `builder ?` ternary, the string that opens
`'The spec is the design; where you must diverge, CHANGE THE SPEC FIRST` gains this string
concatenated ahead of it, byte for byte, with its trailing space:

```text
Before your first product edit, check that the spec can be built as written: probe each claim it makes about current code against the tree, cross-read its scope, design and acceptance for two statements that cannot both hold, and check that its files-touched list holds every path the change and the commit hooks will need. 
```

One comment line above the ternary says why the typed arm does not carry it:
`// TOOL-aLightenedLoop-4 - the feasibility check is reading craft: the role carries it for a typed builder, and the untyped arm carries it inline.`
The change is a string concatenation inside the existing ternary. It adds no definition, loop or
arrow, so the file keeps its one top-level definition (`tools/workflows/unattended-unit.js@71852dc0917e:20-26`).

### The spec format (S3, S4)

In `tools/memory-tree/SPEC-TEMPLATE.template.md`, the writing-rules bullet at line 107 becomes:

```text
- Verify every claim about existing code against source at writing time, and cite where you read
  it: `path#symbol` for a definition, else the blob-pinned line `<path>@<oid>:<n>`. A bare line
  number drifts as the file is edited, and neither form does. Mark the rest `UNVERIFIED`.
```

After the recurring §4 sub-heads bullet, the one ending `### Alternatives rejected`., a new bullet:

```text
- **A watched path brings its manifest.** Where the project keeps a kickoff manifest, a unit that
  edits a path the manifest's `watch:` line names lists the manifest under
  `### Files touched (estimate)` as well, with its `last-audit` re-stamp named beside it. The
  manifest check's staged leg refuses a commit that stages a watched path unless that commit also
  moves the stamp, so a builder held to its declared paths cannot commit the unit without it.
```

The bullet names no path, because the template ships to adopters whose manifest lives elsewhere,
and the template declares no manifest placeholder (`tools/memory-tree/kit.toml@fdae4a7106f3:70-74`).

### The spec writer's role (S5)

In `tools/roles/agents/gov-spec-writer.agent.md`, lines 30 and 31 become:

```text
- Verify every claim about current code by reading that code, and cite where you read it in the
  form the spec format's writing rules give. A claim you did not verify is a claim you do not make.
```

### The renders (S6)

`python tools/roles/render_agents.py --write` rewrites the two agent files. Every other role
renders byte-identical, because no other source moved.
`bash tools/memory-tree/adopt-memory-tree.sh --render` rewrites `memory/TEMPLATE-SPEC.md`. The
other three documents it renders stay byte-identical.

### The arm (S8)

In `tools/workflows/unattended-build.test.sh`, beside the OC4 child arms:

- Inside the `for m in unattended attended` loop over the untyped child, one `has` reads
  `check that the spec can be built as written` in `$o`.
- After the typed child's run on `$OC_CT`, one `hasnt_` reads the same text in its `$o`. That is
  the typed prompt; the typed builder gets the step from its role.

### What this does not check

- Whether a builder actually probes before editing. The role and the prompt say so, and nothing
  observes the order of a builder's tool calls.
- Whether a spec's citations are true. The positional check reads every pinned line against its
  blob and every symbol against its file. It does not ask whether the cited line supports the claim.
- Whether a spec names the manifest when it should. That join is the §3 follow-up.

### Alternatives rejected

- The feasibility sentence in both harness arms, with no role edit. A builder spawned from a handoff
  file, outside the harness, would miss it. The typed arm would also restate craft the roles README
  assigns to the role.
- The role alone, leaving the harness untouched. An untyped builder would then lack a step a typed
  one has, while the harness keeps every other piece of the role's reading craft inline for it.
- Bare `path:line` citations, as the brief words them. The positional check's producers limb reds a
  directive that asks for them, and a bare line number goes stale as the file is edited.
- Leaving the spec writer's forms in its role beside the format's new rule. The same rule would then
  live in two places, which the roles README and the charter's one-fact rule both forbid.

### Files touched (estimate)

- `tools/roles/agents/gov-builder.agent.md`
- `.claude/agents/gov-builder.md`
- `tools/roles/agents/gov-spec-writer.agent.md`
- `.claude/agents/gov-spec-writer.md`
- `tools/workflows/unattended-unit.js`
- `tools/workflows/unattended-build.test.sh`
- `tools/memory-tree/SPEC-TEMPLATE.template.md`
- `memory/TEMPLATE-SPEC.md`

## 5. Production-readiness checklist

- security — N/A: prose in two prompts and one format document, and no new write path or surface.
- perf / scale — the builder body grows by about 560 bytes, under its 4096-byte ceiling. Timing is <!-- PINNED 2026-11-14 -->
  exempt, as §3 says.
- error / empty / loading states — N/A: no code path branches on the new text.
- observability — the handoff render prints the role body's size on stderr on every render.
- risks — a builder may read "spend minutes" as licence to skip deeper reading. The step bounds the
  check, not the reading the paragraph above it already requires.
- testing — the probes of §6 before the commit, and the arm of §7, observed RED and then GREEN by
  the main loop at the close.
- migration — none. An adopter receives the text at the next kit versions the lander mints.
- user docs — the spec format is the page for its own rules. No `help/` page restates role bodies.

## 6. Acceptance criteria

All commands run from the worktree root in Git Bash, before the pass commit unless stated. `$S` is
the scratch root the task names.

- **AC1** — After `python tools/roles/render_agents.py --write`, `git status --porcelain .claude/agents/`
  lists exactly `.claude/agents/gov-builder.md` and `.claude/agents/gov-spec-writer.md`, and
  `grep -c 'check that the spec can be built as written' .claude/agents/gov-builder.md` prints `1`.
  Red when: the paragraph is missing from the source, so the grep prints `0`, or a third agent file
  renders differently.
- **AC2** — When the `tools/roles/handoff.py` render in the block below runs before the edit and
  again after it, its outputs saved to `$S`, `diff` of the two prints the
  marker line, whose `role-sha` moves, then the S1 paragraph's six lines and the blank line after
  them as added lines, and nothing else.
  Its stderr load-set note reports the body under 4096 bytes. <!-- PINNED 2026-11-14 -->
  Red when: the role render drifts elsewhere, or the paragraph pushes the body over its ceiling and
  the note reports it.
  figure: DERIVED, the byte count read from the note at observation time.

  ```bash
  python tools/roles/handoff.py render --role gov-builder --build aLightenedLoop --unit TOOL-aLightenedLoop-4 \
    --input spec=memory/builds/aLightenedLoop/spec/2026-11-14-spec-TOOL-aLightenedLoop-4.md --stdout > "$S/h0.md"
  # ...edit and render the role, then the same command into "$S/h1.md"
  diff "$S/h0.md" "$S/h1.md"
  ```
- **AC3** — The probe below prints the builder prompt the harness composes. Run over the harness as
  `HEAD` holds it and over the edited `tools/workflows/unattended-unit.js`, the typed prompts
  (`gov-builder`) compare equal under `cmp`. The edited untyped prompt holds the S2 sentence once,
  and deleting that one occurrence yields the old untyped prompt byte for byte. The check in the
  block prints `True`.
  Red when: the sentence lands in the typed arm, so `cmp` reports a difference, or the edit moves
  any other byte, so the comparison prints `False`.

  ```bash
  cat > "$S/unit-prompt.js" <<'EOF'
  const fs = require('fs')
  const src = fs.readFileSync(process.argv[2], 'utf8').replace(/^\s*export\s+const\s+meta\s*=/m, 'const meta =')
  const F = Object.getPrototypeOf(async function () {}).constructor
  const a = { repo: '.', slug: 's', unitId: 'T-s-1', specPath: 'p.md', briefPath: 'b.md', driver: 'drv',
    ground: 'G /x ', checklist: 'c', scratch: '/x', mode: 'attended' }
  if (process.argv[3]) a.roles = { builder: process.argv[3] }
  new F('args', 'agent', 'log', 'phase', src)(JSON.stringify(a), async (p) => { process.stdout.write(p); return null }, () => {}, () => {})
  EOF
  git show HEAD:tools/workflows/unattended-unit.js > "$S/before.js"
  node "$S/unit-prompt.js" "$S/before.js" > "$S/u0.txt"; node "$S/unit-prompt.js" tools/workflows/unattended-unit.js > "$S/u1.txt"
  node "$S/unit-prompt.js" "$S/before.js" gov-builder > "$S/t0.txt"; node "$S/unit-prompt.js" tools/workflows/unattended-unit.js gov-builder > "$S/t1.txt"
  cmp "$S/t0.txt" "$S/t1.txt" && echo typed-identical
  python -c "import sys; a=open(sys.argv[1]).read(); b=open(sys.argv[2]).read(); s='Before your first product edit, check that the spec can be built as written: '; i=a.find(s); j=a.find('The spec is the design;', i); print(a.count(s) == 1 and a[:i] + a[j:] == b)" "$S/u1.txt" "$S/u0.txt"
  ```

- **AC4** — After `bash tools/memory-tree/adopt-memory-tree.sh --render`, the block below lists
  `memory/TEMPLATE-SPEC.md` alone of the four rendered documents. `grep -c` over
  `memory/TEMPLATE-SPEC.md` prints `1` for `A watched path brings its manifest` and `1` for
  `the blob-pinned line`, and the same two counts over `tools/memory-tree/SPEC-TEMPLATE.template.md`.
  Red when: the render was not re-run, so the rendered count is `0`, or a second copy of either rule
  lands in the format.

  ```bash
  git status --porcelain -- memory/TEMPLATE-SPEC.md memory/HYGIENE.md memory/guides/BUILD-METHOD.md memory/guides/ANNOTATION-STYLE.md
  ```
- **AC5** — `grep -c '<path>@<oid>:<n>' tools/roles/agents/gov-spec-writer.agent.md .claude/agents/gov-spec-writer.md`
  prints `0` for both files, and `grep -c "form the spec format's writing rules give"` prints `1`
  for both, and `grep -c 'TEMPLATE-SPEC' tools/roles/agents/gov-spec-writer.agent.md` prints `0`.
  Red when: the role still restates the forms, or names the protocol file the catalogue checker's
  R5 refuses.
- **AC6** — `git grep -n -i -E 'file:line|path and line|<path>:<line>' -- tools/roles/agents/gov-builder.agent.md tools/roles/agents/gov-spec-writer.agent.md tools/workflows/unattended-unit.js tools/memory-tree/SPEC-TEMPLATE.template.md`
  prints nothing and exits 1, as it did at `846d51d39`.
  Red when: a new line asks for a line citation in one of the three spellings, and the grep prints
  it.

## 7. Gates

`roles catalogue` · `roles render wiring` · `roles render selftest` · `roles adopter self-test` · `unattended-build self-test` · `workflow script syntax` · `kit/dogfood doc parity` · `positional (the citation check alone)` · `policy fixtures` · `check-wiring self-test` · `lexicon naming predicates` · `verifier fan-out self-test` · `tier2-review self-test` · `review-join self-test` · `recall floor` · `recall floor arms` · `spec tokens (a spec's own names resolve)` · `memory hygiene` · `kit epoch (shipped bytes move, the version moves)` · `kit version markers`

New arm: tools/workflows/unattended-build.test.sh · covers AC3 · the two untyped `has` assertions, staged by deleting the S2 sentence from the untyped arm, and the typed `hasnt_`, staged by adding it to the typed arm · none

The roles legs read S1, S5 and the two agent renders. `roles render wiring` byte-compares the
renders, and `roles catalogue` grades each body against its ceiling and R5. `kit/dogfood doc parity`
compares `memory/TEMPLATE-SPEC.md` with its source. `positional (the citation check alone)` runs
the producers limb AC6 approximates. `policy fixtures` names the builder's base file in its guard.
The remaining legs are owed by the guards the files-touched paths trip. This spec's author ran only
the spec-token checker and the memory hygiene gate; every other verdict is the main loop's at the
close.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-14 · initial draft from the brief `2026-11-14-prompt-TOOL-aLightenedLoop-1-brief`
  and the analysis `2026-11-14-build-TOOL-aLightenedLoop-1-analysis`, grounded at `846d51d39`.

## 10. Reuse audit

The seams are the two carriers the roles kit already splits craft and protocol across: the builder
role's divergence paragraph and the harness's divergence ternary, which keeps the role's reading
craft inline for an untyped builder. Both are extended in place. The citation forms are the ones
`tools/playbook/positional.py` already defines and its producers limb enforces, so no new form is
minted. `python tools/codebase-map/reuse_lookup.py "builder checks the spec's claims about current code before its first edit and hands back a divergence"`
ranked only name-stem neighbours such as `check` and `build_records`, none a prompt carrier, so no
code seam fits a prose change, and none is needed. Recall returned TOOL-aOrientedCast-4, which built
the typed hand-back this unit leaves unchanged, and TOOL-aOrientedCast-1's brief, which set the rule
that role craft lives in the role and stage protocol in the harness. It also returned the dRedressedBar
agent-returns record, where a builder's staged watch-list file needed a re-stamp its spec never
named. No hit disagreed with source.

Recall terms used: `python tools/memory-recall/query.py "how does a builder learn early that its spec is wrong about current code" --terms "builder divergence DIVERGENCE hand-back spec claim feasibility gov-builder role prompt unattended-unit manifest re-stamp last-audit cite blob-pinned"`
