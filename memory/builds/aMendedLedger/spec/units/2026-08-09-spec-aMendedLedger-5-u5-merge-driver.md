# TOOL-aMendedLedger-5 — U5: the row-keyed merge driver, its launcher shim and its wiring

**Status:** SPECCED · rev-2 · 2026-08-09 · node a · Tier-2 · base 663ca427 · streams tooling

## 1. Goal

Port upstream `ARCH-dQuarriedLedger-1` U9 into this repo: a three-way merge driver that key-merges
`memory/DECISIONS.md` and `memory/backlog/*.md` by record id, so an append-collision between two
nodes auto-resolves without ever duplicating or dropping a row. The master's S5 names five parts —
the driver, its launcher shim, its `.gitattributes` entries, its per-node `git config` wiring and its
replay test — and this unit builds all five plus the gate leg that keeps them honest.

## 2. Scope (IN)

- **S1** New `tools/lib/pyrun.sh`: source `tools/lib/resolve-python.sh`, then
  `PY=$(resolve_python) || exit 2; exec "$PY" "$@"`. Git never runs through `tools/run-gates.sh`, so
  the `$PYBIN` substitution at `tools/run-gates.sh:52` does not reach a merge driver and the shim is
  the only place the launcher can be resolved.
- **S2** New `tools/memory-tree/merge-rows.py`: the master's §4 decision table implemented exactly,
  three regions, fail-closed, `write_bytes`, with the anchor grammar IMPORTED from
  `tools/memory-recall/extract.py` through `grammar_for(root)` and `anchor_at(line, g)` — never
  vendored, and deferred into the first anchor call.
- **S3** `.gitattributes` gains `memory/DECISIONS.md merge=rows` and `memory/backlog/*.md merge=rows`.
- **S4** `tools/check-wiring.sh` gains a `check_merge_rows` case in the shape of its existing arms: an
  unset `merge.rows.driver` is REPORTED in `--check` and SET in `--fix`/`--session`, and a value
  someone else set is never clobbered. `tools/check-wiring.test.sh` gains fixtures for those states.
- **S5** New `tools/memory-tree/merge-rows.test.sh`: the master's AC7 (a)-(d), the delete/modify
  interaction in both directions, the union-shape conflict, and an end-to-end two-branch `git merge`
  through the real `.gitattributes` + `git config` wiring.
- **S6** `tools/gate-legs.json` gains the leg `row-keyed merge driver replay`, and `AGENTS.md`'s gate
  suite gains a bullet citing `tools/memory-tree/merge-rows.test.sh` verbatim.
- **S7** New codebase-map dossier `memory/map/features/memory-tree-merge-driver.md`, structured as a
  copy of `memory/map/features/codebase-map.md` because the gate imposes three requirements past
  "claim the leg name": a fenced TOML block carrying EXACTLY the seven top-level keys `feature`,
  `title`, `status` (`shipped`), `streams` (`["tooling"]`), `decisions`, `claims` and `paths` — a
  missing or unknown one is a hard `MapError` at `tools/codebase-map/map_lib.py:601`; a `[claims]`
  table holding ALL NINE inventory ids, `gate-legs = ["row-keyed merge driver replay"]` and the other
  eight `[]`, because `missing_c`/`unknown_c` raise at `map_lib.py:619-629`; and the three pinned
  prose headings `## Constraints & why`, `## Shared seams`, `## Gaps` (`REQUIRED_HEADINGS`,
  `map_lib.py:49`) plus `## Reuse affordance` (`AFFORDANCE_HEADING`, `map_lib.py:55`) carrying at
  least one `seam:` line — the affordance check is GRACED by a shrink-only exempt list that new
  dossiers are never on (`tools/codebase-map/test_codebase_map.py:68-85`). Only `gate-legs` is
  claimed: `kits`/`memory-tree` sits in `baseline.toml` and claiming it here would raise LAZY
  BASELINE and make a merge-driver dossier the recorded owner of the whole kit. Plus a regeneration
  of `memory/map/generated/`.
- **S8** `.claude/SESSION-KICKOFF.md` carries its own `last-audit` re-stamp in this same commit,
  because this commit stages the watched path `tools/gate-legs.json`.
- **S9** `tools/memory-tree/README.md` gains one table row per new kit file, so the kit's own
  hand-kept file table does not go stale in the commit that makes it stale.

## 3. Non-goals (OUT)

- **`merge=union`.** Rejected on upstream's measurement, not preference: union introduced a duplicate
  in 147 of 151 historical `DECISIONS.md` conflicts. Master §3 states this and it is not reopened.
- **Adopter packaging of the driver.** `tools/memory-tree/adopt-memory-tree.sh` is untouched. A
  copy-installed memory-tree kit lands at `<root>/memory-tree/` and cannot reach `tools/lib/pyrun.sh`
  at all, so shipping the driver to adopters is a kit-layout change with its own blast radius.
  Follow-up, not this unit. The driver still RESOLVES both layouts (§4 Data model) so the follow-up
  is a packaging question rather than a rewrite.
- **The `regenerate` driver.** Withdrawn upstream for a structural reason: `ort` checks the merge
  result out only AFTER the per-path merges run, so a generator invoked from inside a driver renders
  from the pre-merge tree.
- **Any content change to `memory/DECISIONS.md` or `memory/backlog/*.md`.** U7 owns the rows. This
  unit only reads them, in the identity arm.
- **An `eol=lf` pin on the two governed indexes.** `.gitattributes:2` already normalises committed
  blobs with `* text=auto`, and the driver is newline-preserving by construction, so the pin buys the
  driver nothing while rewriting worktree bytes on every node's next checkout.
