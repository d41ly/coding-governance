# Wave 3 — lens: SECURITY

**Serves:** research TOOL-aScouredKit-2

## Verdict: CLEAN WITH FIXES

Scope: the whole product at HEAD (`66c4891c`), graded against the charter's §9 and against the
trust boundary the product itself declares — `tools/govkit/govkit.py` reading a target-authored
`.governance/deploy.toml` and `.governance/install.json`, then running commands built from them.
Node `a`, Windows 11, git 2.54.0.windows.1, python 3.14.

Everything below that says REPRODUCED was run. Fixtures live under the session scratchpad
(`.../scratchpad/sym2`, `.../scratchpad/rce`); each command is quoted so the arm can be rebuilt.

---

## Findings

### F1 — HIGH · `apply` writes outside the target through a directory link, and exits 0

`tools/govkit/govkit.py:649` — `demand_contained_dest` is, by its own docstring, "PURE STRING
CONTAINMENT, no target root needed and none taken". It normalises the destination and rejects `..`,
a POSIX absolute and a drive letter. It never touches the filesystem, so it cannot see that a
component of the path is a link out of the tree. The write site it protects is
`tools/govkit/govkit.py:4103-4104` (`dp.parent.mkdir(parents=True); dp.write_bytes(data)`), and
Python follows links on both.

REPRODUCED, twice, on two fresh fixtures:

```
# target with tools/ as a directory junction to a sibling dir outside the repo
New-Item -ItemType Junction -Path $S\sym2\tgt\tools -Target $S\sym2\outside
python tools/govkit/govkit.py apply --target $S/sym2/tgt --kits memory-tree
  -> apply rc=0
  -> files outside the target: 26
python tools/govkit/govkit.py check --target $S/sym2/tgt
  -> govkit: integrity: 26/26 engine row(s) verified · provenance: 26/26 resolved
```

`plan` previewed 26 rows spelled `tools/memory-tree/…`, `apply` reported `landed 26 file(s)`, the
receipt records 30 rows, and every byte landed in `$S/sym2/outside/memory-tree/`. `check` then
verified all 26 through the same link and reported a clean install. Nothing in the run named the
escape.

The count is the same 26 that round 3's `prefix = "../../x"` reproduction produced. Same class, one
mechanism over.

**The check that catches it already exists in this engine, in a different verb.** `cmd_update`
(`tools/govkit/govkit.py:5671-5677`) resolves the receipt path and calls `relative_to(target)`, with
a comment calling this "the one boundary this whole tool is built around". Run against the identical
escaped tree:

```
python tools/govkit/govkit.py update --target $S/sym2/tgt --write
  -> govkit: receipt row 'tools/memory-tree/.memory-tree.conf.example' resolves outside the
     target repository — refusing it: a path that escapes the tree the operator named is not a
     path this verb may write, whatever the verdict says
     (…one such line per row, all 26 refused, nothing written)
```

Two verbs, one question, opposite answers — and the permissive one is the one that writes first.
That is verbatim the framing `demand_contained_dest`'s own docstring uses about round 3 ("THE
CONTAINMENT CHECK ALREADY EXISTED, IN THE WRONG VERB"), which makes this the same finding recurring
through the fix written to end it.

Reachability: a junction needs no elevation on Windows and is transparent to Python and to git (git
staged all 26 as `tools/memory-tree/…`). On POSIX a committed symlink `tools -> /etc` reaches the
same write; `git add` would then refuse, but only AFTER `write_bytes` has landed the file. The
layout is not exotic — a repo with `tools` linked at a shared tree is an ordinary monorepo shape,
so this fires on an honest adopter as well as a hostile one.

Fix: at the write site, and at `demand_contained_dest`'s callers that hold a target root, do what
`cmd_update` already does — `(target / dest).resolve().relative_to(target.resolve())`. Keep the
string check (it reaches `plan`, which has no root-relative write to resolve); add the resolving one
where the bytes land.

---

### F2 — HIGH · the read-only `check` verb executes a script from the target's working tree, after its own integrity loop has reported that script does not match the receipt

