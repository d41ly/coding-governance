**Serves:** journal TOOL-dBoundRoles-7

# TOOL-dBoundRoles-7 — acceptance ledger

Each criterion of section 6, read by the pass that built the unit with a probe of the code it changed, on the
worktree before the pass commit at base `6177e8c3d`: `node` probes in the session scratchpad that ran the exported
`scanWriteTargets`, `checkCommand`, `checkShellWrites`, `readWorkOrderAllowance` and `checkRoutedEntry` over a
fixture repository made under `%TEMP%` (a `.git` directory, as deviation 73 says), its `.memory-tree.conf` declaring
`MEMORY_ROOT="memory"` and `ROUTED_PATHS="tools/"`, a `.claude/roles.json` naming a `none`, a `spec` and a `product`
role with the `classes` map, and a fixture agent transcript whose first `user` record carries a `## Task` section with
an `### allowance` block. The hook ran whole through `main` for AC4 and AC7. A copy of the hook whose
`checkShellWrites` call is cut from `main` exited 0 on the none-role-shell and allowance-out payloads, where the hook
exited 2. A differential probe of `scanCommandHeads` (with and without `reserved`), `buildCommandView`,
`checkCommand` and `checkPollWait` against the hook at base over a corpus of gate, poll, heredoc and home commands
found no difference. No gate, suite or bar ran in the pass: the `New arm:` arm section 7 declares, its RED-first
observation, and the legs section 7 lists are owed to the main loop at the close.

**Evidences:** TOOL-dBoundRoles-7
- AC1 — `sed -i` — `scanWriteTargets("sed -i 's/a/b/' a.py")` returned `a.py` with `why` `sed -i`, and with no `-i` returned no target; `-Ei`, `-ie`, BSD's `-i ''`, `--in-place=.bak` and `bash -c` around it each named the file operand, and a `sed -i` quoted in a commit message named none. The shape is `tools/hooks/scratch-guard.js#scanInPlaceOperands`. OWED: the `BR7-AC1` rows of `tools/hooks/scratch-guard.test.sh`, RED first at the close.
- AC2 — `interpreter write` — `python -c "open('a.py','w').write('x')"`, a `python3 -` heredoc calling `Path('b.txt').write_text('x')` and `node -e "require('fs').writeFileSync('c.js','')"` returned `a.py`, `b.txt` and `c.js` with `why` `interpreter write`; `python -c "print(open('a.py').read())"` returned none; PowerShell's `[IO.File]::WriteAllText('ps.txt', 'x')` and a `timeout 30 node` heredoc's `appendFileSync` were named too. The shape is `tools/hooks/scratch-guard.js#scanInterpreterWrites` over `scanCommandHeads`' `inline` entries. OWED: the `BR7-AC2` rows, RED first at the close.
- AC3 — `git apply` — `git apply fix.patch`, the patch file placed against a `cwd` and its `+++` line naming `b/d.py`, and `git apply` fed the same patch in a heredoc each returned `d.py` with `why` `git apply`; `git apply --check` returned none, and a `rename to new.py` line was named. The shape is `tools/hooks/scratch-guard.js#scanPatchTargets`. OWED: the `BR7-AC3` rows, RED first at the close.
- AC4 — `gov-researcher` — `checkShellWrites("sed -i 's/a/b/' a.py")` at the fixture root with `agent_type` `gov-researcher` returned a deny naming the target, `sed -i`, the write gate's step 6b refusal and `The remedy is the driver's`; with no `-i` it returned null; the same payload through `main` exited 2, and through the cut copy 0. OWED: the `BR7-AC4` rows, RED first at the close.
- AC5 — `memory/builds/x/spec/` — with `agent_type` `gov-spec-writer` and a transcript handing that allowance, a redirect under `memory/builds/x/spec` returned null and one under `memory/builds/y/spec` a deny naming the allowance, the transcript and its `gov:handoff` marker; a backticked entry under the harness layout `subagents/workflows/<run id>/` admitted, and a `none` block refused the write under `memory/builds/x/spec`. The matcher is `tools/hooks/scratch-guard.js#checkRoutedEntry`, which `checkRouted` now reads too. OWED: the `BR7-AC5` rows, RED first at the close.
- AC6 — `allowance not located` — the same payload with no `transcript_path` returned a witness naming `allowance not located` and why, and no deny; an `agent_id` of `../x` was refused a path by `TRANSCRIPT_ID_RE`. OWED: the `BR7-AC6` row at the close.
- AC7 — `agent_type` — with no `agent_type`, `checkShellWrites` returned null for `sed -i 's/a/b/' a.py`; with a preloaded stub making `fs.existsSync` throw, the hook refused a `gov-builder` payload with exit 2 naming the shell-write arm, and admitted the main loop's with exit 0 and an empty stderr. OWED: the `BR7-AC7` rows, RED first at the close.
- AC8 — `home` — `checkCommand("sed -i 's/a/b/' ~/x")` returned one finding of kind `home` with `why` `sed -i`, and with no `-i` none. OWED: the `BR7-AC8` row, RED first at the close.
- AC9 — `WHAT ESCAPES THE WRITE GATE` — `grep -n "sed -i" tools/hooks/scratch-guard.js` printed the header's paragraph naming the main loop's shell write as unseen and the shapes a role agent's is held to, and the fifth-check paragraph naming what still escapes; `tools/hooks/README.md`'s write-target guard section, its new fifth-check section and `help/roles.md`'s closing paragraphs of "What the hooks refuse" name the same. OWED: the `format-guard self-test` and `memory hygiene` legs at the close.
- seen-red — `scratch-guard self-test` — red `f3ec096a8` — green `f3ec096a8` — the shell-write arm cut from main, BR7-AC4 to AC7 red
