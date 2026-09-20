# TOOL-aBlindedTrial-2 — the driver reads `spec-audit:` from the build README and owes the audit only when it is declared

**Status:** INPROGRESS · rev-1 · 2026-09-20 · node a · Tier-2 · base b7dee206 · streams tooling · order 1 · ratified 2026-09-20

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

Make the pre-code spec audit opt-in for an unattended run: `tools/unattended/unattended.sh` reads a
`spec-audit: <<date>>` key from the build README at the pinned BASE, pins it as a run fact, and
its `specs-audited` Definition-of-Done grader reports "not owed" with an announced line when the key
is absent — the trial in `TOOL-aBlindedTrial-1` measured no quality the audit buys on one-context
units at 12× the tokens, and the owner ruled it opt-in on 2026-09-20.

## 2. Scope (IN)

- S1 — `check_authorization()` gains one awk arm reading `^spec-audit:` from the README blob at
  BASE beside `authorized-by:` (`unattended.sh:1466-1477`), into `AUTH_SPEC_AUDIT`; a present value
  that is not `<date>` is a refusal with its own `fail` branch and `hit` arm. Observed by AC1,
  AC5.
- S2 — preflight pins `set_fact "$rel" spec-audit "$AUTH_SPEC_AUDIT"` only when declared, guarded
  for idempotence like the recipe facts (`unattended.sh:2836-2841`). Observed by AC2.
- S3 — the `specs-audited)` grader (`unattended.sh:3750`) gains a term zero before its README-region
  read: no `spec-audit` fact → `DOD_OUT="specs-audited — not owed: the spec audit is opt-in …"` and
  `return 0`, the `pieces-complete` shape at `:3308-3318`. Its header comment and the `:3796`
  message drop "MUST-by-default". Observed by AC3, AC4.
- S4 — preflight prints one `unattended: spec-audit — …` line before `preflight OK`
  (`unattended.sh:2869`): `opted in by README spec-audit: <date>` or `not owed (opt-in)`, and when
  not owed and the build has two or more roster units or any spec grades FORKED, a second clause
  recommends the key. Observed by AC6.
- S5 — the MUST-by-default comment (`unattended.sh:455-458`) gains one sentence pointing at
  `TOOL-aBlindedTrial-6`; `check-pass-order.sh:21`'s `specs-audited` gloss follows. Observed by AC7.
- S6 — `SKILL.template.md:96`'s directive gloss reads "the spec audit that precedes code, when the
  build declares it", the harness bullet (`:577-590`) tells the caller to read the preflight line
  and pass `specAudit`, `PROTOCOL.template.md` §4's `specs-audited` row gloss follows, both renders
  regenerate, and `KIT_UNATTENDED_VERSION` moves 1.24 → 1.25 in every paired carrier. Observed by
  AC8.
- S7 — `unattended.test.sh`'s `specs-audited` block (`:5557-5602`) keeps its existing arms green by
  declaring the key in their fixture, and gains the not-owed arm and the declared arm. Observed by
  AC3, AC4.

## 3. Non-goals (OUT)

- `DOD_CORE` and `DIRECTIVES_CORE` are not edited: removing a member moves `CORE_FLOOR` and
  `DIRECTIVES_FLOOR` in every adopter's committed conf and the protocol's count word — M3's veto 2.
- No new `.unattended.conf` key. A project-wide default is a follow-up; the per-build key is the
  owner's instrument.
- `--review` is untouched: it records rounds and never invokes the harness.
- The harness's `specAudit` arg is `TOOL-aBlindedTrial-3`; the hook's refusal is
  `TOOL-aBlindedTrial-4`; the method text is `TOOL-aBlindedTrial-5`.

### Edges

- **hands-off** `TOOL-aBlindedTrial-3` — the caller passes `specAudit` from the preflight line; the
  harness owns the OFF branch.
- **hands-off** `TOOL-aBlindedTrial-4` — the same key, same date shape, read from the worktree
  README by the hook; this unit reads it at BASE.
- **hands-off** `TOOL-aBlindedTrial-5` — M4's text says when the audit is owed.

## 4. Design

### Data model

One front-matter key on the build README: `spec-audit: <date>`. Read at BASE (`GIT show
"$base:$rel"`), so a working-copy edit does not opt a live run in — the same provenance property
`authorized-by:` has. Pinned once as the run fact `spec-audit`; `fact "$rel" spec-audit` is the
single read everything downstream makes.

### Inventory

- `AUTH_SPEC_AUDIT` — shell variable, set in `check_authorization()`.
- fact key `spec-audit` — the protocol lists facts as "the driver's `set_fact` keys", so no closed
  set moves.
- one new `fail <N>` branch for a malformed value; `N` is the next free code, with a `hit` arm.
- `print_spec_audit_line` — a shell function leading with a declared lexicon verb, printing S4's
  line; no `verb_`/`dod_` prefix (the offender pin is shrink-only).

### Files touched (estimate)

`tools/unattended/unattended.sh` · `tools/unattended/unattended.test.sh` ·
`tools/unattended/SKILL.template.md` · `tools/unattended/PROTOCOL.template.md` ·
`.claude/skills/unattended/SKILL.md` · `memory/guides/UNATTENDED-PROTOCOL.md` ·
`tools/unattended/check-pass-order.sh` (comment) · every `KIT_UNATTENDED_VERSION` carrier
(`check-kit-versions.sh` pairs them) · `memory/map/features/unattended.md` prose.

