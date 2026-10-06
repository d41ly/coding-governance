# TOOL-aGraftedHelix-30 — a verb grades `authorization-reachable` alone, and every reconciling merge runs it before the run spends more

**Status:** CLOSED · rev-1 · 2026-10-05 · node a · Tier-2 · base 018b5675 · streams tooling · order 14 · ratified 2026-10-05

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-04-build-TOOL-aGraftedHelix-30-1-acceptance-ledger.md](../build/2026-10-04-build-TOOL-aGraftedHelix-30-1-acceptance-ledger.md) | journal | — |
| [2026-10-06-build-TOOL-aGraftedHelix-29-runlog-b9bb22c3.md](../build/2026-10-06-build-TOOL-aGraftedHelix-29-runlog-b9bb22c3.md) | journal | TOOL-aGraftedHelix-29 TOOL-aGraftedHelix-31 TOOL-aGraftedHelix-32 TOOL-aGraftedHelix-33 TOOL-aGraftedHelix-34 TOOL-aGraftedHelix-35 TOOL-aGraftedHelix-36 TOOL-aGraftedHelix-37 TOOL-aGraftedHelix-38 TOOL-aGraftedHelix-39 TOOL-aGraftedHelix-40 TOOL-aGraftedHelix-41 |
| [2026-10-05-prompt-TOOL-aGraftedHelix-29-1-spec-brief.md](../prompts/2026-10-05-prompt-TOOL-aGraftedHelix-29-1-spec-brief.md) | journal | TOOL-aGraftedHelix-29 TOOL-aGraftedHelix-31 TOOL-aGraftedHelix-32 |
| [2026-10-06-review-TOOL-aGraftedHelix-29-closing-diff-round1.md](../reviews/2026-10-06-review-TOOL-aGraftedHelix-29-closing-diff-round1.md) | diff-review | TOOL-aGraftedHelix-29 TOOL-aGraftedHelix-31 TOOL-aGraftedHelix-32 TOOL-aGraftedHelix-33 TOOL-aGraftedHelix-34 |

<!-- /gen:spec-records -->

## 1. Goal

A mid-build merge of `origin/main` brought check 89 into this run's driver, and check 89 refuses the
run's own BASE README. Nothing graded `authorization-reachable` again until `--close`, where it takes
no override and the BASE blob cannot change, so the run built for nine more hours before it had to
rotate. This unit gives the driver a read-only verb that grades that one item with the arm `--close`
uses, and puts it on both reconciling paths: after a mid-run merge of the remote's default branch,
and between the lander's `--prepare` and `--close`. A refusal names the two exits a run has. A class
record carries the shape to every checklist over a merge that touches the driver.

## 2. Scope (IN)

- **S1** — `--authorization <slug>` is a slug verb of `tools/unattended/unattended.sh`: a member of
  `VERBS_SLUG`, one `#   unattended.sh --authorization` header line, and one dispatch arm calling
  `print_authorization`. Observed by AC1 and AC5.
- **S2** — `print_authorization` refuses first what needs no network: a malformed slug, an absent
  run-state file and a terminal record, through `check_slug`, check 10 and `refuse_if_terminal` as
  `--close` does. It then calls `observe_anchor`, clears `TB`, and calls
  `dod_met "$slug" "$rel" authorization-reachable machine`, which is the only grading it does. Met
  prints one `authorization-reachable — met` line and exits 0. Unmet with `TB` set means the README
  read at a derived BASE refused, so it prints one line naming both exits of §4 and exits 1, setting
  the status itself when no refusing check did. No anchor observed, or unmet with `TB` empty, means
  the predicate never reached the README, so it prints one `not evaluated` line, no exits, and sets
  the status to 2. Observed by AC1, AC2, AC3 and AC4.
- **S3** — The verb writes nothing to the working tree, the index, the run-state file or the remote.
  The run log START and END lines every verb writes under the git dir are the only bytes it adds.
  Observed by AC1, AC2 and AC10.
