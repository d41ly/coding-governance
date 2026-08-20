# TOOL-aBoundedVerdict-18 — the two checks that cannot fail get subjects

**Status:** SPECCED · rev-2 · 2026-08-19 · node c · Tier-2 · base 098bebd9 · streams tooling

## 1. Goal

Two close-path checks are green because nothing they could catch is reachable: the
`landed-via-lander` Definition-of-Done item is two conf-non-empty tests plus a grep the merge bar has
already run inside the same close, and the gate leg's check 8 exempts terminal records and every
tracked record is terminal, so it has zero subjects while three of them carry exactly the bytes it
exists to refuse. Give each one a subject, or say in the source why it has none.

## 2. Scope (IN)

- **S1** — **`landed-via-lander` gains a REAL observation: the lander writes a marker and `--landed`
  reads it.** Resolved by the owner at F2 against this spec's own recommendation, which was to narrow
  the claim instead. Today the item asserts that `LANDER` and `BYPASS_BAN` are non-empty and that the
  run-state file does not contain the flag — three facts, of which the third is leg check 11's job and
  the first two are that the conf parsed, so it cannot fail for anything the run did. After S1 it can.
- **S1a** — the marker is a DECLARATION, not a convention: a new `.unattended.conf` key names the path
  the lander writes and the driver reads. Undeclared, the item degrades to S2's narrower claim rather
  than refusing — an adopter who has not adapted their lander must not be wedged by a key they have
  never heard of, and this is the one place in the unit where a missing declaration is allowed to mean
  "not asked" instead of "unmet".
- **S1b** — the marker carries the run's own identity, not just its existence. A bare touched file is
  satisfied by any previous landing, which is the pass-by-finding-anything shape this repo has already
  paid for twice; it names the slug and the witness sha `--landed` is about to record, and `--landed`
  compares them rather than testing presence.
- **S1c** — the ADOPTER path carries the change, because S1 changes what `LANDER` means for everyone
  who has one: `adopt-unattended.sh` seeds the key, the conf example documents what a compliant lander
  must write, and `tools/push-main.sh` — this repo's own declared lander — writes it, so the dogfood
  is the first adopter rather than an exception to the rule.
- **S2** — the redundant grep is DELETED regardless of S1, because it duplicates leg check 11 inside
  the same close. Where the marker key is undeclared, the item's remaining claim is stated honestly in
  the protocol's Asserts cell: an item that says less beats one that implies a check it does not run.
- **S3** — leg check 8's terminal exemption either goes, or gains a comment stating why retired bytes
  are exempt. Measured: all seven tracked run-state records are terminal, so the check has zero
  subjects, while three of them carry 1280, 3082 and 4032 bytes of the copied unit list the check
  exists to refuse.
- **S4** — whichever way S3 resolves, the check gains a RED fixture in
  `check-unattended.test.sh`. A check whose only evidence is a corpus that cannot trigger it is the
  `fixture-passes-by-finding-nothing` class, and this unit's whole subject is that class.
- **S5** — a one-line note in each check's source recording that its vacuity was measured and on what
  date, so a later reader can tell a deliberately narrow check from an accidentally empty one.

## 3. Non-goals (OUT)

- No new Definition-of-Done item, and no removal of one. `landed-via-lander` keeps its name and its
  slot; what changes is what it observes or what it claims.
- Not leg check 11, which owns the bypass-flag ban over the run-state file and does it correctly. S1's
  redundancy is on the driver side.
- Not a general vacuity sweep of the other seventeen leg checks. The audit examined four; the rest are
  named as uncovered in its own coverage section and a sweep is a separate unit if the owner wants one.
- Not the `landed-via-lander` item's TRUST properties. Whether a run could lie about having used the
  lander is protocol section nine's subject and unchanged here.
- No change to the CORE DoD floor or to any checker assignment.

## 4. Design

### `landed-via-lander`, as it stands

```
[ -n "$LANDER" ] && [ -n "$BYPASS_BAN" ] && ! grep -qF -- "$BYPASS_BAN" "$rel"
```

