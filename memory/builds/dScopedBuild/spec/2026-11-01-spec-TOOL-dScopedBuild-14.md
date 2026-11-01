# TOOL-dScopedBuild-14 — the deviation gate under `deviation.gate`, at the commit and at the Build exit

**Status:** DEFERRED · rev-3 · 2026-11-01 · node a · Tier-2 · base f4597719 · streams tooling · order 2 · advances TOOL-dScopedBuild-16

**Carries:** cl-dClosedLoop-0412@021fa28b whole
**Carries:** node:policy-key.deviation.gate

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-01-build-TOOL-dScopedBuild-1-agent-ledger.md](../build/2026-11-01-build-TOOL-dScopedBuild-1-agent-ledger.md) | journal | TOOL-dScopedBuild-1 TOOL-dScopedBuild-2 TOOL-dScopedBuild-3 TOOL-dScopedBuild-4 TOOL-dScopedBuild-5 TOOL-dScopedBuild-6 TOOL-dScopedBuild-7 TOOL-dScopedBuild-8 TOOL-dScopedBuild-9 TOOL-dScopedBuild-10 TOOL-dScopedBuild-11 TOOL-dScopedBuild-12 TOOL-dScopedBuild-13 TOOL-dScopedBuild-15 TOOL-dScopedBuild-25 TOOL-dScopedBuild-26 TOOL-dScopedBuild-27 TOOL-dScopedBuild-28 TOOL-dScopedBuild-29 TOOL-dScopedBuild-30 TOOL-dScopedBuild-31 TOOL-dScopedBuild-32 TOOL-dScopedBuild-33 TOOL-dScopedBuild-34 TOOL-dScopedBuild-35 TOOL-dScopedBuild-36 TOOL-dScopedBuild-37 TOOL-dScopedBuild-38 TOOL-dScopedBuild-39 TOOL-dScopedBuild-40 TOOL-dScopedBuild-41 TOOL-dScopedBuild-42 TOOL-dScopedBuild-43 |
| [2026-11-01-build-TOOL-dScopedBuild-1-reuse-scout-a.md](../build/2026-11-01-build-TOOL-dScopedBuild-1-reuse-scout-a.md) | research | TOOL-dScopedBuild-1 TOOL-dScopedBuild-6 TOOL-dScopedBuild-7 TOOL-dScopedBuild-15 |
| [2026-11-01-build-TOOL-dScopedBuild-1-spec-stage-returns.md](../build/2026-11-01-build-TOOL-dScopedBuild-1-spec-stage-returns.md) | research | TOOL-dScopedBuild-1 TOOL-dScopedBuild-2 TOOL-dScopedBuild-3 TOOL-dScopedBuild-4 TOOL-dScopedBuild-5 TOOL-dScopedBuild-6 TOOL-dScopedBuild-7 TOOL-dScopedBuild-8 TOOL-dScopedBuild-9 TOOL-dScopedBuild-10 TOOL-dScopedBuild-11 TOOL-dScopedBuild-12 TOOL-dScopedBuild-13 TOOL-dScopedBuild-15 |
| [2026-11-01-prompt-TOOL-dScopedBuild-1-fix-brief.md](../prompts/2026-11-01-prompt-TOOL-dScopedBuild-1-fix-brief.md) | research | TOOL-dScopedBuild-1 TOOL-dScopedBuild-3 TOOL-dScopedBuild-6 TOOL-dScopedBuild-9 TOOL-dScopedBuild-10 TOOL-dScopedBuild-11 TOOL-dScopedBuild-13 TOOL-dScopedBuild-15 |
| [2026-11-01-prompt-TOOL-dScopedBuild-1-spec-brief.md](../prompts/2026-11-01-prompt-TOOL-dScopedBuild-1-spec-brief.md) | research | TOOL-dScopedBuild-1 TOOL-dScopedBuild-2 TOOL-dScopedBuild-3 TOOL-dScopedBuild-4 TOOL-dScopedBuild-5 TOOL-dScopedBuild-6 TOOL-dScopedBuild-7 TOOL-dScopedBuild-8 TOOL-dScopedBuild-9 TOOL-dScopedBuild-10 TOOL-dScopedBuild-11 TOOL-dScopedBuild-12 TOOL-dScopedBuild-13 TOOL-dScopedBuild-15 |
| [2026-11-01-review-TOOL-dScopedBuild-1-spec-audit-round1.md](../reviews/2026-11-01-review-TOOL-dScopedBuild-1-spec-audit-round1.md) | spec-audit | TOOL-dScopedBuild-1 TOOL-dScopedBuild-10 TOOL-dScopedBuild-11 TOOL-dScopedBuild-12 TOOL-dScopedBuild-13 TOOL-dScopedBuild-15 TOOL-dScopedBuild-2 TOOL-dScopedBuild-3 TOOL-dScopedBuild-4 TOOL-dScopedBuild-5 TOOL-dScopedBuild-6 TOOL-dScopedBuild-7 TOOL-dScopedBuild-8 TOOL-dScopedBuild-9 |

