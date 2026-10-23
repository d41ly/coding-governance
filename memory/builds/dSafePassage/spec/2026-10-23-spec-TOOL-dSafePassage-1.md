# TOOL-dSafePassage-1 — the upgrade-step kind: the step row, succession rows, their one reader, and frozen landed rows

**Status:** DEFERRED · rev-4 · 2026-10-23 · node d · Tier-2 · base 3708a705 · streams tooling · order 1 · advances TOOL-dSafePassage-14

**Carries:** cl-dClosedLoop-0018@ed08a364 whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dSafePassage-1-deviation-11.md](../build/2026-10-23-build-TOOL-dSafePassage-1-deviation-11.md) | deviation | — |
| [2026-10-23-prompt-TOOL-dSafePassage-1-2-spec-writer.md](../prompts/2026-10-23-prompt-TOOL-dSafePassage-1-2-spec-writer.md) | journal | — |
| [2026-10-23-prompt-TOOL-dSafePassage-1-deviation-after-fix.md](../prompts/2026-10-23-prompt-TOOL-dSafePassage-1-deviation-after-fix.md) | research | TOOL-dSafePassage-7 TOOL-dSafePassage-11 TOOL-dSafePassage-13 |
| [2026-10-23-prompt-TOOL-dSafePassage-1-owner-audit-cap.md](../prompts/2026-10-23-prompt-TOOL-dSafePassage-1-owner-audit-cap.md) | research | — |
| [2026-10-23-prompt-TOOL-dSafePassage-1-spec-brief.md](../prompts/2026-10-23-prompt-TOOL-dSafePassage-1-spec-brief.md) | research | TOOL-dSafePassage-2 TOOL-dSafePassage-3 TOOL-dSafePassage-4 TOOL-dSafePassage-5 TOOL-dSafePassage-6 TOOL-dSafePassage-7 TOOL-dSafePassage-8 TOOL-dSafePassage-9 TOOL-dSafePassage-10 TOOL-dSafePassage-11 TOOL-dSafePassage-12 TOOL-dSafePassage-13 |
| [2026-10-23-review-TOOL-dSafePassage-1-2-3-4-5-6-7-8-9-10-11-12-13-spec-audit-round1.md](../reviews/2026-10-23-review-TOOL-dSafePassage-1-2-3-4-5-6-7-8-9-10-11-12-13-spec-audit-round1.md) | spec-audit | TOOL-dSafePassage-3 TOOL-dSafePassage-2 TOOL-dSafePassage-4 TOOL-dSafePassage-7 TOOL-dSafePassage-11 TOOL-dSafePassage-12 TOOL-dSafePassage-8 TOOL-dSafePassage-6 TOOL-dSafePassage-9 TOOL-dSafePassage-10 TOOL-dSafePassage-13 TOOL-dSafePassage-5 |

<!-- /gen:spec-records -->

## 1. Goal

Give gov a declared upgrade-step kind: a kit descriptor's `[[upgrade]]` row and the registry's
`[[retired]]` succession row, one reader for both, `update` and `check` that carry a retired kit to
its successor instead of refusing the whole run, the first two steps (`.agent-cap.conf`'s
`FANOUT_CAP` into `runtime.agents-in-flight`, and `template-size-limits.txt`'s rows into
`budgets.*`), and a leg that keeps every landed step row frozen. It closes `gap-deploy-15` (a receipt
naming a retired kit refuses the whole update, and `check` reds on it) and `gap-deploy-16` (no
upgrade-step kind: a moved conf key is only reported).

## 2. Scope (IN)

- **S1** — The step row. Every registry entry's descriptor may carry `[[upgrade]]` rows, and
  `tools/govkit/steps.toml` carries rows of the same grammar for surfaces no descriptor owns
  (§4 Data model). Keys: `id`, `up`, `down`, `witness`, `surfaces`, `needs-target` and an optional
  `resume`. The introducing commit is DERIVED by the reader and never typed in the row (§8 F2).
  Observed by AC1, AC2 and AC3.
- **S2** — The succession row. `tools/govkit/registry.toml` gains `[[retired]]` rows: `id` (an entry
  id or a step id), `successor` (a live id of the same kind, or `none`) and `surfaces`, the commit
  that retires it derived like the introducing commit. Observed by AC2 and AC4.
  **Readers:** by name: `tools/govkit/govkit.py`, whose `load_registry` and `read_descriptors` load
  the registry whole and so read no table they do not name; this item adds the table and retires
  nothing · by value: NO VALUE READERS — no reader holds a value of the new table until S4.
- **S3** — The one reader, `tools/govkit/upgrade_steps.py`. `read_steps` and `read_retired` parse,
  validate and order every row at a revision or in the working tree; `govkit.py` calls them and
  parses no row itself. A CLI, `python tools/govkit/upgrade_steps.py list`, prints the ordered rows.
  Observed by AC1, AC2 and AC3.
- **S4** — `update` and `check` read succession through `resolve_claim`. A claimed kit that is no
  longer a registry entry and carries a `[[retired]]` row is carried to its successor, or released
  with its rows routed to the existing `withdrawn` arm when the successor is `none`, in place of the
  whole-run refusal at `tools/govkit/govkit.py:9235-9239` and the problem `check` appends at
  `tools/govkit/govkit.py:5677-5679`. A claimed id with no succession row still refuses.
  Observed by AC6, AC7, AC8 and AC9. The replaced refusal's text, "which is no longer a registry
  entry", is spelled once in the tree, by `git grep -n -F 'no longer a registry entry' -- tools skills`.
  **Readers:** by name: `tools/govkit/govkit.py`, at :9237, and no test asserts the text · by value:
  NO VALUE READERS — the refusal is a raise and a report line, and nothing compares, counts or
  derives from its text.
