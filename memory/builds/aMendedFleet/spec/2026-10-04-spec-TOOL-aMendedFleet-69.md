# TOOL-aMendedFleet-69 — the agent-instructions kit announces a canonical file past 32 KiB and states both tool facts as verified

**Status:** SPECCED · rev-2 · 2026-10-04 · node a · Tier-1 · base 7af5f564 · streams tooling · ratified 2026-10-04 · order 69

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

The agent-instructions kit tells an adopter that Codex reads the canonical `AGENTS.md` with
"nothing extra", and that Claude Code does not read `AGENTS.md` at all. Both are now wrong in a way
that costs an adopter instructions. Codex reads at most 32 KiB of project instructions by default,
while this repo's own `AGENTS.md` is 64,344 bytes and the charter template it renders is 48,193,
both PINNED by `wc -c` on 2026-10-04, so a charter adopter that drops few kit blocks ships a file
Codex reads only part of. Claude Code has read
`AGENTS.md` since 2.1.277, but only in a project with no `CLAUDE.md`. This unit makes the adopter
announce a canonical file over the Codex default beside the byte count it already prints, corrects
the README's Codex row and the Claude Code claim in every kit carrier and in the `AGENTS.md`
wrapper, and stamps both facts with the date, node and source they were verified against, as the
charter's §6 requires of an environment claim.

## 2. Scope (IN)

- **S1** — The install path of `tools/agent-instructions/adopt-agent-instructions.sh`, directly
  after the `canonical:` line it prints, prints one announce line when the canonical file is larger
  than 32768 bytes: `  ! AGENTS.md is <n> bytes, over 32768: Codex reads at most 32 KiB of project
  instructions by default (project_doc_max_bytes) - trim it, or raise that key in the Codex config`.
  The figure is a shell constant beside `CANON`, and the exit status does not change. Observed by
  AC1.
- **S2** — The `--check` path prints the same line before its OK line, under the same condition,
  and its exit status still depends on the wiring alone. Observed by AC2 and AC3.
- **S3** — The README's Codex row reads that `AGENTS.md` IS the canonical, that Codex reads only
  its first 32 KiB by default, and that the adopter announces a file over it. The phrase
  "nothing extra" leaves the row. Observed by AC4.
- **S4** — The Claude Code claim is restated, with the same meaning, in the README's opening
  paragraph, its table row and the adopter's header comment: Claude Code reads `CLAUDE.md`; from
  2.1.277 it also reads `AGENTS.md`, but only in a project with no `CLAUDE.md`; so `CLAUDE.md`
  stays the `@AGENTS.md` import, which serves a CLI older than 2.1.277 and a project whose
  `CLAUDE.md` exists for another reason. The link to the vendor issue stays, now marked closed.
  Observed by AC5.
- **S5** — Each of the two facts carries one stamp in the README, in the shape
  `(verified <date>, node <tag>, against <source>)`: the Codex figure against
  `DEFAULT_PROJECT_DOC_MAX_BYTES` in `openai/codex` at `codex-rs/config/src/config_toml.rs`, and the
  Claude Code behaviour against the 2.1.277 entry of `anthropics/claude-code`'s `CHANGELOG.md`. The
  date and node are the build pass's own, written only after that pass re-runs both probes.
  Observed by AC6.
- **S6** — Line 14 of `AGENTS.md`, the wrapper's parenthetical about wiring, keeps its pointer to
  the kit and replaces its stated reason with a pointer to the kit README, so the repo states the
  Claude Code fact once. Observed by AC7.

## 3. Non-goals (OUT)

- The charter template's §6 sentence that an `AGENTS.md`-only repo "ships a repo Claude Code cannot
  read". It is a governance-template edit rendered into `AGENTS.md` by the playbook renderer, a
  second mechanism; §8 F2 splits it to `PLAY-aMendedFleet-3`.
- Changing the default alias set, the modes, any exit code or the wiring itself. The import stays
  correct under both CLI behaviours.
- Trimming this repo's `AGENTS.md` under 32 KiB, or changing the template's 48 KiB cap. The
  announce makes the fact visible; the trim is the context diet's, unit 79 among it, and a cap
  change is an owner call.
- Writing a Codex `config.toml` for an adopter. The kit owns no Codex configuration.
- The tool and repository counts in the README's opening paragraph. They are the standard's own
  claims, cited as such, and no part of this kit's behaviour rests on them.

### Edges

- **hands-off** `PLAY-aMendedFleet-3` — the charter template's §6 sentence, split to that unit by
  §8 F2; it relies on this unit's stamped README as the fact's one home.
- **consumes-from** external — network access and an authenticated `gh` at the build pass, which
  S5's stamps are verified through.

