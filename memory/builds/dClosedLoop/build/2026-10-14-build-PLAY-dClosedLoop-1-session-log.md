# Session log — dClosedLoop: the kickoff card, every dispatch and its outcome, and where each record sits

**Serves:** research PLAY-dClosedLoop-1

Everything this build's sessions produce is kept in this folder, never only in a scratchpad (owner,
2026-10-14). This log holds what has no other home: the kickoff card as appended, each agent
dispatch and what became of it, events that changed the plan, and an index of the other records.

## Sessions

| Session | Node | Started | Outcome |
|---|---|---|---|
| `b73dcb0a-c6f8-44ce-865e-12f4b5031146` | d | 2026-10-14 14:01 +03:00 | Kickoff; manifest re-stamp `742957fcf`; build opened; five researcher handoffs rendered; four researchers dispatched and lost when the Claude Code process exited, the fifth never launched. |
| `1799cb98-0882-4ab8-a308-19495d2a487a` | d | 2026-10-14 | Resumed the build; owner note below; all five researchers re-dispatched from the same handoff files. |

## Owner notes

- 2026-10-14, session `1799cb98`: "One note, everything produced while working on the owner's task
  in this session - agent handoffs, suggestions, analysis, etc. must be saved in its build folder for
  future analysis, not lost in the scratchpad."

## The kickoff card, as appended in session b73dcb0a

The two kickoff questions and their answers are quoted in the brief,
`prompts/2026-10-14-prompt-PLAY-dClosedLoop-1-brief.md`. The card's startup lines are the
SessionStart hook's and are not repeated; its body was:

