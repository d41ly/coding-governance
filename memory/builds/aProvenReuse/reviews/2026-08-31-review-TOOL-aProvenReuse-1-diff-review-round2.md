**Serves:** diff-review TOOL-aProvenReuse-1 TOOL-aProvenReuse-2 TOOL-aProvenReuse-5

# aProvenReuse — closing diff review: the fold itself, round 2

Round 2 · 2026-08-31 · node `a` · branch `branch/unattended-kit-gaps-a3b869` · adjudicated by one
synthesis pass over the finder/skeptic corpus, with every load-bearing claim re-verified against the
worktree at HEAD before it was written down.

**Range reviewed:** `62b6ec19...HEAD` — HEAD `a32227b6`, two commits (`bbaef9bb` the round-1 fold,
`a32227b6` unit 5), 22 files, +798/-103. The subject is the FOLD, not the original diff: round 1
graded `3bfc5e87..62b6ec19` and its findings are inputs here, not targets.

## Verdict: BLOCKED

One blocker, and it is not a judgement call: `bash tools/unattended/check-unattended.sh` prints
`UNATTENDED check 22 FAILED` against this tree, naming `RECALL_CLI` in both join directions. The
leg `unattended kit gate` in `tools/gate-legs.json` carries `subject: repo` with no `guard`, so it
runs on every bar and at the push boundary. The round-1 fold introduced a gate failure the fold did
not run. Everything else can land after it, but nothing lands before it.

Underneath the blocker the shape is the one the round was called to look for and mostly found: eight
of the eleven findings are the fold's own TEXT rather than its code — a fix that closed the sentence
it was pointed at and left the other half of the same claim standing, in a protocol, a spec, a
comment, or a fixture rationale. The prior held.

**Review shape:** raw 31 · confirmed 24 · refuted 7 · unverified 0 · precision 0.77. The 24
confirmed collapse to **11 distinct defects** — four lenses independently found the same protocol
row, the same truncated comment, the same duplicated assertion and the same fixture, which is signal
about the fold's surface rather than about the corpus.

| # | Sev | Where | What |
|---|-----|-------|------|
| F1 | **blocker** | `tools/unattended/PROTOCOL.template.md:548` + render | `RECALL_CLI` added to both confs, never to §8's key table — check 22 reds in both directions |
| F2 | high | `tools/unattended/PROTOCOL.template.md:326` + render | the `reuse-probed` row still describes the deleted kit-absence arm and never names `RECALL_CLI` |
| F3 | high | `tools/memory-tree/check-memory-hygiene.sh:1092-1094` | the terms cut is per LINE, so a WRAPPED terms value still buys the probe half — the F4 hole, reopened |
| F4 | high | `…/spec/2026-08-31-spec-TOOL-aProvenReuse-2.md:254` | AC3a, §4 and §7 still specify the hardcoded-path behaviour; AC3a is false against the code AND against its own test |
| F5 | high | `…/spec/2026-08-31-spec-TOOL-aProvenReuse-1.md:53` | unit 1's spec still specifies the single-blob scan and five arms; no rev entry for the fold |
| F6 | medium | `tools/memory-tree/check-memory-hygiene.test.sh:223` | fixture 85 grades a hand-typed line, not the shipped skeleton — pins the instance, not the class |
| F7 | medium | `…/spec/2026-08-31-spec-TOOL-aProvenReuse-1.md:210` | AC6 is a delta against an assertion count the same fold moved |
| F8 | low | `tools/unattended/unattended.sh:3265` | reflow dropped "zero on a"; the comment no longer states its own conclusion |
| F9 | low | `tools/memory-tree/check-memory-hygiene.test.sh:697` | the added F4 assertion is byte-identical to line 691 |
| F10 | low | `tools/memory-tree/check-memory-hygiene.sh:1092` | terms BEFORE the finding on one line loses the finding and reds falsely |
| F11 | low | `tools/unattended/unattended.test.sh:3421` | the pin's stated premise ("`dod_met` does not clear `DOD_OUT`") is false and the fold edited that sentence |

