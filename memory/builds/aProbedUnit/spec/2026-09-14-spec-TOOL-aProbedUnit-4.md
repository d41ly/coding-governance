# TOOL-aProbedUnit-4 — every harness agent is handed the session scratchpad, as a required `scratch` argument

**Status:** CLOSED · rev-4 · 2026-09-14 · node a · Tier-2 · base 1b000d1a · streams tooling · order 4 · ratified 2026-09-14

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-14-build-TOOL-aProbedUnit-4-1-acceptance-ledger.md](../build/2026-09-14-build-TOOL-aProbedUnit-4-1-acceptance-ledger.md) | journal | — |
| [2026-09-14-prompt-TOOL-aProbedUnit-1-1-spec-briefs.md](../prompts/2026-09-14-prompt-TOOL-aProbedUnit-1-1-spec-briefs.md) | journal | TOOL-aProbedUnit-1 TOOL-aProbedUnit-2 TOOL-aProbedUnit-3 TOOL-aProbedUnit-5 TOOL-aProbedUnit-6 TOOL-aProbedUnit-7 |
| [2026-09-14-prompt-TOOL-aProbedUnit-4-1-build-brief.md](../prompts/2026-09-14-prompt-TOOL-aProbedUnit-4-1-build-brief.md) | journal | — |
| [2026-09-14-review-TOOL-aProbedUnit-1-spec-audit-round1.md](../reviews/2026-09-14-review-TOOL-aProbedUnit-1-spec-audit-round1.md) | spec-audit | TOOL-aProbedUnit-1 TOOL-aProbedUnit-2 TOOL-aProbedUnit-3 TOOL-aProbedUnit-5 TOOL-aProbedUnit-6 TOOL-aProbedUnit-7 |
| [2026-09-14-review-TOOL-aProbedUnit-1-spec-audit-round2.md](../reviews/2026-09-14-review-TOOL-aProbedUnit-1-spec-audit-round2.md) | spec-audit | TOOL-aProbedUnit-1 TOOL-aProbedUnit-2 TOOL-aProbedUnit-3 TOOL-aProbedUnit-5 TOOL-aProbedUnit-6 TOOL-aProbedUnit-7 |

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
  below spells. The inputs block in the header comment, the contract a caller reads, gains the row
  `scratch: "<absolute session scratchpad>", // REQUIRED` beside `slug`, because a script that
  refuses without an argument its own contract does not list is the missing-carrier class. Observed
  by AC1 and AC2; the row by AC6.
- **S2** — `GROUND` carries one sentence naming that path as where every temporary file, backup,
  probe or log goes, what is never used instead, and the ONE exception with its reason: a git clone
  or a fixture repository, which needs a short path on Windows, goes under `%TEMP%/<short-name>`,
  never inside the worktree and never at a drive root. Every parent-side agent — spec writers, the
  audit recorder, the disposal agent — is prefixed by `GROUND`, so one sentence reaches all of them.
  Observed by AC3.
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
  existing fixture that reaches past the `slug` refusal gains a `scratch`, because a required
  argument reds every fixture that lacks it and that is the point. A fixture that reaches the CHILD
  gains two things, not one: `"scratch":"/tmp/s"` AND a `ground` that names it, `"G. goes under
  /tmp/s. "`, because the child's join refuses a pair that disagrees, not a pair that is merely
  incomplete — `"scratch":"/tmp/s"` beside the base `"ground":"G. "` is exactly AC5's `names no`
  THROW. Three fixtures reach the child, and the four `run_wf … "$C"` calls at `:552`, `:553`, `:577`
  and `:580` are every call that does: `CHILD_ARGS` at `:551`, which `childU` and `childA` are
  computed from and every `F2` child-prompt `has` arm reads, and the two inline fixtures at `:577`
  and `:580`, which exist to red a misspelt and an absent `mode` and would otherwise red on
  `scratch` first, because `check('scratch', …)` sits ahead of the `mode` test. The thirteen parent
  fixtures gain the key alone; the parent builds its own `GROUND`. The arms are observed by AC1 to
  AC5, one at a time; the fixture set is observed by AC7 — its grep half by the pass, its
  whole-suite half at `--close`.
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
'Every temporary file, backup, probe or log this run makes goes under ' + scratch +
', spelled absolute; never $TMPDIR, $TMP, $TEMP, /tmp, a bare mktemp, or any OTHER path outside the repository. ' +
'The ONE exception is a git clone or a fixture repository, which needs a SHORT path on Windows because that scratchpad path is long enough that a clone under it fails with Filename too long: it goes under %TEMP%/<short-name>, never inside the worktree and never at a drive root. '
```

OTHER is load-bearing: the scratchpad is itself outside the repository — section 8 F1 clones into
it under `%TEMP%` — so without the word the last clause forbids the destination the first names,
and AC3 pins the corrected bytes. The exception is the brief's, from unit 3's pass (rev-4): the
short root is spelled as the brief spells it for this node, because a workflow script has no `os`
and cannot derive `%TEMP%` from `scratch`; the `<os.tmpdir()>/claude/<short-name>` base is unit
5's to allow, and this sentence is re-spelled when that lands.

The inputs block at `tools/workflows/unattended-build.template.js:135-146` — the header comment a
caller reads the contract from — gains one row beside `slug`,
`scratch: "<absolute session scratchpad>", // REQUIRED`, because a script that refuses without an
argument its own contract does not list is the missing-carrier class S5 fixes for the Skill.

