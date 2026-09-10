# gate-lint — source-hygiene scans over the languages whose failures are SILENT

```toml
feature = "gate-lint"
title = "Two scanners for the failure modes a reader cannot see: PowerShell's decoding traps, and a shell loop that blocks forever"
status = "shipped"
streams = ["tooling"]
decisions = ["TOOL-aLeakedHandle-1"]

[claims]
gate-legs = [
  "shell hygiene (a loop fed by a command substitution)",
  "shell-hygiene selftest",
]
kits = ["gate-lint"]
git-hooks = []
workflow-scripts = []
skill-engines = []
rendered-skills = []
gotcha-classes = []
guides = []
backlog-shards = []
lexicon-verbs = []
[paths]
globs = [
  "tools/gate-lint/*",
  "memory/project/substitution-fed-loops.txt",
]
```

The kit exists for one class of defect: source that a person reads as correct and a machine executes
wrongly, with no error anywhere. `ps-hygiene.py` owns PowerShell's two — case-only identifier
collisions, because PS variable names are case-INSENSITIVE, and a BOM-less script holding non-ASCII,
because 5.1 decodes it as CP1252 and an em dash closes a string early. `sh_hygiene.py` owns the
shell one: a `while … done` loop fed by a heredoc or here-string whose body holds a command
substitution, which reads until an EOF that a surviving grandchild can keep from ever arriving.

## Constraints & why

**A scanner nobody runs proves nothing, and this kit spent its first month proving it.**
`ps-hygiene.py` landed in August 2026 wired to no leg, in a tree with zero `.ps1` files, printing
`OK — 0 .ps1 file(s) clean` and exiting 0. Its own closing review filed that as a finding and it
stayed open. The kit descriptor recorded it honestly as the hole `gate-lint-leg-wiring`, declared
undischargeable by construction — `discharge = { command = ["bash", "-c", "exit 1"] }` — rather than
as a silence. `TOOL-aLeakedHandle-1` discharged it by giving the kit its first two legs; the hole is
gone from the descriptor and the PowerShell half is still unlegged, which is a real gap and is
listed as one below rather than closed by association.

**A kit file names nothing outside itself by literal, and the registry is what that costs.** The
shell scanner grades a repository's own sites, so the list of carried exceptions is nothing but
literals naming files outside the kit — which the carried-prefix ban refuses in a shipped kit body.
So the registry lives at `memory/project/substitution-fed-loops.txt` beside the other gate
registries and arrives as the leg's argv. The same decision is what makes the scanner usable by an
adopter who has their own sites and their own registry, which a hard-coded path could not be.

**The scan grades the LOOP-FEEDING forms alone, and that boundary was measured rather than argued.**
Run over this tree before the ban was wired, the predicate separated four populations that a looser
one would have merged: the loop heredocs carrying a substitution, the substitution-free loop
heredocs whose bodies are plain `$var` expansions, the non-loop heredocs, and the here-strings whose
substitution is an argument rather than a stream. Banning the argument forms would have redded every
assertion helper in the test files. The counts are DERIVED and printed on every run, green included.

**`done < <(…)` is counted and NOT banned, and the count is printed so nobody reads the green line
as covering it.** It carries the same EOF dependency. `TOOL-dScriptedRepeat-13` records that a NUL
stream cannot ride a heredoc, because command substitution strips NUL bytes, so process substitution
is the only form left for those consumers — banning it would contradict a landed decision this kit
does not own.

**The registry is keyed on the DELIMITER, never on a line number.** A line-keyed registry reds on an
edit above the waived line, and a gate whose steady state is red gets bypassed; this repo has
already paid two cycles for one. Set equality runs in both directions with the counts, so a drained
site forces its row out in the same commit instead of leaving a widened exemption behind.

**An empty population is a REFUSAL rather than a pass.** A scan that graded nothing reports the same
zero a clean tree does, and the two are indistinguishable from outside. Both scanners state in their
own headers what they do NOT check, because a structural check reads as a semantic one to everybody
who did not write it.

## Shared seams

- `memory/project/*.txt` — the shrink-only registry convention, shared with
  `install-prefix-waivers.txt`, `unarmed-branches.txt` and `testsuite-count-waivers.txt`. Same
  directory, same both-directions rule. Membership is declared through `PROJECT_REGISTRY_EXTRA` in
  `.memory-tree.conf`, because hygiene check 3 keeps that directory a closed set.
- `tools/gate-legs.json` — the leg manifest is the single source for what the bar runs. The kit
  descriptor declares the same two rows through `{kit}` and `{memory_root}` tokens, and `govkit`
  compares the two spellings in both directions.
- `git ls-files` as the population — the same derived-not-authored rule
  `check-testsuite-counts.sh` and `check-install-prefix.sh` already apply. A hand-kept list goes
  quiet on the file that arrives without being added to it.

## Reuse affordance

seam: `sh_hygiene.scan_file` — reuse for any per-line shell source classifier that must tell a
heredoc, a here-string and a process substitution apart; extend via the `CLASSES` table, which is
what both the report and the gated set are derived from, so a new class is one row and no second
list.

seam: the delimiter-keyed registry pair (`read_registry` + `check_registry`) — reuse for any ratchet
that must land green over a non-compliant population without keying on a line number; extend via the
`DELIMITER` shape test, which is the whole of the malformed-key refusal.

## Affordances

- `python tools/gate-lint/sh_hygiene.py <registry> [root]` — the tree scan. It prints every measured
  population, then the verdict.
- `python tools/gate-lint/sh_hygiene.py --selftest` — the predicate proved in both directions over a
  fixture holding the failing form and its nearest innocent neighbour.
- `python tools/gate-lint/ps-hygiene.py [root]` — the PowerShell scans, and `--selftest` for the
  same proof. Neither is on the bar.
- `memory/project/substitution-fed-loops.txt` — the carried sites. Delete a row when its site is
  drained; the leg reds if you delete one too early or too late.

## Gaps

- **`ps-hygiene.py` is still on no leg.** This kit's original defect, half-closed. There are zero
  tracked `.ps1` files in this repository, so wiring it would put a leg on the bar whose population
  is empty and whose green line proves nothing — the refusal `sh_hygiene.py` now implements would
  red it on the first run. The honest fix is the same refusal in the PowerShell scanner plus a leg
  that an adopter with `.ps1` files receives; neither is built.
- **Nineteen carried sites and nothing that schedules the drain.** The registry ratchets — the count
  can only fall — but a ratchet that never drains is a waiver wearing a ratchet's clothes. The drain
  is a backlog row against the tooling family, not a unit of the build that wired the leg.
- **The scan reads SHAPE, not reachability.** A `$(printf …)` in a loop heredoc body is a hit even
  though nothing about it can hang today. That is deliberate — the shape is what a later edit turns
  dangerous — but it means a registry row is not evidence that its site is safe.
- **One line, one form.** A redirect split across a line continuation is invisible to the predicate.
  None exists in this tree; a repo that writes them gets a silent miss rather than a refusal.
