# TOOL-dQuietDisk-37 — the closing review's MEDIUM and LOW findings: the missing arms, the template key's builder arguments, the CR guard on batch names, and the serial runner's owned temp root

**Status:** CLOSED · rev-1 · 2026-11-22 · node d · Tier-2 · base db9670ee · streams tooling · order 9

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-20-build-TOOL-dQuietDisk-1-agent-ledger.md](../build/2026-11-20-build-TOOL-dQuietDisk-1-agent-ledger.md) | journal | TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-6 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-9 TOOL-dQuietDisk-10 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-15 TOOL-dQuietDisk-16 TOOL-dQuietDisk-17 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19 TOOL-dQuietDisk-26 TOOL-dQuietDisk-28 TOOL-dQuietDisk-36 |
| [2026-11-22-build-TOOL-dQuietDisk-37-1-acceptance-ledger.md](../build/2026-11-22-build-TOOL-dQuietDisk-37-1-acceptance-ledger.md) | journal | — |
| [2026-11-22-build-TOOL-dQuietDisk-37-deviation-1.md](../build/2026-11-22-build-TOOL-dQuietDisk-37-deviation-1.md) | deviation | — |
| [2026-11-22-build-TOOL-dQuietDisk-37-red-fix-9.md](../build/2026-11-22-build-TOOL-dQuietDisk-37-red-fix-9.md) | red-fix | — |
| [2026-11-22-build-TOOL-dQuietDisk-37-widen-22.md](../build/2026-11-22-build-TOOL-dQuietDisk-37-widen-22.md) | widen | — |
| [2026-11-22-build-TOOL-dQuietDisk-37-widen-23.md](../build/2026-11-22-build-TOOL-dQuietDisk-37-widen-23.md) | widen | — |
| [2026-11-22-prompt-TOOL-dQuietDisk-37-1-spec-writer.md](../prompts/2026-11-22-prompt-TOOL-dQuietDisk-37-1-spec-writer.md) | journal | — |
| [2026-11-22-prompt-TOOL-dQuietDisk-37-build-brief.md](../prompts/2026-11-22-prompt-TOOL-dQuietDisk-37-build-brief.md) | journal | — |
| [2026-11-22-prompt-TOOL-dQuietDisk-37-spec-task.md](../prompts/2026-11-22-prompt-TOOL-dQuietDisk-37-spec-task.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

The closing diff review of `b3f5a2bc3..879413160` converged at round 2 with five MEDIUM and four
LOW findings standing, and this unit batches eight of them. Most are verification gaps: new
behaviour whose only evidence was an uncommitted probe. This unit commits arms for the kit
attestation, the outer swept root, the TEMP/TMP export, the Python sweep, the one-diff rule, the
template race and BlobBatch's fallbacks. Three findings change behaviour. The template key folds in
the builder's arguments, `blob_at` stops sending a name holding a CR to the batch handle, and the
`--serial` self-test runner exports its owned root. Each item takes the fix the review's skeptic
judged sound, or the class-level fix the review states where the finder's fix was instance-only.

## 2. Scope (IN)

- **S1** — M1. `check_kit_attestations`, a new function in `tools/govkit/selftest.py`, called from
  `main` in its scratch-root block beside `check_receipt_schema`. It builds one scratch gov and runs
  one fixture bar in it under a held-tier selection, so the runner itself writes the
  `gate-selftest-last` record. It then calls `derive_kit_attestations` and prints seven `check`
  lines. Observed by AC1 and AC10.
  1. The runner's own record attests `demo`, whose leg row carries the declarative key `purpose`,
     and the attestation's `legs` row equals the record's `row`.
  2. The digest is the SHA-256 of the sorted `<source>TAB<oid>LF` lines that `git ls-tree -r HEAD`
     gives for the sources of `demo` and its required entry `dep`. The `legs` entry holds the
     record's `sha`.
  3. With no record file, `demo` is not attested.
  4. With the record's `row` rewritten as forty zeros, `demo` is not attested.
  5. With a `demo` source moved by a commit after the record's `sha`, `demo` is not attested.
  6. With a `dep` source moved the same way, `demo` is not attested.
  7. At a `to_commit` that is the fixture's first commit and not HEAD, the answer is `[]`.
  Each case puts the record and the tree back before the next.
- **S2** — M2, the runner's half. `tools/run-gates/run-gates.test.sh` arm 8 gains cases 8f and 8g
  on its own `build_owned_fixture` and `run_owned_bar`. The fixture gains an `env.sh` leg in its
  `fx` directory, which appends its `TEMP`, its `TMP` and `${GATE_OUTER_AMBIENT_TMP-unset}` to
  `$RG_PATHS`. Two bars run.
  The first runs under `GATE_OUTER_AMBIENT_TMP` naming a directory A, which holds three plain files
  and one dead owner whose absolute common dir names no directory. It also gets `TEMP` and `TMP`
  pointing at a decoy directory. The second runs with `GATE_OUTER_AMBIENT_TMP` naming no directory.
  Five assertions follow, and `FLOOR_ASSERTIONS` moves from 490 to 497 with S7's two [DERIVED,
  counted off the new lines]. Observed by AC3 and AC10.
  1. 8f1: the first bar prints `TMPDIR entries 3`, the count of A after its sweep.
  2. 8f2: the dead owner's directory in A is gone, and the bar announced its pid.
  3. 8f3: the leg read `GATE_OUTER_AMBIENT_TMP` as unset.
  4. 8f4: the second bar printed the `GATE_OUTER_AMBIENT_TMP names no directory` NOTE line.
  5. 8g: the leg's `TEMP` and `TMP` both name the bar's own `gate-work.*/tmp` under its ambient
     `TMPDIR`, never the decoy.
