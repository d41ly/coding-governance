# TOOL-aRepatriatedFork-6 — unattended set_fact refuses a value that can forge a second fact

**Status:** SPECCED · rev-1 · 2026-09-23 · node a · Tier-2 · base a7c78ad2 · streams tooling · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-23-prompt-TOOL-aRepatriatedFork-6-build-brief.md](../prompts/2026-09-23-prompt-TOOL-aRepatriatedFork-6-build-brief.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

Close a security hole in the unattended driver. `set_fact` in `tools/unattended/unattended.sh` writes
a caller's value into `RUN.md` with no guard, and `--attest --value` hands it agent-supplied text, so
an agent can write a forged `phase: LANDED` line that every reader takes as the run's phase. nc
guards against a literal newline; this unit takes that guard, closes the escape-sequence path nc's
guard misses, and gates the class at the leg.

## 2. Scope (IN)

- **S1** — `set_fact` refuses a key or value carrying a line feed or a carriage return, with `fail 17`
  and a message naming the key, before the file is touched. Observed by AC1 and AC4.
- **S2** — `set_fact` hands the key and value to `awk` through the environment and reads them with
  `ENVIRON`, never through `awk -v`, so a backslash sequence in a value is stored as written. This is
  the path nc's guard does not close. Observed by AC2.
- **S3** — The check leg refuses a run-state file whose `## Run facts` section carries one key twice
  with two DIFFERENT values, because the driver's readers take the first match and a second,
  different line is a fact nothing wrote. Observed by AC5 and AC6.
- **S4** — Every verb that writes a caller-supplied string is driven with both hostile forms, a
  literal newline and a backslash-n, and each is asserted to leave `phase` unchanged. The verb set is
  the class, not `--attest` alone. Observed by AC3.
- **S5** — The DoD refusal at `tools/unattended/unattended.sh:3674-3683` prints the `--override`
  spelling for an item outside `DOD_NO_OVERRIDE` and `gates-green`, and the comment at `:3988-3989`
  that claims fail 13 already prints it becomes true. This is the second half of nc carve-out 21.
  Observed by AC7.
- **S6** — `KIT_UNATTENDED_VERSION` moves in the four carriers `tools/check-kit-versions.sh` pairs.
  Observed by AC8.

## 3. Non-goals (OUT)

- A run that edits `RUN.md` by hand. `TOOL-aBoundedCeiling-11` records one that did, and it stays
  open. S3 catches the duplicate-line form of a hand edit as a side effect; a hand edit that REPLACES
  the real line is not detectable from the file and is not claimed.
- The protocol's own residuals: a run that edits this kit, shims its tools or skips the hook layer
  (`tools/unattended/PROTOCOL.template.md:540-543`).
- Sibling writers. `park()` at `tools/unattended/unattended.sh:4634-4643` and the piece and set
  record writers use `printf '%s'`, which interprets no escape in its argument, and each already
  refuses a newline (`:1322`, `:4805`, `:4907`, `:4965`, `:5028`, `:5148`, `:5213`, `:5346`). S4
  drives them anyway, because the class is the verb set.

### Edges

- **hands-off** external — the hand-edit route to a terminal phase, `TOOL-aBoundedCeiling-11`, which this unit narrows and does not close

## 4. Design

### Threat model

**Actor.** The agent carrying an unattended run. The protocol trusts it to author exactly the
agent-checked DoD items, through `--attest`, and nothing else (`tools/unattended/unattended.sh:4663-4683`).

**Capability.** It chooses the argv of any verb, `--attest <slug> --item <item> --value <text>` and
`--resume --keepalive-id <id>` included.

**What it can forge today.** Any `## Run facts` key, `phase` above all. `set_fact`'s insert branch
places a new key directly under the heading (`:3118`), above every existing fact, and the three
readers return the FIRST match: `fact()` at `:738-748`, and `fact_of`/`phase_of` in the leg at
`tools/unattended/check-unattended.sh:773-783`. A forged `phase: LANDED` makes
`refuse_if_terminal` (`:1790`) refuse every later verb, lets the stop-guard allow the session to end
(`tools/unattended/stop-guard.js:137`), and drops the run from the leg's open-run checks, which skip
`LANDED` at `check-unattended.sh:2163` and `:2321`. Adding forged `witness:` and `landed-anchor:`
lines in the same value satisfies check 15's shape and ancestry halves with any sha already on the
default branch. `--landed`, which re-observes the remote and requires the lander marker, is never
called.

**Preconditions.** A live run-state file and one agent-checked DoD item, which every run has.

**Why this is not the same as editing `RUN.md` by hand.** The protocol's model is that an
unauthorized landing must be a visibly deliberate act (`tools/unattended/PROTOCOL.template.md:524-525`).
A hand edit shows in the diff as a phase line changed by no verb. The attest route is laundered: the
driver prints `unattended: attested — <key>: yes` and stages the file as a routine attestation
(`:4679-4680`).

### The exploit path, reproduced

`set_fact` at `tools/unattended/unattended.sh:3113-3125` writes with
`awk -v k="$k" -v v="$v"`. POSIX `awk -v` processes escape sequences in the assigned value, so the
two characters backslash and `n` become a line feed. A literal line feed passes through as one too.

Reproduced 2026-09-23 by extracting `set_fact` and `fact` from each tree into a scratch script under
the session scratchpad and writing an `some-item` fact into a fixture holding `phase: RUNNING`.

| tree | value | set_fact rc | `fact phase` afterwards |
|---|---|---|---|
| gov a7c78ad2 | `yes`, a literal line feed, `phase: LANDED` | 0 | `LANDED` |
| gov a7c78ad2 | `yes\nphase: LANDED`, one argv line | 0 | `LANDED` |
| nc f69e2ffb | literal line feed form | 1, `fail 17` | `RUNNING` |
| nc f69e2ffb | `yes\nphase: LANDED`, one argv line | 0 | `LANDED` |

The fixture after the gov escape case reads `some-item: yes`, `phase: LANDED`, `phase: RUNNING`, in
that order. nc's guard counts line feeds in the SHELL string (`scripts/unattended/unattended.sh:3138`
at nc), which holds none in the escape case; awk manufactures the line feed after the check. inCMS
runs gov's unguarded `set_fact` at `scripts/unattended/unattended.sh:3134` and has the same exposure.

