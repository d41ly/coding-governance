# TOOL-dWitnessedBar-56 — the round-1 audit of units 40 to 51, verdict-boundary minors batched: a lossless selection, one adoption rule on both readers, honest peer reads, and floors under the new arms

**Status:** CLOSED · rev-5 · 2026-11-20 · node d · Tier-2 · base cdfbd1cf · streams tooling · order 32 · advances TOOL-dWitnessedBar-31

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md) | journal | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-54 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-57 TOOL-dWitnessedBar-58 TOOL-dWitnessedBar-59 TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-61 TOOL-dWitnessedBar-62 TOOL-dWitnessedBar-63 TOOL-dWitnessedBar-64 TOOL-dWitnessedBar-65 TOOL-dWitnessedBar-66 TOOL-dWitnessedBar-67 TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-71 TOOL-dWitnessedBar-72 TOOL-dWitnessedBar-73 TOOL-dWitnessedBar-74 TOOL-dWitnessedBar-75 TOOL-dWitnessedBar-76 TOOL-dWitnessedBar-77 TOOL-dWitnessedBar-78 TOOL-dWitnessedBar-79 TOOL-dWitnessedBar-80 TOOL-dWitnessedBar-81 TOOL-dWitnessedBar-82 TOOL-dWitnessedBar-83 TOOL-dWitnessedBar-84 TOOL-dWitnessedBar-85 TOOL-dWitnessedBar-86 TOOL-dWitnessedBar-87 TOOL-dWitnessedBar-88 TOOL-dWitnessedBar-89 TOOL-dWitnessedBar-90 TOOL-dWitnessedBar-91 TOOL-dWitnessedBar-92 TOOL-dWitnessedBar-93 TOOL-dWitnessedBar-94 TOOL-dWitnessedBar-95 TOOL-dWitnessedBar-96 TOOL-dWitnessedBar-97 |
| [2026-10-25-build-TOOL-dWitnessedBar-52-round2-fix-return.md](../build/2026-10-25-build-TOOL-dWitnessedBar-52-round2-fix-return.md) | research | TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-57 |
| [2026-10-25-build-TOOL-dWitnessedBar-56-deviation-561.md](../build/2026-10-25-build-TOOL-dWitnessedBar-56-deviation-561.md) | deviation | — |
| [2026-10-25-build-TOOL-dWitnessedBar-56-deviation-562.md](../build/2026-10-25-build-TOOL-dWitnessedBar-56-deviation-562.md) | deviation | — |
| [2026-10-26-build-TOOL-dWitnessedBar-56-deviation-563.md](../build/2026-10-26-build-TOOL-dWitnessedBar-56-deviation-563.md) | deviation | — |
| [2026-11-19-build-TOOL-dWitnessedBar-56-1-acceptance-ledger.md](../build/2026-11-19-build-TOOL-dWitnessedBar-56-1-acceptance-ledger.md) | journal | — |
| [2026-11-19-build-TOOL-dWitnessedBar-56-1-builder-return.md](../build/2026-11-19-build-TOOL-dWitnessedBar-56-1-builder-return.md) | journal | — |
| [2026-11-20-build-TOOL-dWitnessedBar-56-red-fix-138.md](../build/2026-11-20-build-TOOL-dWitnessedBar-56-red-fix-138.md) | red-fix | — |
| [2026-11-20-build-TOOL-dWitnessedBar-56-red-fix-139.md](../build/2026-11-20-build-TOOL-dWitnessedBar-56-red-fix-139.md) | red-fix | — |
| [2026-11-20-build-TOOL-dWitnessedBar-56-red-fix-140.md](../build/2026-11-20-build-TOOL-dWitnessedBar-56-red-fix-140.md) | red-fix | — |
| [2026-11-20-build-TOOL-dWitnessedBar-56-red-fix-141.md](../build/2026-11-20-build-TOOL-dWitnessedBar-56-red-fix-141.md) | red-fix | — |
| [2026-10-25-prompt-TOOL-dWitnessedBar-1-parents-crosscheck.md](../prompts/2026-10-25-prompt-TOOL-dWitnessedBar-1-parents-crosscheck.md) | research | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-84 |
| [2026-10-25-prompt-TOOL-dWitnessedBar-52-round2-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dWitnessedBar-52-round2-fix-brief.md) | research | TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-57 |
| [2026-10-26-prompt-TOOL-dWitnessedBar-1-parents-reground.md](../prompts/2026-10-26-prompt-TOOL-dWitnessedBar-1-parents-reground.md) | research | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-51 |
| [2026-11-19-prompt-TOOL-dWitnessedBar-56-build-brief.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-56-build-brief.md) | journal | — |
| [2026-11-19-prompt-TOOL-dWitnessedBar-56-reground-brief.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-56-reground-brief.md) | journal | — |
| [2026-11-19-prompt-TOOL-dWitnessedBar-56-reground-spec-writer.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-56-reground-spec-writer.md) | journal | — |
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

