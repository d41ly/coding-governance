## Verdict: CLEAN WITH FIXES

**Serves:** spec-audit TOOL-aTetheredScratch-1 TOOL-aTetheredScratch-2

M4 spec audit of both units at rev-1, run as a `Workflow` with four lenses — design correctness,
declaration completeness, acceptance rigor, and unit-2 risk. Every finding below was folded into
rev-2 of the named spec, or resolved by the owner. No finding was refuted.

Node `a` · 2026-08-20 · base `56b945cb` · 4/4 lenses returned · 32 findings, 6 blocker-class.

## The six that would have shipped a broken unit

**B1 — the allowlist denied the destination the hook recommends.** Raised independently by two lenses.
On Windows `TEMP` is `C:\Users\DAILY-~1\AppData\Local\Temp` and the session scratchpad is a subtree of
it, so both sit *inside* `$HOME`. Unit 1 rev-1 allowlisted only `<home>/.claude/`. Measured over
23,966 historical Bash tool calls in `~/.claude/projects/*/*.jsonl`: the rev-1 predicate denied 123
commands, **73 of them legitimate** `%TEMP%`/scratchpad writes, including
`export TMPDIR=/c/Users/daily-agent/AppData/Local/Temp/claude/gatetmp` — verbatim the workaround
`memory/guides/SESSION-KICKOFF.md:225-226` prescribes, and the one unit 1's own bar run needs.
Folded: `resolveAllowedRoots()` derives the allowlist from `TMPDIR`, `TEMP`, `TMP` plus
`<home>/.claude/` at hook start (spec-1 §4, AC2).

**B2 — no string handling, so the guard denies its own prose.** Rev-1 scanned raw command text. The
literal `> ~/.merge-bar.log` appears in this build's README, in spec-1, and in its commit messages, so
`git commit -m "…"` and every heredoc quoting the shape would have been blocked. The sibling already
solved it at `tools/hooks/agent-cap.js:65-72` (`stripStrings`) and rev-1 copied the deny protocol from
that file while dropping this. Folded: `buildCommandView()` blanks quoted strings and heredoc bodies
first (spec-1 §4, AC4).

**B3 — the lexicon pin is shrink-only and a new `.js` lands twice.** `.lexicon.conf:23` declares `js` a
live probe language, `:87` pins `VERB_OFFENDER_PIN="463"`, and the waiver file is empty. Measured:
`tools/hooks/agent-cap.js` contributes 16 verb offenders and `.claude/hooks/agent-cap.js` 16 more, so
a new hook in two copies would red `lexicon naming predicates`. Folded: every function in the new hook
leads with a declared `VERBS` token (spec-1 §5, AC11), with a waiver row named as the fallback in §8.

**B4 — a watched pathspec edited with no re-stamp.** `memory/guides/SESSION-KICKOFF.md:6` watches
`tools/gate-legs.json`, which unit 1 edits to add its leg. Rev-1 put the `last-audit` re-stamp in unit
2 only, while asserting unit 1 lands independently — so unit 1 alone would have red the
`kickoff-manifest ratchet`. Folded: the re-stamp is unit 1's (spec-1 §2, AC12).

**B5 — the false-positive probe could not find anything.** Rev-1's AC5 population was tracked `*.sh`
files and `tools/gate-legs.json` argv strings. Measured: `grep -c '>' tools/gate-legs.json` → 0 (legs
are argv vectors exec'd with no shell, as rev-1's own spec-2 §3 states), and
`git grep -nE '(>>?|2>|&>)[[:space:]]*(~|\$HOME|\$\{HOME\})/' -- '*.sh'` → nothing. The AC written to
catch false positives was itself the `fixture-passes-by-finding-nothing` class. Folded: the population
is now the real corpus of Bash tool-call texts, which is what surfaced B1 (spec-1 AC5).

**B6 — unit 2's root did not exist and its tripwire could not fire.** `/tmp` is an MSYS `usertemp`
mount onto `%TEMP%`, which is under `$HOME`, so no external root was available. Measured:
`TMPDIR="C:/Users/daily-agent/AppData/Local/Temp"` fails 4 arms of `check-template-size.test.sh`
(the gate normalises its key through `cd && pwd` while `mktemp` echoes `TMPDIR` verbatim). And the
abandonment condition rested on `tools/unattended/adopt-unattended.test.sh:137`, which compares `pwd`
against `git rev-parse --show-toplevel` — an MSYS-versus-drive-letter divergence invariant under every
`TMPDIR` value, so it would have passed regardless. Resolved by the owner: the retarget is dropped and
replaced by the root cause.

