# TOOL-aEvidencedLens-2 — spec lenses probe read-only, and every spec finding carries its evidence

**Status:** CLOSED · rev-2 · 2026-10-05 · node a · Tier-2 · base 028b5cac · streams tooling · order 2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-05-prompt-TOOL-aEvidencedLens-1-1-spec-brief.md](../prompts/2026-10-05-prompt-TOOL-aEvidencedLens-1-1-spec-brief.md) | journal | TOOL-aEvidencedLens-1 TOOL-aEvidencedLens-3 TOOL-aEvidencedLens-4 TOOL-aEvidencedLens-5 TOOL-aEvidencedLens-6 TOOL-aEvidencedLens-7 TOOL-aEvidencedLens-8 TOOL-aEvidencedLens-9 TOOL-aEvidencedLens-10 TOOL-aEvidencedLens-11 |
| [2026-10-05-prompt-TOOL-aEvidencedLens-2-2-build-brief.md](../prompts/2026-10-05-prompt-TOOL-aEvidencedLens-2-2-build-brief.md) | journal | — |
| [2026-10-05-review-TOOL-aEvidencedLens-1-spec-audit-round1.md](../reviews/2026-10-05-review-TOOL-aEvidencedLens-1-spec-audit-round1.md) | spec-audit | TOOL-aEvidencedLens-1 TOOL-aEvidencedLens-3 TOOL-aEvidencedLens-4 TOOL-aEvidencedLens-5 TOOL-aEvidencedLens-6 TOOL-aEvidencedLens-7 TOOL-aEvidencedLens-8 TOOL-aEvidencedLens-9 TOOL-aEvidencedLens-10 TOOL-aEvidencedLens-11 |

<!-- /gen:spec-records -->

## 1. Goal

A spec lens may not look outside the spec set, so it cannot run the command a criterion names, grep
a consumer or time a stated goal. About two in five of the defects that got past the audit needed
exactly that evidence (measured 2026-10-05, session study). This unit lets a spec lens probe the tree
read-only under a stated policy, gives it a scratch directory to probe into, and makes every spec
finding carry the evidence it rests on, so a skeptic can re-run it.

## 2. Scope (IN)

- **S1** — The spec finding line drops "nothing outside the spec set". In its place it says every
  finding is ABOUT the spec set and its evidence may come from anywhere in `repo` at HEAD. The diff
  finding line keeps "nothing outside the diff". Observed by AC5.
  - **Readers:** by name: `tools/workflows/tier2-review.template.js` and its render
    `tools/workflows/tier2-review.js` are the only files spelling the phrase.
    by value: NO VALUE READERS because the phrase is prompt prose, and no arm or checker compares or
    counts it.
- **S2** — A PROBE POLICY block, spec kind only, is built once and placed in every spec finder prompt
  directly under its `LENS:` line. Its rules are the constant `PROBE_RULES` under §4. Observed by AC1
  and AC2.
- **S3** — `SPEC_FINDING_SCHEMA`'s finding item gains a REQUIRED string `evidence`: the command run
  and what it printed, or `read: <path>:<line>` for a finding resting on reading alone. The finding
  line asks for it and the spec JSON return line names it. `FINDING_SCHEMA`, the diff kind's, is
  unchanged. Observed by AC4.
- **S4** — A new arg `scratch`, read on the spec kind only, validated in the prelude before any
  agent. Absent, not a string, not absolute by the build harness's own shape test, carrying a control
  character, or equal to or under an absolute `repo` → `throw new Error('tier2-review: …')` naming
  the field, the legal shape and the value given. Folded to forward slashes once. The diff kind never
  reads it. Observed by AC3.
- **S5** — `inputPrint` gains `PROBE_RULES` on the spec kind only, spread so the diff kind's print
  object is unchanged. `scratch` does NOT join the print, and neither does any text interpolating it.
  Observed by AC6.
