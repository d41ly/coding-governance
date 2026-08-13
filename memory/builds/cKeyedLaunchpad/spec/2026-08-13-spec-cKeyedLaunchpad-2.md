# KICK-cKeyedLaunchpad-2 — one location list, and the three kits the move drags in

**Status:** OPEN · rev-2 · 2026-08-13 · node c · Tier-2 · base f006691f · streams kickoff+tooling

## 1. Goal

Give the kickoff manifest one authoritative list of where it may live, and move this repo's manifest
to the home the memory tree governs. Today the order is spelled in five files that do not agree, and
this repo's own manifest sits at the third entry of a list whose first two locations do not exist
here.

## 2. Scope (IN)

- S1. A read-only `--locations` verb in `manifest-check.sh` printing one repo-relative path per line
  and exiting 0, with its own arm in the argument `case` and placed BEFORE the repo probe.
- S2. The discovery loop and the not-found error string are BUILT from the same array the verb
  prints, collapsing the script's three internal spellings to one.
- S3. The order becomes `memory/guides/SESSION-KICKOFF.md` then `.claude/SESSION-KICKOFF.md`. The
  `docs/claude/`, `docs/` and repo-root spellings are dropped.
- S4. `SKILL.md` Step 2 and `WIRE-INTO-PROJECT.md` §4 stop restating the list and invoke the verb.
- S5. `SKILL.md` gains location 3, the skill's own base directory, as an engine-owned machine-global
  fallback with an explicit Step 2b skip and a READY-card line naming it as unaudited.
- S6. `git mv .claude/SESSION-KICKOFF.md memory/guides/SESSION-KICKOFF.md`, with the `last-audit`
  re-stamp in the same commit.
- S7. Every other site that spells the old path moves with it: `AGENTS.md:54`,
  `tools/memory-tree/README.md:166`, `tools/memory-tree/BUILD-METHOD.template.md:42` plus its
  re-render, and the four extra `docs/SESSION-KICKOFF.md` sites in `WIRE`.
- S8. `memory/project/method-carriers.txt` row 5 is DELETED, not repointed.
- S9. `tools/drift-audit/drift_signals.py` gains `memory/guides/SESSION-KICKOFF.md` to
  `PRODUCT_GLOBS` — the FILE path, never a directory.
- S10. A new codebase-map dossier at `memory/map/features/kickoff.md` claiming
  `guides = ["SESSION-KICKOFF.md"]`, plus a regeneration of `memory/map/generated/`.
- S11. `READ_PATH_CEILING` is raised in `.memory-tree.conf` with the reason in the commit message.
- S12. The self-test is retargeted: `write_manifest` writes to the new primary location, and the one
  scenario that depends on a dropped spelling is rewritten.

## 3. Non-goals (OUT)

- **The `governance-template:` marker fallback is kept, not dropped.** `SKILL.md:74-77` and
  `WIRE:331-332` both promise it and `manifest-check.sh` implements none of it. Dropping it while
  pointing the docs at `--locations` would silently change behaviour for an adopter who has an
  instantiated playbook and no manifest. It stays, relabelled as ENGINE-ONLY, which is a different
  question from "where may a manifest file live" and so is not a second answer to the same one.
- **No gate over `AGENTS.md`.** The charter can name a file that does not exist and the whole bar
  stays green, because check 15's population is `memory/` only and the install-prefix gate's
  population does not reach the charter. That gap is real and is parked in the build README as a
  follow-up; closing it is a different unit.
- **No retrofit of adopters.** NicoCares keeps `.claude/`, which survives as location 2.
- **`READ_PATH_CEILING` is not left raised.** U6's S8 lowers it once the traps are evicted, with its
  own Files-touched row and criterion. This unit owns the raise; the obligation is ACCEPTED there, not
  merely named here. The M4 audit found rev-1 named a sibling that had not taken the work, and nothing
  on the bar would ever have noticed — the ceiling only fails when exceeded, so one left high is green
  forever.
