# TOOL-dTrueNorth-27 — the nine bar legs this build turned red, each cleared at its cause

**Status:** CLOSED · rev-3 · 2026-10-22 · node d · Tier-2 · base 271aa59d · streams tooling · order 11

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-21-build-TOOL-dTrueNorth-27-ledger.md](../build/2026-10-21-build-TOOL-dTrueNorth-27-ledger.md) | journal | — |
| [2026-10-22-build-TOOL-dTrueNorth-27-bar1.log](../build/2026-10-22-build-TOOL-dTrueNorth-27-bar1.log) | journal | — |
| [2026-10-22-build-TOOL-dTrueNorth-27-deviation-28.md](../build/2026-10-22-build-TOOL-dTrueNorth-27-deviation-28.md) | deviation | — |
| [2026-10-22-build-TOOL-dTrueNorth-27-deviation-29.md](../build/2026-10-22-build-TOOL-dTrueNorth-27-deviation-29.md) | deviation | — |
| [2026-10-22-build-TOOL-dTrueNorth-27-deviation-30.md](../build/2026-10-22-build-TOOL-dTrueNorth-27-deviation-30.md) | deviation | — |
| [2026-10-21-prompt-TOOL-dTrueNorth-27-build-brief.md](../prompts/2026-10-21-prompt-TOOL-dTrueNorth-27-build-brief.md) | journal | — |
| [2026-10-22-prompt-TOOL-dTrueNorth-27-1-spec-writer.md](../prompts/2026-10-22-prompt-TOOL-dTrueNorth-27-1-spec-writer.md) | journal | — |
| [2026-10-22-prompt-TOOL-dTrueNorth-27-2-spec-writer.md](../prompts/2026-10-22-prompt-TOOL-dTrueNorth-27-2-spec-writer.md) | journal | — |
| [2026-10-22-prompt-TOOL-dTrueNorth-27-3-spec-writer.md](../prompts/2026-10-22-prompt-TOOL-dTrueNorth-27-3-spec-writer.md) | journal | — |
| [2026-10-22-prompt-TOOL-dTrueNorth-27-divergence-2-brief.md](../prompts/2026-10-22-prompt-TOOL-dTrueNorth-27-divergence-2-brief.md) | research | — |
| [2026-10-22-prompt-TOOL-dTrueNorth-27-divergence-brief.md](../prompts/2026-10-22-prompt-TOOL-dTrueNorth-27-divergence-brief.md) | research | — |
| [2026-10-22-prompt-TOOL-dTrueNorth-27-spec-brief.md](../prompts/2026-10-22-prompt-TOOL-dTrueNorth-27-spec-brief.md) | research | — |
| [2026-10-22-review-TOOL-dTrueNorth-23-closing-diff-review-round2.md](../reviews/2026-10-22-review-TOOL-dTrueNorth-23-closing-diff-review-round2.md) | diff-review | TOOL-dTrueNorth-23 TOOL-dTrueNorth-24 TOOL-dTrueNorth-25 TOOL-dTrueNorth-26 TOOL-dTrueNorth-29 TOOL-dTrueNorth-30 |

<!-- /gen:spec-records -->

## 1. Goal

The plain merge bar at `f4b9849c9`, run after every unit closed, reds 9 of 68 legs
(`memory/builds/dTrueNorth/build/2026-10-22-build-TOOL-dTrueNorth-27-bar1.log`). Each red traces to
this build's own diff, unpushed above `origin/main` at `271aa59d`. This unit turns every one green
before the close: it fixes the cause in code wherever a fix exists, and raises a declared ceiling or
pin only where the build's design makes the count grow. Every line cited below was read at
`f4b9849c9`.

| Leg | What the bar measured | Cause in this build | Scope |
|---|---|---|---|
| `kickoff-manifest ratchet` | check 9: 10 watched commits since `last-body-change` | nine of the ten watched commits are this build's units, and §B never gained the build's mechanisms | S1 |
| `shell hygiene (a loop fed by a command substitution)` | `check-memory-hygiene.sh` 10 `<<<` sites, registry 8 | checks 29 and 30's printing loops (units 3, 16) | S2 |
| `shell hygiene (a fork spent on builtin work)` | six registry rows exceeded | eight sites this build added, listed in §4 | S3 |
| `spawn budget (forks per hot entrypoint)` | memory-hygiene 191 forks, ceiling 189 | checks 29 and 30 each start a generator process | S4 |
| `install-prefix (shipped surface)` | 13 kit-path spellings on 13 lines | units 4, 16, 20, 23 | S5 |
| `harness arms (fail branches armed or pinned)` | check 49 branches 23 and 24 unarmed; census 323, ceiling 319 | units 16, 20, 26 | S6 |
| `drift-audit records` | `PLAY-dClosedLoop-1` cited by product source; `cutoff_keys_armed` 36, pin 34 | units 6, 16 (the view head); units 1, 5 (two keys) | S7 |
| `remote literals (kit code names no remote)` | four lines of `deviation_join.py` | unit 4 | S8 |
| `govkit selfcheck` | one "sentence" pairs `update` with a re-render | unit 4 | S9 |

The install-prefix count is thirteen, not the twelve the brief lists: the bar also names
`tools/memory-tree/tree_lib.py:256`, written by `TOOL-dTrueNorth-23`.

## 2. Scope (IN)

- **S1** — `memory/guides/SESSION-KICKOFF.md` §B gains the four pointer bullets §4 gives verbatim: the
  carries join with the coverage region, the deviation record and its join, the audit pin, and the
  as-built view. `last-body-change` advances to the sha HEAD names when the edit is made, and
  `last-audit` re-stamps `<now> @ <that sha>` by the manifest's stamp rule
  (`memory/guides/SESSION-KICKOFF.md:23`). Both ride the commit that edits the watched files
  `tools/memory-tree/check-memory-hygiene.sh` and `.memory-tree.conf`, with a `manifest-audit:` line
  in its message, as `db2303a86` did. Observed by AC1.
- **S2** — checks 29 and 30 of `tools/memory-tree/check-memory-hygiene.sh` print their verb's lines
  without a here-string-fed loop (`:1687`, `:1714`), so the file's `<<<` count returns to its
  registry's 8 (`memory/project/substitution-fed-loops.txt:39`) and that row is unchanged. Observed
  by AC2.