- **S6** — The `args` header comment documents `scratch` as a `name:` key. Observed by AC7.
- **S7** — The fixtures that run a spec audit carry `scratch`: the prelude `base` object and the
  whole-script `SPEC` object in `tools/workflows/tier2-review.test.sh`, and `MT_ARGS` in
  `tools/workflows/unattended-build.test.sh`. New prelude arms pin each refusal of S4 and its passing
  case, and `FLOOR_ASSERTIONS` rises by the assertions they add. Observed by AC8 and AC11.
- **S8** — `memory/map/features/review-harnesses.md` stops saying `tier2-review.js` tells its agents
  nothing about temporary files; it says a spec audit hands its lenses `scratch` and a diff review
  still does not. Observed by AC9.
- **S9** — The template and its render land in the same commit, the render regenerated, never
  hand-edited. Observed by AC10.

## 3. Non-goals (OUT)

- The skeptic re-running `evidence`, and the policy reaching the skeptic prompt — unit 3.
- `scratch` on the diff kind, and on the two drift-audit harnesses. The build rule keeps the diff
  kind's prompts and lenses still; the ask stays open for both.
- Carrying `evidence` into the ledger, the appendix, the synthesis prompt or `confirmedFindings`.
- The acquire sentence. It does not contain the phrase S1 drops, and unit 4 rewrites its moved-blob
  half, so this unit leaves it untouched.
- Enforcing read-only. The policy is an instruction; nothing here can stop a lens that ignores it.
- A command-count budget per lens. Each command is bounded; their number is not.

### Edges

- **consumes-from** `TOOL-aEvidencedLens-1` — the five-lens catalogue the policy sits under, and the
  one `REVIEW_SHAPE` bump this unit relies on rather than repeats.
- **hands-off** `TOOL-aEvidencedLens-3` — the skeptic re-runs each finding's `evidence` under the
  same read-only policy.
- **hands-off** `TOOL-aEvidencedLens-5` — the build harness's Audit stage passes its own `scratch`,
  and its prelude applies this unit's two extra refusals so it never accepts a value this harness
  refuses; until it does, that stage's spec audit is refused.
- **hands-off** `TOOL-aEvidencedLens-11` — the method's sentence that spec lenses probe read-only,
  scratch only, every command bounded, which states this unit's policy in M4.
- **hands-off** external — `TOOL-aProbedUnit-16`, the ask that every review harness hand its agents a
  scratch root, stays open for the diff kind and the two drift-audit harnesses. This unit discharges
  its spec-audit half only, so the header carries no `advances` verb across builds.

## 4. Design

### Evidence

Read at HEAD of the run branch, whose `tools/` tree equals base `028b5cac`.

- The spec finding line (template line 778) ends "No speculation, no style nits, nothing outside the
  spec set." The diff line (779) ends "nothing outside the diff". The acquire sentence (766-769) does
  not carry the phrase.
- `SPEC_FINDING_SCHEMA` (390-413) requires `file, where, severity, claim, impact, fix` per item. The
  resume probe re-emits lens files under `buildKeyedSchema(SPEC_FINDING_SCHEMA, [])` (651), so a lens
  file lacking `evidence` fails re-emission and is dispatched, which is the safe direction.
- `allFindings` spreads each finding (`{ ...f, lens, ref }`, line 812), so `evidence` reaches every
  later stage with no change here; unit 3 decides what the skeptic shows.
- The build harness refuses its `scratch` by `/^(\/|[A-Za-z]:[\\/])/` and folds backslashes once
  (`tools/workflows/unattended-build.template.js` lines 218-225). That is the shape S4 reuses.
- The owner ruling `TOOL-aProbedUnit-10` says every harness agent is handed the session scratchpad as
  a REQUIRED `scratch` and writes every temporary file under it.
- `inputPrint` (614) holds no `repo`, on purpose: a take-over from another worktree must reuse. A
  scratchpad path changes with every session, so a print holding it would make a resumed run, the
  case the key exists for, re-dispatch every lens.
- The lens DURABILITY write goes to `<git-common-dir>/review-lenses/<key>/` (784), which sits under
  `repo` on a primary checkout. A read-only rule with no exception would forbid the write the same
  prompt demands two lines later.