- No change to C1-C6, and no manifest-format version bump. U3 owns that.

## 4. Design

### Why the verb can only cover two of the three locations

`manifest-check.sh` decides repo membership by git identity, not path strings, and refuses an
out-of-repo path with exit 2 by design. The skill's base directory is outside every repository. So
the script cannot check, or even meaningfully list, location 3. Splitting ownership is therefore not
a compromise but the only correct shape: the SCRIPT owns the two gatable in-repo locations and is the
single source for them, and the ENGINE owns location 3 plus its consequences. `SKILL.md` states
location 3 once, as engine behaviour, and does not restate locations 1 and 2.

This is what the owner's decision costs, and the spec says it plainly: a manifest at location 3 is
read but never audited. Step 2b skips it and the READY card says so, so a stale machine-global
manifest is visible every kickoff rather than silently authoritative.

### Placement, and two ways the verb fails quietly

The argument parser's catch-all is `*) MF="$a" ;;`, so a `--locations` flag without its own case arm
is reinterpreted as a manifest path and dies at exit 2. And the repo probe at line 21 runs before any
argument handling, so a verb placed after it is unusable from outside a repo — measured, the script
exits 2 before reading `argv` at all, with or without an argument. The verb therefore needs both its
own arm AND a position ahead of line 21.

A print-only verb also keeps the harness meta-gate untouched. `check-arms.py` counts `fail <n> "…"`
call sites, the script has exactly 16, and `ARMS_FLOORS` pins it at `16:16` with zero slack. Adding
any `fail` branch would force both a floor raise and a matching positive assertion. Printing and
exiting 0 adds neither.

### The read-path budget, and why it forces a temporary raise

Hygiene check 16 bounds the bytes a session reads through the charter's read path. It stands at 5
files / 53,775 B against a ceiling of 71,891 B, leaving 18,116 B. The manifest is 21,170 B. Rewriting
`AGENTS.md:54` to a `memory/`-prefixed path therefore pulls the manifest onto the read path and
exceeds the ceiling by 3,054 B.

Three options were considered and two rejected. Naming the manifest in `AGENTS.md` without a
resolvable token defeats the check rather than satisfying it. Deferring the `AGENTS.md` edit to U6
leaves the charter pointing at a deleted path for the whole interval, and §3 records that nothing
would catch it. So this unit raises the ceiling with the reason written down, and U6 lowers it after
evicting roughly 14,665 B of traps. Both movements are explicit and both are in a commit that says
why, which is the convention `.memory-tree.conf`'s other cutoffs already follow.

### What the move drags in

| Kit | What must change | Why it reds otherwise |
|---|---|---|
| memory-tree | `BUILD-METHOD.template.md:42` and its re-render | The path becomes a dead citation in check 15's corpus, and `DEAD_PATH_PIN` is 0 — no room to register it |
| memory-tree | `method-carriers.txt` row 5 deleted | Check 4 fails loudly on a declared carrier that no longer exists |
| codebase-map | a `kickoff` dossier + regenerated artifacts | A new `memory/guides/*.md` reds the coverage gate, and `baseline.toml` is closed to new keys |
| drift-audit | the `PRODUCT_GLOBS` file entry | Without it the manifest silently leaves the product surface |

The `BUILD-METHOD` pair must move in ONE commit and in one direction. Parity renders TEMPLATE to
LIVE, so editing only the live copy is reverted by the next render, and editing only the template
reds the check arm.

### Why row 5 is deleted rather than repointed

`check-method-carriers.sh` excludes the whole memory tree from its population. A row naming a path
inside `memory/` would satisfy check 4's two arms — the file exists and it does point at the method —
while checks 3 and 5 can never see it again. That is a vacuous row: an assertion that cannot fail,
which this repo bans by name. The registry declares files OUTSIDE `memory/` that point at the method,
and after the move the manifest is not one. Deleting the row makes the population accurate. The
coverage loss is real, is a direct cost of the owner's chosen home, and is named here rather than
papered over with a row that always passes.

