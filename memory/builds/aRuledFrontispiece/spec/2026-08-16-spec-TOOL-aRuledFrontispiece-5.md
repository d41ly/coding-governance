# TOOL-aRuledFrontispiece-5 — the build README joins the hygiene index set at its own cap tier

**Status:** OPEN · rev-2 · 2026-08-16 · node a · Tier-2 · base 96141aed · streams tooling

## 1. Goal

The build README is the entry point of every attended and unattended build and is under no size cap
at all, while every other index in the tree is. This unit puts it under one, at a tier sized for what
it actually is, and fixes the two rendered lines that the tier would otherwise red.

## 2. Scope (IN)

- **S1** — `index_set()` in `tools/memory-tree/check-memory-hygiene.sh` gains every tracked
  `README.md` one segment under the builds directory. 39 files join checks 6 and 7.
- **S2** — check 6 gains a third class for that set: 25600 bytes, and NO line-count cap. The awk's
  per-file selection gains one branch and a zero-means-unlimited convention for the line figure, and
  the finding text drops the line half when a class carries no line cap.
- **S3** — check 7's single hardcoded 300 becomes a per-class budget: 350 characters for a build
  README, 300 for every other member. The class test is spelled ONCE, in a shell variable passed into
  both awk programs with `-v`, because two spellings of one class is the two-answers-to-one-question
  shape that put a second full expression into this same check's exemption list once already.
- **S4** — check 7 does not measure a front-matter block. Front matter is a structured value at
  column 0, not an index entry.
- **S5** — `render_region` wraps the `**Build status:**` line so a rendered line never exceeds 300
  characters, using `textwrap.fill` with `break_on_hyphens=False` and `break_long_words=False`.
- **S6** — `memory/builds/aUnmannedHelm/README.md:78` is shortened in place. It is the only authored
  line in the corpus over the new tier, at 419 characters.
- **S7** — `tools/memory-tree/check-memory-hygiene.test.sh` gains a red arm per new branch, including
  one proving a non-build index member still reds at 300 while a build README does not.
- **S8** — the four build READMEs whose `**Build status:**` line exceeds 300 characters at
  `base 96141aed` are re-rendered by `python tools/memory-tree/gen_build_index.py --write` inside
  THIS unit's commit. S5 changes what a fresh render produces, so their committed bytes stop equalling
  it the moment the wrap lands, and check 9 of `tools/memory-tree/check-memory-hygiene.sh` is
  `gen_build_index.py --check`. Deferring the re-render to a later unit leaves the merge bar red
  across every unit in between, which M6 forbids.
- **S9** — the comment at `tools/memory-tree/gen_build_index.py:534-536` is corrected in the same
  commit. It states that `LIVE.md` is in check 7's entry-budget population "and the build README's
  region is not", and S1 makes the second half false. The reason the roster renders in full there and
  as a count in `LIVE.md` survives the correction; only the stated justification changes.

## 3. Non-goals (OUT)

- Replacing the roster with a count. `TOOL-aMouldedFolio-2` S4 renders the FULL roster in the build
  README and only its COUNT in `LIVE.md` and the ledger shards, and `render_region`'s own comment at
  `gen_build_index.py:362-365` says `unit(s)` and `ids` answer different questions and are
  deliberately not reconciled. This unit WRAPS the list. Reversing that decision needs a new id
  naming the record it supersedes, per the build's own append-only rule.
- Relaxing check 7 globally. §4 records the cost.
- Touching the guides tier, the map-dossier exemptions or the run-state exemption.
- Moving `KIT_MEMORY_TREE_VERSION`. `TOOL-aRuledFrontispiece-10`, at position 10 of the build order,
  moves it once for the whole build.
- Re-rendering a README this unit's own wrap does not change. S8 carries exactly the four files whose
  rendered bytes S5 moves; the corpus retrofit — the new regions and the marker pairs that admit them
  — belongs to `TOOL-aRuledFrontispiece-10` and to `TOOL-aRuledFrontispiece-11`, at positions 10 and 9.
