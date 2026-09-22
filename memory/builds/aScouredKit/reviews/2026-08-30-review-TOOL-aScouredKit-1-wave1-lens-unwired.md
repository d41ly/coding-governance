# Wave 1 — LENS 2: unwired functionality (built, shipped, never reachable)

**Serves:** research TOOL-aScouredKit-1

## Verdict: CLEAN WITH FIXES


Subject: whole repo at `093730e40355d6a04300966f791f2634379e8b45`.
Lens slug: `unwired`. Date: 2026-08-30.

---

## Method, and what it cleared

This repo is unusually well-closed on its DECLARED surfaces, so most of the budget went into
proving the obvious candidates *clean* before finding the real gap. Recording the negatives, because
a later reviewer should not repeat them.

Seven registration surfaces were enumerated per the lens brief and checked in both directions:

| Surface | Check | Result |
|---|---|---|
| `tools/gate-legs.json` (86 legs) | every leg claimed by a descriptor `[[gate_leg]]` or a registry `[[exempt_leg]]` | **closed: 68 + 18 = 86, zero unclaimed, zero stale exemptions, zero double-claimed** |
| `tools/*/kit.toml` + `tools/govkit/entries/*.kit.toml` | every `[check]`/`[adopt]` argv path resolves after `{kit}`/`{prefix}` substitution | **all resolve** |
| `tools/govkit/registry.toml` | surface assertion, both directions | **green: 58 tracked paths, 25 entries, 17 exemptions, 0 unclaimed** |
| `.claude/settings.json` hooks | all three named hook files exist and are tracked | **all present** (`agent-cap.js`, `scratch-guard.js`, `recall-opened.js`) |
| Rendered Skills | each of the 4 `.claude/skills/*/SKILL.md` has a wiring gate leg | **all four covered** — `memory-recall skill wiring`, `unattended skill wiring`, `lexicon wiring`, `drift-audit wiring` |
| Charter placeholders | `[[placeholder]]` rows ↔ `{{TOKEN}}` in the template | **28 / 28 both directions** |
| Charter fences | every `kit:` fence names a registry entry; every `when:` fence names a `[[block]]` | **valid** |

Also cleared, each a candidate I expected to fire:

- **Rendered artifacts carry no unsubstituted tokens.** All four `SKILL.md` files plus
  `memory/HYGIENE.md`, `memory/TEMPLATE-SPEC.md`, `memory/guides/BUILD-METHOD.md`,
  `UNATTENDED-PROTOCOL.md` and `REVIEW-PROTOCOL.md` scanned for `{TOKEN}` / `{{TOKEN}}`: clean.
- **`tools/manifest-check.sh`** in `WIRE-INTO-PROJECT.md:416` and `:455` is *not* a dead path. It is
  the ADOPTER-side destination: `tools/govkit/entries/kickoff-manifest.kit.toml` declares
  `to = "{prefix}/manifest-check.sh"`, which resolves to exactly that under the default prefix. The
  runbook is correct for its audience. False positive, discarded.
- **`render_playbook.py --charter`** has no external caller but carries `default='AGENTS.md'` and is
  read at `:559`. A defaulted escape hatch, not dead. Discarded.
- **`tools/govkit/check_runbook_parity.py`** — zero callers, absent from `gate-legs.json`, exits 1
  with 18 problems. **Already tracked** as `TOOL-dScaffoldedMirror-15` (DEFERRED, verified
  2026-08-24, same 18). Confirmed still live and still 18; not re-reported as new.
- **`GATE_TURNSTILE_HELD`** (`run-gates.sh:697`) is exported as a "LINEAGE MARKER for any future
  nested caller" and has exactly one occurrence tree-wide — nothing reads it, which is the textbook
  computed→serialized→never-read shape. **Already written up** in
  `memory/builds/aBoundedCeiling/reviews/2026-08-27-review-TOOL-aBoundedCeiling-1-diff-review-round2.md:37`,
  including the live nesting deadlock it fails to prevent. Not re-reported.

Backlogs read in full before writing: `memory/backlog/TOOL.md` (274 lines), `DEPL.md`, `PLAY.md`,
`KICK.md`. Every finding below was grepped against TOOL.md + DEPL.md: `requires_config_first` 0 hits,
`placeholders =` 0, `drop_blocks` 0, `cross-os` 0, `TOOLCHAIN_NOTES` 0, `unknown key` 0,
`descriptor key` 0. The three `delegate` hits are unrelated prose.

