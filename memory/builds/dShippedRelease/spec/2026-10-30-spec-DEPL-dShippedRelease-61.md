# DEPL-dShippedRelease-61 — gov's own harnesses declare `install.from`, so the default refuses no suite once a tag exists

**Status:** OPEN · rev-1 · 2026-10-30 · node d · Tier-2 · base f4597719 · streams deployer · order 19 · advances DEPL-dShippedRelease-32

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md](../build/2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md) | journal | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 DEPL-dShippedRelease-49 DEPL-dShippedRelease-50 DEPL-dShippedRelease-51 DEPL-dShippedRelease-52 DEPL-dShippedRelease-53 DEPL-dShippedRelease-54 DEPL-dShippedRelease-55 DEPL-dShippedRelease-56 DEPL-dShippedRelease-57 DEPL-dShippedRelease-58 DEPL-dShippedRelease-59 DEPL-dShippedRelease-60 DEPL-dShippedRelease-62 DEPL-dShippedRelease-63 DEPL-dShippedRelease-64 DEPL-dShippedRelease-65 DEPL-dShippedRelease-66 DEPL-dShippedRelease-67 DEPL-dShippedRelease-68 DEPL-dShippedRelease-69 DEPL-dShippedRelease-70 DEPL-dShippedRelease-71 DEPL-dShippedRelease-72 DEPL-dShippedRelease-73 DEPL-dShippedRelease-74 DEPL-dShippedRelease-75 DEPL-dShippedRelease-76 DEPL-dShippedRelease-77 DEPL-dShippedRelease-78 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 6 of `reviews/2026-10-30-review-DEPL-dShippedRelease-1-spec-audit-round1.md`, HIGH,
item H6. Unit 25 S3 reads `install.from` from the target, scratch targets hold no policy file, and
the default `release-tag` then refuses an `apply` from any untagged commit once one `gov/v*` tag
exists. Every landing's prepared merge is untagged and unit 3 cuts tags weekly, so from the first
cut the bar is red on every landing. The refusal stays for every target; the harnesses say what they
mean.

## 2. Scope (IN)

- **S1** — The override. `read_install_from(target)` in `tools/govkit/govkit.py` answers
  `GOVKIT_INSTALL_FROM` when that variable is set to an allowed value of the row, and otherwise the
  literal `read_policy_value("install.from", target)`. A set value prints
  `install.from — <value> by GOVKIT_INSTALL_FROM` on every use, so it is never silent. Unit 25 S3
  reads through it, and no target, mode or checkout is exempted by name. Observed by AC1, AC2.
- **S2** — The harnesses. Each module that spawns the deployer from a gov checkout assigns
  `GOVKIT_INSTALL_FROM=any-commit` once, for its own children: `tools/govkit/selftest.py`,
  `tools/govkit/matrix.py` and `tools/policy/check_policy.py`, and each other file the census of §4
  prints at the pass. The disposition is named here because a future `apply` spawn reads the
  refusal, loud and by name. Observed by AC3.
- **S3** — The fixture. `--case tagged-clone` of `receipt_schema_5.py --fixture` tags a scratch
  clone behind its HEAD, unsets the variable, and reads the refusal; with the variable set the same
  `apply` exits 0. Observed by AC1, AC2.

## 3. Non-goals (OUT)

- Where the refusal sits: DEPL-dShippedRelease-62.
- A planted `.governance/policy.toml` in every harness target: §8 F1.

### Edges

- **consumes-from** `DEPL-dShippedRelease-25` — S3's read of `install.from` and the `--fixture` cases, without which there is no refusal to declare around
- **hands-off** `DEPL-dShippedRelease-62` — `read_install_from`, the read that unit's pre-write check calls

## 4. Design

### Evidence

- `tools/govkit/selftest.py:220` spawns the real GOVKIT, and report id 6 counted 85 `run("apply"` or `gov("apply"` sites; `tools/govkit/matrix.py:118` and `:409` and
  `tools/policy/check_policy.py:1168` spawn it too.
