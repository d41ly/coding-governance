# Tier-2 code review — the cumulative diff landing on main (the `update` verb)

Scoped to `main...HEAD` for the aTetheredConvoy build: the `update` verb, the convergence ratchet,
`check`'s evidence loop, the seventeen descriptors and the registry rows. Batched lenses, then
skeptics defaulting to REFUTE inside the review protocol's hard cap, then one synthesis.

**Review shape: raw 25 candidates · confirmed 23 · refuted 2 · unverified 0 · precision 0.92.**

The 23 confirmed findings collapse to **14 distinct defects** — four clusters were found
independently by more than one lens, which is itself the signal: the write phase of `cmd_update` is
50 lines long and produced eleven of the twenty-three. The dedup map is the last section; every raw
id is accounted for, none is dropped.

## Verdict: BLOCKED — 2 blockers, 2 highs, 5 mediums, 5 lows

The verb is well-shaped in the read path and broken in the write path, and it breaks in one place
for one reason: **the `--write` loop dispatches on `verdict` alone and never reads the `how` it
computed forty lines earlier.** `cmd_update` spends lines 1456-1498 deciding, per role, whether gov
is even allowed to supply bytes — `seed` is `report-reseed  # never written`, `rendered` is
`adopter  # CAP at report; the adopter owns these bytes`, `project-owned` is `skip` — and then line
1516 throws that decision away and branches on the verdict string. Every role reaches the same
`if v == "stale" or v == "missing": dp.write_bytes(...)`. Two blockers, one high and two mediums are
that single line; a `how == "table"` guard on 1519 closes all five.

The second blocker is the same shape one level up: the schema-1 role-distrust arm (1467-1478) is a
one-shot validation that the run **which fails it** launders away, because `receipt["schema"] = 2`
at 1554 sits after the write block with no guard on `r.problems`. Running the documented command
twice turns a refusal into a silent overwrite of a `project-owned` file.

Everything else is smaller: one path-containment hole on target-supplied receipt data, one record
desync that leaves every updated target permanently red under `check`, two verdicts that are
reported but never computed (`re-rendered`, `unrecorded`), two selftest arms that cannot fail, and
five cosmetic dead-value / stale-doc items. Nothing here requires a redesign — the blockers are a
one-line guard and a two-line condition.

