# Acceptance ledger — DEPL-dCarriedReceipt-13, `govkit adopt` and the receipt bootstrap

**Serves:** journal DEPL-dCarriedReceipt-13

Built on node `a` under session slug `aResumedRelay`, resuming the unattended run that stopped at ten
of fifteen units. Every observation below was made against the merged tree, after `origin/main` came
in — not against the vintage the spec was written on.

**Evidences:** DEPL-dCarriedReceipt-13
- AC1 — `python tools/govkit/govkit.py adopt --target <t>` — RED observed FIRST, before a line of
  this unit existed: exit **2**, `govkit: unknown subcommand 'adopt'`, printed from `main`'s
  fall-through. GREEN afterwards, and what survives the RED is the JOIN that keeps it green
  honestly: three arms assert `adopt` is in `USAGE`, in `main`'s dispatch tuple, and that the module
  docstring no longer spells a verb COUNT beside either. The docstring said "all five verbs" and had
  been wrong since the sixth landed.
- AC2 — `tools/govkit/selftest.py` — a run without `--write` exits 0, `install.json` does not exist
  afterwards, `git status --porcelain` in the target is empty, and the output carries `READ-ONLY`
  rather than looking like a run that worked.
- AC3 — `tools/govkit/selftest.py` — over a target holding gov's bytes at `--to`, the row records
  `carry: "verbatim"`, `gov_oid == oid`, and `evidence: "vintage-match"` rather than `"apply"`.
- AC4 — `tools/govkit/selftest.py` — THE INVERSION GATE, in three arms plus a standing predicate.
  The relocated row proves the `relocate` rung; its `gov_oid` equals `git -C <gov> rev-parse
  <commit>:<src>`; and it does NOT equal `git -C <target> rev-parse :<path>`. The write half runs on
  its own fixture, where the source never moved between the two waves, so an `update --write` to the
  ADOPTED vintage leaves that path out of `git status --porcelain` entirely. Split onto a second
  fixture deliberately: on the ladder fixture gov DID move that file, so a no-write assertion there
  would have been about gov standing still rather than about the rung.
- AC5 — `tools/govkit/selftest.py` — rung-major, on a fixture whose newest commit matches only at
  `relocate` while the older matches `verbatim`. The written row's `commit` is the older sha and its
  `carry` is `verbatim`. Recency-major would pick the newer one, which is the arm's whole point.
- AC6 — `tools/govkit/selftest.py` — a destination matching no gov vintage records
  `evidence: "unattributed"`, carries neither `commit` nor `gov_oid`, KEEPS the role its rule
  declared (`engine`, asserted by name so a collapse back into `forked` reds), and the run exits 0.
  A following `update` prints the row and skips it before `classify_row`; `update --write` leaves its
  bytes byte-identical.
- AC7 — `tools/govkit/selftest.py` — `--pin <path>=<rev>` records `evidence: "pinned"` at the commit
  the operator named, with gov's blob there, and NO `carry`: the pin fixes the base and never the
  proof. Three refusal arms beside it — a `--pin` with no `=`, one naming an unresolvable revision,
  and one naming a revision where gov holds no blob for that source.
- AC8 — `tools/govkit/selftest.py` + `python tools/govkit/refusal_join.py` — all three refusals fire
  by name: `--target` resolving to the gov checkout, an existing receipt without `--re-adopt`, and a
  target index differing from HEAD. A fourth arm holds the WIDTH that §8 F1 chose: an UNSTAGED edit
  does NOT refuse. `--re-adopt` is asserted to release exactly the receipt refusal and nothing else.
  `refusal_join.py` enumerates 197 branches, and `BRANCH_PIN` moved 190 → 197 with both values named
  in its own header, 7/7 of the new branches armed.
- AC9 — `tools/govkit/selftest.py` — THE ROLE BINDING. A descriptor-declared `forked` source whose
  target copy is byte-identical to gov's blob at an older commit adopts as `role: "forked"`, carrying
  the rule's `direction` and `record`, with the matching commit recorded beside it as evidence and
  acted on by nothing. `update --write` writes ZERO bytes to that path, asserted on the bytes rather
  than on the printed word. Left-shifted as a standing predicate over the WHOLE receipt: the set of
  rows written `forked` equals the set of destinations whose rule declares it.
- AC10 — `tools/govkit/selftest.py` — the envelope carries `schema`, `gov_source`, `gov_commit`,
  `prefix`, `kits`, `files` and NONE of `orders`, `baseline`, `after`, `hook_block`, `gate_runner`.
  The absent set is asserted as hard as the present one. `gov_commit` equals the resolved `--to`;
  `install.sums` is non-empty and holds one line per `sha256`-carrying row; and `check` joins the two
  at the same N, greater than zero, read off its own `sidecar:` note.
