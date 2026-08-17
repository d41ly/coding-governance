# tooling backlog — rotated 2026-08-17 (second)

> Terminal rows moved byte-identical out of `../backlog/TOOL.md` when the union of this branch's
> rows and main's crossed the index size cap. Two independent rotations happened on the two
> sides; every row absent from the merged index was verified present in an archive before the
> merge was written. Nothing edited, nothing deleted.

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
- TOOL-aBranchedMandate-4 · CLOSED · `adopt-unattended.sh` decides repo membership by PATH-STRING prefix strip, which never converges under an MSYS mount point, so its not-inside guard misfires ahead of the whitespace guard and reds the adopter e2e on node `a` → `builds/aBranchedMandate/`
- TOOL-cBriefedPilot-30 · CLOSED · CLOSED by TOOL-cSettledDocket-1 — `--park` writes §2's DECISION kind, with the command in the Skill an agent reads
- TOOL-cBriefedPilot-31 · CLOSED · CLOSED by TOOL-cSettledDocket-2 — check 16 joins the EFFECTIVE set, and `DIRECTIVES_EXTRA_TABLE` gives a project its row source
- TOOL-cBriefedPilot-32 · CLOSED · CLOSED by TOOL-cSettledDocket-3 — both assertions hoisted above the Tier-1 cut and keyed on section TITLE, not number
- TOOL-cBriefedPilot-34 · CLOSED · CLOSED by TOOL-cSettledDocket-4 — the hygiene suite's 52 inline sites count; the label no longer says `helper`
- TOOL-cBriefedPilot-35 · CLOSED · CLOSED by TOOL-cSettledDocket-5 — a leg over the derived population, and that suite already counted
- TOOL-cBriefedPilot-38 · CLOSED · CLOSED by TOOL-cSettledDocket-6 — the standing frozen-versus-live fixture, which survived main's redesign of what it tests
