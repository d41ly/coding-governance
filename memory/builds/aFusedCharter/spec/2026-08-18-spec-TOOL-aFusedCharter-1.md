# TOOL-aFusedCharter-1 — the product becomes one tracked path, and every consumer of the old three is repointed

**Status:** OPEN · rev-1 · 2026-08-18 · node a · Tier-2 · base 497d25d0 · streams tooling

## 1. Goal

Rename the converged ruleset to `coding-governance-agents.template.md`, delete the two sibling files
as tracked paths, and repoint every gate, registry, hook, conf, dossier and runbook that names any
of the three. The rename is the cheap half; the consumer surface is the unit.

## 2. Scope (IN)

**S1 — Rename with `git mv`**, so history follows: `parallel-coding-governance.template.md` becomes
`coding-governance-agents.template.md`. The new name says what the file BECOMES in a target, which
is the whole correction — the old name described a topic, and the file it renders into is
`AGENTS.md`.

**S2 — Delete `parallel-coding-governance.domain-rules.md` and `parallel-coding-governance.customize.md`
as tracked paths.** `PLAY-aFusedCharter-1` empties the first into the converged file;
`DEPL-aFusedCharter-1` absorbs the second's mechanical half into a renderer and its non-mechanical
half into `WIRE-INTO-PROJECT.md`. This unit performs the `git rm`, and it performs it in the same
commit as S1 so no intermediate tree has a stub pointing at an absent file.

**S3 — Repoint the four gates that name a path.**

- `tools/check-template-size.sh` — the header's examples and the remedy string inside the
  over-budget message, which tells the reader to move a section into the companion. The remedy
  becomes: trim non-instructional prose, or drop a kit-conditional block.
- `tools/check-playbook-parity.sh` — three variables (`TEMPLATE`, `CUSTOMIZE`, `DOMAIN`) become one,
  the three-file existence precondition becomes one file, and S3 of that gate — the catalogue
  arithmetic asserting `customize.md`'s placeholder counts — is DELETED, because its subject no
  longer exists. Its S1 kit-coverage grep loses two of its three haystacks; the surviving haystack
  is the converged file plus `WIRE-INTO-PROJECT.md`, which is where `PLAY-aFusedCharter-1` S6 moves
  the kit prose. Without that second haystack the gate reds on seven kits the day it lands.
- `tools/check-placeholders.sh` — the marker lockstep compared TWO carriers. With one carrier a
  comparison is not available, so the assertion becomes presence plus well-formedness of the single
  marker, and the header states plainly that the lockstep question died with the second file rather
  than being weakened. The `--check <a> <b>` survival mode is untouched; it takes explicit
  arguments and never reads a tracked source.
- `tools/check-install-prefix.sh` — its shipped-surface population names the playbook files.

**S4 — Repoint the declarations and records.** `tools/template-size-limits.txt` and
`tools/template-size-highwater.txt` are keyed by repo-relative path: both rows are rewritten to the
new key, and the limits file gains a comment line recording that the key moved and why, per that
file's own stated grammar. `tools/playbook-kit-waivers.txt`, `.gitattributes` (whose
`parallel-coding-governance*.md` pattern would silently stop matching), and `.memory-tree.conf`'s
stream comment.

**S5 — Repoint the deployer.** `tools/govkit/registry.toml`'s `[surface]` globs name two
`parallel-coding-governance*` patterns; `tools/govkit/entries/playbook.kit.toml` names both deployed
files in two `[[files]]` rules, in its `claims`, in its `lf_pin` pattern and in the
`playbook-placeholders` hole's discharge command. `tools/govkit/selftest.py` names the companion.
The second `[[files]]` rule is DELETED with the file it ships.

**S6 — Repoint the prose consumers**, each of which is product an adopter or a session reads:
`README.md`, `WIRE-INTO-PROJECT.md`, `AGENTS.md`, `memory/guides/SESSION-KICKOFF.md` (the kickoff
manifest — a `watch:` entry names the template, so the manifest is re-stamped with a delta line in
this commit), `skills/session-kickoff/SKILL.md` and `MANIFEST-TEMPLATE.md`,
`tools/agent-instructions/README.md`, `tools/gate-lint/README.md`, `tools/memory-tree/README.md`,
`memory/map/features/playbook.md` (its `paths.globs` and its prose), and `memory/backlog/PLAY.md`.

