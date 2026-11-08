**Serves:** research TOOL-dRankedPlan-1 TOOL-dRankedPlan-3

# dRankedPlan — the parents cross-check readers' returns, verbatim

The `gov-spec-reviewer` return the cross-check record [`2026-11-05-build-TOOL-dRankedPlan-1-parents-crosscheck`](2026-11-05-build-TOOL-dRankedPlan-1-parents-crosscheck.md) is assembled from, extracted by script from each agent's transcript and not retyped. The brief is [`2026-11-05-prompt-TOOL-dRankedPlan-1-parents-crosscheck`](../prompts/2026-11-05-prompt-TOOL-dRankedPlan-1-parents-crosscheck.md); each group's handoff sits beside it.

## Group A, citation and RH, led by spec 3 (specs 1, 2, 3, 6, 10, 16 and 33)

1. Assumption table

| Spec | Assumption about the parent | Rule | Verdict | Evidence |
|---|---|---|---|---|
| 1 | The `build-readme` row's `fields` are graded against `FRONT_MATTER_KEYS` by key. So adding `priority` to both keeps the gate green (rp1:56-58, :126) | cite | AGREES | tr1:78-86 (S3 reds a `schema.source` literal that no longer matches the row's `fields`) and tr1:185-187 (`FRONT_MATTER_KEYS` "is compared with the `build-readme` row's `fields` by its keys"). The row itself is TOOL-dTotalRecall-4's (tr1:146), and rp1 credits it to S3, the gate that grades it. Rev-5 did not touch this. |
| 2 | `item.plan.lease` is witnessed by `unattended.sh --claims` printing "a live row for the build held by this node" (rp2:188) | RH | no row: the rule does not bind (see 4) | rp2:126 relies on dPlacedRequest-1, -19 and -21, not on tr2. It reads the node (field 2, the fleet tag; pr1:204-207), not a session, class or epoch. |
| 3 | `record_kinds.py new triage` (and `new dupes`) is the registration verb, and its flags are those of tr1 S9 (rp3:74-76, :96-99) | cite | AGREES | tr1:105-109: "`python record_kinds.py new <name> --tag <tag> --writer <door> --check <leg> --field <Key>…`" |
| 3 | A typed kind with no command of its own takes the writer "the factory and its flags", in the `deviation` row's form (rp3:76-79, :454) | cite | AGREES | tr1:191-196 ("else the factory with `--build`, `--unit` and the kind's field flags. No parent claims a generic `build_records.py new <kind>`") and tr1:220. Rev-5 changed only the `hand` sentence of this bullet. |
| 3 | `gov_record.py new triage` is the factory's adapter, and the door admits a factory-writer kind (rp3:79-80, :148, :462) | cite | AGREES | tr2:46-50 (S1: "a thin adapter over one function, `write_new_record`… in… `build_records.py`") and tr2:52-57 (S2: "A factory kind whose `writer` names the factory with its flags… is the door's own") |
| 3 | `derive_content_key` is memory-tree's own, it lives in `build_records.py`, and it has the shape of `derive_section_sha` (rp3:82-83, :462-463) | cite | AGREES | tr2:69-71 (S5) and tr2:225 ("`write_new_record`, `derive_content_key` and `check_mint_authority` in `build_records.py`") |
| 3 | `triage.py` writes through the door "one record per pass per home build that the pass decided an ask in", including home builds that another session holds (rp3:80-81) | cite | MISMATCH | tr2:196-201 and :188 (a `<n>` mint first checks "the build's lease or claim", and "a lease or claim held by another refuses, naming the holder"). See 2. |
| 6 | The Plan breakpoint fires through `--trigger <slug> --subject <path> --cause <c>` (rp6:28, :50-51, :73, :87) | cite | AGREES | dl20:65-71 (S2), unchanged by rev-3 |
| 6 | `review.dispose` declares "a plan revision → `plan.record`" as a route and arms no consumer (rp6:74-76) | cite | AGREES | dl20:106-108 (§3: "Their routes are declared on the `review.dispose` row and are a later build's to arm") and dl20:133-134. See 6 for the row itself. |
| 6 | Arming that route would add a disposal mechanism across the driver's owed count and the DISPOSAL stage (rp6:239-242) | cite + SA | AGREES | dl20:72-75 (S4) and :76-80 (S5) are unchanged. Rev-3's S9 (dl20:86-89) keeps "their default reading unchanged". rp6 reads no route by severity, budget or asks. |
| 10 | A candidate "intake landed" signal is an `intake` row in TOOL-dTotalRecall-1's record-kind registry (option (b), which F5 rejects) (rp10:337-341) | cite | AGREES | tr1:66-70 (S1, the registry). The revised writer bullet is not read. |
| 16 | `record_kinds.py new plan --tag … --writer … --check record-kinds --field …` appends the `plan` row (rp16:41-45, :142) | cite | AGREES | tr1:105-109 (S9) and tr1:78-83 (S3, the `record-kinds` leg) |
| 16 | The `plan` writer cell is the factory and its flags, as tr1 §4 spells it, with no generic `new` (rp16:47-49, :392-394) | cite | AGREES | tr1:191-196 and :220. rp16:392's "TOOL-dTotalRecall-1 rev-4, TOOL-dTotalRecall-2 rev-6" is a dated revision-log entry that was correct at `d1721ef20`. Rev-5 and rev-8 left the factory-writer text as it was. |
| 16 | tr2 S2 admits `gov_record.py new plan` as the factory's adapter (rp16:49-50) | cite | AGREES | tr2:52-57 |
| 16 | The door CLI is `new <kind> --build --unit --title --field <Name>=<value>` (rp16:61-62, :142) | cite | AGREES | tr2:46-48 (S1), tr2:58-60 (S3) and tr2:63-68 (S4) |
| 16 | The witness runs tr1 S4's generated field check over the plan record (rp16:66) | cite | AGREES | tr1:87-89 (S4) |
| 16 | tr1's registry and leg are the seam that F2 reuses, and so is the factory verb (rp16:352, :402-403) | cite | AGREES | tr1:66-70, :78-86 and :105-109 |
| 33 | The seed writes the plan record through `gov_record.py new` (tr2 S1), run from a copied memory-tree kit in a scratch repo that holds only the memory-tree and loop kits (rp33:39-43, :78) | RH | UNKNOWN UNTIL BUILT | tr2:196-199 now reads the holder through pr34 S22's `unattended.sh --lease status build <slug>`. tr2 names no kit lookup for that read and no behaviour when the unattended kit is missing (`grep -n 'resolve_kit\|subprocess' …dTotalRecall-2.md` finds no lease-read lookup). tr2:205-206 and AC5 (tr2:287-290) cover only "neither lease nor claim". |

