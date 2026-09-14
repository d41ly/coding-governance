# TOOL-aProbedUnit-5 — scratch-guard denies an empty temp variable, `/tmp`, and a new entry at the POSIX root

**Status:** SPECCED · rev-1 · 2026-09-14 · node a · Tier-2 · base 1b000d1a · streams tooling · order 5 · ratified 2026-09-14

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-14-prompt-TOOL-aProbedUnit-1-1-spec-briefs.md](../prompts/2026-09-14-prompt-TOOL-aProbedUnit-1-1-spec-briefs.md) | journal | TOOL-aProbedUnit-1 TOOL-aProbedUnit-2 TOOL-aProbedUnit-3 TOOL-aProbedUnit-4 TOOL-aProbedUnit-6 TOOL-aProbedUnit-7 |
| [2026-09-14-review-TOOL-aProbedUnit-1-spec-audit-round1.md](../reviews/2026-09-14-review-TOOL-aProbedUnit-1-spec-audit-round1.md) | spec-audit | TOOL-aProbedUnit-1 TOOL-aProbedUnit-2 TOOL-aProbedUnit-3 TOOL-aProbedUnit-4 TOOL-aProbedUnit-6 TOOL-aProbedUnit-7 |

<!-- /gen:spec-records -->

## 1. Goal

`tools/hooks/scratch-guard.js` reads a write target textually and grades it against the home
directory and the drive root only, so `cp x $TMPDIR/y` with `TMPDIR` empty is allowed and lands
at `/y`, a `/tmp/...` target is allowed by name, and `mkdir -p /mir/x` is allowed because the
drive-root rule needs a drive letter. This unit adds three denials at the one surface that sees
the act, keeps the CLI's own scratch base allowed where it sits inside the newly denied prefix,
and states in the hooks README what the guard still cannot see.

## 2. Scope (IN)

- **S1** — Rule `empty-var`. A write target that opens with `$TMPDIR`, `${TMPDIR}`, `$TMP`,
  `${TMP}`, `$TEMP` or `${TEMP}`, whose variable is empty or unset in the hook's `process.env`, is
  denied with a message naming the variable and saying the write lands at the filesystem root. A
  NON-empty variable is expanded into the target and grading continues on the expansion. The
  `${VAR:-default}` form expands to its default when the variable is empty. A variable the SAME
  command assigns is not graded by this rule, because its value is unknowable textually. Observed
  by AC1, AC2 and AC5.
- **S2** — Rule `tmp`. A target whose comparable form is `/tmp` or sits under it is denied,
  naming the session scratchpad as the destination, UNLESS it sits under an allowed root. The
  allowed roots grow by one: the CLI's scratchpad base, `<os.tmpdir()>/claude`, so a POSIX host
  whose scratchpad sits under `/tmp` keeps the one destination the owner wants. Observed by AC3,
  AC6 and AC7.
- **S3** — Rule `posix-root`. A target `/<top>/...` with no drive letter after
  `buildComparablePath`, whose `<top>` is more than one character and is not in a hand-listed
  POSIX conventional set, is litter and is denied. `tmp` and `temp` are deliberately absent from
  that set, so S2 and S3 agree on `/tmp`. Observed by AC4 and AC8.
- **S4** — `renderDeny` gains one sentence per new kind, so a reader learns which rule they hit
  and where the write belongs. The existing `home` and `drive-root` sentences are unchanged.
  Observed by AC9.
- **S5** — `tools/hooks/scratch-guard.test.sh` gains the arms section 6 names, each denial
  observed RED against the hook at base before the fix lands, and the two existing arms that
  the `/tmp` ruling flips are re-targeted rather than deleted. `FLOOR_ASSERTIONS` rises by the
  arms added. Observed by AC10.
- **S6** — `tools/hooks/README.md`, which today documents `agent-cap` alone, gains a
  `scratch-guard` section stating the five rules and what the predicate does not catch. Observed
  by AC11.
- **S7** — `memory/map/generated/symbols.json` is re-rendered in the same commit, because every
  new top-level function in the hook is a symbol the freshness leg compares. Observed by AC12.

