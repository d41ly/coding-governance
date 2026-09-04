# TOOL-aJoinedCanon-6 — a ledger answer is joined to its own criterion

**Status:** SPECCED · rev-1 · 2026-09-04 · node a · Tier-2 · base 750ca0ca · streams tooling · order 6

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

Check 23 pairs a spec's acceptance criteria to their ledger answers by LABEL and compares nothing
else, so a ledger line keyed `AC4` that answers `AC5`'s question passes and a ledger line keyed to a
label the spec never wrote is invisible. This unit adds the two halves of that join a machine can
actually decide: a walk of the ledger's own labels, and a token comparison between a criterion and
the answer that claims to evidence it.

## 2. Scope (IN)

- **S1** — A ledger-side label walk. Every `**Evidences:** <uid>` bullet whose `<uid>` is in check
  23's graded unit set and whose label the spec's §6 does not number becomes a named failure.
  Observed by AC1.
- **S2** — A token join. For a criterion whose label DOES appear in the ledger map, the criterion's
  backticked tokens and the answer's backticked tokens must share at least one token under
  case-folded bidirectional containment. Observed by AC2 and AC3.
- **S3** — Both arms are bullet-scoped on both sides: a criterion's tokens are collected across its
  continuation lines, and so are an answer's. Observed by AC4.
- **S4** — Two new dated cutoff keys in `.memory-tree.conf`, `LEDGER_LABEL_CUTOFF` and
  `LEDGER_TOKEN_CUTOFF`, each compared against the SPEC's filename date exactly as `alcut` is at
  `check-memory-hygiene.sh:1376`, each blank-means-off. Observed by AC5 and AC6.
- **S5** — Both arms announce an empty population, in the shape `check-memory-hygiene.sh:1526`
  already uses, so a cutoff that grandfathers everything is not mistaken for a clean run. Observed
  by AC7.
- **S6** — The ledger grammar in `memory/HYGIENE.md` and `tools/memory-tree/HYGIENE.template.md`
  states the token rule, so an author reads it where the grammar lives rather than discovering it
  from a red bar. Observed by AC8.
- **S7** — A failing fixture per new `fail 23` branch in `check-memory-hygiene.test.sh`, with the
  positive `hit` assertion the harness meta-gate requires. Observed by AC9.

## 3. Non-goals (OUT)

- **The semantic half is explicitly out.** A machine cannot tell that a well-formed answer is about
  the wrong QUESTION. `DEPL-dRetiredFork-3`'s ledger `AC3` cites `classify_outcome` while its spec
  `AC3` asks about an empty artifact, and under this unit's predicate that pair would still have to
  be caught by a token disagreement, not by understanding either sentence. The row that approaches
  this from the other side is `TOOL-aBoundedVerdict-32` (`memory/backlog/TOOL.md:152`), which
  records that nothing gates a criterion against the TREE at close time. Neither row subsumes the
  other and this unit does not close that one.
- **No retrofit of any landed ledger.** `DEPL-dRetiredFork-3` is CLOSED and green and its ledger
  invents a label its spec never wrote; it stays as it is. `.memory-tree.conf:307-323` states the
  position this unit obeys — back-filling another build's ledger is not this build's to do, because
  a build's own folder owns its own prose.
- **`ACCEPTANCE_LEDGER_CUTOFF` and `ACCEPTANCE_LEDGER_GRANDFATHER` are not touched.** The
  grandfather list is declared SHRINK-ONLY with a stated admission reason that no unit here meets,
  so a new arm buys its own cutoff key instead of a new exemption row.
- **Check 12's acceptance-witness arm is not touched.** That arm
  (`check-memory-hygiene.sh:1020-1048`) decides whether a criterion names anything at all. This unit
  never re-grades that: a criterion with no backticked token is silent here, not doubly red.
- **HYGIENE.md's numbered catalog is not renumbered.** It stops at item 22 while the shell
  implements 23; that is `TOOL-aScouredKit-22` (`memory/backlog/TOOL.md:300`) and it is a different
  edit to the same file pair.
