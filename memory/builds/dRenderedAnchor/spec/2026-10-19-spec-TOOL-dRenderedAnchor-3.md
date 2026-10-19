# TOOL-dRenderedAnchor-3 — the closing review's round-2 findings on unit 2 closed as one batch

**Status:** INPROGRESS · rev-2 · 2026-10-19 · node d · Tier-2 · base 8a0e0b59 · streams tooling

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-19-prompt-TOOL-dRenderedAnchor-3-1-revision.md](../prompts/2026-10-19-prompt-TOOL-dRenderedAnchor-3-1-revision.md) | research | — |
| [2026-10-19-prompt-TOOL-dRenderedAnchor-3-2-spec-writer.md](../prompts/2026-10-19-prompt-TOOL-dRenderedAnchor-3-2-spec-writer.md) | journal | — |
| [2026-10-19-prompt-TOOL-dRenderedAnchor-3-brief.md](../prompts/2026-10-19-prompt-TOOL-dRenderedAnchor-3-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

Round 2 of the closing diff review read unit 2 and confirmed 2 mediums and 7 lows. This unit closes
all nine in one batch. The `/build` Skill's citation pass resolves a harness the way the role index
does and can no longer name an adopter's repo-root file as the merge bar. It substitutes each
citation whole. Every new arm reads a population it does not derive from what it guards, and
each guard term gets a row that only that term rejects. The help text and docstrings state the
predicates that ship.

## 2. Scope (IN)

- **S1** — M1, the harness half. `tools/roles/roles_lib.py` gains `extract_workflow_harnesses`,
  which returns the `harness` value of each `[[workflow]]` entry whose `driver` is `workflow`, in
  table order. `resolve_cited_paths` takes the loaded table as a fourth argument and the roles kit
  directory in place of the tool root. A citation whose `<home>/<file>` is a pair `HARNESS_RE`
  parses out of one of those harnesses resolves through `resolve_kit_dir` with `here` at the kit
  directory's parent, which is the call `resolve_harness_path` makes. Observed by AC1 and AC13.
- **S2** — M1, every other citation. Its answer is F1's. Under F1's recommended pick C4 it resolves
  through `resolve_kit_dir` with `here` at the roles kit directory, which is the call
  `derive_kit_paths` makes. Under C1 it is not listed, so the plain prefix answers it. Under either
  pick no citation that is not a harness reaches a probe above the tool root. Observed by AC2, and
  by AC3 under C4 only.
- **S3** — L3. The citation pass in `render_skill` of `tools/roles/adopt-roles.sh` prints the
  template's text with each held citation substituted through `TOOL_ROOT_CITE_RE.sub`, one whole
  match at a time. `render_skill` takes `out` from that call instead of from `cat "$TEMPLATE"`, and
  the `{{KIT_DIR}}`, `{{TOOL_ROOT}}` and `{{MEMORY_ROOT}}` substitutions follow as before. Observed
  by AC5 and AC13.
- **S4** — `derive_harness_paths` in `tools/roles/render_agents.py` iterates
  `extract_workflow_harnesses`, so the role index and the citation pass read one list. Observed by
  AC13.
- **S5** — M2 and L5. Arm 14 of `tools/roles/adopt-roles.test.sh` takes its population from the kit's
  `workflows.toml`, read with `tomllib` by the arm itself. Each `workflow`-driver harness whose
  literal `{{TOOL_ROOT}}<home>/<file>` the template holds is planted and asserted. The asserted count
  must equal that cited count and be at least 2. Each check matches the backtick-delimited path, not
  a substring. Observed by AC4 and AC6.
- **S6** — L3's row, inside arm 14. The fixture's template gains a backticked citation of the first
  planted harness with `x` appended to its file name. The Skill must name that citation under the
  plain prefix. Observed by AC5.
- **S7** — M1's arm, a new arm 15. Each template citation that is not a table harness gets a decoy
  file at the fixture's repository root, and the Skill must still carry its plain-prefix span.
  Under C4 the arm also gets one receipt row placing such a citation under another directory, and
  the Skill must name that directory. Observed by AC2, and by AC3 under C4 only.
- **S8** — L6's arm, a new arm 16. A root-install fixture, with the kit at `roles/`, has a sibling
  directory beside the repository holding each cited harness. `resolve_cited_paths` lists nothing
  there, and `--scaffold` exits 0 with the plain citation. `build_fixture` takes an optional kit
  path and fixture directory, so this arm does not copy it. Observed by AC7.
- **S9** — The suite's `FLOOR_ASSERTIONS` rises by one per floored `check_arm` the unit adds: to 48
  under C1, or 49 under C4. Its header lists arms 15 and 16, and its WHAT THIS DOES NOT CHECK block
  says what they leave out. Observed by AC15.
- **S10** — L4. Section 2e of `tools/lib/resolve-python.test.sh` gains row 7, a `rendered` row from
  home `h` whose `path` is an absolute path to an existing file outside the fixture tree. The
  section's python program writes that row, and it expects `LookupError`. Its row-count check reads
  7, and its comment names the term each row holds. Observed by AC8.
- **S11** — L2. `tools/check-wiring.test.sh` gains one assertion beside its absent-harness note
  check. It matches the note's whole remedy tail on the printed line. Observed by AC9.
- **S12** — L1, L7 and the M1 wording. `help/roles.md` names all three tools that print the
  missing-harness note, the catalogue checker `check_roles.py` among them. That page, the docstring
  of `tools/roles/render_agents.py`, `tools/roles/README.md` and `memory/map/features/roles.md`
  each say that a file beside neither mark is not counted as its kit's and reads as the note.
  The help page, the README, the adopter's header comment and the `resolve_cited_paths` docstring
  each say that only a harness of the workflow table resolves through the role index's call.
  Observed by AC10, AC11 and AC12.
- **S13** — The left-shift M8 owes the two findings no arm gates. L1 and L7 each join
  `memory/gotchas/two-answers-to-one-question.md` as one entry under "Where it bit".
  `memory/gotchas/INDEX.md` is regenerated by `gotchas.py --write` where that changes it.
  Observed by AC14.

## 3. Non-goals (OUT)

- `resolve_harness_path`, `resolve_kit_dir` and their probe order. The role index keeps probing
  `<tool root>/../<home>/` for a harness. At a prefixed install a harness found only at the
  repository root is therefore listed there. At a root install with a sibling holding it, it is
  listed as `../<home>/<file>`, outside the repository. Both predate this build: the probe and the
  `relpath` are at `a60b0c7d`. Arm 16 builds the second layout, and its WHAT THIS DOES NOT CHECK
  line names the index's answer there. This is the follow-up, and not this batch's finding.
- The optional extra in L1's fix, a `check_roles.py` note pointing at `adopt-roles.sh --check`. It
  changes a carried check's output, and the review records it as optional.
- A shell twin of the misplaced scan, and the REVIEW-PROTOCOL and unattended Skill templates' plain
  citations. Unit 2's spec §3 rules both out, and the brief carries that forward.
- Units 1 and 2's specs. Both are CLOSED and frozen.
- Kit version bumps, which the lander's `mint` writes (`tools/push-main.sh:26-29`). Merge and push
  wait for the owner's explicit ask.

Unit 2's code, at `54344d9a7`, is this unit's base, not a sibling's pending work, so no edge
names it.

### Edges

none

## 4. Design

### The base

`base 8a0e0b59` is this branch's tip, which carries units 1 and 2 and the round-2 review record.
The code there is the review's reviewed tip `c66a3663d` plus record commits. The default branch is
still at `a60b0c7d`, which predates both units. Every claim below about current code was read at
`8a0e0b59`.

### What the pass resolves (S1, S2) — M1

`render_skill` passes `kit.parent` to `resolve_cited_paths` (`tools/roles/adopt-roles.sh:176`), so
`resolve_kit_dir`'s second probe, `here.parent / home` (`tools/roles/roles_lib.py:127`), lands at
the repository root at a prefixed install. Every citation took that path at `8a0e0b59`, including
`{{TOOL_ROOT}}run-gates/run-gates.sh` (`tools/roles/SKILL.template.md:84`) and
`{{TOOL_ROOT}}unattended/unattended.sh` (`:12`). `derive_kit_paths` passes the kit directory
instead (`tools/lib/render-doc.sh:168`), so its probes stop at `<tool root>/<home>/`.

```python
def extract_workflow_harnesses(workflows):
    """The `harness` value of each `[[workflow]]` entry whose `driver` is `workflow`, in table order."""
    return [w.get("harness") for w in workflows if w.get("driver") == "workflow"]


def resolve_cited_paths(text, kit_dir, target_root, workflows):
    """`[(cite, rel)]` in first-seen order, one per distinct citation in text that this install
    holds, rel repo-relative. A citation of a `workflow`-driver harness of workflows resolves as
    `resolve_harness_path` does, with `here` at the tool root, so the Skill names a harness where
    the role index lists it. [S2, per F1.] A citation nothing holds, or held outside target_root,
    is not listed, and the caller's plain prefix substitution answers it."""
```

The harness pairs are `{m.groups()}` over `HARNESS_RE.match` of each string that
`extract_workflow_harnesses` returns. A harness `HARNESS_RE` refuses contributes no pair. The
catalogue checker reds that table as R9 (`tools/roles/check_roles.py:289-292`), and
`resolve_harness_path` raises on it (`tools/roles/roles_lib.py:592-594`).

S2's line, under F1's two picks:

| Pick | A citation that is no table harness |
|---|---|
| C4, recommended | `resolve_kit_dir(home, file, kit_dir)`, the `derive_kit_paths` call; listed when it holds |
| C1 | not listed; the plain prefix answers it |

What each citation's answer agrees with, at a prefixed install:

| Citation, and the layout | `8a0e0b59` | C1 | C4 |
|---|---|---|---|
| a harness held at `<tool root>/<home>/` or by a receipt row | the role index | the role index | the role index |
| a harness found only at `<repo>/<home>/` | the role index | the role index | the role index |
| run-gates, absent from the tool root, an adopter file at `<repo>/run-gates/` | that adopter file (M1) | the plain prefix | the plain prefix |
| run-gates under a per-entry install override recorded in the receipt | the receipt row | the plain prefix | the receipt row |

The second row is where the Skill and `derive_kit_paths` keep two answers. It is the role index's
own answer, and §3 names it. The fourth row is F1. The `unattended` and `run-gates` kits declare
`id` equal to `home` (`tools/unattended/kit.toml`, `tools/run-gates/kit.toml`), so in a default
install the plain prefix and `derive_kit_paths` give one answer for both. They part only under an
override.

`derive_harness_paths` (`tools/roles/render_agents.py:158-169`) iterates
`lib.extract_workflow_harnesses(workflows)` and passes each to `resolve_harness_path`. The set and
its order are unchanged, so `.claude/roles.json` is byte-identical. `check_roles.py`'s loop is
left as it is: it grades each entry and reports a defect per key, so it is not a reader of the list.

### Each citation substituted whole (S3) — L3

At `8a0e0b59` the pass prints `cite<TAB>rel` lines and bash applies each with
`${out//"$kp"/"$kv"}` (`tools/roles/adopt-roles.sh:185-187`). That is an unanchored substring, so a
held `{{TOOL_ROOT}}h/t.js` rewrites the front of `{{TOOL_ROOT}}h/t.json`.

The python call now prints the template's text:

```python
held = dict(roles_lib.resolve_cited_paths(text, kit, root, roles_lib.load_workflows(kit)))
sys.stdout.buffer.write(roles_lib.TOOL_ROOT_CITE_RE.sub(
    lambda m: held.get(m.group(0), m.group(0)), text).encode("utf-8"))
```

`render_skill` captures it with the script's `X` sentinel, `out=$("$PY" -B -c '…' … && printf X)`,
and keeps its failure line and `return 2`. The bash loop over `cites` is deleted. The CR strip and
the three token substitutions run on that text as they do now.

The whole match is the boundary. `TOOL_ROOT_CITE_RE`'s `[\w.-]+` is greedy
(`tools/roles/roles_lib.py:75`), so the character after a match is never one of `[\w.-]`. That is
the lookahead the skeptic's fix spells. `re.sub` visits each match once and without overlap. So
`{{TOOL_ROOT}}h/t.json` is its own match and keys `held` by its own text.

`sys.stdout.buffer` keeps a Windows python from writing CRLF. `read_text` already folds the
template's CRLF to LF, so the bytes reaching the substitutions match the `cat` they take the place
of.

### Arm 14's population and oracle (S5, S6) — M2, L5

Arm 14 at `8a0e0b59` iterates `roles_lib.TOOL_ROOT_CITE_RE.finditer` over the template
(`tools/roles/adopt-roles.test.sh:524`). It skips any pair the table does not list, and its floor
`[ "$_i" -ge 2 ]` (`:548`) is met by one pair. Its positive check is `grep -qF -- "<path>"`
(`:543`).

The rewritten arm's inline python reads `<kit>/workflows.toml` with `tomllib` and keeps entries
whose `driver` is `workflow`. It splits each `harness` after a literal `{prefix}/` into home and
file. It keeps a pair when the template text contains `{{TOOL_ROOT}}<home>/<file>` as a substring.
It imports nothing from `roles_lib`. Planting and receipt rows are as now. The bash half asserts
these things:

- the pair count equals the number of kept pairs, and that number is at least 2;
- the Skill holds `` `<tool root>renamed/<file>` `` for each pair, backticks included;
- the Skill holds no `` `<tool root><home>/<file>` `` for any pair.

The floor 2 is PINNED, measured at `8a0e0b59`. The template cites two `workflow`-driver harnesses,
at `tools/roles/SKILL.template.md:45` and `:76`. The table's third, `unattended-unit.js`, is not
cited there (`tools/roles/workflows.toml:55`).

L3's row is in the same block. Before the scaffold, the arm appends one line to the fixture's
template, holding the first kept pair's citation with `x` appended to the file name, in backticks.
After it, the Skill must hold `` `<tool root><home>/<file>x` `` and no `` `<tool root>renamed/<file>x` ``.
That is one more `check_arm`, labelled `arm 14 ...and`, as the suite labels its sub-checks.

### The non-harness decoys (S7) — M1's arm

Arm 15 builds a fixture with `build_fixture`. The arm's own scan finds every backticked span of the
template that holds `{{TOOL_ROOT}}`, using the arm's own pattern rather than `TOOL_ROOT_CITE_RE`.
For each span, the text after the token up to the first space or backtick splits at its first `/`
into home and file. Spans whose pair the arm's own `tomllib` read lists as a `workflow`-driver
harness are skipped. For each remaining one the arm writes `$FX/<home>/<file>`, and its expected
span is the span with `{{TOOL_ROOT}}` replaced by the fixture's tool root. After `--scaffold`, the
Skill must hold each expected span verbatim, and `--check` must exit 0. The count of such spans must
be at least 2. That floor is PINNED at `8a0e0b59`, from `tools/roles/SKILL.template.md:12` and `:84`.

Under C4 the arm adds one sub-check. It writes a receipt row whose `source` ends in the first
span's `<home>/<file>` and whose `path` is `ci/<file>`, and writes that file. After `--scaffold`,
the Skill must hold that span with its citation rendered as `ci/<file>`.

### The root install (S8) — L6

At a root install `TOOL_ROOT` is empty (`tools/roles/adopt-roles.sh:69-70`), so the tool root is
the repository. A harness citation probes `<repo>/../<home>/<file>`. Where a sibling holds it,
`relative_to` raises `ValueError`, and `resolve_cited_paths` catches that
(`tools/roles/roles_lib.py:618`).

`build_fixture` gains two optional positional arguments, the kit path and the fixture directory,
defaulting to `$KREL` and `$TMP_ROOT/fx$n`. `run_adopter` reads the kit path the last
`build_fixture` used. Arm 16 calls it with `roles` and `$TMP_ROOT/a16/repo`, then writes
`$TMP_ROOT/a16/<home>/<file>` for each pair, derived the way arm 14 derives them. It asserts two
things:

- a python call of `roles_lib.resolve_cited_paths` over the template, with the kit at
  `repo/roles`, the target at `repo` and the kit's table, prints no pair;
- `--scaffold` exits 0, and the Skill holds `` `<home>/<file>` `` for each pair.

A copy of `roles_lib.py` whose `except` names `LookupError` alone raises in both. The second shows
as the adopter's `the citation pass … failed` line with exit 2.

### Section 2e's seventh row (S10) — L4

Row 5's `../out/w.js` passes `root in hit.parents`, because `absolute()` keeps `..`. It is refused
only by `".." not in hit.parts` (`tools/lib/resolve_kit_dir.py:42-43`). Row 7 is the one only the
other term refuses: the bash half writes `$TMP/out/y.js` beside `$TMP/out/w.js`. The python program
appends `{"role": "rendered", "source": "p/h/y.template.js", "path": <abs>}` to the receipt before
its queries, where `<abs>` is `(root.parent / "out" / "y.js").absolute().as_posix()`.

The path is written by python on purpose. A shell-written `/tmp/…` path inside a JSON file is not
converted by MSYS, and Windows python reads it as drive-relative. So the row would name no file and
pass on the existence test, which is `fixture-passes-by-finding-nothing`.

It is written in posix form because the join splits `path` on `/` before either escape term is read
(`tools/lib/resolve_kit_dir.py:39`). A Windows `str()` of the path holds backslashes, so its last
`/`-field is not `y.js`, and the join skips the row. The canonical and a copy with
`root in hit.parents` cut then both print `LookupError`, and the row can never be seen red. A
drive-letter posix path still reads as absolute in `root / <abs>` on Windows (`:42`), and on POSIX
`as_posix()` changes nothing. Probed on 2026-10-19 on this Windows host, with 2e's fixture shape and
`here` at `p`: under `str()` both the canonical and the cut copy printed `LookupError`; under
`as_posix()` the canonical printed `LookupError` and the cut copy returned the `out` directory.

The query list gains `y.js`, the expected list a seventh `LookupError`, and the count check reads 7.
The comment says that row 5 holds the `..` term, row 7 the outside-the-tree term, and row 6 the
existence test. With the `root in hit.parents` term cut, row 7 returns a directory outside the tree,
and its `relative_to` raises out of the program. Either way the output differs from the table.

### The remedy tail (S11) — L2

Beside the check at `tools/check-wiring.test.sh:2172-2173`, one `ck` asserts that the printed note
line for `nowhere/absent-harness.js` carries
`"${KP}$RL/adopt-roles.sh --check says whether its kit holds it elsewhere"`. The neighbouring
UNWIRED checks already use this shape for `--scaffold` (`:2149-2150`). The line it reads is
`tools/check-wiring.sh:1746`.

### The wording (S12) — L1, L7, M1

| Place | Today, at `8a0e0b59` | After |
|---|---|---|
| `help/roles.md:135-137` | note printers: `render_agents.py` and check-wiring's report | the catalogue checker `check_roles.py`, `render_agents.py` and check-wiring's report, as `tools/roles/README.md:285` lists them |
| `help/roles.md:141-142` | "neither mark is your own" | not counted as its kit's, and reads as the note |
| `tools/roles/render_agents.py:39-40` | "an adopter's namesake and not the kit's" | the same |
| `tools/roles/README.md:230-231` | "neither mark is the adopter's own" | the same |
| `memory/map/features/roles.md:106-107` | "neither mark is the adopter's own" | the same |
| `help/roles.md:130-132` | "Each tool-root citation of its template is resolved" | each harness of the workflow table resolves as the role index does; S2's answer for the rest |
| `tools/roles/README.md:313-319` | "every `{{TOOL_ROOT}}<home>/<file>` citation the kit resolver holds" | the same as the help page |
| `tools/roles/adopt-roles.sh:30-37` and `:166-168` | every citation the resolver holds | the same |
| `memory/map/features/roles.md:147-149` | "the `/build` Skill's citations" | "the `/build` Skill's harness citations" |

The phrase "not counted as its kit's" is kept on one line in each place, so AC11 can count it.
The help page adds one sentence: a harness its kit ships with no template, `unattended-unit.js`,
is marked by `kit.toml` alone.

### Left-shift (S13)

Each entry is two to four sentences under "Where it bit". It gives the instance, its finding id in
the round-2 record, and the fact that no machine gate compares a help page's list with the README's.
M1, M2, L2 to L6 are left-shifted by arms 14 to 16, section 2e's row 7 and the check-wiring
assertion.

### Inventory

| Minted | Where | Naming cell |
|---|---|---|
| `extract_workflow_harnesses` | `tools/roles/roles_lib.py` | `py.function`, which `lexicon.py --suggest` answered OK on 2026-10-19 |
| adopter arms 15 and 16 | `tools/roles/adopt-roles.test.sh` | — |
| section 2e row 7 | `tools/lib/resolve-python.test.sh` | — |
| one `ck` | `tools/check-wiring.test.sh` | — |

`resolve_cited_paths` keeps its name and gains an argument; its one caller is
`tools/roles/adopt-roles.sh:176`. No receipt field, conf key, leg or file is minted.

### Rollout

Tier-2: a shipped kit edit. No receipt, conf or deploy shape moves. `govkit update` carries the
bytes and re-runs `--scaffold` (`tools/roles/kit.toml:72-73`), so an adopter whose Skill named a
repo-root merge bar corrects itself. In gov the rendered Skill and index are byte-identical. Kit
versions are minted at landing.

### Files touched (estimate)

- `tools/roles/roles_lib.py`, `tools/roles/adopt-roles.sh`, `tools/roles/render_agents.py`,
  `tools/roles/adopt-roles.test.sh`, `tools/roles/README.md`
- `tools/lib/resolve-python.test.sh`
- `tools/check-wiring.test.sh`
- `help/roles.md`
- `memory/map/features/roles.md`
- `memory/gotchas/two-answers-to-one-question.md`, `memory/gotchas/INDEX.md`
- `memory/builds/dRenderedAnchor/build/`, for this unit's acceptance ledger

### Alternatives rejected

| Candidate | The test that rejected it | Verdict |
|---|---|---|
| C1 — harness pairs only, every other citation plain (the skeptic's fix) | the fourth row of the agreement table: an override the receipt records renders plain, where `8a0e0b59` and `derive_kit_paths` resolve it | F1's alternative, not rejected |
| C2 — every citation with `here` at the kit directory | the second row: a harness found only at `<repo>/<home>/` is listed there by the role index, which agent-cap admits by, and the Skill would name the plain path | Rejected |
| C3 — L3 by emitting every citation and applying longest first | python would need `TOOL_ROOT`, a second derivation of the adopter's `.git` walk; the whole-match `re.sub` needs neither | Rejected |
| C4 — harness pairs at the tool root, every other citation at the kit directory | survives every veto, and leaves no row of the agreement table open but the role index's own | F1's recommendation |
| C5 — arm 14 reads its population through `extract_workflow_harnesses` | that is the code the pass now reads, so a break in it moves the arm's population with it, which is M2 again | Rejected |
| C6 — L4 by narrowing 2e's comment and leaving the term ungated | the review offers it as a fallback; a row costs one fixture line | Not taken |
| C7 — L6 as a section beside 2f in `tools/lib/resolve-python.test.sh` | `resolve_cited_paths` is the roles kit's, not the lib's canonical, and the adopter's exit 2 is the consequence the finding names | Rejected |

## 5. Production-readiness checklist

- security — No new write path or egress. M1 narrows a read: a citation that is no harness no
  longer resolves above the tool root. The pass still returns only paths the resolver admits.
- perf / scale — The python call that already runs reads `workflows.toml` once more. No new
  process.
- error / empty / loading states — A refused `HARNESS_RE` value contributes no pair. A failed call
  still exits 2 naming the citation pass. A template with no citation renders as before.
- observability — Unchanged lines. The check-wiring note's remedy is now asserted.
- risks — F1's pick decides the override row. Arm 16 runs a root-install fixture, which this suite
  has not built before; its sibling directory sits under the suite's own `TMP_ROOT`.
- testing — AC1, AC4, AC7 and AC8 are in-process probes. AC2, AC3, AC5 and AC7 run the adopter
  over scratch fixtures. The arms are observed RED then GREEN by the main loop at the close (§7).
- migration — N/A — no receipt, conf or deploy field moves.
- user docs — `help/roles.md` names the three note printers, states the scan's outcome as what it
  counts, and states which citations resolve (S12).

## 6. Acceptance criteria

`<p1>` is this unit's build pass commit. Scratch fixtures go under the run's scratchpad, and a git
fixture under `%TEMP%/<short-name>`. Commands run from the worktree root.

- **AC1** — When a python program imports `tools/roles/roles_lib.py` and calls
  `resolve_cited_paths` over `tools/roles/SKILL.template.md`'s text with the kit's `load_workflows`
  table, in a fixture holding `.git`, `tools/roles/`, both cited harnesses under `tools/workflows/`,
  and `run-gates/run-gates.sh` and `unattended/unattended.sh` at its root, it returns exactly the two
  harness citations, each under `tools/workflows/`.
  Red when: every citation resolves with `here` at the tool root, as at `8a0e0b59`, and the
  run-gates citation returns `run-gates/run-gates.sh`, as the round-2 review reproduced.
- **AC2** — When a bash probe builds a fixture as `build_fixture` does, writes the same two root
  files and runs `adopt-roles.sh --scaffold`, the fixture's Skill holds
  `` `bash tools/run-gates/run-gates.sh` `` and `` `bash tools/unattended/unattended.sh` ``.
  Red when: the adopter and library are as at `8a0e0b59`, and the Skill holds
  `` `bash run-gates/run-gates.sh` ``.
- **AC3** — Owed only if F1 resolves to C4. When that fixture also carries a receipt row whose
  `source` ends in `run-gates/run-gates.sh` and whose `path` is `ci/run-gates.sh`, with the file
  written, the Skill holds `` `bash ci/run-gates.sh` ``, and `derive_kit_paths` over the same tree
  prints that path for the same citation.
  Red when: the non-harness citation takes the plain prefix, and the Skill holds
  `` `bash tools/run-gates/run-gates.sh` ``.
- **AC4** — When `grep -c 'TOOL_ROOT_CITE_RE\|import roles_lib\|roles_lib\.'` runs over arm 14's
  block of `tools/roles/adopt-roles.test.sh`, it prints 0. When that block's population program
  runs over the kit's own `workflows.toml` and `SKILL.template.md`, it prints the
  `unattended-build.js` and `tier2-review.js` pairs.
  Red when: the population is read through `TOOL_ROOT_CITE_RE`, as at `8a0e0b59`, where the first
  count reads 1 or more.
  figure: 2 is PINNED, measured at `8a0e0b59` from `tools/roles/SKILL.template.md:45` and `:76`.
- **AC5** — When a bash probe builds arm 14's fixture, appends a line holding
  `` `{{TOOL_ROOT}}workflows/tier2-review.jsx` `` to its template, and runs `--scaffold`, the Skill
  holds `` `tools/workflows/tier2-review.jsx` `` and `` `tools/renamed/tier2-review.js` ``.
  Red when: the held lines are applied with `${out//"$kp"/"$kv"}`, as at `8a0e0b59`, and the Skill
  holds `` `tools/renamed/tier2-review.jsx` ``.
- **AC6** — When arm 14's positive-check expression runs against a scratch file whose line reads
  `` `C:/x/tools/renamed/tier2-review.js` ``, it fails. Against a file reading
  `` `tools/renamed/tier2-review.js` `` it passes.
  Red when: the check is the bare `grep -qF -- "<path>"` of `8a0e0b59`, which passes the first file.
- **AC7** — When a python program builds S8's root-install layout and calls `resolve_cited_paths`
  with the kit at `repo/roles`, it returns `[]`. When `bash roles/adopt-roles.sh --scaffold` runs in
  `repo`, it exits 0 and the Skill holds `` `workflows/tier2-review.js` ``.
  Red when: a copy of `roles_lib.py` catches `LookupError` alone, the call raises `ValueError`, and
  the adopter exits 2 naming the citation pass.
- **AC8** — When a python program loads `tools/lib/resolve_kit_dir.py`, builds 2e's fixture with
  row 7 written as §4 says, and queries `y.js` with `here` at `p`, it prints `LookupError`.
  Red when: `root in hit.parents` is cut from a copy of the canonical, and the query returns the
  `out` directory.
- **AC9** — When `grep -cF 'adopt-roles.sh --check says whether its kit holds it elsewhere'` runs over
  `tools/check-wiring.test.sh`, it prints at least 1.
  Red when: the suite is as at `8a0e0b59`, where it prints 0.
- **AC10** — When `grep -c 'check_roles.py'` runs over `help/roles.md`, it prints at least 1.
  Red when: the page is as at `8a0e0b59`, where it prints 0.
- **AC11** — When `grep -c "neither mark is your own\|neither mark is the adopter's own\|an adopter's namesake and not"`
  runs over `help/roles.md`, `tools/roles/render_agents.py`, `tools/roles/README.md` and
  `memory/map/features/roles.md`, each prints 0, and `grep -c 'not counted as its kit'` prints at
  least 1 over each.
  Red when: a file is as at `8a0e0b59`, where each first count reads 1 and each second reads 0.
- **AC12** — When `grep -c 'Each tool-root citation of its'` runs over `help/roles.md`, and
  `grep -c 'citation the kit resolver holds'` over `tools/roles/README.md`, each prints 0, and
  `grep -c 'workflow table'` over `help/roles.md` prints at least 2.
  Red when: the pages are as at `8a0e0b59`, where the counts read 1, 1 and 1.
- **AC13** — When `bash tools/roles/adopt-roles.sh --scaffold` runs in this repository at `<p1>`,
  `git diff --quiet -- .claude/skills/build/SKILL.md .claude/roles.json` exits 0.
  Red when: the substitution writes an absolute path, and the diff names Skill lines 45 and 76
  among others.
- **AC14** — When `grep -c 'TOOL-dRenderedAnchor-3'` runs over
  `memory/gotchas/two-answers-to-one-question.md`, it prints at least 1.
  Red when: the record is as at `8a0e0b59`, where it prints 0.
- **AC15** — When `grep -c '^FLOOR_ASSERTIONS='` runs over `tools/roles/adopt-roles.test.sh` it
  prints 1, and the value on that line is 48 under C1 or 49 under C4.
  Red when: the arms land and the floor stays at 43, as `floor-left-below-the-arms-it-guards` names.
  figure: PINNED; one per floored `check_arm` that §4 adds to arms 14 to 16.

## 7. Gates

`roles render selftest` · `roles render wiring` · `roles adopter self-test` · `python resolver (behaviour + inline parity + idiom ban)` · `check-wiring self-test` · `memory hygiene` · `roles catalogue` · `install-prefix (shipped surface)` · `kit version markers` · `codebase-map coverage + freshness` · `recall floor` · `recall floor arms`

The first six are the brief's. `roles catalogue` reads the library S1 changes. The install-prefix
and kit-version legs grade the shipped kit files, and the codebase-map leg sees the minted symbol.
The last two are owed by the `memory/` guard the Files touched paths trip. That was derived on
2026-10-19 from `tools/gate-legs.json`, with the breadth floor `BROAD_LEG_FLOOR` at
`tools/check-spec-tokens.py:262`. Every other guard these paths reach is broad. The close runs the
bar once, after the unit is terminal; no pass runs a leg.

New arm: tools/roles/adopt-roles.test.sh, arm 14 · covers AC4 · TOOL_ROOT_CITE_RE narrowed to [A-Za-z.-]+ in tools/roles/roles_lib.py, so the tier2-review citation matches only its prefix · none
New arm: tools/roles/adopt-roles.test.sh, arm 14 · covers AC6 · resolve_cited_paths' .relative_to dropped in tools/roles/roles_lib.py, so the Skill names an absolute path · none
New arm: tools/roles/adopt-roles.test.sh, arm 14 · covers AC5 · the held lines applied with the unanchored bash loop of 8a0e0b59 in a copy of the adopter passed as ROLES_ADOPTER · FLOOR_ASSERTIONS rises by 1
New arm: tools/roles/adopt-roles.test.sh, arm 15 · covers AC2 AC3 · every citation resolved with here at the tool root, as at 8a0e0b59 · FLOOR_ASSERTIONS rises by 2 under C1, 3 under C4
New arm: tools/roles/adopt-roles.test.sh, arm 16 · covers AC7 · resolve_cited_paths catching LookupError alone · FLOOR_ASSERTIONS rises by 2
New arm: tools/lib/resolve-python.test.sh, section 2e row 7 · covers AC8 · root in hit.parents cut from tools/lib/resolve_kit_dir.py · none
New arm: tools/check-wiring.test.sh, the absent-harness remedy check · covers AC9 · the remedy tail dropped from the echo at tools/check-wiring.sh:1746 · none

## 8. Open questions

- **F1 — How does the `/build` Skill's citation pass answer a citation that is no harness of the workflow table?**
  The brief's item 1 asks that the pass never probe above the tool root and agree with
  `derive_kit_paths` on the same citation. It names "only the workflow table's harnesses" as an
  accepted form. The brief's Acceptance binds the skeptic's corrected fix, which leaves every other
  citation to plain substitution. Those two part on one layout: a run-gates or unattended kit under a
  per-entry install override recorded in the receipt. `8a0e0b59` resolves it through the receipt,
  and so does `derive_kit_paths`. The plain prefix names a path that does not exist there.
  - C1 — the skeptic's fix as written: harness pairs resolve with `here` at the tool root, and every
    other citation is plain. It is the smaller change. It returns the override row to its
    pre-unit-2 answer, which is two answers between the Skill and `BUILD-METHOD.md`. AC3 is struck,
    and the floor is 48.
  - C4 — harness pairs resolve with `here` at the tool root, and every other citation resolves with
    `here` at the roles kit directory, which is `derive_kit_paths`' own call. M1 is closed: no probe
    from the kit directory reaches `<repo>/<home>/` while the kit sits under a prefix. The override
    row keeps the receipt's answer. It costs one branch in `resolve_cited_paths`, one sub-check in
    arm 15, and AC3. The floor is 49.
  - Recommendation: C4. By BUILD-METHOD M3, after the three vetoes, it satisfies the most stated
    criteria: the brief's agreement clause for every non-harness citation, and the skeptic's
    role-index agreement for every harness. It leaves one follow-up open, the role index's own
    probe in §3, against C1's two. Neither option trips veto 2 or 3. This run holds no mandate, so
    the owner decides.
  - RESOLVED (owner, 2026-10-19): C4.

## 9. Revision log

- rev-1 · 2026-10-19 · initial draft from the unit's brief and the closing review's round-2 record.
  The skeptic's fixes were re-read against `8a0e0b59`. Item 1 of the brief and the skeptic's M1 fix
  part on one layout, which is F1. L7's wording claim was found in two more places than the review
  names: the README and the map. L4's row 7 writes its path from python, because a shell path in
  JSON would make it vacuous under MSYS.
- rev-2 · 2026-10-19 · §4 · S10 · AC8 · §10 · the build pass found a divergence: row 7's `<abs>`
  was `str(...)`, a backslash path on Windows that the receipt join's `/`-split
  (`tools/lib/resolve_kit_dir.py:39`) skips, so the section-2e arm could not be seen red. §4 now
  writes it with `.as_posix()` and says why, with the probe that showed it. AC8 and §7's section-2e
  `New arm:` line read through §4 and are unchanged. §10's gotcha line says "python-written and
  posix" in place of "native".

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "list the workflow table's workflow-driver harnesses for
a reader"` ranked `load_workflows` in `tools/roles/roles_lib.py` a SEAM, fan-in 4. Reading its
readers found the `driver == "workflow"` filter in `derive_harness_paths`
(`tools/roles/render_agents.py:162`) and in arm 14 (`tools/roles/adopt-roles.test.sh:519`). The
citation pass would be the next instance, so S1 extracts `extract_workflow_harnesses` beside
`load_workflows`, and `derive_harness_paths` reads through it (S4). Arm 14 deliberately does not
(§4 C5). `python tools/codebase-map/reuse_lookup.py "substitute template citations matched whole at
their boundary"` listed `resolve_cited_paths`, fan-in 1, and no substitution helper. The
substitution reuses `TOOL_ROOT_CITE_RE` itself through `re.sub`, so no existing seam fits a new
helper and none is minted. `resolve_kit_dir` stays the one resolver, and `derive_kit_paths`
(`tools/lib/render-doc.sh:168`) is the call C4's non-harness branch makes. The suite seams are
extended in place: `build_fixture` in `tools/roles/adopt-roles.test.sh`, section 2e in
`tools/lib/resolve-python.test.sh`, and the absent-harness block of `tools/check-wiring.test.sh`.

The brief and the record disagree in one place, which is F1. The review names L7's claim at
`help/roles.md` and the docstring. `tools/roles/README.md:231` and
`memory/map/features/roles.md:107` carry it too, so S12 reaches all four. The recall probe returned
the brief, the round-2 record, unit 2's spec and its ledger, which are this unit's sources, and
`TOOL-aWokenSentinel-21`, the precedent for a shrink-only `FLOOR_ASSERTIONS`.

The gotchas checklist for the touched paths selected `fixture-passes-by-finding-nothing`, which is
why row 7's path is python-written and posix, and why each term has a row only it rejects. It selected
`staged-break-substitutes-a-synthetic-value`, which is why each arm's names come from the shipped
template and table. It selected `two-answers-to-one-question`, which is S12 and S13, and
`test-oracle-read-from-a-historical-sha`, which is why no arm reads `8a0e0b59` and each red half
names it only as the observation's source. `empty-field-collapses-unless-it-is-last` no longer
applies to the pass, since the tab-separated read is deleted.

Recall terms used: `python tools/memory-recall/query.py "how should the build skill's citation pass
limit itself to the workflow table harnesses and substitute each citation whole" --terms
"resolve_cited_paths TOOL_ROOT_CITE_RE workflow-driver harness citation boundary population arm floor
adopt-roles derive_kit_paths namesake"`
