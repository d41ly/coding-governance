**Serves:** research TOOL-dFramedEntrypoint-1

*Research lens for the `dFramedEntrypoint` design pass — how each proposed slot could be gated, and the immutability verdict. Produced 2026-08-24, node d, against base 9ddcc5c9. Findings in this record were subsequently adversarially verified; where the verification corrected a claim, the verification record wins.*

# Enforcement mechanics for a CLOSED build-README slot set

Lens: how do you gate it. Every claim about code carries `file:line`, read from source in the
worktree at `C:/projects/coding-governance/.claude/worktrees/build-readme-governance-18d6ea`
(branch `branch/build-readme-governance-e1c044`, tip `9ddcc5c9`).

---

## 0. The measurements this report prices against

Taken on this tree, node `d`, 2026-08-24. None of these numbers is authored anywhere; re-derive them
rather than quoting this file later.

| Quantity | Value | How |
|---|---|---|
| tracked build READMEs | **61** | `git ls-files 'memory/builds/*/README.md' \| wc -l` |
| tracked specs | 265 | `git ls-files 'memory/builds/*/spec/*.md' \| wc -l` |
| total AUTHORED bytes (title → first `<!-- gen:`) | **340,532 B** | script over the 61 files |
| median authored block | **4,371 B** | same |
| largest authored block | **32,721 B** — `memory/builds/aBoundedVerdict/README.md` (407 lines) | same |
| authored blocks > 4,000 B | 31 of 61 | same |
| READMEs carrying ≥1 `##` heading in the authored block | **42 of 61** | same |
| **distinct** authored heading texts across the corpus | **136** | census |
| READMEs carrying a `roster:units` pair | **11 of 61** | grep |

Heading census, top rows (this is the migration surface for any closed canon):

```
 14  ## Start here
 12  ## Units
  9  ## Units — the authored roster (M2)
  7  ## Build-level rules
  5  ## Review record
  3  ## Order
  3  ## What this build does NOT do
  3  ### The specs
  3  ## Owner decision menu
  … 127 more, nearly all singletons
```

Note `## Build-level rules` already exists 7 times — the owner's slot 6 has a de-facto name in the
corpus. `## Units` / `## Units — the authored roster (M2)` (21 combined) is **load-bearing for the
build method**: `memory/guides/BUILD-METHOD.md:33` — "The roster is the build README's authored Units
table where one exists, else the conforming specs under…". A closed slot set that drops it changes
M2's detect step.

Live leg costs, from `<git-common-dir>/gate-ledger.tsv` (seconds, one row per leg, last run):

| Leg | s | chunk / subject |
|---|---|---|
| `build README slot contract` | **0.347** | records / repo |
| `harness arms (fail branches armed or pinned)` | 0.374 | declarations / repo |
| `verdict epoch (kit version dates the engine)` | 0.503 | — / repo |
| `kit/dogfood doc parity` | 0.580 | declarations / repo |
| `check-arms selftest` | 1.927 | selftests / kit |
| `verdict-epoch self-test` | 17.772 | selftests / kit |
| `memory hygiene` | **77.234** | records / repo |
| `memory-hygiene self-test` | **181.921** | selftests / kit |

Two spot measurements taken here: `python tools/memory-tree/gen_build_index.py --check-format`
runs in **0.13 s** wall on a warm tree; `git blame --porcelain` over **all 61** build READMEs costs
**2.25 s** total; `git log --format=%H -- <readme>` over all 61 costs **2.71 s**.

---

## 1. The slot walk today

### 1.1 The constants

`tools/memory-tree/gen_build_index.py:46-74` declares four marker families:

- `MARK_OPEN` / `MARK_CLOSE` = `<!-- gen:build-index -->` / `<!-- /gen:build-index -->` (`:46-47`)
- `PLAN_OPEN` / `PLAN_CLOSE` = `<!-- roster:units -->` / `<!-- /roster:units -->` (`:53-54`) — the
  AUTHORED plan pair. The header comment at `:50-52` is explicit: "This generator NEVER writes
  between these two markers… It is listed here so the slot walk can FIND it, not so anything can
  render into it."
- `UNITS_OPEN` / `UNITS_CLOSE` = `<!-- gen:build-units -->` / `<!-- /gen:build-units -->` (`:66-67`),
  **nested inside** `build-index` and deliberately **not** in `GEN_REGIONS` (`:61-65` states why).
- `GEN_REGIONS` (`:69-74`) — a 4-tuple in CANONICAL SLOT ORDER: `build-index`, `build-order`,
  `build-edges`, `build-docs`.

### 1.2 `slot_violations` — the whole predicate

`gen_build_index.py:978-1006`. Read literally, it does this:

1. Splits the README on `\n` (`:984`).
2. For each of the four `GEN_REGIONS`, finds its open and close index via `_marker_index`
   (`:970-975`, which requires **column-0 exact equality after stripping exactly one trailing CR**).
   A pair counts only when both are present and `close > open` (`:987-989`).
3. **If no registered region pair is present at all, it returns `[]` (`:990-991`).** A README with no
   generated region is silently clean here — the "no pair" refusal lives in `apply_region`
   (`:911-914`) on the render path, not in the slot walk.
4. `first_open` = the minimum open index across present pairs (`:992`); `inside` = the union of all
   `[open, close]` ranges (`:993`).
5. **Trigger 1** (`:996-998`): any line with `l.strip()` truthy, at index `> first_open`, not in
   `inside` → `"authored content after the first generated marker"`.
6. **Trigger 2** (`:1000-1004`): if `PLAN_CLOSE` is present and sits **before** `first_open`, every
   non-blank line between them → `"authored content between the plan pair and the generated region"`.
7. Returns a sorted deduplicated list of `(1-based line, reason)` (`:1005`).

The docstring at `:979-983` records why there are two triggers and not one: "An earlier draft of the
owning spec named only the first, which would have passed the one README in the corpus that already
carries a plan pair."

**Therefore, exactly what the contract permits today:**

- Front matter, title, and **an arbitrary quantity of arbitrary prose** between the title and the
  first generated marker. There is no upper bound, no heading vocabulary, no required section, no
  ordering rule inside that block. Nothing checks that the `#` title exists at all here.
- A `roster:units` pair anywhere **at or after** `first_open` is unreachable by trigger 2 and its
  contents would be caught by trigger 1 (it is not in `inside`).
- Prose **between two generated regions** — forbidden (trigger 1).
- Prose **after the last generated close** — forbidden (trigger 1).
- Prose between the plan close and the first generated open — forbidden (trigger 2).
- The four generated regions in **any order** — permitted. `slot_violations` never compares
  `first_open`'s identity against `GEN_REGIONS[0]`; canonical order is enforced only by
  `insert_region`'s **creation** position, never by a check.
- Blank lines anywhere — permitted (`l.strip()` gate).
- Content inside a fenced code block after `first_open` — **forbidden**, because `slot_violations`
  is not fence-aware, unlike `strip_records_sentence` (`:788-830`, which explicitly is, `:794-798`).

### 1.3 `insert_region`

`gen_build_index.py:1009-1029`. Creates a missing pair at its canonical `GEN_REGIONS` position by
anchoring on **sibling regions only** — first it walks *backwards* through `GEN_REGIONS` looking for
an earlier region's CLOSE and inserts after it (`:1022-1025`); failing that, forwards for a later
region's OPEN and inserts before it (`:1026-1028`); failing both, appends at EOF (`:1029-1030`).

