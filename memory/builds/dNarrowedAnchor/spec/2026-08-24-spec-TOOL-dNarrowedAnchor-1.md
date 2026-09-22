# TOOL-dNarrowedAnchor-1 — the second anchor is admissible per MODE, and `slug` is not one of them

**Status:** INPROGRESS · rev-1 · 2026-08-25 · node d · Tier-2 · base 9ddcc5c9 · streams tooling

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

Scope `ANCHOR_SCOPE="published"` to the modes whose discipline is to author their own build folder,
so an adopter who turns the key on to enable the prompt path does not silently also let a `slug`-mode
run authorize itself. Today the key is a whole-project switch and the declared mode has no bearing on
which anchor a run may use.

## 2. Scope (IN)

- **S1 — the driver refuses.** `check_authorization` in `tools/unattended/unattended.sh` gains
  `fail 50`: a run whose BASE came from the second anchor while its build README declares (or
  defaults to) `slug` is refused. The admissible set is a kit-owned constant, `SECOND_ANCHOR_MODES`,
  not an adopter declaration.
- **S2 — the leg mirrors it.** `tools/unattended/check-unattended.sh` gains `fail 29`, deriving the
  same verdict from the RECORDED base and the advertised default-branch tip rather than from
  `anchor-kind`, which its subject writes.
- **S3 — both are armed.** New arms in `unattended.test.sh` and `check-unattended.test.sh`, each
  observed RED against the code it guards before being called green. `check-arms.py --check` is on
  the unguarded bar, so an unarmed `fail 50` reds it.
- **S4 — the carriers say so.** `PROTOCOL.template.md` §1, `SKILL.template.md`'s routing table and
  `.unattended.conf.example`'s `ANCHOR_SCOPE` comment state which modes the second anchor serves.

## 3. Non-goals (OUT)

- **No new `.unattended.conf` key.** The admissible set is kit-owned. An adopter-configurable set
  would let a project re-open exactly the hole this closes, and there is no legitimate configuration
  in which a `slug` run needs the second anchor.
- **No change to `ANCHOR_SCOPE`'s own values or default.** Blank still means the strict anchor.
- **No attempt to make `authorized-by:` trustworthy.** It is a byte the run writes, and §9 of the
  protocol already says so. This narrows WHICH declaration reaches the widened anchor; it does not
  make the declaration true. A run that wants to self-authorize can still declare `prompt`.
- **No re-pull into inCMS.** That is a second act on the adopter side, and its receipt
  (`.governance/install.index`) pins a gov commit this build has not made yet. Filed there as
  `ABL-dPublishedAnchor-1`.

## 4. Design

### Inventory

Read against source at BASE `9ddcc5c9`:

| Fact | Value | Where |
|---|---|---|
| the widening | fires only when the README misses at the merge-base | `unattended.sh:762` |
| the anchor it sets | `ANCHOR_KIND=run-branch` | `unattended.sh:773` |
| the mode | read from the blob AT BASE, so it is known only AFTER the anchor fired | `unattended.sh:1119` |
| absent `authorized-by:` | defaults to `slug` | `unattended.sh`, `check_authorization` |
| published vocabulary | `AUTH_MODES="slug prompt recipe"` | `unattended.sh:361` |
| next free driver code | `fail 50` | 1-49 in use |
| next free leg code | `fail 29` | 1-22 and 24-28 in use |

### The ordering, which is why this is checkable at all

The mode cannot select the anchor, because the mode lives in a blob the anchor has to resolve first.
So this is not a branch taken BEFORE widening — it is a refusal taken AFTER, once both facts exist:

```
resolve_base   -> ANCHOR_KIND ∈ {default-branch, run-branch}   (derived from the observation)
check_authorization -> AUTH_MODE ∈ AUTH_MODES                  (read from the blob at that base)
                    -> refuse when ANCHOR_KIND=run-branch and AUTH_MODE ∉ SECOND_ANCHOR_MODES
```

