# wave3 — lens: do the kits actually DO what they claim?

**Serves:** research TOOL-aScouredKit-2

## Verdict: CLEAN WITH FIXES

**Subject:** HEAD `73fc52cc`, whole product. **Node:** `a`, worktree `kit-adversarial-review-15ed31`.
**Axis:** behavioural correctness of the five kits whose OUTPUT a human acts on. Prior waves audited
the instruments (can a gate fail, is a count honest). This one asks whether the answers are right.

Everything below was RUN. Commands and their output are inline. The tree was clean before and after
(one `AGENTS.md` render was made and reverted with `git checkout --`; `git status --porcelain` empty).

---

## Verdict per kit

| kit | verb tested | verdict |
|---|---|---|
| `tools/memory-recall/query.py` | ranked retrieval over the decision corpus | **CLEAN** — 8/8 questions put the true record in the top 5 |
| `skills/session-kickoff/manifest-check.sh` | `--locations`, `--task-skeleton` | **CLEAN** — both agree byte-for-byte with the template, the live manifest and the engine |
| `tools/memory-tree/gotchas.py` | `--for-diff` / `--for-paths` | **selection tracks input**, but one record's anchors invert its own stated intent |
| `tools/playbook/` | render into a target | **two defects**, one of them a red merge-bar leg at HEAD |
| `tools/codebase-map/reuse_lookup.py` | inventory + dossier halves | **stemmer defect** that also disables the `--converge` collision gate |

---

## F1 — BLOCKER. The unguarded bar leg `playbook render wiring` is RED at HEAD.

```
$ git rev-parse --short HEAD
73fc52cc
$ git status --porcelain      # (empty)
$ bash tools/playbook/adopt-playbook.sh --target . --check
render-playbook: DRIFT — the charter region differs from a fresh render
rc=1
```

That command is a merge-bar leg verbatim, and it carries **no guard**, so it runs on every bar
including the push boundary:

```
$ python -c "import json;d=json.load(open('tools/gate-legs.json'));..."
{"name": "playbook render wiring",
 "argv": ["bash","tools/playbook/adopt-playbook.sh","--target",".","--check"],
 "chunk": "wiring", "subject": "repo", "ceiling": 300}
```

**The one differing byte range.** Rendering and diffing:

```
$ python tools/playbook/render_playbook.py --target .
  ...
  DEFAULTED REVIEW_DIR = memory/reviews/   (no answer supplied)
$ git diff AGENTS.md
-- Persist each Tier-2 run as an in-repo artifact folder (`memory/builds/<slug>/reviews/`); ...
+- Persist each Tier-2 run as an in-repo artifact folder (`memory/reviews/`); ...
```

**Provenance — HEAD broke it, and the commit message names the class.** `REVIEW_DIR` is a
`defaulted` placeholder whose default lives at `tools/govkit/entries/playbook.kit.toml:221`:

```toml
key = "REVIEW_DIR"
class = "defaulted"
default = "memory/reviews/"
```

`.governance/deploy.toml` supplies no `review_dir` answer (`grep -n review .governance/deploy.toml`
returns only unrelated lines). At the parent commit the two agreed:

```
$ git show 66c4891c:AGENTS.md | grep -n "Persist each Tier-2 run"
318:- ... (`memory/reviews/`); ...
$ grep -n "Persist each Tier-2 run" AGENTS.md
320:- ... (`memory/builds/<slug>/reviews/`); ...
```

HEAD hand-edited the rendered region — inside `<!-- gov:playbook -->` — to correct a path that does
not exist, and did not move the source that owns the value. `git show --name-only HEAD` touches
neither `playbook.kit.toml` nor `deploy.toml`. The commit's own message says
"this repo's render was hand-filled with a path that never existed", which is exactly what it then
did again, one layer up.

Worse than the red leg: the next `adopt-playbook.sh --target .` **silently reverts** HEAD's
correction, because the render is authoritative over the region.

