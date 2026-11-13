# TOOL-aClearedLedger-3 — the gate guard denies a flag-form suite the leg manifest declares above the direct-check bound, and its parity arm reads every direct-check form

**Status:** SPECCED · rev-1 · 2026-11-13 · node a · Tier-2 · base 8db6f4be · streams tooling · order 3 · closes TOOL-aNimbleMend-16

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-13-prompt-TOOL-aClearedLedger-1-brief.md](../prompts/2026-11-13-prompt-TOOL-aClearedLedger-1-brief.md) | research | TOOL-aClearedLedger-1 TOOL-aClearedLedger-2 TOOL-aClearedLedger-4 TOOL-aClearedLedger-5 TOOL-aClearedLedger-6 TOOL-aClearedLedger-7 TOOL-aClearedLedger-9 TOOL-aClearedLedger-10 |

<!-- /gen:spec-records -->

## 1. Goal

The gate guard's suite reds on two parity arms because six `chunk = selftests` legs of the gate
manifest are suites the hook admits at `BUILDING`. Three of them are suites by measured cost that
the hook cannot see in a flag, so the hook is wrong there; three are direct checks in a form the
arm does not read, so the arm's rule is wrong there. This unit gives the hook one row that reads
the manifest, and gives the arm the one form it lacks, so the two agree with no exemption added.

## 2. Scope (IN)

- **S1** — `tools/unattended/gate-guard.js` gains row D6. A simple command whose script word and
  following words name a `chunk = selftests` leg of the gate manifest, in a direct-check form and
  with a `ceiling` above `DIRECT_CHECK_BOUND`, is a hit while the branch's run is before
  `VERIFYING`. The match rule is §4, "Row D6". Observed by AC1 and AC3.
- **S2** — A direct-check form at or under the bound, a case-scoped variant of a leg, and every
  command at an allowed phase stay admitted. Observed by AC2 and AC4.
- **S3** — The hook reads no file for a command that carries neither a D1 to D5 hit nor a D6
  candidate, and reads the manifest only after a live run is found. Observed by AC5.
- **S4** — Row D6 fails open: an absent manifest, one that does not parse, and one that is no
  list each leave the row unarmed and the command admitted. Observed by AC6.
- **S5** — The parity arm of `tools/unattended/gate-guard.test.sh` reads three direct-check forms,
  `--selftest`, `--fixture` and `fixture`, and exempts a leg in any of them only at or under the
  bound. A leg in such a form above the bound is graded like every other leg: the hook must deny
  it. `PARITY_EXEMPT` holds `test_recall_floor.py` alone. Observed by AC7.
- **S6** — The suite pins the hook's two new constants against its own restatement of them, as it
  pins `PHASES_ALLOW`, so the arm and the hook share no state. Observed by AC8.
- **S7** — The suite gains the arm class "a manifest suite in flag form" over a planted manifest
  beside a copy of the hook (§4, "The suite"). Observed by AC1 to AC4 and AC6, whose probes are
  the arms' payloads; the suite's own verdict is the main loop's, declared in §7.
- **S8** — The texts say what S1 makes true: the header comment of `tools/unattended/gate-guard.js`
  and the paragraph of `tools/unattended/README.md` that lists what the hook refuses. Observed by
  AC9 for the README. The header comment is NOT OBSERVED: no probe tells a true comment from a
  stale one, and the closing review reads it against the code.

## 3. Non-goals (OUT)

- Any new member of `PARITY_EXEMPT`, and any raised bound. The brief forbids an exemption added
  to pass the arm.
- Any edit to `tools/gate-legs.json`. No leg's argv, ceiling or guard moves here.
- A file whose name ends `selftest.py` for any flag-form suite, the cure ask TOOL-aDeferredBar-12
  names. §4 says why it lost.
- `tools/check-spec-tokens.py`, its matcher `BAR` and its suite's parity arm. That reader is this
  build's unit 5, and its exemption list and bound are its own.
- A deny of a direct-check form at or under the bound. A `--selftest` flag or a fixture is the
  direct check `memory/TEMPLATE-SPEC.md` names for an acceptance criterion.
- The `test_recall_floor.py` exemption, which stays as it is; ask TOOL-aDeferredBar-11 owns it.
- The summary sentences in `tools/unattended/VERBS.template.md` and
  `memory/guides/SESSION-KICKOFF.md`. Each names the flag and the suite shapes and stays true.
- The role-gate arm of `tools/hooks/scratch-guard.js`, which already refuses a manifest leg to a
  role agent.