- **No new check number.** Both arms are `fail 23` branches on the existing check, so the kit
  README's check count does not move.

## 4. Design

### Data model

`alledger` at `check-memory-hygiene.sh:1419` emits one space-separated `<unit> <label> <form>`
triple per ledger bullet, and its `form` classification reads the bullet's FIRST LINE only. `alsel`
at `:1457` emits `U\t<seq>\t<uid>` per graded spec and `L\t<seq>\t<uid>\t<label>` per §6 label, and
collects no token. Both gain one field.

| Producer | New field | Content |
|---|---|---|
| `alledger` | 4th, TAB-separated | the answer's backticked tokens, backtick-joined |
| `alsel` `L` row | 5th, TAB-separated | the criterion's backticked tokens, backtick-joined |
| `alsel` `U` row | 4th and 5th | `1`/`0` for the label era and the token era |

A backtick is the field separator inside a token list because the extractor is `` `[^`]+` `` and a
captured token therefore cannot contain one. The `U` row carries the era flags rather than the
filename date, so the date comparison stays in awk beside the one `alcut` already does and bash
reads booleans.

The existing bash reader at `:1495-1500` splits a triple with `${_al% *}` and `${_al##* }`. It gains
a leading `IFS=$'\t' read -r _altriple _altok` and then splits `_altriple` exactly as today, so the
FIRST-WINS map semantics documented there are unchanged. A parallel `ALTOK` map is filled under the
same first-wins rule and the same key.

### The two arms

**Arm A, the ledger-side walk.** The `L` walk at `:1508-1516` gains `ALSPECLAB["$_alk"]=1`, and the
`U` walk gains `ALUID["$_uuid"]=$labera`. A new walk over `ALFORM`'s keys reports any key whose unit
is in `ALUID` with the flag set and whose full key is absent from `ALSPECLAB`. Bash associative-array
key order is unspecified, so the collected offenders are piped through `sort` before the failure
string is built — the three existing arms get byte-stable output from a sorted input stream and this
one must earn it explicitly.

**Arm B, the token join.** Inside the existing `L` walk, when the key is present in `ALFORM` and the
unit's token era is on, the criterion's tokens and `ALTOK`'s tokens are compared. A pair passes when
either token contains the other after case folding, using `[[ $a == *"$b"* ]]`, which is a bash
builtin and forks nothing. An EMPTY list on either side makes the arm silent for that criterion:
an empty spec side is check 12's acceptance-witness arm, and an empty ledger side is already the
existing `albad` branch.

Containment rather than equality is a measured choice, not a softening. The corpus writes the same
subject two ways across the join — a criterion says `tools/govkit/selftest.py` and its answer says
`python tools/govkit/selftest.py`, or a criterion names a spec file by basename and its answer names
it by repo path. Exact set intersection calls all of those disagreements.

### Inventory

Reproduced at base 750ca0ca with a throwaway probe mirroring check 23's own selectors (filename date
at or after the cutoff, `**Status:**` in the first six raw lines, CLOSED, Tier-2, an acceptance
heading, an H1 id, minus `ACCEPTANCE_LEDGER_GRANDFATHER`). Population: 145 CLOSED Tier-2 units,
1,241 answers whose label the spec also numbers.

| Predicate | Failing answers | Rate | Units touched |
|---|---|---|---|
| Arm A — ledger label the spec never wrote | 1 | — | 1 of 145 |
| Arm B — exact token-set intersection | 487 | 39.2% | 136 of 145 |
| Arm B — case-folded bidirectional containment | 315 | 25.4% | 116 of 145 |

Finding 19 binds at **307 of 1,377 ledger answers, 22.3%**, and this table does not reproduce that
figure. The denominators differ: 1,377 counts every ledger answer, while 1,241 counts only those
whose label the spec also numbers, which is the set arm B can grade at all. Both are recorded rather
than reconciled, and the design is sized against the larger of them.

