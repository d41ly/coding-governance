# TOOL-dDeclaredLoop-43 — the guarded write restores each path's prior bytes, and writes each through a sibling temp file

**Status:** DEFERRED · rev-3 · 2026-11-15 · node d · Tier-2 · base ed497191 · streams tooling · order 16 · advances TOOL-dDeclaredLoop-35

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md) | journal | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 TOOL-dDeclaredLoop-68 TOOL-dDeclaredLoop-69 TOOL-dDeclaredLoop-70 TOOL-dDeclaredLoop-71 TOOL-dDeclaredLoop-72 TOOL-dDeclaredLoop-73 TOOL-dDeclaredLoop-74 TOOL-dDeclaredLoop-75 TOOL-dDeclaredLoop-76 TOOL-dDeclaredLoop-77 TOOL-dDeclaredLoop-78 TOOL-dDeclaredLoop-79 TOOL-dDeclaredLoop-80 TOOL-dDeclaredLoop-81 TOOL-dDeclaredLoop-82 TOOL-dDeclaredLoop-83 TOOL-dDeclaredLoop-84 TOOL-dDeclaredLoop-85 TOOL-dDeclaredLoop-86 TOOL-dDeclaredLoop-87 TOOL-dDeclaredLoop-88 TOOL-dDeclaredLoop-89 TOOL-dDeclaredLoop-90 TOOL-dDeclaredLoop-91 TOOL-dDeclaredLoop-92 TOOL-dDeclaredLoop-93 TOOL-dDeclaredLoop-94 TOOL-dDeclaredLoop-95 TOOL-dDeclaredLoop-96 TOOL-dDeclaredLoop-97 TOOL-dDeclaredLoop-98 TOOL-dDeclaredLoop-99 TOOL-dDeclaredLoop-100 |
| [2026-10-24-build-TOOL-dDeclaredLoop-36-promoted-fix-return.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-36-promoted-fix-return.md) | research | TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 |
| [2026-10-24-build-TOOL-dDeclaredLoop-43-deviation-431.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-43-deviation-431.md) | deviation | — |
| [2026-11-15-build-TOOL-dDeclaredLoop-43-deviation-432.md](../build/2026-11-15-build-TOOL-dDeclaredLoop-43-deviation-432.md) | deviation | — |
| [2026-10-24-prompt-TOOL-dDeclaredLoop-36-promoted-fix-brief.md](../prompts/2026-10-24-prompt-TOOL-dDeclaredLoop-36-promoted-fix-brief.md) | research | TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 |
| [2026-11-15-prompt-TOOL-dDeclaredLoop-43-1-spec-writer.md](../prompts/2026-11-15-prompt-TOOL-dDeclaredLoop-43-1-spec-writer.md) | journal | — |
| [2026-11-15-prompt-TOOL-dDeclaredLoop-43-reground-brief.md](../prompts/2026-11-15-prompt-TOOL-dDeclaredLoop-43-reground-brief.md) | research | — |
| [2026-10-24-review-TOOL-dDeclaredLoop-36-spec-audit.md](../reviews/2026-10-24-review-TOOL-dDeclaredLoop-36-spec-audit.md) | spec-audit | TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit (`memory/builds/dDeclaredLoop/reviews/2026-10-24-review-TOOL-dDeclaredLoop-1-spec-audit.md`)
confirmed finding **id 49 at HIGH**, its item **H15**: the guarded write's rollback deleted an existing
policy file instead of restoring it, and neither write was atomic against an interrupt.
`TOOL-dDeclaredLoop-2` landed the first half. `tools/lib/guarded_write.py#write_guarded` reads the
target's prior bytes before writing, puts them back when either step raises, and deletes the target only
where it did not exist. The second half is still open: the write and the restore each go to the target in
place, through `path.write_bytes` or the caller's callable handed the target itself, so an interrupt or a
full disk mid-write leaves the policy file truncated, and every policy reader then falls back to catalogue
defaults. This unit routes both through a sibling temp file and `os.replace`.

## 2. Scope (IN)

