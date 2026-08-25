# KICK-cKeyedLaunchpad-3 — three checks the ratchet never had, and the stall it can actually measure

**Status:** CLOSED · rev-3 · 2026-08-20 · node c · Tier-2 · base f006691f · streams kickoff+tooling

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-13-review-KICK-cKeyedLaunchpad-3-1.md](../reviews/2026-08-13-review-KICK-cKeyedLaunchpad-3-1.md) | spec-audit | KICK-cKeyedLaunchpad-6 |
| [2026-08-14-review-KICK-cKeyedLaunchpad-1-2.md](../reviews/2026-08-14-review-KICK-cKeyedLaunchpad-1-2.md) | spec-audit | KICK-cKeyedLaunchpad-1 KICK-cKeyedLaunchpad-2 KICK-cKeyedLaunchpad-4 KICK-cKeyedLaunchpad-6 KICK-cKeyedLaunchpad-7 TOOL-cKeyedLaunchpad-5 |

<!-- /gen:spec-records -->

## 1. Goal

Give the ratchet an opinion about the manifest's SIZE and SHAPE, not only its structure. C1 through
C6 check placeholders, block parseability, sha ancestry, tracked anchors and watch drift; a 77,056-byte
manifest carrying a 16,196-character line passes all six clean. C7, C8 and C9 close that.

## 2. Scope (IN)

- S1. **C7 — size.** The LF-normalised manifest must be at most 25,600 bytes. Hard red, no grace
  period, with a `MAX_MANIFEST_BYTES` environment override for testability only.
- S2. **C8 — line length.** No line may exceed 400 bytes, with the audit block and fenced code blocks
  exempt.
- S3. **C9 — maintenance stall.** The audit block gains a `last-body-change` key holding a full sha.
  C9 reds when ten or more non-merge watch-pathspec commits have landed since that sha, or when its
  committer date is three or more months old, whichever comes first.
- S4. C7 and C8 sit after C1 and run in both the full and `--staged` legs. C9 sits inside the
  existing non-staged branch after C5 and never runs in the staged leg.
- S5. C2 requires `last-body-change` and validates its shape, and C9 validates the sha is real and an
  ancestor of HEAD, reusing C3's existing branches rather than re-implementing them.
- S6. `KIT_MANIFEST_VERSION` goes to 1.2, applied to all seven sites in one commit, and the retrofit
  message names the new key.
- S7. A `KIT_MANIFEST_VERSION` entry in `tools/check-kit-versions.sh`, so the constant and the two
  shipped markers can no longer drift apart silently.
- S8. `ARMS_FLOORS` for this script is raised from `16:16` to the new branch count, and every new
  branch gets a positive assertion naming its own literal text.

## 3. Non-goals (OUT)

- **C8 does not make the NicoCares manifest pass, and is not meant to.** Its twelve over-length lines
  are five in fences, five authored body bullets and two table rows. The exemptions clear the five
  fence lines; seven survive. The exemptions exist so the check cannot fire on machine-maintained
  data, not to launder an over-cap manifest into green.
- **No table-content or body exemption.** Either one would clear the remaining seven and leave C8
  measuring nothing an author controls, which is the same as not having C8.
- **No retrofit of the NicoCares manifest.** Named in §5 as a live risk with a changed shape, but the
  work belongs to that repo.
- **C9 does not read Step 2b's delta lines.** `aRatchetForge` §10.9 established why: they live in
  commit messages and READY cards, which squash merges do not preserve.
- **C9 does not derive its baseline by walking history.** §4 records the measurement that closed that
  design off.
- **C2 gains a fourth required key and that IS a semantics change**, stated rather than denied: S5
  adds `last-body-change` to the keys C2 requires and shape-checks, with its own absent and
  malformed failures. C1 and C3-C6 are unchanged. No new gate leg.

## 4. Design

### Placement, and why it is not arbitrary

C7 and C8 are file-level, independent of `BLOCK_OK`, and one fork each. They go immediately after C1,
before the C2 block parse, reading the working-tree file through `tr -d '\r'` exactly as C1 and C2
already do. That placement matters for a reason outside this script: the pre-commit hook runs the
manifest staged leg **unconditionally**, unlike the memory-tree and template-size legs beside it,
which both carry `git diff --cached` guards. Every commit in an adopting repo pays this leg, measured
here at 3.76 s. Two cheap checks are affordable there; C9 is not, and it sits inside the existing
`if [ "$STAGED" = 0 ]` branch where it can never reach the hook. S4 is a contract, so §6 observes it
from both sides rather than trusting placement.

