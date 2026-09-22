# TOOL-dRetiredFork-21 — the two hooks whose path comes from a fragment, not from the default

**Status:** CLOSED · rev-2 · 2026-09-03 · node d · Tier-2 · base b0108f13 · streams tooling · order 4 · ratified 2026-09-02

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-03-build-TOOL-dRetiredFork-21-1-acceptance-ledger.md](../build/2026-09-03-build-TOOL-dRetiredFork-21-1-acceptance-ledger.md) | journal | — |
| [2026-09-03-prompt-TOOL-dRetiredFork-21-1-build-brief.md](../prompts/2026-09-03-prompt-TOOL-dRetiredFork-21-1-build-brief.md) | journal | — |
| [2026-09-02-review-TOOL-dRetiredFork-3-21-and-depl-1-9-spec-audit-round3.md](../reviews/2026-09-02-review-TOOL-dRetiredFork-3-21-and-depl-1-9-spec-audit-round3.md) | spec-audit | DEPL-dRetiredFork-1 DEPL-dRetiredFork-2 DEPL-dRetiredFork-3 DEPL-dRetiredFork-6 DEPL-dRetiredFork-7 DEPL-dRetiredFork-8 DEPL-dRetiredFork-9 TOOL-dRetiredFork-3 TOOL-dRetiredFork-5 TOOL-dRetiredFork-8 TOOL-dRetiredFork-9 TOOL-dRetiredFork-11 TOOL-dRetiredFork-12 TOOL-dRetiredFork-13 TOOL-dRetiredFork-14 TOOL-dRetiredFork-15 TOOL-dRetiredFork-16 TOOL-dRetiredFork-17 TOOL-dRetiredFork-19 TOOL-dRetiredFork-20 |
| [2026-09-03-review-TOOL-dRetiredFork-1-21-and-depl-1-9-closing-diff.md](../reviews/2026-09-03-review-TOOL-dRetiredFork-1-21-and-depl-1-9-closing-diff.md) | diff-review | DEPL-dRetiredFork-1 DEPL-dRetiredFork-3 DEPL-dRetiredFork-4 DEPL-dRetiredFork-5 DEPL-dRetiredFork-6 DEPL-dRetiredFork-7 DEPL-dRetiredFork-8 DEPL-dRetiredFork-9 TOOL-dRetiredFork-1 TOOL-dRetiredFork-2 TOOL-dRetiredFork-3 TOOL-dRetiredFork-4 TOOL-dRetiredFork-5 TOOL-dRetiredFork-6 TOOL-dRetiredFork-7 TOOL-dRetiredFork-8 TOOL-dRetiredFork-9 TOOL-dRetiredFork-10 TOOL-dRetiredFork-11 TOOL-dRetiredFork-12 TOOL-dRetiredFork-13 TOOL-dRetiredFork-14 TOOL-dRetiredFork-15 TOOL-dRetiredFork-16 TOOL-dRetiredFork-17 TOOL-dRetiredFork-18 TOOL-dRetiredFork-19 TOOL-dRetiredFork-20 |

<!-- /gen:spec-records -->

## 1. Goal

PROMOTED from spec-audit round 2, blocker 5. `TOOL-dRetiredFork-14` S1 and S1b build the repath
capability inside `tools/settings-merge.py` — the `hook_path` default and the `HOOK_MARKER` dedup.
That is correct for agent-cap and reaches nothing else. Verified at HEAD,
`tools/settings-merge.py:286` resolves `hook_path = a.hook_path or frag["hook_path"]`, so for the
other two hooks the path comes from a committed fragment FILE:

- `tools/hooks/scratch-guard.fragment.json:6` — `"hook_path": ".claude/hooks/scratch-guard.js"`
- `tools/memory-recall/recall-opened.fragment.json:6` — `"hook_path": ".claude/hooks/recall-opened.js"`

Independently, `tools/memory-recall/adopt-memory-recall.sh` copies `recall-opened.js` into
`.claude/hooks/` under `--with-hook`, re-installing the exact copy `TOOL-dRetiredFork-14` S2
withdraws, whatever the descriptor says.

So two of the three rows in that unit's §4 Inventory stay wired to a path that stops shipping, and
one adopter keeps re-creating it. **That is the silent unwiring its §5 calls the highest risk in the
build, produced by the unit written to prevent it.**

## 2. Scope (IN)

