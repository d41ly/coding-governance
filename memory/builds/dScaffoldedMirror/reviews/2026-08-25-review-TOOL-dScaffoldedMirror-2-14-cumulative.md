**Serves:** diff-review TOOL-dScaffoldedMirror-2 TOOL-dScaffoldedMirror-6 TOOL-dScaffoldedMirror-7 TOOL-dScaffoldedMirror-8 TOOL-dScaffoldedMirror-10 TOOL-dScaffoldedMirror-14

# Tier-2 review — dScaffoldedMirror, ROUND 1

**Range:** `500a5db6b8e056c11bbe1c3cd82a16bc186ada5a...HEAD` (HEAD = `a9308644`) · **ROUND 1** ·
2026-08-25 · node `d`.

**Review shape:** raw 37 · confirmed 31 · refuted 6 · unverified 0 · precision 0.84.

The 31 confirmed findings collapse to **17 distinct defects** — five of them found independently by
three or four lenses, which is what a diff full of new refusals looks like when several reviewers run
the `armed-but-unreachable-rule` probe over the same file. Duplicate finding ids are listed on each
entry so the fan's coverage stays auditable.

**Verdict: 1 blocker, 3 high, 9 medium, 4 low. The diff cannot land as it stands** — the blocker is a
merge-bar leg that is RED at HEAD on a clean tree, with no guard to scope it away.

## Verdict: BLOCKED

One blocker, three high, nine medium, four low over 17 distinct defects; 31 confirmed of 37 raw,
precision 0.84. The blocker reproduced independently on a clean tree at HEAD.

## Severity roll-up

| # | Sev | Site | Defect | Dup ids |
|---|---|---|---|---|
| B1 | blocker | `memory/map/features/lexicon.md:22` | three unclaimed inventory keys, three stale map artifacts, unguarded leg RED | 1, 19 |
| H1 | high | `tools/lexicon/lexicon.py:631` | `--measure` returns before STALE WAIVERS is computed | 3, 11, 23, 30 |
| H2 | high | `tools/lexicon/adopt-lexicon.sh:84` | `render_skill` re-implements the VERBS grammar; its gate is structurally blind | 2, 31 |
| H3 | high | `tools/lexicon/adopt-lexicon.sh:251` | `--scaffold` drops `write_skill`'s exit status, reports a failed adoption as success | 7, 20, 36 |
| M1 | medium | `tools/lexicon/kit.toml:53` | `[[outcome]]` probe cannot be false — adoption classified without observing adoption | 27 |
| M2 | medium | `tools/drift-audit/drift_report.py:270` | justification regex unsatisfiable for the `<none>` extension this repo declares | 6, 10, 33 |
| M3 | medium | `tools/lexicon/lexicon.py:837` | `--brief` has no `SyntaxError` guard; exits 1 with a traceback | 9 |
| M4 | medium | `tools/lexicon/lexicon.py:778` | `--suggest` drops the object for every `_`-prefixed name | 12, 32 |
| M5 | medium | `tools/lexicon/lexicon.py:782` | `--suggest` rejoins with `_` regardless of the identifier's convention | 26 |
| M6 | medium | `tools/lexicon/scaffold_lexicon.py:44` | HEADER still claims a frequency ranking that -8 deleted | 13, 25 |
| M7 | medium | `tools/lexicon/lexicon.py:96` | `SCAFFOLD_KNOWN` is a second, already-divergent extension catalog | 22 |
| M8 | medium | `tools/lexicon/kit.toml:109` | a second gate leg with byte-identical argv; one check, two green rows | 4, 21 |
| M9 | medium | `.gitattributes` | the kit's `lf_pin` for the new Skill never reached this repo's own attributes | 5, 28 |
| L1 | low | `tools/lexicon/selftest.py:523` | arm conjunct `"R" in out` is entailed by the first conjunct | 18 |
| L2 | low | `tools/lexicon/scaffold_lexicon.py:55` | the banned-suffix list is authored twice in one file | 16, 35 |
| L3 | low | `tools/lexicon/scaffold_lexicon.py:122` | `debt` is computed and never read | 17 |
| L4 | low | `tools/drift-audit/drift_report.py:1009` | ungradeable names counted as offenders, against `leading_verb`'s contract | 34 |

## What the fan was hunting, and what it caught

The build's own framing asked for four hunts. Three of them paid.

