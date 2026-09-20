# TOOL-dDerivedDocket-19 — authority only from an owner-committed README

**Status:** SPECCED · rev-5 · 2026-09-20 · node d · Tier-2 · base fb07ca25 · streams tooling · order 19

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-14-build-TOOL-dDerivedDocket-1-design.md](../build/2026-09-14-build-TOOL-dDerivedDocket-1-design.md) | research | TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-14 TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-20 TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1 |
| [2026-09-14-prompt-TOOL-dDerivedDocket-1-build-brief.md](../prompts/2026-09-14-prompt-TOOL-dDerivedDocket-1-build-brief.md) | journal | TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-20 TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 TOOL-dDerivedDocket-37 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1 |
| [2026-09-14-prompt-TOOL-dDerivedDocket-1-spec-brief.md](../prompts/2026-09-14-prompt-TOOL-dDerivedDocket-1-spec-brief.md) | journal | TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-14 TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-20 TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1 |
| [2026-09-14-review-TOOL-dDerivedDocket-15-spec-audit-g3-round1.md](../reviews/2026-09-14-review-TOOL-dDerivedDocket-15-spec-audit-g3-round1.md) | spec-audit | TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-20 |

<!-- /gen:spec-records -->

## 1. Goal

The ask envelope lets an ask carry a `may` clause, an authority grant that would lift the build
method's veto 2 for the paths it names (DR §19.3). Honoured from an ask row, a run could file an ask
granting itself a carrier change and then act on it, which was the blocker the critique found (fix
F1). Make authority come from exactly one place, by owner ruling D12-j: a `may:` line in a build
README the owner committed at the default-branch anchor. Nothing a run writes, and no scaffold, may
add to it, and the leg says so when something tries.

## 2. Scope (IN)

- **S1** The authorization scan (`tools/unattended/unattended.sh:1465-1471`) reads a `may:`
  front-matter line from the same blob it already parses. Preflight pins it as the run fact `may:`
  ONLY when the resolved mode is `slug`, and pins `may: none` when the key is absent. Observed by
  AC1.
- **S2** Preflight REFUSES a README whose mode is `prompt` or `recipe` and which carries a `may:`
  line, under a new driver code. Such a README resolves at a run-writable anchor, so its grant is
  one the run could have written, and a refusal makes the attempt loud where ignoring it would not.
  Observed by AC2.
- **S3** The `may:` value is one physical line of space-separated grants, or the single word `none`.
  A grant is a decision id matching the id grammar, or a repo-relative path with no leading `/`, no
  `..` segment and no backslash, containing a `/` or a file extension; either may be bare or wrapped
  in backticks, the form unit 15's ask-row `GRANT` uses, so an owner may copy a proposal verbatim.
  One function in `tools/unattended/lib-unattended.sh` strips the backticks at pin time, and the
  leg's S4 arm calls the same function. A token that is neither, including an id prefix that fails
  the id grammar, refuses preflight as a typo guard. Observed by AC3.
- **S4** Three leg arms. The `may:` fact equals the README's `may:` line at the recorded BASE. A
  `may:` fact other than `none` on a record whose mode is not `slug` reds. No commit among the run's
  own commits (§4) adds or changes a `may:` line in ANY build README, which closes the cross-run
  route of a run landing a README that grants the next run. Observed by AC4, AC5 and AC6.
- **S5** A `SCOPE` row carrying a `may` clause is a V13 failure in the backlog verdicts, which unit
  15 introduces. Observed by AC7.
- **S6** The scaffold `gen_build_index.py --new-build <slug> --asks <ids>` never emits a `may:`
  line, even when a named ask carries a `may` clause. Observed by AC8.
- **S7** Carrier text. Protocol §1, in the template and its installed copy, states the rule once:
  where a grant is honoured, what it lifts, what it does not, and that ask-row and `SCOPE`-row
  clauses honour nothing. BUILD-METHOD M3, in its template and rendered copy, gains ONE sentence
  pointing at it. The protocol §1 rule sentence opens with the fixed phrase
  `A may: grant is honoured only from`, so a criterion can find it. The §1 paragraph adds at most
  350 B to each protocol copy and the M3 sentence at most 120 B and one line to each build-method
  copy, AND EACH IS PAID FOR IN THE SAME EDIT, because no cap is raised in this build. Two
  passages leave, both MOVED rather than deleted, and each is larger than what this unit puts in
  its place:
  - out of protocol §1, the paragraph beginning `A fork with no delegated resolver is parked`,
    down to the sentence ending `spends an owner turn that was not needed`. It moves into the
    `--park` entry of `tools/unattended/VERBS.template.md` and its installed copy
    `memory/guides/UNATTENDED-VERBS.md`, which is where the verb entries live and which §7 of the
    protocol already records as a byte decision of exactly this shape.
  - out of BUILD-METHOD M3, the paragraph beginning `Mark it in place` and ending
    `§8 says what that cannot see`. It moves into §8 of `tools/memory-tree/SPEC-TEMPLATE.template.md`
    and its rendered copy `memory/TEMPLATE-SPEC.md`, which the memory-tree README's method pointer
    table already names as the owner of the §8 mark grammar — and whose own rule is that a rule
    appearing in both the method and a carrier it points at is a defect in the method. M3 keeps
    ONE line pointing there, and the moved text drops its own pointer back to that file, which
    becomes a self-reference once it lands inside it.
  No other unit of this build trims either passage, and neither DESTINATION is this unit's alone.
  One unit rewrites text INSIDE the BUILD-METHOD passage this unit moves: the fork-item unit
  ordered later replaces the sentence saying both readers grade the SECTION and not each item, and
  its own section 2 now follows that sentence into section 8 of `memory/TEMPLATE-SPEC.md` and its
  kit template rather than into M3, because this unit lands first. The move is this unit's; the
  rewrite lands where this unit put the text. The verbs pair is written by an earlier unit of this
  build too, which lands its own moved paragraph in the `--attest` entry while this unit lands in
  `--park`: two disjoint entries in one file, so the sharing is an ordering fact and not a contested
  passage. Observed by AC9 and AC11.
