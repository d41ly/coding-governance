# TOOL-dRedressedBar-20 — govkit's carrier writer counts an entry's version pattern only inside that entry's own basis, so a mint never writes another kit's file

**Status:** CLOSED · rev-2 · 2026-10-14 · node d · Tier-2 · base ebce889c · streams tooling · order 4 · ratified 2026-10-14

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-14-prompt-TOOL-dRedressedBar-20-1-spec-writer.md](../prompts/2026-10-14-prompt-TOOL-dRedressedBar-20-1-spec-writer.md) | journal | — |
| [2026-10-14-prompt-TOOL-dRedressedBar-20-2-revision.md](../prompts/2026-10-14-prompt-TOOL-dRedressedBar-20-2-revision.md) | research | TOOL-dRedressedBar-7 |
| [2026-10-14-prompt-TOOL-dRedressedBar-20-3-spec-writer.md](../prompts/2026-10-14-prompt-TOOL-dRedressedBar-20-3-spec-writer.md) | journal | — |
| [2026-10-14-prompt-TOOL-dRedressedBar-20-brief.md](../prompts/2026-10-14-prompt-TOOL-dRedressedBar-20-brief.md) | research | — |
| [2026-10-15-review-TOOL-dRedressedBar-1-20-diff-review-round1.md](../reviews/2026-10-15-review-TOOL-dRedressedBar-1-20-diff-review-round1.md) | diff-review | TOOL-dRedressedBar-1 TOOL-dRedressedBar-2 TOOL-dRedressedBar-3 TOOL-dRedressedBar-4 TOOL-dRedressedBar-5 TOOL-dRedressedBar-6 TOOL-dRedressedBar-7 TOOL-dRedressedBar-8 TOOL-dRedressedBar-9 TOOL-dRedressedBar-10 TOOL-dRedressedBar-11 TOOL-dRedressedBar-12 TOOL-dRedressedBar-13 TOOL-dRedressedBar-14 TOOL-dRedressedBar-15 TOOL-dRedressedBar-16 TOOL-dRedressedBar-17 TOOL-dRedressedBar-18 TOOL-dRedressedBar-19 |

<!-- /gen:spec-records -->

## 1. Goal

`write_version_carriers` treats a line as a version carrier when it matches any registry entry's
`version_from` pattern. So `playbook`'s `governance-template: v` makes a selftest fixture in
playbook-render's engine a carrier of playbook-render's number. Every mint and every
`selfcheck --fix` rewrites that fixture, moving playbook-render's shipped bytes without a bump. This
unit scopes each pattern to the files of its own entry's basis, which closes the class for every
pattern and keeps the four cross-entry carriers that are real. It then restores the one fixture the
class already rewrote, `tools/playbook/render_playbook.py:1397`, to `v3.5`. That restore moves
playbook-render's bytes, and unit 7's mint dates the move.

Tier-2: it narrows a write path that two verbs share, `mint` and `selfcheck --fix`, and the version
carrier set is a contract those verbs share with the `kit version markers` leg.

## 2. Scope (IN)

- **S1** — THE SCOPE. While `write_version_carriers` (`tools/govkit/govkit.py:798`) walks a file, the
  patterns that make a line a carrier are the patterns of those entries whose basis holds that file.
  The basis is the one `derive_marker_basis` (`:764`) returns, the same argument the writer already
  takes. The walking entry is always among them. A match of entry B's pattern in a file outside B's
  basis is not a carrier, so neither its number nor its same-line aliases are written. The ownership
  clause at `:866-867` is unchanged. Observed by AC1, AC2 and AC3.
- **S2** — THE DOCSTRING. The writer's docstring states the scope and the defect that motivated it,
  in place of the sentence at `:804` that says a line matching ANY entry's pattern counts. Observed
  by AC5.
- **S3** — THE ARM. `check_fix_carriers` (`tools/govkit/selftest.py:1119`) is restaged so it carries
  both halves of the rule. A line matching another entry's pattern in a file outside that entry's
  basis stays as it is. A line matching another entry's pattern in a file both entries' bases hold
  moves. Every assertion it makes today keeps its subject. Observed by AC4, through the `New arm:`
  line in §7.
- **S4** — THE READER AUDIT. Every other reader of an entry's `version_from` pattern reads it only in
  that entry's own source file, or reads no pattern, so none changes. NOT OBSERVED — a read of
  existing code that moves no byte; §4 cites each reader by line.
- **S5** — THE CODE COMMIT MOVES NO KIT. The code commit, which carries S1 to S3, writes
  `tools/govkit/govkit.py` and `tools/govkit/selftest.py`. Both sit under the `{prefix}/govkit`
  registry exemption (`tools/govkit/registry.toml:295-297`), and neither is in any entry's shipped
  set. No function is added or renamed, so `memory/map/generated/symbols.json` is not regenerated.
  Observed by AC6.
