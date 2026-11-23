# TOOL-dQuietDisk-16 — `govkit update` reads every gov blob through one `cat-file --batch` handle

**Status:** CLOSED · rev-4 · 2026-11-22 · node d · Tier-2 · base c3c0811b · streams tooling · order 4

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-20-build-TOOL-dQuietDisk-1-agent-ledger.md](../build/2026-11-20-build-TOOL-dQuietDisk-1-agent-ledger.md) | journal | TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-6 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-9 TOOL-dQuietDisk-10 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-15 TOOL-dQuietDisk-17 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19 TOOL-dQuietDisk-26 TOOL-dQuietDisk-28 TOOL-dQuietDisk-36 TOOL-dQuietDisk-37 |
| [2026-11-22-build-TOOL-dQuietDisk-16-1-acceptance-ledger.md](../build/2026-11-22-build-TOOL-dQuietDisk-16-1-acceptance-ledger.md) | journal | — |
| [2026-11-22-build-TOOL-dQuietDisk-16-deviation-1.md](../build/2026-11-22-build-TOOL-dQuietDisk-16-deviation-1.md) | deviation | — |
| [2026-11-20-prompt-TOOL-dQuietDisk-1-brief.md](../prompts/2026-11-20-prompt-TOOL-dQuietDisk-1-brief.md) | research | TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-6 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-9 TOOL-dQuietDisk-10 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-15 TOOL-dQuietDisk-17 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19 |
| [2026-11-20-prompt-TOOL-dQuietDisk-1-spec-brief.md](../prompts/2026-11-20-prompt-TOOL-dQuietDisk-1-spec-brief.md) | research | TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-6 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-9 TOOL-dQuietDisk-10 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-15 TOOL-dQuietDisk-17 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19 |
| [2026-11-22-prompt-TOOL-dQuietDisk-1-pins-task.md](../prompts/2026-11-22-prompt-TOOL-dQuietDisk-1-pins-task.md) | research | TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-6 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-9 TOOL-dQuietDisk-10 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-15 TOOL-dQuietDisk-17 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19 TOOL-dQuietDisk-26 |
| [2026-11-22-prompt-TOOL-dQuietDisk-11-reground-task.md](../prompts/2026-11-22-prompt-TOOL-dQuietDisk-11-reground-task.md) | research | TOOL-dQuietDisk-11 TOOL-dQuietDisk-15 TOOL-dQuietDisk-26 |
| [2026-11-22-prompt-TOOL-dQuietDisk-16-1-spec-writer.md](../prompts/2026-11-22-prompt-TOOL-dQuietDisk-16-1-spec-writer.md) | journal | — |
| [2026-11-22-prompt-TOOL-dQuietDisk-16-build-brief.md](../prompts/2026-11-22-prompt-TOOL-dQuietDisk-16-build-brief.md) | journal | — |
| [2026-11-22-review-TOOL-dQuietDisk-1-closing-diff-review-round1.md](../reviews/2026-11-22-review-TOOL-dQuietDisk-1-closing-diff-review-round1.md) | diff-review | TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-9 TOOL-dQuietDisk-10 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19 TOOL-dQuietDisk-26 TOOL-dQuietDisk-28 |

<!-- /gen:spec-records -->

## 1. Goal

`govkit update` pays two to three `git show` processes per receipt row, about 810 for a 242 to 293
row receipt (`memory/builds/dQuietDisk/build/2026-11-20-build-TOOL-dQuietDisk-19-analysis.md`, row
G4, rework K7). `tools/govkit/upgrade_steps.py#blob_at` already takes a `batch` handle that no `update` caller
passes. This unit opens one handle per `update` run and threads it to every receipt-row read the
run makes, with the same receipts, writes and printed lines.

## 2. Scope (IN)

- **S1** — `build_blob_batch(root)` in `tools/govkit/upgrade_steps.py` returns a `BlobBatch`
  handle, whose `git -C <root> cat-file --batch` process starts on the first request, through its
  `init_process()`, and stops on its `remove_process()`. The process inherits the caller's
  environment, as the spawn branch's `git show` does. `derive_introduced` builds its handle through
  it in place of its own `subprocess.Popen` line, and ends it with `remove_process()`.
  Observed by AC1 and AC5.
