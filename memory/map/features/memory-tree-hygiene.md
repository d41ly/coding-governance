# memory-tree hygiene engine — the numbered gate over the memory tree

```toml
feature = "memory-tree-hygiene"
title = "check-memory-hygiene.sh: the memory tree's structural gate, its per-class size caps, and the epoch that dates its verdicts"
status = "shipped"
streams = ["tooling"]
decisions = ["TOOL-aRelaxedShard-1", "TOOL-aWidenedGuide-1"]

[claims]
gate-legs = ["memory hygiene", "memory-hygiene self-test", "verdict epoch (kit version dates the engine)", "verdict-epoch self-test", "kit version markers", "kit/dogfood doc parity", "transition-audit arms", "backlog migration selftest", "straggler-guard arms"]
kits = ["memory-tree"]
git-hooks = ["commit-msg", "pre-rebase", "straggler-guard.sh"]
workflow-scripts = []
skill-engines = []
rendered-skills = []
gotcha-classes = ["suite-edited-while-bash-executes-it.md", "ledger-token-wrapped-across-a-line-joins-nothing.md", "inline-fence-swallows-the-rest-of-the-file.md",
  "record-citing-a-foreign-id-defines-or-orphans-it.md", "swallowed-delegate-reads-as-clean.md",
  "waiver-row-that-hides-nothing-reds.md", "pin-gated-checks-arm-nothing-without-a-pin.md",
  "record-without-serves-or-with-a-round-counter.md", "sourced-conf-blank-overrides-the-default.md"]
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
  ".githooks/commit-msg",
  ".githooks/pre-rebase",
  ".githooks/straggler-guard.sh",
  ".githooks/straggler-guard.test.sh",
]
```

## What it is

One shell engine over the tracked contents of `<MEMORY_ROOT>/`, plus the epoch rule that makes its
verdicts datable. How many numbered checks it carries is derivable from the engine and is not
written here, for the same reason the H1 stopped saying it. Several of them delegate to sibling
Python modules (`gen_build_index.py`, `corpus_ids.py`, `gotchas.py`, `row_grammar.py`, `transition_audit.py`);
this dossier owns the engine, its self-test, the epoch and the transition audit, not the other modules.

**One leg here belongs to a module this dossier does NOT own**, and that is deliberate rather than
an oversight to tidy away. `backlog migration selftest` runs `migrate_backlog.py --selftest`, the
suite of the shards-to-builds migration PLANNER and of the relocation ENGINE that lives beside it in
the same module. The leg is CLAIMED here because that module has no dossier of its own and an
unclaimed key reds the map's coverage gate; it is DECLARED in `tools/memory-tree/kit.toml` beside
its four module-selftest siblings rather than exempted in the govkit registry, because the module
ships to every memory-tree adopter and each of them runs `--plan` in their own deployer build
(`TOOL-dDerivedDocket-11` fork F8). It is held like those siblings, by `subject = kit`, so no plain
bar executes it. Its ceiling is pinned at or under the direct-check bound the unattended kit's
gate-guard suite grades every `--selftest` leg against, which is what keeps the flag form a check a
unit pass may run by hand.

**The engine's relationship to the transition audit this dossier DOES own is one direction only**
(`TOOL-dDerivedDocket-12`). `migrate_backlog.py --relocate`, `--repair` and `--ingest` move a
pre-flip branch's row changes into the per-build files and write the `RELOCATED` rows check 25
reads; `--stragglers` lists the refs that still owe one and `--recipe` prints the one relocation
recipe every carrier quotes. All three writing verbs CALL `transition_audit.delta` and
`transition_audit.accounted` and spell no second transition rule, so the audit and the repair that
answers it cannot disagree about what a row change is. That module's CLI resolves its repository
from its own file location, which is why the engine's fixture arms call it in process against an
explicit root — a subprocess launched inside a fixture audits THIS tree instead and returns a clean
verdict about the wrong one.

