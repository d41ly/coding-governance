# TOOL-dWitnessedBar-65 — the round-1 audit of unit 63, its 22 minors batched: one containment rule in three readers, plants a leg runs, a seed order that never stalls, honest seed and sweep failures, and readers that keep every normalisation

**Status:** CLOSED · rev-5 · 2026-11-21 · node d · Tier-2 · base cdfbd1cf · streams tooling · order 37 · advances TOOL-dWitnessedBar-31

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md) | journal | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-54 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 TOOL-dWitnessedBar-58 TOOL-dWitnessedBar-59 TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-61 TOOL-dWitnessedBar-62 TOOL-dWitnessedBar-63 TOOL-dWitnessedBar-64 TOOL-dWitnessedBar-66 TOOL-dWitnessedBar-67 TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-71 TOOL-dWitnessedBar-72 TOOL-dWitnessedBar-73 TOOL-dWitnessedBar-74 TOOL-dWitnessedBar-75 TOOL-dWitnessedBar-76 TOOL-dWitnessedBar-77 TOOL-dWitnessedBar-78 TOOL-dWitnessedBar-79 TOOL-dWitnessedBar-80 TOOL-dWitnessedBar-81 TOOL-dWitnessedBar-82 TOOL-dWitnessedBar-83 TOOL-dWitnessedBar-84 TOOL-dWitnessedBar-85 TOOL-dWitnessedBar-86 TOOL-dWitnessedBar-87 TOOL-dWitnessedBar-88 TOOL-dWitnessedBar-89 TOOL-dWitnessedBar-90 TOOL-dWitnessedBar-91 TOOL-dWitnessedBar-92 TOOL-dWitnessedBar-93 TOOL-dWitnessedBar-94 TOOL-dWitnessedBar-95 TOOL-dWitnessedBar-96 TOOL-dWitnessedBar-97 TOOL-dWitnessedBar-106 TOOL-dWitnessedBar-107 TOOL-dWitnessedBar-108 TOOL-dWitnessedBar-109 TOOL-dWitnessedBar-110 |
| [2026-10-25-build-TOOL-dWitnessedBar-64-round5-fix-return.md](../build/2026-10-25-build-TOOL-dWitnessedBar-64-round5-fix-return.md) | research | TOOL-dWitnessedBar-64 |
| [2026-10-25-build-TOOL-dWitnessedBar-65-deviation-651.md](../build/2026-10-25-build-TOOL-dWitnessedBar-65-deviation-651.md) | deviation | — |
| [2026-10-25-build-TOOL-dWitnessedBar-65-deviation-652.md](../build/2026-10-25-build-TOOL-dWitnessedBar-65-deviation-652.md) | deviation | — |
| [2026-11-19-build-TOOL-dWitnessedBar-65-1-acceptance-ledger.md](../build/2026-11-19-build-TOOL-dWitnessedBar-65-1-acceptance-ledger.md) | journal | — |
| [2026-11-19-build-TOOL-dWitnessedBar-65-1-builder-return.md](../build/2026-11-19-build-TOOL-dWitnessedBar-65-1-builder-return.md) | journal | — |
| [2026-11-21-build-TOOL-dWitnessedBar-65-deviation-653.md](../build/2026-11-21-build-TOOL-dWitnessedBar-65-deviation-653.md) | deviation | — |
| [2026-11-21-build-TOOL-dWitnessedBar-65-widen-8.md](../build/2026-11-21-build-TOOL-dWitnessedBar-65-widen-8.md) | widen | — |
| [2026-10-25-prompt-TOOL-dWitnessedBar-64-round5-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dWitnessedBar-64-round5-fix-brief.md) | research | TOOL-dWitnessedBar-64 |
| [2026-11-19-prompt-TOOL-dWitnessedBar-51-spec-tokens-brief.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-51-spec-tokens-brief.md) | journal | TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-57 TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-62 TOOL-dWitnessedBar-63 TOOL-dWitnessedBar-67 TOOL-dWitnessedBar-73 TOOL-dWitnessedBar-78 TOOL-dWitnessedBar-84 TOOL-dWitnessedBar-88 |
| [2026-11-19-prompt-TOOL-dWitnessedBar-65-build-brief.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-65-build-brief.md) | journal | — |
| [2026-11-19-prompt-TOOL-dWitnessedBar-65-reground-brief.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-65-reground-brief.md) | journal | — |
| [2026-11-19-prompt-TOOL-dWitnessedBar-65-reground-spec-writer.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-65-reground-spec-writer.md) | journal | — |
| [2026-10-25-review-TOOL-dWitnessedBar-64-spec-audit-round1.md](../reviews/2026-10-25-review-TOOL-dWitnessedBar-64-spec-audit-round1.md) | spec-audit | TOOL-dWitnessedBar-64 |
| [2026-11-21-review-TOOL-dWitnessedBar-1-closing-diff-review-round1.md](../reviews/2026-11-21-review-TOOL-dWitnessedBar-1-closing-diff-review-round1.md) | diff-review | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-54 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 TOOL-dWitnessedBar-58 TOOL-dWitnessedBar-59 TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-61 TOOL-dWitnessedBar-62 TOOL-dWitnessedBar-63 TOOL-dWitnessedBar-64 TOOL-dWitnessedBar-66 TOOL-dWitnessedBar-67 TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-71 TOOL-dWitnessedBar-72 TOOL-dWitnessedBar-73 TOOL-dWitnessedBar-74 TOOL-dWitnessedBar-75 TOOL-dWitnessedBar-76 TOOL-dWitnessedBar-77 TOOL-dWitnessedBar-78 TOOL-dWitnessedBar-79 TOOL-dWitnessedBar-80 TOOL-dWitnessedBar-81 TOOL-dWitnessedBar-82 TOOL-dWitnessedBar-83 TOOL-dWitnessedBar-84 TOOL-dWitnessedBar-85 TOOL-dWitnessedBar-86 TOOL-dWitnessedBar-87 TOOL-dWitnessedBar-88 TOOL-dWitnessedBar-89 TOOL-dWitnessedBar-90 TOOL-dWitnessedBar-91 TOOL-dWitnessedBar-92 TOOL-dWitnessedBar-93 TOOL-dWitnessedBar-94 TOOL-dWitnessedBar-95 TOOL-dWitnessedBar-96 TOOL-dWitnessedBar-97 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of unit 63
(`memory/builds/dWitnessedBar/reviews/2026-10-25-review-TOOL-dWitnessedBar-63-spec-audit-round1.md`)
exited CONVERGED with 23 confirmed findings: one HIGH, which `TOOL-dWitnessedBar-64` takes, and 22
minors. BUILD-METHOD M4 batches every MEDIUM and LOW into one unit, or two only where they split into
disjoint write sets by M6's clauses so that both build concurrently. §4 "Why one unit" says why these
stay one. Each finding is named by report id and is its own scope item, including where the report
merged ids into one item. Every finding lands on `TOOL-dWitnessedBar-63`, so this unit repairs that
unit and builds after it (order 37, one step after `TOOL-dWitnessedBar-64`). The report's ids 4, 9 and 12 were refuted by the audit
itself and are no finding here.