- Relocating an authored marker pair or authored prose in any README.
  `TOOL-aRuledFrontispiece-11` owns every authored relocation in the corpus.
- Raising 25600 to pre-pay for the regions `TOOL-aRuledFrontispiece-2`, `-3` and `-4` add at
  positions 3, 4 and 5. That measurement does not exist yet; §5 records who takes it.

## 4. Design

### Data model

Per-class caps after this unit. Only the third row is new; the first two are today's values, read
from the engine.

| Class | Check 6 bytes | Check 6 lines | Check 7 chars | Selected by |
|---|---|---|---|---|
| row index | 20480 | 250 | 300 | the default, everything not matched below |
| guide | 61440 | 750 | exempt | the guides-directory prefix |
| build README | 25600 | none | 350 | the builds prefix plus a `README.md` basename |

The build README is neither class cleanly, which is why it gets its own row rather than joining one.
It is a row document in the sense that `TOOL-aWidenedGuide-1` used — the generated region is rows a
sweep prunes — and prose in the sense that a session reads its narrative end to end. So it takes the
row byte discipline with headroom and drops the line count, which that same decision already recorded
as a proxy rather than a budget.

The measurements this design rests on, taken at `base 96141aed` over the 39 tracked build READMEs.
The over-length population is measured with check 7's OWN predicate — unfenced lines, skipping a `#`
heading and a table separator row — so it is the population the check will actually see. Figures are
UTF-8 bytes; where a line carries middots the character count differs and both are given, because
`length()` counts one or the other depending on the awk build and the comment at
`check-memory-hygiene.sh:391-395` refuses to pin it.

- No README exceeds 25600 bytes. The largest is `memory/builds/cBriefedPilot/README.md` at 24715.
- That same file is 321 lines, so a 250-line cap would red the corpus's biggest entry point on day
  one. It is the reason fork 3 carries no independent line cap, and the byte figure is the real
  budget in any case.
- Nine lines exceed 300, in six builds. FIVE are generated: the four `**Build status:**` lines, in
  `cBriefedPilot` at 577/572, `aRuledFrontispiece` at 354/349, `aUnmannedHelm` at 331/326 and
  `aSealedCaravan` at 327/322, plus `cBriefedPilot`'s `ids:` front-matter line at 479. FOUR are
  authored: `aUnmannedHelm/README.md:78` at 419/412, `bConvergentLodestar/README.md:28` at 309/305,
  `aPrunedCeremony/README.md:97` at 305 and `aPrunedCeremony/README.md:47` at 303/299.
- The 350 tier has to be justified by what SURVIVES this unit, not by the raw population. S5 wraps
  every generated status line, S4 excludes the front-matter line, and S6 shortens the one authored
  line above the tier. What is left is three authored lines in two builds, at 309, 305 and 303 bytes
  — a markdown table row twice and a scope bullet once, none of which can be wrapped without breaking
  its structure. That is what the 350 tier buys. An earlier revision counted two of the generated
  status lines among the authored five and so justified the tier with lines this same unit removes.
- Four lines exceed 350 by byte count and three by character count; the difference is
  `aRuledFrontispiece`'s status line at 354/349. Three of the four are generated and S5 or S4 disposes
  of each. The one authored line above the tier is `aUnmannedHelm/README.md:78`, which S6 shortens.

Both checks measure the WORKING TREE, and `memory/backlog/TOOL.md:5` records `TOOL-aRootedPrefix-3`
as OPEN against exactly that: checks 6 and 7 measure raw working-tree bytes, so an adopter without an
`eol=lf` pin gets a platform-dependent cap and entry budget. This unit INHERITS that row for the new
class rather than closing it, and the inheritance is asymmetric. Check 7's awk already strips a
trailing CR at `check-memory-hygiene.sh:405`, so the 350 entry budget is CR-safe on any checkout.
Check 6's `wc -c` at `check-memory-hygiene.sh:354` is not: on a CRLF checkout every line costs one
more byte, so the largest README measures 25036 rather than 24715 and the 885 bytes of headroom this
section prices become 564. In this repo `.gitattributes` pins `memory/**/*.md text eol=lf`, so no
verdict moves here; for an adopter the new class is one more population under that open row.
Normalising before measuring is the row's own scope and would re-decide all three classes at once,
which is a change none of S7's arms cover.

