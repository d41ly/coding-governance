**Serves:** spec-audit KICK-aReplayedCard-1 KICK-aReplayedCard-2 KICK-aReplayedCard-3 TOOL-aReplayedCard-1 TOOL-aReplayedCard-2 TOOL-aReplayedCard-3 TOOL-aReplayedCard-4 TOOL-aReplayedCard-5

# aReplayedCard — spec audit of the eight-unit set, round 1

*Node `a`, 2026-09-13. A Tier-2 adversarial pass over the eight specs before any code: a fan of four
primed finder lenses, a skeptic stage in five batches prompted to REFUTE each finding, one synthesis.
The mandate was underspecification, contradiction between sibling specs on the four M2 axes (scope,
interface, ordering, acceptance), unstated assumptions about the harness, and prior art in the tree a
spec re-invents, with every code claim checked against the cited file and line. The synthesis re-read
at source every claim a blocker or high below rests on; what it re-read, and what it did not run, is
listed at the end.*

**Round: 1.** Subjects, each pinned at the blob it was read at:

- `memory/builds/aReplayedCard/spec/2026-09-13-spec-KICK-aReplayedCard-1.md@473e72091489d49234b8b2707764995cf28c9783`
- `memory/builds/aReplayedCard/spec/2026-09-13-spec-KICK-aReplayedCard-2.md@3097291b72f107b9456d608b6201ee2d5e112a1d`
- `memory/builds/aReplayedCard/spec/2026-09-13-spec-KICK-aReplayedCard-3.md@aa39cbc721d62bbd30dce2a94cab6aa4818f52bc`
- `memory/builds/aReplayedCard/spec/2026-09-13-spec-TOOL-aReplayedCard-1.md@b1d4f312ab165e866178310a9552f82b3701822d`
- `memory/builds/aReplayedCard/spec/2026-09-13-spec-TOOL-aReplayedCard-2.md@eec054cdcb9933db76c13e7f0a7c78a90c55a03b`
- `memory/builds/aReplayedCard/spec/2026-09-13-spec-TOOL-aReplayedCard-3.md@000afe12a3bdaa405922001f4b4f5555894e3ac8`
- `memory/builds/aReplayedCard/spec/2026-09-13-spec-TOOL-aReplayedCard-4.md@aea60d016409f79fc8dced194cefdcd4a589ad33`
- `memory/builds/aReplayedCard/spec/2026-09-13-spec-TOOL-aReplayedCard-5.md@66d217162abaa9806af7c74f244462a38829318d`

## Verdict: BLOCKED

Four blocker defects stand, and none of them is a matter of taste. Three sit on `TOOL-aReplayedCard-1`,
the deny: it refuses the git commands its own remedy (`/session-kickoff`) issues before a READY line can
exist; it refuses the unattended prompt path's step-4 push with no exemption that can reach it; and it
compares the card's toplevel to the payload's by byte equality across two path alphabets, so on every
registered node (all four are Windows + Git-Bash) every main-loop commit is denied with the suite
green. The fourth sits on `TOOL-aReplayedCard-2`: the fragment merger it routes every command through
emits `node "<path>"` and nothing else, so the `bash … --card --registry` commands the unit specifies
cannot be produced by the seam the unit cites, and applying the check-wiring fragment REPATHS the live
wiring check to a node invocation with no `--session`. Each of the four was read at the source the spec
names, not inferred. Nine high defects follow, most of them on the same two units; the kickoff units
carry the rest. `TOOL-aReplayedCard-4` drew no confirmed finding.

## Review shape

Raw 104, confirmed 50, refuted 54, unverified 0, precision 0.48. Precision sits just under the ~0.5
floor §8 sets before adding agents; the refutations concentrated in the lens reading the specs for rule
conformance rather than checking their claims against source, and the correct response by §8's own
rule is to tighten that lens's priming rather than widen the fan.

**Run integrity.** Lenses 4/4 returned, 0 died. Skeptic batches 5/5 returned, 0 died. 0 contradictory
verdicts demoted to unverified, 0 spurious verdicts discarded, 0 duplicates removed by the pipeline's
dedup stage. The run is complete on its own terms. Two consequences of those figures are stated rather
than left to inference. First, because no lens died, the zero on `TOOL-aReplayedCard-4` is a zero from a
full read by all four lenses, not a zero from absence; it is still a spec audit's zero, which grades
what a document says and not what a mechanism will do. Second, the pipeline's dedup found 0, but the 50
confirmed findings contain many that name one defect from different lenses (four lenses found the
fragment schema, four found the path alphabets). The fold below is editorial: it groups them into 27
distinct defects and keeps every raw id. Each raw id takes the severity of the defect it evidences, so
the per-id table and the integers in the state block agree by construction.

| Defect | Severity | Raw ids folded in |
|---|---|---|
| B1 the deny catches the kickoff's own git | blocker | 1, 36, 64 |
| B2 the prompt path's push is denied with no reachable exemption | blocker | 2, 37, 58 |
| B3 the fragment schema cannot carry the commands | blocker | 7, 31, 59, 84 |
| B4 the tree cell is compared across two alphabets | blocker | 3, 38, 61, 98 |
| H1 the sentinel satisfies the READY predicate | high | 40, 97 |
| H2 `ff —` is undecidable: does a SessionStart hook fetch? | high | 11 |
| H3 node resolution against a file with two registry tables | high | 12, 63 |
| H4 `git grep -l` cannot name the missing token | high | 17, 45, 91 |
| H5 the re-match relocates the writer entry | high | 32, 85 |
| H6 no fragment home satisfies the `{kit}` readers and the destinations leg | high | 33, 60, 88 |
| H7 three new tracked files in the govkit surface, no descriptor row | high | 34, 87 |
| H8 the exemption reads an index that is empty at PreToolUse | high | 62 |
| H9 the acceptance fixture reaps the live run's keepalive | high | 79 |
| M1 AC5 claims inventory keys no extractor mints | medium | 10, 35, 86 |
| M2 three cells with no criterion; `live —` has no empty state | medium | 13, 95 |
| M3 a consumed card drops the Step 1 STOP and pins a stale BASE | medium | 24, 48 |
| M4 the replay invocation carries no `--registry` | medium | 43 |
| M5 an acceptance input a same-step sibling produces, with no edge | medium | 49 |
| M6 sequential and unmarked cannot both hold; `runs` is dead | medium | 51, 71 |
| M7 §5 cites decision 2 for a claim it does not make; a null return is unhandled | medium | 52 |
| M8 a mention-grep passes an orphan citation | medium | 92 |
| M9 basename citations are silently skipped | medium | 93 |
| M10 `ARMS_FLOORS` cannot cover an exit-coded refusal | medium | 94 |
| M11 the hooks kit alone denies with a remedy it cannot run | medium | 99 |
| L1 a user-docs carrier nobody builds | low | 55 |
| L2 two writers of one dossier in one parallel step | low | 56 |
| L3 two legs the unit's files are graded by, not listed | low | 104 |

Tally by raw id: **14 blocker · 17 high · 16 medium · 3 low** = 50. Two severities were RAISED from the
skeptic's verdict and are marked where they are argued: B4 (the skeptic said high on each of its four
ids) and H9 (the skeptic said medium). Two were folded DOWN by their cluster: 35 and 86 (skeptic: high)
sit in M1, because a vacuous criterion whose worst case is a loud ratchet red is not a high.

## Findings