---

## The gap the closed surfaces hide

Everything above validates the *values* inside declarations. **Nothing validates the KEYS.** The kit
descriptor language — 25 entries, the thing that decides what ships into every adopter — has no
allowlist, so a key that no reader consumes is silently inert and a typo of a real key is
indistinguishable from a deliberate declaration.

This is not a hypothesis. Four inert keys already ship, one of them already drifted.

And the repo has already written the rule down, for a two-key file, twelve hundred lines away:

> `tools/run-gates/run-gates.sh:288`
> `# A silently ignored knob is a knob the operator believes they set, so an unknown key REFUSES.`

`gate-profiles.txt` has two legal knobs and `prof_die`s on a third. `kit.toml` has hundreds of keys
across 25 descriptors and refuses nothing.

---

## F1 — `govkit selfcheck` is green on a typo'd descriptor key; a typo'd `guard` silently ships an unguarded leg to every adopter, and the diagnostic built to announce that cannot fire

**Severity: high** · `tools/govkit/govkit.py:4366`

### Reproduced

Baseline: `python tools/govkit/govkit.py selfcheck` → exit 0, `surface 58 tracked path(s) · 25
entr(y|ies) · 17 exemption(s) · 0 unclaimed`.

**Experiment 1** — appended two bogus top-level keys to `tools/unattended/kit.toml`, one of them a
plausible typo of a key that descriptor already carries:

```toml
requires_config_frist = true
bogus_key_that_does_nothing = "xyzzy"
```

`selfcheck` → **exit 0**. `grep -ci "frist|bogus|xyzzy|unknown"` over the output → **0**.

**Experiment 2** — the behaviourally dangerous case. Renamed `guard` → `gaurd` on a lexicon
`[[gate_leg]]`:

```toml
gaurd = ["{kit}/"]
```

`selfcheck` → **exit 0**, zero mentions of either spelling.

Both edits reverted; tree restored to HEAD and selfcheck re-confirmed exit 0.

### Why experiment 2 is the sharp one

The emission path, `tools/govkit/govkit.py:4306-4315`:

```python
guards, dropped = [], []
for g in leg.get("guard", []) or []:
    ...
    else:
        guards.append(s)
```

With the key misspelled, `leg.get("guard")` returns the default. Both `guards` and `dropped` end
**empty**. Then:

- `:4335` — `if guards: row["guard"] = guards`. Empty, so the `guard` key is **omitted** from the
  leg written into the adopter's `gate-legs.json`. That leg now runs on every bar in that repo
  instead of only when its kit dir moves.
- `:4366` — `if dropped and not guards:` → `print(... 'UNGUARDED' ...)`. This is the diagnostic that
  exists specifically to announce a leg that ended up with no guard. It is predicated on `dropped`
  being non-empty, i.e. it only fires when guards were parsed and then discarded. **A guard that was
  never parsed produces `dropped == []` and stays silent** — the exact state the warning was written
  to catch is the one state it cannot report.

So the failure is silent at three consecutive stations: the descriptor is not key-checked, the
emitted leg simply lacks a field, and the guard-loss warning is structurally unreachable for the most
likely cause of guard loss. The adopter sees a green install and a leg whose scoping quietly
evaporated.

This is `memory/gotchas/`'s own recurring shape — a guard sharing state with the thing it guards —
and it is a NEW instance, on the deployer rather than on a gate.

### Fix

Give `read_descriptors` a known-key allowlist per table (`root`, `[[files]]`, `[[gate_leg]]`,
`[config]`, `[adopt]`, `[check]`, `[[hole]]`, `[[outcome]]`, `[[lf_pin]]`, `[[placeholder]]`,
`[[block]]`) and `r.fail` on an unrecognised one, with the `run-gates.sh:288` sentence as the
rationale. Separately, split `:4366` so "no guard declared" and "guards declared and all dropped"
are two distinct reports rather than one, since `guard = []` is a legitimate deliberate value
(`kickoff-manifest.kit.toml` uses it) and must stay distinguishable from a typo.