- AC11 — `tools/govkit/selftest.py` — the envelope is LIVE. Immediately after `adopt --write`, an
  `update --to <older sha> --write` refuses at exit 2 and names BOTH shas, which is `-12` S7 firing
  against a `gov_commit` this verb wrote. S10's absent-optional-keys arm sits beside it: the same
  receipt classifies with no traceback.
- AC12 — `tools/govkit/selftest.py` — the needle map exists at bootstrap, derived per S4a from the
  planned `(src, dest)` pairs. The arm reads the printed pair and needle counts and asserts the
  needle count is exactly twice the pair count, with the CONDITION stated in the arm: every surviving
  gov directory in this fixture carries a slash, so its `/` and `~` forms differ. That condition is
  the arm's, not a law — `-9`'s own parked decision is about a population where it does not hold, and
  this ledger does not inherit the 26-needle figure. The dropped-ambiguous-directory printer is in
  the engine and prints one line per drop naming it; no shipped or fixture descriptor in this tree
  produces such a directory, so that printer is UNARMED and this line says so rather than implying
  coverage.
- AC13 — `tools/govkit/selftest.py` — on a fixture declaring one `[[lf_pin]]` and one merged rule,
  the receipt carries exactly one `attributes` row at `.gitattributes` and one `merged` row carrying
  the `block_id` `check` reads, both in `apply`'s own shapes. Neither carries `gov_oid`, `oid` or
  `evidence`, asserted directly. `check --target` completes with no `KeyError` on `row['block_id']`.
- AC14 — `tools/govkit/selftest.py` — S7's scoping in BOTH directions, on a receipt carrying an
  unattributed `seed` row and the synthesized `attributes` row. Both dispatch through `UPDATE_ROLE`
  rather than being swallowed: the seed row reaches its reseed override, the attributes row reaches
  `-2`'s pins arm, and neither writes a byte. This is the arm that would red under a skip scoped by
  field absence, or by anything wider than the `table` disposition.

## The verb run against a REAL adopter, which no fixture substitutes for

Node `a` reaches both live adopter checkouts and node `d` did not, so this is evidence the unit's
own build could not have produced. Read-only against `C:/projects/nicocares/main` first: **155 rows
would be recorded**, the target's `git status --porcelain` stayed empty afterwards, and no
`install.json` appeared — AC2's promise, kept on a repository gov does not own.

Then `--write` against an INDEX-ONLY MIRROR of that repository, built with
`git clone --shared --no-checkout` from its real gitdir plus `read-tree HEAD`, so the receipt could
be inspected without a byte reaching the live tree. **Nothing was written into
`C:/projects/nicocares`.** Over the resulting 155-row receipt:

- **The inversion gate, over 125 real rows carrying `commit` and `gov_oid`: ZERO mismatches.** Every
  one equals `git rev-parse <commit>:<source>` in gov. This is AC4's standing predicate measured on
  an adopter rather than on a fixture, and it is the field the entire unit's safety rests on.
- **Carried rows whose two identities AGREE: ZERO.** The raw-write arm is closed exactly where it
  must be.
- **`evidence` came out 125 `vintage-match`, 29 `unattributed`, 1 ABSENT** — and the one absence is
  the synthesized `attributes` row, which is precisely the class S11 says carries no `evidence`. The
  four-states-plus-absence model, observed rather than asserted.
- **`role` came out 133 `engine`, 9 `rendered`, 7 `seed`, 3 `forked`, 2 `project-owned`, 1
  `attributes`.** The three `forked` rows are the descriptor's claim, carried through a walk that
  found matches for other rows in the same run.
- **`install.sums` holds 154 lines against 154 rows carrying `sha256`.** The filter agrees on both
  sides, and the single row without one is the `attributes` row — exactly the split S5 states.
- **The 29 unattributed rows are GENUINE, not a walk failure.** Five were sampled and each was asked
  the question directly: does the target's index blob equal gov's blob at ANY commit in that path's
  own history? All five: NONE, over histories of 8 to 108 commits. The liveness control ran the same
  question against an attributed row and got an exact match. So partial attribution proceeded, each
  unattributable row took its own state, and no base was invented for any of them — which is §3's
  non-goal and AC6's behaviour, on a real tree.

## Two things found while building, neither of them this unit's

- **`-14`'s AC8 arm was pinned to a MOVING REF and had gone vacuous.** It fetched
  `HEAD:tools/govkit/govkit.py` and asserted `def run_kit_check` was absent from it — true for
  exactly as long as `-14` was unlanded, and false from the commit that landed it. Fixed in place by
  pinning `af9421d7`, `-14`'s parent, with the reason written beside it. It is the playbook's
  moving-ref class, met at the one place it is easiest to miss: the ref that moved was the one the
  unit was landing onto.
- **`tools/govkit/check_runbook_parity.py` reports 18 problems, and reported the same 18 on
  `origin/main` before this unit touched anything.** Registry entries with no anchored runbook
  section. It is NOT a gate leg — `tools/gate-legs.json` names it nowhere — so nothing was red and
  nothing became red. Recorded because a checker that reports and is not gated is one nobody reads.
