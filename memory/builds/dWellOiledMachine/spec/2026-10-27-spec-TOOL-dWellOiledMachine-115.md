# TOOL-dWellOiledMachine-115 — the round-5 promotions audit's 24 medium and low findings, batched: loader counts, pathspecs, the bare-bash walk, the predicate's cache and attribution, fixture directories and citations

**Status:** OPEN · rev-2 · 2026-10-27 · node a · Tier-2 · base 0689e7fa · streams tooling · order 72 · advances TOOL-dWellOiledMachine-62

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-27-build-TOOL-dWellOiledMachine-115-deviation-1151.md](../build/2026-10-27-build-TOOL-dWellOiledMachine-115-deviation-1151.md) | deviation | — |
| [2026-10-27-review-TOOL-dWellOiledMachine-109-spec-audit.md](../reviews/2026-10-27-review-TOOL-dWellOiledMachine-109-spec-audit.md) | spec-audit | TOOL-dWellOiledMachine-113 TOOL-dWellOiledMachine-114 TOOL-dWellOiledMachine-109 TOOL-dWellOiledMachine-110 TOOL-dWellOiledMachine-111 TOOL-dWellOiledMachine-112 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of the round-5 promotions
(`memory/builds/dWellOiledMachine/reviews/2026-10-27-review-TOOL-dWellOiledMachine-98-spec-audit.md`)
exited BOUNDED with 24 confirmed findings below HIGH. BUILD-METHOD M4 promotes every one of them,
batched into ONE unit, and this is that unit. It closes, by report id:

- MEDIUM (14): 1, 2, 3, 8, 9, 10, 11, 12, 14, 16, 23, 26, 30, 31.
- LOW (10): 6, 7, 13, 15, 17, 18, 19, 24, 25, 32.

Several findings share a report item (M1: 1, 8, 26; M2: 2, 9; M3: 3, 11, 23; M5: 12, 16, 30; L1: 6,
15, 24), and each keeps its own scope item here. Findings 13 and 32 are taken at their skeptics' low
grade, and findings 8, 9, 10, 23 and 26 at their skeptics' medium grade; those grades bind. Each finding
takes the fix its skeptic judged SOUND, or the skeptic's corrected fix where the report marks the
finder's UNSOUND (finding 30).

Three medium items describe a defect a promoted unit already closes: M1 and M2 are the loader
counts that TOOL-dWellOiledMachine-113 and -114 scope, and M4 is the AC12 that
TOOL-dWellOiledMachine-109 rewrites. Here each of those findings takes the part of its fix those
units do not: the edge, the recorded measurement, or the guard against stripping a correct line.

The findings land on specs 98 to 108, so this unit repairs none in particular and sits after every
unit of the build. One unit, not two: findings 15 and 24 each amend specs on both sides of any split
by spec, finding 26 reads specs 96 and 97 together, and every amendment moves this build's README
rev cells, a generated render two halves would both write (M6 clause 3).

## 2. Scope (IN)

Each item names its finding, its report item and the spec it amends. "Spec N takes a rev bump" means
spec N is amended by S25's route, its §9 line naming this unit and the finding. Where the amended
text is itself an amendment of a further spec, that further spec receives the corrected text when
spec N's own amendment lands at the same M2 cross-read.

- **S1** — Finding 1 (M1), on TOOL-dWellOiledMachine-103 §3 and TOOL-dWellOiledMachine-104 §3.
  Spec 103's Edges gains "**consumes-from** `TOOL-dWellOiledMachine-104` — 96 §4's fixture, whose
  first line carries the loader string 103 AC1 counts, so AC1 reads 96's §6 preamble alone", and
  spec 104's Edges gains "**hands-off** `TOOL-dWellOiledMachine-103` — the fixture line that shares
  the loader string 103 AC1 counts in spec 96", in the same spec pass, so the edge keeps both ends.
  Observed by AC1.
- **S2** — Finding 8 (M1), on 103 §4 Evidence. It gains the line "After 103 S2 and 104 S1 land,
  spec 96 carries the loader string twice, once in its §6 preamble and once on the first line of §4's
  fixture: on a scratch copy built 2026-10-27, 2 over the whole file and 1 in the preamble." Observed
  by AC2.
- **S3** — Finding 26 (M1), on 103 AC1 and 106 AC1. Nothing is amended for the count itself, which
  units 113 and 114 scope to the preamble. This item takes the consequence finding 26 names, a
  builder stripping a fixture's loader line to make a whole-file count read 1: at this unit's pass
  each fixture still carries its loader line. Observed by AC3.
