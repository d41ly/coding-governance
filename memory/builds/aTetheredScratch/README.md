---
slug: aTetheredScratch
node: a
opened: 2026-08-20
streams: tooling
roster: TOOL
ids: TOOL-aTetheredScratch-1 TOOL-aTetheredScratch-2
---

# aTetheredScratch — agent scratch stops landing in the operator's home directory

The reported symptom was that "gate bar runs and other tools now emit their temporary files into
`C:\Users\daily-agent`". The diagnosis found the opposite of what the report assumed: **no tracked
tool in this repo writes to `$HOME`.** A grep for a `$HOME`- or `~`-rooted write target across every
tracked `.sh`, `.py` and `.js` returns exactly one hit, `tools/check-wiring.sh:498`, and that is a
READ of the per-machine skill install. Every gate leg uses `mktemp`, and the runner's durable
evidence goes to `<git-dir>/gate-logs/`.

The litter is agent-authored. Eighteen loose files, all dated 2026-08-19, whose contents are verbatim
`run-gates.sh` and `push-main.sh` stdout — the residue of ad-hoc calls shaped like
`bash tools/run-gates/run-gates.sh > ~/.merge-bar.log 2>&1`, written by sessions that needed a log to
outlive a backgrounded call and reached for `~` instead of a scratch dir. Under Git-Bash `~` is the
operator's home. Beside them sits `~/.gov-push/` at 45 entries and 4.3 MB, holding both `mrecall-*`
repos (the already-OPEN `TOOL-aBranchedMandate-6` leak) and generic `tmp.*` dirs — which proves a
prior session exported `TMPDIR` to that path, so ordinary `mktemp -d` landed there too.

That distinction decides where a fix can bind. A rule in a charter is what already failed here: the
governing doc has said "scratch belongs in a scratch dir" for the whole life of this repo, and the
sessions that wrote these files had it loaded. Nothing in a script can catch it either, because no
script is involved — the write happens in the tool call itself. **The only surface that sees the
offending bytes is a `PreToolUse` hook on `Bash`**, which is the same reasoning that put the fan-out
rule in `tools/hooks/agent-cap.js` rather than in prose.

## What the design pass found that the plan did not survive

Two facts from the grounding pass changed the shape of unit 2, and both are recorded here because the
owner picked the wider option before they were known.

**An in-tree scratch root is refused, not merely risky.** Pointing `TMPDIR` anywhere under the working
tree breaks four gate legs, and two of those breaks are *not* repairable with a `.gitignore` line:
`tools/check-template-size.sh:60-68` derives its high-water key by stripping the repo-root prefix, so
a scratch subject inside the tree silently changes key and the arms that prove the keying stop
measuring (`tools/check-template-size.test.sh:165,178,181,205`); and `tools/check-wiring.test.sh:87`
asserts the non-git branch by `cd`-ing into a `mktemp -d`, which inside the tree resolves to the real
repo and re-measures ambient wiring instead. Both are path-membership tests, not tracked-ness tests.
The other two — the codebase-map filesystem extractors and the three JS gates that enumerate
untracked files — would be survivable with an ignore rule, and are moot once the root is external.

**`.claude/settings.json` is tracked and shared by four nodes.** A `TMPDIR` value is an absolute
machine path; `daily-agent`, `agent5`, `agent-0` and `d41ly` do not share one. Writing it into the
tracked settings file would hand three nodes a path that does not exist on them. The carrier is
therefore `.claude/settings.local.json`, untracked and per-machine, plus the `.gitignore` line that
keeps it that way — which also makes the retarget an opt-in each node takes for itself rather than a
fleet-wide change made from one machine.

**And there is a recorded refusal of this move, in a neighbouring form.**
`memory/builds/aBranchedMandate/spec/2026-08-17-spec-TOOL-aBranchedMandate-4.md:76-79` names "making
the leg green by pointing `TMPDIR` somewhere the spellings converge" as a non-goal and "a bypass
wearing a different name", and `:203-204` pins that unit's AC1 to the *ambient* `TMPDIR` on node `a`.
Our motive is hygiene rather than a green leg, which is a different act — but the arm it protects
(`tools/unattended/adopt-unattended.test.sh:130-153`) constructs a two-spelling divergence that a
different temp root can collapse, degrading it to a loud skip. Unit 2 therefore treats that arm as a
gate on itself: if the retarget costs that arm its liveness, the retarget is abandoned and the guard
hook ships alone. Unit 1 does not depend on unit 2 for any of its acceptance.

## Units — the authored roster (M2)

Unit 1 stands alone and delivers the whole of the reported problem. Unit 2 is the crowded-`%TEMP%`
half — the bar timeout documented at `memory/guides/SESSION-KICKOFF.md:223-226` (30733 entries, 58
legs, over ten minutes) — and is written so it can be abandoned without touching unit 1.

<!-- roster:units -->
| # | Unit | Tier | Mechanism |
|---|---|---|---|
| 1 | `TOOL-aTetheredScratch-1` | 2 | a `PreToolUse` guard on `Bash` that denies a `$HOME`-rooted write |
| 2 | `TOOL-aTetheredScratch-2` | 2 | one external scratch root, per-machine, and the sweep of what is already there |
<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** SPECCED · 2 unit(s) · node a · opened 2026-08-20 · streams tooling
ids TOOL-aTetheredScratch-1 TOOL-aTetheredScratch-2

| Unit | Status | Rev | Last change |
|---|---|---|---|
| [TOOL-aTetheredScratch-1 — a PreToolUse guard on Bash that denies a HOME-rooted write](spec/2026-08-20-spec-TOOL-aTetheredScratch-1.md) | SPECCED | rev-1 | 2026-08-20 |
| [TOOL-aTetheredScratch-2 — one external scratch root per machine, and the sweep of what is already there](spec/2026-08-20-spec-TOOL-aTetheredScratch-2.md) | SPECCED | rev-1 | 2026-08-20 |

Records live under `spec/`.
<!-- /gen:build-index -->

<!-- gen:build-order -->

*No spec under this build declares an `order` verb; the build order is whatever its authored plan states.*
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->

<!-- gen:build-docs -->

- **`spec/`**
  - [2026-08-20-spec-TOOL-aTetheredScratch-1.md](spec/2026-08-20-spec-TOOL-aTetheredScratch-1.md)
  - [2026-08-20-spec-TOOL-aTetheredScratch-2.md](spec/2026-08-20-spec-TOOL-aTetheredScratch-2.md)
<!-- /gen:build-docs -->