- **S8** A `memory/DECISIONS.md` row under this unit's own id records the M3 boundary change, as fix
  F1 requires. Observed by AC10.

## 3. Non-goals (OUT)

- The `may` clause grammar on ask rows and the `--asks --ready` Grant column are unit 15's and do
  not change. Under D12-j an ask-row `may` is a PROPOSAL the owner may copy into a README by hand; it
  is printed, and it is never honoured.
- The ids start, E3's recipe and `asks:` pinning are unit 16's.
- Enforcing M3's vetoes in code. The run's M3 resolution is agent judgement; the kit pins the grant
  and states the rule, and nothing here claims to observe what the agent then did.
- Lifting veto 3. A grant lifts veto 2 only; see §8 F1.
- Deciding whether a README on the default branch was typed by the owner or landed by an earlier
  run. The anchor cannot tell, which is why S4's third arm refuses the run-side route instead.
- The endpoint for a derived-LANDED record: unit 22's `landing_commit_of` finds it, and this unit,
  ordered earlier, may not consume from that unit.

### Edges

- **consumes-from** `TOOL-dDerivedDocket-16` — the one-scan front-matter parse that `asks:` joins,
  the pinned-fact seam at preflight, and the resolved mode. Without them `may:` has no scan to join
  and no mode to condition on.
- **consumes-from** `TOOL-dDerivedDocket-15` — the V13 verdict S5 extends and the `--new-build`
  scaffold S6 constrains.
- **consumes-from** `TOOL-dDerivedDocket-17` — the run's-own-commits function the cross-run arm
  calls, given one exclusion tip for a live record and one per merge the terminal walk reads for a
  terminal record.
- **consumes-from** `TOOL-dDerivedDocket-2` — the prepared merge whose first parent is the
  advertised tip, which is why excluding that tip leaves exactly the run's commits, and whose second
  parent is the run branch, the side the terminal-record exclusion reads as the run's.
- **hands-off** `TOOL-dDerivedDocket-20` — the Skill and protocol text for the authority rule, which
  this spec's §5 places with the carriers unit.
- **hands-off** `TOOL-dDerivedDocket-22` — the cross-run arm's endpoint for a derived-LANDED record,
  which that unit's `landing_commit_of` finds; the terminal-record exclusion function that unit's S17
  applies to that landing commit; and the unattended-suite arms its AC13 run executes first.

## 4. Design

### What a grant is, and where it is honoured

| Source of a `may` value | Honoured? | Why |
|---|---|---|
| `may:` in a README resolved in `slug` mode | yes, pinned at preflight | `slug` resolves only at the default-branch anchor, so a folder already existed there before the run |
| `may:` in a README resolved in `prompt` or `recipe` mode | refused at preflight | those modes admit the second anchor, which the run can write |
| a `may` clause on an ask row | never | anyone holding the ask's slug writes the row |
| a `may` clause on a `SCOPE` row | refused as V13 | a triager writes it about someone else's ask |
| the scaffold's output | never emitted | a generated README carries no authored authority |

`slug` mode implies the default-branch anchor because the second anchor admits only
`SECOND_ANCHOR_MODES="prompt recipe"` (`tools/unattended/unattended.sh:580`), and leg check 29
already reds a `slug` record whose BASE came from the second anchor.

### What a grant lifts

