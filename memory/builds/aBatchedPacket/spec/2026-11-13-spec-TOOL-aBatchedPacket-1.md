# TOOL-aBatchedPacket-1 — a front door for the chain packet: the instrument's own `main`, its two per-spec reads answered in-process, bound to the instrument blobs it was read against

**Status:** CLOSED · rev-1 · 2026-11-13 · node a · Tier-2 · base 8db6f4bef · streams tooling · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-13-build-TOOL-aBatchedPacket-1-analysis.md](../build/2026-11-13-build-TOOL-aBatchedPacket-1-analysis.md) | research | — |
| [2026-11-14-build-TOOL-aBatchedPacket-1-1-acceptance-ledger.md](../build/2026-11-14-build-TOOL-aBatchedPacket-1-1-acceptance-ledger.md) | journal | — |
| [2026-11-14-build-TOOL-aBatchedPacket-1-red-fix-1.md](../build/2026-11-14-build-TOOL-aBatchedPacket-1-red-fix-1.md) | red-fix | — |
| [2026-11-13-prompt-TOOL-aBatchedPacket-1-1-builder.md](../prompts/2026-11-13-prompt-TOOL-aBatchedPacket-1-1-builder.md) | journal | — |
| [2026-11-13-prompt-TOOL-aBatchedPacket-1-1-spec-writer.md](../prompts/2026-11-13-prompt-TOOL-aBatchedPacket-1-1-spec-writer.md) | journal | — |
| [2026-11-13-prompt-TOOL-aBatchedPacket-1-brief.md](../prompts/2026-11-13-prompt-TOOL-aBatchedPacket-1-brief.md) | research | — |
| [2026-11-13-review-TOOL-aBatchedPacket-1-diff-review-round1.md](../reviews/2026-11-13-review-TOOL-aBatchedPacket-1-diff-review-round1.md) | diff-review | — |

<!-- /gen:spec-records -->

## 1. Goal

`packet.py --check` and `--write` for a chain build spend their time in two reads that spawn one git
process per spec or per spec revision, and the spec-token checker's packet join pays the same cost
at every dispatch inside a live chain run. This unit adds a front door that runs the instrument's
own `main` with those two reads answered in-process, so both finish in under a minute on node `a`
while every instrument file keeps its bytes and every line printed is still the instrument's own.

## 2. Scope (IN)

Below, `packet.py`, `carries.py` and `schedule.py` name the three instruments under
`memory/builds/dClosedLoop/build/`, and "the door" is the new script.

- **S1** — A new script, `tools/chain-packet.py`, run from the worktree root as the instrument is.
  It takes the instrument's own arguments. With `--write`, `--check` or `--fixture` among them it
  loads the tracked `packet.py` as a module, installs the two reads of S2 and S3, and returns the
  instrument's own `main(argv)`. With any other argument list it runs the instrument as a child
  with the same arguments. Observed by AC1 and AC2.
- **S2** — The coverage report. The instrument's child `carries.py --report <slug>` is answered by
  the carries module's own `design`, `join` and `report`, over each chain spec's working-tree text
  with an empty revision list. If that in-process render raises, the door says so on stderr and
  runs the instrument's own child, so the refusal is the instrument's. Observed by AC1 and AC5.
- **S3** — The parent specs. Each `git show <ref>:<path>` that `schedule.py#tree_state` makes is
  answered from one `tools/memory-tree/tree_lib.py#read_blobs_at` call per parent build, decoded as
  `subprocess.run(text=True, encoding="utf-8")` decodes. A path the batch cannot answer is read by
  the instrument's own `git`. Observed by AC1 and AC5.
- **S4** — The content binding. The door holds one git blob id per instrument as a constant, and
  compares each with the file's bytes before it loads anything. On any mismatch it names the
  instrument on stderr and runs `packet.py` as a child with the same arguments. Observed by AC4.
- **S5** — A `--parity <slug>` mode. It renders the packet the instrument's way, then with the two
  reads installed, in one process, and compares path, bytes and any refusal. Observed by AC3 and
  AC6.
- **S6** — `tools/check-spec-tokens.py#scan_live_packets` runs the door where it ran the
  instrument, when the door is beside the checker, and the instrument directly when it is not. The
  hit's reason keeps its text. Observed by AC8 and AC10.
- **S7** — The door's suite, `tools/chain-packet.test.sh`, with the arms of §4, "The suite", and
  one arm added to `tools/check-spec-tokens.test.sh` for S6's second branch. NOT OBSERVED by a
  criterion: a suite is declared under §7's `New arm:` lines and seen RED then GREEN by the main
  loop at the close.
- **S8** — The registrations a new suite leg owes, listed in §4, "What the new files owe".
  NOT OBSERVED by a criterion: each is graded by its own meta-gate when the main loop runs the bar at
  the close.
- **S9** — The dossier `memory/map/features/spec-tokens.md` names the door among its affordances,
  with its three modes and its fallback. Observed by AC9.
