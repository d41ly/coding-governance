**Serves:** diff-review TOOL-aPrimedKeepalive-1 TOOL-aPrimedKeepalive-2 TOOL-aPrimedKeepalive-3 TOOL-aPrimedKeepalive-4 TOOL-aPrimedKeepalive-5 TOOL-aPrimedKeepalive-6 TOOL-aPrimedKeepalive-7 TOOL-aPrimedKeepalive-8 TOOL-aPrimedKeepalive-9

# Closing diff review — the nine units of aPrimedKeepalive, measuring the CODE and the shipped prose

*Node a, 2026-08-27, ROUND 1 of the closing diff review. This is the first review in this build whose
subject is the delivered tree rather than the specs. Three spec-audit rounds already ran over the SPECS
(4 blockers, then 1, then 2, then M4's NON-CONVERGENT exit promoted the two standing blockers to units
8 and 9); their subject was the specs' internal consistency and it is not re-opened here. Every figure
below was re-derived at HEAD `4393d8f2` against a clean tree with `wc -c`, `grep -n`, `sed -n`, `git
merge-base` and by running the gates named, not read out of any record.*

**Reviewed range: `b4e1d5be879bc8868529fb57c15657e271c39113...HEAD`.**

That base is the merge-base with `origin/main`, deliberately NOT the run's pinned BASE. The work
preceded its own `--preflight` because the pre-commit hook cost ten minutes per commit until unit 6
landed, so the pinned BASE is the tip of the built work and a `BASE..HEAD` diff would be empty. The
build README records this. The range covers 38 files, 2524 insertions, 53 deletions.

## Verdict: BLOCKED

Two blockers, four highs, five mediums and three lows, over fourteen distinct defects consolidated
from twenty confirmed findings. The tally sits in this paragraph rather than on the heading above
because that line's token is a closed set. One blocker reds the merge bar today, on this tree, with no
fixture: `bash tools/check-kit-versions.sh` exits 1. The other arms itself the moment `--close` flips
unit 3 to CLOSED and then reds the push-boundary bar. Neither is a judgement call and both are one
line of edit each.

**Review shape: raw 26 · confirmed 20 · refuted 6 · unverified 0 · precision 0.77.** The twenty
confirmed findings consolidate to fourteen distinct defects — six pairs were the same defect reached
by two lenses, and each pair is merged below with both anchors kept.

**The dominant shape is unchanged for the fourth consecutive round: `amendment-leaves-its-other-half-standing`.**
Both blockers are that class and so are three of the four highs. F1 is the shape at its purest — the
two halves are on the SAME LINE, and one of them moved. F3 is the third carrier of one claim, standing
inside the unit whose entire subject is that claim. F6 and F11 are the class committed by the unit
promoted to close the class. The spec-audit rounds named it, the fold committed it again, and the fold
that swept the fold committed it a third time.

## Findings, severity-ranked

| # | Sev | Site | Defect |
|---|---|---|---|
| F1 | BLOCKER | `tools/unattended/check-unattended.sh:29` | Kit bump moved the marker and the driver, left the leg's constant at 1.10 — merge bar is RED now |
| F2 | BLOCKER | acceptance ledger `:62` | Unit 3 AC7 has no evidence line; hygiene check 23 reds at the push boundary the moment the build closes |
| F3 | HIGH | `tools/unattended/PROTOCOL.template.md:354` | The BINDING contract still says the keepalive dies with the process — the claim the same kit calls MEASURED FALSE |
| F4 | HIGH | `tools/unattended/check-unattended.sh:1135` | Check 7's LANDING exclusion drops spec-4 S1's `sha-shaped` clause; any ref-resolvable witness disarms it |
| F5 | HIGH | `tools/unattended/unattended.sh:1126` | `check_single_live` carries the same omission at the higher-stakes half, and spec-7 S1 codifies the weaker predicate |
| F6 | HIGH | acceptance ledger `:132` | Unit 9's AC1 certifies an inventory wrong in both directions; nothing mechanical can ever contradict it |
| F7 | MEDIUM | `tools/unattended/check-unattended.sh:1131` | Both halves of the exclusion ship with zero test coverage and the arms gate cannot see them |
| F8 | MEDIUM | `tools/unattended/check-unattended.sh:1128` | The new exclusion notices print on the default channel, against this file's own stated contract |
| F9 | MEDIUM | `tools/memory-tree/check-memory-hygiene.sh:12` | The replacement `--staged` held-set enumeration omits check 21, which is also held |
| F10 | MEDIUM | acceptance ledger `:40` | Unit 1's AC6 quotes a string that exists nowhere in the tree; two sibling lines drift the same way |
| F11 | MEDIUM | acceptance ledger `:51` | Unit 2's AC6 reports 24 573 for a file that is 24 549, contradicting two other lines of the same record |
| F12 | LOW | `tools/memory-tree/check-memory-hygiene.sh:1107` | The header written to stop a wrong-number trust cites check 22 at `:610`; the block opens at `:611` |
| F13 | LOW | `tools/memory-tree/check-memory-hygiene.sh:1129` | Three sibling-guard citations are each exactly 7 lines short of their targets |
| F14 | LOW | `tools/memory-tree/README.md:18` | The kit README counts 23 checks and enumerates 22; check 23 appears in neither it nor `HYGIENE.md` |

