# TOOL-dSafePassage-23 — the resolver keeps an override's own name, and prefers the direct executable only for the launcher names

**Status:** DEFERRED · rev-2 · 2026-10-23 · node d · Tier-2 · base 3708a705 · streams tooling · order 4 · advances TOOL-dSafePassage-14

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dSafePassage-23-deviation-69.md](../build/2026-10-23-build-TOOL-dSafePassage-23-deviation-69.md) | deviation | — |
| [2026-10-25-build-TOOL-dSafePassage-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dSafePassage-1-agent-ledger.md) | journal | TOOL-dSafePassage-1 TOOL-dSafePassage-2 TOOL-dSafePassage-3 TOOL-dSafePassage-4 TOOL-dSafePassage-5 TOOL-dSafePassage-6 TOOL-dSafePassage-7 TOOL-dSafePassage-8 TOOL-dSafePassage-9 TOOL-dSafePassage-10 TOOL-dSafePassage-11 TOOL-dSafePassage-12 TOOL-dSafePassage-13 TOOL-dSafePassage-15 TOOL-dSafePassage-16 TOOL-dSafePassage-17 TOOL-dSafePassage-18 TOOL-dSafePassage-19 TOOL-dSafePassage-20 TOOL-dSafePassage-21 TOOL-dSafePassage-22 TOOL-dSafePassage-24 TOOL-dSafePassage-25 TOOL-dSafePassage-26 TOOL-dSafePassage-27 TOOL-dSafePassage-28 TOOL-dSafePassage-29 TOOL-dSafePassage-30 TOOL-dSafePassage-31 TOOL-dSafePassage-32 TOOL-dSafePassage-33 TOOL-dSafePassage-34 TOOL-dSafePassage-35 TOOL-dSafePassage-36 TOOL-dSafePassage-37 TOOL-dSafePassage-38 TOOL-dSafePassage-39 TOOL-dSafePassage-40 TOOL-dSafePassage-41 TOOL-dSafePassage-42 TOOL-dSafePassage-43 TOOL-dSafePassage-44 TOOL-dSafePassage-45 TOOL-dSafePassage-46 TOOL-dSafePassage-47 TOOL-dSafePassage-48 TOOL-dSafePassage-49 TOOL-dSafePassage-50 TOOL-dSafePassage-51 TOOL-dSafePassage-52 TOOL-dSafePassage-53 TOOL-dSafePassage-54 TOOL-dSafePassage-55 TOOL-dSafePassage-56 TOOL-dSafePassage-57 TOOL-dSafePassage-58 TOOL-dSafePassage-59 |
| [2026-10-23-review-TOOL-dSafePassage-15-16-17-18-19-20-21-22-23-24-25-26-spec-audit-round1.md](../reviews/2026-10-23-review-TOOL-dSafePassage-15-16-17-18-19-20-21-22-23-24-25-26-spec-audit-round1.md) | spec-audit | TOOL-dSafePassage-16 TOOL-dSafePassage-20 TOOL-dSafePassage-15 TOOL-dSafePassage-18 TOOL-dSafePassage-19 TOOL-dSafePassage-22 TOOL-dSafePassage-24 TOOL-dSafePassage-17 TOOL-dSafePassage-25 TOOL-dSafePassage-21 TOOL-dSafePassage-26 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of this build
(`memory/builds/dSafePassage/reviews/2026-10-23-review-TOOL-dSafePassage-1-2-3-4-5-6-7-8-9-10-11-12-13-spec-audit-round1.md`)
confirmed finding **id 35** at HIGH, its item **D-7**. TOOL-dSafePassage-11 S3 has every accepted
candidate echo the `sys.executable` its probe printed. Two suites hand the resolver a command that
must itself be spawned: `tools/check-install-prefix.test.sh:238-247` sets `GOV_PYTHON` to a wrapper
that kills only the ban's counter, and `skills/session-kickoff/manifest-check.test.sh:1144-1153` sets
`GOV_PYTHON=python` with a PATH shim named `python` that counts spawns. Echoing the executable skips
both, so the dead-counter arm and K2 AC1 go red, and an operator's own `GOV_PYTHON` wrapper is
skipped without a word. This unit is id 35's promotion, the report's first branch: a candidate taken
from the caller's override or from `GOV_PYTHON` echoes itself, and only the built-in launcher names
are replaced by the executable they start.

