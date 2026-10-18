# Research: one coding practice across platforms

**Serves:** research PLAY-dClosedLoop-1

This is dispatch 109's return, verbatim, except that a title line would be demoted to keep one H1 per record. Its question is in `prompts/2026-10-18-prompt-PLAY-dClosedLoop-1-12-researcher.md`, and its use is in `build/2026-10-18-build-PLAY-dClosedLoop-1-away-pass.md`.

---

1. **Verdict**

Yes. One declared practice makes sense, but one language does not. Every single-language option fails a test I ran or a record I checked. **Recommended:** keep the languages and give each one a fixed role. Python carries the logic. Shell is limited to thin shims (git hooks, the leg launcher) plus grandfathered code that may only shrink. JavaScript is limited to harness surfaces (Workflow scripts and hooks). One rule set covers all three, each rule with its gate, and new and rebuilt code moves to Python by ratchet. Most shell volume goes anyway: 58,613 of the 134,819 bash lines sit in `unattended/`, which the chain dissolves. The biggest defect is not language mix. It is that only one platform is tested: on WSL Ubuntu 22.04, two of three kit checks fail.

2. **Today**

**Language inventory** (tracked, excluding `memory/` and `.claude/`; probe `scratchpad/away/d109/inv.py`):

| Unit | bash files/lines | python | js |
|---|---|---|---|
| .githooks | 10/7,836 | 1/429 | – |
| skills/session-kickoff | 2/3,520 | – | – |
| tools/(top) | 29/13,596 | 3/2,729 | – |
| unattended | 23/58,613 | – | 4/1,360 |
| run-gates | 16/20,950 | 5/2,930 | – |
| memory-tree | 13/13,085 | 11/24,880 | – |
| govkit | 1/184 | 7/32,055 | – |
| workflows | 7/6,918 | 2/1,048 | 11/11,937 |
| hooks | 3/4,369 | – | 3/4,594 |
| lexicon / runlog / memory-recall / codebase-map / drift-audit | 7/1,910 | 37/53,669 | 1/208 |
| lib / gate-lint / roles / process-monitor / others | 21/3,978 | 23/11,812 | 1/166 |
| **Total** | **132/134,819** (prod 62/52,921, tests 70/81,898) | **88/129,572** | **20/18,265** |

- **PowerShell:** none in gov. `ps-hygiene.py` exists only for adopters.
- **Embedded code:** 11 bash files embed 32 Python heredocs or `-c` blocks, and 10 embed 36 node calls. 86 shell files call the resolved `$PY` on 321 lines. 74 files carry inline copies of `resolve_python()`.

**Minimum versions and external commands** (probe `feat.py`):

| Interpreter | What sets the floor | Evidence |
|---|---|---|
| bash ≥5.0 | `EPOCHREALTIME` in 12 production files (`.githooks/pre-push`, `tools/push-main.sh`, `run-gates.sh`, `manifest-check.sh`, `unattended.sh` …); `wait -n` (4.3) in 3; assoc arrays / `mapfile` in 12 | `git grep` output above |
| python ≥3.11 | `tomllib` in 13 files; govkit refuses below it | `tools/govkit/govkit.py:104-111`, `tools/codebase-map/map_lib.py:42`, README.md:90 |
| node ≥14 (nominal) | `??`/`?.` in 6 files, ESM in 10 | feat.py |
| External commands (bash files) | git 116, grep 101, sed 94, mktemp 89, head 81, tr 74, awk 63, … timeout 18, node 16, cygpath 7, tasklist 2, wsl.exe 1, powershell 1, schtasks 1; jq 0 | feat.py |
| External commands (Python argv[0]) | git 54, bash 6, node 2, wsl 1, powershell 1, taskkill 1 | feat.py |

Two things the toolchain fact leaves out:
- **node is a hard dependency.** 10 of 13 hook commands in `.claude/settings.json` are `node …`, plus one leg (`workflow script syntax`). The charter's Toolchain line says only "bash + python3" (AGENTS.md:175).
- **Hooks are not only in `tools/hooks/`.** They also live in `tools/unattended/`, `tools/process-monitor/` and `tools/memory-recall/`, and three SessionStart hooks are bash.

**Platforms on this node:** Git-Bash 5.3.9, git 2.54.0; `python3` = 3.14.5 through the WindowsApps alias, `python` = 3.12.10; node v24.16.0; pwsh 7.6.3; PowerShell 5.1.22621; WSL `Ubuntu` (v2, 22.04.5: bash 5.1.16, python 3.10.12, git 2.34.1, **no node**); docker 29.5.3.

**Read-only checks, three kits per platform.** Each run checked `git status --porcelain | md5sum` before and after; the hash was `04826d51…` both times. Checks run: `adopt-agent-instructions.sh --check --aliases claude`, `gen_map.py --check` (with bytecode writes off), `agent-cap.js --print-cap </dev/null`.