```text
## task
- **Title:** dClosedLoop — re-architect gov onto one loop: Plan → Design → Build → Test → Deploy → Maintain, plus Review at any stage
- **Goal (1–2 sentences):** Agree with the owner on a target architecture in which every kit, skill, hook, gate and record of gov serves a declared stage contract of one loop for concurrent, multi-node, agentic development, and record today's gaps against it. Then open the ordered chain of builds that converges the product onto it.
- **IN scope:** (1) a derived inventory of what ships and how the parts call each other, mapped onto the stages; (2) a gap register per stage plus cross-cutting concerns: Review, multi-node concurrency, role agents, owner use, adopter deployment, cost; (3) design rounds with the owner until principles, stage contracts (entry/exit artifacts, roles, gates, enforcement) and Review triggers are ratified, each answer recorded as made; (4) the architecture record and gap register under memory/builds/dClosedLoop/; (5) the declared spec audit of that record, folded; (6) the chain: one build per stage plus a convergence build, each README naming its stage, scope, predecessor, acceptance, decisions and a planned unit roster; (7) a recommended mapping of the 24 non-terminal builds onto the chain.
- **OUT / non-goals** (explicit cut-line): no product code — nothing under tools/, skills/, coding-governance-agents.template.md or WIRE-INTO-PROJECT.md, no AGENTS.md re-render; no unit specs for chain builds, their own sessions write them (owner, 2026-10-14); no status change to an existing build or ask; no adopter-repo work; no merge or push without the owner's explicit ask.
- **To-do:** (1) commit the manifest re-stamp in memory/guides/SESSION-KICKOFF.md; (2) open memory/builds/dClosedLoop/ with `spec-audit: 2026-10-14` and route the card to it; (3) inventory from the map dossiers, tools/gate-legs.json, hooks and guides, via a bounded read-only role fan-out writing to disk; (4) the gap register, file-cited; (5) present state and gaps, run the design rounds, record each ratified answer in memory/DECISIONS.md; (6) the architecture record; (7) audit it through tools/workflows/tier2-review.js and fold; (8) open the chain folders, gen_build_index.py --write, stage; (9) bar and commit; merge and push only on ask.
- **Reuse:** memory/map/ and tools/gate-legs.json as the derived inventory; tools/drift-audit/drift_report.py as gap evidence; memory/builds/aDeployScout/spec/governance-deployer-research.md for Deploy; memory/guides/BUILD-METHOD.md for Build; tools/workflows/tier2-review.js for the audit; tools/memory-tree/gen_build_index.py for opening builds and memory/LIVE.md.
- **Acceptance check:** (a) the ratified answers exist as decision rows tools/memory-recall/query.py returns; (b) the regenerated memory/LIVE.md lists every chain build as non-terminal, each README naming its stage and predecessor; (c) a join of the gap register against the chain READMEs shows every gap owned by exactly one build and every build owning a gap, seen red on a planted orphan first; (d) the audit report sits under memory/builds/dClosedLoop/reviews/ with every finding folded or rejected with a reason.
- **Gates it must pass:** per pass on the staged tree: kickoff-manifest ratchet, memory hygiene, build README slot contract, no stale generated output (`bash tools/run-gates/run-gates.sh --regen`); the full bar `bash tools/run-gates/run-gates.sh` before any landing.

## manifest
manifest-audit: delta last-audit and last-body-change advanced to ebce889c7 after re-reading §B against the 15 watched commits; no claim stale (tools/gate-legs.json gained two legs §B points at, never restates) · watch-commits-since-stamp: 4

## read
AGENTS.md · coding-governance-agents.template.md · .claude/rules/product.md · memory/DECISIONS.md · memory/guides/BUILD-METHOD.md · memory/guides/REVIEW-PROTOCOL.md · memory/guides/UNATTENDED-PROTOCOL.md · memory/HYGIENE.md · WIRE-INTO-PROJECT.md · memory/LIVE.md · memory/map/features/

## records
DEPL-aDeployScout-1 (govkit, awaiting owner approval) · TOOL-aWrittenMethod-1 · PLAY-aOrientedCast-2 · KICK-aOrientedCast-2 · TOOL-aMooredAnchor-1 · open asks: TOOL-aLevelledCopy-24 (HIGH), TOOL-aHonedRuleset-15, KICK-aHonedRuleset-1, KICK-aReplayedCard-5, TOOL-dDerivedDocket-60
Recall terms used: charter template kit govkit deployer bar legs build-method unattended roles kickoff spec lifecycle

## classes
fixture-passes-by-finding-nothing · guard-above-a-fold-makes-its-fallback-dead · heredoc-escape-reaches-the-regex · inline-fence-swallows-the-rest-of-the-file · staged-break-substitutes-a-synthetic-value · two-answers-to-one-question · a-merge-of-the-default-branch-read-as-additions · amendment-leaves-its-other-half-standing · ledger-token-wrapped-across-a-line-joins-nothing · allowlist-narrower-than-the-root-it-guards · conf-value-interpolated-into-a-regex · fold-text-is-unreviewed-surface · one-value-field-records-a-mixed-outcome · overlap-judged-from-the-invocation-interval · record-file-read-by-line-position · retirement-inventory-misses-readers-by-value

## open
spec audit: declared 2026-10-14 (owner) · chain depth: README plus unit roster (owner) · 24 non-terminal builds and 17 remote claims to map · 15 nonzero drift signals are Maintain-stage evidence

READY — dClosedLoop · node d · branch/gov-architecture-plan-e34297 · base ebce889c7 · Tier-2 · gates kickoff-manifest ratchet, memory hygiene, build README slot contract, regen, full bar before landing
```

## Dispatches

Each handoff file under `prompts/` holds the full prompt its agent was handed, the research question
included; the agent lines derived by `tools/roles/handoff.py agents` go to this build's agent ledger.

