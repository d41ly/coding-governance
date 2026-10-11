# The owner's prompt, verbatim, and what orientation found before the push

**Serves:** research TOOL-aBenchedProbe-1 TOOL-aBenchedProbe-2 DEPL-aBenchedProbe-1 DEPL-aBenchedProbe-2

Handed to `/unattended` as the `--prompt` value on 2026-10-09, node `a`. The value carried whitespace
and named no readable file, so by the Skill's routing table it is the prompt itself and is taken
verbatim. Its backslash-escaped inner quotes are written here as plain quotes. It names no tracked
id of this repo. No owner question was asked: acceptance and gates derive from the prose and the code.

```text
Item 5 of the install-guards retirement, owner-approved on 2026-10-09 (the owner chose to land aLevelledCopy first, then run this as its own build). Repo: C:/projects/coding-governance (gov); start from origin/main, which was 5a836bf0f when aLevelledCopy landed.

Problem. Three hook self-tests are declared subject = "repo" in tools/govkit/entries/push-main.kit.toml, so govkit emits them that way into adopters' gate-legs.json and every adopter bar runs them. run-gates holds only subject=kit legs, and their guards don't help, because a push to main runs GATE_FULL=1, which ignores guards. The three [[gate_leg]] rows are:
- pre-push self-test (bash .githooks/pre-push.test.sh), guard [".githooks/"]
- pre-push bar self-test (python3 .githooks/pre_push_bar_selftest.py), guard [".githooks/"]
- push-main self-test (bash {prefix}/push-main.test.sh), guard push-main.sh / .githooks/
gov's own run-gates README says a held leg is "a self-test of a KIT'S OWN SOURCE", whose job "does not exist in a repository that copy-installs the kit and never edits it". All three are engine files adopters ship verbatim. Measured cost in NicoCares for the pre-push self-test alone, over its last six bars: 815s, 1420s, 1469s, 2135s, 1815s, then 3500s+ on 2026-10-09, the slowest leg every time. The owner's rule: self-tests run on demand only.

Scope:
(a) Declare all three subject="kit" in the descriptor, so adopters hold them unless GATE_SELFTESTS=1, while gov's own bar keeps running them. Check whether gov's tools/gate-legs.json mirrors the descriptor rows and move it in step.
(b) Make run-gates' summary line accurate. It prints "N held: every self-test", which is false while any self-test is declared repo. Edit ONLY that summary line in tools/run-gates/run-gates.sh.
(c) A deployer-side check, e.g. in govkit selfcheck, that flags a [[gate_leg]] whose argv runs a gov-shipped *.test.sh or *selftest* file while its subject is not kit, so this class cannot recur. Observe it RED on a staged break.
(d) Declare a wall-clock ceiling on the pre-push.test.sh leg. Cost is a verdict, and it more than quadrupled in two days with nothing noticing.

Out of scope: pre-push's full-green staleness counting (rev-list --count R..tip versus first-parent landings). The concurrent unattended run aThriftyLanding, session 'Gov: cut the bar price of landing a build', owns it in its unit A. That run also writes .githooks/pre-push, the stamp predicate, GATE_REUSE and the turnstile in tools/run-gates/run-gates.sh, memory/guides/UNATTENDED-PROTOCOL.md and the charter's §1 Landing. Do not touch those. Whoever lands second reconciles. Once preflight passes, SendMessage that session this run's slug and write set.

Lessons from aLevelledCopy (memory note pass-commit-must-carry-run-md):
- Every unit's pass commit must stage memory/builds/<slug>/RUN.md, which holds its --dispatch/--brief rows. check-commit exempts it, and brief-recorded reds a unit whose row lands one commit late.
- Run python tools/codebase-map/gen_map.py --write after any rename or new function, before the close.
- Bump each touched kit version once, after the last move, and check carriers with tools/check-kit-versions.sh and govkit epoch --base <BASE>. Re-stamp the kickoff manifest's last-audit when run-gates.sh is staged.
- The host was heavily contended by frozen-clone suites in %TEMP%/ms4 and ms5. Never kill processes this run did not start.

When the build LANDS (or stops for any reason), notify 'Coding Governance adoption [c3f980]' with the gov head sha, what landed, and whether adopters need anything beyond a normal govkit update. Both adopters plan to pull 5a836bf0 together with this pin. Also notify 'Gov: cut the bar price of landing a build'.
```

## What orientation found, before the roster was written

- **gov's own bar already holds all three.** `tools/run-gates/run-gates.sh` holds a leg when its
  subject is `kit` OR its chunk is `selftests`, by owner ruling of 2026-08-26, and gov's manifest
  puts all three in `selftests`. The emitter carries `subject` to adopters but never `chunk`, so the
  hold reaches gov and not the adopters. Flipping the subject changes nothing on gov's bar: it still
  runs them only under `GATE_SELFTESTS=1`, which is what "keeps running them" can truthfully mean.
- **gov's manifest mirrors the descriptor, and selfcheck enforces it.** The subject parity arm reds a
  descriptor and manifest that disagree, and `tools/govkit/subject-pins.tsv` pins every subject, so
  all three files move together.
- **The emitter writes no `ceiling`.** gov's manifest already declares 1780 s on the pre-push
  self-test, but an adopter row carries `name`, `argv`, `subject`, `guard` and `doc_reads` only. The
  runner's key set has admitted `ceiling` since run-gates 1.2, so the emitter can carry it above
  that floor, as it carries `doc_reads` above 1.25.
- **The filename predicate alone has three near-misses**: `kit/dogfood doc parity`, `marker
  contracts` and `review-protocol parity (kit vs dogfood)` run a `*.test.sh` and are repo-subject
  checks that gov's manifest files under the `declarations` chunk, where gov runs them on every bar.
  The check must not red them.
