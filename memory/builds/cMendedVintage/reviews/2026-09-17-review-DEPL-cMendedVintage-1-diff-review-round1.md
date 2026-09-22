**Serves:** diff-review DEPL-cMendedVintage-1 DEPL-cMendedVintage-2 DEPL-cMendedVintage-3 DEPL-cMendedVintage-4 DEPL-cMendedVintage-5 DEPL-cMendedVintage-6 DEPL-cMendedVintage-7 DEPL-cMendedVintage-8 DEPL-cMendedVintage-9 DEPL-cMendedVintage-10 DEPL-cMendedVintage-11 DEPL-cMendedVintage-12 DEPL-cMendedVintage-13 DEPL-cMendedVintage-14 DEPL-cMendedVintage-15 DEPL-cMendedVintage-16 DEPL-cMendedVintage-17 DEPL-cMendedVintage-18 DEPL-cMendedVintage-19 DEPL-cMendedVintage-20 DEPL-cMendedVintage-21 TOOL-cMendedVintage-1 TOOL-cMendedVintage-2 TOOL-cMendedVintage-3 TOOL-cMendedVintage-4 TOOL-cMendedVintage-5 TOOL-cMendedVintage-6 TOOL-cMendedVintage-7 TOOL-cMendedVintage-8 TOOL-cMendedVintage-9 TOOL-cMendedVintage-10

# cMendedVintage — closing diff review of the 31-unit build

*Node `c`, 2026-09-17. A Tier-2 adversarial pass over the cumulative diff landing on
`branch/govkit-update-rollbacks-0502c4`: a parallel fan of primed finder lenses, a skeptic stage
prompted to REFUTE each finding, one synthesis. Every citation a surviving finding rests on was
re-opened in this worktree at `b6cc8f6f4e511a8d9eddbd3a7835170425335ab6` before this record was
written; where a delivered finding got a detail wrong, the correction is named inside the finding
rather than quietly applied.*

**Reviewed range:** `859daa67e728ae273d5278536fb462c04077f16f...HEAD` (HEAD =
`b6cc8f6f4e511a8d9eddbd3a7835170425335ab6`), 189 changed files, ~18900 insertions, 31 units.

## Verdict: BLOCKED

Three BLOCKER findings, all in `tools/govkit/govkit.py`, all in code this build added or newly made
reachable. One of them — the gate-leg drift guard — is armed by a descriptor change shipped in this
same diff, so it fires on adopters who did nothing wrong and cannot be cleared by re-running either
verb. The other two are a missing containment check on a new write site whose sibling rollback IS
guarded, and a safety refusal whose stated justification this diff invalidated without widening the
refusal. None of them is reachable in THIS repository, because gov does not dogfood govkit and there
is no `.governance/install.json` here; all three are reachable on the first adopter target that takes
this vintage. That asymmetry is the reason the build's own ledgers record so many criteria as OWED,
and it is also the reason a green bar on this tree is not evidence against any of the three.

**Review shape.** Raw 17, confirmed 15, refuted 2, unverified 0, precision 0.88.

**Run integrity.** Lenses 4/4 returned, 0 DIED. Skeptic batches 5/5 returned, 0 DIED. 0 contradictory
verdicts demoted to unverified, 0 spurious verdicts discarded, 0 duplicates. The finding set is
COMPLETE as delivered — every lens and every skeptic batch came back, so a zero count in any lens's
territory is evidence rather than a gap.

**Consolidation, stated so the arithmetic is checkable.** The 15 confirmed findings describe 9
distinct defects: four lenses independently found the renormalize word-split, three independently
found the gate-leg drift comparison, and two independently found the `legs_withheld` flag. Nothing was
dropped in the merge — every one of the 15 is represented below, and the merged entries name the
finding ids they carry. The severity in the table is the one adjudicated HERE, and it differs from the
delivered severity in two places, both named in the row. Counts in this report: **BLOCKER 3 · HIGH 1 ·
MEDIUM 2 · LOW 3**, nine findings.

## Findings, severity-ranked