Term 1 and term 2 fail only if the conf declared nothing, which the leg's required-key loop already
refuses. Term 3 is a grep the leg runs over the same file in the same close. So the item cannot fail
for any reason attributable to the run, which is what makes it vacuous — not that it is wrong, but
that it is answering a question two other checks already answered.

What it is NAMED for is observable at `--landed`: that verb knows the push happened, and it is the only
place the driver sees the landing at all. **The owner resolved F2 toward making it observable** — the
lander writes a marker, `--landed` reads it — which is the option this spec priced highest and
recommended against, on the ground that it changes what `LANDER` means for every adopter. That cost is
real and is accepted; S1a and S1c are where it is paid, and the degradation path in S1a is what keeps
an unadapted adopter working rather than wedged.

Why the marker must carry identity (S1b): a presence test is satisfied by the marker a PREVIOUS landing
left, so the item would pass on a run that never called the lander at all. The same degeneration the
driver's own comments record in `check_authorization`, where an empty base turned a provenance test into
a read of the git index. Presence is not provenance.

### Check 8, as it stands

The check refuses a run-state file carrying a copied unit list — the staleness the main redesign removed
by making the unit list derived. It exempts `LANDED` and `ABORTED` records. Every tracked record is one
or the other. So the check has no subjects at all, and three of the exempt records carry the exact bytes
it refuses, in quantity.

Two readings, and they lead to different fixes:

- the exemption is CORRECT and retired bytes are history that must not be rewritten — in which case the
  check is fine and needs S5's note plus S4's fixture, because its correctness is currently indistinguishable
  from its emptiness;
- or the exemption was a convenience that let the corpus pass — in which case it goes, and three records
  need either repair or a waiver.

S3 forces the choice rather than leaving it implicit, and F1 is where it is made.

### Inventory

| Concern | Today | After |
|---|---|---|
| `landed-via-lander`'s failure modes | none attributable to the run | the lander's marker, matched on slug + witness |
| a landing that skipped `$LANDER` | indistinguishable from one that used it | the item is unmet |
| a marker left by a PREVIOUS landing | would satisfy a presence test | refused: the witness does not match |
| an adopter whose lander writes nothing | — | the key is undeclared, the item degrades to its narrow claim |
| its redundant grep | duplicates leg check 11 | deleted |
| leg check 8's subjects | zero, corpus-wide | non-zero, or a stated reason for zero |
| check 8's evidence | a corpus that cannot trigger it | a red fixture |
| why either check is narrow | unrecorded | a dated note in source |

### Migration

Depends on F1. If check 8's exemption goes, three tracked terminal records carry bytes it refuses, and
they must NOT be rewritten — a terminal record is a record. So the migration is a waiver registry entry
naming those three, shrink-only, which is how this repo already handles a measured pre-existing
population. If the exemption stays, there is no migration.

### Rollout

S5 and S4 first: they are additive, they cost nothing, and they make the current state legible before
it changes. Then S3's decision and its consequence. S1/S2 last, because the answer to whether
`--landed` can observe the lander decides which of the two it is.

### Files touched (estimate)

