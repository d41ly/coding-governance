# Review 1 — Tier-2 adversarial pass over TOOL-aNumeralWarden-1 at rev-1

**Serves:** spec-audit TOOL-aNumeralWarden-1

**Scope:** `spec/2026-08-10-spec-aNumeralWarden-1.md` at rev-1, before any code, at base
`289daf72`.
**Method:** four primed lenses — does the fix close the hole, is the cut-line right, are the
acceptance criteria falsifiable, is every cited fact true at base — then default-refute skeptics in
five batches keyed on an orchestrator-assigned integer, then one synthesis pass. Workflow
`wf_093ab86e`, 10 agents.
**Result:** 26 raw findings, 20 confirmed, 6 refuted, 0 unverified. Precision 0.77, above the 0.5
floor `memory/guides/REVIEW-PROTOCOL.md:89` sets for adding agents rather than tightening scope.
**Disposition:** all ten consolidated findings folded into rev-2. The two that changed the design
are finding 1 (S3 was scoped to the marker K, leaving the concurrency knob resolving on the S1
path) and finding 2 (S1 specified a verdict but no argument extraction, and every acceptance
fixture was single-line against a per-line scanner).

---

## Verdict

**Not ready — this needs a rev before an owner approves it.** The spec is well-researched and its inventory is accurate, but two defects go to the unit's own thesis. First, the concurrency knob it promises to deny (`§1:9-10`, "denies the two caller-settable knobs") is removed by hand-editing two files (S5) and by no rule at all: S3's narrowing of the `|| <literal>` binder is scoped explicitly to the `gov:fixed-verifiers` K (`§2:19-20`, `§4:81-82`, and the rejected alternative at `§4:118-119`), while S1/S2 route the new cap resolution through the same unchanged `boundedK`/`consts` pair — so `const CAP = (args && args.cap) || 5` still resolves to 5 on the cap path, in the inline-`script` modality `REVIEW-PROTOCOL.md:32-36` calls PRIMARY. Second, S1 specifies a *verdict* but never the *extraction*: `agent-cap.js` is a per-line scanner with no paren-balanced argument walk, every shipped call site is multi-line, and every AC is a single-line fixture — so a fully conforming implementation passes AC1-AC6 with `boundedParallel(\n thunks,\n 500\n)` unexamined. Around those sit four acceptance criteria that cannot fail (AC7, AC9, and AC3/AC5 as exit-code-only), one omitted file the merge bar hard-fails on (`.claude/hooks/agent-cap.js`), and a BINDING document the change falsifies with no scope item and no table row. The corrections below are all local — the design is sound, the rev is a half-day of spec text, not a redesign.

## Findings

### 1. The concurrency knob survives the predicate — only the hand edit removes it
**blocker** · `memory/builds/aNumeralWarden/spec/2026-08-10-spec-aNumeralWarden-1.md:19` (S3), with `:14-16` (S1) and `:118-119` (rejected alternative)
*(Merge of confirmed findings 1, 7 and 15 — the same defect seen from three angles: the resolver, the goal statement, and the missing AC.)*

S3 forbids the `|| <literal>` binding **only** as the K of a `gov:fixed-verifiers` line. `§4:81-82` says so in as many words ("stays usable for ordinary constants but is no longer accepted as the K of a `gov:fixed-verifiers` line"), and `§4:118-119` rejects widening it. But `§4:69-71` and `§10:191-193` route S1's and S2's new cap resolution through *the same* `boundedK` (`agent-cap.js:103-107`) reading *the same* `consts` map, which is built at `agent-cap.js:116-121` from **both** `const X = <int>` (`:117`) **and** `<expr> || <int>` (`:119-120`). So after S1/S2 land, `const CAP = (args && args.cap) || 5` (`drift-audit-code.js:22`, `drift-audit-state.js:20`) still resolves to 5 at a call site (`boundedParallel(thunks, CAP)`) and as a definition default (`cap = CAP`, `drift-audit-code.js:23`). Inventory row 3 (`:59`) names this hole and receives no predicate change. The same resolver also survives reassignment: the bare-reassignment kill at `agent-cap.js:195-200` deletes from `ok`, never from `consts`, so `let K = 5; K = 500` resolves to 5.

