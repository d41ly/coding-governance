**Serves:** diff-review DEPL-cMendedVintage-1 DEPL-cMendedVintage-2 DEPL-cMendedVintage-3 DEPL-cMendedVintage-4 DEPL-cMendedVintage-5 DEPL-cMendedVintage-6 DEPL-cMendedVintage-7 DEPL-cMendedVintage-8 DEPL-cMendedVintage-9 DEPL-cMendedVintage-10 DEPL-cMendedVintage-11 DEPL-cMendedVintage-12 DEPL-cMendedVintage-13 DEPL-cMendedVintage-14 DEPL-cMendedVintage-15 DEPL-cMendedVintage-16 DEPL-cMendedVintage-17 DEPL-cMendedVintage-18 DEPL-cMendedVintage-19 DEPL-cMendedVintage-20 DEPL-cMendedVintage-21 DEPL-cMendedVintage-22 DEPL-cMendedVintage-23 DEPL-cMendedVintage-24 DEPL-cMendedVintage-25 DEPL-cMendedVintage-26 DEPL-cMendedVintage-27 DEPL-cMendedVintage-28 TOOL-cMendedVintage-1 TOOL-cMendedVintage-2 TOOL-cMendedVintage-3 TOOL-cMendedVintage-4 TOOL-cMendedVintage-5 TOOL-cMendedVintage-6 TOOL-cMendedVintage-7 TOOL-cMendedVintage-8 TOOL-cMendedVintage-9 TOOL-cMendedVintage-10 TOOL-cMendedVintage-11 TOOL-cMendedVintage-12

# cMendedVintage — closing diff review, ROUND 2

*Node `c`, 2026-09-21. **Round 2.** A Tier-2 adversarial pass over the cumulative diff landing on
`branch/govkit-update-rollbacks-0502c4`: a parallel fan of primed finder lenses, a skeptic stage
prompted to REFUTE each finding, one synthesis. Round 1 reviewed the same base at
`b6cc8f6f4e511a8d9eddbd3a7835170425335ab6`, returned BLOCKED with three blockers and one high, and
its record is
[round 1](2026-09-17-review-DEPL-cMendedVintage-1-diff-review-round1.md). All nine of its findings
were adjudicated and disposed — the four graded blocker-or-high became DEPL-cMendedVintage-22
through -25, all built and closed — and **none of them is re-reported here**. This round grades what
no review has seen: seventeen units and the direct repairs landed after `b6cc8f6f`, including the two
regressions that -22 through -25 themselves shipped. Every citation a surviving finding rests on was
re-opened in this worktree at `4877af81` before this record was written.*

*Eight of the units this round read are NOT on the `Serves:` line above, and their absence is a fact
rather than a gap in the reading: `DEPL-cMendedVintage-29` and `TOOL-cMendedVintage-13` through
`-19` were built straight from the owner's rulings on eight parked decisions, so no spec in this
tree defines them and a binding naming one resolves to nothing. `TOOL-cMendedVintage-17` is graded
below as L1 and `TOOL-cMendedVintage-11` — which does have a spec — as M2, so the reading covered
them whatever the binding line can express. Trimmed rather than left, because a record whose
binding names an id nothing defines is the hygiene gate's own finding, and eight retro-specs written
after the fact would be exactly the re-narration §5 bans.*

**Reviewed range:** `859daa67e728ae273d5278536fb462c04077f16f...4877af81c05b54b1b995f44adf5396e947ccb73a`.

## Verdict: BLOCKED

One BLOCKER, in `tools/govkit/govkit.py`, in the dirty-path precondition that round 1's B3 widened and
DEPL-cMendedVintage-24 rebuilt. It is not the same defect as B3: B3 was a row EXCLUDED from the
graded population, this is the graded population going EMPTY. Both hands of the round-1 repair are
present and correct; the reader under them swallows a non-zero git exit, so one receipt row naming a
path outside the target repository empties all four batched reads and the whole precondition returns
"clean". It is reproduced below on a scratch repo, not argued.

The same asymmetry round 1 named still holds and still matters: **nothing here is reachable in THIS
repository.** `gov` does not dogfood `govkit`, `.governance/` carries a `deploy.toml` and no
`install.json`, so a green bar on this tree is not evidence against the blocker or against either
high. All three land on the first adopter target that takes this vintage.

