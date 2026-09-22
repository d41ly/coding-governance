# Drift audit — wave 1, CODE

**Serves:** research TOOL-aScouredKit-1
**Commissions:** TOOL-aScouredKit-3 TOOL-aScouredKit-4 TOOL-aScouredKit-5 TOOL-aScouredKit-6 TOOL-aScouredKit-7 TOOL-aScouredKit-8 TOOL-aScouredKit-9

## Verdict: CLEAN WITH FIXES


*Subject: the whole repo at `093730e40355d6a04300966f791f2634379e8b45`. Commissioned question: is
the build drifting — dead or inefficient code, unwired functionality, duplicate or reinvented
functionality? Five lenses, five skeptic batches, 23 raw findings.*

## 1. Verdict

**Yes, it is drifting, and the drift is concentrated in the instruments rather than in the product.**
21 of 23 findings survived a skeptic. Nothing found is a correctness bug in what the kits DO. Almost
everything found is a tool that measures, gates or declares something and gets the answer wrong,
silently.

**The single worst thing is finding F1: `fan_in` in `tools/codebase-map/map_lib.py:823` counts bare
identifier tokens with no symbol resolution, and two shipped consumers act on the ranking.** 63% of
its 2561 edges (1626) are files that merely DEFINE the same name. The top-ranked "seams" are
`Path.read_text` (29/29), `Path.resolve` (25/25), `re.search` (21/21). `gen_map.py
--seed-affordances --top 15` returns 15/15 junk. `map_diff.py --converge` APPENDED 31 WARN rows to
tracked `memory/map/reinvention-backlog.md`, first row `| main | main | ... | 34 |`. That file is
append-only and deduped, so the fiction is permanent, and it ships to adopters. It also falsifies a
recorded claim: `builds/bConvergentLodestar/spec/...-1.md:184` asserts the over-count is "mitigated
by import/identifier scoping", and the measurement says it is not.

Runner-up, and the worst SYSTEMIC item: two manifest fields decide whether a gate leg runs
(`subject == kit` OR `chunk == selftests`, `tools/run-gates/run-gates.sh:947`) and the ratchet built
to make that decision visible in a diff pins only one of them (F18). Independently re-derived here at
093730e4: 86 legs, 40 `subject=kit`, 43 `chunk=selftests`, **46 held under the runner's real
predicate** — and `govkit selfcheck` prints `40 held` (F19).

Severity after correction: **5 high, 7 medium, 9 low, 0 blocker.** Both original blockers were
downgraded, both for the same honest reason — the mechanism is real, nothing is broken in this tree
today, the trigger is an adopter or one future edit.

**Run integrity: clean.** 5/5 lenses returned, 0 died. 5/5 skeptic batches returned, 0 died. 0
spurious verdicts discarded, 0 duplicates, 0 contradictory verdicts demoted. This run is complete.
9 severity corrections, **all nine downward, zero upward.**

## 2. CONFIRMED findings (12)

Severity is the post-correction grade. Only F7 and F16 carry a skeptic annotation without a change;
both are noted in §3.