- **S6** — THE RESTORE. A second commit, after the code commit, writes `v3.5` back over `v1.28` on
  `tools/playbook/render_playbook.py:1397`, the fixture line `v3 = ('<!-- governance-template: v...`.
  It changes that one line and no other file. The line's arm keeps passing, because the engine reads
  any major below `TEMPLATE_MAJOR` (4, `:340`) as an older template (`:1001`), and 3 is below 4 just
  as 1 was. The restore moves playbook-render's shipped bytes, so the epoch over `ebce889c7` reads
  playbook-render FAILED at that commit. Unit 20 bumps nothing. Unit 7's mint bumps playbook-render
  from 1.28 to 1.29 (§3 Edges). Observed by AC7 and AC8.

## 3. Non-goals (OUT)

- No descriptor pattern changes. Anchoring `playbook`'s `governance-template: v` would edit
  `tools/govkit/entries/playbook.kit.toml`, which `govkit.py shipped --epoch` lists in
  playbook-render's set, and it fixes one instance of the class.
- No change to the ownership clause, to `derive_marker_basis`, or to which files a basis holds.
- No change to `cmd_mint`, `derive_epoch_state`, selfcheck checks 5 and 5c, or
  `tools/check-kit-versions.sh`. §4's reader audit says why each already agrees.
- No edit to any other fixture line. `render_playbook.py:1646` still reads `v3.5` at the base,
  because the defect writes it only when the writer runs, and S1 stops that.
- No new gate over the tree's foreign-pattern lines. Once the writer cannot write one, such a line is
  inert, and S3's arm guards the writer.
- No kit version bump, no `govkit.py mint` over the worktree (AC3's mint runs in a scratch clone),
  and no regeneration of the symbol index. S6 adds playbook-render to the kits unit 7 mints, and
  unit 7 makes that bump.
- No merge to local main and no push.

### Edges

- **hands-off** `TOOL-dRedressedBar-7` — its S3 mint over `ebce889c7` runs over this unit's writer
  and this unit's restore. It moves five kits: the four its table named before, and playbook-render
  from 1.28 to 1.29, for the bytes S6 moves. In `render_playbook.py` it writes only the version line
  `:1839` and the marker on it. AC3 runs the mint over the code commit in a scratch clone, and AC7
  shows that the writer leaves the restored line alone, so unit 7 meets no divergence of this class.

## 4. Design

Every citation below was read at `9d0ad1c0a`. Its `tools/govkit/govkit.py` and `tools/playbook/`
bytes equal `ebce889c7`'s (`git diff --stat ebce889c7 -- tools/govkit/govkit.py tools/playbook/` is
empty), so they hold at the base too.

### The defect, reproduced

`write_version_carriers` compiles one carrier regex per entry that declares a pattern
(`tools/govkit/govkit.py:817-825`). It then tests every line of every file in the walking entry's
basis against all of them (`:868`). Whose number lands on a matched line is the ownership clause's
choice (`:866-867`). A line belongs to the walking entry when it carries that entry's marker, or when
the file carries that entry's marker and no other entry's.

`tools/playbook/render_playbook.py` is in playbook-render's basis and carries only playbook-render's
marker (`:1839`). Line 1646 is `older_tpl = '<!-- governance-template: v3.5 -->...'`, which
`playbook`'s pattern (`tools/govkit/entries/playbook.kit.toml:6`) matches. So the writer owns it for
playbook-render and writes `1.28` over `3.5`.

It needs no bump to fire. On a `git clone --local` of `9d0ad1c0a`, the §4 `writer` command alone
printed `[('tools/playbook/render_playbook.py', 'playbook-render', 'playbook-render', '3.5', '1.28')]`
and changed line 1646 only (PINNED, 2026-10-14). Unit 7's builder saw the same line move inside
`govkit.py mint --base ebce889c7`, beside the four bumps.

It has fired before. Line 1397's fixture `v3 = ('<!-- governance-template: v...` was written as
`v3.5` by `166bfcd78`. It read `v1.25` at `dac07b824`, `v1.26` at `acf9d3152` and `v1.27` at
`4606faa49`, each a landing merge, and `ed1e9db3c` minted it to `v1.28`. It now carries
playbook-render's version rather than a v3 template's. S6 restores it (F1, resolved (b)).

### The class, measured over the real registry

The predicate: for every entry A with a pattern, every file in A's basis, every line matching another
entry B's pattern then an optional quote and a number. It reports the writer's ownership verdict for
A and whether B's own basis holds the file. It was run read-only through govkit's own functions on
2026-10-14 at `9d0ad1c0a`.

```python
descs = gk.read_descriptors(root, gk.load_registry(root), gk.Report())
basis = gk.derive_marker_basis(root, descs)
rxs = {b: re.compile("(?:" + d["version_from"]["pattern"] + r")['\"]?([0-9]+(?:\.[0-9]+)*)")
       for b, (d, _) in descs.items()
       if (d.get("version_from") or {}).get("pattern") and "none" not in d["version_from"]}
