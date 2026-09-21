**Serves:** diff-review TOOL-aHonedRuleset-1 TOOL-aHonedRuleset-2 TOOL-aHonedRuleset-3 TOOL-aHonedRuleset-4 TOOL-aHonedRuleset-5 TOOL-aHonedRuleset-6 TOOL-aHonedRuleset-8

# Closing diff review — aHonedRuleset

Node `a` · 2026-09-06 · Tier-2 · **ROUND 1** · adversarial fan (4 finder lenses → 5 skeptic batches → this synthesis). Every claim below was re-read at source in the worktree, never taken from a spec or a commit message.

Range reviewed: `6ec402bd3eb7f9cb5ce6257b0f60348ae3e593fc...6455882f40700543681d52a430ee28a3ce2fb7d8` — 21 commits, 42 files, +3554/-337, seven units, all CLOSED.

## Verdict: CLEAN WITH FIXES

Nothing blocks the landing. Two findings are HIGH: one ships a retired rule to adopters in the charter itself, and one leaves three arms of a kit self-test unable to fire, including the only arm that exercises a refusal branch this build added. Five MEDIUM and two LOW follow. The build's own product — the prose deletions, the §13 move, the parity row, the govkit selection — is sound; every finding here is a *second half left standing*, which is the class the build spent three of its seven units closing.

## Review shape

Raw 18 · confirmed 15 · refuted 3 · unverified 0 · precision 0.83.

The 15 confirmed collapse to **9 distinct defects** — five subjects drew two or three independent lenses each (`selftest.py:1086` twice, `memory-tree/README.md:148` twice, `README.md:195` twice, the build-method dossier three times, the test fixture twice). I merged them at write time and kept the strongest evidence from each. That merge is mine, not the pipeline's; see the integrity line below.

## Run integrity

- Lenses 4/4 returned, 0 DIED.
- Skeptic batches 5/5 returned, 0 DIED.
- 0 contradictory verdicts demoted to unverified, 0 spurious verdicts discarded, 0 duplicates removed by the pipeline.

No stage died, so a zero count in this report is evidence of absence rather than evidence of a hole. The one qualification is the duplicate count: the pipeline discarded none, and the collapse from 15 to 9 above was done by hand in this synthesis.

## Findings

| # | Sev | Where | What |
|---|-----|-------|------|
| F1 | HIGH | `coding-governance-agents.template.md:68` (+ `AGENTS.md:140`) | The charter still states the stamp rule unit 5 retired — a third home the new parity row does not watch. |
| F2 | HIGH | `tools/unattended/check-unattended.test.sh:977` | One `reset_tree` discards the check-12 fixture commit; three arms below it can no longer fire, including the new refusal's only arm. |
| F3 | MED | `tools/memory-tree/README.md:148` | Ships a pointer to a BUILD-METHOD budget "DECLARED ON ITS OWN LINE 8" that unit 6 deleted. |
| F4 | MED | `memory/map/features/build-method.md:76` | Dossier prose still describes the deleted caps, and inverts which axis bound first. |
| F5 | MED | `tools/memory-tree/README.md:195` | The method's pointer table still routes the six interactive exits to the kickoff engine. |
| F6 | MED | `coding-governance-agents.template.md:361` | The new connective puts two unenforced rules on the gate-held side of the partition. |
| F7 | MED | `tools/govkit/selftest.py:1086` | The new 7d/7e fixture copies the whole repo root, dragging in every sibling worktree. |
| F8 | LOW | `skills/session-kickoff/SKILL.md:221` | "Six other steps" — §13 enumerates six exits across five steps. |
| F9 | LOW | `tools/unattended/check-unattended.sh:1451` | KICKOFF_EXITS is documented as a §13 count and implemented as a whole-file count. |

---

### F1 — HIGH · the charter is an unretired third home for the stamp rule

`coding-governance-agents.template.md:68`, rendered identically at `AGENTS.md:140`.

The §1 kickoff-manifest merge exception still reads `post-merge HEAD on the default branch, the merge-base otherwise; a commit can't embed its own sha`. Unit 5's commit B changed what the rule says at what it called "both homes and nowhere else": `skills/session-kickoff/manifest-check.sh:200` now holds `STAMP_SHA_RULE="sha = HEAD on any branch"`, interpolated into four failure texts, and `MANIFEST-TEMPLATE.md:29-33` states the same and explicitly retires the older spelling, naming `KICK-cSettledDocket-1` as the record that found the merge-base cannot satisfy check 5 on a feature branch.

