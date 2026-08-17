## Verdict: BLOCKED — one blocker reds the merge bar at HEAD

**Tier-2 code review · cBriefedPilot · 2026-08-16 · node c · target: the cumulative diff landing on
`main` (`709d260..c32161b`, 22 units)**

**Review shape:** raw 32 · confirmed 31 · refuted 1 · unverified 0 · **precision 0.97**.
After deduplication (multiple hunters independently landed on the same defect — the RUN.md staleness
was raised three times, the dead-arm block three times, two of the broken mutation arms three times
each) the 31 confirmed findings collapse to **16 distinct defects**: 1 blocker, 4 high, 7 medium,
4 low. Every finding below survived an adversarial skeptic pass; nothing is carried as unverified.

**The one thing that must happen before this lands:** `bash tools/unattended/check-unattended.sh`
exits 1 at HEAD. That leg carries no `guard` in `tools/gate-legs.json`, so it runs on every bar
invocation including the authoritative `.githooks/pre-push` run. The push is blocked by the kit this
build shipped.

**The shape of the rest.** The high band is one story told four ways: check 16 — the registry↔table
join that the whole pointer-not-copy design rests on — landed with nine arms that cannot run, and
three of those nine additionally cannot produce the state they assert. The meta-gate
(`check-arms.py`) certified all nine as armed because it text-matches assertion strings and cannot
see reachability. That is the single most valuable left-shift in this report: **an arm that is never
executed is indistinguishable, to every gate this repo owns, from an arm that passes.**

---

## 1 · BLOCKER · `memory/builds/cBriefedPilot/RUN.md:7` — the run-state file's copied generated region is two ids stale, and leg check 8 reds

**Claim.** `RUN.md`'s `<!-- run:generated -->` region is a COPY of the build README's
`<!-- gen:build-index -->` slice. The README now carries ids through `TOOL-cBriefedPilot-29`;
the copy stops at `-27`.

**Evidence.** Reproduced at HEAD:

```
UNATTENDED check 8 FAILED — a run-state file's generated region differs from the build README
slice it is a COPY of; re-run the driver rather than hand-editing it:
memory/builds/cBriefedPilot/RUN.md
```

`RUN.md:7` ends its `ids` list at `-27` and says "22 unit(s)"; `README.md:7` runs to `-29`. The
manifest entry `{"name":"unattended kit gate","argv":["bash","tools/unattended/check-unattended.sh"]}`
in `tools/gate-legs.json` carries **no `guard` key** (its three siblings do), so it runs on every bar
invocation. The last re-splice was `50491c2` (after unit 18); units 19 and 20 moved the README's
`ids:` line afterwards with no re-splice.

**Impact.** `.githooks/pre-push` runs the full bar on a default-branch push and blocks a red one, so
this diff cannot land as-is. It is also exactly the drift the `records-current` DoD item checks, so
`--close` blocks on it too. The diff created the divergence itself: it adds `-28`/`-29` to the
README's generated region and commits a `RUN.md` whose copy predates them.

**Fix.** Re-derive the copy, do not hand-edit it. On a clean tree:

```
bash tools/unattended/unattended.sh --preflight cBriefedPilot --keepalive-id ad706085
```

which re-splices the region from the README, then commit `RUN.md` and confirm
`bash tools/unattended/check-unattended.sh` exits 0.

**Left-shift gate.** The root cause is two writers for one fact with only one re-splicer, and that
re-splicer refuses a dirty tree — so the copy strands whenever the README moves mid-run (recorded as
`TOOL-cBriefedPilot-25`). The lazy structural fix is to make `gen_build_index.py` re-splice every
live `RUN.md` region whenever it regenerates a README: one writer, and the copy cannot lag its
source. Failing that, extend `.githooks/pre-commit` with a diff-scoped check-8-only leg that fires
when a `memory/builds/*/README.md` is staged — so the drift is caught at the commit that causes it,
not at the push three units later.

---

## 2 · HIGH · `tools/unattended/check-unattended.test.sh:553` — the nine check-16 arms sit after `exit "$st"` and never execute

**Claim.** Lines 555-606 (nine arms plus the closing green control) follow an unconditional
top-level `exit "$st"` on line 553. Not one of them runs.

