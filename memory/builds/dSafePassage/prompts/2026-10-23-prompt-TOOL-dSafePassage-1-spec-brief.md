**Serves:** research TOOL-dSafePassage-1 TOOL-dSafePassage-2 TOOL-dSafePassage-3 TOOL-dSafePassage-4 TOOL-dSafePassage-5 TOOL-dSafePassage-6 TOOL-dSafePassage-7 TOOL-dSafePassage-8 TOOL-dSafePassage-9 TOOL-dSafePassage-10 TOOL-dSafePassage-11 TOOL-dSafePassage-12 TOOL-dSafePassage-13

# Spec brief — dSafePassage, the thirteen units and the interfaces they share

You write specs and no product code. This is the spec run: README rule 1 says it specs, audits and defers every
unit, and the build run builds them after dGroundRules lands. Read these in order before your first line:

1. The packet, `memory/builds/dSafePassage/prompts/2026-10-21-prompt-PLAY-dClosedLoop-1-packet.md`, whole. Its
   Items section quotes each clause with its id, hash and tokens. Its Acceptance, Gates, Non-goals, Pins, Owned
   nodes, Parents, Gaps, Policy keys and Obligations sections bind every unit.
2. The build README, `memory/builds/dSafePassage/README.md`, and its build-level rules. Rule 6 (fork rungs) and
   rule 7 (writes stay in this folder) bind every spec.
3. `memory/TEMPLATE-SPEC.md`, and `memory/guides/BUILD-METHOD.md` M2, M3 and M5. Every unit is Tier 2, because each
   one is a new or changed kit contract (`memory/guides/SESSION-KICKOFF.md`, Tier rule).
4. The design sources. `B/` is `memory/builds/dClosedLoop/build/`:
   - `B/2026-10-18-build-PLAY-dClosedLoop-1-research-supersession.md`, whole. It is the mechanism (candidate E),
     today's update path with its code lines, and the losing test. Its line numbers are from an older
     `govkit.py`, so re-find each one before citing it.
   - v2, `B/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md`: `[principles]` P38 (from line 1062) and P42
     (near line 1088), the `[policies]` rows at lines 1294 and 1346 and 1403-1406, and the dSafePassage row of
     `[chain]` at line 1766. It is 428 KB, so read only those ranges.
   - The rulings the clauses cite: SA-n in `B/2026-10-18-build-PLAY-dClosedLoop-1-shape-reviews-compared.md`;
     AP-n in `B/2026-10-18-build-PLAY-dClosedLoop-1-away-pass.md`; A4-Fn and C1-Fn in
     `B/2026-10-19-build-PLAY-dClosedLoop-1-whole-audit.md`; and FK-1-3, FK-1-4 and FQ-5 wherever `git grep -n` finds
     them under `B/`. Read the passage your clause cites, not the whole record.
5. Your units' sections below, and the "Shared interfaces" section, which every writer reads.