| # | Sev | Unit(s) | Address | One line |
|---|---|---|---|---|
| B1 | blocker | TOOL-1, KICK-3 | TOOL-1 §2 S1; KICK-3 §2 S1, §3 | `merge` in the commit-shaped set denies the engine's Step 1 ff and Step 2b `merge-base` and repair commit, all pre-READY. |
| B2 | blocker | TOOL-1 | §2 S1, S4; §8 | The prompt path commits then pushes before preflight and kickoff; the push has an empty staged set and no exemption. |
| B3 | blocker | TOOL-2 | §2 S1, S3; §3; §4 Data model, Files touched | `settings-merge.py` emits `node "<path>"` only; no fragment can carry `bash`, `--card`, `--registry`, and the REPATH rewrites the live check-wiring entry. |
| B4 | blocker | TOOL-1, KICK-1 | TOOL-1 §2 S2, §6 AC2/AC3; KICK-1 §2 S3 | The card's toplevel is `/c/…` (bash `pwd`), the payload's is `C:\…`; equality with no normalisation denies every commit on every node. |
| H1 | high | TOOL-1 | §2 S2, §4 step 5, against §6 AC2 | "A line starting `READY —`" is satisfied by `READY — none yet`; the predicate and the criterion contradict. |
| H2 | high | KICK-1, KICK-3 | KICK-1 §2 S3, §4, §5; KICK-3 §2 S1 | `ff — moved` needs a fetch+ff at SessionStart; §5's batch has none and KICK-3 has the engine make it. |
| H3 | high | KICK-1 | §2 S4, §6 AC4 | AGENTS.md holds two `Machine/user` tables both naming `daily-agent`; the match rule is unstated; the real file is no fixture. |
| H4 | high | KICK-2 | §2 S1, S2; §4 | `git grep -l` prints files, not tokens; `-F` without `-w` matches `-1` inside `-10`. |
| H5 | high | TOOL-2 | §2 S1, S2; §6 AC1, AC2 | Two fragments, one command string, one possible marker: the re-match moves the startup entry to `resume|compact`. |
| H6 | high | TOOL-2 | §2 S1, S3, S4; §4; §7 | `{kit}` resolves two dirs up; the kickoff kit is flat and ships to `{prefix}/manifest-check.sh`; no spelling passes `hook destinations` and the card arm together. |
| H7 | high | TOOL-2 | §4 Files touched; §7 | Three new files under `skills/session-kickoff/**` and `tools/*` with explicit-include descriptors; `govkit selfcheck` reds, and it is in neither §7 nor Files touched. |
| H8 | high | TOOL-1 | §2 S4, §4 step 4, §6 AC4 | PreToolUse fires before `git add … && git commit` runs, so the staged set the exemption reads is empty. |
| H9 | high | TOOL-3 | §6 AC2 | The fixture resumes THIS build's live `RUN.md`; the resume section's first act reaps the live keepalive. |
| M1 | medium | TOOL-2 | §2 S7, §6 AC5 | No extractor walks `*.fragment.json`; there are no keys to claim and the criterion cannot red. |
| M2 | medium | KICK-1 | §2 S3, §5, §6 AC2 | `worktrees —`, `live —`, `recent —` have no criterion; `live —` has no state for a repo without the memory-tree kit. |
| M3 | medium | KICK-3 | §2 S1, §6 AC1 | A card in context skips the STOP on `MERGE_HEAD`/`UU` and pins the session-start BASE as the review base. |
| M4 | medium | KICK-1, TOOL-2 | KICK-1 §2 S4, S5; TOOL-2 §2 S1 | Replay writes a fresh card when none exists, and the replay command carries no `--registry`. |
| M5 | medium | KICK-3, TOOL-3 | KICK-3 §3, §6 AC1; TOOL-3 §3, §6 AC2 | Both fixtures need TOOL-2's wiring; neither declares the edge and all three share order 4. |
| M6 | medium | TOOL-5 | §2 S1, S5; §6 AC4 | "Sequentially" and "passes agent-cap unmarked" cannot both hold; `runs` from args is dead. |
| M7 | medium | TOOL-5 | §5 risks, §2 S4, §6 AC1 | Decision 2 records Explore's Bash access as UNVERIFIED, not discovery time; S4 catches a throw, not a null. |
| M8 | medium | KICK-2 | §2 S1, §10 | Existence by mention-grep re-spells the id grammar and passes an orphan citation; `corpus_ids.py` owns both. |
| M9 | medium | KICK-2 | §2 S1, S2; §4 | A basename citation is not a token, so it is neither checked nor marked `UNVERIFIED`. |
| M10 | medium | KICK-1, KICK-2 | KICK-1 §2 S9, §6 AC8, §7; KICK-2 S8, AC7 | `ARMS_FLOORS` counts `fail N "…"` recorder sites; an exit-coded refusal adds none. |
| M11 | medium | TOOL-1 | §4 Migration, Rollout; §3 Edges | The hooks kit does not require the kickoff kit; an adopter with one and not the other is denied with a remedy it cannot run. |
| L1 | low | KICK-1, KICK-2 | §5 user docs | "The kit README" does not exist and no Files touched creates it. |
| L2 | low | KICK-3, TOOL-2 | KICK-3 §2 S6; TOOL-2 §2 S7; build order | Two units edit `memory/map/features/session-kickoff.md` in one parallel step. |
| L3 | low | TOOL-5 | §7 | `lexicon naming predicates` and `install-prefix (shipped surface)` both grade the new files and are not listed. |

---

### B1 — blocker — TOOL-1 §2 S1, with KICK-3 §2 S1 and §3 — raw 1, 36, 64

**The defect.** S1 fires on "`git` followed by `commit`, `merge` or `push` as a word" when the payload
has no `agent_id`, and the deny's one remedy (S3) is `/session-kickoff`. The engine that remedy runs
issues, in the main loop and before Step 5 writes any READY line:

- Step 1 (`skills/session-kickoff/SKILL.md:49-51`): `fetch` + `merge --ff-only <remote>/<default>`
  "only when on the default branch with a clean tree" — the primary tree's normal state, and the
  exact session owner decision 2 forces through a kickoff by refusing a doc-only waiver. KICK-3 S1
  keeps this: "the engine runs only the fast-forward the card reports as not yet made", and "No card →
  the batch as today".
- Step 2b (`SKILL.md:114-124`): `git merge-base <remote>/<default> HEAD` for the re-stamp sha, and a
  repair commit made "NOW as part of kickoff". KICK-3 §3 leaves Steps 2 through 4 unchanged, so on a
  drifted manifest — routine in this repo — the repair `git commit` lands before Step 5's append.

The design record's regex, `\bgit\b.*\b(commit|merge|push)\b`, also matches `git merge-base` at the
`e|-` boundary and `git log --grep push`; the spec pins no regex of its own and exempts nothing beyond
S4's staged README. So the guard's only remedy runs the command the guard denies, inside the remedy.
The "denied forever" reading in raw 1 is overstated — a model can skip the ff and finish — but the spec
makes its own remedy trip the deny and states no carve-out, and in an unattended run the Step 1 STOP on
a failed ff ABORTs the run (`SKILL.md:231`).

