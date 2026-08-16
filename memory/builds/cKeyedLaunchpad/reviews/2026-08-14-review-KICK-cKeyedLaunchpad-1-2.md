**Serves:** spec-audit KICK-cKeyedLaunchpad-1 KICK-cKeyedLaunchpad-2 KICK-cKeyedLaunchpad-3 KICK-cKeyedLaunchpad-4 KICK-cKeyedLaunchpad-6 KICK-cKeyedLaunchpad-7 TOOL-cKeyedLaunchpad-5  <!-- inferred: verdict-bearing pass over the set -->

## Verdict: CHANGES REQUESTED

**Target:** the cumulative diff landing on `main` — `main..HEAD` on
`branch/session-kickoff-skill-review-0c76ec`, 23 commits, 45 files, +3591/-349. The seven built
units of `cKeyedLaunchpad` (KICK-1..7 plus TOOL-5) plus their records: the content-keyed skill-install
check, the single-source manifest location list and the manifest's move to `memory/guides/`, the
three new ratchet checks (C7/C8/C9) and the sealed §A task region (C10) with its per-bullet cap (C11),
the `gotchas.py --for-paths` entrypoint, and the kickoff engine's own size gate.

**Scope.** Every changed file in the range, weighted toward the four that carry executable
consequence — `skills/session-kickoff/manifest-check.sh`, its self-test,
`tools/check-wiring.sh`, `tools/check-template-size.sh` — plus the two documents an adopter
actually executes, `WIRE-INTO-PROJECT.md` and `skills/session-kickoff/SKILL.md`. Records, specs and
generated map artifacts were read for consistency but not audited as deliverables.

**Method.** Findings were produced by parallel lenses over the diff, then every candidate went to an
adversarial skeptic whose default was refutation and whose verdict had to reproduce against the tree,
a scratch repository, or a live command. Verifier fan-out stayed inside
`memory/guides/REVIEW-PROTOCOL.md`'s at-most-5-total, at-most-5-concurrent budget.

**Shape:** raw 24, confirmed 22, refuted 2, unverified 0. **Precision 0.92.** The 22 confirmed carry
cross-lens duplicates — three defects were reached independently by three lenses each, two by two —
and dedupe to **12 distinct defects**.

**Severity split (distinct):** 0 blockers, 2 high, 8 medium, 2 low.

**Verdict rationale.** Nothing here blocks the design; two findings block the merge. **H1** makes a
SessionStart-driven check print a remedy that, if followed, breaks `/session-kickoff` machine-wide
once the worktree it names is removed — and the check cannot then report the damage it caused. **H2**
puts four brand-new checks into the `--staged` pre-commit leg that `WIRE-INTO-PROJECT.md` installs
unconditionally, so an adopter on the documented upgrade path can have every commit in their repo
blocked by a manifest region they were never told to add. Both are small edits; both should land
before this diff does. The remaining ten fold into edits and two test-path corrections.

---

## H1 (high) — `check_skill_install`'s remedy points the machine-global install at a throwaway worktree

**File:** `tools/check-wiring.sh:507` (MSYS branch) and `:509` (POSIX branch); `ROOT` set at `:25`.

`ROOT=$(git rev-parse --show-toplevel)` is the *current* worktree root. Inside a linked worktree —
which is where this repo does all feature work by convention (`memory/guides/SESSION-KICKOFF.md:50`
pins `.claude/worktrees/<branch-slug>/`; the pre-commit branch guard refuses primary-tree commits off
the default branch) — that is an ephemeral directory. The new check interpolates it straight into the
junction target.

Reproduced live from this worktree, `bash tools/check-wiring.sh --check` prints:

```
Fix: New-Item -ItemType Junction -Path "$env:USERPROFILE\.claude\skills\session-kickoff"
     -Target "C:\projects\coding-governance\.claude\worktrees\session-kickoff-skill-review-0c76ec\skills\session-kickoff"
```