- The self-test's prelude arms evaluate template lines from the end of `meta` to
  `const reviewDir = a.reviewDir`, merging a shared `base` object into every arm. A spec-kind
  refusal placed in that span reds every proceeding spec arm unless `base` carries `scratch`.
- `tools/workflows/unattended-build.test.sh` RUNS the callee over `MT_ARGS`, a spec audit with no
  `scratch` (line 744). Its strict double checks top-level `required` only, so a finding double
  without `evidence` still passes, but a refused arg throws and reds every MT arm.

### The policy

Two constants beside `SEVERITY_RUBRIC`, both spec-kind data:

```js
const PROBE_RULES = [
  'Establish every claim with a read-only command, and record the command and what it printed.',
  'Run each section-6 criterion\'s own command or check when it is read-only and bounded, and record what it printed: a criterion already green before the unit is built cannot fail.',
  'Grep the consumers of every name, value or path the spec renames, retires or changes.',
  'Time a stated wall-clock goal once, when one run of it is bounded.',
  'READ-ONLY: write nothing under the repository, with ONE exception, the DURABILITY file this prompt names. Never run a command that writes the tree or the index: no --write, --render, --fix or --in-place, no git add, commit, checkout, switch, reset, restore, stash, merge, rebase, clone or worktree, and no redirect into the repository. Read another revision with git show <rev>:<path>.',
  'Every temporary file goes under the scratch directory named above, spelled absolute; never $TMPDIR, $TMP, $TEMP, /tmp or a bare mktemp.',
  'Bound every command at 120 seconds. Never run a merge bar, a *.test.sh suite or a self-test runner, a --selftest flag included.',
  'A probe that needs a write, such as a staged break, or one of the runs banned above, is DESCRIBED in the finding\'s fix as the probe the build must run. It is never performed.',
]
```

The block is built once, after `scratch` is validated, and is `''` on the diff kind:

```
PROBE POLICY — repository <repo>, scratch directory <scratch>.
- <each PROBE_RULES entry>
```

It is placed in the spec finder prompt between the `LENS:` line and the project note. The rules name
no interpolated value, so they can join the print while the header line, which carries `scratch`,
does not.

### The finding line and the schema

The spec finding line becomes: "Emit CONCRETE findings only — each needs file, where, severity
(blocker|high|medium|low), with "where" being the section address, e.g. "section 2 S5", a one-line
claim, the impact, a proposed fix, and evidence: the command you ran and what it printed, or
read: <path>:<line> for a finding that rests on reading alone. A spec finding is often the ABSENCE
of a line, so address it by section. Every finding is ABOUT the spec set; its evidence may come from
anywhere in <repo> at HEAD. No speculation, no style nits. If nothing real, return findings: []."

The spec return line becomes `Return JSON {lens:"<key>", path, findings:[{file,where,severity,claim,impact,fix,evidence}]}.`
`SPEC_FINDING_SCHEMA`'s item gains `evidence: { type: 'string' }` and lists it in `required`.

### The argument

Placed in the prelude after the subject ladder and before `const reviewDir`:

- spec kind, `a.scratch` not a string, or failing `/^(\/|[A-Za-z]:[\\/])/` → throw, saying a probing
  lens with no scratch has nowhere legal to write;
