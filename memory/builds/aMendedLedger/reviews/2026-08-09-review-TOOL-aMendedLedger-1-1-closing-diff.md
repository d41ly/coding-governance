# Closing review — aMendedLedger, `663ca42..bde0de8`

**Serves:** diff-review TOOL-aMendedLedger-1 TOOL-aMendedLedger-2 TOOL-aMendedLedger-3 TOOL-aMendedLedger-4 TOOL-aMendedLedger-5 TOOL-aMendedLedger-6 TOOL-aMendedLedger-7 TOOL-aMendedLedger-8  <!-- inferred: closing review over a commit range, not a spec -->

- **subject** — seven build commits (`dc5ae99` U1 … `bde0de8` U7) plus two spec commits, 59 files,
  +7418/-182: the journals relocate into their builds, the per-node session ledger retires to
  `memory/archive/ledger/`, the hygiene kit moves to 1.8, a **row-keyed three-way merge driver** is
  wired onto `memory/DECISIONS.md` and `memory/backlog/*.md`, and the docs stop selling a ledger the
  tree no longer has.
- **review shape** — raw 18 · confirmed 14 · refuted 4 · unverified 0 · **precision 0.78**.
- **counts** — 7 blocking · 5 non-blocking.

---

## 1. Verdict

# DO NOT SHIP

**What decided it:** U5 — the merge driver — silently corrupts `memory/DECISIONS.md` at exit `0`, on
the real file, through the wiring this diff commits, on three independent paths I reproduced in this
session. The decisive one is the control: on inputs where git's own three-way merge **conflicts
loudly** (`git merge-file` → rc 1, one hunk, structure intact), the new driver prints
`… 1 new from theirs, 0 dropped, clean`, exits 0, writes zero conflict markers, and leaves the
repo's append-only record of record carrying a **duplicated `## DEPL — deployer` heading and a
duplicated `*(none yet)*` placeholder**. `check-memory-hygiene.sh` and `corpus_ids.py` both return 0
on the corrupted file. The full bar returns **`gates GREEN — 38/38 legs passed`**.

This is not a latent risk. `## KICK` and `## DEPL` are *both* `*(none yet)*` with zero rows today, so
the trigger is two of three nodes landing a first decision in the same family — the next multi-node
session. The file is append-only by charter, so the corruption is not supposed to be editable back
out.

A build that ships a mechanism whose own docstring claims "a row appears at most once by
construction", onto the file that *is* this repo's memory, while its gate leg's oracle shares the
exact blind spot that hides the failure, is the failure class this repo exists to prevent. Six of
seven units are sound and I would land them unchanged; U5 is not shippable in this shape.

**Cheapest honest path to green:** fix B1, B3 and B5 in `merge-rows.py` (all three are contained
edits with a test arm each), fix B2 (a doc string), and add B4's third direction. B6/B7 are the
gates that would have caught the rest.

---

## 2. Blocking findings

### B1 — the driver duplicates a section heading and its placeholder on a two-node first-row append, at exit 0

`tools/memory-tree/merge-rows.py:172` (lead attach) · `:284` (re-emit)

**Failing scenario.** `rows()` attaches every unkeyed line since the previous anchor to the
*following* anchor as its lead-in (`out[k] = lead + [ln]`), so a `## FAMILY` heading rides as part of
the first row of its section. When both sides add the **first** row of the same currently-empty
section, the two rows are id-disjoint: ours is emitted with its lead in the `a_order` loop, theirs is
emitted **again with its own copy of the same lead** at `out.extend(B[k])`.

Reproduced this session against the real `memory/DECISIONS.md`, both sides opening `## DEPL`:

```
merge-rows: 36 row(s) from ours, 1 new from theirs, 0 dropped (delete honoured), clean
rc=0 · conflict markers: 0
'## DEPL' count: 2 (base 1)   ·   'none yet' count: 3 (base 2)
```

