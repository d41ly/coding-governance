# TOOL-dRedressedBar-11 — a receipt-reading probe term in govkit's declared-outcome contract, closing settings-merge's last false-accept route

**Status:** CLOSED · rev-7 · 2026-10-16 · node d · Tier-2 · base ebce889c · streams tooling · order 7

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-15-build-TOOL-dRedressedBar-11-1-acceptance-ledger.md](../build/2026-10-15-build-TOOL-dRedressedBar-11-1-acceptance-ledger.md) | journal | — |
| [2026-10-14-prompt-TOOL-dRedressedBar-11-1-spec-writer.md](../prompts/2026-10-14-prompt-TOOL-dRedressedBar-11-1-spec-writer.md) | journal | — |
| [2026-10-14-prompt-TOOL-dRedressedBar-11-brief.md](../prompts/2026-10-14-prompt-TOOL-dRedressedBar-11-brief.md) | research | — |
| [2026-10-14-prompt-TOOL-dRedressedBar-12-4-revision.md](../prompts/2026-10-14-prompt-TOOL-dRedressedBar-12-4-revision.md) | research | TOOL-dRedressedBar-12 |
| [2026-10-14-prompt-TOOL-dRedressedBar-13-4-revision.md](../prompts/2026-10-14-prompt-TOOL-dRedressedBar-13-4-revision.md) | research | TOOL-dRedressedBar-13 TOOL-dRedressedBar-9 TOOL-dRedressedBar-10 |
| [2026-10-14-prompt-TOOL-dRedressedBar-14-4-revision.md](../prompts/2026-10-14-prompt-TOOL-dRedressedBar-14-4-revision.md) | research | TOOL-dRedressedBar-14 |
| [2026-10-14-review-TOOL-dRedressedBar-10-11-spec-audit-round1.md](../reviews/2026-10-14-review-TOOL-dRedressedBar-10-11-spec-audit-round1.md) | spec-audit | TOOL-dRedressedBar-10 |
| [2026-10-15-review-TOOL-dRedressedBar-1-20-diff-review-round1.md](../reviews/2026-10-15-review-TOOL-dRedressedBar-1-20-diff-review-round1.md) | diff-review | TOOL-dRedressedBar-1 TOOL-dRedressedBar-2 TOOL-dRedressedBar-3 TOOL-dRedressedBar-4 TOOL-dRedressedBar-5 TOOL-dRedressedBar-6 TOOL-dRedressedBar-7 TOOL-dRedressedBar-8 TOOL-dRedressedBar-9 TOOL-dRedressedBar-10 TOOL-dRedressedBar-12 TOOL-dRedressedBar-13 TOOL-dRedressedBar-14 TOOL-dRedressedBar-15 TOOL-dRedressedBar-16 TOOL-dRedressedBar-17 TOOL-dRedressedBar-18 TOOL-dRedressedBar-19 TOOL-dRedressedBar-20 |

<!-- /gen:spec-records -->

## 1. Goal

`TOOL-dRedressedBar-9` declares settings-merge's adopter exit 2 an accepted stop when agent-cap's hook
is absent, and `TOOL-dRedressedBar-10` S22 narrows the absence to two static homes. A hook that only
the target's install receipt locates still reads as absent. If `.claude/settings.json` then fails to
parse or write, the adopter exits 2, the verb prints `no-agent-cap-to-wire` as an accepted stop, and
the real error is swallowed. This unit adds one probe key to the `[[outcome]]` contract,
`must_not_resolve`, evaluated by the same resolver the adopter runs, so the probe and the adopter
cannot disagree about where the hook is. It uses the key in settings-merge's code-2 block, and makes
both refusal sites print the adopter's own reason (owner, 2026-10-14, unit 10 §8 F1 option (c)).

## 2. Scope (IN)

- **S1** — `tools/govkit/govkit.py` declares the probe keys once, beside `classify_outcome`, as
  `OUTCOME_PROBE_KEYS = {"must_exist": True, "must_not_exist": False, "must_not_resolve": False}`.
  `classify_outcome`'s key loop (`:6313-6327`) iterates that mapping. A `must_not_resolve` string is
  evaluated by the inlined `resolve_kit_dir` (`:196-230`), and the two existing keys by `exists()`
  exactly as today. The function's docstring states the new key's grammar and its no-receipt
  reading. Observed by AC1 and AC2.
- **S2** — `tools/govkit/entries/settings-merge.kit.toml`'s code-2 block gains
  `must_not_resolve = "{prefix}/hooks/agent-cap.js"` beside unit 10's two `must_not_exist` terms.
  Nothing else in the descriptor moves. Observed by AC1, AC2, AC3, AC4 and AC5.
- **S3** — The two verb sites that refuse an adopter's exit keep the adopter's stderr and end their
  problem line with it: `_cmd_apply`'s CONFIGURE step (`:7744-7772`, both non-accepted non-zero
  branches) and `_cmd_update`'s gained-adopter loop (`:11119-11126`). The shape is the regenerate
  site's (`:11019-11024`). Neither `subprocess.run` call changes its arguments. Observed by AC3
  and AC4.
- **S4** — `tools/govkit/matrix.py`'s `check_outcome_probes` reads the new key in all three of its
  rules. The agreement rule's `derive_probe_paths` reads keys by their `want` through
  `govkit.OUTCOME_PROBE_KEYS`, never by typed name. A new class rule checks that every probe key of
  every shipped block is one the engine evaluates, with its own liveness line. settings-merge's call
  to `check_outcome_states` gains two receipt rows. Observed by AC6, through the `New arm:` line in §7.
- **S5** — One `[dRB-11]` block in `tools/govkit/selftest.py`, placed after unit 9's `[dRB-9]` block
  in the same scope. It drives the apply route and the update route over a receipt-homed hook and a
  malformed settings file, and the apply route with no hook. Observed by AC3, AC4 and AC5, through
  the `New arm:` line in §7.
