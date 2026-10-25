# TOOL-dGroundRules-71 — the hygiene suite's check-7 arms read the finding line with the cap rule it now carries

**Status:** CLOSED · rev-1 · 2026-10-25 · node d · Tier-1 · base 2b758400 · streams tooling · order 25

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-prompt-TOOL-dGroundRules-71-1-spec-writer.md](../prompts/2026-10-25-prompt-TOOL-dGroundRules-71-1-spec-writer.md) | journal | — |
| [2026-10-25-prompt-TOOL-dGroundRules-71-spec-brief.md](../prompts/2026-10-25-prompt-TOOL-dGroundRules-71-spec-brief.md) | research | — |
| [2026-10-25-review-TOOL-dGroundRules-1-71-closing-diff-round1.md](../reviews/2026-10-25-review-TOOL-dGroundRules-1-71-closing-diff-round1.md) | diff-review | TOOL-dGroundRules-1 TOOL-dGroundRules-2 TOOL-dGroundRules-3 TOOL-dGroundRules-4 TOOL-dGroundRules-5 TOOL-dGroundRules-6 TOOL-dGroundRules-7 TOOL-dGroundRules-8 TOOL-dGroundRules-9 TOOL-dGroundRules-10 TOOL-dGroundRules-11 TOOL-dGroundRules-14 TOOL-dGroundRules-15 TOOL-dGroundRules-16 TOOL-dGroundRules-17 TOOL-dGroundRules-18 TOOL-dGroundRules-19 TOOL-dGroundRules-20 TOOL-dGroundRules-21 TOOL-dGroundRules-22 TOOL-dGroundRules-23 TOOL-dGroundRules-24 TOOL-dGroundRules-25 TOOL-dGroundRules-26 TOOL-dGroundRules-27 TOOL-dGroundRules-28 TOOL-dGroundRules-29 TOOL-dGroundRules-30 TOOL-dGroundRules-31 TOOL-dGroundRules-32 TOOL-dGroundRules-33 TOOL-dGroundRules-34 TOOL-dGroundRules-35 TOOL-dGroundRules-36 TOOL-dGroundRules-37 TOOL-dGroundRules-38 TOOL-dGroundRules-39 TOOL-dGroundRules-40 TOOL-dGroundRules-41 TOOL-dGroundRules-42 TOOL-dGroundRules-43 TOOL-dGroundRules-44 TOOL-dGroundRules-45 TOOL-dGroundRules-46 TOOL-dGroundRules-47 TOOL-dGroundRules-48 TOOL-dGroundRules-49 TOOL-dGroundRules-50 TOOL-dGroundRules-52 TOOL-dGroundRules-55 TOOL-dGroundRules-56 TOOL-dGroundRules-60 TOOL-dGroundRules-61 TOOL-dGroundRules-62 TOOL-dGroundRules-63 TOOL-dGroundRules-64 TOOL-dGroundRules-65 TOOL-dGroundRules-66 TOOL-dGroundRules-67 TOOL-dGroundRules-68 TOOL-dGroundRules-69 TOOL-dGroundRules-70 |

<!-- /gen:spec-records -->

## 1. Goal

The hygiene suite fails three check-7 arms at the close: `check 7 emitted 0 findings, expected
exactly 2`, `missing exact line: memory/backlog/ARCH.md:7 (301 chars > 300)` and
`check 7 reported ''`. Check 7 still fires on the right rows. Each refused finding now ends in
` · <rule>`, the rule that refused it, and the three arms still match the bare `(N chars > M)` line
anchored at its end. This unit respells the three arms to the line the checker prints, and keeps what
each one asserts.

## 2. Scope (IN)

- **S1** — The check-7 arms. In `tools/memory-tree/check-memory-hygiene.test.sh`, the count arm at
  `:1509`, the exact-line arm at `:1512` and the numbering arm at `:1514` are respelled as §4 "The
  arms" gives. Two comment lines go in directly above `:1509`. No other byte of the suite changes,
  and no floor moves. Observed by AC1, AC2 and AC3.

## 3. Non-goals (OUT)

- `tools/memory-tree/check-memory-hygiene.sh`. Its check-7 output is correct as it stands (§4
  "Evidence"), and this unit only grades it.
- The cap values of check 7, and the policy kit's rule text.
- The inherited red arm `the scoped runs do not partition the unscoped run's lines`, and any other
  spec.