- `tools/policy/policy.py:503` reads the policy file from a commit and never opens the working tree, so a planted file needs a commit in every scratch target.
- `GOVKIT_NO_REMOTE_PROBE` and `GOVKIT_RERENDER` are this module's existing environment seams (unit 16 S1, S4).
- The census: `git grep -lE '(govkit\.py|GOVKIT)[" ,]+(apply|adopt|install)\b' -- tools .githooks`, re-run at the pass.

### Inventory

| Minted | Kind | Naming cell |
|---|---|---|
| `read_install_from` | function, `tools/govkit/govkit.py` | `py.function`, OK by `--suggest` at writing |
| `GOVKIT_INSTALL_FROM` | environment variable | none |

### Files touched (estimate)

- `tools/govkit/govkit.py`: S1
- `tools/govkit/selftest.py`, `tools/govkit/matrix.py`, `tools/policy/check_policy.py`: S2
- `tools/govkit/steps/receipt_schema_5.py`: S3
- `help/upgrade-steps.md`: the variable

## 5. Production-readiness checklist

- security — the variable selects a value the row already allows; an operator able to set it can
  already commit the same value, and every use prints.
- perf / scale — N/A — a read or a compare on a path that already runs once per landing.
- error / empty / loading states — the criteria of §6 name each refused and empty state.
- observability — each state prints the line §2 names, on green and red.
- risks — a suite the census misses reds with the refusal's own line after the first tag, which is
  loud and names the variable.
- testing — the criteria of §6 and the arm of §7.
- migration — N/A — the code it changes lands in this same build, so no installed state moves.
- user docs — `help/upgrade-steps.md` names the variable and says it is for harnesses.

## 6. Acceptance criteria

- **AC1** — When `python receipt_schema_5.py --fixture --case tagged-clone` runs with
  `GOVKIT_INSTALL_FROM` unset, `apply` at the untagged HEAD exits 2 naming the tag.
  Red when: the override hides the refusal when no one set it.
- **AC2** — When the same case runs with `GOVKIT_INSTALL_FROM=any-commit`, `apply` exits 0, prints
  `by GOVKIT_INSTALL_FROM`, and the receipt holds `install_from` `any-commit`.
  Red when: a harness cannot install from a prepared merge once a tag exists.
- **AC3** — When `git grep -c GOVKIT_INSTALL_FROM` runs over the census of §4 at the pass, each
  listed file prints at least 1.
  Red when: a harness that spawns `apply` carries no declaration, so it reds on the first tag.

## 7. Gates

`recall floor arms` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `policy fixtures` · `spec tokens (a spec's own names resolve)` · `memory hygiene`

New arm: tools/govkit/selftest.py · covers AC1 AC2 · one annotated `gov/v*` tag behind HEAD in a scratch clone, its failing case the assignment cut from `run` · none

## 8. Open questions

- **F1 — How does a harness say `any-commit`?** Options: (a) one environment variable read at one
  site; (b) a committed `.governance/policy.toml` planted in each target. (b) needs a commit in
  every scratch target, and arms that read the target's tree or its log would each move. (a) is a
  seam of the same kind as `GOVKIT_NO_REMOTE_PROBE`, and it prints on every use. RESOLVED (agent,
  2026-10-30, delegated): (a), rung 3. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-30 · initial draft, promoted from review id 6 (HIGH, item H6) of the round-1 spec audit.

## 10. Reuse audit

The seam extended is DEPL-dShippedRelease-25's S3 read, at the pass `_cmd_apply` already hoists
refusals to (`tools/govkit/govkit.py:7623`).
`python tools/codebase-map/reuse_lookup.py "strip credentials from a remote url before recording it"`
and a read of `tools/govkit/govkit.py` found no other pre-write refusal seam, and
`validate_gate_runner`'s sibling comment names the rule. The recall probe surfaced report items H6
and H7, which agree with this reading.

Recall terms used:
`python tools/memory-recall/query.py "where does an install refusal sit so that no file is written first" --terms "install.from release-tag refusal pre-write containment apply update receipt tag untagged harness"`
