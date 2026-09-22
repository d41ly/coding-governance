# Wave 2 — Lens C: prose load on the load-bearing instruction documents

## Verdict: CLEAN WITH FIXES

**Serves:** research TOOL-aScouredKit-2

**Subject:** `093730e40355d6a04300966f791f2634379e8b45`, whole product surface.
**Question asked:** can any load-bearing instruction `.md` be optimized without breaking its
instructions, unambiguity or context?

**Short answer.** Almost none of it by prose-trimming — the corpus is unusually disciplined about
duplication and says so in its own rules. But the *budgets* are effectively spent, the ratchet that
prices growth has stopped being obeyed, and there are five concrete instances of the two classes this
repo already bans in writing: a rule stated in more carriers than it needs, and a number typed beside
a source that owns it. Those are the findings. Everything else I looked at, I am refusing to propose.

---

## 1. The population, measured

Bytes are `wc -c` on the tracked file. Ceilings from `tools/template-size-limits.txt` (gated by
`tools/check-template-size.sh`), `.memory-tree.conf` / `memory/HYGIENE.md` check 6 (`GUIDE_CAP_BYTES`
61440 / `GUIDE_CAP_LINES` 750), and `memory/guides/BUILD-METHOD.md` M1's own stated budget.

| file | bytes | lines | ceiling | margin | used |
|---|---:|---:|---|---:|---:|
| `AGENTS.md` | 64471 | 584 | 64512 (declared) | **41 B** | **99.94 %** |
| `WIRE-INTO-PROJECT.md` | 59833 | 816 | *none* | — | — |
| `memory/guides/UNATTENDED-PROTOCOL.md` | 57098 | 698 | 61440 B / 750 lines | 4342 B / **52 lines** | 92.9 % |
| `coding-governance-agents.template.md` | 48907 | 407 | 49152 (declared) | **245 B** | **99.50 %** |
| `.claude/skills/unattended/SKILL.md` | 48767 | 731 | *none* | — | — |
| `memory/HYGIENE.md` | 29811 | 397 | 61440 / 750 | 31629 B | 48.5 % |
| `memory/guides/SESSION-KICKOFF.md` | 25508 | 313 | 61440 / 750 | 35932 B | 41.5 % |
| `memory/guides/BUILD-METHOD.md` | 24549 | 317 | **24 KiB / 350 (M1, ungated)** | **27 B** / 33 lines | **99.89 %** |
| `tools/memory-tree/README.md` | 18430 | 214 | none | — | — |
| `skills/session-kickoff/SKILL.md` | 18225 | 274 | 18432 (declared) | **207 B** | **98.88 %** |
| `memory/guides/REVIEW-PROTOCOL.md` | 16304 | 222 | 61440 / 750 | 45136 B | 26.5 % |
| `tools/memory-recall/README.md` | 15386 | 226 | none | — | — |
| `memory/TEMPLATE-SPEC.md` | 14139 | 230 | 61440 / 750 | 47301 B | 23.0 % |
| `tools/run-gates/README.md` | 12762 | 180 | none | — | — |
| `memory/guides/PLAYBOOK-TEMPLATE.md` | 11423 | 187 | 61440 / 750 | 50017 B | 18.6 % |
| `tools/lexicon/README.md` | 11287 | 183 | none | — | — |
| `tools/drift-audit/README.md` | 10115 | 162 | none | — | — |
| `.claude/skills/drift-audit/SKILL.md` | 6550 | 122 | none | — | — |
| `.claude/skills/lexicon/SKILL.md` | 6530 | 87 | none | — | — |
| `tools/pytest-parallel-guardrails/README.md` | 5888 | 87 | none | — | — |
| `tools/codebase-map/README.md` | 5438 | 74 | none | — | — |
| `.claude/skills/memory-recall/SKILL.md` | 5280 | 92 | none | — | — |
| `tools/hooks/README.md` | 4982 | 73 | none | — | — |
| `tools/agent-instructions/README.md` | 3807 | 61 | none | — | — |
| `tools/playbook/README.md` | 2677 | 52 | none | — | — |
| `memory/README.md` | 2412 | 35 | 61440 / 750 | — | — |
| `tools/gate-lint/README.md` | 1945 | 40 | none | — | — |

