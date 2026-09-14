# KICK-aReplayedCard-2 — `--card --append` and `--card --check` run the batched citation check

**Status:** CLOSED · rev-5 · 2026-09-14 · node a · Tier-2 · base c4f02308 · streams kickoff · order 3

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-13-build-KICK-aReplayedCard-1-0-orientation-design.md](../build/2026-09-13-build-KICK-aReplayedCard-1-0-orientation-design.md) | research | KICK-aReplayedCard-1 KICK-aReplayedCard-3 TOOL-aReplayedCard-1 TOOL-aReplayedCard-2 TOOL-aReplayedCard-3 TOOL-aReplayedCard-4 TOOL-aReplayedCard-5 |
| [2026-09-14-build-KICK-aReplayedCard-2-1-acceptance-ledger.md](../build/2026-09-14-build-KICK-aReplayedCard-2-1-acceptance-ledger.md) | journal | — |
| [2026-09-13-prompt-KICK-aReplayedCard-1-0-run-mandate.md](../prompts/2026-09-13-prompt-KICK-aReplayedCard-1-0-run-mandate.md) | journal | KICK-aReplayedCard-1 KICK-aReplayedCard-3 TOOL-aReplayedCard-1 TOOL-aReplayedCard-2 TOOL-aReplayedCard-3 TOOL-aReplayedCard-4 TOOL-aReplayedCard-5 |
| [2026-09-14-prompt-KICK-aReplayedCard-2-brief.md](../prompts/2026-09-14-prompt-KICK-aReplayedCard-2-brief.md) | journal | — |
| [2026-09-13-review-KICK-aReplayedCard-1-spec-audit-round1.md](../reviews/2026-09-13-review-KICK-aReplayedCard-1-spec-audit-round1.md) | spec-audit | KICK-aReplayedCard-1 KICK-aReplayedCard-3 TOOL-aReplayedCard-1 TOOL-aReplayedCard-2 TOOL-aReplayedCard-3 TOOL-aReplayedCard-4 TOOL-aReplayedCard-5 |
| [2026-09-14-review-KICK-aReplayedCard-1-closing-diff-round1.md](../reviews/2026-09-14-review-KICK-aReplayedCard-1-closing-diff-round1.md) | diff-review | KICK-aReplayedCard-1 KICK-aReplayedCard-3 TOOL-aReplayedCard-1 TOOL-aReplayedCard-2 TOOL-aReplayedCard-3 TOOL-aReplayedCard-4 TOOL-aReplayedCard-5 |
| [2026-09-14-review-KICK-aReplayedCard-1-spec-audit-round2.md](../reviews/2026-09-14-review-KICK-aReplayedCard-1-spec-audit-round2.md) | spec-audit | KICK-aReplayedCard-1 KICK-aReplayedCard-3 TOOL-aReplayedCard-1 TOOL-aReplayedCard-2 TOOL-aReplayedCard-3 TOOL-aReplayedCard-4 TOOL-aReplayedCard-5 |
| [2026-09-14-review-KICK-aReplayedCard-1-spec-audit-round3.md](../reviews/2026-09-14-review-KICK-aReplayedCard-1-spec-audit-round3.md) | spec-audit | KICK-aReplayedCard-1 KICK-aReplayedCard-3 TOOL-aReplayedCard-1 TOOL-aReplayedCard-2 TOOL-aReplayedCard-3 TOOL-aReplayedCard-4 TOOL-aReplayedCard-5 |

<!-- /gen:spec-records -->

## 1. Goal

Let the kickoff engine append its curated orientation to the card through the checker rather than
by hand, with every cited path, line range and record id checked for EXISTENCE in two batched
spawns, an annotation on every miss, and a refusal when the card would breach its cap or carry a
stale BASE. The accuracy review the objective asked for is this mechanical half; truth at the cited
line stays with the charter's verify-before-act rule.

## 2. Scope (IN)

