# PLAY-aSiftedPlaybook-2 — the default branch stops being hardcoded as `main`

**Status:** SPECCED · rev-1 · 2026-08-11 · node a · Tier-2 · base 91ef1b05 · streams playbook

## 1. Goal

`parallel-coding-governance.template.md` spells the default branch as the literal `main` in
seventeen places, including two output formats it declares MANDATORY, while every other layer of
this chain resolves the branch dynamically. Introduce `{{DEFAULT_BRANCH}}` so a project on `master`,
`trunk` or `develop` receives a ruleset that is true for it.

## 2. Scope (IN)

- **S1 — the placeholder.** `{{DEFAULT_BRANCH}}` becomes the 37th placeholder. **The name is not
  invented**: `skills/session-kickoff/MANIFEST-TEMPLATE.md:60,126` already defines it with identical
  semantics and documents its derivation from `git symbolic-ref`, and this repo's own filled
  manifest carries the result at `.claude/SESSION-KICKOFF.md:39`. This unit adopts the existing name
  and can copy its fill instruction verbatim, which also makes the two halves of the product agree
  on one spelling.
- **S2 — the seventeen substitutions.** Anchored on verified (line, column) pairs, never a global
  replace. Of thirty `main` substrings in the file, thirteen are other senses and must NOT be
  touched: eleven are the `.domain-rules.md` filename, one is the English adjective at `:100`, and
  one is `main-loop` at `:157`.
- **S3 — the two §16 micro-formats.** `:218` (`pushed <remote>/main …`) and `:219`
  (`merged --no-ff <branch> → main <sha> …`). Treated as their own scope item because §16 declares
  micro-formats "MANDATORY, byte-stable, greppable" and a reader is entitled to know the change was
  deliberate. See §4 and F1.
- **S4 — the customize catalogue.** `parallel-coding-governance.customize.md` gains
  `{{DEFAULT_BRANCH}}` in the template group with its fill instruction, and the counts move
  **36 → 37 and 23 → 24 only**.

## 3. Non-goals (OUT)

- **Parameterizing the companions.** Verified: `domain-rules.md`'s five `main` hits and
  `customize.md`'s three are all other senses. Neither file needs a branch substitution, and adding
  one would create a placeholder with no referent.
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
| total | `customize.md:20` | 36 | **37** |
| in the template | `customize.md:23` | 23 | **24** |
| in the companion | `customize.md:45` | 14 | 14 — unchanged |
| "13 of the 36 … unfilled in the companion" | `customize.md:15` | 13 | 13 — the phrasing's `36` moves, the `13` does not |
| the same claim, restated | `WIRE-INTO-PROJECT.md:98` | 13 | 13 — same treatment |

A template-only placeholder cannot change a companion-only count. A spec that "fixed all four
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

- **AC1** — When `grep -c '{{DEFAULT_BRANCH}}' parallel-coding-governance.template.md` runs, it
  returns 17.
- **AC2** — When `grep -n '\bmain\b' parallel-coding-governance.template.md` runs, every surviving
  hit is one of the thirteen non-branch senses, enumerated by line in the build record. **Zero
  surviving hits mean the substitution was too greedy**, since the `.domain-rules.md` filename must
  still be intact — so this AC fails in both directions, which is the point.
- **AC3** — When `bash tools/check-template-size.sh` runs, it exits 0 and reports the measured size
  read FROM the gate.
- **AC4** — When the placeholder sets are recomputed by `PLAY-aSiftedPlaybook-4` AC1's recipe, the
  union is 37, the template group is 24, the companion group is 14, and the intersection is still
  exactly `{{MEMORY_ROOT}}`.
- **AC5** — When `grep -nE '\{\{[A-Z]' ` is run over a freshly instantiated copy of both deploy
  files, it returns empty — the new placeholder is fillable and documented, not merely added.
- **AC6** — When `bash skills/session-kickoff/manifest-check.sh` runs, it exits 0. Its `{{[A-Z]`
  ban is scoped to `.claude/SESSION-KICKOFF.md` and never reads the playbook, so a 37th placeholder
  cannot trip it — confirmed, and stated so the build does not go looking for a red that cannot
  happen.

## 7. Gates

- `bash tools/check-template-size.sh` — the template grows by 238 bytes.
- `bash skills/session-kickoff/manifest-check.sh` — the template is a watched pathspec; re-stamp.
- `bash tools/memory-tree/check-memory-hygiene.sh`, `python tools/memory-tree/gotchas.py --for-diff`.
- `python tools/drift-audit/drift_report.py` — the template is in `PRODUCT_GLOBS`; no non-terminal
  spec id may be cited from it.
- `bash tools/run-gates.sh` at the push boundary.
- No new gate; the left-shift is `TOOL-aSiftedPlaybook-3`.

## 8. Open questions

- **F1 — may a MANDATORY byte-stable micro-format contain a deploy-time placeholder?** §4 argues it
  may, on the ground that byte-stability describes the instantiated document and the template's two
  bracket shapes already separate runtime slots from deploy-time ones.
  **Recommendation: parameterize both micro-formats.** The fork is left open rather than resolved
  because §16 is the one section that declares a rule about its own formatting, and a reading of it
  that turns out to be the owner's rather than mine would change the deliverable. If the owner
  vetoes, the fallback is to leave `:218-219` literal and add one sentence noting the formats assume
  `main` — worse, but honest, and cheap to revert later.

## 9. Revision log

- rev-1 · 2026-08-11 · initial draft. The seventeen-of-thirty split, the 238-byte cost and the
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

`python tools/codebase-map/reuse_lookup.py "governance playbook template companions"` returns no
dossier for the playbook — the map has seven and none covers this product. Recorded as evidence for
`TOOL-aSiftedPlaybook-1` F1 option 3, which would mint one.

Recall terms used, recorded per M5: `playbook template companion customize domain-rules agnostic
adopter stale externalize byte gate section stub kit wiring`. No prior record proposes
parameterizing the branch name; `PLAY-aCandidStub-1` audited these files at v2.5 without raising it,
which is why it survived a full adversarial pass — a hardcoded `main` reads as correct in a repo
whose branch is `main`.