**Fix.** Add to `.governance/deploy.toml` under `[answers]`:
`review_dir = "memory/builds/<slug>/reviews/"`. Leave the descriptor default alone — `memory/reviews/`
is a reasonable default for a foreign adopter with no build-folder convention; the wrong thing here
is gov having no *answer*. Then re-run the leg to 0. (Second-order: nothing gates a hand edit inside
the rendered region against the renderer, which is why this survived a commit that was specifically
hunting this class.)

---

## F2 — HIGH. `kit:unattended` drops one bullet and leaves the whole ruleset standing; the renderer reports it as dropped.

**Method.** A scratch target repo with `.governance/deploy.toml` copied from gov's and edited to
`kits = ["playbook","playbook-render","memory-tree","run-gates"]`, i.e. no `unattended`, no
`codebase-map`, no `lexicon`; `drop_blocks = ["security-outbound","cross-os"]`.

```
$ python tools/playbook/render_playbook.py --target <scratch>/target
  ...
  dropped   kit:codebase-map
  dropped   kit:lexicon
  dropped   kit:unattended
  dropped   when:cross-os
  dropped   when:security-outbound
render-playbook — wrote the gov:playbook region into .../AGENTS.md

$ grep -n -i 'lexicon' AGENTS.md          # (nothing — correctly gone)
$ grep -n -i 'codebase[- ]map' AGENTS.md  # (nothing — correctly gone)
$ grep -n -i 'unattended' AGENTS.md
56:applies only when the project adopts the unattended-run kit — drop it otherwise.*
62:**Unattended runs** *(kit-conditional — drop this block if the project does not adopt the unattended-run kit).*
64:- The contract is `memory/guides/UNATTENDED-PROTOCOL.md`, installed by the kit: the committed
```

**Cause.** The fence spans three lines:

```
$ grep -n "kit:unattended\|Two independent blocks\|Unattended runs" coding-governance-agents.template.md
55:<!-- kit:unattended -->
57:<!-- /kit:unattended -->
63:*Two independent blocks. The first applies whenever the project keeps a kickoff manifest. The second
70:**Unattended runs** *(kit-conditional — drop this block if the project does not adopt the unattended-run kit).*
```

Only the single Landing bullet at `:56` is fenced. The block at `:70–76` — the one whose own text
says *"drop this block if the project does not adopt the unattended-run kit"* — is outside every
fence, and so is the note at `:63–64` that tells the reader the same thing about both halves.

**What an adopter ships.** A charter with a "**Unattended runs**" section pointing at
`memory/guides/UNATTENDED-PROTOCOL.md`, a file only the unattended kit installs, plus two
hand-deletion instructions — in the one file whose README says filling it "is a program's job and
not a reader's".

**And it reads as success.** The render prints `dropped   kit:unattended`, and:

```
$ python tools/playbook/render_playbook.py --target <scratch>/target --check
render-playbook OK — region matches a fresh render, no placeholder survived
```

Nine lines of the block survive against one dropped. The same shape applies to the
"**Kickoff-manifest merge exception**" half at `:66–68`: declared conditional in prose, no fence, no
`kit:kickoff-manifest` fence anywhere in the template.

**Fix.** Move the `<!-- /kit:unattended -->` close from `:57` to after `:76`, or open a second
`kit:unattended` fence around `:70–76` and drop the two prose "drop this block" sentences (a fence
makes them dead text). Add a `kit:kickoff-manifest` fence around `:66–68` and rewrite the `:63–64`
note as two per-fence sentences that live inside their own fences.

*(Not claimed: the many kits with no fence at all — `pytest`, `gate-lint`, `agent-cap`. The README
declares that most kits carry no conditional ruleset and grades `kits` against the registry instead.
The unattended block is different because it is fenced HALFWAY and self-declares as droppable.)*

---

## F3 — HIGH. `stems()` splits singular from plural, and `--converge` misses the collision it exists to catch.

`tools/codebase-map/map_lib.py:621` documents `stems()` as *"the one definition of 'lexically
related' used by the lookup shortlist AND the --converge collision check, so a match means the same
thing in both."* The stemmer strips ONE suffix, longest-first (`_STEM_SUFFIXES`, `:591`), and the
list holds `sion`/`tion`/`ment` at length 4 but only `s` at length 1.

