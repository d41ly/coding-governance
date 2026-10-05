# Acceptance ledger — TOOL-dThriftyLanding-5

**Serves:** journal TOOL-dThriftyLanding-5

Built on `95304bc0`. Each declaration rests on a read of its leg's program and what it calls; the
table below names the path or conf key that decided each. Measured in a detached worktree holding
these declarations plus one commit adding a line to a file under memory/gotchas/: the bar with
`GATE_DOCS_BASE` and `GATE_BASE` at that commit's parent ran 44 legs and skipped 17 in 65 s; the
same tree with only `GATE_BASE` — today's scoped decision — ran 54 legs in 325 s. Four legs red in
both runs on in-flight state of this build, the manifest stamp, the run-gates README marker and the
kit epoch among them; none is caused by the docs mode.

| Leg | doc_reads | Decided by |
|---|---|---|
| unattended kit gate | builds, guides, archive | RUN and README reads under `$M/builds`, the three protocol byte-compares and BUILD-METHOD under guides, the RUN.md precondition over `git ls-files $M/` |
| pass-order history | builds, project | README, RUN and spec reads at HEAD; `memory/project/pass-order-waiver.txt` |
| brief-recorded | builds, project | RUN and README reads at commits; `memory/project/brief-recorded-waiver.txt` |
| lexicon wiring, lexicon naming predicates | builds | `scan_corpus` reads the .py, .sh and .js files under memory/builds only |
| review-protocol parity | guides | `memory/guides/REVIEW-PROTOCOL.md` |
| every held leg is budgeted | AGENTS.md, CLAUDE.md | `read_registry_tags` scans both for the node table |
| marker contracts, hook destinations, process-monitor wiring, kit version markers, straggler-guard arms, transition-audit arms | none | fixtures under mktemp, or reads under tools/, skills/, .githooks/ and .claude/ only |

Left undeclared, so they run on every doc push: `drift-audit records` and `memory hygiene` read the
whole doc class; `govkit selfcheck` lists memory names; `govkit acceptance matrix` was not fully
traced; `install-prefix` would read a future `*.template.*` file under memory; `recall floor`
reads the memory tree its guard already names; `encoding posture` sits at the 5 s line and reads
a registry under memory/project/. A pass commit's
undeclared write outside memory/builds/ is not re-graded by `unattended kit gate` on a push that
moves nothing under memory/builds/; a pass commit carries its build's records there, and the
commit-msg hook refuses such a write at commit time.

**Evidences:** TOOL-dThriftyLanding-5
- AC1 — `GATE_DOC_PATHS` — declared in `.githooks/gate-env.sh` as memory/, README.md, AGENTS.md, CLAUDE.md, WIRE-INTO-PROJECT.md and the charter template; each is tracked
- AC2 — `GATE skip  unattended kit gate  (docs-only: no path it reads moved)` — printed by the measured docs bar, 65 s against the base scoped bar's 325 s
- AC3 — `disagree about which doc paths` — absent from `govkit selfcheck` with the six descriptors carrying the manifest's values
