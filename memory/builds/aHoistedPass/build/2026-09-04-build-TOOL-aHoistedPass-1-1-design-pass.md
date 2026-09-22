# aHoistedPass — the design pass behind the ten units

**Serves:** research TOOL-aHoistedPass-1 TOOL-aHoistedPass-2 TOOL-aHoistedPass-3 TOOL-aHoistedPass-4 TOOL-aHoistedPass-5 TOOL-aHoistedPass-6 TOOL-aHoistedPass-7 TOOL-aHoistedPass-8 TOOL-aHoistedPass-9 DEPL-aHoistedPass-1

**Commissions:** TOOL-aHoistedPass-1 TOOL-aHoistedPass-2 TOOL-aHoistedPass-3 TOOL-aHoistedPass-4 TOOL-aHoistedPass-5 TOOL-aHoistedPass-6 TOOL-aHoistedPass-7 TOOL-aHoistedPass-8 TOOL-aHoistedPass-9 DEPL-aHoistedPass-1

*Authored 2026-09-04 on node `a`, against `origin/main` = `c4fcf5ad`. Eight revisions: rev-1 from five
research lenses, rev-2 folding three adversarial critiques, rev-3 measuring two blocker fixes, rev-4
adopting the hoist on owner instruction, rev-5 correcting six over-claims about what existing
machinery catches, rev-6 correcting the hoist's own false headline, rev-7 folding four owner rulings,
rev-8 correcting the adopter ruling and 23 citation defects. Two over-claim audits, 246 `file:line`
anchors verified at the tip.*

*One correction this record carries that the design body does not: §5's ratchet predicate was
specified as dropping lines matching `<!--`, which drops only a comment's FIRST line and therefore
passes a multi-line comment carrying the anchor. Measured on four fixtures against the real
`memory/guides/BUILD-METHOD.md`: the line-prefix form PASSES that evasion, a block-stripping form REDS
it, and an honest rule sentence is green in both. The term strips whole `<!-- … -->` blocks across
lines, and `TOOL-aHoistedPass-2` carries the corrected predicate.*

---

# DESIGN rev-8 — the HOIST, with D4 re-decided and nine audit defects corrected at source

**Supersedes rev-7 entirely; rev-7 superseded rev-6, and so on back to rev-1. This file stands alone.**
Written 2026-09-04 on node `a`. Everything is stated against `origin/main` at **`c4fcf5ad`**, re-fetched at
the top of this pass — the SAME tip rev-7 was written against, so no figure moved for a reason outside
this document. Every count below was nevertheless RE-DERIVED here rather than carried, and every line
number was RE-OPENED. Four of rev-7's nine audit defects were off-by-one citations, so re-derivation and
re-opening are the whole discipline of this pass.

**READ THIS BEFORE TRUSTING ANY EARLIER FIXTURE.** The worktree this pass runs in is
**130 commits BEHIND `origin/main`, 0 ahead** — `git rev-list --left-right --count origin/main...HEAD`
= `130  0`, re-run here. Every figure comes from a `MSYS_NO_PATHCONV=1 git show "origin/main:<path>"`
blob or from a `git archive origin/main`-extracted snapshot repo, and every exit code was captured
WITHOUT a pipe.

**THE OWNER RE-DECIDED D4 ON 2026-09-04, after being told the truth about it.** rev-7 discovered that the
`review-harness` edge buys ORDERING ONLY. The owner had been told the edge would make an adopter get the
harness or not get the kit; that was FALSE. The decision was retaken with the real options and **the owner
chose BOTH mechanisms**: the edge STAYS for ordering, PLUS a validation at install time and an announced
skip at gate time. §4.5 and §9 D4 carry it.

**The rule this pass enforces on itself, unchanged and applied harder.** Every sentence asserting that some
mechanism refuses, catches, grades, enforces or prevents something names a line opened in THIS pass. Where
nothing does, the sentence says **the run holds it** and §10 carries the residual. No count of a derived
population appears that was not derived in this pass. Gate legs are cited by NAME.

---

## EXECUTIVE SUMMARY

**Three defects, all still present at `c4fcf5ad`.** (a) **No route** — `passes-harnessed:M6`
(`unattended.sh:469`) points at a section stating no harness rule; **0 of 17** core handles appear in
`memory/guides/BUILD-METHOD.md`; check 16 arm B (`check-unattended.sh:1592`) only asks whether the section
EXISTS. (b) **Wrong shape** — BUILD is ONE `agent()` holding the whole roster (`unattended-build.js:485`);
median roster 4, max 30, over 85 builds. (c) **No witness** — the harness writes nothing to disk.

**The mechanism.** `unattended-build.js` ends after SPEC, AUDIT and DISPOSAL and RETURNS the ordered
roster; the run makes ONE main-loop `Workflow` call per unit against `tools/workflows/unattended-unit.js`,
**by `scriptPath` and never by `name`** (`agent-cap.js:1505-1519`).

**WHAT THE PER-DISPATCH RE-READ ACTUALLY BUYS, corrected.** rev-7 called all four post-read rule blocks
burst rules. **THREE are** — `:1521` one-agent-per-item, `:1541` an unresolvable bound, `:1562` raw
`parallel(`/`pipeline(`. **The fourth, RULE 5 at `:1593`, is a ref-keyed verdict JOIN**, and the hook says
so itself at `:1559-1560`: *"the three rules above all prevent a BURST … while a ref-keyed join is a wrong
verdict, which is cheap to re-run."* The count of four stands; what they are does not.

**D4 IS NOW THREE MECHANISMS, NOT ONE.** The edge (`kit.toml:7`) orders an install and does nothing else —
**measured this pass: `govkit plan --kits unattended` into a target holding neither dependency exits 0 and
previews an `unattended`-only install.** So: **(i)** `selfcheck` check 7 gains a plain-`requires` registry
arm, and `cmd_apply` gains an installed-set REFUSAL after AC8; **(ii)** `check-unattended.sh` gains check
31, which ANNOUNCES a named skip when `tools/workflows/` is absent and FAILS when the directory is present
and a named script is not. Neither subsumes the other: **(i) runs once, at install, and only for installs
made after it lands; (ii) runs on every bar of every adopter forever, including the population (i) can
never reach.** §10's adopter residual is **NARROWED, not RETIRED** — to an adopter who installed before
this lands, never re-runs `apply`, and never sets `GOV_UNATTENDED_REPORT=1`.

**Zero existing descriptors red.** The candidate predicates were run over all 25 registry entries this
pass: nine plain-`requires` edges exist, all nine name a real entry, and both the DEFAULT selection and
`--all` satisfy every edge. The one thing that breaks is a hand-narrowed single-kit `--kits` into a virgin
target, which is nine cases including `--kits drift-audit` — the exact example `govkit.py:495-496` calls
legal. That docstring gains a clause in the same commit.

**Completeness rests on `build-complete` term 5 (`unattended.sh:3353`) ALONE**, escape `--override
build-complete`. **Order rests on nothing that survives a declaration row** (`:4647`). **Honestly
unenforceable:** the agent boundary, the per-run total, the PreToolUse-to-load race, the child's content
between dispatches, and the class that nothing under the run's own uid binds the run.

---

## §0 — CHANGE LEDGER: rev-7 → rev-8

### 0.1 D4, re-decided — what changed in this document

| | rev-7 | rev-8 |
|---|---|---|
| **the ruling** | "EDGE TAKEN, and it buys ordering only." One unit, U9, one descriptor line. | **THREE mechanisms.** The edge for ordering, **plus (i) validation at install time in two govkit verbs, plus (ii) an announced skip at gate time in the unattended leg.** §4.5 is re-cut into 4.5a–4.5e; U9 grows and **U10 is new**. |
| **§10's adopter entry** | "STAYS, unchanged." | **NARROWED, and the narrowing is named to a three-clause population** (§10, first bullet of the adopter block). |
| **the evidence** | read at source only | **plus one observation: `plan --kits unattended` into a virgin target exits 0, selection `unattended`.** The edge's emptiness is now measured, not only argued. |
| **the cost nobody had priced** | — | **`govkit refusal join`** (`refusal_join.py`) demands a named arm for every deployer refusal branch, anchored `(module, function, ordinal)`, against a shrink-only `BRANCH_PIN = 217` (`:41`) whose every movement is argued inline. (i) owes two arms and a pin bump. |

### 0.2 The nine audit defects, each corrected against source in this pass

| # | rev-7 said | corrected, with the line opened here |
|---|---|---|
| **1** | §2.1 and §8: the re-read feeds "four burst-class rule blocks". | **THREE burst + ONE join.** `:1521` fan-out-per-item · `:1541` unresolvable bound · `:1562` raw `parallel(`/`pipeline(` are burst; **`:1593` is RULE 5, the ref-keyed verdict join**, labelled at `:1592` *"LAST because it is the cheapest failure to recover from"* and characterised at `:1559-1560`. **§2.4's residual clause follows the correction**: the narrowing covers a fan-out burst **or a ref-keyed join**, and the clause that goes into the protocol changes wording. |
| **2** | §0.3 T3: `memory/map/baseline.toml:1-11` is "shrink-only and forbids new rows". | **`:10-11` retracts it in the file's own words** — *"Nothing enforces the rule today — that is why the option was available at all."* It is a PROSE CONVENTION with one recorded exception (`:6-11`, `TOOL-aSiftedPlaybook-1`), not a constraint. rev-7 stated a convention as a machine fact, which is the class its own §4.1 self-rule polices. The numberless-leg-name argument (§5B.3) survives as a CONVENTION argument and says so. |
| **3** | §5B.3: "Two legs already ride it." | **THREE do** — `template size <=48KiB` (no positional, so the default subject at `check-template-size.sh:49`), `charter size` (AGENTS.md), `kickoff engine size <=18KiB`. Derived from `tools/gate-legs.json` this pass. rev-7's own §8 recorded the third and its §5B did not. `build-method size` is the FOURTH. |
| **4** | veto 2 is `BUILD-METHOD.md:83`. | **`:84`.** `:83` is veto 1 (*"fails an acceptance criterion or gate already written in the spec"*). Also re-opened: `:76` carries the delegation clause and `:87` says *"Vetoes 2 and 3 are owner turns"*. Cited twice in rev-7 and D1 hangs on it. |
| **5** | the playbook sentence is `SKILL.template.md:365`. | **`:363-364`.** And there is a **near-duplicate at `:489-491`** rev-7 never mentioned, so a reader following `:365` lands in the gap between them. Both are about a PLAYBOOK, not the Skill; §4.4 uses it as an ANALOGY and now says so. |
| **6** | arm B's grep is `check-unattended.sh:1593`. | **`:1592`.** `:1593` is its `|| fail 16` continuation. Also re-opened: the carrier guard `:1589`, the loop `:1590`, `sec=${pair#*:}` `:1591`, and the silence rule `:1586-1588`. Cited three times in rev-7 and it is the exact line U2 edits. |
| **7** | `check_waiver_scope`'s equality is `unattended.sh:1173`. | **`:1172`.** `:1173` is `fail 45`. The function is `:1163-1179`. |
| **8** | `resolve_selection` is `govkit.py:519-583`. | **`:521-590`, with FOUR `derive_install_order` call sites: `:558`, `:567`, `:582`, `:590`.** rev-7's range truncated the function before its default-selection path. **Re-derived over the whole function:** every call passes `all_kits(descs)` or a `sorted()` of an already-fixed id list, and none adds a `requires` target — so the claim survives, and it now survives over the whole function. `derive_install_order` itself is `:486-518`, not `:487-517`. |
| **9** | §3.4 heading: "`pass-order history` grades NEITHER order NOR completeness." | **The leg's own `check-pass-order.sh:21` says *"this measures ORDER and nothing else."*** The body was precise and the heading was not. **New heading: "`pass-order history` grades SPEC-BEFORE-CODE order, not the build's declared UNIT order and not completeness."** Its two exclusions are `:22` (dispatch) and `:23-24` (a non-CLOSED unit); what it DOES check is stated at `:9-10`. |

### 0.3 Further citation corrections found by re-opening everything, not only the nine

| citation | rev-7 | this pass |
|---|---|---|
| `scope_of` | `unattended.sh:505-516` | **`:505-514`** — `:515-517` is a `TOOL-aScouredKit-7` comment |
| the harness's `units` refusal | `unattended-build.js:118-123` | **`:118-124`** (message `:120-122`) |
| the nesting comment | `unattended-build.js:276-277` | **`:274-279`** |
| tier2-review's three version tokens | `check-kit-versions.sh:34-42` | **`:32-44`** — header `:32-37`, comparison loop `:38-44` |
| the five unattended template markers | `check-kit-versions.sh:180-192` | **`:179-192`** — `:179` is the `git ls-files`, `:180-183` the vacuity refusal |
| the install-prefix BAN | `check-install-prefix.sh:315-322` | **`:315-319`** |
| the size gate's shape | `check-template-size.sh:70-96`, `:82-95`, `:98-112`, `:103-112` | **declaration read `:70-78` · precedence argument `:80-90` · resolution `:91` · CR-stripped measurement `:99-101` · over-budget branch `:104-112`** |
| `requires_if`'s registry arm | `govkit.py:1330-1334` | **`:1330-1333`** — `:1334` starts the condition-key arm |
| the unclaimed-leg refusal | `govkit.py:1602-1603` | **`:1602-1604`** |
| **who carries `template size <=48KiB`** | "nobody claims it — it sits in `baseline.toml:34`" | **BOTH statements are needed and rev-7 conflated two registries.** It IS an `[[exempt_leg]]` at **`registry.toml:357`** (so `govkit.py:1602-1604` is satisfied) AND it sits unclaimed in the MAP baseline at `baseline.toml:34`. Two registries, two claims, one leg. |
| the drift ratchet registry | `drift_signals.py:279-291` | **`:279-290`** |
| the recipe build's declaration | `SKILL.template.md:296-345` / `:296-372` | **section `:298-366` · the six keys + `authorized-by`/`playbook`/`pieces` at `:332-338` · the whole piece vocabulary at `:354-355`** |
| the candidate child's marker | "`export const meta` present" | **the DECLARATION is at `:30`**; `:6` and `:8` are comments about it, so a bare `grep -c` returns 3 and means nothing |
| `tools/unattended/README.md` | "five sections" | **four `##` sections** (`:9`, `:24`, `:49`, `:58`), 4092 bytes / 71 lines |
| the map's Gaps contradiction | `memory/map/features/build-method.md` (no line) | **`:74-78`, the contradicting clause at `:77-78`** |

### 0.4 Every count in this document, re-derived here

Same tip as rev-7, so every figure below reproduces — which is the point of re-deriving it rather than
carrying it.

| what | this pass at `c4fcf5ad` |
|---|---|
| tracked specs with a Status header | **478** |
| of those, carrying a conforming `order` verb | **163 (34.1%)** |
| builds where NO spec carries one | **61 of 85** |
| multi-unit builds with ZERO order enforcement | **38 of 61** |
| build READMEs · with a units region · non-empty | **92 · 92 · 85** |
| roster median · mean · max · over five | **4 · 5.62 · 30 · 35 of 85 (41%)** |
| `--plan` sweep | **92 folders, 90 produced a `next:` line**: 69 terminal · 10 READY · 6 FORKED · 5 no-grade · 0 THIN · 0 MISSING; 2 refused earlier at exit 1 |
| gate-leg rows | **93** (and `govkit selfcheck` prints its own derivation: *"legs: 93 in the manifest · 69 claimed · 24 exempt"*) |
| `DIRECTIVES_CORE` | **17 handles over 10 M-sections**, `passes-harnessed:M6` last |
| handles present in the render | **0 of 17**, bare and backticked, one spelling at a time |
| anchor byte floor | **289** = 255 characters of handle + 34 backticks |
| registry entries · plain-`requires` edges | **25 · 9** |
| BUILD-METHOD sizes | template **24564/317** · render **24553/317** |
| UNATTENDED-PROTOCOL | **54772/649** in both halves against `INDEX_CAP_BYTES="61440"` |
| SKILL sizes | template **52471/791** · render **52443/791** |
| the M6 route sentence | **764 bytes / 8 lines** |
| the candidate child | **110 lines / 6933 bytes** |
| kit versions | agent-cap **1.12** · review-harness **1.6** · memory-tree **2.59** · unattended **1.17** |
| unattended version carriers | **8** = 3 engine constants + 5 template markers, each at exactly one marker |

### 0.5 What rev-7 established that rev-8 carries, re-verified where cited

rev-6's corrections A1–A6 and S1–S7 and rev-7's own corrections stand. Re-opened here: `--dispatch` refuses
exactly two things about a unit's STATE (`:4604`, `:4609`); `export const meta` is a SELECTOR
(`check-verifier-fanout.sh:86`, `check-workflow-syntax.js:30` applied at `:72`); `next:` has FOUR shapes
(`:2148`, `:2149`, `:2158`, `:2173`, `:2175`, `return 0` at `:2177`); the loop predicate has **SIX sites in
THREE forms** (`agent-cap.js:705`, `:711`, `:738`, `:910`, `:934`, `:944`); and `UNATTENDED-PROTOCOL.md:642`
still carries the pass-order over-claim.

---

## §1 — THE DEFECT

Three independent failures. Fixing one alone changes nothing observable.

**(a) NO ROUTE.** `passes-harnessed:M6` sits in `DIRECTIVES_CORE` (`unattended.sh:469` — seventeen
`handle:section` entries, `passes-harnessed:M6` last, no scope segment, so `scope_of` returns `all` at
`:505-514`). `## M6 — Passes, commits, parallelism` (`BUILD-METHOD.md:161`) states no harness rule, and
**0 of the 17 handles appear in `memory/guides/BUILD-METHOD.md`**, bare or backticked, re-derived one
spelling at a time this pass. The gate grading the handle, check 16 arm B at `check-unattended.sh:1592`,
is `grep -qE "^## $sec( |\$)"` over a `core` list built at `:1474-1487` — it asserts the section EXISTS
and never opens its body; its refusal is `:1593`. Both halves of the byte-compared protocol pair are
identical (**54772 bytes / 649 lines** each), so the parity legs are green over a sentence incomplete in
both.

**(b) WRONG SHAPE.** BUILD is one `agent()` holding the whole roster (`unattended-build.js:485`,
`renderRoster` defined `:138` and called `:147`). **92 build READMEs, 85 with a non-empty generated units
region; median 4 units, mean 5.62, max 30; 35 of 85 carry more than five.** That prompt also carries a
live over-claim at `:495-497`, read this pass: *"THAT DISPATCH IS THE ORDER GATE: it refuses a unit that
is MISSING, THIN or out of the declared order"* — the third is conditional and the sentence does not say
so.

**(c) NO WITNESS.** The harness writes nothing to disk. `dRetiredFork` ran WITHOUT it and wrote `brief`
and `dispatch` rows anyway, so those rows witness nothing about the harness.

**The proximate cause of "several runs, none used the harness" is none of the three.** Until `532e6f2b`
the AUDIT stage was structurally dead — it ordered a sidechain agent to invoke the Workflow tool, which a
sidechain does not hold — so BUILD was unreachable through the harness. That is fixed. What remains
between a run and the harness is (a) and the enabling instruction in §4.3.

---

## §2 — THE HOIST

### 2.1 The mechanism, and what each dispatch actually buys

`unattended-build.js` ends after SPEC, AUDIT and DISPOSAL and returns the ordered roster. The run then
makes ONE `Workflow` tool call per unit with `scriptPath: tools/workflows/unattended-unit.js` and that
unit's args.

Three properties, all read at the tip this pass:

- **A `Workflow` call consumes no slot.** `guardAgentSpawn` is reached only on
  `data.tool_name === 'Agent'` (`agent-cap.js:1494-1499`). N main-loop Workflow calls do not spend the
  five-per-prompt direct-spawn budget, and N is not bounded by it.