- **S4** — Finding 2 (M2), on TOOL-dWellOiledMachine-106 §3 and TOOL-dWellOiledMachine-107 §3.
  Spec 106's Edges gains "**consumes-from** `TOOL-dWellOiledMachine-107` — 97 §4's fixture, whose
  first line carries the loader string 106 AC1 counts, so AC1 reads 97's §6 preamble alone", and spec
  107's Edges gains "**hands-off** `TOOL-dWellOiledMachine-106` — the fixture line that shares the
  loader string 106 AC1 counts in spec 97", in the same spec pass. Observed by AC1.
- **S5** — Finding 9 (M2), on 106 §4 Evidence. It gains the line "After 106 S2 and 107 S1 land,
  spec 97 carries the loader string twice, once in its §6 preamble and once on the first line of §4's
  fixture: on a scratch copy built 2026-10-27, 2 over the whole file and 1 in the preamble." Observed
  by AC2.
- **S6** — Finding 3 (M3), on TOOL-dWellOiledMachine-108 AC8. Spec 108's AC8 runs
  `git ls-files --error-unmatch tools/runtime/supervise.py tools/memory-tree/door_fixture.py` in place
  of the bare names. Observed by AC4.
- **S7** — Finding 11 (M3), on 108 §4 Evidence. It gains the line "From the repository root,
  `git ls-files --error-unmatch lib-unattended.sh` exits 1 and
  `git ls-files --error-unmatch tools/unattended/lib-unattended.sh` exits 0, measured 2026-10-27: a
  bare pathspec matches only a file at the root (S8)." Observed by AC4.
- **S8** — Finding 23 (M3), on 108 AC8's red case, which reads "Red when: either file is absent and
  the bare-bash check passes over nothing, or a pathspec names a bare filename, which matches only a
  file at the repository root." Observed by AC4.
- **S9** — Finding 10 (M4), on 108 §4 Evidence. Its line on the AC20 slice reads "The flattened AC20
  slice of spec 90, as committed at 05ab0d1f8, prints 0 for each full path and 1 for each bare name,
  so AC12's full-path counts read red before 97 S1's rewrite and bare-name counts could not (S12,
  S13)." Observed by AC5.
- **S10** — Finding 12 (M5), on 108 S10 and §4. 108 S10's walk becomes §4's walk below, which flags
  every List or Tuple literal whose first element is the constant `'bash'` wherever it sits: a direct
  argv, a variable or walrus target, an `args=` keyword, or the left operand of `+`. 108 §4's
  Evidence line on the walk is replaced by the first line of this spec's §4 Evidence, and 108 §4
  gains the sub-head `### What the walk does not check` with the four bullets below. Observed by AC6.
- **S11** — Finding 16 (M5), on 108 S10 and §10. The walk exempts a literal inside an argument of a
  call to `resolve_shell_argv`, the resolved form at `tools/govkit/matrix.py:911`, and prints one last
  line, `subprocess calls <k>`, the liveness count of `test_no_bare_bash_argv`
  (`tools/run-gates/measure_legs.py:2682`). 108 S10 has 90 AC20 expect exactly that one line with `k`
  of 1 or more, and S10 and 108 §10 cite `test_no_bare_bash_argv` as the guard this walk widens.
  Observed by AC6.