### The fix

```sh
set_fact() { # file · key · value
  local f="$1" k="$2" v="$3" tmp
  if [ "$(printf '%s' "$k$v" | wc -l)" -ne 0 ]; then fail 17 "…newline…: $k in $f"; return 1; fi
  case "$k$v" in *$'\r'*) fail 17 "…carriage return…: $k in $f"; return 1 ;; esac
  tmp=$(mktemp) || return 2
  if grep -q "^$k: " "$f"; then
    K="$k" V="$v" awk '{ if (index($0, ENVIRON["K"] ": ") == 1) print ENVIRON["K"] ": " ENVIRON["V"]; else print }' "$f" > "$tmp"
  …
```

The `wc -l` form is the one every sibling uses and the one nc settled on after a `case` pattern built
from a command substitution matched everything (`scripts/unattended/unattended.sh:3134-3137` at nc).
The carriage-return test uses `$'\r'`, which is ANSI-C quoting and not a substitution. It is refused
because `fact()` strips a trailing carriage return (`:742`), so this kit treats the byte as a line end.

`ENVIRON` is chosen over escaping backslashes because it has no escape grammar to get wrong, and a
value keeps its bytes. `K` and `V` are set for the one `awk` invocation only.

### The class gate, S3

The leg reads each tracked `RUN*.md`, takes the `## Run facts` section up to the next `## ` heading,
and refuses a key that appears twice with different values, naming the file, the key and both values.
A same-value repeat is not a forgery, because the first match gives the same answer.

