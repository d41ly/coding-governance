# TOOL-dRedressedBar-28 — install-prefix's two hits at the landing: settings-merge's static absence terms give way to the resolver term, and unit 14's measured landing is spelled through `{prefix}`

**Status:** SPECCED · rev-2 · 2026-10-16 · node d · Tier-2 · base ebce889c · streams tooling · order 22 · ratified 2026-10-16

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-16-build-TOOL-dRedressedBar-28-1-amendments.md](../build/2026-10-16-build-TOOL-dRedressedBar-28-1-amendments.md) | research | — |
| [2026-10-16-prompt-TOOL-dRedressedBar-28-1-spec-writer.md](../prompts/2026-10-16-prompt-TOOL-dRedressedBar-28-1-spec-writer.md) | journal | — |
| [2026-10-16-prompt-TOOL-dRedressedBar-28-brief.md](../prompts/2026-10-16-prompt-TOOL-dRedressedBar-28-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

The landing bar over the prepared merge `30466e12` reds `install-prefix (shipped surface)` on two
kit-path spellings this build wrote. One is the parent-home element of settings-merge's code-2
`must_not_exist` list, from units 10 and 11. The other is a literal landing path in unit 14's comment
in `tools/govkit/govkit.py`. This unit fixes both at their root, with the checker, its population and
its no-waiver rule unchanged, so the owner's landing ask can complete. The descriptor's absence then
rests on unit 11's resolver term alone, which already asks every home the adopter's resolver probes.

## 2. Scope (IN)

- **S1** — The code-2 `[[outcome]]` block of `tools/govkit/entries/settings-merge.kit.toml` (`:46-50`)
  keeps exactly two probe keys: `must_exist = "{prefix}/settings-merge.py"` and
  `must_not_resolve = "{prefix}/hooks/agent-cap.js"`. Its `must_not_exist` list, both elements, is
  retired from this block. `code`, `means` and `ok` do not move, and the key stays in the engine's
  vocabulary for the four other descriptors that declare it. Observed by AC1, AC2, AC3 and AC4.
  - **Readers:** the term is one block's use of a key, and the key stays. The inventory was read at
    `b1eb9737` with `grep -rn "must_not_exist" tools/` over the tree.
    by name: `classify_outcome` in `tools/govkit/govkit.py` evaluates every key
    `OUTCOME_PROBE_KEYS` lists, and `derive_probe_paths` and the key rule in
    `tools/govkit/matrix.py` read the key through that mapping. None of them spells settings-merge's
    term, and each keeps reading the key in `tools/codebase-map/kit.toml`, `tools/lexicon/kit.toml`,
    `tools/memory-tree/kit.toml` and `tools/unattended/kit.toml`. The block's own comment spells the
    term, and S2 rewrites it. Specs 9, 10, 11 and 13 spell it as records, and S4 corrects the two
    sentences the change makes false.
    by value: `classify_outcome` reads the term's two paths at every settings-merge exit 2, and so
    feeds `outcome_accepted` in `_cmd_apply`'s CONFIGURE step and `_cmd_update`'s gained loop. The
    verdict it fed is read by the six settings-merge rows of `check_outcome_states` in
    `tools/govkit/matrix.py` and by the `[dRB-9]`, `[dRB-11]` and `[dRB-12]` checks in
    `tools/govkit/selftest.py`. AC2 and AC3 observe those verdicts unmoved.
- **S2** — The comment directly above that block (`:33-45`) states the absence as the one term it
  now is: what `must_not_resolve` asks, in the resolver's order, and that an exit 2 stays a failure
  wherever the resolver finds the hook. It says the two static terms stood until this unit, why they
  went, and the one measured state that reads differently since. No line of it spells a kit segment
  followed by a file except behind a drained token. Observed by AC1 and AC4.
- **S3** — The unit-14 comment in `tools/govkit/govkit.py` (`:7945-7960`, the hit at `:7950`) spells
  the measured landing through agent-cap's own landing spelling: `{prefix}/hooks/agent-cap.js` with
  `{prefix}` resolved to `scripts`. The measured configuration `[kit.agent-cap] prefix = "scripts"`
  and the rest of the block keep their words, and no code line moves. Observed by AC1 and AC5.
- **S4** — The record, in a spec-writer pass of its own, `<w28>`, run once §8 F1 is resolved and
  before the build pass. Specs 10 and 11 each take one rev bump, CLOSED status unchanged, with a
  revision line naming `TOOL-dRedressedBar-28`. Each §3 Edges block gains the hand-off line to this
  unit. Spec 11's §4 row C5 and its §5 security clause on unit 10's parent-home term are corrected
  as §4 "The CLOSED specs, read" states. No other spec moves. Observed by AC6.

## 3. Non-goals (OUT)

- No change to `tools/check-install-prefix.sh`, to its population or to its drained spellings, and
  no waiver (brief non-goal).
- No change to `tools/settings-merge.py` or to any copy of `resolve_kit_dir` (brief non-goal).
- No change to `OUTCOME_PROBE_KEYS` or `classify_outcome`. The `must_not_exist` key stays in the
  vocabulary, which four other descriptors use.
- No edit to `tools/govkit/matrix.py` or `tools/govkit/selftest.py`. No arm's verdict moves (§4 "The
  arms that grade the block"). The matrix's comments and labels about "static homes" describe the
  resolver's two probes, which still stand.
- No change to how `classify_outcome` builds the term's `<here>`. Closing the symlinked-prefix
  divergence §4 measures is §8 F1 option (b), its own mechanism.
- No corrections to specs 9 and 13. Their sentences about the static terms record what those units
  built and still read true of that history (§4 "The CLOSED specs, read").
- No kit version and no symbol-index move: both product files sit under `{prefix}/govkit`, which the
  registry exempts as the deployer itself (`tools/govkit/registry.toml:295-297`), and no function or
  class moves.
- No `tools/unattended/` self-test suite runs (standing owner instruction, 2026-08-23), and no push
  beyond the owner's landing ask.

### Edges

- **consumes-from** `TOOL-dRedressedBar-10` — the parent-home element of the code-2 list, which S1
  takes out of the block, and the parent-home row of settings-merge's `check_outcome_states` call,
  which AC3 reads unchanged. Its spec takes the reciprocal line at `<w28>`.
- **consumes-from** `TOOL-dRedressedBar-11` — the `must_not_resolve` term, which S1 leaves as the
  block's whole absence, and its two receipt rows in the matrix, which AC3 reads. Without the term, S1
  would leave an accepted stop declared by a presence alone, and the matrix's REFUSED rows would read
  ACCEPTED. Its spec's row C5 and §5 clause are what `<w28>` corrects.
- **hands-off** external — the divergence between the term's lexical `<here>` and the adopter's
  resolved directory on a target whose prefix directory is a symlink or a junction. Per §8 F1, the
  build's wrap-up carries it to the owner as a follow-up, option (b).

## 4. Design

Every line number below was read at `b1eb9737`, the branch tip this spec was grounded on, whose
product files equal the prepared merge's for both files this unit touches.

### The two hits, measured

The checker's counter reads five rules over each line (`tools/check-install-prefix.sh:44-53`). Rule
3 counts `<kit>/<file>.<ext>` under any literal prefix and under a derived base, unless the text
before it ends in a drained spelling (`DRAINED`, `:275`). Run in-process over the two files (the
counter probe below), it prints exactly the brief's two lines:

| File | Spelling | Why it counts |
|---|---|---|
| `tools/govkit/entries/settings-merge.kit.toml:48` | `"{prefix}/../hooks/agent-cap.js"` | `hooks/` follows `../`, which no drained token ends |
| `tools/govkit/govkit.py:7950` | `` `scripts/hooks/agent-cap.js` `` | `hooks/` follows the literal prefix `scripts/` |

No drained spelling can name the prefix's parent. The entry context holds `prefix`, `kit_id`, `kit`,
the target's answers and `memory_root` (`tools/govkit/govkit.py:1433-1495`), and `{kit}` is
`{prefix}/<entry id>`. Every spelling of the parent home therefore reaches `hooks/agent-cap.js`
after `../` or after a token the counter does not drain. So the element cannot be respelled, and it
leaves the block or the leg stays red.

### Is the `must_not_exist` term redundant? Measured

The brief's candidate: `must_not_resolve` calls `resolve_kit_dir("hooks", "agent-cap.js",
target/<prefix>)` (`tools/govkit/govkit.py:6600`), and the resolver reads the receipt, then probes
`<here>/hooks` and `<here>/../hooks` (`:224-227`). That is lexically both homes the static list names.
Two differences remain. `must_not_exist` holds when `(target / resolved).exists()` is false (`:6593`),
and the resolver accepts a home only when the anchor `is_file()` (`:226`). And the resolver takes
the term's `<here>` with `.absolute()`, never `resolve()` (`:209`), while the static element's `..`
is walked by the operating system.

A probe imported gov's `govkit.py` and classified rc 2 over fresh scratch targets under `%TEMP%`,
with the shipped block and with the same block minus `must_not_exist` held in memory. Each target
holds `tools/settings-merge.py` and a `.git` directory unless its row says otherwise, and
settings-merge's `{prefix}` is `tools`. Measured 2026-10-16 at `b1eb9737`, PINNED.

| # | State | At `b1eb9737` | After S1 |
|---|---|---|---|
| 1 | nothing else | ACCEPTED | ACCEPTED |
| 2 | the hook at `tools/hooks/agent-cap.js` | REFUSED | REFUSED |
| 3 | no file at all | REFUSED | REFUSED |
| 4 | the hook at the parent home, `hooks/agent-cap.js` | REFUSED | REFUSED |
| 5 | the hook at `guard/agent-cap.js`, one receipt row recording it | REFUSED | REFUSED |
| 6 | that receipt row, the file absent | ACCEPTED | ACCEPTED |
| 7 | the hook at the parent home, no `.git`, no receipt | REFUSED | REFUSED |
| 8 | the hook at `scripts/hooks/agent-cap.js`, one receipt row recording it | REFUSED | REFUSED |
| 9 | the hook beside it, a receipt holding `{` | REFUSED | REFUSED |
| 10 | a receipt holding `{`, no hook | ACCEPTED | ACCEPTED |
| 11 | a DIRECTORY at `tools/hooks/agent-cap.js` | REFUSED | ACCEPTED |
| 12 | a DIRECTORY at `hooks/agent-cap.js` | REFUSED | ACCEPTED |
| 13 | `tools` a junction to a directory whose parent holds `hooks/agent-cap.js` | ACCEPTED | ACCEPTED |
| 14 | `tools` a junction, the hook at the target's own `hooks/agent-cap.js` | REFUSED | REFUSED |

The brief's four questions, answered from that table and the code:

| Question | Answer |
|---|---|
| `exists()` against `is_file()` | rows 11 and 12 move. gov's `tools/settings-merge.py`, run in a scratch target holding a directory at either home, exits 2 with `refusing to wire agent-cap — tools/no-agent-cap-kit-resolved/agent-cap.js does not exist` (measured). Its resolver missed (`tools/settings-merge.py:192`), so the stop's declared meaning is the adopter's own reason, and after S1 the block reads it that way. At `b1eb9737` it refuses an exit whose cause is the one the block declares |
| a missing token | no move. Every term spells only `{prefix}`, which every entry context carries (`tools/govkit/govkit.py:1470`, `:1480`), and a miss on any term fails the whole block (`:6588-6591`) |
| the receipt-less case | no move. Rows 1 to 4 and 7: with no rows the resolver asks the same two static homes |
| the arms over this block | no move. The table below |

**The symlinked prefix, which the table cannot show on this host.** The adopter resolves its own
directory with `Path(__file__).resolve().parent` (`tools/settings-merge.py:192`), so on a target whose
prefix directory is a link it asks the PHYSICAL parent. Row 13 measures Windows: the static element's
`..` is folded lexically, so neither block asks the physical parent today. On POSIX the kernel walks
`..` through the link, so the static element asked the physical parent, as the adopter does. After S1,
a hook at the physical parent of a linked prefix, recorded by no receipt, with the adopter exiting 2
for another cause, reads ACCEPTED where it read REFUSED. UNVERIFIED on this host, which has no POSIX
symlink. It is §8 F1's residual.

So the candidate is refuted as stated, and confirmed in effect. Removing the term moves no state an
arm or a fixture in the tree stages. It moves two states toward the adopter's own reading (rows 11 and
12), and it gives up one POSIX-only state that the Windows reading already lacks.

### The block after S1

```toml
[[outcome]]
code = 2
probe = { must_exist = "{prefix}/settings-merge.py", must_not_resolve = "{prefix}/hooks/agent-cap.js" }
means = "no-agent-cap-to-wire"
ok = true
```

The matrix's class rule still finds a presence on this accepted stop
(`tools/govkit/matrix.py:219-224`), and its key rule still finds every key in the mapping.

### The comment above the block (S2)

Lines 33 to 37 and 44 to 45 of the descriptor keep their words. Lines 38 to 43, from "wired. The
PRESENCE" through "an exit 2 stays a failure.", become this text, or text saying the same within the
same width:

```toml
# wired. The PRESENCE, `must_exist`, pins `{prefix}` to the adopter's own directory. The ABSENCE
# is one term, `must_not_resolve`, which asks the adopter's own resolver: the receipt,
# `.governance/install.json`, then `{prefix}/hooks`, then the `hooks` directory in `{prefix}`'s
# parent (TOOL-dRedressedBar-11). With the hook wherever the resolver finds it, an exit 2 stays a
# failure. Two `must_not_exist` terms named the two static homes again until TOOL-dRedressedBar-28
# retired them: the resolver already asks both, and the parent home's spelling is a kit path the
# install-prefix ban counts. Since then a non-file named `agent-cap.js` at a static home reads as
# absent, as the adopter reads it.
```

That text, with the block after S1 below it, was run through the counter probe and reads clean
(measured 2026-10-16). The probe line keeps its current width; this file's existing line 48 is
already wider than 100 columns.

### The govkit.py comment (S3)

At `:7949-7951` the measured clause becomes, wrapped within the block's `# ---- ` margin and 100
columns:

```text
Measured: `[kit.agent-cap] prefix = "scripts"` landed the hook at agent-cap's
`{prefix}/hooks/agent-cap.js` with `{prefix}` resolved to `scripts`, and settings-merge exited 2 ...
```

`{prefix}/hooks/agent-cap.js` is how agent-cap's own descriptor spells that landing
(`tools/hooks/kit.toml:24`), so the comment keeps the measured value and names it the way the engine
resolved it. A scratch copy of `govkit.py` carrying this wording reads clean through the counter
probe (measured 2026-10-16). The sentence before and the one after are unchanged.

### The arms that grade the block

| Arm | State it stages | Verdict at `b1eb9737` | After S1 |
|---|---|---|---|
| matrix `check_outcome_probes`, settings-merge's six rows (`tools/govkit/matrix.py:342-349`) | rows 1 to 6 of the table above | each as its label states, all true | the same, all true (AC3) |
| `[dRB-9]` (`tools/govkit/selftest.py:3332-3355`) | an update gaining settings-merge, agent-cap absent everywhere | the declared stop | unchanged (row 1) |
| `[dRB-11]` fixture A, `[dRB-12]` AC2 (`:3379-3420`) | a receipt-homed hook and a malformed settings file | refused, `cannot read` | unchanged (row 5) |
| `[dRB-11]` A-absent (`:3421-3432`) | no hook, a malformed settings file | the declared stop | unchanged (row 1) |
| `[dRB-11]` fixture B (`:3434-3494`) | the hook at `scripts/hooks/agent-cap.js` with its receipt row | refused, `cannot read` | unchanged (row 8) |

The matrix's recorder probe reads 39 labels, every one true, over the shipped block and over the
block minus `must_not_exist`; with `must_not_resolve` dropped as well, the hook-beside, parent-home
and receipt rows record false (measured 2026-10-16). `[dRB-14]` and `[dRB-15]` reach adopter exit 0,
where the block is never consulted. No arm stages a non-file hook or a linked prefix, so no arm
moves.

### The CLOSED specs, read

Specs 9, 10, 11, 13 and 17 were read whole for every sentence about the block's absence terms. Spec
17 carries none. A sentence recording what a unit built at its pass is history and stays. A sentence
stating, in the present, that a static term stands beside the resolver term, or that the resolver
term does not reach a state it does reach, is made false and is corrected at `<w28>`.

| Spec | Sentence | Disposition |
|---|---|---|
| 9 | S1, §4's block and term table, AC1, AC4 and its matrix arm line | history of unit 9's block; stays |
| 9 | §4 "What it does not check" and §5 security on unit 10's narrowing | true of the chain; stays |
| 10 | S22, §4 "S22 — the false-accept routes", AC15 to AC17, §8 F1 | history of unit 10's pass; stays |
| 10 | §3 Edges | gains a hand-off line to this unit (S4) |
| 11 | S2, §3, §4 "The term", AC1 | history of unit 11's pass; stays |
| 11 | §4 row C5, "Rejected; kept" | corrected (S4) |
| 11 | §5 security, "as unit 10's parent-home `must_not_exist` term may. Each fails closed there" | corrected (S4) |
| 11 | §3 Edges | gains a hand-off line to this unit (S4) |
| 13 | S22 and its code-site row 22 | history of unit 13's comment; stays |

`<w28>` writes these four texts, under F1 option (a) and its reading of rows 11 and 12. Each is shown
as it lands, so the fence holds the spec bytes verbatim.

```markdown
<!-- 1. spec 10, §3 Edges, a new last bullet -->
- **hands-off** `TOOL-dRedressedBar-28` — the parent-home element of the code-2 `must_not_exist`
  list, which that unit takes out of the block because no drained spelling names the prefix's
  parent, and the parent-home row of `check_outcome_states`, which its AC3 reads unchanged.

<!-- 2. spec 11, §3 Edges, a new last bullet -->
- **hands-off** `TOOL-dRedressedBar-28` — the code-2 block's two static terms, which that unit takes
  out because this unit's term asks both homes, and this spec's row C5 and §5 security clause,
  which its spec-writer pass corrects.

<!-- 3. spec 11, §4 row C5, the whole verdict cell -->
Rejected; kept. Taken by `TOOL-dRedressedBar-28`, at its §8 F1, once the install-prefix ban counted the parent home's spelling. C4 subsumes the terms in every state that unit measured but the two its §4 names

<!-- 4. spec 11, §5 security: "as unit 10's parent-home `must_not_exist` term may. Each fails closed there" becomes -->
as unit 10's parent-home `must_not_exist` term could until `TOOL-dRedressedBar-28` took it out of
the block. The term fails closed there
```

Each spec takes one revision line, `rev-7 · <date>` followed by its scope tokens, `§3` for spec 10
and `§3 · §4 · §5` for spec 11. Each says it is a records fix for `TOOL-dRedressedBar-28`, written by
that unit's spec-writer pass `<w28>`, with status CLOSED unchanged. If F1 resolves as (b), the texts
are the same, and spec 11's C5 cell also names the added unit.

### The counter probe

AC1's program, saved as a file under `%TEMP%` and run from the worktree root with the paths to grade
as its arguments. It execs the counter of `tools/check-install-prefix.sh` unchanged, in `--check`
mode, with the kit names derived as the shell derives them for gov's `tools/` root and the extension
class read from the script's own `EXT=` line. It grades only the files it is given and loads no
templates, so it is no stand-in for the leg's 406-file population; the leg itself is §7's.

```python
import io, os, re, subprocess, sys
src = open("tools/check-install-prefix.sh", encoding="utf-8").read()
body = src.split("<<'BAN_PY' || true\n", 1)[1].split("\nBAN_PY\n", 1)[0]
ext = re.search(r'^EXT="([^"]+)"', src, re.M).group(1)
listed = subprocess.run(["git", "ls-files", "--", "tools/*/*"], capture_output=True,
                        text=True).stdout.splitlines()
kits = sorted({p.split("/")[1] for p in listed if p.count("/") >= 2})
os.environ.update(BAN_KITS="\n".join(kits), BAN_EXT=ext, BAN_TEMPLATES="")
sys.stdin = io.StringIO("\n".join(sys.argv[1:]) + "\n")
sys.argv = ["ban", "--check"]
exec(compile(body, "BAN_PY", "exec"))
```

### Inventory

None minted: no identifier, key, file or label is added.

### Rollout

Tier-2 by the manifest's tier rule (`memory/guides/SESSION-KICKOFF.md:111-117`): the change moves
the declared outcome contract of the settings-merge entry, so one state classifies differently. No
receipt, conf or deploy shape moves and no target needs an upgrade step. The next `apply` or
`update` reads the new descriptor.

### Files touched (estimate)

- `tools/govkit/entries/settings-merge.kit.toml`
- `tools/govkit/govkit.py`
- `memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-10.md`, at `<w28>`
- `memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-11.md`, at `<w28>`
- `memory/builds/dRedressedBar/build/`, for this unit's acceptance ledger

### Alternatives rejected

Each candidate was written down with the test that could make it lose, and the pick is M3's.

| Candidate | The test that rejected it | Verdict |
|---|---|---|
| C1 — the whole `must_not_exist` term out of the block | rows 1 to 10 and 13 to 14 equal, rows 11 and 12 toward the adopter, the POSIX residual named | Chosen (§8 F1) |
| C2 — only the parent-home element out, unit 9's first element kept | row 11 stays REFUSED while row 12 reads ACCEPTED: one block reading the resolver's two static homes by two file tests, two answers to one question | Rejected |
| C3 — the parent-home element respelled through a drained token | no context token names the prefix's parent (`tools/govkit/govkit.py:1433-1495`), and every spelling reaches `hooks/agent-cap.js` after `../`, which the counter probe counts on the shipped line | Fails the brief's acceptance |
| C4 — the `h` of the parent-home `hooks` written as a TOML unicode escape (a backslash, then `u0068`), which rule 3's lookbehind does not see | the counter probe reads it clean (measured). It keeps the literal the ban exists to refuse, an exemption a pass grants itself, which the checker's header rules out | Rejected by the charter's gate rule |
| C5 — a new context token for the prefix's parent | the counter drains five spellings only (`:275`), and the probe counts `{prefix_parent}/hooks/agent-cap.js` (measured). Draining it changes the checker | Fails a non-goal |
| C6 — `classify_outcome` builds the term's `<here>` as the adopter builds its own directory | closes the linked-prefix divergence on both platforms, and is a second mechanism in the evaluator's contract | §8 F1 option (b) |

## 5. Production-readiness checklist

- security — Rows 11 and 12 newly accept an exit 2 where a non-file sits at a static home. The
  adopter refused before writing, so nothing is wired, and agent-cap's own entry still fails
  wherever it is selected. The POSIX linked-prefix state newly accepts an exit 2 whose cause was a
  malformed or unwritable settings file, which is the false-accept class unit 11 closed, narrowed to
  a hook no receipt records at a linked prefix's physical parent. F1 puts it to the owner. No write
  path, input or egress surface moves.
- perf / scale — N/A — two fewer `exists` calls per settings-merge exit 2.
- error / empty / loading states — An absent, unreadable or malformed receipt still reads as no
  rows, so the term asks the two static homes, as rows 1, 7 and 10 show.
- observability — Unchanged output shapes. An accepted stop prints `no-agent-cap-to-wire` as before.
- risks — Rows 11 and 12 and the POSIX residual are the whole behavioural change, each named in the
  descriptor comment or here. A reader of specs 10 and 11 would believe the static terms still stand
  until `<w28>` lands, which is why S4 runs before the build pass.
- testing — AC1 to AC6 are direct probes: the checker's own counter run in-process, in-process engine
  and matrix calls, greps and diffs. No suite runs. The `govkit acceptance matrix` leg runs in the
  landing bar's declarations chunk. The `govkit selftest` leg is a self-test, held under the owner's
  "land it without self tests".
- migration — N/A — no receipt, conf or deploy field moves.
- user docs — N/A — `help/` holds `README.md`, `measure-legs.md` and `roles.md`, and none covers
  govkit or the accepted stop.

## 6. Acceptance criteria

`<p28>` is this unit's build pass commit and `<w28>` its spec-writer pass commit. `<s10>` and `<s11>`
are the spec files of units 10 and 11. Every command runs from the worktree root, and every scratch
target is a fresh directory under `%TEMP%`.

- **AC1** — When the counter probe of §4, `ban.py`, runs as `python ban.py tools/govkit/govkit.py
  tools/govkit/entries/settings-merge.kit.toml`, it exits 0 and prints one line,
  `install-prefix: clean — 2 tracked file(s) graded, 0 render(s) left out as matching their template, 0 kit-path spelling(s) on 0 line(s)`.
  Red when: run over the two files as `git show b1eb9737:<path>` writes them to a scratch directory,
  it exits 1, prints the brief's two hit lines against the scratch paths, and ends
  `2 kit-path spelling(s) on 2 line(s)`.
  fixture: the red half was observed at spec time on `b1eb9737` with the probe in `--list` mode.
  figure: the counts are DERIVED by the counter at observation.
- **AC2** — When a python program imports `tools/govkit/govkit.py`, loads settings-merge's descriptor
  with `govkit.load_toml` from the tip and from `git show <p28>~1:tools/govkit/entries/settings-merge.kit.toml`,
  and prints `outcome_accepted(2, classify_outcome(t, d, target_context(t, {}, "settings-merge", d), 2), declares_outcome_for(d, 2))`
  over a scratch target per row 1 to 12 of §4's table, every row reads the same at both commits
  except rows 11 and 12, which read REFUSED at `<p28>~1` and ACCEPTED at the tip. gov's
  `tools/settings-merge.py`, copied into a scratch target with a directory at
  `tools/hooks/agent-cap.js` and run from its root, exits 2 with `refusing to wire` on stderr.
  Red when: any of rows 1 to 10 differs, or rows 11 and 12 still read REFUSED at the tip, which
  means a `must_not_exist` term still stands in the block.
  fixture: rows 13 and 14 need a junction, so they are measured where the host allows it and are not
  required; the POSIX residual is UNVERIFIED and observed by no criterion.
- **AC3** — When a python program imports `tools/govkit/matrix.py`, replaces its module-level `check`
  with a recorder, and calls `check_outcome_probes` on a scratch directory, every recorded label is
  true. The eight labels opening `settings-merge exit 2` are the eight it records at `<p28>~1`, with
  the same verdicts.
  Red when: with `govkit.read_descriptors` wrapped to take `must_not_resolve` out of settings-merge's
  code-2 probe as well, the labels for the hook beside it, the prefix's parent home only and a hook
  only the receipt locates record false, so a block left with no absence term cannot pass.
  figure: 39 labels at `b1eb9737`, PINNED 2026-10-16; DERIVED at observation, and equal at both
  commits.
- **AC4** — When `grep -n -A5 '^\[\[outcome\]\]' tools/govkit/entries/settings-merge.kit.toml` runs,
  it prints one block: `code = 2`,
  `probe = { must_exist = "{prefix}/settings-merge.py", must_not_resolve = "{prefix}/hooks/agent-cap.js" }`,
  `means = "no-agent-cap-to-wire"` and `ok = true`.
  `grep -c 'must_not_exist =\|three terms\|any of the three' tools/govkit/entries/settings-merge.kit.toml`
  prints 0, and `sed -n '/^\[adopt\]/,/^\[\[outcome\]\]/p' tools/govkit/entries/settings-merge.kit.toml`
  carries `must_not_resolve`, `.governance/install.json` and `TOOL-dRedressedBar-28`.
  `git diff <p28>~1 <p28> -- tools/govkit/entries/settings-merge.kit.toml` touches only the comment
  above the block and its probe line.
  Red when: the block keeps a `must_not_exist` key, or the comment still counts three terms; the
  count reads 3 at `b1eb9737`.
- **AC5** — When `grep -c 'scripts/hooks/agent-cap.js' tools/govkit/govkit.py` runs, it prints 0.
  `sed -n '/THE RECEIPT, WRITTEN AHEAD OF CONFIGURE/,/bound HERE, once/p' tools/govkit/govkit.py`
  carries `prefix = "scripts"` and `{prefix}/hooks/agent-cap.js`.
  `git diff <p28>~1 <p28> -- tools/govkit/govkit.py | grep -E '^[+-] ' | grep -vE '^[+-] +# ---- '`
  prints nothing, so every changed line is a line of that comment, and no `def` or `class` moves.
  Red when: the literal survives, as at `b1eb9737`, where the count reads 1, or the measured
  `scripts` is lost from the block, or a code line moves.
- **AC6** — When `sed -n '/^### Edges/,/^## 4/p' <s10>` and the same over `<s11>` run at `<w28>`, each
  prints one hands-off bullet naming `TOOL-dRedressedBar-28`. `grep -n '^| C5 ' <s11>` prints a row
  carrying `TOOL-dRedressedBar-28`, and `grep -c 'term may. Each fails closed' <s11>` prints 0. Each
  status header reads `CLOSED · rev-7`, each §9 ends with a rev-7 line naming
  `TOOL-dRedressedBar-28`, and `git diff --stat <w28>~1 <w28>` names no file outside
  `memory/builds/dRedressedBar/`.
  Red when: spec 11 still states the term may leave the tree, where the count reads 1 at
  `b1eb9737`, or either spec carries no hand-off line back to this unit, which the edges join reads
  as a declared edge the other author never saw.

## 7. Gates

`install-prefix (shipped surface)` · `memory hygiene` · `govkit acceptance matrix` · `govkit selftest` · `govkit refusal join` · `recall floor` · `recall floor arms`

The first leg's red half is the brief's output over `30466e12`, and the main loop reads it green at
the landing bar. The three govkit legs and `recall floor arms` are owed by the `{prefix}/govkit/`
guard, and `recall floor` and `recall floor arms` by the `memory/` guard, each tripped by a path under
§4's Files touched. `govkit selftest` is in the selftests chunk, held under the owner's landing ask,
and AC2 observes the states its settings-merge arms stage. This unit adds no arm and moves none.

## 8. Open questions

- **F1 — The owner picked unit 10's F1 as "(c) Narrow + receipt probe" on 2026-10-14, and unit 11's
  row C5 kept the narrowing's static terms for that reason. The landing needs the narrowing's
  parent-home spelling gone. Is the parent home refused through unit 11's resolver term alone, with
  the two named state changes?**
  - (a) Take the whole `must_not_exist` term out of the block (C1). The parent home stays refused
    through the resolver, every arm and fixture state reads as before, rows 11 and 12 read the
    adopter's way, and the POSIX linked-prefix residual is recorded in §4 and §5. S1 to S4 stand as
    written.
  - (b) As (a), and ADD a unit that makes `classify_outcome` build the term's `<here>` as the adopter
    builds its own directory (C6), which closes the linked-prefix divergence on both platforms,
    including the Windows half that stands today. This unit is unchanged; the ADD is an owner turn.
  - (c) Keep the narrowing term. No drained spelling names the parent home (C3, C5), so the leg
    stays red and the landing refuses, which fails the brief's acceptance (M3 veto 1). Listed so the
    reason is on record.
  Recommendation: (a). It satisfies every criterion written here, and it keeps the owner's
  narrowing in force as behaviour at every state this tree's arms and fixtures stage. It spends no
  unit on a configuration no install has been observed in, whose Windows half already stands. (b)
  is the follow-up if the owner wants the linked-prefix case closed.
  RESOLVED (agent, 2026-10-16, delegated): (a). Decided by the build's main loop under the owner's
  2026-10-16 ask "land it without self tests", as relayed to this spec's writer at `<w28>`. Option
  (c) cannot land. Option (b) is an owner turn, so it goes to the build's wrap-up as a follow-up and
  not into this build. S1 to S4 stand as written.

## 9. Revision log

- rev-1 · 2026-10-16 · initial draft from the unit-28 brief. The brief's redundancy candidate was
  probed in-process over 14 states at `b1eb9737` and refuted for two (`exists` against `is_file`)
  plus one POSIX state the host cannot stage. Both respellings and four rejected candidates were run
  through the checker's own counter. One fork, F1, is left to the owner because the change takes out
  the spelling of an owner pick.
- rev-2 · 2026-10-16 · §8 · §3 · §4 · F1 resolved as (a), marked `RESOLVED (agent, 2026-10-16,
  delegated)`. The main loop decided it under the owner's 2026-10-16 ask "land it without self
  tests". Option (b) goes to the build's wrap-up as a follow-up. The §3 external hand-off says so,
  §4 row C1 reads "Chosen (§8 F1)", and the header carries `ratified 2026-10-16`. Written at
  `<w28>`, alongside S4. No scope or criterion moves.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "an outcome probe that asks whether a sibling kit's file
is absent from every home the adopter's resolver probes"` ranked `resolve_kit_dir` a SEAM, fan-in 11
with 71 installs. It is the seam this unit reuses, unchanged: unit 11's `must_not_resolve` term
already calls it from `classify_outcome` (`tools/govkit/govkit.py:6600`), and S1 leaves that term as
the block's whole absence. That is also the remedy the checker prints, "route a sibling kit through
resolve_kit_dir". No new seam is built, and the evaluator, the vocabulary and the matrix are reused
as they stand. The respelling in S3 reuses agent-cap's own landing spelling (`tools/hooks/kit.toml:24`).
The precedent `memory/builds/aSweptBar/` applied each ban's own printed remedy to the offenders it
named, with no predicate changed, which is the shape here.

The gotchas checklist for the two product files selected `two-answers-to-one-question`, which rejected
C2, and `a-folded-field-leaves-its-row-shape-docs-behind`, which is why S2 rewrites the comment and S4
corrects spec 11. It also selected `fixture-passes-by-finding-nothing`, which is why AC1's and AC3's
red halves were observed, and `staged-break-substitutes-a-synthetic-value`, which is why AC3 stages
its break on the shipped descriptor rather than a fixture block.

The brief and the code disagree in two places. The brief says the resolver "already asks both static
homes", which holds lexically but not for a non-file anchor or a linked prefix on POSIX (§4). The
brief says "the govkit selftest's arms over this outcome block"; the arms that grade its verdict by
state are in `tools/govkit/matrix.py`, under the `govkit acceptance matrix` leg, and the selftest's
blocks drive it end to end. The recall probe returned `TOOL-aRepatriatedFork-23`, the ban's
population rule, and `TOOL-dRedressedBar-4`, this build's other install-prefix drain, along with
specs 9 to 11 of this build.

Recall terms used: `python tools/memory-recall/query.py "how is a kit path spelled in a shipped
file so the install-prefix ban drains it, and is a static absence term redundant beside the resolver
term" --terms "install-prefix drained token kit path spelling must_not_exist must_not_resolve
resolve_kit_dir static home parent home settings-merge agent-cap outcome probe"`