| id | sev | where | defect | fix |
|----|-----|-------|--------|-----|
| F1 | blocker | `govkit.py:1519` | The `--write` loop branches on `verdict` and never on `how`, so `rendered` and `seed` rows — both declared never-written — are written from gov's raw bytes on a `missing` verdict. Measured: unrendered `{{…}}` templates written and `git add`-ed into an adopter tree, exit 0 | Scope the write branch: `if a["how"] == "table" and v in ("stale", "missing"):` |
| F2 | blocker | `govkit.py:1554` | `receipt["schema"] = 2` is stamped unconditionally, including on a run whose schema-1 role-distrust arm REFUSED rows and exited 1 — so run 2 skips the guard and overwrites a `project-owned` file | Gate the stamp on `not r.problems` and on every row having been re-resolved; or migrate the row's role in place so the stamp is earned |
| F3 | high | `govkit.py:1518` | Target-supplied receipt paths are joined onto the target root with no containment check, so an absolute or `..`-bearing `path` escapes the named target and is written, deleted and re-hashed | One `under(target, rel)` helper that `resolve()`s and `relative_to()`s; route lines 979, 1367 and 1518 through it and refuse the row by name |
| F4 | high | `govkit.py:1525` | A `withdrawn` row is unlinked but never dropped from `receipt["files"]`, so the regenerated receipt and `install.sums` still claim it — `check` then reds permanently, with no verb that clears it | Filter the withdrawn rows out of `receipt["files"]` before the re-serialize at 1556 |
| F5 | medium | `govkit.py:1495` | `UPDATE_ROLE["rendered"] = "adopter"` is spec'd as "re-run the adopter, compare" but `cmd_update` never reads `d.get("adopt")` — it only relabels the verdict to `re-rendered`. 8 rendered rules across 5 kits get a false-green string | Run the kit's adopter and diff (`cmd_apply:1291` already resolves the argv), or rename the verdict to `re-render-needed` and say no adopter ran |
| F6 | medium | `govkit.py:1521` | The write phase refreshes `sha256` and `commit` but never `version`, so the receipt records the NEW commit against the OLD kit version string | Recompute `row["version"]` alongside the hash, resolved from `to_commit` rather than the working tree |
| F7 | medium | `govkit.py:1456` | `cmd_update` iterates only `receipt["files"]`; nothing scans the target, so the `unrecorded` verdict S5/AC10 specify is never emitted — `grep -rn unrecorded tools/govkit/` returns zero hits | After the row loop, resolve each claimed kit's destinations and report (never act on) any that exist on disk with no receipt row |
| F8 | medium | `selftest.py:471` | The arm "and `update --write` leaves the receipt's kit list unchanged" runs no `--write` and compares a JSON file to the dict it was serialized from nine lines earlier | Run a real `--write` on a fixture with un-installed available entries, and assert no row and no file appeared for any of them |
| F9 | medium | `selftest.py:433` | The arm the comment calls "THE NO-CLOBBER GUARANTEE" is graded on a fixture whose three-way can only conflict, so the sibling branch that writes merged bytes over the operator's file is exercised by nothing | Add a fixture with a disjoint edit so `git merge-file` succeeds, and assert explicitly what the merged write does |
| F10 | low | `govkit.py:315` | `resolve_entry` returns `missing` and `survivors`; no caller reads either | Drop both keys |
| F11 | low | `govkit.py:1240` | `if w.get("scope") == "machine"` tests a key the resolver row never carries — always false, two lines above the working rule-level test | Delete lines 1240-1241 |
| F12 | low | `govkit.py:1490` | `how == "seed"` can never fire (`UPDATE_ROLE` maps `seed` → `"report-reseed"`), and `three_way`'s second return value is discarded at its only call site | Drop the disjunct; make `three_way` return `bytes \| None` |
| F13 | low | `selftest.py:723` | `scratch_gov` is defined twice in one `main()` body with different signatures; the second shadows the first for everything below line 723 | Rename the unit-3 builder at 487 and its four call sites |
| F14 | low | `govkit.py:5` | The module docstring says "All five verbs" and omits `update` (USAGE lists six), and promises "the two SKIPPED lines `apply` prints" when this diff left one | Say six, name `update`, correct the SKIPPED count |

---

## F1 — blocker — `update --write` writes gov bytes for the two roles whose contract forbids it

**`tools/govkit/govkit.py:1519`** (write branch) · dispatch at `:1490-1496` · roles at `:1343`, `:1346`

The loop at 1516 unpacks `row`, `c`, `v` from each `acted` entry and never touches `a["how"]`,
which was recorded at 1498. So `UPDATE_ROLE`'s per-role policy governs the *report* and nothing
else.

**rendered.** `apply` records a rendered destination through the unlanded path (`:1231-1232`) with
no `sha256` and no `commit`. `classify_row` therefore computes `base = None` → `t_state = "differs"`
unconditionally; an absent artifact gives `o_state = "absent"`; `VERDICT_GRID[("absent","differs")]`
= `"missing"`. The `how == "adopter"` cap at 1495 rewrites only `diverged`/`stale`, so `missing`
falls straight into 1519. **Measured** in a scratch target: `apply --kits memory-tree` (whose adopter
exits 1 by design, seed-and-stop, so `memory/` never lands), then `update --write` → `wrote 3` —
`memory/HYGIENE.md`, `memory/TEMPLATE-SPEC.md`, `memory/guides/BUILD-METHOD.md`, each byte-identical
to gov's `*.template.md` with 7 / 2 / 10 surviving `{{…}}` placeholders, each `git add`-ed, exit 0.
Independently reproduced for `unattended`'s `.claude/skills/unattended/SKILL.md` (17 surviving
placeholders). The row then gains a `sha256` and a `commit`, so `install.sums` and `check` agree with
the corruption and the next `update` calls it `current`. This is exactly the surviving-placeholder
class `adopt-unattended.sh --check` exists to red on, written silently into a repo gov does not own.
8 rendered rules across `memory-tree` (3), `unattended` (2), `drift-audit`, `memory-recall`,
`workflows` are reachable this way.