## 3. Non-goals (OUT)

- **The predicate stays TEXTUAL.** It resolves no variable other than the four temp spellings and
  the existing `~` and `$HOME` forms, follows no `cd`, and reads nothing inside a heredoc'd
  script. `cd /tmp && echo x > y` and a Python `open('/tmp/x','w')` inside a heredoc pass exactly
  as they do today. The hook's own header names a real tokenizer as the upgrade path; this unit
  does not take it.
- **No PowerShell variable spelling.** `$env:TEMP\x` opens with `$env:`, which none of the four
  spellings match, so it is graded as it is today: an unresolved token that misses every rule.
  Stated in the README rather than closed, because the corpus measurement that motivated this unit
  was Bash-shaped.
- **UNC paths are not this rule's.** `//server/share/x` has an empty first segment, so the
  `posix-root` regex does not match it and nothing here denies it.
- **The `home` and `drive-root` rules are untouched**, and so are `resolveHomeRoots`,
  `buildRootVariants`, `buildCommandView`, `scanWriteTargets` and the fail-open protocol.
- **No kit version bump inside this unit.** The line-41 constant `KIT_SCRATCH_GUARD_VERSION`
  stays at `1.0`; the `gov:kit agent-cap@1.14` marker on that same line is the kit's and moves to
  `1.15` in the closing pass, once, across every carrier `bash tools/check-kit-versions.sh` names.
  The build README's build-level rules record that.
- **No wiring change.** `tools/hooks/scratch-guard.fragment.json` and `tools/check-wiring.sh`'s
  `scratch-guard` arm are not touched; the hook is already wired and this unit changes what it
  decides, not where it runs.
- **The Git-Bash `/tmp` mapping is recorded, not relitigated.** On node `a`, `cygpath -w /tmp`
  printed `C:\Users\DAILY-~1\AppData\Local\Temp` on 2026-09-14, so a `/tmp/...` write on this
  host lands inside the TEMP root the guard already allows. The owner ruled the denial anyway,
  section 8 F1, and the message names the scratchpad as the remedy.

### Edges

- **hands-off** `TOOL-aProbedUnit-4` — this guard denies the wrong destinations; it cannot supply
  the right one. Handing every harness agent its session scratchpad path, absolute, is that unit's,
  and the deny message here names the scratchpad only as a place, never as a path.
- **consumes-from** external — the CLI's scratchpad layout, `<os.tmpdir()>/claude/<project>/<session>/scratchpad`,
  verified 2026-09-14 on node `a` against this session's own scratchpad path, which sits at
  `C:\Users\DAILY-~1\AppData\Local\Temp\claude\...\scratchpad`. If the CLI moved its base, S2's
  exception would allow a directory nothing writes to and deny the one the CLI uses.
- **hands-off** external — the `agent-cap` marker bump to `1.15`, the closing pass's.

## 4. Design

### The flow today, and where each rule sits

`checkCommand` at `tools/hooks/scratch-guard.js:321` walks `scanWriteTargets`, resolves each
target through `buildResolvedTarget` at `:273`, skips any target under an allowed root at `:328`,
and denies a home-rooted target or a drive-root litter target at `:332` to `:333`, carrying a
`kind` of `home` or `drive-root` into `renderDeny` at `:339`. The three new rules sit in that same
loop, in this order, after the allowed-root skip and before the home test:

1. `empty-var` — decided BEFORE resolution, on the raw `t.value`, because an empty variable leaves
   nothing to resolve. The rest of the loop never sees the target.
2. `tmp` — decided on the resolved comparable form. Sits after the allowed-root skip so
   `<os.tmpdir()>/claude/...` never reaches it.
3. `posix-root` — decided on the resolved comparable form, only when neither the home test nor
   the drive-root test applies, because a POSIX-rooted target has no drive letter and is never
   under a Windows home spelling.

The kinds are disjoint by construction: a target is graded by the first rule that claims it, and
`renderDeny`'s per-kind sentence is chosen by the kinds present in `bad`, exactly as the two
existing kinds are today.

### Rule 1 — `empty-var`

