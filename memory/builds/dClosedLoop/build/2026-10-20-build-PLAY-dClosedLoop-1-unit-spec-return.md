# Return: the unit spec's writer

**Serves:** research PLAY-dClosedLoop-1

This is dispatch 232's return, verbatim, except that a title line would be demoted to keep one H1 per record.
Its question is in `prompts/2026-10-20-prompt-PLAY-dClosedLoop-1-60-spec-writer.md`.

---

I wrote the spec for `PLAY-dClosedLoop-1`. I ran no gate, so the spec-tokens leg and memory hygiene on the staged spec are still the main loop's to run.

**Spec:** `C:\projects\coding-governance\.claude\worktrees\gov-architecture-plan-e34297\memory\builds\dClosedLoop\spec\2026-10-20-spec-PLAY-dClosedLoop-1.md`, 20,690 bytes, under the 48 KiB spec ceiling. It is the only file I wrote. My probes are in the scratch folder `exec/d232/`.

A scratch probe I wrote (not a gate) confirmed:
- The status header is on line 3, and the ten sections are in canonical order, none empty.
- The only unit id in the spec is `PLAY-dClosedLoop-1`. No other build's id leads a cell, heading or list item, and there are no skeleton placeholders.
- Every backticked path in §6 is tracked.
- All 62 `path:line` citations point at tracked files and fall within range.

**Acceptance criteria.** Probes ran at `72b65c083` on 2026-10-20, and each criterion cites its record in the spec.

| AC | Status | Evidence |
|---|---|---|
| AC1, kickoff (a): decision rows | OPEN | `grep dClosedLoop memory/DECISIONS.md` finds nothing. P0.8 mints nine rows (plan :541-599). |
| AC2, kickoff (b): `LIVE.md` and chain READMEs | OPEN | Owed by P0.5 (plan :340-346); no chain folder exists yet. |
| AC3, kickoff (c): gap-ownership join | Done against v2's `[chain]`, open against the READMEs | Red on planted orphans, green on v2 (session log :3336-3339); rc 0 on the folded tree (whole-audit :535). No P0.7 check joins the READMEs. |
| AC4, kickoff (d): audit report and fold | DONE | `reviews/2026-10-18-review-PLAY-dClosedLoop-1-design-audit.md`; fold `[fold]` (audit-fold :45); session log :2772-2774 |
| AC5, baseline taken | DONE | v2 :1809 and whole-audit :579 both name `59ff8f2ac`, which resolves. |
| AC6, P0.1 | OPEN | `deviations.py` has no `--policy` arm (plan :162-165). |
| AC7, P0.2 | OPEN | `deviations.py` has no `--report` mode (plan :226). |
| AC8, P0.3 | OPEN | No packet instrument exists (plan :286-291). |
| AC9, P0.4 | OPEN | The red tests owe a re-run before landing (plan :299-325, :308-309). |
| AC10, P0.7 | OPEN | The opening is not written (plan :530-539). |
| AC11, P0.8 | OPEN | No rows exist yet (plan :598-599). |
| AC12, P0.9 | OPEN | Node d could not find the resume tick (plan :610, :615-622). |

**Legs in §7:** `kickoff-manifest ratchet` · `memory hygiene` · `build README slot contract`. All three are names in `tools/gate-legs.json`. The full bar and the stale-generated-output check (a runner mode, not a leg) are in prose only, without backticks.

**What the records could not supply.** Each of these is an open F-item in §8. None is resolved.
- **F1:** Phase 0 itself. It is the unit's remaining work, and none of it has run.
- **F2:** The atlas measured 16.4 MB, past its 16 MB limit. Should it skip the execution records, or split? Prompt 59 leaves this to you.
- **F3:** Kickoff (a) asks for decision rows for your ratified answers, but P0.8 only covers the execution answers. Are the design rounds' answers owed rows too?
- **F4:** Kickoff (c) joins the gap register against the chain READMEs, but nothing in P0.7 runs that join over the opened READMEs. Is it owed there?
- **F5:** The kickoff record's route (brief :104-107) names a spec dated 2026-10-14 that was never written; this spec is dated 2026-10-20. Should the route be re-appended, as its own comment at :103 says to?

**Corrections and gaps:**
- My first draft said the reuse probe had not surfaced the unit's seams. That was wrong, and I corrected §10. Of the seams cited, only the Deploy research spec is absent from the probe output.
- The spec cites `build/2026-10-20-build-PLAY-dClosedLoop-1-unit-spec-brief.md`, which is untracked right now. It needs to land in the same commit as the spec.
- No section 4 sub-head lists files touched, so the guard-legs join has no write set to read for this spec.