- **S10** — No instrument byte moves. Observed by AC7.

## 3. Non-goals (OUT)

- Any byte of `packet.py`, `carries.py`, `deviations.py`, `schedule.py` or another dClosedLoop
  instrument. The batched read inside `carries.py` is ask `TOOL-dGroundRules-112`, the owner's
  landing and re-pin.
- `carries.py --build <slug> --exit`, the Design-exit join. It reads every revision for its
  dropped-clause arm and stays as slow as it is.
- `packet.py --repin`. The door runs it as a child, unchanged. It is the owner's verb, it prompts at
  a console, and this unit builds no proof for it.
- A recorded-verdict cache, or any stored state. The door keeps nothing between runs.
- An environment variable or flag that names the blob ids. The prototype read them from its
  environment; the product holds them as constants, so nothing outside the file can aim a shortcut
  at other bytes.
- `memory/builds/dDeclaredLoop/`, the branch `branch/unattended-declared-loop-d56bf0`, and the
  driver's `verb_dispatch`.
- `gen_build_index.py --asks`, which is most of what remains of a fast run.
- A chain build's README or packet text, which word the direct `packet.py` call. Both are rendered
  by pinned instruments.
- A `help/` page and a kit descriptor. The door is gov-internal, as the checker beside it is.

### Edges

- **consumes-from** external — the three instruments at the blobs §4, "Inventory" pins, and
  `tree_lib.py#read_blobs_at` with its documented decode. A moved instrument turns the shortcuts
  off; a changed decode is caught only by the suite.
- **hands-off** external — the landing of ask `TOOL-dGroundRules-112` moves `carries.py`, and owes
  the door's constant for it after the three reliance points of §4 are read again against the new
  bytes.
- **hands-off** external — `packet.py --repin` renders every chain packet and pays the walk once
  per packet. Routing it through the shortcuts is a separate ask with its own proof.

## 4. Design

### Evidence

Read at `8db6f4bef`. Every claim of the analysis record
`memory/builds/aBatchedPacket/build/2026-11-13-build-TOOL-aBatchedPacket-1-analysis.md` that this
design rests on was checked against the code, and §10 lists where the two disagree.

- **The report reads no revision.** `carries.py#main` keeps only the second result of `join`,
  `carriers`, and prints `report(b, builds, nodes, specs, carriers)`. `carries.py#join` fills
  `carriers` from `CARRY.findall(text)`, the working-tree text. Its one read of the revision list
  sits under `if revs:` and only appends to `findings`, which `--report` discards.
  `carries.py#report` reads `specs` three times: twice for the text alone and once for a count.
- **The walk is `carries.py#real_specs`.** It runs one `git log` per chain spec and one `git show`
  per commit that log names. Its `git` helper returns stdout whatever the exit status, and decodes
  strictly, so a revision that is not UTF-8 raises in the child.
- **The spec population is the working tree.** `real_specs` globs `*.md` in each chain build's
  `spec/` folder and reads each with `read_text(encoding="utf-8")`. The tree holds 1543 such files
  in 22 builds (DERIVED: the same glob, counted at the base).
- **The child's result has three readers.** `packet.py#derive_sources` reads `returncode`, `stderr`
  for a refusal, and `stdout.strip()` for the coverage field.
- **The parent read is `schedule.py#tree_state`.** It calls `git("ls-tree", "-r", "--name-only",
  ref, <folder>)` once per parent build and `git("show", f"{ref}:{p}")` once per listed `.md`
  path. `schedule.py#git` decodes with `text=True, encoding="utf-8"`, which folds both CRLF and a
  lone CR to LF and raises on bytes that are not UTF-8.
- **The seams are module globals.** `packet.py` binds `subprocess`, `carries` and `schedule` at
  module level, and `derive_sources` reaches the child through `subprocess.run` and the parents
  through `schedule.tree_state`. Replacing the `subprocess` name inside the loaded packet module,
  and the `git` name inside the loaded schedule module, changes those two reads and no file.
- **`packet.py --fixture` pays the walk too.** `packet.py#run_fixture` opens with
  `derive_sources(slug)`, so the bare fixture and each plant cost what a `--check` costs.
- **The kit already has the batch reader.** `tree_lib.py#read_blobs_at` reads every
  `(rev, path)` pair in one `git cat-file --batch`, slices each body by its byte size, decodes
  UTF-8 with CRLF folded, and answers None for a missing object, a non-blob and a blob that is not
  UTF-8. It raises `OSError` on a failed call and never returns a partial answer.
- **The checker reads only stdout.** `scan_live_packets` runs the instrument with
  `capture_output=True`, takes the first stdout line as the hit's reason on a non-zero exit, and
  reads no stderr. It derives the instrument from the one tracked file matching
  `PACKET_INSTRUMENT` and spells no unit id.
