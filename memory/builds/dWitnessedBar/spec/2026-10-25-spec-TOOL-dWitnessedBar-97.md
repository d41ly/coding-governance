# TOOL-dWitnessedBar-97 — the round-1 audit of units 91 and 92, 10 minors batched: derivation notes naming launcher, exit and script, an isolated third clone, pass commits read through the shipped seams, unit 91's note graded and every unit ledger read

**Status:** DEFERRED · rev-1 · 2026-10-25 · node d · Tier-2 · base cdfbd1cf · streams tooling · order 50 · advances TOOL-dWitnessedBar-31

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md) | journal | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-54 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 TOOL-dWitnessedBar-58 TOOL-dWitnessedBar-59 TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-61 TOOL-dWitnessedBar-62 TOOL-dWitnessedBar-63 TOOL-dWitnessedBar-64 TOOL-dWitnessedBar-65 TOOL-dWitnessedBar-66 TOOL-dWitnessedBar-67 TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-71 TOOL-dWitnessedBar-72 TOOL-dWitnessedBar-73 TOOL-dWitnessedBar-74 TOOL-dWitnessedBar-75 TOOL-dWitnessedBar-76 TOOL-dWitnessedBar-77 TOOL-dWitnessedBar-78 TOOL-dWitnessedBar-79 TOOL-dWitnessedBar-80 TOOL-dWitnessedBar-81 TOOL-dWitnessedBar-82 TOOL-dWitnessedBar-83 TOOL-dWitnessedBar-84 TOOL-dWitnessedBar-85 TOOL-dWitnessedBar-86 TOOL-dWitnessedBar-87 TOOL-dWitnessedBar-88 TOOL-dWitnessedBar-89 TOOL-dWitnessedBar-90 TOOL-dWitnessedBar-91 TOOL-dWitnessedBar-92 TOOL-dWitnessedBar-93 TOOL-dWitnessedBar-94 TOOL-dWitnessedBar-95 TOOL-dWitnessedBar-96 |
| [2026-10-25-build-TOOL-dWitnessedBar-97-round14-h1-return.md](../build/2026-10-25-build-TOOL-dWitnessedBar-97-round14-h1-return.md) | research | — |
| [2026-10-25-prompt-TOOL-dWitnessedBar-97-1-spec-writer.md](../prompts/2026-10-25-prompt-TOOL-dWitnessedBar-97-1-spec-writer.md) | journal | TOOL-dWitnessedBar-1 |
| [2026-10-25-prompt-TOOL-dWitnessedBar-97-round14-h1-brief.md](../prompts/2026-10-25-prompt-TOOL-dWitnessedBar-97-round14-h1-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 91 and 92
(`memory/builds/dWitnessedBar/reviews/2026-10-25-review-TOOL-dWitnessedBar-91-spec-audit-round1.md`)
exited CONVERGED with 14 confirmed findings: four at HIGH, which `TOOL-dWitnessedBar-93`,
`TOOL-dWitnessedBar-94`, `TOOL-dWitnessedBar-95` and `TOOL-dWitnessedBar-96` take, and 10 minors.
BUILD-METHOD M4 batches every MEDIUM and LOW into one unit, or two only where they split into
disjoint write sets by M6's clauses. §4 "Why one unit" says why these stay one. Each finding is named
by report id and is its own scope item, including where the report merged two ids into one item.
The minors land on units 91 and 92, so this unit repairs no one unit and builds after every unit of
the build (order 50).

| Report item | Severity | Report id | Lands on | Scope item |
|---|---|---|---|---|
| M1 | MEDIUM | 2 | unit 92 S4, AC4 | S1 |
| M1 | MEDIUM | 6 | unit 92 S4, §4 note table, AC4 | S2 |
| M2 | MEDIUM | 3 | unit 92 S12, AC11 | S3 |
| M3 | MEDIUM | 4 | unit 92 S2, AC2 | S4 |
| M4 | MEDIUM | 9 | unit 92 AC5 | S5 |
| M5 | MEDIUM | 11 | unit 91 S2, AC2 | S6 |
| M6 | MEDIUM | 12 | unit 92 §4 note check, S6, AC6 | S7 |
| M6 | MEDIUM | 14 | unit 92 §4 note check, S6, AC6 | S8 |
| M7 | MEDIUM | 16 | unit 92 §4 note check, S3, S6; unit 91 AC2 | S9 |
| L1 | LOW | 10 | unit 92 AC5, §10 | S10 |

That is 9 MEDIUM and 1 LOW findings by raw id. Ids 2 and 6 share item M1, and ids 12 and 14 share
item M6. Ids 2 and 6 are the defect id 15 names at a medium grade, and unit 96 makes the shared fix;
S1 and S2 add the halves only their fixes name. Id 16 is the defect id 5 names at a medium grade, and
unit 94 makes the shared fix; S9 adds the arms only id 16's fix names.

## 2. Scope (IN)

- **S1** — id 2. A launcher word, never a path, and 92 AC4's Red-when restated. 92 S4's note quotes
  the one word `resolve_python` printed, in `TOOL-dWitnessedBar-96` S2's spelling. 92 AC4's Red-when,
  "a close that runs a derivation through a bare launcher records no resolved interpreter and passes",
  is superseded: a bare launcher word is what `resolve_python` prints, and the break is a note that
  records refusal text in its place. A note holding the first line `resolve_python` writes on
  refusal, `resolve_python: no usable python launcher.`, then `exit 0`, reads as no note through 96
  S3's row. Observed by AC1.
- **S2** — id 6. The exit graded. A derivation run that exits non-zero is recorded with that exit,
  and 96 S3's row refuses it. A note holding `resolve_python: python3 exit 5` and no `exit 0` reads as
  no note. Observed by AC2.
- **S3** — id 3. Which script ran. Every close-time run of the owner derivation that 92 S12 names, 88
  S6, AC6 and AC18, 89 S9, AC9 and AC12, and 90 AC15, runs the bytes §4 "The derivation's identity"
  extracts from 92 §4, and the note recording it carries the backticked `script <c>` on its label's
  line, `<c>` being the checksum that extraction prints. For the four 92 S4 runs, it is 92 S4's note.
  For 90 AC15, it is 92 S12's note under 90's `- AC15`. A run of unit 90's or unit 88's script carries
  another checksum and reads as no note. Observed by AC3.
- **S4** — id 4. 92 S2's third clone, isolated. The third clone of 92 S2 and AC2 is 90 AC1's first
  isolated clone: `_iso=1` is set for the canary's top-level call of `check_canary_keys` alone, and
  `check_canary_keys` stops after its first pair when `_iso` is set. It also carries 92 S2's added
  line after that call site, and a call site whose `case` handles 0, 1 and 2 alone. Its output, with
  stderr joined, holds a line holding `the canary visited 1 of`, which shows the visited failure
  fired, and its last line holds `PASS (`. 92 S2's note in unit 90's ledger carries
  `the canary visited 1 of` beside `PASS (`. Observed by AC4.
- **S5** — id 9. Every pass commit of units 89 and 90, one per dispatched pass. 92 AC5's
  `git log --format=%H -E --grep='^Pass: TOOL-dWitnessedBar-(89|90)$' cdfbd1cf..HEAD` clause is
  superseded by §4's pass-commit read. For each dispatch key of each unit that
  `read_pass_declarations` prints, it takes `pass_commit` over that key's window, bounded by the
  unit's next anchor that `next_anchor` names, as check 23 does. It prints `NO PASS COMMIT <unit>`
  and reds when either unit yields none. `build_commit` is not used here: it answers with one commit
  per unit, and 92 S5 asks of every pass. 88 S5 rules the lookup of a unit's one pass commit and
  stands. 92 S5's note in unit 90's ledger carries `pass_commit` and each sha the read printed.
  Observed by AC5.
- **S6** — id 11. Unit 91's note graded by the note check. 91 AC2's hand-written selector is
  superseded: 91 S2's note is graded by 92 §4's note check, composed as S8 states, fed
  `91|S2|90|AC2|sha)[[:space:]]*rec_sha="`, and by S8's answer count of `AC2` over unit 90's ledgers.
  92 §3's exclusion of notes by other units does not reach this row. Observed by AC6.
- **S7** — id 12. Where a note is written when a unit has two ledgers. A note sits under its answer in
  the highest-numbered ledger of its ledger unit that carries that answer. Observed by AC7.
- **S8** — id 14. Every ledger of a unit read. 92 §4's note check reads every acceptance ledger of the
  row's ledger unit, through §4 "The ledger fragments", and prints `NO LEDGER <unit>` where 92 printed
  `NO SINGLE LEDGER <unit>` for any count but one. 92 AC6's exact count is restated per ledger: for
  each answer it counts, §4's answer count prints at most 1 in each ledger and a sum of at least 1,
  which is exactly 1 where the unit has one ledger. Every note-check run of this build at the close
  runs 92 §4's script with the fragments of `TOOL-dWitnessedBar-93` S1, `TOOL-dWitnessedBar-94` S1,
  `TOOL-dWitnessedBar-96` S1 and this item, and with 96 S3's rows in place of the 92 rows that share
  their first four fields. Observed by AC8.
- **S9** — id 16. The arms only id 16's fix names. Through unit 94's anchored selector, a label
  inside an answer line is no note, and a prose mention of a label under a second answer does not
  make a correct note `MISPLACED`. The half of id 16 that lands on 91 AC2 is closed by S6, which
  grades 91's note through the same selector. Observed by AC9.
- **S10** — id 10. The per-path test through the shipped wrapper. 92 AC5's comparison "the same
  through `GEN_REGION_AWK` before and after" is superseded: for each commit `<C>` S5's read prints and
  each spec path `<p>` its diff names other than its unit's own spec,
  `check_gen_region_only "<C>^:<p>" "<C>:<p>"` returns 0, as `check_generated_render` asks it. A path
  that fails prints `BODY EDIT <unit> <C> <p>`. Observed by AC10.

## 3. Non-goals (OUT)

- Rewording the spec text of units 91 and 92. Each item supersedes a clause by name, answered in the
  ledger of the unit it lands on, as `TOOL-dWitnessedBar-92` §3 does for unit 90.
- The shared fixes units 93, 94, 95 and 96 make: the placement test, the label anchor, 92 AC5's grant
  check and the pattern column with the derivation note's spelling.
- AC11's staged exits, which 92 §4 Evidence pins. S3 makes the close-time runs name their script.
- The left-shift gates the report names: spec-lint rules for a quoted function's output, a criterion
  fed only its own text, a staged red's failing line, a `git log --grep` pass lookup, a hand-written
  ledger awk, a glob over acceptance ledgers and a hand-piped `GEN_REGION_AWK`. No clause of this
  build names them.
- New assertions in the suite, and a `New arm:` line. S4 only clones the suite, so
  `TOOL-dWitnessedBar-88` S6's derivation still names unit 90 the floor's owner.

### Edges

- **consumes-from** `TOOL-dWitnessedBar-92` — S4's note spelling and AC4's Red-when, S12's close-time runs, S2's third clone, AC5's commit half, §4's note check and note table, S6's answer count and AC6, which S1 to S10 supersede or complete (ids 2, 3, 4, 6, 9, 10, 12, 14 and 16)
- **consumes-from** `TOOL-dWitnessedBar-91` — S2's note and AC2's selector, which S6 supersedes with the note check and S9 closes on the 91 side (ids 11 and 16)
- **consumes-from** `TOOL-dWitnessedBar-93` — S1's placement line, which S8 composes into the note check (the composition S8 states)
- **consumes-from** `TOOL-dWitnessedBar-94` — S1's anchored selector, through which S6 and S9 grade, and which S8 composes into the note check (ids 11 and 16)
- **consumes-from** `TOOL-dWitnessedBar-96` — S2's note spelling and S3's pattern rows, through which S1 and S2 stage their reds and on whose note S3 adds the script token, and S1's fragments, which S8 composes into the note check (ids 2, 3 and 6)

## 4. Design

### Why one unit

M4 admits a second unit only so that the two halves build concurrently. Every item writes or grades
notes in the ledgers of units 88, 89 and 90, and S8's answer count reads the answers those notes sit
under, so any split shares those records and reads the other half's notes as an acceptance input,
which M6 clauses 2 and 3 forbid. S6's note lands in the same ledger of unit 90 that S4's and S5's
notes do. Dispatch is strictly sequential, a shared order included
(`tools/workflows/unattended-build.js:76`), so a split would buy no concurrency.

### Evidence

- `tools/lib/resolve-python.sh:39` writes `resolve_python: no usable python launcher. Each candidate
  was RUN with -c 'import sys' and` as its first refusal line, to stderr.
- Probed on 2026-10-25 through 92 §4's note check with the fragments of units 93, 94 and 96 and S8's,
  and 96 S3's row for `92|S4|88|AC6`. A note holding the backticked refusal text above and `exit 0`
  printed `NO NOTE 92 S4 resolve_python:`, and so did a note holding `resolve_python: python3 exit 5`.
- §4 "The derivation's identity" was probed on 2026-10-25. Over spec-92 it extracted 31 lines with
  checksum 788872005, and over spec-90 9 lines with checksum 2001065055. A note carrying the
  backticked `script 2001065055`, fed the row whose token is the backticked `script 788872005`,
  printed a line opening `NO NOTE 92 S4`; with `script 788872005` it printed `NOTES OK 1`. Both figures move with
  any edit to either block, so every criterion derives them at observation time.
- Spec-90 lines 298-300 define the first isolated clone: `_iso=1` set for the top-level call alone,
  and `check_canary_keys` stopping after its first pair when `_iso` is set. Spec-89 S4 (lines 69-74)
  has the canary print `gov-canary: the canary visited <n> of <m> CANARY_KEYS pairs` to stderr and
  return 3 on a visited failure.
- `pass_commit` (`tools/unattended/lib-unattended.sh:1026`) prints the first pass commit after an
  anchor, up to an optional bound, and attributes a commit by its `Pass:` trailer, splitting the
  trailer into ids (`:1069-1075`). `next_anchor` (`:1936`) names a unit's next anchor by ancestry.
  `tools/unattended/check-unattended.sh:4158-4170` takes check 23's window the same way.
  `build_commit` (`:1186`) returns one commit per unit.
- §4's pass-commit read was probed on 2026-10-25. Over `memory/builds/dWitnessedBar/RUN.md`, which
  holds no dispatch row yet, it printed `NO PASS COMMIT TOOL-dWitnessedBar-89` and
  `NO PASS COMMIT TOOL-dWitnessedBar-90`, exit 1. Pointed at `memory/builds/aBatchedArm/RUN.md` with
  its units, it printed two `PASS COMMIT` lines for `TOOL-aBatchedArm-3`, one per dispatch key, and
  three for `TOOL-aBatchedArm-1`, exit 0.
- `check_gen_region_only` (`tools/unattended/lib-unattended.sh:1137`) reads both blobs through `GIT`
  and returns 1 when either is missing. `check_generated_render` calls it as
  `check_gen_region_only "$1^:$2" "$1:$2"` (`tools/unattended/check-unattended.sh:4064`).
- Probed on 2026-10-25, over a scratch copy holding `-89-1-` and `-89-2-` ledgers with the notes in
  the `-2-` file, spec-92's script printed `NO SINGLE LEDGER 89` for each row, exit 1. With S8's
  fragments it printed `NOTES OK 2`, with or without the fragments of units 93, 94 and 96. With a
  `-2-` ledger carrying only `- AC4` and 90 S14's note under `- AC7` in the `-1-` file, it printed
  `NOTES OK 2`. With no ledger it printed `NO LEDGER 89` per row.
- Probed on 2026-10-25, a 89 ledger whose `- AC4` answer line reads
  `- AC4 — passed; see TOOL-dWitnessedBar-90 S1 and TOOL-dWitnessedBar-90 S14` printed `NOTES OK 1`
  for row `90|S1|89|AC4|` through spec-92's script, and `NO NOTE 90 S1` through the composed check.
  A ledger with that mention under `- AC4` and 90 S14's note under `- AC7` printed
  `MISPLACED 90 S14` for row `90|S14|89|AC7|` through spec-92's script and `NOTES OK 1` through the
  composed check.
- Probed on 2026-10-25, a 90 ledger whose 91 S2 note is a continuation under `- AC2` printed
  `NOTES OK 1` for row `91|S2|90|AC2|sha)[[:space:]]*rec_sha="`. Spelled as its own
  `- AC2 — TOOL-dWitnessedBar-91 S2` line, it printed a line opening `NO NOTE 91 S2` through the composed check,
  while 91 AC2's selector printed one line opening `- AC2 `, and `grep -cE '^- AC2 '` printed 2.

### The ledger fragments

S8 rewrites two lines of 92 §4's note check. Spec-92 lines 279-280 become:

```bash
  set -- $b/*TOOL-dWitnessedBar-${l}-*acceptance-ledger*
  [ -e "$1" ] || { echo "NO LEDGER $l"; bad=1; continue; }
```

On spec-92 line 281, the awk program's first rule `'/^\*\*Evidences:\*\*|^#/{o=""}` becomes
`'FNR == 1 || /^\*\*Evidences:\*\*|^#/{o=""}`, so the opener resets at each ledger, and the file
argument `' "$f")` becomes `' "$@")`. No other unit rewrites these fragments.

### The answer count

Run with `bash` from the repository root, the ledger unit and the answer number as its arguments. It
prints `AC<n> MAX <m> SUM <t>` and exits 0 only when no ledger holds the answer twice and one holds it.

```bash
t=0; m=0
for f in memory/builds/dWitnessedBar/build/*TOOL-dWitnessedBar-$1-*acceptance-ledger*; do
  [ -e "$f" ] || continue
  c=$(grep -cE "^- AC$2 " "$f"); t=$((t+c)); [ "$c" -le "$m" ] || m=$c
done
echo "AC$2 MAX $m SUM $t"
[ "$m" -le 1 ] && [ "$t" -ge 1 ]
```

### The derivation's identity

Run with `bash` from the repository root, `SCRATCH` set to the run's scratch directory. It writes the
owner derivation's bytes to `$SCRATCH/derive.sh` and prints their checksum. Every close-time run of
the derivation is `bash "$SCRATCH/derive.sh"` from the repository root.

```bash
sed -n '/^### The owner derivation$/,/^### Inventory$/p' memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-92.md \
  | awk '/^```bash$/{f=1;next} /^```$/{f=0} f' | tr -d '\r' > "$SCRATCH/derive.sh"
cksum < "$SCRATCH/derive.sh" | cut -d' ' -f1
```

### The pass-commit read

Run with `bash` from the repository root, `SCRATCH` set. It prints one
`PASS COMMIT <unit> <sha> pass_commit paths <n>` line per dispatched pass that committed, a
`BODY EDIT <unit> <sha> <path>` line per spec path edited outside its gen regions, and a
`NO PASS COMMIT <unit>` line per unit with none. It exits 0 only when neither of the last two
printed. The loop over dispatch keys is S5's; the `check_gen_region_only` line is S10's.

```bash
. tools/unattended/lib-unattended.sh
r=memory/builds/dWitnessedBar/RUN.md; sd=memory/builds/dWitnessedBar/spec/
read_pass_declarations "$r" > "$SCRATCH/rows"
bad=0
for u in TOOL-dWitnessedBar-89 TOOL-dWitnessedBar-90; do
  awk -v u="$u" '{ k = $0; sub(/^.* dispatch · item /, "", k); sub(/ · reason .*$/, "", k); split(k, x, " "); if (x[2] == u) print x[1] }' "$SCRATCH/rows" > "$SCRATCH/anchors"
  n=0
  while IFS= read -r g; do
    top=$(next_anchor "$g" "$(cat "$SCRATCH/anchors")"); [ -n "$top" ] || top=HEAD
    c=$(pass_commit "$g" "$u" "$r" "$top") || continue
    n=$((n+1)); m=0
    GIT diff-tree --no-commit-id --name-only -r "$c" > "$SCRATCH/paths"
    while IFS= read -r p; do
      case "$p" in "$sd"*) ;; *) continue ;; esac
      case "$p" in *"-spec-$u.md") continue ;; esac
      m=$((m+1))
      check_gen_region_only "$c^:$p" "$c:$p" || { echo "BODY EDIT $u $c $p"; bad=1; }
    done < "$SCRATCH/paths"
    echo "PASS COMMIT $u $c pass_commit paths $m"
  done < "$SCRATCH/anchors"
  [ "$n" -ge 1 ] || { echo "NO PASS COMMIT $u"; bad=1; }
done
[ "$bad" = 0 ]
```

### The note table

Rows in the grammar of 92 §4, with 96 S1's optional pattern column. `<c>` is the checksum §4 "The
derivation's identity" prints at observation time.

```text
92|S4|88|AC6|`script <c>`
92|S4|88|AC18|`script <c>`
92|S4|89|AC9|`script <c>`
92|S4|89|AC12|`script <c>`
92|S12|90|AC15|`script <c>`
92|S2|90|AC1|the canary visited 1 of
92|S5|90|AC13|pass_commit
91|S2|90|AC2|sha)[[:space:]]*rec_sha="
```

The backticks are part of the `script` token, so a longer checksum holding `<c>` as a prefix is no
match.

### Inventory

Minted: the note check's `NO LEDGER <unit>` line; the answer count's `AC<n> MAX <m> SUM <t>` line;
the pass-commit read's `PASS COMMIT`, `BODY EDIT` and `NO PASS COMMIT` lines; the `script <c>` note
token. No function, constant, plant, flag or file in the product. Naming cells: none apply.

### Migration

None: no stored data changes.

### Rollout

At order 50, after every other unit of the build. S5 and S10's read runs after the pass commits of
units 89 and 90 exist, at the close. S4's clone, the scratch copies and every note run at the close,
where every derivation run uses the bytes S3 extracts.

### Files touched (estimate)

- `memory/builds/dWitnessedBar/build/`

### Alternatives rejected

- **Read only the last pass's ledger, id 12's first fix.** A second pass that carries a delta leaves
  the note's answer in the first ledger, so a correct build reds.
- **Hold each unit to one ledger, id 12's third fix.** A unit that needs a second pass is a correct
  build, and M6 defines five pass kinds.
- **Sum the counts over a concatenation, as 92 AC6 would read two ledgers.** A second pass re-answers
  criteria, so a correct build prints 2.
- **`build_commit` per unit, for id 9.** It returns the earliest commit that touches something
  outside the build folder, so a later fix pass and a pass that writes only under the build folder go
  unread.
- **The literal `TOOL-dWitnessedBar-92 §4` as the script token, a way id 3's fix offered.** Any run
  can carry it, so it names no script. The checksum is of the bytes the run executed.
- **Mark AC11's exits PINNED and add a reading criterion only, id 3's second way.** It still needs a
  script identity in the notes, which S3 gives, and AC11's fixed exits are already pinned by 92 §4.

## 5. Production-readiness checklist

- security — no new write path. Scratch copies sit under the run's scratch directory and the clone
  under `%TEMP%`.
- perf / scale — one `pass_commit` walk per dispatch key of two units, one checksum, three fixture
  roots and the two-ledger copies, once, at the close.
- error / empty / loading states — no ledger prints `NO LEDGER`; no pass commit prints
  `NO PASS COMMIT`; an edited spec body prints `BODY EDIT` with its path; a missing blob fails closed
  through `check_gen_region_only`.
- observability — each pass commit is printed with its sha and path count, and each derivation note
  names its launcher, exit and script.
- risks — the note check admits a note in a lower-numbered ledger that carries its answer, where S7
  says to write it in the highest; either placement sits under an answer of that criterion.
- testing — AC1 to AC3 and AC6 to AC9 by fixture at the close; AC4 by scratch clone at the close; AC5
  and AC10 after the pass commits of units 89 and 90, AC10's red in a scratch clone.
- migration — none.
- user docs — none under `help/`; no user-facing surface changes.

## 6. Acceptance criteria

The note check below is 92 §4's script composed as S8 states, fed rows on stdin.

- **AC1** — In a scratch root holding one
  `memory/builds/dWitnessedBar/build/*TOOL-dWitnessedBar-88-*acceptance-ledger*` file whose `- AC6`
  note, labelled `TOOL-dWitnessedBar-92 S4`, holds the backticked
  `resolve_python: no usable python launcher. Each candidate was RUN` and then `exit 0`, the note
  check fed 96 S3's row for `92|S4|88|AC6` prints `NO NOTE 92 S4 resolve_python:` and exits 1.
  Red when: a note recording the resolver's refusal passes as a resolved launcher.
  fixture: a scratch root under the run's scratch directory.
- **AC2** — In the same scratch root with the note holding `resolve_python: python3 exit 5` and no
  `exit 0`, the same check prints `NO NOTE 92 S4 resolve_python:` and exits 1.
  Red when: a derivation that exited non-zero is recorded as a run that passed.
  fixture: a scratch root under the run's scratch directory.
- **AC3** — At the close, with `<c>` printed by §4 "The derivation's identity", the note check fed the
  first five rows of §4's note table prints `NOTES OK 5`. In a scratch copy of 88's ledger whose
  `- AC6` note carries the checksum of unit 90's owner-derivation block, extracted from spec-90 by the
  same `sed` and `awk`, the row for `92|S4|88|AC6` prints a line opening `NO NOTE 92 S4` and exits 1.
  Red when: a close-time run of unit 90's script is recorded as a run of unit 92's.
  figure: `<c>` is DERIVED at observation time; it read 788872005 on 2026-10-25.
  permission: the ledgers are written at the close.
- **AC4** — In 92 AC2's third clone, built as S4 states, the arm's output with stderr joined holds a
  line holding `the canary visited 1 of`, and its last line holds `PASS (`. The note check fed
  `92|S2|90|AC1|the canary visited 1 of` prints `NOTES OK 1`.
  Red when: the third clone ends `PASS (` because no visited failure fired.
  fixture: scratch clones under `%TEMP%/<short-name>`.
  permission: the arm's run is the main loop's, at the close.
- **AC5** — At the close, §4's pass-commit read prints at least one `PASS COMMIT` line for each of
  `TOOL-dWitnessedBar-89` and `TOOL-dWitnessedBar-90`, no `NO PASS COMMIT` line, and exits 0. The
  note check fed `92|S5|90|AC13|pass_commit` prints `NOTES OK 1`.
  Red when: either unit's pass commits are missed and the read passes on none.
  figure: the number of lines is DERIVED from the dispatch rows at observation time. Before either
  unit dispatches, the read prints both `NO PASS COMMIT` lines and exits 1, as probed on 2026-10-25.
  permission: the ledger is written at the close.
- **AC6** — At the close, the note check fed `91|S2|90|AC2|sha)[[:space:]]*rec_sha="` prints
  `NOTES OK 1`, and §4's answer count run as `90 2` exits 0. In a scratch copy of unit 90's ledger
  where 91 S2's note is spelled as its own `- AC2 — TOOL-dWitnessedBar-91 S2` line, the check prints a
  line opening `NO NOTE 91 S2` and exits 1, and the answer count prints `AC2 MAX 2 SUM 2` and exits 1.
  Red when: 91's note doubles 90's `- AC2` answer and passes.
  fixture: a scratch copy of the build's ledgers under the run's scratch directory.
  permission: the ledger is written at the close.
- **AC7** — In a scratch root holding `-89-1-` and `-89-2-` acceptance ledgers that both answer
  `- AC4` and `- AC7`, with the notes of 90 S1 and 90 S14 under those answers in the `-2-` file, the
  note check fed `90|S1|89|AC4|` and `90|S14|89|AC7|` prints `NOTES OK 2` and exits 0. Spec-92's
  unreplaced script prints `NO SINGLE LEDGER 89` twice and exits 1 on the same root.
  Red when: a unit with a second pass reds a correctly placed note.
  fixture: a scratch root under the run's scratch directory.
- **AC8** — In a scratch root whose `-89-2-` ledger carries only `- AC4` with 90 S1's note, and whose
  `-89-1-` ledger carries `- AC4` and `- AC7` with 90 S14's note under `- AC7`, the note check fed the
  same two rows prints `NOTES OK 2`, and the answer count prints `AC7 MAX 1 SUM 1` for `89 7`. With
  the `-2-` ledger holding `- AC4` twice, the count for `89 4` prints a line holding `MAX 2` and exits 1. With no 89
  ledger, the check prints `NO LEDGER 89` per row and exits 1. At the close, the note check fed every
  row of 92 §4's note table, 96 S3's five rows standing in for the rows that share their first four
  fields, prints `NOTES OK 29`, and the answer count exits 0 for each answer 92 AC6 counts.
  Red when: a delta second pass reds a note placed under its answer in the first ledger, or a doubled
  answer in one ledger passes.
  fixture: scratch roots under the run's scratch directory.
  figure: 29 is PINNED, the rows of 92 §4's note table at rev-1, which 96 S3 restates without adding
  one.
  permission: the ledgers are written at the close.
- **AC9** — In a scratch root whose 89 ledger reads
  `- AC4 — passed; see TOOL-dWitnessedBar-90 S1 and TOOL-dWitnessedBar-90 S14` with no continuation
  line, the note check fed `90|S1|89|AC4|` prints `NO NOTE 90 S1` and exits 1. In one whose `- AC4`
  answer line mentions `TOOL-dWitnessedBar-90 S14` and whose `- AC7` answer carries 90 S14's
  continuation note, the check fed `90|S14|89|AC7|` prints `NOTES OK 1`.
  Red when: a label in an answer line passes as a note, or a prose mention makes a correct note
  `MISPLACED`.
  fixture: a scratch root under the run's scratch directory.
- **AC10** — At the close, every `PASS COMMIT` line of AC5's read carries no `BODY EDIT` line beside
  it. In a scratch clone of the built tree, with a dispatch row of `TOOL-dWitnessedBar-89` declaring
  `memory/builds/dWitnessedBar/spec/` appended to `memory/builds/dWitnessedBar/RUN.md` at an anchor
  that is the clone's `HEAD`, and then a commit with the trailer `Pass: TOOL-dWitnessedBar-89` that
  edits a §6 line of spec 88, the read prints
  `BODY EDIT TOOL-dWitnessedBar-89 <sha> memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-88.md`
  and exits 1.
  Red when: a pass commit edits another unit's spec outside its gen regions and the read passes.
  fixture: a scratch clone under `%TEMP%/<short-name>`.
  cost: a clone and two staged commits, at the close.

## 7. Gates

`memory hygiene` · `recall floor` · `recall floor arms`

`recall floor` and `recall floor arms` are owed for the ledgers under `memory/`. AC4 reads 92 AC2's
clones at the close; this unit adds no arm and moves none, so it declares no `New arm:` line, and
`TOOL-dWitnessedBar-88` S6's derivation still names unit 90 the floor's owner.

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a) `**Derived:**`
  naming `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of a repaired unit's clause. Units 91 and 92 are
  themselves derived and carry no clause, so (b) has nothing to split; veto 1 discards it. RESOLVED
  (agent, 2026-10-25, delegated): (a), rung 3, the precedent `TOOL-dWitnessedBar-90` §8 F1 set.
  widens: none · relaxes: none
- **F2 — Which ledgers does the note check read when a unit has two (ids 12 and 14)?** Options: (a)
  the last pass's ledger alone; (b) every ledger of the unit, with the answer count held per ledger;
  (c) a rule that each unit closes with one ledger. (c) reds a correct build that needs a second
  pass, and (a) reds one whose second pass carries a delta. (b) passes both and still refuses a
  doubled answer within a ledger. RESOLVED (agent, 2026-10-25, delegated): (b), rung 3, the most
  feature-rich survivor.
  widens: none · relaxes: none
- **F3 — What names the script a close-time run used (id 3)?** Options: (a) a checksum of the
  extracted bytes the run executed; (b) the literal `TOOL-dWitnessedBar-92 §4`. (b) can be written by
  a run of any script. (a) is derived from the bytes, at no more cost. RESOLVED (agent, 2026-10-25,
  delegated): (a), rung 3, the most feature-rich survivor.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, promoted from the round-1 spec audit of units 91 and 92: 9
  MEDIUM and 1 LOW findings, batched.

## 10. Reuse audit

Each item extends the seam its finding names. S5 and S10 call `read_pass_declarations`,
`pass_commit`, `next_anchor` and `check_gen_region_only` from `tools/unattended/lib-unattended.sh`, the
same seams check 23 reads a pass's window through (`tools/unattended/check-unattended.sh:4158-4170`
and `:4064`), and spell no second rule. S6, S8 and S9 extend 92 §4's note check rather than keeping
91's hand-written awk beside it. S1 to S3 quote `resolve_python` (`tools/lib/resolve-python.sh`).
`python tools/codebase-map/reuse_lookup.py "find every pass commit of a dispatched unit in a build"`
ranked `build`, `units`, `build_commit` and `build_fixture`; `build_commit` answers one commit per
unit, so the per-dispatch seams named above are the ones extended.

Recall terms used: `python tools/memory-recall/query.py "how are a unit's several acceptance ledgers read when it has a second pass" --terms "acceptance ledger second pass pass number glob note check pass_commit dispatch row script identity cksum"`
