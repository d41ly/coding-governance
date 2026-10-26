# TOOL-dBoundRoles-57 — the memory-recall kit's description invariant follows the Skill off the refused tools: augments shell `grep` and `git grep`, and names neither search tool

**Status:** OPEN · rev-2 · 2026-10-26 · node d · Tier-2 · base 462d20f3 · streams tooling · order 31 · advances TOOL-dBoundRoles-27

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dBoundRoles-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dBoundRoles-1-agent-ledger.md) | journal | TOOL-dBoundRoles-1 TOOL-dBoundRoles-2 TOOL-dBoundRoles-3 TOOL-dBoundRoles-4 TOOL-dBoundRoles-5 TOOL-dBoundRoles-6 TOOL-dBoundRoles-7 TOOL-dBoundRoles-8 TOOL-dBoundRoles-9 TOOL-dBoundRoles-10 TOOL-dBoundRoles-11 TOOL-dBoundRoles-12 TOOL-dBoundRoles-13 TOOL-dBoundRoles-14 TOOL-dBoundRoles-15 TOOL-dBoundRoles-16 TOOL-dBoundRoles-17 TOOL-dBoundRoles-18 TOOL-dBoundRoles-19 TOOL-dBoundRoles-20 TOOL-dBoundRoles-21 TOOL-dBoundRoles-22 TOOL-dBoundRoles-23 TOOL-dBoundRoles-24 TOOL-dBoundRoles-25 TOOL-dBoundRoles-26 TOOL-dBoundRoles-37 TOOL-dBoundRoles-38 TOOL-dBoundRoles-39 TOOL-dBoundRoles-40 TOOL-dBoundRoles-41 TOOL-dBoundRoles-42 TOOL-dBoundRoles-43 TOOL-dBoundRoles-44 TOOL-dBoundRoles-45 TOOL-dBoundRoles-46 TOOL-dBoundRoles-47 TOOL-dBoundRoles-48 TOOL-dBoundRoles-49 TOOL-dBoundRoles-50 TOOL-dBoundRoles-51 TOOL-dBoundRoles-52 TOOL-dBoundRoles-53 TOOL-dBoundRoles-54 TOOL-dBoundRoles-55 TOOL-dBoundRoles-56 TOOL-dBoundRoles-58 TOOL-dBoundRoles-59 TOOL-dBoundRoles-60 TOOL-dBoundRoles-61 TOOL-dBoundRoles-62 TOOL-dBoundRoles-63 |
| [2026-10-26-review-TOOL-dBoundRoles-52-spec-audit-round1.md](../reviews/2026-10-26-review-TOOL-dBoundRoles-52-spec-audit-round1.md) | spec-audit | TOOL-dBoundRoles-54 TOOL-dBoundRoles-55 TOOL-dBoundRoles-52 TOOL-dBoundRoles-53 TOOL-dBoundRoles-56 TOOL-dBoundRoles-58 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of the seven promoted specs 45 to 51
(`memory/builds/dBoundRoles/reviews/2026-10-26-review-TOOL-dBoundRoles-45-spec-audit-round1.md`) confirmed
finding **id 29 at HIGH**, report item **H4**. No other id shares the item.

`TOOL-dBoundRoles-51` S8 rewords `tools/memory-recall/SKILL.template.md:15` and `:66` from the search
tools to shell `grep` and `git grep`, and its AC8 requires `grep -nwE 'Grep|Glob'` over the Skills to
print nothing. `tools/memory-recall/selftest.py:1619`, in `test_skill_description_invariants`, asserts
`Grep`, `Glob`, `ordinary code search` and `ADDS retrieval` are in the rendered description, the kit's
pin that the Skill augments code search and never intercepts it. 51's Files touched names neither the
selftest nor `tools/memory-recall/README.md:184`, which still says the Skill "augments Grep and Glob",
and its §7 omits the `memory-recall kit selftest` leg. Built as written, 51 AC8 greens and the kit's
self-test reds, and the builder's only way to green it is to delete an invariant 51 never scoped.

This unit rewrites the invariant to the new wording and keeps what it protects. It repairs
`TOOL-dBoundRoles-51` and builds one step after it (order 31).

## 2. Scope (IN)

- **S1** — The invariant, re-worded. `test_skill_description_invariants` in
  `tools/memory-recall/selftest.py` asserts the rendered description holds `git grep`,
  `ordinary code search` and `ADDS retrieval`, the tokens of the wording 51 S8 writes, and holds neither
  word `Grep` nor `Glob`. The comment over check 1 says the Skill augments shell `grep` and `git grep`
  and never replaces or intercepts them; the comment at `:1644` says a miss falls back to shell `grep`.
  Observed by AC1.
- **S2** — The README follows. `tools/memory-recall/README.md:184` says the description augments shell
  `grep` and `git grep` rather than replacing them, and that `selftest.py` pins it. Observed by AC2.
- **S3** — The leg is named. This spec's §7 names `memory-recall kit selftest`, the leg whose suite holds
  S1, so the close runs it over 51's and this unit's changes together. Observed by AC1.

## 3. Non-goals (OUT)

- The Skill template's wording and its render: `TOOL-dBoundRoles-51` S8's, read here. Where 51's text
  does not hold `git grep`, S1's token is the remedy's reader, and the pass returns the mismatch to the
  main loop as a parked row rather than rewording 51's sentence.