**Review shape.** Raw 17, confirmed 10, refuted 7, unverified 0, precision 0.59. Precision fell from
round 1's 0.88, which is the expected direction over a surface round 1 already hardened: §8 says
heavy multi-lens work over hardened code manufactures refuted noise, and seven refutations out of
seventeen is that sentence arriving on schedule rather than a fan that was primed badly.

**Run integrity.** Lenses 4/4 returned, 0 DIED. Skeptic batches 5/5 returned, 0 DIED. 0 contradictory
verdicts demoted to unverified, 0 spurious verdicts discarded, 0 duplicates reported by the harness.
The finding set is COMPLETE as delivered — every lens and every skeptic batch came back — so a zero
count in any lens's territory is evidence rather than a gap. That statement covers delivery only; it
says nothing about the coverage of the lenses themselves, and the unexercised-suite note at the foot
of this record is the honest bound on that.

**Consolidation, stated so the arithmetic is checkable.** The 10 confirmed findings describe **7
distinct defects**. The harness reported 0 duplicates; that is a delivery fact and it is wrong as an
adjudication. Three lenses independently found the same off-by-one write window in
`scan_uncontained_writes` (delivered 2, 12, 15) and two independently found the same unreserved
`--how runner` spelling (delivered 10, 17). Nothing was dropped in the merge — every one of the 10 is
represented below and each entry names the delivered ids it carries. Counts adjudicated HERE:
**BLOCKER 1 · HIGH 2 · MEDIUM 2 · LOW 2**, seven findings. Two rows differ from the delivered
severity and both say so in the row.

## Findings, severity-ranked

| # | Sev | Site | Defect | From |
|---|-----|------|--------|------|
| B1 | BLOCKER | `tools/govkit/govkit.py:4933` | `_names` swallows a non-zero git exit, so ONE out-of-tree receipt path empties every batched read and the whole S4 dirty-path precondition returns clean | 14 |
| H1 | HIGH | `tools/govkit/govkit.py:1135` | `scan_uncontained_writes`'s window excludes the function's LAST line, so the minimal write helper — join, write, end of function — is invisible to selfcheck arm 9 | 15, 12, 2 |
| H2 | HIGH | `tools/govkit/govkit.py:4979` | Carve-out 4 folds an ABSENT worktree copy into "nothing outside gov's region", so an operator's uncommitted deletion of a gov-only `.gitattributes` reads clean and `update --write` recreates and stages it | 11 |
| M1 | MEDIUM | `tools/govkit/govkit.py:7068` | The single `pins_path` slot is rebound per `attributes` row while `pins_write`/`pins_drop` hold one row, so with two such rows the write destination is no longer the carrier's | 7 |
| M2 | MEDIUM | `tools/process-monitor/selftest.py:890` | `resolve_launcher` derives the Git root with a fixed three `dirname`s, which is wrong for the default `…/Git/cmd/git.exe` PATH entry — the live-tree arm SKIPs permanently from PowerShell | 6 |
| L1 | LOW | `tools/run-gates/derive-ceilings.py:341` | `parse_observed` refuses a tab and a newline in `--how` but not the reserved literal `runner`, so an out-of-band row can be written that every reader treats as runner-derived | 17, 10 |
| L2 | LOW | `tools/govkit/govkit.py:5842` | The renormalize post-condition takes `ln.split("\t")[-1]`, so a pinned path containing a TAB truncates, misses `_lfset2`, and silently leaves the `bad` population | 9 |

---

### B1 — BLOCKER — one out-of-tree receipt path turns the dirty-path guard off

`tools/govkit/govkit.py:4933`, inside `dirty_claimed_paths` (defined at `:4871`), reached through
`demand_claimed_paths_clean` (`:5050`) from `demand_writable_target` (`:5178`, calling at `:5188`).
Delivered finding 14, delivered `blocker`; adjudicated BLOCKER.

```python
def _names(*args: str) -> set[str]:
    out = subprocess.run(["git", "-C", str(target), *args, "--", *claimed],
                         capture_output=True, text=True)
    return {n for n in out.stdout.split("\0") if n}
```