**Evidence.** The file is 606 lines; line 552 is
`[ "$st" = 0 ] && echo "PASS ($n assertions)"`, line 553 is `exit "$st"`, and the entire check-16
block follows. Ran the suite: it prints `PASS (86 assertions)` — none of the ten new assertions is
counted. Commit `2039507` raised `.memory-tree.conf`'s `ARMS_FLOORS` for
`tools/unattended/check-unattended.sh` from `39:39` to `48:48` in the same commit, and
`python tools/memory-tree/check-arms.py` exits 0 today.

**Impact.** Check 16 is the join binding the driver's `DIRECTIVES_CORE` registry to the Skill table
an agent actually reads — the mechanism the whole design rests on — and it ships with zero executed
proof. Both gates that should notice stay green: `check-arms.py` because it text-matches assertion
strings that exist in the file, the suite because it never reaches them. Spec 12's S8 ("every
refusal above gets a RED arm beside the green control") is unmet, and `memory/backlog/TOOL.md:46`
nonetheless marks `TOOL-cBriefedPilot-12` CLOSED. This is a permanent, silent weakening of the arms
pin, and it is what hides findings 3, 4 and 5 below.

**Fix.** Move lines 555-606 to immediately before line 552, so the summary and `exit "$st"` stay
last. Re-run the suite, confirm the assertion count rises from 86 to 96, then fix what the now-live
arms report (findings 3, 4 and 5 — three of the nine red immediately).

**Left-shift gate.** `check-arms.py` counts arms it cannot run. Make the count executable: have each
`*.test.sh` print `PASS (<n> assertions)` — most already do — and pin a shrink-only per-file
assertion floor beside the existing `ARMS_FLOORS`. Ten assertions added and zero executed then reds
on the floor, without any new harness. `TOOL-cBriefedPilot-27` records the reachability hole and
proposes a gate; it is the right follow-up, but the dead code was left in place, so the defect ships
in this diff regardless.

---

## 3 · HIGH · `tools/unattended/check-unattended.test.sh:567` — arm 2's mutation is anchored at column 0 and strips nothing

**Claim.** Arm 2 deletes the Skill template's directive rows with `grep -v '^| \`[a-z]'`, but every
directive row in `tools/unattended/SKILL.template.md` is indented three spaces.

**Evidence.** `grep -c '^| \`[a-z]' tools/unattended/SKILL.template.md` returns 0;
`grep -c '^   | \`[a-z]'` returns 11. Ran the fixture line byte-for-byte against a copy of the kit:
11 rows before, 11 after — the template is byte-identical, `grep -v` still exits 0 so the `&& mv`
runs, and the leg's own extractor (`sed -n 's/^[[:space:]]*|[[:space:]]*\`…'`,
`check-unattended.sh:431`) still returns all 11 handles.

**Impact.** The arm whose own comment calls it "the arm that matters most — without it the join
passes by finding nothing" itself passes by finding nothing. The `[ -z "$tbl" ]` refusal at
`check-unattended.sh:444` is unproven. Verified by relocating the block and running it:
`FAIL missing: the Skill template carries no directive table row this leg can read`.

**Fix.** Match the leg's own row shape, with optional leading whitespace:

```
grep -vE '^[[:space:]]*\| `[a-z]' tools/unattended/SKILL.template.md > t.md \
  && mv t.md tools/unattended/SKILL.template.md
```

**Left-shift gate.** See the shared gate under finding 5 — one helper closes findings 3, 4 and 5.

---

## 4 · HIGH · `tools/unattended/check-unattended.test.sh:571` — arm 3 injects `M2` into a prose cell, which the leg's awk does not count

**Claim.** Arm 3 mutates a row to
`   | \`minimal-prose\` | the transcript rule under a mandate M2 | M10 | D1 |`. The leg's awk
(`check-unattended.sh:432-442`) only increments the carrier count when a **trimmed cell** matches
`^M[0-9]+$`.

**Evidence.** Ran the leg's exact awk over the mutated template: `n` stays 1, output is
`minimal-prose:M10`, AMBIGUOUS count 0.

**Impact.** The `*":AMBIGUOUS"*` branch at `check-unattended.sh:446` — the guard against a directive
row citing two build-method sections — ships with no working arm. Confirmed by execution once
reachable: `FAIL missing: a directive row cites more than one build-method section`. The arm's
comment also misdescribes the check: an `M<n>` mentioned inside prose is not detected at all, by
design.

**Fix.** Mutate a whole cell:

```
sed -i 's/| `minimal-prose` \(.*\)| M10 | D1 |/| `minimal-prose` \1| M10 | M2 |/' \
  tools/unattended/SKILL.template.md
```