- **S4** — `print_authorization` carries a header comment saying what it does not check: the other
  Definition-of-Done items, and whether the merge is what changed the answer. NOT OBSERVED — it is
  prose, and no check reads a comment for its meaning.
- **S5** — `tools/unattended/SKILL.template.md` runs the verb on both reconciling paths. The
  in-place block puts `--authorization <slug>` between `--prepare` and `--close`. The reconcile
  paragraph says to run it after any merge of the remote's default branch into the run branch, mid-
  build included, before the next pass. The rendered Skill is re-adopted. Observed by AC5 and AC6.
- **S6** — `tools/unattended/VERBS.template.md` gains one `--authorization` entry, and its render
  under `memory/guides/` is re-adopted byte-identical (§8 F2). Observed by AC5 and AC7.
- **S7** — One `kind: class` record under `memory/gotchas/`, named
  a-merged-in-check-can-refuse-a-pinned-record, with `universal: false`. Its basename is a new map
  key in the unattended-mandate dossier, and the catalogue index and the map are re-rendered.
  Observed by AC9.
- **S8** — Four arms in the driver's self-test: met with nothing written and the absent record,
  refused with both exits, not evaluated, and a source arm on `print_authorization`'s body.
  Observed by AC1 to AC4.
- **S9** — The unattended kit version, bumped once after the last move in every carrier
  `tools/check-kit-versions.sh` enumerates. The protocol and stops templates move their line 1 and
  nothing else. Observed by AC7 and AC8.

## 3. Non-goals (OUT)

- No change to `--close`, to `dod_met`, to `DOD_CORE` or to the order the close grades its items
  (§8 F1). A close whose authorization item is unmet still grades every other item, as today.
- No change to `tools/push-main.sh`. It is a flat kit that reaches no sibling program today (§8 F1).
- No change to the content of the protocol or stops templates. Their reconcile sentences stay true
  once the Skill runs the verb (§8 F2).
- No new conf key, gate leg, numbered check or kit file. The refusals the verb prints are the ones
  `observe_anchor`, `trusted_base` and `check_authorization` already number.
- No exits line on `--close`'s own unmet branch. Check 21 already names `--abort` when an override
  is tried, and the close's remedy print is suppressed for the non-overridable set on purpose.
- No gate that observes a run running the verb after a merge. The run log that would show it is
  machine-local and untracked, so the class record says it has no machine gate.
- No automatic trigger at the merge itself. A git hook cannot run the predicate (§4).

### Edges

none

## 4. Design

### The defect, measured

Measured on node `a`, 2026-10-05, at `9024901c` on the run branch. PINNED.

| reading | value |
|---|---|
| lines holding `fail 89 ` in the driver at `909c5e0b9^1` | 0 |
| the same at `909c5e0b9`, the mid-build merge of origin/main at cfa2cc45 | 2 |
| `SPEC_AUDIT_ASK_RE=` at `5212726a8^1`, then at the second reconciling merge `5212726a8` | 0, then 1 |
| front matter of the build README at the old BASE `5266d22e` | `authorized-by: prompt` and `spec-audit: 2026-10-04` |
| first-parent commits from `909c5e0b9` to the rotation abort `6707c4b10` | 73, from 10:36 to 19:43 +0300 |
| live run-state files whose BASE README carries `spec-audit:` under a non-slug mode | 0 of the 17 whose recorded phase is neither LANDED nor ABORTED |

The last row is the predicate's check-89 half run over the real tree. Its one near-miss is this
build's archived record, `memory/builds/aGraftedHelix/RUN.ABORTED.6410435d.md`, whose base
`5266d22e` carries the key. The live record's base `018b5675` does not, so the verb reads met on the
live run (AC10).

`--close` grades `DOD_CORE` in declared order, and `gates-green` is first
(`tools/unattended/unattended.sh:690`). The authorization item is third, so a close over a refused
record pays the full bar before it reads the refusal.

