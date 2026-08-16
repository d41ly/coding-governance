# Review aWrittenMethod-1 — Tier-2 on the cumulative diff landing on main

**Serves:** diff-review TOOL-aWrittenMethod-1 TOOL-aWrittenMethod-2 TOOL-aWrittenMethod-3 TOOL-aWrittenMethod-4 TOOL-aWrittenMethod-5 TOOL-aWrittenMethod-6  <!-- inferred: cumulative diff landing on the default branch -->

**Date:** 2026-08-11 · **Tier:** 2 · **Streams:** tooling, playbook
**Subject:** `git diff main...HEAD` @ `5ed9b4b` — 31 files, +1739/-40. The build-method document
(`tools/memory-tree/BUILD-METHOD.template.md` + its rendered `memory/guides/BUILD-METHOD.md`), the
third kit/dogfood parity pair, the unattended kit's new `KEEPALIVE_INTERVAL` declaration, and the
S6 playbook collapse (template §8 → §1, companion §1 → a pointer).
**Question asked:** does the diff ship what it claims, to the people it claims to ship it to?

## 1. Verdict

**No blockers. Two highs, and they share one root: this diff writes documents for adopters, and every
mechanism that would have told us what an adopter receives is blind here because gov is not an
adopter.** The build-method document is the diff's centrepiece and it cannot reach an adopter at all —
`adopt-memory-tree.sh` short-circuits any already-scaffolded tree (id=2), so only a *fresh* scaffold
gets it, and a fresh scaffold that follows the kit's own instructions immediately reds its own hygiene
gate with five dead repo-path citations (**id=10, high**) because the document cites paths that only
the *other* gov kits install. The documented repair for the first half, `--render`, prints "missing
live copy" and exits 0 having created nothing. In the unattended kit the same blindness produces the
second high: `KEEPALIVE_INTERVAL` is defaulted to `""`, the shipped `.unattended.conf.example` never
declares it, and an empty substitution leaves no `{{` — so every fresh adopter's Skill reads *"at the
cadence this project declares — ."* while all three legs, including the placeholder-completeness arm
added for exactly this failure, print green (**id=14, high**; ids 11 and 4 are the same hole seen from
the gate and conf sides). One genuinely separate defect rides the same key: it is the kit's first
free-prose value and it is interpolated unescaped into `sed s|…|…|`, so a `|` truncates SKILL.md to
zero bytes with exit 0 and `--check` then diffs empty-against-empty and certifies it (id=1).

The playbook half is cleaner in substance and stale in prose. S6 collapsed §8's duplicate landing rule
into a pointer at §1 and bumped the machine marker to v2.7 — but the human banner still reads v2.6, and
its changelog sentence still advertises the two rules this same diff deleted (ids 5/16). The two
adopter-facing runbooks now contradict each other about §8: `customize.md` was updated to say §8 no
longer carries the rule, `WIRE-INTO-PROJECT.md:574` still tells adopters to re-pull it (id=6), and §1's
own outbound pointer now round-trips into a section that declines to state the rule (id=17). Nothing
gates the prose version; `check-kit-versions.sh` has no `governance-template` reference.

The through-line for the fix list: **this diff added four new documents and zero new adopter-effect
arms.** `adopt-codebase-map.test.sh` and `adopt-unattended.test.sh` exist because the same class bit
twice before. `tools/memory-tree/` still has no adopter e2e, and the one it needs is the one that arms
`DEAD_PATH_PIN`.

## 2. Review shape

| raw | confirmed | refuted | unverified | precision |
|-----|-----------|---------|------------|-----------|
| 18  | 15        | 3       | 0          | **0.83**  |

Every confirmed finding survived an adversarial skeptic pass; no finding is outstanding. Precision 0.83
is well above the §8 ~0.5 floor and is itself a signal about the subject: this diff is mostly *prose
that makes checkable claims*, which is the highest-yield surface a review can be pointed at and the
lowest-yield one for the existing gates.

