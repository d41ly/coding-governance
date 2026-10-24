# TOOL-dDeclaredLoop-73 — the claimed-requires refusal grades each kit's `requires` at the vintage `update --to` installs

**Status:** OPEN · rev-1 · 2026-10-24 · node d · Tier-2 · base ed497191 · streams tooling · order 5 · advances TOOL-dDeclaredLoop-35

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-TOOL-dDeclaredLoop-68-promoted-fix-return.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-68-promoted-fix-return.md) | research | TOOL-dDeclaredLoop-68 TOOL-dDeclaredLoop-69 TOOL-dDeclaredLoop-70 TOOL-dDeclaredLoop-71 TOOL-dDeclaredLoop-72 TOOL-dDeclaredLoop-74 TOOL-dDeclaredLoop-75 |
| [2026-10-24-build-TOOL-dDeclaredLoop-73-deviation-731.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-73-deviation-731.md) | deviation | — |
| [2026-10-24-prompt-TOOL-dDeclaredLoop-68-promoted-fix-brief.md](../prompts/2026-10-24-prompt-TOOL-dDeclaredLoop-68-promoted-fix-brief.md) | research | TOOL-dDeclaredLoop-68 TOOL-dDeclaredLoop-69 TOOL-dDeclaredLoop-70 TOOL-dDeclaredLoop-71 TOOL-dDeclaredLoop-72 TOOL-dDeclaredLoop-74 TOOL-dDeclaredLoop-75 |

<!-- /gen:spec-records -->

## 1. Goal

The round-3 spec audit (`memory/builds/dDeclaredLoop/reviews/2026-10-24-review-TOOL-dDeclaredLoop-57-spec-audit.md`)
confirmed finding **id 39 at HIGH**, its item **H6**, alone in that item. `TOOL-dDeclaredLoop-57`'s
`demand_claimed_requires` is passed the `descs` `cmd_update` builds with `read_descriptors(root, reg, r)`
(`tools/govkit/govkit.py:9164`), which reads each descriptor from the working tree (:13238-13252), while
`to_commit` is any commit `--to` names (:9178-9182). When `--to` names a fetched tip whose roles kit
requires loop and the working tree's does not, the refusal does not fire and the roles-without-loop
install 57 exists to stop goes through; the reverse refuses an update to a vintage that needs no loop.
57's AC1 and AC4 pass `--to <this unit's commit>`, which equals the working tree, so neither sees it.

This unit makes the refusal read each kit's `requires` at `to_commit`, as `derive_default_gained` reads
the registry there through `blob_at`. It repairs `TOOL-dDeclaredLoop-57`.

## 2. Scope (IN)

- **S1** — `read_requires_at(root, commit, descs)` in `tools/govkit/govkit.py` returns, for each kit of
  `descs`, the `requires` list of its descriptor blob at `commit`, read through `blob_at`
  (`tools/govkit/govkit.py:6706`) at the descriptor path `descs` already carries. Observed by AC1, AC2.
- **S2** — `demand_claimed_requires` grades `derive_unsatisfied_requires` over descriptors whose
  `requires` is S1's answer at `to_commit`, never the working tree's. The predicate itself is unchanged;
  only the `requires` it reads moves to the installed vintage. Observed by AC1, AC2.
- **S3** — A kit whose descriptor does not resolve or does not parse at `to_commit` has unknown
  `requires`, and the refusal names it, `'<kit>' requires are unknown at <commit8>: <reason>`, rather
  than grading it as requiring nothing. Observed by AC3.
- **S4** — The fixture pair joins the arm 57 declares in `tools/govkit/selftest.py`: a gov repository
  with two commits, at one of which the roles descriptor requires loop and at the other not, the working
  tree checked out at the first and `--to` naming the second, then the reverse. Observed by AC1, AC2.

## 3. Non-goals (OUT)

- Which kits' edges are graded, claimed plus gained or only edges the update introduces: the audit's
  id 36, batched into `TOOL-dDeclaredLoop-75`.
- `read_descriptors` for every other use in `cmd_update`: unchanged; this unit moves only the `requires`
  the refusal grades.
- A checklist entry that every check on `update --to` reads at `to_commit`, the finding's left-shift: the
  class is recorded at the close; S4 is this check's differing-vintage fixture.

### Edges

- **consumes-from** `TOOL-dDeclaredLoop-57` — `demand_claimed_requires` and its call in `cmd_update`, whose `requires` this unit reads at `to_commit`
- **hands-off** `TOOL-dDeclaredLoop-75` — the vintage-correct refusal, which that unit scopes to the edges an update introduces, names every pair in its route and observes on the write path (ids 11, 36, 40)

## 4. Design

### Evidence

- `descs[eid] = (resolve_descriptor_paths(load_toml(p), tr), dpath)` with `p = root / dpath`
  (`tools/govkit/govkit.py:13248-13252`): the working tree, and `dpath` repo-relative.
- `to_commit` is `git rev-parse --verify <to_rev>^{commit}` (:9178-9182), any commit of the gov checkout.
- `derive_default_gained` reads the registry at both vintages with `blob_at` and parses with `tomllib`
  (:976-1005); `blob_at` reads `git show <commit>:<path>` and answers `None` on a miss (:6706-6715).

### The read

```python
def read_requires_at(root, commit, descs):
    out, unknown = {}, {}
    for eid, (_desc, dpath) in descs.items():
        blob = blob_at(root, commit, dpath)
        if blob is None:
            unknown[eid] = f"{dpath} does not resolve"; continue
        try:
            out[eid] = list(tomllib.loads(blob.decode("utf-8")).get("requires") or [])
        except (tomllib.TOMLDecodeError, UnicodeDecodeError) as e:
            unknown[eid] = f"{dpath} does not parse ({e})"
    return out, unknown
