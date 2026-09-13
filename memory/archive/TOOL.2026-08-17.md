# tooling backlog — archived 2026-08-17

> Terminal rows only (24, all CLOSED), moved from `../backlog/TOOL.md`, with no id appearing twice
> in this file. TWO rotations landed on this date from concurrent builds and `TOOL.2026-08-17b.md`
> is the other; 17 of the rows below are also rows of that file, so this pair does not partition the
> family between them. The all-time id-collision grep still reaches every row here.

> **SUPERSEDED 2026-09-12 by `TOOL-cSpliceWarden-4`.** The header ABOVE is the corrected one. The
> header this file shipped with read "Terminal rows only, moved byte-identical from
> `../backlog/TOOL.md` … deduplicated by id", and it was false in three ways. As written on
> 2026-08-17 this file held 90 rows, not terminal rows only: 66
> were non-terminal (60 OPEN, 5 SPECCED, 1 DEFERRED). 49 of its ids were ALSO live in
> `../backlog/TOOL.md`, and 7 of those disagreed about status. It was not deduplicated by id —
> `TOOL-aBranchedMandate-2` and `-3` each appeared twice.
>
> The cause is recorded rather than guessed. Two builds rotated to this filename on one day from
> parallel branches, and the branch that wrote this file had never seen the commits that closed the
> rows it froze. The row-keyed merge driver was failing in that window, which commit `c1af5dd2`'s own
> message records, so a backlog merge resolved by taking a side.
>
> What this repair did, under the owner's ratified decision of 2026-09-12 and the `cut` rotation mode
> that decision declared. 49 rows whose id the live shard already owns were DELETED here — the live
> shard owns those ids and wins on every disagreement. 15 rows whose only surviving copy was here
> were MOVED to `../backlog/TOOL.md`, each re-derived to CLOSED from its spec's status header and
> from its closing commit on `origin/main`; their bodies came from those commits, because a closing
> commit often rewrote the sentence as well as the token and this file preserves the pre-close prose.
> Two rows were DROPPED as the stale halves of duplicate pairs whose CLOSED twins survive below.
> Removed verbatim, so nothing is lost by the deletion:
>
>       TOOL-aBranchedMandate-2 · SPECCED · the wiring check's eol arm exits non-zero on a worktree checkout artifact, and `.unattended.conf` declares that command as WIRING_CHECK, so `--preflight` refuses in every fresh worktree and the protocol forbids it from repairing → `builds/aBranchedMandate/`
>       TOOL-aBranchedMandate-3 · SPECCED · a build committed on the run's own branch authorizes nothing, so admits the remote's advertisement of that branch as a declared, recorded, strictly weaker second anchor → `builds/aBranchedMandate/`
>
> 24 terminal rows survive, which is what the corrected header claims. It does NOT claim every id
> sits in exactly one file: 17 of these 24 are still byte-identical rows of
> `TOOL.2026-08-17b.md`, the second rotation of the same date. That overlap is real, it is outside
> the scope ratified on 2026-09-12, and it is filed rather than quietly fixed.
>
> This note is prose, never a row. A dash-led line carrying an id would key as a backlog row under
> hygiene check 20 and join this file's id set — a supersession note that becomes a row is a new
> defect wearing the repair's clothes.

