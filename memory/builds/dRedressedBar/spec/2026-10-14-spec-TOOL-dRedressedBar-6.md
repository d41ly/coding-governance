# TOOL-dRedressedBar-6 — the roles adopter's two exit-1 refusals, armed in its own suite

**Status:** CLOSED · rev-2 · 2026-10-14 · node d · Tier-1 · base ebce889c · streams tooling · order 4

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-14-build-TOOL-dRedressedBar-1-research-bar-profile.md](../build/2026-10-14-build-TOOL-dRedressedBar-1-research-bar-profile.md) | research | TOOL-dRedressedBar-1 TOOL-dRedressedBar-2 TOOL-dRedressedBar-3 TOOL-dRedressedBar-4 TOOL-dRedressedBar-5 TOOL-dRedressedBar-7 TOOL-dRedressedBar-8 TOOL-dRedressedBar-9 |
| [2026-10-13-prompt-TOOL-dRedressedBar-1-brief.md](../prompts/2026-10-13-prompt-TOOL-dRedressedBar-1-brief.md) | research | TOOL-dRedressedBar-1 TOOL-dRedressedBar-2 TOOL-dRedressedBar-3 TOOL-dRedressedBar-4 TOOL-dRedressedBar-5 TOOL-dRedressedBar-7 |
| [2026-10-14-review-TOOL-dRedressedBar-1-9-spec-audit-round1.md](../reviews/2026-10-14-review-TOOL-dRedressedBar-1-9-spec-audit-round1.md) | spec-audit | TOOL-dRedressedBar-1 TOOL-dRedressedBar-2 TOOL-dRedressedBar-3 TOOL-dRedressedBar-4 TOOL-dRedressedBar-5 TOOL-dRedressedBar-7 TOOL-dRedressedBar-8 TOOL-dRedressedBar-9 |

<!-- /gen:spec-records -->

## 1. Goal

The `harness arms (fail branches armed or pinned)` leg reds at `ebce889c` on two refusal sites of
`tools/roles/adopt-roles.sh` that no line of `tools/roles/adopt-roles.test.sh` asserts by its own
failure text (the build brief, item 6). This unit arms both in that suite, so the leg reads the
roles adopter as fully armed and each arm is seen red on a staged break of the adopter.

## 2. Scope (IN)

- **S1** — Arm 4's remedy assertion matches the whole line
  `roles: remedy — bash $KREL/adopt-roles.sh --scaffold`, in a builtin form, so one non-comment line
  of the suite carries the line-209 signature `/adopt-roles.sh --scaffold` whole. Observed by AC1.
- **S2** — A new arm 13, the last block before the floor check, builds its own fixture, asserts it
  scaffolds and checks clean, unlinks the fixture's rendered `.claude/skills/build/SKILL.md`, appends
  `{{UNKNOWN_TOKEN}}` to the fixture's `house/gov-builder.md`, runs `--scaffold`, and in one
  assertion requires exit 1, the line-217 signature, the renderer's line naming the token, and the
  Skill still absent. Observed by AC2 and AC3.
- **S3** — `FLOOR_ASSERTIONS` rises by the two assertions arm 13 adds, its ledger comment names
  this unit, and the suite's header arm list names arm 13 and what it does not check. Observed by
  AC4.
- **S4** — Every line this unit adds or rewrites matches by a shell builtin, with no pipe into
  `grep`, `sed`, `tr` or `wc`. Observed by AC5.

## 3. Non-goals (OUT)

- No edit to `tools/roles/adopt-roles.sh`. Both refusals are correct; the gap is the suite.
- No row in `memory/project/unarmed-branches.txt`. A pin is for a site no fixture reaches, and both
  sites are reached by an ordinary fixture (section 4).
- No `ARMS_FLOORS` token for `tools/roles/adopt-roles.sh` in `.memory-tree.conf`. The leg reds on
  the unarmed sites, not on the absent floor (`tools/memory-tree/check-arms.py:963-965` skips a gate
  with no floor), and the conf is a shared record. A floor for this adopter is a follow-up.
- No arm for the adopter's exit-2 and exit-3 paths. Signature 2 reads `exit 1` and `status=1` only
  (`tools/memory-tree/check-arms.py:146-147`), so they are outside the leg's population.
