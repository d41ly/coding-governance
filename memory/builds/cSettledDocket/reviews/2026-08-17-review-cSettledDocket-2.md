**Reviewed range: `1da67d9...HEAD`** — the cumulative diff, 4 commits (`d607f4b f164b83 444bd26 977107b`), 38 files, +2583/-63.

## Verdict: CHANGES REQUESTED — two blockers, both a unit whose central claim is false and nothing on the bar can see it

**Tier-2 CLOSING REVIEW (M8) · cSettledDocket · 2026-08-17 · the CODE pass · reviewed range:
`1da67d9...HEAD` (`1da67d9..977107b`, 4 commits — 38 files, +2583/-63; all six units built, bar GREEN
57/57 at HEAD on a clean tree)**

**Review shape:** raw 46 · confirmed 43 · refuted 3 · unverified 0 · **precision 0.93**.
The forty-three confirmed findings collapse to **20 distinct defects: 2 blockers · 3 high · 7 medium ·
8 low**. The collapse is heavy — four independent landings on the MOVE-2 fixture, four on the
`--status` arm, four on the stray increment, three on the `--park` bypass screen — because the two
hunted classes are exactly where the defects are. Every finding survived an adversarial skeptic;
nothing is carried as unverified.

This is CODE, so every finding was re-run against the tree during this pass. The five named suites
were executed at HEAD and each floor matches its measured count:

```
tools/unattended/unattended.test.sh            PASS (273 assertions)   FLOOR 273
tools/unattended/check-unattended.test.sh      PASS (174 assertions)   FLOOR 174
tools/memory-tree/check-memory-hygiene.test.sh PASS (137 assertions)   FLOOR 137
tools/check-testsuite-counts.test.sh           PASS ( 12 assertions)   FLOOR  12
skills/session-kickoff/manifest-check.test.sh  PASS ( 62 assertions)   FLOOR  62
```

No floor is pinned below its suite's real count. Two floors are pinned on a *wrong* total — see
**M1** and **L1** — but neither is slack, so neither reds and neither bites.

**Class scoreboard.** Hunt class (a), *a check that cannot fail*: **7 findings**, including both
blockers-adjacent highs and the flagship arm of unit 6. Hunt class (b), *frozen vs live*: **0
findings** — the fixture built to encode that class is itself defective (B1), but no predicate in
this diff joins a historical value to a present one in a way that reds unrepairably. The build
committed class (a) in its own code six times while shipping the standing net against it.

---

### The two things that must change before this build closes

Both are a unit that reports success while delivering nothing, and in both cases the guard that
would have caught it is one document or one `printf` away.

---

## BLOCKERS

### B1 — Unit 6's flagship frozen-vs-live pair cannot fail: MOVE 2 grades a fixture with zero waiver rows

`tools/unattended/check-unattended.test.sh:893`
*(landed independently by four reviewers; confirmed by decisive experiment)*

MOVE 2 restores `$PRISTINE`, sets `phase: ABORTED`, widens `DIRECTIVES_CORE`, and asserts

```sh
miss "$out" "a parked waiver names a handle outside the effective directive set"
```

Check 17 selects its input with `grep -E '^[0-9][0-9-]*T[0-9:]*Z waiver · item [^ ]* · reason '`
(`tools/unattended/check-unattended.sh:413`). The RUN.md written by `build()`
(`check-unattended.test.sh:55-80`) carries **no such row**, PRISTINE is committed before any waiver
exists, and `reset_tree` restores exactly that. So check 17's `while … <<WAIVERS` loop iterates zero
times and the `miss` is vacuous.

**Verified by experiment, not by reading**: copy the kit to scratch, delete check 17's
`case " $PHASES_TERMINAL " in *" $ph "*` exemption entirely — the exact regression this standing
fixture exists to prevent — and the suite still exits 0 with `PASS (174 assertions)`.

Two independent tells confirm the author knew a row was required: the comment says "The waiver is
written by the DRIVER" while **no driver call occurs in the block**, and the LIVE control four lines
below (`:897-900`) has to `printf` the row in by hand. The pair also fails its own S3 — the two
halves differ by *waiver presence*, not by phase.

**Fix.** Append the same row the live control uses, between the `mutate` on `:892` and `frozen`:

```sh
printf '\n2026-08-16T00:00:00Z waiver · item minimal-prose · reason owner took it\n' \
  >> memory/builds/tRun/RUN.md
```

Then the frozen and running halves differ in exactly one variable — the phase. Add a presence
assertion so a future fixture edit cannot silently re-empty the population:

```sh
same "the fixture carries a waiver row" "$(grep -c ' waiver · item ' memory/builds/tRun/RUN.md)" "1"
```

While there, route `frozen()` (`:869`) through the file's own `mutate` helper, so a fixture no-op
cannot disarm both moves at once.

**Left-shift gate.** The general shape — *an arm asserting the ABSENCE of a message over a fixture
whose selector matches nothing* — is invisible to every gate we have. Cheapest mechanical catch: a
**mutation arm on the check itself**. Add to `check-unattended.test.sh` a final block that copies the
engine to `$(mktemp -d)`, neuters check 17's terminal exemption, re-runs the frozen half, and
requires the output to CHANGE. That is the same "live control" discipline the file already applies to
fixtures, applied one level up to the exemption. Generalisable: any `miss` over a scoped exemption
owes a paired *exemption-removed* control.

---

### B2 — `--park` exists in the driver and in no agent-facing catalogue; spec 1's S7 was in scope and not built

