# Review aCandidStub-1 — convergence audit of the three governance playbook files

**Serves:** spec-audit PLAY-aCandidStub-1  <!-- inferred: this build defines exactly one spec id, so the record can serve nothing else -->

**Date:** 2026-08-10 · **Tier:** 2 · **Streams:** playbook
**Targets:** `parallel-coding-governance.template.md` (v2.4, 32083 / 32768 B — **685 B free**) ·
`parallel-coding-governance.customize.md` · `parallel-coding-governance.domain-rules.md`
**Question asked:** does the standing text still describe the repo as it is today?
**Commissioning concern:** recurring bug classes moved out of the doc templates into `memory/gotchas/`
and the playbook did not follow.

## 1. Verdict

The playbook is **converged on the axis it was commissioned for and diverged on the axis nobody was
watching**. Seven separate findings attacked the §10-vs-`memory/gotchas/` seam and every one was
refuted on the same solid ground: the memory-tree kit is marked *Optional* at `template.md:104`, so a
universal rule cannot name an optional kit's directory, and the two corpora are disjoint by written
charter — the only real defect there is a stale bullet count. What is genuinely broken is one level up:
**the deploy chain itself.** `customize.md` is the deploy authority for a three-file product and it
never names `domain-rules.md` even once, so the v2.3 externalization that moved six section bodies out
of the template was never reflected in the procedure that ships them — 13 of the 36 placeholders it
catalogues live only in a file its fill-and-verify step never opens (**id=23, blocker**), the companion
carries no version marker so a stale companion beside a fresh template is undetectable (id=25), and its
drop list still targets line-granular bodies that moved a version ago (id=26). Second-worst is the
§8 review-protocol text: a script written exactly to `template.md:146` is **DENIED at exit 2 by this
repo's own `agent-cap.js`**, because §8 names one of the two markers the hook requires (**id=28,
blocker**). Third is the memory-tree adoption path, which routes an adopter through a pre-flatten
`.memory-tree.conf.example` that the hygiene gate the same template advertises will red (id=16, id=7).
The routing layer between the template and its companion is the connective tissue that failed
everywhere: an orphaned §14 with a colliding number (id=2), two self-descriptions that undercount their
own file (id=3, id=4), and a droppable-set claim each file contradicts (id=24). Net: the *rules* are
sound; the *wiring between the three files* is a version behind.

## 2. Review shape

| raw | confirmed | refuted | unverified | precision | lenses |
|-----|-----------|---------|------------|-----------|--------|
| 34  | 15        | 19      | 0          | **0.44**  | 5/5 live |

Precision 0.44 sits just under the §8 ~0.5 floor (`template.md:148`), which the corpus itself explains:
seven of the nineteen refutations are one cluster (the §10/gotchas hypothesis, ids 1, 9-14) — the
commissioning brief primed every lens toward a thesis the artifact does not support. Excluding that
cluster, precision is 15/27 = 0.56. The lesson for the next audit of a *product* doc is the one the
refutations kept restating: a project-agnostic template stating a rule generically is not drift.

## 3. Findings, severity-ranked, grouped by axis

Severity legend: **B** blocker · **H** high · **M** medium · **L** low.
"Gate" = the left-shift check that would have caught the class mechanically. This repo already gates
doc claims (kit/dogfood parity, verdict epoch, codebase-map coverage); every gate below is the same
shape.

### Axis A — The deploy chain does not know the companion exists

The v2.3 externalization moved §4/§9–§13 bodies into `domain-rules.md`. `customize.md` never followed.
`grep -n 'domain-rules' parallel-coding-governance.customize.md` exits 1.