| id | sev | file:line | claim |
|----|-----|-----------|-------|
| F1 | high | `tools/codebase-map/map_lib.py:823` | `fan_in` counts bare tokens with no symbol resolution; 1626/2561 edges (63%) are same-name definers, and both shipped consumers act on the ranking — `--converge` wrote 31 false rows into tracked `memory/map/reinvention-backlog.md`. |
| F10 | high | `tools/drift-audit/drift_report.py:78` | The docstring claims it is "a deliberate COPY" of `map_lib.load_conf` and that the drift is gated against bash. Both false: it dropped `removeprefix('export ')` and the ends-at-whitespace rule, and the cited gate's 4-spelling fixture at `selftest.py:98-104` covers neither divergence. |
| F19 | high | `tools/govkit/govkit.py:1413` | The reported held count uses `subject == 'kit'` alone. Prints `86 pinned · 40 held`; the runner's own last green recorded 46. The 6 in the gap include BOTH run-gates canaries, which `run-gates.sh:939-944` calls the bar's own liveness assertion. |
| F2 | medium | `tools/codebase-map/map_diff.py:204` | `dead_exports: 412` is 100% false positives; 385 (93.4%) are module-private helpers zeroed by the `- {def_file}` subtraction. The printed caveat names the smallest class present and omits the one covering 93%. The figure cannot move. |
| F14 | medium | `tools/memory-tree/check-method-carriers.sh:59` | One `grep -lF` spawn per TRACKED FILE (1156 here) to return a 14-element list. Reproduced 22.45s vs 0.69s batched, identical output — 32x. `subject=repo`, `guard=[]`, so it runs on every bar in every adopting tree, linear in THEIR whole repo. |
| F15 | medium | `tools/unattended/check-playbook.sh:162` | 941 markdown files each opened by a `grep -q` spawn to discover a population of ONE. Reproduced: 44.1s of discovery loop vs 1.17s batched, same single result. Unguarded, ships at `tools/unattended/kit.toml:96`. |
| F16 | medium | `tools/check-install-prefix.sh:67` | Two per-file grep loops, 354 spawns. Arm 1 10.74s vs 0.30s; arm 2 (`carried_rows`, `:183`) 19.24s vs 0.28s, identical 107 rows. `carried_population()` also runs twice on the `--check` path (`:222`, `:225`) at 2.11s a call. |
| F21 | medium | `tools/drift-audit/drift_report.py:496` | `stalled` uses `shrunk_by <= 0` where `shrunk_by = seed - now`, so a list added EMPTY is a permanent offender no edit can clear. `shrink_only_lists_not_shrinking 3/5` is 2 real offenders plus one un-drainable; the signal can never reach its own tolerance of 0. |
| F3 | low | `tools/unattended/unattended.sh:498` | `is_scope()` has exactly one occurrence repo-wide — its own definition — and `scopes()` at `:496` has no other caller, so both are dead. The real consumer, `check-unattended.sh:197`, rebuilds the set by hand as `AUTH_SCOPES="all $AUTH_MODES"`. |
| F7 | low | `tools/govkit/entries/playbook.kit.toml:206` | `kit = "cross-os"` is read nowhere and names a `[[block]]` from the `when:` namespace, while its only sibling at `:115` names a real registry entry. Two rows, one key name, two namespaces, no reader to notice. |
| F13 | low | `tools/unattended/check-unattended.sh:1193` | Check 10 renders the protocol pair with an unanchored global `sed -e "s|$PREFIX||g"` over the LIVE copy. Both sibling parity gates migrated off exactly this form and document why in their own headers. Latent today: neither file contains a kit path. |
| F17 | low | `memory/backlog/TOOL.md:244` | `TOOL-aCollapsedScan-5` is OPEN and states "no leg in tools/gate-legs.json declares a wall-clock ceiling". Re-derived here: all 86 legs declare one, 0 without. The row's ASK survives (cost policing) while its FACT does not. |

## 3. PARTIAL findings (9) — corrected severity beside the original

Every partial was downgraded. In seven of the nine the skeptic confirmed every mechanical claim and
cut the grade for impact; read these as facts you can rely on with an inflated headline.

