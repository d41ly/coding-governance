# wave2 — lens: can the record-policing gates actually fail?

**Serves:** research TOOL-aScouredKit-1 TOOL-aScouredKit-2

## Verdict: CLEAN WITH FIXES

*Node `a`, 2026-08-30, at HEAD `66c4891c`. Every claim below was produced by running the tool and
reading its output; the probes ran in a throwaway clone at `C:/tmp/gp` so nothing in the worktree was
mutated. Where a check reds, the failing case was OBSERVED, not reasoned about.*

---

## 0. The short answer

The gates can fail. That is the good news and it is not a small one: I constructed minimal violating
inputs for eight checks across three gates and every one of them went red. The hygiene gate's own
meta-gate (`check-arms.py`) holds 23 of 23 `fail` branches ARMED in `check-memory-hygiene.sh` with
only three pinned rows corpus-wide, each carrying a written reason for why no fixture can reach it.
This is a suite that has, on the whole, been seen to fail.

The bad news is narrower and it is the mechanism behind the owner's felt drift: **every truth check
in the suite is a referential-integrity check.** They ask whether a named id resolves, whether a
named path is tracked, whether a generated region reproduces. Not one of them adjudicates whether a
sentence in a record is TRUE. A record can therefore assert anything at all about the tree and stay
green, provided every id and path it mentions exists. The newest build's own README does exactly
that, and the assertion it makes is false.

---

## 1. Enumerating the suite, and what each check adjudicates

The record-policing surface is three merge-bar legs in the `records` chunk of
`tools/gate-legs.json` (86 legs total; `records` holds 3), plus the `declarations` legs that police
the same tree.

`bash tools/memory-tree/check-memory-hygiene.sh` at HEAD: **exit 0, zero bytes of output, 18.2 s.**
`python tools/memory-tree/check-arms.py --check`: exit 0, silent.
`python tools/memory-tree/gen_build_index.py --check-format`: exit 0, advisories only.
`bash skills/session-kickoff/manifest-check.sh`: exit 0, zero bytes.

### SHAPE vs TRUTH, counted

Twenty-three numbered checks live in `check-memory-hygiene.sh` (1–12, 21, 22, 23 in the shell;
13–16 delegated to `corpus_ids.py`, 17–19 to `gotchas.py`, 20 to `row_grammar.py`).

| Class | Checks | What it decides |
|---|---|---|
| SHAPE — spelling, placement, size, grammar | 1, 3, 4, 5, 6, 7, 8, 11, 12, 20, 22, 23 | 12 |
| TRUTH — but only referential integrity | 2, 9, 10, 13, 14, 15, 16, 21, and the two stale-line guards | 9 |
| SEMANTIC FIDELITY — is the claim true | *none* | 0 |

Check 23's own header says this outright and to its credit
(`tools/memory-tree/check-memory-hygiene.sh:1128-1132`): "it reads SHAPE and COVERAGE … a green row
here is not evidence the unit was built correctly." Check 22 grades that a review states a verdict
token from a closed set, never that the verdict is right. Check 8 grades that a backlog row spells
exactly one status token, never that the status is current.

That gap is not a defect in any one check. It is the reason a repo can be green and still not know
what state it is in, and it is why finding F1 below survived a full bar.

### Permanently satisfied / inapplicable

- **Check 11** (`:739-745`) iterates `$TOMBSTONE_ROOTS`, which is `""` in `.memory-tree.conf:26`.
  The loop body is unreachable in this repo. It is declared inapplicable in the conf and in the
  check's own comment, so this is honest, not hidden — recorded for completeness only.
- **Checks 13–15** are behind `ORPHAN_ID_PIN` / `DEAD_PATH_PIN`, both `"0"` in the conf — armed and
  tight, not blank. Check 16 is structural and runs regardless. No blindness here.
- **Drift-audit signals 4 and 5** (`ledger_rows_contradicting_git`, `dangling_pointers_in_own_ledger`)
  both read `memory/project/in-flight/`, which does not exist — the sharded node ledger retired to
  `memory/archive/ledger/`. Signal 5 says `DEAD PROBE`; signal 4 says `empty by declaration`. Two
  probes over one absent directory reporting two different statuses is worth a raised eyebrow, but
  `memory/archive/ledger/README.md:68-72` documents exactly this and says the probe "goes live and
  scores again" if a tree keeps a ledger. **This is category (b)/(c), not drift. I am not filing it.**

