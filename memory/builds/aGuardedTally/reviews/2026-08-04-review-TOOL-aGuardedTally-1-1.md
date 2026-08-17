# Closing Tier-2 review — TOOL-aGuardedTally-1 as BUILT

**Serves:** diff-review TOOL-aGuardedTally-1

**Review root:** `C:/projects/coding-governance` (resolved `git rev-parse --show-toplevel`)
**Head:** `02b1af4` — *feat(memory-tree): adopt the reuse audit as spec section 10, date-gated and enforced*
**Diff reviewed:** `c47b5d2..02b1af4` — the cumulative aGuardedTally landing (spec c47b5d2, rev-2 2f2d122, target pin 1baf679, port cab03ee, reuse-audit adoption 02b1af4)
**Spec under review:** `memory/tooling/builds/2026-08-03-TOOL-aGuardedTally/spec/2026-08-03-spec-aGuardedTally-1.md` (**Status: CLOSED · rev-3**)
**Date:** 2026-08-04 · Tier-2 closing review

**Tally: 1 blocker · 5 high · 5 medium.**

---

## Verdict up front

**S1 holds. S2 does not. S5 holds only for the failure it was written against, not the failure class it names.**

| Deliverable | Built? | Verdict |
|---|---|---|
| S1 — a dead lens never reads as a clean review | Partly | Correct on the two empty-result paths; **absent from the path that produces a report** (H1) |
| S2 — a finding with no verdict is UNVERIFIED, never refuted | **No** | Unbuilt. The guard carries FINDER counts, which are 0 in exactly the failure it must catch (**B1**) |
| S5 — parse JSON args, require an explicit repo | Partly | The parse + presence guard is real and closes the observed incident. The *verify* half and AC5's refuse-on-disagreement half are unbuilt (H2), and the report still cannot name its root (M4) |
| S3 — domain-rules §14, five gate-discipline rules | Yes | Landed. Also the bar that three findings below are measured against — and fail |
| S4 — `ps-hygiene.py` + `--selftest` | Built, **wired to nothing** | The file exists; no leg, no CI, no adopt script, no doc references it (H3). Two false-positive classes in the predicate (M2) |
| Reuse-audit adoption (§10 + check 12 date-gate) | Partly | The dogfood template and the gate moved; **the deployable kit template did not** (H4). The gate's excerpt is blank for the new failure mode (M1) |

**Can every new check actually FAIL?** No, and this is the through-line of the review.
`ps-hygiene.py` cannot fail anything — it is on no leg and there are zero `.ps1` files in the tree, so
its only observable behaviour is a green line produced by scanning nothing. The three new
`tier2-review.js` outcome strings (`UNVERIFIED` / `partial` / `clean`) have never been observed
failing: `tools/workflows/` contains only `tier2-review.js`, `gate-legs.json` has no workflow leg,
and the build folder has no `build/` or `reviews/` subfolder recording a manual run. Check 12's new
ten-section canon does fail — but with a blank diagnostic (M1). This is precisely the bar §14 of
`parallel-coding-governance.domain-rules.md` sets in the same diff: *"a new gate is not landed until
its failing case has been observed."* The diff that introduces the rule does not meet it.

**Does the spec match what was built?** Not at the CLOSED status it now carries. AC4 is verbatim
unbuilt (B1). AC5's second clause is unbuilt (H2). §7 describes a fixture harness that does not
exist and cites AC5 where it means AC6, a mis-citation §9 rev-2's own renumber note explains (M5).

---

## BLOCKER

### B1 — The verify stage still counts an ABSENT verdict as a refutation

**`tools/workflows/tier2-review.js:197`** (and `:200-201`, `:210-217`)

```js
for (const r of verdictResults.filter(Boolean))        // :197 — dead batches dropped, uncounted
  for (const v of r.verdicts || []) verdictByRef[v.ref] = v
const confirmed = allFindings.filter((f) => verdictByRef[f.ref]?.verdict === 'confirmed')   // :200
const refuted = allFindings.length - confirmed.length                                        // :201
```

