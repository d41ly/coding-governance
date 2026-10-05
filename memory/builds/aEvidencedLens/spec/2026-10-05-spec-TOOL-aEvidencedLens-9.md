# TOOL-aEvidencedLens-9 — the bar refuses a run commit that changes `REVIEW_ROUNDS`

**Status:** CLOSED · rev-3 · 2026-10-05 · node a · Tier-2 · base 028b5cac · streams tooling · order 6

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-05-prompt-TOOL-aEvidencedLens-1-1-spec-brief.md](../prompts/2026-10-05-prompt-TOOL-aEvidencedLens-1-1-spec-brief.md) | journal | TOOL-aEvidencedLens-1 TOOL-aEvidencedLens-2 TOOL-aEvidencedLens-3 TOOL-aEvidencedLens-4 TOOL-aEvidencedLens-5 TOOL-aEvidencedLens-6 TOOL-aEvidencedLens-7 TOOL-aEvidencedLens-8 TOOL-aEvidencedLens-10 TOOL-aEvidencedLens-11 |
| [2026-10-05-prompt-TOOL-aEvidencedLens-9-2-build-brief.md](../prompts/2026-10-05-prompt-TOOL-aEvidencedLens-9-2-build-brief.md) | journal | — |
| [2026-10-05-review-TOOL-aEvidencedLens-1-spec-audit-round1.md](../reviews/2026-10-05-review-TOOL-aEvidencedLens-1-spec-audit-round1.md) | spec-audit | TOOL-aEvidencedLens-1 TOOL-aEvidencedLens-2 TOOL-aEvidencedLens-3 TOOL-aEvidencedLens-4 TOOL-aEvidencedLens-5 TOOL-aEvidencedLens-6 TOOL-aEvidencedLens-7 TOOL-aEvidencedLens-8 TOOL-aEvidencedLens-10 TOOL-aEvidencedLens-11 |

<!-- /gen:spec-records -->

## 1. Goal

The owner ruled on 2026-10-05 that the number of spec-audit rounds is operator-adjustable and that an
agent never decides it: the kit default of one round binds unless the human owner changes it. Today
nothing stops an unattended run from committing a new `REVIEW_ROUNDS=` value into `.unattended.conf`
and landing it, so the next run is bounded by a number an agent chose. Check 19 of
`tools/unattended/check-unattended.sh` already refuses the same shape for the `may:` grant: a run's own
commit that writes owner-held authority. This unit adds the round bound to that check, over the same
definition of a run's own commits.

## 2. Scope (IN)

- **S1** — `read_rounds_of`, beside `read_may_of`, reads a `.unattended.conf` blob and prints the
  EFFECTIVE round bound: the value of the LAST `REVIEW_ROUNDS=` line, because the driver sources the
  conf and the last assignment wins, with surrounding quotes, a trailing ` # comment`, trailing
  whitespace and a CR stripped; or, when no such line exists or the last one is empty, the driver's `REVIEW_ROUNDS_DEFAULT`, read from `$DRIVER`. A comment
  line spelling the key is not an assignment. Observed by AC1.
- **S2** — `scan_round_writes`, beside `scan_grant_writes`, takes commit ids on stdin and prints
  `<commit> <old> <new>` for each commit whose effective bound differs from the effective bound at
  EVERY one of its parents. It reads candidates with one `diff-tree --stdin` over the list restricted
  to `.unattended.conf`, then settles each by `read_rounds_of` at the commit and at each parent, as
  `scan_grant_writes` settles a grant. A merge that took one parent's value wrote nothing. Observed by
  AC1 and AC2.
- **S3** — Check 19 runs `scan_round_writes` over the SAME commit list it hands `scan_grant_writes`,
  the `maycs` range per recorded state, and re-scans after the terminal walk's exclusions exactly when
  the grant scan does: one walk, read once, serves both scans. A hit is
  `fail 19` naming the commit, the old and new bound, the run-state file, and that the round bound is
  the owner's, set by an owner commit outside a run. No second definition of a run's commits is
  written. The fail line and the clause header cite the owner's ruling by its record, the run
  mandate `memory/builds/aEvidencedLens/prompts/2026-10-05-prompt-TOOL-aEvidencedLens-1-0-run-mandate.md`
  decision 4, since no decision row holds it. Observed by AC3.
