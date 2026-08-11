# Review aWrittenMethod-2 — Tier-2 on the cumulative diff landing on main

**Date:** 2026-08-11 · **Tier:** 2 · **Streams:** tooling
**Subject:** `git diff 7f614a1...HEAD` @ `d0c0485` — 25 files, +1306/-133. The unattended kit's
authorization hardening (`unattended.sh`, `check-unattended.sh` and both test siblings), the
six-fact protocol amendment (`PROTOCOL.template.md` + `memory/guides/UNATTENDED-PROTOCOL.md`), the
sed-free render rewrite copied across four adopters, and the five aWrittenMethod specs.
**Question asked:** does the authorization the kit exists to enforce actually hold against a run
that wants to defeat it?

## 1. Verdict

**One open blocker, and it is the one that matters: the mandate authorization can be forged with a
single local `git update-ref`, no push and no network.** Check 9 anchors the BASE at
`refs/remotes/origin/<default>` and calls that "outside the run's reach" — but a remote-tracking ref
is an ordinary local ref. A run commits a forged mandate on its own branch, points the tracking ref
at that commit, and `merge-base(origin/main, HEAD)` becomes the forged commit. Checks 9 and 13 then
both certify it, `check-unattended.sh` exits 0 with no output, and the driver's `mandate-reachable`
DoD item passes. Reproduced end-to-end in a scratch repo built from this kit's own test seed
(**id=1, blocker**). The same diff ships the opposite claim to every adopter: PROTOCOL.template.md:22
and memory/guides/UNATTENDED-PROTOCOL.md:22 now assert "The BASE it is reachable from is anchored
outside the run."

The trust root is compromised twice, at two different code sites. `canonical_ref()` — the D3 fix
whose whole purpose is to give `fail 22` a second opinion on `GOV_DEFAULT_BRANCH` steering — reads
`refs/remotes/origin/HEAD`, a local **symref** any process rewrites with one `git symbolic-ref`. Its
contract comment at unattended.sh:139 says "derived from NOTHING the run supplies"; a two-arm test
shows arm A (steer alone) correctly refusing and arm B (steer plus one local symbolic-ref write)
printing `unattended: preflight OK` over a forged mandate, then GATE EXIT=0 (**id=2, high**). Fixing
the anchor ref without fixing the symref that names it leaves the steer standing.

The third high is the mirror image — the gate refusing where it should not. Check 9 recomputes the
merge-base for **every** tracked `RUN.md`, including one in a terminal phase. The first unattended
run that actually lands turns the default-branch bar permanently red: after the merge the recorded
BASE is no longer the merge-base and `origin/main == HEAD`, both by construction, and nothing
deletes or archives a LANDED run-state file (**id=6, high**). `.githooks/pre-push` blocks a red push,
so the kit's first success is also the event that bricks the bar.

The fourth high is a defect class this repo has a meta-gate against. The sed-free render rewrite
introduced `out=$(cat "$TEMPLATE"; printf X) || return 1` — a command substitution whose status is
`printf X`'s, so the guard is a branch no input can take — and the same hunk deleted the
`set -o pipefail` that used to make the old sed render fail loudly. The two refusal strings this diff
*wrote* ("the render FAILED — the template could not be read") are unreachable. The idiom was copied
into four siblings; `adopt-memory-tree.sh` has no emptiness guard on any of its three
`render_doc > …` writes, and `adopt-drift-audit.sh:153` writes the Skill with neither a temp file nor
`[ -s ]`, so a failed read yields a zero-byte SKILL.md, prints "rendered", and `--check` then diffs
empty-against-empty and reports "in sync" (**id=14 / ids 4, 8, 11, high**).

The blocker that reddened the bar is **already remedied in this diff**: specs 2 and 6 landed
INPROGRESS while product source cited their ids, driving the shrink-only
`non_terminal_specs_cited_by_product_source` from 2 to 4 (**id=5, blocker — CLOSED at `d0c0485`**).
The signal now reads 2 of a pin of 2 and the leg is green. It stays in the report because it is the
only finding a gate caught, and because the pin has zero headroom: the next id-citing comment on a
non-terminal spec reds the bar again.

The through-line: **every new guard this diff added is a second read of an input the run can
write.** `canonical_ref`, the base-ref cross-check, the check-9 anchor — three "independent"
derivations, all rooted in local refs. The kit's own comment at unattended.sh:119-121 names the
required property correctly ("Moving it requires a push") and then does not implement it.

## 2. Review shape