---

## F1 — BLOCKER — the kit bump is half-applied, on one line

**Site:** `tools/unattended/check-unattended.sh:29`

The line reads `KIT_UNATTENDED_VERSION=1.10   # gov:kit unattended@1.11 — must match unattended.sh`.
The diff edited the comment half of that line and left the constant. `tools/unattended/unattended.sh:41`
reads 1.11, as do the PROTOCOL, SKILL and PLAYBOOK templates and all three installed renders. This one
line is the whole failure.

**Reproduced at HEAD, no fixture:**

```
$ bash tools/check-kit-versions.sh
kit-versions: tools/unattended/check-unattended.sh KIT_UNATTENDED_VERSION != 1.11 — the driver and its leg disagree about which kit this is
kit-versions: 1 problem(s)
rc=1
```

That leg's row in `tools/gate-legs.json` carries no `guard` key, so it runs on every bar on every node,
including the total run `.githooks/pre-push` forces. The bar cannot go green and the push is blocked.
Tried to refute via a guard, a `GATE_FULL` exemption, and a tolerant regex — `check-kit-versions.sh:150`
matches `^KIT_UNATTENDED_VERSION=$uc([^0-9.]|$)` and does not tolerate it. None holds.

**Fix:** set `KIT_UNATTENDED_VERSION=1.11` at `tools/unattended/check-unattended.sh:29`. Re-run
`bash tools/check-kit-versions.sh` and confirm rc=0.

**Left-shift:** the gate already exists and already catches this — what failed is that nothing ran it
between the bump and the closing review. Move `tools/check-kit-versions.sh` into the pre-commit fast
leg. It is a grep over a fixed carrier list, sub-second, and it is the one gate that would have made
this defect impossible to carry for nine units.

## F2 — BLOCKER — unit 3 numbers AC7 and the ledger stops at AC6

**Site:** `memory/builds/aPrimedKeepalive/build/2026-08-27-build-TOOL-aPrimedKeepalive-1-7-acceptance-ledger.md:62`

The `**Evidences:** TOOL-aPrimedKeepalive-3` block runs AC1 through AC6. Spec 3 numbers AC1 through
AC7 — AC7 was added at rev-3 by the fold (spec-3:129, logged at spec-3:150 as "S5 and AC7 added") and
never reached the ledger. `grep -rn Evidences memory/builds/aPrimedKeepalive/` shows the ledger is the
only record in this build carrying Evidences blocks, so no other tracked file supplies it.

Spec 3's header is `INPROGRESS · rev-3 · 2026-08-27 · node a · Tier-2`. The date sorts at-or-after
`ACCEPTANCE_LEDGER_CUTOFF="2026-08-20"` (`.memory-tree.conf:270`) and the id is absent from
`ACCEPTANCE_LEDGER_GRANDFATHER` (`:288`). Replaying check 23's own flattener and label extractor (the
awk at `check-memory-hygiene.sh:1188-1194`) over this build yields exactly one gap:
`TOOL-aPrimedKeepalive-3/AC7`.

It is not red today only because the spec is still INPROGRESS. **Closing the build is what arms it**,
and `.githooks/pre-push` runs that bar:

```
HYGIENE check 23 FAILED — a CLOSED unit numbers an acceptance criterion that no journal record evidences ... TOOL-aPrimedKeepalive-3/AC7
```

