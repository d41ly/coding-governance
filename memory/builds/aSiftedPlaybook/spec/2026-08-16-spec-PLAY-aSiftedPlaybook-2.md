# PLAY-aSiftedPlaybook-2 — the default branch stops being hardcoded as `main`

**Status:** CLOSED · rev-7 · 2026-08-16 · node a · Tier-2 · base 91ef1b05 · streams playbook · ratified 2026-08-16

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-16-review-PLAY-aSiftedPlaybook-1-1.md](../reviews/2026-08-16-review-PLAY-aSiftedPlaybook-1-1.md) | spec-audit | PLAY-aSiftedPlaybook-1 PLAY-aSiftedPlaybook-3 PLAY-aSiftedPlaybook-4 TOOL-aSiftedPlaybook-1 TOOL-aSiftedPlaybook-2 TOOL-aSiftedPlaybook-3 |
| [2026-08-16-review-PLAY-aSiftedPlaybook-1-2.md](../reviews/2026-08-16-review-PLAY-aSiftedPlaybook-1-2.md) | spec-audit | PLAY-aSiftedPlaybook-1 PLAY-aSiftedPlaybook-3 PLAY-aSiftedPlaybook-4 TOOL-aSiftedPlaybook-1 TOOL-aSiftedPlaybook-2 TOOL-aSiftedPlaybook-3 |
| [2026-08-16-review-PLAY-aSiftedPlaybook-1-3.md](../reviews/2026-08-16-review-PLAY-aSiftedPlaybook-1-3.md) | spec-audit | PLAY-aSiftedPlaybook-3 TOOL-aSiftedPlaybook-1 TOOL-aSiftedPlaybook-2 PLAY-aSiftedPlaybook-1 TOOL-aSiftedPlaybook-3 |
| [2026-08-16-review-PLAY-aSiftedPlaybook-1-4.md](../reviews/2026-08-16-review-PLAY-aSiftedPlaybook-1-4.md) | spec-audit | PLAY-aSiftedPlaybook-1 PLAY-aSiftedPlaybook-3 PLAY-aSiftedPlaybook-4 TOOL-aSiftedPlaybook-1 TOOL-aSiftedPlaybook-2 TOOL-aSiftedPlaybook-3 |
| [2026-08-16-review-PLAY-aSiftedPlaybook-1-5.md](../reviews/2026-08-16-review-PLAY-aSiftedPlaybook-1-5.md) | spec-audit | TOOL-aSiftedPlaybook-1 TOOL-aSiftedPlaybook-2 TOOL-aSiftedPlaybook-3 PLAY-aSiftedPlaybook-3 PLAY-aSiftedPlaybook-1 PLAY-aSiftedPlaybook-4 |
| [2026-08-16-review-PLAY-aSiftedPlaybook-2-6.md](../reviews/2026-08-16-review-PLAY-aSiftedPlaybook-2-6.md) | diff-review | PLAY-aSiftedPlaybook-3 |

<!-- /gen:spec-records -->

## 1. Goal

`parallel-coding-governance.template.md` spells the default branch as the literal `main` in
seventeen places, including two output formats it declares MANDATORY, while every other layer of
this chain resolves the branch dynamically. Introduce `{{DEFAULT_BRANCH}}` so a project on `master`,
`trunk` or `develop` receives a ruleset that is true for it.

## 2. Scope (IN)

- **S1 — the placeholder.** `{{DEFAULT_BRANCH}}` becomes the 37th placeholder. **The name is not
  invented**: `skills/session-kickoff/MANIFEST-TEMPLATE.md:60,126` already defines it with identical
  semantics and documents its derivation from `git symbolic-ref`, and this repo's own filled
  manifest carries the result on its `Remote · default branch:` line
  (`memory/guides/SESSION-KICKOFF.md:52` at HEAD — cited by content because five units re-stamp that
  file and a line anchor in it will not survive them). This unit adopts the existing name
  and can copy its fill instruction verbatim, which also makes the two halves of the product agree
  on one spelling.
