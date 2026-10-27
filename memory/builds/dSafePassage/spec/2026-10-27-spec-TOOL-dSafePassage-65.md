# TOOL-dSafePassage-65 — `update` resolves a row's role from the descriptor at `--to`, not from the gov checkout's working tree

**Status:** DEFERRED · rev-1 · 2026-10-27 · node d · Tier-2 · base 60d90cb7 · streams tooling · order 5 · advances TOOL-dSafePassage-14

**Derived:** TOOL-dSafePassage-5

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-27-prompt-TOOL-dSafePassage-65-build-brief.md](../prompts/2026-10-27-prompt-TOOL-dSafePassage-65-build-brief.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

TOOL-dSafePassage-5's fourth build pass (HEAD `98a01d518`) rolled a walked release-0 tree back to
the pin with the gov clone checked out at its tip, where the `withdraw-one` gov plant drops
`tools/hooks/README.md`'s rule. The row stayed `retired-edited`, where release-0 recorded `engine`,
so TOOL-dSafePassage-64's return never fired. The same tree rolled back with the clone at HEAD and no
gov plant matched release-0 exactly.

The cause is a split vintage inside one run. `_cmd_update` reads every descriptor from the checkout's
working tree (`read_descriptors(root, reg, r)` at `tools/govkit/govkit.py:9521`, which loads
`root / dpath` at `:13873-13877`) and resolves each row's role there (`:10143-10151`). Gov's bytes
come from `--to` (`blob_at(root, to_commit, src)`, `:9127`). The records promise `--to`'s vintage:
a rollback returns the files "to `<rev>`'s bytes as any `update --to <rev>` moves them"
(`help/upgrade-steps.md:206-207`), and DEPL-dGaugedVintage-9 S1 resolves through `to_commit`
"rather than through `HEAD`". This unit makes the role re-resolution read the descriptor at `--to`.

## 2. Scope (IN)

- **S1** — The descriptor at a commit. `read_descriptor_at(root, commit, dpath)` in
  `tools/govkit/govkit.py` returns the descriptor blob at `commit` through `blob_at` (`:6857`),
  parsed with `tomllib` and joined by `resolve_descriptor_paths` over `derive_tool_root(root)`, as
  `read_descriptors` joins the working tree's (`:13866`, `:13877`). It returns `None` when the blob is
  absent. Observed by AC1.
- **S2** — The pool at a commit. `tracked`, `resolve_rule_pool`, `expand_rules` and `resolve_entry`
  take an optional `at`, default `None`, which reads as today. With `at` set, `tracked` lists
  `git ls-tree -r --name-only -z <at>` in place of `ls-files` (`:333-334`), so a `**` rule pools the
  files gov tracks at that commit (`:6815-6819`). No other caller passes it. Observed by AC1.
- **S3** — The re-resolution. Where `to_commit` differs from the checkout's `HEAD`, `_cmd_update`'s
  role re-resolution (`:10143-10151`) resolves each kit through `resolve_entry(root,
  read_descriptor_at(root, to_commit, dpath), ctx, at=to_commit)`. A kit whose descriptor is absent at
  `to_commit`, one gained after it, keeps the working tree's resolution, as today. TOOL-dSafePassage-64's
  return and the role-move branch then read `now` from that resolution. Observed by AC1.
- **S4** — The docs. The "Rolling back" section of `help/upgrade-steps.md` says each file is graded
  under the role `<rev>`'s descriptor gives it. Observed by AC2.

## 3. Non-goals (OUT)

- The other descriptor reads of `_cmd_update`: the registry (`:9520-9521`), the succession rows
  (`read_retired(root, None, None)`, `:9657`), the default-gained `requires`, which
  TOOL-dDeclaredLoop-73 moves, and the landing loop's resolution (`:11532`). Reading the registry at
  `<rev>` would refuse a rollback over a kit gained after it: a claimed id with no succession row is
  `resolve_claim`'s refusal (`:9653-9654`, `:9660`), and the docs keep such a kit claimed
  (`help/upgrade-steps.md:235-236`). No measurement shows another read moving a byte.
- A run whose `--to` is the checkout's `HEAD`, an uncommitted descriptor edit included: read as today.
- Refusing a `--to` other than `HEAD`. `TOOL-dDeclaredLoop-73` §4 rejects it: `update --to <fetched
  tip>` is the documented route.
- The upgrade-walk leg and its `down` case, which TOOL-dSafePassage-5 owns.

### Edges

- **hands-off** `TOOL-dSafePassage-5` — the `down` and `reup` cases over the `withdraw-one` gov plants, whose rollback to the pin resolves `tools/hooks/README.md` at the pin as `engine`, so the row returns to that role

Read and closed, so named here rather than joined: TOOL-dSafePassage-64's return, which this unit
feeds a `now` from `--to`, and TOOL-dSafePassage-4's `update --rollback`.

## 4. Design

### Why the role stayed

At the rollback the row reads `retired-edited` and `--to` is the pin. The re-resolution resolves the
working tree, the tip, where the `withdraw-one` plant removed the rule and its source, so the hooks
kit names no role for the path and `now` is `None` (`:10150-10151`). TOOL-dSafePassage-64's return
needs a `now` (`:10159-10162`), so the row is dispatched as `retired-edited` again. Resolved at the
pin, the rule ships the path as `engine`, the return fires, and the grid grades the row from its kept
`commit` and `gov_oid` as `patched`, as TOOL-dSafePassage-64 §4 reasons.

A rollback cannot be run from a checkout at `<rev>` instead. govkit's root is the checkout its own
file lives in (`repo_root`, `:153`), and the pin's `tools/govkit/govkit.py` carries no `--rollback`
(`git show 60d90cb7:tools/govkit/govkit.py`, zero matches), so a release-0 adopter's rollback is
always run by a later govkit with a later working tree.

### The read

```
role re-resolution, per kit, memoised in _role_res:
  if to_commit != HEAD and (d_at := read_descriptor_at(root, to_commit, dpath)) is not None:
      res = resolve_entry(root, d_at, ctx, at=to_commit)
  else:
      res = resolve_entry(root, d, ctx)                  # today
```

`ctx` is `target_context(target, deploy, kit, d_at or d)`, read from the target as today. A blob
that does not parse raises the `Refusal` `load_toml` raises for the working tree's (`:343-345`),
naming the path and the commit.

### Inventory

Minted: the function `read_descriptor_at` (`python tools/lexicon/lexicon.py --suggest
read_descriptor_at --as py.function`, OK, 2026-10-27); the keyword `at` on `tracked`,
`resolve_rule_pool`, `expand_rules` and `resolve_entry`; the fixture plant `edited-rolled-back` in
`tools/govkit/fixtures/retired_edits.py`. No verdict, role, conf key, gate leg or receipt field.

### Migration

None. A receipt is read as before; a rollback's roles come from `<rev>` from the first run after
landing.

### Rollout

Live at landing, in order 5 beside TOOL-dSafePassage-5, which consumes it and builds after it.

### Files touched (estimate)

- `tools/govkit/govkit.py`
- `tools/govkit/fixtures/retired_edits.py`
- `tools/govkit/selftest.py`
- `help/upgrade-steps.md`

### Alternatives rejected

- **Check the gov clone out at the pin for each `down` in TOOL-dSafePassage-5.** The pin's govkit has
  no `--rollback`, and the root is the running file's checkout, so no adopter can roll back that way.
- **Leave the code and change TOOL-dSafePassage-5's expectation.** Release-0's receipt is what a
  rollback promises, and no record declares a row's role re-derived per run; a defect is not a
  normalization (TOOL-dSafePassage-64 §4 "### Alternatives rejected").
- **Every descriptor read of `_cmd_update` at `--to`.** §3's first bullet.
- **A scratch `git worktree` of `to_commit` as the resolution root.** It registers a worktree in
  gov's own repository on every rollback, and a killed run leaves it behind; S2 reads the same tree
  and writes nothing.
- **Resolve at `to_commit` even when it is `HEAD`.** It moves every run over an uncommitted
  descriptor edit in gov's checkout, which nothing measured asks for (§8 F1).

## 5. Production-readiness checklist

- security: reads only; `blob_at` and `ls-tree` over gov's own repository, no new write path.
- perf / scale: one `git show` per claimed kit and one `ls-tree` per rollback, memoised as
  `_role_res` already is.
- error / empty / loading states: a descriptor absent at `--to` keeps today's resolution; one that
  does not parse refuses by name.
- observability: a row's verdict line prints under the role `--to` gives it.
- risks: a rollback across a descriptor's role move now reports that row `role-moved` and stands back
  (DEPL-cMendedVintage-19 S2), where the working tree agreed with the receipt; it writes nothing for
  that row. HEAD's code parses an older descriptor, as `derive_default_gained` already does for the
  registry (`:1034`).
- testing: the `edited-rolled-back` plant through the arm of §7.
- migration: none.
- user docs: `help/upgrade-steps.md` (S4).

## 6. Acceptance criteria

- **AC1** — When `python "tools/govkit/fixtures/retired_edits.py" --plant edited-rolled-back` runs,
  it exits 0. The `edited-gone` setup's first `update --write` reads `retired-edited` and is
  committed with its order cleared; then, with the scratch gov's working tree still at B,
  `update --rollback --to <A> --write` prints the verdict `patched`, the receipt role reads `engine`,
  no `update-retired-edited-` order is written, and the edited bytes are kept.
  Red when: the re-resolution reads the working tree at B, which pools no `gone.txt`, so the role
  stays `retired-edited` and the rollback writes an order.
- **AC2** — When `git grep -n -e "descriptor gives it" -- help/upgrade-steps.md` runs, it prints the
  section's sentence, and `python "tools/govkit/docs_leg.py"` exits 0.
  Red when: the page names no vintage for a rolled-back file's role.

## 7. Gates

`govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `govkit selfcheck` · `recall floor arms` · `policy fixtures` · `encoding posture (text IO names its encoding)` · `lexicon naming predicates` · `docs` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/govkit/selftest.py · covers AC1 · the `_rte_cases` rows (`tools/govkit/selftest.py:18329-18340`) gain `edited-rolled-back`, its failing case staged by the re-resolution reading the working tree in a working copy · none

## 8. Open questions

- **F1 — When the re-resolution reads `--to`.** Options: (a) only where `to_commit` differs from the
  checkout's `HEAD`; (b) on every run. (b) moves runs whose `--to` is `HEAD` over an uncommitted
  descriptor edit, a change no measurement or record asks for. RESOLVED (agent, 2026-10-27,
  delegated): (a), rung 1, the charter's `[yagni]` and `[small]` over the measured defect, which is a
  rollback. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, from TOOL-dSafePassage-5's fourth build-pass measurement of a
  rollback to the pin leaving the `withdraw-one` row `retired-edited`, by
  `2026-10-27-prompt-TOOL-dSafePassage-5-8-spec-writer.md`.

## 10. Reuse audit

The seam extended is `resolve_entry` and its pool (`tools/govkit/govkit.py:510`, `:482`, `:6798`,
`:333`), given a commit as `resolve_entry_version_at` (`:754`) and `derive_default_gained` (`:1034`)
already read gov at `to_commit` through `blob_at`. `python tools/codebase-map/reuse_lookup.py
"resolve a kit descriptor and its rule pool at a gov commit rather than the working tree"` ranked
`resolve`, `resolve_kit_dir`, `resolve_prefix_token` and `resolve_entry` among its seams:
`resolve_entry` is the resolver this unit extends, and none of the others reads a descriptor at a
commit. The recall probe found TOOL-dDeclaredLoop-73, which moves the claimed-requires refusal to
`to_commit` with `blob_at` and leaves every other read, and its audit finding H6 naming this split.
Line numbers are read at `98a01d518`.

Recall terms used: `python tools/memory-recall/query.py "does update read gov's descriptors at the --to revision or from the gov checkout's working tree" --terms "update --to working tree descriptor read_descriptors resolve_entry to_commit vintage rollback role re-resolution blob_at"`