<!-- /gen:spec-records -->

## 1. Goal

dTrueNorth's deviation join lists every unrecorded departure and never moves an exit, because its
host runs a constant, `report` (`tools/memory-tree/deviation_join.py:144`). This unit makes the join a
gate: the value of `deviation.gate` decides whether an unrecorded deviation is refused, warned with an
ask, or reported, at the push where the join is hosted today, at the commit through a new staged
verb, and at the Build exit beside `build.scope`, each value seen on its planted case (FQ-3, P41).

## 2. Scope (IN)

- **S1** — The I4 read in Python: `read_gate_value(key, repo)` in `tools/memory-tree/routed_commits.py`
  runs `python <policy kit>/policy.py get <key>` in `repo` by subprocess, the kit found by
  `backlog.resolve_kit_dir("policy", "policy.py", …)` as `read_gen_region_awk` finds the unattended kit
  (`deviation_join.py:369-372`), and returns the one value it prints. A kit that does not resolve, a
  `get` exit 2 and a value outside the catalogue row's `allowed` are each a `Refusal` naming the key,
  so the leg exits 2 and never reads a default it did not see. Every call site passes the key as a
  string literal first, `read_gate_value("deviation.gate", repo)`, the shape the policy kit's
  reader-coverage arm counts (`tools/policy/check_policy.py:423-435`). Observed by AC1, AC10.
- **S2** — The I5 renderer: `render_gate_outcome(key, value, findings)` in `routed_commits.py`, pure,
  `findings` a list of `(subject, accept)` pairs, returns `(rc, lines)`: under `refuse` rc 1 and one
  `<key> refuse — <n> finding(s) refused` line; under `warn-and-ask` rc 0 and one
  `ask · <key> · <subject> · accept <accept>` line per finding; under `report` rc 0 and one
  `<key> report — <n> finding(s) listed` line; no finding is rc 0 and one `<key> <value> — clean`
  line under every value. `build.scope`'s arms call the same function (TOOL-dScopedBuild-3). Observed
  by AC2.
