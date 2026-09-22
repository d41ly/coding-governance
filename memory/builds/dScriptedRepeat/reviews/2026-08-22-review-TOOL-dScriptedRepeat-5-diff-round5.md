**Serves:** diff-review TOOL-dScriptedRepeat-5 TOOL-dScriptedRepeat-6 TOOL-dScriptedRepeat-7 TOOL-dScriptedRepeat-9 TOOL-dScriptedRepeat-10 TOOL-dScriptedRepeat-11

# dScriptedRepeat — diff review, round 5 (the fold of round 4's nine)

**Range:** `376c2c635b1a0e5ba0e5cd8ba0a4e8b1bf6a5f1f...22cbb7a3` — one commit, `22cbb7a3` (round 4's
three blockers, both highs, all four mediums; gates first, then the defects they found). 13 files,
1153 insertions, 77 deletions.
**ROUND 5.**

**Review shape:** raw 26 · confirmed 23 · refuted 3 · unverified 0 · precision 0.88. The 23 confirmed
findings collapse to **10 distinct defects**; four clusters were found independently by two to four
lenses each, and that corroboration is recorded per defect rather than inflating the count. Every
mechanism below was re-reproduced against the working tree by the synthesis pass before it was
written down, and the reproductions are quoted where they are the evidence.

## Verdict: BLOCKED

One blocker, three highs, five mediums, one low.

**The standing pattern held for a FIFTH round, and it held in the same function it has held in for
three.** Rounds 1–4 each broke on the previous round's blocker restored by the commit that fixed it,
one abstraction level up: no join, then the wrong parser, then `head -1` at the call sites, then the
terminator test on the raw line. This round it is one `sed` stage earlier than that. Round 4's fix
moved the comment strip in front of the terminator test — correctly — and left untouched the
key-strip that runs before both of them, which eats the whitespace the comment strip requires. So an
empty-valued declaration carrying a trailing comment now parses to **the comment text itself**, at
rc 0, in both parsers and both copies. Round 4's HIGH 4 was the `outputs` guard failing open on the
kit's own template line; this fold moved that read onto the shared parser and narrowed the guard to
`''` alone, and the narrowed guard is what the parser defect walks straight through (**BLOCKER 1**).

**And the three structural gates that were supposed to break the chain are instance gates, all
three.** That is this round's real finding, because the fold's whole thesis rests on them.

- **28a** — the rule is "the refusal must be READ at every call site". It whitelists any line
  containing `||`, so `x=$(declared_list …) || true`, the canonical way to *discard* a refusal, is
  graded compliant. Measured: that spelling at `unattended.sh:2165` restores round 4's BLOCKER 2 byte
  for byte with check 28 green (**HIGH 2**).
- **28b** — the rule is "every declaration key is bound to the parser its real reader calls". It is a
  `grep -nF` for one exact `sed` program text. Measured: 10 template keys, 0 hits, and one of the ten
  (`legs`) is already in exactly the state the check's own comment names as the defect it exists to
  refuse — certified through `declared_scalar`, read by a bespoke `grep -oE` at
  `check-playbook.sh:269` (**HIGH 3**).
- **28c** — the rule is "EVERY SHA DEREFERENCE IN THIS KIT goes through a pinned read". Measured: its
  predicate matches **one line in the whole kit**, and that line is the one it exempts. The kit's
  twelve other sha dereferences are spelled through the uppercase `GIT` wrapper and are invisible to
  it, as is the wrapper definition where the pin actually lives (**HIGH 4**).

Each of the three was observed RED against the live tree before the fixes went in, exactly as the
commit message says. That is a real and unusual discipline, and it is why this round found nine
defects rather than eleven. What a single observed RED cannot establish is the *width* of a
predicate, and all three predicates are one spelling wide.

**The full bar is 92/92 green over this diff.** Everything below is something 92 legs certified.

### Checklist classes hit (`python tools/memory-tree/gotchas.py --for-diff 376c2c63..HEAD`)