### Does the golden harness cover every check?

`check-arms.py --report` discovers gates by predicate (a tracked `*.sh` that defines `fail() {`) and
requires each `fail` branch to have a POSITIVE assertion naming its own failure text in the sibling
`<stem>.test.sh`. Result at HEAD:

```
tools/memory-tree/check-memory-hygiene.sh   branches 23 (floor 20)   armed 23 (floor 20)
skills/session-kickoff/manifest-check.sh    branches 28 (floor 28)   armed 28 (floor 28)
tools/unattended/unattended.sh              branches 104 (floor 101) armed 101, pinned 3
… 8 gates total, pinned rows: 3
```

The population is `*.sh` only, by its own docstring. Checks 13–20 live in Python modules and are
therefore outside it; their arms come from `--selftest`, which is `subject = kit` and held off the
normal bar. That is the owner's 2026-08-23 ruling and I am not re-litigating it, but the consequence
is worth one sentence: **on a routine bar, nothing asserts that checks 13–20 can still fail.**

---

## 2. Observed failing cases — the checks that DO bite

All in the clone at `C:/tmp/gp`, restored between probes.

| Probe | Mutation | Result |
|---|---|---|
| check 23 | delete the `- AC4 …` line for `TOOL-aScouredKit-13` from the ledger | `HYGIENE check 23 FAILED — … TOOL-aScouredKit-13/AC4` |
| check 2 | repoint the README's prompts link at a nonexistent file | `HYGIENE check 2 FAILED — broken relative .md links` |
| check 9 | flip a spec's Tier in its status header | `HYGIENE check 9 FAILED — generated build index differs from a fresh render` |
| check 21 | change a `**Serves:**` id to `TOOL-aScouredKit-<a nonexistent seq>` | `HYGIENE check 21 FAILED — … naming an id that no spec in this tree defines` |
| check 6/7/8 | drain the `memory/backlog/TOOL.md` row from `curation-debt.txt` | all three red (see §5) |
| slot contract | append `## Bogus slot` to a BOUND build README | `build-index FORMAT — authored content outside the slot contract` (exit 1) |

Six checks, six observed reds. The suite is alive.

---

## 3. F1 — a FALSE record in the newest build, and no gate can see it

**`memory/builds/aScouredKit/README.md:51`**

> **Ids `-10` and `-16` through `-34` are NOT units and carry no spec.** They are the findings this
> run reported rather than built, each a row in `memory/backlog/TOOL.md` with its own measurement.

Three of the ids in that range are units, do carry specs, and are not backlog rows:

```
$ git ls-files memory/builds/aScouredKit/spec/ | grep -E '3[012]'
memory/builds/aScouredKit/spec/2026-08-30-spec-TOOL-aScouredKit-30.md
memory/builds/aScouredKit/spec/2026-08-30-spec-TOOL-aScouredKit-31.md
memory/builds/aScouredKit/spec/2026-08-30-spec-TOOL-aScouredKit-32.md

$ head -3 …-30.md
# TOOL-aScouredKit-30 — one derivation everywhere, and the dead pointer REPORTED
**Status:** CLOSED · rev-1 · 2026-08-30 · node a · Tier-1 · base 093730e4 · streams tooling+deployer

$ grep -c 'TOOL-aScouredKit-3[012]' memory/backlog/TOOL.md
0
```

The build's own records contradict the claim in two places:

- `memory/builds/aScouredKit/README.md:99` — the GENERATED units table carries
  `TOOL-aScouredKit-30` with a link to its spec, `Tier 1`, `CLOSED`, `rev-1`. Same for `-31` and
  `-32`. `README.md:83` says **17 unit(s)**.
- `memory/builds/aScouredKit/reviews/2026-08-30-review-TOOL-aScouredKit-1-spec-audit.md:47` —
  "`-30`, `-31` and `-32` are PROMOTED units", and its `**Serves:**` line lists all seventeen.