The 15 confirmed findings collapse to **11 distinct defects** — ids 5/16 are one defect seen twice
(the template banner), ids 13/18 likewise (the parity leg's stale header), and ids 4/11/14 are three
lenses on one hole (`KEEPALIVE_INTERVAL` defaults to empty and nothing can see it). They are reported
separately below because their fixes differ in scope, and grouped by axis because their *causes* do not.

Severity legend: **B** blocker (0) · **H** high (2) · **M** medium (7) · **L** low (6).
"Left-shift gate" = the mechanical check that would have caught the class before a human read the diff.

---

## Axis A — the new document cannot reach an adopter, and reds their gate when it does

### id=10 · **HIGH** · `tools/memory-tree/adopt-memory-tree.sh:69`

The new `render_doc` call ships `BUILD-METHOD.md` into every memory-tree adopter, but the document
cites five paths only the *other* gov kits install — so the memory-tree scaffold writes 5 dead
repo-path citations into the adopter's own present-tense corpus, which its own hygiene check 15 scans.

Reproduced: fresh `git init` + copy `tools/memory-tree` + `--scaffold` + arm `DEAD_PATH_PIN` (the state
the kit tells adopters to reach) yields `check 15 rule 1` on `memory/guides/BUILD-METHOD.md` lines
7 (`tools/run-gates.sh`), 90 (`tools/workflows/tier2-review.js`), 96 (`memory/guides/REVIEW-PROTOCOL.md`),
201 (`memory/gotchas` — a directory the scaffold's own `mkdir -p` at line 59 never creates) and
203 (`memory/guides/UNATTENDED-PROTOCOL.md`). Before this diff the same scaffold produced **1** such
row. This repo's bar cannot see it because gov holds every cited file; a fresh scaffold hides it until
the adopter follows the script's own step 6 ("MEASURE any pin/floor"). The adopter's only escape hatch
is raising the shrink-only pin to 5 — permanently disarming the ratchet. That is verbatim the class
`corpus_ids.py:236-240` records as a measured bug ("seven dead kit paths in a scaffolded `HYGIENE.md`
and the gate exited 0"), reintroduced in a new rendered document. It also breaks
`adopt-memory-tree.sh:2`'s stated contract ("hygiene-passing") and its own step-3 `expect 0`.

**Fix.** Make the cross-kit pointers non-resolving *by construction* rather than dead: write them
elided (`<MEMORY_ROOT>/guides/REVIEW-PROTOCOL.md`, `<TOOL_ROOT>workflows/tier2-review.js`) so `ELISION`
in `corpus_ids.py:55` skips them — M11 already only promises "read these if your project has them".
Alternatively have `adopt-memory-tree.sh` seed the rows it knowingly creates into
`memory/project/corpus-path-unresolved.txt`, and add `memory/gotchas` to the scaffold `mkdir -p` at
line 59.

**Left-shift gate.** `tools/memory-tree/adopt-memory-tree.test.sh` — an adopter e2e in the shape
`adopt-codebase-map.test.sh` and `adopt-unattended.test.sh` already use: scaffold a throwaway repo,
**arm `DEAD_PATH_PIN="0"`**, run the hygiene gate, assert exit 0. No current leg executes the
memory-tree adopter's *effects*, which is the only reason this landed green.

### id=2 · **MEDIUM** · `tools/memory-tree/kit-dogfood-parity.test.sh:53`

The third parity pair (`$M/guides/BUILD-METHOD.md`) can never land in an already-scaffolded adopter
tree, and the documented repair `--render` exits 0 while printing "missing live copy" and repairing
nothing.

`[ ! -f "$live" ]` at line 63 `continue`s **before** the mode dispatch, and line 89
(`[ "$MODE" = --render ] && exit 0`) discards the `st=1` it set — so `--render`, documented at line 6 as
"rewrite the live copies from the templates", prints `kit-parity: missing live copy
memory/guides/BUILD-METHOD.md`, creates no file, and exits 0. Meanwhile `adopt-memory-tree.sh:50-51`
short-circuits any tree carrying the `gov:kit memory-tree@` marker ("already scaffolded — nothing to
do", exit 0), so no adopter upgrading 2.4→2.5 ever receives the new document. `HYGIENE.md` and
`TEMPLATE-SPEC.md` survive a kit upgrade only because `--render` can rewrite an *existing* file; the
newly added third pair is the one document neither path can deliver. Net for every existing adopter:
the parity leg goes permanently red (`--check` exit 1) with a repair command that reports success, and
the build method — including M3's security/write-surface vetoes — is never delivered. The build's own
spec §S2 concedes the `--render` half and works around it locally rather than fixing it.

**Fix.** In `--render` mode, create a missing live copy instead of skipping it: move the
`[ ! -f "$live" ]` guard inside the `--check` branch (keeping `mkdir -p "$(dirname "$live")"` before
the render), and change line 89 to `[ "$MODE" = --render ] && exit "$st"` so a render that could not
repair something is not reported as a pass. Add a converge path in `adopt-memory-tree.sh` that renders
newly-shipped documents into an already-scaffolded tree rather than exiting 0 at the marker check.

**Left-shift gate.** Extend the memory-tree adopter e2e (id=10) with an **upgrade** arm: scaffold at
the previous kit version, drop in the new kit, run the adopter, then assert the parity leg exits 0.
That single arm catches both halves — the delivery gap and the no-op repair — and generalizes to every
future document the kit adds.

### id=15 · **MEDIUM** · `tools/memory-tree/BUILD-METHOD.template.md:237`

The shipped build-method template cites `skills/session-kickoff/SKILL.md` and
`.claude/SESSION-KICKOFF.md` as repo-relative paths; neither exists at those locations in an adopter's
tree.

Per `AGENTS.md` and `WIRE-INTO-PROJECT.md:527` the kickoff engine is a per-machine junction at
`~/.claude/skills/session-kickoff`, explicitly "not in the repo"; `WIRE-INTO-PROJECT.md:336`
instantiates the manifest at `docs/SESSION-KICKOFF.md`. So M11's first pointer (`:237`) and M2's tier
rule (`:42`) both dead-end for every adopter. This is the install-prefix class — "what actually strands
an adopter is a path SPELLED in something they receive" — and no gate reaches it:
`check-install-prefix.sh` derives its alternation from tracked `tools/*` dirs only, and
`corpus_ids.py:242` classifies a citation as a repo path only when its first segment is a derived
tracked top-level dir. `skills/` is one **only in this repo**. The file's own footer caveat covers
`memory/` and nothing else, and the file parameterises `{{TOOL_ROOT}}`/`{{MEMORY_ROOT}}` elsewhere —
the authors parameterised where they thought it mattered and missed here.

**Fix.** Describe the kickoff engine by name rather than by repo path ("the `/session-kickoff` engine,
installed per machine"), and refer to the manifest as "the project's kickoff manifest (the engine
resolves `docs/claude/`, `docs/`, `.claude/` or the root)" in both M2 and M11 — or widen the footer
caveat to name every non-derivable path the file spells.

**Left-shift gate.** Widen `check-install-prefix.sh`'s alternation beyond `tools/*` to include
`skills/` and `.claude/` **for shipped `*.template.md` only**, with deliberate spellings going to the
existing shrink-only waiver file. The kit ships prose; prose that spells a gov-only layout path is the
same defect class the leg already owns.

### id=8 · **LOW** · `tools/memory-tree/BUILD-METHOD.template.md:119`

M5 states the recall CLI "exits 2" if you do not supply 8-14 terms; it exits 2 only when `--terms` is
absent entirely — a short list prints a note and exits 0.

Reproduced against `tools/memory-recall/query.py:1136-1157`:
`--terms "template size gate"` printed `note: 3 rewrite terms; the measured arm used 8-14` on stderr
and exited **0** with 40 hits. `query.py:1151-1157` warns and falls through, and its own comment is
explicit that this is deliberate ("Warn, never refuse: a caller who supplied six real terms should get
an answer"). Exit 2 is reached only when `--terms` is absent, empty, or contradicts `--no-terms`. The
very next paragraph of M5 tells the agent "Never read a probe's exit status as a verdict", which makes
the exit-2 promise the only stated guard on term count — so an agent that supplies three lazy terms
gets a degraded query, a green exit, and a document that told it the tool would have refused. Binding
procedure, already rendered live at `memory/guides/BUILD-METHOD.md:119`, shipping to every adopter.

**Fix.** Reword to: "omitting `--terms` exits 2; a short list only prints a note and still runs, so the
8-14 floor is yours to hold." Re-render with
`bash tools/memory-tree/kit-dogfood-parity.test.sh --render`.

**Left-shift gate.** Doc-vs-code claims about a shipped CLI's exit codes are testable: add a
`memory-recall` selftest arm asserting the documented contract (`--terms` absent → 2; short list → 0 +
note), and cite that arm from the prose so the next edit to either side reds the other. This repo
already gates the same "two answers to one question" shape via kit/dogfood parity and verdict epoch.

---

## Axis B — the unattended kit's first free-prose declaration

Four confirmed findings, two distinct defects. Root cause for both: `KEEPALIVE_INTERVAL` is the first
conf value that is neither a shell command nor a path, and the render/check pair was designed around
values that are.

### id=14 · **HIGH** · `tools/unattended/adopt-unattended.sh:67`

`KEEPALIVE_INTERVAL` is defaulted to empty and rendered into a **mandatory prose slot**, and the
shipped `.unattended.conf.example` never declares it — so every fresh adopter's Skill reads "at the
cadence this project declares — ." while `adopt-unattended.sh --check` reports "in sync".

Reproduced: `SKILL.template.md:27` with an empty value emits literally ``Use `TheCreateCall`, at the
cadence this project declares — . Keep the id it returns.`` The unattended-run agent is told a cadence
is declared and given none, so it invents one. The placeholder-completeness arm the kit added for
exactly this failure (AGENTS.md: "a conf that declares nothing for a key renders a Skill that is
perfectly in sync") cannot see it, because an empty substitution leaves no `{{`-shaped token.
`tools/unattended/.unattended.conf.example` — the file adopters copy verbatim — never mentions the key,
and the ARM-1 fixture conf at `adopt-unattended.test.sh:31-43` omits it too, so the adopter e2e gates
the broken render and passes: **fixture-passes-by-finding-nothing**. Green here only because the
dogfood repo happens to declare it. The spec's S7 scopes the key to `.unattended.conf` + the two
`adopt-unattended.sh` sites and never names the example file, so this is an unspecced gap, not the
documented "optional, outside the required-key loop" decision.

**Fix.** Either (a) add `KEEPALIVE_INTERVAL="<e.g. every 10 minutes (cron 3-59/10 * * * *)>"` to
`tools/unattended/.unattended.conf.example` and make the render refuse an empty value the way the other
required keys do, or (b) keep it optional and make the sentence degrade cleanly — render the
", at the cadence this project declares — <x>" clause only when the value is non-empty.

**Left-shift gate.** Two arms, both cheap: (1) a `hit` arm in `adopt-unattended.test.sh` asserting the
cadence text **reached** the rendered Skill (the existing `grep -cE '\{\{[A-Z_]+\}\}' == 0` arm is
satisfied by an empty interpolation, so absence-of-placeholder is not presence-of-value); (2) a leg
asserting `.unattended.conf.example` declares every key `SKILL.template.md` interpolates — the example
file is what adopters copy, so it is a shipped artifact and belongs on the bar.

### id=11 · **MEDIUM** · `tools/unattended/adopt-unattended.sh:67`

The gate-side statement of the same hole: with `KEEPALIVE_INTERVAL=""`, the placeholder arm at line 99
cannot fire (an empty substitution leaves no token), the diff arm at line 91 compares the Skill to the
same empty render and agrees, and `check-unattended.sh:39`'s required-key loop is exactly
`LANDER BYPASS_BAN GATE_CMD WIRING_CHECK KEEPALIVE_CREATE KEEPALIVE_DELETE` — the new key deliberately
absent per `.unattended.conf:36-39`. That is precisely the hole the line-97-98 comment says the arm
exists to close, reopened one key later. **The new key is the only one whose failure mode is an empty
render rather than a surviving `{{`.**

**Fix.** Add `KEEPALIVE_INTERVAL` to the required-key loop in `tools/unattended/check-unattended.sh:39`,
or default it in `adopt-unattended.sh:67` to something the grep catches
(`KEEPALIVE_INTERVAL="{{KEEPALIVE_INTERVAL}}"`) so an undeclared cadence reds instead of rendering a
dangling em-dash.

**Left-shift gate.** Stop pre-initializing *interpolated* keys to empty. Derive the render's key list
from the template (`grep -o '{{[A-Z_]*}}' SKILL.template.md`) and refuse any key the conf did not set —
that makes the placeholder arm able to fire for all of `LANDER`, `KEEPALIVE_CREATE`,
`KEEPALIVE_DELETE`, `KEEPALIVE_INTERVAL` and every key added after them, instead of one at a time.

### id=4 · **LOW** · `.unattended.conf:40`

The conf comment justifies the exemption as "a key with no consumer" — but it has one:
`SKILL.template.md:27`, the sentence telling the agent how often to schedule the only mechanism keeping
an unattended run alive. The comment contradicts its own preceding clause. Decisive extra evidence for
adopter reachability: the adopter-facing conf key table in `PROTOCOL.template.md:159-171` does **not**
list `KEEPALIVE_INTERVAL` at all, so an adopter following the shipped documentation omits it by default.

**Fix.** As id=11, plus add the key to the `PROTOCOL.template.md` conf table so the shipped
documentation and the shipped example agree with the render.

**Left-shift gate.** A parity arm asserting the conf key table in `PROTOCOL.template.md` enumerates
exactly the keys `check-unattended.sh` requires plus the keys the Skill template interpolates. Three
hand-kept spellings of one key set is two too many.

### id=1 · **MEDIUM** · `tools/unattended/adopt-unattended.sh:80`

Distinct defect on the same key: the value is interpolated **unescaped** into a `sed s|…|…|`
replacement, and a value containing `|` makes sed exit 1 while the `| tr -d '\r'` pipeline still exits
0 — so the adopter writes a **zero-byte SKILL.md** and reports success.

Reproduced: with `KEEPALIVE_INTERVAL='every 10 min | offset 3'`, sed dies (``unknown option to `s'``),
the pipeline returns tr's 0, `render > "$SKILL_OUT"` truncates the file to 0 bytes, and line 110 prints
"unattended: rendered …" and exits 0. The `--check` merge-bar leg then renders an equally empty temp
file, `diff -q` reports them equal, the `{{…}}` grep finds nothing in an empty file, and line 104
prints "unattended: in sync" — **a green gate certifying an empty Skill.** The unattended agent then
has no rendered protocol surface at all. A value containing `&` fails differently: sed re-inserts the
whole match and the render emits a literal `{{KEEPALIVE_INTERVAL}}` — line 99 *would* red on that, but
with the misleading message "declares no value for it" while the conf does declare one. The same
unescaped interpolation covers `LANDER`, a shell command where `|` is entirely ordinary.

**Fix.** Escape conf values before substitution
(`esc(){ printf '%s' "$1" | sed -e 's/[\\&|]/\\\\&/g'; }`, applied to each conf-sourced key) and make
`render()` fail loudly — `set -o pipefail`, or capture sed's status and `exit 1` rather than writing a
truncated file.

**Left-shift gate.** Two: (1) `--check` refuses a zero-byte or implausibly short `SKILL_OUT`, so an
empty render can never be diffed clean against an empty render — the "green by absence" shape this kit
already guards elsewhere (`PAIRS` emptiness, the `no document pairs configured` arm); (2) an
`adopt-unattended.test.sh` arm with a metacharacter-bearing fixture conf (`|`, `&`, `\`) asserting the
render either succeeds byte-correct or exits non-zero. Any template-render kit that interpolates
free prose needs one hostile-value fixture; this is now the second such kit.

---

## Axis C — the v2.7 bump moved the marker and left the prose

### id=5 / id=16 · **MEDIUM** (one defect, two lenses) · `parallel-coding-governance.template.md:3`

The machine marker moved to v2.7 but the file's own visible banner still reads
`*Template **v2.6** · 2026-08-10*`, and its changelog sentence still advertises the two rules this same
diff deleted.

Verified in the working tree: `:3` says v2.6, `:11` says `<!-- governance-template: v2.7 -->` — one
file, two answers. `git show 5ed9b4b -- parallel-coding-governance.template.md` shows the diff bumped
only the marker. The changelog at `:6-9` is now false on both claims: (a) "§1 and §8 accept a committed
standing mandate" — the same diff rewrote `:158` to "landing is §1's rule, not restated here", and
`customize.md:62-64` was updated in the same commit to say §8 "no longer carries a second spelling of
the landing rule"; (b) "the new companion §1, which also carries the unattended-run checklist" — the
same diff collapsed those thirteen companion bullets to a single pointer at
`{{MEMORY_ROOT}}/guides/UNATTENDED-PROTOCOL.md`. `parallel-coding-governance.domain-rules.md:3` reads
v2.7 and `memory/archive/parallel-coding-governance.template-v-2-6.md` was snapshotted, so the bump was
real everywhere except the copy humans read. `WIRE-INTO-PROJECT.md:568` tells adopters to re-pull by
comparing versions, so an adopter reading the banner concludes they are current and skips a pull that
changed §8. **This is an unmet acceptance item of the build's own spec** —
`memory/builds/aWrittenMethod/spec/2026-08-11-spec-aWrittenMethod-1.md` S6 requires "the template's
history line describes the collapse", and `memory/builds/aWrittenMethod/README.md:44` already reports
S6 done.

**Fix.** Set `:3` to `*Template **v2.7** · 2026-08-11.` and replace the `**v2.6 (2026-08-10):**`
sentence with a v2.7 entry: companion §1's unattended block collapsed to one pointer at
`{{MEMORY_ROOT}}/guides/UNATTENDED-PROTOCOL.md`; §8's duplicate landing clause now points at §1 instead
of restating it. The v-2-5/v-2-6 archive snapshots show the changelog is *not* cumulative, so replace
rather than append.

**Left-shift gate.** A four-line leg: the prose `**vN.N**` on line 3 of both
`parallel-coding-governance.template.md` and `…domain-rules.md` must equal their
`<!-- governance-template: vN.N -->` markers, and the markers must equal each other. Nothing guards
this today — `grep -rn governance-template tools/ skills/` over `*.sh`/`*.py` finds no gate,
`check-kit-versions.sh` covers kit constants only, and `/session-kickoff` greps the marker alone. This
is the same shape as the verdict-epoch leg: the version DATES the claims, so a diff that moves a rule
must move the version the reader sees.

### id=6 · **MEDIUM** · `WIRE-INTO-PROJECT.md:574`

The adopter-facing re-pull note still states that §8's commit bullet accepts a committed standing
mandate, which the shipped §8 no longer does after this diff.

The note reads "§1's Landing bullet and §8's commit bullet now accept a committed standing mandate in
place of the explicit ask … Re-pull §1, §8 and the companion in lockstep." Shipped §8 after this diff
(`template.md:158`) is "Commit freely as you go …; landing is §1's rule, not restated here" — no
mandate clause. The same commit edited the *other* adopter-facing runbook to state the opposite, so the
two documents an adopter reads now contradict each other about §8, and the `customize.md` deletion
recipe no longer names the §8 clause this note tells them to re-pull. An adopter either hunts for a
clause that is gone or keeps their own stale duplicate of the landing rule — the exact duplication S6
set out to remove. The trailing snapshot pointer is stale too: the commit added
`…template-v-2-6.md`, so the prior release is v-2-6, not the v-2-5 the note names.
`WIRE-INTO-PROJECT.md` was not touched by the commit at all.

**Fix.** Add a v2.7 paragraph (or amend the v2.6 one): §8's landing clause collapsed into a pointer at
§1, and companion §1's unattended checklist collapsed into a pointer at
`{{MEMORY_ROOT}}/guides/UNATTENDED-PROTOCOL.md`. Point the prior-release snapshot at
`memory/archive/parallel-coding-governance.template-v-2-6.md`.

**Left-shift gate.** Extend the version leg above to a third site: assert `WIRE-INTO-PROJECT.md`'s
re-pull note names the current marker version, and that the snapshot filename it cites is the
highest-numbered `memory/archive/parallel-coding-governance.template-v-*.md` **below** the current
version. Both are one-line derivations from files already on disk; both rotted silently here.

### id=17 · **LOW** · `parallel-coding-governance.template.md:158`

§8 now says landing is "§1's rule, not restated here" while §1's Landing bullet at `:50` still
cross-references "(companion §1, §8)" — the two pointers form a loop. A reader following §1 → §8 for
the mandate rule is sent straight back to §1 and learns nothing. The parenthetical descends from a bare
`(§8)` that pointed at the template's own §8 back when §8 restated the rule; `09b9bd1` only prefixed
"companion §1,", and `5ed9b4b` then emptied the §8 half. The charitable re-reading does not save it:
companion §8 is "Structured returns from orchestration scripts", unrelated to landing.

**Fix.** Drop `, §8` from `:50` so it reads `(companion §1)`, matching `customize.md`'s new note.

**Left-shift gate.** Cheap and general: a leg that resolves every `§N` cross-reference in the template
and companion and reds on one pointing at a section whose body is a stub or a pointer back to the
referring section. The §-stub architecture makes this class structural, not incidental — the same
externalization that created the stubs is what leaves outbound pointers aimed at emptied sections.

---

## Axis D — self-referential drift, in the two files whose job is to prevent it

### id=13 / id=18 · **LOW** (one defect, two lenses) · `tools/memory-tree/kit-dogfood-parity.test.sh:2`

The header block still says "the two documents this kit SHIPS … equal the two documents this repo RUNS
ON" and enumerates only `HYGIENE.template.md` / `SPEC-TEMPLATE.template.md`, while `PAIRS` at `:53` now
carries three.

The same commit fixed the hardcoded `2 pairs` in the success line — correctly, and with a comment
naming it as "the drift class this file exists to catch, sitting in this file's own success line" — and
left the identical stale count two lines from the top of the same file, plus the two-file enumeration
at `:8-9`. So a second hand-kept spelling of the `PAIRS` population survives, in the one file whose
stated purpose is to catch exactly that, and `BUILD-METHOD.md` is invisible to anyone reading the leg
to learn what it grades. Comment-only, hence genuinely low; reachable by the next reader adding a
fourth pair.

**Fix.** Reword `:2-3` to describe the population rather than count it — "the documents this kit SHIPS,
RENDERED for this install, must equal this repo's installed copies; the pair list is `PAIRS`" — and
either add `BUILD-METHOD.md` to the `:8-9` enumeration or restate that block in terms of `PAIRS`. Keep
the 2026-08-08 spec-template incident as the historical example it is.

**Left-shift gate.** Have the leg print its own header contract: derive the usage line from `PAIRS` at
runtime (`# grades $npairs document pairs: …`) so there is exactly one spelling. Where that is
impractical, a `check-arms`-style assertion that no comment in a gate leg states a literal count of a
population the same file computes — this repo already banned that shape once, in this file, in this
commit.

### id=12 · **LOW** · `AGENTS.md:8`

The two hardcoded map counts were replaced with `python tools/codebase-map/reuse_lookup.py` "prints the
live pair", but that command takes a required `query` argument and prints a different pair than the one
described.

Run exactly as spelled, it exits 2 with `error: the following arguments are required: query` — the
instruction in the charter every agent loads is dead as written. With a query supplied, the banner
prints `277 symbols | 84 inventory keys | 7 affordance seams | 6 dossiers`: the dossier half is right,
but **84 is the total inventory-key count**, not the unclaimed/baselined number the deleted sentence
gave — `memory/map/baseline.toml` holds 62 entries, and the only thing that prints that figure is
`gen_map.py:158` ("baseline: {…} unclaimed keys"). The de-hardcoding instinct was right; the
replacement instruction is dead and, once fixed, reports a different quantity than the prose promises.

**Fix.** Spell a command that actually answers it — `python tools/codebase-map/reuse_lookup.py <term>`,
naming what its banner reports (dossiers + total inventory keys) — or point at
`memory/map/generated/MAP.md`'s claimant column / `baseline.toml` for the unclaimed count.

**Left-shift gate.** A leg that extracts fenced/inline `python tools/…` and `bash tools/…` invocations
from `AGENTS.md` and `WIRE-INTO-PROJECT.md` and asserts each parses its own arguments (`--help`, or a
dry-run) without exiting 2. The charter is loaded by every agent on every session; a dead command there
costs more than a dead command anywhere else in the repo, and it is the same class the sibling commit
`22b14ca` was explicitly cleaning up.

---

## 3. What the gates could not see, and why

Three blind spots produced 11 of the 15 confirmed findings. They are worth naming because each has a
one-leg fix that generalizes past this diff.

1. **gov is not an adopter.** Every dead cross-kit path (id=10), every missing example-conf key
   (id=14), every gov-only layout assumption (id=15) is green here because this repo holds the file the
   adopter lacks. Only an adopter-effect e2e sees these, and `tools/memory-tree/` — the kit that
   scaffolds the corpus every other gate reads — is the one kit without one.
2. **Absence-of-placeholder is not presence-of-value.** The unattended kit's newest arm greps the
   render for `{{…}}`. An empty conf value satisfies it, and pre-initializing every key to `""` before
   sourcing the conf guarantees emptiness is the failure mode. Derive the key list from the template
   and refuse unset keys, and ids 4, 11 and 14 all become impossible.
3. **The version humans read is ungated.** `check-kit-versions.sh` gates kit constants and
   `check-verdict-epoch.sh` gates the hygiene engine's version, but the governance template — the
   product — has a machine marker with no prose counterpart on the bar. ids 5/16, 6 and the stale
   snapshot pointer are all one missing four-line leg.

## 4. Recommended landing order

1. **id=1** — one-line escape + `pipefail`. A zero-byte Skill certified green is the worst *shape* in
   the set even at medium severity, and the fix is smallest.
2. **id=14 / id=11 / id=4** — one change to the render's key handling closes all three.
3. **id=10 / id=2** — these two must land together; fixing delivery without fixing the citations ships
   the red gate to more people.
4. **ids 5/16, 6, 17** — the prose sweep, plus the version leg that keeps it swept.
5. **ids 8, 12, 13/18, 15** — doc corrections, each re-rendered through
   `kit-dogfood-parity.test.sh --render` where the file is a shipped template.
