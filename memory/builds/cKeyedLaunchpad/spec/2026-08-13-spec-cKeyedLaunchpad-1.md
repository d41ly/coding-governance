# KICK-cKeyedLaunchpad-1 — the installed engine, and why link-ness is the wrong thing to check

**Status:** OPEN · rev-2 · 2026-08-13 · node c · Tier-1 · base f006691f · streams tooling+kickoff

## 1. Goal

Make a stale or copied `/session-kickoff` install visible at every session start, so the engine a
session actually runs can be trusted to be the engine this repo tracks. Finding F1 in the build
README was found by hand; nothing reports it.

## 2. Scope (IN)

- S1. `tools/check-wiring.sh` gains a `skill` check reporting on the machine-level install at
  `${HOME}/.claude/skills/session-kickoff`.
- S2. The check compares CONTENT, not link-ness: the three shipped files
  (`SKILL.md`, `MANIFEST-TEMPLATE.md`, `manifest-check.sh`) against their tracked counterparts, with
  CR normalised on both sides before comparison. The comparison is CONDITIONAL on a tracked source
  existing in the repo under inspection; where it does not, the check skips.
- S3. Its `--check` report uses the file's existing `ok` / `skip` / `UNWIRED` vocabulary and carries a
  `Fix:` line holding the platform-appropriate junction command from `WIRE-INTO-PROJECT.md` §1.
- S4. Arms in `tools/check-wiring.test.sh`, one per state, each asserting the specific message text.

## 3. Non-goals (OUT)

- **`--fix` must not repair this.** The install lives outside every repository. `DEPL-aSealedCaravan-2`
  records that the deployer's own security rule forbids an out-of-tree write, and a wiring script that
  creates a junction in the user's home directory is that write. `--fix` prints the command and stops.
- **Not a merge-bar leg.** The install is machine state that travels with no commit, so a leg would
  red the bar for a reason unrelated to the diff. This is the shape the manifest already records for
  `merge.rows.driver`: a broken value reads as configured to every check but one, and the remedy is a
  local command, not a commit. SessionStart reporting is the whole delivery.
- No change to what the engine does, to `WIRE-INTO-PROJECT.md` §1, or to the install mechanism itself.
- No detection of a junction pointing at a DIFFERENT `coding-governance` checkout beyond what the
  content comparison already reports.

## 4. Design

### Why content and not link-ness

The obvious check — is the install a symlink or junction — cannot be written reliably here and would
be weaker if it could. Under MSYS git-bash an NTFS junction is not reported by `test -L`; it presents
as an ordinary directory. A link test would therefore report every correctly-junctioned Windows node
as a copy.

The deeper objection is that link-ness is a proxy. What matters is whether the installed bytes equal
the tracked bytes. A junction pointing at a stale second checkout passes a link test and fails the
question the check exists to answer. Comparing content answers it directly and is portable.

### States and reports

| Install state | Report | Exit contribution |
|---|---|---|
| Directory absent | `skip     skill     — /session-kickoff not installed on this machine (WIRE §1)` | none |
| Installed, but no tracked `skills/session-kickoff/` in the repo under inspection | `skip     skill     — the kickoff kit is not adopted in this repo; the install is machine-global (WIRE §1)` | none |
| Three files byte-equal to tracked, CR-normalised | `ok       skill     — installed engine matches tracked` | none |
| Any file differs | `UNWIRED  skill     — installed <file> differs from tracked; this session is running a different engine. Fix: <junction command>` | non-zero under `--check` |
| Directory present, a shipped file missing | `UNWIRED  skill     — installed engine is missing <file>. Fix: <junction command>` | non-zero under `--check` |

### The adopting repo is the common case, not the edge

`check-wiring.sh` is a copy-in kit: the runbook instructs copying it into an adopting project's
`tools/`, and it operates on `$ROOT`, the repo under inspection. That repo has the machine-global
junction — that is the whole point of installing it once per machine — and no tracked kickoff-kit
source to compare against.

Without the second skip state, the check reports `UNWIRED` at every SessionStart, in every adopting
repo, forever, with a `Fix:` line naming a command the operator has already run. Every other arm in
that file resolves both install prefixes and skips when the kit is not adopted; the recall arm's own
comment records why, in terms — a permanent false alarm is the fastest way to train every node to
ignore the wiring verifier.

One claim from the audit finding does not survive and is not repeated here: `--check` is not a gate
leg, so this is SessionStart noise rather than a red bar. That makes it cheaper, not acceptable.

### The CR half

