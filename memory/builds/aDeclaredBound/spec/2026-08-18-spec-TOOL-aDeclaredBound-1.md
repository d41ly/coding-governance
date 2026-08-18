# TOOL-aDeclaredBound-1 — check 7's entry budget becomes a declaration

**Status:** OPEN · rev-2 · 2026-08-18 · node a · Tier-2 · base 497d25d0 · streams tooling

## 1. Goal

Check 7 caps how long one entry line in an index file may be. The number lives in three places
inside one script — twice in the awk that applies it and once in the failure message that reports
it. Move it to `.memory-tree.conf` at its present values, on the pattern `TOOL-aLoosenedCeiling-2`
established for check 6's size caps sixty lines away.

## 2. Scope (IN)

- **S1** — two keys, `ENTRY_CAP_CHARS` and `BUILD_README_ENTRY_CAP_CHARS`, defaulted to 300 and 350,
  declared in the same block as check 6's EIGHT existing cap keys so one conf source overrides all
  ten. Eight, not six: `DOSSIER_CAP_BYTES` and `DOSSIER_CAP_LINES` landed after the previous build,
  with `TOOL-aRelaxedShard-1`, and a spec that counts them wrong writes a wrong loop.
- **S2** — the awk receives both through `-v` bindings and holds no literal.
- **S3** — both keys join the EXISTING validation loop, and the loop's ZERO arm widens to reach
  them. As it stands that arm selects on `*_BYTES`, so a char key matches no arm: a declared 0
  would validate clean and then red every measured line, which is the silent-misconfiguration
  outcome the loop exists to stop. The case pattern gains the char keys with their own message.
- **S3b** — the abort BANNER changes, because it names check 6 and will now also speak for check 7.
  That banner is an `echo` rather than a `fail` branch, so `check-arms.py` cannot notice a stale
  arm for it; the hand-written arm that asserts its text moves in the SAME commit or the assertion
  silently stops matching.
- **S4** — the failure message stops carrying the number. It currently reads `index entry lines over
  300 chars`, which is a THIRD copy of the value and is also the check's armed signature. The
  message becomes cap-free; the per-row detail line already prints `(N chars > CAP)` and keeps doing
  so, which is where a reader learns which cap applied.
- **S5** — the arm that names that signature moves in the SAME commit. It is a literal-text arm and
  the harness meta-gate keys on it, so a reworded message with an unmoved arm is a check that reds
  nothing and reports armed.
- **S6** — arms in BOTH directions per class over one fixture, on unit 2's pattern from the previous
  build: a row silent at a loose declared budget and named at a tight one, for the row-document
  class and the build-README class, plus an arm that the SHIPPED defaults still apply when nothing
  is declared.
- **S7** — the shipped `.memory-tree.conf.example` declares both keys with their values, and
  `HYGIENE.template.md` describes check 7's budget as a declaration. `memory/HYGIENE.md` moves only
  as the render.
- **S8** — `memory/project/curation-debt.txt`'s header, which restates `25600 B / 350 chars` as
  prose, stops naming the entry figure.
- **S9** — the kit-version ordering is stated HERE, not only in the build README. `check-verdict-epoch.sh` is TOPOLOGICAL: the newest behaviour-bearing commit across the engine and its delegates must be an ancestor of, or equal to, the commit that changes
  `KIT_MEMORY_TREE_VERSION`. Units 1 and 2 both move that engine, so the LATER of the two carries the single bump and the earlier carries none. `TOOL-aLoosenedCeiling-1` folded
  exactly this finding at rev-3 after leaving the ordering in a README where neither spec repeated it.


## 3. Non-goals (OUT)

- No default changes. 300 and 350 are what every adopter who declares nothing keeps.
- Check 6's eight caps are not re-opened. Six landed with `TOOL-aLoosenedCeiling-2` and two with
  `TOOL-aRelaxedShard-1`; this unit extends their shared validation loop and changes none of them.
- `ex7` is untouched: the guides, `RUN.md` and map-dossier exemptions select which files are graded,
  not how long a line may be, and this unit does not make the EXEMPTION list adjustable.
- No new class. The two tiers check 7 already has are the two tiers it keeps.

## 4. Design

### Data model

| key | default | class |
|---|---|---|
| `ENTRY_CAP_CHARS` | 300 | every graded index entry line |
| `BUILD_README_ENTRY_CAP_CHARS` | 350 | a line in a build folder's own README |

### Inventory

Three sites hold the number today: the awk's `cap` assignment, its build-README override, and the
`fail 7` message. The message is the interesting one, because `TOOL-aLoosenedCeiling-2` explicitly
declined to reword check 6's message for exactly the reason that applies here — it is armed on its
full literal text. The difference is that check 6's message never carried a cap value, so leaving it
alone cost nothing; check 7's does, so leaving it alone would ship a message that lies to any
adopter who declares a different budget. The rule is the same in both cases: the message and its arm
move together or not at all.

