**Serves:** spec-audit PLAY-dConvergedCharter-22@rev-1 PLAY-dConvergedCharter-11@rev-1 PLAY-dConvergedCharter-17@rev-1 PLAY-dConvergedCharter-12@rev-1 PLAY-dConvergedCharter-16@rev-1 PLAY-dConvergedCharter-5@rev-1 PLAY-dConvergedCharter-20@rev-1 PLAY-dConvergedCharter-21@rev-1 PLAY-dConvergedCharter-23@rev-1 PLAY-dConvergedCharter-6@rev-1 PLAY-dConvergedCharter-3@rev-1 PLAY-dConvergedCharter-19@rev-1 PLAY-dConvergedCharter-2@rev-1 PLAY-dConvergedCharter-13@rev-1 PLAY-dConvergedCharter-1@rev-1 PLAY-dConvergedCharter-10@rev-1 PLAY-dConvergedCharter-7@rev-1 PLAY-dConvergedCharter-9@rev-1 PLAY-dConvergedCharter-8@rev-1 PLAY-dConvergedCharter-15@rev-1 PLAY-dConvergedCharter-4@rev-1 PLAY-dConvergedCharter-14@rev-1 PLAY-dConvergedCharter-18@rev-1

# Tier-2 spec audit: dConvergedCharter, the 23 Convergence specs, round 1

*This was an adversarial pre-code pass over the spec stage of dConvergedCharter, the Convergence build of the dClosedLoop chain. Its goal is to carry the 23 clauses of its `[chain]` row and close its 15 owned gaps. The build has no run-mandate prompt, so the README is the mandate. Synthesised by gov-synthesizer on 2026-11-04. Every item below survived a skeptic who was prompted to refute it.*

Reviewed: memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-22.md@663853e47a7bde42518a3039554675f1f44a4f69, memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-11.md@eefd39817afabd9159ffdb9d98d445089c2ce372, memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-17.md@d5efbc0504ca5da6d90b1c0e489d1dcf2e609628, memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-12.md@1c1c5c37b9d49459fedc7931a56fce046b8b3f6a, memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-16.md@d3c6310ee1848984a9a74e26aceea3c90a470739, memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-5.md@fc33eee79e78d83c7dc5a99b2a415bd5fc729fb4, memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-20.md@10b79825b32b61ebbc8077e633138d7c7a2424de, memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-21.md@feebf2113c9970a55a1dec638239e52d17a14b68, memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-23.md@3615ab55ab351d1387ed15f9e2f7bd7a1b362cc9, memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-6.md@bab7de3054d1311d35f852d72917a525918bdf5f, memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-3.md@40a268f147d54f4d8688f0dd921869a0ec941f8c, memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-19.md@b70d13e856d48237bb327f07942b875c984b1507, memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-2.md@4d757940fb943525ba5cb84aece2a9391eed72d8, memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-13.md@9eebdeac24f74ee97d058bc08b99ff2b7cd14db5, memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-1.md@3d4a93490714c9ec3d06bf03559e9bb587907e29, memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-10.md@8f3c075c6785ecb472ce1965717594d1bf3c274d, memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-7.md@84c10a31afce7ec82b0c970fabbf70ae84642798, memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-9.md@26b0481f38a7ea2c495b4957f626683f339eb703, memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-8.md@61d5092c1473f0818681788c81cf550cc9f0b769, memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-15.md@8a26623259ccebe0918926ed720beb654f814d39, memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-4.md@e109e5517ca0814e2a64d8586c1c8ab20cd81daa, memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-14.md@6f47f575cf4e1bbbc1e07a6b2089bba6b9ed5371, memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-18.md@d7a23d22f5ffe63f781ce1175adf26d541a23873

ROUND: 1

## Verdict: CLEAN WITH FIXES

No item is a blocker. There are 10 HIGH items, which must be fixed in the specs before the build pass starts. Each one, built as written, either reds the bar on gov's own tree, loses an adopter's values, or yields a check that certifies something it never examines.

The HIGH items cluster in three places:

- The policy fold, units 11 and 20. Unit 20's step reads a resolver that never sees the conf home. Unit 11's escape and eval shapes let a missed or failed reader go unseen. A JS write gate goes unarmed partway through the build.
- The unattended-kit retirement, unit 12. It misses readers that resolve the kit by its home name.
- Unit 9's skill rename. It contradicts unit 17's held `/build` client.

Specs 11, 12 and 20 together carry most of the medium items. A re-spec pass on those three should come before any other unit is revised.

## Review shape

Intensity full, raw 56, confirmed 55, refuted 1, unverified 0 (0 uncertain), precision 0.98.

| lens | returned | raw | confirmed | refuted | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|
| coherence | yes | 18 | 18 | 0 | 0 | 0 | 1.00 |
| grounding | yes | 13 | 13 | 0 | 0 | 0 | 1.00 |
| reuse | yes | 8 | 8 | 0 | 0 | 0 | 1.00 |
| blast-radius | yes | 6 | 6 | 0 | 0 | 0 | 1.00 |
| failure-envelope | yes | 11 | 10 | 1 | 0 | 0 | 0.91 |

**Adjudicated tally by item:** 50 items: 0 BLOCKER, 10 HIGH, 31 MEDIUM, 9 LOW.

**Adjudicated tally by raw confirmed finding:** 55 findings: 0 blocker, 11 high, 34 medium, 10 low.

**Merges, same binding grade only:**

- ids 22 and 32 (HIGH) are one defect.
- ids 42 and 49 (MEDIUM) are one defect.
- ids 13, 26 and 51 (MEDIUM) are one defect.
- ids 16 and 28 (LOW) are one defect.

**Re-grades:** the skeptic re-graded five findings: 3, 42 and 48 from high to medium, and 5 and 36 from medium to low. Each sits at its binding grade, and I see no reason to depart from any of them.

**Refuted:** id 52 (spec 8 S2, `check_renderer_live`). It appears only in the appendix.

**Run integrity:**

- Lenses: 5/5 returned, 0 DIED.
- Skeptic batches: 5/5 returned, 0 DIED.
- Demoted to unverified: 0 contradictory verdicts and 0 orphaned duplicate refutations.
- Discarded or merged by the harness: 0 spurious verdicts and 0 duplicates.
- Fixes on confirmed findings: 48 judged sound, 7 judged UNSOUND, 0 none proposed, 0 NOT JUDGED.
- Severity on confirmed findings: 0 UNGRADED by the skeptic, 5 RE-GRADED.
- Unverified findings: 0 answered UNCERTAIN and 0 with no usable verdict.
- Lens notes: none were supplied, so every lens ran on the kit's generic brief.
- Move check: no checked subject moved.

Every count above is zero where it should be, so this run is complete.

**Roles:** finders gov-spec-reviewer, skeptic batches gov-skeptic, synthesis gov-synthesizer.

**Intent:** 1 spec document was supplied as `specs`, as sibling context.

**Checklist:** 110 items, 22 per lens across the 5 lenses. 2 invariants come from its by-design block.

**Rejected fixes:** for ids 6, 35, 36, 45, 46, 49 and 53, the item gives the skeptic's corrected fix, never the finder's rejected proposal. Every other fix was judged SOUND by the skeptic.

## HIGH

### H1. Unit 9 AC2 can only pass if unit 17's held `/build` client is deleted (id 1)

**Specs:** PLAY-dConvergedCharter-9 PLAY-dConvergedCharter-17

- **Where:** spec 9 §6 AC2.
- **What is wrong:** AC2 requires `git ls-files -- tools | grep -c SKILL.template.md` to print 0, and credits the `/build` template's removal to unit 17. Unit 17 S4 keeps `tools/roles/SKILL.template.md` in its held set until the shim row closes, and no window closes inside this build.
- **Consequence:** AC2 stays red on every correct build. The only way to turn it green is to delete the held client, which reds 17 AC3.
- **Fix (judged SOUND):** Restrict AC2 to the five renamed kits: `git ls-files -- tools/{lexicon,drift-audit,branch-reconcile,memory-recall,runlog} | grep -c SKILL.template.md` prints 0. Separately, state that `tools/roles/SKILL.template.md` stays as unit 17's held client until its shim row closes.
- **Left-shift gate:** a spec-audit check that runs each AC's command against the held sets declared by the sibling specs.

### H2. Unit 9's stale-path arm reds the held `/build` rows of unit 17 (id 2)

**Specs:** PLAY-dConvergedCharter-9 PLAY-dConvergedCharter-17

- **Where:** spec 9 §2 S7 (`check_skill_paths`), against spec 17 S3/S4.
- **What is wrong:** S7 admits a `.claude/skills/` path only when it is a `[[drive]]` skill directory or the `from` of an open skill shim. The roles kit's `to`, `probe` and `pattern` rows (`tools/roles/kit.toml:57`, `:90`, `:145`) name `.claude/skills/build/SKILL.md`. Unit 17's shim `from` is `{prefix}/roles/SKILL.template.md`.
- **Consequence:** `core skills conformance` reds gov's tree once units 9 and 17 are both built. The only way to clear it breaks unit 17's held window.
- **Fix (judged SOUND):** Have S7 also admit a path that an open `skill` shim holds through its kit's install row, meaning a command-`to` row whose `from` template renders to that `to`. Alternatively, have unit 17's row name the installed path. Add a plant whose held `/build` row passes the arm.
- **Left-shift gate:** a bug-class checklist entry: "a new arm is run over gov's tree as the sibling held sets leave it".

### H3. Folding `MEMORY_ROOT`/`ROUTED_PATHS` unarms the JS write gate partway through the build (id 19)

**Specs:** PLAY-dConvergedCharter-11

- **Where:** spec 11 §4 "The readers", with S2 and S4.
- **What is wrong:** `scratch-guard.js` reads `MEMORY_ROOT` and `ROUTED_PATHS` straight from `.memory-tree.conf` text (`:1155-1156`, `:1487-1488`). S2 moves both keys out before S4 re-points readers. The spec offers only shell (eval) and Python re-points, with no shape for a node hook. `agent-cap.js`, `format-guard.js` and `procmon-hook.js` read the same homes.
- **Consequence:** the gate reads both keys blank, goes UNARMED, and refuses every Edit/Write in the repository from the next tool call. It fails closed, so the harm is a stalled pass, not an unsafe admit.
- **Fix (judged SOUND):**
  - Add a fourth re-point shape for node hook readers: a committed JSON mirror read with no spawn. Or keep `MEMORY_ROOT` and `ROUTED_PATHS` unfolded as hook-read mechanics.
  - Order S2 so a hook key never leaves its home before its reader is re-pointed.
  - Add a criterion that plants the fold in a scratch clone and observes a routed scratch-guard write still being admitted.
- **Left-shift gate:** have the reader inventory classify readers by language and red any reader class that has no declared re-point shape.

### H4. Unit 20's home-mode step reads `get --explain`, which never names a conf home (ids 22, 32)

**Specs:** PLAY-dConvergedCharter-20 PLAY-dConvergedCharter-11

- **Where:** spec 20 §2 S1 and its by-value readers, and §4 Evidence.
- **What is wrong:** S1 moves a value only where `policy.py get <key> --rev HEAD --explain` names `<home>` as its source, and calls this "unit 11's both-homes reader". Unit 11 puts the home fallback in the separate `legacy` verb (`render_folded_lines`) and never extends `get`/`resolve`. `resolve_read` (`tools/policy/policy.py:749-757`) reads a legacy home only for `AGENTS_PATH`.
- **Consequence:** the up step moves nothing and still strips the folded lines. Every adopter loses its non-default conf values (`BACKLOG_MODE`, `ROUTED_PATHS`, `FAMILIES` and so on). AC1 would probably red on the first build attempt, which forces a redesign at build time.
- **Fix (judged SOUND):**
  - S1 reads a home's assignments with `python policy.py legacy <home> --rev HEAD` (`render_folded_lines`).
  - Each key the home sets to a value different from what `policy.py get <key> --rev HEAD` returns moves through `render_policy_text`.
  - Add a §3 `consumes-from PLAY-dConvergedCharter-11` edge naming `render_folded_lines`, with the reverse edge in unit 11, and correct S1's by-value readers.
  - `fanout_cap.py` keeps its `LOWERED_RE` read.
  - The alternative is for unit 11 to extend `resolve` with a legacy-home fallback and say so in both specs.