A finding whose skeptic batch died — or whose `ref` the skeptic did not echo byte-identically — has
no entry in `verdictByRef`, fails the `=== 'confirmed'` test, and is booked into `refuted` by
subtraction. `verdictResults.filter(Boolean)` drops dead batches with **no counter anywhere**: a
repo-wide grep for `lensesDead` / `UNVERIFIED` returns only `:157`, `:161`, `:162`, all computed
from `finderResults`.

**Impact.** With all four lenses alive and every skeptic batch dead, the harness returns
`confirmed: []`, `refuted: N`, `lensesDead: 0`, `precision 0.00`, `report: null`, and the bare note
`'all findings refuted'` — no degradation marker of any kind. A run with 20 real findings from four
healthy lenses reports a clean bill from a stage that judged nothing. That is the identical
absent-result-counted-as-negative-result class this whole unit exists to kill, moved one stage
downstream. S2's own comment claims to close it (*"a refutation reached with dead skeptics is not a
refutation"*) but carries only LENS counts, which are `0` in exactly this path. AC4 — *"When a
finding reaches the verify stage and no verdict comes back, it is recorded UNVERIFIED, not
refuted"* — is unbuilt while the spec header reads `CLOSED · rev-3` and §9 rev-3 claims
*"BUILT. S1/S2/S5 in tier2-review.js"*. The spec's own §4 Inventory names this as one of the two
known instances of the class.

**Fix.** Mirror S1 one stage down:

```js
const liveVerdicts = verdictResults.filter(Boolean)
const skepticsDead = batches.length - liveVerdicts.length
for (const r of liveVerdicts) for (const v of r.verdicts || []) verdictByRef[v.ref] = v

const confirmed  = allFindings.filter((f) => verdictByRef[f.ref]?.verdict === 'confirmed')
const refuted    = allFindings.filter((f) => verdictByRef[f.ref]?.verdict === 'refuted')
const unverified = allFindings.filter((f) => !verdictByRef[f.ref])
```

Count `refuted` explicitly rather than by subtraction. Compute precision over judged findings only.
Return `unverified` and `skepticsDead` in **every** return shape. Never emit the bare
`all findings refuted` note when `unverified.length > 0 || skepticsDead > 0` — emit
`UNVERIFIED: <n> findings never judged (<d>/<k> skeptic batches died)`.

**Left-shift gate.** `tools/workflows/tier2-review.test.mjs`, wired as a `gate-legs.json` leg: stub
`agent()` to drive four cases and assert the returned `note` — (a) all lenses dead → `UNVERIFIED`;
(b) 2/4 lenses dead, survivors clean → `partial`; (c) findings present, **all skeptic batches
return null** → note contains `UNVERIFIED`, `refuted === 0`, `unverified === allFindings.length`;
(d) one skeptic echoes a mangled ref → that finding lands in `unverified`, not `refuted`. Case (c)
must be seen RED against current `main` before the fix lands. The sibling
`tier2-review-indexed.js` in the upstream repo already implements the index-keyed join — port it
rather than re-deriving it.

---

## HIGH

### H1 — The report-producing return path drops every S1/S2 signal

**`tools/workflows/tier2-review.js:248`**

```js
return { confirmed: confirmed.length, refuted, precision,
         agents: LENSES.length + batches.length + 1,
         report: synth?.path || null, summary: synth?.summary || '' }
```

`root`, `lensesRun` and `lensesDead` are carried on all three early-exit returns (`:163-166`,
`:173`, `:211-217`) and on **none** of the terminal one — the only path that actually emits a
report. `agents` is computed from `LENSES.length`, so dead lenses are counted as agents that ran.

**Impact.** The common degraded case — 3 of 4 lenses die, the survivor finds one confirmed bug —
produces a normal-looking report and a return object byte-indistinguishable from a full four-lens
review, reporting four finder agents. AC2's *"names the dead count"* holds only when the survivors
find nothing, so the AC as worded does not rescue this. S1 states *"the return shape gains
`lensesRun` and `lensesDead`"* unqualified. The computed `lensesDead` is never read by the path
that matters.