| raw | confirmed | refuted | unverified | precision |
|-----|-----------|---------|------------|-----------|
| 18  | 15        | 3       | 0          | **0.83**  |

Every confirmed finding survived an adversarial skeptic pass; nothing is outstanding. The 15 confirmed
findings collapse to **9 distinct defects** — ids 4/8/11/14 are four lenses on one dead read guard,
ids 3/10 are one absent-pin guard, ids 9/15 are one discarded `fail` argument, and ids 13/18 are one
stale map dossier. They are folded below rather than listed separately, because unlike review -1 their
fixes are the same edit.

Severity legend: **B** blocker (2 — one open, one closed in-flight) · **H** high (3) ·
**M** medium (4) · **L** low (6).
"Left-shift gate" = the mechanical check that would have caught the class before a human read the diff.

---

## 3. Findings

### B1 — [blocker] The BASE anchor is a ref the run rewrites with one local command
`tools/unattended/check-unattended.sh:198` (anchor derived at :180-189; the mandate read at :217-231
hangs off the same value) · ids 1

Check 9 computes `mb=$(git merge-base "$lref" HEAD)` where `$lref` is
`refs/remotes/origin/<default>`. A remote-tracking ref is an ordinary local ref: `git update-ref
refs/remotes/origin/main <any commit>` succeeds with exit 0, contacts nothing, and needs no push.

**Reproduced.** In a scratch repo seeded from this kit's own harness: the owner committed
`memory/builds/tRun/RUN.md` with an **empty** mandate block on main and pushed it to a bare origin
(`git remote set-head origin main`). On branch `unit` the run committed a forged
`The owner authorizes tRun to merge and to push.` (commit C), added one commit on top, then ran
`git update-ref refs/remotes/origin/main C`. `merge-base(origin/main, HEAD)` became C; `base:` and
`base-ref:` were recorded **honestly**; `bash tools/unattended/check-unattended.sh` printed nothing
and exited 0; the driver's `mandate-reachable` DoD item passed (only the two agent-attested items
were unmet). Control: restoring the honest anchor and re-recording the base made the same tree red
with `UNATTENDED check 13 FAILED — the mandate block is absent or empty at the recorded BASE`.

Both authorization checks are defeated at once — check 13 reads `git show "$rb:$f"` at that same
run-chosen commit. And the same diff ships the contradicting claim to adopters at
`tools/unattended/PROTOCOL.template.md:22` / `memory/guides/UNATTENDED-PROTOCOL.md:22`.

**Fix.** The anchor must be a value no local command can write. Before trusting `$lref`, resolve the
default-branch tip from the **remote** — `git ls-remote --exit-code origin "refs/heads/$d"` — and
refuse unless it equals `git rev-parse "$lref"`. On no network, **refuse**: a check that cannot run
is not a passing one, which is the rule this same file already applies to an absent `base:`.
Equivalent alternative: require the mandate commit to be reachable from a ref the owner controls
out-of-band — a signed tag verified with `git tag -v`, or an owner-signed commit verified with
`git verify-commit` — instead of from a remote-tracking ref.

**Left-shift gate.** A red arm in `check-unattended.test.sh` that performs exactly the two commands
above (`git update-ref refs/remotes/origin/<default> <run commit>`, then run the leg) and asserts the
leg **reds**. More generally: a gate-authorship rule that every "outside the run's reach" claim in the
kit names the command that would move the value and asserts that command fails or is detected —
`check-arms.py` already enforces the analogous rule for `fail` branches.

---

### B2 — [blocker, CLOSED at `d0c0485`] Non-terminal specs cited by product source reddened the bar
`memory/builds/aWrittenMethod/spec/2026-08-11-spec-aWrittenMethod-2.md:3` and `…-6.md:3` · id 5

The diff added spec-2 and spec-6 with `Status: INPROGRESS` while landing product source that cited
their ids, driving the shrink-only signal `non_terminal_specs_cited_by_product_source` from 2 to 4.
`bash tools/run-gates.sh` was RED — `GATE FAIL drift-audit records (exit 1)`, 46 of 47 legs passing —
and `.githooks/pre-push` blocks a red default-branch push, so the cumulative diff could not land. At
base `7f614a1` the signal read exactly 2 (aBatchedLintel + aGuardedTally), so the diff introduced it.

