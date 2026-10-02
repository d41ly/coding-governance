**Serves:** journal TOOL-aSightedSkeptic-1..9

# Spec brief — aSightedSkeptic, all nine units

ONE file for the whole roster on purpose. Nine units edit one script, and M2 requires their specs to
AGREE on scope, interface, ordering and acceptance. Several writers run at once, each holding only its
own group, so every name two units share is pinned HERE and spelled identically in every spec. A spec
that needs a different spelling has found a fork: record it in §8, do not improvise.

Read first: the owner's mandate beside this file (`2026-10-01-prompt-TOOL-aSightedSkeptic-1-0-run-mandate.md`),
then `tools/workflows/tier2-review.template.js` WHOLE (≈960 lines; the `.js` beside it is its render
and differs only in `{{FANOUT_CAP}}`), then `tools/workflows/tier2-review.test.sh`, `tools/hooks/README.md`
(the fan-out grammar), and `memory/guides/REVIEW-PROTOCOL.md`.

## Shared invariants — every spec states the ones it touches, none contradicts one

1. **The source is the template.** Edit `tools/workflows/tier2-review.template.js`; the render
   `tools/workflows/tier2-review.js` is regenerated from it by
   `bash tools/workflows/check-protocol-parity.test.sh --render`, never hand-edited, and both land in the
   same commit. The `review-protocol parity` leg holds them byte-equal after substitution.
2. **Universal.** Nothing names a path into another kit, a memory-tree layout, or `gotchas.py`. A
   project-specific input is an `args` field the CALLER supplies. Its absence is ANNOUNCED — a
   `log('WARNING: …')` line AND a clause in the synthesis prompt's RUN INTEGRITY block — never a silent
   default. (Class: `memory/gotchas/degradation-known-but-unreported.md`.)
3. **A bad value refuses; an absent value defaults.** The harness already refuses a prose `args`, an
   unknown `kind` and a malformed spec subject. Every new field follows that: absent → documented
   default; present but wrong type or outside its closed set → `throw new Error('tier2-review: …')`
   naming the field, the legal set and what was given, BEFORE any agent spawns. A new field is added
   to the `args` header comment in the same commit, and arm (`args header documents every field read`)
   in the self-test must keep passing.
4. **Fan-out.** `tools/hooks/agent-cap.js` is the enforcement point and is NOT edited by this build.
   `DIFF_LENSES` stays an array LITERAL of at most five elements (no trailing-comma miscount risk is
   ours to reintroduce: see `memory/gotchas/trailing-comma-counted-as-an-element.md`), and
   `const LENSES = isSpec ? SPEC_LENSES : DIFF_LENSES // gov:fixed-verifiers` stays the receiver. A
   lens that does not run is skipped INSIDE its thunk, the way lens reuse already is — never by
   `.filter`/`.map` on the receiver (owner memory: agent-cap refuses map/filter chains).
   `MAX_VERIFIERS` and the verify batching are untouched.
5. **The review KEY must change when the review's shape changes.** Today the key is kind, round,
   subject and a print of `context`/`byDesign`/`priorFindings`. A lens file written by the OLD prompts
   under the same inputs would be REUSED by the new harness. Unit 5 adds a literal
   `const REVIEW_SHAPE = 'lenses5-r1'` to the key derivation; every later unit that changes a prompt,
   a schema or the lens set changes NOTHING about it (one bump for the whole build, decided here), and
   every NEW input field (`specs`, `checklist`, `lensNotes`, `intensity`) joins the `inputPrint`
   fingerprint in the unit that adds it.
6. **Lexicon.** Every new function name leads with a verb from `.lexicon.conf`'s `VERBS:` table —
   `build render derive parse check extract measure scan read write` and the rest — and is checked
   with `python tools/lexicon/lexicon.py --suggest <name> --as js.<surface>` before it is written.
7. **Spec kind stays coherent.** `kind: 'spec-audit'` keeps `SPEC_LENSES`. Units 1, 2, 3 (`specs`),
   4, 6 and 8 apply to both kinds; unit 5's new lenses and unit 7's light subset are diff-kind only, and
   their specs say what the spec kind does with the new argument (refuse, or ignore AND announce —
   pick one, §8 if unsure).