So the value the checker was changed to reject is the value the charter still instructs an agent to write. This is the operating ruleset and it ships to every adopter. The new PAIRS row does not reach it: `tools/check-playbook-parity.sh:125` extracts from MANIFEST-TEMPLATE.md and manifest-check.sh only, so the charter's spelling has no watcher at all.

**Fix.** Change the parenthetical in both carriers to `post-merge HEAD; a commit can't embed its own sha`, dropping the default-branch/merge-base split, and re-render AGENTS.md. The template has 621 bytes of headroom, so this costs nothing.

**Left-shift.** Add the charter template as a third side of the PAIRS row unit 5 built — the extraction machinery already exists and the phrase is on one physical line. A cheaper alternative that also holds: one grep leg refusing the string `the merge-base otherwise` anywhere in the tracked tree. Either way, the rule that "a value stated in prose beside the source that owns it rots" gets a machine, not a promise.

### F2 — HIGH · one `reset_tree` disarms three arms of the unattended self-test

`tools/unattended/check-unattended.test.sh:977`.

The check-12 section builds its fixture at :935-949: `reset_tree`, then it writes the synthetic `skills/session-kickoff/SKILL.md`, appends `KICKOFF_ENGINE` and `KICKOFF_EXITS` to `.unattended.conf`, and **commits** (`git add -A && git commit -q -m engine`). `PRISTINE` was pinned at :214, long before that commit, and `reset_tree` is `git reset -q --hard "$PRISTINE"; git clean -qfd`. The `reset_tree` at :977 therefore does not just clean the tree — it destroys the section's own fixture.

Everything after it runs on a tree with no kickoff engine and no `KICKOFF_ENGINE` key, and check 12 is gated on both (`check-unattended.sh:1425` requires a non-blank `KICKOFF_ENGINE`, `:1426` requires the file to exist, `:1441` requires `KICKOFF_EXITS`). Consequences, all introduced by this diff:

- `:980` — the new arm asserting `KICKOFF_EXITS declares a floor … and there is no protocol at` cannot fire, because check 12 is skipped entirely. The refusal branch unit 3 added at `check-unattended.sh:1450` has **no working arm**, which is §7's "a new gate is not landed until its failing case has been observed", failed on the fixture side.
- `:983` — `git checkout -q -- skills/session-kickoff/SKILL.md` errors, since the path is untracked at PRISTINE. `set -u` only, no `set -e`, so the suite continues past it.
- `:984` and `:988` — both `sed -i 's|^KICKOFF_ENGINE=.*|…|'` calls silently match nothing; the key is not in the conf. The NOPE-engine arm at `:985` cannot hit.
- `:989` — `same "a blank KICKOFF_ENGINE turns the check off" "$(run)" ""` asserts byte-empty output, but `rm -f memory/guides/UNATTENDED-PROTOCOL.md` at `:978` is never undone, and check 10's `_c10_cmp "$SHIP" "$LIVEDOC"` at `:1346` is unconditional and returns 2 on a missing half, so every later `run()` emits `one half of the protocol pair is missing`.

One correction to the finder reports, which both proposed adding a `reset_tree` after the new arm: that fix reproduces the bug, because `reset_tree` is exactly what discards the fixture commit.

**Fix.** At `:977` restore to HEAD rather than to PRISTINE — `git checkout -q -- .` keeps the engine commit — and after the arm's `hit` at `:980` add `git checkout -q -- memory/guides/UNATTENDED-PROTOCOL.md` to put the deleted half back before `:983`.

**Left-shift.** `check-arms.py` already demands a positive assertion naming each branch's own failure text, and this arm satisfies it — the assertion exists, it just cannot pass. Static arming cannot see this class. The suite is off the merge bar by the owner ruling of 2026-08-23 and already carries 26 by-design failures, so a new red is camouflage. The smallest thing that fixes that: pin the expected-failure set the way `check-arms.py` pins its unarmed set — a shrink-only count or signature list of the known-red arms, so a 27th failure is a named delta rather than more noise. Until that exists, the compensating check belongs in the DoD: a unit editing a kit checker or its test runs the suite and records the assertion counts as its acceptance witness.

### F3 — MED · the memory-tree kit README still points at the deleted budget