- **Every new refusal — does its failing case reach it?** H1 is a second DEAD SNIFFER: a refusal
  registered *after* its own reader, in the very unit whose job was to arm `--measure`. M1 and M2 are
  the same family from the other end — a probe that cannot be false, and a marker that cannot match.
- **The render in `adopt-lexicon.sh`.** Three defects were already fixed there. H2 and H3 are the
  fourth and fifth, and H2's gate is blind to itself by construction.
- **The canon selection rule in `scaffold_lexicon.py`.** Clean. `seeded` is built from
  `canon.CLUSTERS` order with membership gated on any live site, so no corpus at any frequency can get
  a non-element-0 form into a proposed table. What survives there is prose (M6) and dead weight (L2,
  L3), not a selection defect.
- **Liveness assertions that cannot be False.** Nothing found beyond M1, which is the `must_exist`
  variant of the same shape.

---

## B1 — blocker: the codebase-map coverage + freshness leg is RED at HEAD

**`memory/map/features/lexicon.md:22`** (dup ids 1, 19)

Reproduced on a clean tree at `a9308644`. `python tools/codebase-map/test_codebase_map.py` fails two
of five:

```
FAIL test_every_inventory_key_is_claimed_or_baselined
UNCLAIMED {'gate-legs': ['lexicon skill wiring'], 'rendered-skills': ['lexicon'], 'lexicon-verbs': ['cmd']}
FAIL test_generated_artifacts_are_fresh
STALE inventories.json — regen: python tools/codebase-map/gen_map.py --write
```

Regenerating produces a ~50-line diff across `inventories.json`, `MAP.md` and `symbols.json`, with
nine new symbols missing (`build_banned_index`, `build_form_index`, `build_negatives`, `read_gloss`,
`read_object`, `run_probe` and siblings). The manifest entry for `codebase-map coverage + freshness`
carries **no `guard` key** and subject `repo`, and `run-gates` only skips a leg when its guard field is
non-empty — so this leg runs on every bar and on `.githooks/pre-push`. It cannot be scoped away.

This is not bookkeeping. A new agent-instruction artifact (`rendered-skills` `lexicon`) and a new gate
leg entered the tree with no dossier accounting for either, which is exactly the declared-population
control §7 describes: a new moving part reds until a declaration claims it.

**Fix.** Add `"lexicon skill wiring"` to the dossier's `gate-legs` list, `"lexicon"` to
`rendered-skills`, `"cmd"` to `lexicon-verbs`, then run `python tools/codebase-map/gen_map.py --write`
and commit the three regenerated artifacts **in the same commit** (§1 DoD). Note the ordering
dependency: if M8 is fixed by deleting the duplicate leg, the `gate-legs` key may not need claiming at
all — resolve M8 first, then reclaim.

**Left-shift.** The gate already exists and already caught this; the failure is that it was not run
before the records commit. The gate-shaped remedy is DoD sequencing, not a new check — wire the map
regen into whatever renders `tools/gate-legs.json`, so a leg addition cannot land without its map row,
and the two artifacts stop being separately forgettable.

---

## H1 — `--measure` returns before STALE WAIVERS can reach `problems`

**`tools/lexicon/lexicon.py:631`** (dup ids 3, 11, 23, 30 — four independent lenses)

The comment at 627-630 states that `--measure` now exits non-zero on UNDECLARED EXTENSIONS, DEAD
PROBE, UNSELECTIVE LAYERS RULE **and STALE WAIVERS**, and that "three later units use it as a
discharge probe, and a probe that cannot fail discharges nothing." Two of those four conditions are
appended to `problems` at lines 648 and 657, inside the waivers/pins loop that only runs **after** the
`return 1 if problems else 0` at line 631.

Confirmed by staging the break: appending `zzz_no_such_symbol_xyz` to
`tools/lexicon/lexicon-verb-waivers.txt` makes plain `--check` exit 1 printing `STALE WAIVERS in
lexicon-verb-waivers.txt`, while `--measure` prints the three pins, prints **no** `# NOTE:` line, and
exits 0. Restored; tree clean.

The non-integer-pin problem at 657 is unreachable from `--measure` for the same reason.

An operator re-measuring pins after curation gets a clean exit 0 and pastes a pin derived from a
corpus carrying dead waivers. A stale waiver is a live silencer whose target text is gone — §7's "an
exemption naming a path that no longer exists reds too, because a stale one silently widens the
surface it was written to narrow."

**Fix.** Hoist the waiver load and the `stale` / pin-parse computation above the `if measure_mode:`
block. They need only `offenders` and `load_waivers`, both already in scope, so one `problems` list
can feed both exits.

