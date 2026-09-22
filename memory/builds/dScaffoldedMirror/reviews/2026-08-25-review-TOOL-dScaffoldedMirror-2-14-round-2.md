**Serves:** diff-review TOOL-dScaffoldedMirror-2 TOOL-dScaffoldedMirror-6 TOOL-dScaffoldedMirror-7 TOOL-dScaffoldedMirror-8 TOOL-dScaffoldedMirror-10 TOOL-dScaffoldedMirror-14

# Tier-2 review — dScaffoldedMirror, ROUND 2 (the FIX, not the diff)

**Range:** `a9308644...HEAD` (HEAD at review time = `1704b1b4`) · **ROUND 2** · 2026-08-25 · node `d`.

**Shape:** four lenses — fix-verification, regression-hunt, arm-vacuity, records-and-prose. No
separate skeptic stage: every finding below was reported WITH an observation, and the ones that
mattered were re-observed by hand before being fixed. Two of the four lenses independently found the
same defect twice over, which is recorded rather than deduplicated away, because the agreement is the
evidence.

## Verdict: CLEAN WITH FIXES

Zero blockers, and the verdict says so — but the round is not a mild one, and the count is where the
severity lives rather than in the label. Round 1's fixes did not hold: three introduced regressions,
one was half a fix, and five of the thirteen self-test arms round 1 added **could not fail**. The
arm-vacuity lens reintroduced H3 in full and watched the suite report 146 of 146 green.

Twenty-six distinct defects — two high, eight medium, fourteen low, one carried, one parked.
Twenty-four fixed in this round with an observed failing case each; one carried with a reason; one
parked for the owner, because taking it unattended would have been the very thing this build exists
to stop.

**There is no round 3, and the reason is a real difference rather than fatigue.** Round 1's fixes
were reasoned; round 2's are observed. Every fix above was staged as a break and watched to red the
arm that claims it, and doing that corrected four of my own conclusions along the way — a no-op M4
break, an L1 arm that cannot be tested by weakening itself, an L4 break that crashed instead of
firing, and a D12 arm that passed twice for the wrong reason. The loop rule is zero blockers, the
driver records CONVERGED, and what would make a round 3 worth its tokens is a fresh surface rather
than another pass over this one.

## Round 1's seventeen — disposition

| # | Round-1 verdict | Round-2 finding |
|---|---|---|
| B1 | fixed | RESOLVED. Map tests 5/5, unguarded leg green. |
| H1 | fixed | **PARTIAL** — the fifth condition, DEAD SNIFFER, still disagreed. See D1. |
| H2 | fixed | RESOLVED. One VERBS reader; a colon-bearing gloss round-trips; a perturbed gloss reds. |
| H3 | fixed | RESOLVED in the script — but its ARM could not fail. See D5. |
| M1 | fixed | RESOLVED. Probe is falsifiable at code 0. |
| M2 | fixed | **REGRESSION** — the new anchors were stricter than the `\b` they replaced. See D4. |
| M3 | fixed | RESOLVED, with a mismatched exception pair left behind. See D14. |
| M4 | fixed | RESOLVED. |
| M5 | fixed | **REGRESSION** — three shapes that had been correct broke. See D2. |
| M6 | fixed | **PARTIAL** — three carriers fixed, six more alive. See D9. |
| M7 | fixed | RESOLVED, with an overstated comment. See D24. |
| M8 | fixed | RESOLVED — and it orphaned a CLOSED spec's §7 and AC8. See D19. |
| M9 | fixed | RESOLVED; class filed as `TOOL-dScaffoldedMirror-20`. |
| L1 | fixed | RESOLVED at the third attempt. The round-1 fix `": R"` was itself satisfied by the header's own `): R…`. |
| L2 | fixed | RESOLVED. |
| L3 | fixed | RESOLVED. |
| L4 | fixed | **REGRESSION** — the emptiness guard did not move with the operands. See D3. |

## Round-2 findings

Severity is on the defect, not on the effort. Every row marked FIXED has a staged break recorded
below it or in the commit that carried it.

