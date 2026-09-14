# TOOL-aProbedUnit-4 — every harness agent is handed the session scratchpad, as a required `scratch` argument

**Status:** SPECCED · rev-1 · 2026-09-14 · node a · Tier-2 · base 1b000d1a · streams tooling · order 4 · ratified 2026-09-14

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-14-prompt-TOOL-aProbedUnit-1-1-spec-briefs.md](../prompts/2026-09-14-prompt-TOOL-aProbedUnit-1-1-spec-briefs.md) | journal | TOOL-aProbedUnit-1 TOOL-aProbedUnit-2 TOOL-aProbedUnit-3 TOOL-aProbedUnit-5 TOOL-aProbedUnit-6 TOOL-aProbedUnit-7 |
| [2026-09-14-review-TOOL-aProbedUnit-1-spec-audit-round1.md](../reviews/2026-09-14-review-TOOL-aProbedUnit-1-spec-audit-round1.md) | spec-audit | TOOL-aProbedUnit-1 TOOL-aProbedUnit-2 TOOL-aProbedUnit-3 TOOL-aProbedUnit-5 TOOL-aProbedUnit-6 TOOL-aProbedUnit-7 |

<!-- /gen:spec-records -->

## 1. Goal

Agents under the build harness write temporary files to `$TMPDIR/x` with `TMPDIR` empty — measured
empty on node `a` this session, the incident on node `d` — so a backup lands at the filesystem
root and its cleanup waits on an approval nobody answers. The session scratchpad path is in the
caller's system prompt and nowhere a workflow script can read. `tools/workflows/unattended-build.template.js`
REQUIRES a `scratch` argument, an absolute path, and hands it to every agent it spawns and to every
child it dispatches, so the one place temporary files belong is spelled in every prompt instead of
guessed from an environment that is empty.

## 2. Scope (IN)

- **S1** — The parent refuses without `scratch`, in the style of its `repo` and `slug` refusals,
  and refuses a `scratch` that is not absolute by shape — not beginning `/` or a drive letter and a
  separator — because a workflow script has no filesystem and shape is the only test it can make.
  Backslashes are folded to `/` once, in the parent, and the folded string is what every carrier
  below spells. Observed by AC1 and AC2.
- **S2** — `GROUND` carries one sentence naming that path as where every temporary file, backup,
  probe, log or throwaway clone goes, what is never used instead, and the one clone spelling that
  works there on Windows. Every parent-side agent — spec writers, the audit recorder, the disposal
  agent — is prefixed by `GROUND`, so one sentence reaches all of them. Observed by AC3.
- **S3** — `dispatch.args` in the roster hand-out carries `scratch`, the folded path, beside
  `repo`, `slug`, `mode`, `driver`, `ground` and `checklist`. Observed by AC4.
- **S4** — `tools/workflows/unattended-unit.js` adds `check('scratch', …)` and one agreement
  refusal: the `ground` it was handed must name the `scratch` it was handed, so a hand-composed
  dispatch cannot drop the path or send a child a different one from the one its ground text names.
  The child's `PROMPT` is `cfg.ground` first, so the sentence reaches the unit agent through the
  parent's text and is not spelled a second time. Observed by AC5.
- **S5** — The unattended Skill's "Drive the build as ONE program" bullet tells the caller to pass
  its own session scratchpad, the path its system prompt names, as `scratch`, absolute; the render
  `.claude/skills/unattended/SKILL.md` and `tools/workflows/unattended-build.js` are re-made in the
  same commit. Observed by AC6.
- **S6** — `tools/workflows/unattended-build.test.sh` gains the arms in section 6 and every
  existing fixture that expects a `RESULT` gains a `scratch`, because a required argument reds every
  fixture that lacks it and that is the point. Observed by AC1 to AC5.
- **S7** — The dossier `memory/map/features/review-harnesses.md` names `scratch` beside the args
  contract it already describes. Observed by AC6.

## 3. Non-goals (OUT)