**Left-shift gate.** See finding 5.

---

## 5 · HIGH · `tools/unattended/check-unattended.test.sh:585` — arm 6's fixture contains every section the registry cites, so arm B cannot fail

**Claim.** `DIRECTIVES_CORE` (`unattended.sh:90`) cites exactly `{M2,M3,M4,M5,M6,M8,M9,M10}`. Arm 6's
stub build method writes headings for all eight.

**Evidence.** Replayed arm B's own loop
(`for pair in $core; sec=${pair#*:}; grep -qE "^## $sec( |$)"`, `check-unattended.sh:461-465`)
against that exact fixture with the real registry: zero unresolved pairs. Only `M7` and `M1`/`M11`
are omitted, and no directive cites them.

**Impact.** Arm B is the only thing proving a directive handle resolves to a real build-method rule —
the pointer half of the pointer-not-copy design — and its single arm is armed by a fixture that
satisfies it. Confirmed once reachable:
`FAIL missing: a directive points at a build-method section that does not exist`.

**Fix.** Drop one cited section from the `printf`, e.g. omit `## M9` so `wrap-up-derived:M9` fails to
resolve:

```
printf '# method\n\n## M2\n\n## M3\n\n## M4\n\n## M5\n\n## M6\n\n## M8\n\n## M10\n'
```

**Left-shift gate (covers findings 3, 4 and 5).** Every one of these three is the same failure: a
mutation arm that does not mutate. Add one helper to the test harness and use it in every arm —
snapshot the fixture, apply the mutation, and `cmp -s` before/after; if the bytes are unchanged, the
arm fails *as an arm*, before the leg is ever invoked. For fixtures built by `printf` rather than
mutated (arm 6), the equivalent assertion is that the leg's own predicate over the fixture returns
the state the arm claims — i.e. the arm asserts the fixture is broken before asserting the leg
notices. That helper is ~5 lines and would have caught three of this diff's four high findings at
the moment they were written.

---

## 6 · MEDIUM · `tools/unattended/check-unattended.sh:460` — `core` is unbound under `set -u` when the table is empty

**Claim.** `core` is assigned only inside the `else` of `if [ -z "$tbl" ]` (line 450), but arm B's
`for pair in $core` at line 460 runs unconditionally. `set -u` is on (line 16).

**Evidence.** Reproduced on a scratch copy with the indented table rows genuinely stripped:

```
UNATTENDED check 16 FAILED — the Skill template carries no directive table row…
tools/unattended/check-unattended.sh: line 460: core: unbound variable
```

`grep` for `core=` returns exactly one hit in the file.

**Impact.** A broken adopter template does not merely red check 16 — the leg dies mid-run, skipping
the rest of arm B, **all of arm C (the `DIRECTIVES_FLOOR` shrink-only pin, lines 469-478)**, and the
final `exit "$status"`. The operator sees a bash internal error where a named refusal belongs, and
the floor check is silently disabled in exactly the state it most needs to run.

**Fix.** Initialise `core=""` before the `if [ -z "$tbl" ]` branch, so arms B and C both run whatever
arm A found.

**Left-shift gate.** `shellcheck` flags this class (SC2154 / conditionally-assigned reads) and the
kit's shell surface is small. Add a `shellcheck -S warning tools/unattended/*.sh` leg — or, if a new
dependency is unwanted, note that arm 2 (finding 3) *would* have caught it the moment its mutation
actually mutated. Two independent gates, both already nearly in place.

---

## 7 · MEDIUM · `tools/unattended/unattended.sh:484` — `case "$r" in *"$BYPASS_BAN"*)` is never-false when the key is undeclared

**Claim.** With `BYPASS_BAN` empty the pattern degenerates to `**`, which matches every string.
The three sibling call sites all guard with `[ -n "$BYPASS_BAN" ]`; this one does not.

**Evidence.** Verified in bash: `r=hello; B=""; case "$r" in *"$B"*) echo MATCHED;; esac` prints
MATCHED. `unattended.sh:60` defaults `BYPASS_BAN=""` and the driver validates no conf key except
`WIRING_CHECK` (line 418) — the non-empty requirement lives only in the leg's check 1
(`check-unattended.sh:53-56`). The siblings at `unattended.sh:921`, `unattended.sh:1181` and
`check-unattended.sh:360` all carry the guard, and review `cFinalBerth-2:237` explicitly prescribed
it, so the unguarded form is the outlier, not a design choice.