`out.returncode` is read by nobody. `claimed` is filtered for empties at `:4929` and for nothing else.
Every claimed path goes into ONE pathspec, so a single path outside the repository makes git fail the
WHOLE invocation: measured in this worktree, `git ls-files -z -- <good> ../../evil` exits 128 and
`git diff --name-only -z -- …` exits 1, both with empty stdout. `in_index`, `in_head`, `staged` and
`unstaged` therefore all come back empty, every claimed path falls through carve-out 1/2 at
`:5018-5024` (absent from the index, present on disk), and the function returns `[]` — the byte-exact
shape of a clean tree.

Reproduced on a scratch repo at `4877af81`: `dirty_claimed_paths(t, ['tools/owned.txt'])` over an
uncommitted edit returns `['tools/owned.txt']`; `dirty_claimed_paths(t, ['tools/owned.txt',
'../../evil'])` returns `[]`.

The input is the target's own `.governance/install.json` — committed, hand-editable, text-merged, and
the artifact this build's whole threat model says gov distrusts. It is loaded with a bare
`json.loads` and no row-path validation, and **every containment refusal over receipt rows runs
LATER**: `demand_writable_target` is called at `:5301` (apply) and `:6687` (update), while
`demand_contained_rows` and `demand_contained_dest` sit at `:5358`, `:6891` and `:7227`. So the guard
is already neutralized by the time anything grades the row that neutralized it.

Two things this build did make it reachable. DEPL-cMendedVintage-24 widened the graded population from
`table` to `WRITING_DISPOSITIONS`, which pulls in the `attributes` row that DEPL-cMendedVintage-28's
own header names as the concrete escaping-path carrier. -28 then put containment ahead of the
untracked-shadow refusal *only*, inside a preamble that narrows with `--kits` — so
`govkit update --kits Y --write` never reaches the containment refusal for an escaping row belonging
to kit X, while `_names` still receives the whole receipt's paths. The run then proceeds to write
kit Y's legitimately-claimed paths over the operator's uncommitted work with no refusal, and a
green-to-red rollback restores the pre-run index entry over it.

The sibling batched reader already learned this. `index_read` (`:4636`) filters out-of-tree paths
lexically and carries a dead-probe refusal, added by DEPL-dSealedTally-4 S4 for exactly this reason.
This reader got neither half.

**Fix.** Both halves, because either alone leaves a hole:

1. Apply `index_read`'s lexical out-of-tree filter to `claimed` before the reads.
2. Assert the delegate. A non-zero `returncode` from `_names` is a DEAD PROBE and must refuse or
   raise — never an empty set, which reads as a clean population. §7's liveness rule says this in as
   many words.

Optionally also hoist the `demand_contained_dest` sweep over `derive_graded_rows(receipt)` into
`demand_claimed_paths_clean`, above `dirty_claimed_paths`, so the ordering -28 established holds for
both consumers of the widened set rather than for the one it was written against.

