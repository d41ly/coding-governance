# PLAY-aFusedCharter-1 — the playbook converges into one file, and loses what does not govern a session

**Status:** OPEN · rev-2 · 2026-08-18 · node a · Tier-2 · base 497d25d0 · streams playbook

## 1. Goal

Fold `parallel-coding-governance.domain-rules.md` back into the operating ruleset, delete the
sections that govern a project's domain rather than a session's conduct, and mark what remains so a
renderer can drop the parts a target has no kit for. The product becomes one file an adopter
receives whole, instead of a ruleset plus a companion that keeps falling out of the deploy path.

## 2. Scope (IN)

**S1 — Fold every `§`-stub into its own section.** Six sections in the ruleset are stubs whose body
lives in the companion: `§1`, `§7`, `§8`, `§9`, `§11`, `§12`. For each, delete the
`… → parallel-coding-governance.domain-rules.md §N. LOAD when …` bullet and append the companion
section's bullets in their existing order under the same heading. The companion's own preamble,
which explains the split and the lockstep re-pull, is deleted with it — after this unit there is no
second file to re-pull.

**S2 — Delete `§4` whole**, both carriers. Port offsets, one-server-per-canonical-port, build-time
versus runtime configuration, the monorepo launch-scope trap, the full-stack verify recipe, the
per-node harness pin and the harness false-signal list. Its three placeholders `{{PORT_OFFSET}}`,
`{{BUILD_TIME_BAKES}}` and `{{VERIFY_RECIPE}}` go with it. `§8`'s "verify before done" rule
currently offers "the `§4` harness" as one of three witnesses; that clause loses the third option
and keeps the other two.

**S3 — Delete `§10`'s twenty-five bug classes**, replacing both the stub and the companion body with
a single rule under the retained heading: every Tier-2 review runs the project's own recurring-class
checklist, and every confirmed finding is left-shifted into a gate or into that checklist. The rule
names no kit; a project without one has a documented manual checklist and the rule still reads true.

**S4 — Delete `§13` whole**, both carriers, with its seven placeholders.

**S5 — Fold `§17` into `§16`** as two bullets at the end of the micro-format section — the clickable
link format, and the session-cwd href resolution with its worktree-segment trap. The `§17` heading
disappears. Sections are NOT renumbered: `§4`, `§10`, `§13` and `§17` become absent numbers, because
renumbering breaks every cross-reference in the file and every citation of this playbook in this
repo's records.

**S6 — Move the kit-advertisement prose to `WIRE-INTO-PROJECT.md`, and add one sentence that is not
a move.** The `lexicon` kit is named in NO surviving carrier: measured with the parity gate's own
predicate, its only mention across the trio is in `parallel-coding-governance.customize.md`, which
this build deletes, and it holds no waiver row. `WIRE-INTO-PROJECT.md` therefore gains a lexicon
sentence as an ADDITION, or the kit-coverage arm reds the day the companion goes. Seven bullets
currently sell a
kit rather than state a rule: `§5`'s codebase-map, drift-audit and memory-recall bullets, `§6`'s
agent-instructions bullet, and `§7`'s pytest-parallel-guardrails, gate-lint and govkit bullets. Each
leaves behind the RULE it exists to enforce, stated without naming the kit, and its adoption case
moves to the runbook section that installs it. The memory-tree bullet in `§5` stays: it is marked
REQUIRED and `§5` and `§6` are both written against it.

**S7 — Move `§8`'s agent-cap hook grammar to `tools/hooks/README.md`, keeping two literals behind.**
The bullet retains: at most five agents in a verify stage and at most five running at once, they are
two rules and not one, batching grows the batch and never the agent count, and a hook enforces both
at the tool call. The marker spellings, the resolvable-bound rules and the direct-spawn slot
accounting move out. The bullet measures 1 474 characters today and is the file's longest.

**Two literal strings in that bullet CANNOT move, and this is the spec audit's first blocker.**
`tools/check-playbook-parity.sh`'s `PAIRS` declares two value-parity rows and BOTH take their stated
side from this file. Both extractions match exactly one line in the whole trio — the concurrency
bullet — and they read `array LITERAL of` a bound `elements` and the backticked hook matcher naming
both tool names. Move them and the gate hits its own anti-vacuity arm, which reds when an extraction
matches NOTHING. The retained bullet therefore carries both literals VERBATIM, in a form those two
`sed` extractions still match, and the build verifies that by RUNNING the gate rather than by reading
the bullet.