**Fix.** Add `root: repo, base, head, lensesRun: liveResults.length, lensesDead` to the terminal
return; compute `agents` from `liveResults.length + liveVerdicts.length + 1`; set
`note: \`partial: ${lensesDead}/${LENSES.length} lenses died\`` when `lensesDead > 0`, and pass that
caveat into the synth prompt so the written report carries it too.

**Left-shift gate.** In the same fixture harness: a case with 3 dead lenses + 1 confirmed finding
asserts the returned object has `lensesDead === 3` and `note` matching `/^partial:/`. Plus a
structural assertion that every `return` statement in the module carries the same key set — cheap,
and it catches the next path added.

---

### H2 — The S5 guard checks that `repo` is PRESENT, never that it resolves

**`tools/workflows/tier2-review.js:53`**

```js
if (!cfg || typeof cfg !== 'object' || Array.isArray(cfg) || !cfg.repo) { throw ... }
```

Presence and JSON shape, nothing more. Grepping `tools/workflows/` for `rev-parse` / `cwd` /
`process.cwd` returns only the two refusal-message strings — nothing resolves a cwd root or compares
it to `repo`. Sixteen sibling scripts in this repo do a `rev-parse` check; this one does not.

**Impact.** A present-but-wrong `repo` (stale path, wrong worktree, typo) makes every
`git -C ${repo} diff ${base}...${head}` inside all four lens agents produce nothing. The agents
complete normally and honestly return `findings: []`, so lines `:168-174` take the
`lensesDead === 0` branch and emit `clean: 0 findings` — the identical false-clean S1 was built to
close, now reached through a hole S5 leaves open and structurally invisible to S1 because all four
lenses are alive. S5 as specced is *"resolve, state and **verify** its review ROOT"*; AC5 demands
*"when the harness is given an explicit review root that differs from its resolved cwd root, it
refuses and names both."* The "state" half exists (`:69`). The verify/refuse half does not. The two
live misdirected runs are prevented only for the exact `args`-is-prose shape.

**Fix.** Before Phase 1 fan-out:

```js
const top = sh(`git -C ${repo} rev-parse --show-toplevel`)   // throws naming repo on failure
for (const ref of [base, head]) sh(`git -C ${repo} rev-parse --verify ${ref}`)
log(`review root: ${top} — diff ${base}...${head} (${sh(`git -C ${repo} rev-parse --short ${head}`)})`)
```

Throw naming the supplied root, the resolved toplevel and the failing ref. Implement the
disagreement arm: compare `top` against the process cwd's toplevel (normalising separators — MSYS
vs PowerShell differ) and refuse naming both, per AC5.

**Left-shift gate.** Fixture cases asserting the harness throws for (a) a `repo` pointing at a
non-existent path, (b) a `repo` pointing at a real directory that is not a git worktree, (c) a
valid `repo` with a bogus `base` ref. Note the `git -C <dir>` parent-discovery trap already in the
recurring-bug-classes catalog: case (b) must assert `--show-toplevel` **equals** the supplied path,
or discovery walks up and returns the parent repo with exit 0.

---

### H3 — `ps-hygiene.py` is wired to nothing; the S4 check cannot fail anything

**`tools/gate-lint/ps-hygiene.py:1`** · **`tools/gate-legs.json:19`**

`grep -rIn 'ps-hygiene|gate-lint'` across the repo hits only the file itself, its own print strings,
one spec line, the prompt doc, and a stale `.pyc`. `tools/gate-legs.json` — this repo's own single
source of legs, parsed by `tools/run-gates.sh:40` — has 19 legs and no `gate-lint` entry. There is
no `.github` directory at all, so no CI path either. No `adopt-*.sh` references it.
`grep -c gate-lint` is 0 in `README.md`, `WIRE-INTO-PROJECT.md`, `AGENTS.md` and `CLAUDE.md`, while
the README documents every sibling kit (memory-tree, codebase-map, pytest-parallel-guardrails,
hooks, workflows).

