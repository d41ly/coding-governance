# TOOL-aRoutedQuill-5 — a default govkit install ships the write gate wired and its product paths armed

**Status:** CLOSED · rev-5 · 2026-10-10 · node a · Tier-2 · base 6473ae38 · streams tooling+deployer · order 5 · ratified 2026-10-09

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-09-build-TOOL-aRoutedQuill-5-1-acceptance-ledger.md](../build/2026-10-09-build-TOOL-aRoutedQuill-5-1-acceptance-ledger.md) | journal | — |
| [2026-10-09-prompt-TOOL-aRoutedQuill-1-0-run-handoff.md](../prompts/2026-10-09-prompt-TOOL-aRoutedQuill-1-0-run-handoff.md) | journal | TOOL-aRoutedQuill-1 KICK-aRoutedQuill-1 TOOL-aRoutedQuill-2 TOOL-aRoutedQuill-3 TOOL-aRoutedQuill-4 PLAY-aRoutedQuill-1 TOOL-aRoutedQuill-6 TOOL-aRoutedQuill-7 |
| [2026-10-09-prompt-TOOL-aRoutedQuill-5-build-brief.md](../prompts/2026-10-09-prompt-TOOL-aRoutedQuill-5-build-brief.md) | journal | — |
| [2026-10-10-review-TOOL-aRoutedQuill-1-closing-diff-round1.md](../reviews/2026-10-10-review-TOOL-aRoutedQuill-1-closing-diff-round1.md) | diff-review | TOOL-aRoutedQuill-1 KICK-aRoutedQuill-1 TOOL-aRoutedQuill-2 TOOL-aRoutedQuill-3 TOOL-aRoutedQuill-4 PLAY-aRoutedQuill-1 TOOL-aRoutedQuill-7 |

<!-- /gen:spec-records -->

## 1. Goal

The write gate and the ownership leg bind only where they are installed, wired and armed, and today
the hooks kit that carries the gate is opt-in and a default install lands its fragments unwired.
This unit makes a default `govkit` install, and an `update` of an existing adopter, ship the gate
wired, the card writer wired and `ROUTED_PATHS` scaffolded from a candidate the adopter confirms. It
makes `check-wiring.sh` report an install that is unwired or unarmed, and states it in the runbook.

## 2. Scope (IN)

- **S1** — `tools/govkit/registry.toml`'s `default` set gains `agent-cap`, `settings-merge` and
  `check-wiring`. The `agent-cap` entry ships `scratch-guard.js` and its fragments, and it ships
  `agent-cap.js` too, whose PreToolUse `Workflow|Agent` entry its adopter wires: every default
  adopter gains the fan-out cap with the gate. `settings-merge` is the entry's declared requirement,
  and `check-wiring` is the reporter owner decision D7 relies on. `check-agent-cap-restatement`, a
  conditional entry requiring `agent-cap`, drops its conditional mark so `--all` reaches it: selfcheck
  7e reds a dependent of the default set that no declared selection reaches, and the precedent fix
  for that state left a prose check out of the default set. Observed by AC1.
- **S2** — The `agent-cap` entry's `requires` gains `kickoff-manifest`, so the gate is never installed
  without the card writer whose `## route` it reads. Observed by AC2.
