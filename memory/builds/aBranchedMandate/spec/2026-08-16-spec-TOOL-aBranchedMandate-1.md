# TOOL-aBranchedMandate-1 — the memory-recall adopter stops reding the bar on a checkout artifact

**Status:** SPECCED · rev-1 · 2026-08-16 · node a · Tier-1 · base 96141aed · streams tooling

## 1. Goal

`tools/memory-recall/adopt-memory-recall.sh --check` byte-compares the rendered Skill against a fresh
render without normalising CR, so every fresh worktree on this fleet reds a merge-bar leg on a file
nobody edited. Give it the normalising half its two sibling adopters already have.

## 2. Scope (IN)

- **S1** — CR-normalise the Skill side of the `--check` comparison in
  `tools/memory-recall/adopt-memory-recall.sh`, matching the seam
  `tools/unattended/adopt-unattended.sh:122` already uses.
- **S2** — CR-normalise the same side of the truncated diff this script prints on failure, so the
  reported hunks are the real drift rather than every line of the file.
- **S3** — one runnable arm that fails if S1 regresses: render, write a CRLF copy of the rendered
  Skill, assert `--check` still exits 0. Its home is F1.
- **S4** — the header comment gains the rule the other two adopters state in their own headers, so
  the next reader of this file learns why the normalisation is there rather than deleting it as
  redundant.

## 3. Non-goals (OUT)

- Changing `.gitattributes`. The `eol=lf` pin is the other half and it is correct; the gotcha record
  says both halves are needed and this unit adds the missing one.
- Changing what `tools/check-wiring.sh` reports about CRLF. That is `TOOL-aBranchedMandate-2`, and it
  depends on this unit landing first.
- Auditing every other byte-comparing gate in the tree for the same class. Three adopters carry the
  `eol=lf` pin on a `.claude/skills/**` render and this unit measures all three; a tree-wide sweep is
  a separate unit nobody has scoped.
- Rendering or re-scaffolding the Skill's content. Nothing about the render is wrong.

## 4. Design

The rule is already written down. `memory/gotchas/gate-green-by-accident-on-generated-bytes.md`
states that a generated file needs **both** an `eol=lf` pin and a normalising comparison, and that
either alone leaves the failure mode. `tools/unattended/adopt-unattended.sh` states the same rule in
its header and implements it. This adopter has the pin and not the comparison.

### Inventory

Measured in this worktree at BASE, by running each adopter's `--check`:

| Adopter | Pin in `.gitattributes` | CR-normalising comparison | `--check` here |
|---|---|---|---|
| `tools/unattended/adopt-unattended.sh` | yes | yes | exit 0 |
| `tools/drift-audit/adopt-drift-audit.sh` | yes | yes | exit 0 |
| `tools/memory-recall/adopt-memory-recall.sh` | yes | **no** | **exit 1** |

The failure was confirmed to be line endings alone and nothing else. The Skill holds CRLF on 89 of
89 lines. With CR stripped from the working copy, `--check` prints
`ok       memory-recall skill — SKILL.md matches the conf` and exits 0; the original bytes were then
restored. That test matters because the diff this script prints is truncated to twenty lines, so
reading the log cannot distinguish a pure line-ending diff from a content drift whose first twenty
lines happen to be line-ending noise.

### Migration

None. The committed bytes do not move — the index already normalises on commit, which is why
`git status` is clean while the working copy holds CRLF. Only the comparison changes.

### Files touched (estimate)

| Path | Change |
|---|---|
| `tools/memory-recall/adopt-memory-recall.sh` | S1, S2, S4 |
| F1's chosen host | S3 |

### Alternatives rejected

- **Normalise both sides.** The render side is produced by this script and is LF by construction; a
  `tr` on it would be a no-op that reads as though the render were untrusted. The sibling at
  `adopt-unattended.sh:122` normalises only the on-disk side, and matching it keeps one shape.
- **Have the gate runner normalise.** It would fix this leg and hide the class everywhere else,
  including in adopters shipped to other repos where no gate runner of ours exists.
- **Drop the `eol=lf` pin instead.** The pin is what makes the committed bytes right, and
  `tools/check-wiring.sh:198` derives its whole eol population from it. Dropping it trades a red leg
  for a silent one.