**Impact.** Neither the scan nor `--selftest` ever executes on the merge bar, while **every**
sibling kit selftest IS a leg (`tools/settings-merge.py --selftest`, `tools/codebase-map/selftest.py`,
`tools/memory-recall/selftest.py` at legs 17/18/19) — so the omission is not a convention. Run on
this tree it prints `ps-hygiene: OK — 0 .ps1 file(s) clean`, exit 0: a green line produced by
scanning nothing, which is the *"a skip must announce itself — a skip that looks like a pass is
indistinguishable from coverage"* rule of domain-rules §14, violated by the tool §14 was written
for. The kit is deployed to other repos and is undiscoverable to any adopter, so it will not run
there either. §3's non-goal (*"The inCMS gate runners, gate-legs.json, the slot pool and the pg
autowire. Project-specific."*) is about not porting inCMS's runner machinery into the kit; it does
not excuse the absence from **this** repo's own leg manifest, nor the README/WIRE absence.

**Fix.** Add two legs to `tools/gate-legs.json`:

```json
{ "name": "ps-hygiene selftest", "argv": ["python3", "tools/gate-lint/ps-hygiene.py", "--selftest"] },
{ "name": "ps-hygiene scan",     "argv": ["python3", "tools/gate-lint/ps-hygiene.py", "."] }
```

Document the tool in `README.md` and `WIRE-INTO-PROJECT.md` alongside the sibling kits, add it to
the `watch:` list in `.claude/SESSION-KICKOFF.md`, and make `main()` print
`SKIP — no .ps1 files found` rather than `OK` when `scanned == 0`.

**Left-shift gate.** The legs above *are* the gate. Observe the scan RED once by staging a `.ps1`
containing `$Foo` and `$foo`, then unstage it — §14 requires the failing case be seen, not assumed.

---

### H4 — §10 landed only in the dogfood template; the DEPLOYED kit template still says nine

**`tools/memory-tree/SPEC-TEMPLATE.template.md:6`** (and `:124`)

At `1baf679`, `diff --strip-trailing-cr tools/memory-tree/SPEC-TEMPLATE.template.md memory/TEMPLATE-SPEC.md`
is byte-identical. At HEAD they differ by exactly the `## 10. Reuse audit` block plus the
nine-vs-ten sentence: commit `02b1af4` added §10 to `memory/TEMPLATE-SPEC.md` (the dogfood copy) and
not to the kit source. The kit template's line 6 still reads *"exactly the nine canonical `##`
sections"*, its skeleton ends at `## 9. Revision log` (line 124 of 128), and
`adopt-memory-tree.sh:40` is `cp "$HERE/SPEC-TEMPLATE.template.md" "$M/TEMPLATE-SPEC.md"` — copied
verbatim. The script's tail (line 71) then tells the adopter to wire the very gate that demands ten.

**Impact.** Every repo adopting this kit installs a nine-section template beside a
`check-memory-hygiene.sh` that reds any Tier-2 spec dated ≥ `2026-08-04` for a section the shipped
template never names — and check 12's failure message points the reader back at that same
nine-section file. This is the *"template prescribes a shape its own gate rejects"* class, in the
source→generated direction. Nothing gates the pair: `hygiene-parity.test.sh` is a before/after
engine byte-identity harness and is explicitly *not* a gate leg; `check-kit-versions.sh` pairs
version constants with markers in `HYGIENE.template.md` and the recall README only.

*Correction to one sub-claim:* re-running `adopt-memory-tree.sh` in **this** repo would **not**
revert §10 — the script exits early on the `gov:kit memory-tree@1.4` marker at
`memory/HYGIENE.md:1` (`adopt-memory-tree.sh:31`). Fresh adoption is the real and stated path; the
verdict is unchanged.

**Fix.** Apply the same `## 10. Reuse audit` block and the date-gated ten/nine line-6 wording to
`tools/memory-tree/SPEC-TEMPLATE.template.md`, so the generated copy is provably derived from the
source rather than hand-edited.