- **S5** — The translation window. Its population is the legacy-homes list dGroundRules derives
  (`cl-dClosedLoop-0013`), read through that list's reader and never retyped. A member's window
  closes when a landed step's `surfaces` names it, and `upgrade_steps.py list --window` prints each
  member `open` or `closed by <step id>`. Observed by AC16.
- **S6** — The step `agent-cap/fanout-cap-to-agents-in-flight`, an `[[upgrade]]` row in
  `tools/hooks/kit.toml` whose program is `tools/govkit/steps/fanout_cap.py`. Its up moves
  `.agent-cap.conf`'s `FANOUT_CAP` into `runtime.agents-in-flight` and retires the file, so the limit
  reads the same before the step and after it; its down restores both files byte-identical.
  Observed by AC10, AC11 and AC12. The file's by-name readers at the base are those
  `git grep -n -F '.agent-cap.conf' -- tools skills` prints, and `cl-dClosedLoop-0016` re-points
  the code readers among them.
  **Readers:** by name: `tools/hooks/agent-cap.js`, `tools/hooks/README.md`,
  `tools/workflows/README.md`, `tools/workflows/check-verifier-fanout.sh`,
  `tools/hooks/agent-cap.test.sh`, `tools/workflows/check-protocol-parity.test.sh` and
  `tools/workflows/check-verifier-fanout.test.sh`; dGroundRules re-points the code readers to the
  policy reader, and this unit re-words the README section on the file ·
  by value: `read_policy_key` reading `runtime.agents-in-flight`, which keeps reading the file as a
  legacy home while it exists (`cl-dClosedLoop-0016`).
- **S7** — The step `govkit/template-size-limits-to-budgets`, a row of `tools/govkit/steps.toml` whose
  program is `tools/govkit/steps/template_size_limits.py`. Its up moves every row of
  `<prefix>/template-size-limits.txt` into `budgets.*` in `.governance/policy.toml`, each row's
  comment block (its argued history) carried above its key and the file's header (the four raise
  conditions) carried above the table, and retires the file; its down restores both files
  byte-identical. Observed by AC13 and AC14. The file's by-name readers at the base are those
  `git grep -l -F 'template-size-limits' -- ':!memory/builds' ':!memory/ledger'` prints, the backlog
  index row aside, and S8 disposes each.
  **Readers:** by name: `tools/check-template-size.sh`, `tools/check-spec-tokens.py`,
  `tools/check-spec-tokens.test.sh`, `tools/govkit/registry.toml`, `.gitattributes`,
  `.memory-tree.conf`, `memory/project/method-carriers.txt`, `tools/line-length-limits.txt`,
  `tools/memory-recall/extract.py`, `tools/run-gates/gate-profiles.txt`,
  `memory/map/features/build-method.md` and `memory/map/features/playbook.md` · by value:
  `read_policy_key` reading every `budgets.*` cap, which reads the file as a legacy home until the
  step (`cl-dClosedLoop-0015`), and through it `tools/check-template-size.sh` and
  `tools/check-spec-tokens.py`'s size join.
- **S8** — Gov migrated first. This unit's pass runs S7's up on gov's own tree, so gov is the first
  tree the step migrates and `tools/template-size-limits.txt` leaves gov in the unit's commit. Every
  by-name reader S7 lists is disposed in the same commit: the `[[exempt]]` row and its three
  `why` mentions in `tools/govkit/registry.toml`, the `.gitattributes` eol row and the
  `RECALL_EXTRA_SOURCES` member in `.memory-tree.conf` are removed or re-pointed to
  `.governance/policy.toml`; the legacy-home branch the two size readers keep for the file is deleted,
  since gov's is the only tree that ever held it (it is an `[[exempt]]` path, shipped to no adopter);
  and each prose mention is re-worded to name `budgets.*`, the map dossiers' generated cards
  re-rendered by `python tools/codebase-map/gen_map.py --write`. Observed by AC13 and AC15.
  **Readers:** by name: the twelve readers S7 lists · by value: NO VALUE READERS beyond S7's — no
  reader compares or counts the file's path itself, only the caps it holds.
- **S9** — Frozen landed rows. `check_frozen` compares every `[[upgrade]]` and `[[retired]]` row
  present at a base on the default branch with the same id at the head: a removed row reds unless a
  `[[retired]]` row at the head names it; an edited `up`, `down`, `witness`, `resume` or `surfaces`
  reds; an edited byte of any program file a landed argv names reds; a correction shipped as a new
  step is green. It runs as a new leg, `step-rows-frozen`, whose argv is
  `python tools/govkit/upgrade_steps.py frozen`, with an `[[exempt_leg]]` row in
  `tools/govkit/registry.toml`. Observed by AC4, AC5 and AC17.
  **Readers:** by name: READER NOT IN TREE — the one reader of both tables is this unit's new
  module; this item retires no name, and the removal it grades is a planted one · by value: NO VALUE READERS — the leg
  reads the rows' values and nothing reads the leg's output but the runner's exit code.
- **S10** — The help page `help/upgrade-steps.md`, linked from `help/README.md`: what an upgrade step
  is, what `update` does with a kit that has a successor, and where `.agent-cap.conf`'s value now
  lives.
  Observed by AC18.