- **Touching `tools/memory-tree/check-memory-hygiene.sh`.** U3 owns it. Any non-comment edit there
  drags in the `KIT_MEMORY_TREE_VERSION` coupling, and U5 has no reason to pay it. Re-read at master
  rev-4: F6 is now `RESOLVED (build, 2026-08-09)` and the `:346` `ex7` rewrite that rev-2 listed as a
  master Non-goal is IN, in U3 — so that constant moves in U3's commit, and this unit still touches
  neither the file nor the constant.
- **Writing this build's spec id into any product-glob file.** `tools/`, `skills/`, `.claude/`, the
  playbook template + its two companions and `WIRE-INTO-PROJECT.md` are `PRODUCT_GLOBS`
  (`tools/drift-audit/drift_signals.py:20-28`). The build is cited by SLUG in source comments; see §7
  coupling 5.
- **Fixing the codebase-map prefixed-install defect.** Recorded in `memory/map/features/codebase-map.md`
  §Gaps and spun off; this unit works around it exactly as the conf's note prescribes.

## 4. Design

### Data model

A file is **three regions** — preamble, row block, trailer — and only the row block is key-merged.
The row block spans the first anchored line to the last, inclusive. Preamble and trailer take an
ordinary three-way text merge through `git merge-file`. The split is load-bearing here and not a
generality, and the measurement is re-taken here because rev-1 mis-stated it: `memory/DECISIONS.md:1`
is the title `# decisions — index`, `:3-4` are two BLOCKQUOTE routing lines (there is no bolded
rotation note — that is upstream's file), `:6` is `## PLAY — playbook` and the first anchored line is
`:8`. `memory/backlog/TOOL.md:1-3` is a title plus a blockquote mutability note, first anchor `:4`.
An unconditional "a line the grammar cannot key conflicts" rule would therefore conflict on every
merge and never reach the auto-resolve.

**THE REGION RULE WINS at the block boundary.** The row block is
`lines[first_anchor:last_anchor+1]` (`C:/projects/incms/main/scripts/merge-rows.py:91-96`,
`split_regions`), so on `memory/DECISIONS.md` the block starts at `:8` and `:1-7` — INCLUDING the
first section heading `## PLAY — playbook` at `:6` — is preamble and takes the ordinary text merge.
This is stated because the two rules otherwise collide at exactly one line and the builder would have
to invent the precedence, and the invented answer changes behaviour whenever the first section
heading moves.

A **row is its lead-in plus its anchor line**, and that rule governs unkeyed lines INSIDE the block
only. Unkeyed lines attach to the FOLLOWING anchor, so a section heading travels with the first row
of its section. Measured on this corpus: `## KICK — kickoff` and `## TOOL — tooling` (and the
`*(none yet)*` placeholder under KICK) DO sit inside the block, INTERLEAVED between anchored rows —
which is what makes the attach-to-FOLLOWING-anchor rule load-bearing. A driver that carried unkeyed
lines in a side list and re-emitted them at the end would move those headings to the bottom of the
file while exiting 0.

The decision table, implemented exactly as the master ratified it:

| case | result |
|---|---|
| id in `%B` only | append |
| id in `%A` only | keep |
| id in both, text identical | keep once |
| id in both, one side equals `%O` | take the side that changed |
| id in both, both changed | CONFLICT with markers |
| id in `%O` and one side, other side untouched | honour the delete |
| id deleted one side, MODIFIED the other | CONFLICT, both directions |
| a line the grammar cannot key, inside the row block | attaches to the FOLLOWING anchor, rc 0 |
| preamble / trailer | ordinary three-way text merge |

The last two rows correct the upstream SPEC from the shipped upstream CODE, and the code is the
authority. `C:/projects/incms/main/scripts/merge-rows.py:173-228` splits the delete case five ways,
not two, and `:99-126` shows the unkeyable line attaching to the next anchor with rc 0 rather than
conflicting. Both are ported as written there.

**Audit counters are incremented at the EMIT sites**, never derived from the input lists. Upstream's
first cut printed `sum(1 for k in a_order if k in A)`, which `rows()` makes a tautology, and it
announced `3 row(s) from ours … clean` over a file it had just written with one row. `kept + took_b`
is the anchored-row count of the file on disk, which is what makes the line reconcilable; `dropped`
is printed even when it is 0, because an omitted term reads exactly like a zero.

**The usage text must carry the four placeholders**, and this DIVERGES from upstream. `main()` prints
usage on `len(argv) < 4`, but upstream prints `__doc__.split("\n\n")[0]`
(`C:/projects/incms/main/scripts/merge-rows.py:255`) — the first docstring paragraph, which at `:2`
is the summary sentence only; the `git config merge.rows.driver '… %O %A %B %P'` line is the SECOND
paragraph, at `:4`, and is never printed. A verbatim port therefore fails AC2. Take
`__doc__.split("\n\n")[:2]` joined, or hoist the
`git config merge.rows.driver 'bash tools/lib/pyrun.sh tools/memory-tree/merge-rows.py %O %A %B %P'`
line into the first paragraph. Either is fine; printing only the summary sentence is not.

**The grammar is imported, never vendored, and the import is deferred.** This repo's
`tools/memory-recall/extract.py:315-344` exposes `grammar_for(root)`, which re-resolves
`.memory-tree.conf` at an EXPLICIT root and returns a bundle carrying `ID_RE` and the four anchor
regexes built from that repo's `FAMILIES`. `extract.py:294-308` exposes `anchor_at(line, g)`, which
is the exact "which id does this line define" predicate the driver needs. The driver calls those two
and re-types neither, so an adopting repo with different families keys on its own ids.

Anchor resolution, deferred into the first `key()` call so every failure below lands in `main()`'s
fail-closed handler rather than killing the process before `%A` is written:

- the **anchor root** is the nearest ancestor directory of `__file__` holding `.memory-tree.conf`.
  Not `git rev-parse`: in a linked worktree the WSL bash resolves ahead of MSYS and cannot read a
  `gitdir:` pointer, which is the failure `C:/projects/incms/main/scripts/pyrun.sh:17-23` documents.
  Not a fixed `parents[2]`: that is correct only at this repo's `tools/` install prefix, and the
  walk-up is correct at both prefixes with no env var and no second declaration.
- the **kit directory** is the first of `<root>/tools/memory-recall` and `<root>/memory-recall` that
  exists — the same two-layout resolution `tools/check-wiring.sh:35` (`first_of`) already supplies for
  both kit layouts. Order is tools-first, copied from `tools/check-wiring.sh:127`
  (`first_of tools/settings-merge.py settings-merge.py`); note that `:122` spells the same pair
  ADOPTER-first, so the two live sites already disagree on order. Take the order from `:127`, not
  from `:122` — only the resolution rule is load-bearing here, and a spec that cites a site using the
  opposite order hands the builder a coin flip.
- `sys.path.append`, never `insert(0, …)`: prepending puts the kit dir ahead of the stdlib, so a
  module name it ever gains shadows the real one, and this driver imports `tempfile` at
  `text_merge`.
- a missing conf, an unreadable `extract.py`, a malformed one, or a missing kit dir all RAISE, and
  the raise is caught.

**Failure is closed.** Any exception becomes a whole-file conflict: `%A` is rewritten as
`<<<<<<< ours` + ours + `=======` + theirs + `>>>>>>> theirs (merge-rows failed; resolve by hand)`
and the driver exits 1. The alternative is what a crashing driver actually does — exit non-zero
without writing `%A`, leaving the path unmerged holding OURS-only content with no markers and the
incoming rows simply absent.

**Newlines are never translated, at any of FOUR sites.** This repo's nodes are CRLF: `core.autocrlf`
is `true`, `.gitattributes:2` is `* text=auto` with no `eol` pin on the governed indexes, and
`memory/DECISIONS.md`, `memory/backlog/TOOL.md` and `memory/backlog/DEPL.md` all hold CRLF in the
worktree while their index blobs are LF. Git hands a merge driver WORKING-TREE-format temp files, so
`%O %A %B` arrive CRLF. Stating only the write half is what makes AC7's `cmp` red on every governed
file, and makes a real merge silently rewrite the whole file's line endings:

1. **read** — `open(p, 'r', encoding='utf-8', errors='replace', newline='')` then
   `splitlines(keepends=True)`. `newline=''` is what suppresses universal-newline translation, so the
   `\r\n` stays on the line. (Upstream does this at `C:/projects/incms/main/scripts/merge-rows.py:248-250`.)
2. **temp files** — `text_merge`'s three temps are written `write_text(..., newline='')`, same
   reason (upstream `:141`).
3. **`git merge-file`'s stdout** — captured as BYTES (`capture_output=True` with **no** `text=True`)
   and decoded `.decode('utf-8', 'replace')`. **This diverges from upstream**, which passes
   `capture_output=True, text=True, encoding="utf-8"` at `:147`; `text=True` is universal-newline
   mode, so it returns a CRLF preamble as LF and site 2's careful `newline=''` is undone one line
   later. Upstream solves sites 1, 2 and 4 and does NOT solve this one — do not port `:147`.
4. **write** — the result goes out through `write_bytes` (upstream `:275`, `:279`). `write_text` on
   the result retranslates and is BANNED.

**Conflict markers are labelled.** `git merge-file` is invoked with `-L ours -L base -L theirs`;
without them git labels the conflict with the temp FILENAMES and the author resolves a file reading
`<<<<<<< C:\Users\…\tmpqm5j4r78\a`.

**No 3.12-only syntax.** The `verdict` string is hoisted out of the print rather than inlined as a
nested same-quote f-string: that shape is PEP 701 and a SyntaxError on 3.11. `tools/lib/resolve-python.sh:30-37`
imposes NO version floor — each candidate is accepted on `-c "import sys"` alone — so the interpreter
a node hands the driver is whatever it has, and a driver that fails to start is the silent-take-ours
shape again.

**The wiring is one literal command**, and the arm that reports it BUILDS it from the two resolved
paths rather than hand-keeping a second copy of the string:

```bash
git config merge.rows.driver 'bash tools/lib/pyrun.sh tools/memory-tree/merge-rows.py %O %A %B %P'
```

**`tools/lib/pyrun.sh` and the byte-identical inline-copy rule.** `tools/lib/resolve-python.test.sh:85`
derives the parity population by `git grep -l '^# >>> resolve_python' -- '*.sh'`, so the rule binds a
file only if it carries that marker. `pyrun.sh` SOURCES the resolver and must therefore NOT carry the
marker block — carrying it would enlist the shim in a parity gate it has no reason to be in. Two
other arms of that same test DO bind it, because their population is every tracked `*.sh` except
`tools/lib/resolve-python*`: the retired-idiom ban at `:99-102` and the bare-invocation ban at
`:137-152`. The specified body clears both, and `:166-167` asserts that exact shape is not caught.
`pyrun.sh` also does NOT `cd`, unlike its upstream ancestor: git invokes a merge driver with cwd at
the top of the working tree and passes `%O %A %B` relative to it, so moving the cwd can only break
paths that are already correct.

### Inventory

| fact | measured at | source |
|---|---|---|
| `tools/lib/pyrun.sh` does not exist | `f9cf666` | `git ls-files \| grep -i pyrun` returns nothing |
| the resolver is source-and-call, executes nothing | `f9cf666` | `tools/lib/resolve-python.sh:25-53` |
| gate legs today | `f9cf666` | `tools/gate-legs.json` holds 38 entries; this unit makes it 39 |
| the charter-vs-manifest pin | `f9cf666` | `tools/drift-audit/drift_signals.py:136` = 7, matched on argv path |
| `merge-rows.py` is NOT in the verdict-epoch scan | `f9cf666` | `tools/memory-tree/check-verdict-epoch.sh:51-52` names one `ENGINE` + three `DELEGATES` |
| `merge-rows.test.sh` is NOT in the check-arms population | `f9cf666` | `tools/memory-tree/check-arms.py:114-131` excludes `*.test.sh` and requires a `fail()` helper |
| two backlog shards carry zero anchors today | `f9cf666` | `memory/backlog/DEPL.md`, `memory/backlog/KICK.md` are 3 lines of preamble |
| the corpus id families | `f9cf666` | `.memory-tree.conf:15` — `PLAY KICK TOOL DEPL` |
| the spec-citation signal is AT its pin, with headroom 0 | HEAD | `drift_report.py` → `non_terminal_specs_cited_by_product_source 2 15`, pin `2` (`drift_signals.py:128`) |
| no product-glob file cites this build today | HEAD | `git grep -l -F 'TOOL-aMendedLedger-' -- tools skills .claude 'parallel-coding-governance*.md' WIRE-INTO-PROJECT.md` → rc 1, no output |
| the governed indexes are CRLF in the worktree | HEAD | `core.autocrlf=true`; `.gitattributes:2` `* text=auto`, no `eol` pin on `memory/DECISIONS.md` or `memory/backlog/*.md` |

Fixture ids are therefore `TOOL-zFixture-<n>`, not upstream's `ABL-dFixture-<n>`: the grammar is
family-gated, so an `ABL-` fixture anchors NOTHING here and every arm would pass by finding nothing.
`zFixture` matches the session era `[a-z][A-Za-z]{2,}-\d+` (`tools/memory-recall/extract.py:331`) and
collides with no real slug.

The fixture ids live in the TEST FILE only, never spelled as literals in this spec. Check 14 harvests
ids from the present-tense `memory/` corpus, so a fixture id spelled with a literal digit makes the
gate demand a definition for a fixture that has none — measured: three check-14 findings, and
registering them would push `ORPHAN_ID_PIN` from 5 to 8 against a shrink-only pin. The `<n>`
placeholder form does not match `\d+` and is therefore not harvested.

### Migration

Nothing moves and no existing file changes shape. `.gitattributes` gains two lines; every other
edit is an addition. A node that has not run `check-wiring.sh --fix` since this lands has
`merge=rows` declared with no driver configured, and git falls back to its built-in three-way text
merge with a warning — the pre-change behaviour, which is why the attribute and the config can land
in one commit without a flag day.

### Rollout

One commit. U5 is independent of U1, U2, U3, U4, U6 and U7 and touches none of their files. Order
inside the commit only matters for two derived artifacts, which must be regenerated LAST:

1. sources: `tools/lib/pyrun.sh`, `tools/memory-tree/merge-rows.py`, `tools/memory-tree/merge-rows.test.sh`;
2. wiring: `.gitattributes`, `tools/check-wiring.sh`, `tools/check-wiring.test.sh`;
3. registry + docs: `tools/gate-legs.json`, `AGENTS.md`, `tools/memory-tree/README.md`;
4. the map: the new dossier, then `python tools/codebase-map/gen_map.py --write`;
5. the manifest re-stamp in `.claude/SESSION-KICKOFF.md`, taken from `date`.

Step 4 is last because `memory/map/generated/` is byte-compared against a fresh render, and both
the new leg NAME (`gate-legs` inventory) and `merge-rows.py`'s new python symbols (`kit-py` layer)
move it. Step 5 is last because the C5s leg compares the staged manifest blob's stamp against HEAD's.

### Files touched (estimate)

**New:** `tools/lib/pyrun.sh`, `tools/memory-tree/merge-rows.py`, `tools/memory-tree/merge-rows.test.sh`,
`memory/map/features/memory-tree-merge-driver.md`.
**Edited:** `.gitattributes`, `tools/check-wiring.sh` (one `check_merge_rows` function plus its line
in the call list at `:244-247`), `tools/check-wiring.test.sh`, `tools/gate-legs.json`, `AGENTS.md`
(one gate-suite bullet), `tools/memory-tree/README.md` (two table rows),
`.claude/SESSION-KICKOFF.md:5` (the `last-audit` value), `memory/map/generated/inventories.json`,
`memory/map/generated/MAP.md`, `memory/map/generated/symbols.json`.

The `check_merge_rows` arm, stated as its states so the builder does not invent them. Column widths
copy the existing arms exactly: a 9-character status field, then a 10-character label field
(`merge` plus five spaces), then the em dash.

| state | output | exit contribution |
|---|---|---|
| `merge-rows.py` resolves to nothing | `skip     merge     — memory-tree merge driver not adopted` | none |
| driver present, `pyrun.sh` absent | `UNWIRED  merge     — …the shim it names is missing` | `unwired++` |
| both present, no tracked path resolves `merge: rows` | `skip     merge     — no path declares merge=rows` | none |
| attribute declared, config unset, `--check` | `UNWIRED  merge     — … Fix: git config merge.rows.driver '<built string>'` | `unwired++` |
| attribute declared, config unset, `DO_FIX=1` | `FIXED    merge     — set merge.rows.driver` | none |
| config set to something else | `UNWIRED  merge     — …NOT overwriting (deliberate?)` | `unwired++` |
| config set to the built string | `ok       merge     — merge.rows.driver wired` | none |

Three shapes are copied rather than reinvented: `first_of` (`tools/check-wiring.sh:35`) resolves both
kit layouts; the never-clobber rule mirrors `check_hooks` at `:70-77`; and setting under `--fix` AND
`--session` mirrors `check_hooks:80-81`, which already sets a git config under both. The `eol` arm's
session exemption is deliberately NOT copied — that arm rewrites file bytes, and this one sets a
repo-local config, which is the same class of act `--session` was created for.

The declared-attribute predicate is ONE call over EVERY tracked path — not a grep of `.gitattributes`
and not a fork per file:

```bash
git ls-files | git check-attr --stdin merge | sed -n 's/: merge: rows$//p'
```

Non-empty means at least one tracked path declares `merge=rows`; empty is the `skip` state in the
table above. rev-1 said "the tracked paths that resolve to `rows`", which is circular — that
population IS the thing being computed — and the two obvious inventions both fail: hardcoding the
paths puts a second copy of `.gitattributes`' truth into `check-wiring.sh`, and looping per file is
~500 process spawns inside a SessionStart hook. `--stdin` keeps it to one process regardless of tree
size, and reading what GIT judges rather than grepping `.gitattributes` is the same rule `check_eol`
follows at `tools/check-wiring.sh:183-186` (attributes come from several files, so the arm must judge
what git judges).

### Alternatives rejected

**Vendoring the anchor regexes into the driver.** Rejected: two copies of a regex is this repo's
catalogued drift class, and `extract.py`'s four anchor patterns are already byte-identical to
upstream's. A stale-but-single grammar beats two that disagree. The residual exposure is stated
rather than hidden: the driver is a pure function of `%O %A %B` PLUS the worktree's grammar, so a
merge that itself changes `FAMILIES` keys its index merge on the pre-merge grammar. At worst a row
whose anchor only the new grammar recognises is treated as unkeyed content; no row is invented or
duplicated.

**Importing the grammar at module scope.** Rejected on upstream's measurement: at module scope an
unreadable `extract.py` kills the driver before `%A` is written, git leaves OURS-only content with
no markers, and the incoming rows are gone with nothing saying so.

**Adding the new leg name to `baseline.toml`.** Rejected: `memory/map/features/codebase-map.md:43-45`
records the baseline as shrink-only and the initial-backfill-only rule, and records that the map's
own first leg failed the coverage assert until a dossier claimed it. A new dossier is the sanctioned
route, and it is also the more useful one — 69 of 71 keys are still unclaimed, and this adds the
second dossier the map has.

**Claiming the leg inside `memory/map/features/codebase-map.md`.** Rejected: that dossier owns the
map kit, not the merge driver, and a claim there would make the map's own feature the recorded owner
of a memory-tree gate.

**Porting upstream's `uv python find 3.11` parse arm verbatim.** Rejected: this repo's bar depends on
`uv` nowhere, and `resolve_python` imposes no version floor, so "the oldest interpreter `pyrun.sh`
accepts" is not a knowable set here. Replaced with two arms that cannot silently skip — a
`py_compile` of the driver under the resolved interpreter, and a source-level ban on the nested
same-quote f-string shape, which is version-independent.

**Guarding the new leg with a `guard` pathspec list.** Rejected: the identity arm reads
`memory/DECISIONS.md` and `memory/backlog/*.md`, which change independently of the driver, so a
guard keyed on the driver's own paths would skip the leg on exactly the diffs that can break it.

## 5. Production-readiness checklist

- security — the driver reads three local blobs git handed it and writes one. It executes nothing and
  reaches no network. Wiring it makes git RUN a script during a merge, which is the same trust
  boundary `core.hooksPath` already crosses in this repo; `--check` reports before `--fix` acts.
- perf / scale — one process per conflicted path during a merge. The governed files are 83 and 3-20
  lines. The new gate leg spins throwaway git repos, each carrying the three `tools/`-prefixed
  directories AC9 enumerates; it is comparable to `tools/check-wiring.test.sh`. The `check_merge_rows`
  arm added to the SessionStart path costs one `git ls-files | git check-attr --stdin` pipeline, not a
  fork per tracked file.
- a11y — N/A. No user interface.
- i18n — N/A. The only strings are conflict markers and one stderr audit line, both consumed by git
  and by the operator resolving the merge.
- error / empty / loading states — an empty `%O` (added on both sides) merges as a pure union of
  keys; a file with no anchors at all is entirely preamble and round-trips; every exception becomes a
  whole-file conflict. All three are asserted.
- observability — the stderr line `merge-rows: <kept> row(s) from ours, <took> new from theirs,
  <dropped> dropped (delete honoured), <verdict>` is the only output, and AC5 forces it to reconcile
  against the file on disk rather than against the inputs.
- risks — **data loss is the live risk**: a driver that drops a row exits 0 and prints nothing
  alarming. AC4 (id-set equality on every rc-0 case) and AC5 (counts reconcile against the result)
  are the two controls. Rollback is `git config --unset merge.rows.driver` plus reverting two
  `.gitattributes` lines; git then falls back to its built-in text merge and nothing else changes.
- testing + left-shift gates — one new leg, always run, no guard. Every `fail`-shaped assertion in the
  new test carries its own red fixture, including the two exemption arms.
- migration / rollback — no data moves; see §4 Migration. Per-node wiring is reported before it is
  applied.
- user docs — `AGENTS.md`'s gate-suite bullet and `tools/memory-tree/README.md`'s file table. The
  ADOPTER-facing surface (`WIRE-INTO-PROJECT.md`) is U6's S6b, not this unit's.

## 6. Acceptance criteria

- **AC1** When `git check-attr merge -- memory/DECISIONS.md memory/backlog/TOOL.md` is run after this
  unit, each path reports `merge: rows`. (Master AC6.)
- **AC2** When `bash tools/lib/pyrun.sh tools/memory-tree/merge-rows.py` is run with no further
  arguments it exits 2 and the text it prints CARRIES the four placeholders `%O %A %B %P` (see §4 —
  upstream's `__doc__.split("\n\n")[0]` slice prints only the summary sentence and would fail this);
  and when it is run with `PATH` prefixed by a directory holding non-executable `python3`, `python`
  and `py` stubs — the `$C` all-bad fixture of `tools/lib/resolve-python.test.sh:53` — AND
  `GOV_PYTHON` pointing at one of those stubs, it exits 2 and stderr carries
  `GOV_PYTHON is set to '<path>' and did not run`, proving the shim halts on the resolver's return
  value rather than falling through. A bare unusable `GOV_PYTHON` on a host that still has a working
  launcher resolves to that launcher and exits 0 BY DESIGN — `tools/lib/resolve-python.sh:30-37`
  returns on the first candidate that runs, so the named-failure block at `:38-51` is unreachable
  until every candidate is dead. That is not the arm, and a builder who "fixes" it by validating
  `GOV_PYTHON` inside `pyrun.sh` has written a second divergent copy of the resolver's contract.
- **AC3** When `bash tools/lib/resolve-python.test.sh` is run after `pyrun.sh` lands it exits 0, and
  `git grep -l '^# >>> resolve_python' -- '*.sh'` — the parity population that test DERIVES at
  `tools/lib/resolve-python.test.sh:85` — does not list `tools/lib/pyrun.sh`, because the shim SOURCES
  the resolver and carries no marker block. (The test itself prints no population: `copies` is
  consumed by the loop at `:87-93` and its only stdout is the `PASS — resolve-python: <n> assertions
  held` line at `:192`, so the assertion is made against the git command, not against the test's
  output.)
- **AC4** When `bash tools/memory-tree/merge-rows.test.sh` is run, every rc-0 case asserts ID-SET
  EQUALITY between the union of the three inputs (minus ids the honoured deletes removed) and the
  written file, computed by a grammar-independent oracle regex rather than by the driver's own
  grammar (master AC7a) — **and the oracle is proved live in the same run**: on a named fixture
  carrying 3 anchored rows it returns exactly the three `TOOL-zFixture-<n>` ids for n in 1..3,
  and on the real `memory/DECISIONS.md` it returns a set of size > 0. An id-set equality over two
  empty sets is not evidence, and the exposure is concrete: `memory/backlog/DEPL.md` and
  `memory/backlog/KICK.md` carry zero anchors, so two of AC7's four identity arms are legitimately
  empty already. This is the `pop_guard` idiom `tools/lib/resolve-python.test.sh:105-106` and
  `:189-190` apply to their own populations; §5's "every `fail`-shaped assertion carries its own red
  fixture" arms the CONFLICT assertions, not the oracle.
- **AC5** When the same test runs its audit arms, the printed `kept`/`took`/`dropped` counts equal the
  expected triple AND `kept + took` equals the anchored-row count of the file on disk, including the
  discriminating fixture where `kept` is 1 while `%A` carried 3 rows. (Master AC7b.)
- **AC6** When the driver runs in a scratch tree whose `tools/memory-recall/extract.py` is
  syntactically broken, it exits non-zero, `%A` CONTAINS the incoming row's text, and `%A` carries
  `^<<<<<<< ours$`. The same three assertions hold for a scratch tree with no `extract.py` at all and
  for one with no `.memory-tree.conf` above the driver. (Master AC7c, widened to all three
  deferred-resolution failures.)
- **AC7** When each of `memory/DECISIONS.md` and every `memory/backlog/*.md` — enumerated by glob, not
  listed — is merged against itself, the driver exits 0 and `cmp` reports the output byte-identical to
  the input; and a synthetic file with no anchors at all round-trips byte-identically too. The
  identity arm is run on a worktree whose `memory/DECISIONS.md` holds **CRLF**, which is this repo's
  actual checkout state, so all four newline sites in §4 are under the `cmp`. (Master AC7d.)
- **AC8** When a fixture has the same id on both sides with different text, the driver exits 1, the
  file holds BOTH texts inside `<<<<<<< ours` / `>>>>>>> theirs` markers, and no marker line carries
  an absolute filesystem path. When ours edits a row theirs deleted, and again when ours deleted a row
  theirs edited, the driver exits 1 and the surviving EDIT is present in the output.
- **AC9** When a throwaway repo is built carrying `.memory-tree.conf`, `tools/memory-tree/` (the
  driver), `tools/memory-recall/` (the grammar) and `tools/lib/` (`pyrun.sh` plus the
  `resolve-python.sh` it sources) — all three under the `tools/` prefix, because the configured
  command's paths are RELATIVE — plus the two `.gitattributes` lines and `merge.rows.driver`, and two
  branches each append a distinct row to `memory/backlog/TOOL.md`, `git merge` auto-resolves: exit 0,
  both rows present, no duplicate id. Three directories, not two: the configured command is
  `bash tools/lib/pyrun.sh tools/memory-tree/merge-rows.py %O %A %B %P`, so a fixture carrying only
  the two kits cannot start the driver at all. (Master AC8.)
- **AC10** When `git config --get merge.rows.driver` is run on a wired node it returns
  `bash tools/lib/pyrun.sh tools/memory-tree/merge-rows.py %O %A %B %P`; when it is unset,
  `bash tools/check-wiring.sh --check` prints `UNWIRED  merge` and exits 1; when `--fix` is then run
  the config is set and a re-check exits 0; and when it is set to a different value, `--fix` leaves
  that value untouched. (Master AC9, plus the never-clobber half.)
- **AC11** When `python tools/drift-audit/drift_report.py --check` is run after this unit it exits 0
  and prints nothing on stderr — `handkept_inventories_disagreeing_with_source` stays at its pin of 7,
  which requires the `AGENTS.md` bullet to cite `tools/memory-tree/merge-rows.test.sh` by argv path,
  AND `non_terminal_specs_cited_by_product_source` stays at 2, which requires
  `git grep -l -F 'TOOL-aMendedLedger-' -- tools skills .claude 'parallel-coding-governance*.md' WIRE-INTO-PROJECT.md`
  to return nothing.
- **AC12** When `python tools/codebase-map/test_codebase_map.py` is run after this unit it exits 0
  with the new leg name claimed by `memory/map/features/memory-tree-merge-driver.md` and no new key in
  `memory/map/baseline.toml` — including `test_dossier_prose_headings_pinned` and
  `test_dossier_affordance_present_or_graced` passing over the new dossier, and
  `test_generated_artifacts_are_fresh` byte-comparing a `memory/map/generated/` regenerated in THIS
  commit.
- **AC13** When `bash tools/run-gates.sh` is run on this unit's commit it is green over 39 legs.
  (Master AC11.)

## 7. Gates

Existing legs that must stay green: `bash tools/run-gates.sh` in full. Load-bearing for this unit —
`python resolver (behaviour + inline parity + idiom ban)`, `check-wiring self-test`, `run-gates
canary`, `codebase-map coverage + freshness`, `codebase-map kit selftest`, `drift-audit records`,
`kickoff-manifest ratchet` + its self-test, `memory hygiene`, `harness arms`.

New leg: `row-keyed merge driver replay` → `["bash", "tools/memory-tree/merge-rows.test.sh"]` in
`tools/gate-legs.json`, with no `guard` key. `tools/run-gates.test.sh:15-27` requires a non-empty
name, `argv` length ≥ 2 and `argv[0]` in `{bash, python, python3, node}`; `:33-43` forbids the leg's
script path appearing literally in `tools/run-gates.sh`.

The master's three couplings, answered for this unit:

1. **`check-memory-hygiene.sh` / `KIT_MEMORY_TREE_VERSION`** — not triggered. U5 does not touch that
   file, and `tools/memory-tree/check-verdict-epoch.sh:51-52` scans only the engine plus
   `gen_build_index.py`, `corpus_ids.py` and `gotchas.py`. `merge-rows.py` living in the same
   directory does not enlist it. **The builder must not "helpfully" bump the constant**: a bump with
   no engine change is a false verdict epoch.
2. **The kickoff manifest's seven watched pathspecs** — U5 stages one, `tools/gate-legs.json`. The
   pre-commit runs `manifest-check.sh --staged`, whose C5s leg is
   `skills/session-kickoff/manifest-check.sh:204-219` (the file is 223 lines, so rev-1's `:213-228`
   ran past EOF) and accepts only a stamp bundled in THAT SAME commit. So this commit re-verifies the
   manifest's §B claims and rewrites `.claude/SESSION-KICKOFF.md:5` as `<ISO datetime from date> @ <40-hex sha>`,
   where the sha is `git merge-base origin/main HEAD` on a branch (HEAD on the default branch) per
   `STAMP_SHA_RULE` at `:154`. C3 additionally requires that sha to be a real ancestor of HEAD.
3. **A new gate leg pushes `handkept_inventories_disagreeing_with_source` up by one** unless
   `AGENTS.md`'s gate-suite section names it. `tools/drift-audit/drift_signals.py:87-95` scopes the
   search to the `## The gate suite` section and matches on the argv path substring, so the bullet
   must contain the literal `tools/memory-tree/merge-rows.test.sh` and must sit before the next `##`.

Two more couplings the master does not state, each of which a builder otherwise discovers as a red bar:

4. **The new leg NAME is a `gate-legs` inventory key for the codebase-map gate**, and
   `merge-rows.py`'s symbols enter the `kit-py` layer.
   `tools/codebase-map/test_codebase_map.py:45-56` reds on an unclaimed key and `:94-112`
   byte-compares `memory/map/generated/`. Hence S7 and Rollout step 4.

5. **No product-source file may cite this build's spec id while the spec is non-terminal.**
   `tools/drift-audit/drift_signals.py:20-28` scopes `PRODUCT_GLOBS` to `tools`, `skills`, `.claude`,
   the three `parallel-coding-governance*.md` files and `WIRE-INTO-PROJECT.md`; `signal_spec_status`
   (`tools/drift-audit/drift_report.py:235-271`) flags every spec whose Status is non-terminal and
   whose own H1 id (`_OWN_ID`, `:231`) `git grep`s inside that scope. Measured at HEAD: `2 of 15`,
   pin `2` (`drift_signals.py:128`) — the signal is AT its pin, so ONE citation reds the
   `drift-audit records` leg and takes AC11 and AC13 with it. The default here is dangerous: the
   upstream file being ported opens its docstring with `(ARCH-dQuarriedLedger-1 U9)` at
   `C:/projects/incms/main/scripts/merge-rows.py:2`, and this repo's own kit sources habitually cite
   their originating spec (`tools/run-gates.sh:24` → `TOOL-aLeasedGauntlet-1 S3`;
   `tools/check-wiring.sh:3`). That provenance line MUST NOT be re-pointed at this build's id in
   `tools/memory-tree/merge-rows.py`, `tools/memory-tree/merge-rows.test.sh`, `tools/lib/pyrun.sh`,
   the `check_merge_rows` comment, the `AGENTS.md` bullet or the new dossier's prose. **Cite the
   build by SLUG — `aMendedLedger U5` — or by the upstream id only.** (`drift_report.py:228-231`
   records why keying on the slug instead of the id was rejected upstream: it over-flagged 107/126,
   because every id of a build shares the slug. The seq is the discriminator — which is exactly why
   the id is the thing that must not appear in a product-glob file.)

Run `python tools/memory-tree/gotchas.py --for-diff 663ca427..HEAD` before the review, not after.

## 8. Open questions

none — the two choices this unit could have forked on are ratified in §4 Alternatives rejected: the
new leg is claimed by a NEW codebase-map dossier rather than by the map kit's own or by
`baseline.toml`, and `check-wiring.sh` sets `merge.rows.driver` under `--session` as well as `--fix`,
matching `check_hooks` rather than the byte-rewriting `eol` arm.

## 9. Revision log

- rev-1 · 2026-08-09 · initial draft, written to master `TOOL-aMendedLedger-1` rev-3 §4 Data model
  and Rollout row U5. The upstream implementation at `C:/projects/incms/main/scripts/merge-rows.py`
  and its fixtures at `scripts/merge-rows.test.sh` were read in full and ported; the grammar import
  was re-pointed at this repo's `tools/memory-recall/extract.py` `grammar_for(root)` +
  `anchor_at(line, g)`, the fixture id family was corrected from `ABL-` to `TOOL-` because the
  grammar is family-gated here, and upstream's `uv`-dependent parse arm was replaced. Four
  constraints were verified against source and are stated where a builder will hit them: the
  inline-copy parity gate binds only marker-carrying files while the two invocation bans bind every
  tracked `*.sh`; the verdict-epoch gate does not scan the new file; the check-arms population does
  not gain it; and the codebase-map coverage gate does.
- rev-2 · 2026-08-09 · folded the consolidated sub-spec review (X1 + D5-1…D5-11) and re-aligned on
  master rev-4, where all six forks now read RESOLVED; U5 depends on none of them, and §3's
  hygiene-engine non-goal now records that F6 put the `:346` `ex7` rewrite into U3. **X1**: the H1 was
  `# TOOL-aMendedLedger-1 U5 — …`, which `gen_build_index.py:54`'s `H1_RE` cannot parse (the id must
  be followed immediately by ` — `), and which put all six specs of this build on one id — the exact
  shape `drift_report.py:228-231` records as over-flagging 107/126 upstream. Now
  `# TOOL-aMendedLedger-5 — U5: …`, per-file seq, the `aFoldedQuarry` precedent. **Three blocking
  fixes.** (1) A fifth §7 coupling and an extended AC11: `tools/` is `PRODUCT_GLOBS[0]`, the
  spec-citation signal measures `2 of 15` against a pin of `2`, and the ported upstream docstring's
  `(ARCH-dQuarriedLedger-1 U9)` provenance line is the default path into that trap — the build is
  cited by SLUG in every product-source file. (2) AC2's `GOV_PYTHON` arm asserted an observation the
  shipped resolver cannot produce: `resolve-python.sh:30-37` returns on the first candidate that
  RUNS, so an unusable `GOV_PYTHON` falls through to a working `python3` and the named-failure block
  at `:38-51` is unreachable — the arm now shadows all three launcher names first, as
  `resolve-python.test.sh:53, :63-66` does. (3) §4 stated only the WRITE half of the newline
  contract; all four sites are now named, and site 3 is recorded as a DIVERGENCE from upstream, which
  passes `text=True` at `merge-rows.py:147` and would return a CRLF region as LF on this repo's
  CRLF worktrees. **Eight non-blocking.** The `memory/DECISIONS.md` corpus measurement was wrong
  (`:1-6` "title, bolded rotation note, routing prose" → `:1` title, `:3-4` blockquote routing,
  `:6` a section heading, first anchor `:8`) and the region rule is now declared to win at the block
  boundary; AC3 asserted a population `resolve-python.test.sh` never prints; the kit-directory bullet
  cited `check-wiring.sh:122`, which spells the pair adopter-first, so the order is now taken from
  `:127`; `check_merge_rows`'s declared-attribute predicate was circular and is now one
  `git ls-files | git check-attr --stdin merge` call; AC4 gained a live-oracle proof; S7 gained the
  three codebase-map dossier requirements past "claim the leg"; AC2 gained the usage-text
  requirement upstream's `__doc__.split("\n\n")[0]` slice does not meet; and AC9 gained the third
  copied directory `tools/lib/`, without which the configured command cannot start. Two citations
  corrected beyond the review: the C5s leg is `manifest-check.sh:204-219`, not `:213-228` (the file
  is 223 lines), and the verdict-epoch scan is declared at `check-verdict-epoch.sh:51-52`, not
  `:50-52` (`:50` is a comment). Every file:line in this spec was re-opened at HEAD.

## 10. Reuse audit

`reuse_lookup.py` was run at the workaround invocation the conf prescribes
(`CODEBASE_MAP_ROOT="$(git rev-parse --show-toplevel)" python tools/codebase-map/reuse_lookup.py …`)
over a corpus of 244 symbols and 70 inventory keys. For "three-way merge of id-anchored index rows
keyed by record id" it ranks `records` (`tools/memory-tree/gotchas.py`, fan-in 6, SEAM) and `merge`
(`tools/settings-merge.py`, fan-in 5, SEAM) first, and neither fits: `gotchas.records` parses front
matter, and `settings-merge.merge` is a recursive dict union for JSON, not a three-way text merge
with conflict markers. It also surfaces `extract_records` and `Grammar` in
`tools/memory-recall/extract.py`, which is the seam this unit does wire through.

For "resolve a python launcher and exec a script with it" the top hit is `recall_conf.resolve`
(fan-in 17, SEAM) — the conf resolver, not a launcher resolver — and the only relevant result is the
`python resolver (behaviour + inline parity + idiom ban)` inventory key, i.e. the gate over
`tools/lib/resolve-python.sh`. That is the correct seam and it is a SHELL function, which the symbol
index cannot rank: `.codebase-map.conf:38` declares `RECALL_DARK_LAYERS="bash"`, so this repo's
product layer is invisible to the ranker by design and the inventory hit is the only signal.

The reuse decision: **no seam fits the merge itself; three existing seams are reused and none is
re-implemented.** `tools/memory-recall/extract.py` supplies the id grammar through `grammar_for(root)`
and the anchor predicate through `anchor_at(line, g)`. `tools/lib/resolve-python.sh` supplies the
launcher through `pyrun.sh`, which sources it rather than re-solving or inlining it.
`tools/check-wiring.sh`'s `first_of` supplies the two-layout path resolution the driver needs to find
its sibling kit. The new dossier records the driver's own forward affordance so the next unit does
not re-derive the region split.