| id | orig → **corrected** | file:line | what survived, and what did not |
|----|---------------------|-----------|--------------------------------|
| F9 | blocker → **high** | `tools/memory-tree/check-memory-hygiene.sh:62` | SURVIVES: the gate SOURCES `.memory-tree.conf` in bash, then delegates 4 checks to five Python readers that each re-parse it with `v.strip().strip('"').strip("'")` — `corpus_ids.py:118`, `gotchas.py:92`, `gen_build_index.py:233`, `check-arms.py:82`, `row_grammar.py:93`. Reproduced: `MEMORY_ROOT=memory   # note` takes `gotchas.py --check` from rc=1 to rc=0 over an identical planted violation, because the Python half walks a directory that does not exist. Coverage is REMOVED, not failed closed. CUT: no tracked conf in this repo uses an inline comment or `export`, so the trigger is an adopter writing a legal spelling the kit's own example neither shows nor forbids. Latent, not live. |
| F18 | blocker → **high** | `tools/govkit/subject-pins.tsv:3` | SURVIVES: `chunk` appears nowhere in `govkit.py` except an unrelated ls-files variable at `:3270`, in no `[[gate_leg]]` claim, and in no other pin file. Demonstrated: flipping `memory hygiene` to `chunk: selftests` leaves `govkit selfcheck` rc=0 and unchanged, and the leg leaves every bar at every boundary. `GATE_FULL` does not lift the hold; no boundary sets `GATE_SELFTESTS`. CUT: nothing is mis-chunked today — all 43 selftests legs are intended holds — and the exploiting edit is still visible in a `gate-legs.json` diff. |
| F4 | high → **medium** | `tools/govkit/govkit.py:4366` | SURVIVES: `read_descriptors` (`:6644-6657`) is `load_toml` and nothing else — no known-key allowlist exists. Injected `bogus_key` and `guard`→`gaurd`; selfcheck exited 0 both times with zero mentions. Silent at three stations: `leg.get("guard", [])` at `:4307`, the guard omitted from the emitted leg at `:4335`, and the UNGUARDED warning at `:4366` predicated on the one state it therefore cannot report. CUT: the comment at `:4290` reasons that a dropped guard "only costs an unnecessary run" — a typo lands in the deliberately-chosen SAFE direction. General class worth a gate; not a live coverage hole. |
| F11 | high → **medium** | `tools/check-testsuite-counts.sh:27` | SURVIVES: `MANIFEST=tools/gate-legs.json` is hardcoded where `run-gates.sh:84` derives the identical file and its `:76` comment says a hardcode "resolves to nothing at any other prefix". Reproduced at prefix `scripts/`: exit 2, permanently, unrepairable in-band. Its descriptor repeats the literal beside a placeholder at `:28`. `check-install-prefix.sh` is structurally blind — its needle requires a `tools/<kit>/` shape. CUT: the CLASS is already specced twice, as `TOOL-aBoundedCeiling-7` and `DEPL-dCarriedReceipt-15`. What is new is only that this instance sits outside both that row's measured 59-file population and the gate's needle. |
| F5 | medium → **low** | `tools/unattended/kit.toml:44` | SURVIVES: `requires_config_first` has exactly one occurrence repo-wide, its own declaration, and no reader in `tools/`. Its `[adopt]` sibling `mutates_index` IS derived and asserted both directions at `govkit.py:1128`/`:1143`, so the asymmetry is real. CUT: no live defect demonstrated, and "the kit governing runs that merge and push" is rhetoric — the key controls install ordering, not run authorization. |
| F6 | medium → **low** | `tools/drift-audit/kit.toml:26` | SURVIVES: `placeholders` on `[[files]]` has no reader anywhere, and 3 of 10 rows have already drifted — drift-audit declares `MEMORY_ROOT`, memory-tree `:28` declares `TOOL_ROOT`, `:34` declares `KIT_DIR`, each absent from its own template. CUT: nothing breaks and nothing can — `render-doc.sh` substitutes both tokens unconditionally regardless of the claim, and all drift is in the safe direction. Dead documentation in a descriptor. |
| F8 | medium → **low** | `WIRE-INTO-PROJECT.md:130` | SURVIVES: `drop_blocks` is documented as an operator control and fully implemented in `render_playbook.py` (`:356`, `:377`, `:385`), and `grep -c drop_blocks tools/govkit/govkit.py` is 0 — `cmd_intake` has no answer, flag or prompt for it. CUT: hand-authoring `deploy.toml` is the sanctioned and actually-used path — this repo's own `.governance/deploy.toml` is hand-written and `matrix.py:264` writes the key by hand too. Failure direction is fail-safe: a charter keeps two blocks it may not need, never loses a rule. |
| F12 | medium → **low** | `tools/workflows/drift-audit-state.js:385` | SURVIVES: the aggregate `downgrades` counter is absent from state.js's RUN INTEGRITY line and `severityCorrections` from its return, both of which `drift-audit-code.js` has (`:377`, `:415`, `:467`). CUT: "never reads it" is false — `judged` is JSON-serialized wholesale into the synthesis prompt, so the per-finding value DOES reach the writer. One counter short of parity, not a missing block, and `README.md:10` says plainly no caller in this tree reads the return keys. |
| F22 | medium → **low** | `tools/drift-audit/drift_signals.py:80` | SURVIVES: the gloss for `memory/project/unarmed-branches.txt` says "empty today and meant to stay so"; the file holds three rows (`unattended.sh` checks 9, 27, 29) and the live signal reports `entries 3`. The file's own header was already corrected for this exact class — the gloss is the surviving copy of a claim the source retracted. CUT: it is a `what` label in `--json` detail rows only; no verdict, count or gate leg is affected. |