Control, identical three inputs, `git merge-file -p`: **rc=1, 1 conflict hunk, heading count 1.**
The driver converts a loud conflict into a silently wrong append-only file. Gates on the corrupted
result: `check-memory-hygiene.sh` rc 0, `corpus_ids.py` rc 0. Independently reproduced by a second
pass end-to-end through `git merge --no-edit` with the real `.gitattributes` + config
(`Merge made by the 'ort' strategy`, rc 0).

`merge-rows.test.sh` cannot see it: its only rc-0 oracle is **ID-SET equality** (`:39`) and no id is
lost or duplicated here. Case 5 (`:209-218`) covers a heading whose position must be *preserved*,
never one that gets *copied* — it adds the extra row on one side only.

**Exact fix.** De-duplicate lead-ins at emit time: in the `b_order` loop at `:284`, strip from `B[k]`
any leading lines already present as the trailing lead-in of `out` before extending; or treat a
`%B`-only row whose non-empty lead collides with an already-emitted lead as a **CONFLICT** rather
than an append. Then add a fixture where **both** sides append a row after the same unkeyed heading
and assert `grep -c '^## '` on the result equals the union of the three inputs' distinct headings.
The current id-set oracle is structurally incapable of seeing this class.

### B2 — the only published `merge.rows.driver` command names paths that exist in no layout; wiring it as written silently drops the incoming rows

`tools/memory-tree/README.md:27`

**Failing scenario.** The kit README publishes
`git config merge.rows.driver 'bash tools/lib/pyrun.sh memory-tree/merge-rows.py %O %A %B %P'`.
That mixes the two install prefixes: in this repo the driver is `tools/memory-tree/merge-rows.py`
(there is no `memory-tree/` at the root); in a copy-installed adopter the shim is `lib/pyrun.sh`
(there is no `tools/`). The command cannot start in **either** layout — verified by reading `:27`
verbatim this session. When a merge driver fails to start, git prints `CONFLICT (content)` but the
driver never writes `%A`, so the path is left holding **ours-only content with zero conflict
markers** and status `UU`. An author who sees "conflict", opens a marker-free file, and `git add`s
it has silently dropped the incoming rows. Reproduced by the verify stage:

```
python.exe: can't open file '...\gov\memory-tree\merge-rows.py': [Errno 2] No such file or directory
CONFLICT (content): Merge conflict in memory/DECISIONS.md          rc=1
→ file holds ours' row only · grep -c '<<<<<<<' = 0 · git status = UU
```

Re-running the same merge with the string `check-wiring.sh` builds succeeds, both rows present. This
is the exact shape `merge-rows.py`'s own docstring (`:32-34`, `:321-326`) calls "silent,
unrecoverable loss". Nothing gates the published string: `merge-rows.test.sh:356` hand-types the
correct one inside its own fixture and `check-wiring.sh:281` *builds* a third; the repo publishes
three answers to one question and gates only the one it invented.

**Exact fix.** Delete the literal from `README.md:27` and point at `bash tools/check-wiring.sh --fix`,
which resolves both prefixes with `first_of` and sets one string. If a literal must stay, spell
**both** layouts explicitly. Add an arm to `merge-rows.test.sh` that extracts the command from
`README.md` and runs it, so the published string is the tested one.

### B3 — the driver keys only 35 of 73 rows in the file it is wired to, and duplicates one of the other 38 at exit 0

`tools/memory-tree/merge-rows.py:49-52` (the claim) · grammar `tools/memory-recall/extract.py:73` ·
oracle `tools/memory-tree/merge-rows.test.sh:39`

**Failing scenario.** The driver keys rows through `extract.py`'s `ERAS`, whose session-scoped
alternative is `[{_NODE}][A-Za-z]{2,}-\d+` inside `\b…\b`. The trailing letter of this repo's
ratified correction-id form kills the word boundary, so `anchor_at('- TOOL-aMendedLedger-1b · …')`
returns `None`. Census run this session over the real file:

```
memory/DECISIONS.md: 91 lines · 73 '- ' rows · 35 anchored · 38 UNKEYED
unkeyed tail: TOOL-aMendedLedger-1b, TOOL-aMendedLedger-1c   ← added by THIS diff (:81-82)
```

Those 38 never enter the keyed path; `rows()` files them as lead-in or trailer, both of which go to
`git merge-file` — precisely the line merge the unit exists to replace. Two consequences, both
measured on the real corpus:

- **INERT.** Two nodes appending different `-9b` rows **CONFLICT** (rc 1) where the identical appends
  with numeric `-9` auto-resolve **clean** (rc 0). The append-collision the unit exists for is
  unresolved for over half the index.
- **DUPLICATES.** The same `TOOL-aMendedLedger-<n>b` row minted on both nodes and filed in different
  regions is emitted **twice** (lines 88 and 93) at rc 0, with the audit line reading
  `35 row(s) from ours, 0 new from theirs, 0 dropped (delete honoured), clean`. That directly
  falsifies the module's own §`WHY THIS CANNOT DUPLICATE` (`:49-52`) and the grammar-drift
  paragraph's promise that "A row is still never invented or duplicated" (`:26-28`).

The gate leg is green and cannot become red: the test's "independent" oracle at `:39` is
`\b[A-Z]+-[A-Za-z0-9]+-[0-9]+\b`, which fails the **same** boundary, so suffixed ids drop out of both
sides of every id-set comparison; no fixture uses one (`grep -nE 'zFixture-[0-9]+[a-z]'` → nothing);
and case 7's real-file identity arm passes trivially because `text_merge` short-circuits on `a == b`.

**Exact fix.** Widen the session ERA at `tools/memory-recall/extract.py:73` to
`[{_NODE}][A-Za-z]{2,}-\d+[a-z]*` — one shared grammar, still un-vendored. That also restores those
38 decision rows to memory-recall and to `corpus_ids`' checks 13-16, which share the regex.
Independently widen the test oracle at `merge-rows.test.sh:39` to
`\b[A-Z]+-[A-Za-z0-9]+-[0-9]+[a-z]*\b`, and add the missing non-vacuity sentinel in this repo's own
`pop_guard` idiom: for every governed index, assert that every `^\s*[-*] ` line keys under the
**driver's** grammar, redding with the offending lines. That arm fires at 38 today. If widening the
shared grammar is out of scope, the honest minimum is to narrow the docstring claim at `:49-52` to
the keyable population and record the correction-row shape as a known gap.

### B4 — the drift-audit arm named "the declaration was not a muzzle" cannot fail on that property

`tools/drift-audit/selftest.py:393-395` (the strip) · `:400` (the arm) ·
`tools/drift-audit/drift_signals.py:57-65` (the new declaration)

**Failing scenario.** This build puts a **gateable** signal into `DECLARED_EMPTY` for the first time
and retires its pin. The only thing keeping that declaration from being a silence-forever switch is
`test_declared_empty`. But direction two **removes the declaration**
(`sig.write_text(… .replace(", 'ledger_rows_contradicting_git'", ""))`) *before* it puts the row back
— so it proves the SIGNAL can move, never that the DECLARATION does not suppress it. `drift_signals.py:62-63`
states the property as fact: "the declaration is not a muzzle … selftest.py asserts both directions".
It does not.

Sabotage run this session — one token added to the over-pin filter at `drift_report.py:517`
(`and s["signal"] not in declared`), turning `DECLARED_EMPTY` into an unconditional muzzle:

```
python tools/drift-audit/selftest.py      → rc 0, "drift-audit selftest: all checks passed"
                                            incl. "ok  a row returns: the declaration was not a muzzle"
python tools/memory-tree/check-arms.py    → rc 0
python tools/drift-audit/drift_report.py --check → rc 0
python tools/codebase-map/test_codebase_map.py   → rc 0
```

No leg on the bar catches it. The shipped code **is** correct today (the verify stage confirmed
`--check` rc 1 with the declaration kept and a row restored), so this is a coverage hole on a new
gateable declaration, not a live break — but it is the one arm in this diff that I could not make
fail, and it guards a switch that can silence a gate forever.

