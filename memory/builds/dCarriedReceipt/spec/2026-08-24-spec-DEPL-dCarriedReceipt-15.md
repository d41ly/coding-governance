# DEPL-dCarriedReceipt-15 — gov stops shipping its own prefix inside kit bodies

**Status:** CLOSED · rev-5 · 2026-08-26 · node d · Tier-2 · base 9ddcc5c9 · streams deployer · ratified 2026-08-24

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-26-build-DEPL-dCarriedReceipt-15-acceptance-ledger.md](../build/2026-08-26-build-DEPL-dCarriedReceipt-15-acceptance-ledger.md) | journal | — |
| [2026-08-24-review-DEPL-dCarriedReceipt-9-spec-precode.md](../reviews/2026-08-24-review-DEPL-dCarriedReceipt-9-spec-precode.md) | spec-audit | DEPL-dCarriedReceipt-9 DEPL-dCarriedReceipt-10 DEPL-dCarriedReceipt-11 DEPL-dCarriedReceipt-12 DEPL-dCarriedReceipt-13 DEPL-dCarriedReceipt-14 |
| [2026-08-25-review-DEPL-dCarriedReceipt-9-round4.md](../reviews/2026-08-25-review-DEPL-dCarriedReceipt-9-round4.md) | spec-audit | DEPL-dCarriedReceipt-9 DEPL-dCarriedReceipt-10 DEPL-dCarriedReceipt-11 DEPL-dCarriedReceipt-12 DEPL-dCarriedReceipt-13 DEPL-dCarriedReceipt-14 |
| [2026-08-25-review-DEPL-dCarriedReceipt-9-round5.md](../reviews/2026-08-25-review-DEPL-dCarriedReceipt-9-round5.md) | spec-audit | DEPL-dCarriedReceipt-9 DEPL-dCarriedReceipt-10 DEPL-dCarriedReceipt-11 DEPL-dCarriedReceipt-12 DEPL-dCarriedReceipt-13 DEPL-dCarriedReceipt-14 |
| [2026-08-25-review-DEPL-dCarriedReceipt-9-round6.md](../reviews/2026-08-25-review-DEPL-dCarriedReceipt-9-round6.md) | spec-audit | DEPL-dCarriedReceipt-9 DEPL-dCarriedReceipt-10 DEPL-dCarriedReceipt-11 DEPL-dCarriedReceipt-12 DEPL-dCarriedReceipt-13 DEPL-dCarriedReceipt-14 |
| [2026-08-26-review-DEPL-dCarriedReceipt-13-diff-review-round1.md](../reviews/2026-08-26-review-DEPL-dCarriedReceipt-13-diff-review-round1.md) | diff-review | DEPL-dCarriedReceipt-4 DEPL-dCarriedReceipt-5 DEPL-dCarriedReceipt-6 DEPL-dCarriedReceipt-13 |
| [2026-08-26-review-DEPL-dCarriedReceipt-4-diff-review-round1.md](../reviews/2026-08-26-review-DEPL-dCarriedReceipt-4-diff-review-round1.md) | diff-review | DEPL-dCarriedReceipt-4 DEPL-dCarriedReceipt-5 DEPL-dCarriedReceipt-6 DEPL-dCarriedReceipt-13 |
| [2026-08-26-review-DEPL-dCarriedReceipt-5-diff-review-round2.md](../reviews/2026-08-26-review-DEPL-dCarriedReceipt-5-diff-review-round2.md) | diff-review | DEPL-dCarriedReceipt-4 DEPL-dCarriedReceipt-5 DEPL-dCarriedReceipt-6 DEPL-dCarriedReceipt-13 |

<!-- /gen:spec-records -->

## 1. Goal

`apply` writes gov's bytes verbatim — `blob_at` at `:2453`, `write_bytes` at `:2469`, with no
substitution between them. `resolve_tokens` (`:516`) reaches destinations, gate-leg argv and guards,
hole discharge commands, adopt and check argv, and `lf_pin` patterns (`:1820`), and it reaches no
file body anywhere. So every literal `tools/<kit>/…` path a kit body spells arrives unchanged in a
target installed at another prefix. The debt is large, and this spec deliberately does not size it
in prose: rev-1's 93 files across 534 lines reproduced under none of the six populations a review
re-measured at `9ddcc5c9`, and neither did the backlog row's 59 files. §4 publishes the exact
predicate instead, and `tools/install-prefix-carried.txt` publishes the count. What the debt
manufactured is not in doubt: inCMS's `scripts/lexicon/lexicon.py` carries seven `tools/`-prefixed
literals right now — four resolvable paths that resolve to nothing in its tree, and three prose
citations quoting `tools/codebase-map/` as the subject of an explanation. Hand-editing the four is
the only remedy an adopter has ever had, and every sync re-manufactures the same edit. `-9`'s needle
map papers over the symptom row by row; this unit removes the bytes that produce it.