A new function `checkEmptyTempVar(value, env, view)` returns the variable NAME when all three hold:
the raw target matches the anchored form `^\$\{?(TMPDIR|TMP|TEMP)\}?(?=/|$)` with the
alternation ordered longest first so `$TMP` cannot claim `$TMPDIR`; `env[name]` is undefined or
the empty string; and the blanked command view carries no `TMP_ASSIGN`-shaped assignment to that
same name. It returns the empty string otherwise. The third condition is the `TMP=$(mktemp -d);
echo x > $TMP/f` shape, one call assigning and using a shell-local variable the hook's environment
never sees; grading it would deny a correct command on every POSIX host where `TMP` is unset, and
the hook's rule is fail-open on what it cannot read.

`buildResolvedTarget` gains the expansion half: a leading `$TMPDIR`, `${TMPDIR}` or
`${TMPDIR:-default}` (and the `TMP` and `TEMP` twins) becomes the variable's value when that value
is non-empty, the `default` text when the variable is empty and a default is spelled, and is left
as written otherwise. The expanded target then flows through the existing comparable-path fold and
the allowed-root skip, so `echo x > $TEMP/a.log` with `TEMP` set resolves under the TEMP root and
is allowed, which is the behaviour today's corpus depends on.

`${TMPDIR:-/tmp}/y` with `TMPDIR` empty expands to `/tmp/y` and is then rule 2's. That is the
correct reading of the command: the shell would write there.

### Rule 2 — `tmp`, and the root it must not swallow

`checkTmpRoot(resolved)` is `resolved === '/tmp' || resolved.startsWith('/tmp/')` on the
comparable form, spelled through the existing boundary-aware `checkUnderRoot` at `:138` so
`/tmpx` is not `/tmp`. The comparable form of `/tmp/x` is `/tmp/x`: the drive fold at `:66`
rewrites only `/<letter>/`, so a three-letter first segment keeps its leading slash, which is
also why today's `checkDriveRootLitter` never sees it.

`resolveAllowedRoots` at `:125` adds one root: `require('os').tmpdir() + '/claude'`, through the
same `addRoot` that re-spells every root under every known home form. Node's `os.tmpdir()` reads
`TMPDIR`, then `TMP`, then `TEMP` on POSIX and falls back to `/tmp`; on Windows it reads `TEMP`,
then `TMP`, never `TMPDIR`, and falls back to the system temp under `SystemRoot`, measured
2026-09-14 on node `a` as `C:\Windows\temp` with all three unset. An empty variable is falsy and
is skipped, so on a POSIX host with none of the three set the new root is `/tmp/claude`, which is
where the CLI's scratchpad sits on such a host. The gotcha `allowlist-narrower-than-the-root-it-guards` is the class this
exception exists for: the sanctioned destination is INSIDE the denied prefix, and a rule 2 without
this root would deny the one place unit 4 tells every agent to write.

The whole of `os.tmpdir()` is NOT added as a root. That would allow every `/tmp` write on a POSIX
host with no `TMPDIR`, which is exactly the population the ruling denies.

### Rule 3 — `posix-root`