**What breaks if it ships:** the hole closes for one knob in two files. Any new harness — or any inline `script` on a `Workflow` call, which `REVIEW-PROTOCOL.md:32-36` records as the primary entry point and as the literal shape of the original incident — writes the same one-line idiom, passes the hook, and `check-verifier-fanout.sh:84` prints `clean — N workflow script(s) obey the ≤5-verifier rule`. `REVIEW-PROTOCOL.md:68-70` records the ~40-agent burst that tripped the rate limiter twice as why the concurrency number exists. No AC catches it: AC1/AC2 use literals, AC4 tests the `||` form only on a marked line, AC6 passes because S5 removed the knob by hand.

**Correction to the spec text:** rewrite S3 (`:19-20`) to bind *every* consumer of `boundedK`, not just the marker K — "a K that is an identifier, at a `gov:fixed-verifiers` line, at a `boundedParallel(`/`boundedPipeline(` call site, or as a helper's `cap =` default, must be bound by a direct `const <name> = <int>` and must not be re-assigned anywhere in the script (mirror the `ok.delete` sweep at `agent-cap.js:195-200` onto `consts`)". This is *narrower* than the alternative rejected at `:118-119` and does not collide with it; say so there. Add to S9/AC: a red arm for `const CAP = (args && args.cap) || 5` + `boundedParallel(t, CAP)`, and one for `let K = 5; K = 500`.

---

### 2. S1 specifies the verdict but not the extraction; every AC fixture is single-line
**high** (borders blocker) · `spec:14-16`, with `§4:76`
*(Confirmed finding 2.)*

S1 says the hook "resolves the cap argument at every CALL SITE through the existing `boundedK` resolver" and `§10:192-193` claims S1-S3 "add call sites rather than a second resolver". `boundedK` converts a *token* to a verdict; **locating** the token is the work, and it does not exist. `agent-cap.js` builds a line array at `:111-112`; the only forward multi-line machinery is the bracket walk for array literals at `:161-169` (the `openersOf` window at `:222-240` is a backward scan for enclosing openers, not an argument walk). Every real call site is multi-line: `tier2-review.js:153-165` and `:206-220` pass no cap at all; `drift-audit-code.js:210-215` and `:250-283` put `CAP` on its own line (`:214`, `:282`). AC1/AC2/AC3 are all single-line fixtures and AC6 only requires exit 0.

**What breaks if it ships:** a per-line implementation satisfies AC1, AC2, AC3, AC6 and AC8 while `boundedParallel(\n  thunks,\n  500\n)` walks straight through — the hole reopens by pressing Enter, with every gate green. The opposite implementation is as bad: `§2:16` as worded ("denies when it … cannot be resolved to an integer") denies `tier2-review.js:153`/`:206`, which pass no cap, reddening AC6 and the `check-verifier-fanout.sh` merge-bar leg. `§4:76` handles the absent case ("absent-and-the-default-is-wide") but §2 does not, so the normative text and the design note disagree.

**Correction:** in S1, specify the extraction — "join forward from `boundedParallel(` / `boundedPipeline(` until the parens balance (the bracket walk at `agent-cap.js:161-169` is the precedent), split on top-level commas, take argument 2". Restate S1's absent-argument rule to match `§4:76`: an omitted cap resolves to the named helper's `cap =` default, and only an unresolvable-or-wide default denies. Add to §6 a red arm with the cap on its own line and a green arm for a bare `boundedParallel(thunks)`.

---

### 3. The wired copy `.claude/hooks/agent-cap.js` is absent from Files-touched
**high** · `spec:104` (§4 table, `:102-110`)
*(Merge of confirmed findings 4a and 20.)*