`fixture-passes-by-finding-nothing` — defects 7, 8 and 9, all three in the suites this fold added.
`second-implementation-is-not-a-second-opinion` — defects 2, 3 and 4, the three new gates.
`containment-tested-one-way` — defects 1 and 5, the two containment tests left in the parser.
`two-answers-to-one-question` — defect 3: `legs` is certified through one reader and read by another.
`fixture-inherits-ambient-machine-state` — defect 7, the replace-ref arm's scratch repo.
`inputs-inside-the-subjects-reach` — defect 4: the pin is the only thing holding the committed BASE
blob outside the run's reach, and the gate asserting it covers one self-exempting line.

---

## BLOCKER 1 — the key-strip eats the whitespace the comment-strip needs, so an empty-valued declaration parses to its own comment

**`tools/unattended/check-playbook.sh:167`** and **`:188`**, with their byte-identical copies at
**`tools/unattended/unattended.sh:2399`** and **`:2420`**. Consumer sites: **`unattended.sh:962`** and
**`check-playbook.sh:213`**.
*Found by two lenses; reproduced end to end by the synthesis pass against both shipped parser bodies.*

Both parsers open the same way:

```sh
sed -n "s/^$2[[:space:]]*=[[:space:]]*//p" | head -1 | sed 's/[[:space:]][[:space:]]*#.*$//'
```

The key-strip consumes the whitespace run after the `=`. The comment strip *requires* whitespace
before the `#`. So when the value is empty and the line carries a comment, the `#` lands at column 0
and nothing removes it — the comment becomes the answer. Measured against both shipped bodies:

```
declared_list   'outputs = # globs. Where pieces land.'    -> rc=0  answer=[# globs. Where pieces land.]
declared_scalar 'curated = # who ratified this playbook…'  -> rc=0  answer=[# who ratified this playbook…]
declared_list   'outputs = ["a/**", "b/**"]   # note'      -> rc=0  answer=[a/** b/**]     (unchanged)
declared_scalar 'curated = "someone 2026-01-01"   # note'  -> rc=0  answer=[someone …]     (unchanged)
```

Two guards fail OPEN on that, and both are refusals this build wrote deliberately.

`unattended.sh:962` is `case "$AUTH_OUTPUTS" in '') fail 46 …`. `AUTH_OUTPUTS` is now the comment
text, so the arm never fires and `check_authorization` **authorizes a recipe-mode run declaring no
output globs** — the exact state the refusal's own message says leaves the scope check with nothing
to compare against. `AUTH_OUTPUTS` has three occurrences in the tree (`:357` init, `:951` parse,
`:962` the test); no downstream scope comparison reads it, so this guard is the key's only consumer
and there is no second line of defence.

`check-playbook.sh:213` is `[ -n "$cur" ] || fail 2 …`, the FREEZE — fork 4's only machine
consequence. `curated` parses to its comment, `cur` is non-empty, and **check 2 passes on an
unratified playbook**. That is round-3 HIGH 6 restored one spelling over.

This is not a contrived authoring shape. The kit's own comment at `check-playbook.sh:218-221` cites
`step_floor =    # TBD 5` verbatim as the authoring it added a shape refusal for, and the shipped
template puts a trailing comment on **every** declaration line — an adopter who copies the template
and clears a value they have not decided yet reaches this on the first try. `step_floor`, `grain`,
`records` and `coverage` take the same wrong value and happen to fail closed downstream.
`piece_checks`/`set_checks` fail closed too, loudly: the comment's words become phantom leg names.
`outputs` and `curated` are the two that fail open, and they are the two on the authorization path.

**Why this is the blocker and not a high.** Round 4 graded the `outputs` guard a HIGH when it failed
on the template's *filled* line. This is the same guard, failing on the template's *unfilled* line,
introduced by the commit that fixed the first — plus the freeze, which round 4 did not touch. It is
live, reproduced, present in both parsers and both copies, and it is the fifth consecutive recurrence
of the same shape in the same function.

**Fix.** Drop the trailing `[[:space:]]*` from the key-strip in both parsers and both copies
(`check-playbook.sh:167` and `:188`, `unattended.sh:2399` and `:2420`):

```sh
sed -n "s/^$2[[:space:]]*=//p"
```