| # | Sev | Site | Defect | From |
|---|-----|------|--------|------|
| B1 | BLOCKER | `tools/govkit/govkit.py:2728` | Gate-leg drift guard compares the receipt against gov's own re-resolution — fires on every gov-side argv change, never on the target edit its message names, and wedges the target permanently | 6, 10, 14 |
| B2 | BLOCKER | `tools/govkit/govkit.py:7209`, `:7245` | The new lf-pin write joins a receipt-supplied path onto the target root with no containment check, while the rollback for that same row IS guarded | 1 |
| B3 | BLOCKER | `tools/govkit/govkit.py:4798` | `demand_claimed_paths_clean` still excludes the `attributes` row on the ground that `update` never writes it — which this same diff made false | 2 |
| H1 | HIGH | `tools/govkit/govkit.py:8562`, `:5493` | The renormalize cleanliness guard word-splits `git diff --name-only`, so a dirty pinned path with a space or a non-ASCII byte is invisible and its uncommitted content is staged | 3, 8, 11, 15 |
| M1 | MEDIUM | `tools/govkit/govkit.py:2833` | The non-manifest gate-legs order is rewritten from `selection` alone, so a scoped or rolled-back `update` deletes every out-of-scope kit's instruction | 7 |
| M2 | MEDIUM | `tools/govkit/govkit.py:7210`, `:7247` | The target's `.gitattributes` is read with `errors="replace"` under universal newlines and rewritten whole — a lossy rewrite of lines gov does not own, against a header that promises the opposite | 5 |
| L1 | LOW | `tools/govkit/govkit.py:2656` | The malformed-runner branch returns `legs_withheld = False` for a run that emitted nothing and carried the previous rows forward | 12, 16 |
| L2 | LOW | `tools/check-install-prefix.sh:202` | Epoch 4's record says it widened "the LEAD class both regexes share"; only `re_ship` moved | 13 |
| L3 | LOW | `memory/map/features/run-gates.md:106` | The dossier says the receipt leg has four built-in fixture arms; it has six, and says so itself | 17 |

---

### B1 — BLOCKER — the gate-leg drift guard is an assertion between two derived values

`tools/govkit/govkit.py:2728`, with the trigger at `tools/gate-lint/kit.toml:64` and the new caller at
`tools/govkit/govkit.py:8635`. Carries delivered findings 6, 10 and 14; adjudicated BLOCKER, above the
`high` all three were delivered at, because the trigger ships in this diff and the resulting state is
not recoverable by the operator.

```python
prev = next((e for e in owned and prior if e["name"] == nm), None)
if prev and (prev.get("argv") != argv or prev.get("guard", []) != guards):
    r.fail(f"leg '{nm}' in the target differs from what the receipt recorded — ...")
    continue
existing[by_name[nm]] = row
```

`prior` is `receipt["gate_runner"]["emitted"]` — gov's record of what gov last wrote. `argv` and
`guards` are this run's fresh resolution of gov's own descriptor. Both sides come from gov. The
target's actual manifest row, `existing[by_name[nm]]`, is read by nothing; it is only assigned, at
:2734. So the guard is the `assertion-between-two-derived-values` class exactly, and it is wrong in
both directions at once.

The direction that is wrong on the way in: a target that hand-edits a row gov owns is never detected,
and :2734 silently overwrites it. That is the class the failure message claims to report, and it is
also a violation of the build's own stated invariant that gov never writes through a path a target
declared its own. `tools/govkit/selftest.py:1384-1388` already records the gap in its own words —
"tampering the RUNNER changes neither side and apply silently repairs it" — so this is the code's own
admission, recorded as a fixture inconvenience rather than as a defect.

The direction that is wrong on the way out is the blocker. Commit `f1a05f8e` shipped
`argv = ["python3", "{kit}/sh_hygiene.py", "{memory_root}/project/substitution-fed-loops.txt"]` for
the leg `shell hygiene (a loop fed by a command substitution)`; `3ca2f144` in THIS build drops the
third element. Any adopter who applied in that window now holds the three-element argv in their
receipt, so `prev.get("argv") != argv` is true on a manifest that is byte-identical to what gov wrote.
`r.fail` plus `continue` makes `len(r.problems) == _legs_problems_before` false at :2757, which
withholds the ENTIRE manifest for every healthy leg in the run; the withheld path then writes
`emitted = list(prior)` at :2802, which `update` stamps straight back into `install.json` on the
`if r.problems:` write at :8766. The next run compares identically. `apply` calls the same function at
:5590 with the same `prior`, so the documented fallback does not clear it either, and the error text
names no recovery. `tools/gate-lint/kit.toml:22-28` makes it worse by telling the adopter to answer
the newly-red leg by putting the path back into their own argv — a gov-emitted name, hence in `owned`,
hence clobbered on the next `update --write`.