A path grant lifts veto 2 for a change confined under that path. A decision-id grant lifts veto 2
for the change that `memory/DECISIONS.md` row ratifies. Veto 1 and veto 3 are untouched. The protocol
states this once, in §1, and M3's added sentence points there, so the rule is not stated twice
(M1's one rule).

### The cross-run arm

A run lands commits on the default branch; a README it lands becomes a default-branch README for
the next run, so without a guard one run could grant another (TOOL-aStandingWrit-1). The arm walks
each run's OWN commits, through the run's-own-commits function unit 17 adds to
`tools/unattended/lib-unattended.sh`, and reds a commit whose diff against its first parent adds or
changes a `may:` front-matter line in any `memory/builds/*/README.md`. A two-parent commit is read
by its combined diff, `git diff-tree --cc`, instead. Its first-parent diff carries everything its
other parent brought in, which for a reconcile is default-branch content, while each parent's own
commits in the range are graded where they were made, so a merge answers only for the lines it
wrote itself (§8 F8). The endpoint and exclusion per recorded state:

- a record in a working phase or HELD: endpoint HEAD, base the recorded BASE, exclusion the default
  branch's advertised tip as the leg already observes it for check 7 (`ADV_HEAD`); with the tip
  unobserved, the local default-branch ref, announced as the weaker reading;
- a terminal record: endpoint its recorded witness. Its exclusions are computed by one function in
  `tools/unattended/lib-unattended.sh`, which this unit adds beside the arm, and a terminal record
  with no witness fact is skipped by name, never passed. The function reads the commit graph, the
  recorded BASE and the record's run-state path, which is its build folder's `RUN.md` even for an
  archived record, because every record commit the run made touched that path. It reads no
  default-branch tip. It walks from the witness, passing each single-parent commit to its parent.
  At each two-parent commit it meets, the witness included, the RUN SIDE is the parent from which a
  commit since BASE touching the run-state path is reachable,
  `git rev-list -1 <parent> ^<BASE> -- <run-state path>`. The function excludes the other parent
  and descends the run side, so nested merges are read in turn. Where neither parent, or both,
  reach such a commit, that merge adds no exclusion and the walk stops there, the fail-closed
  direction; the walk also stops at a commit BASE holds and at a commit with more than two parents.
  The shapes it reads (§8 F8):
  1. **Unit 2's prepared merge T.** An in-place close commit, and any record commit after it, sit
     on T, whose second parent is the run branch, so T's first parent is excluded. Without that, the
     witness's history since BASE runs into every default-branch commit landed since BASE. This
     covers a record unit 22's `--preflight` rotated, whose witness is the landing commit, and an
     in-place run aborted after its close.
  2. **A plain reconcile R on the run branch**, the `git merge <remote>/<def>` a run makes when
     `--prepare` refuses and names it, or mid-run under primary. The run side is R's first parent,
     so R's second parent, the default-branch commits the reconcile brought in, an owner's `may:`
     commit among them, is excluded. `--abort` records HEAD, so a run aborted directly after R has R
     as its witness, read the same way, and so is a landed primary record whose witness, the landing
     merge's second parent, is R.
  3. **The primary lander's `--no-ff` landing merge L**, pushed or not, as the witness or under a
     single-parent fix commit that push-main then pushed. The run side is L's second parent, the run
     branch, so L's first parent is excluded.
  4. **Push-main's reconcile**, the `git merge --no-ff <remote>/<def>` it makes on the default branch
     when the remote moved, which is then the pushed HEAD, the marker's commit and `--landed`'s
     witness. The run side is its first parent, which holds L, so its second parent, other nodes'
     commits, is excluded and the walk goes on to L.
  5. **No merge on the tail.** The witness is the run branch's own tip, whose history since BASE is
     the run's, and there is no exclusion.
- a LANDING record whose landing commit is on the advertised tip (derived LANDED, D12-i2): unit 22
  supplies the endpoint, its landing commit. The exclusion is this function applied to that commit,
  so the record's range does not change when it is rotated or made terminal;
- a committed LANDING record whose landing commit is not yet on the advertised tip, or whose tip is
  unobserved: read as the first case (endpoint HEAD, the advertised tip excluded), because a landing
  that has not reached the tip can still gain commits after a refused push, and ending the walk at the
  landing commit would never grade those (§8 F7).

It reads the diff, never the run's own claim. A grant a person types on the default branch reaches a
run's tree only through a default-branch commit, which the exclusion removes, and through the merge
that brought it in, whose combined diff does not carry it, so the arm never reds the channel D12-j
keeps open.

Stated residual: the function tells a merge's sides by where the record's commits are, not by who
made the other commits. A side that holds run commits but no commit touching the run-state path
since BASE reads as default-branch content, and its commits leave the range. A branch forked from
the run branch after the record's first commit holds that commit, so it reads as both sides and
takes no exclusion; only a branch forked outside the run's history, at BASE or on the default
branch, carrying run commits and merged in, has that shape. No verb of the kit makes one, and like
the anchor's own limit in §3, the arm closes the kit's route, not a deliberate construction. A run
whose record commits already reached the default branch, in an earlier landing or through another
node's run of the same slug, reads both sides at a later merge and stops there, which can red an
owner's grant but hides no run commit. The function makes no remote observation, so a stale or
unobserved tip changes no terminal range.

### Fail codes

The S2 and S3 refusals take new driver codes, and the S4 arms report under the leg's check 19 beside
the mode arms they extend. New numbers are allocated at build time as the next free integer, because
other units of this build allocate codes concurrently.

### Rollout

No gov README carries `may:` today, so every run pins `may: none` and every arm passes over an
honest absence. The fixtures carry the coverage.

### Inventory

- the README front-matter key `may:` and the run fact `may:`;
- two driver refusal codes, numbers allocated at build time;
- the grant-token normalising function in `tools/unattended/lib-unattended.sh` (S3), shared by the
  driver and the leg;
- the terminal-record exclusion function in `tools/unattended/lib-unattended.sh`, which reads each
  merge on a witness's tail by the parent that reaches a commit touching the record's run-state path
  since BASE, shared with unit 22's S17;
- one `memory/DECISIONS.md` row under this unit's own id.

Any new shell function is named through `python tools/lexicon/lexicon.py --suggest <identifier>
--as <cell>`.

### Files touched (estimate)

`tools/unattended/unattended.sh` · `tools/unattended/lib-unattended.sh` ·
`tools/unattended/unattended.test.sh` ·
`tools/unattended/check-unattended.sh` · `tools/unattended/check-unattended.test.sh` ·
`tools/unattended/PROTOCOL.template.md` · `memory/guides/UNATTENDED-PROTOCOL.md` ·
`tools/memory-tree/BUILD-METHOD.template.md` · `memory/guides/BUILD-METHOD.md` ·
`tools/unattended/VERBS.template.md` and `memory/guides/UNATTENDED-VERBS.md`, and
`tools/memory-tree/SPEC-TEMPLATE.template.md` and `memory/TEMPLATE-SPEC.md`, the two pairs S7's
moved passages land in ·
`tools/memory-tree/backlog.py` and its selftest · `tools/memory-tree/gen_build_index.py`'s selftest ·
`memory/DECISIONS.md` · `.memory-tree.conf` for `ARMS_FLOORS`.

### Budgets

NO CAP IS RAISED IN THIS BUILD, and no SHARE of one is claimed either. Raising M1's budget or the
guide cap is an owner turn under veto 2, the free space does not cover every unit that wants it, and
a share is only a promise about a sum nobody can check at a single pass. So this unit lands NET ZERO
OR NEGATIVE on both capped carriers it writes to, paying for each addition inside the same edit
(S7), and AC11 reads each file at this unit's own pass against its PARENT commit rather than against
a budget.

`memory/guides/BUILD-METHOD.md` stood at 26439 B and 336 lines at `abac6d59` and at 27264 B and
347 lines at BASE `fb07ca25`, after aRatifiedRulings, aDeferredBar and aProbedUnit grew it, against
the 27648 B declared at `tools/template-size-limits.txt:86` and the 350 lines its own budget line
declares. This unit adds the M3 pointer sentence, at most 120 B and one line, and removes M3's
`Mark it in place` paragraph, which is larger in both bytes and lines. Only the byte half is gated —
no checker reads the line half of that budget row (`tools/template-size-limits.txt:84-85`) — which
is why AC11 counts the lines itself rather than trusting the leg to.

`memory/guides/UNATTENDED-PROTOCOL.md` stood at 57815 B at `abac6d59` and 60324 B at BASE against
its 61440 B guide cap. This unit adds the §1 rule paragraph, at most 350 B, and removes §1's
`--park` paragraph, which is larger.

Both removals are MOVES with a named destination, so nothing is lost from the contract, and each
frees more than this unit spends. That hands headroom BACK to the other carriers' spenders — units
20 and 31 on the build method, units 3, 4, 5, 16, 17, 20, 22, 27 and 28 on the protocol — instead of
competing with them. Whether their own sum then closes is still the orchestrator's to settle and is
not a thing this unit's pass can observe.

### Alternatives rejected

- **Honour the union of `may` clauses on mandated asks, read at M-BASE (DR §19.2).** Rejected by
  fix F1 and ruling D12-j: M-BASE is on the default branch, but the row's writer is anyone holding
  the ask's slug, including a run that filed it.
- **Ignore a `may:` line on a prompt-mode README silently.** It leaves a self-grant attempt invisible
  in every record; S2's refusal costs a legitimate prompt run nothing, because such a README has no
  reason to carry the key.

## 5. Production-readiness checklist

- security — this unit narrows an authority surface to one owner channel and adds a refusal for the
  run-side route; it adds no write path.
- perf / scale — one more key in an existing scan; the cross-run arm is one diff per commit in the
  run range, over the README glob only, and a terminal record's walk adds one `git rev-list -1` per
  parent of each merge it meets.
- error / empty / loading states — absent key pins `none`; a malformed grant is a named refusal; a
  prompt-mode grant is a named refusal.
- observability — the pinned fact is printed at preflight and re-read by the leg.
- risks — the anchor cannot prove a default-branch README was typed by the owner; S4's third arm
  closes the kit's own route and states the rest.
- testing — arms in the driver and leg suites and in the backlog and build-index selftests, each
  observed by hand in a scratch fixture repo with a local bare remote (D12-h method (b)); the
  unattended-suite arms (`unattended.test.sh`, `check-unattended.test.sh`) run first in unit 22's
  single attributed suite run (its AC13), the next unit the build's self-test list permits, because
  `tools/gate-legs.json` carries no leg for those suites; the backlog and build-index selftest arms
  run at the post-build bar under `GATE_SELFTESTS=1`.
- migration — none; no README carries the key.
- user docs — protocol §1 and one M3 sentence, plus the two passages S7 moves out of those same
  two documents into the verbs guide and the spec template; the Skill's own text is unit 20's.

## 6. Acceptance criteria

- **AC1** — When `--preflight` runs over a `slug`-mode fixture README carrying `may:` with a path
  and a decision id, the record pins those grants as `may:`; with no key it pins `may: none`. Proven
  in `tools/unattended/unattended.test.sh`.
  Red when: the fact is pinned in `prompt` mode as well, so a run-written README grants.
  permission: this unit may not run the unattended suites; the observation is made by hand in a
  scratch fixture repo with a local bare remote, and the suite runs in unit 22's attributed run (its
  AC13), which the main loop makes at the one post-build bar at VERIFYING, after the last unit.