## 3. Non-goals (OUT)

- The walk: ordering is this unit's (S3), and running the rows between a receipt's vintage and its
  target, skipping a held witness, recording progress and reclaiming a dead holder's lock is
  `TOOL-dSafePassage-2`'s. Until it lands, S6 and S7 run only by their own argv.
- The receipt's `steps` field and the schema-4 step (`TOOL-dSafePassage-3`), down steps in reverse
  and the recorded rollback (`TOOL-dSafePassage-4`), the isolated runner and its `-I` contract
  (`TOOL-dSafePassage-7`), gov's source-mode receipt (`TOOL-dSafePassage-8`), the surface class
  registry and the step gate (`TOOL-dSafePassage-10`), the floor step (`TOOL-dSafePassage-11`) and
  the release-0 fixture (`TOOL-dSafePassage-5`).
- `plan` and `apply` given `--kits` naming a retired id: they still refuse an unknown id as today.
- `TOOL-dRetiredFork-38`'s scoped re-stamp (`update --write --kits <one>`), which this unit's
  succession handling neither fixes nor widens.
- Any legacy home other than the two S6 and S7 retire; dConvergedCharter folds the kit conf keys.
- The rows joining dWitnessedBar's append-only populations, which waits for that build's factory.

### Edges

- **consumes-from** external — dGroundRules, landed before the build run: `.governance/policy.toml`
  and its schema (`cl-dClosedLoop-0007`), `read_policy_key` (`cl-dClosedLoop-0008`), the legacy-homes
  list (`cl-dClosedLoop-0013`), `budgets.*` (`cl-dClosedLoop-0015`) and `runtime.agents-in-flight`
  (`cl-dClosedLoop-0016`). Without them S5, S6, S7 and S8 have no key to write and no reader to
  observe.
- **hands-off** `TOOL-dSafePassage-2` — walking the ordered rows this unit's reader returns, running
  each by its argv, and staging every path a step writes, its before-image included.
- **hands-off** `TOOL-dSafePassage-3` — the receipt step's row, placed first in the steps file this
  unit creates.
- **hands-off** `TOOL-dSafePassage-4` — walking the rows this unit's reader returns in reverse,
  running each applied row's `down` argv, and restoring from the before-image each up wrote.
- **hands-off** `TOOL-dSafePassage-7` — resolving an argv's interpreter and placeholders under the
  isolation contract.
- **hands-off** `TOOL-dSafePassage-8` — recording these two steps in gov's own receipt, where their
  witnesses already hold because this unit migrated gov first.
- **hands-off** `TOOL-dSafePassage-10` — the class registry that the member ids in a row's surfaces
  are spelled from.
- **hands-off** `TOOL-dSafePassage-11` — the floor step's row, placed second in the steps file.
- **hands-off** `TOOL-dSafePassage-5` — walking these two steps up, down and up again over the
  release-0 fixture.
- **hands-off** external — dWitnessedBar's append-only factory, which the frozen rows join when it
  lands.
- **hands-off** `TOOL-dSafePassage-17` — the per-row reverted rule and the no-image down this unit's grammar and restore helper gain, the repair of finding 51
- **hands-off** `TOOL-dSafePassage-20` — the one spelling of the unlanded value this unit's reader returns, recorded as null at the writer, the repair of finding 3
- **hands-off** `TOOL-dSafePassage-26` — the minors batch of the round-1 spec audit, which repairs the findings that land on this unit after every unit is built

## 4. Design

### Data model

One grammar for a step row, wherever it is declared.

| Key | Type | Rule |
|---|---|---|
| `id` | string | `<entry>/<slug>`, slug `[a-z0-9][a-z0-9.-]*`. In a descriptor, `<entry>` equals that descriptor's own `id`. In `tools/govkit/steps.toml`, `<entry>` names no registry entry (today `govkit` and `lib`). Unique over every declaring file. |
| `up`, `down`, `witness` | argv list | Non-empty strings. `argv[0]` is `python` or `bash`, which the runner resolves. The only placeholders are `{gov}` (gov's tool root, absolute), `{target}` (the target's checkout root, absolute) and `{prefix}` (the target's install prefix); any other `{...}` is refused. A token beginning `{gov}/` names a program, which must be a tracked file at the revision read. `witness` exits 0 when the step is applied. |
| `resume` | optional | `"atomic"` (the up leaves no partial state) or an argv list under the rules above. Absent means the up is re-runnable over its own partial state. The walk's use of it is `TOOL-dSafePassage-2`'s. |
| `surfaces` | list | Required, possibly empty, so an absence is declared. Each item is `<class>:<name>`, class `[a-z][a-z0-9-]*`. Class membership is the step gate's question, not this reader's (§8 F6). |
| `needs-target` | bool | Required. True when the step must run the target's own code. |

Any other key is refused, and so is an `introduced` key, naming the derivation (§8 F2).

A `[[retired]]` row in `tools/govkit/registry.toml` carries `id`, `successor` and `surfaces`. An
entry id retires to an entry id or `none`; a step id to a step id or `none`. A retired id that is
still a live entry or a declared step is refused, and so is a successor that is not live at the
revision read, and an authored `retired` key.

The introducing commit of a row, and the retiring commit of a succession row, is derived: the oldest
commit on the default branch's first-parent line (the remote ladder's `<remote>/<branch>`, else the
local branch) whose tree holds a row with that id. A row the default branch does not hold yet reads
`unlanded`. The derivation reads the declaring files' blobs commit by commit, oldest first, along
`git rev-list --first-parent --reverse <landed ref> -- <declaring files>`, and stops at the first
holding blob, so a branch commit merged in as a second parent never becomes a row's introducing
commit.