### Normalisation is not optional

`.claude/SESSION-KICKOFF.md` carries no `eol=lf` pin and this checkout is CRLF: 21,170 bytes on disk
against 20,920 normalised. An unnormalised C7 measures a different number per platform, which is the
exact split `.gitattributes` records having already cost this repo a blocked push on the memory-tree
byte caps. `check-template-size.sh` is the in-repo precedent and does the same `tr -d '\r'`.

After U2 the manifest lands under `memory/`, which IS pinned — but adopters at `.claude/` are not, so
the normalisation stays regardless.

### C8 measures bytes, and says so

`awk`'s `length()` counts bytes on this platform, not characters: a line this repo's Python measures
at 194 characters measures 197 in awk, because of multibyte `·`, `—` and `≥`. Getting characters in
POSIX shell would need a locale-aware invocation that cannot be relied on across busybox, mawk and
BSD awk. So the limit is 400 BYTES and the failure message says bytes. Claiming characters and
measuring bytes would be a gate whose message is false by up to three percent.

### The exemption tension, stated rather than hidden

This repo's longest line is 303 bytes — the audit block's `watch:` list of ten pathspecs, which grows
mechanically as watched paths are added. It is at 76% of the cap, and roughly three more pathspecs
would red it. Exempting the audit block is correct, because that line is machine-maintained data with
no prose to wrap. The consequence is that the only line in this repo anywhere near the limit is the
one line C8 cannot see. That is the right trade and it is written down here so the next reader does
not rediscover it as a defect.

### Where C7's 25,600 comes from

It is not measured on this corpus, and it cannot be: C7 ships to adopters this build does not control,
so a limit fitted to gov's manifest would be a pin copied from the wrong corpus in the other
direction. The rule that set it is stated instead, so a future raise has something to argue against.

The seed a fresh adopter instantiates is 8,112 bytes. 25,600 is that seed with room to roughly triple
— enough that a manifest accreting real project knowledge is never fighting the gate, and small
enough that the file stays readable in one sitting. The two live data points bracket it: gov measures
20,920 and passes with 18% of the cap free; NicoCares measures 77,056 and is three times over, which
is the outcome the check exists to produce.

After U6's eviction gov drops to roughly 15 KB — 20,920 less the 14,535-byte traps section plus its
derived ceiling of 8,430 — leaving C7 at about 1.7 times the file it guards.
That slack is deliberate and is the reason C11, U6's per-bullet cap, exists as a separate check: C7
bounds the file, and a file-level cap with that much headroom cannot bound the section that actually
accretes.

### C9 reads a recorded baseline, because the walk cannot survive a rename

The first design derived the baseline by walking `git log --name-status` over the manifest and
classifying each commit — rename skipped, add treated as the manifest's birth, modify compared. **It
does not work, and the measurement is recorded here because the whole design turned on it.**

Reproduced in a scratch repository at git 2.55: create a file, edit it, `git mv` it, then run a
path-scoped `git log --name-status` on the new path. The move is reported as **`A`**, not `R`, and
the walk stops there — pre-rename history is unreachable. Only `git log --follow` reports `R100` and
reaches through. So the rename branch would have been dead code, and U2's own `git mv` of this very
manifest would have been read as the file's birth, reporting a stalled manifest as freshly maintained.
That is the same false-fresh outcome this section rejects the empty-parent inference for, reached by a
different route.

`--follow` would fix the classification and keep every other cost: a candidate cap for the 132-commit
path history at roughly 350 ms per candidate pair, a shallow-clone skip because a graft boundary
yields an empty parent that scores as a false GREEN, and a 2.4 s runtime. The baseline is recorded
instead.

**The mechanism.** The audit block gains `last-body-change`, a full sha naming the commit at which the
manifest body was last genuinely revised. C9 counts non-merge commits touching the watch pathspecs
between that sha and HEAD, and reads that commit's committer date for the elapsed-time arm. There is
no walk, no classification, no candidate cap, and a rename is invisible to it because no history
traversal of the manifest path happens at all. The shallow-clone case reduces to C3's existing
problem — a sha that may be absent — and reuses C3's existing branch rather than inventing a second
one.