### Inventory

Five sites move.

`index_set()` gains one `grep -E` line beside the existing run-state and guides lines. Because it is
computed once and read by both checks, the population question is answered in one place.

Check 6's awk gains one branch. Today it sets `cb = 20480; cl = 250` and overrides both for the
guides prefix; it gains a third case and the convention that `cl = 0` means no line cap, which the
comparison and the finding string both honour. A zero cap that read as "cap of zero" would red every
file, so the guard and the message move together.

Check 7's awk gains a per-file cap and a front-matter skip. The cap is one ternary over a class
prefix passed in with `-v`. The skip walks the leading `---` block exactly as `parse_front_matter`
does — line 1 only, closing at the first `---` — and counts those lines in the unfenced numbering so
reported line numbers do not shift. The failure text names the budget it applied, so a finding says
which tier judged it.

`render_region` wraps its first line. `textwrap.fill` returns its input unchanged when the input
already fits, so the wrap is inert for the 35 READMEs whose status line is under the width and
re-renders exactly four: `aSealedCaravan` at 327, `aUnmannedHelm` at 331, `aRuledFrontispiece` at 354
and `cBriefedPilot` at 577. Those four files are S8, and they land in this unit's own commit.
`render_live` and `render_shards` are untouched: `TOOL-aMouldedFolio-2` S4 renders a COUNT there, not
the roster, so no line they emit approaches the width. The comment stating that reason at
`gen_build_index.py:534-536` is the fifth site, and S9 corrects its second half.
`break_on_hyphens=False` is load-bearing rather than defensive — the default splits a
family-slug-sequence id at a hyphen and would put half an id at the end of a line, which is the one
output shape that must never appear in a roster.

The wrap width is 300, deliberately BELOW every cap in the check, for two reasons. Check 7's own
comment at `check-memory-hygiene.sh:391-395` records that `length()` counts characters or bytes
depending on the awk build and the ambient locale, and refuses to pin the locale; the status line
carries six middots, so a render sitting exactly at the cap would pass on one node and red on
another. And a generator whose output clears the UNRELAXED 300 budget leaves the relaxed tier to do
only what it exists for, which is authored lines. It is not a second spelling of the cap: the
relation between them is an inequality, not an equality, and a wrap width that ever exceeded the cap
would be caught by check 7 on the very next render.

### Migration

One authored line is edited, in `memory/builds/aUnmannedHelm/README.md`. Four READMEs re-render, and
that re-render is THIS unit's commit — the four `**Build status:**` carriers S8 names. The rendered
bytes of every other README are unchanged, so the commit's generated diff is exactly those four files
and `--check` is clean at this unit's tip.

Rules 6 and 7 of the hygiene rule-set move in the render DIRECTION the parity harness declares:
`tools/memory-tree/HYGIENE.template.md` is the authored source and `memory/HYGIENE.md` is this repo's
dogfood render of it. `kit-dogfood-parity.test.sh:30-32` states that direction and refuses a
hand-edited live copy. So the edit is to the template, followed by
`bash tools/memory-tree/kit-dogfood-parity.test.sh --render`; the two files are not byte-identical
and never were, because the render substitutes this install's kit prefix.

### Alternatives rejected

**Bumping check 7's 300 to 350 globally.** Rejected: that check's population is
`memory/DECISIONS.md`, `memory/LIVE.md`, the ledger shards, the backlog shards and the per-build
status files, and every one of those is a curation surface where the entry budget is the discipline
rather than an obstacle to it. `TOOL-aWidenedGuide-1` made exactly this argument when it refused to
triple the row cap along with the guide cap; this is the same argument for a second class.

