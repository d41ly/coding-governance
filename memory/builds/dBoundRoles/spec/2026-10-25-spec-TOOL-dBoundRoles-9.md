# TOOL-dBoundRoles-9 — the `none` and `review` write classes enforced in the role arm

**Status:** OPEN · rev-2 · 2026-10-26 · node d · Tier-2 · base 4ed9e567 · streams tooling · order 13 · advances TOOL-dBoundRoles-27

**Carries:** cl-dClosedLoop-0174@b2c09e04 whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dBoundRoles-1-reuse-scout-c.md](../build/2026-10-25-build-TOOL-dBoundRoles-1-reuse-scout-c.md) | research | TOOL-dBoundRoles-1 TOOL-dBoundRoles-7 TOOL-dBoundRoles-8 TOOL-dBoundRoles-16 TOOL-dBoundRoles-21 TOOL-dBoundRoles-22 TOOL-dBoundRoles-25 |
| [2026-10-25-build-TOOL-dBoundRoles-1-spec-stage-returns.md](../build/2026-10-25-build-TOOL-dBoundRoles-1-spec-stage-returns.md) | research | TOOL-dBoundRoles-1 TOOL-dBoundRoles-2 TOOL-dBoundRoles-3 TOOL-dBoundRoles-4 TOOL-dBoundRoles-5 TOOL-dBoundRoles-6 TOOL-dBoundRoles-7 TOOL-dBoundRoles-8 TOOL-dBoundRoles-10 TOOL-dBoundRoles-11 TOOL-dBoundRoles-12 TOOL-dBoundRoles-13 TOOL-dBoundRoles-14 TOOL-dBoundRoles-15 TOOL-dBoundRoles-16 TOOL-dBoundRoles-17 TOOL-dBoundRoles-18 TOOL-dBoundRoles-19 TOOL-dBoundRoles-20 TOOL-dBoundRoles-21 TOOL-dBoundRoles-22 TOOL-dBoundRoles-23 TOOL-dBoundRoles-24 TOOL-dBoundRoles-25 TOOL-dBoundRoles-26 |
| [2026-10-26-build-TOOL-dBoundRoles-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dBoundRoles-1-agent-ledger.md) | journal | TOOL-dBoundRoles-1 TOOL-dBoundRoles-2 TOOL-dBoundRoles-3 TOOL-dBoundRoles-4 TOOL-dBoundRoles-5 TOOL-dBoundRoles-6 TOOL-dBoundRoles-7 TOOL-dBoundRoles-8 TOOL-dBoundRoles-10 TOOL-dBoundRoles-11 TOOL-dBoundRoles-12 TOOL-dBoundRoles-13 TOOL-dBoundRoles-14 TOOL-dBoundRoles-15 TOOL-dBoundRoles-16 TOOL-dBoundRoles-17 TOOL-dBoundRoles-18 TOOL-dBoundRoles-19 TOOL-dBoundRoles-20 TOOL-dBoundRoles-21 TOOL-dBoundRoles-22 TOOL-dBoundRoles-23 TOOL-dBoundRoles-24 TOOL-dBoundRoles-25 TOOL-dBoundRoles-26 TOOL-dBoundRoles-37 TOOL-dBoundRoles-38 TOOL-dBoundRoles-39 TOOL-dBoundRoles-40 TOOL-dBoundRoles-41 TOOL-dBoundRoles-42 TOOL-dBoundRoles-43 TOOL-dBoundRoles-44 TOOL-dBoundRoles-45 TOOL-dBoundRoles-46 TOOL-dBoundRoles-47 TOOL-dBoundRoles-48 TOOL-dBoundRoles-49 TOOL-dBoundRoles-50 TOOL-dBoundRoles-51 |
| [2026-10-25-prompt-TOOL-dBoundRoles-1-spec-brief.md](../prompts/2026-10-25-prompt-TOOL-dBoundRoles-1-spec-brief.md) | research | TOOL-dBoundRoles-1 TOOL-dBoundRoles-2 TOOL-dBoundRoles-3 TOOL-dBoundRoles-4 TOOL-dBoundRoles-5 TOOL-dBoundRoles-6 TOOL-dBoundRoles-7 TOOL-dBoundRoles-8 TOOL-dBoundRoles-10 TOOL-dBoundRoles-11 TOOL-dBoundRoles-12 TOOL-dBoundRoles-13 TOOL-dBoundRoles-14 TOOL-dBoundRoles-15 TOOL-dBoundRoles-16 TOOL-dBoundRoles-17 TOOL-dBoundRoles-18 TOOL-dBoundRoles-19 TOOL-dBoundRoles-20 TOOL-dBoundRoles-21 TOOL-dBoundRoles-22 TOOL-dBoundRoles-23 TOOL-dBoundRoles-24 TOOL-dBoundRoles-25 TOOL-dBoundRoles-26 |
| [2026-10-26-review-TOOL-dBoundRoles-1-spec-audit-round1.md](../reviews/2026-10-26-review-TOOL-dBoundRoles-1-spec-audit-round1.md) | spec-audit | TOOL-dBoundRoles-1 TOOL-dBoundRoles-10 TOOL-dBoundRoles-11 TOOL-dBoundRoles-12 TOOL-dBoundRoles-13 TOOL-dBoundRoles-14 TOOL-dBoundRoles-15 TOOL-dBoundRoles-16 TOOL-dBoundRoles-17 TOOL-dBoundRoles-18 TOOL-dBoundRoles-19 TOOL-dBoundRoles-2 TOOL-dBoundRoles-20 TOOL-dBoundRoles-21 TOOL-dBoundRoles-22 TOOL-dBoundRoles-23 TOOL-dBoundRoles-24 TOOL-dBoundRoles-25 TOOL-dBoundRoles-26 TOOL-dBoundRoles-3 TOOL-dBoundRoles-4 TOOL-dBoundRoles-5 TOOL-dBoundRoles-6 TOOL-dBoundRoles-7 TOOL-dBoundRoles-8 |

