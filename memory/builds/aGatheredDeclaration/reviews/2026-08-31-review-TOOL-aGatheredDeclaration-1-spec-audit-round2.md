**Serves:** spec-audit TOOL-aGatheredDeclaration-1 TOOL-aGatheredDeclaration-2 TOOL-aGatheredDeclaration-3 TOOL-aGatheredDeclaration-4 TOOL-aGatheredDeclaration-5 TOOL-aGatheredDeclaration-6 TOOL-aGatheredDeclaration-7 TOOL-aGatheredDeclaration-8

# Spec audit — aGatheredDeclaration, round 2

Reviewed 2026-08-31 on node `a`, in worktree
`.claude/worktrees/gate-bar-tooling-review-020565`, against the working tree at base `44734f15`.
Round 1 returned BLOCKED with 29 findings; this round audits the FOLD — the eight specs as they now
stand, with the fold text treated as unreviewed surface. Every source citation below was re-derived
against the tree at this base, not carried from a finder's claim and not carried from round 1.
The roster grew from seven units to eight: `TOOL-aGatheredDeclaration-8` was created during the fold
because round 1's F9 showed unit 2 was pricing a dispatcher rewrite as a format change.

**Range · ROUND 2.**
`memory/builds/aGatheredDeclaration/spec/2026-08-31-spec-TOOL-aGatheredDeclaration-1.md@bb796581082ed55fc26f0542da0e9be6d383a8b1` ·
`memory/builds/aGatheredDeclaration/spec/2026-08-31-spec-TOOL-aGatheredDeclaration-2.md@a276b68064dbc717a9d91a51a79bb54e0d98b75a` ·
`memory/builds/aGatheredDeclaration/spec/2026-08-31-spec-TOOL-aGatheredDeclaration-3.md@b540192e36cc2f9b240b8fcca48e83daabd07ee6` ·
`memory/builds/aGatheredDeclaration/spec/2026-08-31-spec-TOOL-aGatheredDeclaration-4.md@50478a845c59c85bf725d696e91836a5a2061eb7` ·
`memory/builds/aGatheredDeclaration/spec/2026-08-31-spec-TOOL-aGatheredDeclaration-5.md@3366b382c43b6712208000ee264e7f7a8b7ae11a` ·
`memory/builds/aGatheredDeclaration/spec/2026-08-31-spec-TOOL-aGatheredDeclaration-6.md@aa82e1fe6436bc8fdadca2803a5a92ec13ad7e6d` ·
`memory/builds/aGatheredDeclaration/spec/2026-08-31-spec-TOOL-aGatheredDeclaration-7.md@8bc36fae9d2fd9eaf95f886c05534f441acc883e` ·
`memory/builds/aGatheredDeclaration/spec/2026-08-31-spec-TOOL-aGatheredDeclaration-8.md@19de818e1296b06f5622ca3dfc3caae6f260b639`

## Verdict: BLOCKED

Four blockers and six highs. Three of the four blockers are FOLD-INTRODUCED: rev-1 was silent where
rev-2 now names a mechanism, and the named mechanism is one that provably cannot do the job. That is
worse than the silence it replaced, because a wrong path reads as a resolved one and carries an
acceptance criterion built on top of it. The fourth blocker was reachable at rev-1 and the fold
walked past it while closing its sibling. None of the four is a design disagreement; each is a spec
that still does not say what the implementer has to do.

## Review shape

Raw 48 · confirmed 26 · refuted 22 · unverified 0 · precision 0.54.

The 26 confirmed findings de-duplicate to **18 rows** below. Six merges, with their source ids named
on each row: three findings reached the `[gate_runner_seed]` defect from unit 4 and unit 5 and are
one row; two reached the push-boundary blindness from either predicate; two the `profile_bar.py`
omission; three the `.governance/deploy.toml` ownership hole; two the unit-7 emission gap; two the
guard count. Precision at 0.54 is above round 1's 0.42, which is what a second pass over folded
text should look like — the surface is smaller and the priming was carried forward.

**Severity criterion, stated so the ranking is readable.** BLOCKER — a merge-bar leg reds at the
unit's own landing, two criteria in the reviewed set cannot both pass, or a scope item names a
mechanism that provably cannot perform it, so the implementer is blocked or must invent the design
the spec claims to have made. HIGH — nothing in the build catches it: a could-not-fail acceptance
criterion, a guard disarmed by absence, or a sibling contradiction the ACs are blind to. MEDIUM — a
real gap that an existing acceptance criterion or gate WILL catch during the build, at the cost of a
rework loop rather than a wrong landing. LOW — a false claim in a spec whose argument survives it.

## What the fold closed, and what it did not

Round-1 findings are not re-reported below except where the fold left a gap. Five did, and the gap
is named on the row that carries it:

| Prior | What the fold did | Gap |
|---|---|---|
| F17 (u4 §2 S7 — the seed item has no file and no AC) | named `[gate_runner_seed]` and added AC9 | the named path cannot carry a `[bar]` key and AC9 grades a read-only verb — **R1** |
| F16 (u4 — no criterion exercises the declared value) | added AC1b for the declared `true` | rewrote AC1 to exclude the absent-key row, so row 3 lost its only arm — **R11** |
| F10 (u2 — the stamp/pre-push blob pair splits) | S8 freezes the stamp on the JSON blob | predicate 6's pathspec never moved; both predicates are now blind, in the unsafe direction — **R2** |
| F12 (u2 — `PROF_TIMEOUT` has two live consumers) | added `[bar].turnstile_ttl` as the replacement | no criterion in any of the eight units grades it — **R10** |
| F29 (u7 — nothing emits the `[[lane]]` rows) | added S10 for `[[lane]]` | stopped one row short of `[bar]` and `[[profile]]`, same argument — **R4** |

Everything else round 1 raised is either closed or absent from this round's confirmed set.

## Findings

| # | Sev | Unit | Address | Defect |
|---|---|---|---|---|
| R1 | BLOCKER | 4, 5 | u4 §2 S7 / §4 / §6 AC9; u5 §2 S3 / §6 AC5 | the fold routes `[bar]` through `[gate_runner_seed]`, which writes a different file from a closed key tuple |
| R2 | BLOCKER | 2 | §2 S8, §4, §6 AC10 | both pre-push manifest predicates stay pinned to the JSON while the TOML scopes the bar |
| R3 | BLOCKER | 6 | §2 S7, §5, §6 AC6 | AC6 is unsatisfiable beside u2 S3; `dead-path carriers` reds at this unit's landing and the waiver file is unowned |
| R4 | BLOCKER | 7 | §2 S1/S3/S10, §6 AC8 | `--upgrade` emits no `[bar]` table and no `[[profile]]` rows, so it silently orphans the target's profile table |
| R5 | HIGH | 6 | §4 Inventory, Files touched | the re-certified reader inventory still omits `tools/run-gates/profile_bar.py` |
| R6 | HIGH | 6 | §2 S1, S1b, §4 | `subject` → `opt_in` is priced at three edits; it moves 68 descriptor rows and five govkit arms |
| R7 | HIGH | 6 | §2 S6, §4, §7 | S6 edits the rendered charter, not `.governance/deploy.toml` which owns the string; §7 names no playbook leg |
| R8 | HIGH | 4 | §2 S5, §6 AC6 | the hook is given no way to learn the enforcement state a push needs; AC6 has no defined input |
| R9 | HIGH | 2 | §6 AC10 | AC10 never requires the scratch repo to declare a TOML, so it greens with or without the fix |
| R10 | HIGH | 2 | §4 Migration, §6 | `[bar].turnstile_ttl` is graded by no criterion in any of the eight units |
| R11 | MEDIUM | 4 | §4 resolution table, §6 AC1/AC1b/AC2 | the fold armed row 2 and disarmed row 3 — the absent-key state |
| R12 | MEDIUM | 6 | §2 S1(c), §6 AC1 | S1(c) names the seed's filename and not its `grammar` key |
| R13 | MEDIUM | 3 | §2 S4, §6 | `--help` and the unknown-argument refusal have no criterion |
| R14 | MEDIUM | 3 | §2 S9, §5, §6 AC11 | the fold-new ledger read has no unmeasured-leg rendering, no empty state, and a one-armed AC |
| R15 | MEDIUM | 3 | §4 Inventory vs §2 S9 / §6 AC11 | the pinned `LEG` row format contradicts the fold-new columns |
| R16 | MEDIUM | 8 | u8 §4 / §2 S3; u2 §4 | `short_circuit` is declared by neither unit — the 2/8 split dropped it |
| R17 | LOW | 6, 7 | §10 in both | a `govkit.py:2510-2512` citation imported from a prior review is stale |
| R18 | LOW | 2 | §4 wire-format paragraph | "36 of 86 legs carry no guard" is 38 of 86 by the paragraph's own criterion |

---

## BLOCKERS

### R1 — the fold's answer to F17 names the one path that provably cannot carry the key