**Impact.** On a project whose `.unattended.conf` omits the key, **every** `--waive … --reason <text>`
is refused with check 41 naming a bypass flag nobody declared, and the newline branch at line 488 is
dead. The waiver feature is unusable rather than unrestricted, and the operator is shown a false
accusation instead of the real misconfiguration. Bounded by the fact that such a conf already reds
leg check 1 — but the guard is objectively never-false.

**Fix.** Guard it as its siblings do:

```sh
if [ -n "$BYPASS_BAN" ]; then
  case "$r" in *"$BYPASS_BAN"*) fail 41 …; return 1 ;; esac
fi
```

Better: hoist the shared refusal into one helper that both `check_waivers` and `verb_abort` call —
four spellings of one rule is how one of them ends up wrong.

**Left-shift gate.** The driver has no required-key validation of its own; the leg has the list.
Move (or mirror) that loop into the driver's startup so a conf missing a required key refuses at the
first verb, on the operator's machine, instead of producing a nonsense refusal that only the bar can
diagnose.

---

## 8 · MEDIUM · `tools/unattended/unattended.sh:467` — `recorded_waivers`' greedy `^.*` lets a crafted reason forge the recorded handle

**Claim.** The parse is `sed -n 's/^.* waiver · item \([^ ]*\) · reason .*$/\1/p'`. The greedy `^.*`
backtracks to the **last** occurrence of the grammar, so a reason containing the literal
` waiver · item <X> · reason ` makes the readback report `X` instead of the handle `park()` wrote.
Refusal 41 bans the forgery across a newline but not inline on one line.

**Evidence.** Fed a line `park()` would write —
`<ts> waiver · item minimal-prose · reason owner said see waiver · item sub-specced · reason x for context` —
and `recorded_waivers` returns `sub-specced`. `check_waivers` (lines 469-492) refuses only an
undeclared handle, an empty reason, a reason spelling `BYPASS_BAN`, and a newline; the inline grammar
passes all four. `park()` writes the reason verbatim (line 1197) and the reason is owner-supplied
free text the code's own comments name as an injection surface.

**Impact.** The misread `have` feeds refusal 38's `want != have` comparison (lines 497-510), so a
later `--preflight <slug> --waive sub-specced --reason x` compares equal and is **accepted** — at the
verb §10 calls "provably the LAST owner turn". Symmetrically, a legitimate re-issue of the recorded
set is now wrongly refused. The parked record also reads, to a human and to M9's wrap-up derivation,
as two granted waivers where the owner granted one. This is not the §9 uid boundary: no file editing
is involved — the driver writes and then misreads its own well-formed record.

**Fix.** Anchor the parse to `park()`'s own grammar so only the leading timestamp field may precede
the kind:

```sh
sed -n 's/^[^ ]* waiver · item \([^ ]*\) · reason .*$/\1/p'
```

and extend refusal 41's `case "$r" in` to refuse a reason containing ` · item ` (or ` waiver · item `)
for the same reason the newline is refused.

**Left-shift gate.** Add a round-trip property arm beside the existing waiver arms: park a waiver
whose reason embeds the record grammar, then assert `recorded_waivers` returns the handle that was
written. Any writer/reader pair over an owner-supplied free-text field earns exactly one such arm —
it is the cheapest thing that distinguishes "parses" from "parses what we wrote".

---

## 9 · MEDIUM · `tools/unattended/unattended.sh:725` — `spec_ids` and `verb_plan` disagree about an unparseable heading

**Claim.** `spec_ids` (725-731) prints only when **both** a status header and a parsed id exist;
`verb_plan` (777-778) falls back to `basename "$spec" .md` when the same awk yields nothing, and only
skips the file when the STATUS header is missing. The comment at 722-724 claims such a spec is
"invisible to both halves in the same way".

**Evidence.** A spec with a status header and a heading the regex rejects — `# TOOL-x-1: Title` (the
class `[A-Za-z0-9-]*` cannot cross the colon) or `# TOOL-x-1` with no trailing space — is listed
under its basename by `verb_plan` and simultaneously counted absent by `missing_units`. Scanned all
103 tracked specs with both awk programs: **zero divergent files today**, so this is latent, not
live — and no gate enforces the heading grammar that keeps it latent.

