**Serves:** journal TOOL-dDerivedDocket-1..36 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1

# Spec brief — dDerivedDocket, all 38 units

ONE file for the whole roster on purpose. M2 requires sub-specs to AGREE on scope, interface,
ordering and acceptance, and an author who has read only their own unit cannot check three of those
four. Read your unit's row, read the edge table, and read the design sections your unit names.

## What is already decided, and may not be re-litigated

The design record is `memory/builds/dDerivedDocket/build/2026-09-14-build-TOOL-dDerivedDocket-1-design.md`
(DR below). It went through three independently drafted designs, three adversarial critiques, a
judge, two bypass hunts with scratch labs, and three rounds of owner rulings. Its section 17, section
20 and section 22 tables are the owner's rulings; the mandate record beside this file carries them
verbatim. A ruling is cited in §8 as `RESOLVED (owner, 2026-09-13)` naming its D-number, never
re-decided. A fork the design did NOT settle is yours under M3, marked `RESOLVED (agent, 2026-09-14,
delegated)`.

**Where the design and the owner's rulings disagree, the ruling wins.** Four rulings went against the
design's recommendation and several design sections still carry the old text. D4 REOPEN is allowed
(DR 17.1). D6 closeout is a GATE from the flip, retroactive (DR 17.2). D7 severity rows ship now
(DR 17.3). D12-a ids runs ALWAYS start from an owner-landed README, so entry mode E2 is dropped (DR
20.1). D12-b `asks-disposed` is overridable (DR 20.1). D12-h lifts the self-test ban for units 16, 17
and 18. D12-i3 keeps the charter's "land on local main first" and adds an unattended exception (DR
22.1). D12-i5 ABSORB is wider than the write set (DR 22.1). D12-i7 GATE_WALL is hand-set, initially
21600 s (DR 22.1). D12-i9 auto-resume ships ON in the kit and in gov. The prompt path's single owner
turn then ruled: the run SIGNS the D2 and D6 tables itself under mechanical rules (unit 33), the D10
all-node drain is replaced by the permanent transition audit (unit 9), and the remote-CI workflow
file is committed and pushed in this build (unit 32).

## Re-ground before you write — three builds landed in this territory after DR was measured

DR's line citations are at `09a22d2b`; this run's BASE is `abac6d59`. Verify every claim about
current code at BASE and say in §10 where DR and the source disagree. In particular:

- **`TOOL-cSpliceWarden`** reconciled the 2026-08-17 TOOL archive and made rotation a DECLARED mode:
  `ROTATION_MODE` in `.memory-tree.conf`, graded by a new hygiene check 24 delegated to
  `tools/memory-tree/row_grammar.py`. Units 8, 11, 14 and 34 must integrate with it rather than
  assume DR's picture of rotation. Unit 14 may already be done: if regrounding shows check 10's
  backlog blindness is closed, retire it (WONTDO, with the reason) rather than duplicate work.
- **`TOOL-cGradedDebt`** gave `memory/project/curation-debt.txt` a stale-entry guard and made check 8
  print its graded-row count. Units 8 and 34 build on that, not on DR's older description.
- **`TOOL-cWidenedNet`** widened the install-prefix gate to its own class. Every new kit file you
  spec must satisfy it: a kit file names nothing outside itself by literal.

## The spec format this tree enforces for a spec dated 2026-09-14

Read `memory/TEMPLATE-SPEC.md` whole; it states the rules and `memory/HYGIENE.md` check 12 grades
them. The ones most often missed, all armed from 2026-09-08:

- Status header: `**Status:** SPECCED · rev-1 · 2026-09-14 · node d · Tier-<n> · base abac6d59 ·
  streams <stream> · order <n>`. `order` is your roster number below. Do NOT write a `closes` or
  `advances` verb: this build creates those and the parser at BASE does not know them.
- File: `memory/builds/dDerivedDocket/spec/2026-09-14-spec-<FAMILY>-dDerivedDocket-<n>.md`, H1
  `# <FAMILY>-dDerivedDocket-<n> — <title>`. Keep the title short: it renders into the README's
  generated table, and that README sits close to its byte cap.