**Status: remedied in-flight.** `d0c0485` stripped the id comments from the nine citing files
(driver, gate leg, three adopters, the parity leg), keeping the prose. `python
tools/drift-audit/drift_report.py --check` at the tip now reports
`non_terminal_specs_cited_by_product_source 2 of 23 — ok (pin 2, drain it)`.

**Residual risk.** The pin has **zero headroom**. The chosen remedy — drop the citation rather than
close the spec — trades traceability for the green light and leaves the next id-citing comment on a
non-terminal spec to red the bar again. Prefer moving specs to a terminal status (as spec-1 already
is) when the source that cites them lands. Do **not** raise the pin at
`tools/drift-audit/drift_signals.py:137`; it is declared shrink-only.

**Left-shift gate.** Run `python tools/drift-audit/drift_report.py --check` at DoR on the diff, not
only at the push boundary — this is the one finding in the set a gate caught, and it caught it late.
A pre-commit fast leg for the zero-tolerance drift signals would have caught it at authoring time.

---

### H1 — [high] `canonical_ref()` reads a symref the run can rewrite, so `fail 22` agrees with any steer
`tools/unattended/unattended.sh:142` (contract comment at :139, cross-check at :189-194;
`tools/unattended/check-unattended.sh:181` derives from the same symref) · id 2

`canonical_ref()` is documented as "derived from NOTHING the run supplies" and reads
`refs/remotes/origin/HEAD` — a **local symref**. `git symbolic-ref refs/remotes/origin/HEAD
refs/remotes/origin/<x>` succeeds in a repo with no remote configured and no network.

**Reproduced, two arms.** Arm A — steer with `GOV_DEFAULT_BRANCH=steered` against a run-created
`refs/remotes/origin/steered`: the driver correctly refuses,
`UNATTENDED check 22 FAILED — the resolved default-branch ref is not the one refs/remotes/origin/HEAD
names`. Arm B — add one local command, `git symbolic-ref refs/remotes/origin/HEAD
refs/remotes/origin/steered` (rc=0, no remote contacted): the same invocation printed
`unattended: preflight OK — base <run commit>` over the forged mandate, and committing that state
gave GATE EXIT=0, because check-unattended.sh:181 derives its "independent" default branch from the
very same run-writable symref.

The `fail 22` cross-check — the entire D3 fix — is therefore a second read of one run-writable input,
which is precisely the failure mode the comment at :177-179 says it removes. **Not a duplicate of
B1:** this is the symref that *names* the anchor, not the anchor ref itself, and a fix that hardens
only the anchor leaves the ref-selection steer standing.

**Fix.** Drop `refs/remotes/origin/HEAD` as the trust root. Derive the default branch from the remote
(`git ls-remote --symref origin HEAD`) and cache nothing, or require the operator to supply it
out-of-band and verify the resulting ref's tip against `git ls-remote origin`. Keep `fail 22`, but
make `canon` come from the network answer, and refuse when that answer is unavailable.

**Left-shift gate.** Extend the B1 red arm into a pair: for **every** ref or symref the kit treats as
a trust root, a test that writes it locally and asserts the leg reds. A cheap mechanical version — a
grep gate that bans `refs/remotes/` as an argument to `symbolic-ref`/`rev-parse` inside
`tools/unattended/**` unless the same function also calls `git ls-remote` — would have flagged both
B1 and H1 at authoring time.

---

### H2 — [high] Check 9 runs on terminal run-state files, so the first landing reds main permanently
`tools/unattended/check-unattended.sh:202` (loop at :126; the phase is already in scope as `ph` at
:128) · id 6

The loop applies checks 5/6/8/9/13/11 to every tracked `<memory_root>/builds/*/RUN.md`. A terminal
phase only decrements the check-7 `nlive` counter at :138 — it is never skipped — so check 9's
merge-base assertions run on a LANDED file.

**Reproduced.** Preflight a run, set `phase: LANDED`, merge the unit branch into main and push, then
run the leg on main: it prints **both** `check 9 FAILED — a recorded BASE is not the merge-base this
history reproduces … recorded 43fbc355, computed 48ec6909` and `check 9 FAILED — the merge-base
equals HEAD`, rc=1. One further commit on main still reds on the first assertion. Pre-merge control
on the unit branch was rc=0, so the landing causes the red.

Nothing clears it. Neither the driver nor the protocol deletes or archives a terminal RUN.md —
`memory/guides/UNATTENDED-PROTOCOL.md:104` explicitly caps only the **non-terminal** count, so
terminal run-state files persist by design — and `check-unattended.sh` is the "unattended kit gate"
leg in `tools/gate-legs.json`, which `.githooks/pre-push` runs on every default-branch push. The two
assertions predate the rewrite, but this hunk is where they now live and is the last point they can
be scoped.