### Alternatives rejected

- Removing `specs-audited:machine` and `specs-reviewed:M4` from the core sets: adopter-breaking by
  construction (two floor pins per adopter), plus a `DIRECTIVES_EXTRA_TABLE` obligation for any
  project re-adding the directive. Same behaviour is available with zero floor edits.
- A conf key `SPEC_AUDIT_MODE`: the MUST-by-default ruling forbids a conf key that relaxes a
  directive; a per-build declaration carries a date and lives in the mandate.

## 5. Production-readiness checklist

- security — N/A, a read of a committed key at BASE; a run cannot author it
- perf / scale — one awk arm and one fact read; nothing measurable
- error / empty / loading states — absent key = not owed (announced); malformed key = refusal by
  name; the README missing at BASE is already `check_authorization`'s refusal
- observability — the preflight line and the DoD line are the two places a reader learns the state
- risks — two readers of one key (BASE here, worktree in the hook), stated in both READMEs
- testing — arms in `unattended.test.sh`, run alone (the full suite is 13600 s and not on the bar)
- migration — none; an absent key is today's silence with a line added
- user docs — the Skill and protocol renders

## 6. Acceptance criteria

- **AC1** — When a build README at BASE carries `spec-audit: 2026-09-20` and `bash
  tools/unattended/unattended.sh --preflight <slug>` runs, `--status` shows the fact `spec-audit`
  with that date.
  Red when: the key is committed on the run branch only and the fact is still set.
- **AC2** — When `--preflight` runs twice on the same declared build, the fact is written once.
  Red when: the second preflight fails or duplicates the row.
- **AC3** — When a CLOSED unit's build has no key and `--close` runs, stdout carries
  `specs-audited — not owed` and does not carry `a CLOSED unit is named by no tracked spec-audit
  record`.
  Red when: the close blocks on `specs-audited`, or the skip is silent.
- **AC4** — When the key is declared at BASE, a CLOSED unit has no `spec-audit` record and `--close`
  runs, stdout carries `a CLOSED unit is named by no tracked spec-audit record` and the close blocks.
  Red when: a declared build closes without the audit.
- **AC5** — When the key reads `spec-audit: later`, `--preflight` refuses with the new `fail`
  branch's text, and the driver suite carries a `hit` arm on that text.
  Red when: a non-date value pins a fact or is read as absent.
- **AC6** — When `--preflight` runs on an undeclared build with two roster units, stdout carries
  `unattended: spec-audit — not owed (opt-in)` and the recommendation clause; on a declared build it
  carries `opted in by README spec-audit:`.
  Red when: the line is absent, or the recommendation prints for a one-unit build with no fork.
- **AC7** — When `grep -n TOOL-aBlindedTrial-6 tools/unattended/unattended.sh` runs, it names the
  comment block at the MUST-by-default ruling, and `grep -c MUST-by-default` on the `specs-audited`
  grader's message is 0.
  Red when: the ruling comment still reads as unconditional.
- **AC8** — When `bash tools/unattended/check-unattended.sh` and `bash tools/check-kit-versions.sh`
  run after the renders, both exit 0 and every `KIT_UNATTENDED_VERSION` carrier reads 1.25.
  Red when: a template and its render disagree, or one carrier is left at 1.24.

## 7. Gates

`unattended kit gate` · `unattended skill wiring` · `harness arms (fail branches armed or pinned)` · `kit version markers` · `lexicon naming predicates` · `install-prefix (shipped surface)` · `kickoff-manifest ratchet`

New arm: `tools/unattended/unattended.test.sh` · the `specs-audited` block, key absent then present at BASE · none

## 8. Open questions

- **F1 — core-set removal or term zero.** RESOLVED (agent, 2026-09-20, delegated): term zero. The
  removal fails M3's veto 2 (a change to every adopter's governance carrier); the term zero is the
  `pieces-complete` shape already in the file.
- **F2 — where the hook reads the key.** RESOLVED (agent, 2026-09-20, delegated): the worktree,
  because the hook guards the attended path where the owner has just written it; the driver reads
  BASE for provenance. Both READMEs state the pair.

## 9. Revision log

- rev-1 · 2026-09-20 · initial draft from the scout of `unattended.sh` at b7dee206.

## 10. Reuse audit

Probe: `tools/codebase-map/reuse_lookup.py "read a build README front matter key at the pinned base and pin it as a run fact"` returned no candidate in the layer this
unit edits — it reports `unscanned layers: .sh` and resolves no `.js` symbol either — so the seam below
was found by reading the source, not by the probe. The seam is `unattended.sh`'s own announced-skip precedent: the `pieces-complete|set-checks-recorded`
term zero at `:3308-3318` keyed on the pinned `mode` fact, and `check_authorization()`'s awk over the
README blob at BASE for `authorized-by:`. Both are extended, neither duplicated. Recall terms used:
spec audit specs-audited DoD term zero announced skip preflight fact authorized-by README BASE
directive MUST-by-default opt-in.
