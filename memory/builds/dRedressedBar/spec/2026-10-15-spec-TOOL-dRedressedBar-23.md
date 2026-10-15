# TOOL-dRedressedBar-23 — the closing review's govkit findings M3, M4, M6 and L4: a narrower apply keeps a carried kit's orders and order-file legs, target spawns decode stderr through one helper, a leg guard widens, and a routing arm grades each member

**Status:** INPROGRESS · rev-1 · 2026-10-15 · node d · Tier-2 · base ebce889c · streams tooling · order 17

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-15-prompt-TOOL-dRedressedBar-21-4-revision.md](../prompts/2026-10-15-prompt-TOOL-dRedressedBar-21-4-revision.md) | research | TOOL-dRedressedBar-21 |
| [2026-10-15-prompt-TOOL-dRedressedBar-21-brief.md](../prompts/2026-10-15-prompt-TOOL-dRedressedBar-21-brief.md) | research | TOOL-dRedressedBar-21 TOOL-dRedressedBar-22 |
| [2026-10-15-prompt-TOOL-dRedressedBar-23-1-spec-writer.md](../prompts/2026-10-15-prompt-TOOL-dRedressedBar-23-1-spec-writer.md) | journal | — |
| [2026-10-15-prompt-TOOL-dRedressedBar-23-2-revision.md](../prompts/2026-10-15-prompt-TOOL-dRedressedBar-23-2-revision.md) | research | TOOL-dRedressedBar-12 TOOL-dRedressedBar-14 TOOL-dRedressedBar-15 TOOL-dRedressedBar-16 TOOL-dRedressedBar-17 |
| [2026-10-15-prompt-TOOL-dRedressedBar-23-3-spec-writer.md](../prompts/2026-10-15-prompt-TOOL-dRedressedBar-23-3-spec-writer.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 closing diff review over `ebce889c7..e114f1356`
(`reviews/2026-10-15-review-TOOL-dRedressedBar-1-20-diff-review-round1.md`) returned CLEAN WITH
FIXES, and the owner promoted all 13 items into this build (README, Build-level rules, 2026-10-15).
`TOOL-dRedressedBar-21` takes the high, `TOOL-dRedressedBar-22` the profiler's minors, and this unit
the four minors in `tools/govkit/` and `tools/gate-legs.json`. It is ordered after both, and the
README's derived build-order region says so. It closes these findings, by report id:

| id | grade | item | sits in | what is wrong | closed by |
|---|---|---|---|---|---|
| 4 | MEDIUM | M3 | `_cmd_apply`'s RECEIPT update; `write_gate_legs`' no-runner branch | a narrower `apply` keeps a carried kit's claim and rows but writes this run's `orders` alone, and rebuilds `.governance/outbox/gate-legs.md` from the selection alone | S1, S2 |
| 5 | MEDIUM | M4 | `update`'s gained loop | the adopter spawn decodes stderr as strict UTF-8, so a non-UTF-8 byte makes the refusal line claim the adopter printed nothing | S3, S4 |
| 12 | MEDIUM | M6 | the `govkit selftest` guard in `tools/gate-legs.json` | `check_roles_install` reads `tools/codebase-map/kit.toml`, which the guard does not name | S5 |
| 13 | LOW | L4 | the `[-21] AC2` routing arm | its two liveness checks are aggregate over `ADOPTER_BAR_PATHS`, so a member matching nothing passes | S6 |

Ids 1, 2, 3, 6, 9, 10, 11, 14, 15 and 16 belong to units 21 and 22. Ids 7 and 8 were refuted and
stay refuted. Id 4's fix is the one the record states, which the skeptic judged sound, with the two
choices the record leaves open derived in §4 "Two choices, derived". The specs these fixes make
false are CLOSED, so this unit's spec-writer pass `<w23>` corrects them before its build pass, as
units 16, 17 and 19 did.

## 2. Scope (IN)

- **S1** — id 4, M3, the receipt's orders. In `_cmd_apply`, each hole order CONFIGURE appends
  (`tools/govkit/govkit.py:7962-7963`) carries `"kit": eid`, as each machine order already does
  (`:7993-7994`). Beside `_carried_kits` and `_carried_rows` (`:7927-7929`) one more list is bound
  once, `_carried_orders`: every order in the prior receipt's `orders` that is a dict and whose
  `kit` is a carried kit, plus, for a receipt an earlier engine wrote, every `kind == "hole"` order
  carrying no `kit` key whose `id` a carried kit's descriptor declares among its `[[hole]]` ids. The
  RECEIPT update (`:8341-8344`) writes `"orders": orders + _carried_orders`, so the receipt holds
  this run's orders first and the carried ones after, verbatim and in the prior receipt's order.
  The comment above the RECEIPT update names `TOOL-dRedressedBar-23` and says orders are carried as
  rows are. Observed by AC1.
- **S2** — id 4, M3, the order file. In `write_gate_legs`, when `carry_out_of_scope` is set, the
  kits the prior receipt claims outside `selection` and that `descs` declares are bound once, in the
  receipt's `kits` order. `_silenced` (`:4288-4289`) is computed over `selection` plus those kits.
  The non-manifest branch (`:4548-4595`) lists their legs after the selection's, each through the
  same `_silenced` test. A carried kit's silenced leg is listed under `## WITHHELD`, never as an
  instruction, and adds nothing to `_silenced_found`, so it raises no problem. A selected kit's
  silenced leg raises its problem as before. The docstring's `carry_out_of_scope` paragraph says the
  order lists every claimed kit's legs and why a carried kit's withheld leg raises nothing (§4).
  `update` passes the carry too (`:12218-12220`), so it takes the same branch. AC2 observes it
  through `apply` alone. Observed by AC2.
- **S3** — id 5, M4, the helper. One module-level function in `tools/govkit/govkit.py`, placed after
  `resolve_shell_argv` (`:1197`): `run_target_argv(argv, target)`. It returns
  `subprocess.run(resolve_shell_argv(list(argv)), cwd=str(target), capture_output=True, text=True,
  encoding="utf-8", errors="replace")`. Its docstring names the three callers and says one helper
  holds the decode rule so the three cannot disagree. The CONFIGURE spawn (`:8038-8039`), the
  regenerate spawn (`:11309-11311`) and the gained loop's spawn (`:11445-11446`) each call it, and
  nothing else at those sites moves. The comment above the CONFIGURE spawn (`:8028-8037`) keeps its
  sentences, and its decode sentence says the rule is `run_target_argv`'s for all three sites, with
  `TOOL-dRedressedBar-23` beside `TOOL-dRedressedBar-13`. One `[dRB-23]` gained case in
  `tools/govkit/selftest.py`, in the scope that defines `build_gov13` (`:15904`), runs
  `update --write` over a gov whose newly default kit's adopter writes a non-UTF-8 byte to stderr
  and exits 2, and asserts the problem line on the line it names. Observed by AC3.
- **S4** — id 5, M4, the class arm. One `[dRB-23]` static check in `tools/govkit/selftest.py` walks
  `govkit.py`'s syntax. Its population is every `subprocess.run` call whose first positional argument
  is a call to `resolve_shell_argv` and which passes an `encoding` keyword. It asserts every member
  passes `errors="replace"`, and that the population holds the call inside `run_target_argv`, so an
  empty population reds. A second check asserts `run_target_argv` is called exactly three times.
  Observed by AC4.
- **S5** — id 12, M6. The `govkit selftest` leg's `guard` in `tools/gate-legs.json` (`:1430-1434`)
  gains `"{prefix}/codebase-map/kit.toml"` as an exact file, after its three paths. The product
  commit carries the kickoff-manifest re-stamp at its parent that the ratchet's staged check
  requires, as `809f794e4` did. A second commit, `<p23m>`, re-stamps `last-audit:` in
  `memory/guides/SESSION-KICKOFF.md` at the product commit after a section B re-read, with a
  `manifest-audit:` line in its body, as `cafbbc460` did. Observed by AC5.
- **S6** — id 13, L4. The selftest's `read_bar_writes21` takes its members and the engine source as
  arguments, `read_bar_writes21(members, src)`. The three `[-21] AC2` checks read the walk over every
  member of `govkit_module().ADOPTER_BAR_PATHS`, as today. One more check per member runs the walk
  with that member alone and requires at least one routed `write_atomic` site, and its label and
  detail name the member. Observed by AC6.
- **S7** — S3 mints a function, so the symbol index's one generator,
  `python tools/codebase-map/gen_map.py --write`, runs alone before the product commit, and that
  commit carries what it rewrites under `memory/map/generated/`. Observed by AC7.
- **S8** — The record, in two passes. Specs 12, 14, 15, 16 and 17 each take one rev bump in this
  unit's spec-writer pass `<w23>`, which runs before the build pass, with §4 "What this unit corrects
  in each spec" as its brief. Each revision line names `TOOL-dRedressedBar-23` and the report ids
  that table assigns its spec, and each spec's Edges gain a `hands-off` bullet naming
  `TOOL-dRedressedBar-23`. The status of each stays CLOSED. The build pass writes no spec file but
  this one's status and date cells. Every reading below goes to this unit's acceptance ledger under
  `memory/builds/dRedressedBar/build/`, carrying `**Serves:** journal TOOL-dRedressedBar-23`.
  Observed by AC8.

## 3. Non-goals (OUT)

- Any finding outside the round-1 record. Ids 7 and 8 stay refuted.
- The left-shift gates that are their own mechanism. Id 4's invariant run after every `apply`
  fixture is a harness change, and AC1 observes the one sequence the record traced. Id 12's static
  arm over every sibling-kit read is a guard policy: measured at `bf42c5113`, `tools/govkit/selftest.py`
  spells 13 `KIT_DIRS[...]` expressions and the `govkit selftest` guard trips one of them, so the arm
  would widen the guard by a dozen paths or set a breadth rule, which is the owner's. Id 13's
  checklist entry is a record, not a gate. Id 5's left-shift is in scope as S3 and S4, because the
  record names the helper as the better fix and the charter's `[reuse]` rule extracts it at the
  third instance.
- No `'"install.json"'` member in `ADOPTER_BAR_PATHS`. The record says to consider one. The walk
  matches names, not scopes, and the file-name member would make `receipt` a destination, while
  `govkit.py` binds `receipt` to the parsed receipt dict at `:5386`, `:7499` and `:9120`. S6's
  per-member check is what turns a renamed `receipt_path` from a silent hole into a red.
- No change to the four target-side spawns that decode with the host codepage, at `:4976`,
  `:5231`, `:5270` and `:6177`. No change to any git spawn, or to the three spawns that already
  decode UTF-8 with replacement outside the helper (`:5194`, `:6284`, `:13523`).
- No change to the manifest branch of `write_gate_legs`, to its `emitted` carry, or to how `update`
  carries `orders`. `update` maintains no `orders` list (`:4264-4266`).
- No change to `check`'s outbox grading (`:5611-5631`). It reads the carried orders as it reads any.
- No new gate leg, and no change to any leg's argv. S5 widens one guard.
- No kit version moved. Every product file sits under `{prefix}/govkit` or is
  `tools/gate-legs.json`, and the registry exempts both (`tools/govkit/registry.toml:207`, `:296`).
- No `help/` page. `help/` holds `README.md`, `measure-legs.md` and `roles.md`, and none covers
  govkit. `WIRE-INTO-PROJECT.md:1490` already says `apply`'s machine and hole orders are recorded in
  the receipt's `orders`, which stays true.
- No corrections to specs 3 and 13. Spec 3 never claimed the guard covered its read, and spec 13's
  §3 and §5 sentences on the gained loop's strict decode are pinned to the shas they name.

### Edges

- **consumes-from** `TOOL-dRedressedBar-12` — the receipt carry `_carried_kits` and `_carried_rows`
  that S1 extends to orders, and its `[dRB-12]` block, which AC1 extends. Its §3 external hand-off
  on orders is what `<w23>` rewrites as a hand-off to this unit. Without the carry there is no
  carried kit whose orders could be lost.
- **consumes-from** `TOOL-dRedressedBar-14` — `_rcpt_doc` and the RECEIPT update that S1 changes. Its
  S2 and its "The receipt written ahead" table state the `orders` key that `<w23>` corrects.
- **consumes-from** `TOOL-dRedressedBar-15` — the gained loop's `_res_g` resolution and the
  CONFIGURE comment S3 restates. Its §4 "The CONFIGURE comment, restated" is what `<w23>` corrects.
- **consumes-from** `TOOL-dRedressedBar-16` — `apply`'s `carry_out_of_scope=True`, without which the
  non-manifest branch S2 changes never sees a carry. Its S1 and its adopter table are what `<w23>`
  corrects.
- **consumes-from** `TOOL-dRedressedBar-17` — `receipt_path` as a member of `ADOPTER_BAR_PATHS`,
  which S6 grades per member, and the `[dRB-12]` sidecar checks AC1 sits beside. Its S23 and §10 are
  what `<w23>` corrects.
- **hands-off** external — the left-shift gates the record names for ids 4, 12 and 13, each its own
  mechanism (the second bullet above).

## 4. Design

### Evidence, read at `bf42c5113` on 2026-10-15

`bf42c5113` is the build branch's tip when this spec was written. Units 21 and 22 write
`tools/run-gates/`, `help/measure-legs.md` and the symbol index, and neither writes `tools/govkit/`.
Unit 21 also adds two exact files to the `measure-legs selftest` row's guard in
`tools/gate-legs.json`, above the row S5 edits, and re-stamps the kickoff manifest (its S11). So
every `govkit.py` and `selftest.py` line cited here holds until this unit's build pass, give or
take what the build pass itself moves. The `govkit selftest` guard cited at
`tools/gate-legs.json:1430-1434` sits two lines lower once unit 21 lands, and S5's re-stamps follow
unit 21's.

- The carry: `_carried_kits` is every prior-receipt kit outside `selection`, and `_carried_rows` its
  rows (`:7927-7929`). The early receipt writes the prior `orders` whole (`:7934`). CONFIGURE builds
  `orders` for `selection` alone: a hole order `{"kind", "id", "path"}` with no `kit`
  (`:7962-7963`), and a machine order with `kit` (`:7993-7994`). The RECEIPT update writes
  `"orders": orders` (`:8341-8344`).
- `check` takes `selection = receipt.get("kits")` (`:5388`), so a carried kit's holes count as
  declared, and it prints `<kit>: undischargeable` for each machine order (`:5624-5629`).
- `kickoff-manifest` declares one machine-scoped rule, one `[[hole]]` (`manifest-section-b`) and one
  leg, `kickoff-manifest ratchet` (`tools/govkit/entries/kickoff-manifest.kit.toml`). `DEPLOY_FULL`
  declares no `[gate_runner]` (`tools/govkit/selftest.py:700-710`), so the `[dRB-12]` target takes
  the non-manifest branch.
- `write_gate_legs`: `_silenced` is bound over `selection` (`:4288-4289`). The non-manifest branch
  loops `selection` alone, writes `.governance/outbox/gate-legs.md`, and sets `emitted = list(prior)`
  (`:4548-4595`). `_cmd_apply` passes `carry_out_of_scope=True` (`:8264-8266`), and so does `update`
  (`:12218-12220`). `descs` holds every registry entry (`read_descriptors`, `:13187-13202`).
- The three spawns: CONFIGURE passes `encoding="utf-8", errors="replace"` (`:8038-8039`), the
  regenerate site the same (`:11309-11311`), and the gained loop `encoding="utf-8"` alone
  (`:11445-11446`). The gained loop's refusal suffix prints `. It printed nothing to stderr` when
  `_proc_g.stderr` is empty or None (`:11452-11456`). The CONFIGURE comment says the regenerate site
  and the gained loop decode as it does (`:8028-8031`). govkit reconfigures its own stdout to UTF-8
  (`:14077`), so a U+FFFD in a problem line reaches its caller intact.
- Measured over `govkit.py`'s syntax at `bf42c5113`: six `subprocess.run` calls take a
  `resolve_shell_argv(...)` first argument and an `encoding` keyword, at `:5194`, `:6284`, `:8038`,
  `:11309`, `:11445` and `:13523`. Exactly one lacks `errors="replace"`, `:11445`. Four more decode
  with the host codepage, at `:4976`, `:5231`, `:5270` and `:6177`.
- The guard: `["{prefix}/govkit/", "{prefix}/hooks/kit.toml", "{prefix}/settings-merge.py"]`
  (`tools/gate-legs.json:1430-1434`). `check_roles_install` reads codebase-map's descriptor at
  `tools/govkit/selftest.py:2797-2798`. No leg's guard names `{prefix}/codebase-map/kit.toml`.
  `check_guard_trips` is at `tools/check-spec-tokens.py:494`, and `BROAD_LEG_FLOOR` is 5 (`:262`).
- The routing arm: `ADOPTER_BAR_PATHS = ('gr["file"]', 'receipt_path', '"install.sums"')`
  (`tools/govkit/govkit.py:4177`). `read_bar_writes21` reads the constant and `GOVKIT` itself
  (`tools/govkit/selftest.py:16376-16447`), and the two liveness checks are `bool(_dest21)` and
  `bool(_routed21)` over the union (`:16449-16455`).

### Two choices, derived

**A carried kit's withheld leg raises no problem.** The record says to list carried kits' legs,
mirroring the `emitted` carry. Listing a carried leg as an instruction without the `_silenced` test
would reopen D7, which the branch's own comment names (`:4281-4287`), so every listed leg takes the
test. Whether a carried kit's withheld leg also raises a problem decides the run's verdict, and the
manifest branch answers it already: it carries a carried kit's prior rows and resolves none of its
legs, so a narrower apply over a manifest target never raises one. Raising it in the non-manifest
branch alone would give one selection two exit codes by runner kind, which is the
`two-answers-to-one-question` class. The problem was raised by the run that selected the kit, and
the order file lists the leg under `## WITHHELD`, which is the record D7 asked for.

**A keyless hole order is carried through its descriptor.** Every receipt written before this unit
holds hole orders with no `kit`. Keyed on `kit` alone, the first narrower apply after the upgrade
still loses a carried kit's hole orders, which is id 4 on every existing target. The charter's
`[core]` rule asks for an upgrade step beside an additive field, and the hole id is the join the
descriptor already holds. The carried order stays verbatim, keyless, as a carried row stays verbatim.

### What an adopter sees change

| Situation | At `bf42c5113` | After |
|---|---|---|
| `apply --kits settings-merge` after an apply of three kits, no `[gate_runner]` | the receipt's `orders` holds no order of `kickoff-manifest`; `check` prints no `undischargeable` line for it; `gate-legs.md` lists `settings-merge selftest` alone | the receipt keeps `kickoff-manifest`'s hole and machine orders; `check` prints `kickoff-manifest: undischargeable`; `gate-legs.md` lists `kickoff-manifest ratchet` too |
| the same, over a receipt an earlier engine wrote | as above | the keyless hole order is carried |
| a narrower apply where a carried kit's leg names a path the target lacks | the leg is absent from the order | the leg is listed under `## WITHHELD`, and the run's exit is unchanged |
| `update --write` gains a kit whose adopter prints a non-UTF-8 byte and is refused | the refusal line ends `It printed nothing to stderr` on Windows; on POSIX the run raises `UnicodeDecodeError` | the line ends with the adopter's stderr, the byte as U+FFFD |
| an edit to `tools/codebase-map/kit.toml` alone, under a scoped bar | the `govkit selftest` leg is skipped or reused | the leg runs |

### What this unit corrects in each spec

No one role writes these corrections and the product files in one commit. Under
`.claude/roles.json`, only `gov-spec-writer` writes spec files and only `gov-builder` writes product
files, and scratch-guard admits a builder's spec edit only where it moves the status and date cells
of a spec its card routes. So the rows below are this unit's spec-writer pass, `<w23>`, M6's "a
review's fixes folded in". The main loop dispatches it at this unit's turn, after unit 22 is CLOSED
and before the build pass, with this table as its brief. Each target is CLOSED and takes its
correction as a records fix with its status unchanged. A build pass that finds no `<w23>` returns
that to the main loop before any write.

| Spec | Ids | What moves |
|---|---|---|
| 12 | 4 | §3 Edges: the `hands-off` external bullet on `orders` (`:123-126`) becomes a `hands-off` bullet naming `TOOL-dRedressedBar-23`, saying that unit carries a carried kit's orders. Its revision line names AC1 |
| 14 | 4 | S2's "this run's `orders`" and the `orders` row of "The receipt written ahead" table, At RECEIPT, read "this run's `orders`, then every prior order of a carried kit (`TOOL-dRedressedBar-23`)". Edges gain the hands-off. Its revision line names AC1 |
| 15 | 5 | §4 "The CONFIGURE comment, restated": a sentence under the quoted comment states that its decode sentence read as saying the gained loop decodes as CONFIGURE does, that the gained loop decoded strictly until `TOOL-dRedressedBar-23`, and that the three sites now share `run_target_argv`. Edges gain the hands-off. Its revision line names AC3 |
| 16 | 4 | S1's sentence on the non-manifest branch states that it kept `emitted` whole while its order file listed the selection's legs alone, which `TOOL-dRedressedBar-23` corrects. "What an adopter sees change" gains a row for a narrower apply over a target with no runner. Edges gain the hands-off. Its revision line names AC2 |
| 17 | 13 | S23's "so the self-test's routing assertion grades the receipt" and §10's "grades the new member with no new code" each gain that the arm's liveness was aggregate over the members, so a member matching nothing passed until `TOOL-dRedressedBar-23` graded each. Edges gain the hands-off. Its revision line names AC6 |

The brief named specs 12, 14, 16 and 17. Spec 15 is added because it authored the CONFIGURE comment
the record calls false (§4 Evidence, `:8028-8031`).

### The code sites

| Id | File | Change |
|---|---|---|
| 4 | `tools/govkit/govkit.py` | `kit` on hole orders; `_carried_orders` and its comment; the RECEIPT update's `orders` |
| 4 | `tools/govkit/govkit.py` | `write_gate_legs`' carried kits, `_silenced` over them, the non-manifest loop, the docstring paragraph |
| 4 | `tools/govkit/selftest.py` | the `[dRB-12]` block's keyless strip and order, `check` and order-file checks; the `[dRB-23]` no-runner case |
| 5 | `tools/govkit/govkit.py` | `run_target_argv`; the three spawns; the CONFIGURE comment's decode sentence |
| 5 | `tools/govkit/selftest.py` | the `[dRB-23]` gained case and the static class checks |
| 12 | `tools/gate-legs.json`, `memory/guides/SESSION-KICKOFF.md` | one guard path; the re-stamps |
| 13 | `tools/govkit/selftest.py` | `read_bar_writes21(members, src)` and the per-member checks |

### The fixtures

All new selftest code names `encoding="utf-8"` on every text read, write and process call, so the
`tools/govkit/selftest.py` rows of `memory/project/encoding-posture-sites.txt` (`subprocess 24`,
`file-io 1`) do not move. `run_target_argv` names its encoding, so the `govkit.py` row
(`subprocess 35`) does not move either.

- **`[dRB-12]`, extended.** After `_rb12r1b` is read and before `_rb12p2` runs
  (`tools/govkit/selftest.py:3511-3512`), the block reads the receipt, removes the `kit` key from
  every `kind == "hole"` order, writes it back and settles, as a receipt an earlier engine wrote.
  After `_rb12p2` it checks that the receipt's orders of the two carried kits equal those of the stripped receipt, in order and as
  JSON, and that they hold a `machine` order and the `manifest-section-b` hole order. It checks
  that `_rb12chk`'s stdout carries a line opening `govkit check — kickoff-manifest: undischargeable`,
  and that `.governance/outbox/gate-legs.md`, cut at its first `## WITHHELD` line, carries a line
  opening `- kickoff-manifest ratchet: `.
- **`[dRB-23]` no-runner case**, after the `[dRB-16]` block, from `build_gov13` and
  `build_target13(..., M13_DEPLOY_NONE)`. `apply`, settle, `apply --kits demo`, settle: the order's
  instruction half carries `- demo2 leg: `. Then the gov's `demo2/kit.toml` is rewritten by
  `build_kit13("demo2", "demo2 leg", "demo2/absent.sh", False)` and committed, and
  `apply --kits demo` runs again: it exits 0, the instruction half carries no `demo2 leg`, the
  `## WITHHELD` half does, and no output line carries `declares gate leg 'demo2 leg'`.
- **`[dRB-23]` gained case**, from `build_gov13` and `build_target13(..., M13_DEPLOY_NONE)`. After
  `apply` and settle, the gov gains a third kit, `demo3`: its `kit.toml` is
  `build_kit13("demo3", "demo3 leg", "demo3/engine.sh", False)` with `[adopt] argv` set to
  `["bash", "{prefix}/demo3/adopt.sh"]`, an `engine.sh` of `exit 0`, and an `adopt.sh` whose bytes
  are written with `write_bytes` as `printf 'J\366rg\n' >&2` and `exit 2` on two lines, each
  backslash a literal byte. The registry is `M13_REG` with `demo3` appended to `[selection] default`
  and as an `[[entry]]`. The gov commits, and `update --target <t> --write` runs.

### Order, and unit 7

Order 17 places this unit after units 21 and 22, at orders 15 and 16, and the README's derived
build-order region says so. Both of them, like this unit's S7, regenerate `memory/map/generated/`
(their §4 Files touched), so M6's first and third clauses sequence the three. None reads another's
work, so each is a sequence and not an edge. Unit 7's measurement need not cover this unit, because no kit version moves (§3). S3
mints one function, so S7 regenerates `memory/map/generated/` itself.

### Inventory

| Identifier | Kind | Naming cell |
|---|---|---|
| `run_target_argv` | a module-level function | `py.function`. `python tools/lexicon/lexicon.py --suggest run_target_argv --as py.function` prints a line opening `OK — run_target_argv leads with` at `bf42c5113` |
| `_carried_orders` | a local in `_cmd_apply` | none. `grep -c '_carried_orders' tools/govkit/govkit.py` prints 0 at `bf42c5113` |
| `kit` on a hole order | a receipt `orders` key, additive | none |
| `[dRB-23]` | the check-label prefix of the new selftest checks | none |

### Files touched (estimate)

- `tools/govkit/govkit.py`
- `tools/govkit/selftest.py`
- `tools/gate-legs.json`
- `memory/guides/SESSION-KICKOFF.md`
- `memory/map/generated/`
- `memory/builds/dRedressedBar/build/`

Specs 12, 14, 15, 16 and 17 are `<w23>`'s write set, not the build pass's.

### Alternatives rejected

| Candidate | The test that rejected it | Verdict |
|---|---|---|
| Id 4 keyed on `kit` alone | every receipt written before this unit holds keyless hole orders, so the first narrower apply after the upgrade still loses them | Rejected on `[core]` |
| Id 4 with a carried kit's withheld leg raising a problem | the manifest branch raises none for the same selection, so the exit code would depend on the runner kind | Rejected (§4, "Two choices") |
| Id 4 listing carried legs with no `_silenced` test | it writes a leg naming a path the target lacks as an instruction, the D7 defect (`:4281-4287`) | Rejected on `[security]` |
| Id 5 by `errors="replace"` at the gained loop alone | three sites keep three spellings of one decode rule, the drift the record found | Rejected on `[reuse]` |
| Id 5's class arm over every text-mode `subprocess.run` in `govkit.py`, as the record's first left-shift reads | measured, 53 calls decode text without `errors="replace"`, almost all git spawns, so it reds on sites no finding names | Rejected; S4 grades the UTF-8 population of target-side spawns |
| Id 12 by `{prefix}/codebase-map/` as a directory | it would add a seventh leg to that directory's guard count, and the spec-tokens join excludes a guard carried by more than `BROAD_LEG_FLOOR` legs | Rejected; the record asks for the exact file |
| Id 13 with an `'"install.json"'` member | the walk is name-based, and `receipt` names the parsed dict at three sites (§3) | Rejected |
| The spec corrections in the build pass's commit | scratch-guard refuses a builder's edit to another spec | Refused by the hook |

## 5. Production-readiness checklist

- security — S2 keeps the D7 rule for carried legs: no leg naming a path the target lacks is written
  as an instruction. S3 narrows a failure mode: an adopter's stderr bytes can no longer raise inside
  `update` or blank its refusal reason. Nothing new reads from outside gov's descriptors and the
  target's receipt.
- perf / scale — N/A — one list comprehension per apply, one `silenced_legs` walk over a few more
  kits on a narrower apply, and no new process.
- error / empty / loading states — A receipt with no `orders`, or with orders that are not dicts,
  carries nothing. A carried kit that gov's registry no longer declares has no descriptor, so its
  legs are not listed and its keyless hole orders are not matched; its keyed orders are carried.
- observability — `check` reports a carried kit's machine order and verifies its outbox files again,
  and a refused gained adopter's line carries its own reason.
- risks — For a kit `update` rolled back, the order lists gov's current leg argv while the manifest
  branch carries the prior row; the order is a hand-wiring instruction and says nothing runs it, so
  this is stated and not fixed. The `govkit selftest` guard widens by one file, so a scoped bar runs
  that leg on an edit to codebase-map's descriptor. Editing `tools/gate-legs.json` trips the
  run-gates canaries and the kickoff-manifest ratchet, which S5 re-stamps.
- testing — AC1 to AC8 are applies and updates over scratch targets under `%TEMP%`, in-process
  python probes, syntax walks and greps. The arms are declared in §7.
- migration — S1's `kit` key is additive. A receipt an earlier engine wrote is read as before, and
  its keyless hole orders are carried by the descriptor join.
- user docs — N/A — `help/` holds no govkit page, and the runbook's one sentence on `orders` stays
  true (§3).

## 6. Acceptance criteria

AC<n> observes S<n>. `<p23>` is this unit's product commit, `<p23m>` its manifest re-stamp commit
and `<w23>` its spec-writer pass, each named by this unit's ledger. Every command runs from the
worktree root. A target is a fresh `git init` tree under `%TEMP%/<short-name>`, never inside the
worktree, with `core.autocrlf false`, and is committed after each step. A red half "over
`bf42c5113`" runs `python <clone>/tools/govkit/govkit.py` from a local `git clone` of gov under
`%TEMP%`, checked out at `bf42c5113`. A scratch gov is built as `build_gov13` builds it
(`tools/govkit/selftest.py:15904-15935`), from the `govkit.py` the criterion names.

- **AC1** — Over a target whose `.governance/deploy.toml` is `DEPLOY_FULL`, run
  `python tools/govkit/govkit.py apply --target <t> --kits agent-cap,settings-merge,kickoff-manifest`
  twice. Remove `kit` from every `kind == "hole"` order of `.governance/install.json` and commit.
  Run `python tools/govkit/govkit.py apply --target <t> --kits settings-merge`. Its receipt's orders
  whose `kit` is `agent-cap` or `kickoff-manifest`, plus the keyless `manifest-section-b` hole order,
  equal the stripped receipt's, as JSON and in order. They hold one `machine` order of
  `kickoff-manifest`. `python tools/govkit/govkit.py check --target <t>` prints a line opening
  `govkit check — kickoff-manifest: undischargeable`. `.governance/outbox/gate-legs.md`, cut at its
  first `## WITHHELD` line, carries a line opening `- kickoff-manifest ratchet: `. Every hole order a
  fresh three-kit apply writes carries `kit`.
  Red when: over `bf42c5113`, the narrower apply's receipt holds no order with `kit`
  `kickoff-manifest` and none with id `manifest-section-b`, `check` prints no `undischargeable` line,
  and the order file lists `settings-merge selftest` alone. A scratch copy of the tip whose carry
  keys on `kit` alone loses `manifest-section-b`.
  cost: three applies and a `check` per engine, about four minutes.
- **AC2** — Over a scratch gov from the tip's `govkit.py` and a target whose deploy is
  `M13_DEPLOY_NONE`, run `apply`, then `apply --kits demo`. The order file's instruction half, cut at
  `## WITHHELD`, carries a line opening `- demo2 leg: `. Rewrite the gov's `demo2/kit.toml` with leg
  engine `demo2/absent.sh`, commit, and run `apply --kits demo` again. It exits 0. The instruction
  half carries no `demo2 leg`, the `## WITHHELD` half carries `demo2 leg`, and no line of its output
  carries `declares gate leg 'demo2 leg'`.
  Red when: over a gov from `bf42c5113`'s `govkit.py`, the order file after the first narrower apply
  carries no `demo2 leg` anywhere. A scratch copy of the tip whose non-manifest loop reads the
  carried kits without the `_silenced` test lists `demo2 leg` in the instruction half.
  cost: two govs and six applies, about two minutes.
- **AC3** — A python program run from `tools/govkit` imports `govkit` and calls
  `govkit.run_target_argv([sys.executable, "-c", <prog>], <tmp>)`, where `<prog>` writes the five
  bytes `4a f6 72 67 0a` to `sys.stderr.buffer` and exits 2. It returns `returncode` 2, and its
  `stderr` is four characters and a newline: `J`, U+FFFD, `rg`. `inspect.getsource` of `_cmd_apply`
  carries `run_target_argv(` once, and of `_cmd_update` twice. Over the gained case of §4 "The
  fixtures", built from the tip's `govkit.py`, `update --target <t> --write` prints exactly one line
  opening `govkit: kit 'demo3': its adopter exited 2 on the update that gained it`. It carries
  `Its stderr ended: J` followed by U+FFFD and `rg`, and no `It printed nothing to stderr`. No
  output line carries `UnicodeDecodeError`.
  Red when: over `bf42c5113`, `govkit` has no `run_target_argv`, and the same program spawning
  `<prog>` as the gained loop does (`capture_output=True, text=True, encoding="utf-8"`) reads
  `stderr` None on this Windows host. The gained case built from `bf42c5113`'s `govkit.py` prints a
  problem line ending `It printed nothing to stderr`, and no line carries `Its stderr ended: J`.
  fixture: on POSIX the red half raises `UnicodeDecodeError` out of the run instead of printing the
  line; the pass records which host it ran on.
- **AC4** — A python program parses `tools/govkit/govkit.py` with `ast` and selects every
  `subprocess.run` call whose first positional argument is a call to `resolve_shell_argv` and which
  passes an `encoding` keyword. Every selected call passes `errors="replace"`, and one of them sits
  inside the body of `run_target_argv`. Exactly three call nodes call `run_target_argv`.
  Red when: over `bf42c5113` the same program names exactly one call lacking `errors="replace"`, the
  gained loop's at `:11445`, and finds no `run_target_argv`.
  figure: the population is DERIVED at observation. At `bf42c5113` it was 6, PINNED on 2026-10-15.
- **AC5** — A python program loads `tools/gate-legs.json`. The `govkit selftest` leg's `guard` holds
  `{prefix}/codebase-map/kit.toml`, and that string is carried by at most 5 legs. Loading
  `tools/check-spec-tokens.py` with `importlib`, `check_guard_trips("tools/codebase-map/kit.toml", g)`
  is true for that guard entry with `{prefix}` read as `tools`. The `last-audit:` line of
  `memory/guides/SESSION-KICKOFF.md` names a commit at which `git show <sha>:tools/gate-legs.json`
  holds the new path, and `git log -1 --format=%B <p23m>` carries `manifest-audit:`.
  Red when: over `bf42c5113` no entry of that guard trips `tools/codebase-map/kit.toml`.
- **AC6** — A python program extracts the `read_bar_writes21` definition from
  `tools/govkit/selftest.py` with `ast` and executes it in a namespace binding `_ast` and `_re`.
  Called with each member of `govkit.ADOPTER_BAR_PATHS` alone and the tip's `govkit.py` text, it
  returns at least one routed line for every member. Called over a copy of that text in which every
  whole-word `receipt_path` reads `rcpt_file`, it returns none for `receipt_path` alone, and the
  union still returns routed lines and no direct write. The selftest's `[-21] AC2` checks hold one
  per member whose label carries the member.
  Red when: over `bf42c5113`, the same renamed copy, fed to that tip's `read_bar_writes21` through a
  namespace whose `GOVKIT` names the copy and whose `govkit_module()` returns the constant, leaves
  `_dest21` and `_routed21` non-empty and `_direct21` empty, so all three `[-21] AC2` checks pass
  while the receipt member grades nothing.
- **AC7** — A one-liner loading `memory/map/generated/symbols.json` finds an entry with id
  `run_target_argv` and file `tools/govkit/govkit.py`, and `python tools/lexicon/lexicon.py --suggest run_target_argv --as py.function`
  prints a line opening `OK`.
  Red when: the entry is absent, as at `bf42c5113`.
- **AC8** — `git diff <w23>~1 <w23> -- memory/builds/dRedressedBar/spec/` shows specs 12, 14, 15, 16
  and 17 each with one header rev change and one new revision line naming `TOOL-dRedressedBar-23`
  and the report id §4's table assigns it, and each Edges section carrying a `hands-off` bullet
  naming `TOOL-dRedressedBar-23`. Each of the five carries a CLOSED header at `<w23>` and at
  `<w23>~1`. `git diff --name-only <p23>~1 <p23> -- memory/builds/dRedressedBar/spec/` and the same
  over `<p23m>` name no file but this spec. The ledger S8 names exists and carries
  `**Serves:** journal TOOL-dRedressedBar-23`.
  Red when: a spec takes no bump, two bumps or a line missing its id, a status moves, or a
  build-pass commit writes another spec.

## 7. Gates

`govkit selftest` · `govkit acceptance matrix` · `govkit refusal join` · `govkit selfcheck` · `receipt sync (installed files match the receipt)` · `run-gates canary` · `run-gates gov canary` · `kickoff-manifest ratchet` · `codebase-map coverage + freshness` · `lexicon naming predicates` · `encoding posture (text IO names its encoding)` · `spec tokens (a spec's own names resolve)` · `recall floor` · `recall floor arms` · `memory hygiene`

The line is a floor. Joined at `bf42c5113` against the guards in `tools/gate-legs.json` with
`{prefix}` read as `tools`, the Files touched trip `govkit selftest`, `govkit acceptance matrix`,
`govkit refusal join`, `recall floor arms`, `run-gates canary`, `run-gates gov canary` and
`recall floor`. The rest are unguarded legs this unit's files feed.

New arm: tools/govkit/selftest.py · covers AC1 · the `[dRB-12]` order checks over a copy of the tip whose RECEIPT update writes `"orders": orders`, where the carried machine and hole orders are missing and `check` prints no `undischargeable` line · none
New arm: tools/govkit/selftest.py · covers AC2 · the `[dRB-23]` no-runner case over a copy whose non-manifest loop iterates `selection` alone, where the first narrower apply's order lists no `demo2 leg` · none
New arm: tools/govkit/selftest.py · covers AC3 · the `[dRB-23]` gained case over a copy whose `run_target_argv` passes `encoding="utf-8"` alone, where the problem line ends `It printed nothing to stderr` · none
New arm: tools/govkit/selftest.py · covers AC4 · the `[dRB-23]` static checks over a copy whose `run_target_argv` passes no `errors` keyword, where the predicate names that call · none
New arm: tools/govkit/selftest.py · covers AC6 · the per-member `[-21] AC2` checks over a copy in which every `receipt_path` is spelled `rcpt_file`, where the `receipt_path` member's check reds · none

The refusal join's floor does not move: S1 and S2 add no `r.fail` site, and S2 narrows which legs
reach the existing one. The main loop observes each arm red, then green, at the close.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-15 · initial draft, promoted at the round-1 closing diff review's CLEAN WITH FIXES
  exit by the owner's ruling of 2026-10-15. Report ids 4, 5, 12 and 13 are batched here. Each claim
  was re-read at `bf42c5113`. Two choices the record leaves open are derived in §4, and spec 15 is
  added to the brief's list of specs `<w23>` corrects. Drafting note, within rev-1 and before any
  commit: the H1 was shortened to fit hygiene check 7's 350-byte cap on the build README's unit
  row, and §4 Evidence names unit 21's guard edit and re-stamp, both per
  `prompts/2026-10-15-prompt-TOOL-dRedressedBar-21-4-revision.md`.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "spawn a kit's target-side argv and decode its stderr as
utf-8 with replacement"` ranked `resolve_shell_argv` (`tools/govkit/govkit.py:1197`, fan-in 2) among
name-stem neighbours, and it is the seam S3 extends: `run_target_argv` calls it and sits beside it.
`python tools/codebase-map/reuse_lookup.py "carry a claimed kit's outbox orders from the prior
receipt on a narrower apply"` ranked name-stem neighbours (`claims`, `kit_rel`, `derive_carry_map`)
and no carry of receipt state, a miss recorded as a miss; `derive_carry_map` is `update`'s needle
map and not this carry. The seams extended were found by reading the record's citations:
`_carried_kits` and `_carried_rows` (`:7927-7929`) for S1, the `carry_out_of_scope` parameter and
`_silenced` of `write_gate_legs` (`:4227-4289`) for S2, the existing guard for S5, and
`read_bar_writes21` (`tools/govkit/selftest.py:16376`) for S6. `build_gov13`, `build_target13`,
`build_kit13`, `M13_REG` and `M13_DEPLOY_NONE` are reused for the fixtures, and the `[dRB-12]` block
is extended rather than copied. The manifest re-stamps follow `809f794e4` and `cafbbc460`.

The gotchas checklist for `tools/govkit/govkit.py`, `tools/govkit/selftest.py` and
`tools/gate-legs.json` selected these classes, each answered here:
- `held-suite-guard-misses-a-sibling-kit`, the class of id 12, which S5 closes for the one read the
  diff added; §3 says why the class arm is not this unit's.
- `two-answers-to-one-question`, which is why S3 holds one decode rule and S2 gives one exit code
  per selection whatever the runner kind.
- `a-new-local-collides-in-a-long-function`, which is why §4 Inventory greps `_carried_orders`.
- `a-folded-field-leaves-its-row-shape-docs-behind`, for S1's `kit` key: the runbook names the
  `orders` list and no key set (`WIRE-INTO-PROJECT.md:1490`).
- `a-new-leg-trips-a-growing-set-of-meta-gates`, which is why §7 names the canaries and the
  manifest ratchet for a guard edit.
- `fixture-passes-by-finding-nothing` and `staged-break-substitutes-a-synthetic-value`, which is why
  AC4 asserts the population holds the helper's call and AC6 stages the rename over the real engine
  text.
- `line-claim-matched-over-the-whole-output`, which is why AC2 cuts the order file at `## WITHHELD`
  and AC3 reads the one line it names.

The recall probe returned spec 12, the record's M3 item, spec 14 and spec 16, the units whose carry
this extends. The record and the code agree on every citation re-read, give or take a line: the
guard sits at `tools/gate-legs.json:1430-1434` and the read at `tools/govkit/selftest.py:2797-2798`.

Recall terms used: `python tools/memory-recall/query.py "how does a narrower apply carry a claimed
kit's receipt state, and where do adopter spawns decode stderr" --terms "narrower apply carried kit
orders receipt write_gate_legs gate-legs outbox decode errors replace guard liveness"`
