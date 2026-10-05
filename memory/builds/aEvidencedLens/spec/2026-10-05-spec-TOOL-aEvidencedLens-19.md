# TOOL-aEvidencedLens-19 — unit 18's byte tie is observed with filters off: each saved harness file equals its blob byte for byte, and a CRLF copy and a one-byte append each red it

**Status:** SPECCED · rev-1 · 2026-10-05 · node a · Tier-2 · base 028b5cac · streams tooling · order 11

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of `TOOL-aEvidencedLens-18`
(`reviews/2026-10-05-review-TOOL-aEvidencedLens-18-spec-audit-round1.md`) exited CONVERGED with one
confirmed finding at HIGH. The method promotes it to a unit whose mechanism closes it, and this is
that unit. It repairs `TOOL-aEvidencedLens-18` and closes:

- **id 14 (HIGH)** — unit 18's S1 ties each saved harness file to its blob with plain
  `git hash-object`, which applies the path's clean filter. On this node `core.autocrlf=true` comes
  from the system gitconfig and `tools/workflows/tier2-review.js` is `text eol=lf`, so a
  CRLF-rewritten copy hashes to the LF blob and the tie reads equal for bytes the driver did not run
  on. Its §5 names no staged break for that tie, against the build rule that every new refusal is
  observed RED on one. Closed by S1 to S4.

Unit 18 builds first, as written. This unit then re-takes the tie with every filter off, observes
it red on two staged breaks, and runs unit 18's AC1 driver command over exactly the bytes it tied.

## 2. Scope (IN)

- **S1** — SAVED RAW, FROM BASH. `base.js` and `head.js` are written in the run's scratch by
  `git cat-file blob <rev>:tools/workflows/tier2-review.js > <scratch>/<name>.js` run from bash, at
  BASE `028b5cac` and at the pass's `HEAD`. No PowerShell redirect and no text-mode write touches
  either file, since both are the line-ending rewrite this unit exists to catch. Observed by AC1.
- **S2** — THE TIE WITH FILTERS OFF. For each saved file, `git hash-object --no-filters <file>`
  equals `git rev-parse <rev>:tools/workflows/tier2-review.js`, AND `cmp` of the file against
  `git cat-file blob <rev>:tools/workflows/tier2-review.js` reports no difference. The tie reds and
  names the file when either form differs. Both forms run, and the ledger records each. Observed by
  AC1.
- **S3** — TWO STAGED BREAKS RED THE TIE. `head-crlf.js` is `head.js` through `sed 's/$/\r/'`, and
  `head-x.js` is `head.js` with one byte appended. S2's assertion over each, against HEAD's blob,
  reds and names the file. Beside the CRLF red, plain `git hash-object head-crlf.js` is run and its
  output recorded: printing HEAD's blob is what shows the break discriminates the filtered form from
  this one. Observed by AC2.
- **S4** — THE DRIVER RUNS ON THE TIED BYTES. Unit 18's AC1 command,
  `node u15-check.js --mask-class base.js head.js` over the two diff-kind arg sets, runs on the two
  files S2 tied, and S2's tie is taken again after the run. Equal both times means the bytes the
  driver read are the bytes the ledger names. Observed by AC3.
- **S5** — The blob ids, both forms of each tie, the two break reds, the plain-form output over
  `head-crlf.js` and the driver outcomes are written to this unit's acceptance ledger,
  `memory/builds/aEvidencedLens/build/2026-10-05-build-TOOL-aEvidencedLens-19-1-acceptance-ledger.md`,
  carrying `**Serves:** journal TOOL-aEvidencedLens-19` and an `**Evidences:** TOOL-aEvidencedLens-19`
  block. Observed by AC4.

## 3. Non-goals (OUT)

- Any change under `tools/`. This unit observes; a red is a defect in the bytes or the harness,
  fixed in the unit that moved them.
- Rewriting unit 18's criteria or its ledger. Unit 18 is built as written, and its ledger stands as
  the record of what its filtered tie observed. This unit's ledger carries the filter-off tie.
- The report's left-shift proposals for id 14: a check refusing a bare `git hash-object` used as an
  identity assertion, and a spec-audit checklist entry. Each is a separate mechanism, and neither is
  needed to close the finding for this observation.
- The other fourteen confirmed findings of the same audit. They are the minors batch,
  `TOOL-aEvidencedLens-20`.

### Edges

- **consumes-from** `TOOL-aEvidencedLens-18` — the completed observation: its AC1 command over
  `u15-check.js` and the two diff-kind arg sets it carries forward from unit 15, which this unit
  re-runs over bytes tied with filters off.

## 4. Design

### Evidence

Read at `ad25d88c3` on 2026-10-05, in the run's scratch.

- `git config --show-origin --get core.autocrlf` prints the system gitconfig with `true`, and
  `git check-attr text eol -- tools/workflows/tier2-review.js` prints `text: set` and `eol: lf`.
- `git rev-parse HEAD:tools/workflows/tier2-review.js` printed `3faf86625e60`. A `git cat-file blob`
  save of it hashed to the same id with `--no-filters`, and `cmp` against the blob reported no
  difference. A `sed 's/$/\r/'` copy hashed to `3faf86625e60` with plain `git hash-object`, and to
  `7732dff5caaf` with `--no-filters`. The filtered form cannot tell the two files apart; the raw form
  can.

### The tie

```text
bash: git cat-file blob 028b5cac:<harness> > base.js ; git cat-file blob HEAD:<harness> > head.js
for f, rev in (base.js, 028b5cac), (head.js, HEAD):
  assert hash-object --no-filters f == rev-parse rev:<harness>       # red names f
  assert cmp f <(git cat-file blob rev:<harness>)                     # red names f
head-crlf.js = sed 's/$/\r/' head.js ; head-x.js = head.js + 1 byte
  both asserts over each, against HEAD's blob     -> red, names the file
  plain hash-object head-crlf.js                  -> recorded (HEAD's blob shows the filter blind spot)
node u15-check.js --mask-class base.js head.js    -> unit 18's AC1 outcome, per arg set
re-tie base.js and head.js                        -> still equal
```

