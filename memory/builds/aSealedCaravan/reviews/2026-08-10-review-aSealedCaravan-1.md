# Review 1 — Tier-2 pass over both aSealedCaravan specs

**Targets:** `memory/builds/aSealedCaravan/spec/2026-08-10-spec-TOOL-aSealedCaravan-1.md` and
`memory/builds/aSealedCaravan/spec/2026-08-10-spec-DEPL-aSealedCaravan-2.md`, both at rev-1, both
grounded on base `16aeb5ef`, before any code.

**Method:** five primed lenses over the pair — is each scope item buildable as written, does every
measured number in the spec reproduce against the tree, does each acceptance criterion observe the
thing its scope item claims, does the data model carry the state the measured adopters actually
produce, and does the declared gate suite absorb what the unit adds — then a default-refute
verification pass in five verifier batches, each verdict required to reproduce against the file or
the running tree at base.

**Result:** 77 raw findings, **48 confirmed**, 29 refuted, 0 unverified. Precision 0.62, above the
0.5 floor `memory/guides/REVIEW-PROTOCOL.md:89` sets for adding agents rather than tightening scope.
The protocol's ≤5-agent verify budget was respected: five batches over five agents total.

**Severity split:** 6 blockers, 23 high, 17 medium, 2 low. **20 land on `TOOL-aSealedCaravan-1`, 28
on `DEPL-aSealedCaravan-2`.**

---

## How to read this report

- Ids are the raw ids from the verification pass, so they are sparse. `TOOL:N` and `DEPL:N` are line
  numbers in the named spec at rev-1.
- Every row names the section the correction lands in and the concrete edit. The prose sections
  below expand the blockers and the recurring structural clusters; the tables are complete on their
  own.
- **Overlap clusters.** Several findings are the same defect measured by different verifiers. They
  are kept separate because each adds a distinct correction, but they are one edit each:

| Cluster | Ids | One edit |
|---|---|---|
| The S8 predicate is unmeasured | 1, 46 | Run the grep, paste the per-file table, re-cost commit 3 |
| AC9 is green before the work | 6, 14 | Anchor AC9 on text that exists at base |
| The playbook is inside S8's surface and outside its cost table | 50, 57 | Add three Files-touched rows plus the byte budget |
| `REVIEW-PROTOCOL.template.md` is converted by nobody | 47, 58 | Name it in S4/Files-touched, delete `norm()` rather than invert it |
| "41 legs after S8" | 5, 49 | 42, and both script paths cited in the charter |
| AC5's "exactly three work orders" | 4, 21, 38 | Derive the outbox from the selected kits' `[[hole]]` set |
| The `kit.toml` population is undefined | 8, 23, 53, 70 | Define "shipped kit" as a tracked registry, assert both directions |
| An unfilled `map_extractors.py` blocks adoption | 33, 45 | `blocks_adopt` plus an `apply --resume` phase |

**Measurements re-run at review time, at base `16aeb5ef`:** `tools/gate-legs.json` = 40 legs;
`parallel-coding-governance.template.md` = 32688 of 32768 bytes; `ls -d tools/*/` = 10 directories;
`grep -n 'adopt-codebase-map.sh refuses' AGENTS.md` exits 1; the AC1 predicate over S8's declared
surface (99 tracked files) fires **95 times across 37 files**; `drift_report.py --check` is already
red on this branch at `non_terminal_specs_cited_by_product_source = 3` against pin 2.

---

## TOOL-aSealedCaravan-1 — 20 findings

### Blockers (3)

| # | Where | Section | Claim | Concrete edit |
|---|---|---|---|---|
| 46 | `TOOL:126` | §4 The enforcement gate | "Two waivers are declared rather than discovered" and "this repo's own internal references are already `tools/`-prefixed and therefore pass unchanged" are both measurably false — the AC1 predicate over S8's own declared surface hits 37 tracked files and 95 lines at base. After every S1-S11 edit lands (8 of those files), ~28 files and ~63 lines still spell a root-install kit path, covered by neither an S-item nor the two declared waivers. | Run the predicate before writing the cost table — the spec's own recorded trap. Then either narrow S8's surface to files an adopter receives verbatim (excluding `*.test.sh`, `*selftest.py` and `.conf.example` fixtures) or enumerate the real waiver registry in §4 with its measured seed count, pinned shrink-only. Re-cost Files touched from the measured population. |
| 57 | `TOOL:120` | §4 The enforcement gate → §4 Files touched | S8's shipped surface explicitly includes "the playbook with its two companions", but the spec never lists them among the files it changes and never reckons with the 80-byte template budget they sit under. AC2 ("exits 0 on the tree as landed") is unsatisfiable without editing them. `.customize.md:40` additionally declares the *opposite* default from S1 in shipped prose. | Add `parallel-coding-governance.template.md`, `.customize.md` and `.domain-rules.md` to the Files-touched table; state the byte cost against `tools/check-template-size.sh` (32688/32768 today) and where it is paid from; add the `.customize.md:40` root-prefix default to the S11 stale-records list. |
| 14 | `TOOL:241` | §6 AC9 (covers S11) | AC9's first arm is already green: `grep -n 'adopt-codebase-map.sh refuses' AGENTS.md` returns nothing today (measured, exit 1) because `AGENTS.md:94` reads "so `adopt-codebase-map.sh` refuses" with a closing backtick between the two words. The pattern spans a backtick and can never match, before or after the work. | Assert on text that exists — e.g. `grep -n 'non-canonical \`tools/\` prefix' AGENTS.md` returns nothing — and give each of the five records S11 claims its own named assertion rather than one grep standing in for all of them. |

### High (7)

