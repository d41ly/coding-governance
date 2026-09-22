# TOOL-dFoldedVerdict-5 — section 7 becomes its own carrier, and a text-mode read nearly took a gate with it

**Serves:** journal TOOL-dFoldedVerdict-5

*Node `d`, 2026-09-01, owner-present build under `memory/guides/BUILD-METHOD.md`.*

## What binds now

`memory/guides/UNATTENDED-PROTOCOL.md` went from **61440 bytes — exactly `GUIDE_CAP_BYTES`, zero
headroom — to 54231**. The eighteen verb entries live in `memory/guides/UNATTENDED-VERBS.md`, shipped
from `tools/unattended/VERBS.template.md`, and check 10 now iterates TWO byte-compared pairs instead
of one. Check 26's contract arm reads the new carrier ALONE, with its own named refusal when it is
absent, because accepting a hit in either file would pass a half-completed move.

The protocol also gained one sentence it did not have: a `<key>-source:` line is now ADMITTED beside
a fact no verb could write. That is S13, and it is the owner's ruling of 2026-09-01 on
`TOOL-dFoldedVerdict-3` Q2 — four landed records already carry that form while the contract said the
authored half holds the declared facts "and nothing else". It landed here rather than in
`TOOL-dFoldedVerdict-6` for a reason about the diff: at order 1 the permission exists three units
before `TOOL-dFoldedVerdict-3` writes rows relying on it, and a one-sentence addition stays separable
inside a diff that is otherwise a move — inside unit 6's document-wide compression a reader could not
tell an addition from a reword.

## The `--review` bullet moved FALSE, on purpose

Rev-1 through rev-3 of this spec had this unit acting as a backstop that observed a CORRECTED
sentence, because they were written when `TOOL-dFoldedVerdict-1` was sequenced first. The rev-3
reorder inverted that and rev-4 followed it. This unit is order 1, so the pre-image still carries
"at the exit every blocker still standing is promoted to a unit rather than parked", and it is copied
UNCHANGED. AC13 asserts that rather than the opposite.

The verbatim property is the whole verification story here — AC2, AC3 and AC14 all grade this move by
byte-identity, and an amendment made during the move is the single edit that would make a pure move
unverifiable. The false sentence does not survive the build: unit 1 at order 2 corrects it inside the
carrier this unit created, and its AC17 grades it there.

## What went wrong, and it was mine

**A Python text-mode read silently destroyed four embedded CR bytes in `check-unattended.sh`.**
`io.open(p, encoding="utf-8")` applies universal newlines, which rewrites every LONE `\r` to `\n`.
This checker embeds literal CRs inside awk programs — `sub(/<CR>$/,"")` — and my first patch script
read in text mode and wrote back with `newline="\n"`.

The symptom was maximally misleading: check 18 failed reporting that `SKILL.template.md` "names no
`--preflight` invocation", against a file that names it twice. The awk had become an UNTERMINATED
REGEX, died on stderr, and returned an empty locator — so the check blamed the data it could not
read. `git diff` shows nothing unusual; `cat -A` shows everything. Reverted and re-applied with
`newline=""` on both sides plus an assertion that the embedded-CR count is unchanged, which now sits
in the patch script and in `memory/gotchas`-adjacent session memory.

**Check 10's failure message could not be armed.** The first cut parameterised it — one
`_c10_pair name ship livedoc` function emitting `"the shipped $1 ... drifted"`. `check-arms.py`
derives a branch's signature as the longest LITERAL run between interpolations and its `INTERP_RE`
does not recognise a positional `$1`, so the whole message became the signature and no test assertion
could ever name it. The COMPARISON is still shared (`_c10_cmp`, returning 0/1/2); the MESSAGES went
back to literals, one pair each. That also left the protocol pair's two sentences byte-identical, so
the two arms already covering them stayed armed instead of silently going dark.

## The dossier was at its cap too