- **S3** — M2, the Python half. One arm in `tools/lib/resolve-python.test.sh` runs the resolved
  python on a short program. The program imports the canonical `tools/lib/owned_scratch.py` and
  plants six `gate-work.*` roots under a scratch ambient dir.
  | Root | Owner line | Expected |
  |---|---|---|
  | live | `py:` and the program's own pid, the common dir | kept |
  | dead-same | `py:` and a dead pid, the common dir | swept |
  | dead-other | `py:` and a dead pid, another directory that exists | kept |
  | orphan | `py:` and a dead pid, an absolute directory that does not exist | swept |
  | relative | `py:` and a dead pid, `rel/.git` | kept |
  | bash-owned | a dead pid without `py:`, the common dir | kept |
  The dead pid is a child the program started and waited for. The program calls
  `scan_dead_scratch` once and writes the surviving names and its stderr lines to a file under the
  suite's `$TMP`. Two assertions grade that file: exactly the dead-same and orphan roots are gone,
  and exactly two `owned-scratch: sweeping` lines name them. Observed by AC4 and AC10.
- **S4** — M4, the class fix. `resolve_template`, in the `template_cache_sh` block, folds its
  builder arguments into the directory key when any are passed. The fold runs after the scrub and
  before the stage and key paths are set. It replaces `_tc_k` with the `git hash-object --stdin` of
  the line `template-cache args v1`, the caller's key, and one `printf '%q'` line per argument. With
  no argument the key is the caller's, unchanged. Every later line reads the folded key, including
  the `template: <key8>` line. A failed fold says so on stderr and returns 2. Its comment line names
  the fold. The block changes in `tools/lib/template-cache.sh`, the canonical, and byte-identically
  in `tools/lib/lib-selftest.sh` and `.githooks/pre-push.test.sh`. The existing
  `template_cache_sh` parity row grades all three, unchanged. Observed by AC5 and AC6.
- **S5** — M4, the words. The canonical's header gives the argument rule in its USAGE line, its cost
  sentence and its WHAT THIS DOES NOT CHECK sentence. `build_fixture`'s comment in
  `tools/lib/lib-selftest.sh` names the arguments in the key. The KEY paragraph of
  `tools/lib/template_cache.py`'s protocol docstring states that the bash face folds builder
  arguments. It also states that the Python face takes none, so a value its `build` callable binds
  belongs in `inputs`. Observed by AC6.
- **S6** — M4, the hand fold S4 makes redundant. `build_pushed_fixture` in
  `.githooks/pre-push.test.sh` stops writing `$tmp/fx-args` and stops naming it to
  `derive_template_key`, because `resolve_template` now keys the same arguments. Observed by AC6.
  **Readers:**
  by name: `.githooks/pre-push.test.sh`, the one tracked file spelling `fx-args`.
  by value: NO VALUE READERS — the file's bytes fed only the key hash, which S4 now derives from
  the same arguments.
- **S7** — M4's arm and L2's arm, in `tools/lib/lib-selftest.test.sh`. M4 adds three assertions:
  - two `build_fixture --template "" mka x` and `mka y` batches in one cache root, where `mka`
    writes its first argument to a file, each grade their own value;
  - two direct `resolve_template` calls with one key and the arguments `x` and `y` print two
    template paths, each holding its own value;
  - a call with no argument still prints `<root>/<key>/repo`.
  L2 changes the race arm. The builder `mkr` creates a marker named for its own `$BASHPID` beside the
  root. It polls with `sleep 0.1`, for at most `300` rounds, until two markers exist, and only then
  builds. This
  barrier stands in for the fixed one-second sleep. The body prints `built <n>`, the marker count. A
  new assertion requires `built 2`, and the entries-and-nesting assertion now also requires it.
  `FLOOR_ASSERTIONS` moves from 34 to 38 [DERIVED, three for M4 and one for L2]. Observed by AC5,
  AC8 and AC10.
- **S8** — M5. Arm 3h1 of `tools/run-gates/run-gates.test.sh`: the fixture gains `gax/f`, which
  the first run moves beside `xga/f`, so the existing near-miss assertion also grades the guard
  boundary. Its label names both paths. The traced run gains two assertions. No trace line matches
  ` diff --quiet [0-9a-f]{40} -- ga/$`, so the plain guard was not diffed alone. A line matches
  ` diff --quiet [0-9a-f]{40} -- 'fx/\*\.sh'$`, so the glob guard was. The floor move is S2's.
  Observed by AC7 and AC10.
- **S9** — L1. `blob_at` in `tools/govkit/upgrade_steps.py` sends a name to the batch handle only
  where it holds neither a newline nor a CR, as `BatchReader.read_reply` does. Any other name is a
  `git show` spawn. Its docstring names the CR. Observed by AC2.
- **S10** — L1's and L3's arms. `check_blob_batch`, a new function in `tools/govkit/selftest.py`,
  is called from `main` beside S1's. Over a scratch repository holding a committed file `a`, it calls
  `upgrade_steps.blob_at` with and without a `BlobBatch` and prints six `check` lines. Observed by
  AC2 and AC10.
  1. A missing path is None both ways. The handle stays live, and its next read answers `a`'s bytes.
  2. A commit prefix naming two commit objects is None both ways, and the handle stays live.
  3. A handle whose process is a stand-in answering `<name> ambiguous` gives None and stays live.
  4. After the handle's process is killed, the next read answers the bytes `git show` gives, and
     the handle is dead.
  5. A name holding a newline is None, and a spy handle never started its process.
  6. A name `a` followed by a CR is None both ways, and a spy handle never started its process.
  The spy and the stand-in are `BlobBatch` subclasses overriding `init_process`.
- **S11** — L4. `tools/run-gates/run-selftests.sh` exports `TMPDIR`, `TEMP` and `TMP` as
  `$RS_SCRATCH` just before the `--serial` loop. The owned-root comment then says which modes run
  rows under the root: `--pooled` under `$RS_SCRATCH/s/<row>/tmp`, `--serial` under the root
  itself. `--attribute` keeps the ambient `TMPDIR`, and the comment says why. One arm in
  `tools/run-gates/run-selftests.test.sh` swaps a row's suite for `suite-tmproot.sh`. That suite
  prints `FAIL tmp-in-runner-root` when `TEMP` and `TMP` equal `TMPDIR` and `TMPDIR` is a
  `gate-work.*` directory holding an `owner` file, and `FAIL tmp-outside-runner-root` otherwise. It
  exits 1 either way. Under `--serial` the arm wants the first line. `SELFTEST_FLOOR` moves from 144
  to 145 [DERIVED, one arm]. Observed by AC9 and AC10.