- **S3** — the eight spawn-idiom sites this build added take their no-fork forms, listed in §4, so
  every row of `memory/project/spawn-idiom-sites.txt` reads its measured count again and the registry
  is unchanged. Observed by AC3.
- **S4** — on a full hygiene run, `--staged` off and no `--only`, checks 29 and 30 read their verdicts
  from check 9's generator process, `gen_build_index.py --check --with-verdicts`, instead of two
  processes of their own, so the memory-hygiene fork count returns to its ceiling of 189
  (`memory/project/fork-ceilings.txt`, row `memory-hygiene`) and the row is unchanged. Every other
  run keeps today's standalone calls. The two checks' `fail` branches, their messages and their
  printed lines are unchanged. Settled by §8 F2. Observed by AC4 and AC5.
- **S5** — the thirteen kit-path spellings take a derived form: the checker's memory-tree directory
  through an inline `resolve_kit_dir`, its suite's through the shell resolver it already carries, the
  deviation fixture's routed directory through one constant naming `src/`, the generator selftest's
  harness directory through a fixture directory named for no kit, and the `tree_lib.py` comment through
  the drained prose token `<prefix>/`. Observed by AC6, AC7 and AC8.
- **S6** — check 49 branches 23 and 24 of `tools/unattended/unattended.sh` (`:13711`, `:13734`) each
  carry a positive arm in `tools/unattended/unattended.test.sh` naming its whole signature. Branch
  23's message reads the README path from `_readme` after `readme_of "$slug" >/dev/null`, the in-file
  no-fork form (`:4659`), so no command substitution's inner quotes cut its signature. The retirement
  review in §4 finds no candidate among the build's four new code-49 sites, and
  `REFUSAL_CEILINGS`'s token for the driver rises 319 to 323 under the decision row
  `TOOL-dTrueNorth-28`, already the last line of `memory/DECISIONS.md` from the `Pass: none` records
  commit `53321feef` (§4). The pass does not edit `memory/DECISIONS.md`. Settled by §8 F4, recorded as
  deviation-29. Observed by AC9 and AC10.
- **S7** — the as-built view's head derives its `**Serves:**` id and its instrument's file name from
  `DESIGN_VIEW`'s dated record name, `<date>-build-<unit id>-as-built.md`, so no product source spells
  `PLAY-dClosedLoop-1` and the live view's head is byte for byte the instrument's. A `DESIGN_VIEW` not
  so named is a `DesignRefusal` at render, and the three fixtures that render a view at
  `memory/design/view.md` move to a dated record name. Settled by §8 F3. Observed by AC11 and AC12.
  The `cutoff_keys_armed` pin rises 34 to 36 (`tools/drift-audit/drift_signals.py:349`) with its
  `34 -> 36` reason above it, under the same decision row. Settled by §8 F5, recorded as
  deviation-30. Observed by AC13.
- **S8** — `deviation_join.py` reads the decision rows an owner approval must already hold on the
  mainline the remote ladder resolves, through `row_grammar.resolve_remote`, the kit's inline copy of
  the gov lib's ladder (`tools/memory-tree/row_grammar.py:1146`), never a remote spelled by name. The
  module constant `REF` (`tools/memory-tree/deviation_join.py:140`) retires, and its two docstrings
  (`:62`, `:719`) and its fixture's remote-tracking ref line (`:1199`) spell no remote.
  `run_plant_arms` (`deviation_join.py:1460`) holds `GOV_REMOTE` and `GOV_DEFAULT_BRANCH` out of its
  fixtures' environment, so both selftests that call it, the module's own (`run_selftest`, `:1580`)
  and the routed-commits selftest (`tools/memory-tree/routed_commits.py:670`, `:673`), run under the
  hold. The ladder reads both variables (`row_grammar.py:1175`, `:1196`), a post-merge run can export
  `GOV_REMOTE` (`tools/run-gates/post-merge.sh:86`), and the fixtures carry no remote.
  **Readers:** by name: `read_decision_rows`, `check_approver` and `render_lines` in
  `tools/memory-tree/deviation_join.py`, the three functions spelling the constant; no other module
  and no suite spells it.
  by value: `read_decision_rows`, which reads `DECISIONS.md` at the ref, and `check_approver`'s and
  `render_lines`' messages, which print it.
  Observed by AC14 and AC15.
- **S9** — the deviation fixture's commit subject at `deviation_join.py:1100` reads "rendered again"
  in place of "re-rendered", so the paragraph `govkit selfcheck` reads from `add_plant` pairs no
  re-render word with `files.update` (`:1107`). Observed by AC16.
- **S10** — deviation-28 (the unit), deviation-29 (S6) and deviation-30 (S7), written in this unit's
  spec pass, read with no malformed field. Observed by AC17.

## 3. Non-goals (OUT)

- Any red the bar did not print, and any other leg's population.
- `ARMS_FLOORS` (`.memory-tree.conf:633`): the driver's census floor stays 318. A floor stops a gate
  shrinking, and nothing here shrinks one.
- Every other row of `memory/project/fork-ceilings.txt`, `spawn-idiom-sites.txt` and
  `substitution-fed-loops.txt`.
- A waiver or pin row for any of the nine legs, and a `BASELINES` entry for `PLAY-dClosedLoop-1`,
  which `tools/drift-audit/drift_signals.py:359-370` forbids.
- Re-pointing the view's head away from the instrument; that is the report-switch step's.
- Running the unattended kit's own suites: README rule 8 waives their verdict at this landing, so the
  arms S6 lengthens are read by `check-arms.py`, which reads them statically.
- Editing the frozen specs of units 1 to 26, or any other build's spec.

### Edges

- **consumes-from** external — the code units 1 to 26 landed, all CLOSED and frozen: checks 29 and 30
  (units 3, 15, 16, 20), the audit-pin arm (units 5, 14), the deviation join and its fixture (units 4,
  12, 16, 26), the as-built view (units 6, 8, 16, 17), the dispatch edge refusals (units 16, 20, 26)
  and the checker's kit loader (unit 16); a frozen spec cannot write the mirroring hands-off line, so
  they are named here in prose

