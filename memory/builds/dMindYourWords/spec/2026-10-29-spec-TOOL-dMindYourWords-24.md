# TOOL-dMindYourWords-24 — the lexicon finds its sibling kits through `resolve_kit_dir`, never a `parent.parent` probe

**Status:** OPEN · rev-2 · 2026-10-29 · node d · Tier-2 · base ccd1292e · streams tooling · order 2

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-29-build-TOOL-dMindYourWords-1-agent-ledger.md](../build/2026-10-29-build-TOOL-dMindYourWords-1-agent-ledger.md) | journal | TOOL-dMindYourWords-1 TOOL-dMindYourWords-2 TOOL-dMindYourWords-3 TOOL-dMindYourWords-4 TOOL-dMindYourWords-5 TOOL-dMindYourWords-6 TOOL-dMindYourWords-7 TOOL-dMindYourWords-8 TOOL-dMindYourWords-9 TOOL-dMindYourWords-10 TOOL-dMindYourWords-11 TOOL-dMindYourWords-12 TOOL-dMindYourWords-13 TOOL-dMindYourWords-14 TOOL-dMindYourWords-15 TOOL-dMindYourWords-16 TOOL-dMindYourWords-17 TOOL-dMindYourWords-22 TOOL-dMindYourWords-23 TOOL-dMindYourWords-25 TOOL-dMindYourWords-26 TOOL-dMindYourWords-27 TOOL-dMindYourWords-28 TOOL-dMindYourWords-29 TOOL-dMindYourWords-30 TOOL-dMindYourWords-31 TOOL-dMindYourWords-32 TOOL-dMindYourWords-33 TOOL-dMindYourWords-34 TOOL-dMindYourWords-35 TOOL-dMindYourWords-36 TOOL-dMindYourWords-37 |
| [2026-10-29-prompt-TOOL-dMindYourWords-22-promoted-fix-brief.md](../prompts/2026-10-29-prompt-TOOL-dMindYourWords-22-promoted-fix-brief.md) | research | TOOL-dMindYourWords-22 TOOL-dMindYourWords-27 TOOL-dMindYourWords-29 |
| [2026-10-29-review-TOOL-dMindYourWords-22-to-29-spec-audit-round1.md](../reviews/2026-10-29-review-TOOL-dMindYourWords-22-to-29-spec-audit-round1.md) | spec-audit | TOOL-dMindYourWords-27 TOOL-dMindYourWords-26 TOOL-dMindYourWords-28 TOOL-dMindYourWords-22 TOOL-dMindYourWords-23 TOOL-dMindYourWords-25 TOOL-dMindYourWords-29 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 23 of `reviews/2026-10-29-review-TOOL-dMindYourWords-1-spec-audit-round1.md`, HIGH, item
H2. TOOL-dMindYourWords-1's `read_policy_value` finds the policy kit at
`Path(__file__).resolve().parent.parent / "policy" / "policy.py"` and reads `POLICY_DEFAULTS` when
nothing is there. An adopter whose policy kit is homed anywhere else, which only the install receipt
records, silently grades under the defaults while its committed `.governance/policy.toml` says
otherwise. TOOL-dMindYourWords-3 copies the probe for `annotations.py`. This unit locates the policy kit
through the canonical locator, and hands the same locator to unit 3.

## 2. Scope (IN)

- **S1** — The locator in the engine. `tools/lexicon/lexicon.py` carries one inline copy of the
  canonical `resolve_kit_dir` block (`tools/lib/resolve_kit_dir.py`, between its `# >>> resolve_kit_dir`
  and `# <<< resolve_kit_dir` markers), byte-identical. Where the build run's base already carries the
  copy PLAY-dOrderedCharter-10 S7 inlines for the registry read, that copy is the one, and no second is
  written. The existing `resolve_kit_dir` row of `PARITY_ROWS` grades it: its population is every
  tracked `*.py` carrying the opening marker (`tools/lib/resolve-python.test.sh:172`, `:226`), so the
  copy needs no new row. Observed by AC3.
- **S2** — The policy read through it. `read_policy_value` computes the kit directory as
  `resolve_kit_dir("policy", "policy.py", KIT_DIR)`, `KIT_DIR` being this file's directory taken
  logically (`Path(__file__).absolute().parent`, never `resolve()`). A `LookupError` is the absent-kit
  branch, unchanged: `POLICY_DEFAULTS` with its one notice line, which now names the three places looked,
  the receipt and both probes. Observed by AC1 and AC2.
