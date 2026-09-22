# Spec briefs — cMendedVintage, all 23 units

**Serves:** journal DEPL-cMendedVintage-1 DEPL-cMendedVintage-2 DEPL-cMendedVintage-3 DEPL-cMendedVintage-4 DEPL-cMendedVintage-5 DEPL-cMendedVintage-6 DEPL-cMendedVintage-7 DEPL-cMendedVintage-8 DEPL-cMendedVintage-9 DEPL-cMendedVintage-10 DEPL-cMendedVintage-11 DEPL-cMendedVintage-12 DEPL-cMendedVintage-13 DEPL-cMendedVintage-14 TOOL-cMendedVintage-1 TOOL-cMendedVintage-2 TOOL-cMendedVintage-3 TOOL-cMendedVintage-4 TOOL-cMendedVintage-5 TOOL-cMendedVintage-6 TOOL-cMendedVintage-7 TOOL-cMendedVintage-8 TOOL-cMendedVintage-9

What each SPEC writer is handed. The line numbers are from BASE `859daa67` and are POINTERS, not
claims — open the file and re-derive before speccing against one. Every unit below was produced by a
five-lens verification fan with batched skeptics over an adopter session's findings: 18 diagnoses,
all 18 held, 10 of 18 originally-proposed fixes refuted and reworked. What survives is below.

## The root cause every DEPL unit serves

`update` is a byte-mover with no install-effect stage, and it then grades the target with checks that
measure install effects. `apply` has the stage; `update` has none of it, visible role by role in
`UPDATE_ROLE` at `tools/govkit/govkit.py:5433`. Renders cap at report, `.gitattributes` is
report-only, gate legs are emitted nowhere, renormalize never runs. The verify pass then re-runs each
kit's own `[check]` — the program that asks whether those effects happened — and rolls the kit back
on the red it caused. A rolled-back run takes the `if r.problems:` branch and withholds the
`gov_commit` re-stamp, so the next run classifies identically and decides identically.

---

## TOOL-cMendedVintage-9 — `--card --write` must not block on an open stdin

`skills/session-kickoff/manifest-check.sh:128`. `read_session_id` resolves the id by reading stdin
for the SessionStart hook's JSON, guarded only by `[ -t 0 ]`. That admits the hook (pipe, then EOF)
and a human at a terminal, and NOT an open pipe that never sends EOF — every tool-invoked shell.
`sed` then blocks forever. Measured live: 71 minutes at 4.4 s CPU, no children, cleared instantly
with `< /dev/null`. `--session` does not avoid it: the stdin read runs first and `CARD_SID` is only
the fallback. Smallest correct fix is to skip the stdin read entirely when `--session` was supplied,
since that is the caller answering the question the read exists to ask; a bounded read is the weaker
alternative because a bound still costs the wait. The acceptance arm must OBSERVE the hang case —
run the verb with stdin held open and assert it returns — or it grades nothing.

## DEPL-cMendedVintage-1 — no rollback over a step this run declined

Build a `_rr_stale` set populated at the two RENDER-STALENESS declines only — `govkit.py:7409` (kit
ships `rendered` rows and declares no `[[regenerate]]`) and `:7416` (the flag is off) — and NOT at
the inert decline `:7387`, which is a posture the target chose. At `:7553` branch on membership: skip
the restore loop, write the order with the decline string as its FIRST sentence, keep the `r.fail`.
Also un-gate the decline print at `:7471`, which today prints only when `GOVKIT_RERENDER=1` — a
decline that can decide a rollback must not be invisible. Every existing rollback fixture kit is role
`engine` with no rendered row, so `_rr_stale` is empty there and no shipped arm moves.

## DEPL-cMendedVintage-2 — a failed restore keeps its receipt row forward, and says which path

`govkit.py:7556-7670`. All four failure branches `continue` the path loop and fall through to an
UNCONDITIONAL tail that reverts `ROLLBACK_FIELDS` on the row and removes it from `withdrawn_rows`. So
the file stays as this run wrote it while the receipt claims the pre-run `sha256`, and `:7827`
persists that. Gate the field revert on the path actually having restored. The `origin == "landed"`
branch thirty lines up already computes this predicate for its own case — this is the same gating one
level out. Second half: the order file's "Every path marked restored below was put back" sentence
becomes false, and a failed path appears in NONE of `restored`, `removed` or `left alone`; emit a
fourth block naming it. State the half-restored case honestly: when `checkout-index` is what failed
the index was already reverted, so `sha256` matches the worktree and `oid` does not.

## DEPL-cMendedVintage-3 — the coverage tail joins each open gap to its refusal reason

