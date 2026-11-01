# TOOL-dTendedCadence-41 — the session-start hook launched by `bash` through a kit shim that resolves python, never rendered as `node .../maintain_session.py`

**Status:** OPEN · rev-2 · 2026-11-01 · node a · Tier-2 · base f4597719 · streams tooling · order 19 · advances TOOL-dTendedCadence-19

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-01-build-TOOL-dTendedCadence-1-agent-ledger.md](../build/2026-11-01-build-TOOL-dTendedCadence-1-agent-ledger.md) | journal | TOOL-dTendedCadence-1 TOOL-dTendedCadence-2 TOOL-dTendedCadence-3 TOOL-dTendedCadence-4 TOOL-dTendedCadence-5 TOOL-dTendedCadence-6 TOOL-dTendedCadence-7 TOOL-dTendedCadence-8 TOOL-dTendedCadence-9 TOOL-dTendedCadence-10 TOOL-dTendedCadence-11 TOOL-dTendedCadence-12 TOOL-dTendedCadence-13 TOOL-dTendedCadence-14 TOOL-dTendedCadence-15 TOOL-dTendedCadence-16 TOOL-dTendedCadence-17 TOOL-dTendedCadence-18 TOOL-dTendedCadence-35 TOOL-dTendedCadence-36 TOOL-dTendedCadence-37 TOOL-dTendedCadence-38 TOOL-dTendedCadence-39 TOOL-dTendedCadence-40 TOOL-dTendedCadence-42 TOOL-dTendedCadence-43 TOOL-dTendedCadence-44 TOOL-dTendedCadence-45 TOOL-dTendedCadence-46 TOOL-dTendedCadence-47 TOOL-dTendedCadence-48 TOOL-dTendedCadence-49 TOOL-dTendedCadence-50 TOOL-dTendedCadence-51 TOOL-dTendedCadence-52 TOOL-dTendedCadence-53 TOOL-dTendedCadence-54 TOOL-dTendedCadence-55 TOOL-dTendedCadence-56 TOOL-dTendedCadence-57 TOOL-dTendedCadence-58 TOOL-dTendedCadence-59 |
| [2026-11-01-review-TOOL-dTendedCadence-35-to-48-spec-audit-round1.md](../reviews/2026-11-01-review-TOOL-dTendedCadence-35-to-48-spec-audit-round1.md) | spec-audit | TOOL-dTendedCadence-35 TOOL-dTendedCadence-37 TOOL-dTendedCadence-42 TOOL-dTendedCadence-43 TOOL-dTendedCadence-47 TOOL-dTendedCadence-36 TOOL-dTendedCadence-46 TOOL-dTendedCadence-40 TOOL-dTendedCadence-38 TOOL-dTendedCadence-44 TOOL-dTendedCadence-45 TOOL-dTendedCadence-39 TOOL-dTendedCadence-48 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 30 of `reviews/2026-11-01-review-TOOL-dTendedCadence-1-to-18-spec-audit-round1.md`,
HIGH, item H6. Unit 2's fragment carries no `interpreter` key (spec-2 S5, :81-82), so
`tools/settings-merge.py` renders its command with the default `node` (`_INTERPRETERS = ("node",
"bash")`, `_DEFAULT_INTERPRETER = "node"`, `tools/settings-merge.py:247-248`; `render_command`,
`:282-287`), and the merged `.claude/settings.json` runs `node ".../maintain_session.py"`, which fails
at every session start while `settings-merge.py --check` still reports the hook wired. `python`
cannot be named, since `load_fragment` refuses an interpreter outside the pair (`:270-272`), and a
bare `python` would meet the Microsoft Store stub. This unit launches the hook as the repo already
launches a bash hook from a fragment, `tools/check-wiring.fragment.json`, through a kit shim that
resolves python.

## 2. Scope (IN)

