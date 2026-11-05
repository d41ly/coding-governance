**Serves:** research TOOL-dLinkedLibrary-1 TOOL-dLinkedLibrary-8 TOOL-dLinkedLibrary-13 TOOL-dLinkedLibrary-22

# dLinkedLibrary — the parents cross-check readers' returns, verbatim

The `gov-spec-reviewer` return the cross-check record [`2026-11-05-build-TOOL-dLinkedLibrary-1-parents-crosscheck`](2026-11-05-build-TOOL-dLinkedLibrary-1-parents-crosscheck.md) is assembled from, extracted by script from each agent's transcript and not retyped. The brief is [`2026-11-05-prompt-TOOL-dLinkedLibrary-1-parents-crosscheck`](../prompts/2026-11-05-prompt-TOOL-dLinkedLibrary-1-parents-crosscheck.md); each group's handoff sits beside it.

## Group A, citation, led by spec 1 (specs 1, 3, 4, 8, 9, 13, 22, 23, 24, 37, 47 and 52)

1. Assumptions

| Spec | Assumption about the parent | Rule | Verdict | Evidence |
|---|---|---|---|---|
| 1 | tr2's door renders only the `**Serves:**` line and one `- **<Key>:** ` line per field (its S3), so it cannot write the `toml` fence | cite | AGREES | ll1:87-88 · tr2:58-62, S3 unrevised |
| 1 | The `decision` row is added through tr1 S9's factory `record_kinds.py new … --writer hand` | cite | AGREES | ll1:134-136, :188, :442 · tr1:105-109 |
| 1 | S9's verb takes no flag for the six columns (`TOOL-dTotalRecall-1:101-102`) | cite | MISMATCH | ll1:142 · tr1:101-102 is now S8's `seed_population` text. The S9 flags are at tr1:105-106 |
| 1 | The writer stays `hand`, which tr2 S9 keeps on a row whose form is not `fields` (`rows`) | HD | AGREES | ll1:143-145 · tr1:198-200 and tr2:84-88 |
| 1 | AC9's registry is tr1's, absent at base | cite | AGREES | ll1:377 · tr1 S1 at tr1:66 |
| 3 | The `recall-index` row is added through tr1 S9 with writer `generator:<path>`, a door tr1 §4 admits | cite | AGREES | ll3:42, :130-131, :138, :289 · tr1:191 and :105-109 |
| 4 | The `annotation-index` row is added through tr1 S9 with writer `generator:…`, and S9 has no flag for the other columns (no line cite) | cite | AGREES | ll4:50, :95-102, :207, :474 · tr1:105-109 and :191 |
| 8 | The registry and factory are tr1 S1, S3 and S9 | cite | AGREES | ll8:50 · tr1:66, :78, :105 |
| 8 | S9's verb has no flag for `layer`…`unarmed` (`TOOL-dTotalRecall-1:101-102`) | cite | MISMATCH | ll8:69 · tr1:101-102 is now S8. The flags are at tr1:105-106 |
| 8 | `census` and `ruling` are factory-kind rows (tr1 §4 "The rows"), each with writer `gov_record.py new <kind>`, the door being the factory's adapter (tr2 S1, S2) | cite | AGREES | ll8:76-78 · tr1:218 and :192-193 ("the command its owning spec names"), tr2:52-56 |
| 8 | The door over `write_new_record`, tr2 S1 to S6 | cite | AGREES | ll8:53-55 · tr2:46-74 |
| 8 | The door mints every record "under that build's claim", "through the door's existing minting rule" | RH | AGREES | ll8:96-97, :424-428 · tr2:196-206. The spec reads no holder itself and names no `--claims`, holder verb or second ask |
| 8 | The `ruling` closed sets are refused at the write boundary through `read_record` (tr2 S4) | cite | AGREES | ll8:225-227 · tr2:63-68 |
| 9 | The door `gov_record.py new` and `write_new_record` are tr2 S1 to S5, and `origin` is written through tr2 | cite | AGREES | ll9:36-37, :95-96, :110 · tr2:46-73 |
| 13 | The `research-return` row is added through tr1 S9 with `--writer hand` | cite | AGREES | ll13:41-42, :118, :326 · tr1:105-109 |
| 13 | `{ form = "header" }` is a grammar its owner grades (tr1 §4 "Data model") | cite | AGREES | ll13:46 · tr1:178-181 |
| 13 | S9's verb takes no flag for the six columns (`TOOL-dTotalRecall-1:101-102`) | cite | MISMATCH | ll13:49 · tr1:101-102 is now S8. The flags are at tr1:105-106 |
| 13 | The writer stays `hand`, which tr2 S9 keeps on a non-`fields` row | HD | AGREES | ll13:50-52 · tr1:198-200 and tr2:84-88 |
| 13 | A return the door writes takes the `kind:` line by hand afterwards, since the door renders only the Serves and Key lines (tr2 S3) | cite | AGREES | ll13:106-109 · tr2:58-62 |
| 13 | `design-record` is a registered name of tr1, and tr1 S4 grades fields | cite | AGREES | ll13:148, :299 · tr1:216 and :87-89 |
| 13 | AC7's registry is tr1's | cite | AGREES | ll13:272 · tr1:66 |
| 22 | The `gotcha` row is added through tr1 S9 with `--writer hand`, form `header`, not `fields`, which tr1 S4 grades | cite | AGREES | ll22:37, :62-71, :113 · tr1:105-109, :178-181, :87-89 |
| 22 | A `hand` writer is legal on a `header` row | HD | AGREES | ll22:63 · tr1:198-200 (S9 moves only `fields`-form rows) |
| 22 | S9's verb has no flag for the form or the other five columns (`TOOL-dTotalRecall-1:101-102`) | cite | MISMATCH | ll22:74 · tr1:101-102 is now S8. The flags are at tr1:105-106 |
| 23 | tr1's `ruling` row has no value column | cite | AGREES | ll23:356 · tr1:66-69 lists the columns, none a value column |
| 24 | dl20 S6's `measure_class_occurrences` and `review.left-shift` are read by S7 where landed | cite | AGREES | ll24:36-37, :85, :98, :109 · dl20:74-78 and :190-196. S6 was not touched by rev-3 |
| 24 | F6's ask: dl20 S6's `review_dispose.py classes` counts every `class:<slug>` under `second-occurrence` | cite | AGREES | ll24:289-291 · dl20:190-195 |
| 24 | Relies on rev-3's `item.review.dispose` row or its S9 | SA | AGREES | None of ll24 :36, :85, :98, :109 or :289 reads dl20:128 or :86-89. No binding, as the brief expected |
| 37 | S3's ruling plant calls tr2's `gov_record.py new ruling --build dAdopt --unit TOOL-dAdopt-1` in a scratch repo and expects exit 0 | cite | AGREES | ll37:53-55, :79 · tr2:46-50, and tr2:206 with AC5 at tr2:290 (neither lease nor claim writes under the session rule) |
| 37 | The door's authority read succeeds in the plant's scratch repo, where only the memory-tree kit and the door are installed | RH | UNKNOWN UNTIL BUILT | ll37:145-146 · tr2:196-199 reads the holder through `--lease status build <slug>`, and no line of tr2 says what the door does when that command or a remote is absent |
| 37 | The door mints under the claim of the build the owner opened (through ll8 S3) | RH | AGREES | ll37:115-117 · tr2:196-201. The claim rung is unrevised, and no holder read is made |
| 47 | tr1 S3 defines the `record-kinds` leg as `record_kinds.py --check`, unchanged | cite | AGREES | ll47:27, :56, :73 · tr1:78-79 |
| 52 | tr1's `ruling` row has no value column, and its field check grades presence and order alone (its S4) | cite | AGREES | ll52:77-79, :468 · tr1:66-69 and :87-89 |
| 52 | The door runs `read_record`'s closed-set refusal at its write boundary (tr2 S4) | cite | AGREES | ll52:81-82, :84-86 · tr2:63-68 |