- **S12** — Finding 30 (M5, the skeptic's corrected fix), on 108 S10 and AC10. 94 AC8's red arm
  stages six cases in a scratch copy of `supervise.py`: the three 108 S10 names, then
  `cmd = ['bash', 'x']; subprocess.run(cmd)`, `subprocess.run(args=['bash', 'x'])` and
  `subprocess.run(['bash', 'x'] + y)`. 108 AC10 becomes §4's AC10 text, whose spelling grep counts
  `id(n) not in ok`, a substring only the new walk carries. Observed by AC7.
- **S13** — Finding 14 (M6), on TOOL-dWellOiledMachine-98 §4 and §5. 98's predicate becomes §4's
  function below, which fills `_SUBJ` from one `read_attribution_tokens` pass over the window before
  `build_commit` walks it. 98 §5's perf line reads "one attribution pass, one `git log` and one
  `build_commit` walk per call; uncached, `build_commit` took 5 m 04 s over a 1081-commit window and
  1.2 s with `_SUBJ` filled, measured 2026-10-27." Observed by AC8.
- **S14** — Finding 31 (M7), on TOOL-dWellOiledMachine-101, -104 and -107 §4, §5 and the criteria
  texts their S2 and AC2 spell. In each fixture,
  `fx=$(cygpath -u "$TEMP")/abb9N; rm -rf "$fx"; git init -q "$fx"; cd "$fx" || exit 1` becomes
  `fx=$(mktemp -d "$(cygpath -u "$TEMP")/abb9N.XXXXXX"); trap 'cd /; rm -rf "$fx"' EXIT; git init -q "$fx"; cd "$fx" || exit 1`
  and the last line becomes `cd - >/dev/null; rm -rf "$fx"; trap - EXIT`, N being 5, 6 or 7. Each
  `fixture:` text reads "a git repository in a fresh `abb9N.XXXXXX` under `%TEMP%` directory, removed when
  the script exits", and each §5 risks line adds "each run makes its own directory, so two runs on one
  machine never share a repository". Observed by AC9.
  **Readers:** by name: `memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-101.md`, `memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-104.md` and `memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-107.md`, whose fixtures carry the replaced lines. by value: NO VALUE READERS — the fixture directory is read only by its own script.
- **S15** — Finding 6 (L1), on TOOL-dWellOiledMachine-99, -102 and -105 §4 Evidence. Each line
  citation of spec 95, 96 or 97 is rewritten by bullet label, as §4's table lists. Observed by AC10.
- **S16** — Finding 15 (L1), on 98 §4 Evidence and 108 §4 Evidence, by §4's table. Observed by AC10.
- **S17** — Finding 24 (L1), on TOOL-dWellOiledMachine-100, -103 and -106 §4 Evidence, by §4's
  table. Observed by AC10.
- **S18** — Finding 7 (L2), on 108 S21 and AC19. 108 S21 reads "Finding 26 (L8), on 97 S20 and AC14.
  Spec 97's S20 has the pass grep `## Dispositions` for `SEV · TOOL-dPlacedRequest-<id> ·` before
  appending, and append only when it is absent; its AC14 reads 'prints exactly 1' in place of 'prints
  1', and no count is added to its AC12. Observed by AC19." 108 AC19 gains "`<AC14 of spec 97>` piped
  to `grep -c "exactly 1"` prints 1, and `<AC12 of spec 97>` piped to `grep -c "SEV · "` prints 0".
  Observed by AC11.
- **S19** — Finding 13 (L3), on 108 AC15. Its first clause reads "When `<S1 of spec 90>` is piped to
  `grep -c "TOOL-dWellOiledMachine-93"`, it prints 1", a token only 108 S17 adds. Observed by AC12.
- **S20** — Finding 17 (L4), on 98 §4. The predicate finds A with
  `read_attribution_tokens --reverse "$floor..HEAD"` over the amended spec and keeps the first commit
  whose tokens hold the amending unit's id, so a `Pass:` trailer attributes A as it attributes P. 98's
  bullet **A** says so, and names `tools/unattended/lib-unattended.sh:1149`. Observed by AC8.
- **S21** — Finding 18 (L5), on 101, 104 and 107 §10. Each names `build_fixture`
  (`tools/memory-tree/routed_commits.py:387`), which builds a scratch repository from an ordered
  commit list in one `git fast-import`, and says why it is not used: it is Python inside a kit
  self-test, and the fixture must run the bash predicate between commits on several branches.
  Observed by AC13.
- **S22** — Finding 19 (L6), on 107 §4's fixture. Before its `cd`, the fixture reads 97 AC15's loop,
  `l=$(awk '/^- \*\*AC15\*\*/{p=1} /^- \*\*AC16\*\*/{p=0} /^## 7\./{p=0} p' memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-97.md | tr -s '\n ' ' ' | grep -o 'for n in [^`]*done')`,
  exits 1 when it is empty, and its `loop()` becomes
  `loop() { r=$(eval "$l" | tr '\n' ' '); echo "[${r% }]"; }`. 107 §10 then says the fixture runs
  AC15's own loop. Observed by AC14.
- **S23** — Finding 25 (L7), on 108 §4 Files touched and S11. Files touched gains
  `memory/builds/dWellOiledMachine/RUN.md`, and 108 S11's last sentence reads "The two spec
  templates are not edited (§8 F1); the M2 cross-read that lands S11 appends to
  `memory/builds/dWellOiledMachine/RUN.md` the surfaced park entry F1 names." Observed by AC15.
- **S24** — Finding 32 (L8), on 108 AC11, the S11 half. AC11 gains
  "`awk '/^## 7\./{p=1;next} /^## 8\./{p=0} p' <spec 93> | grep -c "kit/dogfood doc parity"` prints
  1, and `awk '/^### Files touched/{p=1;next} /^#/{p=0} p' <spec 93> | grep -c "tools/memory-tree/README.md"`
  prints 1". The S13 half is TOOL-dWellOiledMachine-110's AC22. Observed by AC16.