- TOOL-aWalkedCorpus-1 · CLOSED · memory-recall has TWO corpus enumerators — extract.corpus_files is the measurement path, query.py defines its own — and every widening must teach both. TOOL-aDeclaredCeiling-2 §4 said this was 'recorded as the follow-up it is' and no row existed
- TOOL-aNumeralWarden-4 · CLOSED · `map_lib.scan_js_definitions` joins the export scan in the `kit-js` layer, so the 30 definitions under `tools/` are indexed alongside the 3 `meta` exports and `boundedK` is findable — closed by TOOL-dClosedLexicon-12
- TOOL-aMouldedFolio-3 · CLOSED · the folder claim is DERIVED: 21 disagreements across 15 READMEs went to 0, and the removal is sentence-scoped because in 17 of 17 the sentence shares its line with the next one — closed by TOOL-aMouldedFolio-3
- TOOL-aMouldedFolio-4 · CLOSED · one marker contract, proven across FOUR readers (the fourth writes); the Python side stopped accepting-and-rewriting an indented or trailing-whitespace marker — closed by TOOL-aMouldedFolio-4
- TOOL-aMouldedFolio-5 · CLOSED · check 20 reuses the kit's fence reader and refuses an unterminated fence; unkeyed rows report path and line — closed by TOOL-aMouldedFolio-5
- TOOL-dClosedLexicon-6 · CLOSED · `_glob_match`'s nesting branch escaped the RAW pattern so an earlier wildcard went literal; both branches now share one glob->regex conversion and a CASE TABLE row pins depth-1 and depth-2 — closed by TOOL-dClosedLexicon-1
- TOOL-dClosedLexicon-7 · CLOSED · importer-local precedence now applies only to BARE targets; a fully-qualified dotted import gets no directory precedence, pinned by a case-table row — closed by TOOL-dClosedLexicon-1
- TOOL-dClosedLexicon-8 · CLOSED · `_python_defs` now emits a target per imported NAME and keeps `node.level`, so `from <pkg> import <name>` resolves; pinned by an extract row and a resolve row — closed by TOOL-dClosedLexicon-1
- TOOL-dClosedLexicon-9 · CLOSED · a dotted target now resolves only to a PATH-CONSISTENT candidate, so `concurrent.helper` no longer reds against any same-stem file; two case-table rows pin it — closed by TOOL-dClosedLexicon-1
- TOOL-dClosedLexicon-10 · CLOSED · resolution branches on the importer's LANGUAGE, `**` crosses segments, and candidates match at path boundaries; the relative walk returns nothing when it escapes the root — closed by TOOL-dClosedLexicon-1
- TOOL-dClosedLexicon-5 · CLOSED · `tools/lexicon/kit.toml` reverts to `include = "**"`; the hand-enumeration existed only to dodge the clobber, and a new kit file is deployed again without a list edit — closed by TOOL-dClosedLexicon-4
- TOOL-dClosedLexicon-4 · CLOSED · a `**` file rule now pools every tracked file under `home` MINUS any whose DESTINATION another rule claims, so a re-apply no longer clobbers a project-owned or seeded file — closed by TOOL-dClosedLexicon-4
- TOOL-dClosedLexicon-3 · CLOSED · the run-state unit list is DERIVED from the build README on every read instead of copied, so it cannot go stale; check 8 now asserts the region is EMPTY and `records-current` with it — closed by TOOL-dClosedLexicon-3
- TOOL-dClosedLexicon-11 · CLOSED · `--preflight` now ROTATES a terminal record to `RUN.<phase>.<blob8>.md` and starts fresh; the name derives from the BYTES because no verb commits, so two runs can share a witness — closed by TOOL-dClosedLexicon-11
- TOOL-dClosedLexicon-12 · CLOSED · REFUSED on measurement: of 219 lexicon-only definitions, 166 are deliberate map exclusions and 53 are JS. The coupling buys noise; the JS hole is closed inside the map, 3 rows to 33 — closed by TOOL-dClosedLexicon-12
- TOOL-dClosedLexicon-13 · CLOSED · ROLE_KINDS is the one table and LANDABLE_ROLES derives from it; plan keys on the producer and the destination too, apply names every skip, and the parity arm drops its role filter — closed by TOOL-dClosedLexicon-13
- TOOL-aBranchedMandate-1 · CLOSED · `adopt-memory-recall.sh --check` byte-compares the rendered Skill without normalising CR, so every fresh worktree reds a merge-bar leg on a file nobody edited → `builds/aBranchedMandate/`
- TOOL-aBranchedMandate-4 · CLOSED · `adopt-unattended.sh` decides repo membership by PATH-STRING prefix strip, which never converges under an MSYS mount point, so its not-inside guard misfires ahead of the whitespace guard and reds the adopter e2e on node `a` → `builds/aBranchedMandate/`
- TOOL-cBriefedPilot-36 · CLOSED · checks 8 and 26 contradicted: 26 refuses `--preflight` on a finished run and that is the only verb re-splicing the generated region, so a build continuing after its run ended red check 8 forever with no verb able to clear it. Terminal records are now exempt
- TOOL-cBriefedPilot-37 · CLOSED · `closing-review-recorded` joined on an EIGHT-char base prefix where git abbreviates to seven: the 8-char grep matched none of 48 tracked records, the 7-char matched. The item was unmeetable, clearable only by a self-authored override. Needle is seven now
- TOOL-aWalkedCorpus-3 · CLOSED · the recall floor: check-recall.py is the exit code bench.py cannot have, RECALL_FLOOR names a CELL (records:fts5:r@5) and is DERIVED as the one-retirement worst case, and the floor and the per-id assertion each red ALONE. 20 arms, gov-only
- TOOL-aBranchedMandate-2 · CLOSED · the wiring check's eol arm exits non-zero on a worktree checkout artifact, and `.unattended.conf` declares that command as WIRING_CHECK, so `--preflight` refuses in every fresh worktree and the protocol forbids it from repairing → `builds/aBranchedMandate/`
- TOOL-aBranchedMandate-3 · CLOSED · a build committed on the run's own branch authorizes nothing, so admits the remote's advertisement of that branch as a declared, recorded, strictly weaker second anchor → `builds/aBranchedMandate/`
- TOOL-aWalkedCorpus-7 · CLOSED · origin/main was RED on its own bar at 43eb6b1: lexicon 450 over pin 417, and govkit's DEFAULT-selection apply arm. Both fixed here — TOOL-aWalkedCorpus-8 and -9 — and the pin raised with the 33 arrivals attributed
