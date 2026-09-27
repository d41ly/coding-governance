**Serves:** spec-audit TOOL-aBatchedArm-4

# Tier-2 spec audit — TOOL-aBatchedArm-4, ROUND 3

*The second fold audit. Round 2 (BLOCKED, ten defects, three blocker rows) was folded into rev-3 of
the unit that gives `tools/run-gates/run-selftests.sh` a declared execution mode and wires the kit
runner to both spellings. This round grades THAT fold — where it is wrong and where it is incomplete
— and does not re-report what rounds 1 and 2 already found and the fold closed. Node `a`,
2026-09-13, ROUND 3. Every finding below survived a skeptic prompted to REFUTE it, and every cited
line was re-read in the tree by the author of this report rather than transcribed from a lens: the
kit runner's parser and summary were opened, the six carrier lines were read as text, the charter
was measured with the leg's own script, the §7 derivation was re-run over `tools/gate-legs.json`
with the seven files §4 lists, and the sweep TSV rows were re-read. Each row carries its address
inside the spec, the fix, and the gate that would have caught it before a reviewer had to.*

**Reviewed subject, pinned at blob:**

- `memory/builds/aBatchedArm/spec/2026-09-13-spec-TOOL-aBatchedArm-4.md`@`9036f2c195d32e99957e5e045f54fd4acba96b0d` — rev-3, the fold of round 2's ten defects. ROUND 3.

The sibling specs are NOT in scope and are not re-graded. `TOOL-aQuenchedHarness-4` is cited in one
row (B1) because it is the record that made `--all` this kit's compensating check, which is a fact
about what the carriers this spec edits mean. `TOOL-aBatchedArm-5` has no spec; where a row names it,
it is because this unit hands it a consequence.

## Verdict: BLOCKED

Four rows at BLOCKER, fourteen at HIGH, eight at MEDIUM, one at LOW. Those twenty-seven rows
collapse to **eleven distinct defects**; the table below names which rows share one, so a fold that
repairs a defect repairs every row under it.

The four blocker rows are ONE defect, found independently by all four lenses, and it is the hole in
the fold's central act. Rev-3 correctly lands `--pooled` dark and makes the four DoD carriers say
`--serial` — round 2's blocker is closed. But S3 defines the kit runner's mode rule for `--selftests`
only, while the tree reaches the selftests half by THREE routes: no argument
(`ONLY="${1:---selftests}"` at `run-unattended-gates.sh:121`), `--selftests`, and `--all` (`[ -z
"$ONLY" ]` at `:257`). Three of the six carrier lines spell the other two routes — `kit.toml:125`
and `AGENTS.md:519` are the no-arg form, `kit.toml:126` is `--all` — and the parser takes exactly one
positional, so `--all --serial` is `unknown argument` today. `TOOL-aQuenchedHarness-4` S7/AC6
records `--all` as this kit's compensating check. The spec instructs rewriting `kit.toml:126` to a
form it never defines, and AC4 exercises none of the three routes it leaves undefined. Built as
written, the recorded compensating check either refuses at `:263` after the five checks have already
run, printing `unattended gates RED — 12 ran on demand` for seven suites that never ran — the
liveness class the file's own comment at `:253-257` exists to name — or silently takes whichever
mode the builder guessed. Every acceptance criterion is green in both cases (B1).

Counted the way rounds 1 and 2 were counted, the blocker figure is four ROWS against round 2's three
and round 1's eight; counted by defect it is one against one. Under `memory/guides/BUILD-METHOD.md`
the loop re-arms only on a STRICTLY SMALLER confirmed-blocker count, and four is not smaller than
three, so by the method's own rule this round does not re-arm a round 4. Disposition of the standing
blocker: FOLD — the defect is in the document this review read, and the mechanism it needs (a second
positional at the parser, checked on the RESOLVED verb) is inside this unit's own scope. The fold is
one grammar paragraph in S3, two arms in AC4, and one spelling at `kit.toml:126`. This report says
so plainly rather than trimming a row to make the figure fall.

The rest of the fold is right about the thing round 2 said mattered most — the default no longer
flips, the risky spelling lands dark, the carriers are named — and wrong or incomplete on ten
mechanical items, five of them at HIGH: AC4's serial clause requires a summary line that both names
`serial` and is byte-identical to one that carries no mode token, so it cannot go green (H1); the
carriers clause S3 calls "observed by AC4 and AC5" is observed by no criterion, which is the half of
round-2 H1 the fold did not take (H2); the `AGENTS.md:519` rewrite adds 21 bytes to a file 18 bytes
under an unguarded bar leg's cap, and §7 does not list that leg (H3); §4 still carries rev-2's
pooled-primary design paragraph and §5 migration still hardcodes `:263` to `--serial`, both
contradicting S3 (H4); and the kit runner's own `--help`, the shipped README and
`SESSION-KICKOFF.md:169` teach the refused form and are in no carrier list (H5). Four items at
MEDIUM: §7's derivation was not re-run over the grown file set (M1); AC4's pooled arm is green on a
width-1 pool (M2); AC4 types `7` for a derived count and leaves the pooled pass unpriced, the exact
defect round-2 M3 asked it not to commit (M3); AC7's mechanism is wrong on three counts and round-2
H2's negative clause and M4 arm were dropped (M4). One at LOW: round-2 L1 was not folded (L1).