The exception is not decoration. Measured 2026-09-14 on node `a`, with this worktree as the
source and this session's 170-character scratchpad as the destination: `git clone --local
--no-checkout` exits 128 with `fatal: failed to unlink … Filename too long`. rev-3 answered that
with a `core.longpaths=true` clause, measured to exit 0 for that `--no-checkout` shape; unit 3's
pass then needed a bare fixture origin the driver runs against, found the object writes exceed
MAX_PATH under the scratchpad, and fell back to an untracked `.gov-scratch/` inside the worktree —
a path a stray `git add -A` commits. So the sentence names a short root that works for every clone
shape instead of a flag that works for one, and forbids the worktree fallback by name. Without it
the sentence forbids the one workaround an agent knows and offers nothing that works, which is how
the next backup ends up outside the scratchpad again.

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
  sentence, the hand-out key, and the `scratch: "<absolute session scratchpad>" // REQUIRED` row in
  the inputs block at `:135` to `:146`. About twenty lines.
- `tools/workflows/unattended-unit.js` — two refusals. About ten lines.
- `tools/workflows/unattended-build.test.sh` — the arms, and `scratch` added to sixteen fixture
  lines. Thirteen reach the parent and gain `"scratch":"/tmp/s"` alone: `UNITS` at `:85`, the nine
  `*_UNITS` fixtures at `:254` to `:492`, `S3` at `:385` and `S7` at `:404` — the two multi-line
  spec-stage fixtures — and the inline fixture at `:118`, which expects the `units` refusal that now
  sits behind the `scratch` one. Three reach the child and gain BOTH `"scratch":"/tmp/s"` and
  `"ground":"G. goes under /tmp/s. "` in place of `"ground":"G. "`: `CHILD_ARGS` at `:551`, and the
  two inline fixtures at `:577` and `:580`. The passing case at `:124` runs `$UNITS` and is not a
  fixture line of its own. Every line number is the file at base; `grep -c scratch` over it prints
  0 there, which is why AC7's floor of 16 is a floor and never a coincidence.
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
- risks — every fixture in the test double that reaches past the `slug` refusal reds until it
  carries `scratch`, and a child fixture reds a second time until its `ground` names the path; that
  is the required-argument change doing its job, and AC7's whole-suite run at the close is what sees
  every one of them, because the pass's single arms see only the fixtures they name. The clone
  exception spells `%TEMP%`, this node's short root; a POSIX host has no such variable and no
  MAX_PATH either, so the exception is inert there and the first clause governs.
- testing — section 6, one arm at a time against the sourced preamble; the whole suite is AC7's
  `--close` half, and no pass runs it.
- migration — every existing caller of the harness must add `scratch`; the Skill is the only
  documented caller, and it is edited here. A caller following an older Skill meets the refusal,
  which names the argument.
- user docs — the Skill bullet and the dossier are the docs; the refusal text is the third carrier.

## 6. Acceptance criteria

