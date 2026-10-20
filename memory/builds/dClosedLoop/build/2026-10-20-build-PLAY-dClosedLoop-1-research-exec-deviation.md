# Research: specs held to the design, strictly, for the chain's execution

**Serves:** research PLAY-dClosedLoop-1

This is dispatch 218's return, verbatim, except that a title line would be demoted to keep one H1 per record.
Its question is in `prompts/2026-10-20-prompt-PLAY-dClosedLoop-1-55-researcher.md`.

---

**Specs held to the design: research return (PLAY-dClosedLoop-1, question 5)**

**Answer in brief:** today nothing runs the three bootstrap instruments at a commit, a pass or a landing. They do red correctly on most plants. But in my scratch probes several wrong carries and undeclared departures went green, an owner approval can't be told from an agent's, and two false reds came up. My recommendation is one new gate leg (a check in the merge bar), built as dTrueNorth's first unit after the instruments are fixed. Owner-level deviations get parked in unattended runs.

Repo-relative paths below sit under `C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/`. The design build's folder `memory/builds/dClosedLoop/build/` is written `B/`, and its files keep only their suffix (`B/…-carries.py`). Probes ran in a `--shared` clone at `4592ab001` under my scratch folder (`…/scratchpad/exec/d218/repo`, helpers `mkspecs.py`, `plant.py`, `run.sh`). Nothing was written to the repository.

## Facts

**What a chain spec and a commit must carry**
- **Spec lines:**
  - `**Carries:** cl-…@<hash8> whole | part k/n`, `node:<ns>.<key>`, `**Derived:**`, `**Moved|Retired|Deferred:** … by <decision>` (`B/…-carries.py:7-12`).
  - The hash is the first 8 hex digits of the SHA-256 of the clause text, with the id cut off and whitespace folded (`B/…-carries.py:13,78-80`; `B/…-architecture-v2.md:1798-1801`).
- **Deviation record:**
  - It lives in the departing build's `build/` folder as `<date>-build-<unit>-deviation-<n>.md`.
  - Fields: Departs from, Hand-off, Before/After, Cause, Reason, Evidence, Risk, Approver, Follow-through (`B/…-deviations.py:7-16`).
  - Approval by risk: editorial needs the author or above; additive or stricter needs the spec writer; loosening or breaking needs the owner; an owner ruling always needs the owner (`:17-18`; `B/…-final-questions.md:191-199`).
- **Deviation population:**
  - every clause-hash move since `Baseline:`;
  - every spec revision after the unit's first `Pass: <unit>` commit, except status-only edits;
  - every `AMENDED` line naming `(deviation <record>)`.
  - Source: `B/…-deviations.py:20-27`.
- **As-built view:** `amends`/`supersedes` rows read from **Follow-through:**; it must be regenerated and is never hand-edited (`B/…-asbuilt.py:2-14`).

**What the instruments don't read**
- Whether a spec means what its clause means, and specs outside the chain (`B/…-carries.py:31-33`).
- Whether a record's reason or risk is honest, and a departure made in code alone (`B/…-deviations.py:36-37`).

**What dTrueNorth replaces them with**
- cl-0001 to cl-0006 (`B/…-architecture-v2.md:1764`):
  - cl-0001: the `**Carries:**` parse behind a config cutoff;
  - cl-0002: the carries join added to the spec-tokens leg;
  - cl-0003: the coverage report, and hygiene refusing a spec at INPROGRESS while coverage is red;
  - cl-0004: the deviation join at the commit (through routed-commit attribution) and at the close;
  - cl-0005: audits pinned to `@rev-N`;
  - cl-0006: the as-built view.
- These are themselves stand-ins. Their successors are the classifier (cl-0066, `:1767`), `deviation.approval` (cl-0119, `:1769`), `design.coverage` (cl-0398, `:1780`) and `deviation.gate` (cl-0412, `:1781`).
- dTrueNorth's own specs are checked by the instruments, because its gate doesn't exist yet (`B/…-final-questions.md:287`).