`tools/unattended/SKILL.template.md:196` · `tools/unattended/PROTOCOL.template.md:71`
*(landed independently by two reviewers)*

Repo-wide grep for the verb `--park` outside `memory/` returns **only** `tools/unattended/unattended.sh`
and `tools/unattended/unattended.test.sh`. Zero hits in:

- `tools/unattended/SKILL.template.md` — which spells every other verb as a runnable command block
  (lines 84, 85, 112, 120, 126, 137, 146, 157, 182, 196)
- the rendered `.claude/skills/unattended/SKILL.md`
- `tools/unattended/PROTOCOL.template.md` §7, which enumerates all eight other verbs
- `memory/guides/UNATTENDED-PROTOCOL.md`

`PROTOCOL.template.md:70-72` still declares the DECISION kind with **no writer named**. Worse,
`SKILL.template.md:109` instructs the agent to "Park what you refuse to decide" with no command
behind it, and the `--abort` block still tells the agent to fold a refused decision into the abort
reason — the workaround unit 1 was built to replace.

Unit 1's own justification (`unattended.sh:1266`) is that "an agent that refused a decision at pass
four had nowhere to put it." The place now exists and nothing routes the agent to it, so the mid-run
`decision` kind stays unwritten exactly as before the verb existed. Spec 1 lists S7 — "the protocol's
§2 gains the verb beside the kind it writes, in both copies" — as IN scope; it was not built.

**Fix.** Add a `--park <slug> --item "<question>" --reason "<why>"` block to `SKILL.template.md`
beside the `--close --override` block (the other mid-run recording verb), re-render with
`bash tools/unattended/adopt-unattended.sh`, and name `--park` beside the DECISION kind in
`PROTOCOL.template.md:71` (the parity leg keeps `memory/guides/UNATTENDED-PROTOCOL.md` in step).

**Left-shift gate.** The driver's S10 arm (`unattended.test.sh:1084-1091`) already enforces verb-set
parity across the three enumerations **inside** the driver — header docstring, unknown-arg refusal,
usage line, dispatch. This is precisely that drift class, one document over. **Extend the S10 loop to
a fifth and sixth carrier**: assert each verb in the set also appears in `SKILL.template.md` and in
`PROTOCOL.template.md` §7. Same loop, two more files, and the fourth catalogue becomes mechanically
joined rather than remembered. This is the highest-value single gate in the report — it would have
caught B2 at the moment `--park` was added to dispatch.

---

## HIGH

### H1 — `--park`'s BYPASS_BAN screen reads only `$reason`; an `--item` naming the flag permanently reds the bar on a record no verb can repair

`tools/unattended/unattended.sh:1290`
*(landed independently by three reviewers; reproduced with the real driver)*

```sh
if [ -n "$BYPASS_BAN" ] && printf '%s' "$reason" | grep -qF -- "$BYPASS_BAN"; then
```

`$item` is genuinely free text — protocol §2 calls it "the question, the options seen" — constrained
only against newlines and the literal ` · ` separator, and `park()` (`:1263`) writes it verbatim.
`check-unattended.sh:371` greps the run-state file **whole**, with no phase or terminal exemption:

```sh
if [ -n "$BYPASS_BAN" ] && grep -qF -- "$BYPASS_BAN" "$f"; then   # -> fail 11
```

So `--park tRun --item "should the lander take --no-verify?" --reason "no; the bar is the mandate"`
is accepted, lands in the record, and reds check 11 from that moment on. `park()` only appends, there
is no un-park verb, and once the run is terminal `refuse_if_terminal` blocks every verb — the record
is unrepairable through the kit, and the run can never satisfy its own DoD. A run refusing to bypass
the gate is precisely the decision most likely to be parked, so the wedge sits on the likely path,
mid-run, with nobody present.

The two-field intent is already explicit three lines above: the newline guard (`:1287`) tests
`"$reason$item"`. `--waive` (`:491`) and `--abort` (`:936`) both guard the reason and neither has a
free-text item; `--park` is the first verb with one, and it is the one left unguarded.

**Fix.** Widen the guard the way the newline guard is already widened, and reword the message:

```sh
if [ -n "$BYPASS_BAN" ] && printf '%s' "$reason$item" | grep -qF -- "$BYPASS_BAN"; then
  fail 43 "a parked item or reason spells the declared bypass flag, and the gate greps this file whole for it …"
```

Add the item-side arm to `unattended.test.sh` beside the existing reason-side one at `:1394`.

**Left-shift gate.** The class is *a driver field the gate reads whole but the driver validates in
part*. Add one arm to `unattended.test.sh` that, for **every** verb accepting free text, feeds the
declared `BYPASS_BAN` through each free-text parameter in turn and requires a refusal — a table-driven
loop over `(verb, flag)` pairs rather than a hand-written arm per verb. That scales to the next verb
with a free-text field, which is the recurrence this diff proves is coming.

---

### H2 — `--park`'s idempotence probe is an unanchored `grep -qF`, so a prefix reason is silently dropped with a success exit

`tools/unattended/unattended.sh:1298`
*(landed independently by four reviewers; reproduced)*

```sh
if grep -qF -- " decision · item $item · reason $reason" "$rel"; then
  echo "unattended: decision already parked, unchanged — $item"; return 0
```

`park()` terminates the line immediately after the reason, so the reason is always the line-final
field and the needle has **no right boundary**. Reproduced verbatim:

```sh
printf '…decision · item Q1 · reason owner said keep both A and B\n' \
  | grep -qF -- ' decision · item Q1 · reason owner said keep both'   # matches
```

`verb_park` then prints `decision already parked, unchanged`, exits 0, and writes nothing — a
distinct governance decision lost with a success message, on the one record the protocol says is
where a mid-run refusal must land. It is asymmetric (parking the longer reason first swallows the
shorter; the reverse does not), which is the proof this is not the "compares ONE pair and no-ops on a
match" the comment directly above claims, and the sibling contract it cites (`--waive` *refuses* a
differing set rather than silently no-op'ing) is the opposite behaviour. The protocol's
post-compaction recovery re-runs the run's own steps, which is exactly where a re-derived, shortened
reason appears.

**Fix.** Pin the end of the row. Cheapest correct form, with `ENVIRON` rather than `-v` so backslashes
in free text are not re-escaped:

```sh
NEEDLE=" decision · item $item · reason $reason" \
  awk 'index($0, ENVIRON["NEEDLE"]) == length($0) - length(ENVIRON["NEEDLE"]) + 1 { f = 1 } END { exit !f }' "$rel"
```

The newline and ` · ` refusals above already guarantee the row is one line with a single separator, so
an exact tail comparison is well-defined. Add a test arm parking a strict-prefix reason after a longer
one and asserting **two** rows.

**Left-shift gate.** Class: *a substring test standing in for an equality test on a record row*. The
repo already owns the right instrument — `tools/memory-tree/row_grammar.py` exists to reason about row
shape rather than substrings. Cheapest catch here without reaching for it: add a static arm to
`unattended.test.sh` that greps the driver for `grep -qF -- " ` … `· reason $` patterns and requires
each to be paired with an anchor, since every idempotence probe in this kit compares a line-final
field.

---

### H3 — the arm claiming `--status` surfaces a parked decision asserts only the slug, which every reachable output contains

`tools/unattended/unattended.test.sh:1385`
*(landed independently by four reviewers)*

```sh
hit "$(run --status tRun)" "tRun"
```

under the comment "…and `--status` surfaces it, which is the whole point of writing it somewhere a
reader reaches."

`verb_status` (`unattended.sh:1087-1100`) prints exactly one line —
`printf 'unattended: %s · phase %s · witness %s · next %s\n'` — from phase, witness and
`nonterminal_units`, and **never reads the parked region**. The needle `tRun` is the slug interpolated
as the first field; both refusal paths also interpolate `$rel` (= `memory/builds/tRun/RUN.md`), which
contains the slug; and the test's `run()` folds `2>&1`. So no reachable code path can fail this
assertion, pass or fail, parked or not, and it would keep passing if `--park` wrote nothing at all.

Two harms, not one. It counts toward `FLOOR_ASSERTIONS=273` while proving nothing — hunt class (a) in
the suite that is the driver's contract. And the capability it documents **does not exist**: no verb
prints `decision · item` rows (`verb_resume:1112` names parked *waivers* only; check 17's selector is
anchored on ` waiver · item `), so the only reader of a parked decision is a human opening RUN.md, and
the only consumer is the agent-attested `parked-decisions-surfaced` DoD flag. Spec 1's S6 — "the parked
row is visible to `--status`" — is unbuilt and unverified.

**Fix.** Either make it real — teach `verb_status` to print a parked count or the newest parked item,
then assert on the item text (`hit "$(run --status tRun)" "decision · item do facts 5-7 pin with fact 4"`)
— or delete the arm **and** the comment. Do not leave a needle the refusal path also satisfies. Note
this is coupled to B2: if `--park` gets a route in, this is where the route back out belongs.

**Left-shift gate.** Class: *a needle satisfied by the fixture's own identifier*. A cheap, general
static arm: scan the suite for `hit "$(run …<slug>…)" "<slug>"` — an assertion whose needle is a
substring of its own invocation — and red. Broader and more valuable: make `assert-arms`-style
reasoning available to shell suites the way `tools/memory-tree/check-arms.py` already does for `fail`
branches, so an arm whose needle appears in the command that produced it is flagged by construction.

---

## MEDIUM

### M1 — three of unit 4's 52 new increments sit inside subshells and are discarded; the file's own derivation comment blames a false cause

`tools/memory-tree/check-memory-hygiene.test.sh:799` (also `:825`, `:890`)
*(landed independently by three reviewers; arithmetic re-measured)*

All three sit inside the `( cd "$H" && … )`, `( cd "$Y" && … )` and `( cd "$R" && … )` fixture-building
subshells, so their writes to `n` never reach the parent. Confirmed by arithmetic: 88 helper calls + 49
top-level `n=$((n+1))` = **137**, exactly what the suite prints and exactly the pinned floor. The three
indented increments contribute nothing.

The assertions they were placed to arm live *outside* those subshells and now carry no increment of
their own: `[ "$rch" = 0 ] && { … }` (~`:803`), the `grep -qF 'selected an EMPTY population' <<<"$outy"`
arm (~`:832`), and the check-13 two-claimant grep (~`:900`). Those three are the only assertions in the
file with no increment behind them — strand the block containing them past an exit and the floor stays
satisfied at 137. That is the exact failure mode unit 4 exists to close, reintroduced inside its own fix.

Compounding it, the derivation comment at `:950-956` explains the 52-vs-49 gap as "three sites sit on
paths this run does not take, which is the very signal the floor exists to surface." Both halves are
false: those paths **are** taken (`outh` at `:802`, `outy` at `:834`, `outr` at `:899` all drive later
passing arms), and the three sites are not assertions. The comment explicitly invites re-checking, so a
maintainer who accepts it will hunt for stranded arms that do not exist.

