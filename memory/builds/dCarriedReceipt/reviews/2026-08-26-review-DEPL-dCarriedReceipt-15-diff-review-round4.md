**Serves:** diff-review DEPL-dCarriedReceipt-1 DEPL-dCarriedReceipt-2 DEPL-dCarriedReceipt-3 DEPL-dCarriedReceipt-4 DEPL-dCarriedReceipt-5 DEPL-dCarriedReceipt-6 DEPL-dCarriedReceipt-7 DEPL-dCarriedReceipt-8 DEPL-dCarriedReceipt-9 DEPL-dCarriedReceipt-10 DEPL-dCarriedReceipt-11 DEPL-dCarriedReceipt-12 DEPL-dCarriedReceipt-13 DEPL-dCarriedReceipt-14 DEPL-dCarriedReceipt-15

# Closing diff review, ROUND 4 — the fan ran, and it found the fold's own hole

Node `a` · 2026-08-26 · adversarial fan (lenses → skeptics → synthesis) · this record is the synthesis pass.
Subject: govkit, the mechanical kit deployer at `tools/govkit/govkit.py`, plus the three kits and two
harnesses the build touched. Line numbers in this record are against the head of the range below,
which is the tip of `main`; the `dCarriedReceipt` worktree sits one commit behind it.

Reviewed range: `267b598f0214a2a751aa0e3927c64f3521a2ce98...a9c6d386ac4a73568ddfea83e9182c97e8d35a33` — 27 commits, the fifteen-unit build plus rounds 1–3 and their folds.

## Verdict: BLOCKED

One blocker, and it is the same defect round 2 and round 3 each thought they had closed. A target
repository's own `.governance/deploy.toml` can overwrite the three engine-derived path tokens with
values graded by the PROSE character class, and the read-only `check` verb then executes code from
that repository. I reproduced both halves independently before writing this record.

The blocker count moved 3 → 1 from round 3, which is strictly smaller, so the loop's re-arm condition
in `memory/guides/BUILD-METHOD.md` is met: fold this round, then round 5 measures the fold. Nothing
here is a candidate for promotion-at-exit yet.

The consolation is real and worth stating plainly: rounds 2 and 3 found this class by reasoning about
one entry point at a time, and each fix bounded the entry point in front of it. Round 4 found it by
enumerating the entry points. Every remaining finding below is a variation on that one habit.

## Review shape

raw 20 · confirmed 20 · refuted 0 · unverified 0 · precision 1.00

Twenty confirmed findings collapse to **fourteen distinct defects** — ids 1/4/12/16 are one blocker
found by four lenses, ids 3/11 are one defect, ids 9/14 are one, ids 15/20 are one. The severities
below are the ones adjudicated in this synthesis and they do not all match the lens labels; where
they differ the row says so. Precision 1.00 over twenty findings is not a boast, it is a signal that
the lens priming was narrow — a fan that refutes nothing was probably not asked anything hard.

## Findings

| # | Sev | Where | Defect | Raw ids |
|---|-----|-------|--------|---------|
| B1 | **blocker** | `tools/govkit/govkit.py:703` | `[answers]` / `[kit.<eid>]` overwrite the strict-graded `prefix` / `kit` / `kit_id` with prose-graded values — reproduced as code execution from read-only `check` | 1, 4, 12, 16 |
| H1 | high | `tools/govkit/selftest.py:6060` | the injection arms drive the payload through the top-level `prefix` only, so B1's entry point is asserted by nothing | 2 |
| H2 | high | `tools/govkit/govkit.py:3424` | a `merged` row carries no `oid` and is excluded by no carve-out, so `apply` leaves the target DIRTY and blocks the next writing verb | 3, 11 |
| H3 | high | `tools/govkit/govkit.py:3734` | containment is checked inside the per-entry write loop, so a refusal for entry N lands on a half-installed target with no `install.json` | 5 |
| M1 | medium | `tools/govkit/govkit.py:3424` | the same `pins` exclusion disarms S4 for `apply`, the one verb that actually writes and stages `.gitattributes` | 18 |
| M2 | medium | `tools/govkit/govkit.py:571` | both token classes are `$`-anchored, so a TRAILING newline passes strict and prose alike | 6 |
| M3 | medium | `tools/govkit/govkit.py:4067` | the post-renormalize `oid` re-stamp is gated on `staged`, not on the renormalize having run | 13 |
| M4 | medium | `tools/govkit/selftest.py:6004` | the spawn census allowlists `govkit.git()`, whose subcommand is entirely dynamic, defeating the `git hook run` by-name exclusion | 17 |
| M5 | medium | `tools/govkit/selftest.py:2496` | ruling A's payoff arm asserts only that a substring is absent, never that the verb succeeded | 8 |
| M6 | medium | `tools/unattended/unattended.sh:1575` | `spec_facts` batches every spec into ONE awk, so one absent file is fatal for the whole build | 7 |
| L1 | low | `tools/workflows/drift-audit-code.js:416` | `, severity corrections ${downgrades}` is welded onto the end of an unrelated prose sentence | 9, 14 |
| L2 | low | `tools/check-install-prefix.sh:231` | a genuinely MISSING ratchet falls through its own guard whenever the hit set is zero | 10 |
| L3 | low | `tools/govkit/selftest.py:6120` | the `target`/`gov` label derivation is a flat substring test, and one site is already hand-labelled beyond its reach | 19 |
| L4 | low | `tools/govkit/govkit.py:1745` | `demand_contained_rows` documents two callers, has one, and carries a branch unreachable from it | 15, 20 |