**Left-shift gate.** A selftest arm that seeds a fixture receipt with one legitimate row that is
dirty and one row whose path is `../../evil`, and asserts `update --write` REFUSES — it must fail
today, because the guard currently reports clean. Then the class gate, which is the part that
outlives this fix: a structural arm asserting every `subprocess.run(["git", …])` inside
`dirty_claimed_paths` and `index_read` has its `returncode` read on the same path that consumes its
stdout. Classes: `swallowed-delegate-reads-as-clean` (named by the diff's own checklist),
`vacuous-selector-empty-population`.

---

### H1 — HIGH — the containment scanner cannot see a write that is the last thing a function does

`tools/govkit/govkit.py:1135`, in `scan_uncontained_writes` (`:1047`), consumed by selfcheck arm 9.
Carries delivered findings 15 (`high`), 12 (`medium`) and 2 (`medium`); adjudicated HIGH, at the top
of the three, because the missed shape is the minimal write helper and because this arm is the
structural half of a closed BLOCKER.

```python
stop = fn.end_lineno or node.lineno
...
if not (isinstance(n, ast.Call) and node.lineno <= getattr(n, "lineno", 0) < stop):
    continue
```

`stop` defaults to the function's last line and the test is strict, so a mutating call sitting ON
that last line is excluded from its own binding's window by exactly one line. Measured against the
shipped predicate:

- `scan_uncontained_writes('def f(target, row):\n    dp = target / row["path"]\n    dp.write_text("x")\n')` returns `[]`
- the byte-identical source with one trailing statement appended returns `[(2, 'dp', 'row["path"]')]`
- the `dp.unlink()` variant on the closing line likewise returns `[]`

Arm 9 is the half of DEPL-cMendedVintage-23 written to OUTLIVE its two point fixes at the pins rewrite
and the withdrawal — the standing predicate that is supposed to red when the next write site is added
without a containment check. Its own staged break only ever puts the write mid-function, so the blind
spot is invisible to the arm that proves the predicate fires, and `r.note` prints a reassuring
`0 ungraded` over a shape it never looked at. That is this build's declared defect class arriving
inside a check written to catch that class.

Two honest bounds. No live escape is hidden today: re-running the same predicate over the current
`tools/govkit/govkit.py` with an inclusive window still yields `[]`. And the docstring's "WHAT THIS
DOES NOT ASSERT" paragraph enumerates the destination shapes the arm ignores and does not mention
this one — so it is an undeclared off-by-one rather than a stated limitation, which is why it is a
finding and not a note.

**Fix.** Separate the two intervals; they are not the same question. The rebinding narrowing keeps its
exclusive upper bound, because a rebinding line genuinely ends the previous binding's window. The
write scan does not:

```python
stop = fn.end_lineno or node.lineno          # narrowing loop unchanged, `node.lineno < ln < stop`
stop_write = stop + 1 if stop == (fn.end_lineno or node.lineno) else stop
```

or, more plainly, track the narrowed value and test `node.lineno <= call.lineno < stop_write` where
`stop_write` is `stop` when a rebinding narrowed it and `fn.end_lineno + 1` when nothing did.

**Left-shift gate.** Add the three-line last-statement offender to arm 9's own fixture — `def f(target,
row): dp = target / row["path"]; dp.write_text("x")` with nothing after it — and assert it is
REPORTED. Stage the break, confirm RED, unstage, per §7: this predicate has only ever been observed
passing on its own tree. Classes: `fixture-passes-by-finding-nothing`, `armed-but-unreachable-rule`.

---

### H2 — HIGH — an absent file reads as "nothing outside gov's region", so gov undoes the operator's deletion

`tools/govkit/govkit.py:4979`, in `derive_outside_region` inside `dirty_claimed_paths`; the write that
follows is at `:7720-7724`. Delivered finding 11, delivered `high`; adjudicated HIGH with the severity
discount stated below rather than applied silently. Introduced by DEPL-cMendedVintage-24 S2, in the
diff under review.

```python
if data is None:
    return ""
```

Reproduced on a scratch repo at `4877af81`. Committed `.gitattributes` holding only the
`# govkit:lf-pins` block; worktree copy unlinked, so `git status --porcelain` reads ` D .gitattributes`:

- `dirty_claimed_paths(t, ['.gitattributes'])` returns `['.gitattributes']`
- `dirty_claimed_paths(t, ['.gitattributes'], None, {'.gitattributes': (om, cm)})` returns `[]`
- zero-byte truncation gives the same `[]`
- the same file with `*.png binary` added alongside the block returns `['.gitattributes']`

So the hole is precisely the fresh-adopter shape `apply` creates: a `.gitattributes` gov made, holding
nothing else. The docstring's justification — "a file that is not there holds nothing outside gov's
region either" — is written for the HEAD side, where gov is creating a file that never existed.
Applied to the WORKTREE side it converts an operator's uncommitted deletion into clean.

The write is real, not theoretical. `demand_claimed_paths_clean` passes the region markers for the
`pins` row and does not refuse; the pins arm reads `pins_path.is_file()` false, takes `_cur = None`,
`write_block` creates the file and `git add` stages it, printing only that it wrote the lf-pin block.
Nothing names the reverted deletion. That is verbatim the hazard the refusal text at `:5117` states in
its own words. The asymmetry with carve-out 1 — which calls a STAGED deletion an operator decision and
reports it dirty — is what makes this a hole rather than a policy.

**The discount, stated:** the bytes lost are entirely gov's own generated block, so what the operator
loses is the ACTION, not unique content. The `high` is for the guard breach and the silence, not for
the data.

**Fix.** Distinguish "absent" from "present and empty outside the region" instead of folding both to
`""`. Return `None` from `derive_outside_region` when `data is None` — the caller already reads `None`
as not-eligible — and let the carve-out decline: a side that is absent while another side is present
is a difference the fold must not swallow.