- Any kit version, which the lander's `mint` moves.

### Edges

- **consumes-from** external — the gate manifest's `chunk`, `argv` and `ceiling` fields as the
  run-gates kit writes them. Without a `ceiling` on a row, row D6 never fires for that row.
- **hands-off** external — the second reader of the same manifest, the spec-token checker's
  matcher and its parity arm, which this build's unit 5 repairs at its own cause.
- **hands-off** external — the ceilings themselves. A re-derived ceiling moves a leg across the
  bound, and both the hook and the arm follow it at run time with no edit here.

## 4. Design

### Evidence

Read at `82ceaab5`, the branch tip. The suite's output is the main loop's run at `8db6f4be` on a
frozen clone, the file `a16.out` the brief names.

- **The arm reports six legs at `8db6f4be`.** `a16.out` prints
  `FAIL parity: a manifest suite invocation the hook does NOT deny at BUILDING:` and names
  `routed_commits.py --selftest`, `measure_legs.py --selftest`, three playbook `fixture` legs and
  the `policy fixtures` leg.
- **The count arm fails for two of them at `8db6f4be`.** The arm at
  `tools/unattended/gate-guard.test.sh@d1d0bae33417:404` counts an over-bound `--selftest` leg in
  neither the graded nor the exempt total, so the sum at line 428 of that blob is two short of
  the manifest's count.
- **The hook cannot see a flag.** `tools/unattended/gate-guard.js#resolveFileRow` matches a word
  ending `run-selftests.sh`, `run-unattended-gates.sh`, `.test.sh` or `selftest.py`, and nothing
  else. The header of that file says the hook does not read a ceiling.
- **The predicate hits 53 of the manifest's 74 selftests legs** (PINNED, 2026-11-13, at `82ceaab5`).
  The probe fed each leg's argv to `scanDenyHits`.
  Of the 21 misses, 16 carry a ceiling of 300 and five a higher one (PINNED, 2026-11-13).
- **Three reported legs are suites by measured cost.** `tools/run-gates/selftest-budgets.txt`
  records three readings, each of a leg alone.
  `routed-commits selftest` read 330 s (PINNED, 2026-11-13, at `2ba17e9d`).
  `policy fixtures` read 1210 s (PINNED, 2026-11-13, at `2ba17e9d`).
  `measure-legs selftest` carries a proxy of 250 s (PINNED, 2026-10-15, node d).
  The hook admits each at `BUILDING`: the fixture of "The probe set" answered exit 0 for all
  three at `82ceaab5`.
- **Their ceilings crossed the bound with no hook-relevant diff.** Commit `cf2c673f3` raised two
  ceilings from re-measured budget rows.
  `routed-commits selftest` sits at ceiling 660 in the manifest (PINNED, 2026-11-13, at `82ceaab5`).
  `measure-legs selftest` sits at ceiling 500 there (PINNED, 2026-11-13, at `82ceaab5`).
- **The three playbook legs are direct checks in a form the arm does not read.** Their argv ends
  in the bare word `fixture`, and the arm's exemption tests the one word `--selftest`.
  Each carries ceiling 300 (PINNED, 2026-11-13, at `82ceaab5`).
  They entered the manifest with commit `399788aca`.
- **Two more suites are admitted behind declared exemptions**, both members of `PARITY_EXEMPT`.
  `corpus_ids.py --selftest` sits at ceiling 2690 (PINNED, 2026-11-13, at `82ceaab5`).
  `gen_build_index.py --selftest` sits at ceiling 350 (PINNED, 2026-11-13, at `82ceaab5`).
  Ask TOOL-aDeferredBar-12 records both.
- **A sibling hook already reads the manifest.** `tools/hooks/scratch-guard.js#readGateLegs`
  takes each leg from its first path-bearing word on, and `checkGateLeg` compares the command's
  words to it. That arm binds a role agent only; the gate guard binds the main loop too.
- **A redirection is a word to this hook.** `scanSegments` returns `>`, `x.log` and `2>` as words
  of `python … --selftest > x.log 2>&1` (PINNED, 2026-11-13, at `82ceaab5`), so a word-for-word
  compare must take redirections out first, as `scratch-guard.js#scanCommandHeads` does.

### Which side is wrong

The hook, for every flag-form leg whose ceiling is above the bound. The arm's own comment calls
such a leg "a suite by cost that this hook cannot deny textually", and the measured costs agree.
The hook exists to stop a suite inside a build pass, so the cure is a hook that denies it.

