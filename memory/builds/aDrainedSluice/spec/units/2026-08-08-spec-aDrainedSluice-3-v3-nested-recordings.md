# TOOL-aDrainedSluice-3 — V3: check 5 governs a recording at any depth

**Status:** INPROGRESS · rev-2 · 2026-08-08 · node a · Tier-2 · base 76fcd09b · streams tooling

## 1. Goal

Hygiene check 5 selects `builds/<slug>/(prompts|spec|build|reviews)/<file>.md` — direct children
only. A file one level deeper is ungoverned: it can carry any name at all. Check 12 scans nested
specs, but only those already matching the dated NAME, so a free-named nested file is invisible to
both. Close the gap.

## 2. Scope (IN)

- **S1** — check 5's selector becomes any `.md` at ANY depth under the four subfolders. The kind is
  taken from the SUBFOLDER, which is the first segment after the build slug, not from the file's
  immediate parent — `spec/units/x.md` is a spec, and its parent directory name is not a kind.
- **S1b** — check 5's NAME grammar gains the trailing unit segment check 12's selector ALREADY
  carries: `…-<seq>(-[a-z0-9][a-z0-9-]*)?\.md`. Without it the widened selector is a red merge bar,
  not a ratchet. MEASURED, twice and independently: 14 of 14 tracked nested spec files fail the
  drafted grammar, and 0 of 14 fail once the tail is appended. The draft measured the population's
  SIZE and called it conformance.
- **S1c** — the tail is single-sourced. It is hoisted to one variable beside `FAM_ALT` and
  `DISC_ALT`, and BOTH check 5 and check 12's selector interpolate it, so the next widening cannot
  land in one place only. Two hand-copied EREs for one recording-name grammar is the
  two-answers-to-one-question class, and this change would have made the divergence load-bearing
  rather than latent.
- **S2** — the existing grandfather stays the whole exemption story: a nested file that must keep a
  historical name goes in `legacy-files.txt`, exactly as a direct child does. Nothing needs
  grandfathering once S1b lands, and the ratchet arms clean.
- **S3** — the failure message says the DEPTH is not the problem, on a CONTINUATION line. The first
  line of `fail 5`'s message IS its `check-arms` signature and its arm sits exactly at the armed
  floor with no slack, so rewording that line reds two gate legs for a cosmetic change.
- **S4** — a non-markdown file keeps its existing treatment, and that treatment is NOTHING. Measured
  on a scratch repo: check 4 inspects only the first segment under the build folder and skips the four
  subfolder names, so `spec/notes.txt`, `spec/units/whatever.txt` and `spec/units/free-named.md`
  produce zero findings from checks 3, 4 and 5. `HYGIENE.md` check 4's "non-md only in `build/`"
  describes a rule nothing enforces. This unit closes the free-NAME gap and files the free-KIND gap
  as its own backlog row rather than citing a guard that does not exist.
- **S5** — the self-test gains three fixtures, and two of them are made to DISTINGUISH rather than to
  be satisfied by absence. The legacy arm is TWO-STATE: listed in `legacy-files.txt` it is silent,
  and with that line removed the same file reds — silence alone proves only that nothing selected it.
  The red arm is attributed INSIDE check 5's own output slice, because check 5 prints a bare path and
  checks 2, 9 and 12 all print paths from under `spec/` too. The conforming-nested arm is load-bearing
  for AC4 (kind-from-subfolder) and says so, so it is not deleted later as redundant.

## 3. Non-goals (OUT)

- Constraining the sub-directory NAME. `spec/units/` is a useful grouping and a name gate over it is
  ceremony with no failure behind it.
- Widening check 12's population. It already scans nested specs by dated name; once check 5 forces
  the dated name, the two populations converge on their own.
- Touching check 4's non-markdown rule.

## 4. Design

### Data model

```
before : ^<M>/builds/[^/]+/(prompts|spec|build|reviews)/[^/]+\.md$
after  : ^<M>/builds/[^/]+/(prompts|spec|build|reviews)/(.+/)?[^/]+\.md$
kind   : the FIRST segment after the slug, not the immediate parent
```

### Inventory