The order is total: landed rows by their introducing commit's first-parent position, then unlanded
rows; within one commit, `tools/govkit/steps.toml` first and then the descriptors in registry entry
order; within one file, row order. The steps file comes first because its rows are the receipt and
floor steps every later step's progress depends on (the brief's S5).

The two steps this unit ships:

```toml
# tools/hooks/kit.toml
[[upgrade]]
id = "agent-cap/fanout-cap-to-agents-in-flight"
up = ["python", "{gov}/govkit/steps/fanout_cap.py", "up", "{target}"]
down = ["python", "{gov}/govkit/steps/fanout_cap.py", "down", "{target}"]
witness = ["python", "{gov}/govkit/steps/fanout_cap.py", "witness", "{target}"]
surfaces = ["conf-key:.agent-cap.conf#FANOUT_CAP"]
needs-target = false

# tools/govkit/steps.toml
[[upgrade]]
id = "govkit/template-size-limits-to-budgets"
up = ["python", "{gov}/govkit/steps/template_size_limits.py", "up", "{target}", "{prefix}"]
down = ["python", "{gov}/govkit/steps/template_size_limits.py", "down", "{target}", "{prefix}"]
witness = ["python", "{gov}/govkit/steps/template_size_limits.py", "witness", "{target}", "{prefix}"]
surfaces = ["file:{prefix}/template-size-limits.txt"]
needs-target = false
```

**The before-image.** Each step's up first writes
`.governance/steps/<entry>/<slug>.before.json` at the target, holding every path it will write or
remove with that path's bytes (base64, or `null` for absent) and the sha256 its up will leave there
(`null` for removed). An existing before-image is kept, never overwritten, so a re-run over a killed
up computes from the first image and converges. The witness file change comes last. A down restores
each path from the image only where the current bytes are the image's after-hash or its before
bytes, refuses with exit 1 naming the path where they are neither (a later edit is never discarded
silently), and then removes the image. Both helpers live in `tools/govkit/upgrade_steps.py`, which
each step program imports by its own file's path, because the runner's `-I` drops the script
directory from `sys.path`.

**S6's up.** No `.agent-cap.conf`: exit 0. Otherwise it parses the file through the legacy-home
parser dGroundRules' reader uses for it (one parser, `cl-dClosedLoop-0016`) and refuses with exit 1,
writing nothing, on a malformed `FANOUT_CAP` or any assignment other than `FANOUT_CAP`. It reads the
key's own value through `read_policy_key`. Where `FANOUT_CAP` is lower, it sets
`runtime.agents-in-flight` to `FANOUT_CAP`; where it is not, the file lowers nothing and the key is
left as it is (§8 F10). It then removes the file. Its witness: `.agent-cap.conf` is absent.

**S7's up.** No `<prefix>/template-size-limits.txt`: exit 0. Otherwise it splits the file into its
header comment block and its rows, each row with the comment block above it, and checks each row's
value against the value `read_policy_key` reads for that cap, refusing with exit 1 on any
disagreement. It renders the `[budgets]` table into `.governance/policy.toml` with the header carried
above the table and each comment block above its key, verbatim, and removes the file. Its witness:
the file is absent and every cap reads the value its before-image row held.

**Writing the policy file.** Both steps write through the writer dGroundRules lands, where it lands
one; otherwise through `render_policy_text` in `tools/govkit/upgrade_steps.py`, a line editor that
sets one key in one table and refuses its own output unless `read_policy_key` reads the value back
(§8 F9).

### Inventory

| Minted | Where | Cell |
|---|---|---|
| `read_steps(root, rev, landed_ref)`, `read_retired(root, rev, landed_ref)`, `derive_introduced`, `resolve_claim(eid, entry_ids, retired)`, `check_frozen(root, base, head)`, `write_before_image`, `write_from_before_image`, `render_policy_text`, `main`, `cmd_list`, `cmd_frozen` | `tools/govkit/upgrade_steps.py` | `py.function` snake, verbs read, derive, resolve, check, write, render, main, cmd |
| `StepRow`, `RetiredRow` | `tools/govkit/upgrade_steps.py` | `py.type` pascal |
| `derive_push_base(root, base)`, extracted from `cmd_epoch` | `tools/govkit/govkit.py` | `py.function` snake |
| `cmd_up`, `cmd_down`, `cmd_witness`, `main` | `tools/govkit/steps/fanout_cap.py`, `tools/govkit/steps/template_size_limits.py` | `py.function` snake |
| the step ids `agent-cap/fanout-cap-to-agents-in-flight`, `govkit/template-size-limits-to-budgets` | the rows above | — |
| the leg `step-rows-frozen` | `tools/gate-legs.json`, chunk `declarations`, subject `repo`, no guard (it reads every descriptor, which live anywhere under the tool root), ceiling measured at build | — |

`Refusal` moves from `tools/govkit/govkit.py:115` into `tools/govkit/upgrade_steps.py`, and
`govkit.py` imports it back, so one exception class serves both modules and every existing catcher
of `govkit.Refusal` still resolves. Every new `raise Refusal` and `r.fail` site is an anchor of
`tools/govkit/refusal_join.py`, armed by a `tools/govkit/selftest.py` arm, and its `BRANCH_PIN` floor
moves by the count measured at both ends, as its own convention states.