**seed.** The report-reseed block at 1490-1494 deliberately passes `missing` through unchanged
(`elif v not in ("missing",)`), so a seed the owner deleted keeps verdict `missing` and is written.
**Measured**: apply `playbook`, `git rm docs/PARALLEL.md` and commit (the legitimate owner decision a
seed-then-own role exists to permit), `update --write` → `missing [seed] docs/PARALLEL.md` /
`wrote 1`, file restored and staged, exit 0. `update` silently reverses an owner decision, against
its own `# never written` comment.

**Fix.** One condition:

```python
if a["how"] == "table" and (v == "stale" or v == "missing"):
```

For `report-reseed` and `adopter` rows, print the verdict and leave the bytes alone. If reseeding is
ever wanted it is an explicit `--reseed` flag, not a fallthrough.

**Left-shift gate.** `selftest.py`'s unit-2 block exercises only the flat `check-wiring` entry, i.e.
engine rows only — AC10 and AC11 have no arms at all. Add two to `tools/govkit/selftest.py` (already
a bar leg via `govkit selftest`): a `rendered` row whose artifact is absent, asserting `update
--write` writes nothing and the destination stays absent; and a `seed` row deleted by the owner,
same assertion. Then a cheap invariant arm that outlives both: after any `update --write`, assert no
path on disk under the target contains a `{{`-shaped token — the same predicate
`adopt-unattended.sh --check` already runs, borrowed one layer up.

## F2 — blocker — the schema-1 distrust guard survives exactly one run

**`tools/govkit/govkit.py:1554`** (`receipt["schema"] = RECEIPT_SCHEMA`) · guard at `:1467-1478`

The guard exists because unit 1 measured that a schema-1 receipt stamps `engine` on files the
descriptor declares `project-owned`; it refuses the disagreeing row and adds a finding. But the only
early return between the loop and the write phase is `if not write` at 1510, so 1554 runs on a
failing run — unconditionally, with the offending row's `role` left untouched.

**Reproduced** in a scratch gov+target. Run 1: `tools/demo/owned.sh` recorded `engine`, descriptor
resolves `project-owned` → the refusal prints, exit 1 — and the receipt is still rewritten with
`schema: 2` and the row still tagged `engine`. Run 2: schema 2 → the `schema < 2` arm is skipped
entirely, the row is trusted as `engine`, `how = "table"`, verdict `stale`, and 1521 **overwrote the
project-owned file with gov's bytes** (`gov-v1` → `gov-v2`), exit 0. That is gov supplying bytes for
the one role whose contract is that it never does, reachable by running the documented command
twice.

Two sub-claims ride along and are also true: rows carrying no `kit` field, or a `kit` not in
`descs`, are never validated at all yet ride the same promotion (the guard is
`schema < 2 and row.get("kit") in descs`); and a `now` of `None` inside the guard falls through with
no confirmation. Separately, `receipt["gov_commit"] = to_commit` at 1555 is stamped after a loop
that may have incremented `conflicts` and `r.fail`ed rows, so the receipt asserts a completed
migration while a conflicted file sits at the old bytes.

**Fix.** Track whether every row was re-resolved and agreed, and gate the promotion on it *and* on
`not r.problems`. `gov_commit` likewise: stamp it only when `not r.problems and conflicts == 0`,
otherwise print that the migration is partial and leave the recorded commit.