**Left-shift gate.** A selftest arm staging a gov-only `.gitattributes` with its worktree copy removed,
asserting `update --write` REFUSES. Every existing arm uses a file with operator content alongside the
block, which is the one shape that cannot reach this branch — so the arm set today certifies coverage
it does not have. Classes: `fallback-fabricates-the-passing-value`, `fixture-passes-by-finding-nothing`.

---

### M1 — MEDIUM — the pin write's destination is no longer tied to the row that carries it

`tools/govkit/govkit.py:7068` (the slot), `:7228` (the rebinding), `:7277` (the carrier), with the
write sites at `:7723` and `:7764` and the snapshot at `:7644`. Delivered finding 7, delivered
`medium`; adjudicated MEDIUM. Introduced by DEPL-cMendedVintage-23 S2.

`-23` collapsed three per-row joins into one graded join, which was the right move — the duplication
was the defect's carrier. What it did not do is put the graded path ON the carrier. `pins_path` is
assigned at `:7228` for EVERY row whose role maps to the `pins` disposition; `pins_write` is assigned
at `:7277` only for a row graded `pins-moved`. With two `attributes` rows at different paths where an
earlier one is `pins-moved` and the LAST reads `current`, `pins_write` holds row A while `pins_path`
points at row B. `:7720-7723` then reads and writes B's file, `:7724` stages A's path, `:7731-7733`
stamps `mode`/`block_sha256`/`patterns` onto A's receipt row, `:7735` prints that the block was
written into A, and the snapshot takes its path from A. A's stale block is never repaired while its
receipt row and the run's own output both claim it was — the receipt-disagrees-with-the-tree class the
code at `:7726` says it exists to avoid.

The comment at `:7066` asserts only that `pins_path` is non-None whenever a carrier is set. The
stronger property the refactor silently relies on — that it is THAT carrier's path — holds only under
"one `attributes` row", which the comment at `:7059` calls true "by construction" and which nothing in
the engine enforces. There is no uniqueness refusal; `known_roles` grades gov's descriptors, not
receipts.

Two corrections to the delivered reasoning, neither fatal, both kept so the record is checkable:
`pins_write` and `pins_drop` still cannot both be set, because the branch test at `:7229` does not
depend on the row; and the rollback asymmetry is muted, because a `current` verdict means B already
holds the identical block and the splice is close to a no-op. Reachability is narrow — gov synthesizes
exactly one `attributes` row, hard-coded at `.gitattributes` — so two rows at different paths need a
hand edit or a text merge. That is the same untrusted-receipt threat model `:7190` states as the
reason `demand_contained_dest` was added, so it is in scope rather than hypothetical. Both paths pass
containment, so the escape is contained; the misdirection is not.

**Fix.** Carry the graded path on the carrier: `pins_write = (row, pins_path, _om, _cm, _text, pats)`
and `pins_drop = (row, pins_path)`, unpacking the path at each write site. Additionally, refuse in the
`_cmd_update` preamble a receipt whose `files` carry more than one row with `role == "attributes"` —
that is the invariant `:7059` already claims, and claiming it is not enforcing it.

**Left-shift gate.** A selftest arm with a two-`attributes`-row receipt, the first `pins-moved` and the
second `current` at a different path, asserting either the uniqueness refusal fires or the block lands
at the first row's path. Classes: `two-guards-one-question-two-answers`, `armed-but-unreachable-rule`.

---

### M2 — MEDIUM — the live-tree arm resolves its launcher from an assumption about where git lives

`tools/process-monitor/selftest.py:890`. Delivered finding 6, delivered `medium`; adjudicated MEDIUM.
Shipped by TOOL-cMendedVintage-11.

```python
git = shutil.which("git")
if git:
    home = os.path.dirname(os.path.dirname(os.path.dirname(git)))
    candidates += [os.path.join(home, "usr", "bin", "bash.exe"),
                   os.path.join(home, "bin", "bash.exe")]
```

