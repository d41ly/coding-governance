# DEPL-aTetheredConvoy-2 — update, the verb that moves an install forward

**Status:** CLOSED · rev-4 · 2026-08-20 · node a · Tier-2 · base 0f0a121d · streams deployer+tooling

## 1. Goal

Give `govkit` an `update` verb so a repo that adopted the kits can take a later gov commit without
hand archaeology. Today the deployer lands an install and has no way to move one forward, which makes
every adopting repo an upgrade orphan the moment gov commits again — and makes the receipt, which
already carries everything an update needs, a record nothing reads.

## 2. Scope (IN)

- **S1 — `update`, READ-ONLY by default.** `python tools/govkit/govkit.py update --target <path>`
  classifies every file the receipt records against a newer gov commit and prints the verdict table;
  `--write` performs it. The default is read-only because this verb's failure mode is silent data
  loss in a repository the operator owns and gov does not, and the muscle-memory invocation must not
  be the destructive one. `--to <rev>` overrides the default target commit of gov `HEAD`.
- **S2 — the per-file verdict, DERIVED from three blobs.** For each receipt row: `base` is the blob
  at the receipt's recorded commit, `theirs` is the blob at the new commit, `ours` is the bytes on
  disk. The verdicts ARE §4's table — no count of them is written here, because the fold that added
  the doubly-deleted row left a spelled figure behind describing the table before it. `ours` is compared against the receipt's recorded hash rather
  than against `base`, because for a `rendered` row those differ by construction.
- **S3 — roles gate which rows the table sees at all**, per §4's role table, and the role dispatch
  reads unit 1's frozen schema. A role whose receipt row unit 1 RESERVED but no unit has filled yet
  is refused by name rather than classified from an absent field.
- **S4 — a three-way merge for the diverged case, delegated.** `git merge-file` takes the three blobs
  positionally and is already this repo's structural merge primitive. A clean merge writes; a
  conflict leaves the file byte-identical, writes an order to `.governance/outbox/`, and reds.
- **S5 — a schema-1 receipt is read honestly.** Rows the receipt omits are reported `unrecorded` and
  never touched, and every schema-1 ROLE is treated as untrusted: unit 1 measured that a schema-1
  receipt stamps `engine` on a file its descriptor declares `project-owned`, so `update` re-resolves
  the role from the descriptor at the receipt's commit and refuses the row when the two disagree.
- **S6 — the dispatch is COMPLETE over BOTH enumerations, and a gate says so.** One `selfcheck` arm
  asserts every role in unit 1's frozen table has a row in `update`'s role dispatch; a second asserts
  every CELL of §4's two-comparison verdict grid has a verdict. Refusal counts as a row, silence does
  not. The second arm exists because the first structurally cannot see a missing grid cell — which is
  how rev-1 shipped a grid with no answer for a file deleted on both sides. Unit 6 fills `merged`, and
  reds this arm until it does.
- **S7 — the receipt is rewritten after a write**, recording what each row was before and after, so a
  rollback is the receipt's own inverse rather than a guess.

## 3. Non-goals (OUT)

- **Adding kits to an existing install.** `update` reports a registry entry the receipt does not
  claim as AVAILABLE and refuses to install it, naming the flag that would (`--add-kits`). Widening a
  target's governance surface is an owner decision, and the flag is named here so the refusal can
  point at it, not built here.
- **Removing a kit.** `remove` stays deferred. This unit's receipt reads make it mechanical later.
- **The copier-style three-way for living documents.** Re-rendering the OLD template with the saved
  answers to isolate local accretions is the right answer for a `rendered` artifact and is not this
  unit's: gov does not write those files, the adopters do. `update`'s answer for that role is to
  re-run the adopter and CAP the outcome at report — a rendered row never reaches `diverged` and
  never reaches `git merge-file`.
- **Migrating an existing install's wrong roles.** Unit 1 stops producing them; S5 refuses to act on
  one rather than reinterpreting it.
- **Updating gov-owned artifacts no unit has landed yet.** The `.gitattributes` pin block, the
  emitted gate legs and the CI workflow are `files` rows by unit 1's schema, so they become
  updatable when units 4 and 6 write them. Until then S6's arm reds and this unit refuses those roles
  by name.

**Assumes:** unit 1, in full. **Superseded in part by:** unit 6, which deletes the `merged` refusal
this unit carries and must fill the `merged` verdict row in the same diff.

## 4. Design

### The verdict table

All comparisons on sha256.