- **AC2** — When `--preflight` runs over a `prompt`-mode fixture README carrying `may:`, and over a
  `recipe`-mode one, it refuses under its new code and writes nothing.
  Red when: preflight pins `may: none` and continues, which hides the attempt, or the refusal keys on
  `prompt` alone, so a `recipe` README grants.
- **AC3** — When the `may:` value carries `EXMP-aFoo3`, an id prefix failing the id grammar,
  preflight refuses naming the token; when it carries `` `tools/push-main.sh` `` and, in a second
  fixture, `tools/push-main.sh`, both pin the fact `may: tools/push-main.sh`, and check 19's S4 arm
  is green on both.
  Red when: the malformed token is pinned as a grant, or the two spellings pin differently, so the
  leg's comparison depends on how the owner copied the grant.
- **AC4** — When a fixture record's `may:` fact differs from the README's line at its recorded BASE,
  `bash tools/unattended/check-unattended.sh` reds check 19 naming both values.
  Red when: the arm compares against the README at HEAD.
- **AC5** — When a fixture record in `prompt` mode carries `may:` other than `none`, check 19 reds.
  Red when: the arm grades only `slug` records.
- **AC6** — When a commit among a fixture run's own commits adds a `may:` line to another build's
  README, `bash tools/unattended/check-unattended.sh` reds check 19 naming the commit and the README.
  Take an owner commit on the fixture's default branch, made after BASE, that adds `may:` to a build
  README and reaches the run branch through a prepared merge whose first parent is the advertised
  tip. Check 19 does not red in any of three records:
  - a live record;
  - a terminal primary-mode record whose witness is the `--no-ff` landing merge over the same owner
    commit, graded once with that merge on the advertised tip and once unpushed, where a `may:`
    commit the run made still reds in both;
  - a terminal in-place record whose witness is the single-parent close commit on that prepared
    merge, where a `may:` commit the run made before `--prepare` still reds.

  Two more terminal primary-mode records land a run that made a `may:` commit, over the same owner
  commit. In each, check 19 reds naming the run's commit and names no owner commit:
  - one whose witness is a single-parent fix commit on top of that landing merge, pushed;
  - one whose witness is push-main's `git merge --no-ff <remote>/<def>` reconcile, made after
    another node pushed a second owner commit adding `may:` to a build README.

  Take a run that adds `may:` to another build's README in its own commit, then brings the same kind
  of owner commit in through a plain `git merge` reconcile, and aborts before `--prepare`. Grade it
  once live, before the abort, and its terminal record twice, once with the reconcile itself as the
  witness and once with a single-parent commit after it. In all three, check 19 reds naming the
  run's commit and does not red for the owner's, because the terminal exclusion is the reconcile's
  second parent and never its first, and the reconcile answers only for its combined diff.
  Red when: the arm reads only the run's own README, so the cross-run grant passes; or it walks
  `BASE..HEAD` or `BASE..witness`, so the owner's default-branch grant reds a run that then cannot
  land, and once archived reds the bar for ever; or the terminal row takes an exclusion only from a
  two-parent witness, so an in-place record's single-parent close commit ranges over every
  default-branch commit landed since BASE; or it takes nothing from a plain reconcile, so an owner's
  grant that an aborted run reconciled in reds the archive for ever; or it reads a merge's run side
  from parent order or from the default-branch tip, not from which parent reaches a commit touching
  the run-state path since BASE, so a reconcile's first parent, or a landing merge's second parent
  under a fix commit, is excluded and the run's grant passes, or push-main's reconcile has its first
  parent excluded with the whole run behind it; or it reads a merge by its first-parent diff, so
  the owner's grant a reconcile brought in reds through the reconcile itself.
