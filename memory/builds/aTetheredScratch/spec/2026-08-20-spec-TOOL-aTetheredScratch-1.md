# TOOL-aTetheredScratch-1 — a PreToolUse guard on Bash that denies a HOME-rooted write

**Status:** SPECCED · rev-1 · 2026-08-20 · node a · Tier-2 · base 56b945cb · streams tooling

The reported defect is agent-authored, not code-authored: eighteen files in the operator's home
directory, written by `Bash` tool calls of the shape `... > ~/.merge-bar.log 2>&1`. No script is
involved, so no script can catch it, and the charter rule it violates was already loaded in the
sessions that violated it. The only surface that sees the offending bytes is the tool call.

## 1. Goal

Deny, at the `Bash` tool call, any command whose text names a write target rooted at the operator's
home directory outside `~/.claude/`. The deny must name the offending fragment and state the
sanctioned destination, so the refusal is satisfiable without reading this spec.

This is the same enforcement argument that produced `tools/hooks/agent-cap.js`: a rule that binds only
in prose is a rule the next session breaks, and the hook is the one place that observes the act.

## 2. Scope (IN)

- `tools/hooks/scratch-guard.js` — a `PreToolUse` hook, matcher `Bash`, denying by stderr text and
  exit 2, allowing by silence and exit 0. Fails OPEN on unparseable stdin, matching its sibling.
- `tools/hooks/scratch-guard.test.sh` — the self-test, printing `PASS (<n> assertions)` and pinning a
  non-zero `FLOOR_ASSERTIONS`, so it satisfies `tools/check-testsuite-counts.sh` rather than taking a
  waiver row.
- `tools/hooks/scratch-guard.fragment.json` — the settings fragment carrying `name`, `event`,
  `matcher`, `marker`, `hook_path`, consumed by `tools/settings-merge.py --fragment`.
- `.claude/hooks/scratch-guard.js` — the wired copy, and the `Bash` matcher group appended to
  `.claude/settings.json` by `settings-merge.py`.
- `tools/hooks/kit.toml` — two new `[[files]]` rules and one new `[[gate_leg]]`; `KIT_AGENT_CAP_VERSION`
  bumped, since this entry versions the whole `tools/hooks` home.
- `tools/gate-legs.json` — the leg `scratch-guard self-test`, guarded on `tools/hooks/` and `tools/lib/`.
- `tools/check-wiring.sh` — a `scratch-guard` arm reading the fragment, modelled on the existing
  `recall` arm, which is the one arm that already reads marker and matcher from a fragment file rather
  than hardcoding them. `KIT_CHECK_WIRING_VERSION` bumped, and arms added to `tools/check-wiring.test.sh`.
- `memory/map/features/agent-cap.md` — the new leg name claimed under `gate-legs`, and
  `memory/map/generated/` regenerated in the same commit.

## 3. Non-goals (OUT)

- **Parsing shell.** The predicate is a scan for literal HOME-rooted write shapes. It does not build
  an AST, does not resolve variables, and does not follow a `cd`. See §5 for the named ceiling.
- **Guarding any directory other than the operator's home.** Writes into the repo, into `%TEMP%`, or
  into a session scratchpad are all out of scope; this unit has one subject.
- **`TMPDIR` retargeting and the sweep of the existing litter.** Both are `TOOL-aTetheredScratch-2`,
  deliberately separable, because that unit carries a risk this one does not and may be abandoned.
- **Fixing `TOOL-aBranchedMandate-6`.** The `mrecall-*` leak is a real defect with its own OPEN row;
  relocating or guarding scratch does not repair a cleanup that cannot remove read-only git objects.
- **A second kit version constant.** `version_from` is entry-level and single-valued
  (`tools/govkit/govkit.py:321-341` opens only the named file), so a `KIT_SCRATCH_GUARD_VERSION` would
  be invisible to govkit and buy a note rather than a gate.

## 4. Design

**The hook contract is copied from its sibling, not reinvented.** `tools/hooks/agent-cap.js` denies by
`process.stderr.write(...)` plus `process.exit(2)` and allows by printing nothing and exiting 0; its
header at `:42` records why — "version-robust; no JSON-schema dependency". A repo-wide grep confirms
no source file anywhere emits `permissionDecision` or `hookSpecificOutput`. The new hook uses the same
protocol, reads stdin with the same `fs.readFileSync(0, 'utf8')` inside a `try`, and exits 0 on any
parse failure.

**Scope test.** `data.tool_name !== 'Bash'` exits 0. The command text is `data.tool_input.command`,
absent-safe.

**The predicate, stated as a rule rather than a regex.** A deny requires two things in the same
command: a HOME root and a write context.

