# DEPL-aTetheredConvoy-1 — the update verb, and the ratchet that keeps the kit converged

**Status:** OPEN · rev-1 · 2026-08-16 · node a · Tier-2 · base 0f0a121d · streams deployer+tooling

## 1. Goal

Give `govkit` an `update` verb, so a repo that adopted the kits can take a later gov commit without
hand archaeology; and close the convergence gap underneath it, so a new moving part in this repo
cannot ship without being deployable, updatable and gated. The deployer today lands an install and
has no way to move one forward, which makes every adopting repo an upgrade orphan the moment gov
commits again.

## 2. Scope (IN)

- **S1 — `update`, a sixth verb, READ-ONLY by default.** `python tools/govkit/govkit.py update
  --target <path>` classifies every file the receipt records against a newer gov commit and prints
  the verdict table; `--write` performs it. The default is read-only because this verb's failure mode
  is silent data loss in a repository the operator owns and gov does not, and the muscle-memory
  invocation must not be the destructive one. `--to <rev>` overrides the default target commit of gov
  `HEAD`.
- **S2 — the per-file verdict, DERIVED from three blobs and never declared.** For each receipt row:
  `base` is the blob at the receipt's recorded commit, `theirs` is the blob at the new commit, `ours`
  is the bytes on disk. The six verdicts and their actions are §4's table. Roles gate which files the
  table applies to at all.
- **S3 — a three-way merge for the diverged case, delegated rather than written.** `git merge-file`
  takes the three blobs positionally and is already this repo's structural merge primitive:
  `tools/memory-tree/merge-rows.py` hands its own structure lines to exactly that call. A conflict
  leaves the file untouched, writes an order to `.governance/outbox/`, and reds.
