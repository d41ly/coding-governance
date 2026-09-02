# TOOL-dRetiredFork-19 — the pre-wiring run, and the acceptance ledger

**Serves:** journal TOOL-dRetiredFork-19

## The pre-wiring run (S5, AC5) — hits AND near-misses, before the leg was wired

`AGENTS.md` §7 requires a candidate predicate be run over the real tree before wiring, printing hits
AND near-misses. It earned its keep immediately.

### HIT — the first draft redded 17 innocent tokens across five kits

The predicate matched only the bare `{{TOKEN}}` spelling. Real adopters write the substitution as
`${out//\{\{KIT_DIR\}\}/…}` with the braces **backslash-escaped**, because bare braces there are
shell syntax — so the predicate found NOTHING in the one file it exists to read and reported every
declared token as unsubstituted. Redded: `drift-audit` (3), `lexicon` (6), `memory-recall` (3),
`memory-tree` (2), `unattended` (3). Every one innocent. Wired as drafted it would have blocked
every contributor on day one.

**Disposition:** fixed in the predicate — the scanner accepts both spellings — and pinned by the
self-test's escaped-spelling arm, which is the arm that stops it regressing.

### HIT — `workflows` reported as having no adopter

`tools/workflows/kit.toml` carries `argv = []` and a `why_no_adopter` reason: its render is
performed by the parity gate's own `--render` mode, not by a separate adopter. The draft redded it.

**Disposition:** the DECLARED exemption is now honoured, counted and NAMED on every green line,
because an exemption is not coverage. A kit with no adopter and **no** stated reason still reds, and
that pair is two separate arms.

### NEAR-MISS — a bare `K` reported as substituted-but-undeclared

`tools/unattended/adopt-unattended.sh:212` carries a comment using a placeholder literally named `K`
to explain bash replacement semantics. The scanner reads the whole file, comments included.

**Disposition:** left as-is, and stated in the dossier's Gaps. It can only ever add a spurious entry
to the REPORTED reverse direction, never cause a RED, because the gated direction is
declared-subset-of-substituted and a spurious *extra* cannot make a declared token go missing.

### The corrected run over the real tree

`6 kit(s) graded, 23 rule-token pair(s), 7 kit(s) declaring none, 1 exempt by a declared
why_no_adopter: workflows` — exit 0. The seven declaring none: `agent-instructions`, `codebase-map`,
`gate-lint`, `hooks`, `playbook`, `pytest-parallel-guardrails`, `run-gates`.

**A suspicion the run refuted.** The unit's brief predicted `AUTH_PARAM` was a live violation, since
the unattended descriptor declares eight placeholders while the spec measured seven substituted. It
is substituted; the spec's list was the incomplete one. Recorded because a prediction that survives
unchecked becomes a fact nobody re-measures.

## Acceptance ledger

**Evidences:** TOOL-dRetiredFork-19
- AC1 — `memory/builds/dRetiredFork/spec/2026-09-02-spec-TOOL-dRetiredFork-12.md` — §4 Data model now names ONE token; every surviving `TOOL_ROOT` hit is prose explaining its absence, and §10's is the shape precedent S2 requires, never a declaration
- AC2 — `python tools/check-kit-placeholders.py` — staged `TOOL_ROOT` into the unattended `placeholders` list, observed exit 1 naming both the token and `tools/unattended/adopt-unattended.sh`, reverted, re-observed exit 0. The RED was seen before the leg was wired
- AC3 — `python tools/check-kit-placeholders.py` — exit 0 naming `6 kit(s) graded, 23 rule-token pair(s)`
- AC4 — `bash tools/check-kit-placeholders.test.sh` — the empty-population arm asserts exit 2 and the word REFUSED against a fixture declaring no placeholders
- AC5 — `memory/builds/dRetiredFork/build/2026-09-02-build-TOOL-dRetiredFork-19-1-prewiring-run.md` — the pre-wiring run is recorded above with two hits and one near-miss, each dispositioned
- AC6 — `tools/gate-legs.json` — both legs carry a `ceiling` (60 and 120); `bash tools/check-testsuite-counts.sh` exits 0 because the suite prints `PASS (9 assertions)` against `FLOOR_ASSERTIONS=9`, so no waiver row is owed

## One defect in this unit's own self-test, recorded because it is the class the unit is about

The first suite ran every hermetic arm against the **real tree**: the gate resolved its root from
`__file__`, so `cd` into the scratch dir changed nothing, and three arms passed only because the real
tree happens to be green. That is `fixture-passes-by-finding-nothing` inside the suite written to
prevent it. `--root` was added for exactly this, and it is documented in the gate as existing for the
self-test rather than for operators.
