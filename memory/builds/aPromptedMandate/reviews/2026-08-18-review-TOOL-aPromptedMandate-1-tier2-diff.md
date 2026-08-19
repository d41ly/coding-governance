# aPromptedMandate — Tier-2 diff review

**Serves:** diff-review TOOL-aPromptedMandate-1 TOOL-aPromptedMandate-2 TOOL-aPromptedMandate-3 TOOL-aPromptedMandate-4 TOOL-aPromptedMandate-5 TOOL-aPromptedMandate-6

**Reviewed range:** `b9ebebaae6f776788046980199703c58575d8805...HEAD` (11 commits, six units plus two
phase-witness commits and one reground fold).

**Review shape:** raw 17 · confirmed 12 · refuted 5 · unverified 0 · precision 0.71. The twelve
confirmed findings collapse to **nine distinct sites** — three independent agents landed on
`DIRECTIVES_FLOOR` and three on the prompt path's step 3, which is reported once each below with the
strongest reproduction attached.

**Verdict: 0 blockers, 2 high.** Nothing here defeats the security model. The authorization read,
the BASE observation, and check 19's independent re-derivation all hold under the lens brief, and the
`second-implementation-is-not-a-second-opinion` class found no hit against check 19 itself: the leg
reads the README blob at BASE through `git show`, not through the driver's parse. Both highs are in
the newly-agent-authored surface — the one place this diff moved a document from the owner's hands
into the run's.

**On the build's stated claim** that every new gate predicate was measured firing against the live
tree before its arm was written: it holds for the leg's new predicates (check 19's mode join, check
20's ordering, the scope join's anti-vacuity guard — each reproduced firing here under mutation), and
fails for exactly one arm, M2 below, which asserts a string its own regression cannot produce.

---

## HIGH

### H1 — `DIRECTIVES_FLOOR` left at 11 while `DIRECTIVES_CORE` grew to 13

`.unattended.conf:71` · lens class: `pin-copied-from-another-corpus`

`tools/unattended/unattended.sh:112` now carries 13 entries. `.unattended.conf:71` still declares
`DIRECTIVES_FLOOR="11"`. `tools/unattended/check-unattended.sh:735` tests `[ "$ndir" -ge
"$DIRECTIVES_FLOOR" ]`, so `13 >= 11` passes with two members of slack — exactly the two members this
build added.

**Measured.** Setting the key to 14 reds with `UNATTENDED check 16 FAILED — the kit's CORE directive
set has shrunk below its floor … 13 against 14`, confirming the leg measures 13. Deleting
`researched:M12:prompt` and `solution-tested:M12:prompt` from the driver together with their two
`SKILL.template.md` rows and the installed render leaves `bash tools/unattended/check-unattended.sh`
at rc=0 with no output: arm A's set equality still matches, the scope join goes all-`all` on both
sides with a non-empty extraction so the anti-vacuity guard is satisfied, and arm C passes.

This falsifies the build's own spec-4 **S3** ("DIRECTIVES_FLOOR moves from 11 to 13") and **AC7**
("When DIRECTIVES_CORE is edited to drop a member, check-unattended.sh fails on DIRECTIVES_FLOOR").
The asymmetry is the tell: the same diff bumped `CORE_FLOOR` 10:8 → 12:8 one key up in this same
file, and moved `tools/unattended/.unattended.conf.example:62` 11 → 13. The shipped kit is now
stricter than the repo that dogfoods it.

**Fix.** Set `DIRECTIVES_FLOOR="13"` in `.unattended.conf:71`.

**Left-shift gate.** `tools/unattended/unattended.test.sh:858` added a self-enforcing equality arm
this cycle — but it reads `.unattended.conf.example` only, which is precisely why this miss is
invisible to it. Extend that arm (and its `CORE_FLOOR` sibling at :856) to grade `$ROOT/.unattended.conf`
against `wcw DIRECTIVES_CORE` / `wcw PHASES_CORE:wcw DOD_CORE` as well. The installed conf is the one
the bar actually reads; the example is the one nothing runs.

*One correction to the filed impact, carried so the record is not stronger than the evidence:* the
floor is not the only leg that could see a coordinated deletion — `unattended.test.sh:858` is a strict
equality against the example, so dropping the driver to 11 would red it. The defect is a slack pin on
the one leg whose entire stated purpose is to catch a shrink, not a fully silent hole.

---

### H2 — the prompt path's step 3 tells the agent to author a README that `--preflight` refuses

`tools/unattended/SKILL.template.md:159` · lens class: `inputs-inside-the-subjects-reach`

Step 3 of `## Start a run from a PROMPT` says the run must write
`{{MEMORY_ROOT}}/builds/<slug>/README.md` "with front matter carrying the slug, the streams value,
and **`authorized-by: prompt`**". Two hard requirements go unnamed:

1. **The `<!-- gen:build-index -->` / `<!-- /gen:build-index -->` pair.** `unattended.sh:1313` runs
   `region "$src" "$SRC_OPEN" "$SRC_CLOSE"`; with the pair absent the awk's `no != 1` END clause exits
   3 and preflight emits `fail 9` — *"the build README's generated markers are malformed, and the unit
   list is DERIVED from there"*. **Reproduced** in a scratch fixture with `ANCHOR_SCOPE=published` and
   a README written exactly as step 3 describes: `UNATTENDED check 9 FAILED … memory/builds/tProse/README.md`.
2. **Four of the six front-matter keys.** `tools/memory-tree/gen_build_index.py:105` sets
   `REQUIRED_KEYS = (slug, node, opened, streams, roster, ids)`; step 3 names three. `apply_region`
   raises rather than self-healing on an absent marker pair, so `gates-green` reds at `--close` too.
   Separately `unattended.sh:1574` makes `build-complete` refuse without a well-formed
   `<!-- roster:units -->` region at close.

The agent has no source for either. `grep -c 'gen:build-index'` over `SKILL.template.md`,
`PROTOCOL.template.md`, `memory/guides/UNATTENDED-PROTOCOL.md`, `memory/guides/BUILD-METHOD.md` (the
step-0 read) and the rendered Skill returns 0 in all five. `memory/HYGIENE.md:149` names the key set
but never the marker string, which is the blocking half.

The timing is what makes this high rather than medium: the refusal lands at **step 5**, after step 2's
single owner turn and after step 4's push. This is the exact post-push-refusal shape step 4 goes out
of its way to pre-quote for the push case — the kit already knows this failure mode and pre-empts it
one step earlier, then walks into it here. Latent until now because under the slug path the README is
owner-authored and conformant; this diff made the run the author.

**Fix.** In step 3 (template `:159-164`, and the render at `.claude/skills/unattended/SKILL.md`,
re-rendered via `bash tools/unattended/adopt-unattended.sh`), state the shape the next-but-one step
enforces: the six front-matter keys plus `authorized-by: prompt`, and an empty `<!-- gen:build-index -->`
/ `<!-- /gen:build-index -->` pair — or point at the memory-tree build-README contract the way step 1
now points at the anchor rather than the author. Quote the `fail 9` text the way step 4 quotes the
published-anchor refusal, and add it to step 1's pre-diagnosed refusal list at `:111`.

**Left-shift gate.** `tools/unattended/cross-component.test.sh` is the right home and already has the
machinery: extend its `mk()` with an arm whose README omits the marker pair and assert the check-9
refusal, so the documented shape is *joined* to the accepted shape rather than only written beside it.
That is the same join-both-ways discipline `PHASES_PASSKIND` got in unit 2, applied to the one
document this diff made the run responsible for producing.

---

## MEDIUM

### M1 — `verb_preflight` scaffolds `RUN.md` before validating the README's marker region

`tools/unattended/unattended.sh:1303` · lens class: `inputs-inside-the-subjects-reach`

`scaffold_runmd` runs at `:1303`; the two `region` validations run at `:1313` and `:1318`. The comment
directly above the scaffold states the invariant it breaks: *"The run-state file is created here,
AFTER every precondition passed. A verb that scaffolds and then discovers a refusal has already
changed the state the refusal was about."* Both validated regions are about files that are committed
and readable before the scaffold.

The consequence is a wedge, not just an untidiness. `scaffold_runmd` writes but does not stage
(staging is a later `stage_runmd`), and `check_clean` counts `git ls-files --others
--exclude-standard`, so the orphan untracked `RUN.md` makes the **retry** refuse with a different and
actively false cause: `check 2 FAILED — the working tree is dirty … the run-state file is unchanged`.
Combined with H2 the branch is already pushed, so the run is authorized, wedged, and has nobody to
ask. On this repo the pre-commit hygiene leg would likely red at step 4 before the push, which softens
the endgame here — but an adopter without that leg gets the full shape.

**Fix.** Move the two `region` validations above the `scaffold_runmd` call. That makes the function's
own stated invariant true and costs nothing.

**Left-shift gate.** One arm in `tools/unattended/unattended.test.sh`: drive `--preflight` over a
README with a broken marker pair and assert `[ ! -f memory/builds/<slug>/RUN.md ]` after the refusal —
an on-disk assertion, not an exit code, which is the pattern `tools/govkit/selftest.py` already uses
for its read-only-verb-that-writes arm.

### M2 — the extras-excluded-from-the-scope-join arm asserts a string its own regression cannot produce

`tools/unattended/check-unattended.test.sh:1099` · lens class: `fixture-passes-by-finding-nothing`