This is precisely the failure unit 9 was promoted to prevent, and unit 9's inventory never listed it —
spec 3 was DROPPED from the round-3 subject set because it took no round-2 finding, so the audit that
caught the identical omission on units 1, 2, 4 and 6 never looked at this one. Unit 9 then fixed
exactly the four it was handed. It also breaks this build's own unit-9 AC3 directly.

**Fix:** append an AC7 line to the unit-3 Evidences block in one of the two legal forms. The OBSERVED
form is available now, not amendable: `` grep DIRECTIVES_FLOOR tools/unattended/.unattended.conf.example ``
returns `16`, which equals the driver's `DIRECTIVES_CORE` word count — both true at HEAD. Then re-run
the flatten-and-join, or the full `bash tools/memory-tree/check-memory-hygiene.sh`, before closing.

**Left-shift:** make `unattended.sh --close` run check 23's join over the build's own specs BEFORE it
flips any status header to CLOSED. The check exists, is correct, and fires — it just fires after the
verb that arms it, at the push boundary, which is the most expensive place to learn this. A pre-flip
join is the same code path against the same population and refuses in a second.

## F3 — HIGH — the binding contract still asserts the claim the kit calls MEASURED FALSE

**Site:** `tools/unattended/PROTOCOL.template.md:354`, and its render `memory/guides/UNATTENDED-PROTOCOL.md:354`

Unit 8 removed the "a resumed keepalive is dead" claim from the two Skill sites and left the protocol's
copy standing. Section 5 still opens:

> The scheduling store is in-memory and session-scoped. The job is gone when the agent process exits,
> and deleting it removes it from that same store.

`SKILL.template.md:589-594` calls that intuition MEASURED FALSE in the same kit and cites the
measurement — `TOOL-aPromptedMandate-11`, a run that asserted two keepalives dead while the scheduler's
own listing showed both still firing. `SKILL.template.md:9` names the protocol as the binding contract,
so **on a conflict the false half wins**. Worse, `grep -i resume` over the protocol returns only `:223`
and `:451`: the protocol carries no resume carve-out at all, so a resumed run reading §5 has nothing
redirecting it to the Skill's `## Resume`. It skips the reap and attests `keepalive-reaped` green over
a job still firing — the exact orphan leak unit 8 was promoted to close.

The diff rewrote the bullets immediately under that sentence (unit 1) without touching it, and unit 8's
spec scopes itself to the Skill only. The distinct claim at `SKILL:42` and `:716` — "orphaned in a store
no later run can see" — is about REACHABILITY, is true, and is not this.

**Fix:** rewrite the §5 opening in the template and re-render. State only what is measured: the store is
in-memory and session-scoped and no script can reach it, and a job is NOT known to die with the session
(cite `TOOL-aPromptedMandate-11`). Then `bash tools/unattended/adopt-unattended.sh --check`.

**Left-shift:** unit 8's AC1 was a `grep -c "dead before it starts"` over ONE file. Promote it to a
kit-wide banned-claim list checked by `adopt-unattended.sh --check` across every carrier the kit owns —
protocol template, skill template, playbook template and all three renders. A retired claim that is
grepped for in one file and not the others is the same defect one level up.

## F4 — HIGH — check 7's LANDING exclusion accepts any ref-resolvable witness as a sha

**Site:** `tools/unattended/check-unattended.sh:1135`

The predicate is:

```sh
if [ "$c7ph" = LANDING ] && [ -n "$c7anchor" ] \
   && GIT rev-parse --verify --quiet "$c7w^{commit}" >/dev/null 2>&1 \
   && GIT merge-base --is-ancestor "$c7w" "$c7anchor" 2>/dev/null; then
```

No sha-shape narrowing. Spec-4 S1 states the scope verbatim as a witness that is "sha-shaped, resolves
in this clone, and is an ancestor" — the first clause is unimplemented, and unit 4's AC set grades the
phase clause (AC4) and the fail-closed clause (AC3) but never that one.