```

`demand_claimed_requires` grades the selection over `{eid: ({"requires": out[eid]}, dpath)}` and refuses
first on any selected kit in `unknown`.

### Files touched (estimate)

- `tools/govkit/govkit.py`
- `tools/govkit/selftest.py`

### Alternatives rejected

- **Re-reading every descriptor at `to_commit` for the whole update.** It moves paths and adopters' reads
  this finding does not name; the refusal's input is the only one it does.
- **Refusing a `--to` that differs from the working tree.** `update --to <fetched tip>` is the documented
  route; refusing it removes the feature to dodge the defect.

## 5. Production-readiness checklist

- security — a refusal before any write, now against the bytes that would be installed.
- perf / scale — one `git show` per claimed or gained kit, a dozen.
- error / empty / loading states — S3 names an unknown vintage; an empty selection passes.
- observability — the refusal names the kit, the dependency and the vintage it read.
- risks — a descriptor renamed between vintages reads unknown at `to_commit` and refuses by name; the
  route is an `--to` that carries it.
- testing — AC1 to AC3 as fixture probes; the arm under §7, observed at the close.
- migration — none.
- user docs — none: `help/` holds no page for govkit's update refusals.

## 6. Acceptance criteria

- **AC1** — When a probe builds a scratch gov repository whose roles descriptor requires loop only at
  commit B, checks out commit A, applies roles into a scratch target and runs
  `python tools/govkit/govkit.py update --to B`, it refuses naming `'roles' requires 'loop'`.
  Red when: the refusal reads the working tree's descriptor at A and the update proceeds.
  fixture: two scratch repositories under a short `%TEMP%` path, made by the probe.
- **AC2** — When the same probe checks out B and runs `update --to A`, no requires refusal is printed.
  Red when: the working tree's newer edge refuses an older vintage that needs no loop.
- **AC3** — When a probe imports `govkit` and calls `read_requires_at` at a commit where the roles
  descriptor path does not exist, `roles` is in the second mapping with `does not resolve`, and
  `demand_claimed_requires` raises `Refusal` naming `requires are unknown`.
  Red when: an absent descriptor reads as requiring nothing.

## 7. Gates

`govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `recall floor arms` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/govkit/selftest.py · covers AC1 AC2 AC3 · the two differing vintages each way and an absent descriptor, staged against TOOL-dDeclaredLoop-57's working-tree read · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** RESOLVED (agent, 2026-10-24,
  delegated): `**Derived:** PLAY-dClosedLoop-2`, rung 3, as `TOOL-dDeclaredLoop-36` §8 F1 records.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, promoted from the round-3 spec audit's id 39 (HIGH, item H6).

## 10. Reuse audit

The seams are `blob_at` (`tools/govkit/govkit.py:6706`), the reader `derive_default_gained` already uses
for the same vintage, and the one predicate `derive_unsatisfied_requires` (:950), whose input alone moves.
`python tools/codebase-map/reuse_lookup.py "read a kit descriptor at a recorded commit"` ranked `read`,
`read_text`, `records`, `kit_rel` and `resolve_kit_dir`, none of which reads a blob at a commit; `blob_at`
was found by reading `derive_default_gained`, and agrees with source.

Recall terms used: govkit update to_commit blob_at descriptor requires vintage working tree demand_claimed_requires refusal roles loop
