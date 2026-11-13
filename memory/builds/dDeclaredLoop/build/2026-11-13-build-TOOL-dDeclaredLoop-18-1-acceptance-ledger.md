# TOOL-dDeclaredLoop-18 — acceptance ledger

**Serves:** journal TOOL-dDeclaredLoop-18

No merge bar, no self-test suite and no gate leg ran in this pass. The criteria were observed through
the unit's own fixture, `gov_tag.py --fixture --plant <case>` with the two `--set` flags every tag plant
takes, through the lexicon's `--tags` and `--suggest` verbs, through the greps the spec spells, and
through two `python -c` probes that call the changed checks over the live tree's index. The pass base is
`75a5904c`. Owed to the close: AC8's own command, which is the `tags` leg's, and the RED-first
observation of the new arm in `tools/playbook/adopt-playbook.sh`, seven rows, five in the tag
resolver's block and two in the block guarded on the policy kit.

**Evidences:** TOOL-dDeclaredLoop-18
- AC1 — `policy-ns-word` — the plant exited 1 and printed `tags: tools/policy/catalogue.toml@9ce5a224:2 · shape ·
  policy.step.timeout · first segment 'step' is a namespace word`; the name-check printed the same
  reason for the same tag.
- AC2 — `policy-catalogue` — the plant exited 0 and printed `tags: plant policy-catalogue · 264 members
  of 264 literal names, 6 families of 6 prefixes`, over the installed catalogue's bytes, with `check`
  green.
- AC3 — `loop-rows` — the plant exited 0 and printed `tags: plant loop-rows · where: rc=0 0, check:
  rc=0`, the two `where` lines naming lines 2 and 5 of the loop definition. Under `loop-bad-seg` it
  exited 1 and printed `· shape · step.Plan · segment 'Plan' is outside [a-z0-9][a-z0-9-]*`.
- AC4 — `command-rows` — the plant exited 1 and printed the join line holding `` `command.corekit.old`
  is cited and undeclared in command ``; no line held `` `command.corekit.new` ``.
- AC5 — `namespaces.toml` — the three count greps printed 4, 0 and 4; the four zero-greps and the
  `Ten$` and `item` greps each printed 0; the `fourteen` grep printed 1, and `two or more segments`
  printed 1 for each of the three files.
- AC6 — `policy-family` — the plant exited 1, printed the join line holding `` `policy.review.build.nope`
  is cited and undeclared in policy `` and `tags: join policy · families · 1 families, 2 cited under
  one, 1 declared by the catalogue`, and no line held `` `policy.review.build` ``.
- AC7 — `lexicon.py --tags` — `policy.item.x` alone exited 1 with `lexicon: tag policy.item.x · first
  segment 'item' is a namespace word`. The four-tag input exited 1 with that one `lexicon: tag` line
  and `lexicon: tags · 4 graded, 1 refused`. `--suggest policy --as tag.kit` printed `OK — kit.policy
  satisfies kebab in every segment and breaks no first-segment rule`.
- AC8 — `gov_tag.py check` — NOT RUN: it is the `tags` leg's own command and the close's to observe.
  Observed in its place: the `git grep` for the two dossier spans printed nothing; `git diff --stat`
  over `tools/policy`, `help/reference/kinds.md` and `tools/playbook/core-pending.txt` printed
  nothing; and a probe calling `derive_family_tags`, `check_namespace_joins`, `check_resolves`,
  `check_namespace_purpose` and `check_owned` over the live index returned 0 join reds, 0 resolve
  reds, no purpose red and no owned red, `step` and `item` pending on their `purpose-source`,
  `policy` armed at 264 members, and `step`, `item` and `command` unarmed.
- AC9 — `ns-word-leaf` — the plant exited 0, printed `tags: green · 0 red`, and no line held
  `namespace word`. The `ns-word` plant still exited 1 with `· shape · practice.repo.x · first segment
  'repo' is a namespace word`.
- AC10 — `probe:` — the spec's command printed one blank line and `probe: 575 graded, 0 shape, 0
  name-check · slot point.instruction.name-check · searched-empty`. At the pass base it printed 305
  graded; the 270 added are the 264 members and the 6 families.
