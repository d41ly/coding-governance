**Serves:** spec-audit TOOL-aProbedUnit-1 TOOL-aProbedUnit-2 TOOL-aProbedUnit-3 TOOL-aProbedUnit-4 TOOL-aProbedUnit-5 TOOL-aProbedUnit-6 TOOL-aProbedUnit-7

# Tier-2 spec audit — the `aProbedUnit` spec set, round 1

Written 2026-09-14 on node `a` by the unattended-build harness's spec-audit stage (`tools/workflows/unattended-build.js`): four primed finder lenses, an adversarial skeptic per finding in five batches, one synthesis pass. Subject: the seven SPECCED units of `memory/builds/aProbedUnit/`, read at the blobs named on the range line. Source claims below stand as the skeptic stage confirmed them; this record re-checked the build README's rule three, spec 1's section 6 and 7 and spec 4's section 7 against the worktree at `270611cd` before adjudicating cluster A, and no other claim was independently re-derived here.

Reviewed subjects, pinned: `memory/builds/aProbedUnit/spec/2026-09-14-spec-TOOL-aProbedUnit-1.md@c63a9bb77cc14e4e9045125c7005633efd4c5fd9` · `memory/builds/aProbedUnit/spec/2026-09-14-spec-TOOL-aProbedUnit-2.md@1101650a94105b792fe2b453d7d28f0cae745ead` · `memory/builds/aProbedUnit/spec/2026-09-14-spec-TOOL-aProbedUnit-3.md@92ce4e48f4fef85ca620d9ba4982b380d8fe33f9` · `memory/builds/aProbedUnit/spec/2026-09-14-spec-TOOL-aProbedUnit-4.md@14506117bf4f90b3b49e0f0c2b3e48da8e95b4e2` · `memory/builds/aProbedUnit/spec/2026-09-14-spec-TOOL-aProbedUnit-5.md@34fc3e6d3f2dc5ad0c6f5492d2866646c2ae3198` · `memory/builds/aProbedUnit/spec/2026-09-14-spec-TOOL-aProbedUnit-6.md@4c2ed15d36e390db45dc289d51a8b0945cca45c7` · `memory/builds/aProbedUnit/spec/2026-09-14-spec-TOOL-aProbedUnit-7.md@9aedc220bee125ec8acc2a83d8afefc52503899d` · ROUND 1.

## Verdict: BLOCKED

One defect blocks the set, and it is the build's own subject turned on itself. The README's rule three and unit 1's child paragraph forbid any suite or bar leg inside a pass; specs 1 and 4 name exactly those runs as the ONLY observation their criteria have, and both write the acceptance ledger in the pass commit, so the first child dispatched either breaks the rule this build exists to install or writes OBSERVED rows it did not observe. The same class recurs in specs 6 and 7 as a relabel. Beyond that, three criteria red against a correct build of their own spec (unit 5 AC3, unit 6 AC11) or reverse an owner ruling without a fork (unit 6's defaulted disposition), and the rest is repairable in place with the edits below.

**Review shape:** raw 60 · confirmed 32 · refuted 28 · unverified 0 · precision 0.53.

**Run integrity:** lenses 4/4 returned, 0 DIED; skeptic batches 5/5 returned, 0 DIED; 0 contradictory verdicts demoted to unverified, 0 spurious verdicts discarded, 0 duplicates. Every lens and every skeptic batch came back, so the finding set is complete for the lenses that ran, and a zero count below is positive evidence rather than the artefact of a dead lens. The pipeline's duplicate pass found none; the clustering below is this record's own, because several confirmed ids state one defect from different lenses and the fix is written once per defect. The per-id table keeps all 32 rows so the counts returned to the caller agree with what was adjudicated here.

**Adjudicated severities:** BLOCKER 3 · HIGH 7 · MEDIUM 9 · LOW 13. The three BLOCKER ids are one defect (cluster A) reported by two lenses across two specs; the seven HIGH ids are four defects; the nine MEDIUM ids are eight defects; the thirteen LOW ids are eight defects. Twenty clusters, nineteen distinct defects — clusters A and B are one class with two fixes.

Severity meaning in this record: BLOCKER — the set cannot be dispatched as written, a contradiction between the build's own rule and its specs that the roster must settle once, by one rule, before any pass starts. HIGH — a criterion cannot be observed, or reds, under a correct build of its own spec, or an owner ruling is reversed without the owner; fixable inside that spec. MEDIUM — a claim is false against source or a scope item has no observer, so a reader acting on it does the wrong thing, but a build can still land green. LOW — a figure, a carrier or a gate-list row does not reproduce; no verdict changes.

---

## Per-id severity table