`govkit.py:7797` says landing an unclaimed source is "a verb that does not exist yet". That is false
at BASE: the landing block at `:7150-7340` writes the blob, `git add`s it and mints the full row —
the exact fields the comment says it cannot invent. Delete the sentence and the stale paragraph at
`:7740`, and join `_gap_open` against `dict(_refused_new)` so each open gap prints its own reason.
For an unmatched residue print that no reason was recorded, never a claim about resolution: a
rename-decided destination is in neither set. Keep it inside the existing bare `try/except`, which is
the liveness guard.

## DEPL-cMendedVintage-4 — the unattributed remedy names a command that works

`govkit.py:7853` and `USAGE` at `:8535` both tell the operator to run `govkit adopt --re-adopt
--write`, which re-runs the identical `derive_attribution` walk over identical bytes and returns
`None` again. The working form is `--re-adopt --pin <path>=<rev>`, because `--pin` is what sets
`evidence = "pinned"`. Retire `--allow-ungraded` in the same unit: its only reader is `:7847`, so all
it does is advance the base away from rows nothing graded, writing no bytes. The gate: replace the
prose-grep at `selftest.py:8126` — which passes today while two other copies of the sentence are
wrong — with a behavioural arm plus an assertion over EVERY occurrence of `re-adopt` in a remedy.

## DEPL-cMendedVintage-5 — `[[regenerate]]` for the three kits whose adopter already renders

`tools/lexicon/kit.toml`, `tools/drift-audit/kit.toml`, `tools/memory-recall/kit.toml`. All three
entrypoints re-render with no adoption guard: `adopt-lexicon.sh` under `--render`,
`adopt-drift-audit.sh` on a bare invocation (`render > "$SKILL_OUT"`), `adopt-memory-recall.sh` under
`--scaffold`. Ship lexicon's `[[outcome]]` in the SAME edit, modelled on `tools/unattended/kit.toml`:
without it a claimed-but-unconfigured lexicon trades a silent rollback for an unaccepted `r.fail` at
`govkit.py:7440`. This unit is inert until the flag flips.

## TOOL-cMendedVintage-1 — `adopt-memory-tree.sh --render`

The one adopter with no render path: it accepts only `--scaffold` and exits 0 with "already
scaffolded — nothing to do" on an adopted tree, which is why re-adoption was never the mechanism.
It needs a narrow mode that skips the adoption guard and re-renders its four `rendered` rows. This is
a real adopter-script change, not a descriptor line, and `DEPL-cMendedVintage-8`'s gate reds this
repo until it lands.

## DEPL-cMendedVintage-6 — the regenerate stops deleting shipped fixture records

The eleventh dPolishedVitrine row, open against `tools/govkit/govkit.py`: the unattended adopter
deletes fixture records govkit ships as ENGINE rows, and the regenerate added by that build deletes
them. Measured on a fixture installed at prefix `scripts` and taken to that build's tip. THIS IS THE
PREREQUISITE FOR THE FLAG FLIP and the reason it is sequenced before it — flipping first arms a
recorded data-loss defect at every adopter, which is M3's veto 3. Close the deletion, do not merely
document it.

## DEPL-cMendedVintage-7 — `GOVKIT_RERENDER` defaults ON

`govkit.py:7380`, `os.environ.get("GOVKIT_RERENDER") == "1"` becomes a default-on read. This MUST be
the same commit that pins `GOVKIT_RERENDER="0"` into the two selftest arms whose subject is the
OFF path (`selftest.py:9484` and `:8996` strip the var from the environment and assert off-path
behaviour). Their subject is the off path, so spelling the off value there is correct; leaving them
env-stripped turns this flip into a red `govkit selftest` leg. Keep `=0` readable so an operator can
revert without a code change. This is the dark flag's promotion: `update` executes target-side code
by default for the first time. The argv is always gov's, never the target's `deploy.toml`, so the
trust boundary is unchanged — say that in §9 rather than implying the blast radius is unchanged too.

## DEPL-cMendedVintage-8 — a kit shipping `rendered` rows must declare a regenerate

Invert arm 7l's population at `govkit.py:2033`. Today it opens `if not d.get("regenerate"): continue`
— so its population is the kits that ALREADY have the block, and it grades their prose. Add, before
that line, a refusal for a descriptor shipping any `role == "rendered"` row and declaring no
`[[regenerate]]`. Derived from the descriptors; no new declaration, no new file. It gates gov's own
tree, so no adopter takes anything first and there is no ordering deadlock — but it reds this repo
until `TOOL-cMendedVintage-1` lands.

## TOOL-cMendedVintage-2 — gate-lint stops seeding into the memory tree

