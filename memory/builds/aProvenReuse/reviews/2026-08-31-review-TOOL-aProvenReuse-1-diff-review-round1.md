**Serves:** diff-review TOOL-aProvenReuse-1 TOOL-aProvenReuse-2

# aProvenReuse — closing diff review: the built code, round 1

Round 1 · 2026-08-31 · node `a` · branch `branch/unattended-kit-gaps-a3b869` · adjudicated by one
synthesis pass over the finder/skeptic corpus, with every load-bearing claim re-verified against the
worktree at HEAD before it was written down.

**Range reviewed:** `3bfc5e877e1c416781bffa9e5bf5e1b1b7a27036...HEAD` — HEAD `62b6ec19`, five
commits, 32 files, +1933/-73.

## Verdict: BLOCKED

Two blockers, both on the same merge-bar leg, both reproduced by running that leg in this worktree:
`bash tools/check-install-prefix.sh` exits 1 at HEAD. The leg is `install-prefix (shipped surface)`
in `tools/gate-legs.json` with `subject: repo` and **no guard**, so it runs on every bar including
the push boundary. Neither red is a design defect in either unit — both are bookkeeping the diff
owed and did not pay — but the branch cannot land until they are paid.

Underneath them the two units are sound in the ways that were hardest to get right, and wrong in one
way each that the hand-verification could not have caught, because in both cases the observed RED
proves the predicate fires and says nothing about what it lets through. The high-severity pair is
exactly that shape: unit 1's gate is defeated by the shipped spec skeleton it points authors at, and
its two required facts share one blob so either can buy the other.

## Review shape

**18 raw · 11 confirmed · 7 refuted · 0 unverified · precision 0.61.** The 11 confirmed reports
consolidate to **10 distinct defects** — two independent finders reported the example-conf parity
blind spot (F9 below), and the consolidation is recorded there so a round-2 fold can attribute the
single edit that closes both.

Precision at 0.61 on a diff this small is in band. The refuted seven were mostly hypotheses about
the awk quoting and the shell pipeline that the code had already handled; they are recorded in
"Hunted, and clean" below rather than dropped, because a future reader spending tokens on the same
suspicion is the waste this section exists to prevent.

## Findings, severity-ranked

| # | Sev | Site | Defect |
|---|-----|------|--------|
| F1 | blocker | `tools/install-prefix-waivers.txt:18` | line-keyed waiver stale by one line; leg reds |
| F2 | blocker | `tools/install-prefix-carried.txt:87,98,99` | three carried-prefix rows ROSE; same leg reds again, hidden behind F1 |
| F3 | high | `tools/memory-tree/SPEC-TEMPLATE.template.md:224` | the copy-paste §10 skeleton satisfies both new conjuncts |
| F4 | high | `tools/memory-tree/check-memory-hygiene.sh:1080` | `hasT` and `hasP` scan one blob, so a terms line buys the probe half |
| F5 | medium | `tools/memory-tree/check-memory-hygiene.sh:1079` | the terms arm does not match this corpus's own idiom (15 landed specs) |
| F6 | medium | `tools/memory-tree/check-memory-hygiene.sh:1073` | no empty-population announcement; the arm grades zero specs today |
| F7 | medium | `tools/unattended/unattended.sh:3238` | kit-absent arm evaluated before the log, so a custom prefix fails toward MET |
| F8 | medium | `tools/unattended/unattended.test.sh:819` | the PREFIX arm stages the containment in the direction that cannot fail |
| F9 | medium | `tools/memory-tree/check-memory-hygiene.test.sh:1467` | example-conf parity arm cannot see bare-preset keys — including this diff's |
| F10 | low | `tools/unattended/SKILL.template.md:115` | "records neither A nor B" states AND; the gate refuses on OR |

---

### F1 — blocker — `tools/install-prefix-waivers.txt:18`

The waiver row is keyed `tools/memory-tree/README.md:108`. This diff inserted one line at
`tools/memory-tree/README.md:40` (the `SPEC10_EVIDENCE_CUTOFF` bullet), which shifted the waived
root-prefix spelling to line 109. The waiver no longer matches its hit.

Reproduced in this worktree: `bash tools/check-install-prefix.sh` exits 1 with
`a SHIPPED file spells a root-install kit path — tools/memory-tree/README.md:109`.
`git show main:tools/memory-tree/README.md | sed -n '108p'` returns the waived literal
`` `bash memory-tree/merge-rows.sh %O %A %B %P` ``, and `git diff main...HEAD -- tools/memory-tree/README.md`
shows the single +1 insertion above it.

