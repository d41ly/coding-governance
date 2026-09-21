**Serves:** diff-review TOOL-aBlindedTrial-2 TOOL-aBlindedTrial-3 TOOL-aBlindedTrial-4 TOOL-aBlindedTrial-5

# Closing diff review, round 2 — aBlindedTrial, the fold of round 1's seven findings

Node `a` · 2026-09-20 · Tier-2 · on `branch/spec-audit-opt-in` · adversarial fan through `tier2-review.js` (4 finder lenses → 5 skeptic batches → this synthesis). This round reviews ONLY the text the fold introduced. Every confirmed finding below was re-read at source and re-executed in this synthesis — the hook with crafted payloads on a two-tree fixture, the driver's term zero sliced verbatim and run under the state the finding names, the fold as a pure function under both platforms' `path.resolve` — before it was adjudicated. Nothing was taken from the skeptic's word alone.

**Reviewed range:** `a33237c4606dae69594c4223166d3fd6c5b929ea...HEAD` — **ROUND 2**. HEAD is `1fb5774e946c`; the base resolves (`git cat-file -t` → commit) and is round 1's HEAD. One commit, 16 files, +360/−26: `agent-cap.js` (+F1 coercion, +F2 subjects containment and `..` deny, +F5 MSYS fold, new `extractBuildSlug`), `unattended.sh` (+F3 BASE-keyed term zero with fail 53, +F4 present-but-empty → fail 52), `unattended-build.template.js` and its render (+F6 `round > 1` audit-shaped), `scratch-guard.test.sh` (F7 re-pin to 7), spec 4 rev-3, the hooks README, three test files, the round-1 record.

## Verdict: CLEAN WITH FIXES

Nothing blocks the landing. Round 1's seven findings are each closed in substance: `["spec-audit"]` is denied and the pair arm holds the hook and its callee to one answer; a cross-build relative subject and a `..` segment are denied by name; the term zero keys on the BASE derivation and refuses a disagreeing fact; a bare `spec-audit:` line takes fail 52; `round: 2` beside no declaration throws; `scratch-guard.test.sh` is green at 165/165; spec 4 §7 names the leg. The three suites the brief allows are green (456 · 260 · 165, all exit 0). What this round finds is the residue each fix left on the axis it did not test: the F2 containment reads the SLUG segment of a subject path and never its ROOT, so an absolute or `~`-rooted subject in a second checkout with the same slug is admitted — one MEDIUM, the same class F2 set out to close. The rest is LOW: the F5 fold has no platform guard (a false deny on POSIX single-letter roots, and `/tmp/…` still ENOENTs on win32 with a message that hides its cause); the F3 term zero cannot tell "derived absent" from "never derived" and prints a sentence about a BASE nobody read when item 3 refused early; and three comment headers plus one same-line note still state the pre-fold rule beside the post-fold code. Every fix here is a few lines with one or two test arms; the units are INPROGRESS, so they fold before the close.

## Review shape

Raw **14** · confirmed **12** · refuted **2** · unverified **0** · precision **0.86**.

Precision is well above the 0.5 floor §8 sets, up from 0.57 in round 1 — the fold's surface is small and the lenses were primed with round 1's record. The twelve confirmed collapse to **5 items**: four lenses reported the same defect with the same repro in three cases (ids 1 and 7 · ids 2, 9 and 11 · ids 4, 8 and 12 · ids 5, 10 and 14), and those merges are mine, at write time; the pipeline discarded no duplicates. The two refuted (ids 3 and 6) did not reach this synthesis as text, only as the count, so they are not re-adjudicated here.

Adjudicated, by item: **0 BLOCKER · 0 HIGH · 1 MEDIUM · 4 LOW** (5 items).
Adjudicated, by raw confirmed finding: **0 BLOCKER · 0 HIGH · 2 MEDIUM · 10 LOW** (12 findings; ids 1 and 7 both take the MEDIUM of the item that holds them, and every other id takes LOW).

## Run integrity

- Lenses **4/4** returned, **0 DIED**.
- Skeptic batches **5/5** returned, **0 DIED**.
- **0** contradictory verdicts demoted to unverified, **0** spurious verdicts discarded, **0** duplicates removed by the pipeline.