## Findings folded without ceremony

- Matcher widened to `Bash|PowerShell`; a guard on one shell leaves the act available through the
  other, the hole `agent-cap.js:38-41` records paying for once. `tools/check-wiring.sh:530` ships a
  PowerShell home-directory write in its own remedy string.
- Three `[[files]]` rules, not two — govkit check 7i quantifies per FILE, and the third new file is
  the fragment. An `include = "**"` rule was considered and refused.
- Kit-versus-wired parity arm added (`agent-cap.test.sh:460-467` model). `.claude/**` is outside the
  govkit surface, the codebase-map inventories and both `tools/`-scoped JS gates, so nothing else
  would notice the executed copy drifting from the graded one.
- ACs pinned to the CLASS: one DENY arm per declared home root and write-context family, each with an
  ALLOW near-miss. Rev-1's AC1 would have passed a hook recognising only `~/` with only `>`.
- Fixtures drive `HOME`, `USERPROFILE`, `TMPDIR`, `TEMP`, `TMP` at fixture values —
  `memory/gotchas/fixture-inherits-ambient-machine-state.md:37` names exactly this state, and rev-1
  cited that gotcha in §10 while no AC acted on it.
- Seventh home spelling: the 8.3 contraction. This node reports `USERPROFILE=C:\Users\daily-agent`
  beside `TEMP=C:\Users\DAILY-~1\...`, and the real corpus carries both inside one session.
- `cp`/`mv`/`install`/`rsync` match the LAST argument only. Rev-1 matched any argument, so a
  home-rooted SOURCE was denied — which would have blocked unit 2's own inventory step.
- §7 leg list corrected by measurement: `workflow script syntax` and `verifier fan-out` are
  marker-gated on `export const meta =` and skip a hook file; `settings-merge selftest` runs inside its
  own `TemporaryDirectory()`; the leg whose population actually grows is
  `install-prefix (shipped surface)`, not `install-prefix self-test`.
- "Present rather than skipped" clauses dropped — `run-gates.sh:112` makes them true by construction
  under `GATE_FULL=1`. Replaced by a scoped-run observation of the guard (spec-1 AC13).
- Two of the eighteen swept files are not logs. `.rb-adb.bak` and `.rb-apm.bak` are pre-edit `RUN.md`
  snapshots carrying `phase: LANDING`; recoverable from `d1bc3f3`. Owner: verify against git, record
  the diff, then remove.
- The sweep is by exact name, never by glob — the home directory also holds `.gitconfig`, `.ssh/`,
  `.aws/` and a `.claude.json.tmp.5240.356c33de8f26` that a `~/.*.tmp*` pattern would catch. AC4
  strengthened from eighteen named absences to a whole-directory set comparison.
- Unit 1's independence claim scoped to code rather than acceptance: its bar run needs an ad-hoc
  `TMPDIR` export on this node, and the value used is recorded.

## What the audit cleared

The `TOOL-aBranchedMandate-4` refusal was tested and does **not** bind. Its refused act is defined by
its second clause — turning a leg green "while the adopter stays broken", which "hides a real defect".
That unit's rev-4 landed with 36 assertions and zero skips, so there is no red leg for this build to
buy. Sound distinction, and rev-1 had already guarded it with an AC3 encoding the refused predicate.

Also verified accurate and left alone: the deny/allow protocol description, the six-finding cap, the
`check-playbook-parity.sh:125` PID note, "a leg cannot set an environment variable", the `~/.gov-push`
inventory (45 entries, 4.3 MB, 43 `mrecall-*` repos), and all sixteen acceptance bullets carrying a
backticked witness.

## One finding not folded

The four-break list in unit 2 §4 is presented as closed while `tools/gate-lint/ps-hygiene.py:128,182`
is a fifth filesystem walker. Left as-is: the retarget was dropped, so the list is now historical
reasoning rather than a live constraint, and rewriting a refusal's evidence to be exhaustive about a
path not taken is work with no reader.
