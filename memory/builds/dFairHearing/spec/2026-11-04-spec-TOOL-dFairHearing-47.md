# TOOL-dFairHearing-47 — the last of the bar's own reds: two loops fed from a file, one exempt row, one guard, one cite, and the manifest's stamps

**Status:** CLOSED · rev-1 · 2026-11-04 · node d · Tier-1 · base 22621f55 · streams tooling · order 31

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-03-build-TOOL-dFairHearing-1-agent-ledger.md](../build/2026-11-03-build-TOOL-dFairHearing-1-agent-ledger.md) | journal | TOOL-dFairHearing-1 TOOL-dFairHearing-2 TOOL-dFairHearing-3 TOOL-dFairHearing-4 TOOL-dFairHearing-5 TOOL-dFairHearing-6 TOOL-dFairHearing-7 TOOL-dFairHearing-8 TOOL-dFairHearing-9 TOOL-dFairHearing-10 TOOL-dFairHearing-11 TOOL-dFairHearing-12 TOOL-dFairHearing-13 TOOL-dFairHearing-14 TOOL-dFairHearing-15 TOOL-dFairHearing-16 TOOL-dFairHearing-17 TOOL-dFairHearing-18 TOOL-dFairHearing-20 TOOL-dFairHearing-21 TOOL-dFairHearing-22 TOOL-dFairHearing-23 TOOL-dFairHearing-25 TOOL-dFairHearing-26 TOOL-dFairHearing-27 TOOL-dFairHearing-28 TOOL-dFairHearing-29 TOOL-dFairHearing-30 TOOL-dFairHearing-31 TOOL-dFairHearing-32 TOOL-dFairHearing-33 TOOL-dFairHearing-34 TOOL-dFairHearing-35 TOOL-dFairHearing-36 TOOL-dFairHearing-37 TOOL-dFairHearing-38 TOOL-dFairHearing-39 TOOL-dFairHearing-40 TOOL-dFairHearing-43 TOOL-dFairHearing-44 TOOL-dFairHearing-45 TOOL-dFairHearing-46 |
| [2026-11-04-build-TOOL-dFairHearing-47-1-acceptance-ledger.md](../build/2026-11-04-build-TOOL-dFairHearing-47-1-acceptance-ledger.md) | journal | — |
| [2026-11-04-build-TOOL-dFairHearing-47-deviation-471.md](../build/2026-11-04-build-TOOL-dFairHearing-47-deviation-471.md) | deviation | — |
| [2026-11-04-prompt-TOOL-dFairHearing-47-1-spec-writer.md](../prompts/2026-11-04-prompt-TOOL-dFairHearing-47-1-spec-writer.md) | journal | — |
| [2026-11-04-prompt-TOOL-dFairHearing-47-build-brief.md](../prompts/2026-11-04-prompt-TOOL-dFairHearing-47-build-brief.md) | research | — |
| [2026-11-04-prompt-TOOL-dFairHearing-47-spec-brief.md](../prompts/2026-11-04-prompt-TOOL-dFairHearing-47-spec-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

The close re-ran the bar's lint legs after unit 45 and found three reds this build owns: two
here-string loops, a guard entry govkit will not classify, and the kickoff manifest's stalled body
stamp. Unit 45's builder named two more items and left them: a leg guard short of a kit its new arm
resolves, and a registry reason citing a line that moved. This unit repairs all five, and it is the
build's last.

## 2. Scope (IN)

Line numbers are read at `22621f55a`.

- **S1** — The shell hygiene leg for loops. The loops at `tools/check-hook-destinations.sh:325` and
  `tools/workflows/unattended-build.test.sh:564` each read a scratch file, and the pipeline that fed
  each one writes that file. `memory/project/substitution-fed-loops.txt` gains no row. Observed by AC1.
- **S2** — The govkit selfcheck leg. `tools/govkit/registry.toml` gains an `[[exempt]]` row for
  `.governance/install.json`, and the `policy fixtures` guard keeps naming that file. Observed by AC2.
- **S3** — The `hook destinations self-test` guard in `tools/gate-legs.json` gains the three
  workflows-kit files its suite reads. Observed by AC3.
- **S4** — The reason at `memory/project/unarmed-branches.txt:40` cites the suite line that drives
  the refusal, which is 271. Observed by AC4.
- **S5** — The kickoff manifest. This unit's commit advances `last-audit` and `last-body-change` in
  `memory/guides/SESSION-KICKOFF.md`, and its message carries the `manifest-audit: delta` line.
  Observed by AC5.

## 3. Non-goals (OUT)

- No gate and no arm. Each leg already reds its own item, and the suite edit in S1 keeps every
  assertion the suite makes.
- No edit to `tools/govkit/govkit.py`. The partition already has the class this file needs.
- No other reason in `memory/project/unarmed-branches.txt`. Rows 50, 175 and 176 also cite lines that
  hold no arm at `22621f55a`, but no leg grades a reason's text, so none is a red. They are named here
  as a follow-up.
- No sentence of the manifest's body moves. The re-read found none stale, as S5's design says.
- Not the close's final manifest re-stamp, which the main loop does last.
- No help page. None of the five items changes anything a user reads or runs.

## 4. Design

### Tier

Tier-1. Each item is mechanical. The scratch files of S1 live for one run, and no item adds a write
path, a migration or a shared contract. The brief adopts the five as one unit because they are the
reds of one lint read, as unit 45's were.

### The loops (S1)

Both sites grade as `loop-var-sub`, not as a substitution in the here-string itself. `<<<` holds a
plain expansion, and `tools/gate-lint/sh_hygiene.py:335-340` follows it one assignment back, to
`tools/check-hook-destinations.sh:275` and `tools/workflows/unattended-build.test.sh:553`. The leg's
message asks for a scratch file (`tools/gate-lint/sh_hygiene.py:481`).

The module's docstring puts the stall at the assignment and not at the loop, so copying the variable
into a file would clear the grade and keep the hazard. The pipeline writes the file directly.

`tools/check-hook-destinations.sh` has no scratch file and no trap today. Where `DIR_KITS` was
assigned, after `DIR_HOMES`:

```bash
KITS_FILE=$(mktemp) || { echo "hook-dest: could not make a scratch file — refusing"; exit 2; }
trap 'rm -f "$KITS_FILE"' EXIT
printf '%s\n' "$FLAT" | tail -n +2 | sed -n 's/^K //p' >"$KITS_FILE"
```

The loop's last line becomes `done <"$KITS_FILE"`. The form is `tools/check-line-length.sh:294`'s,
with the refusal shape of this file's own :244. An `exit 2` is outside the refusal sites
`tools/memory-tree/check-arms.py` reads, which are `exit 1` and `status=1` (:74-75), so no pin row is
owed. `printf` into `tail` is not a `var-pipe` shape, so `memory/project/spawn-idiom-sites.txt` keeps
its counts.

In `tools/workflows/unattended-build.test.sh`, `pin_rows` is read twice, so both reads move to the
file. `LAY` and the suite's one trap are made at :2156-2157, well below this arm, so the arm owns its
scratch file and removes it itself. Nothing between the two lines exits.

```bash
pin_file=$(mktemp) || exit 2
"$_rkd_py" -B "$HERE/review_pin.py" --subject memory/builds/tB/build/d.md --design-record-preset whole-design \
    --twin always --unclassed reason --opt-in '{"whole-design": {"topology": "blast-radius"}}' | "$_rkd_py" -c '
import json, sys
for line in sys.stdin:
    for k, v in json.loads(line).items():
        print(k + "\t" + json.dumps(v, separators=(",", ":")))' | tr -d '\r' | sort -u >"$pin_file"
has "FH43 AC3 the pin prints a walk, so the population below is real" "$(<"$pin_file")" 'walk'
```

The loop's body stays as it is, its last line becomes `done <"$pin_file"`, and `rm -f "$pin_file"`
follows it. `$(<"$pin_file")` is bash's no-fork read, and the `redirected-read` ban does not reach it
because nothing else is redirected inside it.

### The exempt row (S2)

The partition at `tools/govkit/govkit.py:2297-2336` gives each guard entry exactly one of six
classes.
`.governance/install.json` matches no prefix class, no descriptor declares it as a root conf, and no
exempt row names it, so it lands in none.

The class this file belongs to is `exempt`. `TOOL-dGroundRules-79` settled the same case for the same
leg: `AGENTS.md` and `help/policy.md` are also gov-only files the `policy fixtures` guard names, and
each holds an `[[exempt]]` row for that reason (`tools/govkit/registry.toml:335-341`). The partition
matches an exact path through `g == p.rstrip("/")` (:2327), and `exempt` keeps `kit-relative` out
(:2329).

After the `help/policy.md` row:

```toml
[[exempt]]
path = ".governance/install.json"
why = "gov's own source-mode deploy receipt, deliberately not shipped: the deployer writes each target its own. It lies outside the declared surface, so this row narrows nothing there. It is the class selfcheck's guard taxonomy gives the `policy fixtures` guard line naming it, a gov-only leg (its `[[exempt_leg]]` row) whose fixture reads the file. TOOL-dFairHearing-47."
```

The row's other readers were read at `22621f55a`, and none moves. Selfcheck requires a non-empty
reason and a path that exists (`tools/govkit/govkit.py:3430-3440`), and the file is tracked.
`tools/check-playbook-parity.sh:307` reads only a row opening with the prefix token.
`run_ships_join` (`tools/policy/check_policy.py:3816`) joins a row only to a census enforcer, and this
path is none.

### The guard (S3)

Unit 45's arm resolves `spec-audit-optin.js` through `resolve_kit_dir`
(`tools/check-hook-destinations.test.sh:361`) and plants a fragment naming that file. The gate then
reads the workflows kit's `kit.toml` for what it ships. The suite's first arm (:280) runs the gate
over every tracked fragment, `spec-audit-optin.fragment.json` among them.

`memory/gotchas/held-suite-guard-misses-a-sibling-kit.md` prefers exact files to a sibling's
directory. The workflows directory is a guard on four legs today, and a fifth would sit it at `BROAD_LEG_FLOOR`,
one leg from leaving the spec-tokens join. So the guard names the three files:

```json
    "guard": [
      "{prefix}/check-hook-destinations.sh",
      "{prefix}/hooks/",
      "{prefix}/memory-recall/",
      "{prefix}/workflows/kit.toml",
      "{prefix}/workflows/spec-audit-optin.fragment.json",
      "{prefix}/workflows/spec-audit-optin.js"
    ],
```

Each is `kit-relative` in the partition. The manifest is this guard's one home: the leg holds an
`[[exempt_leg]]` row (`tools/govkit/registry.toml:351-353`), so no descriptor carries a copy.

### The cite (S4)

`tools/memory-tree/check-arms.py` does not grade the reason's text. A refusal row's key is gate, kind,
occurrence and signature (:835). The reason is refused only when empty or the placeholder (:843), and
is otherwise printed on the row's `waived` line (:858). The module says so at :113: a reason is prose
and nothing checks that it is true. So this repair keeps a record honest and clears no leg.

The brief's 249 does not hold. `tools/check-install-prefix.test.sh:249` is a comment, and the
`run_arm` that drives the refusal is at :271. It stood at :236 when the row was written and at :258 at
BASE `8bec4cefd`, so the cite was already stale when unit 45 moved it 13 lines. The row takes 271,
PINNED at `22621f55a`. That suite is outside this write set, so nothing here moves it.

The edit changes those three digits and nothing else, because `tools/memory-tree/check-arms.py:601`
raises on a refusal row that is not five tab-separated fields.

### The manifest (S5)

`tools/gate-legs.json` is a watched path, so the commit must bundle the `last-audit` re-stamp, or the
pre-commit leg refuses it (`skills/session-kickoff/manifest-check.sh:1775-1791`). The ratchet's stall
check refuses at ten watched non-merge commits since `last-body-change` (:1767-1768). The count is 11,
PINNED at `22621f55a`, since `201eb127c`.

Both stamps take the same sha, `git rev-parse HEAD` read just before the commit, and `last-audit`
takes a datetime later than the one it holds. That is the precedent of `1f7d19660`, whose parent is
the `201eb127c` it stamped: a commit cannot name itself.

The Orientation section was re-read at `22621f55a` against the build's diff from `8bec4cefd`, and no
sentence needs a correction:

- Every tracked path the section cites resolves.
- Of the watched files, only `tools/gate-legs.json` and the charter template moved in this build. The
  section spells no guard entry, and the charter's lookup line it never cited is the one that went.
- The one sentence the build falsified, the `--for-diff` comment under Gate commands, unit 23
  corrected.
- `tools/workflows/spec-audit-optin.js` now refuses at the tool call a spec audit a build did not
  declare. The section's spec-audit bullet says one is owed only where it is declared, which stays
  true.
- Agent-cap's review rules moved to the review kit, and the section names neither.

So only the two stamp lines change. The ratchet's refusal asks for exactly this, a re-read and an
advance, and `1f7d19660`'s delta line records the same no-stale result.

The delta line follows `skills/session-kickoff/SKILL.md:121`, with its count taken before the
re-stamp (:122). That count is `git rev-list --count` from the old `last-audit` sha over the watch list, 1 at
`22621f55a`:

```text
manifest-audit: delta tools/gate-legs.json adds three workflows-kit files to the `hook destinations self-test` leg's guard; the Orientation section re-read against this build, no claim found stale; last-audit and last-body-change advanced to <sha8> · watch-commits-since-stamp: <n>
```

### The probe

Save this block to `$TEMP/fh47probe` and run it from the repository root. It counts what the stall
check counts: the watched non-merge commits since `last-body-change`, over the manifest's own list.

```bash
stamp=$(sed -n 's/^last-body-change: //p' memory/guides/SESSION-KICKOFF.md)
watch=$(sed -n 's/^watch: //p' memory/guides/SESSION-KICKOFF.md | tr ';' ' ')
git rev-list --count --no-merges "$stamp..HEAD" -- $watch
```

### Generated files

This write set pairs no generated file with its generator. It declares three renders, and it declares
neither `tools/memory-tree/gen_build_index.py` nor `tools/memory-tree/backlog.py`.
`memory/map/generated/inventories.json` holds leg names and no guards, no function is added, and
nothing under `tools/codebase-map/` reads `tools/govkit/registry.toml`, so no map file moves. No kit version
moves on the branch, because the lander mints it (`tools/govkit/govkit.py:13845-13846`).

### Rollout

The new exempt row cites this unit's id, which the drift signal counts as product-source evidence
until the header reads CLOSED. The bar runs after that flip, as it does for every unit of this build.

### The header's ask clause

The header carries neither `closes` nor `advances`, for the reason unit 43's Design section gives
under this same heading.

### Files touched (estimate)

- `tools/check-hook-destinations.sh`
- `tools/workflows/unattended-build.test.sh`
- `tools/govkit/registry.toml`
- `tools/gate-legs.json`
- `memory/project/unarmed-branches.txt`
- `memory/guides/SESSION-KICKOFF.md`
- `memory/builds/dFairHearing/build/2026-11-04-build-TOOL-dFairHearing-47-1-acceptance-ledger.md`
- `memory/builds/dFairHearing/spec/2026-11-04-spec-TOOL-dFairHearing-47.md`
- `memory/builds/dFairHearing/README.md`
- `memory/LIVE.md`
- `memory/backlog/TOOL.md`

The last three are the renders the status flip forces, as unit 44 declares them. The departure record
`2026-11-04-build-TOOL-dFairHearing-47-deviation-471` is written beside this spec and is not the
builder's.

### Alternatives rejected

- **A registry row for either loop.** The brief refuses it, and the registry is shrink-only.
- **`printf '%s\n' "$var" >file` beside the existing assignment.** It clears the grade and leaves the
  fork and the wait where the leg's docstring says they are.
- **`done < <(cmd)`.** The leg counts that form and does not grade it, and it has the same dependency.
- **Drop `.governance/install.json` from the guard.** The fixture reads the file, so the leg's
  `guard-trace` case reds again.
- **Add `.governance/` to the partition's `verbatim` tuple.** That class holds the trees a kit deploys
  at a fixed root path, and no kit deploys this receipt: `write_install_receipt` writes it per target.
  It also edits `tools/govkit/govkit.py` for what a declared row already answers.
- **A seventh class.** One file does not earn a class, its selftest arm and its emitter rule.
- **The workflows directory as one guard entry.** It matches its neighbours, but it costs the shared
  guard its margin under `BROAD_LEG_FLOOR` and runs this suite on every edit to that kit.
- **Correct the row to 249, as the brief reads.** That line is a comment, so the record would still
  be false.

## 5. Acceptance criteria

- **AC1** — When `grep -c -e 'done <<<' -e 'DIR_KITS=' tools/check-hook-destinations.sh` runs, it
  prints 0, and `grep -c -e 'done <<<' -e 'pin_rows=' tools/workflows/unattended-build.test.sh` prints
  0. When
  `grep -c 'done <"\$KITS_FILE"' tools/check-hook-destinations.sh` runs, it prints 1, and
  `grep -c 'done <"\$pin_file"' tools/workflows/unattended-build.test.sh` prints 1.
  `bash -n tools/check-hook-destinations.sh` and `bash -n tools/workflows/unattended-build.test.sh`
  each exit 0.
  Red when: a loop still reads a here-string over a substituted variable, as at `22621f55a`, where the
  first two commands each print 2.
- **AC2** — When `grep -B1 -A1 '^path = ".governance/install.json"' tools/govkit/registry.toml` runs,
  it prints three lines: `[[exempt]]`, the path, and a `why` line holding the reason. When
  `grep -c '".governance/install.json"' tools/gate-legs.json` runs, it prints 1.
  Red when: no exempt row names the file, as at `22621f55a`, where the first prints nothing, or the
  guard entry is dropped to clear the leg, so the second prints 0.
- **AC3** — When `grep -A12 '"name": "hook destinations self-test"' tools/gate-legs.json | grep -c '/workflows/'`
  runs, it prints 3.
  Red when: the suite reads a kit its leg's guard omits, as at `22621f55a`, where it prints 0.
- **AC4** — When `grep -c 'check-install-prefix.test.sh:271 drives' memory/project/unarmed-branches.txt`
  runs, it prints 1, and `grep -n 'no kit directories' tools/check-install-prefix.test.sh` prints one
  line opening `271:`. `sed -n 40p memory/project/unarmed-branches.txt | awk -F'\t' '{print NF}'`
  prints 5.
  Red when: the reason cites any other line, as at `22621f55a`, where the first prints 0.
  figure: 271 is PINNED at `22621f55a`, and the second command re-derives it.
- **AC5** — When `git show --name-only --format=%B HEAD` runs at this unit's build commit, it lists
  `memory/guides/SESSION-KICKOFF.md` beside `tools/gate-legs.json` and prints a line opening
  `manifest-audit: delta`. When `bash $TEMP/fh47probe` runs at that commit from the repository root,
  it prints 1.
  Red when: `last-body-change` stays at `201eb127c`, where the probe prints 11 at `22621f55a`, past
  the stall check's limit of ten.
  fixture: the probe is the Design section's fenced block, saved to `$TEMP/fh47probe` and removed after
  the pass.
  figure: 1 is DERIVED at the build commit, which is the one watched commit after its own parent.
  11 is PINNED at `22621f55a`.

## 6. Gates

`shell hygiene (a loop fed by a command substitution)` · `shell hygiene (a fork spent on builtin work)` · `shell hygiene (a fixed-name temp renamed into place)` · `hook destinations (every declared hook path ships)` · `hook destinations self-test` · `govkit selfcheck` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `policy fixtures` · `harness arms (fail branches armed or pinned)` · `kickoff-manifest ratchet` · `unattended-build self-test` · `verifier fan-out self-test` · `tier2-review self-test` · `review-join self-test` · `run-gates canary` · `run-gates gov canary` · `measure-legs selftest` · `recall floor` · `recall floor arms` · `drift-audit records` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

This unit adds and moves no arm. S1's suite edit keeps every assertion and its name, and S2 to S5 are
declarations the legs above already read.

The verdicts of S1, S2 and S5 are derived from each leg's source and the files' text, not from leg
output. This spec's author may run none of these legs, so the main loop reads their first real output
at the close. The loop's behaviour in S1 is observed there too, by the two hook destinations legs and
by `unattended-build self-test`, and the criteria above are the pass's own reading of the text.

## 7. Open questions

none

## 8. Revision log

- rev-1 · 2026-11-04 · S1 to S5 · AC1 to AC5 · initial draft: the three lint reds of the close's
  second read and the two items unit 45's builder named, from brief
  `2026-11-04-prompt-TOOL-dFairHearing-47-spec-brief`. S4 cites 271 where the brief read 249. AC2 and
  AC3 observe through plain greps, and AC5's count through the Design section's probe, so no word of
  the acceptance section reads as a path.

## 9. Reuse audit

Each item extends a seam the tree already carries. S1 takes the `mktemp` and trap form of
`tools/check-line-length.sh:294`, and the recipe ask `TOOL-aLeakedHandle-4` states: write the walk to a
file, read it by redirect, remove it on every exit. S2 extends the `[[exempt]]` rows of
`tools/govkit/registry.toml:335-341`, S3 the leg's own guard list, and S4 and S5 edit two records in
place. `python tools/codebase-map/reuse_lookup.py "feed a shell while read loop from a scratch file instead of a here-string"`
and `"declare a guard pathspec class for a root file gov does not ship"` ranked generic name stems
only, so no existing seam fits beyond those. Two recall hits were stale against the code, and the code won:
`TOOL-aWalkedCorpus-5` counts four prefix classes where the partition now holds six, and the
`dMindYourWords` audit's fix for a root file widens `derive_root_confs`, which describes a kit's conf
and not a receipt. `gotchas.py --for-paths` over the write set named
`held-suite-guard-misses-a-sibling-kit`, which decides S3's form, and
`a-grep-for-a-word-is-a-presence-probe`, which is why the Gates section leaves the behaviour to the
legs.

Recall terms used: `python tools/memory-recall/query.py "a guard pathspec naming a root file falls into no declared class, and a loop fed by a variable assigned from a command substitution" --terms "guard pathspec partition exempt registry.toml selfcheck here-string scratch file substitution-fed last-body-change manifest stall"`
