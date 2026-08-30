# Wave 1 — lens: duplication and reinvention

**Serves:** research TOOL-aScouredKit-1

## Verdict: CLEAN WITH FIXES


**Subject:** whole repo at `093730e40355d6a04300966f791f2634379e8b45`
**Lens:** semantic near-duplication and ORCHESTRATION duplication, drift ranked above repetition.

---

## Method, and what I deliberately did not do

I did not run a clone detector. I enumerated this repo's high-fan-in seams and asked of each
whether a second implementation of that BEHAVIOUR exists that does not wire through the seam, then
tried to make each divergence MOVE against a real fixture.

Seams enumerated and their second-implementation question:

| seam | canonical home | second implementations found | verdict |
|---|---|---|---|
| python launcher resolution | `tools/lib/resolve-python.sh` | 12 inline copies, marker-delimited | **gated** by `tools/lib/resolve-python.test.sh` parity table — not a finding |
| `render_doc` template substitution | `tools/lib/render-doc.sh` | 2 marked inline copies + 4 unmarked hand-rolled `render()` bodies | partially gated — see F5 |
| `agent-cap.js` hook | `tools/hooks/agent-cap.js` | `.claude/hooks/agent-cap.js`, byte-identical | **gated** by `tools/hooks/agent-cap.test.sh:606-624` — not a finding |
| `.memory-tree.conf` reading | bash `source` (the file's own language) | **9 private Python parsers, 3 mutually incompatible grammars** | **F1, F2 — reproduced live** |
| gate-leg manifest path | `run-gates.sh:84` (derived from kit location) | 1 shipped hardcode + 1 descriptor guard | **F3 — reproduced live** |
| review-harness find→verify→synth | `tools/workflows/tier2-review.js` | 2 siblings under `tools/workflows/` | **F4** |
| kit-ships-doc / repo-runs-render parity | 3 independent gates | 3 different substitution mechanisms | **F5** |
| `resolve_bash` | — | 3 copies | already tracked, `TOOL-dSettledRoster-6` — not re-reported |
| generated-region row grammar | `row_grammar.py` | `unit_rows`, `verb_landed` | already tracked, `TOOL-aPromptedMandate-14` — not re-reported |
| waiver-registry keying | 5 registries, 5 grammars | — | owner-ruled divergence, `check-dead-paths.sh:53` — not a finding |

I read `memory/backlog/TOOL.md` (274 rows) and `memory/backlog/DEPL.md` in full, and
`memory/gotchas/INDEX.md` plus the four duplication-class records, before writing anything.

---

## F1 — BLOCKER. One config, two reader languages, inside one gate. A legal spelling silences the delegated half.

**`tools/memory-tree/check-memory-hygiene.sh:62`**

`.memory-tree.conf` is a sourced shell file. The hygiene gate reads it the file's own way:

```sh
62: [ -f "$ROOT/.memory-tree.conf" ] && . "$ROOT/.memory-tree.conf"
```

It then delegates four of its checks to Python modules, each of which **re-parses the same file with
its own private rule**:

- `tools/memory-tree/check-memory-hygiene.sh:607` → `gen_build_index.py` (`load_conf` at `:224`, strip at `:233`)
- `tools/memory-tree/check-memory-hygiene.sh:1079` → `corpus_ids.py` (`load_conf` at `:105`, strip at `:118`)
- `tools/memory-tree/check-memory-hygiene.sh:1089` → `gotchas.py` (`load_conf` at `:83`, strip at `:92`)
- `tools/memory-tree/check-memory-hygiene.sh:1099` → `row_grammar.py` (`load_conf` at `:86`, strip at `:93`)

plus `check-arms.py:73/:82` on the same rule. All five bodies are:

```python
k, _, v = line.partition("=")
conf[k.strip()] = v.strip().strip('"').strip("'")
```

That rule keeps everything after `=` including a trailing ` # comment`, and it does not model
`export `. Bash does both.

### Reproduced

Scratch adopter tree at `/tmp/gv-confdrift`, a memory-tree install, one planted violation
(`memory/gotchas/bad.md` missing the required `description` key). Two runs, the conf differing by a
trailing comment and nothing else:

```
### conf line: MEMORY_ROOT=memory   # the FLAT tree
$ python tools/memory-tree/gotchas.py --check
rc=0                                  # silent. No output at all.

### conf line: MEMORY_ROOT=memory
$ python tools/memory-tree/gotchas.py --check
HYGIENE memory/gotchas/bad.md: front matter is missing required key 'description'
rc=1
```

And the two readers, over the same bytes:

```
bash (what check-memory-hygiene.sh:62 gets):  MEMORY_ROOT=[memory]   exists? yes
corpus_ids.py     MEMORY_ROOT='memory   # the FLAT tree; see HYGIENE.md'  exists? False
gotchas.py        MEMORY_ROOT='memory   # the FLAT tree; see HYGIENE.md'  exists? False
gen_build_index.py MEMORY_ROOT='memory   # the FLAT tree; see HYGIENE.md' exists? False
check-arms.py     MEMORY_ROOT='memory   # the FLAT tree; see HYGIENE.md'  exists? False
```

The `export` half diverges too — `export DISCIPLINES="a b"` lands under the key `'export
DISCIPLINES'`, so `DISCIPLINES` reads as absent:

```
gotchas.py       DISCIPLINES=None   keys_with_export=['export DISCIPLINES']
drift_report.py  DISCIPLINES=None   keys_with_export=['export DISCIPLINES']
recall_conf.py   DISCIPLINES='a b'  keys_with_export=[]
```

### Why this is a blocker and not debt

The failure is silent and it is in the direction that removes coverage. The shell half of the gate
believes it is checking `memory/`; the Python half walks a directory that does not exist and reports
nothing. `gotchas.py` prints *nothing at all* on green, so there is no population count to notice.
`row_grammar.py` at least prints `clean (0 row(s) …)`, which is the liveness assertion the charter
demands and which the other three lack.

Two of this repo's own parsers already get it right and say why:

- `tools/codebase-map/map_lib.py:196-201` — *"match bash sourcing semantics for the restricted
  grammar the conf documents … so an inline ` # comment` can't leak into the value and diverge from
  bash"*
- `tools/memory-recall/recall_conf.py:118-121` — *"an unquoted value ends at the first whitespace,
  so a trailing ` # comment` cannot leak in and diverge from bash"*

So the correct implementation exists here twice. The duplication is the defect.

### Class

New instance of `memory/gotchas/two-readers-of-one-config-one-re-derived.md`, whose recorded instance
is `.unattended.conf`/`BYPASS_BAN` in `check-playbook.sh` and whose own closing line is *"There is no
machine gate yet."* This instance is worse than the recorded one: that one flipped one predicate's rc
1→0, this one re-points the corpus ROOT and so silences every check that walks it.

### Not covered by

`TOOL-aPacedTurnstile-10` / `aCollapsedScan-7` / `aSealedCaravan-5` are about **where** `recall_conf`
looks for the conf under `GIT_DIR`, not **how** any parser reads it. `TOOL-aSealedCaravan-4` is about
rendered docs naming `memory/` at a renamed root. No row names a parser grammar.

### Fix

Route the Python side through one parser with the `map_lib.py:196-201` rule (unquoted value ends at
first whitespace, `export ` stripped), and give it the bash-equivalence arm F2 describes. Cheapest
correct version: `gotchas.py` already imports `corpus_ids.py` at `:98-105` for the append-only
classification, so an intra-kit `load_conf` seam costs no new coupling.

---

## F2 — HIGH. A parser that declares itself a copy is not one, and the gate written for that exact class has a fixture blind to it.

**`tools/drift-audit/drift_report.py:78`**

```python
def load_conf(root: pathlib.Path) -> dict[str, str]:
    """Parse the memory-tree kit's KEY=VALUE conf.

    A deliberate COPY of the twenty lines in codebase-map's `map_lib.load_conf`, not an import of
    it: ... The drift is gated by asserting this parser against BASH sourcing the same file in
    selftest.py, never against a second Python parser ...
    """
```

Both halves of that docstring are currently false.

**It is not a copy.** Run side by side over identical bytes:

```
map_lib.load_conf      (the declared ORIGINAL): {'MEMORY_ROOT': 'memory',           'DISCIPLINES': 'a b'}
drift_report.load_conf (the declared COPY)    : {'MEMORY_ROOT': 'memory   # note', 'export DISCIPLINES': 'a b'}
```

`drift_report.py:99-102` dropped `map_lib.py:192` (`removeprefix("export ")`) and
`map_lib.py:200` (unquoted value ends at whitespace), and added a BOM strip
(`drift_report.py:98`) that `map_lib` does not have. Three divergences, in both directions.

**The gate cannot see it.** `tools/drift-audit/selftest.py:96-123` is the bash-equivalence arm. Its
fixture is four spellings (`:98-104`):

```python
'# a comment with an = sign\n'
'MEMORY_ROOT=memory\n'
'DISCIPLINES="one two three"\n'
"QUOTED_SINGLE='x y'\n"
'\n'
'TRAILING=spaced   \n'
```

Bare, double-quoted, single-quoted, trailing-whitespace. Neither divergent spelling — an inline
` # comment` after an unquoted value, or an `export ` prefix — is in the fixture. The arm passes,
and passes over the one class it exists to catch. This is `memory/gotchas/fixture-passes-by-finding-nothing.md`
inside the assertion written to prevent `two-answers-to-one-question`.

**Impact.** Every drift-audit signal is computed against `ctx.conf` and `ctx.memory_root`, so at an
adopter whose conf carries either spelling the whole Tier-0 report reads a non-existent corpus root.
That is the instrument this repo's own AGENTS.md tells sessions to run *"before theorizing about
drift"*.

### Fix

Two lines in the fixture (`export FOO=bar` and `INLINE=v   # note`), observed RED first, then make
the parser match `map_lib.py`. Or delete the copy and have drift-audit import `map_lib.load_conf`
behind a soft dependency — but the docstring's adoptability argument against that is sound, so the
fixture is the real fix.

---

## F3 — HIGH. Two readers of the leg manifest: one derives its path, the shipped one hardcodes it, and the gate for that class is scoped a directory too deep.

**`tools/check-testsuite-counts.sh:27`**

```sh
27: MANIFEST=tools/gate-legs.json
```

The same file is resolved parametrically eleven directories over, with the reason stated in place:

**`tools/run-gates/run-gates.sh:76-84`**
```sh
# The manifest is the kit dir's SIBLING, derived rather than spelled: this kit installs at
# <prefix>/run-gates/ and a hardcoded "tools/gate-legs.json" resolves to nothing at any other
# prefix.
LEGS_FILE="${GATE_LEGS:-$(dirname "$KITREL")/gate-legs.json}"
```

`check-testsuite-counts.sh` ships. `tools/govkit/entries/check-testsuite-counts.kit.toml:14-17`:

```toml
include = ["check-testsuite-counts.sh", "check-testsuite-counts.test.sh"]
role = "engine"
to = "{prefix}/{relpath}"
```

`role = "engine"` is written verbatim into the adopter, and `[adopt] argv = []` with
`why_no_adopter = "it needs no install step"`, so nothing repaths it.

### Reproduced

Adopter installed at prefix `scripts/`, manifest present at `scripts/gate-legs.json`:

```
$ bash scripts/check-testsuite-counts.sh
testsuite-counts: no tools/gate-legs.json, so the population would be empty and this leg would pass by finding nothing
rc=2
```

Permanent, unfixable in-band, and the message names a path the adopter does not have while their
manifest sits one directory away. It fails CLOSED, which is the good half; the bad half is that the
only repair is editing an `engine`-role file that the next `govkit update` overwrites.

### The descriptor repeats it, on one line

`tools/govkit/entries/check-testsuite-counts.kit.toml:28`:

```toml
guard = ["{prefix}/check-testsuite-counts.sh", "tools/gate-legs.json"]
```

The placeholder machinery is used for the first element of the array and not the second. Whatever the
runner does with a guard pathspec that resolves to nothing, it is not what the author intended, and
AGENTS.md states the property directly: *"A guard naming an untracked path would skip forever and
silently."*

### The gate for this class is structurally blind

`tools/check-install-prefix.sh:175`:

```sh
local re_ship="(^|[^/{}[:alnum:]._-])tools/($alt)/[A-Za-z0-9_.-]+\.(sh|py|js|md|json|toml)"
```

`$alt` is the kit-directory alternation derived at `:46` from `git ls-files -- 'tools/*/*'`. The
needle therefore requires a `tools/<kit>/<file>` shape. `tools/gate-legs.json` sits directly under
`tools/` and matches nothing. Confirmed:

```
$ bash tools/check-install-prefix.sh --list | grep -c 'check-testsuite-counts'
0
$ bash tools/check-install-prefix.sh ; echo rc=$?
rc=0
```

The gate is green and the literal is invisible to it.

### Not covered by

`TOOL-aBoundedCeiling-7` names `.githooks/pre-push` and `tools/run-gates/gate-fingerprint.sh` only,
and its fix sentence is scoped to that hook. `DEPL-dCarriedReceipt-15` is about literal
`tools/<kit>/` paths inside kit bodies — the exact shape `check-install-prefix.sh` already scans, and
not this one. No row names `tools/gate-legs.json` as a hardcoded literal in a shipped body.

### Fix

`MANIFEST="${GATE_LEGS:-$(dirname "$(git -C "$(dirname "$0")" rev-parse --show-prefix)")/gate-legs.json}"`
or simpler, resolve it as this script's own sibling the way `run-gates.sh` does. Then widen
`check-install-prefix.sh`'s needle to cover files directly under `tools/`, or add
`tools/gate-legs.json` as its own needle — the second is one line and observable RED today.

---

## F4 — MEDIUM. Sibling harnesses: one collects a field and drops it, the other counts, reports and returns it.

`tools/workflows/drift-audit-code.js` and `drift-audit-state.js` are a deliberate pair, born from one
shape and last fixed together by `TOOL-dTieredTribunal-3`, which added a run-integrity block to each
of their synthesis prompts.

`drift-audit-state.js` asks its skeptics for `severityCorrection` and then never reads it:

- `:289` — declares `severityCorrection: { type: 'string' }` in the skeptic output schema
- `:319` — *"Mark 'partial' when the fact is real but severity/impact is overstated; give the corrected severity in severityCorrection."*
- `:322` — lists it as an optional returned key
- `:385` — `severityCorrection: v && v.severityCorrection,` carries it into `judged[]`
- …and that is every occurrence in the file.

`drift-audit-code.js` does all three remaining steps:

- `:377` — `const downgrades = judged.filter((f) => f.verdict === 'partial' && f.severityCorrection).length`
- `:415` — interpolates `${downgrades} severity correction(s)` into the run-integrity `note`
- `:467` — returns `severityCorrections: downgrades`

`tier2-review.js` has zero occurrences and is internally consistent — it never asks for the field.
So the divergence is exactly within the pair that is supposed to be one.

**Impact.** The state harness's returned object omits a key its sibling returns, so a caller running
both waves and comparing run-integrity gets an asymmetric contract; and the state wave's
`note` — the one line whose job is to say what degraded — cannot say how many severities the skeptics
corrected, even though its own synthesis prompt tells the writer to print *"PARTIAL findings with the
corrected severity beside the original"*.

**Class.** `memory/gotchas/degradation-known-but-unreported.md` (the counter that reaches the caller
never reaches the report) combined with
`memory/gotchas/amendment-leaves-its-other-half-standing.md`. `TOOL-dTieredTribunal-16` files the
first class against `tier2-review.js` only; this is a separate file and a separate field.

**Fix.** Three lines, copied from the sibling. Worth doing in the same commit as any
`TOOL-dTieredTribunal-16` work so the three harnesses converge rather than two of three.

---

## F5 — LOW. The third kit-ships-doc parity gate still runs the form its two siblings migrated off, each with the reason in its own header.

Three gates do one job — *the document this kit SHIPS, rendered for this install, must equal the
document this repo RUNS ON*:

| gate | mechanism | wired through the gated seam? |
|---|---|---|
| `tools/memory-tree/kit-dogfood-parity.test.sh:56-88` | marked inline copy of `render_doc` | yes — byte-gated by `tools/lib/resolve-python.test.sh` |
| `tools/workflows/check-protocol-parity.test.sh:39` | `sed -e "s\|{{TOOL_ROOT}}\|$TOOLROOT\|g"` | no, but it renders a real `{{…}}` placeholder |
| `tools/unattended/check-unattended.sh:1193` | `sed -e "s\|$PREFIX\|\|g"` — unanchored, global, over the LIVE copy | **no — this is the retired form** |

Both siblings document the retired form as defective, in their own headers:

- `kit-dogfood-parity.test.sh:21-27` — *"It used to strip a literal `tools/` from the live copy with
  an unanchored global `sed`, which was wrong twice over: it also stripped every `tools/` that was
  not a kit path … and it left the SHIPPED templates spelling a root install."*
- `check-protocol-parity.test.sh:35-38` — *"The old form was an unanchored global `sed "s|tools/||g"`
  over the LIVE copy, which stripped every occurrence of `tools/` rather than a leading kit path."*

`check-unattended.sh:1190-1193` is still that form, one kit over, and
`tools/unattended/PROTOCOL.template.md` carries zero `{{…}}` placeholders (measured — the other two
shipped docs carry 10 and 9) so it cannot be migrated by rendering alone.

**Honest impact statement:** this is LATENT today. Measured at HEAD, neither
`tools/unattended/PROTOCOL.template.md` nor `memory/guides/UNATTENDED-PROTOCOL.md` contains a single
`tools/` or kit-path occurrence, so `$PREFIX` substitutes nothing and the two files are byte-identical
(`diff` returns clean). The strip is inert. It becomes live the moment the unattended protocol names
a kit path, which is a document about a kit. Reported as duplication that has drifted rather than as
a live defect, and severity set accordingly.

**Fix.** Give `PROTOCOL.template.md` a `{{TOOL_ROOT}}` placeholder and render it, converging on the
mechanism the other two use; or state in `check-unattended.sh`'s check-10 header why this pair is
deliberately different, the way `check-dead-paths.sh:53` does for its waiver keying.

---

## Considered and NOT reported

- **12 inline `resolve_python` copies** — by design, and byte-gated by the parity table in
  `tools/lib/resolve-python.test.sh`. Working as intended.
- **`.claude/hooks/agent-cap.js` == `tools/hooks/agent-cap.js`** — byte-identical, and
  `tools/hooks/agent-cap.test.sh:606-624` asserts it including an explicit
  *"the wired copy is MISSING (parity must not be satisfiable by absence)"* arm. Exemplary; not a
  finding.
- **Five waiver registries, five grammars** — `check-dead-paths.sh:53-56` states the divergence is
  owner-ruled and explicitly says *"Do not 'restore' the parity."* Not a finding. Note in passing
  that `TOOL-dSpentCeiling-6`'s text (*"`tools/install-prefix-waivers.txt` and
  `tools/dead-path-waivers.txt` both do this"*) is now **half wrong**: `dead-path-waivers.txt` was
  re-keyed to text+ordinal at `431d32c0` after that row was filed at `4b26d2b0`. The row is still
  live for `install-prefix-waivers.txt` alone.
- **The five byte-identical memory-tree `load_conf` bodies considered purely as repetition** — folded
  into F1 rather than reported separately, because the parse rule is what matters and it is one rule.
- **`resolve_bash` ×3**, **`unit_rows`/`verb_landed` row grammar**, **`plan_state` vs the memory-tree
  section reader**, **`rosters()` vs `roster_ids`**, **the `args`-guard gap in the two drift-audit
  harnesses** — all already tracked (`TOOL-dSettledRoster-6`, `TOOL-aPromptedMandate-14`,
  `TOOL-dTieredTribunal-17`, `TOOL-dHonouredPark-6`, `TOOL-dTieredTribunal-4`). Not re-reported.

## Commands run (reproduction)

```sh
# F1
W=/tmp/gv-confdrift; git init -q "$W"; mkdir -p "$W/tools" "$W/memory/gotchas"
cp -r tools/memory-tree tools/lib "$W/tools/"
printf -- '---\nname: bad\n---\nno kind field\n' > "$W/memory/gotchas/bad.md"
printf '# c\nMEMORY_ROOT=memory   # note\nDISCIPLINES="tooling"\nFAMILIES="tooling:TOOL"\n' > "$W/.memory-tree.conf"
cd "$W" && git add -A && python tools/memory-tree/gotchas.py --check; echo rc=$?   # rc=0, silent
printf '# c\nMEMORY_ROOT=memory\nDISCIPLINES="tooling"\nFAMILIES="tooling:TOOL"\n' > .memory-tree.conf
python tools/memory-tree/gotchas.py --check; echo rc=$?                            # rc=1, reds

# F2 — the two parsers side by side over identical bytes (see the transcript above)

# F3
W=/tmp/gv-prefix; git init -q "$W"; mkdir -p "$W/scripts"
cp tools/check-testsuite-counts.sh tools/gate-legs.json "$W/scripts/"
cd "$W" && git add -A && bash scripts/check-testsuite-counts.sh; echo rc=$?        # rc=2
cd <repo> && bash tools/check-install-prefix.sh --list | grep -c check-testsuite   # 0

# F5
diff <(sed 's/\r$//' memory/guides/UNATTENDED-PROTOCOL.md) \
     <(sed 's/\r$//' tools/unattended/PROTOCOL.template.md)                        # clean
```
