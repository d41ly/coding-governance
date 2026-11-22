# TOOL-dWitnessedBar-109 — the attribution check reads every agent trailer line of the message, not only git's final trailer block

**Status:** CLOSED · rev-1 · 2026-11-21 · node d · Tier-2 · base cdfbd1cf · streams tooling · order 51 · advances TOOL-dWitnessedBar-31

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md) | journal | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-54 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 TOOL-dWitnessedBar-58 TOOL-dWitnessedBar-59 TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-61 TOOL-dWitnessedBar-62 TOOL-dWitnessedBar-63 TOOL-dWitnessedBar-64 TOOL-dWitnessedBar-65 TOOL-dWitnessedBar-66 TOOL-dWitnessedBar-67 TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-71 TOOL-dWitnessedBar-72 TOOL-dWitnessedBar-73 TOOL-dWitnessedBar-74 TOOL-dWitnessedBar-75 TOOL-dWitnessedBar-76 TOOL-dWitnessedBar-77 TOOL-dWitnessedBar-78 TOOL-dWitnessedBar-79 TOOL-dWitnessedBar-80 TOOL-dWitnessedBar-81 TOOL-dWitnessedBar-82 TOOL-dWitnessedBar-83 TOOL-dWitnessedBar-84 TOOL-dWitnessedBar-85 TOOL-dWitnessedBar-86 TOOL-dWitnessedBar-87 TOOL-dWitnessedBar-88 TOOL-dWitnessedBar-89 TOOL-dWitnessedBar-90 TOOL-dWitnessedBar-91 TOOL-dWitnessedBar-92 TOOL-dWitnessedBar-93 TOOL-dWitnessedBar-94 TOOL-dWitnessedBar-95 TOOL-dWitnessedBar-96 TOOL-dWitnessedBar-97 TOOL-dWitnessedBar-106 TOOL-dWitnessedBar-107 TOOL-dWitnessedBar-108 TOOL-dWitnessedBar-110 |
| [2026-11-19-build-TOOL-dWitnessedBar-109-1-acceptance-ledger.md](../build/2026-11-19-build-TOOL-dWitnessedBar-109-1-acceptance-ledger.md) | journal | — |
| [2026-11-19-build-TOOL-dWitnessedBar-109-1-builder-return.md](../build/2026-11-19-build-TOOL-dWitnessedBar-109-1-builder-return.md) | journal | — |
| [2026-11-21-build-TOOL-dWitnessedBar-1-runlog-5a748574.md](../build/2026-11-21-build-TOOL-dWitnessedBar-1-runlog-5a748574.md) | journal | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-54 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 TOOL-dWitnessedBar-58 TOOL-dWitnessedBar-59 TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-61 TOOL-dWitnessedBar-62 TOOL-dWitnessedBar-63 TOOL-dWitnessedBar-64 TOOL-dWitnessedBar-65 TOOL-dWitnessedBar-66 TOOL-dWitnessedBar-67 TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-71 TOOL-dWitnessedBar-72 TOOL-dWitnessedBar-73 TOOL-dWitnessedBar-74 TOOL-dWitnessedBar-75 TOOL-dWitnessedBar-76 TOOL-dWitnessedBar-77 TOOL-dWitnessedBar-78 TOOL-dWitnessedBar-79 TOOL-dWitnessedBar-80 TOOL-dWitnessedBar-81 TOOL-dWitnessedBar-82 TOOL-dWitnessedBar-83 TOOL-dWitnessedBar-84 TOOL-dWitnessedBar-85 TOOL-dWitnessedBar-86 TOOL-dWitnessedBar-87 TOOL-dWitnessedBar-88 TOOL-dWitnessedBar-89 TOOL-dWitnessedBar-90 TOOL-dWitnessedBar-91 TOOL-dWitnessedBar-92 TOOL-dWitnessedBar-93 TOOL-dWitnessedBar-94 TOOL-dWitnessedBar-95 TOOL-dWitnessedBar-96 TOOL-dWitnessedBar-97 TOOL-dWitnessedBar-106 TOOL-dWitnessedBar-107 TOOL-dWitnessedBar-108 TOOL-dWitnessedBar-110 |
| [2026-11-21-build-TOOL-dWitnessedBar-109-widen-29.md](../build/2026-11-21-build-TOOL-dWitnessedBar-109-widen-29.md) | widen | — |
| [2026-11-19-prompt-TOOL-dWitnessedBar-109-build-brief.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-109-build-brief.md) | journal | — |
| [2026-11-21-prompt-TOOL-dWitnessedBar-109-promotion-brief.md](../prompts/2026-11-21-prompt-TOOL-dWitnessedBar-109-promotion-brief.md) | journal | — |
| [2026-11-21-prompt-TOOL-dWitnessedBar-109-promotion-spec-writer.md](../prompts/2026-11-21-prompt-TOOL-dWitnessedBar-109-promotion-spec-writer.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

The closing diff review's round 2
(`memory/builds/dWitnessedBar/reviews/2026-11-21-review-TOOL-dWitnessedBar-106-closing-diff-review-round2.md`)
confirmed findings 2, 6 and 9 as one item, H1, at HIGH. `check_message_attribution` picks the agent
trailers only from `git interpret-trailers --parse`, which reads the message's final trailer block.
Once any plain line follows the agent's `Co-Authored-By:` line, git sees no trailer block, the
function returns `none`, and `check_commit_message` admits the commit. The drifted `Opus 5.5` value
and a correct trailer that is not last both pass, which is the class check 49 exists to refuse.

This unit builds the skeptic's class-level fix, re-derived against the code at `34d3c3286`. The agent
lines are chosen by scanning the message as git will keep it, with the same rules the last-line
check uses, so the value check and the last-line check run whether or not git reads those lines as
trailers. Its left-shift gate is five refusal arms and a fixture arm in the unattended suite, a
self-checking attribution case set in `commit_trailers.py --fixture`, and the class recorded in the
bug-class catalogue.

## 2. Scope (IN)

- **S1** — `extract_message_lines(raw)`, a module-level function inside the `commit_trailers_py`
  block, placed directly above `check_message_attribution`. It returns the list of lines git keeps
  of a raw message, in order: the bytes decoded as UTF-8 with `replace`, split on `\n`, every CR
  taken out of each line, reading stopped at the first line `_SCISSORS` full-matches after
  `rstrip()`, and lines opening `#` or holding only whitespace left out. These are exactly the
  rules today's last-line loop applies (`tools/lib/commit_trailers.py@253aca4e:315-321`), moved
  into one function both scans read. Observed by AC1 and AC4.
- **S2** — `check_message_attribution(text, expected)` keeps its signature, its four states and its
  detail strings, and reads the message only through S1:
  1. `expected` empty is `unarmed`, as today.
  2. `key`, `value` and `address` are derived from `expected` as today.
  3. The agent lines are every line of `extract_message_lines(raw)` that matches
     `(?i)^<key>[ \t]*:` (§8 F2) and contains `address`. Each one's value is the text after its
     first `:`, stripped.
  4. No agent line is `none`, with today's detail.
  5. An agent value other than `value` is `refused`, with today's detail naming the first one.
  6. The last item of `extract_message_lines(raw)`, or `''` where it is empty, other than
     `expected` is `refused`, with today's detail. Else `ok`.

  The function makes no subprocess call (§8 F1). Its docstring states the rule above and its
  WHAT IT DOES NOT CHECK note names the three shapes §4 "What the scan does not read" lists.
  Observed by AC1 and AC4.
- **S3** — `--fixture` gains the attribution cases. `_ATTRIBUTION_FIXTURE` is a module constant
  beside `_FIXTURE`: the charter line `Co-Authored-By: Fx <fx@example.invalid>` and the six
  `(name, message, state)` cases §4 "The fixture cases" lists. `check_attribution_fixture()` runs
  `check_message_attribution` over each case and returns `(lines, failed)`: one line
  `commit_trailers: fixture · attribution · <name> · <state>` per case, a case whose state is not
  its planted one ending `· FAIL, the case plants <state>`, and `failed` its count. In `main`, the
  `--fixture` branch prints these lines after the commit lines and returns 1 where `failed` is
  not 0, else 0. The usage line of the module docstring in each of the three files reads
  `three planted commits, both views, and the attribution cases`. Observed by AC2.
- **S4** — The three files hold one block: S1 to S3 are written in
  `tools/lib/commit_trailers.py` and the block between its `# >>> commit_trailers_py` and
  `# <<< commit_trailers_py` markers is copied byte for byte into
  `tools/memory-tree/commit_trailers.py` and `tools/unattended/commit_trailers.py`, which the
  `commit_trailers_py` row of the parity table in `tools/lib/resolve-python.test.sh` holds.
  Observed by AC3.
- **S5** — The left-shift arms, in the `TOOL-dWitnessedBar-108 S10` block of
  `tools/unattended/unattended.test.sh` (`tools/unattended/unattended.test.sh@d85005ad:9772-9811`),
  the six arms §4 "The suite arms" states. The block's opening comment gains one sentence: against
  the parent each message whose agent line is followed by a plain line exits 0, and `--fixture`
  prints no attribution line. Observed by AC5.
- **S6** — The class record `memory/gotchas/trailer-parse-reads-only-the-final-block.md`, `kind:
  class`, not universal, its body as §4 "The class record" states, and `memory/gotchas/INDEX.md`
  re-rendered by `python tools/memory-tree/gotchas.py --write`. Observed by AC6.
- **S7** — The unattended dossier, `memory/map/features/unattended.md`, adds
  `trailer-parse-reads-only-the-final-block.md` to its `gotcha-classes` list, and
  `memory/map/generated/` is re-rendered by `python tools/codebase-map/gen_map.py --write`.
  Observed by AC7.
- **S8** — `help/tags.md`'s attribution sentence (`help/tags.md@8dda1028:264-267`) says the check
  reads a `Co-Authored-By:` line anywhere in the message, whether or not git reads it as a trailer.
  Observed by AC8.

## 3. Non-goals (OUT)

- Round 2's other items, M1, M2, L1, L2 and L3, which `TOOL-dWitnessedBar-110` takes. L1's
  whitespace rule for the last-line compare is that unit's, built over S1's list.
- `read_message_ids`, the `message` verb's reader of `Pass:`. It keeps git's parse on purpose: every
  reader of a committed `Pass:` trailer reads git's parse, and the hook reads it "as the close
  reads" it (`tools/unattended/unattended.sh#check_commit_message`). The attribution rule is a
  position rule, "ends with", which git's parse cannot answer. The class record names the
  distinction for any future trailer reader.
- A change to `tools/unattended/unattended.sh`. Its relay already maps exit 1 to `fail 49` with the
  verb's detail and exit 2 to an echoed line, and the details keep their wording.
- A correction of spec 108's §4 definition of the agent trailers. That spec is CLOSED and frozen;
  this spec's §4 and the function's docstring carry the corrected definition.
- A git trailer separator other than `:`, set through `trailer.separators`, and a `core.commentChar`
  other than `#`. Both stay in the docstring's WHAT IT DOES NOT CHECK note.
- A kit version bump. Versions are minted at landing (`3cecd39a0`).

This unit edits only the built code of CLOSED units, never their specs. `TOOL-dWitnessedBar-108`
built `check_message_attribution`, the `attribution` verb, the S10 arms and the help sentence
(`ddf65d6a6`). `TOOL-dDeclaredLoop-23` built the `--fixture` verb and `build_fixture` (`3d335c77b`).
Each was found by its `Pass:` trailer in `git log` of the file.

### Edges

- **hands-off** `TOOL-dWitnessedBar-110` — L1's trailing-whitespace rule for the last-line compare, and M2's `ATTRIBUTION unarmed` relay, both built over this unit's reader and suite block

## 4. Design

### Evidence

Read on 2026-11-21 at `34d3c3286`, the run branch's HEAD.

- `tools/lib/commit_trailers.py#check_message_attribution` builds `found` from the stdout of
  `git interpret-trailers --parse` (`tools/lib/commit_trailers.py@253aca4e:305-307`), returns
  `none` where no value names the address (`:309-310`), and runs the last-line loop only after
  (`:313-323`). It never reads `proc.returncode`.
- The block sits at `tools/lib/commit_trailers.py@253aca4e:112-411`, and at
  `tools/memory-tree/commit_trailers.py@8485bb36:110-409` and
  `tools/unattended/commit_trailers.py@97f03da5:110-409`. A `diff` of the three marker spans
  printed nothing on 2026-11-21.
- Probe, importing `tools/lib/commit_trailers.py` with the charter line
  `Co-Authored-By: Fx <fx@example.invalid>`: `Fx 2` then `see above`; `Pass: none`, `Fx 2`, a blank
  line and prose; the charter's line, a blank line and prose; each returned `('none', ...)`. With the
  charter line `Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>`, the `Opus 5.5` trailer
  then `see above` returned `none`. The charter's line last returned `ok`.
- Probe, git 2.54 (PINNED 2026-11-21, node d): `git interpret-trailers --parse` reads
  `Co-Authored-By : Fx <fx@example.invalid>` as the trailer `Co-Authored-By: Fx <...>`, reads a key
  in any case, and folds an indented continuation line into the value above it.
- `tools/unattended/unattended.sh#check_commit_message` runs the `attribution` verb, treats exit 0
  as admitted, builds `fail 49` from exit 1's detail, and echoes exit 2's line
  (`tools/unattended/unattended.sh@ca417ff0:15565-15584`).
- No suite, leg or selftest runs `commit_trailers.py --fixture` or reads its output: `git grep` for
  `commit_trailers` in `*.sh`, `*.py` and `tools/gate-legs.json` names only imports of
  `build_fixture` and `read_commits` in `tools/memory-tree/routed_commits.py#run_selftest`.
- The unattended suite's python is `_rkd_py` (`tools/unattended/unattended.test.sh@d85005ad:232`)
  and `HERE` is the suite's own directory, which holds the unattended copy.

### The fixture cases

The charter line is `Co-Authored-By: Fx <fx@example.invalid>`, written `<E>` below; every message
opens `s` and a blank line.

| name | message body after the blank line | state |
|---|---|---|
| `the charter's trailer last` | `Pass: none`, `<E>` | `ok` |
| `another value, then a plain line` | `Co-Authored-By: Fx 2 <fx@example.invalid>`, `see above` | `refused` |
| `another value, a blank line and prose` | `Pass: none`, the `Fx 2` line, a blank line, `later note` | `refused` |
| `the charter's trailer, a blank line and prose` | `<E>`, a blank line, `later note` | `refused` |
| `another value spaced before its colon, then prose` | `Co-Authored-By : Fx 2 <fx@example.invalid>`, `see above` | `refused` |
| `no agent trailer` | `Pass: none` | `none` |

### The suite arms

Each runs `run --check-commit "$CCM"` in the S10 block's fixture, whose charter names
`_fx_at`. A1, A2, A3 and A5 sit after the `admits a message carrying no agent trailer` arm
(`tools/unattended/unattended.test.sh@d85005ad:9796`) and before the AC11 arm.

- **A1** — `Co-Authored-By: Fx 2 <fx@example.invalid>` then `see above`: exit 1, and the output names
  `the trailer 'Co-Authored-By: Fx 2 <fx@example.invalid>' is not the charter's '$_fx_at'`.
- **A2** — `Pass: none`, the `Fx 2` line, a blank line and `later note`: exit 1, the same line.
- **A3** — `Pass: none`, `$_fx_at`, a blank line and `later note`: exit 1, and the output names
  `the message's last line is 'later note'`.
- **A5** — `Co-Authored-By : Fx 2 <fx@example.invalid>` then `see above`: exit 1, A1's line.
- **A6** — `"$_rkd_py" "$HERE/commit_trailers.py" --fixture`: exit 0, and the output names each of the
  six `fixture · attribution · <name> · <state>` lines of the table above.
- **A4** — after the moved-charter arm (`:9810`) and before `rm -f "$CCM"`, the fixture's
  `AGENTS.md` fact line is set to `Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>` and
  committed `--no-verify`. The message `Pass: none`, `Co-Authored-By: Claude Opus 5.5
  <noreply@anthropic.com>`, `see above` exits 1 naming `is not the charter's 'Co-Authored-By: Claude
  Opus 5 <noreply@anthropic.com>'`. It needs its own charter because the record's arm names that
  address, which `_fx_at` does not, so under `_fx_at` the message reads `none` and passes.

Against the parent, A1 to A5 each exit 0 and A6 finds no attribution line, so each is seen red
before the built reader lands.

### What the scan does not read

- A value folded onto an indented continuation line, whose address sits on the second line. The
  first line carries no address and is not an agent line; where the message ends there, the
  last-line check still refuses it.
- A separator other than `:` that `trailer.separators` adds.
- A `core.commentChar` other than `#`.

### The class record

Front matter: `name: trailer-parse-reads-only-the-final-block`, a `description` saying a reader
that selects trailers through `git interpret-trailers --parse` sees only the message's final
trailer block, so a trailer followed by any plain line reads as absent, `kind: class`,
`universal: false`. Sections `## Symptom`, `## Where it bit` (round 2's H1, citing the record by
path, and `tools/lib/commit_trailers.py`) and `## The fix` (scan the message as git keeps it where a
rule is about position or presence anywhere; keep git's parse where the rule is git's own trailer
meaning, as `Pass:` is). The fix section says it is gated by the attribution arms in
`tools/unattended/unattended.test.sh` and the `--fixture` cases, which is check 18's declaration,
and names `rule-stated-with-no-check-that-fails` and `refusal-branch-with-no-arm` as its siblings.

### Inventory

Minted: `extract_message_lines`, `check_attribution_fixture` and `_ATTRIBUTION_FIXTURE` in the
trailer reader's block; the class `trailer-parse-reads-only-the-final-block`. Each function opens
with a verb of `.lexicon.conf`'s VERBS table, `extract` and `check`, graded by the
`lexicon naming predicates` leg's function-name cell.

### Migration

None. The reader's states, exit codes and details keep their shape. Reversible by reverting the
commit.

### Rollout

Order 51. `TOOL-dWitnessedBar-110` edits the same three files and the same suite block, so this unit
builds first and that one over its landed shape. The pass writes this unit's acceptance ledger with
AC5 owed to the close. The pass commit ends with the charter's trailer and nothing after it.

### Files touched (estimate)

- `tools/lib/commit_trailers.py`, `tools/memory-tree/commit_trailers.py`,
  `tools/unattended/commit_trailers.py`
- `tools/unattended/unattended.test.sh`
- `help/tags.md`
- `memory/gotchas/trailer-parse-reads-only-the-final-block.md`, new
- `memory/gotchas/INDEX.md`, re-rendered by `gotchas.py --write`
- `memory/map/features/unattended.md`
- `memory/map/generated/`, re-rendered by `gen_map.py --write`
- `memory/builds/dWitnessedBar/build/`, this unit's acceptance ledger
- `memory/builds/dWitnessedBar/spec/2026-11-21-spec-TOOL-dWitnessedBar-109.md`, its status header
- `memory/builds/dWitnessedBar/RUN.md`
- `memory/builds/dWitnessedBar/README.md`, `memory/backlog/TOOL.md` and `memory/LIVE.md`, rendered by
  `gen_build_index.py --write`

No path above is on the kickoff manifest's `watch:` line in `memory/guides/SESSION-KICKOFF.md`.

### Alternatives rejected

- **The finder's instance fix: refuse when git's parse finds no block.** A message with no agent line
  at all would then refuse, and a commit with no agent trailer is admitted by design.
- **Run git's parse on a copy with the trailing lines cut.** Which lines to cut is the question the
  raw scan answers directly, and the cut would be a second rule beside the last-line loop.
- **A shell scan in `check_commit_message`.** The kit reads trailers through the one reader, and a
  second scan would be a second rule.

## 5. Production-readiness checklist

- security — no new write path; the reader reads a message file and the charter, and the arms write
  under their scratch roots.
- perf / scale — one subprocess fewer per bound commit; the scan is linear in the message.
- error / empty / loading states — an empty message has no agent line and reads `none`; an
  unreadable message file still exits 2.
- observability — every refusal names the found and the expected value or the last line; a fixture
  case that disagrees names its planted state.
- risks — a body line opening `Co-Authored-By:` that quotes another value with the charter's
  address is now refused. That is the record's rule: a line naming the address must carry the value.
- testing — AC1 to AC4 by probe in the pass; AC5 by reading in the pass and by the suite at the
  close; AC6 to AC8 by their commands.
- migration — none; reversible by revert.
- user docs — `help/tags.md`, S8.

## 6. Acceptance criteria

- **AC1** — `python tools/lib/commit_trailers.py attribution <msg> AGENTS.md`, over message files
  holding the five refusal shapes of §4 "The fixture cases" with `Claude Opus 5.5
  <noreply@anthropic.com>` in place of `Fx 2 <fx@example.invalid>` and the repository charter's
  line in place of `<E>`, prints `ATTRIBUTION refused` and exits 1 for each; the charter's line last
  prints `ATTRIBUTION ok`, and `Pass: none` alone prints `ATTRIBUTION none`, each exit 0.
  Red when: any refusal shape prints `ATTRIBUTION none`.
  fixture: message files under the run's scratch directory.
- **AC2** — `python tools/lib/commit_trailers.py --fixture` exits 0 and prints six
  `fixture · attribution ·` lines, each ending with the state §4's table plants. Run over a scratch
  copy of the built file whose `check_message_attribution` is the one at `34d3c3286`, it exits 1
  and prints `FAIL, the case plants refused` on the four cases the parent reads as `none`.
  Red when: the fixture case set passes against the parent reader.
  figure: the six lines are PINNED by §4's table.
- **AC3** — `diff` of the spans between the `commit_trailers_py` markers of
  `tools/lib/commit_trailers.py` against each of `tools/memory-tree/commit_trailers.py` and
  `tools/unattended/commit_trailers.py` prints nothing.
  Red when: a kit copy keeps the parent reader.
- **AC4** — `python -c` with `inspect.getsource` over `commit_trailers.check_message_attribution`
  finds no `subprocess` and calls `extract_message_lines`, and its docstring names the
  continuation line, `trailer.separators` and `core.commentChar`.
  Red when: the agent lines are still chosen through git's parse.
- **AC5** — `grep -n 'see above\|later note\|fixture · attribution'` over the unattended kit's suite
  file names the six arms of §4 "The suite arms" inside the S10 block, each with the exit code and
  line it asserts.
  Red when: an arm's message carries a trailer as its following line, or the arm is absent.
  permission: the owner's standing instruction forbids a pass running this kit's suites; the main
  loop observes the arms RED against the parent and GREEN at the close.
- **AC6** — `python tools/memory-tree/gotchas.py --check` exits 0, and `grep -n
  trailer-parse-reads-only-the-final-block memory/gotchas/INDEX.md` names the class.
  Red when: the record is absent, declares no gate, or the index was not re-rendered.
- **AC7** — `python tools/codebase-map/gen_map.py --check` exits 0, and `grep -n
  trailer-parse-reads-only-the-final-block memory/map/features/unattended.md` names the claim.
  Red when: the class is unclaimed or `memory/map/generated/` was not re-rendered.
- **AC8** — `grep -n 'whether or not git reads it as a trailer' help/tags.md` names the attribution
  sentence.
  Red when: the page still reads the check as one over git's trailers only.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `recall floor` · `recall floor arms` · `python resolver (behaviour + inline parity + idiom ban)` · `lexicon naming predicates` · `codebase-map coverage + freshness`

The guard join over Files touched owes `recall floor` and `recall floor arms`, from the `memory/`
paths; every leg guarding the `tools/` paths is broad and out of the join. The resolver leg holds
the three copies' block parity, the lexicon leg grades the minted names, memory hygiene runs
`gotchas.py --check` over the class record, and the map leg grades the dossier claim. The first two
are the brief's. The `--fixture` cases are read by no leg except through A6.

New arm: tools/unattended/unattended.test.sh · covers AC5 · against the parent each of A1 to A5 reads `none` and exits 0, and A6 finds no attribution line · none
New arm: tools/lib/commit_trailers.py · covers AC2 · the parent's `check_message_attribution` in a scratch copy fails four cases · none

## 8. Open questions

- **F1 — What becomes of the `git interpret-trailers` call and its unread exit status?** Finding 9's
  fix treats a non-zero exit as exit 2. Options: (a) the scan needs no git parse, so
  `check_message_attribution` makes no subprocess call and that failure has no path; (b) keep the
  call beside the scan and map a non-zero exit to `unreadable`. (b) runs a process whose output no
  rule reads, which the charter's `[yagni]` rules out, and finding 5 found no path where the call
  alone fails. RESOLVED (agent, 2026-11-21, delegated): (a), rung 3, the clause holds with nothing
  left to fail open.
  widens: none · relaxes: none
- **F2 — Which key spelling is an agent line?** Options: (a) `(?i)^<key>:`, the record's pattern;
  (b) `(?i)^<key>[ \t]*:`, git's own key rule, which the §4 probe shows reads `Co-Authored-By :` as
  the trailer. (a) leaves that spelling followed by prose reading `none`, the same class.
  RESOLVED (agent, 2026-11-21, delegated): (b), rung 3, the most refusals of the class, with arm A5.
  widens: none · relaxes: none
- **F3 — Where is the fixture case read?** Options: (a) `--fixture` checks its planted states and
  exits 1 on a mismatch, and suite arm A6 runs it; (b) `--fixture` only prints, read by no one;
  (c) a new leg running `--fixture`. (b) is a case no gate reads, which the charter's `[gate]` rules
  out; (c) adds a manifest leg, which veto 2 parks. RESOLVED (agent, 2026-11-21, delegated): (a),
  rung 3.
  widens: none · relaxes: none
- **F4 — Does the class record land in this unit?** Options: (a) yes, with the index and the dossier
  claim, as `TOOL-aLightenedLoop-6` S10 landed its class records inside its promoted unit; (b) a
  separate unit, by M2's rule that a separate document is a separate unit. The record names the
  class entry as part of H1's left-shift gate, and (b) leaves that gate half built until another
  unit is specced. RESOLVED (agent, 2026-11-21, delegated): (a), rung 3, fewest follow-ups.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-21 · initial draft, promoted from the closing diff review's round 2 per
  2026-11-21-prompt-TOOL-dWitnessedBar-109-promotion-brief: H1, findings 2, 6 and 9.

## 10. Reuse audit

S1 and S2 extend the one trailer reader, `tools/lib/commit_trailers.py`, and S1 lifts the line rules
its own last-line loop already applies, so the agent scan and the last-line check read one list.
S3 extends the reader's existing `--fixture` verb beside `build_fixture`, and S5 extends the
`TOOL-dWitnessedBar-108 S10` block. `python tools/codebase-map/reuse_lookup.py "select a commit
message's agent trailer lines by scanning the raw message"` ranked `read_commits` of the trailer
reader among commit helpers on 2026-11-21 and no message-line scanner, so no existing seam fits S1
beyond the reader's own loop, which it extracts.

Recall terms used: `python tools/memory-recall/query.py "how is a commit message's agent trailer value and position checked when text follows the trailer" --terms "Co-Authored-By trailer interpret-trailers parse final block attribution last line scissors commit-msg check 49"`