Commands:

```
for f in <population>; do printf "%8d %6d  %s\n" "$(wc -c < "$f")" "$(wc -l < "$f")" "$f"; done | sort -rn
bash tools/check-template-size.sh coding-governance-agents.template.md
bash tools/check-template-size.sh AGENTS.md
bash tools/check-template-size.sh skills/session-kickoff/SKILL.md
```

All three gated subjects print a `TEMPLATE-SIZE WARN` before their OK line:

```
TEMPLATE-SIZE WARN — coding-governance-agents.template.md grew past its recorded high-water: 48378 -> 48907 (+529).
template-size OK — coding-governance-agents.template.md: 48907 / 49152 bytes (245 under, 99.5%)
TEMPLATE-SIZE WARN — AGENTS.md grew past its recorded high-water: 60930 -> 64471 (+3541).
template-size OK — AGENTS.md: 64471 / 64512 bytes (41 under, 99.9%)
TEMPLATE-SIZE WARN — SKILL.md grew past its recorded high-water: 18215 -> 18225 (+10).
template-size OK — SKILL.md: 18225 / 18432 bytes (207 under, 98.9%)
```

---

## F1 — `AGENTS.md` has 41 bytes of headroom, and the ratchet that is supposed to price growth has been ignored on all three subjects. **high**

`tools/template-size-limits.txt:54` declares 64512 for `AGENTS.md`. Live: 64471. **41 bytes.**

The leg is unguarded, so it runs on every bar:

```json
{ "name": "charter size", "argv": ["bash","tools/check-template-size.sh","AGENTS.md"],
  "chunk": "product", "subject": "repo", "ceiling": 300 }
```
(`tools/gate-legs.json`, the only leg naming `AGENTS.md`.)

**Verified by staging the break.** One ordinary 99-byte wrapped charter line appended, gate run,
restored:

```
TEMPLATE-SIZE check 2 FAILED — the file is over its size budget: AGENTS.md is 64570 bytes, 58 over 64512.
exit=1
```

`git diff --stat AGENTS.md` clean afterwards. So the *next* charter edit of one line reds the merge
bar. And because `AGENTS.md` re-renders the template's `gov:playbook` region (lines 76–470), the
template's own 245-byte margin is not the binding one — `AGENTS.md`'s 41 bytes is.

The second half is worse than the first. `tools/template-size-highwater.txt` reads:

```
1  AGENTS.md                              60930
2  coding-governance-agents.template.md   48378
3  skills/session-kickoff/SKILL.md        18215
```

Live values are 64471 / 48907 / 18225. Every subject is past its record; nobody has re-recorded
with `--bump`. The gate's own header calls the ratchet "what prices growth now that the ceiling is no
longer doing it" (`tools/check-template-size.sh:7-8`). Three standing advisory WARNs on every bar
that nobody acts on is a signal that has stopped meaning anything — the same normalized-deviance
shape §7 gates against elsewhere. The ratchet is not broken; it is unheeded.

Nothing in `memory/backlog/TOOL.md` or `DEPL.md` tracks either half (grepped `64512`, `high-water`,
`highwater`, `template-size` — no hits).

---

## F2 — `memory/HYGIENE.md` declares itself the prose home of the check catalog and stops at check 22. The gate implements check 23. **high**

`memory/HYGIENE.md:114`:

> `## The check catalog (all in tools/memory-tree/check-memory-hygiene.sh; this file is the prose home)`

The numbered list runs 1…22 and ends at `memory/HYGIENE.md:252` (`22. **review verdict
vocabulary**`). There is no item 23. Confirmed:

```
grep -n "^23\.\|check 23\|ACCEPTANCE_LEDGER" memory/HYGIENE.md   ->  no output
grep -n "^23\.\|check 23\|ACCEPTANCE_LEDGER" tools/memory-tree/HYGIENE.template.md -> only line 252 (item 22)
```

