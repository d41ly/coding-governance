# TOOL-aProvenReuse-2 — a `reuse-probed` DoD item joins the run to the recall query log

**Status:** CLOSED · rev-7 · 2026-08-31 · node a · Tier-2 · base 3bfc5e87 · streams tooling · order 2 · ratified 2026-08-31

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-31-build-TOOL-aProvenReuse-1-acceptance-ledger.md](../build/2026-08-31-build-TOOL-aProvenReuse-1-acceptance-ledger.md) | journal | TOOL-aProvenReuse-1 |
| [2026-08-31-prompt-TOOL-aProvenReuse-1.md](../prompts/2026-08-31-prompt-TOOL-aProvenReuse-1.md) | research | TOOL-aProvenReuse-1 |
| [2026-08-31-review-TOOL-aProvenReuse-1-diff-review-round1.md](../reviews/2026-08-31-review-TOOL-aProvenReuse-1-diff-review-round1.md) | diff-review | TOOL-aProvenReuse-1 |
| [2026-08-31-review-TOOL-aProvenReuse-1-diff-review-round2.md](../reviews/2026-08-31-review-TOOL-aProvenReuse-1-diff-review-round2.md) | diff-review | TOOL-aProvenReuse-1 TOOL-aProvenReuse-5 |
| [2026-08-31-review-TOOL-aProvenReuse-1-diff-review-round3.md](../reviews/2026-08-31-review-TOOL-aProvenReuse-1-diff-review-round3.md) | diff-review | TOOL-aProvenReuse-1 TOOL-aProvenReuse-5 |
| [2026-08-31-review-TOOL-aProvenReuse-1-spec-audit-round1.md](../reviews/2026-08-31-review-TOOL-aProvenReuse-1-spec-audit-round1.md) | spec-audit | TOOL-aProvenReuse-1 |
| [2026-08-31-review-TOOL-aProvenReuse-1-spec-audit-round2.md](../reviews/2026-08-31-review-TOOL-aProvenReuse-1-spec-audit-round2.md) | spec-audit | TOOL-aProvenReuse-1 |

<!-- /gen:spec-records -->

## 1. Goal

Give the `reuse-first` directive a LIVENESS half. `TOOL-aProvenReuse-1` makes a spec RECORD a reuse
audit; nothing there can tell a recorded audit from a typed one. This unit makes `--close` observe
that a recall probe actually ran in this run's tree, using the query log
`tools/memory-recall/query.py` already writes, and makes a waived `reuse-first` announce itself
instead of passing in silence.

## 2. Scope (IN)

- **S1** — `reuse-probed:machine` joins `DOD_CORE` in `tools/unattended/unattended.sh`.
- **S2** — a `reuse-probed)` arm in `dod_met` with exactly five outcomes, each with its own message:
  - **waived** — `reuse-first` appears in `recorded_waivers "$rel"`. MET, and `DOD_OUT` names the
    waiver and its recorded reason. This is the arm that ends the silent waiver.
  - **no log** — the log file does not exist. UNMET, and the message says the log is ABSENT rather
    than that zero probes ran. Those are different facts and an operator who confuses them looks for
    the wrong repair.
  - **zero** — the log exists and holds no `query` row for this tree. UNMET, message names the
    remedy: run the probe, or override.
  - **not adopted** — `RECALL_CLI` is blank or names nothing readable. MET, and `DOD_OUT` ANNOUNCES
    the skip. Checked BEFORE `no log`, and it exists because of round-1 finding 24: without it a CORE
    Definition-of-Done item is structurally unmeetable in every adopter that took `unattended`
    without `memory-recall`, and every `--close` there needs an override. A skip that announces
    itself is the `pieces-complete|set-checks-recorded` idiom this arm already copies.
  - **met** — one or more. MET, and `DOD_OUT` reports the COUNT, so the wrap-up carries a number
    rather than a verdict. Rev-1 said it also reported the newest row's timestamp; the code never
    emitted one, and AC4 and the self-test both assert on the count alone — three records agreeing
    and one spec sentence disagreeing, corrected here rather than built to.
- **S3** — the log is located as `$(git rev-parse --git-common-dir)/recall/queries.jsonl`, which is
  where `query.py`'s own `log_path()` puts it and where `recall-opened.js` reads it. The location is
  DERIVED by the same rule both existing readers use, never spelled as a path literal.
