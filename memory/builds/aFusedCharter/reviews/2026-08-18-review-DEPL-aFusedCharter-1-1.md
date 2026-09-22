# Tier-2 diff review — the cumulative aFusedCharter diff landing on main

**Reviewed range:** `bd6dd7f...HEAD` — the whole seven-unit convergence as it would land on `main`.

**Serves:** diff-review DEPL-aFusedCharter-1 PLAY-aFusedCharter-1 PLAY-aFusedCharter-2 PLAY-aFusedCharter-3 TOOL-aFusedCharter-1 TOOL-aFusedCharter-2 TOOL-aFusedCharter-3

**Review shape:** raw 36 · confirmed 31 · refuted 5 · unverified 0 · precision **0.86**.

Eight of the 31 confirmed are exact duplicate pairs raised by different skeptic batches, and one
further pair (`5`/`6`) is one root cause with two carriers where a single fix discharges both. Merged,
the report below carries **22 distinct defects: 2 blockers, 9 high, 7 medium, 4 low**. The merge is
recorded per-finding so the raw ids stay traceable.

---

## Verdict: BLOCKED

Both blockers are the same shape and they are the reason this cannot land as-is: **`render_playbook.py`
bakes node-local, worktree-local ambient state into a committed artifact that a new UNGUARDED gate leg
then byte-compares.** `.githooks/pre-push` sets `GATE_FULL=1`, so the leg runs on the authoritative bar
on every node. The consequence is not a cosmetic wrong string — it is that nodes `b`, `c` and `d` get a
permanently red bar and cannot push, the only in-band fix (re-render) rewrites `AGENTS.md` with the
re-rendering node's identity, and `AGENTS.md` is not in the `merge=rows` set, so each node's fix
hard-conflicts with the last one's. The build shipped a cross-node deadlock behind a green local bar.

The second theme is the cost of the v3.0 convergence itself. Deleting
`parallel-coding-governance.{customize,domain-rules}.md` was correct; **seven carriers still point at
them**, including the repo's front door (`README.md`), the charter every session reads (`AGENTS.md`),
the agent-facing install runbook (`WIRE-INTO-PROJECT.md`, twice), a kit README an adopter receives, the
kickoff engine's hand-back offer, and a gate's own remedy string. Four of those seven sit on a line the
diff itself edited — the filename was updated and the clause beside it was not. That is not seven
independent oversights; it is one missing gate, and it is the single highest-leverage left-shift in this
report.

The third theme is adopter-blindness in the three newly shipped gates. `render_playbook.py`,
`check-microformats.sh` and `check-line-length.sh` each declare a `[[gate_leg]]` that runs in a target
repo, and each of the three fails on install day in a scratch target — two with an uncaught traceback
rather than the Refusal their own docstrings promise. Every one was reproduced in a scratch install.

---

## Findings

| # | sev | site | defect | raw ids |
|---|---|---|---|---|
| B1 | **blocker** | `tools/playbook/render_playbook.py:82` | `derive_project_name` returns the WORKTREE name; committed `AGENTS.md:222` names a throwaway branch dir | 5, 6 |
| B2 | **blocker** | `tools/playbook/render_playbook.py:132` | `derive_machine` bakes `$USERNAME`/`$COMPUTERNAME` into the committed charter; the unguarded render leg then reds on every other node | 14, 1 |
| H1 | high | `tools/playbook/render_playbook.py:251,347` | the shipped renderer resolves its template and descriptors from gov's own layout, so it dies in any adopter with an uncaught `FileNotFoundError` | 15, 3 |
| H2 | high | `tools/playbook/render_playbook.py:281` | `kits` members are never validated; a typo silently deletes a whole kit section and `--check` stays green forever | 7, 17 |
| H3 | high | `tools/check-microformats.sh:24` | the leg passes no subject and the default is gov's repo-root filename, which no adopter has | 16, 22 |
| H4 | high | `tools/check-line-length.sh:104` | with no declaration — deliberately withheld from the payload — the leg's own no-argument invocation exits 2 | 23 |
| H5 | high | `tools/check-template-size.sh:109` | the over-budget remedy string names a deleted file, 1.4 KiB from firing | 24, 11 |
| H6 | high | `WIRE-INTO-PROJECT.md:608` | the Result tree still lists the deleted companion, contradicting §2 in the same document | 25, 10 |
| H7 | high | `README.md:14` | the front-door Contents bullet still tells a reader to copy two deleted files | 26 |
| H8 | high | `AGENTS.md:18,45` | the charter still describes itself as a template plus two companions | 27 |
| H9 | high | `tools/check-playbook-parity.sh:14` | the header still advertises the S3 catalogue class the same diff deleted | 33 |
| M1 | medium | `tools/check-line-length.sh:132` | `count_over`'s exit status is discarded, so a crashed scanner prints `line-length OK` and exits 0 | 2 |
| M2 | medium | `coding-governance-agents.template.md:84` | node-registry cells wrap every value in backticks and substitute verbatim; gov's own answer contains backticks | 8 |
| M3 | medium | `tools/govkit/entries/playbook.kit.toml:36` | the hole's `why` still says the placeholders span BOTH files; the discharge beside it names one | 12, 21 |
| M4 | medium | `tools/agent-instructions/README.md:59` | one two-line hunk contains both answers to one question | 28 |
| M5 | medium | `WIRE-INTO-PROJECT.md:39,670` | two live citations of `.customize.md`, one load-bearing for the mandate re-pull | 30 |
| M6 | medium | `skills/session-kickoff/SKILL.md:273` | the hand-back offer points at a "Customize before use" block that no longer exists | 31 |
| M7 | medium | `tools/memory-tree/README.md:172` | half the line was updated; the `domain-rules.md` §7/§10/§12 pointer was not | 32 |
| L1 | low | `tools/check-placeholders.sh:68` | the trailing `exit "$rc"` was deleted; the verdict is now an accident of the last command | 4, 34 |
| L2 | low | `tools/playbook/render_playbook.py:213` | `keep_fences` is written twice and never read, inside the function that decides what survives a render | 20 |
| L3 | low | `tools/check-microformats.sh:74` | the `⏳` escape is unreachable by construction — armed-but-unreachable rule | 35 |
| L4 | low | `tools/check-placeholders.test.sh:40` | dead companion fixtures, an orphaned `marker` fixture, and a `--check` arm passing the same path twice | 36 |