Check 7 is the guard that stops two unattended runs — each of which merges and pushes to the default
branch with no owner present — from being live at once. The protocol at `:286-298` deliberately sanctions
a tag or a workflow id as a witness and narrows to a sha only where "the ancestry of the witness IS the
claim". That is exactly what this predicate asserts, and check 15 at `:737` already enforces the
narrowing for the identical claim at LANDED, with a comment giving the reason. Check 6 at `:721`
explicitly SKIPS a non-sha-shaped witness, and `test.sh:626` pins that skip on `witness: wf_077104e6`.
`unattended.sh:1411` says it outright: "nothing constrains a non-LANDED witness to a sha".

So at LANDING nothing constrains the shape, and a record carrying `witness: main` (or `HEAD`, or a tag)
resolves through `rev-parse main^{commit}` and passes `merge-base --is-ancestor main $ADV_HEAD` on any
node whose local default branch is at or behind the advertised tip. Demonstrated against this tree:
witness `b4e1d5be~1` satisfies both tests and would be excluded, while the protocol calls that witness
unjudgeable for an ancestry claim. **The run is the sole author of the witness field, so the guard
against two concurrent unsupervised runs is escapable by one word in a file the run writes.**

Tried to refute as a harmless liberalization. It is not: for a mutable ref the ancestry test says
nothing about the run's own work, which is the reasoning check 15 already records nine hundred lines up.

**Fix:** wrap the resolve in the shape guard this file already uses at `:735-737` and `:866`:

```sh
case "$c7w" in [0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f]*) ;; *) c7w="" ;; esac
```

and report the non-sha case as a named fail-closed cause the way S3's other three causes are reported.

**Left-shift:** see F7 — the same test arms cover this and F5. Additionally, a two-line grep leg over the
kit asserting that every `merge-base --is-ancestor` applied to a witness is preceded by the sha-shape
`case` in the same block. Three sites exist today and two of them are correct; the predicate for the
leg is already written in the file.

## F5 — HIGH — the driver's copy carries the same omission, at the admission point

**Site:** `tools/unattended/unattended.sh:1126`

```sh
if [ -n "$w" ] && GIT rev-parse --verify --quiet "$w^{commit}" >/dev/null 2>&1 \
   && GIT merge-base --is-ancestor "$w" "$anc" 2>/dev/null; then
```

Byte-equivalent to F4's, and **not a duplicate of it**: different file, different spec, and spec-7 §3
makes sharing one implementation an explicit non-goal ("They are copy-installed standalone"), so fixing
the leg leaves this standing. Spec-7 §10 says outright that the two must move together.

Impact is higher than the leg's. `check_single_live` gates `verb_preflight` — the point where a second
unattended run is ADMITTED or refused. A run-state file naming a resolvable non-sha witness at LANDING
makes the driver stop counting that record and a genuinely competing run passes preflight. The driver's
own header names "an archive hand-edited back to a non-terminal phase" as the threat model, so a
hand-written or ref-shaped witness is in scope by the code's own stated design.

There is also a specification defect underneath: spec-7 S1 codifies "whose witness resolves" while
spec-4 S1 codifies "sha-shaped, resolves". **Two halves of one predicate, specified differently.** The
driver matches its own spec, which makes this a spec defect rather than a code-vs-spec one, and the
shipped behavior is still the weaker predicate at the higher-stakes half.

**Fix:** apply the same `case` guard here, and reconcile spec-7 S1 with spec-4 S1 so one predicate has
one specification.

**Left-shift:** the two copies are deliberately separate implementations, which means nothing structural
holds them equal. Add a parity arm — a leg asserting the two predicate texts are token-identical modulo
variable names — or accept the divergence and make each spec state the OTHER half's spelling verbatim so
a reader of either finds the pair. The current arrangement has neither.

## F6 — HIGH — unit 9's AC1 certifies an inventory that is wrong in both directions

**Site:** `memory/builds/aPrimedKeepalive/build/2026-08-27-build-TOOL-aPrimedKeepalive-1-7-acceptance-ledger.md:132`

The line reads: "every criterion a fold added now carries a line: unit 1 AC8 and AC9, unit 2 AC9, unit 4
AC6, unit 6 AC5."

Both directions verified. Unit 1's block (lines 35-43) does carry AC8 and AC9; unit 2's (46-54) AC9;
unit 4's (65-71) AC6. **Unit 6's block runs AC1 through AC4 and stops**, while spec-6 §6 numbers AC1
through AC5. So `unit 6 AC5` is asserted present and is absent. And the enumeration omits spec-3's
rev-3-added AC7 entirely — the one entry that reds a gate (F2).