### The verb

`print_authorization` is a sibling of `--abort`'s use of `dod_met`, which grades two items alone at
`tools/unattended/unattended.sh:5459`. The arm it calls is the one `--close` calls at `:9089`:

```bash
[ -n "$ASHA" ] && trusted_base "$rel" && check_authorization "$slug" "$TB"
```

So the verb answers what `--close` would answer from the same tree: same anchor observation, same
derived BASE, same front-matter parse, same refusals. It passes no `allow-degenerate`, which
`run_takeover` passes and `--close` does not. A record whose BASE equals HEAD therefore prints check
16's "built nothing" refusal, as the close does. A reconciling merge always moves HEAD, so the
verb's own path never meets that state.

No output is redirected. `TOOL-aBoundedVerdict-12` records the defect a redirect on this `&&` chain
caused: it silenced `check_authorization`'s refusals while `trusted_base`'s still printed.

The dispatcher exits with `$status` (`:12391`), so the verb sets its exit through that variable.

Two kinds of refusal reach the arm, and only one of them is about the record. `trusted_base` refuses
when it cannot derive a BASE: checks 30 to 33 when the run branch's tip is unpublished, unfetched or
unreachable (`emit_branch_fail`, `:2205`), and checks 16 and 18 over the recorded base.
`check_authorization` refuses the README read at a derived BASE, which is the bytes a run cannot
change. `trusted_base` clears `TB` on entry and sets it only on success (`:2299`), so after the arm
a set `TB` says the README was read. The verb reads that global and calls nothing else, so it is
still one predicate with one spelling. Naming rotation over a branch the clone has not fetched, or
has not pushed, would send a run to abort over a state one git command clears.

The absent-record refusal is a new call site of check 10, worded for this verb as `--close`'s is for
its own, so the harness-arms leg asks for an arm on its literal; AC1 is that arm.

| outcome | stdout | exit |
|---|---|---|
| a malformed slug, no run-state file, a terminal record | the existing numbered refusal | 1 |
| no anchor observed | `observe_anchor`'s numbered refusal, then one line holding `not evaluated` | 2 |
| unmet with `TB` empty | `trusted_base`'s numbered refusal, which names its remedy, then the same line | 2 |
| met | one line holding `authorization-reachable — met`, the BASE and the observed anchor | 0 |
| unmet with `TB` set | `check_authorization`'s numbered refusal, then one line naming both exits | 1 |

### The exits a refusal names

The line opens by saying `--close` will refuse this run too, with no override, while the refusal
above stands; a refusal whose own text names a working-tree remedy is answered by that remedy first.
Then:

- **Rotate.** Commit a build README this driver admits, then
  `--abort <slug> --code repo-state-out-of-mandate --reason <text>`, then
  `--preflight <slug> --keepalive-id <id>` onto the new BASE. This build took this exit.
- **Hand off.** `--park <slug> --item <the question> --reason <text>`, then
  `--handoff <slug> --code owner-decision --reason <text> --reaped <id>`.
- A slug-mode README is the owner's, so there only the hand-off is the run's to take.

`owner-landing` is not offered. `check_handoff_bar` (`:8757`) admits it only on a `gates-run` fact
or an inherited-red record, and `--close` writes neither unless every item is met, so with this item
unmet it is check 83's refusal. `--park` writes a `decision` row, which is what `owner-decision`
requires. `repo-state-out-of-mandate` is in `HALT_CODES_HANDOFF`, so the abort itself prints the
`HANDOFF_CUTOFF` notice from `print_abort_notice` at the moment of the act (§8 F3).

### The two reconciling paths

**The landing.** Under `in-place` the Skill's block is `--prepare`, then `--close`, and it forbids a
second move between them because a move stages the record. The verb stages nothing, so the block
becomes three lines with `--authorization <slug>` in the middle. A refusal there ends the landing
before the bar runs.

