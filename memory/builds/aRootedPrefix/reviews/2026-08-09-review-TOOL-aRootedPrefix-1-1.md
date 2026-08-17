# TOOL-aRootedPrefix-1 — Tier-2 review: codebase-map at any install prefix

**Serves:** spec-audit TOOL-aRootedPrefix-1

**Status:** REVIEWED · rev-1 · 2026-08-09 · node a · Tier-2 · streams tooling
**Under review:** `1d8097a` (the kit is correct at any install prefix) + `63e2643`
(TOOL-aRootedPrefix-2 — every printed path resolves), against base `663ca42`.
**Spec:** `memory/builds/aRootedPrefix/spec/2026-08-09-spec-aRootedPrefix-1.md` (rev-2, S1-S9).
**Verdict:** **CHANGES REQUESTED** — 2 blockers, 2 high.

## Review shape

| | |
|---|---|
| raw findings | 18 |
| confirmed (survived an adversarial skeptic) | 11 |
| refuted | 7 |
| unverified / outstanding | 0 |
| precision | 0.61 |

The 11 confirmed findings collapse to **7 distinct defects**: three reports named the same
unescaped-`sed`-replacement line, two named the same unconditional success echo, and two named the
same `git rev-parse --show-toplevel` anchor from opposite directions. Each merged entry below lists
the reproductions that survived, because they exercise genuinely different reachability paths.

**The shape of the result is itself the headline.** The engine changes (S1-S3, S5-S7) came through
clean: not one confirmed finding lands in `resolve_root`, `require_adopted_root`, the two CLI
refusals, or the version bump. Every defect but one is in `adopt-codebase-map.sh` (S4) — the one
file in the change set that **no gate leg executes**. `tools/gate-legs.json:218` runs
`tools/codebase-map/selftest.py` and nothing else; `selftest.py` never mentions the adopter. S4 was
written without a harness and it shows: 4 of 7 defects, including one blocker, live there.

The core of the fix is sound and I want to say so plainly. `resolve_root` (map_lib.py:83) is the
right shape — pure, `abspath` never `resolve()`, conf-before-`.git` so an adopted root that also
holds `.git` wins, fallback byte-identical to the old grandparent rule so existing root installs
cannot regress. `require_adopted_root` (map_lib.py:155) closes the actual
`vacuous-selector-empty-population` hole the build exists for. Both survived adversarial probing.

---

## BLOCKERS

### B1 — the adopter anchors ROOT with the exact mechanism §4 rejected, and writes into a repo the operator never named

`tools/codebase-map/adopt-codebase-map.sh:18` (merges confirmed ids 1, 15)

```sh
ROOT="$(git -C "$HERE" rev-parse --show-toplevel)" || exit 2
```

The comment above it claims this is "the same anchor map_lib uses". It is not, and the spec says so
in its own words. §4 Alternatives rejected: *"Rejected on the junction case: git resolves the
physical path, so a junctioned kit dir would anchor to the LINK TARGET's repo."*
`map_lib.resolve_root`'s docstring (map_lib.py:100-103) states the same contract from the other
side — `abspath`, never `resolve()`, *"which is why the root is not taken from
`git rev-parse --show-toplevel`"*. S4 shipped the rejected alternative into the one file that
writes to disk. The `-ef` inode cross-check that used to bind adoption to the operator's repo was
deleted in the same hunk.

Two independent reproductions, both measured:

**(a) Junctioned kit dir.** `adopting/tools/codebase-map` -> `kitsrc/codebase-map`:
`--show-toplevel` returned `.../jprobe/kitsrc`, `--show-prefix` returned `codebase-map/`, so the
name check at line 69 passes. The script `cd`s into the **kit's own source repo** and writes
`.codebase-map.conf`, the entire `MAP_ROOT` tree, and the gate file there, then prints `Adopted.`
The adopting repo gets nothing. Because `resolve_root` correctly anchors to the adopting repo, both
CLIs afterwards refuse with `no .codebase-map.conf at the resolved repo root` — a successful-looking
adoption that cannot work, with the artifacts in a third-party repository. In this fleet's layout
that third-party repository is the governance repo itself.

