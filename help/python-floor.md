# The Python floor

**What it is.** Every gate, hook and kit here runs Python through one resolver, and that resolver
refuses any interpreter below a floor. The floor is declared once, in `tools/lib/python-floor.txt`:
one `<major>.<minor>` line, `3.15` today. The resolver block every script carries holds a copy of
that line, `_rp_floor="3.15"`, because a kit copied into another repository has no `tools/lib/` to
read; `python tools/lib/python_floor.py check` fails when a copy differs from the declaration, and <!-- usage: script:tools/lib/python_floor.py#check 7176958e -->
when any tracked file outside `memory/` states a floor of its own instead of pointing here.

## What the refusal says

The resolver tries, in order, the caller's own override, `GOV_PYTHON`, then `python3`, `python` and
`py`. It runs each one once, isolated with `-I`, and asks for its version and its own executable.
The `-I` is new to the probe: a launcher that runs only without it is passed over as `did not run`.
The first at or above the floor wins. For the three launcher names the resolver hands back that
executable's path when the probe named a file.
An override, `GOV_PYTHON` or the caller's own, is handed back and spawned as named.
That holds for a wrapper or a venv launcher, and for an override spelled `python`.

The resolver's file test holds on a Windows App Execution Alias too. So a Store Python whose own
executable is an alias is handed back as printed, and a consumer still spawns the alias. This gap is
closed for the legs the run-gates kit measures, by its `check_app_alias`, and not by the resolver.
The probe's cost on node d, PINNED on 2026-10-23: `python3`, a shim there, answered in 25 ms, and
`py` in 92 ms.

When none qualifies, it exits non-zero. The first line names the refusal and the last names every
candidate it tried:

```text
resolve_python: no usable python launcher at the floor 3.15 (python-floor.txt in gov's lib dir).
resolve_python:   python3: ran 3.14, below the floor 3.15
resolve_python:   python: ran 3.14, below the floor 3.15
resolve_python:   py: did not run
resolve_python: install the floor with: uv python install 3.15
resolve_python: or, on Windows: py install 3.15
resolve_python: tried: python3 python py
```

`bash tools/lib/python-floor.sh preflight` refuses the same way, byte for byte. At the floor it <!-- usage: script:tools/lib/python-floor.sh#preflight 239262cc -->
prints the interpreter and its version and exits 0.

## How to install the floor

- **With uv:** `uv python install 3.15`.
- **On Windows:** `py install 3.15`, the Python install manager; `py -0p` then lists it.
- **Any other way**, then point the resolver at it if it is not first on `PATH`:
  `export GOV_PYTHON=/path/to/python3.15`. `GOV_PYTHON` names the command every consumer spawns,
  and it must still run at the floor; nothing lowers the floor.

## `platforms.provision` — what the refusal does about installing

Set it in `.governance/policy.toml` (see [the policy file](policy.md)). The resolver reads it with <!-- usage: policy:platforms.provision 0eef7dd7 -->
`policy.py get platforms.provision` at the landed revision, so a branch or an uncommitted edit does
not change it.

| Value | The refusal |
|---|---|
| `name` (the default) | names the install command: `uv python install 3.15`, then `py install 3.15` on Windows |
| `uv` | on a terminal, where `uv` runs, offers to run `uv python install 3.15` and runs it only on `y`; otherwise names the command as `name` does and says why nothing was offered |
| `off` | names no command |

```toml
[platforms]
provision = "uv"
```

When no reader can run (no candidate at 3.11 or newer, no policy kit beside the script, or the reader
fails), the refusal reads the default, `name`, and says which.

## The upgrade step

The raise is the upgrade step `lib/python-floor-3.15` in `tools/govkit/steps.toml`, after
`govkit/receipt-schema-4` (see [upgrade steps](upgrade-steps.md)). Its up and its witness are the
preflight. Its down, `python-floor.sh down 3.11 <target> <to>`, runs only in
`govkit update --rollback`, whose `--to` commit is `<to>`. It grades, under 3.11, the files that
rollback restores, read at `<to>`. In an adopter those are the receipt's rows gov shipped that end
`.py` or `.toml`, and every `.governance/*.toml` file of the target. The adopter's other files are
never graded. On gov's own tree they are every tracked `.py` and `.toml` file at `<to>`. It grades
with a real 3.11 interpreter where one resolves (`python3.11`, `py -3.11` or
`uv python find 3.11`), otherwise statically, and it says which mode it ran in on its first line. Any finding stops the down, naming `path:line`, with nothing written. With none, it
writes `3.11` back into the declaration and every copy, in gov's own source tree only.

The script's `floor` verb prints the declared floor and checks the file, with no Python: one
`<major>.<minor>` line and nothing else. The remote CI workflow reads the floor through it.
