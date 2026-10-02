**Serves:** diff-review TOOL-aSightedSkeptic-1 TOOL-aSightedSkeptic-2 TOOL-aSightedSkeptic-3 TOOL-aSightedSkeptic-4 TOOL-aSightedSkeptic-5 TOOL-aSightedSkeptic-6 TOOL-aSightedSkeptic-7 TOOL-aSightedSkeptic-8 TOOL-aSightedSkeptic-9

# Tier-2 closing diff review — aSightedSkeptic, ROUND 1

*The closing review of the build, over the cumulative diff of its nine units at the integration
boundary. The nine units rework the shipped Tier-2 review harness
`tools/workflows/tier2-review.template.js` and its render, and add the replay scorer
`tools/workflows/review_replay.py`. The harness deploys verbatim to adopter repos, so universality
(no path into another kit) is a requirement on every fix below. Node `a`, 2026-10-01, ROUND 1. Every
finding below survived a skeptic prompted to REFUTE it; the grade on each is the binding grade the
skeptic stage assigned under the severity rubric.*

**Reviewed range:** 9fdd0c18d5afac1744c226c3e8ea2716e6d49e30...4c036dc8a84df99b68e08dc3aa91ed61cd9c6eff

## Verdict: CLEAN WITH FIXES

No blocker. Two high findings, both false coverage claims: a spec says a behaviour is "Observed by"
an acceptance arm that never exercises it, and staged breaks of that behaviour stay green. Behaviour
is correct today in both cases, so nothing ships wrong, but the spec ledger misleads the next change.
The medium and low findings are contained: a replay-scorer unit mismatch, a drive-letter ref the
scorer cannot parse, a fix-verdict branch keyed on the wrong condition, and test or wording gaps.
This verdict rests on a run where every lens and every skeptic batch returned (see Run integrity).

## Review shape

- Intensity: full. Round: 1.
- Raw findings 22: confirmed 17, refuted 5, unverified 0 (0 uncertain). Precision 0.77.
- Adjudicated tally by ITEM: 15 items — 0 blocker, 2 high, 5 medium, 8 low.
- Adjudicated tally by RAW confirmed finding: 17 — 0 blocker, 2 high, 6 medium, 9 low.
- Two merges: findings 5 and 21 are one defect (one medium item); findings 16 and 19 are one class
  of unchecked guard (one low item). No other merges.

## Run integrity

- Lenses 5/5 returned, 0 DIED. Skeptic batches 5/5 returned, 0 DIED.
- 0 contradictory verdicts demoted to unverified, 0 spurious verdicts discarded, 0 duplicates.
- Fixes on confirmed findings: 17 judged sound, 0 judged UNSOUND, 0 none proposed, 0 NOT JUDGED.
- Severity on confirmed findings: 0 UNGRADED by the skeptic, 1 RE-GRADED by the skeptic (finding 16,
  medium to low).
- Unverified findings: 0 answered UNCERTAIN, 0 with NO usable verdict.
- Lens notes: none supplied, so every lens ran on the kit's generic brief.
- Intent: 9 spec documents supplied as `specs`, beside the range's commit messages.
- Checklist: 25 items, each assigned to exactly one of 5 lenses: security 5, correctness 5, seams 5,
  verification 5, intent 5.

No lens died, so a zero below (no blockers, no unverified findings) is a count over a full finding
set rather than an artefact of a missing lens. The one non-zero counter is the re-grade of finding
16, which is an adjudication, not a loss; it is stated beside that finding.

## HIGH

### H1 — The synthesis-death and deferred-path CONFIRMED log lines are unchecked (finding 13)

- **Where:** `tools/workflows/tier2-review.template.js:1353` (synth-death) and `:1094` (deferred path).
- **Defect:** Spec 2 S6 (renderFixLine on these paths) and spec 6 S9 (binding grade on these paths)
  both say "Observed by AC3". Both AC3 arms read only the synthesis prompt's CONFIRMED section via
  `scanConfirmedEntries` (`tier2-review.test.sh:665-670`); neither kills the synthesis or a batch.
  The `synth:null` arms (`test.sh:374`, `:1014`) and the dead-batch arm (`:367`) never read a
  `  CONFIRMED [` log line. Three staged breaks (renderFixLine reverted to the raw fix, and both
  grades reverted to `f.severity`) each stayed at 165 passed, 0 failed. On the synth-death path the
  log is the only record of the confirmed set, and the next run reads it.
- **Fix (judged SOUND by the skeptic):** Add two arms. (1) Stubs with `synth:null` and `verify:`
  returning confirmed, severity `blocker`, fixVerdict `unsound`, fixNote `NOTE`; assert every
  `  CONFIRMED [` log line starts `  CONFIRMED [blocker]`, contains `REJECTED` and `NOTE`, and does
  not show the finder's fix as the fix. (2) The same verdicts with `verify:ids-2-2` returning null,
  asserting the deferred-path CONFIRMED lines carry `[blocker]`. Raise `FLOOR_ASSERTIONS` to match.
