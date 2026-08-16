# Review — aSiftedPlaybook spec set, round 5 (M4 spec audit)

**Serves:** spec-audit TOOL-aSiftedPlaybook-1 TOOL-aSiftedPlaybook-2 TOOL-aSiftedPlaybook-3 PLAY-aSiftedPlaybook-3 PLAY-aSiftedPlaybook-1 PLAY-aSiftedPlaybook-2 PLAY-aSiftedPlaybook-4

## Verdict: CLEAN WITH FIXES

*Synthesis pass over the `d64c388..HEAD` fold delta — the round-4 fold (`3d98e85`), the post-fold
run-state refresh, and the `origin/main` reconcile. Four lenses -> batched skeptics -> one synthesis;
**4/4 lenses live, 0 dead, 0 dead skeptic batches, 0 spurious / duplicate / conflicting verdicts**.
**26 raw judged — 10 confirmed, 16 refuted, 0 unverified.** The 10 confirmed collapse to **5
findings** after merging: three lenses filed the same `govkit`-at-BASE frame error, two filed the
same AC3-at-BASE frame error, two filed the same stale receiver count, two filed the same AC8 gap.
**Every finding below was re-measured by this pass against the working tree before it entered the
table**, and the re-verification changed the set — three gradings moved and one rationale was
corrected rather than inherited. The changes are listed in Coverage.*

*Round 4 returned BLOCKED with one blocker, five highs, four mediums and four lows. **The whole fold
landed.** B1, B1's second half, H1, H2, H3, H4, H5, M1, M2, M3, M4, L1, L2, L3 and L4 all reproduce
as fixed against source, and so do all four of the revision-log entries round 4 ordered corrected —
they are annotated in place rather than rewritten away, which is what round 4 asked for. Nothing in
the round-4 fold list is outstanding. The five findings below are new: one hole the round-4 fold
walked past while fixing its twin, one half of a two-part remedy, and three provenance labels the
fold itself introduced.*

**No blocker.** Nothing in this spec set reds a gate, contradicts a mechanism, or requires a design
decision to resolve.

