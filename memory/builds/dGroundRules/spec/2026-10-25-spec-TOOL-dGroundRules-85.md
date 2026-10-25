# TOOL-dGroundRules-85 — both size-cap enforcers split the budgets answer once with builtins, so the memory-hygiene and manifest-check probes fork within their ceilings again

**Status:** CLOSED · rev-1 · 2026-10-25 · node d · Tier-1 · base cae57b1d · streams tooling · order 32

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-prompt-TOOL-dGroundRules-85-1-spec-writer.md](../prompts/2026-10-25-prompt-TOOL-dGroundRules-85-1-spec-writer.md) | journal | — |
| [2026-10-25-prompt-TOOL-dGroundRules-85-spec-brief.md](../prompts/2026-10-25-prompt-TOOL-dGroundRules-85-spec-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

The close's bar pre-check at `cae57b1d8` redded the spawn budget leg. The memory-hygiene probe forks
240 against its ceiling 189, and the manifest-check probe forks 105 against 90. Both were at their
ceilings at the run's base `3c2b69be4`. Every added fork comes from the per-cap budget readers
`TOOL-dGroundRules-9` added (`69aa76517`). This unit reads the budgets answer once and splits it with
builtins in both enforcers, and neither checker's verdict moves.

The readers alone cannot reach 90 for manifest-check. Their measured floor is 96, because the probe
also pays 6 forks to look for the policy kit, which `resolve_kit_file` must do under the kit's
location contract (§4 "The floor"). So the unit also counts check 6's dead-literal listing without a
pipe, which brings manifest-check to 74. Memory hygiene lands at exactly 189, one fork of which comes
from its `HERE` derivation.

## 2. Scope (IN)

- **S1** — `read_cap_modes` in `tools/memory-tree/check-memory-hygiene.sh` (`:505-533`) reads
  `.memory-tree.conf` once for the ten `legacy:` tests, in place of a `grep -qE` per cap (`:511`). It
  splits the budgets answer once into three associative arrays, `CAP_MODE`, `CAP_RULE` and
  `CAP_VALUE`. Check 6's mode string (`:1099`), check 7's two modes (`:1213`) and
  `check_cap_findings` (`:546`) read those arrays, so the two per-cap functions `read_cap_mode` and
  `read_cap_rule` (`:534-535`) and the `CAP_ANSWERS` variable have no caller and leave the file. The
  text is §4 "Memory hygiene". Observed by AC1, AC3 and AC5.
- **S2** — The engine's `HERE` derivation (`:300`) takes the form
  `tools/branch-reconcile/adopt-branch-reconcile.sh:25` uses, with one fork where it spent two.
  Observed by AC1. Because the derivation was the file's only `path-subst` site, the file's
  `path-subst` row in `memory/project/spawn-idiom-sites.txt` is taken out. That row is NOT OBSERVED
  here: the `shell hygiene (a fork spent on builtin work)` leg joins the registry to its scan in both
  directions, and the main loop runs it at the close.
- **S3** — `skills/session-kickoff/manifest-check.sh` sets its three cap values from one builtin
  split of `MB_ANSWERS`, in place of three `$(read_budget_field …)` reads (`:1339-1341`). The text is
  §4 "Manifest-check". `read_budget_field` and `read_budget_rule` stay, because only
  `check_budget_breach` calls them, on a breach. Observed by AC2 and AC4.
- **S4** — Check 6 of the same file (`:1464`) recounts a watch literal from one `git ls-files`
  substitution and counts its lines by parameter expansion, in place of a substitution that pipes
  the listing through `wc -l` and `tr`. It still asks git for a literal the shared listing counted
  zero, and for every literal when a name came back quoted. The text is §4 "Manifest-check".
  Observed by AC2 and AC4.
- **S5** — The `manifest-check` row of `memory/project/fork-ceilings.txt` (`:20`) goes from ceiling 90
  to 74, a lowering of 16, with the reason extended as §4 "The ceilings" gives. The `memory-hygiene`
  row (`:19`) stays at 189. Observed by AC1 and AC2.

## 3. Non-goals (OUT)

- Legs 1-5 and 7-10 of the triage, which `TOOL-dGroundRules-84` and `TOOL-dGroundRules-86` own.
- Any other probe's fork count, and any row of `memory/project/fork-ceilings.txt` but `manifest-check`.
- The budgets' values, the policy kit and its reader contract. Neither enforcer reads
  `.governance/policy.toml` itself.
- `resolve_kit_file` and its rungs (`skills/session-kickoff/manifest-check.sh:854-867`). The probe's
  remaining 6 added forks are that lookup (§4 "The floor").
- The `CAP_NOTE` and `MB_NOTE` refusal lines. Each forks only when the reader refused, and once.
- The other rows `TOOL-dGroundRules-84` writes in `memory/project/spawn-idiom-sites.txt`. This unit
  names its one row by file and class, `tools/memory-tree/check-memory-hygiene.sh` `path-subst`, and
  writes it against the registry `-84` leaves.

### Edges

none

## 4. Design

### Evidence

Measured at `cae57b1d8` and in a scratch clone at `3c2b69be4`, on node d under bash 5.3.9, with the
spawn-budget checker's own `--only <id> --sites`. These counts are pinned to those two commits. The
sites were mapped from base lines to head lines by a line diff of each file, so a site whose line
only moved is not counted as added.

| Probe | Base `3c2b69be4` | `cae57b1d8` | Ceiling |
|---|---|---|---|
| `memory-hygiene` | 189 | 240 | 189 |
| `manifest-check` | 90 | 105 | 90 |

Memory hygiene, +51:

| Site at `cae57b1d8` | Added | What forks |
|---|---|---|
| `check-memory-hygiene.sh:524` | 1 | the one python start that asks the policy kit for all ten caps |
| `check-memory-hygiene.sh:527` | 20 | ten `_v=$(printf …)` value reads piped into `awk`, two traced children each |
| `check-memory-hygiene.sh:534` | 20 | the body of `read_cap_mode`, two traced children for each of ten calls |
| `check-memory-hygiene.sh:1141` | 8 | the eight `$(read_cap_mode …)` substitutions of check 6's mode string at `:1099`, traced at the command's last line |
| `check-memory-hygiene.sh:1247` | 2 | check 7's two `$(read_cap_mode …)` substitutions at `:1213` |
| `:1100` and `:1104` | +1 and -1 | the same awk fork, first traced one line earlier; net 0 |

The per-key `grep -qE` at `:511` adds no counted fork. An external command run directly forks a
child that traces nothing before it execs, and the counter cannot see such a child
(`tools/gate-lint/fork-count.sh:42-45`). It is still ten process starts a run, so S1 takes it out too.

Manifest-check, +15:

| Site at `cae57b1d8` | Added | What forks |
|---|---|---|
| `manifest-check.sh:856` | 1 | `resolve_python` inside `resolve_kit_file` |
| `manifest-check.sh:859` | 2 | `resolve_kit_dir`, once per anchor, `$MC_DIR` and `$ROOT` |
| `manifest-check.sh:863` | 1 | the tracked-anchor rung's `git ls-files` |
| `manifest-check.sh:1322` | 1 | `_mb_py=$(resolve_python …)` |
| `manifest-check.sh:1323` | 1 | `_mb_pk=$(resolve_kit_file policy budgets.py)` |
| `manifest-check.sh:1337` | 6 | the body of `read_budget_field`, two traced children for each of three calls |
| `manifest-check.sh:1339-1341` | 3 | the three `$(read_budget_field …)` substitutions |

The fixture's scratch repository tracks no policy kit, so `_mb_pk` is empty and the no-kit branch is
taken. The budgets python start never runs in this probe, though the triage counted it.

### The floor

Reading the answer once in-shell recovers 50 of memory hygiene's 51, which leaves 190 against 189.
The fork that remains is the python start, and the switch needs it. S2 recovers one fork that predates
the switch, at `:300`, where `$(dirname "$0")` nests inside the `$(cd … && pwd)` substitution.

For manifest-check the readers recover 9 of 15, which leaves 96 against 90. The other 6 are the
policy kit lookup. Its comment (`:1315`) says the kit "is found as every sibling this kit reads is,
by `resolve_kit_file`": a receipt row, then the probes beside this kit, then the one tracked anchor.
The no-kit branch is known only after that lookup. Asking for `_mb_py` only once a kit is found saves
one more and leaves 95, still over. Reading `.governance/policy.toml` from the shell is ruled out by
the policy kit's reader contract. `resolve_caps` reads the policy file once, at the landed revision,
through `policy.read_revision` and `policy.resolve_read`, and the mode comes from the census and
`budgets.enforce` (`tools/policy/budgets.py:14-24`). An absent policy file resolves through
`RESOLUTION_ORDER` (`tools/policy/policy.py:739-749`), so the file's absence does not say the kit's
mode. This unit keeps that contract, and keeps the lookup.

So S4 takes its saving where the probe pays most: check 6's recount at `:1464`, 33 forks. In the
fixture all eleven watch literals are dead. Each spends a three-stage pipeline in a substitution, and
S4 spends one substitution. That is 22 forks, and the probe lands at 96 - 22 = 74. The saving is real
only where a literal counts zero. In a live tree the shared listing counts every literal, and the
recount never runs.

### Memory hygiene

`CAP_ANSWERS="" CAP_NOTE="" CAP_READ=0` (`:504`) becomes the following two lines:

```
CAP_NOTE="" CAP_READ=0
declare -A CAP_MODE=() CAP_RULE=() CAP_VALUE=()
```

In `read_cap_modes`, the `local` line gains `_l _c _r _set=" " _ifs`. The conf is read once, before
the `for _p in $CAP_KEYS` loop:

```
  if [ -f "$ROOT/.memory-tree.conf" ]; then
    while IFS= read -r _l || [ -n "$_l" ]; do
      [[ $_l =~ ^[[:space:]]*(export[[:space:]]+)?([A-Za-z_][A-Za-z0-9_]*)= ]] && _set+="${BASH_REMATCH[2]} "
    done < "$ROOT/.memory-tree.conf"
  fi
```

The `grep -qE` line inside the loop (`:511`) becomes:

```
    case "$_set" in *" ${_p#*:} "*) _how=legacy ;; esac
```

The success branch, from `CAP_ANSWERS=$_out` through the loop's `done` (`:525-529`), becomes:

```
    _ifs=$IFS; IFS=$'\n'; set -f
    for _l in $_out; do
      case "$_l" in
        'budgets: '*' · '*) _c=${_l#budgets: }; _r=${_c#* · }; CAP_RULE[${_c%% · *}]=${_r%% · *} ;;
        *$'\t'*)
          _c=${_l%%$'\t'*}; _r=${_l#*$'\t'}; _v=${_r%%$'\t'*}; _r=${_r#*$'\t'}; CAP_MODE[$_c]=${_r%%$'\t'*}; CAP_VALUE[$_c]=$_v ;;
      esac
    done
    set +f; IFS=$_ifs
    for _p in $CAP_KEYS; do
      _v=${CAP_VALUE[${_p%%:*}]-}
      case "$_v" in ''|*[!0-9]*) ;; *) eval "${_p#*:}=\$_v" ;; esac
    done
```

The lines `read_cap_mode() …` and `read_cap_rule() …` (`:534-535`) are taken out. In
`check_cap_findings`, `_r=$(read_cap_rule "$_cap")` (`:546`) becomes `_r=${CAP_RULE[$_cap]-}`. In
check 6's `-v modes=` string (`:1099`) and check 7's `-v em=` and `-v bem=` (`:1213`), each
`$(read_cap_mode <cap>)` becomes `${CAP_MODE[<cap>]:-refuse}` for the same cap name. The comment
block above the switch (`:494-502`) gains one closing sentence:

```
# The answer is split ONCE, with builtins, into CAP_MODE, CAP_RULE and CAP_VALUE, and the conf is
# read once for the ten `legacy:` tests: a substitution per cap cost 50 forks a run (TOOL-dGroundRules-85).
```

The `HERE` line (`:300`) becomes:

```
HERE=.; [[ $0 == */* ]] && HERE=${0%/*}; HERE="$(cd "$HERE" && pwd)"
```

Each split matches what the awk it stands in for printed. Each tab row is
`<cap>\t<value>\t<mode>\t<source>`, and each `--explain` line is `budgets: <cap> · <rule> · <reason>`
(`tools/policy/budgets.py:360-365`). The awk printed a row's second field as the value and its third
as the mode, and an explain line's second ` · ` segment as the rule. A cap with
no row keeps its declared value, and its mode reads `refuse`, as `${_m:-refuse}` did. The refused
branch leaves all three arrays empty, so every mode is `refuse` and every rule is empty, as an empty
`CAP_ANSWERS` gave before. The split is a word-split `for` with globbing off, as check 6 of
manifest-check splits its listing (`skills/session-kickoff/manifest-check.sh:1456-1461`), and not a
loop fed by a here-string. A here-string would raise the file's `<<<` row in
`memory/project/substitution-fed-loops.txt`, which counts sites in both directions. The conf read is
fed by a file, which that leg does not count.

### Manifest-check

The three `_v=$(read_budget_field …)` lines (`:1339-1341`) become:

```
# The three values from ONE builtin split of the answer, never a substitution per cap (TOOL-dGroundRules-85).
_mb_ifs=$IFS; IFS=$'\n'; set -f
for _l in $MB_ANSWERS; do
  case "$_l" in *$'\t'*) ;; *) continue ;; esac
  _v=${_l#*$'\t'}; _v=${_v%%$'\t'*}
  case "$_v" in ''|*[!0-9]*) continue ;; esac
  case "${_l%%$'\t'*}" in
    manifest-bytes) MAX_MANIFEST_BYTES=$_v ;;
    manifest-line) MANIFEST_LINE_MAX=$_v ;;
    manifest-trap) MANIFEST_TRAP_MAX=$_v ;;
  esac
done
set +f; IFS=$_mb_ifs
```

Check 6's recount line (`:1464`) becomes:

```
    # A literal the listing counted zero, or any name git quoted, is asked of git alone, its lines
    # counted by expansion, not by `wc -l` and `tr` (TOOL-dGroundRules-85).
    if [ "$n" -eq 0 ] || [ -n "$_c6q" ]; then
      _c6one=$(git ls-files -- "$w" 2>/dev/null); _c6nl=${_c6one//[!$'\n']/}
      n=0; [ -z "$_c6one" ] || n=$(( ${#_c6nl} + 1 ))
    fi
```

The condition is the old one's negation by De Morgan, so git is asked in the same cases. The
substitution strips the listing's trailing newline, so a listing of k names holds k - 1 newlines, and
`wc -l` printed k. Manifest-check gains no associative array, so it asks no more of bash than it did.
Memory hygiene already declares several (`tools/memory-tree/check-memory-hygiene.sh:398`).

### The ceilings

The `manifest-check` row's ceiling field goes from `90` to `74`, and its reason gains, after
`measured 90 three times on node a under bash 5.3, 2026-10-13`:

```
; lowered 90 -> 74 at TOOL-dGroundRules-85, which reads the budgets answer with builtins and counts check 6's dead-literal recount without a pipe, measured 74 on node d under bash 5.3
```

The builder measures the row three times before writing it and writes the date it measured on. The
leg reds a ceiling more than max(3, 5 %) above its count
(`memory/project/fork-ceilings.txt:12-13`), so 90 over a measured 74 must be lowered. The
`memory-hygiene` row measures exactly its ceiling, 189, and is not edited.

The scan's other rows for these two files stay. `read_budget_field`, `read_cap_mode` and
`read_cap_rule` pipe into `awk`, and check 6's recount pipes `git` into `wc`. Neither shape is a
`var-pipe` site, which needs a `printf` or `echo` of one expansion piped into a counting command
(`tools/gate-lint/sh_hygiene.py:643-647`). Their callers were near misses of `pure-fn-subst`, because
each body pipes. So only the `path-subst` row of S2 moves.

### Prototype

The text above was applied by a scratch script to a clone at `cae57b1d8`, with the `manifest-check`
row at 74. There, `--only memory-hygiene` printed `ok memory-hygiene · measured 189 · ceiling 189`
four times running, and `--only manifest-check` printed `measured 74` four times. The verdict probe
of §5, run over the clone and over `cae57b1d8`, printed byte-identical findings for both checkers.

### What this does not check

AC3 and AC4 compare five scratch trees: under `warn`, under `refuse`, and with a cap held in both
homes, so the policy reader refuses. They do not cover a pinned cap, a family cap, a build README or a
dossier, or a name git quotes in check 6. A pinned or family cap changes only the reader's answer,
which both sides split the same way. The fork counts are a lower bound. A python or git child the
substitution starts is invisible, so AC1 and AC2 do not see the ten conf greps S1 takes out; AC5
observes that. Only the bar runs the shell-hygiene legs over the registries.

### Alternatives rejected

- Raising either ceiling. The rows shrink only.
- Reading `budgets.*` from `.governance/policy.toml` in the shell, which would skip the python start
  and the lookup. It breaks the reader contract §4 "The floor" names, and it cannot see the census's
  mode or the landed revision.
- A fork-free precheck that skips the lookup when no `.governance/policy.toml` exists. An installed
  kit with no policy file answers its own default mode, which the no-kit branch does not.
- Asking for `_mb_py` only after a kit is found. It saves one fork, which leaves 95, and S4 alone
  brings the probe under 90.
- Folding `resolve_kit_file`'s rungs into one python call. It touches the one body every sibling read
  uses, and its floor is still 92: one `resolve_python` and one python substitution.
- A here-string split with `while read`. It raises the `<<<` count the substitution-fed-loop leg
  pins.

### Rollout

The builder sets this spec's status from DEFERRED to INPROGRESS before its first write. Scratch-guard
admits writes under `ROUTED_PATHS` for a Tier-1 unit only at INPROGRESS, or at SPECCED once graded.
`TOOL-dGroundRules-84` builds first and writes other rows of `memory/project/spawn-idiom-sites.txt`.
This unit takes out its one row by file and class. Both checkers ship, so `kit epoch` and
`verdict epoch` print their bumps as owed at the lander, though no verdict moves. Both files are on the
kickoff manifest's `watch:` list, which `TOOL-dGroundRules-86` re-audits after this unit lands.

### Files touched (estimate)

- `tools/memory-tree/check-memory-hygiene.sh`
- `skills/session-kickoff/manifest-check.sh`
- `memory/project/fork-ceilings.txt`
- `memory/project/spawn-idiom-sites.txt`

## 5. Acceptance criteria

All commands run from the repository root of the pass's worktree, in Git Bash, with `$TEMP` short:
under a deeper directory a scratch clone's git objects pass Windows' 260-character path limit. The
setup makes three clones of the worktree's HEAD. `o85` holds both checkers as they stood at
`cae57b1d8`, `k85` holds the worktree's checkers with two staged breaks, and the worktree itself holds
the change.

```
rm -rf "$TEMP/o85" "$TEMP/k85"; H=$(git rev-parse HEAD)
git clone -q --no-checkout . "$TEMP/o85" && git -C "$TEMP/o85" checkout -q "$H"
git -C "$TEMP/o85" show cae57b1d8:tools/memory-tree/check-memory-hygiene.sh > "$TEMP/o85/tools/memory-tree/check-memory-hygiene.sh"
git -C "$TEMP/o85" show cae57b1d8:skills/session-kickoff/manifest-check.sh > "$TEMP/o85/skills/session-kickoff/manifest-check.sh"
git clone -q --no-checkout . "$TEMP/k85" && git -C "$TEMP/k85" checkout -q "$H"
cp tools/memory-tree/check-memory-hygiene.sh "$TEMP/k85/tools/memory-tree/"
cp skills/session-kickoff/manifest-check.sh "$TEMP/k85/skills/session-kickoff/"
sed -i 's/:-refuse}/:-warn}/g' "$TEMP/k85/tools/memory-tree/check-memory-hygiene.sh"
sed -i 's/manifest-line) MANIFEST_LINE_MAX=/manifest-line) MANIFEST_TRAP_MAX=/' "$TEMP/k85/skills/session-kickoff/manifest-check.sh"
```

`v85.sh` runs one checker of a given tree over scratch repositories whose budgets pass and refuse.
For `mh` it builds three: a guide of 8 lines under `budgets.guide-lines = 3` and a 402-character
README entry, with `budgets.enforce` set to `warn` and then `refuse`, and a third that sets
`budgets.index-bytes` while the conf holds `INDEX_CAP_BYTES`, so the policy reader refuses. For `mc`
it builds two, each holding the worktree's policy kit and this repository's manifest under
`budgets.manifest-line = 60`, with `budgets.enforce` set to `warn` and then `refuse`. It elides both
paths, drops the lines that carry each scratch repository's own seed sha or a cache count, and masks
a bash error's line number. In a tree holding no spec, the hygiene engine prints an
`ALFORM: unbound variable` error at `cae57b1d8` and at `3c2b69be4` alike. The masking keeps that
error equal on both sides.

```
cat > "$TEMP/v85.sh" <<'EOF'
# v85.sh <gov tree> <scratch dir> <mh|mc> -- one checker's findings over scratch trees whose budgets
# pass and refuse, paths elided, seed shas and check 26's cache line dropped, error line numbers masked.
G=$(cd "$1" && pwd); S="$2"; rm -rf "$S"; mkdir -p "$S"; S=$(cd "$S" && pwd)
seed() { git init -q -b main "$1" && git -C "$1" config user.email t@t.test && git -C "$1" config user.name t && git -C "$1" config core.autocrlf false; }
land() { git -C "$1" add -A && git -C "$1" commit -q -m seed; }
show() { o=${2//$S/<S>}; o=${o//$G/<G>}; printf '== %s\n' "$1"; printf '%s\n' "$o" | sed -E 's/: line [0-9]+:/: line N:/' | grep -vE '^row-grammar: check 2[78] |check 26 '; }
long=$(printf '%0400d' 0)
if [ "$3" = mh ]; then
  for how in warn refuse both; do
    t="$S/mh-$how"; seed "$t"; cp "$G/.memory-tree.conf" "$t/"; mkdir -p "$t/memory/guides" "$t/.governance"
    printf '%s\n' '# memory' "- $long" > "$t/memory/README.md"
    gd="$t/memory/guides"; printf 'line %s\n' 1 2 3 4 5 6 7 8 > "$gd/g.md"
    case $how in
      both) printf '%s\n' '[budgets]' 'enforce = "warn"' 'pinned = []' 'index-bytes = 100' > "$t/.governance/policy.toml" ;;
      *) printf '%s\n' '[budgets]' "enforce = \"$how\"" 'pinned = []' 'guide-lines = 3' > "$t/.governance/policy.toml" ;;
    esac
    land "$t"
    o=$(cd "$t" && bash "$G/tools/memory-tree/check-memory-hygiene.sh" 2>&1); show "mh-$how rc=$?" "$o"
  done
else
  for how in warn refuse; do
    t="$S/mc-$how"; seed "$t"; mkdir -p "$t/memory/guides" "$t/tools" "$t/.governance"
    cp -r "$G/tools/policy" "$t/tools/"; pk="$t/tools/policy"; rm -rf "$pk/__pycache__"; cp "$G/memory/guides/SESSION-KICKOFF.md" "$t/memory/guides/"
    printf '%s\n' '[budgets]' "enforce = \"$how\"" 'pinned = []' 'manifest-line = 60' > "$t/.governance/policy.toml"
    land "$t"
    o=$(cd "$t" && bash "$G/skills/session-kickoff/manifest-check.sh" memory/guides/SESSION-KICKOFF.md 2>&1); show "mc-$how rc=$?" "$o"
  done
fi
EOF
```

Each figure below is pinned: measured at `cae57b1d8` with §4's text applied to a scratch clone, on
node d under bash 5.3.9.

- **AC1** — When `bash tools/gate-lint/fork-count.sh memory/project/fork-ceilings.txt . --only memory-hygiene` runs, it prints `fork-count: ok memory-hygiene · measured 189 · ceiling 189 · base 219` and exits 0.
  Red when: the graded tree holds the checker as it stood at `cae57b1d8`. Then `bash tools/gate-lint/fork-count.sh memory/project/fork-ceilings.txt "$TEMP/o85" --only memory-hygiene` prints `fork-count: RED memory-hygiene · measured 240 · ceiling 189 · delta +51` and exits 1.
- **AC2** — When `bash tools/gate-lint/fork-count.sh memory/project/fork-ceilings.txt . --only manifest-check` runs, it prints `fork-count: ok manifest-check · measured 74 · ceiling 74 · base 108` and exits 0.
  Red when: the graded tree holds the checker as it stood at `cae57b1d8`. Then `bash tools/gate-lint/fork-count.sh memory/project/fork-ceilings.txt "$TEMP/o85" --only manifest-check` prints `fork-count: RED manifest-check · measured 105 · ceiling 74 · delta +31` and exits 1.
- **AC3** — When `bash "$TEMP/v85.sh" "$TEMP/o85" "$TEMP/v85s" mh > "$TEMP/v85-mh-old.txt"` and then `bash "$TEMP/v85.sh" . "$TEMP/v85s" mh > "$TEMP/v85-mh-new.txt"` have run, `diff "$TEMP/v85-mh-old.txt" "$TEMP/v85-mh-new.txt"` prints nothing and exits 0. The new file holds, under `mh-warn`, a line opening `BUDGET WARN — guide-lines ·` and ending `8 lines over 3 · budgets.enforce is warn · check 6`, then under `mh-refuse` the scratch guide's line ending `(56B 8L > 98304B/3L) · budgets.enforce is refuse`, then under `mh-both` a line opening `HYGIENE — no policy kit answered the size caps` and ending `budgets.index-bytes is held in both homes`, followed by `memory/README.md:2 (402 chars > 300)`.
  Red when: a cap the reader did not answer defaults to `warn`. Then `bash "$TEMP/v85.sh" "$TEMP/k85" "$TEMP/v85s" mh > "$TEMP/v85-mh-break.txt"` and `diff "$TEMP/v85-mh-old.txt" "$TEMP/v85-mh-break.txt"` print, under `mh-both`, the old side's note and check 7 refusal against `BUDGET WARN — entry-chars · memory/README.md · 402 chars over 300 ·  · check 7` on the new side, and exit 1.
- **AC4** — When `bash "$TEMP/v85.sh" "$TEMP/o85" "$TEMP/v85s" mc > "$TEMP/v85-mc-old.txt"` and then `bash "$TEMP/v85.sh" . "$TEMP/v85s" mc > "$TEMP/v85-mc-new.txt"` have run, `diff "$TEMP/v85-mc-old.txt" "$TEMP/v85-mc-new.txt"` prints nothing and exits 0. The new file holds `BUDGET WARN — manifest-line · memory/guides/SESSION-KICKOFF.md · 349 bytes over 60 · budgets.enforce is warn` under `mc-warn`, eleven `MANIFEST check 6 FAILED — watch pathspec` lines under each tree, and `MANIFEST check 8 FAILED — a manifest line is over the 60-byte limit; wrap the prose or move the detail out (budgets.enforce is refuse):` under `mc-refuse`.
  Red when: the split hands `manifest-line`'s value to the wrong cap. Then `bash "$TEMP/v85.sh" "$TEMP/k85" "$TEMP/v85s" mc > "$TEMP/v85-mc-break.txt"` and `diff "$TEMP/v85-mc-old.txt" "$TEMP/v85-mc-break.txt"` print the `BUDGET WARN — manifest-line` line and the check 8 refusal on the old side only, and exit 1.
- **AC5** — When `git grep -n '_how=legacy' -- tools/memory-tree/check-memory-hygiene.sh` runs, it prints one line, and that line holds `case "$_set" in` and no `grep`.
  Red when: the conf is still grepped once per cap. Then `git grep -n '_how=legacy' cae57b1d8 -- tools/memory-tree/check-memory-hygiene.sh` prints the line numbered 511, which opens `grep -qE`.

## 6. Gates

`spawn budget (forks per hot entrypoint)` · `shell hygiene (a fork spent on builtin work)` · `shell hygiene (a loop fed by a command substitution)` · `memory-hygiene self-test` · `manifest-check self-test` · `scratch-guard self-test` · `lexicon naming predicates` · `policy fixtures` · `recall floor` · `recall floor arms` · `kickoff-manifest ratchet` · `verdict epoch (kit version dates the engine)` · `kit epoch (shipped bytes move, the version moves)` · `spec tokens (a spec's own names resolve)` · `memory hygiene`

Run through `derive_guarded_legs` at `cae57b1d8`, `python tools/check-spec-tokens.py --legs-for`
names these non-broad guarded legs for the four files touched.
`tools/memory-tree/check-memory-hygiene.sh` trips `policy fixtures` through its own exact line.
`skills/session-kickoff/manifest-check.sh` trips `manifest-check self-test`,
`scratch-guard self-test` and `lexicon naming predicates` through `skills/session-kickoff/`, and
`policy fixtures` through its own exact line. Both registries trip `recall floor` and
`recall floor arms` through `memory/`. Every other leg it prints for the hygiene engine trips on a
broad guard. `memory-hygiene self-test` is one of those, named here because it runs the engine this
unit edits.

The unguarded legs named beside them read what this unit changes:

- `spawn budget (forks per hot entrypoint)` grades both rows. AC1 and AC2 run its two probes.
- `shell hygiene (a fork spent on builtin work)` joins `memory/project/spawn-idiom-sites.txt` to its
  scan. The hygiene engine's `path-subst` count goes from 1 to 0, so its row is taken out, and no
  other row of either file moves (§4 "The ceilings").
- `shell hygiene (a loop fed by a command substitution)` reads both files. Neither gains a here-string
  or heredoc loop, so the `<<<` row of 8 for the hygiene engine stays.
- `kickoff-manifest ratchet` runs manifest-check over this repository's manifest. It is red at
  `cae57b1d8` on check 9, which `TOOL-dGroundRules-86` owns, and this unit adds one more watched
  commit to that count.
- `verdict epoch` and `kit epoch` read the shipped bytes of the memory-tree kit and the kickoff skill
  and print their bumps as owed at the lander.
- `memory hygiene` reads this spec.

No suite arm is added or moved. The one pinned count that moves is the `manifest-check` ceiling,
90 to 74, by S5. The `path-subst` row of S2 leaves the registry with its site.

## 7. Open questions

none

## 8. Revision log

- rev-1 · 2026-10-25 · initial draft from this unit's spec brief, grounded at `cae57b1d8`. Both probes
  were measured with the spawn-budget checker's own `--only <id> --sites`, at HEAD and in a scratch
  clone at the base `3c2b69be4`, and each added fork was attributed to its line through a base-to-head
  line map. The measurement corrects the triage in two places. The per-key `grep -qE` costs no counted
  fork, and the manifest-check probe never starts the budgets python, because its fixture holds no
  policy kit. The readers alone reach 190 and 96, so the design adds one older fork in the hygiene
  engine (`:300`) and check 6's dead-literal recount in manifest-check. The main loop may prefer to
  rule on the second, because its saving lands only where a watch literal is dead, which the probe's
  fixture makes of every literal. A prototype of §4 on a scratch clone measured 189 and 74 four times,
  and its verdicts matched `cae57b1d8` byte for byte over all five scratch trees. A follow-up the main
  loop may want: in a scratch tree holding no spec, the hygiene engine prints
  `ALFORM: unbound variable` near `:3393` at both commits measured. The brief and this role's prompt,
  untracked when this draft was written:

```
memory/builds/dGroundRules/prompts/2026-10-25-prompt-TOOL-dGroundRules-85-spec-brief.md
memory/builds/dGroundRules/prompts/2026-10-25-prompt-TOOL-dGroundRules-85-1-spec-writer.md
```

## 9. Reuse audit

Every form here is one the tree already holds. The split reads the policy kit's own answer format,
`budgets.py resolve --explain` (`tools/policy/budgets.py:360-365`), through the one python start
`TOOL-dGroundRules-9` already makes, and `resolve_caps` stays the only reader of the policy file. The
word-split `for` with globbing off is check 6's own idiom (`skills/session-kickoff/manifest-check.sh:1456-1461`).
The `HERE` derivation is `tools/branch-reconcile/adopt-branch-reconcile.sh:25`, which
`TOOL-dGroundRules-84` applies elsewhere. The associative arrays follow the hygiene engine's own
`declare -A` sets (`tools/memory-tree/check-memory-hygiene.sh:398`). `resolve_kit_file` and
`read_budget_field` stay as they are.
`python tools/codebase-map/reuse_lookup.py "parse the policy budgets resolve answer once in shell with builtins, split tab rows without forking"`
ranked name stems only (`row`, `parse`, `resolve`), with `resolve_caps` and `resolve_kit_dir` among
them, which this unit keeps as the reader and the lookup. No existing seam fits beyond those named
above. The recall probe returned the triage record, `TOOL-aThawedCorpus-3` for the spawn ceilings,
`TOOL-aSparedSpawn-19` for the leg's graded-nothing rule, and the `TOOL-dTrueNorth-27` brief, whose
memory-hygiene probe stood at 191 against 189 and was cut back rather than raised. None splits a
budgets answer.

Recall terms used: `python tools/memory-recall/query.py "fork ceiling spawn budget per-cap budget reader subshell awk parse once builtins manifest-check memory-hygiene" --terms "read_cap_mode read_budget_field fork-ceilings spawn budget var-pipe CAP_ANSWERS MB_ANSWERS budgets resolve --explain lowered ceiling"`