**Fix.** Move each increment out of its subshell to immediately precede the assertion it arms — just
after the closing `)` and the `out…=$(…)` capture — rewrite the derivation note to the measured cause
(52 inserted, 3 non-assertions removed, +49), and re-pin `FLOOR_ASSERTIONS` in the same diff. Combined
with **L1**, re-measure and pin whatever the suite then prints (139 by inspection).

**Left-shift gate.** In this file an indented `n=$((n+1))` is almost always a subshell. Add a static
self-check to the suite's own tail: `grep -nE '^[[:space:]]+n=\$\(\(n\+1\)\)' "$0"` must match nothing
outside a function body. Two lines, catches the whole class permanently, and belongs in the suite that
invented the counter.

---

### M2 — `compliant()` never checks that the floor is compared to anything, and `[0-9]+` accepts `FLOOR_ASSERTIONS=0`

`tools/check-testsuite-counts.sh:48`

```sh
compliant() { # file -> 0 when it prints the agreed shape AND pins a floor
  grep -qE 'echo "PASS \(\$[A-Za-z_][A-Za-z0-9_]* assertions\)"' "$1" \
    && grep -qE '^FLOOR_ASSERTIONS=[0-9]+$' "$1"
}
```

The mechanism the leg exists to universalise is the **comparison** of the executed total against a
floor. The leg grades the presence of two independent strings and nothing joins them. Its own green
fixture proves the hole: `mk_ok()` (`check-testsuite-counts.test.sh:24`) writes `FLOOR_ASSERTIONS=3`
plus the echo, with no `[ "$n" -ge "$FLOOR_ASSERTIONS" ]` anywhere, and the leg calls it compliant. The
engine even contradicts itself — its refusal text for the floor-only case reads "nothing compares the
floor to anything", which is precisely the state it lets through once the echo line is present.

A suite draining off the 21-row shrink-only registry can therefore satisfy the new bar with
`FLOOR_ASSERTIONS=0`, or with a floor nothing reads, buy exactly zero protection against the
stranded-arms defect, and have its waiver row deleted as "complied" — the ratchet running backwards.

**Fix.** Require the comparison and a positive floor:

```sh
  && grep -qE '\[ "\$[A-Za-z_][A-Za-z0-9_]*" -ge "\$FLOOR_ASSERTIONS" \]' "$1" \
  && grep -qE '^FLOOR_ASSERTIONS=[1-9][0-9]*$' "$1"
```

Update `mk_ok` to emit the comparison, and add a fixture arm for the floor-present-but-never-compared
state as a third named refusal.

**Left-shift gate.** This is the *decorative conjunction* shape — a predicate whose terms are each
satisfiable without the property the predicate names. The leg's own self-test is the right place: every
named refusal in `check-testsuite-counts.sh` owes a fixture that produces **only** that state. Today
there are three refusal messages and two fixtures; requiring the counts to match is a one-line arm and
would have surfaced both M2 and L8.

---

### M3 — the derived population misses `recall-opened.test.sh`, a `*.test.sh` the bar genuinely runs

`tools/check-testsuite-counts.sh:36`

```sh
suites=$(grep -oE '"[^"]*\.test\.sh"' "$MANIFEST" | tr -d '"' | sort -u)
```

The leg's stated rule is "every self-test the BAR runs", justified by `tools/gate-legs.json` being the
single source for what the bar runs. That is false for one suite: the `memory-recall kit selftest` leg
runs `python3 tools/memory-recall/selftest.py`, which at `selftest.py:1026-1035` subprocesses
`bash <KIT>/recall-opened.test.sh`. Verified — that name appears in no argv string in the manifest, the
suite prints no count and pins no floor, and it is absent from all 21 rows of
`memory/project/testsuite-count-waivers.txt`.

So a `*.test.sh` the bar executes is **neither graded nor named as a known exception** — the silent
exception the file's own header argues against ("a leg with twelve silent exceptions checks nothing, a
leg with twelve NAMED ones ratchets"). 28 `*.test.sh` are tracked, 26 reachable by the grep; the other
omission, `hygiene-parity.test.sh`, is correctly out of scope (it takes a rev argument and is not on the
bar).

**Fix.** Cheapest: add the path to the waiver registry and relax the ghost-waiver refusal to accept a
tracked suite the manifest reaches indirectly. Better: seed the population as
`manifest argv ∪ (tracked *.test.sh named by any file the manifest runs)`. Either way, name it.

**Left-shift gate.** Class: *a derived population that silently omits a member*. Add a reconciliation
arm to the leg: `git ls-files '*.test.sh'` minus the derived population must equal a **declared**
out-of-scope list, so any tracked suite outside both the population and the registry reds by
construction. That is the shape the leg already applies to waiver rows, turned on its own selector.

---

### M4 — the reference converted suite prints `PASS` unconditionally, and pins its floor on a counter of *successes*

`skills/session-kickoff/manifest-check.test.sh:666`
*(landed independently by four reviewers; both halves measured)*

Two defects in the one suite unit 5 converted as the reference shape.

