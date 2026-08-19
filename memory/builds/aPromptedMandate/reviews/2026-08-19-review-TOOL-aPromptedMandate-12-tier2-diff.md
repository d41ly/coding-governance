# aPromptedMandate — Tier-2 diff review, the second closing pass

**Serves:** diff-review TOOL-aPromptedMandate-12 TOOL-aPromptedMandate-13

**Reviewed range:** `c8cee4f...HEAD` (9 commits) — the three records the first bar found stale, the
park of the `build-complete` defect, three keepalive corrections, and the two units the owner
ratified after being asked (TOOL-aPromptedMandate-12, -13). The first closing review covered
`b9ebeba..c8cee4f` and its 12 confirmed findings are already folded; that range is **not** re-reviewed
here.

**Review shape:** raw 18 · confirmed 11 · refuted 7 · unverified 0 · precision 0.61. The eleven
confirmed findings collapse to **seven distinct sites** — four independent agents landed on
`verb_landed`'s un-narrowed selector and two on `FLOOR_ASSERTIONS`, reported once each below with the
strongest reproduction attached.

**Verdict: 0 blockers, 2 high.** Both highs are unit 12's, and they are the two halves of one story:
the narrowing was applied to two of *three* readers of the `gen:build-index` region, and the arms
written to prove the narrowing sit outside the region they claim to perturb — so the one reader that
was missed is also the one the suite could not have caught.

## What holds

Verified rather than assumed, because the lens brief asks for each:

- **The narrowed selector is correct across this entire corpus.** Ran both selectors over all 50
  build READMEs under `memory/builds/*/`. Every row the narrowing drops is a record row
  (`](build/`, `](reviews/`, `](prompts/`) — zero non-record rows dropped anywhere. Builds with
  **sub-spec folders** are admitted correctly: `aDrainedSluice` and `aFoldedQuarry` link
  `]` + `(spec/units/2026-08-08-spec-….md)` and the greedy `.*` takes them. Four builds
  (`aFerriedDossier`, `aKitHardener`, `aRatchetForge`, `bThriftyBellows`) go from non-zero to zero,
  and inspection confirms their regions genuinely hold only record rows — that is the selector being
  right, not dropping units. The `.*`-over-`[^]]*` argument is sound and the bracketed-title case is
  preserved by the selector (though not by the consumer — see L1).
- **`clamp_target` mirrors run-gates' clamp for every input the loop feeds it.** Hand-evaluated both
  case chains against all five: `0`→1, `-3`→1, `nonsense`→1 (the `*[!0-9]*`-first ordering the
  comment claims, confirmed), `99999999999999999999`→64, `999999999999999999999999999999`→64. The
  `-lt 1` floor agrees too. The mirror is accurate *today*; M2 is about it staying that way.
- **The `CLAMP_BUDGET` self-tests cannot pass while their branches sit unexecuted.** Both arms read
  the verdict *message*, so a branch that does not run yields a message that does not match and the
  arm reds. The failure mode is the opposite one — a spurious red with a false cause (L2).
- **`verb_status` and `build-complete` no longer disagree about the region.** Both now route through
  `nonterminal_units`. (They still answer different questions where `unit_rows` is empty — `--status`
  prints `(no non-terminal unit)` while `build-complete` blocks on term 4 — but that is by design, not
  a second reading of the region.) The third reader is H1.

**On the build's stated claim** that every new predicate was measured firing before its arm was
written: it holds visibly for unit 13 — the commit body records two arms that caught their own author
(`timeout 0` disabling the limit rather than expiring it; a hand-rolled fixture where `bcopen`
already existed), and both sub-shapes are folded into the gotcha class. It **fails for unit 12's two
new positive arms**, which pass identically against the pre-fix selector (H2). The claim was made in
good faith and is true of the harder half; the half it is false of is the half that shipped a data
fix with no regression gate.

---

## HIGH

### H1 — `verb_landed` is a THIRD reader of the same region and kept the un-narrowed selector

`tools/unattended/unattended.sh:1154-1156`

