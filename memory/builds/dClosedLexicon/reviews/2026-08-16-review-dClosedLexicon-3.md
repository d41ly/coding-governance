# review-dClosedLexicon-3 — Tier-2 code review of TOOL-dClosedLexicon-1 (the lexicon kit + the placeholder-catalogue gate)

## Verdict: BLOCKED — 1 blocker, 1 high

**Subject:** commits `0007b35` (land UNARMED) + `b062615` (ARM) — `tools/lexicon/`,
`tools/check-placeholders.sh`, `tools/gate-legs.json`, `.lexicon.conf`, `AGENTS.md` · streams
`tooling` · node d · 2026-08-16

**Binding spec:** `spec/2026-08-16-spec-dClosedLexicon-1.md` at rev-6, whose Rollout this two-commit
landing follows. **Folds:** `reviews/2026-08-16-review-dClosedLexicon-2.md` (the M4 spec audit, nine
findings).

## Review shape

| | |
|---|---|
| raw findings | 25 |
| confirmed (survived an adversarial skeptic) | 22 |
| refuted | 3 |
| unverified / outstanding | 0 |
| precision | 0.88 |

The 22 confirmed findings collapse to **13 distinct defects** — four independent verifiers reproduced
the `.lexicon.conf` LAYERS defect (ids 1, 8, 14, 19), three reproduced the marker-lockstep hole
(ids 9, 15, 23), and three more pairs converged (7+20, 2+25, 18+24, 6+12). Duplicates are recorded
under each defect rather than repeated as separate rows; the convergence is itself signal — the
LAYERS row was found by four verifiers running four different reproductions.

**Scope note.** Per the review brief, the security model is out of scope: these are local developer
gates over tracked files in a governance repo, with no network surface, no untrusted input and no
auth. No threat-model findings were sought or manufactured. The lenses were CORRECTNESS, VACUITY and
INTEGRATION SEAMS. The full bar is 60/60 green, so every finding below explains why a **green gate is
wrong**, not merely that something is unchecked.

**The headline.** The kit's own module docstring (`tools/lexicon/lexicon.py:23-27`) names
`vacuous-selector-empty-population` as its dominant failure mode, and arms two defences against it
(`DEAD PROBE` for extractors, `P3 NOT ARMED` for an empty `LAYERS`). The blocker below is that exact
class, landing through the one gap between those two defences: a `LAYERS` rule that is **non-empty
but unmatchable**. `NOT ARMED` tests emptiness; nothing tests reachability. Seven of the thirteen
defects (B1, H1, M3, M4, M5, M6, plus L2) are vacuity or measured-against-nothing findings — the
diff's own stated discipline, applied one level short.

---

## BLOCKER

### B1 — The only armed `LAYERS` rule is unmatchable by construction; `LAYER_OFFENDER_PIN="0"` is unfalsifiable

**`.lexicon.conf:67`** (rule) · **`.lexicon.conf:32`** (the pin it makes vacuous) · duplicates: ids 1, 8, 14, 19

The single declared forbidden import direction is:

```
LAYERS:
  tools/lexicon/* -> tools/codebase-map/*
```

It can never fire. `tools/lexicon/lexicon.py:237` matches the `to` side against
`target.replace(".", "/")` — the import **namespace** — while the glob is spelled as a **repo path**.
A Python module name cannot contain a hyphen, so the only string that could match
`tools/codebase-map/*` is `tools.codebase-map.…`, which is a `SyntaxError`, not an import. There are
no `.js` files under `tools/lexicon/`, so the js-regex extractor cannot reach the `frm` side either.
The target space and the glob space are **disjoint by construction**.

Reproduced four times, independently, including with the exact violation the conf's own comment
(`.lexicon.conf:61-67`) says this rule is "the machine-checkable form of":

- scratch repo + real `.lexicon.conf` + `tools/lexicon/violator.py` containing `import map_lib` →
  0 P3 rows, `lexicon OK`, rc 0.
- scratch repo + real kit + real `tools/codebase-map/map_lib.py` + `tools/lexicon/leak.py` doing
  `sys.path.insert(0, …/codebase-map); import map_lib` → `lexicon OK`, rc 0.