**`tools/hooks/README.md` does not exist and creating it is not free.** `git ls-files tools/hooks/`
returns three files, and that kit declares a non-flat `home`, so `govkit selfcheck`'s arm over
tracked files under a non-flat home reds on any file no `[[files]]` rule claims. S7 therefore CREATES
the README and adds a fourth `[[files]]` rule to `tools/hooks/kit.toml` shipping it — otherwise the
moved grammar either reds the deployer or is deleted rather than moved, and an adopter installing
`agent-cap` receives the hook without the grammar it enforces.

**S8 — Add conditional block markers, in TWO declared namespaces.** Every block the customize
companion lists under its conditional-sections heading gets an HTML-comment fence, so
`DEPL-aFusedCharter-1` can drop it mechanically. Markers are comments, so an unrendered file reads
correctly with every block present.

**One namespace is not enough, and the spec audit is right about why.** Four of the companion's
conditional rows are keyed on a PROJECT PROPERTY rather than on a kit: the security section's
outbound-call lines drop when there is no such surface, the cross-OS section drops for a single-OS
team, the design-system rules drop when there is no UI, and the persona is adjustable. The registry
has no `security` or `cross-os` entry id, so fencing those with a kit id would name an id the
renderer must refuse. `govkit` is a registry EXEMPTION rather than an entry, so a govkit fence would
fail the same check.

- `<!-- kit:` id `-->` … `<!-- /kit:` id `-->` — the id is a `tools/govkit/registry.toml` entry id,
  and the renderer drops the block when the target did not select that kit.
- `<!-- when:` key `-->` … `<!-- /when:` key `-->` — the key is a boolean answered in the target's
  `deploy.toml`, and the renderer drops the block when the answer is false. This is the namespace
  the four project-property rows use.

**S8's first deliverable is an ENUMERATION, not a fence.** The post-fold conditional set is not
knowable from the companion's list, because S6 moves seven kit-advertisement bullets out of the
ruleset entirely and a row whose block has left has nothing to fence. The build therefore enumerates
the surviving conditional blocks against the folded file BEFORE writing any fence, and records that
enumeration in the build folder. The spec audit left this open precisely because it cannot be sized
from the specs, and guessing it is how a fence lands over a block that is no longer there.

**One conditional subject is an inline mid-sentence clause, not a block.** The unattended landing
rule is a clause inside a sentence. S8 lifts it onto its own line before fencing it, rather than
teaching the renderer to drop an inline span — a span-dropping renderer has to reflow the sentence
around it, which is a second mechanism for one clause.

**S9 — Rewrite the preamble.** It currently describes the two-file deploy and the nine companion
checklists. It becomes: what the file is, that filling it is `DEPL-aFusedCharter-1`'s job and not a
reader's, that a wrapped line is still one rule, and where version history lives.

**S10 — Adopt four rules `AGENTS.md` states better than the ruleset does.** Each is a rule this
repo learned and the shipped playbook does not carry. They land as bullets in the named section.
`§6`: a value stated in prose beside the source that owns it rots between changes — point at the
source or gate the pair. `§7`: a gate's own header states what it does NOT check, because a
structural check reads as a semantic one to everybody who did not write it. `§7`: a probe that
cannot move says so — a signal with no liveness assertion reports a reassuring zero when it is
broken. `§7`: no count of a derived population is written in prose; the checker derives it.

## 3. Non-goals (OUT)

**No renumbering.** See S5.

**No rename, and no consumer repointed here.** The file keeps its current name through this unit and
`TOOL-aFusedCharter-1` owns the rename, the deletion of the sibling files as tracked paths, and
every gate, registry, dossier and conf that names them. The two units share one landing pass; the
split is by mechanism, not by commit.

**No micro-format content.** `PLAY-aFusedCharter-2` owns `§16`'s new block. This unit's `§16` work is
only S5's fold.

**No ceiling raise.** The converged file measures 43 998 bytes against a 49 152 ceiling. If a
build-time measurement disagrees, that is a fork for the owner, never a constant edit.

**`§9` and `§11` are not cut.** Both were tested against the admission test and pass: a security
boundary governs any unit adding a write path, and the cross-OS rules govern any fleet with more
than one operating system. Both are already project-conditional, and S8's `when:` namespace is what actually lets the renderer
drop them, since neither has a kit id it could be fenced with.

**No rewriting of surviving rules for style.** Deletion, folding and the ten S-items above. A rule
that survives keeps its words, except where S6 and S7 explicitly restate one.

## 4. Design

### Inventory