for a in rxs:                                  # A walks its basis, as the writer does
    for f in basis[a]:                         # every line, every OTHER entry's pattern
        ...                                    # print f:n, A, B, value, owned?, f in basis[B]?
```

| File:line | Writer | Pattern of | Owned | In the pattern owner's basis |
|---|---|---|---|---|
| `tools/workflows/drift-audit-code.js:3` | drift-audit | review-harness | yes | yes |
| `tools/workflows/drift-audit-code.template.js:3` | drift-audit | review-harness | yes | yes |
| `tools/workflows/drift-audit-state.js:3` | drift-audit | review-harness | yes | yes |
| `tools/workflows/drift-audit-state.template.js:3` | drift-audit | review-harness | yes | yes |
| `tools/playbook/render_playbook.py:1397` | playbook-render | playbook | yes | no |
| `tools/playbook/render_playbook.py:1646` | playbook-render | playbook | yes | no |

Six hits (PINNED, 2026-10-14; AC1 re-derives the writer's half). The four drift-audit harnesses are
real carriers. drift-audit reaches them through its declared `marker_carriers`
(`tools/drift-audit/kit.toml:13`), and review-harness's own `**` claims them. The two
`render_playbook.py` lines are the defect. The column that separates them is the last one, and the
ownership column cannot: both shapes are a file carrying one marker and another entry's pattern.

The predicate's own-pattern half was run too. Twelve lines match the walking entry's own pattern
outside its constant's line, and all are real carriers or correctly unowned: the three
`KIT_UNATTENDED_VERSION` copies, `tools/workflows/tier2-review.js:3`, and eight review-harness lines
the writer leaves unowned, in files that carry no review-harness marker. That matches TOOL-aMendedFleet-64's measured inventory, and
S1 does not touch it, because the walking entry's basis always holds the file it walks.

### The mechanism

`carrier_rxs` becomes a dict keyed by entry id, and each file walk filters it by basis membership.
The ownership clause and everything after `hits` stay as they are.

```python
    carrier_rxs: dict[str, re.Pattern] = {}   # entry id -> its pattern, an optional quote, a number
    for rid, (d, _dp) in descs.items():
        vf = d.get("version_from") or {}
        if "none" in vf or not vf.get("pattern"):
            continue
        try:
            carrier_rxs[rid] = re.compile("(?:" + vf["pattern"] + r")['\"]?([0-9]+(?:\.[0-9]+)*)")
        except re.error:
            continue
    ...
            # inside `for f in sorted(basis.get(eid, ())):`, once the text is read
            file_rxs = [rx for rid, rx in carrier_rxs.items() if f in basis.get(rid, ())]
    ...
                hits = [h for h in (rx.search(ln) for rx in file_rxs) if h] if n != const_at else []