The arm, for the three `fixture` legs. They sit at the bound, like the `--selftest` legs the arm
already exempts, and a fixture is a direct check the spec format names. The arm's rule names one
spelling of a class that has three.

### Row D6

Three constants join the hook, and all three are exported.

| Constant | Value | Meaning |
|---|---|---|
| `DIRECT_CHECK_BOUND` | 300 | a leg whose `ceiling` is at or under it is a direct check; the manifest's default ceiling (PINNED, 2026-09-14, the value the suite declares today) |
| `DIRECT_CHECK_WORDS` | `--selftest`, `--fixture`, `fixture` | the argument words that make a script run its own checks |
| `MANIFEST_BASENAME` | `gate-legs.json` | read in the directory above the hook's own, where the suite already reads it |

**A candidate.** `scanDenyHits` takes a fifth, optional argument, an array. When it is passed,
each simple command whose head word carries no D2 to D4 row, and whose words after the head
include a member of `DIRECT_CHECK_WORDS`, pushes `{ head, words }` onto it. `words` is the head
and every word after it with redirections taken out: a word matching
`^(?:\d*|&)(?:>>?|<{1,3})` is dropped, and so is the word after it when the target is not glued.
The function's return value does not change, and both recursions hand the array on, so a
candidate inside a `bash -c` body or a double-quoted `$( … )` span is found.

**The manifest.** `readSuiteLegs(file)` returns `[{ name, ceiling, words }]`: every row of the
JSON list whose `chunk` is `selftests`, whose `argv` is a list of strings, and whose `ceiling` is
a number above `DIRECT_CHECK_BOUND`. `words` is the argv from its first word carrying `/` on, with
a leading `{prefix}/` taken off that first word. Any read or parse failure, and a value that is
no list, returns the empty list.

**The match.** `checkSuiteLeg(candidate, legs)` returns the first leg for which all hold.

1. The candidate's head, with `\` folded to `/` and lower-cased, equals the leg's first word
   lower-cased, or ends with `/` followed by it.
2. The candidate has no more words than the leg, and each of its later words equals the leg's
   word at that place.
3. The candidate reaches the leg's first `DIRECT_CHECK_WORDS` member: its word count is at least
   that member's place in the leg's words, counted from one.

Rule 2 and rule 3 together make a SHORTER spelling a hit and a LONGER or different one a miss.
`check_policy.py --fixture` runs every case and is a hit; `check_policy.py --fixture <case>` runs
one case and is the direct check.

**The order in `checkCommand`.**

1. `scanDenyHits` with a candidate array. No hit and no candidate returns null, with no file read.
2. The repository, the memory root and the live run are resolved as today. None returns null.
3. With a candidate, `readSuiteLegs` reads the manifest once, and each candidate `checkSuiteLeg`
   matches becomes a hit: row `D6`, `what` `suite`, `shape` `a self-test suite`, and a token
   naming the head, the leg's `name` and its ceiling.
4. No hit returns null. Otherwise the deny is rendered by `renderDeny`, unchanged.

`READ_ONLY_VERBS` is not consulted for D6: a command carrying one is a longer spelling and misses
by rule 2.

### The suite

The parity arm keeps its three assertions and its derivation of the population from the real
manifest. Its rule becomes:

| A leg | The arm |
|---|---|
| its script is `test_recall_floor.py` | exempt, printed |
| its argv carries a direct-check word and its ceiling is at or under the bound | exempt, printed with its ceiling |
| every other leg | graded: the hook fed the argv at `BUILDING` must exit 2 |

The branch that names an over-bound `--selftest` leg "not declared exempt" goes: such a leg is
graded. The suite keeps its own `DIRECT_CHECK_BOUND` and its own word list, and one new assertion
compares both to the hook's exports.

The new arm class runs a copy of the hook beside a planted manifest, in the suite's scratch
directory, with the run record at `BUILDING` unless the row says otherwise.

| Arm | Command fed | Expected |
|---|---|---|
| a `--selftest` leg above the bound | the leg's argv | deny, naming the leg |
| the same leg at the bound | the leg's argv | allow |
| a `--fixture` leg above the bound, spelled short | the script and `--fixture` | deny |
| the same leg with a case word | the script, `--fixture`, a case name | allow |
| the over-bound leg behind a redirection | the argv, `> x.log 2>&1` | deny |
| the over-bound leg in a `bash -c` body | `bash -c '<argv>'` | deny |
| the over-bound leg in a double-quoted `$( … )` | `printf '%s' "$(<argv>)"` | deny |
| the over-bound leg, run at `VERIFYING` | the leg's argv | allow |
| the over-bound leg, manifest absent | the leg's argv | allow |
| the over-bound leg, manifest unparsable | the leg's argv | allow |
| a leg above the bound in no direct-check form, planted in the parity population | a bare script | the parity arm reds, naming it |