- **S25** — The route. Every rev bump above is made by the build run's main loop at BUILD-METHOD M2's
  cross-read, before its first code pass, in a spec pass whose commit touches specs 98 to 108 and
  whose subject names this unit and none of TOOL-dWellOiledMachine-90 to -94. It lands before the
  amendments those eleven specs make are applied. At this unit's own pass, at order 72, nothing is
  written: the pass runs AC1 to AC17 and records them. Observed by AC17.

## 3. Non-goals (OUT)

- The blocker and the high items: B1, TOOL-dWellOiledMachine-109; H1, -110; H2, -111 and -112; H3,
  -113; H4, -114.
- The report's left-shift gates: each finding here is closed by its own criterion, and a lint over
  specs is a separate mechanism (M2).
- No code written at this unit's pass: the code the amended specs describe is built by their units.
- No kit function for the predicate: TOOL-dWellOiledMachine-98 §8 F1 keeps it in spec 95's §6.

### Edges

- **consumes-from** `TOOL-dWellOiledMachine-98` — the predicate in §4 and §5's perf line, rewritten before 98's amendment of spec 95 lands, and called by AC17 (S13, S16, S20)
- **consumes-from** `TOOL-dWellOiledMachine-99` — §4 Evidence's citations (S15)
- **consumes-from** `TOOL-dWellOiledMachine-100` — §4 Evidence's citations (S17)
- **consumes-from** `TOOL-dWellOiledMachine-101` — §4's fixture, §5, §10 and the S2 and AC2 fixture texts (S14, S21)
- **consumes-from** `TOOL-dWellOiledMachine-102` — §4 Evidence's citations (S15)
- **consumes-from** `TOOL-dWellOiledMachine-103` — §3 Edges and §4 Evidence (S1, S2, S17)
- **consumes-from** `TOOL-dWellOiledMachine-104` — §3 Edges, §4's fixture, §5, §10 and the S2 and AC2 fixture texts (S1, S14, S21)
- **consumes-from** `TOOL-dWellOiledMachine-105` — §4 Evidence's citations (S15)
- **consumes-from** `TOOL-dWellOiledMachine-106` — §3 Edges and §4 Evidence (S4, S5, S17)
- **consumes-from** `TOOL-dWellOiledMachine-107` — §3 Edges, §4's fixture, §5, §10 and the S2 and AC2 fixture texts (S4, S14, S21, S22)
- **consumes-from** `TOOL-dWellOiledMachine-108` — S10, S11, S21, §4, AC8, AC10, AC11, AC15 and AC19 (S6 to S12, S16, S18, S19, S23, S24)
- **hands-off** `TOOL-dWellOiledMachine-116` — AC4's second clause, rewritten to count the two full paths S6 writes into 108 AC8 and the bare pathspec as gone (round-6 promotions audit, finding 1)
- **hands-off** `TOOL-dWellOiledMachine-117` — AC4's first clause and §4 Evidence, which ask git for the two files at their repository paths and record why (round-6 promotions audit, finding 9)
- **hands-off** `TOOL-dWellOiledMachine-118` — AC4's red case and §4 Evidence, which name a reverted S6 and record the reading that shows it red (round-6 promotions audit, finding 18)
- **hands-off** `TOOL-dWellOiledMachine-119` — AC6's first clause and red case, which run the walk over the two repository paths (round-6 promotions audit, finding 21)
- **hands-off** `TOOL-dWellOiledMachine-120` — S6, §5's risks line and §7, which quote every path to the two unbuilt fixtures that the cross-read writes into a criterion (round-6 promotions audit, finding 17)
- **hands-off** `TOOL-dWellOiledMachine-121` — S10, S11, S12, S19, §4, §6's preamble, AC3, AC6 to AC9, AC12, AC14, AC16 and §10, amended before this unit's own amendments land (round-6 promotions audit, findings 2, 3, 4, 6, 7, 8, 10, 11, 13, 15, 22, 24, 25 and 27)

## 4. Design

### The walk (S10 to S12)

108 S10 has 90 AC20 run this walk over the two files, its code span on one line:

`python -c "import ast,sys;T=[(f,ast.parse(open(f,encoding='utf-8').read())) for f in sys.argv[1:]];ok={id(x) for f,t in T for c in ast.walk(t) if isinstance(c,ast.Call) and getattr(c.func,'id',getattr(c.func,'attr',None))=='resolve_shell_argv' for a in c.args for x in ast.walk(a)};[print(f,n.lineno) for f,t in T for n in ast.walk(t) if isinstance(n,(ast.List,ast.Tuple)) and n.elts and isinstance(n.elts[0],ast.Constant) and n.elts[0].value=='bash' and id(n) not in ok];print('subprocess calls',sum(isinstance(c,ast.Call) and isinstance(c.func,ast.Attribute) and isinstance(c.func.value,ast.Name) and c.func.value.id=='subprocess' for f,t in T for c in ast.walk(t)))"`