DEPL-cMendedVintage-13 doubled the blast radius by making `update` a second caller of this function at
:8635. The same mechanism was already reproduced end-to-end as a HIGH in
`memory/builds/aPacedTurnstile/reviews/2026-08-18-review-TOOL-aPacedTurnstile-1-run-cumulative.md`
(D3, "the target is permanently wedged"); that fix went to the offending kit row rather than to the
predicate, so the class survived and this build re-armed it.

**Fix.** Compare what the message says it compares:

```python
tgt = existing[by_name[nm]]
if prev and (tgt.get("argv") != prev.get("argv")
             or tgt.get("guard", []) != prev.get("guard", [])):
    r.fail(...); continue
existing[by_name[nm]] = row
```

`prev` stays the ownership record; the comparison subject becomes what is on disk. When the target's
row still equals what gov wrote, gov owns it and may replace it with `row` whatever gov's new argv is.

**Left-shift gate.** Two selftest arms, neither of which exists today, because the current arm tampers
the RECEIPT and so exercises neither case: (1) a fixture whose manifest equals the receipt, with only
the DESCRIPTOR's argv moved — assert the row is REPLACED and the manifest is written; (2) a fixture
whose manifest row is hand-edited away from the receipt — assert the drift `r.fail` fires. Arm (1) is
the regression gate for this finding and arm (2) is the coverage the message has never had. Class:
`assertion-between-two-derived-values`; both arms also close
`shipped-checker-edit-is-an-adopter-contract-change` for this function.

---

### B2 — BLOCKER — the new lf-pin write escapes the target root

`tools/govkit/govkit.py:7209` and `:7245`. Delivered finding 1, delivered `high`; adjudicated BLOCKER
because it writes outside the operator's repository and because the identical class was closed at
three other sites in this same diff.

```python
_pw_path = target / _pw_row["path"]            # 7209
_pw_path.write_text(_pw_new, encoding="utf-8", newline="\n")   # 7213
_pd_path = target / pins_drop["path"]          # 7245
```

`_pw_row["path"]` and `pins_drop["path"]` come straight off the `attributes` row of
`.governance/install.json` — a committed, hand-editable, text-merged file in a repo gov does not own.
Nothing upstream grades it. `demand_contained_dest` is called at :2398, :2462, :3964 and :8227 and
none of those sees this row. `index_read` deliberately FILTERS out-of-tree paths rather than raising
on them (its own header says so), so the snapshot read is not a gate either. The write loop's own
containment check at :7275 is unreachable for this row, because the pins arm of the classification
loop sets `pins_write`/`pins_drop` and `continue`s at :6762 and :6778, so the row never enters `acted`.

With a value like `../../evil` or `C:/x/evil`, `find_block` finds no marker pair, the verdict is
`pins-moved`, and `write_block(None, ...)` returns `block + "\n"` with mode `created` — gov creates a
file outside the target repository. The inconsistency is checkable and is the reason this is a
blocker rather than a hardening note: the rollback for this exact row guards its paths with
`demand_contained_dest(p, ...)` at :8227, so the diff guards the undo of a write it does not guard.
That is `containment-tested-one-way` and `two-guards-one-question-two-answers` in one site.

**Fix.** Grade the row once, in the S9 receipt-integrity preamble, so the classification read at :6767
is covered too. If that is too large a move for a closing fix, the minimum is
`demand_contained_dest(_pw_row["path"], "the receipt's attributes row")` before :7209 and the same for
`pins_drop["path"]` before :7245.

**Left-shift gate.** A selftest arm that writes an `attributes` row with `path = "../escape"` into a
fixture receipt and asserts `update --write` REFUSES — and, because the same read happens at :6767,
asserts it refuses before any byte lands. Then a structural arm that is the real left-shift: assert
every `target / <value-from-the-receipt>` join in `govkit.py` is preceded by a `demand_contained_dest`
on the same expression, so the next write site cannot be added without one. The existing four call
sites make that predicate cheap to write and it would have reddened on this diff.

