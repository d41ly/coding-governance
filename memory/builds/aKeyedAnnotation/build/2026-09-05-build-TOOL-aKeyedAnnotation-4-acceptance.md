<!-- **Serves:** journal TOOL-aKeyedAnnotation-4 -->
**Serves:** journal TOOL-aKeyedAnnotation-4

# aKeyedAnnotation unit 4 — acceptance ledger

**Evidences:** TOOL-aKeyedAnnotation-4

- AC1 — `python tools/codebase-map/reuse_lookup.py` — a candidate sourced from a dossier with a
  non-empty decisions list prints them on a line of their own; one from an empty dossier prints no
  clause at all rather than an empty one. Observed on a real query, which returned two such
  candidates and no empty clauses.
- AC2 — `python tools/codebase-map/test_codebase_map.py` — the new check reports the measured count
  against a pin equal to that measurement and exits 0. Authored in the template sibling and copied to
  this path, per S2.
- AC3 — `python tools/codebase-map/test_codebase_map.py` — blanking the decisions list on a dossier
  that carries several ids REDS the check, naming the count, the pin and the offending features;
  restoring it returns exit 0. Both readings taken, then restored.
- AC4 — `python tools/codebase-map/test_codebase_map.py` — the check asserts a non-empty dossier
  population before reporting any count, so a map root holding none is a named refusal rather than a
  perfect score.
- AC5 — AMENDED, because the mechanism it names does not exist. `tools/codebase-map/gen_map.py`
  scaffolds only the FOUNDATION file, and that is the ONE file the dossier loader excludes from the
  population the new check grades — so annotating it, which is what this unit did first, put the
  guidance where no reader the check could red would ever see it. There is no feature-dossier
  scaffolder to fix. The guidance now sits beside the check itself, in the module that reads the
  population, where a dossier author writing a new one is actually looking. The FOUNDATION skeleton
  is left as it was rather than carrying a comment that would count as the mechanism.
- AC6 — `git grep -w -F` against the memory root for the ONE id this unit added. It resolves to a
  decision row that governs that dossier directly — the ruling that put the build method in the
  memory-tree kit and made it ride the parity leg as a pair row, which is the same seam unit 1
  extended. One id, verified by reading the row rather than by pattern-matching the slug. Sixteen
  dossiers stay empty because this build did not read their governing records, and a guessed id
  resolves, which makes it worse than a visibly empty list.
- AC7 — deferred to the closing bar, which is where a full-bar criterion binds. The diff-scoped gates
  were green at this unit's commit: memory hygiene, spec tokens, codebase-map coverage, drift-audit
  records, corpus ids, the deployer selfcheck and kit versions.
- AC8 — `python tools/codebase-map/selftest.py` — the decisions clause is asserted inside the arm
  that already builds a fixture with NO project-side extractor, and that arm now asserts the absence
  of one explicitly. Passing there IS the portability observation, which is why this extends the
  existing arm rather than adding a second one that would rebuild the same fixture.
- AC9 — `python tools/drift-audit/drift_report.py --check --base-ref HEAD` — the ratchet mechanism
  observed on this build's other new pin, both ways: an unmarked raise REDS naming both values, and a
  marked one clears. The row for THIS pin is registered the same way and in the same list. It cannot
  be observed on this branch for the reason unit 3's ledger records: the ratchet skips a key its base
  ref does not carry, so a pin is unratcheted on the branch that introduces it.
- AC10 — `cmp tools/codebase-map/test_codebase_map.py tools/codebase-map/test_codebase_map.template.py`
  — identical after the change.

## Two documented checks, written down rather than waved

Neither has a proportionate machine form, so §7's rule applies: an exemption is recorded with
its compensating check or it is not an exemption.

- **A dossier-shaped repair names the POPULATION the check reads, not the file the edit
  touched.** S4's honesty comment first landed in the scaffolder's FOUNDATION skeleton, which
  is the one file the dossier loader excludes from the population the new check grades — so the
  guidance could never reach a reader the check would red. It now sits beside the check itself.
  The criterion should have named the population; that is the check.
- **A unit that changes the reuse audit's output SHAPE updates its agent-facing doc in the same
  commit.** The decisions clause is a second line per candidate, and that doc still described a
  candidate as exactly one line. Nothing breaks and no predicate is proportionate, so this is a
  Definition-of-Done item on the codebase-map dossier rather than a leg.

## What this unit broke on its way past, and did not absorb

Appending to the kit conf silently laundered another build's broken citation. A live spec of the
`aMendedLedger` build cites that conf by line number, naming a line eleven rows below the key it
describes. The citation used to point PAST end-of-file, so the spec-token leg flagged it and a waiver
row tolerated it as another build's problem; nine added lines made the named line exist, the leg went
quiet, and the waiver went stale. A wrong citation became an invisible one.

The stale waiver is dropped, which the registry permits because it only ever shrinks. The class is
filed as a backlog row rather than fixed here: a path-plus-line citation is validated for the line
EXISTING and never for what is on it, so any append to a cited file can launder a broken reference.