<!-- /gen:spec-records -->

## 1. Goal

The role arm of the write gate grades two of the five write classes today: a role declaring `none` or
`review` is refused only on spec and product paths, and every other repository write it makes is
admitted (`tools/hooks/scratch-guard.js:102-103`, "`none`, `review` and `records` are declared in the
index and read by nothing here"; step 6 returns null at `:1173`). This unit makes the role arm enforce
both: a `none` role writes nothing in the repository, and a `review` role writes only under a build's
reviews folder, the folder the index's new `classes` map names from the one place it is spelled. It
closes the second half of gap-orient-09 ("the `none` and `review` write classes are declared but read
by nothing").

## 2. Scope (IN)

- **S1** — `WRITE_FOLDERS` moves from `tools/roles/check_roles.py:99` into `tools/roles/roles_lib.py`,
  beside `WRITES`, with its value unchanged; `check_roles.py` reads `lib.WRITE_FOLDERS` at its one use
  (R14, `check_roles.py:233`). Observed by AC6.
  **Readers:** by name: `tools/roles/check_roles.py`, its R14 lookup re-pointed to the library's dict ·
  by value: `tools/roles/check_roles.py`, whose R14 compares each role's `output` with its class's
  folder, unchanged in verdict, and `tools/roles/render_agents.py`, which renders S2's map from it.
- **S2** — `render_roles_index` (`tools/roles/render_agents.py:207`) writes a top-level `classes` key
  into `.claude/roles.json`: one entry per `WRITE_FOLDERS` key, its value the folder spelled exactly as
  the dict spells it, the `{{MEMORY_ROOT}}` token and the `<slug>` placeholder kept. This is shared
  interface I23; the index's other keys are unchanged. Observed by AC5.
- **S3** — `loadRoleIndex` (`scratch-guard.js:952`) grades `classes` when present, an object whose every
  value is a string, and returns it as `classes`, null when absent; any other shape is `broken`, as a
  malformed role `gates` is today (`:977-979`). Observed by AC5.
- **S4** — `matchWriteClass(rel, cls, index, memRoot)` in `scratch-guard.js`: whether a repo-relative
  target lies in class `cls`'s folder as the index's `classes` spells it, with `{{MEMORY_ROOT}}`
  substituted by the conf's `MEMORY_ROOT` normalised as `checkUnarmed` normalises it, `<slug>` matching
  exactly one path segment, and a trailing `/` meaning the folder and everything under it. The hook
  carries no second literal of a class folder. Observed by AC2 and AC3.
- **S5** — Step 6b of `checkRouted`'s one evaluation order (`scratch-guard.js:1113`): a target that is
  neither a product nor a spec path, written by a payload whose `agent_type` names an `agent`-true role
  of the index, reads that role's `writes`. `none` refuses. `review` admits only a target
  `matchWriteClass(rel, "review", …)` places, and refuses every other. Every other class reads as
  today: `spec`, `product` and `records` roles, the main loop and an agent type the index does not
  name are admitted there exactly as at base. An absent index takes the verdict `checkRoleWrite` gives
  an absent index; a broken one refuses; an index with no `classes` refuses a `review` role's write
  and names the re-render. Observed by AC1, AC2, AC4 and AC7.
- **S6** — `checkRoleClass(writes, cls)`, the one predicate S5 and the spec and product steps share:
  given a role's `writes` and a target's class (`spec`, `product`, `review` or `other`), it answers
  admit or refuse, so the shell arm TOOL-dBoundRoles-7 builds asks the same question through the same
  function rather than a copy. Observed by AC1 and AC4.
- **S7** — Every refusal S5 adds names the target, the class it falls in, the role and its `writes`,
  and a remedy with its actor: the driver, which routes the write to a role whose class covers it, or,
  for a review report under the harness's default `reviews/`, the caller, which passes `reviewDir`
  under `<MEMORY_ROOT>/builds/<slug>/reviews/`. Observed by AC2.
- **S8** — The hook's header (`scratch-guard.js:91-104`) and the role-arm section of
  `tools/hooks/README.md` (`:369`) state the four graded classes and that `records` alone is declared
  and read by nothing here; the user page `help/roles.md`, section "What the hooks refuse" (`:103`),
  gains the bullet for a `none` role's write and a `review` role's write outside a reviews folder.
  Observed by AC8.

## 3. Non-goals (OUT)

- The `records` class. The clause names `none` and `review`; a `records` role is admitted where it is
  today, and the header says so (S8).
- A refusal for an agent type the index does not name, `workflow-subagent` included. Its verdict on a
  spec or product path is the one at base; elsewhere it stays admitted. Deny-by-default for an unnamed
  type is TOOL-dBoundRoles-6's and TOOL-dBoundRoles-8's ground, not this clause's.
- The absent-index verdict. TOOL-dBoundRoles-6 turns an absent index into a refusal; S5 calls the same
  branch `checkRoleWrite` takes, so whichever verdict that unit lands applies here unchanged.
- Shell writes: TOOL-dBoundRoles-7, which classes each shell target through this unit's map and
  predicate.
- Binding a review role to ONE build's reviews folder. That is the work order's `allowance`
  (TOOL-dBoundRoles-3), which narrows a class and never widens it (§8 F1).
- The spec class's own path literal at step 6 (`scratch-guard.js:1170-1173`). It stays as it is (§8 F3).
- The review harness's default `reviewDir` of `reviews/` (`tools/workflows/tier2-review.template.js:297`).
  A typed synthesizer writing there is refused by S5, and the refusal names the remedy; changing the
  harness default is not this clause.

### Edges

- **hands-off** `TOOL-dBoundRoles-7` — the index's `classes` map and the `checkRoleClass` and `matchWriteClass` predicates, so the shell arm classes each shell write target from the one spelling of each class folder
- **hands-off** `TOOL-dBoundRoles-43` — the `none` class, whose population after unit 1 unit 43 re-derives (id 20 of the round-1 spec audit)

## 4. Design

### The class map in the index

```json
{
  "classes": {
    "product": "ROUTED_PATHS",
    "records": "{{MEMORY_ROOT}}/",
    "review": "{{MEMORY_ROOT}}/builds/<slug>/reviews/",
    "spec": "{{MEMORY_ROOT}}/builds/<slug>/spec/"
  },
  "gates": { "manifest": "tools/gate-legs.json" },
  "harnesses": ["…"],
  "roles": { "…": "…" }
}
```

The values are `WRITE_FOLDERS`'s, copied by `render_roles_index` with `json.dumps(…, sort_keys=True)`
as every other key is (`render_agents.py:216`). The product class's value is the conf key that holds
its paths, as the dict already spells it, so `matchWriteClass` is never asked about `product`: step 6
already places a product target through `ROUTED_PATHS` (`scratch-guard.js:1163-1166`).

### Step 6b

At base, step 6 places a target as product (a `ROUTED_PATHS` entry matched) or spec (under
`<MEMORY_ROOT>/builds/<seg>/spec/`) and returns null for anything else (`:1173`). Step 6b replaces that
null for a typed role only:

```
6b. neither product nor spec:
    agent_type empty                          -> null   (main loop, unchanged)
    index = loadRoleIndex(top)
      absent                                  -> the absent verdict of checkRoleWrite
      broken                                  -> deny, naming the index
    role = index.roles[agent_type]; not agent-true or not named -> null   (unchanged)
    cls  = matchWriteClass(rel, "review", index, memRoot) ? "review" : "other"
    checkRoleClass(role.writes, cls):
      writes none                             -> deny
      writes review, cls review               -> null
      writes review, cls other                -> deny
      writes review, index.classes null       -> deny, naming the re-render
      writes spec | product | records         -> null   (unchanged)
```

`checkRoleClass` is pure: it reads no file, so steps 6a and 9a call it for the `spec` and `product`
classes and keep every verdict they give at base (a role in the class admits; any other is refused,
the status flip of `checkStatusOnlyEdit` applied after it as today).

### Inventory

Minted: the `classes` index key; `matchWriteClass`, `checkRoleClass`; step 6b of `checkRouted`; the
fixture plants of §7's arm (`none-other`, `review-in`, `review-out`, `review-default-dir`,
`review-mem-root`, `review-no-classes`, `spec-role-other`). Each function name is asked of
`python tools/lexicon/lexicon.py --suggest <name> --as js.function` at the pass. Both new functions
join `module.exports` beside `checkRoleGate` (`scratch-guard.js:1615`), so TOOL-dBoundRoles-7 and the
suite import them.

### Migration

Additive for every role but the two classes. The index re-renders through `adopt-roles.sh --scaffold`,
the roles kit's `[[regenerate]]` row; until it does, a `review` role's write outside spec and product
paths is refused naming the re-render, and a `none` role's is refused regardless, because a `none`
role needs no map. In this repository the `review` role is `gov-synthesizer`, and the `none` roles are
the orienter, the researcher, the reuse scout, the two reviewers and the skeptic (`.claude/roles.json`
at base); none of them writes a repository file in its workflow today: their records are extracted from
transcripts by the main loop, and their temporary files go under the session scratchpad, outside the
repository, which step 3 never gates.

### Rollout

Live at landing in the hooks kit; no switch. The clause is an enforcement, and the population it newly
refuses is the classes that declared they write nothing or only review reports.

### Files touched (estimate)

- `tools/hooks/scratch-guard.js`
- `tools/hooks/scratch-guard.test.sh`
- `tools/hooks/README.md`
- `help/roles.md`
- `tools/roles/roles_lib.py`
- `tools/roles/check_roles.py`
- `tools/roles/render_agents.py`
- `.claude/roles.json` (the render's copy, written by `render_agents.py --write`)

### Alternatives rejected

- **A review-folder literal in the hook.** It is the second copy I23 exists to prevent; `WRITE_FOLDERS`
  already spells the folder for R14.
- **Refusing every repository write from a typed role outside its class, spec and product roles
  included.** A spec writer writes deviation records under `build/` and a builder writes its acceptance
  ledger there; the clause names two classes, and widening it to the others refuses work they do.

## 5. Production-readiness checklist

- security — narrows the write surface: two classes that admitted every non-spec, non-product write now
  admit nothing and one folder; deny by default where the map is absent.
- perf / scale — one extra read of `.claude/roles.json`, only for a typed agent's write outside spec and
  product paths; the index is a few KB.
- error / empty / loading states — absent index, broken index and absent `classes` each have a stated
  verdict (S5); the hook stays fail-closed on a throw (`scratch-guard.js:1544-1550`).
- observability — each refusal names target, class, role, its `writes` and the remedy's actor (S7).
- risks — a typed synthesizer run with the harness's default `reviewDir` is refused; the refusal names
  the remedy, and BUILD-METHOD M8 already requires an explicit `reviewDir`.
- testing — the plants of §4's inventory, run by a pass through `checkRouted` over a fixture
  repository; the suite arm in §7 is observed RED then GREEN by the main loop at the close.
- migration — the index re-render, as §4 Migration says.
- user docs — `help/roles.md`'s "What the hooks refuse" and `tools/hooks/README.md` (S8).

## 6. Acceptance criteria

Each criterion runs `checkRouted` through `node -e` over a fixture repository made under `%TEMP%` with
`git init`, a `.memory-tree.conf` declaring `MEMORY_ROOT` and `ROUTED_PATHS`, and a rendered
`.claude/roles.json`, the payload carrying `tool_name: "Write"`, a `cwd` and the named `agent_type`.

- **AC1** — When a `Write` to a file `a.md` under the fixture's `memory/builds/x/build` folder
  carries `agent_type` `gov-researcher` (a `none` role), `checkRouted` returns a `deny` naming the
  class `none`; with `agent_type` empty it returns null.
  Red when: step 6 still returns null for a target in neither class, as `scratch-guard.js:1173` does at
  base, so the `none` role's write is admitted.
- **AC2** — When `agent_type` is `gov-synthesizer` (`review`), a `Write` to a file `r.md` under
  `memory/builds/x/reviews` returns null, one under `memory/builds/x/build` returns a `deny`, and one
  under the fixture root's `reviews` folder, the harness default, returns a `deny` whose text names
  `reviewDir`.
  Red when: `review` admits any non-spec path, or the refusal names no remedy.
- **AC3** — When the fixture conf sets `MEMORY_ROOT="mem"`, a `review` role's `Write` to a file under
  `mem/builds/x/reviews` returns null and one under `memory/builds/x/reviews` returns a `deny`.
  Red when: the hook matches a literal `memory/` rather than substituting `{{MEMORY_ROOT}}` from the
  conf.
- **AC4** — When `agent_type` is `gov-spec-writer`, a `Write` to a file under `memory/builds/x/build`
  returns null; when it is `gov-researcher`, a `Write` to a file under `memory/builds/x/spec` returns
  the spec arm's `deny` unchanged from base.
  Red when: step 6b refuses a `spec` role outside its class, or `checkRoleClass` changes the verdict
  of step 6a.
- **AC5** — When `python tools/roles/render_agents.py --write` runs over the fixture,
  `.claude/roles.json`'s `classes.review` reads `{{MEMORY_ROOT}}/builds/<slug>/reviews/`; and when
  `loadRoleIndex` reads an index whose `classes` is `3`, it returns `state` `broken`.
  Red when: the render omits `classes`, or `loadRoleIndex` accepts a non-object `classes`.
- **AC6** — When `grep -n "^WRITE_FOLDERS = " tools/roles/roles_lib.py tools/roles/check_roles.py` runs,
  it prints one line, in `roles_lib.py`; and a `python -c` probe importing `check_roles` from
  `tools/roles/` finds that the dict its R14 lookup reads is `roles_lib.WRITE_FOLDERS` itself.
  Red when: `check_roles.py` keeps its own copy of the dict, so the class folder is spelled twice.
- **AC7** — When the fixture's index has no `classes` key, a `review` role's `Write` to
  a file under `memory/builds/x/reviews` returns a `deny` naming the re-render; when the index is absent, the
  same write returns the verdict `checkRoleWrite` returns for an absent index on a spec write in the
  same fixture.
  Red when: an absent `classes` admits the write, or the absent-index verdict differs from the spec
  arm's.
- **AC8** — When `grep -n "records" tools/hooks/scratch-guard.js` runs over the header block, the role
  arm's paragraph names `records` as the one class read by nothing, and
  `grep -n "review" tools/hooks/README.md help/roles.md` shows the role-arm section and the page's
  "What the hooks refuse" list naming the `review` folder rule.
  Red when: the header still says `none`, `review` and `records` are read by nothing, or the page
  lists no refusal for the two classes.

## 7. Gates

`scratch-guard self-test` · `agent-cap self-test` · `format-guard self-test` · `verifier fan-out self-test` · `review-join self-test` · `hook destinations self-test` · `check-wiring self-test` · `lexicon naming predicates` · `roles catalogue` · `roles render wiring` · `roles render selftest` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/hooks/scratch-guard.test.sh · covers AC1 AC2 AC3 AC4 AC7 · the `none-other`, `review-out`, `review-default-dir` and `review-no-classes` plants stage the failing case against a hook whose step 6b is reverted · none

## 8. Open questions

- **F1 — Which reviews folder does a `review` role write: any build's, or only the build it works
  for?** Options: (a) any `<MEMORY_ROOT>/builds/<one segment>/reviews/`, the folder `WRITE_FOLDERS`
  spells with its `<slug>` placeholder; (b) only the build the session card routes or the spawn marker
  names. (b) needs a binding from the writing agent to its work order, which the hook does not have at
  base and which TOOL-dBoundRoles-7 builds from TOOL-dBoundRoles-3's `allowance`. RESOLVED (agent,
  2026-10-25, delegated): (a), rung 3, the class the spec arm already applies to any build
  (`scratch-guard.js:1170-1173`); the allowance narrows it per work order. widens: none · relaxes: none
- **F2 — Where does `WRITE_FOLDERS` live so the renderer and the checker read one copy?** Options: (a)
  `roles_lib.py`, beside `WRITES`, which TOOL-dDeclaredLoop-9 S4 moves there; (b) `render_agents.py`
  imports `check_roles.py`; (c) a second literal in `render_agents.py`. (c) is the defect I23 names; (b)
  makes the renderer import the checker, whose import of the library is the kit's one direction.
  RESOLVED (agent, 2026-10-25, delegated): (a), rung 3, tie-broken by reuse of the library seam
  TOOL-dDeclaredLoop-9 S4 sets. The build run re-grounds on that section; if `WRITES` is still in
  `check_roles.py` then, `WRITE_FOLDERS` moves alone and the two sit apart until it lands.
  widens: none · relaxes: none
- **F3 — Does the spec class move onto the `classes` map too?** Options: (a) only `review` reads the
  map; the spec literal at step 6 stays; (b) both read the map. (b) puts an index read in front of every
  main-loop spec write and makes the spec arm depend on an index re-render that a hooks-kit update can
  precede, refusing spec writes across that window. RESOLVED (agent, 2026-10-25, delegated): (a), rung
  3, the option with fewer open questions; the spec literal pre-exists and this unit adds no second
  one. widens: none · relaxes: none
- **F4 — An index with no `classes` key and a `review` role's write.** Options: (a) refuse, naming the
  re-render; (b) fall back to a literal. (b) is a second literal, the defect of F2. RESOLVED (agent,
  2026-10-25, delegated): (a), rung 3, deny by default (the charter's `[security]`).
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, from the packet's Items 9, the brief's shared interface I23,
  scout C's row for cl-0174, and `tools/hooks/scratch-guard.js` and `tools/roles/` at base `4ed9e567`.
- rev-2 · 2026-10-26 · §3 · the Edges block gains the **hands-off** bullet mirroring the edges of TOOL-dBoundRoles-43, promoted by the round-1 spec audit of the 26 unit specs; nothing else moved.

## 10. Reuse audit

The seam extended is the role arm of `tools/hooks/scratch-guard.js`: `checkRouted`'s step 6
(`:1169-1178`), `checkRoleWrite` (`:1064-1086`) and `loadRoleIndex` (`:952-989`), with
`render_roles_index` (`tools/roles/render_agents.py:207-216`) as the index's one writer and
`WRITE_FOLDERS` (`tools/roles/check_roles.py:99-101`) as the one spelling of each class folder.
`python tools/codebase-map/reuse_lookup.py "refuse a role agent write outside its write class"` ranked
generic name stems (`write`, `RolesError`, `load_roles`) and named no class matcher, so no existing seam
fits for the folder match itself; `matchWriteClass` is new and reads the map rather than a literal.
Scout C's row (`memory/builds/dBoundRoles/build/2026-10-25-build-TOOL-dBoundRoles-1-reuse-scout-c.md:17`)
agreed with source at every line it cites; its `checkRouted` step-6 reference `:1170-1179` is
`:1169-1178` at base `4ed9e567`, one line earlier.

Recall terms used: `python tools/memory-recall/query.py "which write classes does the role arm enforce and which are read by nothing" --terms "role arm write class none review records scratch-guard checkRoleWrite WRITE_FOLDERS roles.json index"`