Run over the real trees before wiring, as the charter requires. PINNED, measured 2026-09-23.

| tree | run-state files | hits, any repeat | hits, different values |
|---|---|---|---|
| gov | 66 | 1, `memory/builds/dCarriedReceipt/RUN.md` `landed-anchor` | 0 |
| inCMS | 12 | 0 | 0 |
| nc | 16 | 0 | 0 |

The one near-miss is the record `TOOL-aBoundedCeiling-9` repaired by hand, which carries
`landed-anchor: remote` twice (`memory/builds/dCarriedReceipt/RUN.md:15`, `:22`). The
different-values rule passes it, which is why the rule is not "any repeat".

### Inventory

One `fail 17` message added in `unattended.sh`, beside the existing `cannot record a run fact` branch.
One leg check in `check-unattended.sh`, numbered by the builder as the next free check. Two shell
names, `K` and `V`, scoped to a single command. No new verb, key or conf value.

### Migration

| adopter | record | disposition |
|---|---|---|
| nc | `nc carve-out 21/24`, the guard at `scripts/unattended/unattended.sh:3120-3141` | deleted; gov bytes are a superset, and nc's guard alone is bypassable |
| nc | `nc carve-out 21/24`, the remedy at `scripts/unattended/unattended.sh:3712-3731` | deleted; gov bytes after S5 |
| nc | census denominator, `scripts/check-nc-wiring.sh:260-269` | falls by one in the same commit |
| inCMS | `KIT_UNATTENDED_DELTA` on `scripts/unattended/unattended.sh` (`kits.json:377-381`) | unchanged in kind; it stays a pointer repath, and the next re-take carries the guard |

### Rollout

One gov commit with the version bump; adopters take it on `govkit update`. A run already live when
the bytes land keeps working: S1 refuses only values no honest verb writes, and S3 passes every
tracked run-state file in all three trees.

### Files touched (estimate)

- `tools/unattended/unattended.sh`
- `tools/unattended/check-unattended.sh`
- `tools/unattended/unattended.test.sh`
- `tools/unattended/check-unattended.test.sh`
- `tools/unattended/check-pass-order.sh`, `tools/unattended/check-brief-recorded.sh` (version markers)
- `tools/unattended/PROTOCOL.template.md` (the check-list entry for S3, and the version marker)

### Alternatives rejected

- **nc's guard alone.** Measured above: the escape form forges at nc.
- **Refuse a backslash in any value.** Honest values carry them, Windows paths first among them, and
  `ENVIRON` makes the byte harmless.
- **Make `fact()` take the LAST match.** It moves which line wins and changes nothing about a line
  nothing wrote; an insert-branch forgery would still be read by whichever reader keeps first-match.

## 5. Production-readiness checklist

- security — this unit. Threat model and residuals are in §4 and §3.
- perf / scale — one `wc -l` pipeline per fact write; S3 is one `awk` pass per run-state file, over
  66 files at gov today.
- error / empty / loading states — a refused fact leaves `RUN.md` byte-identical, which AC4 pins.
- observability — both refusals name the key and the file; S3 names both values.
- risks — a verb that legitimately stored a multi-line value would now refuse. None does: every
  reader is line-wise, so such a value was already unreadable.
- testing — S4's verb-by-form matrix in `tools/unattended/unattended.test.sh`, and S3's arms in
  `tools/unattended/check-unattended.test.sh`; each observed red against a7c78ad2 first.
- migration — none for data. S3 is green on every tracked run-state file in all three trees.
- user docs — the protocol's check list names the new leg check.

## 6. Acceptance criteria

- **AC1** — When `unattended.sh --attest <slug> --item <agent item> --value` is given `yes`, a
  literal line feed and `phase: LANDED`, `tools/unattended/unattended.sh` exits non-zero with the
  new `fail 17` message and `phase` still reads the pre-call value.
  Red when: the value is written, as at a7c78ad2.