**How it got here.** The last records commit, `bfa90c33` ("the exclusion note gets a canonical
slot"), moved the note from inside the roster markers to a `Build-level rules` bullet AND widened its
range from `-16 through -26` to `-16 through -34` in the same edit. The widening swallowed the three
promoted units, which had been added at `13:49` by `--rescope --act add` after the closing loop went
NON-CONVERGENT (`memory/builds/aScouredKit/RUN.md:100-104`).

**Why nobody noticed.** The authored roster (`README.md:61-80`) lists 14 rows. The generated region
lists 17. One file, three unit counts — 34 in the `ids:` front-matter field, 17 in the generated
status line, 14 in the authored roster — and the gates are content with all three, because:

- `tools/unattended/check-unattended.sh:1802-1811` grades only that the `gen:build-units` MARKER PAIR
  is well-formed. It never compares the region's contents to anything.
- Hygiene check 9 regenerates the GENERATED regions and byte-compares. It does not read the authored
  half.
- `gen_build_index.py --check-format` grades the authored half's HEADINGS against a closed canon and
  its slot BYTE SIZES. It does not read a word of the prose inside a slot. (aScouredKit's
  `## Build-level rules` slot is 1471 B, past its 823 B high-water and under its 1800 B ceiling — an
  ADVISORY line, which is the only thing any gate has ever said about this paragraph.)

There is no check anywhere that compares `roster_ids` to `unit_ids_of`.

**Second false clause, same bullet.** `README.md:55` says "The roster region holds units only, which
is what `--plan` and the DoD read." `tools/unattended/unattended.sh:1668-1670` says the opposite of
the second half: "Authorization, the presence term and terminality read the GENERATED region … The
planned-but-unspecced question keeps the authored pair." `build-complete` calls `unit_ids_of`
(`:3108`), which reads `gen:build-units`. Only `--plan`'s `missing_units` term reads the roster.

**Repair.** The exclusion range should read `-10`, `-16` through `-29`, `-33`, `-34` — which is
exactly the set that has backlog rows (`git diff 14e21399..HEAD -- memory/backlog/TOOL.md` adds 17
aScouredKit rows plus 2 re-measurements of older ids). And `-30`, `-31`, `-32` belong in the roster
table as rows 15–17, since they are what the promotion produced.

---

## 4. F2 — the acceptance-ledger check is escapable by a token the same session writes

Check 23's population is CLOSED **Tier-2** specs dated at or after `ACCEPTANCE_LEDGER_CUTOFF`. The
Tier token lives in the spec's own `**Status:**` header and is authored by the run being graded.

**Observed, in three steps:**

1. Removed the `- AC4 …` evidence line for `TOOL-aScouredKit-13` from the ledger →
   `HYGIENE check 23 FAILED — a CLOSED unit numbers an acceptance criterion that no journal record
   evidences … TOOL-aScouredKit-13/AC4`.
2. Left the gap in place; edited `2026-08-30-spec-TOOL-aScouredKit-13.md`'s header from `Tier-2` to
   `Tier-1` → check 23's finding vanished; check 9 red instead (the tier is rendered into the units
   table).
3. Ran `python tools/memory-tree/gen_build_index.py --write` → **exit 0, zero output.** Green, with a
   real, unevidenced acceptance criterion on a closed unit.

Two edits and a regen. Both edits are ones a session makes for legitimate reasons every day.

**This is not hypothetical for this build.** aScouredKit graded 15 of its 17 units Tier-1 and 2
Tier-2. Every other multi-unit build in the post-cutoff corpus is the other way round:

```
dUnstalledConvoy  T2=20 T1=3     dScriptedRepeat  T2=13 T1=0
dCarriedReceipt   T2=11 T1=4     dFramedEntrypoint T2=7 T1=1
dTieredTribunal   T2=6  T1=2     aPrimedKeepalive  T2=5 T1=4
aScouredKit       T2=2  T1=15
```

