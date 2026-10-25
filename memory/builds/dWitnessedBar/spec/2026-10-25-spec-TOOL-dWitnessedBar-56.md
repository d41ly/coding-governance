# TOOL-dWitnessedBar-56 — the round-1 audit of units 40 to 51, verdict-boundary minors batched: a lossless selection, one adoption rule on both readers, honest peer reads, and floors under the new arms

**Status:** OPEN · rev-2 · 2026-10-25 · node d · Tier-2 · base cdfbd1cf · streams tooling · order 32 · advances TOOL-dWitnessedBar-31

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md) | journal | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-54 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-57 TOOL-dWitnessedBar-58 TOOL-dWitnessedBar-59 TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-61 TOOL-dWitnessedBar-62 TOOL-dWitnessedBar-63 |
| [2026-10-25-build-TOOL-dWitnessedBar-52-round2-fix-return.md](../build/2026-10-25-build-TOOL-dWitnessedBar-52-round2-fix-return.md) | research | TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-57 |
| [2026-10-25-prompt-TOOL-dWitnessedBar-52-round2-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dWitnessedBar-52-round2-fix-brief.md) | research | TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-57 |
| [2026-10-25-review-TOOL-dWitnessedBar-52-spec-audit-round1.md](../reviews/2026-10-25-review-TOOL-dWitnessedBar-52-spec-audit-round1.md) | spec-audit | TOOL-dWitnessedBar-54 TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-57 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 40 to 51
(`memory/builds/dWitnessedBar/reviews/2026-10-25-review-TOOL-dWitnessedBar-40-spec-audit-round1.md`)
exited CONVERGED with 48 confirmed findings. Its 4 highs are units 52 to 55. BUILD-METHOD M4 batches
every MEDIUM and LOW; they split into two disjoint write sets by M6's clauses, so they are two units
that build concurrently. This one holds the verdict boundary's 20: the runner's per-tree record, the
pre-push hook, the verdict backends, the run-gates suites and the two kit READMEs. Its sibling
`TOOL-dWitnessedBar-57` holds the resolver, ledger and adopter 24. Each finding is named by report id
and is its own scope item, where the report merged ids into one item too. The minors land on several
units, so this unit repairs none in particular and builds after every unit (order 32).

| Report item | Severity | Report ids | Scope items |
|---|---|---|---|
| M2 | MEDIUM | 2, 16, 47 | S1, S2, S3 |
| M3 | MEDIUM | 3 | S4 |
| M4 | MEDIUM | 4, 14 | S5, S6 |
| M5 | MEDIUM | 15, 33 | S7, S8 |
| M12 | MEDIUM | 32 | S9 |
| L12 | LOW | 27 | S10 |
| M20 | MEDIUM | 48 | S11 |
| L16 | LOW | 49 | S12 |
| L17 | LOW | 52 | S13 |
| L10 | LOW | 23 | S14 |
| M21 | MEDIUM | 50 | S15 |
| L8 | LOW | 20 | S16 |
| M14 | MEDIUM | 35 | S17 |
| L5 | LOW | 11 | S18 |
| M16 | MEDIUM | 37 | S19 |
| L15 | LOW | 41 | S20 |

That is 13 MEDIUM and 7 LOW findings by raw id.

## 2. Scope (IN)

- **S1** — id 2. A `selection.<n>` value is the accepted row's three fields TAB-separated,
  `<leg><TAB><source><TAB><note>`, in place of `TOOL-dWitnessedBar-41` §4's ` · ` join; the hook rebuilds
  each canonical row as `held<TAB>` plus the value. A ` · ` in a note round-trips. Observed by AC1.
- **S2** — id 16. The runner cuts one trailing CR from each selection row before it accepts or hashes
  the row, as the record readers cut it (`tools/run-gates/run-gates.sh:2393`), so a CRLF selection file
  hashes as its LF twin. Observed by AC1.
