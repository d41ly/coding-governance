# Compaction experiment: the results, and what they mean for unattended builds

**Serves:** research PLAY-dClosedLoop-1

This record scores the blind recall (`build/2026-10-15-build-PLAY-dClosedLoop-1-compaction-recall.md`)
against the inventory (`build/2026-10-15-build-PLAY-dClosedLoop-1-compaction-inventory.md`):
- the recall was committed at `ae229d4ee`, before the key was opened;
- the inventory was committed at `bba25eb6b`, before the compaction.

The tallies come from the instrument in `[instrument]`; none is typed.

## [scoring] The rule

- `exact`: every element the question asks for is present and correct.
- `gist`: the core is right, but an element the question asks for is missing or blurred.
- `wrong`: an element contradicts the key.
- `absent`: no answer.

`Lost or wrong` lists every element of the key's answer that the recall lacks, whether or not the
question asked for it. So an `exact` row with an entry there kept everything it was asked for and still
lost a detail.

`Carrier` names the channel that held the answer after the compaction:
- `summary`: the compaction summary alone;
- `hook`: the session-start hook's output;
- `git`: the re-injected git snapshot;
- `reattached`: a file the compaction attached again;
- `redundant`: two or more channels, each enough on its own;
- `inference` or `prior`: not retention;
- `none`: nothing held it.

The scorer is the subject. Every non-exact row and every lost detail is listed, so any row can be
re-scored.

## [verdicts] Each answer scored

| Q | Verdict | Carrier | Lost or wrong |
|---|---|---|---|
| Q01 | exact | redundant | — |
| Q02 | exact | redundant | — |
| Q03 | exact | hook | — |
| Q04 | exact | git | — |
| Q05 | exact | summary | "four commits on", and what dTracedLedger did: it traced check 23's 37 reds and routed them as asks |
| Q06 | exact | hook | — |
| Q07 | absent | none | `incms-test` (refused), `plugin:github:github` (bad authorization header), `plugin:incms:incms-test` (refused); the harness re-emitted this notice with the next tool result after the recall was written |
| Q08 | exact | redundant | — |
| Q09 | exact | summary | — |
| Q10 | exact | redundant | — |
| Q11 | exact | summary | the ruling's own words (paraphrased); the census's other removals: the waits on aOrientedCast's close, on three live builds in the mapping, and on dScriptedRepeat's recipe mode |
| Q12 | exact | summary | — |
| Q13 | gist | summary | what the check refuses on: a live build, a free or own lease, a filed ask; the reason the disposition declares |
| Q14 | gist | summary | "for the build and slice it is placed into" |
| Q15 | gist | summary | the ref written by compare-and-swap; the cache at `.git/orientation/`; subagents' slice through the brief and the subagent-start hook; Codex through a generated override file |
| Q16 | exact | summary | — |
| Q17 | exact | summary | — |
| Q18 | exact | redundant | the owner's own words (paraphrased) |
| Q19 | exact | redundant | — |
| Q20 | exact | summary | — |
| Q21 | exact | summary | — |
| Q22 | gist | summary | P26's "between roles" |
| Q23 | exact | summary | — |
| Q24 | exact | summary | "the main session is the driver, not a worker" |
| Q25 | exact | summary | step 5's "works inside its allowance" and "up to `roles.retries`" |
| Q26 | exact | redundant | "(background)" |
| Q27 | exact | redundant | — |
| Q28 | exact | redundant | — |
| Q29 | exact | redundant | — |
| Q30 | exact | redundant | — |
| Q31 | exact | summary | "any count the owner sets" |
| Q32 | exact | summary | — |
| Q33 | exact | summary | — |
| Q34 | exact | summary | — |
| Q35 | exact | summary | — |
| Q36 | exact | summary | "85 preset rows" |
| Q37 | exact | summary | — |
| Q38 | exact | summary | — |
| Q39 | gist | redundant | the holes themselves: H6, parallel units contending for git's index lock in one worktree; H7, every landing on a node needing its primary tree |
| Q40 | gist | redundant | H8 itself: whether units born of a closing review are reviewed again; "or BLOCKER" |
| Q41 | exact | summary | each hole's name: intake by hook, back-steps recorded, core checks at Build's exit, a fresh session in the worktree |
| Q42 | absent | none | a median 35 tool calls (p90 67) and 146k fresh input tokens |
| Q43 | absent | none | 467k tokens |
| Q44 | absent | none | 4.1%, 116 of 2,800 |
| Q45 | absent | none | role 11, main session 18, command 9, nobody 32 |
| Q46 | exact | reattached | the file counts: 233 and 98 |
| Q47 | gist | inference | 48 of 48 free text; 94 of 94 structured |
| Q48 | wrong | prior | the largest class is step repetition, at 15.7% (answered at the category level); the 1.5% matched from prior knowledge |
| Q49 | absent | none | 64.5% |
| Q50 | absent | none | 0 of 5 |
| Q51 | absent | none | `ae47198f40bd9a4c0` |
| Q52 | absent | none | `46a0872ae7bf` |
| Q53 | absent | none | `51b61c49e522` |
| Q54 | exact | git | — |
| Q55 | absent | none | `525b64a97` |
| Q56 | absent | none | `tools/hooks/scratch-guard.js:796`; `skills/session-kickoff/manifest-check.sh:499` |
| Q57 | absent | none | `dClosedLoop · PLAY-dClosedLoop-1 · research` |
| Q58 | exact | summary | "its stdout the task part and its stderr the description" |
| Q59 | exact | summary | — |
| Q60 | exact | summary | — |
| Q61 | exact | summary | — |
| Q62 | exact | summary | — |
| Q63 | exact | summary | the section tag `[map]` |
| Q64 | exact | redundant | — |
| Q65 | exact | summary | — |
| Q66 | exact | redundant | — |
| Q67 | exact | summary | — |
| Q68 | absent | none | the injection guard's notice: "subagent output matched instruction-shaped pattern(s): settings-json", once with "permissions-allow-deny", its control tags neutralized |
| Q69 | exact | summary | what the resume did print: the process monitor and the wiring check |
| Q70 | absent | none | `amber-tortoise-1734` |
| Q71 | exact | summary | — |