**The mid-run merge.** The Skill's reconcile paragraph, at `tools/unattended/SKILL.template.md:1193`,
tells a run to merge the remote's default branch into the run branch when `--prepare` conflicts. One
added sentence makes the verb the next act after ANY such merge, mid-build included, before the next
pass and before `--prepare` again. The driver the verb runs is the work tree's, which after the merge
commit is the merged one.

### The carriers

The Skill template is not a governance carrier (unit 1, §8 F7). The verbs template is half of the
protocol, and check 26 of the kit gate refuses a declared verb with no entry there. Its entry says
what the verb grades, its three outcomes and their exits, that it writes nothing, and when to run it.
The stops template's §10 and the protocol's §6 already say to reconcile from the remote onto the run
branch and then `--prepare` again, which stays true, so they move their version line alone (§8 F2).

### The class record

Sections as in `memory/gotchas/inherited-git-dir-pins-the-work-tree-to-the-cwd.md`: Symptom, Why,
Where it bit, What to do, Its gate, and What this does NOT say. The class: a merge of the remote's
default branch brings in a check, or narrows one, that the running record cannot satisfy because
the bytes it grades are pinned at BASE. Nothing grades it until the verb that owns the check, and
for a non-overridable item the only exits are rotation and hand-off.

Where it bit is the table above, citing `TOOL-aWardedAudit-4` and `TOOL-aEvidencedLens-22` as the
rulings check 89 enforces, and this unit. What to do names the verb and the two Skill sentences. Its
gate: the verb is **gated by** the four arms S8 adds; the class has **no machine gate**, because the
run log is machine-local. It is a documented check: a reviewer of a reconciling merge that touches
the driver asks whether the verb was run.

Its anchors are `tools/unattended/unattended.sh`, `tools/unattended/SKILL.template.md`,
`tools/push-main.sh` and `.unattended.conf`, so `gotchas.py --for-diff` over a merge that touches the
driver selects it. Check 27 obliges the record to answer its nearest existing record. The pass runs
it and names the hit, or writes `coexists-with`, before committing.

### Inventory

| identifier | where | cell |
|---|---|---|
| `--authorization` | `VERBS_SLUG`, the header and the dispatch | a driver verb, no lexicon cell |
| `print_authorization` | `tools/unattended/unattended.sh` | `sh.function` |
| `a-merged-in-check-can-refuse-a-pinned-record.md` | `memory/gotchas/` | map key, `gotcha-classes` |
| four arms | the driver's self-test | n/a |

`python tools/lexicon/lexicon.py --suggest print_authorization --as sh.function` answered OK on
2026-10-05. The record's basename is the one new map key. It belongs in the unattended-mandate
dossier, which is about what authorizes a run, and that dossier is 8330 bytes today. No conf key,
leg, check number or kit file is minted.

### Files touched (estimate)

- `tools/unattended/unattended.sh`
- `tools/unattended/unattended.test.sh`
- `tools/unattended/VERBS.template.md`
- `tools/unattended/SKILL.template.md`
- `tools/unattended/PROTOCOL.template.md`
- `tools/unattended/STOPS.template.md`
- `tools/unattended/README.md`
- `tools/unattended/check-unattended.sh`
- `tools/unattended/check-pass-order.sh`
- `tools/unattended/check-brief-recorded.sh`
- `memory/guides/UNATTENDED-VERBS.md`
- `memory/guides/UNATTENDED-PROTOCOL.md`
- `memory/guides/UNATTENDED-STOPS.md`
- `.claude/skills/unattended/SKILL.md`
- `memory/gotchas/INDEX.md`
- `memory/map/features/unattended-mandate.md`
- `memory/map/generated/`

The version bump moves the marker on every carrier `tools/check-kit-versions.sh` enumerates. The
class record is one new file under `memory/gotchas/`.

### Rollout

