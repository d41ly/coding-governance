# review-dClosedLexicon-8 — Tier-2 review of the `**`-claims-nothing-others-own fix

**Serves:** diff-review TOOL-dClosedLexicon-4  <!-- inferred: its H1 names the file-rule fix that unit owns -->

## Verdict: PASS WITH FINDINGS — 0 blockers, 1 high

The fix is correct and the defect it names is real: destination-only exclusion is the right rule, the
source-exclusion first cut genuinely under-lands, and I found no descriptor in this repo where the new
pool either clobbers or under-lands. The high is one function away from the fix, not in it —
`plan` never learned to expand a `**` rule, so reverting `tools/lexicon/kit.toml` to `**` moved the one
descriptor whose preflight was complete into the class where it is not.

**Subject:** ONE commit, `40f280b` — TOOL-dClosedLexicon-4 · streams `tooling` · node d · 2026-08-16

| commit | unit |
|---|---|
| `40f280b` | TOOL-dClosedLexicon-4 — a `**` file rule must not claim what another rule owns |

**Binding spec:** `memory/builds/dClosedLexicon/spec/2026-08-16-spec-dClosedLexicon-4.md` at rev-2.
**Bar at subject:** 63/63 green (confirmed by the commit message; not re-run here).

**Explicitly OUT of scope:** everything under `f7306f3` and below. No finding re-raises one folded by
review rounds 1–7.

## Review shape

| | |
|---|---|
| raw findings | 13 |
| confirmed (survived an adversarial skeptic) | 10 |
| refuted | 3 |
| unverified / outstanding | 0 |
| precision | 0.77 |
| **distinct defects after dedupe** | **4** |

The 10 confirmed findings collapse to 4 distinct defects: ids 1/4/7/11 are one plan-vs-apply
divergence, ids 2/12 are one unchecked exit code, ids 6/10/13 are one stale docstring summary, and
id 8 stands alone. Each is filed once below with the strongest measurement from the cluster.

---

## The four judge questions, answered

**Q1 — Is destination-only exclusion correct and complete across this repo's real descriptors?**
YES, on the evidence. All 19 tracked descriptors (`tools/*/kit.toml` + `tools/govkit/entries/*.toml`)
were enumerated; 10 carry a `**` engine rule. No descriptor was found where the new pool still
clobbers a later rule's path, and none where it now under-lands. The source-vs-destination choice is
load-bearing and correct: re-adding source exclusion to a clone drops drift-audit's pool from 8 files
to 6 and stops shipping `drift_signals.template.py`, reddening AC3's arm — reproduced.

**Q2 — Is skipping other `**` rules right, and what about two wildcards / `include = []` / a `to` list
/ `{relpath}`?** No descriptor in this tree has two real `**` rules (lexicon's apparent second hit is
a prose mention inside a comment at `tools/lexicon/kit.toml:11`), so the mutual-skip branch is
unreachable today and its "neither is more specific" reasoning is sound if one ever lands.
`include = []` yields no sources and therefore claims nothing — correct, a rule that names no source
owns no destination. A `to` list is handled: `resolve_dests` returns every element. `{relpath}` is
substituted literally before `resolve_tokens`, so it cannot survive into a claim string. The one real
gap in this area is finding 3 below, and its reachable half is on the write path, not the claim path.

**Q3 — Do the four new arms pin what they claim?** Two of four do not, and the two that do not are the
two carrying the headline guarantee. See finding 2 — demonstrated by injecting a drift-audit-scoped
refusal into `cmd_apply` and watching the suite print `all arms held` while nothing ran.

**Q4 — Does anything else in govkit now disagree with `apply`?** YES — `plan`. See finding 1. That is
the exact class the brief calls "worse than the original bug", and it arrives from the descriptor
side (`tools/lexicon/kit.toml`) rather than the engine side. `check`, `intake`, `selfcheck`, the
receipt and `entry_members` were examined and do not disagree.

---

## Findings, severity-ranked

### [HIGH] 1 — `plan` under-reports lexicon's install by 9 of 12 writes

**`tools/lexicon/kit.toml:17`** (root cause at **`tools/govkit/govkit.py:546`**)
*(consolidates ids 1, 4, 7, 11 — four independent verifiers, identical measurements)*