---

## B1 — blocker — a target answer overwrites the tokens the strict class exists to guard

`tools/govkit/govkit.py:703` (the `[answers]` loop) and `:706` (the `[kit.<eid>]` loop), against the
reserved keys seeded at `:698-701`.

`target_context` builds ONE dict. It first sets `prefix`, `kit_id` and `kit` from a `prefix` graded
by `demand_safe_token` with `prose=False` — the strict class, `TOKEN_VALUE_RE` at `:571`, which
admits no space. It then walks the target's `[answers]` table and its `[kit.<eid>]` table and
assigns `ctx[k]` unconditionally with `prose=True` — `ANSWER_VALUE_RE` at `:657`, which admits
SPACE, comma, equals and colon. There is no reserved-key guard anywhere in the function.

**Reproduced, twice, by me, at the range head.** Loading the module and calling the function
directly:

```
target_context(., {"prefix": "tools", "answers": {"kit": "-m pwned "}}, "drift-audit", {})
  -> ctx["kit"] == '-m pwned '
resolve_tokens("python {kit}/drift_report.py --check", ctx)
  -> ('python -m pwned /drift_report.py --check', [])
```

Zero unresolved tokens. That template is not hypothetical: `tools/drift-audit/kit.toml:80` ships
`discharge = { command = ["bash", "-c", "python {kit}/drift_report.py --check"] }`, and five more
shipped descriptors interpolate `{kit}` inside a `-c` string (drift-audit ×3, codebase-map ×1,
memory-tree ×3). `cmd_check`'s hole loop spawns every one of them with `cwd=str(target)` and NO
`--run-discharge` guard — that flag gates `decline_findings` only. So a read-only
`govkit check --target <t>`, with no `--write` and no flag of any kind, runs `python -m pwned` from
the target's own root. Two independent lenses wrote the sentinel file to disk to prove it; the
`tools/pwn.py z` spelling and the `-m pwned ` spelling both land.

Three things make this worse than an ordinary injection:

- **It is B2 reopened by B2's own fix.** Round 2 split the token class in two precisely so that
  document-only values could carry spaces. Nothing was added to stop a target routing a
  document-class value into a shell-class key.
- **The engine already knows the set.** `needed_answers` at `:6342` declares
  `derived = {"prefix", "kit", "kit_id", "relpath", "memory_root"}` and refuses to ask an operator
  for any of them. `target_context` lets a target supply all five. Two functions, one set, opposite
  answers.
- **The comment above `ANSWER_VALUE_RE` states the false half out loud.** It says a prose value
  reaching a `bash -c` template word-splits, that this "is a correctness bug for the operator who
  wrote it" and "it is not code execution". For every `python {kit}/<script>` template that claim is
  wrong: the injected word becomes the script python runs. A comment asserting a guarantee the code
  does not hold is worse than no comment, because the next reader budgets against it.

**Fix.** Hoist `needed_answers`' `derived` set to a module constant and refuse by name in
`target_context`: any `answers.*` or `kit.<eid>.*` key naming one raises a `Refusal` that says which
key and why. Silently dropping the key also closes the hole but hides an operator's mistake, and this
engine's whole posture is to name what it refuses. Then correct the `ANSWER_VALUE_RE` comment: the
prose class is sound only for a value whose sole consumer is a rendered document, and nothing today
establishes that per key.

