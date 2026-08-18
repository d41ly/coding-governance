# TOOL-aFusedCharter-1 — the product becomes one tracked path, and every consumer of the old three is repointed

**Status:** OPEN · rev-3 · 2026-08-18 · node a · Tier-2 · base 497d25d0 · streams tooling

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
  Its `PAIRS` rows are NOT repointed: both take their stated side from the ruleset, and
  `PLAY-aFusedCharter-1` S7 keeps the two extracted literals in the file rather than moving them,
  which is the resolution of the audit's first blocker. Repointing them at
  `tools/hooks/README.md` would make the gate's "stated" side a file the playbook does not itself
  ship — a change to what this gate is FOR — and `§8` records it as an owner fork rather than
  taking it here.
- `tools/check-placeholders.sh` — the marker lockstep compared TWO carriers. With one carrier a
  comparison is not available, so the assertion becomes presence plus well-formedness of the single
  marker, and the header states plainly that the lockstep question died with the second file rather
  than being weakened. The `--check <a> <b>` survival mode is untouched; it takes explicit
  arguments and never reads a tracked source.
- `tools/check-install-prefix.sh` — its shipped-surface population names the playbook files.

**S4a — Lower the parity gate's arms floor, in the same commit that deletes its branches.**
`.memory-tree.conf`'s `ARMS_FLOORS` pins `tools/check-playbook-parity.sh` at a branch/armed pair of
15 and 15. S3 deletes the catalogue stage, which is six `fail` call sites, so the gate reads 9 and
`check-arms.py` emits its shrink-only refusal — *a guard or an assertion was removed; lower the floor
in a commit that says why*. This unit lowers the pair to the MEASURED post-deletion value, with the
reason beside it, and retires the matching arms in `tools/check-playbook-parity.test.sh`. The floor
is derived by running the harness after the deletion, never predicted here: a floor written from a
prediction is a floor nobody measured.

**S4 — Repoint the declarations and records.** `tools/template-size-limits.txt` and
`tools/template-size-highwater.txt` are keyed by repo-relative path: both rows are rewritten to the
new key, and the limits file gains a comment line recording that the key moved and why, per that
file's own stated grammar. `tools/playbook-kit-waivers.txt`, `.gitattributes` (whose
`parallel-coding-governance*.md` pattern would silently stop matching), and `.memory-tree.conf`'s
stream comment.

**S4b — Pin the line endings the render path depends on, which nothing pins today.** Measured on this
node: `core.autocrlf` is `true`, the ruleset is `eol: lf`, and `AGENTS.md` is `eol: unspecified` —
its committed blob holds zero carriage returns while the worktree copy holds 302. A region rendered
from an LF source and byte-compared against a CRLF charter mismatches on every line, on every node in
the registry, and `bash tools/playbook/adopt-playbook.sh --check` would red permanently for a reason
that has nothing to do with drift. This unit adds `eol=lf` rows for `AGENTS.md`, for
`.governance/deploy.toml` and for `tools/line-length-limits.txt`, alongside the renamed ruleset's.
`DEPL-aFusedCharter-1` independently normalises before comparing, because a pin an adopter has not
adopted protects nobody — the two mitigations are deliberate belt and braces for a failure that is
silent and per-node.

**S5 — Repoint the deployer, including three sites an earlier revision missed.**
`tools/govkit/registry.toml`'s `[surface]` globs name two `parallel-coding-governance*` patterns;
`tools/govkit/entries/playbook.kit.toml` names both deployed files in two `[[files]]` rules, in its
`claims`, in its `lf_pin` pattern and in the `playbook-placeholders` hole's discharge command.
`tools/govkit/selftest.py` names the companion. The second `[[files]]` rule is DELETED with the file
it ships. The three the spec audit found:

- **The `[[exempt]]` row naming `parallel-coding-governance.customize.md`.** S2 deletes that path and
  `selfcheck` reds on an exemption whose path no longer exists — which is exactly the property that
  row's own design was built to have, firing correctly against us.
- **The registry's reason string** for the playbook exemption, which says the parity gate reads this
  repo's customize arithmetic. S3 deletes that arithmetic, so the reason becomes false prose inside
  the file whose whole thesis is that declarations do not drift.