`checkPosixRootLitter(resolved)` matches `^/([^/]+)(/.*)?$` on the comparable form, returns false
when the captured `<top>` is a single character (a drive spelled without its trailing slash, such
as `/c`, which is the drive rule's business), and otherwise returns whether `<top>` is absent from
`POSIX_ROOT_CONVENTIONAL`, a new `Set` beside `DRIVE_ROOT_CONVENTIONAL` at `:290` holding, in
lower case: `dev proc sys usr etc var opt home root mnt media srv bin sbin lib lib64 run boot
private volumes cygdrive workspace workspaces`. Hand-listed for the reason the drive set's header
gives: this is a fact about how filesystems are conventionally laid out, not about this machine,
so there is nothing to derive it from. `tmp` and `temp` are absent on purpose, so a `/tmp` target
that somehow escaped rule 2 is still litter here, and the two rules cannot disagree.

The measured population this rule exists for is four targets in 55,231 real Bash calls on node
`a`, `/mir` and `/xj` among them, every one agent throwaway. That figure is PINNED, measured
2026-09-14 by the run that wrote the spec briefs, using the hook's own `scanWriteTargets` over
the session logs; the same probe counted 72 `$TMPDIR`-rooted, 143 `$TEMP`-rooted and 3,803
`/tmp`-rooted write targets, which are rules 1 and 2's populations.

### The messages

`renderDeny` keeps its two sentences and adds three, one per kind, chosen the way the drive
sentence is chosen today:

- `empty-var`: names the variable, says it is empty in this session, and says the write therefore
  lands at the filesystem root. Remedy: the session scratchpad, spelled absolute.
- `tmp`: says `/tmp` is not a sanctioned destination on this machine and names the scratchpad
  and the temp root as the two that are. On a Git-Bash host this is the honest message even though
  the bytes would have landed under TEMP, because the habit the owner is ending is the spelling.
- `posix-root`: says the target creates a new top-level entry at the POSIX root, names the fix for
  a real conventional root by naming `POSIX_ROOT_CONVENTIONAL`, exactly as the drive sentence
  names its set.

The `BLOCKED by scratch-guard` prefix, the offending-target lines and the resolved-roots list are
unchanged, so the three existing message arms in the suite hold.

### The self-test

`run()` at `tools/hooks/scratch-guard.test.sh:35` pins `TMPDIR=` empty and `TEMP`/`TMP` to the
fixture path for every arm, so a `$TMPDIR` arm already runs with the variable empty and a `$TEMP`
arm already runs with it set. The ALLOW side of rule 1 needs a non-empty `TMPDIR`, and the
`$TEMP`-empty denial needs `TEMP` unset, so `run()` gains one optional fifth argument: words
handed to `env` between the fixed assignments and `node`, such as `-u TEMP` or
`TMPDIR=C:/Users/FIXTUR~1/AppData/Local/Temp`. No new shell function, so the lexicon leg's
`sh.function` population is unchanged.

The `<os.tmpdir()>/claude` arm DERIVES its path rather than pinning one: the suite reads
`node -e` `os.tmpdir()` under the same fixture environment and writes to `<that>/claude/x`. Under
`run()`'s fixed `TEMP`, that resolves to the fixture TEMP on every host, so the arm proves the new
root only where the derived tmpdir is `/tmp`, which is a POSIX host with the three variables
unset; the arm SAYS so in its label rather than passing quietly. Its discriminating twin is a
`/tmp/claude/x` target under the fixture environment, where the derived tmpdir is NOT `/tmp`: that
one is denied, which proves the exception is keyed on `os.tmpdir()` and not on the literal `/tmp`.

Two existing arms flip under the ruling and are re-targeted, not deleted, because each guards a
behaviour that still matters. `near-miss: /tmp is a real root -> allow` at `:110` becomes the rule
2 denial and its near-miss moves to a target under the fixture TEMP. `cp home-rooted SOURCE ->
allow` at `:97` and its `mv` twin at `:99` write to `/tmp/inv/`; their destination becomes a
repo-relative path so they keep proving that a home-rooted SOURCE is a read.

### Inventory

| Identifier | Kind | Cell | Note |
|---|---|---|---|
| `checkEmptyTempVar` | function | `js.function`, camel | `--suggest` answered OK on 2026-09-14 |
| `checkTmpRoot` | function | `js.function`, camel | `--suggest` answered OK on 2026-09-14 |
| `checkPosixRootLitter` | function | `js.function`, camel | `--suggest` answered OK on 2026-09-14 |
| `POSIX_ROOT_CONVENTIONAL` | const `Set` | none graded | sibling of `DRIVE_ROOT_CONVENTIONAL` |
| `empty-var` · `tmp` · `posix-root` | `kind` values | none | join `home` and `drive-root` |

### Files touched (estimate)

- `tools/hooks/scratch-guard.js` — the three predicates, the root, the expansion, the sentences,
  the header's WHAT IT DENIES paragraph.
- `tools/hooks/scratch-guard.test.sh` — the arms in section 6, the `run()` fifth argument, the two
  re-targeted arms, `FLOOR_ASSERTIONS`.
- `tools/hooks/README.md` — the `scratch-guard` section.
- `memory/map/generated/symbols.json` — re-rendered by `python tools/codebase-map/gen_map.py --write`.

### Alternatives rejected

- **Deny every absolute write outside the repo, the scratch roots and home.** Measured wrong
  before this unit existed: 2,449 distinct targets over 128,568 calls, recorded in the hook's own
  `checkDriveRootLitter` header. Rules 2 and 3 are the narrow shape that survived measurement.
- **Treat `/tmp` as allowed on a Git-Bash host, where it maps onto TEMP.** The owner ruled the
  denial on 2026-09-14 and the reason is the habit, not the bytes; section 8 F1.
- **Resolve the variable by spawning a shell.** A hook that spawns a shell per tool call to read
  what a textual rule cannot is the tokenizer upgrade the header names, taken by the back door.
  Rule 1 reads `process.env`, which is the same environment the tool call inherits.

## 5. Production-readiness checklist

- security — a hygiene guard, fail-open on unparseable input as today; it widens what is denied
  and narrows nothing. The new allowed root is derived from `os.tmpdir()`, never authored.
- perf / scale — one `os.tmpdir()` call and three regex tests per write target, on a hook that
  already runs on every Bash and PowerShell call; no file system access beyond the existing
  `realpathSync` on the roots.
- error / empty / loading states — no home resolvable keeps today's degraded branch; no temp
  variable at all makes `os.tmpdir()` the platform fallback, which is the case rule 2's exception
  exists for.
- observability — every denial names its kind in its own sentence, and the resolved-roots list
  now shows the scratchpad base, so a denied agent can see the destination the hook accepts.
- risks — a POSIX host whose `/tmp` habit is legitimate is denied by ruling; a same-command shell
  assignment is exempted textually and stated. Both are in the README section.
- testing — section 6: eight red-first denials, seven allow controls, three message assertions,
  the floor raised by the arms added.
- migration — N/A. No record shape or wiring changes; the hook's stdin protocol is unchanged.
- user docs — `tools/hooks/README.md` gains the section S6 names; the agent-cap dossier under the
  map already claims `tools/hooks/*` and is not edited for a rule its README states.

## 6. Acceptance criteria

The observation for AC1 to AC9 is one hook invocation each, the body of `run()` lifted out of the
suite: the JSON payload built by the same Python one-liner, piped into `node tools/hooks/scratch-guard.js`
under the fixture environment `HOME=/c/Users/fixtureuser`, `USERPROFILE`, `TEMP` and `TMP` at the
fixture values and `TMPDIR` empty, with the exit status read. The whole suite is `--close`'s. The
RED-first observation for each denial is the same invocation against the hook at base
`1b000d1a`, where every command below exits 0; measured 2026-09-14 on node `a` for all six shapes
named in AC1 to AC4, and quoted in the acceptance ledger.

- **AC1** — When the fixture command `cp x $TMPDIR/y` is graded with `TMPDIR` empty, the hook
  exits 2 and its stderr names `TMPDIR` and says the write lands at the filesystem root; the same
  command with `TMPDIR` set to the fixture TEMP through `run()`'s fifth argument exits 0.
  Red when: the base hook is used, which exits 0 on both; or the expansion half is missing, so the
  non-empty case is denied as an unresolved token by no rule and passes for the wrong reason,
  which the paired allow arm cannot tell apart from a correct expansion unless its target is under
  a root — so the allow arm's target is under the fixture TEMP by construction.
- **AC2** — When `echo x > ${TEMP}/y` is graded with `TEMP` unset through `-u TEMP`, the hook
  exits 2 naming `TEMP`; when `echo x > $TEMP/a.log` is graded with the fixture `TEMP` set, it
  exits 0 because the expansion resolves under the TEMP root.
  Red when: the braced spelling is not matched, or `$TEMP` is not expanded and the set case is
  denied.
- **AC3** — When `echo x > /tmp/hyg` is graded, the hook exits 2 and its stderr names the
  scratchpad as the destination; when `echo x > /tmpx/hyg` is graded, it exits 0.
  Red when: the base hook is used, which exits 0 on the first; or the prefix test is a bare
  `startsWith('/tmp')`, which denies the second.
- **AC4** — When `mkdir -p /mir/x` is graded, the hook exits 2 and its stderr names
  `POSIX_ROOT_CONVENTIONAL`; when `echo x > /dev/null`, `echo x > /c/projects/x` and
  `mkdir -p /usr/local/x` are graded, each exits 0.
  Red when: the base hook is used, which exits 0 on the first; or a conventional name is missing
  from the set and one of the three controls is denied; or the single-character guard is missing
  and a `/c` spelling is graded here instead of by the drive rule.
- **AC5** — When `TMP=$(mktemp -d); echo x > $TMP/f` is graded with `TMP` unset through `-u TMP`,
  the hook exits 0.
  Red when: rule 1 ignores the same-command assignment and denies a shell-local variable the
  hook's environment cannot see.
- **AC6** — When `echo x > /tmp/claude/x` is graded under the fixture environment, whose derived
  tmpdir is the fixture TEMP and not `/tmp`, the hook exits 2 with the `tmp` sentence.
  Red when: the exception is keyed on the literal `/tmp/claude` rather than on `os.tmpdir()`, so
  this passes.
- **AC7** — When the suite derives `os.tmpdir()` under the fixture environment with all three
  temp variables unset and grades `echo x > <that>/claude/x` under that same environment, the hook
  exits 0, and the arm's label states that it discriminates only where the derived path is `/tmp`.
  Red when: the new root is absent and the arm is denied on a POSIX host; or the arm pins a path
  instead of deriving one, which makes it a fixture that grades a different machine.
  fixture: the machine's own `os.tmpdir()` under an emptied environment; on node `a` that is
  `C:\Windows\temp`, which is under a conventional drive root and allowed by the existing rule,
  so on this node the arm is a control and not a proof. It is named as such in its label.
- **AC8** — When `echo x > ${TMPDIR:-/tmp}/y` is graded with `TMPDIR` empty, the hook exits 2
  with the `tmp` sentence, because the default expanded and rule 2 read the result.
  Red when: the default form is left unexpanded and no rule claims it.
- **AC9** — When the deny stderr for AC1, AC3 and AC4 is read, each carries the
  `BLOCKED by scratch-guard` prefix, quotes the offending target, and lists at least one resolved
  writable root, so the three existing message arms in the suite still hold on the new kinds.
  Red when: a new kind's sentence replaces the shared prefix or drops the roots list.
- **AC10** — When `bash tools/hooks/scratch-guard.test.sh` runs at the landed tip, it prints
  `PASS` and no `FAIL` line, and `FLOOR_ASSERTIONS` at `tools/hooks/scratch-guard.test.sh:239`
  stands exactly the number of added arms above its base value of 60; at base the same suite
  prints `FAIL` for every arm AC1 to AC4, AC6 and AC8 add, which is the red-first observation of
  the arms themselves.
  Red when: any arm prints `FAIL` at the tip; or the floor did not move, so a stranded arm is
  invisible; or the two re-targeted arms still write under /tmp, in which case the suite is red
  at the tip on arms this unit did not intend to fail.
  cost: the whole suite, which is `--close`'s; the per-arm invocation above is the pass's check.
  permission: the leg `scratch-guard self-test` is chunk `selftests`, held on a default bar; the
  close runs it under `GATE_SELFTESTS=1` or by the direct invocation, once.
  figure: the added-arm count is DERIVED at observation time from the suite's own `---- N passed`
  line at base and at the tip; the floor is then PINNED at base plus that count.
- **AC11** — When `grep -c 'scratch-guard' tools/hooks/README.md` runs at the landed tip, it
  prints a number above 0, and the section it counts names all five rules and the four things
  the predicate does not catch: variable indirection beyond the four temp spellings, `cd`, a
  heredoc'd script, and a PowerShell `$env:` spelling. At base the same `grep -c` prints 0.
  Red when: the README still documents `agent-cap` alone, or the section states the rules and
  omits what they miss.
- **AC12** — When `python tools/codebase-map/gen_map.py --check` runs at the landed tip, it exits
  0; at the tip with the regenerated `memory/map/generated/symbols.json` reverted to base, it
  exits 1 naming that file.
  Red when: the symbols artifact was not re-rendered in the commit that added the three
  functions.

## 7. Gates

`scratch-guard self-test` · `codebase-map coverage + freshness` · `lexicon naming predicates` · `hook destinations (every declared hook path ships)` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

These are the legs `--close` runs, not what the pass runs: the pass verifies with the one hook
invocation that exercises each arm, section 6's preamble, and nothing else. From
`tools/gate-legs.json` at base: `scratch-guard self-test` is chunk `selftests`, subject `kit`,
guarded on `tools/hooks/`, so it is held on a default bar and owed once at the close under
`GATE_SELFTESTS=1`; `codebase-map coverage + freshness` is chunk `declarations`, unguarded, and
is AC12's observation; `lexicon naming predicates` is chunk `declarations`, guarded on `tools/`,
and grades the three new function names against the `js.function` cell; `hook destinations` is
chunk `product`, unguarded, and holds because no hook path moves; `memory hygiene` and
`spec tokens` grade this file.

New arm: `tools/hooks/scratch-guard.test.sh` · each denial arm against the hook at base, which
exits 0 on every one of them · `FLOOR_ASSERTIONS` rises by the arms added.

## 8. Open questions

- **F1 — is `/tmp` denied on a host where Git-Bash maps it onto the allowed TEMP root?** On
  node `a`, `cygpath -w /tmp` prints the TEMP path, so the 3,803 measured `/tmp` writes landed
  inside a sanctioned root and denying them costs a re-spelling on every one. Options: deny `/tmp`
  everywhere, the habit being what the owner is ending; deny it only where `os.tmpdir()` is not
  what `/tmp` resolves to, which needs a probe the hook does not have; leave `/tmp` allowed and
  deny only the empty-variable and root-litter shapes. Recommendation: deny everywhere, with the
  scratchpad base kept allowed inside the prefix.
  RESOLVED (owner, 2026-09-14): deny `/tmp`, beside the empty-variable and root-litter denials;
  the CLI's own scratch base under the temp root stays allowed. Recorded in the run mandate's
  owner-turn table, `memory/builds/aProbedUnit/prompts/2026-09-14-prompt-TOOL-aProbedUnit-1-0-run-mandate.md`,
  and in the build README's build-level rules.

## 9. Revision log

- rev-1 · 2026-09-14 · initial draft.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "deny a write target whose temp variable is empty or that lands under /tmp or at the filesystem root"`,
run 2026-09-14 at this worktree, reported `scan coverage: 71 files scanned | 0 parse skips |
unscanned layers: .sh` and ranked Python `write`/`root` symbols from other kits; its only hit in
the hook was `addRoot` at fan-in 0. The map probe therefore names no seam for this subject and the
seam was found by reading the source: `buildResolvedTarget` at `tools/hooks/scratch-guard.js:273`
already expands `~` and `$HOME` and is where the temp spellings expand; `resolveAllowedRoots` at
`:125` is where the scratchpad base joins the derived roots; `checkDriveRootLitter` at `:315` with
`DRIVE_ROOT_CONVENTIONAL` at `:290` is the shape rule 3 copies. The recall query returned
`TOOL-aTetheredScratch-1` and `-2` first, which record why the allowlist is derived and that a
`TMPDIR` retarget was refused because `/tmp` is a `usertemp` mount onto `%TEMP%` on this host; the
gotcha `allowlist-narrower-than-the-root-it-guards`; `TOOL-aScouredKit-35`, the drive-root rule's
spec; and the run mandate's owner-turn table with the `/tmp` ruling. Where a hit was stale: the
gotcha and `-2` describe `/tmp` as sanctioned, which the 2026-09-14 ruling supersedes for the
guard; the derivation rule they state still holds and rule 2's exception follows it.

Recall terms used: `scratch-guard write target home directory drive-root litter allowlist derived TMPDIR TEMP corpus measured deny`