**Left-shift.** A selftest arm that stages a stale waiver and asserts `--measure` exits non-zero naming
it — **staged red first**, per §7's "a new gate is not landed until its failing case has been
observed." Stronger and just as cheap: an arm asserting that for each of the four conditions the
comment names, `--measure` and `--check` agree on the exit code over the same tree. That gates the
class rather than this instance, and would have caught the DEAD SNIFFER defect too.

---

## H2 — `render_skill` re-implements the VERBS grammar, and its gate cannot see the divergence

**`tools/lexicon/adopt-lexicon.sh:84`** (dup ids 2, 31)

`render_skill` parses the `VERBS:` block in an inline python heredoc rather than going through
`lexicon_conf.py`, the declared ONE reader. Two grammar-legal shapes diverge, both reproduced by
running `lexicon_conf.load_conf` and the heredoc parser over the same fixture text.

1. **An indented `#` comment row inside `VERBS:`.** `lexicon_conf.py` skips it
   (`if not body.startswith("#")`); the heredoc's `re.match(r"\s+(\S+)\s+(.*)$")` accepts it and emits
   a phantom row into the agent-facing Skill table — ``- `#` — grouped: the I/O verbs``, a verb row
   that is not a verb.
2. **A TAB-indented verb row.** `lexicon_conf.py` accepts it (`nxt[:1].isspace()`); the heredoc's
   space-only `if not line.startswith(" "): break` **truncates the render silently**. One fixture
   rendered 1 of 3 declared verbs with no error; against the live conf that is 2 rows against 23.

`check_skill` byte-compares `render_skill`'s stdout against the on-disk `SKILL.md` that `write_skill`
produced **from that same `render_skill`**, so both operands carry the identical defect and the leg
stays green either way. The gate is structurally blind to its own renderer — the
`gate-green-by-accident-on-generated-bytes` class.

The `--check` block 130 lines below names the exact rule being broken: "A second parser here is the
two-answers-to-one-question class, so this shells out rather than re-implementing the grammar."

**Fix.** Delete the heredoc. Extend `lexicon_conf.py`'s CLI with a `--print-verb-rows` mode emitting
`<verb>\t<gloss>` per row from `load_conf` — it already has `--print-verbs` for exactly this bash
consumer — and have `render_skill` shell out to it as `--check` already does. One parser, one grammar,
both divergences gone without a second fix.

**Left-shift.** A selftest arm rendering a conf whose `VERBS:` block carries a comment row *and* a
tab-indented row, asserting the rendered table matches `load_conf`'s table exactly — an assertion
against the **reader**, never against another render. Generalise it: any gate whose two operands come
from one producer gets an arm comparing against an independent third party. That is the
`assertion-between-two-derived-values` class, and it has now bitten twice in this kit.

---

## H3 — `--scaffold` reports a failed adoption as success

**`tools/lexicon/adopt-lexicon.sh:251`** (dup ids 7, 20, 36)

The script runs under `set -u` only, no `-e`. Line 190 (the `--render` path) correctly writes
`write_skill || exit 1`; line 251 (the `--scaffold` path) is a bare `write_skill` followed by the
success `echo`, so the script's exit status is the echo's 0.

Reproduced end to end in a scratch git repo whose tracked corpus has no canon-cluster verbs. The run
printed `scaffold: 0 verb(s) proposed`, then `lexicon: the Skill render failed`, then
`lexicon-adopt: wrote .lexicon.conf marked PROPOSED`, and **exited 0 with no `.claude/skills/lexicon/`
directory at all**. The empty-VERBS path is reachable from `--scaffold` itself, because the seed is
`[rep for rep, … in canon.CLUSTERS if rep in live]`.

The adopter is then wedged. `--check` reds, `--scaffold` refuses because the conf now exists, and
`--render` is discoverable only from the usage line. Nothing printed names it. And because govkit reads
the exit code, `[adopt]` is classified as success — see M1, which removes the other half of the net.

**Fix.** `write_skill || exit 1` at line 251, matching the `--render` branch, with the success echo
moved below it. Make the empty-VERBS refusal name the actual remedy: curate `VERBS:` in
`.lexicon.conf`, then `bash tools/lexicon/adopt-lexicon.sh --render`.

