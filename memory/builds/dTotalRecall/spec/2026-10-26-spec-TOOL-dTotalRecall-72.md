# TOOL-dTotalRecall-72 — unit 57's edge to unit 56 is read at step 21 by a probe no shell quotes, and written with its mirror before unit 57 builds if absent

**Status:** DEFERRED · rev-2 · 2026-10-26 · node d · Tier-2 · base 462d20f3 · streams tooling · order 21 · advances TOOL-dTotalRecall-27

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md) | journal | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 TOOL-dTotalRecall-36 TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 TOOL-dTotalRecall-44 TOOL-dTotalRecall-45 TOOL-dTotalRecall-46 TOOL-dTotalRecall-47 TOOL-dTotalRecall-48 TOOL-dTotalRecall-49 TOOL-dTotalRecall-50 TOOL-dTotalRecall-51 TOOL-dTotalRecall-52 TOOL-dTotalRecall-53 TOOL-dTotalRecall-54 TOOL-dTotalRecall-55 TOOL-dTotalRecall-56 TOOL-dTotalRecall-57 TOOL-dTotalRecall-58 TOOL-dTotalRecall-59 TOOL-dTotalRecall-60 TOOL-dTotalRecall-61 TOOL-dTotalRecall-62 TOOL-dTotalRecall-63 TOOL-dTotalRecall-64 TOOL-dTotalRecall-65 TOOL-dTotalRecall-66 TOOL-dTotalRecall-67 TOOL-dTotalRecall-68 TOOL-dTotalRecall-69 TOOL-dTotalRecall-70 TOOL-dTotalRecall-71 TOOL-dTotalRecall-73 TOOL-dTotalRecall-74 TOOL-dTotalRecall-75 TOOL-dTotalRecall-76 TOOL-dTotalRecall-77 TOOL-dTotalRecall-78 TOOL-dTotalRecall-79 TOOL-dTotalRecall-80 TOOL-dTotalRecall-81 TOOL-dTotalRecall-82 TOOL-dTotalRecall-83 TOOL-dTotalRecall-84 TOOL-dTotalRecall-85 TOOL-dTotalRecall-86 TOOL-dTotalRecall-87 TOOL-dTotalRecall-88 TOOL-dTotalRecall-89 TOOL-dTotalRecall-90 TOOL-dTotalRecall-91 TOOL-dTotalRecall-92 TOOL-dTotalRecall-93 TOOL-dTotalRecall-94 TOOL-dTotalRecall-95 TOOL-dTotalRecall-96 TOOL-dTotalRecall-97 TOOL-dTotalRecall-98 TOOL-dTotalRecall-99 TOOL-dTotalRecall-100 |
| [2026-10-26-review-TOOL-dTotalRecall-71-spec-audit-round1.md](../reviews/2026-10-26-review-TOOL-dTotalRecall-71-spec-audit-round1.md) | spec-audit | TOOL-dTotalRecall-71 TOOL-dTotalRecall-73 TOOL-dTotalRecall-75 TOOL-dTotalRecall-74 TOOL-dTotalRecall-76 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 67 to 70
(`memory/builds/dTotalRecall/reviews/2026-10-26-review-TOOL-dTotalRecall-67-spec-audit-round1.md`)
confirmed finding **id 10 at HIGH**, its item **H2**. That item is the defect of item **B1** (id
23, `TOOL-dTotalRecall-71`) as the grounding lens saw it, and stays its own item only because its
binding grade differs.

`TOOL-dTotalRecall-67` (order 20) passes each string of its §4 table to its probe as `"<string>"`.
Unit 57's edge string, ``**consumes-from** `TOOL-dTotalRecall-56` ``, holds backticks, so bash runs
`TOOL-dTotalRecall-56` as a command and the probe counts `**consumes-from** ` alone. That prints 4
over spec 57 where the edge is absent. Unit 67's S1 therefore reads the edge as present, and its S2
never writes it. Unit 57 then builds at order 30 with no sequencing edge to unit 56.

This unit does unit 67's reading and writing again for that edge, by a probe whose strings never
pass through the shell. Where the edge is absent at this pass's base, it writes the edge into unit
57's §3 and its mirror into unit 56's §3. It repairs `TOOL-dTotalRecall-67`, at step 21, one above
that unit's order and nine steps ahead of units 56 and 57.

## 2. Scope (IN)

- **S1** — The reading. At this pass's base, the probe of §4 counts the edge string over unit 57's
  spec and the mirror string over unit 56's spec. Both counts are recorded before anything is
  written. Observed by AC1 and AC3.