1. Write the four arms first. Observe the refused arm red against the driver at the pass's parent,
   where the verb is check 14's unknown argument.
2. Add the verb: the `VERBS_SLUG` member, the header line, the dispatch arm and
   `print_authorization`. Re-run the four arms as slices. Observe the source arm red on a staged copy
   that inlines the chain, and the not-evaluated arm red on a staged copy without its branch.
3. Edit the Skill and verbs templates, then run `bash tools/unattended/adopt-unattended.sh`.
4. Write the class record, add its basename to the dossier, then run `gotchas.py --write` and
   `gen_map.py --write`.
5. Bump the unattended version once, last, in every carrier, and re-adopt.
6. Make AC10's observation on this run's own record, then commit through the hook.

### Alternatives rejected

Each was tested on node `a`, 2026-10-05, by a probe that reads.

- **The lander invokes the driver after its merge.** `grep` finds one mention of the driver in
  `tools/push-main.sh`, a comment at `:228`, and no invocation of any sibling kit's program. Reaching
  one needs the `resolve_kit_dir` inline block and a python resolver in a flat kit that ships to
  repositories with no unattended kit. The in-place block already puts a driver verb right after the
  prepare, so the lander gains nothing the Skill line does not give.
- **`--close` grades the item before its bar and stops.** The suite pins the opposite: with the item
  unmet, the close still grades every item and prints `specs-audited — not gradable`, at
  `tools/unattended/unattended.test.sh:3814-3826`, `:7764-7775` and `:7890-7906`. A pre-loop
  refusal reds those arms and drops the close's report of every unmet item at once.
  `TOOL-aGradedMandate-13` records why that item's close path is not changed without a further
  review: a wrong refusal there cannot be cleared.
- **A git hook runs the predicate at every merge commit.** `observe_anchor` refuses check 22 when
  `GIT_DIR` is set (`tools/unattended/unattended.sh:1695-1700`), and git exports `GIT_DIR` into a
  linked worktree's hooks, measured by unit 27. Under a hook the predicate refuses before reading
  anything, and scrubbing the variable blinds the tripwire.
- **`--dispatch` grades it at every pass.** BUILD-METHOD M6 says `--dispatch` refuses "on a MISSING
  or THIN unit and on nothing else", and shared invariant 10 bars every unit from editing that file.
  It would also add a remote round trip to every pass and refuse a pass made offline.
- **The holder's `--resume`, which the idle-wake runs every tick.** Its verbs entry would need a
  content edit, it fires on a ten-minute tick rather than at the merge, and it adds a remote round
  trip to every tick.
- **A flag on an existing verb.** `--status` is the one-line, no-network read every reground starts
  with (BUILD-METHOD M7). A remote round trip and a refusal there change the cost of every reground,
  and the verbs entry would still be silent on the behaviour.

## 5. Production-readiness checklist

- security — No new write path. The verb reads, and inherits check 22's injected-config tripwire from
  `observe_anchor`. The exits line spells no bypass flag.
- perf / scale — PINNED on node `a`, 2026-10-05: `git ls-remote --symref origin HEAD` took 661 to
  856 ms over three reads. A driver load is about 1.16 s, per the driver's own `--plan` comment. The
  verb runs once per reconciling merge and once per landing.
- error / empty / loading states — The five rows of the outcome table. A clone missing the tip the
  remote advertises is check 30's refusal, which says to fetch and re-run, and reads not evaluated.
- observability — The met, refused and not-evaluated lines, and the run log's START and END lines.
- risks — The trigger is an instruction. A run that skips the verb meets the refusal at `--close`
  after the bar, which is today's behaviour, and the class record reaches the checklist over any
  merge that touches the driver.
- testing — Four arms in the driver's self-test, each observed red on a staged break. AC10 reads
  the live run.
- migration — None. No record, conf or verb changes meaning.
- user docs — N/A for a `help/` page: gov keeps none. The verbs entry and the two Skill sentences
  are the documentation.