**Exact fix.** Add a **third** direction to `test_declared_empty` that KEEPS the declaration in
place, restores the contradicting row, and asserts `--check` still reds (rc 1) and still names the
signal on stderr. That is the assertion the arm's own label claims, and the only one that fails on
the muzzle sabotage. Direction two then stays as the lift-the-declaration control.

### B5 — a `%B`-only row is appended past the row block, filing an incoming decision under the wrong `## FAMILY` heading — a regression against the behaviour it replaced

`tools/memory-tree/merge-rows.py:284`

**Failing scenario.** `for k in b_order: … out.extend(B[k])` appends every theirs-only row after ALL
of ours' rows. Position survives only when the incoming row is the **first** of its section (it
carries its own heading). `memory/DECISIONS.md` is explicitly `Grouped by family for reading` (`:4`)
with `## PLAY` / `## KICK` / `## TOOL` / `## DEPL` inside the row block. Reproduced this session on
the real file — ours inserts a TOOL row inside `## TOOL`, theirs inserts a PLAY row inside `## PLAY`:

```
merge-rows: 36 row(s) from ours, 1 new from theirs, 0 dropped (delete honoured), clean   rc=0
 13:## TOOL — tooling
 88:- TOOL-aNewOurs-<n> …
 90:- PLAY-bNewTheirs-<n> · theirs appended inside the PLAY section   ← filed under ## TOOL
 91:## DEPL — deployer
```

**The control is what makes this a defect rather than a design quibble.** A parallel finding arguing
that the append rule is merely the ratified U5 decision table was refuted on exactly that ground; it
does not survive the control. The identical two inserts through git's built-in three-way merge —
i.e. the pre-change behaviour — resolve rc 0 clean with the PLAY row at line 10, **correctly under
`## PLAY`**. U5 *introduced* the misfiling. Nothing reds: no hygiene check, `corpus_ids` check or map
inventory parses section membership.

**Exact fix.** Splice rather than append: walk `b_order` and emit each B-only row immediately after
the last key preceding it in `b_order` that was already emitted from `a_order`, falling back to
end-of-block when there is none. Add the mirror of case 5 (`:213-218`) — a B-only row in a
**non-final** section, asserting it stays above the next `^## ` heading. If the append rule is to be
kept deliberately, the U5 decision table must be amended to say so *and* to record that it regresses
placement against the merge it replaces.

### B6 — `check-wiring`'s merge arm reports "ok … wired" for a driver that cannot start

`tools/check-wiring.sh:254-296`

**Failing scenario.** `check_merge_rows` validates three things by **path and string only**:
`merge-rows.py` exists (`:259`), `pyrun.sh` exists (`:264`), and `merge.rows.driver` equals the built
command (`:290`). It never executes the command, and never checks the two runtime dependencies the
driver actually needs — `tools/lib/resolve-python.sh` (sourced by `pyrun.sh:29`) and the sibling
memory-recall kit (`_kit_dir`, `merge-rows.py:95-108`). Both missing states are silent or destructive
at merge time while the arm prints `ok`:

- **State A** (`resolve-python.sh` moved aside): `ok  merge  — merge.rows.driver wired`, then the
  merge prints `resolve_python: command not found` + `CONFLICT`, and the file holds ours' row only
  with `grep -c '<<<<<<<'` = 0 and status `UU`. Silent take-ours; the incoming row is gone. The
  arm's own UNWIRED remedy at `:266` already names `resolve-python.sh` as a dependency — nothing
  asserts it.
- **State B** (`tools/memory-recall` moved aside): the `recall` arm one line above prints
  `skip  recall  — memory-recall kit not adopted` while the merge arm prints `ok`. Every
  governed-index merge then conflicts wholesale, forever. Loud and non-destructive, but the arm's
  header claims it "is what turns 'declared' into 'wired' on each node"; it does not.