## 4. UNVERIFIED findings: ZERO

**No finding went unreached by a skeptic.** All 23 raw findings received a verdict. 5/5 lenses
returned and 5/5 skeptic batches returned, with 0 deaths on either side, so the zero is not a
coverage gap wearing a clean number — it is real. **This is positive evidence:** every claim below
has been independently re-run by an agent that was prompted to refute it, and the two that could be
refuted, were. Nothing in this report rests on a finder's word alone.

The limit is COVERAGE, not verification. Five lenses cannot exhaust a repo this size, and a class no
lens was pointed at is absent from this report for that reason and no other.

## 5. REFUTED findings (2)

| id | file:line | why it was dismissed |
|----|-----------|---------------------|
| F20 | `tools/gate-legs.json:991` | "All 86 ceilings are ≥10x measured, so `cost is a verdict` cannot fire." Every number reproduces (median 37.8x, worst 1229x, `memory hygiene` 12720s vs 22.5s) and none of it is drift: `ee0e7547` and `spec-TOOL-aBoundedCeiling-1` rev-5 record an owner ruling that a ceiling is a HANG bound, not a cost budget. The proposed fix (`measured*2+60s`) is TIGHTER than the 3x/60s rule already tried and reverted after 12 of 40 legs timed out with nothing hanging. |
| F23 | `.githooks/pre-push:215` | "Predicate 8 is unreachable because nothing sets `GATE_SELFTESTS`." Wrong three ways: `:135` sources `.githooks/gate-env.sh` BEFORE the predicate, so the variable IS the coverage of the run about to happen — the finding's own proposed fix, already implemented; the `0 file(s) assign` figure is a deliberately ASSERTED invariant with a recorded owner ruling (`TOOL-dUnstalledConvoy-28`); and `pre-push.test.sh` arms 22, 23, 24, 24b exercise the predicate in both directions. |

Both refutations are the same shape: **a real measurement, correctly taken, of a state that a
recorded decision already chose.** Neither finder read the decision. That is a cost of the review,
not a defect in the tree — but it is the argument for feeding reviewers the by-design set, which
§8 of the charter already mandates.

## 6. Instrument integrity — can this repo's own drift metrics be trusted?

**Read this section first if you are about to act on any number this repo prints about itself.**

Loudly, and up front:

- **`govkit selfcheck` prints a held count that is wrong by 6 legs, on every run.** `40 held` against
  the runner's true 46 (`govkit.py:1413` vs `run-gates.sh:947`). Independently re-derived at
  093730e4. The 6 include both run-gates canaries — the bar's own liveness assertion.
  `subject-pins.tsv:4` states the rule "`repo` legs run on every bar", which is false for six rows
  in that same file. **Two answers to one question, in an instrument, with the wrong one printed.**
- **The subject ratchet cannot fail on the edit that would matter most.** `chunk: selftests` removes
  a leg from every bar at every boundary and the ratchet is blind to it (F18). The ratchet's own
  failure text says "every leg could leave the automatic bar unobserved". It can.
- **`shrink_only_lists_not_shrinking` can never reach 0** (F21). One of its 3 reported offenders is
  `corpus-path-unresolved.txt`, seeded empty, whose own header says empty is the SUCCESS state. A
  signal that cannot reach its tolerance can never be promoted to gateable — the "permanently-red
  decoration" its own sibling comment warns against.