Re-grounded at HEAD `60b2d421a`, past every unit through order 31. The units this one consumes from
landed eight of its items as they built: S2, S4, S5, S6, S11, S16, S17 and S18 each say so, build
nothing, and keep the criterion that observes the landed code.

## 2. Scope (IN)

- **S1** — id 2. A `selection.<n>` value is the accepted row with its `held` field cut and its TABs kept:
  `<leg><TAB><source><TAB><note>`, and `<TAB><mode>` where the row carries `TOOL-dWitnessedBar-30`'s
  fifth field. It replaces the ` · ` join the runner writes today
  (`tools/run-gates/run-gates.sh@e410947a:3155`). The hook rebuilds each canonical row as `held<TAB>`
  plus the value, in place of turning ` · ` back into a TAB in `.githooks/pre-push#check_tree_selection`
  (`.githooks/pre-push@089533f9:1842`), so a ` · ` in a note round-trips. The plants that write or
  compare the joined form move to the TAB form: `.githooks/pre-push.test.sh#write_bg_selection`, its
  `seledit` case (`.githooks/pre-push.test.sh@2b7e4815:2544`), and unit 41's AC1 arm
  (`tools/run-gates/run-gates.evidence.test.sh@588b08cf:740`). `tools/loop/loop_transition.py` reads the
  record's `verdict` key alone and is outside the population. Observed by AC1.
- **S2** — id 16. Present at HEAD: the runner's selection loop cuts one trailing CR from each line
  before it gathers or hashes it (`tools/run-gates/run-gates.sh@e410947a:3150`), as the record readers
  cut it (`tools/run-gates/run-gates.sh@e410947a:2573`), so a CRLF selection file hashes as its LF
  twin. This pass builds nothing for it. Observed by AC1.
- **S3** — id 47. The canonical text is the rows the runner accepted, and only those: four or five TAB
  fields counted on the CR-cut line, the first `held`, a fifth if present `hold` or `run`, a source of
  `quarantine` or `level`, and a leg the manifest carries, the field rule
  `tools/run-gates/verdict_flow.py#read_selection` applies. Today the runner keeps an ignored row in the
  text (`tools/run-gates/run-gates.sh@e410947a:3120-3124`) and accepts a three-field row. Every other
  row is left out of the text and the `selection.<n>` keys and counted on the per-tree record as
  `selection_ignored <n>`; a blank or `#` line is no row and is not counted. So the hook and
  `select --check --selection` read the rows the runner held. Observed by AC2.
- **S4** — id 3. Present at HEAD: `.githooks/pre-push.test.sh#write_bg_verdict`, the helper every
  per-tree plant of the suite writes through (`.githooks/pre-push.test.sh@2b7e4815:2414`), carries
  `reused 0` and `reused_cache 0` (`TOOL-dWitnessedBar-40` §8 F3) and `selection none`
  (`TOOL-dWitnessedBar-41` S3), so unit 4's AC4 plant and unit 40's both-at-0 control are adopted. This
  pass builds nothing for it. Observed by AC3.
- **S5** — id 4. Present at HEAD: the hook exports `GATE_BASE_FROM=inherited` in its inherited-green
  branch (`.githooks/pre-push@089533f9:2530`), and the runner reads it and unsets it before any leg
  (`tools/run-gates/run-gates.sh@e410947a:2815-2817`), so no leg can print it. A push taking that branch
  runs a bar whose environment carries the knob and writes no `.scoped` record. `TOOL-dWitnessedBar-58`
  S1 and S2 observe that at the stub bar and at the runner boundary, and its S3 answers AC4. This pass
  builds nothing for it. Observed by AC4.
- **S6** — id 14. Present at HEAD: `.githooks/pre-push#check_tree_reuse` refuses a per-tree record
  carrying neither `reused` nor `reused_cache` in a branch of its own, before it calls
  `.githooks/pre-push#check_green_reuse`, which forces nothing when both are empty; both per-tree
  readers call it (`TOOL-dWitnessedBar-40` S4). This pass builds nothing for it. Observed by AC5.
- **S7** — id 15. `tools/run-gates/verdict_backends.py#read_local_verdict`, which stands today on its
  `tree` line and `verdict GREEN` alone, reads `NONE` for a record unit 40's predicates refuse: a
  non-zero `reused_cache`, a `reused` with no `reused_cache`, or neither key. Observed by AC6.