- **S1** — `write_guarded` writes the new text through a sibling temp file in the target's own directory,
  then `os.replace`s it over the target, so the target holds its prior bytes or the new text and never a
  part of either. The temp takes an unpredictable name, `<name>.<random>.tmp`, created exclusively and
  owner-only through `tempfile.mkstemp`, the shape of `tools/run-gates/held_halves.py#write_replace`
  (§8 F2). A failure before the rename leaves no temp file behind. Observed by AC1, AC2, AC3.
- **S2** — The restore after a raising step goes through the same sibling-temp replace: a target that
  existed gets its prior bytes back by a rename, and one that did not exist is unlinked, as
  `TOOL-dDeclaredLoop-2` landed it. The original error is raised again. Observed by AC1, AC2.
- **S3** — A callable `new_text` is handed the temp path, not the target, and the temp already holds the
  target's prior bytes, or is empty where the target did not exist, so a callable that reads its path
  before writing it, `tools/playbook/overlay.py#write_overlay_units`, reads what the target held. Observed
  by AC4, AC6.
- **S4** — The change lands in the canonical block of `tools/lib/guarded_write.py` and, byte-identical,
  in the `guarded_write_py` copies `tools/loop/policy_edit.py` and `tools/playbook/instructions_edit.py`
  carry; each file imports `os` and `tempfile` at its head where it does not already. Observed by AC5.
- **S5** — `tools/loop/guard.py` gains the plant `write-guarded-rollback`, four in-process scenarios over
  the loop kit's copy in `tools/loop/policy_edit.py`, run by `--selftest` with every other plant. Observed
  by AC1, AC2, AC3, AC4.

## 3. Non-goals (OUT)

- rev-2's S1, reading each target's prior state before any write, and the restore-not-delete half of
  rev-2's S3: `TOOL-dDeclaredLoop-2` built both into `write_guarded`, so they leave this unit's scope as
  built. The record is the caller's `record()` callable since that unit, so rev-2's restore of a second
  path has no second path to act on.
- Crash consistency past an exception: no fsync and no directory sync, the limit
  `tools/govkit/upgrade_steps.py#write_atomic` states for itself.
- The record's own atomicity. `tools/memory-tree/build_records.py#write_record` validates every field
  before it opens the file, and opens it exclusive, `open(path, "x")`; an interrupt inside its one write
  is that writer's, in the memory-tree kit, outside this block.
- The file mode bits: the replaced target takes the temp's owner-only mode on POSIX, as
  `write_replace` ships; git records only the executable bit, so the index sees no change.
- The terminal proof and its win32 console test: the audit's id 21, batched into
  `TOOL-dDeclaredLoop-56`.
- Extracting one cross-kit temp-replace factory (§8 F3).
- A bug-class checklist entry for "a guarded write lands in place", the finding's left-shift: the class is
  recorded at the close; the plant is this instance's gate.

### Edges

- **consumes-from** `TOOL-dDeclaredLoop-2` — `write_guarded` in `tools/lib/guarded_write.py` and its two inline copies, with the prior-bytes restore that unit landed; this unit moves the write and the restore onto a sibling-temp rename
- **hands-off** `TOOL-dDeclaredLoop-67` — the round-2 minors ids 7, 16, 20, 44 and 49, read over this unit's `write-guarded-rollback` plant in `tools/loop/guard.py` and the three-argument `write_guarded(path, new_text, record)` form this pass keeps

## 4. Design

### Evidence

- `write_guarded` at HEAD writes `path.write_bytes(new_text.encode("utf-8"))`, or calls `new_text(path)`,
  then `record()`; on any `BaseException` it unlinks the path where `held` is `None`, else
  `path.write_bytes(held)`, and raises again (`tools/lib/guarded_write.py#write_guarded`). Both writes
  truncate the target first.
- `tools/run-gates/held_halves.py#write_replace` writes through `tempfile.mkstemp(dir=folder,
  prefix=name + ".", suffix=".tmp")` and `os.replace`, removing the temp on any `BaseException`; its
  docstring gives the reason for the unpredictable name: a fixed `<name>.tmp` is a name a planted link
  redirects.
- `tools/govkit/upgrade_steps.py#write_atomic` is the fixed-name shape, `<name>.govkit-new`, and states why
  the temp is a sibling: `os.replace` raises across a filesystem boundary.
