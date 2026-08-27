# Closing diff review, ROUND 3 — the fold's own fold

**Serves:** diff-review DEPL-dCarriedReceipt-12 DEPL-dCarriedReceipt-7 DEPL-dCarriedReceipt-9

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

THREE blockers, and the count went UP.

- **B1** — a reproduced arbitrary file write. Needed THREE sites, not the one it named: `prefix`,
  `[gate_runner].file` (which exited 0), and the rollback loop.
- **B2** — the round-2 token guard refusing a legitimate Windows install.
- **B3** — the same token guard, red on a merge-bar leg for TWO COMMITS, because one character class
  was grading both paths and prose.

All folded, all armed, every reproduction re-run against the fix. **B2 and B3 are one mistake made
twice**, and B1's second site is that mistake's cousin: I wrote a guard for the case in front of me
and applied it to a population I had not enumerated.

The verdict stays BLOCKED and the case is now stronger than it was. Round 2 had two confirmed
blockers; round 3 has three. M8 re-arms a round only when that count strictly FALLS — it ROSE. A
fourth round over this fold is owed, and the two findings that came from the FULL BAR rather than
from this review are the argument for it: the govkit selftest does not cover the acceptance-matrix
leg, so a green suite sat on top of a red bar for two commits and this review would not have found
it either.

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
- **`C:/PWNED` was refused by `demand_safe_token`**, not by the containment guard, because `:` was
  outside the token class — so my arm credited the wrong guard. Superseded by B2: the class now
  admits an anchored drive letter, so containment owns that refusal and the arm names it.
- **The receipt-invariant arm compared apply's receipt against an index two `update --write` runs
  later**, one of which was my own negative-half arm deliberately staging an operator edit to that
  very file. It reported a real-looking defect naming a real file. Now re-reads the receipt and runs
  before the edit.

All three came from reasoning about the call graph instead of reading it.

---

## B2 — the token class refused a legitimate Windows answer (RESOLVED, owner instruction)

Raised in this round as a park; the owner said resolve it rather than hand it over.

`demand_safe_token`'s class excluded `:`, so a target whose `deploy.toml` says
`user_skills = "C:/Users/x/.claude/skills"` was refused — a CORRECT answer on the platform this
project's own primary node runs on — with a message about command injection naming nothing the
operator did wrong. `kickoff-manifest` is in the DEFAULT selection and its rule is
`{user_skills}/session-kickoff`, so this sat on the common path for every Windows adopter. No arm
caught it: both fixtures spell that answer in forms that already passed (`~/.claude/skills`,
`/tmp/gk-fake-skills`) — `fixture-passes-by-finding-nothing`, aimed at a platform rather than a
branch.

**Fix: exactly one colon wide.** A leading `<letter>:/` is dropped before grading and the REMAINDER
is graded by the unchanged class, so `C:/Users/x` passes while `C:/a;b`, `a:b`, `C:x`, `CC:/x` and
backslash spellings all still refuse.

**Why this is not a hole**, stated because widening a guard that closes a reproduced ACE deserves
it. The threat is a value leaving its argument inside a `bash -c` or `python -c` template, which
needs a shell metacharacter: `;` `|` `&` `$`, a backtick, a quote, a newline, a redirect. A colon is
none of those — it is bash's null command and inert as argument text. What a colon CAN do is make a
path absolute on Windows, and that is a **containment** question, owned one function down by
`demand_contained_dest`. Verified: `prefix = "C:/PWNED"` now passes the character grader and is
refused by the escape grader instead, with **zero files written**. Two guards, two jobs, and the
arms assert which one spoke — a silent swap back would otherwise leave both green while the class
widened.

**Left-shift gate.** A twelve-row truth table on the function, plus four arms through the verbs.
**Failing case observed:** reverting the widening refuses the legitimate Windows answer again.

## Parked for the owner

**RESOLVED — see B2 above.** `demand_safe_token`'s class excluded `:`, so a Windows drive-letter
answer refused a legitimate install. A target whose `deploy.toml` says `user_skills = "C:/Users/x/.claude/skills"` is refused,
with a message about command injection that names nothing the operator did wrong. `kickoff-manifest`
is in the DEFAULT selection and its rule is `to = "{user_skills}/session-kickoff"`, so this sits on
the common path for a Windows adopter. No arm catches it: both fixtures use forms that pass
(`~/.claude/skills`, `/tmp/gk-fake-skills`).

The owner instructed that this be resolved rather than parked. Option (a) taken; nothing remains
open here.