- **S1** — Repath both fragment files to `{prefix}/hooks/scratch-guard.js` and
  `{prefix}/memory-recall/recall-opened.js`, matching the destinations `TOOL-dRetiredFork-14` S2
  leaves shipping.
- **S2** — Stop `tools/memory-recall/adopt-memory-recall.sh --with-hook` writing into
  `.claude/hooks/`, and make its closing instruction name the surviving copy. That line is the last
  thing an adopter reads at the moment they wire the hook, so a stale path there is worse than a
  stale path in a descriptor.
- **S3** — Answer in `TOOL-dRetiredFork-14` S1b, explicitly, whether the repath mode rewrites a path
  supplied by a FRAGMENT or only the built-in default. The answer decides whether S1's edits are
  sufficient, and neither spec states it today.
- **S4** — The gate: over `tools/**/*.fragment.json` plus every adopter script, assert that every
  `hook_path`, and every hook destination an adopter WRITES, resolves to a destination some
  `kit.toml` rule declares. A fragment naming a path no descriptor ships is a wiring hole whatever
  unit created it.
- **S5** — Observe the RED first: revert one fragment to `.claude/hooks/`, confirm the gate reds
  naming the fragment and the undeclared destination, restore.
- **S6** — The ordering constraint this unit inherits: the wired command must move BEFORE the old
  copy is withdrawn. `DEPL-dRetiredFork-3` S5 and AC9 own enforcing it; this unit must not withdraw
  anything before that lands, and says so rather than assuming it.

## 3. Non-goals (OUT)

- The `agent-cap` hook. `TOOL-dRetiredFork-14` owns it and its path genuinely does come from the
  built-in default S1b fixes.
- Withdrawing the `.claude/hooks/` destinations. That is `TOOL-dRetiredFork-14` S2, sequenced with
  it, and doing it here would be the unwiring this unit exists to prevent.
- Deleting an adopter's installed second copy. gov stops SHIPPING one; removal is
  `govkit update --write-withdrawals` on the adopter's own timing.

## 4. Design

### Inventory

| carrier | today | after |
|---|---|---|
| `tools/hooks/scratch-guard.fragment.json:6` | `.claude/hooks/scratch-guard.js` | `{prefix}/hooks/scratch-guard.js` |
| `tools/memory-recall/recall-opened.fragment.json:6` | `.claude/hooks/recall-opened.js` | `{prefix}/memory-recall/recall-opened.js` |
| `tools/memory-recall/adopt-memory-recall.sh` `--with-hook` | copies into `.claude/hooks/` | writes the shipped copy, names it in the closing line |

### Migration

An adopter already wired at the old path is not repaired by a fragment edit alone — that is exactly
what `TOOL-dRetiredFork-14` B3 established for agent-cap, and S3 exists because the same question
has a possibly different answer when the path arrives from a fragment.

### Alternatives rejected

Leaving the fragments and letting `--hook-path` override them per install. It works and it moves the
decision to whoever runs the installer, which is how two of three hooks came to disagree with their
own descriptors in the first place.

## 5. Production-readiness checklist

- security — scratch-guard and agent-cap are security-shaped guards; a window in which either is
  unwired is the risk, and S6's ordering plus `DEPL-dRetiredFork-3` AC9 are the mitigation.
- perf / scale — two JSON edits, one shell edit, one gate pass over a small tracked population.
- a11y — N/A.
- i18n — N/A.
- error / empty / loading states — a fragment with no `hook_path` must REFUSE, not default; an empty
  fragment population REFUSES, because a gate that found no fragments reports the same zero as a
  clean tree.
- observability — the gate names every fragment it graded and the descriptor rule each resolved to.
- risks — repathing a fragment while an adopter's settings still name the old path leaves the hook
  unwired at that adopter. S6 is the ordering answer and `TOOL-dRetiredFork-14` S4's report is the
  detection.
- testing + left-shift gates — S5's observed RED plus arms for a fragment resolving, one not
  resolving, and an empty population.
- migration / rollback — reverting is restoring two JSON values and one shell line.
- user docs — `WIRE-INTO-PROJECT.md`'s hook-wiring step names the shipped destination once.

## 6. Acceptance criteria

- **AC1** — After the change, `grep -rn '\.claude/hooks/' tools/**/*.fragment.json` returns nothing.
- **AC2** — `bash tools/memory-recall/adopt-memory-recall.sh --with-hook` against a fixture writes
  the shipped copy and no file under `.claude/hooks/`, and its closing instruction names the path it
  actually wrote.