Measured at BASE. Section sizes are the ruleset's and the companion's, in bytes.

| Section | Ruleset | Companion | Disposition |
|---|---|---|---|
| `§0` TL;DR | 1 403 | — | keep; the runtime-isolation clause in its streams bullet drops |
| `§1` lifecycle | 3 601 | 1 384 | fold |
| `§2` nodes and IDs | 2 666 | — | keep |
| `§3` streams and worktrees | 1 873 | — | keep |
| `§4` runtime and harness | 396 | 1 554 | DELETE |
| `§5` memory and docs | 3 499 | — | keep, minus S6 |
| `§6` decisions and backlogs | 2 571 | — | keep, minus S6, plus one S10 rule |
| `§7` gates | 4 339 | 1 262 | fold, minus S6, plus three S10 rules |
| `§8` review protocol | 4 127 | 525 | fold, minus S7 |
| `§9` security | 566 | 2 414 | fold |
| `§10` bug classes | 330 | 7 752 | DELETE body, keep one rule |
| `§11` cross-OS | 396 | 1 427 | fold |
| `§12` architecture | 676 | 3 943 | fold |
| `§13` design system | 382 | 1 977 | DELETE |
| `§14` session hygiene | 1 879 | — | keep |
| `§15` voice | 1 117 | — | keep |
| `§16` output discipline | 4 712 | — | keep, plus S5's fold |
| `§17` file references | 651 | — | FOLD into `§16` |

Folded total, before S6, S7 and S10 adjust it: 43 998 bytes.

### Migration

The fold is mechanical enough to be checked rather than eyeballed. Before deleting the companion,
enumerate its bullets; after folding, assert that every bullet whose section survives appears once
in the converged file. This is a build-time check the author runs, not a shipped gate — the shipped
gate is `TOOL-aFusedCharter-2`'s, over a different property.

### Alternatives rejected

**Keep the companion and fix its deploy path instead.** Rejected by the owner's framing: the split's
cost is not only that the companion gets dropped, it is that two files carrying one version marker
in lockstep is a second answer to one question. The stub indirection also costs a load decision per
session, which is the thing this ruleset elsewhere refuses to spend.

**Renumber to close the gaps.** Rejected in S5's terms.

**Move `§4`, `§10` and `§13` to an optional non-deployed reference file.** Rejected by the owner:
that is the shape being retired, one level down.

### Files touched (estimate)

`parallel-coding-governance.template.md` (rewritten), `parallel-coding-governance.domain-rules.md`
(emptied — deleted as a tracked path by `TOOL-aFusedCharter-1`), `WIRE-INTO-PROJECT.md` (S6),
`tools/hooks/README.md` (S7, CREATED), `tools/hooks/kit.toml` (S7, a fourth `[[files]]` rule), and
one new record under `memory/builds/aFusedCharter/build/` holding S8's conditional-block enumeration.

## 5. Production-readiness checklist

- security — `§9` survives whole and gains nothing; the deleted sections carry no security rule.
- perf / scale — N/A, a document.
- a11y — N/A for the document itself. `§13`'s deletion removes the contrast-gate rule from the
  shipped product, which is a real loss for UI adopters and is named as a follow-up.
- i18n — N/A.
- error / empty / loading states — N/A.
- observability — the converged file's size is observable through the existing size gate.
- risks — the fold can silently drop a bullet, and the Migration check above is the mitigation.
  Landing without `TOOL-aFusedCharter-1` reds three legs; the build README makes the two one pass.
- testing + left-shift gates — no new gate here. `TOOL-aFusedCharter-2` and `-3` add them.
- migration / rollback — a document edit; `git revert` restores both files.
- user docs — `WIRE-INTO-PROJECT.md` receives S6 and is itself the user doc.

## 6. Acceptance criteria

- **AC1** — When the fold is complete, `grep -c 'domain-rules' parallel-coding-governance.template.md`
  returns `0` and every surviving companion bullet is present once in the converged file.
- **AC2** — When `bash tools/check-template-size.sh` runs against the converged file, it exits 0 and
  prints a byte count under `49152`; the printed number, not this spec's estimate, is the record.
- **AC3** — When the section headings are enumerated with `grep -nE '^## '`, the four cut numbers are
  absent and the retained bug-class and output-discipline headings are present. The check is written
  against that enumerated output rather than as a regex containing the section glyph: that glyph is
  two UTF-8 bytes, and the same pattern was MEASURED returning 3 matches under `LC_ALL=C.UTF-8` and
  0 under `LC_ALL=C` and under this node's ambient environment — so a regex form would satisfy its
  negative half over the UNCHANGED file and fail its positive half after correct work.