- **S6** — The unit adds no module-level function or class and takes none away, and adds no text-IO site
  without an encoding. So `memory/map/generated/symbols.json` stays fresh after unit 7's regen, the
  encoding-posture registry does not move, and unit 7 need not follow this unit. Observed by AC7.

## 3. Non-goals (OUT)

- No edit to `tools/settings-merge.py`, to `tools/lib/resolve_kit_dir.py`, or to any inlined copy of
  `resolve_kit_dir`. The term calls the resolver and never restates it.
- No change to which kits the registry's default set holds (brief non-goal).
- No edit to what units 9 and 10 own beyond two things. One is the new key in the code-2 block's
  probe. The other is the optional fourth row element in `check_outcome_states` and settings-merge's
  two new rows. Unit 10's two `must_not_exist` terms and its parent-home row stay as written.
- No rewording of the existing refusal texts. CONFIGURE's `unclassified` line still says no evaluator
  exists yet, which has been false since the evaluator landed. It gains the stderr tail only.
- No runtime refusal of an unknown probe key inside `classify_outcome` (§4, alternatives).
- No extracted stderr-tail helper (§4, alternatives).
- No kit version bump, no `KIT_GOVKIT_VERSION` move, and no receipt or descriptor schema change (§4).
- No `help/` page. `help/` holds `README.md` and `roles.md`, and neither covers govkit.

### Edges

- **consumes-from** `TOOL-dRedressedBar-10` — the tree it leaves. That tree holds unit 9's code-2
  block with unit 10's two-term `must_not_exist` list, which S2 adds a key to. It holds unit 9's
  `check_outcome_states` with unit 10's parent-home row, which S4 adds rows to, and unit 9's
  `[dRB-9]` block, which S5's block follows. Without it there is no block to extend and no helper
  to add rows to. AC2's, AC3's and AC4's red halves read its block at its pass commit. Unit 9 is
  reached through this edge, because unit 10 already consumes it and this unit lands after both.
- **hands-off** `TOOL-dRedressedBar-12` — report id 23 (H1) of the units-10-11 spec audit. An apply
  narrower than the receipt's claimed kits writes a receipt holding only its selection's rows
  (`tools/govkit/govkit.py:8019-8021`). So the refusal this unit adds on fixture A's second apply is
  lost on the next one. Unit 12 keeps every claimed kit the selection did not name, with its rows,
  and runs fixture A a third time. It corrects §4 "Which receipt bytes" and the first "What an
  adopter sees change" row.
- **hands-off** `TOOL-dRedressedBar-13` — the same audit's minors on this spec, report ids 6, 7, 10,
  11, 12, 13, 17, 20, 21, 22 and 24. Unit 13 documents the fourth row element of
  `check_outcome_states` and prefixes the key rule's labels. It observes the agreement rule's union
  by `want` on a staged pair, and decodes CONFIGURE's stderr as UTF-8. It rebuilds fixture B through
  `write_vintage_receipt` and restates the code-2 block's comment. It corrects this spec's §4, §5 and
  §7 in one rev bump.
- **hands-off** `TOOL-dRedressedBar-14` — settings-merge's half of a defect measured at spec time: a
  first `apply` selecting agent-cap with `[kit.agent-cap] prefix = "scripts"` exits 1 with both
  adopters at exit 2. CONFIGURE runs before the receipt is written, so neither resolver finds the
  hook. The term agrees with the adopter there. Unit 14 writes the receipt ahead of CONFIGURE, which
  this unit's `must_not_resolve` term then reads.
- **hands-off** `TOOL-dRedressedBar-15` — agent-cap's half of the same defect. Its adopter argv names
  settings-merge's file through agent-cap's own `{prefix}`, and its refusal reports the install
  through S3's stderr tail, which unit 15's red half reads.
- **hands-off** external — the stale `unclassified` clause, and the six inline spellings of a
  stderr tail in `tools/govkit/govkit.py`, consolidated into one helper by their own unit.
- **hands-off** `TOOL-dRedressedBar-28` — the code-2 block's two static terms, which that unit takes
  out because this unit's term asks both homes, and this spec's row C5 and §5 security clause,
  which its spec-writer pass corrects.

## 4. Design

### The residual, measured

settings-merge.py finds the hook through `resolve_kit_dir("hooks", "agent-cap.js", <its own dir>)`
(`tools/settings-merge.py:192`). The resolver reads `.governance/install.json` first. It returns the
directory of the first row whose `source` ends in `hooks/agent-cap.js` and whose `path` is a file
inside the tree. Only then does it probe `<here>/hooks` and `<here>/../hooks` (`:77-111`). Where
nothing is found, the adopter joins a path that exists nowhere (`NO_HOOKS_KIT`, `:117`, `:197-223`)
and refuses with exit 2 (`:1046-1052`). Where the hook IS found, `run` returns 2 on a malformed
settings file (`_load`, `:491-500`) and on a write `OSError` (`:507-539`).

Measured on 2026-10-14 at `60fa5534`, whose `tools/` and `skills/` equal `ebce889c`'s
(`git diff --stat ebce889c7 HEAD -- tools skills` prints nothing), with scratch programs under
`%TEMP%`. Nothing in the tree was written.