It prints `<file> <line>` per bare argv literal, then `subprocess calls <k>`. 108 AC10 reads: "When 90
AC20's walk runs over the two files, it prints exactly one line, `subprocess calls <k>` with `k` of 1
or more; over a scratch copy of `supervise.py` holding S10's six staged cases it prints six
`<file> <line>` lines before that one; over a scratch file whose only spawn is
`subprocess.run(resolve_shell_argv(["bash", "x"]))` it prints only `subprocess calls 1`; and
`grep -c "id(n) not in ok"` prints 1 over `<spec 90>` and 0 over `<spec 94>`, and counts 0 in
`<AC1 of spec 97>`. Red when: a variable-held, keyword or concatenated argv passes, the resolver form
reads as bare, or the walk is spelled in two specs."

### What the walk does not check (the sub-head S10 adds to 108 §4)

- An argv whose first element is not the literal `'bash'`: a name such as `BASH`, `'bash.exe'`, or a
  path to bash.
- A command string run with `shell=True`, `os.system` or `os.exec*`.
- A `bash`-led literal anywhere inside an argument of `resolve_shell_argv`, which is exempt even where
  it is not the argv that call resolves.
- It flags a `bash`-led literal that is never spawned, such as a list of candidate names. That is a
  false red, which surfaces as a deviation and passes nothing wrong.

### The predicate (S13, S20)

98 §4's function, and so the one 98 S1 places in spec 95's §6, becomes:

```bash
check_amended_before_built() {  # amended unit, amending unit, built unit: 0 when ordered
  local d=memory/builds/dWellOiledMachine floor a p
  floor=$(git log --diff-filter=A --format=%H -- "$d/spec/*-TOOL-dWellOiledMachine-$2.md" | tail -1)
  [ -n "$floor" ] || return 1
  read -r a p < <(. "${LIB:-tools/unattended/lib-unattended.sh}" || exit 1
    declare -A _SUBJ=(); while IFS= read -r l; do _SUBJ[${l%% *}]=" ${l#* } "; done < <(read_attribution_tokens "$floor..HEAD")
    a=$(read_attribution_tokens --reverse "$floor..HEAD" -- "$d/spec/*-TOOL-dWellOiledMachine-$1.md" \
      | awk -v id="TOOL-dWellOiledMachine-$2" '{ for (i = 2; i <= NF; i++) if ($i == id) { print $1; exit } }')
    p=$(build_commit "$floor..HEAD" "TOOL-dWellOiledMachine-$3" "$d" "$(read_conf_value .unattended.conf GENERATED_INDEXES)" \
      "$(read_conf_value .unattended.conf SHARED_RECORDS)")
    echo "${a:--} ${p:--}")
  [ "$a" != - ] && [ "$p" != - ] && [ "$a" != "$p" ] && git merge-base --is-ancestor "$a" "$p"
}
```

`_SUBJ` is the cache `build_commit` consults when the caller declares it
(`tools/unattended/lib-unattended.sh:1226`), built the way `tools/unattended/check-pass-order.sh:275`
builds it. The whole-token match on A is the field compare of `read_attribution_tokens`' output,
which keeps 98's guard against `TOOL-dWellOiledMachine-960` and record names.

### Citations rewritten (S15 to S17)

| Finding | Spec | Cited now | Becomes |
|---|---|---|---|
| 6 | 99 | `spec-95.md:50-53` | 95 S3 |
| 6 | 99 | `spec-95.md:120-122` | dropped; the sentence names 95 §5's lines |
| 6 | 102 | `spec-96.md:50-53` | 96 S4 |
| 6 | 102 | `spec-96.md:179-181` | dropped; the sentence names AC5 |
| 6 | 105 | `spec-97.md:135-140` | 97 S24 |
| 6 | 105 | `spec-97.md:225-226` | dropped; the sentence names 97 §5's risks line |
| 15 | 98 | the three `spec-9N.md:` ranges | dropped; the sentence names 95 AC2, 96 AC5 and 97 AC15 |
| 15 | 108 | "at 96's lines 20 and 124" | "in 96's §1 Goal and its first rejected alternative" |
| 24 | 100 | `spec-95.md:136-140`, `:129-130` | dropped; the sentence names 95 AC2 and 95's §6 preamble |
| 24 | 100 | `RUN.md:30` | RUN.md's `base:` fact |
| 24 | 100 | `spec-95.md:29-53` | 95 S1 to S3 |
| 24 | 103 | `spec-96.md:179-181`; "prints lines 150 and 179" | dropped; "`grep -c "<BASE>"` over spec 96 prints 2" |
| 24 | 106 | `spec-97.md:295-297`; "prints lines 234 and 295"; `spec-97.md:199-206` | dropped; "`grep -c "<BASE>"` over spec 97 prints 2"; dropped |