`corescope` is built from `$DIRECTIVES_CORE` alone (`check-unattended.sh:613-627`) so an adopter is
not redded for a scope column the kit never asked them to write. The arm certifying that sets
`DIRECTIVES_EXTRA="house-style:M9"` plus a scope-less extra table, then asserts
`miss … "the Skill's directive table carries no scope cell this leg can read"` — the **vacuity**
message.

**Reproduced both implementations** in a scratch repo. As shipped: the vacuity string appears 0 times
and the disagreement string appears 0 times. With the exclusion broken (`corescope` loop changed to
`for _de in $DIRECTIVES_CORE $DIRECTIVES_EXTRA`): the vacuity string *still* appears 0 times, while
check 16 reds at `:713` with *"the directive scopes the registry declares are not the scopes the
Skill's table shows … house-style:all …"*. `tblscope` is built from the kit template only
(`:697-703`), so the vacuity branch is unreachable in either build. The arm is green over the broken
implementation.

Nothing else in the 212-assertion suite covers it — the only other `DIRECTIVES_EXTRA` uses (test
`:938-961`) exercise the table-source branches.

**Fix.** Assert the discriminating string: `miss "$(run)" "the directive scopes the registry declares
are not the scopes the Skill's table shows"`, or assert the whole leg is silent over the fixture.

**Left-shift gate.** This is the class the leg's own comments cite by name, and it survived anyway,
which says the *arm-writing* step needs the measurement, not just the predicate-writing step. The
build's claim — "every new gate predicate was measured firing against the live tree before its arm was
written" — should be extended one notch to *every new arm was measured RED against the mutation it
names*. `tools/memory-tree/check-arms.py` already enforces the positive half (a `fail` branch armed by
an assertion naming its own failure text) for shell gates; this arm passes that structural bar while
naming the wrong text, so the mechanical follow-on is to have `check-arms.py` require the asserted
string to be one the branch under test can actually emit.

---

## LOW

### L1 — `fail 45` is the only new verdict in this diff with no bar-side second opinion

`tools/unattended/check-unattended.sh:466`