- **Measured.** `--check dDeclaredLoop` on the frozen clone: the instrument 845.5 s and 15,465
  processes; the prototype 16.8 s and 20 processes, with the same eight lines and exit 1 (PINNED,
  2026-11-13, node `a`, the analysis record). `carries.py#design` alone cost 0.8 s on its second
  call in one process (PINNED, 2026-11-13, node `a`, this spec's probe).

### The flow

1. **Find the instruments.** For each role in `INSTRUMENT_BLOBS`, glob
   `memory/builds/dClosedLoop/build/*-build-*-<role>.py`. The door spells no unit id, as the
   checker does not. No packet instrument, or more than one, is the door's own refusal: one line on
   stdout, exit 2, nothing run.
2. **Compare the blobs.** A role is moved when it has no file, more than one file, or a file whose
   blob id is not the constant. The blob id is `derive_blob`: SHA-1 over the git blob header and the
   file's bytes with CRLF folded to LF.
3. **Choose the path.** The shortcuts are on only when no role is moved, the argument list names
   `--write`, `--check` or `--fixture`, and `tree_lib.py` loads from `memory-tree/` beside the
   door. Otherwise the door prints one stderr line naming every reason and returns
   `run_instrument`, the child's exit status. The child inherits stdout, so its lines are the
   instrument's bytes.
4. **Load and install.** `load_module` loads `packet.py` by path, which loads the other instruments
   as it always does. `set_reads` installs the two replacements.
5. **Run.** The door returns `packet.main(argv)`. Argument errors, refusals and exit statuses are
   the instrument's.

The stderr line of step 3 is
`chain-packet: shortcuts off, running the instrument as it stands — <reason>[; <reason>]`. A reason
is `<role>: no file`, `<role>: <n> files`, `<role>: blob <12 hex>, read against <12 hex>`,
`tree_lib.py is not beside this script`, or `no shortcut mode in the arguments`.

### The report read (S2)

`set_reads` rebinds `packet.subprocess` to a stand-in that passes every attribute through to the
real module and replaces `run`. The replacement answers exactly one call shape, the argument list
`[sys.executable, packet.INSTRUMENTS[0], "--report", <slug>]`, and hands every other call to
`subprocess.run` untouched. For that shape it calls `run_report`:

- `builds, nodes, retired = carries.design()`, called again as the child calls it. The prototype
  memoised it; the second call costs under a second, so the product does not.
- `specs` is `real_specs`'s shape with no history: for each build in `builds`, each `*.md` of its
  `spec/` folder in sorted order as `(posix path, read_text(encoding="utf-8"), [])`.
- `carries.join(builds, nodes, retired, specs, slug)`, of which the second result is kept, then
  `carries.report(slug, builds, nodes, specs, carriers)`.
- The answer is `subprocess.CompletedProcess(args, 0, stdout=<report> + "\n", stderr="")`, a
  stdlib type in place of the prototype's own class.

Any exception inside `run_report` prints
`chain-packet: the in-process report raised <type>, running carries.py --report as the instrument does`
on stderr and returns the real `subprocess.run` of the same call. A spec the working tree cannot
decode therefore refuses with the instrument's own line and stderr excerpt.

### The parent read (S3)

`set_reads` rebinds `schedule.git` to `read_git(*args, check=True)`, which holds a cache keyed by
`<ref>:<path>`:

- An `ls-tree` call runs the instrument's own `git` first. Its output lines, each a path, are then
  read in one `read_blobs_at(".", [(ref, path), …])` call, with `ref` the fourth argument as
  `tree_state` passes it. Each text answer is stored after `.replace("\r", "\n")`, which with the
  reader's own CRLF fold equals the instrument's decode. An `OSError` stores nothing.
- A two-argument `show` whose operand is cached with a text value returns it. Every other call,
  a None answer included, goes to the instrument's own `git`, so a missing path, a quoted path and
  a blob that is not UTF-8 fail exactly as they do today.

This is one `cat-file` process per parent build, two for dDeclaredLoop, where the brief and the
prototype have one for the run. The prototype's own long-lived reader parsed a `missing` answer by
splitting on spaces, which misreads a missing path that carries one; the kit's reader already
handles that header and is the one bytes reader the tree has.

### The parity mode (S5)

`check_parity(packet, slug)` runs before `set_reads`:

1. `render_outcome` calls `packet.render_packet(slug)` and returns `("packet", path, text)`, or
   `("refused", message)` or `("unmeasured", message)` for the instrument's two exceptions.
2. `packet.read_tree.cache_clear()` and `packet.read_asks.cache_clear()`, so the second render
   re-reads everything through the installed stand-ins and nothing is compared with itself.
3. `set_reads`, then `render_outcome` again.
4. One stdout line, and exit 0 when the two outcomes are equal, 1 when not:
   `chain-packet: parity <slug> · identical · <n> bytes · <path>`, or
   `chain-packet: parity <slug> · identical · both <refused|unmeasured>: <message>`, or
   `chain-packet: parity <slug> · DIFFERENT · <the instrument's outcome> · <the door's outcome>`,
   an outcome there being its kind with a byte count or a message.

With a moved role, `--parity` prints the step-3 line and exits 2: there is nothing to compare.
The door reconfigures stdout to UTF-8 for this line, as `packet.main` does for its own.

### The checker (S6)

`scan_live_packets` builds its command from a constant, `PACKET_DOOR = "chain-packet.py"`, resolved
beside the checker's own file: the door with `--check <slug>` when that file exists, else the
instrument as today. Nothing else in the function moves, and the reason string keeps the words
`packet.py --check exited`. The `packet` paragraph of the checker's docstring gains one sentence
saying so. The door's refusal of step 1 goes to stdout so a hit quotes it.

### What it does not check

- **A chain spec revision in history that is not UTF-8.** The instrument's child raises on one and
  the packet refuses naming `carries.py --report`; the door reads no history and renders. No
  revision was in that state at `8db6f4bef`: the instrument's measured run printed a summary and
  not a refusal (PINNED, 2026-11-13). `--parity` reports this case as DIFFERENT, and the suite
  stages it.
- **The child failing to start.** The instrument refuses on the child's exit status; the fast path
  has no child. A git that cannot start is no difference: `packet.py#read_tree` runs git before
  either path reaches the report and fails the same way in both.
- **A spec path that is not valid Unicode.** The child would fail encoding its report; the door
  passes the text on.
- **`read_blobs_at`'s decode.** It is bound by no blob. A change to it is caught by the suite's
  equality arms, whose leg is guarded on `tree_lib.py`, and by `--parity`.
- **A CR-only difference in an instrument file.** `derive_blob` folds CRLF, so a working-tree file
  that differs from the pinned blob only in line endings reads as unmoved. Python reads both the
  same way.
- **An object format other than SHA-1.** Every role reads as moved there and the door runs the
  instrument, which is slow and correct.
- **The other modules `packet.py` loads.** The as-built, deviations, bare-ids, map, handoff and
  index-generator modules run as they stand on both paths, and the door relies on no internal of
  them.
- **Speed.** No arm asserts a wall time. AC1 and AC2 measure it once, on one node.
- **The real tree, in the suite.** The suite's fast-path arms run on a trimmed clone. The 1543-spec
  tree is compared only when someone runs `--parity`, which costs the instrument's walk.
- **A caller who runs `packet.py` directly**, as a chain build's README words it. That call is as
  slow as before and writes the bytes the door writes.
- **The Design-exit join**, and whether the instrument's own reading is right. The door changes how
  two inputs are fetched and nothing about what is done with them.
- **An untracked second file of an instrument's shape.** The checker counts tracked files and the
  door globs the working tree, so such a file makes the door refuse or fall back where the checker
  alone would have graded. The result is a hit or a slow run, never a pass.

### The suite

`tools/chain-packet.test.sh` follows `tools/check-spec-tokens.test.sh` for its launcher, its
`arm ok`/`arm FAIL` lines, its `FLOOR_ASSERTIONS` and its `FOREIGN_PREFIX_PROBE` stop after the
first arm. It runs the door beside itself with the fixture as the working directory.

Fixture S is a scratch repository holding only a stub at the packet instrument's path that prints
one line and exits 1, as the checker suite's packet arms build it.

Fixture T is a scratch clone of this repository at HEAD, made as
`tools/run-gates/foreign-prefix.gov.test.sh` makes its clone. One commit in T leaves two specs in
one chain build's `spec/` folder and two in one of its parents', and no other chain spec. The chain
builds are the builds holding a packet. The build is one whose packet the trim makes stale.

| Arm | Fixture | Asserts |
|---|---|---|
| `CP1` | S | exit 1, the stub's line on stdout, and the `shortcuts off` line on stderr naming `carries: no file` |
| `CP2` | S, the stub gone | exit 2 and the door's refusal on stdout |
| `CP3` | T, stale | the door's `--check` and the instrument's print the same stdout and both exit 1 |
| `CP4` | T | the door's `--write` prints `packet: wrote`, then both `--check` runs print the same stdout and exit 0 |
| `CP5` | T | `--parity` prints `identical` with a byte count and exits 0 |
| `CP6` | T, one byte appended to the schedule instrument, uncommitted | the `shortcuts off` line names `schedule`, and stdout and exit equal CP4's |
| `CP7` | T, one kept spec committed with a non-UTF-8 byte and committed again restored | `--parity` prints `DIFFERENT` and exits 1 |

CP3, CP4 and CP5 also assert that stderr holds no `shortcuts off` line, so a run that fell back
cannot pass as a fast one. When an instrument's blob has moved at HEAD those three arms fail naming
the role, which is F2.

The suite's wall-clock ceiling is 900 s, declared on its manifest row. Its cost is roughly eleven <!-- PINNED 2026-11-14 -->
packet renders on T at about 15 s each plus the clone (UNVERIFIED estimate, from the prototype's <!-- PINNED 2026-11-14 -->
16.8 s on the full tree); the builder records the first measured reading.

What the suite does not check: the full tree, speed, the `--fixture` route, and a moved `carries`
or `packet` role on real bytes, which CP6 shows for one role only.

### Inventory

| Minted | Where | Cell |
|---|---|---|
| `tools/chain-packet.py`, `tools/chain-packet.test.sh` | the tool root | no file cell is declared; the hyphenated spelling of the checker beside them |
| `INSTRUMENT_DIR`, `INSTRUMENT_BLOBS`, `FAST_MODES` | the door | no `py.constant` cell is declared |
| `derive_blob(path)` | the door | `py.function` |
| `resolve_instruments()` | the door | `py.function` |
| `scan_moved(found)` | the door | `py.function` |
| `load_module(name, path)` | the door | `py.function` |
| `run_instrument(path, argv)` | the door | `py.function` |
| `run_report(carries, slug)` | the door | `py.function` |
| `read_git(*args, check=True)` | the door, inside `set_reads` | `py.function` |
| `set_reads(packet, tree_lib)` | the door | `py.function` |
| `render_outcome(packet, slug)` | the door | `py.function` |
| `check_parity(packet, tree_lib, slug)` | the door | `py.function` |
| `main(argv)` | the door | `py.function` |
| `PACKET_DOOR` | the checker | no `py.constant` cell is declared |
| the flag `--parity` | the door | no cell grades a flag |
| the prefix `chain-packet:` | stdout and stderr lines | no cell grades an output prefix |
| the leg `chain-packet self-test` | the manifest | the spelling of `spec-tokens self-test` |
| the arm labels `CP1` to `CP7` | the suite | no cell grades an arm label |

Every function name answered OK to `lexicon.py --suggest <name> --as py.function` on 2026-11-13.
The lexicon offered `set_reads` in place of a name led by `patch`, and refused names led by
`answer`, `swap` and `bind` as outside the declared verbs.

`INSTRUMENT_BLOBS` at the base, each equal to `git rev-parse 8db6f4bef:<path>`:

| Role | Blob |
|---|---|
| `packet` | `cab3bff165a1bb61a5854f58d350912e79a7b34b` |
| `carries` | `0b5fab9cc06d7b03c50ab94522092e2b9e266ce3` |
| `schedule` | `5aa5421e265b02ba4478f8860ad9a4f5fea94500` |

Beside each constant the door carries the reliance points read against that blob, as comments:
for `packet`, the module names `subprocess`, `carries`, `schedule`, `INSTRUMENTS[0]`, the report
call's argument shape, `main`, `render_packet`, `Refusal`, `Unmeasured`, `read_tree` and
`read_asks`; for `carries`, the signatures of `design`, `join` and `report`, the glob and read of
`real_specs`, and `main`'s `--report` branch; for `schedule`, the signature of `git` and the two
calls `tree_state` makes.

### What the new files owe

The door and its suite are gov-internal: the instrument they serve lives in this repository's
memory tree, as the checker's corpus does. So they owe exemption rows and no kit descriptor, and no
`help/` page.

| Owed | File | Who |
|---|---|---|
| the leg row: name `chain-packet self-test`, `bash {prefix}/chain-packet.test.sh`, `chunk` `selftests`, `subject` `kit`, `ceiling` 900, guard below | `tools/gate-legs.json` | builder |
| two `[[exempt]]` rows and one `[[exempt_leg]]` row, worded as the checker's are | `tools/govkit/registry.toml` | builder |
| the leg's pin row, by the generator the file's header names | `tools/govkit/subject-pins.tsv` | builder |
| the suite's budget row, from its first measured reading by the file's own rule | `tools/run-gates/selftest-budgets.txt` | builder |
| the leg name in the dossier's `gate-legs` list, both files in its `globs` list, the affordance lines of S9 | `memory/map/features/spec-tokens.md` | builder |
| the floor raised by one, with its `RAISED` comment | `tools/check-spec-tokens.test.sh` | builder |
| the generated map under `memory/map/generated/` | regenerated once | main loop, at the close |
| the leg's cost row | `tools/run-gates/ceiling-evidence.txt` | main loop, from the close's bar |
| the RED then GREEN observation of each `New arm:` line, and the bar | — | main loop, at the close |
| the after-measurements, as the analysis record's section 4 | the build's ledger | main loop |

The guard is `{prefix}/chain-packet.py`, `{prefix}/chain-packet.test.sh`,
`{prefix}/memory-tree/tree_lib.py` and `memory/builds/dClosedLoop/build/`, the files the suite
reads. The list above is what reading the base found. The record
`memory/gotchas/a-new-leg-trips-a-growing-set-of-meta-gates.md` says the set is found by running
it, so the builder runs each named meta-gate's own script and the main loop's bar finds any other.

The `harness arms` leg grades nothing here. Its population is a tracked `*.sh` that defines
`fail() {`, with its sibling suite, and it excludes every `*.test.sh` outright
(`tools/memory-tree/check-arms.py`, its docstring). A Python script's suite is outside it.

### Migration

Additive. A tree without the door runs the packet join as it does today.

### Rollout

No switch. The door is used where it is called, and the checker calls it once it is tracked. The
blob binding is the dark state: with any instrument moved, every call is the instrument's own.

### Files touched (estimate)

- `tools/chain-packet.py`
- `tools/chain-packet.test.sh`
- `tools/check-spec-tokens.py`
- `tools/check-spec-tokens.test.sh`
- `tools/gate-legs.json`
- `tools/govkit/registry.toml`
- `tools/govkit/subject-pins.tsv`
- `tools/run-gates/selftest-budgets.txt`
- `memory/map/features/spec-tokens.md`

### Alternatives rejected

- **The batched read inside `carries.py`.** The root cure, and ask `TOOL-dGroundRules-112`. It
  moves a pinned blob, so it is the owner's landing.
- **A cache keyed on the blobs each stage reads, or a recorded verdict.** A commit precedes each
  re-render and each dispatch, so the key misses when it matters, and a stored verdict sits between
  the instrument and its reader.
- **The prototype's own `cat-file` reader.** A second bytes reader beside the kit's one, with a
  header parse the kit's already gets right.
- **Spelling the three instrument paths.** Each carries a unit id, and the checker derives its
  instrument by shape for that reason.
- **An unconditional fast path.** A re-pinned or stubbed instrument would be graded by shortcuts
  read against other bytes.
- **The suite's arms inside the checker's suite.** The fast-path arms need the real instruments on
  a real tree, minutes of work against that suite's 130 s budget row. F1 holds the choice. <!-- PINNED 2026-11-14 -->

## 5. Production-readiness checklist

- security — no write path of its own: `--write` is the instrument's. Arguments reach the
  instrument's own parser or a child started from a list, never a shell. The blob ids are constants
  with no environment or flag form. The door imports only tracked files it has hashed, plus
  `tree_lib.py`.
- perf / scale — about 20 processes where the instrument makes 15,465 (PINNED, the analysis record).
  What remains is the `--asks` child, about 13 s, out of scope. <!-- PINNED 2026-11-14 -->
- error / empty / loading states — no instrument or several: exit 2 and one line. A moved role:
  the instrument as a child. An in-process report that raises: the instrument's own child. A batch
  read that fails: the instrument's own reads.
- observability — one stderr line whenever the shortcuts are off or the report fell back, naming
  why. The parity line names what was compared.
- risks — the suite's fast-path arms red when an instrument moves (F2). The trimmed fixture T may
  need a different pair of builds than the first tried; the arm's requirement is a stale packet and
  a parent with kept specs. A builder still types `packet.py` unless told otherwise (F4).
- testing — AC4 to AC6 run on fixtures S and T; AC1 to AC3 and AC10 on the frozen clone; the suite
  keeps the fixture arms.
- migration — N/A — additive, see §4, "Migration".
- user docs — the dossier, S9. No `help/` page: the surface is gov-internal.

## 6. Acceptance criteria

`<door>` is the front door script at the tool root. `<clone>` is the frozen clone of `8db6f4bef`
the analysis record measured on, outside this repository, with the built door and the edited
checker copied in. `<S>` and `<T>` are the suite's fixtures, built by hand as §4 describes. Every
command runs from the root of the tree it names.

- **AC1** — When `python <door> --check dDeclaredLoop` runs in `<clone>`, its stdout is the eight
  lines the instrument printed there, it exits 1, its stderr holds no `chain-packet:` line, and it
  finishes in under 60 s. <!-- PINNED 2026-11-14 -->
  Red when: a read is answered from other bytes, or the run fell back to the instrument.
  figure: 60 s is PINNED, the brief's bound; the instrument's 845.5 s is PINNED, 2026-11-13.
  cost: none beyond the run if the instrument's output was kept; otherwise one instrument run.
- **AC2** — When `python <door> --write dDeclaredLoop` runs in `<clone>`, it prints one line opening
  `packet: wrote`, exits 0 and finishes in under 60 s; `python <door> --check dDeclaredLoop` then <!-- PINNED 2026-11-14 -->
  prints a summary line carrying `byte compare green`.
  Red when: the write path is not routed through the instrument's `main`.
  figure: 60 s is PINNED, the brief's bound.
- **AC3** — When `python <door> --parity dDeclaredLoop` runs in a fresh copy of `<clone>`, it prints
  one line carrying `identical` and a byte count, and exits 0.
  Red when: either replaced read differs from the instrument's on the full tree.
  cost: one instrument render, about 14 minutes on node `a`.
- **AC4** — When `python <door> --check tChain` runs in `<S>`, stdout is the stub's one line, the
  exit is the stub's 1, and stderr holds one line opening `chain-packet: shortcuts off`.
  Red when: the blobs are compared after the load, or a mismatch is ignored.
- **AC5** — When `python <door> --check <slug>` and
  `python memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-packet.py --check <slug>`
  run in `<T>`, their stdout is identical and both exit 1; after `python <door> --write <slug>` the
  same two commands print identical stdout and exit 0; and no door run prints `shortcuts off`.
  Red when: `run_report` skips or reorders a spec, or `read_git` decodes a parent spec otherwise.
- **AC6** — When `python <door> --parity <slug>` runs in `<T>`, it prints `identical` and exits 0;
  after a kept spec is committed with a non-UTF-8 byte and committed again restored, it prints
  `DIFFERENT` and exits 1.
  Red when: parity compares one render with itself, or swallows the instrument's refusal.
- **AC7** — When `git diff --quiet 8db6f4bef HEAD -- memory/builds/dClosedLoop/build/` runs at the
  branch tip, it exits 0.
  Red when: any instrument byte moved.
- **AC8** — When `python tools/check-spec-tokens.py` runs in the checker suite's packet fixture, it
  exits 1 and prints
  `packet.py --check exited 1: packet: tChain - stub - byte compare red`; a copy of the checker in
  a tool root that holds the memory-tree kit and no door prints the same line.
  Red when: the door's notice reaches stdout ahead of the summary, or the checker needs the door.
- **AC9** — When `grep -c 'chain-packet' memory/map/features/spec-tokens.md` runs, it prints 3 or
  more.
  Red when: the door is recorded only in this spec.
- **AC10** — When `python tools/check-spec-tokens.py` runs in a copy of `<clone>` whose
  `memory/builds/dDeclaredLoop/RUN.md` ends with an added `phase: BUILDING` line, it prints
  `packet join · 1 live chain run(s) · 1 packet(s) checked` and a `[packet]` hit quoting the
  instrument's summary line, and finishes in under 180 s. <!-- PINNED 2026-11-14 -->
  Red when: the join still runs the instrument's walk.
  figure: 180 s is PINNED, the brief's "a few minutes"; the checker alone took 45.9 s there
  (PINNED, 2026-11-13).
  fixture: the edit is to the copy of the clone, never to this repository's file.
- **AC11** — When `python <door> --fixture` runs in `<clone>` with each `--plant` the instrument
  declares, and with `--plant pin` under each `--control`, every run's stdout and exit status equal
  the instrument's own for the same arguments.
  Red when: a shortcut changes what an arm of the instrument's check reads.
  cost: nineteen instrument runs at about 14 minutes each for the base readings, which F3 decides.

## 7. Gates

`spec-tokens self-test` · `spec tokens (a spec's own names resolve)` · `memory-hygiene self-test` · `build-index selftest` · `policy fixtures` · `run-gates canary` · `run-gates gov canary` · `measure-legs selftest` · `recall floor` · `recall floor arms` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `lexicon naming predicates` · `codebase-map gate coverage` · `codebase-map coverage + freshness` · `testsuite counts (every bar self-test prints one)` · `python reads (a name never bound, an import outside its guard)` · `encoding posture (text IO names its encoding)` · `memory hygiene`

The new leg, chain-packet self-test, is not on that line because the manifest does not hold it
until this unit lands; it is declared below. No path of §4's estimate trips a guard that is not
broad beyond the legs named, by the checker's `--legs-for` at `8db6f4bef`. The held legs run at the
close, and not while the dDeclaredLoop run is live unless the close requires it.

New arm: tools/chain-packet.test.sh · covers AC4 · CP1 and CP2 on fixture S, staged with the blob comparison returning no moved role · `FLOOR_ASSERTIONS`, set by the arms added
New arm: tools/chain-packet.test.sh · covers AC5 · CP3, CP4 and CP6 on fixture T, staged with the report read leaving out each build's last spec · `FLOOR_ASSERTIONS`, set by the arms added
New arm: tools/chain-packet.test.sh · covers AC6 · CP5 and CP7 on fixture T, staged with the caches left uncleared and the second render taken before the reads are installed · `FLOOR_ASSERTIONS`, set by the arms added
New arm: tools/check-spec-tokens.test.sh · covers AC8 · a checker copy in a tool root with no door, staged with the checker calling the door unconditionally · `FLOOR_ASSERTIONS`, raised by one

## 8. Open questions

- **F1 — Where do the door's arms live?**
  - (a) A suite of its own and a new leg, as §4 specifies. It costs the registrations of §4, "What
    the new files owe", and keeps the fast-path arms on real instrument bytes.
  - (b) Only the cheap arms, CP1 and CP2 and the routing arm, inside the checker's suite, with no
    new leg. Equality with the instrument is then shown once, by `--parity` at the close, and no
    standing arm guards a later edit of the door.
  - Recommendation: (a). The door is bound to three constants, so the one change that can break it
    silently is an edit to the door itself, and only real-bytes arms see that.
  RESOLVED (agent, 2026-11-13, delegated): (a).
- **F2 — What do the fast-path arms do once an instrument's blob has moved at HEAD?**
  - (a) Fail, naming the role and the cure: read the reliance points again and set the constant.
    The landing that moves the instrument then owes that step, the landing of ask
    `TOOL-dGroundRules-112` included.
  - (b) Print a not-graded line and pass. The door then runs slow everywhere with one stderr line
    per call, and nothing reds.
  - Recommendation: (a). A skip there would read as coverage, and the fourteen-minute walk would
    return unannounced.
  RESOLVED (agent, 2026-11-13, delegated): (a).
- **F3 — How are AC11's base readings taken?**
  - (a) All nineteen instrument runs, in the background on copies of the frozen clone, three at a
    time, while the build proceeds.
  - (b) The bare fixture, `--plant pin` with both controls, and `--plant run-live` only, five runs.
  - (c) None: the instrument's bytes and the tree are the base's, so its own results are, and AC11
    is cut to AC7.
  - Recommendation: (a). The brief names each plant and control, the runs need no attention, and
    the node's load only stretches their wall time.
  RESOLVED (agent, 2026-11-13, delegated): (b), run one at a time. Option (a) keeps three walks of about 15,000 processes each (PINNED 2026-11-13) on the node for hours beside the live dDeclaredLoop run, which the brief's constraints rule out. AC11 is observed on those five argument lists against the instrument, and on all nineteen through the door against the exits the instrument's docstring states.
- **F4 — Where does a chain session learn to call the door?**
  - (a) One line in the kickoff manifest, `memory/guides/SESSION-KICKOFF.md`, written by the main
    loop at the close, beside the line on the carries join.
  - (b) The dossier and the door's docstring only.
  - Recommendation: (a). Chain READMEs and packets word the direct call and cannot change, so
    without a line every session reads, only the checker's join gets faster.
  RESOLVED (agent, 2026-11-13, delegated): (a).

## 9. Revision log

- rev-1 · 2026-11-13 · initial draft.

## 10. Reuse audit

The seam is `tools/memory-tree/tree_lib.py#read_blobs_at`, which
`python tools/codebase-map/reuse_lookup.py "run a pinned instrument in-process with its per-file
git reads answered by one batched cat-file read, falling back to the instrument as a child when its
blob moved"` ranked as a SEAM with fan-in 7, beside `read_git_output` in the same file and
`read_spec_revisions` in `tools/memory-tree/design_lib.py`, the two-process history read the
checker's own carries join uses. The door calls the first for S3 and needs neither of the others,
since it reads no history. The second seam is the checker's `scan_live_packets`, extended in place
by one command choice. For running an unchanged script with two of its reads replaced, no existing
seam fits: the lookup returned only name-stem neighbours, and nothing under the tool root loads
another script and rebinds a module global of it. Recall returned ask `TOOL-dGroundRules-112`,
which files the root cure and is why the instrument's bytes stay; `PLAY-dClosedLoop-28` and
`TOOL-dGroundRules-88`, which make a re-pin the owner's; and `PLAY-dOrderedCharter-78`, which
records that the packet embeds `carries.py#report`. `gotchas.py --for-paths` over the estimate
selected `staged-break-substitutes-a-synthetic-value`, which is why CP6 moves a real instrument and
CP3 to CP5 run real ones; `fixture-passes-by-finding-nothing`, which the no-fallback assertion
answers; and `held-suite-guard-misses-a-sibling-kit`, which put `tree_lib.py` in the leg's guard.

Where the records and the source disagreed:

- The analysis record's table gives `2 + 100` processes for dDeclaredLoop's parents. Its two
  parents hold 80 and 45 tracked specs at `8db6f4bef`, so the read is 2 and 125.
- Its section 5 says the door has no child to fail when git cannot start. `read_tree` runs git
  before the report on both paths, so that case does not differ; only the Python child's own start
  does.
- Its refusal list omits two the instrument also makes: a failed git call in `run_git`, and a build
  folder that does not exist in `write_packet`. Neither is touched.
- Its reading of `report` cites two reads of `specs`; there is a third, a count.
- The brief asks for `check-arms` over the new suite. That gate's population excludes it, as §4
  states.
- The brief and the prototype read the parents through one `cat-file` process for the run. This
  design makes one per parent build, to reuse the kit's reader.

Recall terms used: `python tools/memory-recall/query.py "make the packet instrument's check and
write fast without moving a pinned instrument's blob" --terms "packet instrument pinned blob repin
carries report history walk cat-file batch read_blobs_at spawn per spec dispatch spec tokens packet
join front door"`
