# TOOL-aShelvedLeg-3 — unit 2's closing-review minors on the held kit gate, batched

**Status:** DEFERRED · rev-1 · 2026-11-11 · node a · Tier-1 · base c55c8b4e · streams tooling

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-10-build-TOOL-aShelvedLeg-1-agent-ledger.md](../build/2026-11-10-build-TOOL-aShelvedLeg-1-agent-ledger.md) | journal | TOOL-aShelvedLeg-1 TOOL-aShelvedLeg-2 |
| [2026-11-11-prompt-TOOL-aShelvedLeg-3-2-spec-writer.md](../prompts/2026-11-11-prompt-TOOL-aShelvedLeg-3-2-spec-writer.md) | journal | — |
| [2026-11-11-prompt-TOOL-aShelvedLeg-3-brief.md](../prompts/2026-11-11-prompt-TOOL-aShelvedLeg-3-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

The MEDIUM and the LOW that the closing review of TOOL-aShelvedLeg-2 confirmed are fixed in one
batch, as M4 promotes them, and each is left-shifted. The findings are items 1 and 2 of
`2026-11-11-review-TOOL-aShelvedLeg-2-closing-diff-round1`. By the owner's ruling of 2026-11-11,
units 1 and 2 land first and this unit lands later on its own, so it is written DEFERRED.

## 2. Scope (IN)

- **S1** — Every sentence in `tools/unattended/` that says the kit gate, `check-unattended.sh` or
  one of its numbered checks runs on the bar, on every bar or on the merge bar is reworded (review
  item 1, ids 2 and 3). The population is re-derived over every tracked file of the directory, not
  a named-file list, and is the four rows of §4, "The sentence sites". Each reworded sentence keeps
  its argument and says the leg runs when someone runs it, which since TOOL-aShelvedLeg-1 is no
  automatic bar. Where the argument rested on the bar running the leg, the sentence says what bounds
  it now. Observed by AC1, AC2 and AC3.
- **S2** — The route-and-selection sentences of the kit gate are reworded in
  `tools/unattended/README.md`, in the HELD comment of `tools/unattended/kit.toml`, and in the record
  `memory/gotchas/changed-mode-selection-ignores-doc-reads.md` (review item 2, ids 1 and 4). The
  rows are §4, "The changed-mode sites". No sentence says the self-test variable at `changed` selects
  the leg by the kit's shipped sources "only" or "alone", or that a records-only change "leaves it
  held". Each file instead points at the runner's own comment headed
  `THE HELD TIER, SELECTED BY THE KIT WHOSE SHIPPED BYTES MOVED` in `run-gates.sh`, and keeps the
  advice to run the leg with the variable at `1`, or through `--checks`, after a records-only
  change. Observed by AC3 and AC4.
- **S3** — One new `kind: class` record in `memory/gotchas/` for the class the review named new
  (§4, "The new gotcha record"), with `memory/gotchas/INDEX.md` re-rendered by `gotchas.py --write`.
  Observed by AC5 and AC7.
- **S4** — The two existing classes the review placed its other findings in each gain one paragraph
  saying where it bit here, with the check that would have caught it (§4, "The appended
  paragraphs"). Neither paragraph adds an anchor. Observed by AC6.

## 3. Non-goals (OUT)

- Any change to what a script does. Every line this unit changes in a `.sh` or `.toml` file is a
  comment. Refusal messages that say a record "would red the bar" are output, and stay.
- The changed-mode selection itself. Adding `doc_reads` to it in `run-gates.sh` is the deferred
  mechanism fix the record `changed-mode-selection-ignores-doc-reads` already names.
- A gate over `tools/unattended/` for this wording, on the bar or off it. AC1 and AC2 are probes of
  this change. The review's proposed bar leg is handed off below.
- Sentences that use "the bar" as a name for the leg's verdict ("asserted by the BAR", "the bar has
  its own opinion", "would red the bar"). They make no claim about where or how often the leg runs,
  and TOOL-aShelvedLeg-2 kept the same usage, as at `check-unattended.sh:2766`. At
  c55c8b4e, `grep -ciE '\bthe bar\b'` counts 18 such lines in `check-unattended.sh` and 12 in its
  test file.
- Past-tense accounts of a defect found while the leg was on the bar, such as `unattended.sh:4513`,
  `unattended.test.sh:5193` and `VERBS.template.md:95`. They were true when written and stay true.
- `PROTOCOL.template.md:124` ("the bar reds a run commit writing either"), whose check is
  `check-unattended.sh`'s. That template renders into the governance carrier
  `memory/guides/UNATTENDED-PROTOCOL.md`, so it joins TOOL-aShelvedLeg-2's handed-off ask about the
  same file's line 48 rather than this unit (M2, and M3 veto 2).
- The `--help` echo at `run-unattended-gates.sh:421`, which is output.
- Re-deciding the owner-accepted cost at `unattended.sh:2993-2997` (build fork F3, 2026-08-13). S1
  states what bounds it now; whether two bounds suffice is the owner's question.
- The kit version bump, which the lander's `mint` moves.

### Edges

- **consumes-from** `TOOL-aShelvedLeg-2` — the changed-mode sentence its S3 wrote in the kit README
  and the HELD comment, the gotcha record its S6 minted, and its S1 rewording, which this unit
  completes for the files its named-file probes could not reach. Without that unit landed, the
  README and `kit.toml` rows of §4 do not exist and AC4 has nothing to read.
- **hands-off** external — the review's left-shift gate for item 1, a pinned class grep run by a leg
  that is on the bar. It is a new gate and a behaviour change, so the main loop files it as an ask.

## 4. Design

### Evidence

Read at c55c8b4e, the tip after TOOL-aShelvedLeg-2 was built and recorded. Unit 2's sentences and
gotcha record do not exist at the default branch's sha, b904a0f9, so this unit is grounded on the
tip and its header `base` names it, as unit 2's did.

- **Tier.** Tier-1 by the tier rule in `memory/guides/SESSION-KICKOFF.md`, "Tier rule": comments, one
  kit's docs and records, with no contract change and no second kit. Units 1 and 2 are Tier-2.
  Unit 1 changed the descriptor's `subject`, and unit 2 also edited two data files of the run-gates
  kit. This unit does neither.
- **The population is re-derived.** The AC2 probe joins each line of every tracked file in
  `tools/unattended/` with the line before it, strips comment markers, and prints a line where a
  subject (the kit gate, `check-unattended`, a gate leg, "the leg", or a numbered check) is
  followed in the same sentence by "on the bar", "every bar" or merge-bar wording. At c55c8b4e it
  prints 12 lines. Four are S1's sites and eight are kept, in the table below. The brief named two
  sites; the probe found two more, `lib-unattended.sh:441` and `unattended.sh:892`, whose subject
  sits on the line above, so a line grep cannot see them.
- **Whose checks.** `lib-unattended.sh:2389` is about check 2, whose caller is
  `check-unattended.sh:1206`. `unattended.sh:2997` is about check 9, whose `fail 9` sites start at
  `check-unattended.sh:2600`. `lib-unattended.sh:438-442` is about the `ceiling_max` comparison and
  `unattended.sh:888-892` about `scan_shared_index_overlaps`. Within this kit, both are read by
  `check-unattended.sh` and by no other leg's script.
- **The runner's rule.** `run-gates.sh:3070-3091` is the comment that owns changed-mode selection.
  It runs a held leg with no, unreadable, non-ancestor or foreign last-run record, one more than
  `GATE_SELFTESTS_MAX_LAG` first-parent commits behind HEAD (10 at `:3094`), or a changed path in its
  selection set. `run-gates.sh:3250` holds a leg only while `GATE_SELFTESTS` is empty, or `changed`
  with the leg found unchanged, so any other non-empty value runs it. The heading text
  `THE HELD TIER, SELECTED BY` occurs once in the file (`:3070`); the shorter `THE HELD TIER` also
  matches `:389`.
- **The neighbour sentence.** The README's "runs only through `--checks` or a bar run with
  `GATE_SELFTESTS=1`" (`README.md:423-424`) and the HELD comment's "by either route" (`kit.toml:262`)
  state the same rule with the `changed` arm left out, one sentence before the changed-mode sentence.
  Rewording one without the other is `amendment-leaves-its-other-half-standing`, so S2 takes both.
- **No bare CR.** A byte read at c55c8b4e finds no CR in `lib-unattended.sh`, `unattended.sh`,
  `README.md` or `kit.toml`. `check-unattended.sh`, which carries four, is not touched.
- **Anchors.** `gotchas.py` derives a record's anchors from every backticked token carrying a `/` or
  a listed extension, `.md` and `.toml` among them (`ANCHOR_RE`, `gotchas.py:65`). The index's third
  column is that count: 3 for `criterion-asserts-what-its-own-command-cannot-show` and 14 for
  `amendment-leaves-its-other-half-standing` at c55c8b4e.

### The sentence sites

Line numbers at c55c8b4e. The builder re-derives them with the AC2 probe.

| File | Lines | Says now | Reword as |
|---|---|---|---|
| `lib-unattended.sh` | 440-442 | "it grades the same declaration on the bar, before any run reaches it" | it grades the same declaration whenever the kit gate runs, which no automatic bar does since TOOL-aShelvedLeg-1, so it reaches a declaration before a run does only when someone runs it |
| `lib-unattended.sh` | 2388-2390 | "It exists because check 2 runs on every bar" | because check 2 walks every build each time the kit gate runs |
| `unattended.sh` | 890-892 | "so a conf no run has read yet is refused on the bar too" | so the kit gate refuses a conf no run has read yet too, whenever it runs |
| `unattended.sh` | 2993-2997 | "Three things bound it and none removes it ... And leg check 9 asserts the same facts independently on the bar." | two things bound it on every run and a third whenever the kit gate runs, and none removes it; leg check 9 asserts the same facts independently when it runs, which no automatic bar does since TOOL-aShelvedLeg-1, so a run nobody checks that way has the first two alone |

The "Reword as" column is guidance, not required text. The rules are: the sentence stays true, it
keeps its argument, and it spells nothing the AC1 and AC2 patterns read. It names no route list with
"only", which would be the class S3 records.

### The kept sites

| Site | Why it stays |
|---|---|
| `VERBS.template.md:95` | past tense: the plan verb's launch cost "was" the largest item on the bar's longest leg |
| `adopt-unattended.sh:937` | the `unattended skill wiring` leg, `subject = "repo"`, which is on the bar |
| `check-playbook.sh:515`, `:615` | the playbook validity gate, `subject = "repo"` |
| `tools/unattended/fixture-pieces/one/piece.md:4` | the playbook leg's piece population, read by `check-playbook.test.sh` |
| `unattended.sh:12150` | a general rule, "a check that cannot run where the bar runs does not belong on the bar", which stays true of any leg |
| `unattended.test.sh:15225`, `:15434` | a fixture's expected backlog line about any red merge-bar leg |

### The changed-mode sites

| File | Lines | Says now | Reword as |
|---|---|---|---|
| `tools/unattended/README.md` | 423-426 | "runs only through ... or a bar run with `GATE_SELFTESTS=1`. `GATE_SELFTESTS=changed` selects it by this kit's shipped sources only ... leaves it held" | it runs when asked, through `--checks` or a bar run with `GATE_SELFTESTS` set; at `changed` the runner decides by the arms its comment headed `THE HELD TIER, SELECTED BY THE KIT WHOSE SHIPPED BYTES MOVED` in `run-gates.sh`, under the kit prefix, lists, and the records its `doc_reads` names are not among them, so a change that moves only those records does not by itself select it |
| `tools/unattended/kit.toml` | 261-265 | "by either route: ... GATE_SELFTESTS=changed selects it by this kit's shipped sources only ... leaves it held" | the same, as a comment, naming `run-gates.sh` |
| the gotcha record | 3 | description: "selected under changed mode by its kit's shipped sources alone, so ... leaves it held" | never selected under changed mode by the records it reads, so a change that moves only those records does not by itself run it |
| the gotcha record | 13-17 | Symptom: "selects a held leg under that mode by its owning kit's shipped sources plus its suite file" | selects a held leg by the arms the runner's comment of that heading lists, and a leg's `doc_reads` are not one of them |
| the gotcha record | 23 | "A records-only change leaves it held under changed mode." | a records-only change does not by itself select it under changed mode |

Both files keep the closing advice: run it with the variable at `1`, or through `--checks`, after
such a change. The gotcha's "reads green" stays, because a held leg prints `GATE held` and does not
fail the bar (review item 2). The record's name stays. `memory/gotchas/INDEX.md` carries the
description, so it is re-rendered.

### The new gotcha record

Front matter at column 0 (`name`, `description`, `kind: class`, `universal: false`), then
`## Symptom`, `## Where it bit`, `## The fix`, `## Gate` and `## Related`. The `## Gate` section
opens with "There is no machine gate for this", which `DECLARES_RE` reads, and says why: no checker
can tell a paraphrase of a rule from a statement of it.

| Name | Class | Anchors | Where it bit |
|---|---|---|---|
| `restated-rule-drops-its-other-arms` | prose restates when a runner selects, holds or skips something, keeps one arm of the rule and narrows it with "only" or "alone", so a reader acts on an arm the code does not have | `tools/run-gates/run-gates.sh`, `tools/unattended/README.md`, `tools/unattended/kit.toml` | TOOL-aShelvedLeg-2's closing review, item 2: the changed-mode sentence left out the record and lag arms |

The fix it states: point at the comment that owns the rule, by its heading text, and say only what
the reader must do differently. Check 27 at `NEAR_MATCH_GATE="red:0.125"` asks a new record to name
its nearest older record. Its `## Related` names `changed-mode-selection-ignores-doc-reads` and
`two-answers-to-one-question` with `coexists-with`, and any further hit the relation probe in AC7
prints.

### The appended paragraphs

Each paragraph names the review record by its stem, without backticks, and carries no backticked
token with a `/` or a listed extension, so neither record's anchor set moves.

| Record | Section | What it adds |
|---|---|---|
| `criterion-asserts-what-its-own-command-cannot-show` | `## Where it bit`, and one line under `## The fix` | TOOL-aShelvedLeg-2's S1 claimed every sentence of the kit's scripts, and its probes read four named files, so the fifth file kept the sentence. The fix line: a criterion that claims every X in a scope reads the whole scope by glob or by `git ls-files`, never a list of named files. |
| `amendment-leaves-its-other-half-standing` | `## Where it bit` | TOOL-aShelvedLeg-1 moved where the kit gate runs, and two comments in the kit's library and driver kept resting an argument on the old placement. The check, at the close: after a change of where a leg runs, grep every file of its kit for a sentence that rests on the old placement. |

The symptom list of the first record is not touched, because its opening sentence types the list's
size.

### Rollout

The status flips from DEFERRED to INPROGRESS when the owner releases the unit, after units 1 and 2
have landed. The builder records the tip it starts from as `PRE` in the acceptance ledger, because
AC3 diffs from it.

### Inventory

Minted: the gotcha name `restated-rule-drops-its-other-arms`. No lexicon cell in this repo grades a
gotcha name; hygiene checks 17 to 19, 27 and 28 grade the record. No other identifier is minted.

### Files touched (estimate)

- `tools/unattended/lib-unattended.sh`
- `tools/unattended/unattended.sh`
- `tools/unattended/README.md`
- `tools/unattended/kit.toml`
- `memory/gotchas/`
- `memory/gotchas/INDEX.md`

### Alternatives rejected

- **Only the two lines the brief named.** The probe found two more of the same claim in the same two
  files, and the review graded the instance-only fix INSTANCE-ONLY.
- **Rewording every "the bar" in the kit.** It used the bar as a name for the leg's verdict, not a
  claim about where it runs, and the closed unit 2 kept that usage. It would touch about thirty
  lines of `check-unattended.sh` and its test, which carries four bare CR bytes.
- **Restating every arm of the selection in the README and the descriptor.** That is a third copy of
  a rule `run-gates.sh` owns, and it would go stale the next time the runner gains an arm. The
  brief asks for a pointer.
- **A new record only, leaving the two existing classes as they are.** The goal asks for each
  finding to be left-shifted, and the review's left-shift for item 1 is a checklist line on an
  existing class. A new record for either would restate a class that exists.

## 5. Production-readiness checklist

- security — N/A: comments, one kit's docs and records; no input, write path or surface.
- perf / scale — N/A: no code path changes.
- error / empty / loading states — N/A: no code path changes.
- observability — N/A: no output changes.
- risks — a comment edit in a `.sh` file could disturb a heredoc or a quoted literal; AC3 observes
  that only comment lines moved.
- testing — AC1 to AC7, all probes of the changed files. The close's bar re-observes S3 and S4
  through `memory hygiene`.
- migration — N/A: an adopter takes the reworded kit files at its next `govkit update`.
- user docs — the kit README's "Running the kit's own checks" paragraph is S2. No page under
  `help/` names this leg or changed mode (`grep -rlE 'GATE_SELFTESTS|unattended kit gate' help/`
  prints nothing at c55c8b4e).

## 6. Acceptance criteria

- **AC1** — When
  `grep -rnE '(check-unattended|(leg )?check [0-9]+|kit gate|gate leg)[^.]*(\b(on the|every) bar|merge[- ]bar)' tools/unattended/`
  runs, it prints nothing.
  Red when: `lib-unattended.sh:2389` or `unattended.sh:2997` keeps its wording, or a rewording
  spells "on the bar", "every bar" or merge-bar wording after its subject. At c55c8b4e it prints
  exactly those two lines.
  figure: two lines is PINNED at c55c8b4e.
- **AC2** — When the probe below runs from the repository root over every file `git ls-files`
  lists under `tools/unattended/`, it prints exactly the eight sites of §4, "The kept sites", and
  none of the four sites of "The sentence sites". Line numbers in `unattended.sh` may move by the
  reworded sentences' wrap; the files and the sentences are what is compared.
  ```
  python - <<'EOF'
  import re, subprocess
  S = r'(check-unattended|gate leg|kit gate|\bleg check \d+|\bcheck \d+\b|\bthe leg\b|\bthis leg\b)'
  B = r'(\bon the bar\b|\bevery bar\b|merge[- ]bar)'
  pat = re.compile(S + r'(?:(?!\. ).)*?' + B, re.I)
  strip = lambda s: re.sub(r'^\s*(#|\*|//)+\s*(-{4}\s*)?', '', s).strip()
  for f in subprocess.run(['git', 'ls-files', 'tools/unattended'], capture_output=True, text=True).stdout.split():
      L = open(f, encoding='utf-8', errors='replace', newline='').read().split('\n')
      for i in range(len(L)):
          a = strip(L[i - 1]) if i else ''
          j = a + ' ' + strip(L[i])
          if any(m.end() > len(a) + 1 for m in pat.finditer(j)):
              print(f'{f}:{i + 1}')
  EOF
  ```
  Red when: any of `lib-unattended.sh:441`, `:2389`, `unattended.sh:892` or `:2997` keeps its claim,
  including across a line break, or a rewording adds a new hit. At c55c8b4e it prints 12 lines: the
  eight kept sites and the four sentence sites.
  figure: 12 and 8 are PINNED at c55c8b4e; run verbatim before this spec's commit.
- **AC3** — When the probe below lists every changed line of the three edited code files that is not
  a comment, it prints nothing, where `PRE` is the tip the build pass started from, recorded in the
  acceptance ledger:
  ```
  git diff -U0 "$PRE" -- tools/unattended/lib-unattended.sh tools/unattended/unattended.sh tools/unattended/kit.toml | grep -E '^[-+][^-+]' | grep -vE '^[-+][[:space:]]*#'
  ```
  Red when: a code line, heredoc, quoted literal or TOML key in those files moved.
- **AC4** — When the probe below joins each of the three S2 files into one line, with comment markers
  stripped, it prints `0` for the narrowing phrases and at least `1` for the pointer in each file.
  The last line counts the heading in the runner and prints `1`, so the pointer names a live comment:
  ```
  for f in tools/unattended/README.md tools/unattended/kit.toml memory/gotchas/changed-mode-selection-ignores-doc-reads.md; do
    t=$(sed 's/^#[[:space:]]*//' "$f" | tr '\n' ' ')
    printf '%s %s %s\n' "$f" "$(printf '%s' "$t" | grep -oE 'shipped sources (only|alone)|leaves it held|runs only through|by either route' | wc -l)" "$(printf '%s' "$t" | grep -oE 'THE HELD TIER, SELECTED BY' | wc -l)"
  done
  grep -c 'THE HELD TIER, SELECTED BY' tools/run-gates/run-gates.sh
  ```
  Red when: any of the three files still narrows the selection with "only" or "alone", still says a
  records-only change leaves the leg held, or keeps the two-route sentence; or a file restates the
  rule without pointing at the runner's comment. At c55c8b4e the first counts are 3, 3 and 3 and the
  second are 0, 0 and 0.
  figure: PINNED at c55c8b4e.
- **AC5** — When `python tools/memory-tree/gotchas.py --check` runs after S3's record and the
  re-rendered `memory/gotchas/INDEX.md` are committed, it exits 0. The index lists the new name on
  one row, and the record's body satisfies `--declares`:
  ```
  grep -c 'restated-rule-drops-its-other-arms' memory/gotchas/INDEX.md
  python tools/memory-tree/gotchas.py --declares < memory/gotchas/restated-rule-drops-its-other-arms.md
  ```
  The grep prints 1 and `--declares` prints `declares: yes`.
  Red when: the record is missing, its `## Gate` section says nothing `DECLARES_RE` reads, it
  derives no anchor, or the index was not re-rendered (check 17 names it stale).
  cost: about two minutes for `--check` on node a, measured 2026-11-10 by unit 2.
- **AC6** — When the probes below read the two existing class records and the re-rendered index,
  each record carries the build's name, and the index's anchor column still reads 3 and 14:
  ```
  grep -c 'aShelvedLeg' memory/gotchas/criterion-asserts-what-its-own-command-cannot-show.md memory/gotchas/amendment-leaves-its-other-half-standing.md
  grep -E '^\| \[(criterion-asserts-what-its-own-command-cannot-show|amendment-leaves-its-other-half-standing)\]' memory/gotchas/INDEX.md | cut -d'|' -f2,4
  ```
  The first prints at least 1 per file. The second prints `14` beside
  `amendment-leaves-its-other-half-standing` and `3` beside
  `criterion-asserts-what-its-own-command-cannot-show`.
  Red when: a paragraph is missing, or it carries a backticked path or file name and so moves the
  record's anchor set and what `--for-paths` selects it on. At c55c8b4e the first prints 0 and 0.
  figure: 3 and 14 are PINNED at c55c8b4e.
- **AC7** — When `python tools/memory-tree/row_grammar.py --check-relations` runs after S3's record
  is committed, it prints no near-match hit naming `restated-rule-drops-its-other-arms` that the
  record's `## Related` section does not name.
  Red when: the record restates an older record above the floor and names no relation to it.
  permission: checks 27 and 28 are graded at the close by the `memory hygiene` leg; this probe is
  the pass's view of check 27.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `docs` · `kit version markers` · `kit epoch (shipped bytes move, the version moves)` · `verdict epoch (kit version dates the engine)` · `lexicon naming predicates` · `routed commits name a specced unit` · `brief-recorded` · `routed-commits selftest` · `tier2-review self-test` · `policy fixtures` · `recall floor` · `recall floor arms`

`routed-commits selftest` guards `tools/unattended/lib-unattended.sh`, `tier2-review self-test`
guards `tools/unattended/unattended.sh`, `policy fixtures` guards `tools/unattended/kit.toml`, and
`recall floor` and `recall floor arms` guard `memory/`. Those five are held or guarded on a default
bar, and the close runs them only if it asks for the held tier. The kit epoch and version legs
expect the lander's `mint`. The full bar runs at the lander.

No new arm: the unit adds and moves no suite arm. Each criterion is a probe of the changed files.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-11 · initial draft.

## 10. Reuse audit

The seams are wording and records that already exist, since this unit changes prose. S1 reuses the
held-leg wording TOOL-aShelvedLeg-2 wrote, "held off every automatic bar by the 2026-11-10 ruling",
at `check-unattended.sh:2-3`. S2 points at the comment `run-gates.sh:3070` owns instead of copying
it. S3 and S4 reuse the gotchas catalogue and its renderer, `gotchas.py --write`. The hold itself is
run-gates' existing one, `subject = "kit"` or `chunk = "selftests"`, released by `GATE_SELFTESTS`,
and nothing here changes it. `python tools/codebase-map/reuse_lookup.py "prose restates when a
runner selects or holds a leg and drops the other selection arms"` returned only name-stem
neighbours (`legs`, `arm`, `leg`, `prose`), and none of them governs comment wording; for prose, no
existing seam fits beyond the wording cited above. `gotchas.py --for-paths` over the estimate
selected `changed-mode-selection-ignores-doc-reads`, which S2 corrects, and
`two-answers-to-one-question`, which the new record relates to.

Recall returned the review record and the unit 3 brief, unit 2's evidence that `run-gates.sh:3070`
states the selection set, and TOOL-dThriftyLanding-13's doc-only push rule, which keeps a lag bound
too. No record names a class for a paraphrase that narrows a rule, so the new record restates none.

Recall terms used: `python tools/memory-recall/query.py "how is a doc sentence that restates a
runner's selection rule narrower than the code found and corrected" --terms "restated rule changed
mode GATE_SELFTESTS held leg selection arms lag bound only alone every bar kit gate"`