- **S1** `--card --append --session <sid>` reads stdin, extracts every path-shaped token and every
  id-shaped token, and resolves them in TWO spawns: `git ls-files -- <paths>`, whose output is
  per path, and `python tools/memory-tree/corpus_ids.py --print-defined-ids`, a new read-only verb
  on the reader that already owns the id grammar and hygiene check 14, set-differenced against the
  id tokens. A path token carrying `:lo-hi` is a miss when `hi` exceeds the file's line count. A
  basename citation, the house style `run-gates.sh:407`, is resolved against `git ls-files` when
  exactly one tracked file has that basename and is a miss when none or several do. The verb's
  FIRST line is the id grammar as a POSIX ERE, `# id-ere: <ere>`, and the defined set follows one
  per line: the shell extracts id tokens with that line and spells no grammar of its own, which is
  how the non-goal below and the one-spawn budget hold at once. The reader is
  `corpus_ids.py` under whichever of `tools/memory-tree/` or `memory-tree/` holds it — the engine's
  own `<MEMORY_TREE_KIT>` rule — launched as `${GOV_PYTHON:-python}`; a tree with neither announces
  the id half skipped on one `NOTE:` line and checks paths alone, and a reader that exits non-zero
  or whose first line is not the grammar is a refusal, exit 2, because a set that could not be read
  is not an empty set. The body arrives on stdin, so `--append` takes its session id from
  `--session` alone. Observed by AC1, AC2, AC3 and AC9.
- **S2** A miss is never dropped. The row stays and one `UNVERIFIED — <token>` line is added beneath
  it, with `(ambiguous: <n> matches)` on a basename that resolved to several files and
  `(past end: <n> lines)` on a range whose `hi` exceeds the count, so an absent citation is visible
  and a present one is not mistaken for a vetted one. Observed by AC2 and AC9.
- **S3** Zero extractable tokens in the body is `DEAD PROBE: nothing to check`, exit 1, and nothing
  is appended. A probe that cannot move says so. Observed by AC3.
- **S4** An append whose result would exceed `CARD_CAP_BYTES`, the constant `KICK-aReplayedCard-1`
  declares, exits 2 naming the overage and leaves the file byte-identical. Observed by AC4.
- **S5** A body carrying a `READY —` line whose tail is not `none yet` replaces the card's
  `READY — none yet` sentinel in place, so the card holds exactly one READY line; a body with no
  such line leaves the sentinel. A second such body, appended to a card that already holds a real
  READY line, REPLACES the previous READY line and the six sections beneath the startup lines, so
  the card holds one body — the latest kickoff's — and the cap is never consumed twice; a session
  that kicks off again, in a sibling worktree say, is never refused for a body it no longer needs.
  A body with no real READY line goes in BEFORE the card's READY line, sentinel or real, so the
  card always ends with its one READY line — the shape `KICK-aReplayedCard-3` AC2 reads; a body's
  own `READY — none yet` line is dropped, never stored; a body carrying two real READY lines is
  refused, exit 2, because one card holds one kickoff. Observed by AC5 and AC10.
- **S6** A body whose READY line carries a `base <sha>` that is not `git rev-parse HEAD` at append
  time is refused with exit 2 naming both shas, so a BASE stale by a commit, a compaction or a
  resume cannot land on the card whatever engine text produced it. Observed by AC8.
- **S7** `--card --check --session <sid>` re-runs S1's check over the whole stored card, skipping
  the `UNVERIFIED —` annotation lines themselves, prints each miss, and exits 1 on any. It writes
  nothing. A card with no extractable token is S3's `DEAD PROBE`, exit 1, for the same reason.
  Observed by AC6.
- **S8** The verb's header states what it does NOT check: relevance, scope correctness, tier, and
  the truth of a claim at the line it cites. NOT OBSERVED by a criterion: prose, read at review.
- **S9** Every refusal uses the script's `MANIFEST env ERROR — …` shape with its exit code, not the
  numbered `fail` recorder, so `ARMS_FLOORS` does not move; every refusal is armed in
  `manifest-check.test.sh` and `FLOOR_ASSERTIONS` moves in the same commit. Observed by AC7.
- **S10** An append carrying a real READY line rewrites the card's `tree —` cell to the toplevel
  the append runs in, spelled as `KICK-aReplayedCard-1` S3 declares, because the kickoff ran THERE
  and that is what the cell asserts; a session that moved to a sibling worktree is then oriented in
  the tree it commits from. Observed by AC10.
- **S11** `--card --check` also refuses, exit 1, a card that carries a real READY line and no
  `## task` section — the shape that says a kickoff ran and left no scope on disk. Observed by
  AC11.

## 3. Non-goals (OUT)

- No second model pass over the card. The design record's section 6 rejects a second LLM refuter:
  another slot, another read of the sources, and no better view of truth.
- No relevance scoring. Relevance is the engine's selection at Step 4 (`KICK-aReplayedCard-3`).
- No waiver line; owner decision 2.
- No per-token git spawn. The design record's verdict 40 measured the loop at 25–50 s for thirty
  tokens against ~1.1 s batched.
- No second spelling of the id grammar in shell. `TOOL-cSpliceWarden-6` ruled that a check grading
  a declared grammar delegates to the reader that owns it; `corpus_ids.py` is that reader.