The existing `s/^[[:space:]]*//` trims the leading run afterwards, so `k = ["a"]`, `k = [`,
`k = [   # x]` and `k = "v" # c` all keep their current answers, while `k =    # c` correctly becomes
empty. Verified against both bodies before proposing it. Then, independently, give `declared_list`
the shape refusal its scalar sibling gained this round: after the comment strip, a non-empty `$raw`
that does not begin with `[` is an array key whose value is not an array, and `return 2` is the
honest answer.

**Left-shift gate.** Add `'Xoutputs =    # noteX|XX'` and `'Xcurated =    # noteX|XX'` to check 28's
specimen lists for **both** parsers — the list half and the scalar half — with the empty answer
expected, staged RED first. Every existing specimen carries a value, which is why 92 legs were green
over this. Add a `check-playbook.test.sh` arm whose fixture empties `curated` but keeps its comment,
asserting check 2 still reds.

---

## HIGH 2 — 28a whitelists `|| true`, the exact spelling that discards a refusal

**`tools/unattended/check-unattended.sh:1458`**
*Found independently by three lenses; the bypass was measured.*

```sh
case "$_txt" in
  *'if !'*|*'||'*) continue ;;
esac
```

A naked substring test over the whole call line, standing in for "the status is consumed". Measured:
I replaced `unattended.sh:2165` with `_declared=$(declared_list "$_blob" set_checks) || true` and ran
28a's exact predicate — **4 sites enumerated, 0 failures, check green**. That mutation is round 4's
BLOCKER 2 byte for byte: rc 2 arrives as empty stdout, the `''` alternative of the declared-null
escape at `unattended.sh:2172` matches first, and `set-checks-recorded` returns MET with no record,
no verdict and no override entry — on an item in `DOD_NO_OVERRIDE`.

`|| true`, `|| :` and `|| _x=""` are not "the wrong branch", which the header explicitly disclaims
covering. They are *no branch at all*: the refusal is consumed and thrown away. The failure message
this arm would have printed says so itself — "called at a site that discards its exit status".

A second, quieter shape is exempted for the same reason: `_a=$(declared_list "$b" k); [ -z "$_a" ] ||
fail …`, where the `||` binds a different command entirely and the parser's rc is genuinely never
read. And the inverse false-positive is real: `x=$(declared_list …); rc=$?` is a correct read that
28a reds.

The only positive arm in the suite (`check-unattended.test.sh:1535`) mutates to
`_declared=$(...); if false; then`, which contains neither token — so **the gate has never been
observed to fail against a `||` spelling**. All four live sites (`unattended.sh:951`, `:2165`;
`check-playbook.sh:315`, `:398`) branch correctly today, which is the only reason this is not the
blocker. The gate is the deliverable, and 28a is the sole guard for the call sites its own header
invites: "Give `declared_scalar` one tomorrow and its call sites start being policed."

**Fix.** Stop whitelisting by substring. Red the discard spellings explicitly, before the generic
arm:

```sh
case "$_txt" in
  *'||'[[:space:]]*true*|*'||'[[:space:]]*:*) ;;   # falls through to fail
  *'if !'*|*'while !'*|*'||'*) continue ;;
esac
```

**Left-shift gate.** Add a suite arm mutating `unattended.sh:2165` to
`_declared=$(declared_list "$_blob" set_checks) || true` and assert check 28 reds, staged RED before
the fix. Add a second arm for `x=$(declared_list …); rc=$?` asserting it does NOT red, so the
tightening does not buy a false positive.

---

## HIGH 3 — 28b is a fixed-string search for one `sed` spelling, and its own positive claim is already false in-tree

**`tools/unattended/check-unattended.sh:1491`**
*Found independently by three lenses; both halves measured.*

```sh
$(grep -nF "s/^$_k[[:space:]]*=" "$_f" …)
```

`grep -nF` — a FIXED-STRING search for one exact character sequence. It matches only a `sed` written
with that literal bracket expression. `awk -F'='`, `grep | cut -d=`, `grep -oE`, and
`sed -n 's/^step_floor[ \t]*=//p'` (a different whitespace class) all pass untouched.

Measured, first half: I replaced `unattended.sh:951` with

```sh
AUTH_OUTPUTS=$(printf '%s\n' "$_pb" | awk -F'=' '/^outputs/{print $2; exit}')
```

