**Serves:** diff-review DEPL-dCarriedReceipt-4 DEPL-dCarriedReceipt-5 DEPL-dCarriedReceipt-6 DEPL-dCarriedReceipt-13 DEPL-dCarriedReceipt-15

# Closing Tier-2 diff review, round 1 — dCarriedReceipt, the five receipt-and-reach units

**Range:** `da9e4cd28072501cd4fe87a81db36c01b9a80f9e...HEAD` (three-dot, base pinned as an immutable
sha; tip `4ad67726`). **Round:** 1.

**Review shape:** raw 24 · confirmed 19 · refuted 5 · unverified 0 · precision 0.79.

Nineteen confirmed entries deduplicate to **14 distinct defects**: five entries are pairs or triples
of the same defect found by different lenses (`12`+`2`, `4`+`13`, `17`+`23`, `3`+`19`+`21`). Each
entry below carries every id that arrived for it, so nothing is lost in the merge. Severity is the
HIGHER of a merged pair.

## Verdict: BLOCKED

**DO NOT LAND AS-IS.** One blocker, one high, eight mediums, four lows. The verdict is the shape
`memory/HYGIENE.md` check 22 reads; "DO NOT LAND AS-IS" is the same statement in the harness's own
words and is kept beside it rather than replaced, because the harness wrote it and this record is
its output.

## The blocker, in one paragraph

`plan --coverage` — a verb that needs no receipt, no `--write`, and prints `NOTHING was written.` on
the same run — executes an argv read out of the target repository's own `.governance/deploy.toml`.
That is arbitrary command execution on the machine of whoever previews a repo, triggered by anyone
who can land a commit or a PR in that repo. The security note that cleared it in the `-5` spec rests
on a claim that is false in both halves. This is the one finding that must be closed before the
merge, not after it.

## Method, and what it does not cover

Adversarial fan over the cumulative diff at the pinned base: primed finder lenses → default-refute
skeptics → synthesis. Twenty-four raw findings, five refuted, nineteen survived, none left
unverified. Precision 0.79 is comfortably above the 0.5 floor `§8` sets, so the scope and priming
were right for this surface and no re-tightening is indicated.

**Not covered:** the diff is roughly 11,000 inserted lines across 61 files; the fan was scoped to the
five units named in the binding line plus their immediate callers. The ten earlier units of this
build were reviewed in their own rounds and were read here only where this diff touches them. The
`selftest.py` additions were read as evidence about the units, not audited as a subject in their own
right — except where a fixture's vacuity is itself the finding (D10).

## Findings, severity-ranked

---

### D1 — BLOCKER — a read-only verb executes a command the TARGET wrote

`tools/govkit/govkit.py:1886` (`decline_findings`), reached from `tools/govkit/govkit.py:1959`
(`cmd_plan`) and `tools/govkit/govkit.py:2096` (`cmd_check`). *(raw id 1, filed `[high]`; escalated
to BLOCKER here — the escalation is this review's, not the pipeline's. Grounds: it moves the trust
boundary this tool's stated security model is built on, and the assessment that cleared it was
factually wrong, so nobody has actually weighed it.)*

`decline_findings` reads `row["discharge"]["command"]` out of `deploy`, which `load_deploy`
(`:563`) reads from the **target's** `.governance/deploy.toml`, and runs it:

```python
rc = subprocess.run(resolve_shell_argv(resolved), cwd=str(target),
                    capture_output=True, text=True).returncode
```

Reachability is the whole finding. `cmd_plan` gates this on `--coverage`/`--emit-declines` only — no
receipt, no `--write` — and the same run prints `NOTHING was written.` at `:1943`. The run never
echoes the argv it just executed; it prints only the state, kit, dest and reason. `cmd_check` reaches
it too, at `:2096`.

The `-5` spec's security bullet (section 5, `discharge`) clears this by asserting that
`[[hole]].discharge` "already does exactly this ... against the same file". **False in both halves.**
`[[hole]]` is iterated from the **gov** kit descriptor at `:2269` (`d.get("hole", [])`, where `d`
comes from `read_descriptors(root, ...)`), and the only pre-existing target-authored execution is
`read_gate_verdicts` at `:2585`, which runs solely inside `apply` (`:3281`, `:3842`) — and which
prints its argv before spawning, at `:3271-3275`. So the equivalence that cleared this does not
exist, and this is the first target-authored command any non-writing verb has ever run.

Secondary: a non-list `discharge.command` is iterated character-by-character at `:1878`, where
`validate_gate_runner` refuses the same shape outright at `:2527`.

