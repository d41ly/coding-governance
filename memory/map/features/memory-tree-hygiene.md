# memory-tree hygiene engine — the gate over the memory tree

```toml
feature = "memory-tree-hygiene"
title = "check-memory-hygiene.sh: the memory tree's structural gate, its per-class size caps, and the epoch that dates its verdicts"
status = "shipped"
streams = ["tooling"]
decisions = ["TOOL-aRelaxedShard-1", "TOOL-aWidenedGuide-1", "TOOL-dDerivedDocket-31"]

[claims]
gate-legs = ["memory hygiene", "memory-hygiene self-test", "verdict epoch (kit version dates the engine)", "verdict-epoch self-test", "kit version markers", "kit/dogfood doc parity", "transition-audit arms", "backlog migration selftest", "straggler-guard arms", "routed commits name a specced unit", "routed-commits selftest"]
kits = ["memory-tree"]
git-hooks = ["commit-msg", "pre-rebase"]
harness-hooks = []
workflow-scripts = []
skill-engines = []
rendered-skills = []
gotcha-classes = ["a-grep-for-a-word-is-a-presence-probe.md",
  "suite-edited-while-bash-executes-it.md", "ledger-token-wrapped-across-a-line-joins-nothing.md", "inline-fence-swallows-the-rest-of-the-file.md",
  "record-citing-a-foreign-id-defines-or-orphans-it.md", "swallowed-delegate-reads-as-clean.md",
  "waiver-row-that-hides-nothing-reds.md", "pin-gated-checks-arm-nothing-without-a-pin.md",
  "record-without-serves-or-with-a-round-counter.md", "sourced-conf-blank-overrides-the-default.md",
  "history-leg-graded-before-the-reconcile-commit.md"]
guides = []
backlog-shards = []
lexicon-verbs = []
[paths]
globs = [
  "tools/memory-tree/check-memory-hygiene.sh",
  "tools/memory-tree/check-memory-hygiene.test.sh",
  "tools/memory-tree/check-verdict-epoch.sh",
  "tools/memory-tree/transition_audit.py",
  "tools/memory-tree/transition-audit.test.sh",
  "tools/memory-tree/migrate_backlog.py",
  "tools/memory-tree/routed_commits.py",
  ".githooks/commit-msg",
  ".githooks/pre-rebase",
  ".githooks/straggler-guard.sh",
  ".githooks/straggler-guard.test.sh",
]
```

## What it is

One shell engine over the tracked contents of `<MEMORY_ROOT>/`, plus the epoch rule that makes its
verdicts datable. How many numbered checks it carries is derivable from the engine and is not
written here. Several of them delegate to sibling
Python modules (`gen_build_index.py`, `corpus_ids.py`, `gotchas.py`, `row_grammar.py`, `transition_audit.py`);
this dossier owns the engine, its self-test, the epoch and the transition audit, not the other modules.
Of those, `gotchas.py` is the one a review reads: it reads the by-design block at the subject's base
(`TOOL-aGraftedHelix-29`), so an invariant a change moves reaches that change's review as a checklist
item and never as an exemption.

**One leg here belongs to a module this dossier does NOT own**, deliberately. `backlog migration selftest` runs `migrate_backlog.py --selftest`, the
suite of the shards-to-builds migration PLANNER and of the relocation ENGINE that lives beside it in
the same module. The leg is CLAIMED here because that module has no dossier of its own and an
unclaimed key reds the map's coverage gate; it is DECLARED in `tools/memory-tree/kit.toml` beside
its module-selftest siblings rather than exempted in the govkit registry, because the module
ships to every memory-tree adopter and each of them runs `--plan` in their own deployer build
(`TOOL-dDerivedDocket-11` fork F8). It is held like those siblings, by `subject = kit`, so no plain
bar executes it. Its ceiling is pinned at or under the direct-check bound the unattended kit's
gate-guard suite grades every `--selftest` leg against, which is what keeps the flag form a check a
unit pass may run by hand.