- **S3** — The docs. The policy-read paragraph of `tools/lexicon/README.md` names the receipt as how a
  renamed policy kit is found; `KIT_LEXICON_VERSION` moves once. NOT OBSERVED as behaviour: prose has no
  grader beyond the carriers' own legs.

## 3. Non-goals (OUT)

- The `annotations.py` locator: TOOL-dMindYourWords-3 builds it after this unit and takes the locator
  through the edge below, `resolve_kit_dir("memory-tree", "annotations.py", KIT_DIR)`.
- The idiom-ban arm the report names as H2's left-shift gate, refusing a `parent.parent / "<kit>"`
  sibling probe across `tools/**/*.py`: a gate is its own unit (BUILD-METHOD M2), and no clause of this
  build names it.
- What `read_policy_value` does with the subprocess's exit codes, and which keys `POLICY_DEFAULTS`
  holds: review ids 14, 15, 46 and 4, the minors batch TOOL-dMindYourWords-29.

### Edges

- **consumes-from** `TOOL-dMindYourWords-1` — `read_policy_value` and its absent-kit branch; without it there is no read to relocate
- **hands-off** `TOOL-dMindYourWords-3` — the inline `resolve_kit_dir` in `tools/lexicon/lexicon.py`, through which S4's `check_contract_pointers` finds `annotations.py` instead of the `<kit>/../memory-tree/` probe
- **hands-off** `TOOL-dMindYourWords-29` — `read_policy_value` located through the receipt, beside which the batch seeds every `POLICY_DEFAULTS` row and maps the subprocess's other exits (ids 4, 14, 15, 46)
- **hands-off** `TOOL-dMindYourWords-37` — the policy locator its arm exercises and AC3's count, which the minors batch guards in the leg and observes with a bare count (review ids 16 and 39)

## 4. Design

### Evidence

- `resolve_kit_dir(home, anchor, here)` reads the `.governance/install.json` receipt first, "the only
  record of a RENAMED kit dir", then probes `<here>/<home>/<anchor>` and `<here>/../<home>/<anchor>`, and
  raises `LookupError` naming all three; it takes `here` with `.absolute()`, never `resolve()`
  (`tools/lib/resolve_kit_dir.py`, the canonical block). With `here` the lexicon kit directory, the
  second probe is today's sibling layout, so the default install reads exactly as before.
- The lexicon kit already carries a shell-wrapped copy of the block (`tools/lexicon/adopt-lexicon.sh:66-103`),
  which uses it for `codebase-map` (`:407`); the engine carries none at HEAD (`git grep -n resolve_kit_dir
  -- tools/lexicon` lists only `adopt-lexicon.sh`).
- PLAY-dOrderedCharter-10 S7, an ancestor's unit built before this build run, has `lexicon.py --tags`
  read the namespace registry "through `resolve_kit_dir("playbook", "namespaces.toml", here)`"
  (`memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-10.md:69`), with
  `tools/lexicon/lexicon.py` in its Files touched.
- The parity row's population grep reads `*.sh`, `*.py`, `.githooks/*` and `WIRE-INTO-PROJECT.md` for
  the marker, every block in a file graded (`tools/lib/resolve-python.test.sh:224-241`). The report's fix
  asked for a new row; the existing row already covers a new copy, so none is added.
- The block imports `json` and `pathlib` inside the function, both stdlib, so
  `check_self_containment` (`tools/lexicon/lexicon.py:2359`) judges nothing new.

### Inventory

Minted: none. `resolve_kit_dir` is the canonical block's name; `KIT_DIR`, if the engine lacks one, is a
module constant in cell `py.constant`, screaming.

### Migration

None. The default layout resolves by the second probe as before; a renamed kit now resolves by the
receipt where it used to read defaults.

### Rollout

Live at landing, one order after TOOL-dMindYourWords-1, before any later unit reads its key through
`read_policy_value`.

### Files touched (estimate)

- `tools/lexicon/lexicon.py`: S1, S2, `KIT_LEXICON_VERSION`
- `tools/lexicon/selftest.py`: the arm of §7
- `tools/lexicon/README.md`: S3

### Alternatives rejected