- **S12** — The ledgers. Each shell file this unit edits has a row in
  `memory/project/shell-role.txt`, and five of them have rows in
  `memory/project/spawn-idiom-sites.txt` [DERIVED, read 2026-11-22]. The rows move only through
  `python tools/memory-tree/ratchet.py widen`, which the main loop runs after the pass, never by
  hand. Observed by AC11.
- **S13** — The adopters. The push-main kit ships `.githooks/pre-push.test.sh` as engine. The
  run-gates kit ships `tools/run-gates/run-selftests.sh` as engine, and
  `tools/run-gates/run-gates.test.sh` and `tools/run-gates/run-selftests.test.sh` as project-owned.
  Each kit's version moves at the mint, never by hand, and reaches nc, ic and swydee only through
  `govkit update`. Observed by AC12.

## 3. Non-goals (OUT)

- No M3. Its arms belong in `tools/unattended/check-pass-order.test.sh` and
  `tools/unattended/check-brief-recorded.test.sh`. Those are unattended-kit suites that the owner's
  standing rule of 2026-08-23 forbids this run to run, so no pass or close could see them RED and
  GREEN. The main loop filed it as ask TOOL-dQuietDisk-39 with the review's fix.
- No review left-shift gate. Each is a separate mechanism: the OWED-line close rule (M1, M2), the
  two checklist entries (M3, M4), the shared `batch_safe_name` predicate (L1), the sleep-in-a-racer
  scan (L2), the `upgrade_steps.py` fail-branch rule (L3) and the per-mode TMPDIR arm (L4). S11's
  arm is that last gate's `--serial` case only.
- No CR guard in `derive_kit_attestations`'s `--batch-check` request, which filters `"\n"` alone.
  It is the same class as L1, but an arm cannot plant it on this host. A source path holding a CR
  would have to be a file in a kit descriptor's survivors, and NTFS refuses a CR in a file name.
  The class fix is the shared predicate above, which the main loop owes as an ask. A wrong answer
  there costs an attestation that no bar reads until TOOL-dQuietDisk-15, which is DEFERRED.
- No arm for `init_owned_tempdir`'s root-making branch. It makes a root only where no ancestor of
  the ambient temp dir is an owned `gate-work.*`. When the python resolver suite runs inside a bar,
  every directory it can make sits under the bar's `$WORK`, so the branch cannot be reached
  deterministically. S3 arms `scan_dead_scratch`, the face that deletes directories.
- No change to `scan_dead_work`, `scan_dead_scratch`, the outer-root block or the TEMP/TMP export
  of `tools/run-gates/run-gates.sh`. M2 judged them right and unarmed.
- No change to the Python face's key. Its `resolve_template` takes no builder arguments
  (`tools/lib/template_cache.py@63ffe62be6ee:180`), so S5 states the rule and changes no code.
- No export under `--attribute` (section 4, "L4").
- No kit version bump by hand. `govkit.py mint` writes every owed bump at the lander.

### Edges

- **consumes-from** external — the template block as TOOL-dQuietDisk-7 built it and
  TOOL-dQuietDisk-36 scrubbed it, `derive_kit_attestations` as TOOL-dQuietDisk-14 built it,
  `BlobBatch` as TOOL-dQuietDisk-16 built it, the owned root as TOOL-dQuietDisk-9 built it, and
  the moved list as TOOL-dQuietDisk-5 built it, all landed at the base. Each spec is CLOSED and
  frozen, so it carries no edge back, and this unit changes their code and arms in place
- **hands-off** external — M3, filed as ask TOOL-dQuietDisk-39; the review's left-shift gates and
  the derive_kit_attestations CR guard, which the main loop files as asks

## 4. Design

### Where the code was read

Every citation is at `db9670ee`, this run's `HEAD`. The review cites older blobs, and
TOOL-dQuietDisk-36 has since changed the template block, so its line numbers do not apply here.

| File | Blob |
|---|---|
| `tools/govkit/govkit.py` | `69a249216283` |
| `tools/govkit/selftest.py` | `b69edc6594ea` |
| `tools/govkit/upgrade_steps.py` | `36c4b7407b33` |
| `tools/lib/template-cache.sh` | `4a40e3df96d6` |
| `tools/lib/lib-selftest.sh` | `77fa654a6ae8` |
| `tools/lib/lib-selftest.test.sh` | `70bb317cd691` |
| `.githooks/pre-push.test.sh` | `e5acad442a90` |
| `tools/run-gates/run-gates.sh` | `d35d666e1720` |
| `tools/run-gates/run-gates.test.sh` | `aa765343ae95` |
| `tools/run-gates/run-selftests.sh` | `df2db1252591` |
| `tools/run-gates/run-selftests.test.sh` | `c5faeaebb0a5` |
| `tools/lib/owned_scratch.py` | `17ab60b2af34` |
| `tools/lib/resolve-python.test.sh` | `f2ef74ebbbd7` |

### M1, the attestation arms

`tools/govkit/govkit.py#derive_kit_attestations` hashes a leg row as
`sha1(json.dumps(row less DECLARATIVE_LEG_KEYS, sort_keys=True))`. It reads the keys from the
`run-gates` descriptor's home, where `held_halves.py` lives. The runner hashes the row with the same
expression inside its manifest program (`tools/run-gates/run-gates.sh@d35d666e1720:3112-3113`). It
writes `sha` and `row` to `<common dir>/gate-selftest-last/<name key>` only after a first-attempt
green under a non-empty selection on a clean, unmoved tree (`:6034-6053`). Two copies of one
expression, with nothing comparing them, are the review's drift risk. So S1's first check reads a
record the runner wrote, never one the arm wrote. A row carrying `purpose` makes the check fail if
either side hashes the whole row while the other leaves the key out.