- **AC7** — When a fixture `BACKLOG.md` carries a `SCOPE` row with a `may` clause, the backlog
  verdicts report V13 naming the row.
  Red when: V13 grades only the clause grammar and admits the label.
- **AC8** — When `python tools/memory-tree/gen_build_index.py --new-build` scaffolds a README over a
  fixture ask carrying a `may` clause, the output has no `may:` line.
  Red when: the scaffold copies the clause into front matter.
- **AC9** — When `bash tools/unattended/check-unattended.sh` and the `kit/dogfood doc parity` leg
  run after S7, both copies of protocol §1 and of BUILD-METHOD are byte-identical to their
  templates, and the `build-method size` leg stays green.
  Red when: the sentence lands in one copy only, or BUILD-METHOD exceeds its byte cap.
  permission: unit passes run no gate legs (fix F7); this observation is made at the build's one
  post-build bar.
- **AC10** — When `git grep -n "TOOL-dDerivedDocket-19" memory/DECISIONS.md` runs, it returns one row
  recording that a grant is honoured only from an owner-committed README and lifts veto 2 only.
  Red when: the row is absent, so the M3 boundary change lives only in carrier prose.
- **AC11** — When `git grep -c "A may: grant is honoured only from"` runs over
  `tools/unattended/PROTOCOL.template.md` and `memory/guides/UNATTENDED-PROTOCOL.md`, each returns 1,
  and that sentence names the owner-committed `slug` README, veto 2 only, and that ask-row and
  `SCOPE`-row clauses honour nothing; `git grep -c "protocol §1"` over
  `tools/memory-tree/BUILD-METHOD.template.md` and `memory/guides/BUILD-METHOD.md` finds exactly one
  more M3 sentence than at this unit's parent; and `git cat-file -s` run at this unit's parent and at
  its commit reports a SMALLER size at the commit for all four of
  `memory/guides/BUILD-METHOD.md`, `tools/memory-tree/BUILD-METHOD.template.md`,
  `memory/guides/UNATTENDED-PROTOCOL.md` and `tools/unattended/PROTOCOL.template.md`, each of the
  first pair also under the 27648 B declared at `tools/template-size-limits.txt:86` and each of the
  second under the 61440 B guide cap. `wc -l` over `memory/guides/BUILD-METHOD.md` at the same two
  commits reports FEWER lines at the commit, and under the line budget its own `**Budget:` line
  declares. The two destinations carry what left: `git grep -c "fork-unresolvable"` over
  `memory/guides/UNATTENDED-VERBS.md` returns at least 1, `git grep -c "and it may WRAP"` over
  `memory/TEMPLATE-SPEC.md` returns 1; `memory/guides/UNATTENDED-VERBS.md` reads under the 61440 B
  cap its guide class carries (`tools/memory-tree/check-memory-hygiene.sh:84`), and no cap clause is
  asserted for `memory/TEMPLATE-SPEC.md`, which sits outside that class and which no row of
  `tools/template-size-limits.txt` names, so it carries no declared ceiling to read.
  Red when: the edit is empty; or either carrier is the same size or LARGER at this unit's commit
  than at its parent, so this unit spent headroom it was told to fund from its own edit instead —
  which is why the comparison is against the parent commit and never against a declared share,
  a share being a claim about a build-wide sum that no single pass can observe; or the line
  count on the build method holds or grows, which no checker would
  catch (`tools/template-size-limits.txt:84-85`) and which is how that document reaches a budget no
  unit of this build may raise; or a passage was DELETED rather than moved, so the carrier shrank
  and the contract lost a rule.
  permission: a read, a byte count and a line count, no gate leg and no suite.

## 7. Gates

`unattended kit gate` · `harness arms (fail branches armed or pinned)` · `memory hygiene` · `kit/dogfood doc parity` · `build-method size` · `build-index selftest` · `spec tokens (a spec's own names resolve)`

New arm: `tools/unattended/unattended.test.sh` · a `slug` README with `may:`, a `prompt` and a `recipe` README with `may:`, a malformed grant, a grant in both spellings · the driver suite's executed-assertion floor, and `ARMS_FLOORS` for `tools/unattended/unattended.sh`
New arm: `tools/unattended/check-unattended.test.sh` · a forged fact, a `prompt` record with a grant, a run's own commit adding `may:` to a foreign README, an owner commit reaching the run through a prepared merge, a terminal primary-mode record whose witness is the landing merge, pushed and unpushed, a primary record whose witness is a fix commit on that pushed landing merge, a primary record whose witness is push-main's reconcile over another node's owner `may:` commit, a terminal in-place record whose witness is the close commit on that prepared merge, and a run aborted before `--prepare` after a plain reconcile brought an owner `may:` commit in, graded live and with its witness once the reconcile and once a commit after it · the leg suite's executed-assertion floor, and `ARMS_FLOORS` for `tools/unattended/check-unattended.sh`