- **Left-shift gate:** a spec-ledger check that every "Observed by ACn" S-line names an arm whose
  assertions mention the S-line's output surface (log, prompt, result field). Short of that, a §10
  checklist entry: "an 'Observed by' claim is verified by staging the break, not by reading the arm".

### H2 — The uncertain count's separation from the no-verdict count is unchecked (finding 14)

- **Where:** `tools/workflows/tier2-review.template.js:1404` (success note), `:1171` (RUN INTEGRITY),
  `:976` (WARNING lines).
- **Defect:** Spec 6 S8 keeps the uncertain count apart from the no-verdict count and cites
  "Observed by AC5". The AC5 arm (`test.sh:784-791`) asserts only result counts, precision and the
  UNVERIFIED prompt section; it never reads `note`, the RUN INTEGRITY clause or the logs, and no arm
  runs an all-uncertain round. Deleting `&& !uncertainFindings.length` at `:1404` stayed green and
  makes an all-uncertain round report "none judged — no skeptic batch returned a usable verdict",
  the exact misreading S8 exists to prevent.
- **Fix (judged SOUND by the skeptic):** Extend the AC5 arm to assert `r.result.note` starts
  `PARTIAL: 1 finding(s) are unverified — 1 answered uncertain`, RUN INTEGRITY contains
  `1 answered UNCERTAIN by a skeptic, 0 with NO usable verdict`, and a log line starts
  `WARNING: 1 finding(s) answered UNCERTAIN`. Add an all-uncertain arm
  (`'verify:': buildGradedVerdicts('uncertain')`) asserting the note contains
  `none confirmed or refuted` and `5 answered uncertain`.
- **Left-shift gate:** the same spec-ledger check as H1; this is the same class (an "Observed by"
  claim no arm discharges), so one gate covers both.

## MEDIUM

### M1 — The replay scorer's known set is raw confirmed findings on the appendix path, while every doc says adjudicated items (findings 5 and 21)

- **Where:** `tools/workflows/review_replay.py:10` (docstring) and `:120` (appendix branch of
  `parse_record_findings`); README `:231`; the map dossier; spec 9 F2.
- **Defect:** The ledger and appendix carry one row per RAW finding
  (`tier2-review.template.js:1018-1024`, rendered at `:1048-1055`); synthesis merges raw findings
  into items separately. `review_replay.py:120-128` takes each confirmed appendix row as a known
  item, and liveness compares rows to the raw `confirmed N`. The docstring, README and spec 9 F2 say
  the known unit is the ADJUDICATED ITEM, "not its raw confirmed findings". So a defect two lenses
  confirmed counts twice on the appendix path and once on the legacy path, and recall from the two
  record eras is in different units while the tool claims they are the same.
- **Note on the refuted sibling:** finding 10 (same line) was refuted because spec 9's extraction
  rule 1 deliberately takes appendix confirmed rows as the items. That refutation stands for "the
  code departs from the spec"; findings 5 and 21 stand because the spec contradicts itself (rule 1
  against F2) and the docstring and README state F2's unit. The cheap fix therefore corrects the
  documents to match the built behaviour, which is consistent with both verdicts.
- **Fix (judged SOUND by the skeptic):** Either state in the docstring, the README and the dossier
  that an appendix-sourced known set is per RAW confirmed finding and print that unit on the
  `replay: known` header line, or collapse confirmed appendix rows sharing one file within
  `--window` into one item before scoring. Add a selftest arm in which two confirmed appendix rows at
  one location are pinned to the chosen behaviour, and bump `ARMS_DECLARED`.
- **Left-shift gate:** the selftest arm above is the gate for the class (it pins the unit); printing
  the unit on the header line makes any later drift visible in every run.

### M2 — A drive-lettered ref is unparseable, so a candidate at the exact location never matches (finding 4)

- **Where:** `tools/workflows/review_replay.py:66` (`extract_line_ref`).
- **Defect:** `LINE_REF` is anchored by `match()` and `[^\s:]*` cannot cross the drive colon, so
  `extract_line_ref('C:/projects/x/tools/a.sh:12')` returns None (probed). The harness ledger ref is
  the finder's raw `${f.file}:${f.line}` (`tier2-review.template.js:800`), never normalized, and
  finders on the Windows nodes write absolute `C:/` paths. The candidate reads CANDIDATE-ONLY, the
  known item MISSED, and recall is understated with no refusal. On the known side the ref becomes
  UNSCORABLE, and on the legacy path the parser falls through to the next backticked token.