`tools/govkit/govkit.py:2764` — `cmd_check` runs `run_kit_check(eid, d, ctx, target, r)` for every
claimed kit. `[check].argv` for six shipped entries is `["bash", "{kit}/adopt-<kit>.sh", "--check"]`,
where `{kit}` resolves INSIDE the target. The file it runs is a file in the target's working tree,
which the target owns and can rewrite.

The integrity loop (`tools/govkit/govkit.py:2610-2660`) hashes every `engine` row against the
receipt and appends a finding on mismatch. It does not stop, skip or gate the spawn below it. So
`check` measures that a file is not what gov shipped and then executes it in the same run.

REPRODUCED:

```
# install agent-instructions into a fresh target, commit, then overwrite the adopter with a payload
printf '#!/usr/bin/env bash\nprintf CODE-EXEC > "$S/rce/PWNED-BY-CHECK.txt"\nexit 0\n' \
  > tools/agent-instructions/adopt-agent-instructions.sh

python tools/govkit/govkit.py check --target $S/rce/tgt
  govkit check — agent-instructions: adopted
  govkit: integrity: 3/4 engine row(s) verified · provenance: 4/4 resolved
  govkit: 'tools/agent-instructions/adopt-agent-instructions.sh' does not match the receipt:
          expected 58f49c5534b3, found 4a4a9e31e20a
  govkit: 1 problem(s)

cat $S/rce/PWNED-BY-CHECK.txt   ->  CODE-EXEC
```

The payload wrote OUTSIDE the target. `check` printed `agent-instructions: adopted` — a green
per-kit verdict derived from the tampered script's own exit code — beside the tamper report.

A control run separates the verbs cleanly:

```
rm PWNED-BY-CHECK.txt
python tools/govkit/govkit.py plan  --target $S/rce/tgt --kits agent-instructions   -> clean
python tools/govkit/govkit.py check --target $S/rce/tgt                             -> PWNED
```

`tools/govkit/govkit.py:6850` (USAGE) states: "`plan`, `check`, `update` and `adopt` are READ-ONLY
and none writes a byte". `plan` holds that. `check` does not, and the bytes it writes are chosen by
the repository under inspection.

What IS disclosed: the `SHELL_EXEC_SITES` header concedes that `cmd_check` "is reachable from the
read-only `check` verb with no opt-in at all, by design, because running `[check].argv` is what
`check` DOES". What is NOT disclosed anywhere is that the code executed is a worktree file the
target can replace, that the receipt hash proving it was replaced is computed in the same run and
ignored, and that the operator-facing usage text calls the verb read-only regardless.

Fix, in ascending cost: (1) skip `run_kit_check` for a kit whose engine rows failed integrity, and
say so — an unmeasured kit is a state, an executed tampered one is not; (2) correct the USAGE
sentence, because a verb that spawns target-chosen code is not "read-only"; (3) put `[check].argv`
behind the same opt-in `[[decline]].discharge` already has, which would make `check` answer the
receipt question with no spawn at all by default.

---

### F3 — MEDIUM · the declared executing surface misclassifies its own read-only spawn, and its header claims a guarantee two of its rows falsify

`tools/govkit/govkit.py:2146` — `SHELL_EXEC_SITES` defines three labels. `target-code` means "the
argv is entirely gov's and what it RUNS is the target's", and the table states its bound directly:
**"What bounds `target-code` is being reachable from a writing verb only."**

`run_kit_check` is labelled `target`. By the table's own definition it is `target-code`: gov writes
`["bash", "{kit}/adopt-…", "--check"]` and the script is the target's (F2 executed it). And it is
reachable from `check`, a non-writing verb. So the one row carrying a stated bound is the row whose
bound is broken, and the label that would have surfaced it is the one not applied.