## 8. Open questions

- **F1 — does a grant lift veto 3 as well as veto 2?** Lifting both is the more feature-rich option,
  and it is discarded by veto 3 itself: a grant that widens a security or write surface beyond the
  tier's pricing is exactly what veto 3 refuses. RESOLVED (agent, 2026-09-14, delegated): veto 2
  only.
- **F2 — where may authority come from?** RESOLVED (owner, 2026-09-13): D12-j, only from an
  owner-committed build README at the default-branch anchor; the scaffold never emits `may:`.
- **F3 — the brief's edge table has unit 16 consuming from this unit, against the declared order.**
  Unit 16 is ordered before this unit, and the hygiene edge arm reds a consumes-from whose target is
  ordered after the consumer. The dependency runs the other way: this unit extends unit 16's scan
  and pinning. RESOLVED (agent, 2026-09-14, delegated): this unit declares consumes-from unit 16;
  unit 16's spec owes the matching hands-off, and its consumes-from this unit is dropped.
- **F4 — which commits does the cross-run arm walk?** Options: the plain `BASE..witness` and
  `BASE..HEAD`; the run's own commits, excluding the default branch's side of the landing. Under both
  lander modes the first holds every default-branch commit landed since BASE, so an owner's
  hand-typed grant, the channel ruling D12-j keeps open, reds the run, and the archived record reds
  the bar for ever. RESOLVED (agent, 2026-09-14, delegated): the run's own commits, through unit
  17's function, with unit 22 supplying the derived-LANDED endpoint; it restates design fix F4's
  range.
- **F5 — how is a grant token spelled in a README?** Options: bare only; backticked only; both,
  normalised to bare by one shared function. Bare-only refuses an owner copying an ask-row proposal
  verbatim; backticked-only diverges from every other front-matter key. RESOLVED (agent, 2026-09-14,
  delegated): both, normalised by one library function the driver and the leg share.
- **F6 — which stage first executes this unit's unattended-suite arms?** Options: (a) add this unit
  to the build's self-test list; (b) unit 22's single `run-unattended-gates.sh --attribute <BASE>`
  run, the next permitted run after this unit; (c) the landing's compensating check, which is on
  demand and bound to no unit. (a) contradicts owner rulings D12-h and D12-i8, which name the
  permitted units, so it is not an option here; (c) guarantees neither execution nor attribution
  before landing. RESOLVED (agent, 2026-09-14, delegated): (b), with a hands-off to unit 22.
- **F7 — where does the cross-run walk end for a committed LANDING record whose landing commit is
  not yet on the advertised tip?** Options: (a) read it as a live record, endpoint HEAD with the
  advertised tip excluded (fold plan c3 E32); (b) end it at its landing commit (fold plan c1 E45).
  (b) never grades a commit made after a refused push, which is exactly when a run keeps writing, so
  it covers less. RESOLVED (agent, 2026-09-14, delegated): (a), the more complete survivor; unit 22
  needs no endpoint for this population.
- **F8 — what does the terminal-record row exclude when its witness is, or sits on, a merge?**
  rev-2 excluded a two-parent witness's first parent only, which ranges an in-place record's
  single-parent close commit over every default-branch commit landed since BASE, so an owner's grant
  reds the archive for ever (spec audit G1 round 2, B2). rev-3 walked single-parent commits to unit
  2's prepared merge, recognised by its `merge: <slug> — land onto` subject. The second fold pass
  added default-branch tip tests, one reading a merge on the tail as a plain reconcile and one
  telling a reconcile witness from a landing merge. Fold verification found both fail open on the
  ordinary primary route: under a single-parent fix commit on a pushed `--no-ff` landing merge, the
  reconcile test excluded the run branch; and with push-main's own `--no-ff` reconcile as the
  witness, the first parent excluded held the landing merge and the whole run. Options:
  - (a) tell each merge's run side by content: the parent from which a commit since BASE touching
    the record's run-state path is reachable. Exclude the other, descend the run side through nested
    merges, and take no exclusion where neither parent or both reach one;
  - (b) keep the tip tests, and state their fail-open shapes as residual.

  (b) knowingly accepts a fail-open on the ordinary primary route, where a fix commit follows the
  landing merge or push-main reconciles. RESOLVED (agent, 2026-09-16, delegated), decided by the
  orchestrator: (a), §4's terminal-record bullet. One rule reads T, a plain reconcile, a primary
  landing merge, push-main's reconcile and a landed witness that is the run's last reconcile. It
  needs no fact, subject or tip, and gives a primary record the same run commits before and after
  `--landed`. F7 is unchanged, because its population is a LANDING record not yet on the advertised
  tip.

  Excluding a reconcile's second parent does not keep the owner's grant out on its own, because the
  arm diffs a commit against its first parent and a reconcile's first-parent diff carries what it
  brought in. Options: (i) diff a merge against the parent the walk excluded; (ii) skip two-parent
  commits; (iii) read a two-parent commit by its combined diff, `git diff-tree --cc`, the lines
  neither parent holds; (iv) keep the first-parent diff. (iv) reds the owner's grant through every
  reconcile, live or terminal. (ii) never grades a grant written in a merge's own conflict
  resolution. (i) needs a run side, which a live range and a merge the walk stopped at lack, and it
  reads an owner's local commit not yet pushed as the merge's. RESOLVED (agent, 2026-09-16,
  delegated): (iii), in every range the arm walks. Each parent's own commits in the range are graded
  where they were made, so the merge answers only for what it wrote.

## 9. Revision log