**Fix.** Read the phase before check 9 and skip the merge-base reproduction when it is in
`PHASES_TERMINAL` — the pin polices a **live** run's provenance, and after landing the branch point
is gone by construction. If a terminal record must still be checked, assert reachability
(`git merge-base --is-ancestor "$rb" HEAD`) rather than equality with a freshly recomputed merge-base.

**Left-shift gate.** A "landing lifecycle" arm in `check-unattended.test.sh`: preflight → close →
merge to the fixture's main → push → run the leg on main, assert **green**. Every gate that reads a
persistent record needs one arm proving the record is still legal after the event it records.
Absent that, add `drift-audit`-style liveness: a signal that reds if a terminal RUN.md is older than
N commits and still tracked.

---

### H3 — [high] `out=$(cat "$T"; printf X) || return 1` is a branch no input can take — in five renderers
`tools/unattended/adopt-unattended.sh:97` · `tools/drift-audit/adopt-drift-audit.sh:118` ·
`tools/memory-recall/adopt-memory-recall.sh:129` · `tools/memory-tree/adopt-memory-tree.sh:70` ·
`tools/memory-tree/kit-dogfood-parity.test.sh:64` · ids 14, 4, 8, 11

A command substitution's exit status is that of the **last** command in the list — `printf X`, always
0. Verified on this environment's bash 5.3.9: `out=$(cat /nonexistent 2>/dev/null; printf X) || echo
FIRED` prints nothing and leaves `out=[X]`. So `|| return 1` never fires, `${out%X}` yields the empty
string, and `render` returns 0 on an unreadable template. `git diff 7f614a1 -- adopt-unattended.sh`
confirms the same hunk deleted `set -o pipefail 2>/dev/null || true` from the old sed render, where a
failing sed **did** make `render` return non-zero; the header comment at :78-81 still credits pipefail
for a property the file no longer has.

Consequences, worst first:
- `tools/memory-tree/adopt-memory-tree.sh` has **no** emptiness guard: `render_doc … > "$M/HYGIENE.md"`
  (and `TEMPLATE-SPEC.md`, `guides/BUILD-METHOD.md`) would scaffold an adopter's committed rule-set
  documents as empty files while the script continues under `set -eu`.
- `tools/drift-audit/adopt-drift-audit.sh:153` does `render > "$SKILL_OUT"` with no temp file and no
  `[ -s ]`, writes a zero-byte SKILL.md, prints "rendered"; its `--check` at :129 then diffs empty
  against empty and reports "in sync (skill rendered from template, project layer present)" — the
  green-by-absence shape the unattended kit added `[ -s ]` specifically to refuse.
- In `adopt-unattended.sh` the two refusals **this diff wrote** at :115 and :136 ("the render FAILED —
  the template could not be read") are unreachable strings; the case is caught only by the `[ -s ]`
  guards at :116/:139, under a different message.

Reachability is narrow — `[ -f "$TEMPLATE" ]` already catches missing and directory cases, leaving
permission bits, TOCTOU deletion and I/O errors — which is the argument for a lower rating. It is
rated high anyway because of `adopt-memory-tree.sh`'s unguarded writes into an adopter's committed
docs, and because this repo's `check-arms.py` meta-gate exists to ban exactly this shape.

**Fix.** Make the read's status survive the sentinel, in all five copies:
`out=$( cat "$TEMPLATE" || exit 1; printf X ) || return 1` (the subshell's `exit 1` propagates), or
gate with `[ -r "$TEMPLATE" ] || return 1` first. Then give `adopt-drift-audit.sh`'s write path and
`adopt-memory-tree.sh`'s three `render_doc >` writes the write-through-temp + `[ -s ]` refusal
`adopt-unattended.sh:138` already has, and correct the `adopt-unattended.sh:78-81` comment to name
the emptiness refusal alone.

**Left-shift gate.** Two, and both are cheap. (a) Teach `tools/memory-tree/check-arms.py` — or a new
shell-lint leg — to flag `$(…; …) ||` where the substitution's last command is a builtin that cannot
fail; it is a purely syntactic pattern. (b) An adopter-effect arm per renderer: `chmod 000` the
template (or point it at an unreadable path) and assert the adopter **refuses** and leaves the
installed file byte-identical. Review -1 already recorded that `tools/memory-tree/` has no adopter
e2e; this finding is the second bill for that.

---

### M1 — [medium] The driver silently accepts an **absent** `base:` / `base-ref:`, contradicting its own comment
`tools/unattended/unattended.sh:206` (and `:199` for `base:`; header comment at `:154`, comment at
`:203-204`) · ids 3, 10

Both guards read `[ -n "$rec" ] && [ "$rec" != … ]`, so an absent line short-circuits to no refusal —
while the comment two lines above says "An absent one is the violation, not the exemption" and the
header at :154 says "a mismatch or an absence is a refusal." The code and its own comment disagree.

**Verified by execution.** On a fixture with an honest anchor and a genuinely owner-committed mandate,
a **wrong** `base:` refuses (`UNATTENDED check 18 FAILED … recorded BOGUSVALUE, derived bac69036`);
after **deleting** the `base:` and `base-ref:` lines from the run-writable file, `--close` printed
`unattended: close OK — every declared DoD item met; phase LANDING` and exited 0, while the separate
gate leg on the identical tree refused (`check 9 FAILED — a run-state file records no BASE`).

`dod_met`'s `mandate-reachable` item (:475) routes through `trusted_base`, so the driver greens on a
run-state file whose pin was deleted and the refusal is deferred from the verb that is supposed to
block to the bar. That leg reaches a run only through the project-declared `GATE_CMD`, so an adopter
whose `GATE_CMD` omits `check-unattended.sh` has **no** BASE-pin enforcement at all — the exact
regression `check-unattended.sh:171-172` documents as already fixed on its own side ("deleting one
line from a run-writable file disarmed the only BASE check on the bar").

Two honest limits on the severity, neither overturning it: `TB` remains the freshly derived base, so
the mandate comparison itself is not defeated by the absence; and at first `--preflight` the driver
writes `base-ref` itself (:368), so absence there is legitimate. The defect is a stated-but-unenforced
invariant plus a comment that will mislead the next maintainer of this authorization path — not an
authorization bypass.

**Fix.** Either make the code match the comment — `if [ -z "$rec" ]; then fail 22 "the run-state file
records no base-ref, and the record is written by the run — an absent pin is not a satisfied one";
elif [ "$rec" != "$RESOLVED_REF" ]; then …` (and the same for `base:` against `$fresh`) — with the
first-preflight case handled explicitly, or rewrite both comments to say the driver derives fresh and
leaves absence to the gate leg. Do not leave the two disagreeing.

**Left-shift gate.** Two red arms in `unattended.test.sh`: delete `base:`, delete `base-ref:`, assert
`--close` refuses. Today's arms only cover a **forged** value, never a deleted one — which is why the
gap survived a leg that looks like it covers the field. Generalize: for every guard of the form
`[ -n "$x" ] && [ "$x" != … ]` in an authorization path, the harness needs both an
absent arm and a wrong arm.

---

### M2 — [medium] `fail 22`'s third argument is computed, passed and discarded
`tools/unattended/unattended.sh:194` and `:207` (definition at `:42`) · ids 9, 15

`fail() { echo "UNATTENDED check $1 FAILED — $2"; status=1; }` reads only `$1` and `$2`; `$3` is never
referenced and there is no second definition. A repo-wide grep finds exactly two three-argument call
sites, both added by this build, both `fail 22`, whose third argument (`resolved $RESOLVED_REF,
canonical $canon` / `recorded $rec, resolved $RESOLVED_REF`) is silently dropped.

Both are reachable: :194 fires on exactly the `GOV_DEFAULT_BRANCH` steer the check exists to catch,
:207 on a forged `base-ref` (driven at `unattended.test.sh:176`). So an operator hitting the newest
authorization refusal sees a bare sentence with **no values** and cannot tell which ref resolved
versus which `refs/remotes/origin/HEAD` names. The file's own convention is the opposite — `fail 18`
at :200 inlines `recorded $rec, derived $fresh` into `$2`, and the `check_slug` comment at :218-222
states the value-trails-the-sentence rule explicitly.

**Fix.** Fold the values into `$2`:
`fail 22 "the resolved default-branch ref is not the one refs/remotes/origin/HEAD names: resolved
$RESOLVED_REF, canonical $canon"`, and likewise at :207.