- **S2 — the seventeen substitutions.** Anchored on verified (line, column) pairs, never a global
  replace. Measured at BASE: the file holds **30 `main` substrings**, of which **11 sit inside the
  word `domain`** — ten in the `.domain-rules.md` filename and one in "domain checklists" at `:4`,
  a distinction that matters to anyone writing a guard against the filename. The remaining **19 are
  word-boundary `main`** (`grep -oE '\bmain\b'`), spread over 16 lines. Two of those 19 are not the
  branch: the English adjective at `:100` and `main-loop` at `:157`. **17 branch senses remain, on
  14 lines.**
- **S3 — the two §16 micro-formats.** `:218` (`pushed <remote>/main …`) and `:219`
  (`merged --no-ff <branch> → main <sha> …`). Treated as their own scope item because §16 declares
  micro-formats "MANDATORY, byte-stable, greppable" and a reader is entitled to know the change was
  deliberate. See §4 and F1.
- **S4 — the customize catalogue.** `parallel-coding-governance.customize.md` gains
  `{{DEFAULT_BRANCH}}` in the template group with its fill instruction, and the counts move
  **36 → 37 and 23 → 24 only**.
- **S5 — the runbook's restated count.** `WIRE-INTO-PROJECT.md:98` reads "the companion carries 13
  of the 36 placeholders" and is that file's only `36`; the **36 becomes 37** here. The **13 is
  separately wrong and is NOT this unit's to fix** — the companion carries 14 — and
  `PLAY-aSiftedPlaybook-4` S4 corrects it at position 3, before this unit runs at position 5. An
  earlier draft of this item asserted "the 13 stays 13", which was true only under the audit's
  mistaken R2.
  It appeared in §4's Files touched but in no scope item and no acceptance criterion, so a builder
  working §2 and §6 would ship a correct template and companion while the runbook still said 36,
  with every AC green — the same shape as `PLAY-aSiftedPlaybook-1`'s S8 defect, one unit over.
  `PLAY-aSiftedPlaybook-3` S6 also edits this file, so whichever lands second re-derives its anchor.

## 3. Non-goals (OUT)

- **Parameterizing the companions.** Verified: `domain-rules.md` has **four** `main` substrings and
  `customize.md` three, all other senses. The four are `domain` at `:1` and `:5`, `maintained` at
  `:33`, and **`push-main` at `:100`** — a script name, called out by name because it is exactly what
  a careless global substitution corrupts. Neither file needs a branch substitution, and adding one
  would create a placeholder with no referent.
- **Changing the trunk-based rule.** §3's "merge small and often to LOCAL `<default>`" keeps its
  meaning exactly. Only the branch's NAME becomes a variable; the workflow does not.
- **Fixing the disjointness sentence.** That is `PLAY-aSiftedPlaybook-4` S1, which corrects it for
  36. This unit re-states it for 37. Ordering is in §4 Rollout.
- **A `{{REMOTE_NAME}}` placeholder.** `origin` is also hardcoded, in the same micro-format. Out of
  scope: it is a second mechanism, it was not in the audit, and `origin` is near-universal in a way
  `main` is not. Follow-up row.

## 4. Design

### The counts move by ONE each, and only two of the four move at all

Four numbers describe the placeholder sets and it is tempting to bump all of them. Three would be
wrong:

| Claim | Location | Today | After |
|---|---|---|---|
| total | the sentence stating the total | 36 | **37** |
| in the template | the template group heading | 23 | **24** |
| in the companion | the companion group heading | 14 | 14 — unchanged |
| "13 of the 36 … unfilled in the companion" | the fill-procedure sentence | 13 | **14** via `PLAY-4` S4; the `36` moves here |
| the same claim, restated | `WIRE-INTO-PROJECT.md` | 13 | **14** via `PLAY-4` S4; the `36` moves here |

Cited by stated VALUE rather than by line number on purpose: at BASE these sit at `customize.md:20`,
`:23`, `:45`, `:15` and `WIRE-INTO-PROJECT.md:98`, but §4 Rollout sequences this unit AFTER
`PLAY-aSiftedPlaybook-4`, which rewrites the first and fourth of those sentences. Line anchors
written here would be stale by the time this unit is built.