```
$ python -c "import sys;sys.path.insert(0,'tools/codebase-map');import map_lib as m;..."
decision     -> ['deci']     decisions     -> ['decision']     <-- DIFFERENT
version      -> ['ver']      versions      -> ['version']      <-- DIFFERENT
session      -> ['ses']      sessions      -> ['session']      <-- DIFFERENT
extension    -> ['exten']    extensions    -> ['extension']    <-- DIFFERENT
permission   -> ['permis']   permissions   -> ['permission']   <-- DIFFERENT
class        -> ['clas']     classes       -> ['class']        <-- DIFFERENT
gate         -> ['gat']      gates         -> ['gat']          (ok)
record       -> ['record']   records       -> ['record']       (ok)
```

Scanning 400 tracked files for singular/plural pairs that both occur and do NOT share a stem, by
combined frequency:

```
           session ( 1174)  vs  sessions     (  103)   ['ses']      / ['session']
          decision (  731)  vs  decisions    (  440)   ['deci']     / ['decision']
           section ( 1010)  vs  sections     (  148)   ['sec']      / ['section']
           comment (  854)  vs  comments     (  101)   ['com']      / ['comment']
           version (  718)  vs  versions     (  188)   ['ver']      / ['version']
         assertion (  509)  vs  assertions   (  188)   ['asser']    / ['assertion']
          question (  451)  vs  questions    (  240)   ['ques']     / ['question']
       measurement (  619)  vs  measurements (   52)   ['measure']  / ['measurement']
          function (  272)  vs  functions    (   19)   ['func']     / ['function']
          argument (  360)  vs  arguments    (   24)   ['argu']     / ['argument']
   ... 10 more
```

**The measured wrong answer**, on `detect_collisions` (`map_lib.py:1205`), the S5 reinvention
detector behind `map_diff.py --converge`:

```python
base=[{"id":"read_decision","file":"a.py","kind":"function"}]
new =[{"id":"load_decisions","file":"b.py","kind":"function"}]
ref ={"read_decision":{"a.py","c.py","d.py","e.py"}}          # fan-in 3 -> a real seam
m.detect_collisions(new,base,ref,{},threshold=3)   ->  []          # MISS

# control: rename the existing seam to the plural, change nothing else
base2=[{"id":"read_decisions",...}]
m.detect_collisions(new,base2,ref2,{},threshold=3)
  -> [CollisionFlag(new='load_decisions', resembles='read_decisions', fanin=3, ...)]
```

A function reinventing an existing seam is flagged or not depending on whether one of the two names
happens to be plural. `selftest.py:884–886` pins only `slugify`/`slug` and one negative; no arm
covers a plural, so the behaviour is unpinned as well as wrong.