## 4. Design

### Evidence

Read at base `7af5f564`, re-verified 2026-10-04 at `efc4b0c9`, whose `tools/`, `skills/` and
`AGENTS.md` bytes equal base.

- `adopt-agent-instructions.sh` line 138 prints `canonical: $CANON (<n> bytes)` on the install path
  only; `--check` exits at line 80 before reaching it. Nothing tracked reads either output line:
  `git grep` for `agent-instructions OK` and for the `canonical:` line finds only the script, and the
  kit's suite greps neither.
- `AGENTS.md` is 64,344 bytes against its 64,512 row in `tools/template-size-limits.txt`, 168 bytes
  under, PINNED by `bash tools/check-template-size.sh AGENTS.md` on 2026-10-04. S6 must fit that.
- Codex: `gh search code project_doc_max_bytes --repo openai/codex` found
  `pub const DEFAULT_PROJECT_DOC_MAX_BYTES: usize = 32 * 1024;` in
  `codex-rs/config/src/config_toml.rs`, and `agents_md.rs` reading at most that many bytes. Measured
  2026-10-04 on node a. A file of exactly 32768 bytes is read whole, so the announce is strictly
  greater-than.
- Claude Code: `gh issue view 6235 --repo anthropics/claude-code` reports `CLOSED`, state reason
  `COMPLETED`, on 2026-08-17. Its `CHANGELOG.md` carries, under 2.1.277, "Added AGENTS.md support: in
  a project with no CLAUDE.md, Claude Code reads AGENTS.md instead", and under 2.1.281 the widening
  to Bedrock, Vertex, Foundry, gateways and telemetry-off sessions. Measured 2026-10-04 on node a.
  The CLI on node a's PATH reports 2.1.178, older than both, so the import still binds on this node.
- The Claude Code claim is spelled in five places outside records: the README twice, the adopter's
  header, `AGENTS.md` line 14, and the charter template's §6 with its render at `AGENTS.md`
  lines 215-216. This unit takes the first four.
- The kit's `kit.toml` declares no version constant, so no kit-version carrier moves.

### Files touched (estimate)

- `tools/agent-instructions/adopt-agent-instructions.sh`
- `tools/agent-instructions/README.md`
- `tools/agent-instructions/adopt-agent-instructions.test.sh`
- `AGENTS.md`

### Rollout

The announce reaches an adopter on its next kit update. On this repo the `agent-instructions
wiring` leg prints it on every bar until `AGENTS.md` falls under 32 KiB, which is the point: the
fact is now visible where the wiring is graded.

### Alternatives rejected

- **Refusing a file over 32 KiB.** The kit is not the only reader and Codex can be configured past
  the default; a refusal would red every charter adopter for a choice that is theirs.
- **Announcing on the install path only, as the report words it.** Install runs once per adopter;
  `--check` runs on every bar, which is where a growing file is seen growing.
- **Dropping the `claude` alias now that the CLI reads `AGENTS.md`.** It reads it only when no
  `CLAUDE.md` exists, and node a's own CLI predates the support.

## 5. Production-readiness checklist

- security — N/A — one `wc -c` comparison and prose; no new write path.
- perf / scale — one extra `wc -c` per run.
- error / empty / loading states — an unreadable canonical is already an exit 2 before either path
  reaches the comparison.
- observability — the announce line is the observability.
- risks — the vendor default can move; S5's stamp dates the figure, and AC6 re-observes it at build.
- testing — AC1 to AC7 directly; one arm in the kit suite under `New arm:`.
- migration — N/A — no stored state.
- user docs — the kit README is the user doc, S3 to S5.

## 6. Acceptance criteria

- **AC1** — When a scratch git repo under a short `%TEMP%` path is given a 40,000-byte source and
  `bash tools/agent-instructions/adopt-agent-instructions.sh --source <that file>` runs there, its
  output carries `over 32768` on the line after `canonical:` and it exits 0.
  Red when: no announce prints, or the exit status moves.
- **AC2** — When `adopt-agent-instructions.sh --check` runs in that repo, it prints the announce and
  exits 0; when `AGENTS.md` is then truncated to exactly 32768 bytes with `head -c` and the check
  re-runs, it prints no announce and exits 0.
  Red when: the boundary is off by one, or the note changes the check's verdict.
- **AC3** — When `bash tools/agent-instructions/adopt-agent-instructions.sh --check` runs at the repo
  root, it prints the announce naming the byte count `wc -c < AGENTS.md` prints, and exits 0.
  Red when: the repo's own oversized charter goes unannounced.
  figure: the byte count is DERIVED at observation time.
