# Wave 1 — lens 4: inefficient code on paths that actually run

**Serves:** research TOOL-aScouredKit-1

## Verdict: CLEAN WITH FIXES


Subject: the whole repo at `093730e40355d6a04300966f791f2634379e8b45`.
Node `a`, 2026-08-30. **The box was contended throughout** — several other wave-1 lens agents were
running against the same tree, and one `bash tools/memory-tree/check-memory-hygiene.sh` never
returned inside 420 s. So **every absolute second below is a reading of a busy machine and I do not
claim otherwise.** Everything load-bearing is stated as a RATIO taken from an interleaved
old/new pair inside ONE shell invocation, which is what `memory/gotchas/process-creation-is-the-suite-cost.md`
prescribes for exactly this reason, plus a SPAWN COUNT, which that same record says is exact and
load-independent.

## What this lens found, in one line

Three unguarded merge-bar legs — all three also SHIPPED to adopters as `[[gate_leg]]` rows — are
each dominated by one grep spawn per file in a `while read` loop. That is the repo's own catalogued
class `process-creation-is-the-suite-cost`, whose fix paragraph names this exact shape
("loops that run a command per (item, file) pair when the file half does not depend on the item").
The class is catalogued; these three instances are not, and none of them carries the
"batching was tried and rejected" note that `tools/check-agent-cap-restatement.sh:100-106` carries
for the same shape — so they are omissions, not decisions.

## What this lens deliberately did NOT report, and why

- **The per-leg ceilings are not vacuous and I withdraw that line of attack.** I first measured
  ceiling-to-cost ratios of 28x–1230x across all 86 legs and was about to call the cost gate
  unfireable. Commit `ee0e7547` settles it: the ceiling is a HANG bound, explicitly not a cost
  budget, sized 10x with a 300 s floor after twelve of forty legs timed out on ambient load under
  the previous 3x/60 s sizing. The commit body cites the same gotcha at me. Refuted before writing.
- **`tools/check-agent-cap-restatement.sh:112`** runs one `grep -HIniE` per markdown file (225
  traced executions). Its header argues the batched form and names three defects it produced. That
  is a recorded decision, not drift.
- **Ceilings absent from all 68 shipped `[[gate_leg]]` blocks** while gov's own manifest declares
  one on all 86 — tracked as `TOOL-aBoundedCeiling-13`.
- **`run-gates canary` at 1319.9 s**, the single most expensive leg on record — tracked as
  `TOOL-aScannedThrottle-5`, which already measured that deleting it entirely moves the bar 0.0%.
- **`tools/memory-tree/check-memory-hygiene.sh`** — its own comments at `:236` and `:517` show the
  per-file fork loops were already collapsed into single `awk`/`xargs` passes. I could not time it
  to completion under load and make no claim about it.
- The memory-recall query path builds two FTS5 indexes behind a digest-keyed cache. Nothing to say.

## Method

```bash
# the ledger, for what each leg actually costs
sort -t$'\t' -k2 -rn "$(git rev-parse --git-common-dir)/gate-ledger.tsv"

# which legs run on a DEFAULT bar (subject != kit, chunk != selftests): 40 of 86,
# 565.9 leg-seconds measured
python - <<'EOF'  # (join gate-legs.json against gate-ledger.tsv)

# spawn counts — exact and load-independent, per the gotcha
PS4='+ ${LINENO} ' bash -x <leg> >/dev/null 2>trace; awk '{print $2}' trace | sort -n | uniq -c | sort -rn
```

The default bar is 40 legs / 565.9 measured leg-seconds. The three legs below are 60.7 s of that
(10.7%) by the ledger's own numbers, and 100% of that 60.7 s is removable.

---

## F1 — `tools/memory-tree/check-method-carriers.sh:59` — one grep spawn per TRACKED FILE

```bash
carriers=$(git ls-files | while IFS= read -r f; do
  case "$f" in ... esac
  grep -lF "$DOC" "$f" 2>/dev/null      # <- line 59, once per tracked file
done)
```

`git ls-files` is **1156 files** in gov. The trace confirms the loop body runs for every one of
them (line 60 traced 2316 times = 2 per iteration; line 61 traced 1156 times).

Three interleaved runs of the loop against a batched equivalent, in one shell invocation each:

| run | per-file loop | batched `xargs -0 grep -lF ... -- /dev/null` | ratio |
|-----|---------------|-----------------------------------------------|-------|
| 1   | 17.81 s       | 0.94 s                                        | 19x   |
| 2   | 19.89 s       | 0.88 s                                        | 22x   |
| 3   | 18.89 s       | 0.53 s                                        | 36x   |

**Output byte-identical in all three runs** — the same 14 carriers. Ledger cost of the leg on a
quiet node: 8.6 s (`method carriers (every pointer declared)`), i.e. the loop IS the leg.

Why this one matters most: **the population is the adopter's WHOLE REPOSITORY**, not their memory
tree. The exclusions (`$M/*`, the template, `*.test.sh`, the leg itself) are applied inside the
loop, so every tracked file in a target repo costs one process creation whatever it is. gov is a
1156-file repo; a 20 000-file adopter pays ~17x gov's spawn count for a check that returns a
14-element list. This leg ships at `tools/memory-tree/kit.toml:147-151` with `subject = "repo"` and
`guard = []`, so it runs on every bar in every adopting tree.

**Fix:** move the `case` filter into the producer and hand the survivors to one `grep`:

```bash
carriers=$(git ls-files -z | while IFS= read -r -d '' f; do
  case "$f" in "$M"/*|"$KITREL"/BUILD-METHOD.template.md|"$KITREL"/check-method-carriers.sh|*.test.sh) continue ;; esac
  printf '%s\0' "$f"
done | xargs -0 grep -lF "$DOC" -- /dev/null 2>/dev/null)
```

`-z`/`-0` keeps the space-in-filename property the current `while read` has and the file's own
comment at `:73-76` insists on. The trailing `/dev/null` forces grep to prefix filenames even when
`xargs` hands it a one-file batch — without it a split batch of one silently drops the filename,
which is the defect `check-agent-cap-restatement.sh` names.

Not in `memory/backlog/TOOL.md` (zero hits for `check-method-carriers`).

---

## F2 — `tools/unattended/check-playbook.sh:162` — 941 markdown files opened to find ONE playbook

```bash
while IFS= read -r f; do
  case "$f" in *.md) ;; *) continue ;; esac
  case "$f" in */PLAYBOOK-TEMPLATE.template.md|*/PLAYBOOK-TEMPLATE.md) continue ;; esac
  if grep -q '^step_selector[[:space:]]*=' "$f" 2>/dev/null && grep -q '^```toml' "$f" 2>/dev/null; then
