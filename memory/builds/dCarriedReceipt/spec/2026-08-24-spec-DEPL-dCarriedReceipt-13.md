# DEPL-dCarriedReceipt-13 — `govkit adopt`, the receipt bootstrap

**Status:** SPECCED · rev-1 · 2026-08-24 · node d · Tier-2 · base 9ddcc5c9 · streams deployer · ratified 2026-08-24

## 1. Goal

`cmd_update` refuses without `<target>/.governance/install.json` (`govkit.py:2932`) and `cmd_check`
refuses the same way. Neither live target has one, so the entire update engine has moved zero rows
against a real adopter and everything in `VERDICT_GRID`, `three_way` and the write loop is exercised
only by fixtures. `adopt` is the unblocker: a read-only verb that measures an already-installed tree
against gov history and writes the receipt that measurement supports. Nothing else in this build
reaches either target without it.

## 2. Scope (IN)

- **S1** — the verb: `adopt --target <t> [--to <rev>] [--pin <path>=<rev>] [--re-adopt] [--write]`.
  Read-only unless `--write`, matching `update`'s default and for the same reason. `--to` and
  `--write` already parse; `--pin` and `--re-adopt` widen `parse_args` (`:3316`), which today returns
  a fixed 8-tuple. `USAGE` (`:3298`) and the verb tuple in `main` (`:3370`) each gain the name.
- **S2** — the destination set comes from `load_deploy` (`:553`), `target_context` (`:535`) and
  `resolve_entry` (`:270`), one entry at a time. `adopt` never invents a second path map: a second
  answer to "where does this file land" drifts the first time a descriptor changes, which is the
  class `-1` closes.