### Edges

- **consumes-from** `KICK-aReplayedCard-1` — the card file, the cap constant and the
  `READY — none yet` sentinel; without the card there is nothing to append to.
- **hands-off** `KICK-aReplayedCard-3` — the engine's Step 5 body shape and the pipe into this verb.
- **hands-off** `TOOL-aReplayedCard-1` — the single `READY —` line the deny reads.
- **consumes-from** external — `git ls-files` over the tracked tree and `corpus_ids.py`'s defined-id
  set; an untracked record is invisible to both and is reported as a miss, which the header states.

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
same rule `tools/check-spec-tokens.py` uses at its line 142, plus a basename-with-extension token
followed by `:<line>`, which that lint counts and skips and this verb resolves when unique; that
lint's exclusions carry over — a glob, a `{{placeholder}}`, a `$var`, a `<slot>` — and two more
that only a card meets: an absolute path (`/x/…`, `C:/…`), because the `tree —` cell carries one
and it is a checkout location rather than a claim about the tree, and a URL. An id token matches
the families the conf declares, extracted by the same regex `corpus_ids.py` exposes on the first
line of its `--print-defined-ids` output, translated to POSIX ERE (`(?:` to `(`, `\d` to `[0-9]`,
the only two constructs the grammar builder uses). Paths go to one `git ls-files -- …` call, with
`<basename>` and `*/<basename>` pathspecs for the basename citations; ids are joined against the
defined set the same python spawn prints. Line ranges are checked against the line count of the
resolved file.

The card after an append is STARTUP + TAIL. STARTUP is the header through the `recent —` line and
the run of `<sha> <subject>` lines beneath it; TAIL is everything after, and holds exactly one
`READY —` line, last. A real-READY body replaces the whole TAIL and re-renders the `tree —` cell; a
body without one is inserted before the TAIL's READY line.

### Inventory

| Identifier | Kind | Where | Cell |
|---|---|---|---|
| `extract_card_tokens` | shell function | `manifest-check.sh` | leads with `extract`, a declared shape out of text |
| `check_card_citations` | shell function | `manifest-check.sh` | leads with `check`, a verdict |
| `add_card_body` | shell function | `manifest-check.sh` | leads with `add`, membership in the file |
| `check_card` | shell function | `manifest-check.sh` | the `--check` verb: S7 and S11 over the stored card |
| `render_tree_cell` | shell function | `manifest-check.sh` | the one spelling of the `tree —` line, lifted out of `render_card` so the append re-renders it identically |
| `split_card` | shell function | `manifest-check.sh` | STARTUP and TAIL of a stored card into two scratch files |
| `--print-defined-ids` | verb | `corpus_ids.py` | a print-only verb beside `--report` and `--measure` |
| `print_defined_ids` | python function | `corpus_ids.py` | leads with `print`, stdout for a caller |

### Migration

None.

### Rollout

Callable by hand from the commit that lands it; the engine pipes into it from
`KICK-aReplayedCard-3` onward.

### Files touched (estimate)

| Path | Change |
|---|---|
| `skills/session-kickoff/manifest-check.sh` | three functions, the two verbs, the miss annotation, the BASE refusal |
| `skills/session-kickoff/manifest-check.test.sh` | arms for S2, S3, S4, S5, S6, S7, S9; `FLOOR_ASSERTIONS` |
| `tools/memory-tree/corpus_ids.py` | the `--print-defined-ids` verb, one selftest arm |
| `tools/memory-tree/README.md` | the verb in `corpus_ids.py`'s row |
| `memory/map/features/session-kickoff.md` | the append and check in the card paragraph |
| `tools/install-prefix-waivers.txt` | two line-keyed rows re-keyed: the verb's lines land above the selftest fixture they waive |
| `tools/install-prefix-carried.txt` | `corpus_ids.py`'s carried count falls 8 to 4: the docstring's usage lines derive the kit path, so the new verb's line adds no literal |
| `memory/guides/SESSION-KICKOFF.md` | `last-audit` re-stamp |

### Alternatives rejected

**Dropping a row whose citation misses.** A dropped row is indistinguishable from a row nobody
wrote; the annotation keeps the claim and marks it.

**Checking truth at the line.** No cheap reader can; the header says so and the charter's §5 rule
owns the rest.

**`git grep -l -F -f` for ids.** `-l` names files, not tokens, so one call cannot say which id was
absent; `-F` without `-w` lets `X-1` match inside `X-10`, the class
`memory/gotchas/id-matched-as-a-substring.md` records; and a mention is not a definition, which is
what hygiene check 14 exists to tell apart.