**Left-shift gate.** `selftest.py` has no arm on `update`'s schema promotion at all. Add the
reproduction as an arm — a schema-1 receipt with one mis-stamped role, assert exit 1 **and** that
the receipt on disk still reads `schema: 1`. The generalizable form, and the one worth having: after
any run where `r.emit()` is non-zero, the receipt is byte-identical to what it was before. That one
arm covers this defect and every future variant of it.

## F3 — high — receipt paths are joined onto the target with no containment check

**`tools/govkit/govkit.py:1518`** (`dp = target / row["path"]`) · same join at `:1367`
(`classify_row`) and `:979` (`cmd_check`'s new evidence loop)

`grep -n 'relative_to\|is_relative_to\|is_absolute' tools/govkit/govkit.py` returns **nothing** —
there is no containment check anywhere in the file. `--target` is `.resolve()`d at argv parse, and
pathlib's `/` lets an absolute right operand replace the left outright, so a row with
`"path": "C:/Users/x/.ssh/authorized_keys"` resolves to that absolute path and
`"../../.githooks/pre-push"` walks out of the tree.

The write is reachable with no gating on `how`: a row with `role` absent (defaults `engine`), a
resolvable `source`, and `schema: 2` skips the re-resolution at 1467; `classify_row` gives
`o_state = absent` → `missing` → 1520-1522 does `mkdir(parents=True)` + `write_bytes(theirs)` outside
the named target. `withdrawn` → `unlink()` is narrower (needs the on-disk hash to match the receipt)
but is the same join. `cmd_check` will `read_bytes()` and hash whatever the receipt names.

`.governance/install.json` is a committed file in a repo govkit does not own, and `cmd_check`'s own
docstring is written around a receipt whose "every recorded commit was rewritten to zeros and whose
every hash was rewritten to nonsense" — this file's whole discipline is refuse-before-write (it
refuses a gov-checkout target, a foreign kit, an unresolvable base commit). A path string that
escapes the target is a hole in exactly that discipline.

**Fix.** One helper, three call sites:

```python
def under(target: pathlib.Path, rel: str) -> pathlib.Path:
    p = (target / rel).resolve()
    p.relative_to(target.resolve())      # raises if it escaped
    return p
```

Refuse the row by name (`r.fail`) rather than skipping it silently; also refuse a `rel` that is
absolute by `PurePosixPath` or carries a drive letter, so the refusal message names the real problem
rather than a resolution artifact.

**Left-shift gate.** A `selftest.py` arm per escape shape — `..`-relative and absolute — asserting
`update --write` and `check` both refuse by name and that the out-of-target path does not exist
afterwards. Then a one-line invariant arm on `apply`, which is the verb that *writes* the receipt:
every `path` it records is target-relative and contains no `..` segment. Cheapest place to stop the
class is where the value is minted, not where it is consumed.

## F4 — high — a `withdrawn` file is deleted from disk and kept in the record

**`tools/govkit/govkit.py:1525`** (`elif v == "withdrawn":`) · re-serialize at `:1554-1559` ·
`check`'s existence arm at `:979-983`

The branch unlinks the file and appends to `deleted`, but never removes the row from
`receipt["files"]`; 1556-1559 then re-serializes that same untouched list and rebuilds
`install.sums` from it. So after a *successful* withdrawal the receipt and the sidecar both claim a
path that does not exist.

**Reproduced** on both a minimal fixture and a real `check-wiring` install: `update --write` →
`withdrawn 1` / `deleted 1`, exit 0; `install.sums` still carries the hash; the very next
`govkit check` prints `'tools/check-wiring.test.sh' is in the receipt and not on disk` and exits 1.
The `written is False` escape at 981 does not apply — `cmd_apply` stamps `written: True` on engine
rows. And it does not self-correct: re-running `update` re-classifies the row `converged`
(`VERDICT_GRID[("absent","absent")]`), which is in no write branch, so `check` stays red on every
subsequent pass. The only route back to green is hand-editing a tool-written receipt. A target
verifying the sidecar with `sha256sum -c` — the sidecar's stated purpose — fails too.

