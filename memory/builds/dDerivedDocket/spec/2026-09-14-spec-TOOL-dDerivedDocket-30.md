# TOOL-dDerivedDocket-30 — checker defects from the stop census

**Status:** SPECCED · rev-3 · 2026-09-16 · node d · Tier-2 · base abac6d59 · streams tooling · order 30

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-14-build-TOOL-dDerivedDocket-1-design.md](../build/2026-09-14-build-TOOL-dDerivedDocket-1-design.md) | research | TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-14 TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1 |
| [2026-09-14-prompt-TOOL-dDerivedDocket-1-build-brief.md](../prompts/2026-09-14-prompt-TOOL-dDerivedDocket-1-build-brief.md) | journal | TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 TOOL-dDerivedDocket-37 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1 |
| [2026-09-14-prompt-TOOL-dDerivedDocket-1-spec-brief.md](../prompts/2026-09-14-prompt-TOOL-dDerivedDocket-1-spec-brief.md) | journal | TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-14 TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1 |
| [2026-09-14-review-TOOL-dDerivedDocket-21-spec-audit-g4-round1.md](../reviews/2026-09-14-review-TOOL-dDerivedDocket-21-spec-audit-g4-round1.md) | spec-audit | TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-31 |

<!-- /gen:spec-records -->

## 1. Goal

Three recorded unattended runs stopped on defects in the unattended kit's own gate leg, and all
three defects are still open at BASE. Check 23 reports a brief the driver staged as an undeclared
write, `check-unattended.sh --only 28` dies on an unbound variable, and the leg's conf allow-list is
a hand-typed key set nothing joins. Fix each, and gate the CLASS behind the second one: a flag a
parser accepts that no document names and no arm exercises is the one invocation nobody runs.

## 2. Scope (IN)

- **S1** Check 23 covers a committed path P, and stops reporting it, only when all three hold: the
  run-state file carries a `brief · item <unit> · reason <h12> P` row for THE unit whose pass commit
  is under test; P lies under the build's own `prompts/`; and P's blob at that commit starts with
  `<h12>`. Any other outside path is reported exactly as at BASE. This executes the owner ruling
  recorded as `TOOL-aLeakedHandle-7`, narrowed by DR's three conditions. Observed by AC1 and AC2.
- **S2** The conf import, the whole of check 1's block, moves above the `only28` guard, so every
  conf-read value is set whatever the scope. Under `--only 28` each numbered check after the 28
  region prints one announced skip naming itself on the leg's REPORT channel, and the list of those
  checks is derived from the file's own check headers rather than typed. Observed by AC3.
- **S3** The check-22 allow-list join. The keys the shipped `.unattended.conf.example` declares AND
  the leg's initialiser block initialises, minus the keys between the bare `gov:conf-allow-begin`
  and `gov:conf-allow-end` sentinels, must be empty. One direction only. Two `fail 22` branches: a
  missing, repeated or empty sentinel region, and a non-empty difference naming each key. The
  comment recording the join as withdrawn is replaced. Observed by AC4.
- **S4** Check 26 gains a flag arm. The parser population is every `--<name>` token on a
  non-comment line inside a new bare sentinel pair, `gov:argv-begin` and `gov:argv-end`, around the
  driver's top-level argument loop, sub-loops included, PLUS every member of `VERBS_SLUG` and
  `VERBS_INLINE`, read from their declarations, because a slug verb is recognised by set membership
  and never appears as a token inside the loop (§8 F5). The documented population is every
  `--<name>` token on the driver header's `#   unattended.sh` lines. A documented flag with no parser
  token fails 26, and so does a parser flag the header never names. Observed by AC5, AC6, AC7 and
  AC12.
- **S5** The driver header documents every flag the parser accepts. At BASE seven are parsed and
  undocumented — `--code`, `--framed`, `--playbook-sha`, `--records-root`, `--run`, `--set` and
  `--waive` — and `--framed` goes on the `--plan` header line beside `[--paths]`; any flag an earlier
  unit of this build added is graded the same way at this unit's commit. Observed by AC7 and AC12.
