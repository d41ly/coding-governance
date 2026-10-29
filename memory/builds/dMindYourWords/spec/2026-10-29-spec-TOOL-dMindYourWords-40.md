# TOOL-dMindYourWords-40 — the lexicon selftest clears the ambient graft and replace variables before any fixture runs

**Status:** OPEN · rev-1 · 2026-10-29 · node d · Tier-2 · base ccd1292e · streams tooling · order 9

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-29-build-TOOL-dMindYourWords-1-agent-ledger.md](../build/2026-10-29-build-TOOL-dMindYourWords-1-agent-ledger.md) | journal | TOOL-dMindYourWords-1 TOOL-dMindYourWords-2 TOOL-dMindYourWords-3 TOOL-dMindYourWords-4 TOOL-dMindYourWords-5 TOOL-dMindYourWords-6 TOOL-dMindYourWords-7 TOOL-dMindYourWords-8 TOOL-dMindYourWords-9 TOOL-dMindYourWords-10 TOOL-dMindYourWords-11 TOOL-dMindYourWords-12 TOOL-dMindYourWords-13 TOOL-dMindYourWords-14 TOOL-dMindYourWords-15 TOOL-dMindYourWords-16 TOOL-dMindYourWords-17 TOOL-dMindYourWords-22 TOOL-dMindYourWords-23 TOOL-dMindYourWords-24 TOOL-dMindYourWords-25 TOOL-dMindYourWords-26 TOOL-dMindYourWords-27 TOOL-dMindYourWords-28 TOOL-dMindYourWords-29 TOOL-dMindYourWords-30 TOOL-dMindYourWords-31 TOOL-dMindYourWords-32 TOOL-dMindYourWords-33 TOOL-dMindYourWords-34 TOOL-dMindYourWords-35 TOOL-dMindYourWords-36 TOOL-dMindYourWords-37 TOOL-dMindYourWords-38 TOOL-dMindYourWords-39 TOOL-dMindYourWords-41 TOOL-dMindYourWords-42 TOOL-dMindYourWords-43 TOOL-dMindYourWords-44 TOOL-dMindYourWords-45 TOOL-dMindYourWords-46 TOOL-dMindYourWords-47 TOOL-dMindYourWords-48 TOOL-dMindYourWords-49 TOOL-dMindYourWords-50 TOOL-dMindYourWords-51 TOOL-dMindYourWords-52 |
| [2026-10-29-prompt-TOOL-dMindYourWords-38-promoted-fix-brief.md](../prompts/2026-10-29-prompt-TOOL-dMindYourWords-38-promoted-fix-brief.md) | research | TOOL-dMindYourWords-38 TOOL-dMindYourWords-48 TOOL-dMindYourWords-51 TOOL-dMindYourWords-52 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 6 of `reviews/2026-10-29-review-TOOL-dMindYourWords-30-to-37-spec-audit-round1.md`,
HIGH, which shares item H4 with id 15 (TOOL-dMindYourWords-41). The graft arms of
TOOL-dMindYourWords-30, -31 and -32 name "the pin cut out of the code" as their failing case, but
`tools/unattended/unattended.sh:86` exports `GIT_GRAFT_FILE=/dev/null` to the bar `--close` runs, and
`tools/lexicon/selftest.py` hands its whole environment to every child. On this build's own close the
graft-file arms therefore cannot go red: the environment pins what the code was meant to. This unit
makes the selftest drop every variable that neutralises a graft or a replace ref before any fixture
runs, so the only pin in force under an arm is the one the kit's code supplies.

## 2. Scope (IN)

- **S1** — The clear. At the top of `tools/lexicon/selftest.py`, beside the identity update at `:44` and
  before any fixture or kit child is spawned, the selftest pops `GIT_GRAFT_FILE`,
  `GIT_NO_REPLACE_OBJECTS` and `GIT_REPLACE_REF_BASE` out of its own `os.environ` at run time, so every
  child, the kit run by `run_case` (`:354`) included, inherits none of them; no name, key or reader
  changes. A comment beside it names `tools/unattended/unattended.sh:86` and
  `unattended.test.sh:3125-3131` as the reason. Observed by AC1 and AC2.

## 3. Non-goals (OUT)

- Proving that a staged graft is in force before an arm judges it: TOOL-dMindYourWords-41 (id 15),
  which reads the environment this unit clears.
- The driver's export itself: `unattended.sh:86` is deliberate hardening of the driver's own reads and
  stays.
- Any other suite: the report names the lexicon selftest's graft arms, and the unattended suite already
  clears the variable at its one graft control (`unattended.test.sh:3125-3131`).
- The selftest-harness rule and checklist entry the report names as H4's left-shift gate: a checklist
  is its own artifact (BUILD-METHOD M2).
- Kit version constants: minted at landing (`tools/push-main.sh:26-31`), so this unit moves none.

### Edges

- **consumes-from** `TOOL-dMindYourWords-30` — the provenance graft arm whose graft-file failing case this clear makes reachable
- **consumes-from** `TOOL-dMindYourWords-32` — the added-set graft arm whose graft-file failing case this clear makes reachable
- **hands-off** `TOOL-dMindYourWords-41` — the cleared environment, under which that unit's control proves a staged graft is in force

