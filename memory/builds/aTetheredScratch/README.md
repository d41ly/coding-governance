---
slug: aTetheredScratch
node: a
opened: 2026-08-20
streams: tooling
roster: TOOL
ids: TOOL-aTetheredScratch-1 TOOL-aTetheredScratch-2 TOOL-aTetheredScratch-3 TOOL-aTetheredScratch-4
---

# aTetheredScratch — agent scratch stops landing in the operator's home directory

The reported symptom was that "gate bar runs and other tools now emit their temporary files into
`C:\Users\daily-agent`". The diagnosis found the opposite of what the report assumed: **no tracked
tool in this repo writes to `$HOME`.** A grep for a `$HOME`- or `~`-rooted write target across every
tracked `.sh`, `.py` and `.js` returns exactly one hit, `tools/check-wiring.sh:498`, and that is a
READ of the per-machine skill install. Every gate leg uses `mktemp`, and the runner's durable
evidence goes to `<git-dir>/gate-logs/`.

The litter is agent-authored. Eighteen loose files, all dated 2026-08-19: **sixteen** are verbatim
`run-gates.sh` and `push-main.sh` stdout — the residue of ad-hoc calls shaped like
`bash tools/run-gates/run-gates.sh > ~/.merge-bar.log 2>&1`, written by sessions that needed a log to
outlive a backgrounded call and reached for `~` instead of a scratch dir — and **two** are not logs at
all. `.rb-adb.bak` and `.rb-apm.bak` are pre-edit snapshots of two builds' `RUN.md`, carrying
`phase: LANDING` where the committed versions carry `phase: LANDED`; the spec audit caught that, and
they are verified against `d1bc3f3` before removal rather than swept as residue. Under Git-Bash `~` is
the operator's home. Beside them sits `~/.gov-push/` at 45 entries and 4.3 MB, holding both `mrecall-*`
repos and generic `tmp.*` dirs — which proves a prior session exported `TMPDIR` to that path, so
ordinary `mktemp -d` landed there too.

That distinction decides where a fix can bind. A rule in a charter is what already failed here: the
governing doc has said "scratch belongs in a scratch dir" for the whole life of this repo, and the
sessions that wrote these files had it loaded. Nothing in a script can catch it either, because no
script is involved — the write happens in the tool call itself. **The only surface that sees the
offending bytes is a `PreToolUse` hook**, matched on `Bash|PowerShell` because a guard wired to one
shell leaves the same act available through the other. That is the same reasoning that put the fan-out
rule in `tools/hooks/agent-cap.js` rather than in prose, and the same one-modality hole that file's
header records paying for.

## What the spec audit changed, and why both units are at rev-2

The first draft of both specs was wrong in ways a four-lens audit caught before any code was written.
Recording it here because the corrections are the interesting part of this build.

**On Windows the scratch roots are INSIDE the home directory.** `TEMP` is
`C:\Users\DAILY-~1\AppData\Local\Temp`, the session scratchpad is a subtree of it, and `/tmp` is an
MSYS `usertemp` mount onto the same place. Unit 1 rev-1 allowlisted only `<home>/.claude/`, so it
would have denied every legitimate temp write. Measured over the real corpus of 23,966 historical Bash
tool calls, that predicate denied 123 commands and **73 of them were legitimate** — including the
exact `export TMPDIR=…` workaround `memory/guides/SESSION-KICKOFF.md:225-226` prescribes, which unit
1's own bar run depends on. Rev-2 derives the allowlist from `TMPDIR`, `TEMP` and `TMP` at hook start.
That is also the literal reading of the owner's rule, "scratchpad/temp and nowhere else".

**A guard with no string handling denies the prose that describes it.** Rev-1 scanned raw command
text, so `git commit -m "fixes the > ~/.merge-bar.log litter"` — a message this very build writes —
would have been blocked. The sibling hook already solved this at `tools/hooks/agent-cap.js:65-72`;
rev-2 copies it.

**The `TMPDIR` retarget was dropped, and the reasoning kept.** It was specced, audited, and refused on
four measurements: there is no external root available on this machine; the Windows path spelling
breaks four arms of `check-template-size.test.sh`; rev-1's abandonment tripwire compared `pwd` against
`git rev-parse`, a divergence invariant under every `TMPDIR` value, so it could never have fired; and
the carrier could not be verified in-session. The reasoning stays in that spec's §4 because the next
session will have the same idea.

**What replaced it is the root cause.** `%TEMP%` holds 6865 entries on node `a` and **4905 are
`mrecall-*`** — `TOOL-aBranchedMandate-6`, OPEN since 2026-08-17 at 3,616 and still growing. The
crowding the retarget was working around is 71% one defect, and the repo already documents the correct
Windows remedy in `tools/memory-recall/query.py:483-494`.

## Units — the authored roster (M2)

Unit 1 stands alone and delivers the whole of the reported problem. Unit 2 clears what is already
there and repairs the leak that keeps refilling it.

<!-- roster:units -->
| # | Unit | Tier | Mechanism |
|---|---|---|---|
| 1 | `TOOL-aTetheredScratch-1` | 2 | a `PreToolUse` guard whose allowlist is derived from the temp roots |
| 2 | `TOOL-aTetheredScratch-2` | 2 | the sweep, and the read-only-git-object cleanup behind 71% of the crowding |
<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** INPROGRESS · 2 unit(s) · node a · opened 2026-08-20 · streams tooling
ids TOOL-aTetheredScratch-1 TOOL-aTetheredScratch-2 TOOL-aTetheredScratch-3 TOOL-aTetheredScratch-4

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-aTetheredScratch-1 — a PreToolUse guard that denies a home-directory write outside the sanctioned scratch roots](spec/2026-08-20-spec-TOOL-aTetheredScratch-1.md) | — | 2 | INPROGRESS | rev-2 | 2026-08-20 |
| [TOOL-aTetheredScratch-2 — sweep the litter, and stop the leak that is 71% of the crowding](spec/2026-08-20-spec-TOOL-aTetheredScratch-2.md) | — | 2 | INPROGRESS | rev-3 | 2026-08-20 |
<!-- /gen:build-units -->

Records: 1 bound to this build, across 2 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: none — every unit id has one.
<!-- /gen:build-index -->

<!-- gen:build-order -->

*No spec under this build declares an `order` verb; the build order is whatever its authored plan states.*
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->