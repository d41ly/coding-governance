# wave2 — charter fidelity: does `AGENTS.md` still describe this repo?

**Serves:** research TOOL-aScouredKit-1

## Verdict: CLEAN WITH FIXES

**Lens:** charter-fidelity. **Subject:** `AGENTS.md` at HEAD (`66c4891c`), plus the secondary
governance docs it points at and the gates that police them.
**Method:** every checkable factual assertion in the 581-line auto-loaded charter, run against the
tree. Path existence machine-derived; every count re-derived from its authoritative source; every
prescribed command actually executed.

## What is healthy — stated first, because a finding list reads as a verdict on the whole document

These were checked and are **correct**, so nobody re-checks them:

- **Every in-repo path the charter names resolves.** A script extracted 86 distinct path-shaped
  backticked tokens from `AGENTS.md` and resolved each against the tree; the only non-resolving ones
  are placeholders (`<git-dir>/…`, `builds/<slug>/`), prefix-relative kit names, and non-paths. Twenty
  load-bearing ones were then checked individually (`tools/run-gates/gate-profiles.txt`,
  `tools/unattended/run-unattended-gates.sh`, all three `memory/guides/*.md` protocols,
  `tools/hooks/agent-cap.js`, `skills/session-kickoff/manifest-check.sh`, `memory/map/baseline.toml`,
  …): **20 of 20 exist.**
- **The rendered region is byte-faithful.** `bash tools/playbook/adopt-playbook.sh --target . --check`
  → `render-playbook OK — region matches a fresh render, no placeholder survived`. So no finding below
  is "somebody hand-edited the charter"; the render is honest and the *answers* are what is wrong.
- **`GATE_FULL` / `GATE_SELFTESTS` semantics (`AGENTS.md:483`) are exactly right.**
  `tools/run-gates/run-gates.sh:947` is literally
  `if { [ "${subjects[$i]}" = kit ] || [ "${chunks[$i]}" = selftests ]; } && [ -z "${GATE_SELFTESTS:-}" ]`.
- **The unattended-removal claim (`AGENTS.md:512`) holds.** "What stayed are the three legs whose
  subject is the REPOSITORY" — `tools/gate-legs.json` carries exactly 3 unattended-touching legs
  (`unattended kit gate`, `playbook validity gate`, `unattended skill wiring`), all `subject: repo`.
- **The four dogfooded gates named at `AGENTS.md:4-6` all exist as legs**: `memory hygiene`,
  `kickoff-manifest ratchet`, `charter size`, `codebase-map coverage + freshness`.
- **The agent-cap bound claims are gated and green.** `agent-cap.js` holds `CAP = 5`,
  `MAX_VERIFIERS = 5`, `MAX_LENSES = 5`; `bash tools/check-playbook-parity.sh` →
  `playbook-parity OK — 15 kit(s) documented or waived · pairs in agreement`.
- **`memory/project/` really does hold `*.txt` waiver registries "and nothing else"** (9 files, all
  `.txt`). The `streams` enum at `AGENTS.md:53` matches `.memory-tree.conf:11` exactly.
- **`tools/check-microformats.sh` is a well-built gate** — it derives its keyword set from the block
  it grades rather than mirroring it, pins a `SENTINEL` against an empty derivation, and states what
  it does not check. No finding.
- **Wiring is live.** `bash tools/check-wiring.sh --session` → all `ok` rows; `core.hooksPath` set;
  the three CRLF `note` rows are the already-known working-copy artifacts.

Nine findings follow. Five are cases of the charter asserting a structure that does not exist; two are
hand-kept inventories drifting from their authoritative source; one is a prescribed command that does
not run; one is a mechanism claim falsified by the workflow the same charter mandates.

---

## F1 — `AGENTS.md:223` sends every session, at session start, to a directory that does not exist

**blocker.**

**What the record says.** `AGENTS.md:222-223`, §6, the section the charter itself designates as
session-start reading:

> - Session-start reading order: ALWAYS load the master decision index first, then the stream logs for the area touched …
> - Logs are two-tier for token scoping: a one-line-per-decision index pointing at per-decision detail files; open details only for the areas you touch.

`memory/DECISIONS.md:5` repeats it from the other side:

> One line per decision, APPEND-ONLY, every family in one file. Detail in `decisions/`.

**What is actually true.**

```
$ ls -d memory/decisions
ls: cannot access 'memory/decisions': No such file or directory
$ git ls-files | grep "decisions/" | head
(no output)
$ git ls-files memory/ | wc -l
945
```

Zero of 945 tracked files under `memory/` sit in a `decisions/` directory, anywhere. There is no
second tier. There are also no per-stream "stream logs" — `memory/DECISIONS.md` is one flat
120-line file holding every family, which is what `AGENTS.md:68` says in the preamble:

> One append-only `memory/DECISIONS.md`; backlogs shard per family at `memory/backlog/<FAMILY>.md`.

So `AGENTS.md:68` and `AGENTS.md:223` describe two different memory topologies, in one auto-loaded
file, and the preamble is the one telling the truth.

**Why this is the serious class and not "merely old".** This is not an append-only record superseded
by a later id, and it is not under `archive/`. It is a live directive in the section that governs how
a session *begins*. Its behavioural instruction — "open details only for the areas you touch" — is
the token-scoping strategy §14 leans on. A session that obeys it goes looking for
`memory/decisions/TOOL-aScouredKit-11.md`, finds nothing, and has to improvise; a session that
disobeys it reads the whole index. Either way the rule is dead text that every session pays to load.

**Fix.** Rewrite §6's two-tier bullet to describe the flat index this repo actually keeps (or
route it through a placeholder answered in `deploy.toml`, since the two-tier shape is a legitimate
option for an adopter). Delete `Detail in \`decisions/\`.` from `memory/DECISIONS.md:5`.

---

## F2 — the charter prescribes a command that exits 2, to print numbers it never prints

**blocker.**

**What the record says.** `AGENTS.md:6-9`, the opening paragraph:

> The map lives at `memory/map/`; its dossiers are the files under `memory/map/features/`, and the
> keys not yet claimed by one are in the `baseline.toml` … Both counts move as dossiers land, so
> neither is spelled here — `python tools/codebase-map/reuse_lookup.py` prints the live pair.

**What is actually true.**

```
$ python tools/codebase-map/reuse_lookup.py
usage: reuse_lookup.py [-h] query [query ...]
reuse_lookup.py: error: the following arguments are required: query
$ echo $?
2
```

And the tool is not a counter at all. Its own `--help`:

> reuse-lookup — the behaviour->seam discovery entrypoint … Assembles a candidate corpus from the
> map's four recall sources … and prints a ranked SHORTLIST for an agent to read.

Given a query it prints seams. It prints neither the dossier count nor the unclaimed-key count, with
or without arguments. No command in `tools/codebase-map/` prints that pair — `gen_map.py` has
`--scaffold/--write/--check/--seed-*`, `map_diff.py` takes a git range and prints a coverage
percentage over that range, not the map totals. The true pair today has to be counted by hand:
18 dossiers under `memory/map/features/`, against the key lists in `memory/map/baseline.toml`.

**Why this matters more than a broken one-liner.** The charter chose to *not spell* two numbers —
correctly, per its own `AGENTS.md:228-230` rule — and delegated them to a command. The delegation
target is wrong, so the numbers are now unavailable rather than merely unstated. That is strictly
worse than the stale-prose problem it was avoiding: a stale number is visibly checkable, an
unrunnable delegation just fails.

**This already caused damage inside this very audit.** The orchestrator's commissioning brief for
this wave repeats the charter's instruction verbatim — "`python tools/codebase-map/reuse_lookup.py`
gives further live figures" — and it does not. The false record propagated into the brief of the
audit sent to find it.

**Fix.** Either point at a command that prints the pair, or add a `--counts` mode to `gen_map.py` and
point at that. Do not replace it with two numbers in prose.

---

