# TOOL-aHoistedPass-3 — the build-method budget becomes a number a gate reads

**Status:** SPECCED · rev-1 · 2026-09-04 · node a · Tier-2 · base c4fcf5ad · streams tooling · order 2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-04-build-aHoistedPass-1-design-pass.md](../build/2026-09-04-build-aHoistedPass-1-design-pass.md) | research | TOOL-aHoistedPass-1 TOOL-aHoistedPass-2 TOOL-aHoistedPass-4 TOOL-aHoistedPass-5 TOOL-aHoistedPass-6 TOOL-aHoistedPass-7 TOOL-aHoistedPass-8 TOOL-aHoistedPass-9 DEPL-aHoistedPass-1 |

<!-- /gen:spec-records -->

## 1. Goal

`tools/memory-tree/BUILD-METHOD.template.md:8` declares `**Budget: ≤24 KB, ≤350 lines**` and no checker
reads that figure, so the document's own stated constraint is prose. Raise the byte half to an exact
integer, declare it where the existing size gate already looks, and add the one term that stops the
number drifting between the document and the declaration.

## 2. Scope (IN)

- **S1** — Rewrite the budget line in `tools/memory-tree/BUILD-METHOD.template.md:8` to state the byte
  half as `≤27648 bytes`, and add a fourth dated raise entry beside the three already recorded inline
  at `:10-14`. The line half stays at `≤350 lines`, untouched.