```

Line 162 traced **941 times**. Two interleaved runs against a two-`grep` batched equivalent:

| run | discovery loop | batched (2 greps + `comm`) | ratio |
|-----|----------------|-----------------------------|-------|
| 1   | 30.73 s        | 1.36 s                      | 23x   |
| 2   | 29.01 s        | 1.26 s                      | 23x   |

Both forms find **the same single playbook**. The ledger records the whole leg
(`playbook validity gate`) at 32.2 s on a quiet node, so this discovery loop is essentially the
entire leg: ~30 s of process creation to identify a one-element population, of which the second
`grep '^```toml'` fires only on the 1 file that passed the first, so ~941 of the ~942 spawns are
the first predicate alone.

This is the **third most expensive leg on the default bar** and it carries no guard
(`subject = "repo"`, no `guard` key in `tools/gate-legs.json`). It ships at
`tools/unattended/kit.toml:96`.

**Fix:** two batched greps and an intersection, filtering the template out of the candidate list
first (verified to produce the identical single-element set):

```bash
cand=$(git -c core.quotePath=false ls-files -z -- '*.md' | ...)   # drop the two TEMPLATE spellings
sel=$(printf '%s' "$cand" | xargs -0 grep -lE '^step_selector[[:space:]]*=' -- /dev/null 2>/dev/null | LC_ALL=C sort)
tml=$(printf '%s' "$cand" | xargs -0 grep -l   '^```toml'                   -- /dev/null 2>/dev/null | LC_ALL=C sort)
PLAYBOOKS=$(comm -12 <(printf '%s\n' "$sel") <(printf '%s\n' "$tml"))
```

The `POP`/liveness assertion at `:170` and the `COUNTS_FOR` override at `:172-176` read `$PLAYBOOKS`
and are untouched by this.

Not tracked. The three `check-playbook` rows in `memory/backlog/TOOL.md` are
`TOOL-dScriptedRepeat-13` (bypass-flag guard, CLOSED), `TOOL-dScrubbedConduit-2` (hardcoded
`tools/` in the fixture) and `TOOL-aGradedDoorway-2` (fixture prefixes) — none is about cost.

---

## F3 — `tools/check-install-prefix.sh:67` and `:183` — 354 grep spawns, 96% of the leg

Two independent per-file loops in one script.

**Arm 1, line 67** — one `grep -nE` per shipped file, 170 files (line 69 traced 170 times):

```
per-file loop: 4.57 s      batched (xargs grep -nE | awk -F: '{print $1":"$2}'): 0.14 s     33x
hits identical: YES (12 hits both ways)
```

**Arm 2, line 183** inside `carried_rows()` — one `grep -cE` per carried-population member, 184
members (lines 180-184 traced 372/184/184/445/291 times):

```
per-file loop: 10.42 s     batched (xargs grep -cE ... -- /dev/null | awk): 0.49 s          21x
identical: YES (107 rows both ways — the exact row set tools/install-prefix-carried.txt tracks)
```

Together **15.0 s of a leg the ledger records at 19.9 s**, collapsing to 0.63 s, with the ratchet
file's 107 rows reproduced byte for byte. `install-prefix (shipped surface)` is `subject = "repo"`
with `guard = []` and ships at `tools/govkit/entries/check-install-prefix.kit.toml:52-56`.

Arm 1's output shape is already what batched grep emits natively: `grep -nE PAT -- f1 f2 ...`
prints `path:lineno:text`, and the loop is hand-reassembling exactly that from a per-file run.

**Secondary, same file:** `carried_population()` (`:131`) is invoked twice on the `--check` path —
once from `carried_live()` at `:222` and again from `carried_rows()` at `:225`. Each call is a
fresh interpreter start plus a full `govkit.read_descriptors` + `resolve_entry` walk of the whole
registry. **Measured: 0.86 s per call.** `carried_live` only needs the COUNT of the population that
`carried_rows` is about to walk, so one of the two calls is duplicated work. Capture the population
once into a variable and derive both the liveness count and the rows from it. (The liveness
assertion's semantics — that the count is over the POPULATION and never over the hit set, argued at
`:157-165` — are preserved by this; it is the same list.)

---

## F4 — `TOOL-aCollapsedScan-5`'s recorded premise is false at this sha

`memory/backlog/TOOL.md:244`, status OPEN:

> no leg in `tools/gate-legs.json` declares a wall-clock ceiling, and the manifest has no field for
> one across its 85 legs

All **86** legs at `093730e4` declare a `ceiling`. The row's own named candidate — "a `ceiling` key
in `tools/gate-legs.json` that `run-gates.sh` grades against `<git-dir>/gate-ledger.tsv`" — landed
in `db361653` and was re-sized in `ee0e7547`.

This is not a wholly stale row and should not be closed blind. Its motivating incident is a COST
regression (check 30 adding ~235 s unnoticed for eight days), and `ee0e7547` says in as many words
that the landed ceilings are a hang bound and "do not pretend to police cost". So the ASK survives
and the FACT does not — which is the worst combination for a reader who greps `ceiling`, finds a
row saying no ceilings exist, and rebuilds something that is already there. Rewrite the lead
sentence to state what landed and scope the row to the cost half alone.

---

## Two smaller observations, recorded without filing

- `<git-dir>/gate-ledger.tsv` carries **91 rows against 86 manifest legs**. Six are orphans the
  carry-forward `awk` at `run-gates.sh:1335` will preserve forever: `marker contract` (renamed to
  `marker contracts`), the four `unattended` legs removed by the 2026-08-23 owner ruling, and a row
  literally named **`t`** at 1.237 s. They are dispatch-hint noise only — the python side keys the
  hint on manifest names, so an orphan can never be scheduled — but `profile_bar.py`'s own header
  already calls this file out as something people misread as a profile. One manifest leg,
  `tier2-review self-test`, has no ledger row and is therefore scheduled last on a cold hint.
- The default bar is 40 of 86 legs and 565.9 measured leg-seconds, of which `govkit acceptance
  matrix` (251.4 s, guarded) and `unattended kit gate` (141.5 s, unguarded) are 69%. With a width-8
  pool the wall clock is floor-bound by the longest leg, so F1–F3 buy leg-seconds and machine load
  rather than much wall clock **in gov**. Their teeth are in the adopter trees, where F1's cost is
  linear in the whole repository.