- **S4** — The clause's own header comment states what it does NOT check: an edit committed outside
  any run, a preflight `--waive`, a value set by a shell construct other than a `REVIEW_ROUNDS=`
  assignment line, a second file the conf sources, a change in the driver's `REVIEW_ROUNDS_DEFAULT`
  itself, and an uncommitted working-copy edit the driver sources for the current run, which raises
  that run's bound and leaves no commit to read. It also states that the comparison is
  effective-value, and the history that makes it so (§8 F1). Observed by AC4.
- **S5** — Check 2's comment above its count reader and its two messages that call a row carrying
  `highs` and `minors` a closing-review row name such a row by its counts, on any subject. Check 2's
  reader already keys on the counts and never on the subject; after `TOOL-aEvidencedLens-7` a spec
  subject's terminal row carries them too. No existing reading changes. Observed by AC5.
- **S6** — `tools/unattended/check-unattended.test.sh` gains arms for S2, S3 and S7, on the shape of
  its grant-write fixture: a run commit raising the bound on a live and on a terminal record, an
  owner commit on the default branch raising it, the run branch merging that owner commit, and a
  post-cutoff countless and folded spec row. NOT OBSERVED inside the pass, because shared
  invariant 9 keeps suites out of passes; the `New arm:` lines in §7 declare them.
- **S7** — Check 2 reads `SPEC_COUNTS_CUTOFF` from `$DRIVER` with `core_of`, as it reads
  `FOLD_CUTOFF`, and names an unreadable value inside check 2 as that one does. In a record whose
  first-commit date (`rv_fc`, the date `FOLD_CUTOFF` is compared against) is on or after it, a
  terminal row on a subject that is not the build slug, its exit one of `CONVERGED`,
  `NON-CONVERGENT`, `CEILING` and `BOUNDED`, fails check 2 when it carries no `highs` and `minors`
  counts or records `disposition fold`. A record first-committed before it keeps today's reading.
  Observed by AC6.

## 3. Non-goals (OUT)

- `REVIEW_ROUNDS` itself, its default, and the driver's reading of it. The owner holds the key and the
  default stays one round.
- Refusing the change at write time. No driver verb writes `.unattended.conf`; a run edits it with a
  file tool, which the bar sees and no verb does.
- Any other conf key. The owner's ruling names the round bound; generalising to every bound key is a
  question for the owner, not this unit.
- Check 2's reading of a counted row. It is right today (§4 Evidence); only its prose moves (S5),
  beside the one new clause S7 adds for rows past `SPEC_COUNTS_CUTOFF`.
- A cutoff for the round scan. §8 F1 says why the effective-value comparison needs none.
  `SPEC_COUNTS_CUTOFF` dates S7's rule only, and `TOOL-aEvidencedLens-7` declares it.
- A kit version bump. The main loop bumps once at the close (shared invariant 7).

### Edges

- **consumes-from** `TOOL-aEvidencedLens-7` — the spec subject's counted terminal row and the driver
  constant `SPEC_COUNTS_CUTOFF`; without the row the rewording of S5 describes a writer that never
  writes a counted spec row, and without the constant S7 has no date to read and names it unreadable.
- **hands-off** `TOOL-aEvidencedLens-14` — the TRIGGER of S3's terminal walk. S3 walks only when the
  grant scan hits, so a round write in the unwalked superset, such as an owner raise merged into the
  run before its witness, reds an archived record for ever; that unit walks on either scan's hit and
  observes the excluded-commit case (round-1 spec audit, id 37, HIGH).

## 4. Design

### Evidence

Read at base `028b5cac`, which is `origin/main` at preflight; the run branch's later commits touch only
`memory/builds/aEvidencedLens/`.

- `scan_grant_writes` at `tools/unattended/check-unattended.sh:1633` reads one `diff-tree --stdin -r -p
  --cc` restricted to build READMEs, then settles each candidate by `read_may_of` at the commit and
  every parent, so a merge taking one side's line wrote nothing.