A template-only placeholder cannot change a companion-EXCLUSIVE count — and 13 was never the
companion's carried count in the first place (it carries 14), which `PLAY-aSiftedPlaybook-4` S4
fixes before this unit runs. A spec that "fixed all four
numbers uniformly" would introduce a fresh error into the very file it was correcting, which is
worth stating because that is the natural mistake here.

### The §16 micro-format question resolves on slot KIND, not on byte-stability

§16 declares its micro-formats byte-stable, so parameterizing them looks like a contradiction. It is
not, and the template's own notation already draws the distinction:

- `<remote>`, `<old>`, `<new>`, `<branch>`, `<sha>`, `<port>` are **runtime slots** — filled
  differently on every emission, angle-bracketed.
- `{{DEFAULT_BRANCH}}` is a **deploy-time slot** — filled once, at instantiation, brace-shaped, and
  gone before any agent ever emits the format.

Byte-stability is a property of the INSTANTIATED document, which is what an agent reads and what a
grep would run against. A filled copy on `master` emits `pushed origin/master …` on every push, as
byte-stable and greppable as `main` ever was. The template is not the artifact the property
describes.

The alternative — leaving them literal — makes §16 mandate emitting a line that is factually wrong
for any project not on `main`, in the one part of §16 whose stated purpose is to be machine-readable.

### Cost

Measured by simulation on the real file, not estimated: **exactly +238 bytes** (32682 → 32920). The
template has 86 free at BASE, so at the current ceiling this unit does not fit.

**It is not, however, blocked by the ceiling in principle.** A shorter name — `{{TRUNK}}` — costs
+85 against 86 free and would land today. That option is rejected on naming grounds, not size:
`{{DEFAULT_BRANCH}}` already exists in this product with documented semantics, and minting a second,
shorter spelling for the same concept is the hand-kept-second-copy defect this build is otherwise
busy removing. **Recorded explicitly so this unit is not read as evidence that the raise was
necessary** — it was a choice between a good name and a small diff, and the raise made the choice
free.

### Files touched (estimate)

| File | Change |
|---|---|
| `parallel-coding-governance.template.md` | 17 substitutions at verified positions |
| `parallel-coding-governance.customize.md` | S4: catalogue entry + two counts |
| `WIRE-INTO-PROJECT.md` | `:98`'s `36` in the restated claim |

### Rollout

Depends on `TOOL-aSiftedPlaybook-1` (the ceiling) unless the owner picks `{{TRUNK}}`. Lands after
`PLAY-aSiftedPlaybook-4`, so the disjointness sentence is corrected once and then updated, rather
than being written twice against two different totals.

### Alternatives rejected

- **`{{TRUNK}}`** — see Cost. Fits today, rejected on naming consistency.
- **Prose instead of a placeholder** ("your default branch"). Rejected: the file's whole contract is
  that `grep -nE '\{\{[A-Z]'` returning empty proves instantiation is complete. Prose is invisible to
  that check, so an unfilled branch name would ship silently.
- **Leaving §16 literal and parameterizing only the rules.** Rejected: it produces a document whose
  rules say one thing and whose mandatory output format says another, which is worse than either
  consistent option.

## 5. Production-readiness checklist

- security — N/A.
- perf / scale — N/A.
- a11y / i18n — N/A.
- error / empty / loading states — N/A.
- observability — N/A.
- risks — **the mis-substitution risk is the whole risk.** Thirteen of thirty hits must not be
  touched, and eleven of those are inside a filename that contains the word. A global replace
  corrupts the companion's own name in every §-stub. AC2 exists to catch exactly that.
- testing + left-shift gates — nothing verifies that a placeholder is catalogued, or that the
  catalogue's counts are true. `TOOL-aSiftedPlaybook-3` is where that becomes machine-checked; until
  then S4 is a documented check.
- migration / rollback — an adopter re-pulling gains one placeholder to fill. `customize.md`'s
  re-pull procedure already handles a new placeholder; no migration step is owed.