- Every §2 Scope item names an `AC<n>` or carries `NOT OBSERVED` and why.
- `### Edges` under §3, one bullet per edge from the table below, `**consumes-from**` or
  `**hands-off**` then the backticked sibling id. Write BOTH ends: the reciprocity arm joins them.
- Every numbered acceptance criterion carries a backticked token AND a `Red when:` clause naming the
  break that turns it red. A criterion whose break is only its own negation is the finding.
- §5 carries every readiness row `.memory-tree.conf` declares in `READINESS_ROWS`.
- §7 Gates names at least one leg `tools/gate-legs.json` resolves.
- §10 records the recall terms you used AND the probe result: a `reuse_lookup` citation or an
  explicit "no existing seam fits". For a unit where DR tested candidates, record each rejected
  candidate and the test that rejected it (M12): the losing designs are in DR sections 0 and 12.
- Example ids use the undeclared family `EXMP`, never a real family, or check 14 counts them as
  citations of ids nothing defines. Never let a bullet or table row LEAD with a real id other than
  your own: that shape DEFINES the id and check 13 then reds a second claimant.

## The roster, each unit's design pointer, and its binding rulings

DR line ranges are in the design record as filed. "Tier" is a proposal; the kickoff manifest's tier
rule decides.

| # | Unit | DR sections | Binding notes |
|---|---|---|---|
| 1 | `TOOL-dDerivedDocket-1` held-suite failure baseline | 21.4 U16 (1801-1826), 21.6 | Built FIRST (D12-i11). Self-tests allowed (D12-i8). Tier 2 |
| 2 | `TOOL-dDerivedDocket-2` in-place landing merge | 21.4 U18 (1843-1877); 21 fixes KF4 | D12-i1. `push-main.sh` keeps its attended path unchanged. Tier 2 |
| 3 | `TOOL-dDerivedDocket-3` the run's landing path | 21.4 U19 (1878-1901); KF2 | Self-tests allowed. The charter exception text is unit 37's. Tier 2 |
| 4 | `TOOL-dDerivedDocket-4` HELD phase, lease, derived phase | 21.4 U26 (2042-2085); KF7, KF15 | Self-tests allowed. CORE_FLOOR moves. Tier 2 |
| 5 | `TOOL-dDerivedDocket-5` auto-resume from HELD | 21.4 U26 scheduler part; 22.1 D12-i9 | ON by default in kit and gov; a DECISIONS row records the charter §9 override by owner ruling. Self-tests allowed. Tier 2 |
| 6 | `TOOL-dDerivedDocket-6` ask parser and status fold | 2, 3, 4 (120-371); 17.1-17.3 | No status token on an ask. REOPEN cancels a named record. SEV most-severe-wins. WITHDRAWN folds to WONTDO. Dark. Tier 2 |
| 7 | `TOOL-dDerivedDocket-7` generated family view | 5 (372-450); 7; 18r.2 L4 | View defines no id; data-loss and mode guards; banner in the header. Dark. Tier 2 |
| 8 | `TOOL-dDerivedDocket-8` hygiene engine in builds mode | 6 (451-487); 20 D12-g | Check 13's skip covers asks filed before `ASK_CUTOFF` only. Integrate check 24 and cGradedDebt. Dark. Tier 2 |
| 9 | `TOOL-dDerivedDocket-9` transition-merge audit | 18 rev-2 (973-1085); 18 rev-3 A1 A3 A5 A6 A7 | Lineage classification, not tip. Liveness and registry. `commit-msg` carrier. PERMANENT. Tier 2 |
| 10 | `TOOL-dDerivedDocket-10` driver refuses shard-into-view | 18r.2 L3; 18 rev-3 A2; 7 | `memory/backlog/*.md merge=rows` is KEPT; `builds/*/BACKLOG.md` ADDED. Tier 2 |
| 11 | `TOOL-dDerivedDocket-11` migration planner | 9 (538-605); 17.2 | Produces the D2 table and the D6 worksheet as records for unit 33. Tier 2 |
| 12 | `TOOL-dDerivedDocket-12` relocation tools | 18.4 (925-951); 18r.3-18r.4 (1019-1043); A4 A6 A10 | RELOCATED provenance rows; `--repair` refuses a status change without confirmation. Tier 2 |
| 13 | `TOOL-dDerivedDocket-13` straggler hook bodies, inventory | 18.3 (913-924); 18r.2 L5 L6; A8 | Hook BODIES, since old branches run main's hook files with their own checkers. Tier 2 |
| 14 | `TOOL-dDerivedDocket-14` rotation-note check for shards archives | 15 U0; regrounding above | May retire against cSpliceWarden. Tier 1 |
| 15 | `TOOL-dDerivedDocket-15` ask envelope and READY | 19.3 (1204-1309); 19 fixes F6; 20 D12-d D12-e | `accept` required for new asks; probe allow-list shipped empty. Tier 2 |
| 16 | `TOOL-dDerivedDocket-16` driver ask-awareness | 19.2 (1119-1203), 19.4 (1310-1377); F2 F4 F5; D12-a D12-f | Ids invocations print the E3 recipe and stop. Self-tests allowed (D12-h). Tier 2 |
| 17 | `TOOL-dDerivedDocket-17` asks-disposed DoD item | 19.5 (1378-1447); F3; D12-b D12-c | OVERRIDABLE with a recorded reason. Self-tests allowed. Tier 2 |
| 18 | `TOOL-dDerivedDocket-18` leg second opinions | 19.8 U13 (1504-1534) | Self-tests allowed. Tier 2 |
| 19 | `TOOL-dDerivedDocket-19` authority only from owner README | 19 fixes F1 (1613-1654); 20 D12-j | Scaffold never emits `may:`. Tier 2 |
| 20 | `TOOL-dDerivedDocket-20` unattended carriers, two-key refusal | 8 (509-537); 19.6, 19.8 U14 | Rewrite the false "MANDATES a backlog row" comment. Tier 2 |
| 21 | `TOOL-dDerivedDocket-21` remote-relative bases, leg guards | 21.4 U17 (1827-1842) | Tier 1 |
| 22 | `TOOL-dDerivedDocket-22` LANDED derived from the tip | 21.4 U20 (1902-1925); KF4 KF5 KF15 | D12-i2. Never derived inside a committed generated file. Self-tests allowed. Tier 2 |
| 23 | `TOOL-dDerivedDocket-23` red attribution, report-only | 21.4 U21 (1926-1949); KF14 KF3 | Signature rules per KF14. Tier 2 |
| 24 | `TOOL-dDerivedDocket-24` inherited-red policy | 21.4 U22 (1950-1985); KF2; 22 D12-i4 D12-i5 | Land, bounded at 10; ABSORB WIDER, own commit per fix. Self-tests allowed. Tier 2 |
| 25 | `TOOL-dDerivedDocket-25` runner hygiene | 21.4 U23 (1986-2000) | Tier 2 |
| 26 | `TOOL-dDerivedDocket-26` honest verdicts under contention | 21.4 U24 (2001-2023); 22 D12-i6 | Retry pass counts, tracked. Tier 2 |
| 27 | `TOOL-dDerivedDocket-27` declared gate wall | 21.4 U25 (2024-2041); 22.1 D12-i7 | GATE_WALL hand-set, initially 21600; a conf check reds below the largest leg ceiling. Self-tests allowed. Tier 2 |
| 28 | `TOOL-dDerivedDocket-28` run-owned process ledger | 21.4 U27 (2086-2102) | Self-tests allowed. Tier 2 |
| 29 | `TOOL-dDerivedDocket-29` review durability | 21.4 U28 (2103-2116) | Tier 2 |
| 30 | `TOOL-dDerivedDocket-30` checker defects | 21.4 U29 (2117-2136) | Self-tests allowed. Tier 2 |
| 31 | `TOOL-dDerivedDocket-31` build-method carriers | 21.4 U30 (2137-2152); 22 D12-i10 | BUILD-METHOD's own byte budget binds. Tier 2 |
| 32 | `TOOL-dDerivedDocket-32` remote CI | 21.6 U9 (2205-2231); 20 D11-b; 22 D12-i12 | Workflow file committed AND pushed here (owner: credential has scope). Full-history checkout. Tier 2 |
| 33 | `TOOL-dDerivedDocket-33` delegated signing: D2 and D6 | 17.2 (826-843); 9 step 5; mandate's final turn | See "Delegated signing" below. Tier 2 |
| 34 | `TOOL-dDerivedDocket-34` THE FLIP | 9 step 10, 11 (618-637), 14 (738-758), 15 U5; A2; D8 | One atomic commit; staged REDs on the real tree; `TOOL-aWeighedCompass-3` disposed as superseded. Tier 2 |
| 35 | `TOOL-dDerivedDocket-35` arming | 19.8 U15; 18r.7 | Real-tree staged REDs of units 9, 13, 16, 17. Tier 2 |
| 36 | `TOOL-dDerivedDocket-36` memory-tree guides and dossier | 11; 15 U6; 19.8 carriers | A `memory-tree-backlog` map dossier claims the `backlog-shards` keys out of `baseline.toml`. Tier 2 |
| 37 | `PLAY-dDerivedDocket-1` charter template | 11; 22.1 D12-i3 | Net-negative bytes under the 48 KiB gate; the unattended landing exception. Tier 2 |
| 38 | `DEPL-dDerivedDocket-1` adopter runbook | 10 (606-617); 11 | Migrate step, the added attribute, the scaffold header fix. Tier 1 |