- **S8** — id 33. `read_local_verdict` reads `NONE` for a record unit 41's predicates refuse: no
  `selection` key, rows rebuilt as S1 states whose hash differs, or `verdict_flow.py select --check
  --selection` exiting 1 at the landed revision, `tools/policy/policy.py#derive_landed_revision`'s
  remote tip, which the hook reads as R. A landed revision that does not derive, or a `select --check`
  that cannot run, reads `DEAD PROBE`. A parity arm runs the hook's adoption and
  `read --backend local-hook` over the same plants. Observed by AC6.
- **S9** — id 32. The hook clears `GATE_BASE_FROM` and `GATE_SELECTION` for every bar, a STUB included,
  beside its clear of `GATE_DOCS_BASE` (`.githooks/pre-push@089533f9:2253-2254`), each joining
  `ENV_CLEARED` when it was set, and sets `GATE_BASE_FROM` only in its inherited-green branch. Both
  already sit in `BAR_INERT_KNOBS` with reason lines (`.githooks/pre-push.test.sh@2b7e4815:1886-1897`,
  §8 F2); the `GATE_SELECTION` line, which leaves the clear to this unit, is reworded to name it.
  Observed by AC7.
- **S10** — id 27. The run record header's `base_from` row
  (`tools/run-gates/run-gates.sh@e410947a:3808`) carries a third field `inherited` when `BASE_FROM`
  reads so, and unit 40's decline line (`tools/run-gates/run-gates.sh@e410947a:6237`) names that row,
  so the record says why no verdict was written. No reader parses the row: `git grep -n base_from`
  outside the runner names only unit 40's `base_from_seen` probe, DERIVED 2026-11-20. Observed by AC8.
- **S11** — id 48. Present at HEAD: unit 51's AC24 arm ages both verdicts 31 days through one
  `os.utime` (`tools/run-gates/run-gates.evidence.test.sh@588b08cf:3212-3229`), so only a sweep that
  reads B's run records keeps the B-named one. This pass builds nothing for it. Observed by AC9.
- **S12** — id 49. The keep's order in `tools/run-gates/keep_tails.py#run_keep`: decode with
  `errors='replace'` and mask runlog's secret shapes, as landed; escape each C0 control byte other than
  TAB and LF, CR included, and DEL as `\xHH`; re-cut the text to its last whole character within
  `tools/run-gates/keep_tails.py#TAIL_BYTES`; then fence it. The record's `Hash` keeps naming the tail
  file's bytes, which the keep checks against the file's name before it writes (§8 F3). The runner's cut
  at a whole UTF-8 character is `TOOL-dWitnessedBar-51` S34's, landed. Observed by AC10.
- **S13** — id 52. The landed writer stages each tail as `tools/run-gates/run-gates.sh#derive_temp_path`'s
  sibling of `<common-dir>/gate-tails/tail` (`tools/run-gates/run-gates.sh@e410947a:6074`):
  `tail.<n><n>.tmp` under `SRANDOM`, `tail.XXXXXXXX` from `mktemp -u` otherwise, and either name with
  `.cut` appended while it drops a split character (`tools/run-gates/run-gates.sh@e410947a:6077`). The
  sweep skips every name that is not hex (`tools/run-gates/run-gates.sh@e410947a:6335`), so a temp a
  crashed bar left is never removed. The sweep reads a file whose name opens `tail.` as a temp and
  unlinks one older than `TAIL_GRACE_S`, never keeping it as a tail; this supersedes unit 42's skip of
  temps. Observed by AC11.
  **Readers:** by name: `tools/run-gates/run-gates.sh`, whose sweep comment says a staging name is
  never swept, reworded here; `tools/run-gates/run-gates.evidence.test.sh`, whose unit 42 AC3 arm
  reads no `tail.*` temp after a run and still holds · by value: `tools/run-gates/README.md`, whose tail
  paragraph states the kept set and gains the temps (S20).
- **S14** — id 23. The tail sweep and the per-tree verdict prune each carry a comment naming the reuse
  cache's prune (`tools/run-gates/run-gates.sh@e410947a:5955-6026`) as the seam considered and
  rejected: it runs only when the cache block fires, keeps no set and swallows errors. Each comment says
  why the tail grace, `tools/run-gates/run-gates.sh#TAIL_GRACE_S`, is seven days against the cache's 30
  (its `cut`, `tools/run-gates/run-gates.sh@e410947a:6015`). Observed by AC12.
