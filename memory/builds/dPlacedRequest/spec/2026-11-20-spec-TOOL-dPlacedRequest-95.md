# TOOL-dPlacedRequest-95 — the kickoff hook never runs a checker it resolved from its target's tree

**Status:** CLOSED · rev-2 · 2026-11-20 · node d · Tier-2 · base 95c3103a · streams tooling · order 37

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-20-build-TOOL-dPlacedRequest-95-1-acceptance-ledger.md](../build/2026-11-20-build-TOOL-dPlacedRequest-95-1-acceptance-ledger.md) | journal | — |
| [2026-11-21-build-TOOL-dPlacedRequest-95-deviation-730.md](../build/2026-11-21-build-TOOL-dPlacedRequest-95-deviation-730.md) | deviation | — |
| [2026-11-20-prompt-TOOL-dPlacedRequest-95-1-spec-writer.md](../prompts/2026-11-20-prompt-TOOL-dPlacedRequest-95-1-spec-writer.md) | journal | — |
| [2026-11-20-prompt-TOOL-dPlacedRequest-95-audit-fold-text-brief.md](../prompts/2026-11-20-prompt-TOOL-dPlacedRequest-95-audit-fold-text-brief.md) | research | TOOL-dPlacedRequest-98 TOOL-dPlacedRequest-99 |
| [2026-11-20-prompt-TOOL-dPlacedRequest-95-closing-review-spec-brief.md](../prompts/2026-11-20-prompt-TOOL-dPlacedRequest-95-closing-review-spec-brief.md) | research | — |
| [2026-11-20-review-TOOL-dPlacedRequest-95-99-spec-audit.md](../reviews/2026-11-20-review-TOOL-dPlacedRequest-95-99-spec-audit.md) | spec-audit | TOOL-dPlacedRequest-96 TOOL-dPlacedRequest-97 TOOL-dPlacedRequest-98 TOOL-dPlacedRequest-99 |

<!-- /gen:spec-records -->

## 1. Goal

The closing diff review of this build, round 1
(`memory/builds/dPlacedRequest/reviews/2026-11-20-review-TOOL-dPlacedRequest-1-64-closing-diff-round1.md`),
confirmed item **H1** at HIGH, finding id 1, and the round-2 exit promoted it to this unit.
`resolveKickoffChecker` in `tools/hooks/scratch-guard.js` walks a third rung, the toplevel of the
commit or edit target's repository, and `readCard` then runs the one `manifest-check.sh` that tree
tracks, inside PreToolUse, before any allow or deny. In an adopter the first two rungs can both miss,
so a `git -C <clone> commit` or an Edit under another repository's routed tree runs that clone's
tracked file with the agent's privileges. This unit resolves the checker from the hook's own install
only, and gates the class.

## 2. Scope (IN)

- **S1** — H1, closed by the record's fix, which the skeptic judged SOUND. `resolveKickoffChecker`
  keeps two rungs, both read from the hook's own install: the kit resolver from `__dirname`, then the
  one tracked `manifest-check.sh` of the hook's own toplevel. The `cwd` rung goes, with the
  parameter that feeds it, so `readCard` resolves nothing from the common dir it is handed; where
  neither rung answers it returns null and the card reads as absent with the shown text it prints
  today. The header comment above `resolveKickoffChecker` is rewritten to name the two install-side
  rungs and to state that the target's tree is never a rung. The left-shift the record names lands
  with it: a scratch-guard self-test arm over its three fixtures, its `FLOOR_ASSERTIONS` rise, and the
  `scratch-guard self-test` budget row re-priced for the arm. The class is one the catalogue already
  holds, code another repository authored running with this node's privileges, so it lands as a
  section of `memory/gotchas/foreign-code-runs-on-the-ambient-credential.md`, with
  `memory/gotchas/INDEX.md` rendered by `gotchas.py --write`. Observed by AC1.

## 3. Non-goals (OUT)

