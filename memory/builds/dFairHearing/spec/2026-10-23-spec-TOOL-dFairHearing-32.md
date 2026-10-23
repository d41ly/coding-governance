# TOOL-dFairHearing-32 — the round-3 spec audit's 32 minors: criteria that observe what their specs change, one source per procedure, and refusals that name their cause

**Status:** OPEN · rev-1 · 2026-10-23 · node d · Tier-2 · base 3708a705 · streams tooling · order 23 · advances TOOL-dFairHearing-19

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dFairHearing-32-deviation-321.md](../build/2026-10-23-build-TOOL-dFairHearing-32-deviation-321.md) | deviation | — |
| [2026-10-23-prompt-TOOL-dFairHearing-28-promoted-fix-brief.md](../prompts/2026-10-23-prompt-TOOL-dFairHearing-28-promoted-fix-brief.md) | research | TOOL-dFairHearing-28 TOOL-dFairHearing-29 TOOL-dFairHearing-30 TOOL-dFairHearing-31 |
| [2026-10-23-prompt-TOOL-dFairHearing-32-1-spec-writer.md](../prompts/2026-10-23-prompt-TOOL-dFairHearing-32-1-spec-writer.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

One batch unit closes every MEDIUM and LOW finding that the round-3 spec audit confirmed
(`memory/builds/dFairHearing/reviews/2026-10-23-review-TOOL-dFairHearing-4-14-25-27-spec-audit.md`).
That is 32 report ids: 21 MEDIUM, items M1 to M14, and 11 LOW, items L1 to L9. Each id is its own §2
item. MEDIUM ids: 2, 3, 5, 6, 7, 12, 13, 14, 17, 20, 23, 24, 25, 26, 30, 31, 32, 33, 35, 36 and 37. LOW
ids: 4, 8, 9, 10, 15, 16, 19, 21, 27, 29 and 38. The minors land on four units, `TOOL-dFairHearing-4`,
`-14`, `-25` and `-27`, so this unit builds after every unit of the build. It makes each corrected
statement true on the code those units built, gives each refusal its named cause, and observes what
each criterion's spec claimed to change. A criterion this unit supersedes is named by the hands-off
bullet in that unit's §3, and that unit's acceptance ledger records it superseded here
(`TOOL-dFairHearing-23` §8 F7's form).

## 2. Scope (IN)

Each item names its report id, its report item, the unit it lands on and the criterion that observes
it. Where a report item merges ids, each id is its own item, and the later ids point at the first
one's mechanism.

- **S1** — id 2 (M1, unit 4, AC1). The resume probe's instruction at
  `tools/workflows/tier2-review.template.js:1021` and its render names `find-<lens>.json or
  verify-batch-<n>.json`, and no carrier under `tools/` or `memory/guides/` spells `verify-<a>-<b>`. A
  stub-run arm captures the `resume:probe` prompt and asserts that it names `verify-batch-<n>.json`.
  This supersedes unit 4 AC8's two absence patterns and adds a prompt half to its AC6.
- **S2** — id 14 (M1, unit 4, AC1). S1's defect from the grounding lens; S1 closes it.
- **S3** — id 23 (M1, unit 4, AC1). S1's defect from the blast-radius lens; S1 closes it.
- **S4** — id 33 (M1, unit 4, AC1). S1's defect from the failure-envelope lens; S1 closes it.
- **S5** — id 32 (M12, unit 4, AC2). `deriveAddressKey`'s spec-kind section class is `section ?<n>`
  or `§ ?<n>`, matched ignoring case, both normalised to `§<n>`. The spec-audit reports write `§4`
  16139 times and `Section <n>` 197 times, the audit's measurement of 2026-10-23, PINNED. This
  supersedes unit 4 §4's "`section <n>` or `§ <n>`".
- **S6** — id 15 (L5, unit 4, AC3). The key differs from the instrument's `loc` in three named places:
  a token must stand as a whole word, an unaddressed finding falls to its lens, and every section form
  is normalised to `§<n>`, where the instrument keys `t.group(1).lower()` unnormalised
  (`memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-research-review-adjudication-instruments.md:1664-1665`).
  The comment above `deriveAddressKey` names all three, so a replay rate unlike 541 of 924 is read as
  a key change. This supersedes unit 4 §4's "two named places".
- **S7** — id 10 (L4, unit 4, AC4). Unit 4 §3's scorer non-goal reads as spec 12 F5 resolved it. The
  two readers agree on `[tag]` and `§<n>`. `tools/workflows/review_replay.py` keeps the S, AC and F
  item-to-section mapping (:100-115) and the suffix path match for scoring. The batch key keeps the
  item token. The `batchBy` verdict's same-batch rate comes from `deriveAddressOrder` and
  `checkSameAddress`, never from the scorer's matcher. Neither reader changes. This supersedes "written
  to agree with S1 field for field".
- **S8** — id 19 (L4, unit 4, AC4). S7's defect from the reuse lens; S7 closes it.
- **S9** — id 6 (M4, unit 14, AC5). Unit 14's arms raise `ARMS_DECLARED` in
  `tools/workflows/replay_scorer.py`'s runner by the number of arms added, as
  `tools/workflows/review_replay.py:84` and `:604-606` hold it. This supersedes the floor field `none`
  on unit 14's `New arm:` line.
- **S10** — id 25 (M4, unit 14, AC5). S9's defect from the blast-radius lens; S9 closes it.
- **S11** — id 7 (M5, unit 14, AC6). The `review-replay` instance's `case_evidence(case)` reads a
  run-case in unit 23 S4's terms: the case's subject record at a pinned blob, and a known set whose
  every row carries an address and a source record (spec 1 S2's reading). A case missing either is
  refused by id. This supersedes unit 14 S2's "the known item's ref and the record it came from".
- **S12** — id 36 (M14, unit 14, AC7). `check_experiment` validates the manifest's references. Arm
  names are unique. Every `base` names another declared arm, and the base graph has no cycle. Every
  `union` member is a declared arm. Each violation exits 2 naming the arm, never a traceback. This adds
  to unit 14 S1's rule list.
- **S13** — id 4 (L1, unit 25, AC8). The `selected` half of unit 25's AC6, which
  `TOOL-dFairHearing-30` AC4 answers, is observed by behaviour. Over a fixture catalogue holding an
  ungated class outside the range's selection, `gotchas.py --for-diff <range> --all-ungated` prints
  output byte-identical to `gotchas.py --for-diff <range>`. This supersedes the `grep -c --
  "--all-ungated"` count, which a docstring recording unit 23 S21's contract reds.
- **S14** — id 5 (M3, unit 25, AC9). Each replay verdict record, unit 25's and unit 30's, names the
  orchestrating commit: this repository's `HEAD` whose recipe, harness and scorer drove the runs,
  distinct from each clone's `HEAD`, which the record names separately. That commit is bound by
  evidence the writer does not choose: it is the first parent of the commit that adds the record, it
  descends from unit 23's build commit, and the record names the blobs of `tools/workflows/README.md`,
  `tools/workflows/tier2-review.js` and `tools/workflows/replay_scorer.py` at it. This pass appends
  what a record lacks, derived from git. This supersedes unit 25 S6's "the commit the runs started
  from", §4's "Each run starts from a commit that descends from unit 23's build commit" and AC7's
  ancestry test.
- **S15** — id 13 (M3, unit 25, AC9). S14's defect from the grounding lens; S14 closes it.
- **S16** — id 9 (L3, unit 25). Unit 25 reads `check_experiment` (unit 14), `DESIGN_RECORD_PRESET`
  (unit 3) and `spec-audit-optin.js` (unit 16) without an edge. Each read is declared by the unit that
  reads it after this audit: `TOOL-dFairHearing-30`, which now carries unit 15's manifest, consumes
  from unit 14, and this unit consumes from unit 3 (S19) and unit 16 (S25). Spec 25 itself takes no new
  consumes-from edge, because adding one there would fold this finding into the spec it was raised on,
  which M4 refuses. NOT OBSERVED by a criterion: an edge is a declaration that hygiene check 12's
  parity arm reads, and no product file changes.
- **S17** — id 21 (L6, unit 25, AC10). One source for the clone envelope. The replay section of
  `tools/workflows/README.md`, with unit 27 S22's EXIT trap, is the procedure every later replay runs,
  and unit 25 §4's restated block is superseded by it. For the runs units 25 and 30 already made, AC10
  observes the residue in this repository.
- **S18** — id 31 (M11, unit 25, AC10). The README's replay section gains the placement step: a
  commit the source history lacks is made by `git commit-tree` over a tree written through a temporary
  `GIT_INDEX_FILE`, referenced only by a transient ref, which the EXIT trap clears with `git update-ref
  -d`. The working tree, the index and `HEAD` of the orchestrating repository never move. This
  supersedes unit 25 §4's "made on a transient branch" and §5's claim that id 36 is covered by the
  exact-commit check.
- **S19** — id 24 (M8, unit 25, AC11). Spec 3's AC7 arm in `tools/workflows/tier2-review.test.sh`
  reads its expected no-flag preset from `DESIGN_RECORD_PRESET` in `tools/workflows/review_pin.py` at
  run time, never the literal `unit-spec`, so it holds under either replay-1 verdict. Any arm pinning
  spec 15 S1's command text is checked the same way against unit 30's decision.
- **S20** — id 29 (L7, unit 25, AC12). A re-run takes a new clone named per attempt: `fhr<run><a>`,
  `<a>` the attempt letter from `a`, for replay 1, and unit 30's `f<r><a><n>` for unit 15's replay. A
  voided clone stays until the record cites it. A run takes at most two attempts. After a second void,
  replay 1 is recorded as not run and spec 1 S9's R-1 ask is filed. This supersedes unit 25 S1's fixed
  names `fhr1` and `fhr2` and S3's unbounded re-run.
- **S21** — id 30 (M10, unit 25, AC12). One rule for a dead run in unit 15's replay: spec 1's void and
  re-run rule applies, with S20's cap, and the count `paired 4 of 4` stands. A record still void after
  its cap ends the replay with no decision taken and no product file of spec 15 S6 changed. This
  supersedes unit 25 S4's "pairs over the records both arms answered".
- **S22** — id 3 (M2, unit 27, AC13). Unit 27 AC11's and AC9's absence checks read the two `.js` files,
  `tools/hooks/agent-cap.js` and `tools/workflows/check-verifier-fanout.js`, through `renderBlankedView`
  (`tools/hooks/agent-cap.js:1303`), the view with string, template and comment contents blanked.
  `tools/check-playbook-parity.sh`, its suite and both REVIEW-PROTOCOL copies keep the whole-text grep,
  where `MAX_LENSES` sits in `sed` and `printf` strings or in prose S16 rewrites. AC9's shell half reads
  assignment lines only. This supersedes the whole-text `.js` halves of AC11 and AC9.
- **S23** — id 8 (L2, unit 27, AC14). Unit 27 S28 is restated: the path limit holds for a clone
  without `core.longpaths`, which is the default for a fresh clone here, since this worktree's `true`
  sits only in its `config.worktree`. Fixtures go under `%TEMP%`. Spec 14 AC2's fixture line
  (:189-190) joins S28's list. Unit 27 AC23, which no tree can turn red, is superseded by AC14.
- **S24** — id 16 (L2, unit 27, AC14). S23's defect from the grounding lens; S23 closes it.
- **S25** — id 12 (M6, unit 27, AC15). `checkOptinPackPresent` ports `tools/lib/resolve_kit_dir.py` as
  its contract, rung for rung. A receipt row whose path is missing or escapes the tree is skipped, a
  `rendered` row joins, and the probes are `<here>/<home>/<anchor>` then `<here>/../<home>/<anchor>`.
  It denies only on the resolver's own refusal, naming the three places looked. One function,
  `resolveKitDir(home, anchor, here)`, between `// >>> resolveKitDir` and `// <<< resolveKitDir` in
  `tools/hooks/agent-cap.js`, serves both `resolveHarnessName` (:112-116) and `checkOptinPackPresent`.
  This supersedes unit 27 S20's deny on a missing-path row and AC15's third case.
- **S26** — id 17 (M6, unit 27, AC16). The port is held to the canonical: a behaviour arm in
  `tools/lib/resolve-python.test.sh`, shaped as its `{prefix}` contract arm (2b), runs
  `resolve_kit_dir.py` and the JS port sliced between its markers over one truth table and requires
  one answer per row.
- **S27** — id 37 (M6, unit 27, AC15). S25's defect from the failure-envelope lens; S25 closes it.
- **S28** — id 20 (M7, unit 27). The check's baseline is the merge bar's, `GATE_BASE` else the
  merge-base with the remote ladder's default branch, never local `main`. `TOOL-dFairHearing-31` S1
  takes exactly that base, so this item adds no second mechanism. NOT OBSERVED here: unit 31's AC1 and
  AC2 observe it.
- **S29** — id 26 (M9, unit 27, AC17). `tools/check-playbook-parity.sh` resolves the owned side of the
  `lens-array bound` pair through `resolve_kit_dir "$_pp_py" workflows check-verifier-fanout.js
  "$_self_dir"`, falling back to `<no workflows kit>` as `HK_DIR` does (:141-148). `fixture()` in
  `tools/check-playbook-parity.test.sh` plants `${FX}workflows/check-verifier-fanout.js` holding `const
  LENS_SLOTS = 5`, declares it as an `[[entry]]` in the fixture registry and waives it in the fixture's
  `playbook-kit-waivers.txt`, so the valid-fixture control stays green. The drift arm (:279-281)
  re-points at that file.
- **S30** — id 27 (L8, unit 27, AC18). Unit 27 §5 says the coupling is transitive. review-harness is
  already coupled to drift-audit (`tools/drift-audit/kit.toml:13`), and govkit closes a scoped update
  over coupled kits the receipt claims (`tools/govkit/govkit.py:1050-1059`, `:9311`). So a scoped
  agent-cap or review-harness update also moves drift-audit when the receipt claims it. This
  supersedes unit 27 AC7's two-kit fixture.
- **S31** — id 35 (M13, unit 27, AC19). `check_held_out_frozen` runs `git ls-files --full-name
  --literal-pathspecs -- <path>` and requires exactly one output line, equal to the path's own
  repo-relative POSIX form. Otherwise it exits 2 naming the path and the line count. This supersedes
  unit 27 S7's empty-output case as the only one handled.
- **S32** — id 38 (L9, unit 27, AC20). `check_ungated`'s sentence end is a full stop, optionally
  followed by closing `*`, `_`, `)` or a backtick, then whitespace or the paragraph's end. This
  supersedes unit 27 S11's "a full stop followed by whitespace or the end of the paragraph".

## 3. Non-goals (OUT)

- No re-review, and no fold into the specs of units 4, 14, 25 and 27: each item makes the corrected
  statement true and reopens no severity.
- No BLOCKER or HIGH finding: ids 11, 1, 28 and 34 are `TOOL-dFairHearing-28`, `-29`, `-30` and `-31`.
- No re-run of a replay. S14, S17, S20 and S21 read the records the runs left and complete them from
  git; a void record that ends a replay is recorded, never re-run here.
- No new gate leg: every arm lands in a suite that exists or that an earlier unit adds.
- No govkit code change: S30 corrects a stated blast radius and a fixture.
- No help page: `help/` covers neither the review harness, the scorer factory nor the hooks.

### Edges

- **consumes-from** `TOOL-dFairHearing-4` — `deriveAddressKey`, the resume probe's instruction and the verify file name, which S1 to S8 correct
- **consumes-from** `TOOL-dFairHearing-14` — `check_experiment`, `case_evidence` and the runner arms, which S9 to S12 correct
- **consumes-from** `TOOL-dFairHearing-25` — replay 1's verdict record and its clone and placement procedure, which S13 to S21 correct
- **consumes-from** `TOOL-dFairHearing-27` — S7, S11, S15, S16, S20, AC7, AC9, AC11 and AC23, which S22 to S32 correct
- **consumes-from** `TOOL-dFairHearing-30` — unit 15's replay verdict record and its clones, which S13, S14, S20 and S21 read
- **consumes-from** `TOOL-dFairHearing-31` — the bar's baseline for the version check, which S28 names in place of a second mechanism
- **consumes-from** `TOOL-dFairHearing-3` — `DESIGN_RECORD_PRESET` and its AC7 arm, which S19 re-pins to the constant
- **consumes-from** `TOOL-dFairHearing-16` — the opt-in pack, `spec-audit-optin.js`, whose home S25's resolver finds

## 4. Design

### Why one unit and not two

The minors land on four specs, and no split of them yields two write sets disjoint by M6's clauses.
S9 to S12 and S31 all write `tools/workflows/replay_scorer.py`. S1, S5 and S19 all write
`tools/workflows/tier2-review.test.sh`. S13 reads `tools/memory-tree/gotchas.py` as an acceptance
input, and S32 writes it. S14 reads `tools/workflows/replay_scorer.py`'s blob as an acceptance input,
and S9 to S12 write it. Any two halves therefore share a written file or a file one writes and the
other reads, so M6's clause 1 or 2 refuses every split.

### The resume probe's spelling (S1)

```
git grep -n -e 'verify-<a>-<b>' -e 'verify-${' -e 'verify:ids' -e 'verify-<first id>' -- tools memory/guides
  -> nothing; `verify-${` matches the id-range lookup and never `verify-batch-${`
stub run: capture the prompt of the `resume:probe` agent -> names `verify-batch-<n>.json`
```

### The address key's section class (S5, S6)

```
/\[([a-z][a-z0-9-]*)\]/                       -> the tag, first anywhere, wins
/(?:\bsection ?|§ ?)(\d+)\b/i  (leftmost)     -> `§<n>`; `\b` never precedes `§`, a non-word character
/\b(S|AC)(\d+)\b/              (leftmost)     -> upper case
else null
```

### The resolver port (S25, S26)

`resolveKitDir(home, anchor, here)` returns a directory or throws an `Error` naming the receipt and the
two probe paths. It finds the root as the nearest directory holding `.git`, reads
`.governance/install.json`'s `files` once, and walks the canonical's three rungs in its order.
`resolveHarnessName` calls it with `('workflows', 'tier2-review.js', <hook dir>)` and keeps its bare
name fallback on a throw. `checkOptinPackPresent` calls it with `('workflows',
'spec-audit-optin.js', <hook dir>)` and denies on a throw with the thrown message. The truth table:

| Row | Layout | Answer |
|---|---|---|
| 1 | receipt row naming the pack inside the tree | that row's directory |
| 2 | receipt row naming a missing path, pack beside the hook | the probe's directory |
| 3 | receipt row with `..` in its path, pack absent | refusal naming three places |
| 4 | `rendered` row whose path names the anchor | that row's directory |
| 5 | no receipt, pack at `<here>/workflows/` | that directory |
| 6 | no receipt, pack at `<here>/../workflows/` | that directory |
| 7 | nothing anywhere | refusal naming three places |

### The placement step (S18)

```bash
idx=$(mktemp -p "$SCRATCH"); trap 'rm -f "$idx"; git update-ref -d refs/replay/<name> 2>/dev/null' EXIT
GIT_INDEX_FILE="$idx" git read-tree <source commit>
GIT_INDEX_FILE="$idx" git update-index --add --cacheinfo 100644,<blob>,<path>
tree=$(GIT_INDEX_FILE="$idx" git write-tree)
git update-ref refs/replay/<name> "$(git commit-tree "$tree" -p <source commit> -m placement)"
# then the recipe, bundling refs/replay/<name>
```

`$SCRATCH` is the run's scratch directory. Each command's exit status is checked, and no step
touches the working tree, the index or `HEAD`.

### Files touched (estimate)

- `tools/workflows/tier2-review.template.js`
- `tools/workflows/tier2-review.js`
- `tools/workflows/tier2-review.test.sh`
- `tools/workflows/replay_scorer.py`
- `tools/workflows/README.md`
- `tools/hooks/agent-cap.js`
- `tools/hooks/agent-cap.test.sh`
- `tools/hooks/README.md`
- `tools/lib/resolve-python.test.sh`
- `tools/check-playbook-parity.sh`
- `tools/check-playbook-parity.test.sh`
- `tools/memory-tree/gotchas.py`
- `memory/builds/dFairHearing/build/`

`tools/workflows/tier2-review.js` is the template's render. `tools/hooks/README.md` changes where it
states the pack's home and the deny's wording. Under `memory/builds/dFairHearing/build/` only the two
replay verdict records change, and only by the lines S14 derives from git.

### Alternatives rejected

- **Two batch units** — §4 "Why one unit and not two".
- **Keep S20's hand port and widen it by hand (S25)** — the next widening of the resolver would miss
  it again, the drift `TOOL-aMendedFleet-102` repaired. One port behind a truth table cannot drift
  silently.
- **Amend spec 25's §3 for id 9 (S16)** — that folds the finding into the spec it was raised on, which
  M4 refuses.
- **Drop unit 27's AC23 with no replacement (S23)** — the restated S28 makes a claim a probe can
  refute, so it gets a criterion that can fail.

## 5. Production-readiness checklist

- security — S25 follows no receipt path outside the tree and no `..` path, as the canonical does, and
  keeps the fail-closed deny on the resolver's refusal. S18's placement writes only a transient ref the
  trap deletes. No new write path.
- perf / scale — one receipt read per spec-audit `Workflow` call; one `git ls-files` per held-out path.
- error / empty / loading states — S12, S31 and S25 turn a bad reference, a multi-line pathspec result
  and a failed resolution into a named exit or deny, never a traceback or an empty population.
- observability — each refusal names its arm, path or the places it looked.
- risks — S14 appends to two records written by earlier units, only with values git derives, so the
  appended lines cannot disagree with the tree.
- testing — scratch probes and fixtures per criterion; the §7 arms observed RED then GREEN at the close.
- migration — none for adopters beyond the deny's wording and the resolver's wider admission (S25).
- user docs — `tools/workflows/README.md` (the replay section) and `tools/hooks/README.md` (the pack's
  home). There is no `help/` page (§3).

## 6. Acceptance criteria

`$SCRATCH` is the pass's scratch directory, and a clone or fixture repository goes under
`%TEMP%/<short name>`. A bare script name is the workflows kit's file under `tools/workflows/`.

- **AC1** — When `git grep -n -e 'verify-<a>-<b>' -e 'verify-${' -e 'verify:ids' -e 'verify-<first id>' -- tools memory/guides`
  runs, it prints nothing. When a scratch stub-agent run of `tools/workflows/tier2-review.js` resumes,
  the prompt its stub captures for the `resume:probe` agent names `verify-batch-<n>.json`.
  Red when: `tools/workflows/tier2-review.template.js:1021` still reads `verify-<a>-<b>.json`.
- **AC2** — When a scratch node probe evaluates the prelude of `tools/workflows/tier2-review.js` as unit
  4 AC1 does, a spec-kind run keys the `where` values `§4`, `Section 3 Design`, `section4`, `§ 4` and
  `SECTION 12` to the `at` values `§4`, `§3`, `§4`, `§4` and `§12`.
  Red when: the class requires a space, so `§4` keys to `null`.
- **AC3** — When `grep -n -B12 "function deriveAddressKey" tools/workflows/tier2-review.template.js`
  runs, the comment it prints names the instrument's `loc` and three differences: whole-word tokens,
  the lens fallback and `§<n>` normalisation.
  Red when: the comment names two differences, or none.
- **AC4** — When a scratch python probe imports `review_replay.py` and a node probe evaluates
  `deriveAddressKey`, both read `[walk-table]` from `x.md:[walk-table] section 4`, the scorer reads
  section 4 and the key `§4` from `x.md:section 4`, and the scorer reads section 2 and the key `S5`
  from `x.md:S5 scope`. `git diff HEAD~1 HEAD -- tools/workflows/review_replay.py` prints nothing at this
  unit's commit.
  Red when: one reader is rewritten to the other's reading of `S5`.
- **AC5** — When `python replay_scorer.py --selftest` runs, it prints `selftest: <n>/<n> arms` and exits
  0. A scratch copy with `ARMS_DECLARED` lowered by one exits non-zero, naming the ran and declared
  counts.
  Red when: unit 14's arms ran with the declared count unraised.
- **AC6** — When `python replay_scorer.py --experiment <m>` runs over a scratch `review-replay` manifest
  whose one case's subject blob is blanked, it exits 2 naming that case and `case_evidence`. A manifest
  whose known set holds a row with no source record exits 2 naming the row.
  Red when: a run-case without a pinned subject is graded.
- **AC7** — When `--experiment` runs over four planted manifests, holding a duplicate arm name, a
  `base` naming no declared arm, a two-arm base cycle and a `union` naming no declared arm, each exits 2
  naming the arm and prints no `Traceback`.
  Red when: a dangling base raises a `KeyError`, or a misspelt union arm adds no coverage silently.
- **AC8** — When unit 30's verdict record states `selected`, `python tools/memory-tree/gotchas.py
  --for-diff <range> --all-ungated` over a fixture catalogue holding an ungated class outside the
  range's selection prints output byte-identical to the same command without the flag. When it states
  `ungated`, unit 30 AC4 answers this criterion.
  Red when: a `selected` verdict ships a flag that widens the checklist.
  fixture: a scratch catalogue repository under `%TEMP%/fgc`, made by the probe.
- **AC9** — When each replay verdict record is read, `git log --diff-filter=A --format=%P -1 -- <record>`
  prints a first parent equal to the record's orchestrating commit. `git merge-base --is-ancestor <unit
  23's commit> <that commit>` exits 0, and each blob the record names equals `git rev-parse
  <that commit>:<path>`. Each clone's `HEAD` is named on its own line.
  Red when: the record's commit is one the writer picked, or it names a clone's `HEAD` as the
  orchestrating commit.
- **AC10** — When `grep -n "trap " tools/workflows/README.md` runs, the replay section prints the EXIT
  trap, and `grep -n "commit-tree" tools/workflows/README.md` prints its placement step. A scratch run
  of that placement and recipe in a fixture repository, with `git bundle create` forced to fail, leaves
  `git for-each-ref refs/replay/` printing nothing, and that repository's `git status --porcelain` and
  `HEAD` unchanged. In this repository `git for-each-ref refs/replay/` prints nothing.
  Red when: a failed bundle leaves a transient ref, or the placement moves the working tree.
  fixture: the repository under `%TEMP%/fpl`, made by the probe.
- **AC11** — When `grep -n DESIGN_RECORD_PRESET tools/workflows/tier2-review.test.sh` runs, it finds
  spec 3's AC7 arm reading its expected preset from the constant. A scratch copy of `review_pin.py` with
  the constant set to `design-audit`, run with two design subjects and no flag as spec 3 AC7 runs it,
  prints `{"preset": "design-audit"}`, which is the value that arm then expects.
  Red when: the arm pins the literal `unit-spec`, so a replay-1 hit reds it.
- **AC12** — When the two replay verdict records are read, every attempt names its own clone, no run
  and no record-and-arm pair lists more than two attempts, and unit 30's record prints `paired 4 of 4` or
  names its void record beside `no decision`. A replay-1 run with no scored attempt has its R-1 ask in
  `memory/builds/dFairHearing/BACKLOG.md`.
  Red when: a clone serves two attempts, a third attempt runs, or a partial pairing decides.
- **AC13** — When a scratch node probe reads `tools/hooks/agent-cap.js` and `check-verifier-fanout.js`
  through `renderBlankedView`, neither holds a `MAX_LENSES` identifier, and the second holds one `const
  LENS_SLOTS` declaration. `git grep -n MAX_LENSES -- tools/check-playbook-parity.sh tools/check-playbook-parity.test.sh tools/workflows/REVIEW-PROTOCOL.template.md memory/guides/REVIEW-PROTOCOL.md`
  prints nothing, and `grep -cE '^[[:space:]]*(readonly |local )?LENS_SLOTS=' check-verifier-fanout.sh`
  prints 0. A scratch `agent-cap.js` copy holding `// MAX_LENSES was 6` passes the probe, and one
  holding `const MAX_LENSES = 6` fails it.
  Red when: a history comment reds a correct build, or a code declaration survives.
- **AC14** — When `git -c core.longpaths=false clone -q . "$SCRATCH/lp"` runs, it exits non-zero and
  prints `Filename too long`. The same clone into `%TEMP%/lp` exits 0.
  Red when: the scratchpad clone succeeds, which makes S23's restated claim false.
  cost: two local clones, about ten seconds each.
  figure: the 152-character scratchpad and the 118-character longest tracked path are PINNED,
  measured on 2026-10-23.
- **AC15** — When a scratch layout holds the hook at `$SCRATCH/p/.claude/hooks/agent-cap.js`, a `.git`
  directory, a receipt row naming a missing path and the pack at `$SCRATCH/p/.claude/workflows/`, a
  spec-audit payload exits 0. With the pack removed too, it exits 2 and its stderr names the receipt
  and both probe paths. With a row whose path holds `..` and no pack, it exits 2 the same way.
  `grep -c "function resolveKitDir" tools/hooks/agent-cap.js` prints 1.
  Red when: a stale receipt row denies a pack that sits beside the hook.
- **AC16** — When a scratch probe runs `resolve_kit_dir.py` and the JS port sliced from
  `tools/hooks/agent-cap.js` between its markers over §4's seven layouts, the two print the same answer
  on every row. A JS copy that denies on row 2 disagrees on that row.
  Red when: the port and the canonical disagree on any row.
- **AC17** — When a scratch copy of `tools/check-playbook-parity.sh` runs over this tree, the `lens-array
  bound` pair extracts 5 from `check-verifier-fanout.js` and 5 from the stated side. Over the
  suite's valid fixture it exits 0, and with the planted `LENS_SLOTS` set to 6 it exits non-zero naming
  `lens-array bound`.
  Red when: the pair hardcodes a `tools/workflows/` path, or the fixture lacks the planted kit and its
  control reds.
- **AC18** — When `python tools/govkit/govkit.py update --target "$TEMP/fhk" --kits agent-cap` runs on a
  target whose receipt claims agent-cap, review-harness and drift-audit, it prints `scope: review-harness
  moves with agent-cap` and a `scope:` line naming drift-audit.
  Red when: drift-audit moves unannounced, or not at all.
  fixture: the target under `%TEMP%/fhk`, made by `govkit.py apply` with the three kits.
  cost: one apply and one update into a scratch target, under a minute.
- **AC19** — When `--experiment` runs with `heldOut` naming a directory, and again a path holding `*`,
  each exits 2 naming the path and its `git ls-files` line count, never a traceback.
  Red when: the first output line is taken, so a different file from the one named is checked.
- **AC20** — When a scratch python probe imports `tools/memory-tree/gotchas.py`, `check_ungated` reads
  ``**Gated by `tools/check-wiring.sh`.** Next sentence names `tools/y`.`` with `tools/check-wiring.sh`
  in scope and `tools/y` outside it.
  Red when: the scope runs past `.**` into the next sentence.

## 7. Gates

`tier2-review self-test` · `verifier fan-out self-test` · `verifier fan-out` · `unattended-build self-test` · `review-join self-test` · `agent-cap self-test` · `scratch-guard self-test` · `hook destinations self-test` · `agent-cap restatement` · `playbook parity selftest` · `playbook parity` · `python resolver (behaviour + inline parity + idiom ban)` · `review-replay selftest` · `gotchas selftest` · `workflow script syntax` · `harness arms (fail branches armed or pinned)` · `testsuite counts (every bar self-test prints one)` · `recall floor` · `recall floor arms` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/workflows/tier2-review.test.sh · covers AC1 AC2 AC11 · the resume probe's old spelling, a space-required section class and spec 3's AC7 arm pinned to the literal under a flipped constant, staged against the harness at `TOOL-dFairHearing-30`'s commit · FLOOR_ASSERTIONS in that suite, raised by the arms added
New arm: tools/workflows/replay_scorer.py (its runner, in the `review-replay selftest` leg) · covers AC5 AC6 AC7 AC19 · a blanked subject blob, each broken reference and a directory and a glob held-out path, staged against the factory at `TOOL-dFairHearing-30`'s commit · that runner's `ARMS_DECLARED`, raised by the arms added
New arm: tools/lib/resolve-python.test.sh · covers AC16 · a JS port that denies on a missing receipt row · none
New arm: tools/hooks/agent-cap.test.sh · covers AC15 · a stale receipt row with the pack beside the hook, staged against the hook at `TOOL-dFairHearing-27`'s commit · none
New arm: tools/check-playbook-parity.test.sh · covers AC17 · the planted workflows kit's `LENS_SLOTS` at 6, and the pair read from the hooks kit as at base · none
New arm: tools/memory-tree/gotchas.py (its selftest) · covers AC20 · a gated sentence closing on `.**`, staged against `TOOL-dFairHearing-27`'s `check_ungated` · none

## 8. Open questions

- **F1 — One batch unit or two (BUILD-METHOD M4, M6)?** Options: (a) one; (b) two, split along a
  disjoint write set. Every split §4 tried shares `replay_scorer.py`, `tier2-review.test.sh` or a file
  one half writes and the other reads as an acceptance input, which M6's clauses 1 and 2 refuse.
  RESOLVED (agent, 2026-10-23, delegated): (a), rung 3. widens: none · relaxes: none
- **F2 — How does id 9's missing edge close without folding (S16)?** Options: (a) add three
  consumes-from edges to spec 25 now; (b) declare each read on the unit that reads it after this audit,
  unit 30 for unit 14 and this unit for units 3 and 16; (c) amend spec 25 at this unit's build pass.
  (a) folds the finding into its own spec, which M4 refuses. (c) edits a spec that is CLOSED by the
  time this unit builds, and a landed record is frozen. RESOLVED (agent, 2026-10-23, delegated): (b),
  rung 3. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft, promoting the 21 MEDIUM and 11 LOW findings of the round-3 spec
  audit of specs 4, 14, 25, 26 and 27 as one batch.

## 10. Reuse audit

Every item extends a seam an earlier unit mints or the base tree carries, and none adds a module. The
seams: `resolve_kit_dir`'s three rungs (`tools/lib/resolve_kit_dir.py:15-51`) and its behaviour-arm
shape (`tools/lib/resolve-python.test.sh`, arm 2b); `renderBlankedView` (`tools/hooks/agent-cap.js:1303`);
the parity gate's per-kit resolution (`tools/check-playbook-parity.sh:141-148`); govkit's coupling
closure (`tools/govkit/govkit.py:1050-1059`, `:9311`); the runner floor (`tools/workflows/review_replay.py:84`,
`:604-606`); and the README recipe with unit 27 S22's trap. `python tools/codebase-map/reuse_lookup.py
"resolve the merge base with the remote default branch or refuse"` ranked `resolve_kit_dir`, with 72
installs, which is the port S25 holds to it. The recall query returned the audit's appendix, spec
4's inventory of the verify file name, spec 14's criteria and `TOOL-aEvidencedLens-15`, the replay
scorer's spec-kind reading, and no prior JS port of the resolver. `TOOL-aMendedFleet-102`, the
resolver drift a hand port repeats, is the audit's citation in item M6, not a recall hit.

Recall terms used: `python tools/memory-recall/query.py "spec audit minors on resume file spelling, address key class, manifest references, replay records and the resolver port" --terms "verify-batch resume probe deriveAddressKey section class case_evidence manifest base union resolve_kit_dir port blanked view"`
