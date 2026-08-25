**Serves:** journal TOOL-dFramedEntrypoint-7

# Acceptance ledger — TOOL-dFramedEntrypoint-7

*Node d, 2026-08-25. The conformance pass, run over the population it can conform honestly.*

**Evidences:** TOOL-dFramedEntrypoint-7

- AC1 — `python tools/memory-tree/gen_build_index.py --survey` prints one row per tracked build
  README with its conformance and, for a non-conforming one, every slot it lacks and every heading
  outside the canon. It is the candidate report this criterion asks for; it ships as a verb of the
  generator rather than as a separate script, because a single-use script under a build folder would
  be a second implementation of a walk the generator already owns.
- AC2 — `python tools/memory-tree/gen_build_index.py --check-format` exits 0 with
  `heading canon BOUND on 1`, and this build's own README is that one. Its registry row moved from
  exempt to bound in the same commit as the file.
- AC3 — `git diff` — every authored block that left this build's README is accounted for: the two
  narrative paragraphs became the description slot, the evidence pointer moved into the parked-
  decisions slot as a pointer to the run-state file, and nothing was deleted without a destination.
  Zero unaccounted.
- AC4 — `exempt-pin` fell 62 to 61 and equals the measured exempt count; the pin is an equality and
  reds in both directions.
- AC5 — `python tools/memory-tree/gen_build_index.py --bump` then `--report`: every bound slot sits
  under its ceiling — 693/900, 435/500, 397/500, 720/1800, 480/1800 — and `git diff --stat` shows
  only `build-readme-slot-highwater.txt` changed, never the ceilings file.
- AC6 — the pass declines a terminal build by its DERIVED status, which is the front-matter `status:`
  key where a build declares one and otherwise the terminal status of every unit's own spec header. A
  build README carries no `**Status:**` header of its own; that is the spec grammar, and the criterion
  said so only after the round-2 audit corrected it.
- AC7 — `bash tools/memory-tree/check-memory-hygiene.sh` and the slot-contract leg are green with the
  bound count at 1, which is greater than zero. Until this unit the leg printed a NOTE saying it had
  graded nothing; that note is gone because the population is no longer empty.
- AC8 — `bash tools/unattended/unattended.sh --status dFramedEntrypoint` reports four parked
  decisions, each carrying its question, the options seen and the reason it was refused. None was
  deleted, and the parked-decisions slot of this build's README points at that file rather than
  restating them.

## The three staged breaks, on the bound file

`## Owner rulings` inserted — exit 1, `heading outside the canon`. That is the exact class the owner
named when they opened this build, refused by name on a real file.
A slot padded past its ceiling — exit 1, naming the slot, the measured bytes and the ceiling.
A slot grown past its high-water but under its ceiling — ADVISORY printed, exit 0 unchanged.

## The population, and what it is not

ONE README is bound: this build's own. The owner's fork-1 ruling seeds from the conformable subset
and reports the rest as still-exempt, and the honest conformable subset at this moment is one file —
the one whose two judgement slots this session actually holds the material for. Conforming another
build's README means authoring its expected improvements and its detriments, which nobody wrote at the
time and which S6's own reasoning forbids inventing. The other 61 rows carry their reason and drain
when their owners conform them.

That is a smaller seed than the twelve live builds F1 contemplated, and it is the F1 recommendation
applied literally rather than optimistically: seed with what can be conformed without inventing a
judgement, and report the remainder.