### Edges

none

This unit carries out the follow-through of `TOOL-dGroundRules-9` (CLOSED), whose emitter added the
rule suffix, and `TOOL-dGroundRules-21` (CLOSED), whose S31 gave a refused policy read its rule. It
changes nothing either unit built.

## 4. Design

### Evidence

Check 7's awk prints each over-cap line as the finding, then five tab-separated fields: mode, cap
class, measure, unit and cap (`tools/memory-tree/check-memory-hygiene.sh:1242`).
`check_cap_findings` (`:539-555`) splits each line on tabs at `:545`. It keeps a refused finding as
its text followed by ` · <rule>` when a rule is known (`:550`). The rule comes from `read_cap_rule`
(`:535`), which reads the policy kit's `budgets: <cap> · <rule>` lines. The tab fields never reach
the output.

Measured at `2b7584007`. The suite's own fixture builder, cut at its main run, was copied into a
scratch script (§5, `f71.sh`), and the checker ran on the tree it builds. The checker printed exactly
these two check-7 findings, and no tab or mode field:

```
memory/backlog/ARCH.md:5 (369 chars > 300) · the policy reader refused, so a breach refuses as before
memory/backlog/ARCH.md:7 (301 chars > 300) · the policy reader refused, so a breach refuses as before
```

So the premise holds, and the defect is in the arms, not in the checker's output. The old count
predicate prints `0` over this output, which is the close's red.

### Why the rule text is stable

The rule is `READER_REFUSED` (`tools/policy/budgets.py:69`). `resolve_caps` gives it to every cap
when `policy.read_revision` refuses (`budgets.py:219-223` and `:249-250`). The read refuses because
the fixture has no landed revision. The suite pins `init.defaultBranch=master` and adds no remote
(`check-memory-hygiene.test.sh:145-153`), and `derive_landed_revision`
(`tools/policy/policy.py:471`) looks for `main`. The suite's comment there already relies on this:
every check-6 and check-7 breach in the fixture refuses as before. So the rule comes from the
fixture's own repository shape. Gov's `.governance/policy.toml` and the landed values of the switch
play no part. The policy kit resolves because the suite runs only on gov's bar, beside it
(`tools/govkit/registry.toml:591`, its exempt-leg row).

### The arms

The count arm and the numbering arm need the shape of a refused finding. They match the finding,
then ` · `, then one or more characters that are not control characters, then the end of the line.
`[^[:cntrl:]]` refuses a tab, so a mode field that leaked into the output would red both arms. The
exact-line arm pins the whole line the fixture yields, rule included, so the suite now also grades
that check 7 names the rule. The `miss` arm at `:1513` matches a prefix and holds as it is.

Lines `:1509`, `:1512` and `:1514` become the lines below, with the two comment lines above the
first. Lines `:1510`, `:1511` and `:1513` are unchanged and are shown for position:

```
# ...and after ` · `, the rule that refused it (TOOL-dGroundRules-9). No fixture here has a landed
# revision, so the policy reader refuses and the rule is budgets.py's READER_REFUSED.
n7=$(grep -cE '^memory/backlog/ARCH\.md:[0-9]+ \([0-9]+ chars > [0-9]+\) · [^[:cntrl:]]+$' <<<"$out")
[ "$n7" = 2 ] || { echo "FAIL check 7 emitted $n7 findings, expected exactly 2 (fence, comment and separator are exempt; the 300-byte row is under the cap)"; st=1; }
n=$((n+1))
hitl 'memory/backlog/ARCH.md:7 (301 chars > 300) · the policy reader refused, so a breach refuses as before'
miss 'memory/backlog/ARCH.md:6 ('
c7line=$(grep -E '^memory/backlog/ARCH\.md:[0-9]+ \([0-9]+ chars > [0-9]+\) · [^[:cntrl:]]+$' <<<"$out" | head -1)
```

The `case` at `:1515-1516` still reads `c7line` by its `memory/backlog/ARCH.md:5 (` prefix and does
not change. Each arm keeps its intent: exactly two findings, line 7 named at 301 over 300, line 6 not
named, and the over-cap row at unfenced line 5. Measured in `LC_ALL=C`, in `LC_ALL=C.UTF-8` and in
the node's default locale, the respelled predicates gave the same counts.

