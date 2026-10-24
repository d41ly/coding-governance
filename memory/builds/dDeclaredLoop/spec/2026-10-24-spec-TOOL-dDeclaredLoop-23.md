# TOOL-dDeclaredLoop-23 — the commit node and its kind, and one trailer reader with both views

**Status:** OPEN · rev-1 · 2026-10-24 · node d · Tier-2 · base ed497191 · streams tooling · order 3 · advances TOOL-dDeclaredLoop-35

**Carries:** cl-dClosedLoop-0108@df656363 whole
**Carries:** node:record-kind.commit

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-TOOL-dDeclaredLoop-1-reuse-scout-b.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-reuse-scout-b.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 |
| [2026-10-24-build-TOOL-dDeclaredLoop-1-spec-stage-returns.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-spec-stage-returns.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 |
| [2026-10-24-prompt-TOOL-dDeclaredLoop-1-spec-brief.md](../prompts/2026-10-24-prompt-TOOL-dDeclaredLoop-1-spec-brief.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 |

<!-- /gen:spec-records -->

## 1. Goal

A commit becomes a node with its own kind: the `commit` native-id class is registered, every trailer key
gov reads is registered with it, and one reader parses them, offering the two views today's readers
answer, the union of subject and trailer ids and the trailer replacing the subject, each consumer naming
its view. Today `Pass:` has two readers that disagree (`gap-spine-09`), and no commit names the item,
act or session that made it, 0 of 6,084, with the trailer schema declared nowhere (`gap-spine-08`).

## 2. Scope (IN)

- **S1** — The `commit` native-id class: a `[[native]]` row in `tools/playbook/namespaces.toml`
  (PLAY-dOrderedCharter-28 S2's shape), `class = "commit"`, `owner = "dDeclaredLoop"`,
  `pattern = "commit_trailers:SHA_RE"` and `resolver = "commit_trailers:resolve_commit"`. Observed by
  AC6.
- **S2** — The commit kind's keys, in PLAY-dOrderedCharter-28's `[[trailer]]` table of
  `tools/playbook/edges.toml`: its rows `Gov-Unit`, `Gov-Item` and `Pass` mapped to `serves`, `Gov-Act`
  to `made-by`, `Gov-Session` to `runs-in` and `Decided` to `decides`, read and asserted here, never
  re-added; and two rows this build adds with no `type`, `Gov-Transition` and `Gov-Policy`, the keys
  TOOL-dDeclaredLoop-3 and TOOL-dDeclaredLoop-2 write (shared interface I7, §8 F2). Observed by AC6.
- **S3** — The one reader, `tools/lib/commit_trailers.py`: `read_commits(repo, revs, keys, paths=())`,
  one `git log` call per read, git's own `%(trailers:key=…,valueonly)` parse; `attribute(commit, view,
  id_re=None)` for the views `union` and `replace`; `decided(commit)`; `read_message_ids(text)` for a
  commit message not yet committed; `SHA_RE` and `resolve_commit`; and a CLI with the verbs `tokens`
  and `message` for the shell consumers. The token rule is today's one rule: ids split on any character
  outside `[A-Za-z0-9-]`, and a `none` anywhere attributes the commit to nothing
  (`tools/unattended/lib-unattended.sh:1073-1074`). Observed by AC1 and AC2.
- **S4** — The copies, each between `# >>> commit_trailers_py -- canonical copy: commit_trailers.py in
  the gov lib dir (byte-identical; gated)` and `# <<< commit_trailers_py`, under one `commit_trailers_py`
  row of `PARITY_ROWS` in `tools/lib/resolve-python.test.sh`: `tools/memory-tree/commit_trailers.py`,
  `tools/unattended/commit_trailers.py` and a block inline in `tools/runlog/model.py`, the pattern
  `remote_ladder_py` sets (`tools/runlog/model.py:622-674`). Observed by AC5.
- **S5** — The re-points, one unit, each consumer naming its view (§4 "### The consumers"): the three
  the clause names, `routed_commits.py` (`union`), unattended's `read_attribution_tokens` (`replace`)
  and runlog's `read_git_range` (`decided`, for `Decided:`); and the four other product readers of `Pass:` that apply
  the same `replace` rule by hand. Observed by AC2, AC3 and AC4.
- **S6** — The planted commits `Pass: none`, `Pass: <id>` and a subject id with `Pass: none`, read
  identically by `routed_commits.py`'s attribution and unattended's commit check before and after the
  re-point. Observed by AC2 and AC3.
- **S7** — The position engine reads commits through this reader: the hand-off of S3's API to
  TOOL-dDeclaredLoop-7. NOT OBSERVED here: that engine does not exist at this unit's order; its own
  spec observes the read.

## 3. Non-goals (OUT)

- The writers of `Gov-Unit`, `Gov-Item`, `Gov-Act` and `Gov-Session`: dWellOiledMachine's commit queue
  and `prepare-commit-msg` filler (memory-plan `[sites]`, PLAY-dOrderedCharter-28 §3). This build writes
  only `Gov-Transition` (TOOL-dDeclaredLoop-3) and `Gov-Policy` (TOOL-dDeclaredLoop-2).
- The commit adapter that turns trailers into edges, `tools/playbook/edge_grammar.py`, and the
  `[[trailer]]` table's existing rows: PLAY-dOrderedCharter-28's.
- The trace checks over act-made commits (memory-plan `commits:` arm): dWellOiledMachine's.
- The `transition_audit.py` merge audit and the commit-msg hook's backlog arm, which read no `Pass:`.
- Test suites that read `Pass:` to assert fixtures (`tools/push-main.test.sh:897`,
  `tools/workflows/unattended-build.test.sh:2506`): a suite reading a fixture's trailer is not a reader
  of record.

### Edges

- **hands-off** `TOOL-dDeclaredLoop-2` — `commit_trailers.py`, which reads the `Gov-Policy` trailer its policy command writes
- **hands-off** `TOOL-dDeclaredLoop-3` — `commit_trailers.py`, which reads the `Gov-Transition` trailer its record writes
- **hands-off** `TOOL-dDeclaredLoop-7` — `commit_trailers.py`, the one reader the position engine reads commits through

## 4. Design

### The reader

```python
SHA_RE = re.compile(r"[0-9a-f]{7,40}")
VIEWS = ("union", "replace")

def read_commits(repo, revs, keys, paths=()):      # -> [{sha, parents, date, subject, trailers}]
def attribute(commit, view, id_re=None):           # -> list of ids, in token order, deduplicated
def decided(commit):                               # -> the Decided values, in git's order
def read_message_ids(text):                        # -> the replace view over an uncommitted message
def resolve_commit(repo, token):                   # -> the full sha, or None
```

`read_commits` builds one format string, `%x1e%H%x1f%P%x1f%cI%x1f%s`, then one
`%x1f%(trailers:key=<k>,valueonly,separator=%x1d)` per requested key, so a consumer pays for the keys it
reads. `subject` is `%s`, the first paragraph joined, which is what every reader reads today.

| View | A commit with a `Pass:` trailer | A commit with none |
|---|---|---|
| `union` | the subject's ids, plus the trailer's ids; `Pass: none` adds none and keeps the subject's | the subject's ids |
| `replace` | the trailer's ids alone; a `none` anywhere attributes nothing | the subject's ids |

The ids are the whole tokens matching `id_re` when given, else every token of the token rule, which is
what `read_attribution_tokens` prints today. The CLI's `tokens <revs>` prints that function's bytes
exactly: `<sha> PASSTRAILER <ids>` for a trailered commit, else `<sha> <subject tokens>`.
`message --view replace <file>` prints the ids `check_commit_message` reads, after the comment and CR
stripping it does today (`tools/unattended/unattended.sh:13491-13496`), using `git interpret-trailers
--parse` as it does.

### The consumers

| Consumer | Today | View | Re-point |
|---|---|---|---|
| `tools/memory-tree/routed_commits.py` `read_routed_commits` (:228-231) | its own format string, ids from subject plus trailer (:282) | `union` | `read_commits(…, keys=("Pass",))` and `attribute(c, "union", id_re)` |
| `tools/memory-tree/routed_commits.py` `read_newest_unit` (:357-371) | a second format string | `union` | the same two calls |
| `tools/memory-tree/deviation_join.py` first-pass reading (:327-331) | the trailer replacing the subject, by hand | `replace` | `attribute(c, "replace", id_re)` |
| `tools/unattended/lib-unattended.sh` `read_attribution_tokens` (:1149) | awk over `git log` | `replace` | `"$py" "$KIT_DIR/commit_trailers.py" tokens "$@"` |
| `tools/unattended/lib-unattended.sh` `pass_commit` walk (:1064-1072) | its own `git log` and token rule | `replace` | reads `read_attribution_tokens` over its range |
| `tools/unattended/check-unattended.sh` (:4219-4223) | one commit's subject and trailer, by hand | `replace` | `commit_trailers.py tokens -1 <sha>` |
| `tools/unattended/unattended.sh` `check_commit_message` (:13491) | `git interpret-trailers` and its own token rule | `replace` | `commit_trailers.py message --view replace <file>` |
| `tools/runlog/model.py` `read_git_range` (:592) | its own `Decided` format | `decided` | `read_commits(…, keys=("Decided",))`, keeping its name-status and body read |

Each Python consumer imports its kit's copy; each shell consumer runs its kit's copy with the
interpreter the kit already resolves (`resolve_python`, `tools/unattended/unattended.sh:393`,
`tools/unattended/check-unattended.sh:94`). The shell spawns stay one per call: the `git log` each
reader ran becomes the reader's own.

### The trailer table

```toml
# tools/playbook/edges.toml, beside PLAY-dOrderedCharter-28's six rows
[[trailer]]
key = "Gov-Transition"     # value: <from> -> <to>, written by TOOL-dDeclaredLoop-3

[[trailer]]
key = "Gov-Policy"         # value: the policy change's record, written by TOOL-dDeclaredLoop-2
```

A row with no `type` registers a key that carries a value and no edge. The commit adapter skips it, and
`read_commits` refuses a key the table does not register, so a consumer cannot read an unregistered
trailer.

### Inventory

Minted: `tools/lib/commit_trailers.py` with `SHA_RE`, `VIEWS`, `read_commits`, `attribute`, `decided`,
`read_message_ids`, `resolve_commit` and the CLI verbs `tokens` and `message`; the parity marker
`commit_trailers_py`; the native class `commit`; the trailer rows `Gov-Transition` and `Gov-Policy`.
Naming cells: each function is asked of `python tools/lexicon/lexicon.py --suggest <name> --as
py.function` at the pass.

### Migration

None: no reader's answer moves, and no trailer is rewritten. A `typeless` trailer row is additive to
PLAY-dOrderedCharter-28's table.

### Rollout

Live at landing; every consumer's output is byte-identical on the planted commits (AC2, AC3).

### Files touched (estimate)

- `tools/lib/commit_trailers.py`
- `tools/lib/resolve-python.test.sh`
- `tools/memory-tree/commit_trailers.py`
- `tools/memory-tree/routed_commits.py`
- `tools/memory-tree/deviation_join.py`
- `tools/unattended/commit_trailers.py`
- `tools/unattended/lib-unattended.sh`
- `tools/unattended/check-unattended.sh`
- `tools/unattended/unattended.sh`
- `tools/runlog/model.py`
- `tools/playbook/namespaces.toml`
- `tools/playbook/edges.toml`

### Alternatives rejected

- **A shell canonical beside the Python one**, as `remote_ladder_sh` is: two implementations of one
  token rule, which is the disagreement this unit closes.
- **Re-pointing only the three readers the clause names**: four more product readers apply `replace`
  by hand, and one reader means every reader.

## 5. Production-readiness checklist

- security — read-only over git history and a message file; no network, no write.
- perf / scale — one `git log` per read, as today; the shell readers trade an awk for one interpreter
  start per call, which the `spawn budget (forks per hot entrypoint)` leg grades.
- error / empty / loading states — an empty range returns no commits; an unregistered key is refused
  by name; a truncated stream is refused, as `routed_commits.py` refuses one today.
- observability — the CLI prints the same lines its shell consumers read today.
- risks — the unattended kit's suites are waived for this landing (README rule 8), so the commit
  check's before-and-after reading is observed by a scratch probe (AC3), not by its suite.
- testing — AC1 to AC6 by probes and fixtures under `%TEMP%`; the routed-commits arm in §7 is observed
  RED then GREEN by the main loop at the close.
- migration — none.
- user docs — none owed: no page under `help/` describes commit trailers.

## 6. Acceptance criteria

- **AC1** — When `python commit_trailers.py --fixture` runs in `tools/lib/`, it builds a scratch
  repository under `%TEMP%` with three commits, a subject naming `TOOL-tFix-1` with no trailer, a
  subject naming `TOOL-tFix-1` with `Pass: none`, and a subject naming none with `Pass: TOOL-tFix-2`,
  and prints `union` as `TOOL-tFix-1`, `TOOL-tFix-1`, `TOOL-tFix-2` and `replace` as `TOOL-tFix-1`,
  nothing, `TOOL-tFix-2`.
  Red when: `replace` keeps the subject's id beside `Pass: none`, so the second commit reads
  `TOOL-tFix-1`.
- **AC2** — When a scratch probe runs the attribution of `tools/memory-tree/routed_commits.py` over
  the AC1 repository twice, once with the file as it stands at base `ed497191`, read out with `git show`,
  and once from the working tree, the ids per commit are identical.
  Red when: the re-pointed reader passes `replace`, so the `Pass: none` commit loses its subject id.
- **AC3** — When the same probe sources `read_attribution_tokens` from
  `tools/unattended/lib-unattended.sh` at base `ed497191` and from the working tree over the AC1
  repository, the two outputs are byte-identical; and `check_commit_message` given the three messages
  as files returns the same exit code from both trees (README rule 8: the kit's suite is waived, so the
  probe observes it).
  Red when: the CLI prints a trailing space or drops `PASSTRAILER`, so the bytes differ.
- **AC4** — When `read_git_range` from `tools/runlog/model.py` reads a scratch commit carrying two
  `Decided:` lines, it returns both values in order, as the same function at base `ed497191` does.
  Red when: the `decided` view joins the values into one string.
- **AC5** — When `git grep -c "commit_trailers_py" -- tools/lib/resolve-python.test.sh` runs, it counts
  the `PARITY_ROWS` row, and `git grep -l ">>> commit_trailers_py" -- tools` lists the canonical and the
  three copies; a one-byte edit to one copy makes the parity extract of that row differ.
  Red when: a copy carries no marker, so the parity population misses it.
- **AC6** — When `grep -n 'class = "commit"' namespaces.toml` and `grep -nE 'key = "Gov-(Transition|Policy)"'
  edges.toml` run in `tools/playbook/`, each finds its rows, and `read_commits` asked for a key
  `Gov-Nope` refuses naming the key.
  Red when: the reader reads any key it is handed, so an unregistered trailer is readable.

## 7. Gates

`routed-commits selftest` · `routed commits name a specced unit` · `runlog selftest` · `pre-push run-log line` · `run-gates run-log line` · `runlog record schema` · `python resolver (behaviour + inline parity + idiom ban)` · `unattended kit gate` · `pass-order history` · `brief-recorded` · `spawn budget (forks per hot entrypoint)` · `playbook render selftest` · `govkit acceptance matrix` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/memory-tree/routed_commits.py · covers AC2 · its AC2 arms re-run through the re-pointed reader, the failing case staged by passing `replace` · none
New arm: tools/lib/resolve-python.test.sh · covers AC5 · the `commit_trailers_py` parity row, its failing case staged by a one-byte edit to the runlog copy · none

## 8. Open questions

- **FACT-QUESTION · F1 — The brief gives this spec's status header the token `DRAFT`; is that a legal
  status?** Probe: `STATUS_TOKENS` at `tools/memory-tree/tree_lib.py:27`. Observation, 2026-10-24:
  `DRAFT` is not in the tuple. Liveness: the tuple would carry it if the vocabulary admitted it.
  RESOLVED (agent, 2026-10-24, delegated): `OPEN`, rung 2. widens: none · relaxes: none
- **F2 — Where are `Gov-Transition` and `Gov-Policy` registered, keys that carry a value and no edge?**
  Options: (a) `[[trailer]]` rows with no `type`, beside PLAY-dOrderedCharter-28's; (b) a constant in
  the reader; (c) a row typed with an existing edge. (b) splits the key register into two places and
  (c) types a transition as an edge it is not. RESOLVED (agent, 2026-10-24, delegated): (a), rung 3, one
  table for every key, shared interface I7's "all registered with the `commit` kind". widens: none ·
  relaxes: none
- **FACT-QUESTION · F3 — Which product files read the `Pass:` trailer?** Probe: `git grep -n
  "key=Pass\|interpret-trailers" -- tools skills .githooks` and the callers of
  `routed_commits.read_routed_commits`, reading each hit. Observation, 2026-10-24: seven product sites,
  the table of §4, beside two test suites. Liveness: a reader using git's trailer parse shows the key.
  RESOLVED (agent, 2026-10-24, delegated): all seven re-pointed, rung 2; the clause's "the three" are
  named among them. widens: none · relaxes: none
- **F4 — One canonical in Python, or one per language?** Options: (a) Python only, the shell readers
  calling its CLI; (b) Python and shell canonicals held to one answer, as the remote ladder is. (b) keeps
  two implementations of one rule. RESOLVED (agent, 2026-10-24, delegated): (a), rung 3, the clause's
  "one reader". widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, from the packet's Items 23, the brief's shared interface I7,
  scout B's row for cl-0108, PLAY-dOrderedCharter-28 S2 and S5, and the readers read at base `ed497191`.

## 10. Reuse audit

The seams extended are PLAY-dOrderedCharter-28's `[[native]]` and `[[trailer]]` tables and the
canonical-copy pattern of `remote_ladder_py` (`tools/lib/resolve_remote.py:16-68`, its copy at
`tools/runlog/model.py:622-674`, its row in `tools/lib/resolve-python.test.sh:168`). `python
tools/codebase-map/reuse_lookup.py "read commit trailers with one parser offering union and replace
attribution views"` ranked `read`, `read_text`, `parse` and `build_commit` (name stems) and named no
trailer seam. Scout B listed four readers; source shows seven product sites, the extra three being
`deviation_join.py:327-331`, `check-unattended.sh:4219` and `read_newest_unit`, recorded as F3. The
recall probe returned scout B's row and the night-pass instrument's quotation of the clause, neither in
disagreement with source.

Recall terms used: `python tools/memory-recall/query.py "how do the two Pass trailer readers disagree on attribution" --terms "Pass trailer union replace read_attribution_tokens routed_commits Decided read_git_range attribution view"`