- **S6** Every argument a parser accepts appears in an arm. Check 26's flag arm also requires each
  driver parser flag on a non-comment line of `unattended.test.sh`, and each argument the leg's own
  scope parser accepts — every `--<name>` token on a non-comment line between the same bare pair,
  `gov:argv-begin` and `gov:argv-end`, placed around the `case "${1:-}"` block in
  `tools/unattended/check-unattended.sh` (`:85-90` at BASE) and extracted by the same exact-line
  match — on a non-comment line of `check-unattended.test.sh`. Where a suite is not installed, which
  is every adopter tree, the arm prints one announced skip naming the suite on the REPORT channel.
  The four arms missing at BASE are added: a `--version` smoke arm and a `--framed` arm in
  `unattended.test.sh`, and `--only 28` and `--skip 28` runs of the leg in
  `check-unattended.test.sh`. Observed by AC8 and AC13.
- **S7** Every new `fail` branch has an arm in `check-unattended.test.sh`, and `ARMS_FLOORS` in
  `.memory-tree.conf` moves in the same commit. The unattended suites run once, at the unit's end,
  under unit 1's attribution. Observed by AC9.
- **S8** The check 31 comment that justifies `${core:-}` and `${M:-}` by the crash this unit fixes
  is rewritten to say they are now belt and braces. Observed by AC10. NOT OBSERVED for the version:
  the unattended kit moves once in this build's landing range, in `TOOL-dDerivedDocket-1`, and this
  unit's bytes ride that move; `kit version markers` grades only the final tree's agreement.
- **S9** The kickoff manifest's `last-audit` is re-stamped in the same commit, with a delta line in
  the commit message, because `.memory-tree.conf` is in its `watch:` list and the staged leg refuses
  a watched change without one. The §B claims that file feeds are re-read first; only the
  `ARMS_FLOORS` figure moves, and no §B claim states that figure. Observed by AC11.

## 3. Non-goals (OUT)

- Check 23 stays report-only. It prints and does not fail at BASE, and turning the class into a
  gate is not in DR's scope for this unit.
- Check 23 recognising an ABSORB commit as a sanctioned out-of-set write is the inherited-red
  unit's work (DR 22.1, D12-i5), in the same block.
- No scoping of the leg to an arbitrary check. Checks 1 to 27 still share state, and the header's
  statement of that stays true.
- The reverse direction of the allow-list join. A key read through a default expansion, as
  `UNITS_REGION_CUTOFF` is at BASE, is initialised nowhere, so the reverse reds a correct tree.
- The verb carrier and the Skill do not join flags. They describe verbs, and at BASE most flags
  appear in neither, so a join there would red the tree for no finding a reader acts on.
- The unarmed branches already pinned in `memory/project/unarmed-branches.txt` stay pinned.

### Edges

- **consumes-from** `TOOL-dDerivedDocket-1` — `run-unattended-gates.sh --attribute`, whose attributed
  verdict, `verdict clean` with every inherited suite filed, is the only criterion the unattended
  suites can meet, since they are red at BASE for causes this unit does not own. Added by this spec;
  the brief's table does not list it.

## 4. Design

### Check 23 — what the three conditions buy

At BASE the subset test at `tools/unattended/check-unattended.sh:2344-2357` compares every path the
pass commit touched against the declared set, with only the run-state file excluded. The driver's
`--brief` verb STAGES the brief it records, so the pass commit carries it without the pass ever
having written it. Measured on the real tree with `--skip 28` on 2026-09-14 at BASE: 29 check 23
lines across two builds, every one naming a `prompts/` path, and five of them naming nothing else.
PINNED as that measurement; the arm's own fixture is what re-derives the behaviour.

Each condition closes a distinct over-exemption. Without the unit match, a pass could commit a
sibling unit's brief unreported. Without the directory condition, a row could name any path and
excuse it. Without the blob prefix, a pass that EDITED its brief after `--brief` hashed it would
have that edit excused, which is the write the declare-before-dispatch rule exists to see. The
blob comes from `git rev-parse <commit>:<P>`, read through the pinned `GIT` wrapper like every other
dereference in the leg, and compared with `<h12>` as a 12-character prefix.

A covered path is announced through the leg's `report` channel naming the brief row, so a reader
running with reports on can see why a path left the line.

### The hoist, and the announced skip

The import at `:147-199` and its initialiser block at `:116-121` sit inside
`if [ "$SCOPE" != only28 ]` at `:110`. Check 30 reads `$MEMORY_ROOT` at `:3224`, outside both scope
guards, so `--only 28` dies there with `set -u`. Re-measured on the real tree at BASE on 2026-09-14:
exit 1, `line 3224: MEMORY_ROOT: unbound variable`. Moving the conf presence test, the initialisers,
the subshell import and its sentinel test above the guard costs nothing on either scope: the import
is one subshell and it ran on every unscoped run already.