**Fix.** Change the row to `tools/memory-tree/README.md:109`.

**Left-shift.** The registry is keyed on a line NUMBER, which is the anti-pattern hygiene check 15
already documents in its own header ("NEVER on a line number — a line number moves on unrelated
edits"). Re-key `tools/install-prefix-waivers.txt` on `(path, matched-text)` or
`(path, occurrence-count)` the way check 15's registry is keyed, and have
`check-install-prefix.sh` red on a waiver whose recorded text no longer appears in its file — that
closes the class instead of this instance, and it also closes the silently-widening variant where a
waived line is deleted and the row keeps waiving whatever moved into its slot.

### F2 — blocker — `tools/install-prefix-carried.txt:87, 98, 99`

The carried-prefix ratchet is shrink-only per file. Three rows rose:

| file | pinned | live |
|---|---|---|
| `tools/unattended/unattended.sh` | 5 | 8 |
| `tools/unattended/unattended.test.sh` | 8 | 10 |
| `tools/unattended/.unattended.conf.example` | 2 | 3 |

Measured with the gate's own emitter: `bash tools/check-install-prefix.sh --list` yields those three
live counts against the pinned rows above. The rise on `unattended.sh` is the three new
`tools/memory-recall/query.py` spellings at lines 3213, 3239 and 3270; on the conf example it is the
new comment at line 61. The awk at `check-install-prefix.sh:255` emits `ROSE <path> <pinned> -> <live>`
and `:313` counts it into `bad`.

This red hides BEHIND F1: the first arm's `[ "$bad" = 0 ] || exit 1` at `:118` fires today and
returns before the carried arm at `:226` ever runs. Fixing the waiver line alone leaves the leg red,
and the second failure will present as a new regression appearing after a "fix". The ratchet was not
regenerated with `--write-ratchet` in the same commit.

**Fix.** Resolve the memory-recall path once into a variable inside the `reuse-probed` arm (the
two-candidate kit probe already computes it) and interpolate that variable into the two `DOD_OUT`
messages, which drops `unattended.sh` back to its pinned 5; name the kit rather than the file path in
the conf-example comment. If the literals are judged deliberate — they are the remedy text an
operator pastes, so there is a real argument for spelling them — re-run
`bash tools/check-install-prefix.sh --write-ratchet`, commit the raised rows, and record WHY the rise
is sanctioned. The gate's own remedy text only sanctions re-ratcheting a DROP, so a raised row
committed without a reason is indistinguishable from an accident.

**Left-shift.** Make the leg report EVERY failing arm before exiting rather than returning at the
first — one `bad` accumulator across arms, one exit at the end. A gate that hides its second failure
behind its first turns one fix cycle into two and makes the second red look like a new regression.
That is a five-line change and it is the generalisable half of this finding.

### F3 — high — `tools/memory-tree/SPEC-TEMPLATE.template.md:224` (and its render `memory/TEMPLATE-SPEC.md:224`)

The fenced §10 copy-paste skeleton contains every magic substring the new check-12 arm looks for, so
a spec that keeps the skeleton's §10 prose satisfies BOTH conjuncts with zero recorded audit.

Verified by running the shipped predicate over the shipped bytes of `memory/TEMPLATE-SPEC.md`
lines 224-243: `hasT=1`, `hasP=1`, gate SILENT. The skeleton body carries `recall terms` (line 233,
"**The recall terms you used**"), `reuse_lookup` (line 230) and `no existing seam` (line 231). Lines
128-243 are the fenced block under "The skeleton (copy everything below this line)" — precisely what
an author copies. So the single most likely way to skip a reuse audit, writing §1-§9 and leaving §10
boilerplate, is exactly the case the gate cannot see, and check 12's own error message points that
author at this file. The same shape passes an explicit DENIAL:
`N/A — no recall terms, no probe; reuse_lookup fits nothing here` scores `hasT=1 hasP=1`, which is
the `N/A — none` class the unit was built to refuse.

Both carriers hold the same bytes and `kit-dogfood-parity.test.sh:53` pairs them, so fixing one
alone reds the bar.

**Fix.** Strip the three trigger substrings out of the FENCED skeleton and move that guidance into
the unfenced prose around the block — the skeleton body becomes
`<the seam this unit wires through, cited by path — or the explicit no-seam finding>` and
`<the terms you passed to the recall CLI, verbatim>`. Better: spell those placeholders with a token
the existing `<FAMILY-slug-seq>|YYYY-MM-DD` placeholder arm already refuses, so an unedited paste
reds on its own rather than merely failing to pass.

**Left-shift.** Add a fixture to `check-memory-hygiene.test.sh` whose §10 IS the shipped skeleton
(read from `tools/memory-tree/SPEC-TEMPLATE.template.md` at run time, never a copy) and assert it
REDS. That is the general form of the charter's "run the candidate predicate over the real tree"
rule, applied to the one input every author starts from — and reading the template rather than
copying it means the fixture cannot rot when the skeleton is reworded. Fixtures 80-84 are all built
from `good10`, never from the skeleton, which is why the suite is green over a hole.

### F4 — high — `tools/memory-tree/check-memory-hygiene.sh:1080`

`hasT` and `hasP` both scan the whole §10 body (`s10`, built at `:1073-1077`), so a recall-terms list
containing any of the five probe tokens satisfies the probe arm on its own. The probe half of the
rule is buyable with one word in the terms line.

Simulated against the exact predicate: a §10 whose entire body is
`Recall terms used: reuse-first reuse audit seam probe.` returns `hasT=1 hasP=1` and the gate is
silent — the `N/A — none` shape the unit exists to refuse, one term away. The collision is not
hypothetical and not rare: an author probing for reuse composes terms from the vocabulary of reuse,
and BOTH of this build's own specs already carry `reuse-first` inside their terms line. Neither reds
today only because a separate `reuse_lookup` paragraph happens to survive beside it — each is one
deleted paragraph away from passing on the terms line alone. The block's own comment argues the two
arms need separate fixtures because they are separate facts; the predicate does not keep them
separate.

**Fix.** Evaluate `hasP` over §10 MINUS the line that satisfied `hasT`. Cheapest form inside the
existing collection loop: two accumulators, appending a line to the probe blob only when that line
does not itself contain `recall terms` / `--terms`. Failing that, drop `reuse-first` from `hasP` — it
is the weakest of the five, and unit 2's `reuse-probed` item already surfaces a waiver at close — but
note that closes the demonstrated instance and not the class.

**Left-shift.** A fixture per conjunct is not enough here; add the CROSS fixture — a §10 that
satisfies one arm and contains the other's token only inside the first arm's line — and assert the
gate still reds. Generalise it as a rule in this build's spec practice: whenever two required facts
are graded off one text, the suite carries a fixture where one fact's text contains the other's
token.

### F5 — medium — `tools/memory-tree/check-memory-hygiene.sh:1079`

The terms arm accepts only the literal bigram `recall terms` or the flag `--terms`, and this corpus
records its terms in a different idiom. Measured for this review, by replicating the exact predicate
over every spec under `memory/builds/*/spec/` whose status header carries `Tier-2`: **254 specs, 133
fail `hasT`, and 15 of those 133 name the recall CLI and its terms inside §10 anyway** — 6 of them in
the plainest form, `with terms` / `was run with the terms`. Two read directly:

- `aPrimedKeepalive-1` §10 — ``python tools/memory-recall/query.py`` with terms
  `` `keepalive preflight orientation park discovery scope rescope amend …` ``
- `aNamedGesture-1` §10 — ``query.py`` was run with the terms
  `` `authorizing parameter prompt mode authorization gesture …` ``

Neither contains the bigram nor the flag. Both satisfy exactly what BUILD-METHOD M5 demands and
exactly what M7 step 5 re-runs, and the gate will tell them they record no terms.

The doc half diverges the same way: `SPEC-TEMPLATE.template.md` §10 says only "The recall terms you
used, verbatim, on a line naming them" and never states that the line must contain the token
`recall terms`, so an author who follows the instruction exactly can still red. Two answers to one
question, and the author reads the one that does not bind.

Nothing reds today only because `SPEC10_EVIDENCE_CUTOFF` sits ahead of every dated spec. The false
positives arrive with the first post-cutoff spec written in the dominant idiom, and that idiom is
live in specs dated as recently as 2026-08-27.

**Fix.** Add the corpus's own forms — `index(s10, "with terms")` and `index(s10, "the terms ")` cover
the six clearest instances and cost nothing — and state the required token verbatim in the §10 prose of
`tools/memory-tree/SPEC-TEMPLATE.template.md`, so the instruction and the predicate become one
answer.

**Left-shift.** The charter's rule was available and was half-run: "run a candidate gate predicate
over the real tree before wiring it, and print hits AND near-misses". The corpus figure recorded in
the check's own header measures who FAILS; nothing measured whether the ACCEPTED spellings are the
ones the corpus uses, which is the near-miss half.
Make that the documented check for every new content predicate in this file: publish the near-miss
list — the records that fail the predicate but satisfy the rule in prose — beside the failure count,
in the same commit. A predicate whose near-miss list was never printed is not landed.

### F6 — medium — `tools/memory-tree/check-memory-hygiene.sh:1073`

The evidence arm carries no empty-population announcement, and the kit's own documented adoption
instruction guarantees its population is empty at adoption.

`.memory-tree.conf:104` sets `SPEC10_EVIDENCE_CUTOFF="2026-09-01"`; no spec in the tree is dated at
or after it, so the four-conjunct guard is false for every spec. The arm grades nothing, prints
nothing, and check 12 goes green with no signal that §10 evidence was never examined. The README
bullet this diff added at `tools/memory-tree/README.md:40` instructs every adopter into exactly that
state ("Set it STRICTLY AHEAD of every dated spec on every LIVE BRANCH"), so the empty population is
guaranteed at adoption, not incidental.

The checker already handles this class twice in the same file: `pop_guard` at `:199`, and the
explicit `:1338` line for check 23 — `check 23 measured NO unit — … a green verdict here is coverage
of nothing`. Every sibling cutoff in check 12 (`STREAMS` 2026-08-09, `SPEC_WITNESS` 2026-08-15,
`FORK_MARK` 2026-08-21, `REVIEW_VERDICT` 2026-08-22) sits in the past and always grades a non-empty
population. This is the only one empty by construction, and it is the only cutoff-scoped rule in
check 12 with no liveness assertion. Charter §7, verbatim: "A probe that cannot move says so."

**Fix.** Count the specs that reach the guard; when `ecut` is non-empty and that count is zero,
print the check-23 line adapted — `memory-hygiene: check 12 graded NO spec against
SPEC10_EVIDENCE_CUTOFF <ecut> — every Tier-2 spec predates it, so a green verdict here is coverage
of nothing`.

**Left-shift.** Gate the class rather than this arm: a self-test that enumerates every
`*_CUTOFF`-guarded block in `check-memory-hygiene.sh` and asserts each one has a reachable
zero-population announcement. Four of the five siblings do not need it today only because their
cutoffs are in the past — a value nothing pins.

### F7 — medium — `tools/unattended/unattended.sh:3238`

The kit-absent arm is evaluated BEFORE the log and returns MET, so a memory-recall installed at any
path other than the two hardcoded guesses turns a core DoD item into a passing announced skip even
when the query log exists and holds evidence.

Ordering verified at `:3238-3242`: the arm tests `$ROOT/tools/memory-recall/query.py` and
`$ROOT/memory-recall/query.py`, returns 0 with an announced skip, and only THEN is the log path
derived from `git rev-parse --git-common-dir` at `:3246`. The two facts are genuinely independent —
the log location knows nothing about where `query.py` lives — so the arm fails toward MET on a core
item whenever the kit is present at neither guessed path, and its message positively asserts "this
tree ships no memory-recall kit", which is then false.

Reachable, not hypothetical: `govkit.py:818-826` accepts a top-level `prefix` (default `tools`) AND a
per-entry `kit.<eid>.prefix`, and `WIRE-INTO-PROJECT.md:589` names "an install at a `prefix` other
than the default" as a first-class attributed state. An adopter on a custom prefix closes every
unattended run on a skip that reads like coverage — the same silent-pass shape this item was built to
close for the `reuse-first` waiver, one level up.

**Fix.** Test the log first. If `$_rl` exists the kit is installed by construction, so go straight to
the join; fall through to the kit-absent skip only when the log is absent AND `query.py` is missing
at both known paths. One reorder, no new path knowledge, and it costs nothing.

**Left-shift.** Add a sixth arm to the `reuse-probed` block of `unattended.test.sh`: kit installed at
a non-default prefix, log present with one matching row, assert the message is the COUNT and not the
skip. More generally — and this is the documented check worth carrying — any DoD arm that can return
MET on an announced skip needs a fixture proving the skip is not reachable while the evidence exists.

### F8 — medium — `tools/unattended/unattended.test.sh:819`

The "PREFIX arm" that justifies `grep -xF` stages the containment in the direction that cannot fail.
It appends a row for the PARENT of the scratch tree (`dirname "$(git rev-parse --show-toplevel)"`)
while `$_rt` is the CHILD. Over lines `{/tmp/x/repo, /tmp/x}` and pattern `/tmp/x/repo`, `grep -cF`
and `grep -cxF` both return 1, so the `miss "2 recall queries"` assertion holds with `-x` deleted.
The arm's own comment ("Under a substring test both rows match and the count reads 2") states an
outcome the fixture does not produce.

The direction that actually breaks is the live one. Run in the PRIMARY tree, `$_rt` is
`C:/projects/coding-governance` and every linked-worktree row CONTAINS it as a strict prefix. Measured
for this review by running the arm's own pipeline over the real log at `.git/recall/queries.jsonl`:
121 query rows, of which `grep -cxF` counts **18** for the primary tree and `grep -cF` counts **121**
— so a substring compare would report every worktree's probes as the primary tree's and meet
`reuse-probed` off another tree's work entirely. The exact-match compare at `unattended.sh:3269` is
correct; its only guard is a staged break that never reds — the "gate you have only ever seen pass"
class, §7.

**Fix.** Invert the fixture. Append a row whose worktree is `"$(git rev-parse --show-toplevel)/sub"`
(escaped through `_rp_esc`) and keep the same `hit "1 recall query recorded"` /
`miss "2 recall queries recorded"` pair. That row contains `$_rt` as a strict prefix, counts under
`grep -cF` and not under `grep -cxF`, and the arm reds the moment `-x` is removed.

**Left-shift.** This is the diff's own instance of `staged-break-substitutes-a-synthetic-value`, and
the cheap general control is procedural, not code: a staged break must be observed RED with the
guard removed, not merely written. Record it as the documented check for every new "this is why the
compare is exact/anchored" arm — delete the operator, run the arm, confirm it fails, restore.

### F9 — medium — `tools/memory-tree/check-memory-hygiene.test.sh:1467` *(consolidates two independent reports)*

The example-conf parity arm derives its population from `${NAME:-}` reads in the engine, and
`SPEC10_EVIDENCE_CUTOFF` is a bare preset (`check-memory-hygiene.sh:55`) read bare into awk
(`-v ecut="$SPEC10_EVIDENCE_CUTOFF"` at `:810`), so the new key falls outside the only check that
enforces the `.memory-tree.conf.example` mirror — despite the comment above the arm declaring the
population to be "every `${NAME:-}` the engine reads".

Ran the arm's own derivation against the engine at HEAD: `_engreads` resolves to exactly
`{ACCEPTANCE_LEDGER_CUTOFF, ACCEPTANCE_LEDGER_GRANDFATHER, GOV_PYTHON, MAP_ROOT, SPEC10_CUTOFF}`, and
`_engkeys` (`:1443`) holds only the ten `*_CAP_*` names. Deleting `SPEC10_EVIDENCE_CUTOFF` from
`tools/memory-tree/.memory-tree.conf.example` leaves the suite green — the exact failure the arm's
own comment says it exists to prevent ("that is what happened to both ACCEPTANCE_LEDGER keys, and the
arm above passed the whole time"), one key class up.

The class already has LIVE misses, which is why this is not filed as merely cosmetic:
`FORK_MARK_CUTOFF` (`:34`) and `REVIEW_VERDICT_CUTOFF` (`:35`) are conf-overridable engine keys and
are absent from the shipped example entirely, and no other reader covers them —
`adopt-memory-tree.sh` only copies the file and `kit.toml` only pattern-matches its path. The arm
written after the ACCEPTANCE_LEDGER omission is already missing two keys it was meant to cover, and
now a third. This diff DID add its key to the example, so there is no live defect from unit 1 — only
a guard that cannot see it.

**Fix.** Widen the population to the preset block: derive names from the assignments between `set -u`
and the `. "$CONF"` source (or from the awk `-v <x>="$NAME"` bindings), union them with the existing
`${NAME:-}` set, and keep the both-directions exemption assertion so a stale exemption reds too. Then
add the two missing keys to the example in the same commit.

**Left-shift.** The widened derivation IS the gate. The one addition worth making beside it: assert
the derived population is non-empty and larger than the previous run's pin, so a future refactor that
stops matching the engine's spelling reds instead of quietly grading nothing — this arm's whole
failure mode is a selector that matches less than it believes.

### F10 — low — `tools/unattended/SKILL.template.md:115` (and its render `.claude/skills/unattended/SKILL.md:115`)

The Skill tells the agent the memory gate refuses a §10 that "records neither the recall terms nor a
probe result"; the gate refuses when EITHER is absent. "Records neither A nor B" states ¬A ∧ ¬B; the
predicate at `check-memory-hygiene.sh:1084-1087` builds `miss` from `if (!hasT)` and `if (!hasP)`
independently and prints on ¬A ∨ ¬B. The shipped `SPEC-TEMPLATE.template.md` §10 contradicts the
Skill directly: "both halves are required".

The misdirection is reachable in exactly the scenario the paragraph governs. The next sentence tells
a `reuse-first`-waived run that naming the waiver "is also how the spec lands" — but naming a waiver
only satisfies `hasP`, and such a spec still reds for the missing terms line. Two shipped documents
give different answers to one question, and the unattended agent reads the wrong one at waiver time.
Both carriers hold the sentence byte-identically, so it ships to every adopter.

**Fix.** "…refuses a spec whose §10 does not record BOTH the recall terms and a probe result", then
re-render so the byte-compare legs stay green.

**Left-shift.** Not gateable as prose logic, so it joins the documented checklist: when one document
describes another's predicate in words, the describing sentence names the boolean explicitly (BOTH /
EITHER / NEITHER) and cites the predicate's file:line, so the next reader can check the paraphrase
against its source in one hop. The deeper fix is the charter's own rule — a paraphrase and its source
are two answers to one question — but the paraphrase earns its place here because the Skill is read
where the source is not.

---

## Hunted, and clean

Recorded so a later round does not re-spend the tokens. Each was a hypothesis raised by a finder and
knocked down against the code.

- **The awk quoting.** Nothing in the new block terminates the single-quoted shell string the awk
  program lives in. The one apostrophe risk in the message text ("no existing seam fits") is inside
  escaped double quotes, not an apostrophe, and the predicate uses `index()` over a `tolower()`ed
  body rather than a regex — so there is no interval-expression or backslash-dialect surface either,
  which the block's own comment explains was deliberate.
- **The §10 body collection loop.** `in10` is reset on every `^## ` line and set only for
  `^## 10. Reuse audit`, so a later section cannot leak into `s10` and a §10 appearing twice
  concatenates rather than silently taking the last. Correct.
- **The four conjuncts.** `want == canon10` prevents grading a spec the section canon did not;
  `ecut != ""` is real blank-means-off (an empty string compares earlier than every date, so omitting
  it would arm the rule over the whole corpus); `fdate != ""` matches the sibling cutoffs. All four
  load-bearing, none redundant.
- **The `grep -c` return.** The pipeline at `unattended.sh:3266` ends `|| true` and the comparison
  reads `"${_rn:-0}" -lt 1`, so an empty or failed count degrades to 0 rather than breaking the `-lt`
  test. No non-numeric value can reach it — `grep -c` emits a bare integer or nothing.
- **`DOD_OUT` leakage between items.** The `reuse-probed` arm sets `DOD_OUT=""` as its first
  statement, before the waiver branch. No path in the arm can report a previous item's message.
- **The `ROOT` operand.** `$ROOT` already holds `--show-toplevel` (set at `:274`) and is reused
  rather than re-derived, which is the correct call under Git-Bash where `pwd` gives the MSYS
  spelling; re-deriving would have been this repo's `two-readers-of-one-config` class.
- **The JSONL escape fold.** `tr '\134' '/' | tr -s '/'` handles the two-backslash-per-separator
  bytes `json.dumps` writes, and the octal spelling avoids the GNU `tr` warning. The row filter
  `'"type": "query"'` cannot collide with `recall-opened.js`'s `"type":"opened"` — different key
  spacing, different value.
- **Scratch-tree bleed in the new unattended arms.** The five new arms leave the log removed and one
  waiver line appended to `memory/builds/tRun/RUN.md`; no later arm in the file reads either. Clean,
  though the waiver line is the one piece of residue worth watching if arms are added after it.
- **`CORE_FLOOR` and the count sentence.** `12:10 -> 12:11`, the protocol row, and the
  `Ten -> Eleven` sentence are joined in both directions by `check-unattended.sh:1512-1537`, and all
  three staged breaks were observed red by hand before this review. Re-checked, not re-derived.

## What this review did not cover

- The rendered artifacts were compared for the sentences named in F3 and F10 only. The full
  render-parity surface is a bar leg and is not re-verified here.
- Neither unit's runtime behaviour was exercised end to end in an adopter tree; F7's custom-prefix
  case is reasoned from `govkit.py` and `WIRE-INTO-PROJECT.md`, not observed.
- The seven refuted findings are summarised in "Hunted, and clean" rather than reproduced in full.