`.claude/settings.json:9` wires `node "${CLAUDE_PROJECT_DIR}/.claude/hooks/agent-cap.js"` — the executed copy is **not** the kit copy. `tools/hooks/agent-cap.test.sh:215-227` runs its parity arm unconditionally in this repo (guard: `[ -n "$ROOT" ] && [ -f "$ROOT/tools/hooks/agent-cap.js" ]`) and prints `FAIL .claude/hooks/agent-cap.js has drifted from tools/hooks/agent-cap.js` with a `cp` remedy; the arm cannot be satisfied by deleting the copy either (`:217-219`). I verified the two files are byte-identical at `289daf72`. Neither §2, §4 nor §5 mentions a re-copy step.

**What breaks if it ships:** a build following the table edits only the kit copy, reddening AC8 and AC11 (all 40 legs) — and until noticed, the hook that actually fires at the `Workflow` call still enforces the old, number-blind rule while the kit copy and every doc say the hole is closed. In-repo precedent confirms this is a convention breach, not a nicety: `memory/builds/aBatchedTribunal/spec/2026-08-09-spec-aBatchedTribunal-1.md:144` carries the row `| .claude/hooks/agent-cap.js | the wired copy, kept byte-identical |`.

**Correction:** add a table row `| .claude/hooks/agent-cap.js | S1 S2 S3 S4 S10 — re-copied from the kit; the test's two-copy parity arm gates it |`, and add `cp tools/hooks/agent-cap.js .claude/hooks/agent-cap.js` to §4 Rollout (`:97-98`).

---

### 4. The BINDING protocol rewrite is a §5 aside, not a scope item — and its shipped twin is unnamed
**high** · `spec:134-135` (and the §4 table at `:102-110`)
*(Merge of confirmed findings 4b, 8 and 21.)*

`§5:134-135` states that `memory/guides/REVIEW-PROTOCOL.md:72-74` — verbatim: "The hook does NOT parse the helper's numeric argument — its own header says so, and its self-test passes a helper call as an ALLOW case regardless of the number." — becomes false under S1 and "needs its paragraph rewritten". No numbered item S1-S10 assigns that work, no §4 table row lists it, §3 does not cut it, and no AC proves it. `memory/TEMPLATE-SPEC.md:103` requires scope to be the numbered list verifiable at DoD. Worse, the document has a shipped twin: `check-protocol-parity.test.sh:45` diffs `memory/guides/REVIEW-PROTOCOL.md` against `tools/workflows/REVIEW-PROTOCOL.template.md` and `exit 1`s on any difference; I confirmed the pair is in exact parity today and that the template carries the identical paragraph at `:72-74`. `--render` (`:40`) is the only restore path and appears nowhere in the spec.

**What breaks if it ships:** either the BINDING charter document keeps asserting the opposite of the shipped hook — the exact false-record class this unit exists to close, and the authority `agent-cap.test.sh:198-199` cites for asserting nothing about the number — or the builder edits one side, reds the protocol-parity leg (`gate-legs.json`), and fails AC11.

**Correction:** promote it to **S11** — "rewrite `memory/guides/REVIEW-PROTOCOL.md:72-74` (and, made imprecise by S3, the predicate at `:48-50`) to describe the post-S1..S4 predicate, then `bash tools/workflows/check-protocol-parity.test.sh --render`" — and add both `memory/guides/REVIEW-PROTOCOL.md` and `tools/workflows/REVIEW-PROTOCOL.template.md` to the §4 table. Add an AC that the protocol no longer contains the string `does NOT parse the helper's numeric argument`.

---

### 5. AC7 is vacuous — it is already green at base with S8 unimplemented
**high** · `spec:148-149`
*(Merge of confirmed findings 5, 9, 14 and 22 — four skeptics reached the same conclusion by the same route.)*

`check-protocol-parity.test.sh` runs a whole-file byte diff at `:45` and `exit 1`s at `:49`, **before** the content assertion at `:53-54` that S8 (`spec:30-31`) hardens. `memory/guides/REVIEW-PROTOCOL.md:7` reads `## The hard cap — ≤5 verify-stage agents TOTAL`; editing it to `≤50` breaks parity with the template (whose line 7 I confirmed still reads `≤5`), so the leg exits non-zero **today, at `289daf72`, with S8 absent**. AC7 is the only criterion covering S8, and no other AC touches this gate.