`derive_push_base` is the base ladder `cmd_epoch` holds today (`tools/govkit/govkit.py:13446-13474`):
`--base`, else `GATE_PUSH_BASE`, else the merge-base with the remote ladder's default branch. Its
second instance is `cmd_frozen`, so it is extracted rather than copied (charter `[reuse]`).

### Migration

Additive for every adopter: a descriptor gaining a table no engine reads changes nothing until
`update` reads it, and `read_descriptors` (`tools/govkit/govkit.py:13238-13253`) loads a descriptor
whole, so the new table reaches no other reader. Gov's own tree is migrated in this unit's pass by S7's
up (S8), after the build run re-grounds against the landed dGroundRules.

### Rollout

The leg is live in the landing that adds it. Its first base has no step rows, so its first run reads
`0 landed row(s)` and says so; it grades a row from the landing after the one that introduces it.

### Files touched (estimate)

- `tools/govkit/upgrade_steps.py`
- `tools/govkit/steps.toml`
- `tools/govkit/steps/fanout_cap.py`
- `tools/govkit/steps/template_size_limits.py`
- `tools/govkit/govkit.py`
- `tools/govkit/registry.toml`
- `tools/govkit/selftest.py`
- `tools/govkit/refusal_join.py`
- `tools/hooks/kit.toml`
- `tools/hooks/README.md`
- `tools/gate-legs.json`
- `tools/template-size-limits.txt` (removed)
- `.governance/policy.toml`
- `.gitattributes`
- `.memory-tree.conf`
- `memory/project/method-carriers.txt`
- `tools/check-template-size.sh`
- `tools/check-spec-tokens.py`
- `tools/check-spec-tokens.test.sh`
- `tools/line-length-limits.txt`
- `tools/memory-recall/extract.py`
- `tools/run-gates/gate-profiles.txt`
- `memory/map/features/build-method.md`
- `memory/map/features/playbook.md`
- `help/upgrade-steps.md`
- `help/README.md`

### Alternatives rejected

- An authored `introduced` commit (§8 F2): a row cannot name the commit that lands it, because that
  commit's id hashes the row.
- The frozen check as an arm of `kit epoch (shipped bytes move, the version moves)`, or of the step
  gate (§8 F4).
- Before-images as comments inside `.governance/policy.toml` (§8 F5).

## 5. Production-readiness checklist

- security — the reader is the write boundary for step rows: deny by default on any unknown key,
  placeholder or interpreter, and on a program path that is not tracked. Steps run no target code
  (`needs-target = false`), and a down never overwrites bytes edited since its up.
- perf / scale — the introducing-commit derivation reads one blob per commit touching a declaring
  file, oldest first, stopping at the first hit; measured at build on gov's history.
- error / empty / loading states — an empty `[[retired]]` population and a base with no rows are
  announced with their counts, never read as coverage. A malformed row exits 2 naming the file, the
  row and the key.
- observability — `list` prints each row's order, id, introducing commit and file; `update` prints
  one line per succession it applies.
- risks — the minimal guard of `cl-dClosedLoop-0012` may refuse S8's write of gov's policy file
  (§8 F8). A shared helper edited under unchanged argv is not frozen (§7, what the leg does not check).
- testing — `tools/govkit/selftest.py` arms over scratch gov trees and targets, one per criterion.
- migration — §4 Migration.
- user docs — `help/upgrade-steps.md` (S10), and `tools/hooks/README.md`'s section on the file.

## 6. Acceptance criteria

- **AC1** — When `python tools/govkit/upgrade_steps.py list` runs on gov's tree after the build, it
  prints `govkit/template-size-limits-to-budgets` before `agent-cap/fanout-cap-to-agents-in-flight`,
  each with its declaring file and `unlanded` or its introducing commit.
  Red when: the reader skips descriptor rows, and the `tools/hooks/kit.toml` row is absent.
- **AC2** — When a scratch gov tree plants, one per run, an unknown key, an authored `introduced`, a
  `{bogus}` placeholder, `argv[0]` of `node`, a `{gov}/` program that is not tracked, a duplicate id,
  a descriptor row whose `<entry>` is another entry's, a `tools/govkit/steps.toml` row whose
  `<entry>` is a registry entry, a `surfaces` item with no `:`, and a `[[retired]]` row whose
  successor is not live, `upgrade_steps.py list` exits 2 naming that file, row and key.
  Red when: any planted case exits 0.
- **AC3** — When a scratch clone carries a row landed on `main` at commit X, and a branch adds a
  second row and merges `main` into itself, `upgrade_steps.py list` prints X for the first row and
  `unlanded` for the second; after `main` merges the branch at M, it prints M for the second.
  Red when: either row reads a commit off `main`'s first-parent line.
- **AC4** — When a branch of a scratch clone edits a landed row's `down` argv, then in a second run
  removes a landed row, then in a third edits one byte of a landed `{gov}/` program,
  `upgrade_steps.py frozen --base <main sha>` exits 1 each time, naming the id and the field or path;
  with the removal plus a `[[retired]]` row naming the removed id and its successor, it exits 0.
  Red when: a planted edit or a planted removal exits 0.
- **AC5** — When the branch instead adds a corrected step under a new id and leaves the landed row as
  it was, `upgrade_steps.py frozen --base <main sha>` exits 0; over a base holding no rows it exits 0
  printing `0 landed row(s)`.
  Red when: the new id reds, or the empty base prints no count.