| Fixture | Reading |
|---|---|
| A: `apply --kits settings-merge`, then a hook at `guard/agent-cap.js` with one receipt row recording it, `{` as `.claude/settings.json`, a second `apply --kits settings-merge` | exit 1, `CONFIGURE settings-merge: adopter exit 2`, one problem: `its adopter exited 2 — unclassified, because no [[outcome]] evaluator exists yet …`, with no reason |
| A, the adopter run directly with the planted receipt | exit 2, `settings-merge: cannot read .claude\settings.json: Expecting property name enclosed in double quotes: line 1 column 2 (char 1)` |
| A, unit 10's block held in memory, classified by the base engine at rc 2 | ACCEPTED, the false accept |
| A, govkit's inlined `resolve_kit_dir("hooks", "agent-cap.js", <t>/tools)` | returns `guard` |
| B: a `stale_target`-shaped install with `[kit.agent-cap] prefix = "scripts"`, `scripts/hooks/agent-cap.js` with its receipt row at the old vintage, `agent-cap` claimed, `{` as settings, then `update --write --to <HEAD>` | exit 1, one problem: `its adopter exited 2 on the update that gained it, and no declared outcome accepts that`, with no reason. Four fragment lines print `REFUSED by settings-merge (exit 2): settings-merge: cannot read …` and count no problem. `gov_commit` stays `24f39915` |
| C: a real `apply --kits agent-cap,settings-merge,kickoff-manifest` with `[kit.agent-cap] prefix = "scripts"` | the receipt row is `scripts/hooks/agent-cap.js` with source `tools/hooks/agent-cap.js`, the same shape A and B plant |

So the brief's claim that the base prints the false accept is wrong. The base has no code-2 block, so
it refuses the exit as `unclassified`. The false accept needs unit 9's or unit 10's block. Each
criterion's red half below is therefore read over unit 10's block, at `<p10>`. The base reading is
red for S3 alone, because no refusal line names the reason.

### The term

```toml
[[outcome]]
code = 2
probe = { must_exist = "{prefix}/settings-merge.py", must_not_exist = ["{prefix}/hooks/agent-cap.js", "{prefix}/../hooks/agent-cap.js"], must_not_resolve = "{prefix}/hooks/agent-cap.js" }
means = "no-agent-cap-to-wire"
ok = true
```

| Part | Meaning |
|---|---|
| value | a string or a list of strings, as the two existing keys take |
| each string | `<here>/<home>/<anchor>` after `resolve_tokens` with the entry's context |
| `<anchor>` | the last segment, the file the kit is found by |
| `<home>` | the segment before it, the kit's home as gov ships it, which the resolver matches against a receipt row's `source` |
| `<here>` | every earlier segment, target-relative and possibly `.`, the directory the adopter resolves from |
| holds when | `resolve_kit_dir(home, anchor, target / here)` raises `LookupError` |

For settings-merge the string splits into `here = {prefix}`, `home = hooks` and
`anchor = agent-cap.js`, the adopter's own call. It reads like unit 10's first term on purpose.

The term is evaluated by govkit's inlined copy of the resolver (`tools/govkit/govkit.py:196-230`),
which the `python resolver (behaviour + inline parity + idiom ban)` leg holds byte-identical to the
copy in `tools/settings-merge.py:77-111`. govkit already calls it for selfcheck 5b (`:2129`). So the
probe asks the adopter's question with the adopter's code, and the receipt half, the static half and
the containment rule are each stated once.

Three readings fail the term and so leave the block unmatched, which refuses the exit. They are a
string with fewer than two segments, an unresolved token, and a `home` or `anchor` that is empty,
`.` or `..`. This is the rule `classify_outcome` already applies to an unresolved token
(`:6318-6320`): deny by default.

**With no receipt.** The resolver treats an absent, unreadable or malformed receipt as no rows
(`tools/settings-merge.py:93-96`). On a fresh `apply` the term therefore reads the two static homes
only. With neither present it holds and the stop is accepted, which is also what the adopter did.

**Which receipt bytes.** The term reads `.governance/install.json` as it is on disk at
classification, which is right after the adopter returns. `_cmd_apply` writes its receipt twice.
`TOOL-dRedressedBar-14`'s S1 writes it between HOOKPROBE and CONFIGURE, and the RECEIPT step
rewrites it at `:8019`, after CONFIGURE (`:7740-7772`). So in `apply` the term reads the receipt this
run wrote ahead of CONFIGURE. That receipt holds this run's rows and the carried ones, and it is
still the same bytes the adopter read. A first `apply` therefore never reaches the "With no receipt"
reading above: the term reads this run's rows before the two static homes. `_cmd_update` writes at
`:12017-12062`, after the gained loop (`:11104-11126`), so there the term reads the prior receipt,
the same bytes the adopter read. A refused apply still writes its receipt: a non-accepted CONFIGURE
exit only calls `r.fail` (`:7764`, `:7771`), and the RECEIPT step at `:8019` then writes `kits` and
`files` from this run's selection alone (`:8021`). A later run's term reads that receipt's rows:
`update` reads the receipt itself, and a later `apply` reads them carried into its own early write.
`TOOL-dRedressedBar-12` keeps it whole, carrying every kit the prior receipt claims with its rows,
and `TOOL-dRedressedBar-14` binds that carry ahead of the early write, so the hook's receipt row
outlives the refused apply.

### The declared key set

```python
#: Every key an `[[outcome]] probe` may carry, mapped to whether the thing it names must be found.
OUTCOME_PROBE_KEYS = {"must_exist": True, "must_not_exist": False, "must_not_resolve": False}
```

`classify_outcome` loops over this mapping in place of its typed pair. For `must_not_resolve` the
found test is "the resolver returned". For the other two it is `(target / resolved).exists()`, as
today. A constant, not a function, so `symbols.json` does not list it: the map lists ids of kind
function and class, and `EPOCH_ROLES` and `RECEIPT_SCHEMA` are absent from it (read 2026-10-14).

### Every reader of `[[outcome]]` probes, and what each does with the term

