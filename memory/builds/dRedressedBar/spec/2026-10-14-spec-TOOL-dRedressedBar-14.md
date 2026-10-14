# TOOL-dRedressedBar-14 — a first apply at a per-kit prefix configures against the homes it just wrote: the receipt is written ahead of CONFIGURE

**Status:** SPECCED · rev-2 · 2026-10-14 · node d · Tier-2 · base ebce889c · streams tooling · order 10

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-14-prompt-TOOL-dRedressedBar-14-2-revision.md](../prompts/2026-10-14-prompt-TOOL-dRedressedBar-14-2-revision.md) | research | — |
| [2026-10-14-prompt-TOOL-dRedressedBar-14-3-spec-writer.md](../prompts/2026-10-14-prompt-TOOL-dRedressedBar-14-3-spec-writer.md) | journal | — |
| [2026-10-14-prompt-TOOL-dRedressedBar-14-brief.md](../prompts/2026-10-14-prompt-TOOL-dRedressedBar-14-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

`TOOL-dRedressedBar-11`'s writer recorded this as an external hand-off. A first `govkit apply` that
selects agent-cap with `[kit.agent-cap] prefix = "scripts"` exits 1, and both adopters exit 2.
`_cmd_apply` runs CONFIGURE (`tools/govkit/govkit.py:7663-7772`) before it writes the receipt
(`:8017-8030`). settings-merge.py finds the hook through `resolve_kit_dir`
(`tools/settings-merge.py:192`), which reads `.governance/install.json` first. With no receipt yet,
it looks only at the two static homes, so a hook landed at `scripts/hooks/agent-cap.js` is not
found. This unit writes the receipt once ahead of CONFIGURE, built from the same lists the RECEIPT
step writes. RECEIPT then rewrites it. So every adopter resolves this run's homes, and the term unit
11 adds reads the same bytes the adopter reads.

Measured at spec time: agent-cap's exit 2 has a second, independent cause, which the receipt does
not reach. That cause is a separate mechanism, and §8 F1 asks where it goes.

## 2. Scope (IN)

- **S1** — `_cmd_apply` writes `.governance/install.json` between HOOKPROBE (`:7648-7661`) and
  CONFIGURE (`:7663`). The bytes are one dict, `_rcpt_doc`, with the same keys in the same order as
  the write at `:8019-8026`. The values are those in §4 "The receipt written ahead". Unit 12's
  `_carried_kits` and `_carried_rows` are bound there, once, rather than in the RECEIPT step. The
  `(target / ".governance").mkdir(exist_ok=True)` line moves up with them. One line prints after the
  write: `govkit apply — receipt written ahead of CONFIGURE: <n> row(s), <k> kit(s); RECEIPT rewrites it`.
  Observed by AC1, AC3 and AC4.
- **S2** — The RECEIPT step updates `_rcpt_doc` with `files` re-derived as `rows + _carried_rows`,
  and with this run's `orders`, `after_map` and `gate_runner`. It writes `_rcpt_doc` with the encoding
  and newline arguments it uses today. `install.sums` and the `STEP_RECEIPT` counts are derived from
  `_rcpt_doc`'s lists. Observed by AC1 and AC2.
- **S3** — A comment above the S1 write says why it exists. It gives the per-kit-prefix case. It
  names the class: adopters that find a sibling kit through the receipt. And it says that RECEIPT
  rewrites the file. Observed by AC5.
- **S4** — One `[dRB-14]` block in `tools/govkit/selftest.py`, after unit 12's `[dRB-12]` block, in
  the scope that defines `stale_target`. It builds a target with `make_target`, `DEPLOY_FULL` plus
  `[kit.agent-cap] prefix = "scripts"`, and runs `apply --kits agent-cap,settings-merge,kickoff-manifest`.
  It then asserts AC1's line, receipt and settings facts, each on the line it names. It asserts no
  exit code, because the exit belongs to agent-cap's argv (§8 F1). Its file reads name
  `encoding="utf-8"`, and its process calls go through `run`. Observed by AC1, through the `New arm:`
  line in §7.
- **S5** — Spec 11's §4 "Which receipt bytes" paragraph is corrected in place, in one rev bump whose
  revision line names `TOOL-dRedressedBar-14`. It states that in `apply` the term reads the receipt
  this run wrote ahead of CONFIGURE. That receipt holds this run's rows and the carried ones, and it
  is still the bytes the adopter read. `update` is unchanged. Observed by AC6.
- **S6** — The unit adds no module-level function or class. It adds no text-IO site without an
  encoding, and it moves no kit version. Observed by AC5.
- **S7** — Every reading below goes to this unit's acceptance ledger under
  `memory/builds/dRedressedBar/build/`, carrying `**Serves:** journal TOOL-dRedressedBar-14`.
  Observed by AC6.

## 3. Non-goals (OUT)

- No change to agent-cap's adopter argv, to any token grammar, or to `tools/hooks/kit.toml`
  (§8 F1).
- No change to `tools/settings-merge.py`, `tools/lib/resolve_kit_dir.py` or any inlined copy of the
  resolver. They already read the receipt, and the fix is to give them one.
- No change to `update`'s or `adopt`'s receipt writes (`:12017-12062`, `:12692`).
- No new step id. `STEPS` (`:94-95`) is the reserved vocabulary, and the S1 line is not a step.
- No move of HOOKPROBE relative to the receipt. The S1 write lands after it.
- No `provisional` field and no receipt schema move. `RECEIPT_SCHEMA` (`:49`) stays 3.
- No change to which kits the registry's default set holds (brief non-goal).
- No stderr-tail helper consolidation. That is the other external hand-off in spec 11 (brief
  non-goal).
- No `help/` page. `help/` holds `README.md` and `roles.md`, and neither covers govkit.

### Edges

- **consumes-from** `TOOL-dRedressedBar-11` — its `must_not_resolve` term, which reads the receipt
  that S1 now writes before classification. It also takes the `[dRB-11]` block's fixture A, whose
  refusal AC3 re-reads over the early write, and S3's stderr tail, which AC1's agent-cap line reads.
  Spec 11's §4 "Which receipt bytes" paragraph is what S5 corrects. Without it, nothing in the
  CONFIGURE outcome reads the receipt, and AC3 has no refusal to keep.
- **consumes-from** `TOOL-dRedressedBar-12` — `_carried_kits` and `_carried_rows`, which S1 binds
  ahead of CONFIGURE so both writes carry them. Without the carry, the early receipt holds only the
  selection's rows. Fixture A's planted `agent-cap` row then disappears during CONFIGURE, and the
  false accept unit 11 closed comes back. AC3 stages exactly that.
- **hands-off** `TOOL-dRedressedBar-15` — agent-cap's own adopter exit 2 at a per-kit prefix (§4,
  measured). Its argv `["python", "{prefix}/settings-merge.py"]` (`tools/hooks/kit.toml:108`)
  resolves `{prefix}` in agent-cap's context, while the file belongs to settings-merge. AC1 pins the
  exit 1 it leaves over this unit, and the reproduction's exit 0 is that unit's close (§8 F1).