---

### B3 — BLOCKER — the dirty-path refusal still excludes the row this diff taught `update` to write

`tools/govkit/govkit.py:4798`, with the header above it at :4770-4774. Delivered finding 2, delivered
`high`; adjudicated BLOCKER because the outcome is destruction of an operator's uncommitted work in a
repository gov does not own, which is the exact hazard the function exists to prevent.

```python
_rows = [row for row in ((receipt or {}).get("files") or [])
         if UPDATE_ROLE.get(row.get("role", "engine")) == "table"]
```

`UPDATE_ROLE["attributes"]` is `"pins"` (:5745), so the `.gitattributes` row is excluded. The
function's own header justifies that in as many words: "`UPDATE_ROLE["attributes"]` is `pins`,
documented in that table as `recompute, compare, report; never write`, so a `.gitattributes` row can
never be that write." As of DEPL-cMendedVintage-10, in this same diff, `update --write` writes that
file at :7213 and :7251 and `git add`s it at :7214 and :7254. The justification is false and the
carve-out is now the one hole in the guard, sitting exactly where the new write landed. This is
`amendment-leaves-its-other-half-standing` with the halves in two different units.

The consequence chain is intact end to end. The row is snapshotted with its PRE-RUN index entry
(`_pins_snap`, origin `attributes`, :7145-7149). `.gitattributes` is explicitly added to
`written_paths` at :8075-8077. The rollback loop iterates snapshot rows with `x["origin"] ==
"attributes"` for every rolled-back kit (:8204-8205) and restores via `update-index --cacheinfo` then
`checkout-index -f` (:8256-8275) — and the code's own S4 comment at :8274 records that
`checkout-index -f` unlinks the existing file before writing the replacement. So on a normal run gov
silently stages the operator's uncommitted `.gitattributes` edits, and on any green-to-red rollback it
destroys them outright.

**Fix.** Add `attributes` to the population `demand_claimed_paths_clean` grades, or put a dedicated
dirty check on the attributes row's path immediately before the pin write. Then delete the "never
write" paragraph in the header — leaving it standing invites the next reader to re-derive the
conclusion that produced this hole. Note that the `-12` carve-out reasoning recorded in that same
header (an `attributes` row carries no `oid`, so `dirty_claimed_paths` has nothing to compare) is the
real constraint to design around: the row needs a comparison the guard can actually make, not just
membership in the list.

**Left-shift gate.** A selftest arm that dirties `.gitattributes` in the fixture target and asserts
`update --write` REFUSES rather than staging it; and a second arm that dirties it, forces a kit's
check green-to-red, and asserts the operator's bytes survive. Class-level left-shift, cheaper and
stronger: assert that every path in `written_paths` is a member of the population
`demand_claimed_paths_clean` graded — one predicate over two existing sets, which reds automatically
the next time a verb learns to write a role it previously only read.

---

### H1 — HIGH — the renormalize cleanliness guard word-splits its own input

`tools/govkit/govkit.py:8562`, sibling at `:5493`. Carries delivered findings 3, 8, 11 and 15 — four
lenses, independently, which is itself a signal about how visible this one is.

```python
_rn_dirty = [p for p in _rn_diff.stdout.split()
             if p in _rn_set and p not in _rn_ours]
```

`_rn_diff` is `git diff --name-only HEAD`; `.split()` splits on arbitrary whitespace rather than on
lines. `_rn_set` comes from `eol_population`, which reads `git ls-files -z` and `check-attr --stdin
-z` (:3844-3856) and therefore holds raw, unquoted paths. Reproduced in a scratch repo by two
reviewers independently: a dirty `a b.txt` prints unquoted on its own line, so `.split()` yields `a`
and `b.txt`, neither of which is in `_rn_set`; a non-ASCII name prints C-quoted under the default
`core.quotePath`, so the single token never matches the raw path either. `_rn_missing` cannot catch
either case — it iterates `_rn_lf` and the file exists.