## The edge table — write BOTH ends

Each line reads `<consumer> consumes-from <producer>`; the producer's spec writes the matching
`hands-off`. Add an edge you discover and say so in §9; never drop one.

- 2 ← 1 · 3 ← 2 · 3 ← 4 · 5 ← 4 · 22 ← 3 · 22 ← 4 · 23 ← 1 · 24 ← 23 · 27 ← 4 · 28 ← 4 · 29 ← 4
- 7 ← 6 · 8 ← 6 · 8 ← 7 · 9 ← 6 · 10 ← 7 · 11 ← 6 · 11 ← 7 · 12 ← 9 · 12 ← 11 · 13 ← 9 · 13 ← 12
- 15 ← 6 · 16 ← 15 · 16 ← 19 · 17 ← 16 · 18 ← 16 · 18 ← 17 · 20 ← 16 · 20 ← 17
- 33 ← 11 · 34 ← 8 · 34 ← 9 · 34 ← 10 · 34 ← 12 · 34 ← 33 · 35 ← 34 · 36 ← 34 · 37 ← 34 · 38 ← 34
- 32 ← 9

## Delegated signing (unit 33) — the owner's terms

The owner ruled "Delegate to this run" instead of signing the D2 same-id table and the D6 triage sweep
personally. That is authority to sign under RULES, not discretion. Unit 33's spec states the rules
mechanically and conservatively. At minimum: `unit` is proposed only where the row was specced in
place or born in its spec's own commit, and never for a pair DR names as different subjects; CLOSED
or WONTDO is written only with cited evidence (a CLOSED spec, a commit, the row's own recorded
withdrawal); a row the rules cannot decide is KEPT, never closed, with its reason naming the rule
that could not decide it. Every signature is a record a later reader can re-derive.

## What this build does NOT do

- **No adopter migration.** Each adopter gets its own DEPL build later.
- **No GitHub settings change.**
- **No pull-request landing.**
- **Not the concurrent adopter-wiring work.** Another session is fixing govkit's attribute emission
  and check-wiring's flat-layout probe. Units 10 and 34 touch the merge attribute only as this design
  requires, and landing reconciles with whatever that session lands first.