## [measured] The tallies

Measured on 2026-10-15 from the build folder, exit 0:

```text
all (71)                  exact 48  gist  7  wrong  1  absent 15
exact with nothing lost    35

by probe group
  session (10)            exact  9  gist  0  wrong  0  absent  1
  design (15)             exact 11  gist  4  wrong  0  absent  0
  policies (13)           exact 13  gist  0  wrong  0  absent  0
  holes (3)               exact  1  gist  2  wrong  0  absent  0
  numbers (9)             exact  1  gist  1  wrong  1  absent  6
  identifiers (7)         exact  1  gist  0  wrong  0  absent  6
  procedure (5)           exact  5  gist  0  wrong  0  absent  0
  records (3)             exact  3  gist  0  wrong  0  absent  0
  owner (2)               exact  2  gist  0  wrong  0  absent  0
  context-only (3)        exact  1  gist  0  wrong  0  absent  2
  pending (1)             exact  1  gist  0  wrong  0  absent  0

by blind confidence
  sure (50)               exact 47  gist  3  wrong  0  absent  0
  partial (4)             exact  1  gist  3  wrong  0  absent  0
  guess (2)               exact  0  gist  1  wrong  1  absent  0
  absent (15)             exact  0  gist  0  wrong  0  absent 15

by where the key says it lives (a fact counts under each class it names)
  I (6)                   exact  6  gist  0  wrong  0  absent  0
  M (3)                   exact  3  gist  0  wrong  0  absent  0
  S1 (2)                  exact  2  gist  0  wrong  0  absent  0
  X (11)                  exact  8  gist  0  wrong  0  absent  3
  R (59)                  exact 40  gist  7  wrong  1  absent 11
  this file only (1)      exact  0  gist  0  wrong  0  absent  1

by the last segment the fact was in play
  S0 (2)                  exact  2  gist  0  wrong  0  absent  0
  S1 (2)                  exact  2  gist  0  wrong  0  absent  0
  S2 (1)                  exact  1  gist  0  wrong  0  absent  0
  S3 (5)                  exact  3  gist  0  wrong  0  absent  2
  S4 (16)                 exact  6  gist  2  wrong  0  absent  8
  S5 (2)                  exact  1  gist  1  wrong  0  absent  0
  S6 (25)                 exact 18  gist  2  wrong  1  absent  4
  S7 (15)                 exact 13  gist  2  wrong  0  absent  0
  S8 (3)                  exact  2  gist  0  wrong  0  absent  1

survivors (exact or gist): 55; by carrier, the channel that held each
  summary      34
  redundant    15
  hook          2
  git           2
  reattached    1
  inference     1

channels the blind recall named, over the survivors (an answer names one or more)
  summary      49
  reattached   15
  hook          5
  git           3
  env           2
  inference     2
  charter       2
  memindex      2
  reminder      1
```