**Left-shift gate.** The tests are complicit: `unattended.test.sh:178` asserts only the `$2` prefix, so
the drop is invisible. Extend both arms to assert the **value** substring. Mechanically: a lint leg
that flags any call to a fixed-arity shell helper with more arguments than the definition reads —
this is a two-line `grep` over the `fail`/`warn` helpers in `tools/**` and would have caught it before
review.

---

### L1 — [low] The map dossier still describes a five-fact authored region under the old belonging rule
`memory/map/features/unattended.md:50` · ids 13, 18

The dossier reads "the authored region holds only the five facts nothing in the tree derives." This
diff falsified both halves: `PROTOCOL.template.md:45` and `memory/guides/UNATTENDED-PROTOCOL.md:45`
now read "exactly six facts and nothing else" with an enumerated item 6 (`base-ref`), and §2 amended
the belonging test to "either nothing in the tree derives a fact, **or** it is recorded SO THAT a
second party can re-derive it." `git diff 7f614a1 -- memory/map/features/unattended.md` is **empty** —
the dossier was never touched. Under the dossier's stated test, fact 6 would be excluded, when it
exists precisely so the gate re-derives it.

The dossier is what a session is pointed at to learn this kit. `test_codebase_map.py` only checks that
a dossier **claims** the key and byte-compares generated artifacts — it never reads this prose, so
nothing reds.