and ran 28b's exact predicate — **kb_keys=10 (liveness passes), 0 failures**. That read returns the
template's untrimmed ` []    # globs. Where pieces land…`, so `case "$AUTH_OUTPUTS" in '')` never
fires and check 46 is bypassed exactly as it was before round 4's fix, with 28a *and* 28b green. The
same holds for `step_floor` and MEDIUM 7's digit-splicing class.

Measured, second half — and this one is not hypothetical: **the check's positive claim is already
false for a key in the shipped template.** The template fence yields ten keys; the hit count is 0 for
every one. `legs` is in the scalar loop's population and check 28 ships a `k = {}    # note` specimen
for its shape, so 28b certifies `legs` through `declared_scalar` — while
`grep -rn 'declared_list\|declared_scalar' tools/unattended/*.sh | grep -w legs` returns **nothing**.
Its real reader is the bespoke `grep -oE "(^[[:space:]]*|[{,][[:space:]]*)\"?$g\"?[[:space:]]*=…"`
plus a hand-written `sed` at `check-playbook.sh:269-278`. That is verbatim the state the check's own
comment names as what it exists to refuse: "certifying a key through a parser its consumer does not
call is a gate confirming its own re-implementation". Live in the tree, under a green 28b.

The binding is also one-directional. The loop only reds keys it catches being read ad-hoc; **no key
is ever required to HAVE a parser reader.** `kb_keys` counts *template keys*, not readers found, so
the `kb_keys -gt 0` liveness assertion is satisfied by a kit that reads every single key ad-hoc.
`check-playbook.sh:83`'s `grep -q '^step_selector[[:space:]]*='` already sits outside the predicate.

**Fix.** Invert 28b to a POSITIVE binding: for each key the template fence declares, require a
literal `declared_list "…" <key>` or `declared_scalar "…" <key>` call somewhere in the driver or the
leg, and red any key with none. That reds on `legs` today, forcing either a real parser read for the
registry or a declared exemption naming its actual reader — the exemption list living beside the
check, so a stale one reds too. Keep the negative scan as a second predicate, widened from a fixed
string to `grep -nE "[^A-Za-z_]$_k[[:space:]]*="` restricted to lines carrying `sed|awk|grep|cut|tr`.

**Left-shift gate.** The positive binding IS the gate. Stage it RED against the live tree first — it
should name `legs` — and add a suite arm that deletes a `declared_scalar` call and asserts check 28
reds naming that key.

---

## HIGH 4 — 28c's live population is exactly one line, and that line is the one it exempts

**`tools/unattended/check-unattended.sh:1524`**
*Found independently by four lenses; the population and the bypass were both measured.*

```sh
$(grep -nE '(^|[^-[:alnum:]_])git ([^|;&]*[[:space:]])?(show|cat-file)[[:space:]]' "$_f" …)
```

Lowercase `git`, two verbs, three named files. I ran that predicate over the three files it scans:

```
tools/unattended/unattended.sh       -> (none)
tools/unattended/check-playbook.sh   -> 121: GITSHOW() { git -c core.useReplaceRefs=false … show "$1" … }
tools/unattended/lib-unattended.sh   -> (none)
```

**One hit in the entire kit, and it is the line the `core.useReplaceRefs=false` case-arm exempts.**
The `fail` branch is unreachable against the live tree, and `sha_reads > 0` — the liveness assertion —
is satisfied by that single self-exempting element.

Everything real is invisible to it. The driver dereferences shas seven times, all through the
uppercase wrapper: `unattended.sh:513`, `886`, **`938`** (`GIT show "$base:$AUTH_PLAYBOOK"` — the
authorization read of the committed BASE blob, one of exactly two inputs the security model places
outside the run's reach), `1027`, **`2147`** (`set-checks-recorded`'s blob), `2784`, `2814`.
`check-unattended.sh` has five more, including check 9's read of the build README at the recorded
base — and `check-unattended.sh` and `adopt-unattended.sh` are not even in the scanned file list.
`lib-unattended.sh:20`, where the wrapper's pin actually lives, carries no `show`/`cat-file` token
and is therefore outside its own gate.