| id | sev | file:line | finding | fix |
|---|---|---|---|---|
| H1 | high | `spec/2026-08-16-spec-TOOL-aSiftedPlaybook-1.md:250` | **S5's carrier is observed by no acceptance criterion anywhere in the build, and the fold that gave `README.md:33` its own AC13 for exactly this reason left the identical hole one scope item over.** AC3 is the only sweep AC and its pathspec is `-- ':!memory/'`; the kickoff manifest S5 edits now lives at `memory/guides/SESSION-KICKOFF.md`. Measured at HEAD: AC3's grep returns eleven hits, none under `memory/`, while `git grep -nE '<same pattern>' -- 'memory/guides/'` returns the live carrier `memory/guides/SESSION-KICKOFF.md:121` — "The template is under a STRICT 32 KiB gate. Never raise it". The hole was opened by the relocation, not by the spec: at BASE the same grep DID see it (`.claude/SESSION-KICKOFF.md:99` and `:100`). I enumerated all sixteen ACs (AC1, 2, 3, 3b, 4, 5, 7, 7b, 9, 8, 6, 6b, 10, 12, 13, 11) and none reads that file's body; no AC in any of the other six specs names it either. **AC4 does not cover it** — I read `skills/session-kickoff/manifest-check.sh` end to end and every `last-audit` reference is block/ratchet/watch-pathspec validation (checks 2, 3, 5, 6, 9); nothing reads the trap prose, so a re-stamp satisfies AC4 with the trap intact. **This build states the standard it is failing here**, in a sentence this same fold wrote: PLAY-1 §3:84-89 says `README.md:33` is received "on all three of the carriers that make a hand-off real: it is named in that unit's scope item, it has its own §4 inventory row, and its **AC13** observes it … The AC is the load-bearing one — AC3's alternation cannot match '19-check', so without it every criterion in the receiving unit goes green with the defect shipped." S5 has the scope item (`:49-53`) and the §4 row (`:163`) and no AC, for a structurally identical reason: AC3's pathspec cannot reach `memory/`. No prior round adjudicated this — round 3's only S5 refutation was about the manifest's path spelling, and round 4's S5 items were M7 and M10. **What ships wrong:** every TOOL-1 AC goes green while the mandatory-read kickoff manifest keeps instructing every session that the gate is a strict 32 KiB never to be raised, after the owner raised it to 49152 — the declared-routed-and-unreceived shape round 2 filed as B1, round 3 as H6 and round 4 as H1. | Add an AC13-shaped criterion for this carrier: when `grep -nE '32 ?KiB\|[Nn]ever raise' memory/guides/SESSION-KICKOFF.md` runs, it reads the new ceiling and no never-raise clause. Alternatively narrow AC3's exclusion to the corpora §3 actually names (`':!memory/builds' ':!memory/archive' ':!memory/DECISIONS.md' ':!memory/backlog'` — measured: 15 hits across 8 files, the carrier among them, and the extra `memory/map/*` hits are the leg label AC8 and AC5 already own). **A positive pathspec cannot fix it** — git exclusions win, and `-- ':!memory/' 'memory/guides/SESSION-KICKOFF.md'` returns zero SESSION-KICKOFF hits (measured). |
| M1 | medium | `spec/2026-08-16-spec-TOOL-aSiftedPlaybook-2.md:203` | **Round-4 M1's remedy was two-part per arm — "Add two rows to TOOL-2 S2's table … and extend AC8 to them" — and the second part landed for one arm.** S2's table gained both A10 (`:34`) and A11 (`:35`); AC8 (`:203-210`) enumerates mutations for A6/A7, A8, A9 and A10 and stops. `grep -n 'A11'` over the whole spec returns exactly `:35` (the table row), `:48` (S2 prose) and `:289` (the log). No other AC reaches it: AC1 is existence-only, AC2 is the `-gt`/`-lt` inversion, AC3 is A4's CRLF, AC7 is the `ARMS_FLOORS` entry. The rev-7 log at `:288-289` nonetheless certifies "Added **A10** (absent record) and **A11** (non-numeric), with AC8 extended" — the half-applied-remedy-plus-certifying-log recurrence round-4 M1 was itself filed for. AC8's closing sentence is now stale against its own body as well: it scopes itself to "The ratchet arms", which S2:37 defines as A6-A9, while the criterion already reaches A10. **What ships wrong:** A11 is the arm for the contract "non-numeric high-water → a NAMED failure, not a shell error" — the failure mode round 4 filed because `set -u` is live at `tools/check-template-size.sh:11` with the numeric comparison at `:28`, on a leg the bar runs twice. With no mutation criterion a builder can write A11 as a bare non-zero-exit assertion, which a `set -u` explosion also satisfies, and every AC in TOOL-2 stays green. `check-arms.py` cannot backstop it — S6 reads the `ARMS_FLOORS` values from `--report` *after* the refactor, so a gate built without the non-numeric fail branch yields a floor derived from its own omission. §5 names arm vacuity as this unit's notable risk by name. | Add the A11 limb to AC8 on the same model as the others — when the non-numeric branch is made to fall through to the numeric comparison (or to a bare shell error) instead of a named failure, **A11** reds — and re-word the closing sentence so it quantifies over the arms that now carry red proofs rather than over "the ratchet arms". Correct rev-7 `:288-289` to name which arms AC8 reaches. |
| L1 | low | `spec/2026-08-16-spec-TOOL-aSiftedPlaybook-2.md:149` | **The blocker fold's own reproduction evidence is attributed to a revision where the command cannot run.** Three carriers say the measurement was taken "in a scratch clone of BASE" — §4 `:149` ("**Mandatory and measured:** in a scratch clone of BASE, `python tools/govkit/govkit.py selfcheck` exits 0 with `0 unclaimed`"), AC9 `:214` ("Reproduced at BASE rather than argued"), rev-7 `:282`. Measured: `git ls-tree -r --name-only 91ef1b05 -- tools/govkit` returns nothing; `git ls-tree -r --name-only HEAD -- tools/govkit` returns 10; the kit lands at `a4caea9`, and `git merge-base --is-ancestor a4caea9 91ef1b05` says NO. BASE is unambiguous in this build — every status header pins `base 91ef1b05` and the build README:37 says "Measured at BASE `91ef1b05`". Round 4's own B1 text said "in a scratch clone of `f43a48c`", which is correct; **the fold degraded a true citation into a false one**. Every anchor in the same cell (`govkit.py:501-519`, `registry.toml:150`, `:134`/`:142`/`:146`) is likewise post-merge, and the quoted numbers are the HEAD numbers — I ran it at HEAD: `surface 37 tracked path(s) · 17 entr(y\|ies) · 10 exemption(s) · 0 unclaimed`, exit 0. **Graded low, not medium:** the obligation the cell states is true at the tree the unit lands on, AC9 is checkable and green at HEAD, and three other carriers already date `govkit` to the merge (TOOL-1 §7:329 "new since the merge", PLAY-3:125 "arrived with the merge at `8712ac0`"), so nothing a builder ships depends on the label. It is the same class round 4 graded L2. | Replace "BASE" with the tree the measurement was taken on in all three places — `:149`, `:214`, `:282` — e.g. "in a scratch clone of `f43a48c`" or "at this branch's HEAD", and say in AC9 that the leg post-dates BASE so the observation is only available post-merge. |
| L2 | low | `spec/2026-08-16-spec-TOOL-aSiftedPlaybook-1.md:33` | **The new S2 sub-item justifying `:14` states a measurement that does not reproduce at the revision it names.** `:33-34` reads "Run at BASE, AC3's grep returns eleven hits and `:14` is one of them; it was named by neither S1 (which scopes `:19` …)". Measured at BASE: the grep returns **twelve**, not eleven (the two extra are `.claude/SESSION-KICKOFF.md:99` and `:100`, a file the manifest move retired), and `git show 91ef1b05:tools/check-template-size.sh \| sed -n '14p'` is `MAX_BYTES=${MAX_BYTES:-32768}` — the constant assignment, i.e. exactly the line S1 owns. Both numbers and the line identity are HEAD facts: at HEAD the grep returns eleven and `:14` is the precedence comment quoted verbatim. **In the frame the sentence names, its own argument inverts** — `:14` IS what S1 names, so the sub-item reads as duplicated scope a verifier would delete. The rev-8 log repeats it at `:405` ("is one of AC3's eleven BASE hits"). **Graded low, not medium:** every acting carrier is HEAD-relative and consistent (S1's `:19`, the §4 row's `2-5, 8, 14, 31-32`, and AC3's grep, which takes no rev argument and therefore runs at HEAD), so the operative claim "`:14` is in scope because AC3 measures it" is true where the builder works, and AC3 is the backstop if the item is dropped. | Change "Run at BASE" to the post-merge tree / HEAD in both places — `:33` and the rev-8 clause at `:405`. |
| L3 | low | `spec/2026-08-16-spec-TOOL-aSiftedPlaybook-3.md:122` | **A spelled population went stale in the commit that changed it.** TOOL-3 §4's new row asserts in the present tense "AC10 observes it and §7 runs it, and this row is the third carrier so **all three receivers** of that obligation match", while the same fold made TOOL-2 a fourth receiver. Enumerated at HEAD, four units carry the `govkit selfcheck` obligation in all three sections: TOOL-1 (§4 `:165`, AC12 `:297`, §7 `:329`), TOOL-2 (§4 `:149`, AC9 `:211`, §7 `:230` — all three added by this fold as round-4's blocker B1), PLAY-3 (§4 `:188`, AC10 `:242`, §7 `:273`), TOOL-3 (§4 `:122`, AC10 `:203`, §7 `:215`). PLAY-3 §7 `:276`, added by the same fold, carries the same three ("the three units receiving this obligation each carried it in a different subset of sections"). It contradicts TOOL-1 AC12 `:299-301` in the same delta, which says "the build creates five such paths across four units" — a figure I measured and confirmed: `template-size-highwater.txt`, `check-template-size.test.sh`, `playbook-kit-waivers.txt`, `check-playbook-parity.sh`, `check-playbook-parity.test.sh` across TOOL-1/2/3 and PLAY-3. **Graded low, not medium:** all four receivers are in fact complete, so a reader auditing three reaches the same verdict as one auditing four and nothing ships wrong — round 4 adjudicated this same class by measurement and downgraded it for the same reason. It stays on the list because it is an affirmative false statement about the build's own population, in the build whose subject is that class, and because it re-introduces the count TOOL-1 AC12 deleted two sections away. | De-number both, matching the policy TOOL-3 `:178` states ("derivation, never a count") and AC12 adopted in this same fold: "every unit that creates a depth-1 `tools/` path carries this obligation in §4, §7 and an AC". Same edit at PLAY-3 `:276`. |

