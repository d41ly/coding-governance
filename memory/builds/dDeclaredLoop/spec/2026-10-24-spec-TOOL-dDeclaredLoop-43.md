# TOOL-dDeclaredLoop-43 — the guarded write restores each path's prior bytes, and writes each through a sibling temp file

**Status:** OPEN · rev-2 · 2026-10-24 · node d · Tier-2 · base ed497191 · streams tooling · order 16 · advances TOOL-dDeclaredLoop-35

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-TOOL-dDeclaredLoop-36-promoted-fix-return.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-36-promoted-fix-return.md) | research | TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 |
| [2026-10-24-build-TOOL-dDeclaredLoop-43-deviation-431.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-43-deviation-431.md) | deviation | — |
| [2026-10-24-prompt-TOOL-dDeclaredLoop-36-promoted-fix-brief.md](../prompts/2026-10-24-prompt-TOOL-dDeclaredLoop-36-promoted-fix-brief.md) | research | TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 |
| [2026-10-24-review-TOOL-dDeclaredLoop-36-spec-audit.md](../reviews/2026-10-24-review-TOOL-dDeclaredLoop-36-spec-audit.md) | spec-audit | TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit (`memory/builds/dDeclaredLoop/reviews/2026-10-24-review-TOOL-dDeclaredLoop-1-spec-audit-round1.md`)
confirmed finding **id 49 at HIGH**, its item **H15**, alone in that item. `TOOL-dDeclaredLoop-2` §4
"The factory — guarded_write.py" has `write_guarded(path, new_text, record)` "remove both when either
write fails". For an existing `.governance/policy.toml` that deletes the owner's file instead of
restoring it, and neither write is atomic against an interrupt, so a failed record write, a refused
path or a killed process leaves the policy file deleted or truncated, and every policy reader falls
back to catalogue defaults. This unit takes the report's fix. It repairs `TOOL-dDeclaredLoop-2`.

## 2. Scope (IN)

- **S1** — `write_guarded` reads, before any write, each target path's prior state: its bytes, or that
  it did not exist. Observed by AC1, AC2.
- **S2** — Each write goes through a sibling temp file in the target's own directory and `os.replace`,
  the shape of govkit's `write_atomic` (`tools/govkit/govkit.py:4198-4232`), so an interrupt mid-write
  leaves the prior file, never a truncated one. Observed by AC3.
- **S3** — On any failure of either write, each path is restored to its prior state: a path that existed
  gets its prior bytes back through the same sibling-temp replace, and only a path that did not exist
  before is deleted. The failure is then re-raised, naming the path that failed. This supersedes
  `TOOL-dDeclaredLoop-2` §4's "removes both when either write fails". Observed by AC1, AC2.
- **S4** — The change lands in the canonical `tools/lib/guarded_write.py`, and so in the
  `guarded_write_py` inline copies the parity row holds in `tools/loop/policy_edit.py` and
  `tools/playbook/instructions_edit.py`. Observed by AC4.

## 3. Non-goals (OUT)

- Crash consistency past an exception: no fsync and no directory sync, the limit govkit's
  `write_atomic` states for itself.
- The terminal proof and its win32 console test: the audit's id 21, batched into
  `TOOL-dDeclaredLoop-56`.
- A bug-class checklist entry for "rollback deletes instead of restoring", the finding's left-shift:
  the class is recorded at the close; AC1 is this instance's gate.

### Edges

- **consumes-from** `TOOL-dDeclaredLoop-2` — `write_guarded` in `tools/lib/guarded_write.py` and its two inline copies, whose rollback this unit replaces
- **hands-off** `TOOL-dDeclaredLoop-67` — the round-2 minors ids 7, 16, 20, 44 and 49: this pass keeps the loop guard fixtures leg green and the three-argument write_guarded form; the rollback fixtures inject the failure through a patched replace, scope items of that unit

## 4. Design

### Evidence

- `write_atomic` writes a sibling `<name>.govkit-new` and `os.replace`s it, and its docstring states why
  the temp file is a sibling: `os.replace` raises across a filesystem boundary
  (`tools/govkit/govkit.py:4198-4232`).