---

## Blockers

### B1 — `tools/playbook/render_playbook.py:82` · the project name is the worktree directory name

*(raw 5 + 6 merged: the probe and the artifact it produced. One fix discharges both.)*

`derive_project_name` is `root.resolve().name` — the exact worktree-sensitivity the sibling
`derive_primary_tree` carries a five-line comment about having fixed via `--git-common-dir`. Measured in
this worktree: `derive_project_name` → `governance-template-convergence-91c2c6`, while
`derive_primary_tree` correctly → `C:/projects/coding-governance`.

The committed artifact carries the result. `AGENTS.md:222` — inside the generated
`<!-- gov:playbook -->` region — reads ``…preamble for `governance-template-convergence-91c2c6` ``. The
charter every session reads opens by identifying a throwaway branch directory as the product, and the
value changes with whatever worktree the next render runs in, so the region is not reproducible.

Because the new `playbook render wiring` leg runs `adopt-playbook.sh --target . --check`, a render from
the primary tree derives `coding-governance` and the leg reports DRIFT. Verified by forcing
`PROBES['project_name'] = 'coding-governance'` and re-rendering: **no match** against the committed
`AGENTS.md`. The leg is unguarded and pre-push sets `GATE_FULL=1`, so the full bar reds on `main` the
moment this lands.

**Fix.** Derive it from the primary tree, not the current one:
`return Path(derive_primary_tree(root, _a)).name or root.resolve().name`. Then re-render `AGENTS.md`
from the PRIMARY tree and commit the corrected region.

**Left-shift.** A `render_playbook.py --selftest` arm that renders twice from two directory names
sharing one `--git-common-dir` and asserts the two outputs are byte-identical. Every `derive_*` probe
in this module is a candidate for that arm; two of the three shipped ones failed it.

### B2 — `tools/playbook/render_playbook.py:132` · the machine identity is read from the environment

*(raw 14 + 1 merged.)*

`derive_machine` reads `$USERNAME`/`$COMPUTERNAME` with no target-repo input. `MACHINE_A` is declared
`class=derived probe=machine` in `tools/govkit/entries/playbook.kit.toml:118-120` and `deploy.toml`
supplies no `machine_a` answer, so the probe always wins — the answer path at `render_playbook.py:306`
only fires when the probe comes back empty. `AGENTS.md:153` now carries `daily-agent @ COMPEETO-AGENT`,
captured from node `a`'s environment and pushed to a public GitHub remote; the hand-authored node
registry never disclosed that hostname.

Reproduced verbatim:

```
$ COMPUTERNAME=DESKTOP-3J1O6CD USERNAME=agent5 bash tools/playbook/adopt-playbook.sh --target . --check
render-playbook: DRIFT — the charter region differs from a fresh render
$ echo $?
1
```