The fixture is TOOL-dQuietDisk-14's AC1 shape, which its ledger observed by a session-scratch
probe. `build_scratch_gov_kit` (`tools/govkit/selftest.py`, inside `main`) is the closest committed
shape: a registry naming entries and each entry's `kit.toml`. The scratch gov holds:

- `govkit.py`, `upgrade_steps.py` and `adopters.toml` in the govkit directory, as
  `build_scratch_gov_kit` copies them, and a registry naming `demo`, `dep` and `run-gates`;
- `demo`, with one engine source and a `[[gate_leg]]` of `subject = "kit"`, which requires `dep`;
- `dep`, with one engine source and no leg;
- `run-gates`, whose home holds `run-gates.sh`, `gate-profiles.txt`, `gate-fingerprint.sh` and
  `held_halves.py`, copied from gov, the runner files `build_owned_fixture` in the canary suite
  copies, plus `held_halves.py`;
- the manifest at the tool root, `gate-legs.json`, where both the runner
  (`tools/run-gates/run-gates.sh@d35d666e1720:424`) and `resolve_tool_path` look. It holds the
  `demo` leg row, with an `argv` that exits 0 and a `purpose`.

The fixture has two commits, so S1's seventh check has a commit that is not HEAD. The bar runs from
the scratch gov's root with the selection set to `1`, the full mode, the minimal profile, no
turnstile and no wall. Its environment has every inherited `GATE_` name and the twelve
`GIT_ENV_LEAKS` names cleared, the way `run_owned_bar` clears the scoping names. The bar must exit 0
and leave the record. Otherwise the first check fails, naming the bar's output, and the six after
it grade nothing.

### M2, the outer root, the export and the Python sweep

The outer block reads `GATE_OUTER_AMBIENT_TMP` once
(`tools/run-gates/run-gates.sh@d35d666e1720:2410-2416`). Naming a directory, it becomes
`RG_SWEPT_TMP`, which the sweep and the `TMPDIR entries` count read. Naming none, it prints the
NOTE. Either way it is unset before any leg. The export is `:2491`. Arm 8 already owns a committed
fixture, a bar helper that clears the scoping names, and private ambient dirs
(`tools/run-gates/run-gates.test.sh@aa765343ae95:3344-3510`). Cases 8f and 8g sit after 8e and
before the arm's final `rm -rf "$OS"`.

Each assertion of S2 reds on one break:

| Case | Break that reds it |
|---|---|
| 8f1 | the count reads the inner ambient, which holds only this bar's own dir, so it prints 1 |
| 8f2 | the sweep reads the inner ambient, so the dead owner in A survives |
| 8f3 | the `unset` line is dropped, so the leg reads A |
| 8f4 | the NOTE branch is dropped |
| 8g | `TEMP` and `TMP` leave the export, so the leg reads the decoy |

The dead owner uses the orphan form: a dead pid and an absolute common dir under `$OS` that is
never created. That way the case does not depend on how the runner spells this repository's
common dir. The pid is 999993, distinct from every other planted pid in the suite. A leg's bash
reads `TEMP` and `TMP` exactly as its runner exported them. A native child gets the Windows
spelling of the same path. Both were measured on 2026-11-22 with bash 5.3.9 [PINNED]. So 8g
compares the leg's bash values with the pattern `"$amb"/gate-work.*/tmp`.

The Python sweep, `tools/lib/owned_scratch.py#scan_dead_scratch`, sweeps a `py:` owner whose pid
is provably dead and whose common dir is this one's, or an absolute directory that does not exist
(`tools/lib/owned_scratch.py@17ab60b2af34:136-145`). The python resolver suite already holds the
parity rows for that module's three blocks
(`tools/lib/resolve-python.test.sh@f2ef74ebbbd7:448-450`). It already resolves a real python as
`$REALPY`, and its `tools/lib/` guard covers the module. The arm runs in a child program, because
`scan_dead_scratch` prints to stderr and the arm reads a file rather than a captured variable. A
child the program started and waited for is dead to `read_pid_alive`. On Windows, `OpenProcess`
succeeds while `Popen` holds the handle, and `GetExitCodeProcess` answers an exit code other than
259. Elsewhere, `os.kill` raises `ProcessLookupError` once the child is reaped. Each staged break
reds a row of the S3 table: the `py:` test dropped sweeps the bash-owned root, the `isdir` test
dropped sweeps dead-other, and the `isabs` test dropped sweeps relative.

### M4, the key that ignores builder arguments

At the base, `resolve_template` runs its builder with every argument after the key
(`tools/lib/template-cache.sh@4a40e3df96d6:63`). It names its directory by the caller's key alone
(`:57`). Every caller passes arguments:

| Caller | Arguments | Resolves per run |
|---|---|---|
| `build_fixture --template` (`tools/lib/lib-selftest.sh@77fa654a6ae8:197-198`) | the builder's own | once per batch |
| `mk_repo` (`tools/run-gates/run-gates.turnstile.test.sh@4a8a14cdf361:366-367`) | `.` | once per builder, two builders [DERIVED, counted 2026-11-22] |
| `build_pushed_fixture` (`.githooks/pre-push.test.sh@e5acad442a90:364-368`) | the tree half and its arguments, also folded by hand into `fx-args` | once per distinct argument list, memoised in `FX_MEMO` |

So the key cannot live with the callers: a direct `resolve_template` caller would stay unkeyed,
which is why the skeptic judged the finder's fix instance-only. S4 puts it in `resolve_template`
itself:

```bash
resolve_template() ( # <root> <key> <builder> [<arg>...] -> <root>/<key>/repo, <key> folding the args; built once per root
  remove_git_env_leaks
  local _tc_r=$1 _tc_k=$2 _tc_l _tc_n; shift 2
  if [ "$#" -gt 1 ]; then
    _tc_k=$({ printf 'template-cache args v1\n%s\n' "$_tc_k"; printf '%q\n' "${@:2}"; } | git hash-object --stdin) \
      || { echo "template-cache: the key of $1's arguments could not be derived" >&2; return 2; }
  fi
  local _tc_dir="$_tc_r/$_tc_k" _tc_s="$_tc_r/.stage-$_tc_k-$BASHPID"
  ...                                   # today's body, unchanged
)
```

