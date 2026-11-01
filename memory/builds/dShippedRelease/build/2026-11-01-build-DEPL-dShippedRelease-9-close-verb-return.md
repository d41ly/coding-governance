**Serves:** research DEPL-dShippedRelease-9

# Unit 9 close-verb return — dShippedRelease

The writer's final return, extracted from its transcript by script, never retyped, and quoted whole.

Run direct/ab8bfca930091a780, from the handoff `2026-11-01-prompt-DEPL-dShippedRelease-1-4-spec-writer.md`.

> The edit to unit 9's spec is made and staged, nothing is committed, and no index was regenerated.
>
> **`DEPL-dShippedRelease-9`: authored (edit)**, in `C:\projects\coding-governance\.claude\worktrees\unattended-dshipped-release-1a351d\memory\builds\dShippedRelease\spec\2026-10-30-spec-DEPL-dShippedRelease-9.md`
>
> **Lines changed**
> - **Line 3, Status:**
>   - The last verb is now `advances DEPL-dShippedRelease-32`.
>   - The rev went from `rev-2` to `rev-3`, and the date from `2026-10-30` to `2026-11-01`.
> - **Lines 28-30, §1 (was 28-29):** the sentence that called this the last unit in build order, so its header closes the ask, now reads: "Units the audit rounds added follow it in build order, so its header advances DEPL-dShippedRelease-32, which stays open until the last unit in build order." This wraps to one more line, so every later line shifts down by one.
> - **Line 354, §9 (new):** the `rev-3 · 2026-11-01 · §1` entry, which cites the owner's stop ruling and states that no scope, design or criterion moved.
>
> **Why the rev moved:** `memory/TEMPLATE-SPEC.md:67-69` bumps the rev on any material content change, and only a pure status flip escapes that. Changing a declared verb and a §1 sentence is content, so the bump and its §9 line were required.
>
> **The claim I checked:** unit 9 is `order 31`, and the highest order in the tree is 38. Twelve other specs, including units 106 and 78, sit at order 31 or later (I didn't check which orders are shared). I left the last unit's id out of the sentence so it can't go stale.
>
> **Acceptance:** `grep -l "closes DEPL-dShippedRelease-32" memory/builds/dShippedRelease/spec/*` prints nothing (grep exit 1).
>
> **Gate:** `bash tools/memory-tree/check-memory-hygiene.sh --only 2,12,13,23,25` exited 0, run after the last edit and with the spec staged. It ran checks 2, 12, 13, 14, 15, 16, 23 and 25. Its only output in the part I read was advisory: check 25's did-not-grade lines on other builds' specs, and check 15's dead-path note.
>
> **Left alone**
> - **Unstaged `BACKLOG.md`:** `memory/builds/dShippedRelease/BACKLOG.md` was already modified when I started, with an added `DEFERRED · DEPL-dShippedRelease-32` row. I did not touch it, so it needs your commit decision.
> - **`gen:spec-records` table:** unit 9's table does not yet list the new close-verb brief, which serves this unit. It will pick that up the next time the index is regenerated.