The same command with this machine's environment prints OK, rc=0. The `playbook render wiring` leg
(`tools/gate-legs.json:729`) carries **no `guard` key** — confirmed by dumping the manifest — and
`run-gates.sh:130`'s `[ -z "${guards[$i]}" ] && continue` means an unguarded leg always runs; pre-push
sets `GATE_FULL=1`, which bypasses guards regardless. So nodes `b`/`c`/`d` in the registry get a
permanently red bar and a blocked push for a reason that is not drift.

Worse, the only in-band remedy is self-defeating. Whichever node re-renders to go green flips the
others red, and `.gitattributes` routes only `memory/DECISIONS.md` and `memory/backlog/*.md` through
`merge=rows` — `AGENTS.md` is pinned `eol=lf` with no merge driver, so cross-node re-renders of that row
hard-conflict on every merge. `TAG_A` has the same class: `derive_node_tag` hardcodes `'a'` at line 128.

**Fix.** Reclassify `MACHINE_A`, `PRIMARY_TREE_A` and `TAG_A` as `asked` in
`tools/govkit/entries/playbook.kit.toml`, so the node-registry row comes from the committed
`deploy.toml` and is identical on every node; delete `derive_machine`'s environment read. If the probe
must survive, fence the node-registry row set so `--check` compares only node-invariant bytes.

**Left-shift.** Add a leg arm — or a `--selftest` arm — that re-runs `--check` under a scrubbed
environment (`env -i` plus a fabricated `USERNAME`/`COMPUTERNAME`) and asserts the same verdict. A gate
that byte-compares a rendered artifact is only meaningful if it is proven insensitive to the renderer's
ambient state; nothing in this diff proves that, which is why a green local bar shipped a cross-node
deadlock.

---

## High

### H1 — `tools/playbook/render_playbook.py:251,347` · the shipped renderer only works inside gov

*(raw 15 + 3 merged.)*

