# TOOL-dWitnessedBar-19 — acceptance ledger

**Serves:** journal TOOL-dWitnessedBar-19

This pass ran no merge bar, no self-test suite and no gate leg. The role hook refused
`govkit.py selfcheck` when the pass tried it in a scratch clone. Every criterion below was checked on
node d on 2026-11-19 by probing the unit's own code: `python -c` calls, the canary's key-set
predicate cut out of `run-gates.test.sh` and run alone, and `govkit.py intake` and `apply` from a
scratch clone holding this pass's changes as a commit, writing into a scratch adopter under
`%TEMP%`. The close still owes: selfcheck 7h over the tree and over AC2, AC3, AC4 and AC6's plants,
the `govkit selftest` runs h and i and its PU1 pair, the RED-first observation of section 7's
`New arm:` line, and every leg that section names.

**Evidences:** TOOL-dWitnessedBar-19
- AC1 — `LEG_KEYS` — the criterion's `git grep` printed three lines. The first is the one `LEG_KEYS`
  line of `tools/run-gates/run-gates.test.sh`, which holds `purpose`. The second is
  `LEG_KEY_FLOORS = {"tag": (1, 51), "purpose": (1, 52)}` in `tools/govkit/govkit.py`. The third
  is arm 1a's control row `{"name":"a",...,"purpose":"checks a"}`, a fixture and not a key set.
  `git grep PURPOSE_FLOOR -- tools` printed nothing. Run alone, the key-set predicate passed the
  control row and the real manifest with the file's own `LEG_KEYS`, and failed both with `purpose`
  cut from it. It failed the near-miss `purposes` either way. run-gates moves 1.51 -> 1.52, its
  README marker with it, and the canary floor moves 458 -> 459.
- AC2 — `selfcheck` — not run: the role hook refuses it in a pass, so the close owes it. A probe
  over `tools/gate-legs.json` found 198 rows (DERIVED), each carrying a one-line string purpose of
  1 to 60 characters (longest 60) with no leading or trailing space. The shape arm measures `len()`
  of the string, which counts characters. The selftest's run h plants 61 `x`s. Its run i plants 60
  `é`s and asserts the shape arm is silent on them.
- AC3 — `selfcheck` — not run: owed to the close. The same probe found 198 distinct purposes
  across 198 rows (DERIVED). Run h gives `template size <=48KiB` the purpose of `charter size` and
  asserts the line naming both legs.
- AC4 — `purposes:` — not run: owed to the close. 7h's note prints
  `purposes: <n> declared · <m> pending`. On this tree `<n>` is 198, `<m>` is 0, and the leg count is
  198 (all DERIVED from `tools/gate-legs.json`). Run h deletes the purpose of `build-method size`, an
  `[[exempt_leg]]` leg, and asserts the presence-arm line naming it.
- AC5 — `[]` — the criterion's `python -c`, run over
  `2026-11-19-build-TOOL-dWitnessedBar-19-purpose-review.md`, printed `[]`. A probe resolved all 198
  `path:line` cites: each names a file `git ls-files` lists and a line inside it, with the record
  generated after every edit landed. 35 rows come from step 1, 16 from step 2, 147 from step 3 and
  none from step 4 (DERIVED).
- AC6 — `selfcheck` — not run: owed to the close. A `tomllib` probe joined the 70 descriptor
  `[[gate_leg]]` rows in the 27 descriptors to the manifest by name and found 0 disagreements on
  `purpose`. The agreement arm compares presence too, and its line names the entry, the leg and both
  values. Run i stages a disagreeing purpose on `pre-push bar self-test` and asserts that line.
- AC7 — `purpose-pending.txt` — the record's "Put to the owner" section lists N = 0 legs (DERIVED).
  No pending population, `[[ledger]]` row, `.gitattributes` line or ask row was written, and
  `git ls-files -- '*purpose-pending.txt'` prints nothing. With no population, presence has no
  exception list. The criterion's stale-row plant needs a pending file, and none exists at N = 0, so
  it has no subject here.
- AC8 — `apply` — the scratch adopter got run-gates and gate-lint from a clone holding this pass as
  a commit. Its runner read `KIT_RUN_GATES_VERSION=1.52`, and all 8 emitted rows of its
  `gate-legs.json` carried their descriptor's purpose. The adopter's runner was then set to 1.51, and
  `apply --kits gate-lint` re-emitted the five gate-lint rows with no `purpose` key. Both applies
  printed the same three problems an install of the base commit prints: the three shell-hygiene legs
  are red in an empty target. That is unrelated to this unit.