- The policy file is the owner's guarded file; its loss is silent, because every reader falls back to
  the catalogue default (`TOOL-dDeclaredLoop-2` §4 "Data model").

### The write

```python
def write_guarded(path, new_text, record_path, record_text):
    prior = {p: (p.read_bytes() if p.exists() else None) for p in (path, record_path)}
    done = []
    try:
        for p, text in ((path, new_text), (record_path, record_text)):
            write_via_sibling(p, text.encode("utf-8"))
            done.append(p)
    except BaseException:
        for p in done:
            if prior[p] is None: p.unlink(missing_ok=True)
            else: write_via_sibling(p, prior[p])
        raise
```

`BaseException` so a `KeyboardInterrupt` between the two writes restores too.

### Files touched (estimate)

- `tools/lib/guarded_write.py`
- `tools/loop/policy_edit.py`
- `tools/playbook/instructions_edit.py`

### Alternatives rejected

- **Writing the record first, then the policy file.** It narrows the window and still leaves an orphan
  record when the second write fails; restoring prior bytes closes it.
- **Importing govkit's `write_atomic`.** govkit is copy-installed as a standalone directory and the
  inline block cannot reach it; the shape is carried, two lines.

## 5. Production-readiness checklist

- security — closes a data-loss path in the owner's guarded file.
- perf / scale — two reads of small files before writing.
- error / empty / loading states — a failure restores and re-raises naming the path; a path absent
  before is absent after.
- observability — the re-raised error names the failed path.
- risks — a restore that itself fails leaves the sibling temp file, which the next write overwrites, as
  govkit's writer does.
- testing — AC1 to AC4 as fixture probes; the arm under §7, observed at the close.
- migration — none.
- user docs — none.

## 6. Acceptance criteria

- **AC1** — When a probe plants the policy file, `policy.toml`, holding known bytes and a record path whose
  directory is read-only, and calls `write_guarded`, the call raises naming the record path and the
  policy file's bytes equal the planted bytes.
  Red when: the rollback deletes the existing policy file.
  fixture: a scratch directory under the run's scratch, with a read-only subdirectory.
- **AC2** — When the same probe starts with no policy file and calls `write_guarded`, the failed call
  leaves no policy file and no record: `os.path.exists` is false for both paths.
  Red when: a path created by the failed call survives it.
- **AC3** — When the probe makes the second `os.replace` raise `KeyboardInterrupt` through a patched
  function, the policy file holds its prior bytes and no `.govkit-new`-style sibling of it is left
  holding the new text as the file itself.
  Red when: the first write went straight to the target, so the interrupt leaves it half-updated.
- **AC4** — When the `guarded_write_py` parity extract runs over the canonical and the two copies, the
  three blocks are identical.
  Red when: one copy keeps the delete-on-failure rollback.

## 7. Gates

`python resolver (behaviour + inline parity + idiom ban)` · `playbook render selftest` · `govkit acceptance matrix` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/loop/guard.py · covers AC1 AC2 · a `write-guarded-rollback` fixture case, staged against the delete-on-failure rollback · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** RESOLVED (agent, 2026-10-24,
  delegated): `**Derived:** PLAY-dClosedLoop-2`, rung 3, as `TOOL-dDeclaredLoop-36` §8 F1 records.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, promoted from the round-1 spec audit's id 49 (HIGH, item H15).
- rev-2 · 2026-10-24 · §3 · the Edges block gains the hands-off bullets mirroring the
  consumes-from edges of TOOL-dDeclaredLoop-67, written by the round-2 spec audit's disposal; nothing else moved.

## 10. Reuse audit

The seam is govkit's `write_atomic` (`tools/govkit/govkit.py:4198`), whose sibling-temp replace this
unit carries into the guarded-write block, and the block's own `guarded_write_py` parity row, which holds
the copies. `python tools/codebase-map/reuse_lookup.py "write a file atomically and restore prior bytes
on failure"` ranked `write`, `write_text` and `write_record`, none of which restores prior bytes; `git
grep os.replace -- 'tools/*.py'` found `write_atomic` as the documented atomic writer.

Recall terms used: write_guarded rollback restore prior bytes os.replace sibling temp atomic policy.toml guarded_write_py
