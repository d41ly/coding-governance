# DEPL-dShippedRelease-18 — every release updates gov's own install first: `kits.cut` refuses a tag at a SHA with no green gov-first record

**Status:** OPEN · rev-1 · 2026-10-30 · node d · Tier-2 · base f4597719 · streams deployer · order 25 · advances DEPL-dShippedRelease-32

**Carries:** cl-dClosedLoop-0428@e9fcd4a6 whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md](../build/2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md) | journal | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 DEPL-dShippedRelease-49 DEPL-dShippedRelease-50 DEPL-dShippedRelease-51 DEPL-dShippedRelease-52 DEPL-dShippedRelease-53 DEPL-dShippedRelease-54 DEPL-dShippedRelease-55 DEPL-dShippedRelease-56 DEPL-dShippedRelease-57 DEPL-dShippedRelease-58 DEPL-dShippedRelease-59 DEPL-dShippedRelease-60 DEPL-dShippedRelease-61 DEPL-dShippedRelease-62 DEPL-dShippedRelease-63 DEPL-dShippedRelease-64 DEPL-dShippedRelease-65 DEPL-dShippedRelease-66 DEPL-dShippedRelease-67 DEPL-dShippedRelease-68 DEPL-dShippedRelease-69 DEPL-dShippedRelease-70 DEPL-dShippedRelease-71 DEPL-dShippedRelease-72 DEPL-dShippedRelease-73 DEPL-dShippedRelease-74 DEPL-dShippedRelease-75 DEPL-dShippedRelease-76 DEPL-dShippedRelease-77 DEPL-dShippedRelease-78 |
| [2026-10-30-build-DEPL-dShippedRelease-1-spec-stage-returns.md](../build/2026-10-30-build-DEPL-dShippedRelease-1-spec-stage-returns.md) | research | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 |
| [2026-10-30-build-DEPL-dShippedRelease-7-reuse-scout-d.md](../build/2026-10-30-build-DEPL-dShippedRelease-7-reuse-scout-d.md) | research | DEPL-dShippedRelease-7 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-20 DEPL-dShippedRelease-25 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-31 |
| [2026-10-30-prompt-DEPL-dShippedRelease-1-spec-brief.md](../prompts/2026-10-30-prompt-DEPL-dShippedRelease-1-spec-brief.md) | research | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 |
| [2026-10-30-review-DEPL-dShippedRelease-1-spec-audit-round1.md](../reviews/2026-10-30-review-DEPL-dShippedRelease-1-spec-audit-round1.md) | spec-audit | DEPL-dShippedRelease-10 DEPL-dShippedRelease-21 DEPL-dShippedRelease-23 DEPL-dShippedRelease-31 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-13 DEPL-dShippedRelease-4 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-6 DEPL-dShippedRelease-27 DEPL-dShippedRelease-5 DEPL-dShippedRelease-30 DEPL-dShippedRelease-3 DEPL-dShippedRelease-25 DEPL-dShippedRelease-7 DEPL-dShippedRelease-16 DEPL-dShippedRelease-20 DEPL-dShippedRelease-17 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-24 DEPL-dShippedRelease-8 DEPL-dShippedRelease-26 DEPL-dShippedRelease-19 DEPL-dShippedRelease-22 DEPL-dShippedRelease-9 |

<!-- /gen:spec-records -->

## 1. Goal

A release must not reach an adopter before the survival path has run on gov. TOOL-dSafePassage-8
already builds that path: the lander runs the `update` gov's own tree takes, in source mode, in every
prepared merge, and records it in gov's source-mode receipt. A release is a subset of those landings,
so this clause is mostly carried there. The one new act is on the tag side: `kits.cut` reads the
record at the SHA it is about to tag, and refuses when the record is absent or red.

## 2. Scope (IN)

Build-run preconditions, specced and DEFERRED at base `f4597719`, none built: TOOL-dSafePassage-1
(`read_steps(root, rev, landed_ref)`, `read_retired`), -2 (`run_step_walk`), -3 (`set_step_state`), -7
(`run_step_isolated`) and -8 (`check_gov_first`, `run_gov_first`, the source-mode receipt). The
parents the scouts list beside them are reached through those units, and each is a precondition of
this build run as the brief states.

