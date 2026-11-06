**Serves:** research TOOL-dTotalRecall-1 TOOL-dTotalRecall-11 TOOL-dTotalRecall-25

# dTotalRecall — the parents cross-check readers' returns, verbatim

The `gov-spec-reviewer` return the cross-check record [`2026-11-05-build-TOOL-dTotalRecall-1-parents-crosscheck`](2026-11-05-build-TOOL-dTotalRecall-1-parents-crosscheck.md) is assembled from, extracted by script from each agent's transcript and not retyped. The brief is [`2026-11-05-prompt-TOOL-dTotalRecall-1-parents-crosscheck`](../prompts/2026-11-05-prompt-TOOL-dTotalRecall-1-parents-crosscheck.md); each group's handoff sits beside it.

## Group A, citation and siblings, led by spec 11 (specs 11, 3, 6, 7, 8, 19, 24, 25, 43, 50, 61, 70 and 89)

1. Assumptions

| Spec | Assumption about the parent | Rule | Verdict | Evidence |
|---|---|---|---|---|
| tr11 | `review.cost` adds four fields to the line: `trigger=`, `shape=`, `efforts=` and `role-sha=` | cite | AGREES | tr11:43-44; dl20:59-62, :157 |
| tr11 | The four fields come after `out-tokens` and arrive all together, so a line written before dl20 and one written after both parse | cite | AGREES | tr11:114-116, :131; dl20:157, :160-162 ("absent, it prints `-`") |
| tr11 | F3: dl20's AC4 keeps every earlier field in its position | cite | AGREES | tr11:317-320; dl20:291-295 |
| tr11 | AC1's sample line ends `trigger=owed shape=- efforts=- role-sha=-` | cite | AGREES | tr11:245-247; dl20:292-293 |
| tr11 | §3 names dl20's `review.cost` act row as a writer that calls `gov_record.py new shape-run` | cite | MISMATCH | tr11:91-93; dl20:59-62, :130, :227-242 |
| tr11 | Once filled, `shape=`, `efforts=` and `role-sha=` are each one token with no spaces (`\S+`) | cite | UNKNOWN UNTIL BUILT | tr11:127; dl20:60-61 |
| tr3 | tr3 writes no lease, and tr2's door mints by calling tr3's claim verbs | RH | AGREES | tr3:74-78; tr2:191-206 |
| tr19 | The door writes `Made-by` as the lease ref when it mints under a lease this session holds, and `owner` otherwise | RH | AGREES | tr19:68-72, :281-283; tr2:196-201, :366-368 (holder read through `--lease status`; no `--claims`; no lease commit parsed) |
| tr7 | The `ask` row has its own writer, `gov_record.py new ask`, which is a handler of tr2's door; `backlog-row` stays tr1's row | HD | AGREES | tr7:87, :147-155; tr2:180; tr1:217, :225-226 |
| tr43 | S8: tr2 S9 moves the `fields`-form `journal`/`log` row onto its door, so the `log` row's writer becomes `gov_record.py new log` | HD | AGREES | tr43:66-69, :258, :378-381; tr2:84-86; tr1:214 (`journal` is `fields`) |
| tr25 | F2: tr2's door replaces the `fence`-form `stream-plan` row's `hand` writer when the planner registers | HD | MISMATCH | tr25:185-188; tr2:62, :84-88; tr1:198-200, :225-226 |
| tr25 | Non-goal: tr2's `record` door takes the `stream-plan` kind over when the planner lands | HD | MISMATCH | tr25:67; tr2:62, :84-88; tr1:198-200 |

2. Mismatches

- **tr11:91-93 against dl20.**
  - tr11 says: "The writers that call the verb: `review.cost`'s review act row (TOOL-dDeclaredLoop-20), the supervisor's journal reconcile for every other role act, and `probe.run` (dWellOiledMachine). This unit ships the verb they call."
  - dl20:130 says: "`item.review.cost` | command | `item.review.report` | the `review-shape` line's cost fields | done | none".
  - dl20:59-62 (S3) limits `review.cost` to `renderShapeLine` adding four fields, and the files-touched list (dl20:227-242) has no `gov_record.py`.
  - Probe: `git grep -n 'new shape-run' ab976b5b3 -- 'memory/builds/*/spec/*'` hits no dDeclaredLoop spec. The only call outside dTotalRecall is TOOL-dWellOiledMachine-19:84, and it uses `--act`, not `--review`.
  - Change: §3 stops naming dl20 as a caller of `new shape-run --review`. It states that no parent spec owns the review-act writer: a later unit or an ask does, and TOOL-dWellOiledMachine-19 calls the `--act` form. tr11 bumps its rev.
  - Cause: pre-existing. dl20:129 at `794a0f5fb` reads the same, tr11 has not changed since then, and the last cross-read read only wb1 for tr11 (crosscheck-returns:124).