| # | Where | Section | Claim | Concrete edit |
|---|---|---|---|---|
| 1 | `TOOL:126` | §4 The enforcement gate, §6 AC1 | The largest hit populations are fixtures that build a ROOT-prefix install on purpose to prove the dual-prefix support the unit keeps by non-goal: `tools/drift-audit/selftest.py` (10), `tools/check-wiring.test.sh` (6, it derives both spellings), `tools/codebase-map/adopt-codebase-map.test.sh` (2, incl. the deliberate `DEFAULT_MDC='python codebase-map/map_diff.py'`), plus 4 in the playbook where `memory-tree/` names the KIT, not a path. The builder discovers a ~35-line waiver registry mid-commit-3, or reds the bar. | Paste the per-file hit table into §4 and narrow the predicate to exclude test/selftest fixtures and kit-NAME references. Also fix AC1's wording: the regex's leading `[^/[:alnum:]._-]` class means a hit can never be `tools/`-prefixed, so "either `tools/`-prefixed or waived" reduces to "waived". |
| 3 | `TOOL:230` | §6 AC4 (covers S5) | "Today it exits 0 over seven such citations" does not reproduce. The seven are `HYGIENE.template.md` lines 11, 20, 98, 123, 161, 209, 233, but `corpus_ids.py:52` is `BACKTICKED = re.compile(r"\`([^\`\s]+)\`")` — lines 123 and 209 carry a space inside the backticks and lines 20 and 233 are unbackticked. Only 3 occurrences (2 distinct paths) are in a shape check 15 can ever see. | Restate AC4 against a fixture the spec builds (scaffold at a `tools/` prefix, assert `corpus_ids.py --check` names the citation) and correct the count to "the 3 of 7 that are single-token backticked citations; the remaining 4 are closed by S4, not S5". The S5 fixture must use a whitespace-free backticked token or it will never fire. |
| 18 | `TOOL:234` | §6 AC6 (covers S7) | AC6 is phrased as a negative a chatty no-op satisfies: "does not exit 0 with all three legs *silently* skipped" is met by adding three `echo` lines to `.githooks/pre-commit:26,32,37` while the hook still exits 0 with every leg unrun — which violates S7's "a guard that finds no kit where a kit IS installed fails". | Restate positively: "When `.githooks/pre-commit` runs in a repo where a kit IS installed but not at the literal guarded path, it exits non-zero and names each guarded path it could not resolve." Add the counterpart arm: "in a repo with no kit at all, it exits 0 and names each leg it skipped." |
| 19 | `TOOL:20` | §2 S2, §6 AC1/AC10 | S2's `manifest-check.sh` move (`scripts/` → `tools/manifest-check.sh`, prescribed at `WIRE-INTO-PROJECT.md:303`) has no acceptance coverage: AC1's alternation lists only `memory-tree\|memory-recall\|codebase-map\|drift-audit\|workflows`, and AC10 enumerates only the four kit dirs. The one scope item that is also an open fork (F1) is the one nothing observes. | Add `scripts/` to the S8 predicate's alternation, and add an AC: in the fixture, the runbook's manifest step writes `tools/manifest-check.sh`, the kickoff skill's fallback chain resolves it, and no shipped file spells `scripts/manifest-check.sh` outside the waiver registry. |
| 47 | `TOOL:144` | §4 Migration, §2 S4, §6 AC8 | `tools/workflows/REVIEW-PROTOCOL.template.md` carries 4 root-relative `workflows/…` lines (26, 37, 41, 85) and is inside S8's surface twice over (`tools/**` and `*.template.*`), but no S-item converts it — S4 names only `HYGIENE.template.md` and `SPEC-TEMPLATE.template.md`. Commit 3 is red either way. | Extend S4 to a third file, or add it to the S8 waiver registry with the reason and drop the `check-protocol-parity.test.sh` `norm()` change from §4/§7. Add an AC for whichever is chosen — AC8 currently covers only kit-dogfood-parity. |
| 58 | `TOOL:144` | §4 Migration, §4 Files touched | The S4 remedy (a placeholder the adopter substitutes) has no substitution point in the workflows kit, which ships no adopter and no render step. The live copy is already `tools/`-prefixed and `check-protocol-parity.test.sh:36` strips `tools/` from the LIVE side only, so once S8 forces the SHIPPED side to `tools/workflows/…` the comparison **inverts** and the leg reds over correct content. The file is absent from the Files-touched Templates row (3 listed) and the fix and the gate change land in different commits. | Name `REVIEW-PROTOCOL.template.md` (5 sites) in Files touched. With one declared prefix the shipped and live copies are byte-identical, so delete `PREFIX`/`TOOLROOT` derivation and the `norm()` substitution outright (CR-strip only) rather than inverting it, and land it with the template edit in one commit, as the spec already requires for S4. |
| 59 | `TOOL:219` | §6 AC1, §4 Files touched | AC1/S8's ban omits `scripts/`, so nothing mechanically enforces the S2 half of the declaration, and the three shipped files that prescribe `scripts/` are missing from Files touched: `skills/session-kickoff/MANIFEST-TEMPLATE.md:8,76` and `skills/session-kickoff/SKILL.md:90,183`. The same skill ships `SKILL.md:58` `python codebase-map/map_diff.py` (which AC1 *does* match) and `:149`'s dual-spelling hedge, yet no `skills/**` file appears anywhere in the table. | Add `scripts/` to the S8 predicate and AC1's alternation; add `skills/session-kickoff/MANIFEST-TEMPLATE.md` (2 sites) and `skills/session-kickoff/SKILL.md` (4 sites) to Files touched. The runbook's `scripts/manifest-check.sh` references are not the only copies. |

### Medium (10)

