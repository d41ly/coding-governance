## Verdict: CHANGES REQUESTED — three blockers, all of them a measurement that no longer reproduces or a mechanism that cannot produce its own stated effect

**Tier-2 SPEC AUDIT · cSettledDocket · 2026-08-16 · the SPEC pass · reviewed range:
`1da67d9...HEAD` (`1da67d9..d607f4b`, 1 commit — one build folder, one README, six specs; no product
code changed)**

**Review shape:** raw 49 · confirmed 40 · refuted 9 · unverified 0 · **precision 0.82**.
The forty confirmed findings collapse to **21 distinct defects: 3 blockers · 5 high · 10 medium ·
3 low** — the collapse is heavy because the two most-hunted defects (spec 3's measurement, spec 5's
premise) were each independently landed on four times. Every finding below survived an adversarial
skeptic pass; nothing is carried as unverified.

These are DESIGNS, not code, so every finding is graded on the same three questions: **is the defect
real and still present at HEAD, does the measurement reproduce, and does the design close the defect
it names.** Where a numeric claim appears below, it was re-run against the tree during this pass and
the command is shown.

---

### The three things that must change before a builder touches this

1. **Spec 3's founding measurement does not reproduce** (§1). "4 of 18 fail §8, **0** fail §9-rev" is
   really **2 and 2** — and half the named repair list fails the *other* assertion, so S2's repair
   recipe cannot clear them and AC4 is unreachable.
2. **Spec 3's mechanism cannot produce spec 3's behaviour** (§2). `next` is a prefix cut; the two
   assertions to un-skip are the *last* two in the block. No placement of that one token yields the
   stated split. §4's "Nothing needs writing" is wrong, and the real edit is a block move in a
   verdict-epoch-dated file.
3. **Spec 5's defect is not real** (§3). `manifest-check.test.sh` already has a counter and already
   prints a summary. The measurement greped for the *other* suites' spelling. Built as written, S1+S2
   land a second counter and a second summary — the two-answers class this repo bans by name — in a
   gate's own proof.

### The shape of the rest

Two classes dominate, and both are about **specs asserting facts about code rather than reading it**.

**A named seam that does not exist** — four findings (§7 `mutate` in the wrong file, §14/§15 `core_of`
unreachable from a subprocess-driven suite, §12 `check_waivers` cannot return reasons, §18 check 17
joins the effective set). Reuse audits are the most-copied section in these six specs and the least
verified; three of them name a helper by a filename it is not in.

**An acceptance criterion that cannot fail or cannot pass** — five findings (§10 AC1's arithmetic
contradicts its own §4, §11's stranding mutation kills the observable it asserts, §13 AC4 is a no-op
under two of three branches, §16 AC1 demands silence a faithful fixture cannot deliver, §5's whole
acceptance set stays green with the hole open). Unit 3's AC set in particular is fully satisfiable
while the rule it exists to enforce stays bypassable.

**Where the build was right.** Unit 6 exists because the last review's closing paragraph named the
class — *take a terminal record, move the world around it, assert the leg stays silent* — and the
build turned that sentence into a unit. Unit 1's non-goal list correctly refuses to join a parked
fork to the directive registry. Unit 2 correctly refuses to take a fork it cannot cost. None of that
is undone by the findings below.

---

## 1 · BLOCKER · `memory/builds/cSettledDocket/spec/2026-08-16-spec-cSettledDocket-3.md:51` — the 4-of-18 measurement does not reproduce: it is 2 §8 failures and 2 §9-rev failures

**Claim.** §4 states "**4 of 18** — the Tier-1 population grew by three and the failures did not
move" and "**0** would fail the §9 rev-log assertion", then enumerates `aWrittenMethod-3`,
`aWrittenMethod-5`, `cBriefedPilot-9`, `cBriefedPilot-17`.

**Reproduced against the live tree.** A copy of the gate with line 626's `if (hdr ~ /Tier-1/) next`
neutralised, run over the real corpus:

```
sed 's|if (hdr ~ /Tier-1/) next|if (0) next|' tools/memory-tree/check-memory-hygiene.sh > /tmp/noskip.sh
bash /tmp/noskip.sh

  aWrittenMethod-3   (header rev-3 not logged in the §9 Revision log)
  aWrittenMethod-5   (header rev-3 not logged in the §9 Revision log)
  cBriefedPilot-9    (terminal Status with unresolved §8 Open questions)
  cBriefedPilot-17   (terminal Status with unresolved §8 Open questions)
```

Population, counted with the check's own selector (`SPEC_FORMAT_CUTOFF 2026-07-15`, `Tier-1` in the
status header): **25 in-scope, 18 terminal**. The denominator is the only half of the figure that
reproduces. The file list is right; **the attribution is inverted for half of it**.

