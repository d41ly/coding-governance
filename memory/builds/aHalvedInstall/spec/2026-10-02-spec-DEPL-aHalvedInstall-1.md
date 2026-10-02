# DEPL-aHalvedInstall-1 — govkit reads each kit's declared required conf keys and names a gap

**Status:** INPROGRESS · rev-3 · 2026-10-02 · node a · Tier-2 · base cd90f7fa · streams deployer · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-02-build-DEPL-aHalvedInstall-1-1-acceptance-ledger.md](../build/2026-10-02-build-DEPL-aHalvedInstall-1-1-acceptance-ledger.md) | journal | — |
| [2026-10-02-prompt-DEPL-aHalvedInstall-1-0-run-mandate.md](../prompts/2026-10-02-prompt-DEPL-aHalvedInstall-1-0-run-mandate.md) | journal | — |
| [2026-10-02-prompt-DEPL-aHalvedInstall-1-2-build-brief.md](../prompts/2026-10-02-prompt-DEPL-aHalvedInstall-1-2-build-brief.md) | journal | — |
| [2026-10-02-review-DEPL-aHalvedInstall-1-closing-diff-round1.md](../reviews/2026-10-02-review-DEPL-aHalvedInstall-1-closing-diff-round1.md) | diff-review | DEPL-aHalvedInstall-2 DEPL-aHalvedInstall-3 DEPL-aHalvedInstall-4 |

<!-- /gen:spec-records -->

## 1. Goal

Every kit with a `[config]` table declares `required_keys_gate` and `required_keys_render`, and
nothing in govkit reads either list: the only reader is selfcheck check 7, which uses them as a
name set for `requires_if`. So a target conf missing a required key, or still holding the example's
`<...>` value, is silent in govkit until the kit's own adopter refuses mid-render. This unit makes
govkit read the two lists against the target's conf, in `check` and before `update` runs a kit's
regenerate, and name every gap by key.

## 2. Scope (IN)

- **S1** — One reader, `read_conf_key_gaps(target, d)`, in `tools/govkit/govkit.py` beside
  `run_kit_check`. It reads the kit's `[config].file` at the target, parses `KEY=` lines, and returns
  one `(key, state)` pair per key in `required_keys_gate` ∪ `required_keys_render` that is not in
  `[config].defaults`, where state is `absent` or `placeholder` (a value wrapped in `<` and `>`). A
  missing conf file makes every such key `absent`. Observed by AC1, AC2 and AC3.
- **S2** — `check` calls it per selected kit after the kit's check arm and reds one finding per gap,
  naming the kit, the conf file, the key and the state. Observed by AC1 and AC2.
- **S3** — `update`, in its re-render step, calls it for a kit before running that kit's
  `[[regenerate]]` argv, and prints one `govkit update — CONF GAP` line per gap of a
  `required_keys_render` key, naming the key. It also runs the kit's hole probes through the same
  helper `check` uses and prints one `govkit update — HOLE` line per undischarged hole. Neither line
  changes the run's disposition: the regenerate still runs and its own outcome still decides.
  Observed by AC4.
- **S4** — The hole-probe loop in `cmd_check` moves into one helper, `run_hole_probes`, that both
  verbs call. `check`'s finding text is unchanged. Observed by AC5.
- **S5** — `tools/unattended/kit.toml` moves `RESUME_SCHEDULE_CREATE` and `RESUME_SCHEDULE_DELETE`
  from `optional_keys` to `conditional_keys`, because the adopter requires them unless
  `RESUME_SCHEDULE` is `off`, and that condition is the hole's to grade (DEPL-aHalvedInstall-2).
  NOT OBSERVED by an arm: a list move check 7 accepts and nothing else reads.
- **S7** — Round 1's folds. An assigned value that is empty or whitespace-only is the state `empty`
  and is reported as ABSENT is (M2). An unreadable conf is the state `unreadable` and a finding, never
  a traceback, in both verbs (M8). drift-audit's `[config]` declares the `MEMORY_ROOT` default its
  adopter and engine already apply, so the reader stops reporting a false gap (M1); and a selfcheck
  arm refuses a required key a kit's own adopter defaults while its descriptor does not, so the
  declaration and the adopter stay one answer. Observed by AC7, AC8 and AC9.
- **S6** — Every kit whose shipped bytes this unit moves is bumped where `govkit epoch` names it.
  govkit itself is not in that population, and is not bumped here. Observed by AC6.

## 3. Non-goals (OUT)

- **Conditional requirements.** A key required only under another key's value stays a hole's job;
  this unit adds no condition syntax to `[config]`.
- **Value validation** beyond the `<...>` example shape. Whether a value is RIGHT is the kit's own
  check.
- **Changing `update`'s disposition** on a gap. Declining the regenerate would land the new
  templates with a stale render, the state DEPL-cMendedVintage-1 had to unwind.
- **`plan`** keeps listing holes as orders without running them.

### Edges

- **hands-off** `DEPL-aHalvedInstall-2` — the `keepalive-tool-names` probe is narrowed there to the
  conditional pair this unit leaves to it.

## 4. Design

### Evidence

Read at base `cd90f7fa`. `required_keys_render` and `required_keys_gate` appear in `govkit.py` once,
in check 7's `key_lists` tuple. `[config].file` is read at three sites, none of which parses keys.
Every shipped kit conf is shell `KEY=VALUE`: `.unattended.conf`, `.memory-tree.conf`,
`.codebase-map.conf`, `.process-monitor.conf` and `.lexicon.conf`'s single-line keys.

### Data model