`theirs absent` is evaluated FIRST, as its own column-2 value, across every column-1 state. rev-1 put
it on the `equal` row only, which routed an edited-and-withdrawn file to `diverged` — contradicting
the prose below it — and sent a doubly-deleted file to `missing`, which would have tried to restore a
blob that does not exist.

| ours vs receipt | theirs vs base | verdict | `--write` action |
|---|---|---|---|
| equal | `theirs` absent | `withdrawn` | delete, and stage the deletion |
| differs | `theirs` absent | `patched` | leave untouched; REPORT — gov withdrew it and the target changed it |
| absent on disk | `theirs` absent | `converged` | nothing; both sides agree it is gone |
| equal | equal | `current` | nothing |
| equal | differs | `stale` | write `theirs` |
| differs | equal | `patched` | leave untouched; REPORT the path and both hashes |
| differs | differs | `diverged` | three-way; clean merge writes, a conflict leaves and reds |
| absent on disk | equal or differs | `missing` | restore `theirs` |
| in no receipt row | — | `unrecorded` | leave untouched; REPORT |

`withdrawn` is the only verdict that deletes, and it deletes only where `ours` still equals the
receipt. A file gov no longer ships that the target has since edited is `patched`, which is now a row
of the table rather than a sentence under it. Getting that backwards is how an updater destroys work
it did not write, and the asymmetry is why the verdict is derived from two comparisons rather than
one.

`unrecorded` conflates two states that are indistinguishable from inside the target — "gov wrote this
and the receipt lost the row" and "the target authored this at a path gov also uses" — and only one
of them is safe to touch. It is reported and never acted on.

### Roles

| role | behaviour | why |
|---|---|---|
| `engine` | the full table | gov owns the bytes |
| `seed` | never written; a moved template is REPORTED as a re-seed available | copied once, then owned |
| `project-owned` | never compared, and after unit 1's re-resolution NO receipt row carries bytes under it — so no loop is written over this role, only the absence assertion | gov supplied no bytes, so there is no `base` |
| `generated` | never compared | produced in the target |
| `rendered` | re-run the adopter, compare against the fresh render, CAP at report | gov does not write these; a second writer races the real one |
| `merged` | refused by name until unit 6 | no writer exists; a half-written region is worse than a named refusal |
| `attributes`, `gate-leg`, `ci` | refused by name until units 4 and 6 | reserved rows with no writer yet |

The cap on `rendered` is deliberate and was bought by the adversarial pass: the natural
implementation sends a rendered row down the full table, which means a target that edited its conf
gets a three-way merge run on an artifact its own adopter regenerates. That contradicts this unit's
own non-goal in the same document.

### The three-way

`ours`, `base` and `theirs` are `%A %O %B`. The row-keyed merge driver already hands its structure
lines to exactly this call, so the primitive is in-house, gated, and has a house record of how it
fails: a wrong argument order does not error, it emits a plausible file with one side's content
silently dropped. Every arm therefore asserts merged CONTENT, never the exit code.

### The refusals

Each is a named message with a positive and a negative arm:

- the receipt's recorded gov commit does not resolve in this checkout — name the commit and DO NOT
  fall back to treating the target as a fresh install. That fallback classifies every file `missing`
  and overwrites every local edit in the repository, which is the worst thing this verb can do.
- a kit the receipt claims is no longer a registry entry — named, because silently dropping it leaves
  its files owned by nobody.
- a receipt row whose descriptor-resolved role disagrees with the recorded one (S5).
- a role with no verdict row (S6).
- `--to <rev>` does not resolve.
- the target resolves to the gov checkout itself.

### Rollout

1. **The classifier and the read-only verb** — S1, S2, S3, S5, S6, the refusals and the report. Zero
   write risk, and usable against every existing install on day one to answer "how far behind is this
   target".
2. **`--write`** — S4's three-way, the conflict outbox, the staging, and S7's receipt rewrite.

### Files touched (estimate)

| Area | Files | Note |
|---|---|---|
| Core | `tools/govkit/govkit.py` | the classifier, the verb, the receipt rewrite |
| Tests | `tools/govkit/selftest.py` | one arm per verdict, plus the refusals and their negatives |
| Docs | `skills/deploy-governance/SKILL.md` | the verb, and the read-only default |
| Map | `memory/map/features/govkit.md` | a new seam |

### Alternatives rejected

**Make it a mode on `apply`.** Rejected: `apply`'s contract is "land what is not there" and its re-run
path already overwrites `engine` files without comparing. Folding a verdict table in means one
invocation is safe on a fresh target and destructive on a patched one, distinguished only by state the
operator cannot see at the prompt.