## B1's CLOSE-OUT — two more sites, found by enumeration

Raised when the owner asked for B1 to be resolved rather than reported. Fixing the site the finding
NAMED and stopping there is `gate the INSTANCE, not the class` — the rule this round had already
broken once. So every write-capable operation in the engine was listed by AST (72 across 19
functions) and every `target / <non-literal>` join classified by where its path comes from.

**Site 2 — `[gate_runner].file`, and it exits 0.** A TARGET-supplied path that `apply` joins onto the
target root and WRITES. Nothing checked it. REPRODUCED: a descriptor declaring
`file = "../../ESCAPED.json"` made `apply` write that file outside the target repository and **exit
0** — a clean success while writing into a tree the operator never named. The `prefix` escape at
least exited non-zero for unrelated reasons. Guarded in `validate_gate_runner`, the PRE-WRITE pass,
for the reason that function's own docstring already gives: legs are emitted last, so a bad
declaration caught at emission time refuses after everything else has landed. Four arms, one of them
asserting on the FILESYSTEM rather than the exit code, because exiting 0 was this site's danger.

**Site 3 — the rollback loop, guarded WITHOUT a reproduction and labelled as such.** `snap_rows` is
built from `acted` BEFORE the write loop's containment check, and the rollback `unlink()`s and
`checkout-index`es each path. Reaching it needs a receipt row spelling an escape AND a kit whose
check goes red after the run; this suite manufactures no way to produce the pair. Guarded anyway —
same class, one condition — and the refusal branch DECLARES ITSELF UNARMED rather than being counted
as coverage.

**The other eight joins are classified and clean:** gov-authored (`[config].file`), git-derived
(`eol_population`, `git_path`), receipt rows already contained by `cmd_update`'s two `relative_to`
checks, or read-only (`_cmd_adopt`, `check_target_reads_subject`).

**A mid-way error worth recording:** an `rc=2` I first read as the new guard firing was actually
"target already carries memory-tree" from a previous apply on the same fixture. Rebuilt clean before
believing it. Reading a refusal without checking WHICH check produced it is this round's recurring
mistake in miniature.

## B3 — one token class was doing two jobs, and it had been red for two commits

Surfaced by the FULL BAR, which had not run since round 2's commit: `govkit acceptance matrix` was
RED at `3dee7112` and stayed red through `a2186f20`. The govkit selftest does not cover that leg, so
a green suite sat on top of a red bar for two commits.

`demand_safe_token`'s strict class was written for `prefix` — a PATH, interpolated into `bash -c` and
`python -c` argv — and was then applied to every `answers.*` and `kit.<eid>.*` value. Those are not
all paths. The playbook charter's placeholders are rendered into a MARKDOWN DOCUMENT, and a
legitimate override carries spaces by nature: `gate_runner = "bash tools/run-gates/run-gates.sh"`,
`id_families = "PLAY KICK TOOL DEPL"`. The live adopter's answers happen to be all path-shaped, which
is why nothing else noticed.

**This is B2's mistake a second time** — one character class written for `prefix` and applied to
every value passing through the same function. B2 was the Windows drive letter; B3 is prose.

**Fix: two classes, named for what they guard.** Strict for a value that becomes a path or reaches an
argv; prose for one whose only consumer renders it into a document. The prose class is still an
ALLOWLIST — it adds space, comma, equals and colon and admits nothing that can end an argument or
start a command. Fifteen rows graded on both classes side by side, plus a PROPERTY arm asserting the
prose class admits no shell metacharacter at all, plus one asserting neither class grades a traversal
because `demand_contained_dest` owns that. Matrix leg green, 35 arms.

**What the prose class does not promise, stated rather than implied:** a value carrying a space that
reaches a `bash -c` template will WORD-SPLIT there. That is a correctness bug for the operator who
wrote it, visible immediately, and it is not code execution.

## What this round says about the method

Round 2's lesson was *a declared population whose labels a human types will be wrong*. Round 3's is
narrower and about me: **I placed one guard three times and wrote three arms wrong, every one of them
by reasoning about the call graph instead of reading it.** Each correction cost a full suite run,
about ten minutes. Two of the four errors would have been caught in seconds by the checks the charter
already mandates — run the predicate over the real tree first (§7), and read the shape of the data
you are asserting on.

The cheap change is not more review. It is: before wiring a predicate, enumerate its real population
and print hits and near-misses; and before asserting on a row, print one.
