# KICK-aReplayedCard-2 — `--card --append` and `--card --check` run the batched citation check

**Status:** SPECCED · rev-1 · 2026-09-13 · node a · Tier-2 · base c4f02308 · streams kickoff · order 3

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-13-build-KICK-aReplayedCard-1-0-orientation-design.md](../build/2026-09-13-build-KICK-aReplayedCard-1-0-orientation-design.md) | research | KICK-aReplayedCard-1 KICK-aReplayedCard-3 TOOL-aReplayedCard-1 TOOL-aReplayedCard-2 TOOL-aReplayedCard-3 TOOL-aReplayedCard-4 TOOL-aReplayedCard-5 |
| [2026-09-13-prompt-KICK-aReplayedCard-1-0-run-mandate.md](../prompts/2026-09-13-prompt-KICK-aReplayedCard-1-0-run-mandate.md) | journal | KICK-aReplayedCard-1 KICK-aReplayedCard-3 TOOL-aReplayedCard-1 TOOL-aReplayedCard-2 TOOL-aReplayedCard-3 TOOL-aReplayedCard-4 TOOL-aReplayedCard-5 |

<!-- /gen:spec-records -->

## 1. Goal

Let the kickoff engine append its curated orientation to the card through the checker rather than
by hand, with every cited path, line range and record id checked for EXISTENCE in one batched git
call, an annotation on every miss, and a refusal when the card would breach its cap. The accuracy
review the objective asked for is this mechanical half; truth at the cited line stays with the
charter's verify-before-act rule.

## 2. Scope (IN)

- **S1** `--card --append --session <sid>` reads stdin, extracts every path-shaped token and every
  id-shaped token, runs ONE `git ls-files -- <paths>` and ONE `git grep -l -F -f <tokenfile>` over
  the memory root, and appends the body to the card. A path token carrying `:lo-hi` is a miss when
  `hi` exceeds the file's line count. Observed by AC1, AC2 and AC3.
- **S2** A miss is never dropped. The row stays and one `UNVERIFIED — <token>` line is added beneath
  it, so an absent citation is visible and a present one is not mistaken for a vetted one.
  Observed by AC2.
- **S3** Zero extractable tokens in the body is `DEAD PROBE: nothing to check`, exit 1, and nothing
  is appended. A probe that cannot move says so. Observed by AC3.
- **S4** An append whose result would exceed the cap constant `KICK-aReplayedCard-1` declares
  exits 2 naming the overage and leaves the file byte-identical. Observed by AC4.
- **S5** A body carrying a `READY —` line replaces the card's `READY — none yet` sentinel in place
  rather than adding a second READY line; a body with no READY line leaves the sentinel. Observed by
  AC5.
- **S6** `--card --check --session <sid>` re-runs S1's check over the whole stored card, prints each
  miss, and exits 1 on any. It writes nothing. Observed by AC6.
- **S7** The verb's header states what it does NOT check: relevance, scope correctness, tier, and
  the truth of a claim at the line it cites. NOT OBSERVED by a criterion: prose, read at review.
- **S8** Every `fail` site added is armed and the `ARMS_FLOORS` entry moves in the same commit.
  Observed by AC7.

## 3. Non-goals (OUT)

- No second model pass over the card. The design record's section 6 rejects a second LLM refuter:
  another slot, another read of the sources, and no better view of truth.
- No relevance scoring. Relevance is the engine's selection at Step 4 (`KICK-aReplayedCard-3`).
- No waiver line; owner decision 2.
- No per-token git spawn. The design record's verdict 40 measured the loop at 25–50 s for thirty
  tokens against ~1.1 s batched.

### Edges

- **consumes-from** `KICK-aReplayedCard-1` — the card file, the cap constant and the
  `READY — none yet` sentinel; without the card there is nothing to append to.
- **hands-off** `KICK-aReplayedCard-3` — the engine's Step 5 body shape and the pipe into this verb.
- **hands-off** `TOOL-aReplayedCard-1` — the single `READY —` line the deny reads.
- **consumes-from** external — `git grep -F -f` over the tracked memory tree; an untracked record is
  invisible to it and is reported as a miss, which the header states.

## 4. Design

### Data model

The appended sections are the engine's, one heading each, holding cited rows and never paraphrase:

```
## task      the sealed skeleton fields as derived, or "unfillable: <field> — <why>"
## manifest  <path> · audit ok|FAIL <files> · watch-commits-since-stamp <n>
## read      ≤12 rows `path:lo-hi — why`
## records   ≤8 rows `ID — one clause — path:line` · `Recall terms used:` line
## classes   gotcha class names from --for-paths, one line
## open      parked fields and questions
READY — <slug> · node <tag> · <branch> · base <sha> · Tier-<n> · gates <list>
```

Token extraction: a path token is a backticked or bare token with a slash and an extension, the
same rule `tools/check-spec-tokens.py` uses at its line 142; an id token matches the families the
conf declares, `FAMILY-<slug>-<seq>`. The two sets are written to one temp file and resolved by the
two git calls. Line ranges are checked against `wc -l` of the resolved file.

### Inventory