The last row is the parity arm's staged break, and it is how the arm is seen red after this unit:
the arm must still catch a suite convention neither the word shapes nor row D6 reads.

### The probe set

`<F>` is a directory a pass builds in the session scratchpad: `<F>/.git/HEAD` holds
`ref: refs/heads/fx`, `<F>/.unattended.conf` holds `MEMORY_ROOT=memory`, and
`<F>/memory/builds/fx/RUN.md` holds the two lines `run-branch: refs/heads/fx` and
`phase: BUILDING`. The hook needs no real repository: it reads those three files. Each row is fed
as a `Bash` payload whose `cwd` is `<F>`, to the hook in place, so the manifest read is the real
one.

| Row | Command | Exit |
|---|---|---|
| P1 | `python3 tools/memory-tree/routed_commits.py --selftest` | 2 |
| P2 | `python3 tools/run-gates/measure_legs.py --selftest` | 2 |
| P3 | `python tools/policy/check_policy.py --fixture --strict-from memory/builds/dClosedLoop/build/` | 2 |
| P4 | `python3 tools/memory-tree/corpus_ids.py --selftest` | 2 |
| P5 | `python3 tools/memory-tree/gen_build_index.py --selftest` | 2 |
| P6 | `python3 tools/memory-tree/gotchas.py --selftest` | 0 |
| P7 | `python tools/playbook/core.py fixture` | 0 |
| P8 | `python tools/policy/check_policy.py --fixture` | 2 |
| P9 | `python tools/policy/check_policy.py --fixture one-case` | 0 |
| P10 | `python3 tools/memory-tree/routed_commits.py --selftest > x.log 2>&1` | 2 |
| P11 | `bash -c 'python3 tools/memory-tree/routed_commits.py --selftest'` | 2 |
| P12 | `python3 C:\repo\tools\memory-tree\routed_commits.py --selftest` | 2 |

P12 is fed with `tool_name` `PowerShell`, the tool that spells a path that way; every other row
is a `Bash` payload.

P1 to P7 answered exit 0 on the hook at `82ceaab5` (PINNED, 2026-11-13). The same fixture
answered exit 2 for a `.test.sh` word, so the fixture can produce a deny.

Rows P1 to P5 hold while those legs sit above the bound. A leg a later re-derivation moves to the
bound or under it flips its row to 0 by design, and the probe then names another over-bound leg.

### The candidate probe

AC5 runs this body as the argument of `node -e`, from the worktree's toplevel. It counts the
candidates of three commands: one with no script, one script with a read-only verb, and one
script with a direct-check word.

```js
const g = require('./tools/unattended/gate-guard.js')
const count = (c) => { const a = []; g.scanDenyHits(c, g.buildCommandView(c), 0, 'Bash', a); return a.length }
console.log(count('git status'), count('python3 x/y.py --list'), count('python3 x/y.py --selftest'))
```

### What it does not check

- A flag-form suite the manifest does not declare, or declares in another chunk.
- A leg in a direct-check form whose ceiling is at or under the bound, whatever it costs. The
  three playbook `fixture` legs measured 38 s, 103 s and 161 s alone (PINNED, at `51cd8b402`).
- A different file with the same trailing path. Rule 1 compares a suffix and resolves nothing.
- A longer spelling of a leg, an extra option included. It is read as a scoped variant.
- A suite reached through an assembled path or an interpreter's own spawn, as the header's
  `ponytail:` note already says of the whole predicate.
- A manifest edited in the working tree, which is read uncommitted.

### Inventory

| Minted | Where | Cell |
|---|---|---|
| `readSuiteLegs` | `tools/unattended/gate-guard.js` | `js.function`; `lexicon.py --suggest` answered OK on 2026-11-13 |
| `checkSuiteLeg` | `tools/unattended/gate-guard.js` | `js.function`; `lexicon.py --suggest` answered OK on 2026-11-13 |
| `DIRECT_CHECK_BOUND`, `DIRECT_CHECK_WORDS`, `MANIFEST_BASENAME` | `tools/unattended/gate-guard.js` | constants in the file's screaming case, beside `CONF_BASENAME` |

### Migration

None. An install that holds no manifest above the kit directory keeps today's behaviour.