Check 23 exists and can red the bar. `tools/memory-tree/check-memory-hygiene.sh:1120`:

```
# ---- 23: every acceptance criterion of a CLOSED Tier-2 unit is EVIDENCED or AMENDED.
# ---- NUMBERED 22 IN THIS COMMENT UNTIL 2026-08-27, AND IT WAS NEVER 22. Every fail arm below
# ---- says 23 and so does the pop_guard; 22 is the review-verdict vocabulary at `:610`, and
# ---- HYGIENE.md item 22 says so too. A spec trusted this header and graded the wrong check.
```

with three live fail arms at `:1285`, `:1286`, `:1287`, all emitting through
`fail() { echo "HYGIENE check $1 FAILED — $2"; ...}` (`:126`). So a session that trips it reads
`HYGIENE check 23 FAILED — …` and, following the file that says it is the prose home, finds nothing.

The header above is the tell: whoever landed check 23 (TOOL-dUnstalledConvoy-12, 2026-08-27) read
`HYGIENE.md` closely enough to cite item 22 and did not add item 23.

**Nothing catches it.** The only leg comparing the two is `kit/dogfood doc parity`
(`tools/memory-tree/kit-dogfood-parity.test.sh`), which byte-compares `memory/HYGIENE.md` against
`tools/memory-tree/HYGIENE.template.md`. Both are missing item 23, so the parity leg is green over a
shared gap. No gate compares the catalog against the shell's check numbers
(grepped `tools/memory-tree/*.sh`, `*.py`, `tools/*.sh`).

Not tracked. `memory/backlog/TOOL.md` has two check-23 rows (`TOOL-aSiftedFork-1`, `-2`) and both are
about the awk stream inside the check, not about its absence from the catalog.

*This is a prose finding, not a trim — but it is the same class as (b): the catalog's completeness is
asserted by a heading rather than derived, and it is now false.*

---

## F3 — `tools/memory-tree/README.md:18` says "23 checks" and then enumerates 22. **medium**

```
| `check-memory-hygiene.sh` | the gate — 23 checks (1-12, 21 and 22 in the shell, 13-16 delegated to
`corpus_ids.py`, 17-19 to `gotchas.py`, 20 to `row_grammar.py`; …) |
```

Add it up: 1–12 (12) + 21, 22 (2) = 14 in the shell; 13–16 (4); 17–19 (3); 20 (1). **22.** Check 23
lives in the shell (`check-memory-hygiene.sh:1120`) and appears in no bucket.

This number is load-bearing by explicit design. `AGENTS.md:203-206` (charter §5) says the hygiene
gate is one "whose check count is **stated by the kit README** and the gate-leg name and is
deliberately not restated here". So the charter delegates the count to this cell, and this cell's own
breakdown now disagrees with its headline.

The repo already names the class in its own backlog — `TOOL-aSiftedFork-5`: *"a number typed beside a
population it does not derive is this repo's own named class"*. That row is a different instance (the
verdict-epoch remedy message). This one is new.

---

## F4 — `AGENTS.md` states the unattended-authorization rule three times; the third is pure restatement. **medium**

1. `AGENTS.md:127` — charter §1 Landing, the normative statement:
   > That explicit ask has ONE substitute: a committed build folder the run did not create, whose
   > shape your merge bar validates. The mandate is ASSERTED, never written by the run that uses it,
   > and must be reachable from a BASE observed on the remote rather than read from a local ref. A
   > run with full shell access can still defeat that, and the control that actually binds lives on
   > the remote.
2. `AGENTS.md:555-560` — "Two protocols are BINDING", the *stronger* version:
   > …replaces the explicit-ask checkpoint with a committed standing mandate it ASSERTS and cannot
   > have written. The BASE that mandate hangs on is OBSERVED from the remote's own HEAD
   > advertisement, never read from a local ref and never named by the environment; both of those
   > were reproduced bypasses. §9 states plainly what a check running under the run's own uid can and
   > cannot buy.