```

`rid` is unbound anywhere else in the function, so it collides with no local
(`a-new-local-collides-in-a-long-function`). The dict keeps the registry's insertion order, which
the leftmost-match tie-break at `:869` reads exactly as it read the list.

A trial of exactly this edit in a scratch clone of `9d0ad1c0a`, 2026-10-14: the `writer` command
printed `[]`. With `KIT_DRIFT_AUDIT_VERSION` edited to `9.99`, it printed fourteen rewrites, two in
each of the four harnesses (the `version:` field and the marker). Both are PINNED observations of a
trial, and AC1 and AC2 re-observe them over the built code.

### Why the scope is the basis

The basis is the population `derive_marker_basis` exists to be. Its docstring
(`tools/govkit/govkit.py:765-772`) says the writer and check 5c read one set so they cannot
disagree. Scoping by `entry_members` instead would build a second population inside the writer.
That is the `two-answers-to-one-question` class. On today's tree the two give the same answer,
because all four harnesses are review-harness members.

### The other readers of a version pattern

| Reader | Where | What it reads | Why it already agrees |
|---|---|---|---|
| `entry_version` | `tools/govkit/govkit.py:529-549` | own pattern, own `version_from` file | it opens one file, the entry's own |
| `resolve_entry_version_at` | `:693-715` | own pattern, own source blob at a commit | same |
| `read_target_kit_version` | `:718-744` | own pattern, the target's copy of own source | same |
| `derive_version_value` | `:12949-12957` | own pattern, on the line its caller hands it | every caller hands the entry's own constant line |
| `derive_epoch_state` | `:12976-13031` | `-G` with own pattern, pathspec `vsrc` (`:13011-13018`) | the pathspec is own source |
| `cmd_mint`'s own write | `:13165-13180` | first own-pattern line of own source | own file |
| selfcheck check 5 | `:2059-2085` | own pattern, own file, exactly one line | own file |
| selfcheck check 5c | `:2162-2232` | `gov:kit <eid>@` markers only | reads no pattern |
| `tools/check-kit-versions.sh` | `:148`, `:349-360` | declared rows with their own regexes, no registry | grades the drift-audit harness fields against drift-audit's constant, the assignment S1 keeps |
| `tools/memory-tree/check-verdict-epoch.sh` | `:281` | its own engine's `KIT_MEMORY_TREE_VERSION` | own constant |
| `tools/govkit/matrix.py` | `:269` | `version_from.file` only | reads no pattern |

The writer has two callers, `selfcheck --fix` (`tools/govkit/govkit.py:1779`) and `cmd_mint`
(`:13194`). Both pass `derive_marker_basis(root, descs)`, so S1 reaches both with no caller change.
No `kit version markers` row names a `render_playbook.py` line, which is why no leg but the epoch
ever saw the rewrite.

### What it does not check

- A foreign pattern matching inside a file that both entries' bases hold is still a carrier, and it
  takes the marker owner's number. A fixture line of that shape would still be written. The class
  predicate found none on 2026-10-14.
- An entry's own pattern matching a fixture line inside its own basis is still a carrier. The
  own-pattern half found no such line.
- The writer prints nothing about a foreign line it does not treat as a carrier, as before.
- The arm's fixture spells `version: ` for its second entry, not `governance-template: v`. The
  shipped pattern is exercised by AC1 and AC3 over the real registry, which is what
  `staged-break-substitutes-a-synthetic-value` asks for.
- Of the two lines the class predicate found in a file outside the pattern owner's basis, only
  `:1397` had already been rewritten, and S6 restores it. A past rewrite that left a line no foreign
  pattern still matches would be outside the predicate's reach. None is known.

### The arm

`check_fix_carriers` keeps every file it has. It gains two, and one descriptor key:

| Fixture path | Bytes | Role after this unit |
|---|---|---|
| `vk/harness.js` (kept) | `  version: '1.0',\n// gov:kit vk@1.0\n` | NEW NEGATIVE: wk's pattern in a file outside wk's basis. The marker moves to 1.1, the field stays 1.0. The shape of `render_playbook.py:1646`. |
| `wk/harness.js` (new) | the same bytes | POSITIVE: in wk's basis by home, in vk's by `marker_carriers`. Both numbers move to 1.1. The shape of `drift-audit-code.js:3`. |
| `<gk.GOVKIT_DIR.name>/<gk.REGISTRY_NAME>` (new) | empty | the stub `derive_tool_root` (`tools/govkit/govkit.py:154-174`) globs for, so the `{prefix}` token resolves to the fixture root |
| vk's descriptor | gains `"marker_carriers": ["{prefix}/wk/harness.js"]` | what drift-audit declares for its harnesses |

The stub's path is spelled through the engine's own two names, the ones `derive_tool_root` reads, not
retyped. The assertions after this unit:

- `[aMF-64 S2] another entry's pattern moves in a file carrying only this entry's marker` keeps its
  subject on `wk/harness.js`, reading `b"  version: '1.1',\n// gov:kit vk@1.1\n"`. Its label gains
  `that both entries' bases hold` so the label says what is graded.
- `[dRB-20] another entry's pattern in a file outside that entry's basis is not a carrier` is new.
  It asserts `vk/harness.js` reads `b"  version: '1.0',\n// gov:kit vk@1.1\n"`.
- The count assertion reads `len(first) == 8`. That is seven before, minus the one field
  `vk/harness.js` no longer moves, plus the two `wk/harness.js` rewrites.
- Every other assertion is unchanged, the idempotent second run included.

A trial of this fixture on 2026-10-14 against S1's trial edit returned eight rewrites with both
harness files as above. Against the base writer it returned nine, with `vk/harness.js`'s field at 1.1,
so the new assertion and the count both fail there (PINNED observations of a trial).

### The restore

The fixture at `tools/playbook/render_playbook.py:1397` opens the `v3` string. The arm at
`:1397-1419` renders that string twice, once with every block kept and once with `node-table`
dropped, and labels each case `a v3.x template renders under the shipped declarations (...) and
notes a reseed`. The comment at `:1392-1395` says the fixture is a seeded v3.x template. S6 writes
`v3.5` back over `v1.28`, the value `166bfcd78` wrote. No other byte moves.

