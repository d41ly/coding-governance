# govkit Phase 0 — kit hardening (build report)

*2026-07-14 · DEPL-aKitHardener · node `a` · branch `main`, BASE `c78958c`. Tier 2. Spec:
[../spec/2026-07-14-spec-aKitHardener-1.md](../spec/2026-07-14-spec-aKitHardener-1.md).*

## Method

Understand → build → review, each an adversarial fan-out (Ultracode). A 7-agent read fanned over the
7 Phase-0 surfaces producing a per-item, line-anchored, checkable hardening inventory; the build applied
it directly (coherence-critical: one version convention across files); a 4-dimension adversarial review
closed it (focused on the Python that cannot run on this machine).

## What shipped (14 files)

| Surface | Change |
|---|---|
| memory-tree | `KIT_MEMORY_TREE_VERSION=1.0` in `check-memory-hygiene.sh` (set before conf, unspoofable); `<!-- gov:kit memory-tree@1.0 -->` marker in `HYGIENE.template.md` + retro-stamped into the live `memory/HYGIENE.md` (gov = fleet target #0) |
| memory-tree adopt | `set -eu`; conf **required** (copy-example + exit 1, no silent demo scaffold); refuse-if-present → **converge guard** (marker → exit 0; foreign `memory/` → exit 1 + recovery hint); `cp` idiom rewritten to `if/else` so `set -e` catches a real failure |
| codebase-map | `KIT_CODEBASE_MAP_VERSION="1.0"` in `map_lib.py`; `$generator: codebase-map@1.0` in inventories.json render; `codebase-map@1.0` folded into MAP.md header; marker assertion added to `selftest.py` |
| codebase-map adopt | idempotency guard: `FOUNDATION.md` present → `gen_map.py --write` (reconverge, re-renders the marker) instead of the `--scaffold` refuse wedge |
| agent-cap.js | `KIT_AGENT_CAP_VERSION = '1.0'`; docstring points wiring at `settings-merge.py` |
| tier2-review.js | `version: '1.0'` in `meta` |
| **settings-merge.py** (new) | stdlib idempotent `.claude/settings.json` merge of the agent-cap Workflow hook; `--check` / `--selftest`; `KIT_SETTINGS_MERGE_VERSION="1.0"`; LF write |
| **check-kit-versions.sh** (new) | gate leg: every kit's version constant present + well-formed, and the memory-tree marker == constant |
| run-gates.sh | +2 legs: `kit version markers`, `settings-merge selftest` |
| WIRE-INTO-PROJECT.md | settings.json step calls `settings-merge.py` (JSON demoted to illustrative); non-Python `python <GATE_FILE>` CI-leg fallback documented in §3b step 5 + §6 |
| AGENTS.md | gate-suite list updated with both new legs |

## Decisions (the non-obvious ones)

- **Version = `1.0` two-part `X.Y`** everywhere (matches `KIT_MANIFEST_VERSION="1.1"`); rejected `1.0.0`.
- **One version home per kit** — no per-file duplication (that reintroduces drift). memory-tree is the only
  two-literal case (constant + shipped-doc marker), guarded by `check-kit-versions.sh`.
- **memory-tree no-conf → halt**, not warn (see spec §"Two contested calls"). **codebase-map → skip `set -e`**
  (already fail-fast via `|| exit N`; adding it is reader-contested and grants no required capability — ponytail).
- Per-file `# gov:<kit>@<v> <sha>` fingerprint headers deferred to Phase 1 (they need the lock writer).

## Verification ledger

**Green here (bash / node / grep):**
- `run-gates.sh` bash legs: memory hygiene · kickoff-manifest ratchet · template size · **kit version markers (new)** · agent-instructions wiring · agent-cap self-test (9/9) · agent-instructions self-test — all ok.
- `node --check tools/hooks/agent-cap.js` — parses. tier2-review.js — data-only field, parses.
- `check-kit-versions.sh` standalone → exit 0.
- **memory-tree adopt idempotency (scratch-repo, 4 cases):** no-conf → halt+copy, no scaffold (exit 1) · with conf → scaffold + `@1.0` marker (exit 0) · re-run → "already scaffolded" (exit 0) · foreign `memory/` → refuse (exit 1). All pass.
- EOL: staged blobs LF (`git ls-files --eol` → `i/lf`; `git diff --cached --check` clean; `od -c` shows `bash\n`).

**NOT run here — no Python interpreter on this machine (must be run on a Python host / CI before merge):**
- `python tools/codebase-map/selftest.py` (incl. the new marker assert) — exit 127 locally.
- `python tools/settings-merge.py --selftest` (its 6 in-file cases) — exit 127 locally.
- `codebase-map` adopt two-run idempotency (calls `gen_map.py`).
- These were verified by **static trace + adversarial agent review** instead. `$generator` safety confirmed:
  the artifact is only produced by `render_inventories_json` (gen + gate call the same renderer → byte-compare
  still matches) and never parsed key-strictly; `$comment` already set that precedent.

> **Merge gate:** the two Python self-test legs are wired into `run-gates.sh` and MUST be green on a
> Python host before this lands. On this machine `run-gates.sh` shows them (and one pre-existing
> manifest-check subcase) RED purely as `exit 127 — python not found`, not as logic failures.

## Gate deltas (manifest re-stamp triggers)

`tools/run-gates.sh` (a manifest `watch:` path) changed — +2 legs. `AGENTS.md` gate-suite list updated.
Manifest `last-audit` re-stamped with the delta line for this unit.

## Closing adversarial review

4-dimension fan-out (settings-merge · python-renders · bash-adopt · scope/ponytail), each self-verifying,
focused on the Python that can't run on this node. **No blockers, no majors.** `python-renders` and
`bash-adopt` returned zero findings — independent confirmation of the `$generator` safety and the
`set -eu`/idempotency logic. Four CONFIRMED low-severity findings, all resolved:

1. **[nit] settings-merge `.bak` was the normalized parse, not raw bytes** → backup now `write_bytes(read_bytes())` (byte-faithful).
2. **[minor] check-kit-versions memory-tree regex under-enforced X.Y** — unquoted constant + `grep -F` substring let `1.0.0` pass green (asymmetric with the 4 quoted-literal kits, which reject it). → trailing boundary added to both the presence regex and the marker match; retested: `1.0`/`2.11` accept, `1.0.0`/`1.0.0.0` reject, `@1.0.0` marker rejected.
3. **[nit] settings-merge docstring used `gov:` (Phase-1 fingerprint prefix)** → changed to `gov:kit` for convention consistency.
4. **[minor, judgment] check-kit-versions partly guards a not-yet-consumed contract** — kept (it's the executable acceptance check for this unit's own deliverable; the memory-tree marker/constant equality is gov-source-only and can't fold into the *deployable* hygiene kit) with an explicit intent comment so it doesn't read as speculative scaffolding.

Verdict: Phase 0 is complete and internally consistent. The only open item is the environmental one —
the two Python self-test legs must run green on a Python host before merge (see the merge gate above).