**Fix.** Do not run a target-authored command under a read-only verb by default. Either gate the
`discharge` branch behind an explicit `--run-discharge`, reporting the row as
`undischarged (probe not run)` — a state, not a silent skip — or restrict execution to `check` alone
and print the fully resolved argv before spawning it, the way `apply` already does. Refuse a
non-list `discharge.command` at the `validate_*` boundary. And correct the `-5` spec's security
bullet: `hole` is gov-authored, `decline` is target-authored.

**Left-shift gate.** Two, and the second is the one that catches the next instance:
1. A selftest arm that builds a target whose `[[decline]].discharge.command` writes a sentinel file,
   runs `plan --coverage`, and asserts the sentinel does **not** exist. Same arm shape for `check`,
   asserting whatever the ruling turns out to be.
2. A source-level arm over `govkit.py` that enumerates every `subprocess.run` / `resolve_shell_argv`
   call site and requires each to sit inside a **declared** set of executing verbs — the "declared
   population, never a directory listing" rule from `§7`. A new spawn reds until a declaration
   claims it, which is exactly what did not happen here.

---

### D2 — HIGH — `adopt --re-adopt --write` bricks the next `apply` on that target

`tools/govkit/govkit.py:5742` (the envelope write), guard at `tools/govkit/govkit.py:5530`.
*(raw ids 12 `[high]` and 2 `[medium]` — one defect.)*

The write emits exactly six keys — `schema`, `gov_source`, `gov_commit`, `prefix`, `kits`, `files` —
and the S10 comment immediately above (`:5740`) states outright that `orders`, `baseline`, `after`,
`hook_block` and `gate_runner` are deliberately not written, justified by "this verb installs
nothing". That justification never considered `--re-adopt` over a receipt **`apply`** wrote.

The `:5530` guard tests only `receipt_path.is_file()` and the flag. Nothing distinguishes an
apply-written receipt from an adopt-written one, and the refusal text actively steers the operator
into the destructive path: *"Re-run with `--re-adopt` to re-measure from scratch."*

After that run, `_cmd_apply` computes `owned = {e["name"] for e in ((receipt or {}).get("gate_runner")
or {}).get("emitted", [])}` at `:3686` — now the empty set — while `by_name` still comes from the
target's on-disk runner file, which still holds every leg `apply` emitted. The first name collision
hits `raise Refusal("the target's runner already has a leg named ... and this target's receipt does
not claim it")` at `:3744`, and the whole install aborts. Permanently, until someone hand-edits the
runner. `--resume` does not help: `step()` is a printer (`:65`) and the LEGS block is unconditional.