The marker's number reaches the arm in one place. `render` reads it with `TEMPLATE_MARKER_RE`
(`:341`) and sets `current` when its major is at least `TEMPLATE_MAJOR` (`:1000-1001`). A current
template carrying a legacy fence is refused (`:1006-1009`), and a template that is not current gets
the reseed note (`:1023-1026`). The fixture carries the legacy `when:node-table` fence, so a major
of 1 and a major of 3 take the same branch. The §4 `v3render` command drives the fixture through
`render` the way the arm does. On 2026-10-14 at `9d0ad1c0a` it printed
`<!-- governance-template: v1.28 --> True True True`. With the fixture's marker set to `v3.5` in a
copy of the source it printed the same three `True`. With the marker set to `v4.0` the render
refused, naming the `when:node-table` fence (PINNED observations of a trial). So the probe can go
red, and the restored value keeps it green.

The restore is its own commit, after the code commit, for three reasons:

- Before S1, any writer run rewrites the line again, so the restore has to come after S1 to stay put.
- AC1's red half reads the code commit's first parent, where only line 1646 moves. AC6 reads the
  code commit's two-file diff. Both hold as written.
- The commit that moves playbook-render's shipped bytes is one line in one file, and its subject
  can say so.

`render_playbook.py` is in playbook-render's epoch set through its `**` rule
(`tools/playbook/kit.toml:18-21`). `python tools/govkit/govkit.py shipped --epoch` lists it, beside
six other paths of that entry (2026-10-14). That kit's bytes are unchanged over `ebce889c7..9d0ad1c0a`, and its value is
`1.28` at both ends (`:1839`). So the restore commit is the move that unit 7's mint dates. AC7
observes the FAILED verdict it leaves for that mint.

### Observation commands

Run from the worktree root. `<sha>` is the commit under observation.

```bash
# clone — a scratch copy of one commit, under a short root
git clone -q --local . "$TEMP/r20" && git -C "$TEMP/r20" checkout -q <sha>
# writer — the carrier writer over the real registry, run from inside the clone
python -B -c "import sys,pathlib; sys.path.insert(0,'tools/govkit'); import govkit as g; r=pathlib.Path('.').resolve(); d=g.read_descriptors(r,g.load_registry(r),g.Report()); print(g.write_version_carriers(r,d,g.derive_marker_basis(r,d)))"
# arm — the one selftest function S3 restages, alone, from the worktree root
python -B -c "import sys,pathlib,tempfile; sys.path.insert(0,'tools/govkit'); import selftest as s; s.check_fix_carriers(pathlib.Path(tempfile.mkdtemp())); sys.exit(1 if s.FAILURES else 0)"
# v3render — S6's fixture through the engine's own render, as its arm drives it, from the worktree root
python -B - <<'PY'
import ast, pathlib, sys, tempfile
sys.path.insert(0, 'tools/playbook'); import render_playbook as r
e = pathlib.Path('tools/playbook').resolve()
v3 = next(ast.literal_eval(n.value) for n in ast.walk(ast.parse((e / 'render_playbook.py').read_text(encoding='utf-8')))
          if isinstance(n, ast.Assign) and getattr(n.targets[0], 'id', '') == 'v3')
t = pathlib.Path(tempfile.mkdtemp()); (t / '.governance').mkdir(); (t / 'TPL.md').write_text(v3, encoding='utf-8')
(t / '.governance' / 'deploy.toml').write_text('kits = ["lexicon"]\n\n[answers]\nplaybook_path = "TPL.md"\n'
    'machine_a = "u"\nprimary_tree_a = "ptree"\nworktree_root_a = "wroot"\nvariances_a = "none"\n', encoding='utf-8')
b, n = r.render(e, e.parent.parent, t)
print(v3.splitlines()[0], '`ptree`' in b, 'SSRF' in b, any('reseed' in x for x in n))
PY
```

The `arm` command calls one function and no other arm, so it is the fixture probe and not the suite.
The `v3render` command calls `render` once over the fixture string it reads from the source, and it
runs no arm. Its three booleans are the arm's own conditions for the every-block-kept case: the node
row survives, the `security-outbound` body survives, and the reseed note is present. The answers are
spelled without a path, unlike the arm's `C:/p/x`, because a drive-path guard on node d refused the
inline script that embedded one (2026-10-14). A refusal escapes as a traceback and a non-zero exit.
Delete `tools/govkit/__pycache__` before each `arm` run, because an edit and a re-run inside one second
can execute the previous bytecode (`staged-break-runs-stale-bytecode`).

### Rollout

1. Reproduce. Clone the pass's starting commit and run `writer`, recording AC1's RED half.
2. Write S3's arm with `govkit.py` untouched. Run `arm` and record its RED: the new label and the
   count fail.
3. Write S1 and S2. Run `arm` again for GREEN, then AC1, AC2, AC3 and AC5 over a clone of the
   working commit.
4. Commit the two files with the unit id in the subject. The commit body states each file's net line
   delta. Units 10 to 19 cite line numbers in both files, and the delta is what their builders
   re-ground by. Keep `govkit.py`'s delta at zero where the docstring allows.
