# TOOL-cKeyedLaunchpad-5 — the anchor selector without a diff, and the latent split it exposes

**Status:** OPEN · rev-3 · 2026-08-13 · node c · Tier-1 · base f006691f · streams tooling+kickoff

## 1. Goal

Make the recurring-bug-class checklist reachable at kickoff, when there is no diff yet but there is a
set of paths. `tools/memory-tree/gotchas.py` already owns the selection; today it is reachable only
through `--for-diff <range>`, so the kickoff engine cannot ask "which classes can the area I am about
to touch hit". This unit adds `--for-paths <path>…` over the same predicate, and closes the two
input-shape defects that predicate has been carrying unexercised.

## 2. Scope (IN)

- S1. Split `do_for_diff` at its diff boundary. Lines 328-343 become
  `do_for_paths(root, conf, paths, label=None)`; `do_for_diff` keeps only the git derivation and its
  empty guard, then delegates. One selection path, no duplicated predicate.
- S2. Normalise caller-supplied paths at the top of `do_for_paths`: backslashes to forward slashes,
  a leading `./` dropped, and an absolute path made relative to `root`. Pure string and `os.path`
  work, no subprocess.
- S3. Add the `--for-paths` verb to `main`, immediately before the fallback usage line, copying
  `--for-diff`'s arity guard and passing `argv[2:]`.
- S4. Refuse a path that is empty, `.`, or `/` — an anchor fragment that short selects the whole
  catalogue, and the checklist degrades to noise with nothing to notice it.
- S5. Update ALL FOUR copies of the verb list, and re-render the two generated artifacts that carry
  one.
- S6. Four `--selftest` arms on the existing `t8` fixture, including one arm per exposed defect.
- S7. **The one-line call site in the kickoff engine.** `SKILL.md` Step 4 invokes `--for-paths` over
  the pointer-map row's entrypoints and reports the selected classes on the READY card. rev-1
  delegated this to U7, which never accepted it; §3 explains why it comes back here.

## 3. Non-goals (OUT)

- No change to `selectable()`'s predicate semantics. The recall bias — substring both ways plus
  basename — is deliberate and documented at `gotchas.py:15-18`. This unit fixes the INPUT shapes
  reaching it, not the matching rule.
- No new gate leg. The gotchas selftest is already a leg and already guarded on `tools/memory-tree/`.
- **The ordering constraint rev-1 gave is answered, not dropped.** rev-1 delegated the call site
  because it must be "sequenced after U2 settles the engine's structure". That is now satisfied by
  ORDER rather than by ownership: S7's edit is one added line in Step 4, it touches none of the
  structure U2 rewrites (Step 2, Step 2b, Scaffolding), and this unit therefore builds AFTER U2
  despite depending on none of its output. The build README's dependency column carries the edge.
- **The call site is IN scope, as S7.** rev-1 put it out and named U7 as the owner; U7 never took it,
  so the verb would have shipped with zero callers, the build's own goal — a checklist reachable at
  kickoff — would have gone unmet, and U6 would have deleted eight manifest bullets in favour of a
  path nothing in the build opens. It is one line in an engine section this unit's own goal names, and
  this is a Tier-1 unit with no dependencies, so it is cheaper here than as a cross-unit hand-off.
- No minimum-length heuristic beyond S4's three refusals. A smarter noise bound is speculative until
  a real pointer-map cell produces bad output.

## 4. Design

### The split

`do_for_diff` is 24 lines of which two are diff-specific: the `git diff --name-only` derivation and
the "touches no file" guard. Everything from the record loop to the final print is already
path-agnostic. The seam is therefore exact, and the delegation direction matters: `do_for_diff` calls
`do_for_paths`, never the reverse. That puts every selection this tool performs — both callers —
through one normalising entry point, which is what makes S2 a root-cause fix rather than a guard
bolted onto the new path.

The header line at `gotchas.py:339` interpolates the range. `do_for_paths` takes an optional `label`
so `do_for_diff` passes the range and keeps its output byte-identical; a direct call renders
`<n> path(s)` instead.

### The two defects this verb exposes

Neither is reachable today, because `git diff --name-only` emits repo-relative POSIX paths and
nothing else. A caller-supplied path can be any shape, so both become live the moment S3 lands.

