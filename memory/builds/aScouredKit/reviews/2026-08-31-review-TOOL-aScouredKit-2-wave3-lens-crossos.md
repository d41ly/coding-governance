# Wave 3 — Lens 2: cross-OS and toolchain

**Serves:** research TOOL-aScouredKit-2

## Verdict: CLEAN WITH FIXES

Scope: the whole product at HEAD `66c4891c3325ac4ea5903e4967702346c760bded`, graded against charter
§11 (cross-OS & toolchain hygiene) and the §7 rules §11 leans on. Ran on node `a`, Windows 11,
Git-Bash / cygwin bash 5.3.9, `core.fileMode=false`, `core.autocrlf` smudging on.

Five findings. Two of them (F1, F4) share one shape: **gov's development platform is the reason the
guard cannot fire.** A Windows-only fleet with `core.fileMode=false` cannot observe a missing exec
bit, and a repo-wide `*.sh text eol=lf` cannot observe a missing per-kit LF pin. Both are the §7 rule
"a guard that shares a variable with the thing it guards is not a guard", applied to the environment
rather than to a variable.

---

## F1 — the hooks ship non-executable, and govkit propagates gov's mode. **high**

`.githooks/pre-push` and `.githooks/pre-commit` are committed at mode **100644**:

```
$ git ls-files -s .githooks/pre-commit .githooks/pre-push
100644 f6482aba… 0    .githooks/pre-commit
100644 062a62c4… 0    .githooks/pre-push
```

Only two tracked `.sh` files in the whole repo carry `100755`
(`tools/memory-tree/adopt-memory-tree.sh`, `tools/memory-tree/check-memory-hygiene.sh`), so the tree
demonstrably *can* carry the bit — these two just got it from a node where `core.fileMode` was true.
On this node `git config core.fileMode` is **false**, and all four rows of the §2 node registry are
`C:/projects/coding-governance`. Git-for-Windows emulates `access(X_OK)` as "the file exists", so on
every registered node the hooks run and the mode is invisible.

On Linux and macOS, `find_hook()` calls `access(path, X_OK)`; a 100644 hook is not found. Modern git
prints an `advice.ignoredHook` hint on stderr; older git says nothing. Either way **the hook does not
run and `git push` succeeds.** `.githooks/pre-push:3` describes what is being skipped:

> runs the FULL gate (tools/run-gates/run-gates.sh) once and BLOCKS the push if it reds

AGENTS.md calls this "where the bar binds". On a POSIX node it binds nothing.

### The deployer carries the defect outward

`tools/govkit/entries/push-main.kit.toml:20-24` ships `.githooks/pre-push` verbatim to the repo root
of every target. The write goes through `land_through_index`, `tools/govkit/govkit.py:5127`:

```python
mode = entry[0] if entry else ((gov_tree_mode(root, to_commit, src) if src else None) or "100644")
```

`gov_tree_mode()` reads **gov's own tree entry** for the source path — which is 100644. Both call
sites carry the same comment, twice:

- `tools/govkit/govkit.py:3425` — "A hook that lands non-executable is a hook that does not run."
- `tools/govkit/govkit.py:5114` — "(§8 F1) — a hook that lands non-executable is a hook that does not run."

So the mechanism written specifically to stop a hook landing non-executable sources its answer from
the one tree where the bit was never set. A fresh Linux target with no prior `.githooks/pre-push`
takes the `else` branch, lands 100644, and gets a dead push boundary on day one.

`hook_probe()` (`tools/govkit/govkit.py:3187-3207`) does not close this either: it tests
`hp.exists()`, not executability, and it probes `pre-commit` only — nothing probes `pre-push` at all.

**Fix.** `git update-index --chmod=+x .githooks/pre-commit .githooks/pre-push`, and a gate leg that
asserts `git ls-files -s .githooks/` reports 100755 for every hook — the mode is a tracked fact, so
this is a two-line check that reds on the class, not the instance. Separately, `land_through_index`
should force 100755 for a destination under `.githooks/` rather than trusting gov's tree, because the
source of that number is the thing the comment says must not be trusted.

**What I did not verify:** I could not run git on a POSIX filesystem from here. The `access(X_OK)`
behaviour of `find_hook()` is read from git's documented behaviour, not measured. The committed mode
and govkit's propagation of it are both measured.

---

## F2 — `date +%s%N` has no BSD fallback and no liveness note. **high**

`tools/run-gates/run-gates.sh:1085` and `:1113`:

```sh
s=$(date +%s%N)
…
e=$(date +%s%N)
local secs; secs=$(printf '%s.%03d' "$(( (e-s)/1000000000 ))" "$(( ((e-s)/1000000)%1000 ))")
```

`%N` is a GNU coreutils extension. BSD/macOS `date` (and busybox) emit the literal `N`, so `s` is
`1756512345N`. Measured here, feeding exactly that shape to the same arithmetic:

```
$ bash -c 'set -u; s="1756512345N"; e="1756512399N";
           secs=$(printf "%s.%03d" "$(( (e-s)/1000000000 ))" "$(( ((e-s)/1000000)%1000 ))");
           echo "RESULT=[$secs]"'
bash: line 1: 1756512399N: value too great for base (error token is "1756512399N")
RESULT=[]
```

The script sets `set -u` and not `set -e` (`tools/run-gates/run-gates.sh:18`), and the arithmetic sits
inside a command substitution, so only that subshell dies. The consequences on a BSD host, per leg:

- two bash arithmetic errors on stderr — roughly 180 lines across an 86-leg bar;
- `$WORK/$i.sec` gets an empty line, so `<git-dir>/gate-ledger.tsv` field 2 is blank
  (`run-gates.sh:1327`). AGENTS.md's "the per-leg table is a `sort -rn` away" stops being true;
- the next run's dispatch hint dies wholesale: the reader does `float(p[1])` inside a
  `try` whose `except` sets `durs = {}` (`run-gates.sh:865-870`), so one blank field discards **every**
  cached duration and the bar falls back to manifest order. The longest-first scheduling AGENTS.md
  documents is inert, silently.

No verdict changes, which is why this is high and not blocker. What makes it a finding rather than a
nit is that the same file guards its two *other* GNU-dependent calls and names the degradation out
loud:

- `run-gates.sh:363` probes `timeout -k 1s 10 true` and prints
  `run-gates: NOTE - this host has no runnable 'timeout -k' …`;
- `run-gates.sh:515` wraps `date -u -d "@…"` in `|| cutoff=""` and prints
  `run-gates: NOTE - this host cannot compute a queue staleness cutoff …`.

§7: "A probe that cannot move says so." This one cannot move and says nothing but a bash parse error.

**Fix.** Probe once at startup — `case $(date +%s%N) in *N) NANOS=0 ;; *) NANOS=1 ;; esac` — fall back
to `date +%s` whole seconds when it is 0, and emit the same `run-gates: NOTE -` shape its two siblings
already use.

---

## F3 — `declare -A` in two shipped kits, no bash-version guard anywhere. **high**

Associative arrays are bash 4.0+. macOS ships `/bin/bash` 3.2.57 and `#!/usr/bin/env bash` finds it
unless the adopter installed a newer one. Shipped occurrences:

- `tools/memory-tree/check-memory-hygiene.sh:121` — `declare -A LEGACY_SET DEBT_SET`
- `tools/memory-tree/check-memory-hygiene.sh:216` — `declare -A STAGED_SET`
- `tools/unattended/unattended.sh:1750` — `declare -A SPEC_ID=() SPEC_ST=() SPEC_PATH=()`

The memory-tree one is the flagship: `kit.toml` gives it `include = "**"`, `role = "engine"`, and
`WIRE-INTO-PROJECT.md:164,171,178` wires it into CI, pre-commit and the merge bar.

On bash 3.2, `declare -A` errors and the name falls back to an *indexed* array, whose subscripts are
arithmetic expressions. The keys here are repo paths. Measured, using an indexed array to reproduce
the 3.2 fallback:

```
$ bash -c 'unset X; X=(); X["memory/README.md"]=1; echo REACHED'
bash: line 1: memory/README.md: arithmetic syntax error: invalid arithmetic operator (error token is ".md")
exit=1

$ bash -c 'unset Y; Y=(); if [ -n "${Y[memory/g/X.md]+x}" ]; then echo HIT; fi; echo REACHED2'
bash: line 1: memory/g/X.md: division by 0 (error token is "g/X.md")
exit=1
```

`REACHED` never prints: an arithmetic error in a non-interactive shell is fatal. So the gate dies at
line 122 (or at the first `in_legacy` call if the waiver registry is empty) with a message that names
an arithmetic operator and never mentions bash.

Grepping the whole product for `BASH_VERSINFO`, `BASH_VERSION`, `bash 4`, `bash-4` returns **nothing**
outside `memory/`. `WIRE-INTO-PROJECT.md:24` is the only prerequisite statement — "Commands are bash
(git-bash on Windows)" — and pins no version, while §11 says "Pin toolchain versions".

**Fix.** One line at the top of each kit entry point that uses them:
`[ "${BASH_VERSINFO[0]:-0}" -ge 4 ] || { echo "…needs bash >= 4 (macOS /bin/bash is 3.2); try brew's bash or set …"; exit 2; }`
and a sentence in `WIRE-INTO-PROJECT.md`'s prerequisites. Rewriting the three sets to a fork-free
bash-3.2 form is the larger option and is not worth it — the sets exist precisely to avoid forks.

---