Seen red on scratch copies of this record:
- with Q42's row removed, it exits 1: `verdicts: missing ['Q42'], extra []`;
- with Q43's verdict changed to `lost`, it exits 1: `verdicts: unknown verdict on ['Q43']`.

It does not check whether a verdict is right. That is the scorer's judgment, shown row by row in
`[verdicts]`.

## [findings] What the run shows

- **The summary keeps decisions and drops evidence.** These survived whole:
  - policy defaults, 13 of 13;
  - procedure, 5 of 5;
  - record locations, 3 of 3;
  - the owner's words, every probe.

  Measured numbers came back 1 of 9, and that one through a re-attached memory file, not the summary.
  Identifiers came back 1 of 7, and that one through the git snapshot. The summary carried no hash, no
  agent id, no `file:line` and not the handoff description.
- **Loss is omission, not corruption, in the answers.** No answer marked `sure` was wrong, and every
  answer that was guessed was marked as a guess. The session could tell what it had lost. The summary
  itself made one false claim: that the last message before the compaction "was not sent". The verbatim
  tail shows it was.
- **Qualifiers go first.** Every `gist` kept the decision and lost its condition:
  - "for the build and slice";
  - what placement checks;
  - "between roles";
  - "or BLOCKER";
  - the problems behind H6 to H8, whose settlements survived.

  Thirteen `exact` rows lost a detail nobody asked for. In a governed build the condition is often the
  rule, so a summary's copy of a decision is a pointer, never the source.
- **The summary is the single point of failure.** It alone carried 34 of the 55 answers that survived.
  Without it, 21 would survive, and 11 of those only because the last script run before the experiment
  happened to be re-attached.
- **Re-injected channels are exact but narrow, and the hook's content is stale.** Every fact the key
  marks as re-injected survived exact. But the hook replayed the kickoff session's card, written
  2026-10-14T14:30:
  - its scope is still right;
  - its `dirty 11` is wrong;
  - its `now —` line is wrong: it reads the primary tree's `main`, not this worktree (gap-orient-05);
  - it holds nothing of the two days of design since.

  The one channel the product controls brought back the oldest content in the context.
- **Re-attachment is real but accidental.** The harness attached three small, recently read files
  again: the probes, the last amend script and one memory file. Two large ones it only named, "too large
  to include". What survives this way depends on what was read last and how big it is.
- **Harness notices die.** Two lived only in the context: the MCP failures (Q07) and the injection
  guard's notice on researcher returns (Q68). The MCP notice came back with the next tool result after
  the recall was written. Nothing re-emits or records the injection guard's match, which is a security
  event.
- **Records hold what the context lost.** Eleven of the fifteen absent answers live in records:
  - the register's Orient rows alone carry Q42 to Q44, and one of Q56's two locations;
  - record locations survived 3 of 3, so the session knew where to look.

  Losing a fact from the context is not losing it from the build, as long as the finding was recorded
  and the record can be found by its tag.
- **Priors are not retention.** Q48's 1.5% came from prior knowledge of the published taxonomy, and the
  answer's other half was wrong.
- **A second compaction erodes slowly.** Two facts that reached this context only through the first
  summary (Q58, Q62) came through the second exact. Principle statements came through with their
  qualifiers trimmed (P26).
- **Recency and content type are confounded.** Taking the last segment each fact was in play:
  - the most recent work lost nothing: S7, 13 of 15 exact, none absent;
  - the orientation round lost the most: S4, 8 of 16 absent.

  But S4 is where the numbers and identifiers came in, and S7 was decisions. This run cannot tell how
  recent a fact was from what kind of fact it was.
- **The canary died, and this run cannot say why.** The summarizer had read the probe file, knew Q70
  was a test, and says it left the canary out on purpose. The canary measured the summarizer's restraint
  when it knew it was being tested, not how far recency carries a fact.

## [limits] What the run cannot show

- **The summarizer knew the experiment**, so its coverage of the probed facts may be inflated. The
  survival rate is an upper bound for a compaction that does not know it is being tested.
- **One run**: one session and one harness version. The summary's sections follow the harness's own
  template, which keeps user messages, concepts, files, errors and pending work, and has no slot for
  evidence or identifiers.