Check 17 second-opinions a parked waiver on three dimensions (handle membership, non-empty reason,
presence in the record's first committed blob); check 19 second-opinions the recorded mode against the
README at BASE. Neither joins scope to mode, so a landed run-state file recording `mode: slug`
alongside `waiver · item researched` passes the bar. `grep -n prompt tools/unattended/check-unattended.sh`
returns no waiver/mode join anywhere. Check 17's own header names the gap: *"Unit 3 refuses a bad
waiver at the moment of writing; this is the SECOND OPINION over what actually landed."* The driver's
other waiver refusals (39, 40) have one; fail 45's does not — and check 19 was added in this same diff
on exactly the principle that a value only the driver reads is a value only the driver can be wrong
about.

**Fix.** In check 17's waiver loop: when `recmode` is non-empty and the handle's third field in
`$DIRECTIVES_CORE` is `prompt` while `recmode != prompt`, fail with a named message. Both inputs are
already in hand — `recmode` is derived at `:466` in the same per-file loop iteration, and
`DIRECTIVES_CORE` is sourced globally. (`corescope` itself is not in scope there; it is computed later
at `:613`. The registry constant it derives from is.)

**Left-shift gate.** Arm it the way the forged-mode arm is armed — edit the *record*, not the anchor.

### L2 — `scope_of` reads `DIRECTIVES_EXTRA`, so scope is a project knob after all

`tools/unattended/unattended.sh:123`

`scope_of` iterates `$(directives)` — core plus extras — so `DIRECTIVES_EXTRA="house-style:M9:prompt"`
does resolve to a scope, contradicting `unattended.sh:105` ("The scope is NOT a project knob") and
`PROTOCOL.template.md:400` ("The scope is KIT-OWNED"). Nothing catches it: check 16 builds `core` by
stripping the third field so arm A passes, and `corescope` comes from `DIRECTIVES_CORE` alone so the
scope join is structurally blind to extras. The result would be a `fail 45` refusal about
"prompt-authorized runs" for a rule the agent's own `DIRECTIVES_EXTRA_TABLE` row grammar
(`handle | text | M<n>`) cannot express.

The substantive invariant is intact — an extra cannot *narrow* the core, since core entries precede
extras and `scope_of` returns the first match — so this is prose-vs-code, self-inflicted, and narrow.

**Fix.** Make the claim true: iterate `$DIRECTIVES_CORE` only and return `all` for anything not found
there, or refuse a three-field `DIRECTIVES_EXTRA` entry at conf-load with a named refusal, the way the
closed `ANCHOR_SCOPE` value set is handled.

**Left-shift gate.** The refusal-at-conf-load route is the one that gates itself.

### L3 — `PHASES_PASSKIND` is joined both ways to the protocol but never to `PHASES_CORE`

`tools/unattended/unattended.sh:89`

The new `kd1`/`kd2` join compares `PHASES_PASSKIND` only against the protocol's `PASS kinds:`
paragraph. A typo or invented token mirrored in both sides (`SPECING`) passes both joins while naming
a position no run can occupy — the failure the run-order join's `pd2` branch exists to catch, one set
over. Deleting the constant entirely *does* red via `kd2`, so vacuity itself is covered. The repo
already applies exactly this subset assertion to the sibling independently-declared set at
`check-unattended.sh:124` ("A TERMINAL phase is not in the effective vocabulary … this one IS
falsifiable, because the two sets are declared independently"), so this is a gap in an established
pattern rather than a design choice. Impact is genuinely low: the constant feeds no runtime branch, so
a bogus token misstates the contract rather than breaking a run, and it needs the same typo authored
twice.

**Fix / left-shift gate.** One line beside the pass-kind join —
`comm -23 <(printf '%s\n' $PHASES_PASSKIND | sort -u) <(printf '%s\n' $PHASES_CORE | sort -u)` must be
empty, with its own failure text — armed in `check-unattended.test.sh` by mutating the driver constant
to a non-core token.

### L4 — the leg's docstring still says "EIGHTEEN checks" after this diff added 19 and 20

`tools/unattended/check-unattended.sh:2` (and `AGENTS.md:159`)

`grep -oE 'fail [0-9]+'` over the file yields `fail 1` through `fail 20` with no gaps; both new
ordinals were added by this diff (fail 19 at `:473`, three `fail 20` branches under the `# ---- 20:
the PROMPT path's own ordering` header). Two carriers now state a number the file contradicts, in a
repo whose own gotcha corpus names this class — `two-answers-to-one-question` — and whose new
pass-kind join exists precisely because "the DoD count sentence went stale in both copies while its
leg stayed green."

**Fix.** Update both to "TWENTY", or drop the numeral from both and let the check ordinals be the
count — the pattern the `AGENTS.md` memory-tree line already uses for its kit version, and for the
same stated reason ("a version written in prose rots between bumps").

**Left-shift gate.** Dropping the numeral is the gate. A count nothing joins will go stale again.

### L5 — `kit.toml`'s `placeholders` declaration is one short of the render surface

`tools/unattended/kit.toml:17`

`SKILL.template.md` carries seven distinct placeholders; `adopt-unattended.sh` `render()` substitutes
all seven (`:172` — `out=${out//\{\{ANCHOR_SCOPE\}\}/"$ANCHOR_EFFECTIVE"}`); the descriptor lists six.
The same descriptor's `optional_keys` also omits `ANCHOR_SCOPE`, a conf key both the driver and the
adopter read. No reader in `tools/govkit/*.py` consumes `placeholders` today (only a comment at
`govkit.py:2667` uses the word), so impact is nil — which is why this is low — but it is the
declaration a future renderer or audit would trust, and the list is not conf-key-scoped (`KIT_DIR` is
install-derived), so `ANCHOR_SCOPE` belongs in it.

**Fix.** Append `"ANCHOR_SCOPE"` to the files rule's `placeholders`, and add `ANCHOR_SCOPE` to
`[config] optional_keys`.

**Left-shift gate.** The govkit selfcheck already asserts the deployable surface in both directions
against a declaration. The natural extension is one more predicate in the same leg: for every files
rule whose `role = "rendered"`, the declared `placeholders` set equals the `{{…}}` tokens measured in
the named template. That would have caught this at the moment unit 5 added the seventh.

---

## What the lens brief cleared

Reported because a class hunted and not found is evidence, and the next reviewer should not re-spend it:

- **`heredoc-escape-reaches-the-regex`** — no hit. The new front-matter awk, the scope splitter and
  check 20's ordering extraction all live in single-quoted program text; the `${rest#*:}` /
  `${p#*:}` shortest/longest-prefix pair in `scope_of` is parameter expansion, not a regex, and its
  two-field default falls out of the pair rather than being tested for.
- **`assertion-between-two-derived-values`** — no hit on check 19. The leg re-derives `mode:` from the
  README blob at BASE via its own `git show` read, and compares it to the run-state file's recorded
  fact. Two independent carriers, so the join is falsifiable; confirmed by mutating the record and
  watching `fail 19` fire.
- **`second-implementation-is-not-a-second-opinion`** — no hit on the front-matter parse. The unit-1
  shape change (the awk no longer prints-and-exits on first match, so the second arm below it is
  reachable) is real and correctly made; the leg does not reuse the driver's parse.
- **`fixture-passes-by-finding-nothing`** — one hit, M2. The scope join's own anti-vacuity guard is
  present and was measured firing.
- **`pin-copied-from-another-corpus`** — one hit, H1, and it is the inverse of the usual shape: the
  *example* was measured and the *dogfood* conf was copied forward unmoved.