## F4 — the LF-pin population is hand-listed per kit, and `{kit}/*.sh` is declared by 1 of 24 entries. **high**

`.gitattributes:5` gives gov a repo-wide `*.sh text eol=lf`. That line is what makes gov itself
structurally incapable of noticing this.

govkit emits a `.gitattributes` block into every target from the `[[lf_pin]]` tables in the entry
descriptors (`tools/govkit/govkit.py:1994-2000`, `lf_pins()` at `:2932`). Parsed across all 24
entries, exactly one declares a pin for its own shell scripts:

| entry | declares `{kit}/*.sh`? | ships `.sh`? |
|---|---|---|
| `run-gates` (`tools/run-gates/kit.toml:140`) | **yes** | yes |
| `memory-tree` | no | yes — `check-memory-hygiene.sh`, `adopt-memory-tree.sh`, `merge-rows.sh`, `check-method-carriers.sh`, … |
| `unattended` | no (pins `{kit}/*.md`, `:151`) | yes — `unattended.sh`, `check-unattended.sh`, `check-playbook.sh`, … |
| `codebase-map`, `drift-audit`, `lexicon`, `memory-recall`, `playbook`, `agent-instructions`, `gate-lint`, `pytest-parallel-guardrails`, `hooks`, `workflows` | no | yes (adopters/checkers) |
| the ten `check-*.kit.toml` root entries + `check-wiring`, `settings-merge`, `kickoff-manifest`, `push-main` | no | yes |

And the decision is *recorded*. `tools/govkit/registry.toml:318-320`:

```toml
[[gov_only_pin]]
pattern = "*.sh"
why = "every shell script in this repo, including ones no kit ships"
```

`lf_pins()`'s docstring (`govkit.py:2938-2941`) says these rows "exist so every eol pin in gov's own
attributes file is accounted for by something — the same completeness claim the path exemptions make".
So the completeness ledger is satisfied by declaring `*.sh` gov-only, and the coverage hole it was
written to prevent is exactly what remains. The `why` is true — the pattern *does* cover scripts no
kit ships — but the conclusion drawn from it (emit nothing) is wrong; the right shape is the one
`tools/gate-legs.json` already has, where a `gov_only_pin` row **and** a kit-scoped `{prefix}/…` pin
both exist.

The product knows the rule. `WIRE-INTO-PROJECT.md:443-444` states it by hand for one file:

> add `tools/manifest-check.sh text eol=lf` (or a repo-wide `*.sh text eol=lf`) to the project's
> `.gitattributes` — the gov repo's EOL rules don't travel with `cp`, and a CRLF checkout kills bash

Second instance, same shape: **`.lexicon.conf` has no `lf_pin`.** `tools/lexicon/kit.toml:118-120`
declares only `.claude/skills/lexicon/SKILL.md`. Gov pins the conf, and its `.gitattributes` comment
says the exposure "INVERTS the unratified-seed refusal: the one check stopping an uncurated verb
table from reaching the merge bar passes exactly when it must fire. Not harmless, and MEASURED." Three
of the four bash-sourced confs (`.memory-tree.conf`, `.codebase-map.conf`, `.unattended.conf`) have
kit pins; the fourth — the one whose comment says the failure is not harmless — does not. Mitigating:
`tools/lexicon/adopt-lexicon.sh:226` now strips CR (`tr -d '\r' < "$CONF"`), so that named instance is
defended in code today. The pin gap is the class.

**Reachability, stated plainly so it can be argued with.** On Linux, `core.autocrlf` defaults to false,
so nothing smudges and an unpinned `.sh` is fine. Measured here: MSYS bash *tolerates* a CRLF script
(`sed 's/$/\r/' tools/memory-tree/merge-rows.sh` still ran to completion), so a Windows-only adopter
survives too. The break is the mixed fleet — a Windows contributor with Git-for-Windows'
"checkout as-is, commit as-is" commits CRLF blobs into a target that has no `text=auto`, and the Linux
CI leg `bash tools/memory-tree/check-memory-hygiene.sh` dies on `fi\r`. That is the case gov's own
`* text=auto` + `*.sh eol=lf` pair defends against in this repo and ships to nobody.

**Fix.** Add `{kit}/*.sh` to every entry that ships shell and `.lexicon.conf` to the lexicon entry.
Better: derive it — for each entry, take gov's `.gitattributes` `eol` answer for the paths under that
entry's `home` and ratchet that any path answering `lf` is covered by one of the entry's `lf_pin`
patterns or by a per-entry `gov_only_pin`. That turns a hand-list into a derivation and reds when a
new shipped file class arrives unpinned.

---

## F5 — a derived-population count written in prose, inside the cross-OS bound that justifies itself. **low**

`tools/check-wiring.sh:271`:

> THE BOUND IS DERIVED, and it is deliberately not "every eol=lf path": that attribute covers 46
> files here, which is far wider than anything this arm should rewrite.

