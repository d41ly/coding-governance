# KICK-cKeyedLaunchpad-3 — three checks the ratchet never had, and the one that reds this repo

**Status:** OPEN · rev-1 · 2026-08-13 · node c · Tier-2 · base f006691f · streams kickoff+tooling

## 1. Goal

Give the ratchet an opinion about the manifest's SIZE and SHAPE, not only its structure. C1 through
C6 check placeholders, block parseability, sha ancestry, tracked anchors and watch drift; a 77,056-byte
manifest carrying a 16,196-character line passes all six clean. C7, C8 and C9 close that.

## 2. Scope (IN)

- S1. **C7 — size.** The LF-normalised manifest must be at most 25,600 bytes. Hard red, no grace
  period, with a `MAX_MANIFEST_BYTES` environment override for testability only.
- S2. **C8 — line length.** No line may exceed 400 bytes, with the audit block and fenced code blocks
  exempt.
- S3. **C9 — maintenance stall.** Red when the manifest's BODY has not changed across ten or more
  non-merge watch-pathspec commits, or three months, whichever comes first.
- S4. C7 and C8 sit after C1 and run in both the full and `--staged` legs. C9 sits inside the
  existing non-staged branch after C5 and never runs in the staged leg.
- S5. `KIT_MANIFEST_VERSION` goes to 1.2, applied to all seven sites in one commit.
- S6. A `KIT_MANIFEST_VERSION` entry in `tools/check-kit-versions.sh`, so the constant and the two
  shipped markers can no longer drift apart silently.
- S7. `ARMS_FLOORS` for this script is raised from `16:16` to the new branch count, and every new
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
  commit messages and READY cards, which squash merges do not preserve. C9 reads git.
- No change to C1-C6 semantics, and no new gate leg.

## 4. Design

### Placement, and why it is not arbitrary

C7 and C8 are file-level, independent of `BLOCK_OK`, and one fork each. They go immediately after C1,
before the C2 block parse, reading the working-tree file through `tr -d '\r'` exactly as C1 and C2
already do. That placement matters for a reason outside this script: the pre-commit hook runs the
manifest staged leg **unconditionally**, unlike the memory-tree and template-size legs beside it,
which both carry `git diff --cached` guards. Every commit in an adopting repo pays this leg, measured
here at 3.76 s. Two cheap checks are affordable there; C9, measured at 2.4 s, is not, and it sits
inside the existing `if [ "$STAGED" = 0 ]` branch where it can never reach the hook.

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

### C9, and the three things C5 does not have to worry about

C9 inverts C5's technique: the same `git show <c>:$MF` versus `git show <c>^:$MF` pair, but comparing
the body with `grep -v '^[[:space:]]*last-audit:'` instead of `blockstamp`, walking until the first
real difference. Verified against this repo's real history — the last eight manifest commits classify
as six pure re-stamps and one genuine body change, which is exactly what C9 must see through.

Three additions C5 does not need:

1. **A rename guard.** C5 is deliberately pathspec-FREE because git's rename detection collapses a
   pure `git mv` of the manifest; scenario 27 exists because that laundering hole was real. C9 must
   be path-scoped, so it meets the mirror of that hole: a path-scoped walk sees a rename as a commit
   touching the manifest whose parent blob is EMPTY, and an empty parent is indistinguishable from a
   body change — a rename would falsely report the manifest as freshly maintained. C9 therefore
   classifies each candidate by git's own `--name-status`: `R` is skipped, `A` is the manifest's
   birth and terminates the walk as a body change, and only `M` is compared. **U2 performs exactly
   this `git mv`,** so this guard is not hypothetical for this build.
2. **A candidate cap.** This repo's manifest has 132 commits of path history at roughly 350 ms per
   candidate pair. An uncapped walk over a manifest whose body never changed is a 46-second check.
   The walk stops at 50 candidates and reds, because a body unchanged across fifty manifest commits
   is the stall C9 exists to report.
3. **A shallow-clone skip.** On a depth-1 clone, `git show <c>^:$MF` fails at the graft boundary and
   yields an empty parent, which a naive comparison scores as a body change — a false GREEN, not a
   missing answer. C9 reuses C3 and C5's existing `SKIP_RANGE` guard and its shallow-clone fixture.

