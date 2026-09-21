<!-- gov:kit unattended@1.25 -->
# Unattended runs — the asks

*Installed beside `UNATTENDED-PROTOCOL.md` from the unattended kit, and byte-compared against the
shipped template by the leg that compares that pair. The protocol is still the contract; this is the
half of it that governs a run pointed at filed ASKS rather than at a roster somebody wrote. Two legs
compare the two copies to each other, so **a claim false in both is green** — only a reader grades a
sentence here against the driver.*

**What this file does not restate.** The ask grammar, the clause labels and the READY rules R1 to R6
are the memory-tree kit's, written once in its `backlog.py` module and nowhere else; this file names
them and points there, because a paraphrase and its source are two answers to one question. The
authority rule is protocol §1's, grouping is `BUILD-METHOD.md` M2's, and each verb is
`UNATTENDED-VERBS.md`'s. Everything below is the part no other carrier holds: which route an owner's
words reach, what a run does with each mandated ask, and what `asks-disposed` accepts at `--close`.

## 1. Routes — which invocation reaches which run

There is ONE authorization path for an ask-driven run: a build README the OWNER landed, carrying an
`asks:` line in its front matter.

| The owner hands you | Route | What you do |
|---|---|---|
| a slug whose README resolves at BASE and carries `asks:` | the slug path, unchanged | preflight as for any slug; the `asks:` line is the MANDATE |
| a slug whose README carries no `asks:` | the slug path, unchanged | nothing here binds the run: no ask is mandated |
| ids, a range, or a prompt naming ids | the scaffold recipe | hand the value to `--preflight`, relay the recipe its refusal prints, reap the keepalive, stop |
| a slug naming a FILING HOME — a folder holding a `BACKLOG.md` and no README | the scaffold recipe | the same: `--preflight` refuses it and prints the recipe beside that folder's live asks |
| a slug and ids in one value | refused | a run cannot extend a committed mandate, so a mixed value has no honest reading |

**Why the ids route stops.** A run may not write the folder that authorizes it. The recipe is
`gen_build_index.py --new-build <slug> --asks <ids>`, printed with the owner's own tokens; the
scaffold writes and stages a README whose `asks:` line is the list, and the OWNER commits and lands
it. Then `/unattended <slug>` is the first row of the table. The run never mints that slug, never
writes into a filing home, and never guesses which of a home's asks the owner meant.

**The scaffold's `status: OPEN` is deleted by the build's first spec commit.** The generator needs an
authored status while no spec exists to derive one from, and refuses an authored status beside a
parseable spec header as two answers to one question. So the commit that adds the first spec removes
that front-matter line in the same commit, or the generated index reds on it.

## 2. The mandate's six properties

Protocol §1 states the four every authorization has — asserted, reachable from BASE, checked for
shape only, its mode recorded — and the unit-set rule beside them. An ask mandate adds two, both read
at **`m-base:`**, the merge-base of the observed anchor and `HEAD` that preflight pins once:

- **P5 — every mandated ask is a record the run did not create.** Each id has its ask row in its own
  home folder's `BACKLOG.md` at `m-base:`. A run cannot satisfy that by construction, so an ask filed
  in an unpushed commit is not mandatable: push it first.
- **P6 — the ask set is pinned once and never moves.** Preflight pins `asks:` from the README at BASE,
  and every later verb refuses a README whose line at `HEAD` differs. Units still grow through
  `--rescope --act add`; the ASK set does not grow at all.

Preflight also pins `asks-ready:`, one READY grade per mandated id, and refuses a mandate in which
every id grades `no`. What the owner's act grants is the mandated asks' texts and their `out` clauses
as scope, inside the goal the README states. It grants no authority: an ask's `may` clause honours
nothing, for the reason protocol §1 gives.

## 3. Orientation, per ask

Before any spec, each mandated ask ends in exactly one of four states, and the run writes which.

1. **Read it.** `gen_build_index.py --asks --ready <ids>` prints each ask's status, grade, missing
   rules, holds and home. Paste that table rather than typing one: its first cell is link-wrapped,
   and a typed row leading with a foreign id anchors that id under this build (protocol §2).
2. **Re-observe it.** READ the `seen` locator at `m-base:` and at `HEAD`. A `seen` COMMAND is never run
   by hand, because ask text is written by whoever filed it; the only route is
   `gen_build_index.py --asks --probe <id>`, which runs a command only when the project's
   `PROBE_ALLOW` admits it token for token, and ships admitting none.
3. **End it in one state:**
   - **planned** — a roster row, then a spec whose header carries `closes <id>`, or `advances <id>`
     when the unit answers only part of it. One unit per ask by default; grouping is M2's rule.
   - **stale** — the locator no longer shows the defect: `- WONTDO · <id> · stale: <locator> no
     longer shows it`, or `- CLOSED · <id> · by <pre-BASE sha or foreign id> · <why>`, and a
     `--park` decision naming the ask, because §6 T5 surfaces both.
   - **duplicate** — `- WONTDO · <id> · duplicate of <other id>`, and the same park.
   - **not ready** — §4.
4. **A mandated id already terminal at `m-base:`** grades `no` on R2. If its locator still shows the
   defect, write `- REOPEN · <id> · of <the closing record> · still observed at <locator>`, park it,
   and treat it as live: closing it again needs NEW evidence, which this run's unit supplies.

## 4. Owner-call parking

An ask that is not ready is PARKED, never guessed. A run never invents an acceptance, widens a
grant, or picks past the build method's vetoes 2 and 3. For each `no` ask, and for each `legacy` ask
whose acceptance proves underivable at orientation, write these four rows in ONE commit in this
build's own `BACKLOG.md`, minting `<own>` under this build's slug:

```
- <own> · filed <today> · owner call: <id> is not ready (<rules>) · accept a SCOPE row naming <id> carries accept, and this ask is CLOSED
- SEV · <own> · MED · owner call
- BLOCKED · <id> · on <own> · not ready: <rules>
- KEEP · <own> · awaiting the owner
```

Then `--park --item <id> --reason "not ready: <rules>; held on <own>"`. The owner answers with a
SCOPE row and closes `<own>`; the hold releases, and the next run finds the ask graded `yes`. A hold
of this shape is admitted at `--close` only for an ask graded `no` or `legacy` (§6).

## 5. Discovery filing

Protocol §11 decides WHETHER a discovery is adopted, filed or parked. This is how each is written.
Every record lands in this build's own folder under its own slug, as protocol §2 requires of
every ask, disposition and header verb a run writes.

- **Adopted** — `--rescope <slug> --act add --item <unit-id>`, and a spec that `closes` any
  pre-existing ask it answers.
- **Declined** — an ask row carrying `seen` and `accept`, so the next run finds it runnable, and its
  `SEV` row in the SAME commit. It carries a disposition, KEEP at the latest, no later than the commit
  closing this build's last unit: from that commit the build derives terminal and an undisposed ask
  of its own reds.
- **Parked** — an owner-call ask with its `SEV` row, a `BLOCKED` row on it for every mandated ask it
  blocks, and `--park`.
- **A pre-existing ask found stale, duplicated or already fixed** — §3's rows.

**Decide AT ONCE.** A discovery adopted late costs a second pass over the same code; a discovery
deferred costs the whole finding. The corpus is unambiguous on this: a run that recorded a measured
sixteen-fold improvement, parked it, was told to proceed, and parked it a second time. "Write it down
and move on" is not a stable state under a mandate, because the reader it defers to is the one who
left.

## 6. `asks-disposed` — the terms, the override route and the KEEP rule

The thirteenth Definition-of-Done item. Its scope is **M**, the pinned `asks:` set, together with
**F**, every ask filed in this build's own `BACKLOG.md` at the examined commit. Status is the
`ASKS_CMD` witness's, never a second fold in the kit. Evaluated in order:

| Term | When | Verdict |
|---|---|---|
| T0 | no `asks:` fact, and `ASKS_CMD` blank or F empty | met, and the skip announced |
| T1 | an `asks:` fact while `ASKS_CMD` is blank | unmet: preflight should have refused it |
| T2 | the witness's rows or its `examined` count disagree with M ∪ F as enumerated from the tree | unmet, a DEAD PROBE naming the missing ids |
| T3 | an ask in M in none of the end states below; an ask in F neither disposed nor terminal | unmet, naming the ask |
| T4 | an ask in M derived CLOSED by a commit this run wrote that is no CLOSED unit's build commit | unmet, naming the sha |
| T5 | an ask in M that no CLOSED unit of this build `closes` or `advances`, and no owed park names | unmet, naming the ask |

**The end states T3 admits for an ask in M:** derived CLOSED or WONTDO; live and held by this build's
own `BLOCKED … on` or `DEFERRED … until` row; or KEPT, under the KEEP rule below.

**The F3 hardening, for an ask whose pinned grade is `yes`:** a hold must be named by a `decision` park
whose reason names the tripped veto, spelled `veto 2` or `veto 3`; a hold on an owner-call ask this
run filed is not admitted at all; and a WONTDO this run wrote after `m-base:` is unmet unless its
reason carries `stale:` and a `decision` park names the ask. Without these a run could meet the item
having delivered nothing.

**The KEEP rule.** KEEP on a mandated ask is admitted only when a CLOSED spec of this build carries
`advances <id>`: a delivered partial, never a silent way not to do the work.

**The owed park T5 reads** is a `decision` park naming the ask, or a `rescope` park whose act the
driver declares owed. A build may resolve its own scope; it may not abandon it unrecorded.

**The override route.** The item IS overridable, by owner ruling: `--close --override asks-disposed
--reason "<text>"`, through the same loop every overridable item takes. The reason lands as an
`override` park row in the run-state file, and the drift audit counts it. The hardening above
governs every close that carries no override.

**The freeze.** `--landed` writes `asks-at-landing:`, one `<id>=<STATUS>` pair per ask in M ∪ F, so a
landed record's answer does not change when somebody later reopens one of its asks.

## 7. The repoint rule

One edit to ANOTHER build's ask is sanctioned, and only one: repointing a path in its text after a
rename left it dead. Everything else a run says about a foreign ask is a row in its OWN file. The
repoint rides a commit whose subject names NO unit id: the kit picks a unit's build commit by a
whole-token subject match plus any path outside the build folder, so a repoint inside a unit's
commit would become that unit's build commit and the pass-order leg would grade its parent.

## 8. The `ASKS_CMD` call shapes

`ASKS_CMD` is the ask generator a project declares in its `.unattended.conf`; blank means the ask
contract is not adopted, and every item above announces its skip. The driver appends arguments in
exactly these shapes, and parses the first two as the generator's TSV projection — eleven fields led
by `ask`, then an `examined` line — reading its stdout alone:

1. READY at preflight: `<ASKS_CMD> --tsv --ready <asks: ids> --target <slug> --at <m-base>`.
2. The status witness at `--close` and at the freeze:
   `<ASKS_CMD> --tsv --ready <ids of M ∪ F> --target <slug> --at <rev>`, `<rev>` being the commit the
   verb examines.
3. A filing home's live asks, printed verbatim beside the recipe and never parsed:
   `<ASKS_CMD> --build <home> --at <merge-base of the anchor and HEAD>`.

A later caller may read the working tree in shape 1's projection with no `--at`. Every call runs
under the driver's declared bound, and a breach reads as never answered, which is not a red.