**Fix.** State the exact predicate on the string-blanked view: `git`, optional flags, then a whole argv
token equal to `commit`, `merge` or `push` followed by whitespace or end, so `merge-base` never matches.
Then either drop `merge` from the set (the engine's ff is the one main-loop merge a pre-READY session
legitimately makes, and `push-main.sh`'s landing merge is post-READY by construction) or exempt
`merge --ff-only`. KICK-3 must state that the Step 2b repair commit is made AFTER Step 5's append, or
that Step 5 appends before the repair commits. Add near-miss arms to §7 for `git merge-base`,
`git merge --ff-only origin/main` and `git log --grep push`, each observed RED first.

**Left-shift.** A class arm in `tools/hooks/scratch-guard.test.sh`: extract every fenced `git …`
command from `skills/session-kickoff/SKILL.md` Steps 0–4 and feed each as a no-card payload, asserting
ALLOW. A deny whose stderr names a remedy owes a proof the remedy is reachable, and the remedy's own
text is the population. Gate the CLASS, not the three literals found here.

---

### B2 — blocker — TOOL-1 §2 S1 and S4, §8 — raw 2, 37, 58

**The defect.** S1 makes `push` commit-shaped. S4's exemption fires only when "the staged set adds a
`README.md` under a `builds/` segment whose staged blob carries `authorized-by: prompt`" — the commit
that creates the authorization. `tools/unattended/SKILL.template.md:283` (PROMPT path) and `:341`
(PLAYBOOK path) order step 4 as "Commit, then PUSH THE BRANCH. Both, in that order. Skip the push and
preflight refuses"; `:185` allows the kickoff "after preflight, never before"; step 1 runs engine Steps
0–4 only. So at the step-4 push: the README is in HEAD, the staged set is empty, no READY line exists,
and the push is a commit-shaped command with no exemption that can see it. The run is denied at its
first push with a remedy (`/session-kickoff`) the template forbids until after the preflight that
refuses without the push. Owner decision 3 — the prompt-path commit is exempted — is not met by the
spec as written, because the decision's purpose was to let the run reach preflight and the push is on
that path.

The one escape, `git commit … && git push` in a single Bash call so the index is still populated at
PreToolUse, is stated nowhere (and H8 shows it would still fail if the `add` shares the call). This
run's own build-folder push (`5f5ba3c4`'s ancestor) would have been denied had TOOL-1 already landed.

**Fix.** Either drop `push` from the set — the pushed commit was already gated at commit time, and the
lander runs the bar at the push boundary regardless — or extend S4 so a push is exempt when HEAD's
commit ADDED a `builds/*/README.md` carrying `authorized-by: prompt` that is absent from `@{upstream}`
(`git diff-tree --no-commit-id --name-only --diff-filter=A HEAD`, then `git show HEAD:<path>`). Keep
AC5's later-commit deny by requiring the README be NEW relative to upstream, never merely present. Add
an AC: after the exempted commit, `git push` exits 0 and the next unrelated commit exits 2.

**Left-shift.** The same class arm as B1, over a second population: the git commands the unattended
Skill template prints for steps 1–4 of both paths, replayed in a scratch clone with a bare upstream, as
consecutive payloads with no READY line. Any deny is a red. `check-unattended.sh` check 20 already
watches the template's `/session-kickoff` and `--preflight` literals; the arm belongs beside it, in the
hook's own suite, because the hook is what changed.

---

### B3 — blocker — TOOL-2 §2 S1, S3; §3; §4 Data model and Files touched — raw 7, 31, 59, 84

**The defect.** S1 specifies two fragments "in the shape `settings-merge.py` reads" whose commands are
`bash <hook_path> --card --registry <registry>` and `bash <hook_path> --card --replay`; S3 gives the
check-wiring entry a fragment whose command is `bash tools/check-wiring.sh --session`. Read at source:

- `tools/settings-merge.py:146` — `_FRAGMENT_KEYS = tuple(AGENT_CAP)`, exactly
  `{name, event, matcher, marker, hook_path}`; `load_fragment` refuses anything else.
- `:168-170` — `_command(hook_path)` returns `node "${CLAUDE_PROJECT_DIR}/<hook_path>"`
  unconditionally. No interpreter field, no argv field. The header (`:34-37`) says everything else
  about an entry "stays fixed, because no consumer has asked to vary it".
- `:227-231` — an entry whose command contains the marker is REPATHED in place to that node form.

So no fragment can produce a bash launcher or a verb: the merger would write `node ".../manifest-check.sh"`
twice with no `--card`, and applying the S3 fragment against the live `bash ".../tools/check-wiring.sh" --session`
entry rewrites it to `node ".../tools/check-wiring.sh"` with no `--session` — the wiring check breaks at
every session start while looking wired. AC1 ("command names the resolved checker path and the verb")
is unreachable by the declared merger. §3 forbids changing commands beyond the matcher, §4 Alternatives
rejects widening the schema as "a second grammar", and Files touched budgets only "the re-match
branch" for `settings-merge.py`. S6's "the fragment carries the token" names a `<registry>` token no
reader expands: `resolve_hook_path` (`:174-198`) resolves `{kit}` and nothing else. The unit is
unbuildable against the seam it cites, and the seam's own docstring says why.

**Fix.** Decide and state one route. (a) Widen the schema explicitly: an optional `interpreter`
(`node|bash`, default `node`) and an `args` array, emitted by `_command`, with a merger self-test arm
applying a bash-with-args fragment and asserting the rendered command verbatim; make the REPATH compare
the whole rendered command; state how an adopter supplies `--registry` (a `.governance/deploy.toml` key
rendered into the fragment, or `--hook-arg` on the merger), since a verbatim fragment cannot carry a
per-adopter value. Rewrite §3's no-command-change bullet and §4 Alternatives to say which widening was
accepted and why. (b) Or drop the fragment route for these three entries, write `.claude/settings.json`
directly, and delete the wiring arm's fragment dependency in S4. Either way, list the schema and
docstring edits in Files touched.

**Left-shift.** A `settings-merge` self-test arm that, for EVERY tracked `*.fragment.json`, applies the
fragment to an empty settings object and asserts the rendered command against a `command:` line the
fragment's own README states — a parity between what the kit says it wires and what the merger emits.
Today the shipped fragments are node-only, so the arm is a no-op that catches the first bash fragment
anyone adds; that is the point.

---

### B4 — blocker — TOOL-1 §2 S2, §6 AC2/AC3, with KICK-1 §2 S3 and §4 — raw 3, 38, 61, 98

**The defect.** S2 requires "a `tree —` cell whose toplevel equals the toplevel derived from `cwd`".
The two sides are written in different alphabets and neither spec names a normalisation. Measured on
this node at the synthesis, not argued: `git rev-parse --show-toplevel` prints
`C:/projects/coding-governance/...`; `manifest-check.sh:72-73` then runs `cd "$ROOT" && pwd`, whose own
comment says it normalises "to the shell's path flavor (git-bash: C:/ vs /c/)", and prints
`/c/projects/coding-governance/...`; node's `path.resolve` prints `C:\projects\coding-governance\...`.
KICK-1 writes the card through the script that owns that ROOT; the hook receives the payload's native
`cwd` and derives its toplevel by "the same `.git` walk `agent-cap.js` already implements" —
`gitCommonDir` at `agent-cap.js:1512`, which returns the COMMON dir rather than the worktree toplevel
the spec says it derives, a second gap on the same line.

Every node in the §2 registry is Windows + Git-Bash. A byte-equality compare therefore fails on all
four, and every main-loop commit is denied with "oriented in A, committing in B" on a single tree.
AC2's green arm and AC3's sibling-worktree arm are both fixture-authored by the self-test in the hook's
own spelling, so the suite is green while the shipped pair denies the fleet. The unit's own §5 names
"deny-forever if the READY predicate is wrong" as its top risk; this realises deny-forever from the
predicate beside it. The class is measured in this repo already: `check-verifier-fanout.sh`'s header
records MSYS `/c/` against `C:/` matching NOTHING, and `tools/hooks/scratch-guard.js:56-69` ships
`buildComparablePath`, whose header calls the drive fold "load-bearing and … found by the smoke test,
not by reasoning". The spec re-invents the comparison beside the function that exists to do it.

