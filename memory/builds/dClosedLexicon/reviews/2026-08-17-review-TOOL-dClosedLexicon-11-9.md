**Serves:** spec-audit TOOL-dClosedLexicon-11..13  <!-- inferred: its H1 names the three specs it audits -->

## Verdict: BLOCKED

**review-dClosedLexicon-9 — M4 spec audit of the three specs closing `TOOL-dClosedLexicon-11`, `-12`,
`-13`** · node d · 2026-08-17 · base `b4f0cf1c`

**Subjects:** `spec/2026-08-17-spec-dClosedLexicon-11.md` · `-12.md` · `-13.md`, all at rev-1, all
authored this run and therefore unreviewed by definition (M4).

**Shape:** four lenses, 41 raw findings; batched skeptics refuted 9; 32 survived and collapse to
**23 distinct defects**. Three are blockers and all three are in spec 11 — the unit cannot be built
as written, because two of them make its own headline acceptance criterion unreachable and the third
puts a tracked file in the tree that the merge bar rejects. Specs 12 and 13 are CLEAN WITH FIXES on
their own: spec 12's numbers reproduce exactly and its conclusion holds; spec 13's design is right and
its two mapping rationales are measurably wrong for four named rules.

| | 11 | 12 | 13 |
|---|---|---|---|
| distinct defects | 11 | 4 | 7 |
| blockers | **3** | 0 | 0 |
| §10 probe claim reproduced? | NO | NO | NO |

**Stop rule (M4):** fold these into a rev-2 of each spec with its §9 line, then re-review spec 11
only. Specs 12 and 13 do not need a second audit once their fixes land — nothing below changes their
shape.

---

# Spec 11 — `a build may have more than one unattended run`

The problem this unit names is REAL and correctly diagnosed: `refuse_if_terminal`
(`unattended.sh:574-581`) is the single branch every phase writer routes through, and it does refuse
`--preflight` on a terminal record. Rotation is the right answer. What is wrong is everything about
WHERE the rotation runs, WHAT it produces, and one acceptance criterion that describes behaviour the
kit has never had.

## [BLOCKER] 11-B1 — AC4 names a refusal that does not exist, and building to it regresses a gated arm

*(§6 AC4, §5 error/empty states, §2 S5 — consolidates ids 0.0 and 3.0)*

AC4 reads "When the run-state file is NON-terminal, `--preflight` still refuses exactly as before."
`--preflight` has never refused a non-terminal record. `refuse_if_terminal` returns 0 for every
non-terminal phase (`unattended.sh:578`, `[ -n "$cur" ] && is_terminal "$cur" || return 0`);
`verb_preflight` then skips scaffolding when the file exists (`:851`) and preserves an existing phase
(`:878`); `check_single_live` (`:432-442`) passes at `n <= 1`, so the build's own live record is
explicitly allowed. The driver's own comment at `:875-877` says the opposite of AC4 in as many words —
"Preflight used to rewrite this unconditionally, so a resumed run that had reached BUILDING was
silently moved back to RUNNING by the verb it is told to re-run after a compaction."

