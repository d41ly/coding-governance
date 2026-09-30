**Serves:** diff-review TOOL-dAlignedCarrier-6 TOOL-dAlignedCarrier-1

# dAlignedCarrier: Tier-2 closing diff review of the round-1 fold, round 2

*Node `d`, 2026-09-30, the unattended build's closing review under `memory/guides/BUILD-METHOD.md`.
Harness: `tools/workflows/tier2-review.js`, with four primed finder lenses, five skeptic batches
prompted to REFUTE each finding, and this synthesis. The subject is THE FOLD TEXT only: the round-1
fold of M1, M2, L1 and L2 into unit 6 (spec rev-4). The round-1 record is
`2026-09-30-review-TOOL-dAlignedCarrier-1-closing-diff-round1.md` in this folder.*

**Range reviewed: `3c45a567159e7156bd40a5189fd61c2ac3365d9a...e01f2ad9dee470063d7fa962c9812f34ffba5744`**
(branch `run/dAlignedCarrier`, 24 files, +813/−66).

**Round: 2.**

## Verdict: CLEAN WITH FIXES

There are no blockers. After adjudication there are no highs either. One finding was confirmed as
high, and this synthesis moved it to medium for the reasons given under M1. The report has six
items: two MEDIUM and four LOW. The fold caused all six. None is a defect that units 1 to 5 carried
in. **M1 alone stops this build from landing.** At `e01f2ad9` the unguarded codebase-map leg reds, so
the close's gates-green bar will red on it whatever else is fixed. Every item is owed a fix under
unit 6's spec before the build lands. None needs a design decision.

## Review shape and run integrity

- **Raw 13, confirmed 12, refuted 1, unverified 0, precision 0.92**, which is 12 / (12 + 1).
- **Refuted:** one raw finding, id 9, did not survive its skeptic. Its text did not reach this
  synthesis, so it appears here only as a count.
- **Adjudicated tally by item:** 6 items, which are 0 BLOCKER, 0 HIGH, 2 MEDIUM (M1, M2) and 4 LOW
  (L1 to L4).
- **Adjudicated tally by raw confirmed finding:** 0 BLOCKER, 0 HIGH, 5 MEDIUM (ids 1, 4, 7, 8, 11)
  and 7 LOW (ids 2, 3, 5, 6, 10, 12, 13). That totals 12, and each confirmed id is in exactly one
  item.
- **Severity moves:**
  - Id 7 was confirmed as high and is adjudicated MEDIUM (see M1).
  - Ids 1, 4 and 11 were confirmed as low. They take MEDIUM because they merge with id 8, which was
    confirmed as medium (see M2).
- **Merges:** the harness reported 0 duplicates, but it counts only identical findings. This synthesis
  merged findings that different lenses raised about the same defect. M2 is ids 1, 4, 8 and 11. L1 is
  ids 3, 5 and 12. L3 is ids 6 and 13. Id 10 stays its own item, L4. It is in the same scanner as L1,
  but it breaks a different contract and takes a different fix.
- **Run integrity:** lenses 4/4 returned and 0 DIED. Skeptic batches 5/5 returned and 0 DIED. No
  contradictory verdict was demoted to unverified, no spurious verdict was discarded, and there were
  0 duplicates. Every counter is zero, so **this run is complete**. The finding set is everything the
  lenses found, with no share lost to a dead lens.
- **What the synthesis checked itself:**
  - It re-read every cited site at `e01f2ad9` and re-pinned the line numbers below.
  - It ran `python tools/codebase-map/test_codebase_map.py` and `gen_map.py --check` in this
    worktree. Both are red, and M1 quotes them.
  - It reproduced L2 in a scratch repository under the session scratchpad.
  - It extracted check 47's scanner and both row patterns verbatim from the checker. With them it
    reproduced L1's wrap miss and L4's truncated excerpt. It also confirmed that a seven-word window
    closes L1 and adds no hit for either row over the 49 tracked files in the kit.
  - It confirmed that the checker's 4 deliberate raw CR bytes are unchanged between the two ends of
    the range.

## Round-1 findings: were they fixed?

| Round 1 | State at `e01f2ad9` | Where round 2 picks it up |
|---|---|---|
| M1, the half-staged record | **Fixed.** `verb_phase` now writes phase (`unattended.sh:4218`) and witness (`:4219`), and only then stages (`:4226`). Check 48 was added for the class, and no confirmed finding touches it. | none |
| M2, the under-paid bar under `primary` | **Fixed in substance** in the notice, the Close paragraph, the export line, the protocol row and both conf comments. **Incomplete** in the "While it runs" bullet. **Over-widened** into a false claim about `GATE_FULL`. | L3, M2 |
| L1, the rename-blind range read | **Fixed** for renames by `--no-renames` and for a failed diff by the unanswerable branch. The quoting half is **overclaimed**. | L2 |
| L2, check 45's stale header | **Fixed.** The header, the echo, the message and the arm moved together. Its left-shift, check 47's row 2, carries two defects of its own. | L1, L4 |