- Check 19's grant-write arm at `:2352` to `:2430` builds `maycs` with `read_run_commits` per recorded
  state: a live record to `HEAD` excluding the advertised tip, a terminal record from its witness,
  scanned over the superset first and walked through `read_run_exclusions` only on a hit.
- The driver sources `.unattended.conf` and reads the bound through
  `read_bound_key REVIEW_ROUNDS "$REVIEW_ROUNDS_DEFAULT"` (`tools/unattended/unattended.sh:811`), with
  `REVIEW_ROUNDS_DEFAULT=1` at `:384`, unquoted, so the leg's `core_of`, which reads only a quoted
  `KEY="…"` line, cannot read it; `read_rounds_of` reads that line itself.
- HISTORY, MEASURED 2026-10-05: `git log -S'REVIEW_ROUNDS' -- .unattended.conf` names one commit,
  `c117d0007` (`TOOL-aProbedUnit-6`), which ADDED `REVIEW_ROUNDS="1"`. `aProbedUnit`'s run-state file
  is `LANDED` with base `1b000d1a` and witness `5493495a`, and
  `git merge-base --is-ancestor` places `c117d0007` inside that range. A raw line comparison would red
  that archived, append-only record on every bar for ever; the effective bound before it was the
  default of 1 and after it is 1, so the effective comparison settles it as no write.
- Check 2: its count reader at `:734` to `:737` keys on `highs` and `minors` being present and never on
  the subject; the comment at `:727` says the counts are written "on the build-slug subject terminal
  round only" and that "every spec-audit row" carries neither, and the messages at `:794` and `:801`
  say "closing-review". `grep -rn "closing-review row carrying counts"` over `tools/` finds no reader
  of those messages outside the leg.

### Data model

```text
scan_round_writes  stdin: <commit>\n...   stdout: <commit> <old-bound> <new-bound>\n...
read_rounds_of     arg: conf blob text    stdout: rounds=<effective bound>
```

```text
check 19 fail: a commit among a run's own commits changes the effective REVIEW_ROUNDS bound in
.unattended.conf, and the round bound is the owner's, set by an owner commit outside any run -
commit and bound follow: <sha> <old> -> <new>, run <run-state file>
```

### Inventory

| Name | Cell | Kind |
|---|---|---|
| `read_rounds_of` | `sh.function` | new function |
| `scan_round_writes` | `sh.function` | new function |

Both were checked with `python tools/lexicon/lexicon.py --suggest <name> --as sh.function` and
answered OK.

### Files touched (estimate)

- `tools/unattended/check-unattended.sh`
- `tools/unattended/check-unattended.test.sh`

### Alternatives rejected

- **A raw line comparison with a cutoff key.** It needs a new `.unattended.conf.example` key, which
  check 22 joins and every adopter receives, to grandfather one historical commit the effective-value
  rule settles without one.
- **Attributing a commit by its `Pass:` trailer.** A run can omit the trailer; `maycs` is derived from
  the recorded range, which the run cannot edit without check 9 or check 15 seeing it, and it is the
  definition the grant scan already trusts.
- **A new check number.** Check 19 is "a run's own commits write owner-held authority"; a second number
  would duplicate its range logic or call into it, and check-arms discovers a branch by its literal
  number either way.

## 5. Production-readiness checklist

- security — the clause narrows what a run can land; it reads git objects only and writes nothing.
- perf / scale — one `diff-tree --stdin` per record over the commit list already built, plus a `git
  show` per candidate and parent; the candidate set is commits touching one file.
- error / empty / loading states — an empty range is already announced by check 19's report line; an
  unreadable blob at a parent reads as absent, so its bound is the default and a raise still reds.
- observability — the fail line names the commit, both bounds and the record.
- risks — a run commit setting the key to the value the default already gives passes, by design: it
  changes no bound. The header says so.
- testing — the function fixture and the leg fixture of §6, observed RED before the clause lands.
- migration — none; the one historical write settles as no change (§4 Evidence).
- user docs — the clause header and the fail line cite the run mandate record as the ruling's
  provenance (S3). No protocol row moves in this build.

## 6. Acceptance criteria