- **`dead_exports: 412` is 100% false positives and structurally pinned at ~59% of the corpus**
  (F2). It cannot move on any repo that uses module-private helpers, which is every repo.
- **The SEAM ranking is 63% noise and two shipped consumers act on it** (F1), one by writing to a
  tracked, append-only file.
- **A gate asserted as coverage in a docstring has never observed its failing case** (F10). The
  bash-equivalence arm at `selftest.py:96-123` exists precisely to catch parser divergence and its
  fixture covers neither divergence that exists.
- **A `what` label tells operators three live unarmed fail branches are "empty today"** (F22).

What is HONEST, verified by the same lens: the codebase-map ratchet moves; the LANGS mode ratchet
moves (the finder refuted itself on this one); both EMPTY-BY-DECLARATION rows are backed by
two-directional selftest arms; the DEAD PROBE is honest about being dead; and the 10x ceilings are a
ratified hang bound rather than a slack cost budget (F20 refuted). The bar itself prints the correct
held figure in its own summary — the wrong number is govkit's, not the runner's.

**Net: the gates that RUN are sound. The instruments that DESCRIBE what runs are not.** Every
finding in this section is a tool reporting on a tool. None is a leg that fails to catch what it was
written to catch.

## 7. Cross-cutting themes — HOW drift enters here

Six mechanisms, each supported by more than one finding.

**1. The instrument ships before its failing case is observed.** F10 (a fixture covering four
spellings, neither of them the divergence it names), F18 (a ratchet pinning one of the two fields
that decide), F19 (a count computed with a different predicate than the thing it counts), F21 (an
offender test a success state can never pass), F4 (a warning predicated on the one state it cannot
reach). The charter already states the rule verbatim in §7: *a new gate is not landed until its
failing case has been observed.* Five instruments here were landed without it. This is the dominant
mechanism and the one with the cheapest countermeasure.

**2. A declaration is free; a reader is optional.** F5, F6, F7, F8 — four keys that read as true and
are consumed by nothing, two of them already drifted from what they assert. The enabling condition
is F4: descriptor tables have no known-key allowlist, so authoring a key costs nothing and no station
ever objects. Fix F4 and this whole class stops being possible to author.

**3. Two readers of one config, one re-derived.** F9 (five naive Python parsers against a bash
`source`), F10 (a "deliberate COPY" that diverged three ways), F3 (`check-unattended.sh` rebuilding
the scope set by hand beside a comment defending derivation), F11 (a hardcoded manifest path beside
a sibling that derives it and says why). **This class is already a named gotcha in this repo's own
memory** — `memory/gotchas/two-readers-of-one-config-one-re-derived.md`. It has produced four fresh
instances since being recorded. Recording a gotcha did not left-shift it; only a gate does.

**4. A catalogued cost class re-entering through new unguarded legs.** F14, F15, F16 — one process
spawn per file in a while-read loop, all three `subject=repo` with `guard=[]`, all three shipped to
adopters, none carrying the "batching rejected" note that their sibling
`check-agent-cap-restatement.sh` carries. The class is
`memory/gotchas/process-creation-is-the-suite-cost.md`. Same lesson as theme 3: the memory note is
not a control. ~60s of a 566s default bar, and F14's cost scales with an ADOPTER'S whole repo.

**5. Prose beside a source that owns the number.** F2 (a caveat naming the smallest class present),
F17 (a backlog row whose fact is now false while its ask survives), F19 (a generated header stating
a rule the runner does not implement), F22 (a gloss contradicting its own file). Charter §6 states
this rule and notes it is "the one most often broken by the document that states it". Three of the
four instances are inside the tooling that polices the class.

**6. Token counting dressed as symbol resolution.** F1 and F2 share one root: `fan_in` is a
`len(index[symbol] - {def_file})` over a bare token index. Every downstream number the map produces
inherits it. This is the only theme with a single root cause and the widest blast radius.

**What the themes say collectively:** drift does not enter this codebase through neglected code. It
enters through *newly written measurement code that was never tested against a failing input*, and
through *declarations that nothing is obliged to read*. Both are authoring-time gaps, which is why
every cheap fix below is a gate or an allowlist rather than a cleanup.