8. **No governance carrier is edited**: not `memory/guides/REVIEW-PROTOCOL.md` or its template,
   not the charter template, not `memory/guides/BUILD-METHOD.md` or its template. Where a carrier's
   text would now be incomplete (M8's invocation block does not show the new args), the spec says so
   in §3 Non-goals and the main loop parks it for the owner. The kit's own `tools/workflows/README.md`
   is NOT a carrier and documents the new args.
9. **Version.** The harness version moves ONCE for the build, `1.16` → `1.17`, in the first unit
   built (unit 5), in every carrier `tools/check-kit-versions.sh` pairs (meta `version`, both `gov:kit`
   ids on that line). Later units do not touch it.

## Pinned interface — spell these exactly

| Name | Kind | Owner unit | Meaning |
|---|---|---|---|
| `renderBrief(role)` | function | 1 | the ONE context block every finder AND skeptic prompt opens with: repo, the diff command or the subject list, round, CONTEXT, BY DESIGN, prior findings, and (unit 3) intent. `role` is `'finder'` or `'skeptic'` |
| `args.specs` | string[] of repo-relative paths | 3 | intent documents; rendered into `renderBrief`; the `intent` lens reads them first |
| `args.checklist` | string, or string[] | 4 | the caller's bug-class checklist output. A string is split into ITEMS at lines starting `- ` (continuation lines attach to the item above); an array is already items |
| `CHECKLIST_ITEMS` / per-lens share | derived | 4 | every item is assigned to EXACTLY ONE running lens; each lens's prompt carries its share |
| `DIFF_LENSES` keys | literal | 5 | `security`, `correctness`, `seams`, `verification`, `intent` — five, in that order |
| `args.lensNotes` | object `{<lens key>: string}` | 5 | project addenda appended to that lens's brief; a key naming no lens of the current kind REFUSES |
| `REVIEW_SHAPE` | const string | 5 | see invariant 5 |
| verdict item `fixVerdict` | enum `sound` `unsound` `none` | 2 | the skeptic's judgement of the finding's proposed `fix`; `none` = no fix was proposed |
| verdict item `fixNote` | string | 2 | why unsound, and the corrected fix when the skeptic has one |
| `SEVERITY_RUBRIC` | const string | 6 | one definition of blocker/high/medium/low, interpolated into finder, skeptic and synthesis prompts |
| verdict item `severity` | enum `blocker` `high` `medium` `low` | 6 | the skeptic's grade for a CONFIRMED finding; the harness carries it to synthesis beside the finder's |
| verdict `uncertain` | third member of `verdict` | 6 | counted UNVERIFIED (outstanding), never refuted, never confirmed |
| `args.intensity` | `'full'` \| `'light'`, default `'full'` | 7 | `light` runs the declared light subset; every skipped lens is logged and named in RUN INTEGRITY |
| `LIGHT_LENSES` | literal subset of `DIFF_LENSES` keys | 7 | decided in unit 7's §8 from the evidence below |
| finding field `lens` | string | 8 | every finding carries the key of the lens that raised it, from the merge on |
| return `ledger` | array | 8 | every finding: `id lens ref severity skepticSeverity verdict reason fixVerdict` |
| return `confirmedFindings` | array | 8 | the confirmed set in the shape `priorFindings` reads (`ref`, `claim`, plus `severity`, `fix`) |
| report appendix | markdown table | 8 | `## Appendix — every finding`, one row per ledger entry, refuted ones included with the skeptic's reason; rendered BY THE HARNESS and handed to the synthesis to copy |
| replay scorer | Python tool | 9 | scores a candidate review's appendix against a past record's confirmed set; `--selftest` built in |

`verdict` keeps `confirmed` and `refuted`; `id` stays the only join key (the `review-join ban` leg).
The new verdict fields are OPTIONAL in `VERDICT_SCHEMA`, because a missing one must degrade to
"unjudged" and be COUNTED and announced, never fail a whole batch into regeneration (§8 schema
discipline in the review protocol). Each spec that adds one says how its absence is counted.

## Build order — the `order` verb each spec carries

Every unit edits the same file, so nothing is parallel: `order 1` … `order 9`, one unit per step, in
this sequence: **5, 1, 3, 4, 2, 6, 7, 8, 9** (unit 5 is order 1, unit 1 is order 2, and so on). Why:
the lens set (5) fixes the keys every later unit addresses; the shared brief (1) is what intent (3)
extends; the checklist split (4) needs the final lens set; the two verdict-schema units (2, 6) are
sequential on one schema; intensity (7) changes which lenses run and therefore what (4) splits over —
unit 7's spec MUST state that the split is over the lenses that actually run; the ledger (8) carries
every field the earlier units add; the scorer (9) reads (8)'s appendix.

## Per-unit scope — what each spec must decide

**Unit 1 — skeptic briefing.** Today's verify prompt carries no repo, range, context or by-design list
(`tier2-review.template.js`, the `phase('Verify')` agent prompt). Extract the finder prompt's shared
lines into `renderBrief`, call it from BOTH prompts, and tell the skeptic to refute a finding whose
defect the diff neither introduced nor touched (pre-existing), and anything the BY DESIGN list names.
The resume key needs no change for this unit (invariant 5). Closes nothing filed; note that
`TOOL-aProbedUnit-16` (no scratch root handed to review agents) is ADJACENT and NOT in scope — say so
in §3.

**Unit 2 — fix verification.** The skeptic sees each finding's `fix` and returns `fixVerdict` and
`fixNote`. The synthesis is told which fixes were judged unsound and writes the skeptic's correction,
not the finder's fix, into the report. Decide (§8, M12 candidates): does an `unsound` fix change the
finding's disposition, or only the fix text? Evidence to weigh: 23 of 45 later-round sampled findings
were defects introduced by a previous round's fix (owner analysis, mandate record).

**Unit 3 — finder intent.** `args.specs` reaches every finder and skeptic through `renderBrief`. With
NO `specs`, every diff-kind finder is told to read the range's commit messages
(`git -C <repo> log --format=%B <base>..<head>`) and any spec or design document the diff touches or
those messages name — derivable in every git repo, so it is universal. The `context` default stays,
but a run with neither `context` nor `specs` logs the WARNING invariant 2 requires. For the spec kind,
the subjects ARE the intent: decide whether `specs` is refused, ignored-and-announced, or added as
sibling context.

**Unit 4 — the checklist.** `args.checklist` (pinned above). Today one lens is told to run "the
PROJECT's checklist" and is handed nothing. Each running lens receives its SHARE and is told to sweep
exactly those classes against the diff, reporting only fresh hits. Decide the split by M12, with
candidates differing in MECHANISM — e.g. every lens gets everything and self-selects; a deterministic
partition (round-robin by item order); a keyword routing of item text to lens briefs. Measured on this
tree with `python tools/memory-tree/gotchas.py --for-diff <range>` over 21 past closing ranges: 11 to
88 classes per range, median about 30, scaling with file count (6 files → 17, 444 files → 86). A
property the pick must make testable: every item is swept by at least one running lens, and the run
can say which. No checklist → WARNING + RUN INTEGRITY clause (invariant 2).

**Unit 5 — the lens set.** Owner's pick: five diff lenses `security correctness seams verification
intent`; `regressions` is RETIRED (its job moves to unit 4's split). Briefs, one or two sentences each,
none web-app-specific:
- `security` — trust boundaries for THIS kind of code: commands built from interpolated input (shell,
  SQL, regex, paths), path traversal and symlinks, secrets reaching logs or output, authorization and
  enforcement bypasses, and trusting unvalidated output from another program or agent.
- `correctness` — as today, minus web-specific items.
- `seams` — as today.
- `verification` — does every behaviour this diff changes have a check that can FAIL: a test or gate
  whose fixture never triggers the rule, a predicate that matches nothing, a skip that reads as a
  pass, a changed behaviour with no test at all. The repo's signature class (13–19% of sampled
  findings; `memory/gotchas/fixture-passes-by-finding-nothing.md`).
- `intent` — does the diff do what its specs and commit messages say: an acceptance criterion with no
  code behind it, a stated mechanism that is not the one built, scope beyond what was asked.

Plus `args.lensNotes` and `REVIEW_SHAPE` (pinned above) and the version move (invariant 9). The
`regressions` key must not survive anywhere it would mislead (the meta phase detail says "4 finder
lenses" today).

**Unit 6 — severity.** One `SEVERITY_RUBRIC`, short, defined by CONSEQUENCE not by feeling:
`blocker` = ships a wrong result, a security hole, data loss, or a gate that certifies what it does not
check, on a reachable path; `high` = the same on a narrow or unlikely path, or a defect that will
mislead the next change; `medium` = a real defect with a contained effect; `low` = cosmetic or a
comment. The writer may refine it; it must stay consequence-shaped. The skeptic returns `severity` for
each confirmed finding; decide (§8) which grade the synthesis is bound by when finder and skeptic
disagree, and say how `blockers`/`highs` (which `tier2-review` derives from the synthesis's `items`,
`TOOL-dMergedTally-1`) stay derived over raw confirmed ids. Add `uncertain` to `verdict`, counted
unverified. Decide whether "default to refuted when uncertain" stays for medium/low only.

**Unit 7 — intensity.** `args.intensity`. Decide `LIGHT_LENSES` in §8 from evidence: in the 84-finding
sample, runtime defects 42, could-not-fail checks 16, stale text 12, spec mismatch 6; low precision
(0.13–0.40) clusters on small or already-hardened diffs (dMergedTally, dMendedRecall, dTieredTribunal).
The harness never picks `light` by itself — the caller does — and a light run says so in its report.
For the spec kind, decide refuse vs ignore-and-announce.

**Unit 8 — the ledger.** Today `allFindings` is built by flattening each lens's `findings` without
carrying the lens (`flatMap` over `liveResults`), refuted findings never reach the report, and the
success return carries `confirmed: confirmed.length`. Carry `lens` on every finding into the skeptic
lines, the synthesis lines, the appendix and the return. Return `ledger` and `confirmedFindings` on
EVERY exit path that has findings (the early returns too, where meaningful). The appendix table is
rendered by the harness (it has every value) and the synthesis is told to include it verbatim; decide
in §8 what the harness can and cannot verify about that copy, and state it in the spec's own §7.

**Unit 9 — the replay benchmark.** A stdlib Python tool in `tools/workflows/` (name it by the lexicon
rules; `review_replay.py` is a candidate) that:
- extracts a past diff-review record's CONFIRMED findings (file and line, from its `file:line` refs)
  and its reviewed range, refusing a record whose stated confirmed count it cannot reproduce (a
  liveness assertion: see `memory/gotchas/fixture-passes-by-finding-nothing.md` and the owner memory
  "a zero-guard does not catch some");
- scores a CANDIDATE review's appendix (unit 8) against it: recall = known findings matched / known,
  where a match is the same file and a line within a declared window; prints matched, missed, and
  candidate-only confirmed findings; decides nothing;
- lists replayable records (`--corpus`): diff reviews whose range resolves in this clone;
- carries `--selftest` with inline fixtures, including a fixture that MUST score below 1.0, so the
  scorer is observed able to report a miss.
The LIVE replay — one real `tier2-review` run on a past round-1 range, scored — needs the `Workflow`
tool, which a unit pass does not hold. It is the MAIN LOOP's act at `VERIFYING`; the spec names it as
the acceptance observation and says the main loop records it in the acceptance ledger. Decide in §8
whether the tool also gets a gate leg (and if so how this repo registers one: `tools/gate-legs.json`
and the kit's `kit.toml`), or stays an on-demand tool.

## How §6 Acceptance and §7 Gates are worded here

A pass runs NO suite. The witnesses are:
- per-pass, the direct checks: `node tools/workflows/check-workflow-syntax.js`,
  `bash tools/workflows/check-verifier-fanout.sh`, `bash tools/workflows/check-review-join.sh`, the
  parity render, and for unit 9 its own `--selftest`;
- for behaviour, a NAMED ARM the unit adds to `tools/workflows/tier2-review.test.sh` (stub agents that
  record each prompt and schema already exist there), each arm observed RED against the pre-change
  script before the change lands. §6 names the arm; the suite itself runs ONCE, at `VERIFYING`, by the
  main loop, and the acceptance ledger reads its lines from that run. Write the criterion as "arm
  `<name>` passes; red when <the break>" — never "run the suite".
Backticked paths in §6 must be TRACKED files (`tools/check-spec-tokens.py`); a file a unit creates is
named by basename, unbackticked, or by the command that observes it.

§10 Reuse: run `python tools/codebase-map/reuse_lookup.py "<behaviour phrase>"` and the recall query
for your unit, and record the terms. The review harness is its own seam; say which existing function
or block each change extends.