**S7 — Repoint the hook and the drift signals.** `.githooks/pre-commit:51` stages a check on the
template by name. `tools/drift-audit/drift_signals.py` names all three files in its product globs.

**S8 — Move the version marker once.** The converged file carries one
`<!-- governance-template: vN.N -->`, bumped to the next minor at this landing and not before.
`PLAY-aFusedCharter-1`, `-2` and `-3` all touch the document and none of them bumps it; a marker
moved mid-build would describe a partial change.

**S9 — Leave the frozen records alone, and say so in the commit.** 60 files under `memory/builds/`
and `memory/archive/` name one of the three paths. Those are append-only decision records and
version snapshots; rewriting them would falsify what a prior unit actually decided against. The
`dead path cites` counter in `python tools/memory-tree/corpus_ids.py --report` reads `0` today and
must still read `0` after the rename, so the exclusion has to be a rule the checker already holds
rather than an assertion here. If it does not hold, that is a fork, not a licence to rewrite
history.

## 3. Non-goals (OUT)

**No content edit.** Every byte of rule text belongs to `PLAY-aFusedCharter-1`, `-2` and `-3`. This
unit moves paths and rewrites the strings that name them.

**No new gate.** The gates this unit touches are amended, never added to. `TOOL-aFusedCharter-2` and
`-3` add legs.

**No rewriting of records under `memory/builds/` or `memory/archive/`.** See S9.

**No govkit behaviour change.** The registry and the descriptor are DATA, and this unit edits data.
`DEPL-aFusedCharter-1` changes what the deployer DOES.

## 4. Design

### Inventory

Measured with `git grep -lF 'parallel-coding-governance'` at BASE: 31 live consumers plus 60 frozen
records. Live consumers, grouped by what breaks if one is missed.

| Group | Files | Failure mode if missed |
|---|---|---|
| gates | `check-template-size.sh` · `check-playbook-parity.sh` · `check-placeholders.sh` · `check-install-prefix.sh` and the three sibling `.test.sh` | the leg reds, loudly — the cheap class |
| declarations | `template-size-limits.txt` · `template-size-highwater.txt` · `playbook-kit-waivers.txt` · `.gitattributes` · `.memory-tree.conf` | SILENT. A limits row keyed on an absent path falls through to the hard default, and a `.gitattributes` pattern that stops matching drops the LF pin on a byte-gated file |
| deployer | `govkit/registry.toml` · `govkit/entries/playbook.kit.toml` · `govkit/selftest.py` | `selfcheck` reds on the surface, or worse, ships an adopter a dead path |
| hook and signals | `.githooks/pre-commit` · `drift-audit/drift_signals.py` | SILENT. A staged-path check on an absent name never fires |
| prose an adopter reads | `README.md` · `WIRE-INTO-PROJECT.md` · `AGENTS.md` · `SESSION-KICKOFF.md` · two kickoff files · four kit READMEs · the map dossier · `backlog/PLAY.md` | a dead path in a document, which the install-prefix gate catches for kit paths but not for these |

The two SILENT groups are why this is Tier 2. A rename whose only failure mode were a red gate would
be Tier 1.

### Migration

Order inside the single commit: `git mv`, then `git rm` the two siblings, then the string rewrites,
then re-run the full bar. The rewrite is not a blind `sed`: `check-placeholders.sh` and
`check-playbook-parity.sh` need semantic amendments, not substitutions, and S3 states each.

After the rewrite, `git grep -lF 'parallel-coding-governance' -- . ':!memory/builds' ':!memory/archive'`
must return empty. That command is the unit's own completeness check and is written into the commit
message.

### Alternatives rejected

**Keep the old filename.** The owner named the new one. It is also the accurate one: the file
becomes `AGENTS.md`, and `parallel-coding-governance` describes a topic rather than an artifact.

**Rewrite the frozen records for consistency.** Rejected in S9's terms.

**Split this unit per consumer group.** Rejected: the groups share one commit by necessity, since an
intermediate tree with a renamed file and an unrepointed gate is a red bar.

### Files touched (estimate)

The 31 live consumers above, plus the two deletions and one rename.

## 5. Production-readiness checklist

- security — N/A; no write path changes. The `.gitattributes` pin is a data-integrity concern, not a
  security one, and is called out in the Inventory.