The docstring (`:1010-1014`) gives the reason and it constrains the new design directly: "Over a
README that violates the slot sequence there is no well-defined 'after the prose' point, which is why
this anchors on sibling REGIONS only — that is the branch every corpus write takes until the surgery
unit lands."

`do_check_format` (`:1137-1157`) is the only caller of `slot_violations`. It selects
`git ls-files -- memory/builds/` filtered to `endswith("/README.md")` (`:1145-1146`) — so it grades
tracked paths, not the worktree listing. Its own docstring (`:1138-1142`) records that it is
"deliberately NOT reachable from `plan()`, `--write` or `--check` (S1a)".

Gate leg: `tools/gate-legs.json:298-307`, name `"build README slot contract"`, `chunk: "records"`,
`subject: "repo"`, **no guard** — it runs on every bar. Mirrored in
`tools/memory-tree/kit.toml` (`[[gate_leg]] name = "build README slot contract"`) and pinned in
`tools/govkit/subject-pins.tsv:16`.

### 1.4 Why POSITIONAL — the recorded reason, and the owner's refusal

Three records bind. **Quote them, do not paraphrase them.**

**(a) The spec's own "Alternatives rejected".**
`memory/builds/aRuledFrontispiece/spec/2026-08-16-spec-TOOL-aRuledFrontispiece-1.md`, §4:

> Bounding the prose by a marker pair of its own was rejected: it makes every README carry two more
> lines to solve a problem that position already solves, and an author who puts prose in the wrong
> place is not helped by being asked to wrap it.

and, immediately after:

> Detecting the plan slot by heading text rather than by a marker was rejected because
> `check_authorization` in the unattended kit byte-compares a marker-delimited region across a base
> commit, and a heading is not a delimiter it can address.

**Read these two together — they cut in opposite directions.** Markers were refused *for prose*;
headings were refused *for the plan slot*, and only because a `check_authorization` byte-compare
needed a delimiter. That second refusal is now **moot**: `TOOL-aBoundedVerdict-11` moved the frozen
authorization scope off the authored pair onto the generated units region's ID set
(`tools/unattended/unattended.sh:1245-1259` and its comment block `:1241-1252`), and the dossier
records the pair as narrowed to a single remaining reader. So "a heading is not a delimiter it can
address" no longer blocks anything, because nothing byte-compares that slice any more.

**(b) The owner's dated ruling**, in the build README —
`memory/builds/aRuledFrontispiece/README.md:194-197`:

> That stopped being true when the owner chose the position-bound prose contract on 2026-08-16:
> conforming the corpus means MOVING authored sections in a double-digit number of build READMEs,
> which no `--check` output can review and which belongs to other nodes' build records.

**(c) The dossier's statement of the same ruling** —
`memory/map/features/build-readme-surface.md:29-32`:

> **The slot sequence is positional, not delimited.** Front matter, title, ONE authored prose block,
> the authored `roster:units` plan, then the generated regions. Bounding the prose with markers
> instead was considered and refused by the owner: it would have let authored content sit anywhere
> and made the contract a labelling convention rather than a shape.

**What was refused, precisely.** The owner refused **marker-pair-bounded prose as the mechanism for
locating the authored block**, on two grounds: (i) it costs two lines per README to solve a problem
position already solves, and (ii) it would let authored content sit *anywhere in the file* as long as
it were wrapped — the contract would grade labelling instead of shape.

**What was NOT refused.** Nothing in any of the three records refuses a **closed heading canon within
the authored block**. The refusal is about *where the authored block sits*, not about *what may be
inside it*. The owner's new ask is orthogonal: keep position-bound bounding (which is what
`slot_violations` already does) and add an internal shape check. A proposal that keeps
`slot_violations` unchanged and adds a heading-sequence walk **does not re-open** the 2026-08-16
ruling. A proposal that introduces per-slot marker pairs **does** re-open it and needs the owner to
reverse ruling (c) explicitly.

One review finding is worth carrying forward. `memory/builds/aRuledFrontispiece/reviews/
2026-08-16-review-TOOL-aRuledFrontispiece-1-1.md:110-119` killed a sibling spec for exactly this
confusion: it observed that a prose block bounded by POSITION "has no anchor", so an
opened-and-not-closed failure shape "describes the marker-delimited block spec-1 §4 explicitly
rejected". The lesson for this design: **refusal messages must be expressed in position/sequence
terms, never in open/close terms**, or a reviewer will read the marker design back into it.

---

## 2. How you enforce a CLOSED heading set

### 2.1 The nearest precedent — check 12's section canon, exact mechanism

`tools/memory-tree/check-memory-hygiene.sh`, and the owner explicitly cited "similar to the SPEC
template". Here is what it actually does.

**The canon is a shell heredoc string literal** at `:729-737`:

```
SPEC_CANON='## 1. Goal
## 2. Scope (IN)
## 3. Non-goals (OUT)
## 4. Design
## 5. Production-readiness checklist
## 6. Acceptance criteria
## 7. Gates
## 8. Open questions
## 9. Revision log'
```

and a ten-section variant built by concatenation at `:746-747`:
`SPEC_CANON10="$SPEC_CANON\n## 10. Reuse audit"`.

**The comparison is one string equality over a newline-joined list of headings**, inside the single
batched awk (`:988-997`):

```awk
ng = 0; got = ""
for (i = 1; i <= n; i++) if (body[i] ~ /^## /) { got = (++ng == 1) ? body[i] : got "\n" body[i] }
want = (fdate != "" && fdate >= cut10) ? canon10 : canon
wantn = (want == canon10) ? "ten" : "nine"
if (got != want) {
  print f " (## sections differ from the canonical " wantn " of " mroot "/TEMPLATE-SPEC.md):"
  print "\001\t" f      # the excerpt is a real diff — rebuilt by the post-pass below
}
```

Seven properties worth copying verbatim:

1. **`^## ` only.** `###` sub-heads are invisible to the canon, which is what lets a spec nest
   freely inside a section. (`:990`)
2. **The body is UNFENCED first.** The awk inlines the fence machine at `:777-790` — CR strip,
   marker-matched fences (only the marker that opened closes), trailing blank lines trimmed
   (`:792-797`). A `## ` line inside a code fence is not a heading. `slot_violations` has no
   equivalent and would need one.
3. **Exact sequence, exact text, exact count** — one `!=` over the joined string. Missing, extra,
   reordered and misspelled are all one finding. No partial credit.
4. **Grandfathering is by FILENAME DATE, not by content or mtime** (`:846-848`: `fbase`/`fdate`
   extracted from the basename; `:992` selects the canon). The whole check is gated on
   `SPEC_FORMAT_CUTOFF` being non-empty (`:728`) and each file is skipped below the cutoff
   (`:766`). `.memory-tree.conf:21` sets it to `2026-07-15`.
5. **Tier-1 is exempt from the canon** and only from the canon — `if (hdr ~ /Tier-1/) next` at
   `:987`, deliberately placed *below* the streams, witness, rev-log and §8 assertions
   (`:865-869` explains the hoist).
6. **The diagnostic is a REAL `diff`, rebuilt outside awk** via a `\001` sentinel record and a
   post-pass (`:1015-1036`), with the canon re-chosen by the same basename-date rule (`:1029-1031`)
   — a comment at `:1027-1028` records that diffing the wrong canon "printed a BLANK excerpt for the
   primary new failure mode — a diagnostic that cannot describe its own finding."