Measured bypass: rewriting `lib-unattended.sh:20` to `GIT() { git "$@"; }` — the pin deleted from the
one wrapper every driver read goes through — leaves 28c enumerating 1 site, exempting it, and
**passing**, liveness assertion satisfied. All twelve wrapper-spelled dereferences become
replace-ref-steerable and check 28 says nothing. The only thing catching it today is a fixed-string
grep in a different leg (`unattended.test.sh:1823`), and the suite arm at
`check-unattended.test.sh:1549-1551` mutates *both* files, which is why the `lib-unattended.sh` half
being a no-op for the count was never noticed.

Two narrower gaps ride along. The verb set is `show|cat-file` while `unattended.sh:57` states the
invariant as "every read below that turns a sha into bytes **or into ancestry** goes through
`GIT()`" — `merge-base`, `rev-list`, `log`, `ls-tree` and `rev-parse <sha>^{}` are all
replace-ref-sensitive and all outside the alternation. And the exemption
`*'core.useReplaceRefs=false'*` is a substring test over the whole line while the comment filter
excludes only lines whose *first* non-space character is `#` — so a trailing comment mentioning the
pin exempts an unpinned read, which is §7's "gate satisfied by its own comment prose".

No live unpinned read exists today: every `GIT show` site is pinned by construction. This is a
coverage and liveness gap in the gate written to make round 4's BLOCKER 3 impossible to repeat, not a
live escape — which is what keeps it off the blocker line.

**Fix.** Match the wrapper as well as the raw command — `(^|[^-[:alnum:]_])(git|GIT)[[:space:]]` —
and widen the verb set to `show|cat-file|ls-tree|archive|rev-list|log|merge-base|diff-tree`. Accept a
`GIT`-spelled site only when the same scan proves `lib-unattended.sh` defines `GIT()` carrying
`core.useReplaceRefs=false`, so the wrapper definition sits *inside* the gate rather than beside it in
another suite. Derive the file population from the kit's tracked `*.sh` (glob or `kit.toml`) instead
of the three-name list. Test the exemption against the git invocation itself, not anywhere on the
line. Assert liveness **per file**.

**Left-shift gate.** Add a suite arm that strips the pin from `lib-unattended.sh:20` *only* and
asserts check 28 reds — staged RED first; the current arm passes with that file untouched. Add a
second arm adding a bare `git merge-base --is-ancestor "$base" HEAD` to the driver and assert it reds.

---

## MEDIUM 5 — the terminator test is still a containment test, so a `]` in the VALUE closes the array

**`tools/unattended/check-playbook.sh:169`** and its copy at **`unattended.sh:2401`**
*Found by one lens; reproduced.*

```sh
case "$raw" in
  *'['*']'*) ;;
  *'['*) return 2 ;;
esac
```

Round 4 moved the comment strip in front of this — correctly — and left the test itself a substring
test over one line. A `]` anywhere in the **value** still satisfies the closed arm. Reproduced
against the shipped body:

```
k = ["a[0]",        (members "b" on following lines)   -> rc=0  members=[a[0]]
k = [               (members "b" on following lines)   -> rc=2  members=[]
```

The second member is **silently dropped**, not refused — and the parser's own header two lines up
states its contract is to refuse rather than return a wrong answer at rc 0.

Reachability differs by key. `outputs` and `grain` hold globs, where `[0-9]` and `[a-z]` character
classes are ordinary — `outputs = ["content/pieces/[0-9]*/**",` opens this on the first line of an
ordinary multi-line array. For `piece_checks`/`set_checks` a bracketed leg name is needed, which is
rarer; when it happens the dropped leg is never in `$pchk`, the `miss_` loop at
`check-playbook.sh:369-374` never looks for it, and a piece carrying no verdict for it counts
`verified` — round-3's blocker consequence on `pieces-complete`, reached by the third spelling of the
one-line-substring class in the same function. The narrower reach is what keeps this at medium.

**Fix.** Test the closer positionally, in both copies byte-identically:

```sh
case "$raw" in *']') ;; *'['*) return 2 ;; esac
```

`["a"]`, `[]`, `[ ]` and `["a[0]", "b"]` still parse; `[`, `[   # x]` and `["a[0]",` all refuse.