- **S3** — id 47. The canonical text is the rows the runner accepted: four TAB fields, the first `held`,
  a source the runner holds, a leg the manifest carries. Every other row is left out of the text and the
  `selection.<n>` keys and counted on the per-tree record as `selection_ignored <n>`, so the hook and
  `select --check --selection` read the same rows the runner held. Observed by AC2.
- **S4** — id 3. The adopt plants in `.githooks/pre-push.test.sh`, `TOOL-dWitnessedBar-4`'s AC4 plant
  and `TOOL-dWitnessedBar-40`'s both-at-0 plant, carry `reused 0`, `reused_cache 0` and `selection none`,
  the keys units 40 and 41 make required. Observed by AC3.
- **S5** — id 4. The hook's export is observed: a push over a scratch clone that takes the inherited-green
  branch (`.githooks/pre-push:2123-2126`) runs a bar whose environment carries `GATE_BASE_FROM=inherited`
  and writes no `.scoped` record. Observed by AC4.
- **S6** — id 14. `check_bar_record` refuses a per-tree record carrying neither `reused` nor
  `reused_cache` in a branch of its own, before it calls `check_green_reuse`, which forces nothing when
  both are empty (`.githooks/pre-push:1549-1559`). Observed by AC5.
- **S7** — id 15. `read_local_verdict` (`TOOL-dWitnessedBar-6` S4) reads `NONE` for a record unit 40's
  predicates refuse: a non-zero `reused_cache`, a `reused` with no `reused_cache`, or neither key.
  Observed by AC6.
- **S8** — id 33. `read_local_verdict` reads `NONE` for a record unit 41's predicates refuse: no
  `selection` key, a rebuilt text whose hash differs, or `select --check --selection` exiting 1; a parity
  arm runs the hook's adoption and `read --backend local-hook` over the same plants. Observed by AC6.
- **S9** — id 32. The hook clears `GATE_BASE_FROM` and `GATE_SELECTION` for every bar, a STUB included,
  as it clears `GATE_DOCS_BASE` (`.githooks/pre-push:1857-1858`), and sets `GATE_BASE_FROM` only in its
  inherited-green branch. Both join `BAR_INERT_KNOBS` in `.githooks/pre-push.test.sh` with a reason line
  (§8 F2). Observed by AC7.
- **S10** — id 27. The run record's `base_from` row (`run-gates.sh:3485`) carries a third field
  `inherited` when `GATE_BASE_FROM` reads so, and unit 40's decline line names that row, so the record
  says why no verdict was written. Observed by AC8.
- **S11** — id 48. `TOOL-dWitnessedBar-51`'s AC24 arm sets the B-named verdict's modification time 31
  days back too, so only a sweep that reads B's run records keeps it. Observed by AC9.
- **S12** — id 49. The tail write's order is: cut at the last whole UTF-8 character within 8192 bytes,
  decode with `errors='replace'`, escape each C0 control byte other than TAB and LF, CR included, and
  DEL as `\xHH`, re-cut to 8192 bytes at a whole character, then hash the stored bytes.
  Observed by AC10.
- **S13** — id 52. The tail sweep reads any file named `<hash>.<suffix>` as a temp, whichever spelling
  `derive_temp_path` gave it (`run-gates.sh:782`: `.tmp` under `SRANDOM`, `mktemp -u` otherwise), and
  unlinks a temp older than `TAIL_GRACE_S`; this rule supersedes unit 42's skip of temps.
  Observed by AC11.
- **S14** — id 23. The tail sweep and the per-tree verdict prune each carry a comment naming the reuse
  cache's 30-day prune (`run-gates.sh:5446-5520`, `cut` at `:5506`) as the seam considered and rejected:
  it runs only when the cache block fires, keeps no set and swallows errors; and why the tail grace is 7
  days against the cache's 30. Observed by AC12.