- **hands-off** external — `update`'s gained loop runs a gained kit's adopter (`:11104-11126`) before
  its receipt write (`:12017-12062`). So a gained kit at a per-kit prefix is not in the receipt its
  sibling resolvers read. Not measured here.

## 4. Design

### The defect, measured

Measured on 2026-10-14 at `29c72f51`, whose `tools/` equals `ebce889c`'s
(`git diff --stat ebce889c7 HEAD -- tools skills` prints nothing). Two fresh `git init` targets were
used, `%TEMP%/drb14` and `%TEMP%/drb14d`, each with `DEPLOY_FULL`'s answers
(`tools/govkit/selftest.py:700-710`). `drb14` also had `[kit.agent-cap] prefix = "scripts"`.
Nothing in the tree was written.

| Step | Reading |
|---|---|
| 1. `drb14`: `apply --kits agent-cap,settings-merge,kickoff-manifest` | exit 1. `CONFIGURE settings-merge: adopter exit 2` and `CONFIGURE agent-cap: adopter exit 2`, two `unclassified` problems. The receipt claims `kickoff-manifest`, `settings-merge`, `agent-cap`, with 18 rows and three `orders`. One row is `scripts/hooks/agent-cap.js`, source `tools/hooks/agent-cap.js`. `.claude/settings.json` wires the three agent-cap fragments at `scripts/hooks/` and carries no `agent-cap.js` command |
| 2. In `drb14`, with the receipt moved aside: `python tools/settings-merge.py` | exit 2, `refusing to wire agent-cap — scripts/no-agent-cap-kit-resolved/agent-cap.js does not exist` |
| 3. The same, with the receipt back | exit 0, `wired agent-cap Workflow\|Agent hook`; settings.json gains `node "${CLAUDE_PROJECT_DIR}/scripts/hooks/agent-cap.js"` |
| 4. In `drb14`: `python scripts/settings-merge.py`, agent-cap's resolved argv | exit 2, `can't open file '…\scripts\settings-merge.py': [Errno 2] No such file or directory` |
| 5. Step 1's apply again, over the uncommitted target holding step 1's receipt | past the foreign and dirty refusals. `CONFIGURE settings-merge: adopter exit 0`, `CONFIGURE agent-cap: adopter exit 2`, exit 1 with one problem. settings.json carries one `scripts/hooks/agent-cap.js` command |
| 6. `drb14d`, no per-kit prefix, the same apply | exit 0. Both adopters `exit 0`; settings.json wires `tools/hooks/agent-cap.js` |

The brief's account holds for settings-merge only. Steps 2, 3 and 5 isolate its exit: the same
adopter, in the same target, differs only by whether a receipt is on disk. Agent-cap's exit is
python failing to open `scripts/settings-merge.py`. agent-cap's argv spells settings-merge's file
with `{prefix}`, and `target_context` resolves `{prefix}` from agent-cap's own `[kit.agent-cap]`
table (`:1452-1455`). settings-merge.py lands at its own prefix, `tools/`. It is the only argv that
names another entry's file. Of the 15 `[adopt].argv` declarations, 12 start in `{kit}`, and
playbook-render's and settings-merge's name their own homes. No receipt change reaches agent-cap's
exit (step 5).

At `<p13>` the settings-merge half reads differently, derived from specs 9, 10 and 11 and not
measured. The hook is at neither static home, and with no receipt `must_not_resolve` holds, so
settings-merge's exit 2 reads `no-agent-cap-to-wire [accepted stop]`. The hook then goes unwired
with no settings-merge problem.

### The receipt written ahead

| Key | Value at the S1 write | At RECEIPT |
|---|---|---|
| `schema`, `gov_source`, `gov_commit`, `prefix` | as `:8020-8021` computes them today | unchanged |
| `kits` | `selection + _carried_kits` | unchanged |
| `files` | `rows + _carried_rows`. Every landed row already carries the `oid` STAGE stamped (`:7638-7645`) | re-derived from `rows + _carried_rows`, after OBSERVE and the re-stamp mutated rows in place |
| `orders` | the prior receipt's `orders`, else `[]` | this run's `orders` |
| `baseline` | this run's `baseline` (BASELINE ran at `:7364-7391`) | unchanged |
| `after` | the prior receipt's `after`, else `{}` | `after_map` |
| `hook_block` | `{"state": hook_state}` | unchanged |
| `gate_runner` | the prior receipt's `gate_runner`, else this run's `kind` and `file` with `emitted: []` and `legs_withheld: False` | this run's, as `:8024-8025` builds it |

The three keys computed after CONFIGURE take what the target holds when the write lands. That is the
prior run's orders, verdicts and legs, or none on a first install. So the early receipt is a true
statement at any instant up to RECEIPT. Nothing is appended to `rows` after LAND. The only appends
are `:7616` and `:7621`. `files` is re-derived at RECEIPT anyway, so a later append cannot be
written to one file and lost from the other.

`receipt`, the in-memory prior receipt, is bound once at `:7251` and never rebound. The S1 write
changes no in-process reader. `foreign_kit_present`, `derive_unsatisfied_requires`,
`demand_writable_target`, the pins union, the `[[own]]` carry at `:7582` and `write_gate_legs`
(`:7953-7955`) all read it exactly as today. `_rcpt_doc` is unbound in `tools/govkit/govkit.py`
(`grep -c` reads 0). Unit 12's two locals read 0 at the base and are unit 12's to mint.

### When CONFIGURE fails

| How the run ends | What `.governance/install.json` claims | Does a re-run recover |
|---|---|---|
| An adopter exits non-zero, accepted or refused | RECEIPT overwrites the early write, so the receipt is the one written today. CONFIGURE only calls `r.fail` (`:7760-7772`) | as today |
| An exception or interrupt escapes `_cmd_apply` between the two writes | the early receipt: this run's selection and carried kits, every landed row with its STAGE `oid`, `gov_commit` this run's commit, and the prior run's `orders`, `after` and `gate_runner` | `apply` does. The kits are claimed, so `foreign_kit_present` passes. Each staged path matches its row's `oid`, so `demand_claimed_paths_clean` passes (`:7036-7106`, carve-out 3; step 5 above measured both). Every adopter then runs again. `update` does not, because it runs no adopter of a claimed kit (`:11100-11103`) |
| The same, at the base | a first apply leaves no receipt, and a re-apply leaves the prior one | a first apply's re-run is refused as foreign (`:7257-7263`); AC4's red half observes it |

`cmd_apply`'s `finally` releases the write lock on every one of these paths (`:7220-7231`).

### Every reader of the receipt during CONFIGURE

No reader assumes the receipt is absent. Each reads absence as zero rows, so the early receipt only
adds rows each one already reads on a later run.

| Reader | Site | With no receipt | With the early receipt |
|---|---|---|---|
| settings-merge's adopter, resolving agent-cap | `tools/settings-merge.py:77-111`, `:192` | static probes only | finds the hook at its per-kit prefix. This is the fix |
| lexicon's adopter, resolving codebase-map | `tools/lexicon/adopt-lexicon.sh:404` | static probes only | finds this run's codebase-map rows |
| unattended's adopter, resolving memory-tree | `tools/unattended/adopt-unattended.sh:328` | static probes only, then `check_tracked`, which a staged path passes | finds this run's memory-tree rows |
| memory-tree's adopter: `{{TOOL_ROOT}}` cites, `rendered_at` and the playbook engine | `tools/memory-tree/adopt-memory-tree.sh:277`, `:281-298`, `:317` | `rows = []` | sees this run's rows, as its next run does today |
| `resolve_owned_hook`, run by settings-merge `--fragment` from `run_fragment_merges` | `tools/settings-merge.py:356-360`; `govkit.py:7777-7780` | the path, unchanged | joins an `[[own]]` hook's `adopter-owned` row, which apply built at `:7577-7594`, on this same run |
| unit 11's `must_not_resolve` term in `classify_outcome` | `:7745`, unit 11 S1 | no rows | reads the bytes the adopter read |
| the target's runner at AFTER, its `receipt sync` leg | `tools/run-gates/check-receipt.py:60-71` | a skip | grades the early receipt's engine rows against the bytes this run landed |

### What an adopter sees change

| Situation | At `<p13>` | After |
|---|---|---|
| a first apply selecting agent-cap and settings-merge with `[kit.agent-cap] prefix = "scripts"` | settings-merge `exit 2 — no-agent-cap-to-wire [accepted stop]`, the hook unwired; agent-cap `exit 2`, refused; exit 1 | settings-merge `exit 0`, the hook wired at `scripts/hooks/agent-cap.js`; agent-cap `exit 2`, refused; exit 1 until §8 F1's work lands |
| the same apply at the default prefix | exit 0, both adopters `exit 0` | unchanged, plus the S1 line |
| unit 11's fixture A, the second apply | exit 1, `cannot read` | unchanged |
| an apply interrupted mid-CONFIGURE | no receipt, or the prior one | the early receipt; a re-run of `apply` recovers |
| any apply | no receipt on disk until the last step | one exists from just before CONFIGURE; RECEIPT rewrites it |

### Order, and unit 7

This unit follows unit 13 (order 9), so its order is 10. Units 12, 13 and 14 all write
`tools/govkit/govkit.py`, `tools/govkit/selftest.py` and spec 11. This unit also binds unit 12's
locals at a new site, and unit 13's S13 rewrites the CONFIGURE call that sits right below the S1
write. Unit 13 is a sequence and not an edge, because no criterion here rests on its work.

Unit 7's version measurement need not cover this unit. Both product files sit under
`{prefix}/govkit`, which the registry exempts as the deployer (`tools/govkit/registry.toml:295-297`),
so no kit version moves. S6 mints no function, so `memory/map/generated/symbols.json` stays as unit
7 regenerates it. The README changes this implies are the dispatcher's. Unit 14 needs a roster row,
and this header's `order 10` adds step 10 on regen. The Build-level rules sentence "Units 10 and 11
follow 7 in that order" should name 12, 13 and 14 too. Under §8 F1 (b), `tools/hooks/kit.toml`
would move agent-cap's version, which unit 7's measurement does not cover.

### Inventory

| Identifier | Kind | Naming cell |
|---|---|---|
| `_rcpt_doc` | a local in `_cmd_apply` | none: `lexicon.py --suggest _rcpt_doc --as py.local` answers that the closed set is function, type, file and constant |
| `[dRB-14]` | the check-label prefix of the new selftest block | none |

### Files touched (estimate)

- `tools/govkit/govkit.py`
- `tools/govkit/selftest.py`
- `memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-11.md`
- `memory/builds/dRedressedBar/build/`

### Alternatives rejected

Each candidate was written down with the test that could make it lose, and the pick is M3's.

| Candidate | The test that could make it lose | Verdict |
|---|---|---|
| C1 — write the receipt ahead of CONFIGURE, from RECEIPT's own lists, and rewrite it at RECEIPT | Settings-merge still exiting 2 with a receipt on disk, or a re-run refused over the early receipt. Steps 3 and 5 measured neither. Losing unit 11's fixture A refusal, which the carry prevents (AC3) | Chosen |
| C2 — run CONFIGURE after the receipt write | OBSERVE reads what the adopters rendered (`:7782-7816`), RENORMALIZE must follow CONFIGURE (`:7819-7821`), and `orders` is filled in CONFIGURE. So the receipt is written twice anyway, with CONFIGURE moved past three steps that consume it | Rejected; it reduces to C1 with a worse order |
| C3 — hand the adopters the planned homes through an environment variable | The resolver must read it, and `git grep -c '>>> resolve_kit_dir'` finds 67 files carrying the inlined copy, held byte-identical to `tools/lib/resolve_kit_dir.py`. Every shipped kit carrying one moves its version, and every resolver gains an input channel | Rejected |
| C4 — hand settings-merge the hook through an argument, `--hook-path`, or its `deploy.toml` fallback | settings-merge's argv has no token for agent-cap's prefix (`target_context`, `:1440-1460`). The fallback joins `NO_HOOKS_KIT` by ruling (`tools/settings-merge.py:197-223`, "never a guessed prefix"). The lexicon, unattended and memory-tree lookups above stay blind. And the term and the adopter would read different sources | Rejected; it closes the instance |
| C5 — the early bytes at another path, such as `install.pending.json` | No resolver reads that path, so it reduces to C3 | Rejected |
| C6 — the early receipt with only the keys known before CONFIGURE | An interrupt then leaves a schema-3 receipt missing three keys every final receipt carries, read by `check` and `update` | Rejected |
| C7 — the early receipt keyed on `rows` alone, without unit 12's carry | AC3's staged break: fixture A's planted row leaves the receipt during CONFIGURE, and the second apply reads `[accepted stop]` | Rejected |

## 5. Production-readiness checklist

- security — Widens nothing. The early bytes are the rows this verb already writes to the same
  path, after the hoisted containment pass (`:7354-7358`). `resolve_kit_dir` still applies its
  containment rule to each row it reads (`tools/settings-merge.py:103`). The adopters were already
  target-side code reading this file. They now read it one step earlier.
- perf / scale — N/A — one more JSON write of the receipt per apply.
- error / empty / loading states — §4 "When CONFIGURE fails". An apply with no prior receipt writes
  the empty values the table names.
- observability — The S1 line says the receipt is on disk ahead of CONFIGURE and that RECEIPT
  rewrites it. An operator reading output that stops after it knows which receipt they hold.
- risks — An arm reading a receipt's presence as proof the run reached RECEIPT is weakened. The one
  found is `[-6] AC5` (`tools/govkit/selftest.py:13722-13724`), and its exit-1 check at `:13716-13718`
  still tells a finding from a Refusal. Every arm asserting no receipt is a refusal before LAND:
  `:1275`, `:4287`, `:5020`, `:5036`, `:5050`, `:11864` and `:13376`. The `govkit selftest` leg grades
  the rest at the close.
- testing — AC1 to AC6 are scratch fixtures under `%TEMP%`, gov clones at `<p13>`, one staged fault
  in a scratch gov copy, and source greps. The new arm is declared in §7.
- migration — N/A — no receipt field, conf key or deploy shape moves.
- user docs — N/A — `help/` holds no govkit page. `grep -n -i 'configure' WIRE-INTO-PROJECT.md
  skills/deploy-governance/SKILL.md` finds no sentence that pairs CONFIGURE with the receipt.

## 6. Acceptance criteria

`<p13>` and `<p14>` are the commits of units 13 and 14's build passes, as their acceptance ledgers
name them. Every command runs from the worktree root. Fixtures live in fresh `git init` targets under
`%TEMP%/<short-name>`, never inside the worktree, with `core.autocrlf false` and
`.governance/deploy.toml` holding `DEPLOY_FULL`'s answers. Where a criterion adds
`[kit.agent-cap] prefix = "scripts"`, it is appended to that file. A red half at `<p13>` runs
`python <clone>/tools/govkit/govkit.py` from a local `git clone` of gov under `%TEMP%`, checked out
at `<p13>`.

- **AC1** — When `python tools/govkit/govkit.py apply --target <t> --kits agent-cap,settings-merge,kickoff-manifest`
  runs over a target with the per-kit prefix, exactly one line opens
  `govkit apply — CONFIGURE settings-merge:` and it ends `adopter exit 0`. The line opening
  `govkit apply — receipt written ahead of CONFIGURE` comes before the first line carrying
  `CONFIGURE `. The receipt holds a row with path `scripts/hooks/agent-cap.js` and source
  `tools/hooks/agent-cap.js`. Read as JSON, `.claude/settings.json`'s `PreToolUse` group with matcher
  `Workflow|Agent` holds exactly one command, and it carries `scripts/hooks/agent-cap.js`. No line
  opens `govkit: kit 'settings-merge'`. Under §8 F1 (a), the run exits 1, and exactly one line
  opens `govkit: kit 'agent-cap'` and carries `settings-merge.py`.
  Red when: at the base it prints `CONFIGURE settings-merge: adopter exit 2` and settings.json holds
  no `agent-cap.js` command (§4, step 1). Over the `<p13>` clone, the settings-merge line carries
  `no-agent-cap-to-wire [accepted stop]` and settings.json holds no `agent-cap.js` command.
  fixture: the base half was observed at spec time on `29c72f51`. The `<p13>` half is derived from
  specs 9 to 11, and the pass observes it first. A `<p13>` half that does not print the accepted stop
  is returned to the main loop and not counted.
  cost: two applies, about a minute with the clone.
- **AC2** — The same apply runs without the per-kit prefix, once at the tip and once from the `<p13>`
  clone, each into its own target. Both exit 0, and each prints two `CONFIGURE` lines ending
  `adopter exit 0`. The two `.claude/settings.json` files are byte-equal. With each output's
  `[3/LAND]` line dropped, `diff` of the two outputs prints exactly one added line, the one opening
  `govkit apply — receipt written ahead of CONFIGURE`.
  Red when: the early write changes what a default-prefix apply configures or prints beyond that line.
  fixture: the base reading is §4 step 6, observed at spec time on `29c72f51`.
- **AC3** — This is spec 11's AC3 fixture A, built as it states. Its second apply prints the S1
  line, exits 1, and has exactly one line opening `govkit: kit 'settings-merge'`, which carries
  `cannot read`. No line carries `no-agent-cap-to-wire`. Then make a scratch copy of gov at the tip
  whose S1 write takes `rows` and `selection` in place of the carried lists. Over that copy, the
  same second apply exits 0 and prints `[accepted stop]`.
  Red when: the early receipt drops a claimed kit's rows, as the staged copy shows.
  cost: two fixture builds, about two minutes.
- **AC4** — Make a scratch copy of gov at the tip with one added line,
  `raise RuntimeError("drb14 staged fault")`, after the line `inert = read_inert_kits(deploy)`
  (`:7670` at the base). Over a per-kit-prefix target, the copy's AC1 apply exits non-zero. It leaves
  `.governance/install.json` claiming `kickoff-manifest`, `settings-merge` and `agent-cap`. Every
  row whose role is `engine` carries an `oid`. Its `orders` is `[]`, where a completed run's receipt
  holds three (§4, step 1), so the file read is the early write. Then the tip's
  unpatched apply runs over the same uncommitted target. No line carries `already carries` or
  `DIRTY`, and exactly one line opens `govkit apply — CONFIGURE settings-merge:`.
  Red when: the same patch over the `<p13>` clone leaves no receipt, and the re-run exits 2 with
  `already carries`.
  fixture: the red half is derived from `foreign_kit_present` (`:6679`) and was not run at spec
  time. The pass observes it first.
  cost: two gov copies and three applies, about three minutes.
- **AC5** — `git diff <p13> <p14> -- tools/govkit/ | grep -E '^[+-](def|class) '` prints nothing.
  `grep -c '_rcpt_doc' tools/govkit/govkit.py` prints at least 3. The comment above the S1 write
  carries `per-kit` and `RECEIPT`. A python program imports `tools/gate-lint/encoding_posture.py`
  and runs `scan_text_io` over `tools/govkit/govkit.py` and `tools/govkit/selftest.py` at `<p14>`.
  Per arm, it counts exactly the rows `memory/project/encoding-posture-sites.txt` declares.
  Red when: the pass minted a function, or added an unencoded text-IO site.
  figure: DERIVED from the registry at observation, after unit 13 moves it.
- **AC6** — Cut spec 11's Design section with `sed -n '/^## 4. Design/,/^## 5/p'` and join it with
  `tr '\n' ' ' | tr -s ' '`. It carries `TOOL-dRedressedBar-14`. Its revision log holds one new line
  naming `TOOL-dRedressedBar-14`. The ledger S7 names exists and carries
  `**Serves:** journal TOOL-dRedressedBar-14`.
  Red when: spec 11's §4 names no unit 14, as at `29c72f51`.

## 7. Gates

`govkit selftest` · `govkit acceptance matrix` · `govkit refusal join` · `govkit selfcheck` · `receipt sync (installed files match the receipt)` · `encoding posture (text IO names its encoding)` · `spec tokens (a spec's own names resolve)` · `recall floor` · `recall floor arms` · `memory hygiene`

New arm: tools/govkit/selftest.py · covers AC1 · the `[dRB-14]` block over unit 13's pass `<p13>`, where settings-merge's line reads the accepted stop and settings.json holds no `agent-cap.js` command · none

AC3 is also re-read by the `[dRB-11]` block's fixture A arm, unchanged, which reds if the early
receipt drops the carried rows. The refusal join's floor does not move. S1 and S2 add one print and
no refusal branch. The main loop observes the new arm red, then green, at the close.

## 8. Open questions

- **F1** — Where does agent-cap's own exit 2 at a per-kit prefix go? The brief's acceptance says the
  reproduction exits 0, and §4 step 5 shows this mechanism cannot get there alone. agent-cap's
  argv names settings-merge's file with agent-cap's `{prefix}`. Fixing that is a change to a
  descriptor or to the token grammar, which is a second mechanism (M2).
  - (a) The main loop adds a unit for agent-cap's adopter argv (M2 ADD), ordered after this one. This
    spec stands as written, AC1 pins the residual exit 1, and the brief's exit-0 criterion moves to
    that unit's close.
  - (b) Fold the argv fix into this unit. It is two mechanisms in one spec, and it moves
    `tools/hooks/kit.toml` and agent-cap's version, which unit 7's measurement does not cover.
  - (c) Leave the argv as the external hand-off above, and close the build with the reproduction
    exiting 1.
  - Recommendation: (a). (b) breaks M2's one-mechanism rule. (c) leaves the brief's exit-0
    criterion unmet. (a) meets every criterion the brief states once both units land, and adding a
    unit is the main loop's act, not this spec's.
  RESOLVED (owner, 2026-10-14): (a). agent-cap's adopter argv is its own unit,
  `TOOL-dRedressedBar-15`, ordered after this one, which §3 Edges hand it to. This spec stands as
  written, AC1's pinned exit 1 stands, and the reproduction's exit 0 moves to unit 15's close.

## 9. Revision log

- rev-1 · 2026-10-14 · initial draft from `prompts/2026-10-14-prompt-TOOL-dRedressedBar-12-brief.md`,
  authored as `TOOL-dRedressedBar-14` because the units-10-11 spec audit's disposal took ids 12 and
  13. The defect was reproduced at `29c72f51` on two scratch targets, and its two causes were split
  by running each adopter by hand. Seven candidates were graded by M12, and the pick was taken by
  M3's rule. Agent-cap's argv went to §8 F1.
- rev-2 · 2026-10-14 · §3 · §8 · F1 is marked resolved by the owner as option (a). Edges replace the
  external hand-off for agent-cap's exit 2 with the hands-off to `TOOL-dRedressedBar-15`, the unit
  the owner added for it. No scope, design or criterion moves, and AC1's pinned exit 1 stands.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "write the install receipt before the adopters run so a
sibling kit at a per-kit prefix resolves on a first apply"` ranked `resolve_kit_dir` as a SEAM with
69 installs, below name-stem matches (`run`, `write`, `resolve`) that are not receipt writers. The
seam extended is the receipt write in `_cmd_apply` (`tools/govkit/govkit.py:8017-8030`), run once
more ahead of CONFIGURE from the same dict. That gives every installed copy of `resolve_kit_dir` the
input it was built to read, so no resolver changes. The lists come from unit 12's carry, the one
place this verb already reads the prior receipt's claims past its selection. The gotchas checklist
for the two product paths selected these classes:
- `a-new-local-collides-in-a-long-function`, which is why `_rcpt_doc` was grepped unbound.
- `verdict-printed-before-the-step-that-reverts-it`, which is why the S1 line says RECEIPT rewrites
  the file.
- `line-claim-matched-over-the-whole-output`, which is why AC1 and AC3 assert on the line they name.
- `two-answers-to-one-question`, which is why both writes serialize one dict.

The recall probe returned `TOOL-aFlaggedScaffold-4` (`memory/builds/aFlaggedScaffold/BACKLOG.md:8`).
It records an apply that died after configure and left "no receipt update — a half-applied install",
which is the state §4's interrupt row now leaves recoverable. It also returned `TOOL-aWalkedCorpus-8`
(`memory/DECISIONS.md:89`), which orders CONFIGURE by `requires`. That is why settings-merge's adopter
runs before agent-cap's, and why step 1 reads settings-merge's exit first. Spec 13's S13 rationale
(`spec/2026-10-14-spec-TOOL-dRedressedBar-13.md:250-251`) says CONFIGURE runs before the receipt is
written. After this unit that is true only of the final receipt, and its decode fix stands on its
own ground.

Recall terms used: `python tools/memory-recall/query.py "why does apply write the install receipt
only after configure, and what reads it during configure" --terms "receipt CONFIGURE adopter
install.json resolve_kit_dir per-kit prefix first apply provisional half-install sibling kit renamed
home"`