- **S15** — id 50. The failure map of unit 43 §4 "The read" landed in
  `tools/run-gates/verdict_backends.py#read_peer_verdict` and
  `tools/run-gates/verdict_backends.py#read_signer_principal`. A refused policy read, an `ls-remote` or
  `fetch` exiting non-zero (an advertised tip the fetch cannot bring in included), and a `verify-tag`
  exit with no recognised line (`ssh-keygen` absent included) read `DEAD PROBE`; `no signature found`
  reads `NONE` `unsigned`; `No principal matched` reads `NONE` `unknown key`. The allowed-signers file is
  made by `tempfile.mkstemp` under the common git dir and unlinked in a `finally`. What it lacks: a bad
  signature, git's `Signature verification failed` on standard error, reads `DEAD PROBE` today
  (reproduced 2026-11-20 over a tag whose message was edited after signing) and reads `NONE` naming the
  bad signature. The plants `peer-tip-missing`, `peer-no-ssh-keygen` and `peer-bad-signature` join
  `PLANTS`. Observed by AC13.
- **S16** — id 20. Present at HEAD: `read_signer_principal` reads the `Good "git" signature for
  <principal>` line from `verify-tag --raw`'s standard error, through
  `tools/run-gates/verdict_backends.py#run_git` with `both`; its standard output is empty. This pass
  builds nothing for it. Observed by AC14.
- **S17** — id 35. Present at HEAD: unit 43's four peer plants run in the verdict backends' plant loop
  of `tools/run-gates/run-gates.gov.test.sh` (`tools/run-gates/run-gates.gov.test.sh@81c01a2c:782-783`),
  the suite `run-gates gov canary` runs, and this unit's §7 names that leg. S7's, S8's and S15's plants
  join the same loop. Observed by AC15.
- **S18** — id 11. Present at HEAD: `tools/loop/guard.py` exists and holds `verdict.peer.signers` in
  `tools/loop/guard.py#OWNER_ONLY_KEYS`. Unit 43 rev-5 moved its AC3 onto the guard's
  `signers-owner-only` plant, and its acceptance ledger
  (`memory/builds/dWitnessedBar/build/2026-11-19-build-TOOL-dWitnessedBar-43-1-acceptance-ledger.md`)
  records AC3 observed by that plant's key-level refusal. This pass builds nothing for it. Observed by
  AC16.
- **S19** — id 37. Each floored suite an arm of units 40, 41, 42, 43, 45, 46 or 51 lands in, where that
  unit's pass left the floor where it was, raises its floor by the assertions those arms add, counted
  by reading, with a dated `RAISED` comment per unit (§4 "The floors"). Observed by AC17.
- **S20** — id 41. The README sentences units 40, 41, 42 and 46 promised landed with their passes:
  `tools/run-gates/README.md` "The verdict per tree" and its tail paragraph, and
  `tools/memory-tree/README.md`'s "What an adopter receives". Unit 44's is this unit's: the
  `MIGRATION NOTE` of `tools/run-gates/README.md` (`tools/run-gates/README.md@50d44089:1688-1692`) names
  the step reading `.githooks/gate-env.sh` and the file `GATE_POLICY_FILE` names, any other non-blank
  value written as `every-red`, the stricter of two values winning, and the conflict refusal, and points
  at `help/upgrade-steps.md` "Where `INHERITED_RED`'s value lives". This unit's own lines land in that
  README too: S1's TAB form, S3's `selection_ignored`, S10's `inherited` field and S13's temps.
  Observed by AC18.

## 3. Non-goals (OUT)

- Any high: units 52 to 55, one per id.
- The resolver, ledger and adopter minors: `TOOL-dWitnessedBar-57`.
- The round-1 minors ids 7 and 46, which wait with `TOOL-dWitnessedBar-28`: no item here needs them.
- The per-tree verdict prune's own staging temps, which `derive_temp_path` names the same way and the
  prune skips: no finding of the report names them.
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
- **hands-off** `TOOL-dWitnessedBar-68` — the `clean` plant and S7's reuse-pair refusal, on which the AC12 record is rebuilt so `read --backend local-hook` admits it and its repeated `reused_cache` decides the printed state (id 1 of the round-1 spec audit of units 66 and 67)

## 4. Design

### Why two units and not one

M6's three clauses hold between this unit and `TOOL-dWitnessedBar-57`. Write sets: this unit's are the
paths below, and unit 57's are the paths its own §4 Files touched names; none intersect but the
`last-audit` re-stamp of `memory/guides/SESSION-KICKOFF.md`, which each lists where it edits a watched
file. Contracts: unit 57's gate-health item reads the selection file `select --rev` writes, which this
unit leaves alone. Shared records: neither writes `memory/DECISIONS.md`, a backlog shard, the run-state
file or a generated index.

### Evidence

Read at HEAD `60b2d421a`, which holds every unit through order 31 landed. Every cited file is clean in
the working tree, and each line citation is pinned to the blob HEAD holds.

- The runner's selection loop (`tools/run-gates/run-gates.sh@e410947a:3146-3173`) cuts the CR, keeps
  every `held` line in the text whether it holds the row or ignores it, and joins each key's value with
  ` · `; it reads a row's fields with `read`, so a row of three fields reaches the hold.