The function-level criteria extract `read_rounds_of` and `scan_round_writes` from
`tools/unattended/check-unattended.sh` with `sed -n '/^read_rounds_of()/,/^}/p;/^scan_round_writes()/,/^}/p'`
into a scratch script that defines `GIT() { git "$@"; }` and `DRIVER` beside them. The fixture
repository is `git init` under a short directory beneath `%TEMP%`.

- **AC1** — When `read_rounds_of` reads a conf blob holding `REVIEW_ROUNDS="1"`, `REVIEW_ROUNDS=2` on a
  later line, and `# REVIEW_ROUNDS=9`, it prints `rounds=2`; with `DRIVER` pointed at a scratch
  driver whose line reads `REVIEW_ROUNDS_DEFAULT=3`, reading a blob with no assignment it prints
  `rounds=3`, the default that driver declares.
  Red when: the first assignment wins, a comment counts, an absent key reads as empty, or the
  default is hard-coded rather than read from `$DRIVER`.
- **AC2** — When `scan_round_writes` reads, in the fixture, a commit raising `REVIEW_ROUNDS="1"` to
  `"2"` it prints that commit with `1 2`; a commit adding `REVIEW_ROUNDS="1"` where none was it prints
  nothing; and a merge whose second parent carries the raised value and whose result keeps it prints
  nothing.
  Red when: a raise is missed, the kit-default addition reads as a write, or a merge taking one side
  reads as a write.
- **AC3** — When `bash tools/unattended/check-unattended.sh` runs over a scratch fixture repository
  holding a live run-state file and one run commit raising the bound, built as the check suite's
  grant-write fixture builds its records, it fails check 19 naming that commit and `1 -> 2`; when the
  raise is instead an owner commit on the fixture's default branch merged into the run branch, check
  19 names no round write. When the run-state file is instead TERMINAL, its base..witness range
  holding a run commit that raises the bound, check 19 fails naming that commit and `1 -> 2`, and
  the fail line names the run mandate record.
  Red when: the clause does not fire on the run's own commit, on a live or a terminal record, or
  fires on the owner's.
  cost: building the fixture mirrors the suite's grant-write recipe, a minute or two by hand.
- **AC4** — When `scan_round_writes` is fed `c117d0007` in this repository, it prints nothing; and
  `grep -n "does NOT check" tools/unattended/check-unattended.sh` prints the clause's header line
  naming an edit outside a run and a `--waive`, and the header names an uncommitted working-copy
  edit.
  Red when: the one historical write reds an archived record, or the header states no limit.
  fixture: `c117d0007` is in this repository's history today.
- **AC5** — When `grep -c "closing-review row carrying counts" tools/unattended/check-unattended.sh`,
  `grep -c 'closing-review subject(s)'` and `grep -c 'build-slug subject terminal round only'` run
  over that file, each prints 0, and check 2's comment names a row by its counts on any subject.
  Red when: the old message, the `:794` message or the `:728` comment survives.
- **AC6** — When check 2's awk program, extracted as `TOOL-aEvidencedLens-7` §4 Evidence extracted
  it, grades with `SPEC_COUNTS_CUTOFF` set to a date before the record's first commit a row
  `review · item S1 · reason verdict CLEAN · blockers 0 · CONVERGED · disposition fold`, and
  separately `review · item S1 · reason verdict CLEAN · blockers 0 · CONVERGED`, each is named; with
  the cutoff after the first commit, neither is named; and the row
  `review · item S1 · reason verdict CLEAN · blockers 0 · CONVERGED · highs 0 · minors 0` is named
  under neither cutoff.
  Red when: a post-cutoff countless or folded spec row passes, or a pre-cutoff record is re-graded.
  fixture: the first-commit date is the extracted program's `rv_fc` input, set by hand.

## 7. Gates

`unattended kit gate` · `unattended skill wiring` · `spec tokens (a spec's own names resolve)`

