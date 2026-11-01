# TOOL-dScopedBuild-30 — the gate keys read through the memory-tree kit's one policy adapter, `read_policy_value`, not a second reader in `routed_commits.py`

**Status:** OPEN · rev-3 · 2026-11-01 · node a · Tier-2 · base f4597719 · streams tooling · order 3 · advances TOOL-dScopedBuild-16

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-01-build-TOOL-dScopedBuild-1-agent-ledger.md](../build/2026-11-01-build-TOOL-dScopedBuild-1-agent-ledger.md) | journal | TOOL-dScopedBuild-1 TOOL-dScopedBuild-2 TOOL-dScopedBuild-3 TOOL-dScopedBuild-4 TOOL-dScopedBuild-5 TOOL-dScopedBuild-6 TOOL-dScopedBuild-7 TOOL-dScopedBuild-8 TOOL-dScopedBuild-9 TOOL-dScopedBuild-10 TOOL-dScopedBuild-11 TOOL-dScopedBuild-12 TOOL-dScopedBuild-13 TOOL-dScopedBuild-14 TOOL-dScopedBuild-15 TOOL-dScopedBuild-25 TOOL-dScopedBuild-26 TOOL-dScopedBuild-27 TOOL-dScopedBuild-28 TOOL-dScopedBuild-29 TOOL-dScopedBuild-31 TOOL-dScopedBuild-32 TOOL-dScopedBuild-33 TOOL-dScopedBuild-34 TOOL-dScopedBuild-35 TOOL-dScopedBuild-36 TOOL-dScopedBuild-37 TOOL-dScopedBuild-38 TOOL-dScopedBuild-39 TOOL-dScopedBuild-40 TOOL-dScopedBuild-41 |
| [2026-11-01-review-TOOL-dScopedBuild-25-spec-audit-round1.md](../reviews/2026-11-01-review-TOOL-dScopedBuild-25-spec-audit-round1.md) | spec-audit | TOOL-dScopedBuild-32 TOOL-dScopedBuild-33 TOOL-dScopedBuild-28 TOOL-dScopedBuild-34 TOOL-dScopedBuild-27 TOOL-dScopedBuild-29 TOOL-dScopedBuild-31 TOOL-dScopedBuild-26 TOOL-dScopedBuild-25 TOOL-dScopedBuild-35 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 1 to 15
(`memory/builds/dScopedBuild/reviews/2026-11-01-review-TOOL-dScopedBuild-1-spec-audit-round1.md`)
confirmed finding **id 19 at HIGH**, report item **H6**. `TOOL-dScopedBuild-14` S1 mints
`read_gate_value(key, repo)` in `tools/memory-tree/routed_commits.py`, with its own `Refusal` and
allowed-value check. The memory-tree kit's adapter is already specced as TOOL-dTotalRecall-8 S10's
`read_policy_value(key, root, rev=None)` in `tools/memory-tree/policy_value.py`, raising
`PolicyRefused`, and dTotalRecall is an ancestor of this build, so it lands first. Unit 14's §4
rejects only the playbook kit's copy. Built as written, the kit holds two key readers with different
refusal classes, units 3 and 8 calling one and ten other builds' units the other.

This unit makes the adapter the one reader of `deviation.gate`, `build.scope` and the four
`retrofit.*` keys, checks each value where the code branches on it, and maps the adapter's refusal to
the legs' exit 2. It repairs `TOOL-dScopedBuild-14` and builds one step after it (order 3).

## 2. Scope (IN)

- **S1** — The reader. Every read unit 14 S1 gives to `read_gate_value` calls
  `read_policy_value(key, root)` from `tools/memory-tree/policy_value.py`, a module of the same kit,
  with the key a string literal first: `read_policy_value("deviation.gate", root)` in unit 14 S4, S5
  and S7. `read_gate_value` is not minted. Unit 14 §4's last rejected-alternative bullet is answered:
  the memory-tree adapter is the reader, and it reads the landed revision as `policy.py get` does
  (PLAY-dOrderedCharter-7 §4 "The policy reads"). Observed by AC1 and AC3.