Both units it repairs have landed, `TOOL-dWitnessedBar-63` at `44989eebd` and `TOOL-dWitnessedBar-64`
at `b26061af2`, and this spec is re-grounded over HEAD `76a3b4bc2`. Ten items are present at HEAD and
are observed, not built: S3 to S7, S14, S16, S19, S20 and S22. Nine are built: S1, S2, S8 to S11,
S15, S17 and S21. S12 and S13 are ledger lines at the close, and S18 is this spec's gate set.

| Report item | Severity | Report ids | Scope items |
|---|---|---|---|
| M1 | MEDIUM | 2, 7, 21 | S1, S2, S3 |
| M2 | MEDIUM | 3, 8 | S4, S5 |
| M3 | MEDIUM | 1 | S6 |
| M4 | MEDIUM | 15 | S7 |
| M5 | MEDIUM | 16 | S8 |
| M6 | MEDIUM | 23 | S9 |
| M7 | MEDIUM | 24 | S10 |
| M8 | MEDIUM | 22 | S11 |
| L1 | LOW | 5, 19 | S12, S13 |
| L2 | LOW | 17, 25 | S14, S15 |
| L3 | LOW | 10 | S16 |
| L4 | LOW | 26 | S17 |
| L5 | LOW | 6 | S18 |
| L6 | LOW | 11 | S19 |
| L7 | LOW | 13 | S20 |
| L8 | LOW | 14 | S21 |
| L9 | LOW | 18 | S22 |

That is 11 MEDIUM and 11 LOW findings by raw id.

## 2. Scope (IN)

- **S1** — id 2. One table of `exists:` forms is fed to all three readers by one arm, which fails on
  any disagreement. The arm is `tools/govkit/selftest.py#check_when_forms_agree`, which reads each
  refused form alone in its own tree through regen's `build_items`, lib-unattended's
  `resolve_generated_indexes` and `govkit.py selfcheck`. Present at HEAD: its rows hold unit 63's AC5
  forms `..\x`, `a\..\..\x`, `\x` and `\\server\share`, the colon form `a:b`, and the `a/../b` shape
  as its `dotdot` row. Left: the refused rows `a\..\b`, `a/..`, `x/..`, `1:x`, `C:x`, `.` and `./.`,
  and the admitted controls `a/b`, `a..b/c` and `.x/y` in its admissible tree, each naming no file.
  Each row states one expected outcome for all three readers, and the arm prints one line per form
  with the three outcomes. Observed by AC1.
- **S2** — id 7. The one rule, which makes unit 63's §5 "through one rule" true. With every `\` folded
  to `/`, a path is refused when it starts with `/`, when it holds a colon anywhere, when any `/`
  segment is exactly `..`, or when it normalises to `.`. Present at HEAD: lib-unattended's form
  (`tools/unattended/lib-unattended.sh#resolve_generated_indexes`) is
  `case "${p//\\//}" in /*|*:*|..|../*|*/..|*/../*)`, unit 63 S9 and its §8 F6 having widened this
  spec's second-character `:` to a colon anywhere. Left: the same branch refuses a folded path that
  the kit's own `normpath` reads as `.`, with unit 62 S21's line (§8 F5). Observed by AC1.
- **S3** — id 21. Present at HEAD (`TOOL-dWitnessedBar-63` S10, S11): govkit selfcheck's `exists:`
  check, `_check_exists_refused` inside `tools/govkit/govkit.py#selfcheck`, refuses where
  `tools/govkit/upgrade_steps.py#derive_contained_rel` returns None or the folded path holds a `..`
  segment, and `tools/run-gates/regen.py#check_when` applies that rule inline. Over a folded path it
  refuses what S2 refuses (§4 Evidence). So unit 62 S22, "holds a `..` segment is refused", stands in
  all three readers. This pass writes no Python reader. Observed by AC1.
- **S4** — id 3. Present at HEAD (`TOOL-dWitnessedBar-63` AC11): the verdict backends' plant loop in
  `tools/run-gates/run-gates.gov.test.sh`, run by the `run-gates gov canary` leg, calls
  `verdict_backends.py --fixture --plant key-no-tab` and owes its exit 1 with every scenario held.
  This pass writes none. Observed by AC3.
- **S5** — id 8. Present at HEAD (`TOOL-dWitnessedBar-63` AC12, its deviation 632): the same loop
  calls `--plant peer-no-ssh-keygen` and owes exit 0, and that plant ages a `gov-signers-` temp past
  `PEER_SIGNERS_GRACE_S` and owes it swept. The suite's `FLOOR_ASSERTIONS` moves only for this unit's
  own new assertions (§7). This pass writes none. Observed by AC3.
