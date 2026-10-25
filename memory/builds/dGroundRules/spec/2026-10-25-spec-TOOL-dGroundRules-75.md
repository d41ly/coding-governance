# TOOL-dGroundRules-75 — a cap of 0 is unchecked in every enforcer, as the budgets switch says

**Status:** CLOSED · rev-1 · 2026-10-25 · node d · Tier-1 · base fce5603f · streams tooling · order 26

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dGroundRules-75-ledger.md](../build/2026-10-25-build-TOOL-dGroundRules-75-ledger.md) | journal | — |
| [2026-10-25-prompt-TOOL-dGroundRules-75-1-spec-writer.md](../prompts/2026-10-25-prompt-TOOL-dGroundRules-75-1-spec-writer.md) | journal | — |
| [2026-10-25-prompt-TOOL-dGroundRules-75-spec-brief.md](../prompts/2026-10-25-prompt-TOOL-dGroundRules-75-spec-brief.md) | research | — |
| [2026-10-25-review-TOOL-dGroundRules-72-79-closing-diff-round2.md](../reviews/2026-10-25-review-TOOL-dGroundRules-72-79-closing-diff-round2.md) | diff-review | TOOL-dGroundRules-72 TOOL-dGroundRules-73 TOOL-dGroundRules-74 TOOL-dGroundRules-76 TOOL-dGroundRules-77 TOOL-dGroundRules-78 TOOL-dGroundRules-79 |

<!-- /gen:spec-records -->

## 1. Goal

The budgets switch reads a cap value of 0 as unchecked. `check_cap` says so (`tools/policy/budgets.py:309-310`),
`check_budgets` accepts 0 (`:349-350`), and `help/size-caps.md:77` promises it. But six enforcers re-derive the
comparison themselves and read 0 as a 0 ceiling or as their old constant. So `budgets.<cap> = 0` passes
`policy.py check` and then refuses, or warns, on every subject. This is item M1 of the closing review, round 1,
merging findings 2, 4 and 5. This unit makes each of those enforcers skip its comparison at 0. It also adds a
zero run to every census case of a switch cap, so a new cap cannot join without it.

## 2. Scope (IN)

- **S1** — The template-size gate, `tools/check-template-size.sh`. Check 6, the pair term at `:241`, opens
  with `[ "$MAX_BYTES" -gt 0 ]`. Check 2 at `:254` opens with the same test. When `MAX_BYTES` is 0, the OK
  line at `:347` prints `template-size OK — <name>: <bytes> bytes, unchecked` and runs no awk division. Each
  is spelled as §4 "The enforcers" gives. Observed by AC1 and AC2.
- **S2** — The hygiene checker, `tools/memory-tree/check-memory-hygiene.sh`. Check 6's byte axis at `:1126`
  reads `ob = cb>0 && sz>cb`. Check 7's comparison at `:1241` opens with `cap > 0 &&`. The conf-layer
  zero refusal at `:196-208` does not change. Observed by AC3 and AC4.
- **S3** — The kickoff manifest checker, `skills/session-kickoff/manifest-check.sh`. Check 7 at `:1359`
  opens with `[ "$MAX_MANIFEST_BYTES" -gt 0 ] &&`. Check 8's awk pattern at `:1380` opens with
  `cap+0 > 0 &&`. Check 11's `over()` at `:1585` adds `cap+0 > 0 &&` after `n > 0 &&`. Observed by AC5.
- **S4** — The roster verb, `tools/roles/handoff.py`. The line `cap = cap or ROSTER_LINE_MAX` at `:518` is
  cut, and both comparisons at `:535` and `:537` open with `cap and`. Observed by AC6.
- **S5** — The render engine, `tools/playbook/render_playbook.py`. `read_one_line_cap` stores `a.value`
  at `:688`, never `a.value or ONE_LINE_MAX`. `check_one_line_regions` compares at `:732` only when
  `limit` is truthy. Observed by AC7.
