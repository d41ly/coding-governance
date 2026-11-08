**Serves:** research TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-5

# dPlacedRequest — the re-ground writers' returns, verbatim

The `gov-spec-writer` return for the re-ground brief [`2026-11-05-prompt-TOOL-dPlacedRequest-1-parents-reground`](../prompts/2026-11-05-prompt-TOOL-dPlacedRequest-1-parents-reground.md), extracted by script from each agent's transcript and not retyped. The cross-check record it folds is [`2026-11-05-build-TOOL-dPlacedRequest-1-parents-crosscheck`](2026-11-05-build-TOOL-dPlacedRequest-1-parents-crosscheck.md); each group's handoff sits beside the brief.

## Group A, led by spec 5

I revised TOOL-dPlacedRequest-5 to rev-5. Row 6 is folded the way the brief decided. Nothing was refused: I re-read both sides at the branch tip, and the MISMATCH still holds. dl20 S7 and its "The hand-out gate" paragraph still hold the hand-out under `owed-only` only for the cause `owed`. The uncommitted dl20 rev-4 changes only S8, the item rows, the dl32 edge and AC1. No commit since `ab976b5b3` and no fork pick touches pr5, dl19 or dl20.

**Unit TOOL-dPlacedRequest-5 (authored, group A)**, file `C:\projects\coding-governance\.claude\worktrees\vigilant-einstein-2d0f7d\memory\builds\dPlacedRequest\spec\2026-10-25-spec-TOOL-dPlacedRequest-5.md`
- **Status:** `DEFERRED · rev-5 · 2026-11-05`, every other field kept. §9 has the new rev-5 line in the brief's form.
- **S6:** a placed `spec audit` now fires at Design's exit with `--cause owed`, because once the preflight reads the record at its BASE, `AUTH_SPEC_AUDIT_FROM` holds `placement`. `--cause placement` stays for every other placed name and item, and for the at-once firing past the position. The parent is cited as "TOOL-dDeclaredLoop-20 S2".
- **S5 and AC5 also changed, which goes past S6, S7 and the hold's criterion.** It was needed: dl19 S6 fires a breakpoint with the cause "taken from S1's list", so the cause S6 fires with is the cause S5 lists. S5 now lists a placed `spec audit` with cause `owed` and everything else with `placement`. AC5 checks both causes.
- **S7:** now states the hold for each `review.blocks` value, as dl20 S7 gives it:
  - `every-review`: held until the verdict is terminal.
  - `owed-only`: held the same way, because of the `owed` cause.
  - `none`: never held; the review runs alongside.
  - `--close`'s specs-audited term is still owed in all three cases.
- **AC1:** gains the plant `audit-request-owed-only`. With `review.blocks = "owed-only"`, it lists the breakpoints, fires the listed `spec audit` through the copied driver's `--trigger`, and expects `"trigger": "owed"` and `"blocks": "yes"`. It goes red when the audit fires with `placement` (`blocks` is `no`). It does not check how the harness reads `blocks`; dl20 AC8 covers that.
- **Kept consistent:** §4 The flow, the `tools/loop/placement.py` arm line in §7 (now covers AC1 too, with the new failing case), and §10's seam sentence.
- **Checks:**
  - `wc -c` is 27971, under 49152.
  - The memory hygiene gate, run over an index copy with only this spec staged, names nothing of the spec. Its one failure is check 9, an owed `gen_build_index.py --write` render, which is the main loop's. The index copy is deleted and the real index is untouched.

**Open points, not edited:**
- **Mid-run placement.** If the record is placed by the session already holding the lease after its preflight, it is in the run's tree but not at its BASE. S5 still lists `owed` there, so the hold applies, but `--close`'s term is not owed until the next preflight. A pure `derive_breakpoints` cannot see the BASE, so I did not make the cause conditional. This choice favours pr5's goal.
- **Possible duplicate breakpoint (dl19 parent text, maybe wrong).** dl19 §4 says Design's opt-in "is S8's derivation", and dl19 S2 under `opt-in` lists the stage's review with cause `opt-in`. Once pr5 S7 adds the `placement` source, dl19 may also list a `spec audit` at the same position with cause `opt-in`, beside pr5's `owed` entry. Neither spec says how two breakpoints at one position are merged. The issue predates this revision and is for the main loop to route.