### Evidence

Each finding's evidence is its row of the report's appendix, which its skeptic re-read and confirmed.
Probes re-run for this spec on 2026-10-27, at HEAD 05ab0d1f8:

- The walk above, over a scratch file, printed the direct list, the variable-held list, the `args=`
  keyword, the walrus target, the `+` operand, the tuple and the list split across lines, and its
  count line. Over a file holding only `resolve_shell_argv(["bash", ...])`, its `+` form,
  `["bash.exe", "x"]` and `[BASH, "x"]`, it printed only the count line. Over
  `tools/run-gates/held_halves.py` it printed line 129, `["bash", SHIM, "--leg"] + list(...)`. 108
  S10's current walk missed four of the seven and flagged the resolver form (S10 to S12).
- `test_no_bare_bash_argv` is defined at `tools/run-gates/measure_legs.py:2682`; it limits itself to
  `subprocess.<attr>` calls, unwraps `ast.BinOp` and asserts `calls >= 3` (S11).
- `build_commit` over `HEAD~100..HEAD`, 1081 commits once main's landings are counted, took 5 m 04 s
  with no `_SUBJ` and 1.2 s with `_SUBJ` filled from one `read_attribution_tokens` pass (S13).
- On a scratch history whose amendment of spec 97 carries `Pass: TOOL-dWellOiledMachine-108` and a
  subject naming no unit, 98's current predicate read every unit as unordered and the function above
  read every unit as ordered (S20).
- A scratch copy of spec 96 with 103 S2 and 104 S1 applied, and of spec 97 with 106 S2 and 107 S1,
  each counted the loader 2 times whole and 1 time in the §6 preamble (S2, S3, S5).
- `git ls-files --error-unmatch lib-unattended.sh` exited 1 from the root and the full path exited 0
  (S7).
- `<S1 of spec 90>` counts `TOOL-dWellOiledMachine-93` 0 times and `re-render` once (S19). Spec 93's
  §7 and Files touched count `kit/dogfood doc parity` and `tools/memory-tree/README.md` 0 times
  (S24).
- `grep -c "<BASE>"` prints 2 over spec 96 and 2 over spec 97 (S17).

### Files touched (estimate)

- `memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-98.md`
- `memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-99.md`
- `memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-100.md`
- `memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-101.md`
- `memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-102.md`
- `memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-103.md`
- `memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-104.md`
- `memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-105.md`
- `memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-106.md`
- `memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-107.md`
- `memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-108.md`
- `memory/builds/dWellOiledMachine/README.md` (re-rendered by
  `python tools/memory-tree/gen_build_index.py --write`, since eleven rev cells move)

### Alternatives rejected

- **Two batches.** Findings 15 and 24 each amend specs on both sides of every split by spec, and
  every split shares the README render (§1).
- **The walk restricted to `subprocess.<attr>` calls, as `test_no_bare_bash_argv` is (S10).** It
  misses the variable-held argv and the dict row at `tools/run-gates/held_halves.py:129`, whose argv
  reaches a spawn later.
- **Only a measured figure in 98 §5, without the cache (S13).** It prices the walk and leaves the
  minutes in every one of about 25 calls.
- **The rev bumps at this unit's own pass.** It is order 72, after every unit it corrects has built.

## 5. Production-readiness checklist

- security — N/A — spec text and criteria change; S14 keeps two fixture runs from deleting each
  other's repository.
- perf / scale — S13 takes each predicate call from minutes to about a second on a window of a
  thousand commits.
- error / empty / loading states — S11's count line makes a walk that parsed no spawn read red; S22's
  fixture exits 1 on an AC15 with no loop.
- observability — the walk prints each bare argv's file and line.
- risks — a build run that skips M2's cross-read builds units 90 to 97 on uncorrected text; AC17 is
  red at this unit's pass in that case.
- testing — AC1 to AC17.
- migration — none.
- user docs — none: no verb or key a user types changes.

## 6. Acceptance criteria

`<spec N>` is `memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-N.md`,
`<X of spec N>` is the bullet labelled X of that spec, from its label to the next column-0 `- **`
label or heading, flattened with `tr -s '\n ' ' '`, `<§4 of spec N>` is
`awk '/^## 4\./{p=1;next} /^## 5\./{p=0} p' <spec N>`, and `<loader>` is the pattern
`sed -n '/^check_amended_before_built() {/,/^}/p'`. Each command runs from the repository root, and
the predicate is loaded as TOOL-dWellOiledMachine-98 §6 states. Each criterion runs at this unit's
pass, after units 90 to 114 have built.