**Write by default with a `--dry-run`.** Rejected on blast radius.

**Write a three-way merge.** Rejected: `git merge-file` is on PATH by construction, takes the blobs
positionally, and is already the primitive the row driver delegates to.

## 5. Production-readiness checklist

- security — the first `govkit` verb that DELETES, bounded to a file gov shipped, gov no longer ships,
  and whose bytes still equal what gov wrote. Read-only by default.
- perf / scale — two `git show` per row; one target.
- a11y — N/A: a command-line tool.
- i18n — N/A: developer tooling.
- error / empty / loading states — the verdict table IS this line; the two verdicts meaning "I cannot
  tell" report rather than act.
- observability — the printed table read-only, the rewritten receipt and the conflict outbox on write.
- risks — data loss in a repo gov does not own is the whole surface, bounded by the read-only default,
  by no action on any verdict meaning the target changed it, and by deletion gated on byte-equality.
  Second: a schema-1 receipt's roles are untrusted, which makes `update` refuse rows on old installs —
  loud, and the correct direction. Third: the three-way argument order, whose wrong form emits a
  plausible file, which is why §6 asserts content.
- testing + left-shift gates — one arm per verdict with a fixture that provably reaches it; every
  refusal with a negative arm.
- migration / rollback — rollback of an `update --write` is bounded by the receipt it rewrote, which
  names every path it touched and the hash each had before.
- user docs — the Skill.

## 6. Acceptance criteria

- **AC1** When `python tools/govkit/govkit.py update --target <fixture>` runs against an install
  whose gov commit has moved, it prints one verdict per receipt row and writes nothing — asserted by a
  `git status --porcelain` snapshot taken before and after being byte-identical, and by no new path
  under `.governance/`.
- **AC2** When an unmodified `engine` file's gov copy has moved, `update --write` writes it and the
  file's sha256 equals `git show <new_commit>:<source>`. Verdict `stale`.
- **AC3** When an `engine` file has been edited locally and gov's copy has NOT moved, `update --write`
  leaves it byte-identical and names it `patched` with both hashes. Nothing else observes the
  no-clobber guarantee.
- **AC4** When an `engine` file has been edited locally AND gov's copy moved compatibly,
  `update --write` produces a file containing BOTH changes. The assertion is on CONTENT, never on the
  `git merge-file` exit code — a reversed argument order emits a plausible file and exits 0.
- **AC5** When that three-way conflicts, the target file is byte-identical to before, an order under
  `.governance/outbox/` names the path and all three hashes, and `update` exits non-zero.
- **AC6** When gov no longer ships a recorded file and the target's copy is unmodified,
  `update --write` deletes it and stages the deletion; when the copy IS modified, the file survives
  and is named `patched`. Both halves in one arm — the asymmetry is the criterion.
- **AC7** When the receipt's recorded commit does not resolve, `update` refuses before reading the
  target's files and NAMES that commit. Negative arm: the same fixture with a resolvable commit does
  not refuse.
- **AC8** When the registry has gained an entry the receipt does not claim, `update` reports it
  available and names `--add-kits`, and `update --write` leaves the receipt's `kits` list unchanged.
- **AC9** When `python tools/govkit/govkit.py selfcheck` runs, it reds if any role in unit 1's frozen
  role table has no row in `update`'s dispatch. Liveness: removing one row from the dispatch reds the
  arm, and a refusal row satisfies it while silence does not.
- **AC9b** When one CELL is removed from §4's verdict grid, `python tools/govkit/govkit.py selfcheck`
  reds naming the missing (ours, theirs) pair. The role arm structurally cannot see this — which is
  how the grid shipped with no answer for a file deleted on both sides.
- **AC9c** When a recorded file is deleted BOTH in the target and at the new gov commit,
  `update --write` reports `converged`, writes nothing, and never attempts a restore — asserted on the
  target's bytes and on the absence of any new path, not on the printed word alone.
- **AC10** When `update` runs against a schema-1 receipt, every installed file the receipt omits is
  reported `unrecorded` and none is written, deleted or merged — asserted on the on-disk bytes of a
  fixture whose receipt had a `seed` row deliberately dropped. And a row whose descriptor-resolved
  role disagrees with the recorded one is REFUSED by name, asserted against a fixture reproducing
  unit 1's measured `project-owned`-stamped-`engine` state.