- **Each `scriptPath` call re-reads the child and runs FOUR rules over it — THREE burst rules and ONE
  join rule. That is the whole of what the re-read buys.** `:1505-1506` takes `tool_input.script` else
  `tool_input.scriptPath`; `:1509` is `readFileSync(spath, 'utf8')`; an unreadable path is DENIED at
  `:1510-1517` (re-observed this pass: an MSYS-style `/c/Users/…` path → **exit 2, ENOENT**). The bytes
  then feed, in order:

  | site | rule | class |
  |---|---|---|
  | `:1521` | `fanoutFindings` — a verify/fan-out stage spawning one agent per item | **burst** |
  | `:1541` | `capFindings` — a bound this file cannot resolve at or under `MAX_VERIFIERS` | **burst** |
  | `:1562` | `offendingLines` — raw `parallel(` / `pipeline(` | **burst** |
  | `:1593` | `scanJoinFindings` — **RULE 5, the ref-keyed verdict join** | **join** |

  The hook says this about itself at `:1559-1560`: *"the three rules above all prevent a BURST, the
  expensive failure this hook exists for, while a ref-keyed join is a wrong verdict, which is cheap to
  re-run"*, and `:1592` labels rule 5 *"LAST because it is the cheapest failure to recover from."*
  **rev-7 called all four burst rules; that was wrong, and it changes §2.4's residual clause.** Nothing at
  any of the four sites reads the prompt, the agent count, the nesting, or the marker. And `:1519` is
  `if (!script) process.exit(0)` — a `name:` call supplies no source and the hook approves it having read
  nothing (re-fixtured this pass: `{tool_name:'Workflow', tool_input:{name:'somewf'}}` → **exit 0**). So
  even this coverage is bought by §4.3 pinning `scriptPath`, and by nothing else.
- **The child is judged by two of its five stated constraints.** See §3.3 for exactly which.

Fixtured this pass at `c4fcf5ad`, in `scriptPath` mode, exit codes captured without a pipe:

| fixture | exit |
|---|---|
| the candidate child, pristine, by Windows-form `scriptPath` | **0** |
| + `for (const u of cfg.units) { await agent(…) }` appended | **2**, `a verify/fan-out stage spawns one agent per item` |
| `{tool_name:'Workflow', tool_input:{name:'somewf'}}` | **0**, nothing read |
| `scriptPath` given as an MSYS `/c/Users/…` path | **2**, `ENOENT`, fail-closed |

rev-6's wider fixture table (a second `await agent(…)` exfiltrating an ssh key → 0; a nested
`await workflow({scriptPath:…},{})` → 0; `export const meta` deleted → 0; `Promise.all(x.map(u=>agent(…)))`
→ 2; raw `parallel(` → 2; `for await (` → 0; `do…while` → 0) is CARRIED and was not re-run in this pass.
It is stated as carried, not as measured here.

### 2.2 The hoist's ranking, and the fork that is now closed

rev-3 through rev-5 ranked the hoist first because it closed hole D's width. rev-6's A1 showed that
closure was much weaker than claimed and re-argued the ranking from scratch on two grounds that survive:

**The baseline nobody priced correctly.** Under rev-3's shape the parent looped and called
`workflow(child)` N times **from inside its own sidechain**. `agent-cap.js:9` states it in the file's own
WHY block — *"workflow sidechains don't run hooks"* — and `:23-24` repeats it for the Agent modality:
*"Agents spawned INSIDE a workflow sidechain remain uncounted and always will be — no hook runs there."*
So under rev-3, **each per-unit dispatch fired ZERO checks**. **The delta is ZERO TO FOUR**, not
one-read-per-build to one-read-per-dispatch.

**The larger half is DELETION.** The hoist removes the callee, so W1–W6, unit U3, rulings R1 and R7 and
the resume re-entry contract become unnecessary rather than satisfied. Each is machinery this project
would otherwise have had to land, gate and observe failing (charter §7: *"A new gate is not landed until
its failing case has been observed"*).

**THE FORK IS CLOSED, AND IT CLOSED THE RIGHT WAY.** rev-6 §2.2 ended: *"If the owner declines to put the
loop in the Skill, the hoist has no carrier at all and the design collapses."* **The owner ruled on
2026-09-04 that `tools/unattended/SKILL.template.md` joins the veto-2 list.** That is not a decline; it is
the stronger form of the same answer. The Skill carries the loop AND every edit to it is now an owner turn,
so the carrier the hoist depends on is a reviewed one. **N1 is settled in the hoist's favour and this
document opens no successor fork.**

**What the hoist costs, priced honestly and not discounted.**

1. The program-held guarantee weakens from *"BUILD is unreachable except through SPEC and AUDIT on a
   terminal verdict"* to *"the ROSTER is not handed out early"*.
2. Loop completeness and order move to the RUN, backed by `build-complete` term 5 alone
   (`unattended.sh:3353`, read this pass), overridable by `--override build-complete`.
3. N returns to the main loop is N stall points, unmeasured in either direction (§2.5).
4. `tools/unattended/SKILL.template.md` becomes the sole carrier of the loop's correctness — now an
   owner-gated carrier, which is stronger than rev-6's position and still not a gate on its content (§10).
5. The Workflow-authorization premise is UNVERIFIED and the hoist multiplies it N+1 times (§8 item 1).

### 2.3 What the harness still buys — the honest statement

**The price.** A run that ignores the handout and dispatches anyway is refused **only** if the unit has
no tracked spec (`unattended.sh:4604`) or grades THIN (`:4609`). It is not refused for being FORKED, for
being already CLOSED, or for having been dispatched before. The order gate that would catch a skip is
opt-in on a spec `order` verb **163 of 478 tracked specs carry**, and it is satisfied by a declaration
row the run writes itself (`:4647`, written at `:4813`). `pass-order history` catches none of this — see
§3.4.

**Does the harness still earn its existence?** Yes, and narrowly: **it makes the review round a program's
output rather than an agent's recollection, and it hands out the roster only on a terminal verdict — it
buys nothing about the build loop.** Concretely: three schema'd agent stages (`unattended-build.js:230`,
`:294`, `:388`) plus one sub-workflow (`await workflow(` at `:327`), a convergence gate over `--review`'s
verdict, and a run-integrity return block. That is a program. It is not the program rev-3 described, and
M6 and PROTOCOL §12 must stop saying it is.

### 2.4 The residual window — ONE CLASS narrowed, and CONDITIONAL

The hoist narrows the window from "read once for N dispatches" to "read once per dispatch", and the
narrowing covers **exactly what the four rules of §2.1 hold: three burst shapes and one join shape.** A
run that rewrites the child into a loop around a spawn, an unsizeable fan-out receiver, a raw
`parallel(`/`pipeline(`, an unresolvable bound **or a ref-keyed verdict join** between dispatch k and k+1
is DENIED at k+1 — the loop-around-spawn arm was re-fixtured DENY at exit 2 in this pass.

**A run that rewrites it any OTHER way is admitted at every one of the N dispatches** (rev-6's fixtures,
carried). **The re-read buys four rules, not a file — and one of the four is not even about a burst.**

**Three preconditions even on that narrow claim:**

1. **The dispatch is by `scriptPath`.** A `name:` call reads nothing (`:1519`, re-fixtured **exit 0**).
   §4.3 pins it; nothing else does. The hole's declared home is `memory/guides/REVIEW-PROTOCOL.md:93-96`,
   under *"Where enforcement does NOT reach"*.
2. **The dispatch is not by inline `script`.** In that mode the hook judges the payload and the tracked
   file is never opened. U4's both-modes check is a **compatibility measurement**, not a sanctioned mode.
3. **The hook's cwd resolves the path.** `:1509` passes the payload string verbatim with no
   `path.resolve`. **An unresolvable path fails CLOSED** (re-observed, `:1510-1517`). The unfixed half is
   a relative path that resolves in the WRONG tree.

**What remains, closed by nothing here:** the child's CONTENT between dispatches; the PreToolUse-to-load
race (NOT VERIFIED racable); that nothing re-checks the child does not NEST (`grep -c "workflow("` over
`tools/hooks/agent-cap.js` = **0**, derived this pass); and the class nothing under the run's own uid
binds. All four are in §10.

**Home for the residual.** `memory/guides/UNATTENDED-PROTOCOL.md:515-521` already lists this class
(*"What it does not close, stated so no reader has to discover it"*, read this pass at `:515`). **THREE**
clauses join it, and the first is worded to the corrected rule set:

- *a run that rewrites the child script it dispatches into anything but a fan-out burst or a ref-keyed
  verdict join*;
- *a run that rewrites it between the hook's read and the runtime's load*;
- *a run that dispatches that child by `name:` or by inline `script`, where the hook reads no tracked
  bytes at all*.

Three clauses, in both halves of the byte-compared pair. No new section.

### 2.5 The mutual exclusivity, the stall surface, and the halt code

**The hoist and any future extension of the slot ledger to `Workflow` calls are incompatible.**
`guardAgentSpawn` claims a numbered slot per (session, prompt) with `MAX_VERIFIERS = 5`
(`agent-cap.js:403`), and it is reached only on an `Agent` payload (`:1494-1499`). A hoisted build makes
one `Workflow` call per roster unit from one prompt. **35 of 85 builds with a non-empty roster carry more
than five units — 41% of this corpus.** A ledger extended to `Workflow` would deny those builds at unit
6, mid-build. The note is recorded in `tools/hooks/agent-cap.js`'s slot-ledger comment block and in
`tools/hooks/README.md`'s `## Direct spawns are COUNTED, not parsed` section (`:119-126`, read this pass,
whose `:121-123` states the count *"is the only enforcement reaching a fan-out made outside a workflow
script"*), which is the first place a reader asking *"why not count Workflow too?"* arrives. Both files
ship with the `agent-cap` kit, so the edit changes adopter bytes and owes the §4.6 bump.

**The keepalive is TIME-keyed, so N returns cost it nothing.** `.unattended.conf:50` is
`KEEPALIVE_INTERVAL="every 10 minutes (cron 3-59/10 * * * *)"`. A run stalled after dispatch 3 of 12 is
woken by the same cron as one stalled inside a long BUILD call.

**`KICKOFF_EXITS` stays at 6.** The floor is `KICKOFF_EXITS="6"` (`.unattended.conf:57`) and grades the
kickoff ENGINE's enumerated interactive exits. A Workflow return is not a kickoff step, so widening it
would be a category error.

**The halt vocabulary needs no new member.** `.unattended.conf:160` declares `HALT_FLOOR="7"` against
`HALT_CODES_CORE` (`unattended.sh:468`, seven members, read this pass). A `committed:false` stop picks
`acceptance-underivable`, `gate-red-out-of-scope` or `fork-unresolvable`.

**NOT VERIFIED that the stall rate rises.** Baseline over the **37 tracked `RUN.md` at `c4fcf5ad`**:
LANDED 24, ABORTED 7, LANDING 4, BUILDING 2 (carried from rev-7's derivation at this same sha and marked
as carried). The separating probe: on any record sitting in `BUILDING`, count its `dispatch · item` rows
(grammar at `:4647`, written at `:4813`) against its roster size. A run that went quiet BETWEEN dispatches
has k rows for a roster of N>k. **The hoist increases the NUMBER of stall points and decreases the COST of
each, and this document asserts nothing about which dominates.**

---

## §3 — THE TARGET SHAPE

### 3.1 Stages

Inside the program: **SPEC** (`unattended-build.js:230`, unchanged); **AUDIT** (unchanged, including the
blob-resolver agent at `:294`, its `await workflow(` at `:327` and the round-recording agent at `:388`);
**DISPOSAL** as its own whole-set stage, run as its own `agent()` call, with the roster not returned
unless it reports done. Then the program ENDS and returns. **BUILD is not a stage of it.**

Outside the program, in the main loop: one `Workflow` call per unit, by `scriptPath`, in roster order,
awaited.

### 3.2 The parent, verbatim shape

```js
// ============================================================ STAGE 3 — DISPOSAL, whole-set
// Standing blockers are disposed BEFORE any unit is built, by ONE agent over the whole spec set.
// Not carried into the first unit: disposal is authority over every unit's spec, and a resumed run
// whose first roster element is already built would spend it on a child that does nothing.
phase('Build')
if (verdict !== 'CONVERGED') {
  const d = await agent(GROUND + disposal, { label: 'dispose:' + slug, schema: DISPOSAL_SCHEMA })
  if (!d || d.disposed !== true) {
    return {
      slug: slug, base: base, round: roundNo, verdict: verdict, blockers: au.blockers,
      roster: [],
      note: 'DEGRADED — blockers were not disposed: ' +
            ((d && d.why) || 'the disposal agent returned nothing') +
            ' — no roster is handed out, so no unit may be dispatched',
    }
  }
  log('blockers disposed: ' + d.summary)
}

// ============================================================ THE HAND-OFF
// The roster is a RETURN VALUE, not a loop. Each element is dispatched by the RUN, as its own
// `Workflow` tool call against tools/workflows/unattended-unit.js BY scriptPath, so PreToolUse fires
// once per unit and the child's CURRENT bytes are read once per unit. What that read judges is three
// fan-out rules and one ref-keyed-join rule — not the prompt, not a second spawn, not a nested call.
// Nothing here enforces any of it.
//
// `specPath` IS EMPTY FOR EVERY UNIT STAGE 1 JUST AUTHORED. `units` arrives in args and `ordered` is
// never mutated, so this program cannot know a path SPEC created. The caller re-reads
// `--plan <slug> --paths` after this returns and joins by id BEFORE dispatch 1; the field is carried
// only so a caller that already had a path does not lose it.
return {
  slug: slug,
  base: base,
  round: roundNo,
  units: ordered.length,
  specced: speccedCount,
  specRefused: specRefused,
  verdict: verdict,
  blockers: au.blockers,
  lastReport: lastReport,
  roster: ordered.map(function (u) {
    return { id: u.id, order: u.order, specPath: u.specPath || '', briefPath: u.briefPath || '' }
  }),
  dispatch: {
    scriptPath: 'tools/workflows/unattended-unit.js',
    args: { repo: repo, slug: slug, driver: DRIVER, ground: GROUND, checklist: CHECKLIST },
    perUnit: ['unitId', 'specPath', 'briefPath'],
    resolvePathsWith: DRIVER + ' --plan ' + slug + ' --paths',
  },
  note:
    specRefused.length || verdict !== 'CONVERGED'
      ? 'DEGRADED — ' + specRefused.length + ' spec(s) refused, verdict ' + verdict
      : 'prologue complete; ' + ordered.length + ' unit(s) to dispatch, in the order above; ' +
        're-read ' + DRIVER + ' --plan ' + slug + ' --paths and join by id before dispatch 1',
}
```

Five things in that block are load-bearing.

- **`roster` is `[]` when disposal fails, and the note says why.** An empty roster is the refusal, spelled
  so a run reading only `roster.length` still stops.
- **`resolvePathsWith` exists because the program cannot know a path its own SPEC stage authored.**
  `units` comes from args and `ordered` is sorted and never touched again; the file is **531 lines**
  (measured this pass) and no `specPath` site is a write. The return names the command that resolves them.
- **`dispatch` carries the invariant args, and `perUnit` names the three that vary.** The roster is NOT
  among them — the child never receives it.
- **No `reportPath` reaches any child.** What a unit must know beyond its spec goes into its BRIEF file,
  because that is the only carrier `--brief` hashes: it refuses an untracked path (`unattended.sh:4199-4200`,
  read this pass) and hashes via `git hash-object` (`:4203`); nothing hashes a prompt string.