**Why blocker, raised from the skeptic's high.** Severity is what ships. What ships is a hook that
denies every main-loop commit on every registered node, whose only exits are the escapes S6 lists as
the guard's ceiling (a subagent commit, a script, a hand-written card in the right spelling) — and the
fix commit is itself a main-loop commit. Loud, yes; but the exit from the state is an evasion the header
names, and the suite that was supposed to catch it is green. That is the wrong-mechanism class, not the
wrong-document one.

**Fix.** KICK-1 S3: write the toplevel in ONE declared spelling — the `--show-toplevel` output before
the `pwd` normalisation, forward-slash drive-letter form. TOOL-1 S2 and Inventory: both sides pass
through `buildComparablePath` before the compare, named as the reused seam; `resolveCommonDir` must
also return the directory where `.git` was found, which is the toplevel, and say so. AC3 gains an arm
where the card holds `/c/…` and the payload `C:\…` for one tree, expecting exit 0.

**Left-shift.** The arm that consumes the WRITER's bytes rather than a hand-written cell: the hook
self-test runs `skills/session-kickoff/manifest-check.sh --card --session t` in its fixture repo and
feeds that file, unedited, to the hook with `process.cwd()` as the payload `cwd`. A cross-kit arm is the
only shape that can catch a spelling fold between two kits, and it is one line longer than the
fixture-authored one.

---

### H1 — high — TOOL-1 §2 S2, §4 Data model step 5, against §6 AC2 — raw 40, 97

**The defect.** S2 requires "a line starting `READY —`" and step 5 denies only on "no `READY —` line".
KICK-1 S3 closes every startup card with `READY — none yet`, which starts with `READY —`. As written,
the predicate allows every fresh card, so the deny never fires in the one window it exists for. AC2
demands exit 2 on a sentinel-only card. The normative text and the criterion contradict; the builder
reads §2 and §4 first. High rather than blocker because the build-level rule "every gate arm is
observed RED before it lands" makes AC2's arm catch it — if the builder honours the rule.

**Fix.** Spell the predicate in S2 and step 5: a `READY —` line whose tail is not `none yet`, naming
the sentinel bytes as KICK-1's; or require the tail to carry `node <tag>` as the charter's READY shape
does. Mirror the exclusion in KICK-2 S5 so the append replaces only the sentinel.

**Left-shift.** The sentinel is one string in two kits. Put it in ONE place — the writer prints it and
the hook's README states it — and add a parity arm on the pattern of `tools/check-playbook-parity.sh`
that compares the hook's regex source against the sentinel the writer emits, so a re-spelling on
either side reds the bar.

---

### H2 — high — KICK-1 §2 S3, §4 Data model, §5; KICK-3 §2 S1 — raw 11

**The defect.** The `ff —` cell has three values: `moved <old>..<new> | unchanged | skipped: <why>`.
`moved` can only be written if `--card` itself runs `fetch` + `merge --ff-only` at every SessionStart.
Yet S3 describes the cell as reporting "the fast-forward the engine's Step 1 makes" — a step that has
not run when the hook writes the card; §5 budgets "one git batch, ~1.6 s" whose design-record source
(`build/…orientation-design.md:118-120`) lists no fetch; and KICK-3 S1 has the engine "run only the
fast-forward the card reports as not yet made". Whether a SessionStart hook performs a network fetch
and mutates local `main` with nobody asking, inside the hook timeout, is undecidable from the spec set,
and KICK-3's consume clause cannot be written until it is. No AC observes the cell in any state.

**Fix.** Decide and state it. The lazy and safe answer: `--card` never fetches and always writes
`ff — skipped: not run at session start`, and the engine keeps the ff. If a fetch is wanted, it is
only on the primary tree, on the default branch, with a clean tree, and the `moved` case is the only
one that can name shas. Add an AC observing the cell on this worktree (`skipped:`) and one forced
`unchanged` or `moved` fixture.

**Left-shift.** A self-test arm that runs `--card` in a scratch repo whose remote is one commit ahead
and asserts `git rev-parse HEAD` is unchanged afterwards. A hook that must not move refs owes a test
that it did not, whichever way the decision falls.

---

### H3 — high — KICK-1 §2 S4, §6 AC4 — raw 12, 63

**The defect.** S4 resolves the node by "matching `$USERNAME` against the Machine/user cell of the
registry table" and prints `node — UNKNOWN` on "no unique cell match". TOOL-2 S6 pins `AGENTS.md` as
this repo's `--registry`. That file carries a `Machine/user` column twice: `:62-64`, the node registry
(`| a | daily-agent |`), and `:155-157`, the charter's embedded §2 example (`` | `a` | `daily-agent` | ``,
backticked). `$USERNAME` on this node is `daily-agent`. Node `b`'s cell is `agent5 @ DESKTOP-3J1O6CD`,
so the match rule (equality, prefix before ` @`, backtick stripping) decides the outcome and none is
stated. Read literally, the node that writes this spec gets `node — UNKNOWN` on its own registry, or
resolves by the accident that one copy is backticked. AC4's two fixtures (exactly one match, none) are
self-test-authored and never the real file's shape; AC1 and AC2 run without `--registry` and check no
`node —` value, which S4 also leaves unspecified.

**Fix.** State: read only the first table under a `## Node registry` heading, or dedupe matches on
Tag before the uniqueness test; strip backticks; match `cell == $USERNAME` or `cell` starts with
`$USERNAME @`; absent `--registry` prints `node — UNKNOWN: no --registry`. Add the real `AGENTS.md`
(via `git show HEAD:AGENTS.md`) as an AC4 fixture expecting tag `a`.

**Left-shift.** The real registry as a fixture is the gate: `manifest-check.test.sh` asserts the tag
the card derives from `AGENTS.md` at HEAD equals the tag whose row names `$USERNAME`. The registry can
gain a table, a backtick or a variance column, and the arm reds the day the parser stops agreeing with
the file it was written for.

---

### H4 — high — KICK-2 §2 S1, S2; §4 Data model — raw 17, 45, 91

**The defect.** S1 pins "ONE `git grep -l -F -f <tokenfile>` over the memory root" as the id
existence check and §10 calls that the reused seam; S2 promises one `UNVERIFIED — <token>` line per
missing token. `-l` prints matching FILE names only, so the single call cannot say which token was
absent; a builder either loops (the 25–50 s shape §4 rejected) or annotates wrongly. And `-F` without
`-w` lets `FAMILY-slug-1` match inside `FAMILY-slug-10` — the class `memory/gotchas/id-matched-as-a-substring.md`
records ("every id ending in a 1-up sequence is a prefix of nine others"). AC2's "an id no record
defines" arm is green on the wrong evidence.

**Fix.** Spell the call as `git grep -h -o -w -F -f <tokenfile> -- <memory root> | sort -u` and
set-difference against the token file — still one spawn, per-token presence, word-anchored. Say the
same for `git ls-files -- <paths>` (its output is per path already). Add an arm with `X-1` absent and
`X-10` present expecting `UNVERIFIED — X-1`. See M8 for the stronger shape.

