# TOOL-aScouredKit-35 — scratch-guard covers the drive root, not only the home directory

**Status:** CLOSED · rev-1 · 2026-08-31 · node a · Tier-1 · base 093730e4 · streams tooling

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

Extend `tools/hooks/scratch-guard.js` to deny a write that creates a NEW TOP-LEVEL entry at a drive
root, so agent scratch cannot land outside the repo, the scratchpad and the guard's reach.

## 2. Scope (IN)

- S1. A second rule beside the home rule: a write target of the form `<drive>:/<segment>` whose
  segment is not a conventional root is denied.
- S2. The conventional-root set is hand-listed and the refusal says so, naming the edit that widens
  it — the guard's other allowlist is DERIVED and this one cannot be.
- S3. The denial message distinguishes the two rules. One message covering both would name neither.
- S4. The predicate is chosen by MEASUREMENT over the real tool-call corpus, not by reasoning, and
  both the chosen and the rejected candidate are recorded with their numbers.
- S5. Arms in `tools/hooks/scratch-guard.test.sh` in both directions, proven discriminating.

## 3. Non-goals (OUT)

- Denying absolute writes generally. §4 records the measurement that refuses this.
- Resolving variables, following `cd`, or reading inside a heredoc. The guard's predicate is
  TEXTUAL by design and its header already states that ceiling; this unit does not move it.
- The home rule, which is unchanged.

## 4. Design

The guard's stated contract is "keeps agent scratch out of the home directory", and it does that
correctly. Everything OUTSIDE home was therefore unguarded — measured live: `~/.junk` is denied,
while `/c/gvi/f`, `/c/newlitter/f` and `/tmp/zz` all pass.

That gap is not theoretical. A completeness lens in this build's wave 3 built a throwaway adopter
fixture at `C:\gvi` — 7.2 MB, a full git repo with 185 deployed files — outside the repo, outside
the session scratchpad, and outside the guard. It survived the session and nothing would ever have
cleaned it up.

### Alternatives rejected — and this is the unit's real content

Two candidates were run over 128,568 real Bash and PowerShell tool calls from this operator's
history:

| candidate | hits | verdict |
|---|---|---|
| any absolute write outside repo + scratch roots + home | 2,449 distinct targets | REFUSED |
| creates a NEW top-level entry at a drive root | 16 calls, 10 targets | TAKEN |

The wide candidate is almost entirely `/tmp/...`, a legitimate scratch root on every POSIX machine;
it would red constantly and be switched off within a day. The narrow one hits `/c/t2`, `/c/gvi`,
`/c/gvt`, `/c/gkt`, `/c/gk2`, `/c/gfclone`, `/c/temp-hyg.txt` and three siblings — every one an
agent throwaway, and ZERO legitimate uses in the whole corpus.

This is the guard's own methodology: its header records a 23,966-call measurement behind the derived
allowlist, for exactly this reason.

## 5. Production-readiness checklist

- security — this DENIES more; it grants nothing. The predicate reads a already-extracted target.
- perf / scale — one regex per write target.
- a11y — N/A. i18n — N/A.
- error / empty / loading states — a target that does not parse as a drive-root path is ignored, so
  a relative path or `/dev/null` is untouched.
- observability — the refusal names which rule fired and how to widen the list.
- risks — a conventional root missing from the hand-list costs one denial whose message names the
  fix. Accepted deliberately: the alternative is deriving a filesystem convention from a machine,
  which has nothing to derive it from.
- testing + left-shift gates — `bash tools/hooks/scratch-guard.test.sh`, a merge-bar leg.
- migration / rollback — none; the hook is stateless.
- user docs — the refusal text.

## 6. Acceptance criteria

- **AC1** — When `mkdir -p /c/gvi`, `echo x > /c/temp-hyg.txt`, `mkdir C:/gvi` or
  `cp memory/x.md /c/scratch/inv/` is fed to the hook, it exits 2.
- **AC2** — When `/tmp/hyg.txt`, `$TMPDIR/bar.txt`, `/c/projects/incms/f.txt`,
  `/c/Windows/Temp/f.txt`, a scratchpad path or `/dev/null` is fed to it, it exits 0.
- **AC3** — When the `checkDriveRootLitter` branch is staged away from
  `tools/hooks/scratch-guard.js`, exactly the four new deny-arms FAIL under
  `bash tools/hooks/scratch-guard.test.sh` and the near-miss arms hold. Observed and recorded in §9.
- **AC4** — When `bash tools/hooks/scratch-guard.test.sh` runs unmodified, all arms hold.

## 7. Gates

`scratch-guard self-test` · `hook wiring` · the full bar at the push boundary.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-08-31 · built. AC3 OBSERVED: with `checkDriveRootLitter` removed from the decision,
  exactly `drive-root mkdir`, `drive-root redirect`, `drive-root windows spelling` and
  `drive-root cp DESTINATION` fail and nothing else does; restored, 70 assertions pass.
  TWO EXISTING ARMS were REPOINTED, not re-baselined, and the difference matters: `cp`/`mv`
  home-rooted SOURCE both used `/c/scratch/inv/` as their destination, which is itself litter under
  the new rule, so the fixture conflated two subjects. Their stated subject is the SOURCE, so the
  destination moved to `/tmp/inv/` and four new arms cover the destination case that was previously
  untested — coverage grew rather than moved.

## 10. Reuse audit

The seam is `scanWriteTargets` and `buildComparablePath`, both already in this file: the new rule
adds a predicate over targets the guard ALREADY extracts and normalises, and introduces no second
scanner. `checkUnderRoot` is deliberately not reused — it asks "is this under a root", and this rule
asks "is this a NEW root", which is the opposite question.