**The engine's relationship to the transition audit this dossier DOES own is one direction only**
(`TOOL-dDerivedDocket-12`). `migrate_backlog.py --relocate`, `--repair` and `--ingest` move a
pre-flip branch's row changes into the per-build files and write the `RELOCATED` rows check 26
reads; `--stragglers` lists the refs that still owe one and `--recipe` prints the one relocation
recipe every carrier quotes. All three writing verbs CALL `transition_audit.delta` and
`transition_audit.accounted` and spell no second transition rule, so the audit and the repair that
answers it cannot disagree about what a row change is. That module's CLI resolves its repository
from its own file location, which is why the engine's fixture arms call it in process against an
explicit root — a subprocess launched inside a fixture audits THIS tree instead and returns a clean
verdict about the wrong one. `--write` (`TOOL-dDerivedDocket-34`) is the switch-over: it feeds the
same engine the whole legacy corpus as new entries from an empty base, files the triage ask,
re-reads what it wrote to prove conservation, and only then removes the authored shards.

The self-test's project-key arms run the engine over
the suite's own scratch tree, one invocation per arm, never over an archive of this repository
(`TOOL-aRatifiedRulings-3`), so a red in the live corpus cannot red an arm that grades a conf key.
Three arms in that block grade the SHIPPED `.memory-tree.conf.example` instead, and they are
parity rather than behaviour: every key the engine validates, every bare `*_CUTOFF` it presets, and
every key the kit's PYTHON modules read out of a dict (`TOOL-dDerivedDocket-50`) must be declared
there, or named on that arm's own exemption list, which is asserted in both directions so a
name nothing reads any more reds too. The python arm's receiver is deliberately UNCONSTRAINED: a
module reaching for a SECOND kit's conf cannot bind it to `conf`, that name being taken by its own,
so a `conf`-anchored derivation is blind to exactly the cross-kit read the arm exists to catch. Its
population is derived from the module text and REFUSES when it finds no key at all, and a fixture
directory holding two deliberately undeclared keys is what proves both halves fire.

The engine is COPY-INSTALLED as a standalone directory, so it carries the python resolver inline and
derives its own prefix. It never reads its identity from a project conf: `KIT_MEMORY_TREE_VERSION` is
set in the file, because a project conf must not be able to spoof which engine graded a tree.

## The size caps — four classes, one line bound

| class | byte bound | line bound |
|---|---|---|
| `guides/*.md` | `GUIDE_CAP_BYTES`, 96 KB default | `GUIDE_CAP_LINES`, 1200 by default |
| `builds/*/README.md` | 25 KB (hardcoded) | none |
| `<MAP_ROOT>/features/*.md` | `DOSSIER_CAP_BYTES` | none |
| every other row document | `ROW_DOC_CAP_BYTES` | none |

`cl = 0` in the awk means the class has NO line bound, and the comparison is guarded
(`b>cb || (cl>0 && l>cl)`) so a zero can never read as "everything is over".

**Both byte bounds are DECLARED and neither can be switched off.** They pre-set to the kit default,
the conf is sourced OVER that, and then a helper re-normalises: blank resolves FORWARD to the default
rather than skipping the check, and a non-numeric or zero value refuses with `exit 2` naming the key.
That is deliberately the OPPOSITE of every measured pin in the same conf block, where blank means
skip — because a cap an adopter can disable by emptying a line is a gate that reports green for a tree
nobody is checking, and `project/curation-debt.txt` is already the deliberate per-file exemption
(`TOOL-aRelaxedShard-1`).