- Every other check of `test_skill_description_invariants`: the flag set, the kickoff clause and the
  launcher checks are unchanged.
- The refused-tool Skill leg the report's left-shift names. S1's no-search-tool assertion is the kit's
  own regression for this Skill.

### Edges

- **consumes-from** `TOOL-dBoundRoles-51` — S8's re-worded description in the memory-recall Skill template and its render, whose tokens S1 asserts (id 29)
- **hands-off** `TOOL-dBoundRoles-60` — S1, S3 and AC1, which unit 60 restates: the no-search-tool half over the whole Skill text, the invariant lifted into one undecorated function and S3's observer (ids 33, 34 and 39 of the round-1 audit of units 52 to 58)

## 4. Design

### Evidence

Read at base `462d20f3` on 2026-10-26:

- `tools/memory-recall/SKILL.template.md:15` reads "Grep and Glob own those, they are correct, and this
  skill neither replaces nor intercepts them: it ADDS retrieval".
- `tools/memory-recall/selftest.py:1598` defines `test_skill_description_invariants`; `:1617-1620` loop
  over the four tokens; `:1644` says the guidance falls back to Grep.
- `tools/memory-recall/README.md:182-186` describes the three pinned properties.
- `tools/gate-legs.json`'s `memory-recall kit selftest` runs `python3 {prefix}/memory-recall/selftest.py`
  and guards `{prefix}/memory-recall/`.

### What the invariant protects

Check 1 exists so the Skill's description cannot be re-worded into a claim on ordinary code search. The
tokens are the evidence of that claim's opposite. Swapping `Grep` and `Glob` for `git grep` keeps the
evidence, and the added no-search-tool assertion pins 51's move inside the kit that owns the Skill,
where 51 AC8's grep is a one-time observation.

### Inventory

Minted: none. One assertion joins an existing check.

### Migration

None: no stored data changes. An adopter's rendered Skill re-renders on the kit's next update, as 51 S8
already requires.

### Rollout

Live at landing, at order 31, after unit 51 at order 30. `TOOL-dBoundRoles-56` shares the order and
writes no file this unit writes.

### Files touched (estimate)

- `tools/memory-recall/selftest.py`
- `tools/memory-recall/README.md`

### Alternatives rejected

- **Drop check 1.** It deletes the kit's AC18 invariant, which no spec scoped.
- **Keep `Grep` and `Glob` in the description.** It undoes 51 S8, which keeps the main loop off a tool
  `TOOL-dBoundRoles-10` refuses.

## 5. Production-readiness checklist

- security — keeps the Skill from steering the main loop to a refused tool, now pinned in the kit's
  suite; no new write path.
- perf / scale — one regex over the description.
- error / empty / loading states — a missing token fails naming it, as check 1 does today.
- observability — each failing token is named.
- risks — 51's exact wording differs from S1's tokens; §3 names the disposition.
- testing — AC1 and AC2 by a direct call of the check and grep; the arm of §7 at the close.
- migration — none.
- user docs — the kit README by S2.

## 6. Acceptance criteria

- **AC1** — When a `python -c` slice puts `tools/memory-recall` on `sys.path`, imports the kit's self-test
  module as a library, runs no suite, and calls `test_skill_description_invariants` on the tree 51 left,
  it returns its summary line; with "Grep and Glob own those" restored to a scratch copy of the template,
  it fails naming `Grep`.
  Red when: the invariant asserts a word 51 removed, or passes a description that names a search tool.
  fixture: the scratch template copy is written under the run's scratch path by the probe.
- **AC2** — When `grep -nwE 'Grep|Glob' tools/memory-recall/README.md` runs, it prints nothing, and
  `grep -n 'git grep' tools/memory-recall/README.md` prints the pinned-properties line.
  Red when: the README still says the Skill augments the search tools.

## 7. Gates

`memory-recall kit selftest` · `memory-recall skill wiring` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/memory-recall/selftest.py · covers AC1 · the description invariant over the shell-probe wording, staged by restoring "Grep and Glob own those" to the template, which reds the no-search-tool assertion · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a) `**Derived:**`
  naming `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of the repaired unit's clause. Unit 51 carries no
  clause; veto 1 discards (b). RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the precedent
  `TOOL-dDeclaredLoop-36` §8 F1 set. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit of units 45 to 51, id 29
  (HIGH, item H4), on the report's fix.
- rev-2 · 2026-10-26 · §3 · the Edges block gains the bullet mirroring TOOL-dBoundRoles-60, the minors batch of the round-1 audit of units 52 to 58; nothing else moved.

## 10. Reuse audit

The seam is `test_skill_description_invariants` (`tools/memory-recall/selftest.py:1598`), whose token
loop S1 re-words and extends rather than adding a second check.
`python tools/codebase-map/reuse_lookup.py "a skill description invariant asserted by a selftest token tuple"`
ranked `resolve_prefix_token`, `read_attribution_tokens`, `build_id_token_re` and `demand_safe_token`,
none a Skill description check, so no existing seam fits beyond the check named.

Recall terms used: `python tools/memory-recall/query.py "how is the recall skill kept from intercepting code search" --terms "memory-recall skill description augments Grep Glob ordinary code search selftest invariant"`