## 6. Acceptance criteria

- **AC1** — When the met arm runs as a slice of the driver's self-test, its prologue and the
  borrowed-record fixture block in a temp script inside the kit dir, `run --authorization tBr2`
  prints a line holding `authorization-reachable — met`, and the call's status is 0. Before and
  after the call, `git status --porcelain` prints nothing, `git hash-object` of the fixture's
  run-state file prints one sha, and `git ls-remote origin` prints the same lines. On a slug with no
  run-state file the verb prints check 10's refusal, and its status is 1.
  Red when: the met record exits non-zero, any of the three reads differs after the call, or the
  absent record passes silently.
  fixture: the block that preflights a prompt-mode README with no key and borrows its record.
- **AC2** — When the refused arm runs in that slice, `run --authorization tBr` prints the check 89
  refusal holding `mode prompt; delete the line` and then one line holding both
  `--abort tBr --code repo-state-out-of-mandate` and `--handoff tBr --code owner-decision`. Its
  status is 1, and the three reads of AC1 are unchanged by the call. Run first against the driver
  at the pass's parent, the same call prints check 14's unknown-argument refusal.
  Red when: the record reads met, the exits line is missing or offers `owner-landing`, or the call
  writes anything.
- **AC3** — When `run --close tBr` and `run --authorization tBr` run in that slice, the check 89
  line each prints is byte-identical. `print_authorization`'s body, cut from the driver between its
  opening line and the next column-0 brace, holds on its non-comment lines one `dod_met` call naming
  `authorization-reachable` and no call of `check_authorization` or `trusted_base`. With the body
  edited in a staged copy to call those two directly, the source arm fails.
  Red when: the verb carries its own copy of the chain, or the two verbs print different refusals.
- **AC4** — When origin's URL is pointed at a path that does not exist in that slice,
  `run --authorization tBr2` prints the anchor's numbered refusal and a line holding
  `not evaluated`, prints no line naming `--handoff`, and its status is 2. With the URL restored and
  the run branch deleted from origin, the same call prints the base derivation's numbered refusal,
  the same line and no exits, with status 2. With the branch pushed again, AC1's answer returns.
  Red when: an unanswered remote or an unpublished branch reads as met, or as a refusal of the record
  with status 1 or the exits printed.
- **AC5** — When `grep -nF -e '--authorization'` runs over `tools/unattended/unattended.sh`,
  `tools/unattended/VERBS.template.md` and `tools/unattended/SKILL.template.md`, it prints the
  `VERBS_SLUG` line, one header line opening `#   unattended.sh --authorization`, the dispatch arm,
  one verbs-carrier entry line opening with the verb in code quotes and an em dash, and at least two
  Skill lines invoking `unattended.sh --authorization <slug>`. The suite holds the verb on a
  non-comment line.
  Red when: any of those carriers lacks the verb, which is the state check 26 reds.
  permission: check 26 itself runs inside `unattended kit gate`, whose ceiling is 16040 s, so the
  main loop runs it at VERIFYING.
- **AC6** — When `grep -n` runs over `.claude/skills/unattended/SKILL.md` for `--prepare --slug`,
  `--authorization` and `--close <slug>`, the in-place block's three command lines print in that
  order on consecutive lines. The reconcile paragraph naming `git merge` names `--authorization`
  inside the same paragraph. `bash tools/unattended/adopt-unattended.sh --check` exits 0.
  Red when: the verb sits after the close or outside the block, or the render drifted.
  cost: the adopter's check is bounded by its leg's 300 s ceiling.
- **AC7** — When `diff` compares `memory/guides/UNATTENDED-VERBS.md`, carriage returns stripped,
  with `tools/unattended/VERBS.template.md` at the build commit, it prints nothing.
  `git diff <the pass's parent sha> -- tools/unattended/VERBS.template.md`
  adds the one entry and moves line 1, and the same diff over
  `tools/unattended/PROTOCOL.template.md` and `tools/unattended/STOPS.template.md` changes line 1 of
  each and nothing else.
  Red when: a render drifted, or a carrier's content moved beyond §8 F2's ruling.