- **S2** — `blob_at`'s batch branch takes the process from `batch.init_process()` and reads its
  `stdin` and `stdout` as today. It tells a dead handle from a missing blob. A `missing` reply
  stays None. An end of stream or a header that does not parse answers that request through the
  spawn branch and marks the handle dead, so every later request on it is a spawn too. A path
  holding a newline is a spawn, since the protocol is line-framed. Observed by AC3.
- **S3** — `cmd_update` builds one handle through the module attribute,
  `upgrade_steps.build_blob_batch(root)`, before it calls `_cmd_update`, and calls its
  `remove_process()` in its `finally`, beside `release_write_lock()`. `_cmd_update` takes it as a
  keyword, `batch`. Observed by AC1, AC3 and AC5.
- **S4** — Every `blob_at` call inside `_cmd_update`, and every call it makes to the six readers
  below, passes `batch=batch`. The in-body sites are the schema back-fill, the S9 integrity loop,
  the `block` branch, the new-destination landing and the held new-destination test; the one
  closure is `_resolve_ver_at`. The six readers are `classify_row`, `resolve_entry_version_at`,
  `read_descriptor_at`, `read_requires_at`, `measure_rendered_rows` and `derive_attribution`. Each
  gains an optional `batch=None` keyword and passes it to its own `blob_at` calls, and
  `read_requires_at` passes it on to `read_descriptor_at`. A caller that passes nothing reads as
  today. Observed by AC1, AC2 and AC8.
- **S5** — `read_registry_at` keeps calling `blob_at` with three positional arguments, so the
  self-test stand-ins for `govkit.blob_at` still answer it. `derive_default_gained` and
  `read_registry_at` take no handle. Observed by AC6.

## 3. Non-goals (OUT)

- No handle on the TARGET. `index_blob`, the `hash-object` per rendered row in
  `measure_rendered_rows`, `check_region_only`'s `blob_at(target, "HEAD", path)`, and every
  `git -C <target>` write stay as they are. A second handle over the target's object store is a
  further saving, outside this unit's brief.
- No handle for the reads that are not receipt-row reads. `decline_findings`, which `update` calls
  for a `[[decline]]` row's `taken_as` source, and `write_install_receipt`'s
  `derive_kit_attestations`, which reads the registry and one descriptor per kit carrying a kit leg
  on each receipt write, keep the spawn branch. Both are shared with `apply`, `adopt`, `check` or
  `plan`, and both count per kit or per decline, never per row.
- No shared handle for the step readers. `derive_introduced` keeps one handle per call, so
  `read_steps`, `read_retired` and `derive_reverse_steps` are unchanged beyond S1.
- No change to `apply`, `adopt` or `check`. Their `blob_at` calls keep the spawn branch; each
  function S4 changes defaults to it.
- No `adopt-*.sh --check` change. Running it once per update is TOOL-dQuietDisk-17.
- No cache of blob bytes across runs and no policy key. The handle answers the same question in
  fewer processes and stores nothing, so the cache rule does not reach it.
- No adopter change. `tools/govkit/` is gov-internal: the registry exempts `{prefix}/govkit`, and
  `python tools/govkit/govkit.py shipped` lists neither `govkit.py` nor `upgrade_steps.py`.

### Edges

none

## 4. Design

### Where the code was read

Every citation is at `c3c0811b8`, this branch's `HEAD` with orders 1 to 3 built, by symbol or as
`<path>@<blob>:<line>`. `tools/govkit/upgrade_steps.py` is blob `45471902ac59` there, unchanged
since `59e882afd`. `tools/govkit/govkit.py` is blob `a1f80842b86e`; TOOL-dQuietDisk-14 and
TOOL-dQuietDisk-18 moved it, and `_cmd_update`'s `def` line now sits lower, by
235 lines [PINNED, read 2026-11-22 from that line at `59e882afd` and at `c3c0811b8`].

### The reads `update` makes today

`blob_at = upgrade_steps.blob_at` (`tools/govkit/govkit.py@a1f80842b86e:6888`) is read by name at
call time. `_cmd_update` (`tools/govkit/govkit.py#_cmd_update`) reaches these gov-blob reads, found
by an AST walk of every `blob_at` call and every call to a reader that makes one:

| Site | Where | Reads per run |
|---|---|---|
| schema below 3 back-fill | `tools/govkit/govkit.py@a1f80842b86e:10112` | one per row lacking `gov_oid` |
| S9 integrity | `tools/govkit/govkit.py@a1f80842b86e:10143` | one per row with `commit` and `gov_oid` |
| `classify_row` | called at `tools/govkit/govkit.py@a1f80842b86e:10770` | `theirs`, `base`, and `theirs_new` on a rename |
| `_resolve_ver_at` | closure at `tools/govkit/govkit.py@a1f80842b86e:9935` | one per written or re-measured row |
| `resolve_entry_version_at` | the per-kit version delta, `tools/govkit/govkit.py@a1f80842b86e:10938` | one per kit |
| `read_requires_at` | `tools/govkit/govkit.py@a1f80842b86e:10008`, to `read_descriptor_at` | one per claimed or gained kit |
| `read_descriptor_at` | role re-resolution, `tools/govkit/govkit.py@a1f80842b86e:10486` | one per kit when `--to` is not `HEAD` |
| `derive_attribution` | a role move under `--accept-role-moves`, `tools/govkit/govkit.py@a1f80842b86e:10549` | one per commit of the source's log |
| `block` branch | `tools/govkit/govkit.py@a1f80842b86e:10600` | two per `block` row |
| new-destination landing | `tools/govkit/govkit.py@a1f80842b86e:12083` | one per landed new destination |
| held new-destination test | `tools/govkit/govkit.py@a1f80842b86e:12202` | up to two per refused new destination |
| `measure_rendered_rows` | called at `tools/govkit/govkit.py@a1f80842b86e:13082` | one per re-measured rendered row |

Left on the spawn branch, by S5 and section 3: `derive_default_gained` at
`tools/govkit/govkit.py@a1f80842b86e:10002`, the registry read inside `read_requires_at`,
`decline_findings` at `tools/govkit/govkit.py@a1f80842b86e:13207`, and `write_install_receipt`'s
attestation reads.

`classify_row` reads two blobs for every row, the S9 loop one more, and `_resolve_ver_at` reads the
same version file once per written row of a kit. That repetition is why the analysis counts about
three spawns per row.

### The saving

The receipt at `C:/projects/nicocares/main` holds
364 rows [PINNED, read from its `.governance/install.json` on 2026-11-22],
353 of them with `commit` and `gov_oid` [PINNED, the same read].
Today an update against it spawns at least three `git show` per such row, one in S9 and two in
`classify_row`. The unit spawns one `cat-file` process for all of them, and keeps only the
registry, descriptor and decline reads of section 3 as spawns, a count fixed by its kits and
declines, never by its rows. AC2 measures the drop on the probe's fixture.

### The handle

```python
class BlobBatch:            # what build_blob_batch returns
    init_process()          # starts the process on the first call; returns the same Popen after
    dead: bool              # set by blob_at on an end of stream or a bad header
    remove_process()        # closes stdin and waits; a no-op when never started
```

`blob_at`'s batch branch keeps its write and its header parse
(`tools/govkit/upgrade_steps.py@45471902ac59:2702-2707`). S2 adds two exits before the parse, both
taken before `init_process()` is called: `batch.dead` or a newline in the path takes the spawn
branch. An empty or malformed header sets `dead` and takes it too. Today an end of stream splits to
fewer than three fields and returns None, so a dead process reads as a missing blob; that is the
defect S2 closes. A lazy start means a run refused before its first read starts no process.

### Why the bytes cannot differ

`git show <rev>:<path>` of a blob prints the blob as stored. It applies no textconv: a probe on
2026-11-20, git 2.54, configured a `diff.<driver>.textconv` on a file and `git show HEAD:f.txt`
printed the stored bytes, as `cat-file --batch` did. Both name the object by the same extended SHA-1
syntax, so an abbreviated `commit` in a receipt row resolves the same way, and an ambiguous one is
None both ways. A receipt source names a file, never a tree, so the two branches' different output
for a tree does not arise; AC4 confirms it over gov's own shipped population.