Three `dirname`s is correct for `…/Git/mingw64/bin/git.exe` and wrong for `…/Git/cmd/git.exe`, which
is the default Git-for-Windows PATH entry and needs two. Verified by running the shipped function both
ways in this worktree. From PowerShell: `which('git')` is `C:\Program Files\Git\cmd\git.EXE`, `home`
becomes `C:\Program Files`, and `resolve_launcher()` returns
`(None, ['bash', 'C:\\Windows\\system32\\bash.EXE', 'C:\\Program Files\\usr\\bin\\bash.exe',
'C:\\Program Files\\bin\\bash.exe'])` — both git-derived candidates are non-existent paths, and
`which('bash')` there is WSL, which answers neither MINGW nor MSYS nor CYGWIN. From Git Bash,
`which('git')` happens to sit one level deeper and the launcher resolves.

So `test_live_tree_dies_completely` — the arm whose docstring says it is what the whole build exists
for — SKIPs on any node whose PATH carries Git's `cmd` directory. The fallback fails in exactly the
situation it was written for: the case where `which('bash')` answers WSL.

**Scope, stated straight, because it is narrower than "permanently".** `tools/process-monitor/kit.toml`
runs the leg as `python {kit}/selftest.py` under `run-gates.sh`, i.e. from Git Bash, where the arm does
run. **The merge bar is unaffected.** What degrades is the ordinary PowerShell invocation, which is
this project's primary shell, and it degrades to a skip that announces itself — so this is lost
coverage, not a false green. TOOL-cMendedVintage-11 replaced an arm that read a working product as
broken with one that, on the common Windows invocation, never runs at all, and it measured green
because it measured from Git Bash.

**Fix.** Stop assuming a fixed depth. Resolution here is by EXECUTION, so a bogus candidate costs one
failed `subprocess.run` and nothing else — just add the two-parent form beside the three-parent one:

```python
for up in (2, 3):
    home = os.path.normpath(os.path.join(os.path.dirname(git), *([os.pardir] * up)))
    candidates += [os.path.join(home, "usr", "bin", "bash.exe"),
                   os.path.join(home, "bin", "bash.exe")]
```

**Left-shift gate.** The arm already reports the candidates it ran, which is why this was findable at
all. Make the report a verdict: a second leg (or a `kit.toml` row) that runs the same selftest with
`PATH` reduced to the `cmd`-style entry and asserts the live-tree arm RUNS rather than skips. Failing
that, a documented manual check in the kit README that the arm is skip-prone off the bar. Classes:
`subprocess-resolves-a-different-shell`, `fixture-inherits-ambient-machine-state`.

---

### L1 — LOW — the reserved provenance spelling is asserted in prose and refused nowhere

`tools/run-gates/derive-ceilings.py:341`, with the write at `:490` and the readers at `:566` and
`:593`. Carries delivered findings 17 and 10, both `low`; adjudicated LOW. Shipped by
TOOL-cMendedVintage-17.

`parse_observed` refuses an empty `--how`, a tab and a newline, on the stated ground that both bytes
are STRUCTURE in a tab-separated artifact. It does not refuse the one value that forges the column's
MEANING: the literal `runner`, which is `RUNNER_SOURCE` at `:93`. `:490` stores `args.how.strip()`
verbatim, so `--write --observed 'leg=900' --how runner` produces a row whose sixth field is
byte-identical to a row this tool derived from the run record, and `read_evidence` at `:308` cannot
tell them apart either — it only defaults an ABSENT sixth field.

Two live consequences. `cmd_check`'s `row[4] == RUNNER_SOURCE` branch at `:566` applies the "REACHED in
a recorded run … a LOWER BOUND on the work" verdict to a number nobody watched the runner produce —
the precise sentence TOOL-cMendedVintage-17's own comment says is FALSE of an out-of-band reading and
deliberately withdrew for typed ones. And the out-of-band roll-up at `:593` excludes the row, so the
green line reports "0 of them out-of-band" over a hand-typed number. The module docstring at `:45` and
the generated artifact header at `:509` both assert the out-of-band row "is never allowed to look like
the in-band one". That claim is written, not enforced.

Weakest point, kept: the REACHED branch is a strict sub-case of the headroom branch, so the pass/fail
verdict is unchanged — the damage is the wrong refusal sentence plus a permanently forged provenance
claim in a tracked artifact, reachable through the sanctioned command with no hand-edit. A direct
hand-edit of the file writes the same bytes with no gate detecting it, so reserving the literal closes
one door of several. Accidental reach is plausible: an operator who ran the leg through the runner
manually, outside the retained window, would reasonably answer `--how runner`.