**Left-shift.** The `X-1`/`X-10` arm is the regression gate for this instance. The class gate is
M8's: delegate existence to the reader that owns the id grammar rather than re-spelling it in shell.

---

### H5 — high — TOOL-2 §2 S1 against S2; §6 AC1, AC2 — raw 32, 85

**The defect.** S2 re-matches "when an entry carrying the fragment's marker sits in a group whose
matcher differs from the fragment's": the entry MOVES. S1 ships two fragments for one script under two
matchers. With `_command` producing byte-identical commands for both (B3), the only marker either can
carry is a substring of `manifest-check.sh`, and `merge()`'s dedup is `marker in command`
(`settings-merge.py:228`). Applying the replay fragment after the card fragment finds the marker under
`startup|clear` and moves it to `resume|compact`; re-applying the card fragment moves it back. AC1's
"two SessionStart groups … each carrying one entry" is unreachable, the merger's own header promise
(apply-twice-changed = 0) breaks, and every adopter run ping-pongs the wiring. Even with B3's schema
widened, the spec assigns the two fragments no distinct marker.

**Fix.** Require distinct markers per fragment and say what they are (the arg substring
`--card --replay` versus `--card --registry`, which presupposes B3's `args` field). Scope the re-match
to entries whose marker AND event match and whose matcher differs. Add an AC applying both card
fragments in both orders, twice, asserting two groups of one entry each and byte-identical output.

**Left-shift.** An idempotence arm in the merger self-test over EVERY tracked fragment: apply the
whole set in file order, then in reverse, then the whole set again, and assert the three results are
byte-identical. The merger's header already promises this; the arm makes the promise a gate.

---

### H6 — high — TOOL-2 §2 S1, S3, S4; §4 Inventory; §7 `hook destinations` — raw 33, 60, 88

**The defect.** Three readers resolve `{kit}` as the fragment's grandparent directory:
`settings-merge.py:186-198` (`Path(frag_file).parent.parent`), `check-wiring.sh:459-470`, and
`check-hook-destinations.sh:71-77` (both `dirname(dirname(frag))`, blanked when `.`). The kickoff kit
is `kind = "flat"` with `to = "{prefix}/manifest-check.sh"` (`tools/govkit/entries/kickoff-manifest.kit.toml:5,13`),
so the destinations leg's only declared checker path is `tools/manifest-check.sh`, a file that does
not exist in this repo, where the checker is `skills/session-kickoff/manifest-check.sh`. A fragment
beside the engine resolves to `skills/manifest-check.sh`; the skeptic reproduced the leg's refusal
("`-> skills/session-kickoff/manifest-check.sh`, which NO kit.toml rule ships"). A literal
`tools/manifest-check.sh` passes the leg and reports the hook file missing in the card arm. The
depth-1 `tools/check-wiring.fragment.json` has the repo root as grandparent, so `{kit}/check-wiring.sh`
resolves to a root-level file that does not exist, and spelling `tools/` into the fragment is the
carried-prefix ban `tools/hooks/README.md` states. In an adopter the flat kit's one-level install breaks
the two-up rule again, so the card arm prints `skip` forever. No spelling satisfies AC4's `ok card`
and §7's `hook destinations` together without a descriptor change the spec does not budget.

**Fix.** State the fragments' tracked home and the resolved `hook_path` under each of the three
readers. Add descriptor `to` rows that make the resolved path a declared destination (or declare a
flat-kit token rule and teach all three readers, listing them in Files touched). Put the check-wiring
fragment inside a kit directory that owns `check-wiring.sh` (`check-wiring.kit.toml`'s home is `tools`,
kind flat — same problem) or extend the resolver with a declared depth. Add an AC that runs
`bash tools/check-hook-destinations.sh` at the landing commit.

**Left-shift.** Extend `check-hook-destinations.sh` to require every tracked `*.fragment.json` — not
only the `hook_path` it names — to be claimed by a descriptor rule, and to print the resolved path per
reader on a mismatch. Three resolvers with one rule and no parity arm between them is the drift the
finding found; the leg should assert all three agree on every fragment.

---

### H7 — high — TOOL-2 §4 Files touched; §7 Gates — raw 34, 87

**The defect.** `skills/session-kickoff/orientation-card.fragment.json`,
`orientation-replay.fragment.json` and `tools/check-wiring.fragment.json` are new tracked paths inside
`registry.toml`'s declared surface (`skills/session-kickoff/**`, `tools/*`), and both owning
descriptors use explicit include lists (`kickoff-manifest.kit.toml:11`, `check-wiring.kit.toml:11`).
The skeptic reproduced `python tools/govkit/govkit.py selfcheck` exiting 1 with "2 unclaimed … a new
moving part must red until a declaration claims it" on two of them staged. `govkit selfcheck` is an
unguarded `subject: repo` leg (`tools/gate-legs.json:1032`), named in neither §7 nor Files touched;
`registry.toml:270` shows even a test file needed an exempt row. The process-monitor fragment is claimed
by that kit's `include = "**"` — raw 87's mechanism was wrong on that file and right on the other three.
Consequence in adopters: the card fragments S5 tells them to apply are never shipped, because a flat
kit ships only what its include list names.

**Fix.** Add `tools/govkit/entries/kickoff-manifest.kit.toml` and `check-wiring.kit.toml` (or registry
exempt rows) to Files touched, `govkit selfcheck` to §7, and an AC that `govkit apply --dry-run` lists
all four new fragments as shipped.

**Left-shift.** A spec-lint arm in `check-spec-tokens.py`: every NEW path in a spec's Files touched
that matches a `registry.toml` surface glob must be accompanied in the same table by a descriptor path
under `tools/govkit/entries/` or by `registry.toml`. The leg that reds at landing is already there; the
lint moves the red to the spec, where it costs a line instead of a cycle.

---

### H8 — high — TOOL-1 §2 S4, §4 Data model step 4, §6 AC4 — raw 62

**The defect.** PreToolUse fires before the Bash command runs. For the ordinary
`git add <folder> && git commit -m …` in one call, the index the hook inspects with
`git diff --cached --name-only --diff-filter=A` is empty, so S4's exemption cannot fire; it fires only
when the `add` was a separate earlier tool call, which nothing states. AC4 passes because its fixture
stages by hand before feeding the payload, and AC4's red-when forbids the worktree-file fallback that
would have covered the single-call form.

**Fix.** Also accept an UNTRACKED (absent from HEAD and from the index) `builds/*/README.md` in the
working tree carrying `authorized-by: prompt` — still the creating commit, still fails AC5's
folder-in-HEAD case. Add an arm for the add-and-commit single-call payload against an empty index.

**Left-shift.** Same population as B2's arm: the literal commands the unattended template prints for
step 4 include the add; feeding them verbatim as payloads is the gate.

---

### H9 — high — TOOL-3 §6 AC2 — raw 79

**The defect.** AC2's fixture is "this build's own `RUN.md`, resumed once from a fresh session". The
Resume section (`tools/unattended/SKILL.template.md:670-683`) makes the first act after reading the
record "REAP the recorded id, and only then schedule a replacement", and states the record cannot be
corrected with the new id. Executed from a second session against the live run, the acceptance run
deletes the running build's keepalive, and the replacement it schedules is recorded nowhere: the live
session's close reaps an id that is already gone and attests `keepalive-reaped` over a job the fixture
session left firing. The template names exactly that outcome — "a keepalive firing forever with a
green `keepalive-reaped` attestation over it" (`:676`) — as the failure the reap order exists to
prevent. The spec's "cost: one kickoff" omits it. Raised from the skeptic's medium: an acceptance
criterion whose execution orphans a scheduled job in the live store is an operational harm, not a
document defect.

**Fix.** Fixture on a throwaway run-state file in a scratch clone with its own keepalive id, or run AC2
at close after the live run's keepalive is already reaped; state which, and add the reap to the cost
line.

**Left-shift.** A `check-spec-tokens.py` rule: a `fixture:` line naming the build's own `RUN.md`, or
any path under the build folder the spec is in, is refused with the reason. The class — an acceptance
run that mutates the state it is verifying — is the one the reference review's B3 named in
`aClosedDocket`, one level up.

---

### M1 — medium — TOOL-2 §2 S7, §6 AC5 — raw 10, 35, 86

**The defect.** S7 has the dossier claim "the two fragment keys the codebase-map inventory will
enumerate". `tools/codebase-map/map_extractors.py:89-135` `EXTRACTORS` enumerates gate-legs, kits,
git-hooks, workflow-scripts, skill-engines, rendered-skills, gotcha-classes, guides, backlog-shards and
lexicon-verbs; nothing walks `*.fragment.json`, `grep fragment tools/codebase-map/` hits only a
scenario fixture, and none of the three shipped fragments is a key in any dossier. Files touched adds
no extractor. AC5 is therefore either vacuous — the coverage leg is green whether or not the dossier
mentions the fragments — or, if the dossier claims the two names anyway, the ratchet reds them as
claims naming dead keys. The could-not-fail class §7 forbids; folded down from the skeptic's high on 35
and 86 because the worst case is a loud red, not a silent pass.

**Fix.** Drop S7 and AC5 and refresh the dossier prose on touch marked NOT OBSERVED, as KICK-3 S6 does;
or scope a fail-closed `hook-fragments` extractor (glob `*.fragment.json`) into this unit, claim all
five fragments in their kits' dossiers, and give it its own RED observation.

**Left-shift.** A `check-spec-tokens.py` rule: an AC naming "inventory key(s)" must name an
`EXTRACTORS` class that exists in `map_extractors.py`. The predicate is a grep; the class it gates is
the vacuous-selector one the tree already has a gotcha for.

---

### M2 — medium — KICK-1 §2 S3, §5 error states, §6 AC2 — raw 13, 95

**The defect.** S3 ends "Observed by AC2", but AC2 asserts only the `tree —` line, BASE and the
closing sentinel; `worktrees —`, `live —` and `recent —` have no criterion in §6. `live —` is "read
from the generated `LIVE.md` at the memory root the conf declares", yet `manifest-check.sh` today reads
`MEMORY_ROOT`, `.memory-tree.conf` and `LIVE.md` zero times (the descriptor's gate-leg comment records
it, `TOOL-aScouredKit-12`), `kickoff-manifest.kit.toml` declares `requires = []`, and the memory-tree
kit is Optional (`PLAY-aCandidStub-1`). `ff —` has a `skipped:` shape and `node —` an `UNKNOWN` shape;
`live —` has neither, and §5's error-state row lists no state for an absent conf or file. An adopter of
a "project-agnostic" kickoff kit without the memory-tree kit has no specified behaviour: a refusal (no
card, every commit denied by TOOL-1) and an invented count are both readings the spec permits. Raw 95's
"S7 makes any derivation failure a refusal" overstates S7; the unspecified state stands.

**Fix.** Add the three cells to AC2 with their derivations (`git worktree list | wc -l`, LIVE.md table
rows minus header, `git log --oneline -5`); add `live — skipped: <why>` to the shape and S3 for no conf
or no LIVE.md, with an arm; note in §3 that the conf read is conditional and never a refusal.

**Left-shift.** A self-test arm running `--card` in a scratch repo with no `.memory-tree.conf`,
asserting exit 0 and the `skipped:` cell. The cross-kit read is the new dependency; the arm is what
keeps it optional.

---

### M3 — medium — KICK-3 §2 S1, §6 AC1, with KICK-1 §2 S3/S5 — raw 24, 48

**The defect.** KICK-1 fixes the card's tree cell as `clean|dirty <n>` at session start and never
updates it; `now —` is computed at replay and never stored, and no `now —` exists at all for a second
unit in a session without a compaction. KICK-3 S1 makes a card in context SATISFY the orientation
batch, and AC1 pins the READY BASE to the card's `tree —` BASE and forbids a second `status --short`.
Two consequences. The engine's Step 1 STOP on a foreign `MERGE_HEAD` or `UU` entry (`SKILL.md:61-63`;
unattended exit 3 ABORT, `:225-227`) reads exactly the entries a count cannot carry, so a run resumed
after dying mid-merge kicks off without the STOP that exists for that state. And any kickoff after a
commit in the same session — the prompt path's exempted build-folder commit makes this systematic — or
after a compaction or `--resume` pins a BASE stale by every commit since, so the charter's diff-scoping
runs against the wrong sha.

