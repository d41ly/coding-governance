**Serves:** journal TOOL-dSafePassage-23

# TOOL-dSafePassage-23 — acceptance ledger

The unit as built, at spec rev-2. In the canonical block of `tools/lib/resolve-python.sh` an accepted
candidate echoes the executable its probe printed only when the candidate's ordinal, `_rp_i`, is
above 2, which is to say it came from `python3`, `python` or `py`, and that path is a file; the
caller's override (`_rp_i` 1) and `GOV_PYTHON` (`_rp_i` 2) are echoed as given. The floor probe is
untouched, so it still binds every candidate. The block's comment says what an override names. All 75
marked copies, the population of S4's `git grep` less the canonical, were re-synced byte-identically by
replacing the old block text with the new. `help/python-floor.md` says an override is spawned as named.
`tools/lib/resolve-python.test.sh` gains arm (h) in section 1b. No deviation.

HOW EACH CRITERION WAS OBSERVED. No gate, suite or bar ran in this pass. Each criterion was observed
by sourcing the block over fakes under the run's scratch directory (`f23/`), each a two-line bash
script printing `<version> <path>`, with `<path>` the canonical file itself as the real file. Owed at
the close: the new arm (h) of `tools/lib/resolve-python.test.sh`, its RED-first observation on a block
copy that echoes the printed executable for every candidate, and the §7 legs, `install-prefix
self-test` and `manifest-check self-test` among them, the two suites id 35 found red.

**Evidences:** TOOL-dSafePassage-23
- AC1 — `GOV_PYTHON=<f23>/w/wrap bash -c '. "$1"; resolve_python' _ tools/lib/resolve-python.sh`, `wrap` printing `3.15 <the canonical's path>`, printed `<f23>/w/wrap`; the same command over HEAD's block printed the canonical's path (the red case).
- AC2 — `PATH="<f23>/shim:$PATH" GOV_PYTHON=python bash -c '. "$1"; resolve_python' _ tools/lib/resolve-python.sh`, the shim `python` printing `3.15 <path>` and appending a line to a counter, printed `python`, the counter holding 1 line; over HEAD's block it printed the path.
- AC3 — with `GOV_PYTHON` unset and `<f23>/fakes/python3` printing `3.15 <the canonical's path>` first on `PATH`, it printed `/c/projects/coding-governance/.claude/worktrees/unattended-dsafepassage-567339/tools/lib/resolve-python.sh`, the path printed; `resolve_python "<f23>/w/wrap"` printed `<f23>/w/wrap` (HEAD's block: the path).
- AC4 — `PATH="<f23>/low:$PATH" GOV_PYTHON=<f23>/w/wrap14`, `wrap14` printing `3.14 <path>` and every launcher name in `low/` printing `3.14`, exited 1 printing `resolve_python:   <f23>/w/wrap14: ran 3.14, below the floor 3.15` and `GOV_PYTHON is set to '<f23>/w/wrap14' and ran 3.14, below the floor 3.15`.
- AC5 — `git grep -n -e "GOV_PYTHON" -- help/python-floor.md` printed `help/python-floor.md:16:An override, \`GOV_PYTHON\` or the caller's own, is handed back and spawned as named.`
- AC6 — `python tools/lib/python_floor.py check` printed nothing and exited 0; a probe comparing every `resolve_python` block of the 75 copies, CRs dropped, to the canonical's printed `parity drift: []`.
- New arm (h) — its 18 lines run outside the suite in a scratch stand-in, with section 1b's `FLO` and `alias` fakes rebuilt: 4 assertions, 0 failures over the new block; over HEAD's block 3 of 4 failed (the GOV_PYTHON wrapper, the caller's override and `GOV_PYTHON=python` each yielded the real interpreter's path), the below-floor assertion holding on both.