Unit 12's own argument is that narrowing one reader while a second open-codes the same pipeline
leaves two answers to one question about one region. `unit_rows` (line 990) was narrowed and
`verb_status` (line 1443) was rerouted through it. `verb_landed` was not:

```sh
set_fact "$rel" units-at-landing \
  "$(region "$(readme_of "$slug")" "$SRC_OPEN" "$SRC_CLOSE" 2>/dev/null \
     | grep -E '^\| \[' | sed -e 's/^| \[//' -e 's/ —.*//' | tr '\n' ' ' | sed 's/ $//')" || return 1
```

Record rows carry no ` — `, so the `s/ —.*//` cut never fires on them and the whole rest of the row
survives — link target, `](build/…)` syntax, `|` column separators and all.

**Reproduced verbatim** against `memory/builds/aPromptedMandate/README.md` today. The current
pipeline emits **1162 bytes**:

```
TOOL-aPromptedMandate-1 … TOOL-aPromptedMandate-6 2026-08-18-build-TOOL-aPromptedMandate-1-anchor-reuse-reproduction.md](build/2026-08-18-build-…md) | research | TOOL-aPromptedMandate-1 TOOL-aPromptedMandate-2 | 2026-08-18-review-TOOL-aPromptedMandate-1-spec-audit.md](reviews/…) | spec-audit | … |
```

The narrowed selector on the same file emits the 8 unit ids and nothing else. `aBranchedMandate`
(13 rows / 6 units) and `aStandingWrit` (3 / 1) reproduce it.

This is worse than the two sites already fixed, on three counts. It writes a **permanent authored
fact** the function's own comment calls the thing that "keeps a terminal record a record" — no verb
re-derives it. **Nothing validates it**: `grep -rn units-at-landing` across `tools/`, the leg and the
guides finds only the writer at `unattended.sh:1154` and two assertions in the driver suite. And it
is **live-reachable now** — `memory/builds/aPromptedMandate/RUN.md` is at `phase: VERIFYING`, and its
README region already carries four record rows, so this build's own `--landed` writes the corrupted
fact. `aBranchedMandate/RUN.md` looks clean only because its region held no records table at landing.

The single arm over the fact (`unattended.test.sh:1371`) uses a fixture README with one unit row and
no records table, so it passes by finding nothing — the same class as H2 and as the gotcha this
commit extends.

**Fix.** Route it through the helper, as `verb_status` now is, and cut at the link opener rather than
only at the em dash (which also fixes the untitled-unit case, where `render_region` emits a bare id
and the current sed leaves the link and status columns attached):

```sh
set_fact "$rel" units-at-landing \
  "$(unit_rows "$(readme_of "$slug")" | sed -e 's/^| \[//' -e 's/\](.*//' -e 's/ —.*//' \
     | tr '\n' ' ' | sed 's/ $//')" || return 1
```

**Left-shift gate.** Two, and the second is the one that generalises:

1. Add a records-table row to the `--landed` fixture README (the `readme()` helper,
   `unattended.test.sh:55-74`, **inside** the marker pair — see H2) and assert `units-at-landing`
   equals exactly `ARCH-tRun-1`. Measure it red against today's code before trusting it.
2. Add a leg predicate that **enumerates the readers of a marker region and requires them to be the
   helper**: a `region … "$SRC_OPEN"` call site in `tools/unattended/unattended.sh` outside
   `unit_rows`/`nonterminal_units` and the two structural validators is a finding. This is exactly
   what `marker-contract.test.sh` already does for the four readers of the *generated-region
   markers*; the region's *row grammar* has no equivalent, and that gap is what let a third
   open-coded copy survive a fix whose whole rationale was that copies diverge.

### H2 — both new unit-12 arms append the record row OUTSIDE the region, so they pass against the pre-fix selector

`tools/unattended/unattended.test.sh:673-684`

The arms append with `>>`:

```sh
bcopen
printf '| [2026-08-01-review-ARCH-tRun-1-x.md](reviews/…) | spec-audit | ARCH-tRun-1 |\n' >> memory/builds/tRun/README.md
```