2. Mismatches

- **ll1:142, ll8:69, ll13:49, ll22:74, one cite in four specs.**
  - The dLinkedLibrary side: ll1:142 reads "S9's verb takes no flag for those six columns (TOOL-dTotalRecall-1:101-102)". ll8:69, ll13:49 and ll22:74 cite the same `TOOL-dTotalRecall-1:101-102`.
  - The parent side at `ab976b5b3`: tr1:101-102 now reads "`tools/memory-tree/kit.toml` (TOOL-dWitnessedBar-13 S2), keyed by record path and section, seeded / once at this unit's landing by `test.seed`'s `seed_population`…", which is S8. The S9 flags now sit at tr1:105-106: "`--writer <door> --check <leg> --field <Key>…` appends a conforming row and refuses one missing a / required column".
  - At `0dc3f1958`, `git show 0dc3f1958:…TOOL-dTotalRecall-1.md | sed -n 101,102p` printed those S9 lines, so the cite was right then.
  - Change: re-cite `TOOL-dTotalRecall-1:101-102` as `TOOL-dTotalRecall-1:105-106` in ll1:142, ll8:69, ll13:49 and ll22:74, or cite `TOOL-dTotalRecall-1 S9` by section so the gen region cannot move it again. Each of those specs needs a rev line, with no change to its design.
  - Cause: the revision. `58b395b6e` (tr1 rev-5) added four rows to tr1's `gen:spec-records` table, at hunks `@@ -24,6 +24,8 @@` and `@@ -44,6 +46,8 @@`, both above S9. That moved every later line by 4.