**Left-shift gate.** A `gate-legs.json` leg asserting
`diff --strip-trailing-cr tools/memory-tree/SPEC-TEMPLATE.template.md memory/TEMPLATE-SPEC.md`
is empty. Single source → generated artifact → parity gate; the pair can then never drift again.

---

### H5 — `SPEC10_CUTOFF` is an env-overridable merge-bar knob, documented nowhere, defaulting to ON

**`tools/memory-tree/check-memory-hygiene.sh:357`**

```sh
SPEC10_CUTOFF="${SPEC10_CUTOFF:-2026-08-04}"
```

Every other threshold in this script lives in the in-repo, reviewable `.memory-tree.conf`
(`SPEC_FORMAT_CUTOFF="2026-07-15"`, line 18) — the file's own header calls that the *"Single
source"*. This one is hardcoded in the script **and** reachable from the environment, because
`. "$ROOT/.memory-tree.conf"` at `:21` precedes it.

Four absences, all verified: it is missing from the file-header config list (`:3-4` names
`MEMORY_ROOT`/`DISCIPLINES`/`FAMILIES`/`TOMBSTONE_ROOTS`/`SPEC_FORMAT_CUTOFF` only), from
`tools/memory-tree/README.md`'s Configure bullets (same five), from `WIRE-INTO-PROJECT.md`, and
from both `.memory-tree.conf` and `.memory-tree.conf.example`. The default asymmetry is real:
`SPEC_FORMAT_CUTOFF` defaults to `''` and gates the whole check **off** at `:344`, while
`SPEC10_CUTOFF` defaults to a hardcoded build date and is therefore **always armed**.

**Impact.** `SPEC10_CUTOFF=2999-01-01` exported from a shell profile, a CI job env, or a wrapper
script silently deletes the §10 requirement tree-wide, with no audit trail — the `fail 12` message
at `:497` interpolates only `$SPEC_FORMAT_CUTOFF`, and a green run never states which canon it
applied. That is a gate bypass that looks exactly like coverage, violating §14's *"a skip must
announce itself"* from the same commit. Independently, any adopter with the ratchet armed silently
acquires a second ratchet on a date they never chose, with no documented way to discover or move
it — and, with H4 unfixed, no template that satisfies it.

**Fix.** Move the value into `.memory-tree.conf` and `.memory-tree.conf.example` beside
`SPEC_FORMAT_CUTOFF`; declare it at the top of the script with the other conf-backed vars and
initialise it to `""` (drop the `:-` fallback so the environment cannot reach it, and so an adopter
opts in exactly as `SPEC_FORMAT_CUTOFF` requires); add it to the file-header list, the README
Configure bullets and `WIRE-INTO-PROJECT.md`; and echo the applied canon (`nine`/`ten` + the cutoff)
on check 12's status line so a green row records which bar it cleared.

**Left-shift gate.** Extend `tools/memory-tree/check-kit-versions.sh` (or add a leg) asserting every
`${VAR:-` default in `check-memory-hygiene.sh` has a matching key in `.memory-tree.conf.example` —
gates the class, not this instance. Add a selftest arm asserting check 12's output names the canon
it applied.

---

## MEDIUM

### M1 — check 12's excerpt post-pass diffs against the NINE-section canon even when awk chose ten

**`tools/memory-tree/check-memory-hygiene.sh:491`**

The awk pass picks the canon per file by filename date (`:427`,
`want = (fdate >= cut10) ? canon10 : canon`), but the post-pass rebuild diffs unconditionally
against `$SPEC_CANON` (nine sections, `:345-353`).

**Impact.** Reproduced live: `SPEC10_CUTOFF=2026-01-01 bash tools/memory-tree/check-memory-hygiene.sh`
printed 11 consecutive `… (## sections differ from the canonical ten of memory/TEMPLATE-SPEC.md):`
lines with **zero excerpt lines between them** — the offending specs' nine headings equal
`$SPEC_CANON` exactly, so `diff` exits 0 and emits nothing. The most likely §10 violation — a spec
written to the old nine-section template, i.e. the entire population H4 will produce — reds with a
header promising an excerpt after a colon and delivering nothing, which reads as a broken gate
rather than a missing section. Conversely a genuinely broken ten-section spec gets a spurious
`> ## 10. Reuse audit` line. The wired selftest treats excerpt content as load-bearing
(`check-memory-hygiene.test.sh:141-143`, `:149-150` asserting the 6-line cap) but its fixture is
dated `2026-08-01` (`:89`), below the default cutoff, so it exercises only the nine-canon path and
cannot see this.