`printf '%q'` puts each argument on one line with its newlines quoted, so two argument lists never
give one text. The fold runs inside the subshell after `remove_git_env_leaks`, so it inherits
TOOL-dQuietDisk-36's scrub. Its `git hash-object` discovers the repository from the caller's
directory, as `derive_template_key`'s does. So both keys take the object format of that directory,
40 hex in gov.

The cost is one `git hash-object` per `resolve_template` call carrying arguments, on a build or a
reuse alike. A call without arguments spends nothing more. That is two processes per turnstile run,
and one per distinct argument list in the pre-push and harness suites, because each caller memoises
its template. A fold in pure bash would cost no process. It loses because it puts a second hash
function beside git's in a block three files carry. Every key stays the same for a call with no
arguments, so the cost probe of TOOL-dQuietDisk-36 (`tools/lib/lib-selftest.test.sh` arm `tcost`)
reads as before.

S6 then retires the pre-push suite's hand fold. Keeping it would leave one fact keyed twice. Its
`cd "$tmp"` stays, because it keeps `derive_template_key`'s repository discovery away from the
caller's directory.

### M5, arm 3h1

A plain guard is answered from a slice of `base.moved`. Any other guard falls back to `changed()`,
which runs `git diff --quiet "$BASE" -- <guards>`
(`tools/run-gates/run-gates.sh@d35d666e1720:599`, `:3557-3573`). The fallback gives the same skip
or run answer, so arm 3h1's answers alone cannot tell the two paths apart. The trace can.
`GIT_TRACE` prints a plain guard bare and a glob guard in single quotes. Measured on 2026-11-22 with
git 2.54.0.windows.1 [PINNED]: `git diff --quiet <sha> -- ga/` and `git diff --quiet <sha> --
'fx/*.sh'`. The traced run (`tools/run-gates/run-gates.test.sh@aa765343ae95:1527-1532`) runs with
`GATE_BASE=HEAD`, so its base is forty hex and both guards are decided in it. Forcing
`check_plain_guard` to return 1, or dropping `write_guard_slices`, makes the absent line appear. The
review's staged break is the first.

The `gax/f` fixture grades the slice's boundary. Under the guard `ga/`, a slice that compared only
`length(g)` bytes would match `gax/f` and print `ok    dir guard` where the arm wants `skip`.

### L1 and L3, `blob_at` and BlobBatch

The batch branch's guard is `"\n" not in name` (`tools/govkit/upgrade_steps.py@36c4b7407b33:2734`).
`BatchReader.read_reply` guards both (`tools/lib/history_store.py@40eeb4d4fa2e:481`). Measured on
2026-11-22 with git 2.54.0.windows.1 [PINNED]: `cat-file --batch` answers `HEAD:a` followed by a
CR with `a`'s blob, and `git show` exits 128 for the same name.

The `ambiguous` reply cannot be reached through any name `blob_at` forms. `blob_at` always asks for
`<commit>:<path>`. Measured the same day, `cat-file --batch` answers `missing` for every such name
whose commit part is ambiguous, whether the prefix names two blobs or two commits. The forms
`<p>:a`, `<p>:`, `<p>^{commit}:a`, `<p>^{tree}:a` and `<p>~0:a` were tried. Only a bare `<p>`
answered `ambiguous` [PINNED]. So S10 checks two things. Its second check is the real case: two
commits sharing a 4-hex prefix give None both ways, and the handle stays live. Its third check
reaches the branch through a stand-in.

The second check's two commits are made in-process. The arm searches `hashlib.sha1` over
`commit <len>\0tree <HEAD tree>\nauthor ...\n\nm<i>\n` until two bodies share a 4-hex prefix, then
writes both with `git hash-object -t commit -w --stdin`. That search took 246 tries in the probe
[PINNED, measured 2026-11-22]. The arm bounds it at 100000 and fails naming the bound when no pair
is found. The fixture repository is made with `--object-format=sha1`, so the search hashes what git
stores.

The fourth check kills the handle's process with `Popen.kill` and `wait`. The next request's write
or read then fails, `blob_at` marks the handle dead, and it answers through `git show`. Every
handle is stopped with `remove_process` before the scratch root goes.

### L2, the race

The race arm's only overlap is the builder's `sleep 1`
(`tools/lib/lib-selftest.test.sh@70bb317cd691:246-257`). A second racer that forks after the first
has written `ready` returns `reused` and never builds. A barrier holds the first builder until the
second has entered, so both are building at once. The first rename wins, and the second meets the
`mv -T` collision this arm exists for. The markers sit beside `$TMP_RACE`, never inside it, so the
`entries 1` count is unchanged. Staged red: the builder without its barrier, with the second
background call started two seconds after the first, prints `built 1`.

### L4, the serial runner's owned root

The comment says every row's TMPDIR, TEMP and TMP sit under the owned root
(`tools/run-gates/run-selftests.sh@df2db1252591:1035-1036`). Only the `--pooled` launch sets them
(`:1701`). The `--serial` loop (`:2407`) and the two `--attribute` evals (`:2272`, `:2323`) run
rows with the ambient TMPDIR.

The task asks for the review's first option where it holds without a new temp entry, and for the
comment narrowed where it does not. It holds for `--serial` and not for `--attribute`.

- `--serial`: exporting the three names as `$RS_SCRATCH` itself makes no entry, because the root
  exists and holds its `owner` record. Python rows then nest in it through `resolve_owned_work`.
  Bash rows' template caches find it through `resolve_template_root`'s walk. Every row's scratch is
  removed by the runner's EXIT trap. The `--serial` stdout and exit are unchanged, which the
  `ATTR_BASE` parity arm of `tools/run-gates/run-selftests.test.sh` pins.
- `--attribute`: an L run and an R run grade two revisions. `resolve_template_root` takes the
  nearest owned `gate-work.*` ancestor, so both sides under one root would share one template
  cache. The key leaves out a builder's helpers (`tools/lib/template-cache.sh@4a40e3df96d6:23-24`),
  so R could reuse a template L built with other helpers and report a wrong baseline. Keeping the
  sides apart needs two new owned roots, each a new temp entry. So `--attribute` keeps today's
  ambient, and the comment says so and why.