**Wrapping the `ids:` front-matter line.** Impossible, not merely undesirable. `parse_front_matter`
at `gen_build_index.py:159` refuses an indented continuation — its message is that keys live at
column 0 and an indented key is silently dropped by every simple parser — and refuses a column-0 line
with no colon. Awk readers in the unattended kit parse the same block for a run's declared slug. A
continuation there is a parser change touching every reader, not a renderer change. The value also
grows one id per unit without bound, so no literal cap on that line has a stable answer. The
exclusion in S4 is therefore the remedy, and it is general rather than a carve-out: measured at
`base 96141aed`, no file in the index set today opens with front matter, so the rule changes no
current verdict and takes effect only for the class S1 admits.

**A `memory/project/curation-debt.txt` row for the one authored over-length line.** Rejected: that
registry is empty today and its own header says an empty file means fully strict. Trading a one-line
edit for the first row in a grandfather list spends a discipline to save an edit.

**Raising the byte cap now.** Rejected as speculative. §5 records the risk and names who measures it.

### Files touched (estimate)

`tools/memory-tree/check-memory-hygiene.sh` · `tools/memory-tree/check-memory-hygiene.test.sh` ·
`tools/memory-tree/gen_build_index.py` and its `--selftest` arms ·
`tools/memory-tree/HYGIENE.template.md` rules 6 and 7, with `memory/HYGIENE.md` re-rendered from it ·
one line of `memory/builds/aUnmannedHelm/README.md` · the generated region of
`memory/builds/aSealedCaravan/README.md`, `memory/builds/aUnmannedHelm/README.md`,
`memory/builds/aRuledFrontispiece/README.md` and `memory/builds/cBriefedPilot/README.md`.

## 5. Production-readiness checklist

- security — N/A. No new input crosses a trust boundary; the checks read tracked files already read.
- perf / scale — 39 files join two awk passes that are already batched over the whole set, so the
  cost is one open per file and no new fork.
- a11y — N/A. No user-facing surface.
- i18n — the wrap width carries a deliberate margin because `length()` is character-or-byte depending
  on the awk build and locale, which check 7's own comment refuses to pin.
- error / empty / loading states — an empty build README, one with no generated region, and one whose
  front matter is the whole file are each legal and each an arm.
- observability — every finding names the file, the unfenced line number, the measured size and the
  budget that judged it, so an operator can tell which tier fired.
- risks — the byte headroom is 885 on the largest README and the wrap does not spend it: each break
  consumes the space it replaces, so `cBriefedPilot`'s status line measures 577 bytes before and after
  and wraps to two lines of at most 291 bytes. What does spend it is `TOOL-aRuledFrontispiece-2`,
  `-3` and `-4`, each adding a generated region to every README that opts in; an order region for 22
  units alone plausibly exceeds
  885, so the cap is expected to BIND at the retrofit at position 10, which takes that measurement.
  The resolution there is a shorter render or an owner fork on the number, never a silent bump.
  Separately, S8 re-renders `memory/builds/aSealedCaravan/README.md`, whose sibling `RUN.md` is a copy
  of that README slice compared by check 8 of `tools/unattended/check-unattended.sh`; that run-state
  file is `phase: LANDED`, which is the terminal-phase carve-out fork 7 resolved and
  `TOOL-aRuledFrontispiece-8` builds at position 2 of the build order. This unit is position 6, so the
  carve-out is in place before the re-render lands. The other run-state file, under `aSiftedPlaybook`,
  has a 264-character status line and does not rewrap.
- testing + left-shift gates — a red arm per new branch in the hygiene test, plus wrap arms in the
  generator's `--selftest`.
- migration / rollback — revert is three source files, the rule-set template with its render, one
  authored line, and the generated region of the four READMEs S8 re-renders; reverting the source
  without the render, or the render without the source, reds check 9 either way, so the commit is the
  rollback unit.
- user docs — rules 6 and 7 of `HYGIENE.md` gain the third class, paired with the kit template.

## 6. Acceptance criteria