- `from tools.codebase_map import map_lib` (underscore spelling) → also no match.
- Direct probe: `_glob_match('map_lib', 'tools/codebase-map/*')` = `False`;
  `_glob_match('tools/codebase_map', 'tools/codebase-map/*')` = `False`.

**Why the green run is wrong, not merely uninformative.** Four load-bearing claims are discharged by
a declaration that cannot fire:

1. `LAYER_OFFENDER_PIN="0"` (`.lexicon.conf:32`) is pinned over the empty set and stays green no
   matter what the lexicon imports.
2. The `P3 NOT ARMED` refusal (`lexicon.py:189-192`) — which exists precisely so "a satisfied
   predicate and one never asked must not share an exit code" — is satisfied by a rule that can
   never be asked. It tests emptiness, not reachability.
3. `tools/lexicon/kit.toml`'s `lexicon-layers` hole (`blocks_gate = true`) is discharged by a
   decorative row.
4. The new `AGENTS.md` charter bullet asserts the pins are measured against this corpus; for this
   pin that is a measurement over the empty set. `memory/map/features/lexicon.md:122-125` records
   the opposite conclusion ("Adequate for the layer directions declared here") — falsified.

The self-containment rule that `subtokens.py` exists as a PORT to honour therefore has **no**
machine-checkable form, despite the spec naming this exact row as that form
(`spec-dClosedLexicon-1.md:165,171`) and the leg riding the merge bar (`tools/gate-legs.json:543`).

The harness cannot see it: both P3 arms in `selftest.py:105-109` use `core/* -> adapters/*` with
`import adapters.db`, where the fixture's package name coincidentally equals its directory name and
carries no hyphen. The green arm does not generalise to the shipped declaration.

**Fix.** Two parts, and the second is the one that matters:

1. *Immediate* — spell the row in the namespace the engine actually matches:
   `tools/lexicon/* -> map_lib*` (verified: `_glob_match('map_lib', 'map_lib*')` is `True`), or fix
   the engine per H1 and keep the path form.
2. *Structural* — close the hole so this cannot recur silently. Add a **DEAD RULE** arm beside the
   existing DEAD PROBE arm: a `LAYERS` row whose `from` glob selects tracked files but whose `to`
   glob matches nothing in the extracted target namespace is a **refusal**, not a pass. Separately,
   refuse a `to` glob containing a character no declared parser language's import target can produce
   (a `-` for Python).

**Left-shift gate.** `tools/lexicon/selftest.py` gains an arm that drives P3 through a rule of *this
repo's own declared shape* — plant the real violation (`sys.path` insert + bare `import map_lib`
under `tools/lexicon/`) and assert a `P3 layer` line. Today every P3 arm uses a fixture whose module
names mirror repo paths, which is why the shipped declaration's shape has never been exercised. Pair
it with the DEAD RULE arm above so an unmatchable rule reds instead of reading as armed.

---

## HIGH

### H1 — The layer predicate compares a dotted module name to a repo-path glob; both commonest real import shapes escape it

**`tools/lexicon/lexicon.py:237`** · duplicates: ids 7, 20

```python
if _glob_match(rel, frm) and _glob_match(target.replace(".", "/"), to):
```

The `frm` side is a repo path (correct). The `to` side is a raw import target run through a blanket
dot-to-slash substitution and then matched against a repo-path glob. That only works when a project's
module names happen to mirror its repo paths **from the root**. Distinct from B1 in artifact and in
fix: B1 is gov's declared rule being unfireable; this is the engine being structurally incapable,
which every adopter inherits.

Reproduced in throwaway repos:

- **JS, the documented example.** `LAYERS: src/core/* -> src/adapters/*` with `src/core/a.js` doing
  `import db from '../adapters/db.js'` — verbatim the example `tools/lexicon/LEXICON.md:55-57`
  prints — yields target `../adapters/db.js`, which the substitution mangles into `///adapters/db/js`.
  Matches nothing. `lexicon OK`, rc 0. The idiomatic relative specifier — the dominant JS import
  form — is unmatchable.
- **Python, flat `sys.path` layout.** `import map_lib` after a `sys.path.insert` yields `map_lib`;
  no `<dir>/<dir>/*` glob can match it. This is the convention across all nine `tools/codebase-map`
  consumers and both `tools/lexicon` ones.