**What breaks if it ships:** S8 can land unimplemented, or implemented wrong, with the checklist complete — and the thing S8 exists to fix stays broken, because the digit-free `grep -qF 'verify-stage agents TOTAL'` at `:53` still matches `≤50 verify-stage agents TOTAL`. The cap number in the BINDING document can then be raised in both copies with the full bar green: a gate reporting on a number it never reads, which is this unit's own subject, the class banned by `memory/TEMPLATE-SPEC.md:134-136`, and the recorded class at `memory/gotchas/fixture-passes-by-finding-nothing.md:11-13`.

**Correction:** rewrite AC7 to isolate the `:53` assertion from the `:45` diff — "edit `memory/guides/REVIEW-PROTOCOL.md:7` to `≤50`, run `bash tools/workflows/check-protocol-parity.test.sh --render` so parity is restored, then `--check` exits non-zero with a message naming the missing hard cap; restore both files afterwards with `git checkout --`". Add the mirror arm (both copies at `≤5` → exit 0). Better still, move S8's proof into the parity gate's own population assertions rather than a one-shot manual mutation of a charter document.

---

### 6. AC3 and AC5 assert only an exit code, and S4's shape rule is underspecified against the shipped helper bodies
**high** · `spec:142`, `spec:145`, `spec:21-22`
*(Confirmed finding 16, with the S4 consequence carried forward.)*

Exit 2 is the shared deny code of every path in `agent-cap.js` — unreadable `scriptPath` at `:322`, rule 2 at `:341`, rule 1 at `:372` — so an arm phrased on the exit code cannot attribute the deny to the branch it names. AC1 (`:139-140`) and AC4 (`:143-144`) pin message content; AC3 and AC5 do not, so the spec applies its own standard inconsistently, and `memory/gotchas/fixture-passes-by-finding-nothing.md:24` states the rule verbatim: "Every arm asserts the SPECIFIC message its branch emits, never a process exit code." Concretely: AC5's fixture denies under the *existing* rule 2 with S4 absent, and AC3's fixture (`async function boundedParallel(t, cap = 99) { … parallel(t.slice(i, i+cap)) // gov:bounded-fanout … }`) denies under S4 with S2 absent.

That last point exposes a second problem in S4 itself. The canonical marked line in all three harnesses is `out.push(...(await parallel(thunks.slice(i, i + cap)))) // gov:bounded-fanout` (`drift-audit-code.js:26`, `drift-audit-state.js:24`, `tier2-review.js:18`). Its width token is the **parameter** `cap`, which is not in `consts` and which `boundedK` returns `false` for. S4 as worded ("must slice a bare identifier by a K that resolves at or under `MAX_VERIFIERS`") therefore denies the three shipped harnesses — directly contradicting AC6 and reddening the merge bar.

**What breaks if it ships:** S2 or S4 can ship non-functional with `agent-cap.test.sh` green and AC8/AC11 green; or S4 ships as literally worded and reds every leg on day one.

**Correction:** restate AC3 → "exits 2 with a message naming the DEFAULT PARAMETER of `boundedParallel` and the resolved value 99"; AC5 → "exits 2 with a message naming the `gov:bounded-fanout` line and the resolved slice width 50"; give each new branch in S1-S4 a distinguishable string. In S4, state how a parameter-named slice width is resolved — the intended rule is presumably "the slice width must be the helper's own `cap` parameter, whose default S2 has already bounded" — and say that explicitly, or AC6 and S4 cannot both hold.

---

### 7. S7 misses the third and most load-bearing copy of the false claim: the hook's own header
**medium** · `spec:28-29` (S7) and `spec:153-154` (AC10)
*(Merge of confirmed findings 6, 10 and 23.)*