---

## F1 — blocker — `RECALL_CLI` is configurable and undocumented, and the leg says so

`tools/unattended/PROTOCOL.template.md:548` (and its render `memory/guides/UNATTENDED-PROTOCOL.md:548`)

The fold added `RECALL_CLI` to `tools/unattended/.unattended.conf.example:74` and to this repo's own
`.unattended.conf:70`, and added no row to §8's binding conf-key table. `grep -n RECALL_CLI` over
either protocol file returns nothing. Check 22 joins three populations — the example conf, the
project conf, and the §8 first-column key set — in both directions, so it fires twice:

```
UNATTENDED check 22 FAILED — the protocol's binding key table and the declared conf disagree, so a
key is either configurable and undocumented or documented and dead.
undocumented in the protocol: RECALL_CLI | documented but in no example: none |
set by this project and undocumented: RECALL_CLI
```

That is the leg's own output on this tree, not a replication. Unit 2's S6 named this leg as the
reason S1 had to reach the protocol; the fold paid that for the DoD-item table and missed the
conf-key table in the same file.

**Fix.** Add one row after `LANDED_ANCHOR_CUTOFF` at `:548` — key, `OPTIONAL`, repo-relative path to
the recall CLI whose query log `reuse-probed` reads, BLANK means not adopted and the item reports an
announced skip — and make the byte-identical edit in `memory/guides/UNATTENDED-PROTOCOL.md`, because
check 10 diffs the pair. Then re-run `bash tools/unattended/check-unattended.sh` and confirm 10 and
22 are both green. Fold this into the same commit as F2; they are two rows of one document.

**Left-shift.** The gate that catches this already exists and already works — what failed is that
nobody ran it, because the full script did not finish inside nine minutes in this worktree. Give it a
scoped invocation next to the existing `SCOPE=only28`: a `SCOPE=docs` that runs only the static
document/conf joins (10, 16, 22 and their siblings — no git fixtures, no scratch trees) in seconds,
and name it in the kit README as the check a doc-touching commit owes before it claims done. A leg
nobody can afford to run at the moment the defect is introduced is a leg that only ever fires at the
push boundary, which is exactly what happened.

## F2 — high — the binding contract still describes an arm the fold deleted

`tools/unattended/PROTOCOL.template.md:326` and `memory/guides/UNATTENDED-PROTOCOL.md:326` (identical bytes)

The `reuse-probed` row still gives the second MET outcome as *"the memory-recall kit is ABSENT from
the tree, an announced skip"*. The driver no longer probes for a kit at all:
`tools/unattended/unattended.sh:3244` tests `[ -z "$RECALL_CLI" ] || [ ! -f "$ROOT/$RECALL_CLI" ]`
and its message names the conf key. `RECALL_CLI` appears nowhere in either protocol file.

This is the amendment-leaves-its-other-half-standing class, in the worst possible file. AGENTS.md §1
makes this document THE contract and forbids the paraphrase that would otherwise carry the
correction, so this row is the only place an operator learns the item's five outcomes. An adopter who
installs both kits and leaves `RECALL_CLI` at the shipped `""` gets a permanent announced skip on a
CORE Definition-of-Done item — the liveness half of `reuse-first` reports MET on every close in that
fleet — while the contract tells them that outcome requires a missing kit. Check 16 joins DoD item
NAMES only and its own header states it does not grade row prose, so nothing catches it.
`SKILL.template.md` and its render were updated in this same fold; this pair was not.

**Fix.** Rewrite the middle MET outcome as "the project declares no readable `RECALL_CLI` — an
announced skip, checked BEFORE the log", leave the rest of the row alone, and re-render.