- **S15** — id 50. `read_peer_verdict`'s failure map (`TOOL-dWitnessedBar-43` §4 "The read"): a signer
  read that exits non-zero, or an advertised tip absent from the object database, is `DEAD PROBE` naming
  the cause; `verify-tag` printing no signature is `NONE` `unsigned`, a bad signature or no matched
  principal `NONE` `unknown key`, any other non-zero exit with no recognised line, `ssh-keygen` absent
  included, `DEAD PROBE`. The allowed-signers file is made by `tempfile.mkstemp` under the git dir and
  unlinked after the read. Observed by AC13.
- **S16** — id 20. The principal is read from `verify-tag --raw`'s stderr, where git prints the
  `Good "git" signature for <principal>` line; its stdout is empty. Observed by AC14.
- **S17** — id 35. Unit 43's four peer plants run from `tools/run-gates/run-gates.gov.test.sh`, the suite
  `run-gates gov canary` runs, and this unit's §7 names that leg. Observed by AC15.
- **S18** — id 11. Unit 43's AC3 rests on `tools/loop/guard.py`, which TOOL-dDeclaredLoop-2 creates
  outside this build and the tree lacks today. At the close the main loop runs AC3's command when the file
  exists, and otherwise records AC3 `NOT OBSERVED` in unit 43's acceptance ledger naming the absent file.
  Observed by AC16.
- **S19** — id 37. Each floored suite an arm of units 40, 41, 42, 43, 45, 46 or 51 lands in raises its
  `FLOOR_ASSERTIONS` by the assertions those arms add, with a dated `RAISED` comment per unit:
  `tools/run-gates/run-gates.evidence.test.sh` (240), `tools/run-gates/run-gates.gov.test.sh` (16),
  `tools/run-gates/adopt-run-gates.test.sh` (17) and `tools/memory-tree/check-memory-hygiene.test.sh`
  (668). Observed by AC17.
- **S20** — id 41. The README sentences units 40, 41, 42, 44 and 46 promise in their §5 land:
  `tools/run-gates/README.md` names the two declines and the reuse pair, the `selection` keys, the tail
  grace and the step's two policy files; `tools/memory-tree/README.md` carries the adopter-receives
  table. This pass writes whichever a pass left out. Observed by AC18.

## 3. Non-goals (OUT)

- Any high: units 52 to 55, one per id.
- The resolver, ledger and adopter minors: `TOOL-dWitnessedBar-57`.
- The spec lints and checklist entries the report names as left-shifts: each is a gate no clause of this
  build names; S8's parity arm and S19's floors are the two this batch builds.
- Re-wording another unit's spec text: each item is closed by what this pass builds or observes.

### Edges

- **consumes-from** `TOOL-dWitnessedBar-41` — the `selection` keys, their canonical text and the hook's rebuild (ids 2, 16, 47, 3, 33)
- **consumes-from** `TOOL-dWitnessedBar-40` — the reuse pair, the keyless refusal, `GATE_BASE_FROM` and its export (ids 3, 4, 14, 15, 27, 32)
- **consumes-from** `TOOL-dWitnessedBar-4` — the per-tree record and its AC4 adopt plant (id 3)
- **consumes-from** `TOOL-dWitnessedBar-5` — the `GATE_SELECTION` knob (id 32)
- **consumes-from** `TOOL-dWitnessedBar-6` — `verdict_backends.py` and `read_local_verdict` (ids 15, 33)
- **consumes-from** `TOOL-dWitnessedBar-42` — the tail sweep and `TAIL_GRACE_S` (ids 23, 52)
- **consumes-from** `TOOL-dWitnessedBar-43` — `read_peer_verdict`, its plants and its AC3 (ids 11, 20, 35, 50)
- **consumes-from** `TOOL-dWitnessedBar-44` — the README migration note it promises (id 41)
- **consumes-from** `TOOL-dWitnessedBar-45` — its arm in `adopt-run-gates.test.sh` (id 37)
- **consumes-from** `TOOL-dWitnessedBar-46` — its hygiene-suite arm and the adopter-receives table (ids 37, 41)
- **consumes-from** `TOOL-dWitnessedBar-51` — the AC24 arm, the tail cut of S34 and the verdict prune of S28 (ids 23, 48, 49)
- **hands-off** `TOOL-dWitnessedBar-58` — AC4's in-leg observation of `GATE_BASE_FROM`, which id 12's unit replaces with observations at the stub bar and the runner boundary, and S10's `inherited` field it reads
- **hands-off** `TOOL-dWitnessedBar-60` — S9's clears of `GATE_BASE_FROM` and `GATE_SELECTION`, which id 28's unit folds into `BAR_CLEARED_KNOBS` and extends to the post-merge and driver scrubs
- **hands-off** `TOOL-dWitnessedBar-62` — the selection round trip, the floors, the README sentences, the tail sweep, the peer read and AC15, which the minors batch keeps lossless, makes able to red and answers by name (ids 4, 5, 6, 15, 16, 17, 20, 31, 32, 42, 45)