| # | Role | Stage | Handoff | Session | Outcome | Return recorded in |
|---|---|---|---|---|---|---|
| 1 | gov-researcher | Plan | `prompts/2026-10-14-prompt-PLAY-dClosedLoop-1-1-researcher.md` | b73dcb0a | lost: process exited | — |
| 2 | gov-researcher | Design | `prompts/2026-10-14-prompt-PLAY-dClosedLoop-1-2-researcher.md` | b73dcb0a | lost: process exited | — |
| 3 | gov-researcher | Build | `prompts/2026-10-14-prompt-PLAY-dClosedLoop-1-3-researcher.md` | b73dcb0a | lost: process exited | — |
| 4 | gov-researcher | Test | `prompts/2026-10-14-prompt-PLAY-dClosedLoop-1-4-researcher.md` | b73dcb0a | lost: process exited | — |
| 5 | gov-researcher | Deploy | `prompts/2026-10-14-prompt-PLAY-dClosedLoop-1-5-researcher.md` | b73dcb0a | never launched: the tool call returned an internal error | — |
| 6 | gov-researcher | Plan | handoff 1, unchanged | 1799cb98 | returned, 5m17s, 23.0k out | `build/2026-10-14-build-PLAY-dClosedLoop-1-research-plan.md` |
| 7 | gov-researcher | Design | handoff 2, unchanged | 1799cb98 | returned, 5m24s, 29.0k out | `build/2026-10-14-build-PLAY-dClosedLoop-1-research-design.md` |
| 8 | gov-researcher | Build | handoff 3, unchanged | 1799cb98 | returned, 4m39s, 24.0k out | `build/2026-10-14-build-PLAY-dClosedLoop-1-research-build.md` |
| 9 | gov-researcher | Test | handoff 4, unchanged | 1799cb98 | returned, 3m47s, 20.9k out | `build/2026-10-14-build-PLAY-dClosedLoop-1-research-test.md` |
| 10 | gov-researcher | Deploy | handoff 5, unchanged | 1799cb98 | returned, 4m08s, 22.6k out | `build/2026-10-14-build-PLAY-dClosedLoop-1-research-deploy.md` |
| 11 | gov-researcher | Orientation: routing and step | `prompts/2026-10-14-prompt-PLAY-dClosedLoop-1-6-researcher.md` | 1799cb98 | dispatched | — |
| 12 | gov-researcher | Orientation: cost | `prompts/2026-10-14-prompt-PLAY-dClosedLoop-1-7-researcher.md` | 1799cb98 | dispatched | — |
| 13 | gov-researcher | Orientation: trust | `prompts/2026-10-14-prompt-PLAY-dClosedLoop-1-8-researcher.md` | 1799cb98 | dispatched | — |
| 14 | gov-researcher | Orientation: determinism | `prompts/2026-10-14-prompt-PLAY-dClosedLoop-1-9-researcher.md` | 1799cb98 | dispatched | — |

Maintain, and the machinery by which the loop corrects itself, is researched by the main loop in
this session rather than by a sixth agent: the direct-spawn budget is five per owner turn
(`tools/hooks/agent-cap.js`, `CAP` and `SLOT_TTL_MS`). Its record is
`build/2026-10-14-build-PLAY-dClosedLoop-1-research-maintain.md`.

The lines `tools/roles/handoff.py agents --handoff <path>` derived for the five handoffs, verbatim.
The verb's `--write` held the agent ledger back, because no spec defines `PLAY-dClosedLoop-1` yet;
it is re-run once the spec lands. Rows 1 to 4 have no `returned` line: their process died.