**Left-shift.** One cheap join catches both F1 and F2 and is a few lines in `check-unattended.sh`:
every key in the kit's `optional_keys`/`required_keys` (`tools/unattended/kit.toml`) must appear at
least once in the protocol BODY, not merely in the §8 table. F1 is a missing table row; F2 is a row
of prose describing a mechanism whose key is never named. A key-mention join reds on both, and it
cannot be satisfied by the table alone.

## F3 — high — the widened probe blob is line-scoped, so a wrapped terms value reopens F4

`tools/memory-tree/check-memory-hygiene.sh:1092-1094`

`cutT` is computed per LINE. A terms value that WRAPS carries the marker only on its first line;
every continuation line falls through the ternary whole and lands in `s10p` intact. Reproduced with
the shipped awk — a §10 whose only content is

```
Recall terms used: `alpha beta gamma delta epsilon zeta eta theta
reuse-first reuse_lookup iota kappa`.
```

scores `hasT=1` AND `hasP=1` with no probe result recorded anywhere. That is precisely the F4 defect
this arm was widened to close: moving `reuse-first` from term 1 to term 9 makes the probe arm
unfailable again. It is not a corner case — 8-14 terms of this corpus's jargon do not fit on one
line at this file's wrap, and **all three specs in this very build wrap theirs**; they pass today
only because each also cites `reuse_lookup` in earlier prose. Fixture 80's terms value is a single
line, so the suite cannot see the hole. The doc section is wrong for the same reason:
`memory/TEMPLATE-SPEC.md:141` and its template claim the scan runs "with each TERMS VALUE removed",
which is false for a wrapped value.

**Fix.** Terminate the cut at the terms VALUE's end rather than the line's: once a line matches the
marker, keep its prefix and continue contributing subsequent lines to `s10p` as empty until a blank
line or the next `- ` bullet head.

**Left-shift.** A fixture whose terms value wraps across two lines with a probe token on the
CONTINUATION, asserting the probe arm still reds. Without it the fix is pinned for the single-line
shape only — the same instance-not-class shape as F6, one level down. Stage the break first and
confirm the fixture reds against the current code; it does.

## F4 — high — unit 2's spec still specifies the behaviour the fold replaced

`memory/builds/aProvenReuse/spec/2026-08-31-spec-TOOL-aProvenReuse-2.md:254` (also `:185-187`, `:301`)

The fold rewrote S2/S3a/S9 for the `RECALL_CLI` declaration and left the acceptance criterion
standing. AC3a still reads "with `tools/memory-recall/query.py` absent from the tree, `--close`
reports MET and the message names the missing kit". The implementation emits "declares no readable
RECALL_CLI … (declared: X)" — it names the KEY — and fires on a blank or unreadable declaration
whether or not `query.py` is present. The self-test that claims to satisfy AC3a asserts the new
string at `tools/unattended/unattended.test.sh:798`. The acceptance criterion is therefore false
against the code AND against its own acceptance evidence; §4 repeats "the message names the missing
kit rather than the missing log" and §7 still says "an adopter without the memory-recall kit".

**Fix.** Restate AC3a against the declaration (blank or unreadable `RECALL_CLI` → MET, message names
the key and the declared value), fix §4 and §7 to match, and extend the rev-5 entry, which currently
claims only S3a/S9 were re-stated.

**Left-shift.** Not gateable at proportionate cost — no checker reads acceptance prose. It goes to
the recurring-bug-class checklist as the concrete instance of
`amendment-leaves-its-other-half-standing`: when a fold changes a MECHANISM, the unit's acceptance
criteria are part of the amendment's surface, not commentary on it. The cheap documented check is a
`grep -n` for the old mechanism's vocabulary across the build folder before the fold commits.

## F5 — high — unit 1's spec was never folded at all

`memory/builds/aProvenReuse/spec/2026-08-31-spec-TOOL-aProvenReuse-1.md:53` (S3 arm P), `:65` (S7)