- **S6** — The recall export, `tools/memory-recall/query.py`. `read_export_cap` returns `a.value` at
  `:1288`. `export` compares at `:1311` and `:1315` only when `cap` is truthy. Its written line at
  `:1327` says `unchecked` in place of `of 0 B`. Observed by AC8.
- **S7** — The census cases, `tools/policy/check_policy.py`. A new `derive_zero_plant(cap, p)` builds a
  zero variant of a row's plant. `run_cap_case` runs it as a third mode, `zero`, for every `switch` row
  that is not a family. It runs in the same pool as `warn` and `refuse`. The module docstring's
  census-case sentence names the third run. Observed by AC1, AC3, AC4, AC5, AC6, AC7, AC8 and AC9.
- **S8** — The template-size suite, `tools/check-template-size.test.sh`. Two arms, A19e and A19f, go
  after A23. They are §4 "The suite arms", and they grade the pair term at 0, which no census plant
  reaches. Observed by AC2.

## 3. Non-goals (OUT)

- The conf-layer refusal of a zero byte or char cap in the hygiene checker (`check-memory-hygiene.sh:196-208`).
  An adopter's conf 0 still aborts, as it does today. Only the policy layer's 0 is unchecked.
- `help/size-caps.md:77` says a 0 is unchecked "as it does in every legacy home". That stays false for
  the hygiene conf's byte and char keys after this unit. It is a document, so it is a separate unit (M2),
  and the main loop files it as an ask.
- Routing every enforcer through `budgets.check_cap`'s verdict in place of its own comparison (§4
  "Alternatives rejected").
- The family caps (`line-length`, `readme-slot`, `role-body`), which take no value from the policy file,
  and the outside caps, which the switch never answers.
- The other findings of the report, the inherited reds the close recorded (unattended shards 1, 3, 5
  and 7, and the hygiene partition arm), and any other spec. Units 73 and 76 touch
  `tools/policy/policy.py` and unit 77 touches `check_policy.py`. This unit cites `check_policy.py` by
  symbol so their lines may move.

### Edges

none

This unit carries out the follow-through of `TOOL-dGroundRules-21` (CLOSED), whose S28 made 0 a valid,
unchecked value, and `TOOL-dGroundRules-9` (CLOSED), whose enforcers read the switch. That unit's
`budgets-zero-cap` case planted only `index-lines`, where check 6 already guards `cl>0`.

## 4. Design

### Evidence

Every premise was re-read at `fce5603f8`, and holds:

- The switch answers 0. In a scratch repository, with `enforce = "refuse"` and a 0 set for five caps,
  `budgets.py resolve` printed `roster-line	0	refuse	file`, and likewise for `one-line-rule`,
  `recall-export`, `manifest-line` and `index-bytes`.