**Impact.** Such a spec is printed twice by `--plan`: once under its basename with its real status,
once as a phantom `MISSING` row for the roster id. With every earlier spec terminal that phantom
becomes `next: <id> (MISSING - spec it first)`, which under an unattended run sends the agent to
re-spec a unit that already has one.

**Fix.** Single-source the extraction: give `spec_ids` the same basename fallback the listing uses,
or — smaller — drop the fallback in `verb_plan` so both halves are blind in the same way, which is
what the comment already claims happens.

**Left-shift gate.** Two parsers over one grammar is the defect; the gate is to have one. Where that
is not done, add a hygiene assertion that every tracked spec's `# <id> ` heading parses under the
driver's exact regex — three lines beside the existing spec-header checks, and it makes the latency
explicit instead of accidental.

---

## 10 · MEDIUM · `memory/backlog/TOOL.md:49` — `TOOL-cBriefedPilot-15` is CLOSED on a body that asserts a rule which did not ship

**Claim.** The row reads
`TOOL-cBriefedPilot-15 · CLOSED · M6 inverts under a mandate: disjoint passes are owed concurrency…`.
The diff flips only the status token; the body is byte-identical to the row as raised. M6 did not
change.

**Evidence.** `git diff 709d260...HEAD -- memory/guides/BUILD-METHOD.md` has hunks at lines 192, 205,
215 and 224 only; the `^## M` heading map puts M6 at 125-155, so those hunks land in M8, M9 and M10 —
M6 is byte-untouched. Spec 15 rev-2 (line 182) records that branch B was taken and "M6 is UNCHANGED",
and `memory/builds/cBriefedPilot/README.md:122` says so in bold. Six sibling rows in this same diff
(`aStandingWrit-3`, `cFinalBerth-3`, `-7`, `-8`, `-20`, `-22`) were rewritten to their outcome on
close; this row is the outlier.

**Impact.** The durable, searchable index a future session greps now asserts a build-method rule
exists that does not. Spec 15 §9 rev-2 states its whole point is that the record must not describe a
rule that did not ship — the README was corrected, the backlog row was not.

**Fix.** Rewrite the body to the shipped outcome, e.g.
`TOOL-cBriefedPilot-15 · CLOSED · branch B on unit 21's token: M6 is UNCHANGED and the unit ships the finding that the inversion has no mechanism`.

**Left-shift gate.** Mechanical and cheap, given the row-keyed merge driver already parses these
files by key: a hygiene check on `memory/backlog/*.md` diffs asserting that a row whose status token
flips to CLOSED also has a **body delta** in the same commit. It cannot verify the body is *true*,
but it makes "closed without rewriting the claim" impossible to do silently — which is the whole
failure here.

---

## 11 · MEDIUM · `tools/unattended/check-unattended.sh:49` — `DIRECTIVES_EXTRA` is defaulted and sourced but never composed into an effective set

**Claim.** Lines 83-84 compose `PHASES="$PHASES_CORE $PHASES_EXTRA"` and `DOD="$DOD_CORE $DOD_EXTRA"`.
There is no equivalent for directives: check 16 builds `core` from `DIRECTIVES_CORE` alone (line 450)
and arm B iterates that same `core` (line 460).

**Evidence.** `grep` shows `DIRECTIVES_EXTRA` is defaulted at line 49, sourced at 51, and never read
again. The **driver** composes properly — `directives()` (`unattended.sh:97`) includes EXTRA and
`--waive`'s membership test at line 474 reads `$(directives)` — so an EXTRA handle is waivable. The
driver's only carrier check (`check_method`, line 455) asserts the FILE exists and never resolves an
`M<n>`.

**Impact.** A project can declare `foo:M99`; the agent is never shown it (nothing joins it to the
Skill table), `--waive foo` succeeds, and the pointer resolves to nothing — the exact state unit 4's
check 34 exists to prevent, reached through the extension point instead. Worse: the join is
bidirectional, so if the project **does** add its extra row to the Skill table, check 16 reds with
"the Skill's table names a directive the registry does not declare". The project is pushed into the
state where the agent is never shown the handle.

**Fix.** Compose the effective set the way the sibling keys do —
`DIRECTIVES="$DIRECTIVES_CORE $DIRECTIVES_EXTRA"` — and run arm B (section resolution) over it,
keeping arm A's registry↔table join and arm C's floor scoped to the core set.