## F3 — §2's node registry holds one row; this repo has four nodes, and the template cannot express more

**high.**

**What the record says.** `AGENTS.md:151-155`, §2, under "Register every node once, in-repo":

```
  | Tag | Machine/user | Primary tree (`main` lives here) | Worktree root | Variances |
  |-----|--------------|----------------------------------|---------------|-----------|
  | `a` | `daily-agent` | `C:/projects/coding-governance` | `C:/projects/coding-governance/.claude/worktrees` | remote `origin`; … |
```

One row. `AGENTS.md:158`, three lines later:

> - A new node claims the lowest free one-letter lowercase tag and adds its row in the same commit.

**What is actually true.** `AGENTS.md:60-65`, the gov-authored preamble above the rendered region,
carries a *second* table headed `## Node registry` with **four** rows — `a` daily-agent, `b` agent5 @
`DESKTOP-3J1O6CD`, `c` agent-0 @ `DESKTOP-8BKM8GN`, `d` d41ly. The fleet is four. Both tables are in
the same auto-loaded file and they disagree on cardinality and on columns.

**Why the render cannot fix it.** `coding-governance-agents.template.md:83` hard-codes exactly one
row of placeholders:

```
  | `{{TAG_A}}` | `{{MACHINE_A}}` | `{{PRIMARY_TREE_A}}` | `{{WORKTREE_ROOT_A}}` | {{VARIANCES_A}} |
```

`tools/govkit/entries/playbook.kit.toml` declares `MACHINE_A` (:125) and `VARIANCES_A` (:144) and
no `_B`/`_C`/`_D` siblings. `.governance/deploy.toml` answers `machine_a` and `variances_a` and
nothing else — correctly, because there is nothing else to answer. So §2's registry is
*structurally* incapable of holding a fleet, and gov's workaround was to author a parallel table
above the marker region. That is two answers to one question, which `AGENTS.md:228-230` forbids by
name.

**The concrete wrong action.** A session on node `b`, `c` or `d` that reads §2 — the numbered,
binding ruleset — finds no row for itself, and `:158` instructs it to "claim the lowest free
one-letter lowercase tag and add its row in the same commit". The lowest free tag *per §2* is `b`,
which node `b` has held since before this build started. The rule as written produces a tag
collision, which is the exact class §2 exists to make impossible.

**Fix.** Make the registry a repeating block the renderer can emit N times from a `nodes` array in
`deploy.toml`, and delete the hand-authored preamble table. Until then, at minimum, make §2's table
point at the preamble table so a reader is not looking at a one-row fleet.

---

## F4 — §8 routes Tier-2 review artifacts to `memory/reviews/`, which does not exist and which the charter's own layout section forbids

**high.**

**What the record says.** `AGENTS.md:318`, §8:

> - Persist each Tier-2 run as an in-repo artifact folder (`memory/reviews/`); periodically re-audit the corpus …

**What is actually true.**

```
$ ls -d memory/reviews
ls: cannot access 'memory/reviews': No such file or directory
$ git ls-files 'memory/builds/*/reviews/*' | wc -l
223
```

**223 of 223** tracked review records live under `memory/builds/<slug>/reviews/`. Zero live at
`memory/reviews/`. This very file is being written to
`memory/builds/aScouredKit/reviews/`, per the orchestrator's instruction — i.e. the operating
practice and the charter directive already disagree and everyone quietly follows the practice.

And `AGENTS.md:52-53`, the layout section of the same file, states the rule the practice follows:

> Specs, reports, research and reviews live under a build's own folder, **NOT the root**.

So `AGENTS.md:318` contradicts `AGENTS.md:52` directly.

**Root cause, which is the interesting part.** `REVIEW_DIR` is declared in
`tools/govkit/entries/playbook.kit.toml:219-222` as `class = "defaulted"`, `default = "memory/reviews/"`.
`.governance/deploy.toml` never answers it. The comment sitting immediately above that declaration,
at `playbook.kit.toml:210-211`, describes this outcome in advance:

> defaulted — a declared default applies, and the render RECORDS that it defaulted. **A default
> silently identical to an answer is how an operator ships a value they never chose.**

gov shipped a value it never chose, into its own charter, past the mechanism it built to prevent
exactly that. The render is not at fault — `adopt-playbook.sh --check` is green — the missing answer
is.

**Fix.** Add `review_dir = "memory/builds/<slug>/reviews/"` to `.governance/deploy.toml [answers]`
and re-render. Consider promoting `REVIEW_DIR` from `defaulted` to `asked`, since a defaulted
directory convention is unverifiable by construction.

---

## F5 — six live cross-references to three sections deleted at v3.0, two of them in §0's TL;DR

**high.**

**What the record says.** Six bullets cite `§4`, `§13`, `§17`:

| line | text (abridged) |
|---|---|
| `AGENTS.md:94` | "…isolate *runtimes* too: ports/DBs per session (**§4**)." — §0 TL;DR |
| `AGENTS.md:99` | "**Verify before claiming done** — a check that exercises the change… (**§4**, §8)." — §0 TL;DR |
| `AGENTS.md:100` | "**Consistency by construction**: build tokens, primitives, and factories *before* the screens… (§12, **§13**)." — §0 TL;DR |
| `AGENTS.md:231` | "(User-facing links follow **§17**, a different convention.)" |
| `AGENTS.md:321` | "…its own/affected test, the relevant gate, or the **§4** harness…" |
| `AGENTS.md:390` | "…system-first UI (§12, **§13**)…" |

**What is actually true.** `grep -n "^## §" AGENTS.md` returns
§0,1,2,3,5,6,7,8,9,10,11,12,14,15,16 — **§4, §13 and §17 do not exist.** They existed through v2.7:

```
$ grep -n "^## §" memory/archive/parallel-coding-governance.template-v-2-7.md
 94:## §4 — Runtime isolation & the verification harness
177:## §13 — Visual consistency (design system FIRST, before screens)
227:## §17 — User-facing file references (make them clickable)
```

They were removed in the v3.0 convergence and the six citations were not.

**This is not the append-only-supersession class.** A decision log superseding an id is designed
behaviour; a live directive pointing at a section that was deleted from the same document is a
dangling pointer. The distinction is that nothing here was superseded — §4's content was dropped,
and §17's merged into §16's link rule (`AGENTS.md:467-469`), so the pointer has a correct target
nobody repointed it at.

**Blast radius beyond this repo.** All six survive verbatim in
`coding-governance-agents.template.md` (:18, :23, :24, :161, :253, :328), so **every adopter's
rendered charter carries them**. Two of the six are in §0, the ten-bullet "load-bearing rules"
summary that is the first thing any session reads.

**Why no gate caught it.** `tools/check-dead-paths.sh` was built for precisely this class — its
header (`:11-16`) names "the v3.0 charter convergence, which deleted two companion files" as its
motivating incident — but its own "WHAT IT DOES NOT CATCH" paragraph (`:35-42`) explains the miss:
it matches **filenames**. A `§`-reference is not a filename. The gate is honest about its blind
spot; the blind spot is just occupied.

**Fix.** Repoint `§17` → `§16`; drop the `§4` and `§13` citations or restore stub sections. This is a
five-line predicate — every `§N` cited must have a matching `^## §N` heading — and it belongs on the
bar, in both the template and the rendered charter.

---

## F6 — the charter delegates the hygiene check count to two carriers; one states no count and the other disagrees with the front door

**medium.**

**What the record says.** `AGENTS.md:204-209`, §5:

> …and a **hygiene gate** whose check count is stated by the kit README and the gate-leg name and is
> deliberately not restated here…

The intent is right and matches `AGENTS.md:228-230` ("point at the source"). The problem is that one
of the two named carriers does not carry it, and the ecosystem around the other has drifted.

**What is actually true.**