- **Fix (judged SOUND by the skeptic):** In `extract_line_ref`, after the backslash fold, strip a
  leading drive prefix (`re.sub(r'^[A-Za-z]:/', '/', s)`) so the absolute path keeps its suffix and
  `check_same_file`'s endswith rule matches it. Add a selftest arm with a drive-lettered candidate
  ref and bump `ARMS_DECLARED`.
- **Left-shift gate:** the selftest arm; extend it to the known side (an appendix ref with a drive
  letter must score, not read UNSCORABLE).

### M3 — An unsound fix's reason-only note is presented as a corrected fix (finding 6)

- **Where:** `tools/workflows/tier2-review.template.js:944-952` (`renderFixLine`) and `:1035-1040`
  (`confirmedFindings`); skeptic prompt at `:897`.
- **Defect:** The skeptic prompt says fixNote "says why and gives the corrected fix when you have
  one", so a non-empty, reason-only note is the INSTRUCTED shape for an unsound fix with no
  correction. The code branches on note emptiness, so that reason is shown to the synthesis as "the
  reason and the corrected fix" and handed onward as `confirmedFindings[].fix`. Spec 2's "say the fix
  is still to be designed" outcome is reachable only when the skeptic disobeys its prompt.
- **Fix (judged SOUND by the skeptic):** Split the question: the skeptic returns the reason in
  fixNote and the replacement in a separate optional field (e.g. `fixCorrection`); render
  `STILL TO BE DESIGNED` and keep `confirmedFindings.fix` as the finder's fix (marked rejected)
  whenever that field is empty. The cheaper alternative: tell the skeptic fixNote holds ONLY the
  corrected fix, empty when it has none, and put the why in `reason`.
- **Left-shift gate:** an arm whose verify stub answers `unsound` with a reason-only note and no
  correction, asserting `STILL TO BE DESIGNED` in the synthesis prompt and the finder's fix (marked
  rejected) in `confirmedFindings`.

### M4 — The candidate side of the replay scorer has no liveness check (finding 17)

- **Where:** `tools/workflows/review_replay.py:395-398` (`main`); compare the known side's
  `no-scorable` refusal at `:146-147`.
- **Defect:** A confirmed candidate row whose ref `extract_line_ref` cannot parse becomes path None
  and is skipped by `measure_recall`. Nothing counts how many candidates were scorable, so if the
  harness's ref shape drifts (a renamed field, `a.js:undefined`, a section-addressed ref) every
  candidate is unscorable and the tool prints `recall 0/m` at exit 0. A probe that cannot move reads
  as a measured miss. The ref is still printed, so it is not wholly silent.
- **Fix (judged SOUND by the skeptic):** Count the candidates with no path; print
  `candidate unscorable N` on the candidate line; refuse (exit 2, `no-scorable` on the candidate)
  when confirmed rows exist and none parse. Add a selftest arm that feeds a candidate appendix whose
  confirmed ref is `-` or `x.js:undefined` and asserts the refusal; bump `ARMS_DECLARED`.
- **Left-shift gate:** the selftest arm. Class-level: §7's liveness rule says a probe that cannot
  move must say so; a §10 entry "every scorer side reports its unscorable count" covers the class.

### M5 — The `sound` and `none` fix-verdict branches and their RUN INTEGRITY counts are unchecked (finding 15)

- **Where:** `tools/workflows/tier2-review.template.js:947` (`renderFixLine`), `:1166-1167`
  (RUN INTEGRITY counts).
- **Defect:** Every fix-verdict arm drives only `unsound` (AC3/AC4 via `buildFixVerdicts`) or an
  absent fixVerdict (AC5 over `ALL_OK`). No arm sends `sound` or `none`; test.sh asserts neither
  `judged SOUND` nor `none proposed`, and RUN INTEGRITY is checked only for `5 NOT JUDGED`
  (`test.sh:710`). Staged breaks (sound printed as NOT JUDGED, the none branch disabled,
  `fixCounts.sound` replaced by 0) all stayed at 165/0.
- **Fix (judged SOUND by the skeptic):** One arm whose verify stub answers fixVerdict `sound` for ids
  1-2, `none` for id 3 and `unsound` for ids 4-5. Assert the CONFIRMED entries carry `judged SOUND`
  and `none proposed`, and RUN INTEGRITY reads
  `2 judged sound, 2 judged UNSOUND, 1 none proposed, 0 NOT JUDGED`.
- **Left-shift gate:** an enum-coverage assertion in the suite: for every legal fixVerdict value,
  at least one arm drives it (derive the value set from the template, not a typed list).

## LOW

### L1 — The specs validation admits `~/` paths and control characters (finding 2)

