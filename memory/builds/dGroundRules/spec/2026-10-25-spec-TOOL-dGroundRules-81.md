# TOOL-dGroundRules-81 — policy-mirror.js resolves every PATH bash that can see the shim again, and its comment and refusal say what it does

**Status:** CLOSED · rev-1 · 2026-10-25 · node d · Tier-1 · base 59f02fde · streams tooling · order 28

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dGroundRules-1-runlog-28554d7f.md](../build/2026-10-25-build-TOOL-dGroundRules-1-runlog-28554d7f.md) | journal | TOOL-dGroundRules-1 TOOL-dGroundRules-2 TOOL-dGroundRules-3 TOOL-dGroundRules-4 TOOL-dGroundRules-5 TOOL-dGroundRules-6 TOOL-dGroundRules-7 TOOL-dGroundRules-8 TOOL-dGroundRules-9 TOOL-dGroundRules-10 TOOL-dGroundRules-11 TOOL-dGroundRules-14 TOOL-dGroundRules-15 TOOL-dGroundRules-16 TOOL-dGroundRules-17 TOOL-dGroundRules-18 TOOL-dGroundRules-19 TOOL-dGroundRules-20 TOOL-dGroundRules-21 TOOL-dGroundRules-22 TOOL-dGroundRules-23 TOOL-dGroundRules-24 TOOL-dGroundRules-25 TOOL-dGroundRules-26 TOOL-dGroundRules-27 TOOL-dGroundRules-28 TOOL-dGroundRules-29 TOOL-dGroundRules-30 TOOL-dGroundRules-31 TOOL-dGroundRules-32 TOOL-dGroundRules-33 TOOL-dGroundRules-34 TOOL-dGroundRules-35 TOOL-dGroundRules-36 TOOL-dGroundRules-37 TOOL-dGroundRules-38 TOOL-dGroundRules-39 TOOL-dGroundRules-40 TOOL-dGroundRules-41 TOOL-dGroundRules-42 TOOL-dGroundRules-43 TOOL-dGroundRules-44 TOOL-dGroundRules-45 TOOL-dGroundRules-46 TOOL-dGroundRules-47 TOOL-dGroundRules-48 TOOL-dGroundRules-49 TOOL-dGroundRules-50 TOOL-dGroundRules-52 TOOL-dGroundRules-55 TOOL-dGroundRules-56 TOOL-dGroundRules-60 TOOL-dGroundRules-61 TOOL-dGroundRules-62 TOOL-dGroundRules-63 TOOL-dGroundRules-64 TOOL-dGroundRules-65 TOOL-dGroundRules-66 TOOL-dGroundRules-67 TOOL-dGroundRules-68 TOOL-dGroundRules-69 TOOL-dGroundRules-70 TOOL-dGroundRules-71 TOOL-dGroundRules-72 TOOL-dGroundRules-73 TOOL-dGroundRules-74 TOOL-dGroundRules-75 TOOL-dGroundRules-76 TOOL-dGroundRules-77 TOOL-dGroundRules-78 TOOL-dGroundRules-79 TOOL-dGroundRules-80 TOOL-dGroundRules-82 TOOL-dGroundRules-83 TOOL-dGroundRules-84 TOOL-dGroundRules-85 TOOL-dGroundRules-86 TOOL-dGroundRules-87 TOOL-dGroundRules-88 |
| [2026-10-25-prompt-TOOL-dGroundRules-81-1-spec-writer.md](../prompts/2026-10-25-prompt-TOOL-dGroundRules-81-1-spec-writer.md) | journal | — |
| [2026-10-25-prompt-TOOL-dGroundRules-81-spec-brief.md](../prompts/2026-10-25-prompt-TOOL-dGroundRules-81-spec-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

`TOOL-dGroundRules-78` S3 narrowed `resolveBash` in `tools/policy/policy-mirror.js` to the first
`bash` on PATH. A host whose first PATH bash is the System32 WSL launcher, with Git's bash later on
PATH, now resolves no bash at all, so every policy read through the helper refuses and agent-cap
rule 7 denies every Agent and Workflow call. This unit puts back the scan of every PATH bash, and
makes the comment above `let BASH;`, the refusal in `runShim` and the kit README state that order
and name `export GOV_BASH=<path>` as the remedy.

## 2. Scope (IN)

- **S1** — In `resolveBash` (`tools/policy/policy-mirror.js:62-73`), the candidate `onPath[0]` in
  `cands` (`:66`) becomes `...onPath`, and the comment above `let BASH;` (`:56-60`) becomes the text
  §4 "The comment" gives. Observed by AC1 and AC3.
- **S2** — The refusal `runShim` throws when no candidate can see the shim (`:80`) becomes the text
  §4 "The refusal" gives. Observed by AC2 and AC3.
- **S3** — The resolver clause in the `**Read from the landed blob only.**` paragraph of
  `tools/policy/README.md` (`:321-323`) becomes the text §4 "The README" gives. Observed by AC4.

## 3. Non-goals (OUT)

- `resolve_bash` in Python, the canonical `tools/lib/resolve_bash.py` and its inline copy in
  `tools/policy/check_policy.py` (`:892-913`). They keep the first PATH bash, for the reason §4
  "Alternatives rejected" gives. The fixture's own `WRONG` line about that resolver
  (`tools/policy/check_policy.py:2238`) is not this unit's refusal and stays.
- The persistent gate that compares the two resolvers' order. `TOOL-dGroundRules-82` builds it after
  this unit, from the order §4 states.
- The `onPath` stat cost the review's L1 named. With the full scan back every stat is read again,
  so L1 reduces to the comment S1 rewrites.
- The file header's sentence at `tools/policy/policy-mirror.js:33-34`, which says the bash is found
  "by running each candidate as the policy kit's checker finds it". It states the method, which both
  resolvers share, and no order, so it stays true.
- `help/policy.md`, which names no bash resolver. Any other spec, and the review's other findings.

### Edges

- **hands-off** `TOOL-dGroundRules-82` — asserts the order §4 "The order" states against the
  canonical resolver's, and reds when either side adds, drops or reorders a candidate.

## 4. Design

### Evidence

Read at `59f02fde9`. Both premises hold.

- **M3 (id 9).** `tools/policy/policy-mirror.js:66` builds `cands` from `ENV.GOV_BASH`, `onPath[0]`,
  the two Git for Windows paths and a bare `bash`. On Windows the bare name resolves by PATH order,
  so it reaches the same first `bash.exe` and adds nothing. The comment at `:56` says candidates are
  found "never by its place on PATH", and the refusal at `:80` says "PATH's bash ... were each run".
  At `fce5603f8` the same line spread `...onPath`. The probe `p81.js` (§5) stubs `spawnSync` with a
  PATH of two directories. D1's `bash` stands for the WSL launcher and fails `test -f`, and D2's
  `bash` stands for a later Git bash that passes. At `59f02fde9` the module tried
  `GB ; D1/bash ; C:/Program Files/Git/bin/bash.exe ; C:/Program Files/Git/usr/bin/bash.exe ; bash`
  and refused `no bash can see`. The module at `fce5603f8` ran the shim under `D2/bash`.
- **L1 (id 4).** `onPath` (`:64-65`) still calls `fs.existsSync` on `bash.exe` and `bash` in every
  PATH directory, and `:66` reads one entry. The comment at `:56-58` claims the order `resolve_bash`
  takes. That resolver (`tools/policy/check_policy.py:899`) asks `shutil.which("bash")` once.

### The order

`TOOL-dGroundRules-82` copies this line:

```
resolveBash tries GOV_BASH ; then each existing bash.exe then bash in every PATH directory, in PATH order ; then C:/Program Files/Git/bin/bash.exe ; then C:/Program Files/Git/usr/bin/bash.exe ; then bash — a repeat tried once, the first whose test -f on the shim exits 0 kept. resolve_bash holds the same order with one PATH bash, the one shutil.which("bash") names, in the PATH slot.
```

The two lists agree on GOV_BASH first and on the last three candidates. They differ in the PATH
slot. The JS tries every PATH bash, and Python tries the one `shutil.which` names. On Windows,
`shutil.which` also searches the current directory first and tries each PATHEXT name, and it skips a
directory or a non-executable file named `bash`, which `fs.existsSync` keeps. So the JS's first PATH
entry equals `shutil.which`'s answer only where the first PATH directory holding a bash holds a
`bash.exe` or `bash` file, as `TOOL-dGroundRules-78` §4 S3 already recorded. Every candidate on
either side is then run with `test -f`, so the difference changes only which working bash is taken.

### The code

In `resolveBash`, `cands` reads:

```
  const cands = [ENV.GOV_BASH, ...onPath, "C:/Program Files/Git/bin/bash.exe", "C:/Program Files/Git/usr/bin/bash.exe", "bash"];
```

That is the line at `fce5603f8`. `onPath` and the loop stay as they are. The `new Set` drops a
repeat, such as a bare `GOV_BASH` that equals a PATH entry.

### The comment

The five lines above `let BASH;` become:

```
// The bash that can SEE the shim. Each candidate is RUN, and the first under which `test -f` on the
// shim exits 0 is kept, so a bash's place on PATH sets when it is tried, never whether it is taken.
// The order: GOV_BASH, then each `bash.exe` and `bash` that exists in each PATH directory, taken
// in PATH order, then Git for Windows' two paths, then the bare name, a repeat tried once. On Windows
// the first PATH bash can be the System32 WSL launcher, which cannot open a `C:/` path, and the bare
// name reaches it too (gotcha subprocess-resolves-a-different-shell), so every later PATH bash is
// tried before Git's fixed paths. The checker's `resolve_bash` holds the same order with one PATH
// bash, the one `shutil.which("bash")` names, in that slot. Where none can see the shim,
// `export GOV_BASH=<path>`. Found once per process.
```

### The refusal

In `runShim`, the template literal's text after `no bash can see ${SHIM}: ` becomes:

```
GOV_BASH, each bash on PATH in order, Git for Windows' two and the bare name were each run; export GOV_BASH=<path> naming one that can
```

The `policy: refused · ${MIRROR_REL}:0 · ` prefix stays. `git grep` finds no other reader of the
old text outside `memory/`. The only other `no bash can see` line is the Python fixture's own
(`tools/policy/check_policy.py:2238`), which this unit does not touch.

### The README

In `tools/policy/README.md`, the two lines from the one opening `` `GOV_BASH`, the first bash `` to the
one ending `every shim outcome` become:

```
`GOV_BASH`, each bash PATH names in PATH order, then Git for Windows' two and the bare name, the first
that can see the shim kept, and `export GOV_BASH=<path>` names one where none can; every shim outcome
```

The line before them, ending `by running each candidate,`, and the line after, opening
`but exit 0`, stay.

### What this does not check

AC1 and AC2 run the module with `spawnSync` stubbed, so no real WSL launcher or Git bash is run.
They show the candidates the module tries and the one it keeps. They do not show that a real host's
PATH puts the WSL launcher first, which the review graded narrow. Nothing here compares the JS order
with the Python order. `TOOL-dGroundRules-82` adds that gate.

### Alternatives rejected

- Widening `resolve_bash` to scan every PATH entry, the review's first option. The parity
  `TOOL-dGroundRules-82` asserts does not need it: the relation §4 "The order" states holds with
  Python unchanged. The function is a byte-identical copy of `tools/lib/resolve_bash.py`, held by a
  parity row (`tools/lib/resolve-python.test.sh:186`) and copied inline in
  `tools/policy/check_policy.py:892-913`. Widening it moves every caller of the canonical and the
  `policy fixtures` leg's resolver, which is outside this write set. The checker runs under the bar,
  where the first PATH bash is Git's, and it reds a `WRONG` that names `GOV_BASH` otherwise.
- The review's fallback, keeping `onPath[0]` and only rewording the comment and refusal. It leaves
  the lost case M3 measured.
- The skeptic's L1 fix, stopping `onPath` at its first file. With the full scan back every entry is
  read.

### Rollout

The builder sets this spec's status from DEFERRED to INPROGRESS before its first write. Scratch-guard
admits writes under `ROUTED_PATHS` for a Tier-1 unit only at INPROGRESS, or at SPECCED once graded.
No help page changes. `help/policy.md` names no bash resolver, and the refusal names its own remedy.

### Files touched (estimate)

- `tools/policy/policy-mirror.js`
- `tools/policy/README.md`

## 5. Acceptance criteria

All commands run from the repository root of the pass's worktree. `p81.js` stubs
`child_process.spawnSync` before it loads the module it is given. `git` answers the current
directory. A `test -f` run answers status 0 only for D2's `bash` in mode `wsl`, and status 1 for
every other candidate. A run of the shim answers the refusal `policy: refused · stub`. PATH holds two
scratch directories, D1 then D2, each holding a file named `bash`, and `GOV_BASH` is `GB`. The script
prints, on one line joined by ` ; `, each candidate tried, each shim run, and the message
`readPolicy` threw, with the scratch directories spelled D1 and D2 and the module's directory spelled
KIT.

```
cat > "$TEMP/p81.js" <<'EOF'
const fs = require("fs"), os = require("os"), path = require("path"), cp = require("child_process");
const mod = path.resolve(process.argv[2]), mode = process.argv[3];
const d1 = fs.mkdtempSync(path.join(os.tmpdir(), "p81a-")), d2 = fs.mkdtempSync(path.join(os.tmpdir(), "p81b-"));
for (const d of [d1, d2]) fs.writeFileSync(path.join(d, "bash"), "");
process.env.PATH = [d1, d2].join(path.delimiter); process.env.GOV_BASH = "GB";
const sees = mode === "wsl" ? path.join(d2, "bash") : "";
const out = [];
cp.spawnSync = (c, args) => {
  if (c === "git") return { status: 0, stdout: process.cwd() + "\n" };
  if (args[0] === "-c") { out.push(c); return { status: c === sees ? 0 : 1 }; }
  out.push(c + " runs " + args.slice(1).join(" "));
  return { status: 2, stderr: "policy: refused · stub" };
};
const { readPolicy } = require(mod);
try { readPolicy("runtime.agents-in-flight", { repo: process.cwd() }); } catch (e) { out.push(e.message); }
const kit = path.dirname(mod).split(path.sep).join("/");
console.log(out.map((c) => c.split(d1).join("D1").split(d2).join("D2").split(path.sep).join("/").split(kit).join("KIT")).join(" ; "));
EOF
```

After S1 and S2, mode `none` is expected to print this line:

```
GB ; D1/bash ; D2/bash ; C:/Program Files/Git/bin/bash.exe ; C:/Program Files/Git/usr/bin/bash.exe ; bash ; policy: refused · .governance/policy.json:0 · no bash can see KIT/policy-shim.sh: GOV_BASH, each bash on PATH in order, Git for Windows' two and the bare name were each run; export GOV_BASH=<path> naming one that can
```

A scratch copy of the module at `59f02fde9` with S1's code line and S2 applied was measured printing
both expected lines. The `policy fixtures`, `policy check` and `agent-cap self-test` legs are gates
this pass may not run. The main loop runs them at the close (§6).

- **AC1** — When `node "$TEMP/p81.js" tools/policy/policy-mirror.js wsl` runs, it prints exactly `GB ; D1/bash ; D2/bash ; D2/bash runs landed ; policy: refused · stub`.
  Red when: `cands` holds `onPath[0]` again. Then it prints a line that holds no `D2/bash`, tries the two Git for Windows paths and the bare `bash`, and refuses `no bash can see`, as it did at `59f02fde9`.
  The module at `fce5603f8` printed the expected line.
- **AC2** — When `node "$TEMP/p81.js" tools/policy/policy-mirror.js none` runs, it prints the line
  given above the criteria for mode `none`.
  Red when: the refusal keeps its old text, or a candidate is dropped or reordered. At `59f02fde9`
  the line held no `D2/bash` and ended `PATH's bash and Git for Windows' two were each run`.
- **AC3** — When `grep -c 'export GOV_BASH=<path>' tools/policy/policy-mirror.js` runs, it prints `2`, and `grep -c 'never by its place on PATH' tools/policy/policy-mirror.js` prints `0`, and `grep -c "in PATH order, then Git for Windows' two paths, then the bare name" tools/policy/policy-mirror.js` prints `1`.
  Red when: the comment above `let BASH;` keeps its old text, or either the comment or the refusal
  does not name the remedy. At `59f02fde9` they printed `0`, `1` and `0`.
- **AC4** — When `grep -c "each bash PATH names in PATH order, then Git for Windows' two and the bare name, the first" tools/policy/README.md` runs, it prints `1`, and `grep -c 'the first bash PATH names' tools/policy/README.md` prints `0`.
  Red when: the README still names only the first PATH bash. At `59f02fde9` they printed `0` and `1`.

## 6. Gates

`policy fixtures` · `policy check` · `agent-cap self-test` · `govkit selfcheck` · `kit epoch (shipped bytes move, the version moves)` · `spec tokens (a spec's own names resolve)` · `memory hygiene`

Run through `derive_guarded_legs` at `59f02fde9`,
`python tools/check-spec-tokens.py --legs-for tools/policy/policy-mirror.js tools/policy/README.md`
names one non-broad guarded leg for both files, `policy fixtures`, through `tools/policy/`. Every
other leg it prints trips only on the broad `tools/`.

Legs named beside it read what this unit changes without their guard tripping. `policy check` runs
`tools/policy/check_policy.py` live, whose `arm_mirror_landed` runs `node policy-mirror.js get` per
key (`tools/policy/check_policy.py:349-373`). `agent-cap self-test` copies `policy-mirror.js` into
its rule-7 checkout (`tools/hooks/agent-cap.test.sh:1196`), and its guard holds no `tools/policy/`
line. `govkit selfcheck` reads the policy kit's prose, and the README lines name no re-render word.
`kit epoch` reads the policy kit's shipped bytes and prints the version move as owed at the lander.

No case in the `policy fixtures` leg reads the refusal text or counts the candidates, so no figure
moves. `tools/policy/check_policy.py` is not touched, so the leg does not grow, and its budget of
970 and ceiling of 1290 stand. No arm is added or moved, so this unit declares no new suite arm. The
persistent row over the resolver order is `TOOL-dGroundRules-82`'s, and AC1 and AC2 are this unit's
probes of the change.

## 7. Open questions

none

## 8. Revision log

- rev-1 · 2026-10-25 · initial draft from the closing review's round-2 findings M3 (id 9) and L1
  (id 4), and this unit's spec brief, grounded at `59f02fde9`. Both premises hold. The lost case was
  reproduced with a stubbed `spawnSync` probe against the module at `59f02fde9`, which refused, and
  at `fce5603f8`, which ran the shim under the second PATH bash. A scratch copy with S1's code line
  and S2 applied printed both lines §5 expects. M3 takes the skeptic-SOUND fix in the shape the brief
  directs. The JS scan is restored and Python is not widened, because the parity the next unit
  asserts holds without it. L1 then reduces to the comment. The review report and the brief, both
  untracked when this draft was written:

```
memory/builds/dGroundRules/reviews/2026-10-25-review-TOOL-dGroundRules-72-79-closing-diff-round2.md
memory/builds/dGroundRules/prompts/2026-10-25-prompt-TOOL-dGroundRules-81-spec-brief.md
```

The review's left-shift gate for M3 and its L2 parity row are one fixture, and
`TOOL-dGroundRules-82` builds it. Its class is the gotcha
`a-view-fix-trades-one-blindness-for-another`.

## 9. Reuse audit

This unit builds no mechanism. S1 puts back the line `resolveBash` held at `fce5603f8`, in the
existing seam. The probe reuses `TOOL-dGroundRules-78`'s `p78.js` stub of `spawnSync`, with a
PATH whose first bash cannot see the shim and a mode that lets a later one see it.
`python tools/codebase-map/reuse_lookup.py "find the bash that can see a script by running each PATH candidate"`
ranked `resolve_bash` (fan-in 5, a seam) first. That is the Python resolver §4 "Alternatives
rejected" keeps unchanged. The JS `resolveBash` is the only JS one, and this unit edits it in place.
The recall probe returned `TOOL-aMendedFleet-98`, which made a Python suite's `bash` resolve to Git
Bash and never to the WSL launcher, `TOOL-dGroundRules-78`'s S3, which this unit partly reverses,
and `TOOL-dSettledRoster-6`, on the `resolve_bash` copies that probe weaker properties. None of
them holds a JS resolver.

Recall terms used: `python tools/memory-recall/query.py "bash resolver every PATH bash WSL launcher first GOV_BASH" --terms "resolveBash resolve_bash onPath GOV_BASH WSL"`
