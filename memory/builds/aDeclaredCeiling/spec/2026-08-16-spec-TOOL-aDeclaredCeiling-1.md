# TOOL-aDeclaredCeiling-1 — the size ceilings become one declaration with their history beside them

**Status:** SPECCED · rev-1 · 2026-08-16 · node a · Tier-2 · base 96141aed · streams tooling

## 1. Goal

`tools/check-template-size.sh` gates two files against two ceilings that live in two unrelated
places: `49152` as a shell default inside the gate, and `18432` as a positional in
`tools/gate-legs.json`'s kickoff leg. Neither carries the reasoning for its value. Replace both with
one declared, per-subject pin whose movements are justified beside the number, on the pattern
`.memory-tree.conf`'s `READ_PATH_CEILING` already sets.

## 2. Scope (IN)

- **S1 — the declaration.** A new `tools/template-size-limits.txt`: `<path>\t<bytes>` rows keyed by
  measured file, comments carrying each value's justification and every movement of it. Seeded with
  the two subjects that exist — the playbook template at 49152 and the kickoff engine at 18432 —
  and with the ceiling reversal's history, which today survives only in `memory/DECISIONS.md` and a
  spec nobody reads at the gate.
- **S2 — the resolution order.** `MAX_BYTES` becomes: positional `$2`, then the environment, then
  **the declared row for this subject**, then the existing hard default. The two override layers are
  untouched — `TOOL-aSiftedPlaybook-2`'s A5 arms them and the self-test needs them — so this inserts
  one layer and removes none. A subject with no declared row falls through to the default exactly as
  today.
- **S3 — the kickoff leg stops carrying its limit in argv.** With the declaration keyed by subject,
  `tools/gate-legs.json`'s `kickoff engine size <=18KiB` leg becomes
  `bash tools/check-template-size.sh skills/session-kickoff/SKILL.md` and the number comes from the
  row. This is the point of the unit: the split between "the template's ceiling is in the script"
  and "the engine's ceiling is in the manifest" is the thing being removed, and leaving the
  positional in place would declare one and hardcode the other.
- **S4 — the carriers that spell the argv.** `AGENTS.md`'s gate-suite bullet spells
  `tools/check-template-size.sh skills/session-kickoff/SKILL.md 18432` verbatim and moves with S3.
  The leg NAME (`<=18KiB`) is an inventory key claimed by `memory/map/features/playbook.md`; it is
  NOT renamed, because renaming a leg key trips the codebase-map coverage gate in both directions
  and this unit has no reason to pay that.
- **S5 — the govkit declaration.** `tools/template-size-limits.txt` is a new depth-1 path under
  `tools/`, which `tools/govkit/registry.toml` asserts. An `[[exempt]]` row lands in the same
  commit, beside the sibling rows for the gate, its self-test and the high-water record.
- **S6 — the arms.** `tools/check-template-size.test.sh` gains: the declared row is what a subject
  with no positional and no env resolves to; a subject with NO row still resolves to the hard
  default; the positional still beats the declaration; the environment still beats the declaration.
  Four arms, because a resolution order with four layers is exactly where an off-by-one layer hides.
- **S7 — the map dossier.** `memory/map/features/playbook.md`'s `[paths].globs` gains the new file,
  and its "Constraints & why" gains the declaration as the ceiling's home. The dossier currently
  says "The ceiling is a shell constant, not a declared pin" in its Gaps section — that gap closes
  here and the sentence moves out of Gaps rather than being deleted.

## 3. Non-goals (OUT)

- **Changing either ceiling's VALUE.** 49152 and 18432 are what they are; this unit changes where
  they are declared. `memory/DECISIONS.md` is append-only and `TOOL-aSiftedPlaybook-1`'s row records
  the reversal that set 49152 — it is cited by the new file, never rewritten, and no new decision row
  is minted because no decision is being taken.
- **Making the high-water record and the limits record one file.** They are keyed the same way and
  the symmetry is tempting. Rejected in §4: one is a measurement the gate WRITES and the other is a
  policy value a human writes, and a `--bump` that can silently move a ceiling is the failure mode
  the whole ratchet exists to avoid.
- **A general conf mechanism for gov's gates.** `.memory-tree.conf` exists and is sourced by the
  memory-tree kit; adding the playbook's ceiling to it would couple two kits that share nothing.
  Whether gov wants one repo-root conf per concern or one for everything is a real question and not
  this unit's.

## 4. Design

### Why a sibling file and not `.memory-tree.conf`