**Fix.** One line beside the existing tab/newline refusal:

```python
if how.strip().lower() == RUNNER_SOURCE:
    sys.exit(f"derive-ceilings: --how may not be '{RUNNER_SOURCE}' — that spelling is reserved for a "
             f"reading this tool derived from the run record")
```

**Left-shift gate.** `tools/run-gates/run-gates.evidence.test.sh` already grades exactly this
distinguishability at its lines 928-940; extend that arm to run `--write --how runner` and assert the
command REFUSES. The arm exists, it grades the right property, and it never tried the one input that
defeats it. Class: `two-answers-to-one-question` (the header asserts the property, the code permits its
negation).

---

### L2 — LOW — the renormalize post-condition still splits a path, one shape further in

`tools/govkit/govkit.py:5842-5843`. Delivered finding 9, delivered `low`; adjudicated LOW. This is the
residual of exactly the class DEPL-cMendedVintage-25 closed here.

```python
bad = [ln.split("\t")[-1] for ln in idx.split("\0")
       if ln and ln.split("\t")[-1] in _lfset2 and "i/lf" not in ln.split()[0]]
```

`-25` moved this read to `git ls-files --eol -z`, which fixed the space and C-quoting halves, and the
comment at `:5830-5834` states "the fields stay tab-separated" — true of the record's own separator,
and the path is the field AFTER it. Measured record shape on this tree,
`git ls-files --eol -z -- AGENTS.md | cat -A`: `i/lf    w/lf    attr/text eol=lf      ^IAGENTS.md^@` —
exactly one `^I`, immediately before the path, every earlier gap a space, and `-z` disables quoting so
the path arrives raw. `[-1]` therefore takes the tail after the last tab, which for a path containing a
TAB is a truncated name never present in `_lfset2`. The record drops out of `bad`, no `r.fail` fires,
and the step prints its reassuring count for a population it did not cover.

The population really can reach that set: `eol_population` fills `lf_paths` from `git ls-files -z` plus
`check-attr --stdin -z`, both NUL-framed, so a tab-bearing path arrives intact — the truncation happens
only here, in the post-condition.

Caveat kept straight: the trigger is one filename shape, a TAB in a tracked path, impossible on Windows
(char 9 is a forbidden NTFS name byte) and pathological on POSIX, and the consequence is an unreported
diagnostic row rather than a wrong write. It stands at `low` because it is reachable on a POSIX adopter
and because it is the same green-by-absence class this very post-condition was just rewritten to close.

**Fix.** Split once from the left, which is exact for this format and cannot be confused by a path:
`ln.split("\t", 1)[1]` in both the value and the membership test.

**Left-shift gate.** A selftest arm on POSIX pinning a path with a TAB in its name and asserting the
post-condition REPORTS it; skipped-with-a-reason on Windows, where the filename cannot exist, so the
skip announces itself rather than reading as coverage. Class: `structured-record-split-on-whitespace`.

---

## What this round did NOT grade

Stated because a review's silence is otherwise read as coverage.

- **Round 1's nine findings.** Out of scope by instruction, all adjudicated and disposed, four of them
  into DEPL-cMendedVintage-22 through -25. This record re-reports none of them, and B1 above is a
  DIFFERENT defect in the function round 1's B3 widened, not a re-report of B3.
- **The deployer suite's 34 red arms.** Pre-existing, traced by the build to a read-only attribution
  to a check-wiring file added two builds ago, plus one stale byte-literal and one liveness threshold
  of 3 over a population of 2. `tools/unattended/check-unattended.test.sh` is separately red at 23,
  also pre-existing and proved so against `git show HEAD:`. Not findings, and not re-verified here.
- **The full bar with `GATE_SELFTESTS=1`.** It does not fit its six-hour wall on this four-core node,
  so no total green underwrites this record. Three of the seven findings above are in code no leg on
  this tree exercises anyway, because gov is not a govkit target.
- **Whether the seven fixes above are correct.** Each names a fix and a left-shift gate; none has been
  implemented or staged-and-reddened. §7 says a gate is not landed until its failing case has been
  observed, and that observation is owed by the units that take these findings, not by this record.