## Review shape

- raw 44 · confirmed 27 · refuted 17 · unverified 0 · precision 0.61

Precision at 0.61 is above the ~0.5 floor `AGENTS.md` §8 sets for adding agents and above round 2's
0.57, so the fan is scoped about right for a fold audit and tightening slightly. Read the confirmed
count with the table below in hand: the pipeline reports zero duplicates because each row addresses
a different section or clause, but four lenses hit the grammar seam (four rows), four hit the AC4
byte-identity seam (four rows), and three hit the charter cap (three rows). Twenty-seven rows is
eleven defects.

## Run integrity

- lenses 4/4 returned, 0 DIED
- skeptic batches 5/5 returned, 0 DIED
- 0 contradictory verdict(s) demoted to unverified
- 0 spurious verdict(s) discarded
- 0 duplicate(s)

Nothing died. Every zero above is a measured zero and not an absence of evidence, so this round's
finding set is complete for the lenses that ran, and a fold may treat the UNVERIFIED bucket as
genuinely empty. The count of round-2 defects NOT re-found here — E-1 (the default flip), E-4 (S6
and SLACK), E-8 (the roster), E-9 (the `watch:` entry) — is likewise a measured zero: those seams
were read and nothing stood. E-2, E-3, E-5, E-6, E-7 and E-10 each stand again in some form, and
the table names which.

## What the fold closed and what it did not

| Round-2 defect | Fold status | Where it stands now |
|---|---|---|
| E-1 · DoD flipped to `--pooled` at the killing bound | CLOSED — both spellings, carriers say `--serial`, bare refuses, flip is unit 5's | its design paragraph in §4 was not rewritten (H4) |
| E-2 · four carriers untouched | HALF — carriers named in S3 and Files touched | no criterion reads any carrier (H2); the grammar cannot express two of them (B1) |
| E-3 · AC7 grep could not see four of five sites | HALF — AC7 exercises rather than greps | mechanism wrong for three sites, negative clause and M4 arm dropped (M4) |
| E-4 · S6 raise on a false premise | CLOSED — count stays six, AC8 names `SLACK` | — |
| E-5 · §7 wrong in both directions | HALF — three legs added, one dropped | derivation not re-run over seven files; `charter size` and `lexicon naming predicates` absent (H3, M1) |
| E-6 · §5 migration hardcodes `:263` to `--serial` | NOT FOLDED — the log says folded, the wording M2 gave was not taken | H4 |
| E-7 · AC4 has no mechanism, admits any integer, no `cost:`/`fixture:` | HALF — mechanism named, `cost:` and `fixture:` added | the count is typed, not derived; pooled pass unpriced; serial clause unsatisfiable (H1, M3) |
| E-8 · roster contradicts the chain | CLOSED — five rows, 4 → 3 → 5 → 1 → 2 | — |
| E-9 · `watch:` left-shift dropped | CLOSED — runner joins `watch:`, re-stamp listed | — |
| E-10 · cost-model paragraph misattributes the scanner | NOT FOLDED — the log lists no §4 cost-model fold | L1 |

## The eleven defects, and which rows carry each

