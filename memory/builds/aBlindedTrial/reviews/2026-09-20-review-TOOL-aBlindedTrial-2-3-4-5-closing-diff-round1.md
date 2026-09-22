**Serves:** diff-review TOOL-aBlindedTrial-2 TOOL-aBlindedTrial-3 TOOL-aBlindedTrial-4 TOOL-aBlindedTrial-5

# Closing diff review — aBlindedTrial, the spec audit becomes opt-in

Node `a` · 2026-09-20 · Tier-2 · on `branch/spec-audit-opt-in` · adversarial fan through `tier2-review.js` (4 finder lenses → 5 skeptic batches → this synthesis). Every confirmed finding below was re-read at source in the worktree and re-executed with a crafted payload or a suite run before it was adjudicated; nothing was taken from a spec, a commit message or the skeptic's word alone.

**Reviewed range:** `b7dee2063e3ef3d9e0a5b1ab7b31d2e6f5ecb7a3...HEAD` — **ROUND 1**. HEAD is `a33237c4`. One correction to the range as the harness spelled it: that 40-hex base does not resolve in this repository (`git cat-file -t` fails on it). The commit that does, and that every spec in the range pins as `base b7dee206`, is `b7dee206c16bf5ffdffeb2712ea0a31da17bac02` — the merge that closed `TOOL-aBlindedTrial-1`. The diff reviewed is that commit to HEAD: 5 commits, 46 files, +1415/−190, units 2–5.

## Verdict: CLEAN WITH FIXES

Nothing blocks the landing, and the product of the four units is the right shape: the driver reads the key at BASE and announces the skip, the harness refuses audit-shaped arguments beside no declaration and returns stated nulls rather than a zero, the hook fails closed on a call it cannot place, and the method text says when the audit is owed. One finding is HIGH: the hook's Rule 0 keys on strict string equality while its callee coerces with `String()`, so `kind: ["spec-audit"]` is admitted by the guard and executed as a spec audit by the harness — the one route the unit exists to close is open to a one-character payload change. Two MEDIUMs follow, both in the same family: a check whose input the subject can reach. The rest is LOW. All three of the top findings are one-line fixes with one test arm each; the units are INPROGRESS, so they fold as spec revisions before the close rather than as a follow-up build.

## Review shape

Raw **14** · confirmed **8** · refuted **6** · unverified **0** · precision **0.57**.

Precision sits just above the 0.5 floor §8 sets. The eight confirmed collapse to **7 items**: ids 1 and 4 are one defect (the `kind` coercion gap) reported by two lenses with the same repro, and are merged here. That merge is mine, at write time; the pipeline discarded no duplicates.

Adjudicated, by item: **0 BLOCKER · 1 HIGH · 2 MEDIUM · 4 LOW** (7 items).
Adjudicated, by raw confirmed finding: **0 BLOCKER · 2 HIGH · 2 MEDIUM · 4 LOW** (8 findings; ids 1 and 4 both take the HIGH of the item that holds them).

## Run integrity

- Lenses **4/4** returned, **0 DIED**.
- Skeptic batches **5/5** returned, **0 DIED**.
- **0** contradictory verdicts demoted to unverified, **0** spurious verdicts discarded, **0** duplicates removed by the pipeline.

No stage died, so a zero in this report is evidence of absence and not of a hole. The one duplicate (ids 1 and 4) was judged by hand in this synthesis, as stated above.

What this synthesis ran, per the lens instruction: `node tools/hooks/agent-cap.js` against a two-build scratch fixture with nine crafted payloads (recorded per finding); `bash tools/workflows/unattended-build.test.sh` — **452 arms, exit 0**; `bash tools/hooks/agent-cap.test.sh` — **240 passed, 0 failed**; `bash tools/hooks/scratch-guard.test.sh` — **164 passed, 1 failed** (F7); one `run_wf` probe of the harness render with `round: 2` beside no `specAudit` (F6). The bar and the 13600 s driver suite were not run, as instructed; the driver's `specs-audited` block was read at source, not executed.