**Exact fix.** Make the arm execute what it validates: run `bash "$shim" "$drv"` with no arguments
and require rc 2 plus the `%O %A %B %P` usage text — `merge-rows.py:313-319` already guarantees
exactly that contract and `merge-rows.test.sh:107-111` already asserts it. One call covers a missing
resolver, a missing interpreter, a syntax error in the driver, and a wrong path. Add a separate check
that `_kit_dir`'s memory-recall directory resolves, since a driver that starts but cannot key rows is
still permanently broken.

### B7 — the two `.gitattributes merge=rows` lines are ungated; deleting them leaves the whole bar green

`.gitattributes:33-34`

**Failing scenario.** `merge=rows` is what actually routes a conflict through the driver; without it
git uses the built-in line merge, which `merge-rows.py:11-15` records as having duplicated an id in
**147 of 151** historical `DECISIONS.md` conflicts. Nothing on the bar asserts those lines exist.
`merge-rows.test.sh` case 9 (`:345-376`) writes its **own** `.gitattributes` inside a scratch repo, so
it proves the driver works against an attribute it invented, not against the repo's.
`check-wiring.sh:275-278` degrades to `skip … no tracked path declares merge=rows` and exits 0 — and
`check-wiring.sh --check` is not a gate leg at all (the bar runs only `check-wiring.test.sh`;
`WIRE-INTO-PROJECT.md:362` in fact forbids making it one). Verified in a clone: dropping the lines
leaves 38 of 39 legs green, the single red being a clone artifact that fires identically with the
lines restored. A future `.gitattributes` reshuffle silently un-wires the driver on every node.

**Exact fix.** Add one assertion to `merge-rows.test.sh` (or a small leg) that runs
`git check-attr merge -- memory/DECISIONS.md memory/backlog/*.md` against the **real** tree and
requires `merge: rows` on every match — the same "what git judges, not what a grep of
`.gitattributes` says" rule the end-to-end arm already applies to its own fixture at `:367-368`.

---

## 3. Non-blocking findings

- **N1 · `tools/memory-tree/check-memory-hygiene.sh:234` — pop_guard 3's precondition is a bare
  extension test, so one unrelated `.txt` reds a clean adopter tree with a false diagnosis.**
  `PRE_REGISTRY=$(… grep -cE '\.txt$')` asks "does any `.txt` exist under `memory/`", not "does a
  registry exist"; the four sibling preconditions (`:130-133`) are kind-specific paths. Reproduced
  A/B on an adopter fixture with no `memory/project/` (legal — check 3's root arm lists `project/`
  as permitted, not required): rc 0 clean → add `memory/archive/old-notes.txt` → rc 1
  `check 3: no registry under memory/project/ … the selector is mis-segmented`, naming a cause that
  is not the cause, for a file in the directory `HYGIENE.md:65` declares wholly exempt. The comment
  at `:230-233` defends the un-segmented precondition ("the population is 5 on a real tree") — true
  here, false for an adopter with no registries at all, which is exactly who the §3a migration this
  build ships tells to upgrade to kit 1.8. **Escalate to blocking the moment any adopter runs that
  migration.** Fix: narrow to the five registry NAMES the case arm at `:238-239` enumerates,
  un-segmented; add the A/B as the guard's false-positive half.
- **N2 · `merge-rows.py:298-300` — the audit line's reconciliation claim is false on every conflict.**
  The comment states unconditionally that `kept + took_b` is the anchored-row count of the file just
  written and "an operator can `grep -c` the result and reconcile". The both-sides branch
  (`:257-264`) writes BOTH rows but increments `kept` once. Reproduced:
  `1 row(s) from ours, 0 new from theirs … CONFLICT`, rc 1, `grep -c '^- TOOL-'` = 2. `audit()`
  asserts the equality at `:317`, but all three call sites (`:325`/`:331`/`:337`) pass `want_rc=0`,
  so the only regime that can break it is never exercised. Fix: scope the claim to clean verdicts or
  count the marker branches honestly, then add a `want_rc=1` call.