- `.githooks/pre-push.test.sh#check_knob_classes` reds a runner knob that is in no class or in two;
  `GATE_BASE_FROM` and `GATE_SELECTION` sit in `BAR_INERT_KNOBS` alone.
- `git verify-tag --raw` prints its good-signature line, `No principal matched.` and
  `Signature verification failed: incorrect signature` on standard error and nothing on standard
  output, reproduced 2026-11-20 with throwaway `ssh-keygen` keys in a scratch repository.

### The selection round trip (S1 to S3, S8)

```
runner: for each line of GATE_SELECTION's file: cut one trailing \r; skip a blank or # line
        accept iff 4 or 5 TAB fields, field 1 == held, field 3 quarantine|level,
        field 5 absent|hold|run, field 2 a manifest leg; else ignored += 1
        canonical = the accepted lines, each LF-terminated
        selection <git hash-object of canonical> | none
        selection.<n> <the accepted line, "held\t" cut>
        selection_ignored <ignored>
hook:   rebuild = for n in 1..: "held\t" + value(selection.<n>) + "\n"; hash; compare
local:  the same rebuild, then select --check --selection at the landed revision
```

### The floors (S19)

Derived 2026-11-20 by joining each named unit's §7 `New arm:` lines to `grep -n '^FLOOR' <suite>` and
to the suite's `RAISED` comments. Each figure is the floor at HEAD, PINNED 2026-11-20.

| Suite | Floor at HEAD | Owed raise |
|---|---|---|
| `tools/run-gates/run-gates.evidence.test.sh` | 302 (`@588b08cf:319`) | unit 41's AC1 arm; units 40, 42 and 51 raised theirs |
| `tools/run-gates/run-gates.gov.test.sh` | 21 (`@81c01a2c:246`) | unit 43's four peer plants |
| `tools/run-gates/adopt-run-gates.test.sh` | 17 (`@6efa9461:231`) | unit 45's section 8 |
| `tools/memory-tree/check-memory-hygiene.test.sh` | 789 (`@3e185cca:5248`) | unit 46's scalar-pins arm, unit 51's AC2 arm |
| `tools/unattended/unattended.test.sh` | 3408, the effective pin (`@0f797c92:20544`) | unit 51's AC16 AC31 arm, with its region's `FLOOR_SHARD_<n>` |

Outside the population: `.githooks/pre-push.test.sh`, where units 40 and 41 land arms, carries no
assertion floor, and the `FLOOR` of `tools/lib/resolve-python.test.sh` is the python floor. Unit 51's
arms in `leg_factory.py`, `ratchet.py`, `resolve-python.test.sh` and `merge-rows.test.sh`, and unit
43's in `guard.py`, land in no floored suite.

### Inventory

Minted: the per-tree key `selection_ignored`; the third `base_from` field `inherited`; the local-hook
plants `reused-cache`, `reused-alone`, `no-pair`, `no-selection`, `edited-selection`,
`underived-selection` and `clean`; the peer plants `peer-tip-missing`, `peer-no-ssh-keygen` and
`peer-bad-signature`; and the keep self-test's `controls` case. Naming cells: each is asked of
`python tools/lexicon/lexicon.py --suggest <name>` at the pass.

### Migration

A per-tree record written between unit 41's pass and this one joins `selection.<n>` with ` · `; its
rebuild hashes differently and it is refused once, so the first push of such a tree runs its bar.
Reverting the pass restores the ` · ` join, and a record written under the TAB form is refused once the
same way.

### Rollout

Live at landing, at order 32 beside `TOOL-dWitnessedBar-57`, after every unit through order 31.
`TOOL-dWitnessedBar-28` stays unbuilt, and none of this unit's items reads it.

### Files touched (estimate)

- `tools/run-gates/run-gates.sh`: the selection loop and keys (S1, S3), `base_from` (S10), the tail
  sweep's temps and the two comments (S13, S14)
- `.githooks/pre-push`: S1's rebuild in `check_tree_selection`, S9's clears
- `.githooks/pre-push.test.sh`: S1's plants, S9's reason line, S8's parity arm
- `tools/run-gates/verdict_backends.py`: S7, S8, S15 and their plants
- `tools/run-gates/keep_tails.py`: S12 and its self-test case
- `tools/run-gates/run-gates.evidence.test.sh`: S1's arm form, the new arms and the floor
- `tools/run-gates/run-gates.gov.test.sh`: the plant loop and the floor
- `tools/run-gates/adopt-run-gates.test.sh`: the floor
- `tools/memory-tree/check-memory-hygiene.test.sh`: the floor
- `tools/unattended/unattended.test.sh`: the effective floor and the shard floor of unit 51's region
- `tools/run-gates/README.md`: S20
- `help/verdict-backends.md`: S15's bad-signature line, in "Registering a node's key"
- `memory/guides/SESSION-KICKOFF.md`: its `last-audit` re-stamp, since its `watch:` line names
  `tools/run-gates/run-gates.sh`

