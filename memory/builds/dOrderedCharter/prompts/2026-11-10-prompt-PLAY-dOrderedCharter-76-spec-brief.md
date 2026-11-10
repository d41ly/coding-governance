**Serves:** research PLAY-dOrderedCharter-76

# Brief: spec 76 — unit 37's later commit, as a unit of its own

## The prompt

> I see that a lot of units are being refused this build and that's wasting tokens

— owner, 2026-11-10. Unit 37's later commit was refused at `--dispatch`: moving CLOSED spec 37 to INPROGRESS made it live, and the
spec-token check redded its AC12, whose backticked `python -c` command splits into a word the check reads as an untracked path. Spec
37 is CLOSED, and the build method freezes a CLOSED spec: a correction is a new unit on top. So the later commit becomes this unit.

## The brief

### Goal

Write spec 76, a new Tier-2 unit that builds what spec 37's section 8 F8, F10 and F11 deferred to its later commit, plus the four
items below, so no pass ever reopens spec 37.

### Items

1. **Where you write.** Write only this scratch file and nothing under the repository:
   `C:/Users/DAILY-~1/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unattended-dorderedcharter-725f52/0394fa33-012c-408f-a840-e6e4cfaac23f/scratchpad/fold76/2026-11-10-spec-PLAY-dOrderedCharter-76.md`
2. **Scope carried from spec 37.** Read spec 37 rev-7 whole. Carry its later-commit scope: the units `[[reference]]` row in
   `tools/playbook/references.toml` with an `h1` (PLAY-dOrderedCharter-40's F4 says why), its page under `help/reference/`, every
   reference row's `unit` field (F10); the unit-line check and every page's unit line (F11, S8); and the `unit-usage` class rows in
   `tools/govkit/surface-classes.toml` and `tools/govkit/usage.toml` (F8). Carry the criteria spec 37 left to the later commit: AC1's
   four-page half, AC8 and AC10's `unit-usage` half, each restated as this unit's own.
3. **Four further items**, from the main loop's observations after unit 37's first pass `19648821f` and its refused builder's plan:
   - The core meta-check reds the legs `help reference pages` and `help page commands`, which carry no `enforces` and no pending row.
     The builder's plan: give both `enforces: ["principle.p42"]` and delete the then-stale `principle.p42` row from
     `tools/playbook/core-pending.txt`, as PLAY-dOrderedCharter-20 did for p11. Confirm at HEAD.
   - The layers check reds `tools/playbook/render_playbook.py#read_fingerprint_lines`'s probe of the docs leg: core kit
     `playbook-render` depends on non-core kit `govkit`. The plan: an optional row for the file in `tools/playbook/kit.toml` at
     `point.runtime.install-target`, the point the policy kit uses for its own edge into govkit. Confirm at HEAD.
   - `tools/playbook/render_playbook.py#write_unit_usage_plant` removes a row with `replace(u.body, ...)`, which matches nothing on a
     CRLF checkout; PLAY-dOrderedCharter-33's later commit `4dd011712` fixed the same defect in `tools/playbook/pins.py#write_unit_plant`
     (its deviation 336). A second copy of that logic owes a shared helper by the reuse rule: say where it lives.
   - `help/step-gate.md`'s class table lists none of `unit`, `drive`, `kind` or `unit-usage`; bring it current.
4. **Header.** `**Status:** DEFERRED · rev-1 · 2026-11-10 · node a · Tier-2 · base <HEAD's short sha> · streams playbook · order 37 ·
   advances PLAY-dOrderedCharter-38`, plus the `**Derived:**` binding line every promoted unit of this build carries.
5. **Edges.** A consumes-from edge into a CLOSED spec reds memory hygiene's edge check unless that spec declares a hands-off back, and
   CLOSED specs are frozen: write `none` and name PLAY-dOrderedCharter-37, PLAY-dOrderedCharter-40 and PLAY-dOrderedCharter-33 as
   dependencies in prose, as spec 75 does.
6. **The spec-token check grades every live spec's acceptance bullets word by word**: a backticked span is split on whitespace and any
   word holding a `/` and a dotted last segment must be a tracked path. Write no acceptance command whose words break that rule; prefer
   `git grep` or a named script over an inline `python -c`.
7. **Every reader claim is a grep**, at HEAD, for anything this unit moves or retires.

Resolve each choice under the fork rule and record it in section 8.

In the spec: new text cites code as `path#symbol`, outside the acceptance bullets, which spell plain tracked paths; a section is named
in words and a check by what it checks; every new fact is pinned, keyed or marked PINNED or DERIVED; a unit is named by its id; every
function name it mints passes `python tools/lexicon/lexicon.py --suggest <name> --as py.function`.

### Acceptance

- Spec 76 builds as written over HEAD, carries spec 37's later-commit scope and the four items, and passes the spec-token check once
  live.

### Gates

None run: the main loop sweeps the spec and runs the spec-token check with it live before its dispatch.

### Non-goals

- No code. No edit to spec 37 or any file under the repository.