- **AC4** — When the surviving bug-class section is read it states one rule and names no class, so
  `grep -c 'Client/server validation divergence' parallel-coding-governance.template.md` returns `0`.
- **AC5** — When the conditional blocks are marked, the enumeration S8 requires exists in the build
  folder, every id inside a `<!-- kit:` fence is a real entry id in `tools/govkit/registry.toml`,
  every key inside a `<!-- when:` fence is answered in this repo's own `deploy.toml`, and every
  opened fence is closed. No fence names `govkit`, which is an exemption rather than an entry.
- **AC6** — When the four adopted rules land, each is greppable in its stated section: the liveness
  rule contains `DEAD PROBE` and the derived-count rule contains `derives`.
- **AC7** — When the seven kit-advertisement bullets are moved, every kit named in one is still
  reachable from `WIRE-INTO-PROJECT.md`, so `bash tools/check-playbook-parity.sh` reports no kit
  newly unnamed AND its two value-parity rows still resolve. Checked by RUNNING that gate after
  `TOOL-aFusedCharter-1` amends its file list, never by reading the bullets.
- **AC8** — When `lexicon` is searched for across the surviving carriers with the parity gate's own
  predicate, it is named in one. It is reachable today ONLY from
  `parallel-coding-governance.customize.md`, which this build deletes, and it has no row in
  `tools/playbook-kit-waivers.txt` — so without a new sentence the kit-coverage arm reds on it.
- **AC9** — When `python tools/govkit/govkit.py selfcheck` runs after S7, it exits 0 with
  `tools/hooks/README.md` claimed by a `[[files]]` rule in that kit's descriptor.

## 7. Gates

`template size <=48KiB` · `playbook parity` · `playbook placeholder catalogue` · `memory hygiene` ·
`install-prefix (shipped surface)` · `codebase-map coverage + freshness` · `govkit selfcheck` (S7
creates a file under a non-flat kit home) · the full bar at the push boundary. No new leg.

## 8. Open questions

none — the forks below are RESOLVED and their resolutions are recorded in the build README.

- **F1 — how does `AGENTS.md` relate to the converged file?** RESOLVED (owner, 2026-08-18): a
  `gov:playbook` marker region holding the render, with project content in authored slots outside
  it. Owned by `PLAY-aFusedCharter-3`; this unit only has to leave the file renderable.
- **F2 — what happens to the twenty-five bug classes?** RESOLVED (owner, 2026-08-18): deleted
  outright. They are not seeded into any kit, and the mechanism that replaces them is the project's
  own per-path checklist.
- **F3 — which further trims?** RESOLVED (owner, 2026-08-18): the kit-advertisement prose, the
  agent-cap hook grammar, and `§17` folded into `§16`. `§9` and `§11` stay.

## 9. Revision log

- rev-1 · 2026-08-18 · initial draft, written after the owner resolved F1 through F3 at kickoff.
- rev-2 · 2026-08-18 · folded the M4 spec audit. S7 keeps the two value-parity literals the gate
  extracts from this file and now CREATES the hooks README with a descriptor rule, S8 gains a second
  fence namespace for the four project-property conditionals plus a required enumeration pass and the
  inline-clause lift, S6 gains the lexicon sentence that is an addition rather than a move, AC3 is
  rewritten off a locale-dependent regex, and three ACs are added for what the audit found
  unobserved.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "the governance playbook and the gates over its claims"`
routes to `memory/map/features/playbook.md`, which owns the size gate, the parity gate and the
placeholder gate. This unit extends the SUBJECT those gates measure and adds no seam of its own; the
seams it must not break are `tools/check-template-size.sh`'s per-subject key in
`tools/template-size-limits.txt` and `tools/check-playbook-parity.sh`'s three-file precondition,
both repointed by `TOOL-aFusedCharter-1`.

`python tools/memory-recall/query.py` was run with terms
`playbook template companion customize domain-rules agnostic adopter externalize byte gate section stub kit wiring marker lockstep`.
The binding prior records are `PLAY-aCandidStub-1`, whose fifteen convergence defects were all
caused by the three-file split, and `TOOL-aSiftedPlaybook-1`, which raised the ceiling to 48 KiB and
replaced it with a high-water ratchet — the headroom this unit spends exists because of that unit.
`PLAY-aCandidStub-2` is an OPEN row asking to externalize `§14`; this unit moves the opposite way
and that row needs a disposition at landing.
