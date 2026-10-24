# TOOL-dDeclaredLoop-70 — every caller of the phase reading takes the adopter population from one driver-conf reader

**Status:** DEFERRED · rev-2 · 2026-10-24 · node d · Tier-2 · base ed497191 · streams tooling · order 36 · advances TOOL-dDeclaredLoop-35

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-TOOL-dDeclaredLoop-68-promoted-fix-return.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-68-promoted-fix-return.md) | research | TOOL-dDeclaredLoop-68 TOOL-dDeclaredLoop-69 TOOL-dDeclaredLoop-71 TOOL-dDeclaredLoop-72 TOOL-dDeclaredLoop-73 TOOL-dDeclaredLoop-74 TOOL-dDeclaredLoop-75 |
| [2026-10-24-build-TOOL-dDeclaredLoop-70-deviation-701.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-70-deviation-701.md) | deviation | — |
| [2026-10-24-prompt-TOOL-dDeclaredLoop-68-promoted-fix-brief.md](../prompts/2026-10-24-prompt-TOOL-dDeclaredLoop-68-promoted-fix-brief.md) | research | TOOL-dDeclaredLoop-68 TOOL-dDeclaredLoop-69 TOOL-dDeclaredLoop-71 TOOL-dDeclaredLoop-72 TOOL-dDeclaredLoop-73 TOOL-dDeclaredLoop-74 TOOL-dDeclaredLoop-75 |
| [2026-10-24-review-TOOL-dDeclaredLoop-68-spec-audit.md](../reviews/2026-10-24-review-TOOL-dDeclaredLoop-68-spec-audit.md) | spec-audit | TOOL-dDeclaredLoop-73 TOOL-dDeclaredLoop-69 TOOL-dDeclaredLoop-71 TOOL-dDeclaredLoop-72 TOOL-dDeclaredLoop-68 TOOL-dDeclaredLoop-74 TOOL-dDeclaredLoop-75 |

<!-- /gen:spec-records -->

## 1. Goal

The round-3 spec audit (`memory/builds/dDeclaredLoop/reviews/2026-10-24-review-TOOL-dDeclaredLoop-57-spec-audit.md`)
confirmed finding **id 19 at HIGH**, its item **H3**, alone in that item. `TOOL-dDeclaredLoop-63` S1 gives
`derive_phase_position` the parameter `extra=()`, and S2 feeds it only from the `--phase` consumer in
`tools/unattended/unattended.sh`. Every other caller gets the empty default and refuses an adopter phase by
name: `TOOL-dDeclaredLoop-31` S7's phase reading (named by `TOOL-dDeclaredLoop-52` S4),
`TOOL-dDeclaredLoop-56` S18's `read_withdrawn_parents`, and `TOOL-dDeclaredLoop-67` S13's held-from
resolution. That is the wedge round 2 graded high, on the paths 63 left out.

This unit takes the fix's second form: the population comes from one place every caller shares. The
default of `extra` stops being the empty tuple and becomes the driver's own answer, read once through one
reader of the driver's conf. It repairs `TOOL-dDeclaredLoop-63`.

## 2. Scope (IN)

- **S1** — `read_driver_conf(tree, names)` in `tools/loop/loop_lib.py`, the loop kit's one reader of a
  value the driver takes from `.unattended.conf`. It composes the value the way the driver does, by
  sourcing that file (`tools/unattended/unattended.sh:617`), in a bash subshell that prints each named
  value and then a sentinel, the import shape of `tools/unattended/check-unattended.sh:336-350`. Bash is
  the loop kit's own `resolve_bash` (`TOOL-dDeclaredLoop-42` S1), never a bare `bash`. It returns the
  names that are set; an absent `.unattended.conf` returns an empty mapping. Observed by AC1, AC4.
- **S2** — A failed read refuses by name: no bash resolved, a non-zero exit, or a missing sentinel each
  raise `driver conf unreadable: <path> — <reason>`, never an empty population, because an empty one
  would read every adopter phase as unknown and refuse it. Observed by AC4.
- **S3** — `derive_phase_position`'s `extra` defaults to `None`, which means
  `resolve_phases_extra(tree)`: the `PHASES_EXTRA` value of S1, split on whitespace and memoised per tree
  for the process. An explicit `extra`, the `--extra` 63 S2 has the driver pass, still wins. The CLI
  `loop_table.py phase` without `--extra` reads the same default. Observed by AC1, AC2.
- **S4** — Every caller is enumerated, with what it passes, in §4's table; none passes an explicit empty
  tuple. 31 S7's reading and `read_withdrawn_parents` call with the default. Observed by AC2, AC3.
