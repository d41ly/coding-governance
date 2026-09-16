# TOOL-cMendedVintage-9 — the card verbs resolve a session id without blocking on an open stdin

**Status:** SPECCED · rev-1 · 2026-09-16 · node c · Tier-2 · base 859daa67 · streams tooling · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-16-prompt-DEPL-cMendedVintage-1-1-spec-briefs.md](../prompts/2026-09-16-prompt-DEPL-cMendedVintage-1-1-spec-briefs.md) | journal | DEPL-cMendedVintage-1 DEPL-cMendedVintage-2 DEPL-cMendedVintage-3 DEPL-cMendedVintage-4 DEPL-cMendedVintage-5 DEPL-cMendedVintage-6 DEPL-cMendedVintage-7 DEPL-cMendedVintage-8 DEPL-cMendedVintage-9 DEPL-cMendedVintage-10 DEPL-cMendedVintage-11 DEPL-cMendedVintage-12 DEPL-cMendedVintage-13 DEPL-cMendedVintage-14 TOOL-cMendedVintage-1 TOOL-cMendedVintage-2 TOOL-cMendedVintage-3 TOOL-cMendedVintage-4 TOOL-cMendedVintage-5 TOOL-cMendedVintage-6 TOOL-cMendedVintage-7 TOOL-cMendedVintage-8 |

<!-- /gen:spec-records -->

## 1. Goal

`read_session_id` in `skills/session-kickoff/manifest-check.sh` reads stdin for the SessionStart
hook's JSON whenever stdin is not a terminal, so every tool-invoked shell — which hands the child an
open pipe that never sends EOF — hangs in `sed` forever. Skip that read when the caller already
answered the question by passing `--session`, so a card verb invoked from a harness returns.

## 2. Scope (IN)

- **S1** `read_session_id` at `skills/session-kickoff/manifest-check.sh:128` skips the stdin read
  when `CARD_SID` is already non-empty, so `--session <sid>` and `--session=<sid>` both short-circuit
  it. Observed by AC1 and AC4.
- **S2** Every other resolution path is unchanged: the hook's JSON still answers when no `--session`
  was given, the two-channel refusal still fires when neither answers, and `--append` still never
  reads stdin. Observed by AC2 and AC3.
- **S3** The comment block above `read_session_id` states the precedence the code now has, because
  the block as written says the two channels are read in the other order. Observed by AC5.
- **S4** `skills/session-kickoff/manifest-check.test.sh` gains one arm that HOLDS stdin open and
  asserts the verb returns, so the hang is in the suite rather than only in the fix. Observed by AC1.

## 3. Non-goals (OUT)

- No bounded read (`read -t 1`, a `timeout` wrapper around the `sed`). A bound still pays the wait on
  every harness invocation and picks a number nothing derives.
- No new flag (`--no-stdin`, `--hook`). The caller passing `--session` is already the declaration.
- No change to `--card --append`, whose stdin IS the body it stores and which is already excluded.
- No change to the refusal messages' wording beyond S3's comment; the message at
  `skills/session-kickoff/manifest-check.sh:133` still names both channels.

### Edges

- **consumes-from** external — the card verbs, their `--session` parsing and `CARD_SID`, all landed
  by `KICK-aReplayedCard-1` and present at this build's BASE. Nothing in this build builds them.
- **hands-off** external — nothing. No other unit in this build touches the kickoff kit.

## 4. Design

### Data model

No data shape changes. `CARD_SID` is already parsed from argv at
`skills/session-kickoff/manifest-check.sh:91-99` BEFORE `read_session_id` runs, so the value the new
test reads is in hand at the point of the test.

Today the line is a three-term short-circuit: `--append` wins, then a terminal on fd 0 wins, then the
`sed` runs. Adding `[ -n "$CARD_SID" ]` as a third guard ahead of `[ -t 0 ]` gives the read four ways
to be skipped and leaves its one way to run — no `--append`, no `--session`, no terminal — exactly
the SessionStart hook's own shape. The assignment two lines down, `[ -n "$sid" ] || sid="$CARD_SID"`,
then supplies the id, so no second code path is needed to make `--session` work.

### The precedence change, and its measured blast radius

This makes `--session` beat the hook's JSON when a caller supplies both. That is a behaviour change
and it is stated rather than implied. The live callers, enumerated rather than assumed:

| Caller | Channel | Affected |
|---|---|---|
| `.claude/settings.json:33` SessionStart hook, `--card --write` | JSON on stdin, no `--session` | no |
| `.claude/settings.json:42` SessionStart hook, `--card --replay` | JSON on stdin, no `--session` | no |
| `skills/session-kickoff/manifest-check.test.sh:801` | JSON on stdin, no `--session` | no |
| `skills/session-kickoff/manifest-check.test.sh` `run_card` | `</dev/null`, `--session` | no |
| `tools/hooks/scratch-guard.test.sh:567` and `:579` | `</dev/null`, `--session` | no |

The population is six live invocations, not zero, and each was read: one feeds stdin, five pass
`--session`, none passes both. Re-derive with
`grep -rn -- '--card' .claude/settings.json skills/session-kickoff/ tools/hooks/`. That reading is
what makes the precedence safe to choose rather than a preference; it is not an argument that no
caller could ever pass both, and S3's comment is where the answer for one that does is written down.

### Inventory

No identifier is minted. The change is one shell test inserted into an existing short-circuit and one
suite arm; there is no new function, flag, file or config key, so no naming cell grades anything here.

### Files touched (estimate)