| # | Sev | Anchor | Says | Repo actually | Fix |
|---|-----|--------|------|---------------|-----|
| 23 | **B** | `customize.md:10` | Fill one file, then "`grep -nE '\{\{[A-Z]'` to confirm no placeholder survived" | 13 of the 36 catalogued placeholders (`{{PORT_OFFSET}}`, `{{VERIFY_RECIPE}}`, `{{KIND_FACTORY_MAP}}`, `{{TOKENS_LOCATION}}`, `{{TYPE_SCALE}}`, …) exist **only** in `domain-rules.md`; `WIRE-INTO-PROJECT.md:71-77` says the companion "MUST travel alongside" | Name both deployed files in the Who/how step; run the closing grep over BOTH; split the catalogue into a template group and a companion group |
| 25 | **H** | `customize.md:47` | Re-pull is defined over the template's `<!-- governance-template: vN.N -->` marker and a per-§-body diff of the template | `grep -c 'governance-template' domain-rules.md` → **0**. No marker, no re-pull step, no snapshot in `memory/archive/`. A v2.4 template beside a v2.2 companion is undetectable — and the template addresses the companion by section *number* | Stamp the same marker into `domain-rules.md`; extend §Re-pull to "diff both; both markers must read the same version" |
| 26 | **M** | `customize.md:39` | Drop entries name multi-bullet bodies — "**§9** lines about outbound calls / stored HTML", "**§4** harness lines and **§13** entirely" | Template §4 (91-93), §9 (157-159), §13 (173-175) are each a heading + ONE stub line; §11 (165-167) is a stub + two inlined rules. The bodies are at `domain-rules.md:7-16, 22-34, 85-94` | Re-target each entry at both files ("drop the template's §9 stub AND `domain-rules.md` §9"); note that dropping a stub alone orphans the companion section |
| 5 | **M** | `customize.md:50` | Snapshots live "under `memory/playbook/archive/` in this repo" | `ls memory/playbook` → No such file. Snapshots are at `memory/archive/parallel-coding-governance.template-v-2-0…2-3.md` | Correct to `memory/archive/` |
| 6 | **L** | `customize.md:26` | Dropping the kit means deleting "the two §5 memory-tree lines from the template" | §5 (lines 95-106) carries **one** memory-tree line (104). Two was true at v2.2 (`memory/archive/…-v-2-2.md:117-118`); the second bullet is gone by v2.3 | Name the bullet instead of counting it |

**Gate A1 — placeholder-coverage check.** Assert `{{X}}` ∪ over `template.md` + `domain-rules.md` ⊆ the
names catalogued in `customize.md`, **and** that every file contributing a placeholder is named in the
fill procedure. Catches id=23 the moment a placeholder moves file. Cheap: three greps and a `comm`.

**Gate A2 — version-marker parity.** `grep -o 'governance-template: v[0-9.]*'` over the template and
the companion must return the same string, both non-empty. Catches id=25 permanently, and reds the
first time either file ships without the marker. Same shape as `check-kit-versions.sh`.

**Gate A3 — dead-path check.** Extract every backticked path from the three files; each must resolve
in the repo, be a known adopter-target path, or be an unfilled `{{…}}`. Catches id=5 and id=21.

### Axis B — §8 prescribes a script the repo's own hook denies