`tools/memory-tree/README.md:148`.

Under `## The build method's displaced sections`, still: `memory/guides/BUILD-METHOD.md holds itself to a budget DECLARED ON ITS OWN LINE 8` and `Read the pair there; both figures were retyped here once and both were stale within a build`. Commit `a3bde74b` deleted the whole `Budget: <=24 KB, <=350 lines` passage from both the template and the render; `d16858ec` removed the two dependent sentences. Neither commit touched this README. Line 8 of BUILD-METHOD.md is now blank and no cap is declared anywhere in the file.

This is the shipped kit README, so every memory-tree adopter is routed to a declaration that exists in no tree. It is also the stated justification for the whole displaced-sections arrangement, which now rests on a constraint nothing states.

**Fix.** Drop the budget sentence and the `Read the pair there` instruction; keep the surviving rationale — the method is re-read WHOLE at every pass boundary, so it grows by displacement — and note that no figure is declared since TOOL-aHonedRuleset-6.

**Left-shift.** The generalisable gate is a dangling-pointer scan: a check that refuses any tracked prose asserting a fact about a *specific line number* of another file (`ON ITS OWN LINE 8`, `line 12 of`) unless a co-located marker in the target confirms it. Cheaper and narrower, and probably the right first move: extend the existing kit-dogfood-parity pair so a change to `BUILD-METHOD.template.md` reds until the kit README is re-read in the same commit.

### F4 — MED · the build-method dossier describes the pre-build state, and inverts it

`memory/map/features/build-method.md:76`.

The Gaps bullet still reads `The caps are declared on the method's own line 8; compare with awk 'END{print NR}' memory/guides/BUILD-METHOD.md and wc -c`, and closes with `The line axis binds before the byte axis, so M1's displacement rule stays load-bearing`. Both caps are gone, so the two commands it hands the next reader have nothing to compare against. The second clause was already backwards against its source: the deleted prose read `**The BYTE half binds first**`, and `a3bde74b`'s own message names the byte-half-binds-first sentence among its deletions.

This dossier's `[paths].globs` (lines 24-25) claim exactly the two files unit 6 edited, so §1's `dossier prose refreshed on touch` applied. `git log -1` on the dossier is `78958d59`, which predates this build — it was never touched. Line 17 of the same dossier lists `amendment-leaves-its-other-half-standing.md` among its own `gotcha-classes`, so the dossier names the class it fell to.

**Fix.** Replace the bullet with the post-deletion fact: BUILD-METHOD declares no local budget since TOOL-aHonedRuleset-6 (owner ruling), it is capped only by the memory-tree hygiene class cap for `guides/`, and M1's displacement discipline survives as a norm with no enforced figure. A Gaps entry whose subject no longer exists is not a gap; deleting it is also acceptable.

**Left-shift.** The map's coverage gate enforces key claims only, so nothing reds on stale dossier prose. The cheap ratchet: a leg that reds when a commit touches a path claimed by a dossier whose own file is not in the same commit. That is mechanical, has no false-negative mode for this class, and would have caught F4 at the moment `a3bde74b` was written.

### F5 — MED · the method's pointer table still routes the six exits to the engine

`tools/memory-tree/README.md:195`.

The row reads `skills/session-kickoff/SKILL.md + memory/guides/SESSION-KICKOFF.md — starting a unit, closed scope, the tier rule, the six interactive exits`, under a heading that says `Read these, do not restate them`. Commit `f4ea3587` moved the enumeration into `memory/guides/UNATTENDED-PROTOCOL.md` §13; SKILL.md now carries only a pointer, and grep over both named files finds no enumeration. The receiving carrier's own row (~:202) lists `mandate, run state, phases and witnesses, DoD, keepalive, landing` and does not claim the exits.

The table is not decoration: `BUILD-METHOD.md` M11 designates it by name as the carrier map — "Names here, scopes there — one hop" — so this row is the single home for what SKILL.md owns. The one hop now lands on a file that only forwards. `check-method-carriers.sh` grades carrier declaration and pointing, not row scopes, so nothing reds. Shipped kit file, so adopters inherit the mis-route. Unit 3's own AC8 grepped for `Step 5b exit`, a string this row does not contain, which is why it passed over it.

**Fix.** Move `the six interactive exits` out of the SKILL.md row and into the UNATTENDED-PROTOCOL.md row, spelled as `§13's six interactive exits and their no-owner-turn resolutions`.