| # | Where | Section | Claim | Concrete edit |
|---|---|---|---|---|
| 49 | `TOOL:249` | §7 Gates | "40 legs today, 41 after S8" is wrong: S8 adds a gate AND its self-test, and §4:118 and §7 both say so. Every comparable gate in `tools/gate-legs.json` carries its self-test as a separate leg (verdict-epoch 5/6, manifest-check 2/8, check-arms 18/19, review-join 27/29, fan-out 24/25). Correct is 42. | Correct to "40 legs today, 42 after S8", and change the drift-audit obligation to name **both** `tools/check-install-prefix.sh` and `tools/check-install-prefix.test.sh` as required charter citations. |
| 5 | `TOOL:249` | §7 Gates | The zero-slack claim on the next line is computed against the wrong number. Measured: `handkept_inventories_disagreeing_with_source = 7 of 40`, pin 7, tolerance 0, and its own comment records that all 7 current misses are SELF-TESTS whose parent gate is cited — exactly the class a builder following "leg 41 uncited reds immediately" forgets. | Restate as "legs 41 and 42 uncited push the pin to 9 against a ceiling of 7". Both new script paths must land in `AGENTS.md`'s gate-suite section in the same commit and both must be claimed in a codebase-map dossier. |
| 6 | `TOOL:241` | §6 AC9 | Duplicate of blocker 14 at medium severity: AC9's first arm passes before any work is done, so a builder can skip the S11 correction and still show AC9 green. The second clause is real — `memory/backlog/TOOL.md:21` reads INPROGRESS today. | Anchor AC9 on a pattern that matches at base and record the base-state count (1) alongside the post-state (0). |
| 26 | `TOOL:49` | §2 S11, §4 | S11 points at "the five stale records listed in section 4", but §4 contains no such list — its sub-heads are Inventory, the four silent-green failures, the enforcement gate, Migration, Rollout, Files touched, the fourteen runbook corrections and Alternatives rejected. The Files-touched Records row names four items, not five, and two of them (the `check-wiring.sh` header, the map dossier) have no AC at all. | Add a five-row table to §4 (record, current text, why stale, correction) and give AC9 one assertion per row, each a runnable grep against text that exists today. |
| 50 | `TOOL:162` | §4 Files touched, §7 | The Files-touched table has no row for the playbook or its two companions, yet §4:120 puts them inside S8's predicate surface and they carry 7 root-relative hits (template 105, 106, 107, 148; customize 40, 56, 57). §7 does not name `template size ≤32KiB` as a leg this unit touches. | Add the row, add `tools/check-template-size.sh` to §7 with the measured headroom, and state whether the four playbook hits are edited or waived — `:105`'s "(`memory-tree/` kit)" reads as a kit NAME and is a waiver candidate. |
| 52 | `TOOL:168` | §4 Files touched, §7 | The Records row omits `.claude/SESSION-KICKOFF.md` and §7 omits the `drift-audit records` leg. Measured on this branch, `drift_report.py --check` already exits 1: `non_terminal_specs_cited_by_product_source = 3` against shrink-only pin 2, because `.claude/SESSION-KICKOFF.md:90,95` cite `TOOL-aRootedPrefix-1`, whose spec header reads INPROGRESS. That citation is new in this planning session — absent at `16aeb5ef`. The bar is red before commit 1. | Add `.claude/SESSION-KICKOFF.md` to the Records row (its own note says "prune when AGENTS.md:94 is rewritten", so it belongs in commit 1 with S11), add `drift-audit records` to §7, and extend AC9 to assert `drift_report.py --check` exits 0 after commit 1. AC9's backlog-row clause does not drain it: the signal reads the SPEC's status header. |
| 60 | `TOOL:130` | §4 The enforcement gate | The S8 waiver registry is placed "in the gate's own directory" under `tools/`, outside the only ratchet that watches waiver lists here. `drift_signals.py` `SHRINK_ONLY` enumerates exactly four `memory/project/*.txt` paths, and its header records that the prior "this repo ships no waiver list of its own" claim was false when written. A registry under `tools/` is a fifth list no signal grades. | Put the registry at `memory/project/install-prefix-waiver.txt` (hygiene check 3 admits any `*.txt` there) and add it to `SHRINK_ONLY` with its seed measurement — or state in §4 why it is exempt. `DECLARED_EMPTY`'s own rule is that an unenumerated exemption is not an exemption. |
| 7 | `TOOL:60` | §3 Non-goals, §4 Alternatives rejected (`TOOL:191`) | `TOOL-aRootedPrefix-1b` says nothing about a `KIT_DIR` key. `memory/archive/DECISIONS.2026-08-10.md:81` records a `--converge`/`collision_flags` measurement at a mis-rooted install. An owner who opens the citation finds it does not say what is claimed, and it is the strongest structural non-goal in the unit. | Re-cite both `TOOL:60` and `TOOL:191` to `TOOL-aRootedPrefix-1` ("resolve_root walks up for the conf, bounded by `.git`") and `-1c` ("Resolution answers WHERE; require_adopted_root answers WHETHER"), or state plainly that no prior record refused a `KIT_DIR` key and this unit is the first to. |
| 9 | `TOOL:181` | §4 The fourteen runbook corrections (S10) | gate-lint is not a gate-legged kit: `tools/gate-legs.json` has no gate-lint entry and `tools/gate-lint/README.md` states "This kit has no gate legs of its own — the consuming project does". Writing a runbook section that claims otherwise ships a new false claim into the artifact whose purpose is to stop shipping false claims. drift-audit (legs 37/38/39) and check-kit-versions (leg 4) do check out. | Reword to "three shipped kits (drift-audit and check-kit-versions, both gate-legged; gate-lint, whose README hands leg wiring to the consuming project) and the row-keyed merge driver appear nowhere", and have the runbook state gate-lint's wiring as an adopter step. |
| 63 | `TOOL:277` | §8 F3 | F3's recommendation to ship `pyrun.sh` + `resolve-python.sh` "as part of the memory-tree kit" puts `pyrun.sh` in the exact case its own header excludes: it sources the canonical resolver *because* `../lib/` is reachable, and states that "a kit copy-installed as a standalone directory … carries the inline block instead — that is the case the marker is for, and this is not it." Relocated, it needs a fourth verbatim resolver copy in one kit, auto-enrolled in a parity population whose exclusion is anchored `^tools/lib/resolve-python`. S9's "delivered by the runbook" and F3 are two different installs. | Pick one and state the mechanics: deliver `tools/lib/` as a directory the runbook copies (S9's wording, parity exclusion intact), or, if the files move into the kit, say how `pyrun.sh` finds its sibling and widen the parity/idiom-ban exclusion pattern in the same change. |

### Blockers in full

#### 46 and 1 — the S8 predicate was never run over the tree it gates

§4 states two things about the enforcement gate and both are false at base. "This repo's own internal
references are already `tools/`-prefixed and therefore pass unchanged" and "two waivers are declared
rather than discovered" are contradicted by running the spec's own AC1 predicate over the spec's own
declared surface. I re-ran it at review time: `git ls-files` over `tools/**`, `skills/**`,
`*.template.*`, `*.fragment.json`, `.githooks/**` and the playbook plus companions is 99 tracked
files, and the predicate fires **95 times across 37 files**.

The shape of the miss matters more than the count. The largest populations are fixtures that build a
root-prefix install *on purpose*, to prove the dual-prefix support this unit keeps by non-goal:
`tools/drift-audit/selftest.py` constructs its throwaway repo at `drift-audit/` and invokes
`drift-audit/drift_report.py` (10 hits); `tools/check-wiring.test.sh` derives both spellings (6);
`tools/codebase-map/adopt-codebase-map.test.sh:133` carries `DEFAULT_MDC='python
codebase-map/map_diff.py'` as a `gov:literal-python` conf VALUE (2); `skills/session-kickoff/
SKILL.md:148-149` deliberately names both spellings ("both spellings ship, so resolve it rather than
assuming"). 27 of the 95 sit in test files. `tools/memory-tree/gen_build_index.py:42` is a
different hazard again: its `GEN_HEADER` string is verbatim line 1 of `memory/LIVE.md` and every
`memory/ledger/*.md` shard, so changing it forces a regenerate and a `KIT_MEMORY_TREE_VERSION` bump.

The spec anticipates predicate *correctness* — "per the recorded trap, the predicate is run over the
real tree BEFORE it is trusted" — but the design it then states is the sizing, and the sizing is
what the measurement falsifies. Files touched budgets ~20 files against a gate that touches 37, and
after every declared S1-S11 edit lands (8 of those files) roughly 28 files and 63 lines still spell a
root-install kit path with no S-item and no waiver. Commit 3 cannot be green as scoped.

**Correction.** Run the grep at spec time and paste the per-file hit table into §4. Then choose
explicitly: narrow S8's surface to files an adopter receives verbatim — excluding `*.test.sh`,
`*selftest.py` and `.conf.example` fixtures, and excluding references where the token names the KIT
rather than an install path — or declare the real waiver registry with its measured seed count,
pinned shrink-only. Re-cost Files touched from the measured population. Separately, AC1's wording is
self-defeating: the regex's leading `[^/[:alnum:]._-]` class means a hit can never be `tools/`-
prefixed, so "either `tools/`-prefixed or waived" reduces to "waived".

#### 57 and 50 — the playbook is inside the gate's surface and outside its cost table

§4:120 puts "the playbook with its two companions" inside S8's predicate surface. Neither
`parallel-coding-governance.template.md` nor `.customize.md` nor `.domain-rules.md` appears in any
row of Files touched, and §7 does not list `template size ≤32KiB` among the legs this unit moves.

Measured: the template carries four root-relative kit-path sites (`:105` `memory-tree/`, `:106`
`codebase-map/`, `:107` `memory-recall/`, `:148` `workflows/tier2-review.js`) and `.customize.md`
carries three (`:40`, `:56`, `:57`). AC2 — "exits 0 on the tree as landed" — is therefore
unsatisfiable without editing them. The template measures **32688 of 32768 bytes**: 80 bytes of
headroom under a limit `AGENTS.md` forbids raising. Four `tools/` insertions cost ~24 of those 80,
leaving 56, and a single further sentence of prose in the same commit reds the gate.

`.customize.md:40` is the sharper half. It reads "`<kit-dir>` is wherever the kit was installed
(`memory-tree/` at the project root by default)" — a shipped prose declaration of exactly the
opposite default from S1, in the deploy-time placeholder catalog an adopter reads. That is a stale
record and belongs in S11's list.

**Correction.** Add all three files to Files touched with their site counts; add
`tools/check-template-size.sh` to §7 with the measured headroom and say where the ~24 bytes are paid
from; add `.customize.md:40` to the S11 stale-records list. Decide and state whether `:105`'s
"(`memory-tree/` kit)" is edited or waived — it reads as a kit name, not a path.

#### 14 and 6 — AC9 is green before the change is made

`grep -n 'adopt-codebase-map.sh refuses' AGENTS.md` exits 1 today. I reproduced it: `AGENTS.md:94`
reads "so `adopt-codebase-map.sh` refuses", with a closing backtick between the two words, so the
pattern spans a backtick and can never match. AC9's first arm returns nothing whether or not the
stale line is corrected.

S11 is the scope item whose entire content is correcting stale records, and AC9 is the only AC
covering it. With the first arm vacuous, the second arm — `memory/backlog/TOOL.md`'s
`TOOL-aRootedPrefix-1` row reading CLOSED, genuinely INPROGRESS at `:21` today — is the only
executable assertion, covering 1 of the 5 records S11 claims. Four stale records land with no
acceptance coverage at all. In a repo whose thesis is that a guard which cannot fire is worse than no
guard, a green-by-absence AC is a defect on its own terms.

**Correction.** Assert on text that exists: `grep -n 'non-canonical \`tools/\` prefix' AGENTS.md`
returns nothing, or grep the whole codebase-map bullet. Then enumerate the five records in §4 (see
finding 26) and give each its own named assertion, each a runnable grep with the base-state count
recorded alongside the post-state.

---

## DEPL-aSealedCaravan-2 — 28 findings

### Blockers (3)

| # | Where | Section | Claim | Concrete edit |
|---|---|---|---|---|
| 33 | `DEPL:37` | §2 S8, §4 Inventory, §6 AC1 | The `map_extractors.py` hole cannot be represented as "an unfilled template plus an outbox order" — an unfilled template makes the codebase-map adopter FAIL, so the kit never lands. `map_extractors.template.py:112-117` raises `MapError` on an empty `EXTRACTORS` dict and `gen_map.py:38` calls `inventory_ids()` at MODULE level, so `adopt-codebase-map.sh` exits 1 at `:191` with no MAP_ROOT tree, no baseline and no GATE_FILE. codebase-map is in the S6 default set. | Give `[[hole]]` a `blocks_adopt = true` flag and split `apply` into a land-and-configure phase and a resume phase: blocked kits get files copied and a work order written, with `[adopt] argv` deferred to `govkit apply --resume`. `check` must distinguish three states — not landed, landed but inert, adopted. Scope AC1's "every gate leg exits 0" to the non-blocked kits. |
| 45 | `DEPL:240` | §6 AC1 (with S6, S8) | AC1 has no satisfying assignment. `test_codebase_map.template.py:70` binds `INVENTORY_IDS = ext.inventory_ids()` at module scope too, so the installed gate cannot even import. `apply` of the DEFAULT kit set can never reach a green fixture, AC2's apply-twice-changed-zero has no green baseline to compare against, and commit 3 lands with its own acceptance matrix red. This also falsifies §4's claim that codebase-map is "the counter-example worth copying" for the unattended path. | Split AC1: assert exit 0 only for gate legs of kits with no `authoring` hole; add an explicit AC that the codebase-map leg is RED-by-design until its outbox order is discharged, then green after a fixture `map_extractors.py` is filled. Correct the §4 inventory row ("Idempotent: yes, reconverges" is not reachable on a fresh tree) and give codebase-map an `[exit_codes] 1 = "seed-and-stop"` entry. |
| 32 | `DEPL:120` | §4 Data model, `[exit_codes]` | The `[exit_codes]` map is keyed per KIT, but the exit-1 collision is per BRANCH inside one adopter. `adopt-codebase-map.sh` alone exits 1 for six unrelated outcomes: `:52` identity refusal (nothing written), `:98/:101/:113` prefix refusals (explicitly "BEFORE anything is written"), `:150` seed conf, `:184` seed extractors, `:189/:191` gen_map crash with a half-written map tree, `:212` gate FAILED with conf + map tree + GATE_FILE all on disk. `adopt-memory-tree.sh` exits 1 at `:23` (seed) and `:35` (refuse to overwrite a foreign `memory/`) — and the spec's own example declares memory-tree as `1 = "seed-and-stop"`, which mis-reads `:35`. | Replace the code→meaning table with a code+effect table: each outcome declares a probe the deployer RUNS (`must_exist` / `must_not_exist` path, e.g. GATE_FILE for codebase-map), so the classification is measured, not asserted — the same "claim nothing until it is read back" rule `adopt-codebase-map.sh:137-139` already states. Alternatively scope in assigning distinct exit codes to every refusal branch and gate it — but then say so, because §4 Alternatives rejected forbids touching the adopters. |

### High (16)

| # | Where | Section | Claim | Concrete edit |
|---|---|---|---|---|
| 2 | `DEPL:69` | §4 Where it lives, §8 F1 | `check-arms.py` is NOT scoped to `tools/**` — `check-arms.py:116` reads `[p for p in git ls-files if p.endswith('.sh')]`, a repo-wide population, and `--report` discovers `skills/session-kickoff/manifest-check.sh`. A `deploy/*.sh` would be inside it, and `deploy/govkit.py` outside it either way since it scans `*.sh` only. The spec contradicts itself at F3 (`DEPL:292`), which states the scan correctly. One third of the location measurement behind fork F1 is false, and F1 is the departure the owner must ratify. | Drop `check-arms.py` from the §4 list and restate the argument on the gates that do hold: `check-review-join.sh:44` (`grep -E '^tools/.*\.js$'`), `check-workflow-syntax.js:38` (`p.startsWith('tools/')`), `map_extractors._tool_kits()` and the drift-audit product globs. |
| 38 | `DEPL:250` | §6 AC5 (covers S8) | AC5's "exactly three work orders" is contradicted by the spec's own §4 inventory table and its own example `kit.toml`. drift-audit is not in the S6 default set, so `drift_signals.py` cannot be one of the three; meanwhile §4:144 gives memory-tree "taxonomy, measured pins", §4:149 gives the manifest ratchet "manifest section B", and the example descriptor at `:113-117` literally declares `[[hole]] id = "measured-pins"`. The shipped memory-tree descriptor would red AC5 on its first run. | Derive the expected outbox from the union of `[[hole]]` blocks over the SELECTED kits and assert that set by id, never a literal count: "the outbox holds exactly one order per declared hole of each selected kit, and `check` exits non-zero until each is discharged." Name the default set's expected id list in the matrix fixture, not in the criterion. |
| 4 | `DEPL:250` | §6 AC5, §2 S8 | Same contradiction from the completeness side: the default set has at least four holes, not three, and `check` would report a target complete while its pins are inherited-vacuous — the exact failure S8 exists to prevent. Both holes are confirmed authoring work in source (`adopt-memory-tree.sh:159` "MEASURE any pin/floor this kit gains against YOUR corpus"; `HYGIENE.template.md:162`; `MANIFEST-TEMPLATE.md:52` "§B — Orientation (derived at instantiation)"). | Reconcile S8 with the table: enumerate the default set's holes as playbook placeholders, manifest §B, memory-tree taxonomy + measured pins, and `map_extractors.py`; move `drift_signals.py` to the `--all` case. |
| 21 | `DEPL:250` | §6 AC5 | AC5 is self-contradictory on its face — "exactly three work orders … and, if drift-audit was selected" under a stated precondition ("when the default set is applied") that excludes drift-audit. The count is AC5's only observable, so the builder must guess which of S8, the §4 table and AC5 is authoritative. | Same edit as 38. Additionally state why memory-tree's and the manifest's holes are or are not outbox orders — silence is what makes the three readings possible. |
| 23 | `DEPL:257` | §6 AC8, §2 S2, §4 Files touched | AC8 quantifies over an undefined population. `tools/` holds ten directories; §4's table lists eight rows; Files touched budgets eight descriptors. `tools/gate-lint/` and `tools/lib/` are in neither, pytest-parallel-guardrails is selectable under `--all` with no row and no descriptor, and the playbook has no directory at all, so S2's "a `kit.toml` in each shipped kit directory" has nowhere to put its descriptor. `selfcheck` is rollout commit 1 and the gate for the whole descriptor layer. | Name an explicit kit registry file as the population and assert both directions: every entry has a descriptor, and every `tools/*` directory is either an entry or listed as not-a-kit with a reason. Say where the playbook's descriptor lives. Resolve TOOL F3 for `tools/lib/` before AC8 can be run. |
| 70 | `DEPL:257` | §6 AC8, §4 Files touched | No measurable population in this repo equals 8, and two members of the only one that exists are undeployable: `tools/gate-lint/` has no adopter, no version constant and zero WIRE mentions; `tools/lib/` is gov-internal by `TOOL-aBatchedTribunal-6j`. Three deployable surfaces are not `tools/*` dirs at all — the playbook, `skills/session-kickoff/manifest-check.sh`, and `tools/settings-merge.py` (a file). Registry-scoped, AC8 is green by construction and blind to a new `tools/` dir; inventory-scoped it reds on day one. `map_extractors._tool_kits()`'s own docstring states the law against exactly this: README-gating "would have silently dropped three of ten". | Define "shipped kit" in S2 as a declared registry, enumerate which of the ten `tools/*` dirs are exempt and why, say how the three non-directory surfaces carry descriptors, and reconcile the Files-touched count with that registry. |
| 24 | `DEPL:27` | §2 S5, §6 | S5 has no acceptance coverage for either guarantee. No AC observes the hard ordering, and none observes "every copy is taken from the gov git index at a recorded commit, never from the working tree". AC3 records a commit but never proves the landed bytes came from it, so a deployer copying from a dirty working tree writes a receipt that is true-looking and false. That is the receipt's entire integrity claim. | Add two ACs. (1) Apply from a gov checkout with a deliberately dirty working tree; for every file in the receipt, the landed bytes equal `git show <recorded_commit>:<path>`. (2) The apply log (or a `plan` dump) shows the `.gitattributes` write and the renormalize strictly before the first kit-content write, and the gate-leg wiring strictly last. |
| 64 | `DEPL:28` | §2 S5, §6 AC1 | S5's ordering has no staging step, but every gate in this suite reads the git index: `check-arms.py:116`, `corpus_ids.py:190`, `resolve-python.test.sh:99/149`, `check-review-join.sh:43`, the codebase-map inventories, and `manifest-check.sh` C4/C6 — C4 tests TRACKED-ness and fails outright on untracked content, and the workflows gates refuse an empty population. `WIRE:309-310` already states this for one kit. AC1's "every gate leg exits 0" therefore measures an empty population — the green-by-empty-population class the whole spec is built to close. `git add --renormalize` also only re-adds already-tracked files, so it precedes the content it would need to stage. | Insert `git add` of the installed path set between "rendered artifacts" and "gate-runner and CI legs" in S5, state explicitly that the gates read the index not the worktree, and have AC1 assert the legs run against the staged tree. |
| 25 | `DEPL:14` | §2 S1, §6 | Two of S1's five subcommands have no AC. `plan` is named nowhere in AC1..AC11 — it is the whole of rollout commit 2 and the only read-only preview of a write-heavy tool, so it can ship inert with every AC green. `intake` (S7) is touched only indirectly by AC6, which exercises `apply --unattended` against a hand-made descriptor of unstated provenance, so nothing proves the interactive and unattended paths are "one code path with two decision sources". | Add an AC for `plan`: its dry-run enumeration of files-to-write equals, set-for-set, the receipt `apply` then produces on the same fixture. Add an AC for `intake`: a scripted stdin session writes `.governance/deploy.toml`, and `apply --unattended` consumes it end to end with zero prompts and zero refusals for missing answers. |
| 35 | `DEPL:255` | §6 AC7, §2 S3, §6 AC2 | AC7's "refuse a repo that already carries a kit" contradicts S3 + AC2 and its detection predicate is unspecified. A fresh deployer can only probe, and probing `tools/<kit>/` does not see a root-prefix adopter like swydee or nicocares — so `apply` lands a SECOND memory-recall at `tools/memory-recall/` while `check-wiring.sh:122` (`first_of memory-recall/recall-opened.fragment.json tools/memory-recall/…`, root spelling FIRST) keeps resolving the OLD copy. A duplicated install the receipt reports as clean and the wiring verifier reports as wired, against the wrong files. | State the predicate: refuse when a kit is resolvable at EITHER prefix and no `.governance/install.json` in this target claims it; proceed when the receipt claims it (the authorized re-run). Probe both `<kit>/` and `tools/<kit>/` for every descriptor id and name the resolved path in the refusal. |
| 36 | `DEPL:246` | §6 AC3, §2 S4 | The receipt hashes working-tree bytes, so `sha256sum -c .governance/install.sums` false-reds on every clone that is not the install machine. `* text=auto` leaves every `.py`/`.md`/`.js` under `tools/` platform-converted, so any receipt-covered file not carried by a `[[lf_pin]]` re-expands to CRLF on a Windows clone with `core.autocrlf=true`. S9 makes `check` the leg a target runs in its own CI — i.e. on a clone. This repo already carries the class as a standing gotcha and ships a dedicated CRLF arm in `check-wiring.sh`. | Hash normalized content, not the working tree: record `git hash-object` of each installed path and check `install.sums` against that; or require `selfcheck` to assert that every receipt-covered path is matched by some kit's `[[lf_pin]]` and refuse a descriptor where it is not. Keep the `sha256sum -c` sidecar only for the LF-pinned subset. |
| 37 | `DEPL:89` | §4 Data model, `[[files]]` | The whole-kit-dir `path = "*"` / `role = "engine"` glob swallows the project-owned files that live INSIDE kit dirs, and no precedence rule is specified. gov TRACKS both `tools/codebase-map/map_extractors.py` and `tools/drift-audit/drift_signals.py`, so combined with S5's "every copy is taken from the gov git index" the glob copies GOV's own filled inventories and measured pins into the target on the FIRST apply, not just on a re-apply. `WIRE:466` states the rule out loud ("NEVER overwrite the project-owned `<kit>/map_extractors.py`"). §4's "no code path writes a project-owned file" is vacuous for exactly those two, and AC4 is unenforceable. | Define precedence explicitly (later `[[files]]` entries win over earlier globs) and require every kit whose adopter seeds a file into its own kit dir to declare that path with `role = "project-owned"`. Have `selfcheck` refuse a descriptor carrying a bare `*` engine glob plus a `[[hole]]` whose artifact resolves inside the kit dir — that combination is the corruption, and it is statically detectable. |
| 65 | `DEPL:243` | §6 AC2 | AC2 makes `git status --porcelain` the idempotency predicate — the weak form this repo's own selftest contract rejects in writing. `tools/memory-recall/selftest.py:82` records "the ignore rule is deliberately absent: `git status --porcelain` is also clean when a write was merely hidden", and its arm at `:375` asserts the write-nothing property BY PATH. The criterion also collides with the staging S5 needs: once `apply` stages, porcelain is non-empty after run 1 and run 2 alike, so AC2 is either weak or unsatisfiable depending on whether `apply` commits — which the spec never says. | Assert idempotency by re-hashing every path in `.governance/install.sums` before and after the second apply and requiring the set and the hashes to be identical, plus an explicit "no path outside the receipt was written" enumeration. State whether `apply` stages or commits. Drop porcelain as the predicate. |
| 67 | `DEPL:125` | §4 Data model, `[[gate_leg]]` | `[[gate_leg]]` is modelled on gate-legs.json's flat `{name, argv}`, but the grounding measured a leg this deployer must emit whose correctness depends on a requirement no argv list can carry. `manifest-check.sh:162-164` WARNs and SKIPS C3 and C5 on a shallow clone, so the manifest ratchet's CI leg enforces nothing under `actions/checkout`'s default depth 1 — `WIRE:318-320` calls `fetch-depth: 0` mandatory. `check-verdict-epoch.sh:83-92` exits 1 rather than 0 for the same reason, which proves the repo treats history depth as leg-correctness data. The deployer emits CI legs whose green is vacuous, in the target, silently. | Add a `ci_requirements` table to `[[gate_leg]]` (at minimum `fetch_depth`), emit it into the target's CI job, and add an acceptance row over a shallow fixture asserting the emitted leg either reds or names the degradation rather than passing. |
| 68 | `DEPL:39` | §2 S8 | S8 names three non-mechanical holes; a fourth — the playbook's conditional-section DELETIONS — is measured, is triggered by S6's own kit-subset feature, and is owned by neither unit. `parallel-coding-governance.customize.md:53-66` lists what must be deleted when a kit is declined (four codebase-map lines, the memory-recall §5 bullet, §9/§11/§13, plus "dropping a template §-stub means dropping the matching section in the companion too"). There are no machine-findable anchors (`grep -c gov:block` → 0) and `TOOL-aSealedCaravan-1` §3 explicitly non-goals marker-fencing. A `--kits` subset that drops codebase-map lands a playbook instructing the target to run a kit it does not have. | Add a fourth `[[hole]]` (`playbook-conditional-sections`, `kind = authoring`) emitting an order that enumerates the sections to delete for the declined kit set; make AC5's count derive from the selection; or make the marker-fencing unit a `requires` of this one. |
| 69 | `DEPL:32` | §2 S6 | S6's default set includes the kickoff kit, but the spec has no machine-scoped install class and never mentions that the session-kickoff engine is installed OUTSIDE the target repo. `WIRE:53-68` is titled "ONCE per machine — NOT per project" and installs it at `~/.claude/skills/session-kickoff` by junction/symlink, verified by restarting the client. Every S3/S4 artifact is repo-scoped, and §5's own security rule forbids the out-of-tree write. As specced the deployer lands a manifest and a ratchet for a skill that will not load, with nothing telling the operator so — contradicting the spec's own "a non-mechanical step is represented, never faked". | Add `scope = "machine" \| "repo"` and a `link` action to `kit.toml`, give the receipt a machine-scoped section so a re-deploy no-ops, and represent the restart-and-confirm step as an unverifiable manual row — or state in §3 that WIRE §1 is out of scope and the kickoff kit ships ratchet-only. |

### Medium (7) and low (2)

| # | Sev | Where | Section | Claim | Concrete edit |
|---|---|---|---|---|---|
| 53 | medium | `DEPL:198` | §4 Files touched | "8 `kit.toml` — one per shipped kit" has no defined population: the only machine enumeration is `map_extractors._tool_kits()`, which returns ten directories today and eleven once `tools/govkit/` lands, while two §4 rows (playbook, manifest ratchet) have no `tools/` directory and one row merges two ("agent-cap, workflows"). AC8 then grades whatever registry it is handed, leaving gate-lint, lib and govkit itself silently descriptor-less — in commit 1, whose whole claimed value is "a machine-readable kit inventory". | Define the population against `_tool_kits()` plus an explicitly enumerated set of non-directory kits, make AC8 assert both directions, and correct the estimate to 11-12 descriptors. |
| 8 | medium | `DEPL:198` | §4 Files touched, §4 Inventory | pytest-parallel-guardrails is selectable by `--all` (S6) yet has no row in the §4 table and no descriptor in the count, so `--all` cannot land it at all. `inventories.json` `kits` enumerates ten directories. | Define "shipped kit" explicitly, add a §4 inventory row for pytest-parallel-guardrails, correct the descriptor count, and say where the playbook's and the manifest ratchet's descriptors live given neither is a `tools/` directory. |
| 41 | medium | `DEPL:159` | §4 Inventory (sibling coupling) | The memory-tree → memory-recall edge is modelled as `siblings` (a prefix constraint) when it is a hard, config-conditional `requires`. `corpus_ids.py:99-104` RAISES a named Problem when any of `DEAD_PATH_PIN`/`ORPHAN_ID_PIN`/`READ_PATH_CEILING` is set and `<kit-parent>/memory-recall/extract.py` is absent, so memory-tree's own declared gate leg (checks 13-16) hard-fails whenever memory-recall is not selected and the pins are answered. S1 lets `--kits` select memory-tree alone; `siblings` says nothing about presence. | Add a conditional edge form — `requires_if = { kit = "memory-recall", when_key_set = ["DEAD_PATH_PIN", "ORPHAN_ID_PIN", "READ_PATH_CEILING"] }` — and make `plan` either pull memory-recall in or refuse and name the keys. Keep `siblings` for the prefix constraint, and have `selfcheck` assert every `siblings` edge dereferenced at runtime is also covered by a `requires`/`requires_if`. |
| 71 | medium | `DEPL:263` | §6 AC10 (covers S10) | AC10's bidirectional descriptor↔runbook parity gate is red on day one with no exemption mechanism and no join key. §3 non-goals the ledger migration ("the descriptor carries it as a block the unattended path refuses"), so WIRE §3a is by design a section with no descriptor step — exactly what AC10 reds on; WIRE §1 is a second (see 69). Measured, WIRE has adoption sections for 3 of 10 kit dirs and zero grep hits for drift-audit, gate-lint, run-gates/gate-legs.json, check-kit-versions, check-verdict-epoch, merge-rows and tier2-review. `drift_signals.py:72-104` records this exact predicate measured wrong twice — display-name matching read 11 of 37 legs where script-path matching read 30, and bullet-count vs item-count is "a guaranteed false positive". | Give the parity gate an enumerated exemption list (`DECLARED_EMPTY` is the precedent: "an exemption that is not enumerated is not an exemption") covering WIRE §1 and §3a plus any section the descriptor deliberately does not cover, and specify the join as a stable id present on both sides — never a display name or a section count. |
| 72 | medium | `DEPL:276` | §7 Gates | §7's "two obligations specific to this unit" names only the `kits` inventory key; S10's Skill creates a second unclaimed key. `skill-engines` is extracted as every `skills/<name>/SKILL.md` (`map_extractors.py:103-110`) and is baselined shrink-only with `session-kickoff` as its only member, so `skills/deploy-governance/` reds `test_every_inventory_key_is_claimed_or_baselined`. A rendered copy under `.claude/skills/` would be a third key (`rendered-skills`), which also carries an `eol=lf` pin and a `--check` wiring leg. | Name `skill-engines` (and `rendered-skills` if a render is produced) in §7 alongside `kits`, and state that `memory/map/features/govkit.md` claims all of them and carries the four required dossier headings (`## Constraints & why`, `## Shared seams`, `## Gaps`, `## Reuse affordance` with a `seam:` line or a `none — <why>` declaration). |
| 74 | medium | `DEPL:25` | §2 S4 | S4 designs the receipt but neither implements nor restates the per-file `# gov: <kit>@<version> <sha>` fingerprint header that `aKitHardener` explicitly deferred to whichever unit ships the lock writer. This unit IS the lock writer, and the headers cannot be retro-added by the later converge unit — they must be written at install time. Without them, `check`'s only evidence is a receipt that vouches for itself, and AC4's project-owned-vs-drift distinction has no out-of-band anchor. | Either add the fingerprint header to `apply`'s write path for `engine`-roled files (and to `check`'s re-derivation), or restate the deferral in §3 naming aKitHardener's OUT row and the risk it leaves open. Silence is the defect. |
| 76 | medium | `DEPL:111` | §4 Data model, `[[lf_pin]]` | The deployer's own `.governance/` artifacts are pinned nowhere, yet AC3 requires `sha256sum -c .governance/install.sums` to exit 0 in the target "with bash alone" — and a CRLF checkout of `install.sums` leaves `\r` on every path, so GNU `sha256sum -c` reports no-such-file. `install.json` and `deploy.toml` are runtime-parsed and equally unpinned. AC8's selfcheck arms contain no pin-completeness check. The hand-listed shape also has precedent for being wrong: `WIRE:132-138` pins 2 of the 5 registries `adopt-memory-tree.sh:80-97` writes. | Derive the `.gitattributes` block from the receipt's actual file list rather than hand-listed `[[lf_pin]]` rows (every `*.sh` written, every runtime-parsed manifest, every byte-compared artifact), add an explicit `.governance/** text eol=lf` pin in the target, and pin `tools/govkit/**/*.toml` in this repo. |
| 10 | low | `DEPL:125` | §4 Data model, `[[gate_leg]]` | `tools/gate-legs.json` is not 40 entries of `{name, argv}` — it carries a third, semantically load-bearing key, `guard`. `run-gates.sh:45` reads `l.get('guard', [])` and `:53` routes a guard-carrying leg through `leg_if_changed()`, which is what makes a leg diff-scoped rather than always-run (leg 8 uses it today). If `[[gate_leg]]` adopts only `{name, argv}`, every leg a target installs becomes unconditional and the diff-scoping mechanism the spec is copying is silently dropped. | Add an optional `guard` field to the `[[gate_leg]]` table and say the target's gate runner honours it, or state explicitly that guards are out of scope for v1 and every deployed leg runs unconditionally. Cheap now, expensive to retrofit. |
| 11 | low | `DEPL:324` | §10 Reuse audit | There are three `adopt-*.sh --check` arms, not five: only `adopt-agent-instructions.sh`, `adopt-memory-recall.sh` and `adopt-drift-audit.sh` implement `--check`. `adopt-codebase-map.sh` and `adopt-memory-tree.sh` have none — and those are two of the five kits in the DEFAULT set, and the heaviest. S9's "every kit's own `--check` arm" has a hole exactly where the default install is heaviest, and the substitute work is budgeted nowhere. | Correct the count to three, name which kits lack a `--check` arm, and say what `check` does for codebase-map and memory-tree. `adopt-codebase-map.sh:212` already runs the installed gate — that is the reusable behaviour, not a `--check` flag. |

### Blockers in full

#### 33 and 45 — the default kit set cannot reach a green install

S8 represents `map_extractors.py` as "an unfilled template plus a work order in
`<target>/.governance/outbox/`". That representation is not available, because an unfilled template
makes the codebase-map adopter fail before the kit lands.

Verified in source: `map_extractors.template.py:112-117` raises `MapError` when `EXTRACTORS` is
empty ("an inventory-less map enforces nothing"), and both `gen_map.py:38`
(`IDS = ext.inventory_ids()`) and `test_codebase_map.template.py:70`
(`INVENTORY_IDS = ext.inventory_ids()`) bind it at MODULE scope. `adopt-codebase-map.sh:180-184`
seeds the unfilled template and exits 1 before reaching `gen_map.py` at `:189/:191` or the gate
install at `:207`. On the next invocation `gen_map.py --scaffold` dies at import. The result on a
fresh unattended install of the S6 default set is: no MAP_ROOT tree, no baseline, no GATE_FILE, and
an installed gate that cannot even be imported.

codebase-map is in the S6 default set, so AC1 — "the default kit set lands, and every gate leg the
descriptor declares exits 0 in that fixture" — has no satisfying assignment: the declared
codebase-map leg is `python <GATE_FILE>` and GATE_FILE does not exist. AC2's apply-twice-changed-zero
then has no green baseline to compare against, and rollout commit 3 lands with its own acceptance
matrix red. It also falsifies §4's use of codebase-map as "the counter-example worth copying" for the
unattended path: its adopter's virtue is that it runs the gate it installed, and on the unattended
path it never gets there.

**Correction.** Give `[[hole]]` a `blocks_adopt = true` flag and split `apply` into a
land-and-configure phase and a resume phase. Kits whose holes block adoption get their files copied
and their work order written, with `[adopt] argv` deferred until `govkit apply --resume` after the
order is discharged. `check` must then distinguish three states — not landed, landed but inert,
adopted — rather than two. Scope AC1's "every gate leg exits 0" to the non-blocked kits and add an
explicit AC that the codebase-map leg is red-by-design until its order is discharged and green after
a fixture `map_extractors.py` is filled. Correct the §4 inventory row: "Idempotent: yes,
reconverges" is not reachable on a fresh tree.

#### 32 — the exit-code map is keyed at the wrong granularity

§4 justifies `[exit_codes]` on the grounds that "three distinct meanings share exit 1 across the
adopters today — a hard refusal, a seed-and-stop where a file was written and now needs editing, and
a drift report from a `--check` arm", and concludes that "declaring them per kit makes the
disambiguation data". The premise is right and the conclusion does not follow: all three meanings
occur inside a SINGLE adopter, so a per-kit map cannot disambiguate a per-branch collision.

`tools/codebase-map/adopt-codebase-map.sh` exits 1 at `:52` (identity refusal — "refusing: this kit
dir belongs to the repo at … you are standing in", nothing written), `:98`, `:101` and `:113` (three
prefix/name/depth refusals, all explicitly "BEFORE anything is written"), `:150` (created
`.codebase-map.conf` — edit and re-run), `:184` (created `map_extractors.py` — declare and re-run),
`:189`/`:191` (gen_map crash, map tree half-written) and `:212` ("gate FAILED on the freshly seeded
tree", with conf, map tree and GATE_FILE all on disk). `adopt-memory-tree.sh` exits 1 at `:23` (seed
conf) and `:35` (refusing to overwrite a foreign `memory/`, nothing written) — and the spec's own
example descriptor declares memory-tree as `1 = "seed-and-stop"`, which mis-reads `:35` as a write.

With a single `1 = "seed-and-stop"` row, `apply` reads the `:212` half-installed-and-broken case and
the `:52` wrong-repo refusal identically, as "a file was written, go edit it". The deployer records
an install that did not happen and leaves the target wedged. This is precisely the disambiguation the
section claims to buy.

**Correction.** Replace the code→meaning table with a code+effect table: each declared outcome names
a probe the deployer RUNS (`must_exist` / `must_not_exist` on a named path — GATE_FILE for
codebase-map, `.memory-tree.conf` for memory-tree), so the classification is measured rather than
asserted. That is the same rule `adopt-codebase-map.sh:137-139` already states for itself: claim
nothing until it is read back. The alternative is to scope in assigning distinct exit codes to every
refusal branch in the four adopters and gate it — legitimate, but then say so explicitly, because §4
Alternatives rejected currently forbids touching them.

---

## Cross-cutting themes

Three patterns run through both specs and are worth naming, because each one is cheaper to fix as a
habit than as nine separate rows.

**Numbers that were reasoned rather than run.** The S8 predicate (95 hits / 37 files, not 2), AC4's
"seven citations" (3 in a shape check 15 can see), "41 legs after S8" (42), "8 `kit.toml`, one per
shipped kit" (a population of 8, 9 or 10 depending on the sentence), "five `adopt-*.sh --check`
arms" (three), "40 entries of `{name, argv}`" (three keys), and AC5's "exactly three work orders"
(two, four or five). `TOOL:133` states the rule the pair needed — "the predicate is run over the
real tree BEFORE it is trusted" — and applies it only to the predicate's correctness, never to the
counts derived from it.

**Acceptance criteria that cannot fail.** TOOL AC9's first arm is green at base; TOOL AC6 is a
negative a chatty no-op satisfies; DEPL AC8 quantifies over an undefined population; DEPL AC2 uses a
predicate this repo's own selftest rejects in writing; DEPL `plan` and `intake` have no AC at all.
Both specs argue at length that a guard which cannot fire is worse than no guard, and then ship
several.

**Scope items with no observer.** TOOL S2's manifest-check move (also its open fork F1), TOOL S11's
five records (one of five observed, and that one by a vacuous grep), DEPL S5's both guarantees, DEPL
S1's `plan` and `intake`. In each case the uncovered item is disproportionately the contested one.

---

## Verdict

**`TOOL-aSealedCaravan-1` — buildable after the listed edits, but the edits change commit 3's shape
and must precede build start.** The unit's thesis is sound and its four silent-green failures are
proved cold, so the design survives. What does not survive is the sizing: the S8 predicate was never
run over the surface S8 declares, and running it turns "two declared waivers over ~20 files" into 95
hits across 37 files, most of them deliberate root-prefix fixtures the unit keeps by non-goal. That
is a decision the spec has to make — narrow the surface or declare the registry — not a number to
patch, and it determines whether commit 3 is a day or a week. Three further corrections are
structural rather than cosmetic: the playbook and its two companions are inside the gate's surface,
absent from the cost table, and sitting on 80 bytes of headroom under a limit the charter forbids
raising; `REVIEW-PROTOCOL.template.md` is converted by no S-item and its parity gate inverts under
S8 either way; and the bar is *already* red on this branch at `drift_report.py --check`, from a
citation this planning session added. Fold all twenty findings into a rev-2, re-run the predicate,
re-cost Files touched, and this is buildable as three commits as designed.

**`DEPL-aSealedCaravan-2` — needs a re-spec of §4 Data model and §6, not a fold.** The goal, the
scope shape, the four-commit rollout and the reuse audit all hold, and the location fork F1 survives
once its false third (`check-arms.py` is repo-wide, not `tools/**`-scoped) is dropped. But the data
model as written cannot express the state the measured adopters produce: exit codes collide per
branch and not per kit; an unfilled `map_extractors.py` blocks adoption rather than deferring it, so
the DEFAULT kit set can never reach the green fixture AC1 demands; a whole-kit `*` engine glob has no
precedence rule and would copy gov's own filled inventories and measured pins into the target; the
memory-tree → memory-recall edge is a config-conditional hard requirement, not a prefix constraint;
`[[gate_leg]]` carries neither `guard` nor a history-depth requirement, so deployed legs lose
diff-scoping and go vacuously green in the target's CI; and the kickoff kit is machine-scoped with no
class to represent it. `apply` needs a resume phase, `[[hole]]` needs `blocks_adopt`, `[[files]]`
needs precedence, and the descriptor population needs a definition before `selfcheck` — rollout
commit 1's entire deliverable — can be written at all. §6 needs a matching rewrite: AC5's count must
derive from the selected kits' declared holes, AC2's predicate must be path-and-hash rather than
porcelain, AC3 must prove provenance against the recorded commit, AC7 must name its detection
predicate, and `plan` and `intake` need criteria. That is a rev-2 design pass over two sections, and
it should go back to the owner with F1 restated on its surviving evidence.

**Neither spec should start building today.** `TOOL-aSealedCaravan-1` can start as soon as its rev-2
lands. `DEPL-aSealedCaravan-2` consumes `TOOL-aSealedCaravan-1`'s declaration, so its re-spec has a
natural slot while the first unit builds.