7. **A separate empty-body test** rides alongside (`:1000-1011`): a section whose body has no line
   matching `/[^ \t]/` before the next `## ` is a finding — "write N/A — <why>".

**Cost of this shape, measured:** it is one arm of the single batched awk that already reads every
spec; `TOOL-aBatchedLintel-1` collapsed ~13 forks per spec into it (`:750-757`). The whole `memory
hygiene` leg is 77.2 s over 265 specs plus everything else.

**What check 12 does NOT do, and the difference matters here:** it never asserts a section's *content*
means anything, it never asserts a section is short, and it has no per-section budget. The only size
axis anywhere near it is check 7's per-line character cap, which is file-class-scoped, not
section-scoped.

### 2.2 Candidate A — exact-heading-sequence walk inside `slot_violations`

**Shape.** Extend `slot_violations` (or add a sibling `slot_canon_violations`) that, for the span
`(title_index, first_open)`, collects every unfenced `^## ` line into a list and compares it against a
module-level canon tuple, exactly as check 12 does:

```python
BUILD_README_CANON = (
    "## What this build is",        # slot 3, immutable
    "## Expected improvements",     # slot 4
    "## Detriments if not built",   # slot 5
    "## Build-level rules",         # slot 6
)
```

plus (a) a required `#` title as line `fm_end+2`-ish, (b) an empty-body refusal per section, and
(c) a "no prose before the first canon heading" refusal so preamble cannot leak back in.

**What it can see.** Heading text, heading order, heading count, section presence, whether a section
body is empty, and — with one more loop — per-section byte/char counts. It sees fenced content
correctly *if* you port `unfenced_lines` (`gen_build_index.py:175-211`, already in the module) into
the walk. It sees `###` sub-heads only if you choose to (recommend: ignore them, as check 12 does, so
a slot can be structured internally).

**What it cannot see.** Whether slot 3's sentence describes this build. Whether slot 4's bullets are
improvements rather than a task list. Whether slot 6's paragraph is a rule. Whether the prose is
*relevant*. All four of the owner's slots are semantic asks with a structural gate; the gate's header
must say so (§7 of the charter: "A gate's OWN header states what it does NOT check").