The HOME roots recognised, all case-insensitive on the drive spelling: `~/`, `$HOME/`, `${HOME}/`, and
the resolved home in its three live spellings — the MSYS form `/c/Users/<user>/`, the Windows form
`C:\Users\<user>\`, and the mixed form `C:/Users/<user>/`. The resolved home comes from `HOME`, else
`USERPROFILE`; when neither is set only the symbolic roots are recognised, and the hook says so in its
header rather than pretending to full coverage.

The write contexts recognised: a redirect operator (`>`, `>>`, `2>`, `&>`, `2>>`) whose target is a
HOME root; a HOME-rooted argument to a writing command from a closed list — `tee`, `cp`, `mv`,
`install`, `touch`, `mkdir`, `rsync`, `dd of=`; and a `TMPDIR=`, `TMP=` or `TEMP=` assignment to a HOME
root, which is the shape that produced `~/.gov-push/`.

**The allowlist is one path.** A target under `<home>/.claude/` is allowed. It is where the per-machine
skill junction, `settings.json` and the wired hooks live, and `tools/check-wiring.sh --fix` plus every
kit adopter legitimately write there. Allowing the whole of `~/.claude/` rather than enumerating files
keeps the guard from reding the repo's own installers.

**The deny message.** Prefix `BLOCKED by scratch-guard: `, the offending fragment quoted, then the
remedy naming the session scratchpad and `<git-dir>/gate-logs/` as the two sanctioned homes for what
these commands were doing. Findings capped at six, as `agent-cap.js` caps them.

**Why an arm in `check-wiring.sh` and not only a leg.** The leg proves the hook's logic. It cannot
prove the hook is *wired*, and an unwired hook is silent in exactly the way a correctly-behaving one
is. The `recall` arm at `tools/check-wiring.sh:161-197` already reads `marker`, `matcher` and
`hook_path` from a shipped fragment; the new arm is that arm with a different fragment, which is why
the fragment file is in scope rather than the values being hardcoded a second time.

**Why the wiring rides `settings-merge.py` and not a hand edit.** `.claude/settings.json` is owned as a
govkit destination by the `settings-merge` entry, and check 4 (`govkit.py:554-563`) reds when two
entries write one destination. `merge()` at `:91-111` looks its group up by exact `matcher` equality
and appends a new group on a miss, so a `Bash` group lands beside `Workflow|Agent` without touching it,
and re-running is a no-op by structure.

## 5. Production-readiness checklist

- **Security** — the hook is a deny-only guard; it reads stdin, writes stderr, and exits. It executes
  nothing from the payload and opens no file. A command it cannot parse is ALLOWED, which is the
  correct failure direction for a hygiene guard and the wrong one for a security control; this is a
  tidiness rule, not a containment boundary, and is written down here so nobody later mistakes it for
  one.
- **The named ceiling** — the predicate is textual. It does not catch `cd ~ && echo x > y`, a path held
  in a shell variable, a home-rooted write inside a heredoc'd python or node script, or a path assembled
  by expansion. It catches the literal shapes that produced every one of the eighteen observed files.
  This ceiling is stated in the hook header as a `ponytail:` comment naming the upgrade path (a real
  tokenizer) so the limit is discoverable at the code, not only here.
- **Perf** — one regex pass over one command string per `Bash` call. No filesystem access, no
  subprocess. The cost is a node process start, which the `Workflow|Agent` hook already pays per call.
- **False positives** — the risk that matters. A guard that reds innocent commands gets disabled, so
  §6 makes a false-positive probe over the real tree an acceptance criterion rather than a hope.
- **Observability** — the deny text is the whole diagnostic; there is no log. A hook that wrote a log
  would be writing scratch, which is the thing being guarded.
- **a11y / i18n / migration / rollback** — N/A for a hook; rollback is deleting the `Bash` group from
  `.claude/settings.json`, which `check-wiring.sh` then reports as UNWIRED rather than silently.
- **Testing** — `tools/hooks/scratch-guard.test.sh`, carrying the payload-builder liveness guard copied
  from `agent-cap.test.sh:31-33`. That guard exists because the hook fails open on unparseable stdin,
  so a fixture that produced nothing makes every ALLOW arm pass for the wrong reason.

## 6. Acceptance criteria

- **AC1** — The failing case is OBSERVED, not assumed: a payload carrying `echo x > ~/.litter` is fed
  to `tools/hooks/scratch-guard.js` and the run exits `2` with stderr matching `BLOCKED by scratch-guard`.
  Recorded in the build record as a transcript line, per the charter's rule that a gate whose red has
  never been seen is an assertion about nothing.
- **AC2** — The ALLOW half is equally observed: `echo x > ~/.claude/settings.json` and a command with
  no HOME root both exit `0` with empty stderr. Without this half the arm is satisfied by a hook that
  denies everything.
- **AC3** — `bash tools/hooks/scratch-guard.test.sh` exits 0 and its last line matches
  `PASS (<n> assertions)` with `n` equal to the arm count, and the file pins a non-zero
  `FLOOR_ASSERTIONS` referenced by the summary, so `tools/check-testsuite-counts.sh` grades it without
  a waiver row.
- **AC4** — The payload-builder liveness guard fires: with the builder in a scratch copy of
  `tools/hooks/scratch-guard.test.sh` stubbed to emit an empty payload, the suite FAILS rather than
  passing green, and the failure names the builder rather than an arm.
- **AC5** — False-positive probe over the real tree. The predicate is run over every line of every
  tracked `*.sh` and every `argv` string in `tools/gate-legs.json`; hits AND near-misses are printed
  and recorded in the build record. Any hit on a legitimate line is a defect in the predicate, fixed
  before wiring.
- **AC6** — `bash tools/check-wiring.sh --check` prints `ok       scratch-guard` when the `Bash` group
  is present, and `UNWIRED  scratch-guard` naming the fragment's matcher when it is absent — both
  observed, with the padded prefix bytes asserted as the existing arm tests assert them.
- **AC7** — `python tools/govkit/govkit.py selfcheck` exits 0 with the new files claimed: no
  "under its home and no file rule claims it" line for either new file, and no "claimed by no
  descriptor" line for the new leg.
- **AC8** — `python tools/codebase-map/gen_map.py --write` produces no diff after the claim is added,
  and `codebase-map coverage + freshness` is green.
- **AC9** — The full bar is GREEN: `GATE_FULL=1 bash tools/run-gates/run-gates.sh`, with
  `scratch-guard self-test` present in the reported legs rather than skipped.

## 7. Gates

`GATE_FULL=1 bash tools/run-gates/run-gates.sh` — the whole manifest, guards bypassed, which is what
`.githooks/pre-push` runs. The legs this unit is most likely to red, named so a failure is diagnosed
rather than re-derived: `scratch-guard self-test` (new), `check-wiring self-test`,
`settings-merge selftest`, `govkit selfcheck`, `govkit selftest`, `codebase-map coverage + freshness`,
`testsuite counts`, `kit version markers`, `install-prefix self-test`, `workflow script syntax`.

The leg list is single-sourced from `tools/gate-legs.json`; that file is authoritative and this
paragraph names likely failures, not the manifest.

## 8. Open questions

- **RESOLVED — where the hook file lives, and under which kit id.** Considered a new govkit entry with
  its own home. Refused: check 7i quantifies per entry over that entry's home
  (`tools/govkit/govkit.py:834-855`), so a second entry on `tools/hooks` leaves `agent-cap` still
  reding on the unclaimed file, and check 4 forbids a second entry claiming `.claude/settings.json`.
  Ratified: the existing `agent-cap` entry claims both new files, and `KIT_AGENT_CAP_VERSION` is the
  version for the whole home. Resolver: this design pass, on the govkit reading.
- **RESOLVED — deny protocol.** Considered emitting `hookSpecificOutput.permissionDecision`. Refused:
  no source file in this repo emits it, and `agent-cap.js:42` records the stderr-plus-exit-2 choice as
  deliberately version-robust. Two protocols for one act would be the two-answers-to-one-question class.
  Ratified: stderr plus exit 2. Resolver: this design pass.
- **OPEN — whether the allowlist should be `~/.claude/` or narrower.** The wide form lets any future
  tool write anywhere under `~/.claude/`, including scratch. The narrow form (an explicit file list)
  reds the repo's own adopters the moment one adds a file. Proceeding on the wide form because a guard
  that reds its own installers gets disabled, and recording the question here because the choice is
  reversible and the narrow form becomes attractive if `~/.claude/` ever accumulates scratch of its own.

## 9. Revision log

- **rev-1** — 2026-08-20 — authored. Grounded on a five-reader recon of `tools/hooks/`, `tools/govkit/`,
  `tools/check-wiring.sh` with `tools/settings-merge.py`, `tools/gate-legs.json` with
  `memory/guides/BUILD-METHOD.md`, and the `TMPDIR` blast radius. Two forks resolved in §8 from that
  reading; one left open.

## 10. Reuse audit

The seam is `tools/hooks/`, and it is extended rather than duplicated. `tools/hooks/agent-cap.js`
supplies the stdin read, the fail-open parse, the deny protocol, the six-finding cap and the message
prefix convention; `tools/hooks/agent-cap.test.sh` supplies the harness shape, the assertion helper and
— importantly — the payload-builder liveness guard at `:31-33` without which every ALLOW arm is
vacuous. `tools/settings-merge.py` already accepts `--fragment` and `--hook-path` and already appends a
new matcher group on an exact-match miss, so no code there changes; only a fragment file is added.
`tools/check-wiring.sh`'s `recall` arm (`:161-197`) is the model for a fragment-reading arm, as against
the `agent-cap` arm which hardcodes its matcher.

No existing seam covers the predicate itself — nothing in this repo inspects `Bash` command text — so
that is the one genuinely new surface, and it is one file.

Recall terms used, recorded so a resuming pass re-runs the same query:
`scratchpad TMPDIR mktemp hermetic scratch repo gate-logs HOME litter temp residue selftest cleanup redirect`.
The probe returned `TOOL-aBranchedMandate-6`, `TOOL-aTimedTurnstile-1`, the `SESSION-KICKOFF.md`
environment trap, and `memory/gotchas/fixture-inherits-ambient-machine-state.md`, all of which are
cited above or in `TOOL-aTetheredScratch-2`.