The claim is recorded in OBSERVED form, with a backticked path, and it is false. **Nothing can catch it:**
unit 6 is Tier-1, and check 23's join filters on `case "$hdr" in *"Tier-2"*`, so the join never looks at
unit 6. That is exactly the hole round 3's finding 7 named — "its AC5 is simply ungraded with nothing
that will ever say so". Unit 9's whole job was closing that list, so **its acceptance is self-certified
against work it did not do**, and any Definition-of-Done claim of full acceptance coverage for this
build is false. `fallback-fabricates-the-passing-value`, in a record the DoD reads as evidence.

**Fix:** add the missing AC5 line to the unit-6 Evidences block — its subject is observable at HEAD
(`grep -n '# ---- 2[23]:' tools/memory-tree/check-memory-hygiene.sh` returns 23, plus the HELD line
naming check 23 alone). Then rewrite AC1's enumeration from what the ledger actually contains rather
than from the rescope reason in `memory/builds/aPrimedKeepalive/RUN.md`, which carries the same
incomplete list.

**Left-shift:** stop letting a hand-typed enumeration be the certificate. A "the ledger is complete"
criterion should cite the OUTPUT of the flatten-and-join, not a list a human retyped from a rescope
note. If check 23's Tier-2 filter is to stay, the join should still ENUMERATE the Tier-1 units it
skipped, so a skip announces itself instead of reading as coverage (§7's own rule).

## F7 — MEDIUM — both halves of the exclusion ship with zero test coverage

**Site:** `tools/unattended/check-unattended.sh:1131` and `tools/unattended/unattended.sh:1122`

`git diff --stat b4e1d5be...HEAD` lists no `*.test.sh` file at all. Neither half of the new exclusion is
exercised. The arms meta-gate cannot see it either — the exclusion adds no `fail N` call site, and
`python tools/memory-tree/check-arms.py --check` exits 0 unchanged.

The only existing check-7 arm (`check-unattended.test.sh:631-642`) builds `tTwo` at phase RUNNING, so it
never enters the `[ "$c7ph" = LANDING ]` branch. I confirmed the negative controls: dropping the LANDING
guard leaves that arm green because tTwo's witness is a local commit not on the fixture's origin, and
dropping the `merge-base` test leaves it green because no fixture record sits at LANDING.

This is a NARROWING of the one check that guarantees "the run" is well-defined, and the negative
controls that make it safe are asserted only in the acceptance ledger's prose. A later edit dropping
either clause leaves `check-unattended.test.sh`, `unattended.test.sh` and the arms gate all green while
two genuinely live runs stop being detected.

Per AGENTS.md the kit's self-tests left the bar with the compensating check being "run them when the
checker's source changes". The source changed and they were not extended.

**Fix:** add two arms beside the existing check-7 block at `:631` — a second live record at LANDING with
a witness off the fixture's advertised tip (must HIT the check-7 failure), and the same record with an
on-tip witness (must MISS it and HIT the EXCLUDED line) — plus the mirrored pair in `unattended.test.sh`
for `check_single_live`. Add a third arm each with a non-sha witness, which is F4/F5's red proof.

**Left-shift:** `check-arms.py` discovers its population from `fail N` call sites, so a check that
narrows by EXCLUDING rather than by failing is invisible to it by construction. Extend its discovery to
any `EXCLUDED`/exclusion emission, or the class recurs on the next narrowing anybody writes.

## F8 — MEDIUM — the exclusion notices print on a channel this file's own header forbids

**Site:** `tools/unattended/check-unattended.sh:1128`

The header at `:12-:18` states `Exit 0 + no output = clean. Anything printed is a violation`, then names
ONE EXCEPTION assigning exactly this category — a check that cannot COMPARE announcing the case it could
not reach — to the REPORT channel "so the line keeps its meaning". The new `check 7 exclusion UNAVAILABLE`
and `check 7 EXCLUDED` lines are unconditional `printf` to stdout. The header was not amended.

Reproducible on this tree with no fixture. The non-terminal set is aPrimedKeepalive (REVIEWING) and
`memory/builds/dTieredTribunal/RUN.md` (LANDING, witness `eb4b0660`), and
`git merge-base --is-ancestor eb4b0660 origin/main` returns ANCESTOR against the advertised tip, so a
clean run emits `unattended: check 7 EXCLUDED memory/builds/dTieredTribunal/RUN.md — …` and returns no
failure. An adopter applying the documented contract reads a green leg as red.

The prefix matters: the pre-existing liveness NOTE at `:561` uses a different prefix AND goes to stderr,
whereas these land on stdout beside `fail()`'s output. The commit's own inline comment argues the choice
against `report()` without touching the header that forbids it — one rule, two answers.

**Fix:** either amend the header to name check 7's exclusion notice as a second sanctioned
default-channel emission and say why, or route the UNAVAILABLE line (a could-not-compare announcement,
the documented REPORT category exactly) through `report` and keep only EXCLUDED unconditional.

**Left-shift:** a leg asserting every unconditional `printf 'unattended:` in this file is either a
`fail`/`report` call or is named in the header's exception list. The header already IS the declaration;
nothing currently reads it.

## F9 — MEDIUM — the replacement `--staged` enumeration is itself incomplete

**Site:** `tools/memory-tree/check-memory-hygiene.sh:12`

The new header names the held set as "13-16, 17-19, the row-grammar arm and 23". Enumerating every
staged guard in the file: `:1058` (13-16), `:1073` (17-19), `:1083` (check 20, the row-grammar arm),
`:1141` (23) — and `:674`, `if [ "$STAGED" = 0 ] && printf '%s\n' "$c21_sel" | grep -q .`, which holds
check 21's entire body including all four fail arms and the `RECORD_UNBOUND_PIN` refusal.

**Check 21 is held and is not named.** It also prints no HELD line, unlike 23, so it is the one held
check that does not announce itself. The repeat at `:1129` omits 20 and 21 as well.

A hand-typed inventory of a machine-enumerable set, replacing a claim the same comment condemns for
being one rule with two verdicts, in a header whose own text records that "A spec trusted this header
and graded the wrong check". A reader or a future spec now believes check 21 binds at commit time.

**Fix:** add 21 to both enumerations, or better, stop enumerating in prose — derive the held set with a
single grep for `[ "$STAGED" = 0 ]` and say so. The list has now been wrong twice.

**Left-shift:** the derivation IS the gate. A four-line check comparing the header's enumeration against
`grep -c 'STAGED" = 0'` over the file would have caught both wrong versions, and per §7 no count of a
derived population belongs in prose beside the thing it counts.

## F10 — MEDIUM — unit 1's AC6 records an observation nobody made

**Site:** `memory/builds/aPrimedKeepalive/build/2026-08-27-build-TOOL-aPrimedKeepalive-1-7-acceptance-ledger.md:40`

The line states M10's keepalive bullet `reads "Create it before ANY other act"`.
`grep -rn "before ANY other act" --include=*.md` returns exactly one hit in the whole tree: the ledger
line itself. The shipped bytes at `memory/guides/BUILD-METHOD.md:276` and its template twin read
`Create it FIRST, reap it before the wrap-up. Both halves: protocol §5.`

The criterion's SUBSTANCE is satisfied — spec-1 AC6 requires only that the bullet no longer read "Create
it before preflight", which `git show b4e1d5be` confirms was the prior wording. That is what makes it
worse: the record that is the sole join between a criterion and the thing that answered it carries a
quotation of bytes that do not exist, and hygiene check 23 grades SHAPE only. A backticked token makes
the line `obs` and it passes forever; the check's own header says it never verifies that an observation
token names anything real. A re-verifier greps the quoted string, gets zero hits, and cannot distinguish
a mis-transcription from a reverted edit.

Two sibling lines drift the same way in the same block: AC2 says the routing table is at line 40 of the
rendered Skill and it is at line 46; `:50` quotes `ADOPT (protocol §11)` where `BUILD-METHOD.md:274` says
`ADOPT (§11)`.

**Fix:** re-run each quoted observation against HEAD and replace the text with what the file says, or
restate the criterion so it grades the obligation rather than a byte string that moves on every fold.

**Left-shift:** an OBSERVED-token liveness arm for check 23. When an evidence line quotes a
double-quoted string alongside a backticked file path, grep that string in the named file and fail on
zero hits. It is a narrow, cheap, high-yield check and it closes F10 and F11 together — this build alone
gives it four live instances.

## F11 — MEDIUM — one record, two answers, about a carrier 27 bytes under a cap this run may not raise

**Site:** `memory/builds/aPrimedKeepalive/build/2026-08-27-build-TOOL-aPrimedKeepalive-1-7-acceptance-ledger.md:51`

Unit 2's AC6 reads `` wc -c memory/guides/BUILD-METHOD.md `` — 24 573. Measured at HEAD: 24549. The
Measured table at `:24` says 24 549 and unit 1's AC7 at `:41` says 24 549. Three-way contradiction inside
one file, in one commit.

Walking the branch: the file genuinely was 24573 through `78c4e727` and was trimmed to 24549 at
`b944720c`; at `4393d8f2` the unit-9 sweep updated the Measured row and unit 1's AC7 and left unit 2's
AC6 at the old value. **The sweep touched two of three sites** — `amendment-leaves-its-other-half-standing`
inside the unit that exists to close it.

Spec-2 AC6 was amended at rev-2 specifically to grade BOTH halves of the pair, and the ledger line grades
only the render. The template is the tighter half by 11 B, is the BINDING half, and is the one that
actually breached during this build (spec-2 §4 records it at 24 584, 8 B over). So the amended
both-halves condition is unevidenced for the half the amendment was written for.

One correction to the reported impact: 24 573 is still under M1's 24 576, so a reader budgeting against
it infers 3 B of headroom where there are 27 — the defect is the contradiction, not a false breach.

**Fix:** rewrite the line as `` AC6 — `wc -c` over BOTH halves — `tools/memory-tree/BUILD-METHOD.template.md`
24 560 and `memory/guides/BUILD-METHOD.md` 24 549, each at or below M1's 24 576 ``, matching unit 1's AC7.

**Left-shift:** F10's OBSERVED-token re-runner covers this too — an evidence line naming a `wc -c` and a
path is re-runnable verbatim. Failing that, one check that a build record gives a single answer per
(metric, path) pair; this record gave two in the same commit.

## F12 — LOW — the anti-stale-pointer header carries a stale pointer

**Site:** `tools/memory-tree/check-memory-hygiene.sh:1107`

The header cites check 22 at `:610`. `grep -n '^# 22 — THE REVIEW VERDICT'` returns 611; line 610 is
blank (the `fi` closing check 9 is 609). The citation is new in this branch and was off by one on
arrival, because the same commit added seven lines above it.

Off by one, so a reader sees the target immediately rather than hunting — which is why it grades low.
It stands because it is a stale in-file pointer inside the one paragraph written to stop exactly that
("A spec trusted this header and graded the wrong check").

**Fix:** cite `:611`, or drop the number and cite the block by name (`# 22 — THE REVIEW VERDICT VOCABULARY`),
which cannot drift when lines shift.

**Left-shift:** see F13 — one leg covers both.

## F13 — LOW — three sibling-guard citations, each exactly 7 lines short

**Site:** `tools/memory-tree/check-memory-hygiene.sh:1129`

The comment cites the `13-19` guards at `:1051`, `:1066` and `:1076`. Those lines are `$bad12"` (the
fail-12 message terminator), `' "$ids"` and `' "$got"; status=1` (two printf continuations). The actual
`if [ "$STAGED" = 0 ]` guards are at 1058, 1073 and 1083.

One correction to the finding's rationale, which does not change the fix: the citations were NOT wrong
when written. `git show 5816a9b64` has the guards at exactly 1051, 1066 and 1076. They drifted because a
LATER commit added a 7-line `--staged` explainer to the top-of-file header (hunk `@@ -6,11 +6,18 @@`,
net +7). Wrong provenance, same defect, same fix.

**Fix:** correct to `:1058`, `:1073`, `:1083`, or drop the line numbers and cite by check number only.

**Left-shift:** a two-line leg banning bare `` `:NNN` `` self-citations inside tracked shell comments —
they are line numbers with nothing deriving them, they move on every edit above them, and this file now
carries four wrong ones (F12 plus these three) in a header whose subject is that exact failure. Cite the
block by name; a name does not shift.

## F14 — LOW — the kit README counts 23 checks and enumerates 22

**Site:** `tools/memory-tree/README.md:18`

The line claims "23 checks (1-12, 21 and 22 in the shell, 13-16 delegated to `corpus_ids.py`, 17-19 to
`gotchas.py`, 20 to `row_grammar.py` …)". Counting the names: 1-12, 21, 22, 13-16, 17-19, 20 = 22. Check
23 — the acceptance-ledger join, live in the shell at `check-memory-hygiene.sh:1108-1205` with three fail
arms and a `pop_guard` — appears nowhere in it. `memory/HYGIENE.md`'s numbered checklist also ends at
item 22, and `README.md:5` still says "21-check hygiene gate", staler still.