**False positives.** Near-zero on a conformed corpus — string equality has no fuzzy edge. The real FP
risk is the fence blindness `slot_violations` has today: a README that *quotes* the canon inside a
```` ``` ```` block (and at least one build README does quote README boilerplate — see
`strip_records_sentence`'s docstring at `:794-798`, "a README documenting this very migration quotes
the retired boilerplate inside a code block") would produce a phantom heading. **Port the fence
reader or this fires on landing.**

**False negatives.** A conforming heading set with garbage under every heading passes. A slot 4 with
one bullet reading "TBD" passes. Structural, not semantic.

**Cost.** Zero new processes. `--check-format` is 0.347 s today over 61 files; the walk is one more
pass over text already read at `:1148`. **Arms cost: ZERO in `check-arms.py`** (see §6) — the module
is Python and outside the arms population. Selftest arms: budget 2 per refusal branch (a red fixture
and a green one), so a 5-refusal design ≈ 10 new `arm()` calls against the current 71 in
`do_selftest` (`gen_build_index.py:1205-1210` is the harness; existing slot arms at `:1485-1503`).

**Migration cost.** 42 of 61 READMEs carry headings, 136 distinct texts. Either (i) a dated cutoff
keyed on **front matter `opened:`** (there is no filename date on a build README, so check 12's
basename trick does not transfer — `opened:` is a REQUIRED front-matter key, `gen_build_index.py:112`,
and is already date-validated at `:246-247`), grandfathering the existing 61 and binding only new
builds; or (ii) a corpus surgery over 61 files, which is exactly the work
`memory/builds/aRuledFrontispiece/README.md:194-197` describes as "MOVING authored sections in a
double-digit number of build READMEs, which no `--check` output can review".

### 2.3 Candidate B — one marker pair per slot

**Shape.** `<!-- slot:description -->` … `<!-- /slot:description -->` × 4, read with the same
`_marker_index` contract, with `apply_region`'s three refusals per pair (`:911-917`).

**What it can see.** Presence, uniqueness, order, non-inversion of each pair, and byte extent of each
slot with no ambiguity at all. It also gives a machine a stable address for slot 3 — which is what an
immutability check would want (§3).

**What it cannot see.** Same semantic blind spots as A, plus: a marker pair says nothing about what
sits *outside* every pair, so you still need `slot_violations`' trigger 1 to forbid loose prose.

**False positives / negatives.** Very low FP. The FN is the one the owner already named: "it would
have let authored content sit anywhere and made the contract a labelling convention rather than a
shape" (`memory/map/features/build-readme-surface.md:31-32`).

**Cost.** 8 new lines in every one of 61 READMEs plus every future one. **And it re-opens a recorded
owner ruling** — `TOOL-aRuledFrontispiece-1` §4 and the 2026-08-16 position-bound choice. It also
touches the four-reader marker contract: `tools/memory-tree/marker-contract.test.sh:1-35` documents
that marker-region well-formedness has **four readers** (three awk in the unattended kit, one Python
here) and that the case table in that file *is* the contract. New pairs read by only one reader do
not enlarge that contract, but any new *reader* does.

**Verdict: do not propose this without an explicit owner reversal.** If the owner wants it, the ask
is a one-line reversal of ruling (c), recorded as a new decision id, not a spec re-litigating §4.

### 2.4 Candidate C — front-matter-carried description (slot 3 only)

**Shape.** `description: <one sentence>` as a front-matter key, alongside the existing
`slug node opened streams roster ids` (`gen_build_index.py:112`).

**What it buys.** The front-matter parser (`:213-250`) is **open-keyed** — it accepts arbitrary
`key: value` at column 0 and only *requires* `REQUIRED_KEYS` (`:242-244`). So a new key is admissible
today with a one-tuple edit. `check_authorization`'s awk (`unattended.sh:1146-1153`) already parses
three optional front-matter keys the same way, so the precedent is live. And a front-matter key has a
natural immutability story: it is a single line at a fixed address.

**What it costs, and this is the trap.** **Check 7 does not measure the front-matter block at all.**
`check-memory-hygiene.sh:513-522`:

> THE FRONT-MATTER BLOCK IS NOT MEASURED. It is machine-written, not read prose: `--write` rewrites
> `ids:` from the derived roster, and that one line is 479 characters in the largest build. It cannot
> be wrapped — `parse_front_matter` refuses an indented continuation and `check-unattended.sh` check
> 13 parses the same block — so measuring it would cap a value no author controls and no renderer may
> reflow.

A `description:` in front matter is therefore **exempt from every character guard in the repo** and
cannot be wrapped (`:232-236` raises on an indented continuation). A one-sentence rule becomes a
one-line rule of unbounded width, invisible to check 7. You would have to add a key-scoped cap inside
`parse_front_matter` — a third place caps live.

There is a second, recorded objection. `memory/builds/aRuledFrontispiece/README.md:47-52`:

> `TOOL-aMouldedFolio-1` refused a front-matter SCHEMA and made `ids:` derived rather than validated,
> on the ground that parity and freshness gates are TRUTH-BLIND — both stay green over a
> self-consistent wrong render.

Adding a validated front-matter key is not automatically the refused schema (S10 of
`TOOL-aRuledFrontispiece-1` added one and was required to say why), but a spec proposing one **owes
that argument**.

**Verdict:** viable for slot 3 *only*, and only with an explicit width cap. Slots 4–6 are multi-line
by construction and cannot live in front matter at all (`:232-236`).

### 2.5 Comparison

| | A: heading canon | B: marker pairs | C: front matter |
|---|---|---|---|
| re-opens the 2026-08-16 owner ruling | **no** | **yes** | no |
| bytes added per README | 0 (headings replace headings) | 8 lines | 1 line |
| sees slot extent unambiguously | yes, between headings | yes | yes (one line) |
| fence-safe | only if you port `unfenced_lines` | yes (column-0 exact) | n/a |
| per-slot budget expressible | yes | yes | yes but check 7 is blind to it |
| covers slots 4/5/6 | yes | yes | **no** |
| new readers to keep in contract | 0 | 1+ (marker-contract.test.sh) | 0 |
| arms cost in `check-arms.py` | 0 (Python) | 0 (Python) | 0 (Python) |
| migration over 61 READMEs | heading rewrite, or `opened:` cutoff | 8 lines × 61 | 1 line × 61 |

---

## 3. IMMUTABILITY — "authored once, never re-authored"

This is a claim about HISTORY. Nothing in the current bytes can express it. Four mechanisms, priced.

### 3.0 First, what already exists in this repo

**There IS a base-comparison seam, and it deliberately stopped being a byte compare.**

`check_authorization` — `tools/unattended/unattended.sh:1119-1279`. What it does:

- `blob=$(GIT show "$base:$rel")` where `rel` is the build README (`:1127`); a missing blob is
  `fail 6` (`:1128-1130`).
- Refuses a blob that does not open with `---` (`:1136-1140`).
- Parses `slug`, `authorized-by`, `playbook`, `pieces` from the blob's front matter in **one awk,
  one `GIT show`** (`:1146-1153`), and refuses a slug mismatch with `fail 20` (`:1223-1226`).
- **The scope comparison is now a SUBSET test over an ID SET, not a byte compare** (`:1241-1265`):
  it extracts the `gen:build-units` region at BASE and at HEAD via `region()` and refuses only when a
  BASE id is missing from HEAD (`comm -23`, `:1261`).

The comment at `:1250-1254` states exactly why byte-equality was abandoned, and **it is the single
most important precedent for the owner's immutability ask**:

> WHY IDS AND NOT BYTES. A row carries the unit's status, rev and last-change date, all rendered from
> its spec header, so they move whenever a unit is built. A byte-level "no row changed" test would
> refuse every run that BUILT anything, on the one item `verb_close` will not override — strictly
> worse than the opt-in hole it replaces.

And `:1264-1271` records the cutoff mechanism that made it landable at all: a run's BASE is pinned
*before* its own work, so the BASE of the run landing the migration cannot carry the region the check
wants — hence `UNITS_REGION_CUTOFF`, below which presence-based opt-in survives. **Any
history-comparing immutability check for slot 3 needs the identical cutoff, for the identical
reason.**

`region()` itself (`unattended.sh:470-479`) is the reusable extractor: exactly one open, exactly one
close, close after open, prints the slice, exit 3 on malformation — and its comment at `:464-469`
records that the missing order check once caused `splice` to **delete the owner's authored mandate
block**. `splice()` (`:483-495`) is the write half, kept deliberately with no live caller.

**Is that seam reusable here? Partially.** `region()` addresses a *marker pair*. It cannot address a
heading-bounded slot. If slot 3 is heading-bounded (candidate A), you get no reuse from `region()` —
you write a new extractor in Python beside `slot_violations`. If slot 3 is marker-bounded
(candidate B), `region()` is directly reusable but you inherit the four-reader contract obligation.

Also note the honest limit stamped on the second-opinion copy of this check,
`tools/unattended/check-unattended.sh:911-914`:

> `rb` is read from a file the run writes. This is an internal-consistency assertion over run-written
> facts, stable and offline and deterministic - not an authorization verdict. What makes it one is
> running this same leg in a clone the run never touched.

The same limit binds any immutability gate that runs under the same uid as the editor.

**And the answer to the DECISIONS.md question: nothing enforces it.** `APPEND_ONLY_ERE` at
`check-memory-hygiene.sh:104` —

```sh
APPEND_ONLY_ERE="^$M/(DECISIONS\.md$|decisions/|archive/)"
```

— is published as a print mode (`:105-107`) and used in exactly **two** places, both as an
**EXEMPTION**: check 2's broken-link scan skips those paths (`:226`), and `corpus_ids.py:263` skips
them for dead-path repair. There is no gate anywhere that compares `memory/DECISIONS.md` against a
base and refuses a rewritten line. The charter's "the decision log is append-only (never rewrite a
ratified record — supersede with a new id + note)" is a **documented manual check**, and it is the
honest precedent for option (d) below.

### 3.1 (a) Git-history comparison

Three sub-variants; they have different failure modes.

**a1 — `git log --format=%H -- <readme> | tail -1`, then `git show <first>:<readme>`, extract slot 3,
byte-compare against HEAD.** ("first-commit-wins", also §3.3.)

- Cost: **measured 2.71 s** for the `git log` half over all 61 READMEs; add one `git show` per file
  ≈ 61 more processes. Call it **5–7 s** added to a 0.35 s leg — a 15–20× cost increase on that leg,
  still small against the 77 s hygiene leg but no longer "free". Node `d`'s AV taxes every exec
  ~0.022 s (recorded in this user's memory), so process count is the cost, not I/O.
- **Failure mode 1 — rewrites.** `--format=%H | tail -1` returns the oldest commit *reachable in this
  history*. A squash-merge, a filter-branch, a shallow clone (`--depth`), or a fresh `git init`
  import returns a different commit, or none. `hygiene-parity.test.sh:54-63` already carries this
  exact lesson: "A shallow clone or a squashed import does that" — and it treats the empty case as a
  **hard exit 2**, not a skip. Copy that.
- **Failure mode 2 — renames.** A build folder renamed loses its history without `--follow`; with
  `--follow`, git's rename detection is heuristic and `--follow` is documented-fragile with
  pathspecs. `memory/project/legacy-files.txt` exists because five records already carry
  grandfathered names.
- **Failure mode 3 — the one that actually kills it.** *The first commit of a README is very often
  not the commit that authored slot 3.* A build folder is typically scaffolded and then filled. So
  "the description at the first commit" is frequently empty or a placeholder, and the check would
  freeze the placeholder forever.
- **Failure mode 4 — worktrees.** `git log` in a linked worktree reads the shared object store and is
  fine; but a *fresh* worktree created from a shallow clone inherits the shallow graft. Same as 1.

**a2 — `git log -L <start>,<end>:<path>`.** Rejected on measurement grounds before writing it: `-L`
requires *line numbers*, and slot 3's line numbers move every time anything above it changes
(front matter `ids:` is rewritten by `--write`). A line-range immutability check on a file whose
earlier lines are machine-rewritten is a check that reports a change on every render.

**a3 — `git blame --porcelain` over the slot's line range, assert every line's commit is the same and
is the oldest.** Cost measured: **2.25 s for all 61 READMEs** — cheaper than a1, because blame is one
process per file with no second `show`. `tools/drift-audit/drift_report.py:974-976` already does
exactly this and records the discipline: "THE CANDIDATES FIRST, THE BLAME ONLY IF THERE ARE ANY.
`git blame` is a process per README and this audit is meant to run in seconds". Its
`_build_blame_dates` (`:873-...`) is a working porcelain parser you can lift.
- Failure mode: **blame attributes a whitespace fix, a typo fix, or a reflow to a new commit.** The
  owner's rule is "never re-authored", not "never touched". Blame cannot tell those apart. It will
  red on a comma.

**Verdict on (a): all three are wrong for this rule.** The claim "never re-authored" is semantic and
git records "changed". The one variant that is defensible is a1 restricted to a **content** compare
of the extracted slot (not the line range), with the shallow/squash case a hard exit 2 — and it still
fails mode 3.

### 3.2 (b) A content hash pinned in front matter or a registry

**Shape.** On first write, `--write` computes `sha256(slot-3 text, normalized)` and stores it as
front-matter `description-sha:` or as a row in `memory/project/<something>.txt`. The check recomputes
and compares.

**What it actually buys: nothing against the threat.** The hash and the text are in the same commit,
written by the same actor. Anyone who edits slot 3 re-runs `--write` (or edits the pin) and the check
agrees with the new text forever. This is precisely the class the charter names — §7's "A guard that
shares a variable with the thing it guards is not a guard… A backstop that reads the same state the
bug corrupts is disabled by the bug it exists to catch" — and the class
`TOOL-aMouldedFolio-1` cited when it refused a front-matter schema: "parity and freshness gates are
TRUTH-BLIND — both stay green over a self-consistent wrong render"
(`memory/builds/aRuledFrontispiece/README.md:47-50`).

A hash pinned in a **separate append-only registry** is marginally better — it makes the edit *visible
in a diff* (which is `subject-pins.tsv`'s stated theory: "THIS FILE GRADES CHANGE, NOT CORRECTNESS.
It exists so a subject cannot move without the move appearing in a diff",
`tools/govkit/subject-pins.tsv:6-8`). That is an honest and cheap claim, and it is much weaker than
"immutable".

**Cost.** ~40 lines in `gen_build_index.py`, one registry file (which then needs a row in check 3's
`project/` allowlist at `check-memory-hygiene.sh:303-307` — that `case` is a **closed set of seven
filenames**, and an eighth registry reds check 3 until it is added).

### 3.3 (c) First-commit-wins

Covered as a1 above. One extra note: it is the only variant with a *documented, landable* cutoff
story, because `check_authorization` already ships one (`UNITS_REGION_CUTOFF`,
`unattended.sh:1266-1276`) and the reason transfers exactly — the run that lands the migration has a
BASE that predates the rule.

### 3.4 (d) Social / documented check

**This is what `memory/DECISIONS.md` already gets**, and it is the repo's own answer to the identical
question. The charter (§6) states the rule; `APPEND_ONLY_ERE` names the paths for *other* checks'
exemptions; no gate enforces it. Cost: one sentence in the rendered template, one bullet in
`memory/HYGIENE.md`, zero seconds, zero arms.

The charter permits this explicitly: "Document deliberate gate exemptions together with their
compensating manual check — an exemption is not coverage" (§7).

### 3.5 Immutability verdict

**Do not gate immutability. Gate SINGULARITY and ADDRESSABILITY; document immutability.**

Concretely: the gate asserts slot 3 **exists, is exactly one section, is non-empty, and is within its
budget**. The rule "authored once, never re-authored" goes in the rendered template and in
`HYGIENE.md` as a documented manual check, citing the DECISIONS.md precedent by name. If the owner
insists on a machine claim, the honest one is the `subject-pins.tsv` shape: a hash in a tracked
registry that **makes an edit appear in a diff**, sold as change-detection and never as immutability
— and its header must say so.

The reason to refuse the strong form, stated in the repo's own terms: a check running under the same
uid as the editor, reading state the editor writes, is not an integrity check
(`unattended.sh:1220-1235` and `check-unattended.sh:911-914` both say this about a far more carefully
constructed version of the same idea, and that one at least reads a blob from a remote-observed BASE).

---

## 4. Character guards — where a per-slot budget lives

### 4.1 What exists

- **Check 6, byte + line caps by CLASS.** `check-memory-hygiene.sh:399-486`. `index_set()`
  (`:400-427`) enumerates the capped population; build READMEs enter at `:417` with a comment at
  `:411-416` recording that they are their own class. The awk at `:461-482` picks the class by path
  prefix and applies `BUILD_README_CAP_BYTES` / `BUILD_README_CAP_LINES` (`:471-473`). A **line cap of
  0 means no independent line cap** (`:474-476` and the validation at `:71-76`).
- **Check 7, per-line character cap by class.** `:488-548`. `sel7` excludes guides and RUN.md via
  `ex7` (`:495-496`); the awk at `:509-544` picks `BUILD_README_ENTRY_CAP_CHARS` for a build README
  (`:515`), skips the front-matter block entirely (`:521-527`), is fence-aware (`:528-534`), and
  exempts `^#` lines and table rules (`:537-538`).