| Reader | Site | With `must_not_resolve` |
|---|---|---|
| `classify_outcome` | `tools/govkit/govkit.py:6295-6329` | evaluates it (S1). The only evaluator of probe keys |
| `run_kit_check`, the `check` verb | `:5091` | through `classify_outcome`, unchanged. settings-merge declares `[check] none`, so its block is never reached here |
| `_cmd_apply` CONFIGURE | `:7745` | through `classify_outcome`; a refused exit now names its reason (S3) |
| `_cmd_update` regenerate loop | `:10999` | through `classify_outcome`, unchanged. settings-merge declares `why_no_regenerate`, not `[[regenerate]]` |
| `_cmd_update` gained loop | `:11121` | through `classify_outcome`; a refused exit now names its reason (S3) |
| matrix class rule | `tools/govkit/matrix.py:174-185` | unchanged. It requires a `must_exist` on every accepted stop, and the term is an absence, so a stop declared by this term alone still reds there |
| matrix agreement rule | `tools/govkit/matrix.py:199-215` | `derive_probe_paths(block, want)` unions every key the mapping gives that `want` (S4) |
| matrix engine-agrees | `check_outcome_states`, unit 9 | two new settings-merge rows (S4) |
| matrix key rule | new, in `check_outcome_probes` | every shipped probe key is in the mapping (S4) |
| selftest arms | `tools/govkit/selftest.py:12781-12802`, `:12902-12928` | unaffected: `must_exist`-only blocks. `:12926` slices the source between `def run_kit_check` and `def classify_outcome`, which S6 keeps true |

No other reader exists: `git grep` for `classify_outcome`, `must_not_exist` and `"outcome"` over
`tools/` and `skills/` finds only these sites and a `tools/roles/handoff.py` dict key of another
meaning. The brief names three readers. `check` and the regenerate loop are two more, and both go
through the one evaluator.

The key rule's census, read on 2026-10-14 through `read_descriptors` at `60fa5534`: 29 descriptors,
18 `[[outcome]]` blocks, 5 with `ok = true`, keys `must_exist` 17 times and `must_not_exist` 6 times,
and no other key. So the rule reads green over the real tree before it is armed, and its staged
break is a typo'd key.

### The refused exit names its reason

Both sites bind the `CompletedProcess` they already create, rather than taking `.returncode` off it,
under a name the long function does not bind: `_cfg_run` in `_cmd_apply` and `_proc_g` in
`_cmd_update` (each `grep -c` reads 0 today). The problem line then ends in the regenerate site's
shape. When stderr has lines, that is `. Its stderr ended: ` and the last three non-blank lines
joined by ` | `. Otherwise it is `. It printed nothing to stderr`. CONFIGURE's call kept
`capture_output=True, text=True` with no encoding at this unit's pass
(`tools/govkit/govkit.py:7781`, read at `fda78c56`). So the tail it prints is decoded with the
host's codepage, and on a host without UTF-8 mode a non-ASCII character in an adopter's stderr,
such as settings-merge's em dash, prints garbled. The regenerate site and the gained loop already
decode UTF-8. Its site count in `memory/project/encoding-posture-sites.txt` was 36, the scanner's
reading at `60fa5534` through `scan_text_io`. `TOOL-dRedressedBar-13`'s S13 gives that call
`encoding="utf-8", errors="replace"`, and the row falls to 35 in the same commit. An accepted exit
prints no tail.

### What an adopter sees change

| Situation | At unit 10's tip | After |
|---|---|---|
| `apply --kits settings-merge`, agent-cap at a home only the receipt records, malformed settings | exit 0; `CONFIGURE settings-merge: adopter exit 2 — no-agent-cap-to-wire [accepted stop]` | exit 1; `CONFIGURE settings-merge: adopter exit 2`; the problem line ends `Its stderr ended: settings-merge: cannot read …`; with `TOOL-dRedressedBar-12`'s carry, the refusal holds on every re-run |
| `update --write` gaining settings-merge, the same state | exit 0; re-stamped; `default-gained settings-merge: adopter exit 2 — no-agent-cap-to-wire` | exit 1; not re-stamped; the problem line ends with the same reason |
| agent-cap absent everywhere, any settings file | the accepted stop | unchanged |
| agent-cap at a receipt-recorded home, valid settings | adopter exit 0 | unchanged; the code-2 block is never consulted |
| any other refused adopter exit in either loop | a code and no reason | the same line, ending with the adopter's stderr tail |

### Versions

No kit version moves. All four files sit under `{prefix}/govkit`, which the registry exempts as the
deployer itself (`tools/govkit/registry.toml:295-297`). So none is a `[[files]]` source whose role
the epoch reads (`EPOCH_ROLES`, `tools/govkit/govkit.py:12935`). `KIT_GOVKIT_VERSION` (`:47`) stays
`1.14`. It was last moved at `8a6cbc9c`, and 39 commits have touched `govkit.py` since without
moving it (`git rev-list --count`). `tools/check-kit-versions.sh:367` grades it against the
two-part shape at `:133`, not its movement. No descriptor schema version exists. The only schema
constant is `RECEIPT_SCHEMA` (`:49`), and no receipt field moves. The new key is additive, and every shipped descriptor is read
exactly as before.

### Order, and unit 7

Unit 7 need not follow this unit. It mints kit versions and runs `regen.py --write`. This unit owes
no version, as above. Its only possible generated-output effect is `symbols.json`, which records
`id`, `kind` and `file` with no line numbers. S6 keeps that set unchanged, and AC7 observes it.

The README ordering this implies already stands in `memory/builds/dRedressedBar/README.md`. Its
Build-level rules say that units 10, 11, 12, 13 and 14 follow 7 in that order, and that each
touches only govkit-exempt files and adds no function. Its derived build-order region lists this
unit at step 7.

### The witnessing arms

`check_outcome_states` gains an optional fourth row element: a mapping from a target-relative path
to text. The helper writes it before it classifies and deletes it after. Two texts state the row
shape: the helper's docstring and spec 9's §4 sentence on its rows. `TOOL-dRedressedBar-13`'s S6
makes both name the fourth element. Lexicon's rows and unit 9's
and unit 10's settings-merge rows carry none, so their labels and verdicts are unchanged.
settings-merge's call gives its scratch directory a `.git` entry. The resolver's root walk then stops
there and never reaches an ambient repository above the scratch directory. Its two new rows are
these.