### Inventory

| Minted identifier | Kind | Naming cell | Graded by |
|---|---|---|---|
| `build_blob_batch` | Python function | `py.function`, lexicon `--suggest` OK | the probes of section 6 |
| `BlobBatch` | Python class | `py.type`, lexicon `--suggest` OK | the probes of section 6 |
| `init_process`, `remove_process` | `BlobBatch` methods | `py.function`, lexicon `--suggest` OK | the probes of section 6 |
| `batch` | keyword of `_cmd_update` and the six readers | none | AC8 |

No verb, flag, conf key, policy key or refusal number is minted. The lexicon grades a method,
a property and a dunder as a function, and `VERB_OFFENDER_PIN` is full, so the handle carries no
`stdin` or `stdout` property and no `close()`: `blob_at` reads the process `init_process()`
returns.

### Files touched (estimate)

`tools/govkit/upgrade_steps.py` · `tools/govkit/govkit.py`

The kickoff manifest's `watch:` line names neither.

### Rollout

Of the other order-4 units, TOOL-dQuietDisk-11
names `tools/govkit/fixture_target.py`, TOOL-dQuietDisk-15 names `tools/run-gates/` files and
TOOL-dQuietDisk-26 names `tools/check-wiring.sh` and its suite, so none shares a path with this one.
TOOL-dQuietDisk-17 (order 5) writes `tools/govkit/govkit.py` and TOOL-dQuietDisk-9 (order 6)
writes `tools/govkit/upgrade_steps.py`, both after it.

### Alternatives rejected

| Alternative | Why it loses |
|---|---|
| A module-level handle set by `cmd_update` | Every reader would depend on hidden state, and `apply` sharing a module with it could inherit a handle opened for another root. |
| Patching `blob_at` itself to keep a handle per root | The self-test stand-ins replace `govkit.blob_at` whole; a handle cached inside the original would outlive the stand-in and the run. |
| `tools/lib/history_store.py#BatchReader` as the handle | No govkit module imports `tools/lib/`, and every self-test scratch gov copies govkit's own files and no `tools/lib/` module into itself (`tools/govkit/selftest.py#build_gov17` among them), so an import would break each one. Its fallback is two `cat-file` spawns where `blob_at`'s is one `git show`, and it strips `GIT_ENV_LEAKS`, which the spawn branch does not. |
| `--batch-command` | It needs git 2.36, and `--batch` already answers every read here. |
| Memoising the version file per kit | It saves the same processes for one site only, while the handle covers every site. |

## 5. Production-readiness checklist

- security: no new write path. The handle reads gov's own object store, which `update` already
  reads through `git show`.
- perf / scale: one `cat-file` process per run replaces two to three `git show` per row. The count
  is AC2's.
- error / empty / loading states: a dead handle falls back to a spawn per read, so a reader failure
  costs processes, never an answer.
- observability: none added; the run prints what it printed.
- risks: the gotcha `test-oracle-read-from-a-historical-sha` was read; this unit reads blobs at the
  commits the receipt names, as today, and changes how, not which. A handle left open on an
  exception is closed by `cmd_update`'s `finally`, which already releases the write lock.
- testing: the probes of section 6.
- migration: N/A — no stored data.
- user docs: N/A — no adopter-visible change; `help/upgrade-steps.md` names no process count.

## 6. Acceptance criteria

- **AC1** — When a probe under `%TEMP%/<short-name>` builds a scratch gov in the govkit self-test's
  shape, holding an entry `demo` of at least 30 files [PINNED] with one rendered row and a version file,
  applies commit A to a target, then commits B, which edits ten files, renames one and deletes one,
  two copies of that target are moved to B with `update --target <t> --write`. One run uses the
  base `govkit.py` and `upgrade_steps.py`, and one the unit's, over the same gov commits. Then
  `.governance/install.json`, its `install.sums` sidecar, the target's tracked tree and the run's
  stdout and exit code are byte-identical between the two.
  Red when: a reader is passed a handle to another root, or a dead handle reads as missing, and a
  row's verdict moves.
  fixture: the scratch gov commits its registry, descriptors and `adopters.toml`, and keeps
  `govkit.py` and `upgrade_steps.py` out of its commits through `.git/info/exclude`, copying the
  base's or the unit's pair in per run, so both runs read the same commits.
