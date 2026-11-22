# TOOL-dQuietDisk-15 — a kit self-test leg is held where gov's attestation matches the vendored bytes

**Status:** DEFERRED · rev-3 · 2026-11-22 · node d · Tier-2 · base c3c0811b · streams tooling · order 4 · advances TOOL-dQuietDisk-33 · ratified 2026-11-22 · deferred: section 8 F1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-20-build-TOOL-dQuietDisk-1-agent-ledger.md](../build/2026-11-20-build-TOOL-dQuietDisk-1-agent-ledger.md) | journal | TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-6 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-9 TOOL-dQuietDisk-10 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-16 TOOL-dQuietDisk-17 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19 TOOL-dQuietDisk-26 TOOL-dQuietDisk-28 TOOL-dQuietDisk-36 TOOL-dQuietDisk-37 |
| [2026-11-20-prompt-TOOL-dQuietDisk-1-brief.md](../prompts/2026-11-20-prompt-TOOL-dQuietDisk-1-brief.md) | research | TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-6 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-9 TOOL-dQuietDisk-10 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-16 TOOL-dQuietDisk-17 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19 |
| [2026-11-20-prompt-TOOL-dQuietDisk-1-spec-brief.md](../prompts/2026-11-20-prompt-TOOL-dQuietDisk-1-spec-brief.md) | research | TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-6 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-9 TOOL-dQuietDisk-10 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-16 TOOL-dQuietDisk-17 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19 |
| [2026-11-22-prompt-TOOL-dQuietDisk-1-pins-task.md](../prompts/2026-11-22-prompt-TOOL-dQuietDisk-1-pins-task.md) | research | TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-6 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-9 TOOL-dQuietDisk-10 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-16 TOOL-dQuietDisk-17 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19 TOOL-dQuietDisk-26 |
| [2026-11-22-prompt-TOOL-dQuietDisk-11-reground-task.md](../prompts/2026-11-22-prompt-TOOL-dQuietDisk-11-reground-task.md) | research | TOOL-dQuietDisk-11 TOOL-dQuietDisk-16 TOOL-dQuietDisk-26 |
| [2026-11-22-prompt-TOOL-dQuietDisk-15-1-spec-writer.md](../prompts/2026-11-22-prompt-TOOL-dQuietDisk-15-1-spec-writer.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

An adopter re-proves gov's kit self-tests whenever its bar runs them, though the kit's bytes change
only at an upgrade. TOOL-dQuietDisk-14 carries gov's attestations in the receipt `govkit` writes. This
unit adds `attested` as a selection source beside `quarantine` and `level` in `verdict_flow.py
select`: a kit self-test leg is held when an attestation in the receipt names it and the vendored
bytes the bar grades are the attested bytes. An unknown hash, a missing or unreadable attestation,
or an edited vendored file runs the leg as today. The switch `verdict.attested` turns the source off.

Whether to build it at all is fork F1: the design section measures that no bar run today would hold
a leg by it.

## 2. Scope (IN)

- **S1** — `derive_attested_rows(ctx)` joins `SELECT_SOURCES` as `("attested", derive_attested_rows)`.
  It reads the receipt `.governance/install.json` at R. For each attestation it recomputes the digest
  from the attestation's own `sources` and calls `check_attestation`. That predicate holds when every
  pair `(source, gov_oid)` has at least one receipt row carrying that `source`, every such row carries
  that `gov_oid`, and each such row's `path` holds a blob at R equal to the row's `oid`. When it holds,
  the source emits one `hold` row per leg the attestation's `legs` names that the manifest at R
  carries, with the note `<kit> <digest[:12]>`. Observed by AC1 and AC3.
- **S2** — No receipt at R, a receipt that is not JSON, no `attestations` key, an attestation whose
  digest does not recompute, a pair no row matches, or a row whose blob at R differs, emits no row
  for that attestation, and one `said` line names which of the six it was. No `said` line begins
  `release  `. Observed by AC2.
- **S3** — `verdict.attested` is read at R through `read_policy_at`, like the other selection keys,
  and the selection header names its value. `hold`, the default, is S1. `run` emits no `attested`
  row, which is today's behaviour. Its catalogue row lands in `tools/policy/catalogue.toml` with
  `owner = "dQuietDisk"`, a `summary` and a `usage`. `help/reference/policy.md` is re-rendered from
  it, and the main loop re-renders `.governance/policy.json` with `policy.py mirror --write`.
  Observed by AC4.
- **S4** — `"attested"` joins `SELECTION_SOURCES` inside the `selection_row` block, and the block's
  inline copy in `tools/drift-audit/drift_report.py` is re-synced byte-identical. That file's
  `SELECTION_HOLDS` gains `attested`, so the gate-health bar leaves out the legs the runner holds by
  it. Observed by AC5.
- **S5** — The runner's `HOLD_SOURCES` gains `attested`, and its refusal line names the three
  selection words. After the selection read and before any leg is decided, when an accepted row
  reads `attested`, the runner runs `verdict_flow.py attested --selection <the record>` once. That
  verb re-derives each `attested` row at the record header's `rev` through `check_attestation`. It
  then runs one `git diff --name-only <rev> --` over the working tree, and prints one line per row
  the diff meets: a row whose receipt paths, or `.governance/install.json`, it names. For each
  such line the runner prints `selection — <leg> held by attested, but <why>, ignored: it runs`,
  and that leg is not held. The row stays in the accepted text and in `SEL_KEYS`, so
  `select --check` still compares equal, and the leg runs in its ordinary slot with its result in
  the verdict. A verb that does not resolve, exits non-zero or prints nothing parsable leaves every
  `attested` row unheld. Observed by AC6 and AC7.
- **S6** — A leg held by `attested` prints `GATE held  <leg>  (attested, <note>)`, writes its
  `held.<n>` key with source `attested`, and is counted in a fourth held tally, `HELD_ATTESTED`,
  printed as `<n> attested` on the summary line beside `kit`, `quarantine` and `level`. It writes no
  held-tier record and joins no `GATE_SELFTESTS=changed` selection, since both read `kit` legs alone.
  Observed by AC6.
- **S7** — `tools/run-gates/README.md`'s "Held by policy" section names the source, the switch, the
  four ways a leg still runs, and that a bar holds by it only when the bar is handed the selection
  record `verdict_flow.py select` writes. Observed by AC8.
- **S8** — `memory/guides/SESSION-KICKOFF.md` re-stamps `last-audit` in the commit that lands S5,
  since `tools/run-gates/run-gates.sh` is on its `watch:` line. Observed by AC9.

## 3. Non-goals (OUT)

- No edit to any adopter. Neither adopter's runner reads a selection today, and neither bar is
  handed one (the design section), so no adopter bar holds by `attested` until a minted run-gates
  kit reaches it through `govkit update` and its owners hand their bar a selection. That wiring is
  theirs, under their own governance.
- No caller that hands a bar a selection. The README names that as the loop engine's Test step.
- No second selection program and no hold outside `select` and the runner's existing source join.
- No attestation writer: TOOL-dQuietDisk-14's.
- No change to the `kit` source or to `GATE_SELFTESTS`. A leg held by `attested` is held whatever
  `GATE_SELFTESTS` says, as `quarantine` and `level` legs are, since the attestation is the run.
- No change to `tools/lib/home_graded.py`. It answers a narrower question (the alternatives table).

### Edges

- **consumes-from** `TOOL-dQuietDisk-14` — the receipt's top-level `attestations` key as built at
  `6749bfa8d`: each entry's `kit`, `digest`, `gov_commit`, `sources` and `legs`, the digest rule
  of `tools/govkit/govkit.py#derive_kit_attestations`, and the leg names `legs` carries. Without it
  no row is emitted and every leg runs as today.
- **consumes-from** external — a caller that hands a bar `GATE_SELECTION`, which no boundary does
  today; and, for an adopter, a minted run-gates kit carrying `verdict_flow.py` and the selection
  join, carried by `govkit update`.

## 4. Design

### Where the code was read

Every gov citation is at `c3c0811b8`, by symbol or as `<path>@<blob>:<line>`. The adopters were read
read-only by `git show HEAD:<path>`: incms `C:/projects/incms/main` at `01fee8175` and nicocares
`C:/projects/nicocares/main` at `613da4a7`, on 2026-11-22. Nothing was run in either.

### What adopters run today, and what this unit could save

Each adopter's bar derives a manifest from gov's emitted legs and execs the vendored runner
(`scripts/gov-bar.sh@aa9c3aeb5d0c:34` in incms, `scripts/nc-bar.sh@864eadcc4272:23` in nicocares).
Neither bar, neither `.githooks/gate-env.sh` and neither pre-push hook sets `GATE_SELFTESTS`
(`git grep` over those files at each head finds it only in `.githooks/pre-push.test.sh`).

Rev-1 found the three hook self-tests emitted as `repo` in both adopters. They now read `kit`. Each
adopter's emitted manifest holds 19 `subject: kit` rows
[PINNED, counted 2026-11-22 at the two heads above], of 61 in incms and 133 in nicocares. The
vendored runner, the same blob in both, holds every one of them when `GATE_SELFTESTS` is empty
(`scripts/run-gates/run-gates.sh@511ed2cf19ea:3277`). So a default adopter bar already runs none of
gov's kit self-tests. The analysis's G2 row, which this unit's K4 rework answers, predates that.

That vendored runner has no `HOLD_SOURCES` and no `GATE_SELECTION` read (`git grep -c` counts 0 in
it), and neither adopter tracks a `verdict_flow.py`. In gov, no boundary hands a bar a selection:
the pre-push hook sets `GATE_SELECTION` on no path (`.githooks/pre-push@a7039aa62361:2389`), and the
README says "No caller hands a bar a selection yet" (`tools/run-gates/README.md@e9740701e93a:170`).
gov's own receipt carries no `attestations` key, so `select` in gov would emit no row either.

| Run | Kit legs run today | Held by this unit |
|---|---|---|
| default adopter bar | 0, held by `kit` | 0 |
| adopter bar under `GATE_SELFTESTS=1` or `changed` | every one, or the moved ones | 0 until its runner reads a selection and is handed one |
| gov bar | per `GATE_SELFTESTS` | 0, since no caller hands a selection and gov's receipt holds no key |

The saving is zero on every run that exists today. It becomes real only after the two external
edges: then each attested leg held under `GATE_SELFTESTS=1` saves its whole suite, the check-wiring
self-test alone measured at 3,786 git processes a run [PINNED, the analysis's G1 evidence row]. The
cost the unit adds is stated in the bound below.

### The bound

`select` gains one policy read, one `git show` of the receipt at R, and one
`git cat-file --batch-check` for every row path at R. The runner gains no process when the record
holds no `attested` row. Otherwise it gains one python process running the verb, which spends that
same `git show`, that same batch check, and one `git diff --name-only`.

### Why the runner checks the working tree too

`select` reads every input at R (`tools/run-gates/verdict_flow.py#derive_selection`), and the
pre-push hook re-derives the record at the remote's tip, so R is often not the tree the bar grades.
An attestation is a claim about the bytes being graded, unlike a quarantine. A record derived where
the kit was unedited would otherwise hold the leg over a push that edits it.

So S5 re-derives the row at R and asks one diff whether the working tree differs from R on any path
the match read. Every such path's blob at R already equals its row's `oid`, so a path the diff does
not name holds the attested bytes in the working tree too. `git diff` compares through the tree's
clean filters, so a line-ending conversion alone names nothing. Paths are passed relative to the
top level, which avoids the ruled false fact that git refuses an MSYS `/c/...` path.

A dropped hold keeps the row in the record, because `select --check` re-derives at R, where the row
holds. Dropping it from the accepted text would make the hook refuse a push whose leg in fact ran.

### Readers of the source set

`SELECTION_SOURCES` is spelled once in the `selection_row` block
(`tools/run-gates/verdict_flow.py@b7294f80fbef:283`), and `tools/lib/resolve-python.test.sh`'s parity
table holds its one inline copy, `tools/drift-audit/drift_report.py@17f401f7bf88:73`, to it. Two more
spellings sit outside the block: the runner's `HOLD_SOURCES`
(`tools/run-gates/run-gates.sh@7848b83f22c0:3140`) with its refusal line at `:3177`, and
`SELECTION_HOLDS` (`tools/drift-audit/drift_report.py@17f401f7bf88:3722`). S4 and S5 move all four.
`git grep` for the pair over `tools/`, `.githooks/` and `skills/` finds no fifth. The runner's hold
decision (`tools/run-gates/run-gates.sh@7848b83f22c0:3517`), its two tally `case`s in `report_one`
and its summary loop at `:5864` each gain the word.

### Inventory

| Minted identifier | Kind | Naming cell | Graded by |
|---|---|---|---|
| `attested` | a word of `SELECTION_SOURCES`, `SELECTION_HOLDS` and `HOLD_SOURCES` | none | AC1, AC5, AC6 |
| `verdict.attested` | policy key, values `hold` and `run` | the catalogue's row | AC4 |
| `attested --selection <path>` | a `verdict_flow.py` verb | none | AC7 |
| `derive_attested_rows`, `check_attestation` | functions in `verdict_flow.py` | none | AC1, AC2, AC7 |
| `HELD_ATTESTED` | the runner's fourth held tally | none | AC6 |
| `attested` | a `verdict_flow.py --fixture` case | none | AC1, AC2, AC3, AC4 |

### Files touched (estimate)

`tools/run-gates/verdict_flow.py` · `tools/run-gates/run-gates.sh` · `tools/run-gates/run-gates.test.sh` · `tools/run-gates/README.md` · `tools/drift-audit/drift_report.py` · `tools/policy/catalogue.toml` · `help/reference/policy.md` (rendered) · `.governance/policy.json` (rendered, the main loop's mirror) · `memory/guides/SESSION-KICKOFF.md` (its `last-audit` re-stamp)

### Shared paths at order 4

No other order-4 unit's estimate shares a path with this one. TOOL-dQuietDisk-11 names the govkit
fixture factory, TOOL-dQuietDisk-16 the govkit engine and its step program, and TOOL-dQuietDisk-26
the check-wiring checker and its suite.

### Alternatives rejected

| Alternative | Why it loses |
|---|---|
| Hold in the runner by reading the receipt itself | A second selection program beside `select`, which the brief and TOOL-dWitnessedBar-5 rule out. |
| Derive `attested` rows from the working tree in `select` | Every input of `select` is read at R, and `select --check` would then disagree with itself. |
| Hash the vendored kit directory as one tree | govkit renders kit literals at the install prefix, so the adopter's tree is not gov's; the receipt's per-row `oid` and `gov_oid` are what both ends hold. |
| The working-tree half through `tools/lib/home_graded.py#derive_home_graded`, as TOOL-dQuietDisk-14's reuse audit proposed | It keeps only `engine` rows whose `oid` equals `gov_oid`. `EPOCH_ROLES` also attests `seed` and `rendered` rows, 17 of incms's rows are `rendered` [PINNED, counted 2026-11-22], so no kit with such a row could hold; and carrying the block would add a fourth inline copy for one hash call the diff against R does without. |
| A `git hash-object --stdin-paths` re-hash of the attested paths | It answers what one diff against R answers, once S1 has matched R's blobs to each row's `oid`. |
| Drop a refused row from the accepted selection text | The hook's `select --check --selection` would then find a row R derives missing, and refuse the push. |

## 5. Production-readiness checklist

- security: an attestation can only HOLD a leg the manifest at R carries. A forged receipt row is
  caught by the blob compare, a forged digest by the recompute, and an edit after R by the diff. The
  direction on every failure is to run.
- perf / scale: the bound in the design section; nothing per leg or per attested file.
- error / empty / loading states: S2's six cases each emit no row and say which; S5's verb failing
  clears every `attested` hold.
- observability: the `GATE held` line, the `held.<n>` key, the fourth tally and the `ignored: it
  runs` line.
- risks: a held leg over edited bytes. S5's diff is the defence, and AC2 and AC7 plant a committed
  and an uncommitted edit. The gotcha `test-oracle-read-from-a-historical-sha` applies to the record's
  `rev`, which is read for blob identity and never as a verdict. A `merged` row carries no `gov_oid`,
  so a kit attesting one never holds; that costs a saving, never a verdict.
- testing: the `attested` fixture case and a runner arm in `tools/run-gates/run-gates.test.sh`.
- migration: none; a receipt without the key holds nothing.
- user docs: `tools/run-gates/README.md` (S7) and `help/reference/policy.md` (S3).

## 6. Acceptance criteria

- **AC1** — When `python tools/run-gates/verdict_flow.py --fixture attested` runs, its first case
  builds a repository with `write_repo`, holding a manifest with one `kit` leg, a vendored file, and a
  receipt whose rows carry the key set of `tools/govkit/fixtures/adopter-ic-2cff5855.receipt.json` and
  whose `attestations` entry names that leg. It runs `select --rev HEAD` and reads one row
  `held · <leg> · attested · <kit> <digest[:12]> · hold`.
  Red when: a matching attestation emits no row, or a row for a leg the manifest lacks.
- **AC2** — When the same fixture runs its negative cases, a digest that does not recompute, a
  receipt with no `attestations` key, no receipt, a pair whose `gov_oid` no row carries, and a
  committed edit to the vendored file, `select` writes no `attested` row in any, and prints a `said`
  line naming each case.
  Red when: any case emits a row, or a case's line names a different cause.
- **AC3** — When the fixture runs `select --check --selection <the AC1 record> --rev HEAD`, it exits 0.
  Red when: the recorded row and its re-derivation at R disagree.
- **AC4** — When the fixture's policy sets `verdict.attested = "run"`, `select` writes no `attested`
  row and its header names the value. When `python tools/policy/policy.py get verdict.attested` runs
  with no policy file, it prints `hold`.
  Red when: the switch does not restore today's selection, or the default is not `hold`.
- **AC5** — When a probe extracts the `selection_row` block from `tools/run-gates/verdict_flow.py` and
  `tools/drift-audit/drift_report.py` with `sed -n '/>>> selection_row/,/<<< selection_row/p'`, the two
  are byte-identical after CRs are dropped, and `drift_report.read_selection_holds` over a planted
  record holding one `attested` row returns that leg.
  Red when: the copy drifts, or the gate-health bar keeps a leg the runner holds.
- **AC6** — When the canary suite's new arm, the `New arm:` line of the Gates section, hands the runner a
  selection holding one `attested` row on a fixture whose receipt matches, with the kit class asked
  for, the bar prints `GATE held  <leg>  (attested, <note>)`, the summary names `1 attested`, the
  verdict holds `held.1` as `<leg> · attested · unrun`, and the leg writes no `.leg` row.
  Red when: the leg runs, or it is counted under another source.
  permission: the main loop observes the arm red and then green at the close; the pass runs no suite.
- **AC7** — When `python tools/run-gates/verdict_flow.py attested --selection <record>` runs in the
  fixture after an uncommitted edit to the vendored file, it prints one line naming the leg and the
  path. On the unedited tree it prints no line. Under that edit the same canary arm prints
  `ignored: it runs` and runs the leg.
  Red when: the working-tree check agrees with R after an edit.
- **AC8** — When `grep -n 'attested' tools/run-gates/README.md` runs, it prints at least three lines
  inside the "Held by policy" section, naming the switch and the four ways the leg runs.
  Red when: the README does not say when a bar holds by the source.
- **AC9** — When `bash skills/session-kickoff/manifest-check.sh --staged` runs over the commit
  landing S5, it exits 0.
  Red when: the watched runner moves without the re-stamp.
- **AC10** — When `python tools/govkit/govkit.py check --target C:/projects/incms/main` and the same
  for `C:/projects/nicocares/main` run read-only from gov before and after this unit, each prints the
  same lines and exits the same.
  Red when: an adopter's check reading moves.
  permission: both targets are read and never written; nothing runs in either `gov-upgrade` worktree.
- **AC11** — When the fixture's AC1 case and the AC6 runner arm run with `GIT_TRACE2_EVENT` set to an
  empty directory, `select` spends at most three git processes more than with `verdict.attested =
  "run"`, and the runner with no `attested` row spends none more than the base runner.
  Red when: a git process is spent per attested path or per leg.
  figure: PINNED, the bound the design section promises.

No verdict moves where no attestation matches: every leg the base runner ran still runs, with the
same result.

## 7. Gates

`run-gates canary` · `run-gates gov canary` · `policy check` · `policy fixtures` · `drift-audit selftest` · `drift-audit records` · `python resolver (behaviour + inline parity + idiom ban)` · `scratch-guard self-test` · `routed-commits selftest` · `kickoff-manifest ratchet` · `recall floor` · `recall floor arms` · `docs` · `line length` · `spec tokens (a spec's own names resolve)`

New arm: tools/run-gates/run-gates.test.sh · covers AC6 AC7 · the held-by-policy block gains an `attested` row on a fixture holding `verdict_flow.py` and a matching receipt; its failing case is staged by skipping the source in the hold decision, which runs the leg, and by skipping the verb call, which holds it over the uncommitted edit · none

`tools/run-gates/verdict_flow.py`'s fixtures are driven by no gate leg: `tools/gate-legs.json` names
no `verdict_flow.py` argv. So AC1 to AC5 and AC7's verb half are direct runs of the fixture, observed
by the pass and not by the bar.

## 8. Open questions

- **F1 — Build the `attested` source, which holds no leg on any run that exists today, or retire the
  unit?**
  - (a) Build S1 to S8 as written. The source is ready when a caller hands bars a selection and the
    adopters update onto a runner that reads one. It adds up to three git processes to every
    `select` (the bound), and nine files.
  - (b) Retire the unit, `WONTDO`, with the design section's table as its reason. TOOL-dQuietDisk-14's
    key stays carried and inert. The main loop files one ask naming the two preconditions and this
    spec as the design to resume, and records in the build README's item for K4 that the adopters'
    default bars already hold their 19 kit legs.
  - (c) Defer the unit, `DEFERRED`, until a caller hands a bar a selection, with the same reason.
  - Recommendation: (b). The build measures git processes and file creates, and (a) adds one kind
    and saves neither on any run today. YAGNI forbids scaffolding for a later caller, and (c) keeps a
    live spec whose base will drift under a runner dWitnessedBar is still changing. The ask keeps the
    design findable. The resolver should weigh against this that the owner's prompt names the
    attestation hold as fix 3, and that M3 ranks the prompt's ask above YAGNI where no veto applies.
  - RESOLVED (agent, 2026-11-22, delegated): (c), defer. Both adopters' default bars already hold
    every gov kit self-test, so building now adds git processes for no saving, and (a) is out. The
    owner's prompt asked for this hold by name, so the spec stays the design to resume rather than
    being retired. Its two preconditions, something handing a bar a selection and the adopters
    updating onto a runner that reads one, are filed as ask TOOL-dQuietDisk-33.

## 9. Revision log

- rev-1 · 2026-11-20 · initial draft. Ordered 4, not the brief's 2: this unit writes
  `tools/run-gates/run-gates.sh`, which TOOL-dQuietDisk-5 writes at order 2, and re-stamps
  `memory/guides/SESSION-KICKOFF.md`, which TOOL-dQuietDisk-6 re-stamps at order 3.
- rev-2 · 2026-11-22 · §1 §2 §3 §4 §5 §6 §7 §8 §10 · S1 S2 S3 S4 S5 S6 S7 S8 · AC1 to AC11 ·
  re-grounded at c3c0811b8 (orders 1 to 3 built), under
  `2026-11-22-prompt-TOOL-dQuietDisk-11-reground-task`. What moved:
  - The saving. Both adopters' emitted hook self-tests now read `kit`, so a default adopter bar holds
    all 19 kit legs already, and no runner anywhere is handed a selection. The design section states
    a zero saving today, and F1 asks whether to build; the goal gains one sentence pointing at it.
  - The attestation as built (`6749bfa8d`): S1 now names every receipt row of a pair, and S2 the six
    causes. The `merged` row's missing `gov_oid` is a stated limit.
  - The working-tree half. Rev-1 re-hashed through `git hash-object --stdin-paths` once per note.
    It is now one verb call per bar running one `git diff --name-only` against R, and a dropped hold
    keeps its row so `select --check` stays equal. TOOL-dQuietDisk-14's proposal to extend
    `home_graded.py` is rejected in the alternatives table.
  - The source set has two more readers than rev-1 named: the `selection_row` block's copy in
    `tools/drift-audit/drift_report.py` and its `SELECTION_HOLDS`. New S4 and AC5 cover them, and
    the old S4 to S7 are renumbered S5 to S8.
  - The runner observation moved out of the fixture, since naming the runner in a criterion is
    refused. It is now a `New arm:` in the canary suite, AC6 and AC7, and AC1 builds its repository
    with `verdict_flow.py`'s own `write_repo`, since a kit imports no sibling kit. AC11 states the
    process bound, and the old AC6 to AC8 are AC8 to AC10.
  - Citations moved to blob-pinned lines at `c3c0811b8`, and the adopters' were re-read at incms
    `01fee8175` and nicocares `613da4a7`.
- rev-3 · 2026-11-22 · §8 · status DEFERRED · the run's coordinator ruled F1 as (c), defer, marked
  in place as delegated, and the header tail names F1 and ask TOOL-dQuietDisk-33, which holds its
  two preconditions. Rev-2's measurements stay as the record of why; scope, design and acceptance
  are kept as written and unbuilt.

## 10. Reuse audit

The seam extended is `verdict_flow.py`'s `SELECT_SOURCES` table and the `selection_row` block's
`SELECTION_SOURCES` (`tools/run-gates/verdict_flow.py#derive_selection`), TOOL-dWitnessedBar-5's
selection, as the brief requires, with the block's inline copy that TOOL-dWitnessedBar-62 S17 added.
The runner's side is its source join `derive_hold_source`
(`tools/run-gates/run-gates.sh#derive_hold_source`), the hold decision beside it, and its held
tallies. The R reads go through `verdict_flow.py`'s own `run_git`, `read_at` and `read_policy_at`.
The receipt rows' `oid` and `gov_oid` are the hash both ends hold, which TOOL-dQuietDisk-14 chose.
The chain build owning the area is dWitnessedBar (Test: held legs); this unit adds a source beside its
two and contradicts none of its rules.

`python tools/codebase-map/reuse_lookup.py "hold a kit self-test leg when its vendored bytes are attested"`
returned `resolve_kit_dir` and name-token neighbours at rev-1. No existing seam fits beyond the
selection table. TOOL-dQuietDisk-14's audit named `tools/lib/home_graded.py#derive_home_graded` as
the adopter-side half; it was read whole at `c3c0811b8` and answers a narrower set, as the
alternatives table says. Recall returned TOOL-aBenchedProbe-1 and -2, which moved the hook
self-tests to `kit`, and that change has now reached both adopters; DEPL-aBenchedProbe-5;
TOOL-dWitnessedBar-5's reuse scout; TOOL-dTendedCadence-1, DEFERRED, which would hand a bar a
`GATE_SELECTION`; and this build's README.

Recall terms used: attestation kit self-test held subject kit selection source quarantine level vendored hash adopter GATE_SELECTION home_graded