| Defect | Descends from | Rows | Severity |
|---|---|---|---|
| F-1 · the kit runner's mode grammar is defined for `--selftests` only; no-arg and `--all` reach the same half, three carriers spell them, the parser takes one positional, and AC4 exercises none | round-2 E-2, incomplete | id=3, id=17, id=25, id=35 | blocker |
| F-2 · AC4's serial clause requires a summary that names `serial` AND is byte-identical to today's, which carries no mode token | round-2 E-7 (M3), new contradiction in the fold | id=1, id=16, id=28, id=34 | high |
| F-3 · the four-carriers clause is observed by no criterion; every AC goes green with the carriers untouched | round-2 E-2 (H1), half-folded | id=2, id=38 | high |
| F-4 · `AGENTS.md` is 18 bytes under the `charter size` cap; the `:519` rewrite adds 21; the leg is unguarded and absent from §7 | new in rev-3 (S3 named `AGENTS.md`) | id=18, id=26, id=36 | high |
| F-5 · §4 "verdict path is pooled" and §5 migration "`:263` declares `--serial`" both contradict S3 | round-2 E-1 leftover, E-6 (M2) unfolded | id=15, id=37 | high |
| F-6 · the kit runner's `--help` (`:127-130`), `tools/unattended/README.md:66` and `SESSION-KICKOFF.md:169` teach the refused form and are in no carrier or AC7 list | round-2 E-2/E-3, incomplete enumeration | id=4, id=29, id=39 | high |
| F-7 · §7 says "five touched files" against seven; `lexicon naming predicates` and the `.githooks/` self-tests are missing; siblings on the same guard hand-picked | round-2 E-5 (M1), half-folded | id=7, id=22, id=31 | medium |
| F-8 · AC4's pooled arm is green on a width-1 pool; the `peak concurrency P of outer O` line is read by nothing | new in rev-3 (AC4 rewrite) | id=5 | medium |
| F-9 · AC4 types `7` for a derived count with no `figure:`; the pooled pass has no cost figure though the record bounds it at 27200 s | round-2 E-7 (M3), fix not taken | id=42 | medium |
| F-10 · AC7's mechanism is wrong on three counts; the negative clause and the M4 source arm were dropped | round-2 E-3 (H2), one of four parts folded | id=23, id=32, id=40 | medium |
| F-11 · the cost-model paragraph still misattributes the scanner and gives two uncited figures for node `a` | round-2 E-10 (L1), unfolded | id=44 | low |

---

# BLOCKERS

## B1 · id=3, id=17, id=25, id=35 — the grammar covers one of the three routes to the selftests half, and the carriers use the other two

**Address:** section 2 S3 (the mode rule and the carriers clause) · section 6 AC4 · section 4
Files touched · section 5 migration.

Verified at source, every step. `run-unattended-gates.sh:121` is `ONLY="${1:---selftests}"`: the
no-argument invocation IS the selftests half. `:123` is `--all) ONLY="" ;;` and the selftests block
at `:257` runs under `[ "$ONLY" = selftests ] || [ -z "$ONLY" ]`, so `--all` reaches the same bare
`bash "$ROOT/tools/run-gates/run-selftests.sh" --kit tools/unattended || st=1` at `:263` that S2
makes refuse. The `case` takes ONE positional and `:160` is `*) unknown argument`, so under today's
parser `--serial` alone and `--all --serial` both exit 2 before anything runs. The usage at
`:127-128` teaches `[--selftests|--checks|--all]` and `--selftests ... (default)`.

Now the carriers S3 names. `kit.toml:125` is `bash tools/unattended/run-unattended-gates.sh` (no
argument) and `:126` is the same with `--all`; `AGENTS.md:519` is the no-argument form;
`.githooks/gate-env.sh:27` and the runner's own `:203` are `--selftests`. So of the five carrier
lines S3 says "say `--serial` in the same commit", three use a route S3 never gives a mode rule to.
`TOOL-aQuenchedHarness-4` S7 measured that "`tools/unattended/kit.toml` declares `--all` as this
kit's compensating check" and its AC6 deliberately switched from `--selftests` to `--all` on that
basis (`memory/builds/aQuenchedHarness/spec/2026-09-06-spec-TOOL-aQuenchedHarness-4.md:45-50,
:170-172`). The recorded compensating check is `--all`, and S3 defines nothing for it.

What happens depends on a choice the spec does not make. A builder who checks the mode inside the
`--selftests)` arm covers the no-arg form by accident (`ONLY` defaults to the string `--selftests`
before the `case`) and leaves `--all` bare: the five `--checks` legs run, `ran` becomes 12, `:263`
refuses, and the summary prints `unattended gates RED — 12 ran on demand` for seven suites that
never started. That is the liveness class the file's own comment at `:253-257` records this same
delegation being caught by once. A builder who checks on the resolved half (`[ "$ONLY" = selftests
] || [ -z "$ONLY" ]`, the predicate `:257` already uses) makes `--all` bare refuse — at `:263`,
after the five checks have spent their time, unless the check is moved to the parser. Either way
`kit.toml:126` must be rewritten to `--all --serial`, an invocation with no stated behaviour, and
AC4's three arms — `--selftests --serial`, `--selftests --pooled`, bare `--selftests` — exercise none
of no-arg, `--all`, `--all --serial` or `--all --pooled`. Every criterion is green in every case.

This is round 1's could-not-fail shape at the kit runner: the unit's central rule, "bare refuses,
every caller declares", is stated for one spelling of bare while the tree's dominant bare spelling
is another, and the recorded DoD has no defined form to be rewritten into.