**Fix.** Rewrite the sentence to six facts and to the amended two-part test, naming `base-ref` as the
instance. Records under `memory/builds/` are historical and stay as written.

**Left-shift gate.** The coverage gate proves a dossier *exists*; nothing proves it is *current*. Add a
freshness signal to `drift-audit` — a dossier whose claimed keys' source files moved since the
dossier's own last commit is stale — or, cheaper and exact for this class, a
`test_codebase_map.py` assertion that any numeral-carrying claim about a protocol section
("five facts") matches the protocol file it cites.

---

### L2 — [low] The driver's own comment still cites the five-fact protocol it now violates
`tools/unattended/unattended.sh:418` · id 17

`verb_resume`'s comment reads "the authored region carries five facts and never restates a derivable
one (protocol section 2)" while the same file writes the **sixth** fact at :368 via `set_fact
base-ref`, and the protocol moved to six on this branch (`5d1faf9`). A reader auditing whether the
driver honours the authored-region contract is told to expect five. No gate covers it:
`check-unattended.sh:247-248` compares the shipped template to the installed doc only, and nothing
reads the driver's comment text.

**Fix.** Update to "six facts", or better, drop the count and cite the section only ("the authored
region never restates a derivable one — protocol section 2") so the number lives in exactly one place.

**Left-shift gate.** Same gate as L1, and the same principle applies to both: prose that restates a
number defined elsewhere is a parity pair with no leg. Either a grep gate that pins the phrase
`\b(five|six|seven) facts\b` across `tools/unattended/**` + `memory/guides/UNATTENDED-PROTOCOL.md` +
`memory/map/features/unattended.md` to one value, or the standing rule: never spell the count outside
the protocol.

---

## 4. Fix order

1. **B1** — the anchor. Nothing else in the kit means anything until the BASE cannot be chosen by the
   run. Ships with its own red arm.
2. **H1** — the symref, in the same change. Fixing one without the other leaves the steer standing,
   and both fixes are the same shape: derive from `git ls-remote`, refuse on no answer.
3. **H2** — the terminal-phase skip. This one blocks the *first successful landing*, so it must land
   before any unattended run does.
4. **H3** — the five dead read guards plus the two missing emptiness refusals. Mechanical, and the
   lint leg that finds them is a grep.
5. **M1, M2** — the driver's absent-pin guard and the dropped diagnostics; both need their test arms
   extended, not just the code fixed.
6. **L1, L2** — the two stale five-fact claims, in one commit with the pin gate.
7. **B2** — verify the drain, not the pin. `non_terminal_specs_cited_by_product_source` sits at 2 of a
   pin of 2 with zero headroom; close spec-2 and spec-6 when their source lands rather than relying on
   citation removal.

## 5. What the gates could not see

Of nine distinct defects, **one** (B2) reddened the bar, and it was the only one that touched a
counted record rather than an authorization property. The other eight are all in the same blind spot:
**the kit gates its own bookkeeping and never the thing the bookkeeping is about.** Three trust roots
were introduced or reinforced by this diff and all three are locally writable; the harness tests every
one of them by forging a *value* and never by moving the *ref*. The single highest-leverage arm this
kit is missing is the adversarial one — a test that plays the run trying to authorize itself, with
`git update-ref`, `git symbolic-ref` and line deletion in its toolkit — because every blocker and high
above falls out of it.