The header still reads `SPECCED · rev-3` and §9's revision log ends at rev-3, with no entry for
`bbaef9bb`. S3 arm P specifies the OLD single-blob scan — "the body contains `reuse_lookup` … or
`reuse-first`" — while the code now builds two blobs (`s10`/`s10p`,
`check-memory-hygiene.sh:1087-1099`). S7 enumerates five self-test arms; the suite now carries six
§10 fixtures (80-85). Unit 2 took rev-5 for its equivalent fix; unit 1 took nothing, so the spec of
record still describes the exact defect the fold's own commit message says it closed.

**Fix.** Add rev-4 to §9, restate S3 arm P as the two-blob scan (the probe half read over the
section with each terms VALUE removed, line prefix kept — and after F3, with the wrap), and S7 as six
arms including the skeleton-boilerplate fixture.

**Left-shift.** The ratchet that would catch this: red when a commit whose subject names `<unit-id>`
touches that unit's implementation files without touching its spec. That is a real gate and it is not
free — it needs the unit-id → files mapping the build folder does not currently carry. Cheaper and
honest for now: the fold checklist gains "every unit whose behaviour the fold changed takes a rev
entry, including the ones the fold did not otherwise open".

## F6 — medium — fixture 85 grades a hand-typed line, not the shipped skeleton

`tools/memory-tree/check-memory-hygiene.test.sh:223`

`evskel()` substitutes the single sentence `REPLACE both bullets. Delete this paragraph.` The real
skeleton §10 in `tools/memory-tree/SPEC-TEMPLATE.template.md` (inside the fence, and its render
`memory/TEMPLATE-SPEC.md`) is a bolded paragraph, that sentence, and two descriptive bullets. Nothing
in the suite reads the template's bytes, so the fixture's own comment — "this fixture is what stops
them moving back" — is not true of any text but that one sentence.

The class this fixture exists to gate is "skeleton boilerplate satisfies the predicate". Pinning the
instance means a later edit to the real skeleton — adding "or no existing seam fits" to the first
bullet, or a `Recall terms used:` example to the second — reopens the F3 hole while fixture 85 stays
green, because it never reads the file it guards. Verified this is a coverage gap and not a live
break: the current skeleton satisfies neither arm. Same could-not-fail shape the arm was added to
close, one level up.

**Fix.** Derive the fixture body from the source: extract the `## 10. Reuse audit` block from inside
the fenced skeleton region of `$HERE/SPEC-TEMPLATE.template.md` (the `markdown` fence opening at
`:152`, closing at `:261`) and splice THAT into the spec.

**Left-shift.** The fix IS the gate, with one condition attached: a non-empty assertion on the
extraction, so an awk range that stops matching FAILs instead of splicing nothing and passing. Note
the related open edge, which nothing exercises either way: the explanatory §10 doc section now living
ABOVE the fence contains "no existing seam fits", "reuse-first", "Recall terms used:" and `--terms`,
so a spec whose §10 is a copy of the EXPLANATION satisfies both arms. That is accepted — the skeleton
says "copy everything below this line" and the section is deliberately outside it — but it is the
reason the derived fixture must read the fenced region specifically and not the whole heading.

## F7 — medium — AC6 is a delta against a number the same fold moved

`memory/builds/aProvenReuse/spec/2026-08-31-spec-TOOL-aProvenReuse-1.md:210`

AC6 reads "S7's five arms present, and the arm count the suite reports moves by five". Counted per
commit: base `3bfc5e87` = 80 hit/miss assertions, unit 1's own landing `693eec21` = 86, so the
arithmetic was already false when the unit landed; HEAD = 88 after the fold added two §10 assertions,
and unit 5 added more to the same suite. An acceptance criterion stated as a delta on a suite-wide
count cannot be satisfied as written, and `n` is load-bearing — it is floored against
`FLOOR_ASSERTIONS` at the file's tail.

**Fix.** Restate AC6 against the arm SET — six §10 arms, each named — and leave the count to the
shrink-only floor that already owns it.

**Left-shift.** Documented check, not a gate: an acceptance criterion never states a DELTA on a
shared counter, because any concurrent unit falsifies it. State the set, or state the floor.