The arm is content-keyed against tracked `skills/session-kickoff/*`, so it fires *precisely* on a
branch that edits the engine — i.e. from a worktree — and it runs at every SessionStart. The install
it repoints (`~/.claude/skills/session-kickoff`) is machine-global and outlives the branch. Follow the
printed command, land the branch, `git worktree remove`, and `/session-kickoff` is dead in every repo
on that node. Worse, `check_skill_install` returns early on `[ ! -d "$inst" ]`, so the verifier that
caused the breakage cannot detect it. The file's own comment justifies only that `--fix` must not
write out-of-tree; it never contemplates the printed target being disposable. Contrast the hooks arm
in the same output, which correctly names the primary tree.

**Fix.** Derive the primary checkout instead of `$ROOT` for the remedy target, and keep comparing
bytes against `$ROOT`:

```sh
PRIMARY=$(dirname "$(git rev-parse --path-format=absolute --git-common-dir)")
# or: PRIMARY=$(git worktree list --porcelain | sed -n '1s/^worktree //p')
```

then interpolate `$PRIMARY/$rel` into both `fix=` strings.

**Left-shift gate.** `tools/check-wiring.test.sh` gained seven arms in this diff and none of them runs
from a worktree. Add one: `git worktree add` a linked tree inside the fixture, run `--check` from it,
and assert the printed `Fix:` target is the *primary* tree's path. That single arm also covers any
future remedy string that reaches for `$ROOT` when it means the machine's canonical checkout.

---

## H2 (high) — C7/C8/C10/C11 execute in the `--staged` pre-commit leg, whose documented scope is still "C1 C2 C4 C6 + C5s"

**File:** `skills/session-kickoff/manifest-check.sh:13` (the stale header), with the four new checks at
`:161` (C7), `:173` (C8), `:193` (C10) and `:216` (C11) — all *above* the `if [ "$STAGED" = 0 ]` split
at `:310`.

C9 was deliberately kept out of the staged leg, and its comment at `:355-357` says why: "the
pre-commit hook runs that leg unconditionally on every commit in an adopting repo, and this question
is not one a single commit changes." The four checks added in this diff got no equivalent
consideration, and they are not stall-shaped questions either — C10 in particular fails on the
*working-tree* manifest regardless of what is staged.

Reproduced: a fixture repo with a `v1.3`-marked legacy manifest carrying no `<!-- kickoff:task -->`
region, with one unrelated, unwatched file staged, gives

```
MANIFEST check 10 FAILED — the manifest carries no sealed task region…    (exit 1)
```

`WIRE-INTO-PROJECT.md:367` installs `bash "$top/tools/manifest-check.sh" --staged || exit 1` as an
unconditional pre-commit hook, and `:523`/`:586` document overwriting the checker wholesale on kit
updates. An adopter who takes the documented upgrade path therefore has every commit in their repo
blocked until they retrofit §A — and the retrofit instructions reach them only through C2's message,
which is a different branch that this run never enters.

**Fix.** Move the C7/C8/C10/C11 blocks inside the `[ "$STAGED" = 0 ]` arm (or guard each with it), and
update the header inventory at `:4-6` and `:13` to name the checks the staged leg actually runs.

**Left-shift gate.** Two arms in `manifest-check.test.sh`: (a) `--staged` against a legacy manifest
with no sealed region and nothing watched staged → expect exit 0; (b) a header-parity arm that derives
the set of check ids reachable above the `STAGED` split and asserts it equals the set spelled on line
13, so the next check added above the split reds until the header follows it. (b) is the one that
actually holds — the split is invisible at the call site and this is the second time prose about it
has gone stale.

---

## M1 (medium) — C9's stall baseline is read out of the file C9 audits, and is never corroborated

**File:** `skills/session-kickoff/manifest-check.sh:384` (the count) and `:385` (the age), with `LBC`
read at `:257` and validated at `:373`/`:375`/`:381`.

`last-body-change` is checked for 40-hex shape, object existence and ancestry — never that the named
commit actually changed the manifest body. So:

```sh
sed -i 's|^last-body-change: .*|last-body-change: '"$(git rev-parse HEAD)"'|' <manifest> && git commit
```

zeroes both the ten-commit threshold and the ninety-day threshold with §B untouched. The manifest path
is not in this repo's own `watch` list (`memory/guides/SESSION-KICKOFF.md:5`), so the re-stamp commit
does not even count toward the next window: the reset is total. The repo's own fixture performs
exactly this move as setup (`manifest-check.test.sh:567-568`, `:585-586`, the `mkrepo c9n`
"rebaseline" step).

