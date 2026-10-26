# TOOL-dBoundRoles-56 — the three readers of a spec's H1 share one fence rule: `parse_spec_h1` and KICK R4 move with `checkBuildable` onto the length rule, and one fixture set sees one id from all three

**Status:** OPEN · rev-2 · 2026-10-26 · node d · Tier-2 · base 462d20f3 · streams tooling · order 31 · advances TOOL-dBoundRoles-27

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dBoundRoles-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dBoundRoles-1-agent-ledger.md) | journal | TOOL-dBoundRoles-1 TOOL-dBoundRoles-2 TOOL-dBoundRoles-3 TOOL-dBoundRoles-4 TOOL-dBoundRoles-5 TOOL-dBoundRoles-6 TOOL-dBoundRoles-7 TOOL-dBoundRoles-8 TOOL-dBoundRoles-9 TOOL-dBoundRoles-10 TOOL-dBoundRoles-11 TOOL-dBoundRoles-12 TOOL-dBoundRoles-13 TOOL-dBoundRoles-14 TOOL-dBoundRoles-15 TOOL-dBoundRoles-16 TOOL-dBoundRoles-17 TOOL-dBoundRoles-18 TOOL-dBoundRoles-19 TOOL-dBoundRoles-20 TOOL-dBoundRoles-21 TOOL-dBoundRoles-22 TOOL-dBoundRoles-23 TOOL-dBoundRoles-24 TOOL-dBoundRoles-25 TOOL-dBoundRoles-26 TOOL-dBoundRoles-37 TOOL-dBoundRoles-38 TOOL-dBoundRoles-39 TOOL-dBoundRoles-40 TOOL-dBoundRoles-41 TOOL-dBoundRoles-42 TOOL-dBoundRoles-43 TOOL-dBoundRoles-44 TOOL-dBoundRoles-45 TOOL-dBoundRoles-46 TOOL-dBoundRoles-47 TOOL-dBoundRoles-48 TOOL-dBoundRoles-49 TOOL-dBoundRoles-50 TOOL-dBoundRoles-51 TOOL-dBoundRoles-52 TOOL-dBoundRoles-53 TOOL-dBoundRoles-54 TOOL-dBoundRoles-55 TOOL-dBoundRoles-57 TOOL-dBoundRoles-58 TOOL-dBoundRoles-59 TOOL-dBoundRoles-60 |
| [2026-10-26-review-TOOL-dBoundRoles-52-spec-audit-round1.md](../reviews/2026-10-26-review-TOOL-dBoundRoles-52-spec-audit-round1.md) | spec-audit | TOOL-dBoundRoles-54 TOOL-dBoundRoles-55 TOOL-dBoundRoles-52 TOOL-dBoundRoles-53 TOOL-dBoundRoles-57 TOOL-dBoundRoles-58 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of the seven promoted specs 45 to 51
(`memory/builds/dBoundRoles/reviews/2026-10-26-review-TOOL-dBoundRoles-45-spec-audit-round1.md`) confirmed
finding **id 20 at HIGH**, report item **H3**. No other id shares the item; id 34 reports the same
defect from its consumers at MEDIUM, item M9, and is `TOOL-dBoundRoles-58`'s.

`TOOL-dBoundRoles-50` S9 moves `checkBuildable`'s H1 scan in `tools/hooks/scratch-guard.js` onto
`readUnfencedLines`, whose fence closes only on a run at least as long as its opener and whose backtick
opener refuses a backtick after the run. The comment at `scratch-guard.js:885-886` says that scan is the
H1 read KICK R4 (`skills/session-kickoff/manifest-check.sh:1042`) and `tree_lib.parse_spec_h1` make, and
`parse_spec_h1` calls itself THE one predicate for which id a spec defines (TOOL-aRepatriatedFork-40).
Neither twin moves. On the shape 50 AC9 builds, an H1 after a three-backtick line inside a
four-backtick fence, the spawn and write gate reads the H1 as fenced while the index generator and
kickoff read it as live, and the two name different units for one spec.

This unit takes the report's second option: the length rule reaches both twins, and one fixture set fed
to all three readers sees one answer. It repairs `TOOL-dBoundRoles-50` and builds one step after it
(order 31).

## 2. Scope (IN)

- **S1** — The memory-tree walker learns the rule. `unfenced_lines(text, by_length=False)` in
  `tools/memory-tree/tree_lib.py` gains a keyword. With `by_length=True` a fence opens on a line of at
  most three spaces of indent and a run of three or more backticks or tildes, a backtick run whose line
  holds a backtick after it opens nothing, and the fence closes only on a line of the same character
  whose run is at least as long, with nothing after it but whitespace: the rule
  `TOOL-dBoundRoles-38` S3 gives `read_unfenced_lines` and 50 S9 completes. The default keeps today's
  rule for every row reader. Observed by AC1.
- **S2** — `parse_spec_h1` walks with `by_length=True`. Its consumers read the new rule through it, each
  unchanged: `tools/memory-tree/gen_build_index.py` (`spec_ids` and its two other calls),
  `tools/memory-recall/extract.py`, `tools/memory-tree/deviation_join.py` and
  `tools/memory-tree/routed_commits.py`. Observed by AC1 and AC3.