`withdrawn` is the only deleting verdict, and it is the one that desynchronizes the two readers of
the one record.

**Fix.** Immediately before the rewrite at 1556:

```python
receipt["files"] = [f for f in receipt["files"] if f["path"] not in set(deleted)]
```

(A `deleted: true` tombstone plus a matching skip in `cmd_check` also works and keeps the history,
but it is the larger diff for the same guarantee.)

**Left-shift gate.** The general arm, not the specific one: **after any `update --write`, running
`check --target` on the same target exits 0.** `update` and `check` are two readers of one record;
nothing on the bar today asserts they agree. That single round-trip arm in `selftest.py` catches
this defect, catches F6's version drift the moment `check` learns to read the field, and catches
whatever the next write branch forgets to record.

## F5 — medium — `re-rendered` is printed by a code path that renders nothing

**`tools/govkit/govkit.py:1495`** · role declared at `:1346` ("re-run the adopter, compare, CAP at
report")

`d.get("adopt")` appears at exactly two sites in the file — 649 (selfcheck) and 1589
(`needed_answers`) — plus `cmd_apply`'s CONFIGURE step at 1291 (`d.get("adopt", {}).get("argv")`).
`cmd_update` (1402-1562) touches none of them; 1495-1496 relabels the verdict string and stops.
Spec DEPL-aTetheredConvoy-2's role table and AC11 both require the run ("asserted by the file
matching a fresh render"), and the build record lists unit 2 as BUILT without deferring it.

Worse than the label: `rendered` is not in `LANDABLE_ROLES`, so those rows carry no `sha256` and no
`commit`, which forces `t_state = "differs"` on every classification — so **every** rendered row
whose artifact exists prints `re-rendered` on **every** update, whether or not anything moved. 8
rows across 5 kits. After `update --write` moves a kit's engine bytes forward, the target's rendered
artifacts are still at the old render and the report says they were re-rendered.

**Fix.** Either run the kit's adopter for the row's kit and diff the result — `cmd_apply:1291`
already resolves `adopt.argv` against the target context, so reuse it — or rename the verdict to
something that does not claim an action (`re-render-needed`) and state in the summary that no
adopter was invoked. The rename is the lazy correct move if the run is deferred; the false claim is
the defect, not the deferral.

**Left-shift gate.** Whichever way it resolves, add the arm that makes the verdict mean something:
a rendered row on a fixture where *nothing moved* must not print an action verdict. A verdict that
fires on every run is indistinguishable from a verdict that is never computed — that is the same
liveness rule this repo already applies to drift-audit signals ("a probe that cannot move prints
DEAD PROBE").

## F6 — medium — the receipt's `version` field is never refreshed by `update`

**`tools/govkit/govkit.py:1521-1523`** and `:1543-1545` · stamped by `cmd_apply` at `:1250`

Both mutating branches refresh `row["sha256"]` and `row["commit"]` and neither touches
`row["version"]`, the per-row kit-version string `cmd_apply` writes from `entry_version`.

**Reproduced**: bumped `KIT_CHECK_WIRING_VERSION` from 1.0 to 9.9 in a gov clone, committed, ran
`update --write`. The target's `tools/check-wiring.sh` on disk now reads 9.9; the receipt row reads
`version: KIT_CHECK_WIRING_VERSION=1.0` against the NEW commit and the NEW sha256. The receipt is
the only record of what version a target runs, and the `[[outcome]]` / `remove` units defer to this
field.

**Fix.** Recompute alongside the hash in both branches. `entry_version` reads the working tree, so
if `--to` can differ from HEAD, resolve the constant through `blob_at(root, to_commit, …)` instead —
otherwise the fix records a third wrong answer.

**Left-shift gate.** Covered by F4's round-trip arm the moment `check` compares the receipt's
`version` to the installed bytes. Add that comparison to `cmd_check`'s engine-row loop (it already
has the bytes in hand for the hash) — one predicate, and the drift becomes impossible to ship
silently.

## F7 — medium — the `unrecorded` verdict S5/AC10 specify does not exist

**`tools/govkit/govkit.py:1456`** (`for row in receipt.get("files", [])`)

`grep -rn unrecorded tools/govkit/` returns zero hits. `cmd_update`'s only loop is over the receipt;
nothing walks the target. `cmd_check` is blind the same way — its disk arm (979-983) quantifies
receipt→disk and its sidecar arm (1030-1034) quantifies receipt↔`install.sums`; neither quantifies
disk→receipt.

**Reproduced** on the exact S5/AC10 fixture: applied `check-wiring` (2 files landed), set `schema: 1`
and deleted the `tools/check-wiring.test.sh` row from the receipt and its `install.sums` line, file
still on disk and gov-installed. `update` reported `current 1` and never named it; `check` exited 0
reporting `integrity: 1/1` and `sidecar: 1 line(s) compared against 1 hashed row(s)` and never named
it. The one guard the spec names for old installs quantifies over a population that excludes the
failure it was written for.

**Fix.** After the row loop, resolve each claimed kit's destinations (`descs` and `resolve_entry` are
already in scope) and print `unrecorded` for any resolved destination present on disk with no
receipt row. Report only, never act — per the role table.