`gov_root` is computed as `Path(__file__).resolve().parent.parent.parent` — the *installed* file's
grandparent, i.e. the target's repo root. From there the engine hardcodes
`gov_root/coding-governance-agents.template.md` (line 347) and `load_declarations` reads
`gov_root/tools/govkit/entries/playbook.kit.toml` + `gov_root/tools/govkit/registry.toml` (line 251).
Neither exists in an adopter: `tools/govkit` is a registry `[[exempt]]` path documented as "the deployer
itself … never installed into a target" (`registry.toml:206-208`), and the `playbook` entry writes the
template to the operator-chosen `{playbook_path}` (govkit's own selftest lands it at `docs/PARALLEL.md`),
never to the repo root.

Reproduced twice in scratch installs. Install 1 (playbook kit only):
`FileNotFoundError: .../tools/govkit/entries/playbook.kit.toml`, rc=1. Install 2 (with `tools/govkit`
copied in): `FileNotFoundError: .../coding-governance-agents.template.md`. Both escape `main`'s
`except Refusal` at line 362 as raw tracebacks, bypassing the docstring's stated refusal contract that
"every one names what the operator must supply". `tools/playbook/kit.toml` ships `**` to
`{prefix}/playbook/` and declares `[adopt]`, `[check]` AND a `[[gate_leg]]` all running
`--target . --check`, so an adopter inherits three broken entry points and a permanently red bar leg.

**Fix.** Read the template path and the descriptor location from the target's
`.governance/deploy.toml` (`prefix`, plus the `playbook_path` govkit already resolved) rather than from
`__file__`'s grandparent, and wrap the template/descriptor reads so a missing input raises `Refusal`
naming the path it wanted. Alternatively drop `[adopt]`/`[check]`/`[[gate_leg]]` from
`tools/playbook/kit.toml` and mark the entry gov-only — but the leg is the point of the unit, so the
first route is the real one.

**Left-shift.** `tools/govkit/matrix.py` already drives the deployer against four repo shapes and
asserts messages rather than exit codes. Add a fifth shape: install the playbook kit into a scratch
target and run its declared `[check]` argv, asserting a Refusal *message* — not rc — so a traceback
fails the arm. Every kit that declares a `[[gate_leg]]` deserves that arm; three of the three new gates
in this diff would have failed it.

### H2 — `tools/playbook/render_playbook.py:281` · a misspelled kit id silently deletes a charter section

*(raw 7 + 17 merged.)*

`render()` validates `drop_blocks` members **twice** — against the declared block list (~line 271) and
against the fences actually present (~line 277). `kits` gets neither. Line 281 computes the drop set as
`{('kit', name) for ns, name in present if ns == 'kit' and name not in kits}` with no membership check
in either direction, though the same function already holds `entries` from `load_declarations()`.

Live evidence: `.governance/deploy.toml`'s `kits` array contains `govkit`, which is neither a registry
entry id nor one of the three kit fence names (`codebase-map`, `lexicon`, `unattended`). It selects
nothing and `python tools/playbook/render_playbook.py --target . --check` exits 0 without a word.
Simulated the typo by rewriting `codebase-map` → `codebasemap` in the parsed set: no Refusal, notes
contained `dropped kit:codebase-map`, and the whole codebase-map ruleset vanished from the rendered
body. `--check` re-renders from the same `deploy.toml`, so it stays green forever.

This is precisely the "unrecognised name that reads as success" the module docstring (lines 29-31) says
both namespaces refuse. `govkit`'s own `resolve_selection` DOES refuse a non-entry id
(`govkit.py:414-420`), but it never reads `deploy.toml`'s top-level `kits` array — only intake writes it,
and intake refuses to rewrite an existing descriptor, so a hand-edited `deploy.toml` reaches the renderer
unvalidated.

**Fix.** Mirror the `drop_blocks` loop: after `kits = set(...)`, refuse any member not in `entries`, and
(once fences are known) any member matching no `kit:` fence. Then correct or remove `govkit` from
`.governance/deploy.toml`.

**Left-shift.** A `--selftest` arm per namespace asserting that an unknown member raises `Refusal`. The
`drop_blocks` half has one; the symmetry gap between two adjacent namespaces in one function is exactly
what a paired arm catches.

### H3 — `tools/check-microformats.sh:24` · the leg can never find its subject in an adopter

*(raw 16 + 22 merged.)*

`FILE=${1:-coding-governance-agents.template.md}`, resolved against the target's git toplevel, with
line 34 exiting 2 on absence and no fallback search. The descriptor's leg
(`tools/govkit/entries/check-microformats.kit.toml:36-38`) is
`argv = ["bash", "{prefix}/check-microformats.sh"]` — no subject, no guard — and govkit only
token-substitutes what appears IN the argv, so nothing supplies a path. Grep of `tools/govkit/*.py`
confirms nothing appends one. The entry `requires = ["playbook"]`, and the playbook entry's one
`[[files]]` rule lands the charter at `{playbook_path}` (`selftest.py:437` confirms `docs/PARALLEL.md`),
so that root filename is never present in an adopter.

Reproduced in a bare scratch repo holding only the gate:
`check-microformats: no such file: coding-governance-agents.template.md`, rc=2. The descriptor's own
`why_no_adopter` claims the gate "reads the charter template wherever the playbook entry put it" — a
message naming an escape the code does not implement.

**Fix.** `argv = ["bash", "{prefix}/check-microformats.sh", "{playbook_path}"]`. `{playbook_path}` is
already an intake answer token; the plumbing exists and is simply not connected. Keep the gov filename
only as the last fallback.

**Left-shift.** Same arm as H1: run every declared `[[gate_leg]]` argv inside a scratch install and
require green. A leg that has never been executed anywhere but gov's own root is an untested leg.

### H4 — `tools/check-line-length.sh:104` · no declaration means exit 2, not the documented default

Line 104 exits 2 when no positional is given and `$DECL` is absent; line 109 exits 2 when the
declaration selects no subject. The kit's gate leg is `argv = ["bash", "{prefix}/check-line-length.sh"]`
— no argument, no guard. Both `tools/govkit/entries/check-line-length.kit.toml:6-10` and
`tools/line-length-limits.txt`'s own header state the declaration is deliberately withheld from the
payload *precisely to avoid a red on install day*, promising "an adopter's declaration is theirs to
write, and a subject with no row is graded at the 450 default".

Reproduced in a bare scratch repo: rc=2 with no declaration, and rc=2 again with a comment-only
declaration. There is no green path for an adopter until they hand-author at least one row — the
withheld-payload decision reproduces the very failure it was made to prevent, through the other door.

**Fix.** Make an absent declaration a `NOT ADOPTED` exit 0 — the `tools/lexicon/lexicon.py` posture this
repo already uses for an opt-in gate — or have `govkit apply` seed a commented-empty declaration in the
target the way `check-install-prefix`'s registry ships seeded-empty. Keep exit 2 only for a declaration
that exists and selects nothing.

**Left-shift.** The scratch-install leg arm again (H1), plus an explicit arm in
`check-line-length.test.sh` for the zero-declaration case. Note that "the kit withholds the file"
and "the gate needs the file" were decided in two different documents and never joined; a single arm
that runs the shipped leg against the shipped payload joins them mechanically.

### H5 — `tools/check-template-size.sh:109` · the over-budget remedy names a deleted file

The `fail 2` message tells the operator to "move an activity-scoped section to
`parallel-coding-governance.domain-rules.md` (leaving a §-stub pointer), per the v2.3 pattern". That file
was deleted in `5b00666`; `git ls-files | grep domain-rules` returns nothing, and
`grep -c domain-rules coding-governance-agents.template.md` is 0, so no §-stub target exists either.
Line 5's header carries the same two dead companion names.

This is a **remedy string** — the exact carrier `tools/check-install-prefix.sh`'s own header names as
what strands a reader ("a runbook step, a usage header, a remedy string"). The branch is live and close:
the charter measures 47 677 bytes against a 49 152 ceiling, so the message fires on ~1.4 KiB of growth,
at the one moment someone actually needs a followable instruction.

**Fix.** Rewrite the remedy to the v3.0 mechanism already stated at `memory/guides/SESSION-KICKOFF.md:135`
— "drop a conditional block, or trim non-instructional prose" — and delete the companion names from the
line-5 header.

**Left-shift.** See the shared gate proposed under H6-H9 below: a deleted-path scan over
non-`memory/` text. `check-install-prefix.sh` already owns the "dead path spelled in a shipped string"
class; the missing half is a path that is dead because it was *deleted*, not because it was
wrongly-prefixed.

### H6 — `WIRE-INTO-PROJECT.md:608` · the install runbook contradicts itself 532 lines apart

The "Result — what the project now has" tree still lists
`docs/parallel-coding-governance.domain-rules.md  # the §4/§9–§13 domain checklists (travels with the
template)`, and `git diff main...HEAD` shows that region untouched while §2 was rewritten. Line 76 now
states "The charter is ONE file and it BECOMES the project's AGENTS.md. There is no companion to ship."
Two contradicting answers in one runbook.

`tools/govkit/selftest.py:437` was updated in this same diff to assert "the playbook entry lands its one
file", so the runbook's post-install verification tree and its own acceptance arm now disagree about
what ships. An agent following the diagram will look for — or fabricate — a file gov no longer produces.

**Fix.** Delete that row from the tree diagram; if the rendered charter is the deliverable, replace it
with the `AGENTS.md` region the renderer writes. Check the surrounding §3/§9 prose for other two-file
assumptions.

**Left-shift.** Shared with H5/H7/H8/M4-M7 — see below.

### H7 — `README.md:14` · the front door instructs copying two deleted files

The diff to `README.md` is literally one line: `parallel-coding-governance.template.md` →
`coding-governance-agents.template.md` at line 11. Lines 13-15 immediately below still read "Two
companions ship with it: **`.customize.md`** … and **`.domain-rules.md`** … copy it alongside the
template into a target repo". Both named files are deleted. The repo's front door states a shipped-product
shape (three files) that `tools/govkit/entries/playbook.kit.toml` now declares as one.

**Fix.** Collapse the bullet to the single charter template and point at
`tools/playbook/adopt-playbook.sh` as the install path, matching `playbook.kit.toml`'s "ONE file as
of v3.0".

### H8 — `AGENTS.md:18,45` · the charter still describes itself as a template plus two companions

Line 18: "Companions: `.customize.md` (deploy-time placeholder catalog) and `.domain-rules.md` (the
§1/§4/§7–§13 activity-scoped checklists the template references by §-stub …)". Line 45: the root holds
"the product template + its two companions". Both sit BEFORE the `<!-- gov:playbook -->` marker at line
75, so they are **authored slots**, not rendered region — hand-maintained stale text in the same bullet
whose first line the diff updated.