**Left-shift gate.** Add `k = ["a[0]",` as a fourth specimen in check 28's `_ml` loop with rc 2
expected, and a `check-playbook.test.sh` arm whose multi-line `piece_checks` opening line carries a
bracketed member. Stage both RED.

---

## MEDIUM 6 — 28a's `rc_sites` is one counter for two parsers and two files

**`tools/unattended/check-unattended.sh:1446-1447`**
*Found by one lens; structurally identical to the defect this same commit fixed one code block away.*

`rc_refusers` and `rc_sites` are incremented inside both the `for _p` parser loop and the inner
`for _f` file loop, and the liveness refusal is a single global `elif [ "$rc_sites" -eq 0 ]`. Its own
message speaks per-parser — "a refusing parser was found and NO call site of it was" — which the code
cannot deliver.

Live measurement: `rc_refusers=1`, `rc_sites=4`. Only `declared_list` carries a nonzero return today,
so the counter is currently honest by accident. The moment `declared_scalar` gains one — which 28a's
own header explicitly invites — its eleven call sites join `rc_sites` while `declared_list`'s four
hold the total up, and a `declared_scalar` whose calls are all spelled outside `$(name<space>`
(backticks, a redirected call, a line continuation) is policed by nothing with the liveness assertion
still green. The per-file half bites today: `check-playbook.sh`'s two sites could become unmatchable
and `unattended.sh`'s two would keep the total at 2.

This is exactly the defect the same commit fixed for `tpl_list`/`tpl_scalar` at `:1610-1611`, under a
comment explaining why one shared counter was wrong — applied to one of the two counters in the file.

**Fix.** Reset a `_sites` counter at the top of each `_p` iteration and each `_f` iteration, and fire
the empty-population refusal naming that parser and that file.

**Left-shift gate.** A suite arm that makes `check-playbook.sh`'s call sites unmatchable (rename the
call spelling) while leaving the driver's intact, asserting check 28 reds. It passes today.

---

## MEDIUM 7 — the replace-ref arm never proves the lever bites, and its scratch repo inherits ambient git config

**`tools/unattended/check-playbook.test.sh:363`**, with `seed()` at **`:32-44`**
*Found independently by three lenses.*

The arm has four controls: the honest and forged trees grade differently, `git replace -f` succeeded,
a ref exists under `refs/replace/`, and the pinned census did not move. **None of them proves the ref
BITES.** There is no unpinned read anywhere in the arm.

`seed()` runs a bare `git init` and sets only `user.email`, `user.name` and `core.autocrlf` — no
`GIT_CONFIG_GLOBAL` isolation, no `HOME` override, nothing pinning `core.useReplaceRefs`. The scratch
repo therefore inherits ambient global and system config. On a node with `core.useReplaceRefs=false`
set globally, with `GIT_NO_REPLACE_OBJECTS` exported, or under a future git that changes the default,
the lever is inert, `PINR = PINH` holds trivially, and the arm goes green over a `GITSHOW` with the
pin deleted. `fixture-inherits-ambient-machine-state` plus `fixture-passes-by-finding-nothing`,
inside the arm written for the blocker whose entire history is "recorded as fixed without reaching
the file".

The kit already knows this. The sibling arm at `unattended.test.sh:1755-1758` carries both halves and
its comment states why in as many words: without a live control, "the driver refused" is
indistinguishable from "the attack never worked here". The newer arm omits the control the older one
documents as mandatory. I confirmed the lever does bite on this node — which is precisely what an
uncontrolled arm cannot tell you.

**Fix.** Add the control the driver suite already has, immediately after installing the ref and
before reading `PINR`:

```sh
same "replace-control: an unpinned read at HONEST returns the forged bytes" \
  "$( cd "$W" && git show "$HONEST:tools/unattended/playbook.fixture.md" | grep -c 'fixture-shape' )" "1"
```

and set `GIT_CONFIG_GLOBAL=/dev/null GIT_CONFIG_SYSTEM=/dev/null` in `seed()` so the arm stops
depending on the developer's global config.

**Left-shift gate.** Run the suite once with `git config --global core.useReplaceRefs false` set and
assert it REDS. That is the staged break for this arm, and it is a two-line experiment.

---

## MEDIUM 8 — `PINF` is the one capture in the fold's new arm that `require_shape` was not applied to

