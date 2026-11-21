# TOOL-dWitnessedBar-107 — verify-peer publishes only a slot the current bar run witnessed

**Status:** CLOSED · rev-1 · 2026-11-21 · node d · Tier-2 · base cdfbd1cf · streams tooling · order 51 · advances TOOL-dWitnessedBar-31

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md) | journal | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-54 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 TOOL-dWitnessedBar-58 TOOL-dWitnessedBar-59 TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-61 TOOL-dWitnessedBar-62 TOOL-dWitnessedBar-63 TOOL-dWitnessedBar-64 TOOL-dWitnessedBar-65 TOOL-dWitnessedBar-66 TOOL-dWitnessedBar-67 TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-71 TOOL-dWitnessedBar-72 TOOL-dWitnessedBar-73 TOOL-dWitnessedBar-74 TOOL-dWitnessedBar-75 TOOL-dWitnessedBar-76 TOOL-dWitnessedBar-77 TOOL-dWitnessedBar-78 TOOL-dWitnessedBar-79 TOOL-dWitnessedBar-80 TOOL-dWitnessedBar-81 TOOL-dWitnessedBar-82 TOOL-dWitnessedBar-83 TOOL-dWitnessedBar-84 TOOL-dWitnessedBar-85 TOOL-dWitnessedBar-86 TOOL-dWitnessedBar-87 TOOL-dWitnessedBar-88 TOOL-dWitnessedBar-89 TOOL-dWitnessedBar-90 TOOL-dWitnessedBar-91 TOOL-dWitnessedBar-92 TOOL-dWitnessedBar-93 TOOL-dWitnessedBar-94 TOOL-dWitnessedBar-95 TOOL-dWitnessedBar-96 TOOL-dWitnessedBar-97 TOOL-dWitnessedBar-106 TOOL-dWitnessedBar-108 |
| [2026-11-19-build-TOOL-dWitnessedBar-107-1-acceptance-ledger.md](../build/2026-11-19-build-TOOL-dWitnessedBar-107-1-acceptance-ledger.md) | journal | — |
| [2026-11-19-build-TOOL-dWitnessedBar-107-1-builder-return.md](../build/2026-11-19-build-TOOL-dWitnessedBar-107-1-builder-return.md) | journal | — |
| [2026-11-21-build-TOOL-dWitnessedBar-107-deviation-1071.md](../build/2026-11-21-build-TOOL-dWitnessedBar-107-deviation-1071.md) | deviation | — |
| [2026-11-19-prompt-TOOL-dWitnessedBar-107-build-brief.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-107-build-brief.md) | journal | — |
| [2026-11-21-prompt-TOOL-dWitnessedBar-107-promotion-brief.md](../prompts/2026-11-21-prompt-TOOL-dWitnessedBar-107-promotion-brief.md) | journal | — |
| [2026-11-21-prompt-TOOL-dWitnessedBar-107-promotion-spec-writer.md](../prompts/2026-11-21-prompt-TOOL-dWitnessedBar-107-promotion-spec-writer.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

The closing diff review's round 1
(`memory/builds/dWitnessedBar/reviews/2026-11-21-review-TOOL-dWitnessedBar-1-closing-diff-review-round1.md`)
confirmed finding 2 at HIGH, report item H2, class `carried-forward-row-read-as-current`. After the
bar runs, `tools/run-gates/verdict_backends.py#run_verify_peer` tests only that
`<common-dir>/gate-verdict/<tree>` is a file and signs its lines into a peer tag. It never asks
whether this run wrote that slot, never reads the bar's exit, and never applies the predicates
`read_local_verdict` applies to the same slot. The runner writes no slot when the tree moved, its
fingerprint did not read or the write failed (`tools/run-gates/run-gates.sh@04da8977:6251`), so a
slot an earlier run left for that tree is published as this run's answer (§4 Evidence).

This unit builds the skeptic's class-level fix. verify-peer snapshots the slot's `run_id` before the
bar, refuses unless the run wrote a new one and its exit agrees with the verdict, and reads the slot
through `read_local_verdict` itself. It publishes a witnessed GREEN or a fresh RED and nothing else.
The record's left-shift gate becomes one fixture plant in the gov canary.

## 2. Scope (IN)

- **S1** — `run_verify_peer`'s per-candidate branch, after the worktree is added, in this order
  (it rewrites `tools/run-gates/verdict_backends.py@d75ea52b:648` to `:660`):
  1. `tree = read_tree_of(repo, sha)` and `slot = common / "gate-verdict" / tree` move ABOVE the bar.
     Where either is empty, `why` is `no full slot path resolves for this candidate's tree` and the
     bar does not run.
  2. `before = read_slot_run_id(slot)`. An `OSError` sets `why` to
     `gate-verdict/<t8> does not read before the bar: <error>` and the bar does not run.
  3. The bar runs as today, under `GATE_FULL=1`, in an environment that omits `GATE_RUN_ID`
     (§8 F2). `rc` is `p.returncode`.
  4. `after = read_slot_run_id(slot)`, its `OSError` read as in step 2 with `after the bar`.
     No file keeps today's `the bar exited <rc> and wrote no full slot for tree <t8>`.
  5. Where `after` is `''` or equals `before`, `why` is
     `the bar exited <rc> and left gate-verdict/<t8> at run <after or none>, a record it did not write`.
  6. `v = read_local_verdict({}, sha, tree, repo)`. Its body reads nothing of its first argument
     (`tools/run-gates/verdict_backends.py#read_local_verdict`), the call unit 69 AC4 made.
  7. It publishes only where `v.state == "GREEN"`, `v.witness == "witnessed"` and `rc == 0`, or where
     `v.state == "RED"` and `rc != 0`. Otherwise `why` is
     `the bar exited <rc> and gate-verdict/<t8>, run <after>, reads <v.state>: <v.why>`.
  8. Before it publishes, `read_slot_run_id(slot)` once more; where it is not `after`, `why` is
     `gate-verdict/<t8> was rewritten while it was read, run <after> then <again>` (§8 F3).
  9. `write_peer_tag(repo, sha, {"verdict": v.state, "tree": tree, "run_id": after}, node, remote)`,
     so the tag carries the state the reader returned and never a line copied from the file.

  `<t8>` is `tree[:8]`. Every `why` prints through today's `not published: <why>` line, so the
  verb's exit stays 1 when any candidate was not published. Observed by AC1, AC2, AC3 and AC4; the
  step-1, step-2 and step-8 refusals are NOT OBSERVED, since staging them needs an unresolvable
  common dir, an unreadable slot or a concurrent writer between two reads, and none is planted here.
- **S2** — `read_slot_run_id(slot)`, a module-level function beside `read_local_verdict`. It returns
  the record's `run_id` value, `''` where the record carries no `run_id` line, and `None` where
  `slot.is_file()` is false. It opens the slot with `encoding="utf-8"`, `errors="replace"` and
  `newline=""` and parses it with `read_tag_lines`, the open and parse unit 69 S2 gave
  `read_local_verdict`. It catches nothing, so an `OSError` reaches S1. Observed by AC1 and AC4.
- **S3** — The plant `peer-stale-slot`. `PLANTS` gains its row, `verify-peer over a stale
  reused_cache 1 slot and a stub bar writing nothing, then stubs writing a reused GREEN, a GREEN on
  exit 1, a RED and a clean GREEN`, and `run_peer_plant` gains an
  `elif case == "peer-stale-slot":` branch above its final `else`, after `write_policy()` as every
  peer case runs. The branch calls `run_stale_slot_plant(top, work, run_scenario)`, a
  module-level function placed after `run_peer_plant`, which builds the scenarios §4 Data model
  lists. Observed by AC1, AC2, AC3 and AC4.
- **S4** — The gov canary, `tools/run-gates/run-gates.gov.test.sh`. Its `for vb_case in` list gains
  `peer-stale-slot:0`, appended to the line holding `peer-bad-signature:1 remote-green:0`, so no
  code line is added. `FLOOR_ASSERTIONS=80` becomes `FLOOR_ASSERTIONS=81`. The owner line above it,
  `# Raised to 80 by TOOL-dWitnessedBar-90, ...`, stays as it is, and one comment line is added below
  the constant: `# RAISED 80 -> 81 by TOOL-dWitnessedBar-107: the peer-stale-slot plant's loop case.`
  The block comment over the loop gains one sentence naming TOOL-dWitnessedBar-107 and the plant.
  Observed by AC5.
- **S5** — The docs. `help/verdict-backends.md`, "Running the peer verifier", gains one paragraph:
  the bar's `run_id` is compared before and after the run, the bar's exit must agree with the
  verdict, and the slot must read as `local-hook` reads it, a witnessed GREEN, or a RED. Anything
  else prints `not published` with its reason, and the bar's environment omits `GATE_RUN_ID`. The
  module docstring's `verify-peer` sentence in `tools/run-gates/verdict_backends.py` says the same in
  one sentence. Observed by AC6.

## 3. Non-goals (OUT)

- The peer reader, `read_peer_verdict`. The record notes it checks none of the reuse or selection
  keys. A tag S1 publishes has passed `read_local_verdict` on the publishing node, so the reader stays
  as it is, and the tag message keeps its four lines (`write_peer_tag`).
- The runner's slot writer (`tools/run-gates/run-gates.sh@04da8977:6251`) and its `run_id`
  derivation. S1 reads what the runner writes and changes nothing in it.
- `read_local_verdict` and `check_local_record`. S1 calls the first as it stands.
- A lock between concurrent full runs on one clone. §8 F3's re-read refuses a rewrite it sees and
  does not prevent one.
- The pre-push policy read of review item H1, which is `TOOL-dWitnessedBar-106`'s, and the four
  MEDIUM and LOW items, which are `TOOL-dWitnessedBar-108`'s.

The code this unit changes was built by TOOL-dWitnessedBar-6, TOOL-dWitnessedBar-43,
TOOL-dWitnessedBar-56, TOOL-dWitnessedBar-62, TOOL-dWitnessedBar-63 and TOOL-dWitnessedBar-90, all
CLOSED, as the `Pass:` trailers on that code's `git log` name them. It edits `run_verify_peer`,
`run_peer_plant`, `PLANTS`, the canary's plant loop and its `FLOOR_ASSERTIONS` line, and calls
`write_peer_tag` and `read_local_verdict`, through which `check_local_record` applies, unchanged.
This unit edits only their built code, never their specs, which stay frozen. A `consumes-from` edge onto a frozen spec could never be reciprocated, so none is declared
(§8 F4).

### Edges

none

## 4. Design

### Evidence

Probed on this node at `63be790a2` (PINNED 2026-11-21). The blob of
`tools/run-gates/verdict_backends.py` at HEAD is `d75ea52b` and of `tools/run-gates/run-gates.sh` is
`04da8977`, the blobs the review cites, so its line numbers hold at HEAD (PINNED 2026-11-21).

- **The defect, at HEAD.** A scratchpad script built a fixture repo with
  `verdict_backends.py#write_fixture_tree`, a throwaway key for node b and a candidate commit whose
  `tools/run-gates/run-gates.sh` was `exit 1`. It pushed `refs/gov/candidate/<sha>` and planted
  `gate-verdict/<tree>` as GREEN with `run_id r0`, `reused 1`, `reused_cache 1` and `selection none`.
  `verdict_backends.py verify-peer` under `GOV_NODE=b` printed
  `verify-peer · 43c3b3db · published refs/gov/verdict/43c3b3db as node b` and exited 0 (PINNED 2026-11-21), and the
  remote listed the verdict ref. `read --backend local-hook` on the same slot printed `NONE · the
  record says its run reused 1 leg(s) from the cache` and exited 1 (PINNED 2026-11-21).
- **The stub reaches verify-peer's bar path.** The bar is `scratch / prefix / "run-gates.sh"`, the
  prefix being `git rev-parse --show-prefix` run in `HERE`
  (`tools/run-gates/verdict_backends.py@d75ea52b:634`). It printed `tools/run-gates/`, equal to
  `FIX_KIT` plus a slash, and the probe's stub at that prefix ran under `resolve_bash`.
- **The run_id is per run.** `RUNID="$TS_RUN"` (`tools/run-gates/run-gates.sh@04da8977:2793`), and
  `TS_RUN` is `${GATE_RUN_ID:-$(date -u +%Y%m%dT%H%M%SZ)-$$}` (`tools/run-gates/run-gates.sh@04da8977:1645`),
  so two unpinned runs differ by their pid, and a pinned `GATE_RUN_ID` repeats (§8 F2).
- **Exit against verdict.** A RED bar exits 1 (`tools/run-gates/run-gates.sh@04da8977:6493`), a HOST
  one exits 4 (`tools/run-gates/run-gates.sh@04da8977:6474`) and writes `RED` (`_vverdict=RED` at
  `tools/run-gates/run-gates.sh@04da8977:6261`), so
  "RED and a non-zero exit" covers both.
- **Neighbour plants.** `--fixture --plant reused-cache` held its one scenario with exit 0, and
  `--fixture --plant peer-unsigned` held both, ssh-keygen running here (PINNED 2026-11-21).
  `peer-signed` ran in 2.3 s and the probe in 1.5 s wall (PINNED 2026-11-21).
- **Counts.** `sh_hygiene.py --shell-role --measure . tools/run-gates/run-gates.gov.test.sh` printed
  `853`, equal to the row in `memory/project/shell-role.txt` (PINNED 2026-11-21). The canary's last
  commit is `da3fbc953`, TOOL-dWitnessedBar-90's, so no arm landed after its absolute count of 80
  (DERIVED by `git log -1 -- tools/run-gates/run-gates.gov.test.sh`).

### Data model

`run_stale_slot_plant` writes one candidate commit on a branch off `main`. It holds a stub at
`<prefix>run-gates.sh`, the prefix read by `run_git(HERE, "rev-parse", "--show-prefix")` exactly as
S1 reads it, so the two agree by construction. It pushes the commit to `origin` as
`refs/gov/candidate/<cand>`, sets `user.signingkey` to node b's key, and plants
`gate-verdict/<cand tree>` holding `tree`, `sha`, `verdict GREEN`, `kind full`, `run_id r0`,
`reused 1`, `reused_cache 1` and `selection none`. The stub reads `VB_STUB_BAR`:

| `VB_STUB_BAR` | the stub writes, at `<git common dir>/gate-verdict/<HEAD tree>` | it exits |
|---|---|---|
| unset | nothing | 1 |
| `reused` | GREEN, `reused 1`, `reused_cache 1`, `selection none`, `run_id s-reused` | 0 |
| `disagree` | GREEN, the pair at 0, `selection none`, `run_id s-disagree` | 1 |
| `red` | RED, the pair at 0, `selection none`, `run_id s-red` | 1 |
| `clean` | GREEN, the pair at 0, `selection none`, `run_id ${GATE_RUN_ID:-s-clean}` | 0 |

Each written record carries the `tree` line `git rev-parse HEAD^{tree}` prints in the worktree. The
common dir is `git rev-parse --path-format=absolute --git-common-dir`. Every verify-peer run is
`run_scenario(<name>, work, [*me, "verify-peer"], <owed>, <needles>, GOV_NODE="b", GOV_REMOTE="origin", VB_STUB_BAR=<mode>)`.
The scenarios, in order, `<c8>` being `cand[:8]`:

| # | scenario | owed | needles |
|---|---|---|---|
| 1 | a stale GREEN slot, reused_cache 1, the bar writing nothing | 1 | `not published`, `at run r0, a record it did not write` |
| 2 | a fresh GREEN whose reused_cache reads 1 | 1 | `not published`, `reads NONE`, `reused 1 leg(s) from the cache` |
| 3 | a fresh clean GREEN on a bar that exited 1 | 1 | `not published`, `the bar exited 1`, `reads GREEN` |
| 4 | no verdict published after three refusals | 0 | `verdict refs: 0` |
| 5 | a fresh RED | 0 | `published refs/gov/verdict/<c8> as node b` |
| 6 | the RED tag's lines | 0 | `verdict\tRED\n`, `run_id\ts-red\n` |
| 7 | a fresh clean GREEN, GATE_RUN_ID=s-red in verify-peer's environment | 0 | `published refs/gov/verdict/<c8> as node b` |
| 8 | the GREEN tag's lines | 0 | `verdict\tGREEN\n`, `run_id\ts-clean\n` |

Scenario 4 appends `(name, rc, 0, needles, said)` to the plant's list, as the lander plants do:
`said` is `verdict refs: <n>` for the lines `git ls-remote origin refs/gov/verdict/*` lists, and
`rc` is 0 only where `n` is 0 (S3). Scenarios 6 and 8 read `git cat-file tag` of the remote's ref, and
after 6 the plant deletes that ref with `git update-ref -d` in the bare remote, so 7's candidate has
no verdict again. Scenario 7 passes `GATE_RUN_ID="s-red"`: a verb that kept it would hand the stub
the id the slot already holds, and step 5 would refuse. The plant's last owed exit is 0, the case
`peer-stale-slot:0` S4 adds.

### Inventory

Minted, each named with a `.lexicon.conf` VERBS verb where it is a function:

| name | kind | where |
|---|---|---|
| `read_slot_run_id` | function | `tools/run-gates/verdict_backends.py` |
| `run_stale_slot_plant` | function | `tools/run-gates/verdict_backends.py` |
| `peer-stale-slot` | plant name, a `PLANTS` key | `tools/run-gates/verdict_backends.py` |
| `VB_STUB_BAR` | the stub's own environment input, read by no product code | the stub's text inside `run_stale_slot_plant` |

No nested function is minted; the stub's text is a local string. Naming cells: the lexicon's
function-verb cell grades both functions. No new file, flag or verb.

### Migration

None: no stored record changes shape. A slot an earlier verify-peer published from stays published,
since S1 reads only candidates with no verdict ref beside them.

### Rollout

Live at landing, at order 51 beside `TOOL-dWitnessedBar-106` and `TOOL-dWitnessedBar-108`. A node
that runs `verify-peer` publishes less, never more: every candidate S1 refuses was one HEAD
published.

### Files touched (estimate)

- `tools/run-gates/verdict_backends.py`
- `tools/run-gates/run-gates.gov.test.sh`
- `help/verdict-backends.md`

S4 adds a loop case to an existing line and a comment line, so the gate-lint shell-role ledger
keeps the canary's row of 853 (§4 Evidence). A pass that adds a code line instead owes that row's
widen route and lists the ledger, its home under memory/project, here.

### Alternatives rejected

- **The finder's instance fix: a changed run_id, an agreeing exit and `check_local_record` on a
  GREEN.** The skeptic judged it INSTANCE-ONLY: it skips the tree-line match, the GREEN or RED line
  validity and the `newline=""` read `read_local_verdict` carries, so a second copy of that reader's
  order would drift from the first.
- **An mtime compare in place of the run_id.** A filesystem with a coarse mtime gives two writes in
  one tick the same stamp, and an mtime proves a write, not which run made it.
- **One candidate commit per stub behaviour.** verify-peer bars every candidate it lists in one
  call, so scenarios could not be told apart; one candidate and `VB_STUB_BAR` give one behaviour
  per call.

## 5. Production-readiness checklist

- security — closes a signed-GREEN path: a peer tag now certifies only a record this run wrote and
  the local-hook reader stands on. Deny by default: every unread, unchanged or disagreeing slot
  refuses.
- perf / scale — three small reads per candidate beside a full bar run (S1 steps 2, 4 and 8). The
  canary's added plant is five verify-peer runs, about 8 s on this node (DERIVED from §4 Evidence's
  1.5 s probe).
  The leg's budget row is 60 s, its last reading 19 s (PINNED 2026-11-21, selftest-budgets row).
  That row is `tools/run-gates/selftest-budgets.txt@0c0e9483:127`.