`memory/map/features/unattended.md` was at **20480 bytes exactly**, against `DOSSIER_CAP_BYTES` of
20480. Claiming the new `guides` key cost 61 bytes and put it over — the second carrier in this build
found sitting precisely on its declared ceiling, which is the pattern rather than the coincidence.
Paid for in scope, not by raising a declaration: the two explicit guides globs collapsed to
`memory/guides/UNATTENDED-*.md`, and one clause in the Gaps preamble that restated the sentence
before it was cut. 20458 bytes, 22 of headroom. No claim was dropped, and the map gate is green over
the wildcard.

## Evidence

**Evidences:** TOOL-dFoldedVerdict-5

- **AC1** — `wc -lc` reports `96  8502` for BOTH halves of the new pair, under 61440 bytes and 750
  lines.
- **AC2** — `diff tools/unattended/VERBS.template.md memory/guides/UNATTENDED-VERBS.md` reports no
  difference.
- **AC3** — 18 verb bullets in `memory/guides/UNATTENDED-VERBS.md`, against 18 in the pre-image
  section 7 measured with the same expression. The slice was taken programmatically between `## 7. The verbs` and
  `## 8. What a project declares` and re-emitted unchanged; the script ASSERTED the count was 18 and
  that the body carried no `tools/` or `memory/` path before writing anything.
- **AC4 — `bash tools/unattended/check-unattended.sh` IS MET EXCEPT FOR ONE INHERITED RED**, and
  that is stated rather than rounded off. On a clean tree it reports exactly ONE failure:
  `check 2 — review loops that ran past the ceiling, stalled without recording it, or exited without
  promoting`. That red exists on `origin/main` for `memory/builds/dMispairedQuote/RUN.md`, predates
  this unit, and is what `TOOL-dFoldedVerdict-3` at order 4 is scoped to clear; the build lands once,
  after it. Check 26 and check 10 — the two this unit changed — are GREEN, over BOTH pairs. The
  criterion as written says "exits 0", and it does not exit 0 yet; claiming otherwise would be the
  green-by-absence shape this build is about.
- **AC5** — the failing cases OBSERVED in both directions against `VERBS.template.md`, plus two the
  criterion did not ask for.
  With the verb bullets deleted from `tools/unattended/VERBS.template.md`: check 26 names a verb
  (`--abort`, `--attest`, …) against the verb carrier, and check 10 reports the pair DRIFTED. With
  that file deleted outright: check 10 reports `one half of the verb-carrier pair is missing, and a
  parity check with one file is a check that cannot fail`, and check 26 reports `the verb carrier is
  absent, so the arm that joins every declared verb to the contract cannot run and would otherwise
  skip in silence`. Restored, the tree returns to the single inherited check-2 red and
  `git diff --stat` against the index is empty. **All FOUR new-or-reworded `fail` branches were seen
  RED**, which is a stronger statement than the criterion asked for: the branches are proven armed
  against the real tree even though the suite arms naming them have not been run.
- **AC6** — `bash tools/unattended/adopt-unattended.sh --check`, observed in BOTH directions. With
  a line appended to the installed copy it reports `memory/guides/UNATTENDED-VERBS.md has
  drifted from the shipped verb carrier; re-run tools/unattended/adopt-unattended.sh`. Restored, it
  reports `unattended: in sync`.
- **AC7** — `bash tools/check-kit-versions.sh` exits 0 with the new template carrying
  `gov:kit unattended@1.14`. It asserts AGREEMENT and never movement; this unit does not bump the
  version and this line is not evidence that anything did.
- **AC8** — `bash tools/memory-tree/check-memory-hygiene.sh` reports no FAILED check. The protocol is
  54231 bytes, strictly below 61440 and strictly below its own pre-image of 61440, which was
  re-measured rather than assumed. At order 1 this unit runs before every sibling that touches the
  file, so the pre-image equalling BASE is the OUTCOME of the measurement and not its premise.
- **AC9** — `awk '/^## 8[.] /{f=1;next} f&&/^## /{f=0} f'` still yields the conf-key table at 29
  rows, and `## 7. The verbs` remains a heading of its own with sections 8 through 12 unrenumbered.