**Skipping basename citations.** Half the corpus cites by basename; a silent skip on the card reads
as vetted, and the lint this rule comes from prints its skip count for exactly that reason.

## 5. Production-readiness checklist

- security — stdin is treated as data; tokens reach git only through `--`, and the id set is read
  from a python process's stdout, never through shell interpolation.
- perf / scale — two spawns per append, ~1.1 s measured for thirty tokens on the git side; the
  python spawn costs one interpreter start; the append happens once per kickoff.
- error / empty / loading states — zero tokens is DEAD PROBE; an over-cap body is refused; a stale
  BASE is refused; a missing card is a refusal naming `--card --write` as the remedy.
- observability — every miss is printed and annotated; `--check` reports the whole card.
- risks — an id that exists but is irrelevant passes; the header states existence-only.
- testing — arms in `manifest-check.test.sh`, staged RED first.
- migration — none.
- user docs — the script's own header; the kit ships no README.

## 6. Acceptance criteria

- **AC1** — When a body citing `skills/session-kickoff/SKILL.md:47-60` and the id
  `TOOL-cBriefedPilot-11` is piped to `--card --append --session t2` with a READY line whose base is
  `git rev-parse HEAD`, the card gains the body, no `UNVERIFIED` line, and exactly one git process
  and one python process were spawned by the check, observed with the self-test's shadowed `git`
  and `python` functions counting invocations.
  Red when: a per-token loop spawns one process per token.
  figure: DERIVED — the shadows count at observation.
- **AC2** — When a body cites a path that is not tracked, an id no spec defines though a record
  cites it, an id `X-1` while `X-10` is defined, and a range whose `hi` exceeds the file's line
  count, the card carries each row followed by its own `UNVERIFIED — <token>` line, and the append
  exits 0.
  Red when: a miss is dropped, the substring id passes, or the cited-but-undefined id passes.
- **AC3** — When a body with no path-shaped and no id-shaped token is piped, stdout carries
  `DEAD PROBE`, the exit is 1, and the card is byte-identical.
  Red when: an empty check appends and exits 0.
- **AC4** — When a body sized past `CARD_CAP_BYTES` is piped to `--card --append`, the exit is 2
  naming the overage and the card is byte-identical.
  Red when: a truncated append lands.
- **AC5** — When a body carrying a `READY — t · node a` line is appended, the card holds exactly one
  line starting `READY —` and it is the body's; a second append without one leaves it; a body whose
  only READY line is `READY — none yet` leaves the sentinel and the card still holds one.
  Red when: `READY — none yet` survives beside the real line and the deny reads the wrong one.
- **AC6** — When `--card --check --session t2` runs over a card holding one annotated miss, it
  prints the miss and exits 1; over a clean card it prints nothing and exits 0.
  Red when: `--check` reads the annotation lines as tokens and reports them as misses.
- **AC7** — When `bash skills/session-kickoff/manifest-check.test.sh` runs, it prints `PASS` at or
  above the moved `FLOOR_ASSERTIONS`, and `check-arms.py --check` reports this script's floor
  unchanged.
  Red when: an arm lands unasserted, or a refusal was written as `fail`.
- **AC8** — When a body whose READY line carries a `base` eight commits behind `git rev-parse HEAD`
  is piped, the exit is 2 naming both shas and the card is byte-identical.
  Red when: a stale BASE lands and the charter's diff-scoping runs against the wrong sha.
- **AC9** — When a body cites `manifest-check.sh:60` and `README.md:1`, the first resolves and is
  not annotated and the second is annotated `UNVERIFIED — README.md:1 (ambiguous: <n> matches)`
  with `n` equal to the count of tracked files named `README.md`.
  Red when: a basename citation is neither resolved nor annotated.
  figure: DERIVED — `git ls-files | grep -c '/README.md$'` at observation.
- **AC10** — When a card written by `--card --write` in worktree A of the self-test's fixture is
  appended to with a real READY line by `--card --append` run from sibling worktree B, the card's
  `tree —` cell names B's toplevel in the declared spelling and the rest of the startup lines are
  byte-identical; when a card already holding a real READY line and its body from A is appended to
  again from B with a second full body, the card holds one READY line, one `## task` section and
  B's cell, and its size is under the cap where two bodies would not be.
  Red when: the cell keeps A, so the deny refuses every commit from B for the session's life; or
  the second append stacks a second body and the cap refuses the moved session.
- **AC11** — When `--card --check` runs over a card holding a real READY line and no `## task`
  heading, it exits 1 naming the missing section; over a card holding both it exits 0.
  Red when: a kickoff's READY line lands with no scope beneath it and the check calls it clean.