| Concern | Change |
|---|---|
| check 5 selector | one segment becomes any depth |
| kind derivation | from the subfolder, not `dirname` |
| exemption | unchanged — `legacy-files.txt` |
| self-test | three new fixtures |

### Migration

None required once the name grammar admits the unit tail. Measured: 14 nested files, all conforming
under the corrected grammar, none under the drafted one.

### Rollout

One commit: the selector, the kind derivation, the message, the fixtures.

### Files touched (estimate)

`tools/memory-tree/check-memory-hygiene.sh` and its test, `memory/HYGIENE.md` (then re-render
  `tools/memory-tree/HYGIENE.template.md`), and `check-memory-hygiene.test.sh`'s check-5 arm string
  if the first message line moves — which S3 avoids.

### Alternatives rejected

- **Ban nesting outright.** Rejected: `spec/units/` is how a multi-unit build stays readable, and
  this build and the last both use it.
- **Let check 12 cover it.** Rejected: check 12's population is files that already match the dated
  name, so a free-named file is outside it by construction — the exact shape of this gap.

## 5. Production-readiness checklist

- security — N/A.
- perf / scale — the selector matches more paths; the loop is already per-file and fork-free.
- a11y — N/A. i18n — N/A.
- error / empty / loading states — the population guard already covers an empty selection.
- observability — the message names the file and the expected pattern.
- risks — a widened selector could red a landed file. Measured: it does not, and the measurement is
  recorded rather than assumed.
- testing + left-shift gates — three fixtures, red and green.
- migration / rollback — one commit.
- user docs — `memory/HYGIENE.md` check 5's wording, then
  `bash tools/memory-tree/kit-dogfood-parity.test.sh --render` to regenerate the shipped copy. The
  render direction is LIVE to SHIPPED, so editing the template alone reds the parity leg AND the
  remedy it prints overwrites the edit.

## 6. Acceptance criteria

- **AC1** — When a free-named `.md` is added under `spec/<sub>/`, check 5 fails naming it.
- **AC2** — When a conforming dated recording is added under `spec/<sub>/`, check 5 is silent.
- **AC3** — When a nested free-named file is listed in `legacy-files.txt`, check 5 is silent; when
  that line is removed, the same file reds. Both states are asserted, because silence alone is also
  what an unwidened selector produces.
- **AC3b** — When the red arm asserts, it asserts inside check 5's own output block, so a path
  printed by check 2, 9 or 12 cannot satisfy it.
- **AC4** — When the kind is derived, it comes from the subfolder: a file under `spec/units/` is
  judged as a spec, not as a `units`.
- **AC5** — When the gate runs over this repo's tree, it stays green — 14 of 14 nested files conform
  under the corrected grammar, measured before the edit.
- **AC5b** — When check 5 and check 12 are read, the recording-name tail appears ONCE, in a shared
  variable both interpolate.
- **AC6** — When `check-memory-hygiene.test.sh` runs, its pass line prints last.

## 7. Gates

`bash tools/run-gates.sh`; the `memory hygiene` and `memory-hygiene self-test` legs carry this unit.

## 8. Open questions

none — the fork below is RESOLVED (owner-ratified 2026-08-08); kept for the record.

- **Fork — the grandfather story the backlog row asked for.** Options: a new nested-specific
  exemption list, or the existing one. RESOLVED (owner, 2026-08-08): the existing `legacy-files.txt`.
  It is already a path list with a stale-entry guard, the nested population is currently empty of
  violations, and a second exemption list for one selector is the two-answers class.

## 9. Revision log

- rev-1 · 2026-08-08 · initial draft.
- rev-2 · 2026-08-08 · folded review 1: M1 adds S1b, the name-grammar tail without which the unit is
  a red merge bar on 14 conforming files; M2 adds S1c, single-sourcing that tail across checks 5 and
  12; M9 restates S4 with the measurement that check 4 governs nothing inside the four subfolders;
  M10 makes the legacy arm two-state and attributes the red arm to check 5's own block; M11 moves the
  message reword to a continuation line so the arm and the armed floor survive; M12 corrects the doc
  edit direction.

## 10. Reuse audit

One regex and one variable change inside a check that already exists, plus three fixtures in a test
harness that already exists. The exemption reuses `legacy-files.txt` and its stale-entry guard. No
new file, no new conf key, no new gate leg.