**`tools/unattended/check-playbook.test.sh:355`**
*Found independently by two lenses.*

`PINH` at `:350` is shape-guarded at `:351`. `TREE1` elsewhere in the file is guarded. `PINF` at
`:355` goes straight into `[ "$PINF" != "$PINH" ]` at `:357` with no guard — and that comparison is
the **fail-open** direction. An empty or malformed `PINF` satisfies `!=` against a non-empty `PINH`,
so the control that establishes the arm can tell honest from forged passes having compared a census
against nothing.

The trigger is not exotic. `fail()` at `check-playbook.sh:27` printfs to stdout unconditionally and
the validity checks run before the census printf, so a `--counts` invocation can emit a failure line
first; `head -1` then captures it. I staged a missing `curated` and confirmed: line 1 of stdout is
`PLAYBOOK check 2 FAILED …`, the census is line 2. Four code paths in the leg suppress the census
line entirely.

`PINR`'s comparison is `=`, which is fail-safe — so the omission landed on precisely the capture
where it costs something. This is round 4's MEDIUM 8 class one capture over, inside the arm that
introduced `require_shape` for that class, and the file states the invariant it is violating in its
own header at `:18-24`.

**Fix.** `require_shape "$PINF" 'pieces=* verified=*' "the forged pinned census this arm compares
against"` immediately after `:355`, matching `PINH`'s treatment. Select by shape rather than position
in all five `--counts` captures: `| grep -m1 '^pieces='`.

**Left-shift gate.** A suite-wide assertion that every `$(… --counts …)` capture in both suites is
followed by a `require_shape` on the same variable — greppable, and it reds on this line today.

---

## MEDIUM 9 — the MEDIUM-7 positive arm is made entirely of negative assertions with no liveness anchor

**`tools/unattended/check-playbook.test.sh:302-317`**
*Found by one lens; verified by reading.*

The arm that proves a valid `step_floor = 1` with a digit-bearing comment parses correctly is
`out=$(run)` followed only by `grep -qE 'check 3 FAILED' && bad` and
`grep -qF 'declares a step selector and no floor' && bad`. Nothing asserts `$out` is non-empty or that
the leg reached a verdict. The guard at `:309` checks only that the `sed` edit took.

The file sets `set -u` but not `set -e`, so a run that dies early — git missing, not-a-work-tree exit
2, a check-1 empty-population red from an unrestored fixture, a syntax error — yields output matching
neither pattern, and the arm reports that the shared parser reads a commented floor correctly having
observed nothing. `FLOOR_ASSERTIONS` at the tail pins the executed assertion count, not leg liveness,
so it does not cover the gap.

Every sibling negative arm in this file is anchored by a positive first (`:264` anchors `:267`, `:295`
anchors `:298`), and the file's own `require_shape` helper at `:97-108` exists for exactly this class
and names it. This one arm was written without it.

**Fix.** One line before the two negatives:

```sh
grep -qF -- 'population 1 playbook' <<<"$out" \
  || bad "the leg produced no population line, so the two refusals asserted absent below were asserted over nothing"
```

**Left-shift gate.** The same suite-wide grep as defect 8, one class up: every `out=$(run)` whose only
assertions are `&& bad` must carry a preceding `|| bad` anchor. Both suites, and it reds here today.

---

## LOW 10 — a non-numeric `step_floor` emits a second refusal that contradicts the first

**`tools/unattended/check-playbook.sh:224`**, consumed at **`:232`**
*Found independently by three lenses; reproduced in a scratch tree.*

The new non-numeric refusal sets `flo=""` so the arithmetic below cannot error on it. Ten lines down,
`if [ -z "$flo" ]` fires. `step_floor = soon` therefore prints:

```
check 3 FAILED — a playbook declares a step floor that is not a number … [soon]
check 3 FAILED — a playbook declares a step selector and no floor
```

The second denies what the first asserts and sends the reader to add a floor that is plainly
declared. It is the exact wrong-cause diagnostic the fix's own test comment at
`check-playbook.test.sh:319-322` says the old code produced — so the misdiagnosis was not removed, it
was joined by a correct message. The suite's arm at `:328` asserts only that the correct message is
PRESENT, never that the false-cause one is ABSENT — while the digit-bearing-comment arm twenty lines
earlier DOES assert an absence, so the discipline exists in the same file and was not applied here.