## 2. Scope (IN)

- **S1** — `tools/check-install-prefix.sh` gains a second arm over a second population: the
  SHIPPING prefix (`tools/<kit>/<file>`) inside the set `resolve_entry` declares shippable, rather
  than the root spelling the existing arm owns over a glob-derived surface. The existing arm and its
  line-granular waivers are untouched.
- **S2** — the new arm's population is derived, never listed, with exactly ONE named addition. It
  walks the registry through `read_descriptors` and `resolve_entry`, so a new kit and a new shipped
  file both enrol the day they land, exactly as the kit-name alternation at `:38` already does. The
  addition is `WIRE-INTO-PROJECT.md`: measured at `9ddcc5c9`, `resolve_entry` resolves it for no
  kit — no descriptor claims it, and its only appearance inside one is a comment in
  `tools/memory-recall/kit.toml` — so a derived-only population would grade it nowhere, while the
  existing arm already carries it for the reason its own comment gives at `:43-45`, that it
  PRESCRIBES the install paths. One member, one reason, declared where a reader can audit it.
- **S3** — the new arm is INERT where the repo is not a kit source, detected by the absence of
  `tools/govkit/registry.toml`, and it says so in one line rather than passing silently. This kit is
  deployed to NicoCares, which installs at `scripts/`; an arm keying on the LOCAL prefix would red
  every usage header in every kit NC received.
- **S4** — a shrink-only ratchet at `tools/install-prefix-carried.txt`, one `<path><TAB><count>` row
  per carrying file, written by `bash tools/check-install-prefix.sh --write-ratchet`. The count may
  fall and never rise, and a row falling to zero must be deleted. Per FILE rather than per line,
  because the existing `<path>:<line>` waiver shape goes stale on every edit above a waived line,
  and one row per hit line would rot within a week. **One function emits both the file and
  `--list`'s `carried-prefix` section**, over the §4 predicate, so the artifact and the report
  cannot disagree — and no number typed into this document restates either. That is what AC1
  asserts.
- **S5** — the executable population fixes itself by DERIVING its own path rather than spelling one.
  `tools/lexicon/lexicon.py` is the demonstration: its runtime usage line (`:559`) computes the path
  from `__file__` against the repo root, and its docstring usage block (`:5-7`) moves into that one
  runtime printer, so the literal has exactly one home and that home is derived. That is four of the
  file's seven literals. The other three, at `:245`, `:246` and `:265`, are NOT touched: they quote
  `tools/codebase-map/` inside backticks as the literal subject of a measured glob bug, and
  rewriting them destroys the explanation they exist to carry.
- **S6** — `render_doc` gets ONE canonical copy under the `resolve_python` pattern this repo already
  runs: the canonical body in `tools/lib/`, a `>>> render_doc — canonical copy:` marker in every
  inlined copy, and the parity population derived by grepping that marker. It retires the second
  spelling at `tools/memory-tree/kit-dogfood-parity.test.sh:58-72`, whose own comment already names
  itself as the drift class.

## 3. Non-goals (OUT)

- **Not** converting every carried line. S5 converts the lexicon kit's four executable literals and
  the ratchet holds the rest, whatever the predicate counts; a unit that rewrites every shipped body
  is a unit nobody can review.
- **Not** rendering placeholders at the write seam. The eager version of this unit teaches `apply`
  to substitute into file bodies, and it must not: the receipt's `sha256` at `:2458` is computed
  from the bytes about to be written, so a rendered body recorded against a single identity reads
  `differs` forever afterwards. Two identities belong to `-7` and the `relocate` rung to `-9`. This
  unit adds no substitution to any write path, which is what keeps it landable alone.