- **The numbers.** Engine defaults at `:43-54`:
  `INDEX_CAP_BYTES=20480 ; INDEX_CAP_LINES=250` · `GUIDE_CAP_BYTES=61440 ; GUIDE_CAP_LINES=750` ·
  `BUILD_README_CAP_BYTES=25600 ; BUILD_README_CAP_LINES=0` ·
  `DOSSIER_CAP_BYTES=20480 ; DOSSIER_CAP_LINES=0` ·
  `ENTRY_CAP_CHARS=300 ; BUILD_README_ENTRY_CAP_CHARS=350`.
  **`.memory-tree.conf` declares `INDEX_CAP_*` and `DOSSIER_CAP_*` and does NOT declare either
  `BUILD_README_*` key** (verified: `grep -n BUILD_README .memory-tree.conf` → no match). So both
  build-README numbers are **kit-owned defaults**, which `.memory-tree.conf:204` states in prose:
  "Every row document except a build README (25,600, kit-owned)".

### 4.2 The conf trap, stated precisely

`check-memory-hygiene.sh:16-54` **pre-sets every conf key**, then `:55` sources the conf **over**
them:

```sh
[ -f "$ROOT/.memory-tree.conf" ] && . "$ROOT/.memory-tree.conf"
```

Consequences you must design around:

- A key **absent** from the conf keeps the engine default. Good.
- A key **present and blank** in the conf **overwrites the default with the empty string**. For a
  *cutoff* key, blank = the check is OFF (`:24-28`, and `:728` guards check 12 on non-empty). For a
  *cap* key, blank hits the validation loop at `:62-79` and the gate **aborts with exit 2** —
  "HYGIENE — cannot run: size cap(s) declared in .memory-tree.conf are unusable" (`:78`). That abort
  is deliberate and documented at `:57-61`: "a gate that cannot read its own thresholds has not found
  a hygiene regression, it has failed to run."
- **One key resolves FORWARD instead**: `SPEC10_CUTOFF`, captured at `:36` before the source and
  restored at `:56` (`: "${SPEC10_CUTOFF:=$_SPEC10_SHIPPED}"`), because a blank date compares earlier
  than every date and would have demanded the ten-section canon of every grandfathered spec
  (`:29-35`).
- The cap validator refuses non-numeric and refuses a **zero byte or char cap**, arithmetically
  rather than by literal match — `case ... in 0)` accepted `"00"` and `"020"`, which awk's `+0`
  coerces to zero (`:68-76`).

### 4.3 Where a per-slot budget should live — and it is NOT check 7

**Layer answer: the generator owns per-slot budgets; `check-memory-hygiene.sh` owns per-file
budgets.** Three reasons, all from source:

1. **Check 7 measures LINES, not SECTIONS.** Its awk (`:509-544`) reads a file line by line with no
   notion of headings; adding section state to it means adding a heading parser to a check whose
   whole design note (`:498-506`) is that it is one batched awk over a *filtered set* and must not
   pin a locale. A section-aware check 7 is a second parser of the build README, in a second
   language, in a second kit-owned file — the two-answers-to-one-question class this repo names
   repeatedly (e.g. `:490-494`, where two spellings of `ex7` silently dropped the guides
   alternative).
2. **`slot_violations` already parses the structure.** Once it knows where each slot starts and ends,
   a byte/char budget per slot is `len()` on a slice already in hand. Zero new parsers.
3. **Check 6/7's population is a `git ls-files` set with a debt registry** (`in_debt` at `:118`;
   `memory/project/curation-debt.txt` currently grandfathers **five** build READMEs — lines 6-9 and
   14 of that file, including `aBoundedVerdict`, `cBriefedPilot`, `aUnmannedHelm`, `aDrainedSluice`,
   `aRuledFrontispiece`, plus `dUnstalledConvoy` at line 48). A slot budget that lands in check 6/7
   inherits that grandfathering wholesale — which is wrong, because the debt rows were granted for
   *whole-file* byte overage, not for a bloated description.

**Declaration.** Put the numbers where `BUILD_README_CAP_*` already lives conceptually — kit-owned
defaults, overridable per project. Since the generator reads `.memory-tree.conf` through
`load_conf` (`gen_build_index.py:162-173`), a `SLOT_CAP_*` family can be read there. **But note
`load_conf`'s parser is not the shell**: check it before relying on it, because the hygiene engine's
source-over-defaults semantics and a Python line-parser are two different readers of one file.

Recommended shape:

```
BUILD_README_SLOT_CAPS="description:600 improvements:800 detriments:800 rules:1200"
```

one key, one string, parsed once — the same idiom as `ARMS_FLOORS` (`.memory-tree.conf:269`, parsed by
`check-arms.py:206-214`) and `RECALL_FLOOR`. A single key means a blank value is one decision, not
four, and it keeps the conf from growing four near-identical rows.

**Validate it the way the caps are validated** (`check-memory-hygiene.sh:62-79`): non-numeric →
named refusal; zero → named refusal ("a zero budget reds every slot"); a name outside the closed slot
set → named refusal. And **measure the numbers against this corpus before declaring them** — the
charter's rule, and `.memory-tree.conf:204-217` is the model derivation to imitate.