- **N3 · `.gitattributes:31` · `tools/check-wiring.sh:246` · `tools/check-wiring.test.sh:228` — all
  three claim git warns when a declared merge driver is unconfigured; git 2.54 emits zero bytes.**
  Measured on `git version 2.54.0.windows.1`: 0 bytes of stderr in both the conflicting and the
  auto-resolving regime. The substantive landing argument survives (the fallback *is* the pre-change
  behaviour, so attribute and config can land in one commit), but a node that never runs
  `check-wiring` gets no signal at all — and the same fallback silently duplicated a row at rc 0 in
  the same run, which makes `check-wiring.sh:285`'s "a line merge that can duplicate a row" the
  accurate half. Fix: drop "with a warning" from all three and say the fallback is silent, which is
  precisely why the merge arm is the only notification.
- **N4 · `tools/memory-tree/merge-rows.test.sh:20` — `ROOT="$(cd "$HERE/../.." && pwd)"` resolves
  outside the repo at the adopter prefix.** `WIRE-INTO-PROJECT.md:103` copies the whole directory to
  `<root>/memory-tree/`, where `../..` is the *parent* of the repo root; the script `cd`s there
  (`:21`) and sources a `resolve-python.sh` that is not present. Reproduced on an adopter fixture:
  `No such file or directory` → `FAIL no usable python on this host`, exit 2 — a path bug diagnosed
  as a python bug, this repo's own catalogued wrong-answer-that-looks-right class. Every other
  copy-installed memory-tree script uses `git rev-parse --show-toplevel`; `WIRE-INTO-PROJECT.md:489`
  still says "Safe to overwrite `memory-tree/*.sh`", a glob this new file joins. Fix: resolve ROOT
  via git identity and add a one-line exclusion at `WIRE:489` naming this file dogfood-only until the
  driver is packaged.
- **N5 · `spec/2026-08-09-spec-aMendedLedger-1.md:273-275` — master AC2 is unsatisfiable as written
  and contradicts §4 Migration.** AC2 requires `similarity index 100%` over *each* relocated file;
  §4 (`:135`) mandates that `MEMORY.md`'s digest folds INTO the relocated bThriftyBellows journal,
  making 100% impossible for that file by construction (measured: four files 100%, bThriftyBellows
  91%). The U1 sub-spec at `:323` asserts "the master's AC2 carries the corrected form" — `:273-275`
  was only corrected for the `-p` flag (rev-4). Worse than a false red: run literally,
  `git log --follow -p` surfaces the *commit-message* line "(similarity index 100%)" and the AC
  falsely **passes**, unable to distinguish the fold from a byte-identical move. Content loss is nil
  — the relocated file is a strict superset, only the digest line added. Fix: carve out the one file
  the Migration table mandates a fold into, and correct the U1 cross-reference in the same edit.

---

## 4. Precision

**14 / 18 = 0.78** (confirmed 14 · refuted 4 · **unverified 0**).

Every one of the 18 raw findings carries an explicit verdict; none was left unadjudicated. The four
refuted were: an archive-README "gate-frozen" misreading, a pop_guard-3 uniqueness claim knocked down
by checks 4 and 8 behaving identically, a `%B`-append complaint refuted as ratified design (but see
**B5**, which survives it on the control), and a WIRE-runbook omission that is a recorded, deliberate
scope exclusion.

**One sub-claim inside B3 is UNVERIFIED and must not be read as a refutation of anything:** the
exculpatory "845 in-process replays over every historical triple → 0 dropped ids". Nobody re-ran it.
Treat "the driver never *drops* a row" as **unproven**. What *is* established is only that the two
reproductions above duplicate rather than drop.

---

## 5. What the build got RIGHT — do not undo

1. **The journal relocation preserved content exactly.** The relocated
   `memory/builds/bThriftyBellows/build/2026-07-16-build-bThriftyBellows-1.md` is a strict superset
   of its original — `diff` shows `2a3,4` only, the folded digest line plus a blank. Nothing was
   removed. A later session must not "restore" that file to a 100% rename by dropping the digest;
   fix the AC (N5), not the file.