**Left-shift gate.** Add the AC10 arm to `selftest.py` with the fixture above, asserting the
`unrecorded` string appears and names the path. The reusable rule: for every verdict in the grid,
`selfcheck` should assert the string is *reachable* in the code that prints verdicts — a verdict
declared in a table and emitted by nothing is the govkit analogue of an unarmed `fail` branch, which
this repo already gates with `check-arms.py`.

## F8 — medium — an AC8 arm that compares a value to itself

**`tools/govkit/selftest.py:471`** — "and `update --write` leaves the receipt's kit list unchanged"

Line 462 writes `rec` to `rp`; 463 runs `update` with **no** `--write` (`cmd_update` returns at
govkit.py:1511 before touching anything); 470 re-reads that same file into `rec2`; 471-472 asserts
`rec2["kits"] == rec["kits"]`. A JSON round-trip of one dict compared to itself, with no writing run
in between. The preceding `--write` at line 450 raised the unresolvable-commit `Refusal` (exit 2)
before the write phase, so it changed nothing either.

The arm's label names a `--write` that never ran. AC8's load-bearing half — that `update --write`
does not silently widen a target's governance surface with the `available (not installed)` entries —
is asserted by nothing. Both the fixture-passes-by-finding-nothing class and the
assertion-between-two-derived-values class, in one arm.

**Fix.** Run `update --target <up3> --write` on a fixture that has un-installed available entries,
then assert both `rec2["kits"] == rec["kits"]` **and** that no receipt row and no on-disk file
appeared for any entry in the `available` list.

**Left-shift gate.** This one is meta and worth the cost: `selftest.py` is a bar leg whose arms are
the bar. A cheap scan — an arm whose message mentions `--write` must appear in a block that actually
invokes `--write` — is a five-line predicate in `selftest.py`'s own `--selftest` sense, and it is the
same doctrine `check-arms.py` already enforces on the hygiene engine (every `fail` branch armed by a
positive assertion naming its own failure text).

## F9 — medium — the no-clobber guarantee is graded on a fixture that can only conflict

**`tools/govkit/selftest.py:433-439`** — `# AC3 — THE NO-CLOBBER GUARANTEE. Nothing else observes it.`

Measured on the fixture: ours = 36 bytes of `# OPERATOR EDIT`, base (`check-wiring.sh` at 24f39915)
= 33243 bytes, theirs (HEAD) = 34084 bytes. `git merge-file -p` returns rc=1 — conflict. So
`cmd_update` always takes the outbox path at 1531-1541 on this fixture, and the sibling branch at
1542-1546, which does `dp.write_bytes(merged)` over the operator's file, is exercised by no arm in
the file.

