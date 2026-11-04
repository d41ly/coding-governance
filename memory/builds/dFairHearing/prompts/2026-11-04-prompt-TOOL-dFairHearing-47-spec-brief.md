# Spec brief — TOOL-dFairHearing-47: the last of the bar's own reds

**Serves:** research TOOL-dFairHearing-47

## The prompt

> /unattended dFairHearing

— owner, 2026-11-02, the invocation that started this build run.

## The brief

### Goal
Write the spec for `TOOL-dFairHearing-47` at `memory/builds/dFairHearing/spec/2026-11-04-spec-TOOL-dFairHearing-47.md`. The close re-ran the bar's lint legs after unit 45 and found a few own reds left, plus two items unit 45's builder named and left. This is a mechanical unit, the build's last. Commit nothing; the main loop commits.

### Items
1. **shell hygiene (a loop fed by a command substitution):** `tools/check-hook-destinations.sh` (from unit 45's CR strip) and `tools/workflows/unattended-build.test.sh` (from unit 43) each have one site the leg reports as a loop fed by `<<<` holding a command substitution, with no registry row. Feed each loop from a scratch file, as the leg's message says. Do not add a registry row.
2. **govkit selfcheck:** `guard pathspec '.governance/install.json' (leg 'policy fixtures') falls into 0 declared classes`, from unit 45's guard line. Read the partition check at `tools/govkit/govkit.py:2297` and scope the honest fix. The fixture does read that file, so the guard must keep naming it.
3. **hook destinations self-test guard:** the leg's guard in `tools/gate-legs.json` lacks the workflows kit, which unit 45's new arm in `tools/check-hook-destinations.test.sh` resolves.
4. **The registry reason at `memory/project/unarmed-branches.txt:40`** cites `tools/check-install-prefix.test.sh:236`, now at 249. Confirm in `check-arms.py` whether that reason is graded, and correct the cite.
5. **The kickoff manifest:** this commit stages `tools/gate-legs.json`, so it bundles the `last-audit` re-stamp of `memory/guides/SESSION-KICKOFF.md`. The `kickoff-manifest ratchet` leg also needs `last-body-change` advanced: re-read the manifest's section B against this build's changes, make any correction it needs, and advance that stamp. Carry the `manifest-audit: delta` line in the commit message.

Write the unit's departure record the way unit 46's was written, and carry `order 31`, no ask clause, Tier-1. No path may pair a generated file with its generator. Spec status `OPEN`.

### Acceptance
A spec conforming to `memory/TEMPLATE-SPEC.md`, one criterion per item, each red on today's tree and green on a correct build. Keep backticked acceptance words clear of `tools/check-spec-tokens.py`: no `{` lead, no untracked path, no bare suite path, and no word matching its `BAR` pattern at lines 419 to 424. Every change-log line names a section, a scope id or an acceptance id. New text cites no check, section or method rule by a bare number.

### Gates
None you run.

### Non-goals
No code, no other spec.