No stage died, so a zero in this report is evidence of absence and not of a hole. The three duplicate groups were judged by hand in this synthesis, as stated above.

What this synthesis ran, per the lens instruction: `node tools/hooks/agent-cap.js` against a two-tree fixture (`r1/memory/builds/tSA` declaring `spec-audit: 2026-09-20`, `r2/memory/builds/tSA` declaring nothing) with eight crafted payloads and against a `/tmp`-rooted fixture with three; the F5 fold extracted from the source line and run as a pure function under `path.posix.resolve` and `path.win32.resolve`; `unattended.sh:3840-3848` sliced VERBATIM with the driver's own `fact` and `fail` and run under `AUTH_SPEC_AUDIT=""` with and without a pinned fact; `bash tools/workflows/unattended-build.test.sh` — **456 arms, exit 0** (452 in round 1; +4 are the F6 arms); `bash tools/hooks/agent-cap.test.sh` — **260 passed, 0 failed** (240 in round 1); `bash tools/hooks/scratch-guard.test.sh` — **165 passed, 0 failed** (164/1 in round 1; F7 closed); `gotchas.py --for-diff a33237c4..HEAD` — 24 classes by anchor + 5 universal. The bar and the 13600 s driver suite were not run, as instructed. All suite output went to files and was grepped, never read through `tail`.

## Findings

| # | Sev | Ids | Where | What |
|---|-----|-----|-------|------|
| R1 | MED | 7, 1 | `tools/hooks/agent-cap.js:1769` (and `extractBuildSlug`, `:1738-1743`) | Containment compares the `builds/<slug>` SEGMENT and never anchors to `repo`: an absolute or `~/` subject path into another checkout with the same slug is admitted. |
| R2 | LOW | 2, 9, 11 | `tools/hooks/agent-cap.js:1775` | The F5 drive fold runs on every platform (POSIX `/w/repo` → `w:/repo` → cwd-relative ENOENT), and on win32 a `/tmp/…` repo still resolves to `C:\tmp\…` with a deny that shows the misfolded path and not the spelling that was tried. |
| R3 | LOW | 4, 8, 12 | `tools/unattended/unattended.sh:3841-3846` | `AUTH_SPEC_AUDIT=""` means both "derived absent at BASE" and "never derived": when item 3 refuses before `:1492`, item 7 prints `at BASE: (none)` or "declares no spec-audit: key" about a README nobody read. |
| R4 | LOW | 5, 10, 14 | `tools/unattended/unattended.sh:3813-3814`, `:2870`, `:2907-2908` | Three headers still say the FACT decides ("Term zero below reads that fact"; "keys its term zero on the fact's presence"; "cannot disagree with the grader") beside code that keys on BASE and refuses a disagreeing fact. |
| R5 | LOW | 13 | `tools/hooks/scratch-guard.test.sh:495` | `SG_SPAN_FLOOR=7` annotated on the same line with `eight spans`; the correct 7 rationale sits only in the paragraph below. |

### R1 — MEDIUM · the subjects rule tests the slug axis and not the root axis (ids 7, 1)

`tools/hooks/agent-cap.js:1738-1743`:

```js
function extractBuildSlug(p) {
  const parts = String(p).replace(/\\/g, '/').split('/')
  if (parts.indexOf('..') !== -1) return null
  const i = parts.indexOf('builds')
  return i === -1 || !parts[i + 1] ? null : parts[i + 1]
}
```

and `:1769` compares `extractBuildSlug(s.path) !== dir[dir.length - 1]`. That is a pure segment scan: it asks "does SOME `builds/<x>` pair in this string spell the declared slug" and never "does this path resolve under `repo`". `reviewDir`, by contrast, is anchored — `path.join(root, ...dir)` at `:1777` — so the two halves of the F2 fix are not the same test.

Reproduced in this synthesis on the two-tree fixture (payloads as object, `scriptPath` in Windows form so the join rule is quiet):

