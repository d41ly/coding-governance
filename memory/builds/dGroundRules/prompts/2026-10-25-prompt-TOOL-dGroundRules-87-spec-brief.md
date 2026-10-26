**Serves:** research TOOL-dGroundRules-87

# Spec brief — TOOL-dGroundRules-87, the spec tokens leg's ceiling covers the packet join over a live chain run

## The prompt

The owner authorized this unit at the hand-off: "Raise the spec tokens leg's ceiling in tools/gate-legs.json to cover the live-chain packet join, as an owner-authorized unit of this run; then re-prepare, close and land. File the carries.py batching as an ask to build and repin once no chain run is live."

The close's bar at `263d31d59` timed the `spec tokens (a spec's own names resolve)` leg out at its 180s ceiling twice, in the pool and on its serial retry, attributed CONTENDED. Measured by the main loop on node a: the leg takes 170-173s alone at HEAD and 5s at origin/main `462d20f35`. The whole difference is the packet join's `packet.py --check dGroundRules` (169s), and inside it `carries.py --report dGroundRules` (143s, 4095 `git show` spawns), which runs only while a chain build's run is live. The batching is ask TOOL-dGroundRules-112 (filed); it cannot land in this run because `packet.py --repin` refuses inside a live chain run.

## The brief

### Goal
Author `memory/builds/dGroundRules/spec/2026-10-25-spec-TOOL-dGroundRules-87.md`, a Tier-1 micro-spec at order 34, status `DEFERRED`, in the shape `2026-10-25-spec-TOOL-dGroundRules-86.md` follows. Author only: no product code, no commit, no gate beyond memory hygiene.

### Items
1. Size the ceiling from evidence, never by typing a number: read `tools/run-gates/derive-ceilings.py` and `tools/run-gates/ceiling-margin.txt` whole, and spec the raise the way their rules and the `2fe73530e` precedent take one (an `--observed LEG=SECONDS` reading with its `--how`, a free host, the margin the file asks). Name the reading the builder takes and the value the margin turns it into; record the 170-173s alone readings above and the two in-bar timeouts as the evidence.
2. S1 is the ceiling raise in `tools/gate-legs.json` for that one leg, with whatever evidence record the derivation tool writes beside it; no other leg moves. Name what the raise does not check (the cost lives in `carries.py`, ask TOOL-dGroundRules-112) and when the ceiling should come back down (once that ask lands and a reading supports it).
3. Each acceptance criterion is a command the pass may run (`derive-ceilings.py --check`, the leg's own command timed alone), never the bar or a self-test suite, and carries `Red when:` with a staged break that reds it by name.
4. §6 names the legs `tools/gate-legs.json` owes through `derive_guarded_legs`; the bar itself runs at the close.
5. §7 "Open questions" reads exactly `none`, with no bullet under it; any follow-up goes in the §8 revision log as prose. No line anywhere in §5 starts at column 0 with `AC<n>` other than the bullets themselves; every AC bullet carries `Red when:`; keep every acceptance code span on one line and free of a `|` the bar pattern reads as a pipe; no retirement word in §2; an untracked path sits in a fenced block; never write a probe copy of a spec inside the spec folder.

### Acceptance
`python tools/check-spec-tokens.py` exits 0 with this spec read as INPROGRESS (the main loop runs it); hygiene check 12 names nothing in this spec.

### Gates
Memory hygiene only.

### Non-goals
`carries.py`, `packet.py` and every other dClosedLoop instrument; any other leg's ceiling; the run-gates runner.

### Reuse
`tools/run-gates/derive-ceilings.py`, `tools/run-gates/ceiling-margin.txt`, and the `2fe73530e` raise.