- No change to how the card's path is answered once a checker resolves: the `--card --path` spawn,
  its bound and `resolveCardBash` stay as `TOOL-dPlacedRequest-34` S28 and `TOOL-dPlacedRequest-43`
  S18 left them.
- No change to the sibling resolvers the record cleared, the roles kit's `resolve_card_path` and the
  driver's `resolve_kickoff_checker`: each runs in the repository the tool itself operates on.
- No new install location for the kickoff skill. An adopter whose hook resolves no checker reads the
  card as absent, which is the hook's existing fail-closed witness, not a new refusal.

### Edges

- **consumes-from** external — the landed kickoff checker walk, built by this build's orientation-card
  unit and CLOSED with it; this unit removes the walk's third rung from the code, and the closed spec
  stays frozen
- **hands-off** external — none of this build's live units reads the removed rung

## 4. Design

### The resolver after this unit

```
resolveKickoffChecker()                      no argument
  1. agent-cap.js resolveKitDir('session-kickoff', 'manifest-check.sh', __dirname)  -> its path
  2. resolveToplevel(__dirname) -> `git ls-files -- manifest-check.sh '*/manifest-check.sh'`
       exactly one tracked hit that exists                                           -> its path
  else                                                                               -> null
readCard(commonDir, sid, checker)  checker undefined -> resolveKickoffChecker()
  null -> card.shown "(no card: no kickoff checker manifest-check.sh resolves to answer --card --path)"
```

The spawn's own `cwd` stays the work tree of the common dir, because the checker answers the path of
the card in that repository; only the choice of WHICH file runs moves to the hook's install. The
three callers, `checkOriented`, the route reader and the write gate's route context, call `readCard`
unchanged.

Cited at the base: the walk is `tools/hooks/scratch-guard.js#resolveKickoffChecker`, its list
`[__dirname, cwd]` at `tools/hooks/scratch-guard.js@e21b4d65:711`; the caller computing `cwd` from
the common dir is `tools/hooks/scratch-guard.js#readCard`; the commit gate's call is
`tools/hooks/scratch-guard.js#checkOriented` and the write gate's is
`tools/hooks/scratch-guard.js#renderRouteText`.

### The arm

Three fixtures, each with a marker file the planted checker writes, under the suite's own `$TMP`:

1. A copy of the hook's `*.js` in a directory outside any repository, as the suite's L15 rows already
   copy it, and a scratch clone tracking one `manifest-check.sh` that writes the marker and prints
   nothing. `readCard(<clone>/.git, "sgtest-c1")`, no checker argument.
2. The same copy inside a scratch repository tracking two copies of `manifest-check.sh`, so the hook's
   own toplevel rung misses, and the clone of fixture 1 as the target.
3. The hook copy of fixture 1 fed the PreToolUse payload of a Bash `git -C <clone> commit -m x`, with
   a `session_id` and a `cwd`, as `run_role_bash` builds one.

Each asserts the marker is absent and the card reads absent naming no kickoff checker. Against the
hook at the base each fixture writes the marker. Each row's text names `TOOL-dPlacedRequest-95`. The
suite's `FLOOR_ASSERTIONS` rises by the rows the arm adds, over whatever value the file holds when this
unit builds, with a comment line naming this unit and its rows.

### The header comment

The comment above `resolveKickoffChecker` (`tools/hooks/scratch-guard.js@e21b4d65:697`, its third
sentence naming the rung "the one `cwd`'s repository tracks") is rewritten with the walk: the kit
resolver from the hook's own directory, then the one tracked file of the hook's own toplevel, and
never the commit or edit target's tree, because that tree's code would run inside PreToolUse.

### The budget row