- **S5** — The fixture cases `phases-extra-default` and `parent-in-extra-phase` join
  `loop_table.py --fixture`: a scratch tree whose `.unattended.conf` sets `PHASES_EXTRA="STAGING"`, read
  with no `--extra`, and a parent build whose run record holds `phase: STAGING`, read through
  `read_withdrawn_parents`. Observed by AC2, AC3.

## 3. Non-goals (OUT)

- `check_transition_tables`' own read of `PHASES_EXTRA` (`TOOL-dDeclaredLoop-67` S23): the audit's ids 20
  and 21, batched into `TOOL-dDeclaredLoop-75`, which points it at S1.
- The held-from lookup's code: `TOOL-dDeclaredLoop-67` S13 builds it at order 38 and inherits S3's
  default by calling `derive_phase_position` with no explicit `extra`, as its consumes-from bullet records.
- A checklist entry that a parameter added with a default enumerates its callers, the finding's
  left-shift: the class is recorded at the close; §4's table is this parameter's enumeration.

### Edges

- **consumes-from** `TOOL-dDeclaredLoop-63` — the `extra` parameter of `derive_phase_position`, the CLI's `--extra` and the adopter-phase reading, whose default this unit makes the driver's population
- **hands-off** `TOOL-dDeclaredLoop-56` — S18's `read_withdrawn_parents` call, which takes S3's default and passes no explicit `extra`
- **hands-off** `TOOL-dDeclaredLoop-67` — S13's held-from lookup, which takes S3's default and passes no explicit `extra`
- **hands-off** `TOOL-dDeclaredLoop-72` — `read_driver_conf`, through which that unit reads the driver's `MEMORY_ROOT`
- **hands-off** `TOOL-dDeclaredLoop-75` — `read_driver_conf`, to which that unit points `check_transition_tables` (ids 20, 21)
- **hands-off** `TOOL-dDeclaredLoop-79` — `read_driver_conf`'s subshell, which that unit isolates from the caller's environment and gives the driver's `ROOT` and `CONF` (ids 2, 16, 32)

## 4. Design

### Evidence

- The driver defaults `PHASES_EXTRA=""` (`tools/unattended/unattended.sh:560-561`) and then sources the
  conf (:617); `phases()` composes `PHASES_CORE` and `PHASES_EXTRA` (:1069). Read at base `ed497191`.
- `check-unattended.sh` imports conf values by sourcing `.unattended.conf` in a subshell, `|| exit 9`,
  printing NUL-separated pairs and the sentinel `__CONF_IMPORT_OK__` (:336-350); its comment records why
  the sentinel, not the exit code, is the verdict.
- `TOOL-dDeclaredLoop-63` §4 rejected parsing `PHASES_EXTRA` out of the conf's text in Python. Sourcing
  is not that: it is the driver's own composition, so a conf that computes a value reads as the driver
  reads it.

### The callers

| Caller | Spec | What it passes |
|---|---|---|
| the `--phase` refusal past a gated step | `TOOL-dDeclaredLoop-19` S6, 63 S2 | `--extra "$PHASES_EXTRA"`, explicit |
| the `--plan` adopter reading | 63 S3 | the driver's explicit value where the driver calls; else the default |
| the build-state phase reading | `TOOL-dDeclaredLoop-31` S7, 52 S4 | the default |
| `read_withdrawn_parents` | `TOOL-dDeclaredLoop-15` S5, 56 S18 | the default |
| the held-from lookup | `TOOL-dDeclaredLoop-67` S13 | the default, inside `derive_phase_position` |
| `check_transition_tables` | 67 S23 | S1, after `TOOL-dDeclaredLoop-75` |

### The reader

```
read_driver_conf(tree, names):
    conf = tree/.unattended.conf ; absent -> {}
    bash = resolve_bash() ; none -> refuse "driver conf unreadable: <conf> — no bash resolved"
    out  = run [bash, "-c", '. "$1" >/dev/null 2>&1 || exit 9; shift
                for n; do eval "v=\${$n-__UNSET__}"; printf "%s\0%s\0" "$n" "$v"; done
                printf "__CONF_IMPORT_OK__\0\0"', "_", conf, *names], cwd=tree
    rc != 0 or no sentinel -> refuse "driver conf unreadable: <conf> — <rc or missing sentinel>"
    return { n: v for each pair where v != "__UNSET__" }
```

### Files touched (estimate)

- `tools/loop/loop_lib.py`
- `tools/loop/loop_table.py`

### Alternatives rejected

- **Threading `--extra` from every caller.** Three of the callers are Python reached without the driver,
  so each would need its own source of the value, which is the two-readers class over again.