- **No `TMPDIR` retarget.** `TOOL-aTetheredScratch-2` refused one on measurement: `/tmp` is a
  `usertemp` mount onto `%TEMP%` and no external root exists. This unit hands a path; it sets no
  variable, exports nothing into the child, and `scratch-guard` keeps grading what a command
  actually targets — that hook's own widening is `TOOL-aProbedUnit-5`.
- **No default, ever.** A defaulted scratch root is the floating temp dir this unit exists to end,
  and a script with no filesystem could only default it to a string it cannot check.
- **No verification that anything was written there.** A workflow script cannot see the tree. The
  sentence is an instruction, the hook is the enforcement, and this unit does not claim the first is
  the second.
- **No install-time rendering of the path.** `TOOL-dPolishedVitrine-1` rules that the harness's
  INSTALL literals are rendered at install rather than handed in args; the scratchpad is
  session-scoped and changes with every session, so `args` is the only carrier that can hold it, and
  the ruling is about a different class of path.
- **No second sentence in the child.** The brief asked for the same sentence in the child's
  `PROMPT`; section 4 explains why the child inherits the parent's one sentence through `cfg.ground`
  and joins the two arguments instead, so one prompt never carries two paths.
- **No version bump.** `unattended-build@1.0` and `unattended-unit@1.0` in the two `meta` blocks
  are engine identities; a required-argument change is a contract change and owes a bump, and the
  build README's rules give every bump to the closing pass. Section 8 F2 records that the brief's
  bump list does not name these two.
- **No change to `tier2-review.js` or the drift-audit siblings.** Their agents are spawned from
  their own prompts, outside this build's mandate; they are named as follow-ups in the Edges.

### Edges

- **consumes-from** external — the build-level rule that `--dispatch` and the child's `check()`
  are where a missing key is refused; the parent's hand-out is the contract the caller copies, and
  nothing here reaches a caller that composes child args by hand except the child's own refusal.
- **hands-off** `TOOL-aProbedUnit-5` — the enforcement: `tools/hooks/scratch-guard.js` denying an
  empty temp variable, `/tmp` and root litter, and allowing the CLI's scratch base. This unit tells
  agents where to write; that unit stops the writes that ignore it.
- **hands-off** external — the two `meta.version` bumps, with the three kit bumps the closing pass
  already owns; and the same `scratch` argument for `tools/workflows/tier2-review.js`, whose lens
  and skeptic agents are told nothing about temporary files today.

## 4. Design

### The parent

After the `slug` refusal at `tools/workflows/unattended-build.template.js:178`, one more of the same
shape:

```js
if (typeof cfg.scratch !== 'string' || !/^(\/|[A-Za-z]:[\\/])/.test(cfg.scratch)) {
  throw new Error('unattended-build: args must carry an explicit `scratch`, an ABSOLUTE path to the ' +
    'session scratchpad — the one the caller\'s own system prompt names. Got ' + JSON.stringify(cfg.scratch) +
    '. Refusing to default it: a defaulted scratch root is the floating temp dir this argument exists to end.')
}
const scratch = cfg.scratch.replace(/\\/g, '/')
```

The fold is here and nowhere else, because the value crosses into a bash-quoted prompt and a JSON
`args` object, and a backslash survives neither reliably — section 8's rule on hand-serialised JSON
names it the top breaker. Every carrier below reads `scratch`, the folded const.

`GROUND` at `:335` gains, after the record sentence and before the mode ternary:

```
'Every temporary file, backup, probe, log or throwaway clone this run makes goes under ' + scratch +
', spelled absolute; never $TMPDIR, $TMP, $TEMP, /tmp, a bare mktemp, or any path outside the repository. ' +
'A clone there is made with `git -c core.longpaths=true clone`, because that path is long enough that a plain clone fails on Windows with Filename too long. '
```