The `scratch-guard self-test` row (`tools/run-gates/selftest-budgets.txt@25b27c00:135`) holds
290 s (PINNED, that row) from a 187 s reading of 2026-11-13. It is re-priced in the PINNED-proxy shape
its peers use, never by a suite run inside the pass (`doc.build-method#m6-passes-commits-parallelism`):
the row's 187 s (PINNED, that row) plus AC1's probe time for the three fixtures, read by direct CLI on
the build's node, x1.5, its note naming both readings, this unit and that it is re-priced from the main
loop's first reading of the leg alone. The leg's `ceiling` in `tools/gate-legs.json` is 490 s (PINNED,
at the base) against an evidenced 187.0 s; the proxy reading is compared with it, and only a reading that approaches it routes a ceiling move, made from the main loop's measured
reading by `GOV_NODE=<tag> derive-ceilings.py --write --observed 'scratch-guard self-test=<s>' --how
'<direct CLI, base, node>'`, then `pass_legs.py --apply` and the `last-audit` re-stamp of
`memory/guides/SESSION-KICKOFF.md`.

### The class record

The class is the one `memory/gotchas/foreign-code-runs-on-the-ambient-credential.md` records: code
another repository authored, run with this node's environment and credential. Its fix already says an
item refuses target-side execution, and a hook resolving a checker from its target's tree is that
execution. A second record would split the class history across two disjoint anchor sets, so this
unit adds a section to the existing record instead, `## It bit again in the PreToolUse hook`, in the
shape of its earlier sections: the third rung, the clone's tracked checker run inside PreToolUse, and
the rule that a hook runs only files of its own install. The section cites `tools/hooks/scratch-guard.js`
in backticks, so `gotchas.py --for-paths tools/hooks/scratch-guard.js` selects the record, the shape
`TOOL-dPlacedRequest-98` uses for its section. Its gate names the arm.

No new record means no new key in the codebase map's `gotcha-classes` inventory
(`tools/codebase-map/map_extractors.py#EXTRACTORS` globs `memory/gotchas/*.md` by filename), so no
dossier claim is owed. The resolver keeps its name and the arm adds no function, so
`memory/map/generated/symbols.json`, which lists each symbol's id, kind and file only, does not move;
a builder who adds a function regenerates it by `python tools/codebase-map/gen_map.py --write`.

### Files touched (estimate)

- `tools/hooks/scratch-guard.js`: the resolver's two rungs, its one call and its header comment
- `tools/hooks/scratch-guard.test.sh`: the arm and the floor
- `tools/run-gates/selftest-budgets.txt`: the `scratch-guard self-test` row re-priced
- the hooks kit's version carrier, the one its descriptor names, moved once by the kit-epoch rule
- `memory/gotchas/foreign-code-runs-on-the-ambient-credential.md`: the section
- `memory/gotchas/INDEX.md`: rendered by `gotchas.py --write`

### Alternatives rejected

- **Keep the `cwd` rung behind a trust check of the target.** Any check that reads the target to decide
  whether to trust it is the same class one step later, and nothing in the hook names a trusted tree.
- **Run the target's checker in a sandbox.** No sandbox exists on the hook's path, and building one is a
  new dependency (`doc.build-method#m3-forks-the-decision-rule-and-the-limit-of-your-authority` veto 2).

## 5. Production-readiness checklist

- security — closes code execution across a trust boundary inside PreToolUse; the hook runs only
  files of its own install afterwards.
- perf / scale — one `git ls-files` fewer on a miss; the arm's three fixtures add seconds to the
  suite, re-priced in §4's budget row.
- error / empty / loading states — no rung answers: the card reads absent, the witness path the hook
  already takes for a session that never kicked off.
- observability — the absent card's shown text names that no kickoff checker resolves.
- risks — an adopter that relied on the target's tracked checker now reads its card absent; the
  witness says why, and the kickoff skill's install is what answers it.
- testing — AC1's probe and the arm in §7.
- migration — none; no data moves.
- user docs — none: the hook's card reading is internal, and no page under `help/` names the rung.

## 6. Acceptance criteria