## 4. Design

### S1 — the four §B bullets, verbatim

Each is one line under the 400-byte cap check 8 reads, appended after the bullet naming the spec
leg line.

```markdown
- A chain spec binds its design clause on a `**Carries:**` or `**Derived:**` line, graded by the carries join of `tools/check-spec-tokens.py` from `SPEC_CARRIES_CUTOFF`; each chain build's README renders it as `gen:build-coverage`, and hygiene check 29 refuses an INPROGRESS spec while it is red (`TOOL-dTrueNorth-2`, `-3`).
- A departure from the frozen design, or from a spec once its code has started, is a `deviation` record that `tools/memory-tree/deviation_join.py` joins at the commit and at the close; the grammar is `memory/HYGIENE.md` "Deviation records" (`TOOL-dTrueNorth-4`).
- A `spec-audit` record pins the spec revision it read as `@rev-N` on its Serves line, and check 21's audit-pin arm refuses one that does not from `SPEC_AUDIT_PIN_CUTOFF` (`TOOL-dTrueNorth-5`).
- The as-built view at `DESIGN_VIEW` is generated by `tools/memory-tree/asbuilt_view.py`: `gen_build_index.py --write` re-renders it in the commit that changes its inputs, check 9 grades its bytes and check 30 its verdicts (`TOOL-dTrueNorth-6`, `-8`).
```

Check 9 measures watched non-merge commits since `last-body-change`
(`skills/session-kickoff/manifest-check.sh:1574-1579`), so the bundled commit counts 1 against the
threshold of 10, and check 5 reads the same commit as the stamp at or after the watched change
(`:1460-1478`).

### S2 and S3 — the sites, and the form each takes

Measured by diffing `sh_hygiene.scan_file` and `scan_spawn_file` over each file's blob before its
first dTrueNorth commit and at `f4b9849c9`. Pinned then.

| File | Line | Class | No-fork form |
|---|---|---|---|
| `tools/memory-tree/check-memory-hygiene.sh` | 1687, 1714 | `<<<` loop-var-sub | a loop over the captured string by parameter expansion (`${r%%$'\n'*}`, `${r#*$'\n'}`), no here-string |
| `tools/memory-tree/check-memory-hygiene.test.sh` | 3330, 3366, 3400 | printf-subst | the conf text as one `$'…'` string |
| `tools/memory-tree/check-memory-hygiene.test.sh` | 4191, 4201, 4251 | var-pipe | the indent as `${out//$'\n'/$'\n'      }` after one leading indent |
| `tools/unattended/unattended.sh` | 13711 | pure-fn-subst | `readme_of "$slug" >/dev/null` before the `fail`, `$_readme` in the message |
| `tools/unattended/unattended.sh` | 13742 | var-pipe | `case $'\n'"$_e_producers"$'\n' in *$'\n'"$_e_id"$'\n'*) …`, the in-file form at `:1494` |
| `tools/workflows/unattended-build.test.sh` | 1750, 1753 | printf-subst | `printf -v` into a local, then the variable |
| `tools/workflows/unattended-build.test.sh` | 1749, 1755, 1757 | var-pipe | a `${UNITS/"$pat"/$rep}` substitution, the literal held in a variable |

`unattended-build.test.sh`'s other printf-subst sites in that range are older lines a build edit
moved, not new ones; the row's net growth is the two above.

### S4 — three verdicts from one generator process

`gen_build_index.py --check --with-verdicts` runs `cmd_check_coverage(root, conf)` and
`cmd_check_asbuilt(root, conf)` in-process first, each under a captured stdout, mapping a `Problem` to
exit 2 and its `build-index: <message>` line as `main()` does (`gen_build_index.py:8663-8677`). It
prints, in order:

```
build-index: verdict 29 exit <rc>
<check 29's verb lines, as --check-coverage prints them>
build-index: verdict 30 exit <rc>
<check 30's verb lines, as --check-asbuilt prints them>
build-index: verdicts end
<--check's own lines>
```

Its exit is `--check`'s. `--with-verdicts` beside `--staged`, or with any mode but `--check`, is the
usage refusal, exit 2. One new function prints the sections, `print_check_verdicts`.

In `check-memory-hygiene.sh`, check 9's call adds `--with-verdicts` when `STAGED` is 0 and `ONLY` is
empty, and splits its capture at the three marker lines by parameter expansion: check 9's own message
and its SKIPPED scan read only the part after `build-index: verdicts end`. Checks 29 and 30 then take
`_c29`/`cov29` and `_c30`/`ab30` from their sections and run their one existing `case` each. A capture
holding no `build-index: verdicts end` line, a traceback in check 9's path, gives both checks exit 2
and the whole capture as their message, the unreadable branch they already have. Otherwise each check
calls its verb as today.

Three constraints on the shell, each a leg this unit must keep green:

- No new `fail` call: checks 9, 29 and 30 keep one `case` or `if` each, so the gate's census and
  arms do not move.
- No new `<<<` site: check 9's assignment keeps its `if ! drift=$(…)` form, because a plain
  `drift=$(…)` line marks `drift` as command-fed for the loop scanner and its existing
  `done <<<"$drift"` loop would then count.
- No new spawn-idiom site: every split is a parameter expansion.

The kit README's paragraphs on the two verbs (`tools/memory-tree/README.md:363-380`) gain the flag,
and checks 29 and 30 in `tools/memory-tree/HYGIENE.template.md` (`:577-604`) say a full run reads
their verdicts from check 9's process, printed as the standalone verbs print them.

### S5 — the thirteen spellings