Three edits, and steps 2 and 3 MUST be one commit. (1) `tools/gate-lint/sh_hygiene.py` makes the
registry positional optional and DELETES the absent-registry refusal — it refuses because "a scan
with no declaration would report the whole population as new", which is byte-identically what the
shipped empty template produces and what that template documents as the correct first install.
(2) delete the `role = "seed"` rule and the template from `tools/gate-lint/kit.toml`, folding its
prose into the kit README. (3) drop the third argv element from the `[[gate_leg]]`. Dropping the seed
while the argv still names the path re-creates `apply` exit 1 at every adopter through
`silenced_legs`. Why not the alternatives: widening `check-memory-hygiene.sh`'s case list reaches an
adopter only on their next `update --kits memory-tree` and a FORKED checker never, and inCMS's is
forked; moving the registry under `tools/` is closed by the carried-prefix ban.

## DEPL-cMendedVintage-9 — no descriptor destination under `{memory_root}/project/`

Extend the bare-target arm at `govkit.py:1899`, where `_bare_have` is already in hand, with one
predicate: no descriptor destination may resolve under `{memory_root}/project/`, reason in the
message — check 3's case list is a closed name set gov cannot widen at an adopter. It fires on
exactly one entry today, which is how you see it RED before landing. Record the residue for the
runbook: at inCMS and NicoCares the receipt row still carries role `seed`, so the `report-reseed`
override at `:6443` rewrites its verdict and they get NO withdrawal order. They must be told.

## TOOL-cMendedVintage-3 — `check-wiring.sh`'s boundary walk cannot produce its empty prefix

Already open as the thirty-second dRetiredFork row, CONFIRMED with a lifted probe. The loop at
`tools/check-wiring.sh:30-37` appends `basename "$_p"` to `KIT_REL` BEFORE testing
`[ -e "$_parent/.git" ]`, so `$_p` itself is never tested as the repo root: a root install yields
`KIT_REL=<reponame>`, not the empty string that `:41` and `:370` assume. Every `${KIT_REL:+…}` rung
in the file rests on this, which is why it is its own unit and sequenced before the remedy unit.

## TOOL-cMendedVintage-4 — the three settings-merge remedies resolve at the install prefix

`tools/check-wiring.sh:353` resolves `SMERGE` at `tools/` or the repo root only, so at a `scripts/`
install every remedy it prints names a dead literal; the eight emission sites then carry a
`:-tools/settings-merge.py` tail. `tools/process-monitor/adopt-process-monitor.sh:219` hardcodes
`$ROOT/tools/settings-merge.py` while the same file derives correctly through `KIT_REL` two lines
above. `tools/memory-recall/adopt-memory-recall.sh:192` is the third carrier the adopter report
missed — same two-rung loop, plus a hardcoded `tools/` fallback, under a comment describing a fix the
code no longer has. `tools/unattended/adopt-unattended.sh:426` is the exemplar that gets it right.

## TOOL-cMendedVintage-5 — the carried predicate sees a `${VAR:-tools/…}` default

`tools/check-install-prefix.sh:400`, `re_ship`'s lead-exclusion class. Drop `-` ONLY
(`[^/{}[:alnum:]._-]` → `[^/{}[:alnum:]._]`), bump `PREDICATE_EPOCH`, run `--rebaseline`, then stage
a break and confirm RED. MEASURED before wiring, per §7: dropping `-` adds 11 occurrences and every
one is the real defect shape. Dropping `/` adds roughly 240 and is dominated by CORRECT `<gov>/tools/…`
spellings that name gov's own install — do not. Ordering is load-bearing: the rebaseline is one-shot
and blesses whatever is in the tree, so `TOOL-cMendedVintage-4` must land first or the dead literals
become invisible again. Lowering `check-wiring.sh`'s row also makes `--check` red with SLACK, so the
same commit re-runs `--write-ratchet` and commits that file.

## DEPL-cMendedVintage-10 — `update --write` writes the `.gitattributes` block, with the renormalize