### Merges are excluded from the count, and that decision reds or greens this repo

`aRatchetForge` §10.9 says "≥10 watch-pathspec commits" and does not say whether merges count. It
decides the verdict here: since this manifest's newest body change, eleven watch-touching commits
have landed counting merges, and six excluding them, against a threshold of ten. Counting merges reds
this repo the day C9 lands.

Merges are excluded, on the merits rather than the convenience. The threshold measures how much
content churn the manifest has not been audited against. A merge commit carries no content of its
own; counting it alongside the commits it brings in double-counts the same churn. `--no-merges`
counts the content-bearing commits, which is what "watch-pathspec commits" means.

### Every branch must be armed, and the message shape decides whether it can be

`check-arms.py` DISCOVERS this script — any tracked non-test `.sh` defining `fail() {` — and requires
each branch's message to carry a literal run of at least twelve characters, after `${VAR}`
interpolations are split out, that some non-comment line of the test file asserts as a substring.
C7, C8 and C9's messages are naturally variable-heavy, which is precisely the shape that fragments a
message into runs too short to assert on.

The manifest already records the remedy for this class: bind the value to a name and put it at the
END of the message, after the literal sentence. Every new branch here follows that shape.

`ARMS_FLOORS` is one-sided upward, so landing new branches without raising the floor leaves it green
while quietly losing coverage over the difference. S7 raises it in the same commit.

### The version bump, and the gap it would otherwise widen

Nothing mechanically forces `KIT_MANIFEST_VERSION` to agree with the two shipped markers:
`check-kit-versions.sh` has no entry for it and `check-verdict-epoch.sh` is hardcoded to the
memory-tree engine. The constant and the markers can drift with the full bar green — the same hole
`check-kit-versions.sh`'s own comment describes for `BUILD-METHOD.template.md`, which went three
bumps behind and shipped that number into every adopting tree. This unit bumps the version, so it
adds the entry that makes the next bump mechanical. That is the left-shift for a gap this unit would
otherwise widen.

The bump has a test cost: the fixture default marker is `v1.1` and one scenario asserts the literal
string `marker to v1.1 LAST` from the retrofit message. Both move with it.

### Files touched (estimate)