The self-test's project-key arms run the engine over
the suite's own scratch tree, one invocation per arm, never over an archive of this repository
(`TOOL-aRatifiedRulings-3`), so a red in the live corpus cannot red an arm that grades a conf key.
Three arms in that block grade the SHIPPED `.memory-tree.conf.example` instead, and they are
parity rather than behaviour: every key the engine validates, every bare `*_CUTOFF` it presets, and
— since `TOOL-dDerivedDocket-50` — every key the kit's PYTHON modules read out of a dict must be
declared there, or named on that arm's own exemption list, which is asserted in both directions so a
name nothing reads any more reds too. The python arm's receiver is deliberately UNCONSTRAINED: a
module reaching for a SECOND kit's conf cannot bind it to `conf`, that name being taken by its own,
so a `conf`-anchored derivation is blind to exactly the cross-kit read the arm exists to catch. Its
population is derived from the module text and REFUSES when it finds no key at all, and a fixture
directory holding two deliberately undeclared keys is what proves both halves fire.

The engine is COPY-INSTALLED as a standalone directory, so it carries the python resolver inline and
derives its own prefix. It never reads its identity from a project conf: `KIT_MEMORY_TREE_VERSION` is
set in the file, because a project conf must not be able to spoof which engine graded a tree.

## The size caps — four classes, one line bound

Check 6 is the part that moves most, so it is the part worth writing down.

| class | byte bound | line bound |
|---|---|---|
| `guides/*.md` | 60 KB (hardcoded) | 750 |
| `builds/*/README.md` | 25 KB (hardcoded) | none |
| `<MAP_ROOT>/features/*.md` | `DOSSIER_CAP_BYTES` | none |
| every other row document | `ROW_DOC_CAP_BYTES` | none |

`cl = 0` in the awk means the class has NO line bound, and the comparison is guarded
(`b>cb || (cl>0 && l>cl)`) so a zero can never read as "everything is over". The message splits on the
same variable, printing one bound or two.

**Both byte bounds are DECLARED and neither can be switched off.** They pre-set to the kit default,
the conf is sourced OVER that, and then a helper re-normalises: blank resolves FORWARD to the default
rather than skipping the check, and a non-numeric or zero value refuses with `exit 2` naming the key.
That is deliberately the OPPOSITE of every measured pin in the same conf block, where blank means
skip — because a cap an adopter can disable by emptying a line is a gate that reports green for a tree
nobody is checking, and `project/curation-debt.txt` is already the deliberate per-file exemption.

**That exemption is now GRADED rather than granted.** A listed file stays IN checks 6, 7 and 8; the
findings are partitioned by leading path into the unwaived ones, which fail as before, and the waived
ones, which are RECORDED. A row that recorded nothing reds as stale, because a row hiding nothing has
stopped shrinking — the `TOOL.md` row was listed for a byte cap raised past it the same day and
outlived its own fault by three weeks. The partition helper assigns to a global and returns nothing:
a command substitution or a pipe would run it in a subshell and drop every write, leaving a guard
that reds every row. The per-row report names which of the three each row EARNS, which is how an
over-wide waiver is made visible without failing a row whose remedy is an open owner call.
`TOOL-cGradedDebt-1`.

**Check 8 reports its graded ROW count.** `pop_guard` counts shard FILES, so a waiver covering 438
of 499 rows reported green over an 88% waived population and printed no number at all. The count
rides a sentinel line out of the same awk, summed across `xargs` invocations because each runs its
own `END`, and stripped before the findings are read.

**The dossier selector is guarded on a non-empty prefix.** `index(f, "")` is 1 for every string, so an
unguarded dossier branch resolves to a bare prefix in a tree with no codebase map and hands the
DOSSIER bound to the whole tree — silently undoing the row cap. Check 7's `ex7` adds its map
alternatives under the same emptiness guard for the same reason.

## Constraints & why

**The row line bound is retired, and that was a decision rather than a tidy-up.** At check 7's
300-char entry budget a 250-line row document may hold 75,000 B, so the byte figure decided every real
case and the line figure needed rows averaging under 82 B — measured on this corpus's backlog rows at
253.7. But it DID bind: over check 6's 29-member row class, 22 sat below the 81.92 B/line break-even
and were line-bound first, every codebase-map dossier among them. `TOOL-aWidenedGuide-1` had refused
to triple the row allowance for exactly that reason. `TOOL-aRelaxedShard-1` reverses that refusal
after the owner was shown the population, and buys the dossier sub-population its own tighter bound so
the relaxation lands on the backlog shards and the decision log that asked for it.