| Defect | Behaviour | Why it is invisible now |
|---|---|---|
| `os.path.basename` in the basename arm | A backslash path matches on Windows and misses on POSIX. `ntpath.basename` splits it; `posixpath.basename` returns the whole string. | Git never emits a backslash, so the arm has only ever seen POSIX input. |
| The catalogue self-exclusion is a repo-relative prefix test | `p.startswith(f"{m}/gotchas/")` does not match an absolute path, so the catalogue starts selecting itself. | Git never emits an absolute path. |

The second is worse than it reads. `gotchas.py:15-18` records that the catalogue must not appear in
its own checklist; an absolute path defeats that filter silently and the output still looks like a
valid checklist. Normalising to repo-relative POSIX before the loop closes both, and is a no-op for
the git-derived caller.

### Data model

`do_for_paths(root: str, conf: dict, paths: list, label: str | None = None) -> int`. Public, matching
its four `do_*` siblings. That costs a `generated/symbols.json` entry and a re-render — see §7 — and
a leading-underscore name would dodge it. The dodge is rejected in §4's alternatives: naming a verb
handler privately to keep a generated file still is the tail wagging the dog.

### The four copies of the verb list

The grounding found the verb set spelled in four places: the module docstring, `main`'s usage string,
`render()`'s help block, and `tools/memory-tree/README.md:22`. Updating three of them is precisely
`memory/gotchas/two-answers-to-one-question.md`, which is a UNIVERSAL record and therefore appears on
this change's own checklist. All four move together. `render()`'s block is byte-compared into
`INDEX.md` by hygiene check 17, so touching it obliges `gotchas.py --write` in the same commit.

### Files touched (estimate)

| File | Change |
|---|---|
| `tools/memory-tree/gotchas.py` | the split, the normaliser, the verb, the docstring and usage strings, `render()`'s help block, four arms |
| `skills/session-kickoff/SKILL.md` | S7's one-line Step 4 call site |
| `tools/memory-tree/README.md` | line 22, the fourth copy of the verb list |
| `memory/gotchas/INDEX.md` | re-rendered by `gotchas.py --write` |
| `tools/memory-tree/HYGIENE.template.md` | version marker line 1, plus the `--for-diff`-only mention at line 260 |
| `memory/HYGIENE.md` | re-rendered from the template, never hand-edited |
| `tools/memory-tree/check-memory-hygiene.sh` | `KIT_MEMORY_TREE_VERSION` and the `gov:kit` marker at line 13 |
| `memory/map/generated/symbols.json` | re-rendered for the new public symbol |

### Alternatives rejected

- **Normalise inside `selectable()`.** It runs per anchor-path pair rather than once per invocation,
  and it changes `do_check`'s behaviour, which has no input-shape problem.
- **Shell out to git to normalise.** `run()` sets `check=True` and `main` catches only `Problem`, so
  a git failure exits as a traceback out of a gate. The normalisation needs no git.
- **A private `_do_for_paths` to avoid the map re-render.** Rejected above.
- **Leaving `render()`'s help block untouched to keep check 17 green.** This was the grounding pass's
  own recommendation and it contradicts the risk it filed one line earlier. A gate kept green by not
  telling it the truth is the failure mode this build exists to close.

## 5. Production-readiness checklist

- security — reads tracked records and caller paths; writes only under `--write`, which is unchanged.
- perf / scale — one normalising comprehension over the caller's path list; selection is unchanged.
- a11y — N/A, terminal output.
- i18n — N/A.
- error / empty / loading states — S4's three refusals, plus the existing empty-selection print.
- observability — stdout IS the checklist, per the module's own contract at `gotchas.py:11`.
- risks — a path fragment too short to be discriminating still selects broadly; S4 bounds the
  degenerate cases and the printed selection count makes the rest visible.
- testing + left-shift gates — S6, on the existing gotchas selftest leg. Each exposed defect gets its
  own arm, so the fix cannot regress silently.
- migration / rollback — additive; `do_for_diff`'s output is byte-identical via `label`.
- user docs — the four verb-list copies in S5.

## 6. Acceptance criteria

- AC1. When `python tools/memory-tree/gotchas.py --for-paths tools/some-gate.sh` runs against a tree
  whose records anchor there, stdout carries the anchored class and omits an unanchored one.
- AC2. When the same path is spelled with a backslash, stdout is identical to AC1's. This is the arm
  that fails today on POSIX and passes on Windows.
- AC3. When an absolute path under the memory tree's `gotchas/` directory is passed, no class is
  selected from the catalogue itself.