**Character vs byte.** Check 7 counts with awk `length()` and deliberately does **not** pin the
locale (`:498-506`: "its character-versus-byte meaning is a property of the awk build and the ambient
locale; pinning it would silently re-decide the cap on any adopter whose awk counts characters
today"). Python has no such ambiguity — `len(str)` is characters, `len(bytes)` is bytes. **Pick one
and say which in the refusal message**, because a Python-side cap will not agree with check 7's on
non-ASCII, and this corpus is full of `·`, `—` and `→`.

---

## 5. What the ADOPTER-facing template needs

### 5.1 The shipped/live pattern, exactly

`tools/memory-tree/` ships three templates and each renders into `memory/`:

`tools/memory-tree/kit.toml`:

```toml
[[files]]
include = ["SPEC-TEMPLATE.template.md"]
role = "rendered"
to = "{memory_root}/TEMPLATE-SPEC.md"
placeholders = ["KIT_DIR", "TOOL_ROOT"]
```

(and the same for `HYGIENE.template.md` → `{memory_root}/HYGIENE.md` and `BUILD-METHOD.template.md`
→ `{memory_root}/guides/BUILD-METHOD.md`).

The render happens at scaffold time in `tools/memory-tree/adopt-memory-tree.sh:79-80` via
`render_doc`, and the **direction is template → live, always**
(`kit-dogfood-parity.test.sh:30-32`: "`--render` writes TEMPLATE -> LIVE. The template is the
authored source; the live copy is this repo's dogfood render of it… Edit the template, then
re-render — never hand-edit the live copy.").

**The parity gate** is `tools/memory-tree/kit-dogfood-parity.test.sh`. Its whole population is one
line, `:53`:

```sh
PAIRS="$M/HYGIENE.md:$KITREL/HYGIENE.template.md $M/TEMPLATE-SPEC.md:$KITREL/SPEC-TEMPLATE.template.md $M/guides/BUILD-METHOD.md:$KITREL/BUILD-METHOD.template.md"
```

It **renders** the template (substituting `{{KIT_DIR}}` and `{{TOOL_ROOT}}`, `:60-74`) and diffs the
result against the live copy — not a strip, for the reasons at `:21-28`. `KITREL` and `TOOLROOT` are
derived from the script's own location (`:41-49`) so a prefixed install renders correctly. Cost:
**0.580 s**.

### 5.2 Where a build-README template lives, and the full wiring bill

A build README is **per build**, so it cannot be a `role = "rendered"` file with a single `to`. It is
the `SPEC-TEMPLATE` pattern: a template document containing a **skeleton to copy**, rendered once
into the memory root. `SPEC-TEMPLATE.template.md:105` is literally `## The skeleton (copy everything
below this line)`.

So: `tools/memory-tree/BUILD-README-TEMPLATE.template.md` → `memory/TEMPLATE-BUILD-README.md`.

**Everything that must move, each verified:**

| # | File | Edit |
|---|---|---|
| 1 | `tools/memory-tree/BUILD-README-TEMPLATE.template.md` | new file |
| 2 | `tools/memory-tree/kit.toml` | a 4th `[[files]] role = "rendered"` block |
| 3 | `tools/memory-tree/kit-dogfood-parity.test.sh:53` | a 4th pair in `PAIRS` |
| 4 | `tools/memory-tree/kit.toml`, `[[gate_leg]] name = "kit/dogfood doc parity"` `guard` | add `{memory_root}/TEMPLATE-BUILD-README.md` |
| 5 | `tools/gate-legs.json:256-262` | add the same path to that leg's `guard` array |
| 6 | `tools/memory-tree/adopt-memory-tree.sh` (beside `:79-80`) | a `render_doc` call |
| 7 | `tools/memory-tree/adopt-memory-tree.sh:91-93` | the README index line for the new doc |
| 8 | `check-memory-hygiene.sh:274` | `F:TEMPLATE-BUILD-README.md` in check 3's closed root-file `case` |
| 9 | `tools/memory-tree/corpus_ids.py:236-239` | the `present` regex allowlist (`TEMPLATE-SPEC\.md` is enumerated there by name) |
| 10 | `tools/memory-tree/README.md` | the file-table row |

Items 4 and 5 are **two carriers of one fact**, and the kit.toml comment on that very leg
(`kit.toml`, under `kit/dogfood doc parity`) records why both must move together:

> TWO carriers, because govkit copies a descriptor's declared guard verbatim into a target: fixing
> gov's manifest alone would leave the half that SHIPS open, and the hole would be exported rather
> than fixed.

Item 8 is a hard red: check 3's root `case` at `:274-276` is a **closed set** —
`F:README.md|F:HYGIENE.md|F:TEMPLATE-SPEC.md|F:DECISIONS.md|F:LIVE.md` and eight directories. A new
root file reds check 3 on the commit that adds it.

**Also verified:** `tools/govkit/govkit.py:859-876` joins every `[[gate_leg]]` in a kit descriptor
against `tools/gate-legs.json` in **both directions** ("a descriptor and the manifest are two
spellings"), and `tools/govkit/subject-pins.tsv` (94 rows, generated by
`python tools/govkit/govkit.py selfcheck --write`) carries one row per leg. **A new gate leg costs
three files, not one.** Not adding a new leg — extending `--check-format` — costs zero of these.

**And the epoch.** `tools/memory-tree/check-verdict-epoch.sh:70-71` lists `gen_build_index.py` in
`DELEGATES`, so **any** behaviour-bearing edit to it requires `KIT_MEMORY_TREE_VERSION`
(`check-memory-hygiene.sh:14`, currently `2.30`) to move in a commit at or after the last such edit
— the rule is topological, not endpoint (`:16-31`). It over-counts deliberately (`:38-42`). Leg cost
0.503 s; its self-test 17.772 s.

### 5.3 The prose home, and the ungated obligation

`memory/HYGIENE.md` is "the rule set; the single mechanical enforcement is
`tools/memory-tree/check-memory-hygiene.sh`" (`:11`) and carries the numbered check catalog from
`:115`. A new check owes an entry **in `HYGIENE.template.md`**, then a `--render` — never the live
copy.

**I found no gate joining that catalog to the code.** Searched: nothing compares HYGIENE.md's check
numbers, or `tools/memory-tree/README.md:18`'s "23 checks (1-12, 21 and 22 in the shell, 13-16
delegated to `corpus_ids.py`, 17-19 to `gotchas.py`, 20 to `row_grammar.py`…)", against the branch set
`check-arms.py --report` derives. That README line is a hand-kept count **with an enumerated range
partition** and it goes stale silently. See §6.4.

---

## 6. The arms tax — exactly what N new checks cost

### 6.1 The population is SHELL only

`check-arms.py:122-138` (`discover`): every tracked `*.sh` that is **not** `*.test.sh` (`:127`),
**defines** `fail() {` matching `HELPER_RE = ^\s*fail\(\)\s*\{` (`:132-133`), and has at least one
non-comment `fail <n> "` call site matching `FAIL_RE = \bfail (\d+) "(.*)$` (`:134-136`). Its test is
the sibling `<stem>.test.sh` (`:137`).

**A Python module is invisible to this gate.** `tools/memory-tree/README.md:18` states it outright:
check 21 "owns its fail branches in the shell and delegates only the PARSE to `gen_build_index.py`,
because `check-arms.py` discovers its population from tracked shell and cannot see a Python raise";
and `:19`, for `row_grammar.py`: "Arms live in its own `--selftest`, which is a gate leg, because the
shell arm-scanner cannot reach a Python module."

**This is the single largest lever in the whole design.** Put the enforcement in
`gen_build_index.py` and the arms tax is **zero**. Put it in `check-memory-hygiene.sh` and every
branch is taxed.

### 6.2 What one shell branch costs

Per `fail` call site added to `check-memory-hygiene.sh`:

1. **A signature must exist.** `branches()` (`:142-165`) extracts the message via `message_of`
   (`:86-102`, stops at the first *unescaped* `"`), then `signature()` (`:104-119`) drops every
   `${VAR}` interpolation and takes the **longest surviving literal run**, trimming only `: " ` and
   spaces. **If that run is under 12 characters the gate raises** (`:161-164`): "has no literal run
   long enough to assert on … reword the message or the arm cannot name it".
2. **A POSITIVE assertion in `check-memory-hygiene.test.sh` containing that exact signature substring.**
   `armed_signatures()` (`:167-188`) reads the test file's lines, **excluding comments** (`:184-185`)
   and excluding NEGATIVE assertions (`NEGATIVE_RE` at `:57`: a `miss` call, or a
   `grep -qF … <<< … &&` form). The docstring at `:175-181` says a comment quoting the message does
   **not** arm — "All three are 'something mentions it', not 'something exercises it'".
3. **`ARMS_FLOORS`.** `.memory-tree.conf:269` currently reads
   `… tools/memory-tree/check-memory-hygiene.sh:20:20 …` against a **measured 23 branches / 23 armed**
   (`check-arms.py --report`, run here). Floors are one-sided upward (`:217-225` parses, `:288-296`
   compares), so N additions do not *force* a bump — but the declared convention in
   `.memory-tree.conf:258-268` is that both numbers are MEASURED, and the comment block records every
   historical movement with its reason. A unit adding checks is expected to re-measure and raise, in
   a commit that says why.
4. **Renumbering hazard.** Pin keys are `(gate, check-number, ordinal-within-that-number)`
   (`check-arms.py:243`, and `:190-204` parses the 4-field TSV). The pin file's own header records
   the live incident: "The 27 row's ORDINAL moved 2 -> 4 on 2026-08-20, and the branch it pins did
   not change. Two `fail 27` branches were inserted ABOVE it … ordinals are assigned by line order
   within a check — so every pinned row below an insertion point goes stale at once, with a message
   that reads like a rewording" (`memory/project/unarmed-branches.txt`, lines 17-24).
   **For check-memory-hygiene.sh specifically this hazard is currently NIL** — the pin holds only
   three rows, all `tools/unattended/unattended.sh`. Inserting a new hygiene check number costs
   nothing in the pin *today*. It becomes live the moment any hygiene branch is ever pinned.
5. **The self-test leg cost.** `memory-hygiene self-test` is **181.9 s** and its fixtures build
   scratch repos. Adding red+green fixtures for a new check is the real wall-clock cost, not the arm
   line.

### 6.3 What one Python refusal costs

- `check-arms.py`: **0**.
- `do_selftest` arms (`gen_build_index.py:1205-1219` is the harness; 71 `arm()` calls exist today):
  budget **2 per refusal branch** — one red fixture, one green — following the existing slot arms at
  `:1485-1503`.
- The leg they run under is `build-index selftest`, `chunk: "selftests"`, `subject: "kit"`,
  `guard: ["tools/lib/", "tools/memory-tree/"]` (`tools/gate-legs.json:284-296`). Per this repo's
  standing rule, **kit self-tests are HELD by default** and need `GATE_SELFTESTS=1`. So a Python arm
  does not run on an ordinary bar — but neither does `memory-hygiene self-test`, which is also
  `chunk: selftests / subject: kit`. **The asymmetry is not coverage; it is the mechanical
  requirement.** `check-arms.py --check` (0.374 s, `chunk: declarations`, `subject: repo`) runs on
  every bar and *forces* a shell arm to exist. Nothing forces a Python arm to exist.
- `check-testsuite-counts.sh:34` derives its population from `*.test.sh` strings in
  `tools/gate-legs.json` — a Python `--selftest` is outside it, so no count-shape obligation.

### 6.4 The leg-name-states-a-count trap, resolved

The trap is real and is currently **half-tripped**:

- `git log -S'"name": "memory hygiene'` shows the leg was once
  `{ "name": "memory hygiene (12 checks)", … }`. It is now `"memory hygiene"`
  (`tools/gate-legs.json:894`) — renamed by `47f4ba2e reconcile: key the leg names to what the
  descriptors actually reference`.
- **`AGENTS.md:208` and `coding-governance-agents.template.md:138` still claim** the hygiene gate's
  "check count is stated by the kit README **and the gate-leg name** and is deliberately not restated
  here." The leg name states no count. That half of the sentence is already false, in both the
  dogfood charter and the **shipped template**.
- The count that survives is `tools/memory-tree/README.md:18` — "23 checks (1-12, 21 and 22 in the
  shell, 13-16 delegated to `corpus_ids.py`, 17-19 to `gotchas.py`, 20 to `row_grammar.py`…)". It is a
  number **and a range partition** beside the thing it counts, and nothing gates it.