**(b) Run by path from another repo.** With a governance repo at `$TMP/gov` (kit at
`tools/codebase-map`) and a target at `$TMP/target`, `cd $TMP/target && bash
$TMP/gov/tools/codebase-map/adopt-codebase-map.sh --scaffold` created `.codebase-map.conf` in
**gov** and left target untouched, while printing relative paths (`tools/codebase-map/...`) that
read as the cwd's repo. Pre-diff, that same invocation exited 1 with `kit dir must live at
<repo-root>/codebase-map/`. This is a **regression**: the deleted `-ef` guard was the only thing
binding adoption to the operator's tree, and line 2 of the script still tells the operator to
"Run it BY PATH from anywhere".

This is a blocker on three counts: it silently writes into an unnamed repository (a house-law
fail-closed violation), it regresses a layout that worked before the diff, and it contradicts a
guarantee the same change set writes into two docstrings.

**Fix.** Resolve ROOT logically from `$HERE`, mirroring `resolve_root`: walk up for
`.codebase-map.conf`, else `.git`, and derive `KIT_REL="${HERE#$ROOT/}"` from the same string — both
spellings then come from one `pwd`, which is what the MSYS comment on line 20 actually needs. If git
must stay for the prefix, add a containment assert **before any write**:

```sh
case "$HERE/" in "$ROOT"/*) ;; *)
  echo "kit dir $HERE is a link into another tree; git resolved the repo root to $ROOT —"
  echo "copy the kit in, or run the adopter from inside the adopting repo"; exit 1;; esac
```

and restore the cwd cross-check: when `git rev-parse --show-toplevel` from the cwd is non-empty and
not `-ef "$ROOT"`, refuse naming **both** paths. Self-adoption still passes because the two agree.

**Left-shift gate.** Add an adopter e2e leg to `tools/gate-legs.json` — there is none today. Minimum
arms: (i) kit dir behind a symlink/junction, assert the conf lands in the adopting repo or the run
refuses, never in the link target's repo; (ii) adopter invoked by path from a *different* repo,
assert refusal. Both fail today.

---

### B2 — three entrypoints put the kit on `sys.path` with `resolve()` while the renderers now embed the `abspath` prefix, so the freshness byte-compare cannot converge

`tools/codebase-map/gen_map.py:21` (also `map_diff.py:41`, `reuse_lookup.py:36`) · confirmed id 9

```python
sys.path.insert(0, str(Path(__file__).resolve().parent))   # gen_map.py:21
```

against `map_lib.kit_dir()` = `Path(os.path.abspath(__file__)).parent` (map_lib.py:124) and the gate
template's `_kit_dir()`, which is `abspath` by design (test_codebase_map.template.py:38-41). The
`resolve()`/`abspath` split predates this diff and was harmless — pre-diff the renderers used the
`REGEN_CMD` constant and carried **no kit-dir dependence at all**. Commit `63e2643` is what makes it
observable: `render_inventories_json`, `render_symbols_json` and `render_map_md` (map_lib.py:1172,
1200, 1240) now embed `kit_rel()`/`regen_cmd()` **into the byte-compared artifacts**.

Reproduced on a repo whose kit dir is a junction (`repo/tools/codebase-map` ->
`repo/vendor/codebase-map`, conf at the root):

- `gen_map.py --write` stamps `generated by vendor/codebase-map/gen_map.py` into
  `inventories.json` and `MAP.md`;
- the gate re-renders `tools/codebase-map/...` and fails
  `STALE inventories.json — regen: python tools/codebase-map/gen_map.py --write`;
- `gen_map.py --check` exits 0 on the same tree — two entrypoints disagreeing about freshness;
- running the printed remedy verbatim re-renders the *vendor* spelling. **The loop never converges.**

This is risk (c) from the review brief realised: not a cross-platform flap but something worse, a
permanently red gate whose own remedy cannot clear it. It bites exactly the symlinked/junctioned
layout that `resolve_root`'s new docstring promises to support — *"the gate's walk-up and the
adopter both accept that layout — this must agree with them"*. `gen_map.py:21` is the one remaining
`resolve()` that breaks that promise.

**Fix.** One line in each of the three entrypoints:

```python
sys.path.insert(0, str(Path(os.path.abspath(__file__)).parent))
```

(`selftest.py:15` carries the same idiom; fix it for consistency, though it drives fixtures.)

**Left-shift gate.** Add an arm to `t_remedy_paths_are_real` that builds the kit behind a
symlink/junction and asserts `gen_map --check` and the gate agree on freshness. The existing arm
uses `shutil.copytree`, so no arm can see this class. Cheaper companion, and worth having anyway: a
grep gate banning `Path(__file__).resolve()` inside `tools/codebase-map/`, with the one-line reason
— the kit has committed to `abspath` in three docstrings and should enforce it mechanically.

---

## HIGH

### H1 — `$KIT_REL` goes unescaped into a `sed` REPLACEMENT, corrupting a conf this same script later `source`s

`tools/codebase-map/adopt-codebase-map.sh:81` (merges confirmed ids 3, 7, 12)

In `sed`'s replacement text, `&` means "the whole match" and `\` escapes. `$KIT_REL` comes from
`git rev-parse --show-prefix` (line 21) and nothing filters it — the `case` at line 69 accepts any
`*/codebase-map`.

Measured with the kit under `R&D/`:

```
MAP_DIFF_CMD="python RMAP_DIFF_CMD="python codebase-map/map_diff.py"D/codebase-map/map_diff.py"
```

`sed` **exits 0**, so the `else` note branch never fires, the `mv` at line 83 commits the corruption,
and line 89 announces a successful stamp over a broken file. Line 92 then `.`-sources that file on
the required re-run: bash parses the mangled remainder as a command word and tries to execute it
(measured: `codebase-map/map_diff.pyb/...: No such file or directory`, and the script continues past
it — no `set -e`). With a segment containing `"` plus `;` it executes chosen commands as the
operator: `KIT_REL='x";echo INJECTED-COMMAND-RAN;"/codebase-map'` ran the echo at source time.