5. Run AC6 over the commit.
6. S6. Write `v3.5` over `v1.28` on `render_playbook.py:1397` and nothing else. Run `v3render`, then
   commit the one file with the unit id in the subject. The commit body says that the restore moves
   playbook-render's shipped bytes and that unit 7's mint bumps it to 1.29. Run AC7 and AC8 over this
   restore commit. Run no mint and no `selfcheck --fix` over the worktree.

### Inventory

No identifier is minted. `carrier_rxs` changes type within its function, and `file_rxs` and `rid`
are new locals of `write_version_carriers`. The new fixture label carries the `[dRB-<n>]` prefix
that unit 9's arms already use in `tools/govkit/selftest.py`.

### Files touched (estimate)

- `tools/govkit/govkit.py`
- `tools/govkit/selftest.py`
- `tools/playbook/render_playbook.py` (S6, the restore commit)

### Alternatives rejected

- **Anchor `playbook`'s pattern**, for example `^<!-- governance-template: v`. It edits a file in
  playbook-render's shipped set, which owes a bump. It fixes one pattern, and `version: ` and
  `KIT_AGENT_CAP_VERSION = ` stay unanchored for the next instance.
- **Tighten the ownership clause.** `render_playbook.py:1646` and `drift-audit-code.js:3` have the
  same ownership shape: one marker in the file and another entry's pattern on the line. No ownership
  rule separates them. Only the pattern owner's basis does.
- **Count only the walking entry's own pattern.** The four drift-audit harness fields stop moving.
  `tools/check-kit-versions.sh:349-360` then reds at the next drift-audit bump, and
  TOOL-aMendedFleet-64's AC2 named this exact break as its red.
- **Scope by `entry_members`.** A second population inside the writer; see "Why the scope is the
  basis".
- **Skip lines inside test fixtures or string literals.** That names an instance by its syntax, and a
  real carrier is often a string literal, such as a harness `version:` field.
- **Leave line 1397 as it reads (F1 (a)).** The owner chose (b) on 2026-10-14.
- **Mint playbook-render inside this unit, after the restore.** That is the bump F1 (b) first
  described. The revision brief gives the bump to unit 7's one mint over `ebce889c7`, which already
  reads every move in the build. A mint here would also run playbook-render's `AGENTS.md` render, and
  unit 7's mint runs that same render again.

## 5. Production-readiness checklist

- security — Narrows an existing write path. The writer still writes only files in a basis, and only
  the number after a declared pattern or marker. No input, argv or egress is added.
- perf / scale — One set-membership test per entry for each file walked, over the population the
  writer already reads. Seconds, as before.
- error / empty / loading states — An entry whose pattern fails to compile is skipped, as before. A
  file no other entry's basis holds has only its walking entry's pattern to match.
- observability — Unchanged: `selfcheck --fix` prints one `govkit: fix` line per rewrite and `mint`
  one line per entry. A foreign line left alone is not reported, as §4 states.
- risks — A real cross-entry carrier outside the pattern owner's basis would stop moving. The class
  predicate found none, and `kit version markers` grades the four that exist, so a dropped one reds
  that leg at the next drift-audit bump. Line numbers that units 10 to 19 cite below the edits shift
  by the commit's net delta, which the commit body states. Between the restore commit and unit 7's
  mint, the epoch reads playbook-render FAILED, as it already reads the four kits units 2, 4 and 5
  moved. The close's one bar runs after unit 7.
- testing — AC1 to AC8, and the restaged arm under `New arm:` in §7. The v3.x arm itself runs in
  `playbook render selftest` at the close.
- migration — None for the code commit. `{prefix}/govkit` is never installed into a target
  (`tools/govkit/registry.toml:295-297`). An adopter receives S6's one fixture line inside
  playbook-render 1.29 through `govkit.py update`. The line is selftest data, and no render reads it.
- user docs — N/A — no page under `help/` names the carrier writer or `mint` (`git grep -n -i
  "mint\|--fix" -- help/` printed nothing on 2026-10-14). The `USAGE` text at
  `tools/govkit/govkit.py:13225-13231` stays true.

## 6. Acceptance criteria

- **AC1** — When the §4 `writer` command runs in a clone of the code commit, it prints `[]` and
  `git status --porcelain` in the clone prints nothing. When it runs in a clone of the code commit's
  first parent, it prints the one tuple naming `tools/playbook/render_playbook.py` with `3.5` and
  `1.28`, and `git diff -U0` there changes line 1646 only.
  Red when: S1 is absent, or a second foreign-pattern line in the tree becomes a carrier.
  figure: the tuple's values are PINNED at `9d0ad1c0a` on 2026-10-14, and they move if
  playbook-render's version moves first.