The guard therefore passes, the run takes the `elif _rn_lf:` arm, and
`git_pathspec(target, ["add", "--renormalize"], _rn_lf)` re-adds from the WORKING TREE — folding the
operator's uncommitted content into the index of a repository gov does not own, which is verbatim what
the `r.fail` two lines above says it exists to refuse. The population is not narrow: `eol_population`
returns every tracked path carrying an `eol` attribute, so an adopter with a broad `* text eol=lf`
rule has their whole tree in `_rn_lf`.

Adjudicated HIGH rather than BLOCKER only because the trigger needs a dirty pinned path whose name
carries a space or a non-ASCII byte at run time. The defect and its outcome are concrete, and this is
`structured-record-split-on-whitespace` in a file that already has a gotcha for it.

**Fix.** Run the diff unambiguously and split on NUL, at both sites:

```python
subprocess.run(["git", "-C", str(target), "-c", "core.quotepath=false",
                "diff", "--name-only", "-z", "HEAD"], capture_output=True, text=True)
... _rn_diff.stdout.split("\0")   # drop the empty tail
```

`_cmd_apply`'s `dirty = [p for p in _alldiff.stdout.split() ...]` at :5493 carries the identical bug
and has already diverged from this copy in other respects (`_rn_gone` subtracts `deleted`, `apply`'s
does not). Two spellings of one safety check is this repo's `second-implementation-is-not-a-second-opinion`
class; the correct fix extracts the shared body — population, dirty/missing guard, `git_pathspec`
call — into one helper both verbs call, with the `deleted` exemption as a parameter.

**Left-shift gate.** A fixture arm with a pinned path named with a space, left dirty, asserting the
refusal fires — run against BOTH verbs, which is the arm that makes the shared helper pay for itself.
The class-level version is a lint over `govkit.py` banning `.split()` on the stdout of any `git`
invocation that is not `-z`: cheap, and it would have reddened both sites.

---

### M1 — MEDIUM — the non-manifest gate-legs order drops every out-of-scope kit

`tools/govkit/govkit.py:2833`. Delivered finding 7, severity unchanged.

The `else:` branch builds `lines` from scratch, loops `for eid in selection` only, never reads the
existing file, and writes it whole. `_cmd_update` passes
`_legs_scope = [e for e in claimed if (not kits or e in set(kits)) and e not in _rolled_kits]`
(:8623). So on a target whose `deploy.toml` declares no `[gate_runner]` or declares `kind = "none"` —
`validate_gate_runner` returns cleanly for both (:3926, :3941) — an `update --write --kits memory-tree`
against a receipt claiming five kits rewrites `.governance/outbox/gate-legs.md` with memory-tree's
rows and the fixed trailer, deleting the other four kits' instructions. Nothing notices: `update`
writes no `orders` row, and `cmd_check`'s outbox arm only asserts that a recorded order EXISTS.

The branch's own S7 comment claims "this refresh costs the reader nothing", which is false on a scoped
run. The manifest branch was given `carry_out_of_scope=True` for precisely this (docstring
:2602-2606), and the conflict-order reap at :8500 explicitly SKIPS on a scoped run for the same
reason. The order branch got neither guard — the "one branch over" shape this function's own D7
comments name twice, and which the `emitted = list(prior)` comment fifteen lines below is itself a
previous instance of.

**Fix.** Either carry forward — merge the previous file's `- <name>: <argv>` lines for kits outside
`selection` before writing — or gate the whole non-manifest write on an unscoped, rollback-free run
and print a WITHHELD line naming the scope when it is skipped, which is the shape the reap at :8503
already uses.

**Left-shift gate.** A fixture with two claimed kits and no `[gate_runner]`: run `update --write
--kits <one>` and assert the other kit's rows are still in `gate-legs.md`. The class-level left-shift
is an arm asserting that every branch of `write_gate_legs` is scope-aware — the manifest branch has
`carry_out_of_scope`, the reap has its skip, and this branch had neither, so a parity arm over the
three is what stops the next one being added bare.

---

### M2 — MEDIUM — the `.gitattributes` rewrite is lossy, against a header that says it is not

`tools/govkit/govkit.py:7210` and `:7247`. Delivered finding 5 at `medium`; the skeptic's honest
narrowing is carried forward rather than dropped.