- **AC3** — `TOOL-dRetiredFork-14` S1b states whether the repath mode rewrites a fragment-supplied
  path, and this spec's §9 records which answer it got.
- **AC4** — When a fragment's `hook_path` names a destination no `kit.toml` rule declares, the new
  gate exits non-zero naming both; the RED is observed by reverting one fragment before wiring.
- **AC5** — When `tools/**/*.fragment.json` matches nothing, the gate REFUSES.
- **AC6** — `bash tools/check-wiring.sh` exits `0` and reports the wired command resolving to a
  tracked file, at gov and against a fixture.
- **AC7** — `bash tools/check-testsuite-counts.sh` exits `0` and the leg declares a ceiling.

## 7. Gates

`check-wiring self-test` · `scratch-guard self-test` · `memory-recall skill wiring` ·
`settings-merge selftest` · `testsuite counts (every bar self-test prints one)` · `govkit selfcheck`.

## 8. Open questions

- **F1 — does the repath mode rewrite a fragment-supplied path?** S3 asks it of
  `TOOL-dRetiredFork-14` and the answer changes this unit's sufficiency: if it does, the fragment
  edits are belt-and-braces; if it does not, they are the only fix and an already-wired adopter needs
  a separate remedy. Recommendation: it should, because the fragment is gov's own data and an
  adopter cannot edit it without forking — which is the class this whole build exists to end.
- **F2 — does `--with-hook` survive at all?** Its whole job is installing a second copy. With one
  copy shipped and wired, the flag may be vestigial. Recommendation: keep it, writing the shipped
  destination, and let `DEPL-dRetiredFork-7`'s census say whether any adopter still relies on it.

**RESOLVED (owner, 2026-09-02): every fork above is settled by its own stated Recommendation.** The owner ratified them as written on 2026-09-02 with the instruction to fold the recommendations. No fork is resolved against its recommendation and none by silence; where a later measurement contradicts a ratified pick, that is a new fork with a new id.

## 9. Revision log

- rev-2 . 2026-09-03 . BUILT, and TWO of six scope items were already delivered by
  `TOOL-dRetiredFork-14` one unit earlier. S1 is DONE: both fragments carry a `{kit}` token expanded
  against THE FRAGMENT'S OWN LOCATION, which is stronger than the `{prefix}` this spec asked for
  because it is correct for a repo whose kits sit at more than one prefix.

  **AC3's answer, recorded as the criterion requires: the repath DOES rewrite a fragment-supplied
  path.** `merge()` takes the fragment, `resolve_hook_path()` expands its token, and a command whose
  marker matches but whose path differs is rewritten in place. So S1's edits are sufficient for an
  already-wired tree, and the permissive reading is the one that shipped.

  S2 was the live find: `adopt-memory-recall.sh --with-hook` still did `mkdir -p .claude/hooks` and
  copied into it, re-creating the exact duplicate the previous unit withdrew, with a closing line
  naming it. It now copies NOTHING -- the hook already ships in the kit dir -- and names the path
  that actually exists.

  S4's gate quantifies over two populations because one is not enough: the fragments, and the
  ADOPTER SCRIPTS. A gate over declarations alone would have passed the whole time that installer
  was re-creating the withdrawn copy, since it reads no fragment. All five arms were observed RED
  before wiring, including the empty-population refusal.



- rev-1 · 2026-09-02 · initial draft. PROMOTED from spec-audit round 2 blocker 5 under BUILD-METHOD
  M4's disposition rule. Both fragment values, `tools/settings-merge.py:286` and the
  `adopt-memory-recall.sh` copy were read at `b0108f13` rather than taken from the review.

## 10. Reuse audit

The seam is `tools/settings-merge.py`'s `merge(obj, hook_path, frag)` and the fragment contract it
reads — `python tools/codebase-map/reuse_lookup.py "resolve a document's backticked tokens against
the tree that owns them"` reports `owners_of` (fan-in 3) as the corpus's declaration-to-owner join,
and S4's gate is that join applied to hook destinations rather than to map keys. The fragment files
are existing declared data; nothing new is introduced but the assertion between them and `kit.toml`.

Recall terms used: `fragment`, `hook_path`, `settings-merge`, `scratch-guard`, `recall-opened`,
`with-hook`, `wiring`, `destination`, `descriptor`, `withdrawal`, `adopter`, `unwired`.