| Row | Present | Receipt row | rc 2 verdict |
|---|---|---|---|
| a hook only the receipt locates | `settings-merge.py`, `guard/agent-cap.js` | `guard/agent-cap.js` | REFUSED |
| a receipt row whose path is absent | `settings-merge.py` | `guard/agent-cap.js` | ACCEPTED |

The receipt row's `source` is agent-cap's engine source as `resolve_entry` gives it, derived and
never typed. The home `guard/agent-cap.js` is a fixture value, and the row asserts it equals neither
static term's resolved path, so it cannot pass on a static home.

The `[dRB-11]` block follows unit 9's `[dRB-9]` block inside the scope that defines `stale_target`.
It builds fixtures A, A-absent and B of §6, through `make_target`, `settle`, `stale_target` with
`DEPLOY_FULL` plus `[kit.agent-cap] prefix = "scripts"`, and `run`. Fixture B's old-vintage
agent-cap row comes from the selftest's `write_vintage_receipt` (`tools/govkit/selftest.py:617-673`),
which writes a row's bytes at a vintage and sets its `commit`, `sha256` and `gov_oid`, and is
idempotent over rows already rewound. The block appends the row and claims `agent-cap`, then calls
`write_vintage_receipt(govroot, t, OLD)` before `settle`, so it never derives an identity itself.
Unit 11's pass derived them by hand with a `git show`, `_sha` and `blob_oid`, and
`TOOL-dRedressedBar-13`'s S17 rebuilds fixture B through the helper. For A and B the block asserts
four
facts. The run exits non-zero. Exactly one line opens with the problem prefix for settings-merge, and
that line carries `cannot read` (the line, never the whole output). No line carries `means`, which
is read from the descriptor's code-2 block at run time. For B, `gov_commit` is unchanged. A-absent
exits 0 and prints `[accepted stop]`. Its file reads name `encoding="utf-8"` and its process calls go
through `run`, so its counted sites stay at the registry's 24 and 1.

### Inventory

| Identifier | Kind | Naming cell |
|---|---|---|
| `must_not_resolve` | an `[[outcome]] probe` key | none; snake case, the shape of `must_not_exist` |
| `OUTCOME_PROBE_KEYS` | a module constant in `tools/govkit/govkit.py` | none: `lexicon.py --suggest OUTCOME_PROBE_KEYS --as py.constant` answered that no `py.constant` cell is declared |
| `_cfg_run`, `_proc_g` | locals in `_cmd_apply` and `_cmd_update` | none |
| `[dRB-11]` | the check-label prefix of the new selftest block | none |

### Rollout

Tier-2: a new vocabulary in the descriptor contract that four engine sites and the matrix read, and a
change to what two verbs accept. No receipt, conf or deploy shape moves, and no target needs an
upgrade step. The next `apply` or `update` an adopter runs reads the new descriptor.

### Files touched (estimate)

- `tools/govkit/govkit.py`
- `tools/govkit/matrix.py`
- `tools/govkit/selftest.py`
- `tools/govkit/entries/settings-merge.kit.toml`
- `memory/builds/dRedressedBar/build/`, for the acceptance ledger §6's `<p11>` reads. Unit 11's
  pass, `b65688cde`, wrote no ledger there, and its commit body carries its readings.

### Alternatives rejected

Each candidate was written down with the test that could make it lose, and the pick is M3's.

| Candidate | The test that rejected it | Verdict |
|---|---|---|
| C1 — a receipt-only key whose reader re-implements the resolver's receipt loop in `classify_outcome` | It needs its own copy of the `source` match, the containment rule and the unreadable-receipt reading. That is two answers to one question, and the copy can drift from the parity-gated resolver unseen | Rejected by the reuse rule |
| C2 — a path token, `{receipt:<kit>}`, resolved in `resolve_tokens` | An unresolved token fails the whole block (`:6318-6320`), so on a fresh `apply` with no receipt the stop would be refused, against the brief's absent case. `resolve_tokens` also feeds every argv the engine runs | Fails the brief's acceptance |
| C3 — `classify_outcome` reads the receipt dict the verb holds | Four call sites change signature, and the dict equals the bytes the adopter read only by the order of writes | Survives; more surface for the same answer |
| C4 — `must_not_resolve`, evaluated by the inlined resolver | Its losing test is fixture A: a term that still read ACCEPTED there would lose. It refuses there, and reads ACCEPTED in the absent rows (AC2) | Chosen |
| C5 — also retire unit 10's two static terms, which C4 subsumes | The owner's pick names the narrowing ("(c) Narrow + receipt probe"), and unit 10's AC15 and parent-home row read those terms. Keeping them costs two `exists` calls | Rejected; kept. Taken by `TOOL-dRedressedBar-28`, at its §8 F1, once the install-prefix ban counted the parent home's spelling. C4 subsumes the terms in every state that unit measured but the two its §4 names |
| C6 — extract a stderr-tail helper for S3 | `govkit.py` spells the idiom six ways (`:5916`, `:6219`, `:6590`, `:6899`, `:11019`, `:13200`). One helper for all six is its own mechanism, and a new function stales `symbols.json` after unit 7's regen | Rejected; handed off |
| C7 — `classify_outcome` refuses any block carrying an unknown key at run time | Descriptors come only from gov's tree, and S4's key rule grades the whole class at the bar | Rejected as YAGNI |

## 5. Production-readiness checklist