- **S3a** — the recall CLI is a DECLARATION, `RECALL_CLI` in `.unattended.conf`, optional and blank
  by default, added to `tools/unattended/kit.toml`'s `optional_keys`. **Rev-4 probed two hardcoded
  paths and that was wrong three ways at once**, which the closing diff review made visible. It broke
  this kit's own stated rule — the dossier says the lander, the bypass flag, the gate command and the
  scheduler tool names all live in `.unattended.conf` and *"a phase token or a DoD item spelled into
  a script is a defect"*; a sibling kit's path is the same kind of fact. It raised the carried-prefix
  ratchet in `tools/check-install-prefix.sh`, whose whole point is that a literal `tools/<kit>/`
  arrives verbatim in an adopter installed at another prefix and resolves to nothing there. And it
  could not be exercised by the self-test at all, because the suite runs the driver from outside the
  scratch tree, so the probe always found the real repo's kit and the outcome was unreachable.
- **S4** — a row belongs to this run when its `worktree` value EQUALS this run's tree. Three
  properties, and each was a round-1 blocker:
  - **The log is JSONL, so the separator is DOUBLE.** Measured on this node, the raw line reads
    `"worktree": "C:\\projects\\coding-governance\\.claude\\worktrees\\<name>"` — two
    backslash BYTES per separator, because Python's `json.dumps` escapes each one. An earlier
    revision said the value "carries `\`" and folded single backslashes; that yields
    `C://projects//coding-governance//...`, which matches no shell-derived root. Verified: the
    naive fold returns `0` on a worktree holding three real query rows, so the item would have
    reported `zero` — UNMET, "go run a probe" — for every conforming Windows run. That is exactly
    the false verdict §4 says the item exists to prevent.
  - **The fold is fold-then-squeeze.** `tr '\134' '/'` turns every backslash byte into a slash and
    `tr -s '/'` collapses the resulting doubles. Octal `\134` rather than a quoted backslash: the
    literal spelling makes GNU tr warn `an unescaped backslash at end of string is not portable`,
    and a gate that prints a warning on every green run trains its reader to ignore it.
  - **THIS RUN'S TREE IS `git rev-parse --show-toplevel`, and the choice is load-bearing.** Round 2
    blocker F4 reproduced it: S4's own pipeline returns `3` against `--show-toplevel`
    (`C:/projects/...`) and `0` against `pwd`, which under Git-Bash gives the MSYS spelling
    `/c/projects/...`. `query.py` logs `str(repo)`, a Windows path, so only the git-derived operand
    can ever match. Naming the fold rule while leaving the other operand unstated is half a
    comparison, and the unstated half is where the false verdict lives.
  - **The compare is EXACT, on the extracted value.** Every worktree here lives under
    `C:/projects/coding-governance/.claude/worktrees/`, so the PRIMARY tree's own logged value is a
    strict PREFIX of all 100-odd linked-worktree rows. A substring test reports MET off another
    tree's probes and prints an inflated count. The value is extracted with
    `grep -o '"worktree": "[^"]*"'`, stripped of its field prefix and closing quote, normalized, and
    compared with `grep -xF`. This is `memory/gotchas/id-matched-as-a-substring.md` on paths.
  - The row filter is the literal `"type": "query"` **with the space**, which is what `json.dumps`
    writes; `recall-opened.js` writes `"type":"opened"` with none, so the two spellings do not
    collide and the filter cannot pick up an `opened` row.
- **S5** — `CORE_FLOOR` moves `12:10` to `12:11` in `.unattended.conf` and in
  `tools/unattended/.unattended.conf.example`.