## Findings

| # | Sev | Where | What | Raw ids |
|---|---|---|---|---|
| M1 | medium | `memory/map/features/unattended.md:17` | the fold's new gotcha record is unclaimed and the map artifacts are stale, so the unguarded map leg reds | 7 |
| M2 | medium | `tools/unattended/unattended.sh:7147` | five carriers say the driver sets neither flag, but under `in-place` it adds `GATE_FULL=1` | 1, 4, 8, 11 |
| L1 | low | `tools/unattended/check-unattended.sh:5525` | check 47's six-word window is one word short of row 2's widest instance | 3, 5, 12 |
| L2 | low | `tools/unattended/unattended.sh:7134` | `core.quotepath=off` still C-quotes a path holding a tab, a quote or a backslash | 2 |
| L3 | low | `tools/unattended/SKILL.template.md:580` | the "While it runs" bullet still tells the loop to export "it" | 6, 13 |
| L4 | low | `tools/unattended/check-unattended.sh:5498` | row 2 consumes no trailing boundary, so its reported excerpt loses a byte | 10 |

### M1 — the fold's new gotcha record reds the codebase-map leg

**Where:**

- The new record is `memory/gotchas/porcelain-diff-names-a-rename-by-its-destination.md`.
- The claim list that should name it is `memory/map/features/unattended.md:17` (`gotcha-classes`).
- The stale generated files are `memory/map/generated/inventories.json` and `memory/map/generated/MAP.md`.

**Defect.** Spec S12 made the L1 class a `memory/gotchas/` record, and `gotcha-classes` is one of the
map's inventories. No dossier claims the new key, and `baseline.toml` is reserved for the initial
backfill. The fold commit touched nothing under `memory/map/`.

**Impact.** At `e01f2ad9`, `python tools/codebase-map/test_codebase_map.py` fails two tests.

- `test_every_inventory_key_is_claimed_or_baselined` fails on
  `UNCLAIMED ... {'gotcha-classes': ['porcelain-diff-names-a-rename-by-its-destination.md']}`.
- `test_generated_artifacts_are_fresh` fails on `STALE inventories.json`.
- `gen_map.py --check` exits 1 and names both `inventories.json` and `MAP.md`.

The leg `codebase-map coverage + freshness` in `tools/gate-legs.json` has no guard and its subject is
`repo`, so every bar runs it. That includes this build's in-place gates-green bar and the pre-push
bar. Nothing escapes, because the bar reds loudly before any landing. The pre-commit map leg missed it
because it triggers only on staged `*.py` and `*.js`, and its own header lists that gap under "does
NOT check" (`.githooks/pre-commit:113-116`). The fold's AC11 ran `gotchas.py --check`, which does not
read the map.

**Adjudication: MEDIUM.** Its skeptic confirmed it as high. This synthesis moved it to medium for
three reasons. The failure is certain and loud, not silent. An existing unguarded leg catches it
before any landing. The recovery is one list edit and one regeneration. That matches how round 1
calibrated its M1, which was also a deterministic refusal recoverable in one step. Even at medium it
is fixed first, because it is the one item that stops this build's landing on its own.

**Fix.** Add `"porcelain-diff-names-a-rename-by-its-destination.md"` to the `gotcha-classes` list in
`memory/map/features/unattended.md`. The kit's own defect minted the record, so that dossier is its
natural home. Then run `python tools/codebase-map/gen_map.py --write`. Commit the dossier edit together
with the regenerated `inventories.json` and `MAP.md`, and re-run `test_codebase_map.py` until every
test reports `ok`.

**Left-shift gate.** Widen the pre-commit map leg's trigger. Today it fires on staged `*.py` or `*.js`
only. It should fire on staged paths under any map inventory's source, and that set should be derived
from the map conf's inventory declarations, not typed as another glob. A commit that adds a gotcha
record then pays the leg's roughly 1.5 s at commit time instead of reaching the bar. The class is
already recorded in `memory/gotchas/hand-named-gate-list-green-while-the-bar-reds.md`. Per §7, run
the widened trigger over recent history first and print which commits it would have caught. Where a
unit's DoD mints a class record, its fold brief should also list the map claim as an acceptance item.

### M2 — "the driver sets neither flag" is false under `in-place`