`tools/hooks/agent-cap.js:19-20` reads: `CAP: default 5 (override with env AGENT_CAP). This guard doesn't verify the numeric arg — it enforces "use the helper"; the helper is where CAP lives.` S1 falsifies the second sentence; fork F1 (`:170-175`) falsifies the first either way. A repo-wide grep for `AGENT_CAP` returns exactly four sites — `README.md:50`, `WIRE-INTO-PROJECT.md:388`, and this header in both copies — so S7 enumerates two of four, AC10 greps only the two it named, and the §4 table assigns `agent-cap.js` "S1 S2 S3 S4 S10", not S7. Nothing catches it.

**What breaks if it ships:** `§4:97` says the hook is deployed verbatim into adopting repos, so its header *is* the adopter-facing contract — every adopter reads a docstring denying the very check the bumped version advertises. `REVIEW-PROTOCOL.md:72` cites this header as its authority, and `agent-cap.test.sh:198-199` repeats it as its stated reason for asserting nothing about the number, which contradicts the arms S9 adds. This header already shipped stale once (`memory/builds/aDrainedSluice/reviews/2026-08-08-review-TOOL-aBatchedTribunal-1-3.md:505-509`).

**Correction:** extend S7 to name `tools/hooks/agent-cap.js:14-21` (the CONTRACT and CAP paragraphs) and fold the `agent-cap.test.sh:198-199` rationale comment into S9. Widen AC10 to `grep -rn 'AGENT_CAP' README.md WIRE-INTO-PROJECT.md tools/hooks/agent-cap.js`. Naming `.claude/hooks/agent-cap.js` here is unnecessary — the parity arm in finding 3 covers it once the copy step is in the table.

---

### 8. S10's "move together" has no enforcement, and AC9 cannot fail
**medium** · `spec:152` (AC9) and `spec:162` (§7)
*(Merge of confirmed findings 12 and 17.)*

`tools/check-kit-versions.sh:23` is `need "KIT_AGENT_CAP_VERSION" tools/hooks/agent-cap.js "KIT_AGENT_CAP_VERSION = '$V'"` with `V='[0-9]+\.[0-9]+'` (`:15`) — a bare presence/format check. Any well-formed value satisfies it, so the gate exits 0 today at 1.1 with S10 unstarted. The constant-vs-`gov:kit`-marker reconciliations exist only for memory-tree (`:30-34`), memory-recall (`:40-44`), drift-audit (`:50-54`) and pytest-parallel-guardrails (`:64-70`); grepping the tree, `gov:kit agent-cap@1.1` is asserted by no gate at all.

**What breaks if it ships:** AC9 is green before, during and after S10; a half-bumped pair (constant at 1.2, marker at 1.1) passes the whole 40-leg bar and ships a deployer-facing marker naming the pre-change engine — while `§4:97-98` makes the bump the deployer's only signal that the contract moved. `§7:166` ("Every assertion lands in a leg that already runs") is therefore false of S10 — a spec asserting a gate covers something it does not, which is this unit's own subject. Mitigating: both literals sit on the same line (`agent-cap.js:37`), so drift is less likely than for the four cross-file pairs — but likelihood is not enforcement.

**Correction:** fold the missing pair assertion into S10 (derive the constant, then `grep -qE "gov:kit agent-cap@<c>([^0-9.]|$)"` — a two-line addition matching the four existing ones), and restate AC9 as "exits 0, **and** exits non-zero when only one of the two agent-cap literals is bumped". Alternatively drop the marker half of S10 and say plainly that the marker is unenforced.

---

### 9. S5 narrows the drift-audit kit's documented `args` contract without moving its version
**medium** · `spec:23-25` (S5) with `spec:26-27` (S6)
*(Confirmed finding 11.)*

`drift-audit-code.js:3` (`version: '1.0'`) and `:15` (`// gov:kit drift-audit@1.0`), identical in `drift-audit-state.js:3`/`:15`, stay put while S10 bumps only `KIT_AGENT_CAP_VERSION`. The `args` input blocks keep advertising `maxVerifiers: 5,` at `drift-audit-code.js:45` and `drift-audit-state.js:43`; S6 corrects only the cap comment at `:19-21`/`:17-19`. These are kit artifacts, not repo-local scripts — `tools/drift-audit/SKILL.template.md:72-73` lists them under the installed `workflows/` prefix and they carry the kit marker. `check-kit-versions.sh:56-57` only asserts `meta.version` is well-formed, never that it moved.