**Left-shift.** Gate the class, not the instance. A selftest arm that greps `adopt-lexicon.sh` for
every call site of the functions that can return non-zero (`write_skill`, `render_skill`) and asserts
each is followed by `|| exit` or terminates a checked chain. A single-site fix certifies coverage the
script does not have, and the shape will recur the next time a mode is added. Cheaper interim: a shell
lint leg flagging an ignored non-zero return in a `set -e`-less script.

---

## M1 — the kit's `[[outcome]]` probe cannot be false

**`tools/lexicon/kit.toml:53`** (dup id 27)

`must_exist = "{kit}/lexicon.py"` is satisfied by the `include = "**"` engine rule, which copies
`lexicon.py` to disk during the WRITE phase, before `[adopt]` ever runs. `classify_outcome`
(`tools/govkit/govkit.py:2030`) therefore returns `adopted` for rc 0 whatever the adopter did. It is a
liveness assertion that is True by construction — the exact shape the build's own hunt list asked for.

Combined with H3 it is load-bearing: govkit reports a lexicon install as adopted when no
`.claude/skills/lexicon/SKILL.md` was written, and the unguarded `lexicon skill wiring` leg then reds
on the target's first bar. The sibling `tools/memory-recall/kit.toml:47` probes its own rendered
`SKILL.md` — the artifact its adopter actually produces — which is the shape this descriptor should
have.

**Fix.** Probe `.lexicon.conf` **and** `.claude/skills/lexicon/SKILL.md`, matching memory-recall.

**Left-shift.** A govkit-level check asserting that every `[[outcome]]` `must_exist` path is *not*
matched by that kit's own `[[files]]` include rules — i.e. that the probe names a side-effect artifact
rather than a copied one. Machine-decidable from the descriptors alone, and it gates every kit at once.

---

## M2 — the LANGS mode ratchet's justification marker is unsatisfiable for `<none>`

**`tools/drift-audit/drift_report.py:270`** (dup ids 6, 10, 33)

`_check_mode_justified` builds `\b + re.escape(ext) + \b\s*:?\s*\b + old …`. For `ext = "<none>"` the
leading `\b` sits before a non-word `<` and the trailing one after a non-word `>`, so the pattern
demands a word character glued outside each bracket. Every human spelling tested returns False:

```
# <none>: dark -> absent, the last extensionless file was deleted.   -> False
# the <none> dark -> absent move                                     -> False
# <none>:dark->absent                                                -> False
# py: parser -> dark because ast broke                               -> True   (control)
```

Only a contrived `x<none>dark -> absent` matches. The case is reachable and live: `.lexicon.conf:23`
declares `<none>::dark` — the tool itself mints that token via `ext_of` for dotless basenames,
covering `.githooks/pre-commit` and `.githooks/pre-push`. Dropping the entry when those files go away
gives `new_rank -1 < old_rank 0`, `build_lang_mode_findings` fires with `absent`, and
`drift_report.py:1452/1467` folds it into a non-zero `--check` exit on an **unguarded** merge-bar leg.
The finding's own remedy text instructs the operator to write exactly the marker the checker rejects.
The only escapes are keeping a dead declaration forever or editing the checker.

Scoped honestly: this reds the branch that removes the declaration rather than persisting once the base
advances. The defect is a refusal with no executable remedy, which §7 bans outright.

**Fix.** Replace the `\b` anchors around the extension with boundary lookarounds —
`(?:(?<=\s)|^)` + `re.escape(ext)` + `(?=\s|:|,|$)` — or drop them for the extension token entirely,
since the `:?` separator plus the `old -> new` clause is already specific enough. Word-character
extensions are unaffected either way.

**Left-shift.** A selftest arm in `test_lang_mode_ratchet` using `<none>` as the extension, asserting
the justified case is silent. The existing arms exercise only `py`/`js`, both all-word tokens, so the
failing case has never been observed — a gate whose vocabulary has never met its own pseudo-token.
Generalise: any checker that emits a remedy string gets one arm asserting the emitted string, fed back
in, satisfies the check. That gates "the remedy I print is a remedy I accept" for every refusal in the
kit.

---

## M3 — `--brief` crashes with a traceback on an unparseable file

**`tools/lexicon/lexicon.py:837`** (dup id 9)

`run_brief` calls `extract(p, mode, pset)` on the target with no `except SyntaxError`, unlike the
corpus loop 30 lines below which catches `(SyntaxError, OSError)`. `_python_defs` (205-211)
deliberately raises, and `extract` does not catch.