- **AC1** — When the three fixtures of §4 are built under a scratch directory and probed through a copy
  of `tools/hooks/scratch-guard.js` by `node -e` calling `readCard` with no checker argument for the
  first two, and by the copy fed the payload on stdin for the third, no marker file exists afterwards
  and the first two print a card shown text naming no kickoff checker; and
  `python tools/memory-tree/gotchas.py --for-paths tools/hooks/scratch-guard.js` prints
  `foreign-code-runs-on-the-ambient-credential`; and
  `grep -c 'TOOL-dPlacedRequest-95' tools/hooks/scratch-guard.test.sh` prints at least 3, while
  `grep '^FLOOR_ASSERTIONS=' tools/hooks/scratch-guard.test.sh` prints a value above 396 and a comment
  line above it names `TOOL-dPlacedRequest-95`; and
  `grep -c "cwd..s repository tracks" tools/hooks/scratch-guard.js` prints 0.
  Red when: the resolver walks `cwd`, or the arm or its floor is missing; the hook at 95c3103ad is
  that break, and the same probe there writes the marker in each fixture, `gotchas.py` does not
  print `foreign-code-runs-on-the-ambient-credential`, the first grep prints 0, the floor reads 396 and the comment names the `cwd`
  rung, its RED-first reading.
  fixture: three scratch repositories the probe builds; the tree holds none today.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `scratch-guard self-test` · `every held leg is budgeted, every budget row resolves` · `agent-cap self-test` · `format-guard self-test` · `hook destinations self-test` · `policy fixtures` · `verifier fan-out self-test` · `review-join self-test` · `recall floor` · `recall floor arms` · `kit epoch (shipped bytes move, the version moves)` · `govkit selfcheck` · `lexicon naming predicates`

New arm: tools/hooks/scratch-guard.test.sh · covers AC1 · the three fixtures of §4, staged against the hook at 95c3103ad whose third rung runs the clone's tracked checker and writes the marker · FLOOR_ASSERTIONS raised by the arm's rows

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-20 · initial draft, promoted from the closing diff review round 1, item H1 (HIGH,
  finding id 1), by the round-2 exit's disposition.
- rev-2 · 2026-11-20 · S1 · §4 · AC1 · §5 · §10 · folded
  2026-11-20-review-TOOL-dPlacedRequest-95-99-spec-audit: finding id 18 (M11), the class lands as a
  section of the existing record `foreign-code-runs-on-the-ambient-credential` rather than a new one;
  finding id 24 (M13), §4 states why no dossier claim and no map regeneration is owed now that no record
  is new; finding id 25 (M14), the `scratch-guard self-test` budget row re-priced as a proxy and its
  ceiling compared; finding id 10 (L2), AC1 observes the arm's rows and the floor rise; finding id 27
  (L7), the resolver's header comment rewritten.
- rev-2 · 2026-11-20 · §4 · editorial, by 2026-11-20-prompt-TOOL-dPlacedRequest-95-audit-fold-text-brief:
  each folded duration carries its mark on its own line, and each build-method section is cited by its
  alias tag.

## 10. Reuse audit

The seam extended is the hook's own resolver, `tools/hooks/scratch-guard.js#resolveKickoffChecker`,
cut to the two rungs it already reads from its install; no new resolver is written.
`python tools/codebase-map/reuse_lookup.py "hook resolves a checker script and runs it"` ranked
`run`, `check`, `resolve` and `resolve_kit_dir`, name stems only, and the last is the kit resolver
rung 1 already reaches through `agent-cap.js`. The recall query below returned the round-1 record's
H1 and `TOOL-dPlacedRequest-2`'s scout; none disagrees with the source read above. The record cites
the walk at line 711 and the source agrees at blob e21b4d65. The nearest existing class record, found
by `grep -rln "foreign-code-runs\|ambient-credential" memory/gotchas/`, is
`memory/gotchas/foreign-code-runs-on-the-ambient-credential.md`, which this unit extends; the new
record rev-1 named, `hook-executes-code-resolved-from-its-target`, is rejected as a second record of
that class.

Recall terms used: scratch-guard resolveKickoffChecker readCard manifest-check.sh PreToolUse cwd rung kit resolver trust boundary orientation card