`tools/unattended/unattended.sh` (the item's arm) · `tools/unattended/check-unattended.sh` (check 8) ·
`tools/unattended/check-unattended.test.sh` (S4's fixture) ·
`tools/unattended/unattended.test.sh` · possibly a waiver registry beside the other `*.txt` lists ·
`memory/guides/UNATTENDED-PROTOCOL.md` and `tools/unattended/PROTOCOL.template.md` (the Asserts cell,
if S2 fires) · the kit version constant.

### Alternatives rejected

- **Delete `landed-via-lander` outright.** Rejected: the CORE DoD set is shrink-only by a declared
  floor, so deleting a member is a reason-free override of everything keyed on it.
- **Have the driver parse the lander's own output to prove it ran.** Rejected: it couples the kit to a
  project-declared command's output format, which is the one thing `LANDER` exists to keep opaque. The
  marker is the same information through a declared interface rather than a scraped one.
- **A presence-only marker.** Rejected at S1b: satisfied by a previous landing's marker, so it would
  read as provenance while proving nothing — weaker than the vacuous item it replaces, because vacuity
  at least does not mislead.
- **Narrowing the claim (this spec's own recommendation through rev-1).** Refused by the owner. Kept as
  the DEGRADATION path in S1a for an adopter with no declared marker, which is the one place its
  reasoning still applies.
- **Leave check 8 as it is and accept the vacuity.** Rejected on this repo's own rule: a check that
  cannot fail is recorded as such or fixed, never left to read as coverage. S5 is the minimum acceptable
  outcome and it is still a change.
- **Repair the three terminal records so check 8 has clean subjects.** Refused: a terminal record is a
  record, and rewriting one to satisfy a check written later is the opposite of what the freeze is for.

## 5. Production-readiness checklist

- **security** — S1b is the security-relevant line. A presence-only marker is a pass-by-finding-anything
  check and would be WEAKER than the vacuous item it replaces, because it would look like provenance.
  The witness comparison is what makes it a check; arm the stale-marker case explicitly. Note also what
  this still does not buy: a run with shell access can write the marker itself, so the item remains an
  attestation the run could forge, exactly as protocol section nine already says of everything the run
  writes. It stops an HONEST bypass, not a deliberate one, and the spec must not claim more.
- **perf / scale** — S1's deletion removes one grep per close.
- **a11y** — N/A.
- **i18n** — N/A.
- **error / empty / loading states** — the empty case IS the subject of this unit.
- **observability** — S5's dated notes are the observability deliverable: they let a reader distinguish
  a narrow check from an empty one without re-measuring.
- **risks** — low. The one real risk is S3 resolving toward removing the exemption and the three
  affected records being repaired rather than waived, which Migration forbids explicitly.
- **testing + left-shift gates** — S4 is the left-shift and it is the point of the unit.
- **migration / rollback** — see Migration; conditional on F1.
- **user docs** — the protocol's Asserts cell, only if S2 fires.

## 6. Acceptance criteria

- **AC1** — When leg check 8 runs against a fixture holding a NON-terminal run-state record carrying a
  copied unit list, it reds naming the file; the red fixture in
  `tools/unattended/check-unattended.test.sh` that does not exist today.
- **AC2** — When `bash tools/unattended/check-unattended.sh` runs against the real tree it is clean, and
  `tools/unattended/check-unattended.sh` carries a dated note saying its check-8 subject count over this
  corpus was measured at zero.
- **AC3** — When `grep -c 'BYPASS_BAN' tools/unattended/unattended.sh` is compared before and after, the
  `landed-via-lander` arm no longer greps the run-state file for the flag — the redundancy S1 removes.
- **AC4** — When a fixture run lands through a lander that writes the declared marker naming the slug
  and witness, `landed-via-lander` is MET; when the same run lands via a bare `git push` and no marker
  is written, the item is UNMET — the two arms that make the item able to fail for something the run
  did, which it cannot today.
- **AC4a** — When the marker exists but names a DIFFERENT witness (the stale-marker case, seeded by
  copying a prior run's marker into place), `landed-via-lander` is UNMET — the arm in
  `tools/unattended/unattended.test.sh` that proves S1b, and the one a presence-only implementation
  passes and must not.
- **AC4b** — When the marker key is UNDECLARED in `.unattended.conf`, the item reports its narrowed
  claim and does not refuse, and the Asserts cell in both halves of the protocol pair says what it then
  asserts; `bash tools/unattended/check-unattended.sh` is clean over the pair.
- **AC4c** — When `bash tools/unattended/adopt-unattended.sh --check` runs after S1c, it is clean, and
  `tools/push-main.sh` writes the marker — observed by landing a fixture through this repo's own
  declared lander rather than through a stub.
- **AC5** — When either check's source is read, it carries the S5 note, and
  `python tools/memory-tree/check-arms.py` is clean with any changed `ARMS_FLOORS` entry updated.
- **AC6** — When the three terminal records carrying copied unit lists are inspected after this unit,
  `git diff` over `memory/builds/*/RUN.md` is empty for them — the arm that proves Migration's
  prohibition held.

## 7. Gates

`tools/unattended/check-unattended.sh` + `tools/unattended/check-unattended.test.sh` ·
`tools/unattended/unattended.test.sh` · `bash tools/unattended/adopt-unattended.sh --check` ·
`python tools/memory-tree/check-arms.py` · `tools/check-testsuite-counts.sh` ·
`tools/check-kit-versions.sh` · `bash tools/run-gates/run-gates.sh`.

## 8. Open questions

- **F1 — does check 8's terminal exemption stay or go?** Measured: it has zero subjects, and three
  exempt records carry the bytes it refuses. Staying means the check is correct and merely
  unexercised, which S4 and S5 make legible. Going means three records need a shrink-only waiver,
  because repairing them is forbidden. **Recommendation: it STAYS, with S4's fixture and S5's note.**
  Grounds: the bytes in question are in terminal records the redesign has already superseded, and a
  check that fires on frozen history produces a red nobody can clear — which is a worse defect than the
  one it would catch.
  RESOLVED (agent, 2026-08-19, delegated): stays. Mechanism-only fork, and the alternative creates an
  unclearable red on frozen records.

- **F2 — can `--landed` observe that the push went through `$LANDER`, and is it worth a mechanism?**
  Options: parse the lander's output (rejected in §4 as coupling); have the lander write a marker the
  driver reads; or accept S2 and let the item claim less. This spec recommended the narrowing.
  RESOLVED (owner, 2026-08-19): **the lander writes a marker.** The cost the owner accepted, stated
  plainly: every adopter with a lander must adapt it, and this unit moves from Tier 1 to Tier 2 because
  it now changes a shipped contract rather than a local predicate. Three things follow and are in
  scope — the key is a declaration (S1a), the marker carries identity rather than existence (S1b), and
  the adopter path plus this repo's own lander carry the change (S1c). What it does not buy is stated
  in §5: a run with shell access can write the marker itself.

## 9. Revision log

- rev-1 · 2026-08-19 · initial draft. Derived from the close-path audit's mediums 7 and 31, kept as one
  unit because both are the same class — a check green for want of a reachable subject — and the fix for
  both is a fixture plus an honest statement rather than new logic. Tier 1: no contract another kit
  reads is changed, and the one item that might narrow its claim does so in a documented cell. F1
  resolved under the delegated fork rule; F2 raised to the owner because one of its options changes what
  a project-declared value means.

- rev-2 · 2026-08-19 · **F2 resolved by the owner against this spec's recommendation: the lander writes
  a marker.** The unit moves Tier 1 -> Tier 2, because it now changes what `LANDER` means for every
  adopter rather than fixing a local predicate. S1 is rewritten from "gains an observation" to the
  mechanism; S1a makes the marker a declared conf key whose absence DEGRADES to the old narrow claim
  rather than wedging an unadapted adopter; S1b makes the marker carry slug and witness, because a
  presence test is satisfied by a previous landing's marker and would read as provenance while proving
  nothing — weaker than the vacuity it replaces; S1c puts the change on the adopter path and on
  `tools/push-main.sh`, so the dogfood is the first adopter. S2 keeps the grep deletion, which was
  never conditional on F2. AC4 splits into four. §5 states what the marker still does not buy: a run
  with shell access can write it, so this stops an honest bypass and not a deliberate one.

## 10. Reuse audit

Two seams, both existing. Leg check 11 already owns the bypass-flag ban over the run-state file, which is
why S1's deletion is a deletion and not a move — the predicate has a home and this item was a second
copy of it. And the shrink-only `*.txt` waiver registry pattern beside the other gate lists is what
Migration would use if F1 had gone the other way; naming it means no new registry mechanism is invented.

`checker_of` and the CORE floor are read, not changed: the floor is why deleting the item was rejected
rather than considered.

Recall terms used, at the SET level for this build: `closing review round cap blocked verdict adversarial
diff fold unattended close build-complete DoD stall halt`.