- perf / scale — N/A.
- a11y — N/A.
- i18n — N/A.
- error / empty / loading states — N/A.
- observability — the completeness grep in Migration is the observation.
- risks — the two SILENT consumer groups. Mitigated by asserting the effect rather than the edit:
  the LF pin is checked with `git check-attr`, and the limits row by running the gate and reading
  which limit it reports.
- testing + left-shift gates — the three sibling `.test.sh` files are amended alongside their gates,
  and the amendments are what prove the gates still red.
- migration / rollback — one commit, revertable. The rename carries history through `git mv`.
- user docs — `README.md` and `WIRE-INTO-PROJECT.md` are in S6.

## 6. Acceptance criteria

- **AC1** — When the landing commit is complete,
  `git grep -lF 'parallel-coding-governance' -- . ':!memory/builds' ':!memory/archive'` returns
  nothing, and the same grep WITHOUT the exclusions still returns the frozen records.
- **AC2** — When `git log --follow coding-governance-agents.template.md` runs, it shows the
  pre-rename history, proving the move was a `git mv` and not an add-plus-delete.
- **AC3** — When `bash tools/check-template-size.sh` runs with no argument, it measures
  `coding-governance-agents.template.md` against `49152` — not against the hard default — which is
  observable because the printed limit reads `49152` and the limits file's row names the new key.
- **AC4** — When `git check-attr text eol -- coding-governance-agents.template.md` runs, it reports
  `eol: lf`, proving the `.gitattributes` pattern still selects the renamed file.
- **AC5** — When `bash tools/check-playbook-parity.sh` runs, it exits 0, its catalogue arm is gone,
  and its kit-coverage arm searches the converged file and `WIRE-INTO-PROJECT.md` — verifiable by
  redding it: delete a kit's mention from both and confirm the gate names that kit.
- **AC6** — When `bash tools/check-placeholders.sh` runs it exits 0 over one carrier, and its
  `--check` mode still reds on a fixture pair carrying a surviving placeholder.
- **AC7** — When `python tools/govkit/govkit.py selfcheck` runs it exits 0, with the playbook entry
  declaring one `[[files]]` rule and a `playbook-placeholders` discharge probe naming one path.
- **AC8** — When `python tools/memory-tree/corpus_ids.py --report` runs, `dead path cites` reads
  `0`, unchanged from BASE.
- **AC9** — When `bash tools/run-gates.sh` runs with `GATE_FULL=1`, every leg is green, and the
  kickoff manifest carries a re-stamped `last-audit` with the delta line in this commit's message.

## 7. Gates

Every leg. This unit's blast radius is the gate suite itself, so the diff-scoped run is not
meaningful here and the full bar is the acceptance instrument — `GATE_FULL=1 bash tools/run-gates.sh`.

## 8. Open questions

none — the fork below is RESOLVED.

- **F1 — does `corpus_ids.py`'s dead-path checker already exempt frozen records?** RESOLVED (agent,
  2026-08-18, delegated by the build's stated order): AC8 makes it an OBSERVATION rather than an
  assumption. `dead path cites` reads `0` at BASE and must still read `0`; if the rename moves it,
  the unit stops and raises it to the owner rather than rewriting append-only records to satisfy a
  counter. The decision rule is stated, so the fork is closed even though the measurement is not yet
  taken.

## 9. Revision log

- rev-1 · 2026-08-18 · initial draft. The consumer inventory is measured, not recalled.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "renaming a shipped product file and its consumers"`
returns the `playbook` dossier for the gates and no seam for the rename itself — a rename has no
mechanism to extend. The seam this unit DOES reuse is `tools/check-template-size.sh`'s per-subject
key discipline: both the limits file and the high-water record are keyed by repo-relative path
precisely so a subject can move, and S4 exercises that design for the first time.

Recall terms used: `playbook template companion customize domain-rules rename consumer gate registry
declaration marker lockstep dead path`. The binding prior record is `TOOL-aSiftedPlaybook-1`, which
moved the size ceiling and established that the limits declaration outranks the environment — the
row this unit rewrites is the one that unit created. `TOOL-aTetheredConvoy-1` is an OPEN backlog row
reporting that the template reached the default branch carrying unresolved conflict markers with
both gates over it green; this unit rewrites both of those gates and should not close that row,
because the marker scan it asks for is still absent.