- **AC8** — When `bash tools/check-kit-versions.sh` runs at the build commit it exits 0, and
  `python tools/govkit/govkit.py epoch --base <the pass's parent sha>` reads clean for the
  unattended kit.
  Red when: a carrier keeps the old version, or the kit's shipped bytes moved with no bump.
- **AC9** — When `python tools/memory-tree/gotchas.py --for-paths tools/unattended/unattended.sh`
  runs, its checklist names the new class record. `python tools/memory-tree/gotchas.py --check`
  exits 0, and `--declares` over the record prints `declares: yes`.
  `python tools/memory-tree/row_grammar.py --check-relations <the pass's parent sha>` exits 0, and
  `python tools/codebase-map/test_codebase_map.py` prints only ok lines.
  Red when: the record is unanchored, declares nothing, is unclaimed, leaves a near match
  unanswered, or the index or the map is stale.
- **AC10** — When `bash tools/unattended/unattended.sh --authorization aGraftedHelix` runs in this
  run's worktree at the build commit, it prints `authorization-reachable — met` and exits 0, and
  `git status --porcelain` reads the same before and after it.
  Red when: the live run, whose BASE README carries no `spec-audit:` line, reads refused, or the
  call writes.
  fixture: this run's own record. The clone must hold the tip the remote advertises; otherwise check
  30 asks for a fetch, and the reading is not evaluated, the close's own precondition.

## 7. Gates

`unattended kit gate` · `pass-order history` · `brief-recorded` · `unattended skill wiring` · `unattended protocol size` · `kit version markers` · `kit epoch (shipped bytes move, the version moves)` · `verdict epoch (kit version dates the engine)` · `install-prefix (shipped surface)` · `lexicon naming predicates` · `check-wiring self-test` · `harness arms (fail branches armed or pinned)` · `line length` · `shell hygiene (a loop fed by a command substitution)` · `memory hygiene` · `codebase-map coverage + freshness` · `recall floor` · `recall floor arms` · `spec tokens (a spec's own names resolve)`

New arm: tools/unattended/unattended.test.sh · the verb on a record its BASE README makes the driver admit, asserting met and nothing written; stage a fact write added to the verb in a copy · the suite's floor rises by the arm's assertion count

New arm: tools/unattended/unattended.test.sh · the verb on the borrowed pre-89 record, asserting check 89 and both exits; stage the driver at the pass's parent · the suite's floor rises by the arm's assertion count

New arm: tools/unattended/unattended.test.sh · the verb with origin unreachable, then with the run branch unpublished, asserting not evaluated, no exits and status 2; stage the not-evaluated branch deleted in a copy · the suite's floor rises by the arm's assertion count

New arm: tools/unattended/unattended.test.sh · the source arm over the verb's body; stage the chain inlined in a copy · the suite's floor rises by the arm's assertion count

The unattended suites are not on the bar (`tools/unattended/README.md`). A pass runs its arms as
slices and the greps and diffs of §6 directly, and the main loop runs the suites once at VERIFYING.

## 8. Open questions

- **F1 — How does the lander's `--prepare` merge run the predicate?**
  Option A has `tools/push-main.sh` invoke the driver after its merge. Option B has `--close` grade
  the item before its bar and stop on a refusal. Option C has the Skill's in-place block run the verb
  between `--prepare` and `--close`. A needs a sibling-kit invocation in a flat kit that has none
  today. B reds the three arms that pin the close's full report of unmet items, and drops that
  report. C needs no driver change beyond the verb, writes nothing, so it is not the second move the
  block forbids, and puts the refusal before the bar. §4 records the reads that rejected A and B.
  RESOLVED (agent, 2026-10-05, delegated): C.