## 4. Design

### Why two units and not one

M6's three clauses hold between this unit and `TOOL-dWitnessedBar-57`. Write sets: this unit's are the
paths below; unit 57's are under `tools/lib/`, `tools/memory-tree/` (but its hygiene suite and README),
`tools/codebase-map/`, `tools/govkit/`, `tools/runlog/`, `tools/drift-audit/`, `tools/check-spec-tokens.py`,
`regen.py` and `measure_legs.py`; none intersect. Contracts: unit 57's gate-health item reads the
selection file `select --rev` writes, which this unit leaves alone. Shared records: neither writes
`memory/DECISIONS.md`, a backlog shard, the run-state file or a generated index.

### Evidence

- `check_green_reuse` sets `force` only on a non-zero `reused_cache`, or a non-zero `reused` with an
  empty `reused_cache` (`.githooks/pre-push:1549-1559`).
- The hook clears `GATE_DOCS_BASE` for every bar (`:1857-1858`) and the class check lists it inert
  (`.githooks/pre-push.test.sh:1592-1593`, `:1617`); `check_knob_classes` reds an unclassified knob
  (`:1619-1629`).
- `base_from` (`run-gates.sh:3485`) records `GATE_BASE` for an explicit and an inherited base alike.
- `derive_temp_path` names a temp `<dest>.<n><n>.tmp` under `SRANDOM`, else `mktemp -u "<dest>.XXXXXXXX"`
  (`run-gates.sh:782`).