`govkit.py:6386`, after the `pins-moved` verdict: the same four calls `apply` makes at `:4620`, plus
`apply`'s renormalize at `:4976` — the whole-diff intersect, refuse-if-dirty, then `git add
--renormalize`. Skipping the renormalize is not cosmetic: a newly-pinned path whose index blob is
CRLF stays CRLF and the only verb that fixes it is the destructive one, so the class stays open. Add
no second dirty check — the write preconditions at `:6009` already cover a receipt-claimed path. ADD
THE ROW TO THE PRE-WRITE SNAPSHOT or a rolling-back run leaves gov's new block staged. Delete the
"Re-run `govkit apply`" sentence at `:6675`: `apply` overwrites engine bytes unconditionally and
ignores `deploy["inert"]` entirely, so the printed remedy destroys exactly the local forks update's
unattributed skip declined to touch. This flips two shipped selftest arms BY NAME
(`selftest.py:1739` and `:1747`); update them, do not paper over them.

## DEPL-cMendedVintage-11 — `cmd_check` grades the attributes row's block

`govkit.py:3164`, `if row.get("role") not in ("merged", "attributes")`. The attributes row already
carries `block_id`, `marker_style` and `block_sha256`, and `lf_pin_block` returns marker-inclusive
text hashed at `:4629`, so the existing extractor grades it unmodified. ON ITS OWN THIS REDS EVERY
ADOPTER WHOSE PINS MOVED and leaves them only the destructive remedy — it ships in the same release
as `DEPL-cMendedVintage-10` and never before.

## DEPL-cMendedVintage-12 — `apply`'s CONFIGURE honours `deploy["inert"]`

`govkit.py:4889` runs each kit's `[adopt].argv` without consulting `deploy["inert"]`, while the
re-render block at `:7389` does. The only reader of that key in 9005 lines is the latter. Three
lines. Independent of every other unit here and worth its own spec because it is a posture the
target declared being ignored by the install verb.

## DEPL-cMendedVintage-13 — `update --write` emits gate legs

The owner ruled this into the run. The emission loops are `apply`'s at `:5122` and `:5278` and
`adopt`'s at `:8371`; `_cmd_update` spans `:5939-7994` and has none, so every new `[[gate_leg]]` gov
ships reaches an adopter only when they re-run `apply` — the residual cap on "fully automatic". It
reuses `DEPL-cMendedVintage-10`'s write stage and is sequenced after it for that reason. Its risk is
the same shape: a new effect on a verb that had none, so the spec owes an explicit §9 on what a
half-written leg manifest does and how it is recovered.

## DEPL-cMendedVintage-14 — stale conflict orders are reaped, and keyed on the full path

Collect each order path as it is written (`govkit.py:6891`, `:7021`), then at the end of an UNSCOPED
write run unlink every `update-conflict-*.md` this run did not write. Key the filename on the full
path rather than the basename at `:6891`, `:6975` AND `:7021` — all three; the basename spelling
silently collapses two conflicts over `kit.toml` into one order, and the withdrawn writer has the
same collision. DO NOT add a counting-threshold refusal: it converts a backlog into a wedge, which is
recorded as the reason `report` replaced `refuse` for the forked role. The reap IS the gate — one
fixture: conflict a row, resolve it, re-run, assert the order is gone. That arm cannot exist today
because nothing removes one.

## TOOL-cMendedVintage-6 — `check-receipt.sh`, the receipt-sync leg

The one genuinely new shipped file, ~20 lines: read `.governance/install.json` and for every row with
`role` absent or `"engine"`, compare the file's sha256 to `row["sha256"]` and fail on a missing file
— `cmd_check`'s integrity arm minus the descriptor and provenance halves that need a gov checkout.
Scope to `engine` exactly as `cmd_check` does: `seed` rows are deliberately exempt and a `merged`
row's `sha256` is the whole merged file. Do NOT use `sha256sum -c install.sums`: that sidecar is
written from every row carrying `sha256`, including seed rows stamped with gov's hash for a file the
target owns. THREE edits, not two — the script, a `[[gate_leg]]` in `tools/run-gates/kit.toml`, and a
matching row in `tools/gate-legs.json`, because `govkit selfcheck` fails any descriptor leg not also
on gov's bar. That third edit means the leg runs HERE, where there is no `install.json`, so it must
print an explicit SKIP and exit 0 — written as a skip, never as a pass.

## TOOL-cMendedVintage-7 — the leg reports `unattributed` rows

One extra loop in `check-receipt.sh` over `f.get("evidence") == "unattributed"`. It goes there and
not into `cmd_check`, which needs the gov checkout and is invoked automatically by nothing, so a
count there never reaches an adopter's bar. BLOCKED ON `DEPL-cMendedVintage-4`: do not red an adopter
for a state whose printed remedy is a no-op. Land as a note first, a failure one release later.

## TOOL-cMendedVintage-8 — process-monitor's empty-live-scope arm gets its own code

`tools/process-monitor/scope.py:271` exits 1 when the declared roots hold no live process AT THAT
MOMENT, and `adopt-process-monitor.sh:228` treats that as a failure — so the kit's `[check]` is
non-deterministic and `update` can roll it back for the time of day. Give that case a distinct code,
keep 1 for `ScopeRefused`/`CensusRefused`, and have the adopter treat the new code as a
self-announcing skip. A single-line demotion of the exit status would also demote the conf-parse
refusal, which must survive. No shipped arm reds: the adopter's own test copies only the adopter, so
the `scope.py` branch never runs there. NO GATE IS CHEAP HERE — a check arm whose verdict depends on
machine state is caught by review, not by a predicate over descriptors. Say that rather than
inventing one.