- **S1** — The survival path, carried by reference. `update` on gov (TOOL-dSafePassage-8 S1), the
  landing's check `check_gov_first` (its S2) and `run_gov_first` in `tools/push-main.sh` (its S4) are
  this clause's mechanism. This unit re-specs none of them and adds no copy. NOT OBSERVED here:
  TOOL-dSafePassage-8's AC3 to AC6 observe the path, and this unit reads only the record it leaves.
- **S2** — The reader. `read_gov_first(root, sha)` in `tools/govkit/upgrade_steps.py` returns
  `(state, why)`, `state` one of `green`, `absent` and `red`, reading the record at the SHA and never
  the working tree:
  - `git show <sha>:.governance/install.json` that names no blob, does not parse as a JSON object, or
    whose `mode` is not `source`, reads `absent`, because a receipt of another shape is no gov-first
    record.
  - An empty `steps` reads `absent`, because a record of nothing proves nothing.
  - A row whose `state` is not `applied` reads `red`, naming the id.
  - `read_steps(root, sha, ...)` gives the ids declared at that SHA. An id declared and not listed
    reads `red`. An id listed and not declared reads `red` unless `read_retired` names it the old id
    of a succession row. This compare is the first half of `check_gov_first`, extracted as
    `check_step_ids(receipt, declared)` and called by both, so the rule lives once.
  - Anything else reads `green`.

  Observed by AC1, AC2, AC3, AC4 and AC5.
- **S3** — The CLI. `python upgrade_steps.py gov-first <sha>` prints one line,
  `gov first — <sha8> · <state> · <why>`, and exits 0 on `green`, 1 on `absent` or `red`, and 2 when
  `<sha>` names no commit. Observed by AC1 to AC5.
- **S4** — The refusal. `cmd_cut` (DEPL-dShippedRelease-3 S5) calls `read_gov_first` on the SHA it is
  about to tag, after it resolves that SHA and before it derives notes or writes a tag. A state other
  than `green` exits 1, prints `cut refused — <sha8> has no green gov-first record: <why>`, writes no
  tag and no notes, and raises the `kits-cut` owner item that unit raises on any other refusal.
  Observed by AC6.
- **S5** — The help page. `help/upgrade-steps.md` (TOOL-dSafePassage-1 S10) gains one paragraph: gov
  takes every step first, at the landing, and a release is refused at a SHA whose record is absent or
  red, with what the operator does about each. Observed by AC7.

## 3. Non-goals (OUT)

- The walk, the source-mode receipt, `check_gov_first`'s witness re-run and `run_gov_first`:
  TOOL-dSafePassage-8's. This unit extracts one compare from `check_gov_first` and changes no verdict.
- `govkit.py cut`, the tag grammar, the notes and the `kits.cut` item row: DEPL-dShippedRelease-3's.
- Re-running an upgrade step or a witness at the cut (§8 F2).
- A refusal at the push of a tag in `.githooks/pre-push`. No tag is made by any other route, and the
  scouts did not verify how that hook treats an annotated tag (§8 F3).
- Proving a landing ran through the lander. A commit that bypassed it and carries a receipt whose
  `steps` still equal the declared ids reads `green`, and the bypass is `hooks.bypass`'s question.

### Edges

- **consumes-from** `DEPL-dShippedRelease-3` — `read_release_tags` and `govkit.py cut`: the cut this unit's refusal sits in, and the reader AC6 uses to see that no tag was made; without them S4 has nowhere to stand
- **consumes-from** external — TOOL-dSafePassage-8's source-mode receipt at `.governance/install.json` in each landed tree and its `check_gov_first`, and TOOL-dSafePassage-1's `read_steps` and `read_retired`; without them `read_gov_first` reads every SHA `absent`

## 4. Design

### The flow at a cut

`run_gov_first` folds the receipt into every prepared merge (TOOL-dSafePassage-8 §4), so the record
of a landed SHA is a blob in that SHA's own tree. `read_gov_first` therefore needs no ref and no
network, and any node holding the SHA can read it. The cut runs after the landing that made the
SHA, so it adds one read, no write and no walk.

```text
kits.cut → govkit.py cut → resolve the SHA → read_gov_first(root, sha)
  green         → derive notes, tag, as DEPL-dShippedRelease-3 says
  absent | red  → exit 1, no tag, no notes, the kits-cut owner item
```