- user docs — these files ARE the docs.

## 6. Acceptance criteria

- **AC1** — When `grep -o '{{DEFAULT_BRANCH}}' parallel-coding-governance.template.md | wc -l` runs,
  it returns **17**; when `grep -c '{{DEFAULT_BRANCH}}' …` runs it returns **14**. Both figures are
  stated because `grep -c` counts matching LINES, not occurrences, and template `:51` alone carries
  two branch senses in one line — an AC spelled with `grep -c` and the number 17 fails a correct
  build.
- **AC2** — Two observations, because one pattern cannot see both failure modes:
  - **(a) not too greedy:** `grep -c 'parallel-coding-governance\.domain-rules\.md'
    parallel-coding-governance.template.md` still returns its BASE value of 10. The filename is the
    substitution's main corruption target and **`\bmain\b` never matched it** — `domain` contains
    `main` only as a substring, with no word boundary before the `m` — so a word-boundary grep is
    structurally blind to that corruption and cannot be the check for it.
  - **(b) not too timid:** `grep -oE '\bmain\b' parallel-coding-governance.template.md | wc -l`
    returns exactly **2** — the adjective at `:100` and `main-loop` at `:157`, both named in §2.
- **AC3** — When `bash tools/check-template-size.sh` runs, it exits 0 and reports the measured size
  read FROM the gate.
- **AC4** — When the placeholder sets are recomputed by `PLAY-aSiftedPlaybook-4` AC1's recipe, the
  union is 37, the template group is 24, the companion group is 14, and the intersection is still
  exactly `{{MEMORY_ROOT}}`.
- **AC5** — When `parallel-coding-governance.customize.md` is read, `{{DEFAULT_BRANCH}}` appears in
  the template group with a fill instruction whose derivation matches
  `skills/session-kickoff/MANIFEST-TEMPLATE.md:60,126` verbatim. **Deliberately not phrased as "run
  the grep over a freshly instantiated copy"**: nothing in this repo instantiates the playbook —
  there is no `adopt-playbook.sh` — so that observation names a step a builder cannot perform, and
  an AC nobody can run is not an AC.
- **AC7** — When `grep -n '36\|37' WIRE-INTO-PROJECT.md` runs, the restated placeholder claim reads
  37. Its companion figure is 14, corrected by `PLAY-aSiftedPlaybook-4` S4 at position 3 — this unit
  moves the total and must not re-introduce 13.
- **AC6** — When `bash skills/session-kickoff/manifest-check.sh` runs, it exits 0. Its `{{[A-Z]`
  ban is scoped to `memory/guides/SESSION-KICKOFF.md` and never reads the playbook, so a 37th placeholder
  cannot trip it — confirmed, and stated so the build does not go looking for a red that cannot
  happen.

## 7. Gates

- `bash tools/check-template-size.sh` — the template grows by 238 bytes.
- `bash skills/session-kickoff/manifest-check.sh` — the template is a watched pathspec; re-stamp.
- `bash tools/memory-tree/check-memory-hygiene.sh`, `python tools/memory-tree/gotchas.py --for-diff`.
- `python tools/drift-audit/drift_report.py --check` — the template is in `PRODUCT_GLOBS`; no non-terminal
  spec id may be cited from it.
- `bash tools/run-gates.sh` at the push boundary.
- No new gate; the left-shift is `TOOL-aSiftedPlaybook-3`.

## 8. Open questions

none — the fork below is RESOLVED (owner, 2026-08-16).

- **F1 — may a MANDATORY byte-stable micro-format contain a deploy-time placeholder?**
  **RESOLVED (owner, 2026-08-16): yes — parameterize both micro-formats.** S3 builds it as specced.
  The ratified reading is §4's: byte-stability is a property of the INSTANTIATED document, and the
  template already separates runtime slots (`<remote>`, `<sha>`) from deploy-time ones
  (`{{DEFAULT_BRANCH}}`) by bracket shape. The rejected fallback was leaving `:218-219` literal with
  a sentence noting they assume `main`.

## 9. Revision log