- **S3** — KICK R4 toggles by the same rule. The awk machine at `skills/session-kickoff/manifest-check.sh`
  :1041-1043 records the opener's character and run length, refuses a backtick opener with a backtick
  after its run, and closes only on a line of that character whose run is at least as long, with nothing
  after it but whitespace. Observed by AC1.
- **S4** — The comment tells the truth. `scratch-guard.js`'s comment over `checkBuildable`'s scan names
  the rule and its two twins by function, and says all three share it. Observed by AC2.
- **S5** — One fixture set, three readers. A case in `tools/hooks/scratch-guard.test.sh` writes five
  fixture specs, each holding one live H1 and, in four of them, a decoy H1 inside a fence: a four-backtick
  fence holding a three-backtick line with the decoy after it; a tilde fence holding a backtick line and
  the decoy; a backtick line whose info string holds a backtick, followed by the live H1; a fence never
  closed holding the only H1; and a four-space-indented backtick line before the live H1. For each, it
  reads the id `parse_spec_h1` returns (`python3 -c` over `tools/memory-tree`), and checks that the
  exported `checkBuildable` admits a route naming that id and refuses one naming the decoy, and that
  `manifest-check.sh`'s R4 accepts the same route and refuses the decoy's. Observed by AC1.

## 3. Non-goals (OUT)

- Moving every reader of `unfenced_lines` onto the length rule. Eight tracked `.md` files read
  differently under it at base, `memory/TEMPLATE-SPEC.md` among them (§4 "Measured"), and the row
  readers answer other questions than which id a spec defines.
- `checkBuildable`'s own move onto `readUnfencedLines` and the format-guard walker: 50 S9's, read here.
- The differences between the readers that are not fences: R4 accepts any unfenced H1 naming the unit,
  while `checkBuildable` and `parse_spec_h1` take the first. S5's fixtures hold one live H1 each, so the
  case does not check that difference.
- The consumers' own observations of the parity: `TOOL-dBoundRoles-58`'s, for id 34.

### Edges

- **consumes-from** `TOOL-dBoundRoles-50` — S9's `checkBuildable` read through `readUnfencedLines` and the CommonMark info-string rule it adds, which S1 and S3 give the twins (id 20)
- **hands-off** `TOOL-dBoundRoles-58` — the fixture set and the shared rule, over which unit 58's item for id 34 observes each consumer of `parse_spec_h1` (id 34)
- **hands-off** `TOOL-dBoundRoles-60` — S2, S3, S5, §3, §4, §5 and §7, which unit 60 restates: the watched-file re-stamp, the leg guard over `tree_lib.py`, the fixture counts, the risk line, the consumer list and the launcher (ids 11, 17, 18, 20, 25, 30 and 31 of the round-1 audit of units 52 to 58)

## 4. Design

### Evidence

Read at base `462d20f3` on 2026-10-26:

- `tools/memory-tree/tree_lib.py:149-176` closes a fence on any line starting with the opener's marker
  character, whatever its run length; `:206-228` is `parse_spec_h1`, reading through it.
