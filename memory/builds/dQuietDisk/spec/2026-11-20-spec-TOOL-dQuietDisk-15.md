# TOOL-dQuietDisk-15 — a kit self-test leg is held where gov's attestation matches the vendored bytes

**Status:** SPECCED · rev-1 · 2026-11-20 · node d · Tier-2 · base 59e882af · streams tooling · order 4

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-20-build-TOOL-dQuietDisk-1-agent-ledger.md](../build/2026-11-20-build-TOOL-dQuietDisk-1-agent-ledger.md) | journal | TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-6 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-9 TOOL-dQuietDisk-10 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-16 TOOL-dQuietDisk-17 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19 TOOL-dQuietDisk-26 TOOL-dQuietDisk-28 |
| [2026-11-20-prompt-TOOL-dQuietDisk-1-brief.md](../prompts/2026-11-20-prompt-TOOL-dQuietDisk-1-brief.md) | research | TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-6 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-9 TOOL-dQuietDisk-10 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-16 TOOL-dQuietDisk-17 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19 |
| [2026-11-20-prompt-TOOL-dQuietDisk-1-spec-brief.md](../prompts/2026-11-20-prompt-TOOL-dQuietDisk-1-spec-brief.md) | research | TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-6 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-9 TOOL-dQuietDisk-10 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-16 TOOL-dQuietDisk-17 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19 |
| [2026-11-22-prompt-TOOL-dQuietDisk-1-pins-task.md](../prompts/2026-11-22-prompt-TOOL-dQuietDisk-1-pins-task.md) | research | TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-6 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-9 TOOL-dQuietDisk-10 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-16 TOOL-dQuietDisk-17 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19 TOOL-dQuietDisk-26 |

<!-- /gen:spec-records -->

## 1. Goal

An adopter re-proves gov's kit self-tests whenever its bar runs them, though the kit's bytes change
only at an upgrade. TOOL-dQuietDisk-14 carries gov's attestations in the receipt `govkit` writes. This
unit adds `attested` as a selection source beside `quarantine` and `level` in `verdict_flow.py
select`: a kit self-test leg is held when an attestation in the receipt names it and the vendored
bytes the bar grades are the attested bytes. An unknown hash, a missing or unreadable attestation,
or an edited vendored file runs the leg as today. The switch `verdict.attested` turns the source off.

## 2. Scope (IN)

- **S1** — `derive_attested_rows(ctx)` joins `SELECT_SOURCES` as `("attested", derive_attested_rows)`,
  and `"attested"` joins `SELECTION_SOURCES`. It reads the receipt `.governance/install.json` at R. For
  each attestation, it recomputes the digest from the attestation's own `sources`. It requires every
  pair `(source, gov_oid)` to match a receipt row carrying that `source` and that `gov_oid`, and the
  blob at R of each such row's `path` to equal the row's `oid`. When all of that holds, it emits one
  row per leg the attestation names that the manifest at R carries, with the note
  `<kit> <digest[:12]>`. Observed by AC1 and AC3.
- **S2** — No receipt at R, a receipt that is not JSON, no `attestations` key, a digest that does not
  recompute, a pair no row matches, or a row whose blob at R differs, emits no row for that
  attestation, and one `said` line names which. Observed by AC2.
- **S3** — `verdict.attested` is read at R like the other selection keys. `hold`, the default, is
  S1. `run` emits no `attested` row, which is today's behaviour. Its catalogue row lands in
  `tools/policy/catalogue.toml` with `owner = "dQuietDisk"`, a `summary` and a `usage`, and
  `help/reference/policy.md` is re-rendered from it. Observed by AC4.
- **S4** — The runner's `HOLD_SOURCES` gains `attested`. Before it holds a leg by an `attested` row,
  it runs `verdict_flow.py attested --tree --note <note>` once per distinct note. That verb re-derives
  the match of S1 against the WORKING TREE: the receipt as it stands, and each attested path's blob
  by one `git hash-object --stdin-paths`. A note that does not match there is ignored with the line
  `selection — <leg> held by attested, but <why>, ignored: it runs`, and the leg runs. Observed by
  AC2 and AC5.
- **S5** — A leg held by `attested` prints `GATE held  <leg>  (attested, <note>)`, writes its
  `held.<n>` key with source `attested`, and is counted in a fourth held tally, `attested`, on the
  summary line beside `kit`, `quarantine` and `level`. Observed by AC1.
- **S6** — `tools/run-gates/README.md`'s "Held by policy" section names the source, the switch, the
  four ways a leg still runs, and that an adopter's bar holds by it only when the bar is run with
  the selection record `verdict_flow.py select` writes. Observed by AC6.
- **S7** — `memory/guides/SESSION-KICKOFF.md` re-stamps `last-audit` in the commit that lands S4,
  since `tools/run-gates/run-gates.sh` is on its `watch:` line. Observed by AC7.

## 3. Non-goals (OUT)