- **S2** — The write. Where the edge string prints 0, this pass writes §4's edge bullet into unit
  57's `### Edges`. Where the mirror string prints 0 in the same case, it writes §4's mirror bullet
  into unit 56's `### Edges`. Each write is a rev bump on that spec, with a §9 line
  `amended by TOOL-dTotalRecall-72 for TOOL-dTotalRecall-67 (id 10, item H2)`. Observed by AC1.
- **S3** — The order. This pass precedes the passes of units 56 and 57. Observed by AC2.

## 3. Non-goals (OUT)

- Editing unit 67's spec. It lands at order 20, one step before this pass, and a landed spec is
  frozen.
- The check that this edge is present at the tip, live-proven on a copy without it, and the record
  of what unit 67's AC1 certified: `TOOL-dTotalRecall-71` (id 23), which reads this pass's output.
- Unit 67's other five strings. None holds a backtick or a `$`, so the double-quoted form reads them
  as written.
- The two amendments unit 67's table leaves out (ids 1 and 12, item M1), and unit 70's own
  backticked rows (id 11): the batch `TOOL-dTotalRecall-76` and `TOOL-dTotalRecall-74`.
- The bug-class entry or spec lint the report suggests as the left-shift gate: the close's
  left-shift step (BUILD-METHOD M8).
- Any code. This unit reads and writes spec text only.

### Edges

- **consumes-from** `TOOL-dTotalRecall-67` — its pass at step 20 and its §2 S2, which names the edge and its mirror this unit writes when unit 67 left them out
- **hands-off** `TOOL-dTotalRecall-57` — its consumes-from edge to unit 56, read here by a probe no shell quotes and written here before that unit's pass if absent
- **hands-off** `TOOL-dTotalRecall-56` — its hands-off mirror to unit 57, written here with the edge when the edge is absent
- **hands-off** `TOOL-dTotalRecall-71` — unit 57's spec as this pass leaves it, which that unit re-reads at the tip with its liveness copies
- **hands-off** `TOOL-dTotalRecall-88` — its AC2 ancestry and its edge and mirror counts, which that batch re-reads at verified revisions (the round-1 audit of units 71 to 76, ids 19, 40)

## 4. Design

### The probe

Every string sits in a Python literal inside a heredoc whose delimiter is quoted, so bash expands
nothing in it. No string is a shell argument. Text is joined on whitespace before counting, as in
unit 67 §4. A revision is read by `git show` inside Python, with `check=True`, so a failed read
raises and is a red, never a 0.

```bash
# run from memory/builds/dTotalRecall/spec/
python - <<'PROBE'
import re, subprocess
EDGE = '**consumes-from** `TOOL-dTotalRecall-56`'
MIRROR = '**hands-off** `TOOL-dTotalRecall-57`'
def text(rev, name):
    raw = (subprocess.run(['git', 'show', rev + ':./' + name], capture_output=True, check=True).stdout.decode('utf-8')
           if rev else open(name, encoding='utf-8').read())
    return re.sub(r'\s+', ' ', raw)
for n, s in (('57', EDGE), ('56', MIRROR)):
    print(n, text('', '2026-10-26-spec-TOOL-dTotalRecall-%s.md' % n).count(s))
PROBE
```

PINNED, measured 2026-10-26 at `653bed738` and again at `addc4073e` with this probe's `text(rev, …)`
form: the edge string prints 0 over spec 57 and 0 over spec 61. The mirror string prints 0 over
spec 56 and 1 over spec 61, whose §3 carries that bullet. The double-quoted form of unit 67 §4
printed 4 over spec 57 at `addc4073e`, with `TOOL-dTotalRecall-56: command not found` on stderr.

### The bullets

Unit 61 §4 describes the edge pair rather than spelling it, so the text comes from the two units'
own designs. Unit 56 empties `ALIAS_COMPARE_KEPT`, and unit 57's AC2 reads both constants gone.

```markdown
- **consumes-from** `TOOL-dTotalRecall-56` — its pass, which moves the last row of `ALIAS_COMPARE_KEPT` out, since this unit's AC2 reads both constants gone
- **hands-off** `TOOL-dTotalRecall-57` — the emptied `ALIAS_COMPARE_KEPT`, whose absence that unit's AC2 reads
```

The edge bullet goes into unit 57 and the mirror bullet into unit 56, each as the last bullet of its
`### Edges`, in the template's shape (`memory/TEMPLATE-SPEC.md`, "§3 Edges").

### Why order 21

The edge must be in unit 57's spec before unit 57 builds at order 30. It can only be judged after
unit 67's pass at order 20. Step 21 is the first step after that. `TOOL-dTotalRecall-71` shares the
step and reads this pass's output, so the edge above runs this pass first under BUILD-METHOD M6, as
unit 68's edge to unit 66 orders step 32. `TOOL-dTotalRecall-20` shares the step and writes neither
spec.