- carrying a character in `\x00-\x1f` → throw, because the value reaches a prompt line and a newline
  would start a forged one (the `specs` rule's L1 precedent in the same file);
- after folding both to forward slashes, lowercasing and dropping a trailing slash, equal to or under
  `repo` when `repo` passes the same absolute test → throw, because a lens writing there writes the
  tree. Lowercasing errs toward refusing; an 8.3 short name or a link aliasing `repo` is not seen.
- otherwise `const scratch` is the folded value; on the diff kind it is `''` and `a.scratch` is never
  read.

`inputPrint` becomes `deriveFnv1a(renderCanonical({ shape, context, …, intensity, ...(isSpec ? { probeRules: PROBE_RULES } : {}) }))`.

### The dossier sentence

`memory/map/features/review-harnesses.md`'s sentence beginning "`tier2-review.js` and the drift-audit
siblings still tell" becomes: "The drift-audit siblings, and `tier2-review.js` on a diff review, still
tell their agents nothing about temporary files; a spec audit hands its lenses `scratch`
(`TOOL-aEvidencedLens-2`)."

### Rollout

From this unit until unit 5 builds, the build harness's Audit stage calls a spec audit with no
`scratch` and is refused. Nothing lands between the two: the build lands once, at the close, and the
audit of promoted units runs after unit 5.

### Inventory

Mints the constant `PROBE_RULES` and the local `scratch`; no function, so no lexicon verb is owed. No
codebase-map inventory key moves.

### Files touched (estimate)

- `tools/workflows/tier2-review.template.js`
- `tools/workflows/tier2-review.js`
- `tools/workflows/tier2-review.test.sh`
- `tools/workflows/unattended-build.test.sh`
- `memory/map/features/review-harnesses.md`

### Alternatives rejected

- **Interpolating `scratch` into the rules and printing the whole block.** A resumed run, which has
  a new scratchpad, would get a new key and re-dispatch every lens: the durability property defeated
  by its own input.
- **A third evidence form, `described: <probe>`.** A skeptic re-running evidence cannot reproduce a
  probe nobody ran, so it would refute the finding for the wrong reason. A write-probe rides `fix`,
  and `evidence` still records what was read.
- **Warning on an absent `scratch`.** See §8 F1.

## 5. Production-readiness checklist

- security — the policy narrows what a lens may do, and S4 refuses the two `scratch` values that
  would widen it: a forged prompt line and a scratch inside the tree. Read-only is instructed, not
  enforced; a lens ignoring it can still write, as it can at HEAD.
- perf / scale — lenses now run commands, each bounded at 120 seconds, with no bound on how many. A
  spec audit's wall clock grows by what the lenses choose to probe; unit 6's yield is where that is
  priced.
- error / empty / loading states — an absent or malformed `scratch` refuses before any agent. An
  empty `evidence` string satisfies `required` and is left to unit 3's skeptic, which refutes
  evidence that does not reproduce.
- observability — the refusal names the field, the shape and the value; the block names the scratch
  directory in every spec finder prompt.
- risks — the Audit stage of the build harness is refused until unit 5 passes `scratch` (§4
  Rollout). A lens may judge a criterion's command read-only when it writes; the rule names the
  common writing flags and git verbs, and the residue is a lens's judgment.
- testing — the arms of S7; the suites run once at VERIFYING, at the main loop.
- migration — none for data. A caller of the spec kind must now pass `scratch`; the only automated
  one is the build harness, which unit 5 changes.
- user docs — the dossier sentence of S8; the method's "lenses probe read-only" is unit 11's.

## 6. Acceptance criteria

The stub run is `tools/workflows/tier2-review.js` evaluated as an AsyncFunction with recording
`agent` doubles, the shape the kit's own self-test uses, copied into a scratch script and run with
`node`. The prelude run evaluates the same template span the self-test extracts. Neither runs a suite.

- **AC1** — When the stub run evaluates `tools/workflows/tier2-review.js` over spec-audit args
  carrying `scratch: '/tmp/s'`, each of the five `find:` prompts carries `PROBE POLICY` exactly once,
  after its `LENS:` line, naming `/tmp/s`, `120 seconds`, `DURABILITY` and `--selftest`, and no
  `synth` prompt carries it. Whether a `verify:` prompt carries it is `TOOL-aEvidencedLens-3`'s,
  whose S5 places the same bytes there, so this criterion asserts nothing about `verify:`.
  Red when: the block is absent, duplicated, or placed above the brief.
- **AC2** — When the stub run evaluates the pass-start render and the new render over the same diff
  args, at round 1 with `checklist` and `specs` and at round 2 with `priorFindings`, every `find:`,
  `verify:` and `synth` prompt is byte-identical with no masking, no prompt contains `PROBE POLICY`,
  and the two `result.key` values are equal.
  Red when: the diff print object gained a key, or a diff prompt moved.
  fixture: the pass-start render is `tools/workflows/tier2-review.js` as `git show` prints it at the
  sha the pass recorded before its first edit, saved to the scratchpad.
- **AC3** — When the prelude run evaluates spec-audit args with `scratch` absent, `'tmp/s'`,
  `'/tmp/s\nX'`, `'/tmp/r'`, `'/tmp/r/'` and `'/tmp/r/sub'` beside `repo: '/tmp/r'`, and
  `'C:\\R\\x'` beside `repo: 'c:/r'`, each throws a message starting `tier2-review:` and naming
  `scratch`, and no agent is traced; `'/tmp/s'`, the sibling `'/tmp/rs'` beside `repo: '/tmp/r'`,
  and `'C:\\t\\s'` proceed, and the run handed `'C:\\t\\s'` carries `C:/t/s` on its `PROBE POLICY`
  line; a diff review handed `scratch: 7` proceeds.
  Red when: an absent `scratch` proceeds on a spec audit, a bare prefix test refuses `/tmp/rs`, or a
  missing case fold admits `C:/R/x` under `c:/r`.
- **AC4** — When the stub run's spec `find:` schema is read, its finding item's `required` lists
  `evidence`, the diff `find:` schema's does not, and the spec finder prompt's return line names
  `evidence`.
  Red when: `evidence` is optional or absent from the spec schema.
- **AC5** — When `grep -c "nothing outside the spec set" tools/workflows/tier2-review.template.js`
  runs it prints 0, `grep -c "nothing outside the diff"` prints 1, and
  `grep -c "its evidence may come from anywhere"` prints 1, over the same file.
  Red when: the old phrase survives beside the new sentence.
- **AC6** — When a copy of the render with one `PROBE_RULES` string edited is stub-run over spec
  args, its `result.key` differs from the unedited render's; and two stub runs differing only in
  `scratch` return the same `result.key`.
  Red when: the rules are not in the print, or `scratch` is.
- **AC7** — When the self-test's header predicate (every field read off the `a` alias has a `name:`
  key in the block from `// --- inputs (via Workflow` to `// S5 (TOOL-aGuardedTally-1)`) runs over
  `tools/workflows/tier2-review.template.js`, it reports no missing field.
  Red when: `a.scratch` is read and the header lacks `scratch:`.