## Per-spec rev-bump fold list

- **`TOOL-aSiftedPlaybook-1` → rev-9** — **H1** (an AC observing the `memory/guides/SESSION-KICKOFF.md` carrier, or AC3's `':!memory/'` narrowed to the corpora §3 names — not a positive pathspec, which git ignores), L2 (S2 `:33` "Run at BASE" → HEAD; the rev-8 clause at `:405` with it).
- **`TOOL-aSiftedPlaybook-2` → rev-8** — **M1** (AC8 gains the A11 limb; its closing sentence re-scoped off "the ratchet arms"; rev-7 `:288-289` names which arms AC8 reaches), L1 (`:149`, `:214`, `:282` re-framed off BASE).
- **`TOOL-aSiftedPlaybook-3` → rev-11** — L3 (`:122` de-numbered).
- **`PLAY-aSiftedPlaybook-3` → rev-9** — L3 (`:276` de-numbered).
- **No fold owed** — `PLAY-aSiftedPlaybook-1` (rev-7), `PLAY-aSiftedPlaybook-2` (rev-7), `PLAY-aSiftedPlaybook-4` (rev-4), the build `README.md`, and `build/2026-08-16-build-aSiftedPlaybook-1-playbook-audit.md`. All three of the round-4 items in those carriers reproduce as folded.

## Checked and clean

- **The entire round-4 fold list reproduces as landed**, verified against source rather than against the revision logs: **B1** (TOOL-2 gained the §4 registry row at `:149`, the §7 gate line at `:230` and **AC9** at `:211`), **B1's second half** (TOOL-1 AC12's "three units in this build create one" is gone; `git show 3d98e85` confirms the clause was deleted, not corrected, and what replaced it is the binding rule "Each unit declares its own paths; none quantifies over the others'"), **H1** (`README.md:33` now has the §4 inventory row at `:162` **and** **AC13** at `:303`; PLAY-1 §3:84-89 and the audit report's bullet at `:83` both re-worded), **H2** (PLAY-3 AC7 `:251-257` now reads "the template at the parent of the bump commit — observed as `git show <bump>^:…`" and says in terms it is NOT the pre-build blob), **H3** (TOOL-1 AC7 `:267` re-worded against the keyed record, **AC7b** `:274` added for the second-consumer observation), **H4** (TOOL-1 §10 `:491-499` enumerates the fourth record and closes "All four"), **H5** (PLAY-3 S7 `:43` now spells `lib` and `hooks` bare and points at TOOL-3 §10 as the owner; §4 `:129-130` and `:187` with it), **M1** (A10 and A11 both in S2's table), **M2** (PLAY-3 `:149` deletes the subtotal — "The table IS the gated total and no subtotal is spelled here" — and TOOL-1 S8 `:82-98` re-derives its forecast from the table with the argument made independent of the value), **M3** (the README's `B*` count deleted at `:94-96`), **M4** (PLAY-4 §1 `:7-12` restated over four defects and three files, §4 `:82-86` gained the `WIRE-INTO-PROJECT.md` row and S4's `customize.md:15`), **L1** (`:464`), **L2** (`5fd7c7e`), **L3** (PLAY-3 S7 `:51-53` points at TOOL-3 S1), **L4** (PLAY-3 §7 `:273` gained the gate line; TOOL-3 §4 `:122` gained the registry row).
- **All four revision-log entries round 4 ordered corrected are corrected, and correctly.** TOOL-1 rev-6 `:417-420`, PLAY-3 rev-6 `:331-334` ("*this clause was WRONG and round 4 measured it so*"), PLAY-3 rev-7 `:322-323`, and PLAY-1 rev-7 `:241-248`. Each annotates the false clause in place instead of rewriting it away — the discipline round 4 asked for by name, and the reason this round could trust the logs enough to spot-check rather than re-derive every one.
- **The `govkit` obligation itself is complete in all four receivers.** Only the count describing them is stale (L3). I checked each unit's §4 row, §7 line and AC individually; none is missing.
- **TOOL-1 AC12's residual figures are correct.** "Five such paths across four units" measures exactly right — `tools/template-size-highwater.txt`, `tools/check-template-size.test.sh`, `tools/playbook-kit-waivers.txt`, `tools/check-playbook-parity.sh`, `tools/check-playbook-parity.test.sh` across TOOL-1, TOOL-2, TOOL-3 and PLAY-3. The bolded "No count … is stated here" sitting one clause from a retrospective figure is a wording tension in an explanatory sentence that governs nothing; four lenses filed variants and the skeptics refuted all of them. Not folded.
- **AC6's "§10's recall result and this list are the same four" is satisfiable and was refuted on measurement.** Four lenses filed it; four skeptic passes refuted it. Re-measured: §10 `:485-499` names four records and closes "All four remain accurate as of their dates", AC6 `:288-292` enumerates the identical four inline, and §10 `:491-492` says in terms that the fourth was "added by hand and named here so AC6's identity clause is true of this section". The cross-check AC6 asks for succeeds. The residue is a preference for "§10's enumeration" over "§10's recall result" on a clause round 4 already adjudicated and folded as ordered. Not folded.
- **AC13's derivation pointer is sound.** The first of its two named sources, `tools/gate-legs.json:3`, reads `"name": "memory hygiene (20 checks)"` — one answer. `tools/memory-tree/README.md` does disagree with itself (`:6` says 19, `:18` says 20), but that carrier is an explicitly deferred out-of-scope follow-up in this build's own audit report and PLAY-1 §3:81, and AC13's pass condition fixes the value anyway ("every hit reads 20 and none reads 19"), so a mis-derivation fails the criterion that ordered it. Two lenses filed it; both refuted. Not folded.
- **PLAY-3 S7's "is NOT restated here" followed by a gloss** is round-4 H5's own remedy applied verbatim, names TOOL-3 §10 as the owner in the same breath, and the two copies agree. Refuted, not folded.
- **Nothing in the `origin/main` reconcile moved a spec anchor.** The reconcile commit's own message asserts it and I spot-re-derived the anchors this round touches — TOOL-1 `:33`/`:163`/`:250`/`:405`, TOOL-2 `:149`/`:203`/`:214`/`:282`, TOOL-3 `:122`, PLAY-3 `:276` — all hold at HEAD.