Confirmed live: `--brief` on a file containing `def broken(:` printed the COVERAGE line, then a raw
Python traceback, and **exited 1**. That contradicts `main()`'s own stated property at 975-976 — the
read-only verbs "cannot reach a pin, a waiver or an exit code of 1 even by accident" — and it fires on
the single most likely case for this verb: an author asking what to call a function in a file they are
mid-edit. The arm `S6: --brief never exits 1` (`selftest.py:628-630`) only ever passes the parseable
fixture `core/a.py`, so nothing catches it.

**Fix.** Wrap the target extraction and return 2 with a named message
(`lexicon: <rel> does not parse, so its objects cannot be read: <e>`), keeping 1 reserved for verdicts.

**Left-shift.** Extend the S6 arm to a small table of hostile targets — unparseable `.py`, a zero-byte
file, a directory, an unarmed extension, a path outside the repo — asserting `code != 1` for each. A
property arm over a population beats an arm over one blessed fixture, which is the
`fixture-passes-by-finding-nothing` shape this suite exists to catch.

---

## M4 — `--suggest` drops the object for every `_`-prefixed name

**`tools/lexicon/lexicon.py:778`** (dup ids 12, 32)

```python
rest = name[len(verb):].lstrip("_") if name.lower().startswith(verb) else ""
```

`subtokens.leading_verb` lstrips underscores before extracting the verb, so for `_fetch_conf` the verb
is `fetch` — but the guard tests the **unstripped** name, which does not start with `fetch`, so `rest`
stays empty and the suggestion collapses to a bare verb.

Reproduced live against this repo's own declaration:

```
--suggest _fetch_conf    -> use `load`          (object and private prefix both gone)
--suggest _get_row       -> use `read`
--suggest fetch_remote   -> use `load_remote`   (control, correct)
```

The tool answers a bare verb to the one question the Skill exists to answer, and the name it proposes
would collide with any real `load`. `_`-prefixed helpers are the dominant private convention in this
very kit (`_python_defs`, `_probe_defs`, `_build_glob_rx`, `_measure_suffix_offenders`,
`_read_defs_at_sha`). `selftest.py:611` exercises only the unprefixed form.

**Fix.** Derive the tail from the same splitter the verb came from rather than by slicing the raw name:
keep the leading-underscore run as a prefix, take `subtokens(name)[1:]` for the tail, and reattach, so
`_fetch_remote` becomes `_load_remote`.

**Left-shift.** Fixture arms for a `_`-prefixed and a `__dunder__` identifier. Better, and it gates the
class: a property arm asserting that for every suggestion, the proposed name and the original differ
**only** in their leading verb token — same prefix, same object tokens, same separator style. That one
assertion catches M4 and M5 together, and any future slicing defect.

---

## M5 — `--suggest` rejoins with `_` regardless of the identifier's convention

**`tools/lexicon/lexicon.py:782`** (dup id 26)

`swap = f"{want}_{rest}"` with `rest` taken verbatim from the source identifier, so a camelCase tail is
glued on after an underscore. Measured against this repo's declaration:

```
--suggest getUserData   -> use `read_UserData`
--suggest createWidget  -> use `build_Widget`
--suggest doThing       -> use `cmd_Thing`
```

Identifiers valid in neither convention. `.lexicon.conf` declares `js:js-regex:probe`, so camelCase is
an armed, first-class input, and `--suggest` is the headline verb of the rendered Skill — this spelling
is what the Skill teaches. Distinct root cause from M4: that one is the `startswith` guard on 778, this
is the unconditional `_` join on 782. Both must be fixed for either output to be right.

**Fix.** Detect the input's separator: if the original name, past any leading underscores, contains no
`_`, emit `want + rest[0].upper() + rest[1:]`; otherwise keep the `_` join.

**Left-shift.** Covered by the M4 property arm above (same separator style as the original). Add one
concrete camelCase arm alongside it so the failure message names the case.

---

## M6 — the scaffolded conf gives an adopter two answers to one question

**`tools/lexicon/scaffold_lexicon.py:44`** (dup ids 13, 25)

`HEADER` — written verbatim into every adopter's generated `.lexicon.conf` — still says the verb table
is "a frequency ranking of what this corpus already does, which is a mirror of the code." Unit -8 made
that false, and the block the same function appends ~110 lines lower contradicts it directly:

> `# PROPOSED from the SHIPPED CANON … A frequency ranking would adopt whatever this repo already`
> `# does most, which is how a naming gate ends up certifying the habit it was installed to change`