- **AC1** — When `grep -c 'consumes-from\*\* .TOOL-dWellOiledMachine-104.'` runs over `<spec 103>`,
  `grep -c 'hands-off\*\* .TOOL-dWellOiledMachine-103.'` over `<spec 104>`,
  `grep -c 'consumes-from\*\* .TOOL-dWellOiledMachine-107.'` over `<spec 106>` and
  `grep -c 'hands-off\*\* .TOOL-dWellOiledMachine-106.'` over `<spec 107>`, each prints 1.
  Red when: the shared loader string joins two specs with no declared edge.
- **AC2** — When `<§4 of spec 103>` and `<§4 of spec 106>` are each piped to
  `grep -c "once on the first line of §4's fixture"`, each prints 1.
  Red when: the second copy of the loader is recorded nowhere.
- **AC3** — When `sed -n '/^### Fixture/,/^### /p'` over `<spec 96>` and over `<spec 97>` is each
  piped to `grep -c "<loader>"`, each prints 1.
  Red when: a fixture's loader line was stripped to make a whole-file count read 1.
- **AC4** — When `git ls-files --error-unmatch supervise.py door_fixture.py`
  runs, it exits 0; `<AC8 of spec 108>` piped to
  `grep -c "error-unmatch supervise.py door_fixture.py"` and to
  `grep -c "only a file at the repository root"` each prints 1; and `<§4 of spec 108>` piped to
  `grep -c "error-unmatch lib-unattended.sh"` prints 1.
  Red when: AC8 keeps a bare pathspec, which exits 1 even after both files are tracked.
- **AC5** — When `<§4 of spec 108>` is piped to `grep -c "0 for each full path and 1 for each bare name"`,
  it prints 1.
  Red when: the base reading of AC12's red case is not recorded.
- **AC6** — When 90 AC20's walk runs over `supervise.py` and
  `door_fixture.py`, it prints one line matching `^subprocess calls [1-9]`;
  `grep -c "id(n) not in ok"` prints 1 over `<spec 90>`; `<S10 of spec 108>` piped to
  `grep -c "test_no_bare_bash_argv"` prints 1; and `grep -c "^### What the walk does not check"` over
  `<spec 108>` prints 1.
  Red when: the walk reads no spawn, or 90 AC20 still runs the narrower walk.
- **AC7** — When the walk runs over a scratch copy of `supervise.py` holding S12's six staged cases,
  it prints six `<file> <line>` lines and the count line; over a scratch file whose only spawn is
  `subprocess.run(resolve_shell_argv(["bash", "x"]))` it prints only `subprocess calls 1`; and
  `<AC10 of spec 108>` piped to `grep -c "id(n) not in ok"` prints 1 and to
  `grep -c "isinstance(n.args"` prints 0.
  fixture: two scratch Python files in the run's scratch directory.
  Red when: a variable-held, keyword or concatenated argv passes, or the resolver form reads as bare.
- **AC8** — When `grep -c "declare -A _SUBJ"` and `grep -c "read_attribution_tokens --reverse"` run
  over `<spec 95>`, each prints 1, and `grep -c "git log --reverse --format='%H %s'"` prints 0; and
  `grep -c "1081-commit window"` over `<spec 98>` prints 1.
  Red when: the predicate walks uncached, or A is attributed by subject alone.
- **AC9** — When `grep -c 'mktemp -d'` runs over `<spec 95>`, `<spec 96>` and `<spec 97>`, each
  prints 1, and `grep -c 'rm -rf "$fx"; git init'` over each prints 0; and when
  `s=$(sed -n '/^### Fixture/,/^### /p' <spec 95> | sed -n '/^eval/,/^cd - /p'); for i in 1 2; do bash -c "$s" | grep -cE '^(before 0|after 1|unbuilt 1)$' & done; wait`
  runs, it prints `3` twice.
  fixture: two git repositories, each in its own fresh `abb95.XXXXXX` under `%TEMP%` directory.
  cost: about a minute.
  Red when: two runs share one repository and one deletes the other's commits.
- **AC10** — When `grep -cE 'spec-9[5-7]\.md:[0-9]'` runs over `<spec 98>`, `<spec 99>`,
  `<spec 100>`, `<spec 102>`, `<spec 103>`, `<spec 105>` and `<spec 106>`, each prints 0;
  `grep -c "prints lines"` over `<spec 103>` and `<spec 106>` and `grep -c "RUN.md:30"` over
  `<spec 100>` each print 0; and `grep -c "lines 20 and 124"` over `<spec 108>` prints 0.
  Red when: a line citation of an open spec stays a few lines off.