The fixture README ends at `<!-- /gen:build-index -->` (`readme()`, lines 55-74); `roster()` then
appends its block *past* that close marker (lines 266-272); and the driver never writes README.md —
every `readme_of` call site (745, 951, 1004, 1155, 1325, 1443, 1583, 1599, 1606-1607) is a read. So
`>>` lands the row at EOF, after `<!-- /roster:units -->`.

`region()`'s awk (`unattended.sh:156-163`) prints only lines strictly between the markers. **Reproduced
on the reconstructed fixture bytes**: the old `^\| \[` and the new `^\| \[.*\]\(spec/` return the
identical single CLOSED unit row, and `nonterminal_units` is empty under both.

Consequence: line 677's `miss build-complete` and lines 683-684's `--status` assertions restate the
green control at 620-622 verbatim, and would pass unchanged if `unit_rows` were reverted to `^| \[`.
The spec's S2 — *a build which carries records satisfies the item* — is unarmed, and **the shipped
data-integrity fix has no regression gate**. This is the fixture-passes-by-finding-nothing class the
same commit adds a gotcha entry for, in the arms written to prove that commit.

(The bracketed-title arm at 686-694 is unaffected by this — it `sed -i`s a row that is inside the
region — but see L1 for what it does not assert.)

**Fix.** Insert inside the region instead of appending, in both files so `records-current` stays met:

```sh
row='| [2026-08-01-review-ARCH-tRun-1-x.md](reviews/2026-08-01-review-ARCH-tRun-1-x.md) | spec-audit | ARCH-tRun-1 |'
sed -i "/^<!-- \/gen:build-index -->/i $row" memory/builds/tRun/README.md
sed -i "/^<!-- \/gen:build-index -->/i $row" memory/builds/tRun/RUN.md
```

Then **re-measure**: revert `unit_rows` to `^\| \[` locally and confirm the arm reds. An arm that has
not been seen red against the pre-fix code is not evidence.

**Left-shift gate.** A fixture-integrity assertion beside the perturbation, cheap and general: after
any arm that means to add a row to a marker region, assert the row is *in* the region before
asserting the behaviour —

```sh
same "the record row landed INSIDE the generated region" \
  "$(awk '/<!-- gen:build-index -->/{f=1;next} /<!-- \/gen:build-index -->/{f=0} f' memory/builds/tRun/README.md | grep -c 'review-ARCH-tRun-1-x')" "1"
```

This is the mechanical form of the gotcha's own advice ("break the subject deliberately and watch the
arm's message appear"): here the subject was never broken, and no message was watched.

---

## MEDIUM

### M1 — the `want_unit` control now re-derives with the PRE-FIX selector

`tools/unattended/unattended.test.sh:1162`

```sh
want_unit=$(awk '…' memory/builds/tRun/README.md | grep -E '^\| \[' | grep -vE '\| (CLOSED|WONTDO) \|' | head -1 | sed -e 's/^| \[//' -e 's/\].*//')
same "--status selects the same first row through the extracted helper" "$(run --status tRun | sed 's/.*· next //')" "$want_unit"
```

This is a re-implementation oracle whose job is to keep the extracted helper honest, and this commit
did not touch it — so it now encodes the exact selector the diff removed, and the arm asserts that
the fix *did not happen*. It passes only because `readme()`'s fixture emits a single `| [`-led row
that **is** spec-linked and carries no records table, so both selectors return the same thing. Its
own comment block still describes "the inline pipeline it replaced", a claim the unit deliberately
falsified.

Not a coverage hole — the narrowing is armed elsewhere once H2 is fixed — but a **stale and vacuous
control** in the one arm whose stated purpose is byte-identity of the extraction. It will also red
spuriously, blaming the now-correct helper, once that shared fixture gains a records row and a
non-terminal unit.

**Fix.** Narrow the control's selector to `grep -E '^\| \[.*\]\(spec/'` (it stays an independent
awk-based re-derivation, so it is not a tautology), and give the fixture a records row so the two
selectors can actually be told apart.