- **Where:** `tools/workflows/tier2-review.template.js:233` (`specsBadIdx`); the claim at `:226`.
- **Defect:** The predicate refuses only a backslash, a leading `/`, a drive letter and a `..`
  segment. `~/x` (home-relative) is admitted though the comment says anything that could point a
  reviewer outside the repository is refused, and members carrying newlines are interpolated raw as
  `  - ${p}` brief lines. Contained: the caller supplies args, and already controls `context` and
  `byDesign` raw, so the forgery half adds little.
- **Fix (judged SOUND by the skeptic):** Extend `specsBadIdx` to refuse a leading `~` and any
  character below 0x20, or match each member against an allow-list such as
  `/^[A-Za-z0-9._][A-Za-z0-9._\/ -]*$/`. Add both values to the refused-value arm list in
  `tier2-review.test.sh`.
- **Left-shift gate:** the refused-value arm list is the gate; adding `~/x` and a newline member
  pins the class.

### L2 — renderCell and the replay parser disagree on what a line is (finding 3)

- **Where:** `tools/workflows/tier2-review.template.js:1044` (`renderCell`);
  `tools/workflows/review_replay.py:88` (`parse_appendix_rows`).
- **Defect:** `renderCell` folds only CR and LF; `parse_appendix_rows` uses `str.splitlines()`, which
  also breaks on `\x0b`, `\x0c`, `\x1c-\x1e`, `\x85`, U+2028 and U+2029. A split cell yields a
  fragment that does not start with `|`, `elif table: break` fires, and every later row is dropped.
  The report is then refused with a misleading liveness count, or, when only refuted rows follow,
  silently loses them. Escaping prevents a forged confirmed row, so it fails closed.
- **Live instance:** this very record carries it. The appendix row for finding 3 quotes the probe
  `'a<U+2028>b'.splitlines()` with a literal U+2028 that `renderCell` did not fold, so the appendix
  below is a verbatim copy containing the character. Observed while writing this report:
  `python tools/workflows/review_replay.py --known <this record> --candidate <this record>` exits 2
  with `REFUSED known ... liveness: 2 confirmed appendix row(s) against a stated confirmed count of
  17`. The parser stopped at row 3, so this record cannot serve as a replay known set until the fix
  lands. That is the finding reproducing itself, not a transcription error.
- **Fix (judged SOUND by the skeptic):** In `renderCell`, fold every character Python's
  `splitlines` treats as a boundary:
  `.replace(/[\r\n\x0b\x0c\x1c-\x1e\x85\u2028\u2029]+/g, ' ')`. Or have `review_replay.py` split on
  `\n` only (`text.split('\n')` after normalizing CRLF). Add a self-test arm that puts a U+2028
  inside a reason cell. Doing both is cheap and closes the class from each side.
- **Left-shift gate:** the U+2028 arm, plus a replay selftest arm parsing a row that contains U+2028
  and asserting every row survives. Once fixed, re-run the replay over this record as the live check.

### L3 — Two correct guards with no arm that breaks them (findings 16 and 19)

- **Where:** `tools/workflows/tier2-review.template.js:1040` (finding 16: the `&& note` guard on
  `confirmedFindings[].fix`) and `:1390` (finding 19: `...(synth ? { regraded } : {})`).
- **Defect:** Both lines implement their spec correctly (spec 8 S4, spec 6 S7), and both specs cite
  an AC as observing them. The only unsound `confirmedFindings` arm (`test.sh:962-971`) always
  supplies fixNote `better fix`, so dropping `&& note` passes (with it dropped, round N+1's
  priorFindings would carry fix `''`). The six-exit-path arms (`test.sh:1010-1022`) never check
  `regraded`, so an unconditional `regraded,` passes and a caller reads "no id moved" on a run with
  no adjudication. Both staged breaks stayed at 165/0.
- **Grade note:** finding 16's finder graded it medium; the skeptic graded it low, and low is
  binding. It is the RUN INTEGRITY re-grade. Low matches the rubric: the code is correct today and
  the gap misleads no spec reader the way H1 and H2 do, because these AC citations are about
  presence rather than a separately rendered surface. Finding 19 was low at both stages.
- **Fix (judged SOUND by the skeptic, both):** (16) In the AC4 block, add a run with
  `verify:ids-2-2` answering confirmed, fixVerdict `unsound`, fixNote `''` (and one with `'   '`);
  assert `confirmedFindings[1].fix === 'f'` and `fixVerdict === 'unsound'`. (19) In the six-exit-path
  arm, assert `!('regraded' in x)` on the four no-synthesis paths and `Array.isArray(x.regraded)` on
  `complete`.
- **Left-shift gate:** the same spec-ledger "Observed by" check named under H1.

### L4 — The replay selftest duplicates the candidate mapping and has already diverged (finding 18)