- rev-1 · 2026-09-14 · initial draft from fix F1 and ruling D12-j. Reverses the brief's edge between
  this unit and unit 16 (§8 F3) and adds consumes-from unit 15, whose V13 verdict and scaffold this
  unit constrains. Adds the cross-run arm, which neither DR nor the brief names, after the regrounding
  found that a `slug` README on the default branch can be one an earlier run landed.
- rev-2 · 2026-09-14 · §3 §4 §5 §7 §8 · S3 S4 S7 · AC1 AC2 AC3 AC6 AC11 · spec audit round 1
  folded. G3 H7: the cross-run arm walks only the run's own commits through unit 17's function, per
  recorded state, with unit 22 supplying the derived-LANDED endpoint (§8 F4; restates design fix F4's
  range); consumes-from units 17 and 2 and hands-off unit 22 added; AC6 gains the owner-commit
  negative arm. G3's observation on in-place LANDING records: a record in a working phase or HELD
  walks to HEAD, as fold plan c1 E45 states. The endpoint of a committed LANDING record whose
  landing commit is not yet on the advertised tip, where fold plans c3 E32 and c1 E45 disagreed, is
  settled by the orchestrator as a live record, endpoint HEAD (§8 F7, §4). G3
  M5: the unattended-suite arms run first in unit 22's attributed run (§8 F6). G3 M23: AC11 reads the
  carrier sentence and both byte budgets. G3 L4: a `recipe` arm and the grant token grammar (§8 F5),
  the normalising function joining Inventory and Files touched.
- rev-3 · 2026-09-16 · spec-audit round 2 fold. G1 B2 (1) with M4 (7, 35), from the G1 round-2
  record.
  - §4's terminal-record bullet excludes the first parent of a prepared merge the witness reaches
    through single-parent commits, recognised by unit 2's subject, before the two-parent test.
  - The derived-LANDED bullet applies the same function to unit 22's landing commit.
  - The stated residual names the subject recognition. Fold verification scoped its population: a
    record whose witness reaches no prepared merge, which includes an in-place run aborted before
    `--prepare`, while unit 2 S3's refusal covers only a plain reconcile made in place of `--prepare`.
  - The Inventory gains the function.
  - AC6 gains the in-place terminal arm and the plain-reconcile arm, and §7's arm list names both.
  - The consumes-from edge to unit 2 names the subject, and the hands-off edge to unit 22 names the
    function (§8 F8).
  - F7 is kept: its population is a LANDING record not yet on the advertised tip.
- rev-4 · 2026-09-16 · §4 · §7 · §8 F8 F9 · S4 · AC6 · spec-audit round 2 fold, second pass, from
  fold verifier problem f2 (plain-reconcile residual), decided by the orchestrator as option A. §4's
  terminal exclusion function gains case 2: a plain reconcile's second parent, when the
  default-branch tip holds it, is excluded, and the function reads the tip the working-phase bullet
  reads. §8 F8 records that decision. §8 F9 extends case 2 to an unlanded two-parent witness,
  because `--abort` records the reconcile itself as its witness. The stated residual is rewritten,
  and the Inventory names the reconcile reading. AC6's plain-reconcile arm grades a run aborted
  before `--prepare` under both witness shapes and asserts that the owner's reconciled `may:` commit
  does not red, and §7's arm line follows. S4's text is unchanged; AC6 still observes it. Fold
  verification: AC6's primary-mode record is graded with its landing-merge witness pushed and
  unpushed, the run's own `may:` commit still red in both, with a matching Red when clause, so each
  of §8 F9's two tip tests is observed; §7's arm line names that record. Third pass, §3 §4 §5 §6 §7
  §8 F8 F9 · AC6, from the fold verifier's two problems on the terminal-row exclusion, a fix commit
  on a pushed landing merge and push-main's reconcile as the witness, decided by the orchestrator as
  a content-based run side. §4's terminal-record bullet replaces the four cases and every tip test
  with one rule: at each merge on the witness's tail, the parent that reaches a commit touching the
  record's run-state path since BASE is the run side, the other parent is excluded and the walk
  descends, and where neither or both do there is no exclusion. The function no longer reads unit
  2's subject or the tip. The cross-run arm reads a two-parent commit by its combined diff, a fork
  this pass decided, because a reconcile's first-parent diff carries the owner's grant. The stated
  residual, the Inventory, §5's perf line and the consumes-from edges to units 2 and 17 follow. §8
  F8 is rewritten as both decisions, and F9, which this rev's second pass added, is withdrawn into
  it. F7 is kept. AC6 gains the fix-commit and push-main-reconcile records and grades the aborted
  run live as well; its `Red when:` replaces the tip-test clause, and §7's arm line follows. S4's
  text is unchanged; AC6 still observes it.