**That exemption is GRADED rather than granted.** A listed file stays IN checks 6, 7 and 8; the
findings are partitioned by leading path into the unwaived ones, which fail as before, and the waived
ones, which are RECORDED. A row that recorded nothing reds as stale, because a row hiding nothing has
stopped shrinking. The partition helper assigns to a global and returns nothing:
a command substitution or a pipe would run it in a subshell and drop every write, leaving a guard
that reds every row. The per-row report names which of the three each row EARNS, which is how an
over-wide waiver is made visible without failing a row whose remedy is an open owner call.
`TOOL-cGradedDebt-1`.

**Check 8 reports its graded ROW count.** `pop_guard` counts shard FILES, so without it a mostly
waived row population reports green and prints no number. The count
rides a sentinel line out of the same awk, summed across `xargs` invocations because each runs its
own `END`, and stripped before the findings are read.

**The dossier selector is guarded on a non-empty prefix.** `index(f, "")` is 1 for every string, so an
unguarded dossier branch resolves to a bare prefix in a tree with no codebase map and hands the
DOSSIER bound to the whole tree — silently undoing the row cap. Check 7's `ex7` adds its map
alternatives under the same emptiness guard for the same reason.

## Constraints & why

**Row documents carry no line bound** (`TOOL-aRelaxedShard-1`, which measured the population and
reverses `TOOL-aWidenedGuide-1`'s refusal). The byte figure decides every real row document; the
line figure bound first only where rows are short, so the codebase-map dossiers take their own
tighter byte bound and the relaxation lands on the backlog shards and the decision log.

**The byte axis is armed for row documents.** The row-class fixture carries three contracts
asserted THROUGH check 6 naming it — that `RUN.md` enters `index_set` at all, that check 7 exempts
it, and the per-class scoping control — so a fixture on the wrong axis silences all three while
every arm still passes.

**A verdict has an epoch.** The kit version dates what the engine decided, so a diff moving a
non-comment line of the engine must move `KIT_MEMORY_TREE_VERSION` too; `hygiene-parity.test.sh`
derives its baseline floor from that constant, so a stale one puts the floor before the change.

**`--offenders` runs the full check and prints only keys.** One `check <n><TAB><key>` per offender a
failing check lists, line locators stripped, headers and `… and` lines dropped, a repeat carrying
`#<k>`; every other line goes to /dev/null and the keys to fd 3, and the exit is the default mode's.
The merge bar's red attribution grades this leg with it as a SET. `TOOL-dDerivedDocket-23`.

## Shared seams

- `.memory-tree.conf` — the one declaration both this engine and the sibling Python modules read.
  The engine's own keys pre-set defaults and the conf is sourced OVER them, so a blank line
  OVERRIDES a default with blank; a non-skippable key needs the re-normalising step the two cap keys
  take, and inherits the same trap if it forgets.
- `MAP_SUB` — resolved once, near the top, from `.codebase-map.conf`'s `MAP_ROOT` and only when that
  root is a DIRECT child of the memory root. Both check 6's dossier class and check 7's `ex7`
  exemption key on it, and both guard it for emptiness, because an empty prefix matches every path.
- `--print-index-set` — the engine OWNS the index-set and read-path populations, and `corpus_ids.py`
  asks for them through this print mode rather than re-deriving them. A transcription of either would
  be the drift class the kit exists to remove.
- `KIT_MEMORY_TREE_VERSION` — read by `check-verdict-epoch.sh`, `check-kit-versions.sh` and
  `hygiene-parity.test.sh`, and mirrored as a `gov:kit memory-tree@<v>` marker in every shipped
  template.
- `BACKLOG_MODE` — the declared layout of an ask, and therefore the population of checks 4, 6, 7, 8,
  10, 13, 15, 20 and 24. The engine resolves it ONCE into `BMODE` (blank reads `shards`) and every
  check reads that; the Python modules read the same key through `backlog.read_conf`, lazily
  imported, so there is no second reader and an unrecognised value refuses on both sides. The
  engine's reading is observable through `--print-backlog-mode`, which exists because the
  project-key stderr line prints only a value that was SET — without it, "blank reads `shards`" is a
  claim nothing can check. `TOOL-dDerivedDocket-8`.
- `FORK_ITEM_CUTOFF` — one declaration, two readers of §8 (`TOOL-dDerivedDocket-31`). Past it the
  engine grades each F-item's span at a terminal status and reds a Tier-2 §8 of any other shape at
  any status; the unattended planning verb prints FORKED for the same bytes. The engine SOURCES the
  key, the planning side reads the line as TEXT through its own kit library and refuses a spelling it
  does not model rather than resolving blank, and the marker-contract harness compares the two
  readings at test time beside the shared case table, because the readers cannot share code.

## Reuse affordance

seam: the CAPTURE-BEFORE-SOURCE idiom — reuse for any conf key that must NOT be disableable by
blanking its line. `check-memory-hygiene.sh` stashes the shipped value in `_SPEC10_SHIPPED` before the
conf is sourced, and restores it afterwards with `: "${SPEC10_CUTOFF:=$_SPEC10_SHIPPED}"`. Anchored on
those two NAMES rather than on line numbers, which move under any edit above them.
seam: the `cl = 0` sentinel plus the guarded comparison — reuse for adding a size class that bounds
bytes only; extend by adding a branch to the awk after the class it must override, and nothing else:
the message split reads the same variable, so a new class gets the right output for free.
seam: `--print-index-set` — reuse for any sibling that needs this engine's population instead of
guessing it; extend by adding a print mode beside it rather than exporting the variable.
seam: the DELEGATE-STATUS idiom — reuse for any check that hands its parse to a sibling module: the
capture keeps `$?`, and a row the delegate prints on every run is the liveness test, so a delegate
that exited 0 having done nothing is refused too. Check 21's `_b21rc` and `n21` are the worked case.

## Check 26 — the transition-merge audit

`transition_audit.py` (`TOOL-dDerivedDocket-9`) is the one delegate whose population is the commit GRAPH rather than the
tracked tree, and the one that is DARK until a project sets `BACKLOG_MODE=builds`. It classifies a
merge as a TRANSITION by LINEAGE — some parent's lineage holds a shards-mode commit touching the
watched paths, and some other parent's holds a builds-mode commit — never by a parent's tip conf,
because a straggler that pulled the new conf early has a builds-mode tip and shards-mode content.

It pins the DEREFERENCE the way the
unattended kit's history leg does (`--no-replace-objects` plus an empty `GIT_GRAFT_FILE`), and both
halves are armed by fixtures that re-parent a merge and then expect the audit to see through it.
Its WATCHED PATHS are the backlog directory plus the FAMILY-named rotated archives alone: widening
the archive half to the whole directory makes every id anchored in a rotated decision log read as a
lost row, which the rotation arm stages. And it caches only the DELTA, under the git common dir,
keyed by merge sha and a module `CACHE_EPOCH` — never the verdict, which a later `RELOCATED` row
changes.

The memory-recall kit is a hard prerequisite under `builds` and is resolved EAGERLY, before any
merge is classified: resolved lazily, a warm delta cache answers every merge without keying a row,
so a tree with no recall kit reports a clean audit. The
kit descriptor carries a `requires_if` edge naming that prerequisite, which govkit's selfcheck
grades and which installs nothing.

The commit-time carrier is the tracked `commit-msg` hook, which is the one hook a clean `git merge`
and a conflicted merge concluded by `git commit` both reach — `pre-commit` never fires on the clean
one (`TOOL-dDerivedDocket-9`). It derives every path it uses and announces a skip rather than blocking
a commit when the kit or a python launcher is missing.

## The straggler layer — instructing a branch before its merge

Check 26 finds a lost row AFTER a pre-flip branch has merged. `.githooks/straggler-guard.sh` is the
layer that reaches that branch beforehand, sourced by `pre-commit`, `pre-rebase` and
`pre-push` through the CALLING HOOK's own directory rather than through the committing tree — a
pre-flip branch carries the old kit, so a rule resolved through `$top` could never reach it. It
reads git objects only and decides three predicates: FLIPPED (the default branch's committed conf
declares `builds`), PRE-FLIP (every merge base with the default is still in shards mode, never the
subject's own tip conf, for the reason check 26 above states), and HAS-DELTA (the lineage holds a
shards-mode commit touching the backlog shards or a family-named archive — the same watched
population check 26 reads, so the two layers are not two answers). It carries the relocation recipe
rendered at the tree's own derived prefix, and `straggler-guard.test.sh` grades that rendering
against the bytes `migrate_backlog.py --recipe` prints.

**WHICH HOOK FILES RUN is the limit of the whole layer.** The shared `core.hooksPath` applies unless
a worktree's config.worktree sets its own, and only an ABSOLUTE value makes a linked worktree run
another checkout's hooks. Under the relative `.githooks` that `check-wiring.sh` writes, a straggler
in a linked worktree runs its OWN pre-flip hook files and none of these refusals fire there. That
case is documented rather than closed: `check-wiring.sh`'s session step marks such a branch
`hooks own-tree`, the drift signal `backlog_stragglers` lists it from any node's run, and check 26
at the merge bar is what guarantees. These layers instruct; the bar decides.

**The routed-commits leg grades the COMMITS, not the tree** (`TOOL-aRoutedQuill-3`).
`routed_commits.py` holds every non-merge commit committed on or after `ROUTED_COMMIT_CUTOFF` that
touches `ROUTED_PATHS` to naming a unit, in its subject or a `Pass:` trailer, whose spec existed at
its first parent: the push-time half of the write gate, which sees Edit and Write calls and nothing
a shell or a hook-less run commits. It reads `GATE_PUSH_BASE` for its RANGE, grades the whole history
beside that range so a push sees the red remote CI would (`TOOL-aRoutedQuill-10`), widens to the
whole history otherwise, and it shares the transition audit's git pin through `tree_lib.build_git_env`.
The attended lander's mint names its unit through the leg's `--newest-unit` verb.

## Gaps

- **Any named unit with a spec at the parent passes the routed-commits leg.** Whether that unit's
  scope covers the change is not read, a merge's own content is not graded, and the conf it reads is
  a file the graded run commits — `TOOL-aRoutedQuill-3` §3.

- **The unfenced-body reader is a TOKENIZER, and a document can grep as complete while it sees
  something shorter.** It opens a fence on any line matching a leading-whitespace-tolerant
  triple-backtick or tilde and closes it only on a later line matching the same marker, so a
  triple-backtick span written INLINE in prose swallows every line to the end of the file. What
  check 12 then reports is the true consequence — a heading-canon diff, a rev not logged, a §10
  missing its evidence — and never the truncation, so the message points away from the cause.
  Class: `inline-fence-swallows-the-rest-of-the-file.md`.

- The `builds/*/README.md` class at 25 KB has no byte-axis arm — `TOOL-aRelaxedShard-2`. A
  class whose ONLY bound is bytes is currently unarmed.
- Checks 6 and 7 measure RAW working-tree bytes, so an adopter without the `eol=lf` pin gets a
  platform-dependent cap: a CRLF checkout adds one byte per line — `TOOL-aRootedPrefix-3`.
- Check 10 resolves a rotated index's live counterpart by BASENAME anywhere under the memory root,
  names a stem that resolves to zero or several rather than skipping it, admits a same-day
  disambiguator after the date, and reads the reference from the index PREAMBLE
  (`TOOL-cSpliceWarden-2`); a fixed path is blind to every `backlog/*.md` shard.
- Check 10 grades ANNOUNCEMENT, never CONTENTS. Nothing in this engine asserts that an archive holds
  what the declared `ROTATION_MODE` says it should: the key is validated against its closed set and
  then read by no check — `TOOL-cSpliceWarden-6`.