`.memory-tree.conf` is the memory-tree kit's project layer, sourced by that kit's engines. The
template ceiling is a playbook-gate policy value with no memory-tree consumer. Putting it there
would make an unrelated kit's conf the home of another kit's constant, which is the coupling the
install-prefix and kit-dogfood gates exist to keep out. The pattern being reused from
`READ_PATH_CEILING` is **a declared value with its movement history beside it**, not the specific
file it lives in.

### Why NOT one file with the high-water record

Both are `<path>\t<bytes>` keyed by measured file, and merging them would halve the new surface.
Rejected on the write asymmetry: `--bump` WRITES the high-water record by design, and a merged file
means one careless `--bump` silently rewrites a ceiling. The ratchet's entire value is that raising
a ceiling is a deliberate act visible in the diff; a mode that can do it as a side effect destroys
that. Two files, one written by the gate and one written only by a person.

### The resolution order, and the one thing that makes it observable

positional `$2` → `MAX_BYTES` env → declared row for this subject → hard default.

Four layers is one more than the gate has today, and `TOOL-aSiftedPlaybook-2`'s harness already
proved the danger: A1/A2/A4 deliberately run with NO override so they observe the SHIPPED value
rather than one the harness supplied. S6's arms extend that discipline downward — each arm pins
which layer won, not merely that some limit applied. An arm that only checks "the gate used 49152"
cannot tell the declaration from the default, and they will be equal on the day this lands, which is
exactly when the arm is written.

### Blast radius, measured

- `tools/gate-legs.json` — S3 changes one leg's argv. `_charter_mentions_every_leg` matches argv
  PATHS, not arguments (`tools/drift-audit/drift_signals.py`), so dropping `18432` does not move
  that signal. Confirmed by reading the probe rather than by running it and inferring.
- The leg NAME is unchanged, so codebase-map coverage and freshness see no key movement.
- `skills/session-kickoff/manifest-check.sh` — `tools/gate-legs.json` and
  `tools/check-template-size.sh` are both watched pathspecs, so a `last-audit` re-stamp rides this
  commit.
- `tools/govkit/govkit.py selfcheck` — S5, or the leg reds on the new depth-1 path.

### Files touched

| File | Change |
|---|---|
| `tools/template-size-limits.txt` | new — S1 |
| `tools/check-template-size.sh` | S2's layer, and its header's usage block |
| `tools/check-template-size.test.sh` | S6's four arms |
| `tools/gate-legs.json` | S3 — the kickoff leg's argv |
| `AGENTS.md` | S4 — the spelled command |
| `tools/govkit/registry.toml` | S5 |
| `memory/map/features/playbook.md` | S7 |
| `memory/guides/SESSION-KICKOFF.md` | the mandatory `last-audit` re-stamp |

### Rollout

One commit. S2 and S3 cannot separate: the moment the leg drops its positional, the declaration is
the only thing standing between the kickoff engine and the 49152 default, and a tree where those
land apart gates `SKILL.md` at 48 KiB.

## 5. Production-readiness checklist

- security — N/A. The gate reads one more tracked file and writes none.
- perf / scale — N/A. One `awk` over a file with two rows.
- a11y / i18n — N/A.
- error / empty / loading states — the declared file being ABSENT is the case that matters: it must
  fall through to the hard default with no error, because an adopter who copies the gate does not
  get gov's limits file. A malformed row for the subject under test is a NAMED failure on the
  pattern the high-water record already sets, not a `set -u` death. Both armed in S6.
- observability — the gate already prints the limit it used on every run; with four layers it should
  also be possible to tell WHICH layer won, and the OK line does not say. Accepted rather than
  fixed: adding a provenance token changes the output contract two other arms match on. Named here
  so the next reader knows it was a choice.
- risks — the real risk is the one §4 names: the declaration and the default are EQUAL on the day
  this lands, so an arm that does not distinguish them passes while the declaration is never read.
  S6's arms exist for that and one of them uses a value deliberately unequal to the default.
- testing + left-shift gates — S6, and every new `fail` branch enters `check-arms.py`'s population
  with its `ARMS_FLOORS` pair re-measured.
- migration / rollback — revert the commit. An adopter is unaffected: the gate is govkit-exempt and
  ships nowhere.
- user docs — `AGENTS.md` (S4) and the dossier (S7).

## 6. Acceptance criteria

- **AC1** — When `bash tools/check-template-size.sh` runs with no positional and no environment
  override, it reports a limit of 49152, and that value comes from the declared row: deleting the
  row changes the reported limit to the hard default. **Two observations, because they are equal
  today** — the second is what proves the declaration is read at all.