**The byte axis had never been armed.** Every check-6 fixture in the suite was a line-axis
construction, so the bound that actually fires in production had no test behind it. Retiring the row
line bound made fixing that mandatory rather than merely worthwhile, because the one row-class fixture
carried three contracts asserted THROUGH check 6 naming it — that `RUN.md` enters `index_set` at all,
that check 7 exempts it, and the per-class scoping control — and all three would have gone quiet
together while every arm still passed.

**A verdict has an epoch.** The kit version dates what the engine decided, so a diff moving a
non-comment line of the engine must move `KIT_MEMORY_TREE_VERSION` too; `hygiene-parity.test.sh`
derives its baseline floor from that constant, and a stale one put the floor before the change.

## Shared seams

- `.memory-tree.conf` — the one declaration both this engine and the sibling Python modules read.
  The engine's own keys pre-set defaults and the conf is sourced OVER them, which means a blank line
  OVERRIDES a default with blank. Every measured pin uses that as "skip this check"; the two cap keys
  must not be skippable, so they are re-normalised after the source instead. Anything adding a
  non-skippable key to this file needs the same step, and inherits the same trap if it forgets.
- `MAP_SUB` — resolved once, near the top, from `.codebase-map.conf`'s `MAP_ROOT` and only when that
  root is a DIRECT child of the memory root. Both check 6's dossier class and check 7's `ex7`
  exemption key on it, and both guard it for emptiness, because an empty prefix matches every path.
- `--print-index-set` — the engine OWNS the index-set and read-path populations, and `corpus_ids.py`
  asks for them through this print mode rather than re-deriving them. A transcription of either would
  be the drift class the kit exists to remove.
- `KIT_MEMORY_TREE_VERSION` — read by `check-verdict-epoch.sh`, `check-kit-versions.sh` and
  `hygiene-parity.test.sh`, and mirrored as a `gov:kit memory-tree@<v>` marker in every shipped
  template. One constant, four consumers.
- `BACKLOG_MODE` — the declared layout of an ask, and therefore the population of checks 4, 6, 7, 8,
  10, 13, 15, 20 and 24. The engine resolves it ONCE into `BMODE` (blank reads `shards`) and every
  check reads that; the Python modules read the same key through `backlog.read_conf`, lazily
  imported, so there is no second reader and an unrecognised value refuses on both sides. The
  engine's reading is observable through `--print-backlog-mode`, which exists because the
  project-key stderr line prints only a value that was SET — without it, "blank reads `shards`" is a
  claim nothing can check. `TOOL-dDerivedDocket-8`.

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

## Check 25 — the transition-merge audit

`transition_audit.py` is the one delegate whose population is the commit GRAPH rather than the
tracked tree, and the one that is DARK until a project sets `BACKLOG_MODE=builds`. It classifies a
merge as a TRANSITION by LINEAGE — some parent's lineage holds a shards-mode commit touching the
watched paths, and some other parent's holds a builds-mode commit — never by a parent's tip conf,
because a straggler that pulled the new conf early has a builds-mode tip and shards-mode content.

Three properties are worth knowing before touching it. It pins the DEREFERENCE the way the
unattended kit's history leg does (`--no-replace-objects` plus an empty `GIT_GRAFT_FILE`), and both
halves are armed by fixtures that re-parent a merge and then expect the audit to see through it.
Its WATCHED PATHS are the backlog directory plus the FAMILY-named rotated archives alone: widening
the archive half to the whole directory makes every id anchored in a rotated decision log read as a
lost row, which the rotation arm stages. And it caches only the DELTA, under the git common dir,
keyed by merge sha and a module `CACHE_EPOCH` — never the verdict, which a later `RELOCATED` row
changes.