## 8. Do this next — cheapest high-value first

Each item names the file to touch. Items 1–5 are one-line-to-one-predicate edits.

1. **Fix the gloss.** `tools/drift-audit/drift_signals.py:80` — drop the cardinality claim from the
   `unarmed-branches.txt` string; the count is derived and printed beside it. (F22)
2. **Correct the stale backlog fact.** `memory/backlog/TOOL.md:244` — rewrite
   `TOOL-aCollapsedScan-5`'s lead sentence to state that all 86 legs declare a ceiling sized 10x per
   `ee0e7547`, and scope the surviving row to the COST half alone. A reader currently greps
   `ceiling`, finds "none exist", and rebuilds what shipped. (F17)
3. **Let a signal reach zero.** `tools/drift-audit/drift_report.py:496` — `shrunk_by < 0` for the
   offender test, and report `shrunk_by == 0 and now > 0` separately. (F21)
4. **Print the count the runner actually uses.** `tools/govkit/govkit.py:1413` — compute held as
   `v == 'kit' or chunk == 'selftests'`, and correct the generated header at
   `tools/govkit/subject-pins.tsv:4`. (F19)
5. **Pin the second deciding field.** `tools/govkit/subject-pins.tsv` gets a `chunk` column,
   compared at `tools/govkit/govkit.py:1404-1411` with the same regenerate-in-the-same-commit
   failure text. Lands with item 4 and makes it fall out automatically. (F18)
6. **Stop the map writing fiction, before fixing the map.** `tools/codebase-map/map_diff.py` —
   gate `--converge`'s WARN emission and `gen_map.py --seed-affordances` off an unresolved index.
   Then decide what to do about the 31 rows already in `memory/map/reinvention-backlog.md`; it is
   append-only, so removing them is a decision, not a cleanup. Cheap arm of the worst finding. (F1)
7. **Batch three grep loops.** `tools/memory-tree/check-method-carriers.sh:52-60`,
   `tools/unattended/check-playbook.sh:156-169`, `tools/check-install-prefix.sh:67` and `:183` —
   plus hoisting the double `carried_population()` call at `:222`/`:225`. All three batched forms
   were run and produce byte-identical output. ~60s off the default bar; F14's saving scales with
   every adopter's repo size. Note the corrected arithmetic on F16: the post-fix leg is ~4.7s, not
   0.63s — the 15.0s saving holds, the ~96% figure does not. (F14, F15, F16)
8. **Observe the failing case, then align the parser.** `tools/drift-audit/selftest.py:98-104` —
   add `export FOO=bar` and `INLINE=v   # note` to the fixture, confirm RED, then align
   `tools/drift-audit/drift_report.py:99-102` with `map_lib.py:190-201`. Fix the false provenance
   docstring at `:78` either way. Do the fixture first; that ordering is the whole point. (F10)
9. **One conf parser, not five.** `tools/memory-tree/corpus_ids.py:118`, `gotchas.py:92`,
   `gen_build_index.py:233`, `check-arms.py:82`, `row_grammar.py:93` — route through one parser
   using the rule `map_lib.py:196-201` documents. `gotchas.py` already imports `corpus_ids.py` at
   `:98`, so the intra-kit seam costs no new coupling. Latent today, silent green when it fires. (F9)
10. **Kill the unread-declaration class at authoring time.** `tools/govkit/govkit.py` — a per-table
    known-key allowlist in `read_descriptors` (`:6644-6657`) with `r.fail` on an unrecognised key.
    This one edit forecloses F5, F6, F7, F8 and every future sibling. Separately split `:4366` so
    "no guard declared" and "all guards dropped" are distinct reports. (F4)
11. **Fix the ranking itself.** `tools/codebase-map/map_lib.py:823` — subtract same-name definers
    (the caller already holds `symbols.json`) and have `build_reference_index` record whether an
    occurrence was dot-prefixed. Both are on-demand code; no committed artifact moves. Then reword
    or drop the `dead_exports` figure at `map_diff.py:204`, whose caveat names the wrong class. Also
    correct the spec claim at `builds/bConvergentLodestar/spec/...-1.md:184`, which this measurement
    falsifies. (F1, F2)
