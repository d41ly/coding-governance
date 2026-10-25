# TOOL-dGroundRules-84 — the shell sources and kit-path spellings this build left red on the bar, each site converted or declared, and the install-prefix counter reads a `limits:` home as the Skill path it is

**Status:** CLOSED · rev-1 · 2026-10-25 · node d · Tier-1 · base cae57b1d · streams tooling · order 31

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dGroundRules-84-research-bar-triage.md](../build/2026-10-25-build-TOOL-dGroundRules-84-research-bar-triage.md) | research | — |
| [2026-10-25-prompt-TOOL-dGroundRules-84-1-researcher.md](../prompts/2026-10-25-prompt-TOOL-dGroundRules-84-1-researcher.md) | journal | — |
| [2026-10-25-prompt-TOOL-dGroundRules-84-1-spec-writer.md](../prompts/2026-10-25-prompt-TOOL-dGroundRules-84-1-spec-writer.md) | journal | — |
| [2026-10-25-prompt-TOOL-dGroundRules-84-bar-triage.md](../prompts/2026-10-25-prompt-TOOL-dGroundRules-84-bar-triage.md) | research | — |
| [2026-10-25-prompt-TOOL-dGroundRules-84-spec-brief.md](../prompts/2026-10-25-prompt-TOOL-dGroundRules-84-spec-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

The close's bar pre-check at `cae57b1d8` failed ten legs, each green at the run's base `3c2b69be4`.
The research record (§8's fenced block) triaged them into three units, and this unit takes legs 3, 4,
5, 7 and 9. They are one location probe, twelve forks spent on builtin work, one fixed-name temp, 34
kit-path spellings and one harness arm. Each site is converted, or declared where no conversion
exists. One spelling is the install-prefix counter's false positive, which this unit fixes in the
counter.

## 2. Scope (IN)

- **S1** — Leg 3, the location probe. The two `git -C "$_dir" rev-parse --show-*` probes at
  `tools/check-template-size.sh:92` and `:93` open with the lint's own scrub, in the text §4 "Leg 3"
  gives. Observed by AC1.
- **S2** — Leg 4, the forks spent on builtin work. Sixteen sites on thirteen lines in eight files
  convert to their no-fork forms, in the text §4 "Leg 4" gives: `.githooks/pre-commit:204`,
  `tools/check-line-length.sh:165`, `tools/check-template-size.sh:90`,
  `tools/check-spec-tokens.test.sh:1715` and `:1726`, `tools/policy/adopt-policy.sh:28`,
  `tools/push-main.test.sh:1107` and `:1109`, `tools/workflows/check-protocol-parity.test.sh:553` and
  `:604`, and `tools/workflows/unattended-build.test.sh:2109`, `:2113` and `:2119`. The template-size
  rewrite also keeps its key derivation whole. Observed by AC2 and AC7.
- **S3** — The rows of `memory/project/spawn-idiom-sites.txt` follow the scan, in the text §4 "The
  registry rows" gives. The `tools/hooks/agent-cap.test.sh` `pure-fn-subst` row (line 117) is taken
  out, because TOOL-dGroundRules-10 converted its sites. A `tools/policy/policy-shim.sh` `var-pipe` row
  of 3 is added, whose reason follows the `tools/run-gates/run-held-wsl.sh` row: the shim's sites
  sit in the byte-identical inline copy of `tools/lib/resolve-remote.sh`, which converts only with its
  canonical copy. A `tools/push-main.test.sh` `pure-fn-subst` row of 1 is added, naming why its one
  site has no no-fork form. The `tools/check-template-size.sh` rows go to `path-subst` 4 and
  `var-pipe` 2. TOOL-dGroundRules-85 also writes rows of this registry, for its own files, and builds
  after this unit, so it writes them against the registry this unit leaves. Observed by AC2.
- **S4** — Leg 5, the fixed-name temp. `tools/policy/adopt-policy.sh:99` writes the scaffold to a
  temp named by `mktemp -u` beside the policy file, then moves it into place, in the text §4 "Leg 5"
  gives. Observed by AC3.
- **S5** — Arm 2 of `tools/policy/adopt-policy.test.sh` (`:36-38`) stages the scaffold's write
  failure with a failing `mv` first on `PATH`, since S4 leaves no fixed temp name to plant a
  directory at. NOT OBSERVED by a criterion here: it is a suite arm §6 declares on its `New arm:`
  line, which the main loop observes RED and then GREEN at the close.
- **S6** — Leg 7, the kit-path spellings. Each of the 33 spellings the leg names, on the lines §4
  "Leg 7" tables, is spelled through a name the file or suite already owns, a named constant, or a
  drained prose token. `tools/govkit/selftest.py` changes for spellings only. Observed by AC4.
- **S7** — The rule-3 operand split of the install-prefix counter (`tools/check-install-prefix.sh:346`)
  gains `:`, in the text §4 "The rule-3 split" gives. A `<kind>:` prefix ahead of a Skill directory
  then reads as no path segment, so `tools/policy/caps.toml:87` counts nothing. Observed by AC5.
- **S8** — Three `DGR84` arms in `tools/check-install-prefix.test.sh`, directly before its
  population block (`:171`), in the text §4 "The arm" gives. NOT OBSERVED by a criterion here: it is
  the suite arm §6 declares on its `New arm:` line, observed RED and then GREEN at the close.
- **S9** — Leg 9, check 7's message. `tools/check-template-size.sh:76` names the two positionals it
  echoes through one variable, so the harness-arms signature stops where arm A15
  (`tools/check-template-size.test.sh:141`) already stops, in the text §4 "Leg 9" gives. Observed by
  AC6.

## 3. Non-goals (OUT)

- Legs 1, 2, 6, 8 and 10 of the bar pre-check, which units TOOL-dGroundRules-85 and
  TOOL-dGroundRules-86 take.
- The fork costs of `tools/memory-tree/check-memory-hygiene.sh` and
  `skills/session-kickoff/manifest-check.sh`, and their rows in the spawn-idiom registry.
- The govkit selftest's verdict. This unit edits `tools/govkit/selftest.py` for two spellings only.
- `tools/policy/caps.toml`. Its line 87 is right as written, and S7 fixes the counter that misread it.
- The lint's function-body reader. `read_function_bodies` lets a later definition of a name win
  (`tools/gate-lint/sh_hygiene.py:766-787`), which is why arm 27's stub makes `$(resolve_python)` read
  as pure. S3 declares that site with the reason. Teaching the reader subshell scope is its own unit.
- The hook's own `policy` join (`tools/hooks/agent-cap.js:465`), which the counter does not count, and
  the other inline copies of `remote_ladder_sh`.
- Any help page. No page under `help/` spells a path or message this unit changes.

### Edges

none

## 4. Design

### Evidence

The sites were re-derived from the tree at `cae57b1d8`, which is this worktree's HEAD. The only
change since is a staged records file, so the product tree is the bar pre-check's tree. A role agent
may run no leg: scratch-guard refused the first leg command this writer ran, the location-probe
lint. So each site comes from that leg's recorded output in the run's scratchpad, the file
bar-reds-cae57b1d8.txt, and was then read in the source and counted by this writer's own probes.

- A scratch copy of the `var-pipe` regex (`tools/gate-lint/sh_hygiene.py:643-647`) and a classifier
  for `$(printf`, `$(cat`, `$(basename` and `$(dirname` reproduce every count the spawn leg printed
  at HEAD. They count `.githooks/pre-commit` 5, `tools/check-line-length.sh` 4,
  `tools/check-template-size.sh` 2, `tools/push-main.test.sh` 19,
  `tools/workflows/check-protocol-parity.test.sh` 4, `tools/workflows/unattended-build.test.sh` 4
  `cat` sites and `tools/policy/policy-shim.sh` 3. Run over each file at `3c2b69be4`, they give the
  registry's numbers, which places each new site.
- The install-prefix counter's own source, cut from the script by its heredoc anchors and fed the
  gate's derived population and kit names, reproduces the leg's 34 spellings once the 19 lines that
  match a render template are set aside. "The rule-3 split" gives the probe and its result.
- `git blame` against the base dates each site, and agrees with the record's attribution.

### Leg 3 — the location probe

Lines 92-93 of `tools/check-template-size.sh` become the lint's printed remedy. The scrub opens the
substitution, which is the form the lint reads as scrubbed (`SCRUBBED`, `tools/gate-lint/sh_hygiene.py:204`):

```
  if [ "$(unset GIT_DIR GIT_WORK_TREE; git -C "$_dir" rev-parse --show-toplevel 2>/dev/null)" = "$ROOT" ]; then
    key=$(unset GIT_DIR GIT_WORK_TREE; git -C "$_dir" rev-parse --show-prefix 2>/dev/null)$_name
```

### Leg 4 — the forks spent on builtin work

`.githooks/pre-commit:204` (TOOL-dGroundRules-6, `4c1f59ccd`). The `tr` form ends every name in a
space, the last one included, and both messages that read it, `:207` and `:209`, spell
`${pg_names}staged`. So the expansion keeps that trailing space:

```
    pg_names="${pg_hit//$'\n'/ } "
```

`tools/check-line-length.sh:165` (TOOL-dGroundRules-9). The first line comes by parameter expansion.
Both names are the function's locals (`:157`), and nothing reads either after this:

```
    _out=${_out:-$_pk}
    printf 'check-line-length: %s — %s\n' "$LL_RULE" "${_out%%$'\n'*}"
```

`tools/check-template-size.sh:90` (TOOL-dGroundRules-9) takes the form of
`tools/branch-reconcile/adopt-branch-reconcile.sh:25`. That form spends neither of the line's two
`dirname` forks, so the file's `path-subst` count goes from 6 to 4. A subject with no slash keeps
`.`, and a subject at the filesystem root keeps `/`, as `dirname` answers:

```
  _up=.; [[ $FILE == */* ]] && { _up=${FILE%/*}; _up=${_up:-/}; }
  _dir=$(cd "$_up" 2>/dev/null && pwd) || _dir=$_up
```

`tools/check-spec-tokens.test.sh:1715` and `:1726` (TOOL-dGroundRules-46, moved by -56) become
`printf -v`. Neither format ends in a newline, so the substitution stripped nothing:

```
  [ "${3:-}" = fence ] && printf -v add '\n\140\140\140text\n%s\n\140\140\140' "$2"
```
```
printf -v _tick -- '- When \140. helper.sh; f\140 runs, it prints \1400\140.'; seed_source "$d" "$_tick"
```

`tools/policy/adopt-policy.sh:28` (TOOL-dGroundRules-1) takes the same reconcile form, byte for byte
the line at `tools/branch-reconcile/adopt-branch-reconcile.sh:25`:

```
HERE=.; [[ $0 == */* ]] && HERE=${0%/*}; HERE="$(cd "$HERE" && pwd)" || exit 2
```

`tools/push-main.test.sh` arm 33 (TOOL-dGroundRules-25). Its four `var-pipe` sites, two on `:1107`
and two on `:1109`, become `[[ ]]` matches over the captured output with a newline on each side. So
`^` and `-x` keep their line anchoring:

```
    elif [[ $'\n'$out33 != *$'\n''push-main: prepared '* || $'\n'$out33$'\n' != *$'\n'merge=1$'\n'* ]]; then
```
```
    elif [[ $'\n'$out33$'\n' == *$'\n'regen-rc=0$'\n'* && $'\n'$out33$'\n' == *$'\n'mirror-rc=0$'\n'* ]]; then
```

The arm's `pure-fn-subst` site is `_py33=$(resolve_python)` at `:1089`. It has no no-fork form. The
lint reads arm 27's stub `resolve_python() { echo bash; }` (`:948`) as the function's body, a later
definition winning, and calls it pure. The call at `:1089` runs the inlined resolver, which runs each
python candidate. S3 declares it.

`tools/workflows/check-protocol-parity.test.sh:553` (TOOL-dGroundRules-10) and `:604`
(TOOL-dGroundRules-30) indent the answer by parameter expansion, the form
TOOL-dGroundRules-83 wrote at `:591`:

```
  printf '  %s\n' "${_pk_dir//$'\n'/$'\n'  }"
```
```
      printf '  %s\n' "${_ub_out//$'\n'/$'\n'  }"
```

`tools/workflows/unattended-build.test.sh` (TOOL-dGroundRules-74). The two stderr reads at `:2109`
and `:2119` become `e=$(<"$LAY/old-hook.err")`. The read at `:2113` redirects stderr, and
`$(<f 2>/dev/null)` is the BANNED `redirected-read` class, which reads empty. So a file test guards
it instead:

```
h=; [ -f "$WS/scripts/$WFK/unattended-build.js" ] && h=$(<"$WS/scripts/$WFK/unattended-build.js")
```

The suite runs under `set -u` alone (`:136`), so a missed test is no exit. The file's `cat-file`
count returns to the registry's 1, the `:2223` read the base held.

### The registry rows

In `memory/project/spawn-idiom-sites.txt`, rows sorted by path and then class:

| Row | Change |
|---|---|
| `tools/hooks/agent-cap.test.sh` `pure-fn-subst` 11 (line 117) | taken out |
| `tools/check-template-size.sh` `path-subst` | 5 to 4 |
| `tools/check-template-size.sh` `var-pipe` | 3 to 2 |
| `tools/policy/policy-shim.sh` `var-pipe` 3 | added after the `tools/playbook/adopt-playbook.sh` row |
| `tools/push-main.test.sh` `pure-fn-subst` 1 | added between its `path-subst` and `var-pipe` rows |

The two new rows' reasons, tab-separated after the count as the header (lines 4-18) requires. A
`pure-fn-subst` reason names its callee and why it keeps its substitution:

```
arrived with the inlined `remote_ladder_sh` block at TOOL-dGroundRules-5, which converts only with its canonical and every copy, the parity arm reading them byte for byte; a parameter expansion or `[[ =~ ]]` is the no-fork form, drained by a follow-up unit
```
```
keeps its substitution: the lint reads arm 27's subshell stub `resolve_python() { echo bash; }` as the body, a later definition winning, while arm 33 calls the inlined resolver, which runs each python candidate, so no no-fork form exists: resolve_python×1
```

The shim's block (`tools/policy/policy-shim.sh:27-69`) is byte-identical to the canonical one in
`tools/lib/resolve-remote.sh:11-53`, measured with `diff` at HEAD. `git log -S` dates it to
`c3932e63b`, TOOL-dGroundRules-5. The other rows the scan measures already match.

### Leg 5 — the fixed-name temp, and the arm it moves

Lines 99-100 of `tools/policy/adopt-policy.sh` become:

```
  _tmp=$(mktemp -u "$FILE.XXXXXXXX")
  if ! { "$PY" -B "$HERE/policy.py" scaffold > "$_tmp" && mv "$_tmp" "$FILE"; } 2>/dev/null; then
    rm -f "$_tmp" 2>/dev/null
```

The `mv` source follows a binding holding `$(mktemp`, which the temp lint admits. An empty `_tmp`
makes the redirect fail, and that takes the refusal path. Arm 2 of the adopter's suite planted a
directory at `policy.toml.tmp` to make the write fail, which an unpredictable name defeats. So S5
restages it:

```
# 2 — the scaffold cannot be moved into place: an `mv` first on PATH that exits 1 stages it, since the
# scaffold's temporary name is unpredictable and nothing can be planted at it (TOOL-dGroundRules-84).
mkrepo no-mv commit; mkdir -p "$TMP/no-mv-bin"; printf '#!/bin/sh\nexit 1\n' > "$TMP/no-mv-bin/mv"; chmod +x "$TMP/no-mv-bin/mv"
PATH="$TMP/no-mv-bin:$PATH" want "--scaffold where the scaffold cannot be written refuses" 1 'policy: the scaffold could not be written to ' --scaffold --target "$R"
```

`want` runs the adopter as a child (`tools/policy/adopt-policy.test.sh:25-30`), so the stub reaches
it. Line 99 is the adopter's only `mv`. The label and the asserted text are unchanged, so the
harness-arms join still reads the refusal as armed. The staging was probed under this Git Bash with
a three-line copy of the S4 shape: the stub made it refuse with exit 1 and leave no temp behind, and
without the stub it wrote the file.

### Leg 7 — the kit-path spellings

Every site the leg named at `cae57b1d8`, and its fix:

| Site | Spelling | Fix |
|---|---|---|
| `.githooks/pre-commit:216` | the guard list under the policy kit, after `HEAD:` | `pg_kit=policy` named once above `:199`; `:199`, `:216` and `:219` read `$pg_kit` |
| `tools/check-spec-tokens.test.sh:1774` | an `OVERLAP_PAIRS` row under the policy kit's name | rows `:1774` and `:1775` spell `pkg` for `policy` |
| `tools/govkit/selftest.py:14685`, `:14687` | `"policy"` joined | `KIT_NAMES["policy"]`, the resolved directory's name (`:117`) |
| `tools/hooks/agent-cap.test.sh:39` | the arms copy's `hooks` directory | `ARMS_HOOKS` bound on `:38` |
| `tools/hooks/agent-cap.test.sh:1202`, `:1203`, `:1205`, `:1211`, `:1213`, `:1216` | rule 7's hook copy | `R7_HOOKS` bound on `:1194` |
| `tools/hooks/agent-cap.test.sh:1234`, `:1235`, `:1237`, `:1238`, `:1240` | the writer split's hook copy | `WS_HOOKS` bound on `:1224` |
| `tools/hooks/agent-cap.test.sh:1229`, `:1239` | the stub mirror's policy directory | `WS_POLICY` bound on `:1224` |
| `tools/policy/README.md:472`, `tools/policy/check_policy.py:73` | the fixture consumer under `hooks/` | the consumer's directory is `consumer/` |
| `tools/policy/check_policy.py:3655` | the same, as a case key | `"consumer/consumer.sh"` |
| `tools/policy/README.md:535`, `:547`, `:653` (two), `tools/policy/check_policy.py:148`, `:3798` | the deployer registry in prose | `<tool-root>/govkit/registry.toml`, with the tool root as the thing 0 to 2 deep |
| `tools/policy/check_policy.py:1070` | the kit's own directory | `KIT.name` (`tools/policy/policy.py:61`) |
| `tools/policy/check_policy.py:2676`, `:2677` | the memory-tree sibling copy | the directory and file names of `load_tree_lib().__file__`, the module `resolve_kit_dir` found |
| `tools/policy/check_policy.py:3804` | the registry joined | `top / budgets.derive_tool_root() / REGISTRY_REL` (imported at `:655`) |
| `tools/policy/policy.py:1039` | `REGISTRY_REL` as one literal | `DEPLOYER_HOME = "govkit"` on its own line, and `REGISTRY_REL = f"{DEPLOYER_HOME}/registry.toml"` |
| `tools/policy/policy.py:1045` | the docstring's registry | "where exactly one `REGISTRY_REL` sits under a `<d>` 0 to 2 deep" |
| `tools/policy/caps.toml:87` | a `limits:` home | S7 |

The bound names keep each path's bytes. `tools/hooks/agent-cap.js:465` resolves the policy kit as
the sibling literally named `policy`, so `R7_HOOKS` and `WS_HOOKS` are `"$R7/kits/hooks"` and
`"$WS/hooks"`, and `WS_POLICY` is `"$WS/policy"`. A directory spelled with no file after it counts
nothing under rule 3, and a path joined from two names is the ban's stated blind spot, which is how a
fixture names its kits (`tools/check-install-prefix.sh:59-60`). TOOL-dRedressedBar-4 took the same
shape, the directory name held in a named constant.

`CONSUMER_FILE` (`tools/policy/check_policy.py:1972`) becomes `("consumer", "consumer.js")`. Its
reader writes the helper path as `../{prefix}policy-mirror.js` (`:4440`), which the new directory's
depth of one keeps. Neither `consumer` nor `pkg` is a kit directory under `tools/`. The kit sits at
its own prefix in `build_repo` (`:4430-4432`), so no fixture path clashes.

`check_policy.py:2676-2677` becomes:

```
        lib = Path(load_tree_lib().__file__)
        (kit.parent / lib.parent.name).mkdir(parents=True, exist_ok=True)
        shutil.copyfile(lib, kit.parent / lib.parent.name / lib.name)
```

### The rule-3 split

`tools/check-install-prefix.sh:346` becomes:

```
            operand = re.split(r"[\s\"'`=(:]", before)[-1]
```

Its comment at `:348` reads `# a Skill dir, even after a `limits:` prefix, a git `hooks/`, a sidecar under the git dir`.
`caps.toml:87`'s `before` is `home = "limits:.claude/skills/`. Its operand was `limits:.claude/skills/`,
whose first segment `DOTDIR` (`^\.[A-Za-z]`) does not match, so the line counted. Line 83's
`name = ".claude/skills/unattended/SKILL.md"` passed. Split on `:` too, the operand is
`.claude/skills/`, which is exempt like line 83. An operand that `HEAD:` precedes keeps counting.
Bare, its `before` ends in `:`, not `/`, so rule 3 counts it before any split. Under a literal
directory, its operand after the cut is that directory. `.githooks/pre-commit:216` is the first
shape, and S6 spells it otherwise.

The candidate predicate over the real tree, measured at `cae57b1d8` with this probe:

```
# split84.py <gov tree> -- the install-prefix counter's own source, cut from the script by its heredoc
# anchors, run over the gate's population before and after rule 3's operand split gains `:`.
import collections, os, pathlib, subprocess, sys
root = pathlib.Path(sys.argv[1]).resolve(); os.chdir(root)
sh = (root / "tools/check-install-prefix.sh").read_text(encoding="utf-8")
head = "<<'BAN_PY' || true\n"
src = sh[sh.index(head) + len(head):sh.index("\nBAN_PY\n")]
OLD = r'''operand = re.split(r"[\s\"'`=(]", before)[-1]'''
NEW = r'''operand = re.split(r"[\s\"'`=(:]", before)[-1]'''
assert src.count(OLD) == 1, "the rule-3 split line moved"
ls = lambda *a: subprocess.run(["git", "ls-files", "--", *a], capture_output=True, text=True).stdout
files = "\n".join(sorted(set(ls("tools/*", "skills/*", ".githooks/*", "*.template.*", "WIRE-INTO-PROJECT.md").split())))
kits = "\n".join(sorted({p.split("/")[1] for p in ls("tools/*/*").split() if p.count("/") >= 2}))
env = dict(os.environ, BAN_KITS=kits, BAN_EXT="sh|py|js|md|json|toml|txt|tsv|conf|example", BAN_TEMPLATES="")
def run(code):
    r = subprocess.run([sys.executable, "-c", code, "--offenders"], input=files, capture_output=True,
                       text=True, env=env, encoding="utf-8")
    assert r.returncode in (0, 1), r.stderr
    return set(r.stdout.splitlines())
before, after = run(src), run(src.replace(OLD, NEW))
print("before", len(before), "after", len(after), collections.Counter(k.split("\t")[0] for k in before))
for k in sorted(before - after): print("lost  ", k)
for k in sorted(after - before): print("gained", k)
```

It printed `before 53 after 52`, then one line, `lost   tools/policy/caps.toml	ban	unattended/SKILL.md`,
and no `gained` line. The 53 are the leg's 34 spellings plus 19 on five render files the probe did not
set aside, because it passes no templates. Those five are `tools/workflows/unattended-build.js` 9,
`tools/unattended/playbook.fixture.md` 5, two `tools/unattended/fixture-records/` files 2 each, and
`tools/workflows/drift-audit-state.js` 1. The grep shows `unattended/SKILL.md` only at
`tools/policy/caps.toml:83` and `:87`, and line 83 never counted, so the lost key is line 87. The
suite's own fixtures spell no kit path after a `:`, so its existing arms are unmoved. PINNED: measured
at `cae57b1d8`, and the leg's rerun at the close re-derives it.

### The arm

S8 inserts these lines directly before `# ==================== the POPULATION is every tracked file`
in `tools/check-install-prefix.test.sh`:

```
# ==================== TOOL-dGroundRules-84 — rule 3's operand splits on `:` too ==============
# A declaration's `<kind>:` prefix ahead of a Skill dir is no path segment, so a `limits:` home counts
# nothing; a `git show` operand naming a kit after `HEAD:`, bare or under a literal directory, still
# counts.
K="$TMP/colon"; build_source_fixture "$K" 'A qdemo kit.'
{
  printf '%s\n' 'home = "limits:.claude/skills/qdemo/SKILL.md"'
  printf '%s\n' 'git show "HEAD:qdemo/x.sh"'
  printf '%s\n' 'git show "HEAD:sub/qdemo/x.sh"'
} > "$K/${PFX}qdemo/colon.sh"
git -C "$K" add -A >/dev/null 2>&1
read_gate "$K"; _kc=$?
if [ "$_kc" = 1 ] && [[ $LAST_OUT != *"  ${PFX}qdemo/colon.sh:1  "* ]]; then good "DGR84 a limits:-prefixed Skill path counts nothing"
else bad "DGR84 a limits:-prefixed Skill path counted, or the gate exited $_kc, wanted 1"; fi
for _n in 2 3; do
  case "$LAST_OUT" in *"  ${PFX}qdemo/colon.sh:$_n  qdemo"*) good "DGR84 ...and the HEAD: operand on line $_n still counts" ;;
    *) bad "DGR84 ...the HEAD: operand on line $_n passed unnamed" ;; esac
done
```

The exit test makes the first arm live, since only a graded red run exits 1. Under the counter at
`cae57b1d8` the first arm reds, and the other two hold on both sides. The third is the shape whose
operand the new split actually cuts. The arm adds no spawn idiom, so the suite's rows stay.

### Leg 9 — check 7's message

`branches` derives a `fail` call's signature through `signature(message_of(...))`
(`tools/memory-tree/check-arms.py:260`). That splits only on `INTERP_RE` (`:135`), which matches no
digit parameter. So check 7's signature ran to the message's end, `(given ${2:-} ${4:-})`, which is
text no run prints, and no arm could hold it. Lines 74-77 become:

```
if [ -n "${2:-}" ] || [ -n "${4:-}" ]; then
  FAIL_CODE=2
  _given="${2:-} ${4:-}"   # named, so the harness-arms signature ends at `(given`
  fail 7 "a retired positional was given, and the limit and the limits path are read through the policy kit's budgets.py now; pass the subject, an empty second argument and the record (given $_given)"
fi
```

The printed message is byte-identical. The signature now ends `the record (given`, which arm A15
(`tools/check-template-size.test.sh:141`) already carries, so the arm is unchanged. `ARMS_FLOORS`
holds `tools/check-template-size.sh:7:7`, and `parse_floors` reads it one-sided upward
(`tools/memory-tree/check-arms.py`), so arming this branch moves no floor.

### Where the record and the tree disagree

| The record | The tree at `cae57b1d8` | This spec |
|---|---|---|
| `pg_names=${pg_hit//$'\n'/ }` | the `tr` form's trailing space carries `${pg_names}staged` at `:207` and `:209` | keeps the trailing space |
| only the template-size `var-pipe` row moves | the reconcile form spends neither `dirname` on `:90`, so `path-subst` measures 4 | `path-subst` 5 to 4 as well |
| push-main's `pure-fn-subst` converts | the site is `$(resolve_python)`, read as pure through arm 27's stub, and the real resolver runs python | a registry row naming that |
| `mktemp -u` then `mv`, alone | adopter arm 2 plants a directory at the fixed name | arm 2 restaged, and a `New arm:` line |
| A15 extended to `(given 9999 )` | the signature ends `(given ${2:-} ${4:-})`, which no output holds | the gate names its positionals, and A15 stays |

The record left the three unattended-build lines unnamed. They are `:2109`, `:2113` and `:2119`, and
the record's file-test guard is right for `:2113`. Every other site agrees with the record.

### What this does not check

AC1 to AC6 run each leg's checker over the tree, and AC7 runs the size gate on two subjects. None
runs a suite. The S5 and S8 arms, the policy fixtures that run the adopter's suite, and the agent-cap,
push-main, spec-tokens and unattended-build suites whose lines change are the close's to run. Nothing
here checks that a spelling moved into a variable still names the right directory. The suites that
use each path check that. No leg reads a path assembled from two names, so a later literal hidden
that way passes the ban, as its header says.

### Alternatives rejected

- Pinning check 7 in `memory/project/unarmed-branches.txt`. The branch has an arm, and only the
  signature's reading kept the arm from counting.
- Teaching `signature()` to split on `${2:-}`. That changes every gate's signatures for one message.
- Converting the shim's three sites in place. The parity arm reads every `remote_ladder_sh` copy
  byte for byte against the canonical one, so one copy cannot move alone.
- A waiver for `caps.toml:87`. The ban takes none (`tools/check-install-prefix.sh` header), and the
  line spells a Skill path the counter already exempts without the prefix.
- Renaming the policy sibling in the agent-cap fixtures. The hook finds it only by that name.

### Rollout

The builder sets this spec's status from DEFERRED to INPROGRESS before its first write. Scratch-guard
admits writes under `ROUTED_PATHS` for a Tier-1 unit only at INPROGRESS, or at SPECCED once graded.
The shipped bytes of the policy, hooks, workflows and govkit kits and of the root gates move, which
`kit epoch` prints as owed at the lander.

### Files touched (estimate)

- `.githooks/pre-commit`
- `tools/check-install-prefix.sh`
- `tools/check-install-prefix.test.sh`
- `tools/check-line-length.sh`
- `tools/check-spec-tokens.test.sh`
- `tools/check-template-size.sh`
- `tools/govkit/selftest.py`
- `tools/hooks/agent-cap.test.sh`
- `tools/policy/README.md`
- `tools/policy/adopt-policy.sh`
- `tools/policy/adopt-policy.test.sh`
- `tools/policy/check_policy.py`
- `tools/policy/policy.py`
- `tools/push-main.test.sh`
- `tools/workflows/check-protocol-parity.test.sh`
- `tools/workflows/unattended-build.test.sh`
- `memory/project/spawn-idiom-sites.txt`

## 5. Acceptance criteria

All commands run from the repository root of the pass's worktree, in Git Bash. Each is a leg's own
command from `tools/gate-legs.json`, run over the tree, and each staged break is undone before the
next criterion. At `cae57b1d8` every criterion but AC7 was red, as the bar log recorded.

- **AC1** — When `python tools/gate-lint/sh_hygiene.py --location-probes memory/project/location-probe-waivers.txt . ':!memory/'` runs, it exits 0 and prints `no undeclared location probe asked from a moved directory`.
  At `cae57b1d8` it printed `2 finding(s)`, naming `tools/check-template-size.sh:92` and `tools/check-template-size.sh:93`.
  Red when: the scrub is left off line 92. Then it exits 1 and names `tools/check-template-size.sh:92` as a probe asked bare.
- **AC2** — When `python tools/gate-lint/sh_hygiene.py --spawn-idioms memory/project/spawn-idiom-sites.txt . ':!*.test.sh' ':!memory/'` runs, it exits 0 and prints `sh-hygiene: OK — no BANNED spawn idiom`.
  At `cae57b1d8` it printed `12 finding(s)`.
  Red when: `.githooks/pre-commit:204` keeps its `tr` pipe. Then it exits 1 and names `.githooks/pre-commit` as declared at 4 `var-pipe` sites and measured at 5.
- **AC3** — When `python tools/gate-lint/sh_hygiene.py --temp-names memory/project/temp-name-sites.txt . ':!*.test.sh' ':!memory/'` runs, it exits 0 and prints `no undeclared fixed-name temp is renamed into place`.
  Red when: `tools/policy/adopt-policy.sh:99` writes `"$FILE.tmp"` again. Then it exits 1 and names `tools/policy/adopt-policy.sh` with one `fixed-temp` site.
- **AC4** — When `bash tools/check-install-prefix.sh` runs, it exits 0 and prints `install-prefix: clean — `.
  At `cae57b1d8` it printed `RED — 427 tracked file(s) graded, 7 render(s) left out as matching their template, 34 kit-path spelling(s) on 33 line(s)`.
  Red when: the case key at `tools/policy/check_policy.py:3655` spells its consumer under `hooks` again. Then it exits 1 and names `tools/policy/check_policy.py:3655` with the kit `hooks`.
  cost: the leg's ceiling in `tools/gate-legs.json` is 2940 s, read at `cae57b1d8`. That is its timeout, and its run time was not measured here.
- **AC5** — When the same `bash tools/check-install-prefix.sh` runs, its output names no line of `tools/policy/caps.toml`.
  Red when: the `:` is taken out of the rule-3 split at `tools/check-install-prefix.sh:346`. Then it exits 1 and names `tools/policy/caps.toml:87` with the kit `unattended`, and that line alone, as §4's probe measured.
  figure: one line, PINNED by that probe at `cae57b1d8`.
- **AC6** — When `python tools/memory-tree/check-arms.py --check` runs, it exits 0 and prints no line opening `HYGIENE check-arms:`.
  Red when: check 7's message spells the positionals inline again. Then it exits 1 and names `tools/check-template-size.sh` check 7 branch 1 as having no positive assertion, with a stranded prefix at `tools/check-template-size.test.sh:141`.
- **AC7** — When `bash tools/check-template-size.sh AGENTS.md` and then `bash tools/check-template-size.sh memory/guides/BUILD-METHOD.md` run, each exits 0, prints `template-size OK — ` and prints no `no-ratchet` line, because each key matches its row in `tools/template-size-highwater.txt`.
  Red when: the slash test is left out of `tools/check-template-size.sh:90`. Then a subject with no slash takes itself for its directory, and the first run prints a `TEMPLATE-SIZE no-ratchet` line whose key spells the file name twice, joined by a slash.

## 6. Gates

`shell hygiene (a location probe asked from a moved directory)` · `shell hygiene (a fork spent on builtin work)` · `shell hygiene (a fixed-name temp renamed into place)` · `install-prefix (shipped surface)` · `install-prefix self-test` · `harness arms (fail branches armed or pinned)` · `template size <=48KiB` · `charter size` · `build-method size` · `unattended protocol size` · `unattended skill size` · `kickoff engine size <=18KiB` · `template size gate selftest` · `line-length gate selftest` · `branch-guard self-test` · `push-main self-test` · `spec-tokens self-test` · `agent-cap self-test` · `scratch-guard self-test` · `verifier fan-out self-test` · `review-join self-test` · `hook destinations self-test` · `tier2-review self-test` · `unattended-build self-test` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `policy fixtures` · `policy check` · `recall floor` · `recall floor arms` · `encoding posture (text IO names its encoding)` · `kit epoch (shipped bytes move, the version moves)` · `testsuite counts (every bar self-test prints one)` · `spec tokens (a spec's own names resolve)` · `memory hygiene`

New arm: tools/check-install-prefix.test.sh · covers AC5 · the counter at cae57b1d8, whose rule-3 split lacks `:`, reds the first DGR84 arm by its label while both HEAD: arms hold · none

New arm: tools/policy/adopt-policy.test.sh · covers none · the adopter with its scaffold write moved out of the `if !` test ignores the failing mv and exits 0, which reds arm 2 by its label · none

Run through `derive_guarded_legs` at `cae57b1d8`, `python tools/check-spec-tokens.py --legs-for`
names fourteen non-broad guarded legs for the estimate above:

- `tools/hooks/agent-cap.test.sh` trips `agent-cap self-test`, `scratch-guard self-test`,
  `verifier fan-out self-test`, `review-join self-test` and `hook destinations self-test` through
  `tools/hooks/`.
- Both workflows suites trip `verifier fan-out self-test`, `review-join self-test`,
  `tier2-review self-test` and `unattended-build self-test` through `tools/workflows/`.
- `tools/govkit/selftest.py` trips `govkit selftest`, `govkit refusal join`,
  `govkit acceptance matrix` and `recall floor arms` through `tools/govkit/`, and `policy fixtures`
  through its own exact line.
- The four `tools/policy/` files, `tools/check-template-size.sh` and `tools/check-line-length.sh`
  trip `policy fixtures`. The line-length gate also trips `line-length gate selftest` and
  `govkit acceptance matrix` through its own exact lines.
- `memory/project/spawn-idiom-sites.txt` trips `recall floor` and `recall floor arms` through
  `memory/`.

Every other leg it prints for these paths trips only on the broad `tools/` or `.githooks/`. The
unguarded and broad legs named beside them read what this unit changes:

- The three `shell hygiene` legs, `install-prefix (shipped surface)` and
  `harness arms (fail branches armed or pinned)` are AC1 to AC6.
- `install-prefix self-test` runs S8's arms, and `policy fixtures` runs the adopter's suite, so S5's
  arm, through `check_policy.py --fixture adopter-suite`.
- The six size legs each run `tools/check-template-size.sh`, so each runs S1, S2's line 90 and S9.
  `template size gate selftest` runs arm A15.
- `branch-guard self-test`, `push-main self-test` and `spec-tokens self-test` run the hook and the two
  suites S2 and S6 edit.
- `policy check` runs `check_policy.py`. `encoding posture (text IO names its encoding)` reads the
  three Python files, and no count moves: S6 adds no text read or write, and `shutil.copyfile` is not
  that class.
- `kit epoch` prints the shipped bytes' move as owed at the lander. `testsuite counts` reads the
  install-prefix suite's count, which S8 raises by three, derived and pinned nowhere.

Pinned counts that move: the `memory/project/spawn-idiom-sites.txt` rows S3 lists, each set to what
the scan measures once S2 lands. No floor or ceiling moves. `tools/check-template-size.sh:7:7` in
`ARMS_FLOORS` is one-sided, and no row of `memory/project/fork-ceilings.txt` traces a file this unit
edits.

## 7. Open questions

none

## 8. Revision log

- rev-1 · 2026-10-25 · initial draft from this unit's spec brief, grounded at `cae57b1d8`. A role
  agent may run no leg, so scratch-guard refused the first leg command. The sites were taken from the
  bar log the main loop recorded at that commit, read in the source, and counted by this writer's
  own probes, which reproduced each count the legs printed. The install-prefix candidate predicate
  ran over the real tree and lost exactly `tools/policy/caps.toml:87`. Five places where the research
  record and the tree disagree are corrected in §4. The largest: leg 9's arm extension could not arm
  the branch, so the gate names its positionals instead, and leg 5's fix moves an adopter arm. A
  follow-up the main loop may want: the lint's `read_function_bodies` lets a stub defined in one
  subshell stand for a function everywhere in the file, which made `tools/push-main.test.sh`'s
  `$(resolve_python)` read as pure. Scoping that reader is its own unit. The research record, the
  brief and this role's prompt, untracked when this draft was written:

```
memory/builds/dGroundRules/build/2026-10-25-build-TOOL-dGroundRules-84-research-bar-triage.md
memory/builds/dGroundRules/prompts/2026-10-25-prompt-TOOL-dGroundRules-84-spec-brief.md
memory/builds/dGroundRules/prompts/2026-10-25-prompt-TOOL-dGroundRules-84-1-spec-writer.md
```

## 9. Reuse audit

Each fix reuses a form the tree already holds. The location-probe scrub is the lint's printed remedy
(`tools/gate-lint/sh_hygiene.py:529-530`). The two directory derivations are the
`tools/branch-reconcile/adopt-branch-reconcile.sh:25` form. The indents are TOOL-dGroundRules-83's
expansion at `tools/workflows/check-protocol-parity.test.sh:591`. The temp is the lint's `mktemp -u`
remedy. The registry rows follow the shapes of the `tools/run-gates/run-held-wsl.sh` row and the
header's `pure-fn-subst` rule. The spellings go through names the files already own:
`KIT_NAMES`, `KIT.name`, `REGISTRY_REL`, `load_tree_lib`, and TOOL-dRedressedBar-4's named-constant
shape. The arm uses the suite's `build_source_fixture`, `read_gate`, `good` and `bad`
(`tools/check-install-prefix.test.sh:52-92`).
`python tools/codebase-map/reuse_lookup.py "indent each line of a captured answer, read a file's first line, or split a path's directory without a fork in bash"`
ranked only name stems (`read`, `read_text`, `resolve_bash`), and none is a no-fork shell form, so
no existing seam fits beyond the in-tree forms above. The recall probe returned TOOL-dRedressedBar-4
for the named-constant shape, TOOL-aRepatriatedFork-23 for the counter's population, and
TOOL-dRedressedBar-1's spawn-registry notes. None changes the rule-3 split.

Recall terms used: `python tools/memory-recall/query.py "spawn idiom registry row var-pipe install-prefix kit path spelling fixture rule 3 operand split skill dir" --terms "spawn-idiom-sites var-pipe pure-fn-subst cat-file path-subst fixed-temp mktemp install-prefix DOTDIR operand limits: STRANDED arm-signature"`
