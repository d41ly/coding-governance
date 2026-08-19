# TOOL-aTetheredScratch-1 — a PreToolUse guard that denies a home-directory write outside the sanctioned scratch roots

**Status:** SPECCED · rev-2 · 2026-08-20 · node a · Tier-2 · base 56b945cb · streams tooling

The reported defect is agent-authored, not code-authored: eighteen files in the operator's home
directory, written by tool calls of the shape `... > ~/.merge-bar.log 2>&1`. No script is involved, so
no script can catch it, and the charter rule it violates was already loaded in the sessions that
violated it. The only surface that sees the offending bytes is the tool call.

## 1. Goal

Deny, at the tool call, any shell command whose text names a write target under the operator's home
directory that is not one of the sanctioned scratch roots. The deny must name the offending fragment
and the roots that would have been allowed, so the refusal is satisfiable without reading this spec.

The owner stated the rule as "temporary files go to scratchpad/temp and nowhere else". That sentence
is the allowlist, and §4 implements it literally rather than approximating it.

## 2. Scope (IN)

- `tools/hooks/scratch-guard.js` — the hook. Every function name leads with a `.lexicon.conf` `VERBS`
  token, so the file adds zero verb offenders to a shrink-only pin.
- `tools/hooks/scratch-guard.test.sh` — the self-test, printing `PASS (<n> assertions)` and pinning a
  non-zero `FLOOR_ASSERTIONS`, so `tools/check-testsuite-counts.sh` grades it without a waiver row.
- `tools/hooks/scratch-guard.fragment.json` — the settings fragment consumed by
  `tools/settings-merge.py --fragment`.
- `.claude/hooks/scratch-guard.js` — the wired copy, plus the matcher group appended to
  `.claude/settings.json` by `settings-merge.py`.
- `tools/hooks/kit.toml` — **three** new `[[files]]` rules, one per new tracked file, because govkit
  check 7i quantifies per FILE and this entry's includes are literal lists. `scratch-guard.js` carries
  the two-destination `to` list. `KIT_AGENT_CAP_VERSION` and its same-line `gov:kit agent-cap@` marker
  bumped together, which is the pair `tools/check-kit-versions.sh:46-50` actually asserts.
- `tools/gate-legs.json` — the leg `scratch-guard self-test`, guarded on `tools/hooks/` and `tools/lib/`.
- `memory/guides/SESSION-KICKOFF.md` — `tools/gate-legs.json` is a WATCHED pathspec, so the
  `last-audit` re-stamp and its delta line are this unit's, not unit 2's.
- `tools/check-wiring.sh` — a `scratch-guard` arm reading the fragment, modelled on the `recall` arm.
  Arms added to `tools/check-wiring.test.sh`.
- `memory/map/features/agent-cap.md` — the new leg name claimed under `gate-legs`, with
  `memory/map/generated/` regenerated in the same commit.

## 3. Non-goals (OUT)

- **Parsing shell.** The predicate scans a string-blanked view for literal write shapes. It builds no
  AST, resolves no variable, and follows no `cd`. The ceiling is named in §5 and in the file header.
- **Guarding anything outside the operator's home.** Writes into the repo or onto another volume are
  not this unit's subject.
- **`TMPDIR` retargeting and the litter sweep.** Both are `TOOL-aTetheredScratch-2`.
- **Fixing `TOOL-aBranchedMandate-6`.** The `mrecall-*` leak has its own OPEN row.
- **A second kit version constant.** `version_from` is entry-level and single-valued
  (`tools/govkit/govkit.py:321-341`), so a `KIT_SCRATCH_GUARD_VERSION` would be invisible to govkit.

## 4. Design

**The hook contract is copied from its sibling, not reinvented.** `tools/hooks/agent-cap.js` denies by
`process.stderr.write(...)` plus `process.exit(2)` and allows by printing nothing and exiting 0; its
header at `:42` records the choice as "version-robust; no JSON-schema dependency". No source file in
this repo emits `permissionDecision`. The new hook uses the same protocol, the same
`fs.readFileSync(0, 'utf8')` inside a `try`, and the same fail-open exit 0 on a parse failure.