Reverting the engine rule to `include = "**"` moves lexicon into the class where `govkit plan` sees
nothing. `planned_writes` resolves sources through `rule_sources()`, which at `govkit.py:137` does
`if not s or any(ch in s for ch in "*?["): continue` — so a `**` rule contributes zero sources. With
no `to`, `rule_destinations()` returns `[]`, and the `if not dests` fallback at line 555 iterates the
empty source list. The rule emits **no row at all**, while `cmd_apply` at lines 851–859 pools
`tracked(root)` under `home` and writes every survivor.

**Reproduced independently, and again by me at `40f280b` against a scratch target:**

```
plan  --kits lexicon  ->  3 write(s)     (the three seed waiver registries only)
apply --kits lexicon  ->  landed 12 file(s), receipt: 12 file(s)
```

With `git show 40f280b^:tools/lexicon/kit.toml` restored, the same `plan` printed `12 write(s)`. This
commit is demonstrably what moved lexicon from a complete preflight to a 25%-complete one. Nine engine
files — `adopt-lexicon.sh`, `lexicon.py`, `kit.toml` among them — now land, and are overwritten on
every re-apply, without ever appearing in the plan the operator approved.

Three things make this more than a cosmetic gap:

- `planned_writes`' own docstring (`govkit.py:534`) promises "Every file `apply` would write".
- `skills/deploy-governance/SKILL.md:42` says plan "Lists every file `apply` would write".
- This commit's own spec (`…-spec-dClosedLexicon-4.md:106`) rests its production-readiness on
  "`plan` output already lists destinations per role, so the exclusion is visible before any write".
  That is measurably false for the very rule class the unit redefined: for a `**` rule plan lists
  nothing, so neither the writes nor the new exclusions are visible before the write.

The reverse direction also misreports: `plan --kits drift-audit` prints
`write [project-owned] tools/drift-audit/drift_signals.py` and `write [rendered] .claude/skills/…`,
neither role being in `LANDABLE_ROLES` — two writes `apply` is designed never to make.