**Left-shift gate.** Two legs, because the class has now escaped three times through three different
doors:

1. A selftest arm that builds a hostile target, runs the READ-ONLY `check`, and asserts on a
   SENTINEL FILE rather than on an exit code — an exit code cannot distinguish "refused" from
   "executed and then reported normally", which is exactly what happened here (the poisoned run
   printed an ordinary `landed-but-inert` report and exited 1).
2. A structural arm over the descriptors themselves: no shipped `kit.toml` may interpolate a
   prose-gradeable token inside a `bash -c` / `python -c` STRING argument. That gates the class
   rather than the instance — it reds when someone adds a seventh such template, which is the door
   nobody is watching.

---

## H1 — high — the injection arms only ever vary the top-level `prefix`

`tools/govkit/selftest.py:6060`, and the `_metas` property loop at `:2756`.

Raised from the lens's `medium`. This is not a coverage gap in the abstract: it is the specific
reason a live, read-only, arbitrary-code-execution path shipped inside the fold written to close
that exact class, and the suite was green over it for two commits.

`a_evil_target(tag, prefix_value, kit)` varies exactly one thing — the top-level `prefix` — and
hard-codes `[answers]\nmemory_root = "memory"` as a literal fixture. All four call sites drive their
payload through `prefix`. A target supplies token values through THREE doors; the arms test one.

The `[-12] TOKEN` property arm at `:2756` cannot compensate. Its `_metas` list holds

```
; | & $ backtick ' " < > ( ) { } * ? ! backslash \n \r \t
```

and no space. The space is the ONE metacharacter the prose class deliberately admits and the one that
carries B1. The row table three lines above it affirms that admission in writing. So the property
arm asserts the class is safe for every character except the one it is unsafe for.

**Fix.** Parameterise `a_evil_target` over WHERE the hostile value is written — top-level `prefix`,
`[answers].<key>`, `[kit.<eid>].<key>` — and run the existing payloads through all three, asserting
on the sentinel in each. Add the space to `_metas` and assert the pair explicitly: the prose class
admits it, and no `bash -c` template in any shipped descriptor may interpolate a prose-graded token.

**Left-shift gate.** The parameterisation IS the gate, but give it the property shape rather than
three copies: a table of (door, payload, expectation) that the arm iterates, so adding a fourth door
to `target_context` without adding its row is what reds. Round 2 recorded the same lesson for the
`print(` substring scan; this is the third arm in this build to pass by finding nothing, so the
class deserves a documented check in the build README as well as an arm.

---

## H2 — high — a `merged` row leaves the target DIRTY, and blocks the next writing verb

`tools/govkit/govkit.py:3424` (the exclusion predicate), with the row minted at `:3773` and both
`oid` stamps scoped at `:3864` and `:4068`.

Reproduced end to end by two lenses on two different kits.

`apply` writes a `merged` row and appends its destination to `staged`, deliberately giving it no
`oid`. `LANDABLE_ROLES` derives to the `write` kinds only (`:1615`), and `ROLE_KINDS["merged"]` is
`"blocked"` (`:1594`), so neither `oid`-stamping loop reaches the row. Carve-out 3 in
`dirty_claimed_paths` needs an `oid` to compare and skips it. The S4 exclusion at `:3424` only drops
rows whose `UPDATE_ROLE` is `pins`, and `UPDATE_ROLE["merged"]` is `block` (`:4396`). So the row
falls through every escape and reads DIRTY.

Live, on a clean scratch target: `apply --kits pytest-parallel-guardrails` exits 0 and stages
`pyproject.toml`; `update --write` immediately afterwards exits 2 with
`1 path(s) this target's receipt claims are DIRTY: pyproject.toml`; a second `apply` exits 2 with the
same message, so `apply --resume` is blocked identically. The independent reproduction with
`--kits push-main` gives the same result on `.githooks/pre-commit`. The operator's only route back to
green is committing a file gov just wrote — which is verbatim the burden owner ruling A was taken to
remove, and the function's own docstring names it.

Three shipped descriptors declare `role = "merged"`: `tools/pytest-parallel-guardrails/kit.toml:15`,
`tools/govkit/entries/push-main.kit.toml:30`, `tools/govkit/entries/settings-merge.kit.toml:18`. The
ruling-A arms use `--kits memory-tree`, which declares none, so the class passes by finding nothing —
the same shape as H1.