**Fix.** Tag the sentinel with the chosen canon — `print "\001\t" f "\t" wantn` — and have the
post-pass select `"$SPEC_CANON10"` when the tag is `ten`, else `"$SPEC_CANON"`, before the `diff`.

**Left-shift gate.** Add a post-cutoff fixture (filename dated ≥ cutoff, nine sections) to
`check-memory-hygiene.test.sh` and assert the excerpt is non-empty and contains
`> ## 10. Reuse audit`. A pure line-count assertion is not enough — it is what let this through.

---

### M2 — `ps-hygiene.py:_code()` strips only whole-line comments, manufacturing two false-positive classes

**`tools/gate-lint/ps-hygiene.py:36`**

`_code()` strips `<# … #>` blocks and whole-line `^\s*#` comments only, so `_IDENT` still sees
trailing comments and single-quoted PowerShell literals. Measured by executing the module:

- `$LEGS = @(1,2)   # $legs is the parsed manifest` → `{'legs': ['LEGS','legs']}`
- `Write-Host 'literal $foo text'` + `$Foo = 1` → `{'foo': ['Foo','foo']}`; a full `scan()` over a
  temp tree containing that file returns a finding, exit 1. A literal here-string
  `@'…$foo…'@` fails identically.

**Impact.** Both are false positives, and both contradict the function's own docstring claim that
*"a collision in prose is not a collision"*. The first case is precisely the comment a maintainer
writes after fixing a case collision — rename plus a note about the old name — so the gate reds the
prose explaining the fix it just approved. `'$foo'` in PowerShell is a literal and never a variable.
Separately, `_BLOCK` strips `<# … #>` anywhere including inside a double-quoted string, which can
delete real code from the scanned text. The tree has **zero** `.ps1` files, so the predicate was
never run over a real tree — the exact step §14 of this same diff mandates
(*"run the candidate over the real tree and print hits AND near-misses before committing"*).

**Fix.** In `_code()`, strip `'[^']*'` spans first, then drop from an unquoted `#` to end of line on
each line (a `#` inside a double-quoted span must survive). Narrow `_BLOCK` so it does not reach
inside quoted spans.

**Left-shift gate.** Two `--selftest` arms asserting `case_collisions()` returns empty for
`$LEGS = 1  # $legs` and for `'$foo'` + `$Foo` — a *clean* assertion, so the regression is observed
rather than assumed. With H3's legs wired, these actually run.

---

### M3 — `memory/TEMPLATE-SPEC.md` contradicts itself: line 6 says ten, lines 48/53/54 still say nine

**`memory/TEMPLATE-SPEC.md:53`**

Line 6 reads *"exactly the ten canonical `##` sections"*; line 53 reads *"**Tier-2** uses the full
nine-section skeleton below"*; line 48 says *"nests as `###` under the nine sections"*; line 54 says
*"the nine-section canon"*. The skeleton actually below now has `## 10. Reuse audit` at line 130, so
line 53's "below" is factually wrong, not merely stale. (Line 7's "nine" is legitimate — it is
explicitly the pre-cutoff branch.)

**Impact.** An author who reads the Tier-2 profile line — the one that actually tells them what to
write — produces a nine-section spec and reds check 12, with the blank excerpt from M1. The
template-vs-gate mismatch class, introduced by a partial edit of the same file.

**Fix.** Update lines 48, 53 and 54 to the date-gated wording — *"the ten canonical sections (nine
for specs dated before `SPEC10_CUTOFF`)"* — and mirror into
`tools/memory-tree/SPEC-TEMPLATE.template.md` per H4.

