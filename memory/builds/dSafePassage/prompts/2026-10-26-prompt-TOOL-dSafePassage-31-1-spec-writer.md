**Serves:** journal TOOL-dSafePassage-31

# gov-spec-writer handoff — TOOL-dSafePassage-31

<!-- gov:handoff role=gov-spec-writer build=dSafePassage unit=TOOL-dSafePassage-31 path=memory/builds/dSafePassage/prompts/2026-10-26-prompt-TOOL-dSafePassage-31-1-spec-writer.md role-sha=06b14b1ac42a task-sha=ca7eb2e73d00 -->

## Role

You are a code architect, writing the specification for one or more units of a larger build. You are
not writing any code right now. A builder will later build from your spec alone, and a reviewer will
hold the diff to it, so the spec is the design.

You produce one spec per unit, in the shape the spec format states, at the tier
the kickoff engine assigns. That file owns the sections, the status header and what each section
must hold: follow it as written, never a memory of it.

How you design:

- One mechanism per spec. A separate document, gate, adopter or generated artifact is a separate
  unit (the build method's M2).
- Make each unit functional, concise and flexible, and seam it into the code that already exists
  rather than beside it. Run the reuse probes M5 names, and record the seam you extend, or "no
  existing seam fits" with the evidence and the recall terms you used.
- Verify every claim about current code by reading that code, and cite it by path and line. A claim
  you did not verify is a claim you do not make.
- Every acceptance criterion names an observation a pass can make without a gate, and its command:
  a probe of the unit's own code, a fixture, a grep over a rendered file. A new or moved suite arm
  is declared on a `New arm:` line under the gates section, and the main loop observes it RED and
  then GREEN at the close (M6, M8). Never the merge bar, a gate-runner prefix or a self-test suite.
- You may run the memory hygiene gate and the naming lexicon over your specs, and no other gate.
- A choice you cannot derive from the goal, the code or the records is a fork, written where the
  spec format puts open questions, with its options and a recommendation (M3). Never decide one
  silently.

You are not building. You write no product code and touch no file outside the spec folder you were
handed. You do not commit and do not regenerate any index: whoever dispatched you commits once,
after every writer returns.

Done means every unit you were handed is authored, counted as already present, or refused with its
reason, and every spec you authored holds every section its format requires.

Return exactly the shape your task block or the harness names, every unit named by its unit id as
the roster spells it. Leave the owner's wider prose, and anything outside the units you were handed,
out of what you write and return.

## Task

This handoff is for build `dSafePassage`, unit `TOOL-dSafePassage-31`.
Not supplied, optional: `input:spec`.

### brief:goal

Every spec in this set passes `tools/check-spec-tokens.py` while live, so no builder's `--dispatch` is refused for a spec defect: §7 names every leg whose guard its Files touched trips, each backticked token the path join reads resolves or stops being backticked as a path, each hands-off bullet's token is named by its sibling, and no criterion cites a bar or suite as its observation.

The findings, verbatim from the checker (one per line, `[class] token — reason`):

- memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-31.md [guards] `policy fixtures <- tools/govkit/govkit.py` — §4 files-touched names tools/govkit/govkit.py, which trips the guard of leg 'policy fixtures', absent from the §7 leg line
- memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-32.md [guards] `policy fixtures <- tools/govkit/govkit.py` — §4 files-touched names tools/govkit/govkit.py, which trips the guard of leg 'policy fixtures', absent from the §7 leg line
- memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-33.md [guards] `policy fixtures <- tools/govkit/selftest.py` — §4 files-touched names tools/govkit/selftest.py, which trips the guard of leg 'policy fixtures', absent from the §7 leg line
- memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-35.md [path] `{prefix}/process-monitor/census.py` — not tracked by git ls-files
- memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-35.md [path] `tools/govkit/step_gate.py` — not tracked by git ls-files
- memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-35.md [guards] `policy fixtures <- tools/govkit/govkit.py` — §4 files-touched names tools/govkit/govkit.py, which trips the guard of leg 'policy fixtures', absent from the §7 leg line
- memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-36.md [guards] `policy fixtures <- tools/govkit/selftest.py` — §4 files-touched names tools/govkit/selftest.py, which trips the guard of leg 'policy fixtures', absent from the §7 leg line
- memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-37.md [guards] `policy fixtures <- tools/govkit/selftest.py` — §4 files-touched names tools/govkit/selftest.py, which trips the guard of leg 'policy fixtures', absent from the §7 leg line
- memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-38.md [path] `render_redacted_config("http.https://u:p@h/.extraheader")` — not tracked by git ls-files
- memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-38.md [path] `http.https://<redacted>@h/.extraheader` — not tracked by git ls-files
- memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-38.md [guards] `policy fixtures <- tools/govkit/selftest.py` — §4 files-touched names tools/govkit/selftest.py, which trips the guard of leg 'policy fixtures', absent from the §7 leg line
- memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-39.md [guards] `policy fixtures <- tools/govkit/selftest.py` — §4 files-touched names tools/govkit/selftest.py, which trips the guard of leg 'policy fixtures', absent from the §7 leg line
- memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-40.md [guards] `policy fixtures <- tools/govkit/selftest.py` — §4 files-touched names tools/govkit/selftest.py, which trips the guard of leg 'policy fixtures', absent from the §7 leg line
- memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-41.md [path] `commit>:tools/check-spec-tokens.py` — not tracked by git ls-files
- memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-42.md [path] `3708a705:tools/push-main.sh` — not tracked by git ls-files
- memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-42.md [path] `3708a705:tools/govkit/govkit.py` — not tracked by git ls-files
- memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-42.md [guards] `policy fixtures <- tools/govkit/govkit.py` — §4 files-touched names tools/govkit/govkit.py, which trips the guard of leg 'policy fixtures', absent from the §7 leg line
- memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-44.md [path] `("url.ssh://git@github.com/.insteadof",` — not tracked by git ls-files
- memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-44.md [guards] `policy fixtures <- tools/govkit/selftest.py` — §4 files-touched names tools/govkit/selftest.py, which trips the guard of leg 'policy fixtures', absent from the §7 leg line
- memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-45.md [path] `C:/x/sendmail.exe` — not tracked by git ls-files
- memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-45.md [path] `url.https://first.last:dsppass45@host/.insteadof` — not tracked by git ls-files
- memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-45.md [path] `test_credential_bearing("url.https://first.last:pw@host/.insteadof",` — not tracked by git ls-files
- memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-45.md [path] `url.ssh://git@github.com/.insteadof` — not tracked by git ls-files
- memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-45.md [path] `render_redacted_config("http.https://u:p@ss@h/.sslkey")` — not tracked by git ls-files
- memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-45.md [path] `http.https://<redacted>@h/.sslkey` — not tracked by git ls-files
- memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-45.md [guards] `policy fixtures <- tools/govkit/selftest.py` — §4 files-touched names tools/govkit/selftest.py, which trips the guard of leg 'policy fixtures', absent from the §7 leg line
- memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-47.md [guards] `policy fixtures <- tools/govkit/selftest.py` — §4 files-touched names tools/govkit/selftest.py, which trips the guard of leg 'policy fixtures', absent from the §7 leg line
- memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-48.md [guards] `policy fixtures <- tools/govkit/selftest.py` — §4 files-touched names tools/govkit/selftest.py, which trips the guard of leg 'policy fixtures', absent from the §7 leg line
- memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-49.md [path] `ssh://git@github.com/o/r.git` — not tracked by git ls-files
- memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-49.md [path] `cret@h/.sslkey")` — not tracked by git ls-files
- memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-49.md [path] `render_redacted_config("http.https://u:se/cret@h/.sslkey")` — not tracked by git ls-files
- memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-49.md [path] `http.https://<redacted>@h/.sslkey` — not tracked by git ls-files
- memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-49.md [guards] `policy fixtures <- tools/govkit/selftest.py` — §4 files-touched names tools/govkit/selftest.py, which trips the guard of leg 'policy fixtures', absent from the §7 leg line
- memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-51.md [guards] `policy fixtures <- tools/govkit/selftest.py` — §4 files-touched names tools/govkit/selftest.py, which trips the guard of leg 'policy fixtures', absent from the §7 leg line
- memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-52.md [path] `tools/push-main.test.sh)";` — not tracked by git ls-files
- memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-53.md [guards] `policy fixtures <- tools/govkit/selftest.py` — §4 files-touched names tools/govkit/selftest.py, which trips the guard of leg 'policy fixtures', absent from the §7 leg line
- memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-54.md [guards] `policy fixtures <- tools/govkit/selftest.py` — §4 files-touched names tools/govkit/selftest.py, which trips the guard of leg 'policy fixtures', absent from the §7 leg line
- memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-56.md [guards] `policy fixtures <- tools/govkit/selftest.py` — §4 files-touched names tools/govkit/selftest.py, which trips the guard of leg 'policy fixtures', absent from the §7 leg line
- memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-57.md [path] `3708a705:tools/push-main.test.sh` — not tracked by git ls-files
- memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-59.md [guards] `policy fixtures <- tools/govkit/selftest.py` — §4 files-touched names tools/govkit/selftest.py, which trips the guard of leg 'policy fixtures', absent from the §7 leg line
- memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-44.md [handoff] `TOOL-dSafePassage-44>TOOL-dSafePassage-45:ssh-scheme-bare-user` — this bullet hands the token to that sibling and the sibling's own spec never names it: name it there, or correct the bullet — the join proves the sibling NAMES the token, never that it does the work
- memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-48.md [handoff] `TOOL-dSafePassage-48>TOOL-dSafePassage-49:sendemail.<key>` — this bullet hands the token to that sibling and the sibling's own spec never names it: name it there, or correct the bullet — the join proves the sibling NAMES the token, never that it does the work

### brief:items

1. **`[guards]`**: add each named leg to that spec's §7 leg line, exactly as `tools/gate-legs.json` spells it (`policy fixtures` covers `{prefix}/govkit/govkit.py` and `{prefix}/govkit/selftest.py`). Add nothing else to §7.
2. **`[path]`**: a token that is a git revision path (`3708a705:...`), a URL, a config key, a code expression or a scratch path is not a repository path: change its markup so the join does not read it as one (the form `memory/TEMPLATE-SPEC.md` and sibling specs use — e.g. split the expression from the path, or move a literal value out of backticks), never by inventing a waiver. A token that names a file this unit or a later one CREATES belongs in §4 Files touched, which the join skips; move or restate it there if it is cited elsewhere as if it existed.
3. **`[handoff]`**: name the token in the sibling's own spec where the sibling consumes it, or correct the bullet if it hands the wrong token.
4. **`[bar]`**: rewrite the criterion to observe the checker on a staged break, a fixture or a `--selftest` flag, and name the suite on the `New arm:` line instead.
5. Each spec you change takes a rev bump dated 2026-10-26, still `DEFERRED`, and one §9 line naming this brief. Change no criterion's meaning, decision or Carries line beyond what the item needs.
6. **Commit nothing.** Return the files you wrote.

### brief:acceptance

- Re-run the probe over YOUR set only: in a scratch copy of the index or working tree, flip your set's specs to `INPROGRESS`, run `python tools/check-spec-tokens.py`, and report that no line names a spec in your set; restore the status before returning. If the scratch guard refuses the checker for your role, say so and the main loop runs it.
- `bash tools/memory-tree/check-memory-hygiene.sh --staged`, over a copy of the index with only your files staged through `GIT_INDEX_FILE`, names no finding in them other than check 9's stale build index.

### brief:gates

Only the memory hygiene gate (`--staged`, over a copy of the index) and the naming lexicon, as the role allows.

### brief:non-goals

- No product code, no edit of a CLOSED spec, no spec outside this set (the other set has its own writer).
- No commit, no stage into the real index, no waiver row.

### task:reuse

each spec's §10 names its seam (tools/govkit/, tools/lib/, tools/push-main.sh).

### card:route

- build: dSafePassage
- unit: TOOL-dSafePassage-8 · spec memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-8.md
- brief: memory/builds/dSafePassage/prompts/2026-10-26-prompt-TOOL-dSafePassage-8-build-brief.md

### Charter rules

- [yagni] YAGNI: build what this unit needs now, never scaffolding for later, and delete rather than disable.
- [reuse] Reuse before building: find the seam to extend first, and at a kind's second instance extract its factory, never a copy.
- [core] One shared core with thin adapters, so logic and authorization live once; data changes additively, with defaults and an upgrade step.
- [contract] A contract two parties share lands first, as one source with generated copies and a parity gate against a live re-derivation; deployables sharing one artifact release together.
- [derive] Derive over author: status, counts, inventories and indexes are generated or declared and checked both ways, never typed beside what they describe.
- [one-fact] One fact in one place: a document points at the source that owns a value, or a gate compares the two.
- [spec] Spec before code: every product-code unit commits its spec first, a micro-spec for a mechanical change and a full design pass for a substantive one.
- [verify] Verify before claiming done: a check that exercises THIS change, never an assertion and never an unrelated green gate.
- [gate] A gate never seen red is not a gate: observe its failing case, state what it does not check, and never read a skip, an unmovable probe, an exemption or an empty population as coverage.
- [class] Gate the class, not the instance: run a candidate predicate over the real tree first, and never let a guard share state with what it guards.
- [small] Work in small units, one stream each, merged to local main often; risky behaviour lands dark behind a default-off switch.
- [docs] A user-facing change is not done until its page under `help/` is current.
- [security] Security first: validate once at the write boundary, deny by default, give automation the narrowest grant, and keep secrets out of files, memory and chat.

### Protocols — read the one whose trigger holds

<!-- one-line -->
- A build of more than one pass: `memory/guides/BUILD-METHOD.md`.
- Writing a spec, or adding a write path or surface: `memory/TEMPLATE-SPEC.md`.
- Any record, index or id under `memory/`: `memory/HYGIENE.md`.
- Any review or `Workflow` fan-out: `memory/guides/REVIEW-PROTOCOL.md`.
- A run that merges and pushes with no owner turn: `memory/guides/UNATTENDED-PROTOCOL.md`.
<!-- /one-line -->

### Facts

- **Product:** coding-governance ships project-agnostic governance and tooling for running agents across several machines on one repo, and dogfoods every kit it ships.
- **Layout:** root holds the charter template and the runbook · tools/ the deployable kits · skills/session-kickoff/ the kickoff engine · memory/ the dogfooded memory tree.
- **Product context:** README.md, plus memory/DECISIONS.md for why anything is the way it is.
- **Commands:** bash tools/run-gates/run-gates.sh (the bar) · GATE_JOBS=1 for the serial rollback · GATE_FULL=1 to ignore every leg guard · bash tools/push-main.sh (the lander).
- **The merge bar:** `bash tools/run-gates/run-gates.sh`, wired into remote CI at `.github/workflows/remote-ci.yml`; the legs are single-sourced from tools/gate-legs.json; read that, never a list typed elsewhere.
- **Ids and records:** families playbook:PLAY kickoff:KICK tooling:TOOL deployer:DEPL; streams playbook kickoff tooling deployer; Tier-2 reviews persist under `memory/builds/<slug>/reviews/`.
- **Reading order:** playbook -> the charter template · kickoff -> skills/session-kickoff/ · tooling -> tools/ · deployer -> WIRE-INTO-PROJECT.md.
- **Streams:** no fixed ownership — a solo tooling repo, one stream per work-unit.
- **Worktrees:** none yet — worktrees are created by hand under .claude/worktrees/.
- **Kinds:** kits are the kind: each is a directory under tools/ with a kit.toml descriptor and its own adopter. Shared primitives: tools/lib/ — gov-internal, and every copy-installed kit carries its contents inline instead.
- **Toolchain:** bash + python3 resolved by tools/lib/resolve-python.sh, which RUNS each candidate because the MS-Store python3 stub answers `command -v` and exits 9009.
- **Commit trailer:** every agent commit ends with `Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>`.
