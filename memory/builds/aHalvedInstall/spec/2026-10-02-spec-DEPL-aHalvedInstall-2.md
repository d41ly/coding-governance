# DEPL-aHalvedInstall-2 — selfcheck refuses a hole discharge that exits 0 on an empty tree

**Status:** CLOSED · rev-1 · 2026-10-02 · node a · Tier-1 · base cd90f7fa · streams deployer · order 2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-02-build-DEPL-aHalvedInstall-2-1-acceptance-ledger.md](../build/2026-10-02-build-DEPL-aHalvedInstall-2-1-acceptance-ledger.md) | journal | — |
| [2026-10-02-prompt-DEPL-aHalvedInstall-2-2-build-brief.md](../prompts/2026-10-02-prompt-DEPL-aHalvedInstall-2-2-build-brief.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

A hole's discharge probe answers "is this hole discharged here". A probe written as a refutation —
`! grep <bad value> <file>` — exits 0 when the file or the key is not there at all, so it reports
discharged for exactly the target it was meant to catch. Two shipped holes have that shape:
`keepalive-tool-names` passes when `RESUME_SCHEDULE_CREATE` and `_DELETE` are absent, and
`playbook-placeholders` passes when the charter file is missing. This unit gives selfcheck check 6 a
liveness arm that runs every hole's probe in an EMPTY directory and refuses one that exits 0 there,
and fixes the two probes it reds.

## 2. Scope (IN)

- **S1** — Check 6 in `tools/govkit/govkit.py` runs each hole's discharge, its tokens resolved
  through `canonical_ctx` and every token that context lacks resolved to its own name, with an empty
  temporary directory as its working directory. Exit 0 is a finding naming the entry, the hole and
  the probe. A probe that cannot launch is NOT a finding: it did not report discharged. The arm notes
  how many probes it ran and how many exited non-zero. Observed by AC1 and AC2.
- **S2** — `keepalive-tool-names` in `tools/unattended/kit.toml` is narrowed to the conditional pair
  DEPL-aHalvedInstall-1 leaves it, and asserts presence: unless `RESUME_SCHEDULE="off"`, each of
  `RESUME_SCHEDULE_CREATE` and `RESUME_SCHEDULE_DELETE` is assigned a non-empty value not wrapped in
  `<` and `>`. Its `why` is rewritten to say so, and to name that the unconditional keepalive keys are
  read by govkit's required-key reader. Observed by AC3.
- **S3** — `playbook-placeholders` in `tools/govkit/entries/playbook.kit.toml` asserts the charter
  file exists before it refutes a placeholder in it. Observed by AC4.
- **S4** — The version of every kit whose shipped bytes move is bumped where `govkit epoch` names it.
  Observed by AC5.

## 3. Non-goals (OUT)

- Probes that need a populated tree to run at all, such as `python {kit}/lexicon.py`, are not
  rewritten: in an empty directory they fail to launch their script, which is a non-zero exit and
  not a vacuous pass.
- No waiver syntax. A hole whose correct answer is "discharged when absent" does not exist today;
  the arm's header says that is the case it does not admit.

### Edges

- **consumes-from** `DEPL-aHalvedInstall-1` — the keepalive keys leave this hole because that unit
  reads them generically; without it, narrowing S2 would drop coverage.

## 4. Design

### Evidence

Read at base `cd90f7fa`. Of the 20 declared holes, two discharges are a negated grep and both exit 0
with no file present: `keepalive-tool-names` and `playbook-placeholders`. `memory-tree-taxonomy` is
also negated, but over a `diff` of two greps, which compares equal on an empty tree and so exits 1.

### Data model

```bash
# keepalive-tool-names, narrowed
grep -qE '^RESUME_SCHEDULE="?off"?$' .unattended.conf || { for k in RESUME_SCHEDULE_CREATE RESUME_SCHEDULE_DELETE; do grep -qE "^${k}=\"[^<\"][^\"]*\"" .unattended.conf || exit 1; done; }
# playbook-placeholders
test -f "$1" && ! grep -qE '\{\{[A-Z]' "$1"
```

### Files touched (estimate)

- `tools/govkit/govkit.py`
- `tools/unattended/kit.toml`
- `tools/govkit/entries/playbook.kit.toml`

### Alternatives rejected

- **Banning `! grep` by pattern.** A text rule misses every other shape that passes on absence — an
  `|| true`, a `for` over an empty glob — and refuses a correct guarded negation. Running the probe
  is the measurement; reading it is a guess.

## 5. Production-readiness checklist

- security — the probes are gov's own descriptor text, run in a fresh temp dir.
- perf / scale — one subprocess per hole, about twenty, on selfcheck only.
- error / empty / loading states — a probe that cannot launch is counted, not refused.
- observability — the note line prints probes run and probes refused.
- risks — a probe reaching outside its cwd could pass on gov's tree; every token resolves relative.
- testing — the arm is observed red on base's two probes before they are fixed.
- migration — none.
- user docs — N/A.

## 6. Acceptance criteria

- **AC1** — When `python tools/govkit/govkit.py selfcheck` runs with the two probes at base text, it
  names `keepalive-tool-names` and `playbook-placeholders` as exiting 0 on an empty tree.
  Red when: the arm runs the probe in the gov checkout instead of an empty directory.
- **AC2** — When `python tools/govkit/govkit.py selfcheck` runs after S2 and S3, no hole is named and the note counts every declared hole.
  Red when: a probe is skipped rather than run, so the count falls short.
- **AC3** — When the narrowed probe runs over a conf with `RESUME_SCHEDULE_CREATE` absent it exits 1;
  with both set to real names, or with `RESUME_SCHEDULE="off"` and neither set, it exits 0; with
  either set to `"<your-durable-schedule-create-tool>"` it exits 1.
  Red when: the probe keeps its base text, which exits 0 on the absent case.
- **AC4** — When the playbook probe runs with no charter file it exits non-zero.
  Red when: the `test -f` conjunct is dropped.
- **AC5** — When `python tools/govkit/govkit.py epoch` runs at the pass's commit, it reports no
  unbumped move.
  Red when: a touched kit's version marker is left.

## 7. Gates

`govkit selfcheck` · `kit epoch (shipped bytes move, the version moves)` · `govkit selftest` · `govkit refusal join` · `recall floor arms` · `govkit acceptance matrix`

New arm: tools/govkit/govkit.py · the base text of either probe · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-02 · initial draft, from the owner's first observation and the hole set at base.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "a hole discharge probe that passes when its subject is absent"`
ranked name-stem neighbours only and printed `unscanned layers: .sh`. The seams extended are
selfcheck check 6, which already walks every hole, `canonical_ctx` for token resolution, and
`resolve_shell_argv`, which `check` already runs every probe through. No existing arm runs a probe
in selfcheck.

Recall terms used: govkit update conflict rollback regenerate rendered vintage stale partial install hole discharge absent key

The question passed with them: "why does govkit update leave a kit half-installed when one row conflicts, and why does a renderer change roll back a kit".