**Nothing runs the instruments today**
- No file under `tools/`, `skills/`, `.claude/`, `.github/` or `.githooks/` names them or `**Carries:**` (grep came back empty).
- A project Definition-of-Done item (`DOD_EXTRA`) is only attested, never executed (`tools/unattended/unattended.sh:12225-12226`).
- The leg file can be replaced through `GATE_LEGS` but not extended (`tools/run-gates/run-gates.sh:246`), and `tools/` is a routed path (`.memory-tree.conf:9`).
- The driver runs `SPEC_TOKENS_CLI` only at `--dispatch` (`unattended.sh:13493-13508`; `.unattended.conf:201`).
- Remote CI runs the full bar with `fetch-depth: 0` (`.github/workflows/remote-ci.yml:61,106`). The lander reconciles with the remote before the gate runs (`memory/guides/UNATTENDED-PROTOCOL.md:424-427`).

**Owner approval in an unattended run**
- After preflight a run gets no further owner word (`UNATTENDED-PROTOCOL.md:626-631`).
- A change that needs the owner is parked (`:664-668`).
- The driver honours an owner grant only from the default-branch anchor (the remote main the run started from), where the run cannot have written it (`unattended.sh:4161-4167`; protocol `:116-117`).
- The Approver field is free text, matched by prefix (`B/…-deviations.py:81-87`). This is the class `gap-flow-14` describes (`B/…-gap-register.md:120`).

**Where the records and the code disagree**
1. **AMENDED.**
   - The records: the ledger lives in journal records as `amended rev-<n>`, "never in the spec" (`memory/HYGIENE.md:604-606,619`), and check 23 matches the lowercase form (`tools/memory-tree/check-memory-hygiene.sh:3013`).
   - The code: `deviations.py:159-162` reads any spec line containing `AMENDED`.
   - Effect: it reads a form no ledger writes, and it false-reds a spec that quotes cl-0004. Seen on my first clean spec set.
2. **Revision numbers.**
   - The records: the spec header's `rev-N` changes only on a material edit (`memory/TEMPLATE-SPEC.md:58,67`).
   - The code: `deviations.py:153-158` numbers revisions by commit count.
3. **Which commit is a pass.**
   - The records: the driver falls back to the commit subject when there is no trailer (`tools/unattended/lib-unattended.sh:1050-1058`), and `routed_commits.py` takes subject and trailer together (`tools/memory-tree/routed_commits.py:22-26`).
   - The code: `deviations.py:150` greps only `^Pass: <unit>$`.
   - Effect: 209 of 722 commits touching `tools/` or `skills/` since 2026-10-01 have no `Pass:` trailer (measured).

## Probes

On the tree as it stands: `carries` exits 2 (no spec measured), `deviations` exits 0 with 0 members, and `asbuilt --check` exits 0. Every built-in plant reds as documented. Each instrument takes under 0.9 s.

The clean two-spec dTrueNorth set reds once, legitimately: dTrueNorth owns `record-kind.deviation` and no spec named it. Once fixed it is green.

**A spec that carries a clause wrongly**

| Plant | What catches it |
|---|---|
| Stale pin | carries (exit 1) |
| `part 1/2` with no `2/2` | carries |
| Two nodes each carrying cl-0006 whole | carries, but only on the merged tree. Each branch alone shows no ambiguity, so the check must run after the lander's reconcile |
| A dTrueNorth spec carrying dGroundRules' cl-0007 | **Nothing.** The join never checks which build a clause belongs to (`carries.py:185-201`) |
| Contradicts its clause but keeps every token | **Nothing** (documented: only a semantic review sees it) |
| A clause dropped, then the spec edited again | Caught at the dropping commit. **Escapes** after the next edit, because the drop arm compares only the last two revisions (`:125-126`). Only `--exit` catches it |

**An undeclared departure**

| Plant | What catches it |
|---|---|
| Spec revised after a `Pass:` commit, no record | deviations |
| Same, record present with a loosening approved by "author" | deviations (approver below the risk) |
| Same, approver written as "owner" | **Green**, though no owner was involved |
| v2 clause edited in place | deviations (clause moved) and carries (stale pin) |
| Spec revised after a pass that is named only in the commit subject | **Nothing** |
| Node a revises the spec while node b's pass is in flight, then both merge | **Nothing.** The revision is not a descendant of the pass |
| cl-0119 loosened, then `Baseline:` re-pointed at that commit | Red, then **green**. The baseline is read from v2's working tree (`deviations.py:133-136`) |
| A record addressed by the header's rev-1 after a status-only commit | **False red** (it wants `@rev-2`) |