**Fix.** State which Step 1 items the card satisfies (branch, worktrees, node) and which the engine
still runs: one `rev-parse HEAD` plus `status --short`, seconds. AC1 should require BASE equal to
`git rev-parse HEAD` at kickoff, preferring the `now —` HEAD when one is in context, never the card's.

**Left-shift.** A write-boundary gate in KICK-2's `--append`: refuse a READY line whose `base <sha>`
differs from `git rev-parse HEAD` at append time, naming both. A stale BASE then cannot land on the
card at all, whichever engine text produced it.

---

### M4 — medium — KICK-1 §2 S4, S5; TOOL-2 §2 S1 — raw 43

**The defect.** S4 resolves the node only from the file `--registry <path>` names and gives no default
for an absent flag; S5 writes a fresh card when replay finds none; TOOL-2 S1 spells the replay command
as `--card --replay` with no registry. A card first written under `resume|compact` — a session started
before wiring, or after a common-dir clean — carries `node — UNKNOWN` for its whole life, and the
startup matcher never re-fires to repair it.

**Fix.** Add `--registry <registry>` to the replay fragment in TOOL-2 S1, or state in S4 the default
when the flag is absent. One line either way.

**Left-shift.** An arm: `--card --replay` with no card on disk produces a card whose `node —` cell
names a tag, not `UNKNOWN`.

---

### M5 — medium — KICK-3 §3 Edges, §6 AC1; TOOL-3 §3 Edges, §6 AC2 — raw 49

**The defect.** KICK-3 AC1's fixture is "a session started after `TOOL-aReplayedCard-2` wires the
hook"; TOOL-3 AC2 needs a fresh session's card to append to. Neither spec declares
`consumes-from TOOL-aReplayedCard-2`, and all three units carry order 4 in one parallel step.
`TEMPLATE-SPEC.md` §3 names "a criterion resting on something the unit does not build" as what an
edge must declare, and `BUILD-METHOD.md` M6 clause 2 forbids parallel passes where one's acceptance
input is the other's output. Neither AC is observable inside its own step; the acceptance ledger cannot
be written until a sibling lands.

**Fix.** Add `consumes-from TOOL-aReplayedCard-2` to both Edges lists, and either order KICK-3 and
TOOL-3 after TOOL-2 or mark AC1/AC2 as observed at the build's close.

**Left-shift.** `gen_build_index.py` already reads every spec's edges to render the build order; a
rule that a `fixture:` line naming a sibling unit id (or "after <id> wires") requires a
`consumes-from` edge to that id is a parse it already does most of.

---