### Alternatives rejected

- **One unit for all 44 minors.** M4 admits two where M6's clauses hold, and they hold.
- **Refuse ` · ` in a note at write time (id 2's other option).** A note is free text a quarantine row
  copies from an ask; the TAB form needs no refusal.
- **One shared Python predicate the hook calls (id 15's first option).** The hook ships verbatim and
  sources no kit (`.githooks/pre-push@089533f9:538`); a parity arm holds the two copies instead.

## 5. Production-readiness checklist

- security — S7 and S8 close the reader that stood on records the hook refuses; S9 keeps a pusher's
  environment from holding a push bar's leg; S15 never reports a probe failure as an owner's choice.
- perf / scale — one more key per record; one `stat` per tail temp; one `select --check` per local-hook
  read of a record that held legs.
- error / empty / loading states — S3 counts what it ignores; S15 names every failure class.
- observability — S10 puts the inherited base on the record; S13 and S14 name their seams.
- risks — S1 refuses records written under the ` · ` join once (§4 Migration).
- testing — AC1 to AC18 by plant, fixture, grep and probe; the arms of §7 at the close; AC4 by
  `TOOL-dWitnessedBar-58`.
- migration — §4.
- user docs — S20; `help/verdict-backends.md` gains S15's bad-signature line.

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
- **AC3** — When `grep -n 'reused_cache.t0.*selection.tnone' .githooks/pre-push.test.sh` runs, it names
  the one plant line of `write_bg_verdict`, which unit 4's AC4 arm and unit 40's both-at-0 control write
  through.
  Red when: an earlier unit's adopt plant lacks a key the hook now requires.
- **AC4** — When `.githooks/pre-push` runs over a scratch clone whose push takes the inherited-green
  branch, the bar it runs receives `GATE_BASE_FROM=inherited`, and `ls <common-dir>/gate-verdict/` holds
  no `.scoped` file for the tree.
  Red when: the hook omits the export, so the decline never fires on a real push.
  fixture: `TOOL-dWitnessedBar-58`'s stub-bar and runner-boundary arms, order 33; this unit's line reads
  `NOT OBSERVED` naming that unit, whose S3 writes it observed.
- **AC5** — When the hook meets a GREEN per-tree record carrying neither `reused` nor `reused_cache`, as
  the `keyless` case of the suite's AC6-8 loop plants it (`.githooks/pre-push.test.sh@2b7e4815:2534-2555`),
  it runs the bar and names the missing pair.
  Red when: `check_tree_reuse`'s keyless branch is deleted, so `check_green_reuse` adopts the record.
- **AC6** — When `python verdict_backends.py --fixture --plant <case>` runs in `tools/run-gates/` for each of
  `reused-cache`, `reused-alone`, `no-pair`, `no-selection`, `edited-selection` and `underived-selection`,
  `read --backend local-hook` prints `NONE`; for `clean` it prints `GREEN`; and the hook's decision over
  each plant agrees.
  Red when: the local-hook reader stands on `verdict GREEN` alone.
- **AC7** — When `check_knob_classes` runs over the built runner, it prints nothing, and a push whose
  caller sets `GATE_BASE_FROM=inherited` on a full decision writes its record.
  Red when: either knob is unclassified, or a caller's value reaches the bar.
- **AC8** — When a scoped run is made with `GATE_BASE_FROM=inherited`, `grep -P '^base_from\t'` over its
  run record's `header` prints `GATE_BASE` and `inherited`, and the decline line names `base_from`.
  Red when: the record cannot show why no verdict was written.
- **AC9** — When unit 51's AC24 fixture runs with both verdicts aged 31 days, the B-named one survives A's
  sweep and the unnamed one is removed.
  Red when: a sweep restricted to `RUNROOT` passes.
- **AC10** — When `python keep_tails.py --selftest` runs in `tools/run-gates/`, its `controls` case, a
  tail holding an ANSI colour sequence, a lone CR, a NUL and 3000 invalid bytes (S12), writes one record
  whose fenced block holds none of the three raw bytes, holds `\x1b`, `\x0d` and `\x00` in their place,
  measures at most `TAIL_BYTES` inside the fence, and whose `Hash` names the tail file's bytes.
  Red when: a control byte is stored raw, the tail exceeds the bound, or the `Hash` names other bytes.
- **AC11** — When a run's sweep meets `<common-dir>/gate-tails/` holding a `tail.<n><n>.tmp` and a
  `tail.XXXXXXXX` temp aged past `TAIL_GRACE_S`, and a fresh `tail.*.tmp`, it removes both aged temps
  and keeps the fresh one.
  Red when: a temp is skipped as no hash, so an aged one is kept forever.
- **AC12** — When `grep -n 'reuse cache' tools/run-gates/run-gates.sh` runs, it names a comment beside
  the tail sweep and one beside the per-tree verdict prune, each citing the 30-day `cut`.
  Red when: the seam record says no age prune exists.
- **AC13** — When `python verdict_backends.py --fixture --plant peer-tip-missing` runs in
  `tools/run-gates/`, `read --backend peer-node` prints `DEAD PROBE` naming the ref the fetch could not
  bring in; under `--plant peer-no-ssh-keygen`, `gpg.ssh.program` pointing at an absent path,
  `DEAD PROBE`; under `--plant peer-bad-signature`, a tag node b signed whose message was edited after
  signing, `NONE` naming the bad signature; under `--plant peer-unsigned`, `NONE` `unsigned`; and
  `grep -n 'mkstemp' verdict_backends.py` names the signer file.
  Red when: a probe failure reads as an owner's choice, or a tampered tag reads as a probe failure.
- **AC14** — When `--plant peer-signed` runs, node a reads `GREEN` naming principal `b`; with
  `read_signer_principal` re-pointed at standard output, it reads no `GREEN`.
  Red when: the principal is parsed from standard output, so no signed tag stands.
- **AC15** — When `python -c "import json, sys; print(any(r['name'] == sys.argv[2] and sys.argv[3] in ' '.join(r['argv']) for r in json.load(open(sys.argv[1], encoding='utf-8'))))" tools/gate-legs.json 'run-gates gov canary' run-gates.gov.test.sh`
  runs, it prints `True`, and `grep -cE 'peer-(swapped-manifest|signed|unsigned|self-tag)' tools/run-gates/run-gates.gov.test.sh`
  prints at least 4.
  Red when: the plants sit in a suite no named leg runs.
- **AC16** — When `python guard.py --fixture --plant signers-owner-only` runs in `tools/loop/`, it exits 1
  with its one scenario held, its `--staged` scenario naming `verdict.peer.signers: owner-only`, and
  `grep -n 'AC3' memory/builds/dWitnessedBar/build/2026-11-19-build-TOOL-dWitnessedBar-43-1-acceptance-ledger.md`
  names that plant.
  Red when: AC3 is recorded observed over a file that does not exist, or over a refusal that names only
  the policy file's path, which the default `owner-only` gives for any agent write.
- **AC17** — When `grep -n '^FLOOR_ASSERTIONS=' <suite>` runs for each suite of §4 "The floors", the last
  value it prints exceeds that table's figure, a dated `RAISED` comment names each unit whose arm it
  counts, and `grep -n '^FLOOR_SHARD_' tools/unattended/unattended.test.sh` shows the shard holding unit
  51's arm raised by the same count.
  Red when: an arm of those units can be deleted and its suite stays green.
  figure: each base figure PINNED 2026-11-20 in §4 "The floors".
- **AC18** — When `grep -n 'selection_ignored\|GATE_POLICY_FILE' README.md` runs in `tools/run-gates/`, it
  names the selection paragraph and the migration note, `grep -c 'each TAB after it turned into' README.md`
  there prints 0, and `grep -n 'What an adopter receives' README.md` in `tools/memory-tree/` names its
  table.
  Red when: a promised doc edit is missing.

## 7. Gates

`measure-legs selftest` · `pre-push self-test` · `pre-push bar self-test` · `pre-push run-log line` · `run-gates canary` · `run-gates evidence` · `run-gates gov canary` · `run-gates adopter e2e` · `run-gates run-log line` · `memory-hygiene self-test` · `memory hygiene` · `kickoff-manifest ratchet` · `recall floor` · `recall floor arms`

`recall floor` and `recall floor arms` guard `memory/`, which holds the kickoff manifest this unit
re-stamps; `kickoff-manifest ratchet` carries no guard and grades the stamp on every bar.

New arm: .githooks/pre-push.test.sh · covers AC6 AC7 · the TAB-joined `selection.<n>` plants, the hook-against-local-hook parity over S7's and S8's plants, and the two knob clears, staged red by restoring the ` · ` join in `check_tree_selection` · none
New arm: tools/run-gates/run-gates.evidence.test.sh · covers AC1 AC2 AC8 AC11 · the CRLF and ` · ` selection, the ignored rows, `base_from`'s third field and the aged temps of both spellings, staged red by joining `selection.<n>` with ` · ` · FLOOR_ASSERTIONS raised by these assertions
New arm: tools/run-gates/run-gates.gov.test.sh · covers AC6 AC13 · S7's and S8's local-hook plants and S15's three peer plants joining the verdict backends' plant loop, staged red by reading `verdict GREEN` alone in `read_local_verdict` · FLOOR_ASSERTIONS raised by these assertions
New arm: tools/run-gates/verdict_backends.py · covers AC6 AC13 AC14 · the local-hook and peer plants, staged red by reading standard output for the principal · none
New arm: tools/run-gates/keep_tails.py · covers AC10 · the `controls` case, staged red by skipping the escape · none

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
- **F3 — Where does S12's escape live, now that the runner keeps a tail's raw bytes and the keep decodes
  them?** `TOOL-dWitnessedBar-51` S34 landed the whole-character cut in the runner and the decode, the
  mask and the fence in `tools/run-gates/keep_tails.py#run_keep`, whose record's `Hash` names the tail
  file's bytes. Options: (a) the keep escapes after its mask and re-cuts, the `Hash` still naming the
  file; (b) the runner escapes at its tail write through a python step per red leg, so the file holds
  the escaped text and its hash; (c) both. (b) leaves AC10's keep-side case, which plants the tail file
  directly, unescaped, and (c) holds one rule in two places; veto 1 discards both. RESOLVED (agent,
  2026-11-20, delegated): (a), the most feature-rich survivor under M3, no veto tripped.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, promoted from the round-1 spec audit of units 40 to 51: 13 MEDIUM and
  7 LOW findings, batched.
- rev-2 · 2026-10-25 · §3 · the Edges block gains the hands-off bullet mirroring TOOL-dWitnessedBar-58's
  consumes-from edge and the hands-off bullet mirroring TOOL-dWitnessedBar-60's consumes-from edge and
  the hands-off bullet mirroring TOOL-dWitnessedBar-62's consumes-from edge, promoted by the round-1
  spec audit of units 52 to 57; nothing else moved.
- rev-3 · 2026-10-25 · §3 · the Edges block gains the hands-off bullet mirroring TOOL-dWitnessedBar-68's
  consumes-from edge, promoted by the round-1 spec audit of units 66 and 67; nothing else moved.
- rev-4 · 2026-10-26 · S18 · AC16 · re-grounded on the cross-check record
  `2026-10-26-build-TOOL-dWitnessedBar-1-parents-crosscheck`, row 98: AC16 observes unit 6 S9's
  key-level `OWNER_ONLY_KEYS` refusal under `agents-with-reason`, not a trailer check, which
  `--staged` cannot make at pre-commit.
- rev-5 · 2026-11-20 · §1 · S1 to S20 · §3 · §4 · §5 · AC3 AC4 AC5 AC8 AC10 AC11 AC13 AC14 AC16 AC17
  AC18 · §7 · §8 F3 · §10 · re-grounded at HEAD `60b2d421a` per brief
  2026-11-19-prompt-TOOL-dWitnessedBar-56-reground-brief: S2, S4, S5, S6, S11, S16, S17 and S18 are
  present as landed, S4's `selection none` plants dropped; S1 and S3 carry unit 30's mode field and the
  field rule of `read_selection`; S8 checks at the landed revision; S12's escape lives in the keep (F3);
  S13 reads the writer's `tail.` temps; S15 narrows to the bad signature and three plants; S19's floors
  re-derived and re-pinned, `tools/unattended/unattended.test.sh` joining; S20 takes unit 44's migration
  note; Files touched gains `help/verdict-backends.md`, the unattended suite and the kickoff manifest's
  re-stamp and drops the memory-tree README; every line citation blob-pinned or cited by symbol.

## 10. Reuse audit

Each item extends the seam its finding names: unit 5's TAB row grammar and `read_selection`'s field rule
for S1 and S3, `check_bar_record` and `read_local_verdict` for S6 to S8 with
`tools/policy/policy.py#derive_landed_revision` for S8's R, the `GATE_DOCS_BASE` clear and its class
line for S9, the `base_from` row for S10, `run_keep` for S12, `derive_temp_path`'s names for S13, the
reuse cache's prune as the named rejected seam for S14, `read_signer_principal` for S15, and the gov
suite's plant loop for the new plants. `python tools/codebase-map/reuse_lookup.py "refuse a per-tree
verdict record the hook would not adopt"`, re-run at HEAD on 2026-11-20, ranked `tree`, `note`,
`records` and `adopt`, generic stems none of which is a verdict reader, so the per-item seams above are
the record.

Recall terms used: `python tools/memory-recall/query.py "what did the round-1 audit of units 40 to 51 find at the verdict boundary" --terms "per-tree verdict selection reused_cache check_bar_record read_local_verdict GATE_BASE_FROM base_from tail sweep peer verify-tag floor"`