- error / empty / loading states — S1 names each refusal on the `not published` line; a pre-run
  read failure skips the bar rather than run it to no purpose.
- observability — each `why` names the tree, the run_id read and the reader's state and reason.
- risks — an operator running verify-peer with `GATE_RUN_ID` set is unaffected (§8 F2). A
  concurrent full run on one clone for the same tree can make S1 refuse a candidate it could have
  published; the next verify-peer run retries it.
- testing — AC1 to AC4 through the plant, AC5 and AC6 by grep and measure; the canary re-observes
  the plant at the close.
- migration — none.
- user docs — `help/verdict-backends.md`, S5.

## 6. Acceptance criteria

- **AC1** — When `python tools/run-gates/verdict_backends.py --fixture --plant peer-stale-slot` runs,
  scenario 1 prints `exit 1 · owed 1` and `held`, its output holds `not published` and
  `at run r0, a record it did not write`, and scenario 4 holds with `verdict refs: 0`.
  Red when: verify-peer publishes a slot the bar did not write, as HEAD does (§4 Evidence: exit 0,
  `published`), or the plant planted no `reused_cache 1` slot and passes by finding nothing.
  fixture: a scratch repository the plant makes under `tempfile.mkdtemp`; ssh-keygen must run.
- **AC2** — When the same plant runs, scenario 2 holds: `exit 1`, `reads NONE` and
  `reused 1 leg(s) from the cache` on its `not published` line.
  Red when: S1 publishes a fresh slot without `read_local_verdict`, so a reused GREEN is signed.