- **tr25:185-188 and tr25:67 against tr2 and tr1.**
  - tr25 says: "(a) `hand`, … and TOOL-dTotalRecall-2's door replaces `hand` when the planner registers" (:188), and "TOOL-dTotalRecall-2's `record` door adopts it when the planner lands" (:67).
  - tr2:84-87 says: "Each registry row whose `writer` is `hand` and whose `schema.form` is `fields` … takes `writer = "gov_record.py new <kind>"` … a `hand` row of another form keeps `hand`, and the pass commit's `Decided:` trailer names the unit or kit owning its door".
  - tr2:62 says: "A row whose `schema.form` is not `fields` is written only by a kind verb of S7". S7 has only `build-readme` and `spec`.
  - tr1:198-200 says: "`hand` is legal on any row TOOL-dTotalRecall-2 S9 does not move. S9 moves only the `fields`-form `hand` rows".
  - The `stream-plan` row is `form = "fence"` (tr25:38), and tr25 comes at order 6, before tr2 at order 12. So tr2's pass finds the row and leaves it `hand`.
  - Change: F2 and the §3 non-goal say the `fence` row keeps `hand` through tr2 S9, and tr2's `Decided:` trailer names dIndexedDesign's planner as the owner of its door. The writer cell moves when that planner lands its own verb, as a handler in `KIND_HANDLERS` or a door of its own. tr2's door does not take it over. tr25 bumps its rev.
  - Cause: the revision `58b395b6e` (tr1 rev-5), which dropped tr1's promise that tr25 relied on. At `794a0f5fb`, tr1:194 read "`hand` is legal until TOOL-dTotalRecall-2 registers a door" and tr1:220 read "TOOL-dTotalRecall-2 replaces each with its door". tr2 S9 already moved `fields`-form rows only at `794a0f5fb` (tr2:77).

3. Unknown until built

- tr11:127: what goes into `shape=`, `efforts=` and `role-sha=` is decided by the build of dBoundRoles' shape registry. dl20 fixes only `-` until then (dl20:60-61). If a value contains a space or a second `=`, `\S+` misparses it or refuses it.

4. Probe hits no rule binds

- tr6:94, :142-145, :200 (`refs/gov/leases`): tr6 reads the lease tip's `status:` itself with `git log -1 --format=%B`. It reads no holder, session, class or epoch, and it does not cite tr2, so RH does not bind.
- tr3:68, :79 (`session`): this is the per-session id rule, not a lease holder read.
- tr3:300, tr6:261, tr19:357 (`F6`): each is that spec's own F6, not tr2's.
- tr8:91: this row has the `generated` form and a `generator:` writer, so it is no `hand` row. tr8:280, :332 use "by hand" in another sense.
- tr24:23, :72, :82, :172-188: "hand commit" and "hand edit" are not writer cells. The tr24:82 consumes-from depends on no revised section.
- tr50:30, :162: "a cause line added by hand", not a writer cell.
- tr61:34-35, tr70:70, :103: "hand-off" and "hand parser", not writer cells.
- tr89:59: "by hand or through the door" is about merging records, not a registry writer cell.
- tr11 (HD/RH): its row's writer is `gov_record.py new shape-run`, a handler, not `hand`, and it reads no lease.
- tr11 (SA): tr11 depends on no stop, dispose, `review_state` or chain rule. The grammar's `kind=` and `at=` sets (tr11:121-122) are untouched by `63669d505`; `git show 63669d505 -- …dDeclaredLoop-32.md …/dFairHearing/spec/ | grep -nE 'shape|review-shape|kind='` printed nothing.

5. Revised sections cited but not relied on

- tr11: none. It cites dl20 S3, the `item.review.cost` row and AC4. dl20 rev-3 moved only S9 (dl20:86-89) and the `item.review.dispose` row (dl20:128), and tr11 cites neither. tr11:356 is a recall hit on dl20's scout row, not an assumption.

6. Parent text that looks wrong

- tr2:88 names "`backlog-row`: TOOL-dTotalRecall-7's ask door" as the owner of that row's door. But tr7:87 disowns `backlog-row` ("TOOL-dTotalRecall-1's row") and registers a separate `ask` row on the same `BACKLOG.md` home (tr7:147-155). As written, nothing ever gives `backlog-row` a door.
- tr2:358 quotes only `lease — none · <tail>` as the non-holder output of `--lease status`. pr34 S23 (pr34:111-113) also prints `lease — off · <tail>` when `RUN_CLAIMS` is off, and tr2's lease rung does not handle that line.
- tr2:196-198 accepts "the slug claim `refs/gov/claims/<slug>` whose `claimant:` is this session's". But tr3 S7 (tr3:60-61) writes the slug claim's claimant as "the content key of the mandate's id list", not a session.