### Migration

An adopter declaring neither key sees no change. The failure message changes text for everyone,
which is why S5 is a scope item rather than an implementation note.

### Files touched (estimate)

- `tools/memory-tree/check-memory-hygiene.sh` — two defaults, two `-v` bindings, the validation
  loop's key list, the message.
- `tools/memory-tree/check-memory-hygiene.test.sh` — S5's arm and S6's arms, and its floor.
- `tools/memory-tree/.memory-tree.conf.example` and `HYGIENE.template.md`.
- `memory/project/curation-debt.txt` — the header sentence only; the registry rows are untouched.
- The kit-version carriers, shared with unit 2.

### Alternatives rejected

- **Leave the message as-is and let it state 300 forever.** Rejected: it is the only line a reader
  sees when the check fires, and an adopter at a different budget would be told their file broke a
  rule that is not theirs.
- **A third key for the message.** Rejected as absurd on its face, and recorded because a first
  draft of this design reached for it before noticing the per-row line already carries the value.

## 5. Production-readiness checklist

- security — N/A. Two integers reach an awk `-v` binding, and the validation that admits them is the
  same one that already guards six neighbouring keys.
- perf / scale — N/A. Two more regex matches at startup.
- a11y · i18n — N/A. A gate that prints text.
- error / empty / loading states — covered by S3's reuse of the existing abort.
- observability — the per-row detail line names the cap that was applied, so a surprised reader can
  tell a declared budget from a shipped one without reading the conf.
- risks — the reachable failure is a reworded message with a stale arm, which is S5 and is the
  reason it is a scope item.
- testing + left-shift gates — S6's both-directions arms; S5's arm move.
- migration / rollback — delete the keys to restore the defaults.
- user docs — S7 and S8.

## 6. Acceptance criteria

- **AC1** — When a fixture declares `ENTRY_CAP_CHARS` below a fixture line's length, `bash
  tools/memory-tree/check-memory-hygiene.test.sh` observes check 7 naming that file; when it
  declares one above, the same fixture is silent.
- **AC2** — When nothing is declared, `bash tools/memory-tree/check-memory-hygiene.test.sh`
  observes a 320-character fixture line named in a row document and silent in a build README, which
  is the 300/350 split still applying from the shipped defaults.
- **AC3** — When a fixture declares a non-numeric or zero entry budget, `bash
  tools/memory-tree/check-memory-hygiene.test.sh` observes the abort's MESSAGE naming the offending
  key, not merely exit 2 — the status alone cannot tell a widened zero arm from an unwidened one,
  since a non-numeric value already aborts today.
- **AC4** — When `python tools/memory-tree/check-arms.py` runs, check 7's branch is armed against
  the message's NEW text, and no branch of the engine has become unarmed.
- **AC5** — When `bash tools/memory-tree/kit-dogfood-parity.test.sh` runs, the edited template and
  the rendered `memory/HYGIENE.md` agree.

## 7. Gates

`bash tools/memory-tree/check-memory-hygiene.sh` · `bash
tools/memory-tree/check-memory-hygiene.test.sh` · `python tools/memory-tree/check-arms.py` · `bash
tools/memory-tree/check-verdict-epoch.sh` · `bash tools/check-kit-versions.sh` · `bash
tools/memory-tree/kit-dogfood-parity.test.sh` · `bash tools/check-testsuite-counts.sh` · and
`GATE_FULL=1 bash tools/run-gates.sh` at the push boundary.

## 8. Open questions

none.

## 9. Revision log

- rev-1 · 2026-08-18 · initial draft.
- rev-2 · 2026-08-18 · folded spec-audit round 1. The key count was six and is eight, so this unit
  makes ten. The zero arm selects on `*_BYTES` and would not have reached either char key, which
  made AC3 pass over an unbuilt guard. The abort banner names check 6 and its arm is hand-written
  rather than meta-gated, so S3b now moves it. S9 states the kit-version ordering that lived only
  in the README, which is the finding the previous build folded at ITS rev-3.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "read a per-adopter numeric limit from a declaration
instead of a source constant"` returns `read_text` and `read` as the top seams, which are file
readers and not the seam this unit needs. The seam it actually extends is the one the previous build
built: the block of shell defaults declared immediately above the conf source in
`check-memory-hygiene.sh`, and the single validation loop beneath it. This unit adds two keys to
both rather than introducing a mechanism, which is why its design section is short.

The recall probe for the set is recorded in `TOOL-aDeclaredBound-4` §10, since that unit carries the
question the corpus actually has prior art about. The binding record for THIS unit is
`TOOL-aLoosenedCeiling-2`, whose S9 established that a gate message carrying a value is an armed
signature and moves only together with its arm — the rule this unit applies in the opposite
direction, because here the message must change.