- **AC11** When a `rendered` row's artifact differs from the receipt, `update` re-runs that kit's
  adopter and reports the outcome; it never invokes `git merge-file` on a rendered path, asserted by
  the absence of any conflict order and by the file matching a fresh render.
- **AC12** When `python tools/govkit/selftest.py` runs, every refusal message this unit adds is
  asserted by name and each carries a negative arm proving it does not fire on the authorized path.

## 7. Gates

`bash tools/run-gates.sh` green at the push boundary. No new leg — the arms ride `govkit selftest`,
and unit 3's deployability leg grades the verb's own fixtures once it lands.

The kit version constant moves.

Before review: `python tools/memory-tree/gotchas.py --for-diff 0f0a121d..HEAD`. The
`heredoc-escape-reaches-the-regex` class is live here: the conflict-order writer emits hashes and
paths through shell in at least one arm.

## 8. Open questions

none — the forks below are RESOLVED. Authority: the owner's instruction to execute this build
delegates resolver authority for THIS build only, and every fork here is one the spec already stated,
which is exactly M3's condition. Each was taken through M3's veto order; none was discarded by a veto,
and the two that touch a write or security surface are called out in the wrap-up as owner-review items
rather than treated as settled by silence.

- **F1 — does `update --write` stage what it writes?** RESOLVED (agent, 2026-08-16, delegated): yes,
  matching `apply`. Every gate in this suite reads the index, so an unstaged update is invisible to the
  verification that follows it, and the deletion half must be staged or the target's next commit
  silently resurrects the file.
- **F2 — refuse on uncommitted changes anywhere, or only in the paths it will touch?** RESOLVED
  (agent, 2026-08-16, delegated): only in the paths it will touch, named individually. A whole-tree
  cleanliness demand makes the verb unusable in exactly the situation it is for.

## 9. Revision log

- rev-4 · 2026-08-16 · folded the scoped fold re-audit. The previous fold added a verdict row and a
  completeness arm and gave neither an acceptance criterion — the only two things it added to this
  unit were the only two nothing graded. Both have one now. A spelled verdict count left over from
  before the new row is deleted, and the role table records that `project-owned` has no
  byte-carrying instance after unit 1's re-resolution, so no loop is written over it.
- rev-3 · 2026-08-16 · folded the M4 spec audit. The verdict grid had `theirs absent` as a value on
  ONE row, so an edited-and-withdrawn file routed to `diverged` against the prose below it, and a file
  deleted on both sides routed to `missing` — a restore of a blob that does not exist. It is now a
  column evaluated first, across every state, with a named no-op verdict for the doubly-deleted case.
  S6's completeness arm gained the verdict grid alongside the role enum, because an arm quantifying
  over roles structurally cannot see a missing grid cell, and an obligation assigned to unit 5 that
  unit 5 never took was struck.
- rev-2 · 2026-08-16 · M3 fork sweep: F1 and F2 resolved in place under the owner's
  execute-the-build delegation. No veto fired.
- rev-1 · 2026-08-16 · split out of the first unit's rev-1, which bundled this verb with the
  convergence ratchet and the prerequisite repairs. The split was forced by an adversarial pass that
  found the combined scope re-deciding four shared facts. Two design changes came out of that pass
  and are folded here rather than deferred: the `rendered` role is CAPPED at report, because sending
  it down the full table contradicted this unit's own non-goal; and every role gets a dispatch row
  with a completeness arm, because the units that add roles would otherwise leave them behind
  silently.

## 10. Reuse audit

Ran `python tools/codebase-map/reuse_lookup.py` for the update classification and the
local-modification refusal. It returned `govkit.py`'s own symbols and no external seam for the
classifier, which is the honest answer — the verdict table is new.

`blob_at` is already "bytes from the gov index at a recorded commit, never the working tree", which is
exactly what `base` and `theirs` are; `update` calls it twice per row rather than reaching for
`git show` again.

`git merge-file` is the three-way, and the seam proving it is house-native is the row-keyed merge
driver, which hands its own structure lines to that call positionally. The lookup surfaced that
driver's duplicate-detection helper as a candidate and it is REJECTED: it is a keyed merge over a ROW
grammar, and an engine file is arbitrary text with no key. What transfers is the delegation, not the
driver.

Unit 1's resolver is reused unchanged for S5's role re-resolution — re-deriving the role inside
`update` would be a second spelling of precedence.

`make_target` in the selftest is the fixture builder; every arm here is a variation on it.

No seam exists for the conflict-order writer, and it follows the outbox's existing one-order-per-file
convention rather than deciding a second one.