Arm A's single corpus-wide hit is `DEPL-dRetiredFork-3` `AC8`. Verified directly: the spec numbers
ELEVEN labels at
`memory/builds/dRetiredFork/spec/2026-09-02-spec-DEPL-dRetiredFork-3.md:96-131`, `AC1`-`AC7` and
`AC9`-`AC12`, and the ledger at
`memory/builds/dRetiredFork/build/2026-09-03-build-DEPL-dRetiredFork-3-1-acceptance-ledger.md:24-64`
writes TWELVE, `AC1`-`AC12`. The invented label is the twelfth, not the thirteenth the findings
record names; the count is otherwise as recorded.

### Migration

**Arm A ships at `LEDGER_LABEL_CUTOFF="2026-09-04"`.** Measured: six CLOSED Tier-2 specs are already
dated at or after 2026-09-04, and arm A reds NONE of them. The one historical hit is dated
2026-09-02 and falls outside. So arm A lands with a live, non-empty first population and reds no
landed work, which is the shape `.memory-tree.conf:298-300` argues for.

**Arm B ships at a `LEDGER_TOKEN_CUTOFF` strictly AFTER the newest spec filename date in the tree at
landing.** No earlier value is available. Measured on the same six-unit cohort dated 2026-09-04 or
later, containment still fails 8 of 44 answers (18.2%) across 5 of those 6 units, so even the
newest closed work does not satisfy this arm. The value is derived in the landing commit rather than
pinned here, because a date typed into a spec goes stale between writing and landing:

```bash
git ls-files 'memory/builds/*/spec/*.md' | sed 's#.*/##' | grep -E '^[0-9]{4}-[0-9]{2}-[0-9]{2}-' \
  | cut -c1-10 | sort | tail -1
```

The landing commit states the chosen value and its reason, per the cutoff discipline the other keys
in that file already follow.

The residual failures under containment are dominated by one legitimate answer form the predicate
cannot recognise: the ledger cites a self-test ARM ID such as `[-ST4]` where the criterion named the
file the arm lives in. That is a real answer, and it is why S6 puts the rule in the ledger grammar
where an author reads it — the fix is a notation the writer follows, not a predicate that guesses.

### Rollout

Arm A and arm B land in one commit and are separated by their cutoffs, not by a flag. A blank value
in either key turns that arm off entirely, which is the rollback: one conf edit, no code revert.

### Files touched (estimate)

| File | Change |
|---|---|
| `tools/memory-tree/check-memory-hygiene.sh` | two awk emitters, two bash walks, two `fail 23` branches, two announce lines |
| `tools/memory-tree/check-memory-hygiene.test.sh` | fixtures for both arms plus their `hit` assertions |
| `.memory-tree.conf` | two keys with their reasons, and the test's fixture conf at `:67` gains both |
| `memory/HYGIENE.md` | the token rule under `## Acceptance ledger` |
| `tools/memory-tree/HYGIENE.template.md` | the same bytes — `kit-dogfood-parity.test.sh:53` compares the pair |

### Alternatives rejected

- **One cutoff key for both arms.** It forces the free arm to wait for the expensive one. Arm A
  is landable today against a live population; arm B is not landable against any date in the corpus.
  One key buys a smaller diff and costs both arms a live first run.
- **Add `DEPL-dRetiredFork-3` to `ACCEPTANCE_LEDGER_GRANDFATHER` and land arm A at the existing
  cutoff.** That list exempts a unit from ALL of check 23, so it would trade one new finding for
  three existing ones. Its own declaration also restricts admissions to units that closed while the
  grammar was unmerged, which this is not.
- **Fix the `DEPL-dRetiredFork-3` ledger line instead.** Ruled out by the position recorded beside
  the grandfather list: a build's own folder owns its own prose.