- **F2 — Which carriers change, given shared invariant 10?**
  Option A adds the verbs entry and the Skill sentences, and moves the protocol and stops templates
  by their version line alone. Option B also adds the verb to the stops template's §10 reconcile
  sentence. Option C adds no verb, using a flag on an existing one, so the verbs template keeps its
  content. Invariant 10 admits a carrier edit only where the contract would otherwise be false, and
  check 26 reads a declared verb with no entry as a contract that does not describe a verb the run
  can call. The 2026-10-05 brief for units 29 to 32 names a protocol-instruction edit for this unit
  and a stops edit for unit 31. Unit 1 added `--claims` and `--beat` entries on the same rule, and
  unit 27's F3 ratified marker-line moves. B edits a sentence that stays true. C is §4's last
  rejected alternative.
  RESOLVED (agent, 2026-10-05, delegated): A, with AC7's diffs as the observation.
- **F3 — Which exits does a refusal name, given `HANDOFF_CUTOFF` and `owner-landing`'s guard?**
  Option A names rotation and the `owner-decision` hand-off for every record, and lets the abort's
  own notice speak to `HANDOFF_CUTOFF` at the act. Option B names rotation only for a record that
  predates the cutoff. Option C names the hand-off alone. Rotation is the protocol's own mechanism
  for carrying a build to a second run (its §2), and the successor run grades everything again, so
  the work does not land as the aborted record left it. B would copy the abort notice's date
  predicate into a second place. C hides the exit this build took. `owner-landing` is check 83's
  refusal here by construction (§4), so offering it would print an exit that refuses.
  RESOLVED (agent, 2026-10-05, delegated): A.
- **F4 — What does the verb exit with when the arm never reached the README?**
  That is no anchor observed, or `trusted_base` refusing to derive a BASE. Option A exits 1, as
  `--close` reads both states, unmet. Option B exits 2 with a not-evaluated line and no exits. A
  tells a run whose remote blinked, or whose branch awaits a fetch or a push, to rotate or hand off.
  B matches `--claims`, which exits 2 with a named refusal when the remote does not answer, and lets
  the printed refusal's own remedy, or the stops template's `platform-unavailable` route, answer.
  RESOLVED (agent, 2026-10-05, delegated): B, told apart by `TB` as §4 states.

## 9. Revision log

- rev-1 · 2026-10-05 · initial draft, from H2 of the closing diff review round 1, the unit's section
  of the 2026-10-05 spec brief and the shared brief's invariants. Grounded against
  `tools/unattended/unattended.sh`, `tools/unattended/SKILL.template.md`,
  `tools/unattended/VERBS.template.md` and `tools/push-main.sh` at `9024901c`, which differs from
  BASE `018b5675` in records alone. The merge history and the population scan were read the same day.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "evaluate one Definition of Done item without closing the run, after a merge brings in a new check"`
ranked Python name stems first, `run` and `check` among them, none of them a driver seam. It printed
`unscanned layers: .sh`, so the shell layer was grepped by hand. The seam this unit extends is
`dod_met` in `tools/unattended/unattended.sh`, which `verb_close` calls for every item and
`verb_abort` already calls for two items alone: the verb is a third caller, with `observe_anchor`
and `refuse_if_terminal` before it as `--close` has them. No existing verb grades the item without
closing; `run_takeover` re-checks authorization with `allow-degenerate`, so it is not the close's
predicate. Recall surfaced the review's H2 and the aborted record's rotation row, both agreeing with
today's source. It also surfaced `TOOL-aBoundedVerdict-12`, the redirect that once hid this chain's
refusals, and `TOOL-aGradedMandate-13`, the reason the close path stays unchanged here. No catalogue
record named the class, so S7 writes one.

Recall terms used: authorization-reachable check_authorization reconcile merge origin close DoD override rotation handoff preflight base

The question passed with them: "how is a run's authorization re-checked after a reconciling merge
brings in a new rule, before close".