- **The entry's `version_from`**, which names the template by its old filename. `selfcheck` reds with
  *version_from names a file that does not exist*, and AC7's shape predicate would not have caught it
  because the entry would still parse.

**S6 — Repoint the prose consumers**, each of which is product an adopter or a session reads:
`README.md`, `WIRE-INTO-PROJECT.md`, `AGENTS.md`, `skills/session-kickoff/SKILL.md` and
`MANIFEST-TEMPLATE.md`, `tools/agent-instructions/README.md`, `tools/gate-lint/README.md`,
`tools/memory-tree/README.md`, and `memory/backlog/PLAY.md`.

**The kickoff manifest names the template at five lines, not one.** `memory/guides/SESSION-KICKOFF.md`
carries it in `watch:`, in `verify-paths:` — both of which `manifest-check.sh` checks as separate
contracts — and in three body lines, one of which is the playbook routing row that ALSO asserts "the
three `parallel-coding-governance.*` files" and "TWO carriers". Those two claims are prose this build
falsifies, so the row is rewritten rather than path-substituted, and the manifest is re-stamped with
a delta line in this commit.

**Four map dossiers carry claims this build falsifies, and three of them cannot be found by
searching for the old filenames.** `memory/map/features/playbook.md` needs its `paths.globs` and its
prose. Beyond it: the lexicon dossier states that TWO files carry the version marker and not three,
which S8 reduces to one; the unattended dossier states that the unattended rules live in the
domain-rules companion; and the govkit dossier states that the customize companion is explicitly not
shipped. None of the three spells `parallel-coding-governance`, so AC1's completeness grep is blind
to all of them — which is why they are enumerated here instead. The generated map artifacts are
re-rendered in the same commit.

**S7 — Repoint the hook and BOTH drift-signal glob lists.** `.githooks/pre-commit` stages a check on
the template by name. `tools/drift-audit/drift_signals.py` enumerates all three paths TWICE, in two
lists that are deliberately different sizes: `PRODUCT_GLOBS` and the narrower `TRACE_GLOBS`, whose
own comment says it is narrower on purpose and which feeds a pinned signal. Repointing one and not
the other silently shrinks the trace haystack and drifts a pin for a reason unrelated to this build —
a signal moving because a glob stopped matching looks exactly like a signal moving because the tree
improved.

**S8 — Move the version marker once.** The converged file carries one
`<!-- governance-template: vN.N -->`, bumped to the next minor at this landing and not before.
`PLAY-aFusedCharter-1`, `-2` and `-3` all touch the document and none of them bumps it; a marker
moved mid-build would describe a partial change.

**S9 — Leave the frozen records alone, and say so in the commit.** Many files under
`memory/builds/` and `memory/archive/` name one of the three paths, and **no count is written here**
— the figure moves as this very build adds records, and an earlier revision of this spec stated one
that was already wrong by the time it was committed. Derive it when you need it:
`git grep -lF 'parallel-coding-governance' -- memory/builds memory/archive | wc -l`. Those files are
append-only decision records and version snapshots; rewriting them would falsify what a prior unit
actually decided against. The
`dead path cites` counter in `python tools/memory-tree/corpus_ids.py --report` reads `0` today and
must still read `0` after the rename, so the exclusion has to be a rule the checker already holds
rather than an assertion here. If it does not hold, that is a fork, not a licence to rewrite
history.

**S10 — Retire the charter-completeness drift signal, HERE rather than in the unit that cuts the
charter.** `_charter_mentions_every_leg` asserts that `AGENTS.md`'s gate-suite section cites every
leg's argv script path. It measures `0 of 70` against a pin of 0 and it is GATEABLE, so it reds the
moment a leg exists that the charter does not name. Three later units — `DEPL-aFusedCharter-1`,
`TOOL-aFusedCharter-2` and `TOOL-aFusedCharter-3` — each add a leg, and the charter bullets that
would name them never arrive, because `PLAY-aFusedCharter-3` deletes that section outright. On the
build's stated order three units red `drift-audit records` with no unit owning the fix. That is the
spec audit's third blocker and this is where it resolves: retiring the signal in the FIRST unit costs
nothing, since between here and the cut the charter still names every pre-existing leg and the
section is deleted regardless.