- **Python, `src/` layout.** `from adapters import db` yields the bare module and escapes.

The `js-regex` sentinel arm in `selftest.py` scores a pass because imports are **extracted**, not
because they are usable by the only predicate that consumes them.

*Minor overstatement corrected during verification:* a bare non-relative JS specifier such as
`'src/adapters/db.js'` does match, so JS is not inert in literally every shape — only in the
idiomatic one.

**Fix.** Resolve each import target to a tracked repo-relative path before globbing:

- Python — try `<dotted>.py` and `<dotted>/__init__.py` against the repo root and against the
  importing file's package dir, then fall back to a tracked-basename lookup
  (`map_lib` → `tools/codebase-map/map_lib.py`).
- JS — `posixpath.normpath(join(dirname(rel), spec))` for a relative specifier; leave a bare package
  specifier unresolved.
- Treat an unresolvable target as **reported dark**, not a silent pass.

**Left-shift gate.** Two selftest arms that must red: a relative JS import crossing a declared layer,
and a flat `sys.path` Python import crossing one. Both fail today. Add the live non-empty assertion
from B1's fix — for each declared `frm` glob, assert at least one tracked file matches it *and* that
the selected file set contributed at least one import target.

---

## MEDIUM

### M1 — `govkit apply` overwrites the three adopter-owned waiver registries on every re-apply

**`tools/lexicon/kit.toml:17`** (the shadowed rule) · **`tools/lexicon/kit.toml:9-11`** (the shadowing one) · id 10

`kit.toml` declares `include = "**"` / `role = "engine"` **before** the `project-owned` rule naming
the three `lexicon-*-waivers.txt`. `govkit.py` iterates file rules in declaration order; a `**`
include expands to every tracked path under `home` (`govkit.py:801-803`), waivers included, and each
is written with an unconditional `dp.write_bytes(data)` (`govkit.py:828`) — the `seed` exists-check
at `:825` does not apply to `engine`. The second rule contributes nothing: `project-owned` is not in
`LANDABLE_ROLES = ("engine","seed")` (`:686`), so it is skipped at `:798` and cannot un-claim
anything. govkit validates no role name (only `merged` is named and refused, `:779`), so the mistake
is silent, and `project-owned` appears nowhere else in the repo's descriptors.

Reproduced end-to-end, twice: `govkit intake` + `apply --kits lexicon` into a scratch target landed
12 files (every tracked lexicon path, waivers included); appending `my_deliberate_exception` to the
target's `lexicon-verb-waivers.txt` and re-applying (authorized by the target's own receipt via
`foreign_kit_present`, `:701-712`) landed 12 files again and the adopter's line was gone.

That is exactly what the comment at `kit.toml:13-17` says must never happen. The consequence
compounds: because the pins are measured **with** those waivers in force, an upgrade wipes the record
and the adopter's bar then reds with offenders over pin and no record of why they were excused. Every
other entry protecting target-owned bytes (`kickoff-manifest.kit.toml`, `playbook.kit.toml`) uses
explicit include lists precisely so nothing shadows them.

*Side observation:* `plan` (`planned_writes`, `:531-568`) does not expand `**`, so it printed 3 writes
where `apply` wrote 12 — the read-only verb **understates** the blast radius rather than warning
about it.

**Fix.** Drop the `**` rule for this entry, list the engine files explicitly (as the flat entries do),
and give the three waiver files `role = "seed"` — govkit already honours seed with
`if role == "seed" and dp.exists(): continue`.

**Left-shift gate.** `govkit selfcheck` rejects an unknown role name, and flags any rule whose
sources are already claimed by an earlier `**` rule in the same entry. Add a `govkit/selftest.py` arm
that applies twice with a mutation in between and asserts the project-owned bytes survive.

### M2 — `--scaffold` can write a `.lexicon.conf` its own single reader refuses to parse

**`tools/lexicon/scaffold_lexicon.py:84`** (unfiltered seed) · **`:112`** (the emitted row) · duplicates: ids 2, 25

