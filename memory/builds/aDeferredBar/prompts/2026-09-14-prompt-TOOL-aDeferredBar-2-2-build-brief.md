# Build brief — TOOL-aDeferredBar-2

**Serves:** journal TOOL-aDeferredBar-2

The pass this brief is handed to builds unit 2 of `aDeferredBar` at rev-3. The spec is
`memory/builds/aDeferredBar/spec/2026-09-13-spec-TOOL-aDeferredBar-2.md` and it is authoritative;
this brief adds only what the spec cannot carry — what two audit rounds settled, what unit 1 left
in the tree, and the rules the pass itself is bound by.

## What the pass builds

The fourth join, `bar`, in `tools/check-spec-tokens.py`: a backticked token in a §6 acceptance
bullet (section found by HEADING text) or on the §7 leg line that spells a bar or suite invocation
is a HIT for a non-terminal spec dated at or after `SPEC_DIRECT_CUTOFF`; the `--list` near-miss
lines; the checker-side refusal of a cutoff not strictly past the date of the commit that set it;
the conf key with its register comment; the ten self-test arms on shared scratch repos; the
template paragraph; the memory-tree version step; the manifest re-stamp; the dossier refresh.
The spec's §4 files table is the write set; declare it with `--dispatch` BEFORE the first edit.

## What the audits and unit 1 already decided, so the pass does not reopen it

- **The cutoff value is DERIVED at your build commit by both clauses**: the day after the LATER of
  the newest spec filename date on any ref or worktree and `git log -1 --format=%cs` of the commit
  you are about to make. Measured 2026-09-14 that is 2026-09-15; if the day has rolled, re-derive
  with the §4 Rollout commands and set what they return. The value is re-derived once more at
  landing by the main loop. No criterion carries the date as a literal.
- **The flag branch of `BAR` requires a NON-EMPTY value** (`GATE_(?:FULL|SELFTESTS)=\S`); a bare
  `*.test.sh` basename with no launcher inside a backticked §6 bullet STAYS a hit; a suite named in
  prose, in a `New arm:` line, in §4, or in a fenced body is NOT a hit and prints as `NEAR` under
  `--list` where the join saw a token at all.
- **Unit 1 landed at 48420340**: memory-tree is at `2.75` in nine carriers and unattended at
  `1.20`; your S7 step is `2.75` → `2.76` in every `tools/memory-tree/*.template.md` marker and every
  render, plus `KIT_MEMORY_TREE_VERSION`. AC11's count is DERIVED by the grep it names, not typed.
- **The manifest is 155 bytes under its 25600-byte cap** after unit 1's trim (C7 of
  `manifest-check.sh` says trim and never raise). Your S8 re-stamp touches `last-audit` and
  `last-body-change` only; do not grow the body.
- **`extract_acceptance` and `AC_HEAD`** are the spellings the lexicon accepted; `extract` is in
  the verb table. Run `python tools/lexicon/lexicon.py --suggest <name> --as py.function` before
  naming anything else.

## The rules this pass is bound by

- **No merge bar, no self-test suite, no `GATE_*=` prefix, no `run-selftests.sh`, no
  `run-unattended-gates.sh` in this pass.** Every arm's fixture is exercised by running
  `python tools/check-spec-tokens.py` (and `--list`) on the fixture DIRECTLY, as §6 spells; the
  suite `tools/check-spec-tokens.test.sh` is not run here — its verdict is the main loop's at
  `VERIFYING`, and you return that fact in `summary`. Observe each new arm's failing case RED by
  running the checker on the staged fixture before the arm is written.
- The join's own failing case is observed RED before it lands: a fixture spec dated at or after
  the cutoff with `GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh` in an AC bullet, the checker
  exit 1 naming `[bar]`.
- Author with Write/Edit, never a heredoc into a Python file: a backslash escape dies one layer in
  and the symptom never looks like quoting (six recorded instances in this repo).
- The waiver file is SHRINK-ONLY; do not add a row. If your first real run over the tree finds a
  hit dated at or after the cutoff, it is this build's to fix and cannot be, because the cutoff is
  past every tracked spec date by construction — report it in `summary` instead.
- Commit ONCE at the end of the pass with the unit id in the subject; flip the spec's status header
  to CLOSED in that same commit; write the acceptance ledger under `build/` per `memory/HYGIENE.md`
  "Acceptance ledger", one line per AC, `**Serves:** journal TOOL-aDeferredBar-2`.
- Then run `python tools/memory-tree/gotchas.py --for-diff HEAD~1..HEAD` and act on what it names
  before returning.

## What the pass must not do

- No edit to `tools/unattended/*`, `tools/workflows/*`, `.claude/settings.json` — unit 3's files.
- No edit to `memory/DECISIONS.md` or `memory/backlog/*.md` — shared records, main-loop only.
- No re-declaration of any leg ceiling; §5 prices the self-test leg and shares scratch repos
  instead.
- No widening of scope: a beneficial discovery goes in `summary` for the main loop to `--rescope`.