What the arms do not check: the rule text of a finding other than line 7's, and a rule from a tree
whose policy kit answers, since this fixture never has one. A finding that lost its rule, which is
what a tree with no policy kit prints, reds all three arms. That is right for this suite, which runs
only beside the policy kit. If `READER_REFUSED` is reworded, the exact-line arm reds, and its `FAIL
missing exact line` message names the old text.

### Alternatives rejected

- An optional suffix in all three arms. It would pass with no rule at all, so the suite would stop
  grading the rule that `TOOL-dGroundRules-9` made check 7 name.
- Any suffix in the exact-line arm too, through `grep -qxE`. That keeps the suite free of the policy
  kit's wording, but no arm then observes which rule the fixture yields. `tools/check-line-length.test.sh:200`
  pins its own enforcer's rule text the same way.

### The floors

S1 adds or moves no `n=$((n+1))` (`:1505`, `:1511`) and no `hitl` or `miss` call, each of which
counts one assertion (`:1057-1058`). So the executed count does not change, and
`FLOOR_ASSERTIONS=670` at `:4388` does not move.

### Rollout

The builder sets this spec's status from DEFERRED to INPROGRESS before its first write. Scratch-guard
admits writes under `ROUTED_PATHS` for a Tier-1 unit only at INPROGRESS, or at SPECCED once graded.

### Files touched (estimate)

- `tools/memory-tree/check-memory-hygiene.test.sh`

## 5. Acceptance criteria

All commands run from the repository root of the pass's worktree. The criteria use two scratch
scripts. `f71.sh` copies the suite's fixture builder, cut at its main run, and writes that run's
output to the file it is given. A second argument appends one line to the fixture's conf.

```
cat > "$TEMP/f71.sh" <<'EOF'
sed -e "s#^HERE=.*#HERE=\"$PWD/tools/memory-tree\"#" -e '/^out=$(bash "$SCRIPT" 2>\/dev\/null); mainrc=$?$/q' tools/memory-tree/check-memory-hygiene.test.sh > "$1.sh"
[ -z "${2:-}" ] || sed -i "/> \.memory-tree\.conf\$/a echo '$2' >> .memory-tree.conf" "$1.sh"
echo 'printf "%s\n" "$out" > "$OUT71"' >> "$1.sh"
OUT71="$1" bash "$1.sh"
EOF
bash "$TEMP/f71.sh" "$TEMP/g71.out"
bash "$TEMP/f71.sh" "$TEMP/r71.out" ENTRY_CAP_CHARS=301
sed 's/before$/before\trefuse/' "$TEMP/g71.out" > "$TEMP/t71.out"
```

`g71.out` is the output as the checker prints it now. `r71.out` stages the cap one higher, so the
301-character row is under it. `t71.out` stages a mode field leaked after the rule, behind a tab.

`p71.sh` holds the respelled arms' predicates from §4, copied byte for byte, read from a file in
place of `$out`. It prints the count, the line-7 count, the line-6 count and the first finding's
`<path>:<line>`, or `none`:

```
cat > "$TEMP/p71.sh" <<'EOF'
F="$1"
n7=$(grep -cE '^memory/backlog/ARCH\.md:[0-9]+ \([0-9]+ chars > [0-9]+\) · [^[:cntrl:]]+$' "$F")
l7=$(grep -cxF 'memory/backlog/ARCH.md:7 (301 chars > 300) · the policy reader refused, so a breach refuses as before' "$F")
l6=$(grep -cF 'memory/backlog/ARCH.md:6 (' "$F")
c7line=$(grep -E '^memory/backlog/ARCH\.md:[0-9]+ \([0-9]+ chars > [0-9]+\) · [^[:cntrl:]]+$' "$F" | head -1)
c7line=${c7line%% (*}
echo "$n7 $l7 $l6 ${c7line:-none}"
EOF
```

The whole suite is a self-test this pass may not run. The main loop runs it at the close, and that
run prints no `FAIL` line naming `check 7` or `memory/backlog/ARCH.md:7`.

