**Serves:** research TOOL-dGroundRules-40

# Probe brief — TOOL-dGroundRules-40 against the built branch, before its builder starts

## The prompt

> A read-only spec review at HEAD 74d17b3a0 found: AC3 cannot red, since a raw `startswith` in either direction answers `False` for `tools/policy/a.py` against `tools/policy/ab.py`, and TOOL-dGroundRules-34 rev-9 now hands its AC17 to this AC3; the probe found `tools/policy` against `tools/policy-x.py` answers `True` under a raw compare, `False` under `check_writes_intersect` and `1` under `overlaps`, keeping the directory without its trailing slash; `PAIRS_SH` sources a bare `lib-unattended.sh` and names `x.py`, so it fails with `No such file or directory`, though spelled whole it prints `0` then `1`; the arm already exists at `tools/check-spec-tokens.test.sh` from TOOL-dGroundRules-32 (5412bbecd), running exactly two pairs graded against fixed answers, so §1's claim that it compares the two rules only with each other and the parity-alone alternative are stale and only the table with per-row, per-rule naming remains; §3 cites `lib-unattended.sh:741-750` for a string-prefix trap those lines do not document (the only such note is `check_guard_trips` in `tools/memory-tree/design_lib.py`); §4's citations into TOOL-dGroundRules-34 drifted; this spec carries no edge for what TOOL-dGroundRules-34 rev-9 hands it (AC17, and the wrong arm comment in `tools/check-spec-tokens.test.sh` claiming a raw prefix compare calls the a.py/ab.py pair overlapping); and `ARM_ROWS` greps a literal `tools/` path while the arm spells paths through `${PFX}` and runs at three prefixes.

## The brief

### Goal
Revise `memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-40.md` to the run's rulings below. Author only: no product code, no commit, no gate.

### Items
1. The string-prefix pair becomes `tools/policy` against `tools/policy-x.py` in §4's arm table row 2, `PAIRS_PY`'s second print, `PAIRS_SH`'s second `overlaps`, `ARM_ROWS`, and S1's and §3's wording; keep the new pair inside fenced blocks.
2. `PAIRS_SH` sources `tools/unattended/lib-unattended.sh` and names whole paths.
3. §1, AC1 and §4 restate the arm as built by TOOL-dGroundRules-32; what this unit adds is the table and per-row, per-rule failure naming.
4. A §2 item corrects the arm comment in `tools/check-spec-tokens.test.sh`, and §3 gains the consumes-from edge from TOOL-dGroundRules-34 naming its AC17 (observed by this AC3) and the comment.
5. §3's string-prefix citation points at `check_guard_trips` in `tools/memory-tree/design_lib.py`; keep the `covers`/`overlaps` citations.
6. `ARM_ROWS` greps the spelling the table actually uses (`${PFX}`-relative), and the spec says which.
7. Cite TOOL-dGroundRules-34's criteria by AC id, not line.
8. The status header's rev rises by one, with a §9 line naming the disagreements and the rulings. Keep the file under 48600 bytes measured with its records region; every §6 code span stays on one line; introduce no retirement word in §2; no code span holds a path glued to a quote or a `rev:path` token, and an untracked or fixture-relative path sits inside a fenced block or carries its target placeholder.

### Acceptance
`python tools/check-spec-tokens.py` exits 0 with this spec read as INPROGRESS (the main loop runs it); every `**Carries:**`/`**Derived:**` line, the H1 and the §8 RESOLVED marks survive; every §6 code span sits on one line.

### Gates
No gate runs in this pass.

### Non-goals
Any other spec; product code; the status cell, which stays `DEFERRED`.

### Limitations
The probe read HEAD 74d17b3a0; TOOL-dGroundRules-34 builds before this unit and was uncommitted while it ran.

### Reuse
The probe record `memory/builds/dGroundRules/prompts/2026-10-24-prompt-TOOL-dGroundRules-39-1-spec-reviewer.md`'s run.