- **S2** — Replace the now-false sentence at `:16-18` ("No gate enforces the pair, which is why
  exceeding it silently was the one option not taken, and whether one is ever added is a SEPARATE
  question nobody has ruled") with one naming the leg and stating what it does not cover.
- **S3** — Re-render `memory/guides/BUILD-METHOD.md` from the template with
  `bash tools/memory-tree/kit-dogfood-parity.test.sh --render`, so S1 and S2 are authored once.
- **S4** — Add one row to `tools/template-size-limits.txt`:
  `memory/guides/BUILD-METHOD.md<TAB>27648`, with the value's arithmetic and its date in the comment
  above it, in the shape the file's own header prescribes.
- **S5** — Add the PAIR TERM to `tools/check-template-size.sh`: one branch at check 6 and exit 6,
  comparing a subject's own `^**Budget:` prose to its declared row. Design §4 carries its placement,
  its two guards and its extractor.
- **S6** — Add exit 6 to the exit-code list in that script's header at `:17-19`, and add exit 4, which
  the list already omits.
- **S7** — Add two arms to `tools/check-template-size.test.sh`: the over-budget arm for this subject
  and the pair-disagreement arm for the new branch, both asserting the message rather than the exit
  code alone, per that file's own rule at `:16`.
- **S8** — Register the leg `build-method size` with the six declarations of §4 `### Inventory`.
- **S9** — Seed the leg's high-water row with
  `bash tools/check-template-size.sh --bump memory/guides/BUILD-METHOD.md`, and commit the resulting
  row in `tools/template-size-highwater.txt`.
- **S10** — Raise `ARMS_FLOORS`'s `tools/check-template-size.sh:6:6` entry in `.memory-tree.conf:203`
  to `7:7`, with the movement argued inline as every other movement in that block is.
- **S11** — Re-stamp the kickoff manifest's `last-audit`, which this diff owes because
  `memory/guides/SESSION-KICKOFF.md:6` lists `tools/check-template-size.sh`, `tools/gate-legs.json`
  and `memory/guides/BUILD-METHOD.md` among its watched pathspecs.

## 3. Non-goals (OUT)

- **The LINE half is not gated.** `check-template-size.sh` measures bytes only (`:99-101`) and this
  unit adds no line axis. `BUILD-METHOD.md:15` argues the byte half binds first at this file's prose
  density, so the choice is priced rather than overlooked. §5 carries it as a residual.
- **No second subject is added.** The leg is per-subject like its three siblings; a future guide
  wanting a byte ceiling writes its own row and its own leg row. Only the PAIR TERM is class-scoped.
- **No new program.** Nothing under `tools/` gains a file. A sibling script would duplicate subject
  resolution, ceiling resolution, CR-normalized measurement and the high-water ratchet.
- **The 17 backticked M6 anchors and the M6 route sentence are NOT written here.** They are
  `TOOL-aHoistedPass-2` at `order 3`. This unit only funds them.
- **The high-water ratchet is not made binding.** It stays advisory and never changes the exit code
  (`check-template-size.sh:114-115`).
- **`memory/map/features/build-method.md:74-78`'s contradicting clause is not corrected here.** It
  claims the line axis binds before the byte axis, against `BUILD-METHOD.md:15`. Follow-up backlog
  row under `TOOL`, because correcting it is a dossier prose edit with its own regen.

## 4. Design

### Data model

The number is written in BYTES, and that is what dissolves the KiB-or-decimal ambiguity rather than
answering it. On a KiB reading the template's 24564 bytes sit 12 under `≤24 KB`; on a decimal reading
they sit 564 over. A checker needs one integer, and the mechanism that will hold it already stores one:
`tools/template-size-limits.txt` declares `<repo-relative-path><TAB><bytes>` and
`tools/check-template-size.sh:91` resolves it as `MAX_BYTES=${2:-${declared:-${MAX_BYTES:-49152}}}`.

**The cap is 27648 bytes.** Arithmetic against the SUBJECT, which is the render:

| term | bytes | where it comes from |
|---|---|---|
| `memory/guides/BUILD-METHOD.md` today | 24553 | measured here, CR-stripped, as the gate measures |
| + the M6 route sentence of `TOOL-aHoistedPass-2` | +742 | CARRIED from the design, which measured 764 in template form and ~22 less after substitution. The sentence is not in the tree, so it cannot be re-derived here |
| + the 17 backticked handle anchors | +289 floor | re-derived here from `DIRECTIVES_CORE` (`tools/unattended/unattended.sh:469`): 17 handles, 255 characters, plus 34 backticks. Realistically 400-700 with joining words |
| + the rewritten budget line and its dated raise entry | ~+300 | estimate |
| + the S2 replacement sentence | ~0 | it replaces `:16-18` rather than adding to it |
| **projected after the build** | **≈26,100** | at 500 bytes of anchors |
| **cap** | **27648** | |
| **headroom** | **≈1,550** | roughly fifteen lines at this file's ~100 B prose line |

27648 is 27 KiB, which matches the KiB-round convention of the three rows already in that file (49152,
18432, 64512). The row is still read as an integer and the prose that pairs with it says `bytes`.

The line half does not move. 317 lines today, plus 8 for the M6 sentence and 2 or 3 for the budget
line, is roughly 328 against the existing `≤350`. The 2026-08-25 raise put that figure where it is and
this unit leaves it there.

### Inventory

**The subject is the RENDER, `memory/guides/BUILD-METHOD.md`.** Four reasons, and the first is the one
that decides it. The budget's own stated reason is the render's re-read cost: `BUILD-METHOD.md:8-9`
says M7 re-reads it WHOLE at every pass boundary and a method too expensive to re-read is skipped
exactly when it is needed. M7 re-reads the render. Second, the render is the file a session in this
repo opens; the template is the shipped source and is read by the renderer. Third,
`kit/dogfood doc parity` renders template to live and diffs, with a guard naming BOTH
`memory/guides/BUILD-METHOD.md` and `tools/memory-tree/`, so template growth cannot land without
reaching the render in the same bar. Fourth, the render is the file hygiene check 6 already caps, so
the tight per-subject ceiling and the loose class ceiling name the same file rather than two.

**Three legs already ride `tools/check-template-size.sh`**, derived here from `tools/gate-legs.json`:

| leg | positional subject | chunk · subject · ceiling |
|---|---|---|
| `template size <=48KiB` | none, so the default at `:49` | `product` · `repo` · 300 |
| `charter size` | `AGENTS.md` | `product` · `repo` · 300 |
| `kickoff engine size <=18KiB` | `skills/session-kickoff/SKILL.md` | `product` · `repo` · 300 |

`build-method size` is the fourth. A fifth leg, `template size gate selftest`, rides the sibling
`tools/check-template-size.test.sh` at chunk `selftests`, subject `kit`, which no boundary runs.

**Six declarations, and the second is not what it looks like.**

1. `tools/gate-legs.json` — one row:
   `{"name": "build-method size", "argv": ["bash", "tools/check-template-size.sh",
   "memory/guides/BUILD-METHOD.md"], "chunk": "product", "subject": "repo", "ceiling": 300}`. All four
   fields copy the three siblings. `subject` is not optional: `tools/govkit/govkit.py:1592-1596` reds
   on an exempt leg whose manifest row declares none, and `:1597-1600` reds on one outside `kit|repo`.
2. `tools/govkit/registry.toml` — an `[[exempt_leg]]` row, NOT a `[[gate_leg]]` in a kit.toml. Read
   here: all three existing size legs are carried that way, at `:277-279`, `:281-283` and `:356-359`,
   and the gate script itself is a path exemption at `:176-178`. The kickoff row records the precedent
   in its own words, that the kickoff-manifest descriptor once declared its size leg as a `gate_leg`
   so `apply` emitted an adopter a row running an engine gov never ships, withdrawn as
   `DEPL-dCarriedReceipt-6`. Declaring `build-method size` in `tools/memory-tree/kit.toml` would repeat
   that exactly: the memory-tree kit ships `BUILD-METHOD.template.md` and ships no size gate. The
   reason string names that asymmetry. `govkit.py:1580-1583` also reds a leg that is exempted AND
   claimed by an entry, so this row and item 4 must not both be entry claims — they are not, because
   item 4 is a different registry.
3. `tools/govkit/subject-pins.tsv` — one row in the shape of `:94`, written by
   `python tools/govkit/govkit.py selfcheck --write`.
4. `memory/map/features/build-method.md:11` — the leg NAME appended to that dossier's `gate-legs`
   claim, which today reads `["method carriers (every pointer declared)", "method-carriers
   self-test"]`. The convention is that the SUBJECT's dossier claims a size leg, evidenced twice:
   `memory/map/features/session-kickoff.md:11` claims `kickoff engine size <=18KiB`, and
   `memory/map/features/playbook.md:11` claims `charter size`. Without a claim, either
   `tools/govkit/govkit.py:1602-1604` or `codebase-map coverage + freshness` reds the new key.
5. Regenerated map artifacts, `python tools/codebase-map/gen_map.py --write`, in the same commit.
6. The high-water row (S9). `memory/map/features/playbook.md:107-111` names this as the third step of
   the seam's own extension recipe, and without it the leg prints
   `TEMPLATE-SIZE no-ratchet — memory/guides/BUILD-METHOD.md has no row … growth is unpriced` on every
   bar at exit 0.

Plus, outside the six: the row in `tools/template-size-limits.txt`, which is the cap itself.

**The leg is named `build-method size`, with no number in it.** The demonstrated reason is that
`template size <=32KiB` had to be renamed in place to `template size <=48KiB` when the ceiling moved
(`memory/map/baseline.toml:6-11`). A numberless name cannot go stale against its own ceiling. The
shrink-only argument that name change is recorded under does NOT apply here and is not claimed:
`baseline.toml:10-11` retracts it in the file's own words, "Nothing enforces the rule today", and in
any case baseline governs UNCLAIMED keys while this one is claimed by item 4.

### Migration

**The PAIR TERM is the only new code.** With the cap in the declaration and the number also in the
document's prose there are two spellings of one fact, which is the class the charter names: a value
stated in prose beside the source that owns it rots between changes. The branch:

```sh
# Placed after `name=` (:102) and BEFORE the over-budget branch (:104). A disagreement makes the
# over-budget verdict ambiguous — you cannot tell which ceiling you failed — so it is reported first.
bline=$(tr -d '\r' < "$FILE" | grep -m1 '^\*\*Budget:')
if [ -n "$declared" ] && [ -n "$bline" ]; then
  prose=$(printf '%s' "$bline" | sed -n 's/^\*\*Budget:[^0-9]*\([0-9][0-9]*\) bytes.*/\1/p')
  if [ "$prose" != "$declared" ]; then
    FAIL_CODE=6
    fail 6 "the subject states its own budget and disagrees with its declaration: $name says
  '${prose:-no bytes figure}', $LIMITS says $declared. Two spellings of one fact; change both or
  neither. A budget line this gate cannot parse as bytes reads the same as a wrong one, deliberately."
  fi
fi
```

**TWO guards, not one.** `[ -n "$declared" ]` keeps an undeclared subject from being compared against
the script's hard default. `[ -n "$bline" ]` keeps the three existing subjects out: each has a declared
row and, verified here with `git grep -nE '^\*\*Budget:'`, zero budget lines. Only two tracked files
carry one, and they are the two halves of this one byte-compared pair.

**An unparseable budget line reds through the same branch.** `${prose:-…}` is empty when the line says
`≤27 KB` rather than bytes, and an empty string is not equal to a declared row, so a prose rewrite back
to a KB spelling reds instead of silently disarming the term. That is the whole point of the term: a
file must not be able to move its prose and pass. One branch covers both cases, which also means one
arm satisfies `check-arms.py`.

**Check 6 and exit 6 are both free**, re-derived here: the file's `fail` numbers are 1, 2, 3, 4 and 5
across six branches (`:76`, `:98`, `:107`, `:137`, `:168`, `:181`) and its `FAIL_CODE` values are 1
through 5. The extractor is `sed`, single-pass, and matches `≤` as literal bytes rather than through a
character class, so no locale is pinned. CR is stripped on the read, as `:99-101` does.

### Rollout

The commit order inside the unit is: template edit, render, declaration row, leg row and the other five
declarations, then the gate code and its arms. The three staged breaks of §6 are observed in a scratch
clone before the leg row lands, per charter §7. `TOOL-aHoistedPass-2` at `order 3` then spends the
headroom this unit creates, and re-bumps the high-water row when its anchors land, because that growth
is intended and argued.

### Files touched (estimate)

`tools/memory-tree/BUILD-METHOD.template.md` · `memory/guides/BUILD-METHOD.md` (rendered) ·
`tools/template-size-limits.txt` · `tools/template-size-highwater.txt` · `tools/check-template-size.sh`
· `tools/check-template-size.test.sh` · `tools/gate-legs.json` · `tools/govkit/registry.toml` ·
`tools/govkit/subject-pins.tsv` (generated) · `memory/map/features/build-method.md` ·
`memory/map/generated/` (generated) · `.memory-tree.conf` · the kickoff manifest.

### Alternatives rejected

- **Subject = the TEMPLATE.** It gives a faster red, because the authored edit is measured directly
  rather than one render later. Rejected because the number prices the render's re-read cost, and
  because the template-minus-render delta is not a constant that can be reasoned about: the template
  carries four `{{KIT_DIR}}` (11 bytes becoming 17, +6 each) and five `{{TOOL_ROOT}}` (13 becoming 6,
  −7 each), a net −11 that is exactly the measured 24564 − 24553 and that a different install prefix
  flips. The one-commit lag is disclosed rather than argued away, and it is not silent: a template edit
  without a render reds `kit/dogfood doc parity`, whose guard names `tools/memory-tree/`.
- **Both files as two legs.** Two rows measuring one text, and the pair term would then need a second
  declared row that parity forces to equal the first. Rejected as the two-spellings class.
- **A new sibling script.** Rejected by the seam at `memory/map/features/playbook.md:107-111`, which
  exists for this and says so.
- **Making the high-water ratchet binding for this subject.** Rejected: `playbook.md:63-68` records
  that no fixed threshold works, and this unit is not the place to re-open it.

## 5. Production-readiness checklist

- **security** — N/A. No new input, no write path, no network, no credential. The gate reads two
  tracked files and exits.
- **perf / scale** — one extra `tr`, `grep` and `sed` per invocation, on files under 30 KB. The leg's
  declared ceiling is 300 seconds, copied from three siblings that measure comparable files.
- **a11y** — N/A. A shell gate with no user surface.
- **i18n** — N/A, with one note: the extractor matches `≤` as literal UTF-8 bytes and pins no locale,
  which is the same discipline `check-memory-hygiene.sh` applies to `length()`.
- **error / empty / loading states** — an absent budget line, an absent declaration row and an absent
  high-water row each have a defined behaviour, and the first two are the term's two guards.
- **observability** — the pass line already names measured bytes, the ceiling and the percentage
  (`:186`); the high-water row (S9) is what makes growth visible between raises.
- **risks** — the term is one comparison over two tracked values with no shared mutable state, so
  concurrency and data-loss do not arise. The rollback is deleting the leg row and the declaration row,
  which returns the subject to the hard default. `ARMS_FLOORS` must move back with it.
- **testing + left-shift gates** — the three staged breaks of §6, plus S7's two permanent arms on
  `tools/check-template-size.test.sh`.
- **migration / rollback** — none. Nothing reads the old prose figure, verified in §10, so nothing
  breaks when it changes shape.
- **user docs** — none. `memory/map/features/build-method.md` and `memory/map/features/playbook.md` are
  the in-repo records, and item 4 updates the first.

Two residuals go to the owner rather than being solved here. **The line axis stays ungated** and a
document that grew in lines without growing in bytes passes. **A later raise of the byte cap is caught
by nothing:** `tools/drift-audit/drift_signals.py:279-290` parses `KEY = value` scalars and
`tools/template-size-limits.txt` is a TSV, so no ratchet row is owed there and none would fit. A raise
is argued in that file's own comment, exactly as the playbook's 49152 is, and nothing grades whether
the argument is good.

## 6. Acceptance criteria

- **AC1** — When `bash tools/check-template-size.sh memory/guides/BUILD-METHOD.md` runs on the
  untouched post-raise tree, it exits 0 and prints one `template-size OK` line naming the measured
  bytes against `27648`. This is the third staged observation: an untouched file passes.
- **AC2** — When filler is appended to a scratch copy of `memory/guides/BUILD-METHOD.md` until it
  exceeds 27648 bytes and the gate is run against it, it exits `1` with the message
  `the file is over its size budget`, naming the file, the measured bytes and the overage. Staged,
  confirmed RED, unstaged before the leg row lands.
- **AC3** — When the `**Budget: ≤27648 bytes` figure in a scratch copy is changed without changing its
  row in the limits file, `bash tools/check-template-size.sh <copy> "" "" <scratch-limits>` exits `6`
  and the message names BOTH numbers. When the row is changed instead and the prose is not, the same
  branch reds the same way.
- **AC4** — When the budget line in a scratch copy is rewritten to a KB spelling, the same branch exits
  `6` with `no bytes figure` in the message, so a prose rewrite cannot disarm the term.
- **AC5** — When `bash tools/check-template-size.sh AGENTS.md` and
  `bash tools/check-template-size.sh skills/session-kickoff/SKILL.md` run after the change, both exit 0
  and neither emits a `check 6` line, because each has a declared row and no `^**Budget:` line.
- **AC6** — When `bash tools/check-template-size.test.sh` runs, it exits 0 with the two new arms
  present, each asserting the specific message rather than the exit code alone.
- **AC7** — When `python3 tools/memory-tree/check-arms.py --check` runs, it exits 0 with the new
  `fail 6` branch ARMED rather than pinned, and `python3 tools/memory-tree/check-arms.py --report`
  shows `tools/check-template-size.sh` at 7 branches and 7 armed against the raised floor.
- **AC8** — When `python tools/govkit/govkit.py selfcheck` runs, it exits 0 and its own note line
  reports one more leg in the manifest and one more exempt than at `c4fcf5ad`, which is what proves the
  `[[exempt_leg]]` row exists (`govkit.py:1602-1604`) and carries a `subject` (`:1592-1600`).
- **AC9** — When `python3 tools/codebase-map/test_codebase_map.py` runs, it exits 0, which is what
  proves `build-method size` is claimed in a dossier and the generated artifacts were regenerated in
  the same commit.
- **AC10** — When `bash tools/memory-tree/kit-dogfood-parity.test.sh` runs, it exits 0, so the budget
  line and the raise entry are byte-identical across the template and the render modulo substitution.
- **AC11** — When `bash skills/session-kickoff/manifest-check.sh` runs, it exits 0 with `last-audit`
  re-stamped, because `memory/guides/SESSION-KICKOFF.md:6` watches three paths this diff moves.
- **AC12** — When `bash tools/run-gates/run-gates.sh` runs after the landing, the reported leg set
  contains `build-method size` and the run is green.

## 7. Gates

New leg: **`build-method size`** — `bash tools/check-template-size.sh memory/guides/BUILD-METHOD.md`,
chunk `product`, subject `repo`, ceiling 300, no guard, so it runs on every bar exactly as its three
siblings do.

Legs that must stay green, each named because this diff reaches it:

- **`kit/dogfood doc parity`** — guarded on `memory/guides/BUILD-METHOD.md` and `tools/memory-tree/`,
  both of which this diff touches, so it runs on this unit's bar.
- **`govkit selfcheck`** — chunk `declarations`, subject `repo`, no guard. It reds until declarations
  1 and 2 both exist.
- **`codebase-map coverage + freshness`** — chunk `declarations`, subject `repo`, no guard. It reds
  until declaration 4 lands and 5 is regenerated.
- **`harness arms (fail branches armed or pinned)`** — chunk `declarations`, subject `repo`, no guard.
  It reds on the new `fail 6` branch until S7's arm exists. This obligation exists because
  `tools/check-template-size.sh` defines `fail() {` at `:29` and has a sibling `.test.sh`, which is
  `check-arms.py`'s discovered population (`:9-12`).
- **`kickoff-manifest ratchet`** — chunk `records`, subject `repo`. S11 is what keeps it green.
- **`memory hygiene`** — chunk `records`, subject `repo`. It grades this spec file under check 12.

**Named and NOT claimed as a catcher.** `harness arms` does not force S10. `ARMS_FLOORS` is one-sided
upward (`check-arms.py:207` and its comparison at `:283-291` red only when the measured count is BELOW
the floor), so 7 branches and 7 arms against a floor of `6:6` passes and nothing says the floor went
stale. The run holds S10. Likewise `kit version markers` grades presence and marker-to-constant
agreement only and reads no diff, and `check-verdict-epoch.sh`'s scan set is the hygiene engine plus
six Python delegates (`:68-72`) and contains no `*.template.md`, so no leg has an opinion about the
version question in §8.

## 8. Open questions

- **F1 — does this unit bump the memory-tree kit version from 2.59?** The unit changes the BODY of a
  template the kit ships to adopters. `tools/check-kit-versions.sh:143-146` requires every tracked
  `tools/memory-tree/*.template.md` to carry a `gov:kit memory-tree@<V>` marker agreeing with
  `KIT_MEMORY_TREE_VERSION`, and it reads no diff, so it is green either way.
  `tools/memory-tree/check-verdict-epoch.sh` states at `:2` that the version dates the ENGINE's
  verdicts, and its scan set (`:68-72`) excludes templates, so it does not demand one and would not
  object to one. **Recommendation: BUMP to 2.60**, because the marker's stated job
  (`check-kit-versions.sh:144`) is to let an adopter tell which text they hold, and two different
  budget lines shipping under one version defeats exactly that. The cost is the constant plus the
  marker on every memory-tree template plus the rendered halves, in this commit, and
  `bash tools/check-kit-versions.sh` derives the full carrier set rather than this spec typing a count
  beside it. The alternative — no bump, on the ground that no engine verdict moved — is defensible and
  cheaper, and it is the owner's call because `TOOL-aHoistedPass-2` edits the same template at
  `order 3` and would face the same question one commit later.

## 9. Revision log

- rev-1 · 2026-09-04 · initial draft, written against `origin/main` at `c4fcf5ad` in a worktree at that
  tip. Design §5B is the source; every line number in it was re-opened here and the corrections below
  are folded in silently above rather than left for a reader to discover.
  - **The render is NOT ungated on bytes today, and the design's framing implies it is.**
    `memory/guides/BUILD-METHOD.md` already rides hygiene check 6 under `GUIDE_CAP_BYTES=61440` and
    `GUIDE_CAP_LINES=750` (`tools/memory-tree/check-memory-hygiene.sh:63`, kit defaults; this repo
    declares neither in `.memory-tree.conf`). What no checker reads is the file's OWN figure. The new
    leg is a tightening from 61440 to 27648, not a first gate, and §4 says so.
  - **The declaration act is SIX items, not five.** `memory/map/features/playbook.md:107-111` records
    the seam's own extension recipe and its third step is a `--bump` to seed the high-water row. The
    design's five omit it, and without it the leg prints a `no-ratchet` line on every bar.
  - **The design does not name `harness arms (fail branches armed or pinned)` for this unit.**
    `tools/check-template-size.sh` is in `check-arms.py`'s discovered population, recorded at
    `memory/map/features/playbook.md:86`, so a new `fail` branch reds that leg until armed. S7 and AC7
    exist for it. `.memory-tree.conf:203` also carries `tools/check-template-size.sh:6:6`, which S10
    moves — and §7 states plainly that nothing forces S10, because the floors are one-sided upward.
  - **The design does not name the kickoff manifest.** `memory/guides/SESSION-KICKOFF.md:6` watches
    `tools/check-template-size.sh`, `tools/gate-legs.json` and `memory/guides/BUILD-METHOD.md`. S11 and
    AC11 exist for it.
  - **The numberless-leg-name argument had the wrong basis.** The design rests it on
    `memory/map/baseline.toml`'s shrink-only rule. That rule governs UNCLAIMED keys, and this leg is
    claimed by declaration 4, so a future rename would edit a dossier and regenerate rather than touch
    baseline. §4 keeps the name for the demonstrated reason instead, and does not restate the retracted
    enforcement claim at `baseline.toml:10-11`.
  - **The pair term needs TWO guards.** The design names `[ -n "$declared" ]` only. Verified here:
    `coding-governance-agents.template.md`, `AGENTS.md` and `skills/session-kickoff/SKILL.md` each
    carry a declared row and zero `^**Budget:` lines, so a single guard would compare all three against
    an empty prose value. AC5 observes the second guard.
  - **The unparseable-budget case was not in the design.** A rewrite from bytes back to `≤27 KB` makes
    the extractor return nothing, which would silently disarm the term. It reds through the same branch
    and AC4 observes it.
  - **`+764` for the M6 route sentence is CARRIED, not re-derived.** That sentence does not exist at
    `c4fcf5ad`, so it cannot be measured here, and §4's table says so in the row. The 289-byte anchor
    floor WAS re-derived: 17 handles from `tools/unattended/unattended.sh:469`, 255 characters, plus 34
    backticks, and 0 of the 17 appear in the render.
  - **Reproduced without change:** the three legs riding the script and their subjects; all three being
    `[[exempt_leg]]` rows at `registry.toml:277-279`, `:281-283` and `:356-359`; check 6 and exit 6
    both free; the two-file `^**Budget:` population; `subject-pins.tsv`'s `:94` row shape; and
    `memory/map/features/build-method.md:11`'s current two-element claim.
  - **Also observed, not in the design:** the script's own exit-code list at `:17-19` omits exit 4, so
    S6 adds two lines rather than one. And the template-minus-render delta is not sign-stable — four
    `{{KIT_DIR}}` grow and five `{{TOOL_ROOT}}` shrink, netting the measured −11 — which is why §4's
    rejected alternative does not rest on the template being the larger half.

## 10. Reuse audit

The probe ran: `python tools/codebase-map/reuse_lookup.py "gate a document's declared byte budget
against its size ceiling declaration"`, over a corpus of 645 symbols, 188 inventory keys, 19 affordance
seams and 20 dossiers. It returned `check-template-size.sh [playbook] (name stem: siz; via
affordance-seam)` among its ranked candidates, alongside the three existing size legs as inventory
keys. **The seam is `tools/check-template-size.sh` subject resolution, declared at
`memory/map/features/playbook.md:107-111`**, whose own words are that it exists for "gating ANY file's
byte size on the merge bar without writing a sibling script", extended by one `tools/gate-legs.json`
entry naming the subject, one row in `tools/template-size-limits.txt` giving its ceiling and the reason
for it, and one `--bump` to seed its high-water row. This unit is that extension verbatim, which is why
§3 forbids a new program and why S9 exists. The second seam at `:112-115`, the high-water record, is
also used and its stated caveat is honoured: a new consumer needs an arm comparing its key to a
literal, which is what S7's arms do through the gate's own message.

Recall terms used: template-size-limits declaration, per-subject ceiling, gate-legs subject, exempt_leg
registry, high-water ratchet, kit/dogfood doc parity, GUIDE_CAP_BYTES, ARMS_FLOORS, check-arms armed
branch, baseline shrink-only, map dossier gate-legs claim, budget prose pair drift.