I am NOT claiming those 15 tier calls are wrong — §8's Tier-1 definition plausibly covers most of
them, and the spec-audit record states the consequence openly
(`…-1-spec-audit.md:36-40`: "No multi-agent spec audit. §8 forbids one at Tier 1 and fifteen of these
units are Tier 1 … Stated as a gap rather than counted as coverage"). I am claiming that the tier
token is simultaneously (a) the selector for check 23, (b) the selector for the §8 review protocol,
and (c) authored by the run it exempts, with no second opinion anywhere in the loop. A build that
declares itself Tier-1 throughout buys itself out of both, silently, and this is the build in the
corpus where that happened most.

Corpus-wide, the forward-only cutoffs mean the newest rules grade a minority of the tree:

| Ratchet | graded | grandfathered |
|---|---|---|
| `SPEC_FORMAT_CUTOFF` 2026-07-15 | 386 / 388 | 2 |
| `STREAMS_CUTOFF` 2026-08-09 | 341 / 388 | 47 |
| `ACCEPTANCE_LEDGER_CUTOFF` 2026-08-20 | 155 / 388 | 233 |
| `FORK_MARK_CUTOFF` 2026-08-21 | 125 / 388 | 263 |
| `REVIEW_VERDICT_CUTOFF` 2026-08-22 | 92 / 223 reviews | 131 |

Each cutoff is documented in `.memory-tree.conf` with the measured retroactive red count and the
argument for forward-only, so this is by design and I am not filing it. It is context for how much a
green hygiene run actually covers on the three newest rules: roughly a third.

Same shape, one file over: `memory/project/readme-contract.txt` carries `exempt-pin: 66` against 13
bound rows — the heading canon and slot budgets bind **13 of 79** build READMEs. aScouredKit IS one
of the 13, which is why its `Build-level rules` slot was measured at all. The registry is a
declared, drained-one-build-at-a-time equality pin with its reasoning in its own header, so again:
context, not a finding.

---

## 5. F3 — the kickoff-manifest ratchet audits a population it lets the audited file choose

`skills/session-kickoff/manifest-check.sh` is one of the three `records`-chunk legs. Its check 5 —
"no unaudited watch drift", the only check in the gate that notices the manifest going stale — reads
its population from the `watch:` line INSIDE the manifest it is auditing
(`memory/guides/SESSION-KICKOFF.md:6`, 10 pathspecs today).

**Observed:**

```
$ sed -i '6s|^watch: .*|watch: README.md|' memory/guides/SESSION-KICKOFF.md
$ bash skills/session-kickoff/manifest-check.sh
exit=0            # zero bytes of output
```

Nine of ten watched paths deleted, including `tools/gate-legs.json`,
`coding-governance-agents.template.md` and `check-memory-hygiene.sh`, and the ratchet is silently
clean. Check 6 requires each surviving pathspec to match a tracked file and check 2 branch 7 refuses
an EMPTY list, so the effective floor is **one path**. There is no coverage floor, no comparison
against a prior list, and no notice.

Compare `check-arms.py`, which floors branch counts per gate in `ARMS_FLOORS` and reds when a gate's
armed count drops. The pattern exists in this repo; this gate does not use it.

Note also that `AGENTS.md` — the governing doc — sits in `verify-paths:` (which check 4 only asserts
is tracked) and NOT in `watch:`. This build changed `AGENTS.md` (`git diff 14e21399..HEAD -- AGENTS.md`,
5 insertions / 8 deletions) and the manifest was not re-audited. The changes are prose
deduplications that move no §B claim, so **no DoD violation here** — but the ratchet could not have
told us either way.

---

## 6. F4 — nine hygiene checks are held silently under `--staged`

`.githooks/pre-commit` runs the fast leg. Under `--staged`, `check-memory-hygiene.sh` holds check 21
branch 1 (`:674`), checks 13–16 (`:1073`), 17–19 (`:1088`), 20 (`:1098`) and 23 (`:1170`). Exactly
one of them says so:

```
$ git add memory/backlog/TOOL.md && bash tools/memory-tree/check-memory-hygiene.sh --staged
memory-hygiene: check 23 HELD under --staged — a corpus-wide join over every closed Tier-2 unit; …
exit=0
```

The file argues for the announcement in its own comment at `:1151-1152` — "A skip that prints nothing
is indistinguishable from a check that found nothing, which is this repo's named class; the line
below is what keeps a held check visible" — and then four sibling blocks in the same file do the
thing it refuses. `pop_guard` is also a no-op under `--staged` (`:188`).

Coverage does not move: the push boundary runs with `STAGED=0`. The cost is that a developer reading
a green pre-commit leg has no way to know that nine checks did not run.

---

## 7. F5 — the tree's largest live record has three checks switched off, and the note explaining why
names a line that has moved

`memory/backlog/TOOL.md` is listed in `memory/project/curation-debt.txt:42`, which
`check-memory-hygiene.sh:125` consults from checks 6, 7 AND 8. Draining that one row:

```
HYGIENE check 6 FAILED — memory/backlog/TOOL.md (198088B > 61440B; no line cap for this class)
HYGIENE check 7 FAILED — memory/backlog/TOOL.md:6 (1124 chars > 300)   [and :7 :8 :9 …]
HYGIENE check 8 FAILED — memory/backlog/TOOL.md:57
```

3.2× the byte cap, a run of rows over the 300-char line cap, and one real status-token fault. The
registry's own header is admirably honest about the blast radius and even predicts the check-8 red —
but it names the wrong line:

> `curation-debt.txt:41` — "Check 8 is NOT idle here - with the registry emptied it reds on line 34"

Measured at HEAD it reds on **line 57** (`- TOOL-aPromptedMandate-8 · CLOSED · …`). Line 34 today is
`- TOOL-dScriptedRepeat-12 · CLOSED · …` and passes. Almost certainly the same row displaced by the
23 rows prepended since the note was written, so the SUBSTANCE holds and only the number rotted —
which is precisely the "a value stated in prose beside the source that owns it" class `AGENTS.md`
§6 names. Low severity, trivially fixed by dropping the number.

Drift-audit's `live_backlog_rows_per_shard 233 / 4` is report-only, so nothing gates the growth
either. The record `AGENTS.md` tells every session to read first is the least-gated record in the
tree.

---

## 8. Not findings — checked and cleared

- **The acceptance ledger's factual claims hold.** `python tools/govkit/selftest.py` prints
  **1001** `ok` lines and exits 0, matching "1001 arms held". `python tools/govkit/govkit.py
  selfcheck` exits 0. `tools/govkit/registry.toml` has exactly **25** `[[entry]]` blocks, matching
  "the live 25-entry registry". The named arms exist:
  `tools/govkit/selftest.py:1080` (`AC-withheld: a leg differing from what the receipt recorded
  WITHHOLDS the manifest`), `:1135` (`AC-ordered`), `:2124` (`a target's own \`kits\` list is
  honoured by a no---kits plan`). The ledger's AC labels match both specs' numbering exactly
  (-11: AC1–AC5, -13: AC1–AC4). One transcription nit: the `-13` AC1 arm is quoted without its
  backticks around `kits`, so a grep of the ledger's string misses the arm on first try.
- **The spec-audit record's stated LIMITS are honest, and in one place it is the record that catches
  the README.** It says seventeen specs (true), fifteen Tier-1 (true), names `-30/-31/-32` as
  promoted units (true), and states plainly that no defect it found came from reading specs. Its
  Serves line binds all 17 ids, which is what makes the README's line 51 detectable at all.
- **Backlog row `TOOL-aScouredKit-22`'s falsifiable claim reproduces.** `grep -c "23"
  memory/HYGIENE.md` returns **0** at HEAD, exactly as the row states.
- **Check 5 of the manifest ratchet is correctly satisfied** despite `last-audit` naming
  `23a20ca6`: the re-stamp commit is `961c6e4c` (2026-08-29 12:17), a descendant of the only
  watch-touching commit in range, `d902165a`.
- **`memory/LIVE.md` correctly omits aScouredKit** (all units terminal), and check 9 gates it.
- **The recorded green** (`<git-dir>/gate-full-green`) names `bfa90c33`, two commits behind HEAD,
  inside `GATE_FULL_MAX_LAG=10` in `.githooks/pre-push:129`. A push would run scoped, by design.
  Nothing is red at HEAD: all three `records` legs and the arms meta-gate pass.
- **No gate is red at the tip.** `main` is `14e21399`; this branch is 16 commits ahead and unmerged.

---

## 9. What would close the gap

The suite already knows how to do everything it needs; the pieces are just not wired to each other.

1. One check comparing `roster_ids` to `unit_ids_of` per build README, with a declared exemption
   grammar for the deliberate case. Both functions already exist in `tools/unattended/unattended.sh`.
2. A `WATCH_FLOOR` in the manifest audit block, graded like `ARMS_FLOORS` — a count, or a required
   subset naming the gate manifest and the charter.
3. Four `printf` lines beside `:674`, `:1073`, `:1088`, `:1098`, copying `:1166`'s shape.
4. Drop the line number from `curation-debt.txt:41`.

None of them makes a shape check into a truth check, and none of them should try. What they do is
stop a record from contradicting a record three paragraphs below it without anything noticing.
