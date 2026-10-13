# PLAY-aOrientedCast-2 — the charter's `[roles]` rule and its generated Agent roles section

**Status:** INPROGRESS · rev-2 · 2026-10-13 · node a · Tier-2 · base 646d4a73 · streams playbook · order 20

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-13-prompt-TOOL-aOrientedCast-16-1-spec-brief.md](../prompts/2026-10-13-prompt-TOOL-aOrientedCast-16-1-spec-brief.md) | journal | TOOL-aOrientedCast-16 TOOL-aOrientedCast-17 TOOL-aOrientedCast-18 TOOL-aOrientedCast-19 |
| [2026-10-13-prompt-TOOL-aOrientedCast-16-2-build-brief.md](../prompts/2026-10-13-prompt-TOOL-aOrientedCast-16-2-build-brief.md) | journal | TOOL-aOrientedCast-16 TOOL-aOrientedCast-17 TOOL-aOrientedCast-18 TOOL-aOrientedCast-19 |
| [2026-10-13-prompt-TOOL-aOrientedCast-20-1-spec-brief.md](../prompts/2026-10-13-prompt-TOOL-aOrientedCast-20-1-spec-brief.md) | journal | TOOL-aOrientedCast-19 TOOL-aOrientedCast-20 TOOL-aOrientedCast-21 PLAY-aOrientedCast-3 |

<!-- /gen:spec-records -->

## 1. Goal

The owner ruled on 2026-10-13 that role agents are non-negotiable wherever gov is adopted, short of a
tool or run that cannot spawn one, and that the charter must say so and list the roles in a generated
section. This unit writes that into the charter template: a section 1 `[roles]` rule naming the
exception and its waiver registry, and a `## Agent roles` section holding the derived roster. The
Tools line that said a weaker version of the rule shrinks to its `/build` clause. Gov's charter is
re-rendered, and the size records, the kickoff manifest stamp and the help page follow. The
template's version move is `PLAY-aOrientedCast-3`'s, the last unit of the set to touch it.

## 2. Scope (IN)

- **S1** — `coding-governance-agents.template.md` gains, on the line after the `[tools]` rule
  (`coding-governance-agents.template.md:46`), a `kit:roles` fence holding the `[roles]` rule in
  §4 "The new text", block A. It sits inside section 1's first one-line region. Observed by AC1,
  AC2 and AC3.
- **S2** — Between the Tools region's closing marker (`coding-governance-agents.template.md:150`) and
  `## Protocols — read the one whose trigger holds` (`:152`), a `kit:roles` fence holds the heading
  `## Agent roles — hand the work to its role` and a one-line region whose only line is
  `{{ROLE_ROSTER}}`, as block C. Observed by AC1, AC2 and AC3.
- **S3** — The Tools bullet inside the existing `kit:roles` fence (`:130`) becomes
  `- An attended code build runs through ` followed by the backticked `/build` and a full stop, as
  block B. Observed by AC1 and AC3.
- **S4** — The template marker (`:9`) stays at `v4.3` in this unit's commit. The playbook kit's one
  version move for this build is `PLAY-aOrientedCast-3`'s, which also edits the template and comes
  after this unit (§4 "Kit version"). Observed by AC4.
- **S5** — `AGENTS.md` is re-rendered with `bash tools/playbook/adopt-playbook.sh --target .`. The
  charter renders first, and the agent types are left as they are, because no edit here moves one.
  Observed by AC2 and AC6.
- **S6** — Both size subjects re-record their row in `tools/template-size-highwater.txt` with
  `--bump`. Observed by AC5.
- **S7** — The same commit re-stamps `last-audit` in `memory/guides/SESSION-KICKOFF.md`, because the
  template is on its `watch:` list. `last-body-change` advances only when check 9's count reaches 10
  with this commit. Observed by AC7.
- **S8** — `help/roles.md` describes the `[roles]` rule, its exception and registry, the generated
  Agent roles section, the role fields `mandatory` and `output` beside the `rules` field step 2
  already names, what an agent type carries, the render order after a role or rule edit, and how an
  adopter with an older seeded template takes the new blocks. Observed by AC8.

## 3. Non-goals (OUT)

- The roster's content and line grammar. They are the roles kit's roster verb, which
  `TOOL-aOrientedCast-17` builds; the placeholder row and its probe are `TOOL-aOrientedCast-18`'s.