1. `echo "PASS ($pass assertions)"` sits outside any guard. Every sibling gates it —
   `check-testsuite-counts.test.sh:88`, `check-memory-hygiene.test.sh:963`,
   `check-unattended.test.sh:958`, `unattended.test.sh:1432` all write
   `[ "$st" = 0 ] && echo "PASS ($n assertions)"`. Here a red run prints `PASS (61 assertions)`
   immediately before `---- 1 failed ----`. The exit code still reds the bar; the damage is to the
   persisted per-leg log under `<git-dir>/gate-logs/`, the artifact a human reads on a red run. This is
   the same class as the note already standing at `check-memory-hygiene.test.sh:940` — "Upstream printed
   PASS ~150 lines early and landed a red merge bar because the head of the output said success" — and
   the exact false-success class TOOL-cBriefedPilot-23 was written to kill.

2. `pass` increments only on the success path (`:30`, `:51`, `:515`, `:621`), so it counts successes, not
   executions. A green run prints exactly 62 against `FLOOR_ASSERTIONS=62`, so **any single ordinary
   failure** drops it to 61 and additionally fires "arms are UNREACHABLE rather than absent; look for a
   block stranded past an exit" — a second, wrong diagnosis pointing the next maintainer at stranded code
   that does not exist. The leg's contract says "executed assertion count", which `$pass` is not.

**Fix.** Track executions in a separate counter incremented at the top of `run()`/`runm()` and at each
inline case, pin the floor against that, and guard the print:
`[ "$fail" = 0 ] && echo "PASS ($ran assertions)"`.

**Left-shift gate.** `compliant()` in `check-testsuite-counts.sh` greps for the line's *presence*, so the
guarded and unguarded spellings are indistinguishable to it — the new leg certifies as the reference the
one suite whose count line can lie. **Tighten the regex to require the guard prefix**
(`\[ "\$[a-z]*" = 0 \] && echo "PASS \(…`), which encodes "printed only on success" into the agreed shape.
Pairs with M2: both are the same edit to the same function.

---

### M5 — `DIRECTIVES_EXTRA_TABLE` has exactly one reader, and the "shown to the agent" half of unit 2's join points at a file nothing routes anyone to