- **S1** — The shim, `tools/drift-audit/maintain-session.sh`: it carries the inline `resolve_python`
  block under its `# >>> resolve_python` marker, since a copy-installed kit cannot source
  `tools/lib/` (`tools/lib/pyrun.sh`'s header states that rule), resolves a launcher, exits 0 with one
  stderr line when none resolves so the session is never blocked, and otherwise `exec`s the resolved
  launcher on `maintain_session.py` beside it with stdin passed through. Observed by AC1 and AC2.
- **S2** — The fragment, `tools/drift-audit/maintain-session.fragment.json`: `"interpreter":
  "bash"`, `"marker": "maintain-session.sh"` and `"hook_path":
  "{kit}/drift-audit/maintain-session.sh"`, its other keys unit 2 S5's. The kit descriptor lists the
  shim as an `engine` file beside the hook. Observed by AC1.
- **S3** — The merge. `adopt-drift-audit.sh --scaffold` merges the fragment as unit 2 S5 says, and
  this repository's `.claude/settings.json` takes the merge, its command `bash
  "${CLAUDE_PROJECT_DIR}/tools/drift-audit/maintain-session.sh"`. Observed by AC1 and AC2.

## 3. Non-goals (OUT)

- Widening `_INTERPRETERS` with `python`. It is a closed pair for a stated security reason
  (`settings-merge.py:243-246`), and the bash shim reaches python without touching it.
- A `settings-merge.py --check` arm refusing a hook whose extension does not match its interpreter:
  the report's left-shift gate, a separate mechanism in another kit, not built here.
- The hook's behaviour: unit 2 S6, unchanged.

### Edges

- **consumes-from** `TOOL-dTendedCadence-2` — `maintain_session.py`, its fragment and the `session-start` host row whose readiness asks the fragment wired; this unit changes how the hook is launched
- **hands-off** `TOOL-dTendedCadence-59` — the shim's argv, the stale node entry, the map key, the Evidence count and the migration prose, which the minors batch repairs (review ids 13, 19, 22, 27, 30, 50, 51)

## 4. Design

### Evidence

- `tools/check-wiring.fragment.json` declares `"interpreter": "bash"` with a `.sh` hook path, the one
  fragment in the tree that does, and `load_fragment` admits it.
- `tools/process-monitor/procmon-session.fragment.json`, the shape unit 2 S5 copies, points at a `.js`
  hook, which is why its default `node` is right there and wrong here.
- `tools/lib/pyrun.sh:14-18` states that a kit copy-installed as a standalone directory carries the
  inline `resolve_python` block rather than sourcing `tools/lib/`.

### Inventory

| Minted | Kind | Naming cell |
|---|---|---|
| `maintain-session.sh` | file, `tools/drift-audit/` | none |

### Files touched (estimate)

- `tools/drift-audit/maintain-session.sh`: S1, new
- `tools/drift-audit/maintain-session.fragment.json`: S2
- `tools/drift-audit/kit.toml`: S2's `engine` row
- `.claude/settings.json`: S3
- `tools/drift-audit/selftest.py`: the cases of §6

### Alternatives rejected

- **`"interpreter": "python"`.** `load_fragment` refuses it by name, so `--scaffold` fails.
- **The shared `tools/lib/pyrun.sh` as the hook path.** It is gov-internal, and an adopter's drift-audit
  copy carries no `tools/lib/`.

## 5. Production-readiness checklist

- security — the command's first word stays inside the closed pair; the shim passes no argument from
  the payload to the shell, only stdin to python.
- perf / scale — one resolver run per session start, the cost every bash consumer of the block pays.
- error / empty / loading states — no python resolved prints one stderr line and exits 0; the hook's
  own failures stay unit 2 S6's.
- observability — the resolver's refusal line names the candidates it ran.
- risks — the inline block's parity is the `python resolver (behaviour + inline parity + idiom ban)`
  leg's, which the new marker enlists.
- testing — the criteria of §6.
- migration — `--scaffold` re-merges the fragment; the marker changes from `maintain_session.py` to
  `maintain-session.sh`, so a repo merged before this unit carries one stale entry the merge replaces
  by name.
- user docs — N/A — the hook is wired by the adopter, not named on a help page.

## 6. Acceptance criteria

- **AC1** — When `python tools/settings-merge.py --check --fragment
  tools/drift-audit/maintain-session.fragment.json` runs, it reports the hook wired, and
  `grep -c 'bash .*maintain-session.sh' .claude/settings.json` prints 1 and
  `grep -c 'node .*maintain_session' .claude/settings.json` prints 0.
  Red when: the merged command names `node`, or the fragment is refused.
- **AC2** — When the merged command is run as written, `bash tools/drift-audit/maintain-session.sh
  --dry-run` with a SessionStart payload on stdin, it prints the two argvs and the session id unit 2
  S6's `--dry-run` prints, and exits 0.
  Red when: the command fails to start the hook, or a missing launcher blocks the session.

## 7. Gates

`drift-audit selftest` · `settings-merge selftest` · `check-wiring self-test` · `lexicon naming predicates` · `python resolver (behaviour + inline parity + idiom ban)` · `hook destinations (every declared hook path ships)` · `policy fixtures` · `memory hygiene`

New arm: tools/drift-audit/selftest.py · covers AC2 · the merged command run over a planted payload, staged against a fragment with no interpreter key · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft, promoted from review id 30 (HIGH, item H6) of the round-1 spec
  audit.
- rev-2 · 2026-11-01 · §3 · the Edges gain the mirror of each edge the promoted units of the round-1 spec audit of units 35 to 48 declare toward this unit (unit 59); no scope, design or criterion moved.

## 10. Reuse audit

The seams reused are `tools/check-wiring.fragment.json`'s `bash` launch, `settings-merge.py`'s
`render_command` and `load_fragment` unchanged, and the inline `resolve_python` block.
`python tools/codebase-map/reuse_lookup.py "launch a python hook from a settings fragment through a bash
shim"` ranked `resolve_python` (fan-in 6, 74 installs, a SEAM), `resolve_bash` and
`run_fragment_merges`; `resolve_python` is the block S1 carries, so the shim extends that seam and
adds no resolver.

Recall terms used: `python tools/memory-recall/query.py "how is a spec audit finding promoted to a
repair unit placed after the unit it repairs" --terms "spec audit promoted repair unit order hands-off
consumes-from minors batch maintenance record key grammar over-pin"`