| Platform | agent-instructions (bash) | codebase-map (python) | hooks (node) |
|---|---|---|---|
| Git-Bash | exit 0 with `--aliases claude`, 0.08 s. The default alias set exits 1 because gov does not wire gemini or copilot. | 0 · 4.52 s | 0 · 0.04 s (prints `5`) |
| pwsh 7, inherited PATH | 0 · 0.07 s | 0 · 4.52 s | 0 · 0.03 s |
| PowerShell 5.1 | 0 · 0.11 s | 0 · 4.58 s | 0 · 0.03 s |
| pwsh 7, clean registry PATH | 0 · **3.51 s**: `bash` resolved to `c:\windows\system32\bash.exe`, the WSL launcher | 0 · 4.88 s | – |
| WSL Ubuntu 22.04 (`/mnt/c`) | 0 · 0.01 s | **1** · `ModuleNotFoundError: No module named 'tomllib'` (map_lib.py:42) | **127** · `node: command not found` |

More WSL results:
- `git -C . rev-parse` → **128**, because this worktree's `.git` holds `gitdir: C:/projects/coding-governance/.git/worktrees/…`.
- `govkit.py --help` → exit 2, "needs tomllib".
- `resolve_python` in WSL returns `python3` (3.10) with rc 0, so the resolver accepts an interpreter below the floor (resolve-python.sh:30).

**Process-creation cost** (`for` loop, `$EPOCHREALTIME`):

| Spawn | Git-Bash ms/spawn (N) | WSL ms/spawn (N=100) |
|---|---|---|
| `/usr/bin/true` (floor) | 10.2 (30) | 0.5 |
| `bash -c true` | 22.7 (30) | 1.6 |
| `python3 -c pass` (WindowsApps alias → 3.14) | **91.7** (30) | 10.9 |
| `python -c pass` (3.12 direct) | 23.2 (30) | – |
| `node -e 0` | 35.8 (30) | absent |
| `git --version` | 20.7 (30) | 1.0 |
| `pwsh -NoProfile -c 0` | 162.9 (10) | – |
| `powershell 5.1 -c 0` | 608.7 (10) | – |
| `wsl.exe -e true` | 266.6 (10) | – |
| `x=$(:)` fork | 6.7 (300) | 0.29 (1000) |
| `$(printf a \| tr a b)` | 28.0 (300) | – |

The resolver tries `python3` before `python`, so on this node every resolved Python spawn costs about 4× what it needs to. Two records disagree with today's figures: gate-lint README:137 says a command substitution costs 89–315 ms, against 6.7–28 ms measured; the process-cost gotcha's 0.022 s per spawn (process-creation-is-the-suite-cost.md:30-33) is against 10–23 ms measured.

**Defect history, by cause and the language it hits** (each from a `memory/gotchas/*.md` record or a code comment; ★ = found by this probe):

| Cause | Classes | Language hit |
|---|---|---|
| Line endings | worktree-crlf-outside-the-gated-population; gate-green-by-accident-on-generated-bytes; text-mode-read-eats-a-bare-cr; msys-grep-counts-cr-on-every-line; CRLF redirected stdout (run-gates.sh:2843, empty-field-collapses:42-48) | any reader; python ×2; bash/grep ×1 |
| Quoting | empty-field-collapses-unless-it-is-last; structured-record-split-on-whitespace; heredoc-escape-reaches-the-regex; inline-marker-breaks-a-line-continuation; bash-c-multiline-flattens-under-msys | bash ×4; python→bash ×1 |
| Shell | the stack ceiling (unattended.test.sh:2286, exit 139); substitution-fed loops hanging (gate-lint README); signal-killed-hook-reads-as-success; bounded-through-a-pipe-is-unbounded | bash ×4 |
| Process cost | process-creation-is-the-suite-cost; spawn-idiom forks | bash ×2 |
| Interpreter discovery | MS-Store stub (resolve-python.sh:4-7); subprocess-resolves-a-different-shell (also confirmed from clean-PATH pwsh); ★ resolver accepts 3.10; ★ the `python3` alias costs 4× | bash, python, pwsh |
| Paths | MAX_PATH (run-selftests.sh:1771); allowlist-narrower-than-the-root-it-guards (TEMP under $HOME); `$TMPDIR` unset (SESSION-KICKOFF.md:184-185); a-gate-that-walks-the-repo-root; ★ the worktree gitdir is a Windows path | js hook, bash, any |
| Encoding | fixture-inherits-ambient-machine-state (PYTHONUTF8); the encoding-posture class; PowerShell BOM-less non-ASCII and case-colliding names | python ×2; pwsh ×2 (adopters) |