| Line | Rule it trips | Derived form |
|---|---|---|
| `tools/check-spec-tokens.py:357` | 4, a quoted kit segment joined by `/` | `KIT_DIR` is `resolve_kit_dir("memory-tree", "design_lib.py", HERE)`, the canonical block inlined between its markers; a `LookupError` leaves the kit unresolved and the checker's existing refusal (`:839`, `:1321`) fires, carrying the resolver's text |
| `tools/check-spec-tokens.test.sh:1633` | 3, a kit segment followed by a file | the memory-tree directory from `resolve_kit_dir "$PY" memory-tree design_lib.py "$HERE"`, as `:189` resolves govkit |
| `tools/memory-tree/deviation_join.py:1068`, `:1148`, `:1149` | 2, gov's prefix then a loose file | one constant, `FIXTURE_ROUTED = "src/"`, read by the fixture conf (`:1004`) and every fixture product path (`:952`, `:1068`, `:1148`, `:1149`), as `routed_commits.py:422` routes its own fixture |
| `tools/memory-tree/gen_build_index.py:6122`, `:6125`, `:6131`, `:6187`, `:6206`, `:6212`, `:6283` | 1, a quoted `"tools"` segment joined | each fixture keeps its harness in one directory named for no kit, joined once from the fixture root; its stand-in resolver and the child stub at `:6283` return that directory; the comment at `:6122` names it |
| `tools/memory-tree/tree_lib.py:256` | 2 | `<prefix>/check-playbook-parity.sh:334`, the drained prose token |

The inline copy joins `tools/lib/resolve-python.test.sh`'s parity population by its marker line
(`:506-507`), so no table row is written.

### S6 — the retirement review of the four sites

The memory-tree README's rule (`tools/memory-tree/README.md:543-551`) makes a site a candidate only
when R1 to R4 all hold. R1 holds for each: every mention of the four messages in the tree is a suite
fixture or a ledger observing one, which R1 does not count (`git grep -F` over `memory/`). R2 holds
for each: the records each cites state no observed occurrence.

| Site | Built by | R3 — does its condition survive elsewhere? | R4 | Candidate |
|---|---|---|---|---|
| `:13711` malformed roster pair | `TOOL-dTrueNorth-26` S9 | `verb_plan`'s fail 42 (`:5958-5959`) and the slot contract (`gen_build_index.py:2673-2685`) refuse the same pair, but neither runs inside `--dispatch`, which reads the working tree's README (`readme_of`, `:1348`) | holds | no |
| `:13734` unreadable consumes-from line | `TOOL-dTrueNorth-20` S6 | check 12's Edges shape arm grades Tier-2 specs dated from `SPEC_EDGES_CUTOFF` only; the refusal reads every spec of the build | holds | no |
| `:13738` consumes-from cycle | `TOOL-dTrueNorth-20` S6 | no other refusal reads a consumes-from cycle | holds | no |
| `:13758` consumer before its producer | `TOOL-dTrueNorth-16` S2 | the order gate reads declared orders, never edges | holds | no |

No site retires, so no row is written to `memory/project/refusal-retirements.txt`. The token
becomes `tools/unattended/unattended.sh:323:2026-10-22:TOOL-dTrueNorth-28`, and the comment above it
(`.memory-tree.conf:640-647`) gains one line naming the raise, the review and the decision.