- `git verify-tag --raw` prints the good-signature line on stderr with rc 0 and nothing on stdout
  (the report's id 20 reproduction; unit 43 §4 Evidence names the line).

### The selection round trip (S1 to S3)

```
runner: for each row of GATE_SELECTION's file: strip one trailing \r; accept iff 4 TAB fields,
        field 1 == held, field 3 a held source, field 2 a manifest leg; else ignored += 1
        canonical = accepted rows, each "held\t<leg>\t<source>\t<note>\n"
        selection <git hash-object of canonical> | none ; selection.<n> <leg>\t<source>\t<note>
        selection_ignored <ignored>
hook:   rebuild = for n in 1..: "held\t" + value(selection.<n>) + "\n"; hash; compare
```

### Inventory

Minted: the per-tree key `selection_ignored`; the plants `peer-tip-missing` and `peer-no-ssh-keygen`;
the witness value `inherited` of `base_from`. Naming cells: each is asked of
`python tools/lexicon/lexicon.py --suggest <name>` at the pass.

### Migration

A per-tree record written between unit 41's pass and this one joins `selection.<n>` with ` · `; its
rebuild hashes differently and it is refused once, so the first push of such a tree runs its bar.

### Rollout

Live at landing, after every other unit of the build, concurrent with `TOOL-dWitnessedBar-57`.

### Files touched (estimate)

- `tools/run-gates/run-gates.sh`
- `.githooks/pre-push`
- `.githooks/pre-push.test.sh`
- `tools/run-gates/verdict_backends.py`
- `tools/run-gates/keep_tails.py`
- `tools/run-gates/run-gates.evidence.test.sh`
- `tools/run-gates/run-gates.gov.test.sh`
- `tools/run-gates/adopt-run-gates.test.sh`
- `tools/memory-tree/check-memory-hygiene.test.sh`
- `tools/run-gates/README.md`
- `tools/memory-tree/README.md`

### Alternatives rejected

- **One unit for all 44 minors.** M4 admits two where M6's clauses hold, and they hold.
- **Refuse ` · ` in a note at write time (id 2's other option).** A note is free text a quarantine row
  copies from an ask; the TAB form needs no refusal.
- **One shared Python predicate the hook calls (id 15's first option).** The hook ships verbatim and
  sources no kit (`.githooks/pre-push:1300`); a parity arm holds the two copies instead.

## 5. Production-readiness checklist

- security — S6, S7 and S8 close a keyless and a cross-reader adoption; S9 keeps a pusher's environment
  from holding a push bar's leg; S15 never reports a probe failure as an owner's choice.
- perf / scale — one more key per record; one `stat` per tail temp.
- error / empty / loading states — S3 counts what it ignores; S15 names every failure class.
- observability — S10 puts the inherited base on the record; S13 and S14 name their seams.
- risks — S1 refuses records written under the ` · ` join once (§4 Migration).
- testing — AC1 to AC18 by plant, fixture and probe; the arms of §7 at the close.
- migration — §4.
- user docs — S20; `help/verdict-backends.md` gains S15's `DEAD PROBE` causes.

## 6. Acceptance criteria

- **AC1** — When the runner makes a full run in a clean scratch clone with `GATE_SELECTION` naming a CRLF
  file whose one `quarantine` row's note holds ` · `, `awk -F'\t' '$1=="selection.1"{print NF}'` over the
  per-tree record prints 4, `selection` equals `git hash-object` of the LF canonical text, the LF twin of
  the file yields the same `selection`, and `.githooks/pre-push` adopts the record where R derives the row.
  Red when: a note's ` · ` or a CR changes the rebuilt hash, so a genuine GREEN is refused.
  fixture: a scratch clone under `%TEMP%/<short-name>`; the tree holds none.
- **AC2** — When the selection file also holds a three-field row and a row whose source is `bogus`, the
  record holds one `selection.<n>`, `selection_ignored 2`, and a `selection` hashed over the accepted row.
  Red when: an ignored row enters the hash, so the hook and `select --check` read different rows.
- **AC3** — When `.githooks/pre-push` runs over unit 4's AC4 plant and unit 40's both-at-0 plant as
  amended, each is adopted, and `grep -c 'selection.none' .githooks/pre-push.test.sh` prints at least 2.
  Red when: an earlier unit's adopt plant lacks a key the hook now requires.
- **AC4** — When `.githooks/pre-push` runs over a scratch clone whose push takes the inherited-green
  branch, a fixture leg printing its environment shows `GATE_BASE_FROM=inherited`, and
  `ls <common-dir>/gate-verdict/` holds no `.scoped` file for the tree.
  Red when: the hook omits the export, so the decline never fires on a real push.
- **AC5** — When the hook meets a GREEN per-tree record carrying neither `reused` nor `reused_cache`, it
  runs the bar and names the missing pair.
  Red when: the keyless branch is deleted, so `check_green_reuse` adopts the record.
- **AC6** — When `python verdict_backends.py --fixture --plant <case>` runs in `tools/run-gates/` for each of
  `reused-cache`, `reused-alone`, `no-pair`, `no-selection`, `edited-selection` and `underived-selection`,
  `read --backend local-hook` prints `NONE`; for `clean` it prints `GREEN`; and the hook's decision over
  each plant agrees.
  Red when: the local-hook reader stands on `verdict GREEN` alone.
- **AC7** — When `check_knob_classes` runs over the built runner, it prints nothing, and a push whose
  caller sets `GATE_BASE_FROM=inherited` on a full decision writes its record.
  Red when: either knob is unclassified, or a caller's value reaches the bar.
- **AC8** — When a scoped run is made with `GATE_BASE_FROM=inherited`, `grep -P '^base_from\t'` over its
  run record prints `GATE_BASE` and `inherited`, and the decline line names `base_from`.
  Red when: the record cannot show why no verdict was written.
- **AC9** — When unit 51's AC24 fixture runs with both verdicts aged 31 days, the B-named one survives A's
  sweep and the unnamed one is removed.
  Red when: a sweep restricted to `RUNROOT` passes.
- **AC10** — When `python keep_tails.py --selftest` runs in `tools/run-gates/` with a tail holding an ANSI
  colour sequence, a lone CR, a NUL and 3000 invalid bytes, the stored record holds none of the three raw
  bytes, measures at most 8192 bytes of tail, and its hash equals the stored bytes'.
  Red when: a control byte is stored raw or the tail exceeds the bound.
- **AC11** — When the tail writer runs with `SRANDOM` unset and its temp is left behind aged past
  `TAIL_GRACE_S`, the sweep removes it; a fresh one survives; an aged `.tmp` temp is removed too.
  Red when: a suffixless temp is kept as a tail.
- **AC12** — When `grep -n 'reuse cache' tools/run-gates/run-gates.sh` runs, it names a comment beside
  the tail sweep and one beside the per-tree verdict prune, each citing the 30-day `cut`.
  Red when: the seam record says no age prune exists.
- **AC13** — When `--plant peer-tip-missing` runs, `read --backend peer-node` prints `DEAD PROBE` naming
  the absent tip; under `--plant peer-no-ssh-keygen`, with no `ssh-keygen` on `PATH`, `DEAD PROBE`; under
  `--plant peer-unsigned`, `NONE` `unsigned`; and `grep -n 'mkstemp' verdict_backends.py` names the
  signer file.
  Red when: a probe failure reads as an owner's choice or a peer's fault.
- **AC14** — When `--plant peer-signed` runs, node a reads `GREEN` naming principal `b`; with the reader
  re-pointed at stdout, it reads `NONE`.
  Red when: the principal is parsed from stdout, so every signed tag reads unsigned.
- **AC15** — When `python -c "import json, sys; print(any(r['name'] == sys.argv[2] and sys.argv[3] in ' '.join(r['argv']) for r in json.load(open(sys.argv[1], encoding='utf-8'))))" tools/gate-legs.json 'run-gates gov canary' run-gates.gov.test.sh`
  runs, it prints `True`, and `grep -cE 'peer-(swapped-manifest|signed|unsigned|self-tag)' tools/run-gates/run-gates.gov.test.sh`
  prints at least 4.
  Red when: the plants sit in a suite no named leg runs.
- **AC16** — When the main loop tests at the close for `guard.py`, the file TOOL-dDeclaredLoop-2 creates at
  the path S18 names, a present file makes AC3 of unit 43 run and exit 1 naming `verdict.peer.signers`; an
  absent one leaves unit 43's ledger line for AC3 reading `NOT OBSERVED` and naming `guard.py`.
  Red when: AC3 is recorded observed over a file that does not exist.
- **AC17** — When `grep -n '^FLOOR_ASSERTIONS=' <suite>` runs for each of S19's four suites, each value
  exceeds its base figure, and a `RAISED` comment names each unit whose arm it counts.
  Red when: an arm of those units can be deleted and its suite stays green.
- **AC18** — When `grep -n 'reused_cache\|selection_ignored\|TAIL_GRACE_S\|GATE_POLICY_FILE' README.md` runs
  in `tools/run-gates/` and `grep -n 'What an adopter receives' README.md` in `tools/memory-tree/`, each
  names its sentence or table.
  Red when: a promised doc edit is missing.

## 7. Gates

`measure-legs selftest` · `pre-push self-test` · `pre-push bar self-test` · `pre-push run-log line` · `run-gates canary` · `run-gates evidence` · `run-gates gov canary` · `run-gates adopter e2e` · `run-gates run-log line` · `memory-hygiene self-test` · `memory hygiene`

New arm: .githooks/pre-push.test.sh · covers AC3 AC4 AC5 AC6 AC7 · the amended adopt plants, the inherited-green export, the keyless record, the hook-against-local-hook parity and the two knob classes, staged red by deleting the keyless branch · none
New arm: tools/run-gates/run-gates.evidence.test.sh · covers AC1 AC2 AC8 AC9 AC11 · the CRLF and ` · ` selection, ignored rows, `base_from`, the aged B-named verdict and the suffixless temp, staged red by joining `selection.<n>` with ` · ` · FLOOR_ASSERTIONS raised by these assertions
New arm: tools/run-gates/run-gates.gov.test.sh · covers AC15 · unit 43's four peer plants run from the suite `run-gates gov canary` runs, staged red by taking one plant out of the suite · FLOOR_ASSERTIONS raised by these assertions
New arm: tools/run-gates/verdict_backends.py · covers AC6 AC13 AC14 · the local-hook and peer plants, staged red by reading stdout for the principal · none
New arm: tools/run-gates/keep_tails.py · covers AC10 · a tail holding controls and invalid bytes, staged red by skipping the escape · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec carrying nothing and derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of each repaired unit's clause. Most repaired units are
  themselves derived and carry none, so (b) has nothing to split; veto 1 discards it. RESOLVED (agent,
  2026-10-25, delegated): (a), rung 3, the precedent `TOOL-dDeclaredLoop-36` §8 F1 set.
  widens: none · relaxes: none
- **F2 — Which push class does `GATE_SELECTION` take (id 32's flagged knob)?** Unit 5 mints it and no
  spec decides. Options: (a) inert, the hook clearing it for every bar and setting it on no path today;
  (b) scrubbed, cleared just before a non-stub bar, so no later hook decision could set it; (c) left to a
  later build. (b) forecloses unit 5 S6 setting it at the push; (c) leaves the class check red at the
  close, which veto 1 discards. RESOLVED (agent, 2026-10-25, delegated): (a), rung 3, the
  `GATE_DOCS_BASE` precedent: a pusher's selection never holds a push bar's leg.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, promoted from the round-1 spec audit of units 40 to 51: 13 MEDIUM and
  7 LOW findings, batched.
- rev-2 · 2026-10-25 · §3 · the Edges block gains the hands-off bullet mirroring TOOL-dWitnessedBar-58's
  consumes-from edge and the hands-off bullet mirroring TOOL-dWitnessedBar-60's consumes-from edge and
  the hands-off bullet mirroring TOOL-dWitnessedBar-62's consumes-from edge, promoted by the round-1
  spec audit of units 52 to 57; nothing else moved.

## 10. Reuse audit

Each item extends the seam its finding names: unit 5's TAB row grammar for S1, the readers' CR strip for
S2, `check_bar_record` and `read_local_verdict` for S6 to S8, the `GATE_DOCS_BASE` clear and its class
line for S9, the `base_from` row for S10, `derive_temp_path` for S13, and the reuse cache's prune as the
named rejected seam for S14. `python tools/codebase-map/reuse_lookup.py "refuse a per-tree verdict record
the hook would not adopt"` ranked `tree`, `note`, `records` and `adopt`, generic stems none of which is a
verdict reader, so the per-item seams above are the record.

Recall terms used: `python tools/memory-recall/query.py "what did the round-1 audit of units 40 to 51 find at the verdict boundary" --terms "per-tree verdict selection reused_cache check_bar_record read_local_verdict GATE_BASE_FROM base_from tail sweep peer verify-tag floor"`