**Severity caveat, recorded not hidden:** the divergence pre-exists for the other 9 `**` descriptors
(verified: `plan --kits drift-audit` prints 3 writes against apply's 8), so the engine defect is not
new. One verifier argued this puts it nearer medium. It is filed high because `plan` is the read-only
verb an operator authorizes a write-into-someone-else's-repo against, its summary line asserts a
count, and this commit is what made that count wrong for the last accurately-planned kit.

**Fix.** Single-source the pool the same way the diff single-sourced `resolve_dests`. Extract the
`any(s == "**")` branch of `cmd_apply` (`govkit.py:851-859`) into a
`resolve_pool(root, desc, rule, ctx, home)` beside `resolve_dests`/`scan_claimed_paths`, and call it
from `planned_writes` (`govkit.py:546`) so a `**` rule's `srcs` is the list `apply` will iterate; then
emit one `write` row per `resolve_dests()` instead of the `rule_destinations()`-or-basename fallback.
While there, mark rows whose role is outside `LANDABLE_ROLES` as skipped rather than `write`. One pool
computation, one destination computation, both verbs — which is the argument the commit message
already makes for `resolve_dests`.

**Left-shift gate.** Add a leg to `python tools/govkit/selftest.py` that, for at least one `**` kit,
asserts the set of `write` destinations printed by `plan` equals the set of paths in the receipt
`apply` writes — set equality, not counts, so a role-filter bug in either direction reds. Wildcards
are now the normal descriptor shape here (10 of 19), so this is not a one-kit arm.

---

### [MEDIUM] 2 — the re-apply's exit code is discarded, so both protection arms pass on a no-op

**`tools/govkit/selftest.py:366`** *(consolidates ids 2, 12)*

`run("apply", "--target", str(t), "--kits", "drift-audit")` on line 366 discards the
`CompletedProcess` — no return code, no stdout assertion — unlike the first apply on line 352, which
is bound as `first` and checked. The two arms that follow are the **only** arms pinning the protection
half of this fix, and both are satisfied by the subject never running:

- line 367: `"ADOPTER EDIT" in seeded.read_text()` is true precisely when nothing was written.
- line 372: `landed_after == landed_before` compares two `iterdir()` listings of a directory a
  refusal never touches.

**Demonstrated by two verifiers independently.** Injecting into `cmd_apply` a refusal that fires only
when a receipt exists and `drift-audit` is in the selection makes the second apply exit 2 and write
nothing; the suite still prints `govkit-selftest: all arms held`, with both AC1 and AC2 reporting ok.
A `Refusal` exits 2 via `govkit.py:1100-1102` before any write.

The pre-existing exit-code arm — "a second apply is NOT refused — the receipt authorises it"
(`selftest.py:211`) — does **not** cover this: different fixture (`ap`), different kit
(`check-wiring`), so it only catches an unscoped refusal. Any future drift-audit-scoped refusal (a
`merged` rule added to the descriptor, a `requires` enforcement, a new answer key going unresolved, a
`foreign_kit_present` regression) silently unpins the silent-data-destruction fix while the bar stays
63/63 green.

This is also the class the file's own header contract forbids — "never an exit code alone" cuts both
ways, and an on-disk effect indistinguishable from inaction is the same vacuity the memory-recall
selftest keeps a note about.

**Fix.** Bind and assert, same shape as the first apply:

```python
second = run("apply", "--target", str(t), "--kits", "drift-audit")
check("the re-apply actually ran",
      second.returncode == 0 and "govkit apply — landed" in second.stdout,
      second.stdout + second.stderr)
```

placed **before** the two protection arms. Do the same for the unchecked `intake` call on line 351.

**Left-shift gate.** This is a general shape, not a one-site slip: extend
`tools/memory-tree/check-arms.py` (or add a govkit-scoped sibling) with a rule that a bare `run(...)`
call in a selftest whose result is discarded reds unless the call site carries an explicit
`# no-assert:` marker with a reason. The harness meta-gate already enforces "every `fail` branch armed
by a positive assertion"; "every subject invocation asserted to have run" is the same predicate on the
other side of the call.

---

### [MEDIUM] 3 — `resolve_dests` drops the `missing` list `resolve_tokens` exists to hand back

**`tools/govkit/govkit.py:699`** *(id 8)*

`resolve_dests` calls `resolve_tokens(...)[0]` and discards the second element. It is now the single
reader for both the write loop and the new exclusion set, so the decision lives in exactly one place —
and that place throws it away.

**Reachable half, MEASURED, on the default selection.** Against a scratch repo whose
`.governance/deploy.toml` supplies no `manifest_path`:

- `plan --kits kickoff-manifest` prints `UNRES. [seed] {manifest_path}` and exits 1 with the
  named-key refusal.
- `apply --kits kickoff-manifest` writes a file **literally named `{manifest_path}`** into the target
  root, `git add`s it, writes a receipt claiming 2 files, and exits 0.

`kickoff-manifest` is in `registry.toml`'s declared default selection. This is not by design:
`resolve_tokens`' own docstring (`govkit.py:226-231`) says emitting a braced path is how a deployer
writes a literal `{memory_root}` into somebody's repository, and that the caller is handed the missing
names to decide. There is no `--unattended` flag; plain `apply` is the only writing verb, and it
discards the list. Verified identical at `f7306f3`, so the write predates this commit — but the
extraction is now the one place the decision lives, which is why it is filed here.

**Refuted half, recorded.** The proposed second seam — a sibling rule whose `to` carries an unresolved
token contributing a claim string with a surviving `{...}` that can never intersect a resolved
destination, silently evaporating the new protection — does **not** hold today. Across all 21
descriptors, every sibling `to` that could collide with a `**` rule's namespace uses `{kit}`,
`{memory_root}` (unconditionally defaulted in `target_context`), `{relpath}` (substituted literally
before `resolve_tokens`) or a literal path. No claim string can carry a surviving brace. Latent, not
reachable. The finding is confirmed on the strength of the measured half only.

**Fix.** Return the missing names from `resolve_dests` (`tuple[list[str], list[str]]`) or pass it the
`Report`. In `cmd_apply`, `r.fail` and skip the write on any missing key so `apply` refuses where
`plan` refuses. In `scan_claimed_paths`, treat an unresolvable claim as a refusal rather than as a
claim that matches nothing — that closes the latent half at the same time.

**Left-shift gate.** Add a govkit selftest arm asserting `plan` and `apply` agree on **refusal**, not
just on writes: for a target missing a required answer key, both verbs must exit non-zero and neither
may leave a path containing `{` or `}` anywhere under the target. A brace-in-a-written-path check is
cheap, total, and catches every future token that gets added without a resolver.

---

### [LOW] 4 — `scan_claimed_paths`' summary line states the rejected design

**`tools/govkit/govkit.py:707`** *(consolidates ids 6, 10, 13)*

The one-line summary reads "Every source and destination some OTHER rule in this descriptor already
owns." The body (lines 727–737) only ever does `claimed.update(resolve_dests(...))` — destinations
only; a source is consumed purely as the argument to `resolve_dests` and is never added to the set.
Lines 715–720 of the same docstring say **"CLAIMED BY DESTINATION, NOT BY SOURCE"** in capitals and
record the 8-files-to-6 measurement that refutes the summary sitting three lines above them.

So the summary names precisely the first cut that was built during this build, measured wrong, and
cut — shipped as the one-line contract of the function that removed it. Reproduced cost of acting on
it: re-adding source exclusion drops drift-audit's pool to
`['README.md', 'adopt-drift-audit.sh', 'drift_report.py', 'drift_signals.py', 'kit.toml', 'selftest.py']`,
`drift_signals.template.py` stops shipping, and AC3's arm reds.

**One leg of the reported impact does not hold, and is recorded as refuted:**
`memory/map/generated/symbols.json:1561` stores only `{id, kind, file}` for this symbol and nothing
under `tools/codebase-map/` extracts docstrings, so no reuse-lookup snippet or map render carries the
wrong sentence, and `help()` shows the correcting paragraph alongside it. That caps this at low —
a stale summary a future author could act on, not a functional defect or a propagating one.

**Fix.** `"""Every DESTINATION some OTHER rule in this descriptor already owns.` — the
"CLAIMED BY DESTINATION, NOT BY SOURCE" paragraph then reads as the elaboration it was written to be
rather than as a contradiction of the line above it.

**Left-shift gate.** Nothing gates this: the govkit selftest asserts messages and on-disk effects, and
the playbook-parity / charter-completeness legs cover prose elsewhere but not docstrings. A general
docstring-vs-code gate is not worth building. What is worth building is narrow: a govkit selftest arm
that greps `scan_claimed_paths`' docstring for the token `source` in its **summary line only** and
reds — this one function's contract is the whole subject of the unit, and it has now been written
wrong once.

---

## What was checked and found clean

- **All 19 descriptors enumerated** (`tools/*/kit.toml`, `tools/govkit/entries/*.toml`); 10 carry a
  `**` engine rule. No clobber and no under-land found in any of them under the new rule.
- **`check`, `intake`, `selfcheck`, `entry_members`, the receipt** — none reads file rules in a way
  that now disagrees with `apply`. The only divergent reader is `plan` (finding 1).
- **The source-vs-destination choice is correct and the spec's record of the correction is accurate** —
  reproduced in both directions (8 files with destination-only, 6 with source exclusion added).
- **AC3 is genuinely asserted before the protection arms**, and the commit message's reasoning for
  that ordering is sound: the cheapest way to pass AC1/AC2 is to stop landing files. That ordering is
  what makes finding 2 a gap in the arms rather than a hole in the fix.
- **`{relpath}`, `to`-as-list, `include = []`, `root_relative`** — all handled correctly by
  `resolve_dests` / `scan_claimed_paths`.

## Reproduction environment

Commit `40f280b` on a clean checkout; scratch git target with
`.governance/deploy.toml` = `schema = 1`, `prefix = "tools"`. The plan/apply divergence for lexicon
(3 vs 12) was re-measured for this report; the finding-2 refusal injection, the finding-3
`{manifest_path}` write, and the source-exclusion under-land were each reproduced by two or more
independent verifiers with matching numbers.