- **S6** — id 1. Present at HEAD: `TOOL-dWitnessedBar-47` sits at order 6, applied as its rev-5 with
  its §9 line (§8 F3), and `TOOL-dWitnessedBar-61` at order 5, both CLOSED. Unit 61's dispatch row
  precedes unit 47's in `memory/builds/dWitnessedBar/RUN.md`, and unit 61's pass commit `9c8821605` is
  an ancestor of unit 47's `14cf1b1bc` (DERIVED 2026-11-21 by AC4's commands). Unit 63 S14 records the
  same sequence, and unit 61's Rollout already names order 6 for unit 47. This pass writes none.
  Observed by AC4.
- **S7** — id 15. Present at HEAD (`TOOL-dWitnessedBar-63` AC23): section `2o` of
  `tools/lib/resolve-python.test.sh` reads unit 61 AC1's `HEAD is unborn` from the seed's stderr
  capture, `$LL/py.err`, which unit 63 S32 moved it to. This unit's §7 names
  `memory-hygiene self-test`, `codebase-map adopter e2e`, `codebase-map kit selftest` and
  `drift-audit selftest`. Those legs run the arms of units 46, 47 and 53, which unit 63's seed
  changes reach. This pass writes none. Observed by AC5.
- **S8** — id 16. `tools/lib/legacy_ledger.py#run_seed_cli` resolves the repository root with
  `git rev-parse --show-toplevel`, and at HEAD exits 2 with `legacy_ledger: not inside a git work tree`
  where none resolves. That case joins unit 63 S6's no-HEAD route before any registration or home is
  read, its reason the toplevel call's first stderr line or `git rev-parse exited <rc>`. Under
  `--population <name>` it prints `unarmed <name> no HEAD: <reason>` and the stderr line
  `legacy_ledger: <name>: no HEAD: <reason>; nothing written`. Under `--all`, stdout is empty and
  stderr carries `seed: no HEAD: <reason>`. Each exits 1 and writes nothing. Where the root resolves,
  the route keeps its landed order, the SHA resolved before registrations are read (§8 F6).
  Observed by AC6.
- **S9** — id 23. `tools/lib/legacy_ledger.py#_run_git` catches `subprocess.TimeoutExpired` beside
  `OSError`, and for either its text reads `git not runnable: <exception>`. So every git call of the
  seed's SHA resolution, S8's toplevel call included, takes the no-HEAD route with that reason. At HEAD
  it catches `OSError` alone and passes the exception's own text. A non-zero exit with empty stderr
  gives `git <verb> exited <rc>`, the form `TOOL-dWitnessedBar-64` S3 landed in `read_head_sha`.
  Present at HEAD: `seed --all` prints the no-HEAD line for every population it picks. Observed by AC7.
- **S10** — id 24. A given `--sha` is folded to lowercase, passes unit 63 S33's grammar `SHA_RE`, and
  then must resolve: `git rev-parse --verify --quiet <sha>^{commit}` exits 0 (§8 F7). The seed stamps
  the full lowercase SHA that call prints, so case and abbreviation fold to one spelling (§8 F4). The
  null SHA is admitted only where `read_head_sha` returns `NULL_SHA`, unit 64's unborn predicate.
  Anything else exits 2 naming `--sha` and writes no home. At HEAD `run_seed_cli` checks `SHA_RE`
  alone and stamps the value as given. Observed by AC8.
- **S11** — id 22. Unit 63 S20's sweep, `tools/run-gates/verdict_backends.py#remove_stale_signer_temps`,
  which `#read_signer_principal` runs on each peer read, touches regular files only
  (`is_file(follow_symlinks=False)`). Each unlink catches `OSError`: `FileNotFoundError` is silent, and
  any other error writes one stderr line naming the file. The read goes on either way, and its verdict
  never depends on the sweep. At HEAD the test follows a link and every `OSError` is silent.
  Observed by AC9.
- **S12** — id 5. Unit 63's AC18 is graded on its ledger half alone. Its three `grep -c` probes print
  1 at HEAD (PINNED 2026-11-21), so they cannot red, and at the close unit 63's AC18 ledger line names
  this item for that half. Observed by AC10.
- **S13** — id 19. The ledger half is checked. Unit 62's AC7 ledger line, owed to the close at HEAD,
  names each suite's own floor string: `run-gates evidence: executed`, `gov-canary: executed`,
  `adopt-e2e: executed`, and `FAIL executed` beside `check-memory-hygiene.test.sh` and no other suite.
  Observed by AC10.
- **S14** — id 17. Present at HEAD (`TOOL-dWitnessedBar-63` S17):
  `tools/run-gates/run-gates.sh#read_record_keys` reads each line whole, strips one trailing CR from the
  value with `${_rk_v%$'\r'}`, and on a repeated key the last line wins, since each match overwrites.
  This pass adds its arm. Observed by AC11.
- **S15** — id 25. Unit 63 S19's readers strip one trailing CR and keep the last of a repeated key.
  `.githooks/pre-push#read_green_file` reads each key with `awk -F'\t' '$1=="<key>"{print $2}'`, which
  prints every match and keeps the CR. Each read becomes an awk form that stores the value and prints
  it at `END` with one trailing CR stripped. Present at HEAD: the Python form,
  `tools/run-gates/verdict_backends.py#read_tag_lines`, overwrites on each match and strips the CR.
  Observed by AC12.
- **S16** — id 10. Present at HEAD (`TOOL-dWitnessedBar-63` S1, S3):
  `tools/run-gates/run-gates.gov.test.sh#check_bar_scrub_parity` strips `PM_SCRUB=` and every quote
  from what it reads, and the suite asserts the first and last names it read against the names on the
  assignment's first and last physical lines, `GIT_DIR` and `GATE_REUSE_DAY` (PINNED 2026-11-21 by
  AC13's figure). `GATE_TURNSTILE_HOLDER`, which rev-4 named last, is no longer last. This pass writes
  none. Observed by AC13.