**Left-shift gate.** A hygiene arm asserting the template's own `## ` headings equal the canon the
script would apply to a spec dated today, plus a grep that no line of `TEMPLATE-SPEC.md` says
"nine-section" outside the explicit pre-cutoff sentence. Generate one from the other, or drive the
template through the gate.

---

### M4 — AC5's report half is unbuilt: the resolved root never reaches the artifact a human reads

**`tools/workflows/tier2-review.js:230`**

The synth prompt (`:221-231`) uses `repo` solely as the write-path fragment `${repo}/${reviewDir}`
and never instructs the report to name the root or the sha; the synth schema (`:235-244`) is
`{path, blockers, highs, summary}` with no such field. `root: repo` is present in all three early
returns and absent from the terminal one.

**Impact.** `repo` is computed → logged → interpolated → never read by the deliverable. AC5 requires
*"the report header states the resolved root and the sha it read"*; the resolved root survives only
in the `:69` transcript log line, which is lost the moment the report is read on its own. A
misdirected run that produces findings still ships a report that cannot identify its target — the
precise failure S5 was written to close, and the reason two prior runs audited the wrong
repository. Distinct from H1: the load-bearing half here is the markdown artifact, a different
requirement.

**Fix.** Extend the synth prompt with a required header line —
`Review root: ${repo} · base ${base} · head ${head} (${shortSha})` — add `root` and the resolved
base sha to the synth schema and to the terminal return, and require a partiality line when
`lensesDead > 0`.

**Left-shift gate.** In the fixture harness, assert the synth prompt string contains the resolved
root and both refs. Cheap, and it is the only thing that keeps a prompt requirement from rotting.

---

### M5 — §7 of the spec promises a fixture harness that does not exist, and mis-cites AC5 for AC6

**`memory/tooling/builds/2026-08-03-TOOL-aGuardedTally/spec/2026-08-03-spec-aGuardedTally-1.md:119`**

§7 Gates promises *"a fixture harness that stubs the agent layer"* covering AC1–AC4 and says the
gate-lint selftest exercises AC5. `ls tools/workflows/` returns `tier2-review.js` and nothing else —
no harness, no stub, no test file. `gate-legs.json` has no workflow leg. The build folder contains
only `prompts/` and `spec/` — no `build/`, no `reviews/` — so there is no recorded manual
verification either. The AC-number drift is self-documented: §9 rev-2 states *"Prior AC5 renumbered
to AC6"*, AC6 is the case-collision/BOM scan and AC5 is the review-root AC, but §7 was not updated
with the renumber. Header at `:3` reads `**Status:** CLOSED · rev-3`.

**Impact.** S1/S2/S5 — the centrepiece of the unit — land with zero automated coverage and are
unreachable by the merge bar, so the three new outcome strings have never been observed failing.
The CLOSED status asserts a gate set that does not exist.

**Fix.** Build the harness (it is the gate B1, H1, H2 and M4 all need anyway), wire it into
`gate-legs.json`, and fix the AC5/AC6 citation. If the harness is genuinely deferred, say so in §7
and in the revision log rather than describing something that was not built, and flip the header off
CLOSED until AC4 holds.

**Left-shift gate.** A hygiene arm asserting every path named in a spec's §7 Gates exists on disk —
a spec may not cite a gate file that is not there. Same shape as the existing pointer checks.

---

## Recommended landing order

1. **B1** — the harness is actively unsafe to trust until absent verdicts stop counting as
   refutations. Build the fixture harness first; it is the gate for B1, H1, H2 and M4.
2. **H3 + M2** — wire `ps-hygiene.py` and fix its predicate together, so the first observed run is
   over a corrected scanner. Do not land the legs until a failing case has been seen RED.
3. **H4 + M3 + M1** — the reuse-audit trio. Fix the deployed template, unify the template's own
   prose, fix the excerpt canon, then add the parity leg and the post-cutoff fixture.
4. **H5** — move `SPEC10_CUTOFF` to conf and make check 12 announce its canon.
5. **M5** — reconcile §7 with reality and re-flip the status once AC4 actually holds.