- **AC1** — When `bash "$TEMP/p71.sh" "$TEMP/g71.out"` runs, it prints `2 1 0 memory/backlog/ARCH.md:5`.
  Red when: the cap is staged one higher. Over `r71.out`, `bash "$TEMP/p71.sh" "$TEMP/r71.out"`
  prints `1 0 0 memory/backlog/ARCH.md:5`, so the count arm and the exact-line arm red by name. Red
  also when a tab field leaks into the output: over `t71.out` it prints `0 0 0 none`, and all three
  arms red. All three were measured at `2b7584007`. So was the old count predicate,
  `grep -cE '^memory/backlog/ARCH\.md:[0-9]+ \([0-9]+ chars > [0-9]+\)$' "$TEMP/g71.out"`, which
  printed `0`.
  permission: the suite that holds the arms is a self-test this pass may not run.
- **AC2** — When `grep -cF ' chars > [0-9]+\) · [^[:cntrl:]]+$' tools/memory-tree/check-memory-hygiene.test.sh` runs, it prints `2`.
  At `2b7584007` it printed `0`.
  Red when: the count arm or the numbering arm spells a predicate other than §4's, so AC1's script no
  longer stands for the arms the suite runs.
- **AC3** — When `grep -cxF "hitl 'memory/backlog/ARCH.md:7 (301 chars > 300) · the policy reader refused, so a breach refuses as before'" tools/memory-tree/check-memory-hygiene.test.sh` runs, it prints `1`.
  At `2b7584007` it printed `0`.
  Red when: the exact-line arm still names the bare line, or names a rule other than the one the
  fixture yields.

## 6. Gates

`memory-hygiene self-test` · `harness arms (fail branches armed or pinned)` · `shell hygiene (a loop fed by a command substitution)` · `shell hygiene (a location probe asked from a moved directory)` · `spec tokens (a spec's own names resolve)` · `memory hygiene`

The guards join owes no leg for `tools/memory-tree/check-memory-hygiene.test.sh`. Run through
`derive_guarded_legs` at `2b7584007`, no non-broad guard trips on it. Every leg
`python tools/check-spec-tokens.py --legs-for tools/memory-tree/check-memory-hygiene.test.sh` prints
trips only on the broad `tools/memory-tree/` or `tools/`. `memory-hygiene self-test`
(`tools/gate-legs.json:396`) is the suite itself, so the close runs it. `harness arms` reads the suite
as the sibling test of `check-memory-hygiene.sh`, and the two shell-hygiene scans read it as a
tracked shell file. They carry no guard and are named because the edit is in what they read.

No arm is added: S1 respells three arms in place, so this unit declares no new suite arm. Their red
is the close's run at `4f76c4b39`, and AC1's staged breaks red them again. No floor moves.

## 7. Open questions

none

## 8. Revision log

- rev-1 · 2026-10-25 · initial draft from the build run's rescope add row for this unit and its spec
  brief, grounded at `2b7584007`. The premise was checked on the checker's own output over the
  suite's fixture tree, not by running the suite. The two findings carry ` · <rule>` and nothing
  else, so the checker is correct and the arms are respelled. Pins the exact-line arm to the fixture's
  rule over an any-suffix match, because only the pin grades the rule. The rule is stable because it
  comes from the fixture's own lack of a landed revision, not from gov's policy file. The brief's leg
  item names §6/§7; in this Tier-1 shape the Gates section is §6, and the leg line sits there. The
  brief, untracked when this draft was written:

```
memory/builds/dGroundRules/prompts/2026-10-25-prompt-TOOL-dGroundRules-71-spec-brief.md
```

## 9. Reuse audit

This unit builds no mechanism. It respells three arms of the suite's check-7 block,
`tools/memory-tree/check-memory-hygiene.test.sh:1504`, in place, with the `hitl` and `miss` helpers
(`:1057-1058`) and the grep the block already uses. AC1 reuses the suite's own fixture builder by
copying it into a scratch script, never retyping the fixture.
`python tools/codebase-map/reuse_lookup.py "match a check 7 finding line that carries the cap rule suffix in the hygiene suite"`
ranked only name stems (`check`, `checks`, `resolve_caps`, `check_line`), and none of them reads a
check-7 finding. The recall probe returned only this unit's own brief and run row on the check-7
arms, plus older records on check 7's caps that do not touch the suite's arms.

Recall terms used: `python tools/memory-recall/query.py "hygiene suite check 7 arms grep bare chars finding after the cap rule suffix" --terms "check_cap_findings read_cap_rule READER_REFUSED chars > 300 ARCH.md:7 hitl"`