---

## F2 — `requires_config_first = true` is declared once and read nowhere; the unattended kit's 8-key config precondition is unenforced

**Severity: medium** · `tools/unattended/kit.toml:44`

`grep -rn "requires_config_first"` over the entire repo, excluding `.git/` and `__pycache__`, returns
**exactly one line — its own declaration.** No reader in `tools/` consumes it.

It sits on the `[adopt]` block of the one kit whose `[config]` is heaviest:

```toml
required_keys_gate = ["LANDER", "BYPASS_BAN", "GATE_CMD", "WIRING_CHECK",
                      "KEEPALIVE_CREATE", "KEEPALIVE_DELETE", "CORE_FLOOR", "DIRECTIVES_FLOOR"]
required_keys_render = ["LANDER", "KEEPALIVE_CREATE", "KEEPALIVE_DELETE", "KEEPALIVE_INTERVAL"]

[adopt]
argv = ["bash", "{kit}/adopt-unattended.sh"]
mutates_index = false
requires_config_first = true
```

The name states an ordering precondition — the target's `.unattended.conf` must carry those keys
before the adopter runs. Nothing sequences on it. Whatever ordering an adopter gets today is
incidental to `apply`'s step order, not derived from this declaration, and a change to that order
would not red anything.

This is the unattended kit, whose whole subject is a run that merges and pushes with no owner turn.
A declared precondition on that kit's install that no code reads is worth more than a tidy-up.

**Fix:** either enforce it (make CONFIGURE-before-ADOPT conditional on this key and assert it), or
delete the key and state the ordering in the descriptor's prose. What it must not stay is a
true-looking declaration with no reader. F1's allowlist would have caught this at authoring time.

---

## F3 — the `placeholders` list on `[[files]]` rules is read by nothing, and has already drifted in 3 of 10 rows

**Severity: medium** · `tools/drift-audit/kit.toml:26`

`grep -rn '"placeholders"|get("placeholders"'` across `tools/` returns **nothing**. The key is
declared on ten `[[files]]` rules across four kits and consumed by no reader.

Because nothing reads it, nothing grades it, and it has drifted. Measured by parsing each rule's
`include` glob and extracting `{{TOKEN}}` / `{TOKEN}`:

| Descriptor row | Declared | Actually in the template | Drift |
|---|---|---|---|
| `tools/drift-audit/kit.toml:26` → `.claude/skills/drift-audit/SKILL.md` | `KIT_DIR, MEMORY_ROOT, WORKFLOWS_DIR` | `KIT_DIR, WORKFLOWS_DIR` | **`MEMORY_ROOT` declared, absent from the file** |
| `tools/memory-tree/kit.toml:28` → `{memory_root}/HYGIENE.md` | `KIT_DIR, TOOL_ROOT` | `KIT_DIR` | **`TOOL_ROOT` declared, absent** |
| `tools/memory-tree/kit.toml:34` → `{memory_root}/TEMPLATE-SPEC.md` | `KIT_DIR, TOOL_ROOT` | `TOOL_ROOT` | **`KIT_DIR` declared, absent** |
| lexicon, memory-recall, unattended×2, memory-tree:40, workflows | — | — | exact match |

**Honest bound on the impact.** The drift is entirely in the safe direction: no template carries a
token that the descriptor fails to declare, and every rendered artifact on disk is free of
unsubstituted tokens (checked, listed above). So nothing is broken *today*. The cost is that the
descriptor is the deployer's contract language, three of its rows are already false, and the first
reader or gate that starts honouring the key inherits three wrong answers — which is precisely the
"hand-kept inventory disagreeing with what it describes" class this repo's own drift audit exists to
catch, sitting inside the deployer's own declarations where that audit does not look.