The mechanism is precise, and an earlier draft of this scope item got it wrong in three ways. The
probe is one row in a `HANDKEPT` list; the retirement is to DELETE that row and add the SIGNAL name
`handkept_inventories_disagreeing_with_source` to `DECLARED_EMPTY`. It then renders as *empty by
declaration*, which is the honest reading and is what the kit's liveness rule asks for here — NOT
`NOT ASKED`, which is a separate engine flag that sets the signal non-gateable and which
`drift_report.py`'s own comment records rejecting for this route deliberately. `PINS` is not touched.
`tools/drift-audit/selftest.py` is not touched either: it carries no arms for this probe, its fixture
already writes an empty `HANDKEPT`, and it already uses this very signal name as the literal its
`DECLARED_EMPTY` arms exercise.

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

Measured with `git grep -lF 'parallel-coding-governance'` at BASE `497d25d0`: 31 live consumers.
That figure is a BASE-time snapshot of the set this unit must repoint, and AC1 re-derives it rather
than trusting it. The frozen-record population is deliberately uncounted, per S9. Live consumers,
grouped by what breaks if one is missed.

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

`playbook parity` and its self-test · `harness arms` · `govkit selfcheck` · `drift-audit records` ·
`kickoff-manifest ratchet` · `codebase-map coverage + freshness` · `memory hygiene`. And then
every leg. This unit's blast radius is the gate suite itself, so the diff-scoped run is not
meaningful here and the full bar is the acceptance instrument — `GATE_FULL=1 bash tools/run-gates.sh`.

## 8. Open questions

none blocking — F1 is RESOLVED; F2 is an OWNER fork the build can proceed without, because its
recommendation is the status quo.

- **F1 — does `corpus_ids.py`'s dead-path checker already exempt frozen records?** RESOLVED (agent,
  2026-08-18, delegated), and the fork was CLOSED BEFORE IT WAS ASKED, which the spec audit is right
  to call out. `corpus_ids.py` restricts its dead-path population to a named set of files under the
  memory root plus four directories, and `builds/` and `archive/` were never candidates; it also
  discards any token with no path separator, which the template's bare filename has none of. So
  `dead path cites` reads 0 after the rename for two reasons, NEITHER of them the exemption the fork
  asked about. AC8 is kept as a regression observation and is honestly labelled as one — it cannot
  come out the other way, and an acceptance criterion that cannot fail is exactly what this repo's
  own gate-discipline rules call an assertion about nothing. The real risk it was reaching for is
  covered instead by S9's rule and by AC1's two-sided grep.
- **F2 — should the parity gate's two value-parity rows keep taking their stated side from the
  playbook, or move to `tools/hooks/README.md` with the grammar?** Recommendation: KEEP them in the
  playbook, which is what `PLAY-aFusedCharter-1` S7 assumes and what this unit builds. That gate's
  whole subject is *a value the playbook STATES equals the source that OWNS it*, so a stated side
  living in a file the playbook does not ship changes what the gate is FOR. That is a change to a
  governance carrier, which the build method makes an owner turn rather than a delegated one — so it
  is raised here rather than taken. Proceeding on the recommendation costs nothing if the owner
  later moves it.

## 9. Revision log

- rev-1 · 2026-08-18 · initial draft. The consumer inventory is measured, not recalled.
- rev-3 · 2026-08-18 · folded the M4 spec audit. New S4a lowers the parity gate's arms floor with
  the branch deletion, new S4b pins the line endings the render comparison depends on, new S10 moves
  the charter-completeness signal retirement here from `PLAY-aFusedCharter-3` because three later
  units add a leg and would each red a zero-pin signal, S5 gains the exemption row plus the reason
  string plus `version_from`, S7 gains the second glob list, S6 gains the manifest's five lines and
  three more dossiers, S3 records why `PAIRS` is not repointed, and F1 is re-marked as a fork that
  was closed before it was asked.
- rev-2 · 2026-08-18 · S9 stated a frozen-record count that the tree moved underneath within the
  same session, because this build's own spec files join that population. The count is deleted and
  replaced with the derivation. Second instance of the class in one session, after
  `DEPL-aFusedCharter-1` rev-2 — which is evidence for `PLAY-aFusedCharter-1` S10's rule that a
  derived population's size is never written in prose.

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