### The five surviving `docs/` sites, named

S7 puts them in scope and rev-1 gave no criterion that reaches them. They are
`WIRE-INTO-PROJECT.md:336` (a `cp` step that installs the manifest into `docs/`), `:372`, `:498`,
`:521`, and `SKILL.md:224` — the Scaffolding write target, which spec-7's §3 explicitly disclaims, so
it is this unit's.

The `cp` step and the Scaffolding target are the two that matter most: they do not merely describe the
old layout, they instruct an adopter to CREATE a manifest at a location the same commit makes the
engine stop looking for. Scaffolding is repointed to location 1.

### Files touched (estimate)

Fourteen files across three kits plus the charter. The move itself is one `git mv`; the rest is the
tail it drags.

### Alternatives rejected

- **A shared conf key instead of a verb.** A `.conf` both the script and the engine read would make
  the engine parse shell, and the engine already invokes the script.
- **Repointing method-carriers row 5.** Vacuous, per above.
- **Broadening `PRODUCT_GLOBS` to `memory` or `memory/guides`.** The header warns exactly against it:
  an id catalogue inside the corpus certifies every spec at once. The entry is the file path.
- **Keeping the root and `docs/` spellings for compatibility.** They are the reason the list is
  unreadable, neither live install uses them, and S12 already pays the test cost of dropping them.

## 5. Production-readiness checklist

- security — the new verb reads nothing and writes nothing; it prints a constant array.
- perf / scale — one fewer stat per discovery, two locations instead of four.
- a11y — N/A, terminal output.
- i18n — N/A.
- error / empty / loading states — the not-found error string is generated from the same array, so it
  can never again disagree with the loop it describes.
- observability — the READY card gains the unaudited-fallback line for location 3.
- risks — the parity leg's guard does not cover `memory/guides/BUILD-METHOD.md`, so a diff-scoped run
  touching only the live half SKIPS the leg and only `GATE_FULL=1` catches it. This unit must not
  trust a scoped green.
- testing + left-shift gates — S12 plus arms for the verb; the dropped spellings are what 34 of the
  41 existing scenarios silently depend on.
- migration / rollback — adopters at `.claude/` are unaffected. Adopters at a dropped spelling get the
  exit-2 not-found message, NOT the version WARN: discovery runs before the version check and exits
  there, and the WARN fires only on a marker-version delta this unit does not create. Their pathless
  pre-commit and CI invocations hard-error on the kit re-pull. The migration is one `git mv` to
  location 1 or 2, and the not-found message names both, which AC4 requires. An upgrade note goes in
  the runbook's §4 beside the retrofit recipe.
- user docs — S4 and S7.

## 6. Acceptance criteria

- AC1. When `bash skills/session-kickoff/manifest-check.sh --locations` runs, it prints exactly
  `memory/guides/SESSION-KICKOFF.md` and `.claude/SESSION-KICKOFF.md`, one per line, and exits 0.
- AC2. When the same command runs with a working directory outside any git repository, it still
  prints the list and exits 0, rather than the repo-probe error.
- AC3. When a manifest exists only at `memory/guides/SESSION-KICKOFF.md`, a bare
  `bash skills/session-kickoff/manifest-check.sh` discovers and checks it.
- AC4. When a manifest exists only at a dropped spelling such as the repo root, the command exits 2
  with a not-found message naming the two supported locations and no others.
- AC5. `grep -c 'SESSION-KICKOFF.md' skills/session-kickoff/manifest-check.sh` shows the path list
  spelled once, not once per consumer.
- AC6. `git grep -l '\.claude/SESSION-KICKOFF\.md'` returns nothing outside build records, the
  engine's own location array, its self-test, and the migration note. The exemption is not a
  weakening: S3 KEEPS that path as location 2, so the array must spell it and AC1 requires the verb to
  print it. An unexempted AC6 contradicts AC1, and a builder driving it green would delete the only
  location every existing adopter uses.