## Findings

| # | Sev | Ids | Where | What |
|---|-----|-----|-------|------|
| F1 | HIGH | 1, 4 | `tools/hooks/agent-cap.js:1737` | Rule 0 tests `a.kind !== 'spec-audit'`; the callee tests `String(a.kind)`. `kind: ["spec-audit"]` passes the hook and runs a full spec audit. |
| F2 | MED | 12 | `tools/hooks/agent-cap.js:1749` | The README is placed from `reviewDir` alone; `subjects` is never read, so an undeclared build's specs are audited by naming any declared build's reviews folder. |
| F3 | MED | 2 | `tools/unattended/unattended.sh:3826` | The `specs-audited` term zero reads the run-authored RUN.md fact, not the BASE-derived `$AUTH_SPEC_AUDIT` that item 3 populated moments earlier in the same shell. |
| F4 | LOW | 5 | `tools/unattended/unattended.sh:1489` | A bare `spec-audit:` line at BASE (present, empty) falls into the `""` arm and reads as undeclared, against the comment two lines above it. |
| F5 | LOW | 13 | `tools/hooks/agent-cap.js:1748` | `path.resolve` turns an MSYS-form `repo` (`/c/...`, `/tmp/...`) into `C:\c\...`, so a DECLARED build is denied with ENOENT on a path that does not exist. |
| F6 | LOW | 11 | `tools/workflows/unattended-build.template.js:273` | `round > 1` beside no `specAudit` is not in the `auditShaped` list although it is the fourth argument that only an audit re-invoke carries. |
| F7 | LOW | 14 | `memory/builds/aBlindedTrial/spec/2026-09-20-spec-TOOL-aBlindedTrial-4.md:50-51` | Unit 4 §3 says scratch-guard's "own arms keep passing"; `scratch-guard.test.sh` is red at HEAD (pre-existing, AC9 floor 8 vs 7 spans), and §7 omits that leg. |

### F1 — HIGH · the guard and its callee disagree on what a spec-audit call IS (ids 1, 4)

`tools/hooks/agent-cap.js:1737`:

```js
if (!a || typeof a !== 'object' || Array.isArray(a) || a.kind !== 'spec-audit') return null
```

`tools/workflows/tier2-review.js:89`:

```js
const kind = a.kind === undefined ? 'diff-review' : String(a.kind)
```

Reproduced against a scratch fixture whose `tOther/README.md` carries no key. `args.kind = "spec-audit"` → exit 2 with the Rule 0 deny. `args.kind = ["spec-audit"]`, same `repo` and `reviewDir` → exit 0, admitted; the same payload with `args` as a JSON string → exit 0. `node -e "String(['spec-audit'])==='spec-audit'"` → `true`, so the harness passes its `KINDS` check, sets `isSpec`, and runs the audit. Rule 0 reads `tool_input.args` and nothing else (its own header says so), and no other rule in the hook keys on `kind`, so nothing downstream catches it. No README edit, no script edit, no shell access: the hook's whole deny branch is bypassed by a shape change inside the one field it keys on.

Why HIGH and not BLOCKER: what an admitted call buys is an undeclared spec audit — the 12× token cost the trial measured, on a build whose owner did not ask for it — not a wrong merge or a corrupted record. And the protocol's §9 already concedes that a run with shell access defeats the hook. But this route needs none, and unit 4's Goal is that the audit is *forbidden* in an attended session; as written, it is forbidden only for callers who spell `kind` as a string. Class: `two-answers-to-one-question` — one predicate ("is this a spec-audit call") with two spellings, one in the guard and one in the callee, and the guard's is the narrower.

**Fix.** Mirror the callee's coercion so the two readers agree: `String(a.kind) !== 'spec-audit'` (`String(undefined)` is `'undefined'`, so an absent `kind` still falls through). Optionally tighten the callee to `typeof a.kind === 'string'` so neither side accepts a non-string `kind` at all — the smaller surface.