## F8 — low — the reflowed comment lost its predicate

`tools/unattended/unattended.sh:3265`

The fold's rewrite of "query.py logs" to "the recall CLI records" also dropped "zero on a". The
sentence now reads "…and that mismatch returns / correct run." Its only job is to record why the join
operand is `--show-toplevel` and not `pwd` — that under Git-Bash `pwd` gives the MSYS spelling while
the CLI logs a Windows path, and the mismatch returns zero on a run that actually probed. As landed
it asserts nothing, so the next reader has no stated reason not to swap the operand back, and the
fact lost is exactly the silent-zero class this item exists to avoid.

**Fix.** `…while the recall CLI records a Windows path, and that mismatch returns zero on a correct
run.`

**Left-shift.** Not worth a gate. Checklist entry, same class as F4: a reflow is an edit to the
sentence's meaning until proven otherwise, so a fold that rewords a comment re-reads the whole
sentence, not the phrase it replaced.

## F9 — low — the F4 assertion is a byte-identical duplicate

`tools/memory-tree/check-memory-hygiene.test.sh:697` (duplicate of `:691`)

Both lines are `hit  'tFixture-80.md (§10 Reuse audit does not record the probe result'`, confirmed
with `cat -A`. `hit()` greps the global `$out` and there is no intervening `out=` assignment, so 697
cannot fail unless 691 does. The real F4 coverage is the widened `evonlyt` fixture value at `:217`,
which 691 already grades. The duplicate increments `n`, which is ratcheted against
`FLOOR_ASSERTIONS`, so the suite reports one assertion of coverage that exercises nothing — a skip
that looks like a pass, in count form. The fold's commit message claims "+2 for F3 and F4"; only F3
added an independently-failing assertion.

**Fix.** Delete `:697` and move its F4 comment above `:691`, which is the assertion that carries it.

**Left-shift.** Cheap and worth it: a suite self-check that collects the argument string of every
`hit`/`miss` within one `$out` region and reds on an exact duplicate. It is a handful of lines, it
fires on the class, and this file is where a padded assertion count does the most damage.

## F10 — low — terms before the finding on one line reds falsely

`tools/memory-tree/check-memory-hygiene.sh:1092`

Same line-scoped cut as F3, opposite direction. A §10 reading `Recall terms used: \`a b c\` — no
existing seam fits.` has BOTH facts and scores `hasT=1, hasP=0`, because the cut runs from the marker
to end of line and discards the finding that follows it. The gate then reds naming as absent
something the author demonstrably wrote. The awk header comment declares only the passing direction
("a finding, then the terms — still satisfies both") and the doc section repeats it, so the remedy is
readable from neither the message nor the comment.

**Fix.** Either state the ordering constraint in the header comment and the §10 doc section, or stop
the cut at the first sentence terminator rather than end of line. The F3 fix touches this same
ternary; do both in one edit.

**Left-shift.** A fixture in the reverse order asserting SILENCE. It belongs in the same commit as
F3's wrap fixture, because both are properties of the cut and neither is currently observed.

## F11 — low — the pin's stated premise is the opposite of the code

`tools/unattended/unattended.test.sh:3421`

The comment justifying the exactly-three-skips pin says "`dod_met` does not clear `DOD_OUT` on entry,
so an item with nothing to say would otherwise inherit the previous item's text".
`unattended.sh:2814-2817` carries the comment "CLEARED ON ENTRY" followed by `DOD_OUT=""`, landed in
`570f8100`. The fold edited this exact sentence to raise the count from two to three, so the false
half was inside the amendment's own line. The same comment block calls the new outcome the
"kit-absent" one, which is the F2 vocabulary the fold retired.

**Fix.** "`dod_met` clears `DOD_OUT` on entry (`unattended.sh:2817`); this count is the second
opinion on that clearing — if it regresses, every MET item inherits the previous item's text and this
pin jumps." And say "not-adopted", not "kit-absent".