- Template-size, check 2. A 100-byte `AGENTS.md`, no limits row and `"AGENTS.md" = 0` under refuse
  printed `TEMPLATE-SIZE check 2 FAILED — ... 100 over 0`, then budgets' own `BUDGET OK — AGENTS.md ·
  AGENTS.md · 100 bytes, unchecked`, and exited 1.
- Template-size, check 6. The same repository shape, with the build method carrying a `**Budget:` line
  and `"memory/guides/BUILD-METHOD.md" = 0`, printed `check 6 FAILED ... its declaration (source file)
  says 0` and exited 6. This is `f75.sh`, §5.
- The constants come back. `handoff.py:518`, `query.py:1288` and `render_playbook.py:688` each turn 0
  into their constant (read).
- Manifest and hygiene take the 0. `manifest-check.sh:1339-1341` assigns it, and so does the hygiene
  checker's `read_cap_modes`, at `check-memory-hygiene.sh:528`. Their awks then compare against it (read).
- Every census row, measured. The plant each row's `CAP_CASES` entry builds was wrapped in §4 "The zero
  run"'s `derive_zero_plant` by a scratch script, built under refuse and run through `run_cap_plant`.
  18 of the 24 switch rows that are not families were RED. The six template-size rows failed check 2,
  and the hygiene byte and char rows failed check 6 or 7. `one-line-rule`, `roster-line` and
  `recall-export` refused at their constant. The three manifest rows failed checks 7, 8 and 11
  "over the 0-byte limit". Six were GREEN, because their enforcer already reads 0 as unchecked:
  `memory/builds/*/spec/` (through `check_cap`), the four hygiene line caps (`cl>0`) and
  `universal-gotchas` (`if budget:`). So the zero run's predicate and its plants both work at HEAD,
  before any enforcer changes.

No premise is dropped.

### The enforcers

Each enforcer takes the rule `check_cap` states: a value of 0, or none, is unchecked. None of them
re-reads the policy file.

`tools/check-template-size.sh`. `MAX_BYTES` is the integer budgets printed. It is never `-`, because the
gate always hands `default:49152` in. The three sites:

```
if [ "$MAX_BYTES" -gt 0 ] && [ -n "$declared" ] && [ -n "$bline" ]; then      # :241, check 6
if [ "$MAX_BYTES" -gt 0 ] && [ "$bytes" -gt "$MAX_BYTES" ]; then              # :254, check 2
[ "$MAX_BYTES" -gt 0 ] || { printf 'template-size OK — %s: %d bytes, unchecked\n' "$name" "$bytes"; exit 0; }   # above :347
```

The third line sits directly above the OK `printf`, after the `WARNED` exit, so the ratchet lines still
print first. The pair term's comment block above `:241` gains one sentence: at 0 there is no ceiling for
the prose to agree with. `budgets-correctness-kept` plants a non-zero row and still reds at check 6.

`check-memory-hygiene.sh`. At `:1126`, `ob = sz>cb` becomes `ob = cb>0 && sz>cb`, the guard the line axis
already has. At `:1241`, the condition becomes `cap > 0 && length(line) > cap && ...`. One comment line
above each says that a policy-layer 0 is unchecked, and that the conf layer refuses a 0 at load.

`manifest-check.sh`. The guard is `[ "$MAX_MANIFEST_BYTES" -gt 0 ] &&` ahead of check 7's comparison.
In check 8's awk the pattern becomes `cap+0 > 0 && length(ln) > cap+0`, and in check 11's `over()` the
test becomes `n > 0 && cap+0 > 0 && len > cap+0`. With nothing printed, `c8` and `c11` are empty and
neither check fires. The `MAX_MANIFEST_BYTES` environment override reads 0 the same way.

`handoff.py`, `render_playbook.py` and `query.py` each keep the switch's value, and each comparison opens
with the value's truth. That also covers a `None`, which `check_cap` reads as unchecked too. The
recall export's written line becomes `wrote <dest> (<size> B, unchecked)` when `cap` is 0. No reader
outside each file reads the changed values. A grep for `read_export_cap`, `read_one_line_cap`,
`check_one_line_regions`, `_ONE_LINE_ANSWERS` and `print_roster` over `tools/` and `skills/` names only
the defining files, plus `check_policy.py`, which reads the three constants by name
(`read_source_number`) and is unaffected. Nothing parses `template-size OK` but the template-size suite's
A0, A1 and A4. They run at non-zero ceilings and keep the `/ <n> bytes` form.

### The zero run

`derive_zero_plant(cap, p)` returns `p` with the row's value moved to the policy file at 0. A value
held in both homes refuses (`budgets.py`, "held in both homes"), so the plant also takes it out of its
legacy home:

```
def derive_zero_plant(cap, p):
    """`p`, a census row's plant, with the row's value at 0 in the policy file and none in its legacy
    home, so the reader answers 0 from the file: a `limits:` row's line left out of the limits file the
    plant writes, a `conf:` key's assignment left out of that conf, a `constant:` home untouched."""
    form, _c, rest = cap.home.partition(":")
    files = dict(p["files"])
    if form == "limits":
        lrel = budgets.derive_limits_rel()
        files[lrel] = "".join(ln for ln in files[lrel].splitlines(True) if not ln.startswith(cap.name + "\t"))
    elif form == "conf":
        path, _c, key = rest.rpartition(":")
        rx = re.compile(budgets.SHELL_KEY.format(re.escape(key)))
        if path in files:
            files[path] = "".join(ln for ln in files[path].splitlines(True) if not rx.match(ln))
    return {**p, "files": files, "extra": f'"{cap.name}" = 0\n'}
```

`extra` is set, never appended to. The hygiene plant already sets `"<cap>" = 10` for a cap its engine
leaves at 0, and a second key would not parse. In `run_cap_case`'s `switch` branch, the pool takes
`max_workers=3` and the modes `("warn", "refuse", "zero")`. A `zero` mode runs
`run_cap_mode(t / "zero", cap, lambda c: derive_zero_plant(c, plant(c)), "refuse")`, but only when
`not cap.family`. Its check is:

```
("zero", "a value of 0 under refuse: exit 0, no breach line, no awk error",
 rc == 0 and p["refuse"] not in out and "BUDGET WARN" not in out and "awk:" not in out, f"exit {rc} · {said}")
```

`said` is `render_said(out, p["refuse"])`. The plant's subject stays over every positive value, so only
a 0 read as unchecked passes it. Under `refuse` no cap warns, so a `BUDGET WARN` line means a breach was
graded at 0. `awk:` catches the template-size OK line dividing by 0. That is the staged break of AC1,
since `awk "BEGIN{print 5/0*100}"` prints `awk: cmd. line:1: error: division by zero attempted` on this
node.

The population is the census. `arm_cap_census` already reds a row with no `CAP_CASES` entry
(`check_policy.py`, `arm_cap_census`, "has no budgets-cap- case"). So a new switch cap gets its zero run
with its case, which is the report's left-shift gate. The checklist entry the report offers "where no
gate fits" is not needed, because this gate fits.

What the zero run does not check: a family or outside row, which takes no policy value. A 0 held in a
legacy home, such as a limits row, a conf key or a code constant, is not checked either. The
template-size guard reads `MAX_BYTES` from any source, so it holds there, but no plant sets it. The
pair term at 0 is not reached either, because no census plant carries a `**Budget:` line. S8 covers that.

### The suite arms

After A23 in `tools/check-template-size.test.sh`:

```
# --- A19e/A19f · a cap of 0 is unchecked (TOOL-dGroundRules-75) --------------------------------
build_scratch_repo '# no rows\n' "${REFUSE}\"$BM\" = 0\n"
printf '**Budget: <=27648 bytes, <=350 lines**\nbody\n' > "$S/$BM"
expect_out "A19e a cap of 0 is unchecked under refuse, its budget line never compared" \
  "BUILD-METHOD.md: 44 bytes, unchecked" 0 run_gate_in "$BM" "" "$TMP/hw-zero"
expect_absent "A19f ...and the OK line runs no division by the 0" "awk:" 0 run_gate_in "$BM" "" "$TMP/hw-zero"
```

At `fce5603f8` the same scenario exits 6 at check 6 (§4 "Evidence"), so A19e reds there. A19f reds
with the OK-line guard alone staged out. The suite has no assertion floor.

### Alternatives rejected

- Every enforcer runs `budgets.py check` and obeys its exit code and verdict line. The report offers this
  as the better template-size form, so a shell keeps no comparison of its own. It costs a second
  Python start on every run of seven template-size legs. The shell would still need the value to print
  its OK line, and the other five enforcers would keep their own comparison anyway. One guard per site
  gives `check_cap`'s answer: 0 unchecked, else `measured <= value` passes. The zero run grades all six
  enforcers against that answer.
- Extending `budgets-zero-cap` with `index-bytes`, `entry-chars` and a manifest cap, as the report
  lists. The zero run covers those three and every other switch row, so three more hand-picked plants
  would be a second copy of one observation.
- The finder's fix for findings 4 and 5, judged UNSOUND. The report gives the skeptic's corrected fix,
  and S2 to S6 are that fix.

### Rollout

The builder sets this spec's status from DEFERRED to INPROGRESS before its first write. Scratch-guard
admits writes under `ROUTED_PATHS` for a Tier-1 unit only at INPROGRESS, or at SPECCED once graded.

### Inventory

One name minted: `derive_zero_plant`, in `tools/policy/check_policy.py`, beside the `derive_*_plant`
functions it wraps.

### Files touched (estimate)

- `tools/check-template-size.sh`
- `tools/check-template-size.test.sh`
- `tools/memory-tree/check-memory-hygiene.sh`
- `skills/session-kickoff/manifest-check.sh`
- `tools/roles/handoff.py`
- `tools/playbook/render_playbook.py`
- `tools/memory-recall/query.py`
- `tools/policy/check_policy.py`

## 5. Acceptance criteria

All commands run from the repository root of the pass's worktree. Each `--fixture <case>` run names one
case, which makes it the module's single-case runner. It prints one `policy-fixture:` line per check,
and as its last line `policy-fixture: <n> assertion(s) executed · <w> wrong`. A zero run that holds
prints a line opening `policy-fixture: budgets-cap-<name> · zero · a value of 0 under refuse` that does
not carry `WRONG`.

The second criterion uses a scratch script. It builds the A19e repository, runs the gate there, and writes its output and
exit to the file it is given:

```
cat > "$TEMP/f75.sh" <<'EOF'
G="$PWD/tools/check-template-size.sh"; S="$(dirname "$1")/f75repo"; rm -rf "$S"
mkdir -p "$S/tools" "$S/.governance" "$S/memory/guides"
printf '# no rows\n' > "$S/tools/template-size-limits.txt"
printf '[budgets]\nenforce = "refuse"\n"memory/guides/BUILD-METHOD.md" = 0\n' > "$S/.governance/policy.toml"
printf '**Budget: <=27648 bytes, <=350 lines**\nbody\n' > "$S/memory/guides/BUILD-METHOD.md"
git -C "$S" init -q && git -C "$S" symbolic-ref HEAD refs/heads/main && git -C "$S" add -A 2>/dev/null
git -C "$S" -c user.name=t -c user.email=t@t.test -c commit.gpgsign=false commit -qm fixture
(cd "$S" && bash "$G" memory/guides/BUILD-METHOD.md "" "$S.hw" > "$1" 2>&1; echo "exit $?" >> "$1")
EOF
```

- **AC1** — When `python tools/policy/check_policy.py --fixture budgets-cap-AGENTS.md` runs, it prints
  the zero line without `WRONG`, and its last line ends `· 0 wrong`.
  Red when: check 2's `[ "$MAX_BYTES" -gt 0 ]` guard is staged out. The zero line then reads `WRONG: exit
  1 · TEMPLATE-SIZE check 2 FAILED`, as measured at `fce5603f8`. Red also when only the OK-line guard is
  staged out: the output carries `awk:`.
- **AC2** — When `bash "$TEMP/f75.sh" "$TEMP/f75.out"` runs, `$TEMP/f75.out` holds the line
  `template-size OK — BUILD-METHOD.md: 44 bytes, unchecked` and ends `exit 0`. Also, `grep -c "A19e a cap of 0 is unchecked" tools/check-template-size.test.sh` prints `1`.
  Red when: the pair term's guard is staged out. The file then holds `check 6 FAILED` and ends `exit 6`,
  as it did at `fce5603f8`.
- **AC3** — When `python tools/policy/check_policy.py --fixture budgets-cap-index-bytes` runs, it prints
  the zero line without `WRONG`, and its last line ends `· 0 wrong`.
  Red when: `ob = cb>0 && sz>cb` is staged back to `ob = sz>cb`. The zero line reads `WRONG: exit 1 ·
  HYGIENE check 6 FAILED`, as measured at `fce5603f8`.
- **AC4** — When `python tools/policy/check_policy.py --fixture budgets-cap-entry-chars` runs, it prints
  the zero line without `WRONG`, and its last line ends `· 0 wrong`.
  Red when: check 7's `cap > 0 &&` is staged out. The zero line reads `WRONG: exit 1 · HYGIENE check 7
  FAILED`, as measured at `fce5603f8`.
- **AC5** — When each of `python tools/policy/check_policy.py --fixture budgets-cap-manifest-bytes`, `python tools/policy/check_policy.py --fixture budgets-cap-manifest-line` and `python tools/policy/check_policy.py --fixture budgets-cap-manifest-trap` runs, each prints its zero line without `WRONG`, and its last line ends `· 0 wrong`.
  Red when: the guard of check 7, check 8 or check 11 is staged out. That case's zero line then reads
  `WRONG: exit 1 · MANIFEST check 7 FAILED`, `check 8 FAILED` or `check 11 FAILED`, each "over the 0-byte"
  limit or cap, as measured at `fce5603f8`.
- **AC6** — When `python tools/policy/check_policy.py --fixture budgets-cap-roster-line` runs, it prints
  the zero line without `WRONG`, and its last line ends `· 0 wrong`.
  Red when: `cap = cap or ROSTER_LINE_MAX` is restored. The zero line reads `WRONG: exit 1 · handoff:
  roster line for gov-builder is 332 characters, past the 200`, as measured at `fce5603f8`.
- **AC7** — When `python tools/policy/check_policy.py --fixture budgets-cap-one-line-rule` runs, it
  prints the zero line without `WRONG`, and its last line ends `· 0 wrong`.
  Red when: `a.value or ONE_LINE_MAX` is restored in `read_one_line_cap`. The zero line reads `WRONG:
  exit 1 · render-playbook: REFUSED — line 2: ... past the 200`, as measured at `fce5603f8`.
- **AC8** — When `python tools/policy/check_policy.py --fixture budgets-cap-recall-export` runs, it
  prints the zero line without `WRONG`, and its last line ends `· 0 wrong`.
  Red when: `a.value or EXPORT_CAP` is restored in `read_export_cap`. The export refuses and the zero
  line reads `WRONG: exit 1`, as measured at `fce5603f8`.
- **AC9** — When `python tools/policy/check_policy.py --fixture budgets-cap-line-length` runs, it prints
  no line carrying `· zero ·`. When `python tools/policy/check_policy.py --fixture budgets-cap-universal-gotchas` runs, it prints the zero line without `WRONG`.
  Red when: the zero mode's `not cap.family` condition is staged out. `budgets-cap-line-length` then
  prints a zero line, because the run reaches a family row that takes no policy value.

## 6. Gates

`policy fixtures` · `govkit acceptance matrix` · `playbook render selftest` · `manifest-check self-test` · `scratch-guard self-test` · `lexicon naming predicates` · `template size gate selftest` · `template size <=48KiB` · `charter size` · `build-method size` · `unattended protocol size` · `unattended skill size` · `kickoff engine size <=18KiB` · `kickoff-manifest ratchet` · `memory hygiene` · `memory-hygiene self-test` · `memory-recall kit selftest` · `roles adopter self-test` · `playbook render wiring` · `harness arms (fail branches armed or pinned)` · `shell hygiene (a loop fed by a command substitution)` · `shell hygiene (a location probe asked from a moved directory)` · `spec tokens (a spec's own names resolve)`

The first six are the legs `derive_guarded_legs` owes at `fce5603f8`, over the eight touched files:

- `policy fixtures` is owed by every file but the template-size suite.
- `govkit acceptance matrix` and `playbook render selftest` are owed by `render_playbook.py`, through `tools/playbook/`.
- `manifest-check self-test`, `scratch-guard self-test` and `lexicon naming predicates` are owed by
  `manifest-check.sh`, through `skills/session-kickoff/`.

`check-template-size.test.sh` owes no guarded leg. The rest carry no guard, or only a broad one, and
read a touched file:

- The seven template-size legs run the gate.
- `template size gate selftest` runs its suite.
- `kickoff-manifest ratchet` runs the manifest checker.
- `memory hygiene` and `memory-hygiene self-test` run the hygiene checker.
- `memory-recall kit selftest` reads `query.py`.
- `roles adopter self-test` runs `handoff.py roster`.
- `playbook render wiring` runs the render engine.
- `harness arms` and the two shell-hygiene scans read the touched shell files.

No floor or pinned count moves. The template-size suite and the policy fixtures have no assertion floor,
and the census cases pin no assertion count. The `policy fixtures` ceiling in `tools/gate-legs.json` does
not move: the zero run shares its case's pool, so a case's wall time stays bounded by its slowest mode.

New arm: tools/policy/check_policy.py --fixture · covers AC1 AC3 AC4 AC5 AC6 AC7 AC8 AC9 · the zero run of every budgets-cap- case of a switch row that is not a family, red at fce5603f8 on 18 of its 24 rows by the scratch probe of §4 · none
New arm: tools/check-template-size.test.sh · covers AC2 · A19e and A19f, staged by the pair-term guard (exit 6 at check 6) and by the OK-line guard (awk: in the output) · none

## 7. Open questions

none

## 8. Revision log

- rev-1 · 2026-10-25 · initial draft from the closing diff review's item M1 (findings 2, 4 and 5) and its
  spec brief, grounded at `fce5603f8`. Every premise held: on the switch's own answers, the gate's run in
  a scratch repository, and a scratch wrap of every census plant at 0 (18 rows red, 6 already green).
  Specs finding 2's SOUND guard for template-size, and the skeptic's corrected fix for findings 4 and 5.
  The report's left-shift gate is specced inside the unit as the census cases' zero run. It is one
  small arm of the same mechanism, and it covers the three plants the report would add to
  `budgets-zero-cap`. The `budgets.py check` routing is rejected in §4. The help page's legacy-home
  clause is named in §3 as a separate ask. The brief, untracked when this draft was written:

```
memory/builds/dGroundRules/prompts/2026-10-25-prompt-TOOL-dGroundRules-75-spec-brief.md
```

## 9. Reuse audit

This unit builds no new mechanism. It extends the switch's rule, `budgets.check_cap` (`budgets.py:304`),
into the six enforcers that compare for themselves, with one guard per site. Its gate extends the census
cases, `run_cap_case` and `CAP_CASES` in `tools/policy/check_policy.py`, with a third mode that wraps each
row's existing plant. `derive_zero_plant` reuses `budgets.SHELL_KEY` and `budgets.derive_limits_rel`
rather than parsing either home again.
`python tools/codebase-map/reuse_lookup.py "a cap value of 0 read as unchecked by every size cap enforcer"`
ranked `resolve_caps` (`tools/policy/budgets.py`, fan-in 7, SEAM) as the one cap seam. The rest were
`read` name stems. That seam is the one the enforcers already call.
The recall probe returned the review item itself, `TOOL-dGroundRules-9`'s cap inventory, and
`TOOL-dGroundRules-21`'s AC28, the `budgets-zero-cap` case that planted only `index-lines`.

Recall terms used: `python tools/memory-recall/query.py "a cap of 0 means unchecked in the budgets switch but enforcers read it as a zero ceiling" --terms "check_cap unchecked budgets-zero-cap CAP_CASES ROSTER_LINE_MAX EXPORT_CAP ONE_LINE_MAX MAX_MANIFEST_BYTES"`