| # | Sev | Anchor | Says | Repo actually | Fix |
|---|-----|--------|------|---------------|-----|
| 28 | **B** | `template.md:146` | "at most 5 verify agents TOTAL (batch grows, agent count does not)", enforced by a hook that "DENIES raw-primitive scripts"; names only the `gov:bounded-fanout` marker | A script written to §8's letter — inline `boundedParallel`, marker present, chunked into 5 batches, `batches.map(g => () => agent(...))` — was piped through the real `tools/hooks/agent-cap.js`: **exit 2**, "agent() fanned over `batches`, which this file does not show to be bounded". The hook needs a SECOND marker `gov:fixed-verifiers` (`agent-cap.js:95`) and one of two literal shapes, `chunk(x, Math.ceil(x.length / K))` or `splitInto(x, K)` (`agent-cap.js:133-134`). `grep -inE 'fixed-verifiers\|splitInto\|chunk\('` over all three playbook files → no hits. `tools/workflows/tier2-review.js:203` carries the marker; the playbook does not | Spell the second marker and the two accepted shapes verbatim in §8; correct "DENIES raw-primitive scripts" to "DENIES raw fan-out primitives AND any `agent()` fanned over a receiver it cannot prove bounded" |

Mitigating: the hook's denial text (`agent-cap.js:334-339`) prints the full remedy, so the adopter is
not stranded — the defect is that the *operating ruleset* is incomplete, not that it is a dead end.

**Gate B1 — doc-example conformance.** Extract the script shape §8 prescribes into a fixture and pipe
it through `tools/hooks/agent-cap.js`; the leg reds unless the documented shape exits 0. This is the
repo's own "a check that cannot fail is not a check" rule (`domain-rules.md:96`) applied to prose: the
playbook currently documents a recipe no gate ever executes — the exact hole
`adopt-codebase-map.test.sh` was added to close for the adopter script.

### Axis C — the adoption path hands out a pre-flatten tree

| # | Sev | Anchor | Says | Repo actually | Fix |
|---|-----|--------|------|---------------|-----|
| 7 | **H** | `customize.md:27` | `{{MEMORY_DISCIPLINES}}` = "space-separated discipline folders + their discipline→FAMILY id map" | `.memory-tree.conf:4-6`: "DISCIPLINES is a CLOSED ENUM of stream values, **NOT a list of directories**"; `FAMILIES` is a separate key (`:15`), shipped as two distinct keys by `adopt-memory-tree.sh:13-14` and `check-memory-hygiene.sh:21-22`. The template itself was updated at the flatten (`template.md:104`: "not a directory"); the customize text is verbatim pre-flatten wording preserved from `…-v-2-0.md:288` | Rewrite to a closed enum of stream values, with FAMILIES as its own key |
| 16 | **H** | `customize.md:30` | Adopt via `adopt-memory-tree.sh --scaffold` | The scaffolder copies `.memory-tree.conf.example`, whose own comments (`:8-9`, `:15`) still define "Discipline folders under `$MEMORY_ROOT/` … Each gets README.md + TREE.md + …" and `builds/YYYY-MM-DD-<FAMILY>-<slug>/`, and then tells the agent to "EDIT IT". Both shapes are rejected by `memory/HYGIENE.md` check 3 (sanctioned root set, no discipline dirs) and check 4 ("`builds/*` is the SLUG alone, no date and no family prefix"). A freshly scaffolded repo reds the gate the template advertises at `:104` | Re-render `.memory-tree.conf.example` to the flat shape; have this bullet name the conf keys the gate needs armed (SPEC_FORMAT_CUTOFF, STREAMS_CUTOFF, UNIVERSAL_BUDGET, the MEASURED pins) rather than implying MEMORY_ROOT + DISCIPLINES are the whole conf |
| 21 | **M** | `customize.md:30` | Command path is `tools/memory-tree/adopt-memory-tree.sh --scaffold` | The instantiating agent stands in the TARGET repo, where the kit lands at `<project>/memory-tree/`. `adopt-memory-tree.sh:6`'s own usage line is `memory-tree/adopt-memory-tree.sh --scaffold`; `WIRE-INTO-PROJECT.md:101-130` prescribes `cp -r <gov>/tools/memory-tree <project>/memory-tree` and hardcodes `"$top/memory-tree/check-memory-hygiene.sh"` in the pre-commit snippet. The script resolves its target via `git rev-parse --show-toplevel`, so running it from the gov clone scaffolds the wrong repo | Spell the target-repo path, or make the two shipped docs agree on one prefix and say which. The §5 `tools/` parentheticals (template 104-106) are this repo's source layout, not the adopter's — worth saying so |

**Gate C1 — scaffold e2e.** Scaffold into a temp repo with `adopt-memory-tree.sh --scaffold`, follow
the conf example's own documented meanings, then run `check-memory-hygiene.sh` — it must be green.
Catches id=16 and any future example/gate divergence. This is `adopt-codebase-map.test.sh`'s exact
argument: gate the adopter on its *effects*, because it WRITES.

**Gate C2 — conf-key doc parity.** Every conf key named in `customize.md` must exist in
`tools/memory-tree/.memory-tree.conf.example`, and the example's own header text must not contain the
banned pre-flatten vocabulary (`discipline folders`, `builds/YYYY-`). Catches id=7 and id=16's doc half.

### Axis D — companion routing and self-description

| # | Sev | Anchor | Says | Repo actually | Fix |
|---|-----|--------|------|---------------|-----|
| 2 | **H** | `domain-rules.md:96` | `## §14 — Gate discipline: a check that cannot fail is not a check` | **No template stub routes to it.** `grep -n 'domain-rules' template.md` returns exactly seven stubs (§4, §8, §9, §10, §11, §12, §13). Worse, the number collides: `template.md:177` is `## §14 — Session execution hygiene`, and the only bare "§14" in the template body (`:93`) resolves to *that* section. A live domain section is unreachable, and following the number lands on the wrong subject | Either add a §14 stub in the template (its subject belongs under §7 Quality gates), or renumber the companion section to a free number and route to it |
| 24 | **H** | `domain-rules.md:5` | "All are droppable-per-project (see the customize companion)" | `customize.md:33-43` sanctions dropping only §9 (partial), §11, §4 (partial) + §13, and §15 — closing at `:43` with "Everything else is universal core — keep verbatim." §8, §10 and §12 are droppable per this line and mandatory per the file it routes to; `template.md:163` even mandates §10 ("RUN it in every Tier-2 review") | Narrow the sentence to the four genuinely droppable sections, or extend `customize.md`'s conditional list to cover §8/§10/§12. The two files must agree on one droppable set |
| 3 | **M** | `template.md:4` | "the six domain checklists (§4, §9–§13) live in `…domain-rules.md`" | The companion holds **eight** sections (§4, §8, §9, §10, §11, §12, §13, §14). Self-contradicting inside the template: `:152` routes §8 to that same companion | State the real set, or a range covering §8 and §14 |
| 4 | **M** | `domain-rules.md:4` | "seven activity-scoped domain sections … §4, §8, §9, §10, §11, §12 and §13" | Eight sections; §14 at line 96 is excluded from both the count and the enumeration. The file misdescribes itself | Correct count and enumeration |
| 8 | **L** | `template.md:163` | "Recurring-bug-classes checklist (**~19 classes**)" | Companion §10 holds **25** bullets (23 bug classes + 2 meta-rules). §10 held exactly 19 at `541c5b7` (2026-07-12); `c2f608e`→`fc89ec1` grew it 19→25 by 2026-07-22 and the template was never re-stamped | Correct the count, or drop it — a count nobody derives is a `two-answers-to-one-question` instance |

**Gate D1 — stub/orphan cross-reference check.** For every `## §N` in `domain-rules.md`, assert a
template line matching `domain-rules\.md.*§N` exists; for every such stub, assert the section exists;
and assert no companion §N collides with a template `## §N` of a different title. Catches id=2 (both
halves), id=3, id=4, and the routing half of id=26. This is the cheapest, highest-value gate in the
report — it is `grep` + a set comparison, and it makes the three-file product's connective tissue
mechanical instead of prose.

**Gate D2 — count-claim check.** Any numeric self-description in the three files (`seven … sections`,
`the six domain checklists`, `~19 classes`, `the two §5 … lines`, `19-check hygiene gate`) is derived
by counting its referent, not authored. Catches id=3, id=4, id=6, id=8 and the whole class. Precedent:
this repo already derives the hygiene-check count and the codebase-map inventory counts.

### Axis E — a superseded rule in the load-bearing summary

| # | Sev | Anchor | Says | Repo actually | Fix |
|---|-----|--------|------|---------------|-----|
| 15 | **H** | `template.md:19` | §0 TL;DR: "**Memory holds only the non-derivable**; **per-node files**, no shared mutable index (§5)." | §5 at `:99` now says the opposite — an authored index several nodes append to "takes a row-keyed merge driver, **never a per-node shard**". The §0 bullet is byte-identical to `memory/archive/…-v-2-3.md`, while §5 was rewritten at v2.4; the template's own v2.4 note (`:6-7`) says the sharded per-node ledger is RETIRED; `git ls-files memory` shows no per-node file — the shards are frozen at `memory/archive/ledger/{a,b,c}.md`. The TL;DR and the section it cites give opposite instructions | Re-word to the v2.4 rule, e.g. "**Memory holds only the non-derivable**; status is DERIVED (a generated index) — no shared mutable index, no per-node shard (§5)." |

**Gate E1 — TL;DR/section vocabulary check, epoch-keyed.** Maintain a small retired-vocabulary list
(`per-node file`, `session ledger`, `discipline folder`) that must not appear in the live template
outside the changelog line, and re-stamp it at each `<!-- governance-template: vN.N -->` bump. Exactly
the `check-verdict-epoch.sh` pattern: the version constant DATES the claim, so a version bump that
touches a §-body forces the summary bullets citing it to be re-read.

## 4. The §10 / `memory/gotchas/` question (why this audit was commissioned)

**What the playbook says today.** `template.md:163` (§10) routes to `domain-rules.md` §10, a
25-bullet prose checklist, and says "RUN it in every Tier-2 review (§8); left-shift each confirmed
class into a gate (§7)". `template.md:143` folds it into the Tier-2 definition; `:41` (§1 DoD) and
`:131` (§7) both name "a §10 checklist entry" as the destination for a finding whose class cannot be
gated. The word "gotcha" appears in the three files exactly once, at `template.md:97`, generically.

**What the repo does today.** `memory/gotchas/` holds an anchored catalogue — `gotchas.py --report`:
10 records, 10 classes, 3 universal against a budget of 3, 0 unanchored, 22 anchors. Hygiene checks
17-19 govern it. `AGENTS.md:70` makes `python tools/memory-tree/gotchas.py --for-diff <base>..<head>`
a bar item: "prints the classes a diff can hit; **run it before a review, not after**."

**Whether that is drift: no.** Seven findings pressed this thesis (ids 1, 9, 10, 11, 12, 13, 14) and
all seven were refuted on evidence, on three independent grounds:

1. **The kit is Optional.** `template.md:104` marks the whole memory-tree kit — sole owner of
   `memory/gotchas/` and of checks 17-19 — as "Optional". A universal §1-DoD/§7 rule cannot name an
   optional kit's directory; every adopter who skips the kit would be left with a dangling destination.
2. **The two corpora are disjoint by charter, not by neglect.**
   `memory/builds/aFoldedQuarry/spec/units/2026-08-08-spec-aFoldedQuarry-6-u4-gotchas.md` §2 S8 says
   the catalogue "starts from THIS repo's own failure history", and its §3 Non-goals says outright:
   "Running the checklist automatically inside the review harness. `--for-diff` prints; wiring it into
   a prompt is a separate, deliberate change." The catalogue was never chartered to replace §10.
3. **The contents confirm it.** `--report` returns install-specific classes (`heredoc-escape-reaches-
   the-regex`, `subprocess-resolves-a-different-shell`, `grammar-bound-to-the-wrong-root`); companion
   §10 carries product-generic ones (client/server validation divergence, stale caches, an index that
   does not serve its query) that `memory/gotchas/` will never hold.

**So the retirement does not happen.** What DOES have to change:

- **`template.md`** — fix the stale count at `:163` (id=8): `~19` → `25`, or drop the parenthetical.
  Optionally add one clause making the two-corpora relationship explicit, e.g. *"adopted the
  memory-tree kit (§5)? `gotchas.py --for-diff` prints your repo's OWN classes too — run both; the
  corpora are disjoint by design."* No change at `:41`, `:131`, `:143` — all three were tested and are
  correct as generic text.
- **`domain-rules.md`** — no content change required. §10 is live and its documented-check mechanism
  is self-describing (`:56` is a live documented-check entry, `:58` the rule for writing one). Its
  *routing* problems (ids 2, 24) are Axis D, not this axis.
- **`customize.md`** — no §10 change. The two real memory-tree defects on its lines (ids 7, 16, 21)
  are conf-shape and install-path defects, not catalogue defects.

**Byte budget.** The template is at 32083 / 32768 — **685 B free**, and the gate's own header says
never raise the limit. The §10 work is free or better: `~19 classes` → `25 classes` is **−1 B**. The
optional two-corpora clause is ~150 B. Against the rest of the template-side fixes — id=28's marker +
shapes sentence (~200 B, the expensive one), id=15's §0 re-word (~+25 B), id=3's header set (~0 B),
id=2 if solved with a new stub (~150 B) — the total is roughly **500-530 B of 685**. Everything fits,
with ~150 B of margin. It does **not** fit if id=2 is solved by adding a §14 stub *and* the two-corpora
clause is taken *and* anything else lands in the same cycle. If more room is needed, the cheapest
externalization is `template.md:167` — §11's stub already carries 485 B of inlined LF/`git -C` rules
that are duplicated in companion §11; moving them out funds every remaining fix twice over. Fixing
the companion and `customize.md` costs nothing: neither is size-gated.

## 5. Refuted (recorded so a later reader does not re-raise them)

1. **id=1** `template.md:163` — §10 routes to a static checklist while the live mechanism is
   `memory/gotchas/` + `gotchas.py`. **Refuted:** the routing target is live (25 bullets); nothing
   retires it; the kit is Optional at `:104`, so a non-adopting project needs exactly that prose list.
2. **id=9** `template.md:143` — "the §10 checklist" as a review step is superseded by
   `gotchas.py --for-diff`. **Refuted:** the corpora are disjoint by charter (aFoldedQuarry U4 §2 S8),
   and that spec's Non-goals explicitly exclude wiring `--for-diff` into the review.
3. **id=10** `template.md:41` — §1 DoD's "§10 checklist entry" should be a `memory/gotchas/` record.
   **Refuted:** universal core (`customize.md:43`) cannot name an optional kit's directory;
   `domain-rules.md:56-58` shows the documented-check mechanism alive.
4. **id=11** `template.md:131` — same claim in §7. **Refuted:** substantively a duplicate of id=10;
   "no gate reads §10" is expected — *ungateable* is what the rule means.
5. **id=12** `template.md:104` — the §5 kit bullet omits the bug-class catalogue. **Refuted:** the
   "19-check hygiene gate" figure includes checks 17-19, the bullet is explicitly non-exhaustive and
   delegates to the kit README, which does document `gotchas.py`.
6. **id=13** `customize.md:30` — the scaffolder creates no `gotchas/` dir and no `UNIVERSAL_BUDGET`.
   **Refuted:** true of the kit, but the cited doc line claims neither; `UNIVERSAL_BUDGET` is not a
   template placeholder, so it has no home in a placeholder catalogue.
7. **id=14** `domain-rules.md:60` — the "vacuous gate" class is authored three times with no parity
   gate. **Refuted:** the three spans state three distinct directives (empty selector · unobserved
   failing case · scope of the fix); a product checklist is not required to mirror one repo's history.
8. **id=17** `template.md:104` — "one GENERATED work-state index" understates two artifact families
   (`LIVE.md` + `ledger/<month>.md`) from two inputs. **Refuted:** a one-clause compression that is not
   false; `:100` and `:69` already carry the fuller statement.
9. **id=18** `template.md:48` — the Landing block never mentions the lander that the pre-push now
   requires. **Refuted:** line 48 never prescribes a raw push, and `domain-rules.md:62` carries the
   lander rule. A placement preference.
10. **id=19** `template.md:106` — §5's kit menu omits `drift-audit/` and `gate-lint/`. **Refuted:** no
    line claims the menu is exhaustive; each bullet is individually true; the template is at its
    ceiling. An omission, not a contradicted claim.
11. **id=20** `template.md:127` — "legs concurrent, wall ≈ longest leg" but `run-gates.sh` is strictly
    serial. **Refuted:** the line is an imperative to the adopting project with an unfilled
    `{{GATE_RUNNER}}`; the conformance gap belongs against the runner, not the doc.
12. **id=22** `customize.md:20` — `{{CI_FILE}}` is always-fill but the dogfood has no CI. **Refuted:**
    an unfilled placeholder in a placeholder catalogue; `AGENTS.md:101-102` books CI as an open
    follow-up. An enhancement request.
13. **id=27** `template.md:146` — "install per WIRE §5" and `tools/workflows/tier2-review.js` do not
    exist in an adopting project. **Refuted:** the template names EVERY kit by its gov-repo source path
    (`:104`, `:105`, `:106`); a non-shipped upstream pointer aimed at the deploying agent is the
    product's deliberate convention.
14. **id=29** `template.md:153` — tool-call enforcement is presented as complete though the hook sees
    nothing on `Workflow({name:…})`. **Refuted:** a near-verbatim port of the binding protocol's own
    wording (`REVIEW-PROTOCOL.md:115-117`); the sentence's subject is where a hook can reach, not
    coverage completeness.
15. **id=30** `template.md:145` — the "no verdict ⇒ UNVERIFIED, never refuted" rule appears nowhere.
    **Refuted:** an omission, not a contradiction; the line as written is true and consistent with the
    protocol and the harness. Enhancement, and the template is size-gated.
16. **id=31** `domain-rules.md:20` — §8 omits the orchestrator-assigned-integer verdict-join rule.
    **Refuted:** §8 is a faithful port of `REVIEW-PROTOCOL.md:100-117`; the join rule sits at `:25-26`
    under a different section, so nothing is omitted from its source.
17. **id=32** `template.md:145` — "a skeptic prompted to REFUTE each finding" is the banned
    per-finding shape. **Refuted:** singular — a skeptic *stage*; the protocol uses the same phrasing
    at `:78-80`, and the count is fixed in the very next bullet.
18. **id=33** `template.md:21` — §0 carries only the concurrency cap, not the ≤5-TOTAL budget.
    **Refuted:** the hook demonstrably enforces what §0 attributes to it (verified by piping a raw
    `parallel(` script through it); §0 carries the budget half as "consolidate before you fan out" and
    routes to §8.
19. **id=34** `template.md:148` — "past ~25 agents returns diminish" is a pre-cap threshold now
    unreachable. **Refuted:** the ~25 figure bounds the LENS axis (the same clause says "scale … with
    LENSES, not skeptics"), while ≤5 bounds the verify-stage axis. `MAX_LENSES = 6` in `agent-cap.js`
    is an array-literal allowlist bound, not a doctrinal total.

## 6. Post-audit corrections

Recorded after the run, from verification done while building the fixes. A confirmed finding is not
a proven one, and two of these were confirmed by reading rather than running.

**Finding 16 — severity CORRECTED, high to medium.** The finding claimed a freshly scaffolded repo
reds the gate because `.memory-tree.conf.example` documents a shape hygiene checks 3 and 4 reject.
Measured: it does not. Both the pre-fix and the post-fix example conf scaffold into a scratch repo
and exit 0, producing the same flat tree (`DECISIONS.md HYGIENE.md LIVE.md README.md
TEMPLATE-SPEC.md backlog builds project`). `adopt-memory-tree.sh` reads `DISCIPLINES` as an enum,
exactly as its own line 12 comment says, and never consults the stale prose. The defect is real —
the comments describe discipline folders, `TREE.md`, a dated build path, nine canonical spec sections
against ten, and `gen-memory-tree.sh` which U2 deleted, and the file ships 4 of the 15 conf keys the
kit reads — but it misinforms the adopter the script explicitly tells to EDIT IT, rather than
breaking the gate. The skeptic confirmed it by reading the comments against `HYGIENE.md`; nobody ran
the scaffolder until the build did.

**Finding 28 — CONFIRMED by reproduction, both arms.** A script written to the letter of the old
`template.md:146` exits 2 under `tools/hooks/agent-cap.js`; the same script with the marker the
revised §8 now spells exits 0. Both observed.

**New defect, out of this review's scope.** Reproducing 28 surfaced a hole in the hook itself: an
identifier bound from an EMPTY array literal is blessed as bounded and never re-examined when a later
statement grows it, so `const batches = []` plus a per-finding `push` fans one agent per item past
both the hook and the merge-bar leg, at exit 0. `tools/hooks/agent-cap.js:171` already guards the
`[].concat(x)` spelling of the same hole. Filed `TOOL-aCandidStub-1`.