### Inventory

Minted: nothing in code. Amended, only where S1 reads 0: the specs of units 56 and 57.

### Files touched (estimate)

- `memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-56.md`
- `memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-57.md`
- `memory/builds/dTotalRecall/build/` (this unit's acceptance-ledger line)

### Alternatives rejected

- **Amend unit 67's §4 to single-quote its strings.** Unit 67 builds at order 20, before this unit.
  A spec changed after its pass is a departure, and the corrected template would still have run at
  step 20 against the gap.
- **Single-quote the string on the command line.** That works for this string, and breaks again on
  the first string holding a `'`. A literal in a quoted heredoc holds both.
- **Write the edge unconditionally.** Unit 61 may have written it at step 19, and a second copy is a
  duplicate edge that AC1 reds.

## 5. Production-readiness checklist

- security — no surface: spec text only.
- perf / scale — two counts over two files.
- error / empty / loading states — a count of 0 is the gap S2 fills. A file the probe cannot read
  raises, which is a red, never a 0.
- observability — the ledger line names both base counts and whether S2 wrote.
- risks — the edge written while unit 61's own edge stands, if unit 61 spelled it otherwise. S1
  counts the exact bullet head, which unit 61's line must carry to be an edge at all.
- testing — AC1 to AC3 by the pass.
- migration — none.
- user docs — none under `help/`.

## 6. Acceptance criteria

- **AC1** — When the probe of §4 runs at this pass's tip, the edge string prints 1 over unit 57's
  spec and the mirror string prints at least 1 over unit 56's spec.
  `git grep -c "amended by TOOL-dTotalRecall-72" -- 2026-10-26-spec-TOOL-dTotalRecall-57.md`, run
  from the spec folder, prints 1 exactly when S1's base count of the edge was 0.
  Red when: the edge is absent from unit 57's spec, or is written twice.
  figure: the base counts are PINNED in §4, measured 2026-10-26; the tip counts are DERIVED by the
  probe at the pass.
- **AC2** — When the pass commits of units 56 and 57 are reached,
  `git merge-base --is-ancestor <this unit's pass commit> <each one>` exits 0 for each, the pass
  commit of a unit being `git log --reverse --format=%H --grep='^Pass: <unit id>$' 462d20f3..HEAD`'s
  first line.
  Red when: unit 56 or unit 57 builds before this pass.
- **AC3** — When `git grep -n "Evidences:\*\* TOOL-dTotalRecall-72" -- memory/builds/dTotalRecall/build`
  runs after the pass, it prints the ledger block. Its AC1 line names the base count of the edge
  string and of the mirror string, on the line's first physical line.
  Red when: the line names only tip counts, so a gap unit 61 left is invisible.

## 7. Gates

`memory hygiene` · `recall floor` · `recall floor arms`

No new arm: this unit writes spec text and a ledger line, and the edge it restores is graded by
hygiene check 12's mirror rule.

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec carrying nothing and derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`, the ruling that a chain spec run carries the units it adds; (b) a `part k/n`
  carry of `TOOL-dTotalRecall-19`'s clause, which would split a clause that unit carries whole. (b)
  reds the parts join; veto 1 discards it. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the
  precedent `TOOL-dDeclaredLoop-36` §8 F1 set. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit of units 67 to 70, id 10
  (HIGH, item H2, the defect of item B1 at its own grade).
- rev-2 · 2026-10-26 · §3 · the Edges block gains the mirror of TOOL-dTotalRecall-88, each the other end of an edge a
  unit the round-1 spec audit of units 71 to 76 promoted wrote; nothing else moved.

## 10. Reuse audit

The seam is unit 67's own probe, the joined-text count of its §4, kept whole except for how a string
reaches it: a literal in a quoted heredoc instead of a shell argument. The revision read is the
`subprocess.run(['git', 'show', ...], check=True)` form unit 70 §4's body compare already uses.
`python tools/codebase-map/reuse_lookup.py "count a phrase holding backticks in a spec file without shell quoting"`
ranked name-stem neighbours only (`counts`, `read_spec_revisions`, `parse_spec_h1`), none of which
counts a phrase in a spec body. The recall query below found the audit's own item and unit 67's
probe, and `TOOL-aLexedStripper-1` §4, which records that a shell backtick opens command
substitution. No existing seam fits beyond unit 67's probe.

Recall terms used: `python tools/memory-recall/query.py "how does a probe pass a string holding backticks to python without the shell running it" --terms "probe backtick double-quote command-substitution argv joined-text count spec amendment liveness stdin heredoc"`