`tools/workflows/unattended-build.test.sh` evaluates the scripts as their runtime does, with stub
hooks that trace every prompt. The PASS never runs it whole — the build-level rule — and it is on no
bar leg either, so the whole-suite run is the close's compensating check, owned by AC7. A pass observes
ONE ARM AT A TIME: from a shell whose working directory is `tools/workflows`, source the suite's
preamble, `sed -n '1,/^# ---- AC2: THE ARGS GUARD/p' unattended-build.test.sh` — lines 1 to 105 at
base, which define `run_wf`, `has`, `hasnt_`, `UNITS`, `returns`, `$C` and every other helper and
run no arm; `CHILD_ARGS` sits at `:551`, past the marker, so AC5 pastes that one literal into the
shell itself — then `run_wf` the named fixture and read the trace it prints. The working
directory matters: sourced, `$0` is the shell, so `HERE` resolves from the cwd, and from anywhere
else the preamble's own `exit 2` guard closes the shell. `has` and `hasnt_` print `ok` or `FAIL` per
assertion; the observation is the named trace line, never an exit status.

- **AC1** — When `run_wf` is given a copy of `UNITS` with its `scratch` key deleted, paired with
  `"$(returns CONVERGED 0)"`, the trace ends in `THROW` and the line carries `must carry an explicit`
  followed by `scratch`; given the copy with `"scratch":"tmp/s"`, a relative path, the same `THROW`;
  given `UNITS` as landed, with `"scratch":"/tmp/s"`, the trace ends in `RESULT`.
  Red when: the absent case yields `RESULT`, which means the refusal was written after a fixture
  gained the key and never observed red; or the relative case passes, which means the shape test
  is a truthiness test.
- **AC2** — When `run_wf` is given the copy with `"scratch":"C:\\tmp\\s"` — two backslashes each in
  the JSON, one each once parsed — the traced `prompt:spec:tB:` line spells `goes under C:/tmp/s`
  and the `RESULT` line's `dispatch.args` carries `"scratch":"C:/tmp/s"`, and `hasnt_` finds neither
  `C:\tmp` on a `prompt:` line nor `C:\\tmp` in the `RESULT`, the spellings an unfolded value takes
  in each carrier.
  Red when: a backslash reaches either carrier.
- **AC3** — When `run_wf "$UNITS" "$(returns CONVERGED 0)"` runs, every traced `prompt:spec:tB:`
  line and the `prompt:audit:record:r1:` line carry `goes under /tmp/s`, `a bare mktemp, or any
  OTHER path outside the repository` and `goes under %TEMP%/<short-name>, never inside the worktree`,
  and none carries `any path outside`, the pre-fold bytes, nor `core.longpaths`, the rev-3 clause
  the exception replaced; and when `run_wf "$UNITS" "$(returns NON-CONVERGENT 2 '{"disposed":false,"standing":["b1"],"summary":"x"}')"`
  runs — the fixture that spawns the disposal agent, which `CONVERGED` skips — the
  `prompt:dispose:tB:` line carries the same three. The `audit:subjects:` prompt is not traced under
  `UNITS`, which supplies `subjects`; it opens with `GROUND` like the other three, and that is read
  in the source rather than the trace. `grep -c 'any OTHER path outside the repository'` over
  `tools/workflows/unattended-build.template.js` and over `tools/workflows/unattended-build.js`
  prints 1 each; the byte parity of the pair is `review-protocol parity (kit vs dogfood)`, observed
  at --close.
  Red when: any traced prompt lacks the sentence, which means it was placed in a stage text rather
  than in `GROUND`; or `any path outside` reappears, the clause that forbade its own destination; or
  the exception is absent, so the sentence forbids the worktree fallback's only alternative; or
  the two files disagree, which the parity leg reds at the close.
- **AC4** — When the `RESULT` line of the `CONVERGED 0` run in AC3 is read, its `dispatch.args`
  carries `"scratch":"/tmp/s"` beside `repo`, `slug`, `mode`, `driver`, `ground` and `checklist`.
  Red when: the key is absent from the hand-out, so a caller copying `dispatch.args` to the child
  meets the child's refusal on every unit.