**Fix (small).** Two lines in `_STEM_SUFFIXES`: add `"sions"`, `"tions"`, `"ments"`, `"ions"`,
`"ses"` so the plural strips to the same stem as the singular — or, cheaper and more robust, strip a
trailing `s` FIRST and then apply the existing longest-first pass. Add one selftest arm asserting
`stems("decision") & stems("decisions")` is non-empty, and run the candidate over the real symbol
table before wiring it (§7's own rule) — the near-miss list above is that run's input.

---

## F4 — MEDIUM. The dossier half of `reuse_lookup.py` returns half the map and misses the true home 2 in 10.

The reuse probe every design pass is required to run. Its `## sources to open` section is documented
as being *"in shortlist order"* (`reuse_lookup.py:356`), i.e. ranked. Ten behaviour phrases whose
true dossier I verified independently by reading `memory/map/features/*`:

| phrase | true dossier | rank | of |
|---|---|---:|---:|
| retrieve the decision records that answer a question, ranked | memory-recall | **MISS** | 6 |
| rank decision records for a plain english question | memory-recall | **MISS** | 4 |
| offline retrieval index over the memory tree | memory-recall | 4 | 13 |
| the closed verb table a function name must lead with | lexicon | 11 | 12 |
| naming convention gate for function verbs | lexicon | 13 | 15 |
| cap how many agents a fan-out may spawn | agent-cap | 3 | 7 |
| ratchet that reds on an unclaimed inventory key | codebase-map | 9 | 11 |
| audit the kickoff manifest stamp | session-kickoff | 8 | 8 |
| a committed build folder authorizes a merge with no owner turn | unattended | 1 | 17 |
| decide at the push boundary whether a full bar is owed | run-gates | 2 | 6 |

Top-3 in 3/10. Absent in 2/10 — including *"rank decision records for a plain english question"*,
which is `memory-recall`'s own one-line description. Median list length ~10 of 18 dossiers; one query
returned all 18.

**This is not the banked `fan_in` finding.** It is a recall measurement of a different output section
against verifiable ground truth, and it has its own named mechanism:

```
$ python -c "...m.stems('how does the gate decide whether a full bar is owed at the push boundary')"
['bar','boundary','decid','doe','full','gat','how','owed','push','wheth']
$ python -c "...m.stems('how does it do what they must not')"
['do','doe','how','must','not','they','what']
```

`_STOPWORDS` (`map_lib.py:583`) is 21 words and holds none of `how, does, do, whether, what, which,
when, why, must, can, may, should, not, they, their, are, has, have, been`. The tool's own input
contract is a plain-English behaviour phrase, so English function words are load-bearing retrieval
stems: in the run above, `session-kickoff` was seeded purely by `decid, wheth` — its dossier prose
contains "decide" and "whether". F3 supplies the other half (a query saying "decisions" cannot reach
a dossier saying "decision").

**Fix.** Extend `_STOPWORDS` with the interrogative/auxiliary set above and land F3's stemmer fix,
then re-run this ten-phrase table as the acceptance check. Both are single-line-ish edits to the
same file, and the table is a ready-made regression fixture.

---

## F5 — MEDIUM. A gotchas record's anchors invert the sentence that disclaims them.

`gotchas.py` derives anchors from every backticked path-like token in a record's body. Line 68–69 of
`memory/gotchas/amendment-leaves-its-other-half-standing.md`:

> The taken set is `memory/builds/` — where specs, their criteria and their revision logs live …
> It is **deliberately NOT** `memory/`, which would select on every note and index in the tree …

Both tokens are backticked, so the harvester takes both:

```
$ python -c "...; print([r['anchors'] for r in recs if 'amendment' in r['name']])"
['memory/', 'memory/builds/']
$ python -c "... selectable('memory/', git_ls_files, 'memory')"
memory/        selects 909   of 1186 tracked files
memory/builds/ selects 843
extra from the disclaimed anchor: 66
```

Live consequence — a diff touching the file every work-unit touches:

```
$ python tools/memory-tree/gotchas.py --for-paths memory/DECISIONS.md
# 2 class(es) selected by an anchor + 4 universal
- [ ] amendment-leaves-its-other-half-standing        <-- the record says this must not happen
- [ ] containment-tested-one-way
```

The author was alive to the hazard — three lines later the same record cites a review path
*"written without backticks so it stays evidence rather than becoming a fifth anchor"* — and the one
sentence they could not de-backtick is the one naming the anchor they were refusing.

`fold-text-is-unreviewed-surface.md` names the same danger from the other side (*"The spelling
deliberately NOT used is a build-directory token, which selects roughly two thirds of this tree…
noise on a checklist is how reviewers learn to skip the checklist"*) and it is right: `memory/builds/`
is 71% of the tree, and the `amendment` record uses it as its primary anchor.

**Nothing catches this.** `cmd_check` (`gotchas.py:256`) has an unanchored arm and an inert-anchor
arm; there is no over-broad arm. The module's docstring already accepts that `--for-diff`
over-selects, so this is not a surprise so much as an unbudgeted one — the `universal` list is
capped at 4 by `UNIVERSAL_BUDGET`, while a de-facto-universal anchor is uncapped.

**Fix (cheap).** Un-backtick `memory/` in that sentence — one character pair, and it restores the
record's stated set. **Fix (structural, optional).** Add a check-19 arm: a non-universal class whose
anchors select more than N% of tracked files reds, so a de-facto-universal record has to spend the
`UNIVERSAL_BUDGET` it is actually using. `memory/builds/` at 71% would red today, which is the point.

---

## F6 — LOW. A record states an anchor count the tool contradicts.

`memory/gotchas/fold-text-is-unreviewed-surface.md:49` opens **"The anchors, and why these three."**
and then explains three. The harvester derives four, because line 23 backticks the evidence path
`memory/builds/dFramedEntrypoint/reviews/2026-08-24-review-…-round2.md`. The generated index agrees
with the tool, not the prose:

```
$ grep -n "fold-text-is-unreviewed-surface" memory/gotchas/INDEX.md
30:| [fold-text-is-unreviewed-surface](…) | class | 4 | ...
```

An authored count beside a derived one — the repo's own `two-answers-to-one-question`, in the
catalogue that holds it. **Fix:** un-backtick the `:23` citation (matching what the `amendment`
record does deliberately), or replace "these three" with a count-free phrasing.

---

## Negative results, stated so they are not re-run

**`tools/memory-recall/query.py` — CLEAN.** Eight questions, each phrased in words a session would
use rather than the record's own words, each with a single true record established by grepping
`memory/DECISIONS.md`. Rank of the true record in the returned list:

| question | want | rank |
|---|---|---:|
| my git push failed with an auth error right after the gate passed | TOOL-aWarmedTether-2 | 2 |
| a timing check blocked a push on a slow machine | TOOL-cSteadyMetronome-1 | 1 |
| one branch moved a row and the other deleted it | TOOL-aMendedLedger-9 | 2 |
| can a run push its own authorization if the second anchor is enabled | TOOL-dNarrowedAnchor-1 | 1 |
| which is the binding budget for the build method guide | TOOL-dHonouredPark-2 | 3 |
| how does an unattended run handle the kickoff engine asking a question | TOOL-aUnmannedHelm-8 | 1 |
| should the recurring bug class section move into gotchas | PLAY-aCandidStub-1 | 1 |
| a CRLF file slipped past the wiring check | TOOL-aUnmannedHelm-10 | 4 |

8/8 in the top 5, 5/8 at rank 1–2. Index build 1.6 s, query 2.1 s cold over 791 records / 34,769
chunks. `--terms` were supplied as the contract requires. It beats grep on these, which is its claim.

**`skills/session-kickoff/manifest-check.sh` — CLEAN.** Both read-only verbs agree with every other
carrier:

```
$ diff <(bash skills/session-kickoff/manifest-check.sh --task-skeleton) \
       <(sed -n '/<!-- kickoff:task -->/,/<!-- \/kickoff:task -->/p' skills/session-kickoff/MANIFEST-TEMPLATE.md)
TEMPLATE MATCHES
$ diff <(… --task-skeleton) <(… memory/guides/SESSION-KICKOFF.md)
LIVE MANIFEST MATCHES
$ bash skills/session-kickoff/manifest-check.sh --locations
memory/guides/SESSION-KICKOFF.md
.claude/SESSION-KICKOFF.md
```

`SKILL.md:72` reads the verb rather than restating the list, `:76` names its fallback as a fallback,
and `:89` states plainly that the governance-doc fallback is engine-only and therefore *not* in
`--locations`. That last line is the shape most kits get wrong and this one gets right.

**`gotchas.py --for-paths` selection DOES track its input**, so the "decorative checklist" hypothesis
is refuted:

```
tools/unattended/check-unattended.sh    13 class(es) + 4 universal
tools/hooks/agent-cap.js                 2 + 4
tools/govkit/govkit.py                   1 + 4
memory/DECISIONS.md                      2 + 4
README.md                                0 + 4
tools/playbook/render_playbook.py        0 + 4
skills/session-kickoff/manifest-check.sh 0 + 4
```

Mean 1.2 classes per tracked file, median 1. F5 is a defect in one record, not in the mechanism.