- **AC2** — When, in a clone of the code commit, the number on the `KIT_DRIFT_AUDIT_VERSION` line of
  `tools/drift-audit/drift_report.py` is edited to `9.99` and the `writer` command runs,
  `grep -c "version: '9.99'"` prints 1 for each of `tools/workflows/drift-audit-code.js`,
  `drift-audit-code.template.js`, `drift-audit-state.js` and `drift-audit-state.template.js`.
  Red when: S1 is narrowed to the walking entry's own pattern, so the harness fields keep the old
  number.
- **AC3** — When `python tools/govkit/govkit.py mint --base ebce889c7` runs in a fresh clone of the
  code commit, it exits 0 and prints an `->` line for each of `agent-cap`, `branch-reconcile`, `roles`
  and `unattended` and for no other entry, and `git status --porcelain -- tools/playbook/` prints
  nothing. After `git -c user.name=scratch -c user.email=scratch@example.invalid commit -qam scratch`
  in that clone, `python tools/govkit/govkit.py epoch --base ebce889c7` prints
  `epoch: playbook-render · clean · 1.28` and no line holding `playbook-render · FAILED`.
  Red when: the mint writes a line of `render_playbook.py`, or a fifth entry mints. Both hold at the
  code commit only. The restore commit follows it and moves playbook-render, so a mint there moves
  five, which is unit 7's measure.
  cost: the mint runs the four kits' `[[regenerate]]` argvs inside the clone, among them the roles
  scaffold and the unattended adopter; minutes, UNVERIFIED.
  figure: the four-kit set is PINNED from unit 7's builder's run over `ebce889c7` on 2026-10-14; the
  mint's own output derives it.
- **AC4** — When the §4 `arm` command runs at the code commit, it exits 0 and prints `ok` for
  `[dRB-20] another entry's pattern in a file outside that entry's basis is not a carrier`, for the
  relabelled `[aMF-64 S2]` positive case and for the count. When it runs after rollout step 2, with
  the arm written and `tools/govkit/govkit.py` untouched, it exits 1, and its `FAIL` lines name the
  new label and the count.
  Red when: S1 is reverted, so `vk/harness.js`'s `version:` field moves to 1.1 and the count reads 9.
  fixture: the arm's own scratch repo under `tempfile.mkdtemp()`; the tree needs nothing else.
- **AC5** — When `grep -c "ANY entry's" tools/govkit/govkit.py` runs at the code commit it prints 0,
  and `grep -c "A pattern counts only in its own entry's basis" tools/govkit/govkit.py` prints 1.
  Red when: the docstring still states the any-entry rule, or never states the scope.
- **AC6** — When `git diff --name-only <first parent> <code commit>` runs, it prints exactly
  `tools/govkit/govkit.py` and `tools/govkit/selftest.py`. And
  `git diff <first parent> <code commit> -- tools/govkit/ | grep -cE '^[+-][[:space:]]*def '` prints 0.
  Red when: a third file moves, such as `tools/govkit/registry.toml` or
  `tools/govkit/entries/playbook.kit.toml`, both in playbook-render's epoch set, or a function is added
  or renamed with no symbol-index regeneration.
- **AC7** — At the restore commit, `grep -n "governance-template: v[0-9]" tools/playbook/render_playbook.py`
  prints exactly two lines, `1397` and `1646`, and both read `v3.5`. `git diff --name-only <code
  commit> <restore commit>` prints exactly `tools/playbook/render_playbook.py`, and `git diff -U0`
  over the same pair changes line 1397 only. In a clone of the restore commit, the §4 `writer`
  command prints `[]` and `git status --porcelain` prints nothing. There,
  `python tools/govkit/govkit.py epoch --base ebce889c7` prints a line opening
  `epoch: playbook-render · FAILED`, the move unit 7's mint dates.
  Red when: line 1397 still reads `v1.28`, or any `v1.` value, or the writer rewrites the restored
  line, or the restore lands before the code commit, or the restore commit carries a second file or
  a bump.
  figure: the line numbers are PINNED at `9d0ad1c0a` on 2026-10-14. The code commit touches no line
  of `render_playbook.py`, so they hold at the restore commit.
- **AC8** — When the §4 `v3render` command runs at the restore commit, it exits 0 and prints
  `<!-- governance-template: v3.5 --> True True True`.
  Red when: the restored marker's major reaches `TEMPLATE_MAJOR`, so the render refuses the fixture's
  `when:node-table` fence, or the reseed note is gone, which would fail the arm at `:1415-1419`.
  figure: the green and red readings are PINNED from the 2026-10-14 trial in §4 "The restore".

## 7. Gates

`govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `govkit selfcheck` · `kit epoch (shipped bytes move, the version moves)` · `kit version markers` · `recall floor arms` · `codebase-map coverage + freshness` · `playbook render selftest` · `memory hygiene`

`govkit refusal join`, `govkit acceptance matrix` and `recall floor arms` are owed by the guard join
on `tools/govkit/`. The refusal join's floor does not move, because no refusal branch is added or
taken away. `kit version markers` is where a dropped drift-audit carrier would show.
`playbook render selftest` is owed by its `{prefix}/playbook/` guard (`tools/gate-legs.json:1637-1640`),
which S6 trips. It runs the v3.x arm over the restored fixture. `kit epoch` reads playbook-render
FAILED from the restore commit until unit 7's mint, and the close's bar runs after that mint.

New arm: tools/govkit/selftest.py · covers AC4 · `check_fix_carriers` over the base writer, where `vk/harness.js`'s `version:` field moves to 1.1 and the rewrite count reads 9 · none

## 8. Open questions

- **F1 — What happens to `render_playbook.py:1397`, the fixture the class already rewrote from `v3.5`
  to `v1.28`?**
  The arm there still grades its intent. `render_playbook.py:1001` treats any major below
  `TEMPLATE_MAJOR` (4) as an older template, and 1 is below 4. But the fixture's comment says it is a
  seeded v3.x template, and its bytes no longer say so.
  - (a) Leave it, and record it as the hands-off external in §3. No fifth kit moves in this build. The
    next unit that moves playbook-render's bytes restores `v3.5` under the bump it already owes.
  - (b) Restore `v3.5` here, in a second commit. Then run `govkit.py mint --base <that commit's
    parent>`, which mints playbook-render alone to 1.29 and runs `adopt-playbook.sh --target .`,
    re-rendering `AGENTS.md`. Unit 7's mint then reads playbook-render clean and still moves four.
    It costs a fifth bump and a charter re-render inside a build whose brief keeps the minted set
    unchanged.
  Recommendation: (a). The bytes are wrong but inert once S1 lands, and (a) dates their restore with
  a bump some unit pays anyway.
  RESOLVED (owner, 2026-10-14): (b). S6 restores the line in its own commit. The revision brief
  `prompts/2026-10-14-prompt-TOOL-dRedressedBar-20-2-revision.md` gives the 1.29 bump to unit 7's
  mint, so no mint runs in this unit and unit 7 moves five kits.

## 9. Revision log

- rev-1 · 2026-10-14 · initial draft from the unit-20 brief. The defect was reproduced at `9d0ad1c0a`
  with the writer alone. The class predicate was run over the real registry, and S1's edit and S3's
  fixture were each trialled in scratch against the base writer and the tightened one.
- rev-2 · 2026-10-14 · §1 · S5 · S6 · §3 · §4 · §5 · AC3 · AC7 · AC8 · §7 · §8 · the owner resolved
  F1 as (b), marked in place. S6 restores `tools/playbook/render_playbook.py:1397` to `v3.5` in a
  second commit after the code commit. AC7 observes that commit, and AC8 observes the line's arm
  through `render` with the new `v3render` command. The restore moves playbook-render's bytes. §3
  Edges hand its 1.28 → 1.29 bump to unit 7's mint, so this unit bumps nothing. The F1 (a) hands-off
  is dropped, and `playbook render selftest` joins §7.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "scope an entry version pattern to the files its own
marker basis holds when writing version carriers"` returned only name-stem neighbours, among them
`write`, `write_text`, `scope`, `owners_of` and `resolve_entry`. None is a seam to build beside. The
unit extends the existing seam, `write_version_carriers` in `tools/govkit/govkit.py`, and reads the
population `derive_marker_basis` already returns, so no new function and no second population are
built. The arm extends `check_fix_carriers` in `tools/govkit/selftest.py`, the writer's existing
fixture, rather than adding a function beside it. The recall probe returned TOOL-aMendedFleet-64, the
unit that wrote the any-entry clause. Its §4 evidence names the drift-audit harnesses as the reason
for that clause and measured the near-misses its ownership guard excludes. That record and the code
agree. It did not measure a foreign pattern in a file outside the pattern owner's basis, because
`render_playbook.py:1646` was written after it landed. The gotchas checklist for the two files
selected `a-new-local-collides-in-a-long-function`, `staged-break-substitutes-a-synthetic-value`,
`staged-break-runs-stale-bytecode` and `two-answers-to-one-question`, and §4 answers each. S6's
`v3render` probe builds nothing new. It calls the engine's own `render` over the arm's own fixture
string, read from the source, with the arm's deploy shape.

Recall terms used: `python tools/memory-recall/query.py "govkit mint or selfcheck --fix rewrote a
version number in a file another kit owns" --terms "write_version_carriers derive_marker_basis
carrier ownership clause version_from pattern marker_carriers foreign mint playbook-render
governance-template"`