**Left-shift gate.** When a diff changes a pipeline that a re-implementation control mirrors, the
control must change in the same diff or the diff must say why not. Mechanically: a one-line text pin
in the suite (`grep -qF` the driver's current selector string out of `unattended.sh`) turns "the
control rotted" into a red instead of a silence — the same shape M2 asks for.

### M2 — `clamp_target` is a second, unjoined copy of run-gates' clamp, pinned only by prose

`tools/run-gates.test.sh:205-214`

The soundness of unit 13 rests on the control running at the clamp's own target width, and the only
thing joining the two spellings is the comment "mirroring run-gates.sh:81-82 INCLUDING ITS CASE
ORDER". Verified the copies agree today (see *What holds*). Verified also that **no arm can ever
observe a divergence**: at `CLAMP_BUDGET=0.05` any control width expires, at `60` any control width
finishes, and the distinguishability arm builds both messages from the same `ctw`. So a change to
run-gates' clamp — the `64`, the 5-char `?????*` bound, or the case order — sends the control to a
width nothing checks, subject and control then differ in width *as well as* clamp path, and the arm
re-accuses the clamp. That is precisely the mis-inference this unit exists to remove, restored
silently.

**Fix.** A one-line text pin beside `clamp_target`, so a change to the clamp reds the canary instead
of quietly rotting it:

```sh
grep -qF 'case "$JOBS" in *[!0-9]*) JOBS=1 ;; ?????*) JOBS=64 ;; esac' "$SCRATCH/tools/run-gates.sh" \
  || { echo "canary: run-gates' clamp moved and clamp_target still mirrors the old one"; fail=1; }
```

**Left-shift gate.** This repo already has the pattern — declared source-of-truth pairs compared
in-script, as `check-playbook-parity.sh` does for values the playbook states. The generalisable rule:
*a mirrored implementation in a test carries a text pin on the thing it mirrors, or it is not a
mirror, it is a fork.* Worth a line in the review protocol's checklist, since this is the second
mirror-rot class in this build (M1 is the first).

---

## LOW

### L1 — `verb_status` still cuts at the FIRST `]`, the case the new selector was chosen to preserve

`tools/unattended/unattended.sh:1443`

```sh
unit=$(nonterminal_units "$(readme_of "$slug")" | head -1 | sed -e 's/^| \[//' -e 's/\].*//')
```

The line unit 12 rewrote to route through the helper kept its old `s/\].*//`. Measured: piping
`| [ARCH-tRun-1 — the [bracketed] unit]` + `(spec/one.md) | OPEN | rev-1 | … |` through that exact sed
yields `ARCH-tRun-1 — the [bracketed` — truncated and bracket-unbalanced. So the selector goes out of
its way to *keep* a bracketed-title row and the consumer then mangles its label.

Low, correctly: the id survives the truncation, so `--status`/`--resume` misreport the next unit's
label to the agent rather than corrupting state. The new bracketed-title arm at 686-694 asserts only
`close OK`/`miss build-complete` and never reads the `--status` label, so it cannot see this.

**Fix.** Cut at the link opener the selector already anchors on:
`sed -e 's/^| \[//' -e 's/\](spec\/.*//'`.

**Left-shift gate.** Extend the existing bracketed-title arm rather than adding one — it already
builds the fixture:

```sh
hit "$(run --status tRun)" "next ARCH-tRun-1 — the [bracketed] unit"
```

The general rule this makes concrete: an arm that proves a row is *selected* must also read what the
consumer *printed* from it. Selection and extraction are two questions, and unit 12 armed one.

### L2 — the SPUN self-test asserts a cause it never checks, and reds falsely on a loaded host

`tools/run-gates.test.sh:268-272`

```sh
v=$( CLAMP_BUDGET=60 clamp_expired_verdict 0 2>&1 )
case "$v" in
  *"the clamp let it spin"*) ;;
  *) echo "canary: the expiry verdict did not blame the clamp when its control finished: $v"; fail=1 ;;
esac
```

`clamp_expired_verdict` returns 1 unconditionally, so the branch is selected purely by message text —
and the fallback fires for the BOTH-expired verdict too, printing "when its control finished" without
ever having checked that it did. Reachability is documented by the file's own measurement 50 lines
up: *"under four concurrent full bars this arm accused the clamp for 0, -3 and nonsense"* — same
instant fixture, same 60s budget. If the subject can expire at 60s under load, so can the width-1
control. Line 274's distinguishability arm has the same dependency and runs the fixture twice more,
for four full fixture bars at a 60s budget in this block alone.

This is the assert-a-cause-you-cannot-see shape unit 13 exists to remove, reintroduced in unit 13's
own self-test. Low because it degrades a canary rather than a gate verdict, and it fails loud.

**Fix.** Make the arm honest about what it can observe — skip loudly rather than red — and fold the
distinguishability check into the same pair of invocations so the fixture runs twice, not four times:

```sh
case "$v" in
  *"the clamp let it spin"*) ;;
  *"BOTH expired"*) echo "canary: SKIP — this host cannot finish the width-1 control inside ${CLAMP_BUDGET}s, so the spun branch is unobservable here" ;;
  *) echo "canary: the expiry verdict emitted neither outcome: $v"; fail=1 ;;
esac
```

**Left-shift gate.** The class is *a self-test whose green depends on host speed*. Cheap detector:
any arm whose subject is wrapped in `timeout` must have a third outcome for "the instrument could not
look", and must not name a cause in the message for an outcome it did not observe. Worth adding to
`memory/gotchas/fixture-passes-by-finding-nothing.md` as the mirror sub-shape — that file now
documents *fixtures that never fire*; this is *an arm that fires and names the wrong reason*.

### L3 — `FLOOR_ASSERTIONS` left at 315 while the suite grew to 341

`tools/unattended/unattended.test.sh:1800`

The unit-12 block adds six executed assertions (three arms × hit+miss) and `c8cee4f` added roughly
three more; HEAD's own commit body reports **`driver 341`** against a floor of **315**. The pin is a
per-pass ratchet in this repo by established practice, not a set-once value:
296 → 305 (`5abd9c9`, unit 1) → 307 (`b0b2b4e`, unit 2) → 315 (`8826eb2`, unit 4) — every prior unit
in this build bumped it in the pass that earned it.

26 assertions of slack defeats the pin for its canonical case. The incident it was written for
(`TOOL-cBriefedPilot-23`) stranded **nine** arms past an unconditional `exit`; 341 − 9 = 332 ≥ 315,
so a byte-identical repeat today reports green. `tools/check-testsuite-counts.sh` grades the *shape*
of the `PASS (n assertions)` line and that a floor is compared — it cannot see a stale value, so the
bar stays green.

And this same diff adds the governing lesson to `memory/guides/SESSION-KICKOFF.md`: *"a floor goes
SLACK rather than red… Commit a floor in the pass that earns it. `TOOL-aPromptedMandate-4`."* The
build is violating a rule it wrote in the same changeset.

**Fix.** Run `bash tools/unattended/unattended.test.sh`, read the `PASS (n assertions)` line, and pin
`FLOOR_ASSERTIONS` to that n in this commit.

**Left-shift gate.** `check-testsuite-counts.sh` already derives its population from
`tools/gate-legs.json` and already parses the printed count. Give it one more predicate: run each
compliant suite, compare the printed n against the floor literal in its own source, and red when the
slack exceeds a declared tolerance (0 is defensible; a small constant is defensible too). That turns
"remember to bump the floor" from a discipline into a leg — which is the only form of it this repo
has ever managed to keep.

---

## Refuted

Seven of the eighteen raw findings did not survive the skeptic pass and are recorded here only so the
next reader does not re-derive them: they alleged defects in the narrowed selector's corpus behaviour
(disproved by the 50-README sweep above), in `clamp_target`'s case ordering (disproved by
hand-evaluation of both chains), and in the reachability of the `CLAMP_BUDGET` branches (they are
reachable; L2 is the real, different problem).

## Suggested disposition

Both highs are one unit's, both are cheap, and H1 writes a permanently wrong terminal record on this
build's own landing — fix it before `--landed` runs. M1 and M2 are rot-prevention on controls that
are correct today and unpinned; they belong in the same pass as H2, since all three are the same
review touching the same two suites. L1-L3 are fold-later.