- **S3** — With `settings-merge` in every default selection, `run_fragment_merges` wires every
  fragment a default install lands: the gate's, the subagent context's, both card fragments and
  check-wiring's SessionStart entry. A landed fragment whose hook file the target does not hold, as
  memory-recall's when its opt-in hook was declined, is reported `not wired — <hook> is not
  installed here` and is not handed to `settings-merge.py`. Observed by AC3.
- **S4** — `derive_default_gained` in `tools/govkit/govkit.py` names the entries the registry's
  `default` holds at the target vintage and did not hold at the receipt's `gov_commit`, less those
  the receipt claims. `update --write` installs them as `apply --kits` would, prints one
  `default-gained` line each and, where the target's `deploy.toml` declares `kits`, appends them
  there; a read-only `update` prints them as `would gain`. The run whose writes add `settings-merge`
  to a receipt wires every fragment the receipt claims; later runs wire only what they land, so a
  deliberate unwire stays unwired. Observed by AC4.
- **S5** — `write_routed_keys` in `tools/memory-tree/adopt-memory-tree.sh` appends
  `ROUTED_PATHS="<candidate>"` and `ROUTED_COMMIT_CUTOFF="<today>"` to `.memory-tree.conf` when
  neither key is assigned, and writes nothing when either is. `derive_routed_candidate` is the
  tracked top-level directories, each with a trailing `/`, less dot-directories and the directory
  holding `MEMORY_ROOT`. `--scaffold` calls it on the conf it has just created from the example and
  names both keys in its seed-and-stop message. Observed by AC5.
- **S6** — A new mode, `--arm-routing`, calls `write_routed_keys` on an existing conf and prints the
  candidate. The memory-tree descriptor declares it as a `[[regenerate]]` block writing
  `.memory-tree.conf`, so `govkit update` runs it, and adds `ROUTED_PATHS` to `optional_keys`; the
  example documents both keys as comments. Observed by AC6.
- **S7** — `check_routed` in `tools/check-wiring.sh` reports `UNWIRED  routed` when a scratch-guard
  fragment is wired and the repository has no `.memory-tree.conf`, and when `ROUTED_PATHS` or
  `ROUTED_COMMIT_CUTOFF` is blank or absent or an entry is absolute, climbs through `..`, covers
  `MEMORY_ROOT` or names nothing tracked. The remedy names `adopt-memory-tree.sh --arm-routing`.
  With no hooks kit and no conf it skips. Observed by AC7.
- **S8** — `check_scratch_guard` grades every `*.fragment.json` the hooks kit ships rather than one,
  each against its own event: `matchers_of` and `wired` take the fragment's `event` and read only
  that event's groups. Observed by AC8.
- **S9** — `check_skill_install` reports `UNWIRED  skill` when a scratch-guard fragment is wired
  here and the machine has no `/session-kickoff` install, because the gate's refusal names that
  skill as its remedy. Its two skips stand everywhere else. Observed by AC9.
- **S10** — `--check` exits 1 on any S7 to S9 line and `--session` prints the same lines and exits
  0, as both modes already do. NOT OBSERVED by a criterion of its own: AC7 observes both modes on
  one arm, and the exit rule is `tools/check-wiring.sh:1428-1429`, unchanged.
- **S11** — `WIRE-INTO-PROJECT.md`: §1 says a gated repository needs the machine skill; §3 names
  both keys and the scaffold; §5's concurrency-guard paragraph says the hooks kit arrives by default
  and lists every hook a default install wires with its event and matcher; the Result list gains
  them. Observed by AC10.
- **S12** — No unattended DoD item, no `CORE_FLOOR` move and no asks. An unattended run's preflight
  already runs `check-wiring.sh --check` as its `WIRING_CHECK`, so S7 to S9 reach it through an
  existing term. NOT OBSERVED: the unit adds nothing to the unattended kit, which its diff shows.

## 3. Non-goals (OUT)

- The gate, its fragments, gov's own `.claude/settings.json` and gov's `ROUTED_PATHS` value. Those
  are `TOOL-aRoutedQuill-2` and `TOOL-aRoutedQuill-4`, and gov is wired by their commits.
- The ownership leg and its cutoff semantics. That is `TOOL-aRoutedQuill-3`; this unit only writes
  the key.
- Installing `/session-kickoff` on a machine. A machine-scoped link stays an order `apply` prints;
  §8 F4 keeps it so.
- Re-wiring a fragment an adopter unwired. Owner decision D7 keeps unwiring possible; check-wiring
  reports it.
- Runbook anchors for the three entries joining the default set, which would move the runbook
  parity pin. A follow-up.
- Pre-dropping a vendored kit prefix from the candidate. §8 F3.

### Edges

- **consumes-from** `TOOL-aRoutedQuill-2` — the widened `scratch-guard.fragment.json`, the
  `ROUTED_PATHS` grammar and its UNARMED rule. Without them there is no gate to install or arm.
- **consumes-from** `TOOL-aRoutedQuill-3` — the ownership leg and `ROUTED_COMMIT_CUTOFF`, which the
  scaffold writes beside `ROUTED_PATHS`.
- **consumes-from** `TOOL-aRoutedQuill-4` — `scratch-guard-subagent.fragment.json`, which the
  install wires and S8's arm grades on its own event.
- **hands-off** `TOOL-aRoutedQuill-6` — a default install that wires the gate and scaffolds
  `ROUTED_PATHS`, which the trial's routed cell runs against.

## 4. Design

### Evidence

Read at `6473ae38` on 2026-10-09.

- The default set is `tools/govkit/registry.toml:38-46`. `agent-cap` requires `settings-merge`
  (`tools/hooks/kit.toml:7`), and `apply` refuses a selection with an unsatisfied requirement
  (`derive_unsatisfied_requires`, `tools/govkit/govkit.py:876-899`); a requirement orders and never
  pulls a kit in (`:837-873`). A target's own `deploy.toml` `kits` list outranks the default
  (`:977-991`).
- `run_fragment_merges` (`govkit.py:5563-5622`, from `TOOL-aRepatriatedFork-11` S3) wires only
  fragments landed this run (`:5579-5581`), and only through the target's own `settings-merge.py`;
  without one it prints `landed UNWIRED` (`:5584-5595`).
- `settings-merge.py` with no fragment wires the built-in `Workflow|Agent` entry for `agent-cap.js`
  (`tools/settings-merge.py:7-13`), which is the `agent-cap` entry's adopter. It refuses to wire a
  hook file that does not exist (`:1040-1052`).
- `recall-opened.fragment.json` ships under memory-recall's `**` rule while `recall-opened.js` ships
  only to a target that opts in (`tools/memory-recall/kit.toml:10-11`, `:50-58`). With
  `settings-merge` present, every default install that did not opt in would print a REFUSED line.
- `update` moves only the kits a receipt claims (`govkit.py:8447-8453`) and prints the rest as
  `available (not installed)`, naming widening an owner decision (`:9192-9197`). The receipt's
  vintage is `gov_commit` (`:8389`), and `blob_at` (`:6118`) reads a file at a gov commit.
- `adopt-memory-tree.sh` copies the example into a missing conf and stops (`:60-65`), an accepted
  outcome (`tools/memory-tree/kit.toml:131-139`). `--render` seeds no conf (`kit.toml:115-118`).
  The descriptor declares `--render` twice (`:128-129`, `:212-213`).
- `check-wiring.sh --session` always exits 0 (`:1428`). Its scratch arm reads one fragment
  (`:687-739`). `matchers_of` flattens every event (`:328-346`), which `TOOL-aRoutedQuill-4`'s
  evidence notes. Its skill arm skips when the machine install is absent (`:1217-1219`) and when
  the kickoff kit is not tracked in this repository (`:1226-1228`), which is every adopter. The
  straggler arm reads the conf by sourcing it in a subshell (`:1349`).
- `WIRE-INTO-PROJECT.md` installs the skill per machine (`:59-74`), wires SessionStart fragments
  through the merger and says `apply` does it (`:737-765`), calls the concurrency guard recommended
  (`:791`), and lists what a project ends with (`:1156-1177`).
- `.unattended.conf:117` declares `WIRING_CHECK="bash tools/check-wiring.sh --check"`.
- Measured 2026-10-09, PINNED: S5's candidate rule, run as a `git ls-files` pipeline over gov's
  tracked tree, yields `skills/ tools/`, since seven top-level directories are tracked and five
  begin with a dot or are `memory`. Gov's declared value adds its two root product files.

### Data model

```sh
# .memory-tree.conf, as write_routed_keys appends it
# ROUTED_PATHS — product paths a write gate and the ownership leg guard. Derived at adoption from
# the tracked top-level directories; confirm or edit before you commit. Blank refuses every write.
ROUTED_PATHS="<candidate>"
# ROUTED_COMMIT_CUTOFF — commits committed before this date are not graded by the ownership leg.
ROUTED_COMMIT_CUTOFF="<today, as an ISO date>"
```

The adopter confirms by reading the value in the seed-and-stop message or the staged update, editing
it if needed, and committing. Neither key is overwritten once assigned, a blank assignment
included, so a deliberate blank stays a visible refusal.

### The hooks a default install wires

| Entry | Hook | Event | Matcher |
|---|---|---|---|
| `agent-cap` | `agent-cap.js` | PreToolUse | `Workflow|Agent` |
| `agent-cap` | `scratch-guard.js` | PreToolUse | `Bash|PowerShell|Edit|Write|MultiEdit|NotebookEdit` |
| `agent-cap` | `scratch-guard.js` | SubagentStart | `*` |
| `kickoff-manifest` | `manifest-check.sh --card --write` | SessionStart | `startup|clear` |
| `kickoff-manifest` | `manifest-check.sh --card --replay` | SessionStart | `resume|compact` |
| `check-wiring` | `check-wiring.sh --session` | SessionStart | `startup|resume|clear` |

### Inventory

| Identifier | Kind | Cell |
|---|---|---|
| `derive_default_gained` | function | `py.function`; `lexicon.py --suggest` answered OK |
| `add_deploy_kits` | function | `py.function`; answered OK |
| `check_routed` | function | `sh.function`; answered OK |
| `derive_routed_candidate` | function | `sh.function`; answered OK |
| `write_routed_keys` | function | `sh.function`; answered OK |
| `--arm-routing` | adopter mode | none: modes carry no naming cell |
| `default-gained` | `update` output field | none |

`check_scratch_guard`, `matchers_of` and `wired` keep their names and widen.

### Files touched (estimate)

`tools/govkit/registry.toml` · `tools/govkit/entries/check-agent-cap-restatement.kit.toml` · `tools/govkit/govkit.py` · `tools/govkit/selftest.py` · `tools/govkit/matrix.py` · `tools/hooks/kit.toml` · `tools/memory-tree/kit.toml` · `tools/memory-tree/adopt-memory-tree.sh` · `tools/memory-tree/.memory-tree.conf.example` · `tools/memory-tree/README.md` · `tools/memory-tree/check-memory-hygiene.test.sh` · `tools/check-wiring.sh` · `tools/check-wiring.test.sh` · `WIRE-INTO-PROJECT.md` · `memory/map/generated/symbols.json`

### Rollout

Lands at order 5, after units 2, 3 and 4. Gov itself is already wired and armed by then, so this
unit changes what adopters receive and nothing in gov's own session. This unit's moves of the
agent-cap, memory-tree and check-wiring kits leave each kit's version owed; this unit's own commits
bump none. The owed versions are minted once, after the build's last unit, as units 1, 2 and 4 also
state: by the lander, or by the run's own mint commit before the close, which names the build's last
built unit. `govkit.py selfcheck` runs after that mint because a version marker can sit outside the
files the mint edited. An adopter's next
`govkit update --write` installs the three entries, wires every fragment, appends the two keys and
leaves all of it staged for the adopter to read before committing.

### Alternatives rejected

- **govkit writing `.claude/settings.json` itself.** `settings-merge.py` is already the one writer
  of that file and the one `run_fragment_merges` calls; a second writer would be two answers to how
  a fragment is merged, re-matched and unwired. Joining the default set costs one small file.
- **A `[[hole]]` for the two keys.** The ownership leg already refuses an unarmed tree by name and
  check-wiring reports it; a hole would be a third red for one state.
- **Seeding the candidate into the example.** The example is gov's bytes; a candidate is a fact
  about the target tree and can only be derived there.
- **Making `--session` exit non-zero.** It runs as a SessionStart hook, where a non-zero exit is not
  a refusal; the UNWIRED line reaching the session is the report.
- **`requires = ["settings-merge"]` on kickoff-manifest.** The gate's own entry requiring the card
  writer covers the case that matters; a target taking the card alone loses nothing by an unwired
  card.

## 5. Production-readiness checklist

- security — A default install now arms two PreToolUse guards and three SessionStart entries in
  every adopter's settings. `settings-merge.py` refuses to wire a missing hook, so no entry
  dispatches against nothing. `--arm-routing` appends to an authored conf and rewrites no line.
- perf / scale — Each adopter session start runs the card writer and the wiring check. The wiring
  check was measured at 35 to 81 s per compaction before its matcher dropped compaction
  (`WIRE-INTO-PROJECT.md:744`); its start cost is UNVERIFIED in an adopter. Each Edit or Write
  pays one node spawn, `TOOL-aRoutedQuill-2`'s cost.
- error / empty / loading states — A repository with no tracked directory gets a blank candidate,
  which the leg and check-wiring refuse by name. An `update` whose regenerate step fails rolls the
  conf back with the kit.
- observability — `default-gained` and `would gain` lines on update; one line per fragment,
  `wired`, `already wired`, `not wired` or REFUSED; check-wiring's `ok` or `UNWIRED` per arm.
- risks — Adopters' Agent fan-outs past the cap are denied from their next update, a behaviour
  change D2 carries with the hooks kit. Every product write in an adopter is refused until a unit is
  specced, the intended change, arriving with the update. The acceptance matrix's default-shape
  expectations move, and govkit's held self-test is long.
- testing — Arms in `tools/govkit/selftest.py` and `tools/govkit/matrix.py`, in
  `tools/check-wiring.test.sh`, and in the hygiene self-test's scaffold fixture.
- migration — `govkit update --write` is the migration: S4 installs and wires, S6 arms.
- user docs — `WIRE-INTO-PROJECT.md` (S11) and the memory-tree README's Configure list.

## 6. Acceptance criteria

- **AC1** — When `python tools/govkit/govkit.py plan` runs against a scratch target with no
  `deploy.toml` `kits` list, its selection holds `agent-cap`, `settings-merge` and `check-wiring`
  beside every entry the base default held, and `govkit.py selfcheck` reports the default set clean.
  Red when: an entry is missing, or the selection's requirements are unsatisfied.
- **AC2** — When `govkit.py apply --kits agent-cap,settings-merge` runs against a target whose
  receipt does not claim `kickoff-manifest`, it refuses naming that requirement.
  Red when: the gate installs without its card writer.
- **AC3** — When a default `govkit.py apply` runs against a scratch target that declines
  memory-recall's hook, its output carries `wired` for every gate, card and check-wiring fragment, a
  `not wired` line naming `recall-opened.js`, and no `landed UNWIRED` or REFUSED line; then
  `check-wiring.sh --check` in the target prints `ok` for `agent-cap`, `scratch` and `card`.
  cost: a full apply into a scratch target, minutes.
  Red when: a default fragment lands unwired, or a declined opt-in hook reads as a refusal.
- **AC4** — When `govkit.py update --write` moves a scratch target whose receipt predates this
  change, it prints `default-gained` for the three entries, installs them, and wires the card
  fragments the receipt already held; after `settings-merge.py --unwire` of the gate's fragment, a
  second update leaves it unwired and `check-wiring.sh --check` names it `UNWIRED`.
  Red when: the migration leaves a held fragment unwired, or a later update re-wires a deliberate
  unwire.
- **AC5** — When `adopt-memory-tree.sh --scaffold` runs in a fixture tracking `src/`, `lib/`,
  `.github/` and the memory root, with no conf, the seeded `.memory-tree.conf` holds
  `ROUTED_PATHS="lib/ src/"` and today's `ROUTED_COMMIT_CUTOFF`, and the run exits 1 naming both.
  Red when: the candidate holds a dot-directory or the memory root, or a key is left blank.
- **AC6** — When `adopt-memory-tree.sh --arm-routing` runs on a conf assigning neither key it
  appends both and prints the candidate; on a conf assigning either, a blank included, it writes
  nothing and says so.
  Red when: an assigned value is overwritten, or a missing pair is not appended.
- **AC7** — When `check-wiring.sh --check` runs on a fixture whose `.memory-tree.conf` assigns
  `ROUTED_PATHS=""`, it prints an `UNWIRED  routed` line naming the key and exits 1, and
  `check-wiring.sh --session` prints the same line and exits 0; with the gate's fragment wired and no
  conf, it prints `UNWIRED  routed` naming the absent conf.
  Red when: an unarmed or conf-less gated tree reads `ok` or `skip`.
- **AC8** — When the fixture's hooks kit ships `scratch-guard.fragment.json` and
  `scratch-guard-subagent.fragment.json` and only the first is wired, `check-wiring.sh --check` names
  the SubagentStart entry `UNWIRED`; when the PreToolUse fragment's matcher is wired under
  `SubagentStart`, it names that entry too.
  Red when: the arm grades one fragment, or a matcher on the wrong event reads as wired.
- **AC9** — When the gate's fragment is wired and `HOME` points at a scratch directory with no
  `/session-kickoff` install, `check-wiring.sh --check` prints `UNWIRED  skill` naming
  `WIRE-INTO-PROJECT.md` §1.
  Red when: it prints `skip`.
- **AC10** — When `grep -n 'NotebookEdit' WIRE-INTO-PROJECT.md` runs, §5 lists the gate's matcher
  beside every other hook in §4's table with its event and matcher, and §3 names `ROUTED_PATHS` and
  `ROUTED_COMMIT_CUTOFF`.
  Red when: a hook a default install wires is absent from the runbook's list.

## 7. Gates

`govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `govkit selfcheck` · `govkit runbook parity` · `recall floor` · `recall floor arms` · `kit epoch (shipped bytes move, the version moves)` · `kit version markers` · `agent-cap self-test` · `scratch-guard self-test` · `verifier fan-out self-test` · `review-join self-test` · `hook destinations self-test` · `hook destinations (every declared hook path ships)` · `check-wiring self-test` · `transition-audit arms` · `straggler-guard arms` · `memory-hygiene self-test` · `memory hygiene` · `python resolver (behaviour + inline parity + idiom ban)` · `install-prefix (shipped surface)` · `lexicon naming predicates` · `codebase-map coverage + freshness` · `harness arms (fail branches armed or pinned)` · `kickoff-manifest ratchet` · `spec tokens (a spec's own names resolve)`