**Fix.** Scope the dirty population to the one disposition that can actually write, which is the
narrowing already made for `_cmd_update`'s `shadowed` guard in this same diff:
`if UPDATE_ROLE.get(row.get("role", "engine")) == "table"`. `block`, `report`, `skip` and `adopter`
can no more meet S4's raw-write hazard than `pins` can, by the criterion the function's own comment
states. Do NOT reach for stamping `oid` on merged rows — the comment at `:4060-4066` records that
making the stamp role-blind regressed `-7` S9's exactly-one-shape criterion, and that lesson cost a
round already.

**Left-shift gate.** An arm that applies a kit carrying a `merged` rule (any of the three) and
asserts `update --write` straight afterwards is not blocked. Better: make the fixture selection
derived — assert that the ruling-A arms cover at least one kit per `ROLE_KINDS` value, so a role
added later without a fixture reds instead of being silently uncovered.

---

## H3 — high — containment is checked inside the write loop, so a refusal lands mid-install

`tools/govkit/govkit.py:3734`, inside `for eid in selection:` at `:3716`.

`demand_contained_rows` runs one entry above that entry's own write loop. A containment refusal
raised for entry N therefore fires only after entries 1..N-1 have already been written and staged.
`.gitattributes` is written and `git add`ed at `:3701-3703`, before the LAND loop even starts, and
`install.json` is written at `:4308`, far below it.

Reproduced: a target with an escaping `[answers] memory_root` and a two-kit selection exits 2 with
the containment refusal for the SECOND entry, having already written the first entry's files, created
and staged `.gitattributes`, created `.governance/outbox/` — and written NO `install.json`.
`govkit check --target` over the wreckage then answers `NOT LANDED (no .governance/install.json)`
across a half-installed tree. The operator cleans up by hand.

The sibling comparison is the argument: `validate_gate_runner` calls `demand_contained_dest` from the
PRE-WRITE pass (`:2837`, reached at `:3636`) for exactly this reason, and its own comment says so —
"legs are emitted last, so a bad declaration caught at emission time refuses after everything else has
landed". The sibling guard landed in the right pass and this one did not.

One correction to the finding as filed, which does not change the verdict: the stated trigger
`answers.playbook_path` is not a real token — the playbook kit's destinations use `{prefix}` and
`{relpath}` only. The reachable escaping answer is `memory_root`, used by memory-tree, unattended and
workflows.

**Fix.** Hoist it. Iterate `selection` once before the LAND step, beside `validate_gate_runner`,
resolve each entry and run `demand_contained_rows` over all of them; then start writing. The
per-entry call at `:3734` can go.

**Left-shift gate.** The existing arm at `selftest.py:2583` tests a SINGLE-kit selection, where the
offending entry is necessarily the first — it structurally cannot see an ordering bug. Change it to a
multi-kit selection with the escape in the LAST entry, and assert the negative that matters: after the
refusal, the target contains no gov-written file at all. That is the property, not the message.

---

## M1 — medium — the same `pins` exclusion disarms S4 for `apply`

`tools/govkit/govkit.py:3424-3425`.

The mirror image of H2, in the same predicate. The exclusion drops every `UPDATE_ROLE == "pins"` row
— i.e. `.gitattributes` — from the S4 dirty population for BOTH writing verbs, justified by a comment
citing `UPDATE_ROLE`, which selfcheck arm 7g itself describes as "`update`'s dispatch". "Recompute,
compare, report; never write" is a property of `_cmd_update` alone.

`_cmd_apply` demonstrably writes and stages that file: `ga_path.write_text(new, ...)` at `:3700` and
`git add -- .gitattributes` at `:3702`. `demand_writable_target` calls the cleanliness check for both
verbs. So a re-`apply` over a target with an uncommitted `.gitattributes` edit no longer refuses: an
edit inside gov's marked block is replaced by `write_block`, and an edit outside it is `git add`ed
wholesale into an index gov does not own. The renormalize guard 300 lines below refuses precisely
this, in those words — "rather than folding somebody's work-in-progress into an index gov does not
own" (`:4022`) — over a different population. Two guards, one hazard, opposite answers.