2. MISMATCH

- **rp3:79-81, S5:** "The door `gov_record.py new triage` (TOOL-dTotalRecall-2 S1) is that factory's adapter… and `triage.py` writes through it, one record per pass per home build that the pass decided an ask in."
  - **tr2:188:** "| `<n>` | the next free `<n>` in the home folder… | the build's lease or claim |"
  - **tr2:196-201:** "The build's authority, in order: the lease `refs/gov/leases/<slug>/build` held by this session… else the slug claim `refs/gov/claims/<slug>` whose `claimant:` is this session's; a lease or claim held by another refuses, naming the holder."
  - **Consequence:** a triage pass writes into the folders of other builds. Any home build that another live session leases or claims gets an exit 2 from the door, so that home's record and its batch are never written.
  - **Change:** S5 has to say what happens to a home build held by another session. One option is to skip the home and print a named `triage — <home> held by <holder>` line, with an AC plant for a foreign-held home. The other is to write the record under the triaging build's own folder instead of the home's. Either way, S6's "the build whose folder holds the record" must follow the choice.
  - **Cause:** pre-existing. `git show b3cc159c9:…TOOL-dTotalRecall-2.md` lines 188-191 carry the same refusal. Rev-7 and rev-8 changed only how the holder is read.

3. UNKNOWN UNTIL BUILT

