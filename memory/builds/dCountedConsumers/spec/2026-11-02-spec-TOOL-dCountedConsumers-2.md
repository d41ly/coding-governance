# TOOL-dCountedConsumers-2 — the trace signal counts a commit that writes a help page as product

**Status:** INPROGRESS · rev-1 · 2026-11-02 · node d · Tier-1 · base 8bec4cef · streams tooling · order 20

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-02-prompt-TOOL-dCountedConsumers-2-brief.md](../prompts/2026-11-02-prompt-TOOL-dCountedConsumers-2-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

`closed_specs_with_no_product_commit` reads a CLOSED unit as traced only when a commit under
`TRACE_GLOBS` names its slug, and `help/` is not under them. A unit whose whole product is a help
page, as the charter's [docs] rule makes it, then reads as an offender. TOOL-dCountedConsumers-1 is
the first instance, and it reds the landing's pre-push bar. Adding `help` to `TRACE_GLOBS` makes a
help-page pass count as product, so that class of unit stops reading as an offender.

## 2. Scope (IN)

- **S1** — `TRACE_GLOBS` in `tools/drift-audit/drift_signals.py:71-76` gains the entry `"help"`,
  as its last item. Observed by AC1, AC2 and AC3.
- **S2** — The comment above the list, `drift_signals.py:67-70`, says why `help` is there, and why
  `PRODUCT_GLOBS` stays without it. It is written in the house's kind: the reason, the measured
  fact behind it, and the scope line. Observed by AC6.
- **S3** — No other CLOSED spec's verdict moves when `help` joins. The only unit that newly passes
  is one of this build's, and none newly fails. Observed by AC4.
- **S4** — Only that comment and that list move. `PRODUCT_GLOBS`, `EVIDENCE_GLOBS`, `BASELINES`
  and every other declaration in the file keep their bytes, and no other product file changes.
  Observed by AC5.

## 3. Non-goals (OUT)

- `PRODUCT_GLOBS` (`drift_signals.py:28-38`). S2 says why in the file itself, and §4 gives the
  reason.
- The shipped seed `tools/drift-audit/drift_signals.template.py`. Its `TRACE_GLOBS` ships empty and
  falls back to `PRODUCT_GLOBS` (`drift_signals.template.py:93-99`). An adopter's layout is the
  adopter's to declare.
- The engine `tools/drift-audit/drift_report.py`, the signal's code included. Its comment at
  `drift_report.py:3558-3560` says this repo narrows `TRACE_GLOBS` by dropping `.claude/`, and that
  stays true.
- The dead probe `discarded_work_landed`.
- The `BASELINES` set for this signal (`drift_signals.py:409-411`). It lists TOOL-aMooredAnchor-1
  alone and is shrink-only. The `--check` output says so: it tells the reader to remove a new
  offender's cause and never to list it (`drift_report.py:4464-4465`). No row is added for
  TOOL-dCountedConsumers-1.
- `memory/project/trace-waiver.txt`. No row is added or removed.
- The slug-level join itself (`drift_report.py:1147-1152`), which open ask TOOL-aReplayedCard-6
  questions. §4 Limitations says what it means for this unit's evidence.
- A self-test arm asserting that the declared list carries `help`, in the shape of
  `tools/drift-audit/selftest.py:2983-2993`. It would be a separate mechanism (M2). Whoever
  dispatched this unit reports it as a follow-up. See §4 Limitations.
- Running the `drift-audit records` or `drift-audit selftest` leg inside the pass. The main loop
  runs them at the close (§6).

## 4. Design

Line numbers are this tree's at `13872590e`, PINNED 2026-11-02. `tools/drift-audit/` is
byte-identical at the base `8bec4cef`, because the build's commits since touch only `help/policy.md`
and records.

### How the signal reads a commit

The signal walks one `git log` over the base ref and `HEAD`, with `--no-merges --full-history`,
restricted to `ctx.trace_globs` (`drift_report.py:1078-1080`). That list is the project layer's
`TRACE_GLOBS`, or `PRODUCT_GLOBS` where none is declared (`drift_report.py:3562`). A CLOSED spec
dated on or after `TRACE_CUTOFF` is traced when its build SLUG appears in one of the walked
subjects (`drift_report.py:1151`). Otherwise it is waived by a `trace-waiver.txt` row, or it is an
offender. A waiver row no untraced spec consumes is itself an offender, a stale waiver
(`drift_report.py:1159-1166`). `--check` judges this signal against `BASELINES` by row identity. It
prints `new` for an offender the set does not list and `stale` for a listed id that is no offender
(`drift_report.py:4338-4343`, `:4458-4468`).

TOOL-dCountedConsumers-1's pass commit is `871f3c975`. It touches `help/policy.md`, `memory/LIVE.md`,
the build README and its own spec, so no path in today's `TRACE_GLOBS` selects it. No other commit
naming the slug touches a traced path, so the unit reads as an offender. That is the brief's reading
of 2 against a baseline of 1.

### The change

`"help"` is appended to `TRACE_GLOBS`. It is a root-relative directory pathspec, spelled like
`"skills"` beside it, and git matches everything under it. `drift_signals.py` is `project-owned`
(`tools/drift-audit/kit.toml:42-44`), so no kit version moves and no adopter's copy changes.

The comment block at `:67-70` keeps its four lines. Two paragraphs follow it, above the list. The
builder may reword them, but each must carry the facts shown here:

```python
# AND ONE PATH WIDER than the kit paths: `help`. It holds the user-facing pages the `docs` leg
# grades, and the charter's [docs] rule makes a current page part of a user-facing change, so a
# pass that writes one has shipped product. Without it a unit whose whole product is a help page
# read as an offender: TOOL-dCountedConsumers-1, whose pass commit touched `help/policy.md` and
# its own records and nothing above. No records commit touches `help/`. Measured 2026-11-02, every
# commit that does is a build, tool, docs or playbook pass.
#
# NOT ADDED TO PRODUCT_GLOBS, and that is a scope line, not a verdict on the pages. PRODUCT_GLOBS
# also feeds signal 2, through EVIDENCE_GLOBS below, and the escape ratio. A help page that names a
# unit id would then cite that unit as shipped, and neither reading was measured with `help` in it.
```

The `No records commit` sentence is measured, PINNED 2026-11-02 at `13872590e`. Of the 90 non-merge
commits that touch `help/` and are reachable from either `origin/main` or `HEAD`, 53 subjects open
`build`, 34 `tool`, 2 `docs` and 1 `playbook`. Four of them touch no path in today's
`TRACE_GLOBS`: `871f3c975`, `65b587e50`, `d88f7ddda` and `bb0159546`. The help pages cite three
unit ids today (`help/agent-limit.md`, `help/policy.md`, `help/roles.md`), which is the concrete
case behind the `PRODUCT_GLOBS` paragraph.

### Which verdicts move

Adding a pathspec only adds subjects to the walk, so a spec traced before stays traced. The one way
a verdict can get worse is a waived spec that becomes traced, which leaves its waiver row unused and
reports it stale. Probe B below measured both directions on 2026-11-02 at `13872590e`. With `help`
joined, exactly one judged spec changes verdict, TOOL-dCountedConsumers-1, and no waiver row goes
stale. Three of the four help-only commits name a slug that a `tools/` commit already traces
(dFoldedAudit, dGroundRules), or name no build slug (`docs(help)`), so they move nothing.

### The probe

Probe B is `probe.py` in `P`, the pass's own scratch directory, spelled absolute. It runs from the
worktree's root. It calls the signal function in-process and runs no gate. It writes no drift
history, which only `--check` writes (`drift_report.py:4447-4454`).

It reads the signal twice per walk end: once with `help` in the list and once without, the second
reproducing the list as it stood before this unit. The `pre` walk is pinned at the build's base
`8bec4cef` and at `13872590e`, the tip the landing's bar read 2 at, before this unit's own commit.
The `head` walk is the one the `drift-audit records` leg takes, the resolved base ref and `HEAD`. A
wrapper on `ctx.git.run` swaps `HEAD` for the walk's end, and the signal makes no other git call
(`drift_report.py:1038-1182`).

```python
import pathlib, sys
sys.path.insert(0, "tools/drift-audit")
import drift_report as dr
SIG, PRE_BASE, PRE_END = "closed_specs_with_no_product_commit", "8bec4cef", "13872590e"
root = dr.repo_root()
conf, proj = dr.load_conf(root), dr.load_project_layer(root)
live = list(proj.TRACE_GLOBS)
listed = set(proj.BASELINES[SIG])
print("globs", "help-in-trace", "yes" if "help" in live else "no",
      "help-in-product", "yes" if "help" in proj.PRODUCT_GLOBS else "no")
def read(base, end, globs):
    ctx = dr.Ctx(root, conf, proj, base)
    ctx.trace_globs = globs
    real = ctx.git.run
    ctx.git.run = lambda *a: real(*[end if x == "HEAD" else x for x in a])
    s = dr.signal_closed_specs_untraceable(ctx)
    return s["value"], {dr.derive_row_identity(d) for d in s["detail"]}
with_help = [g for g in live if g != "help"] + ["help"]
without = [g for g in live if g != "help"]
got = {}
for label, base, end in (("pre", PRE_BASE, PRE_END), ("head", dr.resolve_base_ref(root, None), "HEAD")):
    for arm, globs in (("with", with_help), ("without", without)):
        v, have = got[label, arm] = read(base, end, globs)
        print(label, arm, "value", v, "new", *(sorted(have - listed) or ["none"]),
              "stale", *(sorted(listed - have) or ["none"]))
print("moved", *(sorted(got["pre", "with"][1] ^ got["pre", "without"][1]) or ["none"]))
src = pathlib.Path("tools/drift-audit/drift_signals.py").read_text(encoding="utf-8")
block = src[src.index("TRACE_CUTOFF: str"):src.index("TRACE_GLOBS: list")]
print("comment", *(f"{w}={block.count(w)}" for w in ("help/", "docs", "PRODUCT_GLOBS", "EVIDENCE_GLOBS")))
```

Observed 2026-11-02 at `13872590e`, before the change, it prints:

```
globs help-in-trace no help-in-product no
pre with value 1 new none stale none
pre without value 2 new TOOL-dCountedConsumers-1 stale none
head with value 1 new none stale none
head without value 2 new TOOL-dCountedConsumers-1 stale none
moved TOOL-dCountedConsumers-1
comment help/=0 docs=0 PRODUCT_GLOBS=1 EVIDENCE_GLOBS=0
```

The `without` arms are the probe's liveness: they reproduce the bar's reading of 2 and name the
offender, so a probe that could not see the unit would print `new none` there too. The `moved` line
is live for the same reason.

### Limitations

**The instance clears without this change once this unit commits.** The join is by slug, not by
id. This unit's own pass commit touches `tools/` and its subject names `dCountedConsumers`, so once
it is committed, the `head without` arm also reads 1. That is why AC2 observes the `pre` walk, which ends
before that commit: there, only `help` decides the verdict. The class fix is for the next build
whose only product is a help page.

**Nothing guards `help` staying in the list.** Once this build lands, dropping `help` reds no leg
until a later help-only unit closes. A self-test arm reading the declared list would close that gap,
and §3 names it as a follow-up.

**A help page touched in a records commit would certify its slug.** Measured, none does today. The
first one that does turns the "No records commit" sentence false, and nothing checks it.

**The DEFERRED TOOL-dTendedCadence-18 moves this list.** Its S-scope moves `TRACE_GLOBS` and its
siblings to another kit's project layer "with their values", so `help` moves with them.

### Files touched (estimate)

`tools/drift-audit/drift_signals.py`

### Alternatives rejected

- **A `BASELINES` row for TOOL-dCountedConsumers-1.** The set is shrink-only and the gate says so.
  A row would mark a correct unit as debt.
- **A `trace-waiver.txt` row.** A waiver asserts that no product subject can ever name the unit.
  Here one already does, under a path the list leaves out, so the list is what is wrong.
- **`records-only` on unit 1's header.** Its deliverable is a help page, which is product, and it
  is CLOSED and frozen.
- **`help` in `PRODUCT_GLOBS`.** `TRACE_GLOBS` would then inherit nothing, since it is declared
  outright, and signal 2 and the escape ratio would widen unmeasured. See the comment's second
  paragraph.

## 5. Acceptance criteria

Run from the worktree's root, with `P` set as §4 sets it and probe B written there.

- **AC1** — When `python -B "$P/probe.py"` runs after the change, its first line reads
  `globs help-in-trace yes help-in-product no`. Running
  `grep -c '^    "help",$' tools/drift-audit/drift_signals.py` prints 1.
  Red when: `help` is missing from `TRACE_GLOBS`, is spelled twice, or is added to `PRODUCT_GLOBS`
  as well.
- **AC2** — When `python -B "$P/probe.py"` runs, its `pre with` line reads
  `value 1 new none stale none`. Its `pre without` line reads `value 2 new TOOL-dCountedConsumers-1
  stale none`.
  figure: PINNED. Both values were measured 2026-11-02 over the walk `8bec4cef`..`13872590e`, with
  TOOL-aMooredAnchor-1 the one listed offender. Observed after this unit's spec is CLOSED, the
  `without` line also names TOOL-dCountedConsumers-2 and reads 3, which still passes.
  Red when: the `with` line still names TOOL-dCountedConsumers-1, so `help` does not reach the
  walk. Also red when the `without` line names nothing, so the probe cannot see the instance.
- **AC3** — When `python -B "$P/probe.py"` runs, its `head with` line reads `new none stale none`.
  That is the reading the `drift-audit records` leg takes, with no `new` and no `OVER BASELINE`.
  figure: DERIVED, the walk is re-read at observation from the resolved base ref and `HEAD`.
  Red when: any offender the set does not list, or a listed id no longer an offender, prints after
  `new` or `stale`.
- **AC4** — When `python -B "$P/probe.py"` runs, its `moved` line names TOOL-dCountedConsumers-1
  and no id outside the `dCountedConsumers` slug.
  figure: DERIVED, re-computed over every judged CLOSED spec at observation.
  Red when: another spec's verdict moves either way. A waiver row gone stale counts, and prints
  as its JSON key.
- **AC5** — On the pass commit,
  `git diff --name-only HEAD~1 HEAD -- tools skills help coding-governance-agents.template.md WIRE-INTO-PROJECT.md`
  prints `tools/drift-audit/drift_signals.py` alone. Every hunk header that
  `git diff -U0 HEAD~1 HEAD -- tools/drift-audit/drift_signals.py` prints has an old range inside
  lines 67-76.
  Red when: the pass touches another product file, such as `drift_signals.template.py`, or edits
  `PRODUCT_GLOBS`, `EVIDENCE_GLOBS` or `BASELINES`.
- **AC6** — When `python -B "$P/probe.py"` runs, its `comment` line reads `help/`, `docs` and
  `EVIDENCE_GLOBS` each at 1 or more, and `PRODUCT_GLOBS` at 2 or more.
  figure: PINNED, each read 0 except `PRODUCT_GLOBS=1` on 2026-11-02 at `13872590e`.
  Red when: the comment above the list does not say why `help` is there, or does not say why
  `PRODUCT_GLOBS` stays without it. SHAPE only: it counts words, not whether the reasons are true.

## 6. Gates

`drift-audit records` · `drift-audit selftest`

The main loop runs these legs after the pass. `drift-audit records` is `drift_report.py --check`
(`tools/gate-legs.json:1053-1058`). It must print no `new` line and no `OVER BASELINE` status for
`closed_specs_with_no_product_commit`, and it is the brief's acceptance read at the gate. `drift-audit
selftest` is owed because its guard names the kit directory `tools/drift-audit/`
(`tools/gate-legs.json:928-936`).
Its fixtures write their own project layer, and its one read of the declared file is
`EVIDENCE_GLOBS` (`tools/drift-audit/selftest.py:2988-2993`), which AC5 holds unchanged. The plain
bar runs once at the close. No arm is added or moved.

## 7. Open questions

none

## 8. Revision log

- rev-1 · 2026-11-02 · initial draft.

## 9. Reuse audit

The seam is the declaration this signal already reads: the `TRACE_GLOBS` list and its comment
style at `tools/drift-audit/drift_signals.py:67-76`, extended by one entry and one reason. The
engine reads it through `Ctx.trace_globs` (`drift_report.py:3562`), so no code changes. No
existing seam besides it fits. `reuse_lookup.py` ranked name stems only, `count`, `commit`, `spec`
and `pathspec`, with `git_pathspec` in `tools/govkit/govkit.py` the nearest. None of them selects
the trace walk's paths. Probe B reuses the signal function and the engine's own `Ctx`,
`derive_row_identity` and `resolve_base_ref` rather than re-implementing the join. The recall
query returned this build's brief, cTracedPromise-1's S-item that first narrowed `TRACE_GLOBS`,
TOOL-aMendedFleet-91's records-only verb, the open ask TOOL-aReplayedCard-6 on the slug join, and
the DEFERRED TOOL-dTendedCadence-18 that moves the list. None disagreed with the source as read.

Reuse probe used: `python tools/codebase-map/reuse_lookup.py "the pathspecs whose commits count as evidence a closed spec shipped"`.
Recall terms used: `python tools/memory-recall/query.py "which paths count as product evidence for a closed spec's commit trace" --terms "TRACE_GLOBS closed_specs_with_no_product_commit signal 6 trace-waiver PRODUCT_GLOBS help page product commit BASELINES shrink-only"`.