The export reuses the runner's own root rather than a `tmp` directory inside it, so it adds no
`mkdir` process. The runner's own files in that root are `owner`, `population`, `evidence` and the
`s` and `a` directories. None of them is a name `mktemp` or `mkdtemp` makes.

### Wall-clock ceilings

No ceiling moves. Each figure below is DERIVED from `tools/gate-legs.json@db79c2db62ea`.

| Suite | Added | Ceiling |
|---|---|---|
| `tools/govkit/selftest.py` | one fixture bar on the minimal profile, two small repositories | 11750 s DERIVED |
| `tools/run-gates/run-gates.test.sh` | two fixture bars on the minimal profile | 13200 s DERIVED |
| `tools/lib/lib-selftest.test.sh` | at most four template builds, and the race arm loses its sleep | 370 s DERIVED |
| `tools/lib/resolve-python.test.sh` | one python child | 350 s DERIVED |
| `tools/run-gates/run-selftests.test.sh` | one `--serial` run of one row | 2040 s DERIVED |

### Inventory

| Minted identifier | Kind | Naming cell | Graded by |
|---|---|---|---|
| `check_kit_attestations` | python function | `py.function`, lexicon `--suggest` OK | AC1, its own seven lines |
| `check_blob_batch` | python function | `py.function`, lexicon `--suggest` OK | AC2, its own six lines |
| `env.sh`, `suite-tmproot.sh` | fixture scripts | none: fixture names are not declared | S2's and S11's arms |
| `template-cache args v1` | key text tag | none: a hashed literal | AC5 |

`python tools/lexicon/lexicon.py --suggest <name> --as py.function` printed `OK` for both function
names, run 2026-11-22.

### Files touched (estimate)

`tools/govkit/selftest.py` · `tools/govkit/upgrade_steps.py` · `tools/lib/template-cache.sh` ·
`tools/lib/lib-selftest.sh` · `.githooks/pre-push.test.sh` · `tools/lib/template_cache.py` ·
`tools/lib/lib-selftest.test.sh` · `tools/lib/resolve-python.test.sh` ·
`tools/run-gates/run-gates.test.sh` · `tools/run-gates/run-selftests.sh` ·
`tools/run-gates/run-selftests.test.sh` · `memory/project/shell-role.txt` ·
`memory/project/spawn-idiom-sites.txt` · `memory/map/generated/symbols.json` ·
`memory/builds/dQuietDisk/build/<date>-build-TOOL-dQuietDisk-37-widen-<n>.md`

The eight shell files each have a `shell-role` row. Five of them have `spawn-idiom-sites` rows:
the pre-push suite, the harness suite, the python resolver suite, the canary suite and both
`run-selftests` files [DERIVED, grepped 2026-11-22]. A file gaining a class it has no row for gains
the row through the same widen. Each widen record's number is one past the highest in the build
folder, which holds widen 21 [DERIVED, listed 2026-11-22], so `22` unless another unit widens first.
The two new functions join the codebase map's symbol index. That index is re-rendered by
`gen_map.py --write`, never by hand. No path here is on the kickoff manifest's `watch:` line.

### Alternatives rejected

| Alternative | Why it loses |
|---|---|
| Hash the arguments in `derive_template_key`, or refuse a second argument in `build_fixture` | The finder's fix: a direct `resolve_template` caller stays unkeyed. |
| Fold the arguments with a hash written in bash arithmetic | No process, but a second hash function in a block three files carry, for one process per distinct template. |
| Key the arguments into the directory name as text | Path length and the characters an argument may hold are unbounded. |
| An `--selftest` of its own for `owned_scratch.py` | A new leg with its own manifest row and budget, where the python resolver suite already grades the module and its guard covers it. |
| Compute the row hash a third time inside the M1 arm | A third copy of the expression, which proves the arm agrees with itself. The runner's own record is the comparison. |
| Export TMPDIR under `--attribute` too | The L and R revisions would share one template cache (section 4, "L4"). |
| Export to a `tmp` directory inside the runner's root | One more entry and one `mkdir` process, for a shape the runner's root already gives. |

## 5. Production-readiness checklist

- security: S4 closes a wrong-template serve that is silent today: a later builder call with other
  arguments was handed the first call's repository. S9 closes a read that answered one file's bytes
  for another file's name. Both fail closed: an unkeyable argument list returns 2, and a CR name
  costs a spawn.
- perf / scale: S4 adds one `git hash-object` per `resolve_template` call carrying arguments, two
  per turnstile run. S6 saves one file write per distinct pre-push template. S11 moves serial rows'
  scratch inside the runner's swept root, so a killed serial run strands nothing the next run
  cannot sweep.
- error / empty / loading states: S4's fold failure says so and returns 2, as the verb's other
  failures do. S1's first check reports a fixture bar that did not leave its record, so the six
  checks after it cannot pass on a fixture that never attested.
- observability: unchanged. The `template: <key8>` line now prints the folded key, still eight hex.
- risks: a `--serial` row that counts or clears its ambient TMPDIR now sees the runner's three
  files. Rows already run under an owned `gate-work.*` root in the bar and under `--pooled`, so no
  row relies on an unowned ambient. A key moving for every caller with arguments rebuilds each
  template once. No cache outlives its run's root, so nothing stale is read.
- testing: the probes of section 6, and the new arms in five suites, observed by the main loop.
- migration: N/A — no stored data. Template roots die with their run.
- user docs: N/A — no knob, flag or printed line changes for an operator.

## 6. Acceptance criteria