**Caveat on attribution, not on the defect:** the README is not in this branch's diff (the range touched
only the `gov:kit` marker line of `HYGIENE.md` and `HYGIENE.template.md`), so the mismatch predates unit
6 rather than being created by it. Unit 6 corrected the block header inside the script from 22 to 23 and
left the sibling carriers a deployer reads. The defect is real, reachable by any deployer, and low.

**Fix:** update the parenthetical to "1-12, 21, 22 and 23 in the shell", fix `:5`, and add the matching
item 23 to `memory/HYGIENE.md` and `tools/memory-tree/HYGIENE.template.md` beside item 22, describing the
join and its `--staged` hold.

**Left-shift:** the check count and the enumeration are both derivable from the script. A leg comparing
the README's and `HYGIENE.md`'s enumerations against the script's actual check headers closes this
permanently. Right now the number is typed in three places and has been wrong in two of them since
before this build started.

---

## What was refuted

Six of twenty-six raw findings did not survive the skeptic and are recorded as refuted, not carried.
None of them changed a severity below. No finding is OUTSTANDING — the unverified count is zero, so
every row above has a verdict behind it.

## The checklist, and what it selected

`python tools/memory-tree/gotchas.py --for-diff` over this range selected 22 classes. Four of them have
live instances in the findings above:

- `amendment-leaves-its-other-half-standing` — F1, F2, F3, F6, F11. Five of fourteen, both blockers, and
  three of four highs. Fourth consecutive round in which it dominates.
- `fallback-fabricates-the-passing-value` — F6, F10. Records asserting an observation that was not made.
- `two-answers-to-one-question` — F8, F9, F11. One rule, two verdicts; one metric, two numbers.
- `gate-green-by-accident-on-generated-bytes` and `fixture-passes-by-finding-nothing` — F7, whose existing
  check-7 arm stays green with either clause of the new predicate deleted.

`vacuous-selector-empty-population` and `staged-break-substitutes-a-synthetic-value` were checked against
F4/F5 and F7 and did not produce a finding beyond what is recorded.

## The caps, re-measured at HEAD

All four capped carriers were re-measured and all four are under. None is raiseable by this run.

| Carrier | Measured | Cap | Headroom |
|---|---|---|---|
| `tools/memory-tree/BUILD-METHOD.template.md` | 24 560 B | M1's 24 576 B | 16 B — the BINDING half |
| `memory/guides/BUILD-METHOD.md` | 24 549 B | M1's 24 576 B | 27 B |
| `memory/guides/UNATTENDED-PROTOCOL.md` | 681 L / 55 700 B | `GUIDE_CAP_LINES=750` / `GUIDE_CAP_BYTES=61440` | 69 L |
| `memory/guides/SESSION-KICKOFF.md` | 25 417 B | `MAX_MANIFEST_BYTES=25600` | 183 B |

F11's fix costs bytes in the ledger, which is uncapped. F2, F6 and F10's fixes are also ledger-only.
F3's fix rewrites protocol §5 and has 69 lines of headroom to work in.

## What has to happen before this lands

F1 and F2 are the merge bar. F1 reds it today; F2 reds it at the moment of closing. Both are single-line
edits and neither needs a decision.

F3, F4, F5 and F6 are the four highs and none is cosmetic: F3 ships a false instruction in the binding
contract on the path that leaks keepalives, F4 and F5 leave the concurrency guard escapable by one word
in a file the run itself writes, and F6 makes this build's own completeness certificate false. F7's test
arms are the red proof F4 and F5 need anyway, so they land together.

The five mediums and three lows are records and comments. They are cheap, and eight of the fourteen
defects here are a record disagreeing with the tree it describes — which is the class this repo's own
drift audit exists for and the reason the closing review found more of them than the code.