**Left-shift.** One arm in `agent-cap.test.sh`: `"kind":["spec-audit"]` against the undeclared README → exit 2, as object and as string. The class-level gate is the pair itself: an arm that feeds the SAME payload to `checkSpecAuditDeclared` and to the callee's `kind` derivation and asserts they agree on `isSpec`, so a future edit to either side reds until the other follows.

### F2 — MEDIUM · the declaration is read from where the RECORD lands, not from what is AUDITED (id 12)

`tools/hooks/agent-cap.js:1741-1753` places the README as `<repo>/<parent of reviewDir>/README.md` and never reads `a.subjects`. `tier2-review.js:126-164` accepts any subject path and writes the record to `reviewDir`. The two are unlinked.

Reproduced on a two-build fixture (`tSA` declares `spec-audit: 2026-09-20`, `tOther` declares nothing):

- `{kind:'spec-audit', repo:<root>, reviewDir:'memory/builds/tSA/reviews', subjects:[{path:'memory/builds/tOther/spec/s.md', blob:'abcdef1'}]}` → exit 0.
- `{kind:'spec-audit', repo:<root>/memory/builds/tOther, reviewDir:'../../builds/tSA/reviews'}` → exit 0.
- Control: `reviewDir:'memory/builds/tOther/reviews'` → exit 2.

Downstream nothing reds. `memory/HYGIENE.md` "Record bindings" explicitly lets a record name a spec in ANOTHER build, so the misrouted `**Serves:** spec-audit <tOther ids>` record under `tSA/reviews` passes check 21, and `tOther`'s `specs-audited` at `--close` reports not-owed. `tools/hooks/README.md:127-144` states exactly TWO limits (the programmatic `workflow()` route; worktree-vs-BASE README) and claims the rule makes the audit forbidden in an attended session; this args-only route is neither stated limit. It is also plausible non-adversarially: a caller reusing a prior declared build's invocation and editing only `subjects`. Class: `inputs-inside-the-subjects-reach`, with `containment-tested-one-way` as the shape — the rule asks "is the reviews folder under a declared build" and never "are the subjects under that same build".

