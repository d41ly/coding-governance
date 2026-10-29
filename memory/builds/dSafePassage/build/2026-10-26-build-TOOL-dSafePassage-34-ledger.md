**Serves:** journal TOOL-dSafePassage-34

# TOOL-dSafePassage-34 — acceptance ledger

The unit as built, at spec rev-4. `.memory-tree.conf` declares `SPEC_AC_ORDER_CUTOFF="2026-10-23"`
under a comment block in its siblings' form. `tools/check-spec-tokens.py` declares `AC_ORDER_KEY`
and reads it in `main` through `read_cutoff_key` beside the other four date keys, so a non-ISO value
refuses the run; nothing is graded by it yet, as §3's `TOOL-dSafePassage-41` bullet says.
`tools/check-spec-tokens.test.sh` gains one arm, the non-ISO refusal, and its floor 199 -> 200.
`memory/map/features/spec-tokens.md` names the key. `tools/drift-audit/drift_signals.py` raises
`cutoff_keys_armed` 36 -> 37 with its in-place comment. `memory/guides/SESSION-KICKOFF.md` is
re-stamped because `.memory-tree.conf` is on its `watch:` list.

HOW EACH CRITERION WAS OBSERVED. No gate, suite or bar ran in this pass. Each AC was observed on
node d (Windows) over this worktree or a scratch dir under the session scratchpad.

S3: TOOL-dSafePassage-8 reads `CLOSED · rev-5`, outside `LIVE`, so it needs nothing and its spec is
not written. S4: TOOL-aPacedTurnstile-14 is dated 2026-08-20, before the key, and is not written.

Owed at the close: `spec-tokens self-test` (the new arm, with its RED-first observation by a checker
copy that ignores the key), `drift-audit records`, `drift-audit selftest`, `spec tokens (a spec's own
names resolve)`, `memory hygiene` and the other §7 legs.

**Evidences:** TOOL-dSafePassage-34
- AC1 — handed to TOOL-dSafePassage-41 (its S3 carries this AC as its AC1, with the arm covering it); this pass grades nothing by the key. The read itself: a `python` probe importing the checker and calling `read_cutoff_key(<scratch>, AC_ORDER_KEY)`, the key `SPEC_AC_ORDER_CUTOFF`, returned `''` for a blank key and `'2026-10-23'` for a set one.
- AC2 — the same probe over a scratch conf `SPEC_AC_ORDER_CUTOFF="2026-9-8"` printed `spec-tokens: REFUSING — SPEC_AC_ORDER_CUTOFF 2026-9-8 is not an ISO date (YYYY-MM-DD) ...` and returned `None`, which `main` turns into exit 1 beside the other four keys.
- AC3 — handed to TOOL-dSafePassage-41 (its AC2), whose ledger records the `ac-order` predicate probe printing `key '2026-10-23' · live 37 · graded 1 · out of order 0`, the leg's own `ac-order` line owed to the close; the probe read `'2026-10-23'` from this tree's conf.
- AC4 — `git grep -n -e "SPEC_AC_ORDER_CUTOFF" -- .memory-tree.conf memory/map/features/spec-tokens.md` printed `.memory-tree.conf:984` (the comment), `.memory-tree.conf:992:SPEC_AC_ORDER_CUTOFF="2026-10-23"` and `memory/map/features/spec-tokens.md:133`.
- AC5 — `git grep -n -e "cutoff_keys_armed" -e "36 -> 37" -- tools/drift-audit/drift_signals.py` printed `:352` (the comment naming TOOL-dSafePassage-34 and ER:388) and `:354: "cutoff_keys_armed": 37,`; `python tools/drift-audit/drift_report.py --json` read `cutoff_keys_armed` value 37 of 37, tolerance 37; the staged names list `.memory-tree.conf` and `tools/drift-audit/drift_signals.py` and not `memory/DECISIONS.md`.

The `New arm:` lines of this unit were observed at the close, each RED on its staged break and GREEN restored; a line counts observed when its break reds at least one of its arms. Observed by a researcher in scratch clones of `83817478f` (batch a, `2026-10-28-prompt-TOOL-dSafePassage-5-close-arms-a-researcher.md`), each break staged alone and restored: One `New arm:` line, `tools/check-spec-tokens.test.sh`. The break was a checker copy that ignores the key (`ac_order_cut = ""`). It gave `arm FAIL  a non-ISO SPEC_AC_ORDER_CUTOFF is REFUSED like the other cutoff keys — expected rc 1, got 0` and the dated-red FAIL. Restored: 4/4.