New arm: tools/govkit/selftest.py · covers AC1 AC2 AC4 · a registry whose default set gained an entry after the receipt's vintage, against an update that moves only claimed kits · none

New arm: tools/govkit/matrix.py · covers AC3 · a default apply into the matrix's fresh shape, against the base registry that lands fragments unwired · none

New arm: tools/check-wiring.test.sh · covers AC7 AC8 AC9 · a fixture conf with ROUTED_PATHS blank, a second unwired fragment, and an empty HOME · none

New arm: tools/memory-tree/check-memory-hygiene.test.sh · covers AC5 AC6 · a fixture tree tracking src/, lib/ and .github/ with no conf · none

AC10 is a direct observation of the runbook and adds no arm.

## 8. Open questions

- **F1 — Does `govkit update` install the entries that joined the default set, or print them and
  stop?**
  Installing is the migration this unit exists for, and the widening is the owner's D2, recorded in
  the registry. Printing keeps `update`'s rule that it never widens a target (`govkit.py:9192-9197`)
  and leaves every existing adopter ungated until someone runs `apply --kits`.
  Recommendation: install, and print `default-gained` per entry.
  RESOLVED (owner, 2026-10-09): install, and print `default-gained` per entry.
- **F2 — Does `check-wiring` join the default set?**
  It is the reporter D7 names, and without it an adopter's unwired gate or blank key surfaces only
  as a red leg. It adds a SessionStart run to every adopter session and a held self-test leg.
  Recommendation: join.
  RESOLVED (owner, 2026-10-09): join.