- **S3** — The join's own values: `POLICIES` (`deviation_join.py:142`) reads `("refuse",
  "warn-and-ask", "report")`, the catalogue row's order, and the CLI's `--policy` takes them, its
  default the key's value through S1 rather than `report`. A pure `read_finding_addresses(result,
  commit, close)` lists, in render order, each member and record `render_lines` (`:775`) counts, so its
  length equals that function's count. The constant `HOST_POLICY` is retired: `read_host_lines` (`:811`)
  takes the value as an argument and returns `(lines, findings)`.
  **Readers:** by name: `HOST_POLICY` in `tools/memory-tree/deviation_join.py` (`:144`, `:823`,
  `:825`). by value: `tools/memory-tree/routed_commits.py`, whose docstring and
  `check_deviation_join` docstring say the host runs `report` and never moves the exit (`:47-50`,
  `:339-341`), and `tools/memory-tree/README.md`'s `deviation_join.py` row. Observed by AC3.
- **S4** — The push: `check_deviation_join` (`routed_commits.py:334`) reads the key once through S1,
  renders the RANGE half (late and nobody in the range) and the WHOLE half (every unjoined member,
  refused approver, malformed record and late record) through S2, and returns `(rc, lines)`;
  `check_routed_commits` (`:242`) exits 1 when its own grade or the gate's rc is 1. An off join is rc 0
  and its one line, as today. Observed by AC4, AC5.
- **S5** — The Build exit host: `routed_commits.py --build <slug>` grades the RANGE half alone over
  `B..HEAD`, B from `read_build_base` (TOOL-dScopedBuild-1 S2), keeping only the deviation members
  whose `build` is the slug, through S2; a build with no first pass grades over `$GATE_PUSH_BASE..HEAD`
  as the driver sets it. It is the one Build-exit mode of `routed_commits.py`: TOOL-dScopedBuild-3 S7
  adds its scope arm and the `--write` flag that writes the `scope` record to this mode, and
  TOOL-dScopedBuild-9's touch join runs inside that arm, so no second exit mode is minted. It exits 1
  when any arm it runs refuses. `check_build_exit` (TOOL-dScopedBuild-1 S4) runs it once, inside the
  function and never in a verb body, with `GATE_PUSH_BASE=$BX_BASE`, refuses on its exit 1 naming the
  lines, refuses on its exit 2, and hands every `ask ·` line to S6. Observed by AC6, AC7.
- **S6** — `write_gate_asks <slug> <lines>` in `tools/unattended/unattended.sh`, the one filer of a
  gate's `ask ·` lines, for this key and `build.scope` alike: per line it mints the id through
  `derive_ask_seq` (`:9780`) in the roster's family, composes the ask, SEV and KEEP rows as
  `write_inherited_asks` (`:10020`) does, reuses an OPEN ask whose row names the same subject, and files
  through `write_ask_rows` (`:9984`), dark when `ASKS_CMD` is blank. It writes no row itself. Observed
  by AC7.
- **S7** — The commit, I11: a verb `deviation_join.py --staged`, run at the root, reads the staged
  spec paths from `git diff --cached --name-status -M`. With no spec staged it prints one held line and
  exits 0. Its deviation arm, armed by the key rule as the join is, takes each staged revision of a
  chain-build spec that `check_material` (`:436`) reads as material between its `HEAD` blob and its
  index blob, read in one `read_blobs_at` batch; the revision is a member where the unit has a first
  pass in `HEAD`'s history or an audit pin, read from `read_population`'s facts, which gain `first` and
  `pins`; its address is `<unit>@rev-<N>`, N the `HEAD` blob's revision, joined against
  `read_records`, which reads a staged record. The findings go through S2 under the key. Exit 0, 1 on
  a refusal, 2 nothing measured. Observed by AC8.
- **S8** — Hygiene check 32, "a staged spec revision answers to `deviation.gate`", in
  `tools/memory-tree/check-memory-hygiene.sh` after check 30: under `--staged` it runs S7 and prints
  its lines, failing 32 on exit 1 and on exit 2 as checks 29 and 30 fail on theirs (`:1812-1822`,
  `:1853-1863`); on a full run it prints one line saying the staged set is its population and the
  push range is the routed-commits leg's, and passes. `.githooks/pre-commit` already runs `--staged`
  whenever `memory/**` is staged (`:226-233`). Its entry joins the check catalogue of
  `tools/memory-tree/HYGIENE.template.md`, rendered to `memory/HYGIENE.md`. Observed by AC9.
- **S9** — The key's row (`tools/policy/catalogue.toml:950-953`) gains its `summary` and `usage`, and
  `python tools/policy/policy.py lists --write` drains `deviation.gate` from
  `tools/policy/unsummarised-keys.txt` (`:60`); its values and default stay as written. `help/policy.md`
  names the deviation gate as the key's consumer beside the two families it names (`:8-14`). Observed
  by AC10.
- **S10** — gov's own value, §8 F1: the ask the main loop files asks the owner to commit `[deviation]`
  `gate = "report"` to `.governance/policy.toml`, the value decision PLAY-dClosedLoop-4 sets for the
  chain. NOT OBSERVED by this unit: the write is the owner's, because the policy guard refuses an
  agent's commit to that path (`tools/policy/guarded-paths.txt:5`); AC11 observes the interim.

## 3. Non-goals (OUT)

- The approval grade `deviation.approval`, dDeclaredLoop's key: `HOST_APPROVAL` stays the chain's
  `author-recorded` until that build re-points it.
- The ledger, rescope, hand-back and clause arms at the commit. S7 grades the two revision arms over
  the staged specs; every arm is graded per commit at the push by S4's RANGE half, as today.
- The frozen-spec arm of the same verb and check: TOOL-dScopedBuild-2.
- `build.scope` itself and its arms in the host: TOOL-dScopedBuild-3, which calls S1, S2 and S6.
- The departures report, `deviations.py --report`: the instrument's.
- Writing `.governance/policy.toml`: the owner's (S10).
- A new gate leg: the push half lives in the routed-commits leg and the commit half in check 32.

### Edges

- **consumes-from** `TOOL-dScopedBuild-1` — `check_build_exit` and `--build-exit`, the exit host S5's
  call joins, with `BX_BASE`; and `read_build_base`, the base `--build` reads; without them the gate
  has no Build exit to read at
- **hands-off** `TOOL-dScopedBuild-2` — `--staged`, the I11 verb and check 32, whose frozen arm that
  unit adds beside the deviation arm
- **hands-off** `TOOL-dScopedBuild-3` — `policy.py get`, read through `read_gate_value`, with
  `render_gate_outcome` and `write_gate_asks`, the one renderer and the one filer `build.scope` calls,
  and `--build`, the one Build-exit mode its scope arm and `--write` join
- **hands-off** external — the owner's commit of gov's `deviation.gate` value (S10), filed as an ask
- **hands-off** `TOOL-dScopedBuild-27` — S6's `write_gate_asks` and S2's `render_gate_outcome`, the exit-time filer and the push's ask lines that unit observes over units 3's and 9's fixtures (id 3)
- **hands-off** `TOOL-dScopedBuild-28` — S8's check 32 and S7's `--staged` verb, which that unit's widened pre-commit trigger reaches on a deletion-only commit (id 14)
- **hands-off** `TOOL-dScopedBuild-30` — S1's `read_gate_value`, which that unit answers with `read_policy_value`, `check_gate_value` and the `PolicyRefused` exit 2, superseding AC1 and AC10's third clause (id 19)
- **hands-off** `TOOL-dScopedBuild-35` — AC7's fixture, S2; §5's commit-time cost, S4; AC9's command, S8; the core asks S6 files, S11; S7's staged population, S19; S6's dedupe key, S32; and the asks' log prefix, S34 (ids 5, 15, 12, 26, 37, 50, 8)
- **hands-off** `TOOL-dScopedBuild-36` — S6's `write_gate_asks` and AC7's slug fixture with `ASKS_CMD` declared, over which that unit's S4 shows the filer stages a row (id 11)
- **hands-off** `TOOL-dScopedBuild-39` — S1's `read_gate_value`, which this unit's builder does not mint, reading through `read_policy_value` and minting `check_gate_value` in TOOL-dScopedBuild-30 S2's spelling, as that unit's S8 rules (id 5)

## 4. Design

### Evidence

Read at `5f0b11f12`; no product file differs from base `f4597719`.

- `HOST_POLICY, HOST_APPROVAL = "report", "author-recorded"` (`deviation_join.py:144`) is read only at
  `:823` and `:825`, inside `read_host_lines`, which discards `render_lines`' count, so the host lists
  and never moves the exit (`routed_commits.py:330-331`).
- The CLI already refuses under `--policy refuse` (`deviation_join.py:1795`), and the fixture's
  `pass-revision` plant reds under it (`PLANT_EXITS`, `:1351`).
- `policy.py get` reads the landed revision, `refs/remotes/<remote>/<branch>` (`derive_landed_revision`,
  `tools/policy/policy.py`), and prints the catalogue default `refuse` where gov's policy file sets no
  `deviation.gate`; gov's `.governance/policy.toml` sets none.
- The policy guard lists `.governance/policy.toml` (`tools/policy/guarded-paths.txt:5`), and the
  pre-commit hook refuses an agent's commit to a listed path (`.githooks/pre-commit:186-224`).
- The reader-coverage arm counts a Python call whose first argument is the key literal
  (`check_policy.py:423-435`), and a shell `policy.py get <key>`.
- `.githooks/pre-commit` names neither `deviation_join` nor `routed_commits`; "at the commit" in the
  join's docstring is the per-commit join run at the push (scout C disagreement 3).
- Check 31 is claimed by TOOL-dIndexedDesign-13 S8; no tracked spec claims 32 (§8 F4).

### The three values, where each is read

| Where | Host | Population | `refuse` | `warn-and-ask` | `report` |
|---|---|---|---|---|---|
| commit | check 32, `deviation_join.py --staged` | staged revisions past a pass or pin | commit refused | commit passes, each ask line printed, filed at the exit | commit passes, listed |
| push | routed-commits leg, `check_deviation_join` | RANGE and WHOLE halves | leg red | leg green, ask lines printed | leg green, listed |
| Build exit | `check_build_exit`, `routed_commits.py --build <slug>` | the build's members departing in `B..HEAD` | exit refused | exit passes, asks filed by `write_gate_asks` | exit passes, listed |

The ask is filed at the exit alone (§8 F2). An ask's subject reads `unrecorded deviation: <address>
(<hand>) departing at <sha8>`, its accept `a deviation record departing from <address> joins it, or
the departure is reverted`.

### The staged verb

```
deviation_join.py --staged
  staged = git diff --cached --name-status -M        # one spawn
  no spec path staged            -> "deviation: --staged · held — no spec is staged", exit 0
  deviation arm (key rule armed): read_population(root, conf, read_routed_commits(root, ["HEAD"]))
      for each staged chain-build spec with a HEAD blob, material by check_material(HEAD, index):
          member when facts.first or facts.pins holds its unit; address <unit>@rev-<N at HEAD>
      findings = members no record in read_records joins
      rc, lines = render_gate_outcome("deviation.gate", read_gate_value("deviation.gate", root), findings)
```

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `read_gate_value` | python function, `routed_commits.py` | `py.function`, OK |
| `render_gate_outcome` | python function, `routed_commits.py` | `py.function`, OK |
| `read_finding_addresses` | python function, `deviation_join.py` | `py.function`, OK |
| `write_gate_asks` | shell function, `unattended.sh` | `sh.function`, OK |
| `--staged` | mode of `deviation_join.py` | none |
| `--build` | mode of `routed_commits.py` | none |
| check 32 | hygiene check | none |
| `staged-revision`, `staged-recorded`, `staged-status` | `deviation_join.py` fixture plants | none |

### Rollout

Live at landing. gov reads the landed value, so until the owner's `report` lands (S10) gov's push,
commit and exit read `refuse`, the catalogue default: an unrecorded deviation then stops the push
that carries it, which fails closed. The build pass measures the WHOLE half's findings at its base
(AC11) so the landing knows the count before it runs.

### Files touched (estimate)

- `tools/memory-tree/deviation_join.py`: S3, S7, the plants and their arms, the docstring
- `tools/memory-tree/routed_commits.py`: S1, S2, S4, S5, the docstring, its selftest arms
- `tools/memory-tree/check-memory-hygiene.sh`: S8
- `tools/memory-tree/check-memory-hygiene.test.sh`: S8's arm
- `tools/memory-tree/HYGIENE.template.md` and its render `memory/HYGIENE.md`: S8
- `tools/memory-tree/README.md`: the two rows S3's readers name
- `tools/unattended/unattended.sh`: S5's call in `check_build_exit`, S6
- `tools/unattended/unattended.test.sh`: S5 and S6's arms
- `tools/policy/catalogue.toml` and `tools/policy/unsummarised-keys.txt`: S9
- `help/policy.md`: S9

### Alternatives rejected

- **A gov override constant beside the key.** Lost to §8 F1: a second channel for one value, the
  defect `[one-fact]` names, and the clause says "as the key says".
- **The ask written at the commit by the hook.** Lost to §8 F2: a pre-commit hook writing
  `BACKLOG.md` changes the index of the commit it grades.
- **The exit reading the bar's routed-commits leg output.** Lost to S5: the bar prints the leg's
  lines inside its own log, the gate's rc is folded into the leg's, and the WHOLE half grades every
  chain build's members, not the exiting build's.
- **A `read_policy_value(key, root)` in `tools/playbook/policy_value.py`.** It does not exist
  (scout A disagreement 4); the landed reader is `policy.py get`, which S1 calls.

## 5. Production-readiness checklist

- security — deny by default: an unresolved policy kit, a refused `get` and an out-of-set value each
  exit 2; the value is read at the landed revision, so an uncommitted edit cannot open the gate.
- perf / scale — check 32 reads history only when a spec is staged: one log pass (0.9 s over 7300
  commits, PINNED at `5f0b11f12`) and the population read the push already pays.
- error / empty / loading states — no staged spec is one held line; an off join is one line; no
  finding is a `clean` line under every value.
- observability — every outcome line names the key, its value and the count.
- risks — the interim `refuse` (§4 Rollout); a `warn-and-ask` ask is filed only where an exit runs.
- testing — the arms of §7, each value on a planted fixture whose landed revision holds the policy
  file naming it.
- migration — none; no record changes.
- user docs — `help/policy.md` and `memory/HYGIENE.md` through its template.

## 6. Acceptance criteria

- **AC1** — When `read_gate_value("deviation.gate", root)` runs in a fixture repository whose landed
  revision holds no policy file it returns `refuse`; with one setting `[deviation]` `gate =
  "report"` it returns `report`; with the policy kit unresolved it raises `Refusal`.
  Red when: an unread key returns a value, or the landed value is not the one returned.
  fixture: built by the selftest; the file is committed on the commit the remote's `main` names.
- **AC2** — When `render_gate_outcome("deviation.gate", v, [("s", "a")])` runs, `refuse` returns rc 1,
  `warn-and-ask` rc 0 with one `ask · deviation.gate · s · accept a` line, `report` rc 0 with one
  listed line; with no finding every value returns rc 0 and a `clean` line.
  Red when: `warn-and-ask` returns no ask line, or `report` returns rc 1.
- **AC3** — When `grep -c HOST_POLICY tools/memory-tree/deviation_join.py` runs it prints 0, and
  `len(read_finding_addresses(...))` equals `render_lines(...)[1]` on every plant of the fixture.
  Red when: the constant survives, or the address list and the count disagree.
- **AC4** — When `python deviation_join.py --fixture --plant pass-revision --host routed-commits` runs
  with the fixture's landed revision setting `gate = "refuse"`, it exits 1 naming
  `deviation.gate refuse`; under `"warn-and-ask"` it exits 0 printing an `ask · deviation.gate` line
  naming the revision's address; under `"report"` it exits 0 listing it.
  Red when: a value is not read from the planted policy file, or `refuse` exits 0.
  fixture: the join's own fixture, its base commit holding `.governance/policy.toml`.
- **AC5** — When the same `--host` run takes `--plant status-only` under each of the three values, it
  exits 0 with a `clean` line.
  Red when: a status-only revision is a finding under any value.
- **AC6** — When `routed_commits.py --build dFixA` runs in the fixture after `pass-revision` under
  `refuse`, it exits 1; a member of `dFixB` departing in the same range moves nothing.
  Red when: another build's member refuses this build's exit, or the build's own member passes.
- **AC7** — When `check_build_exit` runs in the driver suite's fixture over a green bar and a host
  stub printing one `ask · deviation.gate · s · accept a` line with rc 0, it returns 0 and
  `write_gate_asks` stages one ask row in the slug's `BACKLOG.md` that the ask generator reads back;
  with the stub's rc 1 it returns 1 naming the gate.
  Red when: a `warn-and-ask` exit files no ask, or a refusing gate passes the exit.
  fixture: the driver suite's slug fixture with `ASKS_CMD` declared.
- **AC8** — When `python deviation_join.py --fixture --plant staged-revision --staged` runs, the plant
  staging a material revision of a passed unit's spec with no record, it exits 1 under `refuse`, 0
  with an ask line under `warn-and-ask` and 0 listing it under `report`; `--plant staged-recorded`,
  its record staged beside it, and `--plant staged-status`, a status-only edit, exit 0 under `refuse`.
  Red when: a planted unrecorded staged revision passes under `refuse`, or a joined one is refused.
- **AC9** — When `bash tools/memory-tree/check-memory-hygiene.sh --staged --only 32` runs in this
  tree with no spec staged, it prints the held line and exits 0; on a full run with `--only 32` it
  prints its population line and exits 0.
  Red when: check 32 is absent, or reads the full tree under `--staged`.
- **AC10** — When `python tools/policy/policy.py get deviation.gate` runs it prints the landed value;
  after `policy.py lists --write`, `grep -c deviation.gate tools/policy/unsummarised-keys.txt` prints 0;
  `grep -c 'read_gate_value("deviation.gate"' tools/memory-tree/routed_commits.py` prints at least 1.
  Red when: the row lacks `summary` or `usage`, or no literal reader exists.
- **AC11** — When the pass runs `python tools/memory-tree/deviation_join.py --policy report` over this
  tree at its base, its summary line's unjoined, refused, malformed and late counts are written to
  the unit's acceptance ledger.
  Red when: the ledger records no count.
  figure: DERIVED at the pass's base; no reading is pinned here.

## 7. Gates

`routed commits name a specced unit` · `routed-commits selftest` · `memory hygiene` · `memory-hygiene self-test` · `unattended kit gate` · `policy check` · `policy fixtures` · `kit/dogfood doc parity` · `recall floor` · `recall floor arms` · `kit version markers` · `harness arms (fail branches armed or pinned)` · `spec tokens (a spec's own names resolve)`

New arm: tools/memory-tree/deviation_join.py · covers AC3 AC4 AC5 AC6 AC8 · the selftest's plants under each committed value, the three staged plants among them, its failing case `pass-revision` under `refuse` exiting 0 · none

New arm: tools/memory-tree/routed_commits.py · covers AC1 AC2 · the selftest's policy-file fixture and the renderer over each value, its failing case `warn-and-ask` printing no ask line · none

New arm: tools/unattended/unattended.test.sh · covers AC7 · the exit over a host stub at rc 0 with one ask line and at rc 1, its failing case a filed-nothing `warn-and-ask` · none

New arm: tools/memory-tree/check-memory-hygiene.test.sh · covers AC9 · a scratch tree staging a planted revision under `refuse`, its failing case check 32 passing it · none

## 8. Open questions

- **F1 — Does gov's policy file declare a `deviation.gate` value, and who writes it?** Options: (a)
  gov declares `report`, the value decision PLAY-dClosedLoop-4 gives the chain, committed by the owner
  because the policy guard refuses an agent's commit to `.governance/policy.toml`, filed as an ask, the
  landed value `refuse` until it lands; (b) a gov override constant in the host; (c) no declaration,
  gov running the catalogue default for good. (b) is a second channel for one value and fails the
  clause's "as the key says"; (c) contradicts the owner's ruling the spec quotes. RESOLVED (agent,
  2026-11-01, delegated): (a), rung 3, the survivor; the main loop files the ask once, target this build's `BACKLOG.md`: "GOV'S POLICY FILE DECLARES NO `deviation.gate`. TOOL-dScopedBuild-14 reads the key at the landed revision, whose catalogue default is `refuse`, and decision PLAY-dClosedLoop-4 runs the chain at `report`; the policy guard refuses an agent's commit to `.governance/policy.toml`", accept "`.governance/policy.toml` on the default branch sets `[deviation]` `gate = 'report'`, seen as `policy.py get deviation.gate --explain` naming the file as its source". widens: none · relaxes: none
- **F2 — Where is a `warn-and-ask` ask filed?** Options: (a) at the Build exit, by the driver's
  `write_gate_asks`, the commit and the push printing the line; (b) at the commit, by the hook; (c) at
  the push. (b) has a hook write the index of the commit it grades, and (c) has the pre-push hook write
  a tree it is pushing. RESOLVED (agent, 2026-11-01, delegated): (a), rung 3. widens: none · relaxes: none
- **F3 — Which arms does the commit grade?** Options: (a) the two revision arms over the staged specs,
  the record-borne arms graded per commit at the push; (b) every arm over the staged set. Both meet
  every criterion and leave nothing uncovered, since the push's RANGE half grades each commit; (a) has
  fewer open questions, because a staged rescope, ledger or hand-back row has no departing commit to
  date it by. RESOLVED (agent, 2026-11-01, delegated): (a), rung 3, the tie-break. widens: none · relaxes: none
- **FACT-QUESTION · F4 — Which hygiene check number does I11 take?** Probe: `git grep -nE "hygiene check 3[0-9]" -- 'memory/builds/*/spec/*.md'`
  and the `check_selected` numbers in
  `tools/memory-tree/check-memory-hygiene.sh`. The observation that decides it: the highest
  `check_selected` is 30 and the probe names 31 in TOOL-dIndexedDesign-13 S8 and no other number.
  Liveness: the probe returns that hit, so it can return a claim. RESOLVED (agent, 2026-11-01,
  delegated): 32; grants: PLAY-dClosedLoop-3 the hygiene gate gains check 32. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft, from the packet's Items 14, v2:1292, final-questions FQ-3, scout
  A's row for this unit and its disagreements 2 and 3, scout C's disagreement 3, and the spec brief's
  I4, I5 and I11.
- rev-2 · 2026-11-01 · §3 · the Edges block gains the bullets mirroring the edges of TOOL-dScopedBuild-27, TOOL-dScopedBuild-28, TOOL-dScopedBuild-30, TOOL-dScopedBuild-35, promoted by the round-1 spec audit's disposal; nothing else moved.
- rev-3 · 2026-11-01 · §3 · the Edges block gains the bullets mirroring the edges of TOOL-dScopedBuild-36 and TOOL-dScopedBuild-39,
  the promotions of the round-1 spec audit of units 25 to 35 (ids 5, 11).

## 10. Reuse audit

The seams extended are `check_deviation_join` (`tools/memory-tree/routed_commits.py:334`), the host the
join already runs in; `render_lines` (`tools/memory-tree/deviation_join.py:775`) and `read_population`
(`:492`), read and never copied; `check_material` (`:436`) for the staged revision; `policy.py get`
(`tools/policy/policy.py`, `cmd_get`) as the one key reader; and `derive_ask_seq` with `write_ask_rows`
(`tools/unattended/unattended.sh:9780`, `:9984`) as the one ask writer, composed as
`write_inherited_asks` (`:10020`) composes them. `python tools/codebase-map/reuse_lookup.py "read a
policy key value and refuse, warn with an ask, or report an unrecorded deviation at the commit"`
ranked name-token helpers (`read`, `read_text`, `key`, `report`) and `read_spec_revisions`; none
grades an outcome by a key, so the renderer is new and every reader it calls exists. Scout A's row
holds against source at `5f0b11f12`; its "join runs at the close" claim does not, as its own
disagreement 2 says: `unattended.sh` never calls the join. The recall probe surfaced
TOOL-dTrueNorth-4 §3, which reserves this re-point for dScopedBuild, and decision PLAY-dClosedLoop-4,
which F1 reads.

Recall terms used: `python tools/memory-recall/query.py "how is the deviation join graded at the commit and at the build exit by deviation.gate" --terms "deviation.gate refuse warn-and-ask report HOST_POLICY deviation_join routed_commits staged pre-commit write_ask_rows"`