The memory-recall kit is a hard prerequisite under `builds` and is resolved EAGERLY, before any
merge is classified. Resolving it lazily was measured as a defect: a warm delta cache answers every
merge without keying a row, so a tree whose recall kit had been deleted reported a clean audit. The
kit descriptor carries a `requires_if` edge naming that prerequisite, which govkit's selfcheck
grades and which installs nothing.

The commit-time carrier is the tracked `commit-msg` hook, which is the one hook a clean `git merge`
and a conflicted merge concluded by `git commit` both reach — `pre-commit` never fires on the clean
one, measured with git 2.54. It derives every path it uses and announces a skip rather than blocking
a commit when the kit or a python launcher is missing.

## The straggler layer — instructing a branch before its merge

Check 25 finds a lost row AFTER a pre-flip branch has merged. `.githooks/straggler-guard.sh` is the
layer that reaches that branch beforehand, sourced by `pre-commit`, the new `pre-rebase` and
`pre-push` through the CALLING HOOK's own directory rather than through the committing tree — a
pre-flip branch carries the old kit, so a rule resolved through `$top` could never reach it. It
reads git objects only and decides three predicates: FLIPPED (the default branch's committed conf
declares `builds`), PRE-FLIP (every merge base with the default is still in shards mode, never the
subject's own tip conf, for the reason check 25 above states), and HAS-DELTA (the lineage holds a
shards-mode commit touching the backlog shards or a family-named archive — the same watched
population check 25 reads, so the two layers are not two answers). It carries the relocation recipe
rendered at the tree's own derived prefix, and `straggler-guard.test.sh` grades that rendering
against the bytes `migrate_backlog.py --recipe` prints.

**WHICH HOOK FILES RUN is the limit of the whole layer.** The shared `core.hooksPath` applies unless
a worktree's config.worktree sets its own, and only an ABSOLUTE value makes a linked worktree run
another checkout's hooks. Under the relative `.githooks` that `check-wiring.sh` writes, a straggler
in a linked worktree runs its OWN pre-flip hook files and none of these refusals fire there. That
case is documented rather than closed: `check-wiring.sh`'s session step marks such a branch
`hooks own-tree`, the drift signal `backlog_stragglers` lists it from any node's run, and check 25
at the merge bar is what guarantees. These layers instruct; the bar decides.

## Gaps

- **The unfenced-body reader is a TOKENIZER, and a document can grep as complete while it sees
  something shorter.** It opens a fence on any line matching a leading-whitespace-tolerant
  triple-backtick or tilde and closes it only on a later line matching the same marker, so a
  triple-backtick span written INLINE in prose swallows every line to the end of the file. What
  check 12 then reports is the true consequence — a heading-canon diff, a rev not logged, a §10
  missing its evidence — and never the truncation, so the message points away from the cause.
  Class: `inline-fence-swallows-the-rest-of-the-file.md`.

- The `builds/*/README.md` class at 25 KB has no byte-axis arm either — `TOOL-aRelaxedShard-2`. A
  class whose ONLY bound is bytes is currently unarmed.
- Checks 6 and 7 measure RAW working-tree bytes, so an adopter without the `eol=lf` pin gets a
  platform-dependent cap: a CRLF checkout adds one byte per line — `TOOL-aRootedPrefix-3`.
- CLOSED by `TOOL-cSpliceWarden-2`: check 10 resolved a rotated index's live counterpart by fixed
  path, so it was blind to every `backlog/*.md` shard — it graded 1 of 4 archives here and skipped 3
  in silence. It now resolves by BASENAME anywhere under the memory root, names a stem that resolves
  to zero or several rather than skipping it, admits a same-day disambiguator after the date, and
  reads the reference from the index PREAMBLE instead of a fixed `head -3`. The last two were unfiled
  and the fourth was found only by running the candidate over the real tree, where fixing the path
  alone reds three files and two of those reds are false.
- Check 10 grades ANNOUNCEMENT, never CONTENTS. Nothing in this engine asserts that an archive holds
  what the declared `ROTATION_MODE` says it should: the key is validated against its closed set and
  then read by no check — `TOOL-cSpliceWarden-6`.
