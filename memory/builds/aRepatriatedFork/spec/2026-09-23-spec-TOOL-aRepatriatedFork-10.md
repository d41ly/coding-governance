# TOOL-aRepatriatedFork-10 — the memory-tree engine grandfathers what it says it does, and its rendered docs state the adopter's own facts

**Status:** CLOSED · rev-2 · 2026-09-23 · node a · Tier-2 · base a7c78ad2 · streams tooling · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-23-build-TOOL-aRepatriatedFork-10-1-acceptance-ledger.md](../build/2026-09-23-build-TOOL-aRepatriatedFork-10-1-acceptance-ledger.md) | journal | — |
| [2026-09-23-prompt-TOOL-aRepatriatedFork-10-build-brief.md](../prompts/2026-09-23-prompt-TOOL-aRepatriatedFork-10-build-brief.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

NicoCares still carries nine carve-outs against the memory-tree kit a week after dRetiredFork
promised the kit's conf keys would absorb them. Measured by running gov's engine over nc's tree, four
of those carve-outs exist for one of three reasons. `LEGACY_SET` reaches a misnamed folder and not a
misnamed file. Check 21 has no answer for undated build artifacts. The kit's two rendered docs state
gov's own conf values and gov's own layout as if they were the adopter's. The rest need only
configuration nobody wrote down. This unit fixes the engine's three gaps, renders the adopter's facts,
and writes the configuration route down, so nc runs gov's engine and gov's rendered docs verbatim.

## 2. Scope (IN)

- **S1** — Check 4's per-entry branch consults `LEG` exactly as its folder branch does. Today
  `tools/memory-tree/check-memory-hygiene.sh:628` tests `LEG` for a bad folder name and the entry
  branch at `:636-637` tests nothing, so a grandfathered root FILE still reds. Observed by AC1.
- **S2** — Check 21's missing-Serves population skips a path `in_legacy` names, as check 5 does at
  `:658`. Observed by AC2.
- **S3** — A declared key, `RECORD_UNDATED_ARTIFACTS`, with values blank or `grade` meaning today's
  behaviour and `exempt` meaning an undated non-markdown file under `build/`, `prompts/` or
  `reviews/` is not graded by check 21. The count exempted prints on every run. Any other value
  aborts in the existing validation block. Observed by AC3 and AC4.
- **S4** — Check 3 whitelists `pass-order-waiver.txt`. The unattended kit reads it at its default
  path `$MEMORY_ROOT/project/pass-order-waiver.txt` (`tools/unattended/check-pass-order.sh:189`), so
  it is a KIT registry, the class `substitution-fed-loops.txt` already joined at `:533-539`. Observed
  by AC5.
- **S5** — `HYGIENE.template.md` renders two conf facts from the adopter's `.memory-tree.conf`
  through two new placeholders, `{{INDEX_CAP_LINES}}` and `{{ENTRY_CAP_UNIT}}`. The sentences at
  `tools/memory-tree/HYGIENE.template.md:62-63`, `:73` and `:182-187` state what THIS tree declares,
  and gov's own history of `INDEX_CAP_LINES=0` stays in gov's decision log. Observed by AC6.
- **S6** — `TOOL_ROOT` is derived from the receipt's `prefix` when `.governance/install.json`
  exists, and from the kit directory's parent otherwise. Today `adopt-memory-tree.sh:37` and
  `kit-dogfood-parity.test.sh:54` use the parent only, which is empty for a flat install, so nc's
  rendered `TEMPLATE-SPEC.md` names the codebase-map generator and extractors with no prefix while
  they sit under `scripts`, and nc registers both as dead paths in its
  `corpus-path-unresolved.txt` rows 38 and 39. Observed by AC7.
- **S7** — A class gate: `tools/check-kit-placeholders.py` refuses a `rendered` template that spells
  `KEY=value` for a key its own kit's `[config]` declares, since that is the repo's own value leaking
  into an adopter's doc. The key set is the `[config]` key lists, its `defaults`, and every key the
  kit's shipped `<file>.example` assigns; a key any `rendered` rule of that kit declares as a
  placeholder is exempt, because the kit states the adopter's value through it. Observed by AC8.
- **S8** — The project-leg seam dRetiredFork-16 ruled for nc's check 90, shipped as a worked,
  runnable example in `tools/memory-tree/README.md` rather than a JSON fragment and a promise, and
  its one unobserved claim observed. Observed by AC9.
- **S9** — `tools/memory-tree/README.md` gains an adopter section mapping each carve-out shape to
  its route, with the carve-out table in §4 as its worked instance. Observed by AC10.
- **S10** — `KIT_MEMORY_TREE_VERSION` moves and every paired marker moves with it; the two new
  placeholders join `placeholders` for `HYGIENE.template.md` in `tools/memory-tree/kit.toml`, and
  `RECORD_UNDATED_ARTIFACTS` joins `optional_keys` and the conf example. Observed by AC10.

## 3. Non-goals (OUT)

- A plugin loader, a `PROJECT_CHECKS` key, or any mechanism by which the engine runs project code.
  `TOOL-dRetiredFork-16` S5 refused it in writing and `tools/memory-tree/README.md:302-306` ships that
  refusal. S8 ships the seam that ruling named instead.
- Absorbing check 90 into gov. It grades nc's own comment convention.
- A git-date fallback for undated records. With S2 and S3 in place nc's `OLDU` path has no
  population left, which is the measurement that makes it unnecessary.
- nc carve-out 8, the recall grammar directory probe in `corpus_ids.py`. It is a derived kit path;
  unit 2 of this build owns that class.
- nc's unnumbered `corpus_ids.py` extension adding `CLAUDE.md` to check 15's dead-path corpus. It
  wants a governing-docs conf key and is filed rather than built here.
- A generic `{{CONF:<KEY>}}` placeholder. Two keys are cited today; each gets a named placeholder,
  following `{{READINESS_ROWS}}`.

### Edges

- **hands-off** external — a governing-docs list for check 15, which nc's unnumbered `corpus_ids.py` extension asks for
- **hands-off** external — NicoCares applies the §4 carve-out table in its own tree, config and data only

## 4. Design

### Data model

`RECORD_UNDATED_ARTIFACTS`, preset blank beside its siblings at
`tools/memory-tree/check-memory-hygiene.sh:117-124`, validated as a closed set beside `ENTRY_CAP_UNIT`,
and added to the observability loop at `:206`. The filter runs on check 21's A rows after the
existing cutoff filter: a basename with no leading ISO date and no `.md` suffix is dropped and
counted, and the count prints as `check 21: N undated non-markdown artifact(s) not graded
(RECORD_UNDATED_ARTIFACTS=exempt)` whether or not N is zero. It narrows a population, so it prints
rather than stays silent; it has no date and so cannot exempt everything the way a future cutoff can.

`gen_build_index.py`'s `read_bindings` is unchanged. Its comment at `:538-545` explains why a
record's kind comes from its folder and not its suffix, and that ruling stands for trees that do not
declare the key.

The two placeholders render inside `render_doc`, the canonical block at `tools/lib/render-doc.sh`
with its two byte-identical inline copies in `adopt-memory-tree.sh` and `kit-dogfood-parity.test.sh`,
exactly as `{{READINESS_ROWS}}` does. A key the conf does not declare renders as the literal text
`undeclared — the engine default applies`, so the doc never restates a default that lives in the
engine's preset block.

### Inventory

Every nc carve-out that touches the memory-tree kit, measured by running gov HEAD's engine over nc's
tree at `e2c26c5b` in a `--shared` clone (audit-D §6) and re-read at nc's merged tree on 2026-09-23.

| nc tag | nc site | What it does | Disposition |
|---|---|---|---|
| 1/24 | `.memory-tree.conf:295-301` | byte-counted entry caps | config, already a key; the HYGIENE note at nc `scripts/HYGIENE.template.md:63-69` becomes S5's render |
| 2/24 | `scripts/check-memory-hygiene.sh:530-536` | three nc registries under `project/` | config: `PROJECT_REGISTRY_EXTRA` |
| 3/24 | `scripts/check-memory-hygiene.sh:697-701` | run-protocol filenames skip check 5 | data: 13 rows in `memory/project/legacy-files.txt` |
| 4/24 | `.memory-tree.conf:290-302` | slug grammar | config, already a key |
| 5/24 | nc `:809` comment only | duplicate `pop_guard 6` | absorbed by `TOOL-dRetiredFork-1`; the duplicate is already gone from nc's tree |
| 6/24 | `scripts/check-memory-hygiene.sh:2569-2585` | check 90, orphaned status-derived comment | project leg, S8 |
| 7/24 | `scripts/check-memory-hygiene.sh:661-668` | root `STATUS.md` admitted by name | upstream S1, plus 10 rows in `legacy-files.txt` |
| 16/20 | `scripts/gen_build_index.py:203` | git env scrub | absorbed by `TOOL-dRetiredFork-2`; gov's own credit comment |
| 19/24 | `scripts/check-memory-hygiene.sh:1041-1080` | git-date fallback and undated non-md exemption | upstream S2 and S3 |
| 20/24 | `scripts/check-memory-hygiene.sh:537-545` | two nc ratchet registries | config: `PROJECT_REGISTRY_EXTRA` |
| untagged | `scripts/check-memory-hygiene.sh:546-553` | `unpainted-remote-forms.txt`, `spec-header-legacy.txt` | config: `PROJECT_REGISTRY_EXTRA` |
| untagged | `scripts/HYGIENE.template.md:189-192` | nc's `INDEX_CAP_LINES=500` note | upstream S5 |
| 8/24 | `scripts/corpus_ids.py:47-54` | recall grammar directory probe | unit 2 of this build |
| untagged | `scripts/corpus_ids.py:374-417` | `CLAUDE.md` in check 15's corpus | filed, §3 |

Populations, PINNED on 2026-09-23 at nc's merged worktree: 10 tracked build-root `STATUS.md`, all at
depth 4; 13 run-protocol files, 12 under `build/` and 1 under `spec/`; 479 undated text files that
are not markdown under `build/`, `prompts/` or `reviews/`, of which 230 are JSON, 177 HTML and 45
Python. The 12 markdown rows check 21 reds are exactly the 12 run-protocol files under `build/`.

### Migration

For gov and every adopter declaring nothing new, output is byte-identical except the rendered docs,
which now state the tree's own two values; gov's own render therefore still says `0` for
`INDEX_CAP_LINES`, because gov declares 0.

What NicoCares then does, in one commit, with no engine edit:

```
PROJECT_REGISTRY_EXTRA="pass-order-waiver.txt css-layout-allowlist.txt mvp-routes.txt operator-preconditions.txt heading-order-debt.txt art-ledger-waiver.txt unpainted-remote-forms.txt spec-header-legacy.txt"
RECORD_UNDATED_ARTIFACTS="exempt"
```

Then 23 rows in `memory/project/legacy-files.txt`, the 10 `STATUS.md` and the 13 run-protocol
files. Then check 90 moves to `scripts/check-build-readme-comments.sh` with its two fixtures, a gate
leg with a ceiling, and an `ARMS_FLOORS` token; its arms move out of nc's
`scripts/check-memory-hygiene.test.sh:825-846` and `:1010-1011`. Then nc takes gov's
`check-memory-hygiene.sh` and `HYGIENE.template.md` verbatim and re-renders `memory/HYGIENE.md`.
`pass-order-waiver.txt` may stay in nc's list after S4; it is then redundant, not wrong.

inCMS runs its own hygiene engine, `scripts/check-docs-hygiene.sh`, and carries its rendered docs as
declared forks. It gains nothing from S1-S4 until unit 13 of this build settles that engine's role;
S5 and S6 remove two of the reasons its `memory/guides/BUILD-METHOD.md` and `TEMPLATE-SPEC.md`
forks exist, and the rest of those rows' deltas are inCMS-only.

### Files touched (estimate)

- `tools/memory-tree/check-memory-hygiene.sh`
- `tools/memory-tree/HYGIENE.template.md`
- `tools/memory-tree/adopt-memory-tree.sh`
- `tools/memory-tree/kit-dogfood-parity.test.sh`
- `tools/lib/render-doc.sh`
- `tools/memory-tree/.memory-tree.conf.example`
- `tools/memory-tree/kit.toml`
- `tools/memory-tree/README.md`
- `tools/check-kit-placeholders.py`
- `memory/HYGIENE.md`, re-rendered

### Alternatives rejected

- **Admit `STATUS.md` by name in check 4**, as nc does. `TOOL-aRuledFrontispiece-7` retired that name
  from the whitelist on purpose, and the registry already exists for exactly this.
- **A suffix list for artifacts** (`RECORD_ARTIFACT_SUFFIXES="json html py"`). nc's 479 files span
  ten suffixes including `gitignore` and `patch`, so the list is a maintenance chore whose omission
  reds a tree for no defect. The structural rule, undated and not markdown, is the class.
- **Re-type the default into the rendered doc.** A value stated in prose beside the source that owns
  it rots between changes; the rendered text names the default's owner instead.

## 5. Production-readiness checklist

- security — no new write path; the new key is validated against a closed set before any check
  runs, and a conf value reaches the render through the existing quoted parameter substitution.
- perf / scale — one extra awk pass over check 21's A rows, and one `sed` read of the receipt.
- error / empty / loading states — blank key means today's behaviour; an unknown value aborts at
  exit 2 naming the key; an undeclared placeholder key renders its explicit undeclared text.
- observability — the exempted artifact count prints on every run, zero included, and the key
  joins the divergent-configuration notice.
- risks — `exempt` could hide a genuine undated record written in a non-markdown format. Bounded by
  the printed count, and by check 5, which already refuses a free-named markdown record.
- testing — one arm per scope item in `tools/memory-tree/check-memory-hygiene.test.sh`, plus the
  placeholder class arm in `check-kit-placeholders.py`'s own selftest.
- migration — additive; the only visible change for a non-declaring adopter is the two sentences in
  its rendered HYGIENE.md, which its dogfood-parity leg asks it to re-render.
- user docs — `tools/memory-tree/README.md`, the conf example, and the rendered HYGIENE.md.

## 6. Acceptance criteria

- **AC1** — When a fixture build root carries `STATUS.md` and `legacy-files.txt` lists it,
  `bash tools/memory-tree/check-memory-hygiene.sh` reports no check 4 finding; unlisted, it reports
  the path.
  Red when: the entry branch at `:636` still ignores `LEG`.
- **AC2** — When a fixture record under `build/` lacks a Serves line and `legacy-files.txt` lists it,
  check 21 does not name it.
  Red when: the A rows are filtered by date only.
- **AC3** — With `RECORD_UNDATED_ARTIFACTS=exempt`, a fixture JSON file named result under a build's
  build folder, with no Serves line,
  is not named by check 21 and the run prints `1 undated non-markdown artifact(s) not graded`; with
  the key blank, check 21 names it.
  Red when: the filter drops the file without printing, or runs when the key is blank.
- **AC4** — With `RECORD_UNDATED_ARTIFACTS=Exempt`, `bash tools/memory-tree/check-memory-hygiene.sh`
  exits 2 naming the key.
  Red when: an unknown value reads as blank.
- **AC5** — When a fixture tracks `memory/project/pass-order-waiver.txt` and declares no
  `PROJECT_REGISTRY_EXTRA`, check 3 reports nothing for it.
  Red when: the name is missing from the whitelist.
- **AC6** — When `bash tools/memory-tree/adopt-memory-tree.sh --render` runs in a fixture declaring
  `INDEX_CAP_LINES="500"` and `ENTRY_CAP_UNIT="bytes"`, the rendered `memory/HYGIENE.md` states
  both values and contains no `INDEX_CAP_LINES=0`.
  Red when: the template still spells gov's value.
- **AC7** — When the same render runs from a kit installed flat at `scripts/` with a receipt whose
  `prefix` is `scripts`, the rendered `memory/TEMPLATE-SPEC.md` names the codebase-map generator
  under the `scripts` prefix.
  Red when: `TOOL_ROOT` is still the empty parent of a flat kit directory.
- **AC8** — `python tools/check-kit-placeholders.py` exits 1 on today's
  `tools/memory-tree/HYGIENE.template.md`, naming `INDEX_CAP_LINES`, and exits 0 after S5.
  Red when: the arm scans no template or skips keys absent from `optional_keys`.
- **AC9** — When the leg's argv, `bash scripts/check-build-readme-comments.sh`, runs in a fixture
  where the script is absent, it exits 127 naming the script, and `tools/memory-tree/README.md`
  ships the runnable script and says which half of `TOOL-dRetiredFork-16`'s claim that observes.
  Red when: the README ships a fragment and a promise, or claims the runner half as observed.
  cost: a fixture runner hung past 300 s the last time this was attempted; the observation needs a
  bounded single-leg manifest.
- **AC10** — `bash tools/check-kit-versions.sh` exits 0 after the bump, and `tools/memory-tree/README.md`
  names `PROJECT_REGISTRY_EXTRA`, `legacy-files.txt`, `RECORD_UNDATED_ARTIFACTS` and the project leg
  as the four adopter routes.
  Red when: a paired marker stays on 2.85, or a route is undocumented.

## 7. Gates

`memory hygiene` · `memory-hygiene self-test` · `kit/dogfood doc parity` · `recall floor` · `recall floor arms` · `kit placeholders (a declared token its adopter substitutes)` · `kit-placeholders self-test` · `python resolver (behaviour + inline parity + idiom ban)` · `kit version markers` · `verdict epoch (kit version dates the engine)`

New arm: `tools/memory-tree/check-memory-hygiene.test.sh` · a legacy-listed root `STATUS.md`, a legacy-listed unbound record, an undated `result.json` under each key value, and a tracked `pass-order-waiver.txt` · the hygiene gate's `ARMS_FLOORS` token moves by the branches S3 adds
New arm: `tools/check-kit-placeholders.test.sh` · a template spelling `INDEX_CAP_LINES=0` under a kit whose conf declares that key · none
New arm: `tools/memory-tree/check-memory-hygiene.test.sh` · a flat `scripts/` install with a receipt, rendered through `--render` · none

## 8. Open questions

- **F1 — `exempt` or a cutoff-scoped exemption?** nc applies its artifact rule only inside the
  `RECORD_SERVES_CUTOFF` branch, so an undated artifact landed after the cutoff is still graded there.
  Options: (a) S3 as written, independent of the cutoff; (b) scope it to the cutoff as nc does.
  Recommendation: (a). A JSON file cannot carry a Serves line at any date, so a date is not what
  decides it.
  RESOLVED (owner, 2026-09-23): (a), independent of the cutoff, as recommended.
- **F2 — the receipt as the `TOOL_ROOT` source.** A copy-installed adopter has no receipt and keeps
  the parent derivation, which is right for any kit-per-directory layout and wrong only for a flat
  one. Options: (a) receipt then parent; (b) a declared `TOOL_ROOT` key in `.memory-tree.conf`.
  Recommendation: (a), because the receipt already records the prefix and a second declaration of it
  is a second copy.
  RESOLVED (owner, 2026-09-23): (a), receipt then parent, as recommended.
- **F3 — does S8 need pre-commit reach?** nc's check 90 ran under `--staged` inside the engine; as a
  project leg it runs at the push bar only, which is a later signal. Gov does not ship
  `.githooks/pre-commit` to adopters, so nc can call its script from its own hook. Recommendation:
  say so in the README example and build nothing.
  RESOLVED (owner, 2026-09-23): a README note, build nothing, as recommended.

## 9. Revision log

- rev-1 · 2026-09-23 · initial draft, from audit-D §6 and §7 and nc's merged tree, with the
  populations re-measured on node a.
- rev-2 · 2026-09-23 · built. S7 and AC8 moved: the predicate run over the real tree before wiring
  redded two unattended templates spelling `ANCHOR_SCOPE="published"` as a described value, and
  rewriting them changes `memory/guides/UNATTENDED-PROTOCOL.md`, a governance carrier; so a key the
  kit renders as a placeholder is exempt, and the key set also reads the kit's conf example, where
  `INDEX_CAP_LINES` is declared. The HYGIENE template's `ROTATION_MODE` sentence was reworded to pass.
  AC9 moved: a unit pass runs no gate runner, so it observes the leg's own exit instead, and the
  runner half stays recorded as unobserved in the README. S3's count line goes to stderr beside the
  other configuration notices. S3 adds no `fail` branch, so the hygiene `ARMS_FLOORS` token does not
  move.

## 10. Reuse audit

Every change rides an existing seam. The preset-and-validate block in
`tools/memory-tree/check-memory-hygiene.sh` already holds five project keys and `LEGACY_SET` already
feeds checks 4 and 5; the render placeholders ride `render_doc` in `tools/lib/render-doc.sh`, found by
grep because `reuse_lookup.py` reports `.sh` as an unscanned layer; its ranked `load_conf` and
`parse_conf` seams are the Python readers and are not what renders a doc. `TOOL-dRetiredFork-15` and
`TOOL-dRetiredFork-16` are the records this unit completes.

Recall terms used: `memory-tree`, `LEGACY_SET`, `in_legacy`, `check 4`, `check 21`, `Serves`,
`RECORD_SERVES_CUTOFF`, `PROJECT_REGISTRY_EXTRA`, `carve-out`, `render_doc`, `TOOL_ROOT`,
`HYGIENE.template`, `project leg`, `adopter`.