## Coverage

Four lenses over the `d64c388..HEAD` fold delta, then one synthesis pass. All four lenses returned;
no skeptic batch died; nothing came back unverified. **Every confirmed finding was re-measured by
this pass before it entered the table**, and the re-verification changed the set in four ways:

- **One rationale was corrected rather than inherited.** The confirming skeptics on the AC8 finding
  argued "A11 is now the only arm in the unit with no proof it can fail". That does **not**
  reproduce — A3 (missing path, exit 2) and A5 (the environment override) carry no mutation
  criterion either. M1 survives on the claim that does reproduce: a two-part remedy applied to one
  part, certified complete by its own log. The refuting skeptics' counter — that AC8 scopes itself
  to "the ratchet arms" (A6-A9), so A11 is outside its remit — is measured as *stale rather than
  exculpatory*: AC8 already reaches A10, which is not a ratchet arm either.
- **Three findings were downgraded from medium to low** — L1, L2 and L3 — on round 4's own
  precedent, applied consistently in both directions. Round 4 graded the `0f4d308` miscitation L2
  and downgraded the receiver-asymmetry item to "a uniformity item that rides the rev bump" because
  nothing shipped wrong. The same test applied here: the frame labels are false, the substance under
  them is true at the tree the builder works in, and the enumerations they mis-count are complete.