**Fix:** one assertion in `selfcheck` — for each `[[files]]` rule declaring `placeholders`, extract
the tokens from the included file and compare both directions. Roughly fifteen lines, and it reds on
the three rows above today, so its failing case is already observed (§7's bar for landing a new gate).

---

## F4 — a placeholder's `kit` key is read nowhere, and one of its two uses names a value from the wrong namespace

**Severity: low** · `tools/govkit/entries/playbook.kit.toml:206`

Two `[[placeholder]]` rows carry a `kit` key:

- `:204-206` — `key = "TOOLCHAIN_NOTES"`, `class = "asked"`, **`kit = "cross-os"`**
- `LEXICON_CONF` — `class = "derived"`, `kit = "lexicon"`

`render_playbook.py` reads a placeholder's `kit` key **nowhere**. Its only two `kit`-namespace
touches are `:204` and `:387`, and both operate on FENCES (`ns == 'kit'`), not on placeholder rows.
`govkit.py` never reads it either.

Worse, the two rows disagree about what the key means. `lexicon` is a registry entry id — the
population `kits` members are drawn from and the one `check_fences` validates a `kit:` fence against.
`cross-os` is **not** a registry entry; it is a `[[block]]` name in the `when:` namespace
(`playbook.kit.toml:241`), and `TOOLCHAIN_NOTES` lives inside the `<!-- when:cross-os -->` fence at
template lines 285-296. So one row keys on the kit namespace and the other keys on the block
namespace, through the same key name, and nothing notices because nothing reads it.

The conditionality the key looks like it should provide is already produced structurally:
`render_playbook.py:388` calls `remove_fenced` **before** the placeholder loop at `:391` iterates
`PLACEHOLDER_RE.findall(text)` over the post-drop text, so a placeholder inside a dropped fence is
never demanded. The key is decoration.

**Fix:** delete both `kit` keys, or — if the intent is to document which fence a placeholder depends
on — rename to `fence` and validate the value against both namespaces. Deleting is the smaller diff
and loses nothing, since the behaviour is already correct without it.

---

## F5 — `drop_blocks` is an operator control the deployer cannot write

**Severity: medium** · `WIRE-INTO-PROJECT.md:130`

The runbook has a section titled "The two blocks that are not about a kit":

> `drop_blocks` in the target's `deploy.toml` names blocks to remove that no kit governs. Two exist:
> `when:security-outbound` — the outbound-call and stored-content rules in `§9` … `when:cross-os` —
> `§11` whole. Drop it for a single-OS team.

The renderer implements it fully and carefully — `render_playbook.py:356, 377, 385` read it, grade it
against `[[block]]` declarations, and refuse a member matching no fence.

**`grep -c drop_blocks tools/govkit/govkit.py` → 0.** The deployer that writes the target's
`deploy.toml` never emits the key. `cmd_intake` (`:6528`) takes `--answer key=value` pairs, computes
`needed_answers(descs, selection)` from the `[[placeholder]]` rows, and writes those; there is no
`drop_blocks` answer, no flag, and no prompt. Intake then refuses to rewrite the file
(`:6544`) once it exists.

Net effect on the supported path: every govkit-deployed charter ships §9's outbound-security rules
and the whole of §11, regardless of whether the project has an outbound surface or is single-OS.
The only way to exercise the feature is to hand-edit `deploy.toml` after intake — which the intake
refusal message does contemplate ("edit it, or remove it deliberately"), so this is a reachability
gap in the deployment path rather than an outright broken feature. Reported at medium, not high, for
exactly that reason.

**Fix:** one line in `cmd_intake` — accept `--drop-block <name>` (repeatable), validate against the
descriptor's `[[block]]` rows, and write the array. The renderer's validation already exists.

---

## Notes for the skeptic

- Every claim above was executed, not read. The two selfcheck experiments mutated tracked files and
  both were reverted; `git status --porcelain` and a re-run of `selfcheck` (exit 0) confirm the tree
  is at HEAD.
- One incident worth recording: mid-session `tools/gate-legs.json` acquired an unrequested change
  (`chunk: records` → `selftests` on the memory-tree hygiene leg) that this lens did not make —
  almost certainly a sibling review agent sharing this worktree. Restored with
  `git checkout -- tools/gate-legs.json`. `govkit selfcheck` run alone on a clean tree does **not**
  mutate it, so it is not a read-only-verb-that-writes defect. Flagged only so nobody attributes that
  hunk to a product bug.
- F1's two experiments are the load-bearing evidence for the whole set: F2, F3 and F4 are the
  already-shipped consequences of the absence F1 demonstrates. If a skeptic refutes F1, F2–F4 survive
  independently as unread keys, but the "why did this happen" story goes with it.