## 2. Scope (IN)

- **S1** — Where the name comes from decides what is echoed. In the canonical block of
  `tools/lib/resolve-python.sh`, an accepted candidate echoes the executable its probe printed only
  when it came from the block's own list, `python3`, `python` and `py`, and that path is a file. A
  candidate that came from the caller's first argument or from `GOV_PYTHON` echoes itself, unchanged,
  whatever it is named, `GOV_PYTHON=python` included. Observed by AC1, AC2 and AC3.
- **S2** — The floor binds every candidate alike. The probe of TOOL-dSafePassage-11 S2 still runs
  each candidate once with `-I -c`, and a candidate below the floor is passed over wherever its name
  came from. Observed by AC4.
- **S3** — What `GOV_PYTHON` means, stated. The block's comment and `help/python-floor.md` say that
  `GOV_PYTHON` names the command a consumer spawns, a wrapper or a venv launcher included, and that
  the resolver prefers the direct executable only for the three launcher names. Observed by AC5.
- **S4** — The copies. Every inline copy of the block is re-synced byte-identically, the population
  `git grep -l '^# >>> resolve_python' -- '*.sh' '*.py' '.githooks/*' WIRE-INTO-PROJECT.md` names
  less the canonical, as TOOL-dSafePassage-11 S5 re-syncs it. Observed by AC6.

## 3. Non-goals (OUT)

- The refusal's text and the order of its lines: id 36, `TOOL-dSafePassage-26`.
- The alias test the block uses for an executable: id 21, `TOOL-dSafePassage-26`.
- Editing either suite's arms. Under S1 both keep passing as written; the close runs them.

### Edges

- **consumes-from** `TOOL-dSafePassage-11` — the canonical block with its floor probe and its executable preference, the inline parity population and `help/python-floor.md`; without them there is no preference to narrow
- **hands-off** `TOOL-dSafePassage-26` — the refusal's kept lines and their order, and the alias test for a printed executable, the two other findings on this block
- **hands-off** `TOOL-dSafePassage-35` — the minors batch of the round-1 audit of units 15 to 26, which reads the parity criterion through the comparison that sees an echo-rule drift

## 4. Design

### Data model

| Candidate came from | Probe at the floor | Echoed |
|---|---|---|
| the caller's override, `$1` | yes | the override, as given |
| `GOV_PYTHON` | yes | `$GOV_PYTHON`, as given |
| `python3`, `python` or `py` | yes, and its printed executable is a file | that executable, forward-slashed |
| `python3`, `python` or `py` | yes, and its printed executable is no file | the launcher name |
| any | below the floor, or does not run | nothing; the next candidate |

### Inventory

Minted: none. The block gains one test of where the candidate came from; no function, conf key,
gate leg or policy key.

### Migration

None for adopters beyond the re-synced copies, whose kit versions the lander mints at the landing
(`tools/push-main.sh:902`).

### Rollout

Live at landing. It builds at order 4, after TOOL-dSafePassage-11 (order 3).

### Files touched (estimate)

- `tools/lib/resolve-python.sh`
- `tools/lib/resolve-python.test.sh`
- `help/python-floor.md`

The inline copies of S4, derived by the `git grep` that S4 names, are re-synced in the same commit
and added to this unit's `--dispatch --writes`.

### Alternatives rejected

- **Keep echoing the executable and rewrite both suites' arms**, the report's second branch. It
  changes what `GOV_PYTHON` means for every operator whose override is a wrapper, a public surface
  M3's veto 2 keeps from a run.
- **Prefer the executable only when the name is a bare launcher name, wherever it came from.** It
  still skips `manifest-check.test.sh`'s shim, which is set as `GOV_PYTHON=python`.

## 5. Production-readiness checklist

- security: an override is spawned as the operator named it, which is what they chose; nothing
  widens.
- perf / scale: an override that is itself an alias keeps its spawn cost, the operator's choice; the
  launcher names keep TOOL-dSafePassage-11's saving.
- error / empty / loading states: unchanged; an override below the floor or not running is refused
  as TOOL-dSafePassage-11 states.