- **One finding was strengthened by a carrier no lens cited.** H1 was filed as an AC gap; PLAY-1
  §3:84-89, written by this same fold, states the three-carrier standard by name and calls the AC
  "the load-bearing one". S5 has two of the three, for the identical reason. That sentence is what
  moves H1 from a nicety to a high.
- **Ten confirmed entries merged into five findings.** Three ids filed the `govkit`-at-BASE frame,
  two the AC3-at-BASE frame, two the receiver count, two the AC8 gap.

- **New-material** — read the fold hunks as the unit of review and asked, per hunk, whether the
  ordered edit is the edit that landed. Contributed M1. Its more valuable contribution this round
  was negative: it found that fifteen of the sixteen round-4 items landed whole, which is the
  evidence behind this round's verdict rather than behind any finding.
- **Factual** — re-derived every anchor, count, quoted string and commit id the fold touched.
  Contributed L1 and L2, both of which are errors the fold's own corrections introduced, and the
  measurement that confirmed AC12's "five paths across four units" is right. This lens is the reason
  the two BASE-frame errors were caught at all: they are invisible to a reader who does not run the
  commands at the revision named.
- **Cross-unit** — checked the hand-offs across the seven specs, the README and the audit report.
  Contributed L3 and the four-receiver enumeration that settles it.