Verified by scaffolding a throwaway repo: both strings land in one generated file, and the wrong one is
the one an adopter reads first — and the one that instructs the curation step. It is also false on the
code: `seeded` comes from `canon.CLUSTERS` order with membership gated on live sites, so the corpus
votes on cluster **membership** only and cannot promote a spelling.

The same stranded claim survives at `scaffold_lexicon.py:9` (module docstring), `adopt-lexicon.sh:10`
("derives a proposal from their own corpus by leading-token frequency") and `README.md:146`. Line 29's
`#:` docstring for the deleted `SEED_VERBS` constant is orphaned with them.

**Fix.** Rewrite `HEADER` to describe the canon rule — the corpus decides *which* clusters appear, the
canon's element 0 decides what each is *called*, curate the glosses and sharpen the NOT clauses — and
fix all four sibling sites in the same commit.

**Left-shift.** This is the `two-answers-to-one-question` class inside a generated artifact, and it is
gateable: an arm asserting that the words `frequency` / `frequency ranking` appear in neither the
emitted conf, nor `scaffold_lexicon.py`'s docstring, nor `adopt-lexicon.sh`'s header, nor
`README.md` — a banned-phrase check pinned to the decision that deleted the mechanism. Cheap,
zero-false-positive on this corpus, and it reds the next time a deleted mechanism is described as live.

---

## M7 — `SCAFFOLD_KNOWN` is a second, already-divergent extension catalog

**`tools/lexicon/lexicon.py:96`** (dup id 22)

```
lexicon.py:96            SCAFFOLD_KNOWN = {"py": ("",           "parser"), "js": ("js-regex", "probe")}
scaffold_lexicon.py:34   KNOWN          = {"py": ("python-ast", "parser"), "js": ("js-regex", "probe")}
```

Already divergent on `py`'s pattern-set id, and nothing compares them — `SCAFFOLD_KNOWN`'s only
reference is `run_probe` (894), `KNOWN` is used only inside `scaffold_lexicon.py`, and no selftest arm
names either. `run_probe`'s printed promise on a conf-less repo is "NO `.lexicon.conf` here, so this is
what adoption would find", which is exactly the claim a second catalog cannot keep.

Benign today only because `parser` mode ignores the pset — which is why the divergence went unnoticed,
and why the next extension added to one table and not the other will make `--probe` preview a LANGS set
`--scaffold` does not write, silently.

**Fix.** Delete `SCAFFOLD_KNOWN`, move `KNOWN` into `lexicon.py` as the one source, and have both
`run_probe` and `scaffold_lexicon.py` read it. `scaffold_lexicon.py` already does
`import lexicon as lex`, so the direction is legal under the declared LAYERS rule.

**Left-shift.** If the single-source fix lands there is nothing to gate — drift becomes structurally
impossible, which §12 prefers over a parity artifact. If two copies must persist for any reason, an arm
asserting `lexicon.SCAFFOLD_KNOWN == scaffold_lexicon.KNOWN`, staged red once.

---

## M8 — two gate legs, one check

**`tools/lexicon/kit.toml:109`** (dup ids 4, 21)

`tools/gate-legs.json` now carries two entries with byte-identical argv
`bash tools/lexicon/adopt-lexicon.sh --check` — `lexicon wiring` (guard `["tools/lexicon/"]`) and
`lexicon skill wiring` (guard `[]`), identical in every other field. Verified by parsing the manifest:
this is the **only** duplicated argv tuple in it. `run-gates` indexes legs positionally with no argv
dedupe, and skips guard evaluation entirely when the guard field is empty, so the unguarded leg
strictly subsumes the guarded one. The guarded leg can never produce a verdict the unguarded one has
not already produced, and on any commit touching `tools/lexicon/` the adopt script — three python
spawns per run — executes twice and a failure reports twice.

A reader counting green rows over-counts coverage by one, and adopters inherit both. `kit.toml:104-108`
even asserts the new leg "is the only leg in this kit without one" while `:74-78` still declares the
guarded twin. The sibling `memory-recall` kit deliberately carries exactly one such leg.

**Fix.** Either direction reaches the same end state — **one unguarded leg**. Simplest: delete the new
`[[gate_leg]]` block at 109-113 and change the existing `lexicon wiring` leg's guard to `[]`, carrying
the new comment onto it. That keeps the established leg name, so `gate-legs` needs no new map key at
all (see B1). Regenerate `tools/gate-legs.json` and the map afterwards.