- **S6** — the SILENT-WAIVER sentence is retired from `tools/unattended/SKILL.template.md` and its
  render `.claude/skills/unattended/SKILL.md`, at BOTH occurrences in each — line 113 ("Waiving it
  is SILENT: the bar stays green…") and line 157 ("`reuse-first` is silent and is recommended
  against"). Measured at fold time: `grep -c reuse-first` returns 0 for
  `tools/unattended/PROTOCOL.template.md` and 0 for `memory/guides/UNATTENDED-PROTOCOL.md`, so
  round-1's "two templates and two renders" model was wrong in both directions and is corrected
  here. The PROTOCOL carriers lose nothing; they GAIN S6a's row.
- **S6b** — the sentences the S6 edit INVALIDATES but does not contain, which round 2's F15 found
  still standing. `SKILL.template.md:114-115` continues *"A waived run's spec §10 must NAME the
  waiver, or the skip leaves no trace at all"*: the first clause survives and becomes TRUE under
  `TOOL-aProvenReuse-1`, and the trailing clause is falsified by this unit's own `waived` outcome,
  where `DOD_OUT` names the waiver and its reason. It is replaced by what the `reuse-probed` line
  now reports. The count phrases in the same paragraphs — *"Two rows carry a consequence"* and the
  per-handle gloss at `:157` — move with it. An edit that retires a sentence and leaves its
  neighbouring clause asserting the retired fact is this repo's
  `amendment-leaves-its-other-half-standing` class.
- **S6a** — `tools/unattended/PROTOCOL.template.md` gains a `reuse-probed` row in its
  Definition-of-Done table, and the count sentence above it moves `Ten kit-owned core items.` to
  `Eleven`. Both are obligations of S1, not optional polish: `check-unattended.sh` check 16 arm E
  joins `DOD_CORE` to that table in BOTH directions and separately word-compares the count sentence
  against the driver's set, and that leg is the unguarded `unattended kit gate`. Omitted, S1 reds the
  merge bar twice. The render `memory/guides/UNATTENDED-PROTOCOL.md` is refreshed with it.
  **And §8's key table gains a `RECALL_CLI` row**, which S3a's declaration makes mandatory: check
  22 joins that table to the declared conf in BOTH directions, so a key this project sets and the
  contract never documents reds the same unguarded leg.
- **S7** — self-test arms in `tools/unattended/unattended.test.sh` for all FIVE S2 outcomes, each
  reachable because S3a made the CLI a declaration the fixture conf can set to a scratch path rather
  than a probe of the real tree. The
  `met` arm's fixture row REPRODUCES A REAL ROW'S ESCAPING — doubled backslashes, `"type": "query"`
  with the space, the same field order — with the `worktree` value set to the scratch tree's OWN
  path escaped the same way, and asserts the arm reports MET with a count of 1. Round 2's F9 caught
  the rev-2 wording, which demanded a literal byte copy of a live row: the suite builds a `mktemp -d`
  scratch repo, so a copied row names a worktree the fixture is not, and under S4's exact compare it
  could only ever produce the `zero` outcome. What must be copied is the ESCAPING, which is where the
  bug was; a fixture authored from the same wrong rule as the code agrees with it and certifies it.
  One further arm carries two rows whose paths are prefix-related and asserts the nested one is not
  counted for the parent.
- **S8** — the kickoff manifest's `last-audit` re-stamp. `memory/guides/SESSION-KICKOFF.md` watches
  `.unattended.conf`, which S5 edits, and `kickoff-manifest ratchet` is the first leg in
  `tools/gate-legs.json`.
- **S9** — the memory-recall coupling is DECLARED as `RECALL_CLI` (S3a) and documented beside it in
  `tools/unattended/.unattended.conf.example`, next to the `CORE_FLOOR` key S5 moves. It is still
  not a `requires` or a `requires_if` in `tools/unattended/kit.toml`: `govkit.py:1114-1129` resolves
  a `requires_if` condition against a config KEY, and while `RECALL_CLI` is now such a key, making
  the edge conditional on it would say "this kit needs memory-recall whenever the project says it
  does", which is a tautology rather than a dependency. **Rev-3 said `tools/unattended/README.md`;
  that file does not exist** — this kit has no README, and its adopter-facing prose is the conf
  example plus the rendered protocol. Round 2's F6 asked which field, and the answer is
  none: `govkit.py:1114-1129` check 7 validates a `requires_if` edge by resolving every
  `when_any_key_set` member against the kit's own declared config key lists, and `.unattended.conf`
  declares no key that says whether memory-recall is installed. A hard `requires` is refused by N6.
  So the edge is real, soft and unconditional, which is a shape the descriptor schema has no
  evaluator for, and inventing a condition key to satisfy a gate would be a declaration written for
  the checker rather than for the adopter. It goes where an adopter reads it, beside S5's
  `CORE_FLOOR` step, and this bullet records WHY rather than leaving a later reader to re-derive it.

## 3. Non-goals (OUT)

- **N1** — a merge-bar leg. The log lives in the git common dir and is neither tracked nor pushed,
  so `tools/unattended/check-unattended.sh` could only ever report DEAD PROBE on it in a fresh
  clone. A check that cannot run where the bar runs does not belong on the bar.
- **N2** — joining the logged terms to the terms a spec records. The log carries `terms` and a spec
  now carries them too, so the join is buildable, but it needs an overlap threshold and this build
  has no measurement to set one from. A threshold copied from nowhere is the
  `pin-copied-from-another-corpus` class.
- **N3** — a time window. The prompt path runs its probes BEFORE the build folder exists, so a
  window anchored on the pinned BASE would systematically miss the orientation probes this whole
  build is about. §4 states the cost of using the tree instead.
- **N4** — observing `tools/codebase-map/reuse_lookup.py`. It writes no log. See the build README's
  third build-level rule.
- **N5** — making the item unoverridable. `authorization-reachable` and `pieces-complete` are the
  two items with no override and both are about authorization; this one is about diligence, and a
  run resumed on a node whose log does not carry the probe has a legitimate reason to override.
- **N6** — making `memory-recall` a HARD `requires` of the unattended kit. S9 documents the edge and
  S2's `not adopted` outcome keeps the item meetable without it; forcing every adopter to take a
  second kit to close a run is a wider change than this unit's goal, and M3 veto 2 puts a new
  install requirement outside a delegated resolver's authority.

## 4. Design

### Inventory

| Path | Change |
|---|---|
| `tools/unattended/unattended.sh` | S1 `DOD_CORE`; S2–S4 the `dod_met` arm |
| `.unattended.conf`, `tools/unattended/.unattended.conf.example` | S5 `CORE_FLOOR` |
| `tools/unattended/SKILL.template.md` | S6 — the silent-waiver sentence, BOTH occurrences |
| `tools/unattended/PROTOCOL.template.md` | S6a — the DoD table row and the count sentence |
| `.claude/skills/unattended/SKILL.md`, `memory/guides/UNATTENDED-PROTOCOL.md` | S6/S6a RENDERS |
| `tools/unattended/kit.toml` | S9 — the memory-recall edge |
| `tools/unattended/unattended.test.sh` | S7 — five outcome arms plus the prefix arm |
| `memory/guides/SESSION-KICKOFF.md` | S8 — the `last-audit` re-stamp |

### What this item claims, and what it does not

Stated here rather than left to a reader, because §7 of the charter requires a check to declare its
own blind spots. The item observes that **a recall probe ran in this worktree**. It does not observe
that the probe was run FOR this build, that its question was relevant, or that its answer was read.
A worktree reused across two builds carries the earlier build's rows and would satisfy the later
one. That limit is accepted because the alternative — a time window — has a worse failure, N3's, and
because the item's job is to make zero distinguishable from unmeasured, which it does.

It also does not observe anything at all in a project that declares no `RECALL_CLI`. There the
`not adopted` outcome fires and says so, which is a SKIP and is reported as one. A skip that looks
like a pass is indistinguishable from coverage, so the message names the KEY rather than the missing
log, and the two messages are deliberately unconfusable.

### Alternatives rejected

- **A `DOD_EXTRA` declaration instead of a core item.** Rejected on inspection of source: `dod_met`
  routes every item it does not know to a `*)` arm that greps the run-state file for an
  attestation. A project-declared item is therefore attestation-only by construction, and an
  attestation is precisely what this unit exists to replace.
- **Enforcement at `--preflight`.** Rejected: on the slug path the probes legitimately run after
  preflight, so the check would refuse every correct run.
- **A new verb, `--record-probe`.** Rejected: it would ask the agent to attest what a log already
  records, which is the weaker of two available evidences and one more thing to forget.
- **A hard `requires = ["memory-recall"]` on the kit.** Rejected at round 1 (finding 24) — see N6.
- **Folding single backslashes, and matching the worktree as a substring.** Both were in rev-1 and
  both were round-1 blockers, measured against the live log. They are recorded here rather than
  quietly corrected because a later reader will reach for exactly these two shapes.
- **Reading the log through `query.py`.** Rejected: the driver is POSIX shell with no Python
  dependency in this path, and the read is one `grep` over a line-oriented file. Adding a Python
  hop to parse JSON the shell can substring-match would make the driver depend on the memory-recall
  kit being installed, which no adopter is required to do.

### Migration

**Two migrations, and both are owed.** At the RUN level: none — a run whose log carries no rows meets
the `zero` outcome and can override with a reason, the documented path for every other unmet item.
At the ADOPTER level, S5 raises the DoD half of `CORE_FLOOR` from 10 to 11, and that floor is
REQUIRED from the project's own `.unattended.conf` rather than defaulted — `check-unattended.sh:387`
refuses an undeclared one outright and `:430` reds when the declared floor sits below the kit's core
count. So taking this kit version obliges an adopter to edit their own conf, and the step goes in
`tools/unattended/.unattended.conf.example` beside the key itself, where they will read it. Round 2's F13 found this
section reading `None` while S5 moved the floor.

### Rollout

Its OWN commit, after `TOOL-aProvenReuse-1`'s, which is what the `order 1` / `order 2` headers
already say. The shared-commit option an earlier revision offered is withdrawn: M6 requires a commit
per pass with the unit id in the subject, and two mechanisms in one commit make the M6 bug-class
checklist over `HEAD~1..HEAD` cover both at once and leave the closing review unable to attribute a
finding. The item is inert for any run that has run a probe, which every conforming run has.

## 5. Production-readiness checklist

- **Security** — the driver reads one more file inside the git common dir, a directory it already
  writes to. No new input from outside the repo, no new write.
- **Performance** — one filtered pass over a file whose growth is one line per query. Measured on
  this node at fold time: **358 453 bytes over 174 rows**, an order of magnitude above the "tens of
  KB" an earlier revision guessed. `memory/builds/aQuarriedLantern/spec/2026-08-03-spec-aQuarriedLantern-1.md`
  already recorded the shape at 2 414 771 bytes over 676 rows. "Bounded by nothing" is acceptable
  rather than unexamined: `memory/builds/aDrainedSluice/spec/units/2026-08-08-spec-aDrainedSluice-7-v6-recall-cache-cap.md`
  considered capping `queries.jsonl` and declined it, and that decision stands.
- **Error states** — the five S2 outcomes are exhaustive: the waiver short-circuit, then the absent
  kit, then "file absent / no match / match" over the log.
- **Observability** — `DOD_OUT` carries a distinct sentence per outcome, and `--close` already
  prints it. The count reaches the wrap-up through the same channel every other item uses.
- **Testing** — S7.
- **Migration/rollback** — revert; `CORE_FLOOR` returns to `12:10`.

## 6. Acceptance criteria

- **AC1** — with `reuse-first` recorded as waived, `bash tools/unattended/unattended.sh --close`
  reports `reuse-probed` MET and the message names the handle and its recorded reason. Observed
  against a fixture run-state file carrying a `waiver · item reuse-first` row.
- **AC2** — with no log file present, `--close` reports `reuse-probed` UNMET and the message
  contains the word `absent`, textually distinct from AC3's and AC3a's messages.
- **AC3** — with a log present holding no `query` row for this tree, `--close` reports UNMET and
  names the remedy.
- **AC3a** — with `RECALL_CLI` blank, `--close` reports MET and the message names the key. With it
  set to a path that does not resolve, the SAME outcome and the message names the value — a typo'd
  path must not fall through to the log arms and report a missing PROBE when the fault is a missing
  FILE. This is the observable for S2's `not adopted` outcome, and without it nothing distinguishes
  "the skip works" from "the skip was never exercised".
- **AC4** — with a log holding at least one `query` row for this tree, `--close` reports MET and the
  message carries the row count. **The fixture row is a byte copy of a real `query` row**, doubled
  backslashes included, not one hand-authored from this spec. Measured now, this tree's live log
  holds `3` such rows, so the arm has a real subject.
- **AC4a** — a log holding one row for `C:/projects/coding-governance` and one for
  `C:/projects/coding-governance/.claude/worktrees/<this tree>` counts exactly ONE for this tree and
  exactly one for the parent. This is S4's exact-compare property, and it fails under any substring
  test.
- **AC5** — `bash tools/unattended/unattended.sh --close <slug> --override reuse-probed --reason "…"`
  records the override as a parked entry, proving N5. Negative control: `--override
  authorization-reachable` is still refused, so this unit did not widen the no-override set.
- **AC6** — `bash tools/unattended/check-unattended.sh` exits 0 with `CORE_FLOOR` at `12:11`, and
  reds with it left at `12:10`. The second half is the liveness assertion for the first.
- **AC6a** — the same command reds when S6a is omitted, on BOTH of check 16 arm E's joins
  independently: once for a `DOD_CORE` item absent from the protocol's Definition-of-Done table, and
  once for the count sentence still reading `Ten`. Two failures, two observations — a single check
  run that goes green after fixing one of them would hide the other.
- **AC7** — `bash tools/unattended/unattended.test.sh` passes with S7's arms present, and
  `bash tools/unattended/run-unattended-gates.sh` exits 0. This IS kit work, so the self-tests the
  2026-08-23 ruling took off the bar are owed here by the Definition of Done.
- **AC8** — `bash tools/check-kit-versions.sh` exits 0 after the version move, and BOTH retired
  phrases are gone from BOTH carriers. Measured at fold time so the criterion has a before as well
  as an after: `grep -c` for the case-sensitive phrase `Waiving it is SILENT` returns **1** in each
  of `tools/unattended/SKILL.template.md` and `.claude/skills/unattended/SKILL.md` and must return
  **0**; `grep -ci` for `is silent and is recommended against` likewise returns **1** in each and
  must return **0**. Two phrases, two greps, because they differ in CASE and a single
  case-sensitive pattern for `is SILENT` never sees the second — round 2's F5, independent of F3.
  The greps name the two files rather than a directory: `grep -rn "is SILENT" tools/unattended/`
  returns **7** hits at HEAD, five of them unrelated source comments S6 does not touch, so a
  directory-scoped emptiness assertion cannot pass even after a correct S6 — round 2's blocker F3.
  `memory/builds/` is excluded for the same reason it always was: this build's README quotes the
  retired sentence as its problem statement.
- **AC9** — `bash skills/session-kickoff/manifest-check.sh` exits 0 after S8's re-stamp.

## 7. Gates

`bash tools/run-gates/run-gates.sh` for the bar. Three legs are named because this unit reaches
each: `kickoff-manifest ratchet` (S8), `unattended kit gate` (unguarded, and the leg S6a exists to
satisfy) and `unattended skill wiring` (S6's renders).
`bash tools/unattended/run-unattended-gates.sh` for the kit self-tests, which the owner's 2026-08-23
ruling took off the bar and which AC7 owes because this IS kit work.
`bash tools/check-kit-versions.sh` for AC8, `bash skills/session-kickoff/manifest-check.sh` for AC9.
What no gate here checks, and all three are §4's stated limits rather than oversights: that the log
this item reads is the log the agent's probe wrote; that the probe was run FOR this build rather
than earlier in the same worktree; and anything at all in a project that declares no `RECALL_CLI`,
where the item reports a SKIP and says so.

## 8. Open questions

- **Q1 — should a missing log be UNMET or a MET-with-notice?** **RESOLVED (agent, 2026-08-31,
  delegated):** UNMET. A missing log is exactly the state where the item cannot answer its question,
  and the charter's rule is that a probe which cannot move says so rather than reporting a
  reassuring zero. Reporting MET would be a green verdict earned by the check being broken.
- **Q2 — is the worktree match the right join, given §4's stated limit?** **RESOLVED (agent,
  2026-08-31, delegated):** yes, by M3's rule. The two surviving options were a worktree match and a
  BASE-anchored time window; the window fails an acceptance criterion this build's own goal states,
  because it cannot see the prompt path's orientation probes. Fewest follow-ups left open decides it,
  and the limit is written into §4 rather than left for a reader to discover.

## 9. Revision log

- rev-1 · 2026-08-31 · authored by the aProvenReuse run.
- rev-7 · 2026-08-31 · closing-diff-review round-3 fold. S2's `met` outcome claimed `DOD_OUT` reports
  the newest row's timestamp; the code never emitted one and AC4 and the self-test both assert the
  count alone, so the spec sentence was the odd record out and is corrected rather than built to.
  N6 still named the retired `kit absent` outcome after S2 renamed it to `not adopted`.
- rev-6 · 2026-08-31 · closing-diff-review round-2 fold. Round 2 found rev-5 had changed S2, S3a
  and S9 to the `RECALL_CLI` declaration and left AC3a, §4 and §7 still describing the hardcoded
  two-path probe it replaced — the `amendment-leaves-its-other-half-standing` class, with AC3a false
  against both the code and its own self-test. All three now describe what shipped. S6a also gained
  the protocol's own `RECALL_CLI` row, without which `check-unattended.sh` check 22 reds on a key
  the conf declares and the contract never documents.
- rev-5 · 2026-08-31 · closing-diff-review fold, blockers F1 and F2. The recall CLI became the
  `RECALL_CLI` declaration (S3a) instead of two hardcoded paths, which is what this kit's own
  declarations-not-constants rule always required; the hardcoded form also raised the carried-prefix
  ratchet and left the not-adopted outcome unreachable by the suite. S9 re-stated on top of it.
- rev-4 · 2026-08-31 · build-time correction. S9 and §4 Migration named `tools/unattended/README.md`
  as the adopter-facing carrier; that file does not exist in this kit, so both now name
  `tools/unattended/.unattended.conf.example`, beside the `CORE_FLOOR` key the same change moves.
  M2 requires the spec to change before the code diverges from it, so this rev precedes the edit.
- rev-3 · 2026-08-31 · round-2 spec-audit fold, at the loop's NON-CONVERGENT exit. Blocker F4 named
  the comparison's OTHER operand, `git rev-parse --show-toplevel`: reproduced, S4's pipeline returns
  3 against it and 0 against `pwd`. Blocker F3 and F5 rewrote AC8, whose directory-scoped grep
  returns 7 hits at HEAD and whose single case-sensitive pattern could not see the second retired
  phrase. F6 settled S9 — the coupling is documented rather than declared, because check 7's
  `requires_if` needs a condition key `.unattended.conf` does not have. F9 replaced AC4's
  byte-copy fixture rule, which cannot match inside the suite's `mktemp` scratch repo, with an
  escaping-reproduction rule. F15 added S6b for the clauses the S6 edit invalidates without
  containing. F13 gave §4 the adopter migration S5 created. F14 moved this header OPEN -> SPECCED.
- rev-2 · 2026-08-31 · round-1 spec-audit fold. Blockers 13, 22 and 34 rewrote S4: the log is
  JSON-escaped, so the separator is two backslash bytes and the rev-1 fold produced
  `C://projects//…` and matched nothing — the item would have reported UNMET on every conforming
  Windows run. Blocker 12 added S6a, the protocol DoD table row and the `Ten` -> `Eleven` count
  sentence that check 16 arm E joins in both directions. Finding 24 added S2's `kit absent` outcome,
  S9 and N6 — a CORE item reading another kit's file was structurally unmeetable for an adopter
  without it. Finding 35 made the worktree compare EXACT rather than a substring, because the
  primary tree's path is a prefix of every linked worktree's. Findings 4 and 27 corrected S6's
  carrier set, measured: the sentence is in the SKILL template and its render TWICE each and in
  neither PROTOCOL carrier. Finding 23 added S8. Finding 40 replaced a log-size figure that was an
  order of magnitude low. Finding 20 withdrew the shared-commit rollout option. AC3a, AC4a and AC6a
  are new observables the fold created.

## 10. Reuse audit

Three seams, all extended in place, none created. `tools/memory-recall/query.py`'s `log_path()`
already writes `<git-common-dir>/recall/queries.jsonl` with a `type: "query"` row carrying `terms`,
`query`, `at` and `worktree`; `tools/memory-recall/recall-opened.js` already reads that file and
already derives the common git dir the way S3 does; and `dod_met` in
`tools/unattended/unattended.sh` already dispatches per item with a demonstrated skip-announcing
idiom at its `pieces-complete|set-checks-recorded` arm, which S2's waived outcome copies rather than
reinvents.

`python tools/codebase-map/reuse_lookup.py "checking that a spec records a reuse audit before code
is written"` returned the `.unattended.conf` affordance seam and `check_audit` in
`tools/memory-recall/check-recall.py`. The latter was inspected and REJECTED: it grades a retrieval
FIXTURE against a pinned precision floor and holds no reader of the query log at all.

Recall terms used: `reuse-first reuse audit spec section 10 seam recall probe terms directive waiver
silent unchecked machine-checked prose`. The same query as this build's other unit, per M5's rule
that the obligation is satisfied once for the SET.

Where a hit was STALE: the recall probe did not surface any reader of the query log, and
`recall-opened.js` was found by grep over `.claude/settings.json` after the SessionStart hook
reported the wiring. That is recorded because it is the probe-failure taxonomy in action — the log
reader exists and the corpus has no decision record naming it, so recall could not have found it.