Under `--only 28` the checks after the 28 region are skipped because the flag's contract is "the 28
region alone", not because they would crash. Each prints
`check <n> skipped under --only 28 — this run asked for the 28 region alone` through `report`, the
channel `GOV_UNATTENDED_REPORT=1` turns on. That keeps the leg's header contract, exit 0 with no
output on a clean tree, true under both scopes. The numbers come from the `# ---- check <n>`
headers after the region's closing guard, so a check added later is skipped and announced without
anyone editing a list.

### Check 22's join

The sentinel region is extracted by an exact-line match on the two bare sentinels, and a region that
is absent, doubled or yields no key fails 22 by name. That refusal is the join's liveness: a region
that reads as empty would otherwise pass every key. The difference is computed with `comm` over three
sorted sets, in the idiom check 22's existing table join already uses at `:1664-1666`. The exact-line
match is what avoids the recorded first-draft trap, an anchored range whose pattern the extractor's
own source line matched, which read 38 keys instead of 20.

Re-measured at BASE: 33 keys in the example, 20 initialised, 20 in the allow-list, and the difference
is empty. Units of this build ordered before this one add conf keys, and this join grades every one
of them the moment it lands; a key one of them forgot to admit is fixed in this unit's commit.

### Check 26's flag arm

At BASE the driver's argument loop starts at `tools/unattended/unattended.sh:4936`, and the header
usage lines are `:5-22`. Measured at BASE on 2026-09-14 with the population rule of S4, PINNED as
that measurement:

- tokens `--<name>` on non-comment lines of the argument loop (`:4936` `while [ $# -gt 0 ]; do` to
  `:5034` `done`): 30; members of `VERBS_SLUG` and `VERBS_INLINE` (`:87-90`): 18; union: 44.
  Header `#   unattended.sh` lines (`:5-22`): 37 tokens.
- loop tokens alone against the header: 14 header tokens have no loop token — `--abort`,
  `--attest`, `--brief`, `--close`, `--dispatch`, `--landed`, `--park`, `--preflight`, `--propose`,
  `--record-piece`, `--record-set`, `--rescope`, `--resume` and `--status`, every slug verb but
  `--review` — because they dispatch by `VERBS_SLUG` membership through `is_slug_verb` (`:92`) in
  the loop's catch-all arm.
- the union against the header: no header token is missing; 7 parser tokens are undocumented —
  `--code`, `--framed`, `--playbook-sha`, `--records-root`, `--run`, `--set` and `--waive`.
- suite halves: `--framed` and `--version` appear on no non-comment line of `unattended.test.sh`;
  `--only` and `--skip` appear on no non-comment line of `check-unattended.test.sh`.

```bash
awk 'NR>=4936 && NR<=5034 && $0 !~ /^[[:space:]]*#/' tools/unattended/unattended.sh | grep -oE -- '--[a-z][a-z0-9-]*'
grep -E '^VERBS_(SLUG|INLINE)=' tools/unattended/unattended.sh | grep -oE -- '--[a-z][a-z0-9-]*'
awk 'NR>=5 && NR<=22' tools/unattended/unattended.sh | grep -E '^#   unattended\.sh' | grep -oE -- '--[a-z][a-z0-9-]*'
```

The line numbers are BASE's; after S4 the loop is read between its sentinels. Every one of the seven
is a real argument of a documented verb. S5 adds each to its verb's header line, which also puts it
in the rendered usage text. `--witness`, `--paths` and `--framed` are parsed inside the `--phase` and
`--plan` arms rather than as case labels, which is why the population is tokens in the fenced region
and not case labels alone.

The suite half measures `--version` and `--framed` as the two driver flags no non-comment line of
`unattended.test.sh` names, and `--only` and `--skip` as the two leg flags no non-comment line of
`check-unattended.test.sh` names; all four are added. The arm grades PRESENCE on a non-comment line
and says so in its header: it cannot tell an arm that asserts something about a flag from one that
merely passes it.

### Inventory

| Identifier | Kind | Cell |
|---|---|---|
| `gov:argv-begin`, `gov:argv-end` | bare sentinel comments in the driver AND in the leg, around each file's own argument parser | none; bare so no extractor line can match them |
| new `fail 22` and `fail 26` branches | leg refusals | `harness arms` population; each is armed or the floor does not move |
| any new shell helper | shell function | lexicon `sh` function cell; each name passes `python tools/lexicon/lexicon.py --suggest <name>` before it is written |

### Files touched (estimate)