- No edit to any adopter. incms `scripts/gov-bar.sh` and nicocares `scripts/nc-bar.sh` exec the
  vendored runner with no selection record (read at incms `b4850abfb` and nicocares `bb2e6543`), so
  neither bar holds by `attested` until its owners pass one. That wiring is theirs, under their own
  governance.
- No second selection program and no hold outside `select` and the runner's existing source join.
- No attestation writer: TOOL-dQuietDisk-14's.
- No change to the `kit` source or to `GATE_SELFTESTS`. A leg held by `attested` is held whatever
  `GATE_SELFTESTS` says, as `quarantine` and `level` legs are, since the attestation is the run.

### Edges

- **consumes-from** `TOOL-dQuietDisk-14` — the receipt's `attestations` key, its digest rule and the
  leg names it carries. Without it no row is emitted and every leg runs as today.
- **consumes-from** external — dWitnessedBar's landed tip, which holds `verdict_flow.py`'s `select`
  (TOOL-dWitnessedBar-5) and the runner's source join; and, for an adopter, a minted run-gates kit
  version carried by `govkit update`, since incms's vendored runner predates `verdict_flow.py`.

## 4. Design

### Why adopters run gov's kit self-tests today

Read at incms `b4850abfb` and nicocares `bb2e6543`, read-only. incms's `scripts/gov-bar.sh` derives
a manifest from `scripts/run-gates/gate-legs.json` and execs `scripts/run-gates/run-gates.sh`;
nicocares's `scripts/nc-bar.sh` does the same over `scripts/gate-legs.json`. Neither sets
`GATE_SELFTESTS`, and neither adopter's `.githooks/gate-env.sh` does. So their 13 `subject: kit`
legs are already held on a default bar by the runner's `kit` source
(`tools/run-gates/run-gates.sh#derive_hold_source`), and run only under `GATE_SELFTESTS=1` or
`changed`.

What runs on every adopter bar is the three hook self-tests, `push-main self-test`,
`pre-push self-test` and `pre-push bar self-test`. Their emitted rows read `"subject": "repo"` in
both adopters. incms emitted them at `cb7bce859` on 2026-10-07, when gov declared them `repo`. gov's
descriptor declares all three `subject = "kit"`
(`tools/govkit/entries/push-main.kit.toml@609cd40b1:73`), and govkit emits the descriptor's subject
(`tools/govkit/govkit.py@609cd40b1:4315`). So a `govkit update` that re-emits those rows holds them
by `kit` with no change in this build; that is recorded for the adopters' upgrade sessions.

This unit is what holds a kit leg on the runs that DO ask for kit self-tests, `GATE_SELFTESTS=1` and
`changed`, and on the three hook legs once re-emitted, when gov has attested the bytes.

### Why the runner checks the working tree too

`select` reads every input at R (`tools/run-gates/verdict_flow.py#derive_selection`), and the
pre-push hook re-derives a selection at the remote's tip
(`.githooks/pre-push@609cd40b1:1789`), so a branch cannot hold a leg its own change breaks. An
attestation is different from a quarantine: it claims something about the bytes being graded. A
selection derived at a tip where the kit was unedited would hold the leg over a push that edits it.
So S4 re-derives the match over the bytes the bar actually grades, through the same function S1
uses, with a working-tree blob reader in place of the R reader. A mismatch drops the hold, which is
the safe direction, and `select --check` still compares rows as today.

### One matcher, two readers

`check_attestation(att, rows, blob_at)` is the one predicate. `blob_at(path)` is `git ls-tree` at R
in `select` and `git hash-object --stdin-paths` over the working tree in the `attested` verb. Each
reader is one git process for the whole set.

### Inventory

| Minted identifier | Kind | Naming cell | Graded by |
|---|---|---|---|
| `attested` | a word of `SELECTION_SOURCES` and `HOLD_SOURCES` | none | AC1 |
| `verdict.attested` | policy key, values `hold` and `run` | the catalogue's row | AC4 |
| `attested` | a `verdict_flow.py` verb, `--tree --note <note>` | none | AC5 |
| `derive_attested_rows`, `check_attestation` | functions in `verdict_flow.py` | none | AC1, AC5 |
| `HELD_ATTESTED` | the runner's fourth held tally | none | AC1 |

### Files touched (estimate)

`tools/run-gates/verdict_flow.py` · `tools/run-gates/run-gates.sh` · `tools/run-gates/README.md` · `tools/policy/catalogue.toml` · `help/reference/policy.md` · `memory/guides/SESSION-KICKOFF.md` (its `last-audit` re-stamp)

### Alternatives rejected

| Alternative | Why it loses |
|---|---|
| Hold in the runner by reading the receipt itself | A second selection program beside `select`, which the brief and TOOL-dWitnessedBar-5 rule out. |
| Derive `attested` rows from the working tree in `select` | Every input of `select` is read at R, and `select --check` would then disagree with itself. |
| Hash the vendored kit directory as one tree | govkit renders kit literals at the install prefix, so the adopter's tree is not gov's; the receipt's per-row `oid` and `gov_oid` are what both ends hold. |

## 5. Production-readiness checklist

