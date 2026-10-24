# TOOL-dDeclaredLoop-34 — the deviation approval route read from deviation.approval: by its risk, the owner for all, or its author recorded

**Status:** OPEN · rev-1 · 2026-10-24 · node d · Tier-2 · base ed497191 · streams tooling · order 27 · advances TOOL-dDeclaredLoop-35

**Carries:** cl-dClosedLoop-0119@a9b53abc whole
**Carries:** node:policy-key.deviation.approval

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-TOOL-dDeclaredLoop-1-reuse-scout-c.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-reuse-scout-c.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 |
| [2026-10-24-build-TOOL-dDeclaredLoop-1-spec-stage-returns.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-spec-stage-returns.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 |
| [2026-10-24-prompt-TOOL-dDeclaredLoop-1-spec-brief.md](../prompts/2026-10-24-prompt-TOOL-dDeclaredLoop-1-spec-brief.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 |

<!-- /gen:spec-records -->

## 1. Goal

Who may approve a departure is a policy value, `deviation.approval`, read by the deviation join's
approver check, with each of its three values graded: `by-risk` (an editorial deviation its author's,
by dOrderedCharter's classifier and not by the record's own word; an additive or stricter one the spec
writer's with the changed sections re-audited at the new revision; a loosening or breaking one the
owner's), `owner-all`, and `author-recorded` (the owner's FQ-3, P41; v2:1293). Today the value is a CLI
flag, `--approval` (`tools/memory-tree/deviation_join.py:1750`), `owner-all` does not exist, the
editorial class is typed by the record, and nothing asks for the re-audit.

## 2. Scope (IN)

- **S1** — The value's reader, `read_approval(root, rev)` in `tools/memory-tree/deviation_join.py`:
  `deviation.approval` through dGroundRules-2's `resolve` (I10), its catalogue row already written,
  default `by-risk`; a value outside `by-risk`, `owner-all` and `author-recorded` refuses naming the key.
  The policy kit is imported from `<prefix>/policy/` as an optional slot with a named fallback: where it
  does not resolve, the default stands and one line says so. `APPROVALS` (:143) gains `owner-all`.
  Observed by AC1 and AC7.
- **S2** — The flag `--approval` (:1750) retires: the CLI, the fixture and the self-test read the
  value from the repository they grade, each fixture repository carrying a committed
  `.governance/policy.toml` that sets it. **Readers:** by name: `tools/memory-tree/deviation_join.py`,
  whose usage block (:74-75), argument table (:1750) and two calls passing `a.approval` (:1765, :1786)
  are re-pointed · by value: `HOST_APPROVAL` in `tools/memory-tree/deviation_join.py` (:144), passed at
  :823 and :825, which S7 keeps as the chain's ruled override. Observed by AC1.
- **S3** — `owner-all`: `check_approver` (:705-733) refuses every record whose approver is not the owner,
  and grades every owner approval by the decision-row citation it already grades (:719-733). Observed
  by AC2.
- **S4** — The editorial class from the classifier. Under `by-risk`, a record whose risk reads
  `editorial` is graded editorial only when dOrderedCharter-33 S1's `derive_change_mark` over the
  record's `Before` and `After` texts returns `editorial`; otherwise the record is refused, naming the
  record and the first differing word, so an author cannot approve a semantic change by calling it
  editorial. `tools/playbook/pins.py` is called as an optional slot: where it does not resolve, the typed
  risk stands and one line says so. Observed by AC3 and AC4.
- **S5** — The re-audit at the new revision. Under `by-risk`, a record at risk `additive` or `stricter`
  approved by the spec writer is refused unless the unit it departs is pinned by a `spec-audit` record
  at a revision later than the one it departs: the unit and revision from `Departs from`
  `<unit>@rev-<N>`, or, for a clause, the spec carrying it through `design_lib.scan_chain_specs` and the
  revision that first carried the change; the pins from `tree_lib.read_bindings` as the join already
  reads them (:562-576). Observed by AC5 and AC6.
- **S6** — The owner's ruling quoted: under every value, an owner approval cites a decision id whose
  row DECISIONS.md holds on the mainline and names the departed clause or new unit, as today
  (:719-733). Observed by AC2.
- **S7** — The chain's ruling stands for the chain. The leg's host keeps passing `author-recorded`,
  `PLAY-dClosedLoop-4`'s ruled value, as an explicit override of the key, and the CLI and every other
  caller read the key. The docstring's approval paragraph (:58-64) says so. Observed by AC7.
- **S8** — The plants, through `python tools/memory-tree/deviation_join.py --fixture --plant <case>`,
  each fixture repository's policy file setting its value: `owner-all-author`, `owner-all-cited`,
  `author-recorded-loosening`, `editorial-semantic`, `editorial-whitespace`, `additive-unaudited`,
  `additive-reaudited` and `no-policy`, beside the existing `below-risk` and `owner-cause` plants
  (`RISK_PLANTS`, :867-868), now read under `by-risk` from their policy file. Observed by AC1 to AC7.

## 3. Non-goals (OUT)

- No refusing gate: `deviation.gate` and the leg's exit are dScopedBuild's; the host still runs
  `report`.
- No classifier: `derive_change_mark` and its spelling map are dOrderedCharter-33's, called and never
  re-specced.
- No change to the record grammar or the risk vocabulary (`RISKS`, :150).
- No write to the chain's records: a record graded under the new terms and found short is listed for
  its writer under `report`.
- No edit of the frozen instrument `deviations.py`, which grades `author-recorded` only (packet,
  Non-goals).
- No help page: no page under `help/` describes the deviation join; `tools/memory-tree/README.md`'s row
  (:27) gains the key.

### Edges

none

## 4. Design

### The approver, by value

| Value | Least approver | Extra terms |
|---|---|---|
| `by-risk` | `LEAST[risk]` (:153-154), the owner when the cause is an owner ruling (:713) | S4's classifier on an `editorial` claim; S5's re-audit on a spec writer's `additive` or `stricter` |
| `owner-all` | the owner, for every record | none |
| `author-recorded` | any role the grammar names | none |

Every value keeps the two refusals the join already makes: an approver opening with no role (:709-711),
and an owner approval citing no held decision row naming the departure (:719-733).

### Where the value comes from

```
read_approval(root, rev) -> (value, source)
  the policy kit resolves  -> resolve("deviation.approval", root, rev): the file's value or the catalogue default
  it does not resolve      -> ("by-risk", "default — the policy kit is not installed")
```

`render_lines` prints `approval <value> (<source>)` in its summary line (:798), so a reader sees which
value graded the records and why.

### Inventory

| Minted | Kind |
|---|---|
| `owner-all` | `APPROVALS` member |
| `read_approval`, `check_reaudit` | functions, `tools/memory-tree/deviation_join.py` |
| the eight plants of S8 | fixture plant names |

Each function name is put to `python tools/lexicon/lexicon.py --suggest <name> --as py.function` in
the build pass.

### Migration

None for records. A caller passing `--approval` is refused by the argument parser, naming the key that
replaced it.

### Rollout

Live at landing. The chain's host keeps `author-recorded`, so no chain landing's report moves; a
non-chain caller reads `by-risk` by default, which grades the records a chain-free repository writes.

### Files touched (estimate)

- `tools/memory-tree/deviation_join.py`
- `tools/memory-tree/README.md`: the module's row (:27)
- `tools/memory-tree/HYGIENE.template.md` and its render `memory/HYGIENE.md`: the approval sentence of
  "Record bindings" (`memory/HYGIENE.md:677-681`), which names two values and the old default

### Alternatives rejected

- **The host reads the key too.** Gov's catalogue default is `by-risk`, and the owner ruled the chain
  runs `author-recorded` (`PLAY-dClosedLoop-4`); the guarded policy file is the owner's to set, so the
  host keeps the ruling as its override until the chain closes.
- **The typed risk kept for editorial.** The clause names the classifier; a typed `editorial` is the
  actor-typed claim the classifier exists to check.

## 5. Production-readiness checklist

- security — no new write; the approval value comes from the guarded policy file at the landed
  revision, never from a flag a run can pass.
- perf / scale — one policy read per run and one classifier call per `editorial` record.
- error / empty / loading states — no policy file reads the default and says so; an unknown value
  refuses by key; an absent classifier keeps the typed risk and says so.
- observability — the summary line names the value and its source.
- risks — records that passed `by-risk` with a typed `editorial` may now be refused; under the host's
  `report` they are listed, never blocking.
- testing — the plants of S8, run by the pass; the self-test arm in §7 at the close.
- migration — none.
- user docs — the kit README row and the hygiene guide's binding section.

## 6. Acceptance criteria

- **AC1** — When `python tools/memory-tree/deviation_join.py --fixture --plant below-risk --policy refuse`
  runs, the fixture's policy file setting `by-risk`, it exits 1 naming the approver below `owner`; with
  `--approval by-risk` added it is refused by the argument parser.
  Red when: the value is still read from the flag, so the plant's policy file grades nothing.
- **AC2** — When the plants `owner-all-author` and `owner-all-cited` run under `--policy refuse`, the
  first exits 1 naming the author below `owner` under `owner-all`, and the second, an owner approval
  citing a held decision row naming its clause, exits 0.
  Red when: `owner-all` is read as `by-risk`, so an author approving an editorial record passes.
- **AC3** — When the plant `editorial-semantic` runs under `--policy refuse`, a record typed `editorial`
  whose `Before` and `After` differ by a word, approved by its author, exits 1 naming the record and the
  first differing word.
  Red when: the typed risk is trusted, so the author's approval passes.
- **AC4** — When the plant `editorial-whitespace` runs, a record typed `editorial` whose texts differ
  only in whitespace, approved by its author, exits 0.
  Red when: every editorial claim is refused, so the author route never passes.
- **AC5** — When the plant `additive-unaudited` runs, a spec writer's approval of an `additive` record
  departing `FIX-dApproval-1@rev-2`, with no spec-audit pin past rev-2, exits 1 naming the re-audit.
  Red when: the spec writer's role alone satisfies `LEAST`, so an unaudited change passes.
- **AC6** — When the plant `additive-reaudited` adds a spec-audit record pinning `FIX-dApproval-1@rev-3`,
  the same approval exits 0.
  Red when: the re-audit term reads any pin at all, so the old revision's audit satisfies it.
- **AC7** — When the plant `author-recorded-loosening` runs, a loosening approved by its author exits 0
  under `author-recorded`; when `no-policy` runs, the summary line reads `approval by-risk` with its
  source; and when `python tools/memory-tree/deviation_join.py --fixture --host routed-commits` runs over
  a fixture whose policy file sets `by-risk`, the host's lines read `approval author-recorded`.
  Red when: the host reads the key, so the chain's ruled value is replaced by the catalogue default.

## 7. Gates

`build-index selftest` · `routed-commits selftest` · `routed commits name a specced unit` · `kit/dogfood doc parity` · `recall floor` · `recall floor arms` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/memory-tree/routed_commits.py · covers AC1 AC2 AC3 AC4 AC5 AC6 AC7 · the `routed-commits selftest` leg, whose self-test runs `deviation_join.run_plant_arms` (`tools/memory-tree/routed_commits.py:660-670`), over the S8 plants against the base join, which reads the value from `--approval`, has no `owner-all`, trusts a typed editorial risk and asks no re-audit · none

## 8. Open questions

- **FACT-QUESTION · F1 — The brief gives this spec's status header the token `DRAFT`; is that a
  legal status?** Probe: `STATUS_TOKENS` at `tools/memory-tree/tree_lib.py:28`. Observation,
  2026-10-24: `DRAFT` is not in the tuple. Liveness: the tuple would list it if the vocabulary admitted
  it. RESOLVED (agent, 2026-10-24, delegated): `OPEN`.
- **F2 — Does the leg's host read `deviation.approval`?** Options: (a) the host keeps the chain's
  ruled `author-recorded` as an override, every other caller reading the key; (b) the host reads the
  key, its value `by-risk` until the owner sets the file; (c) the host reads the key and gov's policy
  file is written to `author-recorded` in this unit. (b) replaces the owner's ruling with a default;
  (c) is an agent write to the guarded file, which veto 3 discards. RESOLVED (agent, 2026-10-24,
  delegated): (a), by rung 1, the owner's ruling `PLAY-dClosedLoop-4`. widens: none. relaxes: none.
- **F3 — How is a typed `editorial` record graded when the classifier reads it semantic?** Options:
  (a) refused, naming the first differing word; (b) re-graded as `additive`. (b) guesses a risk the
  classifier does not state, and a loosening would then pass a spec writer. RESOLVED (agent,
  2026-10-24, delegated): (a), by rung 3. widens: none. relaxes: none.
- **F4 — Which revision does the re-audit read for a clause departure?** Options: (a) the spec carrying
  the clause, through `design_lib.scan_chain_specs`, pinned past the revision that first carried the
  change; (b) re-audit graded on spec-revision departures only. (b) leaves a clause departure's spec
  writer approval with no term, and the clause names both. RESOLVED (agent, 2026-10-24, delegated):
  (a), by rung 3.
- **F5 — Re-wording the approval sentence of `memory/HYGIENE.md` (:677-681), which says the approver
  is graded under one of two values with `author-recorded` the default, changes a governance carrier;
  does the build's grant cover it?** The clause moves the value into `deviation.approval` with three
  values, so the sentence goes stale in this unit. RESOLVED (agent, 2026-10-24, delegated): covered,
  rung 3.
  grants: PLAY-dClosedLoop-3 the approval sentence of tools/memory-tree/HYGIENE.template.md and its render memory/HYGIENE.md re-worded to the key and its three values

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, from the packet's Items 34, v2:1293, final-questions FQ-3 and
  `check_approver` read at base `ed497191`.

## 10. Reuse audit

The seam extended is the deviation join's approver check, `check_approver`
(`tools/memory-tree/deviation_join.py:705-733`), with its `APPROVALS`, `RISKS`, `RANK` and `LEAST`
tables (:143-154) and the audit pins it already reads (:562-576); the classifier is dOrderedCharter-33
S1's and the policy read dGroundRules-2's. `python tools/codebase-map/reuse_lookup.py "grade a deviation approver by risk from a policy value"`
ranked `load_policy` in `tools/roles/roles_lib.py`, the roles kit's effort file, which reads no policy
key and is no seam here, and no approver grader outside the join. `python tools/memory-recall/query.py`
returned scout C's row, the night pass instruments' catalogue row for the key and the brief's row;
scout C cites `APPROVALS` at :143 and the host's `author-recorded` at :144, which agree with source at
base.

Recall terms used: deviation approval by-risk owner-all author-recorded check_approver editorial classifier re-audit spec writer