`tools/unattended/check-unattended.sh` · `tools/unattended/check-unattended.test.sh` ·
`tools/unattended/unattended.sh` · `tools/unattended/unattended.test.sh` · `.memory-tree.conf`
(`ARMS_FLOORS`) · `memory/guides/SESSION-KICKOFF.md` (the stamp) · `memory/map/features/unattended.md`
prose.

### Alternatives rejected

- **`${MEMORY_ROOT:-}` at check 30.** Costed in `TOOL-aHoistedPass-37`: it trades the crash for a
  silent skip of check 30's corpus walk, which removes the liveness assertion that check exists for.
- **Exempting all of `prompts/` in check 23.** DR names it as the break: a sibling's brief and an
  edited brief would both vanish.
- **Pinning the two check-22 branches as unarmed.** `TOOL-aHoistedPass-40` weighed it and the drift
  audit already reports that registry as not shrinking; this unit may run the suite, so the reason
  that forced the pin is gone.
- **Joining flags to the verb carrier.** Rejected in §3.

## 5. Production-readiness checklist

- security — the leg reads more of the driver and its suites and writes nothing. The hoist moves the
  subshell import unchanged, so a hostile conf still cannot end or take over the leg.
- perf / scale — one extra read of the driver and of two suites per run; `--only 28` becomes usable,
  which is the saving the flag was written for.
- error / empty / loading states — an absent sentinel region fails by name, an absent suite is an
  announced skip, and a brief row with a malformed hash does not cover anything.
- observability — the per-check skip lines under `--only 28`, the covered-brief report line, and the
  key and flag names in every new refusal.
- risks — the header gains seven flags, which changes the rendered usage text; nothing parses that
  text except check 26 itself.
- testing — arms in `tools/unattended/check-unattended.test.sh` for each new branch and each staged
  break in §6, run once at the unit's end under `--attribute`.
- migration — adopters receive the hoist and the new arms with their next kit upgrade, and the suite
  half skips in their trees because the suites are withheld from them.
- user docs — the header lines are the usage text; the leg's own block comments are the rest.

## 6. Acceptance criteria

- **AC1** — When a fixture pass commit carries its own unit's brief under `prompts/` and a matching
  `brief · item` row, check 23 in `tools/unattended/check-unattended.test.sh` prints no line for it;
  when the brief was edited after hashing, or the row names a sibling unit, the line is printed.
  Red when: the exemption covers all of `prompts/`, and the edited brief goes unreported.
- **AC2** — When `bash tools/unattended/check-unattended.sh --skip 28` runs on the real tree, no
  check 23 line names a brief whose row, directory and blob all match.
  Red when: the blob is read from the working tree instead of the pass commit, so a brief edited
  and committed later still matches.
  figure: the 29 lines and the five brief-only ones in §4 are PINNED 2026-09-14 at BASE; this
  criterion states the property, not a count.
- **AC3** — When `GOV_UNATTENDED_REPORT=1 bash tools/unattended/check-unattended.sh --only 28` runs
  on the real tree, it exits 0 and prints one skip line each for checks 30 and 31; without the
  variable it exits 0 and prints nothing.
  Red when: the conf read stays inside the guard, and the run exits 1 on
  `MEMORY_ROOT: unbound variable`.
- **AC4** — When a fixture copy of the leg removes one key from between the `gov:conf-allow`
  sentinels, the leg fails 22 naming that key; with one sentinel deleted, it fails 22 naming the
  region.
  Red when: the region is extracted by a pattern the extractor's own source line matches, which
  reads keys from outside the list and hides the removal.
- **AC5** — When a fixture copy of the driver documents `--frobnicate` on a header line with no parser
  token, the leg fails 26 naming `--frobnicate`.
  Red when: the flag arm reads only case labels, so a documented flag parsed nowhere is not missed.
- **AC6** — When a fixture copy of the driver adds a parser arm `--frobnicate)` that no header line
  names, the leg fails 26 naming it.
  Red when: the arm joins one direction only, and an undocumented flag reaches no reader.
- **AC7** — When `bash tools/unattended/check-unattended.sh` runs on the real tree after this unit,
  the flag arm passes with every parser flag, the seven §4 names included, on its verb's header line,
  and with every slug verb found through `VERBS_SLUG`.
  Red when: the header is left as at BASE, which the new arm reds seven times, or the population
  reads the loop alone, which reds fourteen documented slug verbs.