```text
- agent — gov-researcher · effort medium · model claude-opus-5-5 · PLAY-dClosedLoop-1 · prompt [2026-10-14-prompt-PLAY-dClosedLoop-1-1-researcher.md](memory/builds/dClosedLoop/prompts/2026-10-14-prompt-PLAY-dClosedLoop-1-1-researcher.md) · writes none · gates none · run direct/aa7e3d6c065321e82
- agent — gov-researcher · effort medium · model claude-opus-5-5 · PLAY-dClosedLoop-1 · prompt [2026-10-14-prompt-PLAY-dClosedLoop-1-1-researcher.md](memory/builds/dClosedLoop/prompts/2026-10-14-prompt-PLAY-dClosedLoop-1-1-researcher.md) · writes none · gates none · run direct/adedd1eec07881ab6
- returned — gov-researcher · wrote 0 files · 5m17s · 23.0k out · run direct/adedd1eec07881ab6
- agent — gov-researcher · effort medium · model claude-opus-5-5 · PLAY-dClosedLoop-1 · prompt [2026-10-14-prompt-PLAY-dClosedLoop-1-2-researcher.md](memory/builds/dClosedLoop/prompts/2026-10-14-prompt-PLAY-dClosedLoop-1-2-researcher.md) · writes none · gates none · run direct/accff2d8daecc1566
- agent — gov-researcher · effort medium · model claude-opus-5-5 · PLAY-dClosedLoop-1 · prompt [2026-10-14-prompt-PLAY-dClosedLoop-1-2-researcher.md](memory/builds/dClosedLoop/prompts/2026-10-14-prompt-PLAY-dClosedLoop-1-2-researcher.md) · writes none · gates none · run direct/a0cce9c329c0c17d2
- returned — gov-researcher · wrote 0 files · 5m24s · 29.0k out · run direct/a0cce9c329c0c17d2
- agent — gov-researcher · effort medium · model claude-opus-5-5 · PLAY-dClosedLoop-1 · prompt [2026-10-14-prompt-PLAY-dClosedLoop-1-3-researcher.md](memory/builds/dClosedLoop/prompts/2026-10-14-prompt-PLAY-dClosedLoop-1-3-researcher.md) · writes none · gates none · run direct/a6e0851dac91f6647
- agent — gov-researcher · effort medium · model claude-opus-5-5 · PLAY-dClosedLoop-1 · prompt [2026-10-14-prompt-PLAY-dClosedLoop-1-3-researcher.md](memory/builds/dClosedLoop/prompts/2026-10-14-prompt-PLAY-dClosedLoop-1-3-researcher.md) · writes none · gates none · run direct/a5886ceb960724423
- returned — gov-researcher · wrote 0 files · 4m39s · 24.0k out · run direct/a5886ceb960724423
- agent — gov-researcher · effort medium · model claude-opus-5-5 · PLAY-dClosedLoop-1 · prompt [2026-10-14-prompt-PLAY-dClosedLoop-1-4-researcher.md](memory/builds/dClosedLoop/prompts/2026-10-14-prompt-PLAY-dClosedLoop-1-4-researcher.md) · writes none · gates none · run direct/af05ef0640a026274
- agent — gov-researcher · effort medium · model claude-opus-5-5 · PLAY-dClosedLoop-1 · prompt [2026-10-14-prompt-PLAY-dClosedLoop-1-4-researcher.md](memory/builds/dClosedLoop/prompts/2026-10-14-prompt-PLAY-dClosedLoop-1-4-researcher.md) · writes none · gates none · run direct/a636d8714b2045642
- returned — gov-researcher · wrote 0 files · 3m47s · 20.9k out · run direct/a636d8714b2045642
- agent — gov-researcher · effort medium · model claude-opus-5-5 · PLAY-dClosedLoop-1 · prompt [2026-10-14-prompt-PLAY-dClosedLoop-1-5-researcher.md](memory/builds/dClosedLoop/prompts/2026-10-14-prompt-PLAY-dClosedLoop-1-5-researcher.md) · writes none · gates none · run direct/aaf0e3ee001682096
- returned — gov-researcher · wrote 0 files · 4m08s · 22.6k out · run direct/aaf0e3ee001682096
```

## Events

- 2026-10-14, session b73dcb0a: the kickoff manifest failed checks 5 and 9; re-read §B, nothing
  stale, re-stamped in `742957fcf`.
- 2026-10-14, session b73dcb0a: the build folder was opened unregistered, and `gen_build_index.py
  --check-format` named the missing generated regions; registered in
  `memory/project/readme-contract.txt` and rendered with `--write`.
- 2026-10-14, session 1799cb98: the full memory-hygiene run reds check 21 on this build's records
  until the spec defines `PLAY-dClosedLoop-1`, which is expected, and check 23 on acceptance-ledger
  lines of `aSparedSpawn` and `aOrientedCast`, which this build did not write: Test-stage evidence.
- 2026-10-14, session 1799cb98: the context was compacted, and the session reoriented from this
  build's records and the card the compact hook re-rendered. Local main sits at `97e782d51`, four
  commits past this branch's base `742957fcf`: dTracedLedger traced check 23's 37 reds at
  `ebce889c7` and routed them to their owners as asks. `origin/main` is still `ebce889c7`.
- 2026-10-14, session 1799cb98: the owner ruled dLeasedFleet out of scope, with no build outside the
  chain counted on. The census found four reliances: dLeasedFleet itself, aOrientedCast's close,
  three more live builds' closes in the adopted mapping, and dScriptedRepeat's recipe mode. The
  coordination record moves leases, the mailbox and dependency coordination into dDeclaredLoop;
  the chain has ten builds.

## Instruments

### The gap-ownership join

The check behind acceptance (c), run first against the architecture records and, once the chain
opens, against the chain READMEs. It reads two files and writes nothing:

```python
"""Join the gap register's keys against architecture v1's chain table: every gap owned exactly once,
every chain build owning at least one. Reads both records; writes nothing. Ranges like
`gap-test-01 to gap-test-09` are expanded."""
import re
import sys

reg_path, arch_path = sys.argv[1], sys.argv[2]
with open(reg_path, encoding="utf-8") as fh:
    keys = [m.group(1) for m in re.finditer(r"^\| (gap-[a-z]+-\d\d) \|", fh.read(), flags=re.M)]
with open(arch_path, encoding="utf-8") as fh:
    arch = fh.read()

owners = {}
for line in arch.splitlines():
    m = re.match(r"^\| (d[A-Z][A-Za-z]+) \| [^|]+ \| [^|]+ \| [^|]+ \| (.+) \|$", line)
    if not m:
        continue
    build, cell = m.group(1), m.group(2)
    owned = set()
    for a, b in re.findall(r"(gap-[a-z]+-\d\d) to (gap-[a-z]+-\d\d)", cell):
        stem, lo, hi = a.rsplit("-", 1)[0], int(a.rsplit("-", 1)[1]), int(b.rsplit("-", 1)[1])
        owned |= {f"{stem}-{i:02d}" for i in range(lo, hi + 1)}
    owned |= set(re.findall(r"gap-[a-z]+-\d\d", re.sub(r"gap-[a-z]+-\d\d to gap-[a-z]+-\d\d", "", cell)))
    owners[build] = owned

count = {k: [b for b, s in owners.items() if k in s] for k in keys}
unowned = [k for k, bs in count.items() if not bs]
multi = {k: bs for k, bs in count.items() if len(bs) > 1}
phantom = sorted({g for s in owners.values() for g in s} - set(keys))
empty = [b for b, s in owners.items() if not s]
print(f"register keys {len(keys)} · chain builds {len(owners)}")
print("unowned:", unowned or "none")
print("owned twice or more:", multi or "none")
print("owned but not in the register:", phantom or "none")
print("builds owning nothing:", empty or "none")
sys.exit(1 if (unowned or multi or phantom or empty) else 0)
```

Runs, 2026-10-14:

| Against | Result |
|---|---|
| the register and architecture v1 | exit 0: 57 keys, 10 builds, none unowned, none owned twice, none phantom, none empty |
| the register with `gap-review-03` renamed `gap-review-99`, and v1 | exit 1: `gap-review-99` unowned, `gap-review-03` phantom |
| the register and architecture v2 | exit 0: 57 keys, 10 builds, the same four clean lines |
| the register with `gap-plan-07` renamed `gap-plan-99`, and v2 | exit 1 |

### The preset check

Checks architecture v2's `[presets]` table against its `[policies]` catalogue. It reads one file and
writes nothing:

```python
"""Check architecture v2's preset table against its policy catalogue: every presettable key assigned
in every preset, no excluded key present, every enumerated value allowed, and the `standard` column
equal to the catalogue's defaults. Reads one file; writes nothing; exit 1 on any finding."""
import re
import sys

text = open(sys.argv[1], encoding="utf-8").read()


def section(tag):
    m = re.search(r"^## \[" + re.escape(tag) + r"\].*?(?=^## \[|\Z)", text, flags=re.M | re.S)
    return m.group(0) if m else ""


def rows(block, ncols):
    out = []
    for line in block.splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) == ncols and cells[0].startswith("`"):
            out.append([cells[0].strip("`")] + cells[1:])
    return out


STAGES = ["plan", "design", "build", "test", "deploy", "maintain"]
EXCLUDED = {"floor", "policy.guard", "policy.proof", "preset", "charter.practices"}
catalogue = {}
for key, allowed, default, _src in rows(section("policies"), 4):
    keys = [key.replace("<stage>", s) for s in STAGES] if key == "review.<stage>" else [key]
    for k in keys:
        if key == "review.<stage>":
            d = "owed" if k == "review.build" else "opt-in"
        else:
            d = default
        catalogue[k] = (allowed, d)

presets = {r[0]: r[1:] for r in rows(section("presets"), 5)}
findings = []
expected = {k for k in catalogue if k not in EXCLUDED}
for k in sorted(expected - set(presets)):
    findings.append(f"presettable key missing from the preset table: {k}")