- AC4. When `--for-paths` is given no argument, the command prints its usage and returns 2, matching
  `--for-diff`'s arity contract.
- AC5. When `--for-paths` is given an empty string, `.`, or `/`, it refuses with a message naming the
  offending argument, rather than selecting broadly.
- AC6. `python tools/memory-tree/gotchas.py --for-diff <range>` produces byte-identical output to its
  output at BASE, proving the delegation changed no existing behaviour.
- AC7. `python tools/memory-tree/gotchas.py --selftest` reports every arm held, and the arm count has
  grown by four.
- AC8. `bash tools/run-gates.sh` is green, including the verdict-epoch leg, hygiene check 17, and the
  codebase-map freshness byte-compare.
- AC9. `skills/session-kickoff/SKILL.md` Step 4 invokes `--for-paths`, and the verb has at least one
  caller in the tracked tree. Without this the affordance ships dead.
- AC10. The new verb appears in all four copies of the verb list — the module docstring, `main`'s
  fallback usage string, `render()`'s help block, and the kit README — asserted by one grep across the
  four files. Only the third is gated today, and §4 names updating three of four as the very
  two-answers class this repo records.

## 7. Gates

- `python tools/memory-tree/gotchas.py --selftest` — the existing leg, extended by S6.
- `bash tools/memory-tree/check-verdict-epoch.sh` — **this unit trips it.** `gotchas.py` is in the
  leg's DELEGATES scan set, so the first behaviour-bearing line obliges a `KIT_MEMORY_TREE_VERSION`
  bump. Its remedy is a four-file edit that has nothing to do with this change: the constant, the
  `gov:kit` marker at `check-memory-hygiene.sh:13`, line 1 of `HYGIENE.template.md` and line 1 of
  `memory/HYGIENE.md`, then `bash tools/memory-tree/kit-dogfood-parity.test.sh --render`.
- `python tools/codebase-map/test_codebase_map.py` — **this unit trips it.** A new public symbol reds
  the freshness byte-compare until `python tools/codebase-map/gen_map.py --write`. The leg carries no
  guard, so it fires on this diff.
- `bash tools/memory-tree/check-memory-hygiene.sh` check 17 — reds until `gotchas.py --write`.
- `bash tools/run-gates.sh` — the full bar.
- No new gate leg.

## 8. Open questions

none. The one design fork this unit carried — whether to normalise in `do_for_paths` or in
`selectable()` — is settled in §4 by the caller analysis, and the grounding's contrary recommendation
about `render()` is answered in §4's alternatives.

## 9. Revision log

- rev-1 · 2026-08-13 · initial draft, grounded by workflow `wf_0aaecb50-a51`.
- rev-3 · 2026-08-13 · folded the M4 fix-verify pass. Taking the call site at rev-2 moved SKILL.md
  into this unit's write set and silently discarded rev-1's stated sequencing reason. The reason is
  now answered explicitly — the edit is one line in a section U2 does not touch, and this unit
  builds after U2 — and the README's dependency column carries the edge.
- rev-2 · 2026-08-13 · folded the M4 spec audit, review record 1. H7: rev-1's §3 delegated the only
  call site to a sibling that never accepted it, so the verb would have shipped with zero callers and
  this unit's stated goal would have gone unmet while U6 deleted eight manifest bullets pointing at a
  path nothing opens. Taken back as S7, with AC9. M3: S5 put all four verb-list copies in scope and
  only one was observed — AC10 now binds all four in one grep.

## 10. Reuse audit

The seam is `gotchas.py`'s own `selectable()` predicate and its `records()` loader; this unit extends
the module rather than adding one, and the whole design is a refactor that leaves exactly one
selection path. `reuse_lookup.py "select records by the paths a change touches"` returns no
affordance seam for path selection outside this file, which is the expected answer: the predicate has
one home and this unit keeps it that way.

The `--selftest` arm harness is reused verbatim rather than re-invented — `arm(label, want, fn)` at
`gotchas.py:387-400` compares a SUBSTRING of captured stdout plus an appended `[rc=…]`, so every
absence claim must be written in the `0 if X not in text else 1` form with `want="[rc=0]"`, following
the existing absence arms. The `t8` fixture already writes both `tools/some-gate.sh` and
`deep/nested/some-gate.sh`, so the basename-collision arm needs no new fixture.

Recall terms used: `kickoff manifest ratchet last-audit watch verify-paths SESSION-KICKOFF discovery
order traps accretion size gate prose`.