**What clears a red, which the walk had no answer for.** Advancing `last-body-change` is the remedy,
and it is an assertion the author makes: the manifest has been re-read and is still true. That is
deliberately the same trust model `last-audit` already runs on — the ratchet has never been able to
tell a real verification from a reflex stamp, and it does not need to, because C5 independently reds
whenever watched files move past the stamp. What C9 adds is a floor on how long that assertion may go
unrepeated. Under the walk design, a stable and accurate manifest would have red quarterly forever
with no action able to clear it, since the only exit was cosmetic body churn.

**The elapsed-time arm** compares the committer date of `last-body-change` against now, three months.
Committer date rather than author date, because a rebase preserves author date and the question is
when this history last moved.

### The version bump, and the gap it would otherwise widen

Nothing mechanically forces `KIT_MANIFEST_VERSION` to agree with the two shipped markers:
`check-kit-versions.sh` has no entry for it and `check-verdict-epoch.sh` is hardcoded to the
memory-tree engine. The constant and the markers can drift with the full bar green — the same hole
`check-kit-versions.sh`'s own comment describes for `BUILD-METHOD.template.md`, which went three
bumps behind and shipped that number into every adopting tree. This unit bumps the version, so it
adds the entry that makes the next bump mechanical.

The bump has a test cost: the fixture default marker is `v1.1`, one scenario asserts the literal
retrofit string naming that version, and every fixture manifest now needs the new audit-block key.

### Every branch must be armed, and the message shape decides whether it can be

`check-arms.py` DISCOVERS this script — any tracked non-test `.sh` defining `fail() {` — and requires
each branch's message to carry a literal run of at least twelve characters, after `${VAR}`
interpolations are split out, that some non-comment line of the test file asserts as a substring.
C7, C8 and C9's messages are naturally variable-heavy, which is precisely the shape that fragments a
message into runs too short to assert on.

The manifest already records the remedy for this class: bind the value to a name and put it at the
END of the message, after the literal sentence. Every new branch here follows that shape.

`ARMS_FLOORS` is one-sided upward, so landing new branches without raising the floor leaves it green
while quietly losing coverage over the difference. S8 raises it in the same commit.

### Files touched (estimate)