- observability: unchanged.
- risks: none beyond TOOL-dSafePassage-11's, whose copy parity arm reds a copy left behind.
- testing: the resolver arms of §7 over fake launchers.
- migration: the copies, S4.
- user docs: `help/python-floor.md`, S3.

## 6. Acceptance criteria

A fake launcher is TOOL-dSafePassage-11's: a two-line bash script under the run's scratch directory
printing `<version> <path>` for any `-c` and exiting 0.

- **AC1** — When `GOV_PYTHON=<wrapper> bash -c '. "$1"; resolve_python' _ tools/lib/resolve-python.sh`
  runs with `<wrapper>` a fake printing `3.15 <a real file's path>`, it prints `<wrapper>` and not
  that path.
  Red when: the override is replaced by the executable its probe printed.
- **AC2** — When `PATH="<shim dir>:$PATH" GOV_PYTHON=python bash -c '. "$1"; resolve_python' _ tools/lib/resolve-python.sh`
  runs with a fake named `python` in `<shim dir>`, it prints `python`.
  Red when: a `GOV_PYTHON` spelled as a launcher name is replaced by an executable.
- **AC3** — When `PATH="<fakes>:$PATH" bash -c '. "$1"; resolve_python' _ tools/lib/resolve-python.sh`
  runs with `GOV_PYTHON` unset and a fake `python3` printing `3.15 <a real file's path>` first on
  `PATH`, it prints that path forward-slashed; and `bash -c '. "$1"; resolve_python "$2"' _ tools/lib/resolve-python.sh <wrapper>`
  prints `<wrapper>`.
  Red when: the launcher names lose the executable preference, or the caller's override is replaced.
- **AC4** — When AC1's command runs with `<wrapper>` printing `3.14 <path>` and every launcher name a
  fake printing `3.14`, it exits non-zero naming `<wrapper>` with `3.14, below the floor 3.15`.
  Red when: an override skips the floor probe.
- **AC5** — When `git grep -n -e "GOV_PYTHON" -- help/python-floor.md` runs, it prints the sentence
  saying an override is spawned as named.
  Red when: the page is silent on what `GOV_PYTHON` names.
- **AC6** — When `python tools/lib/python_floor.py check` runs after the pass, it prints no copy
  finding.
  Red when: an inline copy differs from the canonical block.

## 7. Gates

`python resolver (behaviour + inline parity + idiom ban)` · `install-prefix self-test` · `manifest-check self-test` · `unattended-build self-test` · `push-main self-test` · `pre-push self-test` · `memory-hygiene self-test` · `check-wiring self-test` · `lexicon selftest` · `spec tokens (a spec's own names resolve)` · `memory hygiene`

New arm: tools/lib/resolve-python.test.sh · covers AC1 AC2 AC3 AC4 · fake launchers and a wrapper override, its failing case staged by a block copy that echoes the printed executable for every candidate · none

`install-prefix self-test` and `manifest-check self-test` are the two suites id 35 found red; the
close runs them and observes them green over this unit's block.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft, the promotion of the round-1 spec audit's id 35 (HIGH, item
  D-7).
- rev-2 · 2026-10-23 · §3 · the Edges gain the ends this unit owes the promotions of the round-1 audit of units 15 to 26, written by the disposal stage: `TOOL-dSafePassage-35`; no other section moved.

## 10. Reuse audit

The seam extended is the canonical resolver block (`tools/lib/resolve-python.sh:24-54` at the base)
as TOOL-dSafePassage-11 S2 and S3 change it, and its inline parity population, whose rows gate every
copy. `python tools/codebase-map/reuse_lookup.py "keep a python override launcher name instead of its
resolved executable"` ranked `resolve`, `resolve_kit_dir`, `resolve_python` (70 installs) and
`resolve_prefix_token`; `resolve_python` is the seam, and the hit agrees with source. The two suites
this unit keeps green were read at `tools/check-install-prefix.test.sh:238-247` and
`skills/session-kickoff/manifest-check.test.sh:1144-1153`.

Recall terms used: `python tools/memory-recall/query.py "how were spec audit findings promoted into repair units placed beside the unit they repair" --terms "spec audit promoted unit repair blocker high minors batch disposal order edges rescope"`