- **AC5** — When `run_wf "$(printf "$CHILD_ARGS" unattended)" '{}' "$C"` runs with the `CHILD_ARGS`
  literal from `:551` pasted in as it stands at base, lacking `scratch`, the trace ends in `THROW` carrying `must carry an explicit`
  followed by `scratch`; with `"scratch":"/tmp/s"` added and `"ground":"G. "` unchanged, so the ground
  names no such path, `THROW` carrying `names no`; with `"ground":"G. goes under /tmp/s. "` and
  `"scratch":"/tmp/s"` together, `RESULT`, and the traced `prompt:unit:A-tB-1:` line opens with that
  ground text. `grep -cE '^(async )?function ' tools/workflows/unattended-unit.js` stays 1 — the
  anchored form, the definition scan the codebase-map JS layer performs, because the unanchored
  `grep -c 'function '` prints 2 at base, line 4 being a comment, and would red the correct file.
  Red when: a mismatched pair passes, which means the join is absent and `scratch` is a dead key;
  or the anchored count moves, a second top-level definition, which `codebase-map coverage +
  freshness` also counts, observed at --close.
- **AC6** — When `grep -c scratch` runs over `tools/unattended/SKILL.template.md`, over
  `.claude/skills/unattended/SKILL.md`, over `memory/map/features/review-harnesses.md`, over
  `tools/workflows/unattended-build.template.js` and over `tools/workflows/unattended-build.js`, each
  prints at least 1, and the Skill's hit sits in its "Drive the build as ONE program" bullet; every
  one of the five prints 0 at base, measured 2026-09-14 on node `a`, which is the staged red. And
  when `grep -cF 'scratch: "<absolute session scratchpad>"'` runs over
  `tools/workflows/unattended-build.template.js` and over `tools/workflows/unattended-build.js`, each
  prints exactly 1 — the inputs-block row S1 names, at `:135` to `:146` at base — and 0 at base,
  re-measured 2026-09-14 on node `a`; the plain `grep -c scratch` cannot see this row, because the
  refusal line alone takes that count from 0 to 1. The
  leg halves — `bash tools/unattended/adopt-unattended.sh --check`,
  `bash tools/workflows/check-protocol-parity.test.sh` and `node tools/workflows/check-workflow-syntax.js`
  exiting 0 after the renders — are the argv of `unattended skill wiring`,
  `review-protocol parity (kit vs dogfood)` and `workflow script syntax` verbatim, so each is
  observed at --close and never by the pass.
  Red when: a count prints 0, which means a carrier was skipped; or the fixed-string count prints 0
  with the refusal landed, which is the contract row omitted with every other carrier green; or it
  prints 2, the row duplicated; or, at the close, either render drifted, or a script no longer
  parses in the AsyncFunction dialect.
- **AC7** — When `grep -c scratch tools/workflows/unattended-build.test.sh` runs at the landed tip,
  it prints 16 or more — the sixteen fixture lines Files touched enumerates, 0 at base, measured
  2026-09-14 on node `a` — and each of `grep -cF 'scratch: the parent REFUSES args with no scratch'`,
  `grep -cF 'scratch: the parent REFUSES a relative scratch'`,
  `grep -cF 'scratch: a backslash scratch is folded before it reaches a prompt'` and
  `grep -cF 'scratch: the child REFUSES a ground that names no scratch'` over the same file prints
  at least 1, the labels of the four staged-red arms section 7 names, each 0 at base because the
  word itself is. That is the pass's half. And when `bash tools/workflows/unattended-build.test.sh`
  runs whole at the landed tip, redirected to a file and never read through `tail`, the file holds
  no `FAIL` line and its `--- <n> arms` line reads 237 plus the arms added — this unit's, and the
  arms units 1, 2, 6 and 7 land in the same file before the close. Observed at `--close`; its
  ledger row reads `observed at --close`.
  Red when: the count is below 16, which is a fixture left without the key and a whole-suite red the
  pass cannot see; or a label count prints 0, which means the arm was pasted into a shell and never
  landed in the file; or, at the close, a `FAIL` line — a fixture without `scratch`, a child fixture
  whose `ground` names no `/tmp/s`, or an inline `mode` fixture now refusing on the wrong key; or
  the arms line reads 237, which means no arm landed and the count was read off this spec.
  figure: 16 is PINNED, counted at base on 2026-09-14; the arm count is DERIVED from the suite's
  own `--- <n> arms` line at the close, and 237 is `TOOL-aProbedUnit-7`'s measurement at
  `270611cd`, PINNED as the base.
  cost: 335 s at that measurement; the suite is on no bar leg and is `--close`'s one direct run.
  permission: the whole-suite half is forbidden to a pass by the build-level rule; the close runs it
  once, and the pass observes the greps alone.