This is the document every session reads first, and it points sessions at §-stubs into nothing.

**Fix.** Delete the companion clause on line 18 and the "+ its two companions" tail on line 45. If the
§-stub story still matters, restate it as the conditional `kit:`/`when:` blocks the renderer drops.

### H9 — `tools/check-playbook-parity.sh:14` · the gate advertises a predicate it no longer runs

Line 14 still enumerates "S3 catalogue — the placeholder counts `customize.md` states equal the measured
sets" as one of the three classes the gate holds. `git diff 497d25d..HEAD` shows the entire S3 stage
deleted along with fail branches 8-13. The surviving script ends at the S2 pair loop; the replacement
comment at line 152 even says "The catalogue stage above" for a stage that is no longer above it. Line 20
sources the gate's anti-vacuity rule from `parallel-coding-governance.domain-rules.md`, which this build
deleted.

The record moved correctly — `.memory-tree.conf`'s `ARMS_FLOORS` dropped 15:15 → 9:9 with a comment
naming the deletion — while the gate's own header did not, so the two disagree about the same gate. Live
run: `playbook-parity OK — 14 kit(s) documented or waived · pairs in agreement` — no catalogue clause in
the verdict either. A reader (or a future review) trusting the header believes the catalogue arithmetic
is still machine-checked. It is not.

**Fix.** Delete the S3 line from the WHY block and re-source the anti-vacuity quotation from the charter
template, or from `memory/gotchas/vacuous-selector-empty-population.md`, which now owns that class.