The sibling check in the same file does not accept its input on trust: C5 re-derives every candidate
stamp commit by comparing `blockstamp` at the commit against its parent (`:341-346`) precisely so body
decoys and block reorders cannot count. C9 has no equivalent, and this diff commits the gotcha class
that names it — `memory/gotchas/inputs-inside-the-subjects-reach.md`: "an input the subject controls is
not evidence; it is testimony."

The design comment at `:363-366` justifies *reading* the baseline rather than walking path history
(squash and rename survival), which is sound. It does not address validating the recorded sha, which
is the gap.

**Fix.** In the `else` branch at `:383`, require that the manifest BODY differs across `$LBC`: compare
`git show "$LBC:$MF"` against `git show "$LBC^:$MF"` with the `manifest-audit` block stripped (invert
the existing `awk '/<!-- manifest-audit/{f=1;next} f&&/-->/{exit} f'` slice), and `fail 9` when they
are byte-equal — a commit that only advanced the stamp is then not a usable baseline.

**Left-shift gate.** An arm in `manifest-check.test.sh` beside the existing C9 arms: re-stamp
`last-body-change` to HEAD with the body untouched, commit, expect `check 9 FAILED`. It is the exact
sequence the current fixture uses as *setup*, so the arm is three lines.

---

## M2 (medium) — `WIRE-INTO-PROJECT.md` §4 never names the new mandatory `last-body-change`