- **AC1** — When a probe puts `tools/govkit` on `sys.path`, imports `selftest` and calls
  `check_kit_attestations` on an empty scratch directory, seven lines print `ok` and none `FAIL`.
  The pass then breaks one clause of `derive_kit_attestations` at a time in its working copy and
  calls it again, and the named line prints `FAIL`. With `keys` forced to `()`, the first line
  fails. With the `rec.get("row")` comparison dropped, the fourth fails. With the record-sha oid
  comparison dropped, the fifth and sixth fail. With `members` held to the entry alone, the sixth
  fails. With the HEAD check dropped, the seventh fails. Each clause is restored with `git checkout`.
  Red when: a check passes on a fixture that never attested, or a clause's removal moves no line.
  fixture: the probe builds its own scratch gov and runs one fixture bar in it; the tree holds none.
- **AC2** — When the same probe calls `check_blob_batch`, six lines print `ok`. With S9's guard
  set back to `"\n" not in name`, the sixth prints `FAIL`, because the handle answers `a`'s bytes.
  With the `missing`/`ambiguous` test of `blob_at` dropped, the first and third fail. With the
  `batch.dead = True` line dropped, the fourth fails.
  Red when: a fallback branch can change and no line moves.
  figure: 246 tries to a shared prefix PINNED, measured 2026-11-22; the bound of 100000 is a
  literal.
- **AC3** — When a probe builds a committed scratch repository with the runner files and
  the `env.sh` leg as S2 states, and runs two fixture bars in it outside the worktree, five things hold.
  With `GATE_OUTER_AMBIENT_TMP` naming a directory holding three files and one orphan owner, the
  first bar prints `TMPDIR entries 3`. The orphan's directory is gone, and the bar printed its pid.
  The leg recorded the outer name as unset. The leg's `TEMP` and `TMP` matched
  `<ambient>/gate-work.*/tmp`. With the name pointing at a missing directory, the second bar printed
  the NOTE line. With the `unset GATE_OUTER_AMBIENT_TMP` line, the `RG_SWEPT_TMP` assignment or
  `TEMP` and `TMP` dropped in a scratch copy of the runner, the matching row of section 4's table
  turns.
  Red when: a case cannot tell the outer root from the inner ambient, or the export from the decoy.
- **AC4** — When a probe runs S3's program against the canonical `tools/lib/owned_scratch.py`, the
  survivors are live, dead-other, relative and bash-owned, and two `owned-scratch: sweeping` lines
  name the other two. Against a scratch copy with the `py:` test, the `isdir` test or the `isabs`
  test dropped, the survivors differ as section 4 states.
  Red when: a widened sweep predicate leaves the survivor set unchanged.
- **AC5** — When a probe sources `tools/lib/template-cache.sh` and calls `resolve_template` with
  one root, one key and builder `mka`, three times, the third call printing `<root>/<key>/repo`. The
  three calls carry `x`, then `y`, then no argument. Their paths differ. The first two templates'
  files hold `x` and `y`, and `build_template_clone` of the second holds `y`. Against the base
  block, the second path equals the first and holds `x`. With `GIT_TRACE2_EVENT` set to an empty
  directory, a call carrying arguments adds one trace file over the base block, built or reused.
  A call without arguments adds none. When a probe runs the race body of S7 through the harness, it
  prints `built 2`.
  Red when: an argument list leaves the key unmoved, a no-argument key moves, or the fold costs more
  than one process.
  figure: the one-process difference DERIVED at observation from the two trace counts.
- **AC6** — When the `template_cache_sh` block is extracted with the parity table's own `blk` awk
  from `tools/lib/template-cache.sh`, `tools/lib/lib-selftest.sh` and the push-main kit's pre-push
  suite, the three compare equal, and each holds `template-cache args v1`. `git grep -n fx-args` prints
  nothing. `grep -n "argument" tools/lib/template_cache.py` prints the KEY paragraph's new sentences.
  Red when: a copy drifts by one byte, which the `template_cache_sh` row then reports, or the hand
  fold survives beside the class fix.
- **AC7** — When a probe builds arm 3h1's fixture with `gax/f` in a scratch directory and reruns
  its traced bar with `GIT_TRACE` set, the trace holds a ` diff --quiet <40 hex> -- 'fx/*.sh'`
  line and no ` diff --quiet <40 hex> -- ga/` line. With `check_plain_guard` returning 1 in the
  fixture's copy of the runner, the `ga/` line appears. With `write_guard_slices` comparing only
  `length(g)` bytes there, the first run prints `ok    dir guard`.
  Red when: the one-diff rule regresses to a per-leg diff, or the slice loses its boundary.
  figure: the trace spellings PINNED, measured 2026-11-22 with git 2.54.0.
- **AC8** — When a probe sources `tools/lib/lib-selftest.sh` and runs S7's race body with the
  barrier, it prints `built 2`, `entries 1 nested 0` and `same template`. With the old
  `sleep 1` builder and the second racer started two seconds late, it prints `built 1`.
  Red when: the arm grades entries and nesting without both racers having built.
  cost: about two seconds for the late racer.
- **AC9** — When a probe makes a fixture repository like the `run-selftests` self-test's, with one
  row whose suite is `suite-tmproot.sh`, and runs the runner in `--serial` mode, the output carries
  `FAIL tmp-in-runner-root`. With the export line dropped from a scratch copy of the runner, it
  carries `FAIL tmp-outside-runner-root`. `grep -n "attribute" tools/run-gates/run-selftests.sh`
  prints the narrowed comment's sentence on why `--attribute` keeps the ambient.
  Red when: the comment claims a mode its code does not give.
- **AC10** — When the main loop runs each suite on a `New arm:` line in section 7, each new line
  prints its pass mark and every base line prints as before. The floors are met:
  `FLOOR_ASSERTIONS` at 497 in the canary suite and at 38 in the harness suite, and `SELFTEST_FLOOR`
  at 145 in the `run-selftests` self-test. Each arm's staged break, as section 7 states it, turns
  its own line.
  Red when: a new line cannot fail, or a base line moves.
  permission: a role pass runs no suite. The RED and GREEN observation is the main loop's, and the
  pass's proxies are AC1 to AC9.
  cost: one run of each of five suites, minutes to hours; the canary's ceiling is 13200 s DERIVED
  from the manifest.