**What breaks if it ships:** an adopter pulls a silently narrowed `args` contract under an unchanged version number, so version detection reports no change while `args:{cap:8, maxVerifiers:8}` becomes a no-op; the kit's own inline documentation still names an input that no longer exists. `§4:92-93`'s "no shipped caller passes it" is true of this tree only, against a comment (`drift-audit-code.js:19-21`) that says the cap **varies by adopter**.

**Correction:** either extend S10 to bump the drift-audit kit's markers (`meta.version` and `gov:kit drift-audit@` in both harnesses, plus `KIT_DRIFT_AUDIT_VERSION`/README if the pair gate binds it) with a migration line in `tools/drift-audit/README.md`, or state in §3 that the drift-audit kit contract is deliberately unversioned in this unit. Either way, make S5 explicit that `//   maxVerifiers: 5,` is struck from both input blocks.

---

### 10. S6 has no acceptance criterion
**low** · `spec:26-27`
*(Confirmed finding 18.)*

Nothing in AC1-AC11 observes the stale comment. `drift-audit-code.js:19` and `drift-audit-state.js:17` both read "(agent-cap.js defaults to 6 here, 5 in the repo this kit was ported from)"; `agent-cap.js:38` reads 5 and `:96` reads 5, and `REVIEW-PROTOCOL.md:70` records "It moved 6 → 5 here", so the comment is false. Both hook scan paths strip line comments (`:67`, `:112`), so AC6 structurally cannot see it. The sibling doc-only item S7 got AC10; `memory/TEMPLATE-SPEC.md:103` requires every scope item to be verifiable at DoD. Scope→AC map for the record: S1→AC1/AC2, S2→AC3, S3→AC4, S4→AC5, S5 (`maxVerifiers` half)→AC6, S5 (`CAP` half)→none, S6→none, S7→AC10, S8→AC7 (vacuous), S9→AC8, S10→AC9 (vacuous).

**Correction:** add "**AC12** — `grep -rn 'defaults to 6' tools/workflows/` returns nothing." One line, in the same manual doc-check slot AC10 occupies.

## Not found

I opened `tools/hooks/agent-cap.js` in full, `tools/workflows/drift-audit-code.js` (helper block, args block, both fan-out call sites), `drift-audit-state.js`, `tier2-review.js` (helper definition at `:15`, both call sites), `check-verifier-fanout.sh`, `check-protocol-parity.test.sh`, `check-kit-versions.sh`, `tools/hooks/agent-cap.test.sh:190-235`, `.claude/settings.json`, `memory/guides/REVIEW-PROTOCOL.md` in full, `tools/workflows/REVIEW-PROTOCOL.template.md`, and the two doc sites in `README.md`/`WIRE-INTO-PROJECT.md`. **The spec's Inventory table (`:55-65`) checks out row by row** — `CAP` at `agent-cap.js:38` really does reach nothing but the deny text at `:337` and `:354-363`; `a.maxVerifiers || 5` really is at `drift-audit-code.js:51`/`drift-audit-state.js:51`; and `offendingLines`'s marker return at `:66` really does exempt a `gov:bounded-fanout` line before any shape check. The two cuts to §3 that I could evaluate are correctly drawn: the opener walk at `:222-240` genuinely needs a statement-level rewrite rather than an opener count, and `MAX_LENSES` at `:97` genuinely is 6 against `MAX_VERIFIERS` 5 — surfacing it as fork F2 with no code moving is the right call. I found nothing wrong with S9's arm design as a concept, nothing wrong with the §5 fail-closed claim (`agent-cap.js:242-245` does fail closed and the new branches described would too), and nothing wrong with §10's reuse audit — I confirmed `boundedK` is a non-exported function in a `.js` file, so the map's symbol corpus genuinely cannot surface it.