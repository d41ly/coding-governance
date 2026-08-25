# TOOL-dFramedEntrypoint-12 — the dead-path waiver registry keys on line TEXT, not line NUMBER

**Status:** SPECCED · rev-1 · 2026-08-25 · node d · Tier-2 · base 60ba1d60 · order 2 · streams tooling

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

`tools/dead-path-waivers.txt` keys each waiver on `<path>:<line>`, so any insertion above a waived
hit unpins it and reds the bar for a reason unrelated to the change. It happened twice inside one
build. The owner ruled the key becomes the surrounding line's TEXT, which survives the failure that
actually occurs and breaks only on rewording.

## 2. Scope (IN)

- **S1** — the waiver row grammar becomes `<path>\t<line-text>\t<reason>`: the path, the exact text
  of the line carrying the waived mention, and the reason. The line NUMBER leaves the key entirely.
- **S2** — `tools/check-dead-paths.sh` matches a hit by comparing the offending line's text to the
  row's, after normalising leading and trailing whitespace and nothing else. A row whose text matches
  no line in that file is STALE and reds, which is the property the current keying already has and
  must not lose.
- **S3** — an AMBIGUITY refusal: if a row's text matches more than one line in its file, the row is
  refused rather than silently waiving both. Line numbers were unique by construction and text is
  not, so the property has to be asserted instead of inherited.
- **S4** — the existing rows are MIGRATED, each keeping its reason verbatim and gaining the text of
  the line it currently points at. The migration is mechanical and its diff is reviewable line by
  line.
- **S5** — arms for: a matching row, a stale row, an ambiguous row, an insertion above a waived hit
  (which must now be a no-op), and a REWORDING of a waived line (which must red).

## 3. Non-goals (OUT)

- No change to which mentions are waived. The population is identical before and after; only the key
  changes.
- No change to the three waiver CLASSES the file's header declares, nor to its shrink-only rule.
- No re-keying of any OTHER registry. `memory/project/` holds several and they have their own
  keyings and their own failure modes; this ruling names one file.
- No attempt to make the key survive rewording too. That needs a content hash or a stable marker in
  the source line, and both are heavier than the failure they would prevent.

## 4. Design

### Data model

Three tab-separated fields per row. Tab-separated rather than space, because a line's text contains
spaces and a reason contains spaces, and a two-space-delimited grammar would be ambiguous the first
time a waived line ended in whitespace. Comment lines keep the leading `#` convention this file
already uses — and, unlike the slot-limits file, no waived line here begins with `#` in a way that
collides, but the checker uses "a line with no tab is a comment" anyway, because that is the rule the
memory-tree kit settled on after this exact class bit it twice.

### Inventory

Four rows today, all naming `tools/memory-tree/check-memory-hygiene.test.sh`, plus the header. Each
becomes one migrated row.

### Migration

One commit. Every row is rewritten and the checker changes with them; a half-migrated file matches
nothing and would red every row as stale, so the two halves cannot be split.

### Alternatives rejected

**Key on PATH alone.** The keying `adopt-memory-tree.sh`'s own comment recommends, and immune to
line drift. Rejected by the owner: a file carrying several waived mentions would get one waiver
covering all of them, which is wider than the fault and hides the next one.

**Leave it line-keyed.** Rejected. It cost this repo two cycles in one build, and the second re-key
was first performed by proximity and scrambled three rows onto the wrong reasons — a failure the
keying invites rather than merely permits.

### Files touched (estimate)

`tools/check-dead-paths.sh` · `tools/dead-path-waivers.txt` · the checker's arms · the kit version
sites if the checker belongs to a versioned kit.

## 5. Production-readiness checklist

- security — N/A.
- perf / scale — one string comparison per hit instead of one integer comparison; the population is
  four rows.
- a11y — N/A.
- i18n — N/A.
- error / empty / loading states — an empty registry is legal and means nothing is waived, which is
  the file's stated fully-strict state and is unchanged.
- observability — the refusal messages name the row and the file, as they do now.
- risks — the ambiguity case is the new one, and S3 makes it a refusal rather than a silent
  double-waiver. The residual risk is a waived line being reworded, which now reds; that is
  intended, because a reworded line is a line whose waiver should be re-read.
- testing + left-shift gates — five arms, each observed RED against a staged break before it lands.
- migration / rollback — one commit, invertible; the old rows are recoverable from git.
- user docs — the file's own header states the new grammar and why the key moved.

## 6. Acceptance criteria

- **AC1** — When a row's text matches exactly one line in its file, `bash tools/check-dead-paths.sh`
  waives that mention and exits 0.
- **AC2** — When a line is INSERTED above a waived hit, `bash tools/check-dead-paths.sh` still exits
  0 with no row edited. This is the failure the ruling exists to remove, and it is staged and
  observed.
- **AC3** — When a waived line is REWORDED, `bash tools/check-dead-paths.sh` exits 1 naming that row
  as stale.
- **AC4** — When a row's text matches more than one line in its file, `bash tools/check-dead-paths.sh`
  exits 1 naming the row and the count, rather than waiving both.
- **AC5** — When a row names a file that no longer exists, `bash tools/check-dead-paths.sh` exits 1
  naming it stale, which is the property the line keying already had.
- **AC6** — When the four existing rows are migrated, `git diff` shows each keeping its reason
  verbatim, and `bash tools/check-dead-paths.sh` exits 0 on the migrated tree.
- **AC7** — When `bash tools/run-gates/run-gates.sh` runs, the `dead-path carriers` leg is green.

## 7. Gates

`dead-path carriers` · `check-arms.py` floors if the checker gains `fail` branches · `memory hygiene`
· `check-testsuite-counts.sh` if the checker's suite prints a count.

## 8. Open questions

- **F1 — is whitespace normalisation the right tolerance?** Leading and trailing only, per S2. Tabs
  inside a line are part of its text. Recommendation: as specced — a re-indent should not unpin a
  waiver, and anything wider starts matching lines the author did not mean.
- **F2 — do the other registries under `memory/project/` follow?** They have their own keyings and
  their own failure modes, and the owner ruled one file. Recommendation: no, and a second registry
  moves only when its own keying has actually failed.

## 9. Revision log

- rev-1 · 2026-08-25 · initial draft, from the owner's ruling on `dFramedEntrypoint`'s fifth park.

## 10. Reuse audit

Memory-recall terms for the regrounding read: `dead path waiver registry keyed line number text
stale row insertion unpin shrink only carriers`. The nearest seam is
`memory/project/method-carriers.txt` with `check-method-carriers.sh`, which keys on PATH alone and is
what `adopt-memory-tree.sh` recommends — deliberately NOT reused here, because the owner ruled
against the precision it loses. No existing checker in this tree matches a waiver by line text, so
this unit builds that matcher rather than extending one, and the evidence is the grep over
`tools/*.sh` for a text-keyed waiver, which returns nothing.