- **`checklist` is in `dispatch.args`.** `unattended-build.js:499` spells the bug-class command inline
  today (verified this pass — the file's only `gotchas.py` occurrence) because a sidechain agent inherits
  the governing doc but not the unattended Skill.

`renderRoster` (`:138`, called `:147`) survives — SPEC (`:230`) and the blob resolver (`:294`) still
consume it — and U5's acceptance asserts it is absent from everything downstream of the audit.

### 3.3 The child, `tools/workflows/unattended-unit.js`

The candidate file is `scratchpad/unattended-unit.candidate.js`, edited in rev-6's pass and unchanged
since. Re-measured this pass: **110 lines, 6933 bytes**. Gates re-run with each checker taken from the
`c4fcf5ad` snapshot, exit codes captured without a pipe:

- `node tools/workflows/check-workflow-syntax.js <child>` → **exit 0**, `workflow-syntax: 1 workflow script(s) parsed clean`.
- `bash tools/workflows/check-verifier-fanout.sh <child>` → **exit 0**, `verifier-fanout: clean — 1 workflow script(s) obey the ≤5-verifier rule`.
- `node tools/hooks/agent-cap.js` fed `{"tool_name":"Workflow","tool_input":{"scriptPath":"<Windows-form path>"}}` → **exit 0**.
- Properties re-derived: `grep -c 'tools/'` = **0**, `grep -c 'agent('` = **1**, `grep -c 'workflow('` = **0**, the `export const meta` DECLARATION at **`:30`** (`:6` and `:8` are comments about it, so a bare line-count returns 3 and means nothing), `grep -c "THAT DISPATCH IS THE ORDER GATE"` = **0**, `grep -c CLOSED` = **1**.

**Its properties, each with what actually holds it.**

- **`export const meta` — ASSERTED ONCE AT LANDING, ENFORCED BY NOTHING STANDING.**
  `check-verifier-fanout.sh:86` selects its population by
  `grep -qE '^[[:space:]]*export[[:space:]]+const[[:space:]]+meta[[:space:]]*='`, and
  `check-workflow-syntax.js:30` is `const MARKER = /^\s*export\s+const\s+meta\s*=/m` applied at `:72` as
  `if (!explicit && !MARKER.test(src)) continue` — both read this pass. **A child that loses the marker
  is not failed; it is removed from both populations.** Disclosed in §10.
- **No loop around a spawn, and no unsizeable fan-out receiver — ENFORCED, per dispatch, by the shipped
  hook.** Re-fixtured this pass at exit 2.
- **No `function`, no `=>`, no non-receiver array method — a FILE-STYLE RULE WITH NO GATE.** The hook
  denies a `.map()` only where the map is the fan-out RECEIVER. Disclosed in §10.
- **It never nests, and NOTHING re-checks that.** `grep -c "workflow(" tools/hooks/agent-cap.js` = **0**,
  and a call fired from inside this sidechain reaches no hook (`agent-cap.js:9`).
- **It spells no `tools/` literal** — measured **0**. So no install-prefix ratchet row and no
  `method-carriers.txt` row.
- **`why` is REQUIRED and never an absence**, the same reason `unattended-build.js:118-124` refuses a
  missing `units` (read this pass, and its message at `:120-122` names `--plan` as the source).

**The status flip is IN the file.** `unattended.sh:2144` —
`case "$st" in CLOSED|WONTDO) [ "$state" = "READY" ] && state="DONE" || state="DONE ($state)" ;;` — is
the **only** thing that removes a unit from `next` candidacy, and `$st` is the spec's status header. Under
the hoist §3.5 makes `--plan` the loop counter, so a child that commits without flipping the header would
leave `--plan` naming the same unit `READY - build it` forever. The child's prompt therefore carries:

> Commit with the unit id in the subject. IN THAT SAME COMMIT, set this unit's spec status header to
> CLOSED — or to WONTDO with a reason. That header is the only fact the driver's --plan verb reads to
> decide a unit is finished, so a unit built without it leaves the run's own loop counter naming this
> unit again, forever.

**U4 asserts it.** Nothing else in the design closes it — `--plan` is read-only over tracked specs by
construction (`unattended.sh:2043`, `git ls-files "$dir/spec/*.md"`, read this pass).

### 3.4 What buys order — the refusals, scoped correctly

A workflow script has no filesystem, so it cannot verify a commit or re-read `--plan`. **The JS loop
bought no order and this document does not claim it did.** What changes is that the RUN, not a script,
now sits between units, and the run CAN read the tree.

- **`--dispatch` refuses exactly two things about the UNIT'S STATE.** `:4604` — a unit no tracked spec
  under this build defines (M2's MISSING). `:4609` — a unit whose spec grades THIN, and that is the only
  arm in its `case`. It does **not** refuse a FORKED unit, an already-CLOSED one, or a re-dispatch.
- **It refuses more about the WRITE SET, and that population is not this design's concern** — it is where
  `UNATTENDED-PROTOCOL.md:646-649` already documents it.
- **The order gate is OPT-IN and ESCAPABLE.** `:4630` runs it only `if [ -n "$_d_ord" ]`; `:4639` is
  `[ -n "$_o_ord" ] || continue`, skipping any sibling with no verb. Re-derived over the tip against
  `ORDER_OK_RE` (`unattended.sh:354`): **163 of 478** tracked specs with a Status header carry a
  conforming verb (34.1%); **61 of 85** builds carry none on any spec; **38 of 61** multi-unit builds have
  zero order enforcement available. And `grep -c "out of the build's own declared order"` over
  `tools/unattended/unattended.test.sh` = **0**: the gate the design leans on has never been observed to
  fire. **U5 adds that arm.**
- **A DECLARATION ROW SATISFIES "DISPATCHED".** `:4647` is
  `grep -qE "^[0-9][0-9-]*T[0-9:]*Z dispatch · item [0-9a-f]+ $_o_id · reason " "$rel" … && continue` — a
  sibling carrying a dispatch row stops blocking whether or not it was ever built. `--dispatch` writes
  that row itself (`park "$rel" dispatch "$grp $unit" "$want"` at `:4813`), and `SKILL.template.md:543`
  orders the declaration BEFORE the pass. So a child that fails at unit 1 leaves exactly the record that
  waves units 2..N through.
- **`pass-order history` grades SPEC-BEFORE-CODE ORDER — not the build's declared UNIT order, and not
  completeness.** (rev-7's heading said it graded neither order nor completeness, which contradicts the
  leg's own header; the body was right and the heading was not.) `check-pass-order.sh:9-10` states what it
  DOES check: *"for every unit a build README carries as CLOSED, the commit that BUILT that unit had a
  conforming, non-THIN spec for it at its first parent."* `:21` says *"this measures ORDER and nothing
  else."* Under WHAT THIS DOES NOT CHECK it excludes *"whether a build pass was DISPATCHED. That is a
  different join over the same range"* (`:22`) and *"anything about a unit that is not CLOSED"* (`:23-24`).
  **So a run that builds three of twelve is green, because the nine it skipped are not CLOSED** — and no
  part of this leg looks at whether unit 2 followed unit 1.

### 3.5 Termination, completeness and resume

**rev-3 §3.5 stays DELETED, and so does `args.verdict`.** Under the hoist a resumed run mid-BUILD does
not call the harness at all.

**Which unit is next is a TREE FACT, and there is already a verb.** `--plan <slug>` takes its unit SET
and ORDER from the generated units region, joins that roster against the tracked specs, and names the
next one. **FOUR outcomes, all read this pass:**

- `next: <id> (READY - build it)` (`:2149`) — dispatch that unit.
- `next: <id> (THIN)` / `(FORKED)` (`:2148`) / `(MISSING - spec it first)` (`:2158`) — **do not
  dispatch.** `--dispatch` refuses THIN (`:4609`) and MISSING (`:4604`); **it does not refuse FORKED.**
- `next: none - every tracked spec is terminal` (`:2175`) — the loop is done.
- **`next: none - no tracked spec grades as a unit (see the NOT A UNIT rows above)` (`:2173`) — A REFUSAL,
  NOT A COMPLETION.** Printed when `_graded` never reached 1, and `verb_plan` still returns 0 (`:2177`).

**Both non-terminal shapes are LIVE at the tip.** The sweep was RE-RUN in this pass: `--plan <slug>` over
every build folder in a `git archive origin/main` snapshot; **92 folders, 90 produced a `next:` line**, the
other two refused earlier in `verb_plan` at exit 1 (aFerriedDossier, bThriftyBellows). The distribution:

| shape | builds |
|---|---|
| `next: none - every tracked spec is terminal` (`:2175`) | **69** |
| `next: <id> (READY - build it)` (`:2149`) | **10** |
| **`next: <id> (FORKED)` (`:2148`)** | **6** — aBatchedLintel, aSurfacedLexicon, aTetheredScratch, bConvergentLodestar, dNarrowedAnchor, dPromptedSeam |
| **`next: none - no tracked spec grades as a unit` (`:2173`)** | **5** — aDeployScout, aKitHardener, aLeanRework, aPortableWarden, aRatchetForge |
| `(THIN)` · `(MISSING - spec it first)` | **0 · 0** |

**Six builds where a run following the bullet would dispatch a unit nothing refuses, and five where a run
branching on `next: none` would call an empty grade a finished build.**

**So the run reads `--plan <slug> --paths`, never a cached list**, and confirms against it after every
return.

**A child returning `committed:false` STOPS the loop, and that stop is held by the RUN alone.** The order
gate does not refuse the successor once unit 1 has a declaration row (`:4647`), and it does not run at all
unless both units carry an `order` verb (`:4630`, `:4639`), which **38 of 61 multi-unit builds** cannot
offer. The run records the `why`, then parks or halts, and nothing refuses it if it does not.

**What catches an incomplete loop: ONE thing.** `build-complete` at `--close`, a `DOD_CORE` item
(`unattended.sh:344`, **12 items**, derived this pass) whose term 5 message is verbatim at `:3353`: *"a
unit of this build is not terminal, so the build is not done; each row below is a unit whose status is
neither CLOSED nor WONTDO"*. **Its only exit is `--override build-complete`.** Term 5 is downstream of the
same status flip §3.3 adds, so the flip is load-bearing twice.

**Resume gets strictly better.** A compaction mid-build loses at most the current unit: the run re-reads
the run-state file, reaps and re-schedules the keepalive, asks `--plan <slug> --paths` for `next` and the
spec paths, recovers `briefPath` for any already-briefed unit from that file's
`brief · item <unit> · reason <hash12> <path>` rows (`unattended.sh:4217`, parked `:4225`, staged `:4226`,
all read this pass), and dispatches. No harness call, no SPEC pass, no review round.

---

## §4 — THE ROUTE

### 4.1 The carrier fix

Re-pointing the handle away from an M-section is not available: check 16 arm A accepts only `/^M[0-9]+$/`
as a Carrier cell and marks anything else `:AMBIGUOUS` (`check-unattended.sh:1496-1507`, read this pass —
the awk emits `h ":AMBIGUOUS"` at `:1506`). M6 is the only M-section stating a pass-sequence rule.

1. **`tools/memory-tree/BUILD-METHOD.template.md`, inside `## M6`** — the route sentence, rewritten for
   the hoisted shape and carrying the `parallel-when-disjoint` clause:

   > **The route is the kit's build harness.** `{{TOOL_ROOT}}workflows/unattended-build.js` runs SPEC,
   > AUDIT and DISPOSAL as stages of one program and returns the ordered unit roster only on a terminal
   > `--review` verdict; the run then dispatches `{{TOOL_ROOT}}workflows/unattended-unit.js` once per
   > unit, by `scriptPath`, each child handed that unit's brief and that unit's spec and never the
   > roster. **One unit per dispatch is the SEQUENCE fallback this section already names**: units
   > sharing an `order` value are the parallel group, and a group whose `--dispatch --writes`
   > declarations are proven disjoint may be dispatched together. It buys ORDER and never ENFORCEMENT:
   > `passes-harnessed` names this route, and what refuses is `--dispatch` at the moment of the act.

   **Re-measured this pass: 764 bytes / 8 lines.** It carries the backticked `` `passes-harnessed` ``
   anchor §5 requires, **and the two backticked `workflows/*.js` paths check 31 reads (§4.5e).** It takes
   no side on recipe mode — no clause admits or excludes it, which is what Ruling 3 requires until U8
   reports. The parallel clause is not decoration: `parallel-when-disjoint:M6` is in `DIRECTIVES_CORE`
   with no scope segment, and §4.4 shows prose cannot make a core directive optional. The paths are
   written `{{TOOL_ROOT}}workflows/…` because `{` and `}` are in the install-prefix gate's excluded lead
   class (`check-install-prefix.sh:60-62`, the regex at `:63`, read this pass: *"`}` and `{` join the
   excluded lead characters so a placeholder-prefixed path … is not itself a hit"*).
   **This design builds no concurrent dispatch path** — §10 carries that.
2. **`memory/guides/BUILD-METHOD.md`** — regenerated, never hand-edited:
   `bash tools/memory-tree/kit-dogfood-parity.test.sh --render`. Byte-compared by
   **`kit/dogfood doc parity`** (chunk `declarations`, subject `repo`, guard includes
   `memory/guides/BUILD-METHOD.md` and `tools/memory-tree/`).
3. **The budget line** (`BUILD-METHOD.template.md:8`) — raised and gated. This is Ruling 2 and it is §5B.
4. **`tools/unattended/PROTOCOL.template.md:635-645` and `memory/guides/UNATTENDED-PROTOCOL.md:635-645` —
   a CORRECTION IN TWO PLACES.**

   **First, `:635-637`.** The live sentence, read verbatim this pass:

   > **The route is the kit's build harness**, taken in `prompt` and `slug` mode. It drives SPEC, AUDIT
   > and BUILD as stages of ONE program, so BUILD is unreachable except through both and on a TERMINAL
   > `--review` verdict. Recipe mode does not take it: its pieces are not specs.

   Its first two sentences are TRUE today and FALSE after the hoist, and they become: the harness drives
   SPEC, AUDIT and DISPOSAL as stages of one program and hands out the ordered roster only on a terminal
   `--review` verdict; the build loop is the RUN's own, one `scriptPath` dispatch per unit; **what the
   program holds is that the roster is not handed out early, not that the build is unreachable early.**

   **THE THIRD SENTENCE IS NOT TOUCHED BY THIS BUILD, AND IT CONTRADICTS THE REGISTRY.** `:637` says
   recipe mode does not take the route; `unattended.sh:469` carries `passes-harnessed:M6` with no scope
   segment, and `scope_of` (`:505-514`) therefore returns `all`. **This design ships with that
   disagreement live, on the bar, until U8 reports** — the M6 sentence asserts NEITHER side, and no other
   edit in §4.6 takes one. §9 D3 states the decision the probe feeds.

   **Second, `:642`.** The TWO LIMITS paragraph reads *"what refuses is `--dispatch` at the moment of the
   act and the pass-order leg over the commit graph"* — read verbatim this pass. `check-pass-order.sh:22`
   says under WHAT THIS DOES NOT CHECK that it grades nothing about dispatch, and `:23-24` that it grades
   nothing about a non-CLOSED unit. **STRIKE `and the pass-order leg over the commit graph` from `:642` in
   BOTH halves.**

   **What §12 must ALSO stop saying.** Wherever it names what `--dispatch` refuses about a unit's STATE,
   it names the two by what they are — **no tracked spec** and **THIN** — and claims no FORKED refusal and
   no re-dispatch backstop. Also in §12: the field list for the dispatch args, by NAME and with no literal
   script path, which is what keeps this carrier off the install-prefix ratchet. Room:
   `memory/guides/UNATTENDED-PROTOCOL.md` is **54772 bytes / 649 lines** against `INDEX_CAP_BYTES="61440"`
   (`.memory-tree.conf:148`), so **6668 bytes free**. The pair is byte-compared by **`unattended kit
   gate`** and **`unattended skill wiring`**, both chunk-and-subject configured to run on every bar.
5. **§9's residual clauses** (`memory/guides/UNATTENDED-PROTOCOL.md:515-521` and its template twin) —
   **THREE** clauses join the existing list, per §2.4, the first worded to the three-burst/one-join
   correction.
6. **`memory/guides/SESSION-KICKOFF.md` stamps — BOTH.** `last-audit` and `last-body-change`:
   `memory/guides/BUILD-METHOD.md`, `tools/gate-legs.json` and `.unattended.conf` are all on the manifest
   watch line, and C9 is excluded from the staged leg by its own header (`manifest-check.sh:373-375`, read
   this pass), so it reds at the full bar rather than pre-commit. Re-derive the commit count against
   `[ "$c9n" -ge 10 ]` (`:400`) at the moment of the commit.

### 4.2 `--plan --paths` — same flag, THREE reasons

`verb_plan` prints `printf '%-34s %-11s %s\n' "$id" "${st:-?}" "$state"` (`:2145`) — id, spec status, plan
state. No spec path. **`bash tools/unattended/unattended.sh --plan <slug> --paths`** emits one
TAB-separated row per unit: `id<TAB>status<TAB>state<TAB>specPath`.

1. So the run can build the harness's `units` arg before the harness call.
2. **So the run can dispatch AT ALL.** `specPath` is empty in the returned roster for every unit SPEC just
   authored, and the child throws without it. The run re-runs `--plan <slug> --paths` **after the harness
   returns and before dispatch 1**, and joins by id.
3. So a resumed run that lost the roster has a source for `specPath` with no harness call.

**Order comes free with it** — the region is rendered in build order, so a `--paths` listing IS build
order.

**`briefPath` is NOT obtainable from any VERB**, because the run AUTHORS that file per unit. **It IS
recoverable on resume** from the run-state file's `brief · item` rows (`unattended.sh:4217`).

**The harness's refusal text is corrected** to name `--plan --paths` for the id set, status, spec path and
order, and the run's own brief for `briefPath`. Today it says *"The caller derives them from `--plan`"*
(`unattended-build.js:118-124`, message at `:120-122`, read this pass), which is false for the path.

### 4.3 The Skill carries the LOOP

**Why this bullet exists.** The Workflow tool refuses a call the user did not authorize, and a skill's own
instructions are believed to be one of the listed authorizations. **That belief is NOT VERIFIED** —
`SKILL.template.md`'s frontmatter declares only `name` and `description` (`:1-4`, with the
`gov:kit unattended@1.17` marker at `:5`), no allowed-tools key, and `grep -cEi "workflow|unattended-build"`
over its **791 lines** returns **0**. **The hoist raises the stake from one call to N+1, so U2's acceptance
includes one OBSERVED dispatch.**

**Placement, verified at the tip.** `tools/unattended/SKILL.template.md` — **52471 bytes / 791 lines**.
`## While it runs` at **`:465`** is the section that holds `- ` items; `## While the work runs` at `:573`
is prose plus fenced blocks and is the wrong home. Insert between the `--dispatch` bullet (opens `:543`)
and the bug-class bullet (`:557`) — the two acts the CHILD performs, with this bullet as what causes it to
perform them.

**The sentence, as it ships:**

```markdown
- **At the BUILD boundary you make the Workflow calls YOURSELF, one per unit, and you delegate none of
  them.** A sidechain agent does not hold that tool, so a delegated invocation is a stage that cannot
  run. Call every one of them by `scriptPath` and NEVER by `name`: a `name:` call supplies the hook no
  source and it approves the run having read nothing. FIRST, call
  `scriptPath: tools/workflows/unattended-build.js` ONCE, with `args` carrying `repo`, `slug`, `base`,
  `units`, `briefDir`, `reviewDir` and `round`; each unit is `{id, order, specPath, briefPath}` and the
  array is ORDERED. Take the id set, the status, the spec path and the ORDER from
  `bash {{KIT_DIR}}/unattended.sh --plan <slug> --paths` — its rows are already in build order — and
  `briefPath` from the brief file you author for that unit. It runs SPEC, AUDIT and DISPOSAL and returns
  the ordered `roster` only on a terminal `--review` verdict; an empty roster is its refusal and you
  stop there. THEN, BEFORE dispatch 1, run `--plan <slug> --paths` AGAIN and join its rows onto the
  roster by id: the harness cannot know a path its own SPEC stage authored, so the `specPath` it
  returned for a freshly specced unit is empty and the child refuses without one. THEN, for each unit in
  that order, call `scriptPath: tools/workflows/unattended-unit.js` with `args` carrying `repo`, `slug`,
  `unitId`, `specPath`, `briefPath`, `driver`, `ground` and `checklist` — one call, AWAITED, before the
  next one begins, and never the roster. One unit per dispatch is M6's SEQUENCE fallback; a group of
  units sharing an `order` value whose `--writes` declarations you have proven disjoint may be
  dispatched together, which is what `parallel-when-disjoint` asks of you. Between calls ask
  `bash {{KIT_DIR}}/unattended.sh --plan <slug> --paths` which unit is next rather than trusting the
  list you are holding: it reads the tree, and your list did not survive the last compaction. **Its
  `next:` has FOUR shapes and you branch on all four.** On `(READY - build it)`, dispatch. On
  `next: none - every tracked spec is terminal`, you are done. On
  `next: none - no tracked spec grades as a unit`, YOU ARE NOT DONE — that verb found no unit at all and
  it still exits 0; read the NOT A UNIT rows above it and halt rather than closing. On a `next:` naming
  a unit as `THIN`, `FORKED` or `MISSING`, DO NOT DISPATCH IT — `--dispatch` refuses a THIN or an
  unspecced unit but it does NOT refuse a FORKED one, so nothing but you stops that call. Resolve the
  fork or spec the unit as its own pass, or halt with `fork-unresolvable`. A child returning
  `committed:false` STOPS the loop — record its `why`, then park or halt. Nothing refuses the next
  dispatch for you: the order gate treats an earlier unit's DECLARATION row as dispatched, and you wrote
  that row before the pass ran. `build-complete` at `--close` is what refuses you if you stopped early,
  and its only exit is `--override build-complete`. Without these calls the pass sequence is a rule you
  remember instead of a program you ran, and `passes-harnessed` names a route nothing took.
```

**Also**: the PROMPT path gets its own "Read `{{MEMORY_ROOT}}/guides/BUILD-METHOD.md` WHOLE" step. That
instruction exists at `:73` (slug path) and inside the recipe path's step 0 (`:316`), so the prompt path
reaches the method only through a doubly-conditional kickoff hand-back while `passes-harnessed` is scope
`all`.

**This whole subsection is now an owner turn.** See §4.4.

### 4.4 The Skill is a veto-2 carrier — the ruling, its reach, and its price

**The decision.** `tools/unattended/SKILL.template.md` joins the veto-2 list (owner, 2026-09-04). Veto 2
is `BUILD-METHOD.md:84` — discard any option that *"needs a new external dependency, install location,
public surface, or a change to a governance carrier"* — with veto 1 at `:83`, `:76` stating the mandate's
delegation *"does not reach veto 2's governance-carrier clause"*, and `:87` stating *"Vetoes 2 and 3 are
owner turns"*. All four lines read this pass. **No unattended run may take an edit to that file.**

**Why it is the right classification, by ANALOGY in the file's own terms.** `SKILL.template.md:363-364`
says *"What you may NOT do is edit the playbook. A run that rewrites the checklist it is graded by has no
rules left."* A near-duplicate bullet sits at `:489-491`. **Both sentences are about a PLAYBOOK — the
recipe-mode artifact — and not about the Skill**, which is why this is an analogy and not a citation of an
existing rule: the Skill is the checklist one level up, the document the run executes from, and the same
argument applies to it with nothing in the tree yet saying so.

**(c) THE RENDER IS NOT A SECOND CARRIER.** `.claude/skills/unattended/SKILL.md` is tracked (**52443
bytes / 791 lines**, 28 bytes under the template because placeholders substitute shorter), and
`adopt-unattended.sh:9` states what its `--check` does: *"`--check` is the merge-bar arm. It renders to a
temp file and DIFFS, so a hand-edited Skill reds."* That arm is the leg **`unattended skill wiring`**
(argv `bash tools/unattended/adopt-unattended.sh --check`, chunk `wiring`, subject `repo`, no guard —
read from `tools/gate-legs.json` this pass), so it runs on every bar. Therefore:

- **A run MAY regenerate the render from an owner-approved template.** `bash tools/unattended/adopt-unattended.sh`
  is a derivation, not an authoring act, and the wiring leg proves the output equals the template's render.
- **A run MAY NOT hand-edit the render**, and that one is CAUGHT rather than merely forbidden — the
  `--check` diff reds on every bar.
- **The owner gate binds the TEMPLATE.** Two different acts, and the design says which is which.

**(b) THE STANDING COST, and where someone meets it.** The cost is larger than "future Skill prose edits
are owner turns", because of a coupling derived this pass: `check-kit-versions.sh:179-192` requires a
`gov:kit unattended@<version>` marker in **every tracked `tools/unattended/*.template.md`** — measured,
five such templates, each carrying exactly one marker at 1.17 — and `:184-191` compares each against the
engine constant read at `:164`, with `:180-183` refusing a vacuous assertion if no template is tracked.
**So every `unattended` kit-version bump edits `SKILL.template.md`, and under this ruling every
`unattended` version bump is an owner turn.** That reaches five of this design's own units (§7) and every
future unit that touches the driver, its checks or its conf.

The note goes in **`tools/unattended/README.md`** (4092 bytes / 71 lines, four `##` sections at `:9`,
`:24`, `:49`, `:58`), as a new short section. Three placements were considered and two rejected for
reasons worth recording:

- **The Skill template's own head — rejected.** Everything there RENDERS into every adopter's Skill, so a
  note about gov's owner process would become run-time instruction bytes for people it does not govern.
- **`PROTOCOL.template.md` §12 — rejected.** Its audience is a RUN; this note's audience is a BUILD's
  author, and a rule filed where the wrong reader meets it is the §1(a) defect in miniature.
- **`tools/unattended/README.md` — taken.** It is the document open on the screen of anyone editing the
  kit, and it is where the version-bump obligation is already the maintainer's business.

**Honest limit, and it is why §10 keeps an entry.** An owner-gated carrier does not stop a run editing the
working tree. The tracked `.claude/settings.json` (45 lines, read this pass) declares PreToolUse matchers
on `Workflow|Agent` (`:5`) and `Bash|PowerShell` (`:14`) only — the `Read` matcher at `:35` is
PostToolUse — and carries no `permissions` block at all. **What the ruling buys is that the edit becomes a
REVIEWABLE ACT in a diff, on a file whose render is byte-compared on every bar. It does not buy that the
edit cannot happen.**

### 4.5 The adopter dependency — the edge, the validation, and the announcement

**The decision, corrected and retaken (owner, 2026-09-04).** `tools/unattended/kit.toml:7` becomes
`requires = ["memory-tree", "review-harness"]` **for ordering**, AND govkit learns to VALIDATE plain
`requires`, AND the unattended leg learns to ANNOUNCE a missing route. The owner was previously told the
edge alone would make an adopter get the harness or not get the kit. That was false, and §4.5a is the
measurement that proves it.

#### 4.5a What the edge buys, derived at source and OBSERVED

`requires` is read at exactly one place in the deployer: `derive_install_order` (`govkit.py:486-518`). Its
comprehension at `:504-505` is
`{d for d in (descs[i][0].get("requires") or []) if d in want and d != i}`, and its docstring at
`:495-496` says *"A dependency OUTSIDE the selection is not an error: `--kits drift-audit` is a legal
install and orders one entry. Only the edges among the selected ids constrain the order."* The only thing
it raises is a cycle (`:510-515`).

`resolve_selection` is **`:521-590`** and has **FOUR** `derive_install_order` call sites — `:558` (`--all`),
`:567` (`--kits`), `:582` (the target's own `deploy.toml` list) and `:590` (the registry default set).
**Re-derived over the whole function this pass**, because rev-7's `:519-583` truncated it before the fourth:
every call passes either `all_kits(descs)` or a `sorted()` of an already-fixed id list, and **not one of
the four adds a `requires` target to the selection.**

**And it is now OBSERVED, not only read.** In a `git archive origin/main` snapshot, against a scratch
target holding neither `memory-tree` nor `review-harness`:

```
python tools/govkit/govkit.py plan --target <scratch> --kits unattended
→ exit 0
→ "govkit plan — target <scratch> · selection: unattended"
```

**One entry. `memory-tree` — an edge that has existed all along — was neither pulled nor complained about.**
That is the whole of what the new edge would buy on its own. (A prerequisite discovered on the way: a target
with no `.governance/deploy.toml` makes `plan` exit **2** with *"no target descriptor … Refusing to guess"*,
so every acceptance arm below must `intake` or seed that file first.)

Unlike `requires_if`, which `selfcheck` check 7 validates against the registry (`govkit.py:1330-1333`,
*"entry '<eid>' requires_if names '<other>', which is not a registry entry"*), **plain `requires` gets no
registry-membership validation at all** — a typo names nothing and reds nothing. The declared chain is
`unattended → memory-tree` (`tools/unattended/kit.toml:7`), the new `unattended → review-harness`,
`review-harness → agent-cap` (`tools/workflows/kit.toml:7`) and `agent-cap → settings-merge`
(`tools/hooks/kit.toml:7`) — three deep, and none of it installs anything.

#### 4.5b (i) VALIDATE AT ADOPT TIME — arm A, the REGISTRY, in `selfcheck` check 7

**Which check: it EXTENDS check 7**, `govkit.py:1326-1341`, whose header at `:1326-1327` already reads *"a
requires_if condition names keys that resolve in the named kit's config lists, and names a kit that is a
registry entry."* The header gains the plain-`requires` clause and the body gains three lines modelled
byte-for-byte on `:1330-1333`:

```python
for dep in d.get("requires") or []:
    if dep not in descs:
        r.fail(f"entry '{eid}' requires '{dep}', which is not a registry entry — the edge then "
               f"orders nothing and reds nothing, which is how it was found")
```

**A new check number was rejected.** Check 7 is already the one place a dependency edge's kit NAME is
graded; splitting `requires` into check 7c would put one class in two places, which is the rule this
document keeps citing. The count of checks in the file is derived by the reader, never written in prose.

**REGISTRY, not installed set, and why.** `selfcheck` grades GOV's own descriptors and takes no `--target`
(observed: its output line is *"surface 64 tracked path(s) · 25 entr(y|ies) · 23 exemption(s) · 0
unclaimed"*). It has no receipt and no adopter tree to ask, so the only question it CAN answer is *does
this dependency name anything at all*. The installed-set question needs a target and is arm B.

**Does it red anything today? NO — and the predicate was RUN, not reasoned about.** Both candidate
predicates were executed over all 25 registry entries' descriptors this pass, resolving each descriptor
through `registry.toml`'s `[[entry]]` rows exactly as govkit does:

| | result |
|---|---|
| plain-`requires` edges in the tree | **9** |
| **HITS — an edge naming a non-entry** | **0** |
| near-misses — every edge that passes, enumerated | `agent-cap→settings-merge` · `check-agent-cap-restatement→agent-cap` · `check-microformats→playbook` · `codebase-map→memory-tree` · `drift-audit→memory-tree` · `memory-recall→memory-tree` · `playbook-render→playbook` · `review-harness→agent-cap` · `unattended→memory-tree` |

**The near-miss that matters is not in that table**: `requires` and `requires_if` are read from two
different keys, so a mis-spelled KEY (`require = […]`, or a `requires_if` typo'd to something else) is
invisible to both arms and always will be. That goes in §10.

**Failing case, staged and observed before it lands.** In a scratch clone: set
`tools/unattended/kit.toml:7` to `requires = ["memory-tree", "reviewharness"]`; run
`python tools/govkit/govkit.py selfcheck`; confirm a non-zero exit naming entry `unattended` and id
`reviewharness`; unstage. **The green half is already observed: the untouched tree exits 0 at the tip in
this pass.**

**Boundary.** Leg **`govkit selfcheck`** — argv `python tools/govkit/govkit.py selfcheck`, chunk
`declarations`, subject `repo`, **no guard**, so every bar.

**The cost rev-7 did not price.** A new `r.fail` is a deployer REFUSAL BRANCH, and
**`tools/govkit/refusal_join.py`** demands every one of them be reached by a named arm, anchored on
`(module, enclosing function, ordinal within that function)`, against a shrink-only `BRANCH_PIN = 217`
(`:41`) whose every movement must name both values and state how many of the new branches are armed
(`:42-110` is that ledger). So arm A owes an arm in `tools/govkit/selftest.py` and a pin bump to 218 with
its reason inline. The leg is **`govkit refusal join`** (chunk `declarations`, subject `repo`, guard
`tools/govkit/`), which this diff touches — so the branch's existence is graded on this unit's own bar
even though the arm's behaviour rides `govkit selftest`, which no boundary runs.

#### 4.5c (i) VALIDATE AT ADOPT TIME — arm B, the INSTALLED SET, in `cmd_apply`

**"Adopt time" means `cmd_apply` (`govkit.py:4243`), not `cmd_adopt` (`:7650`.)** govkit has a verb
literally named `adopt`, and it writes a receipt for a tree that was ALREADY installed (`:7670`: *"Write
the receipt an already-installed tree never had"*). The verb that installs is `apply`. Naming the wrong
one would have put the check where it can never fire.

**Placement: immediately after AC8** (`:4280-4288`), before `demand_writable_target` at `:4295` and
before anything is written.

**The installed set needs no new probe, because AC8 already narrowed it.** `foreign_kit_present`
(`:3891-3898`) answers "registry entries resolvable in the target that this target's receipt does not
claim", and `cmd_apply` at `:4282-4288` REFUSES when it returns anything (*"the target already carries …
and this target's receipt does not claim it"*). So by the time control reaches the new check, a kit that is
present-but-unclaimed has already killed the run. The satisfied set is therefore exactly:

```python
installed = set(selection) | set((receipt or {}).get("kits") or [])
```

with `selection` from `:4272` and `receipt` from `:4275-4276`. Five lines, one `Refusal`, no new primitive.

**It REFUSES rather than reports. Three reasons.** (1) `cmd_apply` is a refuse-before-writing verb by
construction and both its immediate neighbours refuse. (2) `passes-harnessed` is in `DIRECTIVES_CORE`
(`unattended.sh:469`) with scope `all` (`scope_of`, `:505-514`) against `DIRECTIVES_FLOOR="17"`
(`.unattended.conf:87`), so installing `unattended` without the route hands the adopter a rule that binds
every run and a route that does not exist — and the only relaxation is a per-run `--waive` by an owner who
is not there. (3) Install happens once; a report at install time is a line in a stream nobody re-reads.

**WHAT IT BREAKS, stated first because it is the entire cost.** Measured this pass: **all NINE existing
edges are unsatisfied under a single-kit `--kits <that kit>` selection into a virgin target.** One of the
nine is `--kits drift-audit`, which is the exact example `derive_install_order`'s docstring at `:495-496`
calls *"a legal install"*. That sentence is about the ORDERING function and stays literally true there —
`derive_install_order` still raises only on a cycle. But a policy stated in a docstring that a verb one
layer up now refuses is one fact in two places, so **`:495-496` gains a clause naming the apply-time check
in the same commit.** Not a footnote: it is the sentence a future reader will quote back.

**What it does NOT break, also measured:** over the DEFAULT selection (`registry.toml:36` — playbook,
kickoff-manifest, memory-tree, codebase-map, memory-recall, run-gates) and over `--all` (20 non-conditional
entries), **unsatisfied = 0**. The two selections gov's own runbook prescribes are untouched.

**`cmd_plan` gets the same predicate as a printed ROW, not a refusal.** `cmd_plan` (`:2615`, selection at
`:2622`) reads no receipt today and needs the two lines `cmd_apply` has at `:4275-4276`. This is the
smaller half and it is included for one reason: a preview that promises an apply which will then refuse is
the same defect class this document is about. Its exit code does not move.

**Failing case, staged and observed before it lands.** Four arms, all in a scratch clone against a scratch
target seeded with `.governance/deploy.toml`:

1. `apply --kits unattended` into a virgin target → refusal naming `unattended` and BOTH `memory-tree` and
   `review-harness`. Both, because both are genuinely absent, and an arm that expects one name would pass
   on a half-built check.
2. `apply --kits memory-tree,settings-merge,agent-cap,review-harness,unattended` → passes the new check.
3. the receipt carve-out: a target whose receipt claims `review-harness` and `memory-tree`,
   `apply --kits unattended` → passes.
4. `plan --kits unattended` prints the row and still exits 0. **The baseline for this arm is already
   observed: at the tip it exits 0 and prints nothing about the missing dependency.**

Each of arms 1 and the `plan` row is a refusal/finding branch, so `refusal_join.py`'s pin moves to 219 for
the pair (218 for arm A, 219 for arm B) and each names its arm.

**Boundary.** None standing for the behaviour: **`govkit selftest`** is chunk `selftests`, subject `kit`,
which no bar runs — not even `GATE_FULL=1`, which holds every `subject = kit` OR `chunk = selftests` leg;
it needs `GATE_SELFTESTS=1` or a hand run. **`govkit refusal join`** grades that the branch is armed, on
every bar whose diff touches `tools/govkit/`. That split is disclosed in §10.

#### 4.5d Why the adopter script is NOT the place

`grep -n 'workflows\|review-harness\|agent-cap'` over `tools/unattended/adopt-unattended.sh` and
`tools/unattended/check-unattended.sh` returns **zero lines** (run this pass, exit 1). The kit today
neither installs the dependency nor checks for it. Teaching `adopt-unattended.sh` to install it was
rejected: that script renders a Skill from a template (`:2-5`) and has no business fetching another kit,
and a kit that installs its own dependencies duplicates `govkit apply`'s job in a second language.

#### 4.5e (ii) ANNOUNCE AT GATE TIME — check 31 in `check-unattended.sh`, leg `unattended kit gate`

**Which checker.** `tools/unattended/check-unattended.sh`, the leg **`unattended kit gate`** (chunk
`declarations`, subject `repo`, no guard, so every bar). It is the only shipped gate whose subject is the
unattended contract, and it already reads `$M/guides/BUILD-METHOD.md` at arm B (`:1589`).

**Which check number: 31.** Derived by the file's own header recipe (`:4-7`): the `fail <n>` numbers in use
are 1–22 and 24–30, so the max is 30. **23 is NOT free** even though no `fail 23` exists — it is claimed as
a check LABEL by four report strings (`:1929`, `:1938`, `:1942`, `:1983`) and by three stdout violation
lines (`:1981`, `:2002`, `:2018`). So 31.

**What it grades: the route the M6 sentence names RESOLVES.** It slices `$M/guides/BUILD-METHOD.md` from
`^## M6( |$)` to the next `^## ` — the same slice §5's new arm-B body term already computes — scans it for
backticked paths ending `workflows/<name>.js`, and asserts each exists on disk. It knows the path because
the adopter's rendered M6 carries it with `{{TOOL_ROOT}}` already substituted; the check needs no knowledge
of any install prefix.

**Four outcomes, and the split IS the design decision:**

| state | verdict |
|---|---|
| the carrier `$M/guides/BUILD-METHOD.md` is absent | **announced skip**, inheriting arm B's silence rule verbatim (`:1586-1588`: *"SILENT when the carrier is absent — the leg grades the TREE and an adopter may install this kit without the memory-tree one"*) |
| the carrier exists and M6 names no `workflows/*.js` path | **announced skip.** This is the tree's own state until U2 lands, so **the check is born skipping and says so on its first run** |
| M6 names paths and **`tools/workflows/` is ABSENT** | **announced skip — the one the ruling asks for** |
| M6 names paths, `tools/workflows/` is PRESENT, a named script is not | **`fail 31`** |

**Why the last two split.** An absent DIRECTORY means the adopter never took `review-harness` — arm B of
(i) is what refuses that, at the moment of the act that creates it, and redding a standing bar over an
install decision the bar cannot undo punishes the wrong act on the wrong day. A missing FILE inside a
present directory means they took the kit and the route is broken, which is a defect in their tree and is
theirs to fix.

**The exact skip line**, in the kit's own shipped grammar (`report()` at `:591`, gated by
`REPORT=${GOV_UNATTENDED_REPORT:-0}` at `:590`, modelled on `:1929`):

```
unattended-report: check 31 skipped — the build method's M6 names {{path}}, and this tree carries no
tools/workflows/ at all, so the route `passes-harnessed` binds resolves to nothing here and a green
verdict would be coverage of a script that is absent
```

**How it differs in shape from a pass — three distinct prefixes, one of them empty:**

| outcome | what is printed | where |
|---|---|---|
| pass | **nothing.** The file's contract line is `:12-13`: *"Exit 0 + no output = clean"* | — |
| skip | `unattended-report: check 31 skipped — …` | REPORT channel |
| violation | `UNATTENDED check 31 FAILED — …` (`fail()` at `:93`) | stdout, and `status=1` |

**Per-check, never whole-leg.** The leg carries thirty numbered checks over run records, phases, conf keys,
the directive registry and the Skill, and not one of them needs `tools/workflows/`. A whole-leg skip would
discard twenty-nine verdicts to announce one, which is the green-by-absence class one level up.

**The honest cost, and it is the reason §10 keeps an entry.** `REPORT` defaults to 0, so **the default bar
prints nothing.** That is the kit's own ruled convention and not an oversight: `:15-21`
(`TOOL-dUnstalledConvoy-6`) says *"A skip that looks like a pass is indistinguishable from coverage, and a
skip printed by default would falsify the contract line above — so the line keeps its meaning and the
announcement gets a channel of its own."* The default channel exists and is used — check 7's EXCLUSION
notice prints there (`:23-29`) — but only because *"an exclusion is a positive finding that CHANGED THE
VERDICT."* Check 31's skip changes no verdict, so it does not qualify, and taking the loud channel anyway
would leave the header asserting something the code disproves.

**Failing case, three staged arms in a scratch clone with the M6 sentence landed:**

1. delete `tools/workflows/unattended-unit.js`, leave the directory → **`fail 31`** naming the missing path
   and the directive; restore.
2. `rm -rf tools/workflows/` → **exit 0**, default channel silent, and `GOV_UNATTENDED_REPORT=1` printing
   the skip line; restore.
3. the intact tree → neither line, exit 0.

The arm asserts all three outputs are byte-distinguishable, which is the property "a skip does not look
like a pass" actually means.

**A standing obligation the arms are not optional against.** `check-unattended.sh` defines `fail() {` at
`:93`, so it is in `check-arms.py`'s discovered population (`:9-12`: *"a tracked `*.sh` that DEFINES the
helper … its test is the sibling `<stem>.test.sh`"*). **`fail 31` therefore owes a positive arm in
`tools/unattended/check-unattended.test.sh` naming its own failure text, or a row in the shrink-only
`memory/project/unarmed-branches.txt`.** The leg is **`harness arms (fail branches armed or pinned)`**
(chunk `declarations`, subject `repo`, **no guard**), so it runs on every bar — and it grades that the arm
EXISTS even though the arm's own execution is off the bar under the 2026-08-23 self-test ruling.

#### 4.5f Why neither mechanism subsumes the other, and what is left

**The reason is temporal, not topical.**

- **(i) runs ONCE, at install, and only for installs made after it lands.** Nothing re-runs `apply` on its
  own, so (i) can never reach a target that already took `unattended` without `review-harness`.
- **(ii) runs on every bar of every adopter, forever, including exactly that population** — but it can only
  announce, for the reason §4.5e gives.

One closes the door. The other tells you the door was already open. Deleting either leaves a real
population uncovered, and the populations do not overlap.

**§10's adopter residual is NARROWED, not RETIRED.** What remains, named precisely:

1. an adopter who installed `unattended` before this lands, **never re-runs `govkit apply`**, and **never
   sets `GOV_UNATTENDED_REPORT=1`** — still bound by a core directive whose route does not exist in their
   tree, on a bar that is green and silent;
2. nothing makes the `--waive` escape discoverable to that adopter — check 31's skip names the absence, not
   the remedy, and widening it to prescribe a waiver would be a gate handing out a bypass;
3. the whole adopter population is outside this repo and unmeasurable from it, so **both mechanisms' green
   evidence is staged in scratch clones and neither has been observed against a real adopter.**

**(d) The kit-version consequence.** `tools/unattended/kit.toml` ships to adopters (`[[files]] include = "**"`,
role `engine`), so a `requires` change is a payload change and owes the `unattended` 1.17 → 1.18 bump —
which, per §4.4, makes this an owner turn too. The bump is a DISCIPLINE obligation and not a machine one:
`check-kit-versions.sh:17-19` grades marker PRESENCE and `:164-192` grades marker/constant AGREEMENT, and
no branch in that file reads a diff to ask whether a body change earned a bump.

### 4.6 The edit set

- **`tools/workflows/unattended-unit.js`** — NEW, from `scratchpad/unattended-unit.candidate.js` (110
  lines, 6933 bytes, three gates at exit 0 re-run this pass). No further header work is owed.
- **`tools/workflows/unattended-build.js`** — the disposal stage, the DELETION of the BUILD agent (`:485`
  and its schema and prompt, which also deletes the `:495-497` over-claim), the roster return of §3.2 with
  `resolvePathsWith`, the corrected `units` refusal text (`:118-124`), and the correction of the nesting
  comment at `:274-279`.
- **`tools/workflows/tier2-review.js`** — untouched except `version: '1.6' → '1.7'` (`:3`). That one line
  carries THREE tokens — `meta.version`, `gov:kit tier2-review@`, `gov:kit review-harness@` — and
  `check-kit-versions.sh:32-44` compares all three (loop at `:38-44`), so all three move together.
- **`tools/workflows/unattended-build.test.sh`** and **`tools/unattended/unattended.test.sh`** — the arms
  U5 needs. **Neither is a gate leg** and this design does not make one: the owner ruling of 2026-08-23
  keeps a kit's self-tests off the bar.
- **`tools/hooks/agent-cap.js`** — the `for await (` / `do…while` widening at the **SIX sites in THREE
  forms** (`:705`, `:711`, `:738`, `:910`, `:934`, `:944`, each opened this pass), plus the
  mutual-exclusivity note in the slot-ledger comment block. **Bump `KIT_AGENT_CAP_VERSION` 1.12 → 1.13**
  with its same-line `gov:kit` marker, which `check-kit-versions.sh:23` pairs. The `data.cwd` resolution of
  §2.4 precondition 3 is NOT taken here.
- **`tools/hooks/README.md`** — the mutual-exclusivity note in `## Direct spawns are COUNTED, not parsed`
  (`:119-126`), and the two still-open indirection shapes named beside `TOOL-dFoldedVerdict-8`. Write it
  without a digit-next-to-noun or the leg **`agent-cap restatement`** fires.
- **`tools/hooks/agent-cap.test.sh`** — arms in BOTH directions for the widening, which
  `memory/backlog/TOOL.md:10` demands by name. These arms spell no `tools/…` literal.
- **`tools/unattended/unattended.sh`** — `--plan --paths`. **The 1.17 → 1.18 bump is EIGHT carriers**:
  `KIT_UNATTENDED_VERSION` in `unattended.sh` (`:42`), `check-unattended.sh` (`:40`) and
  `check-pass-order.sh` (`:29`), compared at `check-kit-versions.sh:164-178`, plus a
  `gov:kit unattended@` marker in each of the **five** tracked `tools/unattended/*.template.md`
  (`:179-192`), each measured this pass at exactly one marker.
- **`tools/unattended/SKILL.template.md`** — the loop bullet with its four branches, the prompt-path read
  step, the version marker. **OWNER TURN (§4.4).**
- **`tools/unattended/PROTOCOL.template.md`** — §12's `:635-637` correction, the `:642` strike, the
  corrected state-refusal list, the field list, §9's three residual clauses, the version marker. The
  recipe sentence at `:637` is NOT touched.
- **`tools/unattended/kit.toml`** — the `requires` edge (§4.5).
- **`tools/unattended/check-unattended.sh`** — check 16 arm B's second term (§5) **and check 31 (§4.5e)**,
  plus the version constant.
- **`tools/unattended/check-unattended.test.sh`** — check 31's three arms, and `fail 31`'s positive arm,
  which **`harness arms (fail branches armed or pinned)`** requires on every bar.
- **`tools/unattended/README.md`** — the standing-cost section (§4.4).
- **`tools/govkit/govkit.py`** — check 7's plain-`requires` registry arm (`:1326-1341`), `cmd_apply`'s
  installed-set refusal after `:4288`, `cmd_plan`'s row, and the docstring clause at `:495-496`.
- **`tools/govkit/selftest.py`** and **`tools/govkit/refusal_join.py`** — the arms for both new refusal
  branches and the `BRANCH_PIN` 217 → 219 bump with its inline reason, on the file's own convention
  (`:41-110`).
- **`tools/memory-tree/BUILD-METHOD.template.md`** — the M6 sentence, the 17 backticked anchors, the
  budget raise in bytes, and the replacement of the *"No gate enforces the pair … whether one is ever
  added is a SEPARATE question nobody has ruled"* sentence at `:16-18`, which Ruling 2 makes false. **Bump
  `KIT_MEMORY_TREE_VERSION` 2.59 → 2.60.**
- **`tools/template-size-limits.txt`**, **`tools/check-template-size.sh`**,
  **`tools/check-template-size.test.sh`**, **`tools/gate-legs.json`**, **`tools/govkit/registry.toml`**,
  **`tools/govkit/subject-pins.tsv`** — the budget gate (§5B).
- **`tools/install-prefix-carried.txt`** — the ratchet is a **BAN** (`check-install-prefix.sh:315-319`),
  so every rise is hand-justified. **TWO moves:** `tools/unattended/SKILL.template.md` **1 → 2** (row at
  `:101`, read this pass) because its bullet names both script paths; `tools/workflows/unattended-build.js`
  **5 → 6** (row at `:124`) for the `dispatch.scriptPath` literal. `resolvePathsWith` adds no rise. The
  child needs no row (measured **0** `tools/` literals). Verified by leg **`install-prefix (shipped
  surface)`**.
- **`memory/map/features/unattended.md`** — `workflow-scripts` gains `unattended-unit.js` (today the claim
  at `:14` is `["unattended-build.js"]`, read this pass). **`memory/map/features/build-method.md`** —
  `gate-legs` at `:11` gains `build-method size`, and its Gaps bullet at `:74-78` claiming *"The line axis
  binds before the byte axis"* (`:77-78`) is corrected: `BUILD-METHOD.md:15` says the opposite (*"The BYTE
  half binds first"*) and the measurement agrees. Regenerate `memory/map/generated/MAP.md`,
  `inventories.json` and `symbols.json` in the same commit. Leg: **`codebase-map coverage + freshness`**.
- **Four kit versions move** — agent-cap 1.12→1.13, review-harness 1.6→1.7, memory-tree 2.59→2.60,
  unattended 1.17→1.18 — across **thirteen carriers** once the unattended eight are counted. Leg: **`kit
  version markers`**.
- **The record.** A `memory/DECISIONS.md` row superseding `:65` (`TOOL-cBriefedPilot-21 · parallelism
  route: none`, read this pass) with `dUnstalledConvoy`'s cleared verdict; `TOOL-cBriefedPilot-28` at
  `memory/backlog/TOOL.md:137` amended or closed; backlog rows for every §10 residual.
- **Not touched, verified at the tip:** `tools/check-playbook-parity.sh`, `.claude/settings.json`,
  `coding-governance-agents.template.md`, `AGENTS.md`, `skills/session-kickoff/SKILL.md`,
  `tools/unattended/adopt-unattended.sh` (§4.5d).

---

## §5 — THE RATCHET THAT STOPS THIS RECURRING

The most important structural section: rev-1 proved that check 16 arm B cannot fail, then fixed the
instance and left the gate byte-for-byte as it found it. Delete the new M6 sentence the next day and every
leg is green again.

### 5.1 The assertion

Arm B today, at `check-unattended.sh:1589-1594`, read this pass:

```sh
  if [ -f "$M/guides/BUILD-METHOD.md" ]; then          # :1589 — the carrier guard
    for pair in $core; do                              # :1590
      sec=${pair#*:}                                   # :1591
      grep -qE "^## $sec( |\$)" "$M/guides/BUILD-METHOD.md" \   # :1592 — the whole assertion
        || fail 16 "a directive points at a build-method section that does not exist, …"  # :1593
    done                                               # :1594
  fi
```

**Arm B gains a second term: the cited section's BODY must name the handle, in backticks, on a line that
is not an HTML comment.** For each `handle:section` pair, slice `memory/guides/BUILD-METHOD.md` from
`^## <section>( |$)` to the next `^## `, drop lines matching `^[[:space:]]*<!--`, and require
`` `<handle>` `` in what is left.

- **CORE ONLY.** `check-unattended.sh:1474-1487` builds `core` from `$DIRECTIVES_CORE $DIRECTIVES_EXTRA`
  (`:1475-1480`) while `corescope` is built from CORE alone (`:1481-1486`), for exactly this kind of
  reason. The body term takes a third CORE-only list, built in the loop that already exists.
- **BACKTICKS, not a word boundary.** Two holes close with one term: a bare `<!-- anchors: … -->` comment
  would satisfy a naive term while the section still states no rule, and `researched` is an ordinary
  English past participle that a future prose edit would satisfy by accident.
- **It hand-maintains no second table.** The required token is DERIVED from the handle the checker already
  parses for arms A and B — and it must be parsed the SAME way: `core`'s entries are `handle:section` with
  the scope segment already stripped (`:1475-1480`), which is why `sec=${pair#*:}` is correct for
  `researched:M12:prompt` only on that list. The header at `:1466-1469` records the four measured refusals
  that taught this.
- **It inherits arm B's silence** when the carrier is absent, for the reason `:1586-1588` gives.
- **The failing case, observable:** delete `` `passes-harnessed` `` from M6's body and the leg reds. Stage
  it, confirm RED, unstage. A second arm stages the anchor INSIDE an HTML comment and confirms RED.

### 5.2 What it does not check, in the leg's own header

It grades that the section NAMES the handle in a form a comment cannot fake, **not that the sentence
around the name states the rule**. Someone can still leave a dead anchor inside a real sentence. The gate
is strictly stronger than existence-only and strictly weaker than semantics, and its header says exactly
that.

### 5.3 The cost, re-derived at the tip

- **0 of 17 core handles appear in `memory/guides/BUILD-METHOD.md` today**, bare or backticked, checked one
  spelling at a time this pass. The term reds every handle on the day it lands.
- **17 handles over 10 distinct M-sections**, derived from `DIRECTIVES_CORE` (`unattended.sh:469`) this
  pass: M6 ×3 (`parallel-when-disjoint`, `passes-committed`, `passes-harnessed`), M8 ×3, M9 ×2, M10 ×2,
  M12 ×2, and one each for M2, M3, M4, M5, M7.
- **Byte floor: 289** — the 17 spellings (255 characters, summed this pass) plus two backticks each.
  Realistically 400–700 with joining words.
- **Cost across the byte-compared pairs: one render.**
- The leg is **`unattended kit gate`** (chunk `declarations`, subject `repo`, no guard), so it grades on
  every bar, and check 16's own self-test fixtures gain an arm.

---

## §5B — THE BUDGET, AND THE GATE THAT READS IT

**The decision (owner, 2026-09-04): raise the cap AND build the checker in this build.** The owner took
the option that ends the class rather than the cheapest one.

### 5B.1 R4 dissolves by construction

`BUILD-METHOD.template.md:8` reads `**Budget: ≤24 KB, ≤350 lines**`. On a KiB reading the template
(24564 bytes) has 12 bytes of headroom; on a decimal reading it is 564 over. **The question is not
answered — it is destroyed.** A checker needs an exact integer, so the cap is written in BYTES and the
unit disappears from the sentence. This is not a rhetorical move: the mechanism that will read the number
already stores it that way. `tools/check-template-size.sh` resolves a per-subject ceiling from
`tools/template-size-limits.txt` (`:70-78`), whose grammar its own header states as
`<repo-relative-path>\t<bytes>`, resolves the precedence at `:91` (positional → declaration → environment →
a 49152 default), and compares against LF-normalized bytes measured at `:99-101`.

### 5B.2 The number, and its arithmetic

**The cap becomes 27648 bytes.** The arithmetic, every term measured in this pass:

| term | bytes |
|---|---|
| `memory/guides/BUILD-METHOD.md` today | 24553 |
| + the M6 route sentence of §4.1 | +764 (measured; ~22 less after `{{TOOL_ROOT}}` substitution) |
| + the 17 backticked anchors | +289 floor, 400–700 realistic |
| + the rewritten budget line with its dated reason | ~+300 |
| **projected after this build** | **≈26,100** |
| **cap** | **27648** |
| **headroom left** | **≈1,550** |

The LINE half does not move: 317 lines today, +8 for the M6 sentence and +2 or 3 for the budget line, so
~328 against the existing `≤350`. **The raise is byte-only, and the line cap is left exactly where the
2026-08-25 raise put it.**

The prose at `:8-18` already records three prior raises inline with their dates and reasons — ≤20 KB/≤250
lines at M12's landing, ≤24 KB/≤310 on 2026-08-21 (`:10`), the line half to ≤350 on 2026-08-25 (`:10-11`),
with the reasons at `:12-14`. **The fourth entry joins them, dated 2026-09-04, and says what bought it: the
M6 route sentence `passes-harnessed` has pointed at since it was minted, plus the 17 anchors §5's new gate
term requires.**

**And one live sentence becomes false.** `BUILD-METHOD.md:16-18` says today: *"No gate enforces the pair,
which is why exceeding it silently was the one option not taken, and whether one is ever added is a
SEPARATE question nobody has ruled."* **The owner has now ruled it.** That sentence is replaced by one
naming the gate and stating what it does not cover.

### 5B.3 The gate — an existing program, a new declaration

**Nothing new is written.** `tools/check-template-size.sh` already takes its subject as positional `$1`
(default at `:49`), resolves the ceiling declaration-first (`:70-78`, argued at `:80-90`), measures
CR-stripped bytes (`:99-101`), exits 1 over budget with a message naming the file, the measurement and the
overage (`:104-112`), and carries an advisory high-water ratchet (`:114`).

**THREE legs already ride it**, derived from `tools/gate-legs.json` this pass — rev-7 said two and its own
§8 said three:

| leg | subject |
|---|---|
| `template size <=48KiB` | no positional, so the default at `:49` — `coding-governance-agents.template.md` |
| `charter size` | `AGENTS.md` |
| `kickoff engine size <=18KiB` | `skills/session-kickoff/SKILL.md` |

`build-method size` is the fourth. (A fourth leg, `template size gate selftest`, rides the sibling
`check-template-size.test.sh`, chunk `selftests`, subject `kit` — a different script and no boundary runs
it.)

**The one code change is the PAIR TERM, and it is what makes this gate a CLASS gate.** With the cap in the
declaration and the number also in the document's prose, there are two spellings of one fact — the drift
class the charter names (*"A value stated in prose beside the source that OWNS it rots between changes —
point at the source, or gate the pair"*). So: when a subject has a DECLARED row and its own text carries a
`**Budget: ≤<n> bytes` line, the two must agree. About five lines, guarded on `[ -n "$declared" ]` so an
ungated subject is never compared against the script's hard default. **Exit code 6 and check number 6, both
free — derived this pass: the file's `fail` numbers are 1, 2, 3, 4, 5 (`:76`, `:98`, `:107`, `:137`, `:168`,
`:181`) and its `FAIL_CODE` values are 1–5.**

**The subject is the RENDER, `memory/guides/BUILD-METHOD.md`, and not the template.** The template sits a
few bytes above the render (24564 against 24553, because `{{TOOL_ROOT}}` substitutes shorter), and
**`kit/dogfood doc parity`** renders template→live and diffs, so every byte of template growth appears in
the render the gate measures. One leg, not two.

**The leg is named `build-method size`, with no number in it — a CONVENTION argument, not a machine one.**
`memory/map/baseline.toml:6-11` records why the name matters: when the owner raised the charter ceiling,
the leg key `template size <=32KiB` had to be RENAMED in place to `template size <=48KiB`, which is a
delete-plus-add through a file whose stated rule (`:3-4`) is that it only shrinks, *"taken deliberately"*
and recorded as the one exception. **But `:10-11` retracts the enforcement claim in its own words —
*"Nothing enforces the rule today — that is why the option was available at all."*** So the shrink-only
rule is a convention a reader honours, not a constraint a gate imposes, and rev-7 stated it as the latter.
A numberless name is still worth having: it cannot create the situation at all.

### 5B.4 The declaration act — five items, and the second is not what it looks like

1. **`tools/gate-legs.json`** — `{"name": "build-method size", "argv": ["bash", "tools/check-template-size.sh", "memory/guides/BUILD-METHOD.md"], "chunk": "product", "subject": "repo", "ceiling": 300}`. Chunk, subject and ceiling copy its three siblings exactly. **`subject` is not optional**: `govkit.py:1592-1596` reds on an `[[exempt_leg]]` whose manifest row declares none, and `:1597-1600` reds on one outside the closed set `kit|repo`.
2. **`tools/govkit/registry.toml` — an `[[exempt_leg]]` row, NOT a `[[gate_leg]]` in a kit.toml.** Derived
   this pass and it corrects the ruling's assumption. `tools/check-template-size.sh` is a registry
   EXEMPTION (`registry.toml:176-178`: *"gates gov's OWN product template … Prescribed for copy nowhere in
   the runbook"*), and **all three existing size legs are carried by `[[exempt_leg]]` rows** —
   `kickoff engine size <=18KiB` at `:277-279`, `charter size` at `:281-283`, and **`template size <=48KiB`
   at `:357`**, which rev-7 missed while reporting it as claimed by nobody. The kickoff row records the
   precedent in its own words: the kickoff-manifest descriptor once declared it as a `gate_leg`, *"so
   `apply` would have emitted an adopter a row running an engine gov never ships and recorded it in the
   receipt as coverage. DEPL-dCarriedReceipt-6 withdrew the leg and this row is where it went."*
   **Declaring `build-method size` in `tools/memory-tree/kit.toml` would repeat exactly that defect**,
   because the memory-tree kit ships `BUILD-METHOD.md` to adopters but ships no size gate. The reason
   string names that asymmetry.
3. **`tools/govkit/subject-pins.tsv`** — one row, `<name>\t<subject>\t<chunk>` (the shape of `:94`),
   generated by `python tools/govkit/govkit.py selfcheck --write`. The file's own header states why both
   fields are pinned.
4. **`memory/map/features/build-method.md:11`** — the leg NAME added to its `gate-legs` claim, which today
   reads `["method carriers (every pointer declared)", "method-carriers self-test"]`. The convention is
   that the SUBJECT's dossier claims a size leg: `memory/map/features/session-kickoff.md:11` claims
   `kickoff engine size <=18KiB`, and `memory/map/features/playbook.md:11` claims `charter size` and
   `template size gate selftest` — playbook being both the script's owner and the charter's subject. And
   the claim is mandatory in the OTHER registry too: `govkit.py:1602-1604` reds with *"gate leg '<name>' is
   claimed by no descriptor and carried by no [[exempt_leg]]"*, while the same block also reds on an
   exemption with no reason (`:1575`), a stale one (`:1578`), one that is ALSO claimed (`:1581`), and one
   whose manifest row declares no `subject` (`:1593`). **Two registries, and item 2 satisfies one while
   item 4 satisfies the other; rev-7 conflated them.**
5. **Regenerated map artifacts** in the same commit.

Plus, and outside that five: **the row in `tools/template-size-limits.txt`** carrying the number and its
justification, which is the cap itself.

### 5B.5 The failing case, observed before it lands

Two staged breaks, both in a scratch clone, both unstaged after:

1. **Over budget.** Append filler to `memory/guides/BUILD-METHOD.md` until it exceeds 27648 bytes; run
   `bash tools/check-template-size.sh memory/guides/BUILD-METHOD.md`; confirm **exit 1** with the message
   naming the file, the measured bytes and the overage (`:107-111`). Confirm the un-appended file exits
   **0** and prints its one line.
2. **Pair disagreement.** Change the `**Budget: ≤27648 bytes` figure in the document without changing the
   declaration row; confirm **exit 6** naming both numbers. Then change the declaration row without the
   prose and confirm the same. This arm exists because the pair term is the only NEW code, and a term
   nobody has seen move is an assertion about nothing.

Both arms are added to `tools/check-template-size.test.sh`, which already carries over-budget arms for the
generic branch.

### 5B.6 The population, decided honestly

**Derived this pass: exactly TWO tracked files carry a `**Budget:` line, and they are the two halves of one
byte-compared pair** — `memory/guides/BUILD-METHOD.md:8` and `tools/memory-tree/BUILD-METHOD.template.md:8`.
No other tracked `.md` outside `memory/builds/` and `memory/archive/` declares a budget in its own prose.
So **the class has one member today, and the instance and the class coincide.**

That does not make this an instance gate, and the distinction is the whole of Ruling 2(d):

- **The LEG is per-subject** — one `tools/gate-legs.json` row per measured file, exactly as the three
  existing size legs are. A second guide wanting a byte ceiling needs its own row. That is the instance
  half and it is honest about being one.
- **The PAIR TERM is per-class** — its predicate is the prose shape `**Budget: ≤<n> bytes`, not a path, so
  the day a second document declares a budget AND gets a declaration row, its two spellings are compared
  with no further edit.
- **What is NOT gated, and the leg's header says so:** the **LINE** half of the budget.
  `check-template-size.sh` measures bytes only (`:99-101`). `BUILD-METHOD.md:15` argues the byte half binds
  first at this file's prose density, which is why leaving the line axis ungated is a priced choice rather
  than an oversight — but it is ungated, and §10 carries it.

---

## §6 — THE WITNESS

### 6.1 The honest answer, first

An agent boundary leaves no artifact inside this repo's reach. `dRetiredFork` ran WITHOUT the harness and
wrote `brief` rows that are byte-identical to what a harnessed run writes. No leg can distinguish them, and
a `harness-used:agent` DoD item is rejected: it would reproduce `passes-harnessed`'s exact failure one
layer down.

### 6.2 What the leg grades

Rev-1's leg redded a CONFORMING run, because `--brief` STAGES its row (`park` at `unattended.sh:4225`,
`stage_or_fail` at `:4226`, both read this pass) inside the pass whose commit is the build commit.

**Re-anchored at the build commit itself, and named for what it grades: `brief-recorded`.** For every unit a
build README grades CLOSED after the cutoff, locate its build commit exactly as `check-pass-order.sh` does,
then at THAT commit assert:

1. the run-state blob carries at least one `brief · item <id>` row (grammar
   `<ISO-Z> brief · item <unit> · reason <hash12> <tracked-path>`, `unattended.sh:4217`); and
2. the **last** such row for that unit names a path tracked at that commit whose `git hash-object` equals
   the row's 12 hex chars.

**The quantifier: existential over rows, last-row-wins.** A re-brief is the normal case. A universal reading
would red every re-briefed unit; a bare existential would let any stale row satisfy the term.

**What is given up, said plainly: ordering.** Inside one commit, nothing proves the brief preceded the code.
The only way to recover it is to make `--brief` commit its own row, which breaks the one-commit-per-pass
discipline `stage_or_fail` exists to keep. **Rejected.**

### 6.3 The cutoff and the liveness line

A per-build cutoff cannot admit one conforming unit without its non-conforming siblings, so
`BRIEF_RECORDED_CUTOFF` in `.unattended.conf` (+ `.conf.example`) is dated at the landing — the convention
`PASS_ORDER_CUTOFF`, `SPEC_THIN_CUTOFF`, `UNITS_REGION_CUTOFF` and `DISPOSITION_CUTOFF` already establish.
Population on day one is zero.

**The liveness line prints FOUR counts and the exclusion set:**

```
brief-recorded: graded N closed unit(s) · X build(s) skipped by the <date> cutoff · Y with no pinned run BASE · Z unit(s) unbuilt-in-range
brief-recorded: the record surface excluded from build-commit selection was: <build folder> <GENERATED_INDEXES> <SHARED_RECORDS>
```

`graded` increments before the build-commit selection, so a unit graded by NOTHING still counts as graded.
And the exclusion set is composed from two conf keys the GRADED RUN can commit, so widening
`GENERATED_INDEXES` turns a real violation green with no trace but that one count.

### 6.4 Acceptance — four arms, and it does not land without all four

1. **Staged RED on term 1.** In a scratch repo, drop the brief row from a closed unit's build commit;
   confirm the leg reds naming the unit and the commit; unstage.
2. **GREEN on a real conforming UNIT, graded per unit and not per leg-exit.** With the cutoff temporarily
   back-dated, assert that a named unit is reported OK at its build commit and that its non-conforming
   siblings appear as violations. The leg's exit code in that run is 1 and that is the CORRECT result;
   asserting on it would have discarded the leg.
3. **NON-ZERO count of units that reached TERM 1**, printed — not of units entering the loop. Over the live
   tree the leg reports "graded 0 · cutoff <date>" plus the other three counts, never "clean".
4. **Staged RED on term 2.** Edit a closed unit's brief file inside its build commit without a re-brief;
   confirm RED naming both hashes; unstage.

Registration here IS the five-declaration act with a `[[gate_leg]]`, unlike §5B's: a row in
`tools/gate-legs.json`, a `[[gate_leg]]` in `tools/unattended/kit.toml` whose `subject` agrees (the file
already carries four such rows, at `:107-109`, `:117-119`, `:124-126`, `:131-133`, all `subject = "repo"`),
a `subject-pins.tsv` row, the leg NAME in `memory/map/features/unattended.md:11`'s `gate-legs` claim, and
regenerated map artifacts. The difference from §5B is that `brief-recorded` is a script the unattended kit
SHIPS, so an adopter emitted the row can run it.

Its `fail` branch also owes an arm under **`harness arms (fail branches armed or pinned)`**, the same
standing obligation §4.5e's check 31 carries.

### 6.5 If arm 2 cannot be made to pass

Drop the leg and say so. What is left is **`pass-order history`** grading spec-before-code for CLOSED units
and nothing else, plus `--dispatch`'s two state refusals at the moment of the act.

---

## §7 — UNIT BREAKDOWN

Ordered: the record is fixed before anything cites it; the free widening lands independently; the ratchet
lands WITH the route it grades; the shape follows; the deployer work is independent; the announcement needs
the route to exist; the witness last. **OWNER-GATED** marks a unit no unattended run may take to
completion, per §4.4 and M3 veto 2 (`BUILD-METHOD.md:84`).

| # | Unit | Tier | Owner-gated? | Acceptance | Which boundary runs the gates it names |
|---|---|---|---|---|---|
| **U1** | **The record.** A `DECISIONS.md` row superseding `:65`; amend or close `TOOL-cBriefedPilot-28` at `memory/backlog/TOOL.md:137`; correct live files quoting `parallelism route: none` as standing; file every §10 residual as a backlog row. | 1 | no | `grep -c dUnstalledConvoy memory/DECISIONS.md` > 0; `git grep -n "parallelism route: none"` outside `memory/{builds,archive}` returns only citations naming the supersession. | **`memory hygiene`** (chunk `records`, subject `repo`, no guard) — every bar. |
| **U2** | **The route + the ratchet, together.** The M6 sentence with its backticked `passes-harnessed` anchor, its `parallel-when-disjoint` clause and the two backticked `workflows/*.js` paths check 31 later reads; the other 16 anchors; arm B's body term, CORE-only and backtick-keyed and comment-excluding; PROTOCOL §12's `:635-637` correction and the `:642` strike; the corrected state-refusal list; §9's THREE residual clauses; the Skill loop bullet with its `scriptPath` pin, its re-read step and its FOUR `next:` branches; the prompt-path read step; four kit version bumps across thirteen carriers; both manifest stamps. | 2 | **YES** — edits `BUILD-METHOD`, `PROTOCOL` and `SKILL` templates, three veto-2 carriers. | `grep -c unattended-build memory/guides/BUILD-METHOD.md` ≥ 1; the body term OBSERVED RED with the M6 anchor removed AND with it present only inside an HTML comment, green with the real anchor; `grep -c "pass-order leg over the commit graph"` = 0 in BOTH halves of the protocol pair; the rendered Skill names all four `next:` shapes, asserted by grepping each of the three terminal spellings plus `(READY - build it)`; template bytes and lines printed and inside the ratified budget; `bash tools/memory-tree/kit-dogfood-parity.test.sh` exit 0; `bash tools/unattended/adopt-unattended.sh --check` exit 0; `bash tools/check-install-prefix.sh` exit 0 with the SKILL row hand-justified; `bash tools/check-kit-versions.sh` exit 0; `bash skills/session-kickoff/manifest-check.sh` exit 0 **including C9**. **ONE OBSERVED DISPATCH** — a run holding the rendered Skill makes one `scriptPath` Workflow call and the call is TAKEN. | **`kit/dogfood doc parity`** (guarded on `memory/guides/BUILD-METHOD.md` + `tools/memory-tree/`, which this diff touches), **`unattended kit gate`**, **`unattended skill wiring`**, **`kit version markers`**, **`install-prefix (shipped surface)`** — all four unguarded ones on every bar. C9 only at the FULL bar (`manifest-check.sh:373-375` excludes it from the staged leg). |
| **U3′** | **Everything under `tools/hooks/`.** The `for await (` / `do…while` widening at the SIX sites in THREE forms, its arms in both directions, plus the mutual-exclusivity note in the slot-ledger block and in `README.md`. **Independent of the hoist.** | 1 | **YES** — `agent-cap.js` and its README are governance carriers. Landing it as its own unit against `TOOL-dFoldedVerdict-8` drops it out of this build. | Both spellings OBSERVED exit 0 before and exit 2 after, with the byte-identical plain `for` control still exit 2. **All six sites edited, asserted by count and not by eye.** The widened predicate run over the whole tracked tree first, printing hits AND near-misses. Today's tracked workflow scripts still exit 0. | The DENY arms live on **`agent-cap self-test`** (chunk `selftests`, subject `kit`), which **no boundary runs** — on demand only, by the owner ruling of 2026-08-23. The standing reader is **`verifier fan-out`** (chunk `declarations`, subject `repo`, no guard) and it catches over-denial ONLY. |
| **U4** | **The child**, `tools/workflows/unattended-unit.js`, from the candidate as edited in rev-6's pass. | 2 | **YES** — a NEW PUBLIC SURFACE, veto 2's third clause (`BUILD-METHOD.md:84`). | `node tools/workflows/check-workflow-syntax.js` exit 0; `bash tools/workflows/check-verifier-fanout.sh` exit 0 **and its derived file list CONTAINS the child's path** (membership, not exit code); the child holds exactly one `agent(` and **zero `workflow(`**; the `export const meta` DECLARATION present at its own line — asserted here and by nothing standing; **no `function`, no `=>`, no non-receiver array method** — asserted here and by nothing standing; **the PROMPT string names the CLOSED/WONTDO status flip AND the same-commit requirement**; `grep -c "THAT DISPATCH IS THE ORDER GATE"` = 0; args carry no roster field; `grep -c "tools/"` = 0; `scriptPath` mode admits, and the `script`-mode admit is recorded as a compatibility measurement. | **`workflow script syntax`** (chunk `wiring`, subject `repo`, no guard) and **`verifier fan-out`** — both on every bar. |
| **U5** | **The parent and the driver.** The disposal stage, the DELETION of the BUILD agent at `:485` (which also deletes the `:495-497` over-claim), the roster return of §3.2 with `resolvePathsWith`, the corrected `:274-279` comment and `:118-124` refusal, `--plan --paths`, the two ratchet rows, the map claim, and the order-gate arm. | 2 | **YES**, transitively — `--plan --paths` moves `unattended.sh`, which owes the 1.17 → 1.18 bump, which edits `SKILL.template.md`'s marker (`check-kit-versions.sh:179-192`). | An arm asserts the harness makes **zero** `agent()` calls after disposal and that `renderRoster` is absent downstream of the audit; an arm asserts the return carries `roster` as an ordered array of `{id, order, specPath, briefPath}`, `dispatch.scriptPath` equal to the child's path, and `resolvePathsWith` naming `--plan <slug> --paths`; an arm asserts a failed disposal returns `roster: []` with a DEGRADED note; an arm asserts a non-terminal verdict returns no roster; an arm asserts `--plan <slug> --paths` emits a spec path for every unit the padded table lists AND in region order; **an arm asserts the FOURTH `next:` shape**; **an arm in `unattended.test.sh` OBSERVES the order-gate blocker message, which has zero arms today**. `bash tools/check-install-prefix.sh` exit 0. | **`install-prefix (shipped surface)`**, **`codebase-map coverage + freshness`**, **`kit version markers`** — every bar. **The two test files are NOT gate legs and this design does not make them one**, so the suite arms have NO boundary and are run by hand. |
| **U6** | **The `brief-recorded` leg**, its cutoff, its four-count liveness line, its five declarations, and its `fail`-branch arm. | 2 | **YES**, transitively — it moves `.unattended.conf` and `check-unattended.sh`, owing the same bump. | §6.4's four arms, all of them, plus a positive arm naming its own failure text. | The leg itself: chunk `declarations`, subject `repo`, guarded on the kit dir with its reason. **`harness arms (fail branches armed or pinned)`** (no guard) on every bar. |
| **U7** | **The budget and its gate (Ruling 2).** Raise `BUILD-METHOD`'s byte cap to **27648** with the dated reason beside the three prior raises; replace the now-false "no gate enforces the pair" sentence at `:16-18`; add the row to `tools/template-size-limits.txt`; add the PAIR TERM to `tools/check-template-size.sh` (check 6 / exit 6, both derived free this pass) and its two arms to the self-test; register the leg **`build-method size`** by §5B.4's five declarations. | 2 | **YES** — `BUILD-METHOD` is a veto-2 carrier and its own budget prose already makes raises owner calls. | **The staged breaks of §5B.5, both observed before the leg lands**: over-budget → exit 1 naming file, bytes and overage; pair disagreement → exit 6 naming both numbers; the untouched file → exit 0. `bash tools/check-template-size.sh memory/guides/BUILD-METHOD.md` exit 0 after the raise, with the measured bytes printed in the landing report. `python tools/govkit/govkit.py selfcheck` exit 0 — which is what proves the `[[exempt_leg]]` row AND the dossier claim are both present, since `:1602-1604` reds without one and the map's coverage leg reds without the other. `bash tools/memory-tree/kit-dogfood-parity.test.sh` exit 0. | **`build-method size`** itself (chunk `product`, subject `repo`, no guard) — every bar, the same boundary as its three siblings. Its self-test arms ride **`template size gate selftest`** (chunk `selftests`, subject `kit`), which **no boundary runs**. **`codebase-map coverage + freshness`**, **`govkit selfcheck`** and **`kit version markers`** on every bar. |
| **U8** | **The recipe probe (Ruling 3).** In a scratch clone at the tip, construct the smallest honest recipe-mode build and run `--plan` on it, then feed the harness the unit set that produces. Record the answer and the decision it feeds; change no shipped byte on the strength of a guess. | 1 | no — it lands a record, not a carrier. | §9 D3 states the question, the construction and the two decisions it feeds. **The unit is DONE when the record exists, whichever way the answer falls**, and it does not itself take option (a) or (b). | **None runs the probe** — it is a measurement in a scratch clone, and saying so is the point. Only the record it lands is on **`memory hygiene`**. |
| **U9** | **The dependency edge AND its install-time validation (Ruling 4, mechanism i).** `tools/unattended/kit.toml:7` → `requires = ["memory-tree", "review-harness"]`; check 7's plain-`requires` registry arm (`govkit.py:1326-1341`); `cmd_apply`'s installed-set refusal after `:4288`; `cmd_plan`'s preview row; the `derive_install_order` docstring clause at `:495-496`; two `selftest.py` arms; `refusal_join.py`'s `BRANCH_PIN` 217 → 219 with its inline reason; the `unattended` version bump the descriptor change owes. | 2 | **YES**, transitively — a `kit.toml` change owes the bump, which edits `SKILL.template.md`'s marker. | `python tools/govkit/govkit.py selfcheck` exit 0 on the untouched tree (**already observed this pass**) and **non-zero with a staged `requires = [… "reviewharness"]`**, naming entry and id; the FOUR apply arms of §4.5c, each OBSERVED, including the receipt carve-out and the `plan` row; a `plan` for a selection naming both kits shows `review-harness` ordered BEFORE `unattended`; `python tools/govkit/refusal_join.py` exit 0 with the pin at 219 and both anchors named; `bash tools/check-kit-versions.sh` exit 0. | **`govkit selfcheck`** (chunk `declarations`, subject `repo`, no guard) and **`govkit refusal join`** (guard `tools/govkit/`, which this diff touches) — both on this unit's bar. **`govkit selftest`** (chunk `selftests`, subject `kit`) runs the apply arms and **no boundary runs it**, not even `GATE_FULL=1`. **`kit version markers`** every bar. |
| **U10** | **The gate-time announcement (Ruling 4, mechanism ii).** Check 31 in `check-unattended.sh`: the M6 slice, the `workflows/*.js` scan, the four-outcome split, the `report()` skip line and the `fail 31` branch; its three arms plus the positive arm `fail 31` owes; the `unattended` version bump. **Lands AFTER U2**, because it reads the sentence U2 writes. | 2 | **YES**, transitively — it moves `check-unattended.sh`, owing the same bump. | The three staged arms of §4.5e, all observed: `fail 31` on a missing FILE in a present directory; exit 0 + a REPORT-channel skip and a silent default channel on an absent DIRECTORY; neither line on an intact tree. **All three outputs asserted byte-distinguishable.** `python tools/memory-tree/check-arms.py --check` exit 0 with `fail 31` armed rather than pinned. | **`unattended kit gate`** (chunk `declarations`, subject `repo`, no guard) — every bar, and it is the leg being changed. **`harness arms (fail branches armed or pinned)`** (no guard) — every bar; it grades that the arm EXISTS even though the arm's own execution rides `tools/unattended/check-unattended.test.sh`, which is not a gate leg. **`kit version markers`** every bar. |

**What died: rev-3's U3**, the `gov:sequential-units` clause set. Not degraded, deferred or folded — the
hoist removes the problem it solved.

**Owner-gated: U2, U3′, U4, U5, U6, U7, U9, U10 — eight of ten.** Only U1 and U8 are not, and both land
records rather than carriers. **That is the price of Ruling 1 stated as a number**, and five of those eight
(U5, U6, U7 via memory-tree, U9, U10) are gated by the version-marker coupling rather than by a prose edit
anyone intended.

---

## §8 — MEASUREMENT INDEX

Everything re-derived in THIS pass at `origin/main` = **`c4fcf5ad`**, from a blob or from a
`git archive origin/main` snapshot, with the command beside it. Where a figure is CARRIED it says so.

| what | how | result |
|---|---|---|
| tip | `git fetch`; `git rev-parse origin/main` | **`c4fcf5ad`** — the same tip rev-7 used |
| this worktree against the tip | `git rev-list --left-right --count origin/main...HEAD` | **130 behind, 0 ahead** |
| gate-leg rows | parsed `tools/gate-legs.json` | **93**, and `govkit selfcheck` prints *"93 in the manifest · 69 claimed · 24 exempt"* |
| **what the hook's re-read feeds** | `agent-cap.js:1521`, `:1541`, `:1562`, `:1593`, each opened | **THREE burst rules and ONE JOIN rule.** `:1559-1560` says so in the file's own words; `:1592` labels rule 5 the cheapest to recover from |
| `guardAgentSpawn` reachability | `agent-cap.js:1494-1499` | reached ONLY on `data.tool_name === 'Agent'` |
| `MAX_VERIFIERS` | `agent-cap.js:403` | **5** |
| the `name:` route | fixture fed to the hook, exit captured without a pipe | **exit 0**, nothing read (`:1519`) |
| unreadable `scriptPath` | an MSYS `/c/Users/…` path | **exit 2**, `ENOENT`, fail-closed (`:1510-1517`) |
| the child, `scriptPath` mode | Windows-form path | **exit 0** |
| loop-around-spawn DENY | `for (const u of cfg.units) { await agent(…) }` appended | **exit 2**, the `:1521` message |
| the other six fixtures | rev-6 | **CARRIED, not re-run** |
| sidechain hook coverage | `agent-cap.js:9`, `:23-24` | *"workflow sidechains don't run hooks"*; *"Agents spawned INSIDE a workflow sidechain remain uncounted"* |
| does the hook see `workflow(` | `grep -c "workflow(" tools/hooks/agent-cap.js` | **0** |
| loop-predicate sites | opened each line | **SIX in THREE forms**: `\b(for\|while)\s*\(` at `:705`, `:738`, `:934`, `:944` · `\b(for\|while)\s*$` at `:910` · `\b(?:for\|while)\s*\(/g` at `:711` |
| `--dispatch` state refusals | `unattended.sh:4604`, `:4609` | MISSING and THIN; the THIN `case` has one arm |
| order-gate opt-in | `:4630`, `:4639` | conditional on BOTH units carrying an `order` verb |
| order-gate escape | `:4647`; written at `:4813` | **a declaration row alone satisfies "dispatched"** |
| order-verb corpus | every tracked `memory/builds/*/spec/*.md` with a `**Status:**` header, against `ORDER_OK_RE` (`:354`) | **163 of 478** (34.1%) · **61 of 85** builds carry none · **38 of 61** multi-unit builds have zero enforcement |
| order-gate arms in the kit suite | `grep -c "out of the build's own declared order" tools/unattended/unattended.test.sh` | **0** |
| **what `pass-order history` grades** | `check-pass-order.sh:9-10`, `:21`, `:22`, `:23-24` | **spec-before-code ORDER for CLOSED units.** `:21` *"this measures ORDER and nothing else"*; NOT dispatch (`:22`); nothing about a non-CLOSED unit (`:23-24`) |
| where §12 still claims otherwise | `UNATTENDED-PROTOCOL.md:642` and its template twin | *"and the pass-order leg over the commit graph"* — struck by U2 |
| the recipe contradiction | `UNATTENDED-PROTOCOL.md:637` against `unattended.sh:469` + `scope_of` `:505-514` | *"Recipe mode does not take it"* against a directive with no scope segment, which resolves to `all` |
| **waiver-scope grammar** | `check_waiver_scope` `:1163-1179`, **comparison at `:1172`**, `fail 45` at `:1173` | `[ "$sc" != all ] && [ "$sc" != "${AUTH_MODE:-}" ]` — one mode or `all`, so no mode LIST is expressible |
| auth modes | `unattended.sh:478` | `slug prompt recipe` |
| the completeness catcher | `unattended.sh:3353`, `DOD_CORE` `:344` | **one**, at `--close`; `DOD_CORE` has **12** items; exit `--override build-complete` |
| the termination oracle | `unattended.sh:2144` | `case "$st" in CLOSED\|WONTDO)` on the spec's status HEADER |
| `--plan` reads the INDEX | `unattended.sh:2043` | `git ls-files "$dir/spec/*.md"` — an unstaged spec is invisible |
| `next:` shapes | `:2148`, `:2149`, `:2158`, `:2173`, `:2175`, `return 0` at `:2177` | **FOUR**, one of them a refusal at exit 0 |
| `next:` over the WHOLE corpus | `--plan <slug>` for every build folder, RE-RUN in the snapshot | **92** folders, **90** produced a line: **69** terminal · **10** READY · **6** FORKED · **5** no-grade · **0** THIN · **0** MISSING. Two refused earlier at exit 1 |
| build rosters | generated `gen:build-units` regions over all 92 READMEs | **85** non-empty · median **4** · mean **5.62** · max **30** · **35 of 85** over five |
| tracked run records | `phase:` in all tracked `RUN.md` | **37** — LANDED 24, ABORTED 7, LANDING 4, BUILDING 2. **CARRIED from rev-7 at this same sha** |
| core directives | `DIRECTIVES_CORE` `:469` against `DIRECTIVES_FLOOR="17"` (`.unattended.conf:87`) | **17** over **10** M-sections; `passes-harnessed:M6` last and unscoped, `parallel-when-disjoint:M6` unscoped |
| handles present in the render | each of the 17 spellings grepped against the render | **0 of 17**, bare and backticked |
| anchor byte floor | 17 spellings (255 chars) + 34 backticks | **289** |
| the M6 route sentence | written to a file and measured | **764 bytes / 8 lines** |
| BUILD-METHOD sizes | `wc -c -l` | template **24564/317**, render **24553/317** |
| the budget prose | `BUILD-METHOD.md:8-18` | `≤24 KB, ≤350 lines` at `:8`; three prior raises at `:10-14`; **`:15` says the BYTE half binds first**; `:16-18` says no gate enforces the pair and nobody has ruled |
| budget-declaring population | `git grep -nE '^\*\*Budget'` over tracked `*.md`, excluding builds/archive | **2 files — one document's two halves** |
| **legs riding `check-template-size.sh`** | parsed `tools/gate-legs.json` | **THREE**: `template size <=48KiB` (default subject, `:49`) · `charter size` · `kickoff engine size <=18KiB`. A fourth leg rides the sibling `.test.sh` |
| the size gate's shape | `check-template-size.sh:49`, `:70-78`, `:80-90`, `:91`, `:99-101`, `:104-112` | subject as `$1`; declaration outranks environment; ceiling in bytes; CR-stripped measurement; **`fail` numbers 1–5 and `FAIL_CODE` 1–5 used, 6 free on both axes** |
| **how those legs are declared** | `registry.toml:176-178`, `:277-279`, `:281-283`, **`:357`**; `govkit.py:1568-1606` | the script is a registry EXEMPTION; **all three legs are `[[exempt_leg]]` rows**; `:1602-1604` reds on a leg claimed by neither; `:1592-1600` demands each exempt leg's manifest row declare a `subject` in `kit\|repo` |
| who claims a size leg in the MAP | `git grep` over `memory/map/features/*.md` and `generated/MAP.md` | `session-kickoff.md:11` claims the kickoff one; `playbook.md:11` claims `charter size` and the selftest; **`template size <=48KiB` is unclaimed and sits in `baseline.toml:34`** — a different registry from the govkit exemption |
| **the map baseline's own rule** | `memory/map/baseline.toml:3-4`, `:6-9`, **`:10-11`** | shrink-only with one recorded exception — and *"Nothing enforces the rule today"* |
| **`requires` is read where** | `govkit.py:486-518`; `resolve_selection` **`:521-590`** | ONE place, filtered `if d in want` (`:504-505`); **FOUR call sites `:558`, `:567`, `:582`, `:590`, none of which expands the selection**; only a cycle refuses (`:510-515`) |
| **the edge, OBSERVED** | `govkit plan --target <virgin> --kits unattended` in the snapshot | **exit 0**, `selection: unattended` — the existing `memory-tree` edge pulled nothing and complained about nothing |
| a target with no descriptor | the same command before seeding `.governance/deploy.toml` | **exit 2**, *"Refusing to guess"* — so every acceptance arm must seed or `intake` first |
| is `requires` validated | `govkit.py` grep | **no** — only `requires_if` is checked against the registry (`:1330-1333`, inside check 7 at `:1326-1341`) |
| **the candidate registry predicate, RUN over every kit.toml** | all 25 `[[entry]]` descriptors resolved through `registry.toml` | **9 plain-`requires` edges · 0 HITS · 9 near-misses enumerated in §4.5b** |
| **the candidate installed-set predicate, RUN** | over the DEFAULT selection (`registry.toml:36`), over `--all`, and over every single-kit selection | **DEFAULT: 0 unsatisfied · `--all` (20 entries): 0 unsatisfied · single-kit: ALL NINE unsatisfied**, `--kits drift-audit` among them |
| the declared chain | `tools/unattended/kit.toml:7`, `tools/workflows/kit.toml:7`, `tools/hooks/kit.toml:7` | `memory-tree` → (new) `review-harness` → `agent-cap` → `settings-merge` |
| `cmd_apply`'s existing refusals | `govkit.py:4272`, `:4275-4276`, `:4282-4288`, `:4295` | selection, receipt, **AC8 refuses a present-but-unclaimed kit**, then the write preconditions |
| the deployer's arm requirement | `refusal_join.py:2-25`, `BRANCH_PIN = 217` at `:41`, the ledger at `:42-110` | every refusal branch reached by a named arm, anchored `(module, function, ordinal)`; a pin rise names both values and how many are armed |
| does the adopter script install or assert it | `grep -n 'workflows\|review-harness\|agent-cap'` over `adopt-unattended.sh` and `check-unattended.sh` | **zero lines, exit 1** — neither |
| **check-unattended's channels** | `:12-13`, `:15-21`, `:23-29`, `fail()` `:93`, `REPORT=` `:590`, `report()` `:591` | pass = no output · skip = `unattended-report: …`, off by default · violation = `UNATTENDED check <n> FAILED — …` |
| **an existing skip line's grammar** | `check-unattended.sh:1929` (and `:1815`, `:1938`, `:1942`) | `report "check <n> skipped for <subject> — <why>"` |
| **free check number in that file** | `grep -oE 'fail [0-9]+' … \| sort -un`, plus the report-string labels | **1–22 and 24–30 used; 23 claimed as a label with no `fail`; 31 is next** |
| **check-arms' population** | `check-arms.py:9-12` | tracked `*.sh` DEFINING `fail() {`, tested by the sibling `<stem>.test.sh` — so `check-unattended.sh` is in it and `govkit.py` is not |
| the Skill render | `adopt-unattended.sh:9`; `tools/gate-legs.json` | *"renders to a temp file and DIFFS, so a hand-edited Skill reds"*; leg **`unattended skill wiring`**, chunk `wiring`, subject `repo`, no guard |
| SKILL sizes and anchors | `wc -c -l`; `grep -n '^## '` | template **52471/791**, render **52443/791**; `## While it runs` **:465**, `## While the work runs` **:573**, `--dispatch` bullet **:543**, bug-class bullet **:557** |
| SKILL frontmatter | `:1-4`, marker `:5` | `name` and `description` only — **no allowed-tools key** |
| Workflow mentions in the Skill | `grep -cEi "workflow\|unattended-build"` | **0** |
| **the Skill's playbook sentences** | `SKILL.template.md:363-364` **and the near-duplicate at `:489-491`** | both about a PLAYBOOK, not the Skill — §4.4 uses them as an analogy and says so |
| what a recipe build declares | `SKILL.template.md:298-366`, keys at `:332-338` | `authorized-by: recipe`, `playbook: <path resolved at BASE>`, `pieces: <n>`, plus the six required keys (`:261`) and the region marker pair |
| does the recipe path author specs | the same section | **no** — its whole vocabulary is `--record-piece` / `--record-set` (`:354-355`) |
| unattended version carriers | `check-kit-versions.sh:164-192`; measured over the tree | **8** — 3 engine constants (`unattended.sh:42`, `check-unattended.sh:40`, `check-pass-order.sh:29`) + **5** template markers, each at exactly one marker, all 1.17 |
| what kit-versions grades | `check-kit-versions.sh:17-19`, `:32-44`, `:164-192` | PRESENCE and marker/constant AGREEMENT. **No branch reads a diff**, so it never asks whether a body change earned a bump |
| kit versions | the four `version_from` sources | agent-cap **1.12**, review-harness **1.6**, memory-tree **2.59**, unattended **1.17** |
| UNATTENDED-PROTOCOL size | `wc -c -l` against `INDEX_CAP_BYTES` (`.memory-tree.conf:148`) | **54772/649** against **61440** — 6668 free; both halves identical |
| the residual list's home | `UNATTENDED-PROTOCOL.md:515-521` | *"What it does not close, stated so no reader has to discover it"* |
| the `name:` hole's declared home | `memory/guides/REVIEW-PROTOCOL.md:93-96` | under *"Where enforcement does NOT reach"* |
| **veto 2, and its reach** | `BUILD-METHOD.md:83`, **`:84`**, `:76`, `:87` | veto 1 at `:83`; **veto 2 at `:84`**; the delegation *"does not reach veto 2's governance-carrier clause"* at `:76`; *"Vetoes 2 and 3 are owner turns"* at `:87` |
| new build folders are contract-bound | `memory/project/readme-contract.txt:1-27`, forward/reverse at `:3-6`, pin at `:11-14` | `gen_build_index.py --check-format` refuses a tracked build README named by no row, in BOTH directions, against an `exempt-pin` EQUALITY |
| the harness's empty-`units` throw | `unattended-build.js:118-124`, message `:120-122` | throws, and its message names `--plan` as the source |
| the parent's agent/workflow sites | `grep -n "await agent(\|await workflow("` | `:230` SPEC · `:294` blob resolver · `:327` `workflow(` · `:388` round record · **`:485` BUILD, deleted by U5**; file is **531** lines |
| the parent's own over-claim | `unattended-build.js:495-497` | *"THAT DISPATCH IS THE ORDER GATE: it refuses a unit that is MISSING, THIN or out of the declared order"* |
| the bug-class command | `grep -n gotchas.py` over the parent | **`:499`**, the only occurrence |
| the edited candidate child | `wc -l -c`; three gates; property greps | **110 lines / 6933 bytes**; syntax **0**, verifier-fanout **0**, agent-cap `scriptPath` **0**; `tools/` **0**, `agent(` **1**, `workflow(` **0**, the `meta` DECLARATION at `:30`, order-gate over-claim **0**, `CLOSED` **1** |
| `meta` as a selector | `check-verifier-fanout.sh:86`; `check-workflow-syntax.js:30` + `:72` | both SELECT by the marker; absence DEPOPULATES |
| what denies writing the judge | `.claude/settings.json`, 45 lines | PreToolUse `Workflow\|Agent` `:5` and `Bash\|PowerShell` `:14`; `Read` `:35` is PostToolUse; **no `permissions` block at all** |
| install-prefix rows that move | `tools/install-prefix-carried.txt:101`, `:124` | SKILL.template.md **1**, unattended-build.js **5** |
| the install-prefix lead class | `check-install-prefix.sh:60-62`, regex `:63` | `{` and `}` excluded so `{{TOOL_ROOT}}…` is not a hit |
| the ratchet's nature | `check-install-prefix.sh:315-319` | a **BAN**, not shrink-only |
| C9's threshold and exclusion | `manifest-check.sh:400`, header `:373-375` | `[ "$c9n" -ge 10 ]`; never in the staged leg |
| the drift ratchet registry | `drift_signals.py:279-290` | `{"file", "key", "weakens"}` over `KEY = value` scalars only; `tools/template-size-limits.txt` is TSV, so **no row is owed and none would fit** |
| brief-row grammar and staging | `unattended.sh:4199-4200`, `:4203`, `:4217`, `:4225-4226` | refuses an untracked path; hashes with `git hash-object`; row parked then STAGED |
| halt vocabulary | `HALT_CODES_CORE` `:468` against `HALT_FLOOR="7"` (`.unattended.conf:160`) | **7 members** |
| kickoff interactive exits | `.unattended.conf:57` | `KICKOFF_EXITS="6"` — unchanged, untouched |
| keepalive cadence | `.unattended.conf:50` | `every 10 minutes (cron 3-59/10 * * * *)` |
| the map's own contradiction | `memory/map/features/build-method.md:74-78`, clause at `:77-78` | *"The line axis binds before the byte axis"* against `BUILD-METHOD.md:15` |
| `tools/unattended/README.md` | `wc -c -l`; `grep -n '^## '` | **4092 bytes / 71 lines**, FOUR `##` sections at `:9`, `:24`, `:49`, `:58` |
| `tools/unattended/kit.toml`'s legs | `grep -n gate_leg` | FOUR `[[gate_leg]]` rows at `:107`, `:117`, `:124`, `:131`, all `subject = "repo"` |

**CARRIED from earlier passes, not re-derived here:** rev-6's wider fixture table (§2.1); the 37 tracked
`RUN.md` phase split; the 477 workflow run records with `agentCount` median 9, max 79; and
`wf_9b984206-816`'s three sequential `await workflow()` calls.

**NOT VERIFIED, and named — SEVEN:**

1. **That a Skill bullet authorizes a Workflow call.** The load-bearing assumption of the whole hoist.
   Measured: no allowed-tools key, zero mentions in 791 lines. **Probe: dispatch the child once from a run
   that has loaded the rendered Skill and record whether the call is TAKEN.** It is U2's acceptance.
2. **Whether the hook SHOULD read anything but fan-out and join shapes.** It does not; whether extending it
   is desirable, affordable or well-defined is open and filed.
3. Whether the PreToolUse-to-load gap is racable.
4. Whether the hoist raises the stall rate.
5. Whether a `runId` survives a compaction.
6. **Whether a recipe-mode build's unit set is necessarily empty, and whether the harness throws on it.**
   U8 measures it; §9 D3 states the decision it feeds.
7. The wall-clock cost of N child workflows against one roster agent, in either direction.

---

## §9 — DECISIONS

Four owner rulings, all dated **2026-09-04**, of which **D4 was retaken the same day after the design
corrected the facts it had been decided on**. Two prior rulings are withdrawn and one is moot; they are
kept here so a reader meeting a rev-5 citation finds its disposition.

### D1 — `tools/unattended/SKILL.template.md` JOINS THE VETO-2 LIST. *(owner, 2026-09-04)*

**The list is five pairs, not four:** `BUILD-METHOD` (template + render), `UNATTENDED-PROTOCOL` (template +
render), `agent-cap.js` + `tools/hooks/README.md`, the new `tools/workflows/unattended-unit.js` as a public
surface, and now `tools/unattended/SKILL.template.md` + its render. Veto 2 is `BUILD-METHOD.md:84`.

**Consequences, all worked through above:**

- **It settles N1 FOR the hoist and closes the fork.** §2.2 records the closure rather than the question.
- **The standing cost is larger than prose edits**, because `check-kit-versions.sh:179-192` puts a version
  marker in that file: **every `unattended` kit-version bump is now an owner turn.** Written into
  `tools/unattended/README.md` (§4.4), with the two rejected placements and their reasons.
- **The RENDER is not a second carrier** (§4.4c): a run MAY regenerate `.claude/skills/unattended/SKILL.md`
  from an owner-approved template, and MAY NOT hand-edit it — and only the second is CAUGHT, by
  **`unattended skill wiring`** on every bar.
- **Eight of ten §7 units are owner-gated**, five of them only through the version-marker coupling.
- **What it does not buy** (§10): an owner-gated carrier does not stop a run editing the working tree. It
  makes the edit a reviewable act in a diff.

### D2 — RAISE THE BUDGET TO 27648 BYTES AND BUILD THE CHECKER IN THIS BUILD. *(owner, 2026-09-04)*

Supersedes rev-6's R3 and R4, and **R4 dissolves rather than being answered**: a checker needs an exact
integer, so the cap is written in bytes and the KiB-or-decimal question stops existing (§5B.1). Consequences:
the number and its arithmetic (§5B.2, ≈1550 bytes of headroom after this build, line cap untouched); the
gate is an existing program **three legs already ride** plus one class-scoped pair term at check 6 / exit 6,
both derived free this pass (§5B.3); its declaration act is FIVE items and the second is an `[[exempt_leg]]`
row rather than a `[[gate_leg]]`, because the opposite was tried and withdrawn as `DEPL-dCarriedReceipt-6`
(§5B.4); its failing case is staged and observed before it lands (§5B.5); and the population is one document
today, gated per-subject with a per-class pair term, with the LINE axis left ungated and disclosed (§5B.6).
It becomes **U7**.

### D3 — MEASURE RECIPE MODE BEFORE DECIDING IT. *(owner, 2026-09-04)*

Supersedes rev-6's R6. **Neither option is taken now.** Neither the scope grammar is widened nor the
protocol sentence struck.

**The question the probe answers, stated so a negative is possible:** *does a recipe-mode build have a unit
set at all, and if not, what does the route `passes-harnessed` names actually do when a recipe run takes
it?*

**What the probe constructs, derived from what `authorized-by: recipe` requires** (`SKILL.template.md:298-366`,
keys at `:332-338`, read this pass): a build folder at `memory/builds/<slug>/README.md` with the six
required keys (`:261`) and the generated-region marker pair, plus `authorized-by: recipe`,
`playbook: <repo-relative path>` and `pieces: <n>`. **For `--plan` alone, the playbook and the push are not
needed** — `verb_plan` never reads `authorized-by`; what it reads is `git ls-files "<dir>/spec/*.md"`
(`:2043`) and the generated units region. **So the smallest honest recipe build for this probe is that
README, with an empty units region and no specs, STAGED — not merely written.** Staged rather than committed
because `git ls-files` reads the index, and an unstaged folder would produce an empty spec set for a reason
that has nothing to do with recipe mode, which is the dishonest version of this measurement.

**And it runs in a scratch clone, not the real tree.** `memory/project/readme-contract.txt:1-27` (read this
pass) has `gen_build_index.py --check-format` refuse *a tracked build README named by no row at all* in the
forward direction (`:3-4`), against an `exempt-pin` EQUALITY (`:11-14`) — so staging a probe build in the
live tree would owe a contract row and a pin move for a folder nobody intends to keep.

**The two halves of the measurement:** (i) `bash tools/unattended/unattended.sh --plan <slug>` on that
folder, recording the exact `next:` line and the exit code; (ii) the harness invoked with the unit set that
produces, recording whether `unattended-build.js:118-124` throws.

**The decision it feeds, and only this one:**

- **If the unit set is empty and the harness throws**, then `passes-harnessed` binds a route a recipe run
  cannot take, and the choice is between leaving the scope `all` and correcting `UNATTENDED-PROTOCOL.md:637`
  to match, or widening the scope grammar to a mode LIST — `check_waiver_scope`'s equality at
  **`unattended.sh:1172`** becomes a membership test, `DIRECTIVES_FLOOR="17"` is unaffected, and the Skill's
  Scope cell moves with it.
- **If it is not empty**, the protocol sentence at `:637` is simply wrong and is struck, and no grammar
  moves.
- **A prose exemption in M6 is refused either way**: prose cannot make a core directive optional, and §5's
  new body term would then certify a false sentence.

**WHAT THIS DESIGN SHIPS WITH, said plainly.** `UNATTENDED-PROTOCOL.md:637` says *"Recipe mode does not take
it: its pieces are not specs"* while `unattended.sh:469` binds `passes-harnessed` in every mode
(`scope_of` → `all`, `:505-514`). **That is a live carrier/registry disagreement, on the bar today, and it
stays there for the duration of this build** — from U2's landing until U8 reports. Nothing in the edit set
takes a side: the M6 route sentence of §4.1 carries no recipe clause, the §12 correction touches
`:635-637`'s first two sentences and leaves the third, and the `:642` strike is about the pass-order leg.
**U2's M6 sentence asserts NEITHER side.**

### D4 — THE EDGE, PLUS VALIDATION AT INSTALL, PLUS ANNOUNCEMENT AT GATE. *(owner, 2026-09-04 — CORRECTED AND RE-DECIDED THE SAME DAY)*

**Why it was retaken.** The owner was told the `review-harness` edge would make an adopter get the harness or
not get the kit. **That was FALSE.** `requires` is read only by `derive_install_order` (`govkit.py:486-518`),
filtered `if d in want` at `:504-505`, and `resolve_selection` (`:521-590`) never expands a selection at any
of its four call sites. Observed this pass: **`plan --kits unattended` into a target with neither dependency
exits 0 and previews an `unattended`-only install.** The owner was told, and chose **all three mechanisms**.

**The edge STAYS, for ordering.** `tools/unattended/kit.toml:7` → `requires = ["memory-tree", "review-harness"]`.
It buys correct install order when both kits are selected, and the dependency written down as data where a
reader can find it. Nothing else.

**(i) VALIDATE AT INSTALL, in two arms and two verbs** (§4.5b, §4.5c):

- **arm A — REGISTRY**, extending `selfcheck` check 7 (`govkit.py:1326-1341`), modelled on `requires_if`'s
  arm at `:1330-1333`. It validates the NAME because `selfcheck` has no target and no receipt, so the name
  is the only question it can answer. **Ran over all 25 entries this pass: nine edges, zero hits, and the
  nine passing edges enumerated.** Its failing case is a staged typo; the green half is already observed.
  Boundary: **`govkit selfcheck`**, every bar. It owes a `selftest.py` arm and a `refusal_join.py`
  `BRANCH_PIN` bump.
- **arm B — INSTALLED SET**, in `cmd_apply` (`govkit.py:4243`) right after AC8 (`:4282-4288`), where the
  satisfied set is exactly `selection ∪ receipt.kits` because AC8 has already refused anything else. **It
  REFUSES.** Its cost is stated first: **all nine existing edges fail under a single-kit `--kits` into a
  virgin target, `--kits drift-audit` — the docstring's own legal example at `:495-496` — among them**, so
  that docstring gains a clause in the same commit. **Over the DEFAULT selection and over `--all`, zero
  edges fail.** Boundary for the behaviour: none standing — `govkit selftest` is chunk `selftests`, subject
  `kit`, off even a `GATE_FULL=1` bar.
- **"Adopt time" means `cmd_apply`, not the verb named `adopt`** (`:7650`), which writes a receipt for a
  tree already installed. Naming the wrong one would have put the check where it can never fire.

**(ii) ANNOUNCE AT GATE, as check 31 in `check-unattended.sh`** (§4.5e), leg **`unattended kit gate`**,
number derived free this pass. It scans M6's own slice for the `workflows/*.js` paths U2 writes and splits
four ways: **announced skip** when the carrier is absent, when M6 names no path (the tree's state until U2
lands, so the check is born skipping), and when `tools/workflows/` is absent entirely; **`fail 31`** when the
directory is present and a named script is not. The skip rides the kit's shipped REPORT channel
(`report()` `:591`, `REPORT=${GOV_UNATTENDED_REPORT:-0}` `:590`) in the grammar `:1929` already uses, and its
three shapes — nothing, `unattended-report: check 31 skipped — …`, `UNATTENDED check 31 FAILED — …` — are
byte-distinguishable, which is the arm. **Per-check, never whole-leg**, because a whole-leg skip discards
twenty-nine verdicts to announce one. `fail 31` owes an arm under **`harness arms (fail branches armed or
pinned)`**, on every bar.

**Neither subsumes the other, and the reason is temporal** (§4.5f): (i) runs once, at install, and only for
installs made after it lands; (ii) runs on every bar of every adopter forever, including the population (i)
can never reach — but can only announce.

**§10's adopter residual is NARROWED, NOT RETIRED**, to the three-clause population §4.5f names.

It becomes **U9** (the edge + mechanism i) and **U10** (mechanism ii, after U2).

### Withdrawn and moot, kept for citation

- **R1 — WITHDRAWN.** It asked whether "at most 5 verify agents TOTAL" governs sequential disjoint build
  dispatch, to license a `gov:sequential-units` marker. The hoist needs no marker, and the premise was weak:
  `guardAgentSpawn` is reached only on `Agent` (`agent-cap.js:1494-1499`).
- **R7 — MOOT.** It existed only to route an R1 refusal.
- **N1 — CLOSED by D1**, in the hoist's favour. §2.2 carries the argument; this document opens no successor
  fork and no unit is blocked on a ruling.

---

## §10 — WHAT THIS DOES NOT SOLVE

- **THE CHILD'S CONTENT BETWEEN DISPATCHES IS UNGUARDED.** The re-read at `agent-cap.js:1509` feeds three
  burst rules (`:1521`, `:1541`, `:1562`) and one join rule (`:1593`) and nothing else. A second `agent()`
  with any prompt, a nested `workflow()`, a rewritten prompt string and a deleted `export const meta` all
  admit. **The run holds this. Nothing else does.**
- **The read-window narrowing is CONDITIONAL on three things** (§2.4): `scriptPath` rather than `name:`
  (`:1519` exits 0) and rather than inline `script`; and the hook's cwd resolving a relative path. An
  UNREADABLE path fails closed (re-observed, `:1510-1517`); one that resolves in the WRONG tree does not.
  **All three are held by the Skill bullet — now an OWNER-GATED carrier, which is stronger than rev-6's
  position and is still not a gate.** An owner-gated carrier means an edit to it is a REVIEWABLE ACT in a
  diff on a file whose render is byte-compared on every bar by **`unattended skill wiring`**. It does not
  mean the edit cannot happen. Nothing in the tracked `.claude/settings.json` (no Write or Edit matcher, no
  `permissions` block) stops a run editing the working-tree copy, and the wiring leg compares the RENDER to
  the TEMPLATE — a run that edits both consistently reds nothing. **The ruling converts an unreviewed edit
  into a reviewed one; it does not convert prose into enforcement.**
- **`export const meta` has NO enforcer.** Both readers SELECT by it, so deleting it removes the child from
  both populations silently. Asserted once at U4's landing; unread after that.
- **Three of the child's five constraints have NO enforcer.** `function`, `=>` and a non-receiver `.map()`
  all admit. A file-style rule asserted once, with no standing reader.
- **Nothing re-checks that the child does not NEST.** `grep -c "workflow(" agent-cap.js` = 0, and a nested
  call fires no hook (`:9`). Held by U4's acceptance and by review.
- **Nothing under the run's own uid binds the run.** Every property here evaporates in one `Write`. The
  control that binds lives on the remote.
- **LOOP COMPLETENESS RESTS ON ONE OVERRIDABLE CHECK.** `build-complete` term 5 at `--close`
  (`unattended.sh:3353`), exit `--override build-complete`.
- **LOOP ORDER RESTS ON NOTHING THAT SURVIVES A DECLARATION ROW.** The order gate runs only when both units
  carry an `order` verb (`:4630`, `:4639`) — **38 of 61 multi-unit builds cannot offer that** — and a
  sibling's dispatch ROW un-blocks it (`:4647`), a row `--dispatch` writes itself (`:4813`) before the pass
  runs. It has never been observed to fire; U5 adds one arm, which makes it observed, not stronger. And
  `pass-order history` does not cover the gap: it grades spec-before-code for CLOSED units and nothing about
  dispatch (`check-pass-order.sh:22`) or a non-CLOSED unit (`:23-24`).
- **`--dispatch` does not refuse a FORKED unit, a re-dispatch, or a unit already CLOSED — and FORKED is what
  `--plan` names on SIX builds at the tip** (aBatchedLintel, aSurfacedLexicon, aTetheredScratch,
  bConvergentLodestar, dNarrowedAnchor, dPromptedSeam). Each refusal is one line and each owes its own
  failing-case arm, so both are backlog rows rather than units here.
- **A reader can mistake `next: none - no tracked spec grades as a unit` (`:2173`) for completion, on FIVE
  builds at the tip** (aDeployScout, aKitHardener, aLeanRework, aPortableWarden, aRatchetForge). §4.3's
  bullet branches on it; **nothing machine-checks that a run did.**
- **The Workflow-authorization premise is UNVERIFIED** and the hoist multiplies it N+1 times.
- **N returns to the main loop is N stall points**, unmeasured in either direction.
- **M6 will name a concurrent dispatch path this design does not build.** The clause states a permission,
  not a capability.
- **Two loop spellings stay open until U3′ lands**, across SIX predicate sites in THREE forms, and two more
  shapes stay open after it — the local helper and recursion.
- **Under-denial has no standing reader.** The widening's DENY arms live on `agent-cap self-test`, chunk
  `selftests`, which no boundary runs.
- **A resume inside the SPEC/AUDIT prologue still records a second review round.** The hoist shrinks the
  window from the whole build to the prologue; it does not close it.
- **The per-run total stays unbounded and unreadable.** `guardAgentSpawn` never sees a Workflow call, and
  this design adds no counter.
- **THE BUDGET'S LINE AXIS STAYS UNGATED.** `build-method size` measures bytes only (`check-template-size.sh:99-101`).
  `BUILD-METHOD.md:15` argues the byte half binds first at this file's prose density, so this is priced
  rather than overlooked — but a document that grew in lines without growing in bytes would pass.
- **A LATER RAISE OF THE BYTE CAP IS CAUGHT BY NOTHING.** The drift-audit ratchet registry
  (`drift_signals.py:279-290`) parses `KEY = value` scalars, and `tools/template-size-limits.txt` is a TSV,
  so no row is owed there and none would fit. A raise is argued in that file's own comment, exactly as the
  playbook's 49152 is, and nothing grades whether the argument is good.
- **THE MAP BASELINE'S SHRINK-ONLY RULE IS A CONVENTION, NOT A CONSTRAINT.** `memory/map/baseline.toml:10-11`
  says *"Nothing enforces the rule today."* rev-7 cited it as a constraint; nothing new here changes that,
  and the numberless leg name is a convention argument.
- **A forgotten kit-version bump reds nothing** — and under D1 that also means a forgotten bump silently
  skips the owner turn the marker coupling creates. `check-kit-versions.sh:17-19` and `:164-192` grade
  presence and agreement, and no branch in the file reads a diff.

**The adopter block, after D4's three mechanisms.**

- **THE ADOPTER GAP IS NARROWED, NOT CLOSED, and what is left is exactly three clauses** (§4.5f): an adopter
  who installed `unattended` before this lands, **never re-runs `govkit apply`**, and **never sets
  `GOV_UNATTENDED_REPORT=1`**, is still bound by `passes-harnessed` with a route that does not exist in
  their tree, on a bar that is green and silent.
- **Check 31 names the absence, never the remedy.** It does not tell that adopter about the preflight
  `--waive`, and widening it to do so would be a gate handing out its own bypass.
- **Neither mechanism has been observed against a real adopter.** The whole adopter population is outside
  this repo and unmeasurable from it, so both arms' evidence is staged in scratch clones. Saying otherwise
  would be the `passes-harnessed` failure one layer over.
- **A MIS-SPELLED KEY IS INVISIBLE TO BOTH ARMS.** `requires` and `requires_if` are read from two literal
  key names (`govkit.py:504`, `:1330`); a descriptor writing `require = […]` declares nothing, validates
  against nothing, and reds nothing. Backlog row, not a unit.
- **`cmd_apply`'s installed-set arm has no standing behavioural reader.** Its arms ride `govkit selftest`,
  chunk `selftests`, subject `kit` — off even a `GATE_FULL=1` bar. `govkit refusal join` grades that the
  branch is armed, not that it behaves.
- **RECIPE MODE IS UNRESOLVED, AND THE CARRIER AND THE REGISTRY DISAGREE ABOUT IT ON THE BAR TODAY.**
  `UNATTENDED-PROTOCOL.md:637` against `unattended.sh:469`. It stays that way until U8 reports, and D3 says
  so out loud rather than hiding it in a unit.
- **Whether a `runId` survives a compaction** is unverified, so the runtime's prefix cache is a bonus and
  never the mechanism. Under the hoist it matters less: `--plan`'s `next` is a tree fact — **provided
  something flips the status header, which the edited child now instructs and nothing enforces.**


---

## Appendix A — the candidate child, verbatim

`tools/workflows/unattended-unit.js` as measured on 2026-09-04: 110 lines, 6933 bytes. Three gates
re-run at exit 0 — `check-workflow-syntax.js`, `check-verifier-fanout.sh`, and `agent-cap.js` in both
`script` and `scriptPath` input modes. It carries zero `tools/` literals, one `agent(` and zero
`workflow(` in code. `TOOL-aHoistedPass-5` governs it and may correct it; this appendix exists so the
unit has a durable subject rather than a path in a session scratchpad.

```javascript
// unattended-unit.js — ONE unit, ONE agent, oriented in that unit's spec and brief and nothing else.
//
// IT IS A BARE TOP-LEVEL SCRIPT, not a module. The Workflow runtime evaluates the body as an async
// function with the hooks injected as parameters, so `export default` never runs and never parses:
// the workflow-syntax gate beside this file says so in its own header, and its strip regex does not
// match `export default`. `export const meta` is the one export the dialect keeps.
//
// `export const meta` IS A SELECTOR, NOT A REQUIREMENT. Both readers of this file pick their
// population by that exact marker — check-verifier-fanout.sh:86 and check-workflow-syntax.js:30 —
// so deleting it does not fail either gate, it removes this file from both. Their vacuity guards
// (check-verifier-fanout.sh:92-99, check-workflow-syntax.js:89-92) fire only when the WHOLE
// population is empty, and other workflow scripts keep it non-empty. Asserted once, at landing.
//
// IT NEVER NESTS, AND NOTHING CHECKS THAT. The fan-out guard contains no occurrence of the nesting
// primitive's call form at all, so it does not look at nesting; a nested call here would be legal
// at the hook, and one fired from inside this sidechain reaches no hook either (agent-cap.js:9).
// This property is asserted once, when the file lands, and is held after that by review alone.
//
// IT IS ONE STRAIGHT LINE — A STYLE RULE WITH NO ENFORCER. No loop, no array method, no Promise
// combinator, no function definition and no arrow, so the one spawn below is visible in a single
// screen. Measured against the shipped hook: `function`, `=>` and a non-receiver `.map` all ADMIT
// at exit 0. What the hook DOES deny, per dispatch, is a loop around a spawn, a fan-out receiver it
// cannot size, a raw fan-out primitive, an unresolvable bound and a ref-keyed verdict join
// (agent-cap.js:1521, :1541, :1562, :1593). Keep this file that shape anyway, and do not mistake
// the shape for a guarantee.
//
// IT SPELLS NO PATHS. The driver spelling, the ground text, the per-pass checklist command and both
// document paths arrive in `args`, so this file carries no install-prefix literal and needs no
// ratchet row and no method-carriers row.
export const meta = {
  name: 'unattended-unit',
  version: '1.0', // gov:kit unattended-unit@1.0 — engine identity (deployed verbatim)
  description:
    'Builds exactly ONE unit of an unattended build, in a sidechain whose orientation is that unit spec and that unit brief. The roster is not in scope here; the parent holds it and holds the order.',
  phases: [{ title: 'Unit', detail: 'read the brief and the spec, declare the write set, build, commit' }],
}

// ARGS ARRIVE AS A STRING even when the caller hands the tool JSON, so this parses first and
// validates second — ported from unattended-build.js, which added the guard after a sibling harness
// twice reviewed a DIFFERENT repository than the one it was briefed on.
let cfg = args
if (typeof cfg === 'string') {
  try {
    cfg = JSON.parse(cfg)
  } catch (e) {
    throw new Error(
      'unattended-unit: args must be JSON carrying repo, slug, unitId, specPath and briefPath; could not parse the string given (' +
        e.message + '). Refusing to default any of them.',
    )
  }
}
if (!cfg || typeof cfg !== 'object' || Array.isArray(cfg) || !cfg.repo) {
  throw new Error('unattended-unit: args must carry an explicit `repo`. Refusing to default the build root to the process cwd.')
}
if (!cfg.slug) throw new Error('unattended-unit: args must carry an explicit `slug`; every driver verb below is slug-addressed.')
if (!cfg.unitId) throw new Error('unattended-unit: args must carry an explicit `unitId`; this script builds one unit and cannot pick it.')
if (!cfg.specPath) throw new Error('unattended-unit: args must carry `specPath`. A unit built without its spec in hand is the defect this harness exists to close.')
if (!cfg.briefPath) throw new Error('unattended-unit: args must carry `briefPath`. The brief is the only carrier the driver hashes.')
if (!cfg.driver) throw new Error('unattended-unit: args must carry `driver`, the driver invocation. This file spells no install path.')
if (!cfg.ground) throw new Error('unattended-unit: args must carry `ground`, the grounding preamble the parent built.')
if (!cfg.checklist) throw new Error('unattended-unit: args must carry `checklist`, the per-pass bug-class command. It is owed after every commit.')

// `why` is REQUIRED and is never an absence: an empty result with no reason is indistinguishable
// from a clean pass over nothing.
const UNIT_SCHEMA = {
  type: 'object',
  required: ['committed', 'sha', 'why', 'summary'],
  additionalProperties: true,
  properties: {
    committed: { type: 'boolean' },
    sha: { type: 'string' },
    why: { type: 'string' },
    summary: { type: 'string' },
  },
}

phase('Unit')

const PROMPT =
  cfg.ground +
  '\n\nBuild exactly ONE unit: ' + cfg.unitId + '. You are handed two documents and you read both ' +
  'whole before you touch code: the BRIEF at ' + cfg.briefPath + ' and the SPEC at ' + cfg.specPath +
  '. The spec is the design; where you must diverge, CHANGE THE SPEC FIRST as a rev-N bump with its ' +
  'section 9 line, then write the code.\n' +
  'Declare the write set with `' + cfg.driver + ' --dispatch ' + cfg.slug + ' --pass ' + cfg.unitId +
  ' --writes <path>` before you write anything. A REFUSAL FROM IT IS BINDING — read it and stop. ' +
  'ITS SILENCE IS NOT A CLEARANCE: it refuses this unit only for having no tracked spec or a THIN ' +
  'one, plus the shape of the paths you declared; its ORDER gate runs only where this unit AND the ' +
  'blocking sibling both carry an `order` verb, and a sibling that merely declared a dispatch stops ' +
  'blocking whether or not it was ever built. Order is the parent roster you were dispatched from, ' +
  'not something this verb proves.\n' +
  'Record what you were handed with `' + cfg.driver + ' --brief ' + cfg.slug + ' --unit ' + cfg.unitId +
  ' --path ' + cfg.briefPath + '`.\n' +
  'Commit with the unit id in the subject. IN THAT SAME COMMIT, set this unit\'s spec status header ' +
  'to CLOSED — or to WONTDO with a reason. That header is the only fact the driver\'s --plan verb ' +
  'reads to decide a unit is finished, so a unit built without it leaves the run\'s own loop counter ' +
  'naming this unit again, forever.\n' +
  'Then run `' + cfg.checklist + '` and act on what it names ' +
  'before you return. Return committed:false with a `why` rather than a commit you cannot stand behind.'

const r = await agent(PROMPT, { label: 'unit:' + cfg.unitId, schema: UNIT_SCHEMA })

log('unit ' + cfg.unitId + ': committed=' + String(!!(r && r.committed)) + ' sha=' + ((r && r.sha) || '-'))

return {
  committed: !!(r && r.committed),
  sha: (r && r.sha) || '',
  why: (r && r.why) || '',
  summary: (r && r.summary) || '',
}

```