for k in sorted(set(presets) - expected):
    findings.append(f"preset table names a key that is excluded or not in the catalogue: {k}")

FREE = re.compile(r"hours|days|set of named|each cap|any subset|the role efforts|a repo-declared")
for k, vals in presets.items():
    if k not in catalogue:
        continue
    allowed_text, default = catalogue[k]
    if not FREE.search(allowed_text):
        allowed = {a.strip() for a in re.split(r"[,;]", allowed_text) if a.strip()}
        for name, v in zip(["velocity", "standard", "strict", "autonomous"], vals):
            if v not in allowed:
                findings.append(f"{k}: {name} = '{v}' is not an allowed value ({allowed_text})")
        if vals[1] != default:
            findings.append(f"{k}: standard = '{vals[1]}' but the catalogue default is '{default}'")

print(f"catalogue keys {len(catalogue)} · presettable {len(expected)} · preset rows {len(presets)}")
print("\n".join(findings) if findings else "no findings")
sys.exit(1 if findings else 0)
```

Runs, 2026-10-14:

| Against | Result |
|---|---|
| v2 as first written | exit 1: `hooks.bypass`'s catalogue default read "allowed, every use recorded", a note fused into the value |
| a copy with strict `leases` set to `sometimes` and standard `build.scope` set to `refuse` | exit 1, naming both planted defects |
| v2 with the catalogue cell corrected to `allowed`, the recording left to the floor | exit 0: 47 catalogue keys, 43 presettable, 43 preset rows, no findings |
| v2 after foundations step 1, with `EXCLUDED` gaining `"charter.practices"` in the source above (presets never touch the practice set) | exit 0: 49 catalogue keys, 44 presettable, 44 preset rows, no findings |

The gap-ownership join after foundations step 1, against the register (61 keys, the four owner-raised
`gap-found-*` rows added) and v2 (dOrderedCharter added as the root): exit 0, 61 keys, 11 builds,
none unowned, none owned twice, none phantom, none empty.

After step 1's continuation (`gap-found-05` owned by dOrderedCharter, `gap-found-06` by
dDeclaredLoop): the join exits 0 on 63 keys and 11 builds; the preset check exits 0 on 49 catalogue
keys, 44 presettable, 44 preset rows.

After the core consistency step (`gap-found-07` and `gap-found-08` owned by dOrderedCharter;
`core.bypass` and `core.exceptions` added to the catalogue and every preset): the join exits 0 on 65
keys and 11 builds; the preset check exits 0 on 51 catalogue keys, 46 presettable, 46 preset rows.
The four chain-row amendments were applied by a script that refused unless each old row matched
exactly once.

After the flow walk's Plan and Design stages (four `gap-flow-*` rows; `design.forks` and
`design.reentry` added; the preset `autonomous` renamed `guarded`, and the preset check's column
names updated to match): the join exits 0 on 69 keys and 11 builds; the preset check exits 0 on 53
catalogue keys, 48 presettable, 48 preset rows. The v2 amendments ran through a script that refused
unless each old text matched exactly once.

After the flow walk's Build, Test, Deploy, Maintain and Review stages and the flow-interactions round
(`gap-flow-05` to `gap-flow-09`; seventeen policies added in all since the Design stage): the join
exits 0 on 74 keys and 11 builds; the preset check exits 0 on 69 catalogue keys, 64 presettable,
64 preset rows.

After the owner's no-foreign-build directive (dLeasedFleet's row removed, its three gaps moved to
dDeclaredLoop): the join exits 0 on 74 keys and 10 builds; with `gap-flow-06` struck from
dDeclaredLoop's row and `gap-conc-01` added to dRankedPlan's in a copy, it exits 1 naming both; the
preset check exits 0 on 69 catalogue keys, 64 presettable, 64 preset rows, unchanged.

### The foreign-build census

Lists every build slug a design record names that is not a chain build, the chain read from v2's
chain table. It reads one or two files, writes nothing and judges nothing: whether a hit is counted
on is decided by reading it (the coordination record's `[audit]`), and a reliance worded without a
slug is invisible to it.

```python
"""List every build slug a design record names that is not a chain build, with the lines naming it.
The chain is read from the record's own chain table (rows `| dXxx | stage | parents | units | gaps |`)
plus dClosedLoop. Reads one file, writes nothing, judges nothing: whether a hit is counted on or only
cited as evidence is decided by reading it, and the census exits 0 either way."""
import re
import sys

