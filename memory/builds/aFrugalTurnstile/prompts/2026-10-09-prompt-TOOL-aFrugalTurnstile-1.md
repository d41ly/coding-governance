# The owner's prompt, verbatim, and the coordination taken before the push

**Serves:** research TOOL-aFrugalTurnstile-1 TOOL-aFrugalTurnstile-2 TOOL-aFrugalTurnstile-3 TOOL-aFrugalTurnstile-4 TOOL-aFrugalTurnstile-5 TOOL-aFrugalTurnstile-6 TOOL-aFrugalTurnstile-7 TOOL-aFrugalTurnstile-8 TOOL-aFrugalTurnstile-9 TOOL-aFrugalTurnstile-10 PLAY-aFrugalTurnstile-1 DEPL-aFrugalTurnstile-1

Handed to `/unattended` as the `--prompt` value on 2026-10-09, node `a`. The value carried whitespace
and named no readable file, so by the Skill's routing table it is the prompt itself and is taken
verbatim. It names no tracked id of this repo: `ABL-aYieldedFork-1` is an inCMS id, cited as the
incident, and `ABL` is not a gov family.

```text
Cut the cost of landing a build through gov's push boundary. The owner calls the current price unacceptable: build aYieldedFork (inCMS C:/projects/incms/main + NicoCares C:/projects/incms/main/vendor/nicocares-package) took more than 6 hours to land across the two repos, almost all of it re-running full bars. Sequence this AFTER the item-5 build (self-tests reclassified to subject=kit) that the session 'Gov: retire adopters' install-guards CRLF and keepalive duties' is running; rebase on whatever it lands.

MEASURED on 2026-10-09, node a (16 cores, 32 GB, Windows/MSYS):
- inCMS paid 5 full bars, about 25 to 60 min each, before one landed. One red was a lint line in a test, one a lexicon pin another session's landing tipped over, two were load-sensitive migration tests (subprocess alembic upgrade, empty stderr) that pass 10/10 alone, and one was a records leg. nc paid 3 full bars. Each repo's build had ALREADY run a full bar at its unattended --close, over the same merged tree.
- Why every push to main was FULL. (i) pre-push's staleness predicate counts lag with `git rev-list --count R..tip`, i.e. ALL commits, against GATE_FULL_MAX_LAG=10, so any --no-ff build merge carrying more than 10 commits forces FULL: 'the recorded full green is 254 commits behind the tip (bound 10)'. (ii) inCMS: 'the leg manifest differs from the one the recorded green was earned on'. This is inCMS ABL-aYieldedFork-1: the stamp predicate hashes {prefix}/gate-legs.json, never the manifest a GOV_GATE_CMD bar hands run-gates. (iii) nc: 'the pushed tip is a merge whose second parent the recorded green does not cover', although the close bar graded the identical merged tree.
- Reuse exists but is never used at the boundary: run-gates' GATE_REUSE=1 skips a leg whose input key matches a recorded green, but .githooks/pre-push never sets it and a reusing run cannot stamp gate-full-green. So a one-line fix after a red costs another whole bar.
- Contention: gov's own bars, inCMS's and nc's ran at once on one host. The gate queue is per repository common dir. The gov session measured process spawns at 20.4x their floor, and inCMS bars hit gov-bar's ceiling and pytest-serial-heavy timeouts.

BUILD THESE FOUR, each a unit with its failing case staged first:

A. ONE GREEN PER TREE. A full green proves a TREE, so key the push boundary's reuse of it on the tree's content fingerprint (run-gates already records `fingerprint` and pre-push already re-derives a tree digest). A push whose tip tree equals a tree with a recorded full green, under the same manifest and bar command, runs nothing new. That covers the close bar's tree reaching main as a --no-ff merge. Count the staleness bound in first-parent landings, not all commits. Fix ABL-aYieldedFork-1 in the same unit: the stamp must hash the manifest the bar actually ran (a GOV_GATE_CMD bar's GATE_LEGS), so an adopter wrapper bar can stamp a usable green at all.

B. RE-RUN ONLY WHAT FAILED. After a red, the next run of the same bar on a tree that differs only by the fix runs the failed legs plus every leg whose input key moved, and reuses the rest from that run's own ledger. The result may stamp gate-full-green when every reused verdict came from a full run of the same manifest and bar on the same base lineage. Keep the 'any missing term means execute' safety direction.

D. ONE BAR PER MACHINE. Make the gate queue host-wide (not per common dir), so concurrent bars from different repositories and worktrees queue rather than starve each other into time-outs, ceilings and load flakes. A queued wait is announced with its holder. Keep the per-repo turnstile semantics otherwise.

E. LAND ON A SCOPED BAR, FULL BAR AFTER THE MERGE. Today the charter says the push boundary 'DECIDES whether a full bar is owed, against a recorded green and a declared staleness bound', but inCMS's unattended rule demands a full green bar for every unattended landing. Design and build the mechanism that makes the cheaper path safe: the push lands on the scoped bar (diff-guarded legs plus a full green within the bound), a full bar runs after the merge (on a dedicated runner, remote CI, or the next idle local slot), and its red is binding. It blocks the next landing until fixed or reverted, through a recorded state the boundary reads; it is never just a log line. Write the protocol and charter text for it (UNATTENDED-PROTOCOL landing rule, charter section 1 Landing), and state plainly what an adopter must declare to opt in. Relaxing inCMS's own CLAUDE.md unattended condition 3 is the adopter's change; the adoption session will make it after this lands, on the owner's yes.

Out of scope: the self-test reclassification (item 5, its own run); per-test flake fixes inside adopters' suites; GATE_DOC_PATHS declarations in adopters (the adoption session does those).

Measure before and after on a fixture and on a real adopter push: bars paid per landing, and wall time. One gov pin; specs, closing review, full bar, land via push-main. When it LANDS or stops, notify the session named 'Coding Governance adoption [c3f980]' with the gov head sha, what landed, and what each adopter must declare to use it.
```

## The coordination, taken before the push

The prompt sequences this build after "item 5". Asked over the cross-session channel on 2026-10-09,
the session named in the prompt answered, condensed only where it repeated itself:

```text
Item 5 is NOT STARTED. There's no slug yet, and it waits on the owner's go in my session. No ETA.
Expected write set: tools/govkit/entries/push-main.kit.toml (three [[gate_leg]] rows go
subject="kit", pre-push.test.sh gets a ceiling); tools/gate-legs.json rows for those legs;
tools/run-gates/run-gates.sh, only the summary line that prints "N held: every self-test";
tools/govkit/govkit.py, a deployer check; kit version bumps for push-main, run-gates and govkit.
Overlap with you: run-gates.sh, at one summary line only. One candidate the adoption session floated,
NOT owner-approved: pre-push's full-green staleness counting first-parent landings. If you take it,
I'll drop it from item 5.
```

This run answered that the first-parent count is unit A's (the prompt names it), that it proceeds now
on main `5a836bf0f` because item 5 has not started, that it leaves the held-summary line alone, and
that whichever build lands second reconciles. "Sequence this AFTER item 5" is therefore read as: land
after item 5 if item 5 lands first, and reconcile against it either way. No owner turn was taken: the
prompt answers every field the kickoff skeleton asks for, ACCEPTANCE and GATES included.