- A. control — `repo: <r1>`, subject `memory/builds/tSA/spec/s.md` → exit 0.
- B. control — `repo: <r2>` (undeclared), same relative subject → exit 2 (the README deny).
- C. `repo: <r1>`, subject `<r2 in C:/ form>/memory/builds/tSA/spec/s.md` → **exit 0, admitted**.
- D. same with the subject in `/c/…` form → **exit 0**.
- E. subject `~/memory/builds/tSA/spec/s.md` → **exit 0**.
- F. subject `memory/builds/tOther/spec/s.md` → exit 2 naming `subjects` (the fold's own deny holds).
- H. subject `../r2/memory/builds/tSA/spec/s.md` → exit 2 (the `..` deny holds).

Downstream nothing catches it: `tier2-review.js:333-336` hands each lens `git hash-object <path>` in `${repo}` and then `Read the file WHOLE`, and both accept an absolute path outside the repo. So `r2/tSA`'s specs are audited under `r1/tSA`'s declaration and the record lands in `r1` — the exact sentence the fold's new deny text uses ("would audit a build whose README this rule never read"). `tools/hooks/README.md:137-143` now states the subjects rule as closed and still says TWO LIMITS; neither it nor the header comment at `:1728-1731` declares absolute subjects out of scope, and `agent-cap.test.sh:780-787` has no absolute-path arm.

Why MEDIUM and not HIGH: it needs a same-slug `builds/` folder in a second tree. Slugs are session-minted, so that is contrived across builds — but this node's layout has it by construction (the primary tree beside every worktree), and the same-repo worktrees share one declaration only when nobody has edited it. Fail-open in this one shape, and it is the class F2 set out to close, tested on one axis. Classes: `containment-tested-one-way`, `allowlist-narrower-than-the-root-it-guards` (in the admitting direction).

**Fix.** The lazy one is the right one: a subject a direct spec-audit call carries is repo-relative by the harness's own contract (`unattended-build.template.js:1393` joins on `u.specPath`, which is repo-relative; the hook already treats `reviewDir` that way), so deny the other spellings by name. In `extractBuildSlug`, after the backslash fold: `if (q.startsWith('~') || /^([A-Za-z]:|\/)/.test(q)) return null` (q = the folded string) — an absolute or home-rooted subject is then denied by the same `subjects` sentence a `..` segment is. If an absolute subject INSIDE `repo` must stay admitted (probe G above admits it today), anchor instead: fold `repo` and compute `root` above the subjects check, and deny any subject whose `path.resolve(root, s.path)` does not start with `path.resolve(root, ...dir) + path.sep` — but that route inherits R2's MSYS-form problem for subjects, so take the deny-by-name unless G is a sanctioned shape.

**Left-shift.** Two arms in `agent-cap.test.sh`: an absolute subject into a sibling scratch tree carrying the same slug → deny naming `subjects`; a `~/` subject → deny. The README's TWO LIMITS paragraph stays true once the arm lands; today it names a limit set the rule does not meet.

### R2 — LOW · the F5 fold is unguarded by platform and narrower than the spelling it was raised for (ids 2, 9, 11)

`tools/hooks/agent-cap.js:1775`:

```js
const repo = a.repo.replace(/\\/g, '/').replace(/^\/([A-Za-z])\//, '$1:/')
```

`grep -c process.platform tools/hooks/agent-cap.js` → 0. Run as a pure function in this synthesis:

| input | folded | `path.posix.resolve('/cwd', …)` | `path.win32.resolve('C:\\cwd', …)` |
|---|---|---|---|
| `/a/b/c` | `a:/b/c` | `/cwd/a:/b/c` | `a:\b\c` |
| `/u/home/repo` | `u:/home/repo` | `/cwd/u:/home/repo` | `u:\home\repo` |
| `/w/repo` | `w:/repo` | `/cwd/w:/repo` | `w:\repo` |
| `/tmp/x` | `/tmp/x` | `/tmp/x` | `C:\tmp\x` |
| `/home/u/repo` | `/home/u/repo` | `/home/u/repo` | `C:\home\u\repo` |

Two halves. **POSIX** (ids 2, 11): a copy-installed adopter whose repo's first path segment is one letter is rewritten to a drive spelling, `path.resolve` makes it cwd-relative, `readFileSync` throws ENOENT, and the catch at `:1786` denies a DECLARED build — where the pre-fold `path.resolve(cwd, a.repo)` resolved it correctly. **win32** (id 9): the fold covers only `/<drive>/`; a repo under any other MSYS mount still falls to win32's drive-root-relative rule. Reproduced here from a Git-Bash `/tmp` cwd with a dated key at `r1/memory/builds/tSA/README.md`: `repo: /tmp/f9.gDsQ/r1` → exit 2, `C:/tmp/f9.gDsQ/r1/memory/builds/tSA/README.md could not be read … (ENOENT)`; the same tree in `pwd -W` form → exit 0; in `/c/` form → exit 0. Round 1's F5 named `/tmp/x` in its own repro and then prescribed a drive-only fold, so the fold faithfully implemented a fix narrower than the finding it closed. `MEMORY.md` records that long suites on this node run on clones under TEMP.

Both halves are fail-closed and admit nothing; the cost is a false deny of the one call Rule 0 exists to admit, on a path shape nobody typed, with a message that shows the misfolded path and not the spelling to fix. None of this repo's four nodes is POSIX, hence LOW. The F5 test arm (`agent-cap.test.sh:793`) derives `SAM` from `SAJ` with a sed that fires only on an `X:/` prefix, so on POSIX it feeds the unchanged path and cannot see the first half. Classes: `a-view-fix-trades-one-blindness-for-another`, `allowlist-narrower-than-the-root-it-guards`.

**Fix.** Gate the fold on the platform it corrects, and make the residual announce itself: `const repo = process.platform === 'win32' ? a.repo.replace(/\\/g,'/').replace(/^\/([A-Za-z])\//,'$1:/') : a.repo`, then `if (process.platform === 'win32' && repo.startsWith('/')) return renderDeny('a spec-audit Workflow call whose \`repo\` (' + JSON.stringify(a.repo) + ') is an MSYS mount path other than /<drive>/… cannot be placed from Node on Windows; pass the Windows or /<drive>/ spelling.')`. The README's `/c/…` sentence says `/tmp`-style mounts are not folded.

**Left-shift.** The hook exports nothing, so use the trick the F1 pair arm already uses: grep the fold line out of the source and evaluate it with `process.platform` overridden (`Object.defineProperty(process, 'platform', {value: 'linux'})`) feeding `/w/repo` and asserting it is left alone; and one arm on win32 with `repo` as `/tmp/<x>` → deny naming `repo` and `MSYS`, an announced skip on POSIX.

### R3 — LOW · the term zero cannot tell "derived absent" from "never derived" (ids 4, 8, 12)

`AUTH_SPEC_AUDIT=""` at `unattended.sh:782`, with the stated meaning "the pre-code audit is not owed by this build", is assigned exactly once more, at `:1492` inside `check_authorization`, after fail 6 (`:1456`) and fail 7 (`:1466`) can return. Item 3, `authorization-reachable` (`:3332`), is `[ -n "$ASHA" ] && trusted_base "$rel" && check_authorization "$slug" "$TB"`; `verb_close` runs `observe_anchor || true` (`:3201`), so an unreachable remote leaves `ASHA` empty and the chain never reaches `:1492`. The DoD loop (`:3233-3284`) grades EVERY item and only counts `unmet` — the sole `return 1` is after the loop. Item 7 then reads the global default.

Reproduced in this synthesis with `:3840-3848` sliced verbatim beside the driver's own `fact` and `fail`, `AUTH_SPEC_AUDIT` never re-assigned:

- RUN.md carrying `spec-audit: 2026-09-20` → `UNATTENDED check 53 FAILED — … the BASE derivation decides - at BASE: (none); recorded: 2026-09-20`, rc 1.
- RUN.md carrying no fact → rc 0, `DOD_OUT=specs-audited — not owed: … the build README at BASE declares no spec-audit: key …`.

Both sentences are about a README the process never read. The verdict is unaffected — item 3 is unmet and `fail 21` forbids overriding it — so nothing is admitted; but the operator reads a second refusal whose stated cause is false and points at a README key when the real cause is the refused anchor. The inner comment at `:3834` asserts the global "is populated from the README blob at BASE", which holds only when `:1492` ran. The pre-fold fact-keyed term zero did not have this ambiguity; the fold introduced it by reading a global whose "not set" and "set to empty" are the same bytes. This kit's own rule is that a probe that could not move says so. Classes: `fallback-fabricates-the-passing-value`, `degradation-known-but-unreported`.

**Fix.** Make "not derived" distinguishable: set `AUTH_SPEC_AUDIT_DERIVED=1` on the line after `:1492` (initialised empty beside `:782`), and open the `specs-audited` arm with `[ -n "${AUTH_SPEC_AUDIT_DERIVED:-}" ] || { DOD_OUT="specs-audited — not gradable: the README at BASE was not derived in this shell (authorization-reachable is unmet above)"; return 1; }` before the presence comparison, so the fail-53 sentence is only ever printed over a derivation that happened. The `unset`-default alternative (`[ -z "${AUTH_SPEC_AUDIT+x}" ]`) works too but touches every reader of the global; the flag touches two lines.

**Left-shift.** One arm in the `specs-audited` block of `unattended.test.sh`: key at BASE, fact pinned, remote unreachable at `--close` → `hit` the not-gradable text and `miss` `at BASE: (none)`. The same arm covers the fail 6/7 shapes since all three leave `:1492` unreached.

### R4 — LOW · three headers still state the pre-F3 rule (ids 5, 10, 14)

`git blame` puts all three in `85d930a9`, the pre-fold commit; the fold `1fb5774e` rewrote the body of `specs-audited` and its inner TERM ZERO comment (`:3831-3839`) and touched none of them:

- `unattended.sh:3813-3814` (the arm's own header): "which --preflight pins as the `spec-audit` fact. Term zero below reads that fact; absent, the item is MET and announces that nothing was owed." The code sixteen lines down keys on `AUTH_SPEC_AUDIT` and `fail 53`s when the fact is absent and BASE declares — so the sentence is now plainly false, and it names as the input the exact thing F3 removed (a reader trusting it expects deleting the RUN.md line to flip the verdict, which is the bypass F3 closed).
- `unattended.sh:2870` (the preflight comment): "the `specs-audited` grader keys its term zero on the fact's presence."
- `unattended.sh:2907-2908` (`print_spec_audit_line`'s header): "Reads the PINNED fact and never the README, so it cannot disagree with the grader." The grader now reads BASE; `trusted_base`'s S12 comment (`:1115`) says the derived base moves mid-run when another node lands the folder, so the preflight line and the grader CAN disagree, and fail 53 is precisely the case where they do.

Comment-only, no behavioural defect, but §7's rule that a gate's own header states what it checks is broken in the direction that matters — it names an input the gate no longer trusts — and two answers to one question sit inside one function. `memory/guides/UNATTENDED-PROTOCOL.md:343` carries a cousin of the first sentence ("which `--preflight` pins as the `spec-audit` fact; absent, MET"); it is not wrong as written because its subject is the README at BASE, but re-read it when the three above are rewritten. Class: `amendment-leaves-its-other-half-standing`.

**Fix.** `:3813-3814` → "key in its README at BASE, read by `authorization-reachable` into `AUTH_SPEC_AUDIT` in this same shell. Term zero below keys on THAT; the `spec-audit` fact --preflight pins is EVIDENCE compared against it, and a presence disagreement is fail 53. Derived absent, the item is MET and announces that nothing was owed." `:2870` → "the `specs-audited` grader compares the fact against the BASE derivation as evidence (fail 53 on a presence disagreement)." `:2908` → "Reads the PINNED fact; at --close the grader re-derives from BASE and refuses (fail 53) if the two disagree on presence."

**Left-shift.** None machine-gateable in this repo today; the compensating check is R3's arm, whose `hit` text asserts the post-fold keying in words the header must not contradict.

### R5 — LOW · one line states 7 and eight for the same floor (id 13)

`tools/hooks/scratch-guard.test.sh:495`:

```sh
SG_SPAN_FLOOR=7   # measured 2026-09-14 at base c95fe32a: eight spans between `## Step 0` and `## Step 5`
```

The F7 fold changed `8` to `7` and left the same-line comment byte-identical, so the value line annotates 7 with a justification of eight; the correct rationale (`KICK-aReplayedCard-3` restructured the Steps; 7 at `b7dee206` and every commit since) sits only in the RE-PINNED paragraph on `:496-499`. The arm behaves correctly — 165/165 green here — and the "eight" is true as history of `c95fe32a`, so nothing is false; it is the wrong half of the story on the line that owns the value, and the next reader re-pinning AC9 reads "eight" first. Class: `amendment-leaves-its-other-half-standing`.

**Fix.** `SG_SPAN_FLOOR=7   # 7 at main b7dee206 (was 8 at c95fe32a, 2026-09-14) — re-pin note below`.

**Left-shift.** None; a records edit.

## By design — not re-reported

Stated in the brief and confirmed unchanged at source; none of these is a finding.

- The two readers of one key (driver at BASE, hook at the worktree) disagreeing for exactly one uncommitted edit — `tools/hooks/README.md:144-146` still states it.
- The nested `workflow()` inside a running harness being invisible to the hook — unit 3 is that route's enforcement; its arms are green at 456.
- An unparseable `args` string admitting at the hook — the harness throws on it, so no audit runs.
- `specs-audited` staying in `DOD_CORE` — a term zero, not a set edit.

## Checklist classes run

`gotchas.py --for-diff a33237c4..HEAD` selected 24 classes by anchor + 5 universal. Produced a confirmed finding: `containment-tested-one-way` and `allowlist-narrower-than-the-root-it-guards` (R1, R2), `a-view-fix-trades-one-blindness-for-another` (R2), `fallback-fabricates-the-passing-value` and `degradation-known-but-unreported` (R3), `amendment-leaves-its-other-half-standing` (R4, R5). Checked and clean on this diff, named so a zero reads as a check: `two-answers-to-one-question` and `two-guards-one-question-two-answers` (the F1 pair arm now holds the hook and callee to one `kind` predicate; six shapes, all agree at 260/260), `fixture-passes-by-finding-nothing` (every new hook arm asserts an exit code both ways and a needle; the F3/F4 driver arms `hit` the refusal text and `miss` the pre-fold sentence), `staged-break-substitutes-a-synthetic-value` (the driver arms mutate RUN.md and the README on the fixture's own commits), `second-implementation-is-not-a-second-opinion` (the pair arm reads the callee's own `kind` line out of its source rather than restating it), `hand-named-gate-list-green-while-the-bar-reds` (spec 4 §7 now names `scratch-guard self-test`, and that suite is green), `record-without-serves-or-with-a-round-counter` (this record's filename puts the round in a non-numeric suffix and its first line binds four ids), `heredoc-escape-reaches-the-regex` (the fold's regexes are in a `.js` file, not a heredoc; this synthesis lost one backslash to an inline `node -e` and re-ran from a file). The remaining 17 selected classes were read against the diff and matched nothing in it.

## Left-shift summary

| # | Gate or documented check |
|---|---|
| R1 | `agent-cap.test.sh` arms: absolute subject into a same-slug sibling tree → deny naming `subjects`; `~/` subject → deny. README TWO LIMITS re-read. |
| R2 | `agent-cap.test.sh` arms: the fold line evaluated under an overridden `process.platform` leaves `/w/repo` alone; `repo` as `/tmp/<x>` on win32 → deny naming `repo` + `MSYS` (announced skip on POSIX). |
| R3 | `unattended.test.sh` arm: key at BASE, fact pinned, anchor unreachable at `--close` → `hit` the not-gradable text, `miss` `at BASE: (none)`. |
| R4 | Comment rewrites at `:3813-3814`, `:2870`, `:2908`; R3's arm text is the compensating check. |
| R5 | Comment rewrite at `scratch-guard.test.sh:495`. |

State at synthesis: `branch/spec-audit-opt-in` at `1fb5774e946c` · base `a33237c4606d` · `unattended-build.test.sh` 456/456 · `agent-cap.test.sh` 260/260 · `scratch-guard.test.sh` 165/165 · bar not run (by instruction) · driver suite not run whole (by instruction; the term zero was run as a verbatim slice).