- security — Narrows an accepted stop and widens nothing: one more state is refused, none is newly
  accepted. The term reads the receipt through the resolver's own containment, so a row whose path
  escapes the tree is skipped, never followed. That containment covers receipt rows only
  (`tools/govkit/govkit.py:222`). The resolver's two static probes, `<here>/hooks` and
  `<here>/../hooks` (`:224`), carry none, so with `prefix` at `.` the term's second static probe may
  leave the tree, as unit 10's parent-home `must_not_exist` term could until `TOOL-dRedressedBar-28`
  took it out of the block. The term fails closed there: a hook in the target's parent makes the term refuse an exit unit 9 accepted, never accept one. S3
  prints, verbatim
  and to the operator's terminal, the last three stderr lines of whichever adopter CONFIGURE or the
  gained loop refuses, as the regenerate site already does. So its producers are every shipped
  descriptor's `[adopt].argv`: thirteen bash adopters, and `tools/settings-merge.py`, which
  agent-cap's and settings-merge's argv both run. The bash adopters' own stderr lines were read
  with `git ls-files 'tools/*adopt-*.sh' 'tools/playbook/adopt-playbook.sh' | grep -v test | xargs grep -h '>&2'`
  at `fda78c56`. They print kit names, paths such as `$KIT_REL`, `$TARGET` and `$FIXTURE_REL`,
  refusal and usage text, the `ROUTED_PATHS` candidate memory-tree appends to its conf, and
  unfilled template lines, and none expands a credential. settings-merge's stderr carries paths and
  parse positions, never settings values. A child process an adopter runs reaches the tail too, as
  the target-side code's own output.
- perf / scale — N/A — one receipt read per settings-merge exit 2, and two matrix rows.
- error / empty / loading states — No receipt, an unreadable receipt and a malformed receipt each
  read as no rows, which is the adopter's reading. A malformed term value refuses the block.
- observability — A refused exit now names its reason on its own problem line. An accepted stop
  prints as before.
- risks — The gained loop runs one argv once for two kits when both are gained
  (`tools/govkit/govkit.py:11112-11118`). agent-cap is listed first, so that run is classified by
  agent-cap's descriptor, which declares no outcome, and the term is not read. A target whose
  installed `settings-merge.py` carries an older resolver than gov's could disagree with the term;
  the parity leg holds gov's copies only.
- testing — AC1 to AC7 are direct probes: greps, in-process engine calls, and scratch targets under
  `%TEMP%`. The two new arms are declared in §7.
- migration — N/A — no receipt, conf or deploy field moves.
- user docs — N/A — `help/` holds no govkit page, and no runbook sentence names the accepted stop or
  the probe grammar. The grammar's one statement is `classify_outcome`'s docstring (S1).

## 6. Acceptance criteria

`<p10>` and `<p11>` are the commits of units 10 and 11's build passes, as their acceptance ledgers
name them. Every command runs from the worktree root. Fixtures live in fresh `git init` targets under
`%TEMP%/<short-name>`, never inside the worktree, with `.governance/deploy.toml` holding
`DEPLOY_FULL`'s answers (`tools/govkit/selftest.py:700-710`).

- **AC1** — When `grep -n -A5 '^\[\[outcome\]\]' tools/govkit/entries/settings-merge.kit.toml` runs,
  it prints one block carrying `code = 2`, unit 10's two-term `must_not_exist`,
  `must_not_resolve = "{prefix}/hooks/agent-cap.js"`, `means = "no-agent-cap-to-wire"` and `ok = true`.
  `grep -n 'must_not_resolve' tools/govkit/govkit.py` prints the `OUTCOME_PROBE_KEYS` line and
  `classify_outcome`'s docstring, and `grep -n '("must_exist", True)' tools/govkit/govkit.py` prints
  nothing, where at `ebce889c` it prints the typed pair at line 6313.
  Red when: the block keeps unit 10's terms alone, or the loop keeps its typed key pair.
- **AC2** — When a python program imports `tools/govkit/govkit.py`, reads the shipped descriptors
  with `read_descriptors`, and prints `outcome_accepted(2, classify_outcome(...), declares_outcome_for(d, 2))`
  for settings-merge over scratch targets, each holding `.git` and `tools/settings-merge.py`, it reads
  as follows. ACCEPTED with nothing else. REFUSED with `guard/agent-cap.js` present and a receipt row
  recording it. ACCEPTED with that row and the file absent. ACCEPTED with the file present and no
  receipt. ACCEPTED with the file present and a receipt holding `{`. REFUSED with the hook at
  `tools/hooks/agent-cap.js`, and REFUSED at `hooks/agent-cap.js`. With gov's `tools/settings-merge.py`
  copied in and `{` as `.claude/settings.json`, the adopter's stderr carries `cannot read` in the
  REFUSED receipt row and `refusing to wire` in the no-receipt row. So the term and the adopter agree
  on both sides.
  Red when: the program reads the block from `git show <p10>:tools/govkit/entries/settings-merge.kit.toml`,
  and the receipt row reads ACCEPTED.
- **AC3** — Fixture A: `python tools/govkit/govkit.py apply --target <t> --kits settings-merge`, commit,
  then gov's `tools/hooks/agent-cap.js` copied to `<t>/guard/agent-cap.js`. One row is appended to
  `.governance/install.json`'s `files`, with path `guard/agent-cap.js`, kit `agent-cap`, role `engine`,
  source `tools/hooks/agent-cap.js`, and that blob's `sha256` and `gov_oid`. `agent-cap` is added to
  its `kits`, `{` is written to `.claude/settings.json`, and the target is committed. When the same
  apply then runs again, it exits 1. Its `CONFIGURE settings-merge:` line carries no
  `no-agent-cap-to-wire`. Exactly one line opens `govkit: kit 'settings-merge'`, and that line carries
  `cannot read` and `settings.json`.
  Red when: the same fixture over a gov clone checked out at `<p10>` exits 0 and prints
  `[accepted stop]`, or the problem line names no reason, as at `ebce889c`.
  fixture: the base half was observed at spec time on `60fa5534` (§4, fixture A).
  cost: a local `git clone` of gov to `%TEMP%` for the `<p10>` half, about a minute.