- AC6b. `git grep -n 'docs/SESSION-KICKOFF\.md'` returns nothing outside build records and the
  migration note. This is the criterion that reaches the dropped spellings; AC5 and AC6 both miss
  them by construction, and they are what F2 and F6 are about.
- AC7. `bash tools/memory-tree/check-method-carriers.sh` exits 0 with a carrier count one lower.
- AC8. `python tools/codebase-map/test_codebase_map.py` exits 0, with the new guide claimed by the
  `kickoff` dossier and the generated artifacts byte-identical to a fresh render.
- AC9. `python tools/drift-audit/drift_report.py --check` exits 0 and the
  `non_terminal_specs_cited_by_product_source` value is unchanged at its pin.
- AC10. `GATE_FULL=1 bash tools/run-gates.sh` is green, including the parity leg the scoped run skips.
- AC11. `bash skills/session-kickoff/manifest-check.test.sh` passes with `write_manifest` targeting
  the new primary location.
- AC12. The engine's READY card, run in a repo whose only manifest is at the skill base directory,
  carries a line stating the manifest is machine-global and unaudited.

## 7. Gates

- `bash skills/session-kickoff/manifest-check.sh` and its self-test — both change.
- `bash tools/memory-tree/check-memory-hygiene.sh` — checks 15 and 16 both move.
- `bash tools/memory-tree/check-method-carriers.sh` · `bash tools/memory-tree/kit-dogfood-parity.test.sh`
- `python tools/codebase-map/test_codebase_map.py` · `python tools/drift-audit/drift_report.py --check`
- `GATE_FULL=1 bash tools/run-gates.sh` — required, not optional, per §5's guard-gap risk.

## 8. Open questions

none — the forks below were RESOLVED by the owner at kickoff, before authoring, and are recorded in
the build README.

- Primary manifest home. RESOLVED (owner, 2026-08-13): `memory/guides/SESSION-KICKOFF.md`.
- Whether the manifest keeps its drift-audit product surface. RESOLVED (owner, 2026-08-13): yes, via
  an explicit file path in `PRODUCT_GLOBS`.
- The third location. RESOLVED (owner, 2026-08-13): the skill base directory, accepted as ungatable,
  with the engine flagging it rather than auditing it.

## 9. Revision log

- rev-1 · 2026-08-13 · initial draft, grounded by workflow `wf_0aaecb50-a51`.
- rev-2 · 2026-08-13 · folded the M4 spec audit, review record 1. H4: AC6 contradicted AC1 and S3 —
  the engine must spell location 2, so an unexempted grep for it could only be satisfied by deleting
  the location every adopter uses; AC6 is now scoped and says why. H5: the four `docs/`-spelled sites
  S7 puts in scope had no criterion reaching them — added AC6b, named all five sites in §4, and took
  `SKILL.md:224` which spec-7 disclaims, including repointing the Scaffolding write target. H6: §3
  assigned the ceiling lowering to a sibling that had not accepted it; it is accepted in that spec now
  and this bullet says so. M2: the migration row named the version WARN, which discovery runs before
  and which fires only on a delta this unit does not create — replaced with the real mechanism and an
  actual migration path.

## 10. Reuse audit

The seam is `manifest-check.sh` itself: it already owns discovery, already carries the 0/1/2 exit
contract a print-only verb slots into, and is already the script `SKILL.md` Step 2b is forbidden to
reimplement. This unit makes that existing single-source claim true for the location list too, rather
than adding a new carrier for it.

`reuse_lookup.py "the one place a list of paths is declared for several readers"` returns
`install-prefix` and `gate-legs`, both of which single-source a list from a declaration rather than a
directory listing. `tools/gate-legs.json` is the closest prior art — one manifest, many readers, and
a canary that refuses a malformed one. It is not extended here because the location list is three
entries consumed by one script and one engine, and a JSON file for that would be a carrier heavier
than the fact it carries.

Recall terms used: `kickoff manifest ratchet last-audit watch verify-paths SESSION-KICKOFF discovery
order traps accretion size gate prose`.