- rev-5 · 2026-09-16 · regrounded on fb07ca25 (origin/main). S1 and §10 re-cite the authorization
  scan at `tools/unattended/unattended.sh:1465-1471` and §4 `SECOND_ANCHOR_MODES` at `:580`, both
  moved by the aProbedUnit, aDeferredBar and aRatifiedRulings driver commits with their shapes
  unchanged. §4 Budgets re-measures both carriers at BASE: BUILD-METHOD at 27264 B and 347 lines
  after aRatifiedRulings, aDeferredBar and aProbedUnit grew it, 384 B and 3 lines under its caps, and
  the protocol at 60324 B, 1116 B under its cap; this unit's own budgets and AC11 are unchanged. §10
  states what the landed builds moved at the seams. No landed build adds a `may:` grant, and no S-item
  is done on main. Extended 2026-09-20, same base, on a second regrounding pass: every citation above
  re-read at HEAD and confirmed, `tools/unattended/unattended.sh:1465-1471` the one front-matter `awk` and `:580`
  `SECOND_ANCHOR_MODES`; check 29's refusal at `tools/unattended/check-unattended.sh:1420` and
  `ADV_HEAD` at `:294` still carry the shapes S4 and §4 read; `tools/gate-legs.json` still runs neither
  unattended suite, so §8 F6's premise holds; and both carriers re-measured unchanged at 27264 B and
  60324 B. §4 Budgets now states that this unit's 300 B and unit 20's 250 B together exceed
  BUILD-METHOD's 384 B of headroom, which is the orchestrator's to settle and not this unit's.
  Verification pass, same regrounding: that extension cited the authorization scan by bare basename,
  and now spells it `tools/unattended/unattended.sh:1465-1471`, so the citation resolves against a
  tracked path instead of being skipped as an untracked one.
  Extended again 2026-09-20, same base, by the regrounding consolidation pass · §4 Budgets · S7 ·
  AC1 AC11 · §7. The two capped carriers are TRIMMED to fit rather than re-argued, because no cap is
  raised in this build: BUILD-METHOD falls from 300 B to 120 B and one line, of the 384 B free, and
  the protocol from 600 B to 350 B of the 1116 B free. S7 prices both, §4 Budgets records the
  trimmed split against unit 20's own cut to 160 B and what it leaves unit 31, and AC11 now reads
  each file's SIZE against its cap at the pass as well as its net growth. AC1's `permission:` line
  says where unit 22's attributed run happens under the conservative reading of the D12-h conflict,
  which this pass folds and does not decide; §8 F6 stands as resolved. §7's two `New arm:` lines
  name the suites' executed-assertion floors beside their `ARMS_FLOORS` pins. Every criterion here
  asserting a count was re-run at HEAD: none asserts that a phrase counts zero, so none could be
  green before the unit acts.
  Extended again on the closing consolidation pass · S7 · §4 Budgets · §5 · AC11, with the header
  date moved to the last-change date and the rev kept. The two capped carriers stop being priced
  as SHARES of free space and become NET ZERO OR NEGATIVE at this unit's own pass, which is the
  only thing a pass can observe: a share is a claim about a build-wide sum, and the sum did not
  close on either carrier. S7 names the two passages that leave — protocol §1's `--park`
  paragraph, to the `--park` entry of the verbs pair, and M3's `Mark it in place` paragraph, to
  §8 of the spec-template pair, whose own pointer table already owns that grammar — and both are
  moves rather than deletions. §4 Budgets is rewritten around that, §4 Files touched gains the
  two destination pairs, and §5's user-docs line follows. AC11 now compares all four carrier
  files against this unit's PARENT commit, counts BUILD-METHOD's lines itself because no checker
  reads that half, and reds a carrier that held or grew, a line count that did not fall, and a
  passage deleted instead of moved. Each destination witness was counted at HEAD and returns 0
  today, so AC11 cannot be green before the unit acts. Both passages are this unit's alone to
  TRIM, though neither destination is its alone to write.
  Verification pass, same consolidation: AC11's closing clause read `each destination is under its
  own cap`, which could not fail for `memory/TEMPLATE-SPEC.md` — that file sits outside the guide
  class and no row of `tools/template-size-limits.txt` names it, so it has no ceiling to be under.
  The clause now names the verbs guide's real cap and says plainly that the spec template has none.
  No trim, destination or byte figure moved.
  Extended again on the close-out pass, same base and rev · S7. The closing claim is weakened to
  what is true. The TRIMS are still uncontested, and no byte figure moves; what is shared is the
  two destinations. An earlier unit of this build lands its own moved paragraph in the `--attest`
  entry of the verbs pair this unit writes through `--park`, and the fork-item unit ordered later
  rewrites one sentence INSIDE the BUILD-METHOD passage this unit moves, following it into section
  8 of `memory/TEMPLATE-SPEC.md` rather than back into M3. Neither is a second trim of either
  passage, so AC9 and AC11 are unchanged; the record exists so a reader does not take
  "no other unit" as a claim about the destinations. The close-out verifier re-spelled AC3's
  malformed example token in the build's `EXMP` example family; it stays malformed, because the id
  grammar the arm exercises reads `[A-Z]+-[A-Za-z0-9]+-[0-9]+` and is blind to the family.

## 10. Reuse audit

The seam is the authorization scan's single `awk` over the README blob at BASE
(`tools/unattended/unattended.sh:1465-1471`), which unit 16 extends with `asks:` and this unit with
`may:`, plus leg check 19's re-parse of the same blob. `reuse_lookup.py "authority grant honoured
only from an owner committed record"` returns the `unattended` dossier's `.unattended.conf` seam and
generic record helpers; no seam in the lookup grades authority, and its scan reports `.sh` unscanned.
The recall probe surfaced `TOOL-aStandingWrit-1`, which names the property S4's third arm closes: a
run that lands a new build README authorizes the next run. Where DR and the source disagree: DR
§19.2's "union of `may` clauses" is superseded by F1 and D12-j, and no code implements either yet.

BASE is `fb07ca25`, origin/main, which HEAD `94fd2f54` merges without changing code. From
`abac6d59` to it, `tools/unattended/unattended.sh`, `tools/unattended/check-unattended.sh`,
`tools/unattended/lib-unattended.sh`, the protocol and BUILD-METHOD moved under aRatifiedRulings,
dPolishedVitrine, aDeferredBar, aReplayedCard and aProbedUnit: the stall probe and `--audit`, a
spec-token run at `--dispatch`, a brief-row path reader in the library, protocol fact 13 (the run's
local branch ref), and M6's rule that a pass runs no bar and no suite. None adds a `may:` key, a
grant token, or a walk of a run's own commits; the scan, check 19's re-parse, check 29 and
`ADV_HEAD` keep their shapes at new lines, `tools/push-main.sh`'s `--no-ff` reconcile is unchanged,
and no build README on `fb07ca25` carries `may:`. `tools/gate-legs.json` still carries no leg for
either unattended suite.

Recall terms used: `veto-2 governance-carrier authority grant owner-committed default-branch anchor
prompt-mode run-authored mandate scaffold delegated resolver`