`leading_verb` (`subtokens.py:37`) does `lstrip('_')` then splits; `_SUBTOKEN_RE`'s `[0-9]+`
alternative makes `_2fa_verify` yield the leading token `'2'`. `scaffold_lexicon.py:84` takes
`counts.most_common(SEED_VERBS)` with **no alphabetic filter** and emits a bare `  2` row.
`lexicon_conf.py:103-104` then raises `ConfError: a verb must be alphabetic, got '2'`.

Reproduced end to end: `adopt-lexicon.sh --scaffold` exits 0 and prints "wrote .lexicon.conf marked
PROPOSED"; the very next `python tools/lexicon/lexicon.py` dies rc 1 with
`.lexicon.conf:37: a verb must be alphabetic, got '2'`, and `adopt-lexicon.sh --check` reds with
"does not parse". A writer emitting a file its own single reader rejects is a real contract break,
and `_2fa_verify` / JS `_2foo` are legal identifiers — most reachable in a small adopter corpus where
every distinct leading token falls inside the top 25, i.e. exactly the fresh-adopter case.

*One sub-claim was checked and is wrong:* the unratified-seed refusal at `adopt-lexicon.sh:76` **does**
still speak — line 69 only sets `fail=1` and falls through, so both messages print. It does not change
the defect.