- **Exact token-set equality.** Measured at 39.2% against containment's 25.4%, and the extra 172
  answers are dominated by path-prefix and invocation-prefix variance rather than by disagreement.
- **A third form in the ledger grammar for "no shared token, and here is why".** It re-introduces
  the escape hatch `HYGIENE.md:302-305` deliberately refuses, where a third form turns the ledger
  into a checkbox exercise.

## 5. Production-readiness checklist

- security — N/A. Both arms read tracked records already in the working tree and write nothing.
- perf / scale — no new process is spawned. Both awks gain fields on lines they already emit, and
  arm B's comparison is a bash builtin inside a loop that already runs. The wall-clock delta is
  UNVERIFIED and AC10 measures it. Note when reading history here: check 23's 962.0 s figure
  measures the implementation `TOOL-aCollapsedScan-13` retired, and that record says so.
- a11y — N/A. A shell gate has no user interface.
- i18n — N/A, with one real constraint: case folding must not be locale-sensitive, so the comparison
  stays ASCII and the surrounding code sets no `LC_ALL`, matching the deliberate choice at
  `check-memory-hygiene.sh:1503-1506`.
- error / empty / loading states — an empty population per arm announces itself, which is S5.
- observability — each failure names the unit and the label, in the shape the three existing `fail 23`
  branches use.
- risks — the named risk is arm B's false-positive rate against future authors, which is what §8's
  fork is about. There is no data-loss or rollback hazard: a blank cutoff disarms either arm.
- testing + left-shift gates — the harness meta-gate makes this mandatory rather than optional. Every
  `fail` branch must be ARMED by a positive assertion in `check-memory-hygiene.test.sh` naming a
  literal slice of its own failure text, or be listed in `memory/project/unarmed-branches.txt`; neither new
  branch will be listed there.
- migration / rollback — two dated cutoffs, per §4 Migration. Rollback is a conf edit.
- user docs — the ledger grammar in the `HYGIENE` pair is the doc, and it is S6.

## 6. Acceptance criteria

- **AC1** — When a fixture ledger evidences a graded unit with a label its spec never numbers, `bash
  tools/memory-tree/check-memory-hygiene.sh` reds naming that unit and that label; removing the
  fixture line returns the run to green.
- **AC2** — When a fixture criterion names `` `alpha` `` and its ledger answer names only
  `` `beta` ``, `bash tools/memory-tree/check-memory-hygiene.sh` reds naming that pair.
- **AC3** — When that same fixture answer names `` `python alpha --write` ``, the run is green,
  because containment matches where exact intersection would not.
- **AC4** — When a fixture criterion's only backticked token sits on a CONTINUATION line rather than
  the bullet head, the run is green; the same fixture with the token deleted reds. This is the
  bullet-scope assertion, and it is the one that would silently pass if the token capture were
  line-scoped like `alledger`'s existing `form` classification.
- **AC5** — When `LEDGER_LABEL_CUTOFF` is set past a fixture spec's filename date, that spec's
  orphan ledger label stops being reported and the rest of check 23's verdict on it is unchanged.
- **AC6** — When either new key is blank in `.memory-tree.conf`, its arm reports nothing at all and
  `bash tools/memory-tree/check-memory-hygiene.sh` is green over the real tree.
- **AC7** — When every graded spec predates an arm's cutoff, that arm prints its own
  `measured NO unit` announce line, matching the shape at `check-memory-hygiene.sh:1526`.
- **AC8** — When the token rule lands in `memory/HYGIENE.md`, `bash
  tools/memory-tree/kit-dogfood-parity.test.sh` is green, proving
  `tools/memory-tree/HYGIENE.template.md` carries the same bytes.
- **AC9** — When `python3 tools/memory-tree/check-arms.py --check` runs, both new `fail 23` branches
  are ARMED, and neither appears in `memory/project/unarmed-branches.txt`.