**Fix.** S3 states the kit runner's grammar in one paragraph: a verb (`--selftests|--checks|--all`,
and say whether the no-argument default to `--selftests` is KEPT or DROPPED — kept is the smaller
diff and the carriers then read `--serial` alone, which also fits H3's byte budget) plus a mode
(`--serial|--pooled`), two positionals in either order, parsed at `:121-161` and REFUSED THERE,
before any `run_one`, so `ran` is 0 when the refusal prints. `--all` and the no-argument form take
the mode exactly as `--selftests` does; `--checks` refuses a mode the way S2's non-executing verbs
do. AC4 gains three arms: no-argument exits 2 naming both spellings and executes nothing; `--all`
bare exits 2 naming both spellings and executes NO check (red when any `--checks` leg ran first);
`--all --serial` produces both halves' verdicts, byte-identical to today's `--all` on the checks
half. The carrier edits spell `kit.toml:125` as `--selftests --serial` (or `--serial`, per the
default decision) and `kit.toml:126` as `--all --serial`. Cite `TOOL-aQuenchedHarness-4` S7 as the
record that makes `--all` primary, and add the usage at `:127-130` to Files touched (H5).

**Left-shift gate.** A spec-audit DoR check with a predicate: for every S item that adds a required
argument to a script, enumerate the script's `case` arms and every tracked invocation of its
basename (`git grep -n '<basename>'`), and require the S item to state the new argument's rule per
arm and per invocation. The mechanical half is one grep and one `sed -n '/^case/,/^esac/p'`; the
spec either lists every hit or explains each omission. Same rule as "gate the CLASS, not the
instance", applied to a CLI's routes.

---

# HIGH

## H1 · id=1, id=16, id=28, id=34 — AC4's serial clause cannot go green

**Address:** section 2 S3 (lines 36-38 against 45-46) · section 6 AC4 first clause.