| # | Sev | Site | Defect | Status |
|---|---|---|---|---|
| D1 | high | `tools/lexicon/lexicon.py:726` | DEAD SNIFFER set `exit_code` directly, 79 lines below the measure-mode return, so `--measure` exited **0** with three clean pins on a tree `--check` redded by name — and the round-1 arm's own comment claimed it "would have caught the DEAD SNIFFER defect as well" | FIXED |
| D5 | high | `tools/lexicon/selftest.py:793` | the H3 arm considered ZERO `render_skill` call sites and two already-checked `write_skill` ones; H3 reintroduced in full left the suite 146/146 green | FIXED |
| D2 | medium | `tools/lexicon/lexicon.py:804` | rebuilding the tail from `subtokens()` lowercases, splits digit boundaries and drops non-word characters: `getUserURLs`→`readUserUrLs`, `fetch_v2_data`→`load_v_2_data`, `create$data`→`build_data`. The last two were CORRECT before round 1 | FIXED |
| D3 | medium | `drift_report.py:1011` | operands moved to `gradeable`, the `if not added` guard did not: an all-ungradeable window returned value 0, of 0, live True, no `not_asked` — and printed a plain `ok` | FIXED |
| D4 | medium | `drift_report.py:275` | the round-1 lookarounds required whitespace-or-start, strictly narrower than `\b`: `#py:`, `# (py:` and `# js,py:` all stopped justifying moves that used to work | FIXED |
| D6 | medium | `tools/lexicon/selftest.py:811` | the `("fetch","load")` row asserted a token the message template always prints, so it passed on the template rather than the suggestion — L1's class inside L1's fix | FIXED |
| D7 | medium | `tools/lexicon/selftest.py:827` | two "rejects the defect form" arms entailed by the row above them, naming spellings the current code cannot produce; green through three separate staged defects | DELETED |
| D8 | medium | `drift-audit/selftest.py:812` | the L4 non-vacuity arm guarded `before["of"] > 0`, a property of the previous window; nothing asserted the commit reached the signal | FIXED |
| D9 | medium | nine files | the frequency-ranking claim had NINE carriers. Round 1 fixed the three inside `scaffold_lexicon.py`. The survivors included the refusal printed to an adopter's terminal on the first `--check` of every adoption, the README's Adopting section, the charter bullet, and two files in the shipped `drift-audit` kit | FIXED |
| D10 | medium | `tools/lexicon/README.md:98` | "this repo added 136 definitions and zero offenders… the gate refused nothing" — live signal reads 47 of 331, 14.2%. Not one figure survived, and it is the premise of the whole Supply section | FIXED |
| D11 | medium | `spec/…-10.md:38` | S7 declared BUILT at rev-4; `git log --name-only` over the whole build returns nine files under `tools/lexicon/` and `LEXICON.md` is not one. A Definition-of-Done item contradicted by git | FIXED |
| D12 | low | `adopt-lexicon.sh:67` | the version capture is a pipeline and takes `head -1`'s status, so an unreadable constant renders `gov:kit lexicon@` with nothing after it — and `--check` reports "Skill in sync", because it compares a render against a render and both carry the same empty version | FIXED |
| D13 | low | `lexicon.py:641` | the round-1 hoist COPIED the pin parse instead of moving it; the upper copy discarded its value for a side effect | FIXED |
| D14 | low | `lexicon.py:908` | `--brief` caught `(SyntaxError, ValueError)` against the corpus loop's `(SyntaxError, OSError)` — missed the unreadable file, and would report an internal bug as "does not parse" | FIXED |
| D15 | low | `README.md:127` | names `lexicon skill wiring`, the leg M8 deleted | FIXED |
| D16 | low | `canon.py:40` | "EIGHT are in no cluster… the other two" — its own data says seven and three; `t` is element 3 of the `test` cluster four lines down | FIXED |
| D17 | low | `lexicon_conf.py:3` | "Three consumers… when its unit unparks" long after it unparked; the dossier says four and lists them correctly | FIXED |
| D18 | low | `builds/…/README.md:36` | the opening diagnosis in the present tense, plus a line pointer that had come to name the replacement | FIXED |
| D19 | low | `spec/…-10.md:279,299` | §7 and AC8 name the leg M8 deleted; the unit's real net effect is a guard change | FIXED, rev-5 |
| D20 | low | `map/features/lexicon.md:28` | `cmd` inserted out of order in an otherwise alphabetical claim | FIXED |
| D21 | low | `selftest.py:769` | the agreement arms asserted exit codes alone — agreement on the number 1 for two different reasons is not agreement | FIXED |
| D22 | low | `selftest.py:760` | `ZZZ_STALE` declared, then a different waiver string hardcoded in the loop it was declared for | FIXED |
| D23 | low | `selftest.py:840` | label says "exit 1 stays reserved for VERDICTS"; the arm never reads the exit code | FIXED |
| D24 | low | `lexicon.py:96` | the M7 fix comment claims the two catalogs "graded python through a different code path". They did not — `extract_text` dispatches on `mode` and reads `pset` only under `probe`. A fix comment is read as provenance | FIXED |
| D25 | low | `subtokens.py:20` | ASCII-only: `délete_user` grades as verb `d`, and a fully non-ASCII name is skipped with no report at all | CARRIED |
| D26 | — | `.memory-tree.conf:207` | the charter's read path is 51 B under its declared ceiling, so no new ratified decision record can be written | PARKED |