### M6 — medium — TOOL-5 §2 S1 against S5; §6 AC4 — raw 51, 71

**The defect.** S1 spawns `runs` agents "from a two-element array literal, sequentially"; S5 says the
script passes `agent-cap.js` "unmarked: its only fan is a two-element literal". `tools/hooks/README.md:61-84`
admits a sequential `await agent(` loop only under `gov:sequential-agents(<K>)` on a strict
`for (const x of <identifier>)` header over a proven-bounded identifier; the skeptic fed the shapes to
the hook via `check-verifier-fanout.sh`: an unmarked loop is DENIED, a marked loop with the literal in
the header is DENIED, `Array.from({length: args.runs})` is DENIED; only `const RUNS = [0, 1]` with a
marked `for (const i of RUNS)` (marked, not unmarked) or two hand-unrolled awaits (unmarked, `runs`
meaningless) pass. An unmarked literal fan is PARALLEL, which runs two kickoffs concurrently in one
repo and contaminates the wall figure the harness exists to measure. `runs` is an arg while the
literal fixes the count at two.

**Fix.** Fix runs at 2 as a `gov:fixed-verifiers` const literal with a `gov:sequential-agents(2)` loop
header (or unroll two awaits); drop `runs` from args or pin it to 2 in the schema; say in S5 that the
script passes WITH the sequential marker.

**Left-shift.** AC4 already runs `check-verifier-fanout.sh` at landing; the gate exists. The
spec-level fix is to name the marker, so the first draft passes rather than the third.

---

### M7 — medium — TOOL-5 §5 risks, §2 S4, §6 AC1 — raw 52