## 7. Gates

`manifest-check self-test` · `kickoff-manifest ratchet` · `lexicon naming predicates` · `shell hygiene (a loop fed by a command substitution)` · `memory hygiene` · `install-prefix (shipped surface)`

New arm: `skills/session-kickoff/manifest-check.test.sh` · an untracked path, a cited-but-undefined id, `X-1` beside a defined `X-10`, an over-long range · `FLOOR_ASSERTIONS`
New arm: `skills/session-kickoff/manifest-check.test.sh` · a token-free body · same
New arm: `skills/session-kickoff/manifest-check.test.sh` · a body past the cap · same
New arm: `skills/session-kickoff/manifest-check.test.sh` · a READY line with a stale base · same
New arm: `skills/session-kickoff/manifest-check.test.sh` · a unique and an ambiguous basename citation · same
New arm: `skills/session-kickoff/manifest-check.test.sh` · an append from a sibling worktree of the fixture · same
New arm: `skills/session-kickoff/manifest-check.test.sh` · a READY line with no `## task` section · same

The full bar is owed with `GATE_SELFTESTS=1`.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-09-13 · initial draft.
- rev-2 · 2026-09-13 · §1 · §2 · §3 · §4 · §6 · §7 · S1 · S2 · S5 · S6 · S7 · S9 · AC1 · AC2
  · AC5 · AC7 · AC8 · AC9 · folded the round-1 spec audit. Id existence delegates to a new
  `corpus_ids.py --print-defined-ids` verb instead of a mention grep (H4, M8); basename citations
  resolve when unique and annotate when not (M9); the sentinel exclusion is spelled in S5 (H1); a
  READY line with a stale base is refused at the write boundary (M3's left-shift); `--check` skips
  its own annotations (S7); refusals use the env-error shape and `ARMS_FLOORS` is dropped for
  `FLOOR_ASSERTIONS` (M10); the user-docs row names the script header (L1).
- rev-3 · 2026-09-14 · §2 · §6 · §7 · S10 · S11 · AC10 · AC11 · folded the round-2 spec audit.
  The append rewrites the `tree —` cell to the tree it runs in, so a session that moved worktrees
  has a remedy (round-2 H4); `--check` refuses a READY line with no `## task` beneath it (round-2
  M3's left-shift).
- rev-4 · 2026-09-14 · §2 · §6 · S5 · AC10 · folded the round-3 spec audit's exit: a second real
  READY append replaces the previous READY line and body, so a re-kickoff never stacks bodies
  against the cap (round-3 M5).
- rev-5 · 2026-09-14 · §2 · §4 · S1 · S2 · S5 · S7 · the build pass's divergences, changed here
  before the code. The shell cannot extract id-shaped tokens without the grammar and the non-goal
  bans spelling it, so the ONE python spawn carries the grammar on its first line as a POSIX ERE
  (S1, §4); the reader is located by the engine's `<MEMORY_TREE_KIT>` rule and a tree without it
  announces the skip; a reader that fails is a refusal, not an empty set. `--append` takes its
  session id from `--session` alone, because stdin is the body. Absolute paths and URLs are not
  path tokens: the `tree —` cell carries one. A range miss says `(past end: <n> lines)` (S2). The
  STARTUP/TAIL model is written down (§4): a no-READY body goes before the READY line so the card
  always ends with it, which `KICK-aReplayedCard-3` AC2 reads; a body's sentinel line is dropped;
  two real READY lines refuse (S5). `--check` over a token-free card is DEAD PROBE (S7). Three
  helpers join the inventory; the kit README's verb row and the dossier's card paragraph join the
  files touched.

## 10. Reuse audit

The seams are `tools/memory-tree/corpus_ids.py`, the reader that owns the id grammar and hygiene
check 14 and gains one print verb beside its `--report` and `--measure`, and the path-shaped rule in
`tools/check-spec-tokens.py` line 142, reused rather than re-spelled. `python
tools/codebase-map/reuse_lookup.py "session orientation card written at session start, replayed
after compaction, commit denied until READY"` returned `manifest-check.sh` as the seam and reported
the shell layer unscanned; the id reader was found through `TOOL-cSpliceWarden-6`, which ruled that
a check grading a declared grammar delegates to its owner. The `UNVERIFIED —` annotation reuses
the spelling the spec template already reserves for a claim not verified against source.

Recall terms used: `manifest-check verb kickoff engine scratch-guard PreToolUse deny SessionStart matcher settings-merge fragment check-wiring arm session card compaction`
