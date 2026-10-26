# TOOL-dGroundRules-86 — the records and the runbook this build's code left stale: the kickoff manifest re-audited and re-stamped, dSafePassage-26's Readers clause, the TOOL-dGroundRules-34 ledger's AC32 token, two method-carrier rows and the policy kit's runbook section

**Status:** CLOSED · rev-2 · 2026-10-25 · node d · Tier-1 · base cae57b1d · streams tooling · order 33

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dGroundRules-1-runlog-28554d7f.md](../build/2026-10-25-build-TOOL-dGroundRules-1-runlog-28554d7f.md) | journal | TOOL-dGroundRules-1 TOOL-dGroundRules-2 TOOL-dGroundRules-3 TOOL-dGroundRules-4 TOOL-dGroundRules-5 TOOL-dGroundRules-6 TOOL-dGroundRules-7 TOOL-dGroundRules-8 TOOL-dGroundRules-9 TOOL-dGroundRules-10 TOOL-dGroundRules-11 TOOL-dGroundRules-14 TOOL-dGroundRules-15 TOOL-dGroundRules-16 TOOL-dGroundRules-17 TOOL-dGroundRules-18 TOOL-dGroundRules-19 TOOL-dGroundRules-20 TOOL-dGroundRules-21 TOOL-dGroundRules-22 TOOL-dGroundRules-23 TOOL-dGroundRules-24 TOOL-dGroundRules-25 TOOL-dGroundRules-26 TOOL-dGroundRules-27 TOOL-dGroundRules-28 TOOL-dGroundRules-29 TOOL-dGroundRules-30 TOOL-dGroundRules-31 TOOL-dGroundRules-32 TOOL-dGroundRules-33 TOOL-dGroundRules-34 TOOL-dGroundRules-35 TOOL-dGroundRules-36 TOOL-dGroundRules-37 TOOL-dGroundRules-38 TOOL-dGroundRules-39 TOOL-dGroundRules-40 TOOL-dGroundRules-41 TOOL-dGroundRules-42 TOOL-dGroundRules-43 TOOL-dGroundRules-44 TOOL-dGroundRules-45 TOOL-dGroundRules-46 TOOL-dGroundRules-47 TOOL-dGroundRules-48 TOOL-dGroundRules-49 TOOL-dGroundRules-50 TOOL-dGroundRules-52 TOOL-dGroundRules-55 TOOL-dGroundRules-56 TOOL-dGroundRules-60 TOOL-dGroundRules-61 TOOL-dGroundRules-62 TOOL-dGroundRules-63 TOOL-dGroundRules-64 TOOL-dGroundRules-65 TOOL-dGroundRules-66 TOOL-dGroundRules-67 TOOL-dGroundRules-68 TOOL-dGroundRules-69 TOOL-dGroundRules-70 TOOL-dGroundRules-71 TOOL-dGroundRules-72 TOOL-dGroundRules-73 TOOL-dGroundRules-74 TOOL-dGroundRules-75 TOOL-dGroundRules-76 TOOL-dGroundRules-77 TOOL-dGroundRules-78 TOOL-dGroundRules-79 TOOL-dGroundRules-80 TOOL-dGroundRules-81 TOOL-dGroundRules-82 TOOL-dGroundRules-83 TOOL-dGroundRules-84 TOOL-dGroundRules-85 TOOL-dGroundRules-87 TOOL-dGroundRules-88 |
| [2026-10-25-prompt-TOOL-dGroundRules-86-1-spec-writer.md](../prompts/2026-10-25-prompt-TOOL-dGroundRules-86-1-spec-writer.md) | journal | — |
| [2026-10-25-prompt-TOOL-dGroundRules-86-2-spec-writer.md](../prompts/2026-10-25-prompt-TOOL-dGroundRules-86-2-spec-writer.md) | journal | — |
| [2026-10-25-prompt-TOOL-dGroundRules-86-3-spec-writer.md](../prompts/2026-10-25-prompt-TOOL-dGroundRules-86-3-spec-writer.md) | journal | — |
| [2026-10-25-prompt-TOOL-dGroundRules-86-merge-brief.md](../prompts/2026-10-25-prompt-TOOL-dGroundRules-86-merge-brief.md) | research | — |
| [2026-10-25-prompt-TOOL-dGroundRules-86-rev2-brief.md](../prompts/2026-10-25-prompt-TOOL-dGroundRules-86-rev2-brief.md) | research | — |
| [2026-10-25-prompt-TOOL-dGroundRules-86-spec-brief.md](../prompts/2026-10-25-prompt-TOOL-dGroundRules-86-spec-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

The close's bar pre-check at `cae57b1d8` reds four legs that a record or a doc can fix: the
kickoff-manifest ratchet, memory hygiene (checks 25 and 23), method carriers and govkit runbook
parity. Each was green at the run's base `3c2b69be4`, and each red is this build's code moving under
a record or a doc that describes it. This unit brings each record and the runbook back to the tree.
It builds after `TOOL-dGroundRules-84` and `TOOL-dGroundRules-85`, so the manifest re-audit reads the
tree they leave; both have landed, at `5e8c8c5e7` and `2550ccaa7`. S3 edits another build's spec,
which only the spec-writer role may write, so it lands with this spec's rev-2 commit, before the
build. The builder writes S1, S2, S4, S5 and S6.

## 2. Scope (IN)

- **S1** — The body of `memory/guides/SESSION-KICKOFF.md` §B. The trap bullet at
  `memory/guides/SESSION-KICKOFF.md:172-173` takes the text §4 "The manifest" gives. A pointer
  bullet for the policy file follows the bullet at `:75`, in the text §4 gives. Every other §B claim
  is re-verified at the audit commit by the probes §4 lists. A claim found stale there is fixed in
  the same edit and named in the commit's delta line. Observed by AC1.
- **S2** — The audit block's stamps, by the stamp rule at `memory/guides/SESSION-KICKOFF.md:23`.
  `last-audit` (`:5`) becomes the audit's datetime `@` the full sha of the audit commit, and
  `last-body-change` (`:8`) becomes that same sha. The commit message carries a
  `manifest-audit: delta` line in the shape §4 gives. Observed by AC1.
- **S3** — Landed by this spec's rev-2 pass, in the spec commit. In
  `memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-26.md`, S30's Readers clause
  (`:258-262`) holds the text §4 "The Readers clause" gives. Its header (`:3`) reads rev-5 dated
  2026-10-25, its status DEFERRED kept. Its §9 holds the rev-5 line §4 gives, at `:728`, after the
  rev-4 line. The builder writes nothing for S3. Observed by AC2.
- **S4** — The AC32 answer of the `TOOL-dGroundRules-34` ledger
  (`memory/builds/dGroundRules/build/2026-10-23-build-TOOL-dGroundRules-34-ledger.md:51`) carries
  `gen:build-order` as its observation token in place of `165`. The rest of the line stays.
  Observed by AC2.
- **S5** — `memory/project/method-carriers.txt` gains two rows after its last (`:35`), one for
  `tools/policy/caps.toml` and one for `tools/policy/check_policy.py`, in the text §4 "The carrier
  rows" gives. Observed by AC3.
- **S6** — `WIRE-INTO-PROJECT.md` gains an anchored section for the registry entry `policy`, in the
  text §4 "The runbook section" gives. It sits between the 3h section's last line (`:751`) and
  `## 4` (`:753`), with one blank line on each side. Observed by AC4.

## 3. Non-goals (OUT)

- Legs 3 to 7 and 9 of the triage. `TOOL-dGroundRules-84` and `TOOL-dGroundRules-85` own them.
- Any edit to dSafePassage-26 by the builder. S3 landed with this spec's rev-2, and it touched
  S30's Readers clause, the header and §9 only. S30's body cites
  `tools/hooks/agent-cap.js:1631-1632` as the shared parser, and §8 names that as a follow-up.
- The policy kit's code, and `PROBLEM_PIN` in `tools/govkit/check_runbook_parity.py:60`. The count
  meets the pin after S6 (§6).
- Hygiene check 9. It reds on the staged rescope's build README, which the committing loop renders
  with `gen_build_index.py --write`.
- A deviation record for S3. §4 "Evidence" shows the join already holds one.
- Any help page. No page under `help/` describes the runbook or the kickoff manifest, and
  `help/policy.md` is gov's own, unshipped (`tools/govkit/registry.toml:332-333`) and current.

### Edges

none

## 4. Design

### Evidence

Measured at `cae57b1d8`. Scratch-guard refused this role a leg run (`manifest-check.sh` was refused
by name), so memory hygiene, which the role may run, ran whole, and the other three legs were
re-derived from each checker's own predicate, read from its source and replayed read-only. Every
line this spec cites was re-read at `2550ccaa7` for rev-2, and the citations give the lines there.

| Leg | Re-derived at `cae57b1d8` | The predicate replayed |
|---|---|---|
| kickoff-manifest ratchet | check 9: 20 non-merge commits touching a `watch:` path since `last-body-change` `f221e1135`, against a cap of 10 | `skills/session-kickoff/manifest-check.sh:1645-1648`, a `git rev-list --count --no-merges` over the eleven `watch:` paths |
| memory hygiene | check 25: dSafePassage-26 S30 by name lists `loadDeclaredCap`, which no reader spells; check 23: `TOOL-dGroundRules-34/AC32`; check 9: the staged README | the leg's own run |
| method carriers | check 3: `tools/policy/caps.toml` and `tools/policy/check_policy.py` mention the method and are undeclared; no row is stale | the population at `tools/memory-tree/check-method-carriers.sh:66-74`, the registry parse at `:82` |
| govkit runbook parity | 19 problems against `PROBLEM_PIN` 18; the extra one is `registry entry 'policy' has no anchored runbook section` | `tools/govkit/check_runbook_parity.py:64-95` over `tools/govkit/registry.toml` and `WIRE-INTO-PROJECT.md` |

Check 5 of the ratchet holds at `cae57b1d8`. The one watched commit after `ea46113d8`, `f2b41e328`,
is itself the commit that stamped `last-audit` at `ea46113d8`
(`skills/session-kickoff/manifest-check.sh:1526-1542` reads it so). At `2550ccaa7` it still holds:
`last-audit` reads `5e8c8c5e7`, and the one watched commit after it, `2550ccaa7`, is the commit
that stamped it. `last-body-change` still reads `f221e1135`, and check 9's replayed count there is
22.

S3 needs no deviation record. It revises dSafePassage-26 past its audited rev-1, which the audit arm
addresses `TOOL-dSafePassage-26@rev-1` (`tools/memory-tree/deviation_join.py:603-606`).
`memory/builds/dSafePassage/build/2026-10-23-build-TOOL-dSafePassage-26-deviation-120.md` already
departs from that address, and the join is by address (`tools/memory-tree/deviation_join.py:671`).
Its host reports and never moves the exit (`tools/memory-tree/routed_commits.py:44-49`).

### Where the tree disagrees with the triage and the brief

- **Leg 1 is wider than one claim.** The triage found `memory/guides/SESSION-KICKOFF.md:172-173`
  calling a raise "an owner decision, not an edit". The same bullet calls the 48 KiB ceiling a gate.
  Since `69aa76517` every cap the census classes `switch`, 27 of its 33 rows, breaches as
  `budgets.enforce` says (`tools/check-template-size.sh:17-21`). That includes the template's row
  and check 6's per-class caps (`tools/policy/caps.toml:114-115`). This repository sets it to warn
  (`.governance/policy.toml:5`). A run may also raise a measured-file row on the terms the limits
  file's header states (`tools/template-size-limits.txt:16-24`). And §B names nothing of this
  build's policy file, while the pre-commit guard refuses every agent edit to it but one raised cap
  (`help/policy.md:149-191`). S1 answers all three.
- **Leg 2's by-value half names a function too.** `read_legacy_fanout`
  (`tools/policy/policy.py:767`) spells `FANOUT_CAP` through `FANOUT_LINE` (`:764`) and
  `.agent-cap.conf` through `LEGACY_FANOUT` (`:763`), as the triage says. The value reaches the agent
  limit through `derive_lowered_limit` (`:789-804`), and the hook reads that limit in
  `readWriterBound` (`tools/hooks/agent-cap.js:466-471`). S3's by-value half names
  `derive_lowered_limit`.
- **dSafePassage-26 logs its revisions in §9.** The brief says §8. That spec is Tier-2: its §8 is
  the open questions (`:698`) and its §9 the revision log (`:721`).
- **The runbook's kit-path placeholder is `<prefix>`.** The brief says `<tool-root>/`. The runbook
  defines `<prefix>` (`WIRE-INTO-PROJECT.md:25`) and spells it 123 times, and `<tool-root>` never.
  The install-prefix leg drains both spellings (`tools/check-install-prefix.sh:53`) and reads the
  runbook (`:241`). S6 spells `<prefix>/`, the placeholder the runbook defines.
- Legs 8 and 10 agree with the triage. The carriers registry keys on path alone
  (`tools/memory-tree/check-method-carriers.sh:82`, `:92`), so the four line sites are two rows.

### The manifest

The §B re-audit at `cae57b1d8`, claim by claim. The builder re-runs the same probes at the audit
commit, because `TOOL-dGroundRules-84` and `TOOL-dGroundRules-85` landed between. At `2550ccaa7`
the §B body is byte-identical to `cae57b1d8`'s; only the `last-audit` stamp moved.

| §B lines | What was probed | Verdict |
|---|---|---|
| 49-73 | every path cited resolves in `git ls-files`; every key and flag is spelled by the file the bullet names; `BUILD-METHOD.md` M2, M3 and M6 exist; `memory/guides/UNATTENDED-STOPS.md:561` is §13 | holds |
| 61, 70 | `GATE_BOUND` is the unattended kit's (`.unattended.conf:58`, `tools/unattended/check-unattended.sh:271`); `SPEC_AUDIT_DEFAULT` is `.unattended.conf:326` | holds |
| 74 | check 6's per-class caps are the bound | holds; the switch over them is S1's trap |
| 81-84 | each entrypoint and `memory/builds/aDeployScout/` resolves | holds |
| 88-112 | each flag is spelled by its script: `--regen`, `--calibrate-width`, `GATE_ATTRIBUTE`, `--pooled`, `GOV_NODE`, `--attribute`, `--for-diff`, `--for-paths`, `--base`, `--terms` | holds |
| 117-133 | `--new-spec` in `gen_build_index.py`; `parse_spec_h1` in `tools/memory-tree/tree_lib.py`; `memory/ledger/` holds month files | holds |
| 140-142 | the self-test suites stay held by default (`:94`) | holds; its prune condition is unmet |
| 169-215 | every cited path and hook exists, including `tools/unattended/gate-guard.js` | 172-173 stale, the rest hold |

S1's pointer bullet, inserted after `:75` as one line:

```
- This repository's policy values live in `.governance/policy.toml`, checked against `tools/policy/catalogue.toml`; the pre-commit guard refuses an agent's change to it but one raised measured-file cap with its record (`help/policy.md`).
```

S1's trap bullet, in place of the two lines at `:172-173`:

```
- Every size cap `tools/policy/caps.toml` classes `switch`, the template's and check 6's among
  them, warns or refuses as `budgets.enforce` in `.governance/policy.toml` says
  (`help/size-caps.md`). A run raises the template's row only on the terms in the header of
  `tools/template-size-limits.txt`. Read the margin FROM `bash tools/check-template-size.sh`.
```

The pointer bullet measures 237 bytes and the trap bullet 361, under check 8's 400-byte line cap
and check 11's 400-byte bullet cap (`skills/session-kickoff/manifest-check.sh:1319-1320`). Neither
names the switch's value, which `.governance/policy.toml` owns.

S2's stamps follow the stamp rule, "sha = `HEAD` on any branch; datetime always advances". The audit
commit is `HEAD` when the builder starts the audit, after `TOOL-dGroundRules-84` and
`TOOL-dGroundRules-85` have landed. Its full sha is what `git rev-parse HEAD` prints there, and the
datetime is what `date -Iseconds` prints:

```
last-audit: <date -Iseconds at the audit> @ <git rev-parse HEAD at the audit>
last-body-change: <git rev-parse HEAD at the audit>
```

No file this unit touches is a `watch:` path, so after its commit check 9 counts 0 commits since the
audit commit and check 5 finds no watched commit after it. The commit message carries this line, in
the shape of the precedent `d85890512`, `<A8>` being the audit commit's first eight hex digits:

```
manifest-audit: delta section B gains a pointer to the policy file and its guard, and the size-cap trap names the budgets switch and the limits file's raise terms (TOOL-dGroundRules-9, -10); last-audit and last-body-change advanced to <A8> · watch-commits-since-stamp: 0
```

### The Readers clause

Landed by rev-2's pass (S3); this section records what it wrote. The five lines at
`memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-26.md:258-262` read:

```
  **Readers:** by name: `read_legacy_fanout` in `tools/policy/policy.py`, whose `FANOUT_LINE` spells
  `FANOUT_CAP` and whose `LEGACY_FANOUT` spells `.agent-cap.conf`, and the other files S43's grep
  prints, which that item derives and disposes · by value: `derive_lowered_limit` in
  `tools/policy/policy.py`, which lowers `runtime.agents-in-flight` to that line's value where it is
  smaller, the value the step's up carries to `runtime.agents-in-flight`. Observed by AC29.
```

Every by-name token resolves: `tools/policy/policy.py` is a tracked path, and that file spells
`read_legacy_fanout`, `FANOUT_LINE`, `FANOUT_CAP`, `LEGACY_FANOUT` and `.agent-cap.conf`
(`tools/policy/policy.py:763-768`). Check 25 resolves a token as a tracked path, or as a whole
token spelled by a tracked file outside the memory tree's records
(`tools/memory-tree/check-memory-hygiene.sh:2858-2910`).

The header reads
`**Status:** DEFERRED · rev-5 · 2026-10-25 · node d · Tier-2 · base 3708a705 · streams tooling · order 6 · advances TOOL-dSafePassage-14`.
The §9 line after rev-4:

```
- rev-5 · 2026-10-25 · §2 · S30 · the Readers clause names the code that reads `FANOUT_CAP` since `TOOL-dGroundRules-10` (`2ebafd441`) moved the agent limit to the policy reader: `read_legacy_fanout` and `LEGACY_FANOUT` by name and `derive_lowered_limit` by value, each in `tools/policy/policy.py`. Hygiene check 25 found the hook function the clause named spelled by no reader. Written by `TOOL-dGroundRules-86`; no other section moved.
```

### The ledger answer

Line 51 of the ledger opens `` - AC32 — `gen:build-order` — through `` and keeps the rest. Check 23
passes a pair when either backticked token contains the other after case folding
(`tools/memory-tree/check-memory-hygiene.sh:3390-3394`). `gen:build-order` sits inside the
criterion's own token
(`memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-34.md:571`), and the answer
already reports the grep that printed `165` and `179`.

### The carrier rows

Appended after `:35`, in the shape of the `tools/template-size-limits.txt` row (`:21`):

```
tools/policy/caps.toml · the size-cap census row for the rendered method: its name and its limits-file home are the method's path, the subject the cap measures — a row keyed by the file, never a restatement of what the method says
tools/policy/check_policy.py · the cap census's case table and its budgets-correctness-kept case name the method's path as a size-cap subject they plant into a scratch repository — a path the checker reads, never a restatement of what the method says
```

The two sites are `tools/policy/caps.toml:63`, `:67` and `tools/policy/check_policy.py:3489`,
`:3758`. Neither file holds a `## M<n>` heading, so check 5 of the leg stays clean.

### The runbook section

The 3h section's shape (`WIRE-INTO-PROJECT.md:732-751`): the anchor, a `##` heading, one paragraph
saying what the kit is and whether it is a default, then numbered steps. The facts: the registry's
default list holds no `policy` (`tools/govkit/registry.toml:38-54`); `review-harness` requires it
(`tools/workflows/kit.toml:10`) and it requires `memory-tree` (`tools/policy/kit.toml:12`); govkit
refuses an unmet dependency and never widens a selection (`tools/govkit/govkit.py:7558-7564`); the
adopter, its regenerate and its check are `tools/policy/kit.toml:32-43`; its printed strings are
`tools/policy/adopt-policy.sh:93`, `:136`; the shipped leg is `tools/policy/kit.toml:79-81`.

The section opens with the anchor line `<!-- govkit:entry policy -->`, then the heading line
`## 3i — Adopt the policy kit (with the review harness)`, then one blank line and this body. The two
lines sit outside the fence here only so this spec carries no column-0 heading inside a fence:

```
One file per repository, `.governance/policy.toml`, holds the policy values its gates and hooks
read, each checked against the kit's catalogue. The kit is not in the default selection. The
`review-harness` kit requires it, and `govkit` refuses a selection that names a kit without what it
requires, naming the missing id.

1. Add `policy` to `kits` in `.governance/deploy.toml`, with `memory-tree`, which it requires.
2. **What the install renders.** The kit's adopter, `bash <prefix>/policy/adopt-policy.sh
   --scaffold`, runs at install and at every update unless `GOVKIT_RERENDER=0` declines it. It
   writes the starter policy file only where none exists, and says `kept` otherwise: the file is
   yours from its first write. It then renders the harness's two concurrency settings in
   `.claude/settings.json` and the JSON mirror the hooks read, `.governance/policy.json`.
3. **Commit, then re-run.** The mirror renders a commit, so on install day `--scaffold` prints one
   line deferring it, ending `commit, then re-run --scaffold`, and exits 0. Commit the install and
   the policy file, then run `--scaffold` again.
4. **The leg ships.** The kit's `policy check` leg runs `python <prefix>/policy/check_policy.py`
   over your policy file, and `adopt-policy.sh --check` runs the same check. Every key, its allowed
   values and its default are rows of `<prefix>/policy/catalogue.toml`, whose grammar
   `<prefix>/policy/README.md` gives.
```

Every kit path is `<prefix>/`-spelled. The text cites no charter section by number, which the
playbook-parity leg reads the runbook for (`tools/check-playbook-parity.sh:156`, `:341`).

### What this does not check

- No leg reads §B's prose. AC1's two greps observe S1's trap only; the other verdicts of the
  re-audit are the builder's reading, recorded in the commit's delta line.
- The ratchet grades the stamps' shape and ancestry, never that §B was read.
- Runbook parity grades an anchor and a non-empty body, never the prose
  (`tools/govkit/check_runbook_parity.py:14-17`). The install-prefix and playbook-parity legs read
  S6's text at the close.
- Check 25 resolves names and never asks whether the list is complete.

### Rollout

This unit builds at order 33, after `TOOL-dGroundRules-84` and `TOOL-dGroundRules-85`. The builder
sets this spec's status from DEFERRED to INPROGRESS before its first write, because
`WIRE-INTO-PROJECT.md` is under `ROUTED_PATHS`. The commit renders the build README with
`gen_build_index.py --write`. If runbook parity at the audit commit, before S6, counts other than
19, the pin's move is outside this unit: the builder reports it and leaves `PROBLEM_PIN` as it is.

### Files touched (estimate)

- `memory/guides/SESSION-KICKOFF.md`
- `memory/builds/dGroundRules/build/2026-10-23-build-TOOL-dGroundRules-34-ledger.md`
- `memory/project/method-carriers.txt`
- `WIRE-INTO-PROJECT.md`

## 5. Acceptance criteria

All commands run from the repository root of the pass's worktree, in Git Bash, at the audit commit
with S1, S2, S4, S5 and S6 applied in the worktree and before the unit's commit. S3 is already in
that tree, landed with this spec's rev-2 commit. Each break below is the same command on the tree
before this unit's edit, which at `cae57b1d8` printed what the clause quotes. The hygiene
criterion's green and its break were both observed at `cae57b1d8` in a scratch clone, with S3 and
S4 applied as §4 gives them. The carriers and runbook criteria were observed by replaying each
checker's predicate there with S5 and S6 applied: no carrier undeclared or stale, and 18 runbook
problems.

- **AC1** — When `bash skills/session-kickoff/manifest-check.sh` runs, it prints no `MANIFEST check 9 FAILED` line and no `MANIFEST check 5 FAILED` line, and exits 0. Then `git grep -c "budgets.enforce" -- memory/guides/SESSION-KICKOFF.md` prints `memory/guides/SESSION-KICKOFF.md:1`, and `git grep -c "an owner decision, not an edit" -- memory/guides/SESSION-KICKOFF.md` prints nothing.
  Red when: the stamps and the trap stand as at `cae57b1d8`. Then the ratchet prints `MANIFEST check 9 FAILED` ending `non-merge commits since f221e113556ac8406fcbd834cce37f746c23bd73`, and the second grep prints `memory/guides/SESSION-KICKOFF.md:1`.
  figure: DERIVED. The watched-commit count was 20 at `cae57b1d8` and 22 at `2550ccaa7`, replayed, the two added being the commits of `TOOL-dGroundRules-84` and `TOOL-dGroundRules-85`.
- **AC2** — When `bash tools/memory-tree/check-memory-hygiene.sh` runs, no line it prints names `§2 item S30` of `2026-10-23-spec-TOOL-dSafePassage-26.md`, and no line names `TOOL-dGroundRules-34/AC32`. The first half is S3's: the main loop observes it at the close, over the tree this spec's rev-2 commit leaves. The second half is S4's, observed at the audit commit.
  Red when: S3's clause and S4's token are absent. Then it prints `HYGIENE check 25 FAILED` with a line naming `§2 item S30` and `loadDeclaredCap`, and `HYGIENE check 23 FAILED` ending `TOOL-dGroundRules-34/AC32`. Both were printed at `2550ccaa7`, before rev-2's pass.
- **AC3** — When `bash tools/memory-tree/check-method-carriers.sh` runs, it prints one line, `method-carriers:` followed by the carrier count and `carrier(s), all declared and pointing`, and exits 0.
  Red when: S5's two rows are absent. Then it prints `METHOD-CARRIERS check 3 FAILED` and the two indented paths `tools/policy/caps.toml` and `tools/policy/check_policy.py`, and exits 1.
  figure: DERIVED. The carrier count was 33 at `cae57b1d8`, replayed from the leg's own population.
- **AC4** — When `python tools/govkit/check_runbook_parity.py` runs, it prints `runbook-parity: 18 problem(s) · pin 18`, no line naming the entry `'policy'`, and exits 0.
  Red when: S6's section is absent. Then it prints `runbook-parity: registry entry 'policy' has no anchored runbook section`, `runbook-parity: 19 problem(s) · pin 18` and a line opening `runbook-parity: 1 MORE than the pin`, and exits 1.
  figure: PINNED. 18 is `PROBLEM_PIN` (`tools/govkit/check_runbook_parity.py:60`), and the count before S6 was 19 at `cae57b1d8`, replayed.

## 6. Gates

`recall floor` · `recall floor arms` · `kickoff-manifest ratchet` · `memory hygiene` · `method carriers (every pointer declared)` · `govkit runbook parity` · `install-prefix (shipped surface)` · `playbook parity` · `spec tokens (a spec's own names resolve)`

Run through `derive_guarded_legs` at `2550ccaa7`, `python tools/check-spec-tokens.py --legs-for`
over the four files touched names two guarded legs. Each of the three `memory/` files trips
`recall floor` and `recall floor arms` through the guard `memory/`, which two legs carry, under the
broad floor of 5. `WIRE-INTO-PROJECT.md` trips no guarded leg.

The unguarded legs named beside them read what this unit changes:

- `kickoff-manifest ratchet` reads S1 and S2, observed by AC1.
- `memory hygiene` reads S3 and S4, observed by AC2, S3's half at the close. Its check 12 also
  grades S3's header rev against the rev-5 line in dSafePassage-26's §9.
- `method carriers (every pointer declared)` reads S5, observed by AC3.
- `govkit runbook parity` reads S6, observed by AC4. Its pin of 18 does not move: S6 takes the
  count from 19 to 18, which the pin already holds.
- `install-prefix (shipped surface)` reads the runbook (`tools/check-install-prefix.sh:241`). S6
  spells only `<prefix>/`, a drained spelling (`:53`).
- `playbook parity` reads the runbook and `memory/guides/`. Neither S1 nor S6 cites a charter
  section by number.
- `spec tokens (a spec's own names resolve)` reads this spec while it is INPROGRESS. Its joins over
  live specs read no DEFERRED spec, dSafePassage-26 included (`tools/check-spec-tokens.py:331`).

No arm is added or moved. No floor, ceiling or pinned count moves.

## 7. Open questions

none

## 8. Revision log

- rev-1 · 2026-10-25 · initial draft from this unit's spec brief, grounded at `cae57b1d8`. Each of
  the four legs was re-derived over the current tree: memory hygiene by its own run, and the
  manifest ratchet, method carriers and runbook parity by their checkers' predicates replayed
  read-only, since scratch-guard refused this role the leg runs. The re-audit read §B whole and
  found the trap at lines 172-173 wider than the triage's one claim, and §B silent on this build's
  policy file. Four corrections are in §4: the size-cap switch, the by-value reader
  `derive_lowered_limit`, dSafePassage-26's revision log at §9 rather than §8, and the runbook's
  `<prefix>` placeholder rather than `<tool-root>`. Two follow-ups for the main loop, neither a
  fork. dSafePassage-26 S30's body still cites `tools/hooks/agent-cap.js:1631-1632` as the shared
  parser of `.agent-cap.conf`, and those lines parse handoff marks now; dSafePassage's own run owns
  that clause. And deviation record 120 of dSafePassage lists the commits that revised
  dSafePassage-26 in its After and Evidence fields, which S3's commit will not be among; the join
  is by address and holds. The triage record, the brief and this role's prompt, untracked when this
  draft was written:

```
memory/builds/dGroundRules/build/2026-10-25-build-TOOL-dGroundRules-84-research-bar-triage.md
memory/builds/dGroundRules/prompts/2026-10-25-prompt-TOOL-dGroundRules-86-spec-brief.md
memory/builds/dGroundRules/prompts/2026-10-25-prompt-TOOL-dGroundRules-86-1-spec-writer.md
```

- rev-2 · 2026-10-25 · §1 · S3 · §3 · §4 · AC1 · AC2 · §6 · S3 leaves the build for this spec-writer
  pass, which landed it in dSafePassage-26 with this spec's commit. The rev-1 builder returned a
  DIVERGENCE with nothing committed, because scratch-guard admits a product role only a status
  flip, and only on a spec its route names (`tools/hooks/scratch-guard.js:1064-1086`);
  dSafePassage-26 is not on the route. §4 "Files touched" drops that path, so §6's guard derivation
  reads four files, re-run at `2550ccaa7` with the same two guarded legs. AC2's check-25 half is
  observed at the close over the tree this pass leaves. Every cited line was re-read at
  `2550ccaa7`. Seven had moved, and each now cites its line there: the check 9 and check 5
  predicates of `skills/session-kickoff/manifest-check.sh`, 15 lines lower; check 25's resolution rule and
  check 23's containment test in `tools/memory-tree/check-memory-hygiene.sh`, 14 lines lower; the
  two `tools/policy/check_policy.py` method sites, one lower; and the deferral line of
  `tools/policy/adopt-policy.sh`, one lower. Every other citation reads at `2550ccaa7` as rev-1
  says. The §B body is unchanged since `cae57b1d8`; `last-audit` was re-stamped at `5e8c8c5e7`, and
  check 9's count is 22. S1, S2, S4, S5 and S6 did not move. The two follow-ups rev-1 names stand.
  This pass's brief and prompt, untracked when it was written:

```
memory/builds/dGroundRules/prompts/2026-10-25-prompt-TOOL-dGroundRules-86-rev2-brief.md
memory/builds/dGroundRules/prompts/2026-10-25-prompt-TOOL-dGroundRules-86-2-spec-writer.md
```

## 9. Reuse audit

Each fix extends the record or the doc that already holds its fact. S1 and S2 reuse the
`TOOL-dTrueNorth-27` re-audit at `d85890512`: both stamps at the audit commit and a
`manifest-audit: delta` line. S3 keeps S30's clause shape and changes only the readers it names.
S5's rows take the shape of the `tools/template-size-limits.txt` row of
`memory/project/method-carriers.txt` (`:21`). S6 follows the 3h section of `WIRE-INTO-PROJECT.md`
(`:732-751`) and keys on the entry `tools/govkit/registry.toml` declares at `:126-127`. Its facts
are read from `tools/policy/kit.toml` and `tools/policy/adopt-policy.sh`, never restated beyond them.
`python tools/codebase-map/reuse_lookup.py "an anchored runbook section for a registry entry and a declared method-carrier row"`
ranked only name stems (`rows`, `row`, `declares`, `resolve_entry`), and none writes a record or a
runbook section. No existing seam fits beyond the records and the runbook themselves. The recall
probe returned the `TOOL-dTrueNorth-27` brief and spec writer's prompt for the re-audit, the
`dClosedLoop` session log's delta line shape, `TOOL-aHonedRuleset-13` on check 9's counter, and a
review recording that a watched-file commit owes both stamps, not one.

Recall terms used: `python tools/memory-recall/query.py "re-audit the kickoff manifest section B and advance last-body-change after a build's watched commits" --terms "manifest-audit last-body-change last-audit re-stamp watch-commits-since-stamp check 9 stall SESSION-KICKOFF §B runbook-parity govkit:entry method-carriers Readers"`
