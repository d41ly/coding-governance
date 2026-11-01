**Serves:** research TOOL-dRankedPlan-82

# Spec brief — TOOL-dRankedPlan-82, the spec tokens leg's ceiling covers the packet join over this run's live chain

## The prompt

The owner answered the run's hand-off `owner-decision` at `be042d1e2`: "Raise the spec-tokens leg's ceiling in
tools/gate-legs.json enough for the live chain's packet join, then resume dRankedPlan, re-run the close and land it."
The answer is recorded in `memory/builds/dRankedPlan/prompts/2026-10-27-prompt-TOOL-dRankedPlan-1-owner-review-until-no-high.md`.

The close's bar timed the `spec tokens (a spec's own names resolve)` leg out at its 390 s ceiling twice, in the pool
and on its serial retry, red OWN (`memory/builds/dRankedPlan/RUN.md`, the hold reason). Measured by the main loop on
node a with the host idle: `packet.py --check dRankedPlan` alone took 344 s, and inside it `carries.py` spawns one
`git` per chain spec revision across the chain's 954 specs. The ceiling was last raised from 180 to 390 s by
`TOOL-dGroundRules-87` (`64c85a989`) from a 195.0 s reading over one live chain run; its evidence row is
`tools/run-gates/ceiling-evidence.txt:132`. The batching cure is ask `TOOL-dGroundRules-112`, which needs the owner's
repin outside a live chain run, so it cannot land here.

## The brief

### Goal
Author `memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-82.md`, a Tier-1 micro-spec at order 28,
status `DEFERRED`, in the shape of `memory/builds/dGroundRules/spec/2026-10-25-spec-TOOL-dGroundRules-87.md`, which it
follows section for section. This unit is built in this run, not carried forward: say so in §1, citing the owner's
answer above. Author only: no product code, no commit, no gate beyond memory hygiene.

### Items
1. Size the ceiling from evidence, never by typing a number: read `tools/run-gates/derive-ceilings.py` and
   `tools/run-gates/ceiling-margin.txt` whole, and spec the raise the way `TOOL-dGroundRules-87` took it: one reading
   R of the leg alone on a free host, written with `derive-ceilings.py --write --observed` and a `--how` text, and C
   the least multiple of 10 at or above 2R. The evidence row rises from 195.0 to R; the monotone rule allows it.
2. S1 is that leg's ceiling in `tools/gate-legs.json` (`:1700`, 390 today) and its evidence row; no other row of
   either file moves. S2 is the `last-audit` re-stamp of `memory/guides/SESSION-KICKOFF.md`, because
   `tools/gate-legs.json` is a watched path. Read both from the tree at this unit's base, never from the precedent.
3. Name what the raise does not check (the cost stays in `carries.py`, ask `TOOL-dGroundRules-112`) and when the
   ceiling comes back down (once that ask lands and a reading supports it).
4. Each acceptance criterion is a command the pass may run (`derive-ceilings.py --check`, the leg's own command timed
   alone, `manifest-check.sh --staged`, a staged-diff count), never the bar or a self-test suite, and carries
   `Red when:` with a staged break that reds it by name.
5. §6 names the legs the three touched files owe through `python tools/check-spec-tokens.py --legs-for`; the bar
   itself runs at the close.
6. §7 "Open questions" reads exactly `none`, with no bullet under it; any follow-up goes in the §8 revision log as
   prose. No line anywhere in §5 starts at column 0 with `AC<n>` other than the bullets themselves; every AC bullet
   carries `Red when:`; keep every acceptance code span on one line and free of a `|`; no retirement word in §2; an
   untracked path sits in a fenced block; never write a probe copy of a spec inside the spec folder.

### Acceptance
`python tools/check-spec-tokens.py` names nothing in this spec (the main loop runs it); hygiene check 12 names
nothing in this spec.

### Gates
Memory hygiene only.

### Non-goals
`carries.py`, `packet.py` and every other dClosedLoop instrument; any other leg's ceiling; the run-gates runner;
`tools/run-gates/ceiling-margin.txt`.

### Reuse
`tools/run-gates/derive-ceilings.py`, `tools/run-gates/ceiling-margin.txt`, and `TOOL-dGroundRules-87`'s raise at
`64c85a989`.