- **Where:** `tools/workflows/review_replay.py:288-289` (`run_selftest`) against `:396-398` (`main`).
- **Defect:** The selftest rebuilds the row-to-candidate mapping inline as `r["ref"]`; `main` uses
  `r.get("ref") or "-"`. They already diverge on a `-` ref, so the mapping the live `--candidate`
  path uses is reached by no arm. Spec 9 S7 keeps I/O out of the selftest by design, which excuses
  `main`'s file and git access, not the duplicated mapping. Test-only effect.
- **Fix (judged SOUND by the skeptic):** Move the mapping into one function, e.g.
  `extract_candidates(rows)`, called from both `main` and `run_selftest`. Optionally add an arm
  calling `main([...])` on temp files written from the inline fixtures, asserting exit 0 and the
  recall line.
- **Left-shift gate:** the shared function is the fix for the class; M4's new candidate arm then
  exercises the live mapping for free.

### L5 — parseChecklist's rule text says "indented", the code accepts any continuation (finding 8)

- **Where:** `tools/workflows/tier2-review.template.js:249` (rule text), code at `:256-257`; README
  `:180` states the code's rule.
- **Defect:** The refusal text and the args header say indented lines continue an item; the code
  appends EVERY non-blank line not starting `- `. A non-indented trailer would be silently glued to
  the last item. No effect with `gotchas.py`'s current output.
- **Fix (judged SOUND by the skeptic):** Make the rule text say every following line that does not
  start `- ` continues it, matching the README; or require leading whitespace for a continuation and
  refuse otherwise.
- **Left-shift gate:** an arm feeding a non-indented trailer line and pinning the chosen behaviour.

### L6 — RUN INTEGRITY lists lens notes for a lens a light run skipped (finding 11)

- **Where:** `tools/workflows/tier2-review.template.js:1172-1173`; validation at `:506-511`,
  `notedLenses` at `:518`, injection at `:761`.
- **Defect:** On a light run a lensNotes key for a skipped lens (security or intent) is accepted,
  joins the review key, reaches no prompt, and RUN INTEGRITY still reports "lens notes supplied for:
  security". Contained, because the Intensity clause beside it names security as not run.
- **Note on the refuted sibling:** finding 7 (same line) was refuted as by design, citing spec 7's
  non-goal "special handling of args.lensNotes naming a skipped lens". Finding 11 was confirmed by a
  different skeptic batch. The two readings conflict on whether the wording is a defect at all; the
  binding grade is low either way, and the fix is a wording change that does not add the special
  handling the non-goal excludes, so it is recorded here and is safe to take or leave.