- security: an attestation can only HOLD a leg the manifest carries; a forged receipt row is caught
  by the blob compare, and a forged digest by the recompute. The safe direction on every failure is
  to run.
- perf / scale: one `ls-tree` in `select`, one `hash-object` per distinct note in the runner.
- error / empty / loading states: S2's six cases each emit no row and say which.
- observability: the `GATE held` line, the `held.<n>` key and the fourth tally (S5).
- risks: a held leg over edited bytes. S4's working-tree check is the defence, and AC2 and AC5
  plant both edits.
- testing: verdict_flow's own fixtures (AC1 to AC5) on an adopter fixture.
- migration: none; a receipt without the key holds nothing.
- user docs: `tools/run-gates/README.md` (S6) and `help/reference/policy.md` (S3).

## 6. Acceptance criteria

- **AC1** — When the run-gates kit's verdict_flow.py runs `--fixture attested`, it builds an adopter
  with govkit's fixture factory `build_target`, installs a kit, writes a matching attestation
  into its receipt, runs `select --rev HEAD` and then the runner with that selection, and reads the
  kit's leg as `GATE held` with `(attested, ` and a summary tally of `1 attested`.
  Red when: a matching attestation does not hold the leg.
- **AC2** — When the same fixture runs its four negative cases, an unknown digest, a receipt with no
  `attestations` key, a committed edit to one vendored file, and an uncommitted edit to one vendored
  file, the leg runs in each, and the last case prints the runner's `ignored: it runs` line.
  Red when: any of the four holds the leg.
- **AC3** — When `select --check` runs over the AC1 run record at the same R, it exits 0.
  Red when: the recorded selection and its re-derivation disagree.
- **AC4** — When the fixture's policy sets `verdict.attested = "run"`, `select` writes no `attested`
  row and the leg runs; and `python tools/policy/policy.py get verdict.attested` prints `hold` with no
  policy file.
  Red when: the switch does not restore today's behaviour, or the default is not `hold`.
- **AC5** — When verdict_flow.py's `attested --tree --note <note>` runs in the
  fixture after a vendored edit, it exits 1 and names the path whose blob moved; on the unedited tree
  it exits 0.
  Red when: the working-tree reader agrees with R after an edit.
- **AC6** — When `grep -c 'attested' tools/run-gates/README.md` runs, it prints 3 or more, inside the
  "Held by policy" section.
  Red when: the README does not say when an adopter's bar holds by the source.
- **AC7** — When `bash skills/session-kickoff/manifest-check.sh --staged` runs over the commit landing
  S4, it exits 0.
  Red when: the watched runner moves without the re-stamp.
- **AC8** — When `python tools/govkit/govkit.py check --target C:/projects/incms/main` and the same for
  `C:/projects/nicocares/main` run read-only from gov before and after this unit, each prints the same
  lines and exits the same.
  Red when: an adopter's check reading moves.
  permission: both targets are read and never written; nothing runs in either `gov-upgrade` worktree.

## 7. Gates

`run-gates canary` · `policy check` · `policy fixtures` · `scratch-guard self-test` · `routed-commits selftest` · `kickoff-manifest ratchet` · `recall floor` · `recall floor arms` · `line length` · `spec tokens (a spec's own names resolve)`

New arm: tools/run-gates/verdict_flow.py · covers AC1 AC2 AC5 · the `--fixture attested` cases on an adopter fixture; the failing case is staged by skipping the blob compare, which holds the leg over the committed edit, and by skipping the working-tree check, which holds it over the uncommitted one · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-20 · initial draft. Ordered 4, not the brief's 2: this unit writes
  `tools/run-gates/run-gates.sh`, which TOOL-dQuietDisk-5 writes at order 2, and re-stamps
  `memory/guides/SESSION-KICKOFF.md`, which TOOL-dQuietDisk-6 re-stamps at order 3.

## 10. Reuse audit

The seam extended is `verdict_flow.py`'s `SELECT_SOURCES` table and `SELECTION_SOURCES`
(`tools/run-gates/verdict_flow.py#derive_selection`), TOOL-dWitnessedBar-5's selection, as the brief
requires, and the runner's source join `derive_hold_source`
(`tools/run-gates/run-gates.sh#derive_hold_source`). The receipt rows' `oid` and `gov_oid` are the
hash both ends hold, which TOOL-dQuietDisk-14 chose. The chain build owning the area is dWitnessedBar
(Test: held legs); this unit adds a source beside its two and contradicts none of its rules.

`python tools/codebase-map/reuse_lookup.py "hold a kit self-test leg when its vendored bytes are attested"`
returned `resolve_kit_dir` and name-token neighbours. No existing seam fits beyond the selection
table. Recall returned TOOL-aBenchedProbe-1 and -2, which moved the hook self-tests to `kit`,
DEPL-aBenchedProbe-5, TOOL-dWitnessedBar-5's reuse scout, and this build's README. The source agreed;
the adopters' stale `repo` rows are what the aBenchedProbe change has not yet reached.

Recall terms used: attestation kit self-test held subject kit selection source quarantine level vendored hash adopter