12. **Delete two dead functions or wire one.** `tools/unattended/unattended.sh:496-498` — delete
    `scopes()`/`is_scope()`, or call `is_scope` in `check_waiver_scope` (`:1139`) so a malformed
    scope gets its own refusal instead of `fail 45` blaming the run's mode. (F3)
13. **Converge the third parity mechanism.** `tools/unattended/PROTOCOL.template.md` gets a
    `{{TOOL_ROOT}}` placeholder and is rendered, matching both siblings; or
    `check-unattended.sh:1193` gets a header stating why this pair is deliberately different. (F13)
14. **Fold into the tracked prefix work.** `tools/check-testsuite-counts.sh:27` — resolve the
    manifest as this script's own sibling per `run-gates.sh:84`, and use `{prefix}` in the descriptor
    guard at `check-testsuite-counts.kit.toml:28`. Widen `check-install-prefix.sh:175`, whose needle
    requires a `tools/<kit>/` shape and is structurally blind here. Belongs with
    `DEPL-dCarriedReceipt-15`. (F11)
15. **Three lines for harness parity.** Copy `drift-audit-code.js:377`, `:415`, `:467` into
    `tools/workflows/drift-audit-state.js`. Land with any `TOOL-dTieredTribunal-16` work so all
    three harnesses converge rather than two of three. (F12)

## Appendix — counts, precision, and what precision does NOT mean

```
raw          23
confirmed    12   (3 high, 5 medium, 4 low)
partial       9   (2 high, 2 medium, 5 low — post-correction)
refuted       2
unverified    0
precision  0.86   = confirmed / (confirmed + refuted) = 12/14
```

Counting partials as half-credit gives 0.72 across all 23. Both figures are stated because neither
is the whole answer.

**Correction direction: all nine severity corrections are DOWNWARD. Zero upward.** Read precision
0.86 as: the finders got the FACTS right 21 times out of 23, and got the SEVERITY wrong 9 times out
of 23, always in the same direction. Nothing was fabricated — but a reader who took the raw grades
at face value would have seen two blockers that are not blockers and would have spent the budget in
the wrong order. Precision measures whether the finding is real. It says nothing about whether the
grade is.

Two additional skeptic annotations that are NOT severity changes and are excluded from the nine:
F7 was re-affirmed at low, and F16's grade held at medium while its impact arithmetic was corrected
(post-fix leg ~4.7s, not 0.63s).

**Where findings pull against each other**, stated rather than quietly resolved:

- **F17 (confirmed) and F20 (refuted) rest on the same fact and reach opposite verdicts on what it
  means.** Both agree every leg now declares a ceiling. F17 grades the stale backlog row as drift and
  is right; F20 grades the 10x sizing as drift and is wrong, because the sizing is a ratified
  decision. Same measurement, two questions, and only one of them was a live defect.
- **F9 was downgraded for latency while F10 was confirmed on the same subject.** Both concern
  `.memory-tree.conf` parsing. F9's silent-green mechanism needs an adopter to write a legal spelling;
  F10's false docstring and uncovering fixture are wrong in this tree today. The pair should be fixed
  together, in F10's order — fixture first.
- **F4's fix is the precondition for F5, F6, F7 and F8**, yet F4 was downgraded to medium and three
  of those four to low. The individual grades are right and the aggregate is understated: one
  medium-graded gap is the authoring-time enabler for four low-graded instances, which is why the
  allowlist sits at item 10 rather than at the bottom.
- **F11 is a real instance of a class already specced twice.** It is reported because it falls
  outside both the tracked row's measured population and the gate's needle — not because the class is
  news.

**Run integrity, restated for anyone quoting a zero from this report:** 5/5 lenses returned, 0 died;
5/5 skeptic batches returned, 0 died; 0 spurious verdicts, 0 duplicates, 0 contradictory verdicts
demoted. The `unverified 0` in §4 is therefore evidence, not an artifact of a dead agent.
