# TOOL-aMendedFleet-25 — live specs carry a declared byte ceiling, and a spec already over it is held at its recorded high-water

**Status:** CLOSED · rev-3 · 2026-10-04 · node a · Tier-2 · base 7af5f564 · streams tooling · ratified 2026-10-04 · order 25

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-04-build-TOOL-aMendedFleet-25-1-acceptance-ledger.md](../build/2026-10-04-build-TOOL-aMendedFleet-25-1-acceptance-ledger.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

A spec has no size bound. A unit builder re-reads its current spec whole at every pass boundary
(the build method's M7, step 4), so a spec's bytes are a read cost paid once per pass, and nothing
prices them: the largest tracked spec is 156,459 bytes against a median of 17,121. This unit gives
every LIVE spec a byte ceiling DECLARED in the same file that declares the charter template's, and
prices growth the way the template's gate does: a spec already over the ceiling when this lands is
held at its recorded high-water, so it may shrink and may not grow.

## 2. Scope (IN)

- **S1** — `tools/template-size-limits.txt` gains one CLASS row, key `memory/builds/*/spec/`, value
  49152, under a comment block giving the derivation and stating that the key is a class label no
  measured file's key equals, so `tools/check-template-size.sh` never reads it. Observed by AC1, AC6.
- **S2** — `tools/check-spec-tokens.py` gains an eighth join, `size`. Its population is the
  checker's existing LIVE population, so a terminal spec is never measured. Each spec is measured in
  bytes with carriage returns stripped, which is how `tools/check-template-size.sh` measures. A spec
  over the class ceiling and not held by S3 is a hit whose token is the composite `size <- <path>`,
  so a waiver row on the bare path neither swallows it nor reads stale because of it. Observed by AC2.
- **S3** — A spec over the ceiling is HELD when `tools/template-size-highwater.txt` carries a row
  keyed by its exact path and its size does not exceed that row. Over its row, it is a hit naming the
  recorded figure and the measured one. Observed by AC3.
- **S4** — A high-water row whose key sits under `memory/builds/` and names anything but a live spec
  over the ceiling is STALE and reds, with the line naming the row and why: untracked, terminal, or
  back under the ceiling. That is the rule the checker already applies to a waiver row no hit uses.
  Observed by AC4.
- **S5** — The join prints one line on every run naming the ceiling and where it was read, the
  graded count, the largest unheld spec with its size, and the held count. The line carries the text
  `live spec(s) ·`, which the unattended driver's refusal diagnosis already filters on, so it cannot
  crowd a real hit out of that diagnosis. With no class row the line says the arm is off and the
  checker exits as before; a class row whose value is not a number REFUSES. Observed by AC1, AC5.
- **S6** — The five live specs over 49152 bytes at landing each get a high-water row, written by
  the template gate's own writer, `bash tools/check-template-size.sh --bump <spec> 1048576`. The
  explicit limit is required because that gate's over-budget branch exits before its bump branch.
  Observed by AC1.
- **S7** — The checker's docstring gains a `size` entry in its join list, stating what the join
  does not check, and the limits file's header gains one paragraph on CLASS rows. Observed by AC6.
- **S8** — `tools/check-spec-tokens.test.sh` gains one arm, named under §7 `New arm:`.
  NOT OBSERVED by a pass: the suite is a self-test the close runs, and a pass runs none.
- **S9** — `memory/map/generated/symbols.json` is regenerated for the two new definitions, in the
  same commit. NOT OBSERVED by a criterion here: `python tools/codebase-map/gen_map.py --check` at
  the close is its check, and §7 names the leg that reads it.

## 3. Non-goals (OUT)

- Moving the review corpus's recurring spec-shape finding classes into this checker or into hygiene
  check 12. The synthesis bundled it with this point; it is a different mechanism with its own
  staged breaks, and the close files it as an ask.
- Measuring a terminal spec. A landed record is frozen, and this checker never rewrites one to
  clear a hit. Of the specs over 49152 bytes, all but five are terminal.
- A line cap. The template gate prices bytes only, and so does this.
- A conf key, a dated cutoff or a kit surface. Unit 21 of this build prices every new cutoff key,
  and both the checker and the two sidecar files are exemptions in `tools/govkit/registry.toml`,
  so an adopter receives none of this.
- Pricing growth of a spec under the ceiling. It is free until it reaches the ceiling; the report
  line names the largest such spec so the tail stays visible.

### Edges

none

## 4. Design

### Evidence

Read at base `7af5f564`; none of the files below moved between it and `580dc980`.

- `tools/check-template-size.sh` measures ONE subject per invocation, CR-stripped. Its ceiling
  resolves positional, then the declared row keyed by the repo-relative path, then the environment,
  then 49152. Its high-water half is advisory: a subject past its recorded row prints a WARN line,
  and `--bump` rewrites that subject's row and re-sorts the file. Its over-budget branch exits before
  the bump branch, which is why S6 passes a limit.
- `tools/template-size-limits.txt` carries five per-file rows with their history above each, and
  states that a person writes it; `tools/template-size-highwater.txt` carries five rows and is
  written by `--bump`. `tools/govkit/registry.toml` exempts both files and `tools/check-spec-tokens.py`
  as gov-only, so the join reads gov's own files from gov's own tool root.
- `tools/check-spec-tokens.py` defines LIVE as OPEN, SPECCED, INPROGRESS or BLOCKED, refuses an empty
  population, prints one line per join on every run, and treats a waiver row nothing produces as
  STALE. Its waiver registry, `memory/project/spec-token-waivers.txt`, states that its count may fall
  and never rise.
- Measured over `git ls-files` with carriage returns stripped: 901 specs, median 17,121 bytes, 90th
  percentile 46,302, largest 156,459, all terminal at the top. 68 specs are live; 11 exceed 32,768
  and 5 exceed 49,152. PINNED, measured 2026-10-04 at `580dc980`; AC1's line derives the live
  figures from then on.

The five live specs over 49152 bytes at base:

| bytes | status | spec |
|---:|---|---|
| 80139 | SPECCED | `memory/builds/aMendedLedger/spec/units/2026-08-10-spec-aMendedLedger-8-u9-driver-redesign.md` |
| 63810 | INPROGRESS | `memory/builds/aQuarriedLantern/spec/2026-08-03-spec-aQuarriedLantern-1.md` |
| 62695 | SPECCED | `memory/builds/aMendedLedger/spec/units/2026-08-09-spec-aMendedLedger-7-u8-keyed-corpus.md` |
| 59692 | INPROGRESS | `memory/builds/dPolishedVitrine/spec/2026-09-12-spec-TOOL-dPolishedVitrine-1.md` |
| 49730 | SPECCED | `memory/builds/aMendedLedger/spec/units/2026-08-09-spec-aMendedLedger-5-u5-merge-driver.md` |

### Mechanism

`read_size_ceilings` reads the two sidecar files from the directory holding the leg manifest the
checker already derives, so a fixture tree that supplies its own manifest supplies its own sidecars
too. It returns the class ceiling, or nothing when the class row is absent, and the high-water rows
as a path-to-bytes map. It parses each file the way the template gate does: tab-separated, comment
and blank lines skipped, the value stripped of whitespace.

`scan_spec_sizes` walks the live specs the checker already selected. Its hits join the existing
waiver pass unchanged. Its stale rows join the existing stale list, so one exit decision covers
both. No glob matching is needed: the class row is a label, and class membership is the checker's
own population test.

```
spec-tokens: size join · 68 live spec(s) · ceiling 49152 from tools/template-size-limits.txt · largest unheld 48652 B <path> · 5 held at a recorded high-water
spec-tokens: size join · 68 live spec(s) · no class row in tools/template-size-limits.txt (arm off)
```

### Inventory

- `read_size_ceilings` and `scan_spec_sizes` in `tools/check-spec-tokens.py`, cell `py.function`.
  `python tools/lexicon/lexicon.py --suggest` answered OK for both on 2026-10-04.
- The class row in `tools/template-size-limits.txt`, and five path rows in
  `tools/template-size-highwater.txt`.

### Files touched (estimate)

- `tools/check-spec-tokens.py`
- `tools/check-spec-tokens.test.sh`
- `tools/template-size-limits.txt`
- `tools/template-size-highwater.txt`
- `memory/map/generated/symbols.json`

### Rollout

The class row, the five high-water rows and the join land in one commit, so the `spec tokens` leg
is green on landing. Another build that later grows one of the five, or closes it, meets the join
like any other change; S4's stale rule is what makes a closed one's row go.

### Alternatives rejected

- **A class mode in `tools/check-template-size.sh`.** It measures one subject per invocation and
  knows no spec status, so it would need the status grammar copied into a generic size gate. It
  would also cost one bash process per live spec on every bar.
- **A spec class in hygiene check 6.** That needs a kit conf key every adopter receives, which M3's
  veto 2 discards without an owner turn, and check 6 does not read a spec's status.
- **Waiver rows for the five.** The waiver registry states that its count never rises, and a
  waiver holds no figure, so a waived spec could double unnoticed.
- **A dated cutoff instead of holding the five.** It adds a cutoff key, which unit 21's budget
  refuses, and it leaves the five free to grow.

## 5. Production-readiness checklist

- security — N/A: reads tracked files the checker already reads, plus two tracked text files; no
  new write path, since S6 uses the template gate's existing writer.
- perf / scale — one read per live spec, already read by the other joins; seconds on a 180 s leg.
- error / empty / loading states — no class row is an announced OFF; a non-numeric class row or
  high-water row refuses; an empty live population already refuses.
- observability — S5's line on every run, and every hit names its figures.
- risks — a held spec's owner cannot grow it in a fold; the remedy is to split the spec or move
  history out, and the owner may raise one row by hand in a reviewed diff.
- testing — direct runs on the tree and in a scratch clone, plus the S8 arm.
- migration — S6's five rows; nothing else.
- user docs — the checker's docstring and the limits file's header.

## 6. Acceptance criteria

- **AC1** — When `python tools/check-spec-tokens.py` runs on the tree after the pass, it exits 0
  and prints the size join's line naming ceiling 49152 from `tools/template-size-limits.txt`, a live
  count equal to the count on its own summary line, and 5 held specs.
  Red when: the line is absent, its count disagrees with the summary line, or a seeded spec reds.
  figure: the live count DERIVED at observation time; the five PINNED at `580dc980`.
- **AC2** — When, in a `git clone --local` of the unit's branch under `%TEMP%`, one live spec under
  the ceiling is padded past 49152 bytes and committed as the staged break,
  `python tools/check-spec-tokens.py` exits 1 and names `size <- ` followed by that spec's path.
  Red when: it exits 0, or the hit does not name the path.
- **AC3** — When, in that clone, one line is appended to
  `memory/builds/aMendedLedger/spec/units/2026-08-10-spec-aMendedLedger-8-u9-driver-redesign.md`,
  the checker names it with its recorded high-water and its new size; with the line taken back out,
  the hit is absent. Red when: the grown held spec passes.
  fixture: that spec is SPECCED at base; if it is terminal at build time, take any held spec.
- **AC4** — When, in that clone, that spec's status token is flipped to CLOSED, the checker exits 1
  with a STALE line naming its row in `tools/template-size-highwater.txt` and the reason terminal.
  Red when: the run passes with the row still present.
- **AC5** — When, in that clone, the class row is deleted from `tools/template-size-limits.txt`,
  `python tools/check-spec-tokens.py` prints the arm-off line and reports no size hit; when the row's
  value is set to a non-number, it prints a REFUSING line and exits 1.
  Red when: the absent row is silent, or the non-number is read as zero or as off.
- **AC6** — When `bash tools/check-template-size.sh` runs after the pass, it prints the same
  `template-size OK` line it prints at base, and `grep -n "spec/" tools/template-size-limits.txt`
  shows the class row under its comment block.
  Red when: the class row changes the template gate's verdict or line.

## 7. Gates

`spec tokens (a spec's own names resolve)` · `spec-tokens self-test` · `template size <=48KiB` · `template size gate selftest` · `lexicon naming predicates` · `kit epoch (shipped bytes move, the version moves)` · `python resolver (behaviour + inline parity + idiom ban)` · `push-main self-test` · `check-wiring self-test` · `settings-merge selftest` · `run-gates canary` · `run-gates evidence` · `foreign-prefix parity (every self-test at three prefixes)` · `install-prefix self-test` · `dead-path carriers self-test` · `kit-placeholders self-test` · `codebase-map coverage + freshness` · `recall floor` · `recall floor arms`

The last three are owed by S9's regenerated map artifact. Every other leg past the first six is owed by the tool-root guard, which the checker excludes as broad;
they are named so the close reads one list.

New arm: tools/check-spec-tokens.test.sh · a fixture tree with a class row, a padded live spec, a held spec grown by one line and a stale row for a terminal spec, staged red by skipping the size join · none

## 8. Open questions

- **F1 — Where does the join live?**
  Options: a class mode in the template gate; a spec class in hygiene check 6; an arm of the spec
  token checker. §4's alternatives give the reasons the first two lose; the checker already selects
  the live population, reports per join and owns a stale rule.
  RESOLVED (agent, 2026-10-04, delegated): an eighth join of `tools/check-spec-tokens.py`.
- **F2 — How are the live specs already over the ceiling admitted?**
  Options: waiver rows; a dated cutoff; per-path rows in the high-water file. Waiver rows break the
  registry's stated count rule and hold no figure; a cutoff is refused by unit 21's budget and leaves
  growth free. A high-water row is the template's own mechanism and freezes the figure.
  RESOLVED (agent, 2026-10-04, delegated): per-path high-water rows written by `--bump`.
- **F3 — What is the ceiling?**
  Options: 32768, which holds eleven live specs; 49152, which holds five; the largest live spec,
  which holds none and bounds nothing. 49152 is the charter template's own ceiling, so no spec costs
  more to re-read than the ruleset, and it reaches the tail without touching the median.
  RESOLVED (agent, 2026-10-04, delegated): 49152 bytes.
- **F4 — Does a stale high-water row red?**
  Options: red; report in the listing only. A row left for a closed spec hides nothing, but it is
  rot in a file a person reads, and the checker reds a stale waiver row for the same reason.
  RESOLVED (agent, 2026-10-04, delegated): red, as a stale waiver does.

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft, from the template gate, its two sidecar files, the spec token
  checker at base, and a CR-stripped size census of every tracked spec.
- rev-2 · 2026-10-04 · S9 · §4 · §7 · M2 cross-read: the two functions this unit adds to
  `tools/check-spec-tokens.py` move `memory/map/generated/symbols.json`, which units 18, 70 and 82
  regenerate and declare for their own definitions; this spec omitted the write, its Files touched
  row and the legs it owes.
- rev-3 · 2026-10-04 · §4 · built: the arm-off line in §4 Mechanism ended `live spec(s)` with no
  ` ·` after it, so it did not carry the text S5 requires and `--dispatch` would not filter it;
  the count moves ahead of the arm-off clause, as in the armed line.

## 10. Reuse audit

The seam is the template gate's declared-ceiling-and-high-water pair: `tools/template-size-limits.txt`
takes the class row and `tools/template-size-highwater.txt` takes the held rows, written by the
existing `--bump` of `tools/check-template-size.sh`, so no second writer exists. The grading half
extends `tools/check-spec-tokens.py`, whose LIVE population, waiver pass and stale rule it joins.
`python tools/codebase-map/reuse_lookup.py "cap the byte size of a document against a declared ceiling and a recorded high-water"`
returned only name-token neighbours in other kits and printed `unscanned layers: .sh`, so it could
not see the shell gate; read in source, the gate is the seam, and the dossier
`memory/map/features/playbook.md` names its subject resolution as the reuse point for gating any
file's bytes. Recall returned `TOOL-dFoldedVerdict-7`, an ask proposing to price a carrier's growth
against a recorded high-water the way that gate does, and `TOOL-aHoistedPass-29`, which records that
no ratchet reads the limits file, so a later raise of a row is caught only by review. Where the
report and the tree disagree: the synthesis gave a median near 18 KB; the census gives 17,121 bytes
over all specs and 19,214 over the 501 dated since 2026-09-01.

Recall terms used: `python tools/memory-recall/query.py "was a byte ceiling or size cap on spec files ever proposed, set or rejected" --terms "spec byte ceiling size cap high-water ratchet template-size-limits check-template-size bump grandfather spec length budget"`