This survives because the census only DERIVES the `target` label ("a site is TARGET-controlled when
its function reaches `target_context` or `resolve_tokens`, and the arm DERIVES that"). There is no
derivation for `target-code` — it is one hand-typed row, `hook_probe`, and the selftest asserts
membership rather than the property. A hand-maintained label disagreeing with the code exactly when
it matters is the failure this table's own header names.

Second half, same block: the header asserts "every target-supplied value entering one of these argvs
passes `demand_safe_token` at the boundary, which is armed, reproduced-against, and does not depend
on six call sites each remembering to be careful." Two rows in the table are argvs the target writes
END TO END, neither of which passes `demand_safe_token` at all:

- `read_gate_verdicts` (`tools/govkit/govkit.py:3101`) spawns `[gate_runner].command` verbatim.
  `validate_gate_runner` refuses only a string-instead-of-array. `_cmd_apply:3906` prints it first
  and the docstring there is honest ("It EXECUTES target-authored code … anyone with commit access
  there chooses what runs on the operator's machine"), so the SITE is disclosed; the TABLE's blanket
  sentence is not true of it.
- `decline_findings` (`tools/govkit/govkit.py:2386`) spawns `[[decline]].discharge.command`
  verbatim. Gated behind `--run-discharge`, printed before spawning, refuses a non-array — the
  best-behaved spawn in the file, and still not a `demand_safe_token` consumer.

Fix: type `run_kit_check` as `target-code`, delete or re-scope the "reachable from a writing verb
only" clause (it is now false), and rewrite the guarantee sentence to name the three regimes it
actually has — graded interpolation, whole-argv target authorship behind an opt-in, and whole-argv
target authorship announced but not gated.

---

### F4 — MEDIUM · "redacted" gate evidence masks exactly one credential shape

`tools/run-gates/run-gates.sh:110`:

```sh
redact() { sed -E 's#://[^/@[:space:]]+:[^/@[:space:]]+@#://***:***@#g'; }
```

That is the whole redactor. It is applied to `<git-dir>/gate-logs/<leg>.log` (line 1119) and to
`<git-dir>/gate-run/<id>/<i>.out` (line 1134). Measured against six lines:

| input | after `redact` |
|---|---|
| `https://user:s3cr3t@github.com/x.git` | masked |
| `GITHUB_TOKEN=ghp_AAAA…` | **unchanged** |
| `Authorization: Bearer eyJhbGciOi.PAYLOAD.SIG` | **unchanged** |
| `AWS_SECRET_ACCESS_KEY=wJalrXUtnFEMI/…` | **unchanged** |
| `export ANTHROPIC_API_KEY=sk-ant-api03-XXXX` | **unchanged** |
| `curl -H "x-api-key: sk-live-123" …` | **unchanged** |

Three prose sites say "redacted" with no scope: `AGENTS.md:532`, `tools/run-gates/README.md:112`,
`memory/map/features/run-gates.md:38`. The function's own comment does name its scope ("mask URL
userinfo"), so the code is honest and the documents are not — the charter's §7 rule that "a gate's
OWN header states what it does NOT check" applied one layer out.

The evidence arm (`tools/run-gates/run-gates.evidence.test.sh:139-146`) asserts the one shape the
implementation handles, so it can never discover the gap. The arm is a positive control for a
predicate, not coverage of a class.

Blast radius is real but bounded: both files are `chmod 600` and live under `<git-dir>`, so this is
a durable plaintext credential on the operator's own disk rather than a leak to a remote. Terminal
output is unredacted by deliberate design (stated: ephemeral).

Fix, cheapest first: qualify the three prose claims to "URL userinfo masked" — that alone closes the
false-confidence half. If broader masking is wanted, add `(?i)(token|secret|key|password|passwd|
authorization|bearer)\s*[=:]\s*\S+` to the same sed and add one arm per shape; the arm is what makes
the claim true, not the regex.

---

### F5 — LOW · unvalidated receipt fields reach `git show` as option-position argv

`tools/govkit/govkit.py:3341`:

```python
out = subprocess.run(["git", "-C", str(root), "show", f"{commit}:{path}"], …)
```

Both `commit` and `path` come from the TARGET's `.governance/install.json`
(`cmd_check:2650`, `row.get("commit")` / `row.get("source")`). `install.json` is a second
target-authored input and, unlike `deploy.toml`, nothing grades it — no `demand_safe_token`, no
shape check, and no `--` separating revisions from options.

`git show` accepts diff options, `--output=<file>` among them. Confirmed on this engine:

```
git show "--output=$PWD/PWNED.txt" HEAD   ->  rc=0, PWNED.txt created
```

So a receipt row can steer `git show` into option position in GOV's own checkout. Impact is small
and I am grading it that way rather than dressing it up: the argument is always
`<attacker-string>:<attacker-string>`, so the written filename always carries a `:` — invalid on
Windows (the write simply fails), legal but useless on POSIX. I found no option reachable this way
that executes (`--ext-diff` / `--textconv` need a driver configured in gov's own repo, which the
target cannot write).

Reported because the CLASS is the interesting part: `deploy.toml` is graded at a documented boundary
and `install.json` is not graded at all, while it feeds `target / row["path"]` reads, git argv, and
— in `update` — writes. Fix: `--` before the revspec is impossible for `show`, so grade the fields:
`commit` against `^[0-9a-fA-F]{7,64}$`, `source` against the same path class `demand_safe_token`
already owns.

---

### F6 — LOW · the adopter spawn drops `resolve_tokens`' missing list, the defect its sibling documents at length

`tools/govkit/govkit.py:4198`:

```python
resolved = [resolve_tokens(a, ctx)[0] for a in argv]
rc = subprocess.run(resolve_shell_argv(resolved), cwd=str(target), …).returncode
```

`exempt_leg` (`tools/govkit/govkit.py:3149-3155`) carries a paragraph on exactly this: "`resolve_tokens(a, ctx)[0]`
dropped it, so a command holding an unresolved token was EXECUTED with a literal brace in its argv,
exited non-zero for that reason, and the function returned True". `cmd_check`'s hole-probe loop
(2775-2782) reads the missing list and refuses. The apply-side adopter spawn still discards it and
spawns.

Latent today rather than live: I enumerated every `[adopt].argv` in the thirteen shipped
descriptors and each interpolates only `{kit}` or `{prefix}`, both SEEDED, so no shipped kit can
reach the branch. It fires the day a descriptor adds an answer-supplied token to an adopter argv —
which is precisely the change `needed_answers` was widened for. Fix: three lines, matching the
sibling at 2775.

---

### F7 — LOW · one consumer of `prefix` reads it raw

`tools/govkit/govkit.py:3068-3069`, `check_target_reads_subject`:

```python
prefix = (deploy.get("prefix") or "tools").strip("/")
runner = target / prefix / "run-gates" / "run-gates.sh"
```

Every other consumer routes `prefix` through `demand_safe_token` at `target_context:818`. This one
joins the raw value onto the target root and reads. `prefix = "../../.."` therefore reads a file
outside the named tree. It only extracts `KIT_RUN_GATES_VERSION` and returns a bool, so the impact
is a wrong feature-gate decision and an out-of-tree read, not a write and not a leak. Reported for
the inconsistency: one ungraded reader of a value the file grades everywhere else is how the next
consumer inherits the wrong habit. Fix: one call, same as line 818.

---

## Classes checked and found CLEAN

Reported because absence is evidence, and because the next reviewer should not re-run these.

- **Every token that reaches a SPAWN is gov-seeded.** I enumerated all `argv = ` and
  `discharge.command` in the thirteen `kit.toml` descriptors: the complete token set is
  `{kit}`, `{prefix}`, `{gate_file}`, and `{k}` (the last is `${k}`, excluded by `TOKEN_RX`'s
  lookbehind at govkit.py:495). `{kit}` and `{prefix}` are in `SEEDED_TOKENS`, refused from
  `[answers]` and strict-graded when set per-entry. `{gate_file}` is prose-class and
  target-suppliable, but it appears in exactly one place — `tools/codebase-map/kit.toml:54`, a
  `[[gate_leg]].argv` — which govkit WRITES into the target's own gate manifest and never spawns.
  So the prose class never reaches a govkit spawn. The comment at govkit.py:700 claiming this is
  correct as written.
- **`deploy['kits']` reaches only a membership test.** `resolve_selection`
  (govkit.py:474-483) shape-checks the container and elements, then tests each against `descs` and
  refuses an unknown id. Nothing in that path builds a filesystem or argv value. The recent build's
  spec claim holds.
- **The Windows executable search does not include the child's cwd.** `subprocess.run(["python", …],
  cwd=<hostile dir containing python.bat>)` executed the real python; the plant was not run. So the
  bare `python` / `python3` argv[0] in six descriptors is not a hijack surface even though
  `resolve_shell_argv` only fixes `bash`. (Tested directly; not reasoned from docs.)
- **`plan` spawns nothing.** Controlled against the F2 payload: `plan` left the tree clean, `check`
  did not. `[[decline]].discharge` is the only spawn `plan` can reach and it is `--run-discharge`
  gated, printed before spawning, and refuses a non-array command (govkit.py:2339-2386).
- **The rollback and update write loops are contained.** `govkit.py:6071` calls
  `demand_contained_dest` per path before `unlink`/`checkout-index`; `govkit.py:5671` resolves and
  contains. Both catch the F1 link; only `apply` does not.
- **`agent-cap.js` fail-opens are all declared.** `guardAgentSpawn` returns null (allow) on a
  missing `session_id`/`prompt_id`/`tool_use_id`, on an unresolvable git common dir, and on a failed
  `mkdirSync` — the first two are stated in the header and at agent-cap.js:895-901; the third is
  the same "directory cannot be resolved" clause and is the one I would tighten if any. A token that
  cannot be CREATED denies (agent-cap.js:938). `AGENT_CAP` is refused, not ignored. An unreadable
  `scriptPath` denies. `--only=join` would disable rules 1-3, and `tools/check-wiring.sh:149`
  refuses a wired command carrying `--only` — verified present, not assumed.
- **`scratch-guard.js` is not a security control and says so** (header, lines 33-35: "FAILS OPEN …
  a security control would have to fail the other way"). Graded as declared; no finding.
- **The unattended anchor.** `memory/guides/UNATTENDED-PROTOCOL.md:562-600` discloses the reduction
  ("Nothing a script running under the run's own uid constitutes authorization") and then names the
  specific levers: editing the kit, shimming the tools it calls, `--no-verify`, an empty
  `core.hooksPath`, overriding the gate command, a seeded relay endpoint, never creating a
  run-state file, object-substitution refs and grafts. I looked for one outside that set and did
  not find one. Every candidate I formed — `GOV_BASH`, `PATH` ordering, a planted `bash` — is an
  instance of "shims the ordinary tools this kit calls", which is disclosed. No finding.
- **Secrets in receipts and review records.** `.governance/install.json` and `install.sums` carry
  paths, roles, hashes and commit ids only. `FAILED_LEGS` (run-gates.sh:1197-1200) carries a leg
  name, an exit code and a POINTER at the log — never the bytes — so `gate-last-summary.txt` and
  `gate-last-failure.txt` cannot carry a credential from leg output. (`gate-last-summary.txt` is
  the one evidence file written without `chmod 600`, at run-gates.sh:1467; it holds no leg output,
  so I did not raise it.)

## What I did not reach

- The POSIX half of F1. I demonstrated the escape with a Windows junction, which is the platform
  this repo's primary node runs on. The POSIX symlink case is the same `write_bytes` through the
  same unresolved path and I am confident in it, but I did not execute it here.
- `tools/settings-merge.py` and `tools/check-wiring.sh` as write surfaces. Both are operator-run
  against the operator's own tree and take no target-authored input; I read them for a hook-command
  injection and found none, but I did not fuzz them.
- The `[[gate_leg]]` emission path into a foreign `gate-legs.json`. `{gate_file}` lands there
  prose-class, which means an adopter can write a spaced value into their own gate manifest. That is
  a target acting on itself, not a boundary crossing, so I stopped.