- **A second probe rung in `read_policy_value`**, trying a few likely homes: it guesses where the receipt
  knows, which is the defect.
- **Importing `tools/lib/resolve_kit_dir.py`**: `<prefix>/lib/` is gov-internal and ships nothing, and
  the kit may import no sibling (`check_self_containment`), so the inline copy under parity is the
  route every copy-installed consumer takes.

## 5. Production-readiness checklist

- security — the receipt row is followed only when its path exists inside the tree and holds no `..`
  part (the canonical block's own rule); a probe never escapes the repository.
- perf / scale — one JSON read of the receipt per policy read, once per run.
- error / empty / loading states — no receipt and no sibling: `LookupError`, the absent-kit branch with
  its notice; an unreadable receipt reads as no rows (the block's own rule).
- observability — the notice names the three places looked.
- risks — none beyond the block's own, which its parity row and behaviour section grade.
- testing — AC1 to AC3 and the arm of §7.
- migration — none.
- user docs — `tools/lexicon/README.md` (S3).

## 6. Acceptance criteria

- **AC1** — When `python <prefix>/lexicon/lexicon.py` runs in a fixture adopter whose policy kit sits in
  a renamed directory recorded by an `install.json` receipt row, and whose committed
  `.governance/policy.toml` sets `lexicon.pin = "no-gate"`, a branch adding an unledgered offender exits
  0 and prints the `undeclared site` finding.
  Red when: the read misses the renamed kit and grades under the default `shrink-only`, exiting 1.
  fixture: a scratch adopter under `%TEMP%` with the lexicon kit copied and the policy kit homed at
  `scripts/pol/`.
- **AC2** — When the same fixture has no receipt row and no sibling policy directory, the run reads
  `shrink-only` and its notice names the receipt and both probe paths.
  Red when: a missing kit reds, or the notice omits where it looked.
- **AC3** — When `git grep -c '^# >>> resolve_kit_dir' -- tools/lexicon/lexicon.py` runs, it prints 1,
  and `git grep -n 'parent.parent / "policy"' -- tools/lexicon/` prints nothing.
  Red when: a second copy lands beside an ancestor's, or the hand-written probe survives.

## 7. Gates

`lexicon naming predicates` · `lexicon selftest` · `codebase-map kit selftest` · `python resolver (behaviour + inline parity + idiom ban)` · `kit version markers`

New arm: tools/lexicon/selftest.py · covers AC1 AC2 · a fixture adopter with a receipt homing the policy kit at `scripts/pol/` and a committed `no-gate`, its failing case the locator swapped back to the `parent.parent` probe, under which AC1's run exits 1 · none

## 8. Open questions

- **F1 — Does the engine carry its own copy of the block, or reuse one?** Options: (a) reuse the copy
  PLAY-dOrderedCharter-10 S7 inlines where the base carries it, else inline one; (b) always inline a
  second copy for the policy read. (b) puts two parity-graded copies of one block in one file, which the
  report's L10 calls duplicated upkeep. RESOLVED (agent, 2026-10-29, delegated): (a), rung 3, one copy
  per file under the existing row. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-29 · initial draft, promoted from review id 23 (HIGH, item H2) of the round-1 spec
  audit.
- rev-2 · 2026-10-29 · §3 · the Edges gain the mirror of each edge the promoted units of the round-1 audit of units 22 to 29
  declare toward this unit (TOOL-dMindYourWords-37); no scope, design or criterion moved.

## 10. Reuse audit

The seam is `resolve_kit_dir` (`tools/lib/resolve_kit_dir.py`), carried inline under the `resolve_kit_dir`
row of `PARITY_ROWS`. `python tools/codebase-map/reuse_lookup.py "locate a sibling kit directory through
the install receipt"` ranked it first, a SEAM with fan-in 16 and 75 installs, among them
`tools/lexicon/adopt-lexicon.sh`; the next candidates, `kit_rel` and `kit_dir`
(`tools/codebase-map/map_lib.py`), resolve a kit's own directory, not a sibling's. The record and the
source agree: the report's H2 cites `adopt-lexicon.sh:66-103`, which holds the copy at HEAD.

Recall terms used: `python tools/memory-recall/query.py "how does a copy-installed kit find a renamed sibling kit through the install receipt" --terms "resolve_kit_dir receipt install.json sibling kit probe parity PARITY_ROWS inline copy policy.py"`