- **Self-scored.** The rows are listed for anyone to re-score.
- **The probes sample what the inventory asked.** Most of the context was the researchers' full
  returns and v2's text, and those were not probed line by line.

## [conclusions] Keeping facts across automatic compaction in governed unattended builds

1. **Unattended compaction is designed out; keep it out.**
   - In the settled loop the unattended driver is the executor. Its checklist is a program (P24), and
     its engine is owed to the lower-level step. Every role agent starts fresh per item (P25), so if the
     engine holds no model context, nothing long-lived compacts.
   - That becomes a requirement on the engine: **the executor holds no model context.**
   - The run shows why. A summary loses identifiers, numbers and qualifiers, and can assert a false
     state.
   - Compaction stays possible in three places only:
     - an item that overflows its agent;
     - a role session the executor starts when it cannot spawn (`roles.no-spawn` executor-role-session);
     - the attended driver, as in this session.
2. **Write at the item boundary, never at the compaction.**
   - An automatic compaction comes when it comes, and a fact written just before one, the canary, did
     not carry.
   - Step 6 of the item cycle persists the return as a typed record (P26), so it is the write point.
     Whatever an item finds goes into its return, and so into a record: numbers, identifiers, harness
     notices.
   - A pre-compaction hook, where the harness offers one, is a backstop for an item's work in flight,
     never the store.
3. **After a compaction, re-derive; never trust the summary's state.**
   - Position comes from witnesses (P22): `next`, the card's ref, git.
   - The summary is a model-typed claim with no key, so P23 already refuses it. It is a lead to follow,
     not a state to trust.
4. **Start fresh at an item boundary rather than compact.**
   - A fresh session from a current card costs less than a resume: a median 146k fresh input tokens
     against 467k (gap-orient-06).
   - It loses nothing the records hold. A compaction loses what this run lost.
   - So a model-driven session nearing its window ends at the next item boundary and continues fresh
     from the card. The executor restarts its role session; the attended driver tells the owner.
   - Compaction remains the fallback for an item that overflows. (Fork CX-1.)
5. **The compact replay carries the current card, shaped for what summaries drop.**
   - The hook is the product's one controlled channel, and it works: everything re-injected survived
     exact.
   - It renders the build's card from its ref at that moment, in the session's own tree.
     gap-orient-05, 11 and 12 already own those mechanics.
   - The card carries the classes the summary loses:
     - handles: the base and HEAD SHAs, the current item and its actor, the open handoff's description,
       the open fork tags;
     - pointers, by tag, to the records that hold numbers and evidence.
   - The summary keeps decisions; the card keeps handles.
6. **Record harness notices with the return.** An injection-guard match on a return is a security
   event. The executor persists returns at step 6, so it persists their annotations too. (Fork CX-2.)
7. **Owner words go through the intake hook; H2 is confirmed.** The owner's quotes survived because the
   harness's template keeps user messages, which is a template choice, not a guarantee. The prompt-submit
   hook writing every owner prompt verbatim makes it deterministic.
8. **Size items to fit their agent.** An item whose reading overflows its agent's window compacts
   mid-item and loses its own handles, the way this session did. Plan and Design size items to fit one
   context, and the allowance names a context ceiling.

## [proposed] For the owner

- **CX-1, `context.on-full`.** What a model-driven session does as its window fills:
  - `fresh-at-boundary`, recommended: at `context.threshold`, a share of the window proposed at 60%, it
    ends at the next item boundary and continues fresh from the card;
  - `compact-with-card`: the harness compacts, and the hook re-injects the current card.
- **CX-2, `notices.record`.** Which harness notices become session-log events:
  - `security-and-failures`, recommended: injection-guard matches on returns, and connection failures;
  - `all`;
  - `none`.
- **CX-3, two gaps and the owed checks.**
  - gap-orient-14: compaction is ungoverned. Nothing persists an item's work before an automatic
    compaction, nothing sets a session's response to a full window, and the summary is treated as a
    source. Owner: dDeclaredLoop.
  - gap-roles-09: a return's harness notices are not recorded. Owner: dBoundRoles.
  - Into v2's `[owed]`, to verify at the lower-level step rather than assume:
    - whether the harness honours compaction instructions in the instruction file, that is, a keep-list
      in the charter;
    - whether a pre-compaction hook can flush an item's partial return, in the main session and in a
      subagent;
    - whether a subagent's own compaction re-injects its brief;
    - the re-attachment rule's count and size cap, so the card file is sized to come back too;
    - the requirement that the executor's engine holds no model context.