3. Unknown until built

- ll37 S3 and AC3: what the door does in the `%TEMP%/ro-<case>` scratch repo, which has the memory-tree kit but no dPlacedRequest kit and possibly no remote, when its lease rung calls `unattended.sh --lease status build dAdopt` (tr2:196-199). It could fall through to the session rule (tr2:205-206), or it could error and fail the expected exit 0. Only tr2's build run decides this, along with how its lease rung reaches a sibling kit's command.

4. Rule-wide hits no rule binds

- ll1:114 (the SA probe): the `rework budget spent` draw is S6's re-run of the two raters of the decision rubric. It goes through dl30 and dl31's `budget.py draw` and `--exhausted`. That is not a spec audit, and it relies on none of dl20, dl32 or fh17.
- ll13:107 (the HD probe): "takes the line by hand" means editing the `kind:` line into a record the door wrote. It assumes no `hand` writer and no door for a non-`fields` row.
- ll24:101 ("Writing the gate a left-shift earns … filed by `review.dispose`"): this is a non-goal about the left-shift count of dl20 S6 and §4 (dl20:190-196). It does not touch the dispose row rev-3 changed. dl20 is not a parent, so nothing binds.
- ll37, ll47 and ll52 are units promoted from a spec audit (ll37:166, ll47:141, ll52:461, F1 in each). The promotion is history, and none cites dl20, dl32 or fh17 for routing, so SA does not bind.
- ll24:131, ll23:311, ll47:111, ll52:391, ll9:266 and ll8:330-331 ("by hand", "hand-written leg or record") are about legs or records written by hand, not the registry's `hand` writer.

5. Revised parent sections each citation spec cites without depending on them

- 1: none. It cites tr1 S9 and tr2 S3 and S9, none revised. It reads tr2 S9's form rule, not tr1's revised writer bullet.
- 3: tr1 §4's writer bullet is cited only for `generator:<path>` (tr1:191). The rev-5 `hand` sentence (tr1:198-200) is not depended on.
- 4: none.
- 8: tr2 S6 and §4 "Minting" (rev-7 and rev-8): only the claim rung is relied on. The lease-holder read, the `--lease status` verb and §8 F6 are not.
- 9: none. S1 to S5 is cited, and Minting is not.
- 13: none. The `header` form and the `hand` writer both depend on tr1 §4 and tr2 S9, and they agree.
- 22: none. It depends on the `hand` legality of tr1:198-200, and that agrees.
- 23: none.
- 24: dl20 rev-3's `item.review.dispose` row (dl20:128) and S9 (dl20:86-89). Only S6 is depended on.
- 37: tr2 §3's external edge, §4 "Minting"'s holder read and §8 F6. They are depended on only through the fixture question in section 3.
- 47: none.
- 52: none.

6. Parent text that looks wrong

- tr2:197-199 says `--lease status` "prints the lease's `fleet-tag`, `session`, `lease`-mode class and `epoch`", yet tr2:360 says S22's line "lacks the class", which is only asked for as a seventh field. "Minting" states as present a column that is still an open ask.
- tr2 §4 "Minting" (tr2:196-206) gives the door, a memory-tree file, no way to locate `unattended.sh`, and no behaviour when that command or a remote is absent in an adopter or scratch repo.

The specs read were dLinkedLibrary specs 1, 3, 4, 8, 9, 13, 22, 23, 24, 37, 47 and 52, and dTotalRecall specs 1 and 2, all at `ab976b5b3`. dDeclaredLoop spec 20 was also read, at `ab976b5b3`. The two dTotalRecall specs were diffed against `0dc3f1958`. No dLinkedLibrary spec changed between `0dc3f1958` and `ab976b5b3` (`git diff --stat` printed nothing). Paths:
- C:\projects\coding-governance\.claude\worktrees\vigilant-einstein-2d0f7d\memory\builds\dLinkedLibrary\spec\
- C:\projects\coding-governance\.claude\worktrees\vigilant-einstein-2d0f7d\memory\builds\dTotalRecall\spec\2026-10-26-spec-TOOL-dTotalRecall-1.md
- C:\projects\coding-governance\.claude\worktrees\vigilant-einstein-2d0f7d\memory\builds\dTotalRecall\spec\2026-10-26-spec-TOOL-dTotalRecall-2.md
- C:\projects\coding-governance\.claude\worktrees\vigilant-einstein-2d0f7d\memory\builds\dDeclaredLoop\spec\2026-10-24-spec-TOOL-dDeclaredLoop-20.md
