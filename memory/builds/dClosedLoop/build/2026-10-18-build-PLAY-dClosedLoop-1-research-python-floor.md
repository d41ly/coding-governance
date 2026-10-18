# Research: the Python floor, and a plan for macOS and pwsh-launch

**Serves:** research PLAY-dClosedLoop-1

This is dispatch 113's return, verbatim, except that a title line would be demoted to keep one H1 per record. Its question is in `prompts/2026-10-18-prompt-PLAY-dClosedLoop-1-15-researcher.md`, and its use is in `build/2026-10-18-build-PLAY-dClosedLoop-1-away-pass.md`.

---

1. **Verdict**

- **The floor:** keep **3.11**. None of today's tracked Python needs anything newer, and none of the designed units does either. Raise the floor to **3.12** before 3.11's end of life (2027-10). Ship that raise as an upgrade step under P38, after the chain closes. Pay the provisioning cost now, though: Ubuntu 22.04's apt has only a 3.11 release candidate. Add one arm: Python 3.15 now reads TOML 1.1, so a node running it accepts files that gov's floor refuses.
- **macOS:** planned for later, not promised. It needs a bash 5 guard at every entry point, a lint for GNU-only flags, one shared way to find `timeout`, and a `macos-15` runner. The work starts when a node registers macOS, and only after `unattended/` is dissolved. About 5 units.
- **pwsh-launch:** planned for later, not promised. It needs one `resolve_bash` in `tools/lib` that finds Git's `bin\bash.exe` through `git --exec-path`, a refusal when an entry point finds itself running in the wrong bash, and a hook-shell row in the conformance fixture. The work starts when a node declares a PowerShell launch. About 4 units.

2. **The floor**

**Census of version-bound features in tracked Python.** The probes were `scratchpad/away/d113/census.py` (AST, 111 tracked `.py` files) and `compile_all.py` / `compile310.py`.

| Feature | Version | Uses / files | Sample |
|---|---|---|---|
| `import tomllib` | added 3.11 | 19 / 14 `.py` (13 outside `memory/`), plus 2 shell heredocs and 1 `kit.toml` command | `tools/codebase-map/map_lib.py:42`, `tools/check-playbook-parity.sh:172`, `tools/pytest-parallel-guardrails/kit.toml:53` |
| `datetime.UTC` | added 3.11 | 4 / 3 | `tools/memory-recall/query.py:82` |
| `zip(strict=)`, `dataclass(slots=)`, `X \| Y` annotations | 3.10 | 3 / 3, 3 / 1, 310 / 41 | `tools/runlog/runlog_lib.py:69` |
| `except*`, `match`, `type` statement, PEP 695 generics | 3.10–3.12 syntax | **0** | — |
| PEP 594 modules (removed 3.13), `distutils` / `imp` / `asyncore` (removed 3.12), `ast.Num/Str/Bytes/NameConstant/Ellipsis`, `pkgutil.find_loader`, `unittest.makeSuite` | removed 3.12–3.14 | **0** | — |
| `shutil.rmtree(onerror=)` | deprecated 3.12 | 2 / 1, already switches on version | `tools/memory-recall/selftest.py:349` |
| Regex possessive or atomic forms | 3.11 | 0 (the 5 text hits were all escaped `\+`) | — |

- **Syntax:** all 111 files compile under WSL 3.10.12, 3.12.10 and 3.14.5, with 0 failures and 0 warnings.
- **The floor binds on stdlib only.** It is `tomllib` and `datetime.UTC`, both 3.11.
- **The floor is tested nowhere.** No node runs 3.11 (`py -0p` lists 3.14 and 3.12 only). `.github/workflows/remote-ci.yml:47,88` runs `windows-latest` with no setup-python step. `ast.parse(feature_version=(3,11))` **accepts** a PEP 701 nested f-string on both 3.12 and 3.14 (measured), so a version-flagged parse cannot stand in for the floor. A PEP 701 escape has already happened once; today a one-kit text ban guards it (`tools/memory-tree/merge-rows.test.sh:347-356`).