- **Left-shift gate:** a spec-token check that every interface a spec cites as a sibling's is a token that sibling defines in its own §2.

### H5. Adopters' committed `.githooks/gate-env.sh` policy keys are silently dropped (id 23)

**Specs:** PLAY-dConvergedCharter-20 PLAY-dConvergedCharter-11

- **Where:** spec 20 §2 S2 ("no descriptor ships it, so no adopter holds it") and §4 Alternatives rejected.
- **What is wrong:** `WIRE-INTO-PROJECT.md:921-936` tells adopters to declare `GATE_DOC_PATHS` and `GATE_POST_MERGE` in their own committed gate file. `pre-push` ships to every push-main adopter (`registry.toml:311-313`). Unit 11 re-points those readers to `policy.py get`, which has no home fallback, and no step moves the adopter's values.
- **Consequence:** after `update`, an adopter's `GATE_POST_MERGE` and `GATE_DOC_PATHS` (and `INHERITED_RED`/`_MAX_AGE`, where set) are ignored with no message. The post-merge mode turns off, and every doc push pays the full bar.
- **Fix (judged SOUND):** Add a `gate/conf-to-policy` step (S1's home mode over `.githooks/gate-env.sh`, owner-policy keys only), declared in the push-main or run-gates descriptor whose hook reads the file. Or have unit 11's shipped readers fall back to the gate file through `legacy` until the step has run. Correct S2 and the rejected alternative.
- **Left-shift gate:** a checklist entry: "a file the runbook tells adopters to write counts as adopter-held, whether or not a descriptor ships it".

### H6. Units 12, 7 and 22 write rows through a door that writes nothing for an agent (id 33)

**Specs:** PLAY-dConvergedCharter-12 PLAY-dConvergedCharter-7 PLAY-dConvergedCharter-22 PLAY-dConvergedCharter-13

- **Where:** spec 12 §2 S1 and Files touched, spec 7 §2 S7, and spec 22 §2 S4.
- **What is wrong:** all three route unit rows through `instructions.edit` / `instructions_edit.py`. Under the default `owner-command-agents-propose` (`catalogue.toml:647-649`), that door only prints a proposal for an agent. Spec 13 §8 F2 already resolved that an agent pass appends the kit row itself and records it through the change record's door.
- **Consequence:**
  - Unit 12 deletes the four UNATTENDED guides with their rationale unwritten, and unit 7's arm grades that loss only at order 17.
  - Unit 22 removes the `[[exempt_leg]]` row while the overlay row was never written, so govkit check 7h reds.
- **Fix (judged SOUND):**
  - In spec 12 S1 and spec 7 S7, write each row by unit 13's route: a kit-manifest edit plus `build_records.py new change`, refused unless `instructions_edit.py check` passes. Cite spec 13 F2 and add the `consumes-from PLAY-dConvergedCharter-13` edge.
  - In spec 22 S4, remove the exempt row only after confirming the overlay holds `leg.adopter.<slug>`. If the door printed a proposal, read the row as `accepted · held` and remove nothing.
  - Add an AC that plants the door printing a proposal and writing nothing.
- **Left-shift gate:** a spec-audit check that every write a spec routes through a guarded door names the door's mode under the default policy.

### H7. Retiring `tools/unattended/` breaks code that resolves the kit by its home name (id 40)

**Specs:** PLAY-dConvergedCharter-12

- **Where:** spec 12 §2 S2 (Readers), §4 Files touched and §7 Gates.
- **What is wrong:** several readers call `resolve_kit_dir … unattended <file>` and are absent from the inventory:
  - `tools/lib/resolve-python.test.sh:168` (`|| exit 2`). Its `kickoff_region` PARITY_ROWS canonical at `:352` is `check-unattended.sh`, which the spec deletes.
  - `tools/memory-tree/deviation_join.py:376`, which reads `GEN_REGION_AWK` from `lib-unattended.sh` and raises Unmeasured at `:400-413` when it is missing.
  - `tools/check-spec-tokens.test.sh:1950` and `tools/run-gates/run-selftests.test.sh:252`, both `|| exit 2`.
  - The drift-audit and runlog selftests, which turn into a permanent SKIP.
- **Consequence:** at the pass commit:
  - The python-resolver and spec-tokens suites die.
  - The deviation join this build's own close uses (`deviations.py --report`) stops measuring.
  - Two arms skip silently, and the skips read as coverage.
- **Fix (judged SOUND):**
  - Add the home-name readers to S2 and §4.
  - Move `GEN_REGION_AWK` and the `kickoff_region` canonical to a surviving home (the runtime kit, or `tools/lib/`) in the same commit.
  - Re-point the four `exit 2` and Unmeasured sites, and retire or re-point the drift-audit and runlog arms.
  - Add `python resolver (behaviour + inline parity + idiom ban)`, `spec-tokens self-test`, `drift-audit selftest` and `runlog selftest` to §7.
  - Add an inventory needle for the bare home `unattended` as passed to `resolve_kit_dir`.
  - On a scratch clone with the kit removed, confirm that `deviations.py --report dConvergedCharter` measures.
- **Left-shift gate:** make `derive_readers` take a kit's home name as a needle whenever it retires a kit.

### H8. Unit 11's `arm_folded_homes` exempts any file that mentions the policy path (id 46)

**Specs:** PLAY-dConvergedCharter-11

- **Where:** spec 11 §2 S5.
- **What is wrong:** a file that spells a folded KEY and its home escapes the arm if it spells `.governance/policy.toml` anywhere, comments included. `check-memory-hygiene.sh` sources `.memory-tree.conf` (`:188`) and names the policy path in a comment (`:618`). 21 home readers escape the same way.
- **Consequence:** if S4's re-point misses a reader, the arm stays green on it. The arm certifies readers it never graded.
- **Fix (finder's proposal REJECTED; skeptic's corrected fix):**
  - Exclude comment lines from the escape.
  - Key the exemption on the read shape for the same home, not on any mention of the policy path.
  - Keep an explicit, named exemption row for by-revision readers that legitimately read the home's history (`transition_audit.read_modes`).
  - Add a fixture: a file that sources a home and mentions `.governance/policy.toml` only in a comment must red.
- **Left-shift gate:** every new arm ships a fixture whose red case contains the arm's escape token in a comment.

### H9. The shell re-point `eval "$(… policy.py legacy <home>)"` swallows reader failure (id 47)

**Specs:** PLAY-dConvergedCharter-11

- **Where:** spec 11 §2 S4 (last bullet) and §5.
- **What is wrong:** when the reader fails (no python, a malformed `policy.toml`, a missing kit), the substitution is empty and eval binds nothing. §5 never prices a reader failure.
- **Consequence:** callers silently run on their built-in defaults. The hygiene engine reads clean under default modes, and `INHERITED_RED` falls back from gov's `land`.
- **Fix (judged SOUND):** Spell the re-point the way `unattended.sh:507` already does: capture the output into a variable, test the exit status, and refuse naming the reader. Never eval a substitution directly. Add a plant that breaks `policy.py` and asserts the reader refuses. Add a §5 line on reader failure.
- **Left-shift gate:** a lint that reds `eval "$(` over a delegate whose exit status is not tested (class swallowed-delegate-reads-as-clean).

### H10. Unit 23 AC5's grep passes bare basenames and matches nothing (id 50)

**Specs:** PLAY-dConvergedCharter-23

- **Where:** spec 23 §6 AC5.
- **What is wrong:** `git grep -n "hashlib.sha256" -- maintain_file.py loop_review.py release.py` matches only at the repo root. The files live in `tools/drift-audit/`, `tools/loop/` and `tools/integrations/`. The single spelling also misses `from hashlib import sha256` and `hashlib.new("sha256")`.
- **Consequence:** the half of AC5 that is meant to show no hash is computed outside the shared block prints nothing, whatever the code holds.
- **Fix (judged SOUND):** Spell the full paths: `git grep -n -E 'sha256' -- tools/drift-audit/maintain_file.py tools/loop/loop_review.py tools/integrations/release.py`. Grade every hit outside a `# >>> derive_key_hash` … `# <<<` span. Stage a red by planting a `hashlib.sha256(` line outside the block in one copy.
- **Left-shift gate:** spec-audit runs each AC command at base and reds a pathspec that matches no tracked file (class rule-stated-with-no-check-that-fails).

## MEDIUM

### M1. Unit 12 moves `check-playbook.sh` but deletes the template it reads (id 3)

- **Where:** spec 12 §2 S2/S3 and §4 "The legs".
- **What is wrong:** `check-playbook.sh:25` reads `$HERE/PLAYBOOK-TEMPLATE.template.md` and exits 2 at `:64` when it is missing. S2's `git rm -r tools/unattended/` removes that template, and no spec-12 line moves it.
- **Consequence:** the `playbook validity gate` leg, which unit 12 keeps, exits 2 after the unit. `memory/guides/PLAYBOOK-TEMPLATE.md` loses its source until unit 7.
- **Fix (judged SOUND):** `git mv` the template and its `[[files]]` row to the runtime kit with the checker, or re-point `TEMPLATE=`. Add it to Files touched and the leg table. Run the leg on a scratch clone with `tools/unattended/` removed.
- **Left-shift gate:** when a script moves, the reader inventory lists the files it opens relative to `$HERE`.

### M2. No unit owns closing a shim row (id 4)

- **Where:** spec 20 §3 Non-goals, against spec 17 §3, spec 9 S5 and spec 12 S2.
- **What is wrong:** units 17, 9 and 12 hand the close to unit 20. Unit 20 says closing belongs to the owning unit, and S4 only reds an open row.
- **Consequence:** "removed once the window closes" has no owner. S4 will eventually red with no named change to clear it.
- **Fix (judged SOUND):** Pick one owner and write it the same way in all four specs. For example, unit 20 S4's red names the owning unit and a release-bound follow-through record, and units 9, 12 and 17 stop saying unit 20 closes their rows. Or unit 20 owns a close verb under `install.deprecation-window`.
- **Left-shift gate:** the spec brief's edge-pair check reds a duty that each side assigns to the other.

### M3. The run conf's `_EXTRA` keys get contradictory rules across units 11, 12, 20 and 22 (id 6)

- **Where:** spec 11 §2 S1/S2 and §4 Evidence (107 folded keys), against spec 20 S3/AC4 and spec 22 S5.
- **What is wrong:**
  - Unit 11 folds all 53 `.unattended.conf` rows, the six `_EXTRA`/`_EXTRA_TABLE` extension keys included.
  - Unit 20 defines its dropped keys as ones "the catalogue does not carry", and its AC4 reds if an extension key moves into the policy file.
  - Unit 22 treats those keys as leaving with the kit.
  - Unit 12 (order 4) removes the `unattended.*` catalogue rows before unit 20 (order 7) reads them.
- **Consequence:** AC4 contradicts its siblings whichever reading holds. After unit 12, `derive_home_folds('.unattended.conf')` maps no key at all.
- **Fix (finder's proposal REJECTED; skeptic's corrected fix):**
  - Do both of the following, not one.
  - Exclude the `_EXTRA` and `_EXTRA_TABLE` keys from unit 11's fold, so the 107 becomes 101 and they stay in `legacy-homes.txt` as unit 22's leaves-with rows.
  - Have unit 20's `unattended/run-conf-retired` step read a key map pinned in the step for the folded `.unattended.conf` keys, or have unit 12 keep their catalogue rows until unit 20's window closes.
  - Align AC4's fixture to that rule.
- **Left-shift gate:** a checklist entry: "a key population that two units read at different orders is pinned at one of them".

### M4. Unit 11 AC8 expects a folded key to print nothing (id 7)

- **Where:** spec 11 §6 AC8, against §2 S3.
- **What is wrong:** S3 says `legacy` prints the policy file's value for a key whose `legacy` names the home. S2 writes gov's `INHERITED_RED=land` into the policy file. AC8 expects `legacy .githooks/gate-env.sh --key INHERITED_RED` to print nothing.
- **Consequence:** AC8 reds on a correct build. Making it pass breaks S3's contract.
- **Fix (judged SOUND):** AC8 expects `land` at `--rev HEAD`. Add a case at a pre-fold commit that prints the gate file's line.
- **Left-shift gate:** spec-audit derives each AC's expected output from the S-clause it cites.

### M5. Unit 11 AC8's mechanic case names a key gov never assigns (id 21)

- **Where:** spec 11 §6 AC8 and §2 S2 ("its six mechanic keys").
- **What is wrong:** `.githooks/gate-env.sh` assigns only `GOV_KITROOT` (`:90`) and `GATE_WSL_MIRROR_DEFAULT` (`:113`). `GOV_PYTHON` appears only in the comment at `:55`.
- **Consequence:** AC8's positive half prints nothing, or passes on an empty line. In either case it certifies nothing.
- **Fix (judged SOUND):** Point AC8 at `GOV_KITROOT` or `GATE_WSL_MIRROR_DEFAULT`, or at a fixture that assigns `GOV_PYTHON`. Reword S2 to "the mechanic keys it assigns".
- **Left-shift gate:** `legacy-homes.txt` harvesting reds a row whose key is only commented in its home.

### M6. Unit 11 AC6 and unit 12 P3 cannot exit 0 while `read_policy_key` stays spelled (id 8)

- **Where:** spec 11 §6 AC6, and spec 12 §2 P3.
- **What is wrong:** `derive_readers` counts comments and docs. `read_policy_key` remains in `tools/policy/policy.py` (`:25`, the `:1138` `POLICY_KEY_READ` regex, the `:1199` docstring) and in `tools/policy/README.md:155`, and neither S4 nor S7 changes them.
- **Consequence:** AC6 cannot pass, and unit 12's precondition stays red, which blocks unit 12.
- **Fix (judged SOUND):** Retire `POLICY_KEY_READ`/`scan_gate_readers`' `read_policy_key` shape and README:155 in S4/S7 and list them as readers. Or name them as `--except` paths in AC6 and P3 with the reason.
- **Left-shift gate:** spec-audit runs each "exits 0 over gov's tree" AC against the post-change Files touched set.

### M7. Unit 11 §7 hand-names gates and leaves out the legs of the files it edits (id 9)

- **Where:** spec 11 §7 Gates.
- **What is wrong:** S4 edits `.githooks/pre-push`, `push-main.sh`, `post-merge.sh`, `held_halves.py` and their tests. §7 omits `pre-push self-test`, `pre-push bar self-test`, `push-main self-test` and `held-halves selftest`, while declaring a New arm in `pre-push.test.sh`.
- **Consequence:** the unit can be green on its named legs and red on the bar.
- **Fix (judged SOUND):** Derive §7 from `tools/gate-legs.json` for every path in Files touched, or at least add the four legs. Or state that the pass runs the full bar.
- **Left-shift gate:** a spec-token check that §7 contains every leg whose guard admits a Files-touched path (class hand-named-gate-list-green-while-the-bar-reds).

### M8. Unit 21 AC6 needs an edit to `settings_census.py` that its Files touched omits (id 10)

- **Where:** spec 21 §2 S4 and Files touched, against §6 AC6.
- **What is wrong:** unit 22 (order 1) creates `tools/govkit/settings_census.py`, which calls `load_policy`. Unit 21 S4 says that population "leaves with the file", but the file is not in Files touched. AC6 requires `git grep -n load_policy` over `tools/` to print nothing.
- **Consequence:** either AC6 reds, or the builder writes outside its declared `--writes` set.
- **Fix (judged SOUND):** Add `tools/govkit/settings_census.py` to Files touched and to S4's by-name readers. Say what the census prints once the seed is gone, for example one "house file retired" line rather than an empty population.
- **Left-shift gate:** the spec brief cross-checks each unit's readers against files that earlier units in the build order create.

### M9. Unit 11's `arm_house_readers` reds the migrator and the readers unit 21 must keep (ids 42, 49)

- **Where:** spec 21 §2 S1, §6 AC6 and §7 New arm, with spec 11 §2 S8.
- **What is wrong:**
  - Once the seed is gone, S8 reds every file other than `roles_lib.py` that spells `house/policy.toml`.
  - Unit 21's step `tools/govkit/steps/house_seed.py`, its selftest plants, `render_agents.py`'s fixture and `tools/playbook/adopt_declarations.py` (`derive_house_proposals`) must all spell that path.
  - `tools/govkit/selftest.py:9581` and `tools/policy/README.md:149-157`, `:385` also spell it, and the README still describes the house file as a legacy home.
- **Consequence:** AC6 conflicts with S1, and the landing reds on the migrator. The alternative is that the builder builds the path from fragments, which blinds the arm.
- **Fix:**
  - id 42 (judged SOUND):
    - Have spec 21 require an exemption list in unit 11's arm and state it in AC6. Or file an ask on unit 11 to scope the arm to shipped call shapes and exclude `govkit/steps`.
    - Add `tools/policy/README.md` (`:149-157`, `:385`, `:522-527`) and the `selftest.py:9581` comment to S4's readers and §4.
    - Run AC6's arm over the tip with `house_seed.py` present.
  - id 49 (finder's proposal REJECTED; skeptic's corrected fix):
    - Declare the exempt set once and use it in both AC6 (`--except` on each path) and unit 11 S8.
    - The set is `tools/govkit/steps/house_seed.py`, `tools/playbook/adopt_declarations.py` (`derive_house_proposals`) and the selftest file holding their plants.
    - Require each of these to spell `house/policy.toml` literally, so the inventory still sees them.
    - Add a plant that puts the spelling in a non-exempt file and asserts the arm reds.
- **Left-shift gate:** a checklist entry: "a single-reader arm names the migrators that must outlive the seed".

### M10. Unit 14's adopter exit arm disagrees with unit 20's definition (id 11)

- **Where:** spec 14 §2 S7, against spec 20 S5.
- **What is wrong:**
  - Spec 14 runs `derive_pending_steps` per registered adopter with no release.
  - Spec 20 grades every register row through `derive_migration_state` at a required `--release`.
  - Spec 5 exits 2 "not graded" until a release tag exists.
- **Consequence:** `fates_join.py check --exit` has no release argument and no rule for folding exit 2. Before a release is cut, its adopter half is ungraded with no stated outcome.
- **Fix (judged SOUND):** Describe the arm as unit 20 does. State where `check --exit` gets the release, and that an adopter-arm exit 2 makes the exit check "not graded" rather than green.
- **Left-shift gate:** a spec-token check that a shared interface is described with the same signature in every spec that calls it.

### M11. Who removes `PLAYBOOK-TEMPLATE.md` and `SESSION-KICKOFF.md` is stated three ways (id 12)

- **Where:** spec 7 §2 S8 and §4 "The guides", against spec 1 §4 Evidence and spec 19 §2.
- **What is wrong:**
  - Unit 7 (order 17) removes `PLAYBOOK-TEMPLATE.md` and moves `SESSION-KICKOFF.md`.
  - Unit 1 says units 12 and 16 remove both files first.
  - Unit 19 says unit 12 retires `PLAYBOOK-TEMPLATE.md`. Unit 19 does include `SESSION-KICKOFF.md` in its population, so it is wrong on one file only.
- **Consequence:** both files remain tracked from order 12 to 17, and units 1 and 19 never grade them.
- **Fix (judged SOUND):** Fix one owner per guide in units 1 and 19 to match unit 7's table. Include both files in those units' populations, or state why they are exempt.
- **Left-shift gate:** the spec brief's owned-node table reds a file that two units claim to retire, or that a unit says another retires.

### M12. Spec 19's covered-pin arm reds the instance pins S6 keeps (ids 13, 26, 51)

- **Where:** spec 19 §2 S5, S6, S7 and §4 "The pins after".
- **What is wrong:**
  - S5 adds `*.conf` and `*.example text eol=lf` to gov's `.gitattributes`, and git's match covers dot-led basenames.
  - S6 keeps `.codebase-map.conf`, `.memory-tree.conf`, `.process-monitor.conf` and `.memory-tree.conf.example` as instances "no class covers" (`codebase-map/kit.toml:141`, `memory-tree/kit.toml:366`, `:369`, `process-monitor/kit.toml:107`).
  - S7 reds any pin a class line covers but never says which class set it grades against.
  - `.process-monitor.conf` is deleted by unit 11.
  - `{playbook_path}` (`playbook.kit.toml:65`) is in neither rule.
- **Consequence:** `check_covered_pins` reds gov's own descriptors at landing. The builder must silently choose S6 or S7, and AC6 is ill-defined.
- **Fix (judged SOUND):**
  - State that S7 grades a kit's `[[lf_pin]]` only against the class rows the kits declare (`*.md`, `*.txt`, `*.toml`, `*.sh`, `*.js`, `*.json`), never gov's `.gitattributes` class lines. Or retire the conf and example instances into `*.conf` and `*.example` class rows.
  - Drop `.process-monitor.conf` from S6.
  - Resolve placeholder tokens (`{kit}`, `{prefix}`, `{playbook_path}`, `{memory_root}`) before taking an extension, and place `{playbook_path}` in S6 or the class conversion.
  - Add plants for a root-conf pin and a placeholder pin.
- **Left-shift gate:** spec-audit runs each new arm over the after-state the same spec's S-clauses produce.

### M13. Unit 3 S5 edits a landed step program that `check_frozen` guards (id 14)

- **Where:** spec 3 §2 S5 and §7 Gates.
- **What is wrong:** S5 edits `tools/govkit/steps/memory_journal_alias.py`, the program of the landed `[[upgrade]]` row `memory-tree/serves-journal-read-as-log`. `check_frozen` (`upgrade_steps.py:1038-1041`) reds any byte change to such a program, even when the argv is kept. §7 omits `step-rows-frozen` and `upgrade-walk`. The clash bites only if dTotalRecall lands without ask A1.
- **Consequence:** the step-rows-frozen leg reds, and the unit's hand-named gates never run it.
- **Fix (judged SOUND):** Ship the pair-taking program as a new file named by the new `[[upgrade]]` rows, leaving the landed bytes unchanged. Or make the edit conditional on ask A1 landing in dTotalRecall-20 first. Add `step-rows-frozen` and `upgrade-walk` to §7.
- **Left-shift gate:** spec-audit reds a Files-touched path that a landed `[[upgrade]]` row names.

### M14. Unit 9 S2's reader inventory omits gov's receipt rows (id 15)

- **Where:** spec 9 §2 S2 Readers.
- **What is wrong:** the list misses `.governance/install.json` (`:164`, `:566`, `:770`, `:812`) and the `.gitattributes` lines (`:282`, `:286`), and it asserts "NO VALUE READERS". Unit 19 may remove the `.gitattributes` lines first, but the receipt rows are a real omission.
- **Consequence:** gov's receipt keeps rows for files that no longer exist.
- **Fix (judged SOUND):** Add the receipt rows and the `.gitattributes` template lines to S2's by-name readers, derived with `derive_readers <path> --kind path`.
- **Left-shift gate:** a retirement spec's reader list must be the printed output of `derive_readers`, never typed (class retirement-inventory-misses-readers-by-value).

### M15. `post-merge.sh` cannot read `GOV_PYTHON` through a python reader (id 20)

- **Where:** spec 11 §2 S4 (first bullet), §4 Evidence (post-merge's three keys) and §8 F3.
- **What is wrong:** S4 re-points every `read_policy_key` copy "under the inline `resolve_kit_dir` pre-push:806-830 already carries". `post-merge.sh` carries no resolver ("sources no kit", `:170`). One of its keys, `GOV_PYTHON` (`:231`), is the interpreter the reader would need.
- **Consequence:** the copy cannot be deleted as written. On a host where only `GOV_PYTHON` names a working python, post-merge either runs its bar without it or refuses.
- **Fix (judged SOUND):** State that `post-merge.sh` gains the inlined `resolve_python` and `resolve_kit_dir` blocks under PARITY_ROWS. Keep `GOV_PYTHON`, and arguably every mechanic key post-merge reads, on a pure-shell parse of the gate file at `<sha>`. If one copy must stay, record that as a departure.
- **Left-shift gate:** a checklist entry: "a key that names the interpreter is never read through that interpreter".

### M16. Unit 12's inventory misses readers that name the kit by its entry id (id 24)

- **Where:** spec 12 §4 Evidence, §2 S2 by-value needles and §6 AC2.
- **What is wrong:** the needles are path-shaped only. They miss:
  - `.governance/deploy.toml:20` (the selection `"unattended"`).
  - `tools/lib/render-doc.sh:217` and `tools/memory-tree/adopt-memory-tree.sh:439` (`rendered_at("unattended", "PROTOCOL.template.md")` behind `{{UNATTENDED_PROTOCOL}}`).
  - `tools/memory-tree/kit.toml:71`.
- **Consequence:** AC2 exits 0 while the deploy selection names a removed entry, and the rendered method points at "the unattended-run protocol of this repo", which no longer exists.
- **Fix (judged SOUND):** Add `'"unattended"'` as a quoted-token needle and the `{{UNATTENDED_PROTOCOL}}` token. Name the three files in S2. Extend AC2 with a planted `"unattended"` selection row that must red.
- **Left-shift gate:** same as H7. A kit retirement inventory always includes the kit's entry id and placeholder tokens.

### M17. Unit 6's census leaves 33 tracked memory files with no home (id 25)

- **Where:** spec 6 §4 "The census".
- **What is wrong:** the rows sum to 10,501, but `git ls-files memory` lists 10,534. The gap includes 21 `memory/builds/*/spec/units/*.md` specs and 38 non-script data files under `build/` (tsv, json, log, out, txt, svg, html).
- **Consequence:** AC2's "0 unregistered" meets homes that no row owns. The builder either stalls or widens a glob to `**`.
- **Fix (judged SOUND):** Re-run the census grouped by full shape (depth and extension). Add rows for `memory/builds/*/spec/units/*.md` and for the build data files. Pin the total so the table's sum is checked against the listing.
- **Left-shift gate:** a census table carries a checked total equal to its source listing's count.

### M18. Unit 7's deletion walk pulls the moved `SESSION-KICKOFF.md` into the graded population (id 27)

- **Where:** spec 7 §2 S6, against S8.
- **What is wrong:** `git log --diff-filter=D -M -- 'memory/guides/*'` cannot pair a rename whose destination lies outside the pathspec. S8's move to `memory/project/` therefore reports as `D`, which a scratch repo reproduced.
- **Consequence:** `check_rationale_kept` reds every `SESSION-KICKOFF.md` section at the unit's own tip, or the builder hand-exempts the file.
- **Fix (judged SOUND):** Walk without a pathspec and filter to `memory/guides/` afterwards, or give both the old and new paths in the pathspec. Add a plant that moves a guide out and expects it ungraded.
- **Left-shift gate:** a checklist entry: "a `--diff-filter=D` walk with a pathspec misreports moves out of the pathspec".

### M19. Unit 7 S7 names the dossier mover instead of the guide mover (id 34)

- **Where:** spec 7 §2 S7 and §3 Edges.
- **What is wrong:** S7 and the edge consume `dossier_move.py`, whose route sends `seam:` lines to proposals and other sections to records. Unit 13 builds the factory `tools/lib/prose_move.py` and the guide caller `tools/playbook/guide_move.py`.
- **Consequence:** guide rationale lands as dossier proposals and records, not where S6's `explains=` arm looks, or a builder writes a third mover.
- **Fix (judged SOUND):** Name `tools/playbook/guide_move.py plan|apply` in S7 and §10. Route `help` and `explains=` through a rationale route of `prose_move.py`, or through a `--rationale` route unit 7 adds to `guide_move.py`. Change the edge token, and have unit 13 declare the reverse edge.
- **Left-shift gate:** same as H4. Edge tokens must resolve to the sibling's own defined interface.

### M20. Unit 11 S5 and S8 build two more single-reader scanners beside `arm_single_reader` (id 35)

- **Where:** spec 11 §2 S5 and S8, and §10.
- **What is wrong:** `tools/policy/check_policy.py:631-656` already implements `arm_single_reader`. It is comment- and docstring-aware, matches `READ_SHAPE`, and is used by two ARMS rows. S5 and S8 each define a raw-spelling scanner, and §10 cites neither existing seam.
- **Consequence:** there are three scanners with different false-red and false-green rules. S8 reds a comment that the existing arm would not.
- **Fix (finder's proposal REJECTED; skeptic's corrected fix):**
  - S8: extend `arm_single_reader` to take an excluded-file set, and add one ARMS row for the house file with `tools/roles/roles_lib.py` as its one reader and `const="load_policy"`, armed only once the seed is absent.
  - S5: keep the conjunction of a folded KEY and its home path, without the adapter shapes. Run it through the same comment- and docstring-skipping helpers (`COMMENT_LEADS`, `derive_docstring_lines`) and `READ_SHAPE`-style read detection, not a raw spelling scan.
  - Cite `arm_single_reader` and `READ_SHAPE` in §10.
- **Left-shift gate:** the reuse scout's brief lists existing ARMS predicates, and a spec that adds an arm cites one or says why none fits.

### M21. Unit 6's residue arm duplicates hygiene check 3's home allowlist (id 37)

- **Where:** spec 6 §2 S1 and §10.
- **What is wrong:** `tools/memory-tree/check-memory-hygiene.sh:882-975` (check 3) already reds memory-tree paths outside a declared set, with `PROJECT_REGISTRY_EXTRA` as the adopter widening. S1 builds a second allowlist from `record-kinds.toml` `home` globs, and §10 does not cite check 3.
- **Consequence:** a new home must be declared twice. A non-`.txt` `PROJECT_REGISTRY_EXTRA` entry, or a new root directory, passes one arm and reds the other.
- **Fix (judged SOUND):** Name check 3 in §10. Then either derive check 3's sets from the registry's `home` cells, or state in §4 which arm owns which part of the tree and how `PROJECT_REGISTRY_EXTRA` maps to a row. Add an AC that plants an extra registry and sees both arms agree.
- **Left-shift gate:** same as M20. An arm over a population an existing arm grades must name that arm.

### M22. Unit 2 adds a second home-glob matcher in `positional.py` (id 38)

- **Where:** spec 2 §2 S1 and §4 Inventory (`--homes`).
- **What is wrong:** `derive_positional_class` matches the `home` globs printed by a new `record_kinds.py --homes` itself. Spec 6 S1 and TOOL-dCalibratedLens-33 require one home-match predicate and no second glob dialect.
- **Consequence:** where the two dialects differ (`*` crossing `/`, a `**` home), a live path reads as frozen and S3's live-row arm stays green on it.
- **Fix (judged SOUND):** Replace `--homes` with a classifier mode, for example `python record_kinds.py --lifecycle <path>...` printing `<path>\t<lifecycle>` through unit 6's predicate. `derive_positional_class` matches no globs itself. Add an AC with a `**` home (class decision-re-derived-by-a-second-process).
- **Left-shift gate:** a lint that reds `fnmatch`/glob matching of `home` cells outside the one predicate.

### M23. Unit 12 ignores the live carriers under the memory root (id 41)

- **Where:** spec 12 §4 Evidence ("Outside it and the memory root") and §7 Gates.
- **What is wrong:** `check-dead-paths.sh:57-62` grades `memory/map/features/*` and `memory/gotchas/*` as live carriers. 42 of those files name `unattended.sh`, `check-unattended.sh` or `lib-unattended.sh`. `memory/map/features/unattended.md` claims the kit, its hooks, legs, Skill and guides.
- **Consequence:** at the pass commit:
  - The dead-path leg reds.
  - The dossier's claims go STALE, so codebase-map coverage reds.
  - The generated map files go stale.
- **Fix (judged SOUND):** Add the dossiers (`unattended.md`, `unattended-mandate.md`, `unattended-stops.md`, `agent-cap.md`, `playbook-mode.md`) and the gotcha pages, derived by `bash tools/check-dead-paths.sh --list` on a scratch clone with the kit removed, to §4. Add the regenerated `memory/map/generated/*`. Add `dead-path carriers (deleted files still named)` and `codebase-map coverage + freshness` to §7.
- **Left-shift gate:** covered by M26's fix: `derive_readers` includes the live carriers.

### M24. Unit 16's hook move leaves a stale codebase-map claim (id 43)

- **Where:** spec 16 §2 S3 (Readers), §4 Files touched and §7 Gates.
- **What is wrong:** re-pointing the SessionStart hook changes the `harness-hooks` key that `memory/map/features/session-kickoff.md:14` claims. Other carriers are also outside the inventory's reach:
  - `build-method.md:85`, `playbook.md:60` and `testsuite-counts.md:97`.
  - The gotcha `shipped-checker-edit-is-an-adopter-contract-change.md` and four others.
- **Consequence:** STALE CLAIM plus UNCLAIMED key, so `codebase-map coverage + freshness` reds and the generated map goes stale.
- **Fix (judged SOUND):** Add `session-kickoff.md` (its harness-hooks claim and paths globs), the other dossiers that spell the old path, and the regenerated `memory/map/generated/*` to §4. Add `codebase-map coverage + freshness` to §7.
- **Left-shift gate:** same as M23.

### M25. Unit 9's five new Skills mint unclaimed codebase-map keys (id 44)

- **Where:** spec 9 §4 Files touched, §7 Gates and AC7.
- **What is wrong:** rendering `.claude/skills/gov-*/SKILL.md` adds five `rendered-skills` keys. The dossiers claim the old names, and the shrink-only baseline cannot gain `gov-drift`. AC7 excludes `:!memory`.
- **Consequence:** `codebase-map coverage + freshness` reds with UNCLAIMED gov-recall, gov-runlog, gov-lexicon, gov-drift and gov-cleanup.
- **Fix (judged SOUND):** Add the dossier claims (`memory-recall.md`, `runlog.md`, `lexicon.md`, `branch-reconcile.md`, and a new dossier for gov-drift) and the regenerated `memory/map/generated/*` to §4. Add `codebase-map coverage + freshness` to §7.
- **Left-shift gate:** same as M23.

### M26. `derive_readers` (shared interface I1) excludes the memory root's live carriers (id 45)

- **Where:** spec 11 §2 S6.
- **What is wrong:** the walk covers "every tracked text file outside the memory root". `memory/map/features/*` and `memory/gotchas/*` are graded as live by the dead-path and codebase-map legs. Units 9, 12, 16, 17 and 21 treat a clean exit as a complete inventory.
- **Consequence:** retiring units' ACs pass while live carriers still name the retired path. This is the root of M23, M24 and M25.
- **Fix (finder's proposal REJECTED; skeptic's corrected fix):**
  - Keep the memory root excluded, except the live carriers `check-dead-paths.sh` grades.
  - By default, include `memory/map/features/*` and `memory/gotchas/*`, read from one shared list with `check-dead-paths.sh` rather than a typed copy.
  - Change AC6's red-when to "a reader under the memory root outside those carriers is named".
  - Add a fixture that plants a path reader in `memory/map/features/x.md` and expects it returned.
- **Left-shift gate:** the shared carrier list itself. A single source keeps the inventory and the dead-path leg in step.

### M27. Unit 21's house-seed step writes a below-floor effort with no owner act (id 48)

- **Where:** spec 21 §2 S1 step (3), §4 "The fold" and §5 security.
- **What is wrong:** every unruled house effort is written into `roles.effort.*`, including levels below `medium`. DEPL-dShippedRelease-28 S5 allows those only under `policy-file.guard` at `owner-only`. An adopter holding one is already red under R12, which narrows the path.
- **Consequence:** an automated step lands a below-floor effort with no owner act, or `check_effort_floor` reds after the house file is deleted.
- **Fix (judged SOUND):** Add a "below the floor" row to "The fold". Treat it like an unruled grant: stop the up step writing nothing and name the key and the `--rule` command, or follow DEPL-28 S5's `held: policy-file.guard is <value>`. Add an AC that plants `gov-skeptic = "low"` and asserts both files stay byte-identical.
- **Left-shift gate:** a checklist entry: "a migration that writes a guarded value states the guard it writes under".

### M28. Unit 22's `--apply` makes two writes with no failure order (id 53)

- **Where:** spec 22 §2 S4 (`--apply` for a leg) and §5.
- **What is wrong:** the overlay `[[gate-leg]]` row is written through the door, then the `[[exempt_leg]]` row is removed from `tools/govkit/registry.toml` "in the same act". No rollback is stated.
- **Consequence:** a half-applied state, most likely a leg that is both overlay-claimed and exempt. The census reads it as `owed` or `moved`, and the "neither" state is the one check 7h fails.
- **Fix (finder's proposal REJECTED; skeptic's corrected fix):**
  - Take before-images of both `.governance/instructions.toml` and `tools/govkit/registry.toml`.
  - Write the overlay row through the door, then remove the exempt row.
  - On any failure, restore both before-images byte for byte (TOOL-dSafePassage-1's helpers) and exit 2 naming the step that failed.
  - Add a plant that fails the registry write and asserts both files are byte-identical.
- **Left-shift gate:** a checklist entry: "a multi-file write states its before-images and restore".

### M29. Unit 3's merge-evidence window is anchored on the wall clock (id 54)

- **Where:** spec 3 §2 S1-S3.
- **What is wrong:** S1 says the window ends "at the commit measured". S2 walks `git log --since=<since>`, and `check_merge_evidence(root)` takes no `since`.
- **Consequence:** the record-kinds leg's verdict at a fixed SHA changes with the run date, so a CI re-run can flip. A guarded or cached leg keeps a stale verdict.
- **Fix (judged SOUND):** Derive `since` as the committer date of the commit being graded (HEAD, or the merge-base for a branch) minus 30 days, passed explicitly. State in S3 that the leg has no path guard, or one that admits every memory-root commit.
- **Left-shift gate:** a lint that reds `--since=` in a gate leg unless it is derived from a commit date.

### M30. Unit 9's rename step byte-compares where its precedent recognises (id 55)

- **Where:** spec 9 §2 S4 (`skill_rename.py` UP) and §5.
- **What is wrong:** the old Skill is withdrawn only where its bytes equal the old kit's render. The cited precedent, `adopt-branch-reconcile.sh:104-115`, strips CRs and recognises the render by `name:` front matter plus the CLI name.
- **Consequence:** CRLF copies, older renders and renders with other answers are kept as "hand-edited". The step reads applied, the old Skill stays beside `gov-<new>`, and S5's forwarder collides with it.
- **Fix (judged SOUND):** Define the render by the precedent's recognition test, with CRs stripped. Add plant variants with a CRLF copy and one rendered from an older template, and assert both are withdrawn.
- **Left-shift gate:** spec-audit checks that a cited precedent actually does what the spec says it does.

### M31. Unit 11's `legacy` parser defines no grammar for a sourced home's lines (id 56)

- **Where:** spec 11 §2 S3 (`render_folded_lines`) and §4 Migration.
- **What is wrong:** the parser prints "the home's own last KEY= line". Adopter homes were sourced, so they may hold `export KEY=`, `$VAR`/`$(…)` expansions, multi-line quoted values, continuations or CRLF.
- **Consequence:** adopters read different values than before, which contradicts §4's "reads exactly what it read before".
- **Fix (judged SOUND):** State the accepted grammar: plain `KEY=value` or `KEY="value"` on one line. Have `legacy` refuse, naming file and line, any assignment outside it (`export`, expansion, an unterminated quote). Add plants for an `export KEY=` line and an unterminated multi-line value.
- **Left-shift gate:** a checklist entry: "replacing `source` with a parser states the grammar and refuses everything outside it".

## LOW

### L1. Unit 20 S3 cites the wrong `update` arm (id 5)

- **Where:** spec 20 §2 S3, against spec 12 §8 F4.
- **What is wrong:** S3 cites "update's withdrawn arm for a claim retired to `none`". Unit 12 sets the successor to `runtime`. The files still leave, because `govkit.py:9547-9565` carries the rows and the grid (`:8286`) reads them `withdrawn`.
- **Consequence:** a wrong citation only. The skeptic graded it low because behaviour is unaffected.
- **Fix (judged SOUND):** Align the citation with the carried-claim path, or have unit 12 take successor `none`. Add an AC4 case asserting the adopter's `tools/unattended/` files are gone after `update`.
- **Left-shift gate:** same as H4.

### L2. Unit 20 misstates the `legacy-homes.txt` counts (ids 16, 28)

- **Where:** spec 20 §2 S3 Readers (`:77`, "45 `.unattended.conf` rows") and §4 Evidence (`:134`, "116 rows across six homes").
- **What is wrong:** the list holds 115 rows across seven homes, 53 of them `.unattended.conf`. Spec 11 states these figures correctly.
- **Consequence:** a builder pinning 45 misses eight readers, and the spec set gives two answers to one question.
- **Fix (judged SOUND):** Restate as 115 rows across seven homes and 53 `.unattended.conf` rows, or cite unit 11's figures, or mark them DERIVED by `grep -c`.
- **Left-shift gate:** pinned figures carry their command, and spec-audit re-runs it (class two-answers-to-one-question).

### L3. Unit 17 AC6's grep already prints lines at base (id 17)

- **Where:** spec 17 §6 AC6.
- **What is wrong:** `grep -nE 'skill|held' shims.md` already matches "held" at `:16`, `:44` and `:48` today.
- **Consequence:** the AC can read green before S5 is written.
- **Fix (judged SOUND):** Grep for the new kind specifically (``grep -n '`skill`' shims.md`` or `grep -n 'kind = "skill"'`) and confirm it prints nothing at base.
- **Left-shift gate:** spec-audit runs each AC at base and requires the red half to be red (class fixture-passes-by-finding-nothing).

### L4. Unit 3 S4 cites `derive_readers` at the wrong section (id 18)

- **Where:** spec 3 §2 S4.
- **What is wrong:** S4 cites "PLAY-dConvergedCharter-11 S1". The function is defined in S6 (I1).
- **Consequence:** a misleading address for a shared interface.
- **Fix (judged SOUND):** Cite "PLAY-dConvergedCharter-11 S6 (I1)".
- **Left-shift gate:** a spec-token check that an `<unit> S<n>` citation's section defines the cited token.

### L5. Unit 19's `eol=lf` counts are off by one (id 29)

- **Where:** spec 19 §4 Evidence and §10.
- **What is wrong:** base holds 78 `eol=lf` lines, one of them a comment (`:72`), so 77 pins. The spec says 79 and 78, and wrongly "corrects" scout A's correct 78.
- **Consequence:** wrong evidence only. AC5 pins its own after-state figure.
- **Fix (judged SOUND):** Restate as 78 lines and 77 pins, and drop the scout correction.
- **Left-shift gate:** same as L2.

### L6. Unit 11's pinned reader counts do not reproduce (id 30)

- **Where:** spec 11 §4 Evidence ("72 … 31 … 15, PINNED by git grep -l").
- **What is wrong:** no reading of "tracked code files outside the memory root" yields 72/31/15.
- **Consequence:** the build has no baseline to check its derived re-point population against.
- **Fix (judged SOUND):** Re-pin with the exact command, for example `git grep -lF <home> -- '*.js' '*.mjs' '*.cjs' '*.py' '*.sh' '.githooks/*' ':!memory' | wc -l`, or drop the figures.
- **Left-shift gate:** same as L2.

### L7. Unit 7 misstates the guides' size (id 31)

- **Where:** spec 7 §4 Evidence ("301 KB").
- **What is wrong:** the ten guides hold 317,842 bytes, which agrees with spec 13's total.
- **Consequence:** cosmetic.
- **Fix (judged SOUND):** Restate as 317,842 bytes (`wc -c`).
- **Left-shift gate:** same as L2.

### L8. Unit 9's rename step re-derives `update`'s withdrawal grid (id 36)

- **Where:** spec 9 §2 S4 and §4 Migration.
- **What is wrong:** the UP's byte test re-derives `VERDICT_GRID`'s `withdrawn` and `retired-edited` cells (`govkit.py:8283-8292`). Spec 20 §4 rejects the same design, and spec 9 does not say why its case differs.
- **Consequence:** the decision is made a second time, and it is contained: only unedited renders go, and a shim forwarder replaces them.
- **Fix (finder's proposal REJECTED; skeptic's corrected fix):** Keep the UP clearing the old path, since the S5 forwarder re-occupies it. Have it decide with govkit's own classification of the old `[[files]]` row (`VERDICT_GRID`: delete only on `withdrawn`, keep and name on `retired-edited`), not its own byte comparison. In §4 alternatives, state why this case differs from spec 20 §4's rejection: the path is replaced by a forwarder, not left empty. Cite `VERDICT_GRID` in §10.
- **Left-shift gate:** same as M20. Cite the existing classifier or say why none fits.

### L9. Unit 22's census duplicates govkit check 7h's red (id 39)

- **Where:** spec 22 §2 S2, §4 The states (`undeclared`) and AC2.
- **What is wrong:** `settings_census.py --check` exits 1 on a leg that no descriptor or `[[exempt_leg]]` covers, which check 7h (`govkit.py:2689-2690`) already reds.
- **Consequence:** two reds with two remedy texts for one fact.
- **Fix (judged SOUND):** Report the row as "undeclared · govkit selfcheck 7h reds it" with `--check` exit 0. Or drop `undeclared` from `--check` and have AC2 observe the printed row.
- **Left-shift gate:** same as M20.

review-shape kind=spec-audit round=1 intensity=full at=synth raw=56 confirmed=55 refuted=1 unverified=0 blocker=0 high=11 medium=34 low=10 agents=11 out-tokens=286394

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes |
|---|---|---|---|---|---|---|---|---|
| 1 | coherence | memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-9.md:section 6 AC2 | high | high | confirmed | I ran `git ls-files -- tools \| grep SKILL.template.md`. It printed 7 paths, including tools/roles/SKILL.template.md. Spec-9:215-216 AC2 says the count prints 0, with '/build's ... with units 17'. Spec-17 S4:72 keeps `tools/roles/SKILL.template.md` in the held set 'until the row closes', and spec-17:83-85 says no window can close inside this build. A correct build therefore leaves the count at 1, and AC2 can only turn green if the builder deletes the held client. | sound | - |
| 2 | coherence | memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-9.md:section 2 S7 (check_skill_paths), against unit 17 S3/S4 | high | high | confirmed | `git grep '\.claude/skills/' -- '*kit.toml'` prints tools/roles/kit.toml:57 `to`, :90 `probe` and :145 `pattern`, all naming `.claude/skills/build/SKILL.md`. Spec-9 S7 (:82-87) admits a path only when it is a `[[drive]]` skill directory or the `from` of an open skill shim. Spec-17 S3 sets that row's `from` to `{prefix}/roles/SKILL.template.md`, not the installed path, and S4 keeps the roles kit's install row, probe and lf_pin in the held set. The arm therefore reds gov's tree. | sound | - |
| 3 | coherence | memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-12.md:section 2 S2/S3 and section 4 'The legs' | high | medium | confirmed | In tools/unattended/check-playbook.sh, :25 sets `TEMPLATE="$HERE/PLAYBOOK-TEMPLATE.template.md"` and :64 exits 2 when that file is missing. `git ls-files` shows the template only at tools/unattended/PLAYBOOK-TEMPLATE.template.md. Spec-12 S2 runs `git rm -r tools/unattended/` and keeps only resume-tick.sh. S3, the legs table (:151) and Files touched (:180-181) move check-playbook.sh and its suite but never the template, and no spec-12 line mentions PLAYBOOK-TEMPLATE. The kept leg therefore exits 2 after unit 12. The red is loud and blocks the landing, so I grade it medium. | sound | - |
| 4 | coherence | memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-20.md:section 3 Non-goals (closing a shim row), against unit 17 §3, unit 9 S5 and unit 12 S2 | medium | medium | confirmed | Each spec hands the job to another unit. Spec-17:83 gives 'Closing the row and removing the held set' to unit 20, and spec-17:95 hands it off to 20. Spec-9 S5 calls removing a row 'unit 20's exit check', and spec-12 S2 says 'until PLAY-dConvergedCharter-20 closes it'. Spec-20 §3 non-goals (:107-108) says 'the commit that closes it is the owning unit's, units 16 and 17 for theirs', and spec-20 S4 only reds an open row. So no unit owns the close. | sound | - |
| 5 | coherence | memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-20.md:section 2 S3, against unit 12 §8 F4 | medium | low | confirmed | The mismatch is real: spec-20 S3 (:70-72) names 'update's withdrawn arm for a claim retired to `none`', while spec-12 F4 resolved the successor to `runtime`. The claimed impact does not hold, though. govkit.py:9547-9565 carries a claimed kit's rows to its successor, and the verdict grid (govkit.py:8286) maps ('equal','absent') to `withdrawn`. Carried rows whose source gov no longer ships, tools/unattended/*, therefore still read `withdrawn` through the grid. The adopter's files do leave; only the arm spec-20 cites is wrong, so the defect is in the citation. | sound | - |
| 6 | coherence | memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-11.md:section 2 S1/S2 and section 4 Evidence (107 folded keys), against unit 20 S3/AC4 and unit 22 S5 | medium | medium | confirmed | legacy-homes.txt holds 53 .unattended.conf rows, including DIRECTIVES_EXTRA, DIRECTIVES_EXTRA_TABLE, DOD_EXTRA, HALT_CODES_EXTRA, HOLD_CODES_EXTRA and PHASES_EXTRA (:70-95). Spec-11 §4 counts 102 kit-conf rows (6+2+35+6+53) plus 5, so the six extension keys get catalogue rows with `legacy`. Spec-20 S3 defines the dropped keys as those 'the catalogue does not carry, the run conf's extension keys', and AC4 reds if an extension key moves into the policy file. Spec-12 S2 removes the folded `unattended.*` catalogue rows at order 4, before unit 20 at order 7. The four specs give no consistent rule. | unsound | - |
| 7 | coherence | memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-11.md:section 6 AC8, against section 2 S3 | medium | medium | confirmed | legacy-homes.txt:20 lists `.githooks/gate-env.sh INHERITED_RED owner-policy`, so S1 folds it, and gate-env.sh:103 is `INHERITED_RED=land`. S2 writes gov's value into .governance/policy.toml. S3 (:62-71) says that for a key whose `legacy` names the home, `legacy` prints the policy file's value where that file sets it, and that `--key` prints it bare. At `--rev HEAD`, `legacy --key INHERITED_RED` therefore prints `land`, but AC8 (:315-316) expects nothing. | sound | - |
| 8 | coherence | memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-11.md:section 6 AC6 (and unit 12 §2 P3) | medium | medium | confirmed | Outside memory/, `git grep read_policy_key` finds hits in tools/policy/policy.py (3, at :25, the :1138 POLICY_KEY_READ regex and the :1199 docstring) and tools/policy/README.md (5, :155 among them). S6 counts comment lines and docs as readers. S4 lists policy.py's POLICY_KEY_READ/scan_gate_readers only as 're-derived', not removed, and S7 rewrites only README:212-219. AC6 has no `--except`, so `--readers read_policy_key --kind value` still names policy.py and README:155 and exits 1. The same applies to spec-12 P3 (:38). | sound | - |
| 9 | coherence | memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-11.md:section 7 Gates | medium | medium | confirmed | I scanned tools/gate-legs.json. It holds 'pre-push self-test' (.githooks/pre-push.test.sh), 'pre-push bar self-test' (guard .githooks/), 'push-main self-test' and 'held-halves selftest'. S4 edits .githooks/pre-push, push-main.sh, post-merge.sh, held_halves.py, push-main.test.sh and pre-push.test.sh. Spec-11 §7 (:331) lists none of those four legs, yet it declares a New arm in pre-push.test.sh covering AC5. | sound | hand-named-gate-list-green-while-the-bar-reds |
| 10 | coherence | memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-21.md:section 2 S4 and Files touched, against section 6 AC6 | medium | medium | confirmed | Unit 22 is order 1 and creates tools/govkit/settings_census.py, which calls `load_policy` (spec-22:116,137). Unit 21 is order 8, and its S4 (:77-78) says that population 'leaves with the file'. Spec-21's Files touched (:153-161) and the S4 by-name readers omit settings_census.py, yet AC6 (:208) requires `git grep -n load_policy` over tools/ to print nothing. | sound | - |
| 11 | coherence | memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-14.md:section 2 S7, against unit 20 S5 | medium | medium | confirmed | Spec-14 S7 (:97-100) has the arm read `derive_pending_steps` per registered adopter and gives no release. Spec-20 S5 defines `check_adopters_converged(root, release)` over every register row 'registered or not', read through `derive_migration_state` at `--release <tag>`, with exit 2 on an empty register. Spec-5 (:67,179) exits 2 'not graded' before a release tag exists. Spec-14 says nothing about how `check --exit` supplies the release or folds that exit 2 into its verdict. | sound | - |
| 12 | coherence | memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-7.md:section 2 S8 and section 4 'The guides', against unit 1 §4 Evidence and unit 19 §2 | medium | medium | confirmed | Spec-1:90 and :108-110 say units 12 and 16 remove PLAYBOOK-TEMPLATE.md and SESSION-KICKOFF.md 'first'. Spec-19:39 says unit 12 retires PLAYBOOK-TEMPLATE.md. Spec-12's Files touched names only the four UNATTENDED guides. Spec-7 S8 (:82-85) and its table (:192,194) remove PLAYBOOK-TEMPLATE.md and move SESSION-KICKOFF.md at order 17, after unit 19 (order 12) and unit 1 (order 15). One detail is overstated: spec-19 does include SESSION-KICKOFF.md in its own population (:129, :161), so only PLAYBOOK-TEMPLATE.md is mis-owned there. Unit 1 is wrong on both files. | sound | - |
| 13 | coherence | memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-19.md:section 2 S6/S7 and section 4 'The pins after' | medium | medium | confirmed | Spec-19 S5 (:61-62) and 'The pins after' (:139) add `*.conf text eol=lf` and `*.example text eol=lf` to gov's .gitattributes. S6 (:73-74) keeps `.codebase-map.conf`, `.memory-tree.conf`, `.process-monitor.conf` and `.memory-tree.conf.example` as instances that 'no class covers'. S7 (:81-84) reads every `[[lf_pin]]` pattern and reds any that is not a class line while a class line covers its extension. With *.conf and *.example in place, those kept rows are covered, so S6 and S7 contradict each other. git grep shows these rows at codebase-map/kit.toml:141, memory-tree/kit.toml:366 and :369, and process-monitor/kit.toml:107. Spec-11 S2 (:51) deletes `.process-monitor.conf`. | sound | - |
| 14 | coherence | memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-3.md:section 2 S5 and section 7 Gates | medium | medium | confirmed | Spec-3 S5 (:62-63) edits the program of TOOL-dTotalRecall-20 S1 and relies on 'the landed row's frozen argv keeps its behaviour'. In upgrade_steps.py, check_frozen (:1038-1041) reds a landed step whose program file moved bytes, even when its argv is unchanged. tools/gate-legs.json:1440 has the step-rows-frozen leg, and spec-3 §7 (:186) leaves it out of its gate list, along with upgrade-walk. The program does not exist yet: tools/govkit/steps/ holds only fanout_cap, python_floor and receipt_schema_4, and dTotalRecall is DEFERRED. So the clash depends on dTotalRecall landing without ask A1, which is exactly the condition the finding states. | sound | - |
| 15 | coherence | memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-9.md:section 2 S2 Readers | medium | medium | confirmed | Spec-9 S2 Readers (:44-51) names the five kit.toml rows, the adopt scripts and the drift-audit README. It then says 'NO VALUE READERS'. git grep shows .governance/install.json:164, :566, :770 and :812, each with path and source set to a SKILL.template.md, plus .gitattributes:282 and :286. None of these is in S2's list. The .gitattributes lines may already be gone because spec-19 S5 goes first, but the install.json receipt rows are a real omission. | sound | retirement-inventory-misses-readers-by-value |
| 16 | coherence | memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-20.md:section 2 S3 Readers and section 4 Evidence | low | low | confirmed | Spec-20 says '45 `.unattended.conf` rows' (:77) and '116 rows across six homes' (:134). The command `grep -v '^#' tools/policy/legacy-homes.txt \| awk \| uniq -c` printed 53 .unattended.conf rows over seven distinct homes, and `grep -vc '^#'` printed 115. Spec-11:160-161 says 115 and 53. | sound | two-answers-to-one-question |
| 17 | coherence | memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-17.md:section 6 AC6 | low | low | confirmed | Spec-17 AC6 (:205) runs `grep -nE 'skill\|held' shims.md`. Run against help/shims.md today, it already matches :16, :44 and :48 on 'held' and nothing on 'skill'. The command therefore prints lines before S5 is built, so it cannot tell the built page from today's. | sound | fixture-passes-by-finding-nothing |
| 18 | coherence | memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-3.md:section 2 S4 | low | low | confirmed | Spec-3:56 cites `derive_readers` as 'PLAY-dConvergedCharter-11 S1'. In spec-11, S1 (:37) is 'The fold's catalogue rows', and S6 (:110) is 'The reader inventory (shared interface I1), derive_readers'. The section address is wrong. | sound | - |
| 19 | grounding | memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-11.md:section 4 "The readers" (with S2, S4) | high | high | confirmed | scratch-guard.js reads MEMORY_ROOT and ROUTED_PATHS from the .memory-tree.conf text with readConfKey (:1155-1156, :1487-1488). checkUnarmed (:916-917) returns 'blank or absent', and the hook then refuses every write except one to the conf (:1158-1160). legacy-homes.txt lists both keys as owner-policy rows of .memory-tree.conf, so spec-11 S1/S2 folds them and moves their lines out. Spec-11 §4 'The readers' (:199-208) and S4's last bullet give only a shell eval re-point and a Python parser re-point. No JS hook shape is given, and scratch-guard.js appears nowhere in spec-11. Migration (:217-220) moves the values (S2) before the re-points (S4). The gate fails closed, so the consequence is every write refused rather than an unsafe admit. | sound | settings-edit-takes-effect-mid-session |
| 20 | grounding | memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-11.md:section 2 S4 first bullet; section 4 Evidence (post-merge's three keys); section 8 F3 | medium | medium | confirmed | I counted with grep -c: post-merge.sh has 0 resolve_kit_dir and 0 resolve_python/resolve-python hits (push-main.sh has 12/22, unattended.sh 10/32). post-merge.sh:170 says the hook 'sources no kit'. :231 reads GOV_PYTHON with read_policy_key, and spec-11 S4 (:73-80) deletes that copy and re-points to `policy.py legacy … --key`. That re-point needs a python before GOV_PYTHON is known. Spec-11:391 says the resolver is one every shell reader 'already carries or gains', but S4 itself says 'already carries', and neither addresses the GOV_PYTHON bootstrap. | sound | - |
| 21 | grounding | memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-11.md:section 6 AC8; section 2 S2 ('its six mechanic keys') | medium | medium | confirmed | grep of .githooks/gate-env.sh finds only two mechanic assignments: :90 GOV_KITROOT=tools and :113 GATE_WSL_MIRROR_DEFAULT. GOV_PYTHON appears only in the comment at :55. legacy-homes.txt still lists six mechanic rows, because the comment is harvested. So the positive half of spec-11 AC8 (:315), 'prints the mechanic's value' for GOV_PYTHON, would print nothing. S2's 'its six mechanic keys' (:49) overstates what gov assigns. | sound | - |
| 22 | grounding | memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-20.md:section 2 S1 (the up reads `policy.py get <key> --rev HEAD --explain`; by-value reader 'unit 11's both-homes reader behind policy.py get') | high | high | confirmed | In tools/policy/policy.py, resolve() (:752-757) is resolve_read over the catalogue row and the policy revision. The only legacy read is the .agent-cap.conf fan-out for AGENTS_PATH, with no kit-conf fallback. Spec-11 puts the home fallback in the separate `legacy` verb (S3, :62-71; Migration :217-220 says 'S3 falls back to the home'). Spec-11 never extends get/resolve. Spec-20 S1 (:38-44) moves a value only where `get --explain` names the home, and claims (:51) that unit 11's both-homes reader sits behind `get`. Built as written, the step moves nothing and then takes the conf keys out. That loses adopter values, though AC1 would likely catch it at build time. | sound | - |
| 23 | grounding | memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-20.md:section 2 S2 ('.githooks/gate-env.sh takes no step: no descriptor ships it, so no adopter holds it'); section 4 Alternatives rejected | high | high | confirmed | WIRE-INTO-PROJECT.md:921-927 and the table at :936 tell adopters to declare GATE_DOC_PATHS and GATE_POST_MERGE in their own .githooks/gate-env.sh and commit it. The [[exempt]] row at registry.toml:311-313 says pre-push travels to every push-main adopter. pre-push:652 and :1744-1745 read those keys from the gate file. Spec-11 S1/S4 folds the gate file's owner-policy keys and re-points their readers to `policy.py get`, which has no home fallback. Spec-20 S2 (:57-58) says 'no descriptor ships it, so no adopter holds it'. The first half is true; the second is false. | sound | - |
| 24 | grounding | memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-12.md:section 4 Evidence ('34 tracked files spell unattended/ ... they are S2's by-name readers'); section 2 S2 by-value needles; section 6 AC2 | medium | medium | confirmed | Spec-12 S2's by-name list (:57-69) and its value needles (:70-72: /unattended, unattended.sh and the four guide names) do not cover several readers git grep finds: .governance/deploy.toml:20 (the selection entry "unattended"), tools/lib/render-doc.sh:217 and tools/memory-tree/adopt-memory-tree.sh:439 (rendered_at("unattended", "PROTOCOL.template.md") behind {{UNATTENDED_PROTOCOL}}), and tools/memory-tree/kit.toml:71's placeholder. render-doc.sh:193-202 shows rendered_at returns None when no row matches, so the render falls back to the generic phrase at :210. AC2 (:238-242) only checks the path and /unattended needles. | sound | - |
| 25 | grounding | memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-6.md:section 4 "The census" | medium | medium | confirmed | Re-probed. `git ls-files memory \| wc -l` printed 10534. The table in spec 6 §4 'The census' sums to 10501, a gap of 33. `git ls-files memory \| grep -c /spec/units/` printed 21. Grouping by depth and extension found 51 files under memory/builds/*/build/ that are not md, py or sh: tsv 20, js 13, json 5, log 4, out 3, txt 2, svg 2, html 2. Of these, 38 (everything but js) are not scripts, so neither 'a script beside its record' nor any other row admits them. The predicate the arm is to call, `check_pockets`, does not exist in the tree (`git grep check_pockets` matched only spec 6), so whether `memory/builds/*/*/*.md` admits a depth-6 spec is unspecified. The data files are left out whatever glob semantics apply, so AC2's '0 unregistered' meets homes no row owns. | sound | - |
| 26 | grounding | memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-19.md:section 2 S6 ('rows whose pattern no class covers stay instances: the root confs ... .memory-tree.conf.example') against S5 and S7 | medium | medium | confirmed | Spec 19 S5 adds `*.conf` and `*.example text eol=lf` as class lines. S6 keeps `.codebase-map.conf`, `.memory-tree.conf`, `.process-monitor.conf` and `.memory-tree.conf.example` as instances 'no class covers'. S7 reds every kit `[[lf_pin]]` pattern 'that is not a class line while a class line covers its extension'. In a scratch repo with those two class lines, `git check-attr eol -- .codebase-map.conf tools/memory-tree/.memory-tree.conf.example` printed `eol: lf` for both, so the class lines do cover dot-led files. `git grep -A1 '^\[\[lf_pin\]\]'` shows those patterns at codebase-map/kit.toml:141, memory-tree/kit.toml:366 and :369, and process-monitor/kit.toml:107. S7 as written would red the rows S6 keeps. | sound | - |
| 27 | grounding | memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-7.md:section 2 S6 ('rename detection stays on and only a D entry joins the population') against S8's move of SESSION-KICKOFF.md | medium | medium | confirmed | Spec 7 S6 says 'rename detection stays on and only a D entry joins the population'. Its §4 evidence (:181), alternatives (:262) and F3 (:361) all run the walk as `git log --diff-filter=D -- 'memory/guides/*'`. S8 moves SESSION-KICKOFF.md to memory/project/, and the §4 table (:194) says it is 'not graded'. I reproduced this in a scratch repo. With the pathspec, `git log --first-parent --diff-merges=first-parent --diff-filter=D --name-status -M -- 'memory/guides/*'` printed `D memory/guides/SESSION-KICKOFF.md`. Without the pathspec it printed nothing. The pathspec form therefore puts the moved manifest into the graded population. | sound | - |
| 28 | grounding | memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-20.md:section 4 Evidence ('116 rows across six homes'); section 2 S3 ('the 45 .unattended.conf rows') | low | low | confirmed | Spec 20 :134 reads '116 rows across six homes' and :77 reads 'the 45 `.unattended.conf` rows'. `git show 0d1c1dda:tools/policy/legacy-homes.txt \| grep -v '^#' \| grep -c .` printed 115. The per-home counts are .codebase-map.conf 6, gate-env.sh 11, .lexicon.conf 2, .memory-tree.conf 35, .process-monitor.conf 6, .unattended.conf 53 and the house file 2, which is seven homes. Spec 11 :160 states 115 and 53 correctly. No behaviour derives from spec 20's figures. | sound | - |
| 29 | grounding | memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-19.md:section 4 Evidence ('79 eol=lf lines ... 78 pins'); section 10 ('scout A counts 78 eol=lf lines and source holds 79') | low | low | confirmed | `git show 0d1c1dda:.gitattributes \| grep -c 'eol=lf'` printed 78, and the only comment line among them is :72. That makes 78 lines and 77 pins. Spec 19 :117 says 79 lines and 78 pins, and :284 'corrects' scout A's 78, which was right. AC5 pins its own after-state figure, so this affects the evidence only. | sound | - |
| 30 | grounding | memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-11.md:section 4 Evidence ('72 tracked code files ... spell .memory-tree.conf, 31 .unattended.conf and 15 gate-env.sh, PINNED by git grep -l') | low | low | confirmed | Spec 11 :175-176 pins 72/31/15 by `git grep -l` at d8a12f046. `git diff --stat 0d1c1dda d8a12f046 -- ':!memory'` printed nothing, so the two revisions hold the same product files. I tried several readings at d8a12f046: everything outside memory (116/70/31), code extensions plus hooks (81/46/21), tools/ py and sh (71/32/13), and code without self-tests (55/21/8, 48/17/8, 54/24/10). None reproduces 72/31/15. | sound | - |
| 31 | grounding | memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-7.md:section 4 Evidence ('memory/guides/ holds ten files at base, 301 KB') | low | low | confirmed | `cat memory/guides/*.md \| wc -c` printed 317842. Summing `git cat-file -s` over the ten guides at d8a12f046 also gave 317842, which is 310 KiB or 318 KB. Spec 7 :175's '301 KB' matches neither unit. The figure is cosmetic. | sound | - |
| 32 | reuse | memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-20.md:section 2 S1 (and its Readers by value), section 4 Evidence | high | high | confirmed | Spec 20 S1 moves a value only where `policy.py get <key> --rev HEAD --explain` names `<home>` as its source. In tools/policy/policy.py:749, `resolve_read` reads a legacy home only for AGENTS_PATH, through `derive_lowered_limit`. Unit 11 adds the home fallback to the separate `legacy` verb (S3, `render_folded_lines`). Its S1-S4 never extend `get`/`resolve`, and its §5 line ('get --explain names the source of a folded key') does not make get read the conf. In an adopter tree before the step, get therefore answers the policy file or the default, never the home. The up moves nothing, yet still strips the folded lines, so non-default conf values are lost. | sound | decision-re-derived-by-a-second-process |
| 33 | reuse | memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-12.md:section 2 S1, Files touched; also PLAY-dConvergedCharter-7 section 2 S7 and PLAY-dConvergedCharter-22 section 2 S4 | high | high | confirmed | catalogue.toml:647-649 sets `instructions.edit` default `owner-command-agents-propose`. dOrderedCharter-15 :65 says that under this default a write without proof 'prints the proposal and writes nothing'. Spec 13 §8 F2 (:231-238) resolved (b): an agent pass appends the kit row itself and records it through the change record's door. Despite that, spec 12 :44 writes rationale 'through `instructions.edit`' and then deletes the guides. Spec 7 :79 does the same. Spec 22 S4 (:59) adds through `instructions_edit.py add --manifest overlay` and removes the `[[exempt_leg]]` row 'in the same act' with no check that the row landed. Built as written, the rows are only proposed while the guides and the exempt row are removed. | sound | - |
| 34 | reuse | memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-7.md:section 2 S7 and section 3 Edges (consumes-from PLAY-dConvergedCharter-13) | medium | medium | confirmed | Spec 7 :78 names the mover '(I16, `dossier_move.py`)', and the §3 edge at :156 consumes `dossier_move.py` from unit 13. Unit 13 S1 defines I16 as the factory `tools/lib/prose_move.py` (`derive_moves`, `write_moves`). S2 makes `dossier_move.py` its codebase-map caller, whose route sends `seam:` lines to proposals and other sections to records. S3 makes `tools/playbook/guide_move.py` the guide caller. Spec 7 names neither prose_move.py nor guide_move.py, so the edge token and the seam it points at are wrong for guides. | sound | - |
| 35 | reuse | memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-11.md:section 2 S5 and S8, section 10 | medium | medium | confirmed | check_policy.py:631-656 defines `arm_single_reader`, which skips comments and docstrings, matches READ_SHAPE, and is used by two ARMS rows (:752, :756). `grep arm_single_reader\|READ_SHAPE` over the spec set printed nothing. Spec 11 S5 and S8 each define their own spelling-based scanner. S8 reds any file other than roles_lib.py that 'spells `house/policy.toml`', so a comment reds where the existing arm would not. The fix is unsound for S5. `arm_single_reader`'s `const` matches the bare token `\bconst\b` on any non-comment line, so passing the folded KEYs as `const` would red every legitimate consumer that uses `$BACKLOG_MODE` after evaling `policy.py legacy`. A plain home-path reader row would also red readers of the retrofit `_CUTOFF`/`_PIN` keys and the mechanic keys, which stay in those homes by design. | unsound | - |
| 36 | reuse | memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-9.md:section 2 S4, section 4 Migration | medium | low | confirmed | Spec 9 S4 has the step's UP 'withdraw the old render where its bytes equal the old kit's render ... and names and keeps a file that is not'. That re-derives VERDICT_GRID's ('equal','absent') withdrawn and ('differs','absent') retired-edited cells (govkit.py:8283-8292) and skips the `--write-withdrawals` consent noted at :8311-8312. Spec 20 :196 rejects the same design. No withdrawal citation appears in spec 9. The effect is contained: only unedited renders are deleted, and §4 Migration (:158) then puts a shim forwarder at the old path. That is also why the fix is unsound. If deletion happens only through update's withdrawal under `--write-withdrawals`, then without the flag the old render stays at the path that `shims.py --write` must fill with the forwarder, which breaks S5 and the Migration sequence. AC4's `withdrawn` verdict would also only mean an order, not a cleared path. | unsound | - |
| 37 | reuse | memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-6.md:section 2 S1, section 10 | medium | medium | confirmed | Read spec-6 S1 and §10. S1 builds its own home allowlist from the registry's `home` globs. §10 names only check_record_kinds, the factory and check_pockets as seams. It never mentions hygiene check 3, `structure` or PROJECT_REGISTRY_EXTRA. Read check-memory-hygiene.sh:882-975. Check 3 is a closed allowlist of memory root files and directories, `project/` registries (with the PROJECT_REGISTRY_EXTRA widening), backlog shards, builds-root files and map entries. So a new home has to be declared in both places. One caveat: §4 gives `memory/project/*.txt` to the `registry` row, so a `.txt` extra registry passes both arms. Only a non-.txt PROJECT_REGISTRY_EXTRA entry, or a new root directory, makes the two arms disagree. The effect is contained. | sound | - |
| 38 | reuse | memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-2.md:section 2 S1, section 4 Inventory (`--homes`) | medium | medium | confirmed | Read spec-2 S1 (lines 40-46). positional.py's derive_positional_class matches the `home` globs itself, using rows printed by the new `record_kinds.py --homes` mode. The spec names no shared predicate and `grep derive_record_kind` over spec-2 hits nothing. That clashes with spec-6 S1, which says 'through the home-match predicate ... never a second glob dialect', and with TOOL-dCalibratedLens-33:40/74/91/152 (one glob dialect, no second matcher). A dialect mismatch, such as `*` crossing `/`, would class a live path as frozen. That only bites on homes whose globs the two dialects read differently, so the effect is contained. | sound | decision-re-derived-by-a-second-process |
| 39 | reuse | memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-22.md:section 2 S2, section 4 The states (`undeclared`), AC2 | low | low | confirmed | Read govkit.py:2689-2690: check 7h already fails a leg that no descriptor claims and no [[exempt_leg]] covers. Spec-22 S2 (lines 44-49) and the §4 states row (line 150, `undeclared \| ... \| 1`) make `settings_census.py --check` exit 1 on the same fact. One planted leg therefore gives two reds with two remedy texts. Both reds are correct, so the cost is duplicate noise only. | sound | - |
| 40 | blast-radius | memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-12.md:section 2 S2 (Readers) / section 4 Files touched / section 7 Gates | high | high | confirmed | Re-ran the git grep. These files resolve the kit by its home name `unattended`: resolve-python.test.sh:168 (`\|\| exit 2`), check-spec-tokens.test.sh:1950 (`\|\| exit 2`), run-selftests.test.sh:252 (`\|\| exit 2`), deviation_join.py:376, drift-audit/selftest.py:3702,4360, runlog/selftest.py:4429, marker-contract.test.sh:111 and the turnstile test:1317. resolve-python.test.sh:352 has a `kickoff_region` PARITY_ROWS canonical of `$UNATTENDED_DIR/check-unattended.sh`. deviation_join.py:400-413 raises Unmeasured when lib-unattended.sh, which holds GEN_REGION_AWK, does not resolve. Read drift-audit:3700-3707 and runlog:4429-4435: both turn into a SKIP. Spec 12's S2 by-name list and its §4 Files touched name none of these files, and §7 omits the python resolver, spec-tokens, drift-audit and runlog legs. S2's by-value needle `unattended.sh` might list some of them, but the spec gives GEN_REGION_AWK and the kickoff_region canonical no new home. The skips would also read as coverage. | sound | - |
| 41 | blast-radius | memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-12.md:section 4 Evidence ('Outside it and the memory root') / section 7 Gates | medium | medium | confirmed | Read check-dead-paths.sh:57-62 and :190-197. Its needles are basenames git no longer tracks, and memory/map/features/* and memory/gotchas/* are graded as live carriers. Ran `git grep -c` for unattended.sh, check-unattended.sh and lib-unattended.sh over those two directories: 42 files, before counting the kit's other basenames. Spec 12 names no memory/map file and no gotcha, and does not list `dead-path` or `codebase-map coverage` in §7 (grep count 0 for both). Its inventory excludes the memory root. So the dead-path leg reds at the pass commit, and the dossier claims on the kit go stale. | sound | - |
| 42 | blast-radius | memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-21.md:section 2 S1 and AC6 / section 7 New arm (render_agents.py) | high | medium | confirmed | Spec-11 S8 (lines 122-128): once the seed is gone, any file other than roles_lib.py that spells `house/policy.toml` reds. Spec-21 S1 adds house_seed.py, which must read the adopter's house file, and its plants write that file. AC6 needs the arm armed and naming no reader. Ran git grep for `house/policy.toml`: tools/govkit/selftest.py:9581 and tools/policy/README.md:150-151 spell it. Neither is in spec-21 S4's readers or §4 Files touched; S4 lists tools/roles/README.md but not tools/policy/README.md. So AC6 conflicts with S1, and the policy README keeps describing a removed legacy home. The builder would have to exempt files ad hoc. The failure is loud, so it is contained. | sound | - |
| 43 | blast-radius | memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-16.md:section 2 S3 (Readers) / section 4 Files touched / section 7 Gates | medium | medium | confirmed | Read memory/map/features/session-kickoff.md: it claims `harness-hooks = ["SessionStart skills/session-kickoff/manifest-check.sh"]`. map_extractors.py:141-171 builds the key `<event> <script>` from .claude/settings.json. Spec 16 S3 re-points settings.json:38/47 but names no memory/map file, and `grep -c 'codebase-map coverage'` over spec 16 prints 0. Its S3 reader list comes from the derive_readers walk, which excludes the memory root. So the move leaves a stale claim and an unclaimed key, and the codebase-map leg reds. | sound | - |
| 44 | blast-radius | memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-9.md:section 4 Files touched / section 7 Gates / AC7 | medium | medium | confirmed | The dossiers claim the old skill names: branch-reconcile.md:18 `cleanup`, lexicon.md:23, memory-recall.md:22, runlog.md:21. memory/map/baseline.toml holds `rendered-skills = ["drift-audit"]`, and .claude/skills/ currently holds cleanup, drift-audit, lexicon, memory-recall and runlog. Spec 9 S2 renders .claude/skills/gov-*/SKILL.md, which mints five new keys. The spec names no memory/map file and `grep -c 'codebase-map coverage'` prints 0. So the coverage leg reds with UNCLAIMED keys. | sound | - |
| 45 | blast-radius | memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-11.md:section 2 S6 (derive_readers, shared interface I1) | medium | medium | confirmed | Spec-11 S6 (lines 110-118): derive_readers walks 'every tracked text file outside the memory root'. AC6 (lines 308-310) even reds when 'a reader under the memory root is' named. check-dead-paths.sh:57-62 grades memory/map/features and memory/gotchas as live carriers. So a retiring unit's clean inventory misses live carriers that later red the dead-path and codebase-map legs. That matches ids 41, 43 and 44. | unsound | - |
| 46 | failure-envelope | memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-11.md:section 2 S5 (arm_folded_homes) | high | high | confirmed | Spec-11 S5: a file that spells the folded KEY and the home's path escapes the arm if it spells the policy file's path anywhere. check-memory-hygiene.sh:188 sources .memory-tree.conf, and :618 is a comment naming `.governance/policy.toml`, so the escape covers it. Re-ran the count (conf readers outside memory that also spell policy.toml): 21. So the arm passes a reader it never graded whenever S4's re-point misses one. | unsound | - |
| 47 | failure-envelope | memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-11.md:section 2 S4, last bullet; section 5 | high | high | confirmed | Spec-11 S4 (lines 94-96) prescribes `eval "$(… policy.py legacy <home>)"` in shell. If the reader fails, eval gets an empty string and binds nothing, so the caller silently runs on its defaults. Spec-11 §5 covers only an absent home and a malformed policy file under on-invalid. It says nothing about a failed reader, such as no python or a missing kit. unattended.sh:507 shows the existing pattern: capture the output, test the exit status, name the failure. | sound | swallowed-delegate-reads-as-clean |
| 48 | failure-envelope | memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-21.md:section 2 S1 step (3); section 4 'The fold'; section 5 security | high | medium | confirmed | DEPL-28 S5 (lines 63-67) allows a house value below medium only under the owner's authorization, with a `held:` print otherwise. TOOL-dBoundRoles-23 S5/S6 runs check_effort_floor on policy-file levels and reds them under non-owner-only guards. Spec-21 S1 step (3) writes every unruled effort through render_policy_text. Its §4 fold table has no below-floor row, and grep finds no 'floor' or 'below' in its body. One thing narrows the path: dBoundRoles-23 S5 also makes R12 red a below-floor house value. An adopter holding one is therefore already red. The effect is contained. | sound | - |
| 49 | failure-envelope | memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-21.md:section 6 AC6; with spec 11 section 2 S8 | medium | medium | confirmed | In spec 21, S1 (lines 39-47) has the step tools/govkit/steps/house_seed.py read the house file through derive_house_proposals and delete it last. AC6 (lines 207-211) asks derive_readers to return no reader of tools/roles/house/policy.toml 'outside frozen records'. In spec 11, S8 (lines 122-126) reds every file other than roles_lib.py that spells house/policy.toml. Neither spec exempts the migrator. DEPL-dShippedRelease-28's inventory places derive_house_proposals in tools/playbook/adopt_declarations.py, so that file also reads the house file and is not exempted either. `git grep -n house/policy.toml -- ':!memory'` already lists tools/govkit/selftest.py:9581, tools/policy/policy.py:1119 and others. Once the seed leaves gov, the arm and AC6 red on the readers the step needs to keep. The other way out is to build the path from fragments, which blinds the arm. | unsound | - |
| 50 | failure-envelope | memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-23.md:section 6 AC5 | high | high | confirmed | Spec 23 AC5 (line 195) reads `git grep -n "hashlib.sha256" -- maintain_file.py loop_review.py release.py`. Section 4 places those files in tools/drift-audit/, tools/loop/ and tools/integrations/. Run from the repo root, that exact command printed nothing (rc=1), because a bare basename pathspec matches only at the root. Whatever the code holds, this half of AC5 can never find a stray hash. The single spelling also misses `from hashlib import sha256` and `hashlib.new('sha256')`. The parity extractor half compares only the block copies with each other, so nothing checks for a hash computed outside the block. | sound | rule-stated-with-no-check-that-fails |
| 51 | failure-envelope | memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-19.md:section 2 S6 and S7 | medium | medium | confirmed | In spec 19, S5 adds `*.conf` and `*.example` class lines to gov's .gitattributes ('The pins after', lines 133-142). S7 reds every descriptor `[[lf_pin]]` pattern 'while a class line covers its extension' and does not say which class set counts. Read against gov's file, the descriptor rows .codebase-map.conf, .memory-tree.conf, .process-monitor.conf and {kit}/.memory-tree.conf.example would red, yet S6 says they must stay. The pattern `{playbook_path}` (re-probed at tools/govkit/entries/playbook.kit.toml:65) appears in neither S6's kept list nor S7's rule, and the spec says nothing about placeholder patterns. AC6's 'only class patterns and the uncovered instances S6 lists' is therefore ill-defined. | sound | - |
| 52 | failure-envelope | memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-8.md:section 2 S2 (check_renderer_live) | medium | - | refuted | The premise is false on re-probe: the case is already red in the same gate. PLAY-dOrderedCharter-20 S4 (memory/builds/dOrderedCharter/spec/...-20.md lines 63-69) says of renderers.toml that 'a file two rows claim, or none, is red, so each instruction file has exactly one renderer of record'. Its S8 runs that table check inside the same `render_playbook.py --check-render` that runs check_renderer_live. A listed instruction file whose row was deleted is therefore red as 'claimed by none' and does not pass silently. Spec 8 S2 does not need its own verdict for that class. | none | - |
| 53 | failure-envelope | memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-22.md:section 2 S4 (--apply for a leg); section 5 | medium | medium | confirmed | Spec 22 S4 (lines 57-60) makes two writes: the overlay `[[gate-leg]]` row through instructions_edit.py, 'then' removal of the `[[exempt_leg]]` row from tools/govkit/registry.toml 'in the same act'. It states no failure handling, and section 5 (lines 203-204) prices only an absent door, home or kind and an unparsable manifest. Because the door write comes first, the likely half-applied state is a leg that is both overlay-claimed and still exempt, not the 'neither' state the finding stresses. A half-applied state with no recovery and no defined census reading is still real and reachable. The effect is contained to gov's tree on an owner-invoked command. | unsound | - |
| 54 | failure-envelope | memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-3.md:section 2 S1-S3 | medium | medium | confirmed | In spec 3, S1 (lines 36-41) defines the window as '30 days ending at the commit measured'. S2 (lines 42-43) walks `git log ... --since=<since>`. S3 (line 48) calls `check_merge_evidence(root)` with no since, and no line says how since is derived. A window anchored on the wall clock lets the record-kinds leg's verdict at a fixed commit change with the run date: a pair crosses the 0.9 share or 20-commit floor with no file changed. The spec never says the window is anchored on the commit's own date. | sound | - |
| 55 | failure-envelope | memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-9.md:section 2 S4 (skill_rename.py UP); section 5 | medium | medium | confirmed | Spec 9 S4 (lines 64-66) withdraws the old Skill only 'where its bytes equal the old kit's render', and cites adopt-branch-reconcile.sh as the precedent. Re-read at tools/branch-reconcile/adopt-branch-reconcile.sh:104-115, the precedent never compares bytes. It strips CRs (`tr -d '\r'`) and recognises its old render by `name: branch-reconcile` in the front matter plus the CLI name branch_reconcile.py in the body. Under the spec's byte compare, a copy that is CRLF, rendered from an older template, or rendered with other answers is kept as 'not a kit render'. The witness then reads 'no kit render' and the step reads applied, so the old Skill stays beside gov-<new>. | sound | - |
| 56 | failure-envelope | memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-11.md:section 2 S3 (render_folded_lines); section 4 Migration | medium | medium | confirmed | In spec 11, S3 (lines 62-68) prints 'the home's own last KEY= line' and defines no line grammar. Section 4 (lines 173-174) records that the homes are sourced today (`. "$CONF"` at unattended.sh:746, check-memory-hygiene.sh:188). The Migration section (lines 220-222) claims a tree with its homes 'reads exactly what it read before'. Gov's own homes are plain; grep found no export or $( in them. An adopter's sourced conf, however, may legally hold `export KEY=`, `$VAR` or `$(...)` expansions, or multi-line quoted values, and a line parser would read these differently from sourcing. The spec neither handles nor refuses them, so the 'exactly what it read before' claim does not hold for those homes. | sound | - |