Branch 23's signature after the message edit is its longest literal run, `, which is malformed, so a
producer planned there with no spec yet could not block its consumer; repair the pair between`
(`check-arms.py:204-221`). The arm at `unattended.test.sh:6464` asserts the printed message through
that run. Branch 24's signature is its whole message up to `or the word external`, and the prefix
arm at `:6429` asserts all of it.

### S7 — the head's two names

`VIEW_HEAD` (`asbuilt_view.py:131-133`) carries two slots, `{serves}` and `{instrument}`, beside
`{sha}` and `{count}`. `derive_head_names(view_rel)` reads the view's file name by string slicing,
with no pattern: a name ending `-as-built.md`, opening with a date `datetime.date.fromisoformat`
accepts, then `-build-`, then a non-empty unit id. It returns the id and
`build/<date>-build-<id>-asbuilt.py`, and raises `DesignRefusal` naming `DESIGN_VIEW` otherwise. No
pattern is added, so `TOOL-dTrueNorth-20` AC21's scan of `asbuilt_view.py` meets no new
`re.compile`. For the live view the names are `PLAY-dClosedLoop-1` and
`build/2026-10-19-build-PLAY-dClosedLoop-1-asbuilt.py`, the instrument's own literal
(`memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-asbuilt.py:74-77`).

The fixtures that render a view at `memory/design/view.md`, and so meet the refusal, move to a dated
record name: `asbuilt_view.build_view_fixture` (`:349`), the generator's coverage fixture
(`gen_build_index.py:4675-4697`), and the hygiene suite's check 30 fixture
(`check-memory-hygiene.test.sh:4147-4177`). The fixtures that only read a view keep their path. The
generator arm at `gen_build_index.py:5028` asserts the head names the id and instrument its fixture's
`view_rel` carries, and the edit arm below it still shows the record's own Serves line moves no byte.
The module docstring (`asbuilt_view.py:17`, `:26`), the comment above `VIEW_HEAD` (`:127-130`) and the
kit README's row for the view (`tools/memory-tree/README.md:28`) say where the two names come from.

The pin: `"cutoff_keys_armed": 36`, with the line `34 -> 36 at dTrueNorth's close, 2026-10-22, under
decision TOOL-dTrueNorth-28: TOOL-dTrueNorth-1 arms SPEC_CARRIES_CUTOFF and TOOL-dTrueNorth-5
SPEC_AUDIT_PIN_CUTOFF in .memory-tree.conf; no key stopped being armed.` directly above it, inside
`RATCHET_LOOKBACK`'s 14 lines (`drift_signals.py:433`).

### S8 — the ref

`read_decision_ref(root)` returns `(ref, why)`: from `row_grammar.resolve_remote(root)`, the ref is
`<remote>/<branch>`, the branch `main` when the ladder names none, the bare branch when there is no
remote, as `row_grammar.py:1219-1222` reads its base; a ladder refusal returns no ref and its text.
`read_decision_rows` reads at that ref, and an unread ref leaves the rows `None`, so every owner
citation is refused, as an unread `DECISIONS.md` is today (`:761-762`). The two messages name the ref
read, or the refusal. The fixture's `main` never moves past its base (`:1081-1083`, `:1200`), so with
no remote configured the ladder's fallback reads the commit the old ref line pointed at. That holds
only while the two variables are unset, so `run_plant_arms` takes both out of `os.environ` on entry
and restores them in a `finally` around its whole body, as it already restores the strip
(`:1572-1574`) and as `run_fixture` does (`:1248-1253`). The hold lives there, not in `run_selftest`, because the routed-commits selftest calls
`run_plant_arms` directly (`routed_commits.py:670`, `:673`) and never passes through `run_selftest`.
The `GOV_REMOTE` arm of AC15 sets its own value inside that hold.
`tools/memory-tree/HYGIENE.template.md:667` says the row is held on the mainline the remote ladder
resolves, and `memory/HYGIENE.md` is re-rendered from it.

Every new or edited sentence in the memory-tree kit avoids pairing `update` with a re-render word
(S9's predicate, `govkit.py:3612-3660`), a remote's name followed by `/`, and a kit path literal.

### The decision row

Already committed: the last line of `memory/DECISIONS.md` at `53321feef`, a `Pass: none` records
commit that landed ahead of this unit's pass. It had to land first because check-arms refuses a
`REFUSAL_CEILINGS` token whose decision id no `DECISIONS.md` row carries
(`tools/memory-tree/check-arms.py:986-988`, joined by `check_id_carried`, `:651-653`), so the
pass's raise to 323 could not go green before the row existed; and the file is a shared record
(`.unattended.conf:417`) that `--dispatch` refuses a pass declaring
(`tools/unattended/unattended.sh:13833`), so the row could ride no pass. It sits below the file's last
heading (`memory/DECISIONS.md:5-6`, `:140`) in `TOOL-aSweptBar-6`'s form, and it names
`TOOL-aSweptBar-6`, the older row check 27 ranks it a near match of, so the check's "must name it"
holds (`tools/memory-tree/check-memory-hygiene.sh:2913-2914`). The pass does not edit the file:

```markdown
- **TOOL-dTrueNorth-28** - **the driver's refusal ceiling rises 319 -> 323 and the drift pin cutoff_keys_armed 34 -> 36 to their census, under TOOL-aSparedSpawn-14's rule, as TOOL-aSweptBar-6 raised it 318 -> 319**: agent, 2026-10-22, under ER:388 (PLAY-dClosedLoop-6). Detail `builds/dTrueNorth/`.
```

The retirement review and the two key names are not in the row. They live in deviation-29 (the
review of the four code-49 sites, none a candidate) and deviation-30 (`SPEC_CARRIES_CUTOFF` and
`SPEC_AUDIT_PIN_CUTOFF`), under the build folder the row's closing Detail pointer names.

### Inventory

| Identifier | Kind | Lexicon cell |
|---|---|---|
| `--with-verdicts` | flag of `gen_build_index.py --check` | none |
| `print_check_verdicts` | function, `gen_build_index.py` | `py.function` |
| `derive_head_names` | function, `asbuilt_view.py` | `py.function` |
| `read_decision_ref` | function, `deviation_join.py` | `py.function` |
| `FIXTURE_ROUTED` | constant, `deviation_join.py` | none |
| `TOOL-dTrueNorth-28` | decision id, `memory/DECISIONS.md` | none |

### Files touched (estimate)

- `memory/guides/SESSION-KICKOFF.md`
- `tools/memory-tree/check-memory-hygiene.sh`
- `tools/memory-tree/check-memory-hygiene.test.sh`
- `tools/memory-tree/gen_build_index.py`
- `tools/memory-tree/asbuilt_view.py`
- `tools/memory-tree/deviation_join.py`
- `tools/memory-tree/tree_lib.py`
- `tools/memory-tree/HYGIENE.template.md`
- `memory/HYGIENE.md` (re-rendered from the template, never edited)
- `tools/memory-tree/README.md`
- `tools/check-spec-tokens.py`
- `tools/check-spec-tokens.test.sh`
- `tools/unattended/unattended.sh`
- `tools/unattended/unattended.test.sh`
- `tools/workflows/unattended-build.test.sh`
- `tools/drift-audit/drift_signals.py`
- `.memory-tree.conf`
- `memory/DECISIONS.md` (not edited by the pass: its row landed in the `Pass: none` records commit `53321feef`)
- `memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-as-built.md` (re-rendered by `--write`, never edited)
- `memory/builds/dTrueNorth/build/2026-10-22-build-TOOL-dTrueNorth-27-deviation-28.md` (new, this spec pass)
- `memory/builds/dTrueNorth/build/2026-10-22-build-TOOL-dTrueNorth-27-deviation-29.md` (new, this spec pass)
- `memory/builds/dTrueNorth/build/2026-10-22-build-TOOL-dTrueNorth-27-deviation-30.md` (new, this spec pass)

### Alternatives rejected

- **S4: route the two python calls through a redirect to a file.** The counter reads traced BASHPIDs,
  so a direct child would vanish from the count while the fork stays: the counter's blind spot, not a
  saving (`tools/gate-lint/fork-count.sh:42-44`).
- **S5: compose the fixture's `tools/` prefix from a variable.** It spells nothing the gate reads and
  keeps a gov-prefix lookalike in fixture data; `src/` names no prefix at all.
- **S8: a second inline copy of the ladder in `deviation_join.py`.** The module already imports
  `row_grammar`, whose copy is the kit's one; a second copy in one kit is the copy `[reuse]` forbids.
- **S7: a pattern over the view's name in `asbuilt_view.py`.** It is a `re.compile` with a literal
  leaf, which unit 20's AC21 scan flags in that file.

## 5. Production-readiness checklist

- security — S8 keeps the approval rule's property: rows are read on the ladder's mainline, never the
  run's branch, and a ladder refusal leaves every owner citation refused. S5's resolver reads the
  install receipt the parity-gated way.
- perf / scale — S4 spares a full hygiene run two interpreter starts and two module imports; the
  verdicts' own reads are unchanged.
- error / empty / loading states — a misnamed view, a missing verdict section and a ladder refusal are
  each a named refusal or an unreadable branch; none reads as green.
- observability — checks 29 and 30 print the same lines either path; the ceiling prints its date and
  decision on every run.
- risks — S4 couples three verdicts to one process, so a traceback in check 9's path also fails
  checks 29 and 30, the conservative direction. S7 refuses a misnamed `DESIGN_VIEW` that rendered
  before.
- testing — AC1 to AC17 as probes and fixtures; the arms under §7.
- migration — additive: the flag is opt-in, the `DESIGN_*` keys are gov's and blank at every adopter,
  and the live head's bytes do not move.
- user docs — the kit README and `memory/HYGIENE.md`; no page under `help/` covers these engines.

## 6. Acceptance criteria

Every command runs from the repository root under bash 5.3. A scratch repository sits under a short
`%TEMP%` path with no hook installed.

- **AC1** — When `bash skills/session-kickoff/manifest-check.sh` runs at the unit's tip, it exits 0
  and prints no `check 9` line; `grep -c 'TOOL-dTrueNorth-' memory/guides/SESSION-KICKOFF.md` prints 4;
  and `bash tools/gate-lint/fork-count.sh memory/project/fork-ceilings.txt . --only manifest-check`
  prints `ok manifest-check`.
  Red when: `last-body-change` stays at `f8bbdc85`, or a bullet passes 400 bytes.
- **AC2** — When `python tools/gate-lint/sh_hygiene.py memory/project/substitution-fed-loops.txt` runs,
  it names no site in `tools/memory-tree/check-memory-hygiene.sh`, and
  `git diff --stat origin/main -- memory/project/substitution-fed-loops.txt` prints nothing.
  Red when: either check's printing loop is fed by `<<<`.
- **AC3** — When `python tools/gate-lint/sh_hygiene.py --spawn-idioms memory/project/spawn-idiom-sites.txt . ':!*.test.sh' ':!memory/'`
  runs, it prints none of the six registry findings the bar printed, and
  `git diff --stat origin/main -- memory/project/spawn-idiom-sites.txt` prints nothing.
  Red when: any site in §4's table keeps its forking form.
- **AC4** — When `bash tools/gate-lint/fork-count.sh memory/project/fork-ceilings.txt . --only memory-hygiene`
  runs, it prints `ok memory-hygiene` with a measured count of at most 189, and
  `memory/project/fork-ceilings.txt` is unchanged in the unit's diff.
  Red when: checks 29 and 30 start their own generator processes on a full run.
  cost: about a minute.
  figure: 191 at `f4b9849c9`, DERIVED by the same command.
- **AC5** — When `bash tools/memory-tree/check-memory-hygiene.sh` runs over the tree, its
  `memory-hygiene: check 29:` and `memory-hygiene: check 30:` lines equal those
  `bash tools/memory-tree/check-memory-hygiene.sh --only 29` and `--only 30` print; and
  `python tools/memory-tree/gen_build_index.py --check --with-verdicts` prints
  `build-index: verdict 29 exit 0`, `build-index: verdict 30 exit 0` and `build-index: verdicts end`
  above `--check`'s own lines, its exit `--check`'s.
  Red when: the full run's verdict lines differ from the standalone verbs'.
- **AC6** — When `bash tools/check-install-prefix.sh` runs, it exits 0, and
  `bash tools/check-install-prefix.sh --list` names no line of `tools/check-spec-tokens.py`,
  the checker's own test file, `tools/memory-tree/deviation_join.py`,
  `tools/memory-tree/gen_build_index.py` or `tools/memory-tree/tree_lib.py`.
  Red when: any of the thirteen spellings stands.
- **AC7** — When a probe copies `tools/check-spec-tokens.py` alone into a scratch repository's
  `tools/` and runs it, it exits non-zero printing `REFUSING` and the resolver's three places; in the
  tree, `python tools/check-spec-tokens.py --legs-for tools/memory-tree/design_lib.py` runs as before;
  and the block between `# >>> resolve_kit_dir` and `# <<< resolve_kit_dir` in the checker equals
  `tools/lib/resolve_kit_dir.py`'s, compared with `diff`.
  Red when: the checker loads a kit it guessed, or its copy drifts from the canonical.