- **An environment variable the driver exports.** A hand run or a gate leg has no driver parent and would
  read the empty set, the refusal this unit removes.
- **govkit's `parse_conf_line`.** It reads one assignment's text, held to bash by a parity table
  (`tools/govkit/selftest.py:850-861`), and cannot see a value the conf computes; the driver sources.

## 5. Production-readiness checklist

- security — sourcing `.unattended.conf` runs project shell, which the driver already does on every
  verb; the subshell writes nothing and its output is read as data.
- perf / scale — one bash per process per tree, memoised.
- error / empty / loading states — S2 refuses by name; a blank `PHASES_EXTRA` reads as no adopter phase.
- observability — S2's refusal names the conf and the reason.
- risks — a conf that prints to stdout is silenced by the redirect; a conf that exits is the missing
  sentinel and refuses, as `check-unattended.sh` treats it.
- testing — AC1 to AC4 as plants; the arm under §7, observed at the close.
- migration — none: the reading is unbuilt at base.
- user docs — none beyond 63 §5's protocol sentence.

## 6. Acceptance criteria

- **AC1** — When `python loop_table.py phase STAGING` runs in a scratch tree whose `.unattended.conf`
  sets `PHASES_EXTRA="STAGING"`, with no `--extra`, it prints `state none · step none · adopter phase`
  and exits 0.
  Red when: the default is the empty tuple, so the phase is refused for lacking a row.
- **AC2** — When `python loop_table.py --fixture --plant phases-extra-default` calls
  `derive_phase_position("STAGING")` and 31 S7's reading over a run in `STAGING`, both read
  `adopter phase` and neither refuses.
  Red when: a caller passes `extra=()` or omits the population.
- **AC3** — When `--plant parent-in-extra-phase` reads a parent whose run record holds `phase: STAGING`
  through `read_withdrawn_parents`, it reports no withdrawn parent and does not refuse.
  Red when: the parent read refuses the adopter phase by name.
  fixture: the parent read reaches `derive_phase_position` once `TOOL-dDeclaredLoop-56` S18 lands at
  order 36; before that it reads `phase: ABORTED` literally, so the main loop observes it at the close.
- **AC4** — When `--plant conf-unreadable` gives a `.unattended.conf` holding `exit 3`, the reading exits
  non-zero printing `driver conf unreadable`, and with no `.unattended.conf` at all `STAGING` is refused
  by name and the core phases still read.
  Red when: a failed source reads as an empty population and passes silently.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)`

This pass keeps the sibling-minted `loop transition tables` leg (`TOOL-dDeclaredLoop-13`) green, which
runs `loop_table.py`; the leg is outside the base manifest the leg line is joined against.

New arm: tools/loop/loop_table.py · covers AC1 AC2 AC3 AC4 · the default-population, parent-in-extra-phase and unreadable-conf plants, staged against TOOL-dDeclaredLoop-63's empty default · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** RESOLVED (agent, 2026-10-24,
  delegated): `**Derived:** PLAY-dClosedLoop-2`, rung 3, as `TOOL-dDeclaredLoop-36` §8 F1 records.
  widens: none · relaxes: none
- **F2 — Thread the value from every caller, or read it in one shared place?** The fix names both. (a)
  every caller passes it leaves the Python callers no source; (b) one reader all callers default to.
  (a) fails AC2 for the callers the driver does not start, and veto 1 discards it. RESOLVED (agent,
  2026-10-24, delegated): (b). widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, promoted from the round-3 spec audit's id 19 (HIGH, item H3).
- rev-2 · 2026-10-24 · §3 · the Edges block gains the bullets mirroring the edges of
  TOOL-dDeclaredLoop-79, written by the round-4 spec audit's disposal; nothing else moved.

## 10. Reuse audit

The seam is the driver's own composition of its conf, sourced as `check-unattended.sh:336-350` imports it,
with the loop kit's `resolve_bash` (`TOOL-dDeclaredLoop-42`); `derive_phase_position` (63) is extended in
place. `python tools/codebase-map/reuse_lookup.py "read the adopter phase vocabulary from the driver conf"`
ranked `read`, `read_text`, `load_conf` and the driver's `phases` (`tools/unattended/unattended.sh`); the
`load_conf` hits read `.memory-tree.conf` through `parse_conf`, and no Python reader sources
`.unattended.conf`, so no existing Python seam fits and S1 is the loop kit's first.

Recall terms used: MEMORY_ROOT PHASES_EXTRA unattended.conf memory-tree.conf sourced subshell sentinel driver conf reader two-readers