- **F3 — Does the candidate drop a top-level directory that holds only gov's installed kits?**
  Kept, the adopter's own kit update commits must name a unit. Dropped, a receipt-reading
  derivation decides something the adopter confirms anyway, and a mixed directory needs a rule of
  its own.
  Recommendation: keep it in the candidate; the confirmation step is where the adopter drops it.
  RESOLVED (owner, 2026-10-09): keep it in the candidate; the adopter drops it when confirming.
- **F4 — How is `/session-kickoff` made reachable in an adopter?**
  Option (a): the machine junction stays an order `apply` prints, and check-wiring reports a gated
  repository on a machine without it (S9). Option (b): a project-scoped copy under the target's
  `.claude/skills/`, rendered with its paths, which needs a render the kickoff kit does not have.
  Recommendation: (a).
  RESOLVED (owner, 2026-10-09): (a), the machine junction, and check-wiring reports a gated repository without it.

## 9. Revision log

- rev-1 · 2026-10-09 · initial draft.
- rev-2 · 2026-10-09 · §3 · §4 · cross-read fold: order 4 to 5, because `KICK-aRoutedQuill-1` moved
  from order 1 to 2, which shifts every later step by one.
- rev-3 · 2026-10-09 · §8 · owner resolves F1 (install), F2 (join), F3 (keep) and F4 (a).
- rev-4 · 2026-10-09 · §4 · the M2 cross-read of 2026-10-09 found §4 Rollout giving this unit its own
  kit-version bump commit named for this unit, where units 1, 2 and 4 say the versions are minted
  once by the lander; Rollout now leaves the three kits' versions owed and minted once after the
  build's last unit, and keeps the selfcheck after the mint.
