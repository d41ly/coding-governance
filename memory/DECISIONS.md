# decisions — index

> One line per decision, APPEND-ONLY, every family in one file. Detail in `decisions/`.
> Grouped by family for reading; the file is never re-sorted and a landed row is never edited.

## PLAY — playbook

- PLAY-cDerivedGlossary-1 — Ported 2 lessons from inCMS DES-bMirroredLexicon-1 to domain-rules §12+§10: runtime-derive-vs-artifact fork; a gate's hardcoded export-mirror drifts, so derive it + a non-vacuity sentinel. — _Accepted 2026-07-22 (node c)_

## KICK — kickoff

*(none yet)*

## TOOL — tooling

- TOOL-aRuledParchment-1 · spec-format discipline in the kit: SPEC-TEMPLATE.template.md + conf-gated check 12 (SPEC_FORMAT_CUTOFF) + hardened _unfenced + self-test; dogfood armed 2026-07-15 -> builds/2026-07-15-TOOL-aRuledParchment/ (upstream inCMS ARCH-aRuledParchment-1/-2)
- TOOL-aWardenGraft-1 · adopted inCMS branch-guard inline in .githooks/pre-commit (§3 enforcement + red/green self-test); DECLINED node-doctor (inCMS-specific check registry, no cg env-health need) + standalone new-stream (thin git, stays adopter-supplied per WIRE §5)
- TOOL-aWireWarden-1 · built check-wiring.sh (--check/--fix/--session) + SessionStart hook auto-wiring unset core.hooksPath (never clobbers) + agent-cap detection via settings-merge.py --check; adopted agent-cap on cg; Tier-2 review wf_f0164aef -> builds/2026-07-15-TOOL-aWireWarden/
- TOOL-bThriftyBellows-1 · kit 1.2 fork-collapse of check-memory-hygiene.sh: set membership, one-awk checks 2/4/8, memoized index_set, batched wc + stale-guard — 2647s → 34s on a 1487-file tree, byte-identical ×3 targets (upstream PERF-eThriftyBellows-1) -> journal/2026-07-16-bThriftyBellows
- TOOL-bTamedTempest-1 · pytest-parallel-guardrails kit 1.0: xdist four-knob recipe + crashprobe death-attribution + aiosqlite seam patch + forced-race gate + domain-rules additions; 11-finding review folded (upstream inCMS ARCH-eVigilantCanary-2) -> builds/2026-07-16-TOOL-bTamedTempest/
- TOOL-aQuarriedLantern-1 · memory-recall kit 1.0 ported from inCMS ARCH-aTemperedLoom-1..-4: conf-driven retrieval, conf_digest in the cache key, loud zero-record diagnosis, rendered Skill + opt-in hook, 2 gate legs + WIRE §3c gate-wiring step -> builds/2026-08-03-TOOL-aQuarriedLantern/
- TOOL-aBatchedLintel-1 · kit 1.4 fork-collapse 2: checks 12 and 7 to one awk each (42.88s + 7.86s of an 81.77s run; 257.8s→1.66s upstream at 356 specs) + hygiene-parity.test.sh + 16 self-test arms; byte-identical over the real corpus and 28 shapes -> builds/2026-08-03-TOOL-aBatchedLintel/
- TOOL-aFoldedQuarry-1 · fold inCMS ARCH-dQuarriedLedger-1 + ARCH-dWinnowedTrove-2 into the memory-tree kit as a PARAMETERISED port (mechanism, never inCMS's corpus numbers), then re-dogfood on this repo's memory/ -> builds/2026-08-08-TOOL-aFoldedQuarry/
- TOOL-aFoldedQuarry-2 · U6 tier2-review.js joins findings to verdicts on an orchestrator-assigned INTEGER (Map), not an echoed file:line; agreeing repeat idempotent, disagreeing repeat -> UNVERIFIED; kept the kit's unverified/PARTIAL reporting; 2 new gates + 16-arm self-test
- TOOL-aFoldedQuarry-3 · U1 flatten: builds/<slug>/ (no date/FAMILY), one append-only DECISIONS.md, backlog/<FAMILY>.md; discipline becomes the spec header's `streams` enum gated by STREAMS_CUTOFF; every retargeted selector asserts a NON-EMPTY population; kit 1.4->1.5
- TOOL-aFoldedQuarry-4 · U2 retires gen-memory-tree.sh/TREE.md for gen_build_index.py: build status DERIVED from spec headers, rendered into each build README, LIVE.md and ledger/<month>.md; one source of truth per build (a `status:` key is legal ONLY when nothing is derivable)
- TOOL-aFoldedQuarry-5 · U3 corpus_ids.py adds checks 13-16 (id collision, orphan waiver, 4-rule dead-path registry, read-path accounting); declares no grammar or set it does not own — grammar from memory-recall, the two sets asked of the shell; pins measured
- TOOL-aFoldedQuarry-6 · U4 gotchas.py + an 8-record bug-class corpus grown from THIS build's failures (not inCMS's 178); anchors DERIVED from the record body, --for-diff stdout IS the reviewer checklist, universal set budgeted at 3
- TOOL-aFoldedQuarry-7 · U5 check-arms.py makes the harness disciplines mechanical: every `fail` BRANCH armed or pinned, keyed on the CALL SITE (14 branches behind 12 numbers), pinned in BOTH directions, excluded from its own scan; measured 14 branches / 5 armed
- TOOL-aFoldedQuarry-9 · reconciled node c's drift-audit landing (TOOL-cSightedPlumb-1) with the flatten: its build folder migrated to builds/cSightedPlumb/ with authored front matter, memory/tooling/TREE.md stayed deleted, gate legs unioned to 31 in the compact one-line format
- TOOL-aDrainedSluice-2 · V1 check-arms DISCOVERS its gate/test population, so a second gate is covered the day it lands; the signature capture stops at the first UNESCAPED quote, or five manifest branches carry the gate's own shell source — text no assertion can emit; floors are PER GATE
- TOOL-aDrainedSluice-3 · V3 check 5 governs a recording at ANY depth under a build's kind folder, kind taken from the SUBFOLDER not the parent; measured first — the drafted grammar redded 14 conforming files, so check 5 and check 12 now interpolate one REC_TAIL instead of two hand-copied EREs
- TOOL-aDrainedSluice-4 · V4 the §9 rev-scan closes on the next `## ` heading. The branch has TWO conditions and both became newly reachable, so the fixture pair is deliberate: a §9 logging a SMALLER rev, and a §9 logging NONE. A fix that closes the range for the maximum passes the first alone
- TOOL-aDrainedSluice-9 · V8 a dead DIRECTORY citation is a dead citation — check 15's harvest required a file extension, hiding four. REPAIRED, not registered: the registry is for citations that cannot legally be edited, and a live ledger is present-tense navigation, not a frozen record
- TOOL-aDrainedSluice-9b · V8 DEAD_PATH_EXCLUDE names prefixes that are not repo CONTENT. Resolution never touches the filesystem, so a checkout location classifies as dead identically on every node — the question is meaning, not portability, so it is declared in the conf rather than guessed
- TOOL-aDrainedSluice-5 · V2 every fail branch in every gate is ARMED (30/30, pin empty, floors 16:16 and 14:14). Where an arm goes is a property of the harness: hygiene never short-circuits so its fixtures batch; the manifest gate's CALLERS do, so its 16 branches need ten invocations
- TOOL-aDrainedSluice-5b · V2 instrumenting fail() before writing anything showed 11 of 16 manifest branches ALREADY firing while asserting only `check N FAILED` — which names the check, not the branch. Eleven were an assertion swap; five needed a fixture. Measure the population, then write
- TOOL-aDrainedSluice-6 · V5 one python resolver, and it RUNS the candidate: the MS-Store python3 stub answers `command -v` and exits 9009. Sourced by the four scripts the runbook never copies out; carried INLINE byte-identical (gated) by every copy-installed kit, where `../lib/` does not exist
- TOOL-aDrainedSluice-6b · V5 an override that is SET and unusable is a NAMED failure, never a fall-through — the operator believes they chose, and did not. `py -3` is impossible: the probe quotes the candidate and consumers use "$PY" as one word, so every candidate is a single word
- TOOL-aDrainedSluice-7 · V6 the recall cache gets a byte budget (absent = 512 MB measured here, blank = uncapped) with LRU by built_at. The WHOLE PLAN is computed before anything is deleted, or `delete nothing when the budget cannot be met` is unreachable from a greedy loop
- TOOL-aDrainedSluice-7b · V6 mid-build is `a database newer than the manifest`, NOT `no readable manifest` — the latter is reasoned from a FIRST build and evicts a rebuilding sibling. Deletion removes the manifest LAST and keeps it on any failure; rmtree leaves protected rubble on win32
- TOOL-aDrainedSluice-8 · V7 three gates whose INPUT was narrower than their claim. Both JS gates now see untracked-and-unignored files (the landing boundary moves deliberately; .gitignore is the escape hatch), and their arms exercise the DISCOVERY path every existing arm bypassed
- TOOL-aDrainedSluice-8b · V7 check-wiring repairs CRLF on the eol=lf-pinned `.claude/` renders — bounded to that intersection because the attribute alone covers 46 files. It rewrites bytes: `git checkout --` is state-dependent here, since diff and status disagree about the same file
- TOOL-aDrainedSluice-8c · V7 hygiene-parity refuses a baseline below a DERIVED kit-version floor (first commit introducing the current constant, not a sha that rots), and refuses the no-history case by name — `no floor found` is not `any baseline is fine`
- TOOL-bThriftyBellows-2 · WONTDO — the single-pass generator has no subject left: U2 deleted gen-memory-tree.sh and TREE.md, and check 9 delegates to gen_build_index.py. The measurement it preserved (cache-and-grep is SLOWER; mmap index reads win) lives in the bug-class catalogue
- TOOL-aDrainedSluice-1 · the tooling backlog is DRAINED — twelve rows, eleven CLOSED and one WONTDO, each resolved by a landed unit rather than by re-scoping. A drained row stays short on purpose: an index entry is capped at 300 chars so it stays scannable, and the record lives here

## DEPL — deployer

*(none yet)*
