**Serves:** research TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-51

# Round-1 fix pass — the spec writer's returns

The returns of the agent dispatched from `memory/builds/dWitnessedBar/prompts/2026-10-25-prompt-TOOL-dWitnessedBar-40-1-spec-writer.md`, run direct/aa60714b713a021d5, one per stop (the pass, then the size trim the main loop chose), extracted from its transcript by script.

## Return 1

I cleared every finding in the brief, but TOOL-dWitnessedBar-51 is still over the 49152-byte spec ceiling. It was already 49370 bytes before I touched it, not the 48965 the brief assumed, and my fixes bring it to 49444 (292 over). So the main loop's `check-spec-tokens.py` will still report a size hit on unit 51. You asked for a split proposal in that case, but I found no split that BUILD-METHOD M4 allows, so I'm returning a decision for you instead (below).

After my edits, `bash tools/memory-tree/check-memory-hygiene.sh --only 2,12,25` prints no dWitnessedBar finding. It prints only these five lines, which are not findings and come from units 20 and 24, which I did not touch:

memory-hygiene: check 25 did not grade `policy.py lists` — READER NOT IN TREE covers it, on memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-20.md S2
memory-hygiene: check 25 did not grade `legacy-homes` — READER NOT IN TREE covers it, on memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-20.md S2
memory-hygiene: check 25 did not grade `check_policy.py` — READER NOT IN TREE covers it, on memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-20.md S2
memory-hygiene: check 25 did not grade `tools/playbook/core.py meta-check` — READER NOT IN TREE covers it, on memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-24.md S14
memory-hygiene: check 25 did not grade `core-pending.txt` — READER NOT IN TREE covers it, on memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-24.md S14

I did not run `check-spec-tokens.py`, since my role doesn't allow it, so that result is still yours to observe. I staged nothing and committed nothing, touched no deviation record, and did not run the index generator.

### Per finding

**1. Unit 51 does not parse past AC30.** I rewrote AC30's planted tail as "a line that opens with three backticks", so no fence opens. Check 12 then reported one more problem: S37's `YYYY-MM-DD` matched the skeleton-placeholder pattern. I respelled it as "a valid `%Y-%m-%d` date", which means the same thing. Check 12 is now clean on unit 51.

**2. Check 25, retirements owe a Readers clause.**
- **Unit 44 S4:** this one really does retire a name (`up` deletes the `INHERITED_RED` assignment), so I added a `**Readers:**` clause:
  - **By name:** `tools/unattended/unattended.sh` (`read_gate_policy`), `tools/unattended/unattended.test.sh`, `tools/unattended/.unattended.conf.example`, `.unattended.conf`, `.githooks/gate-env.sh`, `.githooks/pre-push` and `.githooks/pre-push.test.sh`. Each one spells the name at HEAD. The clause points to TOOL-dWitnessedBar-3 S8 for the rest of the name's readers.
  - **By value:** `read_policy_at` and `read_gate_policy`.
  - I removed the backticks from the unit id because check 25 tried to resolve it as a reader.
- **Unit 51 S28, S31 and S48:** none of these retires a name, so I reworded each and kept its meaning:
  - S28: "removes the rest" became "prunes the rest".
  - S31: "removed against changed" became "a row gone on one side and changed on the other".
  - S48: "drops `DECLARATIVE_LEG_KEYS` before hashing" became "hashes each row less its `DECLARATIVE_LEG_KEYS`".

**3. Check-spec-tokens.**
- **Handoff:** unit 51 does read the value, so I left unit 28's bullet alone. Unit 51 S26 now says it reads `tests.product`'s `declared-with-runners` as `declared`.
- **Stale pins:** I re-pinned each `**Carries:**` line and added a §8 mark in the `RESOLVED (agent, 2026-10-25, delegated)` shape naming the deviation that moved it:

  | Unit | New pin | Deviation | §8 mark |
  |---|---|---|---|
  | 3 | `cl-dClosedLoop-0341@65d333f3` | 31 | F5 |
  | 7 | `cl-dClosedLoop-0345@72933671` | 71 | F4 |
  | 16 | `cl-dClosedLoop-0354@13f6f9b8` | 161 | F6 |
  | 21 | `cl-dClosedLoop-0359@5c408077` | 211 | F4 |
  | 28 | `cl-dClosedLoop-0366@337938da` | 281 | F5 |

  Each existing rev-2 line in §9 now says what moved, with no bump to rev-3.
- **Token:** unit 16 S1 now names `memory/builds/dClosedLoop/build/2026-10-17-build-PLAY-dClosedLoop-1-final-reviews-instruments.md:1087-1090` in backticks, where it states the population rule. The rev-2 line of unit 16 records this too.

### Decision needed: unit 51's size

M4 allows two units only when the write sets are disjoint under M6. That means no shared path, neither unit writing a file the other reads as a contract, and neither depending on the other's output. Unit 51's own §4 says no such split exists, and checking each item's write set against the code confirms it:

- **One shared file:** `tools/lib/resolve-python.test.sh` (whose `PARITY_ROWS` list starts at `:168`) is written by S19, S20, S21, S29 and S46. That pulls in the files those items touch: `fix_keeps.py`, `seen_red.py`, `drift_report.py`, `govkit.py`, `pre-push` and `push-main.sh`.
- **That group chains into the runner:** `govkit.py` brings in S14 and S25, `drift_report.py` brings in S7 and S23, S7 brings in `verdict_flow.py` (S15, S36), S36 brings in `held_halves.py` (S48, and S47 reads it as a contract), and S48 brings in `run-gates.sh` (S28, S34, S39, S40).
- **The only candidate second half is the ledger items** (S1, S2, S9, S10, S17, S30–S33, S37, S50). Two links tie it back:
  - S9's `date-cutoffs` registration and S12's `ratchet selftest` `enforces` both write `tools/memory-tree/kit.toml`. That file is also an input to the generated `tools/gate-legs.json`, which S11, S12 and S42 also write.
  - S1's widen rows are worked out from every shell file that grew up to HEAD, including the ones this unit's own runner items grow. So S1 depends on the other half's output.

Options:
- **(a)** Keep one unit and shrink text that is not a criterion. The §1 report-item table repeats the "id N" that every S item already carries; reducing it to the three merged rows (M1, M2, M3) plus one sentence saves about 1.5 KB. Compressing the §4 files list into a paragraph would save a little more.
- **(b)** Hold unit 51 above the ceiling with a high-water row, written by `check-template-size.sh --bump` with an explicit limit.
- **(c)** Split anyway and build the two halves in sequence. M4 forbids this, because it allows two units only when both can build at once.

I recommend **(a)**: it trims no criterion and keeps unit 51 one unit, as M4 requires. I didn't apply it because the brief said to return rather than trim when the size was over.

Files changed:
- C:\projects\coding-governance\.claude\worktrees\unattended-dwitnessedbar-d0e46e\memory\builds\dWitnessedBar\spec\2026-10-25-spec-TOOL-dWitnessedBar-3.md
- C:\projects\coding-governance\.claude\worktrees\unattended-dwitnessedbar-d0e46e\memory\builds\dWitnessedBar\spec\2026-10-25-spec-TOOL-dWitnessedBar-7.md
- C:\projects\coding-governance\.claude\worktrees\unattended-dwitnessedbar-d0e46e\memory\builds\dWitnessedBar\spec\2026-10-25-spec-TOOL-dWitnessedBar-16.md
- C:\projects\coding-governance\.claude\worktrees\unattended-dwitnessedbar-d0e46e\memory\builds\dWitnessedBar\spec\2026-10-25-spec-TOOL-dWitnessedBar-21.md
- C:\projects\coding-governance\.claude\worktrees\unattended-dwitnessedbar-d0e46e\memory\builds\dWitnessedBar\spec\2026-10-25-spec-TOOL-dWitnessedBar-28.md
- C:\projects\coding-governance\.claude\worktrees\unattended-dwitnessedbar-d0e46e\memory\builds\dWitnessedBar\spec\2026-10-25-spec-TOOL-dWitnessedBar-44.md
- C:\projects\coding-governance\.claude\worktrees\unattended-dwitnessedbar-d0e46e\memory\builds\dWitnessedBar\spec\2026-10-25-spec-TOOL-dWitnessedBar-51.md

## Return 2

I compressed unit 51 as you directed. It is now **48400 bytes**, 752 under the 49152 ceiling and inside your 48500 target. `check-memory-hygiene.sh --only 2,12,25` prints **no dWitnessedBar finding**; it prints only the same five "check 25 did not grade … READER NOT IN TREE covers it" notes on units 20 and 24, which are not findings.

- **§1 table:** cut to its header and the three merged rows (M1, M2, M3). One sentence now covers the rest: M4 to M34 and L1 to L13 each hold one report id and map to one scope item in report order, from M4 (id 2) as S7 to L13 (id 56) as S50, and each scope item names its id. The line "That is 37 MEDIUM and 13 LOW findings by raw id." stays.
- **§4 Files touched:** now a paragraph instead of a list, with all 61 paths still in backticks and in their original order. That includes the two record patterns, `memory/builds/dWitnessedBar/build/<date>-build-TOOL-dWitnessedBar-51-widen-<n>.md` and `...-51-deviation-<n>.md`. The paragraph form should not change what `check-spec-tokens.py` sees. Its reader at `tools/check-spec-tokens.py:532` collects every backticked path under the `### Files touched` sub-head (defined at `:325`) whatever the layout, so it gets the same 61 paths. I haven't run `check-spec-tokens.py` itself, since my role doesn't allow it.
- **Unchanged:** no criterion, scope item or edge, no rev bump, and no other part of the file. Nothing is staged or committed.

The file is C:\projects\coding-governance\.claude\worktrees\unattended-dwitnessedbar-d0e46e\memory\builds\dWitnessedBar\spec\2026-10-25-spec-TOOL-dWitnessedBar-51.md