`&` in a directory name (`R&D`, `Q&A`) is ordinary on both platforms. A `|` is safe only by luck —
`sed` errors and the note branch fires. This is a silently-wrong-but-confident write in the one line
the code goes out of its way to get right by construction; it is the same class the whole build
exists to close, in the file the build added.

**Fix.** Keep path text out of `sed`'s replacement grammar and out of a shell-quoted value.
Validate first, fail closed, then stamp without `sed`:

```sh
case "$KIT_REL" in *[!A-Za-z0-9._/-]*)
  echo "note: prefix '$KIT_REL' cannot be expressed in the conf grammar — set MAP_DIFF_CMD by hand" ;;
*)
  grep -v '^MAP_DIFF_CMD=' "$ROOT/.codebase-map.conf" > "$ROOT/.codebase-map.conf.new" \
    && printf 'MAP_DIFF_CMD="python %s/map_diff.py"\n' "$KIT_REL" >> "$ROOT/.codebase-map.conf.new" \
    && mv "$ROOT/.codebase-map.conf.new" "$ROOT/.codebase-map.conf" ;;
esac
```

Then re-read the file and confirm the expected line is present before claiming success (see L1).

**Left-shift gate.** In the new adopter e2e leg, parameterise the install prefix over a hostile set
— `R&D/`, `a b/`, `x'y/`, and (POSIX only) `a|b/` — and assert after each run that
`. .codebase-map.conf` in a clean subshell yields exactly the expected `MAP_DIFF_CMD` and executes
nothing. A conf-grammar round-trip arm belongs in `selftest.py` next to `t_conf_grammar` too.

### H2 — the stamp only fires on the branch the documented flow never takes, so AC8 fails on the primary adoption path

`tools/codebase-map/adopt-codebase-map.sh:74` + `tools/codebase-map/gen_map.py:207` · confirmed id 16

The `MAP_DIFF_CMD` stamp sits inside `if [ ! -f "$ROOT/.codebase-map.conf" ]`. But the kit's own
README step 2 (`tools/codebase-map/README.md:45`) and `WIRE-INTO-PROJECT.md:150` both instruct
`cp <kit>/.codebase-map.conf.example .codebase-map.conf` **before** the adopter runs. On the
documented path the branch never fires and nothing validates the value.

Reproduced at a `tools/`-prefixed install following the docs verbatim: the adopter ran to `Adopted.`
at exit 0, and the scaffolded `memory/map/README.md:24` shipped

```
5. Digest any range: `python codebase-map/map_diff.py <base>..<head>`
```

while `ls codebase-map/map_diff.py` -> No such file. Line 16 of the same README correctly said
`python tools/codebase-map/gen_map.py --write`, isolating the cause to `gen_map.py:207`:

```python
diff_cmd=conf.get("MAP_DIFF_CMD") or f"python {m.kit_rel()}/map_diff.py",
```

The truthy-but-stale conf value beats the prefix-correct fallback. WIRE §3b step 6 then copies that
same dead string into the kickoff manifest.

AC8 says: *"the regen command the gate PRINTS names a path that exists"*. S9's rejected-alternative
paragraph says the acceptance test is *"the same one line — does the path the kit printed exist"*.
On the documented adoption path, for the digest command, it does not. The example's own comment
tells the operator the adopter will stamp the line, so the wrong value is the **default outcome**.