**What the designed units would want**

| Unit (build) | What it needs | Minimum |
|---|---|---|
| Supervisor (dWellOiledMachine) | `subprocess`, process groups, timeouts; `asyncio.TaskGroup` / `asyncio.timeout` if it is async | 3.11 |
| `gov trace` / `gov why` | JSON index and a graph walk | any |
| Conformance fixture | `subprocess`, `json`, `tomllib` | 3.11 |
| The gates' parallel runs | a thread pool over child processes; `ThreadPoolExecutor` is already in use (`tools/run-gates/regen.py:329`) | 3.8 |
| Typed returns | TypedDict with `Required` / `NotRequired`, `Self` (3.11). `ReadOnly` / `TypeIs` (3.13) only help a type checker, and gov runs none (0 files mention mypy or pyright) | 3.11 |
| Reading and writing TOML | Reading is TOML 1.0 through `tomllib` (3.11). **No version ships a writer**: "This module does not support writing TOML" ([docs](https://docs.python.org/3.14/library/tomllib.html)). An emitter is owed under every candidate | 3.11 |

- **Free-threading and subinterpreters buy nothing here.** 3.14 supports free-threading officially and adds `concurrent.interpreters` ([3.14 What's New](https://docs.python.org/3.14/whatsnew/3.14.html)), but every leg is a child process.
- **Spawn cost does not depend on the version, only on the alias.** Measured with `$EPOCHREALTIME`, N=20:

| Spawn | ms each |
|---|---|
| 3.12 direct, `-c pass` | 27.0 |
| 3.14 direct, `-c pass` | 26.8 |
| `python3` alias (resolves to 3.14) | 105.5 |
| 3.12 direct, `import tomllib,json,subprocess` | 49.8 |
| 3.14 direct, same imports | 51.2 |

**End of life** ([devguide](https://devguide.python.org/versions/), [python.org](https://www.python.org/downloads/))

| Version | Status | End of life |
|---|---|---|
| 3.10 | ended | 2026-10-01 |
| 3.11 | security fixes only | 2027-10 |
| 3.12 | security fixes only | 2028-10 |
| 3.13 | security fixes only | 2029-10 |
| 3.14 | bugfix | 2030-10 |
| 3.15 | bugfix, released 2026-10-09 | 2031-10 |

- **How long the chain runs.** Distinct unit ids landed on main were 296, 443 and 504 in August, September and October (`git log main --since=… | grep -oE '(PLAY|KICK|TOOL|DEPL)-…-[0-9]+' | sort -u`). At that pace 367 units take about 1–3 months. That is an inference, because chain units are heavier.
- **So:** the chain should close before 3.11's end of life, but adopters will still be running gov when 3.11 expires.

**Availability and provisioning**

| Platform | 3.11 | 3.12 | 3.13 | 3.14 |
|---|---|---|---|---|
| Windows: install manager (`py list --online`, measured) | 3.11.9 only (no binaries for later security releases) | 3.12.10 only | 3.13.16 only | current |
| Windows: Store | ships the same install manager ([docs](https://docs.python.org/3.14/using/windows.html)). Its `python3` alias costs 4× | | | |
| Windows: full installer | deprecated in 3.14, last produced for 3.15 | | | |
| Ubuntu 22.04 | apt has **3.11.0~rc1** (`apt-cache policy python3.11`, confirmed on [packages.ubuntu.com](https://packages.ubuntu.com/search?keywords=python3.11&searchon=names&exact=1&suite=all&section=all)); deadsnakes or uv | deadsnakes or uv | deadsnakes or uv | deadsnakes or uv |
| Ubuntu 24.04 | deadsnakes | **native 3.12.3** | deadsnakes | deadsnakes |
| Ubuntu 26.04 | deadsnakes | deadsnakes | deadsnakes | **native 3.14.3** |
| Debian 12 | **native 3.11.2** | none | none | none |
| Debian 13 | none | none | native 3.13.5 | none |
| macOS | Homebrew or uv. The stock `/usr/bin/python3` is the developer-tools 3.9 (inference, not measured) | | | |

- Distro sources: [Ubuntu](https://packages.ubuntu.com/search?keywords=python3&searchon=names&exact=1&suite=all&section=all), [Debian](https://packages.debian.org/search?keywords=python3&searchon=names&exact=1&suite=all&section=all), [deadsnakes](https://launchpad.net/~deadsnakes/+archive/ubuntu/ppa).
- **Recommended provisioner:** uv (`uv python install 3.11`), which uses the python-build-standalone builds on every platform ([uv](https://docs.astral.sh/uv/guides/install-python/)). On Windows, `py install 3.11` is also fine.
- **The resolver must prefer the direct executable over the alias.**

**Raising the floor later, against now**

- **Now (to 3.12 or above):**
  - Every node provisions immediately.
  - Debian 12 loses its native Python.
  - No feature is gained.
  - Edits: 8 files, 9 lines, `README.md:90`, `tools/govkit/govkit.py:104-111` and `map_lib.py:17` among them.
- **Later, under P38:**
  - One upgrade step: up is a preflight that refuses below the new floor and names the provisioning command; down restores the old declaration; the witness is the interpreter version on the receipt.
  - One edit to the floor, once it is declared in a single place.
  - A re-run of the census arm.
  - The adopter's cost is the same whenever it is paid. Waiting lets Ubuntu 22.04 leave standard support first (May 2027, [Ubuntu](https://ubuntu.com/about/release-cycle)). Debian 12's LTS runs to 2028-06-30 ([Debian](https://wiki.debian.org/LTS)), so it stays in support either way.

**TOML dialect split (measured, and new).** Python 3.15's `tomllib` accepts TOML 1.1, including multi-line inline tables ([3.15 What's New](https://docs.python.org/3.15/whatsnew/3.15.html)). The same file is refused on 3.12.10 and on 3.14.5 with `TOMLDecodeError Invalid initial character for a key part (at line 1, column 8)`. A file one node accepts, another node refuses. 3.15 also makes UTF-8 the default encoding, which would dissolve much of the P-enc class once the floor reaches 3.15.

**Candidates**

| Floor | Mechanism | Losing test | Result |
|---|---|---|---|
| **3.11** | keep it, enforce it in the resolver and in an arm that runs the real interpreter | (a) a designed unit needs a feature newer than 3.11; (b) no 3.11 can be provisioned on a tier-1 platform; (c) its end of life falls before the chain closes | **Survives.** (a) 0 hits; (b) yes, but Ubuntu 22.04 needs deadsnakes or uv, and Windows stays on 3.11.9; (c) 2027-10 against an estimated chain close in 2027-Q1. It holds only until 2027-10 |
| 3.12 | raise now | it must unlock something a unit needs, and be native on every tier-1 Linux | **Loses:** 0 features gained, and Debian 12 has only 3.11.2 |
| 3.13 | raise now | same | **Loses:** 0 features gained; not native on Ubuntu 24.04 (`ubuntu-latest`) or Debian 12 |
| 3.14 | raise now for free-threading or subinterpreters | the gates or the supervisor need parallelism inside one process | **Loses:** legs are child processes, spawn cost is equal (26.8 against 27.0 ms), and it is native only on Ubuntu 26.04 |

3. **macOS**

**Blockers measured** (`scratchpad/away/d113/shcensus.py`, comment lines stripped, 132 shell files, 62 production)

| Blocker | Production files | Test files | Sample |
|---|---|---|---|
| `EPOCHREALTIME` / `EPOCHSECONDS` (bash 5.0) | 10 | 9 | `.githooks/pre-push:423`, `tools/run-gates/run-gates.sh`, `tools/push-main.sh` |
| Associative arrays (4.0) | 7 | 4 | `tools/gate-lint/fork-count.sh:73` |
| `mapfile` (4.0) | 5 | 4 | `.githooks/pre-push:859` |
| `printf %(…)T` (4.2) | 4 | 1 | |
| `wait -n` (4.3) | 1 | 3 | |
| `\|&` (4.0, a parse error on 3.2) | 1 | 4 | |
| `${x,,}` (4.0) | 2 | 1 | |
| `$BASHPID` (4.0) | 3 | 1 | |
| `globstar` (4.0) | 1 | 0 | |
| A bash version guard at an entry point | **0** (only `fork-count.sh:138`) | | |
| `timeout` (absent on macOS) | 12, of which 1 guarded (`tools/check-wiring.sh:1931`) | 14 | `tools/run-gates/run-gates.sh` (17 lines). A `gtimeout` seam exists at `tools/run-gates/run-selftests.sh:1053` |
| `date -d` (GNU) | 5 | 6 | `skills/session-kickoff/manifest-check.sh:606-607` already falls back to BSD `-r` |
| `xargs -r` | 7 | 2 | `.githooks/commit-msg:54` |
| `stat -c` | 1 (`tools/unattended/unattended.sh:8285`) | 2 | |
| `sed -i` with no suffix | 1 (`tools/unattended/resume-tick.sh:404`) | 31 | |
| `/proc` | 2 | 3 | `tools/run-gates/run-gates.sh:531` already falls back to `sysctl` (:534) |
| `nproc` | 1 | 2 | |
| `grep -P`, `find -printf`, gawk functions, `readlink -f`, `realpath` | 0 | | |

- **Stock bash:** macOS ships bash 3.2.57, the last GPLv2 release ([jmmv](https://jmmv.dev/2019/11/macos-bash-baggage.html)).
- **Shebangs help:** 128 of 129 are `#!/usr/bin/env bash`, so a Homebrew bash 5 that comes first on PATH is picked up.
- **Case-insensitive filesystem:** 0 collisions (`git ls-files | tr A-Z a-z | sort | uniq -d`) and 0 non-ASCII paths. Windows already runs case-insensitive, so this is no new risk.
- **Python and node:** Homebrew or uv, with the resolver's floor arm required. Claude Code needs macOS 13+ ([setup](https://code.claude.com/docs/en/setup.md)).
- **Most blockers dissolve with `unattended/`.** It holds 4 of the 12 `timeout` files, plus `stat -c`, `sed -i`, `globstar` and `declare -g`.

**Runner:** GitHub `macos-15` (arm64), or `macos-latest`, which is now `macos-26` ([runner-images](https://github.com/actions/runner-images)). A fleet Mac covers the held tier.

**Trigger:** a node-registry row with OS darwin, or an adopter asking for it, and only after dWellOiledMachine dissolves `unattended/`.

**Units**

| Build | Unit |
|---|---|
| dWitnessedBar | a `require_bash 5` primitive in `tools/lib`, sourced by every entry point, with its arm |
| dWitnessedBar | the GNU-flag lint as a leg over a shrink-only ledger, using the census predicate above |
| dWitnessedBar | one `timeout` resolver extracted from `run-selftests.sh:1053`, its second instance |
| dWitnessedBar | the `macos` runner adapter |
| dShippedRelease | the macOS platform row: a provisioning preflight (bash ≥5, coreutils, Python at the floor, node) and an emitted macOS CI job |
| dWellOiledMachine | a darwin conformance row (refines the planned fixture) |

**Gaps**

| Gap | Owner | What |
|---|---|---|
| port-12 | dWitnessedBar | no bash floor guard |
| port-13 | dWitnessedBar | GNU-only flags are not ledgered |
| port-14 | dWitnessedBar | `timeout` resolution is not shared |

4. **pwsh-launch**

**Blockers measured** (all through `pwsh -NoProfile`, with PATH rebuilt from the registry the way a fresh terminal builds it)

| Entry point | Under PowerShell | Evidence |
|---|---|---|
| Typed `bash tools/run-gates/run-gates.sh` | `c:\windows\system32\bash.exe`, which is WSL: bash 5.1.16, Python 3.10, and a gitdir its git cannot read | `Get-Command bash -All` |
| git hooks | Git's bash: `hook bash=5.3.9 uname=MINGW64` | a throwaway repo in scratch |
| Bare `bash` from Python | **WSL, under every launch shell**, because Windows searches System32 before PATH. Measured from Git-Bash: `/bin/bash: -c: … 5.1.16(1)-release` | `subprocess.run(['bash',…])` |
| `govkit.resolve_bash` (`tools/govkit/govkit.py:1136`) | **refuses** on a clean PATH, so `resolve_shell_argv` falls back to bare `bash`, which is WSL | probe `rb.py` |
| Bare `bash` from node (`tools/unattended/stop-guard.js:111`) | Git-Bash PATH: 5.3.9; clean PATH: **5.1.16, WSL** | probe `nodebash.js` |
| The 3 bash SessionStart hooks (`.claude/settings.json`) | depend on which Git Bash executable the harness runs. `Git\bin\bash.exe` sees `/usr/bin` tools; **`Git\usr\bin\bash.exe` sees no sed, awk, grep or mktemp, and `timeout` resolves to Windows' `timeout.exe`** | probe `clean.ps1` |
| `python3` | the WindowsApps alias, at 105.5 ms against 27.0 ms direct | |

- **The fix is reachable.** `git --exec-path` gives `C:/Program Files/Git/mingw64/libexec/git-core`, and the bash next to it exists.
- **Claude Code without Git for Windows** has no Bash tool and falls back to PowerShell ([setup](https://code.claude.com/docs/en/setup.md)).

**Candidates**

| Candidate | Mechanism | Losing test | Result |
|---|---|---|---|
| **Extend the seam** | one `resolve_bash` in `tools/lib`, built from govkit's and `corpus_ids.py`'s copies. It derives `<git>/bin/bash.exe` from `git --exec-path`, refuses System32 and WindowsApps, and has a JS twin | resolves Git's bash under a clean PATH | **Passes** (derived, exists, and `bin\bash.exe` sees the tools) |
| PATH precondition | require Git's `usr\bin` ahead of System32 | a fresh terminal's PATH | **Loses:** the machine PATH puts System32 first |
| `gov.ps1` / `gov.cmd` shim | a fourth language | P37's role rule | **Loses:** P37 allows only Python, shell and JS |

**Runner:** `windows-latest` with `shell: pwsh` and PATH rebuilt inside the step. The runner image's own PATH is not a fresh terminal's, an inference that is not measured.

**Trigger:** a node registers `launch-shell: pwsh`, or the owner adds `pwsh-launch` to `platforms.supported`.

**Units**

| Build | Unit |
|---|---|
| dWitnessedBar | the shared `resolve_bash` (Python and JS); the bare-shell-name arm already planned enforces it |
| dWitnessedBar | a wrong-bash refusal at every entry point: running under WSL on `/mnt/c` with a Windows gitdir |
| dWitnessedBar | the `pwsh-launch` runner adapter |
| dWellOiledMachine | a conformance row: which bash the hooks run in, and PATH inside a hook |

**Gaps**

| Gap | Owner | What |
|---|---|---|
| port-15 | dWitnessedBar | Python's bare `bash` is WSL on every launch shell |
| port-16 | dWitnessedBar | `resolve_bash` refuses under a clean PATH |
| port-17 | dWellOiledMachine | the hook shell is not pinned |

5. **Chain, gaps and forks**

**Units by build** ("new" adds a unit; "refines" sharpens one v2 already plans)

| Build | Floor | macOS | pwsh-launch |
|---|---|---|---|
| dWitnessedBar | refines the interpreter-floor arm: it runs a real 3.11 and absorbs `merge-rows.test.sh:347-356`; **new** TOML 1.0 arm; refines the resolver's provisioning message | 4 new | 3 new |
| dShippedRelease | refines the floor declared once in the kit factory; refines the emitted CI job (`ubuntu-22.04`, floor and latest); **new** template for a floor-raise step | 1 new | — |
| dWellOiledMachine | 0 (interpreter versions in the node registry are already planned) | 1 refined | 1 new |
| dTendedCadence | **new** detector that files an intake 6 months before the floor's end of life | — | — |
| **Total** | 3 new, 3 refined | 5 new, 1 refined | 4 new |

macOS and pwsh-launch units are planned and stay unscheduled until their triggers hold. The raise to 3.12 itself is a patch build after the chain, not a chain unit.

**Gaps**

| Gap | Owner | What |
|---|---|---|
| port-09 (HIGH) | dWitnessedBar | the floor is tested nowhere |
| port-10 (MED) | dWitnessedBar | the TOML 1.1 split |
| port-11 (LOW) | dShippedRelease | Windows binaries for 3.11 and 3.12 are frozen |
| port-12 to port-17 | as in sections 3 and 4 | |

**Keys**

| Key | Allowed | Default | Owner |
|---|---|---|---|
| `platforms.supported` | unchanged | windows-gitbash, linux | dShippedRelease |
| `platforms.provision` | `name`, `uv` (offered while attended), `off` | `name` | dShippedRelease |
| `maintain.interpreter-eol` | `file`, `warn`, `off` | `file` | dTendedCadence |

**Owner's forks**

| Fork | Options | Recommendation |
|---|---|---|
| F1, the floor now | 3.11, 3.12, 3.13, 3.14 | **3.11** |
| F2, the next floor | 3.12 by 2027-10; 3.14; 3.15 (UTF-8 default, TOML 1.1) | **3.12**, as a P38 step |
| F3, provisioning | name the command only; uv; the install manager | **name per platform, recommend uv** |
| F4, pwsh remedy | the seam; PATH precondition; a shim | **the seam** |
| F5, macOS start | on a registered node; now | **on a registered node, after the dissolution** |

**Where a record and the code disagree**

- **`EPOCHREALTIME` count:** research-compatibility line 39 says 12 production files. I measured 10 production plus 9 test files (19 in all).
- **The `python3` alias:** the record calls it the Microsoft Store alias. On this node it is the Python install manager's alias, which `py -0p` shows pointing at `pythoncore-3.14-64`.

Probes are in `C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/away/d113/`. I wrote no repository file.

Sources: [devguide](https://devguide.python.org/versions/) · [python.org](https://www.python.org/downloads/) · [3.15](https://docs.python.org/3.15/whatsnew/3.15.html) · [3.14](https://docs.python.org/3.14/whatsnew/3.14.html) · [tomllib](https://docs.python.org/3.14/library/tomllib.html) · [Windows](https://docs.python.org/3.14/using/windows.html) · [Ubuntu pkgs](https://packages.ubuntu.com/search?keywords=python3&searchon=names&exact=1&suite=all&section=all) · [Ubuntu 3.11](https://packages.ubuntu.com/search?keywords=python3.11&searchon=names&exact=1&suite=all&section=all) · [Debian](https://packages.debian.org/search?keywords=python3&searchon=names&exact=1&suite=all&section=all) · [Debian LTS](https://wiki.debian.org/LTS) · [Ubuntu cycle](https://ubuntu.com/about/release-cycle) · [deadsnakes](https://launchpad.net/~deadsnakes/+archive/ubuntu/ppa) · [uv](https://docs.astral.sh/uv/guides/install-python/) · [runner-images](https://github.com/actions/runner-images) · [Claude setup](https://code.claude.com/docs/en/setup.md) · [macOS bash](https://jmmv.dev/2019/11/macos-bash-baggage.html)