**Left-shift.** Same ratchet as F3: a commit that removes a named scope from a carrier should red until the pointer table is in the same commit. The table's rows are already machine-readable — `check-method-carriers.sh` parses them — so the incremental cost is a set-difference over the scopes named, not a new parser.

### F6 — MED · the new connective claims gate cover for two rules with no arm

`coding-governance-agents.template.md:361`, rendered at `AGENTS.md:425`.

Unit 2 deleted three sentences that each map onto a numbered `fail` arm of `check-microformats.sh` and replaced them with `A gate holds the block's own syntax; what follows binds EMISSION, which no gate sees`. Two of the rules the connective leaves on the gate-held side have no arm: `Tail fields are separated by ' · ' and by nothing else`, and `alternation inside one is the ASCII '|'`. The gate's arms are sentinel, joiner count, joiner position, bare parens, colon-as-label, and placeholder case — nothing else.

Verified by staging the break. Rewriting one definition to `- \`gates — GREEN, <leg>; <leg> | <leg> …\`` — comma and semicolon separators plus a bare ASCII pipe outside a placeholder — leaves `bash tools/check-microformats.sh` at exit 0 with `microformats OK — 11 definition(s) graded, 11 keyword(s) derived`.

The reason this matters beyond accuracy: `a gate holds it` was this build's licence for deleting three sentences. The sentence it left behind extends that licence to two rules nothing enforces, and the next editor applying the same reasoning deletes a rule with no machine home. §7 says a gate's own header states what it does NOT check; here the charter breaks that from the other side.

**Fix.** Either narrow the sentence to name what is actually held (`The joiner, bare parentheses, a labelling colon and placeholder case are held by a gate over this block`), or add the two missing arms — a separator arm asserting every field break in a definition is ` · `, and an alternation arm rejecting a bare `|` outside `<…>`. Mirror into AGENTS.md.

**Left-shift.** Adding the two arms *is* the left-shift, and it is the better half of the choice: it makes the sentence true rather than smaller, and the definition block is eleven lines, so the arms are cheap. Whichever is chosen, stage the break and observe RED before landing — the same rule this finding was found by.

### F7 — MED · the new govkit fixture copies the repository root

`tools/govkit/selftest.py:1086`.

`shutil.copytree(HERE.parents[1], gcopy, ignore=shutil.ignore_patterns(".git"))` — `HERE` is `tools/govkit`, so `parents[1]` is the repo root, unconditionally, with only `.git` filtered. `.gitignore` holds `__pycache__/` and `*.pyc`; the thing that actually keeps `.claude/worktrees/` out of git is `.git/info/exclude:12`, which the copy drops along with `.git`. The ignore pattern also strips each nested worktree's `.git` *file*, so those checkouts stop looking like repos and the fixture's `git add -A` commits them.

Measured on node `a`'s primary tree today: 22,786 non-`.git` files, 21,030 of them under `.claude/worktrees/` across 17 live checkouts, against 1,657 in a linked worktree. Reproduced end to end at roughly 130-147 s added to the leg. `selfcheck` matches rooted prefixes, so nested `tools/*` paths never enter the surface and the verdict is unaffected — I ran selfcheck inside the fat copy and it exited 0. This is cost, scope and flakiness, not a wrong grade. The flake is real: those worktrees hold running sessions rewriting lock files and mailboxes, and a file vanishing between scandir and copy2 raises `shutil.Error` and reds the leg for a reason unrelated to govkit.

The blast radius is bounded — the leg is `chunk: selftests` / `subject: kit`, so neither the default bar nor `GATE_FULL=1` runs it, and the ceiling is not breached. But any session doing kit work from the primary tree, where the documented invocation runs, pays it.

**Fix.** Build the fixture from the population selfcheck actually grades: materialise from `git -C <root> ls-files -z`, which gives tracked working-tree content and nothing excluded. Minimum viable alternative: replace the ignore with one that also drops `.claude`.

**Left-shift.** An assertion inside the fixture itself, one line after the copy: the scratch repo's tracked file count must be under a declared ceiling, refusing loudly if the copy scope ever widens again. `scratch_gov` at :844 copies `HERE` only, so the ceiling also documents why this arm is the exception.

### F8 — LOW · "steps" where §13 says "exits"

`skills/session-kickoff/SKILL.md:221`.