- **AC11** — When `grep -n -E` for the eight shell files runs over `memory/project/shell-role.txt`
  after the widen, it prints eight rows. Each moved row ends `widened:<stem>`, and that stem names a
  file under `memory/builds/dQuietDisk/build/` whose Caused-by is `TOOL-dQuietDisk-37`. The same
  holds for every moved row of `memory/project/spawn-idiom-sites.txt`. Then
  `git diff --stat -- memory/project/` shows only those rows.
  Red when: a row is edited by hand, or a row for a file this unit does not touch moves.
- **AC12** — When `python tools/govkit/govkit.py shipped` runs, it lists the pre-push suite under
  `push-main`, and the self-test runner, the canary suite and the runner's own self-test under
  `run-gates`. When `python tools/govkit/govkit.py check --target C:/projects/incms/main`, and the
  same with `C:/projects/nicocares/main`, run read-only from gov before and after the unit, each
  prints the same bytes and exit code.
  Red when: a copy is not claimed by its kit, or a check reads differently.
  permission: read-only against the adopters' main checkouts, never their `gov-upgrade` worktrees.
  fixture: the adopters reach the change only after a minted version and their own `govkit update`.

No verdict a passing suite gave at the base moves. The new arms grade behaviour that already holds,
except for S4's key, S9's guard and S11's export, each of which AC5, AC2 and AC9 see red at the base.

## 7. Gates

`govkit selftest` · `govkit selfcheck` · `policy fixtures` · `recall floor` · `recall floor arms` · `extract-arms self-test` · `govkit acceptance matrix` · `govkit refusal join` · `selftest harness self-test` · `python resolver (behaviour + inline parity + idiom ban)` · `run-gates canary` · `run-gates turnstile` · `run-gates evidence` · `run-selftests self-test` · `pre-push self-test` · `pre-push bar self-test` · `pre-push run-log line` · `kit epoch (shipped bytes move, the version moves)` · `portability (shell lines only shrink)` · `ratchet (never gains)` · `codebase-map coverage + freshness` · `lexicon naming predicates` · `line length` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/govkit/selftest.py · covers AC1 AC10 · check_kit_attestations's seven lines; each failing case is staged by dropping the clause AC1 names from derive_kit_attestations in tools/govkit/govkit.py · none, the suite has no floor
New arm: tools/govkit/selftest.py · covers AC2 AC10 · check_blob_batch's six lines; the CR line is red at the base, and the others by dropping the branch AC2 names from blob_at · none, the suite has no floor
New arm: tools/run-gates/run-gates.test.sh · covers AC3 AC7 AC10 · arm 8's 8f1 to 8f4 and 8g, staged by dropping the outer root's assignment, its unset, its NOTE or TEMP and TMP from the export in the fixture's runner copy; arm 3h1's two trace lines, staged by check_plain_guard returning 1 · FLOOR_ASSERTIONS 490 to 497
New arm: tools/lib/resolve-python.test.sh · covers AC4 AC10 · the Python sweep's survivor set and its two lines, staged by dropping the py: test from a scratch copy of scan_dead_scratch · none, the suite has no floor
New arm: tools/lib/lib-selftest.test.sh · covers AC5 AC8 AC10 · the three argument-key lines, red against the base block; the race arm's built-2 line, staged by the sleep-1 builder with a late second racer · FLOOR_ASSERTIONS 34 to 38
New arm: tools/run-gates/run-selftests.test.sh · covers AC9 AC10 · the serial row's TMPDIR, TEMP and TMP under the runner's root, staged by dropping the export line · SELFTEST_FLOOR 144 to 145

The bar runs once at the close. The new arms' RED and GREEN observation is the main loop's. No
criterion has the pass run a suite, a gate leg or the bar.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-22 · initial draft, under `2026-11-22-prompt-TOOL-dQuietDisk-37-spec-task`, from
  the round-1 closing review's M1, M2, M4, M5 and L1 to L4. Order 9: it follows TOOL-dQuietDisk-36 at
  order 8, and its write set meets no live unit.

## 10. Reuse audit

Every seam extended is the one the finding names, and no unit adds a helper. M1 and L3 extend
`tools/govkit/selftest.py`'s `check` arms and its scratch-gov shape, `build_scratch_gov_kit`. M2
extends the canary suite's arm 8, `build_owned_fixture` and `run_owned_bar`, and the python
resolver suite's existing coverage of `owned_scratch.py`. M4 extends the `template_cache_sh` block
and its parity row. M5 extends arm 3h1 and its `check_gm_line`. L2 extends the harness suite's
`run_harness` race arm. L4 extends the runner's own root and its self-test's `arm` fixture suites.
`python tools/codebase-map/reuse_lookup.py` ran three probes. "self-test arm that drives blob_at
through a cat-file batch handle and kills the process" ranked `arm`, `armed`, `write_fixture_files`
and `read_blobs_at`. "fold builder arguments into the template cache key hash" ranked `key`, `keys`,
`build` and `build_records`. "fixture bar asserting the outer ambient temp root is counted and
swept" ranked `counts`, `fixture`, `repo_root` and `run_fixture_git`. None of them is a seam for
these arms: each is a name stem the lookup matched. The class predicate for L1, a line-framed
`cat-file --batch` writer guarding a newline and not a CR, was run over `tools/`, `skills/` and
`.githooks/`. It found `blob_at` and `derive_kit_attestations` in this build's diff, and older
readers in other kits. Section 3 says why only `blob_at` is fixed here.

Owning chain builds: dWitnessedBar (Test: gate health) for the suites and the two runners, and
dSafePassage (Supersession) for `blob_at`, whose contract as the one revision-blob reader
(TOOL-dSafePassage-26 S14) S9 keeps: a name it cannot ask the batch is a spawn, as a newline is
today. No spec of either build defines the template cache, the owned root or the attestation.

Recall terms used: closing review MEDIUM LOW batched attestation arms derive_kit_attestations
gate-selftest-last outer ambient root TEMP TMP export scan_dead_scratch template key builder
arguments resolve_template one moved list check_plain_guard blob_at CR batch BlobBatch ambiguous
race barrier run-selftests serial owned root