The arm's message states a general "never overwritten" guarantee that the code honours only when the
merge conflicts. (One correction to the finding's framing that does not change the verdict: a
successful `merge-file` output retains the operator's hunks, so "silent data loss" overstates it —
the defect is an unexercised write branch sitting behind an arm whose text claims it cannot happen.)

**Fix.** Add a second fixture whose edit is disjoint from gov's change so `git merge-file` succeeds,
and assert explicitly what happens: either the merged write is intended — then reword the arm to say
"merged, not clobbered" — or it must be capped at report like `rendered` is.

**Left-shift gate.** The generalizable arm for the whole `update` write phase: every branch of the
`for a in acted:` loop is reached by at least one arm. Five branches, five fixtures; today three are
covered. That enumeration is cheap and it is what F1 and this finding are both instances of — an
untraversed branch in the one loop that writes bytes into a repo gov does not own.

## F10 — low — `resolve_entry` returns two keys nobody reads

**`tools/govkit/govkit.py:315`** — `"missing": sorted(set(missing)), "survivors": survivors`

Exhaustive subscript grep over every consumer (govkit.py:686, 706, 867, 1220, 1470 and
selftest.py:318-328): callers read `writes`, `unlanded`, `carved` and `census`, and check
missing-ness through the per-row `w["missing"]`. Nothing reads `res["missing"]` or
`res["survivors"]`. So the aggregation and the `sorted(set(...))` run per entry per verb for no
reader, and `survivors` keeps a purely internal intermediate alive in the return of the one resolver
that `plan`, `apply`, `check` and `update` all share.

**Fix.** Drop both keys. **Left-shift gate.** None worth building for this class — an unused-key
linter over dict returns costs more than it saves. Ordinary review catches it.

## F11 — low — a permanently-false guard two lines above the working one

**`tools/govkit/govkit.py:1240`** — `if w.get("scope") == "machine": continue`

`expand_rules` (263-268) emits rows with exactly `{rule, src, dest, role}`; `resolve_entry` (:305)
adds `dest`/`missing`. Nothing anywhere assigns `scope` onto a write row — `scope = "machine"` exists
only at the rule level (`entries/kickoff-manifest.kit.toml:25`). The three `scope` reads in the file
are :876 (on the rule), :1240 (this one) and :1243 (the working one, on the rule re-fetched via
`d.get('files')[w['rule']]`).

No runtime defect today. The stated risk is the real one: it reads as a redundant duplicate of the
line below, so a later cleanup deletes the working one and machine-scoped rules land into targets.

**Fix.** Delete 1240-1241. **Left-shift gate.** None — deleting the line is the gate.

## F12 — low — two dead values in the verb's decision path

**`tools/govkit/govkit.py:1490`** (`if how == "seed" or how == "report-reseed"`) and **`:1530`**
(`merged, how = three_way(...)`)

`UPDATE_ROLE`'s values are `{table, report-reseed, skip, adopter, refuse}` — never the literal
`"seed"` — and `how` is only ever `UPDATE_ROLE.get(role)` at 1458, with the dict never mutated. So
the first disjunct cannot fire. `three_way` is defined at 1381 and called at exactly one site, 1530,
where its second return value is bound (shadowing `how`, incidentally) and never read — the caller
branches on `merged is None`.

**Fix.** Drop the disjunct; make `three_way` return `bytes | None`. **Left-shift gate.** None; both
are one-line deletions.

## F13 — low — `scratch_gov` is defined twice in one function body

**`tools/govkit/selftest.py:723`** shadows **`:487`**

Same 8-space indentation inside the single `main()` body, different signatures
(`(kit_toml) -> CompletedProcess` vs `(mutates, guard) -> pathlib.Path`), so the second binds over
the first for everything below 723. It works only because every unit-3 call site (541, 545, 551,
555) and the `scratch_gov.n` counter (527, read at 488-489) sit above it. Latent: an arm added below
723 that wants the unit-3 builder gets a `TypeError` inside a gate leg rather than a readable arm.