Measured at HEAD:

```
$ git ls-files -z | git check-attr --stdin -z eol | python3 -c "…count value=='lf'…"
eol=lf paths: 1109
```

The *argument* is fine and the arm's bound really is derived from the tree. The number in it is off by
a factor of 24, in a comment whose job is to justify a cross-OS bound — §7's "NO count of a derived
population is written in prose", broken in the paragraph that establishes the bound. Adjacent to the
hardcoded-values lens; included because the sentence is a cross-OS one.

**Fix.** Delete the number: "far wider than anything this arm should rewrite" carries the whole
argument without it.

---

## Axes checked and found CLEAN

Recorded so a later wave does not re-spend the tokens.

**(a) committed line endings.** `git ls-files --eol | grep -c 'i/crlf'` → **0**. Nothing is committed
CRLF. The `i/lf w/crlf` set is large but is the expected smudge of unpinned paths on this fleet; the
three rendered `SKILL.md` files in it are the known by-design trio. The `.gitattributes` pin set is
otherwise thorough and every pin carries its measured incident. No unpinned execution-sensitive file
in *gov* is exposed — the exposure is one level out, at the deployer (F4).

**(b) MSYS path mangling.** `git -C` appears in shipped code at exactly two sites,
`skills/session-kickoff/manifest-check.sh:97,103`, and both feed it a `$(cd … && pwd)`-normalised
value; the surrounding comment (`:86-88`) already names the two-spellings problem and decides
membership by git identity rather than string compare. govkit drives git through
`subprocess.run([… "-C", str(target) …])` with `pathlib` values, which never produces a bare
backslash argv on Windows in a way MSYS can mangle — argv is passed to CreateProcess, not to a shell.
`kit-dogfood-parity.test.sh:42-46` handles the same two-spellings hazard explicitly. Nothing found.

**(c) the python launcher.** `bash tools/lib/resolve-python.test.sh` → `PASS — resolve-python: 53
assertions held`, covering behaviour, byte-identical inline parity across every copy-installed kit,
and an idiom ban on bare launcher names. The two non-resolver spellings that survive
(`tools/check-wiring.sh:87,89`) are `PY=python3` used only inside a printed remedy string and are
marked `# gov:literal-python`. `tools/gate-legs.json` stores the canonical `python3`/`python` in
argv[0] and `run-gates.sh:1084` rewrites it to `$PYBIN`. All 30 `.py` shebangs are
`#!/usr/bin/env python3` and nothing invokes a script by shebang. Clean.

**(d) shell portability of the batched greps.** The three scripts named in the brief use
`xargs -0 … grep -HnE` / `grep -cHE` / `grep -lE`. `-0` is present in BSD/macOS xargs; `-H` and
multi-file `-c` are in BSD grep. `-r` is a documented no-op in FreeBSD/macOS xargs. So the batched
forms are portable, and each of the three carries a comment explaining exactly why `-0` and `-H` are
load-bearing (`check-install-prefix.sh:74-82`, `check-method-carriers.sh:60`,
`check-playbook.sh:163-167`) — this landed with its reasoning intact. `grep -P` and `sed -r`: zero
occurrences in shipped code. Clean.

**(e) other platform assumptions.** `sed -i`: only in a `memory/builds/` repro script, not shipped.
`find -printf`, `stat -c`, `nproc` as a sole source, `readlink -f`, `realpath`: none in a load-bearing
path — `det_cores()` (`run-gates.sh:196-203`) chains `nproc` → `getconf _NPROCESSORS_ONLN` →
`$NUMBER_OF_PROCESSORS` and `det_ram()` chains `getconf` → `/proc/meminfo` → `sysctl -n hw.memsize`,
which is a *better* BSD story than most of this repo. `touch -d` at
`tools/hooks/agent-cap.test.sh:554` already falls back to BSD's `touch -A`. Case-sensitivity: `git
ls-files | tr A-Z a-z | sort | uniq -d` → empty, no case-only collisions. `/tmp` hardcoded in one
shipped comment and one govkit *test* fixture only; everything else uses `mktemp`.
`LC_ALL=C` is applied at the two places order is compared byte-wise; the bare `sort -u` calls are all
feeding set-membership tests where collation cannot change the answer, or are paired with a `comm`
whose other operand was sorted in the same process. Clean.

**Not verified — flagged, not claimed.** `mktemp -d` with no template appears 75 times in shipped
scripts. Whether BSD/macOS `mktemp` accepts it without `-t` I could not test from here, and my
recollection is that FreeBSD made it legal and Apple inherited that. If a macOS adopter reports
`usage: mktemp …`, this is where it comes from, and the fix is `mktemp -d -t gov` everywhere. I am
deliberately not filing it as a finding on a memory.