- **AC8** — When a fixture copy of `unattended.test.sh` drops every line naming `--version`, the leg
  fails 26 naming it; with the suite absent, the leg's REPORT channel carries one skip line naming
  the suite and the exit status is the other checks' verdict; and when a fixture copy of
  `unattended.test.sh` drops every line naming `--framed`, the leg fails 26 naming it.
  Red when: an absent suite is read as an empty one and reds every flag in an adopter tree.
- **AC9** — When `bash tools/unattended/run-unattended-gates.sh --attribute <BASE>` runs once at the
  unit's end, its attribution summary reads `verdict clean`, meaning no NEW FAIL, no
  `DEAD PROBE at L` and no `OVER BUDGET at L`. Every suite it reports with INHERITED lines or
  `DEAD PROBE at R` is named by its file path in a filed backlog row or ask that is not CLOSED, as
  `git grep -n '<suite file>' -- memory/backlog 'memory/builds/*/BACKLOG.md'` shows. And
  `python3 tools/memory-tree/check-arms.py --check` passes with the moved `ARMS_FLOORS` row.
  Red when: a new branch ships with no arm, so the harness arms leg reds on the floor; or an arm this
  unit added fails, or an existing arm newly fails because of it; or the attributed run is read by
  its NEW count alone, so a suite this unit's change aborted before its first FAIL line, or pushed
  past its budget, reads as clean; or an inherited failure is attributed away with no record filing
  it.
  cost: the unattended suites' declared budgets, once, with the BASE side cached.
  permission: D12-i8 lifts the do-not-run instruction for this unit.
- **AC10** — When `grep -n 'belt and braces' tools/unattended/check-unattended.sh` runs after this
  unit, the check 31 comment names `${core:-}` and `${M:-}` as belt and braces and no longer gives
  the `--only 28` crash as their reason.
  Red when: the comment still justifies them by a crash that no longer happens, so a reader keeps
  two guards for a reason that is false.
- **AC11** — When `bash skills/session-kickoff/manifest-check.sh` runs on the unit's commit, check 5
  passes with the re-stamped `last-audit`.
  Red when: the conf moves with no re-stamp, which the staged leg refuses at the commit.
- **AC12** — When a fixture copy of the driver keeps a slug verb's header line but drops the verb
  from `VERBS_SLUG`, the leg fails 26 naming it; with the verb restored to the set and no case label
  anywhere, the leg passes.
  Red when: the parser population is the loop's case labels alone, so a verb the set dispatches
  reads as undocumented-parser or missing-parser by accident.
- **AC13** — When a fixture copy of `check-unattended.test.sh` drops every line naming `--skip`, the
  leg fails 26 naming `--skip`; with the leg's `gov:argv-begin` sentinel deleted, it fails 26 naming
  the region.
  Red when: the leg half has no fenced population, so an implementation grading only the driver half
  passes every other criterion.

## 7. Gates

`unattended kit gate` · `harness arms (fail branches armed or pinned)` · `kit version markers` · `shell hygiene (a loop fed by a command substitution)` · `lexicon naming predicates` · `line length` · `codebase-map coverage + freshness` · `kickoff-manifest ratchet` · `memory hygiene`

New arm: `tools/unattended/check-unattended.test.sh` · an edited brief, a sibling's brief, and a matching brief in a fixture pass commit · the check-unattended arms floor
New arm: `tools/unattended/check-unattended.test.sh` · a removed allow-list key, a deleted sentinel, a documented flag with no parser token, a parser flag with no header line, a suite missing `--version` · `ARMS_FLOORS` for `tools/unattended/check-unattended.sh`
New arm: `tools/unattended/check-unattended.test.sh` · the leg run with `--only 28` · none
New arm: `tools/unattended/unattended.test.sh` · the driver run with `--version` · none
New arm: `tools/unattended/unattended.test.sh` · the driver run with `--plan --framed` · none
New arm: `tools/unattended/check-unattended.test.sh` · the leg run with `--skip 28` · none

## 8. Open questions

- **F1** — Which direction does the flag join grade? Options: (a) documented to parser, DR's third
  criterion; (b) both. (b) reds seven flags at BASE, which S5 documents in the same commit.
  RESOLVED (agent, 2026-09-14, delegated): (b). It satisfies DR's criterion and also catches the
  flag nobody can read about, at the cost of seven header edits.
- **F2** — Where does the suite-arm class gate live? Options: (a) inside each suite, asserting its own
  coverage; (b) in the leg's check 26, with an announced skip where a suite is absent. (a) runs only
  when the suite runs, and the unattended suites are on no bar, so it would be a gate nobody runs.
  RESOLVED (agent, 2026-09-14, delegated): (b).