- **S3** — attribution, per planned destination present in the target's INDEX. Walk `git -C <gov> log
  <to-rev> -- <src>`, **never `--all`**. At `9ddcc5c9` gov carries 8 commits reachable from a ref and
  not from `HEAD`; a walk that reaches them attributes a row to a vintage the adopter was never
  offered.
- **S4** — the attribution is **RUNG-MAJOR**: every commit in the walk is tested at `verbatim` first,
  then `eol`, then `relocate`, and the newest commit within the FIRST rung that matches wins. Rung
  order dominates recency because preferring a newer commit at a lossier rung selects a base whose
  delta was never applied, and the three-way then re-applies work the adopter already has.
- **S5** — the row written: `gov_oid`, `oid`, `commit`, `carry`, and a new `evidence` field reading
  `"vintage-match"`. `apply` writes `"apply"`. An INFERRED base must never be mistaken for one a write
  produced, and today no receipt row carries any provenance-of-provenance field at all.
- **S6** — `--pin <path>=<rev>` fixes one destination's base by operator assertion. Such a row records
  `evidence: "pinned"`, so an assertion is never read back as a proof.
- **S7** — a destination attributing to nothing takes role `forked` from `-10`, with no `commit` and
  no `gov_oid`. Report-only, written in neither direction, ever.
- **S8** — three refusals: `--target` resolving to the gov checkout (the form at `:2930`); an existing
  `install.json` without `--re-adopt`, on `cmd_intake`'s stated reasoning (`:3186-3191`) that a
  committed authorization is not something a verb silently rewrites; and a dirty target index.
- **S9** — `selftest.py` arms per branch and a `refusal_join.py` arm per refusal.

## 3. Non-goals (OUT)

- **Not** refusing when some rows fail to attribute. Partial attribution is the normal state of a
  hand-forked adopter, and a bootstrap that demands totality bootstraps nothing. Measured below.
- **Not** writing a single byte into the target's working tree. `adopt` writes `install.json` and
  `install.sums` under `--write` and nothing else. The first byte movement is `update`'s, after an
  operator has read the receipt.
- **Not** auto-resolving a base for a row matching no gov vintage. That is on the build's ratified
  cut list; such a row is `forked` and stays `forked`.
- **Not** rename detection during attribution. A destination whose source moved in gov attributes at
  the source path the descriptor declares TODAY; `-11` owns renames on the update path.
- **Not** installing an unadopted kit, and **not** `--force` or `--yes`. Both are cut-list items.
- **Land-alone:** `adopt` needs `-1` (destinations), `-7` (two identities), `-9` (the rungs) and
  `-10` (role `forked`) beneath it. It cannot land before them, and it is stated in section 8.

## 4. Design

### Data model

Each written row carries the receipt shape `apply` already produces at `:2458-2460` — `path`, `role`,
`kit`, `version`, `source`, `commit` — plus `-7`'s `gov_oid` and `oid`, `-9`'s `carry`, and this
unit's `evidence`. `evidence` takes exactly `"apply"`, `"vintage-match"` or `"pinned"`.

**The safety argument rests on one field.** A bootstrapped row's `gov_oid` is the hash of the GOV blob
at `commit` — `blob_at(root, commit, src)` (`:2148`) — and never of the bytes on the target's disk.
Invert that and `gov_oid == oid` for every row, the identities agree, the local-delta predicate reads
false, and a repathed file classifies `("equal","differs")` → `stale` (`:2845`) → `dp.write_bytes(
c["theirs"])` (`:3071`) on the FIRST write. Every carried edit in the tree would be destroyed by the
first update, reported as a clean write with zero conflicts. The field is the whole difference between
a bootstrap and a silent overwrite.

### Inventory

Measured at `9ddcc5c9` against inCMS's own `.governance/install.index`, which is the only receipt-like
artefact either live target holds. Of its 92 rows, 38 carry a blob OID that exists in gov's object
database and 54 do not. Excluding the 13 `project-owned` rows — bytes gov never authored, which
`UPDATE_ROLE` skips (`:2860`) — **41 gov-authored rows do not attribute by verbatim identity**, and 16
of those are the deliberate divergences `.governance/kits.json` documents, each carrying a `record` id.
The `eol` and `relocate` rungs are what must reduce the remaining 25; whatever survives them is
`forked`. This is the measurement behind S3's non-goal: a bootstrap that refused on any unattributable
row would refuse on inCMS today.

### Migration

None. `adopt` creates a receipt where there was none. `--re-adopt` replaces one, which is why it is a
flag rather than the default.

### Alternatives rejected

- *Hash the target's bytes into `gov_oid`.* Rejected above; it is the inversion that makes the first
  update destructive.
- *Walk `git log --all`.* It reaches 8 commits off `HEAD` in this repo today, several of them on
  in-flight branches. An adopter attributed to an unmerged branch has a base nobody shipped.
- *Prefer the newest matching commit across all rungs.* This is the rung-major decision inverted, and
  it is load-bearing: a newer `relocate` match beats an older `verbatim` one only if you are willing
  to treat a lossy transform as evidence, which then feeds a three-way base that was never real.
- *Fold `adopt` into `intake`.* `intake` writes the descriptor from operator answers and refuses to
  measure anything (`-3`). Measuring a tree and recording a decision are different verbs with
  different refusals, and merging them makes one refusal reachable through the other's flags.
- *Derive destinations from the target's tree instead of the descriptor.* That is a second path map,
  and it would classify any file the adopter happened to place under a kit directory as gov's.

### Files touched (estimate)

`tools/govkit/govkit.py` (~180 lines: `cmd_adopt`, the attribution walk, `parse_args`, `USAGE`,
`main`), `tools/govkit/selftest.py` (9 arms), one fixture family building a scratch gov with a
multi-commit history and a target holding verbatim, `eol`, `relocate` and unattributable copies.

## 5. Production-readiness checklist

- security — `adopt` is the field that decides whether the first `update --write` is a sync or a
  wipe. S5's `gov_oid` rule is the security content of this unit; every other line is bookkeeping
  around it.
- perf / scale — one `git log` walk per planned destination, bounded by that path's history. On
  NicoCares' 143 planned writes this is the run's dominant cost; the walk is capped at the first
  matching commit per rung and short-circuits on `verbatim`.
- a11y — N/A: CLI.
- i18n — N/A.
- error / empty / loading states — a target with `deploy.toml` and an empty tree bootstraps a receipt
  with zero rows and says so rather than exiting silently; a destination absent from the index is
  reported as not-installed and gets no row.
- observability — the run prints one line per destination with its rung and its evidence, and a tally
  by rung and by `forked`. That tally is the operator's read on whether the tree is adoptable before
  a byte moves.
- risks — the real risk is a WRONG attribution that looks right: a path whose history contains a
  coincidentally identical blob at an old commit. Rung-major plus newest-within-rung bounds it, and
  `--pin` is the operator's correction. A wrong base makes a later three-way noisier, never
  destructive, because the raw-write arm stays closed whenever `oid != gov_oid`.
- testing + left-shift gates — nine `selftest.py` arms. The class left-shifted is the inversion in
  S5, gated as a standing predicate: for every written row, `gov_oid` equals `git -C <gov> rev-parse
  <commit>:<src>`.
- migration / rollback — the receipt is a new file; rollback is deleting it. `--re-adopt` is the only
  path that replaces an existing one and it refuses without the flag.
- user docs — `WIRE-INTO-PROJECT.md` gains an adoption section: `intake`, then `adopt`, then read the
  receipt, then `update`. This is the first documented path onto the engine for an existing tree.

## 6. Acceptance criteria

- **AC1** — At `9ddcc5c9`, `python tools/govkit/govkit.py adopt --target <t>` exits **2** with
  `unknown subcommand 'adopt'` from `main` (`:3387`). Observe this RED first; the verb does not exist.
- **AC2** — Without `--write`, a run against a fixture prints its per-destination rows and creates no
  `.governance/install.json` (`test ! -e`), and the target's index is unchanged
  (`git -C <target> status --porcelain` empty).
- **AC3** — With `--write` against a target holding gov's bytes verbatim at `--to`, every row records
  `carry: "verbatim"`, `gov_oid == oid`, and `evidence: "vintage-match"`.
- **AC4** — The inversion gate. For a target file that is a `relocate` of gov's blob, the written row's
  `gov_oid` equals `git -C <gov> rev-parse <commit>:<src>` and does **not** equal
  `git -C <target> rev-parse :<path>`; a subsequent `govkit.py update --to <same rev> --write` writes
  zero bytes to that path and `git -C <target> status --porcelain` stays empty.
- **AC5** — Rung-major. In a fixture where the newest commit in a path's history matches only at
  `relocate` while an older commit matches `verbatim`, the written row's `commit` is the older one and
  its `carry` is `"verbatim"`.
- **AC6** — Partial attribution proceeds. A fixture carrying one destination that matches no gov
  vintage writes that row with `role: "forked"`, no `commit` and no `gov_oid`, and the run exits **0**.
- **AC7** — `--pin <path>=<rev>` overrides the walk for that path only, and the row records
  `evidence: "pinned"` rather than `"vintage-match"`.
- **AC8** — All three refusals fire by name: `--target` pointed at the gov checkout; a second `adopt`
  over an existing `install.json` without `--re-adopt`; and a run against a target whose index is
  dirty. `python tools/govkit/refusal_join.py` exits 0 with an arm for each.

## 7. Gates

`bash tools/run-gates/run-gates.sh` full bar; specifically the `govkit selftest` and `govkit
selfcheck` legs, plus `tools/govkit/refusal_join.py`. Adds nine arms and the AC4 standing predicate to
`selftest.py`; adds no new leg file. The `selfcheck` verb-coverage arm must also see the new verb, so
its assertion over `USAGE` and `main`'s dispatch stays honest.

## 8. Open questions

- **F1 — must `adopt` refuse on a dirty target WORKTREE, or only a dirty INDEX?** Index only. `adopt`
  reads the index and writes one file under `.governance/`; refusing over an unrelated unstaged edit
  in a repository gov does not own is the shape adopters learn to route around. `-12` owns the
  worktree preconditions on the verbs that write bytes.
  RESOLVED (agent, 2026-08-24, delegated): index only, under the full-scope approval.
- **F2 — should `--re-adopt` preserve rows the previous receipt marked `forked`?** No. `--re-adopt`
  re-measures from scratch; carrying a stale `forked` verdict forward is exactly the trusted-from-the-
  receipt shape the `carry` contract forbids.
  RESOLVED (agent, 2026-08-24, delegated): full re-measurement.
- **F3 — landing order.** This unit cannot land alone: it consumes `-1`'s destination resolution,
  `-7`'s two identities, `-9`'s rungs and `-10`'s `forked` role. It lands after all four, which is the
  build README's step 5.
  RESOLVED (agent, 2026-08-24, delegated): lands after `-1`, `-7`, `-9`, `-10`.

## 9. Revision log

- rev-1 · 2026-08-24 · initial draft, from the kit-sync design pass (5 lenses + fold). `cmd_update`'s
  no-receipt refusal, `resolve_entry`'s return shape, `blob_at`'s index-side contract, `parse_args`'
  8-tuple and `main`'s verb dispatch were each read in source at `9ddcc5c9`. **Two brief corrections.**
  The brief says gov carries 6 commits off `HEAD`; measured, `git rev-list --all --not HEAD --count`
  reports **8** at `9ddcc5c9`, which strengthens rather than weakens the no-`--all` rule. The brief
  says 28 of inCMS's 92 rows cannot attribute; that number does not reproduce from any instrument in
  either tree. Measured by blob identity against gov's object database, 54 of 92 do not attribute
  verbatim, or **41** excluding the 13 `project-owned` rows. The brief's other figure is exact: 16 of
  them are documented in `.governance/kits.json`, each with a `record` id.

## 10. Reuse audit

Every input is an existing seam and none is duplicated: `load_deploy` (`:553`) for the descriptor,
`target_context` (`:535`) and `resolve_tokens` (`:516`) for the ctx, `resolve_entry` (`:270`) for the
destinations, `blob_at` (`:2148`) for gov-side bytes, and `-7`'s index-side reader for target-side
bytes. The receipt row shape is `cmd_apply`'s (`:2458-2460`) with the fields `-7`, `-9` and this unit
add, so `cmd_update` reads one row grammar rather than two. The refusals reuse the `Refusal` class
(`:78`) and the `Report` findings channel (`:565`), and are counted by the existing `refusal_join.py`
contract rather than a new counter. One genuinely new mechanism exists — the attribution walk — and it
has no prior seam: nothing in this engine has ever asked git a question about a path's history.