- **AC2** — When the same verb is given the single-line value `yes\nphase: LANDED`, the file holds
  exactly one new line, `<key>: yes\nphase: LANDED` with the backslash intact, and `phase` still
  reads the pre-call value.
  Red when: `awk -v` turns the escape into a line feed, which is the path nc's guard misses.
- **AC3** — When the S4 matrix drives every value-writing verb in `tools/unattended/unattended.sh`,
  `--attest`, `--resume --keepalive-id`, `--park`, `--propose`, `--brief`, `--record-piece`,
  `--record-set`, `--rescope` and `--preflight --waive`, with both hostile forms, no case changes
  `phase`.
  Red when: any verb stores either form as a second line.
- **AC4** — When a refused fact write returns, `git hash-object` of the run-state file equals its
  pre-call hash.
  Red when: the guard runs after the file is rewritten.
- **AC5** — When a fixture run-state file carries `phase: RUNNING` and a second `phase: LANDED` under
  `## Run facts`, `tools/unattended/check-unattended.sh` exits non-zero naming the file, `phase` and
  both values.
  Red when: the leg reads only the first match and passes.
- **AC6** — When `tools/unattended/check-unattended.sh` runs over gov's tree, the new check reports
  66 run-state files graded and no hit, `memory/builds/dCarriedReceipt/RUN.md` included.
  Red when: the check fires on a same-value repeat, or grades nothing.
  figure: PINNED at 66, measured 2026-09-23; the check prints the count it derives.
- **AC7** — When `--close` refuses a machine-checked item outside `DOD_NO_OVERRIDE`,
  `tools/unattended/unattended.sh` prints `--close <slug> --override <item> --reason`; for
  `gates-green` it does not.
  Red when: the refusal still prints no remedy while the comment claims it does.
- **AC8** — After the bump, `bash tools/check-kit-versions.sh` exits `0`, and with one bumped carrier
  reverted it exits non-zero naming it.
  Red when: a carrier was missed.

## 7. Gates

`unattended kit gate` · `unattended skill wiring` · `harness arms (fail branches armed or pinned)` · `kit version markers`

New arm: `tools/unattended/unattended.test.sh` · the S4 verb-by-form matrix, run first against the a7c78ad2 driver to observe `phase` read `LANDED` · none
New arm: `tools/unattended/check-unattended.test.sh` · a fixture with two different `phase` values under `## Run facts`, observed passing against the a7c78ad2 leg first · none

## 8. Open questions

- **F1 — should S3 also refuse a same-value repeat for keys the driver owns exclusively, `phase`
  above all?** It would catch a forgery that happens to repeat the real value, which forges nothing.
  Recommendation: no; the different-values rule is the one that separates a forgery from a repair.
  RESOLVED (owner, 2026-09-23): no, as recommended.
- **F2 — should `--attest` refuse a value outside a closed set, `yes` and a reason sentence?** It
  narrows what an agent can author at all. Recommendation: no; S1 and S2 remove the forging power,
  and the value is prose by design.
  RESOLVED (owner, 2026-09-23): no, as recommended.

## 9. Revision log

- rev-1 · 2026-09-23 · initial draft, measured against gov a7c78ad2, nc f69e2ffb and inCMS 1bc57da27,
  with the forgery reproduced on all three from extracted functions under the session scratchpad.

## 10. Reuse audit

The seam is the newline refusal every sibling writer already carries, for example
`tools/unattended/unattended.sh:4805-4808` in the review verb, and nc's port of it into `set_fact`.
S2 adds the one thing none of them needs, because they write through `printf '%s'`.
`tools/codebase-map/reuse_lookup.py` scans no `.sh` and ranked unrelated Python `run` and `write`
symbols, so no existing seam fits beyond the sibling guard.

Recall terms used: `set_fact attest newline forge phase LANDED run-state RUN.md write-guard record_piece sibling`.