**Address:** unit 4, §2 S7, §4 ("S7 writes the seed through `[gate_runner_seed]`, the same path
`TOOL-aGatheredDeclaration-5` S3 uses") and §6 AC9. Unit 5, §2 S3, §4 files-touched, and §6 AC5.
*(source ids 1, 9, 28)*

Round 1's F17 asked unit 4 to name a file and a criterion for "the kit's adopter seed declares
`enforce_ceilings = false`". The fold named `[gate_runner_seed]` and cited unit 5's identical S3 as
precedent. Both are wrong, verified at source in three independent ways:

- `tools/run-gates/kit.toml:105-135` is `[gate_runner_seed]`, and it seeds the TARGET's
  `.governance/deploy.toml` `[gate_runner]` table — `kind`, `grammar`, `file`, `command`,
  `dedupe_key`, `run_all_env`, `observed_*`. It has no key for a `[bar]` table and no route into the
  target's `gate-legs.toml`, which is a different file read by a different program.
- `tools/govkit/govkit.py:6620` emits that block from a CLOSED tuple —
  `("kind","grammar","file","dedupe_key","run_all_env") + OBSERVED_KEYS + ("command",)` — with
  `if k not in seed: continue`. An added key is dropped in silence, so even the wrong destination is
  unreachable.
- `tools/run-gates/adopt-run-gates.sh:22-24` documents `--check` as "read-only … Writes nothing,
  ever", and `:162-165` has adopt mode print "nothing to write — the `[gate_runner]` declaration is
  emitted by `govkit intake`" and exit 0. AC9 grades "a freshly seeded target" with that verb. There
  is no producer for the state it grades, and the verb never opens a manifest.

No unit owns a write path that puts a `[bar]` table into an adopter's `gate-legs.toml`. Unit 4 §4
and unit 5 §4 list neither `govkit.py` nor any emitter; unit 6 S1's govkit scope is the grammar enum,
the splice writer, the subject pins and the filename, and never mentions `[bar]`.

One correction to the finder's impact claim, because the record should be accurate: adopters do NOT
inherit enforcement ON. Units 4 and 5 both carry a resolution table whose third row resolves an
absent key to `false`, so the shipped default survives the missing seed. What does not survive is the
implementability of S7/S3 and the ability of AC9/AC5 to fail.

**Fix.** Re-point both scope items at the emitter that actually writes a target's manifest: state
that unit 6 S1's textual-splice writer emits the `[bar]` table with `enforce_ceilings = false` and
`turnstile = false`, and add `[bar]` emission to unit 6 S1's scope and files-touched. Restate AC9
and AC5 to parse the emitted `<prefix>/gate-legs.toml` in a freshly intaken scratch target and assert
the two keys, run against whichever verb writes it. Fix both units in one edit — the fold's failure
mode here was that unit 4 copied unit 5 without testing it.

**Left-shift gate.** Extend `tools/run-gates/adopt-run-gates.test.sh` (or the govkit intake selftest)
with an arm that runs a full intake into a scratch target and asserts the emitted manifest's `[bar]`
table key-by-key against the kit's declared defaults. It is the general form: any kit default that an
adopter must receive gets an intake arm that reads the emitted file, never the seed.

### R2 — the fold closed pre-push predicate 7 and left predicate 6, in the unsafe direction

**Address:** unit 2, §2 S8, §4 "The stamp and the hook must not split", §6 AC10.
*(source ids 16, 29)*

Round 1's F10 said the stamp and the hook's blob would split. The fold's answer is to keep the stamp
writing the JSON blob so predicates 6 and 7 keep agreeing. They do agree — and both now watch a file
that no longer scopes the bar.

Verified at source. `.githooks/pre-push:195` is predicate 6,
`git diff --quiet "$rec_sha" "$main_local" -- tools/gate-legs.json`, whose own header states its job:
"A guard added, widened or removed in this very push cannot be trusted to scope this very push."
`:203` is predicate 7, `git hash-object -- tools/gate-legs.json`. Both spell the path literally.
`tools/run-gates/run-gates.sh:1430` (and its sibling at `:1021`) stamp `manifest_blob` from
`$LEGS_FILE`, which S2 makes resolve to the TOML.

With the JSON tracked and frozen from unit 2's landing until unit 6 deletes it, `git diff --quiet`
on it always exits 0. Across that window — which contains unit 2's own push and units 3, 4 and 5,
two of which edit `[bar]` in exactly that file — a push may rewrite guards, ceilings, `opt_in`
values or the entire leg set in `gate-legs.toml` and be scoped against a stale recorded green.
Predicate 4 does not cover it; it fingerprints at the recorded sha, not the pushed tip. Unit 2 §4's
closing claim, "it needs no cross-unit ordering guarantee", is exactly what this refutes: the push
boundary is weaker than before for the whole window. AC10 asserts only that the push is NOT forced to
a full bar, which is the direction the defect satisfies.

**Fix.** Extend S8 to BOTH predicates. Adding `tools/gate-legs.toml` to predicate 6's pathspec is a
one-line additive change that waits on nothing — `git diff --quiet -- a b` covers both — and it
restores the guard for the window. Add a criterion: a push whose diff touches ONLY `gate-legs.toml`
IS forced to a full bar, observed RED first against the unmoved pathspec. If the frozen-JSON stamp
is kept for predicate 7, say in §4 that predicate 7 is known-blind until unit 6 and name the
compensating check, which §7 of the charter requires of any deliberate exemption.

**Left-shift gate.** Parameterise `.githooks/pre-push.test.sh`'s manifest-touch fixture over the
manifest filename, so every predicate that names a manifest path is exercised once per format. A
hook predicate that hardcodes a path should have a test that hardcodes the OTHER path.

### R3 — unit 6's AC6 cannot pass beside unit 2 S3, and its landing reds a leg that runs on every bar

**Address:** unit 6, §2 S7, §5 risks, §6 AC6.
*(source id 40)*

AC6 reads "no carrier names `tools/gate-legs.json`, asserted by the leg's own green". Unit 2 S3 makes
the JSON branch PERMANENT in `run-gates.sh` for the legacy pair, so `run-gates.sh` must keep spelling
the name. The two criteria cannot both hold.

`tools/check-dead-paths.sh:76-84` derives its needles as BASENAMES from
`git log --diff-filter=D --name-only`, minus every basename the tree still carries, and greps every
tracked file except `memory/`, the waiver file and its own two. Deleting `tools/gate-legs.json`
therefore turns the literal `gate-legs.json` into a needle. Re-derived at this base:
**31 tracked files outside `memory/` carry that string today**, 30 of them surviving the deletion —
`run-gates.sh` itself, `.githooks/pre-push` and its test, `tools/run-gates/kit.toml`,
`tools/govkit/govkit.py`, `tools/govkit/registry.toml`, `tools/govkit/subject-pins.tsv`,
`tools/govkit/entries/check-testsuite-counts.kit.toml`, `tools/govkit/selftest.py`,
`tools/codebase-map/map_extractors.py`, `tools/drift-audit/drift_signals.py` and its template,
`tools/memory-tree/check-memory-hygiene.sh`, `tools/template-size-limits.txt`,
`tools/workflows/drift-audit-state.js`, `tools/unattended/run-unattended-gates.sh`,
`.governance/deploy.toml`, `.codebase-map.conf`, `.gitattributes`, `AGENTS.md` and six suites whose
legacy-pair arms legitimately must spell it. The `dead-path carriers` leg is `subject = repo` with no
guard, so it runs on every bar, including this unit's own landing.

§5 reads the resulting red as the backstop working. It is not — it is the unit's landing failing.
And `tools/dead-path-waivers.txt`, the only route through, is SHRINK-ONLY by its own header and
appears in no scope item, no acceptance criterion and no files-touched list. The implementer meets a
wall of undeclared waiver rows at landing with no budget for them.

**Fix.** Add a scope item owning `tools/dead-path-waivers.txt`: one row per surviving carrier, with
the permanent ones (the loader's legacy branch, the kit seed, the adopter fixtures) reasoned as "a
live path in an adopter, dead only in gov". Reword AC6 to the gate's actual predicate — the basename
— and assert it as "green with the declared waiver set", plus a control that an UNDECLARED new
carrier still reds. State in §4 that the waiver file's shrink-only header is being ratcheted the
wrong way in this one commit and why.

**Left-shift gate.** The control arm IS the gate: add an arm to `check-dead-paths.sh`'s own test
that plants a fresh undeclared carrier and asserts RED. That is what stops a waiver-set edit from
silently widening the surface it was written to narrow.

### R4 — `--upgrade` writes a manifest that drops two of the three top-level tables the loader owns

**Address:** unit 7, §2 S1/S3/S10 and §6 AC8.
*(source ids 25, 39)*

S10 was added in the fold with the right argument — "emitting the legs alone would write a file the
runner rejects" — and stops one row short. The emitted `gate-legs.toml` carries legs, `[[lane]]` rows
and prose comments, and nothing else: no `[bar]` table, no `[[profile]]` rows.

Unit 2 S3 defines the legacy pair as `gate-legs.json` TOGETHER WITH `gate-profiles.txt` and makes the
TOML win wholesale wherever it exists. Verified: `tools/run-gates/run-gates.sh:178` is
`PROFILES="${GATE_PROFILES:-$KITREL/gate-profiles.txt}"`, and `tools/run-gates/kit.toml:146` pins
`{kit}/gate-profiles.txt` into every target, so adopters really do hold the profile half. NicoCares
adopts the kit at prefix `scripts/` with its own profile table present, and its 40-row manifest
declares no `ceiling` at all.

So running the shipped tool against a real adopter converts a working merge bar into one with no
declared pool width, no `default_ceiling`, and no `turnstile` / `enforce_ceilings` declaration — the
moment the TOML exists, the target's profile table stops being read. On an 8-core/8GB box the
declared width 4 becomes the built-in `min(cores, 8)`, i.e. sixteen scratch repos where the table
declared eight. AC8 compares leg counts only, and unit 2's refusal list (unparseable, unknown key,
undeclared lane, empty leg list, escaping cwd) has no empty-profile-table case, so nothing observes
it. No non-goal in unit 7 §3 withholds this.

**Fix.** Extend S10 to the class rather than the instance: the emitted file carries a `[bar]` table
seeded from the same defaults R1 resolves, and `[[profile]]` rows read from the target's
`gate-profiles.txt`, or REFUSES when that file is absent. Extend AC8 past the leg count to the
resolved profile row and width, compared against the target's pre-upgrade table.

**Left-shift gate.** Add a refusal to the unit-2 loader: a TOML declaring no `[[profile]]` row exits
2 naming the file. A converter that drops a table is then caught by the loader on the first run
rather than by a wide pool on a small machine, and the same refusal covers a hand-written adopter
manifest.

---

## HIGH

### R5 — the re-certified reader inventory still omits `profile_bar.py`

**Address:** unit 6, §4 Inventory table and §4 files-touched; §7 gate list.
*(source ids 22, 33)*

`tools/run-gates/profile_bar.py:319` resolves the manifest exactly as the runner does —
`os.environ.get("GATE_LEGS") or os.path.join(os.path.dirname(KITDIR), "gate-legs.json")` — and
`:253` does `json.load(fh)` over it inside `measure_orphans`, called from the record build at `:467`.
It is a tracked manifest reader inside the run-gates kit and it backs the `profile-bar selftest` leg,
whose guard is `tools/run-gates/` — precisely the commits this build makes.

It appears in no row of §4's ten-reader inventory, no scope item, no files-touched list, and unit 6's
§7 omits `profile-bar selftest` while unit 2's includes it. §4's own text claims the rev-1 inventory
was refuted by a re-run grep; any grep for `gate-legs` returns this file. It is worse than a missing
row: `measure_orphans` swallows `OSError` and returns `None`, so after S7 the orphan probe goes
permanently DARK rather than failing, and `profile_bar.test.sh` drives the profiler over its own
scratch-repo JSON fixtures, so the selftest leg stays green over the dead path. Unit 6 §3 calls
exactly that a defect: "a reader whose behaviour changes here is a defect". Unit 2 §10 compounds it
by calling the `LEGS_FILE` derivation "the seam this unit extends" — there are two copies of that
derivation in one kit (`run-gates.sh:84` and `profile_bar.py:319`) and §10 checked one.

**Fix.** Add a `profile_bar.py` row to §4's inventory and to files-touched, add `profile-bar
selftest` to §7, and add a criterion that the profiler's orphan count and manifest leg count are
unchanged across the format move, run at the commit where both files exist. Correct unit 2 §10 to
name both copies of the derivation.

**Left-shift gate.** Make `measure_orphans` DECLARE its liveness instead of swallowing `OSError`: a
manifest it cannot read prints `DEAD PROBE` and reds, per the charter's rule that a probe which
cannot move says so. That converts this whole class from a silent dark probe into a leg failure.

### R6 — `subject` → `opt_in` is priced at three edits and moves five govkit arms and 68 descriptor rows

**Address:** unit 6, §2 S1 and S1b, §4 files-touched.
*(source id 21)*

S1 prices govkit at "THREE changes rather than a filename" and S1b adds the version pin file. The key
is read by considerably more of govkit than that: `govkit.py:1235` hardcodes `tools/gate-legs.json`,
`:1239` builds `manifest_subject` from it, `:1264` REDS a descriptor leg declaring no `subject`,
`:1271` validates the closed set, `:1285` reds when the manifest declares none while a descriptor
does, `:1290` reds on disagreement, `:1322-1330` reads `manifest_subject` for every `[[exempt_leg]]`
row, `:4332-4334` writes `row["subject"]` on emit behind `check_target_reads_subject`, and
`SUBJECT_FLOOR_RUN_GATES` at `:2971-2972` pins the run-gates version at which the key entered the set.
68 `^subject = ` rows sit across 23 descriptor TOMLs, 21 of them under `tools/govkit/entries/` and
the rest in other kits' `kit.toml`.

S1b's own premise — "once `subject` is gone" — is the trigger for every one of them. Unit 6's
files-touched names neither the entries nor the other kits' descriptors, and unit 2 §3 explicitly
pushes govkit's emitter to unit 6, so no sibling owns it. The consequence lands on
`govkit selfcheck`, which is `chunk = declarations`, `subject = repo`, no guard.

**Fix.** Extend S1 with a fourth change naming the descriptor-key migration and the selfcheck arms at
`govkit.py:1239-1330`, `:4334` and `:2972`; add `tools/govkit/entries/*.kit.toml` and each kit's
`kit.toml` `[[gate_leg]]` rows to §4's files-touched; add a criterion that `govkit selfcheck` is
green with no `subject` key anywhere in the tree.

**Left-shift gate.** A cross-kit descriptor key rename deserves the same treatment any shared
contract gets: one arm that greps the tracked descriptor population for the retired key and reds on
any survivor, so a kit added later cannot reintroduce it.

### R7 — S6 edits the rendered charter and not the file that owns the sentence

**Address:** unit 6, §2 S6, §4 files-touched, §7 gate list.
*(source ids 24, 34, 46)*

Verified end to end. `.governance/deploy.toml:44` holds
`gate_commands = "bash tools/run-gates/run-gates.sh — the legs are single-sourced from
tools/gate-legs.json; …"`. `coding-governance-agents.template.md:180` carries `{{GATE_COMMANDS}}`.
`AGENTS.md:250` is that value rendered, and it sits INSIDE the `<!-- gov:playbook -->` region, whose
markers are at `AGENTS.md:76` and `:470`. So S6's "AGENTS.md, the template, and whatever
`tools/playbook/` renders from them" has the direction backwards: the renderer reads deploy.toml plus
the template and WRITES the charter.

`.governance/deploy.toml` appears in no scope item and no files-touched list, and neither does
`.codebase-map.conf:13`, a second carrier of the same string. A hand edit to AGENTS.md:250 is
reverted by the next render, and `playbook render wiring`
(`bash tools/playbook/adopt-playbook.sh --target . --check`) reds on the divergence — it is
`subject = repo` with no guard, as are `playbook parity` and `playbook placeholder catalogue`. §7's
gate list gained `template size` and `charter size` in the fold and still names none of the three.
AC6's dead-paths backstop catches the deploy.toml string only AFTER the deletion, which is the late
red S9 exists to avoid.

**Fix.** Name `.governance/deploy.toml`'s `gate_commands` as the source in S6 and add it and
`.codebase-map.conf` to files-touched; say which AGENTS.md text is rendered (inside the region) and
which is gov-authored (the merge-bar section below `:470`). Add `playbook render wiring` and
`playbook placeholder catalogue` to §7 and a criterion that `adopt-playbook.sh --target . --check`
is green after the edit.

**Left-shift gate.** This is the "point at the source or gate the pair" rule failing on the document
that states it. The durable fix is for the placeholder catalogue leg to refuse a `{{…}}` value that
names a tracked path which no longer exists — a deploy value naming a deleted file should red at the
render, not at the dead-path scan two units later.

### R8 — S5 needs the hook to know a state no unit teaches it

**Address:** unit 4, §2 S5 and §6 AC6.
*(source id 30)*

S5 requires `.githooks/pre-push` to treat an enforcement-OFF stamp as covering a push that needs it
off, "never the reverse" — which requires the hook to know what the push NEEDS. The hook resolves
everything with git and `awk -F'\t'` and contains no TOML reader at all. Predicate 8 works only
because `:213` reads `[ -n "${GATE_SELFTESTS:-}" ]` — the pusher's own exported environment carries
the answer. For ceilings there is no such variable unless `GATE_CEILINGS` is exported, and unit 4 S2
makes its ABSENCE take the declared value, which lives in `gate-legs.toml` — unreadable by the hook
until unit 6 S2, order 6, two units later.

So AC6's "when the push needs it ON" has no defined input. Read env-only, a repo declaring
`enforce_ceilings = true` never forces a full bar over an OFF-earned stamp, which is precisely the
stamp confusion S5 claims to close. Read from the declaration, unit 6 is an undeclared prerequisite
of unit 4. §4's resolution table covers the runner, not the hook, and the spec's own AC1b shows it
knew the env-versus-declaration trap on the runner side and never applied it here.

**Fix.** State in S5 how the hook resolves the needed state — env-only, or by shelling out to
`run-gates.sh --manifest` and parsing the reported source — and if it is the declaration, record
unit 6 S2 as a prerequisite in §3 or move S5 into unit 6. Rewrite AC6 to name the input it varies.

**Left-shift gate.** Add a `.githooks/pre-push.test.sh` arm per resolution source: one fixture with
`GATE_CEILINGS` exported, one with it unset and the declaration ON. Whichever design is chosen, one
of the two arms must red before the fix and green after.

### R9 — AC10 greens whether or not the fix it grades exists

**Address:** unit 2, §6 AC10.
*(source id 42)*

AC10 asks that "a bar runs and a default-branch push follows in one scratch repo" not force a full
bar, and never requires the scratch repo to declare a `gate-legs.toml`.
`.githooks/pre-push.test.sh` contains no reference to any `.toml` at all — grep returns `:132`
(the stamp helper hashing `tools/gate-legs.json`) and `:184` (the manifest-touch fixture writing
JSON). On a JSON-only fixture `LEGS_FILE` resolves to the JSON, the stamp hashes the JSON, and
predicate 7 hashes the JSON, with or without S8's hardcode. The one criterion covering the window
this unit opens is satisfied by the absence of the condition it grades. It is also the only criterion
in §6 covering S8 that does NOT carry "Observed RED first", unlike AC3, AC7, AC9 and AC12.

**Fix.** Name the state: the scratch repo declares BOTH `gate-legs.toml` and `gate-legs.json` with
differing bytes, the run reads the TOML, and predicate 7 does not fire. Add the control — the same
fixture with the stamp writing the TOML blob DOES force a full bar — so the arm distinguishes the fix
from its absence. Observed RED first.

**Left-shift gate.** Make the dual-format fixture a shared helper in `.githooks/pre-push.test.sh` and
route every predicate arm through it, so no future arm can accidentally test the single-format world.

### R10 — `[bar].turnstile_ttl` is graded by nothing in the entire build

**Address:** unit 2, §4 Migration ("`timeout=` is dropped"), §6; unit 4 §3; unit 5 throughout.
*(source id 17)*

The key was added by the fold as the named replacement for a live consumer. Grepped across all eight
specs: `turnstile_ttl` appears in unit 2's data model, its consumer table, its cross-reference to
unit 4, and its revision log, plus unit 4's non-goal deferring it. No acceptance criterion anywhere
touches it. Unit 2's AC7 covers `[bar]` booleans only and this is an integer; AC1 compares leg count
and manifest order, not `[bar]` scalars. Unit 5 never names it while its own fail-open argument rests
on the bounded wait derived from it: `run-gates.sh:434` is
`TS_TTL=$(( PROF_TIMEOUT * 3 ))`, `:435` falls back to `${GATE_TURNSTILE_TTL:-1800}`, and `:440` is
`TS_MAXWAIT=$(( TS_TTL * 4 ))`.

A loader that drops the key, or that lets the pre-existing `GATE_TURNSTILE_TTL` env var silently
outrank the declared value, passes all eight specs. The value is behaviour-identical on gov today,
which caps the blast radius but does not close the grading gap in a build whose entire thesis is that
declarations must be graded.

**Fix.** Add a criterion asserting the resolved TTL equals `[bar].turnstile_ttl` with
`GATE_TURNSTILE_TTL` unset, and state in S4 or §4 which of the two outranks the other.

**Left-shift gate.** The class is bigger than this key: add one arm that enumerates the declared
`[bar]` key set and asserts each key has an observable in `--manifest` output. A declared key with no
reporter is then a red, not an audit finding.

---

## MEDIUM

### R11 — the fold armed row 2 of the resolution table and disarmed row 3

**Address:** unit 4, §4 resolution table (third row) against §6 AC1, AC1b, AC2.
*(source id 10)*

Round 1's F16 prescribed "every resolution table gets one arm per row" and called it the single
highest-value edit across the set. At rev-1, AC1 graded the "neither" row. rev-2 reworded AC1 to
"the SHIPPED state, not an absent key" and added AC1b for the declared `true`, so all three criteria
now sit on rows 1 and 2 and row 3 lost the only arm it had. The absent-key state is not
hypothetical — it is what unit 7's upgrader emits (R4) and what any hand-written adopter manifest
starts as. Its row carries its own observable, "the runner says the default was taken", which nothing
grades. An implementation that crashes on an absent `[bar]`, or that resolves it to enforcement ON,
passes every criterion in the unit.

**Fix.** Add AC1c: with no `[bar]` table at all and `GATE_CEILINGS` unset, the leg completes AND
`--manifest` reports enforcement off with source `default`. Observed RED first.

**Left-shift gate.** Make the arm-per-row rule mechanical for this build: one test file per
resolution table, named for it, with one test function per row, so a row added later without an arm
is visible in the diff.

### R12 — S1(c) names the seed's filename and leaves its grammar key behind

**Address:** unit 6, §2 S1(c) and §6 AC1.
*(source id 11)*

S1 was rewritten in the fold to be explicitly "THREE changes rather than a filename", and S1(c) is
still a filename. `tools/run-gates/kit.toml:107` declares `grammar = "json-array"` on the line
immediately above `file = "{prefix}/gate-legs.json"` at `:108`, inside the same `[gate_runner_seed]`
block. S1(a)'s new `toml-legs` enum member is exactly what that value must become, and the seed is
the only place a target's grammar comes from — so `toml-legs` has no declared producer anywhere in
the build. A freshly intaken target would declare a JSON-array grammar against a `.toml` file.
(`govkit.py:2947` accepts `None` or `'json-array'`, so the refusal does not fire at the adopter; the
grammar simply lies, and a JSON array is emitted into a file the runner parses as TOML.) AC1 grades
the emitted manifest file, not the seed block, so nothing in this unit can fail on it.

**Fix.** Name the `grammar` key alongside the file name in S1(c), and add a criterion asserting the
emitted `[gate_runner]` block carries `grammar = "toml-legs"` and a `.toml` `file`.

**Left-shift gate.** Add a govkit selfcheck arm that asserts every seed's declared `grammar` matches
the extension of its declared `file`. It is one predicate and it covers every kit that ever ships a
manifest seed.

### R13 — the one pure-surface scope item has no criterion at all

**Address:** unit 3, §2 S4, absent from §6.
*(source id 12)*

S4 declares `--help` / `-h` (usage line, exit 0) and an unknown argument as exit 2 naming it, and §5
repeats the unknown-flag refusal. The acceptance set covers `--leg` (AC1-AC4), `--list` (AC5),
`--manifest` (AC6, AC11), the two-token need-a-value guard (AC7), the shard stamp (AC8), the opt-in
ledger (AC9) and the turnstile query verbs (AC10). Nothing grades `--help` or the unknown-argument
exit. AC4 is a `--leg` value matching no leg; AC7 is a flag given with no value. Both are different
cases. §5 mentions the refusal, but a readiness checklist is not a criterion. The item can ship
entirely absent with every criterion green — the plain form of the lens, and the fold added S8, S9,
AC10 and AC11 without noticing it.

**Fix.** One criterion: `--help` prints the usage line and exits 0, and an unrecognised flag exits 2
with the offending token in the message. Observed RED first.

**Left-shift gate.** A section-2/section-6 coverage check for this build's own specs: every `S<n>`
must be named by at least one `AC<n>` body. Cheap, greppable, and it would have caught this row
without a reviewer.

### R14 — S9 reads a per-clone ledger and never says what an unmeasured leg renders

**Address:** unit 3, §2 S9, §5 error/empty states, §6 AC11.
*(source id 13)*

S9 is fold-new and adds a read of `<git-dir>/gate-ledger.tsv`, which is untracked, per-clone, and
holds a row only for a leg some previous run measured. On a fresh clone it does not exist. §5's
error/empty/loading list still names exactly three argument errors and says nothing about an absent
ledger or an unmeasured leg, and AC11 grades "against a planted ledger" only. So the ceiling,
measurement and ratio columns are undefined for the common case, and the "flag any leg whose ceiling
is under 3x its measurement" rule then flags nothing and reports clean — the green-by-absence shape
S9 was added to prevent in the declarations it watches.

**Fix.** State the unmeasured-leg rendering in S9 (an explicit `unmeasured` token, never a zero or a
blank), add it to §5's empty states, and give AC11 a second arm with the ledger absent, asserting
every row reads `unmeasured` and nothing is flagged.

**Left-shift gate.** Make the flag count a liveness assertion: `--manifest` prints the number of legs
it could measure alongside the number it flagged, so "0 flagged" out of 0 measured is visibly
different from "0 flagged" out of 86.

### R15 — the pinned output contract contradicts the fold's new columns

**Address:** unit 3, §4 Inventory against §2 S9 and §6 AC11.
*(source id 19)*

§4 pins the row byte-for-byte at `:86`:
`LEG  <name>  <lane>  <opt-in|always>  <ceiling|none>  <guards>  <would-run|held|guarded-out>` — no
measurement, no ratio. The fold-new AC11 requires each leg row to carry the declared ceiling, the
seconds from `gate-ledger.tsv` and their ratio, with a flag under 3x. The revision log confirms S9
and AC11 arrived at rev-2 while the pinned format did not move. Both statements ship in the same unit
and the same commit, so an implementer must pick one and violate the other; AC6 byte-compares header
counts against an independent reader, and unit 4 AC8 grades a third spelling of the same column.

**Fix.** Extend §4's `LEG` row and header line to carry the ledger seconds, the ratio and the
under-3x flag, so the one place that pins the format matches S9 and AC11.

**Left-shift gate.** Have the `--manifest` test assert the row against the format string quoted in
§4 rather than against a hand-written expectation, so the spec's code block and the test cannot
diverge silently.

### R16 — the 2/8 split left `short_circuit` declared by neither unit

**Address:** unit 8, §4 Data model and §2 S3 / §6 AC3-AC4; unit 2, §4 Data model and §6 AC9.
*(source id 47)*

Unit 8's `[[lane]]` example declares `short_circuit = true` and S3, AC3 and AC4 all depend on it,
while unit 8 §3 disclaims the format outright: "`TOOL-aGatheredDeclaration-2` owns the schema and
ships the `[[lane]]` rows; this unit reads them." Unit 2's lane row at `:85-87` carries only `name`
and `concurrency`, its optional-key paragraph enumerates leg keys exclusively, and S1 defers the
field set to unit 1 §S4, whose union table maps `phase` → `lane` as a per-leg key and declares no
`[[lane]]` table keys at all. So the key unit 8 requires is declared by nobody, and either unit 8
lands against a schema that does not know it or the implementer widens unit 2's schema inside unit
8's commit — the schema drifting outside the unit that declares it, which is the single-source
property this build exists to establish. (The refusal half is weaker than it first looks: AC9 and §5
scope the unknown-key exit to legs, not lane rows, so the key is unvalidated rather than rejected.)

**Fix.** Unit 2 §4 enumerates the `[[lane]]` key set the way it enumerates the leg one — `name`,
`concurrency`, `short_circuit` (default false) — with `short_circuit` declared-and-inert exactly as
`full_only` is, and AC9 extended to a lane row carrying an undeclared key. Unit 8 §3 then reads
"unit 2 declares `short_circuit`; this unit gives it meaning".

**Left-shift gate.** Extend unit 2's unknown-key refusal to every table the loader owns, not just
`[[leg]]`, with one arm per table. A schema that validates one of its three tables is a schema with
two silent halves.

---

## LOW

### R17 — a citation imported from a prior review without re-verification

**Address:** unit 6 §10 final paragraph, mirrored in unit 7 §10.
*(source id 27)*

`grep -n vanished tools/govkit/govkit.py` returns exactly two hits: `:4115`, an unrelated comment,
and `:4462`, which carries the `"vanished is not a leg that passed"` message. The specs cite
`govkit.py:2510-2512`, which is the `deploy.get("decline")` block roughly 1950 lines away. The stale
number originates in
`memory/builds/.../2026-08-24-review-TOOL-dUnstalledConvoy-26-spec-rev2.md`'s H2, but both units
restate it in their own voice as live evidence for a consequence they say adopters will meet once per
migrated leg. Unit 5 §10 sets the standard the other two skipped: "A hit can be stale, so the two
open defects were re-read against source."

**Fix.** Repoint both citations to `tools/govkit/govkit.py:4461-4462` and state whether the branch
(before green, after `None`) actually fires on a format move or only on a leg rename.

**Left-shift gate.** None worth building. This is the §10 discipline unit 5 already demonstrates —
a hit carried from another record is re-read before it is restated.

### R18 — a rev-2 figure presented as re-derived is wrong by its own criterion

**Address:** unit 2, §4 "The wire format is RS/US and is an INTERFACE".
*(source ids 37, 48)*

Re-derived from `tools/gate-legs.json` at this base: 86 legs, 36 omit the `guard` key, and 2 more
declare `guard = []` (`run-gates wiring`, `lexicon wiring`). The emitter does
`",".join(l.get("guard", []))`, so both cases produce the empty field the RS/US separators exist to
preserve. The population the paragraph argues about is 38 of 86 (44%), not 36 (42%). The prior record
`memory/builds/aBoundedCeiling/reviews/2026-08-27-review-TOOL-aBoundedCeiling-1-round1.md:50` counted
38 of 85 by the same criterion, so the new figure silently disagrees with an existing review. The
argument survives; the number does not.

**Fix.** State 38 of 86, or drop the figure and write "an empty guard field is the common case, not
an edge — derive the count from the manifest", which is what the same section demands of
`--manifest` in unit 3.

**Left-shift gate.** The charter rule already covers it: no count of a derived population is written
in prose. If the figure is load-bearing enough to keep, it belongs in the arm that asserts the wire
format, not in the paragraph beside it.