The clone clause is not decoration. Measured 2026-09-14 on node `a`, with this worktree as the
source and this session's 170-character scratchpad as the destination: `git clone --local
--no-checkout` exits 128 with `fatal: failed to unlink … Filename too long`, and `git -c
core.longpaths=true clone --local --no-checkout` exits 0 and leaves a pack. Without the clause the
sentence forbids the one workaround an agent knows — a short root under `/tmp` — and offers nothing
that works, which is how the next backup ends up outside the scratchpad again.

`dispatch.args` at `:917` gains `scratch: scratch`. `perUnit` and `resolvePathsWith` are unchanged.

### The child

`tools/workflows/unattended-unit.js` adds, after the `checklist` check at `:82`:

```js
check('scratch', 'Every temporary file this unit makes goes there, and a child that guessed a root would guess the empty $TMPDIR the parent exists to replace.')
if (String(cfg.ground).indexOf(cfg.scratch) === -1) {
  throw new Error('unattended-unit: the `ground` text names no `' + cfg.scratch + '`, so the scratch root this ' +
    'child was handed is not the one its grounding sentence tells the agent to use. The parent hands out both ' +
    'in dispatch.args; pass them together.')
}
```

Two refusals, one predicate function, and `cfg.scratch` is not a dead key: the join is what it is
for. The child's `PROMPT` opens with `cfg.ground`, so the sentence the parent built with this same
path is the first paragraph the unit agent reads, and the child adds no second copy. A caller who
composes child args by hand from the hand-out passes `ground` and `scratch` together; one who drops
either meets a refusal that names the other.

This keeps the file at exactly one top-level definition — `check` — which the codebase-map JS
liveness floor counts, and adds no loop, array method or arrow.

### The Skill

The "Drive the build as ONE program" bullet in `tools/unattended/SKILL.template.md` at `:557` gains
one sentence: the harness call carries `scratch: <your session scratchpad, absolute>` — the path
your own system prompt names, never `$TMPDIR` — and refuses without it; the child receives it in
`dispatch.args` and refuses too. The render is re-made by `bash tools/unattended/adopt-unattended.sh`.

### The renders

`tools/workflows/unattended-build.js` is re-made by `bash tools/workflows/check-protocol-parity.test.sh
--render`, in the same commit, and the parity leg byte-compares the pair. `.claude/skills/unattended/SKILL.md`
likewise.

### Inventory

One argument key, `scratch`, on two scripts; one const, `scratch`, in the parent. No function, no
verb, no conf key, no gate leg, no inventory key of any codebase-map layer, so
`memory/map/generated/` does not move.

### Files touched (estimate)

- `tools/workflows/unattended-build.template.js` and its render — the refusal, the fold, the
  sentence, the hand-out key. About twenty lines.
- `tools/workflows/unattended-unit.js` — two refusals. About ten lines.
- `tools/workflows/unattended-build.test.sh` — the arms, and `scratch` added to `UNITS`, the nine
  `*_UNITS` fixtures at `:254` to `:492`, `CHILD_ARGS` at `:551`, and the inline passing fixtures at
  `:114` to `:118` that expect a result rather than a refusal.
- `tools/unattended/SKILL.template.md` and its render; `memory/map/features/review-harnesses.md`.

### Alternatives rejected

- **The sentence twice, parent `GROUND` and child `PROMPT`, per the brief.** The child's prompt
  already opens with `cfg.ground`; a second copy is the same sentence twice in one prompt, and with
  a hand-composed dispatch it is two sentences that can name two paths. The join replaces the copy.
- **A `scratch` default of `<os.tmpdir()>/claude`.** Correct on this node, and a script with no
  filesystem and no `os` cannot compute it; a string literal would be the floating root again.
- **Validating existence.** No filesystem in a workflow script; shape is all that can be asserted,
  and a caller who passes an absolute path that does not exist meets `mkdir -p` in the agent's own
  hands, not a refusal here.
- **Exporting `TMPDIR` in the child prompt.** Refused by `TOOL-aTetheredScratch-2`'s measurement
  and by the rule that an instruction is not an enforcement; the hook is the enforcement.

## 5. Production-readiness checklist

- security — the path is embedded into a prompt string and a JSON object, both under the caller's
  control already; the fold removes the one character that breaks both. A caller may name any
  absolute path, which is the trust level `repo` already carries.
- perf / scale — one regex and one `replace` per run; nothing measurable.
- error / empty / loading states — absent, non-string, relative and backslash-only values are each
  refused or folded and named in section 6; an absent `ground` in the child is already refused by
  its own check, so the agreement test runs only over a present one.
- observability — the refusal messages name the missing or mismatched value; the sentence in every
  prompt names the path, so a transcript shows what the agent was told.
- risks — every fixture in the test double that expects `RESULT` reds until it carries `scratch`;
  that is the required-argument change doing its job, and section 6 counts it. The clone clause
  rests on one measurement on one node; a POSIX host ignores `core.longpaths` harmlessly.
- testing — section 6; the suite is on no bar leg and runs directly.
- migration — every existing caller of the harness must add `scratch`; the Skill is the only
  documented caller, and it is edited here. A caller following an older Skill meets the refusal,
  which names the argument.
- user docs — the Skill bullet and the dossier are the docs; the refusal text is the third carrier.

## 6. Acceptance criteria

The suite `tools/workflows/unattended-build.test.sh` evaluates the scripts as their runtime does,
with stub hooks that trace every prompt, and is on no bar leg, so each criterion is observed by
running it directly. `has` and `hasnt_` print `ok` or `FAIL` per assertion and the suite exits 1 on
any `FAIL`; the observation is the named line, not the exit alone.

- **AC1** — When `run_wf` is given the `UNITS` fixture without a `scratch` key, the trace ends in
  `THROW` and carries the words `must carry an explicit` followed by the key name; given `scratch`
  as a relative path such as `tmp/s`, the same refusal; given the fixture with `scratch` set to an
  absolute path, the trace ends in `RESULT`.
  Red when: the absent case yields `RESULT`, which means the refusal was written after a fixture
  gained the key and never observed red; or the relative case passes, which means the shape test
  is a truthiness test.
- **AC2** — When `scratch` is given with backslashes, the traced `prompt:spec:` line spells the
  path with forward slashes and no backslash survives in the `dispatch.args` of the `RESULT`.
  Red when: a backslash reaches either carrier.
- **AC3** — When `run_wf` runs the valid fixture, every traced `prompt:` line — the spec writers,
  `audit:record` and `dispose:` — carries `goes under /tmp/s` and `a bare mktemp, or any path
  outside the repository` and `core.longpaths=true`, so `grep -c` of `a bare mktemp` over
  `tools/workflows/unattended-build.template.js` and over `tools/workflows/unattended-build.js` is 1
  each.
  Red when: any traced prompt lacks the sentence, which means it was placed in a stage text rather
  than in `GROUND`; or the two files disagree, which `review-protocol parity (kit vs dogfood)` reds
  at the close.
- **AC4** — When the valid fixture's `RESULT` is read, its `dispatch.args` carries
  `"scratch":"/tmp/s"` beside the six existing keys.
  Red when: the key is absent from the hand-out, so a caller copying `dispatch.args` to the child
  meets the child's refusal on every unit.
- **AC5** — When `run_wf` runs `unattended-unit.js` with `CHILD_ARGS` lacking `scratch`, the trace
  ends in `THROW` naming `scratch`; with `scratch` present but a `ground` that does not contain it,
  `THROW` carrying `names no`; with both agreeing, `RESULT`, and the traced `prompt:unit:` line
  opens with the ground text. `grep -c 'function '` over `tools/workflows/unattended-unit.js` stays 1.
  Red when: a mismatched pair passes, which means the join is absent and `scratch` is a dead key;
  or a second top-level definition appears, which `codebase-map coverage + freshness` counts.
- **AC6** — When `bash tools/unattended/adopt-unattended.sh --check` and `bash
  tools/workflows/check-protocol-parity.test.sh` run after the renders, both exit 0; `grep -c
  scratch` over `tools/unattended/SKILL.template.md` is at least 1 in the harness bullet, and over
  `memory/map/features/review-harnesses.md` at least 1. `node tools/workflows/check-workflow-syntax.js`
  exits 0 over both edited scripts.
  Red when: either render drifted, or a script no longer parses in the AsyncFunction dialect.

## 7. Gates

`review-protocol parity (kit vs dogfood)` · `workflow script syntax` · `unattended skill wiring` · `verifier fan-out` · `codebase-map coverage + freshness` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `install-prefix (shipped surface)`

These are what `--close` runs, once. The pass runs none of them: it verifies with
`bash tools/workflows/unattended-build.test.sh`, which is on no leg, and reads the arms section 6
names. `verifier fan-out` is listed because it reads every `export const meta` script and the
child's shape is what keeps it out of that gate's deny set.

New arm: `tools/workflows/unattended-build.test.sh` · the absent, relative and mismatched cases of
AC1 and AC5 run against the scripts at base, where every one of them yields `RESULT`, before the
refusals land · no assertion floor exists in this suite, so none moves.

## 8. Open questions

- **FACT-QUESTION · F1 — does a clone under the session scratchpad work on Windows at all?** The
  memory note from 2026-09-03 records `git clone --local` into the scratchpad failing with
  `Filename too long` and a short root under `/tmp` as the cheaper fix, `core.longpaths` untested;
  `TOOL-aProbedUnit-5` denies `/tmp`. Probe: a local no-checkout clone of this worktree into this
  session's scratchpad, once plain and once with `-c core.longpaths=true`, reading the exit status
  and whether a pack file lands. Liveness: the plain clone must fail, or the probe measured a path
  short enough to prove nothing.
  RESOLVED (agent, 2026-09-14, delegated): the plain clone exits 128 with the recorded message and
  the `core.longpaths` clone exits 0 and leaves `pack-049c2549….idx`, measured on node `a` against
  the 170-character scratchpad. The sentence carries the working spelling; the short-root
  workaround is what unit 5 removes.
- **F2 — who bumps `unattended-build@1.0` and `unattended-unit@1.0`?** The build README gives every
  version bump to the closing pass and the brief lists unattended, memory-tree and agent-cap; the
  two `meta` versions are not on the list, and a required argument is a contract change. Options:
  this unit bumps them; the closing pass bumps them beside the three; nobody does.
  RESOLVED (agent, 2026-09-14, delegated): the closing pass, beside the three the brief names, 1.0
  to 1.1 on both, in the same commit the unattended bump lands in — the rule that a unit bumps no
  version was written for exactly the collision two units bumping one carrier would make, and the
  brief's list is an omission rather than a ruling.

## 9. Revision log

- rev-1 · 2026-09-14 · initial draft.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "hand every harness agent the session scratchpad path as a required argument"`
returned no seam that fits — its candidates are the codebase-map's own `require_adopted_root` and
`attribute_paths`, both Python and both about the map's tree, and its header prints `unscanned
layers: .sh`, which does not reach a `.js` workflow script either way. The seams this unit extends
were found by reading the two scripts and are cited by line in section 4: the `repo` and `slug`
refusals at `tools/workflows/unattended-build.template.js:171` and `:178`, `GROUND` at `:335`,
`dispatch.args` at `:917`, and the `check()` predicate at `tools/workflows/unattended-unit.js:71`.
The memory-recall hits that bind it: `TOOL-dPolishedVitrine-1`, which section 3 distinguishes from
this argument, and `TOOL-aTetheredScratch-2`, which is why no variable is set. One disagreement
with the brief, settled in section 4: the child inherits the parent's sentence through `cfg.ground`
and joins the two keys rather than restating the sentence.

Recall terms used: `scratchpad session temp dir TMPDIR empty backup fixer prompt args harness child absolute path`