The item this reads through is `item.kits.cut`, owned by DEPL-dShippedRelease-3, and `item.kits.update`
is DEPL-dShippedRelease-17's. This unit owns no node.

### Why the compare moves and the witness does not

`check_gov_first` asks two things: the ids equal both ways, and each `applied` witness holds now. The
first is a pure function of a receipt and a declared list, so both callers share it. The second runs
programs on a tree, and the tree at a tag's SHA may not be the tree checked out at the cut (§8 F2).

### Inventory

| Minted | Kind | Home |
|---|---|---|
| `read_gov_first`, `check_step_ids` | functions | `tools/govkit/upgrade_steps.py` |
| `gov-first` | CLI verb | `tools/govkit/upgrade_steps.py` |

`python tools/lexicon/lexicon.py --suggest read_gov_first --as py.function` printed OK on 2026-10-30.
`check_step_ids` leads with the declared verb `check`. No conf key, policy key or gate leg is minted.

### Migration

Additive. The first tag is cut after TOOL-dSafePassage-8's first landing, so every SHA a cut can
name carries the record. A cut at a SHA older than that landing refuses as `absent`, which is the
intent: no release predates gov's own walk.

### Rollout

The refusal is live at the first `govkit.py cut` after the build lands. Nothing runs at an adopter,
which never cuts.

### Files touched (estimate)

- `tools/govkit/upgrade_steps.py`
- `tools/govkit/govkit.py`
- `tools/govkit/selftest.py`
- `help/upgrade-steps.md`

### Alternatives rejected

- **Re-run `check_gov_first` whole at the cut.** It runs each witness on a working tree, which is
  the wrong tree for a tag at a SHA other than the checkout. The test that rejected it: the cut's
  SHA is resolved from the remote tip, and nothing makes the node's working tree equal it (§8 F2).
- **A separate gov-first ref written at the landing.** It adds a second record of one fact beside the
  receipt, which the landing already commits. The test: TOOL-dSafePassage-8 §4 folds the receipt into
  the merge, so a blob read at the SHA answers with no new writer (`[one-fact]`).
- **Grading the receipt's `gov_commit`.** A source receipt has none (TOOL-dSafePassage-8 S1, §8 F2
  there), so the field cannot bind the record to a SHA. The blob's own place in the SHA's tree does.

## 5. Production-readiness checklist

- security: read-only at the cut. The blob is parsed as JSON and its values are printed, never run.
  A crafted receipt cannot run anything here, and it can only forge a `green` for a SHA that already
  landed with that receipt in its tree.
- perf / scale: one `git show` and one `read_steps` at a revision per cut.
- error / empty / loading states: no receipt, a malformed one and an empty `steps` each read `absent`
  by name. A SHA that names no commit exits 2. A refused `read_steps` passes its `Refusal` up.
- observability: the one CLI line, and the cut's refusal line naming the SHA and the reason.
- risks: a red record at the tip holds every release until a landing repairs it. That is the point of
  the clause, and the `kits-cut` owner item puts it in front of the owner.
- testing: the probes of §6 and one arm in `tools/govkit/selftest.py` (§7).
- migration: §4 "### Migration".
- user docs: `help/upgrade-steps.md`, S5.

## 6. Acceptance criteria

- **AC1** — When `python upgrade_steps.py gov-first <sha>` runs on a fixture commit whose tree holds
  no `install.json`, it prints `absent` and exits 1.
  Red when: a missing record reads `green`, or the reader falls back to the working tree's receipt.
  fixture: a scratch repository under `%TEMP%`.
- **AC2** — When `python upgrade_steps.py gov-first <sha>` runs on a fixture commit whose receipt holds
  a `steps` row with state `failed`, it prints `red`, names that id and exits 1.
  Red when: the reader trusts the row's presence and ignores its `state`.
- **AC3** — When `python upgrade_steps.py gov-first <sha>` runs on a fixture commit declaring one step
  the receipt does not list, it prints `red` naming the id and exits 1. With a listed id that a
  `[[retired]]` row names as an old id, and nothing else differing, it prints `green`.
  Red when: the compare runs one way only, or a retired id reds a tree that walked its successor.