- **AC1** — When `bash tools/memory-tree/check-memory-hygiene.sh --print-index-set` runs at this
  unit's tip, its output contains `memory/builds/cBriefedPilot/README.md`, and
  `bash tools/memory-tree/check-memory-hygiene.sh` exits 0 over the corpus.
- **AC2** — When a fixture build README exceeds 25600 bytes,
  `bash tools/memory-tree/check-memory-hygiene.sh` fails check 6 naming that file with the byte
  figure and its 25600 budget, and with no line figure in the message.
- **AC3** — When a fixture build README carries 400 lines and fewer than 25600 bytes,
  `bash tools/memory-tree/check-memory-hygiene.sh` reports nothing for it under check 6.
- **AC4** — When a fixture build README carries a 360-character authored line outside its front
  matter, `bash tools/memory-tree/check-memory-hygiene.sh` fails check 7 naming the file, the
  unfenced line number and the 350 budget.
- **AC5** — When a fixture build README carries a 400-character `ids:` line inside its front matter,
  check 7 passes, and when the same line is moved below the closing `---` it fails.
- **AC6** — When a fixture `memory/backlog/` shard carries a 310-character line, check 7 still fails
  at 300, proving the relaxation is per-class and not global.
- **AC7** — When `python tools/memory-tree/gen_build_index.py --write` runs over a build whose roster
  makes the status line exceed 300 characters, every rendered line of the region is at most 300
  characters and no line begins or ends with a fragment of an id.
- **AC8** — When `python tools/memory-tree/gen_build_index.py --write` runs over a build whose status
  line is already under the width, the README is byte-identical to its render at `base 96141aed`.
- **AC9** — When `bash tools/memory-tree/check-memory-hygiene.test.sh` runs, it passes and its check-7
  `hit` assertion names the new per-class wording rather than `index entry lines over 300 chars`.
- **AC10** — When `python tools/memory-tree/check-arms.py` runs, it passes with
  `memory/project/unarmed-branches.txt` still holding one row, because this unit adds no new
  `fail` call site and the reworded check-6 and check-7 messages carry armed signatures.
- **AC11** — When every unfenced line of `memory/builds/aUnmannedHelm/README.md` is measured at this
  unit's tip, none exceeds 350 characters.
- **AC12** — When `python tools/memory-tree/gen_build_index.py --check` runs at this unit's tip it
  exits 0, and `git diff --name-only 96141aed..HEAD -- 'memory/builds/*/README.md'` lists exactly
  `aRuledFrontispiece`, `aSealedCaravan`, `aUnmannedHelm` and `cBriefedPilot` — the four S8 carries,
  and no fifth.
- **AC13** — When `bash tools/memory-tree/kit-dogfood-parity.test.sh` runs at this unit's tip it
  passes, with rules 6 and 7 edited in `tools/memory-tree/HYGIENE.template.md` and `memory/HYGIENE.md`
  produced by `--render` rather than by hand.

## 7. Gates

`bash tools/memory-tree/check-memory-hygiene.sh`, whose check 9 is the one S8 exists to keep green —
it delegates to `gen_build_index.py --check` at `check-memory-hygiene.sh:464` and reds on any README
whose committed bytes differ from a fresh render ·
`bash tools/memory-tree/check-memory-hygiene.test.sh` ·
`python tools/memory-tree/check-arms.py`, because both reworded messages change their signatures and
`ARMS_FLOORS` pins this engine at `tools/memory-tree/check-memory-hygiene.sh:14:14` ·
`python tools/memory-tree/gen_build_index.py --selftest` ·
`bash tools/memory-tree/kit-dogfood-parity.test.sh` for the paired `HYGIENE.md` edit ·
`bash tools/unattended/check-unattended.sh` for the run-state copy check ·
`bash tools/memory-tree/check-verdict-epoch.sh`, which `TOOL-aRuledFrontispiece-10` discharges for
the whole build.

## 8. Open questions