1. **The gate-leg name states no count.** The manifest holds exactly two hygiene legs:
   ```
   $ python -c "import json; [print(repr(l['name'])) for l in json.load(open('tools/gate-legs.json')) if 'hygiene' in l['name']]"
   'memory-hygiene self-test'
   'memory hygiene'
   ```
   Neither carries a number. (This is not a silly expectation — counts-in-leg-names is a live pattern
   in this manifest: `kickoff engine size <=18KiB` is a leg name.) So half of the charter's stated
   delegation is fictional.

2. **The two prose carriers disagree by two.**
   - `tools/memory-tree/README.md:18` — the kit README, the carrier the charter names:
     "`check-memory-hygiene.sh` | the gate — **23 checks** (1-12, 21, 22 and 23 in the shell, 13-16
     delegated to `corpus_ids.py`, 17-19 to `gotchas.py`, 20 to `row_grammar.py`)…"
   - `README.md:33` — this repo's front door: "…and a **21-check** hygiene gate."

3. **The source settles it at 23.** `tools/memory-tree/check-memory-hygiene.sh:1167` and `:1288` both
   emit diagnostics naming `check 23`; `:35` documents `check 22`'s cutoff. Checks 22 and 23 exist;
   `README.md:33` predates them.

**Impact.** `README.md` is the repo's front door and the first thing a new node or an evaluating
adopter reads. It understates the gate by two checks. More structurally: because the gate-leg name
carries no count, the charter's delegation gives a reader exactly one usable carrier where it
promised two, and single-carrier prose counts are the thing that rots — which is what happened.

**Fix.** Delete the count from `README.md:33` and point at the kit README (one carrier, one fact), or
rename the leg to carry the count so the charter's sentence becomes true. Not both.

---

## F7 — §1's Definition of Done requires a `help/` page; there is no `help/`

**medium.**

**What the record says.** Two live directives.

- `AGENTS.md:120`, §1 Definition of Done: "- User-facing change → its `help/` page created/updated (§5)."
- `AGENTS.md:193`, §5: "…one concise task-oriented page per feature (*what · how · short example*) in
  `help/` + an index; update on change, REMOVE on feature removal; **a user-facing feature without an
  up-to-date page is not done** (§1)."

**What is actually true.** `ls -d help` → `No such file or directory`. There is no `help/` directory
and no index. `git ls-files` finds no such path.

**Root cause is the same as F4.** `HELP_DIR` is `class = "defaulted"`, `default = "help/"`
(`tools/govkit/entries/playbook.kit.toml:213-217`), and `.governance/deploy.toml` does not answer it.

**Why medium and not high.** The DoD bullet is conditional ("User-facing change →") and gov's
user-facing surface is its READMEs, so a session can reasonably read the bullet as not firing. But it
*does* fire: every kit here ships a README an adopter reads, which is a user-facing page by any
reading of §5. Today the rule is either dead or unsatisfiable, and both are bad in a DoD.

**Fix.** Answer `help_dir` in `deploy.toml` with the convention gov actually uses (per-kit
`tools/<kit>/README.md`), or drop the bullet via a `when:` fence. Leaving a DoD item pointing at a
directory that does not exist trains sessions to skim the DoD.

---

## F8 — "What ships here (the product)" names 13 of the 25 entries in the declared registry, and omits the merge bar

**medium.**

**What the record says.** `AGENTS.md:16-42`, the section titled "## What ships here (the product)",
is a hand-kept prose inventory. Across its three bullets it names 13 things that correspond to
registry entries: `playbook`, `playbook-render`, `kickoff-manifest`, `memory-tree`, `memory-recall`,
`codebase-map`, `drift-audit`, `agent-cap`, `review-harness`, `unattended`, `agent-instructions`,
`pytest-parallel-guardrails`, `check-wiring`.

**What is actually true.** `tools/govkit/registry.toml` — the authoritative declared population, the
one `AGENTS.md:250-253` (§7) mandates — holds **25** `[[entry]]` ids (`registry.toml:39-147`). The
charter's prose omits **12**:

`run-gates` · `lexicon` · `gate-lint` · `push-main` · `settings-merge` · `check-placeholders` ·
`check-line-length` · `check-microformats` · `check-testsuite-counts` · `check-kit-versions` ·
`check-install-prefix` · `check-agent-cap-restatement`

Two of those omissions are notable rather than pedantic:

- **`run-gates`** is the merge bar — the single most-invoked thing in this repo, given its own
  700-line section later in the same file. A reader building a model of the product from "What ships
  here" does not learn it is a shipped, installable kit.
- **`lexicon`** has its own `.lexicon.conf` (18 KB at repo root), its own rendered Skill, six
  kit-conditional bullets in §12 (`AGENTS.md:379-386`), a gate leg (`lexicon naming predicates`), and
  four of the eleven drift signals in the Tier-0 report. It is invisible in the product inventory.

**Why this is the recorded defect class.** §7 of this same charter (`AGENTS.md:250-253`) says:

> Deploy your own tooling as a DECLARED population, never a directory listing: a registry plus a
> descriptor each, **asserted against the tracked surface in both directions** — a new moving part
> reds until a declaration claims it…

`registry.toml` is that declaration and `tools/govkit/` asserts it against the tree. But the charter's
prose is a *third* copy of the same population, asserted against nothing. `check-dead-paths.sh` only
proves that names present in prose resolve; nothing proves that entries present in the registry
appear in prose. So the inventory can only ever drift downward, silently, which is what it has done.

**Fix.** Either replace the enumeration with a pointer ("the shipped population is
`tools/govkit/registry.toml`; read it there") — the same move `AGENTS.md:474` already makes for gate
legs and `:517` makes for leg counts — or add a leg asserting registry ⊆ charter prose. The pointer is
cheaper and cannot rot.

---

## F9 — "there is no staleness-drift class here" for hooks is false in the worktree workflow §3 mandates

**medium.**

**What the record says.** `AGENTS.md:537-539`:

> The active hooks are the tracked `.githooks/` dir via `core.hooksPath`, **not an out-of-tree copy,
> so there is no staleness-drift class here.**

**What is actually true.** In a worktree — which `AGENTS.md:175` mandates for *all* feature work
("feature work happens ONLY in sibling worktrees") — `core.hooksPath` is a per-worktree absolute path
into the **primary** tree:

```
$ git config --show-origin core.hooksPath
file:C:/projects/coding-governance/.git/worktrees/kit-adversarial-review-15ed31/config.worktree	C:\projects\coding-governance\.githooks
$ git -C C:/projects/coding-governance rev-parse --abbrev-ref HEAD
main
```

This worktree is on `branch/kit-adversarial-review-15ed31`. The hooks that will actually run on a
commit or push from here are `main`'s checkout of `.githooks/`, not this branch's. They are
byte-identical today (`diff -q` → identical), so nothing is currently broken — this is a latent
class, not a live failure.

**The concrete wrong action.** A session that edits `.githooks/pre-push` in a worktree — the only
place §3 lets it work — and then tests by pushing, is testing `main`'s copy. It gets a green that
proves nothing about its change, and the charter has told it in advance that this class does not
exist here, so it will not think to check. That is the "guard that shares state with the thing it
guards" shape §7 warns about, one level up.

**Fix.** Narrow the sentence: the claim that the tracked dir beats a `.git/hooks` copy is true and
worth keeping; the "no staleness-drift class" conclusion is not. Add the worktree caveat, or have
`check-wiring.sh --session` warn when `core.hooksPath` resolves outside the current worktree.

---

## Two things deliberately NOT reported

- **The three `.claude/skills/*/SKILL.md` CRLF notes** — confirmed as the already-known working-copy
  artifacts; `check-wiring.sh` states in its own output that they do not gate.
- **`AGENTS.md:549`'s "written nowhere else"** about the agent-cap constants is loosely false —
  §8 at `:302-303` does write `5` twice — but `tools/check-playbook-parity.sh` machine-compares those
  restatements against `agent-cap.js` and is green, so the risk the sentence exists to manage is
  actually managed. Prose imprecision over a gated value; not worth a row.