- **AC4** — When `grep -c "nothing extra" tools/agent-instructions/README.md` runs it prints 0, and
  `grep -n "project_doc_max_bytes" tools/agent-instructions/README.md` hits the Codex row.
  Red when: the row still promises nothing extra.
- **AC5** — When `git grep -n -i "does not read" -- tools/agent-instructions/` runs it prints
  nothing, and `git grep -n "2.1.277" -- tools/agent-instructions/` hits both the README and the
  adopter.
  Red when: a carrier still states the pre-2.1.277 behaviour as current.
- **AC6** — When, at the build pass, `gh api` fetches the raw bytes of the Codex config source S5
  names and they are searched with `grep -F "32 * 1024"`, and the same call fetches the Claude Code
  changelog S5 names and it is searched with `grep -F "Added AGENTS.md support"`, both hit; and
  `grep -c "verified 2026" tools/agent-instructions/README.md` prints at least 2.
  Red when: a stamp is written without its probe hitting, or a probe misses and the claim is
  stamped anyway.
  permission: network and an authenticated `gh`; a pass without either parks the unit rather than
  stamping.
- **AC7** — When `sed -n 14p AGENTS.md` runs it names the kit README and not the Claude Code
  behaviour; `bash tools/check-template-size.sh AGENTS.md` exits 0; and
  `bash tools/playbook/adopt-playbook.sh --target . --check` exits 0.
  Red when: the wrapper still restates the fact, outgrows its row, or the edit disturbs the render.

## 7. Gates

`agent-instructions wiring` · `agent-instructions self-test` · `charter size` · `playbook render wiring` · `line length` · `spec tokens (a spec's own names resolve)`

New arm: `tools/agent-instructions/adopt-agent-instructions.test.sh` · a canonical of 32769 bytes announces on install and on `--check`, one of 32768 does not · none

## 8. Open questions

- **F1 — Does the announce run on `--check` too?**
  Options: the install path only, as the report words it; both paths. Install runs once per adopter
  and `--check` runs on every bar.
  RESOLVED (agent, 2026-10-04, delegated): both, per S1 and S2.
- **F2 — Does the charter template's §6 sentence move in this unit?**
  Options: here; a unit of its own. It is a template edit priced by the template size gate's
  high-water and rendered into `AGENTS.md` by the playbook renderer, a different mechanism and
  write set from this kit.
  RESOLVED (agent, 2026-10-04, delegated): split — the charter template's §6 "Claude Code cannot
  read" clause and its render in `AGENTS.md` move to a new unit the run adds.
- **FACT-QUESTION · F3 — Is the README's Claude Code claim stale?**
  Probe: `gh issue view 6235 --repo anthropics/claude-code --json state,stateReason` and a `grep`
  of that repo's `CHANGELOG.md` for `AGENTS.md`. Observation: the issue closed COMPLETED on
  2026-08-17 and 2.1.277 added the support. Liveness: the same grep for `CLAUDE.md` hits many
  entries, so a miss on `AGENTS.md` would have been a real negative.
  RESOLVED (agent, 2026-10-04, delegated): stale; restated per S4.

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft, from the kit's adopter and README at base, the vendor issue
  and changelog, and the Codex source, all read 2026-10-04.
- rev-2 · 2026-10-04 · §3 · M2 cross-read: the §8 F2 split was named only as a unit the run adds;
  it is `PLAY-aMendedFleet-3`, so the non-goal and the hands-off edge now name it.

## 10. Reuse audit

No existing seam fits. The size checker `tools/check-template-size.sh` is gov-internal and a
copy-installed kit names nothing outside itself, so the announce is one comparison in the adopter
beside the count it already prints. `python tools/codebase-map/reuse_lookup.py "warn when an
instruction file exceeds a byte limit another tool reads"` returned only name-stem neighbours,
`read_text` and `read_conf` among them, and reported `unscanned layers: .sh`, so a grep of
`tools/**/*.sh` for `32768` and `KiB` supplied the shell half and found only size-limit rows. Recall
returned `PLAY-aSiftedPlaybook-3`, which wrote the charter sentence F2 splits off;
`aFusedCharter`'s README, recording that `@`-imports are Claude Code syntax and `AGENTS.md` cannot
import a second file, which is why the import direction stays; and `TOOL-dSettledRoster-1`, that no
path gate reaches `AGENTS.md`, which this unit does not change. Where the report and the tree
disagree: the report named only the Codex row as stale; the Claude Code claim went stale on
2026-08-17, after the kit was written.

Recall terms used: `python tools/memory-recall/query.py "why does the agent-instructions kit wire
CLAUDE.md to AGENTS.md and what does each tool read" --terms "agent-instructions AGENTS.md CLAUDE.md
import canonical alias wiring Codex Gemini pointer mode natively"`