- **AC8** — When `python tools/memory-tree/deviation_join.py --selftest` and
  `python tools/memory-tree/gen_build_index.py --selftest` run, each exits 0, the first with its
  fixture routing `src/` and the second with its `TOOL-dTrueNorth-14`, `-19` and `-20` harness arms
  ok.
  Red when: a fixture's routed path or harness directory no longer matches what its reader resolves.
  cost: minutes.
- **AC9** — When `python tools/memory-tree/check-arms.py --check` runs, it prints no
  `HYGIENE check-arms:` line naming `tools/unattended/unattended.sh`; and
  `python tools/memory-tree/check-arms.py --report` prints no `STRANDED` token on the rows of check 49
  branches 23 and 24.
  Red when: an arm asserts a prefix short of its branch's signature.
- **AC10** — When `python tools/memory-tree/check-arms.py --check` runs, it prints
  `check-arms: ceiling tools/unattended/unattended.sh 323/323 · 2026-10-22 · TOOL-dTrueNorth-28`, and
  `grep -c 'TOOL-dTrueNorth-28' memory/DECISIONS.md` prints 1.
  Red when: the census passes 323, or the decision id is absent from the log.
  figure: the census 323 at `f4b9849c9`, DERIVED by the same command.
- **AC11** — When `git grep -c 'PLAY-dClosedLoop-1' -- tools/memory-tree/asbuilt_view.py tools/memory-tree/gen_build_index.py`
  runs, it prints nothing; and `python tools/drift-audit/drift_report.py --check` prints no
  `new   PLAY-dClosedLoop-1` line.
  Red when: product source spells the id again.
- **AC12** — When the view is re-rendered and
  `python memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-asbuilt.py --check` and
  `python tools/memory-tree/gen_build_index.py --check` run, both exit 0; and a probe calling
  `asbuilt_view.derive_head_names` with the argument `"memory/design/view.md"` raises `DesignRefusal` naming
  `DESIGN_VIEW`.
  Red when: the derived head differs by a byte from the instrument's, or a misnamed view renders.
- **AC13** — When `python tools/drift-audit/drift_report.py --check` runs, `cutoff_keys_armed` reads
  36 against pin 36, and `grep -n -B2 '"cutoff_keys_armed": 36' tools/drift-audit/drift_signals.py`
  shows the `34 -> 36` line naming `SPEC_CARRIES_CUTOFF`, `SPEC_AUDIT_PIN_CUTOFF` and
  `TOOL-dTrueNorth-28`.
  Red when: the raise carries no `<old> -> <new>` reason within `RATCHET_LOOKBACK` lines.