The replacement pointer says `Six other steps of this engine also stop to ask`. §13 enumerates six *exits* at five distinct steps — Step 0 carries two of them, the ambiguous worktree parent and no-git-anywhere. The prose this diff deleted used the correct noun, and §13's heading, the `KICKOFF_EXITS` key description and `check-unattended.sh`'s failure text all say exits.

This pointer is the only thing left in the engine after the enumeration moved, so its count is what a reader carries forward. A reader auditing the engine for six stopping steps finds five and concludes an exit was dropped — which is precisely the state the `KICKOFF_EXITS` floor exists to detect, reported by prose instead of by the gate.

**Fix.** `Six other interactive exits of this engine stop to ask`.

**Left-shift.** None worth building. A noun-choice error in one sentence is not a gateable class, and the honest record is that this is a documented manual check at review time.

### F9 — LOW · KICKOFF_EXITS counts the whole protocol, not §13

`tools/unattended/check-unattended.sh:1451`.

`nex=$(tr -d '\r' < "$LIVEDOC" | grep -cE '^[0-9]+\. \*\*Step ' || true)` runs over all 675 lines. `.unattended.conf:55` says `It counts in memory/guides/UNATTENDED-PROTOCOL.md section 13, which is where those exits live`, and the kit example at :85 repeats `section 13`. Both declarations promise a section-scoped count.

They agree today only by accident: all six matches are lines 661-674, inside §13 at 652-675. The masking path is reachable rather than theoretical — the protocol already uses the `N. **Bold` top-level idiom 29 times across other sections, and §12 is exactly the kind of section that would enumerate steps. One such item leading `**Step ` raises the numerator and lets an exit be dropped from §13 while the shrink-only floor still passes, which the conf's own comment names as the thing nothing else notices.

**Fix.** Scope the count to its declared section, and refuse by name when the §13 heading is absent, the way the missing-protocol branch immediately above it does:

```sh
nex=$(tr -d '\r' < "$LIVEDOC" | awk '/^## 13[.] /{f=1;next} f&&/^## /{f=0} f' | grep -cE '^[0-9]+\. \*\*Step ' || true)
```

**Left-shift.** The fix carries its own arm: stage a `**Step ` list item outside §13 in the fixture protocol and assert the floor still reds when an exit is deleted from §13. That arm is the gate; without it the scope fix is another thing only ever seen passing. Note it lands in the same file as F2, so fix that fixture first.

## Not filed

- **The template-size WARN is pre-existing, not this build's.** `bash tools/check-template-size.sh` exits 0 but prints `grew past its recorded high-water: 48378 -> 48531`. The `coding-governance-agents.template.md` row in `tools/template-size-highwater.txt` is untouched in this range — the only edit is the SKILL.md row, bumped DOWN 18215 → 16991 to match unit 3's move, which is correct. The template was 49144 at base, so the warn predates the diff; this build shrank the overrun from +766 to +153. Worth a `--bump` at some point, not a finding here.
- **Byte arithmetic verified.** Template 48531 / 49152 (621 free, 98.7%), AGENTS.md 63868, SKILL.md 16991 — all matching the build's own figures. `check-playbook-parity.sh` is green (`15 kit(s) documented or waived · pairs in agreement`), so the five `sed`-extracted phrases in the agent-cap bullet each survive verbatim on one physical line, and unit 5's new PAIRS row agrees. `check-microformats.sh` is green at 11 definitions and 11 derived keywords.
- **The §13 move itself is clean.** The six exits are in the installed protocol and the template, the engine keeps a pointer, `check-unattended.sh` counts in the installed copy, and BUILD-METHOD's two `Step 5b exit 5` references were repointed. The three misses above are all in files unit 3's AC predicates did not reach — a pointer table, a dossier and a kit README — not in the move.

## Left-shift summary

One theme carries five of the nine findings. Every one of F3, F4, F5 (and F1 in a different register) is the same shape: an amendment landed in the files its acceptance criteria named, and a second carrier kept describing the world before it. The build closed that class three times inside BUILD-METHOD and did not have a mechanism, only attention. The mechanism that would have caught all of them is one ratchet, not four: **a commit touching a path claimed by a dossier or named in a carrier table reds until that dossier or table is in the same commit.** The map tree already knows the claims and `check-method-carriers.sh` already parses the rows, so it is a set difference, not a new parser. That is the single highest-value follow-up this review produces.
