# Spec brief — TOOL-aDeferredBar-3 — the act refusal: a PreToolUse hook in the unattended kit

**Serves:** journal TOOL-aDeferredBar-3

The writer authors `memory/builds/aDeferredBar/spec/2026-09-13-spec-TOOL-aDeferredBar-3.md` at
Tier 2 against `memory/TEMPLATE-SPEC.md`. Read the research record under `build/` whole first;
its section 2 (the corpus) and section 3 (candidate C2, and why C3 lost) are this unit.

## The mechanism, in one sentence

`tools/unattended/gate-guard.js`, a `PreToolUse` hook on matcher `Bash|PowerShell`, DENIES a
command that would run a full merge bar or a self-test suite while the current branch's
unattended run is in a phase before `VERIFYING`; the plain bar passes; everything else passes;
it fails open. Modelled on `tools/hooks/scratch-guard.js` — read that file whole, it is the
precedent for every shape decision below — and wired the way `tools/process-monitor/procmon-hook.js`
is: a `*.fragment.json` beside it, merged by `python tools/settings-merge.py --fragment`.

## The predicate — measured, not reasoned

Denied while the run is before `VERIFYING`, on a STRING-BLANKED view of the command (the sibling
hook's `stripStrings`/`buildCommandView` distinction, so `git commit -m "ran run-gates.sh"` is not
a hit), where the token sits at COMMAND POSITION — line start or after `;`, `&&`, `||`, `|`, `(`,
`then`, `do`, `else` — optionally behind `env`, any `VAR=value` prefixes, `timeout N`, `bash`/`sh`:

- a `GATE_FULL=` or `GATE_SELFTESTS=` assignment prefixing a command, or exported;
- `run-selftests.sh`, `run-unattended-gates.sh`;
- any path ending `.test.sh`.

NOT denied: `run-gates.sh` with neither prefix — the scoped bar the owner allows at the main loop;
`node <hook>.js` fed a fixture on stdin, which is how THIS unit observes itself; `--list`,
`--check`, `--help` forms of the runners if the spec finds they cost seconds (measure — do not
assume). Section 5 carries the deny message: what was matched, the phase and the run-state file
that keyed it, and the substitute (the direct check; the bar at `VERIFYING`, by the main loop).

**Measure the shipped predicate over the corpus before wiring it**, the way `scratch-guard.js`
measured its own: the transcript store is `~/.claude/projects/C--projects-coding-governance*/**/*.jsonl`,
each `Bash`/`PowerShell` `tool_use` carries `input.command`, and the record's `isSidechain` says
whether an agent inside a `Workflow` issued it. The research record's section 2 has a first cut
of this probe and its counts; this unit's §6 reports HITS and NEAR-MISSES of the final predicate
over that same corpus, and the near-miss list is what proves the blanked view earns its keep.

## The key — which run, which phase — and what it must NOT read