- **Not** touching `-9`'s needle map, `carry`, or any rung name.
- **Not** a reverse transform, an upstream verb, or a free-form rewrite rule. Build-wide cut line.
- **Not** widening the EXISTING arm's population or relaxing any of its twelve waivers.
- **Land-alone:** this unit leaves gov green on its own and changes nothing in either adopter tree
  beyond the lexicon kit's own bytes. It has no landing partner. Its only ordering constraint is the
  negative one above — the write-seam render is not in it, so `-7` is not a prerequisite.

## 4. Design

### Inventory

**The predicate is the claim and the artifact is the count.** rev-1 published 93 files across 534
lines; a review re-measured six candidate populations at `9ddcc5c9` — 97/656, 86/594, 109/752 and
three test-excluded variants — and none of them is that pair, nor the backlog row's 59 files. The
failure is not arithmetic. "Shippable" has several defensible spellings, and a prose sentence and a
shell script are free to spell it differently forever. So this unit publishes the predicate here,
exactly as `--write-ratchet` implements it, and asserts the numbers nowhere but in the file it
writes:

```
population  every distinct SOURCE path `resolve_entry` (:270) resolves across the descriptors
            `read_descriptors` (:3281) returns, deduplicated by source path -- the same pair
            `planned_writes` (:1359) walks -- PLUS the one named addition S2 declares,
            `WIRE-INTO-PROJECT.md`, which that pair resolves for no kit. NO test or selftest
            exclusion: a shipped test IS received, which is exactly where this population and
            the existing arm's part company.
kit names   the alternation check-install-prefix.sh:38 already derives from
            `git ls-files -- 'tools/*/*'`, never a list typed anywhere.
hit         a LINE matching (^|[^/{}[:alnum:]._-])tools/(<alt>)/[A-Za-z0-9_.-]+\.(sh|py|js|md|json|toml)
            -- the existing arm's regex with the shipping prefix bound. `{` and `}` stay in the
            excluded lead class for the reason :52-55 already gives: the corrected placeholder
            form must not be a hit.
count       hit LINES per source path. A line carrying two literals counts once.
row         `<path><TAB><count>`, emitted only where count > 0, sorted by path.
```

`tools/gate-legs.json` carries a heavy load of these literals and reaches no target through
`resolve_entry`, which is precisely why the new arm's population is the shippable set rather than
the existing arm's `tools/*` glob. Two neighbouring claims did not survive re-measurement at
`9ddcc5c9` and are corrected here rather than left standing. `tools/check-kit-versions.sh` is INSIDE
the population, not outside it: `resolve_entry` resolves it as its own registry entry's engine, so
it is graded like any other shipped source. And `WIRE-INTO-PROJECT.md` is not resolve_entry-resolved
by any descriptor, so it reaches the population only through S2's single named addition — which is
what that addition is for. Without it, F2's ratchet answer would be false and this file's 27 hit
lines, re-verified under the predicate above at `9ddcc5c9`, would be graded by neither arm. F2 still
rules it ratcheted rather than converted.

### Data model

`tools/install-prefix-carried.txt` is tracked, comment-tolerant, `<path><TAB><count>`. It is a FLOOR
file in the same sense inCMS's `.governance/row-count.txt` is: the number may fall, never rise. A
file absent from it may carry zero hits and no more.

### Alternatives rejected

- *Make the existing regex prefix-parametric in place.* The two questions have different populations
  and different remedies. The root spelling is a mistake with twelve deliberate exceptions; the
  shipping prefix is standing debt across most of the shipped surface, sized by the ratchet and by
  no number typed in this document. Folding them into one predicate means one waiver file where a
  real root-spelling regression hides among the debt rows.
- *Placeholders in executable bodies, rendered at install.* `check-install-prefix.sh:52-54` already
  blesses `{{TOOL_ROOT}}` and the shipped `*.template.md` set already uses it, so the mechanism is
  real — but it needs a render step, and gov RUNS its own executables from its own tree. A
  `{{TOOL_ROOT}}` in `lexicon.py`'s usage printer is wrong in gov and wrong in every adopter until
  something substitutes it. Runtime derivation is correct in both with no step at all, and the
  existing gate's own rationale at `:8` already says every engine derives its own prefix.
- *Keep `render_doc` duplicated.* Two spellings of one substitution is what
  `kit-dogfood-parity.test.sh:55` names in its own comment, and
  `tools/unattended/cross-component.test.sh:53-56` is already a further spelling using `sed` with a
  `|` delimiter, the exact hazard `render_doc`'s comment at `:65-67` warns against.

### Files touched (estimate)