**Fix.** Inside the same `try`, when `Array.isArray(a.subjects)`, walk each subject path the way `reviewDir` is walked (fold `\`, split on `/`, find the index of `builds`) and deny by name unless every subject's `builds/<slug>` equals `dir[dir.length-1]`. A direct `tier2-review.js` spec audit always carries `subjects` (it refuses without them), so `reviewDir`'s parent becomes the only build the call can audit.

**Left-shift.** Two arms: cross-build subjects → deny; same-build subjects → allow. The README's "TWO LIMITS" paragraph becomes true again once the arm lands; until then it should say three.

### F3 — MEDIUM · the term zero reads the run's own record where the BASE-derived value already sits (id 2)

`tools/unattended/unattended.sh:3826`:

```sh
if [ -z "$(fact "$rel" spec-audit)" ]; then
  DOD_OUT="specs-audited — not owed: the spec audit is opt-in and the build README at BASE declares no spec-audit: key, ..."
  return 0
fi
```

`fact "$rel" spec-audit` reads RUN.md, the run-state file the run itself writes. Yet at `--close` the loop over `DOD_CORE` (`:407`) has already graded item 3, `authorization-reachable` — non-overridable, `:3310` — which calls `trusted_base` then `check_authorization "$slug" "$TB"`, and that populates the global `AUTH_SPEC_AUDIT` from the README blob at BASE (`:1478-1493`). Item 7, `specs-audited`, runs in the same shell four items later and ignores it.

Consequence: an owner commits `spec-audit: <date>` at BASE; the run deletes or blanks the one `spec-audit:` line in RUN.md before `--close`; the grader returns MET and prints a sentence claiming the README at BASE declares no key, which is false. Every unit lands with no audit evidence and no recorded `--override`. This is the deleted-`base:`-line shape the kit's own `trusted_base` header (`:1016`, "the recorded value is now EVIDENCE, never the input") and the `authorization-reachable` header (`:3311`, "RE-DERIVED, never read out of the run-state file") name as a closed bypass, re-opened one item over. Nothing cross-checks the fact: `check-unattended.sh`, `check-pass-order.sh` and `check-brief-recorded.sh` never mention `spec-audit`; `records-current` grades marker regions; `--close` does not re-preflight. The comment at `:3825` ("Keyed on the pinned fact, never on the worktree README") chose correctly against the worktree and then chose the run's record over the BASE derivation that was in hand.

MEDIUM rather than HIGH: §9 concedes a run with shell access defeats the driver's checks too, and the honest exit (`--override` with a reason) exists. But the kit's own standard for this exact class is that the record is evidence and BASE is input, and the fix is one variable already populated. Class: `inputs-inside-the-subjects-reach`; also `two-readers-of-one-config-one-re-derived` — one reader re-derives from BASE, the other reads a private copy.

**Fix.** Key the term zero on `${AUTH_SPEC_AUDIT:-}`, not the fact, and treat a disagreement between `$AUTH_SPEC_AUDIT` and `fact "$rel" spec-audit` (fact present but BASE absent, or the reverse) as a refusal with its own `fail` code, matching how `trusted_base` handles `base:`. Keep the fact as the evidence the preflight line and `--status` print.

**Left-shift.** One arm in the `specs-audited` block of `unattended.test.sh`: key at BASE, `spec-audit:` line deleted from RUN.md, `--close` must block on `specs-audited` and name the disagreement. The class-level gate is the one the file already carries for `base:`; this is the second key that owes it.

### F4 — LOW · a present-but-empty key reads as absent (id 5)

`tools/unattended/unattended.sh:1478` emits `spec-audit=` (empty) for a bare `spec-audit:` line — verified with the awk arm in isolation. `:1489` lists `""` beside the date pattern, so present-with-no-value falls through as undeclared: preflight prints `not owed (opt-in)`, and `--close`'s term zero says the README "declares no spec-audit: key", which is false for that README. The comment at `:1483-1486` says a present value that is not a date is a REFUSAL because "read as absent it would silently opt a build out that the owner meant to opt in" — this is that case, one value narrower. `gen_build_index.parse_front_matter` stores `fm['spec-audit'] = ''` without complaint, so such a README lands.

One correction to the finder's framing, which the skeptic also made: the hook's `readFrontMatterKey` (`scratch-guard.js:621`) requires `\S+`, so the hook ALSO reads the bare line as absent and denies — that deny is the designed consequence of "absent" in an attended session, not a third interpretation. The defect is the driver's `""` arm conflating key-absent with key-present-empty, and the DoD line's false claim. Class: `amendment-leaves-its-other-half-standing` — the refusal arm was written for "not a date" and the case pattern kept an escape the comment forbids.

**Fix.** Test presence separately: `printf '%s\n' "$_fm" | grep -q '^spec-audit='` — present with an empty value takes the `fail 52` branch (`declared: (empty)`); genuinely absent stays not owed.

**Left-shift.** One `hit` arm on a README carrying `spec-audit:` alone.

### F5 — LOW · an MSYS-form `repo` is a false deny of the one declared call (id 13)

`tools/hooks/agent-cap.js:1748`: `path.resolve(data.cwd || process.cwd(), a.repo)`. On win32 a leading `/` is root-relative to the cwd's drive, so `/tmp/x` and `/c/projects/x` become `C:\tmp\x` and `C:\c\projects\x`. Reproduced: a README with a dated key at a real Git-Bash path, `repo:'/tmp/tmp.pcZSjYoFbb'` → exit 2, `C:/tmp/tmp.pcZSjYoFbb/memory/builds/tSA/README.md could not be read ... (ENOENT)`; the identical Windows-form path → exit 0.

Fail-closed, so it admits nothing. But `repo` is a free-form agent-supplied string with no spelling contract (the harness header says `/abs/path/to/worktree`; spec AC1 says "a valid `repo`"), the harness's own `git -C ${repo}` runs in Git Bash and accepts MSYS form, and `scratch-guard.js:88-94, 385-386` documents that this node's corpus carries `/c/...` spellings — its `buildComparablePath` drive fold exists because a smoke test hit exactly this. Spec AC2 names "a declared build is denied" as its red condition. The hook test sidesteps the class by spelling `SAJ` via `pwd -W`. Class: `allowlist-narrower-than-the-root-it-guards` (platform path alphabet).

**Fix.** Fold before resolving: `String(a.repo).replace(/\\/g,'/').replace(/^\/([A-Za-z])\//, '$1:/')` — the replace `buildComparablePath` already carries, minus its lowercasing (an fs read must not lowercase).

**Left-shift.** One arm with `repo` in `/<drive>/...` form derived from `$SAJ` → allow.

### F6 — LOW · `round > 1` is the fourth audit-shaped argument and the list has three (id 11)

`tools/workflows/unattended-build.template.js:273` (and the render at the same line):

```js
const auditShaped = ['subjects', 'auditIds', 'subjectRound'].filter(function (k) { return a[k] !== undefined })
```

The args block (`:158`) defines `round` as "which audit round this invocation is"; the only paths that tell a caller to pass `round > 1` are audit re-invokes (`:988`, `:1318`). Reproduced with `run_wf` on the render: `OFF_UNITS` plus `"round":2` → no throw, `log:audit round 2: NOT-OWED — off by declaration ...`, `RESULT ... "round":2 ... "verdict":"NOT-OWED"`. Nothing on the OFF path consumes `round`, so the effect is nil — the hand-out is idempotent. But the comment at `:267-271` says EVERY audit-shaped argument beside no declaration is refused by name, and this one is not. Class: `amendment-leaves-its-other-half-standing`.

**Fix.** Add `a.round !== undefined && a.round > 1` to the predicate so the same throw names it.

**Left-shift.** One arm beside the three BT3-AC5 arms: `round: 2` beside no `specAudit` → THROW.

### F7 — LOW · unit 4 asserts a suite green that is red, and its gate list omits the leg (id 14)

`memory/builds/aBlindedTrial/spec/2026-09-20-spec-TOOL-aBlindedTrial-4.md:50-51`: "No change to `scratch-guard.js`'s behaviour; only the front-matter reader becomes shared, and its own arms keep passing." `bash tools/hooks/scratch-guard.test.sh` at HEAD: exit 1, `164 passed, 1 failed`, the one being `AC9 extracted 7 spans, under the floor of 8`. `SG_SPAN_FLOOR=8` at `scratch-guard.test.sh:495` was measured at `c95fe32a`; the engine's Steps 0–4 carry 7 inline `git` spans at HEAD, at the true base `b7dee206c16b`, and on `main` — so this is pre-existing and not caused by this diff.

It still binds here. `tools/gate-legs.json:253-266` lists `scratch-guard self-test` as `chunk: selftests / subject: kit` with guard `tools/hooks/`; this diff edits `tools/hooks/scratch-guard.js` (+32 lines); AGENTS.md says the `GATE_SELFTESTS=1` run is owed by a DoD for KIT work. So the leg fires on the run this unit owes and reds. The spec's §3 claim is false as written, and its §7 names `agent-cap self-test` but not the sibling leg the same guard trips. The 164 green arms include every reader-lift arm, so the lift itself is sound. Class: `hand-named-gate-list-green-while-the-bar-reds`.

**Fix.** In its own records commit: re-pin `SG_SPAN_FLOOR` to 7 with a dated reason naming `KICK-aReplayedCard-3` (which restructured the engine's Steps), or restore the dropped span in `skills/session-kickoff/SKILL.md`; add `scratch-guard self-test` to unit 4 §7; re-run and record the count so the §3 claim is observed.

**Left-shift.** The class-level check is derivable: a spec's §7 gate list must include every leg in `gate-legs.json` whose `guard` any path in the unit's §4 "Files touched" trips. Both inputs are machine-readable today; a hygiene arm or a `check-spec-tokens` sibling could red an omission at spec time rather than at the close.

## By design — not re-reported

Stated in the brief and confirmed at source; none of these is a finding.

- The two readers of one key (driver at BASE, hook at the worktree) disagreeing for exactly one uncommitted edit — `tools/hooks/README.md:141-143` states it.
- The nested `workflow()` inside a running harness being invisible to the hook — unit 3 is that route's enforcement, and its 452 arms are green.
- An unparseable `args` string admitting at the hook — the harness throws on it (`tier2-review.js:54-63`), so no audit runs.
- `DOD_CORE` and `DIRECTIVES_CORE` keeping `specs-audited` / `specs-reviewed` — a term zero, not a set edit, so no adopter floor moves; M3's veto 2.
- The dossier trims in `memory/map/features/`.

## Checklist classes run

The M6 checklist for this range (`gotchas.py --for-diff`, 50 classes: 45 by anchor + 5 universal) was run over the touched area. Classes that produced a confirmed finding: `two-answers-to-one-question` (F1), `inputs-inside-the-subjects-reach` and `containment-tested-one-way` (F2, F3), `two-readers-of-one-config-one-re-derived` (F3), `amendment-leaves-its-other-half-standing` (F4, F6), `allowlist-narrower-than-the-root-it-guards` (F5), `hand-named-gate-list-green-while-the-bar-reds` (F7). Classes checked and clean on this diff, named so a zero reads as a check and not an omission: `fixture-passes-by-finding-nothing` (the BT3 OFF arms assert positive log lines and the absence of `workflow:`; the hook arms assert exit codes both ways), `staged-break-substitutes-a-synthetic-value` (the hook arms use the shipped date shape), `degradation-known-but-unreported` (the OFF return carries `ran:false` and stated nulls, and the note predicate exempts `NOT-OWED`), `fallback-fabricates-the-passing-value` (no `0` on a path that counted nothing), `conf-value-interpolated-into-a-regex` (no conf value reaches a regex in this diff), `id-matched-as-a-substring` (`specs-audited` joins with `grep -qxF`), `fixture-removes-the-path-under-test` (the OFF fixtures strip `specAudit` and `subjects`, which is the path under test), `second-implementation-is-not-a-second-opinion` (the hook does not recompute the harness's answer; it reads a different input — which is F1's problem in the other direction). The remaining 34 selected classes were read against the diff and matched nothing in it.

## Left-shift summary

| # | Gate or documented check |
|---|---|
| F1 | `agent-cap.test.sh` arm: `"kind":["spec-audit"]` → deny (object and string). Pair arm: the hook predicate and `tier2-review.js`'s `kind` derivation agree on one payload set. |
| F2 | `agent-cap.test.sh` arms: cross-build `subjects` → deny; same-build → allow. README "TWO LIMITS" paragraph re-read. |
| F3 | `unattended.test.sh` arm: key at BASE, RUN.md line deleted, `--close` blocks on `specs-audited` naming the disagreement. |
| F4 | `unattended.test.sh` `hit` arm on a bare `spec-audit:` line → `fail 52`. |
| F5 | `agent-cap.test.sh` arm: `repo` in `/<drive>/…` form → allow. |
| F6 | `unattended-build.test.sh` arm: `round: 2` beside no `specAudit` → THROW. |
| F7 | Re-pin `SG_SPAN_FLOOR` with a dated reason; unit 4 §7 gains the leg. Candidate class gate: §7 must name every leg whose `guard` the unit's touched paths trip. |

State at synthesis: `branch/spec-audit-opt-in` at `a33237c4` · true base `b7dee206c16b` · `unattended-build.test.sh` 452/452 · `agent-cap.test.sh` 240/240 · `scratch-guard.test.sh` 164/165 (AC9, pre-existing) · bar not run (by instruction).