**Left-shift gate.** A four-line canary in `check-unattended.test.sh` (or the run-gates canary):
every `*_EXTRA` key defaulted in `check-unattended.sh` must appear in a composition line. Three keys
exist and one was missed — the population is small enough that a grep is the whole gate.

---

## 12 · MEDIUM · `tools/unattended/unattended.sh:762` — `fail 19`'s message states a fact about the code that stopped being true at unit 6

**Claim.** The refusal says the roster "is the README's authored Units table, which it does not
parse". Unit 6 added `roster_ids()`/`missing_units()` (714-733), which parse exactly that region. The
branch also fires on `[ -z "$specs" ]` **before** the `missing_units` loop at line 787.

**Evidence.** The test's own comment at `unattended.test.sh:858` says "did not parse" in the past
tense while the live message says it in the present. The malformed-roster refusal at line 755 runs
earlier, so this is not that path.

**Impact.** Two answers to one question: `PROTOCOL.template.md:210` and `SKILL.template.md:129` both
promise "a planned unit nobody has specced is reported as MISSING", while the driver refuses outright
and blames a parser it now has. The refused state — a well-formed roster and zero tracked specs — is
the state at the **start of every build**. A refusal message stating a false fact about the code is
the class unit 21 just filed against a binding document.

**Fix.** Report the roster ids as MISSING when `roster_ids` is non-empty, and fail 19 only when there
is neither a roster nor a spec. At minimum, drop the ", which it does not parse" clause.

**Left-shift gate.** Add the arm the promise implies: a fixture build with a well-formed roster and
zero specs must LIST each roster id as MISSING, not refuse. Any promise a binding document makes in
those words earns one arm — that arm is the join between the doc and the driver.

---

## 13 · LOW · `tools/unattended/PROTOCOL.template.md:250` — `## 10.` is inserted before `## 9.`, and the parity leg is blind to it

**Claim.** `grep -n '^## '` on both `tools/unattended/PROTOCOL.template.md` and
`memory/guides/UNATTENDED-PROTOCOL.md` returns identical lists ending 8 (225), **10 (250), 9 (281)**.
The pair is byte-identical, so check 12/15's parity comparison stays green on a misordered document.

**Evidence.** `diff` of the pair reports IDENTICAL. Live cross-references to §9 at lines 29, 45 and
82; to §10 at 20, 73 and 198. Not a deliberate stable-numbering trade-off: the unit's own spec,
`spec/2026-08-14-spec-cBriefedPilot-18.md:134`, specifies `| §10 | new, last, mechanism only |`.

**Impact.** §1 and §2 both send the reader to §9 for the boundary claim — the most load-bearing
caveat in the binding contract — and it now sits past a section numbered after it, in the one
document whose whole design argument is that a rule has exactly one findable home.

**Fix.** Move the `## 10.` block below `## 9.` in `tools/unattended/PROTOCOL.template.md` and re-copy
to `memory/guides/UNATTENDED-PROTOCOL.md`, keeping the byte-identity the parity leg checks.

**Left-shift gate.** Two lines beside the existing parity check: `grep -n '^## [0-9]'` and assert the
section numbers are ascending. Parity answers "are the two copies the same"; it never answered "is
either one coherent", and this is the cheapest way to ask the second question.

---

## 14 · LOW · `tools/unattended/SKILL.template.md:163` — the override paragraph describes an outcome the driver refuses

**Claim.** The paragraph tells the agent that supplying one `--override`/`--reason` pair for two
unmet items "leaves the second overridden on a reason written about the first, and the close records
that as a decision somebody made". With unit 1's paired accumulator, it does not.

**Evidence.** Traced `verb_close` (1107-1152): `--override` pushes an item with an empty reason and
sets `OV_PEND` (1237); `--reason` fills only the LAST pushed slot (1239). For
`--override A --override B --reason r`, A keeps an empty reason and the validation loop (1120-1134)
raises `fail 12` **before** the parking loop at 1150, so nothing is written. An item absent from
`OV_ITEMS` entirely makes `is_overridden` return 1, `dod_met` runs, and check 13 blocks the close.
`unattended.test.sh:554-555` already asserts exactly that refusal. The same stale sentence is in the
render at `.claude/skills/unattended/SKILL.md:163`.

**Impact.** The agent-facing Skill — whose only reader is the agent — describes the pre-accumulator
SCALAR behaviour, telling that reader that misuse silently records a wrong reason when the code this
very unit built refuses it. It over-warns rather than under-warns, hence LOW, but it is wrong about
the code.