Held at medium rather than high: the population is one file, and what is destroyed is inside a
gov-marked region. It is still a live weakening of the guard, introduced by this diff, and it buys
nothing — the burden ruling A removed is `update --write` straight after `apply`, which does not
require touching `apply` at all.

**Fix.** Scope the exclusion to the call site that cannot write the row. The `verb` parameter is
already in hand: `if verb == "apply" or UPDATE_ROLE.get(...) != "pins"`. If H2's fix lands as the
`== "table"` narrowing, apply the same verb scoping to it.

**Left-shift gate.** The negative arm the suite lacks: dirty `.gitattributes`, run `apply`, assert it
still refuses. The existing ruling-A arms only ever exercise `update`, which is why an exclusion
written for `update` reached `apply` unremarked.

---

## M2 — medium — both token classes admit a TRAILING newline

`tools/govkit/govkit.py:571` and `:657`, with the diagnostic at `:675`.

Python's `$` matches immediately before a trailing newline. I ran both patterns at the range head:
`TOKEN_VALUE_RE.match("tools\n")` and `ANSWER_VALUE_RE.match("tools\n")` are both True. So a trailing
newline passes the STRICT class — the one written for values interpolated into argv this engine runs.
`target_context` only `.strip("/")`s the prefix, so
`target_context(., {"prefix": "tools\n"}, "drift-audit", {})` returns `kit == 'tools\n/drift-audit'`,
which I confirmed directly.

Interpolated into `tools/drift-audit/kit.toml:80` that yields a `bash -c` string whose first line is
`python tools` and whose second is `/drift-audit/drift_report.py --check`: the intended command is
truncated and the exit status becomes that of a fabricated second one. A newline is a command
separator, and the guard's own comment at `:651-653` lists exactly that class as refused.

Scoped honestly: this is truncation and exit-status forgery, not the arbitrary execution B1 buys —
only a value ENDING in a newline passes, since an interior one fails both patterns. It is a hole in
the one guard the security model rests on, and the second half is worse for diagnosis than for
security: for body `a\nb` the match fails and the per-character scan at `:675` finds nothing bad, by
the same `$` rule, so the refusal message reads `carries ''` and names no offending character.

**Fix.** `rx.fullmatch(body)` — or `\Z` for `$` — in `demand_safe_token` AND in the `bad` set
comprehension. Both, or the diagnostic stays broken.

**Left-shift gate.** Add a trailing-newline row to the `[-12] TOKEN` table and a trailing variant to
the `_metas` loop, which today wraps every metacharacter as `a{m}b` and so tests only the interior
position. Pair it with H1's space row: one arm, three positions (leading, interior, trailing), every
metacharacter.

---

## M3 — medium — the `oid` re-stamp is gated on the wrong condition

`tools/govkit/govkit.py:4067`.

The post-renormalize re-stamp exists because `git add --renormalize` rewrites index blobs after the
first `oid` was taken at `:3865`. It is gated on `if staged:` — "the LAND step wrote something" — not
on whether the renormalize ran. Those are different conditions, and the renormalize block is gated on
`pins`, which is the union of this selection and every kit the receipt already claims (`:3686`).

So: a re-`apply` of an all-`seed` selection whose files already exist lands nothing new (`staged`
empty) while `pins` is non-empty, the renormalize runs, and the rows keep blobs the target no longer
holds. Two shipped entries declare exactly one `seed` rule each —
`tools/govkit/entries/check-kit-versions.kit.toml` and `tools/govkit/entries/playbook.kit.toml` —
and apply's seed arm skips `staged.append` when the destination exists while still appending a
landable row that gets stamped.

The obvious refutation — "the dirty guard above the renormalize would refuse anyway, since a blob it
rewrites must differ from HEAD" — was tested and fails. In a scratch repo with a committed CRLF file
and a newly added `*.sh text eol=lf`, `git diff --name-only HEAD` printed nothing while
`git add --renormalize` rewrote the index blob. The guard is blind to exactly the population the
renormalize moves.

Consequence: on the CRLF adopter this whole mechanism exists for, the receipt records blobs the target
does not hold — and via ruling A's carve-out at `:3388`, which compares precisely that field, those
paths read DIRTY on the next writing verb. Narrower than H2 (the stale row's own path must be one the
renormalize actually moves, which needs the pin to be new to that path), but it is measurably the
wrong condition guarding the field ruling A depends on.