You never edit an instrument, v2, the as-built view or the packet (the packet's Non-goals).

## Every spec, whatever its unit

- The path is `memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-<n>.md`. The H1 is
  `# TOOL-dSafePassage-<n> — <title>`, with an EM DASH and never a colon, because the index and `--plan` read
  nothing else.
- The status header is `**Status:** OPEN · rev-1 · 2026-10-23 · node d · Tier-2 · base 3708a705 · streams tooling ·
  order <n> · advances TOOL-dSafePassage-14`. Take `<n>` from your group below. The main loop flips it to `DEFERRED`
  after the audit.
- Put each binding line at column 0 on a line of its own, in the shape `carries.py`'s `CARRY` regex parses:
  `**Carries:** <the Items id>@<hash8> whole`. A unit that builds an owned node adds
  `**Carries:** node:policy-key.<key>` too, as `TOOL-dTrueNorth-4` carries `node:record-kind.deviation`.
- Every token the packet's Items list for your clause appears in your spec verbatim, inside backticks, because the
  token arm reads them. `cl-dClosedLoop-0021` has none.
- Each "seen red on" case in your clause is an acceptance criterion. It is observed RED on its planted case and
  green without it, by a probe or fixture of the unit's own code that a pass can run. No criterion names the merge
  bar, a `GATE_*=` prefix, a `*.test.sh` suite or a `--selftest` run. A new suite arm goes on a `New arm:` line in
  §7, and the main loop observes it at the close.
- Name each gap your unit closes, from the packet's Gaps, in §1 or §3 with its id.
- For §10, run `python tools/codebase-map/reuse_lookup.py "<behaviour>"` and
  `python tools/memory-recall/query.py "<question>" --terms "<8-14 terms>"`. Record the seam, the terms you used and
  where each hit disagrees with source.
- Settle every §8 fork by README rule 6's rungs (the execution plan's `[phase-2]`, "How a fork is settled when
  nothing may park", `B/2026-10-20-build-PLAY-dClosedLoop-1-execution-plan.md` lines 901-948), in the §8 mark shape TEMPLATE-SPEC states. A choice on rung 5 or 6
  cites its ruling (ER:240, ER:388, ER:328 or P0.8 row 5) and carries `widens:` and `relaxes:`, each a value or
  `none`. Never leave an open question. A FACT-QUESTION names its probe, and you run that probe now.
- Files touched names every product path. They become the unit's `--dispatch --writes` set in the build run.
- **The parent is unbuilt.** dGroundRules has not been specced, and its clauses are this build's interface to the
  policy file. Cite them by clause id as the contract: `cl-dClosedLoop-0007` (the `.governance/policy.toml` schema,
  a catalogue row carrying a summary and a usage), `cl-dClosedLoop-0008` (the reader, `read_policy_key`'s contract),
  `cl-dClosedLoop-0015` (`budgets.*`) and `cl-dClosedLoop-0016` (`runtime.agents-in-flight`). Never invent a name
  for something those clauses name. State in §8 that the build run re-grounds against the landed parent first.
- A departure from your clause (a narrowing, a changed case, a dropped term) is a deviation record. Write it beside
  your spec as `memory/builds/dSafePassage/build/2026-10-23-build-TOOL-dSafePassage-<n>-deviation-<k>.md`, in the
  grammar of `memory/HYGIENE.md` "Deviation records", approver `author`, under the chain's `author-recorded`
  value. `<k>` must be unique within the build, so it is ten times your order plus your record's number in your
  group: order 2's first record is `deviation-21`. Do not commit it; the commit stage commits it with the specs.

## Shared interfaces — one spelling for every writer

These are fixed so that thirteen specs from five writers agree on the interface axis (M2). If one is wrong, say so
in your §8 as a fork and settle it there. Never respell one silently.

- **S1 · the step row.** A kit descriptor's `kit.toml` declares `[[upgrade]]` rows with these keys: `id`
  (`<entry>/<slug>`), `introduced` (the gov commit that lands it), `up` and `down` (argv lists, run from gov's
  checkout), `witness` (an argv list whose exit 0 means applied), `surfaces` (S6 member ids it carries),
  `needs-target` (a bool: whether the step needs the target's code), and `resume` (optional: `atomic`, or an argv
  list). Steps for surfaces no descriptor owns, the receipt and the interpreter floor, are rows of the same grammar
  in `tools/govkit/steps.toml`. Unit 1 owns the grammar, its one reader and the frozen-row check.
- **S2 · succession.** `tools/govkit/registry.toml` gains `[[retired]]` rows: `id` (the old entry id), `successor`
  (an entry id or `none`), `retired` (the commit) and `surfaces`. Unit 1 owns them. `update` and `check` read them
  through unit 1's reader.
- **S3 · one module.** `tools/govkit/upgrade_steps.py` holds the step machinery: unit 1's reader, unit 2's walk and
  lock reclaim, unit 4's reverse walk, and unit 7's isolated runner. `govkit.py` calls it and re-parses nothing.
  Each unit names its own functions in its Inventory.
- **S4 · the receipt.** `RECEIPT_SCHEMA = 4` in `tools/govkit/govkit.py`. The receipt gains `steps`, a list of
  objects `{"id", "introduced", "state"}`, where `state` is `applied`, `failed` or `rolled-back`. A failed row adds
  `"failure"`, and the list's last `applied` row is the last completed step. Unit 3 owns the field and the schema
  step. Units 2, 4 and 8 write it through one writer unit 3 names.
- **S5 · step order and the first two steps.** The walk orders steps by their `introduced` commit along gov's
  first-parent history, then by row order. The first step is `govkit/receipt-schema-4` (unit 3). The second is
  `lib/python-floor-3.15` (unit 11). Both are rows in `tools/govkit/steps.toml`.
- **S6 · the surface population.** Unit 10 owns one reader of the adopter-visible members, by class. The classes
  are receipt `files` rows, installable descriptor paths, hook entries, commands, agents, conf keys, policy keys,
  CLI verbs and registry entries. Each member's id is `<class>:<name>`. Steps' `surfaces` and `[[retired]]` rows
  name members by that id. The class registry is `tools/govkit/surface-classes.toml`, where a later build's class
  joins with its own row.
- **S7 · the legs.** Each of these is a row in `tools/gate-legs.json`. Unit 5's leg is `upgrade-walk`. Unit 10's is
  `step-gate`, run by `tools/govkit/step_gate.py`. Unit 13's is `docs`, an arm over S6's population run by
  `tools/govkit/docs_leg.py`, which imports unit 10's reader. Unit 11 retires `merge-rows.test.sh`'s PEP 701 ban
  and adds no leg.
- **S8 · the fixture.** Unit 5's release-0 tree is generated, never hand-copied. `apply` writes it at a pinned
  commit into a scratch clone, and the pin lives in `tools/govkit/fixtures/release-0/pin.txt`. The planted edits
  are declared in `tools/govkit/fixtures/release-0/plants.toml`.
- **S9 · the floor.** One declaration, `tools/lib/python-floor.txt`, holding one line, `3.15`. The resolver
  (`tools/lib/resolve-python.sh`), the preflight, remote CI's setup step (unit 12) and every other floor statement
  read it.
- **S10 · gov's own receipt.** Unit 8 creates gov's source-mode receipt at the adopter path,
  `.governance/install.json`, with `"mode": "source"`. It fixes `plan`'s refusal of gov's `.governance/deploy.toml`
  (probe B in the research), so `update` runs on gov's own tree the way an adopter runs it.
- **S11 · the policy keys.** Each owned key is a catalogue row under `cl-dClosedLoop-0007`, with its Allowed values
  and default from v2's `[policies]` rows. It is read through `read_policy_key` (`cl-dClosedLoop-0008`) and owned by
  the unit that builds it: `help.enforce` by unit 13, `platforms.provision` by unit 11,
  `install.deprecation-window` and `install.on-shim-call` by unit 6, and `install.retired-edits` by unit 9.

## The units

**Writer groups.** The `order` value is the writer group and the build order. The packet's Items number is the
unit's number.

| Order | Units | What they share |
|---|---|---|
| 1 | 1, 3 | the step row, succession, frozen rows, the receipt's schema 4 |
| 2 | 2, 4, 7 | the walk, the reverse walk and rollback, the isolation contract |
| 3 | 11, 12, 8 | the floor step, gov's executors at the floor, gov first |
| 4 | 6, 9, 10 | shims, retired edits and unwired hooks, the step gate |
| 5 | 13, 5 | the docs leg, the release-0 fixture and the `upgrade-walk` leg |

- **TOOL-dSafePassage-1**, Items 1. S1, S2 and S3's reader. It declares the legacy homes as the translation window's
  population: `.agent-cap.conf`'s `FANOUT_CAP` moves into `runtime.agents-in-flight` (seen on a planted
  `FANOUT_CAP=2`), and `template-size-limits.txt`'s rows move into `budgets.*`, each step retiring its file. Landed
  rows are frozen, seen red on a planted edit and a planted removal. Gaps gap-deploy-15 and gap-deploy-16.
- **TOOL-dSafePassage-3**, Items 3. S4, and the step `govkit/receipt-schema-4`, whose down restores schema 3. It
  pins the `gov_oid` back-fill to `schema < 3`. It inventories the receipt's readers by value: govkit, matrix's
  schema fixtures and `check-receipt.py`. It is seen red on a planted schema-3 receipt.
- **TOOL-dSafePassage-2**, Items 2. The walk: oldest first, a step skipped when its witness holds, the receipt
  advanced per completed step, a failed or killed step stopping the walk with the failure recorded, and a dead
  holder's lock reclaimed. Gap gap-deploy-19.
- **TOOL-dSafePassage-4**, Items 4. Down steps in reverse, each tolerating a killed up's partial state, and a
  recorded rollback that lifts the downgrade refusal for a rollback only. Gap gap-deploy-17.
- **TOOL-dSafePassage-7**, Items 7. The isolated runner in S3: a declared working directory, a scrubbed environment,
  `-I`, `core.hooksPath` emptied through `GIT_CONFIG_COUNT`, and no ambient credential. It is seen on a planted
  target hook and a planted target module, each not run.
- **TOOL-dSafePassage-11**, Items 11. S9, the step `lib/python-floor-3.15`, the resolver's refusal and preference,
  and the `platforms.provision` key. It retires the PEP 701 ban. Gaps gap-tool-22 and gap-tool-12.
- **TOOL-dSafePassage-12**, Items 12. `.github/workflows/remote-ci.yml` sets up Python at S9's floor in every job
  that runs Python, its action pinned by full sha, with the floor's preflight as the bar's first step. Gap
  gap-tool-23.
- **TOOL-dSafePassage-8**, Items 8. S10. The lander runs each new step on gov's tree in the prepared merge, it is
  recorded in gov's receipt, and it is seen red on a planted step whose witness fails on gov. Gap gap-deploy-20.
- **TOOL-dSafePassage-6**, Items 6. Forwarding shims for a moved command, hook path or module import, under
  `install.deprecation-window` and `install.on-shim-call`. Gap gap-deploy-24.
- **TOOL-dSafePassage-9**, Items 9. Withdrawn hook fragments unwired, the `retired-edited` state under
  `install.retired-edits`, and the edited-render case. Gap gap-deploy-18.
- **TOOL-dSafePassage-10**, Items 10. S6 and the `step-gate` leg, with each planted rename and removal red and
  green. Gap gap-deploy-25.
- **TOOL-dSafePassage-13**, Items 13. The `docs` leg under `help.enforce`, with its usage rows, fingerprints,
  page-command tests, offline link check and shrink-only list. Gap gap-found-35.
- **TOOL-dSafePassage-5**, Items 5. S8 and the `upgrade-walk` leg, walking every step the units above declare:
  up, down byte-identical, up again, each step skipped once, killed once and failed once. Gap gap-tool-10.