- `skills/session-kickoff/manifest-check.sh:1042` toggles `fence = !fence` on any line matching
  `^ ? ? ?(```|~~~)`, and R4 accepts any unfenced H1 whose first token is the unit.
- `tools/hooks/scratch-guard.js:885-892` toggles the same way and takes the first unfenced H1;
  `checkBuildable` is in the file's `module.exports` (`:1615`).
- `git grep -n parse_spec_h1` names its consumers in `gen_build_index.py` (`:567`, `:738`, `:8604`),
  `extract.py` (`:621`, `:695`), `deviation_join.py` (`:541`) and `routed_commits.py` (`:207`).

### Measured

On 2026-10-26, a probe compared `unfenced_lines` with S1's rule over every tracked `.md` file: 8 of
6795 yield different lines, `memory/TEMPLATE-SPEC.md`, `WIRE-INTO-PROJECT.md` and
`tools/memory-tree/SPEC-TEMPLATE.template.md` among them, which is why the default stays. Over the 1898
tracked spec files under `memory/builds/`, `parse_spec_h1` returns the same id under both rules for
every one, so S2 moves no spec's id. Both figures are PINNED at that date; AC3 re-derives the second.

### Inventory

Minted: the keyword `by_length` and the case's five fixtures. No function name.

### Migration

None: no stored data changes, and §4 "Measured" shows no tracked spec changes its id.

### Rollout

Live at landing, at order 31, after unit 50 at order 30. `TOOL-dBoundRoles-57` shares the order and
writes no file this unit writes. The kickoff engine's copy under a user's home updates by its own
install path; `manifest-check.sh` here is the source.

### Files touched (estimate)

- `tools/memory-tree/tree_lib.py`
- `skills/session-kickoff/manifest-check.sh`
- `tools/hooks/scratch-guard.js`
- `tools/hooks/scratch-guard.test.sh`

### Alternatives rejected

- **Keep `checkBuildable` on its twins' toggle, the report's first option.** It leaves the toggle that
  50 AC9's grep refuses, and the twins already differ from each other on a tilde fence holding
  backticks, so no fixture set over fence edges agrees under it (§8 F2).
- **Move every `unfenced_lines` caller.** Eight files read differently, with no clause asking for it.
- **A second walker in `parse_spec_h1`.** Two rules in one kit with no shared code; the keyword keeps one
  walker with one switch.

## 5. Production-readiness checklist

- security — the write and spawn gate, the index and kickoff resolve one unit per spec, so a route
  cannot admit a spec the index files under another id; no new write path.
- perf / scale — one comparison more per fence line in three readers.
- error / empty / loading states — an unclosed fence yields no H1 in all three, as AC1's fourth fixture
  shows.
- observability — the comment at `checkBuildable` names the rule and its twins.
- risks — the kickoff engine's size leg reads `manifest-check.sh`'s bytes; the awk grows by a few lines.
- testing — AC1 to AC3 by the parity case, grep and the index generator's check; the arm of §7 at the
  close.
- migration — none.
- user docs — none under `help/`: no user-facing surface changes.

## 6. Acceptance criteria

- **AC1** — When the scratch-guard suite's parity case feeds S5's five fixture specs to
  `parse_spec_h1`, to the exported `checkBuildable` and to `manifest-check.sh`'s R4, all three name the
  same id for each fixture, the decoy is refused by both route checks, and the unclosed fence yields no
  id from any reader.
  Red when: one reader closes a long fence on a short run, or toggles on a tilde fence's backtick line.
  fixture: the five specs and a scratch card are written under the run's scratch path by the case.
- **AC2** — When `grep -n 'parse_spec_h1' tools/hooks/scratch-guard.js` runs, it names the comment over
  `checkBuildable`'s scan, which also names R4 and the length rule.
  Red when: the comment still claims a parity the code does not keep.
- **AC3** — When `python tools/memory-tree/gen_build_index.py --check` runs on the built tree it exits 0,
  and a `python -c` probe re-runs §4 "Measured"'s comparison over the tracked specs and prints no spec
  whose id moved.
  Red when: S2 changes which unit a tracked spec defines.
  figure: the spec population is DERIVED at observation time.

## 7. Gates

`build-index selftest` · `memory-hygiene self-test` · `routed-commits selftest` · `memory-recall kit selftest` · `manifest-check self-test` · `kickoff engine size <=18KiB` · `agent-cap self-test` · `scratch-guard self-test` · `format-guard self-test` · `verifier fan-out self-test` · `review-join self-test` · `hook destinations self-test` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

`agent-cap self-test` is named because `tools/hooks/` trips its guard at base; unit 25's pass renames it
on every live §7 line when it renames the leg.

New arm: tools/hooks/scratch-guard.test.sh · covers AC1 · the five fence-edge fixtures through three readers, staged by restoring R4's `fence = !fence` toggle, which admits the first fixture's decoy · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a) `**Derived:**`
  naming `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of the repaired unit's clause. Unit 50 carries no
  clause; veto 1 discards (b). RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the precedent
  `TOOL-dDeclaredLoop-36` §8 F1 set. widens: none · relaxes: none
- **F2 — Keep `checkBuildable` on its twins' rule, or move the twins onto the length rule?** Options: (a)
  the length rule in all three, with the parity case; (b) `checkBuildable` kept on the toggle, 50 AC9
  restated, and a parity case over the shapes the toggle readers agree on. (b) fails 50 AC9 as written,
  and its parity case must leave out the tilde shape, where `tree_lib` and the toggle already disagree.
  (a) satisfies 50 AC9 and gives one rule to every H1 reader. RESOLVED (agent, 2026-10-26, delegated):
  (a), rung 3, the most feature-rich survivor. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit of units 45 to 51, id 20
  (HIGH, item H3; id 34 shares the defect at MEDIUM, item M9), on the report's second option.
- rev-2 · 2026-10-26 · §3 · the Edges block gains the bullet mirroring TOOL-dBoundRoles-60, the minors batch of the round-1 audit of units 52 to 58; nothing else moved.

## 10. Reuse audit

The seams are `tree_lib.unfenced_lines` (`tools/memory-tree/tree_lib.py:149`), which S1 extends by a
keyword rather than copying, `TOOL-dBoundRoles-38`'s rule, which S1 and S3 restate in Python and awk, and
the scratch-guard suite's existing drive of `manifest-check.sh`, which S5 reuses for R4.
`python tools/codebase-map/reuse_lookup.py "one fence rule shared by every reader of a spec heading"`
ranked `read`, `read_text`, `read_conf` and `read_journal`, none a fence walker, so no existing seam fits
beyond the walker named.

Recall terms used: `python tools/memory-recall/query.py "how is the spec H1 read kept identical across the index generator kickoff and the hooks" --terms "parse_spec_h1 unfenced_lines fence toggle R4 checkBuildable H1 parity one predicate"`