**Fix.** Set a flag inside the `if pins:` block when `git add --renormalize` is invoked, and re-stamp
when that flag is set OR `staged` is non-empty.

**Left-shift gate.** An arm that re-applies an all-`seed` selection into a target with LF pins already
present and asserts every receipt `oid` still matches `index_read`. State the invariant once —
"after apply, every landable row's `oid` equals the target's index blob" — and assert it at the end of
every apply-shaped arm rather than in one place.

---

## M4 — medium — the spawn census allowlists the module's own git wrapper

`tools/govkit/selftest.py:6004`.

`_git_plumbing1` decides plumbing-ness from the LITERAL elements of the argv list. For
`govkit.py:109` — `["git", "-C", str(root), *args]` — that list is `['git', '-C']`, so
`"hook" in _words and "run" in _words` is False and the call is allowlisted unconditionally, with no
resolvable subcommand at all. Same for `index_read` (`:3164`) and `_names` (`:3367`). I ran the
predicate over the real tree to confirm.

The census correctly finds today's eight sites, and the inline
`["git", "-C", str(target), "hook", "run", "pre-commit"]` at `govkit.py:2977` is the one the by-name
exclusion catches. But the by-name mechanism IS the guarantee the declaration's header sells — "every
`subprocess.run`/`Popen`, minus an allowlist of literal `git` plumbing argv", with `git hook run`
"excluded from that allowlist BY NAME" — and it is defeated by the module's own primary git wrapper.
One future `git(target, "hook", "run", "pre-commit")` spawns target-authored hook code with zero
census rows, zero label and a green both-directions arm.

No live exploit today: all eight `git()` callers pass gov's own `root` with literal subcommands. This
is a latent gate gap, and it is the M2-from-round-3 shape — a guarantee narrower than the sentence
selling it — reintroduced inside the fix for it.

**Fix.** Make an unresolvable subcommand a census HIT rather than an allowlist entry: in
`_git_plumbing1`, return False if any element before a `--` is a `Starred` or a non-`Constant` node.
`govkit.git` then lands in `_exec_found` and must take a `SHELL_EXEC_SITES` row — label it `gov`
today, and the row forces the next reader to re-answer when a caller passes `hook`/`run`.

**Left-shift gate.** That change is the gate. Add the negative fixture that proves it can fail: a
synthetic call node with a starred tail, asserted to be a hit. An allowlist predicate nobody has seen
refuse anything is an allowlist that allows everything.

---

## M5 — medium — ruling A's payoff arm asserts an absence and never a success

`tools/govkit/selftest.py:2496`.

The arm carrying owner ruling A's entire payoff asserts `"DIRTY" not in _poa2.stderr` and never
touches `_poa2.returncode`. The negative twin further down asserts
`_poa3.returncode == 2 and "DIRTY" in _poa3.stderr` — a one-token asymmetry inside the same fixture,
which is what makes it visible.

I checked the downstream arms as a possible mitigation and they do not cover it: the receipt re-read
and the `oid` invariant grade the receipt `apply` wrote against the index, which a failed
`update --write` leaves unchanged, and the `>= 10` liveness counts apply's rows. The verb does pass
today — a fresh intake + apply + `update --write` returns 0 with no DIRTY — so this is a latent
one-sided assertion, not a currently-masked failure.

Two qualifications the raw finding overstates, kept here because the record should not be more
alarming than the code. The arm is NOT could-not-fail for its own subject: a regression in the `oid`
carve-out re-emits the DIRTY refusal and the arm goes red. And a generally broken `update` fails the
twin three lines down. The residual blind spot needs a failure mode that refuses on the clean
post-apply tree but gets DIRTY-masked on the dirtied one — narrower than "any refusal", still a real
hole, and in a repo whose charter names exactly this defect class it is not one to leave.

**Fix.** `_poa2.returncode == 0 and "DIRTY" not in _poa2.stderr`, with the return code in the detail
string. Same treatment for the `[-12] RULING-B` arm's `"absent from its INDEX" not in _pob.stderr`,
which has the identical shape.

**Left-shift gate.** A meta-arm over the suite's own source: any assertion whose predicate is a bare
`X not in <proc>.stderr` must also constrain that proc's `returncode`. This is the third
absence-only arm this build has produced (round 2's `print(` scan, H1's fixture, this one), so the
class has earned a mechanical check rather than a third hand-fix.

---

## M6 — medium — one absent spec file kills the whole build's plan table

