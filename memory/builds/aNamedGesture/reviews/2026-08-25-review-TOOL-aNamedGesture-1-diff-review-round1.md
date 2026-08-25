**Serves:** diff-review TOOL-aNamedGesture-1

# Diff review round 1 — the authorizing parameter, at the integration boundary

*Range `381008a1a58154611594502ed8208fc8ad0b1b74...HEAD` (HEAD `d7f66970`), reviewed once at the
integration boundary per §8 rather than per increment. **ROUND 1.** Node a, 2026-08-25.*

**Review shape.** Raw 9, confirmed 4, refuted 5, unverified 0, **precision 0.44**. Below the
protocol's 0.5 lever, and the diagnosis is target richness rather than priming: the diff is 26 files
of which 17 are records, and the code it adds is one conf key, one `case`-derived default and two
value guards that the spec had already been through four revisions of. Heavy lensing over an
already-hardened surface manufactures refuted noise — §8 says review that light or skip it, and the
yield here says the same. Two of the four survivors are the SAME defect found by two lenses, so the
distinct yield is **3 defects from 9 reports**.

## Verdict: CLEAN WITH FIXES

No blocker. No high. Three distinct low findings, all fixable inside this build without touching the
mechanism. The security model holds: the parameter is the authorization GESTURE, the pushed build
folder at the declared anchor remains the authorization, and protocol §9 is untouched by this diff.

| Severity | Count | Distinct sites |
|---|---|---|
| BLOCKER | 0 | — |
| HIGH | 0 | — |
| LOW | 4 reports / 3 defects | `adopt-unattended.sh`, `.memory-tree.conf`, `map/features/unattended.md` |

---

## LOW

### L1 — the surviving-placeholder refusal the `{{AUTH_PARAM}}`-last ordering credits does not exist on the WRITE path

**`tools/unattended/adopt-unattended.sh:227`** (comment at `:225-226`; the arm it names is at `:247`,
the write path at `:293-297`).

The ordering comment is correct about the mechanism and wrong about the backstop. `render()` is shared
by both modes, but the `grep -qE '\{\{[A-Z_]+\}\}'` refusal lives inside `if [ "$MODE" = "--check" ]`
at `:231`. Reproduced in a scratch repo: with `AUTH_PARAM='--{{LANDER}}'` — hyphen-led, no whitespace,
no pipe, no backtick, so both new guards at `:166` and `:173` pass — the write path prints
`unattended: rendered …` and exits 0 over a Skill whose routing row and prompt fence read
`--{{LANDER}}`.

The asymmetry is not deliberate. The write path already carries its own refusals (empty render at
`:296`, the malformed-`AUTH_PARAM` cases, the whitespace kit path), so "render blindly, check later"
is not this script's design anywhere else.

Second half of the same defect: when `--check` eventually does red, it prints `…declares no value for
it`. `AUTH_PARAM` is the first key whose DECLARED value can itself produce a surviving placeholder, so
a message that was true for every previous cause is now false for this one and sends the reader
hunting an undeclared key that is plainly declared.

**Fix.** Hoist the surviving-placeholder refusal out of the `--check` branch into a shared post-render
assertion beside the existing `[ -s "$TMPW" ]` emptiness refusal, so the write path refuses instead of
reporting success. Reword the message to cover both causes: `…declares no value for it, or a declared
value carries a placeholder shape`. Cheaper alternative if the ordering is to stay the only defence:
add `*'{{'*` to the character guard at `:173` so the value can never inject one — but that guards
`AUTH_PARAM` alone and leaves the write path fail-open for the next key.

**Left-shift.** A fixture arm in `tools/unattended/adopt-unattended.test.sh` that declares
`AUTH_PARAM='--{{LANDER}}'` and asserts the WRITE invocation exits non-zero — the RED case observed
before the arm lands, per §7. Gate the CLASS, not this key: the assertion is "no render, in either
mode, is installed carrying `{{[A-Z_]+}}`", which is one predicate covering every present and future
placeholder.

### L2 — the recorded read-path measurement does not reproduce, so the declared 256 B margin is really 253

**`.memory-tree.conf:354`** (`MEASURED 138876 B on this tree`), ceiling at `:363`, margin doctrine at
`:346` and `:360`. Reported twice, by two lenses, as ids 2 and 6 — one defect.

Summing `git cat-file -s` over the six read-path blobs at HEAD gives **138879**: DECISIONS 20970 +
LIVE 2040 + BUILD-METHOD 24385 + REVIEW-PROTOCOL 15614 + SESSION-KICKOFF 25433 + UNATTENDED-PROTOCOL
50437. `python tools/memory-tree/corpus_ids.py --report` prints the same figure, so this is not a
CRLF or worktree artifact. `139132 - 138879 = 253`, against the `DECLARED 256` the same block asserts
three lines above.

The figure never matched its own commit — `git log -S138876 -- .memory-tree.conf` puts it in
`d7f66970` itself, and the prior branch tips sum to 137777 and 137894, so it was not a
correct-when-made carry-forward either. The measurement was taken before the same commit's final
read-path edits.