- No change to `build_fixture`, `run_adopter`, or any arm but arm 4's remedy assertion.
- Nothing TOOL-dRedressedBar-1, TOOL-dRedressedBar-4 or TOOL-dRedressedBar-5 owns in this file: the
  probe stop or `WHOLE_RUN` row, the `workflows` homonym in arm 9, and the fork-idiom conversions.

### Edges

- **consumes-from** `TOOL-dRedressedBar-5` — the no-fork spellings of this suite's assertions, arm
  4's remedy line among them. This unit rewrites that line over unit 5's spelling and adds no
  fork idiom beside it; built before unit 5, it would edit a line unit 5 then converts again.
- **consumes-from** `TOOL-dRedressedBar-1` — the foreign-prefix parity fix for this suite. Without
  it, the parity leg stays red on this suite whatever arm 13 does.
- **consumes-from** `TOOL-dRedressedBar-4` — the arm 9 rewrite at the old line 228, in the same file.
- **hands-off** `TOOL-dRedressedBar-10` — §4's cites of `tools/roles/adopt-roles.test.sh` at
  `:100-107` and `:63` are `ebce889c` line numbers, which units 1 and 4 shift before this unit
  starts (report id 14). That unit adds the sentence stating so to §4, and classifies the arms this
  unit leaves in that file.

## 4. Design

### What the leg reads

`check-arms.py` puts every tracked non-test `*.sh` with an `exit 1` site into its population when
`ARMS_REFUSALS="graded"` (`.memory-tree.conf:639`). A site is armed when any non-comment line of its
sibling `<stem>.test.sh` that is not a negative assertion holds the site's signature as a substring
(`classify`, `tools/memory-tree/check-arms.py:810-821`; `armed_signatures`, `:270-292`). The
signature is the longest literal run of the message the site's `echo` prints, with each
interpolation, `$0` included, cut out (`extract_print_message`, `:395-416`; `signature`, `:204-221`).

The adopter has exactly two `exit 1` sites:

| line | message | signature |
|---|---|---|
| `tools/roles/adopt-roles.sh:209` | `roles: remedy — bash $KIT_REL/adopt-roles.sh --scaffold` | `/adopt-roles.sh --scaffold` |
| `tools/roles/adopt-roles.sh:217` | `roles: the agent render refused, so nothing more was written — fix what it named and re-run $0 --scaffold` | `roles: the agent render refused, so nothing more was written — fix what it named and re-run` |

At line 209 the literal after `$KIT_REL` is 26 characters against 20 before it, so the path half is
the signature. Each signature must sit whole on one line of the suite, because the scan reads line
by line.

### Line 209: arm 4 already reaches it

Arm 4 (`tools/roles/adopt-roles.test.sh:100-107`) appends one byte to a rendered agent type and runs
`--check`. `render_agents.py --check` exits 1 on the drift, the adopter sets `stale=1` and prints
the line-209 remedy (`tools/roles/adopt-roles.sh:205-209`). Its assertion greps
`adopt-roles.sh --scaffold$`, which stops one character short of the signature, so the scan reads it
as unarmed. S1 rewrites that assertion to a whole-line match of the remedy, in the builtin
anchored-literal form the forms table of
`memory/builds/aSweptBar/spec/2026-10-13-spec-TOOL-aSweptBar-5.md` records:

```bash
[[ $'\n'$out$'\n' == *$'\n'"roles: remedy — bash $KREL/adopt-roles.sh --scaffold"$'\n'* ]]
```

`$KREL` is the kit's repo-relative path, which equals the fixture's `$KIT_REL` because
`build_fixture` copies the kit to the same relative path (`tools/roles/adopt-roles.test.sh:67-75`).
That holds at all three prefixes the parity leg runs. The remedy line comes from `echo`, so it carries
no carriage return; one left by the renderer's Python output on the line above ends that line, not
this one. The brief asks for "an arm for each". This site gets an assertion rather than a fixture,
because arm 4 already stages the break that reaches it and a second fixture would copy arm 4.

### Line 217: arm 13

No arm runs `--scaffold` against a renderer that refuses. Arm 13 does, after arm 12 and before the
floor check:

1. `build_fixture`, then the liveness assertion every fixture arm carries:
   `arm 13 the fixture scaffolds and checks clean`.
2. Unlink `$FX/.claude/skills/build/SKILL.md`, so the claim "nothing more was written" can be seen.
3. Append `{{UNKNOWN_TOKEN}}` to `$FX/$KREL/house/gov-builder.md`. `roles_lib.render_role` raises
   R10 on a render token other than `{{MEMORY_ROOT}}` in an overlay
   (`tools/roles/roles_lib.py:576-580`). `render_agents.py` turns the error into exit 2 and prints
   it on stderr (`tools/roles/render_agents.py:226-238`). The adopter runs that render before it
   writes the Skill (`tools/roles/adopt-roles.sh:214-217`). The append reaches the render whatever the
   overlay held, so the break needs no knowledge of the file's bytes. It is arm 3's token idiom.
4. `out=$(run_adopter --scaffold); rc=$?`, then one assertion,
   `arm 13 a refused agent render stops the scaffold, naming the refusal, and writes no Skill`:
   `rc` is 1; `$out` holds the line-217 signature as one quoted literal; `$out` holds
   `{{UNKNOWN_TOKEN}}`, so the refusal is the staged one and not some other; and
   `.claude/skills/build/SKILL.md` is absent.

Every test in step 4 is `[ … ]` or `[[ $out == *'…'* ]]`, the forms the suite's arms 10 and 11
already use, so the shell hygiene leg counts no new site in a file unit 5 leaves with no row.

What arm 13 does not check: which rule refused. Any non-zero exit of the renderer takes the same
branch, so the arm proves the adopter's handling of a refusal and grades R10 only as the trigger.

### The floor and the header

`FLOOR_ASSERTIONS` is 38 at `ebce889c` (PINNED, `tools/roles/adopt-roles.test.sh:63`). It rises by
2 over whatever the file holds when the unit starts, and the ledger comment above it gains
`+2 for arm 13 (TOOL-dRedressedBar-6)`. Arm 4's rewrite adds no assertion. The header's arm list
(`:13-25`) gains arm 13, and its "does not check" paragraph gains the rule-blindness above.

### Files touched (estimate)

- `tools/roles/adopt-roles.test.sh`

### Alternatives rejected

- A second fixture arm for line 209. It would duplicate arm 4's staged break to reach the same exit.
- Pinning either site in `memory/project/unarmed-branches.txt`. Both are reachable, and the brief's
  non-goal refuses a registry row a code change can fix.
- An `# arm-signature:` marker above either site. A marker belongs to a DELEGATED site, and the scan
  refuses one above a REASONED site (`tools/memory-tree/check-arms.py:539-544`). Both sites here are
  REASONED.
- A staged break in `house/policy.toml`, an unknown effort level. It needs a `sed` over a line whose
  presence depends on the policy's contents. The overlay append works whatever the file holds.
- Arming line 209 by spelling only `/adopt-roles.sh --scaffold` in the assertion. It arms the leg,
  but it would pass on a remedy that lost `bash` or the `roles: remedy — ` head. The whole line
  holds the remedy the operator copies.

## 5. Acceptance criteria

- **AC1** — When `grep -nF 'adopt-roles.sh --scaffold' tools/roles/adopt-roles.test.sh` runs, the
  only hit inside the `# ---- arm 4:` block is a non-comment assertion line holding
  `"roles: remedy — bash $KREL/adopt-roles.sh --scaffold"` as one literal. Red when: the assertion
  still stops at `adopt-roles.sh --scaffold$`, without the leading `/`, and the leg reads line 209
  unarmed.
- **AC2** — When
  `grep -nF 'roles: the agent render refused, so nothing more was written — fix what it named and re-run' tools/roles/adopt-roles.test.sh`
  runs, it hits one non-comment line inside the `# ---- arm 13:` block. Red when: the text is
  shortened, split across two lines, or written only in a comment, and the leg reads line 217
  unarmed.