New arm: tools/unattended/check-unattended.test.sh · a run commit raising `REVIEW_ROUNDS`, which the base leg passes · none
New arm: tools/unattended/check-unattended.test.sh · an owner raise merged into the run branch, which a scan reading the first-parent diff would red · none
New arm: tools/unattended/check-unattended.test.sh · a terminal record whose range holds a run commit raising the bound, which a live-only fixture never reaches · none
New arm: tools/unattended/check-unattended.test.sh · a post-cutoff countless and a post-cutoff folded terminal spec row, which the base check 2 passes · none

## 8. Open questions

- **F1 — Is a change the RAW `REVIEW_ROUNDS=` line or the EFFECTIVE bound?** The brief says "changes
  the `REVIEW_ROUNDS=` line". Read raw, `c117d0007` inside `aProbedUnit`'s landed range reds an
  append-only record for ever, and the only repair is a cutoff key an adopter would inherit. Read as
  the effective bound, that commit changed nothing, a respelling such as `1` to `"1"` changes nothing,
  and every change in the number the driver applies still reds. The owner's rule is about the number.
  RESOLVED (agent, 2026-10-05, delegated): the effective bound, S1 and S2, measured against the
  history in §4 Evidence.
- **F2 — How is a commit "a run's"?** The brief names two definitions, a `Pass:` trailer or membership
  in a recorded run's range, and says to reuse the grant scan's. That scan uses the range.
  RESOLVED (agent, 2026-10-05, delegated): the range, the same `maycs` list, S3.

## 9. Revision log

- rev-1 · 2026-10-05 · initial draft, from the spec brief's unit 9, the owner's 2026-10-05 ruling and
  check 19 read at `028b5cac`.
- rev-2 · 2026-10-05 · §3 §5 §7 S3 S4 S6 S7 AC1 AC3 AC4 AC5 AC6 · round-1 spec audit fold. Id 17
  (MEDIUM): AC1 reads the default from a scratch driver declaring 3. Id 18 (MEDIUM): AC3 adds the
  terminal-record case; its excluded-commit half rests on the walk trigger and is
  `TOOL-aEvidencedLens-14`'s. Id 41 (MEDIUM): S4's header names the uncommitted working-copy edit.
  Id 47 (MEDIUM): the §5 hand-off to unit 11 is dropped, and S3 cites the run mandate record as the
  ruling's provenance. Id 19 (LOW): AC5 greps the `:794` message and the `:728` comment. For
  `TOOL-aEvidencedLens-7`'s id 46 fold, S7 and AC6 add check 2's `SPEC_COUNTS_CUTOFF` clause and the
  §3 consumes-from edge names the constant. §3 gains the hands-off edge to `TOOL-aEvidencedLens-14`,
  the unit id 37 (HIGH) was promoted to.
- rev-3 · 2026-10-05 · S1 · build pass. S1 now strips a trailing ` # comment` and reads an
  EMPTY last assignment as the default, because the driver sources the conf and `read_bound_key`
  takes an empty value as unset; the raw reading would have called `REVIEW_ROUNDS=""` a change from 1.

## 10. Reuse audit

The seam extended is check 19's grant-write arm in `tools/unattended/check-unattended.sh`: its
`maycs` range per recorded state, its superset-then-walk order and its two-stage settle, which
`scan_round_writes` copies in shape and `read_rounds_of` mirrors from `read_may_of`. No second range
definition is written; the new scan is called on the list the grant scan already holds.
`python tools/codebase-map/reuse_lookup.py` prints `unscanned layers: .sh`, so it cannot see this
seam; it was found by grepping `scan_grant_writes` and reading check 19. The recall query's top hit
was `TOOL-dDerivedDocket-19`, the ruling and spec that built the grant-write arm ("no run commit may
write one"), which this unit extends to a second owner-held value. `TOOL-aProbedUnit-6`, which made
`REVIEW_ROUNDS` a tracked conf key so that a change "leaves a diff behind", did not rank; it was found
by `git log -S` (§4 Evidence), and its comment at `tools/unattended/unattended.sh:810` is the property
this clause reads.

Recall terms used: `python tools/memory-recall/query.py "what stops an unattended run from changing owner-held conf keys like the review round bound" --terms "REVIEW_ROUNDS owner grant may scan_grant_writes check 19 run commits read_run_commits unattended.conf authority"`