`tools/unattended/check-unattended.sh:513` · `tools/unattended/PROTOCOL.template.md:242`
*(two reviewers, distinct evidence: the agent's route and the binding contract)*

Exhaustive grep: `DIRECTIVES_EXTRA_TABLE` appears only in `.unattended.conf:70`,
`check-unattended.sh` (49, 513-530), `check-unattended.test.sh`, and spec 2. **Zero hits** in
`adopt-unattended.sh`, `SKILL.template.md`, the rendered `.claude/skills/unattended/SKILL.md`,
`tools/unattended/.unattended.conf.example`, or either protocol copy.

Unit 2's stated defect is that an extra directive was "waivable by a verb and invisible to the agent."
Check 16 arm A is now satisfied by a conf-declared markdown file carrying a matching row — and nothing
renders, references, or points at that file. The Skill's directive table (`SKILL.template.md:27-39`) is
eleven kit rows with no pointer to a project row source, and `verb_resume` (`unattended.sh:1112`) still
tells the agent "the directives and their waivers — the table in the unattended Skill". So the gate half
is closed and the agent half is still open.

Separately, spec 2's AC2 ("the resolved rule is stated in UNATTENDED-PROTOCOL.md §10") was not built:
the §8 conf-key table (`:232-246`) lists every other key the leg reads including `DIRECTIVES_EXTRA` and
`DIRECTIVES_FLOOR`, and §10 (`:287-316`) still asserts "the list an agent reads is the table in the
rendered Skill" — false the moment a project declares a row source. An adopter copying the shipped
`.unattended.conf.example` cannot discover the extension point at all; it is reachable only in this repo.

**Fix.** Add a `DIRECTIVES_EXTRA_TABLE` row to the §8 key table, add the key with its comment to
`.unattended.conf.example`, amend §10 to say the agent's list is the Skill table UNION the declared row
source, and have `SKILL.template.md` render a pointer line that `adopt-unattended.sh` substitutes. Keep
the declared-path-missing refusal so an empty substitution stays a named failure.

**Left-shift gate.** Class: *a conf key the engine reads and no catalogue documents*. `check-unattended.sh`
already parses the conf; add a check asserting **every** conf key the engine reads appears in the
protocol's §8 key table and in `.unattended.conf.example`. Derive the key set from the engine's own
reads, not a hand-list, so the next key is joined by construction. This is the conf-side twin of B2's
verb-set gate, and the two together close the whole "new surface, no catalogue" family.

---

### M6 — a terminal Tier-1 spec with a present-but-empty §8 is still silent; the new `q == 0` refusal closes only the missing-heading case

`tools/memory-tree/check-memory-hygiene.sh:685`

Reproduced on a scratch memory tree with `SPEC_FORMAT_CUTOFF` armed and a Tier-1 `**Status:** CLOSED`
spec:

- control A, no `## 8.` at all → reds with the new message
- control C, `## 8.` with `- an unanswered fork` → reds with "terminal Status with unresolved §8 Open questions"
- **case B, `## 8. Open questions` immediately followed by `## 9. Revision log` → SILENT**

The range opens so `q > 0` skips the new refusal, the item loop finds only a blank line so `q8` stays
empty, and the pre-existing `q8 != ""` guard short-circuits the unresolved-fork branch. Tier-2 is covered
by the empty-section-body check, but that block sits **below** the `hdr ~ /Tier-1/` cut, so Tier-1 has no
backstop. The new refusal's own message says "silence and a resolved fork are the same byte without this"
— and after the hoist, keeping the heading and deleting the body is the cheapest way to reproduce exactly
that byte.

**Fix.** Fold the empty case into the new branch:
`if (q == 0 || q8 == "") print f " (terminal Status and no answered Open questions section found …)"`,
and add a Tier-1 fixture (`tFixture-65`) with an empty `## 8.` asserting the message, next to `tFixture-64`.

**Left-shift gate.** Class: *a new refusal that closes one of two ways to reach the state it names.* House
rule worth writing into `REVIEW-PROTOCOL.md`: **a new gate arm owes a fixture per reachable path to its
target state, not per message.** Mechanically, the closest existing instrument is `check-arms.py` — extend
its notion of "armed" from "a positive assertion names the failure text" to "each `print`/`fail` branch in
a multi-condition guard is reached by its own fixture."

---

### M7 — "six waiver registries" is now false in five prose sites, and the new registry is absent from the HYGIENE catalog entirely

`AGENTS.md:50` · `memory/HYGIENE.md:101,111` · `tools/memory-tree/HYGIENE.template.md:101,111` ·
`tools/memory-tree/check-memory-hygiene.sh:227`
*(two reviewers; verified on disk)*

`memory/project/` now holds **seven** registries — `corpus-path-unresolved.txt`, `curation-debt.txt`,
`id-orphan-waiver.txt`, `legacy-files.txt`, `method-carriers.txt`, `testsuite-count-waivers.txt`,
`unarmed-branches.txt` — and `check-memory-hygiene.sh:240-241` whitelists all seven. The stale "six"
survives in all five sites above.

`HYGIENE.md:111` states it as a **rule**, so the installed hygiene document an author consults now
contradicts the gate it describes, and `HYGIENE.template.md` ships that contradiction to adopters. Worse
than a miscount: grepping `testsuite-count` in both files returns nothing, so the new registry is not
merely mis-tallied, it is missing from the catalog those files carry.

The same commit recognised the rot one line away — `check-memory-hygiene.sh:232` was deliberately
de-numbered from "the six registries stay" to "the registries stay" — and edited `AGENTS.md` six lines
lower to add the new leg's bullet while leaving the count.

**Fix.** De-number all five sites the way `:232` was de-numbered ("the gate's `*.txt` waiver registries and
nothing else"), fix the engine comment at `:227`, and add the new registry to the HYGIENE catalog.
`memory/HYGIENE.md` and `tools/memory-tree/HYGIENE.template.md` must change together —
`kit-dogfood-parity.test.sh` byte-compares them.

**Left-shift gate.** Nothing gates a prose count, and this is the second time it has rotted. Two options,
both cheap: (1) a hygiene check that the registry filenames whitelisted in the engine each appear by name
in `HYGIENE.md` — a set join, not a count; or (2) the standing rule the engine already adopted — **no
cardinal in prose about a set the gate derives**. Prefer (1); it also catches the absent-from-catalog half,
which a de-numbering alone does not.

---

## LOW

### L1 — a stray top-level `n=$((n+1))` between two function definitions counts an assertion that does not exist

`tools/memory-tree/check-memory-hygiene.test.sh:424`
*(landed independently by four reviewers)*

Line 424 is a bare `n=$((n+1))` sitting between the `lineno()` definition (423) and `before()` (425).
Function definitions execute nothing, `lineno()` is a plain accessor with no FAIL branch, and `before()`
carries its own increment inside its body. So it executes once, unconditionally, arming nothing: 137
reported against 136 real. Because the total sits exactly on the pin, deleting the dead line — the correct
cleanup — reds the bar for no behavioural reason. Low only because the floor is `-ge`.

**Fix.** Delete `:424` and re-pin in the same commit, folded into M1's re-measure.

**Left-shift gate.** Same static arm as M1, widened: an increment must be followed, within its statement
group, by an assertion. Cheapest approximation that catches both L1 and M1: require every top-level
`n=$((n+1))` to be at column 0 **and** followed within N lines by a line containing `st=1`.

---

### L2 — the count-line half of `compliant()` is unanchored and is satisfied by a string inside a fixture generator

`tools/check-testsuite-counts.sh:49`

The leg's own self-test satisfies the regex twice: at its real line 88, and at line 24 —
`mk_ok() { printf 'FLOOR_ASSERTIONS=3\necho "PASS ($n assertions)"\n' > "$1"; }`. Delete or strand line 88
and the leg still calls that suite compliant, on the fixture string alone. The floor half is anchored
(`^FLOOR_ASSERTIONS=[0-9]+$`) so the conjunction is not fully decorative — but the half carrying the leg's
actual claim is satisfiable by a comment or a here-doc in any of the 26 graded suites.

**Fix.** Anchor it the way the floor half already is:
`grep -qE '^[^#]*echo "PASS \(\$[A-Za-z_][A-Za-z0-9_]* assertions\)"[[:space:]]*$'`, and add a self-test arm
whose fixture's only occurrence of the shape is inside a single-quoted string.

**Left-shift gate.** House rule for this leg, testable in its self-test: **a fixture generator must not
satisfy the predicate it generates fixtures for.** One arm — run `compliant()` against
`check-testsuite-counts.test.sh` with its real count line removed and require a refusal.

---

### L3 — `TEMPLATE-SPEC`'s Tier-1 profile now understates what the gate enforces, and ships that to adopters

`memory/TEMPLATE-SPEC.md:75` · `tools/memory-tree/SPEC-TEMPLATE.template.md:75`

Both still read "the status header + placeholder rules are enforced; the nine-section canon is not …
write the few sections that matter." After unit 3's hoist, a Tier-1 spec is graded on the §9 revision-log
high-water **and** the terminal-§8 resolution rule, including the new `q == 0` refusal — the engine says so
at `check-memory-hygiene.sh:626` ("these two run for EVERY TIER, so they sit ABOVE the Tier-1 cut"). The
impact is already recorded in the diff: all three shape-only §8 repairs in `HEAD~1` (aWrittenMethod-3,
cBriefedPilot-17, cBriefedPilot-9) are CLOSED Tier-1 specs edited solely to satisfy the newly-hoisted rule.
An adopter's first terminal Tier-1 spec reds against a rule their own template says does not apply.

**Fix.** Amend the Tier-1 bullet in `SPEC-TEMPLATE.template.md` and re-render `memory/TEMPLATE-SPEC.md`:
the section canon and empty-body test are waived for Tier-1; the §9 high-water and terminal-§8 rules are
enforced on both tiers.

**Left-shift gate.** Class inverted — *the doc claims LESS than the gate enforces.* Add to the hygiene
self-test a Tier-1 fixture per tier-scoped rule, asserting the message, so the tier profile is defined by
executed arms rather than by prose; then the doc is derived from the arms, and moving an assertion across
the `Tier-1) next` cut without touching the doc reds.

---

### L4 — the hoisted assertions require a canonically NUMBERED heading from a tier TEMPLATE-SPEC exempts from the canon

`tools/memory-tree/check-memory-hygiene.sh:645` (and `:661`)

Reproduced: a Tier-1 spec with header `rev-2` and an unnumbered `## Revision log` listing rev-1 and rev-2
reds with `(header rev-2 not logged in the §9 Revision log)` — a false claim; the log is right there. Same
at `:661` for a terminal Tier-1 spec with `## Open questions`, which hits the new `q == 0` refusal saying
no such section was found. The harness's own Tier-1 fixture `tFixture-5` uses free-form `## Whatever`
headings and is asserted silent, so unnumbered headings are legal for that tier — and the diff shows the
tightening: `tFixture-5` had to be given a `## 9. Revision log` to stay silent. `tFixture-63` proves
number-**independence**, not number-**optionality**. Low because the live corpus is all-numbered.

**Fix.** Make the number optional in both openers — `/^## ([0-9]+\. )?Revision log/` and
`/^## ([0-9]+\. )?Open questions/` — keeping the §8 range close as-is plus a bare `^## ` alternative if
Tier-1 free-form sections may follow. Add a Tier-1 fixture with unnumbered headings asserting silence,
beside `tFixture-63`.

**Left-shift gate.** Class: *a fixture edited to keep an arm green, where the edit is the finding.* Worth a
`REVIEW-PROTOCOL.md` line: **when a diff modifies an existing fixture to keep it silent, the diff owes an
explicit statement of the behaviour change that required it.** No mechanism catches this; a review question
does.

---

### L5 — the govkit descriptor guards both new legs where gov's own manifest guards neither, and the guard misses the population the leg grades

`tools/govkit/entries/check-testsuite-counts.kit.toml:27`
*(two reviewers; one correctly narrowed the claim)*

`tools/gate-legs.json:541-555` adds both legs with **no** guard (always run). The shipped descriptor guards
leg 1 on `{prefix}/check-testsuite-counts.sh` and `tools/gate-legs.json`. The leg's verdict is
content-derived from every `*.test.sh` the manifest names, none of which is in that guard — so in an adopter,
a diff that drops a count line from an existing suite, or edits the waiver registry, skips this leg on a
diff-scoped run: exactly the changes it grades. House style agrees with gov: sibling descriptors give
state-checking legs `guard = []` (`memory-tree/kit.toml:55-59`, `drift-audit/kit.toml:49-53`) and reserve
`{kit}/` guards for self-tests, which leg 2 correctly does. govkit never joins a descriptor's `gate_leg`
block to gov's manifest (`govkit.py:434-462` classifies only guard pathspecs already present; `:898-900`
uses the block for token extraction), so nothing sees the divergence. Low per the charter: a too-narrow
guard costs an early signal, not a merge verdict.

**Fix.** Drop `guard` from leg 1 so the descriptor matches what gov itself runs.

**Left-shift gate.** Descriptor-vs-manifest divergence is by design per `registry.toml:143-144`, so a strict
join is wrong. Narrower and correct: a govkit `selfcheck` rule that a descriptor `gate_leg` whose command is
not scoped to `{prefix}` must declare `guard = []` or a guard naming a path outside the kit — encoding the
house convention the two sibling kits already follow.

---

### L6 — the leg's name and opening sentence claim "every bar self-test"; eleven python self-tests are silently out of scope

`tools/gate-legs.json:543` · `tools/check-testsuite-counts.sh:2`

The manifest leg is named "testsuite counts (every bar self-test prints one)" and the engine's line 2 says
"Every self-test the BAR runs". The population is `*.test.sh` only. The manifest also runs
`gen_build_index.py --selftest`, `corpus_ids.py --selftest`, `gotchas.py --selftest`,
`row_grammar.py --selftest`, `check-arms.py --selftest`, `codebase-map/selftest.py`, `test_codebase_map.py`,
`settings-merge.py --selftest`, `memory-recall/selftest.py`, `drift-audit/selftest.py` and
`govkit/selftest.py`. None prints a count against a floor, none is waived, and nothing records that they are
out of scope. The scoping is defensible; the **unnamed** exclusion is the shape the file's own "twelve NAMED
ones ratchet" argument rejects.

**Fix.** Narrow the claim in both places ("every bar `*.test.sh`") and add a one-line header note naming the
python self-tests as a deliberate scoped-out population with the reason — or extend the population and seed
eleven more rows.

**Left-shift gate.** Covered by M3's reconciliation arm if the declared out-of-scope list is required to be
explicit: then "silently excluded" becomes unrepresentable, and this finding and M3 close together.

---

### L7 — `PK_ITEM` is initialised inside the conf-default block, so a tracked conf can pre-set it and defeat one of `--park`'s refusals

`tools/unattended/unattended.sh:63`

`PK_ITEM=""` sits two lines above `. "$CONF"` (`:65`), inside the conf-default block, while **every** other
CLI-argument variable (`VERB SLUG KID REASON arg OV_* WAIVE_*`) is initialised at `:1319-1324`, after the
source. `PK_ITEM` appears nowhere between 65 and 1319, so the early init buys nothing under `set -u`, and
`check-unattended.sh` rejects no unknown conf key. With `PK_ITEM="anything"` in `.unattended.conf`,
`--park <slug> --reason r` never reaches the `[ -n "$item" ]` refusal at `:1277` and the parked question comes
from a tracked file rather than the agent's argv.

Weighed the counter — `.unattended.conf` is arbitrary sourced shell, and the agent can satisfy `--item` with
any string anyway — which caps this at low. It does not make the placement correct: a one-line misplacement
defeating one of the verb's seven refusals, in a kit whose premise is refusals a run cannot write its own way
past.

**Fix.** Move `PK_ITEM=""` down to `:1319` beside `VERB=""; SLUG=""; KID=""; REASON=""`.

**Left-shift gate.** Static arm in `unattended.test.sh`: every variable assigned from `$2` in the dispatch
loop must have its initialiser **after** the `. "$CONF"` line. Derive the variable set from the dispatch
block itself, so the next CLI flag is covered without an edit.

---

### L8 — the count-present / floor-absent case gets the message for the opposite state, and no arm covers it

`tools/check-testsuite-counts.sh:74`

`compliant()` requires both greps, but the disambiguating branch at `:71` tests only for the floor. So a
suite that prints the agreed count with no `FLOOR_ASSERTIONS` falls to `:74` and is told it "prints no
executed assertion count against a floor" — false of it — while the mirrored state gets a precise message at
`:72`. The fixture comment at `check-testsuite-counts.test.sh:65` states the intent outright ("Distinct
message, because the fix is different"), a principle this case does not receive. It is the **most common**
non-compliant shape in the population the docstring measured — 15 suites print some count, only 3 pin a floor
— so it is the message most of the 21 waived rows will hit as the registry drains.
`mk_floor_only` exists; there is no `mk_count_only`.

**Fix.** Split the else branch on the count grep: "a self-test prints the agreed count line but pins no
FLOOR_ASSERTIONS, so nothing compares the count to anything." Add a `mk_count_only` fixture and an arm
asserting that text, and raise the floor by one.

**Left-shift gate.** Same arm as M2: **refusal-message count must equal fixture count** in the leg's
self-test. One assertion closes M2's missing third refusal and L8's missing third fixture.

---

## What the three refuted claims were, and why they matter

Three of the 46 raw findings did not survive the skeptic. Recording the shape, not the text, because the
same shapes will recur:

1. **A floor claimed to be pinned below its suite's real count.** Re-measured all five; every floor equals
   its measured count exactly. Two floors are pinned on a *wrong* total (M1, L1) — a different defect, and
   the distinction matters: a floor that is wrong-but-tight still bites, a floor that is slack does not.
2. **A `--park` refusal claimed unreachable.** All seven refusals are reachable; the real defects are the
   two that are too *narrow* (H1) and one that is too *loose* (H2).
3. **A guard clause claimed to name no `*.test.sh` path.** Leg 2's guard does name
   `{prefix}/check-testsuite-counts.test.sh` and matches convention; only leg 1 diverges (L5). The
   surviving residual was re-scoped rather than dropped.

---

## The single highest-value gate in this report

**B2's fix.** `unattended.test.sh:1084-1091` already loops the verb set across three carriers inside the
driver. Adding `SKILL.template.md` and `PROTOCOL.template.md` §7 as carriers four and five is a
two-line change to an existing loop, and it converts the entire "a new verb the agent is never told about"
family from a review question into a bar failure. B2 is in this report only because that loop stops at the
driver's own file.

Second-highest: **M5's conf-key join** (every key the engine reads must appear in the protocol key table and
the shipped example), which is the same gate on the conf axis. Together they close the "new surface, no
catalogue" family in both directions.

---

## Recommended close order

1. **B1** — one `printf` plus a presence assertion; unit 6 is not delivered until this lands.
2. **B2** — Skill block, protocol bullet, re-render, and the S10 loop extension.
3. **H1, H2, H3** — three edits in `unattended.sh`/`unattended.test.sh`; H3 is coupled to B2, so do them
   in one pass.
4. **M1 + L1 together** — one re-measure, one re-pin, one corrected derivation comment, one static arm.
5. **M2 + L2 + L8 together** — one `compliant()` rewrite and one refusal-vs-fixture arm.
6. **M3 + L6 together** — one reconciliation arm and the narrowed claim.
7. **M4, M5, M6, M7** — independent.
8. **L3 + L4 together** — both are unit 3's tier profile; one doc amend, one regex loosening, two fixtures.
9. **L5, L7** — one-line each.