The verdict is unaffected (check 3 reds either way) and the driver ignores this leg's exit status by
design, which is why this is low. It also collapses two distinct states onto one message, weakening
the `probe "no step floor"` arm at `:105`, which now asserts a message that no longer uniquely
identifies its cause.

**Fix.** Carry the refusal as its own state rather than by emptying the value: set `flo_bad=1`
alongside `flo=""` and guard `:232` with `if [ -z "$flo" ] && [ -z "${flo_bad:-}" ]; then`.

**Left-shift gate.** Add `grep -qF -- 'declares a step selector and no floor' <<<"$(run)" && bad …` to
the non-numeric arm, matching the counter-assertion the digit-comment arm already carries. It reds
today.

---

## Refuted (3 of 26)

Recorded so a later round does not re-file them.

- A claim that `check_authorization`'s `AUTH_OUTPUTS` scope is compared against the run's actual diff
  downstream, which would make BLOCKER 1's guard non-load-bearing. Refuted: `AUTH_OUTPUTS` has three
  occurrences in the tree and none is a comparison. The refutation strengthened BLOCKER 1 rather than
  weakening it.
- A claim that 28a's enumeration misses backtick-spelled call sites today. Refuted: no backtick call
  site exists in the kit, and the enumeration's narrowness is already carried by defect 6.
- A claim that check 28's byte comparison of the two parser copies could pass over an empty pair.
  Refuted: `:1546` and `:1554` each red explicitly on an empty extraction, and both arms have observed
  RED coverage in the suite.

## What was checked and found sound

Recorded so the next round does not re-spend on it.

- **The copy-inline byte comparison.** Both parsers, both copies, extracted and compared, with an
  explicit refusal on an empty extraction on each side. This is the part of check 28 that works.
- **The declared-null escapes.** `none` is matched as a word, not a prefix, at all sites
  (`unattended.sh:2172`, `check-playbook.sh:320`, `:412`). Round-3 HIGH 3 has not come back.
- **The `--counts` refusal-to-print.** A playbook whose declaration the leg could not read gets no
  census line at all, and the caller's own "no count line" refusal is the honest outcome. Verified by
  the suite arm at `check-playbook.test.sh:296-299`.
- **The reverted exit-status read at the `pieces-complete` call site.** The commit message explains
  why it was measured and refused, the reason sits at the call site and in spec 6 rev-10, and the two
  refusals that DO invalidate a census reach the caller by other routes. Both routes checked. This is
  the right call, recorded in the right places.
- **`DOD_NO_OVERRIDE`.** `pieces-complete` and `authorization-reachable` are both in it and no waiver
  path reaches either. Nothing in this diff moved that.

## Recommendation

Fix BLOCKER 1 first and separately: it is four `sed` fragments in two files, it is live, and the
reproduction above is the acceptance test. Then the three gate defects (2, 3, 4) together, because
they are one class — every one of the three new gates is one spelling wide — and fixing them
individually invites a sixth round of the same conversation.

**The pattern to break is not the parser bug. It is that every repair so far has been written to the
INSTANCE the review named.** Round 3 fixed `head -1` at the call sites; round 4 fixed the terminator
test's position; this round fixed the comment strip's position. Each was correct, and each left the
next stage of the same pipeline untouched. The three new gates repeat that one level up: 28a polices
the spelling round 4 found, 28b the `sed` spelling round 4 found, 28c the lowercase `git` spelling
round 4 found. Before round 6, the useful question is not "what else is wrong with `declared_list`"
but **"what would this predicate refuse to see"** — asked of every predicate before it is armed, and
answered by running it over the real tree and printing hits AND near-misses, which §7 already requires
and which would have caught all three of these in minutes.

One concrete suggestion for that. Check 28's specimen lists are the right shape and the wrong width.
They should be **generated from the shipped template's own lines under systematic mutation** — value
deleted, comment removed, comment kept, bracket in a member, member moved to the next line — rather
than hand-listed one specimen per round as each defect is found. A generated specimen set is the only
version of this check that can catch a spelling nobody has thought of yet.