3. `AGENTS.md:579-584` — Conventions, **559 bytes**, carrying no property the first two do not:
   > Commit freely; **merge to `main` and `git push` each need an explicit ask — or a committed build
   > folder the run did not create**, whose shape the merge bar validates. The mandate is ASSERTED,
   > never written by the run that uses it, and must be reachable from the run's pinned BASE, which
   > is observed from the remote rather than read from any local ref. A run with full shell access
   > can still defeat that; the protocol's §9 says exactly how, and the control that actually binds
   > lives on the remote. Rules: `memory/guides/UNATTENDED-PROTOCOL.md`.

There is a fourth partial at `AGENTS.md:36` (the "What ships here" bullet on the unattended kit).

**Where each removed rule survives.** "explicit ask, or a committed build folder the run did not
create" → `AGENTS.md:127`. "ASSERTED, never written by the run that uses it" → `AGENTS.md:127` and
`:557`. "BASE observed from the remote, not a local ref" → `AGENTS.md:127` and `:558-559` (which says
it more precisely: *HEAD advertisement*, and names the reproduced bypasses). "full shell access can
still defeat it / §9 / the control lives on the remote" → `AGENTS.md:127` and `:560`. The pointer at
`memory/guides/UNATTENDED-PROTOCOL.md` survives at `:556`.

So bullet 3 can collapse to its first clause plus its pointer — roughly `- Commit freely; merge and
push each need an explicit ask, or the standing-mandate substitute (§1 Landing, and "Two protocols
are BINDING" above).` That is ~440 bytes recovered, **eleven times the current margin**, with every
rule surviving in a named carrier inside the same file. This is exactly what §6 calls "one fact in
one place", applied to the document that states it.

The template's own §1 unattended block already models the discipline: *"It is NOT paraphrased here —
a paraphrase and its source are two answers to one question, and the paraphrase is the copy that
rots."* Bullet 3 is the paraphrase.

---

## F5 — `memory/guides/BUILD-METHOD.md` is 27 bytes under its own byte budget — the half M1 says binds first — and no gate enforces it. **medium**

M1 (`memory/guides/BUILD-METHOD.md:8-19`):

> **Budget: ≤24 KB, ≤350 lines** … **The BYTE half binds first** — at this file's ~100 B prose line
> the bytes run out near line 316, so most of the line figure is headroom the bytes do not grant. No
> gate enforces the pair.

Live: **24549 bytes** (`wc -c`, LF-normalized identical), **317 lines**. Against 24 KiB = 24576 that
is 27 bytes and the file is one line past its own predicted stopping point. Against a decimal 24 KB
= 24000 it is already 549 bytes **over**. M1 does not say which, so the document is at best 0.1 %
from its stated constraint and at worst silently in breach of it — and it cannot be told apart,
because nothing measures it. Only check 6 touches this file, at 61440 B / 750 lines, which it is
nowhere near.

**A tracked row records the wrong half.** `memory/backlog/TOOL.md:26`, `TOOL-dHonouredPark-2`
(CLOSED): *"BUILD-METHOD.md's declared budget rises to 350 lines (owner, 2026-08-25), from 310, which
it was already 2 over at 470bb09b. The raise fixes the breach and NOT the blindness: M1 declares the
pair and no gate enforces it, which is why a governance carrier sat over its own stated constraint
unnoticed."* The LINE half was raised to 350 and now has 33 lines of slack. Nobody re-examined the
BYTE half, and the file itself says that is the one that binds. The row's description — a line breach
— is no longer the live condition. **The row got worse and changed shape.**

The remedy is one row in `tools/template-size-limits.txt` (with the ambiguity resolved in the same
edit) and one leg in `tools/gate-legs.json`; the machinery already exists and already takes a
per-subject declared ceiling. `TOOL-dHonouredPark-2` explicitly parks that as "a separate question
nobody has been asked". Asking it is now overdue by 27 bytes.