- **AC2** — When `bash tools/check-template-size.sh skills/session-kickoff/SKILL.md` runs with NO
  positional limit, it reports 18432. This is S3's whole point and it fails today.
- **AC3** — When a positional limit is passed, it wins over the declared row; when `MAX_BYTES` is
  set and no positional is given, it wins over the declared row. The two existing override layers
  are unmoved.
- **AC4** — When `tools/template-size-limits.txt` is absent, the gate exits 0 using the hard default
  and says nothing alarming. An adopter's copy has no limits file.
- **AC5** — When the declared row for the subject is non-numeric, `bash tools/check-template-size.sh`
  fails by NAME with its own message and a distinct exit code, not a shell error. Same contract the
  high-water record already has, on the file a person edits by hand.
- **AC6** — When `grep -n 18432 tools/gate-legs.json AGENTS.md` runs, neither spells it as a
  command argument any more; the leg NAME `kickoff engine size <=18KiB` is unchanged.
- **AC7** — When `python tools/codebase-map/test_codebase_map.py` runs, coverage and freshness are
  green with the new file claimed in `memory/map/features/playbook.md` and no inventory key moved.
- **AC8** — When `python tools/govkit/govkit.py selfcheck` runs it is green with
  `tools/template-size-limits.txt` declared.
- **AC9** — When `python tools/drift-audit/drift_report.py --check` runs,
  `handkept_inventories_disagreeing_with_source` still reports 0 at pin 0 after S3's argv change —
  the confirmation that §4's read of the probe was right.
- **AC10** — When `python tools/memory-tree/check-arms.py --report` runs, every new `fail` branch is
  ARMED and the `ARMS_FLOORS` pair equals the measured `<branches>:<armed>`.
- **AC11** — When `bash tools/check-template-size.test.sh` runs it exits 0, and each of S6's four
  arms reds under a mutation that removes the layer it pins.
- **AC12** — When `bash tools/run-gates.sh` runs, it is green.

## 7. Gates

- `bash tools/check-template-size.sh` and `bash tools/check-template-size.test.sh` — the subject.
- `bash tools/run-gates.test.sh` — the canary over the changed manifest.
- `python tools/codebase-map/test_codebase_map.py` — coverage + freshness.
- `python tools/drift-audit/drift_report.py --check` — the argv change, per AC9.
- `bash skills/session-kickoff/manifest-check.sh` — two watched pathspecs move; re-stamp.
- `python tools/memory-tree/check-arms.py` · `python tools/govkit/govkit.py selfcheck`.
- `bash tools/run-gates.sh` at the push boundary.

## 8. Open questions

none.

## 9. Revision log

- rev-1 · 2026-08-16 · initial draft. The follow-up as `TOOL-aSiftedPlaybook-1` §4 recorded it was
  "make the ceiling a declared pin". The design pass found the better framing: there are TWO
  ceilings and they live in two unrelated places, so the unit is not "move a constant" but "stop
  splitting one policy across a script and a manifest". S3 is the part the original follow-up did
  not ask for and is the part that makes the declaration worth having.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "declared byte budget pin justified beside its value"`
returned `tools/memory-tree/gotchas.py:declares` (fan-in 5, SEAM), `row_grammar.py:do_emit_pin`, and
the `row-grammar` dossier's `id_pattern(conf)` affordance. **The seam this unit extends is the size
gate's own three-layer resolution** (`tools/check-template-size.sh`, positional → env → default),
which the playbook dossier already publishes as a reuse affordance: "reuse for gating ANY file's
byte size on the merge bar … extend via one gate-legs.json entry passing the subject and its limit
positionally". This unit changes that affordance — the limit stops being passed positionally — so
S7's dossier edit is not bookkeeping, it is the affordance's own text going stale.

`python tools/memory-recall/query.py "why is a repo constraint declared in a conf file rather than
hardcoded in the gate that enforces it" --terms "declared pin conf ceiling budget shrink-only floor
ratchet constant gate justification movement recorded"` returned 40 hits. The useful ones are this
build's own rows and `memory/map/features/playbook.md:81`. **`READ_PATH_CEILING` — the prior art this
unit is modelled on — did not appear**, because it is declared in `.memory-tree.conf` at the repo
root and the corpus is rooted at `MEMORY_ROOT`. That miss is `TOOL-aDeclaredCeiling-2`'s subject; it
is recorded here as the live reproduction rather than as a gap in this unit's grounding, and the
prior art was read directly instead (`.memory-tree.conf:57-71`, fourteen lines of movement history
beside one number — the shape S1 copies).