**File:** `WIRE-INTO-PROJECT.md:345` (step 2's key list), retrofit recipe at `:382-383`.

Step 2 enumerates `watch`, `verify-paths`, `last-audit` and stops. `manifest-check.sh:263` hard-fails
C2 without `last-body-change`. `grep -rn 'last-body-change\|BODY_CHANGE' WIRE-INTO-PROJECT.md` returns
nothing — the runbook, which is the file an agent executes, never names the key.

The "per the template's Customize notes" delegation partly covers a fresh instantiation
(`MANIFEST-TEMPLATE.md:129` documents `{{BODY_CHANGE_SHA}}`), but the retrofit path has no template to
consult: §4's recipe says only "derive watch/verify-paths as in step 2 above". And C2's own remedy
string routes the adopter to that section — "Full recipe: coding-governance/WIRE-INTO-PROJECT.md §4"
(`manifest-check.sh:241`) — so the failure message points at the section that omits the key the failure
is about.

**Fix.** Add `last-body-change` to the §4 step 2 key list with its stamp rule: the full sha of the
commit where the BODY was last genuinely revised; at instantiation, the same sha as `last-audit`.

**Left-shift gate.** See M4 — one runbook-parity leg covers M2, M3 and M4 together.

---

## M3 (medium) — §4 still advertises a repo-root `SESSION-KICKOFF.md` that both implementations dropped

**File:** `WIRE-INTO-PROJECT.md:331`.

The chain now reads: "the locations `bash tools/manifest-check.sh --locations` prints, in order →
`SESSION-KICKOFF.md` → else it greps `docs/` + root for the `governance-template:` marker … Write the
manifest to one of those paths so it resolves."

The bare root spelling is a leftover: commit `24f3991` replaced the first three entries of the old
four-entry chain with the `--locations` delegation and left the fourth dangling after the arrow.
Neither implementation honours it — `MANIFEST_LOCATIONS` (`manifest-check.sh:30`) is exactly
`memory/guides/SESSION-KICKOFF.md .claude/SESSION-KICKOFF.md`, and `SKILL.md` Step 2's post-`--locations`
list is only the skill's own base dir and the `governance-template:` marker grep, which hunts the
*playbook* marker, not a manifest. An adopter who takes the sentence at its word and writes
`<project>/SESSION-KICKOFF.md` gets exit 2 ("no kickoff manifest at …") from the gate and an engine
that never loads the project layer.

This is the two-answers-to-one-question defect the `--locations` verb was introduced to end,
surviving in the one file the verb's own comment (`:21`) names as the reason it exists.

**Fix.** Delete the ` → \`SESSION-KICKOFF.md\`` term so the chain is: `--locations` output, then the
`governance-template:` marker fallback (and mark that fallback engine-only, as `SKILL.md` now does).

**Left-shift gate.** See M4.

---

## M4 (medium) — the runbook still stamps `kickoff-manifest: v1.1`, in two places, against a v1.3 kit

**File:** `WIRE-INTO-PROJECT.md:391` (retrofit step 6) and `:522` (the adopted-tree diagram).

`KIT_MANIFEST_VERSION="1.3"` (`manifest-check.sh:18`) and `MANIFEST-TEMPLATE.md:3` carries
`kickoff-manifest: v1.3`, but step 6 still instructs "Bump the manifest marker to
`kickoff-manifest: v1.1` **LAST**", and the tree diagram — a line this diff edited, moving the path to
`memory/guides/` while leaving the parenthetical alone — still reads `(v1.1: manifest-audit block)`.

`check-kit-versions.sh:33-39` compares only the constant against `MANIFEST-TEMPLATE.md`; no gate reads
this file for version markers (`check-install-prefix.sh` reads it for path spellings only), so this
third spelling drifts ungated. An adopter following step 6 stamps v1.1 into a manifest instantiated
from the v1.3 seed and earns `WARN: manifest format v1.1 < kit v1.3` on every kickoff forever
(`manifest-check.sh:124-126`) — on a manifest whose stamp predates the `last-body-change` key and the
sealed-region contract it claims to have retrofitted.

**Fix.** Update both lines to v1.3 (`(v1.3: manifest-audit block + sealed §A task region)`), or drop
the version from `:522` entirely so the annotation cannot rot again.

**Left-shift gate (covers M2, M3 and M4).** One runbook-parity leg — the cheapest place is an extension
of `tools/check-kit-versions.sh`, which already owns the marker/constant pair:

1. every `kickoff-manifest: v<x>` spelled in `WIRE-INTO-PROJECT.md` equals `KIT_MANIFEST_VERSION`;
2. every manifest path the runbook tells an adopter to write is a member of
   `manifest-check.sh --locations`;
3. every audit key C2 hard-requires appears in §4 step 2.

All three are greps against files the gate already reads. The class here is not three typos, it is that
the runbook is an unexecuted second copy of contracts the code owns — nothing gates prose in that file
today, and this diff put three fresh disagreements into it.

---

## M5 (medium) — `SKILL.md`'s new gotchas step reuses `<KIT>`, a token the same document binds to the memory-recall kit

**File:** `skills/session-kickoff/SKILL.md:175`.

`<KIT>` appears exactly three times in the file: line 175 (`python <KIT>/gotchas.py --for-paths …`) and
lines 181/184, where its *only* binding is given as "whichever of `memory-recall/` or
`tools/memory-recall/` holds `query.py`". There is no earlier glossary and no token convention in the
front matter or Steps 0-2.

`gotchas.py` ships in the memory-tree kit (`tools/memory-tree/gotchas.py`, whose own usage line spells
that path); `tools/memory-recall/` contains no such file. An agent resolving the token as the document
defines it runs the new command against a directory that does not hold the script — so
`--for-paths`, the entrypoint this diff added to `gotchas.py` specifically for this step, is dead
plumbing from the engine's side. The paragraph introducing it is even scoped "when the project ships
the memory-tree kit", which makes the collision plain on a careful read and invisible on a fast one.

**Fix.** Give the block its own resolution clause, mirroring the memory-recall one: "`<MT>` is whichever
of `memory-tree/` or `tools/memory-tree/` holds `gotchas.py`", and use `python <MT>/gotchas.py
--for-paths …`.

**Left-shift gate.** A grep leg over `skills/session-kickoff/SKILL.md`: every `<TOKEN>/<script>` command
must have `<TOKEN>` bound in the same document to a kit that actually contains `<script>` in this repo.
Twenty lines of shell, and it catches the whole class — an engine that instructs an agent to run a path
is only as good as the path resolving.

---

## M6 (medium) — C10's byte-exactness sentinel is applied after the newlines it defends have been stripped

**File:** `skills/session-kickoff/manifest-check.sh:211`, with the captures at `:207` and `:210` and the
comment at `:201-203`.

`c10have=$(region …)` and `c10want=$(… | region …)` both have their trailing newlines stripped by
command substitution *before* `"${c10have}X" != "${c10want}X"` is formed, so the sentinel is appended to
an already-stripped string and defends nothing. The comparison behaves identically to comparing the bare
variables.

Reproduced against the real script: a manifest whose sealed region carries two trailing blank lines
before `<!-- /kickoff:task -->` (confirmed with `cat -A`) passes at exit 0, silently. A leading blank
line, or any text bullet, correctly reds. Nothing else catches it — C1 is placeholder-shaped, C8 is
per-line length.

The prior art the comment credits does it correctly, with the sentinel *inside* the substitution:
`tools/memory-tree/kit-dogfood-parity.test.sh:66`, `out=$( cat "$1" || exit 1; printf X )`. This
borrowing copied the comment but not the one placement that made the idiom work, and the comment now
asserts a protection the code does not provide. Impact is bounded — whitespace-only drift inside the
region, no field value can change this way — but the seal's stated "not hand-authorable" guarantee is
false as written.

**Fix.** Capture with the sentinel inside, preserving the exit status the `if !` at `:207` depends on:

```sh
c10have=$(region "$MF" '<!-- kickoff:task -->' '<!-- /kickoff:task -->' 2>/dev/null; s=$?; printf X; exit $s) || fail 10 "…"
c10want=$(printf '%s\n' "$TASK_SKELETON" | region /dev/stdin '<!-- kickoff:task -->' '<!-- /kickoff:task -->' 2>/dev/null; printf X)
[ "$c10have" = "$c10want" ] || fail 10 "…"
```

**Left-shift gate.** The C10 arms at `manifest-check.test.sh:589-623` cover an absent region, a
one-character edit, a transposed pair and CRLF — every case *except* the one the sentinel exists for.
Add a trailing-blank-line arm expecting exit 1. The gap was invisible from both directions: the comment
claimed the protection and no arm asked for it.

---

## M7 (medium) — self-test case 30's body decoy is written to a path `write_manifest` no longer creates

**File:** `skills/session-kickoff/manifest-check.test.sh:406`.

`write_manifest` (`:71-102`) writes only `$1/memory/guides/SESSION-KICKOFF.md` after this diff's move.
Case 30 appends its `last-audit:` decoy to `$R/SESSION-KICKOFF.md` — the repo root — so `>>` creates a
stray file that `MANIFEST_LOCATIONS` never reads (the file is visibly present in the fixture listing).

Ran four variants of the case shape: (A) decoy at the root, as the suite does it; (B) no decoy at all,
i.e. case 17; (C) decoy appended to the real manifest, as intended. All produced byte-identical output
— `MANIFEST check 5 FAILED — staged changes touch watched files: Makefile`, exit 1. The arm is
therefore indistinguishable from case 17 and proves nothing beyond it: the `blockstamp()` block-scoping
at `:150-153` that makes a *body* `last-audit:` decoy fail to satisfy C5s is unarmed, and a regression
letting a body line count would still pass this suite. `check-arms.py` still scores the branch as armed,
because the failure text is asserted — the meta-gate cannot see a fixture that passes by finding
nothing.

**Fix.** Change the append target to `"$R/memory/guides/SESSION-KICKOFF.md"`, matching the other 20 call
sites the move updated.

**Left-shift gate.** See M8.

---

## M8 (medium) — self-test case 18's co-staged manifest edit lands in the same stale root path

**File:** `skills/session-kickoff/manifest-check.test.sh:264`.

Same root cause as M7, distinct arm and distinct lost coverage. The `unrelated trap note` is appended to
`$R/SESSION-KICKOFF.md`, so no co-staged manifest edit ever reaches the manifest under test. Reproduced:
the as-written variant, the intended variant, and the bare no-edit case 17 all print the identical
`check 5 FAILED` / exit 1. The arm no longer proves the proposition it is named for — that a staged
manifest edit which does not move the stamp still fails C5s — and a regression to "any staged manifest
edit satisfies C5s" would pass.

**Fix.** Change the append target to `"$R/memory/guides/SESSION-KICKOFF.md"`.

**Left-shift gate (covers M7 and M8).** Add a preamble assertion to the suite: after each fixture is
built, fail if any path outside `MANIFEST_LOCATIONS` matching `SESSION-KICKOFF.md` exists in `$R`. Two
lines, and it is the only mechanical defence against a bulk path move that updates 20 call sites and
misses 2 — the arms stay green either way, so nothing else can notice.

---

## L1 (low) — `check-template-size.sh`'s failure remedy names the playbook's companion, on a script that now gates two files

**File:** `tools/check-template-size.sh:31-32` (the remedy), `:7-8` (the usage header).

`tools/gate-legs.json` adds a second consumer — `bash tools/check-template-size.sh
skills/session-kickoff/SKILL.md 18432` — and the positional at `:19` exists precisely so "a second file
can ride this script". The failure block is unconditional and playbook-only: forcing it
(`bash tools/check-template-size.sh skills/session-kickoff/SKILL.md 100`) prints "move an
activity-scoped section to `parallel-coding-governance.domain-rules.md` … per the v2.3 pattern" — a
companion the kickoff engine has no relationship to.

`SKILL.md` is 17502 LF-normalized bytes against the 18432 cap: 930 bytes of headroom, 95.0% used. This
remedy will fire, on the one file the new leg exists to gate, and send its author to the wrong document.
The usage header at `:7-8` also documents only the `MAX_BYTES` env form and not the positional the new
leg depends on — though the comment block at `:14-18` explains it at length, so only the header is
stale.

**Fix.** Make the remedy file-agnostic ("trim non-instructional prose, or externalize a section into a
companion this file points at") or branch it on `$name`; add the
`tools/check-template-size.sh <file> [<max-bytes>]` form to the header.

**Left-shift gate.** Nothing worth building. If anything: a one-line arm asserting the failure output
names no file other than the one being gated. Weigh that against just writing a remedy that does not
name a file.

---

## L2 (low) — `SKILL.md` Step 2's `--locations` fallback covers an unreachable copy but not a pre-v1.3 one

**File:** `skills/session-kickoff/SKILL.md:75`.

The fallback clause reads "If no copy is reachable…". The commoner case is a copy that *is* reachable
and does not know the verb: `git show 7e0b779:skills/session-kickoff/manifest-check.sh` is
`KIT_MANIFEST_VERSION=1.1` with an arg loop whose default arm is `*) MF="$a"` and no `--locations` case,
so it resolves `--locations` as a manifest path and exits 2 with

```
MANIFEST env ERROR — '--locations' not found (tried the repo root, then <cwd>)
```

— a message about a missing *manifest*. Step 2b's resolution order tries `tools/`/`scripts/manifest-check.sh`
*before* the copy shipped beside the skill, so an already-adopted repo hits the stale copy first, and the
kit acknowledges that population elsewhere (the `ver_older` forward-drift WARN; `scripts/manifest-check.sh`
described as "the pre-2026-08 default, still honoured"). An agent reading that error can plausibly
conclude the repo has no manifest and take the Scaffolding path, creating a duplicate beside the
existing one. Step 3's `--task-skeleton` call has the same dependency with no fallback at all.

**Fix.** Extend the sentence: "If no copy is reachable, **or the copy exits non-zero on the verb (a
pre-v1.3 kit)**, the in-repo order is `memory/guides/` then `.claude/`." Same for the `--task-skeleton`
call in Step 3.

**Left-shift gate.** Prose in a Skill is not worth a gate of its own. The durable answer is the version
WARN the kit already emits — make Step 2's fallback trigger on *any* non-zero exit rather than on
reachability, and the class closes without a new leg.

---

## What the diff got right

Worth recording, because two of these are why the review found what it found:

- C5's stamp corroboration (`:341-346`) is the correct shape, and it is the standard M1 is measured
  against. The technique was already in the file; C9 just did not reach for it.
- C9's exclusion from the staged leg, with its reason written down at the call site (`:355-357`), is
  exactly the note that made H2 legible. The four new checks needed the same sentence and did not get it.
- `gotchas.py --for-paths` is the right entrypoint for a pre-diff READY card — the only defect is which
  token the engine spells to reach it (M5).
- The `--locations` verb genuinely single-sources the location list for both implementations. Its three
  surviving contradictions (M3, M4, and M2's missing key) are all in the one file nothing gates.