The consequence is not cosmetic. AC13 of the spec requires "the margin is the declared 256 B", and
`memory/builds/aNamedGesture/build/2026-08-25-build-TOOL-aNamedGesture-1-acceptance-ledger.md:48-49`
grades it met with "measures 138876 B … a margin of exactly the declared 256 B". That is a false pass
on a stated acceptance criterion, and hygiene check 16 stays green because it compares the live figure
against the ceiling alone and never against the recorded derivation.

Strongest refutation considered and rejected: `memory/guides/SESSION-KICKOFF.md:311-313` tells the
next author to measure with `corpus_ids.py --report` and never estimate, so the stale number cannot
propagate arithmetically, and the error direction yields a loud early red rather than a silent pass.
It is still a self-contradicting recorded measurement inside the file whose entire doctrine is
measured-over-computed — precisely the "number typed beside the thing it counts" class §7 bans.

**Fix.** Re-measure at the tip and set `READ_PATH_CEILING="139135"` (138879 + 256), correcting the
`MEASURED` figure in the comment and the AC13 rows in both the spec and the acceptance ledger to
138879. If the 3 B are deliberately conceded, say so and record the margin as 253 rather than
restating 256.

**Left-shift.** The lazy gate is a deletion: drop the `MEASURED <n> B` literal from the comment
entirely and point at `python tools/memory-tree/corpus_ids.py --report`, which owns the number and
cannot go stale. Where a recorded pair must survive for audit, the mechanical form is a check that
recomputes `READ_PATH_CEILING - live` and reds when it does not equal the declared margin at the
commit that moves the ceiling. The wider class is the acceptance-witness rule: **an AC whose witness
is a NUMBER carries the command that reproduces it**, so the ledger row cannot be graded by
re-typing the figure it is grading.

### L3 — the dossier says the driver and the leg read `AUTH_PARAM`; neither does

**`memory/map/features/unattended.md:76`** (the inserted clause is at `:74-76`; the file contradicts
itself at `:163`).

The diff inserted "and the token that authorizes a prompt-mode run" into the sentence whose very next
clause is "The driver and the leg READ them". `grep -c AUTH_PARAM` returns 0 for both
`tools/unattended/unattended.sh` and `tools/unattended/check-unattended.sh`, and 7 for
`tools/unattended/adopt-unattended.sh`, the only value consumer. The driver's conf pre-set block at
`unattended.sh:212-214` does not name the key and the script never references it.

The weak defence — check 22 in `check-unattended.sh:1173` greps `^[A-Z_]+=` out of `.unattended.conf`
and joins it against the protocol's §8 table, so the leg touches the key NAME generically — does not
save the sentence: it never reads the VALUE, and the driver clause is plainly false. A reader greps
the two named scripts, finds nothing, and cannot tell whether the key is dead plumbing or the dossier
describes another revision. The same file already states the truth 80 lines later, so the dossier
disagrees with itself.

**Fix.** Split the sentence so the reader is routed to the right file: keep the driver/leg list as it
was, and add that the ADOPTER reads `AUTH_PARAM`, which is rendered into the Skill and read at run
time by nobody — which is also the security-model point protocol §8 already makes.

**Left-shift.** No cheap mechanical gate fits a prose claim about WHO reads a key, and inventing one
for a single sentence is the over-build this project keeps refusing. Take the documented-check route
§7 sanctions for an ungateable class and add it to the gotchas checklist: **a dossier clause naming
WHICH script reads a declaration is a claim, and a claim gets grepped before it lands.** If it later
earns a gate, the honest shape is an extension of check 22 that joins the conf's key list against the
scripts that actually reference each key, and reds when a dossier sentence names a non-reader.

---

## Not findings, recorded so the next round does not re-report them

- **The guard runs after the conf has already executed.** `adopt-unattended.sh` SOURCES
  `.unattended.conf`, so the value guards at `:166` and `:173` fire after arbitrary shell in that file
  has run. This is pre-existing for every key in that file and is not a control this diff weakens. The
  guards are typo-catchers for a value interpolated into a table row and a code span, and they are
  documented as exactly that.
- **Nothing verifies the gesture was made.** No script in this kit sees an invocation, so the rendered
  parameter cannot be checked at run time. That is the security model, not a gap in it: the parameter
  is the GESTURE, the authorization stays the pushed build folder resolved at the declared anchor, and
  §9 is unchanged by this diff.
- **The kit default literal lives in one place.** The post-source `case` deriving `AUTH_EFFECTIVE`,
  copied from the `ANCHOR_SCOPE` seam directly above it. Verified as the single carrier; the blank
  declarations in both shipped confs are the "kit default" signal and not "off".

## What this review did NOT check

- The kit vintage move 1.9 → 1.10 was not re-derived across all five source carriers plus three
  regenerated artifacts; the diff asserts the set and no lens re-counted it.
- The gate bar was not run as part of this review. Verdict covers the diff's content, not its green.
- The prompt-record path under `builds/<slug>/prompts/` was exercised only on the shapes the fixtures
  carry; no adversarial prompt bytes (a heading-canon collision, a fence-blind generated-region
  marker at column 1) were fed through it end to end.