none — fork 3 resolved membership and both cap figures, and the build README resolved that the roster
is wrapped rather than counted; §4 verifies the mechanisms behind both and §5 hands the one open
measurement, the byte headroom after `TOOL-aRuledFrontispiece-2` through `-4` render, to the unit at
position 10 rather than reopening a number the owner set.

The build README's park P2 — whether front matter is measured at all, which is S4 and is wider than
the words fork 3 used — is RESOLVED (owner, 2026-08-16): exclude the front-matter block from check 7's
measurement. S4 is built as written and no fork returns here. `TOOL-aRootedPrefix-3` stays OPEN and is
inherited rather than resolved; §4 records the inheritance and what it costs an adopter.

## 9. Revision log

- rev-1 · 2026-08-16 · initial draft.
- rev-2 · 2026-08-16 · folded the M4 spec audit (`reviews/2026-08-16-review-aRuledFrontispiece-1.md`).
  BLOCKER "S5's wrap reds hygiene check 9 at its own tip": four READMEs carry a status line over 300,
  not three, so the re-render becomes S8 and lands in this unit's own commit; the §3 deferral and the
  §4 Migration handoff are gone, and §4 Inventory and §5 name four files. MEDIUM "the 350 tier's
  justification counts two GENERATED lines this unit wraps": §4's population is re-measured with check
  7's own predicate and the tier is now justified by the three authored lines that SURVIVE the wrap.
  MEDIUM "a new byte class inherits an OPEN row about raw working-tree measurement":
  `TOOL-aRootedPrefix-3` is cited at `memory/backlog/TOOL.md:5` and the inheritance is recorded,
  asymmetric between the two checks and quantified for an adopter. MEDIUM "byte-paired edit inverts
  the parity harness's render direction": §4 Migration now says edit the template, then `--render`.
  Park P2 marked RESOLVED (owner, 2026-08-16) in §8. Two defects found while folding and folded here:
  the comment at `gen_build_index.py:534-536` becomes false the moment S1 lands, which is S9, and §5's
  migration bullet claimed no generated bytes change in this commit.

## 10. Reuse audit

Recall terms used, recorded so a resumed session re-runs the same query: `index set byte cap line cap
entry budget per-class guides tier grandfather curation debt front matter column zero roster wrap
truth-blind`.

The map probe for "per-class byte and line cap over an index file set" returned no engine outside
`tools/memory-tree/check-memory-hygiene.sh` itself; the ranked hits were the codebase-map render
functions and the recall query budget, neither of which measures a document against a cap. The
per-class mechanism this unit extends is therefore the only one in the corpus, which is the reason
the change is a branch inside it rather than a new predicate beside it.

| Behaviour needed | Existing seam | Decision |
|---|---|---|
| select the capped population once | `index_set()` at `check-memory-hygiene.sh:322` | EXTEND — one more line in the same subshell, still computed once for both checks |
| choose a cap per file class | check 6's awk at `check-memory-hygiene.sh:363-371` | EXTEND — the guides branch is the pattern; a third case and a zero-means-unlimited line figure |
| skip a structured block while measuring lines | check 7's fence walk at `check-memory-hygiene.sh:401-417` | REUSE THE SHAPE — the front-matter skip is a second stateful skip in the same loop, counted the same way |
| bound a rendered line without breaking a token | `textwrap.fill` in the standard library | REUSE — no wrapper, and the two non-default flags carry the whole correctness argument |
| grandfather a file that cannot meet a cap | `memory/project/curation-debt.txt` | REJECTED — §4 records why one authored edit beats the first row in an empty registry |

The claims that check 7's budget is one hardcoded literal in one awk pass, that check 6's caps are
20480 bytes and 250 lines with a wider guides tier, that no index-set member today opens with front
matter, that `parse_front_matter` refuses an indented or colonless front-matter line, and that
`check-arms.py` keys a branch on its `fail` call site and its message signature were verified against
source at writing time. Every measured figure in §4 was RE-measured at rev-2, with check 7's own
predicate rather than a plain line scan, after the audit found the tier justified partly by lines
this unit itself removes.