| id | severity | unit | address | cluster |
|----|----------|------|---------|---------|
| 1 | BLOCKER | 4 | §6 preamble · §7 · §5 testing | A |
| 20 | BLOCKER | 4 | §7 · §6 preamble, against spec 1 §4 S1 and spec 7 §7 | A |
| 19 | BLOCKER | 1 | §6 AC1 AC3 AC4 AC5 AC7 AC8 · §4 S1 paragraph · §2 S6 · §7 · §4 Rollout | A |
| 21 | HIGH | 6 | §6 AC12, AC10, AC11 · §6 preamble · §7 | B |
| 8 | HIGH | 6 | §6 AC12 | B |
| 22 | HIGH | 7 | §7 second paragraph · §6 AC6 AC7 AC8 | B |
| 17 | HIGH | 5 | §6 AC3 · §2 S3 · §4 Rule 3 | C |
| 38 | HIGH | 5 | §6 AC3 · §4 Rule 3 · §2 S3 | C |
| 18 | HIGH | 6 | §6 AC11, against spec 1 §4 "The bytes" and §3 "No --bump" | D |
| 48 | HIGH | 6 | §4 The verb · §8 | E |
| 23 | MEDIUM | 6 | §3 "No new verb" · §4 The key, against spec 3 §3 and Edges | F |
| 51 | MEDIUM | 6 | §4 The key, against spec 3 §3 | F |
| 6 | MEDIUM | 5 | §6 AC7 · §2 S2 | G |
| 7 | MEDIUM | 6 | §6 AC10 · §2 S7 | H |
| 9 | MEDIUM | 3 | §7 New arm line · §2 S5 | I |
| 25 | MEDIUM | 4 | §4 The parent, the pinned GROUND sentence · §2 S2 · §6 AC3 | J |
| 52 | MEDIUM | 7 | §2 S6 S7 · §3 carrier inventory · §10 | K |
| 54 | MEDIUM | 1 | §4 "Four carriers, one rule", first paragraph | L |
| 3 | MEDIUM | 2 | §2 S3 · §6 AC2 | M |
| 10 | LOW | 3 | §2 S2 · §6 AC1 AC2 AC3 | M |
| 11 | LOW | 3 | §2 S4 · §6 AC6 | M |
| 13 | LOW | 3 | §2 S7 · §6 AC7 | M |
| 15 | LOW | 7 | §2 S4 · §6 AC4 | M |
| 16 | LOW | 7 | §2 S7 · §6 AC8 | M |
| 12 | LOW | 3 | §2 S3 · §4 step 4 · §6 | N |
| 31 | LOW | 6 | §7 gate list · §2 S8 · §6 AC11 | O |
| 33 | LOW | 6 | §3 second bullet, against spec 7 §3 and Edges | P |
| 35 | LOW | 5 | §5 testing line · §6 preamble | Q |
| 42 | LOW | 4 | §6 AC5 last sentence | R |
| 44 | LOW | 4 | §4 The parent · Files touched | S |
| 46 | LOW | 7 | §2 S5 · §4 "The comments that describe a shape the file no longer has" | S |
| 45 | LOW | 7 | §4 The prompt, the PROMOTE line · V1 | T |

---

## BLOCKER

### A — the pass is told to make an observation the build forbids: `TOOL-aProbedUnit-4` §6 preamble and §7 (ids 1, 20); `TOOL-aProbedUnit-1` §6 AC1 AC3 AC4 AC5 AC7 AC8 against its own §4 S1 paragraph, §2 S6 and §7 (id 19)