`skills/session-kickoff/SKILL.md` carries an `eol=lf` pin, and this fleet runs `core.autocrlf=true`.
A Windows checkout can therefore hold CRLF in the installed copy while the tracked blob is LF. The
manifest already records the general rule: a gate that byte-compares a generated file needs both an
`eol=lf` pin and CR normalisation in the comparison, and either alone leaves the file green only
right after a render. Both sides of this comparison are normalised through the same filter, so a
CRLF copy reports `ok` rather than a false stale.

### Files touched (estimate)

| File | Change |
|---|---|
| `tools/check-wiring.sh` | one check block, following the existing per-check shape |
| `tools/check-wiring.test.sh` | four arms, one per state |

### Alternatives rejected

- **A `test -L` link check.** Wrong on MSYS, and weaker than content comparison even where it works.
- **A merge-bar leg.** Reds the bar on machine state, which no commit can fix.
- **Auto-repair in `--fix`.** An out-of-repo write, refused on the grounds `DEPL-aSealedCaravan-2`
  already established.

## 5. Production-readiness checklist

- security — the check reads two directories and writes nothing; the out-of-repo write is an explicit
  non-goal.
- perf / scale — three file comparisons at SessionStart.
- a11y — N/A, terminal output.
- i18n — N/A.
- error / empty / loading states — the absent-directory and missing-file states are enumerated above.
- observability — the report line IS the observability.
- risks — a false `ok` if both sides are stale together, which is impossible: the tracked side is the
  working tree.
- testing + left-shift gates — S4; the existing `tools/check-wiring.test.sh` leg carries it.
- migration / rollback — none; the check is additive and reports only.
- user docs — one line in `WIRE-INTO-PROJECT.md` §1 pointing at the new report.

## 6. Acceptance criteria

- AC1. When the install directory is absent, `bash tools/check-wiring.sh --check` prints a line
  beginning `skip     skill` and does not contribute a failure.
- AC2. When the installed `SKILL.md` differs from the tracked one, `--check` prints a line beginning
  `UNWIRED  skill` that names `SKILL.md` and carries a `Fix:` remedy, and `--check` exits non-zero.
- AC3. When all three files are byte-equal to tracked, `--check` prints a line beginning `ok       skill`.
- AC4. When the installed copy differs from tracked only by CRLF line endings, AC3's `ok` line is
  printed — not AC2's.
- AC5. When `--fix` runs against a stale install, the install directory's contents are byte-identical
  before and after, asserted in the test rather than argued in prose.
- AC6. Each arm in `tools/check-wiring.test.sh` asserts its specific message text; no arm passes on an
  exit code alone.
- AC7. When the install directory exists but the repo under inspection tracks no
  `skills/session-kickoff/`, `--check` prints a line beginning `skip     skill` and contributes no
  failure. The fixture is adopter-shaped: a repo with the kit copied into `tools/` and no tracked kit
  source. Without this arm the check is a permanent false alarm in every adopting repo.

## 7. Gates

- `bash tools/check-wiring.test.sh` — the existing leg, extended by S4.
- `bash tools/run-gates.sh` — the full bar, green at the push boundary.
- No new gate leg. The rationale is §3's second non-goal.

## 8. Open questions

none — the forks this unit could have carried were resolved before authoring. `--fix` behaviour is
settled by `DEPL-aSealedCaravan-2`, and the content-versus-link-ness choice is settled by the MSYS
constraint in §4.

## 9. Revision log

- rev-1 · 2026-08-13 · initial draft.
- rev-2 · 2026-08-13 · folded the M4 spec audit, review record 1. H9: the state table assumed the repo
  under inspection was this one, so an adopting repo — which has the machine-global install and no
  tracked kit source — would have reported UNWIRED at every SessionStart forever. Added the fifth
  state, made S2's comparison conditional on a tracked source, and added AC7 with an adopter-shaped
  fixture. §5's exhaustiveness claim now holds.

## 10. Reuse audit

The seam is `tools/check-wiring.sh` itself: it already owns per-check detection, the
`ok` / `skip` / `UNWIRED` vocabulary and the `Fix:` remedy convention, and it already runs at
SessionStart through `.claude/settings.json`. This unit adds one check block to that file and adds no
new script. `reuse_lookup.py "report whether an installed tool matches its tracked source"` returns
`check-wiring.sh` and `kit-dogfood-parity.PAIRS`; the latter is the byte-compare pattern this unit's
CR normalisation follows, but it compares two in-repo paths and cannot be pointed outside the tree,
so it is cited as prior art rather than extended.

Recall terms used: `kickoff manifest ratchet last-audit watch verify-paths SESSION-KICKOFF discovery
order traps accretion size gate prose`.