- The waiver registry's grammar, its grader and how a stand-in is declared. They are
  `TOOL-aOrientedCast-19`'s; the rule and the help page only name the registry.
- The roles kit's `rules` key, its checker and what an agent type carries. They are
  `TOOL-aOrientedCast-16`'s, and so are the help page's step 2 re-key to rule tags and the runbook
  paragraph that describes the old key (its S7).
- Re-rendering `.claude/agents/`. Nothing this unit edits is carried into an agent type (§4 "Render
  order").
- Raising `AGENTS.md`'s 16384-byte ceiling, an owner decision (§8 F2).
- Trimming other charter rules to fund the roster.
- A render note for an adopter whose seeded template lags the shipped minor version (§3 Edges).
- A new gate arm. The legs that grade the template and its render already cover every change here.
- The template's version move, which `PLAY-aOrientedCast-3` carries (§3 Edges).

### Edges

- **consumes-from** `TOOL-aOrientedCast-18` — the `ROLE_ROSTER` `[[placeholder]]` row with
  `class = "derived"` and `kit = "roles"`, and its probe. Without them the render refuses the
  template's `{{ROLE_ROSTER}}` as a placeholder no row declares.
- **consumes-from** `TOOL-aOrientedCast-17` — the `handoff.py roster` lines, one per role file, each a
  `- ` bullet of at most 200 characters, which the probe returns. Their total must fit the budget §4
  derives. The help page also spells that unit's `mandatory` and `output` fields and its verb.
- **consumes-from** `TOOL-aOrientedCast-19` — the registry `role-stand-in-waiver.txt` under the
  memory root's `project/` folder, which the `[roles]` rule and the help page name, and the
  `handoff.py render ... --stand-in` declaration and the roles README's "Standing in for a role"
  section, which the help page points at. §8 F1 records how the name was settled.
- **consumes-from** `TOOL-aOrientedCast-16` — an agent-type render that reads the v4.3 charter's
  tagged rules and carries its Protocols and Facts sections, and the help page's step 2 re-keyed to
  `rules`, which S8 extends. Without it `render_agents.py --check` refuses on the v4.3 charter, so
  AC6 cannot be observed.
- **hands-off** `PLAY-aOrientedCast-3` — the template's one version move for this build, to `v4.4`,
  in that unit's commit. The epoch leg clears this unit's template edit once a later commit bumps the
  marker, so that move dates blocks A to C as well as that unit's own.
- **hands-off** external — an adopter keeps its seeded template across `govkit update`, so a template
  seeded before v4.4 renders without the rule and the section until its owner merges them in. A
  render note naming a seeded template whose minor version lags the shipped one is a follow-up
  outside this build; the help page tells the adopter meanwhile.

## 4. Design

### Evidence

Read at `d518b483` on 2026-10-13, which is BASE `646d4a73` plus this build's landing, the merge of
main's v4.3 charter and the second addendum's records.

- The template is v4.3 (`coding-governance-agents.template.md:9`). Section 1's first one-line region
  is `:13-51`, and `[tools]` is `:46`. The Tools section is `:101-150`, with the roles bullet in a
  `kit:roles` fence at `:129-131`. `## Protocols` is `:152`, its region `:154-166`. No line carries
  a `[roles]` tag.
- `AGENTS.md` is the whole `gov:playbook` region (`:1` to `:158`). Its marker is `:10` and the
  rendered roles bullet `:125`. Gov's `kits` array selects `roles` (`.governance/deploy.toml:25`).
- The renderer drops unselected `kit:` blocks before it collects placeholders
  (`tools/playbook/render_playbook.py:985-995`), so a target without the roles kit never reaches the
  `ROLE_ROSTER` probe. A placeholder no row declares refuses (`:996-999`). A surviving block loses
  its fence markers (`remove_fenced`, `:577-594`). `check_fences` (`:546-575`) refuses only an
  undeclared or unbalanced fence, so one kit id may fence three blocks.
- One-line regions are graded after substitution (`:1011`): every line a `- ` bullet of at most
  `ONE_LINE_MAX = 200` characters (`:126`, `:631-662`). A placeholder value carrying a one-line
  marker refuses (`:820-823`). `--answers <KEY>` resolves one placeholder exactly as the render does
  (`:1648-1654`).
- The playbook kit's version is the template marker (`tools/govkit/entries/playbook.kit.toml:6`).
  `tools/check-placeholders.sh:58-70` requires exactly one marker. `tools/check-playbook-parity.sh`
  pairs the marker's major with `TEMPLATE_MAJOR = 4` (`render_playbook.py:340`). The kit-version
  gate carries no playbook row. `git grep "v4\.3"` outside the memory tree finds the two markers and
  nothing else.
- The template is a `seed` (`playbook.kit.toml:18-26`), and an update never rewrites a seeded
  template (`:134-138`). The default selection holds `playbook` and `roles` but not
  `playbook-render` (`tools/govkit/registry.toml:38-53`), so a default install copies the template
  and fills placeholders by hand.
- Ceilings: the template 49152 (`tools/template-size-limits.txt:33`), `AGENTS.md` 16384 (`:65`), whose
  raise the file calls an owner decision. High-water rows: `AGENTS.md` 14114 and the template 12724
  (`tools/template-size-highwater.txt:2-3`), both already below the files the merge left. Line-length
  cap 450 for both (`tools/line-length-limits.txt:23-24`).
- Parity's kit-coverage arm accepts `<!-- kit:roles -->` in the template or `<prefix>/roles/` in the
  runbook (`tools/check-playbook-parity.sh:223`), so the shorter Tools bullet keeps `roles` named.
- `memory/guides/SESSION-KICKOFF.md:6` watches the template. The staged leg reds a watched change with
  no new stamp (`skills/session-kickoff/manifest-check.sh:1576-1590`), the stamp rule is "sha = HEAD
  on any branch" (`:1339`), and check 9 reds at 10 non-merge watched commits since
  `last-body-change` (`:1568-1571`). No §B claim names the Tools roles bullet or a charter section
  list.
- A builder may run only `lexicon naming predicates` (`tools/roles/house/policy.toml:28`). §6
  therefore observes with the render's write mode, `--answers`, `render_agents.py --check`, greps and
  `python -c` probes, none of which is a leg.

### The new text

**Block A**, inserted after `coding-governance-agents.template.md:46`:

```markdown
<!-- kit:roles -->
- [roles] Spec writing and review, building and the closing review run in role agents (Agent roles); inline only if none can spawn and `{{MEMORY_ROOT}}/project/role-stand-in-waiver.txt` waives it.
<!-- /kit:roles -->
```

The rule renders at 187 characters with `memory` as the root. It stays within 200 while the memory
root and the registry name together take at most 43 characters, so a root of up to 19 characters.
Every section 1 tag is lowercase, and `roles` is unused there.

**Block B**, replacing the bullet at `:130`, inside its existing fence:

```markdown
- An attended code build runs through `/build`.
```

**Block C**, inserted between the blank line at `:151` and `## Protocols` at `:152`:

```markdown
<!-- kit:roles -->
## Agent roles — hand the work to its role

<!-- one-line -->
{{ROLE_ROSTER}}
<!-- /one-line -->

<!-- /kit:roles -->
```

With the roles kit selected, the render reads: the Tools close, a blank line, the heading, a blank
line, the region, a blank line, `## Protocols`. Without it, the Tools close, a blank line and
`## Protocols`, byte-identical to v4.3.

### Bytes, measured

PINNED on 2026-10-13 at `d518b483`, by splicing blocks A to C into CR-stripped copies of both files
and leaving the roster empty. The builder re-measures, because a sibling landing first moves both.

| Subject | Now | After, roster excluded | Ceiling | Left for the roster |
|---|---|---|---|---|
| `coding-governance-agents.template.md` | 12927 | 13186 | 49152 | not applicable |
| `AGENTS.md` | 14762 | 14918 | 16384 | 1466 |

The roster's budget is DERIVED as 16384 minus the measured size without it: each line costs its
length plus one newline. Over the ten role files at `d518b483`, 1466 bytes allow a mean of 145
characters a line, and the longest role `description` there is already 165.
`TOOL-aOrientedCast-17` owns the lines, so the measurement at build time decides, and §8 F2 says
what happens past the ceiling.

### Render order and the agent types

The charter renders first and the agent types second: the roster reads only role files, and an agent
type reads the rendered charter. This unit edits no section 1 rule a role can cite, since a role
citing `roles` would have redded its checker before this unit existed, and no row of
`TOOL-aOrientedCast-16`'s role table cites it. It leaves the text of `## Protocols` and `## Facts`,
the two sections every agent type carries whole, alone, and block C sits above both headings,
outside both sections. So the re-render moves no agent type, and AC6 observes that. A drift there
means a sibling disagrees with this design; the builder stops and reports it rather than
re-rendering `.claude/agents/` here.

### Older seeded templates

This unit reads no charter, so a v3.x one changes nothing here. An adopter's seeded template of v4.3
or earlier carries no `{{ROLE_ROSTER}}`, so the new probe never runs and its render is unchanged. Its
charter lacks the rule and the section until the adopter merges blocks A to C into its seed. The
help page says how, and the §3 hands-off names the render note that would tell them. A default
install copies the template rather than rendering it, so its operator fills `{{ROLE_ROSTER}}` by hand
like every other placeholder, from the output of `handoff.py roster`, the verb
`TOOL-aOrientedCast-18` §8 F1 names.

### Kit version

No kit version moves here. The template is the `playbook` kit's carrier, the marker at
`coding-governance-agents.template.md:9`, read through `version_from`
(`tools/govkit/entries/playbook.kit.toml:6`, `govkit.py` `entry_version` at `:529`). The owner's
third addendum puts two micro-formats and a rule into the same template, and `PLAY-aOrientedCast-3`
(order 21) adds them after this unit, so that unit carries the set's one move, to v4.4. The epoch leg
clears a move of a kit's shipped bytes once a later commit bumps the kit's version
(`derive_epoch_state`, `tools/govkit/govkit.py:12976`), so its bump dates this unit's commit too. The
size record and its gate are registry exemptions (`tools/govkit/registry.toml:280`); `help/` and
`memory/` belong to no kit.

### Probes

The two probes §6 names, run from the repository root on the unit's commit.

```bash
# P1 (AC2): the rendered roster region equals the placeholder's value, one line per role file.
python -c "import sys,json,subprocess as s,glob;v=json.loads(s.run([sys.executable,'tools/playbook/render_playbook.py','--target','.','--answers','ROLE_ROSTER'],capture_output=True,text=True,encoding='utf-8').stdout)['ROLE_ROSTER'];t=open('AGENTS.md',encoding='utf-8').read().replace('\r','');b=t.split('## Agent roles',1)[1].split('<!-- one-line -->\n',1)[1].split('\n<!-- /one-line -->',1)[0];L=b.split('\n');n=len(glob.glob('tools/roles/agents/*.agent.md'));assert b==v,'region differs from the probe';assert len(L)==n,(len(L),n);assert all(x.startswith('- ') and len(x)<=200 for x in L);print('roster ok',len(L),'lines, longest',max(map(len,L)))"

# P2 (AC3): with the roles kit dropped, the template renders as its parent did.
python -c "import sys,subprocess as s;sys.path.insert(0,'tools/playbook');import render_playbook as r;g=lambda c:s.run(['git','show',c+':coding-governance-agents.template.md'],capture_output=True,text=True,encoding='utf-8').stdout.replace('\r','');d={('kit','roles')};assert r.remove_fenced(g('HEAD'),d)==r.remove_fenced(g('HEAD~1'),d),'a target without roles renders a change';print('drop ok')"
```

P2 was run on 2026-10-13 against the spliced scratch copy in place of `HEAD`, and printed equality.

### Inventory

Minted: the section 1 tag `roles` and the heading text `Agent roles — hand the work to its role`.
No function, file, conf key, placeholder or version is minted here, so no
`.lexicon.conf` cell grades a name in this unit.

### Files touched (estimate)

`coding-governance-agents.template.md` · `AGENTS.md` · `tools/template-size-highwater.txt` · `memory/guides/SESSION-KICKOFF.md` · `help/roles.md`

### Rollout

1. Apply blocks A to C to the template, leaving its marker at v4.3.
2. Render the charter: `bash tools/playbook/adopt-playbook.sh --target .`.
3. Run `python tools/roles/render_agents.py --check`. On any drift, stop and report (AC6).
4. Measure `AGENTS.md` with carriage returns stripped. Past 16384, stop before committing (§8 F2).
5. Re-record both rows: `bash tools/check-template-size.sh --bump`, then
   `bash tools/check-template-size.sh --bump AGENTS.md`.
6. Edit `help/roles.md` as §4 "The help page" says.
7. Re-read the §B claims the template feeds, then re-stamp `last-audit` as
   `<ISO datetime> @ <git rev-parse HEAD>` at staging. Derive check 9's count with
   `git rev-list --count --no-merges <last-body-change>..HEAD -- <the watch paths>`; at 9 or more
   before this commit, advance `last-body-change` to the same sha as well.
8. Commit once, with the unit id in the subject.

Rollback is a revert of that one commit: the template, its render, both records and the stamp move
together.

### The help page

`help/roles.md` changes in six places, on the page as `TOOL-aOrientedCast-16` leaves it. Field
names, the registry file, the stand-in declaration and the roster verb are spelled as their units'
specs spell them (§3 Edges).

- The opening paragraph gains a sentence: the charter states this as its `[roles]` rule and lists
  every role under `## Agent roles`, a section generated from the role files.
- Step 2 of "How a task reaches an agent", which names the rule tags a role cites (`rules`), gains
  when the role is mandatory (`mandatory`) and where its output goes (`output`).
- Step 4 says the agent type starts without the full charter and carries the rules its role cites
  and the charter's Protocols and Facts sections.
- "How to use it" states the render order: after changing a role file, re-render the charter with
  `bash tools/playbook/adopt-playbook.sh --target .`, because its Agent roles section is generated
  from the role files; after changing a role, an overlay, the policy or a charter rule, run
  `render_agents.py --write`; then start a new session.
- A new section, `## When no role agent can be spawned`, says inline work is refused and states the
  exception. It names the registry, `role-stand-in-waiver.txt` under `<memory root>/project/`, which
  holds an owner's row per build and role. It says a stand-in declares itself by rendering the
  role's handoff with `handoff.py render ... --stand-in`, and that a waiver never admits a write the
  hooks refuse. For the row grammar it points at the roles README's "Standing in for a role"
  section rather than restating it: no tree holds the registry until an owner writes its first row.
- "In a repository that adopts the kit" gains a bullet: the rule and the section ship with template
  v4.4; a template seeded earlier keeps rendering without them, so merge blocks A to C from gov's
  template into yours and re-render. Without the playbook renderer, fill `{{ROLE_ROSTER}}` from
  `python <prefix>/roles/handoff.py roster`.

### Alternatives rejected

- **The heading outside the fence.** A target without the roles kit would render a heading over an
  empty region, a section that is false for it. `PLAY-aOrientedCast-1` rejected an unfenced bullet
  for the same reason: a kit-conditional rule is fenced by the entry that ships it.
- **A static exception bullet in the Agent roles region.** It costs about 140 bytes of the budget the
  roster needs, and the owner put the exception in the rule.
- **Keeping the Tools bullet whole.** It would state a weaker form of the `[roles]` rule a second time,
  two answers to one question.
- **The rule after `[spec]`.** Either placement reads. After `[tools]` keeps the two rules that point
  at section 3 adjacent.
- **Moving the template's version here as well.** A second move in this build would date nothing the
  later one does not, and the epoch leg needs only the last.
- **Funding the roster by trimming other rules.** No rule here is made redundant by it, and each is
  an owner-ratified practice (§8 F2).

## 5. Production-readiness checklist

- security — no code and no new write path. The rule names an owner-only waiver registry; it widens
  nothing.
- perf / scale — every session reads `AGENTS.md`, which grows by 156 bytes plus the roster, at most
  1466 bytes, inside its 16 KiB ceiling (§4 "Bytes, measured").
- error / empty / loading states — a target without the roles kit renders none of this (AC3). An
  empty roster refuses the render, as every derived placeholder whose probe returns nothing does
  (`resolve_placeholder_raw`, `render_playbook.py:826`). A roster line past 200 characters refuses
  the render by line number.
- observability — the render prints a `derived ROLE_ROSTER` note, and `--answers ROLE_ROSTER` prints
  the value alone.
- risks — the roster can push `AGENTS.md` past its ceiling (§8 F2). The rule renders at 187 of 200
  characters, so an adopter whose memory root passes 19 characters gets a named render refusal on
  that line. The registry name is a sibling's to mint (§8 F1). Seeded templates lag (§3 Edges).
- testing — the size, line-length, parity, render, placeholder, epoch, version, manifest, dead-path
  and roles legs at the close; this unit adds no arm. §6 observes each change directly.
- migration — gov renders at this commit. An adopter's charter re-renders from its own seed at
  `govkit update`, unchanged until the adopter merges the new blocks; the help page says how.
- user docs — `help/roles.md` (S8).

## 6. Acceptance criteria

No criterion runs a gate leg, a suite or a `--selftest` flag. Each reads a file, runs the render's
write mode, or runs a probe from §4 "Probes".

- **AC1** — When `grep -n "kit:roles\|\[roles\]\|\[tools\]\|## Agent roles\|ROLE_ROSTER\|runs through\|## Protocols" coding-governance-agents.template.md`
  runs, it prints six fence lines and: the `[roles]` rule once, inside the first fence pair, whose
  opening line directly follows `[tools]`; the Tools bullet once, reading only "An attended code build runs through" and
  the backticked `/build`, inside the second pair; and `## Agent roles — hand the work to its role`
  once, in the third pair, above `{{ROLE_ROSTER}}`, which sits alone between `<!-- one-line -->` and
  `<!-- /one-line -->`. That pair's closing fence is the line before `## Protocols`.
  Red when: a block is unfenced, out of order or outside its region, or the Tools bullet keeps its
  first sentence.
- **AC2** — When `bash tools/playbook/adopt-playbook.sh --target .` runs on the unit's commit, it
  exits 0 and `git diff --quiet -- AGENTS.md` exits 0 afterwards; `grep -c "kit:roles" AGENTS.md`
  prints 0; the rendered `[roles]` rule appears once, naming `role-stand-in-waiver.txt` under
  `memory/project/`; and probe P1 prints `roster ok`.
  Red when: the committed region differs from a fresh render, a fence marker survives, or the roster
  region disagrees with the `--answers ROLE_ROSTER` value, its line count or its 200-character cap.
  figure: the expected line count is DERIVED from the role files when P1 runs.
- **AC3** — When probe P2, which applies `remove_fenced` with the roles kit dropped to the template
  at `HEAD` and `HEAD~1`, runs on the unit's commit, it prints `drop ok`.
  Red when: a target without the roles kit renders anything this unit added, a blank line included.
- **AC4** — When `git show HEAD:coding-governance-agents.template.md | grep -c "governance-template: v4.3"`
  and the same over `AGENTS.md` run on the unit's commit, each prints 1.
  Red when: this unit moves the template's marker, which `PLAY-aOrientedCast-3` moves once for the
  set, or the render carries a different value from its template.
- **AC5** — When `tr -d '\r' < AGENTS.md | wc -c` and the same over
  `coding-governance-agents.template.md` run on the unit's commit, the first prints at most 16384 and
  the second at most 49152, and each equals its row in `tools/template-size-highwater.txt`.
  Red when: `AGENTS.md` passes its declared ceiling, or either row was not re-recorded.
  figure: DERIVED at observation; §4's projection is PINNED at `d518b483`.
- **AC6** — When `python tools/roles/render_agents.py --check` runs after the charter re-render, it
  exits 0 and names no `drift`, `missing` or `stale` path.
  Red when: the template edit moved an agent type, which means a role cites a rule or reads a
  section this unit was designed not to touch.
- **AC7** — When `git show` reads `memory/guides/SESSION-KICKOFF.md` at `HEAD` and at `HEAD~1` and
  `grep "^last-audit:"` runs over each, the two lines differ and the first ends with the sha
  `git rev-parse HEAD~1` prints; and the `git rev-list --count --no-merges` count of §4 "Rollout"
  step 7 prints under 10 at `HEAD`.
  Red when: the commit stages a watched file with no new stamp, or check 9's stall count reaches 10.
- **AC8** — When `grep -n "Agent roles\|\[roles\]\|role-stand-in-waiver\|--stand-in\|mandatory\|adopt-playbook\|v4.4" help/roles.md`
  runs, it shows the rule and the generated section, the registry and the `--stand-in` declaration
  inside a section on the exception, the `mandatory` and `output` fields in step 2, the
  charter-then-agents render order and the v4.4 seed note.
  Red when: the page omits the rule, the section, either field, the exception, the registry, the
  declaration, the render order or the seed note.

## 7. Gates

`template size <=48KiB` · `charter size` · `line length` · `playbook parity` · `playbook render wiring` · `playbook placeholder catalogue` · `micro-format definitions` · `kickoff-manifest ratchet` · `kit epoch (shipped bytes move, the version moves)` · `kit version markers` · `dead-path carriers (deleted files still named)` · `agent-instructions wiring` · `agent-cap restatement` · `roles catalogue` · `roles render wiring` · `recall floor` · `recall floor arms` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

This unit adds no gate arm. The main loop runs the legs above once, at the close; no pass runs one.

## 8. Open questions

- **F1 — The waiver registry's file name is minted by `TOOL-aOrientedCast-19`, specced at the same
  time as this unit. How do the `[roles]` rule and the help page spell it?**
  (a) Spell the name that unit's spec mints, and let its spec govern any later disagreement: M2
  fixes a disagreement in one document, and the name is that unit's to mint.
  (b) Name no path: the rule says "an owner waiver row", and the help page points at the roles kit's
  README.
  (c) A second derived placeholder that renders the registry path from the roles kit.
  (b) leaves an agent reading the charter no file to check, and drops what the brief's row asks the
  rule to name. (c) adds a descriptor row and a probe outside this unit's write set, a second
  mechanism with more open questions.
  Recommendation: (a), the option satisfying the most of what the design asks. That spec, read on
  2026-10-13, mints `role-stand-in-waiver.txt` under `<MEMORY_ROOT>/project/` (its §2 S1) and hands
  that spelling to this unit in its §3 Edges, and gov's rule renders at 187 characters with it.
  RESOLVED (agent, 2026-10-13, delegated): (a), spelled `role-stand-in-waiver.txt`.
- **F2 — What does the build do if the re-rendered `AGENTS.md` measures over its 16384-byte ceiling?**
  The roster is `TOOL-aOrientedCast-17`'s output and its length is unknown when this spec is written;
  §4 derives the budget it must fit.
  (a) Raise `AGENTS.md`'s row in `tools/template-size-limits.txt`. That file and the size gate's own
  message make a raise an owner decision recorded in `memory/DECISIONS.md`: M3 veto 2.
  (b) Trim other charter rules to fund the roster. That edits owner-ratified practices outside this
  unit's mechanism, a §3 non-goal: M3 veto 1.
  (c) Shorten the roster lines or narrow the roster. That is the roster verb's and the probe's
  contract, so it is an M2 AMEND of a sibling's spec, which the main loop may make and a builder may
  not.
  (d) Commit nothing, and return the measured size and the overage to the main loop, which takes
  (c) by an AMEND or parks the unit for the owner with (a) beside it.
  Recommendation: (d). It is the only option a builder may take, and it leaves (c) to the one
  resolver allowed to take it.
  RESOLVED (agent, 2026-10-13, delegated): (d).

## 9. Revision log

- rev-1 · 2026-10-13 · initial draft.
- rev-2 · 2026-10-13 · §1 · S4 · AC4 · §3 · §4 · the template's version move goes to
  `PLAY-aOrientedCast-3`, which the owner's third addendum added and which edits the template after
  this unit, so it is now the last unit to touch it. S4 and AC4 now hold the marker at v4.3 in this
  unit's commit; block D, its Inventory entry and probe P2's marker rewrite leave §4, whose "Kit
  version" says why; §3 gains the non-goal and a hands-off edge to that unit. The help page still
  names v4.4, the version that first ships the rule and the section.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "render a generated section of the charter listing the
agent roles from a derived placeholder inside a kit fence"` ranked name-token neighbours (`render`,
`kit_rel`, `resolve_kit_dir`, `extract_charter_sections`) and no seam for charter prose. The seams
reused, each verified at source: the renderer's `kit:` fence pass, `remove_fenced`
(`tools/playbook/render_playbook.py:577`), which already drops the Tools bullet's `kit:roles` block;
the one-line region grade, `check_one_line_regions` (`:631`), which grades the roster after
substitution as it grades section 2's `{{ADOPTER_RULES}}`; and the derived-placeholder route
`{{NODE_TABLE}}` takes, `PROBES` (`:530`) and `derive_node_table` (`:421`), which
`TOOL-aOrientedCast-18` extends. This unit writes no code. Where the record and the source disagreed:
the brief places `PROBES` at line 528, and it is at 530 on `d518b483`.

Recall terms used: `charter template kit fence one-line region derived placeholder NODE_TABLE render
AGENTS.md high-water governance-template marker` — which surfaced `PLAY-aOrientedCast-1` (the
`kit:roles` fence and pricing growth against the high-water), `TOOL-aDistilledCharter-2` and
`TOOL-aDistilledCharter-5` (the `NODE_TABLE` derived placeholder and its probe), and
`PLAY-aDistilledCharter-1` (the fence pass as the seam a kit-conditional rule extends).