## 7. Gates

`review-protocol parity (kit vs dogfood)` · `workflow script syntax` · `unattended skill wiring` · `verifier fan-out` · `codebase-map coverage + freshness` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `install-prefix (shipped surface)`

These are what `--close` runs, once, over the whole build. The PASS runs none of them and no
suite: it observes the single-arm runs AC1 to AC5 describe against the sourced preamble, and the
grep halves of AC3, AC5, AC6 and AC7. The leg halves — AC3's byte parity, AC5's definition count
under the map leg, AC6's three commands, AC7's whole-suite run — are the close's, and their ledger
rows read `observed at --close`. `verifier fan-out` is listed because it reads every `export const
meta` script and the child's shape is what keeps it out of that gate's deny set.

`tools/workflows/unattended-build.test.sh` is on NO bar leg: no row in `tools/gate-legs.json`
names it, read 2026-09-14, so neither `GATE_FULL=1` nor `GATE_SELFTESTS=1` reaches it, and the
build-level rule forbids a pass running it whole. The compensating check is one direct run at the
close, whole, redirected to a file and never read through `tail`, and AC7 is the criterion that
owns it, so the ledger has a row to mark; `TOOL-aProbedUnit-7` measured it at 237 arms and 335 s
at `270611cd` on node `a`, and the suite's own `--- <n> arms` line is the figure once this unit's
arms are in. That run is what sees every fixture this unit's required argument reds — the thirteen
parent fixtures and the three child ones Files touched enumerates — because the pass's single arms
see only the fixtures they name, and a child fixture with the key but the base `ground` reds there
on the join, which no pass arm loads.

New arm: `tools/workflows/unattended-build.test.sh` · the absent, relative and mismatched cases of
AC1 and AC5, and the backslash case of AC2, each run as one arm against the scripts at base, where
the first three yield `RESULT` and the fourth spells a backslash, before the refusals and the fold
land; their labels are the four fixed strings AC7 greps, each opening `scratch:` · no assertion
floor exists in this suite, so none moves.

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
- rev-2 · 2026-09-14 · S6 · §4 · §5 · §6 · §7 · AC1 AC2 AC3 AC4 AC5 AC6 · folded round-1 clusters
  A (ids 1, 20: the per-arm observation form, the whole-suite run made the close's), J (id 25:
  `any OTHER path outside the repository`, AC3's token), R (id 42: the anchored definition grep),
  S (id 44: the inputs-block row); corrected the inline-fixture lines in Files touched to `:118`
  and `:124` while verifying them.
- rev-3 · 2026-09-14 · S1 · S6 · §4 Files touched · §5 · §6 · §7 · AC6 AC7 · folded round-2
  clusters C (ids 11, 26: a child fixture gains `scratch` AND a `ground` naming it), D (id 4: AC7,
  the suite's whole run given its own row), J (id 8: the inputs-block row's fixed-string grep, and
  S1 names the row). While verifying: the two inline child fixtures sit at `:577` and `:580`, not
  the audit's `:571` and `:573`; `S3` at `:385` and `S7` at `:404` reach past the `slug` refusal and
  were unlisted; `:124` runs `$UNITS` and is no fixture line, so the set is sixteen, not thirteen.
- rev-4 · 2026-09-14 · S2 · §4 · §5 · §6 AC3 · M2 AMEND from unit 3's pass, carried by this unit's
  build brief: the `core.longpaths=true` clone clause becomes the ONE exception — a git clone or a
  fixture repository goes under `%TEMP%/<short-name>`, never inside the worktree and never at a
  drive root — because F1's measurement covered a `--no-checkout` clone alone and unit 3's bare
  fixture origin exceeded MAX_PATH under the scratchpad regardless, falling back to an untracked
  dir inside the worktree. `throwaway clone` leaves the first clause's list, since the exception
  now owns clones. AC3's third token is the exception's bytes; `core.longpaths` joins its
  must-not list. F1 stays RESOLVED: its observation is unchanged, its consequence moved.

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