- **Fix (judged SOUND by the skeptic):** Report the notes of skipped lenses apart (e.g. "lens notes
  for skipped lenses, unread: ...") in the log and RUN INTEGRITY, or filter `notedLenses` by
  `runningLensKeys` for the "supplied for" clause.
- **Left-shift gate:** a light-run arm with `lensNotes {security: ...}` asserting the chosen wording.

### L7 — The map dossier still claims the three review pipelines carry the same accounting (finding 12)

- **Where:** `memory/map/features/review-harnesses.md:120` (the Gaps bullet).
- **Defect:** The diff edits this dossier (it adds the review_replay paragraph above `## Gaps`) but
  leaves the bullet saying the three pipelines "now carry the same accounting". tier2-review now has
  an uncertain verdict, fixVerdict/fixNote, binding severity and a findings ledger with an appendix;
  the drift-audit siblings have none of them. The next change to a drift-audit harness will read
  parity that no longer exists. Docs only.
- **Fix (judged SOUND by the skeptic):** Amend the Gaps bullet to name what tier2-review gained in
  aSightedSkeptic that the drift-audit siblings lack.
- **Left-shift gate:** none cheap; the bullet already notes nothing structural stops divergence.
  A §10 entry "a dossier claim of parity between kits names the features it compares" is the
  documented check.

### L8 — The unit 9 acceptance ledger's preamble contradicts its own AC8 line (finding 22)

- **Where:**
  `memory/builds/aSightedSkeptic/build/2026-10-01-build-TOOL-aSightedSkeptic-9-1-acceptance-ledger.md:8`.
- **Defect:** 4c036dc8 appended the AC8 (live replay) evidence line but left the preamble saying AC8
  "is not evidenced in this record yet". Two sentences in one record disagree. No behavioural effect.
- **Fix (judged SOUND by the skeptic):** Replace the preamble sentence with one pointing at the AC8
  line and the live-replay record, or delete it.
- **Left-shift gate:** none worth building; a record-hygiene §10 entry "appending evidence re-reads
  the record's own status sentences" is the documented check.

## Refuted (for the record)

Five findings were refuted: 1 (specs trust class, by design per spec 3 §5), 7 (lens notes wording,
spec 7 non-goal), 9 (priorFindings hand-off predates the diff), 10 (appendix rows as items, spec 9
rule 1) and 20 (SCOPE line reading, no run shown). Findings 7 and 10 sit on the same lines as
confirmed findings 11 and 5/21; how the two verdicts coexist is stated under L6 and M1. Their reasons
are in the appendix.

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict |
|---|---|---|---|---|---|---|---|
| 1 | security | tools/workflows/tier2-review.template.js:712 | medium | - | refuted | By design per spec TOOL-aSightedSkeptic-3 section 5 (security): 'Intent documents and commit messages are repository content of the same trust as the diff itself.' The skeptic already reads the author-controlled diff, whose comments can say 'X is intentional' just as well, so no new trust class reaches it. S1 is documented as a guard against a caller's TYPO in args.specs ('so a caller's typo cannot point a reviewer outside the repository'), not an enforcement boundary: finders and skeptics hold full Read/Bash, so a path named in a commit message bypasses nothing S1 enforces. Graded medium and not established as a defect. | sound |
| 2 | security | tools/workflows/tier2-review.template.js:233 | low | low | confirmed | tier2-review.template.js:233 specsBadIdx refuses only a backslash, a leading '/', a drive letter and a '..' segment, so '~/x' is admitted while the comment at :226 claims anything that could point a reviewer outside the repository is refused. The newline-forgery half adds little, because the same caller already controls context and byDesign raw. The consequence is contained to a caller-supplied value, so it is low. | sound |
| 3 | security | tools/workflows/tier2-review.template.js:1044 | low | low | confirmed | renderCell (tier2-review.template.js:1044) folds only \r and \n, while review_replay.py parse_appendix_rows (:88) uses str.splitlines(), which also splits on U+2028, \x85, \x0b, \x0c and \x1c-\x1e. Probed: 'a b'.splitlines() and 'a\x85b'.splitlines() both give ['a','b']. A split cell yields a tail fragment that does not start with '\|', which triggers 'elif table: break', so every later row is dropped and the report is refused with a misleading liveness count. Both sides are new in this diff. It fails closed and is rare, so it is low. | sound |
| 4 | correctness | tools/workflows/review_replay.py:66 | medium | medium | confirmed | Probed: extract_line_ref('C:/projects/x/tools/a.sh:12') returns None, because LINE_REF is anchored by match() and [^\s:]* cannot cross the drive colon. The ledger ref is raw `${f.file}:${f.line}` (tier2-review.template.js:800), never normalized, so a finder writing an absolute Windows path becomes a candidate with path None. It can never match, the known item reads MISSED, and recall is understated silently. On the known side the same ref becomes UNSCORABLE, and in the legacy path the next backticked token is used instead. Both the tool and the ref are new in this diff. | sound |
| 5 | correctness | tools/workflows/review_replay.py:120 | medium | medium | confirmed | The ledger and appendix carry one row per raw finding (tier2-review.template.js:1024 maps the findings), so appendix confirmed rows are raw skeptic-confirmed findings from before synthesis merges or drops them. review_replay.py:120-128 takes those rows as the known items. Meanwhile the docstring (:10), README :231 and spec 9 (:107, F2) say the known unit is the ADJUDICATED ITEM, 'not its raw confirmed findings'. Spec 9 section 1 also calls appendix confirmed rows 'the items', which is the same internal contradiction. Appendix-era and legacy scores are therefore in different units, which skews the cross-version comparison the tool exists for. The effect is contained to how the benchmark is read. | sound |
| 6 | correctness | tools/workflows/tier2-review.template.js:944 | medium | medium | confirmed | The skeptic prompt (tier2-review.template.js:897) tells it fixNote 'says why and gives the corrected fix when you have one', so a non-empty, reason-only note is the instructed shape for an unsound fix with no correction. renderFixLine (944-952) branches only on note emptiness, so that note is presented to the synthesis as 'the reason and the corrected fix', and confirmedFindings (1035-1040) hands the reason onward as `fix`. Spec 2 S-lines 42-43 want 'where an unsound fix's note gives no correction, say the fix is still to be designed'. The code tests 'note empty' instead of 'no correction', so that outcome is reachable only when the skeptic disobeys. The effect is contained to report and next-round wording, so medium. | sound |
| 7 | correctness | tools/workflows/tier2-review.template.js:1173 | low | - | refuted | By design. Spec 7's non-goals list 'Special handling of args.lensNotes naming a skipped lens', and the spec accepts that the light-run WARNING names the skipped lens. The RUN INTEGRITY sentence 'lens notes supplied for: ...' is literally true, because the notes were supplied. It does not claim they were applied, and the adjacent intensity clause names the lenses that did not run. | sound |
| 8 | correctness | tools/workflows/tier2-review.template.js:249 | low | low | confirmed | parseChecklist's `rule` text (line 249) says 'indented lines after an item continue it'. The code (lines 256-257) appends ANY non-blank line not starting '- ' to the last item, indented or not, and README line 180 states the code's broader rule. The mismatch sits only in an error/rule string, and gotchas.py's output indents its continuations, so there is no behavioural effect today. | sound |
| 9 | seams | tools/workflows/tier2-review.template.js:734 | medium | - | refuted | Not introduced by this diff. The base already rendered a prior finding as `ref - claim` only (the same priorFindings.map line), and the 'Judge the FIX' prompt predates it. Spec 8's current-state section (line 123) records knowingly that priorFindings is read as f.ref and f.claim\|\|f.title, and that extra fields 'change the next round's key and nothing else'. Its AC (line 218) asserts only `<ref> - <claim>` in find: prompts. The fold finder reviews the fold diff itself, which is the applied fix. The fix field is therefore a deliberate key-bearing hand-off, not a broken seam. | sound |
| 10 | seams | tools/workflows/review_replay.py:120 | medium | - | refuted | The code implements the spec's explicit rule. Spec 9's Known-set extraction, rule 1, says that for an appendix record the rows whose verdict is `confirmed` ARE the items, each row's ref is its location, and liveness is confirmed-row count against the stated count. F2's 'adjudicated item' resolution exists because legacy records lack raw locations, and appendix records carry them. Scoring the appendix's raw rows is the spec's deliberate choice, not a silent swap. The cross-format comparability concern is speculative design commentary rather than a demonstrated wrong result. | sound |
| 11 | seams | tools/workflows/tier2-review.template.js:1173 | low | low | confirmed | Both lensNotes (unit 5) and intensity (unit 7) are new in this diff; the base has neither. The validation at template.js:506-511 accepts any key in LENS_KEYS, including the lenses a light run skips, and notedLenses = Object.keys(lensNotes) (line 518). The prompt injection at line 761 reaches only the lenses that run, but the RUN INTEGRITY clause at 1172-1173 lists every noted key. A light run with lensNotes {security:...} therefore reports 'lens notes supplied for: security' for a lens that never ran. The effect is contained, because the Intensity clause beside it names security as NOT run. | sound |
| 12 | seams | memory/map/features/review-harnesses.md:120 | low | low | confirmed | This diff edits memory/map/features/review-harnesses.md: it adds the review_replay paragraph just above ## Gaps. It left the Gaps bullet at line 120 unchanged, and that bullet still says the three pipelines 'now carry the same accounting'. The diff made that false. tier2-review now has an uncertain verdict, fixVerdict/fixNote, binding severity and a findings ledger with an appendix, while a grep of drift-audit-code/state.template.js finds none of them. Only the docs are affected, and the same bullet already warns that 'a future divergence has nothing structural stopping it', so this is graded low. | sound |
| 13 | verification | tools/workflows/tier2-review.template.js:1353 | high | high | confirmed | Spec 2 S6 and spec 6 S9 both claim 'Observed by AC3'. Both AC3 arms read only the synthesis prompt's CONFIRMED section through scanConfirmedEntries (test.sh:665-670), and neither kills the synthesis or a batch. The only synth:null arms (test.sh:374, 1014) and the dead-batch arm (test.sh:367) assert exit, pending, ledger length and confirmedFindings length. They never read the '  CONFIRMED [' log lines at template.js:1094 and 1353, and no assertion in test.sh mentions those lines. A regression in renderFixLine or deriveBindingSeverity on those paths would stay green while the spec ledger reads it as covered. That misleads the next change, so it is graded high. Behaviour is correct today. | sound |
| 14 | verification | tools/workflows/tier2-review.template.js:1404 | high | high | confirmed | Spec 6 S8 says the success note and RUN INTEGRITY name the uncertain count apart from the no-verdict count, and cites 'Observed by AC5'. The AC5 arm (test.sh:784-791) asserts only result.uncertain/unverified/confirmed/refuted/precision and the UNVERIFIED prompt section. A grep of test.sh shows no assertion on result.note beyond the clean/deferred arms, and none on 'answered UNCERTAIN' or the UNCERTAIN WARNING log. No arm runs an all-uncertain round. Deleting '&& !uncertainFindings.length' at template.js:1404 would ship the exact 'none judged — no skeptic batch returned' misreading S8 exists to prevent. This is a false coverage claim in the spec, graded high. | sound |
| 15 | verification | tools/workflows/tier2-review.template.js:947 | medium | medium | confirmed | The fix-verdict arms drive only 'unsound' (AC3/AC4 via buildFixVerdicts) and absent (AC5 over ALL_OK). No arm sends 'sound' or 'none', and test.sh asserts neither 'judged SOUND' nor 'none proposed'. RUN INTEGRITY is checked only for '5 NOT JUDGED' (test.sh:710), so the sound/unsound/none counts at template.js:1166-1167 go unchecked. Spec 2 S3/S4 describe all four branches. The defect is a test gap with contained effect, so it is graded medium. | sound |
| 16 | verification | tools/workflows/tier2-review.template.js:1040 | medium | low | confirmed | tier2-review.template.js:1040 implements spec 8 S4 correctly (`fixVerdict === 'unsound' && note ? note : f.fix`), and S4 says it is 'Observed by AC4'. But the only confirmedFindings arm with an unsound verdict (tier2-review.test.sh:962-971, unsound2) always supplies fixNote 'better fix'. The line-698 arm with an empty note is unit 2's and checks the synthesis prompt, not confirmedFindings. So dropping the `&& note` guard passes every arm. This is a real gap in the gate. The code is correct today, so nothing ships wrong. NOTE: the requested durability path under C:/projects/coding-governance/.git/review-lenses/ was refused by the worktree-isolation guard on Write, so the copy is in the session scratchpad named in `path`. | sound |
| 17 | verification | tools/workflows/review_replay.py:398 | medium | medium | confirmed | In main (review_replay.py:395-398), a confirmed candidate row whose ref extract_line_ref cannot parse becomes path None, and measure_recall skips it. The known side refuses 'no-scorable' at line 146-147. The candidate side has no such check, and print_score has no unscorable count for candidates. Harness refs are free text from LLM finders, so a ref with no line is reachable. Such a row prints as CANDIDATE-ONLY, the same as a located miss, and recall is understated at exit 0. The ref is still printed, so this is not fully silent. The tool is informational, so the effect is contained. | sound |
| 18 | verification | tools/workflows/review_replay.py:288 | low | low | confirmed | run_selftest (review_replay.py:288-289) rebuilds the candidate mapping inline as `r["ref"]`. main (396-398) uses `r.get("ref") or "-"`. The two have already diverged on a '-' ref: None vs '-'. So the mapping the live --candidate path uses is reached by no arm. Spec 9 S7 keeps file and git access out of the selftest by design, which excludes main's I/O and scan_corpus. It does not excuse the duplicated mapping. The effect is test-only. | sound |
| 19 | verification | tools/workflows/tier2-review.template.js:1390 | low | low | confirmed | Spec 6 S7 says regraded is absent on every path where no synthesis ran, 'Observed by AC6'. AC6's arm (tier2-review.test.sh:795-797) checks only a synthesis run. The six-exit-path arms (1010-1022) check ledger and confirmedFindings, never regraded. At template line 1390 the conditional spread `...(synth ? { regraded } : {})` is right, but replacing it with an unconditional `regraded,` passes every arm. This is a coverage gap. Behaviour is correct today. | sound |
| 20 | intent | tools/workflows/tier2-review.template.js:728 | medium | - | refuted | I could not show that the SCOPE line causes this refutation, and the finder graded it medium. (1) Fold rounds: renderBrief already narrows a fold round to 'what the previous round's fixes introduced, not the whole build'. A whole-build 'AC has no code' finding is out of a fold round by that design, and round 1 already owns it. (2) A missing listed document: the same skeptic brief carries the INTENT block's explicit line that a missing listed document 'is itself a finding against its path'. That specific instruction sits beside the general SCOPE rule. (3) Specs committed before BASE: an AC the change was meant to implement and does not is a defect the diff introduced, because the claim and the incomplete delivery are both in the range. Reading it as 'unchanged at base' is strained. The worry rests on how an LLM reads the prompt, and no run was shown in which it happened. | unsound |
| 21 | intent | tools/workflows/review_replay.py:10 | medium | medium | confirmed | review_replay.py:10-13 says the known set is ADJUDICATED ITEMS 'not its raw confirmed findings', and README:231 says the same for both paths. But parse_record_findings (appendix branch, ~line 120) takes one item per confirmed appendix row. renderAppendix (tier2-review.template.js:1048-1055) renders `ledger`, which has one entry per RAW finding (built at ~1018 from allFindings), and the synthesis merges raw findings into items separately (template ~1233-1245, TOOL-dMergedTally-1). The liveness check compares rows to the raw `confirmed N` count, so an appendix known set is raw confirmed findings, while a legacy one is items. The stated unit is false on the appendix path, and recall is measured over different units on the two paths. Spec 9 makes the same conflation ('Rows whose verdict column is confirmed are the items'), so the built code matches the spec text but contradicts the F2 resolution and the docstring. The effect is contained to a scorer that decides nothing, so it is medium. | sound |
| 22 | intent | memory/builds/aSightedSkeptic/build/2026-10-01-build-TOOL-aSightedSkeptic-9-1-acceptance-ledger.md:8 | low | low | confirmed | 4c036dc8 appended the AC8 line to the acceptance ledger and left the preamble at lines 8-9, 'AC8, the live replay, is the main loop's and is not evidenced in this record yet.' The commit's diff touches only the tail. Two sentences in one record now disagree, and nothing behaves differently. | sound |
