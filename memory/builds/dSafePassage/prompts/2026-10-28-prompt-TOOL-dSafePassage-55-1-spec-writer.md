**Serves:** research TOOL-dSafePassage-55

# Brief: the struck order sweep leaves TOOL-dSafePassage-55 moot and 51 and 59 with residuals

## The prompt

No owner prompt. TOOL-dSafePassage-49 rev-6 (5d4b43a7f, built as c24318735) struck §8 F1(a)'s order sweep and its AC2. The run had built TOOL-dSafePassage-4, -18 and -19 in consumes-from order, which `--dispatch`'s edge refusal enforces, and they are CLOSED. The spec writer for that revision reported three DEFERRED specs that rest on the sweep. The run revises them under M2.

## The brief

### Goal

No DEFERRED spec in dSafePassage asks for the struck sweep, a header move on a CLOSED spec, or AC2's four relations. Each of TOOL-dSafePassage-51, -55 and -59 either keeps a buildable residual or is closed WONTDO with its reason.

**What TOOL-49 rev-6's writer found.**
- **TOOL-dSafePassage-55 (DEFERRED, order 15).** Its whole scope rests on F1(a)'s sweep and AC2's four relations: S1, S2, AC1, AC2 and the §4 probe table, "the roster hand-out refuses on TOOL-49 AC2's whole order predicate".
- **TOOL-dSafePassage-51 (DEFERRED, order 14).** The sweep sits under S1's hand-out step, S2, S3, AC2 (the Rollout amendments to `TOOL-dSafePassage-4 builds at order 3`), its §3 consumes-from text, §5 risks and §10. AC1, which reads `Pass:` trailer order, still observes something real. TOOL-49's deviation 181 also hands 51 the ordering of S7's rev-parse refusal after the config read (`memory/builds/dSafePassage/build/2026-10-28-build-TOOL-dSafePassage-49-deviation-181.md`).
- **TOOL-dSafePassage-59 (DEFERRED, order 15).** The sweep sits under S1 and AC1 (its checks under `Pass: none`) and S4 and AC12 (the TOOL-43 Rollout phrase).

**The main loop's recommendations.**
- **TOOL-dSafePassage-55: WONTDO.** Set its status to `WONTDO` with the reason that the relation it gates was enforced by `--dispatch`'s consumes-from refusal (`tools/unattended/unattended.sh:13857-13926`) and the sweep was struck by TOOL-49 rev-6. Cite RUN.md's dispatch rows. Do this only if no part of its scope survives on its own. If a part does survive, say which and keep it as the residual.
- **TOOL-dSafePassage-51: residual.** Strike the sweep-dependent items and criteria. Keep AC1 and every item not resting on the sweep, and take on deviation 181's ordering note if it fits 51's one mechanism. Correct §3, §5 and §10 to match.
- **TOOL-dSafePassage-59: residual.** Strike S1/AC1 and S4/AC12's sweep parts and keep the rest.
- If striking leaves a criterion number unused, keep the number and mark it struck, as TOOL-49 rev-6 did, so no cross-reference dangles. Fix every edge bullet that pointed at a struck item, and its mirror in the other spec.

### Items

1. **Revise TOOL-dSafePassage-51, -55 and -59** as rev bumps dated 2026-10-28, each with one §9 line naming this brief. 51 and 59 stay `DEFERRED`; 55 goes to `WONTDO` or keeps a residual. Re-read each spec's cited code lines at HEAD `10511362a`.
2. **Cross-read** every other DEFERRED dSafePassage spec (TOOL-dSafePassage-52, -53, -54, -56, -57, -58, -61) for a citation of a struck item. Fix it in place. CLOSED specs are read-only: report a contradiction in one.
3. **Commit nothing.** Return the files you wrote and each spec's disposition.

### Acceptance

- `grep -n 'order 3\|F1(a)\|sweep' memory/builds/dSafePassage/spec/*TOOL-dSafePassage-5[159].md` prints only struck or historical lines.
- `bash tools/memory-tree/check-memory-hygiene.sh --staged`, run over a copy of the index with only your files staged through `GIT_INDEX_FILE`, names no finding in them other than check 9's stale build index.

### Gates

Only the memory hygiene gate (`--staged`, over a copy of the index) and the naming lexicon, as the role allows.

### Non-goals

- No product code.
- No edit to a CLOSED spec.
- No commit, and no stage into the real index.