From the hook's stdin `cwd`, resolve the repository root; read `.unattended.conf` there for
`MEMORY_ROOT` (the kit's own project layer, and the one path the kit may spell); read
`<root>/<MEMORY_ROOT>/builds/*/RUN.md`; take the record whose `branch-ref:` equals the current
`HEAD` ref, read from the `.git` file-or-directory's `HEAD` without spawning git; read its
`phase:`. **A run-state file for ANOTHER branch keys nothing** — two stale `BUILDING` records
sit on `main` today (`aUnblockedFleet`, `aClosedDocket`) and a hook keyed on "any record is
BUILDING" would deny every session forever. No matching record → allow. Unreadable anything →
allow. Phase in `VERIFYING`, `LANDING`, `LANDED`, `ABORTED` → allow: the owed `GATE_SELFTESTS=1`
bar for kit work, the close's own bar and the lander all happen there. Any other phase, including
a project's `PHASES_EXTRA` member, → the deny set applies.

The four allowed names are spelled in the hook as the TAIL of the driver's `PHASES_CORE`
(`tools/unattended/unattended.sh`), with the comment saying so — `lib-unattended.sh` already
spells phase names in a `case` at its line 405, and `check-unattended.sh` refuses a RESTATED SET
(its lines 374–390), not a literal. FACT-QUESTION for §8: *does `check-unattended.sh` red a kit
file carrying those four literals?* Probe: `bash tools/unattended/check-unattended.sh` over the
tree with the hook present — a READ of the checker's verdict, seconds. Liveness: the same checker
reds on a `PHASES_CORE` restatement, which the spec cites from its own test.

## Why it is the unattended kit's file and not the hooks kit's

The key is the run-state record, whose layout and conf key belong to this kit; a hook in
`tools/hooks/` reading `.unattended.conf` and `builds/*/RUN.md` would name a sibling kit's
record by literal, which `tools/hooks/README.md` bans and a merge-bar leg grades. Two kits
already ship their own hooks this way (`memory-recall`, `process-monitor`).

## The write set (section 4 files table)

1. `tools/unattended/gate-guard.js` — the hook. Function names from the declared verb table
   (`.lexicon.conf`, cell `js.function camel`): `check…`, `read…`, `build…`, `resolve…`,
   `render…` as `scratch-guard.js` uses them. No `tools/` literal; the conf key and the record
   basename are the only spellings.
2. `tools/unattended/gate-guard.fragment.json` — `{name, event: "PreToolUse", matcher:
   "Bash|PowerShell", marker: "gate-guard.js", hook_path: "{kit}/unattended/gate-guard.js"}`,
   the shape `procmon-hook.fragment.json` has. `hook destinations` quantifies over tracked
   fragments, so this is what makes the hook gradeable at all.
3. `.claude/settings.json` — wired by `python tools/settings-merge.py --fragment
   tools/unattended/gate-guard.fragment.json`, never by hand. Settings are hot-reloaded
   mid-session (`TOOL-cRefutedPremise-1`): the hook is LIVE the moment this file lands, including
   for the pass that lands it.
4. `tools/unattended/gate-guard.test.sh` — WITHHELD from the bar like its five siblings: added to
   the `project-owned` include list in `tools/unattended/kit.toml`, and a budget row in
   `tools/run-gates/selftest-budgets.txt` so `run-unattended-gates.sh` enumerates it. Arms: each
   deny shape denied with `phase: BUILDING`; the plain bar allowed; every shape allowed at
   `VERIFYING`; a record on another branch keys nothing; no record → allow; unparseable stdin →
   exit 0; a quoted mention → allow. Fixtures build a scratch repo under `mktemp -d` with a `.git`
   `HEAD`, a conf and a record — never the real tree.
5. `tools/unattended/kit.toml` — the withheld-suite row; the `**` engine rule already ships the
   hook and the fragment.
6. `tools/unattended/adopt-unattended.sh` — the `--check` arm that reports the hook UNWIRED when
   the fragment's marker is absent from the settings file, in `adopt-process-monitor.sh`'s
   `add_problem` register, naming the `settings-merge.py --fragment` remedy.
7. `tools/unattended/README.md` and `tools/unattended/SKILL.template.md` — the paragraph and the
   half-sentence saying the act is refused, not only forbidden; `KIT_UNATTENDED_VERSION` and the
   render markers move one step past where unit 1 left them.
8. `memory/map/features/unattended.md` — prose refresh on touch; no new inventory key is claimed
   unless the spec adds a leg, which it does not.

NOT in the write set: `tools/check-wiring.sh` (the `hook destinations` leg and the adopter's
`--check` arm cover the wiring; a check-wiring arm is a follow-up backlog row, say so in §3);
`tools/hooks/*`; any phase-vocabulary change.

## The acceptance criteria — this unit is observed by the hook, never by a suite

`printf '<json>' | node tools/unattended/gate-guard.js; echo $?` with a fixture stdin naming a
scratch `cwd` is the observation for every arm — exit 2 and the deny text on stderr for a hit,
exit 0 and silence for an allow. Its OWN failing case, observed RED before it lands: a fixture
`RUN.md` at `phase: BUILDING` on the fixture's branch and the command
`GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh` → denied. Then `bash
tools/check-hook-destinations.sh`, `python tools/settings-merge.py --check`, `bash
tools/unattended/adopt-unattended.sh --check`, `bash tools/check-kit-versions.sh`, and
`python tools/codebase-map/test_codebase_map.py` — each direct, each seconds. NOT ONE criterion
names the bar, a `GATE_*=` prefix or a `*.test.sh` suite as its observation; once this hook is
wired, such a criterion could not be observed by the pass that builds it.

§7 leg line: `hook destinations (every declared hook path ships)` · `unattended skill wiring`
· `unattended kit gate` · `kit version markers` · `verdict epoch (kit version dates the engine)`
· `codebase-map coverage + freshness` · `lexicon naming predicates` · `install-prefix (shipped
surface)` — resolve every name with `python tools/check-spec-tokens.py --list` and drop what does
not resolve. `New arm: tools/unattended/gate-guard.test.sh · a fixture record at BUILDING and the
flagged bar · none`.

## Resolved forks — mark RESOLVED (agent, 2026-09-13, delegated)

- **Hooks kit vs unattended kit as the home** → unattended, for the literal-ban reason above.
- **Key on the phase vs deny whenever a record exists** → the phase, because the main loop owes a
  full bar at `VERIFYING` and a hook that denied it would be bypassed or disabled within a day.
- **Deny the plain bar too** → no; it is the scoped form the owner allows, and the child prompt
  (unit 1) forbids it by instruction where the hook cannot tell a child from the main loop.
- **`*.test.sh` broadly vs the unattended suites only** → broadly; the ledger's three most
  expensive suites are other kits'.