- **AC10** — When `LEDGER_TOKEN_CUTOFF` is temporarily set to `ACCEPTANCE_LEDGER_CUTOFF`'s value and
  `bash tools/memory-tree/check-memory-hygiene.sh` is run, the arm reports a count within a stated
  tolerance of the 315-of-1,241 figure in §4, re-deriving the table from the landed arm instead of
  from the probe that is not committed. The temporary value is reverted in the same session.
- **AC11** — When the whole bar runs, `bash tools/run-gates/run-gates.sh` is green with
  `memory hygiene` and `memory-hygiene self-test` among its legs, and the elapsed row for
  `memory hygiene` in `<git-dir>/gate-ledger.tsv` is recorded beside the pre-change one.

## 7. Gates

- `memory hygiene` — `bash tools/memory-tree/check-memory-hygiene.sh`, unguarded, and the leg both
  arms actually bind on. Check 23 is HELD under `--staged` (`check-memory-hygiene.sh:1405`), so these
  arms bind at the push boundary and never in pre-commit.
- `memory-hygiene self-test` — `bash tools/memory-tree/check-memory-hygiene.test.sh`, guarded on
  `tools/memory-tree/`, which this unit edits.
- `kit/dogfood doc parity` — `bash tools/memory-tree/kit-dogfood-parity.test.sh`, the byte-compare
  that makes the `HYGIENE` pair move together.
- `harness arms (fail branches armed or pinned)` — `python3 tools/memory-tree/check-arms.py --check`,
  unguarded, and the leg that refuses an unarmed new `fail` branch.
- `check-arms selftest` — `python3 tools/memory-tree/check-arms.py --selftest`.
- No new leg. Both arms live inside a check that already has one.

## 8. Open questions

- **FORK-1 · Does arm B red, or does it only report?** The measured failure rate is 25.4% corpus-wide
  and 18.2% on the newest closed cohort, both under the most forgiving cheap predicate, and the
  residual is dominated by one legitimate answer form — a ledger citing a self-test arm id where the
  criterion named a file. A forward cutoff means no landed work reds either way, so the question is
  purely what future authors face.

  Option A, red. The rule becomes real, and the notation it demands is one an author can follow once
  it is written in the ledger grammar. The risk is a gate that manufactures work on correct ledgers
  and gets waived.

  Option B, advisory. The arm prints a count and a list and never sets `status=1`, for one release,
  and the count decides whether option A is safe. The risk is a printed number nobody reads, which
  is this repo's own named class.

  **Recommendation: A.** An advisory arm has no failing case to observe, so it cannot satisfy the
  build rule that a new arm owes an observed red, and a check that cannot fail is the shape §7 of
  the charter refuses outright. UNRESOLVED — the owner decides, and it is the one decision in this
  spec that changes what the arm is.

## 9. Revision log

- rev-1 · 2026-09-04 · initial draft.

## 10. Reuse audit

No existing seam fits, and the probe says why. `python tools/codebase-map/reuse_lookup.py "join a
ledger answer to the acceptance criterion it answers"` over 645 symbols and 19 affordance seams
returns no join helper: its ranked hits are `join_aliases` in `tools/memory-recall/extract.py`
(fan-in 1, an alias-table builder), `joinCall` and `scanJoinFindings` in `tools/hooks/agent-cap.js`
(fan-in 0, both about the fan-out cap), and `signal_ledger` in
`tools/drift-audit/drift_report.py` (fan-in 0, a drift signal and not this ledger). Nothing in the
corpus compares two token sets across a document join. The seam this unit extends is therefore
check 23's own, already built and named in §4: the `ALFORM` map at
`tools/memory-tree/check-memory-hygiene.sh:1495` and the label walk at `:1508-1516`, both of which
gain fields rather than callers. The recall query surfaced two rows worth reading before building,
and both are in §3: `TOOL-aBoundedVerdict-32` and `TOOL-aScouredKit-22`.

Recall terms used: `acceptance ledger criterion label join hygiene check 23 backticked token
OBSERVED AMENDED cutoff grandfather shape coverage`