## 4. Design

### Evidence

- `tools/unattended/unattended.sh:86` runs `export GIT_GRAFT_FILE=/dev/null`, and
  `tools/unattended/unattended.test.sh:3125-3131` records that this export reached a graft arm under
  `--close` and changed its outcome, needing `env -u GIT_GRAFT_FILE`.
- `tools/lexicon/selftest.py` touches the environment only at `:44` (identity and `core.autocrlf`) and
  at `:5990` (one child's `PYTHONIOENCODING`); `run_case` spawns the kit with the inherited environment
  (`:354-355`).
- Measured on git 2.54.0 in a fixture under `%TEMP%`: after `git replace --graft <c2>`, `git rev-list
  --parents -n 1 <c2>` printed one word; with `GIT_REPLACE_REF_BASE=refs/nothing/` exported it printed
  two, as `--no-replace-objects` did. So that variable neutralises a replace-ref arm the way
  `GIT_GRAFT_FILE` neutralises a graft-file arm. PINNED 2026-10-29.

### The clear

```
# beside :44, before the first spawn
for name in ("GIT_GRAFT_FILE", "GIT_NO_REPLACE_OBJECTS", "GIT_REPLACE_REF_BASE"):
    os.environ.pop(name, None)
```

### Inventory

Minted: none.

### Rollout

Live at landing, one order after TOOL-dMindYourWords-30 and -32, whose arms it serves; the drift-blame
arm TOOL-dMindYourWords-31 adds later runs under the same clear by construction.

### Files touched (estimate)

- `tools/lexicon/selftest.py`: S1

### Alternatives rejected

- **`env -u` per graft arm**, the unattended suite's form: each new graft arm must remember it, and the
  arm that forgets is the one this finding describes.
- **Clearing the variables in the kit's `build_git_env`**: the kit sets `GIT_GRAFT_FILE` there on
  purpose; what must not leak is the CALLER's pin into a fixture that tests the kit's.

## 5. Production-readiness checklist

- security — N/A — a test-harness environment; no product surface.
- perf / scale — none.
- error / empty / loading states — an unset variable is popped as a no-op.
- observability — the comment names why the clear exists.
- risks — an arm that relied on an ambient pin now runs unpinned; no arm at base does, since no arm
  sets or reads any of the three.
- testing — AC1, AC2 and the arm of §7.
- migration — none.
- user docs — N/A — selftest internals.

## 6. Acceptance criteria

- **AC1** — When `GIT_GRAFT_FILE=/dev/null GIT_NO_REPLACE_OBJECTS=1 GIT_REPLACE_REF_BASE=refs/x/ python -c
  "import os; p = 'tools/lexicon/selftest.py'; src = open(p, encoding='utf-8').read();
  exec(src[:src.index('# ---- P1')], {'__file__': p, '__name__': 'probe'});
  print([k for k in ('GIT_GRAFT_FILE', 'GIT_NO_REPLACE_OBJECTS', 'GIT_REPLACE_REF_BASE') if k in
  os.environ])"` runs, executing the selftest's prologue up to its first arm, it prints `[]`.
  Red when: any of the three survives the prologue and reaches a fixture child.
  fixture: the prologue alone, which defines `run_case` and spawns no fixture repository (measured
  2026-10-29: the prologue executes in this form from the repository root).
- **AC2** — When `grep -n -m1 'subprocess.run(' tools/lexicon/selftest.py` and `grep -n -m1
  'GIT_REPLACE_REF_BASE' tools/lexicon/selftest.py` run after the pass, the second's line number is
  below the first's, which is `76` at base.
  Red when: the clear sits after a spawn that already inherited the pin.

## 7. Gates

`lexicon selftest` · `codebase-map kit selftest`

New arm: tools/lexicon/selftest.py · covers AC1 · the clear itself, observed at the close by exporting `GIT_GRAFT_FILE=/dev/null` in the calling shell with the pin cut from the provenance blame, under which the graft-file arm of TOOL-dMindYourWords-30 must red · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-29 · initial draft, promoted from review id 6 (HIGH, item H4, shared with id 15) of the
  round-1 audit of units 30 to 37, with the replace-ref base variable measured.

## 10. Reuse audit

The seam is the selftest's own module-level environment set at `tools/lexicon/selftest.py:44`, extended
by three removals, and the reason is the control the unattended suite already wrote
(`tools/unattended/unattended.test.sh:3125-3131`). `python tools/codebase-map/reuse_lookup.py "clear an
inherited git variable before a fixture child runs"` ranked generic readers and no shared fixture
environment for the lexicon kit, which imports no sibling, so no existing seam fits beyond the line this
unit extends.

Recall terms used: `python tools/memory-recall/query.py "how does a kit hold every git history read to the replace and graft pin as a class rather than a list" --terms "graft replace no-replace-objects pinned reader run_git build_git_env inventory spawn class history"`