- **S2** — The check. `check_gate_value(key, lines, allowed)` in `routed_commits.py`, pure, returns
  the first line of `lines` when it is a member of `allowed` and otherwise raises `Refusal` naming the
  key and the value. Each call site passes the closed set its code branches on: `POLICIES`
  (`tools/memory-tree/deviation_join.py:142`, unit 14 S3's order) for `deviation.gate`. Observed by
  AC2.
- **S3** — The refusal. The two CLIs that read a key, `routed_commits.py` and
  `deviation_join.py --staged`, read `policy_value.PolicyRefused` as they read `Refusal`: exit 2 with
  one line naming the key and the adapter's stderr line, never a default. Observed by AC1.
- **S4** — Units 14 AC1 and AC10's third clause are superseded. AC1 is restated by this unit's AC1,
  and AC10's `grep -c 'read_gate_value("deviation.gate"' tools/memory-tree/routed_commits.py` by AC3.
  Unit 14's acceptance ledger answers both with a note naming `TOOL-dScopedBuild-30 S4`. Observed by
  AC3.

## 3. Non-goals (OUT)

- The adapter itself: TOOL-dTotalRecall-8 S10 builds it, to PLAY-dOrderedCharter-7's contract.
- What each value does: unit 14's three values and unit 3's and unit 8's stand.
- The reads of units 3 and 8, which their own builds spell through S1 and S2 as their §3 lines say.
- The left-shift scout-brief rule the report names. No clause of this build names it.

### Edges

- **consumes-from** `TOOL-dScopedBuild-14` — S1's `read_gate_value`, which S1 to S3 answer with the adapter, the check and the refusal, and AC1 and AC10's third clause, which S4 supersedes (id 19)
- **hands-off** `TOOL-dScopedBuild-3` — S4's `build.scope` read, spelled `check_gate_value("build.scope", read_policy_value("build.scope", root), <the three values>)` by that unit's build
- **hands-off** `TOOL-dScopedBuild-8` — S1's four `retrofit.*` reads, each spelled through `read_policy_value` with its key literal and checked by `check_gate_value` against that key's own closed set
- **consumes-from** external — TOOL-dTotalRecall-8 S10's `read_policy_value` and `PolicyRefused`, DEFERRED at base and an ancestor's, landed before this build runs
- **hands-off** `TOOL-dScopedBuild-39` — S2's `check_gate_value`, which that unit's S20 calls, AC3, which its S7 completes, and §4's last command, which its S27 respells (ids 8, 12, 18)
- **hands-off** `TOOL-dScopedBuild-41` — the ledger note answering §4's last Evidence command, naming TOOL-dScopedBuild-39 S27, which that unit's AC3 reads (ids 2, 14, 23)

## 4. Design

### Evidence

- TOOL-dTotalRecall-8 S10 (`memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-8.md:81-82`)
  specs `read_policy_value` in `tools/memory-tree/policy_value.py`, and its §8 F4 rules a kit-local
  adapter because a kit imports no sibling. Its §3 hands the module to TOOL-dTotalRecall-16.
- PLAY-dOrderedCharter-7 §4 "The policy reads" (`.../2026-10-23-spec-PLAY-dOrderedCharter-7.md:196-211`):
  the adapter runs `get <key> --explain` in `root`, returns the stdout lines and the explain line, and
  raises `PolicyRefused` on exit 2 or with no policy kit.
- `policy.py get` refuses a value its catalogue row does not admit (`tools/policy/policy.py:596`), so
  S2 refuses only what a future row widens past the code's closed set.
- The reader-coverage arm counts `read_policy_value("deviation.gate", root)` by its first row
  (`tools/policy/check_policy.py:426-427`).
- `git grep -l read_policy_value -- 'memory/builds/*/spec/'` lists 50 specs at `c891f007`, PINNED on
  2026-11-01.

### The read, after this unit

```
lines = read_policy_value("deviation.gate", root)          # PolicyRefused -> exit 2 naming the key
value = check_gate_value("deviation.gate", lines, POLICIES) # Refusal -> exit 2 naming key and value
```

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `check_gate_value` | python function, `routed_commits.py` | `py.function`, OK |

### Migration

None: no stored data changes.

### Rollout

Built at order 3, one step after unit 14 (order 2), tied with unit 2. Units 3 (order 4) and 8
(order 6) read their keys through S1 and S2.

### Files touched (estimate)

- `tools/memory-tree/routed_commits.py`
- `tools/memory-tree/deviation_join.py`
- `memory/map/generated/symbols.json`, regenerated by `gen_map.py --write`

### Alternatives rejected

- **Keep `read_gate_value` as a wrapper over the adapter.** It is a second name for one read whose
  refusal class differs, the shape the finding names; S2 keeps only the value check.
- **Rename the reads in units 3 and 8 alone, the finder's fix.** It leaves unit 14's own AC10 grepping
  the old name, so a correct build reds it; S4 supersedes that clause.

## 5. Production-readiness checklist

- security — deny by default: a refused read and an unknown value each exit 2, as unit 14 S1 asked.
- perf / scale — one `get` per key per run, as before.
- error / empty / loading states — no policy kit raises `PolicyRefused`, exit 2 naming the key.
- observability — the refusal line carries the adapter's stderr line.
- risks — the adapter lands with an ancestor; until it lands the build cannot run this unit, which
  is the precondition §3 names.
- testing — AC1 and AC2 in the routed-commits selftest, AC3 by probe.
- migration — none.
- user docs — none under `help/`; no user-facing surface changes.

## 6. Acceptance criteria

- **AC1** — When the routed-commits selftest's fixture repository has a landed revision holding no
  policy file, `check_gate_value("deviation.gate", read_policy_value("deviation.gate", root),
  POLICIES)` returns `refuse`; with one setting `[deviation]` `gate = "report"` it returns `report`;
  with the policy kit unresolved, `python routed_commits.py --build dFixA` exits 2 printing
  `deviation.gate`.
  Red when: an unread key returns a value, or a refused read exits 0 or 1.
  fixture: built by the selftest; the file is committed on the commit the remote's `main` names.
- **AC2** — When `python -c` calls `routed_commits.check_gate_value("k", ["bogus"], ("a", "b"))`, it
  raises `Refusal` naming `k` and `bogus`; over `["a"]` it returns `a`.
  Red when: an out-of-set value is returned.
- **AC3** — When `git grep -n read_gate_value -- tools/` runs on the built tree it prints nothing, and
  `check_policy.scan_reader_keys(".")` holds `deviation.gate`.
  Red when: the second reader is defined, or no literal read of the key exists.

## 7. Gates

`routed-commits selftest` · `routed commits name a specced unit` · `policy fixtures` · `policy check` · `codebase-map coverage + freshness` · `recall floor` · `recall floor arms` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/memory-tree/routed_commits.py · covers AC1 AC2 · the selftest's policy-file fixture read through the adapter, an unresolved kit, and an out-of-set value, staged by returning the value unchecked · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a)
  `**Derived:**` naming `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of unit 14's clause. RESOLVED
  (agent, 2026-11-01, delegated): (a), rung 3, the precedent `TOOL-dWitnessedBar-91` §8 F1 set.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft, promoted from the round-1 spec audit of units 1 to 15, id 19
  (HIGH, item H6).
- rev-2 · 2026-11-01 · §3 · the Edges block gains the bullets mirroring the edges of TOOL-dScopedBuild-39,
  the promotions of the round-1 spec audit of units 25 to 35 (ids 8, 12, 18).
- rev-3 · 2026-11-01 · §3 · the Edges block gains the bullet mirroring the edges of TOOL-dScopedBuild-41,
  the promotions of the round-1 spec audit of units 36 to 39 (ids 2, 14, 23).

## 10. Reuse audit

The seam is TOOL-dTotalRecall-8 S10's `read_policy_value` in `tools/memory-tree/policy_value.py`,
the kit's one policy adapter, which this build's specs had not named; the scout record
`memory/builds/dScopedBuild/build/2026-11-01-build-TOOL-dScopedBuild-1-reuse-scout-a.md` looked only
at the playbook path.
`python tools/codebase-map/reuse_lookup.py "read a policy value through the memory-tree kit adapter
and refuse an out of set value"` ranked `read`, `read_text`, `tree`, `resolve_kit_dir` and `kit_rel`;
the adapter is not in the tree at base, so the map cannot see it, and the spec corpus is where it
was found.

Recall terms used: `python tools/memory-recall/query.py "how does a python module of the codebase-map kit read a policy key" --terms "read_policy_value policy_value.py PolicyRefused codebase-map memory-tree adapter resolve_kit_dir reader coverage literal"`