2. **The ledger was retired by DECLARATION, not by deleting the signal.** The three shards moved to
   `memory/archive/ledger/` with a README, and the kit ENGINE is untouched — `drift_report.py` still
   reads `<memory_root>/project/in-flight/*.md` for adopters who keep a ledger. Do not "clean up"
   `ledger_rows_contradicting_git` out of `drift_signals.py`; the whole point is that the probe
   survives its empty population.
3. **`--check` treats a DEAD gateable signal as a FAILURE, not a skip** (`drift_report.py:508-518`).
   The old predicate required `live`, so a blind probe scored like a probe that found nothing — which
   is how a pre-flatten glob stayed green on the bar. This is the generic fix and it catches the next
   blind probe with nobody noticing the next layout change. Do not relax it back to requiring `live`.
   The `DECLARED_EMPTY` exception is **enumerated with its reason inline**, never inferred — keep it
   that way (and arm it: **B4**).
4. **The `pop_guard` idiom** in `check-memory-hygiene.sh:113-121` — a precondition asking "does a file
   of this kind exist anywhere under the memory root" against a population asking "does one exist at
   the exact path this check expects". It catches a check that silently selects an empty population,
   which is the highest-value class in a hygiene engine. N1 is a precision defect in *one*
   precondition; the idiom itself is right and must survive the fix.
5. **The merge-rows test oracle is deliberately grammar-INDEPENDENT** (`merge-rows.test.sh:37-39`),
   with the comment explaining that sharing the driver's regex would make every arm "self-consistent
   and blind: a grammar that stopped recognising a row would remove it from BOTH sides of the
   comparison". That reasoning is exactly correct and is the reason B3 is a *coverage* hole rather
   than an invisible one. The fix is to **widen** the oracle, never to point it at the driver's regex.
6. **The driver fails CLOSED.** A driver error writes a conflict rather than a silent take-ours —
   verified in State B, where a missing memory-recall kit produced
   `merge-rows: FAILED (RuntimeError …) — writing a conflict rather than a silent take-ours` with
   markers. Do not "simplify" that wrapper away.
7. **The anchor grammar is IMPORTED from memory-recall, never vendored** (`merge-rows.py:95-108`).
   One grammar, one place to fix. B3's fix must widen the shared terminal, not fork a second copy.
8. **The map dossier records the driver's adopter gap honestly**
   (`memory/map/features/memory-tree-merge-driver.md` §Gaps: not packaged for adopters, and no
   regenerate driver "and there will not be one"). That candour is what let a refutation land
   correctly instead of becoming a phantom finding.

---

## 6. What was actually verified by execution

A green bar proves nothing here — the bar was green through every reproduction below.

**Gates run (this session, at `bde0de8`, clean worktree):**

| Command | Result |
|---|---|
| `bash tools/run-gates.sh` | **`gates GREEN — 38/38 legs passed (1 skipped)`**, rc 0 |
| `bash tools/memory-tree/check-memory-hygiene.sh` (on the **corrupted** DECISIONS.md) | rc 0 — blind |
| `python tools/memory-tree/corpus_ids.py` (same corrupted file) | rc 0 — blind |
| `python tools/drift-audit/selftest.py` | rc 0, "all checks passed" |
| `python tools/memory-tree/check-arms.py` | rc 0 |
| `python tools/codebase-map/test_codebase_map.py` | rc 0 |
| `git check-attr merge -- memory/DECISIONS.md memory/backlog/{TOOL,PLAY}.md` | `merge: rows` on all three — the wiring is live |

**Arms sabotaged and observed:**