`Path.read_text(encoding="utf-8", errors="replace")` opens with `newline=None`, so universal-newline
translation collapses CRLF and CR to LF and any invalid byte becomes U+FFFD. `write_block` returns the
WHOLE file text, and the subsequent `write_text(..., newline="\n")` at :7213 — and the
`"\n".join(_pd_lines[...])` write at :7248 — persist that for every line including the target's own,
then `git add` it. Three lines above the withdrawal's read, its own header asserts the opposite:
"NOTHING OUTSIDE THE REGION IS READ OR REWRITTEN, and nothing is normalized: the surviving lines are
the file's own, rejoined." A reader budgets against a guarantee the code does not hold.

Stated honestly, and this is why it is not higher: `apply` carries the identical construction at
:5108-5110, so this is a shared pre-existing class rather than something new here, and the common
outcome — a Windows adopter's CRLF `.gitattributes` rewritten whole to LF and staged — is noisy rather
than destructive. The genuinely lossy U+FFFD case needs a non-UTF-8 `.gitattributes`. What is
confirmed is the gap between the code and its stated guarantee, and the real whole-file rewrite. Note
that it compounds B3: the operator cannot recover the pre-run bytes from the rollback, because the
rollback restores the index blob over the worktree.

**Fix.** Read and write `.gitattributes` as bytes, or with `errors="strict"` and `newline=""`, splice
only the marked line range, and refuse rather than replace on a decode error. If byte fidelity is
genuinely out of scope, correct the header so it stops claiming it — a false guarantee beside working
code is worse than no guarantee.

**Left-shift gate.** An arm whose fixture `.gitattributes` holds a CRLF line and a non-UTF-8 byte
outside gov's block, asserting those bytes are unchanged after `update --write`. Class:
`text-mode-read-eats-a-bare-cr` and `worktree-crlf-outside-the-gated-population`, both already in this
repo's checklist, neither currently armed against govkit's own writes.

---

### L1 — LOW — `legs_withheld: False` on a run that withheld its legs

`tools/govkit/govkit.py:2656`. Carries delivered findings 12 and 16.

On the `refuse_bad_runner=False` path — `update` only, :8636 — a malformed runner file takes `r.fail`
and then `return prior, False`: the previous run's rows carried forward, nothing emitted, and the flag
saying not withheld. It bypasses the only site that sets the flag, `_legs_withheld = True` at :2803.
The caller stores it at :8641-8644, and the receipt IS persisted on this path — `r.problems` is
non-empty, so the `if r.problems:` branch at :8766 writes `install.json` before returning, withholding
the schema and `gov_commit` re-stamp rather than the file. The field's own comment at :2613-2618
defines its purpose as letting a later reader tell "a run that wrote its legs from one that carried
the previous run's rows forward", and says that without it "the withheld fact lives only in stdout
nobody kept". This run is precisely the latter and the only durable record says otherwise. Reachable
through any hand-edited or truncated `gate-legs.json` during `update`, which is exactly the residue
that branch was added for.

Low because nothing reads the field programmatically today (only `selftest.py:1434` asserts it), so
the harm is record fidelity for a human reader. It is still `one-value-field-records-a-mixed-outcome`,
and it is on the verb whose bytes are already on disk when the branch is reached.

**Fix.** `return prior, True`. If the intent is to distinguish "withheld by findings" from "withheld
by a malformed runner", make it a string state rather than a bool that is wrong about both.

**Left-shift gate.** Extend the existing `selftest.py` malformed-runner arm to assert the receipt's
`legs_withheld` is true, not merely that the run failed — the arm is already there and grades one
field short.

---

### L2 — LOW — epoch 4's record overstates which regexes it widened

`tools/check-install-prefix.sh:202`, with the epoch block at :368-375. Delivered finding 13.

Line 202 is still `RE="(^|[^/{}[:alnum:]._-])($alt)/[A-Za-z0-9_.-]+\.($EXT)"` — `-` remains in the
excluded lead class — while :417's `re_ship` is `"(^|[^/{}[:alnum:]._])tools/..."` without it. The
epoch-4 entry states it "Drops `-` from the LEAD class both regexes share", and the inline note at
:413 repeats the claim. Only `re_ship` moved, so arm 1 still cannot see `${VAR:-<kit>/file.py}`; the
`:+` and `:=` cousins do reach it, since `+` and `=` were never excluded.