- **S17** — id 26. The arm's `PM_SCRUB` reads, the list read in `check_bar_scrub_parity` and the
  last-name read beside it, run from the line opening `PM_SCRUB="` to the first line, that opening line
  included, holding the closing quote. They are written in awk rather than as a `sed` range. Text
  after the closing quote is discarded, and the arm fails on any token not matching
  `^[A-Z_][A-Z0-9_]*$`. At HEAD both use the range `/^PM_SCRUB="/,/"$/`, which never tests its opening
  line for the end and needs the quote to end a line. Observed by AC14.
- **S18** — id 6. This unit's §7 names `run-gates canary`, the suite that grades `regen.py`, and
  `pre-push bar self-test`, for the hook readers S15 changes. NOT OBSERVED: the item is this spec's
  declared gate set, which the close runs; no criterion of a unit observes its own §7.
- **S19** — id 11. Present at HEAD: unit 63's spec cites the code its builder needed by symbol,
  `tools/govkit/selftest.py#check_inherited_red_step` in its S16 and
  `tools/unattended/lib-unattended.sh#resolve_generated_indexes` in its S9 and S22, and holds no line
  cite into either file. NOT OBSERVED: these are corrections to spec text, and no built artifact
  carries them. §4 Evidence gives the grep that re-derives it.
- **S20** — id 13. Present at HEAD (`TOOL-dWitnessedBar-63` S10): selfcheck's `exists:` failure is its
  own line per row, naming the registry entry, the row's path and the `when` it got.
  `_check_exists_refused` reads `derive_contained_rel`'s None and never calls
  `tools/govkit/govkit.py#demand_contained_dest`, so that Refusal's fixed `.governance/deploy.toml`
  hint cannot reach the operator. This pass writes none. Observed by AC2.
- **S21** — id 14. The comment beside `PEER_SIGNERS_GRACE_S` in `tools/run-gates/verdict_backends.py`
  names `TAIL_GRACE_S` (`TOOL-dWitnessedBar-42`) as the same run-gates kit's bash constant for the
  tail sweep. It gives the constant's seven-day span and its bash side as the reasons it is not
  reused. `TAIL_GRACE_S=604800` is `tools/run-gates/run-gates.sh@76a3b4bc2:2767`, and
  `tools/run-gates/kit.toml` declares `id = "run-gates"` (`tools/run-gates/kit.toml@76a3b4bc2:11`) and
  `include = "**"` (`tools/run-gates/kit.toml@76a3b4bc2:23`). Observed by AC15.