### Rollout

No switch. The row binds only where the hook already binds: a branch whose run record is before
`VERIFYING`. An attended session with no run record is never refused.

### Files touched (estimate)

- `tools/unattended/gate-guard.js`
- `tools/unattended/gate-guard.test.sh`
- `tools/unattended/README.md`

### Alternatives rejected

- **A `selftest.py` file per flag-form suite**, the cure of ask TOOL-aDeferredBar-12. It writes
  `tools/gate-legs.json`, which this build's units 5, 7 and 10 read as an acceptance input, so the
  passes could not run apart (the build method's M6). It adds a wrapper file to two more kits per
  leg, five legs at `82ceaab5` by the probe above. It does nothing for a leg whose ceiling crosses the
  bound later: commit `cf2c673f3` moved two with no rename to prompt anyone.
- **One literal row per script**, as the matcher `BAR` carries for `check_policy.py`. A list of
  suites typed beside the manifest that declares them. The same commit `cf2c673f3` is the test:
  it would have needed a hook edit that nothing asked for.
- **Two new members of `PARITY_EXEMPT`.** The brief forbids it, and the measured costs say the
  legs are suites.
- **Deny every manifest selftests leg, whatever its ceiling.** It flips the suite's arm
  `F2 a --selftest FLAG on another file -> allow` and withdraws the direct check the spec format
  names. An arm already written refuses it.
- **A candidate with no word test.** Every `python <script>` call would walk to `.git` and read
  each run record. The word test keeps the file reads where a direct-check word is present.
- **Resolving paths against `cwd`**, as `scratch-guard.js#buildGateWord` does. It needs the
  toplevel and a path resolver this hook would copy, to tell apart two files a suffix cannot.
  No install holds two such files.

## 5. Production-readiness checklist

- security — N/A — a hygiene rule that fails open, as the hook's header states of itself. The row
  adds one read of a tracked JSON file and no write.
- perf / scale — a command with no hit and no candidate costs one scan, as today. A candidate
  adds the walk to `.git` and the run-record scan; the manifest is read only when a run is live.
- error / empty / loading states — an absent, unparsable or non-list manifest answers the empty
  list; a row with no `ceiling`, no `argv` or no path-bearing word is skipped. Nothing throws
  past the existing fail-open wrap in `main`.
- observability — the deny names the head word, the manifest leg and its ceiling. An unarmed row
  prints nothing, as every fail-open path of this hook does.
- risks — a leg whose ceiling a later unit of this build re-derives changes side at run time.
  The arm and the hook read the same file, so they move together; the probe rows are stated
  against today's ceilings.
- testing — AC1 to AC9 are probes a pass runs. The arm classes of §7 are the main loop's.
- migration — N/A — no stored shape moves.
- user docs — `tools/unattended/README.md`, S8. No page under `help/` names the hook's rows.

## 6. Acceptance criteria

`<F>` and rows P1 to P12 are §4's probe set. Each row is fed on stdin to
`node tools/unattended/gate-guard.js` from the toplevel of the worktree the unit is built in.

- **AC1** — When rows P1 to P5 are fed to `node tools/unattended/gate-guard.js`, each exits 2 and
  its stderr holds `BLOCKED by gate-guard` and the leg's manifest name.
  Red when: row D6 is absent. At `82ceaab5` each row exits 0.
  figure: the five legs are DERIVED from the manifest's ceilings at observation time.
- **AC2** — When rows P6 and P7 are fed to `node tools/unattended/gate-guard.js`, each exits 0 with
  an empty stderr.
  Red when: the bound is not applied and every direct-check form of the manifest is denied.
- **AC3** — When rows P8, P10, P11 and P12 are fed to `node tools/unattended/gate-guard.js`, each
  exits 2.
  Red when: the compare is exact and a short spelling walks, a redirection word is compared as an
  argument, the candidate array is not handed into the `bash -c` body, or `\` is not folded.
- **AC4** — When row P9 is fed to `node tools/unattended/gate-guard.js`, it exits 0; and when row
  P1 is fed after `phase: VERIFYING` replaces the phase line of `<F>`'s run record, it exits 0.
  Red when: a longer spelling matches by prefix, or row D6 skips the phase test.
- **AC5** — When the candidate probe of §4 runs through `node -e`, it prints `0 0 1`.
  Red when: every launched script is a candidate, which prints `0 1 1`, or none is, which prints
  `0 0 0`.
- **AC6** — When
  `node -p "JSON.stringify(require('./tools/unattended/gate-guard.js').readSuiteLegs('<F>/absent.json'))"`
  runs, it prints `[]`, and it prints `[]` again for a file under `<F>` holding the text `{`.
  Red when: a read or parse failure throws.
- **AC7** — When a pass classifies every `chunk = selftests` leg of `tools/gate-legs.json` with a
  one-off `node -e` probe over the hook's exports, each leg is exactly one of: denied by
  `scanDenyHits`, matched by `checkSuiteLeg` against `readSuiteLegs`, in a direct-check form at
  or under `DIRECT_CHECK_BOUND`, or the script `test_recall_floor.py`. The probe prints the four
  counts and their sum equals the leg count.
  Red when: a leg above the bound falls in no class, which is the parity arm's first failure.
  figure: DERIVED at observation time. At `82ceaab5` the classes read 53, 5, 15 and 1 of 74.
- **AC8** — When `node -p "require('./tools/unattended/gate-guard.js').DIRECT_CHECK_BOUND"` runs,
  it prints `300`; when
  `node -p "require('./tools/unattended/gate-guard.js').DIRECT_CHECK_WORDS.join(',')"` runs, it
  prints `--selftest,--fixture,fixture`; and
  `grep -c 'DIRECT_CHECK_WORDS' tools/unattended/gate-guard.test.sh` prints 1 or more.
  Red when: the constants are not exported, so the suite cannot pin its restatement to them.
  figure: PINNED, 2026-11-13, the bound the suite declares at `82ceaab5`.
- **AC9** — When `grep -n 'gate-legs.json' tools/unattended/README.md` runs, it prints a line of
  the paragraph headed "The act is refused at the tool call".
  Red when: the README still lists the word shapes alone.
- **AC10** — When the main loop runs the suite the `New arm:` lines of §7 name, no line of its
  output opens `FAIL parity:`, and the suite exits 0.
  Red when: a flag-form leg above the bound is admitted, or a leg is counted in neither total.
  At `8db6f4be` the suite prints two such lines.
  permission: a role agent's pass runs no suite. The main loop runs it on a frozen clone.

## 7. Gates

The main loop runs the gate guard's suite at the close, and the bar once after the last unit.
That suite is withheld from the manifest and runs through the unattended kit's own runner.

`install-prefix (shipped surface)` · `codebase-map coverage + freshness` · `kit version markers` · `lexicon naming predicates`

New arm: `tools/unattended/gate-guard.test.sh` · covers AC1 AC2 AC3 AC4 AC6 · the arm class "a manifest suite in flag form"; its failing case is the suite run against a hook whose `DIRECT_CHECK_BOUND` is set above every planted ceiling, so no deny arm of the class holds · `FLOOR_ASSERTIONS` rises by the count of assertions the class adds
New arm: `tools/unattended/gate-guard.test.sh` · covers AC7 AC10 · the parity arm under its new rule; RED is recorded at `8db6f4be` in `a16.out`, and after this unit its failing case is the planted over-bound leg in no direct-check form, the last row of §4's arm table · none
New arm: `tools/unattended/gate-guard.test.sh` · covers AC8 · the pin of the suite's own bound and word list against the hook's exports; its failing case is a hook whose `DIRECT_CHECK_WORDS` lacks `fixture` · `FLOOR_ASSERTIONS` rises by one

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-13 · initial draft.

## 10. Reuse audit

`tools/codebase-map/reuse_lookup.py "a hook denies a self-test suite invocation the gate manifest
declares"` ranked no seam for a manifest read inside a hook; its candidates were name-stem hits
such as `load_manifest` in `tools/run-gates/held_halves.py`, a python reader. The seam was found
by reading: `tools/hooks/scratch-guard.js#readGateLegs` and `checkGateLeg`, the role-gate arm's
row G1. This unit extends the gate guard's own `scanDenyHits` and `checkCommand`, and COPIES the
manifest read's shape and the redirection rule from the sibling hook instead of requiring them,
for the reason `gate-guard.js#buildHeredocView` records: a `require` of a sibling kit's file is a
literal the install-prefix ban refuses, and an adopter may not hold that kit. The recall probe
returned ask TOOL-aDeferredBar-12, the round-2 closing review of aDeferredBar and the spec of
TOOL-aDeferredBar-3; the hits agreed with source except on the exemption list, which the
spec-token suite carries with four members and this suite with three.

Recall terms used: gate-guard parity selftests chunk ceiling DIRECT_CHECK_BOUND PARITY_EXEMPT
flag-form whole-suite fixture manifest deny BUILDING