Measured rather than asserted: widening arm 1's class the same way adds exactly one hit over the whole
tracked tree at HEAD (`memory/map/FOUNDATION.md:34`), which is outside arm 1's shipped-file
population. So today's coverage loss is nil — this is a stale record plus a latent gap, not a live
miss. It is the same shape as the `EXT` note twelve lines above it, which exists because one predicate
written twice gets widened once, and it is the failure mode the S1 comment at :187 names by hand.

**Fix.** Either drop `-` from `RE` too — measured cost zero new hits in arm 1's population — and leave
the comment as written, or hoist the lead class into one `LEAD="[^/{}[:alnum:]._]"` both regexes
interpolate, the treatment `EXT` already gets, and reword the epoch block to name which arm it moved.

**Left-shift gate.** The hoist IS the gate: one variable cannot be widened in one place. If the hoist
is declined, an arm asserting both regexes carry the same lead class is the cheap substitute. Class:
`two-answers-to-one-question`.

---

### L3 — LOW — the dossier counts four fixture arms and the leg has six

`memory/map/features/run-gates.md:106`. Delivered finding 17.

The dossier says the new `receipt sync` leg's "four built-in fixture arms are the only part of it any
gov bar grades". `check_fixtures` in `tools/run-gates/check-receipt.py` appends six results
(:152, :158, :165, :171, :182, :191), its own docstring at :139 says "The six built-in arms", and the
checker prints `fixtures: 6/6 arm(s) ok`. Both halves landed in the same commit, `8b40e1d1`, and
disagree with each other. The subset reading — four `check_engine_rows` arms against two
`print_unattributed` arms — does not save it, because the sentence makes an all-of-them claim and the
two `print_unattributed` arms are built-in fixture arms graded on the same run.

No runtime effect; the harm is that a reader auditing the leg's coverage from the dossier is told two
arms fewer than exist, and the number will be wrong again on the next arm. It is the charter's own
"NO count of a derived population is written in prose", broken in the file that documents the bar.

**Fix.** Drop the number: "its built-in fixture arms are the only part of it any gov bar grades". The
leg already prints `fixtures: N/N arm(s) ok` on every run, which is the answer that cannot rot.

**Left-shift gate.** The map's freshness leg already reads these dossiers; a predicate banning a
written-out cardinal immediately before "built-in", "arm(s)", "leg(s)" or "fixture" in
`memory/map/features/*.md` is a narrow, low-false-positive version of the rule the charter states in
prose. Class: `two-answers-to-one-question`.

---

## Refuted, and why they are recorded

Two of the seventeen raw findings were refuted by the skeptic stage and are not carried. They are not
listed with their reasoning here because the refutation is what the stage is for and re-litigating it
in the permanent record invites the next reader to re-open a closed question. Precision for this run
is 0.88 — comfortably above the ~0.5 floor at which §8 says to tighten scope rather than add agents,
and high enough that the lens priming for this surface should be reused rather than retuned.

## What this review did NOT cover

Stated because a green row that is not a verified row is the defect class this build exists to close.

- **The merge bar.** A full `GATE_SELFTESTS=1` run was executing in parallel with this review and is
  not incorporated. No finding above depends on it, and none of the three blockers is reachable by it:
  gov has no `.governance/install.json`, so B1, B2 and B3 are all observable only against a scratch
  fixture target. A green bar on this tree is not evidence against them.
- **The out-of-suite arms.** `tools/govkit/selftest.py` and `tools/govkit/matrix.py` grew many arms
  that no pass in this build was permitted to execute — `gate-guard.js` denies suites until VERIFYING.
  This review read them as source; it did not run them. Every left-shift suggestion above that names a
  selftest arm is therefore a proposal against an unexercised suite, and the suite's own liveness is
  itself unverified by this pass.
- **The conflict-order reap.** `tools/govkit/govkit.py:8500` is the only code in this build that
  unlinks files in a target's repository. Four lenses looked at it and none returned a finding. With
  4/4 lenses returned and 0 died, that zero is evidence rather than a gap — but it is evidence from
  reading, not from execution, and the reap has no executed arm in this build either.
- **Dossier and record prose beyond the two findings above.** The map's own coverage and freshness
  legs grade that; this pass read only what a finding led it to.