`tools/check-install-prefix.sh` (~60 lines), `tools/install-prefix-carried.txt` (new, one row per
carrying file),
`tools/check-install-prefix.test.sh` (4 arms), `tools/lexicon/lexicon.py` (~12 lines),
`tools/lib/render-doc.sh` (new, ~15 lines), plus marker enrolment in
`tools/memory-tree/adopt-memory-tree.sh` and `tools/memory-tree/kit-dogfood-parity.test.sh`.

## 5. Production-readiness checklist

- security — N/A: the arm reads tracked bytes and writes nothing, and no path in it reaches a target.
- perf / scale — one registry walk plus one read of 168 blobs, on a leg that already reads 162 files.
  Same order of magnitude as the arm beside it.
- a11y — N/A: CLI.
- i18n — N/A.
- error / empty / loading states — a repo with no `tools/govkit/registry.toml` prints the announced
  skip and exits 0. An empty shippable set is a failure and not a pass, matching the existing arm's
  two empty-population guards at `:39` and `:50`.
- observability — `--list` gains a `carried-prefix` section printing per-file counts against their
  floors, so the debt is readable rather than inferred from an exit code.
- risks — the material risk is redding an adopter's bar with a gate they receive. S3 is the answer
  and AC3 is its proof. The residual risk is a per-file count hiding a swap, one literal removed and
  another added in the same file. Accepted, and named, because per-line granularity was measured to
  rot faster than it guards.
- testing + left-shift gates — four arms in `tools/check-install-prefix.test.sh`, each observed RED
  before the fix. The left-shift is S1 itself: the class becomes a standing predicate over a derived
  population, so a new kit shipping a literal prefix reds on its landing commit.
- migration / rollback — the ratchet file is new and additive, and deleting it with the arm restores
  `9ddcc5c9` behaviour exactly. `lexicon.py`'s change is a pure move of one string into a printer.
- user docs — `WIRE-INTO-PROJECT.md` gains one line under the install step saying a kit body never
  spells the install prefix, and how the ratchet is read. Its own literal paths are prescriptive
  install instructions and stay, entered in the ratchet at whatever count the predicate gives them.

## 6. Acceptance criteria

- **AC1** — `bash tools/check-install-prefix.sh --list` prints a `carried-prefix` section whose rows
  are byte-identical to `tools/install-prefix-carried.txt` as written by
  `bash tools/check-install-prefix.sh --write-ratchet`, because one function emits both over the §4
  predicate. The section is non-empty, and its row count and column sum ARE this unit's inventory
  claim — nothing in this spec restates them. Observe RED first: at `9ddcc5c9` the command prints no
  such section and exits 0, so every carried line is unmeasured.
- **AC2** — Adding one literal `tools/lexicon/lexicon.py` to a shippable file that
  `tools/install-prefix-carried.txt` records at its current count makes
  `bash tools/check-install-prefix.sh` exit 1 and name that file. Removing a hit and lowering the row
  keeps it at 0. Staged, observed red, unstaged.
- **AC3** — Run against a fixture with no `tools/govkit/registry.toml`, the same command prints one
  line naming the skipped arm and its reason, and exits 0. A NicoCares-shaped fixture at
  `prefix = "scripts"` carrying `scripts/lexicon/lexicon.py` in a usage header is NOT a hit.
- **AC4** — `python tools/lexicon/lexicon.py --nosuchmode` prints a usage line reading
  `tools/lexicon/lexicon.py`, and the same file copied to `scripts/lexicon/lexicon.py` in a scratch
  repo prints `scripts/lexicon/lexicon.py`. Observe RED first: at `9ddcc5c9` both print
  `tools/lexicon/lexicon.py`, which is four of inCMS's seven `tools/`-prefixed literals; the other
  three are the prose citations S5 leaves alone.