Of the 25 classes: bash 11, python 6, cross-language 5, PowerShell 2, JS 1. Only the shell, quoting, process-cost and stub classes go away if bash goes. Line endings, encoding and paths hit Python just as hard.

3. **Candidates**

| | A. Python-first (shims only) | B. Node-first | C. Compiled single binary | D. Polyglot, a role per language, gates (+ ratchet toward A) |
|---|---|---|---|---|
| Mechanism | logic in Python ≥3.11; shell ≤ a shim for git hooks and leg launch; JS for Workflow scripts and hooks | everything in node | Go or Rust executables per OS/arch | today's languages, each with a declared role; a rule set with gates; a shrink-only shell ledger |
| Platforms covered | Win+Git-Bash, Linux; macOS once bash is only shims | the same, wherever node is installed | everything built for | Win+Git-Bash; Linux once the floor is provisioned; macOS needs brew bash ≥5 |
| Classes removed | shell ×4, quoting ×4, process cost ×2, the stub (11) | the bash 11 and the python 6 | almost all interpreter classes | none removed; each guarded or budgeted |
| Classes kept | line endings, encoding, paths, discovery (floor, alias) | line endings, paths, node discovery | paths, line endings in data, AV scanning of new binaries | all, behind gates |
| Migration (today's tree) | 62 prod + 70 test bash files, 134,819 lines, less ~4 hook shims; 58,613 of the lines are rewritten anyway by the absorption of `unattended/` (fates `[kits]` :55) | 132 bash + 88 python files (264,391 lines) | all 240 files (282,656 lines), and Workflow JS stays | 0 files; gates only |
| Adopters' cost | Python ≥3.11 on every node (Ubuntu 22.04 ships 3.10) | node on every node | per-target release builds; no source to read or fork | today's: bash ≥5, python ≥3.11, node |
| **Losing test** | resolved Python spawns slower than bash, or no floor-meeting Python on a declared platform | some install that runs gov's hooks has no node | an adopter runs a patched or forked kit | a recorded class that is language-caused and that no static or platform gate can prevent |
| **Result** | **Conditional pass.** `python` 23.2 ms = `bash -c` 22.7 ms, but the resolved `python3` alias costs 91.7 ms, and WSL resolves 3.10 (tomllib fails). It passes only once the resolver enforces the floor and prefers the direct exe. | **LOSES.** Claude Code here is a 254,858,400-byte native PE (`~/.local/bin/claude`); node is a separate install. WSL has neither claude nor node (exit 127). node also spawns slower than python (35.8 vs 23.2 ms). | **LOSES.** gate-lint/kit.toml:23 records "one live adopter runs a fork" of a shipped checker. Workflow scripts stay JS, so there is still no single language. | **Partial pass.** Process cost (6.7 ms vs 0.29 ms per fork) and the exit-139 ceiling cannot be gated, only budgeted (fork-count leg). Hence the ratchet toward A. |

The candidates stop at four. A fifth, PowerShell-first, would differ only in detail from B: it is not on Linux by default, and it spawns at 162.9–608.7 ms.

**Recommendation:** D now, moving to A by ratchet. It ranks first because the cost of A is mostly already paid by the chain's rewrites, and D's gates are needed under every option anyway.

4. **The practice**

| Rule | Gate | Exists? |
|---|---|---|
| **P-enc:** every text read, write and subprocess names `utf-8`; Python entry points write stdout as UTF-8 bytes | `encoding posture` leg (Python only) | yes, in gov's legs; **missing** from gate-lint/kit.toml's `[[gate_leg]]`s (:61,:73,:87,:97), so adopters get no leg. A stdout arm and a JS arm are new. |
| **P-eol:** every execution-sensitive or parsed file is pinned `eol=lf` *by class* (`*.py`, `*.js`, `*.json`, `*.toml`, extensionless hooks); readers open binary or with `newline=''`; writers emit LF bytes | new: a class leg joining `git ls-files --eol` with the attributes | **no.** Pins are per-directory instances (.gitattributes:143,151,199,200,251); 70 of 88 `.py` and 2 `.js` files are `w/crlf` in this worktree (`core.autocrlf=true` globally) |
| **P-path:** forward slashes; `cygpath -m` at the MSYS-to-native boundary; never a backslashed path into MSYS bash; scratch under a short root; worktree pointers readable from every declared platform | the location-probes leg (GIT_DIR); a new path-literal arm; a worktree-pointer arm | partial |
| **P-launch:** argv lists only, never `bash -c` with a multi-line script; never a bare `bash` or `sh` from Python, Node or PowerShell; interpreters resolved once to an absolute exe; a spawn budget per entry point | `shell hygiene` spawn-idioms and loop legs, `spawn budget` leg; a new bare-shell-name arm over Python and JS | partial |
| **P-tmp:** never a raw `$TMPDIR`; temp from `mktemp`/`tempfile` under the handed scratch | scratch-guard self-test | yes |
| **P-interp:** an interpreter is accepted only if it runs **and** meets the declared floor (bash 5.0, python 3.11, node 18); the direct exe beats an App Execution Alias | `python resolver` leg (runs the candidate); a floor arm and a feature-floor census are new | partial |
| **P-quote:** quoted heredocs only; no source written through a heredoc; no tab-IFS reads of fields that can be empty; quoted expansions of records | none (no shellcheck on the node) | **no** |
| **P-signal:** a trap on every git hook | dWellOiledMachine's unit (v2:1317) | owed |
| **P-role:** a new file's language follows its role; shell lines outside shims only shrink | new ledger population | **no** |

| Platform | Declare | Tested by | Today |
|---|---|---|---|
| Windows 11 + Git-Bash | tier 1 | all 4 fleet nodes (fleet.toml:20-46); remote CI `windows-latest` (remote-ci.yml:47) | green |
| Linux (WSL2 / native), floor provisioned | tier 1 | `run-held-wsl.sh`, the existing seam (:1-3), widened from the held tier to a platform half; a container job (docker 29.5.3 here); an `ubuntu-latest` CI job | **red:** tomllib, node, gitdir |
| PowerShell as launch shell | tier 2 (launch only) | pwsh fixture with a clean PATH | green, but `bash` resolves to WSL |
| macOS | unsupported until a fleet node exists | none possible here | untested; stock bash 3.2 is below the 5.0 floor (inference) |

5. **Chain, gaps and forks**

**Units by build:**

| Build | Unit |
|---|---|
| dOrderedCharter | the `portable` practice in the catalogue, absorbing `[cross-os]` and `[bytes]`, with its reach per step; the portability principle registered with its enforcing legs (P16, v2:694) |
| dWitnessedBar | the `portability` leg pack: the eol class leg, the encoding stdout and JS arms, the bare-shell-name arm, the interpreter-floor arm and feature census, and the shell-role ledger on the ledger factory (v2:1318); platform runner adapters under the product-test contract, generalising `run-held-wsl.sh`; the resolver's floor and alias order |
| dTotalRecall | `cause`, `language` and `platform` fields on the bug-class kind, so the portability lens is handed by path |
| dWellOiledMachine | each harness adapter's capability table declares its interpreter (node for hooks); the node registry's runtime facts carry OS, shell and interpreter versions, replacing free-text `variances` |
| dShippedRelease | the kit factory declares per-kit interpreter floors; install preflight records versions in the receipt; the emitted CI gains a Linux job |
| dFairHearing | the portability lens's checklist fed from the classes above (already opt-in, v2:1308) |
| dConvergedCharter | per-directory eol pins retired into the class pins |

**Gaps to register** (proposed family `port`):

| Gap | Severity | What |
|---|---|---|
| port-01 | HIGH | no declared platform matrix; Linux fails 2 of 3 checks; CI is Windows-only |
| port-02 | HIGH | the resolver accepts below-floor Python and prefers the 4× alias |
| port-03 | MED | eol pins are instances, not the class |
| port-04 | MED | node is an undeclared hard dependency |
| port-05 | MED | gate-lint ships `encoding_posture` with no adopter leg, and README:5-7 lists 3 of its 4 legs |
| port-06 | MED | Windows-path worktree pointers are unreadable from WSL |
| port-07 | LOW | bug classes carry no cause or platform field |
| port-08 | LOW | node registry OS facts are free text |

**Owner's forks:**
- **F1, the language practice.** A structural decision, not a policy (P10, v2:619). Options: A, B, C, D, or D with the ratchet toward A. **Recommend D with the ratchet.**
- **F2, harness hooks.** Keep node, declared, or move to Python. **Recommend node**, re-measured at dWellOiledMachine's adapters.
- **F3, `platforms.supported`.** Default `[windows-gitbash, linux]`; allowed `windows-gitbash | linux | macos | pwsh-launch`.
- **F4, `platforms.verify`.** Default `held`; allowed `held | bar | ci | off`. Recommend `held` until the Linux half is green, then `ci`.
- **F5, the Python floor.** Keep 3.11 or drop to 3.10 with a vendored TOML parser. **Recommend keeping 3.11** (govkit.py:107-109 rejects vendoring) and having the resolver name how to provision it.
- **F6, worktree pointers.** Git's `--relative-paths` (available in 2.54 here). The test it must pass first: WSL's git 2.34 still opens such a repository. Not run.

Probes and their outputs are in `C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/away/d109/` (`inv.py`, `feat.py`, `per.json`, `psprobe.ps1`, `psclean.ps1`, `wslprobe.sh`, `wslrun.sh`, `wslspawn.sh`). No repository file was written.
