# TOOL-dDerivedDocket-53 — acceptance ledger

**Serves:** journal TOOL-dDerivedDocket-53

A pinned read pins its conf too: one sibling reader, `read_conf_at_rev`, that takes a rev and returns
the declarations the `.memory-tree.conf` blob at that rev yields, through `parse_conf` and through no
second grammar; three named refusals in place of any fall back to the working tree; a source notice
on stderr; and ten arms in the build-index selftest over two fixture repositories.

The direct check for every line below is the FLAG form
`python tools/memory-tree/gen_build_index.py --selftest`, which is the check this pass may make. The
identical argv's run as a HELD `chunk = selftests` LEG is deferred to the bar the orchestrator runs at
VERIFYING, and so is the codebase-map coverage leg AC6's `permission:` line names. No merge bar, no
gate leg and no `*.test.sh` suite ran in this pass.

Every one of the ten new arms has an observed RED, staged and unstaged by a scratch script that
restores the module in a `finally` block. Six breaks: the working-tree read standing in for the
pinned one (five arms red), the zero-declaration refusal removed outright (two red), the zero test
applied to the dict `parse_conf` RETURNED instead of to the blob's own declarations (two red), the
source notice moved to stdout (one red), the second refusal given the first's wording (two red), and
the blob read taken back to `run()`'s text mode (one red).

The pass landed in two commits and the second is a repair the diff's own bug-class checklist
produced. `naming-leg-grades-what-python-named` names nested helpers as graded definitions, and the
three this unit first wrote — `_conf_commit`, `_pinned`, `_conf_refusal` — each led with a word the
declared table does not carry, confirmed one by one with
`python tools/lexicon/lexicon.py --suggest <name> --as py.function`; they are now
`_build_conf_commit`, `_read_pinned_conf` and `_read_conf_refusal`, each answered OK by the same
command. The second finding was the pass's own: the blob was first read through `run()`, whose text
mode UNIVERSAL-NEWLINES the result and decodes it with the locale encoding, so this reader and
`read_text` disagreed on a lone CR and on a non-ASCII value — one reader of a config file re-derived,
which is the split the one-parser rule exists to close. It now reads bytes and applies `read_text`'s
own transform, and a tenth arm holds the two readers equal over a conf built to split them.

**Evidences:** TOOL-dDerivedDocket-53
- AC1 — `python tools/memory-tree/gen_build_index.py --selftest` — the new fixture repository carries
  four commits; two of them declare `MEMORY_ROOT` and `ASK_CUTOFF` differently, and the working tree
  holds the newer pair. The arm asserts both halves in ONE value,
  `pinned=memory-old working=memory-new`, so the contrast is the assertion rather than a second arm's
  business; a companion arm pins the second key at the same rev. Observed RED under the
  working-tree-stands-in break, where the same value reads `pinned=memory-new working=memory-new`.
- AC2 — `.memory-tree.conf` — three refusal arms plus a distinctness arm, all over that same
  fixture. A rev that resolves to nothing draws "resolves to no commit"; the root commit, which
  carries no blob, draws "carries no .memory-tree.conf blob"; an all-comment, all-blank blob draws
  "yields zero declarations". Each names the rev and the path and returns no conf. The distinctness
  arm reads `distinct=3 refused=3` and compares the texts with the REV ITSELF neutralised, because
  every refusal embeds its own rev and comparing the raw strings would call three copies of one
  sentence distinct — a vacuous test, and the reason the arm carries the refusal COUNT in the same
  value. Observed RED three ways: with the zero-declaration refusal deleted, with the zero test
  applied to the returned dict rather than to the blob (both leave the all-comment arm reporting
  `{'MEMORY_ROOT': 'memory', 'DISCIPLINES': '', 'FAMILIES': ''}`, which is the seeded-defaults shape
  §4 predicted and `parse_conf` cannot raise on), and with the second refusal given the first's
  wording, which drops the distinctness arm to `distinct=2`.
- AC3 — `tools/memory-tree/gen_build_index.py` — the arm captures stdout and stderr separately around
  one pinned read and asserts `notice=True names-rev=True stdout=''`: the notice reaches stderr, it
  carries the rev, and the mode's own output stream stays empty. Observed RED under the
  notice-on-stdout break, which reports `notice=False names-rev=False` with the line sitting in
  `stdout`.
- AC4 — `git grep -c "def load_conf(root: str) -> dict:"` — returns 1 at the parent `4fce85ec` and 1
  over the staged tree that became this commit; `load_conf` keeps its name, signature, body and
  callers, and the pinned reader is a sibling with its own seed literal. The full suite reaches
  `PASS — gen_build_index: all arms held`, so the existing working-tree arms pass unchanged, and a
  further arm asserts `load_conf` still answers `memory-new` from the fixture's checkout. The two
  seed literals are held equal by an arm rather than by a shared constant, reading
  `extra=['ASK_CUTOFF'] missing=[] undeclared-agree=True` against `load_conf` over a root with no
  conf file.
- AC5 — `git grep -c "parse_conf"` — 3 at the parent `4fce85ec` and 6 at both of this unit's
  commits, so it returns MORE than the parent. The diff adds no `re.compile` and no conf-line pattern
  of any kind: the pinned reader hands the blob's text to `parse_conf` and reads not one line of it
  itself, and the only new judgement it makes is `len()` over that parser's own output. A tenth arm
  holds the property the count alone cannot see — that the one parser is also handed the same BYTES
  by both readers. Over a conf carrying CRLF endings, a lone CR and a utf-8 value outside ASCII, the
  pinned read and `load_conf` return equal dicts; observed RED with the blob read taken back to
  `run()`'s text mode, where the lone CR becomes a line break and a key `B` nobody declared appears.
- AC6 — `memory/map/generated/symbols.json` — `python tools/codebase-map/gen_map.py --write`
  re-derived all three artifacts; only `symbols.json` moved, it carries the `read_conf_at_rev` row,
  and it is staged in the same commit as the module. What AC6's `permission:` line defers is the
  codebase-map coverage LEG over the real tree, which belongs to the build's one post-build bar and
  was not run here.