---

### The shared left-shift for H5-H9 and M3-M7 (ten of the twenty-two)

Ten findings are one class: **a file was deleted and the carriers that name it were not updated**. Four
of them sit on a line the diff itself edited. This is the highest-leverage gate in the report and it is
cheap:

> A leg that, for every path deleted in the diff's range, greps the tracked non-`memory/` corpus for the
> deleted basename and reds on any hit not covered by a shrink-only waiver registry.

The population is derivable (`git diff --diff-filter=D --name-only <base>..<head>`), the haystack is the
same one `check-install-prefix.sh` already walks, and the waiver shape is the one used four times
elsewhere in this tree. Scoped to the diff it costs nothing on a records-only commit; run under
`GATE_FULL=1` it grades the whole corpus. Had it existed, this diff would have arrived with ten fewer
findings and two fewer runbook contradictions — and `memory/archive/` snapshots, which legitimately name
the deleted files, are excluded by the existing `memory/` scope rule.

---

## Medium

### M1 — `tools/check-line-length.sh:132` · a crashed scanner reports `line-length OK`

`over=$(count_over "$f" "$limit")` discards the scanner's status; line 133's
`n=$(... | grep -c . || true)` turns an empty result into 0; the else branch at 140 certifies. The
resolved limit is validated only when it comes from the declaration (line 116 covers `declared` alone),
so the positional `$2` and `LINE_MAX` — both documented invocations in the file's own usage header at
lines 5-6 — are unvalidated.

Reproduced exactly:

```
$ bash tools/check-line-length.sh AGENTS.md abc
  <Python ValueError traceback>
  line-length OK — …: 0 over 0 characters      # rc=0
$ LINE_MAX=abc bash tools/check-line-length.sh README.md
  <same>                                        # rc=0
```

`over` is empty on any scanner failure — bad limit, unreadable file, interpreter death, deleted temp
scan — so the gate certifies a subject it never measured. That is the "green because nothing was
measured" class this tree bans by name, and it also violates the script's own stated contract at line 34
("2 = could not run").

**Fix.**
`over=$(count_over "$f" "$limit") || { fail 4 "the offender scan did not run for $f, so no line was measured"; continue; }`,
and apply the existing `grep -qE '^[0-9]+$'` numeric guard to the resolved `$limit`, covering the
positional and `LINE_MAX` paths, not only `$declared`.

**Left-shift.** `check-arms.py` already requires every `fail` branch to be armed by a positive
assertion naming its own failure text; a `fail 4` here brings the branch under that existing gate for
free. Beyond that: an arm that hands the gate a deliberately un-runnable subject and asserts a
non-zero, non-certifying verdict. Every gate in this tree that shells out to a scanner wants that arm.

### M2 — `coding-governance-agents.template.md:84` · table cells are substituted without escaping

Line 84 is
`` | `{{TAG_A}}` | `{{MACHINE_A}}` | `{{PRIMARY_TREE_A}}` | `{{WORKTREE_ROOT_A}}` | `{{VARIANCES_A}}` | ``.
`VARIANCES_A` is `class=asked` (descriptor lines 138-140), substituted verbatim at
`render_playbook.py:331` with no escaping, and gov's own `deploy.toml` answer contains backticks. So
`AGENTS.md:153` renders raw as
`` `remote `origin`; Windows + Git-Bash, so give `git -C` forward-slash paths` ``, which CommonMark
parses as a code span "remote ", bare text "origin", then further broken spans. The §2 table an agent is
told to identify its node from is unreadable, and any answer containing a backtick or a pipe corrupts its
cell the same way.

**Fix.** Escape values destined for a table cell in `render()` — at minimum `|` → `\|`, and refuse or
strip backticks in an answer — or drop the backtick wrapping around `{{VARIANCES_A}}` in the template
and remove the backticks from the `deploy.toml` answer.