- **AC10** — `python3 tools/codebase-map/test_codebase_map.py` exits 0, all five tests ok. Observed
  RED first: `UNCLAIMED ... {'guides': ['UNATTENDED-VERBS.md']}`.
- **AC11** — `python tools/memory-tree/check-arms.py --check` exits 0, and `--report` shows this
  file at **172 branches / 164 armed**, both risen from the BASE 169 / 161. The +3 is exactly the
  three new `fail` branches; the fourth finding was a REWORD, not an addition.
- **AC12** — neither corrected row in `memory/backlog/TOOL.md` still asserts what was measured
  false. A `grep -c` for the eight-verb claim and one for the cap mis-attribution both return 0. Both rows were rewritten WHOLE. A first pass corrected only each row's prefix and quoted
  the original below it, which leaves a second copy of the false claim in the same file — the exact
  misread S10 exists to prevent.
- **AC13** — the `--review` bullet extracted from the pre-image section 7 and from BOTH halves of the
  new pair is byte-identical across all three, 628 bytes, and each still contains
  `promoted to a unit rather than parked`. This is the INVERSE of what rev-3 asserted, per S11.
- **AC13a** — S13's sentence is present in both halves of the `UNATTENDED-PROTOCOL` pair, and
  check 10 reports no failure over that pair. The CONTENT reading is a reader's and is written as one: no grep
  distinguishes a clause that sanctions the source-suffixed form from one that merely mentions it.
- **AC14** — `grep -cE '^- .--[a-z-]+. — '` reports **0** over each half of the PROTOCOL pair and
  **18** over each half of the NEW pair. This is the criterion that separates a completed move from a
  HALF-MOVE, and neither existing leg can: check 10 compares copies to each other and passes when
  neither was emptied.
- **AC15** — `python tools/govkit/govkit.py selfcheck` exits 0 with S7's `[[files]]` destination
  present and unique.
- **AC16** — `grep -c 'UNATTENDED-VERBS'` returns 1 for both `tools/unattended/SKILL.template.md` and
  the rendered `.claude/skills/unattended/SKILL.md`, and the adopter then reports `unattended: in
  sync` over the regenerated render.

## What this pass did NOT do

**The four new test arms have never been executed, and the distinction matters.** The standing owner
instruction is that this kit's self-tests are not run by this session, and AC11 named the
compensating check for exactly that reason. So the ARMS are written and statically counted by
`check-arms.py`, and no fixture has driven one.

What HAS been observed is the thing the arms exist to observe: every one of the four
new-or-reworded `fail` branches was driven RED directly against this tree under AC5, each printing
its own message. The branch is proven; the arm that would keep it proven in CI is not. A future
session running `bash tools/unattended/check-unattended.test.sh` is what closes the gap, and until
then these four arms carry the weaker guarantee — worth knowing before trusting a green suite.

The three legs that DO run — `unattended kit gate`, `unattended skill wiring`, `pass-order history` —
cover the checker itself.

It did not correct the `--review` bullet: that is `TOOL-dFoldedVerdict-1`'s at order 2, by S11.

It did not bump `KIT_UNATTENDED_VERSION`. The owner ruled the bump moves ONCE, on
`TOOL-dFoldedVerdict-6`, the build's last landing unit.

It did not cite `UNATTENDED-VERBS.md` from `AGENTS.md`. F3 resolved against it: editing the charter
is a governance-carrier change and M3's veto 2 reserves that for the owner.

`memory/project/unarmed-branches.txt` was NOT touched and did not need to be. It pins rows by
`(gate, check, ordinal)`, and the check-26 refusal inserted here became ordinal 2 — which renumbers
every later branch of check 26. That file carries rows for checks 2 and 16 of this gate and none for
10 or 26, verified by reading it, so no pinned row moved. Had one existed below the insertion it
would have silently repointed at a different branch.