**The matcher is `Bash|PowerShell`, one group, two exact strings.** A guard wired to `Bash` alone
leaves the identical act available through the PowerShell surface — the same one-modality hole
`agent-cap.js:38-41` records paying for, where "`Workflow` alone leaves direct spawns unguarded". That
this fleet really does drive PowerShell at the home directory is in the tree:
`tools/check-wiring.sh:530` ships `New-Item -ItemType Junction -Path "$env:USERPROFILE\.claude\..."`
as its own remedy string.

**The command text is `tool_input.command`**, confirmed against the published PreToolUse payload for
`Bash`. AC0 observes it on this machine before any predicate code is written, because a wrong key
yields a hook that always exits 0 and a suite that is green about it — the charter's "guard that
shares a variable with the thing it guards".

**The scan runs over a command VIEW, not the raw text.** `buildCommandView()` blanks quoted-string
contents and heredoc bodies before anything else looks at it, exactly as `agent-cap.js:65-72`
(`stripStrings`) does and for the same reason. Without it the guard denies any command that merely
QUOTES the bad shape — including this build's own commit messages, which contain
`> ~/.merge-bar.log` verbatim, and any heredoc writing these very specs.

**Home roots recognised**, all compared case-insensitively: `~/`, `$HOME/`, `${HOME}/`, and the
resolved home in four live spellings — `/c/Users/<user>/`, `C:\Users\<user>\`, `C:/Users/<user>/`, and
the 8.3 contraction `C:\Users\<USER~1>\`. The 8.3 form is not hypothetical: this node reports
`USERPROFILE=C:\Users\daily-agent` while `TEMP=C:\Users\DAILY-~1\AppData\Local\Temp`, and the real
corpus carries both spellings inside one session. `resolveHomeRoots()` derives the set from `HOME`,
else `USERPROFILE`; with neither set only the symbolic roots are recognised, and the header says so.

**Write contexts recognised.** A redirect operator (`>`, `>>`, `2>`, `2>>`, `&>`) whose target is a
home root; a home-rooted argument to `tee`, `touch`, `mkdir` or `dd of=`; the **last** argument only
of `cp`, `mv`, `install` or `rsync`, because those take a source first and a home-rooted SOURCE is a
read — which is exactly what unit 2's inventory step does; and a `TMPDIR=`, `TMP=` or `TEMP=`
assignment to a home root outside the allowlist, the shape that produced `~/.gov-push/`.

**The allowlist is DERIVED at hook start, and this is the correction that rev-2 exists for.** On
Windows the scratch roots are *inside* the home directory: `TEMP` is
`C:\Users\DAILY-~1\AppData\Local\Temp` and the session scratchpad is a subtree of it. A hardcoded
`<home>/.claude/` allowlist therefore denies every legitimate temp write. Measured over the real
corpus of 23,966 historical Bash tool calls, the rev-1 predicate denied 123 commands of which **73
were legitimate** `%TEMP%` or scratchpad writes — including `export TMPDIR=…/claude/gatetmp`, which is
verbatim the workaround `memory/guides/SESSION-KICKOFF.md:225-226` prescribes and which unit 1's own
AC9 bar run depends on.

`resolveAllowedRoots()` therefore returns, normalised to every spelling above: the values of `TMPDIR`,
`TEMP` and `TMP` when set; `<home>/.claude/`; and nothing else. A target under any of them is allowed;
a target under a home root and under none of them is denied. That is "scratchpad/temp and nowhere
else", derived rather than authored, and it self-corrects if unit 2 later moves `TMPDIR`.

**Prefix comparison is boundary-aware.** A root matches only at a path separator, so `~/.claudex` and
`~/.claude-scratch` are denied while `~/.claude/x` is allowed.

**The deny message.** Prefix `BLOCKED by scratch-guard: `, the offending fragment quoted, then the
resolved allowlist printed as the remedy — the roots are derived, so the message names the real ones
rather than a guess. Findings capped at six, as `agent-cap.js:737` caps them.

**Why an arm in `check-wiring.sh` and not only a leg.** The leg proves the hook's logic and cannot
prove it is WIRED, and an unwired hook is silent in exactly the way a correct one is. The `recall` arm
at `tools/check-wiring.sh:161-197` already reads marker, matcher and hook path from a shipped
fragment; the new arm is that arm with a different fragment.

**Why the wiring rides `settings-merge.py`.** `.claude/settings.json` is owned as a govkit destination
by the `settings-merge` entry, and check 4 reds when two entries write one destination. `merge()` at
`:91-111` looks its group up by exact matcher equality and appends on a miss, so the new group lands
beside `Workflow|Agent` untouched and re-running is a structural no-op.

## 5. Production-readiness checklist

- **Security** — a deny-only guard. It reads stdin, writes stderr, exits; it executes nothing from the
  payload and opens no file. A command it cannot parse is ALLOWED, which is right for a hygiene rule
  and wrong for a containment boundary. This is tidiness, not containment, and that is written here so
  nobody later mistakes it for the latter.
- **The named ceiling** — the predicate is textual. It does not catch `cd ~ && echo x > y`, a path
  held in a variable, or a home-rooted write inside a heredoc'd python script. It catches the literal
  shapes that produced every one of the eighteen observed files. Stated in the hook header as a
  `ponytail:` comment naming the upgrade path, so the limit is discoverable at the code.
- **Ambient state** — `memory/gotchas/fixture-inherits-ambient-machine-state.md:37` names `$HOME` and
  `TMPDIR` as state a fixture inherits without saying so. Every arm therefore invokes the hook with
  `HOME`, `USERPROFILE`, `TMPDIR`, `TEMP` and `TMP` set to fixture values, so the suite measures the
  same thing on nodes `b`, `c` and `d` instead of passing green because their homes differ.
- **Lexicon** — `.lexicon.conf:23` declares `js` a live probe language and `:87` pins
  `VERB_OFFENDER_PIN="463"` shrink-only, with an empty waiver file. Measured: `agent-cap.js`
  contributes 16 offenders and its wired mirror 16 more. Every function in the new hook therefore
  leads with a `VERBS` token — `build`, `read`, `resolve`, `scan`, `check`, `render`, `main` — so the
  pin does not move and no waiver row is needed.
- **Perf** — one pass over one command string per call, no filesystem access, no subprocess.
- **False positives** — the risk that matters, and the one rev-1 got wrong. §6 measures it over the
  real corpus rather than over a population chosen for convenience.
- **Observability** — the deny text is the whole diagnostic. A hook that wrote a log would be writing
  scratch.
- **Rollback** — delete the group from `.claude/settings.json`; `check-wiring.sh` then reports UNWIRED
  rather than going quiet.
- **a11y / i18n / migration** — N/A for a hook.
- **Testing** — the payload-builder liveness guard from `agent-cap.test.sh:31-33`, without which every
  ALLOW arm passes for the wrong reason; plus the kit-versus-wired parity arm modelled on
  `agent-cap.test.sh:460-467`, because `.claude/**` is outside the govkit surface, outside the
  codebase-map inventories and outside both `tools/`-scoped JS gates — nothing else would notice the
  executed copy drifting from the graded one.

## 6. Acceptance criteria

- **AC0** — The payload key is OBSERVED before any predicate code exists: a throwaway `PreToolUse`
  hook writes raw stdin to a file, one Bash call is made, and the captured JSON shows
  `tool_input.command`. The transcript line goes in the build record. Run FIRST.
- **AC1** — The failing case is observed: `echo x > ~/.litter` fed to `tools/hooks/scratch-guard.js`
  exits `2` with stderr matching `BLOCKED by scratch-guard`.
- **AC2** — The ALLOW half is equally observed, and covers the collision rev-1 missed: each of
  `echo x > ~/.claude/settings.json`, a write to `$TEMP/x.log`, a write into the session scratchpad,
  and `export TMPDIR=$TEMP/gatetmp` exits `0` with empty stderr.
- **AC3** — The arm set spans the CLASS, not one instance: one DENY arm per declared home root
  (all seven spellings) and per write-context family, each paired with an ALLOW near-miss — `>` to a
  repo path, `cp` between repo paths, `cp ~/.merge-bar.log /c/scratch/` (home-rooted SOURCE),
  `TMPDIR=` to a sanctioned root, and the boundary pair `~/.claudex` DENY versus `~/.claude/x` ALLOW.
  `FLOOR_ASSERTIONS` equals that derived count.
- **AC4** — Quoting does not trigger the guard: `git commit -m "fixes the > ~/.merge-bar.log litter"`
  and a heredoc whose body contains the shape both exit `0`.
- **AC5** — False-positive probe over the REAL corpus: the predicate is run over every Bash command in
  `~/.claude/projects/*/*.jsonl` (23,966 on node `a`), hits and near-misses printed and recorded. It
  must flag the `> "$HOME/.merge-bar.log"` family and must return **zero** denies on `%TEMP%` or
  scratchpad writes. This population is what surfaced the rev-1 allowlist defect; the rev-1 population
  was structurally empty and could not have.
- **AC6** — The payload-builder liveness guard fires: with the builder in a scratch copy of
  `tools/hooks/scratch-guard.test.sh` stubbed to emit an empty payload, the suite FAILS and names the
  builder rather than an arm.
- **AC7** — The kit-versus-wired parity arm fires both ways: with `.claude/hooks/scratch-guard.js`
  absent the suite FAILS saying parity must not be satisfiable by absence, and with it drifted by one
  byte the suite FAILS naming the drift.
- **AC8** — Every arm runs with `HOME`, `USERPROFILE`, `TMPDIR`, `TEMP` and `TMP` driven at fixture
  values, and one arm covers the degraded branch: with `HOME` and `USERPROFILE` both unset the
  symbolic roots still deny.
- **AC9** — `bash tools/check-wiring.sh --check` prints `ok       scratch-guard` when the group is
  present and `UNWIRED  scratch-guard` naming the fragment's matcher when absent, both observed with
  the padded prefix bytes asserted as the existing arm tests assert them.
- **AC10** — `python tools/govkit/govkit.py selfcheck` exits 0: no "under its home and no file rule
  claims it" line for any of the three new files, and no "claimed by no descriptor" line for the leg.
- **AC11** — `python tools/lexicon/lexicon.py` reports no new verb offender, with the pin
  `VERB_OFFENDER_PIN` unmoved at its current value.
- **AC12** — `bash skills/session-kickoff/manifest-check.sh` exits 0 after the `last-audit` re-stamp,
  with the delta line in the commit message.
- **AC13** — The guard's own leg is guarded correctly, observed on a scoped run rather than under
  `GATE_FULL=1` where no leg can skip: with only a `memory/` file changed the leg reports
  `GATE skip  scratch-guard self-test`, and with `tools/hooks/scratch-guard.js` changed it runs.
- **AC14** — The full bar is GREEN: `GATE_FULL=1 bash tools/run-gates/run-gates.sh`, reporting a leg
  count equal to the entry count of `tools/gate-legs.json`.

## 7. Gates

`GATE_FULL=1 bash tools/run-gates/run-gates.sh`. The legs this unit can actually red, corrected in
rev-2 after measuring which ones its population reaches: `scratch-guard self-test` (new),
`lexicon naming predicates`, `kickoff-manifest ratchet`, `check-wiring self-test`, `govkit selfcheck`,
`govkit selftest`, `codebase-map coverage + freshness`, `testsuite counts`, `kit version markers`,
`install-prefix (shipped surface)`, `review-join ban`.

Dropped from rev-1 after measurement: `workflow script syntax` and `verifier fan-out` are both
marker-gated on `export const meta =` and skip a hook file; `settings-merge selftest` runs entirely
inside its own `TemporaryDirectory()` and never sees a new fragment on disk;
`install-prefix self-test` was the wrong name for the hermetic harness — the leg whose population
grows is `install-prefix (shipped surface)`.

**Precondition, recorded rather than assumed:** the full bar does not currently finish on node `a`
under the ambient `TMPDIR` (`memory/guides/SESSION-KICKOFF.md:223-226`; measured this session at 6865
entries, 4905 of them `mrecall-*`). AC14 is therefore run with an ad-hoc `TMPDIR` export, and the
value used is recorded in the build record so unit 2's evidence is comparable. The allowlist in §4
derives from `TMPDIR`, so the guard permits that export rather than blocking its own acceptance.

## 8. Open questions

- **RESOLVED — the allowlist is derived, not authored.** Rev-1 hardcoded `<home>/.claude/`, which on
  Windows denies `%TEMP%` and the session scratchpad because both sit under `$HOME`. Measured: 73 of
  123 denies over the real corpus were legitimate. Ratified: derive from `TMPDIR`, `TEMP`, `TMP` plus
  `<home>/.claude/`. Resolver: the rev-1 spec audit, acceptance and unit-2 lenses concurring.
- **RESOLVED — matcher width.** Considered `Bash` alone. Refused: it repeats the one-modality hole
  `agent-cap.js:38-41` records, and the repo ships a PowerShell home-directory write in its own remedy
  string. Ratified: `Bash|PowerShell`. Resolver: the design lens.
- **RESOLVED — where the file lives and under which kit id.** A second govkit entry on `tools/hooks`
  buys nothing: check 7i still quantifies `agent-cap` over the unclaimed file, and check 4 forbids a
  second claim on `.claude/settings.json`. An `include = "**"` rule (the `tools/memory-recall/kit.toml:9`
  shape) was considered and refused — this entry's four existing rules are deliberately one-per-file.
  Ratified: three literal rules in the existing entry. Resolver: the declarations lens.
- **RESOLVED — deny protocol.** stderr plus exit 2, matching the sibling. Two protocols for one act
  would be the two-answers-to-one-question class.
- **OPEN — whether the lexicon-clean naming survives contact with the code.** The design commits every
  function to a `VERBS` token, which the table's own header says is a scoping claim rather than a
  spelling one. If a function genuinely will not fit, the honest response is to split it, not to add a
  verb — but if that proves wrong twice, the fallback is a waiver row keyed on the identifier text,
  which covers both copies at once. Proceeding on the naming, recording the fallback.

## 9. Revision log

- **rev-1** — 2026-08-20 — authored. Grounded on a five-reader recon of `tools/hooks/`, `tools/govkit/`,
  `tools/check-wiring.sh` with `tools/settings-merge.py`, `tools/gate-legs.json` with
  `memory/guides/BUILD-METHOD.md`, and the `TMPDIR` blast radius.
- **rev-2** — 2026-08-20 — the M4 spec audit folded in, four lenses. Five blocker-class corrections:
  the allowlist is derived rather than hardcoded, because `%TEMP%` is inside `$HOME` on Windows and
  rev-1 would have denied 73 legitimate commands out of 123; the scan runs over a string-blanked view,
  because rev-1 denied any command quoting the shape, including this build's own commit messages;
  the lexicon pin is shrink-only and a new `.js` in two copies would have red it; `tools/gate-legs.json`
  is a WATCHED pathspec so the manifest re-stamp is this unit's; and AC5's population was structurally
  empty. Plus the `Bash|PowerShell` widening, three file rules rather than two, the kit-versus-wired
  parity arm, ambient-state fixture pinning, destination-only matching for `cp`/`mv`/`install`/`rsync`,
  the 8.3 home spelling, and a corrected §7 leg list.

## 10. Reuse audit

The seam is `tools/hooks/`, extended rather than duplicated. `tools/hooks/agent-cap.js` supplies the
stdin read, the fail-open parse, the deny protocol, the six-finding cap, the message-prefix convention
and — the rev-2 addition — `stripStrings` at `:65-72`, whose absence was one of the two defects that
would have made the guard unusable on contact. `tools/hooks/agent-cap.test.sh` supplies the harness
shape, the assertion helper, the payload-builder liveness guard at `:31-33` and the kit-versus-wired
parity arm at `:460-467`. `tools/settings-merge.py` already accepts `--fragment` and `--hook-path` and
already appends a new matcher group on an exact-match miss, so no code there changes.
`tools/check-wiring.sh`'s `recall` arm at `:161-197` is the model for a fragment-reading arm, as
against the `agent-cap` arm which hardcodes its matcher.

No existing seam covers the predicate — nothing in this repo inspects shell command text — so that is
the one genuinely new surface, and it is one file.

Recall terms used, recorded so a resuming pass re-runs the same query:
`scratchpad TMPDIR mktemp hermetic scratch repo gate-logs HOME litter temp residue selftest cleanup redirect`.
The probe returned `TOOL-aBranchedMandate-6`, `TOOL-aTimedTurnstile-1`, the `SESSION-KICKOFF.md`
environment trap, and `memory/gotchas/fixture-inherits-ambient-machine-state.md`, the last of which
became §5's ambient-state rule and AC8.