- **Muzzle sabotage (B4), by me.** Added `and s["signal"] not in declared` to the over-pin filter at
  `drift_report.py:517`, making `DECLARED_EMPTY` an unconditional silencer. Observed **GREEN**:
  `selftest.py` rc 0 "all checks passed" *including* the line reading "the declaration was not a
  muzzle"; `check-arms.py` rc 0; `drift_report.py --check` rc 0; `test_codebase_map.py` rc 0. **No
  leg reddened.** Restored with `git checkout --`; `git status --porcelain` empty; selftest green
  again.
- **`.gitattributes` deletion (B7), verify stage, in a clone.** Dropped the `merge=rows` lines,
  `git check-attr` → `merge: unspecified`; bar still 38/39 green. The one red
  (`drift-audit records`) reproduced identically with the lines **restored** — a clone artifact, not
  a signal.
- **`pop_guard 3` removal (N1), verify stage.** Deleting the `pop_guard 3` call *does* red
  `check-memory-hygiene.test.sh` — so the guard's red half is armed; N1 is a precision defect, not an
  absent arm.

**Corruption reproduced by execution (all against the real `memory/DECISIONS.md`):**

- **B1 heading duplication, by me.** Driver run on the real file, both sides opening `## DEPL`:
  rc 0, `clean`, 0 markers, `## DEPL` ×2 (base 1), `*(none yet)*` ×3 (base 2).
  **Control:** `git merge-file -p` on the identical three inputs → **rc 1, 1 conflict hunk, heading
  ×1**. Also reproduced end-to-end by the verify stage through `git merge --no-edit` with the real
  attribute + config (`Merge made by the 'ort' strategy`, rc 0).
- **B5 misfiled row, by me.** Ours inserts a TOOL row in `## TOOL`, theirs a PLAY row in `## PLAY`:
  rc 0 `clean`, PLAY row at line 90 under `## TOOL` (heading 13, next heading 91).
  **Control:** the same two inserts through `git merge-file` → rc 0 with the PLAY row at line 10,
  correctly under `## PLAY`. **The misfiling is a regression introduced by U5.**
- **B3 grammar census + duplication, by me.** `extract.grammar_for('.')` + `anchor_at` over the real
  file → 91 lines, 73 rows, **35 anchored, 38 unkeyed**, the tail two being `TOOL-aMendedLedger-1b`
  and `-1c` added by this diff. Same `TOOL-aMendedLedger-<n>b` row filed by both nodes in different
  regions → rc 0, `0 new from theirs, 0 dropped, clean`, **id present twice** (lines 88, 93).
  Verify stage additionally measured the INERT half (`-9b` appends conflict, numeric `-9` appends
  resolve clean) and the e2e conflict through real git.
- **B2 / B6 silent take-ours, verify stage.** The README string configured verbatim → driver cannot
  start → `CONFLICT` with **ours-only content, 0 markers, status `UU`**. `resolve-python.sh` moved
  aside → `check-wiring --check` prints `ok merge — merge.rows.driver wired` while the same merge
  loses the incoming row. `memory-recall` moved aside → arm still `ok`, every merge conflicts
  wholesale.
- **N3, verify stage.** Unconfigured driver on `git 2.54.0.windows.1`: **0 bytes of stderr** in both
  the conflicting and the auto-resolving regime; in the latter the built-in fallback silently
  duplicated a row at rc 0.

**Merges performed:** none against this repo. Every reproduction ran the driver directly on scratch
copies under the session scratchpad, or used `git merge-file` as a control, or ran in a throwaway
`git clone --shared`. **Nothing was staged and nothing was committed.** The worktree was verified
clean (`git status --porcelain` empty) after each sabotage and after the corrupted-file hygiene run;
`tools/drift-audit/drift_report.py` and `memory/DECISIONS.md` were both restored to their committed
bytes.

**Not re-run by me** (carried from the verify stage, listed so a future reader knows which evidence
is second-hand): the adopter-fixture false red for N1, the State A/B `check-wiring` reproductions,
the `.gitattributes`-deletion clone run, the git-2.54 zero-stderr measurement, the
`similarity index` measurements behind N5, and the adopter-prefix `ROOT` failure behind N4.