- **AC8** — When `grep -c '"scratch":' tools/workflows/unattended-build.test.sh` runs it prints 1 or
  more, `grep -c "scratch: '/tmp/s'" tools/workflows/tier2-review.test.sh` prints 2 or more, and the
  stub run of the callee over the new `MT_ARGS` prints a `RESULT` line and no `THROW` line.
  Red when: `MT_ARGS` lacks `scratch` and the callee throws.
  permission: the two suites themselves run once at VERIFYING, at the main loop, and not in this pass.
- **AC9** — When `grep -c "hands its lenses" memory/map/features/review-harnesses.md` runs it prints
  1, and `grep -c "and the drift-audit siblings still tell their agents nothing"` over the same file
  prints 0, because the sentence now names the diff kind apart.
  Red when: the dossier still says `tier2-review.js` hands no agent a scratch root.
- **AC10** — When the template is rendered with `{{FANOUT_CAP}}` replaced by the value
  `bash tools/workflows/check-verifier-fanout.sh --print-cap` prints, the result equals
  `tools/workflows/tier2-review.js` byte for byte, and `bash tools/check-install-prefix.sh --offenders`
  prints no key naming a file this unit touched.
  Red when: the render was hand-edited, or a rule spells a kit path.
  figure: the cap is DERIVED from the hook at observation time.
- **AC11** — When `grep -c "spec scratch:" tools/workflows/tier2-review.test.sh` runs it prints at
  least 10, one arm per refusal and passing case AC3 names, where the pre-pass file prints 0, and
  `grep -o 'FLOOR_ASSERTIONS=[0-9]*' tools/workflows/tier2-review.test.sh` reads its pre-pass value
  plus the number of assertions the pass's new arms add. Both figures are written in the pass's
  commit message.
  Red when: the refusals ship with no arm, or the floor did not move by the assertions added.
  figure: DERIVED at observation time from the pre-pass file and the pass's own diff.
  permission: a pass runs no suite; the arms are read at the main loop's VERIFYING run.