**Fix.** Move the check out of the create-only branch: after `. "$ROOT/.codebase-map.conf"`, extract
the path token from `MAP_DIFF_CMD` and, when it is not a file under `$ROOT`, re-stamp it with
`$KIT_REL` or refuse naming both the configured and the real spelling. Belt-and-braces in
`gen_map.py:207`: treat a `MAP_DIFF_CMD` whose path does not exist as absent and fall back to
`f"python {m.kit_rel()}/map_diff.py"`.

**Left-shift gate.** Extend AC8's arm from the regen command to **every** path the kit prints. In
`t_remedy_paths_are_real`, after a prefixed scaffold, extract each backticked/`python `-prefixed
path token from the scaffolded `README.md`, `MAP.md` header, `inventories.json` `$comment`, the
gate's STALE remedy and all three `--help` texts, and assert each names an existing file under the
root. That single arm covers H2 and would have caught it pre-merge.

---

## MEDIUM

### M1 — in a `.git`-less tree the gate's `_kit_dir()` walks to the filesystem root and imports `map_lib.py` from outside the project

`tools/codebase-map/test_codebase_map.template.py:49` · confirmed id 2

The loop breaks only on `(parent / ".git").exists()`, so the docstring's claim that *"it can never
leave the repo into a neighbouring checkout"* is false whenever `.git` is absent — a `git archive`
tarball, a docker build whose `.dockerignore` drops `.git`, a vendored source drop.

Measured: gate at `<x>/export/tests/test_codebase_map.py`, no `.git` anywhere, an unrelated kit copy
at `<x>/outside/codebase-map`. `_kit_dir()` returned the out-of-tree directory and the module-level
`sys.path.insert` + `import map_lib` **loaded and executed it** (probe printed
`map_lib is ...\outside\codebase-map\map_lib.py OUT-OF-TREE COPY`).

The new `sorted(parent.glob("*/codebase-map"))` probe at line 44 is what widens the surface. The
pre-1.1 walk was also unbounded but could match only `<ancestor>/codebase-map`; the glob now covers
**every immediate subdirectory of every ancestor up to `/`**, including user-writable ones — at
`parent=/` it matches `/tmp/codebase-map/map_lib.py`. The project's own test suite then executes
third-party code and byte-compares this repo's artifacts against a foreign engine and KIT version:
a green or a red that says nothing about this repo. (The glob's cost and `PermissionError` exposure
on a large repo are real but secondary; `glob` swallows permission errors and each level is one
`scandir`. Bounding the walk fixes the cost too.)

**Fix.** Make the boundary `.git` **OR** `.codebase-map.conf` — the conf is committed, so it
survives an export that drops `.git`. Probe that ancestor's candidates, then `break`
unconditionally, and let the existing named `Probed:` `RuntimeError` fire at the boundary instead of
walking above it.

**Left-shift gate.** `selftest.py`'s `probe()` (selftest.py:211) unconditionally `mkdir`s `.git` at
the fixture root, so case (d) and every other arm bound the walk and none can see this. Add the
missing arm: a tree with **no** `.git`, its conf at the export root, and a planted
`<sibling>/codebase-map/map_lib.py` one level above — the gate must raise, not import the plant.
The arm fails today.

### M2 — the adopter accepts any prefix depth; the gate template it installs resolves only one segment

`tools/codebase-map/adopt-codebase-map.sh:70` · confirmed id 4

The shell `case` pattern `*/codebase-map` matches slashes, and line 71 tells the operator "any prefix
above it is fine". The gate template probes only `<ancestor>`, `<ancestor>/codebase-map` and
`<ancestor>/*/codebase-map`. The two validators disagree.

Reproduced at `<root>/a/b/codebase-map` with `GATE_FILE` outside the kit: the name check passes,
`.codebase-map.conf` is written (lines 74-91), the whole map tree is scaffolded (105-117) and the
gate is copied in (120-126) — and only **then** does line 129 die with
`RuntimeError: codebase-map kit dir ... not found above ...`, listing 4 probed paths, none of them
the real kit dir. The adopter relabels this `gate FAILED on the freshly seeded tree — fix before
committing`, which sends the operator hunting a coverage violation that does not exist, and the repo
is left half-adopted. `resolve_root` is depth-unbounded, so the CLIs work at a depth the merge gate
can never run at.

The one-segment cap is an explicit §3 non-goal and that is fine. Advertising an unbounded prefix and
discovering the cap after the tree is scaffolded is not.

**Fix.** After the name check, add the depth check the gate actually implements, **before** the conf
is written:

```sh
case "$KIT_REL" in */*/codebase-map)
  echo "prefix deeper than one segment: the gate template probes only <ancestor>/codebase-map and"
  echo "<ancestor>/*/codebase-map — install at <root>/codebase-map or <root>/<one-segment>/codebase-map,"
  echo "or point GATE_FILE inside the kit dir"; exit 1;; esac
```

**Left-shift gate.** One parity arm in `selftest.py`: for each of a set of prefixes, assert the
adopter's accept/refuse decision equals whether the gate template's `_kit_dir()` can resolve the kit
from a `GATE_FILE` outside it. That binds the two validators together so a future widening of either
must move the other.

---

## LOW

### L1 — the "was stamped" success line prints on the failure branch, and the stamp is never verified

`tools/codebase-map/adopt-codebase-map.sh:89` (merges confirmed ids 6, 17)

Lines 88-89 sit **outside** the `if`/`else` that decides whether the stamp landed, so after
`note: could not stamp MAP_DIFF_CMD — set it to "python tools/codebase-map/map_diff.py" by hand.`
the operator immediately reads `MAP_DIFF_CMD was stamped for this install prefix: python
tools/codebase-map/map_diff.py`. Reproduced end-to-end two ways: a `|` in `$KIT_REL` (sed exits 1)
and a stub `sed` first on PATH. The second line is the one they will believe, so they skip the manual
fix and ship a conf carrying the example's nonexistent `python codebase-map/map_diff.py`, which
`gen_map.py:207` then renders into the map README (the H2 mechanism, reached from the other side).

Two smaller edges in the same block: the `mv` at line 83 has its exit status unchecked, and `sed`
exits 0 when the `^MAP_DIFF_CMD=` anchor matches nothing — so if a future example file ever comments
that key out, the same false success prints. A fail-open success message is precisely the class this
repo's DEAD PROBE doctrine targets.

**Fix.** Move the echo inside the success branch (after the `mv`), and make that branch conditional
on the substitution actually landing — re-read the conf and
`grep -q "^MAP_DIFF_CMD=\"python $KIT_REL/map_diff.py\"$"` before claiming it, falling through to the
manual-fix note otherwise.

**Left-shift gate.** The adopter e2e leg should assert on **stdout as a whole**: no run may print both
a failure note and a success claim for the same step. A cheap generic form — grep the adopter's
output for `could not` co-occurring with `was stamped`/`Adopted.` — generalises past this one line.

---

## What the refutations say (7 of 18)

Worth recording, because the refuted set clusters in one place: the **engine**. Claims that
`resolve_root` mishandles case-insensitive filesystems, a kit dir at the filesystem root, or a repo
with no `.git` anywhere; that `relative_kit` breaks when root equals the kit dir or the kit is not
under root; that `require_adopted_root` can falsely refuse a legitimate adopter; and that embedding
`kit_rel()`/`regen_cmd()` in the three renderers flaps the byte-compare across platforms — all were
probed and did not survive. `relative_kit`'s `ValueError` fallback to the bare dir name (map_lib.py:127)
and the POSIX-join discipline hold; the false-refusal risk is genuinely bounded by step 4 of the
resolution table, as §5 claims. The only surviving render-determinism defect (B2) is a
`resolve()`/`abspath` split that predates this change and became observable through it — not a flaw
in the S9 design, which §4's rejected-parameter paragraph argued correctly.

## Merge bar

Recommend holding the merge for **B1** and **B2**. Both are small, mechanical fixes (a containment
assert plus a logical ROOT; three `resolve()` -> `abspath` edits), and both are the same underlying
mistake — physical vs logical path resolution — which the spec had already reasoned through and
gotten right in `map_lib` and wrong everywhere else.

**H1** and **H2** should land with them: H1 because it writes a corrupt file and then sources it, H2
because it defeats AC8 on the primary documented adoption path, which is the acceptance criterion
this build's second commit exists to satisfy.

**M1**, **M2** and **L1** are legitimate follow-ups if the owner prefers a narrower merge; M1 in
particular changes a gate template that adopters own and do not receive on an engine update, so the
sooner it is right the fewer stale copies exist in the field.

## The one structural recommendation

Add an **adopter e2e leg** to `tools/gate-legs.json`. Four of the seven defects — including a
blocker — are in a shell script that no gate leg has ever executed, while the Python engine beside
it, which `selftest.py` covers at 20-plus arms, produced zero confirmed findings. That correlation
is the review's most useful output. The leg needs a fixture repo, a parameterised install prefix,
and the arms named under B1, H1, H2, M2 and L1 above; every one of them fails today.