- **S4 — receipt schema 2, and a reader that accepts schema 1 honestly.** Schema 2 carries a
  `schema` field, a per-file `version` (the kit's version constant at install), and a row for every
  file gov is responsible for rather than only those a given run wrote. A schema-1 receipt is read
  by re-deriving the expected file set from the descriptors at the receipt's own commit and marking
  anything the receipt omits as `unrecorded` — reported, never touched. A receipt that lost rows is
  not a receipt that says the target has fewer files.
- **S5 — `plan` and `apply` share ONE file-set expansion.** The function that turns a descriptor's
  file rules into destinations is called by both, so `plan`'s rows are `apply`'s rows by construction
  rather than by two implementations agreeing. `plan` marks a role `apply` cannot land as `SKIP`
  with the reason, never as `write`.
- **S6 — the `playbook` entry's file rules are retagged `seed`.** Gov supplies those bytes once and
  the target owns them afterwards, which is what `seed` means and is not what `project-owned` means.
- **S7 — leg correspondence, both directions.** Every `[[gate_leg]]` a descriptor declares names a
  leg that exists in `tools/gate-legs.json`; every leg in that manifest is claimed by exactly one
  descriptor's `[[gate_leg]]` or carried by a new `[[exempt_leg]]` row in `registry.toml` with a
  non-empty reason, and an `[[exempt_leg]]` naming a leg that no longer exists reds. This is the
  same shape and the same staleness rule as the existing path exemptions.
- **S8 — version correspondence becomes a FAILURE.** The `5b` cross-check between each descriptor's
  `version_from` and `tools/check-kit-versions.sh`'s `need` list is a problem rather than a note in
  both directions. `version_from` accepts a LIST of tables, because one entry versions three files.
  A constant claimed by no entry is carried by an `[[exempt_version]]` row with a reason, on the
  same staleness rule.
- **S9 — per-file claim inside a kit home.** Every tracked file under an entry's `home` is matched
  by at least one of that entry's file rules. Derived from `git ls-files`; no new population.
- **S10 — the surface widens to `skills/*`.** `skills/deploy-governance/` becomes an exemption
  carrying its reason. A future skill then reds until a declaration claims it, which is the state
  every other tracked deployable surface is already in.
- **S11 — the deployability leg.** One new gate leg drives `plan` and two `apply` runs for EVERY
  registry entry into a hermetic `mktemp -d` fixture and asserts three things per entry: an entry
  declaring a landable role lands at least one byte; `plan`'s promised destination set equals the
  receipt's path set; and the second `apply` changes no path and no hash. Every other arm in this
  unit is a declaration compared against a declaration. This one executes the product.
- **S12 — the repairs the correspondence arms surface at base**, which are small and are listed in
  §4 rather than discovered by the builder: two version constants absent from the gate's list, three
  constants no entry claims, and one prose count inside the file whose own header bans prose counts.

## 3. Non-goals (OUT)

- **Finishing the deployer.** The gate-runner and CI leg emitter, the `.gitattributes` block writer
  and its renormalize, and the `merged` role all stay unbuilt and stay REPORTED on every run. They
  are named on every `apply` today, which is the honest state; widening this unit to close them
  would bury both halves of what the owner asked for.
- **`remove`, and fleet fan-out.** Both were deferred by the deployer unit and stay deferred. This
  unit's receipt work is what makes `remove` mechanical later — the inverse of a complete receipt —
  and that is the whole of its contribution to them.
- **The copier-style three-way for living documents.** The research designs re-rendering the OLD
  template with the saved answers to isolate local accretions before replaying onto the new render.
  That is the right answer for `rendered` artifacts and it is not this unit's: gov does not write
  `rendered` files at all — the ADOPTERS do — so `update`'s answer for that role is to re-run the
  adopter and compare, and a spec that half-designs the copier path would ship a second renderer
  racing the real one.
- **Adding kits to an existing install.** `update` reports a registry entry the receipt does not
  claim as AVAILABLE and refuses to install it. Widening a target's governance surface is an owner
  decision, and the flag that would do it (`--add-kits`) is named here so the refusal can point at
  it, not built here.
- **Extending `check-arms.py` to a Python population.** Already an open backlog row from the
  deployer unit, already reserved for the owner as a governance-carrier change, and this unit's new
  refusals ride the existing test-layer guarantee instead.
- **Repairing what the correspondence arms find beyond S12's list.** S12's repairs are the ones
  measured at base and needed to make the new arms green. If turning an arm on surfaces a
  disagreement this spec has not named, it is a backlog row: a unit that repairs whatever its own
  new gate happens to find has no bounded diff.

## 4. Design

### What is actually wrong today, measured

Each finding below was reproduced against the tree at base, most by driving `govkit` end to end into
a throwaway repository. They are ordered by what they cost.

**A1 — the descriptors and the leg manifest are two spellings of one fact, unasserted.** Reproduce
with a read of both populations: descriptor `[[gate_leg]]` names against the `name` keys in
`tools/gate-legs.json`. Measured at base: seven declared leg names exist in no manifest leg at all,
and the large majority of manifest legs are claimed by no descriptor — including legs a target that
takes the kit plainly must receive, such as the memory-tree engine's own self-tests, the codebase-map
adopter end-to-end, the unattended kit's three, and the flat gates'. The deployer spec's AC10
specified the descriptor-to-manifest direction of this check. Neither direction exists in
`selfcheck`; arm `7c` reads the manifest only to classify guard pathspecs. The consequence is latent
rather than active only because the leg emitter is unbuilt — the moment it is built, it emits from a
population nothing has ever validated.

**A2 — `plan` does not promise the file set `apply` produces.** Driven into a fixture with the
default selection: `plan` reported eleven writes; `apply` reported fifty-six landed files. The two
numbers are not even in the same units — `planned_writes` emits one row per file RULE, so a rule
whose include is `**` is one row, while `apply` expands the same rule over `git ls-files`. Worse,
`plan` marks a role `apply` cannot land as `write`: six of the seven destinations it named as writes
were never written and appear in no receipt, including the playbook's own destination and every
`rendered` artifact. AC11 of the deployer spec has no satisfying assignment against this code.

**A3 — the `playbook` entry, in the DEFAULT set, lands zero bytes.** Both of its file rules carry
`role = "project-owned"`. The role table defines that as "the target authors it; gov never supplies
the bytes", and the apply layer has no code path that writes one — deliberately, and correctly for
the role. But gov DOES supply the playbook: the runbook copies the template to an owner-chosen path
and the target then fills its placeholders. That is the `seed` row of the same table, distinguished
from `project-owned` by exactly the column the deployer spec added at rev-7 to tell them apart.
Measured: after an `apply` of the default set, neither playbook file exists in the target and the
`playbook-placeholders` hole probes two paths nothing wrote.

**A4 — the receipt is not a stable inventory.** Two identical `apply` runs, no gov change between
them, produced fifty-seven receipt rows and then fifty-six. The cause is one line: a `seed` file is
skipped when its destination exists, and the receipt is serialized from the write log rather than
from the resolved file set. So a `seed` row is present after the first run and gone after the
second. Every consumer that treats the receipt as the statement of what gov put in the target — this
unit's `update`, the deferred `remove`, and the deployer spec's own AC2 — is reading a record that
shrinks when nothing changed.

**A5 — the receipt records no kit version.** S4 of the deployer spec requires "role, sha256, kit id
and version". The implementation records `path`, `role`, `kit`, `sha256`, `source`, `commit`. There
is no version anywhere in the file. Without it there is no version-gated migration and no per-kit
verdict that does not re-derive everything from gov.

**A6 — the version cross-check is a note, so a disagreement lives at exit 0.** `selfcheck` exits 0
today while reporting five disagreements between the registry's version claims and the repo's own
version gate. That is the correct behaviour for a check the deployer unit declared out of scope to
REPAIR — and it is the wrong behaviour for a ratchet, because a new kit whose version constant no
entry claims is then invisible.

**A7 — a new file inside a kit with explicit includes is claimed by nothing.** The surface predicate
is depth-1 under `tools/`, so a file added inside an existing kit directory collapses to the
directory, which is already claimed. Entries whose include is `**` cover it; entries with a literal
include list do not. Measured at base the exposure is one file, which is small and is not the point:
the predicate that would catch the next one does not exist.

**A8 — `skills/*` beyond the kickoff tree is outside every assertion.** The surface globs name
`skills/session-kickoff/**` specifically. A second skill directory is already tracked and is in no
entry, no exemption and no inventory the ratchet reads.

**A9 — `check` cannot report a copy-only kit as adopted.** The state defaults to
`landed-but-inert` and is only lifted by a `check.argv` the entry declares. Two entries in the
default set declare none, so they are reported inert forever. "Inert" is a verdict about a kit that
failed to configure; a kit with nothing to configure has not failed.

**A10 — a count in prose, inside the file whose header bans counts in prose.** One exemption reason
in `registry.toml` states the size of gov's leg manifest. The manifest has grown since. The file's
own header explains why no count belongs in it.

### The verdict table — `update`'s whole mechanism

Three blobs per receipt row. `base` is `git show <receipt_commit>:<source>`, `theirs` is
`git show <new_commit>:<source>`, `ours` is the bytes at the destination in the target. All three
comparisons are on sha256, and `ours` is compared to the receipt's recorded hash rather than to
`base` — the receipt's hash is what gov actually wrote, and for a `rendered` or future `merged` row
those differ by construction.

| ours vs receipt | theirs vs base | verdict | `--write` action |
|---|---|---|---|
| equal | equal | `current` | nothing |
| equal | differs | `stale` | write `theirs` |
| equal | `theirs` absent | `withdrawn` | delete, and stage the deletion |
| differs | equal | `patched` | leave untouched; REPORT the path and both hashes |
| differs | differs | `diverged` | three-way; clean merge writes, a conflict leaves and reds |
| absent on disk | any | `missing` | restore `theirs` |
| in no receipt row | — | `unrecorded` | leave untouched; REPORT |

`withdrawn` is the only verdict that deletes, and it deletes only where `ours` still equals the
receipt — a file gov no longer ships that the target has since edited is `patched`, not `withdrawn`.
Getting that backwards is how an updater destroys work it did not write, and the asymmetry is the
whole reason the verdict is derived from two comparisons rather than one.

`unrecorded` exists for schema-1 receipts, where A4 means a row can be missing from a file that is
nonetheless installed. It is reported and never acted on, because the two states it conflates —
"gov wrote this and the receipt lost the row" and "the target authored this at a path gov also
uses" — are indistinguishable from inside the target, and only one of them is safe to touch.

### Roles gate which rows the table sees at all

| role | `update` behaviour | why |
|---|---|---|
| `engine` | the full table | gov owns the bytes; this is the base case |
| `seed` | never written; a moved template is REPORTED as a re-seed available | copied once, then owned. Overwriting is the failure the role exists to prevent |
| `project-owned` | never compared | gov never supplied the bytes, so there is no `base` to compare against |
| `generated` | never compared | produced in the target |
| `rendered` | re-run the kit's adopter, then compare the output against the receipt hash | gov does not write these; the adopter does, and a second writer would race it |
| `merged` | refused by name, as `apply` already refuses it | no writer exists anywhere in this repo, and a half-written region is worse than a named refusal |

### The three-way is `git merge-file`, not new code

`ours`, `base` and `theirs` are exactly `%A %O %B`. `tools/memory-tree/merge-rows.py` already hands
its structure lines to `git merge-file` positionally for precisely this reason, so the primitive is
in-house, gated, and has a house record of how it fails. `update` writes the three blobs to a scratch
directory, calls it, and takes the result only on a clean exit. A conflicting merge leaves the target
file byte-identical and writes `.governance/outbox/update-conflict-<kit>-<n>.md` naming the path and
all three hashes.

The argument order trap is recorded in this repo's own manifest as an environment trap: a wrong
order does not error, it emits a plausible file with one side's content silently dropped. The arms
in §6 therefore assert the merged CONTENT, never the exit code.

### The refusals, each of which is a named message

`update` refuses, before reading anything further, when:

- the receipt's `gov_commit` does not resolve in this checkout. It names the commit and does NOT
  fall back to treating the target as a fresh install — that fallback would classify every file as
  `missing` and overwrite every local edit in the repository, which is the single worst thing this
  verb can do.
- a kit the receipt claims is no longer a registry entry. Named, because silently dropping it leaves
  its files in the target owned by nobody.
- a descriptor in the update set declares a `merged` rule. The same refusal `apply` already carries,
  reached from a second entry point.
- `--to <rev>` does not resolve.
- the target resolves to the gov checkout itself.

And it REPORTS, without refusing, a registry entry the receipt does not claim, naming `--add-kits`
as the flag that would install it and stating that this verb does not.

### The convergence ratchet: four correspondences and one execution

The owner's question is what forces a NEW moving part to ship govkit-ready. The tempting answer is
more declarations to keep in sync, and it is wrong for the reason this whole tool exists: each new
declaration is another spelling of a fact somebody else already wrote. Four of the five arms below
therefore assert a correspondence between populations that ALREADY exist and add nothing new to
maintain; the exemption tables they need are the minimum, because deployability is not derivable
from the thing being exempted. The fifth arm does not compare declarations at all.

**R1 — legs, both directions** (S7). Descriptor-to-manifest catches a leg renamed in one place. The
reverse direction is the one that enforces the owner's ask: a leg added to `tools/gate-legs.json`
reds `selfcheck` until a descriptor claims it or an `[[exempt_leg]]` row explains why a target does
not get it. The exemption is a new population and it is unavoidable — nothing in a leg's own row
says whether an adopter should receive it — but it carries the same reason requirement and the same
staleness rule as the path exemptions, so a stale one reds rather than quietly widening the surface.

**R2 — versions, both directions, as failures** (S8). No new population beyond the exemption rows,
because both sides already exist. `version_from` becomes a list of tables so an entry can claim more
than one constant, which one entry measurably needs.

**R3 — files inside a kit home** (S9). No new population at all: `git ls-files` under `home` against
the union of the entry's own include rules. This is the arm that catches A7.

**R4 — the surface widens** (S10). One glob and one exemption row.

**R5 — deployability, executed** (S11). For every registry entry: a hermetic fixture, `plan`, two
`apply` runs, three assertions. It is the only arm that would have caught A2 and A3, and neither of
those is subtle — the playbook has been in the default set landing nothing. A descriptor that parses
and deploys nothing is indistinguishable from one that works, from the outside, which is the sentence
`govkit.py`'s own module docstring opens with. That sentence is now true of `govkit`.

The answers R5 needs per entry come from `needed_answers()`, which is already derived from the
descriptors rather than hand-kept, so a kit that starts needing a new token does not silently make
this leg unrunnable. Entries whose adopter is expected to fail — the blocking hole in the default
set is the known one — are asserted on the LAND phase only; `apply` already separates the two.

**Every one of the five carries a liveness arm.** An assertion that finds nothing on a clean tree is
indistinguishable from one that cannot find anything, and this repo names that class. The existing
`selftest.py` already builds a scratch gov tree and feeds it input that must red; each new arm gets
the same pair, and R5's negative fixture retags a landable rule to `project-owned` and asserts the
leg reds — which is A3 reproduced deliberately.

### The repairs S12 carries

Measured at base by running `python tools/govkit/govkit.py selfcheck`, which reports all five as
notes today:

- the playbook's template marker and `tools/check-wiring.sh`'s constant are absent from
  `tools/check-kit-versions.sh`'s `need` list; two rows added.
- the two drift-audit workflow scripts' version constants are claimed by no entry; the
  `review-harness` entry claims them, which is what `version_from` becoming a list is for.
- `govkit.py`'s own constant is claimed by no entry and cannot be, because the deployer is a
  registry exemption; an `[[exempt_version]]` row states that rather than leaving it a permanent
  note.
- the prose count in one exemption reason is removed (A10).

### Rollout

Four commits, each independently green and independently useful.

1. **The correspondence ratchet** — R1 through R4, the S12 repairs, and their liveness arms. No
   deployer behaviour changes. Immediate value as the convergence gate, and it is the commit that
   answers the owner's second question on its own.
2. **The truthful plan and the truthful receipt** — S5, S6, S4's schema 2, A9's third state, and R5
   with its fixture. This is the commit `update` cannot be built without: a verb that reasons about
   what gov installed needs a record that does not shrink, and a preview that promises what the
   writer performs.
3. **`update`, read-only** — S2's classifier and the verdict table, the schema-1 reader, the
   refusals and the report. Zero write risk, and usable against every existing install on day one to
   answer "how far behind is this target".
4. **`update --write`** — S3's three-way, the conflict outbox, the staging, and the receipt rewrite.

### Files touched (estimate)

| Area | Files | Note |
|---|---|---|
| Core | `tools/govkit/govkit.py` | the classifier, the shared expansion, the schema-2 writer |
| Registry | `tools/govkit/registry.toml` | two new exemption tables, one surface glob, one prose repair |
| Descriptors | the entries whose legs, versions or roles move | the count is DERIVED by `selfcheck`, and is deliberately not written here |
| Version gate | `tools/check-kit-versions.sh` | two `need` rows; it is a `seed`, so adopters re-seed rather than inherit |
| Tests | `tools/govkit/selftest.py`, a new deployability harness | every new arm plus its liveness pair |
| Gates | `tools/gate-legs.json`, `AGENTS.md` | one new leg, cited in the charter |
| Map | `memory/map/features/govkit.md` | new gate-leg claim, new seams, the Gaps section shrinks |

### Alternatives rejected

**Make `update` a mode on `apply`.** Cheaper by one verb and rejected: `apply`'s contract is "land
what is not there", and its re-run path already overwrites `engine` files without comparing. Folding
a verdict table into it means the same invocation is safe on a fresh target and destructive on a
patched one, distinguished only by state the operator cannot see at the prompt.

**Make `update` write by default, with a `--dry-run`.** Rejected on blast radius. Every other verb
here is either read-only or explicitly named `apply`; a verb whose default action rewrites files in
somebody else's repository should not be the one reached by typing its name.

**A lockfile separate from the receipt.** The research proposed one. Rejected: the receipt already
carries per-file role, hash and source commit, and a second file describing the same install is the
defect class this tool exists to close. Schema 2 extends the receipt instead.

**Solve convergence by requiring a checklist in the contributing docs.** Rejected without argument —
this repo's whole thesis is that a rule no gate reads is a rule that decays, and the manifest's own
trap list records adding a moving part tripping four gates precisely because those four are
mechanical.

**Write a three-way merge.** Rejected: `git merge-file` is on PATH by construction here, takes the
three blobs positionally, and is already the primitive `merge-rows.py` delegates its structure lines
to. A second merge implementation in this repo would be a second answer to one question.

## 5. Production-readiness checklist

- security — `update --write` is the first verb in this tool that DELETES, and the deletion is
  bounded to a file gov shipped, that gov no longer ships, whose bytes still equal what gov wrote.
  Every other outcome leaves the file. No remote is contacted and nothing is committed or pushed;
  the operator lands, as with `apply`. The gov-checkout-as-target refusal is carried forward.
- perf / scale — a single target; the cost is dominated by `git show` per file, which is one
  subprocess per receipt row. The new deployability leg is the real cost and is guarded on the
  descriptor and deployer paths, so a records-only commit does not pay it.
- a11y — N/A: a command-line tool with no interface beyond stdout.
- i18n — N/A: developer tooling, English only.
- error / empty / loading states — the verdict table IS this line: every state a file can be in has
  a name, and the two that mean "I cannot tell" (`patched`, `unrecorded`) report rather than act.
- observability — the printed verdict table is the read-only product, and the rewritten receipt plus
  the conflict outbox are the write-mode record.
- risks — data loss in a repository gov does not own is the entire risk surface. It is bounded three
  ways: read-only by default, no action on any verdict that means "the target changed this", and
  deletion gated on byte-equality with the receipt. The second risk is a schema-1 receipt whose lost
  rows make a real install look partial; `unrecorded` names it rather than guessing. The third is the
  three-way argument order, whose wrong form emits a plausible file rather than an error, which is
  why §6 asserts merged content.
- testing + left-shift gates — every refusal gets an arm asserting its MESSAGE and a negative arm
  proving it does not fire on the authorized path; every new `selfcheck` arm gets a liveness pair in
  a scratch gov tree. The deployability leg is itself the left-shift for the descriptors.
- migration / rollback — schema 1 to schema 2 is a read-side migration only: `update` reads both and
  the next `apply` writes schema 2. Rollback of an `update --write` is bounded by the receipt it
  rewrote, which names every path it touched and the hash each had before.
- user docs — `skills/deploy-governance/SKILL.md` gains the verb; the runbook's update prose, which
  already tells a reader to overwrite engine files wholesale on a kit update, points at it instead.

## 6. Acceptance criteria

- **AC1** When `python tools/govkit/govkit.py update --target <fixture>` runs against an install
  whose gov commit has moved, it prints one verdict per receipt row from the §4 table and writes
  nothing — asserted by comparing a `git status --porcelain` snapshot of the fixture taken before
  and after, and by the absence of any new path under `.governance/`.
- **AC2** When a fixture's `engine` file is unmodified and gov's copy has moved, `update --write`
  writes gov's new bytes, and the file's sha256 equals `git show <new_commit>:<source>`. Verdict
  `stale`.
- **AC3** When a fixture's `engine` file has been edited locally and gov's copy has NOT moved,
  `update --write` leaves the file byte-identical and the report names it `patched` with both
  hashes. This is the arm that proves the verb does not clobber, and nothing else observes it.
- **AC4** When a fixture's `engine` file has been edited locally AND gov's copy has moved
  compatibly, `update --write` produces the three-way result: the file contains BOTH the local edit
  and gov's change. The assertion is on CONTENT, never on the `git merge-file` exit code — a
  reversed argument order emits a plausible file with one side dropped and exits 0.
- **AC5** When that three-way conflicts, the target file is byte-identical to before, an order
  exists at `.governance/outbox/` naming the path and all three hashes, and `update` exits non-zero.
- **AC6** When gov no longer ships a file the receipt records and the target's copy is unmodified,
  `update --write` deletes it and stages the deletion; when the target's copy IS modified, the file
  survives and the report names it `patched`. Both halves in one arm, because the asymmetry is the
  criterion.
- **AC7** When the receipt's `gov_commit` does not resolve in the gov checkout, `update` refuses
  before reading the target's files, and the message NAMES that commit. A negative arm proves the
  same refusal does not fire when the commit resolves.
- **AC8** When the registry has gained an entry the receipt does not claim, `update` reports it as
  available and names `--add-kits`, and `update --write` installs nothing for it — asserted by the
  receipt's `kits` list being unchanged.
- **AC9** When `python tools/govkit/govkit.py plan --target <fixture>` and then `apply` run against
  the same fixture, the set of destinations `plan` marks `write` equals the set of paths the receipt
  records, exactly — no path added and none missing. This is A2's criterion and it fails against the
  code at base.
- **AC10** When `apply` runs twice against a fixture with no gov change, the receipt's path set and
  every row's hash are identical between the two runs, INCLUDING every `seed` row. This is A4's
  criterion and it fails against the code at base.
- **AC11** When the default set is applied to a fixture, both playbook destinations exist on disk
  and are recorded in the receipt with `role = "seed"`, and the `playbook-placeholders` hole probe
  runs against files that exist.
- **AC12** When `python tools/govkit/govkit.py selfcheck` runs in this repo, it exits non-zero
  naming the offender for each of: a descriptor `[[gate_leg]]` whose name is in no
  `tools/gate-legs.json` leg; a manifest leg claimed by no descriptor and carried by no
  `[[exempt_leg]]`; an `[[exempt_leg]]` naming a leg that no longer exists; a `version_from` file the
  version gate does not assert; a `need` row no entry claims and no `[[exempt_version]]` carries; and
  a tracked file under an entry's `home` matched by none of its file rules.
- **AC13** When `python tools/govkit/selftest.py` runs each of AC12's six arms against a scratch gov
  tree where the two sides AGREE, it is silent; and against a minimally violating tree, it reds.
  Both halves per arm — an assertion that finds nothing on a clean tree is indistinguishable from
  one that cannot find anything.
- **AC14** When the deployability leg `bash tools/govkit/deployability.test.sh` runs, every registry
  entry declaring at least one landable role lands at least one byte into its fixture, and an entry
  retagged so no rule is landable makes that leg RED. The negative half is A3 reproduced
  deliberately.
- **AC15** When a tracked skill directory outside `skills/session-kickoff/` exists and no
  declaration claims it, `selfcheck` reds; with the exemption row present, it is silent, and removing
  the directory while leaving the row reds as stale.
- **AC16** When `update` runs against a schema-1 receipt, every installed file the receipt omits is
  reported `unrecorded` and none is written, deleted or merged — asserted on the on-disk bytes of a
  fixture whose receipt has had a `seed` row deliberately dropped.
- **AC17** When a kit declaring a `merged` rule is in the update set, `update` refuses by name with
  the same message `apply` carries, and the refusal is reached from both entry points — asserted by
  the message being a single constant that both arms match.
- **AC18** When a kit entry declares no `check.argv`, `python tools/govkit/govkit.py check` reports
  it `landed` rather than `landed-but-inert`, and a kit whose declared check arm exits non-zero is
  still reported `landed-but-inert`.
- **AC19** When `python tools/govkit/selftest.py` runs, every refusal message added by this unit is
  asserted by name in at least one arm, and each also has a negative arm proving it does not fire on
  the authorized path — a guard that always fires and one that never can are the same defect with
  opposite signs.

## 7. Gates

`bash tools/run-gates.sh` green at the push boundary; `GATE_FULL=1` for the DoD. One new leg — the
deployability harness — plus the extended `govkit selfcheck` and `govkit selftest` legs, which
already ride the bar.

Adding a leg trips four gates at once, and this repo's manifest already front-loads them as a trap
worth doing in one pass: the codebase-map coverage assert, the codebase-map freshness byte-compare,
the kickoff-manifest ratchet, and drift-audit's handkept charter signal, which is pinned with zero
slack — so the new leg's script path must be named in the charter's gate-suite section in the same
commit or the bar reds immediately.

Two further obligations specific to this unit. `tools/check-kit-versions.sh` gains two `need` rows,
and it is a `seed` in its own registry entry, so the change reaches adopters on their next
re-seed rather than silently. And the govkit dossier's Gaps section shrinks as commits 1 and 2 land,
which the map's freshness byte-compare will demand be re-rendered.

Before review: `python tools/memory-tree/gotchas.py --for-diff 0f0a121d..HEAD`. Run at base over this
unit's paths it already selects three universal classes, and two of them are this spec's own subject:
`two-answers-to-one-question` is what every correspondence arm attacks, and
`fixture-passes-by-finding-nothing` is why AC13 exists.

## 8. Open questions

- **F1 — is `update` one unit or three?** RECOMMENDATION: one, as written. The three parts are not
  independent — `update` cannot be correct on a receipt that shrinks, and the ratchet is what keeps
  `update` true as the repo grows — and the rollout already splits them into four independently
  green commits, which is the separation that matters. Splitting into three specs would put the
  prerequisite repairs in a unit whose acceptance criteria are all "a later unit becomes possible".
  Owner call, because it is a scope decision rather than a design one.
- **F2 — does an `[[exempt_leg]]` row belong in `registry.toml` or beside the leg in
  `tools/gate-legs.json`?** RECOMMENDATION: the registry. The manifest is consumed by
  `run-gates.sh` at every invocation and adding a deployer-only key to its rows makes the runner's
  input carry data the runner ignores. The registry is already the home of "who owns this path and
  why is this one exempt", and the staleness rule is already written there. The cost is that a
  contributor adding a leg edits two files; that is the point of the arm.
- **F3 — should `update` re-run adopters for `rendered` artifacts, or only report them stale?**
  RECOMMENDATION: re-run, then compare, as §4's role table states. Reporting alone leaves a target
  whose engine files moved and whose rendered Skill still names the old shape, which is precisely
  the silent-green failure the deployer unit's grounding measured in this repo's own tree. The risk
  is that an adopter does more than render; that is bounded by running it exactly as `apply`'s
  configure phase already does, and by the fact that `check` re-runs the same arms afterwards.
  Agent-resolvable under a standing mandate if one is in force.

## 9. Revision log

- rev-1 · 2026-08-16 · initial draft. Grounded on a read of `govkit.py`, `registry.toml` and every
  descriptor, on a mechanical comparison of the descriptor leg declarations against
  `tools/gate-legs.json`, and on driving `intake`, `plan`, `apply`, a second `apply` and `check` end
  to end into a throwaway repository. Ten findings, three blocker-class; two of the three make the
  `update` verb unbuildable as the code stands, which is why the rollout repairs them first.

## 10. Reuse audit

Ran `python tools/codebase-map/reuse_lookup.py` for the update classification and the local-
modification refusal. It returned `govkit.py`'s own symbols and no external seam for the classifier
itself, which is the honest answer — the verdict table is new. Four seams are reused rather than
reinvented, and one candidate is rejected on inspection.

`blob_at()` in `tools/govkit/govkit.py` is already "bytes from the gov index at a recorded commit,
never the working tree", which is exactly what `base` and `theirs` are; `update` calls it twice per
row rather than reaching for `git show` again.

`git merge-file` is the three-way, and the seam that proves it is house-native is
`tools/memory-tree/merge-rows.py`, which hands its own structure lines to that call positionally.
The lookup surfaced `no_new_duplicates` from the same file as a candidate and it is REJECTED: that
driver is a keyed merge over a ROW grammar, and an engine file is arbitrary text with no key. What
transfers is the delegation, not the driver.

`planned_writes()` and `apply`'s land loop are today two expansions of one descriptor, which is A2.
S5 makes the second call the first rather than adding a third.

`make_target()` in `tools/govkit/selftest.py` and `mkrepo()` in
`tools/codebase-map/adopt-codebase-map.test.sh` are the fixture builders the deployability leg
extends; the deployer spec already committed to extending the second rather than writing a third,
and this unit inherits that.

`needed_answers()` is reused unchanged as the source of the deployability leg's per-entry answers,
because it is already DERIVED from the descriptors — a hand-kept answer list inside a test harness
would be a fourth spelling of the same fact and would silently stop covering a kit that grew a token.

No seam exists for the receipt schema migration or the conflict outbox writer; both are small and
both are new. The outbox directory and its one-order-per-file convention already exist in `apply`
and are followed rather than re-decided.