- The two callers: `tools/loop/policy_edit.py#write_policy_change` passes text;
  `tools/playbook/instructions_edit.py#write_candidate` passes `overlay.write_overlay_units` as a
  callable for an overlay `add`, and that writer reads its target's bytes before writing them.
- The policy file is the owner's guarded file; its loss is silent, because every reader falls back to
  the catalogue default (`TOOL-dDeclaredLoop-2` §4 "Data model").

### The write

The block's body after this unit. One nested helper, so the codebase map's symbol list, which reads
top-level definitions only (`tools/codebase-map/map_lib.py#python_symbols`), gains no row.

```python
def write_guarded(path, new_text, record):
    path = pathlib.Path(path)
    held = path.read_bytes() if path.is_file() else None

    def replace_target(fill):
        fd, tmp = tempfile.mkstemp(dir=path.parent, prefix=path.name + ".", suffix=".tmp")
        try:
            with os.fdopen(fd, "wb") as fh:
                fh.write(fill if isinstance(fill, bytes) else held or b"")
            if callable(fill):
                fill(pathlib.Path(tmp))
            os.replace(tmp, path)
        except BaseException:
            pathlib.Path(tmp).unlink(missing_ok=True)
            raise

    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        replace_target(new_text if callable(new_text) else new_text.encode("utf-8"))
        return record()
    except BaseException:
        if held is None:
            path.unlink(missing_ok=True)
        elif path.is_file() and path.read_bytes() != held:
            replace_target(held)
        raise
```

`BaseException`, as at HEAD, so a `KeyboardInterrupt` between the rename and the record restores too. The
restore skips a target whose bytes are still the prior ones, so a failure before the rename writes
nothing more. The docstring keeps its contract and names the sibling temp.

### The plant

`write-guarded-rollback` joins `PLANTS` in `tools/loop/guard.py` and runs as one more branch of
`tools/loop/guard.py#run_guard_plant`, after `write_guard_plant` has committed the scratch policy file.
It imports the loop kit's `policy_edit` module from `KIT`, and wraps `os.replace` with
`unittest.mock.patch.object` in a spy that records each destination and can raise once. Each scenario
appends `(name, 0 if every observation holds else 1, 0, "bytes held", said)`, `said` naming each
observation, so `run_fixture` prints it `held` or `MISSED`. A `KeyboardInterrupt` the third scenario
plants is caught inside that scenario, because `run_fixture` catches only `LookupError`, `LoopError`,
`OSError` and `CalledProcessError`.

| Scenario | Plant | Observed |
|---|---|---|
| `record refused over a prior file` | `record` raises `OSError("fx: record refused")` | the error reached the caller; the policy file's bytes equal the committed bytes; two renames onto it; no `policy.toml.*.tmp` sibling |
| `record refused, no prior file` | the same over `fx-absent/policy.toml` | the path does not exist; one rename onto it; no temp sibling |
| `interrupted at the rename` | the spy raises `KeyboardInterrupt` on its first call | the interrupt reached the caller; the policy file holds the committed bytes; no temp sibling |
| `a callable over its prior bytes` | `new_text` reads the path it is handed and appends one line | the policy file is the committed bytes plus the line; the handed path is a sibling, not the target; `record()`'s value returned; no temp sibling |

`run_selftest`'s owed map needs no entry: the plant's last scenario owes exit 0, the default.

### Files touched (estimate)

- `tools/lib/guarded_write.py`
- `tools/loop/policy_edit.py`
- `tools/playbook/instructions_edit.py`
- `tools/loop/guard.py`

### Alternatives rejected

- **Writing the record first, then the target.** It narrows the window and still leaves the target
  half-written by an interrupt in its own write.
- **Importing a shared writer.** The loop and playbook kits are copy-installed and `<prefix>/lib/` ships to
  no install, so neither can import `write_replace` or `write_atomic`; the block carries the shape inline.
- **The rollback arm in `tools/lib/resolve-python.test.sh`.** That suite holds the copies to the canonical
  already; the behaviour is observed once, over a carrier, and `TOOL-dDeclaredLoop-67` §2 S10 reads the
  plant in `tools/loop/guard.py`.

## 5. Production-readiness checklist