- **AC4** — Fixture B: a target built as `stale_target` builds it (`tools/govkit/selftest.py:3237-3249`),
  with `[kit.agent-cap] prefix = "scripts"` added to its deploy. Before the commit,
  `scripts/hooks/agent-cap.js` gets the hook's bytes at the old vintage, with one receipt row at that
  vintage's identities, `agent-cap` claimed, and `{` as `.claude/settings.json`. When
  `python tools/govkit/govkit.py update --target <t> --write --to <tip sha>` runs, it exits 1, and the
  receipt's `gov_commit` stays at the old vintage. One line opens
  `govkit: kit 'settings-merge': its adopter exited 2 on the update that gained it`, and it carries
  `cannot read`. No line carries `default-gained settings-merge: adopter exit 2 — no-agent-cap-to-wire`.
  Red when: over the `<p10>` clone the run exits 0, re-stamps, and prints that accepted line.
  fixture: the base half was observed at spec time on `60fa5534` (§4, fixture B): exit 1, the one
  problem line with no reason.
  cost: the build and the update take about a minute per gov tree.
- **AC5** — Fixture A-absent is fixture A with no hook and no receipt row, and `{` still as settings.
  The second `python tools/govkit/govkit.py apply --target <t> --kits settings-merge` exits 0 and
  prints `CONFIGURE settings-merge: adopter exit 2 — no-agent-cap-to-wire [accepted stop]`. Unit 9's
  AC2 program, run at the tip, still exits 0 and prints its accepted-stop line.
  Red when: the term reads a receipt with no matching row as a found hook, and the stop is refused.
- **AC6** — When a python program imports `tools/govkit/matrix.py`, replaces its module-level `check`
  with a recorder, and calls `check_outcome_probes` on a scratch directory, every recorded label is
  true. The key rule records one label per shipped `[[outcome]]` block, and its liveness label is
  recorded. settings-merge's rows record unit 9's three, unit 10's one and this unit's two. The two
  labels opening `lexicon ` equal unit 10 AC7's pinned pair. With `govkit.read_descriptors` patched to
  rename settings-merge's `must_not_resolve` to `must_not_resolves`, the key rule's settings-merge
  label and the receipt-homed row both record false.
  Red when: a probe key the engine does not evaluate reads green, or the receipt-homed row passes on
  a block without the term.
  figure: the block count is DERIVED by `read_descriptors` at observation; 18 at `60fa5534`, PINNED
  2026-10-14, plus unit 9's one.
- **AC7** — When `git diff <p10> <p11> -- tools/govkit/ | grep -E '^[+-](def|class) '` runs, it prints
  nothing. A python program that imports `tools/gate-lint/encoding_posture.py` and runs
  `scan_text_io` over `tools/govkit/govkit.py`, `tools/govkit/matrix.py` and `tools/govkit/selftest.py`
  at `<p11>` counts, per arm, exactly the rows `memory/project/encoding-posture-sites.txt` declares.
  Red when: the pass minted a function, which stales `symbols.json` past unit 7's regen, or added an
  unencoded text-IO site.
  figure: DERIVED from the registry at observation; 36 subprocess sites in `govkit.py`, 24 subprocess
  and 1 file-io in `selftest.py`, and none in `matrix.py` at `60fa5534`, PINNED 2026-10-14.

## 7. Gates

`govkit selftest` · `govkit acceptance matrix` · `govkit refusal join` · `govkit selfcheck` · `receipt sync (installed files match the receipt)` · `recall floor` · `recall floor arms` · `memory hygiene` · `encoding posture (text IO names its encoding)`

New arm: tools/govkit/matrix.py · covers AC2 AC6 · settings-merge's receipt-homed row over unit 10's block at `<p10>` reads ACCEPTED, and the key rule over a descriptor patched to `must_not_resolves` reads false · none
New arm: tools/govkit/selftest.py · covers AC3 AC4 AC5 · the `[dRB-11]` block over unit 10's block, where fixtures A and B exit 0 on the accepted stop, and at `ebce889c`, where the problem lines carry no `cannot read` · none

The refusal join's floor does not move: S3 lengthens two existing `r.fail` messages and adds no
refusal branch, and the term's failures leave a block unmatched rather than raising. The main loop
observes both new arms red, then green, at the close.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-14 · initial draft from the unit-11 brief. The residual was reproduced on both
  verbs at `60fa5534` with planted receipt rows, and the planted shape was matched against a real
  per-kit-prefix install. Seven candidates were graded by M12, and the pick was taken by M3's rule.
- rev-2 · 2026-10-14 · §3 · Edges gain the hands-off to `TOOL-dRedressedBar-12`, the unit the
  units-10-11 spec audit's one high was promoted into, for report id 23. They also gain the hands-off
  to `TOOL-dRedressedBar-13`, the batch its minors were promoted into, for report ids 6, 7, 10, 11,
  12, 13, 17, 20, 21, 22 and 24. No scope, design or criterion moves.
- rev-3 · 2026-10-14 · §3 · Edges split the external hand-off for the apply-prefix defect into the
  hands-off to `TOOL-dRedressedBar-14`, for settings-merge's half, and the hands-off to
  `TOOL-dRedressedBar-15`, for agent-cap's half, the units the owner added for it. No scope, design
  or criterion moves.
- rev-4 · 2026-10-14 · §4 · a records fix for TOOL-dRedressedBar-12, closing the units-10-11 spec
  audit's report id 23 (H1), written by that unit's spec-writer pass `<w12>` as its S4. The status
  stays CLOSED. §4 "Which receipt bytes" states that a refused apply still writes its receipt and
  that a later run reads that receipt, which unit 12 keeps whole. The first "What an adopter sees
  change" row's "After" cell says the refusal holds on every re-run, which TOOL-dRedressedBar-12's
  AC2 observes. AC3's text does not move. No scope or criterion moves.