This is a blocker rather than a wording slip because a **gated arm asserts the contrary**.
`tools/unattended/unattended.test.sh:532-544` sets `phase: BUILDING`, commits, re-runs `--preflight`
and asserts both `preflight OK` and "a re-run preflight leaves a reached phase alone". An
implementation satisfying AC4 literally reds that leg. §5 repeats the false claim ("a build whose
record is NON-terminal is still refused") and S5's arm inherits it.

Recorded as REFUTED, so it is not folded: S5's clause "still refused by every verb that refused it
before" is NOT a dead probe — `--landed` (fail 31, `:733-737`) and `--phase` (fails 15 and 19) do
refuse a non-terminal record, so the quantifier is non-empty. It simply must not include
`--preflight`.

**FOLD.** Replace AC4 with the property that is observable and actually at risk: *"When the run-state
file is NON-terminal, `--preflight` does NOT rotate it — the file keeps its name, its recorded phase
and its parked entries, no `RUN.*.md` appears, and the verb exits 0 as it does today."* Restate the §5
error-states line and S5's arm the same way, and name `unattended.test.sh:543-544` in S5 as the
existing arm the new behaviour must leave green.

## [BLOCKER] 11-B2 — rotation placed before the precondition block makes `--preflight` refuse itself

*(§5 security, §4, §10 — consolidates ids 2.0 and 1.0)*

§5 states "Rotation happens BEFORE those checks, so a refusal still leaves no fresh record", and §10
pins the change to one call site — `refuse_if_terminal`, which is called at `unattended.sh:821`. The
precondition block follows immediately: `observe_anchor` (`:826`), `check_clean` (`:827`),
`check_branch`, `check_wiring`, `check_single_live`, then `trusted_base` + `check_authorization`
(`:841-843`), with the single write gate at `:847`.

`check_clean` (`:386-397`) counts `git diff --name-only` + `git diff --cached --name-only` +
`git ls-files --others --exclude-standard` and `fail 2`s on any non-zero count. **The rotation is what
makes the tree dirty.** MEASURED in a scratch repo: `mv RUN.md RUN.ABORTED.abc12345.md` plus a fresh
`RUN.md` → count 2; `git mv` plus a fresh `RUN.md` → count 2; `git mv` alone → count 1. Every variant
is non-zero. So a rotating `--preflight` on a terminal record ALWAYS reaches `:847`, prints the literal
string `unattended: --preflight refused; the run-state file is unchanged`, and returns 1 — over a tree
where the retired record has already been renamed away and no file exists at the path `--resume`,
`check-unattended.sh:137` (`^$M/builds/[^/]+/RUN\.md$`) and every reader glob look for. **AC1 ("both
exist afterwards") is unreachable.**

The ordering also breaks the invariant the file states twice, at `:845-846` and `:849`: "NOTHING is
written until every precondition above has passed. A verb that writes and then discovers a refusal has
already changed the state the refusal was about." And §5's justification is a non-sequitur about the
wrong artefact — the harm is the retired record leaving the reader path, not a fresh record appearing.

**FOLD.** State in §4 exactly where rotation runs: the **collision TEST** runs with the other
preconditions (before `:847`, so a colliding archive name refuses while the tree is untouched), and the
**rename** runs after the `[ "$status" = 0 ]` gate, in the same position as `scaffold_runmd`. Rewrite
the §5 security bullet to "rotation happens AFTER every precondition, so `the run-state file is
unchanged` stays true on every refusal path", and add an S5 arm asserting a rotating `--preflight`
exits 0 on an otherwise-clean tree.

## [BLOCKER] 11-B3 — the archive name reds memory-hygiene check 4, which §4 rejected another name for

*(§2 S2, §4, §6 AC1/AC6, §7 — id 3.1)*

`check-memory-hygiene.sh:284` whitelists exactly `F:README.md`, `F:STATUS.md`, `F:RUN.md`,
`D:prompts`, `D:spec`, `D:build`, `D:reviews` at a build-folder root, and `:285` requires every other
FILE to match the recording grammar `rre` at `:274`. This build's own record is `phase: ABORTED`,
`witness: 365be1c7…` (`memory/builds/dClosedLexicon/RUN.md:12-13`), so the name S2 produces is
`RUN.ABORTED.365be1c7.md`. **REPRODUCED** by running check 4's awk verbatim over
`git ls-files memory/` plus that path — the only line printed was
`memory/builds/dClosedLexicon/RUN.ABORTED.365be1c7.md`. Check 4 has no waiver path
(`legacy-files.txt` grandfathers check 5 only) and no `in_debt`/`in_scope` filter.

§4 rejects the `runs/<seq>.md` alternative *because* it "collides with hygiene check 4's folder
grammar" — without noticing that the chosen name collides with the same check. The gate's own comment
at `:260-266` records that admitting `RUN.md` required amending this whitelist; the spec schedules no
equivalent amendment. §4's Files-touched list names neither `tools/memory-tree/check-memory-hygiene.sh`
nor the `KIT_MEMORY_TREE_VERSION` bump that editing a non-comment line of it forces via the
verdict-epoch leg, and §7 lists only the four unattended commands.

One framing correction, recorded: AC1 and AC6 *can* both hold, because the self-tests build scratch
repos. The failure is that the first dogfooded second run — this build — writes a TRACKED file the
merge bar rejects.

**FOLD.** Pick one and write it into §2, §4 and §7: either (a) add `RUN.*.md` to check 4's whitelist,
with `tools/memory-tree/check-memory-hygiene.sh`, the `KIT_MEMORY_TREE_VERSION` bump,
`check-verdict-epoch.sh` and `check-memory-hygiene.test.sh` added to Files touched and Gates, and the
memory-tree kit version pair priced; or (b) choose a name check 4 already admits under the build's own
`build/` folder. Whichever you pick, add an AC asserting `bash tools/memory-tree/check-memory-hygiene.sh`
is green with a rotated record present in the index.

## [MAJOR] 11-1 — S2's "which is the same run" is false, and AC3 then refuses forever with no way out

*(§2 S2 vs §6 AC3, with §3 foreclosing the remedy — id 0.5)*

S2 argues two runs cannot collide "unless they ended at the same phase AND the same witness, which is
the same run". The witness is HEAD at the moment the phase was written — `verb_abort` does
`head=$(GIT rev-parse HEAD)` then `set_fact … phase ABORTED` / `witness "$head"`
(`unattended.sh:808-810`) — and **no driver verb commits**: `stage_or_fail` (`:553-561`) calls
`stage_runmd` (`:545`), which is `GIT add` only, and `grep -c "git commit"` over `unattended.sh` and
`check-unattended.sh` returns 0 for both. So run A aborts at commit W; run B preflights, builds
nothing, aborts — its witness is also W; run C computes the identical archive name, finds it present,
and per AC3 refuses and writes nothing. The archive name is derived from the RETIRED record, so the
collision is frozen: no verb can repair it, §3 forecloses a run index, and no §5 or §8 line names an
operator path out. The unit then reproduces its own §1 problem statement one abort later — and the
driver already carries this exact class in writing at `:855-858`: "the refusal named a remedy that did
not exist."

**FOLD.** Delete the "which is the same run" sentence — the code refutes it — and make the derived
name total by appending a fact the finished record already carries and that a second run cannot
duplicate (`keepalive` id, or `base`), so "derived, not chosen" survives while distinct runs cannot
alias. If you keep the two-part name instead, add a §2 item and an AC naming the exact operator act
that clears a legitimate collision and what it may touch.

## [MAJOR] 11-2 — nothing says rotation stages the rename, so the archive is invisible to the leg

*(§2 S3, §4, §6 AC5 — id 2.1)*

S3 widens the leg's population to `RUN.md` PLUS `RUN.*.md`, which assumes the archived record is
TRACKED. `check-unattended.sh:132` builds that population from the INDEX (`FILES=$(git ls-files "$M/")`,
selected at `:138`), and the driver states the consequence in writing at `unattended.sh:558-560`: "the
gate leg's whole per-run population is the index, so an unstaged run is invisible to every check it
has". CONFIRMED in a scratch repo that a plain `mv` leaves the archive as `??` — untracked. Nothing in
S1, S2, §4 or S5 says the rotation stages either side, and `scaffold_runmd`/`stage_runmd`/`stage_or_fail`
(`:525-561`) stage only `RUN.md`.

The S5 arm for AC5 would not catch it: `check-unattended.test.sh` commits its fixtures (`git add -A &&
git commit -q -m base --no-verify` in the setup block), so a hand-built archived record is tracked in
the test and untracked in production — this repo's own `fixture-passes-by-finding-nothing` class.

**FOLD.** Make S1 state that rotation stages BOTH sides (`git mv`, or `git add` the archive plus
`git rm --cached` the old path) and route it through `stage_or_fail` so the existing refusal covers it;
add to S5 an arm asserting the archived path appears in `git ls-files` after a REAL rotation, not only
in a hand-built fixture.

## [MINOR] 11-3 — S4 is the one scope item with no AC and no gate that could see it

*(§2 S4 vs §6/§7; §5 user docs — id 0.4)*

AC1–AC5 name only `--preflight`, the archived bytes, the collision refusal, the non-terminal case and
`check-unattended.sh`; AC6 is the whole bar. Neither §7 gate can see protocol CONTENT:
`check-unattended.sh`'s protocol leg (`:377-393`, `fail 10`) is a byte-diff of `PROTOCOL.template.md`
against `memory/guides/UNATTENDED-PROTOCOL.md` — green whatever either says — and
`adopt-unattended.sh --check` diffs the rendered SKILL.md against template+conf and greps for surviving
`{{…}}`. §5 also names a second doc deliverable, "the Skill's 'Start a run' step", which appears in no
S-number and is absent from §4's Files touched.

**FOLD.** Give S4 an AC with an observation — e.g. *"`check-unattended.sh` asserts that the installed
protocol's §2 names the archive filename grammar; a rotation shipped with a protocol that does not
describe it reds"* (content-grepping a doc is an established idiom here — check 12 greps the kickoff
engine's READY string). Then either add an S-number plus a Files-touched entry for
`tools/unattended/SKILL.template.md` and the rendered `.claude/skills/unattended/SKILL.md`, or drop
that clause from §5.

## [MINOR] 11-4 — an existing gated arm asserts the opposite of S1, and the spec says arms are only ADDED

*(§2 S5, §5 testing, §7 — id 2.2)*

`unattended.test.sh:919` drives all five phase writers over a LANDED record, `--preflight` among them,
asserting for each `hit "$out" "the run is already finished…"` (`:922`) and
`same "the finished record survived $v" "$(sum)" "$before"` (`:923`), where
`sum() { git hash-object memory/builds/tRun/RUN.md; }` (`:137`). Under S1 both assertions must fail for
the `--preflight` member, and the `sum()` operand must move to the archived path. §7 says "No new leg;
arms are added to legs already on the bar" and §5 says "S5, on two legs that already ride the bar" —
neither admits an arm that must CHANGE. Note the arm above it derives the 5-writer population from
source (`writers=$(grep -c 'set_fact "$rel" phase' "$SCRIPT")`, `:912`), so the drive list is not free
to shrink silently.

**FOLD.** Add to S5 that the drive list at `unattended.test.sh:919` drops `--preflight` and gains a
replacement arm proving `--preflight` rotates while the other four still refuse, with the byte-identity
assertion re-pointed at the archived path.

## [MINOR] 11-5 — nothing constrains an ABORTED record's witness to a sha, so the derived name can carry a separator

*(§2 S2, §4 "The name carries its own provenance" — id 2.4)*

The leg gates the witness in three places and none constrains a non-LANDED record: check 5
(`check-unattended.sh:216-218`) asserts PRESENCE only; check 6 (`:222-227`) matches `[0-9a-f]{7,}` and
comments the rest "not sha-shaped: unjudgeable, and skipping it is the discipline, not an omission";
the sha-shape refusal at `:239-244` is guarded by `if [ "$ph" = LANDED ]`. `PHASES_TERMINAL` is
`LANDED ABORTED` (`unattended.sh:74`), so a record reading `phase: ABORTED` / `witness: tag/v1` passes
the whole leg and `RUN.<phase>.<witness8>.md` becomes a path with a separator in it. The driver always
writes a sha, so this needs a hand-edited record — but that is the model this kit adopts in writing
elsewhere (`check-unattended.sh:269`, "the record is written by the run — an absent pin is not a
satisfied one"), and "the name cannot be chosen" is the sentence carrying S2's collision argument.

**FOLD.** Have S1 refuse to rotate unless the retired record's witness matches the sha shape the leg
already spells, and qualify §4's "the name cannot be chosen" accordingly; add an S5 arm over a terminal
record with a non-sha witness.

## [MINOR] 11-6 — §4 credits the protocol pair to check 15; it is check 10

*(§4 Files touched — consolidates ids 1.8 and 2.3)*

`check-unattended.sh:377` opens "---- 10: the kit ships what this repo runs. ONE pair.", with `fail 10`
at `:388` and `:392`. Check 15 is the LANDED-witness pair (`:242` shape, `:319` ancestry) — separately
load-bearing here, since S3 puts archived LANDED records into that same population.
`check-unattended.test.sh:266` arms "check 10, both branches" for exactly this drift.

**FOLD.** Correct §4 to "kept byte-equal by check 10", and add one line stating what checks 15, 9 and
13 will now assert over every archived record once S3 widens the population.

## [MINOR] 11-7 — §7 omits the leg that judges the kit version pair, which §4 says the unit moves

*(§4 vs §7 — id 1.9)*

§4 lists "the kit version pair"; §7 lists only the four unattended commands. The pair is judged by
`tools/check-kit-versions.sh:99-105`, which derives its value from `^KIT_UNATTENDED_VERSION=` in
`unattended.sh` and requires the same literal in `check-unattended.sh`. It is a bar leg
(`tools/gate-legs.json` carries `{"name": "kit version markers", "argv": ["bash",
"tools/check-kit-versions.sh"]}`). Sibling spec -12, whose §4 also lists "the kit version pair", DOES
list it in §7. Two specs from one pass answer the same question two ways.

**FOLD.** Add `bash tools/check-kit-versions.sh` to §7.

## [MINOR] 11-8 — the §10 probe result is asserted, not measured

*(§10 — id 1.4)*

RE-RUN on this tree: `python tools/codebase-map/reuse_lookup.py "retire a record and start a fresh
one"` piped through `grep -inE "rotat|archive"` matches nothing (rc 1). The candidates are `records`,
`extract_records`, `test_generated_artifacts_are_fresh`, `zero_record_diagnosis`,
`strip_records_sentence`, `t_zero_records_is_loud` plus dossier and inventory rows. §10 claims it
"surfaces the memory-tree kit's index ROTATION" — that rotation is a prose discipline in
`check-memory-hygiene.sh:373` and `:468-474`, not an indexed symbol, so the probe cannot surface it.
The reuse DECISION is sound and hand-verifiable; only the attribution is false.

**FOLD.** Record what the probe actually returned and that it MISSED the precedent — M5 makes "nothing
found" an ANSWER to record — and cite the rotation precedent directly (check-memory-hygiene checks 6
and 10, `HYGIENE.template.md` §"Index budgets, caps, rotation") as hand-verified.

---

# Spec 12 — `the census question, measured`

The unit is sound and its conclusion holds. Every census number in §1 reproduces exactly, the JS hole
is real, and refusing the coupling is right. Four fixes, none structural.

## [MINOR] 12-1 — §1 contradicts its own table, and AC2's floor is exactly 3 too low

*(§1 third bullet vs the §1 table; §6 AC2 — consolidates ids 0.1 and 1.10)*

RE-DERIVED on this tree with the lexicon's own `js-regex` set (`tools/lexicon/lexicon.py:97-105`): the
six tracked `tools/**/*.js` yield **30** definitions — `agent-cap.js` 19, `recall-opened.js` 4,
`check-workflow-syntax.js` 1, and 2 each from `drift-audit-code.js`, `drift-audit-state.js`,
`tier2-review.js` — and **none is named `meta`** (the arrow pattern cannot see `export const meta = {`).
`memory/map/generated/symbols.json` carries 426 rows, of which exactly 3 are `.js`, all
`{"id": "meta", "kind": "const-export"}`. So the index carries **ZERO** of the 30 — which is precisely
what §1's own table row `map-only | 3` asserts, contradicting the bullet four lines below it: "The
recall index carries **3** of them". The post-union count deduped on `(id, file)` is 30 + 3 = **33**,
so AC2's "at least 30 and still include the three `meta` rows" is satisfied by an extractor that finds
only 27 of the 30, and the AC's own inference ("so the union kept both sources") is broken by the same
3. Filed minor because AC4's cross-check arm backstops it: it reds on exactly that 27-of-30 extractor,
and the lexicon is present in this repo so the arm runs rather than skips.

**FOLD.** Correct the §1 bullet to *"the recall index carries NONE of them — its three `kit-js` rows
are the `meta` blocks, which the definition probe cannot see; that is the table's map-only 3"*, and
restate AC2 as *"`kit-js` rows number at least 33 — the 30 measured definitions PLUS the three `meta`
rows"*.

## [MINOR] 12-2 — §3's OUT forbids what S5 builds and AC4 accepts

*(§2 S5 vs §3 — id 1.1)*

§3's first OUT is maximally broad: "Any consumption of a lexicon-owned census by the map, in either
direction, mandatory or optional." S5 is an optional consumption of the lexicon's census sited inside
`tools/codebase-map/selftest.py`, promoted to AC4. Nothing in §3 excepts test-time. The spec
effectively resolves this two sections later — §4's "Optional consumption" paragraph is unambiguously
about the INDEX ("makes the index's contents depend on which kits a target installed") and names S5
approvingly one sentence after "the lexicon's census stays the lexicon's business" — so this is one
scoping clause, not a design change.

**FOLD.** Scope the §3 OUT to what the unit actually refuses — consumption by the GENERATED index /
`SYMBOL_EXTRACTORS` at render time — and state that a TEST-time cross-check is deliberately excepted,
with the reason the two differ (a skipped arm cannot silently shrink `symbols.json`).

## [MINOR] 12-3 — S4 and S6 have no acceptance criterion and no gate that could observe them

*(§2 S4, S6 vs §6/§7 — id 0.6)*

No AC in §6 mentions a comment, a backlog row or a decision record. §7's four gates —
`codebase-map/selftest.py`, `test_codebase_map.py`, `check-kit-versions.sh`, `lexicon/selftest.py` —
read none of `memory/backlog/TOOL.md`, `memory/DECISIONS.md`, or the prose of `map_extractors.py`. §1
says the stale sentence "is the sentence that kept this closed", so leaving its replacement unasserted
leaves the exact artefact that caused the miss unguarded. Prior art in this build sets the standard:
`2026-08-16-spec-dClosedLexicon-4.md` carries S1–S4 with every item landing on an AC and no bookkeeping
S-item at all.

**FOLD.** Add an AC for S6 naming the observation ("both rows read CLOSED in `memory/backlog/TOOL.md`
and the §1 table's four numbers appear in the minted decision row"); for S4, either fold the corrected
sentence into the extractor docstring the selftest already reads, or state plainly in §5 that S4 is
unasserted and why. While there, re-point S4's citation: the `SYMBOL_EXTRACTORS` dict opens at
`map_extractors.py:199` and the sentence you are replacing is at `:202-204`.

## [MINOR] 12-4 — the §10 probe result is asserted, not measured

*(§10 — id 1.5)*

RE-RUN: `python tools/codebase-map/reuse_lookup.py "javascript symbol extraction"` piped through
`grep -in enumerate` matches nothing (rc 1). The candidates are `render_symbols_json`, `all_symbols`,
`python_symbols`, `t_symbol_extractors_fail_closed`,
`t_symbols_render_deterministic_and_fail_closed`, then neighbours. `enumerate_exports` IS in the corpus
(`symbols.json` carries it against `tools/codebase-map/map_lib.py`), so the probe could have returned
it and simply did not rank it. §10's "surfaces only `enumerate_exports`" is false twice over.

**FOLD.** Replace the sentence with the query's real output, or with a query that does return
`enumerate_exports`, and keep the §1 inference tied to the measured 30-vs-3 gap — which reproduces
exactly — rather than to a probe result that does not.

---

# Spec 13 — `govkit's preview promises writes apply will not perform`

The diagnosis is right, the one-table design is right, and §1's role census reproduces exactly
(MEASURED across all descriptors: `rendered` 8, `project-owned` 4, `merged` 3, `generated` 1). The
defects are in the two mapping RATIONALES, which are measurably false for four named rules, and in an
acceptance set that cannot observe the half of S1 those rationales govern.

## [MAJOR] 13-1 — the `side-effect` rationale is false for the two rules with no adopter

*(§2 S1, §4 role table, §5 risks — consolidates ids 1.2, 2.10 and 3.5)*

S1 maps `rendered` and `generated` to `side-effect` because "something else in the install produces it
— the kit's adopter runs during `apply`'s CONFIGURE step". CONFIGURE is
`argv = d.get("adopt", {}).get("argv") or []` / `if not argv: continue` (`govkit.py:932-934`), so an
entry with an empty adopter runs nothing. Two entries carrying a re-labelled rule declare exactly that:

- `tools/workflows/kit.toml` (entry `review-harness`) — the `rendered` rule
  `REVIEW-PROTOCOL.template.md -> {memory_root}/guides/REVIEW-PROTOCOL.md`, with `argv = []` at `:21`
  and `why_no_adopter = "…the render is performed by the parity gate's own --render mode rather than
  by a separate adopter"`.
- `tools/govkit/entries/check-install-prefix.kit.toml` — the tree's ONLY `generated` rule
  (`install-prefix-waivers.txt`), with `argv = []` at `:27` and its own note "this is seeded empty
  rather than copied".

Nothing in `apply` produces either destination, yet `planned_writes` already stamps side-effect rows
with `src: "(produced by the adopter or the merge)"` (`govkit.py:570`). So 2 of the 9 re-labelled
rendered/generated rules would be previewed under a promise no step keeps — the same over-promise this
unit exists to delete, moved one mark over. §5's mitigation is unavailable: applied honestly, "asserted
against the behaviour `apply` actually exhibits for that role" reds on these two.

**FOLD.** Key the plan kind on whether a producer EXISTS, not on the role alone: emit `side-effect`
only when the entry declares a non-empty `adopt.argv` (and is not blocked by a hole) or a
`side_effects` entry covering the destination, and a distinct mark otherwise. Correct the S1 rationale
sentence, and add an AC naming `review-harness` and `check-install-prefix` as the two MEASURED cases.

## [MAJOR] 13-2 — two `project-owned` rules share a destination with a sibling `seed` rule, and AC4 cannot see it

*(§2 S1, §4, §6 AC4 — id 2.9)*

S1 maps `project-owned` to `order` ("the target is expected to supply it"). In 2 of the 4
`project-owned` rules a sibling `seed` rule in the SAME descriptor lands that exact destination during
the same `apply`: `tools/codebase-map/kit.toml:13-20` pairs `map_extractors.py` (`project-owned`, no
`to`, so `resolve_dests` defaults it to `{kit}/map_extractors.py`) with
`map_extractors.template.py` (`seed`, `to = "{kit}/map_extractors.py"`); `tools/drift-audit/kit.toml`
carries the identical pair for `drift_signals.py`. MEASURED,
`plan --target <scratch> --kits codebase-map` prints both rows at one path:

```
write  [project-owned] tools/codebase-map/map_extractors.py   <- codebase-map
write  [seed         ] tools/codebase-map/map_extractors.py   <- codebase-map
```

`codebase-map` is in the DEFAULT selection (`registry.toml:37`). Under S1 the first row becomes ORDER
while the second stays a write, so the preview prints two contradictory verbs for one path and the spec
says nothing about which a reader should believe. AC4 is set-equality between plan's write set and the
receipt's `files`; the seed row keeps that destination in the write set, so AC4 stays green whatever
the ORDER row says. §5's mitigation is ill-defined here too: apply's behaviour at that destination
depends on a SIBLING rule, not on the role.

**FOLD.** Make the classification a function of the DESTINATION as well as the role — a
`project-owned` destination some other selected rule writes is not an order — and state in §4 which
single row a plan prints for a shared destination. Add an AC over `codebase-map` (or `drift-audit`)
asserting the preview does not ORDER a path the same run writes; a set-equality AC cannot express it.

## [MAJOR] 13-3 — no acceptance criterion observes the side-effect/order half of S1, and §5 claims one does

*(§2 S1 vs §6; contradicts §5 risks — id 0.2)*

S1's whole content is a three-way mapping, and §6 contains no criterion that reads a `side-effect` or an
`order` row. AC1 is negative only ("neither `project-owned` row is counted as a write… 0 write(s)");
AC4 compares only plan's `write` set against apply's receipt; AC5 covers the unknown role. Over the
default selection (`registry.toml:37`) the non-landable rules are 4 `rendered` (memory-tree 3,
memory-recall 1) and 3 `project-owned` (playbook 2, codebase-map 1) — counted directly from the
descriptors. An implementation emitting all seven as `order`, or all seven as `side-effect`, satisfies
every AC in §6. §5 claims the opposite: "Each of the six mappings is asserted against the behaviour
`apply` actually exhibits for that role, not against the table itself, so a wrong entry reds." It
cannot be: `govkit.py:881` is a single
`if role not in LANDABLE_ROLES or rule.get("scope") == "machine" or rule.get("link"): continue`, so
apply's observable behaviour is IDENTICAL for `rendered`, `generated` and `project-owned`.

**FOLD.** Add an AC that pins the mapping positively and per-role over a named selection — e.g. *"When
`plan` runs over the default selection, the 4 `rendered` rows are marked SIDE and the 3 `project-owned`
rows are marked ORDER, counted by role"* — and requalify the §5 sentence to say what is actually
assertable (S3's per-rule skip line is the behaviour that distinguishes them, once S3 lands).

## [MAJOR] 13-4 — §5 sends the builder to a file that does not exist and misses the doc that carries the false promise

*(§5 user docs vs §4 Files touched — consolidates ids 1.3 and 3.6)*

`git ls-files tools/govkit/` returns only `entries/*.kit.toml`, `govkit.py`, `registry.toml`,
`selftest.py`; `ls` agrees — **there is no `tools/govkit/README.md`**, on disk or in the index. `USAGE`
(`govkit.py:1057-1068`) is five usage lines plus the read-only note and carries no plan legend; the
`write`/ORDER/SIDE/UNRES. marks live only in `cmd_plan`'s printer (`govkit.py:590-598`). Meanwhile §4
closes its list at "`tools/govkit/govkit.py`, `tools/govkit/selftest.py`. No descriptor edits, no
registry edit." The document that actually states plan's promise is unnamed anywhere in the spec:
`skills/deploy-governance/SKILL.md:42` — "Lists every file `apply` would write, with its role and the
source commit its bytes would come from" — which this build's own
`reviews/2026-08-16-review-TOOL-dClosedLexicon-4-8.md:96-98` already listed as one of the three carriers of
the false promise this row exists to close, alongside `planned_writes`' docstring at `govkit.py:534`.

**FOLD.** Replace the §5 line with the carriers that exist — `cmd_plan`'s mark legend
(`govkit.py:590-598`), `planned_writes`' docstring (`govkit.py:534`, whose "Machine-scoped rules
produce an ORDER" exception list goes stale once four roles map to non-write kinds), and
`skills/deploy-governance/SKILL.md:40-42` — and add the last to §4 Files touched.

## [MAJOR] 13-5 — the §10 probe surfaces neither member of the pair it claims to surface

*(§10 — id 1.6)*

RE-RUN: `python tools/codebase-map/reuse_lookup.py "one predicate, two callers"` prints thirteen
candidates — `id_pattern(conf)`, `registry.toml`, `agent-cap.topLevelArgs`,
`assertion-between-two-derived-values.md`, `check-install-prefix.sh`, `check-template-size.sh`,
`kit-dogfood-parity.PAIRS`, "lexicon naming predicates", `lexicon.subtokens`, `manifest-check.sh`,
`merge-rows.skeleton`, `pyrun.sh`, `two-answers-to-one-question.md` — and
`grep -inE "resolve_dests|resolve_rule_pool"` over the full output matches nothing (rc 1). Both
functions ARE in the corpus (`symbols.json` carries both ids against `tools/govkit/govkit.py`), so this
is a probe result the spec did not run. §10 says it "surfaces that pair and nothing else with this
shape"; both halves of that sentence are false. §10 is the section whose content is supposed to BE a
run probe, which is why this is filed major rather than as a wording slip.

**FOLD.** Record the probe's real output including the miss, and cite the pair as hand-verified at
`govkit.py:691` (`def resolve_dests`) and `:715` (`def resolve_rule_pool`) — whose docstrings state the
one-seam-for-plan-and-apply rule verbatim, so the reuse DECISION stands unchanged.

## [MINOR] 13-6 — AC4 names one of the two operands S4 requires

*(§2 S4 vs §6 AC4 — id 0.7)*

S4: "compares plan's `write` set against apply's receipt over EVERY role, on the `**` kit it already
uses **and** on the default selection." AC4: "…over the default selection". The existing arm at
`tools/govkit/selftest.py:393` runs `run("plan", "--target", str(t), "--kits", "drift-audit")` — the
`**` kit — and its comment at `:381-392` records that the wildcard pool is what the arm was written for
("plan 3, apply 12", echoed at `govkit.py:551-556`). The `**` half of S4's change is observed by no
criterion.

**FOLD.** State both operands in AC4: "…over the `**` kit (`--kits drift-audit`) and over the default
selection, with NO role filter, the two sets are equal in both."

## [MINOR] 13-7 — `planned_writes` is cited inside `cmd_apply`, the function §1 contrasts it with

*(§1 — consolidates ids 1.7, 2.11 and 3.7)*

§1 cites `planned_writes` at `govkit.py:864`. `def planned_writes` is at `:531` and its
`{"kind": "write"}` emit at `:564`; `:864` is a continuation line of `cmd_apply`'s `merged` refusal
f-string. `git diff --stat b4f0cf1c..HEAD -- tools/govkit/govkit.py` is empty, so this is not drift.
The sibling citation `govkit.py:881` IS correct — that is exactly the `role not in LANDABLE_ROLES`
write condition — and §10's joint `:690` is the blank line immediately above `def resolve_dests` at
`:691`, so neither of those is folded.

**FOLD.** Re-cite as `planned_writes` (`govkit.py:531`, emit at `:564`).

---

# Cross-cutting

## [MINOR] X-1 — none of the three §10s records the decision-record probe or its terms

*(all three specs, §10 — id 3.8)*

`grep -rln "query.py" memory/builds/dClosedLexicon/` returns nothing (rc 1) across the whole build
folder, and grepping the three specs for `memory-recall|query.py|--terms` returns nothing. M5
(`BUILD-METHOD.md:106-118`) makes the obligation TWO probes in order — map dossier first, decision
records second — and requires §10 to carry "the recall terms you used, because composing them is the
expensive half and M7 re-runs the query". M7 step 5 is "Re-run the recall probe with the terms recorded
in that spec's §10", so the omission costs the next reground, not just the record. Mitigating, and why
this is minor: `TEMPLATE-SPEC.md` §10 — the machine-checked half — asks only for the `reuse_lookup`
result, so the specs satisfy the template and miss the method. The channel is not idle here: spec 12's
§1 attribution and spec 11's archive-name choice both turn on records a `query.py` pass indexes.

**FOLD.** Run `python tools/memory-recall/query.py` ONCE for the set (M5: "Satisfy it once for the SET,
not per spec") with 8–14 corpus-jargon terms, and write the question and the terms into each §10.

---

## What was checked and found sound

Coverage, not courtesy — each of these was independently re-derived or re-run against source at
`b4f0cf1c`, and each is a claim a lens attacked and failed to break.

- **Spec 12's entire census reproduces exactly.** Running the lexicon's own extractor over
  `git ls-files` and diffing against `memory/map/generated/symbols.json` gives 642 distinct `(id,file)`
  for the lexicon, 426 map rows, 219 lexicon-only, 3 map-only, 53 JS (30 under `tools/`, 23 under
  `.claude/`), and the 120 / 46 / 53 split. Every figure in §1 is honest. The only defect is the
  sentence about which 3 the index carries (12-1).
- **Spec 12's conclusion holds.** `boundedK` is a statement-leading `function` at
  `tools/hooks/agent-cap.js:125` and is absent from `symbols.json` — `TOOL-aNumeralWarden-4` verbatim.
  The refusal of the coupling is well-argued and §4's three-shapes analysis is correct.
- **Spec 12's S2 floor is a measurement, not an assumption.** All six tracked `tools/**/*.js` yield at
  least one definition today: 19, 4, 1, 2, 2, 2.
- **Spec 13's role census reproduces exactly.** Grepping every tracked descriptor:
  `engine` 21, `seed` 5, `rendered` 8, `project-owned` 4, `merged` 3, `generated` 1 — matching §1's
  "(8) / (4) / (3) / (1)".
- **Spec 13's core diagnosis and its `cmd_apply` citation are right.** `govkit.py:881` is the
  `role not in LANDABLE_ROLES or scope == "machine" or link: continue` line, and `LANDABLE_ROLES` is
  the hand-written `("engine", "seed")` at `:688`. The two-predicates-for-one-question framing is the
  correct one and the `resolve_dests`/`resolve_rule_pool` precedent is the right shape to copy.
- **Spec 13's AC6 is NOT vacuous** (a lens claimed it was; REFUTED). Pinning the derived
  `LANDABLE_ROLES` against a literal is this repo's ratchet idiom — it moves the moment a table edit
  makes a fifth role a write, which is the failure AC6 names.
- **Spec 13's §3 OUT on `cmd_check` is correct discipline** — the `landed-but-inert` / `! grep` rc-2
  defect is a second mechanism and belongs in its own unit (M3), with the measurement attached.
- **Spec 11's diagnosis and its F1 resolution are right.** `refuse_if_terminal` really is the single
  branch every phase writer routes through, and `unattended.test.sh:912-913` derives the 5-writer
  population from source rather than listing it. Keeping the archive in the build folder is correct:
  `check-unattended.sh:137` selects `^$M/builds/[^/]+/RUN\.md$`, and `--resume` and every reader glob
  look there.
- **Spec 12's citations at `map_extractors.py:190` and `:199` are near-misses, not misdirections**
  (two lenses filed them; both REFUTED). `:190` is inside `_live_py`'s own docstring, `:199` is the
  opening line of the dict whose comment S4 replaces. Fix them opportunistically under 12-3; neither is
  a defect on its own.
- **Spec 12's S5 is drift protection, not a second opinion — and the spec says so** (a lens filed the
  gap; REFUTED against §3's "The duplication that leaves is one regex family in two kits" and §8's
  invitation to press exactly that trade). Its inert-operand vacuity is already armed one leg over, by
  `tools/lexicon/selftest.py`'s frozen per-pattern-set sentinel (`lexicon.py:94-96`).
- **Spec 12's `map_extractors.template.py` belongs in §4's list** (a lens argued it does not; REFUTED):
  the seed's commented example is `m.enumerate_exports(...)`, export-scan-only, so an adopter who
  instantiates it inherits the same blindness.
- **Nine of 41 raw findings were refuted by the skeptics and are not folded**, including two
  citation-precision complaints and one claim that spec 12's per-file liveness floor over-reaches an
  adopter (it does not: `js_definitions` runs only where a project's own `map_extractors.py` wires it
  in, and the shipped template's dict is empty).

## Reproduction environment

Worktree `.claude/worktrees/run-gates-performance-f1f419` at `b4f0cf1c`
(`git diff --stat b4f0cf1c..HEAD -- tools/govkit/govkit.py` empty). Check 4's awk lifted verbatim from
`check-memory-hygiene.sh:267-289` and run over `git ls-files memory/` plus the hypothetical archive
path. `check_clean`'s dirty-count measured in a scratch git repo across three rotation spellings
(`mv`+fresh, `git mv`+fresh, `git mv` alone → 2, 2, 1). The three `reuse_lookup.py` queries re-run as
written in each §10. The JS census re-derived through `tools/lexicon/lexicon.py`'s own
`PATTERN_SETS["js-regex"]`, not a reimplementation.