**Fix.** `seeded = [v for v, _n in counts.most_common(SEED_VERBS) if v.isalpha()]`. Non-alpha tokens
then correctly remain in `verb_offenders` (line 86 subtracts the seeded set), so they are still
counted against the pin rather than laundered — only the unparseable row disappears.
(`subtokens.leading_verb`'s docstring also claims `1` yields `""`; it yields `"1"`.)

**Left-shift gate.** The scaffold path is genuinely unexercised — there is no `tools/lexicon/*.test.sh`,
`selftest.py` never invokes `--scaffold`, and no gate leg runs it. Add a scaffold arm: run `--scaffold`
in a throwaway repo whose corpus contains `def _2fa_token()`, then assert the written conf parses
through `load_conf` and that `--check` reds **only** on the unratified stamp. That single arm covers
M2 and M3 together.

### M3 — `SUFFIX_OFFENDER_PIN` is a hardcoded `"0"` under a comment claiming all three pins were MEASURED

**`tools/lexicon/scaffold_lexicon.py:100`** (the literal) · **`:97-98`** (the comment it sits under) · id 3

The scaffolder writes "MEASURED against this corpus at scaffold time. Shrink-only: the count may
fall, never rise." and then emits `SUFFIX_OFFENDER_PIN="0"` as a literal directly beneath it. The
claim is false only for this key: `VERB_OFFENDER_PIN` is genuinely derived at line 86, and
`LAYER_OFFENDER_PIN="0"` is legitimately zero because `LAYERS` ships empty by design.

Reproduced: on a fixture carrying `class FooManager` and `class BarHelper`, `--scaffold` prints
"2 type definition(s) scanned", writes `SUFFIX_OFFENDER_PIN="0"`, and the engine then reds with
"suffix offenders 2 over pin 0". The measurement machinery already exists and is discarded —
`types_` is extracted at `:77` and `types_seen` accumulated at `:78`, used only in the summary print.

The same false claim is repeated in `tools/lexicon/kit.toml:79` ("The three offender pins are
MEASURED against the adopting corpus at scaffold") and `adopt-lexicon.sh:15` ("Pins are MEASURED
against the adopting corpus, never inherited"). Any real adopter with legacy `*Manager`/`*Handler`
types gets a post-curation gate red on day one whose only apparent remedy is **raising** a pin the
file's own comment declares shrink-only — the one edit direction the design forbids.

**Fix.** Measure it the way the verb pin is measured: while walking definitions, count definition-site
type names ending in a `BANNED_SUFFIXES` token (reuse the predicate from `lexicon.py:229`) and emit
that count. Leave `LAYER_OFFENDER_PIN="0"` literal but move it out from under the MEASURED comment,
and correct the claim in `kit.toml:79` and `adopt-lexicon.sh:15`.

**Left-shift gate.** The scaffold arm from M2, extended: the fixture carries a `*Manager` type, and
the arm asserts the scaffolded conf's `SUFFIX_OFFENDER_PIN` equals the count the engine then reports —
i.e. that a freshly scaffolded, freshly ratified conf is **green on its first run**. That single
invariant is the right gate for M3 and M4 both.

### M4 — `VERB_OFFENDER_PIN` is measured against the UNCURATED seed, and there is no re-measure verb

**`tools/lexicon/scaffold_lexicon.py:86`** · id 11

`verb_offenders` counts definitions whose leading token is outside the 25-row `seeded` list. But
`LEXICON.md:36-37` and `README.md:64-68` both mandate **deleting** rows from that seed before
ratifying, and every deleted row moves its whole definition population into the offender set. The pin
is therefore stale by construction the moment the adopter follows the documented next step.

This repo's own conf records the consequence: `--scaffold` here prints
`25 verb(s) proposed from 584 definition(s); VERB_OFFENDER_PIN=300`, and the seed contains exactly
the ten non-verbs the landed conf names (`t do git kit signal bounded all repo is no`). The curated
table's actual offender count is **412** (`lexicon.py --list | grep -c 'P1 verb'`), and
`.lexicon.conf:30` pins 412 with the comment "MEASURED against this corpus **after curation**" — a
hand re-measurement, because the tool offers none. `lexicon.py main()` accepts only `--check|--list`,
and `adopt-lexicon.sh:93-97` refuses to re-scaffold over an existing conf.

So the shipped path deterministically leaves the pin low (300 vs 412 here), the first gate run reds,
and the only remedy is raising a pin every doc calls shrink-only.

**Fix.** Add `bash tools/lexicon/adopt-lexicon.sh --measure`, which re-derives the three pins from the
**current** conf reusing `lexicon.py`'s own counting path (not a second implementation) and rewrites
the three pin lines. Make it the discharge command for the `lexicon-pins` hole, and change the
scaffolded comment from "MEASURED at scaffold time" to "PROVISIONAL — re-run `--measure` after
curating the table", so the shrink-only rule starts from the ratified table rather than the seed.

**Left-shift gate.** See M3's gate — "a freshly scaffolded, curated, ratified conf is green on its
first engine run" covers this. Add a second arm asserting `--measure` is idempotent and that a pin it
writes is never larger than the one it replaces (the shrink-only direction, enforced rather than
documented).

### M5 — `check-placeholders` catalogue coverage is one-directional: a catalogue entry naming a dead placeholder passes green

**`tools/check-placeholders.sh:75-77`** · id 4

Arm 1 loops only over the **measured** set and greps each into the catalogue; there is no reverse
loop anywhere in the script. Arm 2 (`tally_for`, `:80-85`) reads only the `### In \`<file>\` — <n>`
headings and never parses the bullet lists. So the catalogue can name a placeholder that exists in
neither shipped source and the gate stays green — against a script whose own line 2 states its
subject as "the playbook's placeholder catalogue agrees with the playbook".

Reproduced: in a scratch copy of the three shipped files, replacing `{{CI_FILE}}` in the template and
bumping the heading 23 → 22 leaves `customize.md` still listing `{{CI_FILE}}` as a placeholder to
fill, and the gate prints `check-placeholders OK — 22 + 15 placeholders catalogued`, rc 0.

This is the inverse of the standard the repo already holds itself to: `AGENTS.md` describes the
sibling codebase-map gate as failing on "any unclaimed new key AND any claim naming a dead key (the
map cannot rot into fiction)". The deployer consequence is concrete — the catalogue tells a one-time
deploy agent to gather a value, possibly an *(ask user)* one, for a placeholder that does not exist.
No dead entry exists today (37 catalogued, 37 used, both `comm` sides empty), so this is a latent
one-directional gap rather than a live wrong number.

**Fix.** Add a fifth arm: extract `\{\{[A-Z][A-Z0-9_]*\}\}` from `$CATALOGUE` and red on any token not
present in `$t_set ∪ $c_set`, message `CATALOGUED BUT DEAD`. Verified empty (green) against the tree
as it stands, so it lands without a red.

**Left-shift gate.** A negative fixture arm in `check-placeholders.test.sh` whose catalogue names a
placeholder absent from both sources, asserting the `CATALOGUED BUT DEAD` message.

### M6 — The marker-lockstep arm counts DISTINCT markers across both files, so a file with no marker passes as "agreeing"

**`tools/check-placeholders.sh:113-121`** · duplicates: ids 9, 15, 23

```sh
markers=$(grep -hoE '<!-- governance-template: v[0-9]+\.[0-9]+ -->' "$TEMPLATE" "$COMPANION" | sort -u)
n_markers=$(printf '%s\n' "$markers" | grep -c . || true)
if [ "$n_markers" -ne 1 ]; then
```

`grep -h` across both files plus `sort -u` collapses to one line whenever **exactly one** file carries
a marker, and `-ne 1` is the only test. Reproduced three times: deleting the
`<!-- governance-template: v2.8 -->` line from `parallel-coding-governance.domain-rules.md` makes the
gate print `check-placeholders OK — 23 + 15 placeholders catalogued, 1 shared and declared, markers
agree at <!-- governance-template: v2.8 -->`, rc 0.

Deleting a marker (a rewrite, a section move) is the most likely way the two carriers fall out of
lockstep, and the companion has no other consumer — `govkit`'s `playbook.kit.toml:6` takes
`version_from` the **template** only. So a dropped companion marker is invisible to the whole bar
while the leg's own header (`:15`) states its job as "the two marker-carrying files agree". This is
the identical hole `tools/check-kit-versions.sh:66-70` already records paying for: "a shipped doc
that self-identifies as nothing cannot be caught by any comparison."

The same script applies the opposite discipline 47 lines earlier (`:63-70`: a zero measurement is its
own arm), so this is an inconsistency inside one file, not a design choice.

*Also dead:* the `|| echo '(none)'` fallback at `:118` never fires — `||` binds to the `grep | head`
pipeline whose status is `head`'s, which is 0 on empty input — so even the error path would print a
blank field rather than naming the absent marker.

**Fix.** Extract each file's marker into its own variable, red if either is empty (naming which file),
then compare the two values for equality. Replace the `head -1 || echo '(none)'` idiom with an
explicit empty-string default.

**Left-shift gate.** `check-placeholders.test.sh` case 6 (`:83-88`) only sed-rewrites `v9.9 → v8.8`,
i.e. the DISAGREEING pair. Add an arm whose fixture deletes one carrier's marker line entirely and
asserts the run reds naming that file.

### M7 — `KIT_LEXICON_VERSION` is presence-checked only; three shipped `gov:kit lexicon@1.0` markers are unpaired

**`tools/check-kit-versions.sh:146`** · duplicates: ids 18, 24

The line is a bare `need "KIT_LEXICON_VERSION" tools/lexicon/lexicon.py` — presence plus
`[0-9]+\.[0-9]+` shape. Three markers ship with nothing comparing them to the constant:
`tools/lexicon/lexicon.py:2`, `tools/lexicon/README.md:1`, `tools/lexicon/LEXICON.md:1`, all
`gov:kit lexicon@1.0`. `tools/lexicon/kit.toml:7` makes govkit resolve the **constant**
(`version_from = { file = "lexicon.py", pattern = "^KIT_LEXICON_VERSION = " }`) while an adopter greps
the **markers** — the `two-answers-to-one-question` split. Bumping the constant to `"1.1"` leaves all
three markers stale with the full bar green.

Every other marker-carrying kit in this same file got an explicit pair assertion, each added *after*
this exact failure: agent-cap (`:43-49`, "a half-bumped pair therefore passed"), settings-merge
(`:53-60`, "Presence-only left a half-bumped pair passing"), memory-tree (`:62-96`, whose block also
states the derived-population law — "naming one file is why the hole reopened at every bump"),
unattended (`:102`), memory-recall (`:111`), drift-audit (`:121`), pytest-guardrails (`:151`). The
lexicon is the first marker-carrying kit to land with **zero** pair assertion.

Worse than a convention oversight: the unit spec's own inventory table
(`spec-dClosedLexicon-1.md:255`) lists the marker row with the reason "the version pair gate compares
marker to constant" — the requirement was written and the implementation shipped without it.
`adopt-lexicon.sh --check` has no VERSION/marker logic either.

**Fix.** Follow the memory-tree block's derived-population form, not the `need` one: read the constant,
refuse if unreadable, then **enumerate** the carrier population from the tree
(`git ls-files 'tools/lexicon/*.md'` plus `lexicon.py`), refuse on an empty population, and red on any
carrier lacking `gov:kit lexicon@$lx([^0-9.]|$)`.

**Left-shift gate.** The derived-population form *is* the gate — it is what stops the hole reopening
at the next bump, which the memory-tree block records happening when the population was named by hand.

### M8 — P2 silently exempts a type named EXACTLY a banned suffix, contradicting S2 with no rationale and no arm

**`tools/lexicon/lexicon.py:229`** · id 22

```python
if name.endswith(suf) and name != suf:
```

Verified: with the shipped `BANNED_SUFFIXES="Manager Helper Util Utils Handler Processor Data Info"`
and `SUFFIX_OFFENDER_PIN="0"`, a file defining `class Manager`, `class Data` and `class Info` runs
green and exits 0, while the control `class ThingManager` in the same position reds with
`P2 suffix … over pin 0`.

The spec's S2 (`spec-dClosedLexicon-1.md:26`) states the predicate without qualification — "no type
DEFINED in the corpus ends with a declared `BANNED_SUFFIXES` entry" — and no rationale for the
exemption appears in the spec, `LEXICON.md`, `README.md` or the code, nor any selftest arm covering
it. `Data`, `Info` and `Handler` are plausible real class names, and the design prose's headline case
("a type named `…Manager` is a type nobody scoped") describes precisely what the exemption lets
through. P2 reads as airtight at pin 0 while its most egregious input is unreachable.

**Fix.** Drop `and name != suf` so a bare `Manager`/`Data`/`Info` is an offender — the waiver file is
the escape hatch if a repo genuinely wants one. If the exemption is deliberate, say so in S2 **and**
in the code, and arm the boundary in both directions.

**Left-shift gate.** A selftest arm asserting `class Manager` reds naming `Manager`, plus its control
(`class ThingManager` reds, `class Managerial` does not). Boundary conditions get arms in both
directions, which is the discipline the other 28 arms already follow.

### M9 — `customize.md`'s new "37 in total as a UNION" is ungated prose, five lines below the sentence explaining why not to write it

**`parallel-coding-governance.customize.md:22`** · id 16

`check-placeholders.sh` derives only the two per-file tallies (`tally_for`, `:80-85`) and the
shared-placeholder line; **no code path computes or asserts a union**. Measured today: template 23,
companion 15, union 37 — correct now. Adding one placeholder to the template forces `23 → 24` under
gate pressure while `37` silently rots. The restated `23 and 15` on the same line are ungated too, so
if anything the finding undercounts.

The irony is structural: lines 15-17 of the same file **delete** the intro sentence's counts because
they "carried a stale pair through two revisions", and line 22 recreates the same authored-number
class five lines below.

**Fix.** Add a fourth predicate to `check-placeholders.sh`:
`union=$(printf '%s\n%s\n' "$t_set" "$c_set" | sort -u | grep -c .)`, parse
`^([0-9]+) in total as a UNION` out of `$CATALOGUE`, **refuse when the heading is absent** (same shape
as `tally_for`), and red when the two disagree.

**Left-shift gate.** Matching green and red arms in `check-placeholders.test.sh` (the fixture's union
is 4). The general rule this diff should adopt: a number written in a gated document is either
derived by the gate or deleted — there is no third state, which is exactly what lines 15-17 argue.

---

## LOW

### L1 — The placeholder-catalogue self-test leg's guard omits the very file the leg executes

**`tools/gate-legs.json:589`** and **`tools/govkit/entries/check-placeholders.kit.toml:41`** · duplicates: ids 6, 12

The guard is the single pathspec `tools/check-placeholders.sh`; the leg's argv is
`bash tools/check-placeholders.test.sh`. `run-gates.sh:63` evaluates guards as
`git diff --quiet "$BASE" -- <pathspec>`, and a git pathspec naming that exact file does not match
`tools/check-placeholders.test.sh`. So a commit that edits **only** the self-test skips the leg that
runs it — the same edit that breaks an arm is the edit that silences the leg checking it.

Enumerated every self-test leg's guard: all 27 others guard a **directory** containing both engine and
harness (`tools/lexicon/`, `tools/workflows/`, `tools/memory-tree/`, `tools/govkit/`, `.githooks/`, …).
This is the sole outlier, and nothing structural forced it — govkit's 7c guard-class table
(`govkit.py:434-461`) would class `tools/check-placeholders.test.sh` as kit-relative, exactly one
class, so widening is legal.

Correctly bounded to an early-signal loss because `.githooks/pre-push` sets `GATE_FULL=1` (asserted at
`run-gates.test.sh:284-293`), hence low.

**Fix.** Add `{prefix}/check-placeholders.test.sh` to the descriptor's guard list and
`tools/check-placeholders.test.sh` to the corresponding array in `tools/gate-legs.json`, keeping the
two in lockstep.

**Left-shift gate.** The run-gates canary (`tools/run-gates.test.sh:30-44`) currently asserts only
that a guard matches **some** tracked path, which is why no arm sees this. Strengthen it: for any leg
whose argv names a tracked script, assert that script is matched by the leg's own guard. That is a
one-predicate change that would have caught this at authoring time and prevents the class.

### L2 — The `check-placeholders.sh` header states a count that was wrong the moment it was written

**`tools/check-placeholders.sh:8`** · id 13

The header says the two shipped files "carry 23 and 14 placeholders permanently and by design".
Measured: `bash tools/check-placeholders.sh` prints `23 + 15 placeholders catalogued`. Commit
`0007b35` adds this header **and** adds `{{LEXICON_CONF}}` to
`parallel-coding-governance.domain-rules.md` in the same commit (its own message says "23 and 15
placeholders by design"), so the header was stale on arrival. `customize.md`'s tallies are correct and
gate-asserted; nothing checks the header prose.

This is exactly the prose-that-rots class this gate was written to replace, sitting in the file a
reader consults to learn what the gate measures.

**Fix.** Drop the figures rather than correcting them — the catalogue's per-file tallies are the gated
single source, as the neighbouring `customize.md` edit itself argues. Reword to: "they carry
placeholders permanently and by design; the per-file counts live in the catalogue and are gated below."

**Left-shift gate.** Same rule as M9: a count in a document this repo ships is derived or deleted.
Worth a one-line addition to `memory/HYGIENE.md` so it applies to the next gate's header too.

---

## Verdict and landing order

**BLOCKED.** B1 must be fixed before this unit is considered landed: the merge bar currently runs a
leg (`tools/gate-legs.json:543`) whose one armed rule cannot fire, and `AGENTS.md` now carries a
charter bullet asserting a measurement over the empty set.

Suggested order, because the fixes compose:

1. **H1** first — fix the engine's target resolution. B1's path-spelled rule then becomes correct as
   written, and M8's arm work lands in the same file.
2. **B1** — add the DEAD RULE arm and the P3 selftest arm of this repo's own declared shape. Verify
   `LAYER_OFFENDER_PIN="0"` is now falsifiable by planting the real violation.
3. **M1** — the govkit shadowing, before any adopter re-applies.
4. **M2 + M3 + M4** together — one scaffold arm ("a freshly scaffolded, curated, ratified conf is
   green on its first engine run") is the gate for all three, and that arm is the single highest-value
   addition in this list: the entire `--scaffold` path is currently unexercised by any leg.
5. **M5 + M6 + M9** together — three arms in `check-placeholders.test.sh`, all in one file.
6. **M7** — the derived-population pair assertion.
7. **L1 + L2** — the guard widening (plus the canary strengthening) and the header trim.

## What the review says about the diff's own method

The kit is unusually well armed for a first landing: 28 selftest arms each asserting a **message**
rather than an exit code, a `DEAD PROBE` vacuity arm on the extractor side, a `SENTINEL` freeze per
shipped pattern set, waivers keyed on matched text with staleness detection, and a two-commit rollout
that lands inert before arming. Nine of the thirteen defects here are found *by* that discipline being
applied one level short of where it needed to reach — the vacuity arm covers extractors and empty
declarations but not unmatchable ones; the pins are measured but one is a literal and another is
measured pre-curation; the version constant is present but unpaired. The remediation pattern the repo
already owns (`check-kit-versions.sh`'s three recorded pair-assertion retrofits, the codebase-map
gate's bidirectionality) is the right template for every one of them.