`cmd_check`'s outbox arm at `:2231` also goes quiet — `receipt.get("orders")` is empty, `n_orders` is
0, no note prints, and every recorded order silently stops being verified. `adopt`'s success line
warns about none of it, and `WIRE-INTO-PROJECT.md:605-607` enumerates only row-level losses ("not the
commit, not the rung, not the role").

Recoverable, since the receipt is git-tracked — but only by an operator who works out what happened.

**Fix.** On the `--re-adopt` path, load the existing receipt and carry `gate_runner`, `orders`,
`baseline`, `after` and `hook_block` forward **verbatim** into the new envelope: they record what an
install DID, and re-measuring provenance does not invalidate that. Or refuse `--re-adopt` over a
receipt carrying a `gate_runner.emitted` list, naming the field and pointing at `update`. Silently
re-measuring over an install record is the destruction the verb's own docstring says it avoids.

**Left-shift gate.** A selftest arm that runs `apply --write` → `adopt --re-adopt --write` →
`apply --write` and asserts the third command exits 0 rather than refusing. Plus a receipt-envelope
invariant: the top-level key set is a declared population, and any writer that emits a strict subset
of the keys an existing receipt already carries reds by that fact.

---

### D3 — MEDIUM — the carried-prefix arm has no liveness assertion on its own population

`tools/check-install-prefix.sh:172` (the pipeline), `:181` (`--write-ratchet`), `:197`/`:222`
(`--check`). *(raw ids 3, 21 `[medium]` and 19 `[low]` — one defect.)*

`carried_rows()` ends in `| LC_ALL=C sort`, and the script sets only `set -u`, no `pipefail`. A dead
`carried_population` — a `resolve_python` miss, a `govkit` import error, a `resolve_entry` raise, a
python traceback out of the heredoc — therefore yields **zero rows at exit 0**. Verified by repro:
`producer-returns-1 | ... | sort` into `rows > file && echo MV` prints MV, rc 0, rows 0.

So `--write-ratchet` at `:181` truncates the tracked 105-row `tools/install-prefix-carried.txt` and
prints `wrote 0 carried-prefix row(s)` at exit 0. Once that empty ratchet is committed with the
derivation still broken, `--check` runs both sides empty, the awk reports nothing, and `:222` prints
`carried-prefix clean — 0 recorded file(s), none rising` at exit 0, forever. Green-by-absence, in a
leg that is on the bar (`install-prefix (shipped surface)`, `tools/gate-legs.json`).

Not automatic, and the correction matters: while the ratchet is still non-empty a collapsed
population reds first, emitting SLACK for all 105 rows. But the remedy that red prints at `:218` —
*"re-run `--write-ratchet` in the pass that earned the drop and commit the file"* — walks the
operator straight into the truncation. The false green is reachable by following the gate's own
instructions.

The class is not hypothetical. The `-15` acceptance ledger records it firing during this very build:
the first `--write-ratchet` wrote zero rows and "reported it cheerfully". The CR cause was fixed with
`tr -d '\r'`; no liveness assertion was added. The **first** arm of this same script guards the
identical shape twice, by name, at `:105` ("no kit directories under `tools/` — that is not a pass")
and `:118` ("the shipped surface is empty — that is not a pass"). The instance was fixed; the class
was not.

**Fix.** Capture `rows=$(carried_rows)` once and assert it non-empty in **both** branches, in the
same words the arm above uses: `[ -n "$rows" ] || { echo "install-prefix: the carried-prefix
population is empty — that is not a pass"; exit 1; }`. The SKIP branch at `:175` already covers the
legitimate not-a-kit-source case, so a non-empty assertion here cannot false-red. Also propagate the
producer's real status: `set -o pipefail` around the derivation, or have the python emit a sentinel
line the shell requires.

**Left-shift gate.** An arm in `check-install-prefix.test.sh` that stubs `carried_population` to
produce nothing and asserts BOTH `--write-ratchet` and `--check` exit non-zero. And a gotcha entry so
`gotchas.py --for-diff` surfaces the class on the next shell-gate diff: *a derived population whose
producer sits behind an unchecked pipe reports clean when it dies.*

---

### D4 — MEDIUM — `NR==FNR` inverts when the ratchet file is empty, and the diagnosis prints backwards

`tools/check-install-prefix.sh:199`.  *(raw id 6.)*

`awk` distinguishes the pin file from the measured file only by `NR==FNR` — and that predicate is
true for the **whole of file 2** when file 1 has zero records, because `FNR` resets per file while
`NR` does not. With an empty-but-present `tools/install-prefix-carried.txt`, `pin[]` gets filled from
`$CARRIED.now`, `now[]` stays empty, and the END block prints
`SLACK <path> N -> 0 (delete the row)` for every measured file — telling the operator to delete a
ratchet that in fact records nothing. The correct verdict, `UNRECORDED`, never prints.

Reproduced with the exact awk body from `:198-212` over an empty pin file and a two-row measured
file: `SLACK a 2 -> 0 (delete the row)` for every row, exit 1, roles inverted.

The state is reachable through D3's write path, and the `[ ! -f "$CARRIED" ]` guard at `:188` checks
existence only, never row count, so an empty file sails past it into the inverted awk. Not
defensible as by-design: the awk's own comment says it reports "all four conditions", and in this
state it reports one of them wrongly for all 105 files.

**Fix.** Discriminate by `FILENAME == pinf` — the variable is already passed as `-v pinf` (see D13) —
so an empty pin file cannot swap the roles. Change `:188` to `[ ! -s "$CARRIED" ]`.

**Left-shift gate.** An arm running the gate against an empty-but-present ratchet with a non-empty
measured population, asserting the output names `UNRECORDED` and does **not** name `SLACK`.

---

### D5 — MEDIUM — `adopt --write` is a third receipt writer that never takes the per-target write lock

`tools/govkit/govkit.py:5538` (what it does take) and `:5742` (what it writes).
*(raw ids 13 `[medium]` and 4 `[low]` — one defect.)*

`take_write_lock` is called only from `demand_writable_target` (`:3134`), which is called only from
`cmd_apply` (`:3229`) and `cmd_update` (`:4444`). `cmd_adopt` calls neither, tests for no held lock,
and has no `try/finally: release_write_lock()` — yet it writes both `.governance/install.json` and
`.governance/install.sums` at `:5742-5749`.

The lock's own docstring at `:3086` states the invariant this breaks: it is per-**target** rather than
per-(target, verb) precisely because "`apply` and `update` both write the receipt, so letting the two
interleave is the case this exists for". `adopt` is now a third receipt writer standing outside it.

The window is wide, not theoretical: `derive_attribution` (`:5463`) spawns one
`git log --format=%H <to> -- <src>` per row, and its own docstring cites 143 planned writes on a real
adopter, so the gap between the `:5530` existence check and the `:5742` write is minutes. The loser's
receipt is the file that governs every future destructive `update --write`, and a half-merged or
stale one is exactly what S9's preamble at `:4510` refuses forever.

The coupling explains the miss without excusing it: `demand_adopt_index_clean`'s docstring says `-12`
owns the worktree preconditions "on the verbs that write bytes into the target", a deliberate opt-out
— but the lock is bundled inside `demand_writable_target`, so opting out of the preconditions
silently opted out of the lock too. Read-only `adopt` correctly needs nothing; the gap is on
`--write` alone.

**Fix.** Split `cmd_adopt` the way `cmd_update` is split, call `take_write_lock(target, "adopt")` on
the `--write` path only (matching the read-only-runs-pay-nothing rule at `:3126`), release it in a
`finally`, and re-check `receipt_path.is_file()` **after** the lock is held so the existence guard
stops being a check-then-mutate.

**Left-shift gate.** A source-level arm: every function that writes `.governance/install.json` must
appear in a declared set of lock-taking verbs. That is the arm that reds when the fourth writer
arrives. Plus a behavioural arm that plants a held lockfile and asserts `adopt --write` refuses.

---

### D6 — MEDIUM — an unmatched `adopt --pin` is silently ignored

`tools/govkit/govkit.py:5640`.  *(raw id 9.)*

`pins` is written only by the arg parser at `:6000` and read only as `pins.get(dest)` at `:5640`,
inside the per-plan-row loop. No key-consumption check exists anywhere in `cmd_adopt`, so a `--pin`
naming a path that matches no plan row does nothing and says nothing. Three reachable spellings hit
it: a typo; a Windows/absolute/backslashed path; and a dest the target does not track, which
`continue`s at `:5605-5608` **before** the pin lookup is even reached.

The consequence is a closed loop. The row it was meant to rescue keeps `evidence: "unattributed"`,
`_cmd_update` keeps skipping it at `:4741`, and the tally remedy at `:4796` prints
*"`govkit adopt --pin <path>=<rev>` supplies one"* — the command the operator just ran to no effect.

The asymmetry is the tell: the same flag already refuses loudly on its other two error classes
(`--pin {dest}={pin} does not resolve in this gov checkout` at `:5643`, `gov holds no blob for
'{src}'` at `:5647`), and the parser refuses a missing `=` with the comment "accepting it would
silently pin nothing" (`:5996-5998`). That is the exact rationale this gap violates, on the one flag
that exists to un-skip a row. The `-13` spec's S6 and AC7 define what a MATCHED pin does; nothing
ratifies ignoring an unmatched one.

**Fix.** Track consumed keys (`used.add(dest)` beside the `pins.get`) and after the row loop raise a
`Refusal` naming every `--pin` key that matched no row, listing the destinations that were measured
so a typo cannot read as a pin that was applied.

**Left-shift gate.** An arm asserting `adopt --pin nosuch/path=HEAD --write` exits non-zero with the
key named. Generalizable class for the checklist: *an operator assertion consumed by lookup, with no
check that any lookup hit.*

---

### D7 — MEDIUM — `apply`'s no-manifest branch writes silenced legs into the adopter's order

`tools/govkit/govkit.py:3819`.  *(raw id 14.)*

The silenced-leg bar `-6` added is built **inside** the manifest branch only: `_silenced = {...}` at
`:3697-3698`, consumed at `:3726`. The `else:` at `:3819` — taken whenever `[gate_runner].kind` is
`none` or absent, which is the normal state of a target that has not promoted a runner yet — loops
the same `d.get("gate_leg", [])` and appends `f"- {leg.get('name')}: {argv}"` with no filter and
emits no finding at all.

The asymmetry is stark. On a manifest target, a leg naming a path gov does not ship yields an
`r.fail` and exit 1 with the leg withheld. On a no-runner target, the same leg is written into
`.governance/outbox/gate-legs.md` as a written instruction to the adopter to wire a leg whose engine
no kit ships, with no warning anywhere in the run.

Coverage confirms the gap is untested: every `-6` arm builds an `a6_target` whose `deploy.toml`
declares `kind = "manifest"` (`selftest.py:5919`), so `selftest.py:5983-6011` exercises only the
branch that was fixed. `cmd_plan` does print the SILENT line for both kinds (`:1925`), which softens
it for a plan-then-apply operator — but `apply` itself is silent and the written order stands.

This is `§7`'s *gate the CLASS, not the instance* broken one branch over from the unit that closed
the class.

**Fix.** Hoist the `_silenced` computation above the `if gr.get("kind") == "manifest":` split and
reuse it in the order branch: omit the offending legs from `gate-legs.md` (or write them under a
`WITHHELD` heading) and raise the same `r.fail` text.

**Left-shift gate.** Add a `kind = "none"` fixture to the `-6` arms so both branches are graded — and
make it the default fixture shape for that unit, since no-runner is the state a fresh adopter is
actually in.

---

### D8 — MEDIUM — `decline_findings` is keyed by `dest` while the population it filters is keyed by (kit, dest)

`tools/govkit/govkit.py:1893`.  *(raw id 15.)*

`decline_findings` returns `out[dest] = state` (`:1889`), while `coverage_rows` returns rows carrying
both `kit` and `dest` and its own S4 docstring (`:1832`) insists on ROWS, NEVER UNIQUE DESTINATIONS —
"a destination-keyed tally is exactly what hid the one collision measured at NicoCares".

Every consumer then throws the kit away: `cmd_plan:1961` filters with `declined.get(g["dest"])`,
`:1972` drops every gap row at that dest, and `:1849` resolves the `taken_as` comparison source with
`next((g["src"] for g in gaps if g["dest"] == dest), None)` — whichever gap row happens to be first.
The summary compounds it, printing `{len(declined)} declined`, a **dest** count, against a `gaps`
list that fell by **row** count.

Honest scoping: I could not reproduce a cross-kit same-dest collision in today's registry — every
write-kind rule checked resolves under `{kit}/{prefix}`, and `derive_rule_kind`'s `covered` demotion
is per-entry. The collision is structurally possible, not present in the shipped set. What **is**
reachable now is the mis-attributed row: a `[[decline]]` naming kit A for a dest only kit B ships
passes every arm — kit in `descs`, kit in selection, `why` non-empty, dest not in `have`, and
`dest not in planned` cannot fire because `planned = {g['dest'] for g in gaps} | have` is itself
dest-keyed and B's gap row supplies it. So it grades `declined`, hides B's genuine gap, and
mis-attributes it in the per-kit tally. The function validates the kit field twice and then cannot
check the one thing that pairs it with the dest.

**Fix.** Key the returned map on `(kit, dest)`; look it up in both call sites as
`declined.get((g["kit"], g["dest"]))`; resolve `src` from the gap row matching the same pair rather
than the first dest match.

**Left-shift gate.** A two-kit fixture where both kits plan a write to one dest, with one `[[decline]]`
naming only the first — asserting the second kit's gap still prints. Same fixture asserts the
`declined` count and the `gaps` delta agree.

---

### D9 — MEDIUM — `adopt` stamps `sha256` from the INDEX while `check` verifies the WORKTREE

`tools/govkit/govkit.py:5628` (the stamp) against `tools/govkit/govkit.py:2125` (the verify).
*(raw id 16.)*

`cmd_adopt` sets `ours = index_blob(target, idx[dest][1])` at `:5608` — `git cat-file blob`, the
object store, never disk — and stamps `row["sha256"] = sha256(ours)` at `:5628`, which is also what
`install.sums` renders at `:5747`. `cmd_check`'s integrity arm at `:2124-2126` compares that field
against `dp.read_bytes()`, the **worktree**, with no eol normalisation and no fallback.

The two populations are documented to differ. `demand_adopt_index_clean` (`:5484-5508`) deliberately
permits unstaged worktree edits ("An UNSTAGED edit does not block"), and the `-13` acceptance
ledger's AC8 arm asserts that width as a tested property. Any `core.autocrlf=true` clone adds the
same divergence for every non-LF-pinned text file — the same population `-7` cites, where 23 of 24
engine rows misread.

So `govkit adopt --write` followed by `govkit check` reports `'<path>' does not match the receipt`
for rows nothing is wrong with, and a bare `sha256sum -c install.sums` fails on the same rows —
precisely on the trees `adopt` was written for. `apply` does not have this: it writes `data` and
hashes `data`, self-consistent by construction at `:3462-3464`. The asymmetry is `adopt`'s alone, and
the docstring at `:5625-5628` claims the opposite property (*"`sha256sum -c` stays honest on a tree
this verb did not touch"*), as does the ratified round-4 decision H2.

**Fix.** Hash the **worktree** bytes for `sha256` — keeping `oid` as the index identity, which is
what the verdict logic actually reads — so the field keeps answering the question `check` and
`install.sums` ask. Or make the divergence explicit and refuse/warn per row where index blob and
worktree file differ.

**Left-shift gate.** An arm that adopts a target holding one unstaged worktree edit and then runs
`check`, asserting green. A `core.autocrlf=true` variant of the same arm if the harness can set it.

---

### D10 — MEDIUM — the gate's self-test grades none of the 118 lines this diff added to it

`tools/check-install-prefix.test.sh:35` (`mkfix`).  *(raw id 22.)*

`git diff --stat` over this range shows +128 lines in `tools/check-install-prefix.sh` and **zero** in
`tools/check-install-prefix.test.sh` — the self-test was not touched by this diff at all. `mkfix`
builds `tools/memory-tree/` plus a copy of the gate and nothing else: no `tools/govkit/registry.toml`,
no `tools/lib/resolve-python.sh`. So the guard at `:175` is true for **every** fixture and every arm
takes the SKIPPED branch. Reproduced: a fixture-shaped scratch repo prints the four SKIPPED lines and
exits 0, and `bash tools/check-install-prefix.test.sh` passes all nine arms, every one of them a
first-arm arm.

The `install-prefix self-test` leg (`tools/gate-legs.json:777`) therefore reports PASS while the
shrink-only ratchet, the four awk conditions, `carried_population` and the SKIP branch itself are all
unasserted. This is what keeps D3 and D4 invisible. The staged break is recorded in the `-15` ledger
as a manual observation, which is not the same as a leg that reds when someone edits the arm — and
the file's own header promises "Every red arm has a green control over the SAME mechanism" and "The
population guards get their own arms". Neither holds for arm two.

**Fix.** Add an `mkfix_source` that also writes a minimal `tools/govkit/registry.toml`,
`tools/lib/resolve-python.sh` and a descriptor, then add arms mirroring the ledger's AC2/AC3: a ROSE
arm, a SLACK arm, an UNRECORDED arm, a green control, and one arm asserting the SKIPPED text on a
non-source tree.

**Left-shift gate.** The arms above, plus a liveness assertion **on the test file itself**: the suite
counts how many arms reached the non-SKIPPED branch and reds if that count is zero. A self-test whose
every fixture takes one branch is the `fixture-passes-by-finding-nothing` class applied to the grader,
and it needs the same treatment as any other probe that cannot move.

---

### D11 — LOW — `EVIDENCE_STATES` declares an `"apply"` no branch can assign, and the comment above it says otherwise

`tools/govkit/govkit.py:5423`, comment at `:5417`.  *(raw ids 17 and 23 — one defect.)*

Exhaustive grep of `evidence` assignments in the engine returns only `:5655` (`pinned`), `:5666`
(`unattributed`) and `:5670` (`vintage-match`), all inside `cmd_adopt`. The row `_cmd_apply` builds at
`:3463` carries `path/role/kit/version/sha256/gov_oid/source/commit` and never `evidence`; neither
does the unlanded row at `:3425`. So `"apply"` is unassignable, and the comment at `:5417` —
"`apply` stamps `\"apply\"`" — asserts a writer that does not exist, inside the same comment block
that warns the field-absence reading was destructive.

The property the constant was added to provide therefore does not hold: an apply-written row is
distinguished from S11's two synthesized classes by nothing. The `-13` ledger's live 155-row adopt
confirms it empirically — 125 vintage-match, 29 unattributed, 1 absent, no `apply`.

Nothing is destructive today: `_cmd_update`'s skip keys on the literal `"unattributed"` at `:4741`
and absence falls through to the role dispatch correctly. The risk is forward: a later reader
tightening that skip on the strength of the comment reintroduces the field-absence reading the same
comment warns against.

**Fix.** Pick one and make it true. Either stamp `row["evidence"] = "apply"` at `:3463` (and re-stamp
it on `_cmd_update`'s raw-write arm, which currently leaves a written row still claiming
`vintage-match`), or drop `"apply"` from the tuple and correct `:5417` to say apply rows carry no
`evidence` at all.

**Left-shift gate.** `selftest.py:5382` joins the tuple in one direction only
(`_lit13 <= set(EVIDENCE_STATES)`), so a declared-but-unproduced state passes forever. Add the
reverse arm — `set(EVIDENCE_STATES) <= _lit13` — so every declared state must be assignable by some
literal in the engine. That is the `armed-but-unreachable-rule` class, gated.

---

### D12 — LOW — the check arm writes scratch into the tracked working tree, with no trap

`tools/check-install-prefix.sh:197`.  *(raw id 11.)*

`CARRIED="tools/install-prefix-carried.txt"` (`:129`), so `carried_rows > "$CARRIED.now"` writes
scratch **into the subject it is grading**. `grep -n trap` over the file returns nothing, and
`.gitignore` holds only `__pycache__/` and `*.pyc`. Observed live: a `--check` run in this worktree
left `?? tools/install-prefix-carried.txt.now` in `git status`.

Scoping correction: the `rm -f` at `:214` does run on both awk-pass and awk-fail, since `cstat` is
captured first, so the leak is confined to abnormal termination and to two concurrent invocations
clobbering one scratch path — narrower than the raw finding implied. It is still real, and it has a
concrete downstream cost: `tools/run-gates/gate-fingerprint.sh:57,68` folds `git status --porcelain`
and the blob hash of every untracked file into the working-tree fingerprint, and `run-gates.sh:644`
computes `FPRINT_START` for the recorded-green stamp — so a leftover `.now` shifts the fingerprint and
forces an unnecessary full bar at the push boundary. It also breaks the charter's stated
hermetic-leg rule while grading the tree it writes into.

**Fix.** `now=$(mktemp)` with `trap 'rm -f "$now"' EXIT`, and pass `"$now"` to awk. Same for
`$CARRIED.tmp` in the `--write-ratchet` branch, keeping the final `mv` into place.

**Left-shift gate.** One arm per bar leg is overkill; one arm over the whole class is not. Add a
run-gates canary that snapshots `git status --porcelain` before and after each self-test leg and reds
on a difference. That catches every future leg that dirties the tree, not just this one.

---

### D13 — LOW — `awk -v pinf="$CARRIED"` passes a variable the program never reads

`tools/check-install-prefix.sh:198`.  *(raw id 20.)*

`pinf` appears nowhere in the awk body between `:199` and `:212` — not in the `NR==FNR` block, not in
the `now[]` block, not in any of the three `printf` strings in END. All four condition messages
hardcode their text and none names the ratchet file, so a reader who assumes the messages name their
source is wrong, and the next edit that wants the filename adds a second way to spell it.

**Fix.** D4 wants `FILENAME == pinf` in place of `NR==FNR`, which uses the variable and fixes the
inversion in the same edit. Take that. If D4 is deferred, delete the flag.

**Left-shift gate.** None warranted. A gate for unused `awk -v` variables costs more than the class
is worth, and D4's arm covers the line either way.

---

### D14 — LOW — the remedy `update` prints names an invocation `adopt` always refuses

`tools/govkit/govkit.py:4795`, same omission at `tools/govkit/govkit.py:4726`.  *(raw id 24.)*

`evidence: "unattributed"` is written only by `cmd_adopt` (`:5666`), so any target holding such a row
has `.governance/install.json` on disk by construction. `cmd_adopt` then refuses at `:5530-5537`
(`receipt_path.is_file() and not re_adopt`) before `--pin` is ever consulted. The remedy `update`
prints — "`govkit adopt --pin <path>=<rev>` supplies one" — therefore always refuses as written; the
working invocation needs `--re-adopt` and `--write`.

Bounded rather than absent: the refusal text itself names `--re-adopt`, so an operator recovers on
the second try instead of being stranded. Which is why this is low, not why it is a non-finding. The
line still names a command that cannot work, in the one sentence the comment at `:4792-4794` says
exists to stop an operator concluding the tool is broken. And it composes badly with D6: an operator
who fixes the invocation and then mistypes the path gets silence.

**Fix.** `govkit adopt --re-adopt --pin <path>=<rev> --write` at `:4795`, and fix the same phrasing in
the S7 docstring at `:4726`.

**Left-shift gate.** An arm that extracts the printed remedy invocation and executes it against the
adopt fixture, asserting exit 0. A remedy that is run is a remedy that cannot rot; a remedy that is
only spelled is prose beside a source that owns it.

---

## The hunt list, answered

The brief named six areas to hunt hardest. Four came back clean, and clean here means read
first-hand rather than absent from the finding set.

**(a) `gov_oid` holding target bytes — HELD.** Both writing arms take gov's blob. The pinned arm at
`:5647-5648` sets `row["gov_oid"] = blob_oid(was)` where `was = blob_at(root, pinned, p["src"])` —
gov's object store at the pinned commit. The walk arm at `:5668` unpacks
`row["commit"], row["gov_oid"], rung = hit` from `derive_attribution`, which reads gov. The
unattributed arm writes neither field, deliberately (`:5661-5666`). `ours` is used only for `sha256`,
`oid`, and as the right-hand side of the rung comparison. No path stamps target bytes into `gov_oid`.
The inversion the whole unit is written against does not exist in the code. **D9 is the mirror-image
defect on a different field, and it is worth reading in that light: the `gov_oid`/target-bytes
discipline was applied so carefully that `sha256`'s own population question went unasked.**

**(b) the raw-write arm on differing identities or a `forked` row — HELD, twice over.**
`classify_row:4258` sets `o_state = "equal"` only on `gov_oid and ours_oid == gov_oid`, so a row with
no `gov_oid` — every unattributed row, every unlanded row — reads `differs` and cannot reach the raw
arm even if the D-nothing skip were removed. And `ROLE_DISPOSITION["forked"] = "report"` at `:3966`
closes the arm to forked rows by dispatch, before any verdict is computed. Two independent guards,
neither depending on the other. That is the shape `§7` asks for and it is present here.

**(c) the `cmd_update` skip's scoping — HELD.** `:4741` reads
`if how == "table" and row.get("evidence") == "unattributed"`. Keyed on the string, never on
field-absence, so the unlanded channel and the synthesized `attributes` row are not swallowed; scoped
to `table`, the only disposition that can put bytes on disk, so `seed` still reaches its reseed
override and `attributes` still reaches `-2`'s pins arm. Both halves are as the comment claims and
AC14 grades both. No finding.

**(d) `adopt` producing a receipt a later `update --write` acts on destructively — HELD for the
receipt's ROWS, BROKEN for its ENVELOPE.** No row-level path was found: an unattributed row is
skipped, a pinned or vintage-matched row carries gov's identity, and a forked row is dispatched to
`report`. The destruction that *is* reachable is D2's, and it runs the other way — `adopt` destroying
what `apply` recorded, rather than misleading a later `update`.

**(e) predicates that cannot fail, fixtures that pass by finding nothing — FOUND, three of them.**
D10 (every self-test fixture takes the SKIPPED branch), D3 (a probe that cannot move reports clean),
D11 (a one-directional membership join that a declared-but-unproduced state passes forever). This was
the richest lens of the six, which is consistent with `§8`'s prediction about fresh surface.

**(f) shell quoting, subshell exit-code loss, CR/LF in `check-install-prefix.sh` — FOUND, four.**
D3 (pipeline exit status is `sort`'s), D4 (`NR==FNR` inversion), D12 (scratch in the tracked tree),
D13 (dead `-v`). The CR handling itself is correct — `tr -d '\r'` at `:167` is present and the
comment explaining it is accurate — but it was applied as an instance fix, and the class it belongs
to is D3.

## Recommended landing order

1. **D1** before anything else, and before the merge. It is the only finding whose cost falls on a
   third party's machine.
2. **D2**, **D5**, **D9** — the three that damage a target's receipt or lock out a writing verb.
3. **D10** before **D3** and **D4**, because D10 is why nobody would see D3 and D4 red. Fixing the
   arm first means the D3/D4 fixes land with a grader that can actually fail.
4. **D7**, **D8**, **D6** — behavioural gaps with no data loss attached.
5. **D11**, **D12**, **D13**, **D14** at leisure; D13 rides along with D4.

## Left-shift summary

Every confirmed finding above carries a gate suggestion, per `§7`. Three of them are class-level
rather than instance-level and are the ones worth building even if the rest are done by hand:

- **A declared population of executing call sites** in `govkit.py` (D1). A new `subprocess.run` reds
  until a declaration claims the verb it sits in. This is the gate that would have caught D1 at
  authoring time.
- **A liveness assertion on every derived population in a shell gate** (D3), plus the gotcha entry so
  `gotchas.py --for-diff` raises the class on the next shell-gate diff.
- **A liveness assertion on the self-test itself** (D10): a suite whose every fixture takes one
  branch reds by that fact. `§7` already demands that a gate's failing case be observed; this extends
  it to demanding that the observation be a leg rather than a memory.
