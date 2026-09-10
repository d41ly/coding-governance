# gate-lint — drop-in source-hygiene scans

Project-agnostic checks for classes that make a script misbehave **silently**.

The kit declares **two** gate legs of its own, both in `kit.toml`: `shell hygiene (a loop fed by a
command substitution)` and `shell-hygiene selftest`. It declared NONE until
`TOOL-aLeakedHandle-1`, and the PowerShell half below is still on no leg anywhere — see
*What is still unwired*. Anything not declared there is the consuming project's to wire, and the
two-line adoption step for that is documented here rather than left implicit.

## ps-hygiene.py

```bash
python3 tools/gate-lint/ps-hygiene.py [root]   # exit 0 clean, 1 findings, 2 usage
python3 tools/gate-lint/ps-hygiene.py --selftest
```

Scans **every** `.ps1` under `root` for two classes:

- **Case-only identifier collisions.** PowerShell variable names are case-INSENSITIVE, so `$LEGS`
  and `$legs` are ONE variable. Upstream this bit one file three times: `$LEGS = @($legs.legs)`
  overwrote a parsed manifest with its own sub-array, and `foreach ($sel in ...)` clobbered a `$SEL`
  selection map — which also disabled the backstop that read `$SEL`, because a guard sharing a
  variable with the thing it guards is not a guard.
- **BOM-less scripts containing non-ASCII.** PowerShell 5.1 decodes them as CP1252, so an em dash
  inside a double-quoted string becomes three chars ending in U+201D — which PowerShell accepts as a
  string delimiter. It closes the string early and desynchronises the parser. Every text-mode read
  hides this, so the check is byte-level.

## sh_hygiene.py

```bash
python3 <tool-root>/gate-lint/sh_hygiene.py <registry-path> [root]   # exit 0 clean, 1 findings, 2 refusal
python3 <tool-root>/gate-lint/sh_hygiene.py --selftest
```

Scans **every tracked** `*.sh` for one class: a `while … done` loop whose input redirect is an
unquoted heredoc, or a here-string, whose body holds a command substitution. `$( )` reads until
EOF; EOF arrives when the LAST inherited write end closes, not when the direct child exits. Where
the substituted command is a shell FUNCTION the substitution forks a subshell which forks the real
program, so the reader waits on a grandchild — and under MSYS that is not reliably the write end
that closes. Measured in the kit's home repository: a merge-bar leg sat at zero CPU for 63 minutes
with the forked subshell holding both ends of its own pipe and no descendant alive. The remedy is
a scratch FILE — redirect the walk to it, then read it by redirect, which keeps the loop in the
current shell so a `return` inside it still returns from the enclosing function.

It takes the registry path as an ARGUMENT and derives its population from `git ls-files`, so it
names nothing outside the kit by literal. The registry itself SHIPS: `kit.toml` seeds an empty one
to `{memory_root}/project/substitution-fed-loops.txt`, which is where the leg's argv points, and
`seed` means it is copied once and owned by that repository from then on — a later install never
overwrites the rows an adopter has declared. Declaring the leg without shipping the file is what
`TOOL-aLeakedHandle-1` first landed, and it made `govkit apply` exit 1 at every adopter with the leg
withheld and no coverage recorded; the arm that now catches that class is `govkit selfcheck`'s
`gate legs` check. The registry is shrink-only and keyed on the file plus the redirect delimiter,
never on a line number: set equality runs in both directions, so a new site fails AND a row whose
site is gone fails. Fill it on the first install from what the leg reports — the seeded header says
how.

It counts `done < <(…)` and prints the count WITHOUT gating it. That form carries the same EOF
dependency, and it is the only one left for a NUL stream, because command substitution strips NUL
bytes. An empty population is a refusal rather than a pass.

## Wiring it into a host project

Add it as a gate leg wherever that project enumerates them, e.g. an entry in a leg manifest, a CI
step, or a pre-commit hook:

```bash
python3 tools/gate-lint/ps-hygiene.py . || exit 1
```

Run `--selftest` in the same place. Per `coding-governance-agents.template.md` §7, a gate
whose failing case has never been observed is not a gate — `--selftest` is how these prove they
can still fail after a refactor.

## What is still unwired

`ps-hygiene.py` is on no leg, here or anywhere. That is deliberate and it is a gap rather than a
decision: the kit's home repository has zero tracked `.ps1` files, so a leg over it would report a
green line produced by an empty population — which is the shape both scanners exist to refuse, and
which the shell scanner now refuses outright. Wiring it earns its place in a repo where PowerShell
exists.

**Adoption is not automatic.** A repo with no `.ps1` files gets `0 files clean`, which is honest but
proves nothing; the scan only earns its place where PowerShell exists.
