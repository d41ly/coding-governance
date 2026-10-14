# Research: routing and step resolution — how a session picks a build, step, unit and pass today

**Serves:** research PLAY-dClosedLoop-1

The gov-researcher's return for handoff `prompts/2026-10-14-prompt-PLAY-dClosedLoop-1-6-researcher.md`
(dispatch 11), verbatim. The harness escaped `<` and `>` in the returned text as HTML entities; they
are restored here, and nothing else is changed.

---

# Routing and step resolution: how a session picks a build, step, unit and pass today

## 1. Inventory

- **SessionStart `--card --write`** (on startup or clear) renders the card: tree, BASE, the claims, and a *count* of live builds. It matches nothing against the request. `.claude/settings.json:33-40`, `skills/session-kickoff/manifest-check.sh:529`
- **`--card --replay`** (on resume or compact) prints the stored card back with one `now —` line, so a resumed session gets its old `## route` again. `manifest-check.sh:20`
- **`/session-kickoff` Step 3** has the agent "DERIVE these fields yourself" from the message and memory. That is where the request gets placed in a build. `skills/session-kickoff/SKILL.md:126-131`
- **Brief `## route` grammar**: one build, one or more units each with a spec, and one brief. `manifest-check.sh --brief-skeleton`, `:162-163`
- **`check_card_route`** (R1-R6) checks only that the route's build, units, specs and brief exist and pair up. It does not check whether the unit is live, its status, or whether the owner said go. `manifest-check.sh:1000-1001`
- **`LIVE.md`** is the generated list of non-terminal builds. Each build's status comes from its specs' status headers. `memory/LIVE.md:1-5`
- **`memory/ledger/`** lists builds by the month they opened. It is not read when routing. `memory/ledger/2026-10.md`
- **`gen_build_index.py --new-build`** opens a build only from asks that are already filed and grade ready. It refuses a build that answers no ask. `tools/memory-tree/gen_build_index.py:3451,3588-3633`
- **`--ready`** grades the asks in a mandate. `gen_build_index.py:3384`
- **`--asks --path`** lists the open asks that touch a given path. `gen_build_index.py:2684-2700`
- **`/build`** is told the build by the READY card. The agent sets the next READY unit's spec to INPROGRESS, then appends a `## route`. `.claude/skills/build/SKILL.md:16,59-63`
- **`/unattended` entry** picks its path by the *shape* of what it was handed (a slug, a prompt or ids). A prompt with no build folder always means a new build. `tools/unattended/SKILL.template.md:26-32`
- **`--plan --paths`** prints `next:` from the units region, the spec status headers and `plan_state`. `tools/unattended/unattended.sh:5785,5928-5929,5994`, with the rule ladder at `derive_next_shape` `:5762`
- **`--dispatch`** refuses a MISSING or THIN unit, and refuses one out of `order`. The order is read from the spec headers. `unattended.sh:13470-13480,13530ff`
- **`--resume` and phase**: the phase is the `phase:` fact the verbs write into RUN.md. LANDED is derived from the ancestry of the remote tip. `unattended.sh:1439,1480-1530,9008`
- **Pass record**: `--dispatch` writes `dispatch · item` rows, and `pass_commit` walks git to find each pass's commit. `tools/unattended/lib-unattended.sh:932,1022`
- **`resume-tick.sh`** restarts a stale run, deciding only from `--liveness`. `tools/unattended/resume-tick.sh:10-18`
- **`routed_commits.py --newest-unit`** derives the unit the newest commits name. `tools/memory-tree/routed_commits.py`
- **The write gate**: `checkRouted` (`tools/hooks/scratch-guard.js:1113`) and `checkBuildable` (`:873`, `BUILDABLE_STATUS` `:796`). It admits a write when the spec reads INPROGRESS, a status the agent types (`:89`).
- **format-guard** arms only when the route's build is a row of LIVE.md. `tools/hooks/format-guard.js:17-20,479-482`

## 2. Sequence

**New attended session**
1. The card is written. ENFORCED (`settings.json:33-40`).
2. Is the request an open build, a new build, an amendment, an ask or none? LEFT TO THE AGENT (`SKILL.md:126-131`). The card shows only a count of live builds (`:529`).
3. Opening a new build: ENFORCED only if `--new-build` is used, which requires filed asks. Writing a README by hand is not refused.
4. The route lands on the card. ENFORCED for existence only (`manifest-check.sh:1000-1001`). A route to a terminal build passes.
5. The owner says go. LEFT TO THE AGENT: the reply is quoted in the brief, and nothing checks it.
6. Which unit: `--plan` prints `next:`, the agent picks it and flips it to INPROGRESS. LEFT TO THE AGENT (`build/SKILL.md:59-61`).
7. Product writes: ENFORCED by the write gate (`scratch-guard.js:1192`), but it reads typed status.
8. Which pass: LEFT TO THE AGENT. M6 lists five pass kinds (`BUILD-METHOD.md:182-183`), and nothing derives which one is due.