`skills/session-kickoff/manifest-check.sh` — one term added to line 128, plus the comment block above
it (about five lines). `skills/session-kickoff/manifest-check.test.sh` — one arm of about eight lines
beside the existing `AC3` card arms near line 795.

`ARMS_FLOORS` in `.memory-tree.conf` pins `skills/session-kickoff/manifest-check.sh:28:28`. This unit
adds a condition to an existing branch and deletes no `exit 2`, so the branch and armed counts do not
fall and the floor does not move. If a build-time reading disagrees, the floor is what moved and the
change is wrong, not the pin.

### Alternatives rejected

- **A bounded read.** `sid=$(timeout 1 sed …)` or a `read -t 1` loop returns, but every harness
  invocation then pays the bound, and the bound is a magic number with nothing behind it. It also
  leaves the hang visible as latency rather than removing it.
- **Discriminate on the fd type.** `[ -p /dev/stdin ]` is true for the hook's own channel, which is a
  pipe, so it cannot tell the hook apart from a harness. This is the discriminator that looks obvious
  and does not exist.
- **Refuse when both channels are present.** A refusal is a worse outcome than a precedence for a
  caller that is already telling the truth, and no live caller produces the state.

### Migration

None. No stored artifact changes shape, and a card written before this lands is read unchanged.

### Rollout

Lands directly. The change can only widen the set of invocations that return, and the two hook
entries in `.claude/settings.json` take the unchanged path.

## 5. Production-readiness checklist

- **security** — the id still passes the `..` and `[A-Za-z0-9._-]` guards at
  `skills/session-kickoff/manifest-check.sh:135-138` before it is joined into a path; the skip is
  ahead of those guards, not instead of them. An id from `--session` was already subject to them.
- **perf / scale** — removes an unbounded wait; adds one string test.
- **error / empty / loading states** — an empty `--session ""` leaves `CARD_SID` empty, so the guard
  does not fire, the read runs, and the existing refusal at line 133 still names both channels. AC3
  observes that.
- **observability** — no new output. The refusal message is the only place the channels are named and
  it is unchanged.
- **risks** — the precedence change is the only one, and the table in §4 is its measurement. The
  residual is a future caller that passes both and expects stdin to win; S3's comment is what such a
  caller reads.
- **testing** — four direct observations against the real script (AC1-AC4) plus one source assertion
  (AC5), and one arm folded into the kit's own suite by S4.
- **migration** — N/A, nothing stored changes.
- **user docs** — `skills/session-kickoff/SKILL.md` describes the verbs and not the id channels, so
  no page changes. The comment block S3 rewrites is the documentation for this behaviour.

## 6. Acceptance criteria

- **AC1** — When `sleep 30 | timeout 10 bash skills/session-kickoff/manifest-check.sh --card --path --session probe-ac1`
  runs from the repo root, it exits 0 within the bound and prints a path ending `probe-ac1.md`.
  Red when: the stdin read still runs, `sed` blocks on the pipe that never closes, and `timeout`
  returns 124.
- **AC2** — When `printf '{"session_id":"probe-ac2"}' | bash skills/session-kickoff/manifest-check.sh --card --path`
  runs with no `--session`, it exits 0 and prints a path ending `probe-ac2.md`.
  Red when: the new guard is written so that it also skips the read for a caller that passed no
  `--session`, which silently breaks the SessionStart hook.
- **AC3** — When `bash skills/session-kickoff/manifest-check.sh --card --path </dev/null` runs, it
  exits 2 and the message names both channels.
  Red when: the guard is placed so that an absent id resolves to the empty string and the verb
  proceeds, or so that the refusal names only one channel.
- **AC4** — When `printf '{"session_id":"hookside"}' | bash skills/session-kickoff/manifest-check.sh --card --path --session flagside`
  runs, it prints a path ending `flagside.md`.
  Red when: the read is skipped but the assignment order still lets a stdin-derived id overwrite
  `CARD_SID`, so the hook's value wins and the declared precedence is not the one implemented.
- **AC5** — When `grep -n 'session' skills/session-kickoff/manifest-check.sh` is read over the
  comment block above `read_session_id`, that block states that `--session` suppresses the stdin read.
  Red when: the code changed and the block beside it still describes stdin as the first channel
  consulted, which is the prose-beside-the-source class this repo already gates elsewhere.

## 7. Gates

`kickoff-manifest ratchet` · `manifest-check self-test` · `scratch-guard self-test`

New arm: skills/session-kickoff/manifest-check.test.sh · a `sleep`-held pipe on stdin with
`--session` supplied, asserting the verb returns instead of reaching the suite's own wall · none

The `scratch-guard self-test` leg is named because two of its arms invoke the card writer with
`--session` and `</dev/null`; they take the new short-circuit and must stay green.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-09-16 · initial draft.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py` over the card's session-id resolution returns no seam for
this behaviour: the ranked candidates are all rendering and kit-path helpers, and the file has no
existing "read one field from the hook's JSON" helper to extend — the `sed` at
`skills/session-kickoff/manifest-check.sh:128` is the only such site in the kit. The seam this unit
extends is therefore that line itself, and the short-circuit it already uses for `--append`: the fix
adds a fourth term to an existing three-term guard rather than introducing a mechanism. Recall
confirmed the surrounding design is `KICK-aReplayedCard-1` §S2 ("the `session_id` is read from the
JSON the SessionStart hook hands on stdin, else from `--session <sid>`"), which states an ELSE this
code does not implement — so the change restores the documented order rather than inventing one, and
no prior record considered the never-EOF case.

Recall terms used: `kickoff manifest card session orientation stdin hook SessionStart sid terminal
pipe blocking read refusal`