## 7. Gates

`tier2-review self-test` · `unattended-build self-test` · `verifier fan-out self-test` · `review-join self-test` · `review-protocol parity (kit vs dogfood)` · `install-prefix (shipped surface)` · `workflow script syntax` · `recall floor` · `recall floor arms` · `spec tokens (a spec's own names resolve)`

New arm: tools/workflows/tier2-review.test.sh · `spec scratch:` one arm per AC3 case, the refusals of an absent, relative, multi-line, equal, trailing-slash, nested and case-folded Windows `scratch` beside the passing plain, sibling and Windows cases, against the base prelude that reads no `scratch` · `FLOOR_ASSERTIONS` raised by the assertions added
New arm: tools/workflows/tier2-review.test.sh · the spec finding schema requires `evidence`, against the base schema · `FLOOR_ASSERTIONS` raised by the assertions added

## 8. Open questions

- **F1 — Is an absent `scratch` on a spec audit refused or warned?** (a) Refuse before any agent.
  (b) Warn, run without a probe directory, and say so in RUN INTEGRITY. Option (b) briefs five lenses
  to probe with nowhere legal to write, and contradicts the owner ruling `TOOL-aProbedUnit-10` that
  every harness agent is handed `scratch` as REQUIRED. Shared invariant 4's warn-on-absent default is
  overridden here by the brief's own unit-2 paragraph. Recommend (a).
  RESOLVED (agent, 2026-10-05, delegated): (a), refuse.
- **F2 — Is `scratch` refused only by the build harness's shape, or also for a control character and
  for a path inside `repo`?** (a) Exactly the build harness's test. (b) That test plus the two
  refusals. Option (b) closes a forged prompt line and a write into the tree the read-only rule
  exists to prevent, and trips no veto: it narrows a surface. Recommend (b).
  RESOLVED (agent, 2026-10-05, delegated): (b), the shape test plus both refusals.

## 9. Revision log

- rev-1 · 2026-10-05 · initial draft, from the template, its render, both self-tests and the build
  harness's `scratch` refusal at HEAD.
- rev-2 · 2026-10-05 · §3 §7 S7 AC1 AC3 AC11 · round-1 spec audit fold. The §3 hands-off to
  `TOOL-aEvidencedLens-5` now names the refusal contract it mirrors, for that unit's id 40 fold, and
  §3 gains the hands-off to `TOOL-aEvidencedLens-11` that mirrors that unit's existing consumes-from. Id 7 (MEDIUM): AC11 counts
  the `spec scratch:` arms against the pre-pass file and checks the floor equality. Id 8 (MEDIUM):
  AC3 adds the sibling `/tmp/rs`, a trailing-slash value, a case-folded Windows pair and the folded
  value on the `PROBE POLICY` line. Id 27 (MEDIUM): AC1 no longer asserts the block is absent from
  `verify:`, which `TOOL-aEvidencedLens-3` S5 fills after this unit.

## 10. Reuse audit

Three seams are extended, none rebuilt. The `scratch` refusal and its backslash fold are the build
harness's own (`tools/workflows/unattended-build.template.js` lines 218-225, `TOOL-aProbedUnit-4`),
reused by shape. The temp-file sentence of `PROBE_RULES` is that file's `GROUND` sentence with the
clone exception dropped, because a lens clones nothing. The `evidence` field rides the existing
`SPEC_FINDING_SCHEMA` and the finding spread, so no new join or carrier is built.
`python tools/codebase-map/reuse_lookup.py "refuse an absent or relative scratch path argument"`
returned only name-stem matches such as `CensusRefused` and `deriveSidecarPath`, none a scratch
seam, and it cannot see the JavaScript template's prelude as a seam. Recall returned the owner ruling
`TOOL-aProbedUnit-10`, the `TOOL-aProbedUnit-4` spec that made `scratch` required on the build
harness, and the open ask `TOOL-aProbedUnit-16` that names `tier2-review.js` as owing the same arg;
§3 Edges records what of it this unit discharges.

Recall terms used: scratch scratchpad absolute path refuse unattended-build ground temporary files read-only probe evidence lens