- **AC5** — with backtick-delimited spans and fenced blocks removed,
  `grep -cE 'tools/[A-Za-z0-9_-]+/' tools/lexicon/lexicon.py` returns 0, and that file's row in
  `tools/install-prefix-carried.txt` falls to exactly the count of its surviving PROSE citations —
  the ones S5 is forbidden to touch.

  **AMENDED at rev-5.** The criterion demanded NO row at all, on a measurement taken when all three
  prose citations spelled a bare directory and were therefore invisible to the §4 predicate, which
  requires a kit name followed by a real FILE. The file has moved since and one of them now spells a
  real file, so it IS a ratchet hit — while remaining exactly the kind of citation S5 says to leave
  alone, because rewriting it destroys the explanation it carries. Demanding zero would force S5 to
  do the one thing §2 forbids it. What the criterion asserts instead is that the EXECUTABLE
  population S5 owns goes to zero, which the stripped grep measures, and that the residual row is
  prose and nothing else. The measured value goes in the acceptance ledger, not here. Observe RED first: at `9ddcc5c9` the same stripped count is 4 — the docstring
  usage block at `:5-7` and the runtime usage printer at `:559`, which is the whole of the
  population S5 touches — and that file's ratchet row reads 4 there, not 3. Measured rather than
  reasoned, at `9ddcc5c9`: the §4 predicate hits lines `5`, `6`, `7` and `559` and NONE of `:245`,
  `:246`, `:265`, because it requires a kit name followed by a real FILE and those three spell
  `tools/codebase-map/` followed by `/`, by `*` and by a space. So the three prose citations S5
  leaves alone are invisible to the ratchet exactly as they are to the executable predicate, and no
  reading of this criterion may assert a residual row of 3. An unstripped `grep` returning 0 is not
  this criterion either, and would demand a rewrite §2 does not propose.
- **AC6** — Editing one inlined `render_doc` copy without the other reds
  `bash tools/memory-tree/kit-dogfood-parity.test.sh`, and the marker-derived population names both
  `tools/memory-tree/adopt-memory-tree.sh` and `tools/memory-tree/kit-dogfood-parity.test.sh`.
- **AC7** — `bash tools/run-gates/run-gates.sh` is green, and green again under `GATE_SELFTESTS=1`,
  so the `install-prefix self-test` kit-subject leg is exercised rather than held past this change.

## 7. Gates

`bash tools/run-gates/run-gates.sh` full bar. Specifically the `install-prefix (shipped surface)`
leg, its `install-prefix self-test` kit-subject sibling, `kit/dogfood doc parity`, and the
`python resolver (behaviour + inline parity + idiom ban)` leg whose marker mechanism S6 reuses.
Adds four arms and one tracked ratchet file. **Adds no gate leg**, deliberately: extending the
existing script leaves `tools/gate-legs.json` unchanged and therefore does not re-stamp the kickoff
manifest.

## 8. Open questions

- **F1 — per-file counts, or per-line waivers like the existing arm?** Per file. Measured: the
  existing shape is `<path>:<line>`, and one row per hit LINE across the carried population —
  hundreds of rows, counted by the artifact and by nothing here — would go stale on the first edit
  above any waived line, at which point the stale-waiver arm at `:92-97` reds for a reason unrelated
  to the class. Per file trades swap-blindness for a ratchet that survives ordinary editing.
  RESOLVED (agent, 2026-08-24, delegated): per file, under the full-scope approval.
- **F2 — should `WIRE-INTO-PROJECT.md`'s prescriptive paths be converted?** No. They are the
  instructions for choosing a prefix, so they must show a concrete one. They enter the ratchet with
  that reason and stay; converting them would make the install document teach a placeholder nobody
  substitutes.
  RESOLVED (agent, 2026-08-24, delegated): ratcheted, not converted.

## 9. Revision log

- rev-5 · 2026-08-26 · BUILT and CLOSED on node `a`, session `aResumedRelay`. ONE criterion
  AMENDED, AC5, and the amendment is the same shape the unit is about: it demanded a residual of
  ZERO on a measurement taken when all three of the file's prose citations spelled a bare directory
  and were invisible to the §4 predicate. One of them now spells a real file and is a hit, while
  remaining exactly the citation §2 forbids S5 to rewrite — so the criterion as written required S5
  to do the one thing it may not. It now asserts what it was standing in for: the executable
  population goes to zero, and the residual is prose. Everything else was observed as written,
  including both halves of AC2 and AC4 and the staged drift for AC6. Two things the spec did not
  foresee, both in the ledger: python's newline translation made the derived population arrive with
  a trailing CR, so all 181 paths failed a file test and the first ratchet came out empty; and the
  repo's own idiom ban redded the launcher fallback this arm was first written with, which is the
  ban doing its job. No `BRANCH_PIN` movement — this unit touches no deployer refusal branch.