- **AC11** — When `<AC14 of spec 97>` is piped to `grep -c "exactly 1"`, it prints 1;
  `<AC12 of spec 97>` piped to `grep -c "SEV · "` prints 0; and `<S21 of spec 108>` piped to
  `grep -c "AC14"` prints 1.
  Red when: one disposition row is counted by two criteria of spec 97.
- **AC12** — When `<AC15 of spec 108>` is piped to `grep -c 'grep -c "TOOL-dWellOiledMachine-93"'`, it
  prints 1, and to `grep -c 'grep -c "re-render"'` it prints 0.
  Red when: AC15's first clause stays green on spec 90 as it is today.
- **AC13** — When `awk '/^## 10\./{p=1} p'` over `<spec 101>`, `<spec 104>` and `<spec 107>` is each
  piped to `grep -c "routed_commits.py"`, each prints 1.
  Red when: a reuse audit still says no history-fixture seam exists.
- **AC14** — When the script under spec 97's `### Fixture` runs, it prints `ordered []`, `late [94]`
  and `unamended [91 92 93 94]`; and `sed -n '/^### Fixture/,/^### /p' <spec 97>` piped to
  `grep -c "^loop() { r=\"\"; for n"` prints 0 and to `grep -c "AC15"` prints 1 or more.
  fixture: a git repository in a fresh `abb97.XXXXXX` under `%TEMP%` directory, removed when the script
  exits.
  Red when: the fixture re-types AC15's loop, so a wrong list in AC15 cannot turn AC16 red.
- **AC15** — When `awk '/^### Files touched/{p=1;next} /^#/{p=0} p' <spec 108> | grep -c "RUN.md"`
  runs, it prints 1, and `<S11 of spec 108>` piped to `grep -c "park entry"` prints 1.
  Red when: F1's run-state write is missing from the write set.
- **AC16** — When `<AC11 of spec 108>` is piped to `grep -c "kit/dogfood doc parity"` and to
  `grep -c "tools/memory-tree/README.md"`, each prints 1, and the two counts it adds print 1 each
  over `<spec 93>`.
  Red when: S11's edits to spec 93 are skipped and AC11 still passes.
- **AC17** — When
  `for p in "98 90" "99 90" "100 90" "101 90" "102 93" "103 93" "104 93" "105 92" "106 92" "107 92" "108 92"; do set -- $p; check_amended_before_built $1 115 $2 || echo $1; done`
  runs, it prints nothing.
  Red when: this batch's rev bump of a spec lands after the build commit of the earliest unit that
  spec's corrections reach, and the loop prints that spec.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `recall floor` · `recall floor arms` · `tier2-review self-test` · `policy fixtures`

No arm is added or moved at this unit's pass: each criterion is a probe or a grep, and the arms the
amended units declare stay on their own §7 lines.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, the round-5 promotions audit's 24 medium and low findings
  batched.
- rev-2 · 2026-10-27 · §3 · Edges: the reciprocal of each edge the spec audit of the round-6
  promotions' promoted units declare on this unit, mirrored from TOOL-dWellOiledMachine-116, TOOL-dWellOiledMachine-117, TOOL-dWellOiledMachine-118, TOOL-dWellOiledMachine-119, TOOL-dWellOiledMachine-120, TOOL-dWellOiledMachine-121.

## 10. Reuse audit

Each item extends the seam its finding names: `test_no_bare_bash_argv`
(`tools/run-gates/measure_legs.py:2682`), widened from `subprocess.<attr>` calls to every `bash`-led
literal and kept with its liveness count (S10 to S12); `build_commit`'s `_SUBJ` cache and
`read_attribution_tokens` (`tools/unattended/lib-unattended.sh:1149`), as
`tools/unattended/check-pass-order.sh:275` uses them (S13, S20); `mktemp -d` with an exit trap for
the fixtures (S14); and spec 108's own slice convention for every criterion. The probe
`python tools/codebase-map/reuse_lookup.py "flag a subprocess argv that opens with a bare bash
literal"` ranked `resolve_bash` and `resolve_shell_argv` among name-stem hits and no argv guard,
which the grep for `test_no_bare_bash_argv` found instead. The probe for "build a scratch git
repository fixture from an ordered list of commits" ranked name stems only; `build_fixture` in
`tools/memory-tree/routed_commits.py:387` was found by reading, and S21 records it. No item mints a
module.

Recall terms used: `python tools/memory-recall/query.py "how is a promoted spec criterion that is
green before its build made red at base" --terms "criterion green at base bare name full path grep
count flattened slice red case rewrite"`
