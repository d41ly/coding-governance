**Serves:** journal TOOL-aLevelledCopy-7 TOOL-aLevelledCopy-8 TOOL-aLevelledCopy-9

# Spec brief — the closing review's promotions, units 7 to 9

The closing diff review's round 1 is CONVERGED with zero blockers, one high and fourteen minors:
`memory/builds/aLevelledCopy/reviews/2026-10-09-review-TOOL-aLevelledCopy-1-closing-diff-round1.md`.
Read it whole. Its fixes were judged by a skeptic, and one, M5's, was judged UNSOUND and corrected
in the report. By the build method's M4, every confirmed finding is PROMOTED: one unit for the high,
and the minors batched into two units across disjoint write sets. Every spec here is Tier-2 with the
full ten sections, `status OPEN`, `rev-1`, `node a`, `base ce9192c0` and `streams tooling`. The first
brief beside this file, `2026-10-09-prompt-TOOL-aLevelledCopy-1-1-spec-brief.md`, states the
invariants that still bind: no suite in a pass, staged breaks observed, no §6 path a unit creates,
and §7 legs per `check-spec-tokens.py --list`. Name the specs you author by unit id.

Order: TOOL-7 is `order 3`; TOOL-8 is `order 4`, because it writes `tools/check-wiring.sh` after
TOOL-7; TOOL-9 is `order 3`, and its write set is disjoint from both.

## TOOL-aLevelledCopy-7 — the ssh arm stands back when the operator chose an SSH program

Closes H1 (id 3) and M1 (id 9), one root cause. git resolves SSH as `GIT_SSH_COMMAND`, then
`core.sshCommand`, then `GIT_SSH`, so a repo-local `core.sshCommand` written at SessionStart
silently replaces an operator's plink or Windows OpenSSH. Before the set and UNWIRED branches of
`check_ssh_keepalive`, treat any of these as the operator's choice: a non-empty `GIT_SSH`, a
non-empty `GIT_SSH_VARIANT`, or a set `ssh.variant` at any scope. Print a `note ssh` line naming
which one, write nothing, count nothing. `--check` must then NOT print a Fix line telling the
operator to set `core.sshCommand`. Header: the does-not-check list names `GIT_SSH`. Gate: LC2 arms
in `tools/check-wiring.test.sh`, one per trigger (`GIT_SSH=/bin/false`, `GIT_SSH_VARIANT=ssh`,
`ssh.variant` in the fixture's global file). Each asserts the note, an unset key and no UNWIRED,
and each is observed RED against the current arm first. Also amend TOOL-aLevelledCopy-2's spec?
NO: a closed spec stays closed. This unit's spec carries the change, and its §3 Edges names unit 2
as `consumes-from`.

## TOOL-aLevelledCopy-8 — the ssh arm's failure states each get a verdict and an arm

Batches M3 (16), L1 (5, 10), M4 (6), M5 (7), M7 (13) and L2 (14). One write set: `tools/check-wiring.sh`,
`tools/check-wiring.test.sh`, and whatever M5's chosen mechanism needs.
- **M3 and L1**: a failed `git config core.sshCommand` write prints `UNWIRED ssh — could not set …`
  and counts. Id 10 asks for the same else-branch in the pre-existing hookspath arm, and consistency
  favours doing both. Gate: a held `.git/config.lock` (chmod is unreliable on MSYS), `--fix`, then
  assert UNWIRED and exit 1, with a twin for hookspath.
- **M4**: decide set-versus-unset with plain `git config --get core.sshCommand`, where exit 1 is the
  only "unset". `--show-scope` is used only for the label, and any other status is a `note` that
  writes nothing. Gate: shadow `git` with a function that exits 129 on `--show-scope`. The report
  also asks you to grep check-wiring for other `2>/dev/null || true` reads that feed a write
  decision; list what you find in §4 and fix only those this arm owns.
- **M5**: a new check-wiring beside an older push-main reds `--check` and the shipped self-test.
  The finder's fix (downgrade to `note`) was judged UNSOUND: a deleted line in gov would then pass.
  Read the report's corrected fix, then decide among: (a) `requires = ["push-main"]` on the
  check-wiring descriptor, which forces the lander onto every check-wiring adopter (weigh that against
  M3 veto 2); (b) govkit holding check-wiring whenever push-main is held or out of scope;
  (c) `derive_marker_coupling` in `tools/govkit/govkit.py`, an existing seam that already makes kits
  "move TOGETHER" when one ships another's marker; (d) a reworded `n=0` message naming kit skew plus
  a self-test skip outside gov only. Record the fork in §8 and resolve it under M3. If the pick
  writes `tools/govkit/*`, it collides with TOOL-9's write set: say so, and move that half to
  TOOL-9 or sequence TOOL-9 before you.
- **M7**: an LC2 arm seeds `GOV_SSH_KEEPALIVE='ssh'$(touch "$D/ran")` and asserts `$D/ran` is absent,
  `cannot derive` is printed and the key is unset. Observe it RED against an `eval`-based derivation.
- **L2**: arms for `C:/x/origin.git` (skip, nothing set) and `ssh://git@example.invalid/o/r.git`
  (FIXED under `--session`).

## TOOL-aLevelledCopy-9 — receipt fixtures are hermetic, a renamed row keeps its bit, the records agree

Batches M2 (4, 12), M6 (8), L3 (15), L4 (18) and L5 (19). Write set: `tools/run-gates/check-receipt.py`,
`tools/govkit/govkit.py`, `tools/govkit/selftest.py`, and this build's records.
- **M2**: each fixture's `[core]` sets `attributesFile` to a non-existent in-fixture path, spawns run
  with `GIT_ATTR_NOSYSTEM=1`, and `git init --object-format=sha1`. The docstring says exactly what
  is pinned. Gate: a CLASS arm (fixture-inherits-ambient-machine-state) running `check_git_arms`
  with `HOME` and `XDG_CONFIG_HOME` at a scratch dir whose `git/attributes` holds `* text=auto
  eol=lf`, and `GIT_CONFIG_GLOBAL` setting `init.defaultObjectFormat=sha256`. All arms must still
  pass, and RED must be observed with the pins removed.
- **L3**: a built-in arm with no `.git` and one CRLF engine row carrying an LF sha256 and oid:
  one DRIFTED, one `GIT … not consulted` line, eol-only 0.
- **M6**: the renamed arm of `update` must resolve the landed mode from the OLD path's index entry,
  because `index0` predates `git mv`. Pass the entry mode into `land_through_index`, or use the
  acted entry's `mode_to`. Gate: a `check_mode_carry`-style arm per touching verdict that lands
  through `land_through_index` (renamed at least), asserting never-down.
- **L4**: the main loop already dropped the authored Status column from the README roster, in the
  disposal commit. The left-shift is yours to choose: a hygiene refusal of a Status column in an
  authored `roster:units` table (memory-tree kit, a wider write set), or a `memory/gotchas/` class
  record (which needs `gotchas.py --write` and a codebase-map dossier claim). Prefer the gotcha
  unless the gate is cheap. Say which in §8.
- **L5**: spec 3 AC6 names `WSL ext4`, but the run was on WSL `/tmp`, which is tmpfs. TOOL-3 is
  CLOSED, and editing a CLOSED spec after its build commit risks the pass-order history leg reading
  spec-after-code. Decide between a rev-3 bump of spec 3 with its §9 line, and recording the
  correction in this unit's ledger as the AMENDED form against TOOL-3, after checking how
  `tools/unattended/` grades a later spec commit on a CLOSED unit. Record the choice in §8.