- **S22** — id 18. Present at HEAD: unit 62's re-ground re-pinned its coverage figure to 96 at
  `4cf1a82ca`, so `grep -nw 77` over its spec prints only its records-table line naming
  `TOOL-dWitnessedBar-77` (PINNED 2026-11-21 by AC16's grep), and no 77-carrier is left to answer. Unit
  63 S4 answers unit 62's AC13 on the figure the built tree re-derives. This pass writes none.
  Observed by AC16.

## 3. Non-goals (OUT)

- Re-wording unit 63's spec text, or any other unit's. Each item is closed by what this pass builds or
  observes. A claim or criterion of unit 63 that an item replaces is answered in unit 63's ledger by
  name. S6's move of unit 47's status header landed with unit 47's rev-5.
- The unborn predicate itself, which is `TOOL-dWitnessedBar-64`'s (id 20) and has landed. S10 calls
  `read_head_sha` as built.
- The spec lints, roster lint and checklist entries the report names as left-shift gates. No clause
  of this build names them. S1's shared-table arm and S17's token grammar are the regression arms
  this batch builds.
- Unit 28, deferred with three dOrderedCharter asks (TOOL-dWitnessedBar-101 to -103): no item here
  needs it.

### Edges

- **consumes-from** `TOOL-dWitnessedBar-63` — every item amends what unit 63 builds: its containment readers, plants, seed routes, sweep, record readers, `PM_SCRUB` reader and its AC18 (all 22 ids)
- **consumes-from** `TOOL-dWitnessedBar-47` — its pass commit at order 6, which S6 observes landing after unit 61's (id 1)
- **hands-off** `TOOL-dWitnessedBar-66` — AC12's hook half, which the round-1 audit of units 64 and 65 found planted on a key `read_green_file` never reads, replanted on `sha` (id 6)
- **hands-off** `TOOL-dWitnessedBar-67` — the round-1 audit of units 64 and 65's minors on this unit: the AC12 `fingerprint` line, the sweep's arm and every filesystem call, the `PM_SCRUB` arm graded on the built list and its single assignment, the seed's timeout, `--all` route and `--sha` prefix check, the unterminated record line, AC4's per-file read, the segment rule's bytes and its second Python spelling, and this unit's order (ids 1, 3, 5, 7, 9, 11, 12, 14, 15, 16, 17, 18, 19, 20, 23)
- **hands-off** `TOOL-dWitnessedBar-69` — S15's one-CR strip and last-wins rule, which the round-1 spec audit of units 66 and 67 found unreachable on Git for Windows behind the hook's `$(awk ...)` reads and Python's default text-mode open, moved onto a whole-line bash read and a `newline=''` open (id 19)

## 4. Design

### Why one unit

M4 admits a second unit only so that the two halves build concurrently. Here no concurrency is
available to buy: dispatch is strictly sequential, a shared order included
(`tools/workflows/unattended-build.js@76a3b4bc2:78`). `TOOL-dWitnessedBar-67` S16 gave this unit
order 37 alone, one step after `TOOL-dWitnessedBar-64`, which wrote the same seed files. One unit
holds all 22 findings.

### Evidence

Read at HEAD `76a3b4bc2` on 2026-11-21.

- The landed rules. lib-unattended folds `\` and tests `/*|*:*|..|../*|*/..|*/../*`
  (`tools/unattended/lib-unattended.sh#resolve_generated_indexes`). `derive_contained_rel` refuses a
  normal form `.`, `..` or `../…`, a rooted or `ntpath`-absolute path, and a colon anywhere, and both
  Python readers add the folded `..` segment (`tools/govkit/govkit.py#selfcheck`,
  `tools/run-gates/regen.py#check_when`).
- They part on one class. An escaping normal form needs a `..` segment or a leading `/` in the folded
  text, and `ntpath.isabs` holds only for a folded leading `/` or a colon. What is left is a normal form
  of `.` with no `..` segment, such as `.` or `./.`: the Python readers refuse it, and lib-unattended
  tests `[ -e "$root/." ]`, which holds. Unit 63's builder return names `exists:.` as this residual.
- `tools/unattended/lib-unattended.sh#normpath` collapses `//`, then strips a leading `./`, the dot
  segments and a trailing `/`, so `.`, `./` and `./.` each read `.` there.
- `check_when_forms_agree` puts each refused form in its own tree, since one refused row refuses its
  whole descriptor in regen, and pins its refused count in `graded == len(refused) == 10`.
- The plant loop's case list holds `key-no-tab:1` and `peer-no-ssh-keygen:0`, and the leg
  `run-gates gov canary` runs `run-gates.gov.test.sh` (`tools/gate-legs.json`).
- `run_seed_cli` calls `rev-parse --show-toplevel`, then `read_head_sha`, then `read_registrations`,
  and its no-HEAD route prints from the registrations it picked. `_run_git` catches `OSError` alone
  and passes no timeout.
- `tools/lib/legacy_ledger.py#SHA_RE` is `[0-9a-f]{8,40}`, so an upper-case `--sha` exits 2 at HEAD.
  `HEAD` folded to `head` still fails it.
- The sweep tests `p.is_file()`, which follows a link, and continues on every `OSError`. The floor in
  `tools/lib/python-floor.txt` is 3.15, which has `Path.is_file(follow_symlinks=...)`.
- `PM_SCRUB` spans five lines of `tools/run-gates/post-merge.sh` and holds 30 names (DERIVED by
  `sed -n '/^PM_SCRUB="/,/"$/p' tools/run-gates/post-merge.sh | sed -e 's/^PM_SCRUB=//' -e 's/"//g' | wc -w`).
- S19: `grep -nE 'selftest\.py:[0-9]|lib-unattended\.sh:[0-9]'` over unit 63's spec prints nothing.
- AC18's three probes each print 1 at HEAD, and so does `grep -c 'FAIL executed'
  tools/memory-tree/check-memory-hygiene.test.sh` (PINNED 2026-11-21).

### Inventory

Minted: the reasons `git not runnable: <exception>` and `seed: no HEAD: <reason>`, lib-unattended's
refusal of a path reading `.`, and the rows and controls S1 adds to `check_when_forms_agree`. The form
`git <verb> exited <rc>` is `TOOL-dWitnessedBar-64`'s. No function, constant, plant or flag is minted.
Naming cells: none apply.

### Migration

None: no item changes stored data. S14 and S15 read records written before them unchanged, since the
runner escapes CR when it appends and writes each key once.

### Rollout

Live at landing at order 37, after `TOOL-dWitnessedBar-63` (35) and `TOOL-dWitnessedBar-64` (36),
both CLOSED. S6 landed with unit 47's rev-5. Neither unit consumes from the other. S1, S2, S8 to S11,
S14, S15 and S17 stage the regression arms under §7. S6, S12, S13 and S22 are observed by the main loop
at the close.

### Files touched (estimate)

The `legacy_ledger.py` population is every copy of the `legacy_ledger_py` block, three files (DERIVED
by `git grep -l '>>> legacy_ledger_py' -- tools`), held identical by the resolver suite's parity part.
`tools/govkit/govkit.py`, `tools/run-gates/regen.py` and `tools/run-gates/run-gates.sh` leave the list:
S3, S14 and S20 are present at HEAD. A shell file grown past its shell-role row is widened as unit 51
S1 states, its record declared through `--dispatch`.

- `tools/govkit/selftest.py`
- `tools/unattended/lib-unattended.sh`
- `tools/lib/legacy_ledger.py`
- `tools/memory-tree/legacy_ledger.py`
- `tools/gate-lint/legacy_ledger.py`
- `tools/lib/resolve-python.test.sh`
- `tools/run-gates/verdict_backends.py`
- `.githooks/pre-push`
- `tools/run-gates/run-gates.gov.test.sh`
- `tools/run-gates/run-gates.evidence.test.sh`

### Alternatives rejected

- **The normpath rule in all three readers (id 2's first option).** lib-unattended would need a
  `..`-resolving `normpath` in bash; its own folds only `.` segments. It would also admit `a/../b`,
  which unit 62 S22 refuses (§8 F2).
- **Two batches, seed-side and the rest.** §4 "Why one unit".
- **Teach the hand-out to break an order tie by `consumes-from` edges (id 1).** That is new behaviour
  in the unattended kit, whose suites this build waives, and S6's move landed first (§8 F3).

## 5. Production-readiness checklist

- security — S1 and S2 make `exists:` containment one rule in three readers. S10 checks `--sha` for
  existence at the write boundary. S8 and S9 write nothing where HEAD is unknown.
- perf / scale — one `rev-parse` per given `--sha`. Seven more single-form trees in the govkit
  selftest arm, each one selfcheck and one shell run, inside that leg's ceiling in
  `tools/gate-legs.json`.
- error / empty / loading states — S8, S9 and S11 turn a missing repository, an unrunnable git and a
  failed unlink into named outcomes, never a traceback.
- observability — S9's reasons name the git verb and exit code, and S11 names a file it could not
  unlink.
- risks — S2's `.` refusal skips a row lib-unattended kept at HEAD. Regen and selfcheck refuse that
  row already, so no tree the bar admits holds one.
- testing — AC1 to AC16 by fixture, plant and probe. The arms under §7 at the close.
- migration — none.
- user docs — none under `help/`. No user-facing surface changes.

## 6. Acceptance criteria

- **AC1** — When each form of S1's table is planted alone beside one conf-true row in a scratch copy
  of the run-gates descriptor and read by lib-unattended's `resolve_generated_indexes`,
  `regen.build_items` and `govkit.py selfcheck`, each reader refuses each refused form S1 names and
  admits each control. Refused means lib-unattended skips the row with unit 62 S21's line, regen
  raises `Refusal` naming the row, and selfcheck fails naming the row. The arm prints one line per
  form with the three outcomes.
  Red when: any two readers part on one form, or a reader admits a `..` segment, a colon, or a path
  that normalises to `.`.
  fixture: scratch trees under `%TEMP%/<short-name>`, built by the arm.
- **AC2** — When `govkit.py selfcheck` runs over the table's `a/../b` tree, its failure line for that
  row names the entry, the row and the `exists:` path, and holds no `deploy.toml`.
  Red when: selfcheck passes `demand_contained_dest`'s Refusal text through.
- **AC3** — When `grep -nE 'key-no-tab:1|peer-no-ssh-keygen:0' tools/run-gates/run-gates.gov.test.sh`
  runs, it names the plant loop's case list, which the `run-gates gov canary` leg runs.
  `python verdict_backends.py --fixture --plant peer-no-ssh-keygen`, run in `tools/run-gates/`, exits 0
  printing `signer temps left: 1 gov-signers-young`.
  Red when: either plant leaves the loop, or the plant's aged signer temp survives.
- **AC4** — When `sed -n 3p` runs over unit 47's and unit 61's specs, unit 47's header carries `order 6`
  and unit 61's carries `order 5`. At the close,
  `grep -nE ' dispatch · item [0-9a-f]+ TOOL-dWitnessedBar-(61|47) ' memory/builds/dWitnessedBar/RUN.md`
  prints 61's row above 47's. `git merge-base --is-ancestor` of unit 61's pass commit and unit 47's,
  each found by `build_commit`, exits 0.
  Red when: the run stopped at `--dispatch` for unit 47, or the two units share an order again.
- **AC5** — When `grep -n 'HEAD is unborn' tools/lib/resolve-python.test.sh` runs, it names section
  `2o`'s `63 AC23` assertion over the stderr capture `$LL/py.err`. When the seed runs in a commitless
  `git init` with stdout and stderr captured apart, `HEAD is unborn` is in the stderr capture only.
  Red when: section `2o` looks for the unborn line on stdout, which unit 63 S32 has emptied of it.
- **AC6** — When `python legacy_ledger.py seed --population p` runs in a scratch directory with
  `GIT_CEILING_DIRECTORIES` set to its parent, it exits 1, stdout is one line opening
  `unarmed p no HEAD: `, stderr carries `legacy_ledger: p: no HEAD: ` and no `Traceback`, and nothing
  is written. With `--all` in its place, it exits 1, stdout is empty and stderr carries
  `seed: no HEAD: `.
  Red when: the seed exits 2 with `not inside a git work tree`, or reads registrations or a home first.
  fixture: a scratch directory under `%TEMP%/<short-name>`, built by section `2o`.
- **AC7** — When the seed runs with `PATH` naming only an empty scratch directory and python invoked by
  absolute path, stdout opens `unarmed p no HEAD: git not runnable: ` and stderr holds no `Traceback`.
  A probe importing `legacy_ledger.py` replaces `subprocess.run` for the call holding `--verify` only,
  once with one raising `subprocess.TimeoutExpired` and once with one exiting 2 silently. Under
  `seed --all` over two registrations, each population prints a no-HEAD line, reading
  `git not runnable: ` under the first and `git rev-parse exited 2` under the second.
  Red when: a spawn failure, a timeout or a silent non-zero exit raises out of the seed, prints an empty
  reason, or stops `--all` at its first population.
- **AC8** — When `seed --sha 0000000000000000000000000000000000000000` runs in a fixture holding one
  commit, it exits 2 naming `--sha` and writes no home. So does `seed --sha deadbeef` where
  `git rev-parse --verify --quiet deadbeef^{commit}` exits non-zero. `seed --sha` given HEAD's first 8
  hex characters in upper case arms the population, its rows carrying HEAD's full lowercase SHA. In a
  commitless `git init`, `seed --sha 0000000000000000000000000000000000000000` arms with null-SHA rows.
  Red when: a SHA naming no commit is stamped, or the null SHA is stamped in a repository with commits.
- **AC9** — When a probe importing `verdict_backends.py` runs `remove_stale_signer_temps` over a scratch
  directory holding two aged `gov-signers-` files, an aged directory `gov-signers-d` and, where
  `os.symlink` succeeds on the host, an aged link `gov-signers-l` to an aged file outside it, with
  `os.unlink` replaced, the call returns without raising. The stand-in records each path it is given,
  raises `FileNotFoundError` for one file and `PermissionError` for the other, and is never given the
  directory or the link. Stderr names the second file once.
  Red when: the sweep raises into the read, changes its verdict, or touches an entry that is not a
  regular file.
- **AC10** — When `grep -n 'AC7' memory/builds/dWitnessedBar/build/*TOOL-dWitnessedBar-62*acceptance-ledger*`
  runs at the close, the line names `run-gates evidence: executed`, `gov-canary: executed`,
  `adopt-e2e: executed` and `FAIL executed`, the last beside the memory-tree hygiene suite alone. Unit
  63's AC18 ledger line names this unit's S12 for its grep half.
  Red when: unit 62's AC7 is graded on `FAIL executed` for another suite, or unit 63's AC18 is recorded
  green on its grep half.
- **AC11** — When `read_record_keys`, cut by `awk '/^read_record_keys\(\)/,/^}/' tools/run-gates/run-gates.sh`
  and sourced in a probe, reads a record holding `verdict<TAB>GREEN<CR>`, `note<TAB>a<TAB>`, then
  `head<TAB>x` followed by `head<TAB>y`, it gives `verdict` as `GREEN`, `note` as `a<TAB>` and `head`
  as `y`.
  Red when: the reader drops the CR strip, or keeps the first of a repeated key.
- **AC12** — When the `key-no-tab` plant's record also holds `verdict<TAB>GREEN<CR>` and two `sha`
  lines, `read --backend local-hook` and the hook's `read_green_file`, cut by
  `awk '/^read_green_file\(\)/,/^}/' .githooks/pre-push`, each read `GREEN` and the second `sha`.
  Red when: the two readers part on a CRLF line or a repeated key.
- **AC13** — When `check_bar_scrub_parity` reads `PM_SCRUB` from `tools/run-gates/post-merge.sh`, the
  list's first word is `GIT_DIR` and its last is `GATE_REUSE_DAY`, each a whole word, and no word holds
  `=` or `"`.
  Red when: the first word reads `PM_SCRUB=GIT_DIR`.
  figure: both names are PINNED at `76a3b4bc2`, measured 2026-11-21 by the §4 `sed` range.
- **AC14** — When the reader runs over a scratch copy of `tools/run-gates/post-merge.sh` with
  `  # note GATE_SELECTION` after the closing quote, and over one with the assignment on a single line,
  each reads exactly the base list. With `GATE_SELECTION` cut from the list while the comment still
  names it, the arm fails naming `GATE_SELECTION`. A planted token `bad-name` fails the grammar
  `^[A-Z_][A-Z0-9_]*$`.
  Red when: a trailing comment's words enter the name set, or the read runs past the closing quote.
- **AC15** — When `grep -n 'TAIL_GRACE_S' verdict_backends.py` runs in `tools/run-gates/` on the built
  tree, it names the comment beside `PEER_SIGNERS_GRACE_S`, which calls `TAIL_GRACE_S` the run-gates
  kit's own constant. `grep -nE 'another kit' verdict_backends.py`, run in the same directory, prints
  no line naming `TAIL_GRACE_S`.
  Red when: the comment places the constant in another kit, or is absent.
- **AC16** — When `grep -nw 77 memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-62.md`
  runs, it prints one line, the records-table row naming `TOOL-dWitnessedBar-77`. At the close, unit
  62's ledger line for AC13 names the built tree's derived figure.
  Red when: a 77-carrier of unit 62 is answered by no ledger line.
  figure: the one line is PINNED at `76a3b4bc2`, measured 2026-11-21.

## 7. Gates

`govkit selftest` · `govkit selfcheck` · `govkit refusal join` · `govkit acceptance matrix` · `recall floor arms` · `routed-commits selftest` · `measure-legs selftest` · `shell-hygiene selftest` · `python resolver (behaviour + inline parity + idiom ban)` · `run-gates gov canary` · `run-gates canary` · `run-gates evidence` · `pre-push self-test` · `pre-push bar self-test` · `memory-hygiene self-test` · `codebase-map adopter e2e` · `codebase-map kit selftest` · `drift-audit selftest` · `policy fixtures` · `memory hygiene`

The unattended kit's own suites are waived for this build's landing (README rule), so S2's bash
reader is observed through the govkit selftest arm, as unit 63's S9 is. Every leg here with subject
`kit` in `tools/gate-legs.json` is held unless the main loop sets GATE_SELFTESTS at the close.

New arm: tools/govkit/selftest.py · covers AC1 AC2 · `check_when_forms_agree` gains S1's refused rows and controls and prints each form's three outcomes, staged red by taking the `..`-segment clause out of regen's `check_when` in the arm's copy, which admits `a\..\b`, and by taking out lib-unattended's `.` refusal, which admits `.` · none
New arm: tools/run-gates/run-gates.gov.test.sh · covers AC12 AC13 AC14 · the `key-no-tab` plant's CRLF and repeated-`sha` record read by the hook's `read_green_file`, and the `PM_SCRUB` reader's first-word, trailing-comment, one-line and token-grammar cases, staged red by removing the hook's CR strip and by restoring the `sed` range · FLOOR_ASSERTIONS raised by these assertions
New arm: tools/run-gates/run-gates.evidence.test.sh · covers AC11 · the `63-AC16` record-reader arm gains the CRLF and repeated-key cases, staged red by removing the CR strip · FLOOR_ASSERTIONS raised by these assertions
New arm: tools/lib/resolve-python.test.sh · covers AC6 AC7 AC8 · section `2o` gains the outside-any-repository seed, the empty-`PATH` and stand-in probe failures, and the four `--sha` cases, staged red by restoring the exit-2 work-tree refusal and by dropping the existence check · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec that carries nothing and is derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of the repaired unit's clause. Unit 63 is itself derived
  and carries none, so (b) has nothing to split; veto 1 discards it. RESOLVED (agent, 2026-10-25,
  delegated): (a), rung 3, the precedent `TOOL-dDeclaredLoop-36` §8 F1 set.
  widens: none · relaxes: none
- **F2 — Which containment rule do the three `exists:` readers share (ids 2, 7, 21)?** Options: (a) the
  segment rule, refusing a leading `/`, a second-character `:` and any `..` segment after folding `\`;
  (b) `demand_contained_dest`'s normpath rule in all three. (b) admits `a/../b`, which unit 62 S22
  refuses, and needs a bash `normpath`. Veto 1 discards it against unit 62's AC2. RESOLVED (agent,
  2026-10-25, delegated): (a), rung 3. It refuses every form (b) refuses (§4 Evidence), and it is
  tie-broken by reuse of `read_gate_policy`'s pattern.
  widens: none · relaxes: none
- **F3 — How does unit 61 come to build before unit 47 (id 1)?** Options: (a) move unit 47 to order 6,
  applied in the commit that lands this spec; (b) the same move made in this unit's build pass;
  (c) teach the hand-out to break order ties by edges. (b) lands at order 36, after the step-5 stall,
  so AC4 cannot pass. (c) also lands at order 36, and needs the unattended kit's waived suites. Veto 1
  discards both. RESOLVED (agent, 2026-10-25, delegated): (a), rung 3, the one survivor and the
  report's corrected fix. It is applied as unit 47's rev-5 with its §9 line.
  widens: none · relaxes: none
- **F4 — What does a given `--sha` stamp (id 24)?** Options: (a) the value as given, once it resolves;
  (b) the full lowercase SHA that `rev-parse --verify <sha>^{commit}` prints. (a) leaves the report's
  case question open and stamps abbreviations, which unit 14 S9's compare with the base's SHA would read
  as different. RESOLVED (agent, 2026-10-25, delegated): (b), rung 3. It meets the most criteria and
  leaves no open question, and the resolving call is the existence check S10 already makes.
  widens: none · relaxes: none
- **F5 — How do the three readers agree on a path that normalises to `.` (forced by the re-ground)?**
  Unit 63 landed the Python readers on `derive_contained_rel`, which refuses that class, and
  lib-unattended on a pattern that admits it, so S1's table cannot hold `.` with no change on one side.
  Options: (a) lib-unattended also refuses a folded path its own `normpath` reads as `.`; (b) the
  Python readers admit it, a special case beside `derive_contained_rel`; (c) `.` stays out of S1's
  table, named as unchecked. (b) puts a second rule beside the one unit 63 S10 chose, and (c) leaves
  §1's one rule false on a form the arm can plant. RESOLVED (agent, 2026-11-21, delegated): (a),
  rung 3, the most criteria met with no open question, tie-broken by reuse of lib-unattended's
  `normpath`.
  widens: none · relaxes: none
- **F6 — Where the root resolves, does S8's no-HEAD route still read registrations first (forced by
  the re-ground)?** Unit 63 landed the route printing from the registrations it picked, so a
  `seed = []` registration reads `unarmed <name> no seed`, and `retrofit.unseeded: refuse` refuses
  before any no-HEAD line. Options: (a) S8 changes the no-root case alone, and a resolved root keeps the
  landed order; (b) under `--population` the route never reads registrations and prints from the
  given name. (b) turns both landed outcomes into a no-HEAD line on that route. RESOLVED (agent,
  2026-11-21, delegated): (a), rung 3: it meets AC6 as (b) does and re-decides no landed outcome. The
  `--home` route, which reads no registration, keeps its exit 2 where no root resolves.
  widens: none · relaxes: none
- **F7 — Does a given `--sha` fold case before the grammar (forced by the re-ground)?** `SHA_RE` is
  lowercase only, so AC8's upper-case abbreviation exits 2 at HEAD before S10's resolution runs.
  Options: (a) fold the value to lowercase, then apply `SHA_RE` and the resolution; (b) keep the
  grammar refusing upper case and rewrite AC8's case in lower case. (b) fails AC8 as written; veto 1
  discards it. RESOLVED (agent, 2026-11-21, delegated): (a), the one survivor. `HEAD` folds to `head`,
  which `SHA_RE` still refuses, so unit 63 AC23 stands.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, promoted from the round-1 spec audit of unit 63: 11 MEDIUM and
  11 LOW findings, batched.
- rev-2 · 2026-10-25 · §1 · §3 · §4 · S6 · the header's order moves from 36 to 37, applied as
  `TOOL-dWitnessedBar-67` S16 (id 14 of the round-1 audit of units 64 and 65), with §1, S6's consumer
  orders, §4 "Why one unit" and §4 Rollout restated to match. §3 gains the hands-off edges to units 66
  and 67. No scope item or criterion moves.
- rev-3 · 2026-10-25 · §3 · the Edges block gains the hands-off bullet mirroring TOOL-dWitnessedBar-69's
  consumes-from edge, promoted by the round-1 spec audit of units 66 and 67; nothing else moved.
- rev-4 · 2026-11-19 · §7 · the leg line gains `policy fixtures`, whose manifest guard holds the §4 path
  `tools/govkit/govkit.py`, per brief 2026-11-19-prompt-TOOL-dWitnessedBar-51-spec-tokens-brief; nothing
  else moved.
- rev-5 · 2026-11-21 · §1 to §10 · S1 to S11 · S14 to S17 · S19 to S22 · AC1 to AC3 · AC5 to AC9 ·
  AC13 · AC16 · re-grounded over units 63 and 64 as landed, per
  2026-11-19-prompt-TOOL-dWitnessedBar-65-reground-brief: ten items are present at HEAD and observed;
  S2 takes unit 63's colon-anywhere rule and adds the `.` refusal (§8 F5); S8 changes the no-root case
  alone (§8 F6); S9 spells `git <verb> exited <rc>`; S10 folds case (§8 F7); section `2l` reads `2o`
  and the signer prefix `gov-signers-`; citations move to `path#symbol` or blob-pinned lines.

## 10. Reuse audit

Each item extends the seam its finding names. S1 extends `tools/govkit/selftest.py#check_when_forms_agree`,
the three-reader arm units 54, 62 and 63 built. S2 extends
`tools/unattended/lib-unattended.sh#resolve_generated_indexes` with the kit's own
`tools/unattended/lib-unattended.sh#normpath`, and S3's Python readers rest on
`tools/govkit/upgrade_steps.py#derive_contained_rel`. S6 reuses the order verb and the `--dispatch`
edge refusal. S4 and S5 reuse the gov suite's plant loop, which units 6, 56 and 63 fill. S8 to S10
extend `tools/lib/legacy_ledger.py#run_seed_cli`, `#_run_git` and `#read_head_sha`. S14 and S15 reuse
the runner's CR strip in `tools/run-gates/run-gates.sh#read_record_keys`. S16 and S17 reuse
post-merge's own fold of `PM_SCRUB`, `${PM_SCRUB//$'\n'/ }`.

`python tools/codebase-map/reuse_lookup.py "refuse a repo-relative path holding a dot-dot segment"`,
re-run on 2026-11-21, ranked `repo_root`, `PolicyRefused`, `OverlayRefused` and `refuse_wrong_shell`.
It missed both containment rules, which reading `#resolve_generated_indexes` and
`#derive_contained_rel` found, so the map and the source disagree here. No existing seam fits beyond
those named.

Recall terms used: `python tools/memory-recall/query.py "what did the round-1 audit of unit 63 find" --terms "exists containment segment rule normpath backslash PM_SCRUB range plant floor null sha unborn signer sweep CR"`