- rev-5 · 2026-10-10 · §2 · §4 · build divergence: with `agent-cap` in the default set, selfcheck 7e
  reds `check-agent-cap-restatement`, a conditional entry requiring it that no selection reaches. S1
  drops that entry's conditional mark so `--all` reaches it, and Files touched names its descriptor.
  The Inventory gains `add_deploy_kits`, S4's writer of a target's `deploy.toml` `kits` list.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "govkit default selection gains a hook kit, wires every
landed settings fragment at install and update, and an adopter scaffolds a conf key from a derived
candidate"` ranked `wired` in `tools/check-wiring.sh` as a seam, with `parse_conf` and `kit_rel` in
`tools/memory-tree/tree_lib.py`. The extended seams are `wired` and `matchers_of`, which S8 scopes by
event; `run_fragment_merges` in `tools/govkit/govkit.py`, which already wires a landed fragment and
needs only a selection that always carries `settings-merge`; and `blob_at`, which reads the registry
at the receipt's vintage. No new writer of `.claude/settings.json` is added.

Recall terms used: `default-selection run_fragment_merges settings-merge landed-UNWIRED
fragment-wiring agent-cap scratch-guard check-wiring seed-and-stop regenerate widening add-kits` —
which surfaced `TOOL-aRepatriatedFork-11`, `TOOL-aReplayedCard-15`, `TOOL-aWalkedCorpus-7` and
`TOOL-aWalkedCorpus-8`.