`tools/unattended/unattended.sh:1575`.

`spec_facts` hands `"$@"` — every spec of a build — to ONE awk invocation. `load_spec_facts` reads its
stdout through a process substitution and never tests the status. `set -e` is off, by the driver's own
comment.

Reproduced: GNU Awk 5.4.0 given five spec paths with the third absent printed exactly ONE row, then
`fatal: cannot open file`, and exited 2. Rows two, four and five produced nothing — row two because
it is only flushed by row three's `FNR==1`. `git ls-files` lists index entries, so an ordinary
worktree deletion, a sparse checkout, a mid-rename or a mid-merge state reaches this.

In `verb_plan` the three maps then come back near-empty, `SPEC_PATH` misses, and every unit in the
rendered region prints `NO TRACKED SPEC (rendered row without one)` at exit 0 — a complete-looking,
wholly fabricated table on the one verb an agent reads to pick up work. The per-spec awk this
replaced localised the damage to the missing file.

Scope note: this function does not exist in the `dCarriedReceipt` worktree, which is one commit
behind; it arrived on `main` via `3f8c7ebe` and is inside the reviewed range. The `_renderable == 0`
detail is also position-dependent — with a later gap some rows survive. The defect and its impact
hold either way.

**Fix.** Filter before the batch: drop arguments that are not readable files, and emit a row with
empty id and status for each dropped path, so the caller sees `NOT A UNIT` for that one file instead
of losing the build.

**Left-shift gate.** Test the status. `load_spec_facts` should refuse loudly when `spec_facts` exits
non-zero — a driver that renders a plan table from a failed producer is the worst possible failure
mode, because it is indistinguishable from a correct one. Add the arm: a build with one tracked spec
deleted from the worktree, asserting `plan` names that spec and grades the others.

---

## L1 — low — the RUN INTEGRITY splice welded a datum onto a prose sentence

`tools/workflows/drift-audit-code.js:416`.

Verified at the range head. Line 416 ends
`...Say so where you would otherwise call a zero positive evidence., severity corrections ${downgrades}`
— the fragment was cut off the `counts:` line at `:413` and welded onto the tail of an unrelated
sentence about lens deaths. `downgrades` is still computed and still returned as `severityCorrections`,
so the datum is not lost; it is the PROMPT INPUT that is corrupted, and the prose eight lines above
instructs the agent to state the correction direction beside precision — so the number is no longer
where the instruction points.

`tools/workflows/drift-audit-state.js` took the same block cleanly because its counts line never
carried the datum, which is exactly why the mis-splice survived the port.

**Fix.** Move `, severity corrections ${downgrades}` back onto the end of the `counts:` line at
`:413`; end `:416` at `...call a zero positive evidence.`

**Left-shift gate.** Not worth a gate of its own. Fold it into the harness's existing shape check if
one exists, or accept it as a documented check: when porting a prompt block between the two
harnesses, diff the two `counts:` lines afterwards. The sibling asymmetry is what found it and is the
cheapest detector.

---

## L2 — low — a MISSING ratchet falls through its own guard

`tools/check-install-prefix.sh:231`.

Narrowing the guard to `[ ! -s "$CARRIED" ] && [ -n "$rows" ]` means a genuinely missing `$CARRIED`
falls through whenever the hit set is zero — which is the goal state the same commit added L1 to
support. The awk two lines below then cannot open its first file.

Reproduced in a hermetic scratch repo with the real script: awk exits 2 with
`fatal: cannot open file`, `cstat` is non-zero, and the gate prints the carried-literal remedy
("apply writes gov's bytes VERBATIM...") instead of the accurate
`install-prefix: no <file> — run --write-ratchet once and commit it`. Both controls isolate it:
empty-but-present with zero rows exits 0 clean (so `-s` over `-f` still buys what D4 wanted), and
missing with non-empty rows prints the correct message.

The gate still reds, so this is a wrong remedy rather than a green-by-absence — hence low. The clear
message is unreachable in exactly the state the change was written to permit.

**Fix.** Split the two states: `if [ ! -e "$CARRIED" ]` keeps the original refusal unconditionally,
and the `[ -n "$rows" ]` narrowing applies only to the empty-but-present case.

**Left-shift gate.** The gate's own self-test should assert the MESSAGE, not just the exit code, for
each of the four (present/missing × zero/non-zero) states. A refusal that reds for the wrong reason
teaches the operator the wrong repair, which costs more than the red.