- **rp33 S1:** tr2's build run decides whether the door, run in `ratify.py`'s scratch repo with no unattended kit, finds `unattended.sh --lease status` or falls through to the session rule. If the door errors there, rp33 S1 reds the fixture at its base.

4. Rule-wide hits a rule does not bind

- **rp2:188, :380 (RH):** the lease witness reads only "held by this node", which is `--claims`' fleet-tag field (pr1:204-207). It reads no session, class or epoch, and rp2:126 relies on dPlacedRequest-1, -19 and -21, not on tr2.
- **SA across all seven specs:** a grep for `converg|ceiling|rework|budget|review.design|max-rounds|route-back|chain|severity|REVIEW_ROUNDS|precision floor|review_state|no-fall` finds no spec that states a spec-audit exit, a routing by budget or severity, `review_state`'s shape, or a chain stop. rp6 S2 (rp6:50-53) passes a plan record to the harness "as a spec-audit subject" but states no rounds, exit or target for it. Whether dl32 S3's `no-fall` applies to it is dl32's own subject classification.
- **HD across all seven specs:** every writer cell these specs register (`triage`, `dupes`, `plan`) is "the factory and its flags", never `hand`. None of the specs relies on tr2 S9 giving a `hand` row a door.

5. Revised parent sections cited that no assumption depends on

- **rp1:** none. It cites tr1 S3 only, and S3 was not revised.
- **rp3:** tr1 §4's writer bullet, its revised `hand` sentence (tr1:196-198) and the note under the rows (tr1:224-226). It cites none of tr2's revised sections (§3 edge, §4 "Minting", §8 F6). Its mismatch rests on a Minting text that was not revised.
- **rp6:** none. It cites dl20 S2, S4, S5 and §3, and none of dl20's revised §4 `item.review.dispose` row or S9.
- **rp10:** tr1's revised writer bullet, which F5's rejected option (b) does not read.
- **rp16:** tr1 §4's revised `hand` sentence and the note under the rows (tr1:196-198, :224-226). The rp16:392 rev cites (tr1 rev-4, tr2 rev-6) are historical.
- **rp33:** none. It cites tr2 S1 only.

6. Parent text that looks wrong

- **dl20:128 vs dl20:106-108 and :133-134:** the rev-3 `item.review.dispose` Routes cell lists no plan-revision or landing-record route, while §3 and the line after the table say both "are declared routes of `item.review.dispose`". The rev-2 row lacked them too.
- **tr1:196-197 vs tr2:48-50:** tr1 says "No parent claims a generic `build_records.py new <kind>`", while tr2 S1 names "The factory's own stand-in verb `build_records.py new <kind>` (PLAY-dOrderedCharter-7 S8)".
- **tr2:191 and :211 vs tr2:200 and :289:** the slug mint passes `--claimant <content key>`, yet authority accepts a slug claim "whose `claimant:` is this session's". One claimant field is read as two different values.

Files read (all at `ab976b5b3`, which is this worktree's HEAD):
- C:\projects\coding-governance\.claude\worktrees\vigilant-einstein-2d0f7d\memory\builds\dRankedPlan\spec\2026-10-26-spec-TOOL-dRankedPlan-{1,2,3,6,10,16}.md
- C:\projects\coding-governance\.claude\worktrees\vigilant-einstein-2d0f7d\memory\builds\dRankedPlan\spec\2026-10-27-spec-TOOL-dRankedPlan-33.md
- C:\projects\coding-governance\.claude\worktrees\vigilant-einstein-2d0f7d\memory\builds\dTotalRecall\spec\2026-10-26-spec-TOOL-dTotalRecall-{1,2}.md
- C:\projects\coding-governance\.claude\worktrees\vigilant-einstein-2d0f7d\memory\builds\dDeclaredLoop\spec\2026-10-24-spec-TOOL-dDeclaredLoop-{20,32}.md