Verified: `run-unattended-gates.sh:277-283` prints `unattended gates GREEN — $ran ran on demand; no
self-test here runs on the merge bar` or one of two RED variants, and none carries a mode token. S3
says both "`--selftests --serial` is today's behaviour byte-for-byte" and "under either spelling the
kit runner's summary line names the mode". AC4 repeats both for one subject: "its summary line
names `serial` ... and is byte-identical to today's bare invocation's". A line that names a mode is
not byte-identical to one that does not. One clause fails whatever is built, the spec gives no
precedence, and the builder drops whichever is cheaper — which is the silent reinterpretation this
round exists to catch. S3's "parsed from the runner's own summary line" also misnames the source:
the withheld count is on `run-selftests: $withheld cost verdict(s) WITHHELD under $SWEEP_CONDITION`
at `run-selftests.sh:745`, which is a preamble line, while the runner's summary is `sweep GREEN|RED
—` at `:748`/`:750` and carries no count. AC4's own text gets this right; S3 does not.

Two of the four rows also argue that per-suite `%5ss` seconds defeat byte-identity; that is a
misreading — AC4 speaks of the summary line, which carries no seconds — and it is not the ground
this row stands on. The contradiction is.

**Fix.** Pick one and write it in S3 and AC4 together. The one §5 observability already promises:
the kit runner's summary gains exactly one mode token under BOTH spellings, in a shape S3 states
(for instance `unattended gates GREEN — 7 ran on demand · serial; ...`), and byte-identity is scoped
to the delegated runner's pass-through output and the exit code — "identical except for the appended
mode token" in AC4's words. The alternative — the serial summary stays byte-identical and only the
pooled one names the mode — is honest too but contradicts §5 observability, which would then be
rewritten. Either way, correct S3's source line to `:745` and say whether `run-selftests.sh`'s own
serial header names its mode, since AC5's five arms assert substrings and the pass-through claim
depends on that line not moving.

**Left-shift gate.** Check 12's witness arm, tightened: a criterion whose `Red when` names
byte-identity must name the baseline it is compared against (a retained gate-log, or a same-commit
run at BASE before the change lands) or it is an assertion about nothing. A documented spec-audit
rule until the arm exists.

## H2 · id=2, id=38 — the carriers clause is observed by nothing

**Address:** section 2 S3 (the carriers sentence, "Observed by AC4 and AC5") · section 6 (absence).

Verified. S3 names the carriers — `.githooks/gate-env.sh:27`, `tools/unattended/kit.toml:125-126`,
`run-unattended-gates.sh:26-27` and `:203`, `AGENTS.md:519` — and says they "say `--serial` in the
same commit, so the verdict they name is the one that was measured". AC4 observes the kit runner's
runtime behaviour; AC5 observes five arms of `run-selftests.test.sh`; AC7's exercised set is
`run-selftests.sh --help`, three of its remedies, and `SESSION-KICKOFF.md:132`; AC8 is the
install-prefix count. No criterion reads any carrier as text. At HEAD every carrier records the
bare form that S3 makes exit 2, so all eight criteria go green with the recorded DoD invocation
refusing. Round-2 H1's fix asked for exactly this criterion — "shows each DoD line naming the
declared mode and the verdict it carries; red when any carrier still presents the pooled GREEN as
the cost check" — and rev-3 took the naming half and not the observing half. §5 migration restates
the promise but is not an observer.

The fold's central act — making the recorded DoD command the one that was measured — can be
skipped entirely with every AC green.

**Fix.** AC9: when the carrier lines (by file and line, the four S3 names plus the three H5 adds)
are read as text after the S3 commit, each names `--serial` or `--pooled` beside
`run-unattended-gates.sh` and none spells the bare form or `(default)`; red when any does. Same
shape as AC7's manifest-line clause.

**Left-shift gate.** The same grep on the bar: `tools/check-playbook-parity.sh` already
machine-compares five values against the sources that own them; a sixth pair — the kit runner's
`--help` mode list against the mode each DoD sentence names — reds a carrier that describes an
invocation the runner no longer has. Round-2 H1 named it; it is still the right gate.

## H3 · id=18, id=26, id=36 — `AGENTS.md` has 18 bytes of headroom and the `:519` rewrite needs 21

**Address:** section 4 Files touched (`AGENTS.md`) · section 7 Gates · section 2 S3 (the
`AGENTS.md:519` carrier).

Measured with the leg's own script: `bash tools/check-template-size.sh AGENTS.md` reports
`64494 / 64512 bytes (18 under)` at HEAD. `charter size` is `tools/gate-legs.json`'s unguarded
`subject = repo`, `chunk = product` leg — on every bar, branch and lander — and it is absent from
§7. `AGENTS.md:519` is `` `bash tools/unattended/run-unattended-gates.sh` `` inside backticks;
appending ` --selftests --serial`, the form AC4 exercises, is 21 bytes and reds the leg on the S3
commit at the first branch bar. ` --serial` alone is 9 bytes and fits, but under S3 as written it is
the no-arg-plus-mode form the spec does not define (B1). One row typed 20 for the 21; the arithmetic
is space, eleven, space, eight.

Nothing in the spec prices, budgets or compensates the edit. This is round-2 H3's shape — the
described edit reds a leg the criteria do not name — one file over.

**Fix.** §7 adds `charter size`. S3 or Files touched gives the `AGENTS.md:519` edit a byte budget:
net at most +18, measured with the leg at staging, and says how — the shortest declared form once
B1 defines it, or the same paragraph trimmed to pay for it (name the words). The gate's own advice
is to externalize rather than spend headroom, and this paragraph already points at `kit.toml` for
the compensating check; the shortest honest edit may be to point rather than restate.

**Left-shift gate.** Exists and is unguarded; the gap is the SPEC's. The same DoR derivation M1
asks for (legs whose guard covers a touched file or whose `argv` names it) lists this leg by
construction, since its `argv` names `AGENTS.md`.

## H4 · id=15, id=37 — §4 argues rev-2's design and §5 migration hardcodes `:263`; both contradict S3

**Address:** section 4 "Why the kit runner's verdict path is pooled and its cost path is declared"
(lines 97-105) · section 5 migration (lines 153-155) · section 9 rev-3 log.

Verified in rev-3. §4 lines 97-105 still read "The verdict path is the pooled one; the serial cost
pass is its own declared invocation" and condemn rev-1 for "leaving nothing in the tree issuing
`--pooled`", while rev-3 S3 makes every DoD carrier say `--serial` and lands `--pooled` with no
carrier naming it — which is precisely the state §4 condemns, now deliberate. The rev-3 log lists
"§4 Files" as folded and nothing else in §4, and itself calls the pooled default the round-2
blocker. A builder reading §4 wires the DoD verdict path pooled, the round-2 blocker; a builder
reading S3 does not; the spec does not say which section binds.

§5 migration still reads "the five bare-mode arms, the one bare caller and the four DoD carriers
declare `--serial` in the same commit". §4's first paragraph pins "the one bare caller" as `:263`,
and S3 requires `--selftests --pooled` to reach the runner's sweep branch, so `:263` must FORWARD the
mode the kit runner was given, not carry `--serial`. Round-2 M2 gave the replacement sentence; the
rev-3 log claims §5 migration folded; the sentence was not taken. The rev-3 log's own "the default
stays `--serial`" also contradicts S3's "bare `--selftests` REFUSES". Only AC4's pooled arm stands
between a builder following §5 and green — M2's could-not-fail shape, unchanged.

**Fix.** Rewrite the §4 subsection to rev-3's shape: the DoD verdict path is `--serial` by
declaration at the carriers; `--pooled` is a declared invocation that exists, is exercised by AC4
and by unit 3's AC4 measurement, and is named by no carrier until `TOOL-aBatchedArm-5` re-points
them; and say plainly that "nothing in the tree issues `--pooled` by a recorded DoD command" is
true and deliberate, so the spec's own argument against rev-1 is answered rather than left standing
against rev-3. Rewrite the migration bullet as M2 asked: "the five arms declare `--serial`; the one
bare caller at `:263` forwards the mode the kit runner was given, per S3; the carriers name
`--serial`". Correct the rev-3 log's "default stays `--serial`" to "bare refuses; the carriers say
`--serial`".

**Left-shift gate.** None mechanical; the documented fold rule round-2 M2 stated — every mode
assignment is stated in exactly one S item and every other mention points at it — applied this
time to §4 as well as §5. A fold log that names a section as folded while the section's binding
sentence is unchanged is the class check 12's revision-log arm could carry: for each section the
log names, the section's diff against the previous rev is non-empty.

## H5 · id=4, id=29, id=39 — three more sites teach the refused form, one of them the kit runner's own `--help`

**Address:** section 2 S3 (carriers) · section 2 S5 ("the usage line", singular) · section 4 Files
touched · section 6 AC7.

Verified at HEAD with `git grep`. `run-unattended-gates.sh:127-130` prints `usage: ...
[--selftests|--checks|--all]` and `--selftests ... (default)`: after S3 it teaches the refused form
and a default that no longer exists, and it is the first thing a person or adopter reads.
`tools/unattended/README.md:66` lists `run-unattended-gates.sh          # the kit's self-tests, ON
DEMAND ONLY` — the no-arg form, in a SHIPPED kit file, so adopters receive the stale line.
`memory/guides/SESSION-KICKOFF.md:168-169` records the owner's standing instruction as "`--checks`
yes, `--selftests` only when they ask" — the refused spelling, in a file the spec already touches
for `:132` only. None is among S3's carriers; S5 scopes "the usage line" to `run-selftests.sh`;
AC7's five sites are that runner's. `README.md` is not in Files touched.

Line 127 is one of the kit runner's four counted install-prefix literals (re-counted with the
epoch-2 regex at `check-install-prefix.sh:250`: `:127`, `:203`, and two on `:250`; the `$ROOT/`
calls at `:258` and `:263` are excluded by their lead character). So the usage line must be edited
IN PLACE — moving it to a heredoc or rephrasing it without the literal drops the count and reds the
leg `SLACK`, the exact trap round-2 H3 named for the sibling runner. Nothing in the spec says so.

**Fix.** S3 and Files touched add `run-unattended-gates.sh:127-130` (drop `(default)`, list the two
modes, keep the literal on its line), `tools/unattended/README.md:66`, and
`SESSION-KICKOFF.md:168-169` beside the four carriers. AC7 exercises `run-unattended-gates.sh --help`
the way it exercises the runner's, and reads `README.md:66` and `SESSION-KICKOFF.md:169` as text.
The SESSION-KICKOFF edit rides the `last-audit` re-stamp §4 already owes. AC8 gains
`run-unattended-gates.sh` count UNCHANGED at four.

**Left-shift gate.** The H2 grep on the bar covers `--help`; for the README and the manifest, the
`watch:` entry §4 adds for the runner should be joined by the kit runner, so the manifest ratchet
reds the next kit-runner change that leaves `:169` stale.

---

# MEDIUM

## M1 · id=7, id=22, id=31 — §7 says "five touched files" against seven, and the derivation was not re-run

**Address:** section 7 Gates, the derivation paragraph · section 4 Files touched.

Re-derived against `tools/gate-legs.json` at HEAD with the seven files §4 lists. §7 says "it reads
none of the five touched files" while §4 lists seven. Missing and matching: `lexicon naming
predicates` (`python tools/lexicon/lexicon.py`; guard `tools/`, `skills/session-kickoff/`,
`.githooks/`, `.claude/`; `subject = repo`, `chunk = declarations`, so NOT held and on every bar
whose diff touches those roots) hits five of the seven files, and `.lexicon.conf:380-383` arms the
`sh.function snake` cell with `sh.function.conv 6` pinned, so a refusal or mode-parse helper added
to either runner and named off the verb table reds a leg the spec never names.
`TOOL-aQuenchedHarness-4` rev-2 H3 already ruled that leg into §7 for work on this same runner
(`:227` of that spec). `branch-guard self-test`, `pre-push self-test` and `push-main self-test` are
guarded on `.githooks/`, which `gate-env.sh` hits, and run under the `GATE_SELFTESTS=1` bar
`gate-env.sh:28` makes the kit-work DoD; also absent. `charter size` is H3. And the listed set is
hand-picked: `run-gates canary` (guard `tools/`) is listed while `run-gates evidence`,
`install-prefix self-test`, `check-wiring self-test`, `settings-merge selftest` and the
`dead-path`/`spec-tokens`/`kit-placeholders` self-tests on the same guard are not; `run-gates gov
canary` (guard `tools/run-gates/`) is listed while `run-gates turnstile`, `run-gates adopter e2e`
and `profile-bar selftest` on the same guard are not.

Two rows overstate: `govkit acceptance matrix` is guarded on `tools/govkit/`, `tools/playbook/` and
two loose scripts, not on `kit.toml`, so that sub-claim is wrong; and "a leg not listed is not run"
is false — every missing leg is unguarded or guarded on a touched root, so the BAR runs it. What is
wrong is the spec's own statement of what grades it, made under a claim of machine derivation that
was demonstrably performed at an earlier file set. The "reds only at the lander" aside misapplies a
`.py` gotcha; a `.sh` change on the branch bar is graded there. MEDIUM on the same basis as
round-2 M1: the bar cannot miss these legs, the record does.

**Fix.** Re-derive over the seven files and state the rule used: every leg whose guard covers a
touched path or whose `argv` names one, plus the unguarded legs that read a touched file. Add
`charter size` and `lexicon naming predicates`; name the three `.githooks/`-guarded self-tests as
run by the kit-work bar; either list every guard-sibling or state the derivation lists guards, not
legs. Replace "five" with the derived count or drop the number.

**Left-shift gate.** Round-2 M1's, still unbuilt: a spec-audit DoR check that DERIVES §7 from
`gate-legs.json` against Files touched and diffs it against the authored list. The derivation is
twelve lines of python and ran for this row.

## M2 · id=5 — AC4's pooled arm is green on a pool of width one

**Address:** section 6 AC4 (pooled arm) · section 6 AC6 · section 5 observability.

Verified. AC4's pooled arm asserts the mode name and the withheld count. The count is parsed from
`$withheld cost verdict(s) WITHHELD under $SWEEP_CONDITION` (`run-selftests.sh:745`), so the width
pair is on the very line being parsed, and §5 observability promises the kit runner "repeats both".
`SELFTEST_OUTER_WIDTH=1` at `:301-315` is a live path: it yields a width-1 pool that still withholds
7 and still prints the pooled summary, as does a width-1 profile row. So `condition: pooled@1x8`,
seven withheld verdicts and `pooled` on the kit runner's summary is AC4 green with the pool serial —
exactly the shape that leaves unit 3's eight shard rows running one after another. The `peak
concurrency $SWEEP_PEAK of outer $OUTER` line at `:717` is read by nothing. The §3 turnstile
non-goal is about external contention, not the pool's own declared width, so no non-goal withholds
this. Same class as H2: a §5 promise with no observer.

**Fix.** AC4's pooled arm additionally asserts the runner's `peak concurrency P of outer O` line
with O equal to min(resolved width, row count) and P at least 2, and that the kit runner repeats
the width pair; red when O is 1 or P is 1. On a host whose resolved width is 1 the arm cannot pass,
so it SKIPS naming itself and why — a skip must announce itself.

**Left-shift gate.** The `:717` guard already reds a pool that ran WIDER than its bound; a
symmetric line — a pool declared pooled that ran at width 1 prints `POOLED AT WIDTH 1` on the
summary — is the runner-side gate, and AC4 then asserts its absence.

## M3 · id=42 — AC4 types `7` for a derived count, carries no `figure:`, and leaves the pooled pass unpriced

**Address:** section 6 AC4 (`exactly 7`, `cost:`).

Verified. AC4 states "a withheld count of exactly 7" and "the pooled count is not 7" with no
`figure:` line, while `memory/TEMPLATE-SPEC.md:352` makes `figure:` the field a criterion stating
a number must carry, and charter §7 bans a typed count of a derived population outright. Seven is
right at HEAD (`selftest-budgets.txt:110-116`) and wrong next: `TOOL-aBatchedArm-3` lands eight
shard rows under the same `--kit tools/unattended` filter next in the roster. The kit runner's own
comment at `run-unattended-gates.sh:253-257` records this exact defect — "It read `ran + 6` ...
main added a SEVENTH suite while this delegation was in flight" — and round-2 M3's fix said to pin
the figure as "withheld equals the row count `--list` reports for the filter — the `_uc` the kit
runner derives at `:258`". Rev-3 typed 7. The `cost:` line prices the serial pass at 12657 s and
the pooled pass at nothing; under the inherited bound (`sweep-ceiling-factor: 2` at
`selftest-budgets.txt:49`) the gate selftest row alone bounds the pooled wall at 13600 x 2 = 27200
s, so the pooled pass can cost more than the serial one beside it.

**Fix.** "a withheld count equal to the row count `run-selftests.sh --kit tools/unattended --list`
prints at observation time — the `_uc` the kit runner derives at `:258`" with `figure: DERIVED`;
`cost:` states the pooled bound (largest row budget times the factor, 27200 s at HEAD) beside the
serial figure.

**Left-shift gate.** Check 12's witness arm: a criterion whose `Red when` names an integer must
carry a `figure:` line. The template already declares the field; the arm that requires it is the
gate.

## M4 · id=23, id=32, id=40 — AC7's mechanism is wrong on three counts, and round-2 H2 was folded one part in four

**Address:** section 6 AC7 · section 2 S5 · section 7 New arm.

Verified against `run-selftests.sh`. AC7 says "the three printed remedies via the refusals that
print them (they interpolate `$SELF`, so a grep cannot see them)". Only `:412` is a refusal, and
it is the literal `Use the no-flag mode, which reports each suite as it finishes` — no `$SELF`, and
a grep DOES see it. `:746` (`for a cost verdict, run the serial mode: bash $SELF`) prints on every
completed sweep and `:758` (`the serial re-run: bash $SELF`) on a RED one; neither is a refusal.
The usage heredoc teaches the bare form twice — `:78` `(no flag)   run the declared population` and
`:93-94` `Use the no-flag mode for that` — not once. Round-2 H2's fix had four parts: observe emitted
bytes, list the sites by line in S5, restore a NEGATIVE clause (none says `no-flag` or `(no flag)`),
and add the M4 source arm (every `bash $SELF` in the runner is followed by a mode, staged RED first)
to §7. Rev-3 took the first. Without the negative clause AC7's predicate "every emitted or written
command names `--serial` or `--pooled`" passes `:412`, `:78` and `:93-94` unchanged, because none is
a command. §7's New arm list still omits the M4 arm. An arm builder following "via the refusals"
finds one site of three.

**Fix.** AC7 names the sites by line and trigger: `:77-78` and `:93-94` via `--help`; `:412` via
`SELFTEST_TIMEOUT_BIN=nonexistent --pooled`; `:746` via any completed `--pooled` run over the test
fixture; `:758` via a RED one (`tools/suite-red.sh` in `build_repo`); and `SESSION-KICKOFF.md:132`
as text. Restore the negative clause verbatim. Drop "they interpolate `$SELF`" or count it as two.
List the same sites in S5. Add the M4 arm to §7's New arm list.

**Left-shift gate.** The M4 arm, in `run-selftests.test.sh`: one grep over the runner asserting
every `bash $SELF` is followed by `--serial|--pooled|--check|--list|--rank`, staged RED first. It
reds the day a remedy is added without a mode, which is the class.

---

# LOW

## L1 · id=44 — the cost-model paragraph was not folded

**Address:** section 4 "What the cost model says about the goal" (lines 116-122).

Verified. Rev-3 still reads "roughly 53,000 forks at roughly 190 ms" and "On a node without the
on-access scanner (19 to 39 ms per spawn against 251 here)". `run-unattended-gates.sh:168-171`,
written on node `d`, records that the 19-39 ms node HAS the scanner: "an on-access antivirus scanner
sits in front of every exec on this node, and one spawn costs 0.019-0.039 s here against roughly a
millisecond on a machine without one". Two per-spawn figures for node `a` (190, 251) with no cite.
The rev-3 log lists "§4 Files" and no cost-model fold. Round-2 L1 survived a skeptic and was not
folded; the paragraph argues from the inverse of the record it leans on.

**Fix.** As round-2 L1 wrote it: cite `TOOL-aGradedDoorway-10`; one per-spawn figure for node `a`
with its record; "on node `d` (scanner present, 19-39 ms)".

**Left-shift gate.** None; a wording fix. The documented rule stands: a figure in a design
paragraph carries the id of the record that measured it.

---

## What a fold should do first

One paragraph precedes everything else: **the kit runner's grammar** (B1). Verb plus mode, two
positionals, refused at the parser before any `run_one`, the no-arg default kept or dropped by an
explicit sentence, `--all` and no-arg taking the mode exactly as `--selftests` does. Every other
HIGH follows from that sentence being written: H1's summary token is then a one-line shape; H2's
AC9 reads the carriers the grammar lets S3 spell; H3's byte budget is fixed by which spelling
`AGENTS.md:519` takes; H4's §4 and §5 sentences are rewritten to point at S3; H5's three sites are
added to the same lists.

After that, the mechanical set is a single pass with every line number in hand: §7 derived over
seven files with the rule stated (M1); AC4's pooled arm asserts the peak line (M2) and a derived
count with `figure:` and the 27200 s bound (M3); AC7 lists its sites by line and trigger, restores
the negative clause, and §7 gains the M4 arm (M4); one cite comes back (L1).

Four things the fold got RIGHT should not be reopened: the default no longer flips and `--pooled`
lands dark; S6 rests on the counted literal and AC8 names `SLACK`; the roster has five rows in the
4 → 3 → 5 → 1 → 2 order with unit 5 marked unspecced; the runner joins `watch:` and the re-stamp is
listed. Round-2 E-1, E-4, E-8 and E-9 were read again this round and nothing stood against them.
