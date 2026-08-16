---
slug: dClosedLexicon
node: d
opened: 2026-08-16
streams: playbook+tooling
roster: PLAY+TOOL
ids: PLAY-dClosedLexicon-1 TOOL-dClosedLexicon-1 TOOL-dClosedLexicon-2 TOOL-dClosedLexicon-3 TOOL-dClosedLexicon-4 TOOL-dClosedLexicon-5 TOOL-dClosedLexicon-6 TOOL-dClosedLexicon-7 TOOL-dClosedLexicon-8 TOOL-dClosedLexicon-9 TOOL-dClosedLexicon-10
---

# dClosedLexicon — a declared naming lexicon, gated, and portable into an unknown repo

Node `d` · opened 2026-08-16 · streams playbook+tooling.

Commissioned from a translation of the `XiaoYouChR/Ghost-Downloader-3` agent charter. Most of that
document is one Python/Qt application's house style and does not survive the trip. Its closed verb
table does, because the table's real function is not naming — a verb you cannot pick is a
responsibility you have not scoped.

The unit funds companion §12's existing claim that a project can gate its naming conventions, which
today names the goal and ships nothing that does it. Three predicates, one per-repo declaration, and
the portability machinery that lets the same engine land in a repo whose language set is unknown at
authoring time.

The adversarial pass moved the design in three places. The scaffold seed is derived from the
adopter's own corpus and then frozen, because an adopter cannot author a closed vocabulary for a
domain they have not read. Vacuity is armed twice, since the corpus-side arm is itself defeated by an
empty corpus. The kit chassis — the version pair, the govkit entry, the leg guards, the install-prefix
compliance, the map claim — turned out to be the bulk of the work rather than the predicates.

The build carries THREE units. `TOOL-dClosedLexicon-1` is the lexicon kit and the playbook edits that
route to it, and it leads — nothing blocks it. `TOOL-dClosedLexicon-2` wires the verb table into the
`codebase-map` ratchet and the `drift-audit` signal set, and is inert without unit 1; the two were
one until unit 1's rev-3, when the review found §1 does not let a single unit carry a cross-stream
contract change. `PLAY-dClosedLexicon-1` adds the §0 fallback rule and is BLOCKED on the ceiling
raise landing in a parallel build.

The owner ratified the scope menu on 2026-08-16. All three predicates ship behind one opt-in kit,
with the retirement condition for P1 written into F4 so a later session can act on it without
reargument. `TOOL-dClosedLexicon-2`'s open forks are counted in the run section below rather than
here, because this sentence said "one fork" and the 2026-08-16 audit added a second.

The sequencing has been rewritten twice and the reasons are worth reading before trusting any of it.
`PLAY-dClosedLexicon-1` began as a byte-freeing predecessor the whole build was parked on. It then
refuted its own plan on measurement: §14 is the one externalization candidate with NO activity
trigger, because per-call token discipline has no activity to trigger on, so a §-stub would have made
always-on rules dark. The reusable half of that finding is that §-stub externalization is available
only to activity-scoped sections. Then the ceiling moved to 48 KiB, which deleted the byte pressure
that unit existed to relieve. What survives there is the §0 line, its 157 B still over the PRESENT
ceiling by 140, and the refutation itself — which corrects `PLAY-aCandidStub-2`, an OPEN row that
still recommends the move this build proved wrong.

One mechanism was CUT rather than built — a pin-direction guard, on two independent defects. Unit 1's
F-A14 records what that cut costs, because a coverage mode nothing enforces is weaker than the spec
first claimed.

Two of the three findings that opened this build were already tracked: `PLAY-aSealedCaravan-1` owns
the `{{MEMORY_ROOT}}` disjointness error and `PLAY-aCandidStub-2` owns the byte budget. The unit
reopens the first only because it converts a repeated prose correction into a gate. The stale
`19-check` count in template §5 is new, and its fix is to delete the number rather than update it.

## The 2026-08-16 unattended run — classification and what it carries

The M4 audit at `reviews/2026-08-16-review-dClosedLexicon-2.md` came back BLOCKED with two blockers,
and the classification after folding it is: `TOOL-dClosedLexicon-1` READY and building;
`TOOL-dClosedLexicon-2` BLOCKED on a parked scope fork; `PLAY-dClosedLexicon-1` still BLOCKED on the
ceiling raise, which has NOT landed — the ceiling is still 32,768 and the template measures 32,682,
so the 157 B line still does not fit. The aSiftedPlaybook merge specced that raise; it did not land it.

Unit 2 is parked at its F3 and the run does not build it. rev-2 declared two drift signals in
`drift_signals.py`, which is the project-owned DATA layer and cannot declare one. The two routes that
can — editing the shipped `drift_report.py` engine, or folding both into the single `HANDKEPT` signal
— differ in what gets built, and one of them reverses a doctrine this build's own spec states while
the other degrades a pin unit 1 depends on. That is scope, and the standing mandate does not delegate
scope. Unit 2 was always inert without unit 1, so parking it costs this run nothing.

The table below is
GENERATED from the status header of every spec in this folder — do not hand-edit it.

<!-- gen:build-index -->
**Build status:** BLOCKED · 3 unit(s) · node d · opened 2026-08-16 · streams playbook+tooling · ids PLAY-dClosedLexicon-1 TOOL-dClosedLexicon-1 TOOL-dClosedLexicon-2 TOOL-dClosedLexicon-3 TOOL-dClosedLexicon-4 TOOL-dClosedLexicon-5 TOOL-dClosedLexicon-6 TOOL-dClosedLexicon-7 TOOL-dClosedLexicon-8 TOOL-dClosedLexicon-9 TOOL-dClosedLexicon-10

| Unit | Status | Rev | Last change |
|---|---|---|---|
| [PLAY-dClosedLexicon-1 — §0 gains a fallback rule, and the §14 externalization is refuted](spec/2026-08-16-spec-PLAY-dClosedLexicon-1.md) | BLOCKED | rev-2 | 2026-08-16 |
| [TOOL-dClosedLexicon-1 — a declared naming lexicon, gated, and portable into an unknown repo](spec/2026-08-16-spec-dClosedLexicon-1.md) | CLOSED | rev-11 | 2026-08-16 |
| [TOOL-dClosedLexicon-2 — wiring the verb table into the map ratchet and the drift signal set](spec/2026-08-16-spec-dClosedLexicon-2.md) | BLOCKED | rev-3 | 2026-08-16 |

Records live under `spec/` and `reviews/`.
<!-- /gen:build-index -->