- **AC3** — When the same plant runs, scenario 3 holds: `exit 1`, `the bar exited 1` and
  `reads GREEN` on its `not published` line.
  Red when: S1 ignores `p.returncode`, so a GREEN record on a failed bar is published.
- **AC4** — When the same plant runs, scenarios 5 to 8 hold, the last line prints
  `8 of 8 scenario(s) held · all held` (DERIVED from §4 Data model's table), and the command exits 0.
  Red when: S1 refuses every candidate, so no fresh RED or witnessed GREEN publishes; the tag
  carries a run_id other than the one the bar wrote; or `GATE_RUN_ID` reaches the bar, so scenario 7
  reads `s-red` as unchanged and refuses.
- **AC5** — When `grep -n 'peer-stale-slot:0' tools/run-gates/run-gates.gov.test.sh` runs it prints
  one line, which also holds `remote-green:0`; `grep -n -A1 '^FLOOR_ASSERTIONS=81$' tools/run-gates/run-gates.gov.test.sh`
  prints the constant and `# RAISED 80 -> 81 by TOOL-dWitnessedBar-107`; the line above it still
  starts `# Raised to 80 by TOOL-dWitnessedBar-90`; and
  `python tools/gate-lint/sh_hygiene.py --shell-role --measure . tools/run-gates/run-gates.gov.test.sh`
  prints `853` (PINNED 2026-11-21 in §4 Evidence).
  Red when: the case sits on a new line, the floor is left at 80, or TOOL-dWitnessedBar-90's owner
  line is edited.
- **AC6** — When `grep -c 'not published' help/verdict-backends.md` runs it prints at least 1, and
  `grep -n 'GATE_RUN_ID' help/verdict-backends.md tools/run-gates/verdict_backends.py` names the
  help paragraph, the docstring sentence and S1 step 3's environment.
  Red when: the page still says the verb pushes a tag for every candidate it bars.

## 7. Gates

`run-gates gov canary` · `lexicon naming predicates` · `python reads (a name never bound, an import outside its guard)` · `portability (shell lines only shrink)` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

`python tools/check-spec-tokens.py --legs-for` names no guarded leg for `help/verdict-backends.md`,
and every leg it names for the two kit paths carries a broad guard, so the join owes none of them
(PINNED 2026-11-21). The legs above are the ones this change can red: the canary runs the plant, the
lexicon grades the two new function names, `python reads` scans the module, and the shell-role leg
holds the canary's 853 code lines (PINNED 2026-11-21). The canary is chunk `selftests`, held
unless `GATE_SELFTESTS` is set, which `SELFTESTS_OWED_PATHS="tools/"` in `.unattended.conf` makes
the main loop set at the close.
WHAT THE ARM DOES NOT CHECK: a real peer's bar, a concurrent writer between S1's reads, or the
step-1 and step-2 refusals.

New arm: tools/run-gates/run-gates.gov.test.sh · covers AC1 AC2 AC3 AC4 · the `peer-stale-slot` loop case, its stale `reused_cache 1` slot and a stub bar that exits 1 writing nothing, run red against HEAD's `run_verify_peer` first · FLOOR_ASSERTIONS 80 -> 81

## 8. Open questions

- **F1 — Which binding line does a unit the closing review promoted carry?** The carries join reds a
  chain spec that carries nothing and is derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of a repaired unit's clause. The review item spans
  TOOL-dWitnessedBar-6 and TOOL-dWitnessedBar-43 and carries no clause of its own, so (b) has
  nothing to split; veto 1 discards it.
  RESOLVED (agent, 2026-11-21, delegated): (a), the precedent every promoted unit of this build sets
  (`TOOL-dWitnessedBar-69` §8 F1).
  widens: none · relaxes: none
- **F2 — What does S1 do with a `GATE_RUN_ID` in the operator's environment?** A pinned id repeats
  (§4 Evidence), so step 5 would read every re-run as stale. Options: (a) remove it from the bar's
  environment; (b) keep it, so a pinned id refuses every candidate; (c) refuse the verb, exit 2,
  while it is set. (b) leaves an operator a refusal with no cure in the verb, a follow-up; (c) adds
  a refusal surface no criterion asks for. RESOLVED (agent, 2026-11-21, delegated): (a), the most
  criteria met with no follow-up, observed by AC4's scenario 7.
  widens: none · relaxes: none
- **F3 — How is the published run_id bound to the verdict `read_local_verdict` read?** The reader
  re-opens the slot, so a rewrite between S1's reads would pair one run's id with another's state.
  Options: (a) re-read the run_id after the reader and refuse on a change (S1 step 8); (b) one read
  after the bar only; (c) change `read_local_verdict` to return its record. (b) leaves the pairing
  open, a follow-up; (c) changes the reader every backend dispatch calls through `read_verdict`,
  beyond this unit's scope (§3). RESOLVED (agent, 2026-11-21, delegated): (a), tie-broken by reuse
  of the reader as it stands.
  widens: none · relaxes: none
- **F4 — How does §3 record the CLOSED units whose built code this unit edits?** The six units are
  CLOSED and their specs are frozen, so no `hands-off` can be written back into them. Check 12's
  reciprocity join grades a CLOSED target like any other: run as
  `check-memory-hygiene.sh --only 12 --spec` over the in-build form, it printed one
  `declares no matching **hands-off**` finding per edge, 6 in all (PINNED 2026-11-21). Options:
  (a) an in-build `consumes-from` edge to each; (b) `external` bullets naming the units in prose;
  (c) no edge bullet, with `none` under Edges and the units named in §3 prose. (a) fails the memory
  hygiene gate this spec owes, and (b) dodges the join's refusal of a same-build id written as
  `external`, so veto 1 discards both. RESOLVED (agent, 2026-11-21, delegated): (c), on the
  coordinator's correction of the brief, which had asked for (a).
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-21 · initial draft, promoted from the closing diff review's round 1, finding 2
  (HIGH, item H2), per 2026-11-21-prompt-TOOL-dWitnessedBar-107-promotion-brief.

## 10. Reuse audit

The seam is the code the finding names. S1 calls `tools/run-gates/verdict_backends.py#read_local_verdict`
whole, the reader the `local-hook` backend already stands on, rather than a second copy of its
order, and S2 reuses its `newline=""` open and `read_tag_lines`. S3 extends
`verdict_backends.py#run_peer_plant`, whose keyed, pushed setup every peer plant shares, and
`run_fixture_command` and `run_scenario` as they stand. S4 extends the canary's existing plant loop.
`python tools/codebase-map/reuse_lookup.py "refuse a record the current run did not write, compare run id before and after"`
ranked `run`, `write`, `before`, `write_text` and `run_git` first (PINNED 2026-11-21), none a
freshness check, and `grep -rn run_id tools --include=*.py` finds no before-and-after compare, so no
existing seam fits the snapshot itself.
Recall terms used: `--terms "verify-peer stale slot run_id gate-verdict carried-forward witnessed local-hook check_local_record reused_cache peer-node tag"`.