| File | Change |
|---|---|
| `skills/session-kickoff/manifest-check.sh` | C7, C8, C9, the version constant, the retrofit string |
| `skills/session-kickoff/manifest-check.test.sh` | new arms, the fixture marker default, the v1.1 literal |
| `skills/session-kickoff/MANIFEST-TEMPLATE.md` | the marker |
| the manifest (at U2's new path) | the marker, and the `last-audit` re-stamp the edit obliges |
| `tools/check-kit-versions.sh` | the new entry |
| `.memory-tree.conf` | the raised `ARMS_FLOORS` pair |

### Alternatives rejected

- **C8 as a character cap.** Not implementable portably in POSIX awk; see above.
- **Exempting table or body lines.** Clears the seven remaining NicoCares lines and leaves C8 gating
  nothing an author writes.
- **C9 in the staged leg.** 2.4 s on a hook that already runs unconditionally on every commit.
- **Deriving C9's baseline from the empty-parent blob instead of `--name-status`.** That is the exact
  inference that makes a rename read as maintenance.
- **A hard-coded 25,600 with no override.** `check-template-size.sh` accepts `MAX_BYTES` and drives
  its own self-test with it; without the same hatch, testing C7 means writing a >25 KiB fixture on
  every suite run, and the suite's stated cost is fixture construction.

## 5. Production-readiness checklist

- security — three read-only checks over a tracked file and git history.
- perf / scale — C7 and C8 are one fork each on a hook that fires every commit; C9 is 2.4 s and is
  excluded from that hook. The candidate cap bounds C9's worst case.
- a11y — N/A, terminal output.
- i18n — the byte-versus-character decision is stated in the message rather than papered over.
- error / empty / loading states — the shallow-clone skip, the candidate cap, and the rename class.
- observability — each failure names the measured value at the END of a literal sentence, which is
  both the armable shape and the readable one.
- risks — **the hard-red decision rests on an assumption the grounding falsified.** The manifest
  records that adopters "re-pull on kit update", but the only real adopter's checker is several
  revisions stale and predates the MSYS path-resolution rewrite. So C7 does not red NicoCares when
  this lands; it reds at an unpredictable future re-pull, against a manifest three times the cap,
  with no migration staged. The decision stands — it is the owner's — but its consequence is
  different from the one it was taken against, and §8 records that.
- testing + left-shift gates — S7, plus S6 which makes the next version bump mechanical.
- migration / rollback — `MAX_MANIFEST_BYTES` exists for the self-test, not as an adopter escape
  hatch; the remedy string says so, following `check-template-size.sh`'s "do NOT raise the limit".
- user docs — the `WIRE` Maintenance section already documents the stall thresholds as an owner
  review; it changes to say the check now performs it.

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
- AC7. When the manifest body has not changed across ten or more non-merge watch-pathspec commits,
  the check fails naming C9 and reports the count and the baseline sha.
- AC8. When the manifest has been re-stamped repeatedly with no body change, C9 sees through every
  re-stamp — a fixture of six pure stamps plus one body change resolves to the body change.
- AC9. When the manifest was renamed since its last body change, C9 does NOT report it as freshly
  maintained. This is the arm that fails without the `--name-status` guard.
- AC10. When the repository is a shallow clone, C9 emits a WARN and skips, and does not report green.
- AC11. When the walk reaches the candidate cap without finding a body change, the check fails rather
  than passing.
- AC12. `python tools/memory-tree/check-arms.py` reports every branch armed, with the floor raised to
  the new count.
- AC13. `bash tools/check-kit-versions.sh` fails when `KIT_MANIFEST_VERSION` and either shipped
  marker disagree — asserted by a fixture, not by inspection.
- AC14. `GATE_FULL=1 bash tools/run-gates.sh` is green on this repo, C9 included. Per §4 this holds
  only because merges are excluded; with merges counted this repo measures eleven against a threshold
  of ten.

## 7. Gates

- `bash skills/session-kickoff/manifest-check.sh` and `manifest-check.test.sh`.
- `python tools/memory-tree/check-arms.py` — the floor moves; a slack floor is a silent coverage loss.
- `bash tools/check-kit-versions.sh` — gains the entry S6 adds.
- `GATE_FULL=1 bash tools/run-gates.sh`.
- No new gate leg; all three checks ride the existing ratchet leg.

## 8. Open questions

none — the forks are RESOLVED, two by the owner before authoring and one on the merits below.

- The C7 severity. RESOLVED (owner, 2026-08-13): hard red from day one. Recorded with a correction:
  the consequence is not the one the decision was taken against, per §5. The owner may revisit; the
  spec does not assume they will.
- The C9 thresholds. RESOLVED (owner, 2026-08-13): `aRatchetForge` §10.9's ten commits or three
  months.
- Whether merges count toward C9's threshold. RESOLVED (agent, 2026-08-13): excluded. The prior spec
  is silent, so this is not a re-litigation of an owner decision but the filling of a genuine gap in
  it. It is decided on the merits in §4 and it is the difference between this repo reding and passing
  on day one, so it is flagged rather than buried.

## 9. Revision log

- rev-1 · 2026-08-13 · initial draft, grounded by workflow `wf_0aaecb50-a51`.

## 10. Reuse audit

Three seams are extended rather than re-invented. C7 copies `tools/check-template-size.sh`'s byte
measurement verbatim — `tr -d '\r' | wc -c`, an env-overridable cap, and a remedy that refuses to
raise the limit. C8 copies the fence-tracking awk in `check-memory-hygiene.sh`'s check 7, which
already tracks both ``` and `~~~`, strips CR, and exempts table separator rows; its exemption set is
adapted, not its mechanism. C9 inverts `manifest-check.sh`'s own C5 loop, reusing the `WATCH` array
C2 already parses and the `SKIP_RANGE` shallow guard C3 already sets.

`reuse_lookup.py "gate a document's size and line length"` returned `check-install-prefix.sh` and the
`template size <=32KiB` leg. The latter is the right MECHANISM and the wrong HOME: it is a gov-only
leg over a single named file, and these checks must ride `manifest-check.sh` so an adopter inherits
them by re-pulling the kit rather than by copying a gate. The mechanism is reused; the leg is not
extended.

Recall terms used: `kickoff manifest ratchet last-audit watch verify-paths SESSION-KICKOFF discovery
order traps accretion size gate prose`.