- **AC4** — When `python upgrade_steps.py gov-first <sha>` runs on a fixture commit whose receipt has
  no `"mode": "source"`, and again on one whose `steps` is empty, each prints `absent` and exits 1.
  Red when: an adopter-shaped receipt or an empty population reads as a record.
- **AC5** — When `python upgrade_steps.py gov-first <sha>` runs on a fixture commit whose receipt lists
  every declared id `applied`, it prints `green` and exits 0.
  Red when: `green` cannot be reached, which would make AC1 to AC4 pass by refusing everything.
- **AC6** — When `python tools/govkit/govkit.py cut --tip <sha>` runs in a fixture whose tip carries
  AC1's plant, it exits 1 printing `cut refused`, and `read_release_tags(root)` lists no tag at that
  SHA. On AC5's tree it exits 0 and the tag exists.
  Red when: the cut tags first and reads the record after, or reads it at a SHA other than the tag's.
  fixture: a scratch clone and a bare remote under `%TEMP%`, after DEPL-dShippedRelease-3 is built.
- **AC7** — When `grep -n 'gov-first' upgrade-steps.md` runs, it prints the paragraph of S5.
  Red when: the page does not name the refusal.
  fixture: the page exists once TOOL-dSafePassage-1 is built.

## 7. Gates

`govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `policy fixtures` · `recall floor arms` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/govkit/selftest.py · covers AC1 AC2 AC3 AC4 AC5 AC6 · planted fixture commits with no receipt, a failed row, an undeclared id, a non-source receipt and an empty steps list, each seen refused, and a green receipt seen tagged · none

What these do not check: that the landing behind a green record ran through the lander, that a witness
still holds at the tag, or that a tag pushed by hand passed this refusal.

## 8. Open questions

- **F1 — What is a green gov-first record?** Options: (a) the receipt blob at the SHA, its `steps`
  equal to the ids declared at that SHA and every row `applied`; (b) the blob's presence alone; (c) a
  new per-SHA ref. (b) reads a failed walk as green, which fails the clause's "updating gov's own
  install first". (c) states one fact twice. RESOLVED (agent, 2026-10-30, delegated): (a), rung 3,
  because it is the only option a SHA alone can answer with no new writer. widens: none · relaxes: none
- **F2 — Does the cut re-run the witnesses?** Options: (a) the id compare and the states only; (b)
  `check_gov_first` whole, in a worktree checked out at the SHA. (b) adds a worktree and a step-process
  run to a cadence program, and TOOL-dSafePassage-8 already re-ran every witness in that SHA's own
  landing. RESOLVED (agent, 2026-10-30, delegated): (a), rung 3. The landing is where the witnesses
  ran, and the clause asks that the path ran before the release, not that it runs twice.
  widens: none · relaxes: none
- **F3 — Where does the refusal sit?** Options: (a) in `govkit.py cut`, before the tag; (b) in
  `.githooks/pre-push`, on the tag's push. Scout D's disagreement 16 names the tag side, and scout C
  records that the hook's treatment of an annotated tag is unverified. (b) also runs after the notes
  are generated. RESOLVED (agent, 2026-10-30, delegated): (a), rung 3, the first act that can refuse.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-30 · initial draft.

## 10. Reuse audit

The seam extended is TOOL-dSafePassage-8's `check_gov_first` in `tools/govkit/upgrade_steps.py`, not
built, reused by extracting its id compare, and the source-mode receipt it leaves in every landed
tree. `reuse_lookup.py "refuse cutting a release tag at a commit with no green record"` ranked
`records`, `build_commit` and `CensusRefused`, which are name-stem neighbours, and none is a cut or a
tag seam, so the lookup disagrees with the source only by having nothing to find: no cut exists at
HEAD and only three `archive/*` tags do. At HEAD `update` still refuses gov
(`tools/govkit/govkit.py:9167-9168`), as TOOL-dSafePassage-8 §1 says, and `upgrade_steps.py` does not
exist. The recall probe found TOOL-dSafePassage-8 first, and scout D's disagreement 16, which this
spec follows, that only the tag-side refusal is new. Candidates rejected and their tests are under
§4 "### Alternatives rejected".

Recall terms used: `python tools/memory-recall/query.py "how does every release update gov's own install first before an adopter meets it" --terms "gov first release tag kits.cut source-mode receipt survival path update landing adopter order"`