**Why the split matters, not just the arithmetic.** `aWrittenMethod-3` and `-5` carry the older
eight-section canon — `## 7. Open questions`, `## 8. Revision log`, no `## 9.` — so the §8 range
never opens (`q8` stays empty, line 703's `q8 != ""` is false, the check is silent) while the §9 scan
finds no `^## 9\. Revision log` and fires on `!seen`. S2's repair recipe — "converting each bold-prose
resolution to the `###` sub-head form … one line changing `**Question — RESOLVED: answer.**`" — is
**inapplicable to two of the four**: they need a §9 section added or the sections renumbered, which is
exactly the ten-section ceremony Tier-1 exists to skip, and is not shape-only.

**Impact.** §5's "four documents gain a heading", §4's "one changed line per file" `git diff --stat`
proof, AC4 ("exits 0 over the whole real corpus after the four repairs") and AC5's shape-only framing
all fail as written. A builder following S2 makes two files green, re-runs, and finds two still red
with a repair the spec never budgeted. The same figure is copied into `README.md:69` and `:77` as
"4 of 15" (§21), so three documents now state one measurement and none is right.

**Fix.** Re-state §4 as **2 of 18 fail §8** (`cBriefedPilot-9`, `-17`) and **2 of 25 in-scope Tier-1
specs fail §9-rev** (`aWrittenMethod-3`, `-5`). Split S2 into two repair kinds — bold-prose → `###`
sub-head for the first pair, section renumber (`## 7.`→`## 8.`, `## 8.`→`## 9.`) for the second — and
note that `aWrittenMethod-3`'s §7 already uses a `### F1 …` sub-head with `**RESOLVED…**` in the
paragraph *below* it, so renumbering alone still reds it: the gate requires `RESOLVED` on the item
line. Re-state the "shape-only, one changed line per file" proof per kind.

**Left-shift gate.** The measurement was taken by reading, not by running. Every spec that pins a
corpus-wide count should carry the **command that produced it**, and the hygiene suite should gain a
fixture-free arm that runs the gate with a named assertion disabled and asserts the finding set — the
"neutralise the skip and diff the output" move above is six lines and would have produced the correct
split on the first attempt. Cheapest durable version: a `--only <assertion>` flag on
`check-memory-hygiene.sh` so a spec author can measure one predicate over the real corpus without
editing the gate.

---

## 2 · BLOCKER · `memory/builds/cSettledDocket/spec/2026-08-16-spec-cSettledDocket-3.md:20` and `:60` — moving the `next` cannot produce S1's behaviour: the two assertions to un-skip are the LAST two in the block

**Claim.** S1: "move the `Tier-1` skip BELOW the terminal-fork assertion and the §9 rev-log
assertion … Everything the skip currently protects — the canonical ten-section compare, the §10 body
assertion — stays Tier-2-only." §4: "Nothing needs writing — a `next` needs to move three assertions
later in the same awk program." §10 repeats "the unit moves one `next` statement."

**Reproduced by reading source order.** In `tools/memory-tree/check-memory-hygiene.sh`, below the
skip at **626**, in order:

| # | assertion | lines | S1 wants it |
|---|---|---|---|
| a | section canon compare | 628-636 | Tier-2 only |
| b | empty section bodies | 638-651 | Tier-2 only (unnamed by S1) |
| c | header rev vs §9 rev-log | 652-675 | **all tiers** |
| d | terminal status needs resolved §8 | 676-705 | **all tiers** |

`next` is a **prefix cut** in a linear awk rule body. The two blocks that must stay Tier-2-only
(a, b) *precede* the two that must grade every tier (c, d). No placement of a single `next` runs
(c)+(d) while skipping (a)+(b). Concretely: §4's literal "three assertions later" lands the skip
between (c) and (d) — the terminal-fork rule *the unit exists to enforce* stays skipped. Four later
lands it at the end of the block, where it is inert and (a)+(b) now grade Tier-1, contradicting S1's
own next sentence, non-goal 1, S4 and AC3 ("a Tier-1 spec with non-canonical `##` sections stays
SILENT").

Measured cost of getting it wrong that way: with the skip fully neutralised the canon fires on **four**
Tier-1 specs — `aPrunedCeremony-2`, `-3`, `aWrittenMethod-3`, `-5` — none of them in the repair budget.

**Impact.** The unit's Design section is mechanically wrong, and it is the section a builder will
follow literally. Both outcomes are bad: the cheap one silently leaves the target rule skipped and
ships a green build that closed nothing; the other reds four Tier-1 specs the build did not plan to
repair. §5's risk paragraph prices a one-token move, so the real risk — a **block reorder inside a
180-line awk program whose verdicts are dated by `KIT_MEMORY_TREE_VERSION`** — is unbudgeted.

**Fix.** Respec the edit: **hoist blocks (c) and (d) above line 626**, leaving the skip immediately
above the canon and empty-body assertions. Alternatively replace `next` with a `t1 = (hdr ~ /Tier-1/)`
flag and wrap (a)+(b) in `if (!t1) { … }`, which is the smaller diff and keeps source order stable —
but say which. Update §4's "three", §5's risk statement and "Files touched" accordingly, and fix S1's
enumeration of what the skip protects: it names the canon and "the §10 body assertion", but the
predicate at 638-651 is a **generic empty-section-body** check, not a §10 one.

**Left-shift gate.** This is spec review catching what a spec-writing convention should have caught:
any S-item naming a *mechanism* ("move a `next`") rather than an *outcome* ought to carry the
before/after line ranges. Machine-side, the durable one is smaller — the hygiene suite has arms for
Tier-2 §8/§9 but none pinning that Tier-1 is *silent* on them today. Add those two arms now, before
the change: they turn "the skip moved" from a claim into a diff of two arm verdicts, and they are the
paired Tier-1 twins S3 already asks for.

---

## 3 · BLOCKER · `memory/builds/cSettledDocket/spec/2026-08-16-spec-cSettledDocket-5.md:7` — the named defect is not real at HEAD: the suite already has a counter and already prints a summary

**Claim.** §1: `skills/session-kickoff/manifest-check.test.sh` "prints no assertion summary and
carries no counter", and "it is the only self-test leg on the bar with no executed-count signal".
AC1: "prints `PASS (` with its executed count on a green run, **where today it prints no count**".

**Reproduced against the file.**

```
skills/session-kickoff/manifest-check.test.sh:9    pass=0; fail=0
                                             :30   echo "ok   $name"; pass=$((pass+1))     # run()
                                             :51   echo "ok   $name"; pass=$((pass+1))     # runm()
                                             :515  … pass=$((pass+1))                      # inline
                                             :621  … pass=$((pass+1))                      # inline
                                             :661  echo "---- $pass passed, $fail failed ----"
```

The spec's own parenthetical measurement — zero `PASS (` output, zero `n=$((n+1))` sites — is
literally true and **measures the wrong thing**: it greps for the other three suites' spelling. The
suite counts; it just counts under a different name and prints under a different format.

**Impact.** S1 ("a counter in the suite's assertion helpers") and S2 ("a summary line printing the
executed count") are, as written, instructions to add a **second counter and a second summary** beside
the existing pair, in the two helpers that already carry one — two answers to one question, in a
file whose entire subject is a count that can silently disagree with itself. AC1 is false today and
is satisfiable by exactly that wrong implementation. §4's "this one is not known to route every
assertion through helpers" is answerable now and answers itself: `run()`/`runm()` carry all but two
arms. The unit-4-shaped inline-site contingency §4 budgets for is therefore dead weight.

**Fix.** Rewrite §1 to the reproducible state — *a `pass`/`fail` counter and a summary exist; no
`FLOOR_ASSERTIONS` pin does*. The genuine gap is **S3 alone**: `grep -rn FLOOR_ASSERTIONS` returns
only `check-memory-hygiene.test.sh:823`, `check-unattended.test.sh:861`, `unattended.test.sh:1366`.
Reduce S1/S2 to "floor the existing `$pass`, and — if format parity across the four suites is wanted
— reshape the existing `---- N passed, M failed ----` line into the shared `PASS (n assertions)`
form", note the two inline sites at :515 and :621 that already bypass the helpers, and restate AC1
against the current output rather than against a void. Re-derive the Tier and the size estimate from
that: this is a two-line unit, not a five-item one.

**Left-shift gate.** A spec whose §1 rests on an absence must state the **command and its exit status**
(`grep -c 'pass=$((pass+1))' <file>` → 4), because a shape-specific grep proves the shape is absent,
never the property. Machine-side: the four self-test legs now differ in counter name, summary format
and floor presence, and nothing joins them. Add a leg — or an arm in `run-gates.test.sh` — asserting
every `*.test.sh` named in `tools/gate-legs.json` prints a count in one agreed shape. That single
predicate answers this unit's question mechanically, and would also have caught §17.

---

## 4 · HIGH · `memory/builds/cSettledDocket/spec/2026-08-16-spec-cSettledDocket-1.md:21` — S2 imports half of `--waive`'s reason contract: no bypass-flag refusal, no newline refusal

**Claim.** S2 makes `--park`'s reason "REQUIRED and non-empty, refused with the same argument unit 3
made for `--waive`". Nothing in §2, §4, §5 or AC1-AC6 mentions the bypass flag or an embedded
newline — the other two halves of that argument.

**Reproduced at source.** `park()` (`tools/unattended/unattended.sh:1260`) writes
`printf '\n%s %s · item %s · reason %s\n'` with `$4` **verbatim** into a line-oriented, append-only
region. Its existing reason-bearing callers guard it:

- `check_waivers` fail 41 (`unattended.sh:489-496`) — refuses a `BYPASS_BAN` spelling **and** an
  embedded newline;
- `verb_abort` fail 36 (`:934-937`) — refuses the bypass spelling;
- `verb_close --override` (`:1142-1173`) — guards **neither**, so the surface is not brand new.

Both hazards are live. Check 11 (`tools/unattended/check-unattended.sh:371`) is a whole-file
`grep -qF -- "$BYPASS_BAN"` with `BYPASS_BAN="--no-verify"` (`.unattended.conf:19`). Check 17 selects
parked rows line-by-line via `^[0-9][0-9-]*T[0-9:]*Z waiver · item [^ ]* · reason ` (`:413`), and its
own comment at `:378` says only the waiver kind is joined — so a forged `override · item gates-green
· reason …` line, injected through a newline in a reason, is graded by **nothing** and surfaces in
the wrap-up derivation as a DoD override that never happened.

**Impact.** `--park` is the first reason writer whose text comes from the **agent, mid-run** rather
than the owner. With S3 refusing on a terminal record and non-goal 3 refusing `--unpark`, a reason
that spells `--no-verify` reds the merge bar **permanently** on a record no verb can rewrite — the
exact wedge unit 6 of this same build exists to catch. S4's free-text `--item` is the same vector.
The spec cites unit 3's argument and takes only the cheapest third of it.

**Fix.** Add an S-line routing **both** `--item` and `--reason` through the identical refusal
`check_waivers` uses — bypass-flag substring plus a `wc -l` newline test — evaluated before anything
is written, reusing fail 41's exact message text (`check-arms.py` keys arms on failure text). Add two
AC arms: a newline-bearing reason is refused and the record is byte-identical afterwards (the
`git hash-object` shape AC2 already uses), and a bypass-spelling reason is refused. Add the matching
arms to S6's list.

**Left-shift gate.** The guards live in each *verb's* path, so every new `park()` caller re-inherits
nothing. Move the two refusals **into `park()` itself** — one guard where all callers route through
is a smaller diff than a guard per verb, and it retro-fixes `verb_close --override`, which has been
unguarded all along. Then add the arm that actually enforces it: a derived count of `park()` call
sites pinned against the count of sites reached through the guarded entry, so a sixth caller reds
until it routes correctly.

---

## 5 · HIGH · `memory/builds/cSettledDocket/spec/2026-08-16-spec-cSettledDocket-3.md:32` — S5's "after this it is true" does not hold: the §8 assertion is keyed on the literal heading `## 8. Open questions`, and Tier-1 is canon-exempt

**Claim.** S5 keeps `TEMPLATE-SPEC.md`'s "machine-checked" wording "because after this it is true".

**Reproduced.** `check-memory-hygiene.sh:681` opens the terminal-fork range only on
`L ~ /^## 8\. Open questions/`. With no match, `q8` stays empty and line 703's `q8 != ""` is false —
**silent**. Non-goal 1 keeps Tier-1 exempt from the section canon by design, so a Tier-1 spec may
legally number Open questions anything it likes. `aWrittenMethod-3` and `-5` are that shape today:
with the skip neutralised they emit canon and §9-rev findings and are **silent on §8**.

**Impact.** Renumbering those two greens the corpus while leaving the rule bypassable by any future
Tier-1 spec doing a thing the same spec explicitly permits. `TEMPLATE-SPEC`'s "machine-checked" claim
stays false for the tier the unit exists to fix — the defect is not closed, only its current
instances are. And the acceptance set cannot see it: **AC1-AC5 all pass with the hole open**. AC1 uses
a correctly-numbered §8; AC3 only asserts silence on non-canonical sections. This is the
"unfalsifiable acceptance criterion" class in its most expensive form — a fully green AC set over a
design that does not close its own defect.

**Fix.** Key the Tier-1 §8/§9 assertions on the section **title** rather than its number —
`^## [0-9]+\. Open questions` / `^## [0-9]+\. Revision log`, closing on the next `^## ` — or add a
Tier-1 rule that a terminal spec must carry a recognisable Open-questions section at all. Add an AC
with a Tier-1 fixture whose Open questions sits at `## 7.` and whose fork is unresolved; that arm is
the one that distinguishes "the rule now runs on Tier-1" from "the rule now runs on Tier-1 specs that
happen to be numbered like Tier-2 ones".

**Left-shift gate.** Any predicate keyed on a section **number** in a corpus where numbering is
tier-conditional is a vacuity waiting to happen. Cheap standing arm: for every terminal spec, assert
the §8 range **opened** — a spec where the range never opens should print "no Open questions section
found", not nothing. Silence and pass are the same byte today, which is why this survived.

---

## 6 · HIGH · `memory/builds/cSettledDocket/spec/2026-08-16-spec-cSettledDocket-5.md:96` — §10 copies a counter shape whose variable name is already a live global in the target file

**Claim.** §10: the counter shape is "copied deliberately rather than varied" from
`TOOL-cBriefedPilot-23`. That shape names the counter **`n`** and prints `PASS ($n assertions)` —
`unattended.test.sh:17`/`:1368`, `check-unattended.test.sh:863`,
`check-memory-hygiene.test.sh:825`.

**Reproduced.** `skills/session-kickoff/manifest-check.test.sh:500` is
`n=$(git -C "$R" rev-list --count HEAD)`, tested at `:501` with `[ "$n" -ne 4 ]`. It is a **global** —
the only `local n` in the file is at `:67`, inside a function.

**Impact.** Adopting `n` verbatim silently discards every increment accumulated before line 500 and
restarts the counter from 4. AC2 ("`FLOOR_ASSERTIONS` … equals the measured count at build time")
then pins the floor to that truncated total, and the pin **passes while being a lie** — the exact
failure mode unit 4's spec says this file class is riskiest for, landed in the unit that is supposed
to be the safe one.

**Fix.** Reuse the existing `$pass` (no new variable, no collision — and see §3, which removes the
need for a new counter entirely), or name the new counter something not already bound in this file
and say so in §10 instead of "copied deliberately rather than varied". Add an arm asserting the
printed count is strictly greater than the commit-count arm's value, so a future re-collision reds.

**Left-shift gate.** "Copy the shape" is a reuse claim, and reuse claims in this build are the least
verified section (§7, §12, §14, §15, §18 are all the same class). The mechanical version is a lint
already justified by the last review's §10: flag any variable a suite assigns at top level that is
also assigned inside a helper — one grep, and it catches shadowing before it eats a floor.

---

## 7 · HIGH · `memory/builds/cSettledDocket/spec/2026-08-16-spec-cSettledDocket-4.md:110` — the reuse audit names `mutate`, which does not exist in the only file this unit touches

**Claim.** §10: "`mutate` from the same unit is reused for S4's fixture edit", and "No new helper is
added". §4:74 pins Files touched to "`check-memory-hygiene.test.sh` only, plus the two backlog rows".

**Reproduced.** `mutate() {` is defined at `tools/unattended/check-unattended.test.sh:119` and
`tools/unattended/unattended.test.sh:29` — nowhere else. `grep -n mutate
tools/memory-tree/check-memory-hygiene.test.sh` returns **nothing**. The three claims cannot all hold.
Sibling spec 5 §10:98-101 states the true population ("it lives in the two unattended suites") and
declines to copy it as "a third implementation of a five-line helper" — so **this build carries two
contradictory reuse claims about one helper**.

**Impact.** Concrete, and it hits the one arm that matters. S4's stranding arm is the only thing
bounding a ~50-site mechanical sweep of a gate's own proof. Without `mutate`'s `git hash-object`
before/after guard — the guard its own comment at `:115-118` exists to explain — a stranding
mutation that silently matches nothing makes S4 **pass by finding nothing**. That is the
fixture-passes-vacuously class, in the arm whose job is proving the widened count is honest.

**Fix.** Replace the `mutate` claim with what the arm will actually do: an inline `git hash-object`
before/after comparison on the copied suite — the same choice spec 5 §10 makes, for the same stated
reason — or add the copy to "Files touched" and argue the third implementation there. Pick one and
make both specs say it.

**Left-shift gate.** Every §10 reuse claim in this build that names a symbol should name the
**file:line it is defined at**. Three of the six specs got this wrong (§7, §14, §12). That is cheap to
enforce mechanically: a hygiene arm that any backticked identifier in a §10 reuse audit resolves to a
definition in a tracked file would have caught all three at commit time.

---

## 8 · HIGH · `memory/builds/cSettledDocket/spec/2026-08-16-spec-cSettledDocket-1.md:37` — the non-goal's premise is false: `fork` is not a declared parked kind

**Claim.** Non-goal 1 rules out "a fifth parked kind" on the grounds that "`fork` is already declared
in §2".

**Reproduced.** `grep -ciw fork memory/guides/UNATTENDED-PROTOCOL.md` → **0**. §2 item 3 enumerates
the four kinds in prose: "a parked **DECISION** … an **ABORT** reason, a recorded DoD **OVERRIDE**,
and an owner directive **WAIVER**". The three implemented kind strings each match their prose name:
`abort` (`unattended.sh:957`), `waiver` (`:1054`), `override` (`:1173`). The unwritten fourth is
therefore **`decision`**.

**Impact.** S1 ("writing through the existing `park()` with kind `fork`") and AC1
(`grep -c 'fork · item '`) mint a token the contract never spells — which is precisely the fifth-kind
outcome the non-goal says it is avoiding, reached through the sentence that justifies the
non-goal. S7's "the protocol's §2 gains the verb beside the kind it writes" has no kind to sit beside.
Nothing on the bar joins park kinds to §2, so the drift is silent: check 17's selector simply ignores
non-waiver lines.

**Fix.** Use `decision` — §2's own word — in S1, AC1's grep and S7. If `fork` is genuinely wanted,
drop the non-goal and spec the §2 rename in both protocol copies as scope, naming the parity leg in
Gates.

**Left-shift gate.** The kind vocabulary is declared in prose in one file and implemented as string
literals in another, joined by nothing. Add the join to `check-unattended.sh` in the shape check 16
arms D/E already use: derive the kind set from `park()`'s call sites and assert each token appears in
§2, both directions. It is the only gate pattern in this kit that compares a declaration to code
rather than a copy to a copy, and this is its next obvious customer.

---

## 9 · MEDIUM · `memory/builds/cSettledDocket/spec/2026-08-16-spec-cSettledDocket-1.md:23` — S3 leans on `refuse_if_terminal`, which returns 0 when the record does not exist

**Claim.** S3 makes `refuse_if_terminal` the record-state guard; §10 calls it "the single answer to
'may this verb touch this record'".

**Reproduced.** `refuse_if_terminal` (`unattended.sh:662`) opens with `[ -f "$rel" ] || return 0` at
`:664`. `park()` (`:1260-1262`) appends with `>>`, which **creates** the file. Every sibling verb
carries its own `[ -f "$rel" ] || fail 10` immediately before the call — `--phase` (`:820`),
`--landed` (`:886`), `--abort` (`:924`), `--status` (`:1089`), `--close` (`:1137`) — and the driver's
comment at `:1045-1046` documents this exact `>>`-creates-the-file hazard.

**Impact.** `--park <slug>` issued before `--preflight` writes a bare `RUN.md` holding one parked
line: no generated marker pair, no `base:`, no `phase:`. Swept into a commit it reds check 8
(malformed generated markers, unexempt on every phase), check 9 (records no BASE) and check 7 (a
phase-less file is not in `PHASES_TERMINAL`, so it counts as a second LIVE run) — **permanently**,
since no verb rewrites a record it cannot parse. No S-item, AC or test arm covers it.

**Fix.** Add a scope line: `--park` refuses when the run-state file does not exist, with its own
failure text, evaluated before `park()` is reached; and an AC that `--park` on an unknown slug writes
nothing and leaves the tree with no new file. Correct §10's "single answer" sentence.

**Left-shift gate.** Five verbs hand-repeat `[ -f "$rel" ] || fail 10` and the sixth will forget.
Fold the existence test **into `refuse_if_terminal`** behind a flag, or into `park()` — one guard at
the shared seam. Then the derived arm in §10 below becomes worth having.

---

## 10 · MEDIUM · `memory/builds/cSettledDocket/spec/2026-08-16-spec-cSettledDocket-1.md:130` — the standing guard that forces new verbs into the terminal-refusal drive list keys on phase writers, so `--park` is invisible to it

**Claim.** §10 leans on `refuse_if_terminal` being "called by all five verbs" as the coverage argument.

**Reproduced.** `unattended.test.sh:1321` derives `writers=$(grep -c 'set_fact "$rel" phase' "$SCRIPT")`
and pins it at 5, commenting that "a sixth phase writer reds this arm until it is added to the drive
list, which is the property a hand-written list cannot have." In the driver there are exactly five
`set_fact "$rel" phase` sites (854, 900, 955, 1044, 1180) and exactly five `refuse_if_terminal`
callers (831, 887, 938, 967, 1138).

**Impact.** `--park` writes a parked entry, not a phase. After unit 1 there are **six**
`refuse_if_terminal` callers and still **five** phase writers: the arm stays green, the new verb never
enters the terminal drive loop, and the guard whose stated purpose is "the property a hand-written
list cannot have" quietly fails to have it.

**Fix.** Widen the derived population to `grep -c 'refuse_if_terminal "$rel"'` and add `--park` to the
drive list — or state in §10 that S6's terminal arm is hand-written and unprotected by the derived
guard, so the next reader does not inherit a false assurance.

**Left-shift gate.** A derived guard is only as good as the population it indexes. When a suite pins
`grep -c <pattern>`, the pattern should be the one naming the **property under test**, not a proxy
that happens to correlate today. Worth a one-line comment convention: every derived pin states which
property it stands in for.

---

## 11 · MEDIUM · `memory/builds/cSettledDocket/spec/2026-08-16-spec-cSettledDocket-4.md:85` (and spec 5 `:73`) — AC2's stranding mutation kills the observable AC2 asserts

**Claim.** AC2: "stranding a block of INLINE arms past an early `exit` makes the suite refuse with
`arms are UNREACHABLE rather than absent`." Spec 5's AC3 copies the mutation verbatim.

**Reproduced.** `check-memory-hygiene.test.sh` ends at 826: the floor test carrying that message is
**824**, `PASS (…)` is **825**, `exit "$st"` is **826**. A top-level `exit` inserted anywhere earlier
terminates the script **before 824**, so the floor never evaluates and the refusal is never printed.
Same tail layout in `check-unattended.test.sh` (861-863) and `unattended.test.sh` (1366-1368).
Grepping the phrase repo-wide returns exactly those three floor lines and nothing else — **no
existing arm exercises the branch**, so this is the first attempt and it is specced against an
unreachable observation.

**Impact.** The one arm proving the widened floor is honest cannot produce its own evidence. Two specs
in this build carry it.

**Fix.** Respec the mutation to one that strands arms while leaving the tail reachable — wrap the
block in `if false; then … fi`, delete it, or use a `return` inside a helper — and state the
observable as the printed refusal **plus** a non-zero exit. Fix both specs in one pass.

**Left-shift gate.** The floor's own message ("look for a block stranded past an exit") describes a
mutation that would also strand the floor. That is worth an arm in each of the three floored suites
now, independent of this build: it costs three lines and converts a message nobody has ever seen into
one somebody has.

---

## 12 · MEDIUM · `memory/builds/cSettledDocket/spec/2026-08-16-spec-cSettledDocket-1.md:28` — S5 mis-describes `--waive`'s re-preflight rule: it compares handle SETS and never compares reasons

**Claim.** S5 makes `--park` "IDEMPOTENT on a byte-identical `(item, reason)` pair, matching
`--waive`'s re-preflight rule".

**Reproduced.** `recorded_waivers` (`unattended.sh:465-470`) sed-extracts only the **handle**;
`check_waivers`' refusal 38 (`:515-517`) compares the sorted requested handle set against the recorded
handle set — reasons never enter it; `verb_preflight` (`:1052`) parks only when
`[ -z "$(recorded_waivers "$rel")" ]`, i.e. skips parking entirely once **any** waiver is recorded. A
re-preflight with the same handle and a different reason passes and is silently not re-parked.

**Impact.** `--waive`'s rule is handle-set equality, not `(item, reason)` idempotence, so S5 points a
builder at a seam with different semantics — and `recorded_waivers` hardcodes the `waiver` kind and
strips the reason, so it cannot supply what S5 needs.

**Fix.** State S5's rule on its own terms — skip when a `<kind> · item <h> · reason <r>` line already
exists verbatim — drop the "matching `--waive`" claim, and note that a new reader is required.

**Left-shift gate.** Same class as §7 and §14: a reuse claim naming behaviour rather than a line. The
§10 identifier-resolves rule above covers the symbol half; this half needs the convention that a spec
citing another verb's *rule* quotes the predicate.

---

## 13 · MEDIUM · `memory/builds/cSettledDocket/spec/2026-08-16-spec-cSettledDocket-2.md:62` — branch A is mis-costed: `core` is read by arm B as well as arm A

**Claim.** §4's branch A and §10 both price it as "arm A's existing `comm` join with one variable
widened" — four characters.

**Reproduced.** `check-unattended.sh:482` builds `core=$(printf '%s\n' $DIRECTIVES_CORE | sort -u)`
**once**, above both guards, and reads it twice: arm A's `comm -23`/`comm -13` joins (`:508-509`) and
arm B's `for pair in $core; do sec=${pair#*:}; grep -qE "^## $sec( |$)" "$M/guides/BUILD-METHOD.md"`
(`:517-521`).

**Impact.** Widening `core` to the effective set makes every project-declared extra handle
additionally required to cite an `M<n>` section that exists in the **kit's** `BUILD-METHOD.md` — a
second, differently-worded refusal (fail 16, "a directive points at a build-method section that does
not exist") that would still fire for a project whose extra directive points at its own method
document. The branch analysis never mentions it, and the owner is being asked to pick between
branches on these costs. (Arm B is guarded by `[ -f "$M/guides/BUILD-METHOD.md" ]`, so it is
conditional, not universal — the omission from a fork's cost analysis stands.)

**Fix.** Split the variable in the cost analysis: branch A must either introduce a separate
`effective` for arm A, or accept that arm B's section-resolution rule extends to extras. Re-cost
accordingly, and correct §10.

**Left-shift gate.** A fork spec that prices a change as "one variable widened" should list that
variable's **read sites**. `grep -n '\$core'` is the whole audit. Worth making a §4 convention for any
spec whose deliverable is a costed fork.

---

## 14 · MEDIUM · `memory/builds/cSettledDocket/spec/2026-08-16-spec-cSettledDocket-6.md:124` — the reuse audit names `core_of`, which the test suite cannot reach

**Claim.** §10: `PHASES_TERMINAL` is read from the driver "through the leg's existing `core_of`, not
re-declared, so the fixture's idea of terminal cannot drift from the kit's".

**Reproduced.** `core_of()` is defined at `tools/unattended/check-unattended.sh:64` and consumed at
`:75-78` **inside that script's own process**. The leg has no source guard and runs all eighteen
checks at top level, so sourcing it to reach the helper would execute it.
`check-unattended.test.sh` copies the leg into `$TMP` (`:26`) and drives it as a subprocess via
`run() { bash "$SCRIPT" 2>&1; }` (`:113`); there is no `source`/`.` anywhere in the suite, and
`PHASES_TERMINAL` appears in it **zero** times. The suite's established idiom for a driver constant is
its own grep — `grep '^PHASES_CORE=' "$HERE/unattended.sh"` at `:81-83` and `:158-162` — and it
already hardcodes `LANDED`/`ABORTED` at `:251`, `:271`, `:373`, `:386`.

**Impact.** The stated no-drift guarantee has no mechanism behind it. A builder following §10 will
either source the leg (executing it), invent a third idiom, or — most likely — hardcode a terminal
phase name, which is **the frozen-versus-live shape this very unit exists to catch**.

**Fix.** Point the reuse audit at the suite's real idiom (grep the driver constant and derive), or
state that `core_of` must first be factored into a sourceable file — which is a scope item, not a
reuse.

**Left-shift gate.** Covered by §7's identifier-resolves rule, with one addition worth having on its
own: a helper a test suite is told to reuse must be **callable from the suite's process model**. The
cheap mechanical form is the source guard the leg lacks — add `[ "${BASH_SOURCE[0]}" = "$0" ] ||
return 0` around the check body and the reuse becomes real rather than aspirational.

---

## 15 · MEDIUM · `memory/builds/cSettledDocket/spec/2026-08-16-spec-cSettledDocket-6.md:75` — AC1 demands total leg silence after five moves, but two of them red check 16 by construction

**Claim.** AC1: with a TERMINAL record, **each** of the five moves leaves
`bash tools/unattended/check-unattended.sh` silent.

**Reproduced.** "Add a directive to the core set" widens `DIRECTIVES_CORE` in the driver. Check 16
arm A joins that constant — read via `core_of` at `:77` — to `SKILL.template.md`'s table in **both**
directions (`check-unattended.sh:508-510`), with no run population and **no terminal exemption**. So
the move reds "a directive is declared in the registry and absent from the Skill's table" regardless
of any run's phase. "Add a phase to the vocabulary" reds arm D the same way against the protocol's
run-order paragraph. The move table names only check 17 and check 4 as possible collisions, and §4's
"Each row is one `mutate`" puts the two-file edit that would keep it silent out of scope.

**Impact.** AC1 fails on a **faithful** fixture. A builder chasing silence will either widen the moves
silently or exempt check 16 on terminal records — which is exactly the over-wide exemption AC4 exists
to forbid, in the same unit. (The phase half is weaker: §10's `pedit` note anticipates editing both
protocol copies, which also satisfies arm D. The directive half alone establishes the defect.)

**Fix.** Either compose those two moves so they stay internally consistent — add the Skill table row
and the protocol run-order token in the same mutation — or scope AC1 **per move** to the check named
in that row's collision column, asserting silence only for the frozen-versus-live checks under test.

**Left-shift gate.** The move table already has a collision column; it was filled by recall rather
than by running the leg. Before the fixture is written, run each move once against a LIVE record and
record the actual finding set — that is the control S3 already requires, used one step earlier.

---

## 16 · MEDIUM · `memory/builds/cSettledDocket/spec/2026-08-16-spec-cSettledDocket-4.md:83` — AC1's arithmetic contradicts its own §4 and cannot pass: three inline sites sit inside `for` loops

**Claim.** AC1: "the count equals the previous count plus the number of inline sites edited."
§4:52-54 of the same spec: "a site inside a loop increments per iteration, which is correct."

**Reproduced.** `check-memory-hygiene.test.sh` has inline `st=1` assertions at `:686` (inside
`for c in 3 4 5 8 12`), `:798` (`for p in MEMORY.md IN-FLIGHT.md README.md in-flight journal`) and
`:803` (`for r in` five registries) — three sites, five iterations each. `grep -c 'st=1'` is 60,
matching the spec's own site measurement. A correct sweep therefore raises the runtime count by
`(sites - 3) + 15`, never by the site count.

**Impact.** AC1 is unsatisfiable as written, and it is the **one derived cross-check** §4:60-62 offers
against a mis-edited ~50-site sweep ("a derived cross-check rather than an eyeball"). A builder held
to it either hoists the increment out of the loop — making a five-iteration arm count once,
reintroducing the exact under-count the unit exists to remove — or fudges the re-pinned
`FLOOR_ASSERTIONS=83` (`:823`), turning a ratchet into a number nobody derived, in the file whose
whole subject is a count that was a lie.

**Fix.** Restate AC1 with an explicit loop term: the count rises by the number of non-loop sites
edited plus the summed trip counts of the looped ones, with the three enumerated in the commit
message. Or keep only the `>= FLOOR_ASSERTIONS` and AC3 pair and drop the equality.

**Left-shift gate.** Any AC asserting an arithmetic identity over a count should be **run once against
the current tree** while the spec is written — the before/after delta here is computable today. The
durable version is smaller: the suites' `PASS (n assertions)` line should print sites and executions
separately, so a loop's contribution is visible rather than inferred.

---

## 17 · MEDIUM · `memory/builds/cSettledDocket/spec/2026-08-16-spec-cSettledDocket-5.md:8` — "the only self-test leg on the bar with no executed-count signal" is false; three siblings have none

**Claim.** §1's scoping sentence.

**Reproduced.** Surveying the self-test legs `AGENTS.md` enumerates alongside `manifest-check.test.sh`,
all of which appear in `tools/gate-legs.json`:

```
tools/memory-tree/check-verdict-epoch.test.sh:168     PASS — check-verdict-epoch: all arms held
tools/workflows/check-verifier-fanout.test.sh:81      PASS — check-verifier-fanout: all arms held
tools/workflows/check-review-join.test.sh:168         PASS — review-join + workflow-syntax gates: all arms held
```

Zero increment sites, zero `FLOOR_ASSERTIONS`, **no number** in any of the three PASS lines.

**Impact.** Combined with §3, the unit as scoped upgrades the one leg that **already reports a count**
and leaves the three that genuinely report none. The stranded-arm class stays unobservable exactly
where the spec claims to have closed it.

**Fix.** Widen the scope to the three legs that actually have no count signal, or narrow §1 to "the
one leg with a count but no floor" and file the other three as their own backlog row.

**Left-shift gate.** Same one as §3: a leg over `tools/gate-legs.json` asserting every `*.test.sh` in
the manifest prints a count in one agreed shape. That predicate answers §3, §6 and §17 at once and is
the highest-value gate this review can suggest.

---

## 18 · MEDIUM · `memory/builds/cSettledDocket/spec/2026-08-16-spec-cSettledDocket-6.md:87` and README `:58` — the only recorded inter-unit dependency rests on a constant neither unit touches

**Claim.** §5: unit 6 depends on unit 3 because "both touch `ARMS_FLOORS`, so building them in
sequence avoids two units racing one constant." The README roster's "Depends on: 3" cell inherits it.

**Reproduced.** `ARMS_FLOORS` (`.memory-tree.conf:87`) pins `<gate>:<branches>:<armed>` for five
**GATE** scripts, parsed at `check-arms.py:201` and enforced strictly one-sided upward (`:280-286`
fires only when `got < want`); `check-arms.py:121` excludes `*.test.sh` from the gate population
entirely. Unit 6's Files touched (`:83`) is `check-unattended.test.sh` plus **its own**
`FLOOR_ASSERTIONS` (`check-unattended.test.sh:861`) — a different constant in a different file; that
gate is pinned 60:60 and adding test-side arms cannot move it. Unit 3 moves an awk `next` inside
check 12's program, which uses `print`, not the shell `fail()` the discovery predicate keys on — its
14:14 entry does not move either. `python tools/memory-tree/check-arms.py` exits 0 today.

**Impact.** Two independent units are serialised in the roster for a fictitious reason, and a reader
will believe the pair was checked for constant collisions when the real shared surfaces — two
shrink-only re-pins in different files, and unit 3's blast radius over the corpus unit 6 fixtures
against — were never examined. Spec 3's conditional "`.memory-tree.conf` if `ARMS_FLOORS` moves"
(`:76`) goes with it.

**Fix.** Delete the `ARMS_FLOORS` rationale from §5 and the `3` from README `:58`, or replace both
with the real ordering argument if one exists (unit 3's repairs landing before unit 6's fixture is
written is a plausible one — write that down instead).

**Left-shift gate.** A roster "Depends on" cell is a claim about shared surface. Make it carry the
surface: `| Depends on | Shared surface |`. An empty second column is then visibly an assertion
nobody could name, which is the whole finding.

---

## 19 · LOW · `memory/builds/cSettledDocket/spec/2026-08-16-spec-cSettledDocket-2.md:113` — AC4 cannot fail under branches A or C

**Claim.** AC4: `bash tools/unattended/check-unattended.sh` is silent on this repo, which declares
extras.

**Reproduced.** This repo's `.unattended.conf:62` is `DIRECTIVES_EXTRA=""`. Branch A widens a join by
a variable that is empty — byte-identical set, no behaviour change. Branch C edits `check_waivers`,
which lives in the **driver** (`unattended.sh:472`), not in `check-unattended.sh` at all, so AC4's
subject is untouched. Only branch B gives AC4 anything to grade.

**Impact.** The unit's **only** real-tree blast-radius criterion is satisfied before any code is
written, for two of the three branches.

**Fix.** Replace AC4 with a fixture that DECLARES an extra handle in a scratch tree and asserts the
branch-specific outcome — red for A, green-plus-visible for B, refusal-at-`--waive` for C — keeping
the empty-extras case as a control rather than as the criterion.

**Left-shift gate.** An AC whose subject is "this repo" is only a criterion if this repo exercises the
path. Worth a spec-writing rule: any AC naming the live tree states the tree value it depends on
(`DIRECTIVES_EXTRA=""` here), which makes the vacuity self-evident in the sentence.

---

## 20 · LOW · `memory/builds/cSettledDocket/spec/2026-08-16-spec-cSettledDocket-1.md:61` — §4's asymmetry argument cites the wrong registry

**Claim.** §4: "Check 17 joins a WAIVER's item to `DIRECTIVES_CORE`."

**Reproduced.** `check-unattended.sh:395` is
`case " $DIRECTIVES_CORE $DIRECTIVES_EXTRA " in *" $wh:"*)` — check 17 joins to the **effective** set.
That is the exact fact **unit 2 of this same build** turns on: check 16 arm A builds `core` from
`DIRECTIVES_CORE` alone (`:483`) while check 17 uses CORE+EXTRA.

**Impact.** The asymmetry conclusion (a rule with a registry versus a question with none) survives;
the source fact cited for it is wrong and contradicts the sibling spec, which will mislead anyone
reading units 1 and 2 together — and they are meant to be read together.

**Fix.** Name the effective set and cross-reference unit 2, so the two units describe one registry
consistently.

**Left-shift gate.** Two specs in one build state opposite facts about one line. A build-level
consistency pass over the specs' factual claims is the human version; the mechanical version is §7's
identifier-resolves rule extended to constants — a spec naming `DIRECTIVES_CORE` beside a `check <n>`
should resolve to that check's actual read.

---

## 21 · LOW · `memory/builds/cSettledDocket/README.md:69` and `:77` — the provenance table and Risk 1 carry the same mis-split as §1, at a third figure

**Claim.** `:69` — "4 of 15 Tier-1 terminal specs would fail the §8 rule if the skip were lifted";
`:77` repeats it as the pre-merge measurement inside Risk 1.

**Reproduced.** Per §1: the split is **2 §8 + 2 §9-rev**, over 18 terminal Tier-1 specs. The four
filenames are right; the classification is not.

**Impact.** Risk 1 presents a single repair class where there are two, and understates the change's
shape in the one paragraph an owner reads before approving the risk. Three documents now state one
measurement — spec 3 §4, README `:69`, README `:77` — and none is right.

**Fix.** Update both README figures with the split once spec 3 §4 is corrected, or replace them with a
pointer to the spec so the measurement has **one home** rather than three.

**Left-shift gate.** A number that appears in a spec and in the build README is a number that will
drift. The charter already refuses to spell live counts in prose for exactly this reason
("`python tools/codebase-map/reuse_lookup.py` prints the live pair"). Extend that habit to build
records: the README's provenance column should name the command, not the answer.

---

## What this pass says about the build's method

**The specs were written from memory of the code, not from the code.** Three of the six carry a
measurement that does not reproduce (§1, §3, §21) and five carry a reuse claim naming a seam that is
not where the spec says it is (§7, §12, §14, §18, §20). Every one of those was found by running a
command that fits on one line. The build's own §4 sections repeatedly promise "a derived cross-check
rather than an eyeball" and then supply the eyeball. **The single cheapest change to this method is a
rule that every numeric or locational claim in a spec ships with the command that produced it** — not
for the reader's benefit, but because writing the command is what forces the author to run it.

**The measurement idiom that failed twice is "grep for the shape".** Spec 5 concluded a counter was
absent because the other suites' spelling was absent (§3). Spec 3 concluded four files failed one
assertion because four files appeared in one earlier run (§1). Both are shape-matching standing in for
property-checking, and both produced a confident wrong number that then propagated into acceptance
criteria and a README risk paragraph. The fix is the same in both: **run the predicate, read its
output**, rather than grepping for what its output would look like.

**Acceptance criteria in this build grade the change, not the defect.** §5 is the sharpest case — unit
3's entire AC set passes while the rule it exists to make true stays bypassable by any Tier-1 spec
that renumbers a section. §19, §11, §15 and §16 are the same disease in milder forms: an AC that is
vacuous, one whose observable is destroyed by its own mutation, one that demands an outcome a faithful
fixture cannot produce, and one whose arithmetic contradicts its own design note. A useful standing
question for the AC section: **name the wrong implementation this criterion would reject.** Four of
these five have no answer.

**Where the previous review's lesson did land.** Unit 6 exists because the last pass's closing
paragraph named the frozen-versus-live class and asked for a standing fixture. The unit is the right
unit; §14, §15 and §18 are execution defects in it, not a case against it. Fixing those three is much
cheaper than the class it closes, and it is the one unit here whose value does not depend on any of
the other five.
