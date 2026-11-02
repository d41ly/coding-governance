**Serves:** research PLAY-dOrderedCharter-17 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-42

# Brief: the four asks filed against this build's specs, folded before their units build

## The prompt

> dOrderedCharter

— owner, 2026-11-02, invoking `/unattended` for the build run. README rule 1 makes it the build run, which builds
every carried unit; the four asks below were filed in this build's `BACKLOG.md` on 2026-10-26, after the spec run
landed, and each one's `accept` clause is a spec amendment.

## The brief

### Goal

Amend specs 17, 11, 25 and 42 so each reads as its ask's `accept` clause says, and make each spec's header carry
`closes` for its ask, so building the unit closes the ask.

### Items

1. **PLAY-dOrderedCharter-56 → spec 17.** Its non-goals name `TOOL-dFurnishedOrders-4` as the slots' renderer, not
   dBoundRoles (clauses cl-dClosedLoop-0195 and cl-dClosedLoop-0203 give slot rendering to dFurnishedOrders).
2. **PLAY-dOrderedCharter-57 → spec 11.** S1's `derive_load_set` carries a `features` argument
   (`TOOL-dFurnishedOrders-18` selects a work order's units by `feature.*`), and reports the selector `unarmed` while
   no `feature` namespace is registered; one acceptance criterion observes that on a fixture with none registered.
3. **PLAY-dOrderedCharter-58 → spec 25.** §3 names dLinkedLibrary, not dTotalRecall, as the build arming the
   `feature` selector (clause cl-dClosedLoop-0209).
4. **PLAY-dOrderedCharter-59 → spec 42.** The typed-kind file-name join reads `-<kind>-<n>.md` only on the stem
   `-build-<unit id>-<kind>-<n>.md`; one acceptance criterion observes a research record named `…-return-plan-2.md`
   staying bound once `plan` joins `TYPED_RECORD_KINDS`.

In every spec you revise:

- Bump the **Status:** rev by one, dated 2026-11-02, the status kept `DEFERRED`, add `closes <ask id>` before the
  existing `advances PLAY-dOrderedCharter-38`, and add one §9 line naming the ask and this brief.
- Verify every name you cite (a function, a unit, a clause) against the tree or the clause text before writing it.
- Stay under the 49152-byte cap with the generated records rows the render adds; a spec over 47000 bytes is trimmed
  in its authored prose.

### Acceptance

- `grep -n 'closes PLAY-dOrderedCharter-5[6-9]'` prints one header line in each of the four specs.
- `grep -n 'TOOL-dFurnishedOrders-4'` prints spec 17's non-goal; `grep -n 'features'` prints spec 11's S1 signature
  and its AC; `grep -n 'dLinkedLibrary'` prints spec 25's §3; `grep -n 'return-plan-2'` prints spec 42's AC.
- Each Status line is one rev higher, and §9 holds the new line.
- `python tools/check-spec-tokens.py` over the four specs exits 0.

### Gates

The spec-token check above; memory hygiene's staged leg at the commit.

### Non-goals

No code, no other spec, no edit of `BACKLOG.md`: the ask closes when its unit's build commit flips the spec CLOSED.

### Limitations

- Writes stay in the four spec files and the files `gen_build_index.py --write` rewrites.
- This is an unattended run and nobody answers a question: where an ask's accept clause cannot be written truthfully
  against the tree, leave that spec unedited and say so in the return.
- Commit once, after `python tools/memory-tree/gen_build_index.py --write`, staging the four specs and every file the
  render rewrote by name, and only when the spec-token check exits 0. Subject: `spec(dOrderedCharter):
  PLAY-dOrderedCharter-17 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-42 — asks 56 to 59
  folded before their units build`; trailers `Pass: none` and `Co-Authored-By: Claude Opus 5.5
  <noreply@anthropic.com>`. Give `git commit` a 600000 ms timeout: the pre-commit hook takes minutes.
- Scratch files go under the session scratchpad
  `C:/Users/DAILY-~1/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unattended-dorderedcharter-725f52/0394fa33-012c-408f-a840-e6e4cfaac23f/scratchpad`.
- Return the commit sha, each spec's new rev, and the output of each acceptance grep.

### Reuse

Each ask names its own source clause or unit; read those, never a paraphrase.
