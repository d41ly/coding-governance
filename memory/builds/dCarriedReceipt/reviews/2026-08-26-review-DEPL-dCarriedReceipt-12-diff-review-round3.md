# Closing diff review, ROUND 3 — the fold's own fold

**Serves:** review DEPL-dCarriedReceipt-12 DEPL-dCarriedReceipt-7 DEPL-dCarriedReceipt-9

Node `a` · 2026-08-26 · base `267b598f` (round 2's recorded tip) · head = working tree.

## Scope, and what this round is

Everything since round 2 was recorded: commit `3dee7112` (round 2's own fold) plus this session's
uncommitted work — the owner's four rulings, S13's inCMS fixture, and the six remaining round-2
findings.

**THE FAN DID NOT RUN.** This is a single-reviewer pass, the same shape round 1 recorded for `-4`.
An adversarial workflow was authored and BLOCKED three times by this repo's own `agent-cap` hook —
first for fanning one verify agent per finding, then twice on the marker grammar for a bounded
receiver. That is the hook working; it is also why the finding below was found by reading and by a
sandbox rather than by five lenses. Weight the coverage claim accordingly: what follows is what one
pass over one diff found, and it is not a substitute for the fan.

## Verdict: BLOCKED

One reproduced defect of the same class as round 2's blockers, plus three defects in the FIX for it,
plus three of my own arms asserting things that were not true. All folded. The verdict is BLOCKED
rather than CLEAN because the confirmed-blocker count did not fall — round 2 had two, round 3 has
one, and one of them is an arbitrary file write.

---

## B1 — a target-supplied `prefix` escapes the target repository, and `apply` WRITES there

`tools/govkit/govkit.py`, `target_context` → `planned_writes` / `_cmd_apply`.

**REPRODUCED, in a sandbox, before anything was written.** A target repo whose own
`.governance/deploy.toml` says `prefix = "../../PWNED"`:

- `govkit plan` printed 26 rows rooted at `../../PWNED/memory-tree/`, cheerfully.
- `govkit apply` **wrote all 26 files outside the target repository.** Counted on the filesystem.

`demand_safe_token` — round 2's own fix for the command-injection blocker — cannot catch this, and
correctly so: its character class admits `.` and `/` because every legitimate token value there is a
path fragment. A traversal is spelled entirely in legal characters.

**The containment check already existed, in the wrong verb.** `cmd_update`'s write loop resolves each
row against the target root and refuses on `ValueError`, under a comment calling it *"the one
boundary this whole tool is built around"*. `apply` — the verb that actually writes kit files — had
no such check on the path it derives from the target's own `prefix`. Same class as B1/B2 one
operation over: **a target-supplied value reaching a dangerous operation because the guard was
written for a different caller.**

**Fix.** `demand_contained_dest` — pure string containment, since a destination is a repo-relative
POSIX path and escapes exactly when it normalises to `..`-leading or is absolute. A drive letter
counts, because this project's own node is Windows and `posixpath.isabs("C:/x")` is False. Called
from the two row producers of the two verbs that had no guard.

**Failing case observed:** neutering the guard puts all 29 escaping rows back in the preview.

**Left-shift gate.** Four arms, on `plan` and on `apply`, plus one asserting on the FILESYSTEM that
nothing landed above the target — because a refusal that still wrote is the failure that matters.

---

## What the fix got wrong, three times, and what each cost

Recorded at length because the placement mistakes are more instructive than the defect.

**Placement 1 — `resolve_dests`.** Eight call sites reach that function, `selfcheck` and `update`
among them. A whole-run `Refusal` raised from inside it fired on `-11`'s escaping-rename fixture and
**pre-empted that unit's own refusal** — the *"two units refusing one state with two messages"*
defect this codebase keeps recording, introduced by the fix for a different one.

**Placement 2 — `resolve_entry`.** Measured, and the wrong seam in both directions: `plan` does not
route through it at all (it has `planned_writes`, the seam `resolve_rule_pool`'s own docstring
already records), while `update`, `adopt` and `selfcheck` all do. Exactly backwards — the verb that
needed the guard did not get it, and the verbs that own their own refusals kept being pre-empted.

**Placement 3, and a fourth error inside it.** Guarding both row producers explicitly. The first cut
checked at `planned_writes`' return, over `out`, reading `row["rule"]` — a key plan rows **have never
carried**. The machine/link exemption could therefore never fire, and `kickoff-manifest`'s
`{user_skills}/session-kickoff` would have been refused on every plan. Caught by reading the row
shape rather than by the suite, which is roughly ten minutes a round cheaper.

**The exemption itself was also missed first time.** A `scope = "machine"` or `link = true` rule
lands outside by design and `apply` writes nothing for it — it emits an order. Without the exemption
five `kickoff-manifest` arms went red. §7 says to run a candidate predicate over the real tree and
print hits AND near-misses *before* wiring it. That step was skipped; the suite caught what it would
have caught. Run afterwards over all 46 declared destinations: **0 false positives, 0 near-misses,
and the one exemption is load-bearing.**

---

## M1 — `apply` stamped receipt `oid`s before the renormalize

`git add --renormalize` rewrites the index blob of every LF-pinned path, and it runs AFTER the stamp.
Every affected row recorded a blob the target does not hold. `-9` S12 defines `oid` as *the blob
ACTUALLY WRITTEN*; a value stamped before the last thing that writes is not that.

Invisible in gov's own tree because gov ships LF, so the renormalize is a no-op here — and live at
exactly the adopter `-7` exists for, the one whose checkout applies a line-ending filter.

**Found by ruling A's arm**, which was written to assert something else entirely. That is the
argument for writing the negative half of every pair.

**Fix.** One re-stamp after the renormalize. **The first cut was role-blind and regressed two
ratified criteria** — `-7` S9 requires an `attributes` row to carry NEITHER identity, and AC5 and
AC11 both assert it. Restored to `LANDABLE_ROLES`; `.gitattributes` is unblocked at the dirty check
instead, where `UPDATE_ROLE["attributes"] == "pins"` (*"recompute, compare, report; never write"*)
says why it can never be S4's hazard.

**Left-shift gate.** An invariant arm: every landable receipt row records the blob the target's index
holds. **Declared skip:** gov ships LF, so the renormalize is a no-op in this fixture and M1's
specific trigger goes unexercised here. Reaching it needs an apply onto a CRLF checkout, and no
fixture in this suite builds one — `clone_crlf` clones a target that was *already* applied to.

---

## My own arms, three of them wrong

Recorded because a wrong arm that names a real file is the most expensive kind.

- **`/etc/govkit` is not a hazard.** `target_context` does `.strip("/")`, so it becomes `etc/govkit`,
  an ordinary relative path inside the target. My arm asserted a refusal — it was asserting a bug.
- **`C:/PWNED` is refused, but by `demand_safe_token`**, because `:` is outside the token class. The
  containment guard never sees it. Both arms now assert the OUTCOME — did anything land outside —
  rather than which guard spoke.
- **The receipt-invariant arm compared apply's receipt against an index two `update --write` runs
  later**, one of which was my own negative-half arm deliberately staging an operator edit to that
  very file. It reported a real-looking defect naming a real file. Now re-reads the receipt and runs
  before the edit.

All three came from reasoning about the call graph instead of reading it.

---

## Parked for the owner

**`demand_safe_token`'s class excludes `:`, so a Windows drive-letter answer refuses a legitimate
install.** A target whose `deploy.toml` says `user_skills = "C:/Users/x/.claude/skills"` is refused,
with a message about command injection that names nothing the operator did wrong. `kickoff-manifest`
is in the DEFAULT selection and its rule is `to = "{user_skills}/session-kickoff"`, so this sits on
the common path for a Windows adopter. No arm catches it: both fixtures use forms that pass
(`~/.claude/skills`, `/tmp/gk-fake-skills`).

The guard is doing its job — a `:` in a value interpolated into a `bash -c` template is exactly the
reproduced injection — so this is a blast-radius question, not a bug report. Widening a guard that
closes a reproduced ACE is an owner decision and this run has no owner turn. Options are in the
run-state park.

## What this round says about the method

Round 2's lesson was *a declared population whose labels a human types will be wrong*. Round 3's is
narrower and about me: **I placed one guard three times and wrote three arms wrong, every one of them
by reasoning about the call graph instead of reading it.** Each correction cost a full suite run,
about ten minutes. Two of the four errors would have been caught in seconds by the checks the charter
already mandates — run the predicate over the real tree first (§7), and read the shape of the data
you are asserting on.

The cheap change is not more review. It is: before wiring a predicate, enumerate its real population
and print hits and near-misses; and before asserting on a row, print one.