- **AC2** — When both AC1 runs set `GIT_TRACE2_EVENT` to their own empty directory, the unit's
  directory holds at most one file whose `cmd_name` event names `cat-file` that the base's lacks.
  Every file in it whose `cmd_name` names `show` has a `start` argv reading `<commit>:<path>` for
  the registry or a descriptor the scratch registry names. Its file count is lower than the base's
  by at least the number of receipt rows.
  Red when: a site S4 names still calls `blob_at` without the handle.
  figure: DERIVED at observation; the analysis's PINNED reading is about 810 for 242 to 293 rows,
  measured 2026-11-20.
- **AC3** — When the probe's unit run replaces `upgrade_steps.build_blob_batch` with a wrapper
  that kills the handle's process after its fifth reply, the receipt, sums and tree still equal
  AC1's. A `blob_at` call on a dead handle for a missing path returns None, and one for a present
  path returns its bytes.
  Red when: an end of stream is read as `missing`.
- **AC4** — When a probe calls `blob_at(root, "HEAD", src)` with and without a handle for every
  source in the third column `python tools/govkit/govkit.py shipped` prints, every pair of answers
  is equal.
  Red when: the batch branch strips, adds or decodes a byte.
- **AC5** — When the probe runs `update --write` with the base code and with the unit's, each under
  its own `GIT_TRACE2_EVENT` directory, on a target with a dirty claimed path, both refuse at
  `demand_writable_target`, and the unit's directory holds no more `cat-file` files than the
  base's. When a run refuses after reads, every `cat-file` file in its directory holds an `exit`
  event.
  Red when: the handle starts eagerly, or a refusal leaves its process running.
- **AC6** — When `python -c` prints the source of `govkit.read_registry_at` through `inspect`, its
  `blob_at` call has exactly three positional arguments and no keyword. When the self-test's
  stand-in, `lambda _r, c, _p: ...` assigned to `govkit.blob_at`, is installed in the probe and
  `derive_default_gained` runs, it returns without a `TypeError`.
  Red when: a handle is threaded into the registry read, so the stand-in breaks.
- **AC7** — When a scratch `git clone --shared` of gov at the unit's base runs
  `python tools/govkit/govkit.py update --target C:/projects/incms/main` read-only, once with the
  base's `govkit.py` and `upgrade_steps.py` in its working tree and once with the unit's, the two
  stdouts and exit codes are byte-identical, and the same holds for `C:/projects/nicocares/main`.
  So does each target's `python tools/govkit/govkit.py check`.
  Red when: a preview line moves.
  cost: minutes per run; the analysis measured about 3.5 min for a write run.
  permission: read-only against the adopters' main checkouts, never their `gov-upgrade` worktrees.
- **AC8** — When a probe walks the AST of the unit's `tools/govkit/govkit.py`, every `blob_at` call
  inside `_cmd_update`, and every call there to the six readers S4 names, carries the keyword
  `batch`, and each of those readers passes `batch` to every `blob_at` or `read_descriptor_at`
  call in its own body. The calls in `derive_default_gained`, `read_registry_at`,
  `decline_findings` and `derive_kit_attestations` carry none.
  Red when: a site is missed, or a section 3 exclusion is threaded.

## 7. Gates

`govkit selftest` · `govkit selfcheck` · `govkit refusal join` · `govkit acceptance matrix` · `govkit runbook parity` · `recall floor arms` · `policy fixtures` · `upgrade-walk` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `line length`

The bar runs once at the close. This unit adds no suite arm.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-20 · initial draft. Order 4, not the briefed 1. `tools/govkit/govkit.py` is
  written by TOOL-dQuietDisk-14 (order 1), TOOL-dQuietDisk-17 (order 2) and TOOL-dQuietDisk-18
  (order 3), and no unit depends on this one, so it takes the first free order; order 4's other
  unit, TOOL-dQuietDisk-19, writes records only. TOOL-dQuietDisk-9 also writes
  `tools/govkit/upgrade_steps.py` and is sequenced after it.