**Left-shift.** A canary in `run-gates`, or in whatever renders `gate-legs.json`, that reds on any two
legs sharing an argv tuple. It is a declared-population invariant, it is one `collections.Counter`, and
this is the second kit to grow a redundant leg.

---

## M9 — the new rendered Skill is outside check-wiring's CRLF-repair population

**`.gitattributes`** (dup ids 5, 28) · declared at `tools/lexicon/kit.toml:117`

`git check-attr eol` over the four tracked rendered Skills:

```
.claude/skills/drift-audit/SKILL.md    -> eol: lf
.claude/skills/memory-recall/SKILL.md  -> eol: lf
.claude/skills/unattended/SKILL.md     -> eol: lf
.claude/skills/lexicon/SKILL.md        -> eol: unspecified
```

`.gitattributes` carries explicit rows for the other three (lines 75, 81, 87) and none for lexicon.
`tools/check-wiring.sh` `check_eol` (280-283) derives its repair population as tracked
`.claude/skills/**/*.md` **carrying** that attribute, so this file is outside both the report and
`--fix`, while `* text=auto` plus `core.autocrlf` smudges every unpinned path on this fleet. The kit's
`[[lf_pin]]` is only emitted into a **target's** `.gitattributes` by `govkit apply`; nothing maps a kit
lf_pin back onto this repo's own file, so the dogfooding repo gets nothing from the declaration.

The gate hides it: `check_skill` runs `tr -d '\r'` before comparing, so a CRLF working copy stays green.
What is left exposed is the artifact — this build's own comment records that for memory-recall "those
CRs rendered straight into SKILL.md and broke its YAML frontmatter", i.e. a Skill that silently stops
loading while its wiring leg reports green.

**Fix.** Add `.claude/skills/lexicon/SKILL.md text eol=lf` beside the three siblings with the same
one-line rationale, run `git add --renormalize` on it in the same commit, and account for it in
`tools/govkit/registry.toml` the way the siblings are.

**Left-shift.** The real gap is that a kit's `lf_pin` declaration is unenforced against this repo. Add a
check-wiring arm asserting that every `[[lf_pin]]` declared by any kit in `tools/*/kit.toml`, whose
target path is tracked here, carries the matching `eol=lf` attribute here. That is a declared-population
assertion in both directions, and it covers every future kit rather than this one Skill.

---

## L1 — a selftest conjunct that cannot independently fail

**`tools/lexicon/selftest.py:523`** (dup id 18)

```python
check("--measure names the undeclared extension", "UNDECLARED EXTENSIONS" in out and "R" in out, out)
```

`"R" in out` is satisfied by the R inside `UNDECLA` **R** `ED`, so the second conjunct is entailed by
the first. The arm cannot distinguish "the message names the `.R` extension" from "the message exists at
all" — a regression emitting the refusal without its extension list still passes. The
`fixture-passes-by-finding-nothing` shape, inside the suite written to catch it. The engine does print
bare extension names, so a real assertion was available and is not what was written.

**Fix.** Assert the extension as printed — `": R" in out`, or parse the line following the
`UNDECLARED EXTENSIONS` marker and assert on its contents. Confirm the arm reds when the extension is
stripped from the message.

**Left-shift.** Substring assertions containing their own needle are not detectable in general, but the
common case is: a lint arm over `selftest.py` flagging any `check(...)` whose asserted substring is two
characters or fewer, or whose second conjunct's needle is a substring of the first conjunct's needle.
Both are one regex over the suite, and either would have caught this line.

---

## L2 — the banned-suffix list is authored twice in one file

**`tools/lexicon/scaffold_lexicon.py:55`** (dup ids 16, 35)

`_measure_suffix_offenders` hardcodes `("Manager", "Helper", "Util", "Utils", "Handler", "Processor",
"Data", "Info")`, while line 129 emits `BANNED_SUFFIXES="Manager Helper Util Utils Handler Processor
Data Info"` as a separate literal. One `main()` run authors both — the pin, and the declaration the pin
is measured against — and nothing links them.

Identical today, so nothing is wrong yet. The defect is that editing either alone ships an adopter a
conf whose declared list and whose pin disagree, and the pin reds on their first `--check` against a
number the tool itself wrote. That is verbatim the `TOOL-dScaffoldedMirror-1` regression the comment at
128-131 says this unit closed — reintroduced by the unit that closed it. Unlike the other duplicated
list in this diff, this one feeds a **committed number**, not a preview.

