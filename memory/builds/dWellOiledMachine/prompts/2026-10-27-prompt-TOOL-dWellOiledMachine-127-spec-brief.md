**Serves:** research TOOL-dWellOiledMachine-127

# Spec brief — TOOL-dWellOiledMachine-127, the spec tokens and routed commits ceilings cover this build's close

## The prompt

The owner ruled at the hand-off: "Raise the spec tokens and routed commits ceilings with evidence rows in a separate unit, then re-run dWellOiledMachine's close and land it." The ruling is recorded at `memory/builds/dWellOiledMachine/prompts/2026-10-27-prompt-TOOL-dWellOiledMachine-1-owner-raise-ceilings.md`.

The close's bar at `10ab21489` timed out two legs twice each, in the pool and on the serial retry, and attributed both CONTENDED. `spec tokens (a spec's own names resolve)` hit its 390 s ceiling and `routed commits name a specced unit` hit its 300 s ceiling. The main loop then ran each leg's own argv on node a at `ec8ad0363`; the two ran side by side, so these are not solo readings. Spec tokens exited 0 in 512 s, its packet join over 1 live chain run. Routed commits exited 0 in 358 s. The spec tokens cost is the packet join's `packet.py --check dWellOiledMachine`, whose `carries.py --report` spawns one `git show` per chain spec revision; it runs only while this chain build's run is live, which is exactly its own close. `TOOL-dGroundRules-87` raised the same leg from 180 to 390 s on a 195 s reading at dGroundRules' close, and its spec is the shape to follow.

## The brief

### Goal
Author `memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-127.md`, a Tier-1 micro-spec, status `DEFERRED`, in the shape `memory/builds/dGroundRules/spec/2026-10-25-spec-TOOL-dGroundRules-87.md` follows, its **Derived:** line included. The status header carries NO `order` verb: every other unit of this build is DEFERRED to the build run, and an unordered unit is neither blocked by them nor blocks them at dispatch. Author only: no product code, no commit, no gate beyond memory hygiene.

### Items
1. Size each ceiling from evidence, never by typing a number. Read `tools/run-gates/derive-ceilings.py` and `tools/run-gates/ceiling-margin.txt` whole, and spec each raise the way TOOL-dGroundRules-87 took one: a reading of the leg alone on a free host, written with `--observed '<leg>=<seconds>'` and its `--how`, and C derived from the margin the file asks. The builder takes the two readings one after the other, never side by side. Record the in-bar timeouts and the 512 s and 358 s side-by-side readings as the evidence.
2. S1 raises `spec tokens (a spec's own names resolve)`, S2 raises `routed commits name a specced unit`, each in `tools/gate-legs.json` with its row in `tools/run-gates/ceiling-evidence.txt`. Routed commits has no evidence row today, so verify what `--observed` writes for a leg with no row. No other leg moves. Verify what `routed_commits.py` grades when no `GATE_PUSH_BASE` is exported, and spec the reading against the base the close's bar gives it, so the reading measures the bar's work.
3. S3 is the kickoff manifest's `last-audit` re-stamp, because `tools/gate-legs.json` is a watched path, as TOOL-dGroundRules-87's S2 was.
4. Name what the raises do not check. The spec tokens cost lives in `carries.py`: find the ask TOOL-dGroundRules-87 filed for it and cite it. Say why routed commits grows. Say when each ceiling should come back down.
5. Each acceptance criterion is a command the pass may run, such as `derive-ceilings.py --check` or a leg's own command timed alone, never the bar or a self-test suite. Each carries `Red when:` with a staged break that reds it by name.
6. §6 names the legs `tools/gate-legs.json` owes through `derive_guarded_legs`; the bar itself runs at the close.
7. Format rules:
   - §7 "Open questions" reads exactly `none`, with no bullet under it; any follow-up goes in the §8 revision log as prose.
   - Every §8 mark keeps `widens: … · relaxes: …` on ONE line.
   - No line in §5 starts at column 0 with `AC<n>` other than the bullets themselves, and every AC bullet carries `Red when:`.
   - Keep every acceptance code span on one line and free of a `|` the bar pattern reads as a pipe.
   - No retirement word in §2.
   - An untracked path sits in a fenced block.
   - Never write a probe copy of a spec inside the spec folder.
8. Bounded searches only: one `git grep` over a per-file spawn loop, and every shell search under `timeout 90`.

### Acceptance
`python tools/check-spec-tokens.py` exits 0 with this spec read as INPROGRESS (the main loop runs it); hygiene check 12 names nothing in this spec.

### Gates
Memory hygiene only.

### Non-goals
`carries.py`, `packet.py` and every other dClosedLoop instrument; `routed_commits.py`'s own cost; any other leg's ceiling and `tools/run-gates/ceiling-margin.txt`; the run-gates runner; every other unit of this build.

### Reuse
`tools/run-gates/derive-ceilings.py --observed`, `tools/run-gates/ceiling-margin.txt`, and TOOL-dGroundRules-87's raise at `64c85a989`.
