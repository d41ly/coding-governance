# Build brief — TOOL-aRepatriatedFork-49

**Serves:** journal TOOL-aRepatriatedFork-49

A unit pass under the aRepatriatedFork mandate, promoted under BUILD-METHOD M4 from the round-2 closing diff review's H1. Build `memory/builds/aRepatriatedFork/spec/2026-09-30-spec-TOOL-aRepatriatedFork-49.md` exactly: the bar that certifies a default-branch push reads only the tracked leg manifest, through a python the environment did not name. `GATE_LEGS` and `GATE_REUSE` are unset before any bar not labelled STUB, `GOV_PYTHON` and every `*_PY` name are dropped beside `GOV_KITROOT`, and the runner's manifest is vetted with `check_reviewed_file`. The red-first control is the review's own repro: each of the four routes lands a RED tracked bar on the `ce8a78f5` hook.

## How to build this unit

The spec is the scope. Its section 8 forks are RESOLVED (agent, 2026-09-30, delegated) under the
mandate; do not reopen them. F3's option (b) is the owner's, not this pass's.

- **Spec before code.** The spec is already committed. If building shows the spec must change, commit
  that change FIRST as a records commit (rev bump plus a section 9 line stating the intent), then the
  code. The pass-order leg (`bash tools/unattended/check-pass-order.sh`) must stay green.
- **Red first.** Write the new `.githooks/pre-push.test.sh` arms before the hook moves, and run them
  as a slice against the `ce8a78f5` hook: every route must land there. Then change the hook and run
  the same slice again.
- **No bar and no whole suite inside the pass.** Verify with the direct checks the spec's section 6
  names. A long suite is SLICED: its prologue plus the block you changed, in a temporary script inside
  the kit dir, removed afterwards.
- **Leave these green** before committing, each by its own command: `bash tools/check-install-prefix.sh`,
  `python tools/govkit/govkit.py epoch --base f8fdd873`, `bash tools/check-kit-versions.sh`,
  `python tools/govkit/govkit.py selfcheck`, `python tools/lexicon/lexicon.py`,
  `python3 tools/gate-lint/encoding_posture.py memory/project/encoding-posture-sites.txt . tools skills`,
  `python3 tools/memory-tree/check-arms.py --check`, `bash tools/memory-tree/check-memory-hygiene.sh`,
  `python tools/memory-tree/gen_build_index.py --check` and `--check-format`,
  `bash skills/session-kickoff/manifest-check.sh`, `bash tools/unattended/check-pass-order.sh`,
  `python3 tools/codebase-map/test_codebase_map.py`. A kit whose shipped bytes move takes its version
  bump in EVERY carrier. A staged watched file owes a `last-audit` re-stamp and a `Manifest delta:` line.
- **Windows traps.** Working copies may be CRLF: edit with the Edit tool or binary-mode Python, never a
  text-mode rewrite of a `.sh`. Author scripts with the Write tool, never a bash heredoc carrying a
  backslash. Never `python -` without input. Scratch clones via `mktemp -d`, never a fixed name.
- **Commit** with the unit id in the subject, a `Decided: <choice> — <why>` trailer per choice, and
  `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` last. Never `--no-verify`.
