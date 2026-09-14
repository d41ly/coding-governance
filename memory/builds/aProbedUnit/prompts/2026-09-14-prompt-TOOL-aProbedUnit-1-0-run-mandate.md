# Run mandate — aProbedUnit

**Serves:** journal TOOL-aProbedUnit-1

The owner's prompt, verbatim, as handed to `/unattended --prompt` on node `a`, 2026-09-14. The bytes
travel here rather than as a reference, because the build folder is the authorization and may not
point at a file that can be edited after the run starts. The value carried whitespace and named no
readable file, so it is the prompt itself.

## The prompt

> Several major changes and bug fixes need to be made to the unattended kit. Review them, orient in
> the relevant code, build per the protocol. Ensure that this build equally applies to the repo
> itself and its adopters:
>
> * CRITICAL. Individual unattended build units (workflows/agents building individual specs) are
>   instructed to run full gates (including self-checks), which results in many stalled unit builds -
>   up to 12h so far and counting, blocking entire builds. This should not happen. In a single
>   session, gates should only run ONCE, PRE-MERGE, when all the findings get fixed.
> * CRITICAL. Unattended build units are often stalled during certain command executions, resulting
>   in whole sessions being blocked for hours. Unit audit probe is required to spot long running build
>   units and make them progress. PRIMARY OBJECTIVE: code needs to be written. If a check is slow,
>   cleanup command is hanged, or any other unrelated to code writing is not progressing - it can be
>   skipped and should not block the session from progressing.
> * HIGH. On the above, node d has encountered this problem - "Almost all of that time was one
>   blocked command, not work. fix:web did about 13 minutes of real work, sat for 6 hours 14 minutes
>   on a single rm, and has been working again since 09:30 local. It isn't hung now.
>
>   The transcript shows the sequence:
>   - 03:12–03:16 local: it worked normally. It made the web edits, observed a staged red, and saved
>     backups of two files before editing them.
>   - 03:15:56: it ran rm -f /LinkLanding.keep … to clean up one of those backups. Because $TMPDIR
>     was empty in its shell, the copy had gone to /LinkLanding.keep, the Git Bash root outside the
>     repo and scratchpad.
>   - 09:30:37: that rm finally returned, with nothing in between. A trivial delete that takes 6 hours
>     and then succeeds most likely hit an approval prompt for a delete outside the workspace, which
>     sat unanswered until 09:30. I can't see the prompt itself in the transcript, so that part is
>     inference.
>   - Since 09:30: it has finished the typecheck, the lexicon and clone checks, and both staged e2e
>     reds. The run.sh harness's local API and web servers for the modals spec came up at
>     09:41–09:42, so a 10-minute timeout from about 09:51 is the worst case.
>
>   Because this workflow runs its two fixers as a pair, the API fixer (done at 03:28) and the verify
>   stage have been waiting on fix:web the whole time. No other work was lost; the stray backup is
>   gone.
>
>   To stop this recurring, future fixer prompts will tell agents to put backups in the scratchpad
>   path explicitly instead of relying on $TMPDIR." Apply a fix that will make units write directly
>   to their session's scratchpad and this issue doesn't reoccur. A floating temp dir has been an
>   ongoing problem - the owner has seen sessions write to /tmp /Temp and various other dirs.
> * Only ONE round of tier2 reviews for specs by default, instead of two. Blockers and Highs are
>   promoted, Mediums and Lows are folded into their specs.

## The one owner turn, and its answers

Asked once, four questions in one call, before the build folder was written. Answered 2026-09-14:

| Question | Answer |
|---|---|
| What does "promoted" mean for a spec-audit finding? | A UNIT, per M4: `--rescope --act add`, specced at its tier, audited once, built. Mediums and lows are rev-bumped into their spec with no re-review. |
| Does the one-round default cover the closing diff review? | SPECS ONLY. The diff review keeps its convergence loop; a code blocker is undone work and its fix is what round 2 checks. |
| The stall bound the audit probe grades against? | 30 minutes — `UNIT_STALL_BOUND=1800`, declared in `.unattended.conf`. |
| Should the scratch-guard deny `/tmp` writes too? | YES. Deny `/tmp`, beside the empty-variable and root-litter denials; the CLI's own scratch base under the temp root stays allowed. |

## How the prompt maps to units

| Prompt item | Unit | Mechanism |
|---|---|---|
| CRITICAL, gates per unit | `TOOL-aProbedUnit-1` | no gate, suite or bar runs inside a unit pass; the bar runs once at `--close` |
| CRITICAL, stalled commands | `TOOL-aProbedUnit-2` | every command a unit runs carries a timeout; a stalled non-code command is skipped and named |
| CRITICAL, unit audit probe | `TOOL-aProbedUnit-3` | `--audit <slug>`: idle time per dispatched unit against `UNIT_STALL_BOUND`, and the keepalive runs it |
| HIGH, scratchpad | `TOOL-aProbedUnit-4` | the harness hands every agent the caller's scratchpad path and orders every temporary file under it |
| HIGH, `$TMPDIR` empty, `/tmp` | `TOOL-aProbedUnit-5` | the scratch-guard hook denies an empty temp variable at a target's head, `/tmp`, and a new entry at the POSIX root |
| one review round | `TOOL-aProbedUnit-6` | `REVIEW_ROUNDS` (default 1) bounds a spec-audit subject; the `BOUNDED` terminal exit |
| blockers and highs promoted | `TOOL-aProbedUnit-7` | the harness's DISPOSAL stage runs on any confirmed finding and disposes by severity |

## What the orientation found before the roster was written

- `memory/builds/aRatifiedRulings/README.md` carries the 2026-09-13 owner ruling "a pass runs the
  fast diff-scoped gates and NOTHING held" — a rule with no carrier in the child prompt, which is why
  unit 1 exists. This prompt tightens it: not even diff-scoped; the bar runs once.
- `TOOL-aProvenReuse-3` (OPEN) argues a spec-subject blocker has no promotable referent. The owner's
  answer above keeps M4's meaning; unit 7's disposal prompt says what the promoted unit IS.
- `TMPDIR` is empty on node `a` too (measured this session), and the scratch-guard's own scanner
  over 55,231 real tool calls found 72 `$TMPDIR`-rooted write targets, 3,803 `/tmp` targets, and 4
  POSIX-root litter targets — the corpus behind unit 5's predicates.
- The CLI's SessionStart hooks receive `CLAUDE_ENV_FILE`, which could export `TMPDIR` per session.
  NOT taken: pointing `TMPDIR` at the scratchpad puts every gate leg's `mktemp -d` clone under a
  ~150-character path, which this node's own memory records failing on MAX_PATH.