## [instrument] The scorer

Run from the build folder:
`python compaction_score.py <probes> <recall> <inventory> <this record>`. It refuses unless every probe
from Q01 to Q71 has exactly one row in each file, and unless every verdict is one of the four.

```python
"""Join the compaction experiment's four files and print its tallies: the probes (groups), the blind
recall (confidence, channels), the key (where each fact lives, its segments) and the verdicts (verdict,
carrier, what was lost). Exits 1 unless every probe Q01..Q71 has exactly one row in each."""
import re
import sys
from collections import Counter

probes_p, recall_p, key_p, verdict_p = sys.argv[1:5]
QS = [f"Q{i:02d}" for i in range(1, 72)]
V = ["exact", "gist", "wrong", "absent"]


def table(path, ncols):
    """Rows `| Qnn | c1 | ... |`, keyed by probe, the cells after the probe split on ' | '."""
    out = {}
    for line in open(path, encoding="utf-8", newline=""):
        m = re.match(r"\| (Q\d\d) \| (.*) \|$", line.rstrip("\r\n"))
        if not m:
            continue
        cells = [c.strip() for c in m.group(2).split(" | ")]
        if len(cells) != ncols:
            sys.exit(f"{path}: {m.group(1)} has {len(cells)} cells, expected {ncols}")
        if m.group(1) in out:
            sys.exit(f"{path}: {m.group(1)} twice")
        out[m.group(1)] = cells
    return out


groups, group = {}, None
for line in open(probes_p, encoding="utf-8", newline=""):
    if m := re.match(r"## \[([a-z-]+)\]", line):
        group = m.group(1)
    if m := re.match(r"- (Q\d\d)\. ", line):
        groups[m.group(1)] = group

recall = table(recall_p, 3)    # confidence, channels, answer
key = table(key_p, 3)          # answer, lives, segments
verdict = table(verdict_p, 3)  # verdict, carrier, lost or wrong
for name, t in (("probes", groups), ("recall", recall), ("key", key), ("verdicts", verdict)):
    if sorted(t) != QS:
        sys.exit(f"{name}: missing {sorted(set(QS) - set(t))}, extra {sorted(set(t) - set(QS))}")
bad = [q for q in QS if verdict[q][0] not in V]
if bad:
    sys.exit(f"verdicts: unknown verdict on {bad}")


def row(label, qs):
    c = Counter(verdict[q][0] for q in qs)
    return f"{label + f' ({len(qs)})':<26}" + "  ".join(f"{v} {c.get(v, 0):>2}" for v in V)


def lives(q):
    return [t.strip() for t in re.sub(r"\(.*?\)", "", key[q][1]).split(",")]


def last_seg(q):
    return f"S{max(int(s) for s in re.findall(r'S(\d)', key[q][2]))}"


print(row("all", QS))
print(f"exact with nothing lost    {sum(1 for q in QS if verdict[q][0] == 'exact' and verdict[q][2] == '—')}")
print("\nby probe group")
for g in dict.fromkeys(groups[q] for q in QS):
    print(row(f"  {g}", [q for q in QS if groups[q] == g]))
print("\nby blind confidence")
for conf in ("sure", "partial", "guess", "absent"):
    print(row(f"  {conf}", [q for q in QS if recall[q][0] == conf]))
print("\nby where the key says it lives (a fact counts under each class it names)")
for cls in ("I", "M", "S1", "X", "R", "this file only"):
    print(row(f"  {cls}", [q for q in QS if cls in lives(q)]))
print("\nby the last segment the fact was in play")
for s in sorted({last_seg(q) for q in QS}):
    print(row(f"  {s}", [q for q in QS if last_seg(q) == s]))
surv = [q for q in QS if verdict[q][0] in ("exact", "gist")]
print(f"\nsurvivors (exact or gist): {len(surv)}; by carrier, the channel that held each")
for k, n in Counter(verdict[q][1] for q in surv).most_common():
    print(f"  {k:<12}{n:>3}")
print("\nchannels the blind recall named, over the survivors (an answer names one or more)")
for k, n in Counter(c.strip() for q in surv for c in recall[q][1].split(",")).most_common():
    print(f"  {k:<12}{n:>3}")
```