| File | Change |
|---|---|
| `skills/session-kickoff/manifest-check.sh` | C7, C8, C9, C2's new key, the version constant, the retrofit string |
| `skills/session-kickoff/manifest-check.test.sh` | new arms, the fixture marker default, the retrofit literal, the new key in every fixture |
| `skills/session-kickoff/MANIFEST-TEMPLATE.md` | the marker and the new audit-block key |
| the manifest (at U2's new path) | the marker, the new key, and the `last-audit` re-stamp the edit obliges |
| `tools/check-kit-versions.sh` | the new entry |
| `.memory-tree.conf` | the raised `ARMS_FLOORS` pair |

### Alternatives rejected

- **C8 as a character cap.** Not implementable portably in POSIX awk; see above.
- **Exempting table or body lines.** Clears the seven remaining NicoCares lines and leaves C8 gating
  nothing an author writes.
- **C9 in the staged leg.** Even at the baseline design's lower cost, the hook runs unconditionally on
  every commit and C9 answers a question no single commit changes.
- **The `--name-status` walk.** Measured not to work; see above.
- **The `--follow` walk.** Works, and carries the candidate cap, the shallow-clone skip and the
  runtime for a question a recorded sha answers directly.
- **A hard-coded 25,600 with no override.** `check-template-size.sh` accepts `MAX_BYTES` and drives
  its own self-test with it; without the same hatch, testing C7 means writing a >25 KiB fixture on
  every suite run, and the suite's stated cost is fixture construction.

## 5. Production-readiness checklist

- security — read-only checks over a tracked file and git history.
- perf / scale — C7 and C8 are one fork each on a hook that fires every commit; C9 is two git commands
  against a recorded sha, with no history walk to bound.
- a11y — N/A, terminal output.
- i18n — the byte-versus-character decision is stated in the message rather than papered over.
- error / empty / loading states — an absent or malformed `last-body-change` is a C2 failure with the
  retrofit text; an unreachable sha reuses C3's shallow-clone and foreign-stamp branches.
- observability — each failure names the measured value at the END of a literal sentence, which is
  both the armable shape and the readable one. C9's message names the remedy: advance the key.
- risks — **the hard-red decision for C7 rests on an assumption the grounding falsified.** The manifest
  records that adopters "re-pull on kit update", but the only real adopter's checker is several
  revisions stale and predates the MSYS path-resolution rewrite. So C7 does not red NicoCares when
  this lands; it reds at an unpredictable future re-pull, against a manifest three times the cap, with
  no migration staged. The decision stands — it is the owner's — but its consequence is different from
  the one it was taken against. C9 carries no equivalent risk now that advancing the key clears it.
- testing + left-shift gates — S8, plus S7 which makes the next version bump mechanical.
- migration / rollback — `MAX_MANIFEST_BYTES` exists for the self-test, not as an adopter escape
  hatch. A v1.1 manifest lacking `last-body-change` gets the version WARN and the C2 retrofit text
  naming the key, which is the upgrade instruction.
- user docs — the `WIRE` Maintenance section documents the stall thresholds as an owner review; it
  changes to say the check now performs it, and to name the key that clears it.

## 6. Acceptance criteria

- AC1. When a manifest exceeds 25,600 LF-normalised bytes, the check fails naming C7 and reports the
  measured size, and exits 1.
- AC2. When a manifest is CRLF and its LF-normalised size is under the cap, C7 passes — the check
  measures normalised bytes, not on-disk bytes.
- AC3. When a body line exceeds 400 bytes, the check fails naming C8 and the offending line number.
- AC4. When the audit block's `watch:` line exceeds 400 bytes, C8 does NOT fire.
- AC5. When a line inside a fenced block exceeds 400 bytes, C8 does NOT fire.
- AC6. When a table content row exceeds 400 bytes, C8 DOES fire — the exemption set is audit and
  fences only.
- AC7. When `last-body-change` is absent from the audit block, C2 fails with a message naming the key
  and carrying the retrofit instruction.
- AC8. When `last-body-change` holds anything but a full 40-hex sha, C2 fails naming the malformed
  value.
- AC9. When ten or more non-merge watch-pathspec commits have landed since `last-body-change`, the
  check fails naming C9, reporting the count and the baseline sha, and naming advancing the key as the
  remedy.
- AC10. When nine such commits have landed, C9 passes — the threshold is observed at its boundary from
  both sides.
- AC11. When merge commits would carry the count over the threshold but non-merge commits would not,
  C9 passes. This is the arm that fails if `--no-merges` is dropped, and it is the difference between
  this repo reding and passing on day one.
- AC12. When `last-body-change` names a commit whose committer date is three or more months old, C9
  fails on the elapsed-time arm with fewer than ten commits present. The fixture ages a commit with
  `GIT_COMMITTER_DATE`.
- AC13. When `last-body-change` is advanced to a current commit, a previously red C9 passes — the
  documented remedy is observed, not assumed.
- AC14. When the manifest is renamed with `git mv` between the baseline and HEAD, C9's verdict is
  unchanged. This is the arm the previous design could not satisfy.
- AC15. When `last-body-change` names a sha unknown to the repository, the check fails or WARN-skips
  exactly as C3 does for `last-audit`, and does not report green.
- AC15b. When `last-body-change` names a real commit that is NOT an ancestor of HEAD — a squash-merged
  or rewritten stamp — the check fails exactly as C3 does for `last-audit`. S5 claims the ancestor
  branch is reused; this is what observes it.
- AC16. When `manifest-check.sh --staged` runs against a staged manifest that is oversize or carries an
  over-long line, it fails — C7 and C8 are present in the staged leg.
- AC17. When `manifest-check.sh --staged` runs against a stalled manifest, it exits 0 with no C9 line,
  and the staged leg's header enumeration is asserted as a literal string — C9 is absent from that leg.
- AC18. `python tools/memory-tree/check-arms.py` reports every branch armed, with the floor raised to
  the new count.
- AC19. `bash tools/check-kit-versions.sh` fails when `KIT_MANIFEST_VERSION` and either shipped marker
  disagree — asserted by a fixture, not by inspection.
- AC20. `GATE_FULL=1 bash tools/run-gates.sh` is green on this repo, C9 included.

## 7. Gates

- `bash skills/session-kickoff/manifest-check.sh` and `manifest-check.test.sh`.
- `python tools/memory-tree/check-arms.py` — the floor moves; a slack floor is a silent coverage loss.
- `bash tools/check-kit-versions.sh` — gains the entry S7 adds.
- `GATE_FULL=1 bash tools/run-gates.sh`.
- No new gate leg; all three checks ride the existing ratchet leg.

## 8. Open questions

none — the forks are RESOLVED, three by the owner and one on the merits below.

- The C7 severity. RESOLVED (owner, 2026-08-13): hard red from day one. Recorded with a correction:
  the consequence is not the one the decision was taken against, per §5.
- The C9 thresholds. RESOLVED (owner, 2026-08-13): `aRatchetForge` §10.9's ten commits or three
  months.
- The C9 mechanism, after the M4 audit reproduced the rename defect. RESOLVED (owner, 2026-08-13): a
  recorded baseline in the audit block rather than a `--follow` history walk. This also settles what
  clears a C9 red, which the walk design had no answer for.
- Whether merges count toward C9's threshold. RESOLVED (agent, 2026-08-13): excluded. The prior spec
  is silent, so this fills a genuine gap rather than re-litigating an owner decision. It is decided on
  the merits in the earlier revision's §4 and is now observed directly by AC11.

## 9. Revision log

- rev-1 · 2026-08-13 · initial draft, grounded by workflow `wf_0aaecb50-a51`.
- rev-3 · 2026-08-13 · folded the M4 fix-verify pass. S5 added a fourth required audit-block key
  while §3 still claimed "No change to C1-C6 semantics" — C2 demonstrably changes, so §3 now says so
  rather than denying it. Added AC15b: S5 claims C3's ancestor branch is reused and nothing observed
  the non-ancestor case. Corrected the post-eviction figure, which was computed against U6's
  superseded 4,000-byte target, and the C10/C11 echo after U4 took C10.
- rev-2 · 2026-08-13 · folded the M4 spec audit, review record 1. B1 (blocker): C9's rename guard
  could not fire — a path-scoped `git log --name-status` reports a `git mv` as an add, not a rename,
  reproduced at git 2.55, so U2's own move would have read as the manifest's birth. Replaced the
  history walk with a recorded `last-body-change` baseline, which also answers H3 (nothing cleared a
  C9 red) and removes the candidate cap, the shallow-clone false-green and the 2.4 s runtime. H1: the
  three-month branch had neither a design nor a criterion — now names committer date and carries an
  aged-fixture criterion. H2: the staged/non-staged placement contract was unobserved — two criteria
  added. M1: C7's 25,600 had no derivation — the rule that set it is now stated with both live data
  points. Criteria grew from 14 to 20.

## 10. Reuse audit

Three seams are extended rather than re-invented. C7 copies `tools/check-template-size.sh`'s byte
measurement verbatim — `tr -d '\r' | wc -c`, an env-overridable cap, and a remedy that refuses to
raise the limit. C8 copies the fence-tracking awk in `check-memory-hygiene.sh`'s check 7, which
already tracks both ``` and `~~~`, strips CR, and exempts table separator rows; its exemption set is
adapted, not its mechanism. C9 reuses the `WATCH` array C2 already parses and C3's existing sha
validation branches, and after the rev-2 redesign it reuses `last-audit`'s own storage shape — a
key in the audit block, validated the same way — rather than deriving anything from history.

`reuse_lookup.py "gate a document's size and line length"` returned `check-install-prefix.sh` and the
`template size <=32KiB` leg. The latter is the right MECHANISM and the wrong HOME: it is a gov-only
leg over a single named file, and these checks must ride `manifest-check.sh` so an adopter inherits
them by re-pulling the kit rather than by copying a gate. The mechanism is reused; the leg is not
extended.

C7's limit is deliberately NOT measured on this corpus, which is the opposite of what
`memory/gotchas/pin-copied-from-another-corpus.md` prescribes. That record's rule is that a pin is
measured at adoption rather than inherited; it assumes the gate and the corpus share an owner. This
limit ships to repos this build has never seen, so §4 states the rule that set it and the two live
measurements that bracket it, which is the closest available equivalent to a derivation.

Recall terms used: `kickoff manifest ratchet last-audit watch verify-paths SESSION-KICKOFF discovery
order traps accretion size gate prose`.