**Resumed session**
1. The card and route are replayed. ENFORCED.
2. Whether the route is still right: LEFT TO THE AGENT. Nothing compares it with LIVE.md or the leases.
3. Unit and pass: same as steps 6 and 8 above.

**Unattended run**
1. Which path: ENFORCED, but by input shape only. A prompt always opens a new build (`SKILL.template.md:28-32`).
2. Start and resume: ENFORCED by `--preflight` and `--resume` (lease matrix, phase).
3. Next unit: LEFT TO THE AGENT. It re-reads `--plan` between dispatches, and the guide says "Nothing refuses the next dispatch for you" (`memory/guides/UNATTENDED-VERBS.md:761`). Only MISSING, THIN and out-of-order units are refused (`unattended.sh:13470-13480`).
4. A stalled run is restarted. ENFORCED (`resume-tick.sh`).

## 3. Measurements

**(a) Mis-routing signal.** Run with `python3 - <<'EOF'`, abridged to its predicate. For each `memory/builds/*/README.md` with `opened:`, collect the backticked paths under `#+ Files touched` in its specs. Count a build as "live at X" when `opened<=X` and `git log -1 --format=%cs -- <folder>` >= X.

```
builds with opened: 167 | opened >= 2026-08-15 : 131
share >=1 Files-touched path with a build live at open: 110
same, excluding memory/map/generated + LIVE.md: 110
README names another build with supersede/retire/continue/successor wording: 6
```

The 21 builds that share nothing declare no Files-touched paths at all. So **110 of 110** builds that declare paths share at least one with a live build.

Same predicate with the 30 most-cited paths removed (the top ones are `tools/gate-legs.json:57` and `tools/unattended/unattended.sh:49`):

```
sharing >=3 non-hub paths with ONE build live at open: 71   (of 110)
sharing >=5 non-hub paths ...: 46
opened per day, top: [('2026-08-16', 11), ('2026-09-04', 10), ('2026-10-09', 9), ('2026-10-11', 9)]
```

**(b) Continued versus new.**

`ls .git/orientation | wc -l` → 20. The per-card `grep -c '^## route'` loop → 3 routed (dRemeasuredRender, dRedressedBar, dSweptBranches), and 2 cards share the title dClosedLoop.

Transcripts, classified by a Write of a build README with front matter or `--new-build <slug>` (new), against a `- build: <slug>` line or a write into an existing build folder (continued):

```
transcripts: 64 mtime span 2026-08-24 .. 2026-10-14
{'NEW': 1, 'CONT': 5, 'NONE': 58}
```

This covers node d only, and the store is pruned, so it is weak evidence.

Commit days per build:

```
for s in $(grep -l "^opened: 2026-\(08-1[5-9]\|08-[23]\|09\|10\)" memory/builds/*/README.md | cut -d/ -f3); do git log --format=%cs -- memory/builds/$s | sort -u | wc -l; done | awk ...
builds: 131  commit-days=1: 20  2-3: 57  >=4: 54
```

Kickoff commits: `git log --since=2026-08-15 --format=%s | grep -cE "^kickoff\("` → 16, of which 13 name one build.

One probe was dead: "README `ids:` line grew after opening" → 131/131. That line is regenerated, so it moves for every build.

**(c) Derived versus typed state.**

Every step-resolution read above uses typed state:
- spec status: `unattended.sh:5928`
- `order` verb: `:13530ff`
- INPROGRESS: `scratch-guard.js:796,897`, `build/SKILL.md:61`
- RUN.md `phase:`, written by the verbs: `unattended.sh:1626`

Two reads are derived: LANDED from tip ancestry (`unattended.sh:1480-1530`), and the pass commit (`lib-unattended.sh:932`).

Status against a commit that names the id (`re.findall` over `git log --format=%s%n%b`):

```
CLOSED 1244 1187 · WONTDO 33 26 · SPECCED 16 9 · INPROGRESS 10 10 · DEFERRED 10 6 · OPEN 2 1 · BLOCKED 2 1 · DRAFT 1 0
```

Most recent commit naming each INPROGRESS id: 2026-08-19 to 2026-10-06. That is 10/10 idle for at least 8 days and 9/10 for more than 14.

`python3 tools/memory-tree/routed_commits.py --newest-unit HEAD~30..HEAD` → `TOOL-aOrientedCast-27`, rc=0. This session works on dClosedLoop, and its records commits name no unit.

## 4. Gaps