- security — closes a data-loss path in the owner's guarded file; the temp's unpredictable, exclusive name
  leaves no fixed sibling for an agent to plant as a link (§8 F2).
- perf / scale — one temp file and one rename per write, two on a restore; the plant adds one scratch
  repository to the `loop guard fixtures` leg, inside its declared ceiling of 300 s, PINNED from
  `tools/gate-legs.json` on 2026-11-15.
- error / empty / loading states — a failure before the rename leaves the target as it was and no temp; a
  failure after it restores by rename; a target absent before is absent after.
- observability — the original error is raised again, and each caller prints it in its `refused` line.
- risks — a restore that itself raises replaces the original error, which Python keeps as its context,
  and the target may then hold the new text; the window is one rename.
- testing — AC1 to AC6; the plant under §7, observed RED over HEAD's in-place write, then GREEN.
- migration — none.
- user docs — none: `help/policy.md` states what the door writes, and this unit changes how, not what.

Existing arms this change could newly red, and what keeps each green:

| Arm | Why it could red | What keeps it green |
|---|---|---|
| `python resolver (behaviour + inline parity + idiom ban)` | its `guarded_write_py` row compares the three blocks | S4 writes the same block in all three; AC5 |
| `loop guard fixtures` | the `raise-admitted`, `proof-signed-*` and `set-run-live` plants write through `policy_edit.py` | the success path writes the same bytes; S5's plant joins its run |
| `instruction edits selftest` | its write arms reach `write_candidate` | text writes are unchanged in content; S3 keeps the callable's read |
| `playbook render selftest` | it runs `overlay.py --fixture`, whose `write-then-render` plant adds an overlay row through the callable | S3 hands the callable a temp holding the prior bytes; AC6 |
| `codebase-map coverage + freshness` | `memory/map/generated/symbols.json` lists top-level functions | no top-level definition is added; the helper is nested |

Unchanged, read and found untouched: the `[[exempt_leg]]` row `loop guard fixtures` in
`tools/govkit/registry.toml`, whose text names "the policy command" plants; the `[[usage]]` rows of
`tools/govkit/usage.toml`, since no verb or flag moves; the kickoff manifest and the gate-leg manifest,
which name none of the four files' symbols. The plant spells no install prefix: it reaches the kit through
`KIT`.

## 6. Acceptance criteria

- **AC1** — When `python tools/loop/guard.py --fixture --plant write-guarded-rollback` runs, its scenario
  `record refused over a prior file` prints `held`: the record's error reached the caller, the policy
  file's bytes equal the committed bytes, the spy saw two renames onto it, and no `policy.toml.*.tmp`
  sibling remains.
  Red when: the write or the restore goes to the target in place, as at HEAD, so the spy sees no rename.
- **AC2** — When the same command runs, its scenario `record refused, no prior file` prints `held`: the
  target does not exist, the spy saw one rename onto it, and no temp sibling remains.
  Red when: the restore leaves the renamed file or a temp file behind.
- **AC3** — When the same command runs, its scenario `interrupted at the rename` prints `held`: the
  planted `KeyboardInterrupt` reached the caller, the policy file holds its committed bytes, and no temp
  sibling remains.
  Red when: the new text reaches the target before the rename, as at HEAD, where no rename is called and
  the write lands.
- **AC4** — When the same command runs, its scenario `a callable over its prior bytes` prints `held`: the
  policy file is the committed bytes plus the appended line, the callable was handed a sibling path and not
  the target, and no temp sibling remains.
  Red when: the callable is handed the target, as at HEAD, or an empty temp, so the prior bytes are lost.
- **AC5** — When `awk '/^# >>> guarded_write_py/,/^# <<< guarded_write_py/'` runs over
  `tools/lib/guarded_write.py`, `tools/loop/policy_edit.py` and `tools/playbook/instructions_edit.py`,
  carriage returns dropped, the three outputs are identical and each holds `os.replace`.
  Red when: one copy keeps the in-place write.
- **AC6** — When `python tools/playbook/overlay.py --fixture --plant write-then-render` runs, it exits 0:
  the overlay row written through `instructions_edit.py`'s copy, by the callable form, is in the render.
  Red when: the callable writes a path the rename never moves onto the overlay file.

## 7. Gates