**Finding.** The build README's rule three reads "No self-test suite runs inside a pass of THIS build either", and unit 1 — order 1 — installs a child paragraph that bans "any leg of its manifest, any `*.test.sh` self-test suite" inside a pass and declares itself the override of any section 7 that says otherwise. Spec 4's section 7 then says the pass "verifies with `bash tools/workflows/unattended-build.test.sh`" run whole (335 s by spec 7's own measurement), and its section 6 preamble says each of AC1–AC5 "is observed by running it directly"; no per-arm form is named anywhere in spec 4, and the S6 fixture edits (every RESULT-expecting fixture gaining `scratch`) cannot be seen without the suite. Spec 1 says in its own section 7 that the pass runs NONE of the listed legs and verifies with AC6's double alone, while AC3 (`check-protocol-parity.test.sh`), AC5 (`check-template-size.sh`) and AC8 (`manifest-check.sh`) are purely leg invocations and AC1, AC4 and AC7 each carry one (`check-install-prefix.sh`, `kit-dogfood-parity.test.sh`, `adopt-unattended.sh --check`), all phrased "at the landed tip". Both specs put the acceptance ledger in the pass commit (spec 1 S6, its Rollout table; spec 4's section 7), and `memory/HYGIENE.md`'s ledger section admits only OBSERVED with a token naming the command that made the observation, or AMENDED. The first child dispatched therefore either runs the banned legs — the stall class this build exists to close — or writes ledger rows for observations it did not make. Spec 1's Rollout also misnumbers the parity criteria as "AC2, AC4 and AC7" where the protocol-parity leg is AC3.

**Why BLOCKER and not HIGH.** Each spec is fixable in place, but the defect is one wrong model of what a pass observes, written into four of seven specs (clusters A and B) by the same roster against a rule the same roster wrote into the README. Fixed per spec by four children, it yields four answers. It must be settled once, by one sentence in the README — "a pass observes the grep or the single arm; the leg or suite half of any criterion is the close's" — and then applied to all four specs before dispatch.

**Fix.** Spec 4: adopt spec 7's per-arm form in section 6 — source the suite's preamble up to `# ---- AC2: THE ARGS GUARD` from `tools/workflows/unattended-build.test.sh`, `run_wf` each named fixture, read the trace — for AC1–AC5, and rewrite section 7 so the whole-suite run is the close's compensating check, named as such. Spec 1: split each leg-shaped criterion into its pass-cheap grep (the ledger's OBSERVED token) and state the leg half as "observed at `--close`"; correct "AC2, AC4 and AC7" to "AC3, AC4 and AC7". README: add the one-sentence observation split to the build-level rules so the next spec cannot re-open the question.

**Left-shift.** A branch of hygiene check 23's token arm, armed by a build README that carries the phrase `No self-test suite runs inside a pass`: every backticked command in a spec's section 6 is joined against the argv column of `tools/gate-legs.json` and against `*.test.sh` filenames under `git ls-files`, and a hit REDS unless the criterion's own line carries `observed at --close`. Stage the break by pointing it at spec 4 as written.

---

## HIGH

### B — the same class, relabel form: `TOOL-aProbedUnit-6` §6 AC12, AC10, AC11 against its §6 preamble and §7 (ids 21, 8); `TOOL-aProbedUnit-7` §7 second paragraph against §6 AC6 AC7 AC8 (id 22)

**Finding.** Spec 6's preamble says the pass observes each criterion by the single command it names and the suites whole are the closing pass's, yet AC12's named command IS `bash tools/unattended/unattended.test.sh --shard 2/2` ("minutes"), and AC10 and AC11 name the `unattended kit gate`, `unattended skill wiring`, `build-method size`, `kit/dogfood doc parity` and `kickoff-manifest ratchet` legs that section 7 says the pass does not run. AC12 is wrong twice over: it assigns the shard to `--close`'s compensating run, `bash tools/unattended/run-unattended-gates.sh`, whose own help text says the suites run UNSHARDED, so the `FLOOR_SHARD_2` pin at `unattended.test.sh:5461` is read by nobody scheduled, and the over-pin-and-read-the-breach-line derivation it cites itself needs a suite run. Spec 7's section 7 says the pass verifies with the single-arm runs of AC1–AC5 "then the four grep pairs of AC6 through AC8", but those three criteria also carry six leg invocations (`check-workflow-syntax.js`, `check-protocol-parity.test.sh`, `kit-dogfood-parity.test.sh`, `check-template-size.sh`, `manifest-check.sh`, `adopt-unattended.sh --check`) that section 7 reserves for the close, and Rollout writes the ledger in the pass.

**Why HIGH.** Both specs already carry a per-arm or grep observation for the criteria's other half, so the fix is a relabel of the leg half, not a new observation — and it lands inside the spec once cluster A's rule is written.

**Fix.** Spec 6: give AC12 a per-arm observation (the sliced `review_state` calls and single `run --review` invocations AC3–AC6 already use), re-state its floor clause against the unsharded compensating run (`FLOOR_ASSERTIONS` only, the `FAIL` count read from the redirected output), and either drop the `FLOOR_SHARD_2` clause or name who runs the shard and when; mark AC10's and AC11's leg halves "observed at `--close`". Spec 7: reduce AC6–AC8 to their grep pairs for the pass and state the six leg runs as the close's observation of the same criteria.

**Left-shift.** The same check-23 branch as cluster A; it reds spec 6 AC12 and spec 7 AC6–AC8 as written, which is the staged break. For the shard floor specifically: `run-unattended-gates.sh` prints, beside its unsharded verdict, the line "shard floors `FLOOR_SHARD_1`/`FLOOR_SHARD_2` NOT graded by this run", so a reader never mistakes its green for shard coverage — the skip-announces-itself rule from `AGENTS.md` §7.

### C — `TOOL-aProbedUnit-5` §6 AC3 against §2 S3 and §4 Rule 3 (ids 17, 38)

**Finding.** AC3's allow control asserts `echo x > /tmpx/hyg` exits 0. Rule 3 (`posix-root`) denies any `/<top>/...` whose `<top>` is longer than one character and absent from `POSIX_ROOT_CONVENTIONAL`; the listed set is `dev proc sys usr etc var opt home root mnt media srv bin sbin lib lib64 run boot private volumes cygdrive workspace workspaces`, `tmpx` is four characters and not in it, `buildComparablePath` keeps the leading slash (the drive fold rewrites only `/<letter>/`), no home or allowed-root spelling claims it and `checkDriveRootLitter` needs a drive letter, so rule 3's `^/([^/]+)(/.*)?$` captures `tmpx` and denies it. The one arm that proves rule 2 is boundary-aware (`/tmpx` is not `/tmp`) is red at a correct tip by the unit's own rule 3; its "Red when" names only the bare-`startsWith` failure. The builder either weakens rule 3, adds `tmpx` to a set that is supposed to hold conventional roots, or rewrites the criterion after the fact.

**Fix.** Keep `/tmpx/hyg` and assert it exits 2 with the `posix-root` sentence and NOT the `tmp` sentence — that proves the `/tmp` boundary more sharply than an exit-0 control could — or re-target the allow control to a near-miss rule 3 does not claim (`/usr/tmpx/hyg`, `/c/tmpx/hyg`). State in section 4 that adjacent rules are discriminated by the deny KIND in stderr, not by exit status.

**Left-shift.** The scratch-guard suite's deny arms assert the kind sentence, never exit status alone, and the suite carries one table row per `check*` function in `tools/hooks/scratch-guard.js` with a deny arm AND an allow control each; a rule function with no row reds the suite. Stage the break by adding a `checkNoop` with no row.

### D — `TOOL-aProbedUnit-6` §6 AC11 against `TOOL-aProbedUnit-1` §4 "The bytes" and §3 "No --bump" (id 18)

**Finding.** AC11 requires `wc -c memory/guides/BUILD-METHOD.md` at the landed tip to be at or below the figure at base, pinned as 26743 at `1b000d1a` in the status header and RUN.md. Unit 1, order 1, lands +103 bytes on that render (26743 → 26846 by its own table) before unit 6 runs; unit 6's sentence swap is −13, leaving the file at about 26833, above the pin. The criterion cannot be observed green as written; the pass either amends it mid-build or records an untrue OBSERVED row.

**Fix.** Compare against the render at the pass's parent commit (`git show HEAD~1:memory/guides/BUILD-METHOD.md | wc -c`), or assert the swap's own delta (287 → 274 bytes) and leave the whole-file figure to the `build-method size` leg, which is what actually bounds it.

**Left-shift.** A `check-spec-tokens.sh` branch: a section 6 that pins an absolute `wc -c` figure for a path that ANOTHER spec of the same build names in its Files touched is a finding, with the remedy text "compare against the parent commit". The join is over data the check already reads (section 6 paths, Files touched paths); stage the break with spec 6 as written.

### E — `TOOL-aProbedUnit-6` §4 The verb and §8, against the 2026-09-01 owner ruling (id 48)

**Finding.** S3's defaulted `--disposition promote` reverses a recorded OWNER ruling of 2026-09-01 — `memory/builds/dFoldedVerdict/README.md` build-level rules and spec `TOOL-dFoldedVerdict-1` section 4: "a forced value is a constant, and a constant is not evidence for the clause that reads it — so the field stays evidence at every exit". Spec 6 cites `TOOL-dFoldedVerdict-1` only as "the refusal this unit deletes", never engages that reasoning, and section 8 records the default among three choices "made without a fork". The 2026-09-14 owner turn covers severity and round count, not the field's optionality, and the gotcha unit 6 cites governs which value a RUN writes on a mixed outcome, not a driver default. After the pass the decision log holds two live answers on whether the driver may write a disposition the run did not state, and check 2's clause 3 reads a driver-written constant — exactly what the earlier ruling refused.

**Why HIGH.** An owner ruling reversed by an agent decision with no fork is not a pass's call to make; but the spec has a second path that needs no owner (below), so it is fixable inside the spec.

**Fix.** Either raise it as a fork in section 8 with the 2026-09-01 ruling quoted, parked for the owner; or keep the flag REQUIRED and fix the harness recorder prompt at `tools/workflows/unattended-build.template.js:624` to pass `--disposition promote` explicitly (the alternative the spec rejected), citing the ruling as the reason the driver writes no default.

**Left-shift.** Ungateable structurally; a §10 checklist entry: before a spec makes a required driver flag optional or defaulted, run `python3 tools/memory-recall/query.py` for the flag name and cite every ruling it returns in section 10, naming which one this narrows or supersedes. `TOOL-cRefutedPremise-1` already records the sibling class.

---

## MEDIUM

### F — the delegated decision nobody took: `TOOL-aProbedUnit-6` §3 "No new verb" and §4 The key, against `TOOL-aProbedUnit-3` §3 "No shared bound reader" and its Edges (ids 23, 51)

**Finding.** Spec 3 states that `UNIT_STALL_BOUND` is instance two of the `GATE_BOUND` defaulted-validated-announced conf-read `case` block, cites the charter's instance-two extract rule, and hands the decision to unit 6 "which sees all three and lands after this one"; its Edges repeat the hand-off. Spec 6 writes the third inline block copied "verbatim" from `GATE_BOUND`, says "No new function or verb", mentions neither `UNIT_STALL_BOUND` nor a hoist, and its section 8 reads "none". The decision one spec of the set delegates to another is taken nowhere; the third copy lands with no recorded reason and the next key becomes a fourth.

**Fix.** Spec 6 section 4 or 8 records the call: hoist `read_bound_key <NAME> <DEFAULT> <NOTE>` and route all three through it, or reject extraction with a reason (the three sentences differ; `REVIEW_ROUNDS` carries an upper-bound arm the others lack) and say so where spec 3 pointed. Spec 3's Edge then names that line.

**Left-shift.** The build README already carries a `Parked decisions` section. A delegated decision is a row there — `<question> · handed to <unit> · resolved: <spec section or none>` — and the closing pass refuses a README whose table holds a row with `resolved: none`. Gateable as a hygiene arm over the README's own heading; stage the break with this build's README plus the row spec 3 should have written.

### G — `TOOL-aProbedUnit-5` §6 AC7 and §2 S2 (id 6)

**Finding.** AC7 is the only criterion observing S2's allow half (the `<os.tmpdir()>/claude` root), and by its own `fixture:` line it is a control, not a proof, on node `a`. `resolveAllowedRoots` (`scratch-guard.js:125-134`) already allows whatever `TEMP`/`TMP`/`TMPDIR` name, `os.tmpdir()` on Windows reads `TEMP` then `TMP`, so the new root is inside an allowed root whenever any is set; with all three unset it is `C:/Windows/temp/claude` and `windows` is in `DRIVE_ROOT_CONVENTIONAL`. Every registered node (`AGENTS.md` §2) is Windows, so on no node in the registry can this criterion fail whether or not the root was added: an owner ruling ("allows the CLI's scratch base") with no observable failing case, against `AGENTS.md` §7's first bullet on new gates.

**Fix.** Add a discriminating arm through `run()`'s fifth argument that sets `TEMP=/tmp TMP=/tmp` so `os.tmpdir()` derives `/tmp` on this node too, then grades `echo x > /tmp/claude/x` as allowed and `echo x > /tmp/other` as denied — or state in AC7 that the allow half is observed only on a POSIX node and name which node and when.

**Left-shift.** The cluster-C suite rule (deny arm AND allow control per rule function) plus a red-first rehearsal line in the spec's section 6: every allow control names the commit-local edit that makes it red (here, removing the root) and the "Red when" must be reachable on the building node or say which node it needs.

### H — `TOOL-aProbedUnit-6` §6 AC10 and §2 S7 (id 7)

**Finding.** `grep -c 'BOUNDED' tools/unattended/SKILL.template.md` prints 1 at base (line 694, "The bar it runs is BOUNDED"), so AC10's SKILL half is satisfied before the S7 edits — the new `BOUNDED` bullet, "one of four states" at :630 becoming five, the reconciling opening sentence, the default-disposition sentence — exist. Nothing else reads the Skill's state vocabulary: `adopt-unattended.sh --check` is render parity only, `check-unattended.sh` reads `NON-CONVERGENT` only from run-state rows, the harness suite's PV-AC12 arm compares the checklist command. A Skill left describing four states passes AC10 and `--check` alike. The VERBS half of AC10 does discriminate (0 at base).

**Fix.** Grep a phrase unique to the new text (the bullet's own opening, or `defaults to \`promote\``) printing 1, and assert `grep -c 'one of four states' tools/unattended/SKILL.template.md` prints 0 at the tip.

**Left-shift.** A pre-dispatch oracle run: `check-spec-tokens.sh` executes every section 6 `grep -c <pattern> <tracked path>` at the build's base sha and REDS when the asserted tip value already holds there — a criterion green before the work exists cannot observe the work. This also catches cluster R's oracle. Stage the break with AC10 as written.

### I — `TOOL-aProbedUnit-3` §7 New arm line and §2 S5 (id 9)

**Finding.** Section 7 says "no assertion floor exists in this suite, so none moves" about `tools/unattended/unattended.test.sh`; the suite pins an effective `FLOOR_ASSERTIONS=706` at :5434 (the 675 at :5403 is marked shadowed) plus `FLOOR_SHARD_1=208` and `FLOOR_SHARD_2=510`, selected at :5463-5465, and unit 6's AC12 pins against exactly that floor. The spec's non-goal about `ARMS_FLOORS` in `.memory-tree.conf` is a different pin. Sibling specs 5 and 6 raise their suites' floors by the arms they add; this unit adds the AC1–AC5 fixtures and three check-51 arms with no raise, so a stranded or unreachable check-51 arm is invisible, and unit 6's "exactly the added arms above 706" measures against a base already carrying these unpinned arms.

**Fix.** Add a criterion that `FLOOR_ASSERTIONS` rises by this unit's executed assertions above 706, derived from the suite's floor-breach line with the floor over-pinned (the method unit 6 AC12 cites), observed at `--close` per cluster A's rule; correct the section 7 line.

**Left-shift.** A `check-spec-tokens.sh` branch: when a spec's Files touched names a `*.test.sh` that contains a `FLOOR_` assignment, section 7 must carry a `FLOOR_` token, and the literal phrase "no assertion floor exists" against such a file reds. Both are greps over data the check already joins.

### J — `TOOL-aProbedUnit-4` §4 The parent, the pinned GROUND sentence, against §2 S2 and §6 AC3 (id 25)

**Finding.** The pinned string reads "goes under <scratch>, spelled absolute; never $TMPDIR, $TMP, $TEMP, /tmp, a bare mktemp, or any path outside the repository". The scratchpad it names as the destination is itself outside the repository — spec 4 places it under `%TEMP%` (section 8 F1's 170-character clone target) — so the last clause forbids the destination the first clause names. AC3 greps "a bare mktemp, or any path outside the repository" verbatim, so the contradiction ships into every GROUND-prefixed prompt as pinned bytes.

**Fix.** Spell it "or any OTHER path outside the repository" and adjust AC3's grep token to match.

**Left-shift.** No gate reads prose semantics; a §10 checklist entry — a pinned sentence of the shape "X; never ... any path outside Y" is checked once for whether X is inside Y — and the harness suite's AC3 arm asserts the corrected bytes so the wrong ones cannot come back.

### K — `TOOL-aProbedUnit-7` §2 S6 S7 and §3 carrier inventory, against `TOOL-aLeakedHandle-6` (id 52)

**Finding.** `TOOL-aLeakedHandle-6` (owner ruling 2026-09-13, `memory/DECISIONS.md`) landed the M4 sentence at `tools/memory-tree/BUILD-METHOD.template.md:143` — a blocker confirmed after CONVERGED "takes the exit's own disposition, FOLD or PROMOTE" — and the check-37 message at `tools/unattended/unattended.sh:4096`, "DISPOSED under the build method's M4, fold or promote". Under the severity rule a BLOCKER is never folded and a CONVERGED exit records no disposition at all (spec 7 section 5's stated cost), so "the exit's own disposition" has no referent. Spec 7 replaces only the :140 sentence; spec 6 section 4 explicitly keeps the fail-37 message. Neither carrier is in spec 7's inventory and the ruling is not cited. After the pass, M4 holds two answers for a late blocker on a converged subject and the driver's own refusal points at the old rule — the two-answers class the README's carrier rule exists to prevent.

**Fix.** Add `BUILD-METHOD.template.md:143` and the check-37 sentence to S6/S7 (or to unit 6's terminal-grep edit, which touches the same message), rewrite both to "takes the severity rule's disposition", cite `TOOL-aLeakedHandle-6` in section 10 as the ruling this narrows, and count the :143 bytes in section 4's M1 measurement.

**Left-shift.** A retired-phrase criterion, one per vocabulary move: `grep -rc 'fold or promote' <driver> <template> <render> <VERBS> <SKILL>` printing 0 at the tip, listed in section 6 and observed by the pass (it is a grep). Generalised: `tools/unattended/check-unattended.sh` gains a `retired-phrases` arm reading a list the kit ships, so a phrase retired once cannot return in any carrier. Stage the break with the :143 sentence.

### L — `TOOL-aProbedUnit-1` §4 "Four carriers, one rule, and which text binds", first paragraph (id 54)

**Finding.** "A sidechain child holds neither the Skill nor the charter" is refuted by a MEASURED record: `memory/guides/REVIEW-PROTOCOL.md:228-231` (2026-08-15, the sidechain's first message carried `CLAUDE.md` and the whole of `AGENTS.md`) and the charter's own §8 line "It DOES inherit the governing doc". Spec 1's section 1 already depends on the opposite ("reads ... template §1's gates green"). The inventory that section 4 says "names all four so the next change moves all four" omits the fifth carrier the child measurably reads — the charter's §1 DoD "Gates green" line — so the next vocabulary move skips it, and the spec ships a refuted premise, the class `TOOL-cRefutedPremise-1` records and `TOOL-dUnstalledConvoy-16` records recurring on this exact claim.

**Fix.** Rewrite the paragraph to the measured fact (the child holds `AGENTS.md` and the hooks; it does not hold the unattended Skill), cite REVIEW-PROTOCOL.md's measurement, and either add the charter's §1 DoD line to the inventory with the reconciling sentence section 4 already drafts ("a pass is finer than the work-unit; the unit's gates-green is met at the close") or state why the charter is deliberately not edited.

**Left-shift.** Ungateable as prose; a §10 entry keyed on the recurrence: any sentence about what a sidechain "holds" or "inherits" cites REVIEW-PROTOCOL.md's measured section, and a memory-recall probe for `sidechain inherit` is a DoR item for a spec touching the harness prompts.

### M — "Observed by ACn" where the AC observes nothing of the item: `TOOL-aProbedUnit-2` §2 S3 (id 3, MEDIUM); `TOOL-aProbedUnit-3` §2 S2, S4, S7 (ids 10, 11, 13, LOW); `TOOL-aProbedUnit-7` §2 S4, S7 (ids 15, 16, LOW)

**Finding.** Six scope items cite an acceptance criterion that does not observe them, and the hygiene scope-join arm grades only that an S item names an AC label. id 3: spec 2's S3 (the `has` arm beside unit 1's) says "Observed by AC2", but AC2 observes only the `grep -c` count over the traced prompt and the ordering of two paragraphs; no criterion asserts the `has` line exists in `tools/workflows/unattended-build.test.sh` — sibling spec 1 AC6 carries that clause and spec 2 dropped it. A pass that lands the paragraph and skips the arm satisfies every criterion, and the class reader for "the child lost the rule" is optional in practice; MEDIUM because that arm is the reader for the build's headline mechanism. id 10: spec 3's S2 requires the openness predicate be hoisted into one function both `--dispatch` and `--audit` call "rather than copied", but AC1–AC3 observe only `--audit`'s behaviour, so a verbatim copy of `unattended.sh:4802-4815` passes. id 11: S4 lists `tools/unattended/kit.toml` `optional_keys` as a carrier of `UNIT_STALL_BOUND`, but check 22 (`check-unattended.sh:1630-1689`) joins the protocol table, the example conf and the project conf only, and no criterion greps `kit.toml` (spec 6 AC10 does, for `REVIEW_ROUNDS`). id 13: S7 says the dossier `memory/map/features/unattended.md` names `--audit` in its keepalive paragraph; AC7 measures only its byte cap, and the dossier sits at 20470 bytes today, so an untouched dossier passes. id 15: spec 7's S4 says every non-throwing exit past the stage carries `promoted` and `folded`, naming the attended every-unit-terminal return at template line ~851 among three; AC1, AC2 and AC5 reach the main and degraded returns, AC4's `A_UNITS` fixture has `planState READY` so it also exits via the main return and asserts only the prompt line, and the existing T_UNITS arm asserts only `standing` and roster — that return can omit both keys, the missing-key-versus-stated-zero distinction the file itself refuses at 895-899. id 16: S7 edits the `CONVERGED` bullet and replaces a VERBS clause with a pointer; AC8 greps only the NON-CONVERGENT bullet's `DISPOSED BY SEVERITY` and the ABSENCE of the old VERBS clause, so the CONVERGED bullet can stay unedited and VERBS can lose its clause without gaining the pointer. (The third sub-claim of id 16, a capitalised reuse redding the exact-1 count, is speculative — the design's CONVERGED clause is lowercase — and is not carried here.)

**Fix.** One grep each. id 3: AC2 gains `grep -cF 'YOUR PRIMARY OBJECTIVE IS CODE WRITTEN AND COMMITTED' tools/workflows/unattended-build.test.sh` printing 1 at the tip and 0 at base. id 10: AC3 gains `grep -c 'check_pass_open' tools/unattended/unattended.sh` printing at least 3 (one definition, two call sites), and the same for `scan_dirty_paths` with `check_clean` as its second caller. id 11: AC6 gains `grep -c UNIT_STALL_BOUND tools/unattended/kit.toml` printing 1. id 13: AC7 gains `grep -c -- '--audit' memory/map/features/unattended.md` printing at least 1. id 15: AC4 asserts its RESULT line carries `"promoted":0,"folded":2`. id 16: grep a phrase unique to the CONVERGED clause (`still disposed`) printing 1 in template and render, and the VERBS pointer's own phrase (`severity rule`) printing 1 in `tools/unattended/VERBS.template.md` and `memory/guides/UNATTENDED-VERBS.md`.

**Left-shift.** Extend the hygiene scope-join arm with the rule check 23's `LEDGER_TOKEN` branch already applies to ledger rows: an S item and the AC it names must share a backticked token, case-folded, either way round. An S item naming `kit.toml` whose cited AC never spells `kit.toml` is a finding. One arm covers all six ids; stage the break with spec 3's S4.

---

## LOW

### N — `TOOL-aProbedUnit-3` §2 S3 and §4 step 4, the deletion case (id 12)

**Finding.** Section 4 step 4 says a listed path that no longer exists "has no mtime and is skipped"; step 5 makes a `stat` that answers nothing the third check-51 refusal. AC1 uses a clean tree, AC2 an untracked `touch`, AC5 a shadowed `stat` over a dirty tree; no criterion puts a deleted tracked file in the dirty set. An implementation that runs `stat` over every listed path and treats any failure as a dead probe passes all of AC1–AC5 and then refuses with check 51 on every unit that deletes a file, so the keepalive reads a broken verb instead of a verdict. The skip branch is designed, unobserved, and confusable with the branch that is observed.

**Fix.** Add an AC2-shaped arm: delete a tracked file on disk in the fixture (`git rm --cached` is not enough) and assert the verdict line prints rather than the check-51 sentence.

**Left-shift.** The suite rule from cluster C, applied to verbs: every refusal number a verb can print has one arm that reaches it and one control that reaches the branch it is most easily confused with; the unattended suite's arm table is greppable for `fail 51` and the control is the deletion fixture.

### O — `TOOL-aProbedUnit-6` §7 gate list against §2 S8, §4 The method and §6 AC11 (id 31)

**Finding.** `memory/guides/SESSION-KICKOFF.md`'s watch line names both `.unattended.conf` and `memory/guides/BUILD-METHOD.md`; spec 6 S7 edits the conf, S8 edits the method render and re-stamps `last-audit`, and AC11 runs `skills/session-kickoff/manifest-check.sh`, the argv of the `kickoff-manifest ratchet` leg in `tools/gate-legs.json`. Section 7 says "These are the legs `--close` runs" for this diff and omits that leg, while specs 1, 3 and 7 list it for the same obligation.

**Fix.** Add `kickoff-manifest ratchet` to section 7 with its chunk, as specs 1 and 7 do.

**Left-shift.** A `check-spec-tokens.sh` branch: a spec whose Files touched names a path on the manifest's watch line must list `kickoff-manifest ratchet` in section 7. The watch line is machine-readable and the check already reads Files touched; stage the break with spec 6 as written.

### P — `TOOL-aProbedUnit-6` §3 second bullet against `TOOL-aProbedUnit-7` §3 "No backlog row" and its Edges (id 33)

**Finding.** Spec 6 says backlog row `TOOL-aProvenReuse-3` "is unit 7's to close"; spec 7 says no backlog row is edited in its pass (`fail 49` refuses the declaration, because `memory/backlog` is in `SHARED_RECORDS` in `.unattended.conf` and `--dispatch` refuses a declaration overlapping one) and hands the flip to the closing pass. Two owners named for one status flip, one of them impossible; the closing pass may read spec 6 and assume unit 7 did it.

**Fix.** Spec 6 points at the closing pass, matching spec 7's Edge.

**Left-shift.** A backlog id named by any spec in a build as "to close" is listed once in the build README's roster with its closer — the README already carries the roster table — and a documented closing-pass check reads that list and nothing in a spec's section 3. Cluster F's `Parked decisions` arm can carry this row shape too.

### Q — `TOOL-aProbedUnit-5` §5 testing line and §6 preamble (id 35)

**Finding.** Section 5 counts "eight red-first denials, seven allow controls"; counted from section 6 itself, denial arms are AC1, AC2, AC3, AC4, AC6, AC8 (six) and allow controls AC1(1), AC2(1), AC3(1), AC4(3), AC5(1), AC7(1) (eight); the preamble says "all six shapes named in AC1 to AC4" where AC1–AC4 name four (the six are those plus AC6 and AC8, which AC10 lists correctly). Two prose counts of a population AC10 says is derived at observation, disagreeing with the criteria and with each other — `AGENTS.md` §7's no-count-in-prose rule.

**Fix.** Drop the counts from section 5 and the preamble (AC10 derives the figure), or make them agree with the criteria as numbered.

**Left-shift.** A `check-spec-tokens.sh` grep over sections 5 and 6 prose for `<number-word or digits> (arms|denials|controls|assertions)` in a spec whose section 6 carries a derivation clause; the remedy text is "point at the derivation". Small, and it reds this spec as written.

### R — `TOOL-aProbedUnit-4` §6 AC5, last sentence (id 42)

**Finding.** `grep -c 'function ' tools/workflows/unattended-unit.js` prints 2 at base, not 1: line 4 is a comment reading "function with the hooks injected", and only line 71 is the definition. The oracle "stays 1" reds the correct landed state and does not measure the second-top-level-definition class it claims; the intent (one definition, `check`) is right, the pinned figure is wrong.

**Fix.** Spell the oracle as `grep -cE '^(async )?function ' tools/workflows/unattended-unit.js` stays `1`, the definition scan the codebase-map's JS layer actually performs.

**Left-shift.** Cluster H's pre-dispatch oracle run: executed at base, this grep prints 2 against a pinned 1 and the criterion is refused before a child meets it.

### S — carriers the inventory missed: `TOOL-aProbedUnit-4` §4 The parent and Files touched (id 44); `TOOL-aProbedUnit-7` §2 S5 and §4 "The comments that describe a shape the file no longer has" (id 46)

**Finding.** id 44: the harness's inputs contract lives in its own header comment at `tools/workflows/unattended-build.template.js:135-146` (`{ repo … slug … mode … }`) and lists every arg the file takes; unit 4 adds a REQUIRED `scratch` arg and enumerates its carriers (refusal text, Skill bullet, dossier args contract in S7) but never that block, so the one place a caller reads the contract from the script omits the argument the script now refuses without — the same missing-carrier class S5 fixes for the Skill. id 46: `meta.phases[2].detail` at `tools/workflows/unattended-build.template.js:9` reads "dispose every blocker still standing over the whole spec set"; after unit 7 the stage disposes every CONFIRMED finding by severity, so that exported description — the one every `meta`-scanning reader sees — is a fourth carrier of the replaced predicate, absent from S5's three-row table (lines 55-58, 613-615, 704-719).

**Fix.** id 44: add the `scratch: "<absolute session scratchpad>" // REQUIRED` row to the inputs block in section 4's Files touched table. id 46: add line 9 to S5's table with the severity wording.

**Left-shift.** Cluster K's retired-phrase criterion (`blocker still standing` printing 0 across the harness files) covers id 46. For id 44, the harness suite's args arm asserts every key the refusal names appears in the header's inputs block — a grep over the file's own first 150 lines, staged red by the spec as written.

### T — `TOOL-aProbedUnit-7` §4 The prompt, the `[unattended] PROMOTE` line, and V1 (id 45)

**Finding.** The spelled promotion command `<DRIVER> --rescope <slug> --act add --item <id>` omits `--reason`, which `verb_rescope` refuses without (`unattended.sh:4571`, `fail 48`) and the driver's header at line 14 lists as required. The unit rewrites the prompt and carries the incomplete invocation forward, so the disposal agent's first promotion as spelled is refused. The finding's second half is overstated and not carried: V1's `has` is a substring match on `--rescope tB --act add`, so adding `--reason` to the prompt keeps that arm green.

**Fix.** Spell `--rescope <slug> --act add --item <id> --reason <text>` in the prompt; V1 may assert the longer substring.

**Left-shift.** A harness-suite arm that extracts every `<DRIVER> --<verb>` line the template spells and asserts each carries the flags the driver's own header marks required for that verb — the header is the source, so the arm cannot drift from it. Stage the break with the prompt as written.

---

## What this round did not cover

The build README's owner-answer paragraph and its build-level rules were read as binding and not audited; every finding above measures a spec against them, none contests them. Cluster A's fix asks the README for one more sentence, which is a completion of rule three and not a change to it. The specs' cost figures (spec 7's 335 s suite measurement, spec 1's 26743 → 26846 byte table, the 20470-byte dossier) are taken as the specs and the skeptics report them; only the byte figure in cluster D was reasoned about, not re-measured. `RUN.md` and the `prompts/` folder were not in scope. The refuted 28 are not listed here; the pipeline holds them, and none was demoted rather than refuted.

Precision 0.53 sits just above the ~0.5 floor `AGENTS.md` §8 sets, so the lens priming holds for a round 2 on this set without adding agents; the useful tightening is the one this round's survivors already show — every finding that lived carried a `file:line` from the tree, not only a section address in the spec.