**Fix.** Restate the shipped behaviour: a pair left without `--reason` is refused, and an item with no
pair at all simply blocks the close. Re-render with `bash tools/unattended/adopt-unattended.sh` so
template and render stay in sync.

**Left-shift gate.** Reuse the join this build just invented. Require every refusal the Skill
describes in prose to cite its check number, then add a check-16-shaped leg joining the check numbers
cited in `SKILL.template.md` to the `fail <n>` sites in `unattended.sh`. A paragraph describing a
refusal that no longer exists — or never did — then reds, exactly as an unjoined directive handle
does.

---

## 15 · LOW · `tools/check-kit-versions.sh:144` — the pre-existing `u=` pairing is fully subsumed by the new loop

**Claim.** Lines 110-124 derive `$uc` from `unattended.sh` and loop
`for s in tools/unattended/unattended.sh tools/unattended/check-unattended.sh`, asserting
`^KIT_UNATTENDED_VERSION=$uc([^0-9.]|$)`. Lines 144-147 recompute `$u` with the identical grep on the
identical file and assert the identical regex against the identical second file.

**Evidence.** On a half-bump, both line 117 and line 146 print — different wording — and each does
`fails=$((fails+1))`. On an unreadable constant, both line 112 and line 146 print.

**Impact.** Two implementations of one assertion: one defect, two messages, two increments, and a
future edit to one copy leaves the other saying something else. This is precisely the
second-implementation-is-not-a-second-opinion shape the new block's own comment argues against.

**Fix.** Delete lines 143-149 (the comment, the `u=` capture and its `if`). The new block already
covers both constants and both same-line markers.

**Left-shift gate.** A canary asserting each tracked kit dir appears exactly once across
`check-kit-versions.sh`'s assertion sites. The script's coverage list should be derived from
`tools/*`, the way the install-prefix gate already derives its kit-name alternation — a hand-maintained
second list is how the duplicate got there.

---

## 16 · LOW · `tools/unattended/check-unattended.sh:431` — `tbl` is a second row grammar that buys nothing, and its comment over-claims

**Claim.** The sed row filter for `tbl`
(`^[[:space:]]*|[[:space:]]*\`[a-z][a-z-]*\`[[:space:]]*|`) and the awk row filter for `tblpairs` are
the same regex in BRE vs ERE. Any row matching it necessarily has a trimmed cell 2 equal to
`` `handle` ``, so awk always prints `h:c` or `h:AMBIGUOUS` — `tbl` is non-empty exactly when
`tblpairs` is. `tbl` is read only by the `[ -z "$tbl" ]` test on line 444.

**Impact.** Dead plumbing, and two row grammars a future editor must keep in step. The adjacent
comment claiming "a table whose columns are reordered still joins" is false for the same reason:
both filters pin the handle to the row's FIRST cell, so a reorder that moves it degrades to an
`only_reg` refusal — loud, but not the claimed behaviour.

**Fix.** Drop the `tbl=` assignment, test `[ -z "$tblpairs" ]` on line 444, and correct the comment to
say the handle must be the row's first cell.

**Left-shift gate.** No new gate needed — the existing arm requirement is the gate, once it actually
runs (finding 2). A second parser that no arm can distinguish from the first is dead by definition:
if you cannot write an input where they disagree, delete one.

---

## What this pass did not audit

Only the unattended kit's shell surface, its two binding documents, the Skill template and its
render, `check-kit-versions.sh`, and the records this build leaves (`memory/backlog/TOOL.md`,
`memory/builds/cBriefedPilot/`). The 22 specs were audited as designs by
`2026-08-15-review-cBriefedPilot-1.md` and are not re-read here. No leg outside the unattended kit
was executed beyond `check-arms.py` and the unattended suites, and no claim is made about the rest of
the bar being green — only that **the unattended leg is red**, which is sufficient to block the push.

## The one recommendation above the individual fixes

Three of four high findings and one medium are the same root cause: **this repo's arms meta-gate
grades text, not execution.** `check-arms.py` certified nine branches as armed while the arms sat
past an `exit`, and three of those nine could not have produced their asserted state even if they
ran. Every other gate in the suite held. Pin a shrink-only per-file assertion-count floor beside the
existing `ARMS_FLOORS`, and add the five-line "did the mutation mutate" helper to the test harness.
Together they cost under twenty lines and would have caught four of this diff's five most serious
defects before the review existed — which is the only kind of gate worth adding.