- **F3** — One skip line, or one per check, under `--only 28`? RESOLVED (agent, 2026-09-14,
  delegated): one per check, derived from the check headers, because a skip whose subject is a set
  cannot say which check it was about; check 31's header states the same rule.
- **F4** — Does check 23's exemption read the brief's blob from the working tree or from the pass
  commit? RESOLVED (agent, 2026-09-14, delegated): from the pass commit, since the question is what
  that commit wrote.
- **F5 — how does the flag arm see verbs dispatched by set membership?** Options: (a) the parser
  population includes the `VERBS_SLUG` and `VERBS_INLINE` members, read from their declarations; (b) a
  second fence around the post-loop `case "$VERB"` dispatch. The driver states that the set is the
  dispatch, and check 26's verb join already reads it. RESOLVED (agent, 2026-09-14, delegated): (a).

## 9. Revision log

- rev-1 · 2026-09-14 · initial draft. Adds one edge the brief's table does not list,
  consumes-from unit 1, for the attributed suite run.
- rev-2 · 2026-09-14 · folds the round-1 spec audit (G4 H6, M23, M7; G1 M11). H6: S4's parser
  population adds the `VERBS_SLUG` and `VERBS_INLINE` members (F5, AC12); seven flags are
  undocumented at BASE, not six, `--framed` among them, and the probe and its BASE output, re-run by
  the fold, are in §4 (S5, AC7, and F1's count); `--framed` and `--skip` gain arms (S6, AC8). M23:
  S6 fences the leg's own scope parser with the same sentinel pair (AC13). M7 with G1 M11: S8's
  version half is a pointer to unit 1 under the build's one-owner rule, and AC10 now observes the
  check 31 comment S8 rewrites.
- rev-3 · 2026-09-16 · spec-audit round 2 fold, second pass. Plan c1 E41, G1 H1 (2, 24), a sibling
  fold from the G1 round-2 record: §6 AC9 reads unit 1's `verdict clean` and the inherited-suite
  filing, and the §3 consumes-from edge to unit 1 is updated. Fold verification: §6 AC3's `Red when:`
  code span, which opened on one line and closed on the next, is reflowed onto one line; the words
  are unchanged. Third pass, from the fold-2 verifier problem that §6 AC9's `Red when:` carried only
  the shorter consumer clause: AC9 now also reds when an arm this unit added fails or an existing arm
  newly fails, when a suite is pushed past its budget, and when an inherited failure is attributed
  away with no record filing it, so each positive clause of unit 1 S10's criterion has a red, as
  units 16, 17 and 18 state them.

## 10. Reuse audit

Every seam is in the leg or its driver. The subshell conf import and its bare sentinel pair already
exist at `tools/unattended/check-unattended.sh:147-199`; S3 reads the pair it was fenced for, and S4
copies that fence for the argument loop. Check 22's `comm` join at `:1664-1666` is the idiom for S3.
Check 26's verb join at `:2473-2532`, which reads each carrier once into memory, is the loop S4
extends. Check 31's one-announced-skip-per-subject pattern is S2's and S6's. The driver's
`--brief` row grammar, `brief · item <unit> · reason <h12> <path>` from `verb_brief`, is what S1
matches, exactly as written. `python tools/codebase-map/reuse_lookup.py "join every flag a
command-line parser accepts against its documented usage and its test arms"` returned only
Python parser neighbours such as `parse_args` in `tools/govkit/govkit.py`, and reports `.sh` as an
unscanned layer; no existing seam joins a shell parser's flags to anything. Recall returned
`TOOL-aHoistedPass-37` and `TOOL-aHoistedPass-40`, which carry the costed options for S2 and S3, and
the owner ruling `TOOL-aLeakedHandle-7`, which S1 executes.

Where DR, the records and the source disagree at BASE: DR cites check 23 at `:2347-2357`, and the
subset test spans `:2344-2357`. The owner ruling excludes "the path a brief row names", and DR
narrows that with three conditions. S1 follows DR, because each case the narrowing removes, an
edited brief or a sibling's, is one the ruling's own reason does not reach: in both, the committed
bytes are not what `--brief` staged for this pass. `TOOL-aHoistedPass-40` names the two check-22 branches only by shape, so S3
defines them.

Recall terms used: `check-unattended conf-allow sentinel allow-list check 22 only28 MEMORY_ROOT
unbound check 23 brief prompts dispatch`