**Fix.** Rename the unit-3 builder to `scratch_gov_legs` and update its four call sites plus the
counter attribute.

**Left-shift gate.** A `python -We::SyntaxWarning -m py_compile` will not catch this, but the
existing `govkit selftest` leg would surface it the day an arm lands below 723 — as a `TypeError`, not
a finding. If it recurs, the cheap catch is an AST pass over `selftest.py` asserting no duplicate
`def` name inside one scope; not worth building for a single instance.

## F14 — low — the module docstring describes a five-verb file

**`tools/govkit/govkit.py:5-8`**

Line 5 says "All five verbs" and enumerates `selfcheck` / `plan` / `check` / `apply` / `intake` —
`update` is absent, while `USAGE` at 1671-1677 lists six and `main()` dispatches six. Line 8 points
the reader at "the two SKIPPED lines `apply` prints" (with 12-15 promising both steps are "REPORTED
on every run"), but exactly one SKIPPED print survives (`:1273`); `git diff main` shows the second
(`.gitattributes blocks: SKIPPED`) was deleted in this branch along with selftest.py's assertion on
it. The gitattributes step is now reported per-row via `UNLANDED_REASON` when a descriptor declares
such a rule, not on every run.

**Fix.** Say six verbs, name `update` and its read-only default, and correct the SKIPPED sentence to
the one line actually printed (or restore the missing print).

**Left-shift gate.** Real and cheap, because this file's whole thesis is one spelling: a `selfcheck`
arm asserting every verb `main()` dispatches appears in both `USAGE` and the module docstring. The
verb set is already enumerable from the dispatch table; two membership tests close the class
permanently.

---

## The one class, and the one gate that would have caught most of it

Eleven of the twenty-three confirmed findings — F1, F2, F4, F6, and the four raw duplicates each
attracted — live in the fifty lines between `govkit.py:1516` and `:1559`. That is the block that
writes bytes and deletes files in a repository gov does not own, and it is the block with the
weakest arms: unit 2's selftest coverage is engine rows on one flat entry, and AC10/AC11 have no
arms at all.

The single highest-value left-shift, ahead of any individual fix, is the **round-trip invariant**:
after any `update --write`, `govkit check --target` on the same target exits 0; and after any
`update` run that exits non-zero, the receipt is byte-identical to what it was before. Those two
assertions catch F2, F4 and F6 directly, and they would have caught F1's receipt re-stamping the
moment a rendered row gained a hash it should never have had. Both are a handful of lines in
`tools/govkit/selftest.py`, which already rides the bar.

## Dedup map — 23 confirmed → 14 distinct

| report id | raw ids | why merged |
|-----------|---------|------------|
| F1 | 6 (blocker), 19 (blocker), 2 (high), 9 (medium), 22 (medium) | One root cause: the write loop at 1519 ignores `how`. 6 and 19 are the rendered manifestation found twice, 9 and 22 the seed manifestation found twice, 2 is the shared diagnosis. Severity taken from the highest confirmed manifestation |
| F2 | 10 (blocker), 4 (medium), 21 (medium) | All three are the unconditional stamp at 1554-1555; 10 carries the reproduced two-run data-loss path, 4 adds the `gov_commit` half |
| F3 | 1 (high) | — |
| F4 | 7 (high), 11 (high), 3 (medium), 20 (medium) | Four independent reproductions of the withdrawn row surviving the receipt |
| F5 | 12 (medium) | — |
| F6 | 13 (medium) | — |
| F7 | 14 (medium) | — |
| F8 | 23 (medium) | — |
| F9 | 24 (medium) | — |
| F10 | 15 (low) | — |
| F11 | 16 (low) | — |
| F12 | 17 (low) | — |
| F13 | 18 (low) | — |
| F14 | 25 (low) | — |

Two candidates were refuted at the skeptic stage and are not carried here. No finding is unverified:
every row above was confirmed against source, and F1, F2, F3, F4, F6, F7 and F9 were reproduced or
measured on live fixtures — the reproduction commands are in each section.