**Branching on `ANCHOR_KIND` here does not break the evidence-never-an-input rule.** That rule bans
reading the RECORDED value back out of the run-state file, which is a byte the subject wrote — the
comment on `AUTH_MODE` states it and points at `anchor-kind` for the reason. The value used here is
the one `resolve_base` just derived from the remote observation and the local history, in the same
invocation, and the driver already branches on freshly-derived `AUTH_MODE` for `recipe`.

### The leg's derivation is independent, not a copy

The leg may not read `anchor-kind` — its own source says so, and a leg reading a value its subject
writes is the class this kit has been burned by. It already holds the two facts it needs: `ADV_HEAD`,
the advertised default-branch tip, and the `authorized-by:` value at the run's recorded base. So:

- base IS an ancestor of `ADV_HEAD` → the first anchor could have produced it → nothing to say.
- base is NOT an ancestor of `ADV_HEAD`, and the declared mode is outside `SECOND_ANCHOR_MODES` →
  `fail 29`.
- `ADV_HEAD` unreadable → CANNOT TELL, and it stays silent, exactly as `is_published` does. A leg
  that reds on an unreachable remote is a leg that reds on a train.

### The close-time case, stated rather than designed around

A run can start on one anchor and close on the other: the folder reaching the default branch mid-run
moves it to the first anchor, and only the pathological reverse — the folder being DELETED from the
default branch under a live `slug` run — moves it to the second. In that reverse case this refusal
fires at `--close` on a run that preflighted cleanly. That is a wedge, and it is the correct one:
before this change the same run would have silently self-authorized off its own branch tip. The
refusal names both exits — restore the folder on the default branch, or `--abort`.

### Files touched (estimate)

| Path | Change |
|---|---|
| `tools/unattended/unattended.sh` | `SECOND_ANCHOR_MODES`; `fail 50` in `check_authorization` |
| `tools/unattended/check-unattended.sh` | `fail 29` |
| `tools/unattended/unattended.test.sh` | arms for `fail 50`, both directions |
| `tools/unattended/check-unattended.test.sh` | arms for `fail 29`, incl. the cannot-tell arm |
| `tools/unattended/PROTOCOL.template.md` | §1 states which modes the second anchor serves |
| `tools/unattended/SKILL.template.md` | the routing table's `published` precondition |
| `tools/unattended/.unattended.conf.example` | the `ANCHOR_SCOPE` comment |

### Alternatives rejected

- **A per-mode `ANCHOR_SCOPE` value** (`published:prompt`): a second grammar inside a key whose whole
  value guard is "anything unrecognised means the strict anchor", so a typo would silently narrow to
  the strict anchor and the prompt path would stop working with no message.
- **Refusing at `resolve_base`**: the mode is not known there. It would need a second blob read
  against a base not yet chosen, which is the chicken-and-egg this design routes around.
- **An adopter-declared set**: §3.
- **Leaving it and documenting it**: what inCMS already did, and the reason its charter now carries a
  paragraph about a concession it did not want. A cost that has to be written into every adopter's
  charter is a kit defect.

## 5. Production-readiness checklist

- **security** — the point. It narrows a self-authorization path from every mode to the two whose
  discipline declares it. It does not close self-authorization; §3 says so.
- **perf / scale** — N/A. One `merge-base --is-ancestor` in the leg, on a path that already runs one.
- **a11y** — N/A — no user-facing surface.
- **i18n** — N/A — no user-facing surface.
- **error / empty / loading states** — the leg's third state (CANNOT TELL) is explicit and silent, and
  it is armed, because a silent state that nothing exercises is where a check quietly stops checking.
- **observability** — both refusals name the mode, the base and both exits. `anchor-kind` continues to
  be recorded and continues to be read by nothing.
- **risks** — the close-time wedge in §4, bounded to a folder deleted from the default branch under a
  live run. Adopters on the strict anchor are unaffected: the second anchor never fires for them.