## 5. Production-readiness checklist

- security — N/A. The comparison's strictness about content is unchanged; only line endings stop
  counting as content.
- perf / scale — N/A. One `tr` over an 89-line file.
- a11y — N/A. No user-facing surface.
- i18n — N/A. No message content changes.
- error / empty / loading states — the existing empty-render guard is untouched. This unit must not
  weaken it: a normalised comparison of two empty files is the green-by-absence shape the sibling
  adopter refuses explicitly, and the arm in S3 does not exercise it.
- observability — the truncated failure diff becomes readable, which is S2. Today a CR-only drift and
  a real content drift print the same wall of removed lines.
- risks — the one real risk is that normalisation hides a genuine drift that consists only of line
  endings *in the render*. That cannot happen here: the render is generated LF in-process.
- testing + left-shift gates — S3. The regression is invisible without a fixture, because the tracked
  worktree on a node that has run the repair is LF and the comparison passes for the wrong reason.
- migration / rollback — revert the commit; nothing persists.
- user docs — S4 only. No adopter-facing instruction changes.

## 6. Acceptance criteria

- **AC1** — When `bash tools/memory-recall/adopt-memory-recall.sh --check` runs in a worktree whose
  `.claude/skills/memory-recall/SKILL.md` holds CRLF, it exits 0 and prints its `ok` line.
- **AC2** — When the rendered Skill differs from the conf in CONTENT, `--check` still exits 1 and
  still names the drift. Proven by mutating one line of `SKILL.md` in a scratch copy, not by
  reasoning about the code.
- **AC3** — When `bash tools/run-gates.sh` runs in a fresh worktree created by `git worktree add`,
  the leg named `memory-recall skill wiring` is green.
- **AC4** — When the arm in S3 runs against a build with S1 reverted, it fails, and its message names
  `.claude/skills/memory-recall/SKILL.md`.
- **AC5** — When `bash tools/check-wiring.sh --check` runs in that same fresh worktree, its eol arm
  still reports the CRLF paths. This unit does not silence that report; it removes the red leg the
  report warns about.

## 7. Gates

- `bash tools/run-gates.sh` — the whole bar, and specifically the leg `memory-recall skill wiring`
  which is the one this unit turns green.
- `python tools/memory-recall/selftest.py` — must stay green whether or not F1 puts S3 inside it.
- `python tools/codebase-map/test_codebase_map.py` — reds if F1's resolution adds a gate leg that no
  dossier claims. Named here because the cost is invisible until the bar runs.
- `python tools/drift-audit/drift_report.py --check` — its hand-kept leg-count signal sits at a pin
  with zero slack, so an added leg reds it.

## 8. Open questions

- **F1 — where does S3's arm live?** Two options. **(a) Fold it into
  `tools/memory-recall/selftest.py`**, which is already a leg, so no new leg is created and none of
  the four leg-addition gates in §7 move. It costs a `subprocess` call to bash from a python selftest
  that today exercises only the retrieval engine. **(b) A new
  `tools/memory-recall/adopt-memory-recall.test.sh`**, matching how `tools/unattended/` tests its own
  adopter, at the cost of a new gate leg plus the dossier claim, the map re-render, the manifest
  re-stamp and the drift-signal pin it drags with it. **Recommendation: (a).** The arm is four lines
  and the shape it proves is not adopter-specific; option (b) spends four gate movements on file
  placement. Revisit if a second adopter-level arm appears, at which point a sibling test file is
  earning its keep.

## 9. Revision log

- rev-1 · 2026-08-16 · initial draft, from the reproduction recorded under this build's `build/`.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py` returned no seam for this behaviour, which is correct:
the thing being reused is not a symbol but a two-line idiom. The seam is
`tools/unattended/adopt-unattended.sh:122`, `diff -q <(tr -d '\r' < "$SKILL_OUT") "$TMP"`, with its
rule stated at that file's lines 9 to 12. `tools/drift-audit/adopt-drift-audit.sh` carries the same
shape. This unit makes the third copy of a three-copy idiom agree with the other two rather than
introducing anything. No new abstraction is warranted at three call sites in three separately
copy-installed kits — a shared helper cannot be shared across kits that ship independently, which is
the same constraint that makes `resolve_python` an inline byte-identical block rather than an import.