```python
CONF_KEY_RX = re.compile(r'^([A-Z][A-Z0-9_]*)=(.*)$')

def read_conf_key_gaps(target, d) -> list[tuple[str, str]]:
    cfg = d.get("config") or {}
    want = [k for k in dict.fromkeys(list(cfg.get("required_keys_gate") or [])
                                     + list(cfg.get("required_keys_render") or []))
            if k not in (cfg.get("defaults") or {})]
    ...  # parse the conf once; a value stripped of one layer of quotes and wrapped in <> is a placeholder
```

The parse takes the LAST assignment of a key, as `source` would.

### Rollout

A target whose conf already carries every required key sees no new line. A target missing one gets a
named `check` finding where before it got the adopter's unnamed placeholder refusal.

### Files touched (estimate)

- `tools/govkit/govkit.py`
- `tools/govkit/selftest.py`
- `tools/unattended/kit.toml`

### Alternatives rejected

- **A hole per kit for its required keys.** Six kits declare `[config]`; six probes restating six
  lists is the second copy this unit exists to remove.
- **Refusing `update` on a gap.** See Non-goals.

## 5. Production-readiness checklist

- security — the conf is read, never sourced: no target value is executed by govkit.
- perf / scale — one small file read per kit per verb.
- error / empty / loading states — an absent conf reports every required key absent; an unreadable
  one is a finding naming the read error.
- observability — every gap names the kit, the file, the key and the state.
- risks — an adopter conf missing a key it never needed would now red `check`; the lists are the
  kits' own declarations, so that conf was already one the adopter refuses.
- testing — selftest arms over a fixture conf, each observed red against its break.
- migration — none.
- user docs — N/A: no verb or flag changes.

## 6. Acceptance criteria

- **AC1** — When `python tools/govkit/govkit.py check --target <fixture>` runs over a fixture whose
  conf omits a `required_keys_render` key, the output names that key with `absent`.
  Red when: `read_conf_key_gaps` is not called from `check`.
  fixture: built by the selftest arm in a temp dir.
- **AC2** — When the same fixture's conf holds that key as `"<your-tool>"`, the output names it
  with `placeholder`; with a real value, no line names it.
  Red when: the placeholder test reads the raw value with its quotes still on.
- **AC3** — When the fixture's descriptor lists the key in `defaults`, an absent key is not named.
  Red when: `defaults` is not subtracted.
- **AC4** — When `python tools/govkit/govkit.py update --target <fixture> --write` re-renders a kit
  whose conf omits a render key, the output carries a `CONF GAP` line naming the key before the
  regenerate's own `ran` line.
  Red when: the call sits after the argv, or not in `update` at all.
- **AC5** — When `check` runs over the existing hole fixtures, the `UNDISCHARGED` and `stood down`
  lines are byte-identical to base.
  Red when: `run_hole_probes` drops the stand-down branch.
- **AC6** — When `python tools/govkit/govkit.py epoch` runs at the pass's commit, it prints no
  `FAILED` line.
  Red when: a kit whose shipped set the commit moves keeps its version.

- **AC7** — When `check` runs over a fixture conf holding `DEMO_KEY=""`, the output names the key
  as empty.
  Red when: an empty value is stored and passes as satisfied.
- **AC8** — When the fixture's conf path is a directory, `check` names it `unreadable` and `update`
  prints a `CONF GAP` line for it; neither raises.
  Red when: `read_text` is unguarded.
- **AC9** — When `python tools/govkit/govkit.py selfcheck` runs with drift-audit's `defaults` line
  removed, it names drift-audit and `MEMORY_ROOT`; with it, nothing.
  Red when: the arm does not read the adopter, so it cannot see the default.

## 7. Gates

`govkit selfcheck` · `kit epoch (shipped bytes move, the version moves)` · `govkit selftest` · `govkit refusal join` · `recall floor arms` · `govkit acceptance matrix`

New arm: tools/govkit/selftest.py · a fixture conf missing, placeholder-valued and defaulted · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-02 · initial draft, from the owner's first observation and govkit read at base.
- rev-3 · 2026-10-02 · S7 · AC7 · AC8 · AC9 · folded the closing review's round 1 M1, M2 and M8 (2026-10-02-review-DEPL-aHalvedInstall-1-closing-diff-round1.md).
- rev-2 · 2026-10-02 · build pass · S6 · AC6 · `govkit epoch` does not grade govkit itself, and
  `KIT_GOVKIT_VERSION` has stood at 1.12 across 66 commits to the file since `7bd70200`: it moves on
  release, not per change. S6 now bumps only what `epoch` names.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "read a kit's declared required config keys from the target conf"`
ranked name-stem neighbours only and printed `unscanned layers: .sh`. Its nearest real seam is
`parse_conf_line` in `tools/memory-tree/tree_lib.py`, the memory-tree kit's one conf-line parser. It
sits across a kit edge govkit does not import over, and this unit asks a narrower question — is the
key assigned, and is its value the example shape — so S1 parses `export`-prefixed and quoted
assignments and nothing more, and says so in its header. No govkit reader of the key lists exists:
they are named by check 7 only. The seams extended are `cmd_check`'s hole
loop, lifted into `run_hole_probes` so `update` reuses it, and the re-render step's per-kit loop in
`_cmd_update`, which already reads each kit's descriptor before its argv. The recall probe returned
TOOL-dRetiredFork-29 and TOOL-bQuiltedLantern-1, which made rendered rows refreshable but did not
touch conf keys.

Recall terms used: govkit update conflict rollback regenerate rendered vintage stale partial install hole discharge absent key

The question passed with them: "why does govkit update leave a kit half-installed when one row conflicts, and why does a renderer change roll back a kit".
