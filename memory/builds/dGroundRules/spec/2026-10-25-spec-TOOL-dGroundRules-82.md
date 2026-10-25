# TOOL-dGroundRules-82 — a parity row holds policy-mirror.js's bash candidate order against the canonical resolve_bash

**Status:** CLOSED · rev-1 · 2026-10-25 · node d · Tier-1 · base 59f02fde · streams tooling · order 29

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dGroundRules-82-ledger.md](../build/2026-10-25-build-TOOL-dGroundRules-82-ledger.md) | journal | — |
| [2026-10-25-prompt-TOOL-dGroundRules-82-1-spec-writer.md](../prompts/2026-10-25-prompt-TOOL-dGroundRules-82-1-spec-writer.md) | journal | — |
| [2026-10-25-prompt-TOOL-dGroundRules-82-spec-brief.md](../prompts/2026-10-25-prompt-TOOL-dGroundRules-82-spec-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

`tools/policy/README.md` and the comment above `let BASH;` in `tools/policy/policy-mirror.js` both
claim that the JS `resolveBash` keeps the order of the canonical `resolve_bash`, and nothing checks
it. This unit adds one behaviour section to `tools/lib/resolve-python.test.sh`. It runs both
resolvers with their spawn stubbed over one fixture PATH, and reds when either side adds, omits or
reorders a candidate against the order `TOOL-dGroundRules-81` states.

## 2. Scope (IN)

- **S1** — A new section `2j` in `tools/lib/resolve-python.test.sh`, directly above the
  `# ---- 3. THE BAN` header and after section `2i`, in the text §4 "The section" gives. It holds two
  assertions, one per resolver. Observed by AC1, AC2 and AC3.

## 3. Non-goals (OUT)

- `tools/policy/policy-mirror.js`, `tools/policy/README.md`, `tools/lib/resolve_bash.py` and the
  inline copy in `tools/policy/check_policy.py`. This unit reads them and edits none of them.
  `TOOL-dGroundRules-81` sets the JS order, and the Python order stays as it is.
- A `PARITY_ROWS` row. That table compares bytes between copies of one block, and these two
  resolvers are in two languages (§4 "Alternatives rejected").
- A policy fixture case. `tools/policy/check_policy.py` is not touched, so the `policy fixtures`
  leg does not grow.
- The other `resolve_bash` copies that return another shape (`TOOL-dSettledRoster-6`'s ask), the
  review's other findings, and any other spec.

### Edges

- **consumes-from** `TOOL-dGroundRules-81` — its §4 "The order" line is the order this section
  asserts. Without its S1, the JS list holds no second PATH bash, and AC1 reds as AC2's first break
  shows.

## 4. Design

### Evidence

Read at `59f02fde9`. The premise of L2 (id 6) holds.

- `git grep -n resolveBash` and `git grep -n onPath` outside `memory/` find only
  `tools/policy/policy-mirror.js` (`:62`, `:64`, `:66`, `:79`). No suite, fixture or parity row
  reads either name.
- `tools/lib/resolve-python.test.sh:186` holds the `resolve_bash_py` row. It compares the bytes of
  `tools/lib/resolve_bash.py` with its copy in `tools/policy/check_policy.py` (`:892-913`) and reads
  no JS.
- The claim sits in the resolver clause of `tools/policy/README.md` (`:321-323`) and in the comment
  above `let BASH;` (`tools/policy/policy-mirror.js:56-60`). `TOOL-dGroundRules-81` rewrites both
  and keeps the claim, now stated as one order with a different PATH slot.

The canonical `resolve_bash` (`tools/lib/resolve_bash.py:15-34`) tries `GOV_BASH`, then
`shutil.which("bash")`, then the two Git for Windows paths, then a bare `bash`. It skips an empty or
repeated candidate. `TOOL-dGroundRules-81` §4 "The order" states the JS order after its S1:

```
resolveBash tries GOV_BASH ; then each existing bash.exe then bash in every PATH directory, in PATH order ; then C:/Program Files/Git/bin/bash.exe ; then C:/Program Files/Git/usr/bin/bash.exe ; then bash — a repeat tried once, the first whose test -f on the shim exits 0 kept. resolve_bash holds the same order with one PATH bash, the one shutil.which("bash") names, in the PATH slot.
```

That is the relation this section asserts. GOV_BASH comes first and the last three candidates
close the list on both sides. In the PATH slot, the JS tries every PATH bash and Python tries only
the one `which` names.

Two host facts shape the fixture. Both were measured on this node (Python 3.14.6, node 22.22.3,
git-bash).

- On Windows, `shutil.which("bash")` does not find an extensionless `bash` file. A PATH of two
  directories each holding only `bash` made the Python side skip both and take Git's
  `usr/bin/bash.EXE` instead. So each fixture directory holds the name `which` finds on the host:
  `bash.exe` under git-bash, `bash` elsewhere. `which` returns the extension in PATHEXT's case
  (`.EXE`), so the Python side writes it as `.exe`.
- Under git-bash, `: > D2/bash` written beside `D2/bash.exe` opens `bash.exe`, so one directory
  cannot hold both names. The section does not assert the JS order of `bash.exe` before `bash`
  inside one directory.

The PATH is cut down to the two fixture directories. Neither stubbed resolver spawns anything, and
`node` and the python are run by absolute path. So the host's own PATH bashes, Git's `usr/bin` and
the System32 WSL launcher on this node, never enter either list.

### The section

S1 inserts these lines, blank line included, directly above `# ---- 3. THE BAN`:

```
# ---- 2j. THE TWO BASH RESOLVERS' CANDIDATE ORDER, BEHAVIOUR (TOOL-dGroundRules-82) -----------------
# Parity holds check_policy.py's copy of resolve_bash to its canonical; this holds the policy kit's JS
# resolveBash to the canonical's candidate ORDER, which no byte compare can, as TOOL-dGroundRules-81 §4
# "The order" states it. Each runs with its spawn stubbed, so every candidate fails and each prints all
# it tried, over a PATH of two fixture directories, each holding the bash name `shutil.which` finds on
# this host. GOV_BASH first and RB_TAIL last are one order on both sides; in the PATH slot the JS tries
# every PATH bash and Python the one `which` names. D1 stands for a first PATH bash that cannot see the
# shim, so D2 in the JS list is the case TOOL-dGroundRules-81 restored. A host with no node prints no
# list and reds, never skips. WHAT THIS DOES NOT CHECK: which candidate a real host keeps, a repeat
# tried once, a `bash.exe` before a `bash` in one directory (git-bash opens `bash.exe` when asked to
# write `bash` beside it), or any resolve_bash copy but the canonical.
POLICY_DIR=$(resolve_kit_dir "$REALPY" policy policy-mirror.js "$HERE") || exit 2
NODE=$(command -v node)
case "$(uname -s)" in MINGW*|MSYS*|CYGWIN*) RB_B=bash.exe ;; *) RB_B=bash ;; esac
RB="$TMP/rb"; mkdir -p "$RB/D1" "$RB/D2"
: > "$RB/D1/$RB_B"; : > "$RB/D2/$RB_B"; chmod +x "$RB/D1/$RB_B" "$RB/D2/$RB_B"
RB_TAIL="C:/Program Files/Git/bin/bash.exe;C:/Program Files/Git/usr/bin/bash.exe;bash"
rb_js=$(cd "$RB" && PATH="$RB/D1:$RB/D2" GOV_BASH=GB "$NODE" -e '
const cp = require("child_process"), path = require("path");
const root = path.dirname(process.env.PATH.split(path.delimiter)[0]), tried = [];
cp.spawnSync = (c) => c === "git" ? { status: 0, stdout: process.cwd() + "\n" } : (tried.push(c), { status: 1 });
try { require(process.argv[1]).readPolicy("runtime.agents-in-flight"); } catch (_e) { /* the refusal is expected */ }
console.log(tried.map((c) => c.split(root).join("F").split(path.sep).join("/")).join(";"));' "$ROOT/$POLICY_DIR/policy-mirror.js" 2>&1)
rb_py=$(cd "$RB" && PATH="$RB/D1:$RB/D2" GOV_BASH=GB "$REALPY_ABS" -B -c '
import os, subprocess, sys
sys.path.insert(0, sys.argv[1])
import resolve_bash
root, tried = os.path.dirname(os.environ["PATH"].split(os.pathsep)[0]), []
subprocess.run = lambda argv, **kw: tried.append(argv[0]) or subprocess.CompletedProcess(argv, 1)
resolve_bash.resolve_bash("x")
print(";".join(c.replace(root, "F").replace(os.sep, "/").replace(".EXE", ".exe") for c in tried))' "$HERE" 2>&1 | tr -d '\r')
[ "$rb_js" = "GB;F/D1/$RB_B;F/D2/$RB_B;$RB_TAIL" ] \
  || bad "the JS resolveBash order left the one TOOL-dGroundRules-81 states: $rb_js"; ok
[ "$rb_py" = "GB;F/D1/$RB_B;$RB_TAIL" ] \
  || bad "the canonical resolve_bash order left the one TOOL-dGroundRules-81 states: $rb_py"; ok

```

How it reads each side:

- **JS.** The stub follows `TOOL-dGroundRules-78`'s `p78.js`. `git` answers the current directory,
  and every other spawn is recorded and answers status 1. `readPolicy` then reaches `runShim`, which
  calls `resolveBash`, and refuses `no bash can see`. The module reads PATH when it loads, so PATH is
  set before node starts. The module is found through `resolve_kit_dir`, the way sections above find
  the `unattended` and `run-gates` kits (`tools/lib/resolve-python.test.sh:157-158`).
- **Python.** It imports the canonical `tools/lib/resolve_bash.py` from `$HERE`, never the
  `check_policy.py` copy, which the `resolve_bash_py` row already holds byte-identical to it. It
  stubs `subprocess.run` for that process.
- Both outputs spell the fixture root `F`, taken from the first PATH entry the program itself sees.
  That keeps the comparison free of how git-bash converts `/tmp` paths and of 8.3 short names.

The names `POLICY_DIR`, `NODE`, `RB`, `RB_B`, `RB_TAIL`, `rb_js` and `rb_py` appear nowhere else in
the file at `59f02fde9`. The §3 bans grade other files: §3 and §3b skip the files under
`$KIT_REL/resolve-python`, this one included. The `FOREIGN_PREFIX_PROBE` stop
(`tools/lib/resolve-python.test.sh:62`) comes before this section, so the foreign-prefix leg never
runs it.

### What this does not check

The section compares lists of candidates tried. It does not run a real bash or show which one a host
keeps. `TOOL-dGroundRules-81`'s AC1 probe covers the JS side keeping D2. It does not check the
`bash.exe`-before-`bash` order inside one PATH directory, for the git-bash reason above. It does not
grade `shutil.which`'s own differences from `fs.existsSync`, such as a directory named `bash`, which
`TOOL-dGroundRules-81` §4 records. It does not grade the copies of `resolve_bash` that return another
shape. On a host whose expected names differ from this node's, the section asserts the same order
with `bash` in place of `bash.exe` in the PATH slot.

### Alternatives rejected

- A `PARITY_ROWS` row, as `TOOL-dGroundRules-78` §8 named the ask. That table extracts a marked
  block and compares bytes (`tools/lib/resolve-python.test.sh:221-241`). A JS function and a Python
  one share no bytes. Sections `2b` to `2d` already hold two canonicals in two languages to one
  answer, so this unit follows that pattern.
- A policy fixture case. The brief allows one where the row cannot live in this suite, and it can.
  The `policy fixtures` leg is the build's slowest (budget 970, ceiling 1290), and the canonical
  this row reads lives in `tools/lib/`.
- Widening `resolve_bash` so both lists match exactly. `TOOL-dGroundRules-81` §4 "Alternatives
  rejected" keeps Python unchanged. This section asserts the relation as it stands.
- A Python order derived from `shutil.which` at run time. The row would then compare the canonical
  with itself. Both expected lists are written in the row instead, built from the one shared
  `RB_TAIL`.

### Rollout

The builder sets this spec's status from DEFERRED to INPROGRESS before its first write. Scratch-guard
admits writes under `ROUTED_PATHS` for a Tier-1 unit only at INPROGRESS, or at SPECCED once graded.
This unit builds after `TOOL-dGroundRules-81`. Built before it, AC1 reds as AC2's first break does.
No help page changes, because nothing a user runs behaves differently.

### Files touched (estimate)

- `tools/lib/resolve-python.test.sh`

## 5. Acceptance criteria

All commands run from the repository root of the pass's worktree. `p82.sh` runs section `2j` alone,
cut from the suite by its own header and the `# ---- 3. ` header after it. It runs the section's
code, not a copy. It copies the worktree's tracked `tools/lib` and `tools/policy` into the scratch
repository it is given, defines the suite's preamble (`HERE`, `ROOT`, `TMP`, `ok`, `bad`, `REALPY`,
`REALPY_ABS`, and `resolve_kit_dir` cut from the suite itself), and prints each `FAIL` line and then
the count and status. A second argument stages one break in the scratch copy. `js-narrow` puts
`onPath[0]` back for `...onPath`, the state at `59f02fde9`. `js-order` swaps the two Git for Windows
paths in `cands`. `py-add` adds `"sh"` after the bare `"bash"` in the canonical's candidates.
`py-omit` empties the canonical's PATH slot. A missing section prints `0 assertion(s), status 0`, so it never passes AC1.

```
cat > "$TEMP/p82.sh" <<'EOF'
d="$1"; rm -rf "$d"; mkdir -p "$d"
git ls-files -z -- tools/lib tools/policy | tar --null -T - -cf - | tar -xf - -C "$d"
git -C "$d" init -q
case "${2:-}" in
  js-narrow) sed -i 's/\.\.\.onPath, "C:/onPath[0], "C:/' "$d/tools/policy/policy-mirror.js" ;;
  js-order) sed -i 's#"C:/Program Files/Git/bin/bash.exe", "C:/Program Files/Git/usr/bin/bash.exe", "bash"\]#"C:/Program Files/Git/usr/bin/bash.exe", "C:/Program Files/Git/bin/bash.exe", "bash"]#' "$d/tools/policy/policy-mirror.js" ;;
  py-add) sed -i 's#"C:/Program Files/Git/usr/bin/bash.exe", "bash"\]#"C:/Program Files/Git/usr/bin/bash.exe", "bash", "sh"]#' "$d/tools/lib/resolve_bash.py" ;;
  py-omit) sed -i 's#shutil.which("bash") or "",#"",#' "$d/tools/lib/resolve_bash.py" ;;
esac
HERE="$d/tools/lib"; ROOT="$d"; TMP=$(mktemp -d); st=0; n=0
ok() { n=$((n+1)); }; bad() { echo "FAIL $1"; st=1; n=$((n+1)); }
. "$HERE/resolve-python.sh"; REALPY=$(resolve_python); REALPY_ABS=$(command -v "$REALPY")
eval "$(sed -n '/^resolve_kit_dir() {/,/^}/p' "$HERE/resolve-python.test.sh")"
eval "$(awk '/^# ---- 2j\./{f=1} /^# ---- 3\. /{f=0} f' "$HERE/resolve-python.test.sh")"
rm -rf "$TMP"; echo "$n assertion(s), status $st"
EOF
```

The expected lines below are this node's, a git-bash host, where the fixture name is `bash.exe`.
On another host each `bash.exe` in a fixture path reads `bash`. The suite's own `bad` counts a
failing assertion twice, so one failure prints `3 assertion(s)`. A scratch repository holding
`tools/lib` and `tools/policy` at `59f02fde9`, with `TOOL-dGroundRules-81`'s S1 line and this
section applied, was measured printing every line below. The green run took 1.4s.

Each staged break prints one `FAIL` line and then `3 assertion(s), status 1`. Its `FAIL` line is
given below, one per break. Each line opens with the break's name and `: `, which the run does not
print:

```
js-narrow: FAIL the JS resolveBash order left the one TOOL-dGroundRules-81 states: GB;F/D1/bash.exe;C:/Program Files/Git/bin/bash.exe;C:/Program Files/Git/usr/bin/bash.exe;bash
js-order: FAIL the JS resolveBash order left the one TOOL-dGroundRules-81 states: GB;F/D1/bash.exe;F/D2/bash.exe;C:/Program Files/Git/usr/bin/bash.exe;C:/Program Files/Git/bin/bash.exe;bash
py-add: FAIL the canonical resolve_bash order left the one TOOL-dGroundRules-81 states: GB;F/D1/bash.exe;C:/Program Files/Git/bin/bash.exe;C:/Program Files/Git/usr/bin/bash.exe;bash;sh
py-omit: FAIL the canonical resolve_bash order left the one TOOL-dGroundRules-81 states: GB;C:/Program Files/Git/bin/bash.exe;C:/Program Files/Git/usr/bin/bash.exe;bash
```

The `python resolver (behaviour + inline parity + idiom ban)` leg is a gate this pass may not run.
The main loop runs it at the close (§6).

- **AC1** — When `bash "$TEMP/p82.sh" "$TEMP/r82"` runs, it prints exactly one line, `2 assertion(s), status 0`.
  Red when: the section is missing or cut short. Then it prints `0 assertion(s), status 0`, or a
  count other than `2`.
- **AC2** — When `bash "$TEMP/p82.sh" "$TEMP/r82" js-narrow` runs, it prints the `js-narrow` line given above the criteria and `3 assertion(s), status 1`.
  When `bash "$TEMP/p82.sh" "$TEMP/r82" js-order` runs, it prints the `js-order` line given above the criteria and `3 assertion(s), status 1`.
  Red when: the JS assertion is weakened so it stops requiring the second PATH bash or the
  order of the tail, for example compared as a set or only by its first entry. Then either run
  prints `2 assertion(s), status 0`.
- **AC3** — When `bash "$TEMP/p82.sh" "$TEMP/r82" py-add` runs, it prints the `py-add` line given above the criteria and `3 assertion(s), status 1`.
  When `bash "$TEMP/p82.sh" "$TEMP/r82" py-omit` runs, it prints the `py-omit` line given above the criteria and `3 assertion(s), status 1`.
  Red when: the Python side reads anything but the canonical `tools/lib/resolve_bash.py`, for
  example the `check_policy.py` copy or an order typed into the section. Then the canonical's
  staged break goes unseen and both runs print `2 assertion(s), status 0`.

## 6. Gates

`python resolver (behaviour + inline parity + idiom ban)` · `foreign-prefix parity (every self-test at three prefixes)` · `spec tokens (a spec's own names resolve)` · `memory hygiene`

`derive_guarded_legs` over `tools/gate-legs.json` at `59f02fde9` names no non-broad guarded leg for
`tools/lib/resolve-python.test.sh`. Every guard it trips is broad: `tools/lib/` (37 legs) and
`tools/` (12 legs), the same two `TOOL-dGroundRules-81` and spec-tokens list as excluded. This was
derived by reading the manifest's guards with the function's own breadth rule, more than 5 legs.

Two legs read the file without a non-broad guard. `python resolver (behaviour + inline parity + idiom ban)`
runs it (its argv, `tools/gate-legs.json:320-326`). It gains two assertions and about two process
starts. Its budget row (`tools/run-gates/selftest-budgets.txt:91`, 150, from a worst reading of 99s)
and its ceiling of 350 stand, and no floor or pinned count moves. `foreign-prefix parity (every self-test at three prefixes)`
runs it with `FOREIGN_PREFIX_PROBE=1`, which stops at line 62, before this section, so that leg does
not change.

`tools/policy/check_policy.py` is not touched, so the `policy fixtures` leg does not grow, and its
budget of 970 and ceiling of 1290 stand.

New arm: tools/lib/resolve-python.test.sh · covers AC1 AC2 AC3 · section 2j; `onPath[0]` staged for `...onPath` in policy-mirror.js, or the canonical's PATH slot staged empty, reds it by name · none

## 7. Open questions

none

## 8. Revision log

- rev-1 · 2026-10-25 · initial draft from the closing review's round-2 finding L2 (id 6) and this
  unit's spec brief, grounded at `59f02fde9`. The premise holds: no suite, fixture or row reads
  `resolveBash`. The order is the one `TOOL-dGroundRules-81` §4 states. That spec was not at the
  base. Its draft sat in the spec folder when this one was written, and its order matches its
  brief's direction: the JS scan of every PATH bash comes back, and Python stays unchanged. The
  skeptic-SOUND fix is taken in the widened form the report allows. The assertion is the relation
  between the two orders, because only the JS side widens. The section was measured in a scratch
  repository holding `tools/lib` and `tools/policy` at `59f02fde9`, with `TOOL-dGroundRules-81`'s
  code line and this section applied. The green run and each of the four staged breaks printed what
  §5 states. A first fixture with an extensionless `bash`, as `p78.js` and `p81.js` use, left the
  Python side blind to the PATH slot on Windows. A second, with `bash.exe` and `bash` in one
  directory, wrote only one file under git-bash. §4 records both. The review report, the brief and
  `TOOL-dGroundRules-81`'s spec were untracked when this draft was written:

```
memory/builds/dGroundRules/reviews/2026-10-25-review-TOOL-dGroundRules-72-79-closing-diff-round2.md
memory/builds/dGroundRules/prompts/2026-10-25-prompt-TOOL-dGroundRules-82-spec-brief.md
memory/builds/dGroundRules/spec/2026-10-25-spec-TOOL-dGroundRules-81.md
```

The report's left-shift class is the gotcha `rule-stated-with-no-check-that-fails`, and the section
is its gate. The report's fallback, a bug-class checklist entry, applies only where no row is built,
so it is not filed.

## 9. Reuse audit

This unit builds no mechanism. It extends the seam `tools/lib/resolve-python.test.sh` already uses to
hold two canonicals in two languages to one answer: sections `2b` (`:243-264`), `2c` and `2d` run each
canonical over one table and compare outputs. The JS stub reuses `TOOL-dGroundRules-78`'s `p78.js`
shape. The policy kit is found through the suite's inline `resolve_kit_dir`, as `:157-158` find two
sibling kits.
`python tools/codebase-map/reuse_lookup.py "compare two implementations of one resolver by candidate order in a parity table"`
ranked `resolve` (fan-in 71), `resolve_kit_dir` (a seam, which this section calls) and `resolve_bash`
(fan-in 5, the canonical this section reads). None compares two resolvers' orders. The recall probe
returned the `TOOL-dGroundRules-78` brief that first named this ask, `TOOL-dSettledRoster-3` and
`TOOL-dSettledRoster-6` on the `resolve_bash` copies, and `TOOL-dGroundRules-81`'s spec. No record
holds a cross-language order check.

Recall terms used: `python tools/memory-recall/query.py "resolver parity row candidate order JS resolveBash canonical resolve_bash" --terms "resolveBash resolve_bash parity PARITY_ROWS candidate order spawnSync stub"`