- rev-7 · 2026-08-16 · folded round-3 M9. S1's manifest anchor was path-substituted by the reconcile
  but never re-derived: `:39` is an acceptance-criteria line, and the default-branch line is `:52`.
  Now cited by content, since S1's whole argument depends on a builder finding it.
- rev-6 · 2026-08-16 · folded round-3 H10. S5 preserved "the 13 stays 13", which was true only under
  the 2026-08-16 audit's mistaken R2 — the companion carries 14, not 13. The correction belongs to
  `PLAY-aSiftedPlaybook-4` S4, which lands two positions earlier; this unit now moves only the total.
- rev-5 · 2026-08-16 · folded round-2 lows. §3's companion count was five against a measured four,
  and now names `push-main` at `domain-rules.md:100` explicitly, since a script name is what a
  global substitution corrupts. §10's "no playbook dossier" is re-dated as a BASE-time observation
  and no longer points at the rejected F1 option 3.
- rev-4 · 2026-08-16 · folded round-2 audit finding H8. `WIRE-INTO-PROJECT.md:98` sat in §4's Files
  touched with no scope item and no AC, so every acceptance criterion would have gone green over a
  runbook still claiming 36 placeholders. Added as S5 with AC7, and noted the anchor collision with
  `PLAY-aSiftedPlaybook-3` S6, which edits the same file.
- rev-3 · 2026-08-16 · owner resolved F1: parameterize both §16 micro-formats. No scope change —
  S3 was already written that way — but the unit is now ratified rather than pending a reading of
  §16 that could have gone the other way.
- rev-2 · 2026-08-16 · folded four findings from the spec audit `wf_4ed62ebb-cef`, all re-measured
  before folding. AC1 counted lines where it meant occurrences and would have failed a correct build
  (17 occurrences sit on 14 lines). AC2 was structurally blind to the corruption it claimed to
  catch — `\bmain\b` scores zero on `domain-rules`, so it never guarded the filename — and is now
  two observations. AC5 named an instantiation step this repo has no tool to perform. S2's
  "eleven are the filename" was off by one: eleven are the word `domain`, ten of them the filename.
- rev-1 · 2026-08-16 · initial draft. The seventeen-of-thirty split, the 238-byte cost and the
  `{{TRUNK}}` alternative were measured by the `default-branch` lens of `wf_4e13d9e7-550`; the
  pre-existing `{{DEFAULT_BRANCH}}` in `MANIFEST-TEMPLATE.md` was found by that lens and changed the
  unit's design from "mint a placeholder" to "adopt the one this product already has".

## 10. Reuse audit

**An existing seam fits, and finding it changed the design.**
`skills/session-kickoff/MANIFEST-TEMPLATE.md:60,126` already defines `{{DEFAULT_BRANCH}}` with the
same meaning and a documented derivation (`git symbolic-ref --short refs/remotes/<remote>/HEAD`,
falling back to `main` then `master`). The kickoff engine resolves it at Step 0, and
`.githooks/pre-commit:16` and `tools/push-main.sh:20` resolve the same value at runtime through
`GOV_DEFAULT_BRANCH`. This unit therefore extends an existing product-wide convention rather than
introducing one, and the customize entry should cite the manifest template's wording so the two do
not drift into two derivations of one value.

`python tools/codebase-map/reuse_lookup.py "governance playbook template companions"` returned no
dossier for the playbook **at BASE `91ef1b05`** — the map had seven and none covered this product.
A BASE-time observation, not a live one: the owner resolved `TOOL-aSiftedPlaybook-1` F1 against
minting a dossier there, and `TOOL-aSiftedPlaybook-2` S5 mints
`memory/map/features/playbook.md` instead, after which this paragraph's premise no longer holds.

Recall terms used, recorded per M5: `playbook template companion customize domain-rules agnostic
adopter stale externalize byte gate section stub kit wiring`. No prior record proposes
parameterizing the branch name; `PLAY-aCandidStub-1` audited these files at v2.5 without raising it,
which is why it survived a full adversarial pass — a hardcoded `main` reads as correct in a repo
whose branch is `main`.