Also: `asbuilt --check` reds on every new record until `--write` is run (`asbuilt.py:81`).

The instruments sit under `memory/`, so any run can edit them. That is the `TOOL-aStandingWrit-7` class (`memory/builds/aStandingWrit/BACKLOG.md:11`).

## Candidates

| | How it works | Test that could make it lose | Result |
|---|---|---|---|
| **A** | A per-unit command in each spec's Gates section, or a `DOD_EXTRA` item, run by the agent | Does anything refuse a landing when the agent skips it? | **Loses.** It is attested only (`unattended.sh:12225`) |
| **B** | Point `SPEC_TOKENS_CLI` at a wrapper under `memory/` that runs both joins | A departure committed after the run's last dispatch, or in an attended session, or pushed to CI | **Loses.** It runs only at `--dispatch` (`:13493`); it also needs an owner turn to change the conf, and the run can edit the wrapper |
| **C** | Merge-bar legs running the instruments: at pre-push on every node, at `--close` (gates-green), in remote CI, on the lander's reconciled tree | All the plants above | **Survives only after hardening.** As written it misses the escapes and false reds above, and exits 2 on today's tree |
| **D** | Pre-commit or commit-msg hook | A hand-made worktree with no hooks path set (it is per worktree, `config.worktree`) | **Loses as the gate.** Pre-push already covers it; keep only as an early warning |
| **E** | Opt-in spec audit, and the owner reading the coverage report at each Design exit | A stale pin in a build with no `spec-audit:` line | **Loses as a gate** (`specs-audited` is not owed, protocol `:355`). It is the **only** catcher of a semantic contradiction, so it is a required complement |

## Recommendation

**1. Make C the gate, as dTrueNorth's first unit.** Land it together with dTrueNorth's first specs, so the join never exits 2. The legs run:
- `carries` (and `--exit` per build at its Design exit);
- `deviations`;
- `asbuilt --check`.

Before it lands, harden the instruments. They are design-build records, not product code:
- pin the baseline sha and the instruments' blob hashes in the leg's argv, so changing them is a routed edit;
- add a check that a carried clause belongs to the spec's own build;
- attribute a pass from subject and trailer together, as `routed_commits.py` does;
- count any revision that is not an ancestor of the first pass;
- read `amended rev-N` from journal ledgers;
- address `rev-N` by the spec header, not by commit count;
- declare the leg's history and base reads.

Each node is then gated by the same pre-push bar, `--close` and CI.

**2. Approval by risk when unattended.**
- Editorial: the run's own agent approves.
- Additive or stricter: the spec-writer role approves, with a re-audit record at the new revision.
- Loosening, breaking or an owner ruling: **park** it as a surfaced decision and set the unit to BLOCKED, so nothing that departs lands. The owner approves in an attended turn, quoted. A deviation known in advance can be pre-approved by a decision id on an owner-committed `may:` line.

**3. Switching to dTrueNorth's controls without a gap.**
- Set the product join's cutoff at or before the first chain spec's date, not the date the join lands. The repo's usual cutoff convention would exempt dTrueNorth's own specs.
- Run the bootstrap and product legs together until the product reds on every plant above.
- Retire each bootstrap leg in the unit that re-points it: cl-0398, cl-0412, cl-0119 and cl-0066.

## What today's gov cannot do, and the smallest change for each

1. **Run the comparison at any landing.** Change: **a chain build's unit**, dTrueNorth unit 1, bootstrap legs as in recommendation 1, plus the instrument fixes as a records commit.
2. **Verify an owner's approval.** Change: **a policy** (park loosening and breaking deviations; owner approvals only in attended turns), until cl-0119 and the guard land.
3. **Catch a semantic contradiction or a code-only departure.** Change: **a manual step**. The owner adds `spec-audit:` to every chain build README, and reads `carries.py --report <slug>` at each Design exit.
4. **Catch a dropped clause after a later edit.** Change: **a manual step**. Run `carries.py --build <slug> --exit` at every Design exit, until cl-0003 makes hygiene refuse it.

**For you to run:** the scratch guard refuses a researcher running a gate leg. In the main session, please run `python tools/check-spec-tokens.py` over a tree holding a planted stale pin, to confirm today's spec-tokens leg is blind to it (expected: green).