- rev-2 · 2026-11-22 · S1 · S2 · S3 · §4 · under
  `2026-11-22-prompt-TOOL-dQuietDisk-1-divergence-task`. Every minted
  name the lexicon refused leads with a declared verb, each checked by `--suggest`: `open_blob_batch`
  is `build_blob_batch`, and the handle's `stdin` and `stdout` properties and its `close()` become
  `init_process()`, which `blob_at`'s batch branch calls for the process, and `remove_process()`.
  No criterion had the pass run a suite, a `--selftest`, a gate leg or the bar.
- rev-3 · 2026-11-22 · wording only, under `2026-11-22-prompt-TOOL-dQuietDisk-1-pins-task`. In section
  1, section 4 and section 10 the three symbol citations naming a bare basename now name
  `tools/govkit/upgrade_steps.py` and `tools/govkit/govkit.py`, and in section 6 AC1's fixture floor
  is marked PINNED as the size the spec fixes. Design, scope and acceptance unchanged.
- rev-4 · 2026-11-22 · S1 · S3 · S4 · §3 · §4 · AC1 · AC2 · AC3 · AC4 · AC5 · AC7 · AC8 · §10 ·
  re-grounded at c3c0811b8 (orders 1 to 3 built), under
  `2026-11-22-prompt-TOOL-dQuietDisk-11-reground-task`. `upgrade_steps.py` is unmoved;
  `govkit.py` moved by 235 lines [PINNED] and every citation is re-pinned to its blob. An AST walk at the
  new base corrected the site table: `_add_held` and `_write_rb_finish` read no blob, at this base
  or the old one, and the reads were the `block` branch, the new-destination landing, the held
  new-destination test, the per-kit version delta and `derive_attribution`, which S4 now names.
  Scope narrows to the brief's own words, receipt-row reads: `decline_findings` and unit 14's
  `derive_kit_attestations` stay on the spawn branch (section 3). AC2 no longer claims zero `show`
  processes, which the registry reads of S5 already broke, and grades each remaining `show` by its
  path; AC5 compares `cat-file` counts with the base's, since `derive_pending_steps` and the
  `cat-file -e` check run before the refusal; AC7 runs both codes from one scratch clone so both
  read the same gov commit; AC8 is new, the AST probe of S4. S3 names the module attribute so AC3's
  wrapper can reach it. The goal is unchanged; the saving is stated in section 4.

## 10. Reuse audit

The seam extended is `tools/govkit/upgrade_steps.py#blob_at`'s `batch` parameter, "THE ONE revision-blob reader"
by its own docstring (TOOL-dSafePassage-26 S14), and `derive_introduced`'s held process
(`tools/govkit/upgrade_steps.py@45471902ac59:1019`), whose inline `Popen` becomes the shared opener.
TOOL-dQuietDisk-1's `BatchReader` (`tools/lib/history_store.py#BatchReader`) is not used: no
govkit module imports `tools/lib/` at `c3c0811b8`, every self-test scratch gov copies govkit's own
files and no `tools/lib/` module, and `blob_at` is already the one reader every govkit call site names.

`python tools/codebase-map/reuse_lookup.py "read many git objects through one cat-file batch process"`,
re-run at `c3c0811b8`, ranked `read_text`, `read`, `git`, `run_git` and `read_git`, each a one-shot
read or spawn helper, so nothing beyond `blob_at`.
Recall returned DEPL-aLevelledCopy-1, whose `read_tree_modes` memoises one `ls-tree` per commit for
the same reason, DEPL-dRemeasuredRender-1 (`measure_rendered_rows`), and TOOL-dSafePassage-3's spec.
The owning chain build is dSafePassage (Supersession: govkit update and apply). Of its CLOSED units,
26's S14 moved `blob_at` into `upgrade_steps.py` as the reader the introducing-commit derivation
reads through, with the self-test's patching of `gk.blob_at` kept working, which S5 preserves. Unit
5 is the release-0 fixture and the walk, 10 the step gate, 25 a refused landing's cleanup and 27 the
landing's untracked snapshot; none reads `update`'s rows, so none is contradicted.

Recall terms used: govkit update blob_at batch cat-file receipt row classify_row gov_oid upgrade_steps derive_introduced show