- **Premise** — attacked the fold's load-bearing claims rather than its citations. Contributed
  **H1**, the only finding this round with a nameable wrong ship, by asking what observes S5 rather
  than what S5 says. Highest yield per finding for the second round running.
- **Synthesis (this pass)** — re-verified all ten confirmed entries against the tree, merged them to
  five, adjudicated the two lens splits by measuring (AC8/A11: the confirmers' *conclusion* holds and
  their *rationale* does not, so the finding survives with a corrected basis; the receiver count:
  the refuters are right that nothing ships wrong, so it drops to low rather than out), re-ran the
  round-4 fold list item by item against source, and read `manifest-check.sh` end to end to rule out
  AC4 as coverage for H1.

**Report limits.** 4/4 lenses live, 0 dead skeptic batches, 0 unverified findings — nothing in this
round is carried on an unchecked verdict. Two limits are real. First, this pass reviewed the
**delta**, not the whole spec set: a defect that has sat unchanged since rev-1 and survived four
rounds is outside what any of the five lenses looked at, and H1 is proof the class exists — it was
opened by a relocation in `24f3991`, not by any fold, and no round found it until this one. Second,
the round-4 fold list was verified against source at HEAD rather than by re-deriving each round-3
and round-4 finding from scratch; a fold that landed the *letter* of a remedy while missing its
point would read as clean here.

**Disposition — build.** **Yes: the build can proceed to its first code pass from this spec set once
the five findings above are folded, and I agree there should be no round 6.** No blocker exists.
Nothing here reds a gate, contradicts a mechanism, leaves a fork open, or requires a decision — the
entire fold list is one added acceptance criterion, one added AC limb, and four wrong words in six
places. Weighed against round 4, the signal is unambiguous: sixteen of sixteen ordered items landed,
every certifying log entry was corrected as instructed, and three of this round's five findings are
provenance labels rather than design. That is the shape of a spec set that has converged, and the
protocol's own ground applies — a fifth pass over prose that four passes have already worked will
return prose. **H1 is the one worth folding carefully rather than quickly**, because it is the only
finding with a nameable wrong ship: without an AC on the `memory/guides/SESSION-KICKOFF.md` carrier,
a builder can take every TOOL-1 criterion green while the mandatory-read kickoff manifest keeps
telling every future session that the template gate is a strict 32 KiB never to be raised — the
exact rot TOOL-1 §1 exists to prevent, shipped by the unit that exists to prevent it. It is a high
and not a blocker because S5 already instructs the edit in full, with the quoted text and the line
range; what is missing is the net under it, and the net is one grep. Fold the five, bump the four
revs, and build.