`python resolver (behaviour + inline parity + idiom ban)` · `loop guard fixtures` · `instruction edits selftest` · `playbook render selftest` · `govkit acceptance matrix` · `codebase-map coverage + freshness` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/loop/guard.py · covers AC1 AC2 AC3 AC4 · the `write-guarded-rollback` plant run over HEAD's in-place write, where the spy sees no rename · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** RESOLVED (agent, 2026-10-24,
  delegated): `**Derived:** PLAY-dClosedLoop-2`, rung 3, as `TOOL-dDeclaredLoop-36` §8 F1 records.
  widens: none · relaxes: none
- **F2 — Which temp file does the guarded write rename?**
  - (a) An unpredictable `<name>.<random>.tmp` through `tempfile.mkstemp`, exclusive and owner-only, the
    shape of `tools/run-gates/held_halves.py#write_replace`.
  - (b) A fixed `<name>.<suffix>` sibling, the shape of `tools/govkit/upgrade_steps.py#write_atomic`,
    which rev-2 named.
  Recommendation: (a). The policy file is the one file the guard keeps agents from; a fixed sibling is a
  name an agent can plant as a link, and the rename would then move that link into the policy file's
  place. The cost is the owner-only mode on POSIX, which git does not record. The body is written on (a).
  RESOLVED (agent, 2026-11-15, delegated): (a), rung 3: a fixed sibling name is one an agent can plant as a link
  widens: none · relaxes: none
- **F3 — Does this unit extract one temp-replace factory across kits?**
  - (a) No: the shape lives in the `guarded_write_py` block, whose copies one parity row already holds,
    and the cross-kit extraction is filed as an ask at the close.
  - (b) Yes: a `tools/lib/` canonical with its own parity row, carried by `held_halves.py` and by the
    guarded-write block.
  Recommendation: (a). `write_replace` is the kind's first instance, so this block is its second, and the
  charter's reuse rule asks for the factory; but (b) is a second mechanism in a third kit, a separate
  unit by the build method's M2, and this re-ground adds none. The body is written on (a).
  RESOLVED (agent, 2026-11-15, delegated): (a), rung 3: a shared writer across kits is a second mechanism, filed as an ask at the close
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, promoted from the round-1 spec audit's id 49 (HIGH, item H15).
- rev-2 · 2026-10-24 · §3 · the Edges block gains the hands-off bullets mirroring the
  consumes-from edges of TOOL-dDeclaredLoop-67, written by the round-2 spec audit's disposal; nothing else moved.
- rev-3 · 2026-11-15 · §1 · S1 S2 S3 S4 S5 · §3 · §4 · §5 · AC1 AC2 AC3 AC4 AC5 AC6 · §7 · §8 F2 F3 · §10 ·
  re-grounded over HEAD after TOOL-dDeclaredLoop-2 landed the three-argument `write_guarded` with its
  prior-bytes restore: the two-path design leaves, rev-2's S1 and S3 restore leave scope as built, the
  write, the restore and a callable's write move onto a sibling-temp rename, the plant moves to an
  in-process spy since a read-only directory does not fail a write on win32, and the `write_atomic`
  citation moves to `tools/govkit/upgrade_steps.py`; per the re-ground brief
  `2026-11-15-prompt-TOOL-dDeclaredLoop-43-reground-brief`.

## 10. Reuse audit

The seam is `tools/run-gates/held_halves.py#write_replace`, whose unpredictable sibling-temp replace this
unit carries into the guarded-write block, and the block's own `guarded_write_py` parity row in
`tools/lib/resolve-python.test.sh`, which holds the copies. `python tools/codebase-map/reuse_lookup.py
"write a file through a temp file beside it and rename it over the target"` ranked `write`, `write_text`,
`write_change` and `write_record`, none of which renames over its target; the recall query returned this
spec, `TOOL-dRedressedBar-21`'s spec, which introduced `write_replace` with the planted-link reason, and
`TOOL-dRedressedBar-14`'s receipt writes through `write_atomic`. Stale beside the code: rev-2 cited
`write_atomic` at `tools/govkit/govkit.py`, which no longer holds it.

Recall terms used: write_replace write_atomic sibling temp os.replace mkstemp planted link guarded write rollback prior bytes