- rev-4 · 2026-08-24 · round-3 fold: the §9 entry shape is corrected to the mandated `round-N fold:` colon form.
- rev-3 · 2026-08-24 · round-2 fold: every item re-measured at `9ddcc5c9` before it was written.
  AC5 no longer contradicts the predicate printed two sections above it, though not for the reason
  the review gave: its premise was that §4's regex still MATCHES the three prose citations, and it
  does not — the regex demands a kit name followed by a real FILE, so `tools/codebase-map/`
  followed by `/`, `*` or a space is no hit — which makes the true residual row 0 rather than 3, so
  AC5 now asserts that S4 deletes the row and records the pre-fix reading of 4. The `534` figure is
  withdrawn consistently: §4's alternatives and §8 F1 were still asserting it as live fact after §4
  withdrew it, and both now size the debt by the artifact, which is the claim AC1 already makes.
  §4's carrier paragraph is corrected in two places — `tools/check-kit-versions.sh` IS
  resolve_entry-resolved and `WIRE-INTO-PROJECT.md` is NOT — and S2 therefore declares
  `WIRE-INTO-PROJECT.md` as one named addition to the derived population, without which F2's ratchet
  answer would be false and its 27 hit lines would be graded by neither arm.
- rev-2 · 2026-08-24 · folded the pre-code review: §4's inventory table is replaced by the exact
  predicate `--write-ratchet` implements, because rev-1's 93/534 reproduced under none of six
  re-measured populations and neither did the backlog row's 59 files. AC1 now asserts that
  `--list`'s section and the ratchet file agree byte-for-byte out of one function, which makes the
  artifact the claim instead of a prose number. AC5 is narrowed to the executable population — the
  four literals S5 actually reaches — and asserts the residual ratchet row of 3 rather than
  demanding a count §2 cannot deliver; §1 and S5 now state the split as four resolvable paths plus
  three prose citations at `:245`, `:246` and `:265`. The unsourced per-file counts in §4 and F2 are
  withdrawn, except `WIRE-INTO-PROJECT.md`'s 27, re-verified under the published predicate.
- rev-1 · 2026-08-24 · initial draft, from the kit-sync design pass. Three corrections to the
  design-pass brief, each re-measured at `9ddcc5c9`. **(a)** The brief's "59 files under gov `tools/`
  contain a literal `tools/<kit>/` path" does not reproduce at any population tried: 93 of 168
  shippable sources (534 lines), 64 non-test (219 lines), 77 files over the existing arm's
  glob-derived shipped surface (340 lines), or 70 of those restricted to `tools/`. This spec carries
  the measured numbers and states its population. **(b)** The brief asks that `render_doc` be
  promoted "into govkit as the ONE renderer". It cannot be: every consumer is shipped bash running
  standalone in the adopter's tree, and govkit is Python that never runs there —
  `adopt-memory-tree.sh`, `kit-dogfood-parity.test.sh`, `adopt-unattended.sh`,
  `adopt-memory-recall.sh` and `cross-component.test.sh` are five shell spellings and there are zero
  Python callers. S6 promotes it under the `resolve_python` canonical-copy pattern instead, which is
  this repo's existing answer to exactly this shape. **(c)** The brief reads
  `check-install-prefix.sh:53` as blessing the placeholder form; the blessing is implemented at
  `:55`, by the `{}` characters in the excluded lead-character class, and `:52-54` is the comment
  explaining it. Verified and unchanged from the brief: `blob_at` at `:2453`, `write_bytes` at
  `:2469`, `resolve_tokens` at `:516`, `render_doc` at `adopt-memory-tree.sh:64-78`, and lexicon's
  seven paths in both trees.

## 10. Reuse audit

No new mechanism. S2's population comes from `read_descriptors` plus `resolve_entry` (`:270`), the
same pair `planned_writes` (`:1359`) uses, rather than a second path map — the duplicate-answer
defect this build fixes elsewhere. S4's ratchet reuses the shrink-only shape and the stale-row rule
already implemented for `tools/install-prefix-waivers.txt`, in a second file only because the two
populations differ. S6 reuses the `resolve_python` canonical-copy machinery at
`tools/lib/resolve-python.sh`, whose parity gate already derives its population by grepping an inline
marker, so `render_doc` enrols into an existing gate rather than earning a new one. S3's announced
skip reuses the existing arm's two empty-population refusals at `:39` and `:50`. Nothing here touches
`resolve_tokens`, which stays a substituter for paths and argv and never becomes a body renderer.