- **AC14** — When `bash tools/check-remote-literals.sh` runs, it exits 0 and names no line of
  `tools/memory-tree/deviation_join.py`.
  Red when: any of the four lines spells the remote.
- **AC15** — When `python tools/memory-tree/deviation_join.py --approval author-recorded` runs in the
  tree, no line says `DECISIONS.md is unread`; and when a probe exports `GOV_REMOTE` naming no remote
  of a scratch clone and calls `deviation_join.read_decision_ref` there, it returns no ref and the
  ladder's refusal text.
  Red when: the rows are read on a ref the ladder did not resolve.
- **AC16** — When `python tools/govkit/govkit.py selfcheck` runs, it exits 0 and prints no line
  naming `tools/memory-tree/deviation_join.py`.
  Red when: a paragraph of the kit pairs `update` with a re-render word.
- **AC17** — When `python tools/memory-tree/deviation_join.py --approval author-recorded` runs after
  the records are committed, no `malformed:` or `refused:` line names
  `2026-10-22-build-TOOL-dTrueNorth-27-deviation-28`, `-29` or `-30`, and the rescope add member for
  `TOOL-dTrueNorth-27` joins deviation-28. Under `--approval by-risk`, deviation-29 and -30, each a
  loosening approved by the author, are listed on `refused:` lines beside deviation-20, -21 and -26,
  and deviation-28 is not.
  Red when: a record falls outside the grammar, or the add member is recorded by nobody.

## 7. Gates

`kickoff-manifest ratchet` · `shell hygiene (a loop fed by a command substitution)` · `shell hygiene (a fork spent on builtin work)` · `spawn budget (forks per hot entrypoint)` · `install-prefix (shipped surface)` · `harness arms (fail branches armed or pinned)` · `drift-audit records` · `remote literals (kit code names no remote)` · `govkit selfcheck` · `build-index selftest` · `drift-audit selftest` · `kit/dogfood doc parity` · `memory-hygiene self-test` · `recall floor` · `recall floor arms` · `review-join self-test` · `straggler-guard arms` · `tier2-review self-test` · `transition-audit arms` · `unattended-build self-test` · `verifier fan-out self-test` · `memory hygiene` · `routed-commits selftest` · `spec-tokens self-test` · `spec tokens (a spec's own names resolve)` · `unattended kit gate` · `verdict epoch (kit version dates the engine)` · `python resolver (behaviour + inline parity + idiom ban)` · `check-arms selftest` · `install-prefix self-test` · `remote literals self-test` · `lexicon naming predicates` · `dead-path carriers (deleted files still named)`

New arm: tools/memory-tree/check-memory-hygiene.test.sh · covers AC5 · a full run over the check 29 and 30 fixture with an INPROGRESS spec on red coverage and a planted view finding, beside its `--only` runs · none
New arm: tools/memory-tree/gen_build_index.py (its selftest) · covers AC5 AC12 · `--check --with-verdicts` over a fixture with a planted verdict, and a view named outside the record grammar · none
New arm: tools/memory-tree/asbuilt_view.py (its selftest) · covers AC12 · the fixture view at a dated record name, its head's two names asserted · none
New arm: tools/memory-tree/deviation_join.py (its selftest, run by the routed-commits selftest) · covers AC15 · a `GOV_REMOTE` naming no remote of the fixture, set inside `run_plant_arms`' hold that keeps an exported `GOV_REMOTE` or `GOV_DEFAULT_BRANCH` out of every other arm's fixture under both selftests that call it · none
New arm: tools/unattended/unattended.test.sh · covers AC9 · the two arms lengthened to their signatures · none

The nine red legs are graded by the merged bar at the close; each AC above runs its leg's own command
as a probe. README rule 8 waives the unattended suites' verdict at this landing, so AC9 reads the
lengthened arms through `check-arms.py`, which reads them without running them.
`KIT_MEMORY_TREE_VERSION` is minted by the lander for the kit files this unit moves.

## 8. Open questions

- **F1 — Which binding line does a unit the bar promoted carry?** The carries join of
  `TOOL-dTrueNorth-2` reds a chain spec carrying nothing and derived from nothing. (a) `**Derived:**`
  naming `PLAY-dClosedLoop-2`, the owner's ruling that a run carries the units it adds (ER:320).
  (b) None, which reds `unbound`. Recommendation (a). Rung 3. RESOLVED (agent, 2026-10-22,
  delegated): (a). widens: none · relaxes: none
- **F2 — How does the memory-hygiene fork budget clear?** Checks 29 and 30 each spend one counted
  fork, their generator process, and nothing else this build added runs in the fork-count fixture:
  check 21's new captures sit behind its records precondition (`check-memory-hygiene.sh:1338`), and
  the fixture holds no record. (a) Both verdicts ride check 9's generator process on a full run. (b)
  One shared process for the two, and the ceiling 189 to 190. (c) Convert two of the prelude's older
  population counters (`:524-533`). (d) The ceiling 189 to 191. (b) and (d) fail the non-goal "a
  raise where a code fix exists" (veto 1); (c) leaves the cause standing and changes a part of the
  hygiene gate no dTrueNorth clause names. (a) changes the delegation of check 29, the coverage
  check of `cl-dClosedLoop-0003`, and of check 30, the gate of `cl-dClosedLoop-0006`, through the
  verb that renders both clauses' region and view, which the grant covers. Recommendation (a). Rung
  3. RESOLVED (agent, 2026-10-22, delegated): (a). grants: PLAY-dClosedLoop-3 checks 29 and 30 read
  their verdicts from check 9's generator process on a full run, for cl-dClosedLoop-0003 and
  cl-dClosedLoop-0006 · widens: none · relaxes: none