**Fix.** Declare the tuple once at module scope, read it in `_measure_suffix_offenders`, and build line
129 as `'BANNED_SUFFIXES="%s"' % " ".join(BANNED)`.

**Left-shift.** Once single-sourced there is nothing to gate. Worth keeping permanently either way: an
**end-to-end** arm that scaffolds a fixture repo, then runs the gate inside it and asserts exit 0. A
scaffold whose output immediately reds its own gate is the one failure this kit has already shipped
once, and that arm gates it regardless of which internal copy drifts.

---

## L3 — `debt` is computed and never read

**`tools/lexicon/scaffold_lexicon.py:122`** (dup id 17)

`grep -n debt tools/lexicon/scaffold_lexicon.py` returns exactly one hit: the assignment. No
`body.append`, print or return consumes it, and the comment on 121 calls it "the corpus's one other job
here". The scaffolded conf body (127-172) writes `BANNED_SUFFIXES`, `LANGS`, the three pins, `ratified`,
`VERBS` and `LAYERS` — nothing debt-shaped.

So the scaffold's stated second output — which live spellings become debt on convergence — never reaches
the adopter, in the conf or on the `scaffold:` stdout line. They get the proposal with no indication of
what converging on it costs, which is the number `--probe` prints for an already-adopted repo. Dead as
written, and the comment reads as coverage.

**Fix.** Either emit it — a `# DEBT: get->read x12, …` block above `VERBS:`, and/or a field on the
`scaffold:` line — or delete the computation and the comment claiming it. §0: delete over disable.

**Left-shift.** The gateable form is a lint leg flagging an assigned-once, never-read local in the kit's
own sources. If that is too noisy to arm, this becomes a §10 checklist entry: a comment claiming an
output — does anything consume it?

---

## L4 — the marginal-offense rate counts ungradeable names as offenders

**`tools/drift-audit/drift_report.py:1009`** (dup id 34)

`(lex.leading_verb(n) or "") not in verbs` is True for any name `leading_verb` returns `""` for.
`subtokens.py:29-38` states plainly that `""` means the caller "must treat as UNGRADEABLE rather than as
a violation", and `lexicon.py:576-578` does exactly that (`if not verb: continue`). The vestigial
`or ""` — `leading_verb` always returns a str — reads as a half-written guard.

Reachable through either armed extractor: the js probe accepts `[A-Za-z_$][\w$]*`, so `function $(sel)`
and `const _ = () => …` both extract to a name with no word characters, and the Python ast path accepts
`def _(…)`. No such name exists in this tree today, so live cost is zero and the signal is report-only
(`gateable: False`) — hence low. But the docstring declares the operands part of the contract, and this
is the one instrument whose entire value rests on both operands coming from one extractor. A rate that
disagrees with the gate on the same population is the `two-answers-to-one-question` class in miniature.

**Fix.** Filter ungradeable names out of both operands before the ratio:
`graded = {(p, n) for p, n in added if lex.leading_verb(n)}`, take offenders over `graded`, report
`of=len(graded)`.

**Left-shift.** An arm feeding the signal a fixture containing an ungradeable definition (`def _(…)`) and
asserting it appears in neither the numerator nor the denominator. Broader and worth more: a shared
helper — `lex.is_gradeable(name)` — used by both the gate and the signal, so the contract has one
implementation instead of two readings of a docstring.

---

## Notes for round 2

- **B1 and M8 are coupled.** Resolve M8 first. The `gate-legs` map key may disappear along with the
  duplicate leg, and regenerating the map twice is wasted work.
- **H3 and M1 are one hole from two sides.** Fixing only the exit status leaves govkit classifying on a
  probe that cannot fail; fixing only the probe leaves the script exiting 0. Land both.
- **M4 and M5 are one output.** Neither fix alone makes `--suggest` correct for a `_`-prefixed camelCase
  name. The single property arm proposed under M4 covers both.
- **The recurring shape in this diff is a refusal registered on the wrong side of its own reader**
  (H1, M1, M2) — three instances, in the build whose stated purpose was arming refusals. The
  cross-cutting left-shift worth the most is the "the remedy I print is a remedy I accept" arm proposed
  under M2, plus the measure/check exit-code agreement arm under H1. Between them they gate the class
  rather than these three instances.
- **Refuted (6):** not carried here. The refuted set was dominated by claims about the canon selection
  rule and about `--probe`'s liveness, both of which held up under reading.