**Where:**

- The runtime notice at `tools/unattended/unattended.sh:7147` ("whose bar inherits both; this driver
  sets neither").
- The header comment at `:7104-7105` ("the driver still sets neither"), four lines after `:7101` says
  the in-place close adds `GATE_FULL=1` itself.
- The Skill's Close paragraph at `tools/unattended/SKILL.template.md:949-950` ("the driver never sets,
  adds or removes either"), and its render at `.claude/skills/unattended/SKILL.md:949-950`.
- `.unattended.conf:29` and `tools/unattended/.unattended.conf.example:42` ("The driver never sets
  either flag").
- The code that contradicts all of them is `:7518`, the in-place gates-green arm:
  `run_bounded env -u GATE_WALL GATE_FULL=1 "${_genv[@]}" $GATE_CMD`.

**Defect.** Before the fold, the notice said the driver "sets it nowhere" and the Skill said it "never
sets" the flag. Both were about `GATE_SELFTESTS` alone, and both were true. The fold widened each claim
to cover both flags. For `GATE_FULL` under `in-place` that is false, and two carriers now contradict
themselves in adjacent sentences. The comment says at `:7101` that the in-place close adds
`GATE_FULL=1` itself, and then says at `:7105` that the driver still sets neither. The Skill says "never
sets, adds or removes either" and then says that under `primary` the close's bar carries "no
`GATE_FULL` of its own", which implies the in-place bar does. **The wording started in the round-1
record.** Its option (a) said "The driver still sets neither flag". Spec 6 carried that into S11
(line 85) and §8 F5 (line 352), and the fold carried it into five places. A review's recommended-fix
text is also surface nobody reviewed.

**Impact.** No runtime behaviour changes, and the export the text prescribes is correct under both
modes. But binding text now states an invariant that the code breaks. It does so in this repo's own
declared mode, since `.unattended.conf:23` declares `LANDER_MODE="in-place"` six lines above the false
comment. The error is already spreading. The brief for this very round states its security model as
"the driver never sets GATE_FULL or GATE_SELFTESTS itself", which is false for `GATE_FULL` under
`in-place`. The accurate model is that the driver never sets `GATE_SELFTESTS`, while its in-place
close adds `GATE_FULL=1` (TOOL-dDerivedDocket-3 S3). A maintainer who brings the code in line with
the text would delete that `GATE_FULL=1`. That would bring back guard-scoped grading of the landing
merge, which is the shape of two reproduced aborts. The only thing that would catch it is the barenv
arm at `tools/unattended/unattended.test.sh:8724`, and that arm is a held kit self-test, not a plain
bar leg.

**Adjudication: MEDIUM.** Id 8 was confirmed as medium, and its skeptic noted that it sits near low.
Ids 1, 4 and 11 were confirmed as low. The item stays at medium for three reasons. The Skill is
binding text. Five carriers state the claim. And it has already spread into a review brief's
security model.

**Fix.** Keep the claim to the flag that ruling TOOL-dDerivedDocket-70 covers, in all five carriers
and in spec S11 and F5 (rev-5).

- End the notice with "...whose bar inherits both; this driver never sets GATE_SELFTESTS".
- In the Skill, the comment at `:7105` and both conf comments, write: "the driver never sets
  `GATE_SELFTESTS`; under `in-place` the close adds `GATE_FULL=1` to its own bar, so the exported
  `GATE_FULL` is redundant there and is the half `primary` needs".
- In `.unattended.conf`, attribute only the `GATE_SELFTESTS` half to TOOL-dDerivedDocket-70.
- Re-render the Skill with `adopt-unattended.sh`. Then re-read the protocol byte share. The protocol
  row at `PROTOCOL.template.md:458` does not carry the overclaim and needs no edit.

No arm strands. The notice arm at `unattended.test.sh:8765` and the export-cutting `sed` at `:8819`
both stop at "into this run's one --close", before the tail that changes, and no arm quotes "sets
neither".

**Left-shift gate.** Add a row to check 47's retired-premises table for the class: "never sets" or
"sets neither" within a few words of `GATE_FULL`, or of "either flag", in a shipped kit file. Measure
it over the tree first and print hits and near-misses, because the true sentence about
`GATE_SELFTESTS` must stay green. Also add a §10 checklist entry: a fold that widens a claim from one
value to two re-reads the code path for the second value, not only the ruling behind the first.

### L1 — check 47's window is one word short for row 2

**Where:** the tail loop at `tools/unattended/check-unattended.sh:5525`
(`for (i = (k > 6 ? k - 5 : 1); ...)`), and the header claim at `:5476-5477`.

**Defect.** The scanner carries the previous six words into the next line. Row 1's widest instance is
7 tokens, so it fits even when its last word starts a line. Row 2's first alternative can be 8 tokens
wide: the mode token, up to two words, the close word, up to three words, then the announce word. A
maximal row-2 instance wrapped just before the announce word therefore escapes. The header still says
the window "holds the widest instance the pattern admits". That was true for row 1, and it stopped
being true when the fold added row 2. The "does NOT check" paragraph does not list the gap.

**Impact.** Reproduced with the scanner extracted verbatim. `# under the in-place mode the close of the
run` followed by `# announces the owed bar` gives no hit. The same words on one line give a hit, and so
does the wrap one word earlier. One legal wrap of an admitted spelling therefore passes the class gate
while the header certifies that it is covered. That is the could-not-fail shape one level up, but it
needs one exact wrap position, so it is low.

**Fix.** Keep seven words: `for (i = (k > 7 ? k - 6 : 1); i <= k; i++)`. Change the header to say
"previous seven words". A match is still reported only where it ends on the current line, so the wider
window adds no duplicate reports. The synthesis measured the widened scanner over the kit's 49 tracked
files and got no hit for either row.

**Left-shift gate.** Stage each row's widest instance wrapped at EVERY word position, as a loop in
`check-unattended.test.sh`. Assemble it from fragments like the existing row-2 arms at `:5522-5530`,
and expect that row's fail line at every position. A future row that outgrows the window then reds,
which covers the class rather than this one width.

### L2 — `core.quotepath=off` does not make the range read unquoted

**Where:**

- The range read at `tools/unattended/unattended.sh:7134`.
- Its comment at `:7113-7114` ("Paths are read unquoted").
- The new gotcha record's claims at
  `memory/gotchas/porcelain-diff-names-a-rename-by-its-destination.md:27`, `:36` and `:42`, where
  line 42 says "a path is compared as it is spelled".

**Defect.** `core.quotepath=off` stops git quoting non-ASCII bytes. Git still C-quotes any path that
holds a double quote, a backslash, a tab or a newline. Such a path under a declared prefix prints
with a leading quote, and the `"$_q"*` prefix match at `:7142` cannot match it.

**Impact.** Reproduced in a scratch repository with `core.protectNTFS=false`, which stands in for a
POSIX adopter's clone. Under `-c core.quotepath=off diff --no-renames --name-only`, the committed path
`kitsurface/a<TAB>b.sh` printed as `"kitsurface/a\tb.sh"`, and the prefix match found nothing. With
`-z` it printed raw. A range whose only touch on a declared prefix is such a path announces nothing,
which breaks the "never one fewer" promise that round 1's L1 fix restored. NTFS nodes cannot reach
this, because `protectNTFS` refuses those characters. POSIX adopters of this project-agnostic kit
can. The written guarantee is false in both the comment and a class record that other scripts will
copy.

**Fix.** Read the names NUL-delimited and keep the failure branch:
`_touched=$(set -o pipefail; GIT -c core.quotepath=off diff --no-renames --name-only -z "$_b" HEAD 2>/dev/null | tr '\0' '\n') || { ...unanswerable... }`.
A name that holds a newline then splits into pieces. Its first piece still prefix-matches, so the only
possible error is announcing too much. Correct the `:7113` comment and the gotcha record's "The fix"
paragraph so both name `-z`.

**Left-shift gate.** Add an arm that commits a tab-bearing path under the declared prefix, and
nothing else, through `update-index --index-info` with `core.protectNTFS=false`. Give it its own
scratch repository, because a Windows worktree cannot check that path out. The arm expects the
notice. Round 1 proposed a predicate for the class: a porcelain `diff --name-only` whose output is
prefix-matched must carry `--no-renames`. Extend that predicate to require `-z` as well.

### L3 — the "While it runs" bullet still says "export it"

**Where:** `tools/unattended/SKILL.template.md:580-581`, and its render at
`.claude/skills/unattended/SKILL.md:580`.

**Defect.** The bullet's closing sentence still reads "the driver still sets the flag nowhere, and you
export it into the one `--close`". Spec S6 and S11 at rev-4 require the "While it runs" bullet to name
the pair, and the fold commit's message says the pair was carried into that bullet. The fold changed
only line 571 of the bullet and left the closing sentence in the singular. A correction to raw id 13:
the rev-4 log's "S6's three mentions of the exported flag name the pair" is about the spec's own S6
text, and there it is true. The defect is that the implementation falls short of S6, not a false log
line.

**Impact.** This is the bullet a main loop is pointed at while the run is in progress. "Export it"
reads as `GATE_SELFTESTS=1` alone. Under `primary` that is exactly the under-payment round 1's M2
found. The risk is reduced by two things: the pair is named at `:571-572` in the same bullet, and the
sentence points at the Close section. But the one bullet now gives two answers.

**Fix.** Reword it to "...the driver still sets `GATE_SELFTESTS` nowhere, and you export the pair
`GATE_FULL=1 GATE_SELFTESTS=1` into the one `--close`, as the Close section spells." Use M2's
scoped wording and do not bring back "sets neither". Re-render with `adopt-unattended.sh` so the Skill
parity leg holds.

**Left-shift gate.** Round 1's M2 arm exercises the export the notice PRINTS, and no arm reads the
Skill's prose. Add a suite arm over the rendered Skill: every sentence that pairs "export" with
`--close` names both flags or says "the pair". Measure it over the tree first. Where that proves too
loose, add a §10 checklist entry instead: a fold that renames a value greps every carrier for the old
value's pronoun forms ("it", "the flag"), not only its spelling.

### L4 — row 2's reported excerpt is one byte short

**Where:** the row-2 pattern `_c47_re2` at `tools/unattended/check-unattended.sh:5498`, and the shared
scanner's report and offset at `:5521-5523`.

**Defect.** The scanner reports `substr(s, RSTART + 1, RLENGTH - 2)` and sets its end offset to
`RLENGTH - 2`. Both assume that every row's pattern consumes one trailing boundary character. Row 1
ends in `[^a-z0-9_]` and does. Row 2's alternatives end in `announc` and `close`, which consume none,
so every row-2 excerpt loses a real letter.

**Impact.** Reproduced with the extracted scanner. `# the in-place close announces the owed bar`
reports `"in-place close announ"`. The acceptance ledger's AC12 records that same truncated excerpt
without noting it (`build/2026-09-30-build-TOOL-dAlignedCarrier-6-1-acceptance-ledger.md:73`).
Detection and dedup are unaffected, because the end offset is one byte early but still on the current
line. The cost is the fail-47 message quoting text that is not the matched sentence. There is also a
per-row contract the "ONE SCANNER" header never states, which the next row will copy.

**Fix.** End both row-2 alternatives with a consumed boundary, as
`...[ ]announc[a-z]*[^a-z0-9_]` and `...[ ]in-place[^ ]*[ ]close[a-z]*[^a-z0-9_]`. The scanned window
always ends in a space, so a trailing character is always there. State the trailing-boundary contract
in the check-47 header beside "ONE SCANNER". Fix L1 and L4 in the same pass and run L1's
per-position arm after both changes, so the arm grades the scanner as it will ship.

**Left-shift gate.** The row arms at `check-unattended.test.sh:5508` and `:5527` hit only the prefix
`matches: <file>: `. Extend each to hit the full quoted excerpt of its staged sentence. `hit` is
`grep -qF` of the whole string, so a truncated excerpt then reds.

## What the finding set does not contain

No confirmed finding touches check 48's predicate. None touches `verb_phase`'s reordered staging or
the unanswerable branch of the new range read. None touches check 47's row 1, which keeps its
behaviour, or the security model's read-only property of `--status` and `--plan`. The fold's driver
changes are the `verb_phase` reorder, the range read and the notice text, and none of them is
reachable from `--status` or `--plan`. `print_selftests_owed` is called only from `verb_phase` and
from resume orientation. This run's integrity counters are all zero, so that absence is the four
lenses' own result, not the gap left by a dead lens. It is evidence at the depth those lenses went,
not proof. The one refuted finding is not described because its text did not reach this synthesis.

## Disposition and fold order

Round 1 recorded CONVERGED. BUILD-METHOD M4 says CONVERGED is terminal for its subject, and that a
finding confirmed afterwards in the fold text takes the severity rule's disposition, never another
round. Nothing here is above MEDIUM, so under that rule every item is FOLDED into spec 6 as a rev-5
bump with a §9 line. None is promoted.

1. **M1** first, because it is the one item that reds this build's own bar.
2. **M2, then L3**, in one pass over the Skill so the two sentences agree. Then re-render.
3. **L1 and L4** together, since both are in check 47's scanner. Run the per-position arm after the
   boundary change.
4. **L2**, with its gotcha-record correction in the same commit.

The fold then owes `gen_map.py --check` clean, a Skill parity check, and each item's named arm
observed red before its fix and green after. Round 1's fold produced every item in this record, which
is the fold-text-is-unreviewed-surface lesson again. The orchestrator should decide whether to verify
the rev-5 fold only by those arms, or to give it a narrow cold read as well.