- **AC6** — When a scratch gov tree's registry carries `[[retired]]` `old` with successor `new`, and
  a target's receipt claims `old`, `govkit.py update --target <t>` prints
  `retired old: claimed by its successor new` and no refusal; with `--write`, the receipt's `kits`
  holds `new` and not `old`.
  Red when: the run refuses with `no longer a registry entry`.
- **AC7** — When the successor is `none`, `govkit.py update --target <t> --write` names each of
  `old`'s rows `withdrawn` with an outbox order and deletes none of their files.
  Red when: the run refuses, or a file of `old` leaves the target.
- **AC8** — When the receipt claims an id that is neither a registry entry nor a `[[retired]]` id,
  `govkit.py update --target <t>` still refuses before writing.
  Red when: the run proceeds.
- **AC9** — When `govkit.py check --target <t>` runs on AC6's receipt, it prints
  `old: retired, successor new` and counts no problem for it; on AC8's receipt it still counts one.
  Red when: AC6's receipt prints probe A's `which is not a registry entry`.
- **AC10** — When a scratch target with dGroundRules' policy file at its defaults and a committed
  `.agent-cap.conf` of `FANOUT_CAP=2` runs S6's `up` argv and commits, `read_policy_key` reads
  `runtime.agents-in-flight` as 2 before and after, `.agent-cap.conf` is gone, the policy file holds
  `agents-in-flight = 2`, and S6's `witness` argv exits 0, where it exited 1 before.
  Red when: the value after the step reads the default of 6.
  fixture: needs dGroundRules' policy file and `read_policy_key` at the build run's base; the tree
  holds neither today.
- **AC11** — When S6's `down` argv runs after its up, `.agent-cap.conf` and `.governance/policy.toml`
  are byte-identical to the before state and `.governance/steps/agent-cap/` is gone; when it runs
  after an up killed once the before-image was written, it exits 0 and leaves the before state; when
  the policy file was edited after the up, it exits 1 naming the file and changes nothing.
  Red when: a byte differs after a down, or the edited file is overwritten.
- **AC12** — When `.agent-cap.conf` holds `FANOUT_CAP=abc`, or a second assignment `OTHER=1`, S6's up
  exits 1 naming the file and writes no byte, the before-image included.
  Red when: the up exits 0, or any file under the target changes.
- **AC13** — When S7's `up` argv runs on a scratch copy of gov's tree at the build run's base, every
  cap that `read_policy_key` reads for a row of `tools/template-size-limits.txt` reads the same value
  after the step as before, the file is gone, each row's comment block stands above its key in
  `.governance/policy.toml` (by `grep -n -F 'RAISED from 32768' .governance/policy.toml`), and the
  header's four raise conditions stand above the table.
  Red when: a planted row whose comment block contains a tab-separated line reads a different cap
  after the step.
  fixture: needs the landed `budgets.*` and its reader, as AC10.
- **AC14** — When S7's `down` argv runs after its up on that copy, `tools/template-size-limits.txt`
  and `.governance/policy.toml` are byte-identical to the base.
  Red when: a byte differs.
- **AC15** — When the unit is committed, `git ls-files tools/template-size-limits.txt` prints nothing,
  `git grep -l -F 'template-size-limits' -- ':!memory/builds' ':!memory/ledger' ':!memory/backlog'`
  prints nothing, and S7's `witness` argv exits 0 on gov's own tree.
  Red when: any of the twelve readers S7 lists still spells the name.
- **AC16** — When `python tools/govkit/upgrade_steps.py list --window` runs on gov's tree after the
  unit, it prints `.agent-cap.conf` and `template-size-limits.txt` closed by their step ids and every
  other legacy home `open`; with a step whose `surfaces` names a home the list does not hold, it
  exits 1 naming it.
  Red when: the unlisted home prints nothing and the run exits 0.
- **AC17** — When `tools/gate-legs.json` is read, a row named `step-rows-frozen` carries the argv
  `python {prefix}/govkit/upgrade_steps.py frozen`, and `tools/govkit/registry.toml` carries an
  `[[exempt_leg]]` row with that name.
  Red when: either row is missing, and `govkit selfcheck` would read the leg as unclaimed.
- **AC18** — When `help/README.md` is read, it links `help/upgrade-steps.md`, and that page names
  `[[upgrade]]`, `[[retired]]` and `runtime.agents-in-flight`.
  Red when: the page is missing or names none of the three.

## 7. Gates

`govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `recall floor arms` · `recall floor` · `agent-cap self-test` · `scratch-guard self-test` · `verifier fan-out self-test` · `review-join self-test` · `hook destinations self-test` · `run-gates canary` · `run-gates gov canary` · `measure-legs selftest` · `kit/dogfood doc parity` · `transition-audit arms` · `straggler-guard arms` · `memory-hygiene self-test` · `build-index selftest` · `govkit selfcheck` · `kit epoch (shipped bytes move, the version moves)` · `dead-path carriers (deleted files still named)` · `method carriers (every pointer declared)` · `template size <=48KiB` · `leg ceilings clear their evidenced maximum` · `every held leg is budgeted, every budget row resolves` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

The new leg `step-rows-frozen` is not on the line above, because the manifest does not hold it until
this unit builds it. It is observed red by AC4 and green by AC5.

New arm: tools/govkit/selftest.py · covers AC2 AC3 AC4 AC5 AC6 AC7 AC8 AC9 AC10 AC11 AC12 AC13 AC14 AC16 · each case staged by its own scratch gov tree or target, one planted row, receipt or file per arm · `tools/govkit/refusal_join.py` `BRANCH_PIN`, by the measured count

What the frozen leg does not check: a shared module a step program imports, edited under unchanged
argv; whether a correction step actually reverses the defect it corrects; and any row the default
branch has not landed.

## 8. Open questions

- **F1 — One mechanism per spec, or this clause in parts?** BUILD-METHOD M2 asks one mechanism per
  spec, and the clause holds a grammar, its reader, two steps and a frozen-row gate. (a) Carry it
  whole in this unit. (b) Carry it in parts across new units. The roster is the README's authored
  table, one unit per clause, and five writers run at once, so a new unit id minted here can collide
  with a sibling's; every part shares the one grammar the reader validates. Veto 1 does not
  discriminate, and (a) leaves fewer open questions. Recommendation (a), with the split left to the
  spec audit. Rung 3. RESOLVED (agent, 2026-10-23, delegated): (a).
- **F2 — Is the introducing commit typed in the row, or derived?** The clause lists it among the
  row's fields and the brief's S1 gives it a key, `introduced`. (a) Typed. (b) Derived by the reader
  from the default branch's first-parent history, and `retired` likewise. A row cannot name the
  commit that lands it, because that commit's id hashes the row, and any other typed commit is a
  second copy of a fact git owns (charter `[derive]`), which can disagree with it. (a) fails the
  clause's frozen comparison on the first row it carries. The reader still returns `introduced`, so
  the walk and the receipt keep the brief's spelling. Recommendation (b), a departure from the
  clause's row-field list recorded as
  `memory/builds/dSafePassage/build/2026-10-23-build-TOOL-dSafePassage-1-deviation-11.md`. Rung 3.
  RESOLVED (agent, 2026-10-23, delegated): (b).
- **F3 — What does a landed row freeze?** (a) Its id, introducing commit and argv, the clause's set.
  (b) Those, plus `surfaces`, the bytes of every `{gov}/` program its argv names, and every landed
  `[[retired]]` row. Under (a) an edited landed row's `surfaces` would cover a later landing's
  removal with no new step, an edited program would change what an unchanged down reverses (the
  shape audit's M31 consequence), and a removed succession row would bring probe A back. (b) meets
  every criterion (a) does and closes three follow-ups (a) leaves. `needs-target` stays mutable, so
  a step later found to need target code can be marked so. Recommendation (b). Rung 3.
  RESOLVED (agent, 2026-10-23, delegated): (b).
- **F4 — Where does the frozen check run?** (a) Its own leg, `step-rows-frozen`. (b) An arm of
  `kit epoch (shipped bytes move, the version moves)`. (c) An arm of `TOOL-dSafePassage-10`'s step
  gate. (c) depends on a unit sequenced after this one, which the ordering axis of M2 refuses. (b)
  grades a different mechanism, version bumps, and would make one leg's red mean two things. (a)
  reuses `cmd_epoch`'s base ladder through `derive_push_base`. Recommendation (a). Rung 3.
  RESOLVED (agent, 2026-10-23, delegated): (a).
- **F5 — Where does a step keep what its down restores?** (a) A JSON before-image under
  `.governance/steps/`. (b) Comments inside `.governance/policy.toml`. (c) No image: the down
  re-synthesises the files. A TOML comment cannot carry a byte-order mark or a lone CR, and
  `.agent-cap.conf` is read BOM-led and CRLF today (`tools/hooks/agent-cap.test.sh:1991`), so (b)
  and (c) fail `cl-dClosedLoop-0022`'s down byte-identical on such a file. (a) writes inside
  `.governance/`, the directory govkit already writes the receipt and its outbox into
  (`tools/govkit/govkit.py:9170` and `:7039`), so it adds no install location. Recommendation (a). Rung 3.
  RESOLVED (agent, 2026-10-23, delegated): (a).
- **F6 — How are surface member ids spelled before the class registry exists?** The class registry
  is `TOOL-dSafePassage-10`'s, sequenced after this unit. (a) This reader checks the
  `<class>:<name>` shape only, and these rows spell `conf-key:.agent-cap.conf#FANOUT_CAP` and
  `file:{prefix}/template-size-limits.txt`, the class tokens on the model of the packet's owned-node
  spelling `policy-key.<key>`. (b) The reader checks class membership too. (b) depends on a later
  unit. Recommendation (a); the M2 interface cross-read reconciles the two spellings with unit 10's
  registry before the first code pass. Rung 3. RESOLVED (agent, 2026-10-23, delegated): (a).
- **F7 — How are rows ordered across declaring files within one commit?** The brief's S5 orders by
  introducing commit, then by row order, which leaves files unordered. (a) The steps file first, then
  descriptors in registry entry order. (b) Descriptors first. Under (b) a descriptor step landing
  with the receipt step would run before the `steps` field exists, against S5's first step.
  Recommendation (a). Rung 1, the brief's S5. RESOLVED (agent, 2026-10-23, delegated): (a).