- **AC3** — When `bash tools/roles/adopt-roles.sh --scaffold` runs in a fixture built as
  `build_fixture` builds it, with `.claude/skills/build/SKILL.md` unlinked and `{{UNKNOWN_TOKEN}}`
  appended to `tools/roles/house/gov-builder.md`, it exits 1. It prints the line-217 message and a
  `render_agents:` line naming `{{UNKNOWN_TOKEN}}`, and the Skill is still absent. Red when: the
  appended file is one the agent render does not read, the scaffold exits 0, and arm 13 grades a
  fixture that never refuses.
  fixture: none in the tree. It is a fresh `git init` repository under `%TEMP%/<short-name>`, never
  inside the worktree, and was not observed at spec time: the worktree-isolation hook refused the
  `git init` outside this worktree. The result is derived from `tools/roles/adopt-roles.sh:214-217`,
  `tools/roles/render_agents.py:226-238` and `tools/roles/roles_lib.py:576-580`.
- **AC4** — When `grep -n -B3 '^FLOOR_ASSERTIONS=' tools/roles/adopt-roles.test.sh` runs, the value
  is 2 above the one the file held when the unit started, and the comment above it reads
  `+2 for arm 13 (TOOL-dRedressedBar-6)`. Red when: the floor is unmoved, so the suite stays green
  after arm 13 is cut.
  figure: 38 at `ebce889c`, PINNED; the start value is read from the tree the builder starts on.
- **AC5** — When `git diff -U0 <pass>~1 <pass> -- tools/roles/adopt-roles.test.sh` is read at this
  unit's pass commit, no `+` line pipes into `grep`, `sed`, `tr` or `wc`, and none spawns
  `$(printf`. Red when: an assertion is spelled `printf '%s' "$out" | grep`, a `var-pipe` site the
  `shell hygiene (a fork spent on builtin work)` leg counts against a file with no row.

## 6. Gates

`harness arms (fail branches armed or pinned)` · `roles adopter self-test` · `foreign-prefix parity (every self-test at three prefixes)` · `shell hygiene (a fork spent on builtin work)` · `shell hygiene (a loop fed by a command substitution)` · `install-prefix (shipped surface)`

The main loop runs these at the close. The first is the leg this unit turns green; its red was
observed by the full bar over `ebce889c`. The touched path trips only the broad `tools/` guard, so
the guard join owes no leg.

New arm: tools/roles/adopt-roles.test.sh · covers AC1 · grade a copy through `ROLES_ADOPTER` whose line-209 remedy reads `roles: remedy — bash adopt-roles.sh --scaffold` and arm 4 reds · none
New arm: tools/roles/adopt-roles.test.sh · covers AC2 AC3 · grade a copy through `ROLES_ADOPTER` whose agent render drops its `|| { …; exit 1; }` refusal, and arm 13 reds on exit 0 and a written Skill · `FLOOR_ASSERTIONS` +2

## 7. Open questions

none

## 8. Revision log

- rev-1 · 2026-10-14 · initial draft, from item 6 of the build brief.
- rev-2 · 2026-10-14 · §3 · Edges gain the hands-off to TOOL-dRedressedBar-10, the batch the round-1
  spec audit's minors were promoted into, for report id 14. No scope, design or criterion moves.

## 9. Reuse audit

The seam is the suite's own fixture shape: `build_fixture` and `run_adopter`
(`tools/roles/adopt-roles.test.sh:67-76`), arm 4's existing staged break for line 209, and arm 3's
`{{UNKNOWN_TOKEN}}` idiom for the break arm 13 stages. `ROLES_ADOPTER` (`:5`, `:37`) is the suite's
own seam for grading a broken copy, and both `New arm:` observations use it.
`tools/codebase-map/reuse_lookup.py "assert an adopter refusal by exit code and its failure text in a fixture repository"`
ranked `build_fixture` as a seam, with `tools/roles/adopt-roles.test.sh` among its holders, and
nothing nearer. Recall named TOOL-aGraftedHelix-47, which put adopter exits into the leg's
population, and TOOL-aDeferredBar-8, which asked for it. The gotcha
`memory/gotchas/fixture-passes-by-finding-nothing.md` is why arm 13 asserts the staged token by
name and runs a liveness assertion first.

Recall terms used: `python tools/memory-recall/query.py "how is an unarmed adopter exit armed in its sibling self-test" --terms "check-arms refusal signature exit site armed positive assertion adopter sibling test.sh unarmed-branches staged break"`