## How each fix was observed

A gate seen only passing is an assertion about nothing, so every one of these was staged.

- **D1** needed an ISOLATED tree to prove. Three earlier probes reused this repo's own
  `.lexicon.conf`, whose LAYERS rule and `.pyc` files raise two other problems that already redded
  `--measure` and masked the disagreement entirely. On a tree whose only problem is a blind sniffer:
  pre-fix `--check` 1 / `--measure` **0**; post-fix 1 / 1.
- **D2** measured against sixteen identifier shapes. Three are now correct that were correct in
  NEITHER the original nor round 1: `GET_USER_DATA`→`READ_USER_DATA`, `FetchUserData`→`LoadUserData`,
  `fetch_conf_`→`load_conf_`.
- **D3** required its own repo. Appending an ungradeable file to the existing fixture leaves the
  earlier gradeable definitions in a cumulative window, so it is not all-ungradeable at all; the
  first spelling of the arm papered over that with an `or of > 0` escape and stayed green with the
  guard reverted.
- **D5** staged as `[ -n "$CONF" ] && write_skill` — a `&&` BEFORE the call, which makes it
  conditional and discards its status. The rewritten predicate also refuses that shape over a
  synthetic line, so it is tuned to the shape rather than to the current file.
- **D6**, **D7** and **D8** staged by replacing the whole `swap` expression with a constant, by
  reintroducing M4 and M5 separately, and by patching the extractor to skip word-character-free names.
- **D12** produced two vacuity defects in its OWN new arm before it was right: the refusal arm first
  passed on a bash invocation error, then on a missing-declaration refusal. Both are non-zero exits.
  It is falsifiable now because the sandbox carries a valid declaration, so deleting the guard makes
  `--render` exit **0** and ship a version-less marker.

Suites: `lexicon selftest` 146 → **163** arms; `drift-audit selftest` +9.

## Carried and parked, with reasons

- **D25** is pre-existing, out of reach of this repo's corpus, and a real hole in a predicate that
  silently mis-selects its population. It wants its own unit, not a patch at the end of a fix round.
- **D26** is the one thing here that is not mine to decide. The read path is six files, 133899 B,
  against a declared 133950 — and a `DECISIONS.md` row costs about 295 B under the 300-char index
  cap. The record that is owed is a supersession of `TOOL-dScaffoldedMirror-18`, which says gov takes
  the 459-row backfill and lands it; `-9` is DEFERRED under the owner's own six-units ruling, so a
  session reading the decision index first concludes gov holds the backfill. The three ways out are
  raising the ceiling a second time inside the build that exists to stop exactly that, trimming ~300 B
  from four binding protocol guides at speed with no owner turn, or leaving a §6 obligation unmet for
  a byte budget. Parked with all three written down.
- **M9's class gate** stays filed as `TOOL-dScaffoldedMirror-20` rather than half-built: neither
  `check-wiring.sh` (which resolves python only to NAME it in a remedy string and executes none) nor
  the shipped `drift_report.py` (whose adopters hold no kit descriptors) is a home it works in.

## The pattern worth naming

Two lenses reached it independently, and it is the transferable finding of the whole round:

**A finding reported as `file:line` gets fixed at `file`.** M6 was reported at
`scaffold_lexicon.py:44`; the claim had nine carriers and the three inside that file were repaired.
D9's survivors included the message an adopter reads on their first run. The repair for a
claim-level defect is a repo-wide grep for the claim's WORDS, run AS the fix rather than as the
verification afterwards — which is how the two carriers in the shipped `drift-audit` kit surfaced,
since no lens had named them.

The second pattern is narrower and sharper: **an arm written to close a vacuity finding is written
under time pressure by someone who has just been told they are bad at this, and is therefore prime
territory for the same defect.** Five of round 1's thirteen arms were vacuous, one of them inside the
fix for vacuity; and D12's arm reproduced the class twice more while being written. The only thing
that caught any of them was staging the break.

## Appendix — what the lenses were told was by design

Carried from the round-2 briefing so the fan's priming stays auditable: the `subtokens.py` port is
deliberate and its parity leg is gov-internal; the kit is opt-in and reports `NOT ADOPTED` at exit 0;
the seed ships `PROPOSED` with `ratified` empty on purpose; `LAYERS` seeds empty and an unarmed P3
reds; `VERB_OFFENDER_PIN` falling 463 → 384 is the shrink-only doctrine working. The lenses were also
given this repo's own recurring classes — `armed-but-unreachable-rule`,
`fixture-passes-by-finding-nothing`, `two-answers-to-one-question`,
`assertion-between-two-derived-values` — and asked for new instances rather than re-reports. Three of
the four returned instances of the second class in code written to close the first.