- HIGH: deciding which build a request belongs to is entirely the agent's call (`SKILL.md:126-131`). Absent: any matcher of a request against LIVE.md or the asks. I searched `manifest-check.sh`, `gen_build_index.py` and the skills.
- HIGH: `/unattended` given a prompt always opens a new build, with no check against live builds (`SKILL.template.md:29`).
- HIGH: the route check checks existence only. A route to a terminal or someone else's leased build lands (`manifest-check.sh:1000-1001`).
- HIGH: the unit's step and the write gate read INPROGRESS, which the agent types. 10/10 INPROGRESS units are stale (`scratch-guard.js:89`).
- HIGH: no pass resolver. M6's five kinds are chosen by hand. Absent: a "pass due" derivation; I searched `unattended.sh` and `lib-unattended.sh`.
- MED: no build-level step. LIVE's "Status" column is spec vocabulary, not Plan to Maintain (`LIVE.md:11`).
- MED: "Nothing refuses the next dispatch" (`UNATTENDED-VERBS.md:761`).
- MED: the card shows a count, not the live builds or which session leases each (`manifest-check.sh:529`).
- MED: no recorded disposition. Only 6 of 131 builds name a predecessor, so mis-routing cannot be audited.
- LOW: the mis-routing signal saturates. 110/110 share paths with a live build, so path overlap cannot measure it.

## 5. Candidates

**A — Inferred router (path and ask overlap).**
- Mechanism: rank live builds by how many paths and asks the request shares with them, and auto-assign the top match. Step resolution stays as `--plan` does it today.
- Seam: `gen_build_index.py --asks --path` (`:2684-2700`).
- Losing test: among builds opened earlier, it must rank first the build a README names as the one it continues or supersedes.
- Result: **0/5 at rank 1**. The named build ranked 15/46, 22/52, 40/76, 2/87 and 11/162; two more named builds opened later and could not be ranked. **Rejected** as a decider. Its ranked list is still useful as evidence on the card.

**B — Declared disposition, checked at the card.**
- Mechanism: the route gains `- disposition: continue|amend|new|ask|none`. `--card --append` refuses unless that disposition's witness holds:
  - continue or amend: the build is in LIVE.md and its lease is free or this session's;
  - new: the README came from `--new-build` or a committed authorization;
  - ask: the id is filed and open;
  - none: no route at all.
  Step resolution stays on `--plan`.
- Seam: `check_card_route`, `manifest-check.sh:1003`.
- Losing test: if the current R1-R6 already refuse a route to a terminal build, B adds nothing.
- Result: by reading the code, they do not. R3-R5 check existence only (`:1000-1001,1036-1047`). B **survives** for routing, but it leaves step resolution on typed status, which (c) shows is stale.

**C — Derived resolver, with B for the new-session fork.**
- Routing: a session whose branch or worktree carries a build's lease is mechanically that build's session. Only a session holding no lease declares a disposition, as in B.
- Step resolution: each unit's step and next pass are computed from witnesses, never from status headers:
  - spec tracked: Design done;
  - audit or review verdict record: review done;
  - an attributed pass commit (`pass_commit`, `routed_commits --newest-unit`): built;
  - landed ancestry: deployed.
  The build's step is that of its least-advanced unit, and the answer is `next —`.
- Seam: `--plan`'s `derive_next_shape` (`unattended.sh:5762`), `pass_commit` (`lib-unattended.sh:932`), `read_derived_phase` (`unattended.sh:1439`).
- Losing test: if derived witnesses are missing for a large share of terminal units, the resolver would mis-place them.
- Result: 1187/1244 CLOSED units (95.4%) have a commit naming the id; 57 would need a one-time backfill. Every INPROGRESS unit has gone at least 8 days without a commit. C **survives**.
- Remaining risk: a commit that names an id is not proof that the unit was built. The build must test the `Pass:`-trailer join and plant a CLOSED-but-unbuilt fixture to see it red.

**Hand-offs:** card size goes to the orientation-cost researcher; trust in INPROGRESS and RUN.md fields to the trust researcher; extending the write gate to the derived step to the action-bounds researcher.

## 6. Pick

I recommend C, with B's declared disposition as its entry fork.

Step, unit and pass are all derivable from history, and (c) shows the typed status they are read from today is stale (10 of 10 INPROGRESS units idle for at least 8 days). A disposition must not be inferred: path overlap put the build each README names first in 0 of 5 cases and saturates at 110 of 110. So routing a session that holds no lease stays a judgment, recorded as a disposition and checked against LIVE.md and the leases.

Whose judgment: the owner's at Plan entry, and the agent's for an in-goal amendment or a patch build entering at Design. In both cases the card refuses any disposition whose witness does not hold.
