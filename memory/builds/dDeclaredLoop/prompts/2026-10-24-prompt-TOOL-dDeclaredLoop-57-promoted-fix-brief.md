**Serves:** research TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67

# Promoted-fix brief — the round-2 promotions, before their commit

Fix the eleven specs the round-2 spec audit's disposal added, `TOOL-dDeclaredLoop-57` to `-67`, so
`python tools/check-spec-tokens.py` names no dDeclaredLoop spec and `bash tools/memory-tree/check-memory-hygiene.sh
--only 12,25` prints no dDeclaredLoop line, changing nothing else.

- Each `[bar]` hit: a bar or suite is not an acceptance observation. Re-express the criterion as the observation of
  the unit's own code: the checker run on a staged break, a fixture, or a probe of the function. Where the
  criterion truly needs a suite arm, move it to a `New arm:` line in §7, which the main loop observes at the close.
- Each check-12 hit (an acceptance bullet naming no backticked witness): give the bullet the backticked command or
  file that observes it.
- Each check-25 hit (a §2 item that retires a named thing): add a `**Readers:**` clause, `by name:` every reader
  that spells the name (each found by `git grep -n` at HEAD) and `by value:` its value's readers or
  `NO VALUE READERS` and a reason; or, where the item retires nothing, reword it so it no longer reads as a
  retirement. The passing clauses in `TOOL-dDeclaredLoop-7`, `-11` and `-21` show the shape.
- The specs are uncommitted at rev-1, so edit them in place with no rev bump. Touch no deviation record and no spec
  numbered 1 to 56.
- Do not commit, do not stage, do not run the build-index generator. Re-run the hygiene checks (`--only 12,25`) and
  report each file changed and the dDeclaredLoop lines left.

## The hits, verbatim

- memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-67.md [bar] `resolve-python.test.sh` — a bar or suite is not an acceptance observation: observe the checker on a staged break, a --selftest flag or a fixture; name the suite under New arm:; the bar and the suites run once, after the build is complete
- memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-67.md [bar] `selftest.py` — a bar or suite is not an acceptance observation: observe the checker on a staged break, a --selftest flag or a fixture; name the suite under New arm:; the bar and the suites run once, after the build is complete
- memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-67.md [bar] `run-gates.sh` — a bar or suite is not an acceptance observation: observe the checker on a staged break, a --selftest flag or a fixture; name the suite under New arm:; the bar and the suites run once, after the build is complete
- memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-67.md [bar] `python selftest.py` — a bar or suite is not an acceptance observation: observe the checker on a staged break, a --selftest flag or a fixture; name the suite under New arm:; the bar and the suites run once, after the build is complete
- memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-67.md (acceptance bullets naming no backticked witness, required at/after SPEC_WITNESS_CUTOFF): 2026-08-15 -- AC29
- memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-58.md (§2 items that retire a named thing carry no **Readers:** clause; write **Readers:** then by name: and the readers that spell the name, then by value: and the readers of its value, or NO VALUE READERS and a reason): S3
- memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-66.md (§2 items that retire a named thing carry no **Readers:** clause; write **Readers:** then by name: and the readers that spell the name, then by value: and the readers of its value, or NO VALUE READERS and a reason): S4