**So: adding N shell checks silently falsifies one prose line and requires a manual edit to a second
that is already wrong.** Adding zero shell checks — putting everything in `gen_build_index.py` —
avoids both. If the design must add a shell check anyway, fix `AGENTS.md:208` and the template line
in the same commit, or the unit lands a documented false claim.

### 6.5 N, per candidate mechanism

Assuming the enforcement lives in `gen_build_index.py --check-format` (recommended):

| Mechanism | new `fail` branches in shell | `check-arms` rows | ARMS_FLOORS edit | new `arm()` in `do_selftest` | new gate legs |
|---|---|---|---|---|---|
| A: heading canon + empty-body + per-slot budget | **0** | **0** | **none required** | ~10–12 | 0 |
| B: marker pairs per slot | 0 | 0 | none | ~12–16 | 0 |
| C: front-matter description + width cap | 0 | 0 | none | ~4 | 0 |
| **Same, if placed in `check-memory-hygiene.sh` instead** | 4–6 | 4–6 | 20:20 → measured | 8–12 fixtures | 0 |

The shell variant additionally costs: a numbered entry in `HYGIENE.template.md` + `--render`, a
`tools/memory-tree/README.md:18` count edit, an `AGENTS.md:208` correction, and 4–6 red/green fixtures
in a 181.9 s self-test.

---

## 7. Recommendation — one mechanism per slot

**Package: extend `--check-format`. Zero new gate legs, zero arms tax, one kit-version bump.**

All four slots are enforced by **one extended `slot_violations`** in
`tools/memory-tree/gen_build_index.py`, graded by the existing
`build README slot contract` leg (`tools/gate-legs.json:298-307`, 0.347 s, no guard, runs on every
bar). No new leg means no `kit.toml` `[[gate_leg]]`, no `tools/gate-legs.json` row, no
`tools/govkit/subject-pins.tsv` row.

| Slot | Mechanism | What the check asserts |
|---|---|---|
| **3 — immutable description** | **Exact heading canon (candidate A)**, first position, plus a **byte budget**, plus a **documented** immutability rule with no gate | the heading `## <canon text>` is present, is the FIRST `##` in the authored block, its body is non-empty, and its body is ≤ its declared budget |
| **4 — expected improvements** | Heading canon, second position + **all non-blank body lines are list items** + byte budget | present, in order, non-empty, every non-blank line matches `^\s*[-*]\s`, ≤ budget |
| **5 — detriments if not built** | Identical to slot 4, third position | same |
| **6 — build-level rules** | Heading canon, fourth position, **MAY be empty**, byte budget | present in the sequence; body may be empty; ≤ budget |

Supporting decisions, each with its reason:

1. **Keep `slot_violations`' two existing triggers unchanged.** They are the position-bound contract
   the owner chose on 2026-08-16 and they are what keeps generated regions clean. The new walk is
   *additive*, inside the region they already bound.
2. **Add a fifth trigger: no non-blank prose between the `#` title and the first canon heading, and
   none between the last canon section and the plan/generated boundary.** Without it, "irrelevant
   prose" simply moves above the first heading and the closed set buys nothing. This is the trigger
   that actually answers "guarded against irrelevant prose".
3. **Port `unfenced_lines` (`gen_build_index.py:175-211`) into the walk.** `slot_violations` is
   fence-blind today and at least one build README quotes README boilerplate inside a fence
   (`strip_records_sentence:794-798`). Without this, the gate reds on landing over a false heading.
4. **Grandfather by front-matter `opened:`, not by filename.** A build README has no date in its
   name. `opened:` is required (`:112`) and date-validated (`:246-247`). Declare
   `BUILD_README_CANON_CUTOFF` in `.memory-tree.conf`; **blank must resolve FORWARD to a shipped
   value or turn the check off explicitly** — decide which and say so at the declaration, because
   `SPEC10_CUTOFF` (`check-memory-hygiene.sh:29-36, 56`) exists solely because a blank date compares
   earlier than every date and silently demanded the canon of the whole corpus.
5. **`BUILD_README_SLOT_CAPS` as one space-separated `name:number` string**, in the `ARMS_FLOORS`
   idiom, validated like the caps at `:62-79` (non-numeric → named refusal, zero → named refusal,
   unknown slot name → named refusal). Measure the four numbers against this corpus before declaring
   them.
6. **Bump `KIT_MEMORY_TREE_VERSION`** (`check-memory-hygiene.sh:14`, currently `2.30`) in a commit at
   or after the last engine edit — `check-verdict-epoch.sh:71` lists `gen_build_index.py` as a
   delegate and the rule is topological.
7. **Stage the break and observe RED before landing** — charter §7, "A new gate is not landed until
   its failing case has been observed."
8. **Run the candidate predicate over the real tree first and print hits AND near-misses.** With 136
   distinct headings across 42 files, the near-miss list *is* the migration plan.

### 7.1 What this package explicitly does NOT check

To be copied verbatim into the function header, per §7's rule that a gate's own header states its
blind spots:

- **It does not check that slot 3 was authored once.** "Never re-authored" is a claim about history;
  this reads the current bytes. The rule is documented in `memory/HYGIENE.md` and the rendered
  template as a manual check, on the same footing as `memory/DECISIONS.md`'s append-only rule, which
  `APPEND_ONLY_ERE` (`check-memory-hygiene.sh:104`) names for other checks' *exemptions* and which no
  gate enforces either.
- **It does not check that any slot's prose is true, current, or about this build.** A conforming
  heading set over four paragraphs of nonsense passes. It grades SHAPE, SEQUENCE and SIZE.
- **It does not check that slot 4 lists improvements or that slot 5 lists detriments.** It checks that
  the lines are list items. A bullet reading "TBD" passes.
- **It does not check the four generated regions are in canonical order.** That is a property of
  `insert_region`'s creation position (`:1009-1029`) and has never been asserted; this package does
  not change that.
- **It does not reach `###` sub-heads.** A slot may be internally structured; only `^## ` is graded,
  as in check 12 (`:990`).
- **It says nothing about a README with no generated region at all.** `slot_violations` returns `[]`
  when no pair is present (`:990-991`); that refusal lives on the render path in `apply_region`
  (`:911-914`) and this package does not move it.
- **Its byte counting is Python `len()` and will not agree with check 7's awk `length()` on
  non-ASCII.** Check 7 deliberately does not pin its locale (`:498-506`); this one is character-exact
  by construction. Two budgets, two counters, and the refusal message must say which.

### 7.2 Two things a spec must decide that I could not

- **Does `## Units` survive?** `memory/guides/BUILD-METHOD.md:33` reads the authored Units table as
  M2's roster source, and 21 of 61 READMEs carry one. A closed 4-slot canon either admits a fifth
  `## Units` slot, or M2's detect step changes, or the 11 `roster:units` carriers break. This is an
  owner fork, not an implementation detail.
- **`readme_mechanism_drift` re-baselines.** `tools/drift-audit/drift_report.py:923-1030` scans the
  **authored region only** ("Everything from the first `<!-- gen:` marker down is rendered … and
  cannot drift", `:965-966`) and its pin is `19` at `tools/drift-audit/drift_signals.py:187`. Shrinking
  340,532 authored bytes to four bounded slots moves that measurement. Re-measure the pin in the same
  build or the drift signal reports a change nobody made.