**Left-shift.** A `--selftest` arm that renders a fixture answer containing `` ` ``, `|` and a newline,
and asserts the rendered row still parses as one table row with the expected cell count. Substitution
into a structured host format is a category the renderer will meet again for every future `asked` key.

### M3 — `tools/govkit/entries/playbook.kit.toml:36` · the hole's `why` describes a probe that no longer exists

*(raw 12 + 21 merged.)*

The `[[hole]]`'s `why` still reads "the placeholders span BOTH deployed files … a probe naming only the
main file was MEASURED going false-green while the companion sat unfilled, which is why both operands are
named", while the `discharge` on line 37 names exactly one operand, `{playbook_path}`. The entry's own
header (lines 9-14) says "ONE file as of v3.0. The charter converged and the domain companion was
deleted", and `[[files]] include` lists exactly one file.

The reason string is the sole record of what this probe covers, so a later reader either widens the probe
back to a file that is gone — the `why` explicitly invites it — or distrusts the reason. The truncated
comment at lines 6-9 ("What ships is the charter template, and / # the old note read:") also trails off
mid-sentence.

**Fix.** Rewrite the `why` for the single-file entry, keeping the false-green history as a past-tense
note rather than a claim about the current operands; finish the truncated comment.

### M4 — `tools/agent-instructions/README.md:59` · both answers to one question in one two-line hunk

Line 59: "fill `coding-governance-agents.template.md` per its customize companion". Line 60, added in the
same hunk: "The charter is ONE file as of v3.0 — there is no companion to copy alongside (the §-stubs
reference it)". The trailing parenthetical is an orphaned fragment of the deleted clause with no
antecedent. The correct instruction — `tools/playbook/adopt-playbook.sh --target <repo>` — appears
nowhere in this file.

**Fix.** Replace "per its customize companion" with a pointer to `tools/playbook/adopt-playbook.sh`,
which is now the thing that fills the placeholders.

### M5 — `WIRE-INTO-PROJECT.md:39,670` · two live citations of the deleted customize companion

Line 39 was edited by this diff (the template name changed) while the corroboration beside it — "and
`.customize.md` says it twice" — was left pointing at a deleted file. It is live §0 precondition text,
not a historical note. Line 670 — "read the customize companion's conditional-sections row first" — is
load-bearing procedure inside the v2.6 unattended-mandate re-pull, and the conditional-sections concept
now lives as `drop_blocks` in `deploy.toml` per WIRE §2 line 130.

**Fix.** Drop the corroboration on line 39; on line 670 point at the new §2 "The two blocks that are not
about a kit" section and at `drop_blocks` in the target's `deploy.toml`.

### M6 — `skills/session-kickoff/SKILL.md:273` · the hand-back points at a block that does not exist

Line 273 names the playbook template "per its OWN 'Customize before use' block"; grep for that string in
`coding-governance-agents.template.md` exits 1. The diff touched this exact line to update the filename
and left the dead reference. The kickoff engine is installed per-machine and is what offers playbook
adoption to a fresh project, so it now instructs an agent to follow a block that does not exist. The
template's own header already states the v3.0 answer: "`tools/playbook/adopt-playbook.sh` fills every
placeholder and drops the blocks a target has no kit for".

**Fix.** Replace the parenthetical with `via tools/playbook/adopt-playbook.sh --target <repo>`.

### M7 — `tools/memory-tree/README.md:172` · half the line was updated

The diff for this file is one line: the template name was changed while
`` + `…domain-rules.md` §7, §10, §12 `` on the same line was kept. This is the adopter-facing kit
README's governing-docs list, routing readers to sections of a deleted file for the DoR/DoD/landing
rules it promises.

**Fix.** Drop the `…domain-rules.md` clause and fold its section numbers into the charter reference if
those sections survive there.

---

## Low

### L1 — `tools/check-placeholders.sh:68` · the trailing `exit "$rc"` was deleted

*(raw 4 + 34 merged.)*

The file is exactly 68 lines; the last statement is
`[ "$rc" -eq 0 ] && echo "check-placeholders OK — one marker carrier at $marker"` with no trailing
`exit "$rc"`. `git log -p --follow` carries the `-exit "$rc"` hunk; `od -c` on the tail confirms the file
ends immediately after that line. There is no `set -e`, so the script's status is the last command's.

It is correct **today** only by short-circuit accident: `rc=1` makes the `[` fail and the AND-list
returns 1. The asymmetry is internal to the file — the `--check` branch 29 lines above still ends with an
explicit `exit "$rc"` at line 39 — so the two modes now produce verdicts by different mechanisms, and
any line appended below line 68 (a trailing `echo`, a cleanup `rm -f`, a `trap`, a `true`) silently makes
the marker gate always-green while still printing its failure text. The `playbook placeholder catalogue`
leg runs this script bare, so that always-green would land on the bar. No arm in
`check-placeholders.test.sh` asserts exit-code provenance.

**Fix.** Restore `exit "$rc"` as the last line, matching the `--check` branch. One line.

**Left-shift.** A repo-wide shell-hygiene predicate: every gate script under `tools/` ends in an
explicit `exit`. `tools/gate-lint/ps-hygiene.py` already owns the "silently misbehaving script" class for
PowerShell; this is its sh sibling and the population is derivable from `tools/gate-legs.json`.

### L2 — `tools/playbook/render_playbook.py:213` · `keep_fences` is written twice and never read

Line 205 `out, skip_depth, keep_fences = [], 0, True`; line 213
`keep_fences = False  # a surviving block loses its markers in the render`; line 223 `del keep_fences`.
`grep -n keep_fences` returns exactly those three lines. Both fence branches `continue`
unconditionally regardless of it. Dead plumbing inside the one function that decides which charter
sections survive a render — a reader has to prove it is inert before trusting the drop logic around it —
and the comment on line 213 documents an intent the code no longer implements.

**Fix.** Delete lines 205's initialiser, 213 and 223.

### L3 — `tools/check-microformats.sh:74` · the `⏳` escape is unreachable by construction

`case "$head" in *" "*) [ "$head" = "⏳" ] || fail 3 …`. Re-ran the gate's own derivation
(`head=${body%% — *}`) over the live microformats block: all 11 heads print space-free, and the
hourglass definition yields head exactly `⏳` (bytes `e2 8f b3`, no space). The case arm therefore never
matches it, so the equality is never evaluated — the two conditions are mutually exclusive by
construction. Even the adversarial near-miss (`⏳  — x`, double space) yields head `⏳ ` with a trailing
space, which matches the arm but fails the equality and still reds. The guard's true branch cannot be
taken under any input.

`check-microformats.test.sh` carries 13 arms, none of which puts `⏳` in a fixture, so nothing notices.
This is `memory/gotchas/armed-but-unreachable-rule.md`, a named class in this tree: a reader believes
`⏳` is specially admitted by the position predicate when it is admitted only because the predicate does
not look at it.

**Fix.** Delete the `[ "$head" = "⏳" ] ||` guard — the position predicate already passes `⏳`. If a
non-keyword head is genuinely meant to be admitted, restate the exemption as a declared set the test can
exercise.

**Left-shift.** The existing `check-arms.py` requires an arm per `fail` branch; the gap here is one
level down — an arm that proves the *escape* inside a branch is reachable. Cheapest version: require a
fixture per named exemption, so an exemption with no fixture is itself a finding.

### L4 — `tools/check-placeholders.test.sh:40` · dead fixtures and a duplicated operand

Three structural problems, all verified:

1. `mkfixture` (lines 39-41) still writes `parallel-coding-governance.domain-rules.md` and
   `parallel-coding-governance.customize.md`; the gate under test now reads only
   `coding-governance-agents.template.md`. Those two files and the whole `GOOD_CAT` catalogue body they
   carry are dead fixture material.
2. `grep -n 'TMPROOT/marker'` returns exactly two hits — lines 63 and 64, the `mkfixture` write and its
   `git commit`. The diff deleted both the `sed` that broke it and the
   `arm "red: the two marker-carrying files disagree"` that consumed it, leaving an orphan git-init/commit
   under a now-false comment reading `# 2. the lockstep — the whole point of the marker`.
3. Line 92 passes `$ROOT/coding-governance-agents.template.md` as **both** operands of `--check`, so the
   arm would pass identically if the loop read only `$2`. No arm anywhere in the suite puts a surviving
   placeholder in the FIRST position, so the two-file iteration is genuinely unproven in that direction.

**Fix.** Delete the two companion writes and the orphan `$TMPROOT/marker` block; give the `--check` arm
two distinct fixture files so the second operand is actually exercised.

**Note on one sub-claim.** The raw finding said the suite's `PASS (N assertions)` count still includes
the weakened arm. The shape is wrong — this suite prints `check-placeholders.test OK — N arm(s)` and is
waived from the counted shape at `memory/project/testsuite-count-waivers.txt:26`. The substance survives:
the weakened arm still increments the reported total.

---

## Disposition

Land nothing until B1 and B2 are fixed and `AGENTS.md` is re-rendered **from the primary tree**. Those
two plus H1-H3 are one afternoon; H5-H9 and M3-M7 are ten one-line text edits that the proposed
deleted-path gate should be written alongside, so the eleventh carrier reds instead of shipping. M1, M2
and L1 are small and independent. L2-L4 are cleanup.

The two gates worth building out of this review, in order of leverage:

1. **Deleted-path carrier scan** — catches ten of twenty-two findings, and is the difference between "the
   convergence was correct" and "the convergence half-landed in eleven files".
2. **Scratch-install leg execution** — a fifth shape in `tools/govkit/matrix.py` that runs every declared
   `[[gate_leg]]` argv inside a real scratch target and asserts a message, never an exit code alone.
   Catches H1, H3 and H4, and would have caught them on install day rather than on an adopter's.

A distant third, but the one that would have caught both blockers: **render determinism** — render twice
under two scrubbed environments and two directory names sharing a `--git-common-dir`, and assert the
bytes are identical. A gate that byte-compares a generated artifact is only as good as the proof that the
artifact does not depend on who generated it.