- **F3 — How does product source stop citing `PLAY-dClosedLoop-1`?** The view's head must equal the
  instrument's, which spells the id, so the question is where the product reads it from. (a) Derive
  the id and the instrument's name from `DESIGN_VIEW`'s dated record name, refusing any other name.
  (b) The same, with a fallback head for an undated name, which fabricates names the view does not
  carry. (c) A conf key holding the two names, a second copy of the instrument's literal. (d) List
  the id in `BASELINES`, which the signal's own rule forbids. Parity does not force the citation:
  (a) renders the live head byte for byte. The view is `cl-dClosedLoop-0006`'s, so the grant covers
  it. Recommendation (a). Rung 3. RESOLVED (agent, 2026-10-22, delegated): (a). grants:
  PLAY-dClosedLoop-3 the view's head derived from DESIGN_VIEW's record name, for cl-dClosedLoop-0006
  · widens: none · relaxes: none
- **F4 — Does the driver's refusal ceiling rise, and does any of the four sites retire?** The review
  in §4 finds no candidate. (a) Keep all four and raise 319 to 323 under `TOOL-dTrueNorth-28`. (b)
  Retire site 23 on the commit-boundary refusals, and raise to 322; R3 fails at the dispatch moment,
  and it reverses `TOOL-dTrueNorth-26` S9, a CLOSED unit's scope (veto 1). (c) Consolidate sites 24
  and 25 into one shape refusal, rewriting two armed messages, still a raise. (d) No change, failing
  AC10 (veto 1). The ceiling guards the dispatch refusals, a governance carrier no dTrueNorth clause
  names, so veto 2 holds outside the grant and rung 5 takes the most capable option: (a) meets AC9
  and AC10 and keeps every refusal. RESOLVED (agent, 2026-10-22, delegated): (a), citing ER:388
  (`PLAY-dClosedLoop-6`), recorded as deviation-29. widens: REFUSAL_CEILINGS · relaxes: none
- **F5 — Does the `cutoff_keys_armed` pin rise?** (a) 34 to 36, the two keys the design puts its
  binding lines and audit pins behind. (b) Disarm two other keys, which turns off rules landed specs
  are graded by. (c) No change, failing AC13 (veto 1). The pin is the drift-audit kit's, a carrier no
  dTrueNorth clause names, so rung 5 takes (a). RESOLVED (agent, 2026-10-22, delegated): (a), citing
  ER:388 (`PLAY-dClosedLoop-6`), recorded as deviation-30. widens: cutoff_keys_armed · relaxes: none
- **F6 — Does the grant or the ruling cover every other carrier edit here?** S2 and S4 change checks
  29 and 30, `cl-dClosedLoop-0003`'s and `cl-dClosedLoop-0006`'s; S7's head is
  `cl-dClosedLoop-0006`'s view; S8 and S9 are `cl-dClosedLoop-0004`'s join and its fixture. S3, S5 and
  S6's message edit change no output for any input, and S1 is a record. RESOLVED (agent, 2026-10-22,
  delegated): lifted by `PLAY-dClosedLoop-3`, rung 3, for S2, S4 and S7 to S9; S3, S5 and S6's edit
  change no carrier's behaviour. grants: PLAY-dClosedLoop-3 the memory-tree kit edits S2, S4 and S7
  to S9 make for cl-dClosedLoop-0003, cl-dClosedLoop-0004 and cl-dClosedLoop-0006 · widens: none ·
  relaxes: none

## 9. Revision log

- rev-1 · 2026-10-22 · initial draft, one scope item per red leg of the plain bar at `f4b9849c9`, with deviation records 28 to 30.
- rev-2 · 2026-10-22 · the builder's DIVERGENCE: §4's verbatim `TOOL-dTrueNorth-28` row failed check 27, a near match of `TOOL-aSweptBar-6` it did not name, so the row names it; the row appends at the file's end, not a TOOL section, in its own `Pass: none` records commit, since `--dispatch` refuses the shared record (§4, S6); S8 and §7's deviation arm state the selftest's hold on `GOV_REMOTE` and `GOV_DEFAULT_BRANCH`.
- rev-3 · 2026-10-22 · §4's row disagreed with the one `53321feef` committed, whose text check 7's 300-character cap had cut: §4 now quotes the committed row, says it landed ahead of the pass because check-arms refuses a ceiling token no row carries, and puts the review and the key names in deviations 29 and 30; S6 and Files touched say the pass does not edit `memory/DECISIONS.md`; S8 put the hold in `run_selftest`, which the routed-commits selftest bypasses, so S8 and §7 now name `run_plant_arms`.

## 10. Reuse audit

Every item extends a seam the tree already has, read at `f4b9849c9`. S2 and S3 reuse the no-fork
forms the files already use, `readme_of`'s `_readme` (`tools/unattended/unattended.sh:1348`, `:4659`)
and the `case` membership test (`:1494`), and follow `TOOL-aSweptBar-5` and `TOOL-dRedressedBar-5`,
which converted regrown spawn idioms the same way. S4 extends the generator's own verb dispatch
(`tools/memory-tree/gen_build_index.py:8663-8677`) and check 9's existing call. S5 reuses the
canonical `tools/lib/resolve_kit_dir.py`, inlined as `tools/drift-audit/drift_report.py:55-92`
carries it, the suite's shell resolver at `tools/check-spec-tokens.test.sh:189`, and
`routed_commits.py:422`'s `src/` fixture route. S8 reuses `row_grammar.resolve_remote`
(`tools/memory-tree/row_grammar.py:1146`) and its caller's fallback (`:1219-1222`). S7 found no seam:
`python tools/codebase-map/reuse_lookup.py "derive a record id and date from a dated record file
name"` ranked `records`, `read_records` and `derive_clause_hash` by name stem, none of them a file-name
reader, and the one record-name pattern in the kit (`gen_build_index.py:706`) is the deviation name's
alone, so `derive_head_names` reads the name by slicing. `python tools/codebase-map/reuse_lookup.py
"run several verdict verbs of the build index generator in one process and split their output by
section"` ranked `run` and `run_arms` by name stem and no multi-verb host, which S4's flag is.

Recall terms used: `python tools/memory-recall/query.py "clear the merge bar's red legs a build caused
before its close: spawn idioms, fork budget, install prefix, arms, drift pins" --terms "fork ceiling
spawn idiom registry here-string loop install-prefix kit path remote ladder refusal ceiling retirement
review cutoff pin as-built head"`
