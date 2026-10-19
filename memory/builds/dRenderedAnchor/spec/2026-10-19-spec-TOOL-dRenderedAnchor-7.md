# TOOL-dRenderedAnchor-7 — unit 6's closing-review findings closed as one batch, with no review round after it

**Status:** SPECCED · rev-1 · 2026-10-19 · node d · Tier-2 · base 05357638 · streams tooling

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-19-prompt-TOOL-dRenderedAnchor-7-brief.md](../prompts/2026-10-19-prompt-TOOL-dRenderedAnchor-7-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

Close the six confirmed items of unit 6's closing diff review
(`memory/builds/dRenderedAnchor/reviews/2026-10-19-review-TOOL-dRenderedAnchor-6-closing-diff-round1.md`)
as the build's last unit. A kit installed through a junction renders its own install's harness
paths. A path held by the install receipt cannot reach a JS literal or a shell command without the
renderers' charset guard. The render mode's re-run never degrades silently. Every new refusal, and
the exit status the re-run passes back, has an arm. No review round follows this unit (owner,
2026-10-19).

## 2. Scope (IN)

- **S1** — H1. The canonical `derive_kit_paths` in `tools/lib/render-doc.sh` takes its kit directory
  with `pathlib.Path(sys.argv[1]).absolute()`, as `resolve_kit_dir` already does, instead of
  `.resolve()`. All four inline copies are re-synced byte-identical. Observed by AC1 and AC2.
- **S2** — H1's arm. `tools/lib/resolve-python.test.sh` gains section 2h. It runs the canonical over
  a kit directory reached through a junction whose prefix differs from its target's. Observed by AC1.
- **S3** — M1's factory. `tools/lib/render-doc.sh` gains a fourth canonical block,
  `check_kit_cites`, with a parity row and a behaviour section 2i in
  `tools/lib/resolve-python.test.sh`. Observed by AC3 and AC4.
- **S4** — M1's call sites. The parity script and `tools/unattended/adopt-unattended.sh` each carry
  `check_kit_cites` inline and call it right after the derivation whose lines `render_kit_cites`
  applies. A hit exits 2 before anything is written. The parity script's charset comment says the
  citation channel has its own check. Observed by AC5.
- **S5** — L2. The parity script's re-run guard reads `"${PROTOCOL_PARITY_REPASS:-}" != 1`. When
  the two derivations differ and the guard suppresses the re-run, the script prints one line naming
  `PROTOCOL_PARITY_REPASS` and exits 1. Observed by AC6.
- **S6** — L3. Arm RA6-1 captures the render mode's output and asserts the re-run line and the exit
  status. A new arm, RA7-1, stages a re-run that alone fails and asserts that the parent passes the
  child's status back. Observed by AC7.
- **S7** — L4. A new arm, RA7-4, puts a directory of `python3`, `python` and `py` stubs that exit
  9009 first on PATH, with `GOV_PYTHON` unset. It runs `adopt-unattended.sh --check` and, under §8
  F1's recommended option, the parity script's check mode. Each must exit 2, and the resolver's
  reason must be the last line printed. Observed by AC8.
- **S8** — §8 F1's recommended option. The parity script's `FANOUT_CAP` block moves, with its
  comment, from before the function definitions to just after the citation check of S4. A host with
  no python is then refused on the resolver's own reason. Observed by AC8.
- **S9** — L1 and the documentation, in three changes. Observed by AC9. Unit 6's spec is CLOSED and
  stays unedited, so this spec's §4 and this unit's ledger carry its correction.
  - `tools/workflows/README.md` and the comment above the parity script's second pass state what
    `--tracked-only` actually does. It creates only a live copy this install already tracks. A
    tracked harness absent from the worktree is written again, and the run then re-runs once.
  - The same README states S5's suppression line.
  - Both kit READMEs state S4's refusal.
- **S10** — Gov's own renders stay byte-identical. Observed by AC10.

## 3. Non-goals (OUT)

- `roles_lib.resolve_harness_path`'s probe order, and `render_doc`'s unanchored apply loop
  (`tools/lib/render-doc.sh:50-53`). The brief rules both out.
- A charset check inside `derive_kit_paths` or `render_doc`. The memory-tree renderers share both,
  and their documents are outside this unit's two renderers.
- A check on the parity script's second derivation (`tools/workflows/check-protocol-parity.test.sh:602`).
  Its values are compared and never substituted, and the child re-run derives them again at the
  checked first site (§4, Alternatives rejected).
- The review's optional L1 arm, and the checklist entries the review proposes under each item. The
  brief lists neither. The arms of S2, S3, S4, S5, S6 and S7 are the regression gates.
- A grep that refuses `.resolve()` in a canonical render block. The junction arm is H1's gate.
- `tools/workflows/check-verifier-fanout.sh`, whose no-python notice reaches the parity script's
  captured `--print-cap` answer (§4).
- The four inherited reds. Running the unattended kit's own self-test suites, under the owner's
  standing rule (`TOOL-dDerivedDocket-76` in `memory/DECISIONS.md`). Any further review round
  (owner, 2026-10-19).
- Kit version bumps. The lander's `mint` writes them, and merge and push wait for the owner's ask.

Units 1 to 6 are CLOSED. Unit 6's commits on this branch are this unit's ground, not a sibling's
pending work, so no edge names them.

### Edges

none

## 4. Design

### The base

`base 05357638` is the default branch. The branch tip `a99b3f23` adds unit 6's build pass
`b31803aab` and its records on top of it. Every claim below about current code was read at
`a99b3f23`.

### H1 — the junction (S1, S2)

`derive_kit_paths` resolves its kit argument physically, at `tools/lib/render-doc.sh:157`. Its own
nested `resolve_kit_dir` takes `here` logically, at `:113`, with the comment `never resolve(): a
junction must not move it`. Both renderers find their own root with a logical walk. The adopter
states that walk as the junction contract (`tools/unattended/adopt-unattended.sh:55-61`). So under
a junction the derivation's root is the link target's repository, and every held citation is
spelled relative to it.

The fix is the one line, `kit = pathlib.Path(sys.argv[1]).absolute()`. The canonical has four
inline copies, each at the same line of its block:

| Copy | Line |
|---|---|
| `tools/memory-tree/adopt-memory-tree.sh` | 264 |
| `tools/memory-tree/kit-dogfood-parity.test.sh` | 192 |
| `tools/unattended/adopt-unattended.sh` | 401 |
| `tools/workflows/check-protocol-parity.test.sh` | 293 |

The `derive_kit_paths` parity row (`tools/lib/resolve-python.test.sh:174`) grades every copy. The
roles adopter keeps its own derivation and already reads `.absolute()`
(`tools/roles/adopt-roles.sh:180`).

**No caller passes a `..` segment**, which `absolute()` would keep and the receipt rung's
`".." not in hit.parts` test (`render-doc.sh:128`) would then refuse:

- the parity script passes `KITREL`, built from basenames (`check-protocol-parity.test.sh:76-82`);
- the unattended adopter passes `KIT_DIR`, a `cd && pwd` (`adopt-unattended.sh:28`);
- the memory-tree adopter and its parity suite pass a prefix-stripped `cd && pwd`
  (`adopt-memory-tree.sh:11-18`, `kit-dogfood-parity.test.sh:52`);
- section 2f passes a `mktemp -d` path (`resolve-python.test.sh:393`).

Gov's tree holds no symbolic link or junction: `find tools skills memory .claude -maxdepth 2 -type
l` printed nothing on 2026-10-19. So the two spellings agree for every one of gov's renders (S10).

**Section 2h** follows 2g (`resolve-python.test.sh:396-406`) and uses 2f's shape:

| Path | Content |
|---|---|
| `$TMP/jb/.git`, `$TMP/jt/.git` | empty directories, so each walk stops at its own repository |
| `$TMP/jt/tools/wf/t.js` | one line |
| `$TMP/jb/.gov/wf` | a link to `$TMP/jt/tools/wf` |
| `$TMP/jb/x.template.md` | `cites {{TOOL_ROOT}}wf/t.js here` |

The canonical, sourced, runs `derive_kit_paths "$REALPY" "$TMP/jb/.gov/wf" "$TMP/jb/x.template.md"`.
It must print `{{TOOL_ROOT}}wf/t.js<TAB>.gov/wf/t.js`. With `.resolve()` it prints `tools/wf/t.js`.

The link follows the idiom of `tools/unattended/adopt-unattended.test.sh:551-566`. It tries
`ln -s` first and tests `[ -L ]` after creating it, because on this fleet `ln -s` can exit 0 and
leave a copy. If that fails, it removes the copy and makes a directory junction with
`cmd //c mklink //J`. **If neither yields a link, the section FAILS and names why; it does not
skip.** This suite is gov-internal (`tools/lib/`) and runs only on hosts that can link: the Windows
nodes and `.github/workflows/remote-ci.yml`'s `windows-latest` runners make a junction without a
privilege, and a POSIX host makes the symlink. A skip here would be a gate that cannot go red.

### M1 — the citation charset (S3, S4)

A citation's value is `(resolve_kit_dir(...) / anchor).relative_to(root)`. The directory part
comes from a receipt row's `path`, and `emit()` refuses only tab, CR and LF
(`render-doc.sh:149-154`). `render_kit_cites` substitutes the value verbatim (`:280-285`). The value
reaches `const DRIVER = 'bash {{TOOL_ROOT}}unattended/unattended.sh'`
(`tools/workflows/unattended-build.template.js:557`). It also reaches the commands the Skill and the
protocol tell an agent to run. Each script already refuses its own substituted paths outside
`[A-Za-z0-9._/+@-]`: the parity script at `check-protocol-parity.test.sh:460-466`, and the adopter
at `adopt-unattended.sh:535` and `:589-594`.

Two scripts need the same loop, so the charter's `[reuse]` rule makes it a gated canonical:

```bash
# >>> check_kit_cites — canonical copy: render-doc.sh in gov's lib dir (byte-identical; gated)
# `check_kit_cites <label> <kit paths>` returns 2 at the first `{{TOOL_ROOT}}<home>/<file>` line
# whose path is empty or holds a character outside [A-Za-z0-9._/+@-], printing one line naming the
# cite and the path, and 0 otherwise. It reads exactly the lines `render_kit_cites` applies: a bare
# `{{TOOL_ROOT}}` line and an adopter-placeholder line carry phrases with spaces, never applied here.
check_kit_cites() {
  local kp kv
  while IFS=$'\t' read -r kp kv; do
    case "$kp" in '{{TOOL_ROOT}}'?*) ;; *) continue ;; esac
    case "$kv" in
      ''|*[!A-Za-z0-9._/+@-]*)
        echo "$1: the citation $kp resolves to '$kv', which is empty or holds a character outside [A-Za-z0-9._/+@-]. A citation lands in a JS string literal and in commands an agent runs, where a quote ends the string and a space splits the command. Fix the install receipt row that places it."
        return 2 ;;
    esac
  done <<<"${2//$'\r'/}"
  return 0
}
# <<< check_kit_cites
```

The two-field `read` keeps the value last, so an empty value cannot shift a field. The block sits
after `render_kit_cites` in the canonical file, and the header paragraph at `render-doc.sh:28-31`
names it. The parity row is `check_kit_cites|$ROOT/$KIT_REL/render-doc.sh|$KIT_REL/render-doc`,
beside the `render_kit_cites` row (`resolve-python.test.sh:175`). The row's population grep finds
the two renderers' copies with no further edit (`:215`).

The call sites, each placed immediately after the derivation and refusing with exit 2:

| Script | After | Call |
|---|---|---|
| `tools/workflows/check-protocol-parity.test.sh` | `:522-523`, the `KIT_PATHS` derivation | `check_kit_cites protocol-parity "$KIT_PATHS" \|\| exit 2` |
| `tools/unattended/adopt-unattended.sh` | `:570`, the `KIT_PATHS` derivation | `check_kit_cites unattended "$KIT_PATHS" \|\| exit 2` |

Neither site has written anything yet. The parity script writes only after its render loop
(`:583-594`). The adopter's first write is the stamp (`:582-610`). The comment at
`check-protocol-parity.test.sh:457-459` gains one sentence: a citation's path is checked where it is
derived, by `check_kit_cites`.

**Section 2i** runs the canonical, sourced, over three CRLF inputs:

| Input lines | Expected |
|---|---|
| `{{TOOL_ROOT}}h/t.js<TAB>p/k/t.js`, `{{TOOL_ROOT}}<TAB>q r/`, `{{GATE_RUNNER}}<TAB>the merge bar of this repo` | return 0, nothing printed |
| the first set plus `{{TOOL_ROOT}}h/u.js<TAB>p/u';x;'/u.js` | return 2, one line naming `{{TOOL_ROOT}}h/u.js` and `p/u';x;'/u.js` |
| the first set plus `{{TOOL_ROOT}}h/v.js<TAB>p/q r/v.js` | return 2, one line naming `{{TOOL_ROOT}}h/v.js` |

If the value case is taken out, all three inputs return 0. If the cite filter is taken out, the
first input returns 2 on the bare line's `q r/`.

### L2 — the suppressed re-run (S5)

The guard at `check-protocol-parity.test.sh:604` is `[ -z "${PROTOCOL_PARITY_REPASS+set}" ]`. It is
false for an inherited empty value, and the moved-citations case then reaches `exit 0` at `:609`.
The replacement:

```bash
  if [ "$_kp_after" != "$KIT_PATHS" ]; then
    if [ "${PROTOCOL_PARITY_REPASS:-}" != 1 ]; then
      echo "protocol-parity: this render wrote a file a template's citation resolves to, so the citations moved; rendering once more"
      PROTOCOL_PARITY_REPASS=1 bash "$HERE/${0##*/}" "$@"
      exit $?
    fi
    echo "protocol-parity: the citations moved after this render wrote, and PROTOCOL_PARITY_REPASS=1 suppressed the re-run, so a rendered copy may name a stale path. Run bash $KITREL/check-protocol-parity.test.sh --render with PROTOCOL_PARITY_REPASS unset"
    exit 1
  fi
  exit 0
```

The exit code is 1 because the header's table reads `1 = drift` (`:3`), and the live copies now
disagree with what a check-mode run would derive. The render mode's other non-writes also exit 1
(`:584`, `:590`). Inside a legitimate re-run the derivations agree, because the child derives over
files the parent already wrote. So the branch is reached only through a value inherited from a
caller.

### L1 — what `--tracked-only` does (S9)

The skip at `check-protocol-parity.test.sh:535` fires only for a live copy that is absent AND
untracked. A tracked harness deleted from the worktree is therefore rendered and recreated
(`:583-594`). The first derivation could not see that harness, because `resolve_kit_dir` keeps a row
or a probe only when it is a file (`render-doc.sh:128`, `:132`). The second derivation sees it, and
the run re-runs once. So three carriers were wrong:

- `tools/workflows/README.md:68`, which says `--tracked-only` "never re-runs";
- the comment at `check-protocol-parity.test.sh:600-601`;
- unit 6's spec §4, which says the same in its paragraph on the second pass.

The first two are restated to the review's corrected text. The third is CLOSED and frozen, so this
paragraph is the correction.

### L3 and L4 — the arms (S6, S7)

Every arm lives in `tools/workflows/unattended-build.test.sh`, inside the unattended-adopter guard
(`:2246`) that RA6 already shares with PV-AC12. Three helpers are extracted, each at its second
instance:

| Helper | Extracted from | Used by |
|---|---|---|
| `build_renamed <dir>` | RA6's layout steps, `:2283-2287` | RA6-1, RA7-1, RA7-2 twice, RA7-3 |
| `seed_unattended_kit <dir>` | RA6-2's kit copy, conf and settings file, `:2296-2311` | RA6-2, RA7-3 |
| `write_python_stubs <dir> <always\|repass>` | new | RA7-1, RA7-4 |

`write_python_stubs` writes `python3`, `python` and `py` in the given directory, using the shape of
`mkfake` (`tools/lib/resolve-python.test.sh:47-53`). Under `always` each stub exits 9009. Under
`repass` each stub exits 9009 when `PROTOCOL_PARITY_REPASS` is 1 and otherwise runs `exec` on the
absolute path of the suite's own resolved python, which is `command -v "$_rkd_py"` (`:122`). Every
run that uses the stubs prepends their directory to PATH and unsets `GOV_PYTHON`. Unsetting is
required: `resolve_python` falls through from a failed `GOV_PYTHON` to the launcher names
(`check-protocol-parity.test.sh:124-131`), so a wrapper passed through `GOV_PYTHON` alone stages
nothing.

| Arm | Layout | Run | Asserts |
|---|---|---|---|
| RA6-1, two more sites | `build_renamed` | `--render`, output kept | the re-run line occurs exactly once; `rc=0` |
| RA7-1 | `build_renamed`, stubs `repass` | `--render` | the re-run line is present; `rc=2` |
| RA7-2 | `build_renamed`, with `PROTOCOL_PARITY_REPASS=1` exported in a subshell | `--render` | the suppression line is present; no re-run line; `rc=1` |
| RA7-2 | a second `build_renamed`, with `PROTOCOL_PARITY_REPASS=` exported | `--render` | the re-run line occurs exactly once; `rc=0` |
| RA7-3 | `build_renamed`, then the receipt replaced (below), then `seed_unattended_kit` | the parity script's `--render`, then the adopter | each `rc=2` with its refusal line; neither document written |
| RA7-4 | `$R6` after RA6-2, stubs `always` | `adopt-unattended.sh --check`, then the parity script's check mode | each `rc=2`, and the last line before `rc=` is `resolve_python: tried: python3 python py` |

RA7-3's receipt holds two rows. Each `source` sits under a neutral `g/$WFK/` and each `path` under
`q r/`, and both files are copied into place:

| role | source file | path |
|---|---|---|
| engine | `check-verifier-fanout.sh` | `q r/check-verifier-fanout.sh` |
| engine | `unattended-unit.js` | `q r/unattended-unit.js` |

The first row is the protocol's line-92 citation and the second is the Skill's line-125 citation.
Every kit segment is `$WFK` or `$UNK`, never typed, as in RA6.

**Why RA7-4 asserts the LAST line.** The brief's staged break, `|| exit 2` replaced by `|| :` on the
resolver line, leaves the exit code at 2 in both scripts. The next line runs `derive_kit_paths` with
an empty launcher, and that refuses with exit 2 too (`adopt-unattended.sh:570`,
`check-protocol-parity.test.sh:522-523`). The resolver's reason goes to stderr either way
(`check-protocol-parity.test.sh:132-145`). So an arm asserting only the code and the reason stays
green under the break. Under the break, the line printed after the reason is the shell's `command not
found` in the adopter, and `protocol-parity: could not resolve the citations the templates make` in
the parity script. Asserting that the reason is the last line therefore reds on the break.

**Why the parity half needs S8.** Under no python, the parity script never reaches its resolver
line today. `FANOUT_CAP` is asked first (`check-protocol-parity.test.sh:106-115`). The fan-out gate
prints its no-python notice to stderr (`tools/workflows/check-verifier-fanout.sh:138`), and the
parity script captures that with `2>&1`. Then either the gate finds no hook, because only the
`.claude/hooks/` rung remains (`:144-147`), or the captured answer is not a single digit. Both refuse
with exit 2 before `:514`. This held at the base too: `git show 05357638` carries both lines. So the
review's L4 claim that the base script "ran with no python" does not match the code, and the
resolver refusal at `:514` is unreachable on a host with no python. S8 moves the `FANOUT_CAP` block
(`:100-115`) to just after S4's check, ahead of `TMPD` (`:525`). Nothing between its old and new
places reads `FANOUT_CAP`, whose one reader is `render` (`:482`). No arm asserts the fan-out refusal's
text: a grep of `tools/` for `would not answer the effective fan-out cap` and `not a digit 1-9`
outside the script finds nothing. Under F1's other option, S8 is dropped and RA7-4 runs the adopter
only.

`FLOOR_ASSERTIONS` (`unattended-build.test.sh:2950`) rises by the executed count of every new
assertion site. That count is written in a `RAISED` comment beside the earlier ones (`:2946-2949`).

### Inventory

| Minted | Where | Naming cell |
|---|---|---|
| `check_kit_cites` | `tools/lib/render-doc.sh`, inline in the two renderers | `sh.function`; `lexicon.py --suggest` answered OK on 2026-10-19 |
| `build_renamed`, `seed_unattended_kit`, `write_python_stubs` | `tools/workflows/unattended-build.test.sh` | `sh.function`; each answered OK on 2026-10-19 |
| parity row `check_kit_cites`, sections 2h and 2i | `tools/lib/resolve-python.test.sh` | — |
| arms `RA7-1` to `RA7-4` | `tools/workflows/unattended-build.test.sh` | — |

No receipt field, conf key, environment variable, leg or file is minted.

### Rollout

Tier-2: a cross-kit change to a carried canonical, and a shipped edit to three kits. `govkit update`
carries the bytes, and the review-harness regenerate and the next adopter run re-render. On a
junction install the citations move to the logical spelling, which is the fix itself. Kit versions
are minted at landing.

### Files touched (estimate)

- `tools/lib/render-doc.sh`, `tools/lib/resolve-python.test.sh`
- `tools/memory-tree/adopt-memory-tree.sh`, `tools/memory-tree/kit-dogfood-parity.test.sh`
- `tools/workflows/check-protocol-parity.test.sh`, `tools/workflows/unattended-build.test.sh`,
  `tools/workflows/README.md`
- `tools/unattended/adopt-unattended.sh`, `tools/unattended/README.md`
- `memory/builds/dRenderedAnchor/build/`, for this unit's acceptance ledger

### Alternatives rejected

| Candidate | The test that rejected it | Verdict |
|---|---|---|
| C1 — the charset check inside `render_kit_cites` | it runs inside `render`, whose failure branch says the template could not be read (`check-protocol-parity.test.sh:550-551`), and an `exit` there would fire mid-loop; the brief places it after the derivation | Rejected |
| C2 — the check inside `derive_kit_paths`' `emit()` | it would refuse in the memory-tree renderers too, whose documents this unit does not own | Rejected |
| C3 — one inline loop per call site | the charter's `[reuse]` rule extracts a factory at the second instance, and two ungated loops drift | Rejected |
| C4 — a check after the second derivation too | its values are only compared; the child re-run derives them again and refuses at its first site before it renders, so the refusal could never fire, and an unarmed refusal contradicts the goal | Rejected |
| C5 — L2's suppression exits 2 | the header's code table names a misconfigured invocation 2 and drift 1, and the condition is a render the next check reads as drift | Rejected |
| C6 — section 2h skips when no link can be made | a skip reads as coverage, and every host this gov-internal suite runs on can link | Rejected |
| C7 — L4's arm asserts the exit code and the reason only | the brief's own staged break leaves both standing (above) | Rejected |

## 5. Production-readiness checklist

- security — M1 closes a receipt-to-JS-literal channel: a receipt row's path no longer reaches a
  quoted literal or an agent's command unchecked. H1 stops the renderers from citing paths in
  another repository. No new write path.
- perf / scale — One more bash loop over `KIT_PATHS` per run. No new python start.
- error / empty / loading states — An empty or out-of-set citation path is exit 2 with its line.
  With no python, the parity script now reports the resolver's reason instead of a polluted fan-out
  answer (F1). A suppressed re-run is exit 1 with its line.
- observability — Every new refusal prints one line naming its cause.
- risks — The memory-tree renderers take S1 too, so a memory-tree junction install renders its
  citations logically from now on, which is the same fix there. Whether the unattended kit's own
  suites hold a junction fixture that reads a citation is UNVERIFIED. Those suites are not run here,
  under the owner's rule.
- testing — AC1 to AC8 are fixture or in-process probes, and AC9 and AC10 read this worktree. The
  main loop observes each new arm RED, then GREEN, at the close (§7).
- migration — N/A — no receipt, conf or deploy field moves, and an update re-renders.
- user docs — The two kit READMEs (S9). No `help/` page covers these renders: `ls help/` lists only
  `README.md`, `measure-legs.md` and `roles.md`.

## 6. Acceptance criteria

`<p1>` is this unit's build pass commit. Each probe is a bash script under the session scratchpad
that copies the named arm's steps into a scratch directory. The parity script is the review-harness
kit's `check-protocol-parity`, named in prose here because its file is a suite-shaped name.

- **AC1** — When a probe builds section 2h's fixture and runs `derive_kit_paths` from
  `tools/lib/render-doc.sh` over it, it prints `{{TOOL_ROOT}}wf/t.js` and `.gov/wf/t.js` on one
  tab-separated line.
  Red when: `.absolute()` is reverted to `.resolve()` in the canonical, and the value reads
  `tools/wf/t.js`.
  fixture: a junction made by `cmd //c mklink //J` on this host; the tree holds none today.
- **AC2** — When `diff <(awk '/^# >>> derive_kit_paths/,/^# <<< derive_kit_paths/' tools/lib/render-doc.sh) <(awk '/^# >>> derive_kit_paths/,/^# <<< derive_kit_paths/' <copy>)`
  runs for each of the four copies of §4, CRs dropped, each prints nothing.
  Red when: one copy keeps `.resolve()`, and its diff names that copy's `kit =` line.
- **AC3** — When `check_kit_cites t "$KP"` runs with `tools/lib/render-doc.sh` sourced over each of
  section 2i's three inputs, it returns 0, 2 and 2. The second and third each print one line naming
  their cite.
  Red when: the value case is taken out, and all three return 0; or the cite filter is, and the
  first returns 2 on `q r/`.
- **AC4** — When the AC2 diff runs with `check_kit_cites` for the parity script's copy and the
  adopter's copy, each prints nothing.
  Red when: one byte of either copy changes, and its diff names the line.
- **AC5** — When a probe builds RA7-3's layout and runs the parity script there in render mode, it
  exits 2 and prints a line that begins `protocol-parity: the citation
  {{TOOL_ROOT}}workflows/check-verifier-fanout.sh resolves to 'q r/check-verifier-fanout.sh'`. No
  `memory/guides/REVIEW-PROTOCOL.md` exists afterwards. When `bash scripts/unattended/adopt-unattended.sh`
  then runs there, it exits 2 with the line naming `{{TOOL_ROOT}}workflows/unattended-unit.js`, and
  no `.claude/skills/unattended/SKILL.md` exists afterwards.
  Red when: the `check_kit_cites` call is taken out of the parity script, which exits 0 and writes a
  protocol naming `q r/check-verifier-fanout.sh`; or out of the adopter, which writes a Skill naming
  `q r/unattended-unit.js`.
- **AC6** — When a probe builds a fresh `build_renamed` layout and runs the parity script there in
  render mode with `PROTOCOL_PARITY_REPASS=1` exported, it exits 1. It prints the line naming
  `PROTOCOL_PARITY_REPASS` and no `rendering once more` line. With `PROTOCOL_PARITY_REPASS=`
  exported over a second fresh layout, it prints `rendering once more` exactly once and exits 0.
  Red when: the suppression branch is taken out, and the first run exits 0 with no line; or the
  guard is reverted to the `+set` test, and the second run prints no re-run line.
- **AC7** — When a probe builds a fresh `build_renamed` layout and runs the parity script there in
  render mode, `grep -c 'rendering once more'` over its output prints 1 and it exits 0. Over a
  second fresh layout, with the `repass` stubs first on PATH and `GOV_PYTHON` unset, it prints the
  re-run line and exits 2.
  Red when: `exit $?` after the re-run is changed to `exit 0`, and the second run exits 0; or the
  announcement is taken out, and the count reads 0.
- **AC8** — When a probe takes `$R6` after RA6-2 and runs `adopt-unattended.sh --check` there with
  the `always` stubs first on PATH and `GOV_PYTHON` unset, it exits 2. The last line it prints is
  `resolve_python: tried: python3 python py`. Under F1's recommended option, the parity script's
  check mode run the same way exits 2 with the same last line.
  Red when: `|| exit 2` on the resolver line becomes `|| :`, and the last line is the shell's
  `command not found` in the adopter, or `protocol-parity: could not resolve the citations the
  templates make` in the parity script.
- **AC9** — When `grep -c 'never re-runs'` runs over `tools/workflows/README.md`, it prints 0.
  `grep -c 'PROTOCOL_PARITY_REPASS'` over the same file prints at least 2. `grep -cF
  'A-Za-z0-9._/+@-'` over it and over `tools/unattended/README.md` prints at least 1 for each.
  `grep -c 'nothing is created, so the two derivations agree'` over the parity script prints 0.
  Red when: the files are as at `a99b3f23`, where the counts read 1, 1, 0, 0 and 1.
  figure: the five baseline counts are PINNED, measured at `a99b3f23` on 2026-10-19.
- **AC10** — When the parity script runs in render mode and `bash tools/unattended/adopt-unattended.sh`
  runs, both in this worktree at `<p1>`, `git status --porcelain` prints nothing. A probe then runs
  `derive_kit_paths` from `<p1>`'s `tools/lib/render-doc.sh` and from `a99b3f23`'s, taken by `git
  show` into the scratchpad. Each runs over `tools/memory-tree/*.template.md`, the five review-harness
  templates and `tools/unattended/SKILL.template.md`, and the two outputs are identical.
  Red when: a held citation is spelled relative to a different root, and the status names
  `memory/guides/REVIEW-PROTOCOL.md` while the diff names its line.

## 7. Gates

`review-protocol parity (kit vs dogfood)` · `python resolver (behaviour + inline parity + idiom ban)` · `kit/dogfood doc parity` · `unattended skill wiring` · `unattended skill size` · `unattended-build self-test` · `tier2-review self-test` · `verifier fan-out self-test` · `review-join self-test` · `shell hygiene (a loop fed by a command substitution)` · `shell hygiene (a location probe asked from a moved directory)` · `shell hygiene (a fork spent on builtin work)` · `shell hygiene (a fixed-name temp renamed into place)` · `spawn budget (forks per hot entrypoint)` · `harness arms (fail branches armed or pinned)` · `install-prefix (shipped surface)` · `kit version markers` · `kit epoch (shipped bytes move, the version moves)` · `codebase-map coverage + freshness` · `memory hygiene` · `recall floor` · `recall floor arms`

The brief names review-protocol parity, the python resolver, the unattended-build self-test, the
unattended wiring leg, the shell hygiene legs and memory hygiene. The memory-tree copies owe the
kit/dogfood parity leg. The four `{prefix}/workflows/` legs and the two recall legs are owed by the
guards the Files touched paths trip. They were derived on 2026-10-19 from `tools/gate-legs.json`,
with the breadth floor `BROAD_LEG_FLOOR = 5` (`tools/check-spec-tokens.py:262`) excluding
`{prefix}/`, `{prefix}/lib/` and `{prefix}/memory-tree/` as broad. New shell lines take the no-fork
forms those legs require, and no registry row is added or raised. The close runs the bar once, after
the unit is terminal; no pass runs a leg.

New arm: tools/lib/resolve-python.test.sh, section 2h · covers AC1 · `.absolute()` reverted to `.resolve()` in render-doc.sh's derive_kit_paths · none
New arm: tools/lib/resolve-python.test.sh, section 2i · covers AC3 · the value case taken out of render-doc.sh's check_kit_cites, then separately its cite filter · none
New arm: tools/lib/resolve-python.test.sh, parity row check_kit_cites · covers AC4 · one byte changed in the parity script's copy · none
New arm: tools/workflows/unattended-build.test.sh, RA7-3 · covers AC5 · the check_kit_cites call taken out of the parity script, then separately out of adopt-unattended.sh · FLOOR_ASSERTIONS rises by the arm's executed count
New arm: tools/workflows/unattended-build.test.sh, RA7-2 · covers AC6 · the suppression branch taken out, then separately the guard reverted to the +set test · FLOOR_ASSERTIONS rises by the arm's executed count
New arm: tools/workflows/unattended-build.test.sh, RA6-1's two new sites and RA7-1 · covers AC7 · the re-run announcement taken out, then separately `exit $?` changed to `exit 0` · FLOOR_ASSERTIONS rises by the arm's executed count
New arm: tools/workflows/unattended-build.test.sh, RA7-4 · covers AC8 · `|| exit 2` replaced by `|| :` on adopt-unattended.sh's resolver line, then separately on the parity script's · FLOOR_ASSERTIONS rises by the arm's executed count

## 8. Open questions

- **F1 — With no python on the host, the parity script never reaches its new resolver refusal,
  because the fan-out step refuses first (§4). Does this unit move that step, so the brief's L4 arm
  can observe the parity half?**
  - (a) Leave the order. RA7-4 runs the adopter only. The parity half of L4 is recorded NOT
    OBSERVED, with §4's evidence that its refusal is unreachable under any python-less PATH. The
    `|| exit 2` stays as the guard for a launcher that answers one call and not the next.
  - (b) Move the `FANOUT_CAP` block, with its comment, to just after the citation check (S8). A host
    with no python is refused on the resolver's own reason instead of a fan-out answer polluted by
    the gate's notice, and RA7-4 arms both scripts as the brief asks. This reorders one refusal, and
    no arm in `tools/` reads the fan-out refusal's text.
  - Recommendation: (b). It satisfies all of the brief's L4 acceptance, gives a clearer message on
    the same failure, and needs no new surface. (a) is the smaller diff and leaves one brief
    criterion half-observed.

## 9. Revision log

- rev-1 · 2026-10-19 · initial draft from the unit's brief and unit 6's closing review. The
  citation charset check is a gated canonical because its two renderers are its second instance.
  The second derivation's check was dropped as unreachable. L4's staged break was found not to red
  an exit-code assertion, so the arm asserts the last line. The parity half was found unreachable
  under the current order, which F1 puts to the owner.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "refuse a substituted path value holding a character
outside the path charset before rendering"` ranked `derive_kit_paths` a SEAM with four installs,
defined in the five files this unit edits. `python tools/codebase-map/reuse_lookup.py "a kit
directory reached through a junction keeps its logical path when citations are derived"` ranked
`resolve_kit_dir` a SEAM at fan-in 11 with 71 installs. Its `absolute()` line is the spelling S1
copies. Those are the seams this unit extends: one line of the `derive_kit_paths` canonical and its
copies, and a sibling canonical in `tools/lib/render-doc.sh` gated by the same `PARITY_ROWS` table.
No existing seam fits the citation charset check. Each renderer's existing guard tests its own
named variables in a `case`, and neither reads `KIT_PATHS`. So `check_kit_cites` is new. The
gate-side seams are extended in place: RA6's layout and adopter steps in
`tools/workflows/unattended-build.test.sh` become `build_renamed` and `seed_unattended_kit`;
`mkfake`'s stub shape and section 2f's fixture shape in `tools/lib/resolve-python.test.sh` are
reused; and the link idiom of `tools/unattended/adopt-unattended.test.sh:551-566` is reused.

The recall probe returned this unit's brief, unit 6's spec and closing review, and unit 1's spec.
It also returned `TOOL-aUnmannedHelm-9`, the adopter's junction precedent that §4 cites. The review
and the code disagree in two places, both recorded in §4. The review's L4 says the base parity
script ran with no python, and the code says it refused at the fan-out step. The review's staged
break for L4 does not red the assertion it proposes.

The gotchas checklist for the touched paths selected these classes:

- `fixture-passes-by-finding-nothing`, which is why section 2h fails rather than skips without a link;
- `staged-break-substitutes-a-synthetic-value`, which is why each red half removes the shipped call
  or reverts the shipped line;
- `degradation-known-but-unreported`, which is L2's class;
- `two-answers-to-one-question`, which is H1's class;
- `empty-field-collapses-unless-it-is-last`, which is why `check_kit_cites` reads the value last;
- `test-oracle-read-from-a-historical-sha`, which is why only AC10's one-time probe, and no arm,
  compares against `a99b3f23`.

Recall terms used: `python tools/memory-recall/query.py "how does a junction-installed kit render
its harness citations, and what guards a receipt-held path substituted into a JS literal" --terms
"derive_kit_paths junction absolute resolve charset render_kit_cites PROTOCOL_PARITY_REPASS
resolve_python 9009 check-protocol-parity adopt-unattended"`