- rev-5 · 2026-10-14 · §4 · §5 · §7 · a records fix for TOOL-dRedressedBar-13, closing the
  units-10-11 spec audit's report ids 6, 7, 10, 11, 12, 13, 17, 20, 21, 22 and 24, written by that
  unit's spec-writer pass `<w13>`. The status stays CLOSED. Corrected in place: §4 "The witnessing
  arms" names the two texts that state the row shape and that they gain the fourth element (id 6),
  and builds fixture B's old-vintage row through `write_vintage_receipt` (id 17). §4 "The refused
  exit names its reason" states that CONFIGURE decoded its stderr with the host's codepage, and that
  TOOL-dRedressedBar-13 decodes it as UTF-8 and moves the row from 36 to 35 (id 13). §4 "Order, and
  unit 7" points at the build README, which already holds the ordering it called pending (ids 11
  and 21). Files touched gains `memory/builds/dRedressedBar/build/`, and §7 gains `recall floor` and
  `memory hygiene` (id 20). §5 security states that the resolver's containment covers receipt rows
  only (id 12), and prices the stderr tail over every adopter that can print it (id 24). Criterion
  halves that did not hold, each observed in its corrected form by TOOL-dRedressedBar-13: AC6 pinned
  the two `lexicon ` labels while S4 gave the key rule no label prefix (id 7, its AC7). AC6 never
  exercised the agreement rule's union by `want`, because settings-merge has one `ok = true` block
  (id 10, its AC9). AC4's "Before the commit" was inexact, because `stale_target` has already
  settled when the plant begins (id 17, its AC15). The fourth element is observed in the helper's
  docstring and spec 9 (id 6, its AC6). Id 22 is a code fix that unit's build pass owns: S2's
  "Nothing else in the descriptor moves" left the code-2 block's comment describing one term. No
  criterion text moves. The CONFIGURE call is cited at `tools/govkit/govkit.py:7781`, read at
  `fda78c56`, where the report read `:7744`, because later build passes moved `_cmd_apply`.
- rev-6 · 2026-10-14 · §4 · a records fix for TOOL-dRedressedBar-14, written by that unit's
  spec-writer pass `<w14>` as its S5. The status stays CLOSED. §4 "Which receipt bytes" states
  that `_cmd_apply` writes its receipt twice, and that in `apply` the term reads the receipt this
  run wrote ahead of CONFIGURE. That receipt holds this run's rows and the carried ones, and it is
  still the bytes the adopter read. `update` is unchanged. Two rev-1 sentences are reworded because
  unit 14's ordering made them false. "`_cmd_apply` writes its receipt at `:8019`, after CONFIGURE"
  now names both writes, and "So in both verbs the term reads the prior receipt" now says that of
  `update` alone. One `<w12>` sentence is reworded for the same reason. "A later run's term reads
  that receipt" now says that `update` reads the receipt itself, and that a later `apply` reads its
  rows carried into its own early write. `<w12>`'s sentence naming `TOOL-dRedressedBar-12` keeps
  its words and adds that unit 14 binds that carry ahead of the early write. `<w12>`'s other
  sentences stay as written, and `<w13>` wrote nothing into this paragraph. The paragraph also says
  that a first `apply` never reaches the "With no receipt" reading above it. That reading describes
  the base, and its paragraph is not edited. The base line citations are unchanged. Unit 14's write
  is cited by its spec's S1, because unit 14 is not built yet. No scope or criterion moves.
- rev-7 · 2026-10-16 · §3 · §4 · §5 · a records fix for TOOL-dRedressedBar-28, written by that
  unit's spec-writer pass `<w28>`. The status stays CLOSED. That unit takes unit 10's two static
  terms out of the code-2 block. The install-prefix ban counts the parent home's spelling, no drained
  token names the prefix's parent, and this unit's term asks both homes. §3 Edges gain the hands-off
  to `TOOL-dRedressedBar-28`. §4 row C5 keeps its rejection and adds that unit 28 took it, at its §8
  F1, and that C4 subsumes the terms in every state unit 28 measured but the two its §4 names. §5
  security no longer states that unit 10's term may leave the tree as a peer of this unit's. It says
  the term could until unit 28 took it out, and that this unit's term fails closed there. S2, §4
  "The term" and AC1 record the block as this unit built it, and do not move. No scope or criterion
  moves.

## 10. Reuse audit

`tools/codebase-map/reuse_lookup.py "an outcome probe term that resolves a sibling kit's installed
home from the target's install receipt"` ranked `resolve_kit_dir` as a SEAM with 69 installs, and
`classify_outcome`, `outcome_accepted` and `resolve_entry` below it. Two seams are extended. The
declared-outcome evaluator `classify_outcome` in `tools/govkit/govkit.py` gains one key. The
sibling-kit resolver `resolve_kit_dir`, already inlined in that file and parity-gated, is called
unchanged as the key's evaluator. Unit 9's `check_outcome_states` in `tools/govkit/matrix.py` takes
the rows. The gotchas checklist for the four files selected `a-new-local-collides-in-a-long-function`,
which is why S3 names unbound locals, and `line-claim-matched-over-the-whole-output`, which is why
AC3, AC4 and the arm read one line. It also selected `fixture-inherits-ambient-machine-state`, which is
why the matrix scratch holds `.git`, and `two-answers-to-one-question`, which rejected C1.

The brief and the code disagree in three places. The brief says the base prints the false accept,
but it prints `unclassified`, because the base has no code-2 block (measured, §4). The brief names
three readers, but `check` and the regenerate loop are two more, both through the one evaluator. The
brief's reuse line names the resolver's receipt read, but this unit calls the whole resolver, because
the receipt half alone would be a second copy of it. The recall probe returned TOOL-aWalkedCorpus-9
(`memory/DECISIONS.md:90`), the ruling that a declared outcome may be an accepted stop.
DEPL-dRetiredFork-5 made `check` read the probe, and its inverted-verdict history is why S1 leaves
`outcome_accepted` untouched.

Recall terms used: `python tools/memory-recall/query.py "how does an adopter outcome probe find a
sibling kit installed at a home only the install receipt records" --terms "classify_outcome outcome
probe must_not_exist receipt install.json resolve_kit_dir renamed home accepted stop settings-merge
agent-cap"`