---

## F6 — "48 KiB" is typed in three prose carriers beside the file that owns it, and it has already moved once. **medium**

| carrier | text |
|---|---|
| `AGENTS.md:17` | "the operating ruleset; **≤48 KiB, gated** by `tools/check-template-size.sh`" |
| `AGENTS.md:575` | "The template is the operating ruleset — keep it ≤48 KiB" |
| `memory/guides/SESSION-KICKOFF.md:194` | "The template is under a 48 KiB gate" |

The owner is `tools/template-size-limits.txt:27` (`coding-governance-agents.template.md	49152`),
whose header records that this value **moved once already**, 32768 → 49152 on owner order
(`TOOL-aSiftedPlaybook-1`). Every one of the three prose carriers would have been wrong for the
duration of that move, and `AGENTS.md:575` is 100 bytes in a file with 41 to spare.

`AGENTS.md:230` states the rule being broken: *"A value stated in prose beside the source that OWNS
it rots between changes — point at the source, or gate the pair. This is the same rule as 'derive
over author' … and it is the one most often broken by the document that states it."*

Safe cut: `AGENTS.md:575-576` loses only the digit — the rule ("the template is the operating
ruleset; anything activity-scoped goes in a companion") stays, and the number survives at
`tools/template-size-limits.txt:27` with its history and at `AGENTS.md:17`'s pointer to the gate. Not
tracked in either backlog (grepped `48 KiB`).

---

## F7 — The GATE_SELFTESTS owner ruling carries two different dates in two carriers. **medium**

- `AGENTS.md:484` — `GATE_SELFTESTS=1 … # ON DEMAND ONLY: no boundary sets it (owner, **2026-08-27**)`
- `memory/guides/SESSION-KICKOFF.md:121` — `GATE_SELFTESTS=1 … both held by default (owner ruling **2026-08-26**). GATE_FULL does NOT unlock them. On demand only`

Same rule, same knob, two provenance stamps. Neither date resolves in `memory/DECISIONS.md` under a
`GATE_SELFTESTS` search (`grep -rn "GATE_SELFTESTS" memory/DECISIONS.md memory/decisions/` — no
hits), so a reader cannot adjudicate from the log either. §6 requires that "non-obvious rules carry
provenance inline (the motivating decision/incident id)" — an id would have made this unambiguous;
two bare dates make it worse than none.

This is the predicted failure of the duplication underneath it: the gate-command catalog is stated
twice, at `AGENTS.md:479-485` and `memory/guides/SESSION-KICKOFF.md:117-125`, plus a third abbreviated
copy at `AGENTS.md:226` (the rendered `{{EVERYDAY_COMMANDS}}` value). I am **not** proposing to cut
the manifest's copy — front-loading the gate commands is the manifest's declared job (§1 DoD names
"a gate command" as manifest content). The fix is to make one carrier own the ruling's date and the
other point at it.

---

## F8 — `AGENTS.md:529-530` keeps a 190-byte measurement it declares obsolete in the same sentence. **low**

```
The only cold/warm pair on record is node `a`, 2026-08-21: 393 s warm against 432 s with the dispatch
hint removed. It describes a bar that no longer exists.
```

Class (c) history, and of the *non*-load-bearing kind: it stops nobody from "fixing" a rule back,
because there is no rule — it is two numbers plus a disclaimer that they describe a system that is
gone. The paragraph immediately above it already tells the reader where live per-leg timing lives:
*"`<git-dir>/gate-ledger.tsv` carries one row per leg with its own seconds … Read it there."* The
figures themselves survive in git history and in the build record that measured them.

**Deliberately distinguished from a protected row.** `memory/backlog/TOOL.md:90`
(`TOOL-aTimedTurnstile-4`) protects a *different* cold/warm pair — 607.3 s vs 382.1 s, plus spawn-tax
figures — and says explicitly they "are load-bearing elsewhere and must not be edited away". That row
is the surviving carrier for those numbers; the 393/432 dispatch-hint pair is not in it.

190 bytes, in a file with 41. Small, but it is the cleanest cut in the corpus: the document itself
certifies the bytes carry nothing.

---

## F9 — The second- and fifth-largest instruction documents have no ceiling at all, and the largest guide is at 92.9 % of its. **low**

- `WIRE-INTO-PROJECT.md` — 59833 B / 816 lines. No row in `tools/template-size-limits.txt`, none in
  `tools/line-length-limits.txt`, not under `MEMORY_ROOT` so check 6 never sees it. It is the agent
  runbook for wiring the whole chain into a target repo, i.e. the document a deploying agent reads
  end to end. Grepped: `grep -rn "WIRE-INTO-PROJECT" tools/template-size-limits.txt
  tools/line-length-limits.txt tools/gate-legs.json .memory-tree.conf` → no output.
- `.claude/skills/unattended/SKILL.md` — 48767 B / 731 lines, larger than the 48 KiB charter cap,
  rendered from `tools/unattended/SKILL.template.md`. Uncapped. It declares itself "the operating
  summary" of `memory/guides/UNATTENDED-PROTOCOL.md` (57098 B) — a summary at 85 % of its source's
  size. An unattended run reads both: ~106 KB before it does anything.
- `memory/guides/UNATTENDED-PROTOCOL.md` — 92.9 % of `GUIDE_CAP_BYTES` and **52 lines** under
  `GUIDE_CAP_LINES`. It is the only guide anywhere near either bound; the next is `BUILD-METHOD.md`
  at 40 %.

I checked whether the SKILL is a copy-paste of the protocol and it is **not** — longest shared word
run is 20 words, 21 merged shared spans ≥9 words totalling ~250 words out of 7896. It is a genuine
re-derivation. That makes it *harder* to trim safely, not easier, and I am not proposing a cut. The
finding is the missing bound: the two documents that grow fastest are the two nothing measures.

---

## What I looked at and am refusing to propose

- **The lexicon rationale in charter §12 vs `.claude/skills/lexicon/SKILL.md`.** Three spans totalling
  68 words are shared verbatim ("which verb is this?" is answerable only when a function does ONE
  thing…; a row with only a positive gloss cannot tell two verbs apart; if the reflex on a refusal is
  to add a verb, the table has become a synonym list). Real duplication, ~600 bytes, and cutting it
  from the charter would buy fifteen times the current margin. **Refused:** the Skill loads only when
  the skill system triggers it; the charter is read every turn. An agent naming a function without
  invoking `/lexicon` would lose the scoping rule entirely, and no gate would catch the loss. That is
  the catastrophic-regression case the brief describes.
- **The charter §8 agent-cap bullet vs `memory/guides/REVIEW-PROTOCOL.md`.** Deliberate, and
  machine-compared: `tools/check-playbook-parity.sh` pins five of its values,
  `tools/check-agent-cap-restatement.sh` bans a bare digit anywhere in live prose. The restatement is
  gated, so it is not a rot risk.
- **`AGENTS.md:472-476`'s "this section used to enumerate all seventy…"** — class (c) history that
  **is** load-bearing: it stops a future session re-adding the leg list. Keep.
- **`AGENTS.md:519-527`'s 2026-08-23 timing paragraph.** Dated, explicitly historical, and it carries
  a live decision rule (a 1565 s leg puts a 26-minute floor under any full run; the distribution is a
  handful of suites and a long tail). Keep. Worth noting that `AGENTS.md:517-518` says *"Do not read a
  leg COUNT out of this paragraph"* and the next paragraph opens with "Fifty of the ninety-two legs";
  it is saved only by "then present". `tools/gate-legs.json` now holds 86.
- **`memory/guides/BUILD-METHOD.md` M11's six-carrier list vs the memory-tree README's pointer table.**
  M11 says "Names here, scopes there" — the split is declared and the overlap is names only. Keep.
- **Reflow, tightening, emphasis, section merges.** Not proposed, per the brief.