path = sys.argv[1]
chain_src = sys.argv[2] if len(sys.argv) > 2 else path
with open(chain_src, encoding="utf-8") as fh:
    chain = {"dClosedLoop"} | set(re.findall(r"^\| (d[A-Z][A-Za-z]+) \| [^|]+ \| [^|]+ \| [^|]+ \| [^|]+ \|$",
                                              fh.read(), flags=re.M))
with open(path, encoding="utf-8") as fh:
    lines = fh.read().splitlines()
hits = {}
for n, line in enumerate(lines, 1):
    for slug in re.findall(r"\b[abcd][A-Z][a-z]+[A-Z][a-z]+\b", line):
        if slug not in chain:
            hits.setdefault(slug, []).append(n)
print(f"chain builds {len(chain) - 1} (+ dClosedLoop) · foreign slugs {len(hits)}")
for slug in sorted(hits):
    print(f"{slug}: lines {', '.join(str(n) for n in sorted(set(hits[slug])))}")
```

Runs, 2026-10-14:

| Against | Result |
|---|---|
| the six design records, before the directive's changes, chain from v2 | v2: aOrientedCast, dPolishedVitrine; walkthrough: aDeployScout, aOrientedCast, dNarrowedAnchor, dScriptedRepeat; flow: four evidence citations; flow interactions and foundations: none; v1: 24, all in the live-build mapping |
| v2 after the changes, its own chain of ten | dLeasedFleet only in the revision lines, and dPolishedVitrine in the mapping's Plan action |

## Records index

| Record | What it holds |
|---|---|
| `prompts/2026-10-14-prompt-PLAY-dClosedLoop-1-brief.md` | The owner's prompt, verbatim; the brief; the owner's confirmation; the route. |
| `prompts/2026-10-14-prompt-PLAY-dClosedLoop-1-{1..5}-researcher.md` | The five research handoffs, one stage each. |
| `build/2026-10-14-build-PLAY-dClosedLoop-1-session-log.md` | This log. |
| `build/2026-10-14-build-PLAY-dClosedLoop-1-research-{plan,design,build,test,deploy}.md` | The five stage researchers' returns, verbatim. |
| `build/2026-10-14-build-PLAY-dClosedLoop-1-research-maintain.md` | The main loop's Maintain research, with every instrument beside its output. |
| `build/2026-10-14-build-PLAY-dClosedLoop-1-gap-register.md` | The gaps, keyed, graded and evidenced, each owned by one chain build; the register derives its counts. |
| `build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v0.md` | The first proposal, before the owner's rounds, unedited. |
| `build/2026-10-14-build-PLAY-dClosedLoop-1-design-rounds.md` | Rounds 1 to 5: every question, option and answer verbatim, and what each changed. |
| `build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v1.md` | The design after rounds 1 to 4, unedited. |
| `build/2026-10-14-build-PLAY-dClosedLoop-1-walkthrough.md` | The ten chain builds' designs as presented, each fork and answer, and each revision. |
| `build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md` | The converged design, amended in place under dated `Revised:` lines: principles, the policy catalogue and presets, the chain's rosters. |
| `build/2026-10-14-build-PLAY-dClosedLoop-1-foundations.md` | The owner's foundations revisit, step by step: their words, the measured current state, the response, the forks and answers. |
| `build/2026-10-14-build-PLAY-dClosedLoop-1-flow.md` | The flow walk, stage by stage: the layers, each stage's scope, boundaries and checklist, the forks and answers. |
| `build/2026-10-14-build-PLAY-dClosedLoop-1-flow-interactions.md` | Each step's scope, the eighteen interaction edges, the shared state, and the six interactions settled after. |
| `build/2026-10-14-build-PLAY-dClosedLoop-1-coordination.md` | The owner's no-foreign-build directive, the census of what the design counted on, and leases, the mailbox and dependency coordination designed into dDeclaredLoop. |
| `build/2026-10-14-build-PLAY-dClosedLoop-1-orientation.md` | The owner's questions on how sessions and agents enter, orient, resume and progress along the flow; the research dispatched; then the current state, the design and the forks. |