- **F8 — Who moves gov's own caps, given the minimal guard?** `cl-dClosedLoop-0012`'s minimal guard
  refuses every agent write to the policy file but a single cap raise, and S8 writes every
  `budgets.*` row in one step. (a) This unit's pass runs S7 on gov, every cap reading unchanged
  through the reader. (b) `TOOL-dSafePassage-8`'s lander runs it in the prepared merge. (c) Gov keeps
  the file until an attended run moves it. (c) fails `TOOL-dSafePassage-8`'s red on a step whose
  witness does not hold on gov, and leaves gov's `[[exempt]]` row naming a file the step removes.
  (b) leaves the tree between the unit's commit and the landing with a registry row and a file that
  disagree. (a) survives veto 1, and if the landed guard refuses a value-preserving step write it
  fails only veto 3. Recommendation (a), rung 5, "Standing ruling takes it (Recommended)" (ER:388):
  the one step-write shape whose every `budgets.*` value reads unchanged through the reader is asked
  of dGroundRules as `TOOL-dGroundRules-13` in `memory/builds/dGroundRules/BACKLOG.md`, since this
  run reaches another build only through an ask row, and the build run re-grounds against the guard
  dGroundRules lands before S7 writes gov's policy file.
  RESOLVED (agent, 2026-10-23, delegated): (a) · widens: the minimal guard's admitted agent-write
  shapes, by one value-preserving step write of the policy file, only where the landed guard refuses
  it · relaxes: none.
- **F9 — What does this unit do while its parent is unbuilt?** dGroundRules has no spec yet, and its
  clauses are this unit's contract: `cl-dClosedLoop-0007` (the policy file), `cl-dClosedLoop-0008`
  (`read_policy_key`), `cl-dClosedLoop-0013` (the legacy-homes list), `cl-dClosedLoop-0015`
  (`budgets.*`) and `cl-dClosedLoop-0016` (`runtime.agents-in-flight`). (a) The build run re-grounds
  against the landed parent before its first pass, takes the landed module paths, table layout,
  writer and legacy-home parser as spelled there, and bumps this spec's rev with a §9 line where any
  differs from §4. (b) Fix the parent's names here. (b) invents names those clauses own, which the
  brief forbids. Recommendation (a). Rung 1, the brief's parent rule. RESOLVED (agent, 2026-10-23,
  delegated): (a).
- **F10 — When `FANOUT_CAP` does not lower the key, does the step write the key?** (a) No: the file
  lowered nothing, so it is retired and the policy file is left byte-identical. (b) Write the key's
  current value explicitly. (b) adds a second statement of a default the catalogue already holds
  (charter `[one-fact]`), and a diff that changes no value. Both meet AC10. Recommendation (a).
  Rung 3. RESOLVED (agent, 2026-10-23, delegated): (a).
- **F11 — What happens to a retired kit's rows when its successor is `none`?** (a) They route to the
  existing `withdrawn` arm: a report and an outbox order, deleted only under `--write-withdrawals`.
  (b) The run refuses, as today. (b) keeps `gap-deploy-15` open. (a) reuses the arm
  `tools/govkit/govkit.py:10741-10778` already holds, whose rename path degrades a row naming an
  unknown kit to `withdrawn` (`tools/govkit/govkit.py:9610-9621`). Recommendation (a). Rung 3.
  RESOLVED (agent, 2026-10-23, delegated): (a).

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft, from the spec brief
  `memory/builds/dSafePassage/prompts/2026-10-23-prompt-TOOL-dSafePassage-1-spec-brief.md` and the
  packet's Items 1.
- rev-2 · 2026-10-23 · §8 F8 cites the ask `TOOL-dGroundRules-13` in place of the withdrawn
  deviation-12, whose clause is dGroundRules', and says the build run re-grounds against the guard
  dGroundRules lands, from
  `memory/builds/dSafePassage/prompts/2026-10-23-prompt-TOOL-dSafePassage-1-deviation-after-fix.md`.
- rev-3 · 2026-10-23 · §3 · the Edges gain the ends this unit owes the promotions of the round-1 spec audit's findings, written by the disposal stage: `TOOL-dSafePassage-17`, `TOOL-dSafePassage-20`, `TOOL-dSafePassage-26`; no other section moved.
- rev-4 · 2026-10-23 · §3 · the Edges gain the hands-off `TOOL-dSafePassage-4` that unit's
  consumes-from already declared, so the reciprocity join of hygiene check 12 holds; no other
  section moved.

## 10. Reuse audit

The seams extended, found with `python tools/codebase-map/reuse_lookup.py "declare a versioned
upgrade step in a kit descriptor and read it at a commit"`: `read_descriptors`
(`tools/govkit/govkit.py:13238`), which loads each descriptor whole and so reaches the new table
with no new loader; `load_registry` (`tools/govkit/govkit.py:247`) for the `[[retired]]` table;
`cmd_epoch`'s base ladder (`tools/govkit/govkit.py:13446-13474`), extracted as `derive_push_base` at
its second instance; `resolve_remote` (`tools/govkit/govkit.py:558`) for the default branch; the
`withdrawn` arm (`tools/govkit/govkit.py:10741-10778`) for a successor of `none`; and govkit's
`Refusal` with the refusal join's anchors. The lookup also ranked `read_blobs_at`
(`tools/memory-tree/tree_lib.py`), which belongs to another kit, and govkit imports no other kit's
module, so the blob read stays a small `git cat-file` reader in the new module. Where a hit
disagreed with source: the research record's line numbers for `_cmd_update` are from an older
`govkit.py` (the claim refusal it puts at :8855-8861 is :9235-9239 at the base, and `check`'s at
:5677-5679), and its probe A text is `check`'s, not `update`'s. The recall probe added
`TOOL-aFlaggedScaffold-3` (update has no arm for a source gov started shipping), which bounds what a
successor's new files get on the first update and is not widened here, and `TOOL-dRetiredFork-38`,
named in §3.

Recall terms used: `python tools/memory-recall/query.py "how does govkit update handle a retired
kit, an upgrade step, or a moved conf key" --terms "govkit update receipt registry entry retired
successor descriptor upgrade step withdrawn migration conf"`