---

## L3 — low — the `target`/`gov` label derivation is a flat substring test

`tools/govkit/selftest.py:6120`.

`_derived_target` is a substring test over each spawn site's OWN function source against a flat
name→source map, so it is not transitive. The live evidence is stronger than the finding as filed: I
ran it over the eight declared sites and it derives only FIVE. `read_gate_verdicts` is labelled
`target` BY HAND and contains neither `target_context` nor `resolve_tokens`, yet it spawns
`resolve_shell_argv(list(cmd))` at `govkit.py:2910` where `cmd` is the TARGET's own
`[gate_runner].command`.

So a target-controlled site whose argv is resolved through a helper already exists today, and the
check is one-directional — it only reds derived-target rows typed `gov`. The comment's claim that the
label is DERIVED so "the next spawn cannot be mislabelled by hand" is already false for one of the
six sites. The finding's supporting sentence (that all eight are caught because each calls
`resolve_tokens` inline) is wrong in detail; the defect it names is real and reachable now rather than
after a hypothetical refactor.

**Fix.** Walk the call graph one or two hops: build `callees[fn]` from `ast.Call` nodes with
`ast.Name` funcs and close `_derived_target` transitively before comparing. Cheaper alternative:
assert in the arm that every site's own body contains a resolution call, so a future indirection reds
instead of passing.

**Left-shift gate.** Make the check bidirectional as part of the fix — a row typed `target` that
derives as `gov` should red too, which is what would have caught `read_gate_verdicts` on the day it
was labelled. A one-directional derivation check is half a gate.

---

## L4 — low — `demand_contained_rows` claims two callers, has one, and carries a dead branch

`tools/govkit/govkit.py:1745`, with the unreachable branch at `:1752-1755`.

Both sub-claims verify. The whole repo has two hits for the symbol: the definition and ONE call site,
`_cmd_apply` at `:3734`. The docstring says "One reader, two callers". The intended second producer,
`planned_writes`, inlines `demand_contained_dest` at `:1821` with its own comment explaining why —
plan rows never carried `row["rule"]`, so the machine/link exemption could not fire there.

The `attributes` / `.gitattributes:<pattern>` exemption is consequently dead from the sole caller:
those destinations are minted only inside `planned_writes` at `:1832`, and the rows the one caller
passes come from `resolve_entry`, whose roles come from descriptor `[[files]]` rules — `attributes`
is not in `ROLE_KINDS`, and selfcheck arm 3b refuses any role that is not.

No wrong behaviour today. It is residue from an abandoned two-caller design, and it is the
comment-versus-code class this same diff spends three paragraphs correcting elsewhere — a docstring
asserting a caller count the code does not hold, plus a branch for a row shape that cannot arrive.
The next reader adding a caller will trust both.

**Fix.** Two-line deletion of the branch plus a corrected docstring naming its one caller. Or route
`planned_writes` through the function so the claim becomes true and the branch live — it already
handles the machine/link exemption that forced the inline copy, and only needs the plan row's rule
index threaded through. Prefer the deletion; the second option is a refactor wearing a comment fix's
clothes.

**Left-shift gate.** None warranted for this instance. The class — a docstring asserting a caller
count — is cheap to gate if it recurs: a check that any docstring naming "N callers" matches the grep
count. One occurrence is not a pattern; record it as a documented check and gate it on the second.

---

## What this round says about the last three

Every blocker this build has produced is the same mistake in a different costume: a guard was written
for the entry point in front of the author and applied to a population nobody enumerated. Round 2's
token guard bounded `prefix`. Round 3's containment guard bounded `apply`'s dest and needed three
sites, not one. Round 4's blocker is the token guard again, bypassed through the two doors round 2
never listed.

The selftest suite has now shipped four arms that pass by finding nothing (round 2's `print(` scan,
plus H1, M5 and — latently — M4 and L3 here). That is not bad luck. It is what happens when an arm is
written against the INSTANCE a review named instead of the CLASS the instance belongs to, which is
the rule §7 states and the rule this build keeps re-learning. The three structural gates proposed
above — a descriptor-level scan for prose tokens inside `-c` strings, a door-parameterised injection
table, and a meta-arm banning absence-only assertions — are worth more than the fourteen point fixes,
because they are the only ones that fail for a defect nobody has met yet.