- **testing + left-shift gates** — `check-arms.py --check` is unguarded on the bar, so `fail 50`
  cannot land unarmed. The kit self-tests are off the bar by owner ruling, so they are run by hand via
  `run-unattended-gates.sh` and the result is recorded here.
- **migration / rollback** — none. No stored shape changes. Rollback is deleting one condition.
- **help/ docs** — N/A — this kit's carriers ARE its docs, and S4 updates all three.

## 6. Acceptance criteria

- **AC1** — When a build README declaring `authorized-by: slug` is resolved through the second anchor,
  `--preflight` exits non-zero naming `fail 50`, the mode and both exits. Observed.
- **AC2** — When the same README declares `prompt`, and again when it declares `recipe`, the second
  anchor is accepted and preflight proceeds. Observed for both — a refusal that fires on everything is
  not a narrowing.
- **AC3** — When a `slug` README resolves at the FIRST anchor, nothing changes: no refusal, on a
  project with `ANCHOR_SCOPE="published"` and on one without. Observed.
- **AC4** — When a run-state file records a base that is not an ancestor of the advertised
  default-branch tip and its README declares `slug`, `check-unattended.sh` exits non-zero naming
  `fail 29`. Observed.
- **AC5** — When the advertised default-branch tip cannot be read, `fail 29` does NOT fire. Observed,
  because this is the arm that decides whether the leg reds a fleet on a network fault.
- **AC6** — When either new condition is deleted from its source, its arm FAILS, and passes again when
  restored — witnessed by `bash tools/unattended/unattended.test.sh` for `fail 50` and
  `bash tools/unattended/check-unattended.test.sh` for `fail 29`. Observed for both.
- **AC7** — `python3 tools/memory-tree/check-arms.py --check` exits 0 with `fail 50` and `fail 29`
  armed rather than pinned.
- **AC8** — `bash tools/unattended/check-unattended.sh` and `bash
  tools/unattended/adopt-unattended.sh --check` exit 0, and `bash
  tools/unattended/run-unattended-gates.sh` reports every suite green.

## 7. Gates

On the bar: `harness arms (fail branches armed or pinned)` — unguarded, and the one that makes S3
non-optional — plus `unattended kit gate` and `unattended skill wiring`.

Off the bar by owner ruling 2026-08-23 and therefore run BY HAND, with the result recorded in §9:
`bash tools/unattended/run-unattended-gates.sh`, which carries `unattended.test.sh` and
`check-unattended.test.sh`. A suite that is not on the bar and not run is not coverage.

## 8. Open questions

- **F1 — does `recipe` belong in `SECOND_ANCHOR_MODES`?** Options: (a) `prompt` + `recipe`, because
  `SKILL.template.md`'s playbook path says in as many words that a run authoring its own build folder
  "needs `published`"; (b) `prompt` alone, narrowest, but it breaks the documented playbook-run path
  for any adopter whose owner does not pre-land the folder. Recommendation (a), because (b) would make
  the kit's own routing table describe a path preflight refuses.
  **RESOLVED (author, 2026-08-24): (a).** The carrier states the requirement, so excluding `recipe`
  would contradict a shipped instruction rather than narrow an abuse.
- **F2 — refuse, or downgrade to the strict anchor?** A downgrade would let a `slug` run continue
  against the merge-base instead of erroring. Rejected: the merge-base is exactly where its README was
  already shown to be absent, so the run would take `fail 6` one step later with a message about the
  wrong thing. **RESOLVED (author, 2026-08-24): refuse, and name both exits.**

## 9. Revision log

- rev-1 · 2026-08-24 · initial draft.

## 10. Reuse audit

No new seam. `check_authorization` already reads the mode and already refuses on it (`fail 44` for a
mode outside the published set), so S1 is one more condition in the function that owns the question.
The leg already derives published-ness from `ADV_HEAD`/`ADV_TIPS` for check 9, so S2 reuses that
observation rather than making a second one — `is_published` itself is deliberately NOT reused,
because it answers "ancestor of ANY advertised tip", which is true under both anchors and would
therefore never discriminate.