**The defect.** §5 cites "design record §7 decision 2" for "the agent definition's discovery time".
Decision 2 (`build/…orientation-design.md:449-452`) records as UNVERIFIED whether an Explore-typed
agent can run Bash and the Skill tool; the record contains no mention of discovery time. That
unverified item bears directly on AC1's first live arm — Explore reading its wall via `date` in Bash —
and S4 catches only a spawn throw, while the harness's documented dead-agent shape is a null return
(AC1's red-when names it; no scope item handles it). If Explore cannot run Bash the Explore half of the
matrix is dead for a reason S4 does not record.

**Fix.** Re-cite decision 2 correctly. Add an S4 clause for a null return and for an arm that spawned
but reports it could not execute a step. Let AC1 fall back to the default workflow agent type when
Explore refuses Bash, recording which type ran.

**Left-shift.** The harness's own record: every arm carries `spawned | null | threw | refused-step`
as a closed field, so a dead arm is a named value the caller can grep, never a zero.

---

### M8 — medium — KICK-2 §2 S1, §10 — raw 92

**The defect.** S1 decides id existence by grepping MENTIONS over the memory root and re-spells the
id grammar (`FAMILY-<slug>-<seq>` from the conf's families) in shell. `tools/memory-tree/corpus_ids.py`
owns that grammar; its check 14 exists precisely because an id can be "cited but never defined", and
its waiver list means orphans exist in the tree today. `TOOL-cSpliceWarden-6` rules that a check
grading a declared grammar DELEGATES to the reader that owns it, because "spelling a second row
predicate in shell let five of six evasions pass". AC2's arm is worded "an id no record defines",
which a mention-grep cannot test: an orphan citation — including one the card itself wrote in a
previous session — passes it, so `UNVERIFIED` is absent on exactly the ids the corpus already knows are
undefined.

**Fix.** Add a `--print-defined-ids` verb to `corpus_ids.py` and have the append join against it — one
python spawn replaces the git grep, same two-spawn budget. Cite check 14 and `TOOL-cSpliceWarden-6` in
§10. Arm with an orphan id.

**Left-shift.** The delegation IS the gate: one id grammar, one reader, and `hygiene-parity.test.sh`
already asserts the kit's readers agree. A second predicate in shell is the thing that rots.

---

### M9 — medium — KICK-2 §2 S1, S2; §4 Token extraction — raw 93

**The defect.** The path rule borrowed from `tools/check-spec-tokens.py:21` ("a slash AND an
extension") means a basename citation such as `run-gates.sh:407` is not a token: neither checked nor
annotated, which contradicts S2's "a present one is not mistaken for a vetted one". The lint the rule
comes from measured this population — 854 of 1721 citations cite a kit file by basename, the house
style — and its answer is SKIP AND COUNT, printed every run. The engine's Step 4 rows and the recall
output cite by basename constantly, so every such row on the card reads as vetted with no `UNVERIFIED`
beside it: the silent-skip class §7 forbids, over half the corpus.

**Fix.** Either resolve a basename against `git ls-files` when it is unique (a miss when ambiguous),
or print `skipped — <n> basename citation(s)` in the append output and store it on the card so
`--check` can read it back. State which in S1 and add an arm.

**Left-shift.** The stored `skipped —` line is the gate: `--card --check` reds when a card carries
basename-shaped rows and no skipped line, so the skip can never be silent on disk.

---

### M10 — medium — KICK-1 §2 S9, §6 AC8, §7 New-arm rows; mirrored in KICK-2 S8, AC7 — raw 94

**The defect.** `ARMS_FLOORS`' population is `fail <n> "…"` call sites (`check-arms.py:53`,
`FAIL_RE = \bfail (\d+) "`), and `manifest-check.sh:133` defines `fail()` as the numbered MANIFEST-check
recorder (`echo "MANIFEST check $1 FAILED — $2"; status=1`), reached only after a manifest is resolved.
The `--card` verb dispatches before that point and its refusals are exit-coded (S2 "exits non-zero",
S7; KICK-2 S3 exit 1, S4 exit 2). A card refusal written as `fail N` would misnumber a manifest check
and print the wrong sentence; written as `echo …; exit 2` it is invisible to `check-arms.py`. The
script's own header (`:59-66`) already records that print-only verbs add no `fail` branch. AC8's
"moved by the number of fail sites added" is satisfied by zero, and the three New-arm rows name a
floor that structurally cannot cover the arm; only `FLOOR_ASSERTIONS` in the test file can.

**Fix.** State the refusal shape (the existing `MANIFEST env ERROR — …; exit 2` form, or a `refuse()`
helper with its own exit code), drop `ARMS_FLOORS` from S9/AC8 and the gate rows, keep
`FLOOR_ASSERTIONS`. Same edit in KICK-2 S8/AC7.

**Left-shift.** `FLOOR_ASSERTIONS` moving in the same commit is the gate that fits; the spec should
name it alone. If `refuse()` is introduced, extend `check-arms.py`'s `FAIL_RE` to count it — one regex
edit gates the new class for every future verb.

---

### M11 — medium — TOOL-1 §4 Migration and Rollout; §3 Edges — raw 99

**The defect.** The deny lands in the hooks kit, whose descriptor declares `requires = ["settings-merge"]`
(`tools/hooks/kit.toml:7`) and which is not in the registry's default selection
(`tools/govkit/registry.toml:36`); its only remedy and the only card writer ship with
`kickoff-manifest`. Step 5 denies on "card absent", so an adopter selecting the hooks kit alone is
denied every main-loop commit with a remedy it cannot execute. Migration's "the designed state —
TOOL-2 orders the writer's wiring before this file lands in an adopter" holds only when both kits are
installed. `TOOL-aUnmannedHelm-4` records that kit-dependent rules are KIT-CONDITIONAL, and the recall
arm (`check-wiring.sh:434-445`) is the precedent for treating an un-adopted sibling as a skip.

**Fix.** Either add `kickoff-manifest` to the hooks kit's `requires` and list the descriptor in Files
touched, or make the deny fail open with one stderr line when no `orientation/` directory and no
`manifest-check.sh` exist in the tree; cite `TOOL-aUnmannedHelm-4`.

**Left-shift.** An arm: the hook run against a scratch tree with no checker present exits 0 and prints
the one line. `govkit selfcheck` already validates `requires` closure if the row is taken instead.

---

### L1 — low — KICK-1 §5 user docs; KICK-2 §5 — raw 55

Both §5 rows name "the kit README" as the carrier for the verb family. `git ls-files skills/session-kickoff/`
shows no README, neither Files touched creates one, and a new tracked file under
`skills/session-kickoff/**` needs a descriptor claim (H7's class). **Fix:** point the row at the
script header and `WIRE-INTO-PROJECT.md`, or add the README with its registry row and `govkit selfcheck`
to §7. **Left-shift:** H7's spec-lint rule covers this instance too.

### L2 — low — KICK-3 §2 S6; TOOL-2 §2 S7; the build order — raw 56

Both Files touched list `memory/map/features/session-kickoff.md`, and both units carry order 4.
M6 `parallel-when-disjoint` clause 1 requires non-intersecting write sets; TOOL-4 §3 applies that rule
to itself at order 1 for the same reason. **Fix:** route both dossier edits through KICK-3 (TOOL-2's
fragment keys do not exist, M1), or serialise TOOL-2 after KICK-3. **Left-shift:** `gen_build_index.py`
renders the order from the specs; intersecting Files touched within one parallel step is a join it can
red on.

### L3 — low — TOOL-5 §7 Gates — raw 104

`.lexicon.conf:23` arms `js:js-regex:probe`, so every function `tools/workflows/orient-counterfactual.js`
defines is graded by `lexicon naming predicates`; `check-install-prefix.sh:54` puts every tracked
`tools/*` and `*.template.*` file — the script and `orient.agent.template.md` — in `install-prefix`'s
population. §7 lists neither, while every sibling spec adding such files lists both; a unit verified
against its four named legs lands red at the lander for legs it never ran (the branch-bar skip class
the auto-memory records). **Fix:** add both legs and name the verb cell the new functions use.
**Left-shift:** a `check-spec-tokens.py` rule that a Files touched path matching a leg's declared
population (the lexicon LANGS and the install-prefix globs are both machine-readable) requires that
leg in §7.

---

## The cross-read on the four M2 axes

Where two specs disagree, both are named, because a fix to one that leaves the other is a fold.

- **Interface.** TOOL-2 S1 versus `settings-merge.py`'s schema (B3). TOOL-1 S2 versus KICK-1 S3 on
  the toplevel's spelling (B4). TOOL-1 S2 versus KICK-1's sentinel (H1). TOOL-2 S1's two fragments
  versus S2's marker-keyed re-match (H5). KICK-1 S4's `--registry` versus TOOL-2 S1's replay command
  (M4). KICK-1's `ff —` values versus KICK-3 S1's "the ff the card reports as not yet made" (H2).
- **Ordering.** TOOL-1 at order 3 lands the deny before TOOL-2 wires the writer at order 4; the
  Rollout names the window, and B1 shows the hand-invoked kickoff the Rollout prescribes for that window
  is itself denied. KICK-3 and TOOL-3 at order 4 rest on TOOL-2 at order 4 (M5). KICK-3 S6 and TOOL-2
  S7 write one dossier in one step (L2). The Step 2b repair commit versus Step 5's append (B1).
- **Scope.** KICK-1 S3's `live —` cell adds a cross-kit read the descriptor's `requires = []` does
  not declare (M2). TOOL-2 S6 calls `--registry` "a settings value" while S1's fragment is verbatim
  data that cannot carry it (B3). TOOL-1 lands in a kit whose `requires` does not name the writer's kit
  (M11). TOOL-2 Files touched omits every descriptor the unit's new files need (H7, H6).
- **Acceptance.** KICK-3 AC1 pins BASE to the card's; the engine pins it to `rev-parse HEAD` (M3).
  TOOL-1 AC2 denies the sentinel; S2 allows it (H1). TOOL-2 AC5 names keys no inventory mints (M1).
  KICK-1 S3 says "Observed by AC2" for cells AC2 does not read (M2). TOOL-3 AC2's fixture is the live
  run (H9).

**Prior art the specs re-invent.** `buildComparablePath` in the very file TOOL-1 edits (B4).
`corpus_ids.py`'s id grammar and check 14, with a ruling that says delegate (M8).
`check-spec-tokens.py`'s skip-and-count over basename citations, adopted without the count (M9).
`agent-cap.js`'s `.git` walk, cited for a toplevel it does not return (B4). The recall arm's `skip`
posture for an un-adopted sibling (M11).

**Harness assumptions, and which were verified.** The SessionStart matcher vocabulary
(`startup|resume|clear|compact`) rests on the design record's appendix verdicts 3 and 16 and was not
re-verified here against the harness documentation; the specs cite it correctly. PreToolUse fires
before the command executes — H8 rests on it and it is the documented order. A Workflow script's
`agent()` loop shape was verified by the skeptic against the hook itself (M6). Whether an Explore-typed
agent can run Bash is UNVERIFIED in the design record and stays so (M7). The hook payload fields the
deny reads (`session_id`, `tool_use_id`, `cwd`, `agent_id`) are the ones `scratch-guard.js` and
`agent-cap.js` already read; no spec assumes a field the existing hooks do not consume.

## What this pass did NOT do, said rather than implied

- **It read documents and the source they cite; it drove no fixture.** The synthesis re-read at source:
  `settings-merge.py:146,168-170,199-231`; `skills/session-kickoff/SKILL.md:47-63,112-124`;
  `tools/unattended/SKILL.template.md:185,283,341,670-683`; `tools/hooks/scratch-guard.js:56-69`;
  `skills/session-kickoff/manifest-check.sh:72-73,133`; `AGENTS.md:62-64,155-157`;
  `tools/codebase-map/map_extractors.py:89-135`; `tools/memory-tree/check-arms.py:53`;
  `tools/hooks/README.md:58-86`; `tools/govkit/entries/kickoff-manifest.kit.toml` and
  `check-wiring.kit.toml`; and it measured the three path spellings on this node. Three reproductions
  are the skeptic's, reported as such and not repeated: `govkit selfcheck` on the staged fragments (H7),
  `check-hook-destinations.sh`'s resolver on the candidate fragment homes (H6), and
  `check-verifier-fanout.sh` on the loop shapes (M6).
- **A spec audit grades what a document says.** The four blockers were all found by reading code the
  specs cite, which is the same limit `aClosedDocket`'s audit recorded; the defect a correct-sounding
  sentence hides in an unbuilt mechanism is out of reach here, and TOOL-4's zero is subject to it.
- **The design record's appendix was read for the claims the specs rest on, not re-audited.** Verdict
  13 (a node spawn at 0.8–1.1 s), verdict 35 (the batch's cost), and decision 2 (M7) were checked for
  what they say; their measurements were not re-run.
- **Precision was 0.48, under §8's floor.** Reported rather than smoothed; the response by §8's own
  rule is to tighten the prose-conformance lens's priming, not to widen the fan. Round 2 should re-audit
  the revised set at its new blobs, with a lens dedicated to the four blockers' fixes and one to the
  cross-spec axes, since eleven of the twenty-seven defects here span two specs.