| Identifier | Kind | Where | Cell |
|---|---|---|---|
| `extract_card_tokens` | shell function | `manifest-check.sh` | leads with `extract`, a declared shape out of text |
| `check_card_citations` | shell function | `manifest-check.sh` | leads with `check`, a verdict |
| `add_card_body` | shell function | `manifest-check.sh` | leads with `add`, membership in the file |

### Migration

None.

### Rollout

Callable by hand from the commit that lands it; the engine pipes into it from
`KICK-aReplayedCard-3` onward.

### Files touched (estimate)

| Path | Change |
|---|---|
| `skills/session-kickoff/manifest-check.sh` | three functions, the two verbs, the miss annotation |
| `skills/session-kickoff/manifest-check.test.sh` | arms for S2, S3, S4, S5, S6 |
| `.memory-tree.conf` | `ARMS_FLOORS` |
| `memory/guides/SESSION-KICKOFF.md` | `last-audit` re-stamp |

### Alternatives rejected

**Dropping a row whose citation misses.** A dropped row is indistinguishable from a row nobody
wrote; the annotation keeps the claim and marks it.

**Checking truth at the line.** No cheap reader can; the header says so and the charter's §5 rule
owns the rest.

## 5. Production-readiness checklist

- security — stdin is treated as data; tokens reach git only through `-f <file>` and `--`, never
  through shell interpolation.
- perf / scale — two git spawns per append, ~1.1 s measured for thirty tokens; the append happens
  once per kickoff.
- error / empty / loading states — zero tokens is DEAD PROBE; an over-cap body is refused; a missing
  card is a refusal naming `--card` as the remedy.
- observability — every miss is printed and annotated; `--check` reports the whole card.
- risks — an id that exists but is irrelevant passes; the header states existence-only.
- testing — arms in `manifest-check.test.sh`, staged RED first.
- migration — none.
- user docs — the kit README's verb table.

## 6. Acceptance criteria

- **AC1** — When a body citing `skills/session-kickoff/SKILL.md:47-60` and the id
  `TOOL-cBriefedPilot-11` is piped to `--card --append --session t2`, the card gains the body, no
  `UNVERIFIED` line, and exactly two git processes were spawned by the check, observed with the
  self-test's shadowed `git` function counting invocations.
  Red when: a per-token loop spawns one git per token.
  figure: DERIVED — the shadow counts at observation.
- **AC2** — When a body cites a path that is not tracked, an id no record defines, and a range whose
  `hi` exceeds the file's line count, the card carries each row followed by its own
  `UNVERIFIED — <token>` line, and the append exits 0.
  Red when: a miss is dropped or the append refuses.
- **AC3** — When a body with no path-shaped and no id-shaped token is piped, stdout carries
  `DEAD PROBE`, the exit is 1, and the card is byte-identical.
  Red when: an empty check appends and exits 0.
- **AC4** — When a body sized past `CARD_CAP_BYTES` is piped to `--card --append`, the exit is 2
  naming the overage and the card is byte-identical.
  Red when: a truncated append lands.
- **AC5** — When a body carrying a `READY —` line is appended, the card holds exactly one line
  starting `READY —` and it is the body's; a second append without one leaves it.
  Red when: `READY — none yet` survives beside the real line and the deny reads the wrong one.
- **AC6** — When `--card --check --session t2` runs over a card holding one annotated miss, it
  prints the miss and exits 1; over a clean card it prints nothing and exits 0.
  Red when: `--check` reads the annotation lines as tokens and reports them as misses.
- **AC7** — When `python tools/memory-tree/check-arms.py --check` runs, this script's floor has
  moved by the `fail` sites added here and none is in `unarmed-branches.txt`.
  Red when: an arm lands unasserted.

## 7. Gates

`manifest-check self-test` · `harness arms (fail branches armed or pinned)` · `kickoff-manifest ratchet` · `lexicon naming predicates` · `shell hygiene (a loop fed by a command substitution)` · `memory hygiene`

New arm: `skills/session-kickoff/manifest-check.test.sh` · a body with an untracked path, an undefined id and an over-long range · this script's `ARMS_FLOORS` entry
New arm: `skills/session-kickoff/manifest-check.test.sh` · a token-free body · same floors
New arm: `skills/session-kickoff/manifest-check.test.sh` · a body past the cap · same floors

The full bar is owed with `GATE_SELFTESTS=1`.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-09-13 · initial draft.

## 10. Reuse audit

The seam is the path-shaped rule in `tools/check-spec-tokens.py` line 142, reused verbatim rather
than re-spelled, and the batched `git grep -F -f` shape the design record's skeptic measured
against the per-token loop. `python tools/codebase-map/reuse_lookup.py "session orientation card
written at session start, replayed after compaction, commit denied until READY"` returned
`manifest-check.sh` as the seam and reported the shell layer unscanned; the extraction rule was
found by reading the spec-token lint. The `UNVERIFIED —` annotation reuses the spelling the
spec template already reserves for a claim not verified against source.

Recall terms used: `manifest-check verb kickoff engine scratch-guard PreToolUse deny SessionStart matcher settings-merge fragment check-wiring arm session card compaction`
