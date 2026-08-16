# TOOL-aRuledFrontispiece-5 — the build README joins the hygiene index set at its own cap tier

**Status:** OPEN · rev-1 · 2026-08-16 · node a · Tier-2 · base 96141aed · streams tooling

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

## 3. Non-goals (OUT)

- Replacing the roster with a count. `TOOL-aMouldedFolio-2` S4 renders the FULL roster in the build
  README and only its COUNT in `LIVE.md` and the ledger shards, and `render_region`'s own comment at
  `gen_build_index.py:362-365` says `unit(s)` and `ids` answer different questions and are
  deliberately not reconciled. This unit WRAPS the list. Reversing that decision needs a new id
  naming the record it supersedes, per the build's own append-only rule.
- Relaxing check 7 globally. §4 records the cost.
- Touching the guides tier, the map-dossier exemptions or the run-state exemption.
- Moving `KIT_MEMORY_TREE_VERSION`. Unit 10 moves it once for the whole build.
- Re-rendering the corpus. Unit 10 owns the retrofit; this unit ships the caps, the wrap and the arms.
- Raising 25600 to pre-pay for the regions units 2, 3 and 4 add. That measurement does not exist yet;
  §5 records who takes it.

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

The measurements this design rests on, taken at `base 96141aed` over the 39 tracked build READMEs:

- No README exceeds 25600 bytes. The largest is `memory/builds/cBriefedPilot/README.md` at 24715.
- That same file is 321 lines, so a 250-line cap would red the corpus's biggest entry point on day
  one. It is the reason fork 3 carries no independent line cap, and the byte figure is the real
  budget in any case.
- Five authored lines already sit between 300 and 331 characters, in four builds, and every one of
  them is a markdown table row or a scope bullet that cannot be wrapped without breaking its
  structure. That is what the 350 tier buys, and it is the whole justification for the number.
- Exactly three lines exceed 350. Two are GENERATED — the `ids:` front-matter line at 479 characters
  and the `**Build status:**` line at 577, both in `cBriefedPilot` — and one is authored,
  `aUnmannedHelm/README.md:78` at 419.

### Inventory

Four sites move.

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
already fits, so the wrap is inert for the 36 READMEs whose status line is under the width and
re-renders exactly three: `aSealedCaravan` at 327, `aUnmannedHelm` at 331 and `cBriefedPilot` at 577.
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

One authored line is edited, in `memory/builds/aUnmannedHelm/README.md`. Three READMEs re-render, and
that re-render is unit 10's commit rather than this one's. `memory/HYGIENE.md` rules 6 and 7 and
`tools/memory-tree/HYGIENE.template.md` move together as a byte-paired edit.

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
`tools/memory-tree/gen_build_index.py` and its `--selftest` arms · `memory/HYGIENE.md` and
`tools/memory-tree/HYGIENE.template.md` as a byte-paired edit · one line of
`memory/builds/aUnmannedHelm/README.md`.

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
- risks — the byte headroom is 885 on the largest README, and units 2, 3 and 4 each add a generated
  region to every README that opts in. An order region for 22 units alone plausibly exceeds that, so
  the cap is expected to BIND at unit 10's retrofit. Unit 10 takes that measurement; the resolution
  there is a shorter render or an owner fork on the number, never a silent bump. Separately, this
  unit's wrap re-renders `memory/builds/aSealedCaravan/README.md`, whose sibling `RUN.md` is a copy of
  that README slice compared by check 8 of `tools/unattended/check-unattended.sh`; that run-state file
  is `phase: LANDED`, which is the terminal-phase carve-out fork 7 resolved and unit 8 builds, and
  unit 8 precedes unit 10's retrofit in the total order, so the carve-out is in place before the
  re-render lands. The other run-state file, under `aSiftedPlaybook`, has a 264-character status line
  and does not rewrap.
- testing + left-shift gates — a red arm per new branch in the hygiene test, plus wrap arms in the
  generator's `--selftest`.
- migration / rollback — revert is three source files plus the paired doc edit and one authored line;
  no generated bytes change in this unit's own commit.
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

## 7. Gates

`bash tools/memory-tree/check-memory-hygiene.sh` · `bash tools/memory-tree/check-memory-hygiene.test.sh` ·
`python tools/memory-tree/check-arms.py`, because both reworded messages change their signatures and
`ARMS_FLOORS` pins this engine at `tools/memory-tree/check-memory-hygiene.sh:14:14` ·
`python tools/memory-tree/gen_build_index.py --selftest` ·
`bash tools/memory-tree/kit-dogfood-parity.test.sh` for the paired `HYGIENE.md` edit ·
`bash tools/unattended/check-unattended.sh` for the run-state copy check ·
`bash tools/memory-tree/check-verdict-epoch.sh`, which unit 10 discharges for the whole build.

## 8. Open questions

none — fork 3 resolved membership and both cap figures, and the build README resolved that the roster
is wrapped rather than counted; §4 verifies the mechanisms behind both and §5 hands the one open
measurement, the byte headroom after units 2 through 4 render, to unit 10 rather than reopening a
number the owner set.

## 9. Revision log

- rev-1 · 2026-08-16 · initial draft.

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
matter, that `parse_front_matter` refuses an indented or colonless front-matter line, that
`check-arms.py` keys a branch on its `fail` call site and its message signature, and every measured
figure in §4 were verified against source and against the corpus at writing time.