### Files touched (estimate)

None under `tools/`. The dispatch write set is:

- the acceptance ledger of S5;
- this spec's own status header and `gen:spec-records` region;
- the regenerated `memory/builds/aEvidencedLens/README.md`;
- `memory/LIVE.md` and the month's ledger shard, declared at dispatch if and only if
  `gen_build_index.py`'s derived build status, with this unit flipped to CLOSED, differs from the
  status currently rendered; otherwise neither. That is the rule the same audit's ids 12 and 15 set
  out, applied here to this unit's own dispatch because this unit may close the build.

The scratch files and the driver live in the run's scratch directory.

### Alternatives rejected

- **`git hash-object --path=<harness>`.** It still applies the path's filters; the audit's skeptic
  reproduced it printing the LF blob for the CRLF copy.
- **`cmp` alone.** It ties bytes but prints no id, and the ledger names blobs by id. Both run, since
  each costs one command.
- **Amending unit 18's S1 before it builds.** That is a fold, and the method promotes a spec-audit
  finding rather than folding it.

## 5. Production-readiness checklist

- security — N/A: no code, and no write outside the build's records and the two generated indexes.
- perf / scale — four hashes, four `cmp` runs, two staged breaks and one driver pass, seconds.
- error / empty / loading states — a mismatch in either form, a break that reads green, and a file
  that moves between tie and run each red the observation with the file's name.
- observability — the ledger names both blobs, both forms per file, both break outcomes, the
  plain-form output and the driver outcomes.
- risks — `u15-check.js` lives in scratch, which a lost session empties. It is rebuilt as unit 18's
  §6 preamble says, and the ledger says which happened.
- testing — S3's two breaks are the tie's liveness; S4's re-tie is the driver run's.
- migration — none.
- user docs — N/A.

## 6. Acceptance criteria

Every file named here lives in the run's scratch directory, outside the tree. `u15-check.js` is unit
15's driver, rebuilt when absent as unit 18's §6 preamble states.

- **AC1** — When `base.js` and `head.js` are saved from bash with `git cat-file blob` at BASE
  `028b5cac` and at the pass's `HEAD`, `git hash-object --no-filters` of each equals `git rev-parse`
  of `tools/workflows/tier2-review.js` at the same revision, and `cmp` of each against `git cat-file
  blob` of the same reports no difference.
  Red when: either form differs for either file.
- **AC2** — When `head-crlf.js`, which is `head.js` through `sed 's/$/\r/'`, and `head-x.js`, which
  is `head.js` with one byte appended, are each put through AC1's two assertions against HEAD's blob,
  both assertions red on both files and each red names its file. Plain `git hash-object
  head-crlf.js` is run beside them and its output recorded.
  Red when: either break reads green under either assertion.
- **AC3** — When `node u15-check.js --mask-class base.js head.js` runs over the two diff-kind arg sets
  on the files AC1 tied, it yields exactly one `resume:probe` prompt per run, the BASE and HEAD
  prompts are byte-identical per arg set, and each of the four runs prints a `<KEY>` count of 1.
  AC1's assertions are then repeated and still hold.
  Red when: the probe moved, a run has no `resume:probe` label, a count is not 1, or a file no longer
  ties after the run.
- **AC4** — When `2026-10-05-build-TOOL-aEvidencedLens-19-1-acceptance-ledger.md` under the build's
  `build/` folder is read, it carries `**Serves:** journal TOOL-aEvidencedLens-19` and an
  `**Evidences:** TOOL-aEvidencedLens-19` block. The block names the two blob ids, both assertion
  forms per file with their outcomes, both break reds, the plain-form output over `head-crlf.js`, and
  AC3's outcomes per arg set.
  Red when: the observation lives only in the transcript, in a file check 23 does not read, or the
  ledger omits either break.

## 7. Gates

`memory hygiene` · `recall floor` · `recall floor arms` · `spec tokens (a spec's own names resolve)`

No `New arm:` line: a self-test cannot read this repository's BASE from an adopter's copy
(`TOOL-aEvidencedLens-13` §3).

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-05 · initial draft, promoted from the spec audit of unit 18
  (`reviews/2026-10-05-review-TOOL-aEvidencedLens-18-spec-audit-round1.md`), id 14 (HIGH),
  repairing `TOOL-aEvidencedLens-18`.

## 10. Reuse audit

The seam reused is unit 18's AC1 observation and, through it, unit 15's stub driver `u15-check.js`.
This unit changes how the two inputs are saved and tied, adds two staged breaks, and re-runs the
driver; no tool is built. `python tools/codebase-map/reuse_lookup.py "compare a saved file to its
git blob byte for byte with line-ending filters off"` returned name-stem neighbours only (`git`,
`blob_oid`, `hash_file`, `confirm_blobs`) and printed `unscanned layers: .sh`. None of them is a
check over a scratch file of this observation, so no existing seam fits beyond the git plumbing
itself. The recall probe returned unit 18's spec, the audit finding this unit closes, unit 15's
audit id 5, and the CRLF decisions `TOOL-aUnmannedHelm-10` and `TOOL-aDrainedSluice-8b`, which
record that a working-copy CRLF reaches consumers no byte gate watches. That is this finding's
class, answered here for one observation by tying with filters off.

Recall terms used: hash-object no-filters blob crlf autocrlf acceptance ledger byte identity staged break object database working copy