**Left-shift.** Checklist, same class as F8. Not gateable: no checker grades whether a comment's
premise matches the function it describes.

---

## Checked and found clean

Stated because a skip that looks like a pass is indistinguishable from coverage.

- **The widened parity arm (unit 5, `check-memory-hygiene.test.sh:1480-1514`).** The preset
  derivation `^[A-Z][A-Z0-9_]*_CUTOFF=` over the comment-stripped engine matches exactly seven keys,
  all genuine adopter cutoffs (`FORK_MARK`, `REVIEW_VERDICT`, `SPEC10`, `SPEC10_EVIDENCE`,
  `SPEC_FORMAT`, `SPEC_WITNESS`, `STREAMS`), and nothing it should not — the column-0 anchor keeps it
  off in-function and in-awk assignments. All seven are declared in
  `tools/memory-tree/.memory-tree.conf.example`, so the forward direction is satisfied. The union is
  additive, so the reverse direction — each `_engexempt` key (`GOV_PYTHON`, `MAP_ROOT`) must still
  appear in `_engreads` — cannot be broken by it. The new `[ -n "$_engpresets" ]` liveness assertion
  is reachable exactly as intended: it is the only thing standing between a regex that stops matching
  and a silent return to the blind spot.
- **Fixture 80 reds for the right arm.** Its assertion pins the substring `does not record the probe
  result`; when both facts are absent the message reads `does not record the recall terms used AND
  the probe result`, which does not contain it. The arm cannot be satisfied by a red for the other
  reason. Neither new fixture passes by finding nothing — 80 and 85 are both `hit` assertions on
  specific message text.
- **The rendered pairs are current.** `bash tools/memory-tree/kit-dogfood-parity.test.sh` →
  `kit-parity: shipped and installed docs agree (3 pairs)`, covering
  `SPEC-TEMPLATE.template.md` ↔ `memory/TEMPLATE-SPEC.md`. The §10 doc section moved above the fence
  in both halves. `PROTOCOL.template.md:326` and its render are byte-identical — which is why F1 and
  F2 must be fixed in both halves at once, not why they are green.
- **`RECALL_CLI`'s path contract.** An ABSOLUTE value resolves to `$ROOT//abs/path`, which does not
  exist, so it reads as not-adopted and announces itself with `(declared: …)` — the same outcome the
  suite pins for a typo'd path at `unattended.test.sh:802-804`, and deliberately so. A parent
  traversal that IS readable cannot redirect anything: the declared path is used only as an adoption
  witness and is never dereferenced, and the log is located from `git rev-parse --git-common-dir`
  independently of it. The conf example prose states REPO-RELATIVE and blank-means-not-adopted;
  `kit.toml:38` lists the key in `optional_keys`. Every part of the mechanism is documented except
  the one place the charter calls binding — which is F1 and F2.
- **The two skip messages cannot be confused.** Not-adopted returns 0 with "declares no readable
  RECALL_CLI … nothing this item could observe"; log-absent returns 1 with "the recall query log is
  ABSENT at `<path>` … cannot answer its question rather than answering it with a zero". Different
  words, different verdicts, and the suite pins each with a `miss` on the other's text.

## Environment note — not a finding

Three arms in the unattended suite's bounded-observation region failed a wall-clock assertion during
one run while other sessions on sibling worktrees ran the same suites concurrently. The range touches
zero lines of `run_bounded`, `check_wiring`, `GATE_BOUND` or `RB_OUT`, verified by grep, and those
arms passed earlier in the same session. Recorded here so a later reader does not re-derive it as a
defect of this diff.

Separately: `bash tools/unattended/check-unattended.sh` did not finish within nine minutes in this
worktree. The check-22 failure above is its own line-2 output, emitted early — the verdict does not
depend on the run completing — but the cost is the reason F1's left-shift is a scoped invocation
rather than "run the leg more often".
