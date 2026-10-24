**Serves:** research PLAY-dOrderedCharter-1

# dOrderedCharter's specs against its parents' landed specs: a read-only cross-check

Node d, 2026-10-24, base `5e2007467` (origin/main). dOrderedCharter's spec run landed at `32165a706`
(02:41). Later that day dSafePassage re-grounded eight specs against dGroundRules' landed specs
(`bfa738f13`, then `234481624` and `68bef398e`, landed at `1769e08cc` and `5e2007467`). dOrderedCharter's
specs predate both its parents' final text, so this record compares each assumption they make about a
parent with what the parents' DEFERRED specs now say. It is not an audit: no spec was edited, no review
harness ran, and the verdicts feed the build run's re-ground step.

**Counts:** 52 assumptions · 26 AGREES · 21 MISMATCH · 5 UNKNOWN UNTIL BUILT · plus 9 parent surfaces
dOrderedCharter relies on without naming them. Of the 52, 26 are about dSafePassage (18 · 6 · 2) and
26 about dGroundRules (8 · 15 · 3).

## Method

- Population: `grep -l dSafePassage memory/builds/dOrderedCharter/spec/*.md` gives 8 specs (19, 30,
  31, 33, 34, 35, 37, 49); `grep -l dGroundRules` gives 23 (1, 2, 4, 6, 7, 9, 11, 14, 15, 19, 20, 25,
  26, 27, 31 to 37, 46, 49). Each spec's parent-facing text was read around every mention, then
  widened by `grep` for the parents' interface tokens (`template-size-limits`, `CODEX_MAX`,
  `budgets.`, `surface-classes`, `write_row_order`, `.governance/`, each owned key's name). No
  dOrderedCharter spec spells `policy.py`, `catalogue.toml`, `unsummarised-keys.txt`,
  `read_policy_value` or `budgets.py`.
- dSafePassage side: specs 1, 5, 6, 8, 9, 10, 11 and 13 at their 2026-10-24 revisions, each §9 rev
  line read first; spec 35 for its title only.
- dGroundRules side: specs 1 to 4, 6, 8 and 9 in §2 and §4; 5 and 21 where they touch a key's
  default or the mirror.
- Aliases: `ocN:L` is line L of dOrderedCharter's `spec/2026-10-2?-spec-PLAY-dOrderedCharter-N.md`;
  `spN:L` of `../../dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-N.md`; `grN:L` of
  `../../dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-N.md`; `v2:L` of
  `../../dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md`; `gk:L` of
  `tools/govkit/govkit.py` at the base.
- What it does not check: anything either parent's build run decides after `5e2007467`; parent units
  promoted from audits beyond those named; whether dOrderedCharter's own specs agree with each other,
  except where a parent fact makes two of them disagree (rows 10 and 11).

## Summary table

| # | Spec | Assumption about the parent | Verdict | Evidence |
|---|---|---|---|---|
| 1 | oc31 | an `[[upgrade]]` row in the playbook descriptor: `id`, argv `up`/`down`/`witness` with `{gov}` and `{target}`, `surfaces`, `needs-target` | AGREES | oc31:146-152; sp1:193-197 |
| 2 | oc31 | a `[[retired]]` row carries an entry id to a live entry, `agent-instructions` to `playbook-render` | AGREES | oc31:135-138; sp1:57-61, :201-204; `tools/govkit/registry.toml:66` |
| 3 | oc31 | a `[[retired]]` row may hold a step-shaped id no step ever declared, `playbook/seeded-template` | UNKNOWN UNTIL BUILT | oc31:140-143, :330-337; sp1:201-204 states no rule either way |
| 4 | oc31 | the before-image helpers live in `tools/govkit/upgrade_steps.py`, imported by file path, and a down refuses a third state | AGREES | oc31:174-189; sp1:240-247 |
| 5 | oc31 | `update` carries a claimed retired kit to its successor (AC3) | AGREES | oc31:281-285; sp1:66-70 |
| 6 | oc31 | `upgrade_steps.py list` prints a succession row with its successor (AC3) | UNKNOWN UNTIL BUILT | oc31:281-282; sp1:64, :361, :371-373 name step rows only |
| 7 | oc31 | a class row is `id`, `reader`, `plant`, `summary`, each a `<path>:<function>` under the tool root | AGREES | oc31:155-165; sp10:31-36, :97-108 |
| 8 | oc31 | the gate takes `--base`, `--list`, `--fixture --plant <class>` and `--with-row` | AGREES | oc31:272-275; sp10:53-56, :138-141 |
| 9 | oc31 | `entry:agent-instructions` is a member of a parent class | AGREES | oc31:137; sp10:123 |
| 10 | oc31 | the `module-export` class holds the re-exports for `install.deprecation-window`, and no `[[shim]]` row is written | MISMATCH | oc31:59-63, :338-345; sp6:63-68, :89-91 |
| 11 | oc19 | the re-export rides "dSafePassage's shim" for the window | MISMATCH | oc19:99-100, :159; sp6:89-91; oc31:338-345 |
| 12 | oc31 | an edited seeded copy gov stops shipping reads `retired-edited` with one order (AC9) | MISMATCH | oc31:304-308; sp9:41-45, :127-128; gk:9988-9990 |
| 13 | oc31 | `install.retired-edits` keeps an edited retired file and never deletes it | AGREES | oc31:83-85; sp9:54-58 |
| 14 | oc31 | gov first: steps run on gov's tree in the lander's prepared merge and land in the source receipt's `steps` | AGREES | oc31:96-98, :311-314; sp8:33-52, :72-79 |
| 15 | oc31 | `help/upgrade-steps.md` is the parent's page | AGREES | oc31:99-100; sp1:136-139 |
| 16 | oc31 | the parent's legs are `step-gate`, `step-rows-frozen` and `upgrade walk` | MISMATCH | oc31:323-325; sp5:70 |
| 17 | oc33 | a `unit` class row's `witness` reads change records as the class's own-record witness | AGREES | oc33:65-69, :151-162; sp10:45-46, :102 |
| 18 | oc33, oc35 | orders go through `write_row_order(outbox, "unit", <repository tag>, <target revision>, <body>)` | MISMATCH | oc33:73-78, :148-149, oc35:182-183; sp9:143-147; gk:10760 |
| 19 | oc37 | the docs leg is `tools/govkit/docs_leg.py`, anchors `<!-- usage: <id> <fp8> -->` and computes the fingerprint | AGREES | oc37:45-56; sp13:52-58 |
| 20 | oc37 | a policy key's usage shape is `key`, read from its catalogue row | AGREES | oc37:61-63; sp13:45-51 |
| 21 | oc37 | the drive rows and the kinds register each gain a `[[class]]` row in `tools/govkit/usage.toml` | MISMATCH | oc37:61-64; sp13:40-44, :85-90 |
| 22 | oc37 | `build_target` builds the scratch adopter the tutorial runs in | AGREES | oc37:70-72; sp5:81-84 |
| 23 | oc37 | today's hand-written pages stay anchored by the parent's S11 | AGREES | oc37:85; sp13:99-105 |
| 24 | oc30 | the interpreter-floor rule pairs with `python resolver (…)`, whose floor arms the parent lands | AGREES | oc30:75, :122; sp11:504-511 |
| 25 | oc49 | the parent's unit 35 is a precedent batch of a review's minors | AGREES | oc49:676; sp35:1 |
| 26 | oc33, oc34, oc35, oc37 | the parent is built before this build's build run | AGREES | oc33:283, oc34:347; v2:1767 |
| 27 | oc2, oc7, oc11, oc15, oc20, oc25, oc26, oc33, oc35 | the one reader returns a key's file value, else its catalogue default with a reason | AGREES | oc2:58-59, oc7:104-106; gr2:60-64, gr3:32-35 |
| 28 | the same | until the reader lands, the unit reads the catalogue default | AGREES | oc25:54-56; gr1:39-41; v2:1767: the reader lands first, so the branch never runs |
| 29 | oc1 | an unset `charter.practices` reads its catalogue default, the `foundation` set | MISMATCH | oc1:59-63, :114; gr1:122, gr21:123-126; v2:1143 |
| 30 | oc1 | a `charter.practices` value is a set of practice tags the value check admits | UNKNOWN UNTIL BUILT | oc1:59-61; gr1:69-71, :145 |
| 31 | oc4 | the map's preset line: "each key reads its file value, else its catalogue default" | MISMATCH | oc4:90, :106-109; gr4:47-55, gr21:123-126 |
| 32 | oc9 | `render_unit(unit, policy_reader)` renders a `policy:<key>` unit from the reader's value | UNKNOWN UNTIL BUILT | oc9:70-73, :100; gr2:60-64, gr1:105-106 |
| 33 | oc11 | caps are `tools/template-size-limits.txt` rows read by `check-template-size.sh`'s key derivation, until `budgets.*` lands | MISMATCH | oc11:52-55, :218-221; gr9:46-58, :69-73; sp1:110-114 |
| 34 | oc11 | `budgets.enforce` defaults to `warn` | AGREES | oc11:200-203; gr1:31-35 |
| 35 | oc11, oc34 | Codex's `CODEX_MAX` sits outside the switch, refused whatever `budgets.enforce` says | AGREES | oc11:57-59, oc34:49-52; gr9:79-82, :175 |
| 36 | oc34 | the charter's cap key is `budgets.agents-md` | MISMATCH | oc34:144, :148; gr9:138-140, :153; gr6:39-43 |
| 37 | oc6 | `template-size-limits.txt` carries `budgets.*` "until dGroundRules moves them", and S7 adds a sentence to its header | MISMATCH | oc6:66-73; gr9:94-96; sp1:94-114 |
| 38 | oc6 | a raise goes through the one write shape the minimal guard admits | AGREES | oc6:70-73; gr6:39-45 |
| 39 | oc2 | `AGENTS.md` is raised in the unit's commit under the limits file's four conditions | MISMATCH | oc2:96-99; gr6:39-45; sp1:110-114 |
| 40 | oc7, oc15 | the minimal guard's TTY proof is one implementation a command calls, on its standard input | MISMATCH | oc15:71-73, :315, oc7:99-100, :143; gr6:46-48, :161-170, :360-367 |
| 41 | oc15, oc32, oc34 | the minimal guard refuses an agent's write to `.governance/instructions.toml` | AGREES | oc15:69-70, oc32:98, :232; gr6:22-26, :31-32 |
| 42 | oc31, oc32, oc49 | a step run by `update` in the prepared merge writes guarded files without the guard firing | AGREES | oc31:192-196, oc32:317-322, oc49:636-640; gr6:105-107; sp8:260-265 |
| 43 | oc32 | the one reader is extended in place to load the overlay's `[[policy]]` rows after the catalogue | MISMATCH | oc32:69-75, :176-178, :215; gr1:105-106, :171; gr2:28-37; gr4:30-34 |
| 44 | oc46 | the reader reads the same revision as `read_overlay`, `HEAD` | MISMATCH | oc46:37-40, :79-82, :100-103; gr2:28-33, :60-64 |
| 45 | oc35 | the unit lands `instructions.exclude`'s catalogue row with a summary and a usage | MISMATCH | oc35:57-59, :220-222, :302-305; gr1:39-41, :50-56; v2:1245 |
| 46 | oc19 | the three `tags.*` keys are new catalogue rows the unit lands | MISMATCH | oc19:85-91; gr1:39-41; v2:1349-1352 |
| 47 | oc27 | `memory.code-budget` joins the catalogue later | MISMATCH | oc27:35-38; gr1:39-41; v2:1365 |
| 48 | oc14 | `memory.load-budget` waits for both parents, held meanwhile as `LOAD_BUDGET_DEFAULT = 8192` | MISMATCH | oc14:94-96; gr1:39-41, gr3:32-35 |
| 49 | oc36 | the tag-valued keys' values are encoded so the check can read them | UNKNOWN UNTIL BUILT | oc36:92; gr1:139-160, :69-71 |
| 50 | oc37, oc49 | the policy catalogue renders a reference page, and a row with no `summary` or `usage` refuses the render | MISMATCH | oc37:45-50, oc49:44-48; gr1:50-56, :73-75 |
| 51 | oc37 | the policy schema's reader is the parent's own, loaded by path | MISMATCH | oc37:113-116; gr1:105-106, :171 |
| 52 | oc2, oc7, oc20, oc25, oc26 | each key's literal default is v2's | AGREES | oc20:91-92, oc26:61-62; v2:1144-1145, :1351, :1353-1354, :1359 |

## The mismatches, both sides quoted

- **Rows 10 and 11.** oc31:62-63 holds the names "how long they stay is unit 19's hold under
  `install.deprecation-window`", and oc31:338-345 rejects a `[[shim]]` row because a `module` forwarder
  replaces the whole file. oc19:159 still consumes "dSafePassage's shim". sp6:63-68 counts the window
  per `[[shim]]` row only, and sp6:89-91 expects one: "The first rows are the later builds' that move a
  surface, among them dOrderedCharter's `map_lib` re-export". So no mechanism holds the re-export for
  the window, and the two specs contradict each other. Change: either a `[[shim]]` kind for a partial
  re-export, which is the parent's call, or oc31 states its own hold rule and oc19's edge drops the shim.
- **Row 12.** oc31:304-308 expects an edited seeded copy to read `retired-edited` with one order.
  sp9:127-128 sends "both a first-time engine row and a row already carrying the role" to the new
  arm, and names no seed row. At the base the seed override rewrites a differing seed to
  `reseed-available` (gk:9988-9990), which sp9 leaves in place. Change: sp9's arm takes seed rows,
  which is a re-ground ask of dSafePassage, or oc31 states the verdict a seed row actually gets.
- **Row 16.** oc31:323-324 names "`upgrade walk`"; sp5:70 lands the leg as `upgrade-walk`. Change:
  the spelling.
- **Row 18.** oc33:148-149 calls `write_row_order(outbox, "unit", <repository tag>, <target revision>,
  <body>)`. sp9:143-147 types `row` as a receipt row, with `kind` `retired-edited` or `render-edited`,
  and today's writer keys the file on `render_order_slug(row['path'])` (gk:10760). A tag string has
  no `path`. `run_unit_drift` lives in `tools/playbook/pins.py`, which cannot import `govkit.py`
  (gr1:105-106). Change: pass a mapping that carries `path`, or ask the parent for a key argument,
  and put the call where govkit's writer is reachable.
- **Row 21.** oc37:61-64 gives the drive rows and the kinds register `[[class]]` rows in
  `usage.toml`. sp13:40-44 allows "One `[[class]]` row per class of TOOL-dSafePassage-10's class
  registry", and sp13:88-90 makes "a `[[class]]` row naming no registered class" a finding. Only oc33
  registers its class (`unit`). Change: each registry also lands a `surface-classes.toml` row with a
  reader and a plant (sp10:31-36), or its members go in as `[[usage]]` rows.
- **Row 29.** oc1:61-63 reads `charter.practices` "with the catalogue default v2 states, the
  `foundation` set". v2:1143's default is not a literal, so gr1:122 writes `{ derived = ... }`, and
  gr21:123-126 resolves such a row "to a `Refusal` naming the row ... 'a derived default no reader
  computes yet'". The mirror omits the key. Change: on that refusal oc1 computes the `foundation` set
  itself and says so; whether the reader gains a hook for it is the owner's call.
- **Row 31.** oc4:90 prints "each key reads its file value, else its catalogue default". gr4:47-55
  adds a `last-valid` source for an invalid file, and gr21:123-126 a refusal for a derived default.
  Change: drop the restated order and point at `policy.py get --explain`, which prints the source.
- **Row 33.** oc11:52-55 measures against "the `tools/template-size-limits.txt` row for the charter
  and each Skill", read "through the same key derivation `check-template-size.sh` uses" (oc11:218-221).
  gr9:69-73: the two readers "stop parsing it: `budgets.py` is its one reader". sp1:110-114 then
  removes the file from gov. Change: one `budgets.py resolve <cap>` call per load point, run as a
  subprocess, with caps named as the census names them (gr9:37-45).
- **Row 36.** oc34:144 prints `(budgets.agents-md)`. gr9:138-140: a cap is a `[budgets]` key "quoted
  where it carries a `/`, `.` or `*`: `"AGENTS.md" = 20480`", and gr6:39-43 admits a raise only when
  the key's last segment is a tracked file's path. Change: `budgets."AGENTS.md"`.
- **Row 37.** oc6:66-69 calls the limits rows "the carriers of `budgets.*` until dGroundRules moves
  them", and oc6:70-73 adds a sentence to that file's header. gr9:94-96 says moving the rows is
  "dSafePassage's step", and sp1:110-114 deletes the file in dSafePassage unit 1's commit. Change: S6
  reads both caps through `budgets.py resolve`. S7's sentence goes where the four raise conditions
  now live, above `[budgets]` in `.governance/policy.toml` (sp1:96-99), which is a guarded path, so the
  owner writes it or the sentence moves to `help/`.
- **Row 39.** oc2:96-99 raises `AGENTS.md` "under `tools/template-size-limits.txt`'s four conditions".
  The file is gone (sp1:110-114). gr6:39-45 admits one agent shape: one `budgets` leaf raised, a
  `RAISED <old> -> <new>` comment above it, and a `memory/DECISIONS.md` row. Change: that shape on
  `budgets."AGENTS.md"`.
- **Row 40.** oc15:71-73 makes `tty-cli` "an interactive terminal on the command's standard input,
  called through that guard's one implementation", and oc7:99-100 reuses it. gr6:46-48 tests
  "stderr being a terminal", and gr6:161-170 places that test, `[ -t 2 ]`, inline in
  `.githooks/pre-commit`. Python cannot call it, and it tests a different stream. Change: either the
  build run asks the parent to extract the test into a callable in `tools/policy/`, or dOrderedCharter
  writes its own proof and states it is a second one; in both cases it picks one stream.
- **Row 43.** oc32:176-178: "after loading the catalogue, the reader loads `read_overlay(root).policies`
  and adds each as a row". `read_overlay` is the playbook kit's, and gr1:105-106 says "A kit may not
  import a sibling kit". `load_catalogue(kit)` (gr1:171) reads the kit's own file, with no repo and no
  revision. The reader reads one revision's blobs (gr2:28-37), and `validate` refuses "one per leaf no
  catalogue row names" (gr4:30-34), so the whole file falls back to its last valid revision
  (gr4:47-55). The mirror iterates the catalogue only (gr8:105-106). Change: an overlay-policies read
  inside `tools/policy/`, on the same revision's blob, seen by `validate`, `arm_schema` and the mirror.
- **Row 44.** oc46:37-40 fixes the overlay's revision at `HEAD`, and oc46:100-103 says "dGroundRules'
  reader ... names the same revision". gr2:28-33 lands it as `refs/remotes/<remote>/<branch>`, else
  the local branch; `HEAD` is read only with `--rev` (gr2:60-64). oc46:81-82 says "dGroundRules has no
  spec yet", which is stale. Change: the two must read one revision: either the overlay reads the
  landed ref, or oc32's extension passes `--rev HEAD` and says why.
- **Rows 45 and 46.** oc35:220-222 puts "The catalogue row for `instructions.exclude`" into the
  catalogue, and oc19:89-91 treats the `tags.*` keys as new. gr1:39-41 already lands "one `[[key]]` table
  per row of v2's `[policies]` table", owners equal to v2's, so these rows exist with owner
  dOrderedCharter (v2:1245, :1349-1352) and no summary or usage (gr1:50-56). oc35:305's red, "which
  `cl-dClosedLoop-0007`'s schema refuses", is wrong: the shrink-only list admits the row. Change: fill
  `summary` and `usage` on each landed row and drain it with `policy.py lists --write` in the same
  commit, as dSafePassage specs 6, 9, 11 and 13 now do.
- **Rows 47 and 48.** oc27:35-38 waits "once that key is in the catalogue", and oc14:94-96 holds
  `LOAD_BUDGET_DEFAULT = 8192` until both parents land. gr1:39-41 puts every v2 row in the catalogue at
  dGroundRules, so `policy.py get` returns `16k` and `8k` (pattern strings) from then on (gr3:32-35).
  Change: read the key, convert `k`, and drop the constant, a second spelling of the default.
- **Row 50.** oc37:49-50: "A row with no `summary` or no `usage` refuses the render", and oc49:44-48
  keeps that refusal for a mapped field. gr1:73-75: "Today's keys sit on the shrink-only list; only
  the four keys of S1 carry a summary and a usage". The policy page's first render refuses. Change:
  render summarised rows and list the rest as undocumented, or defer the policy page.
- **Row 51.** oc37:113-116 loads "the parents' own readers" by path. For the policy schema, that loads
  `tools/policy/policy.py` from the playbook kit, which gr1:105-106 rules out. Change: read
  `tools/policy/catalogue.toml` with `tomllib`, as sp10's rev-3 does for its `policy` class.

## Parent surfaces dOrderedCharter does not name

- **U1.** dSafePassage unit 1 deletes `tools/template-size-limits.txt` from gov in its own commit
  and moves every row under `budgets.*` (sp1:94-123). Specs 2, 3, 6, 11, 31 (its Readers list), 49,
  50 and 55 still read, edit or measure against the file (oc3:73, oc49:147, oc50:49 and :115,
  oc55:192), and none of them names that unit for it. Rows 33, 37 and 39 are three instances.
- **U2.** dGroundRules' cap census `tools/policy/caps.toml`, joined both ways by `arm_cap_census`
  (gr9:37-45, :85-88). Its `codex-instructions` row names `agent-instructions/adopt-agent-instructions.sh`
  as enforcer and `CODEX_MAX` as home (gr9:175). oc31 moves the constant and deletes the kit, so the
  row goes stale in that commit; specs 6, 11 and 34 read the constant there.
- **U3.** `tools/policy/unsummarised-keys.txt`, shrink-only, drained by `policy.py lists --write` and
  graded both ways by `--check` (gr1:50-56). All 16 dOrderedCharter-owned keys land on it. Specs 19
  and 35 mention a summary, and none names the list or the verb.
- **U4.** The reader-coverage arm (gr8:26-28, :94-95). Once every dOrderedCharter spec is terminal,
  each of the 16 keys needs a reader in a scanned shape: a `.py` or `.js` call with the key literal
  first, or `policy.py get <key>` in shell. `.toml` is not scanned, so oc9's `policy:<key>` unit
  reads nothing for it. No spec spells the call.
- **U5.** `read_policy_value` lives once in `govkit.py` and is reached by govkit modules
  (sp9:154-158). dOrderedCharter's readers sit in `tools/playbook/` and `tools/roles/`, which cannot
  import govkit, so each needs `policy.py get` as a subprocess through the inlined `resolve_kit_dir`
  (`tools/playbook/render_playbook.py:78-79`). A second helper there owes a parity row.
- **U6.** The minimal guard covers `.governance/deploy.toml` (gr6:22-26, :31-32). oc30's pass edits
  that file's `:28` comment (oc30:60-64, :171), which an agent commit cannot land. oc32 routes its own
  edit of that file through the step (oc32:317-322); oc30 does not.
- **U7.** `step-rows-frozen` freezes every byte of a program a landed argv names (sp1:126-131). oc31
  puts the `charter-key` class reader and plant in the step program (oc31:155-158), and oc49 adds a
  `census` verb to it (oc49:77-79, :343). Any later edit to the reader reds the leg, and so does
  oc49's edit if it lands after oc31's.
- **U8.** The docs leg anchors each member on exactly one page, and a member anchored while still on
  `memory/project/docs-undocumented.txt` is a finding (sp13:52-58, :68-75). oc37's rendered policy page
  anchors every catalogue key, including the five that dSafePassage's own pages already anchor
  (sp13:99-105), and names neither rule.
- **U9.** A registered class whose population is empty exits 2 (sp10:47-49, sp13:85-87). oc31's
  `module-export` empties when the last re-export goes, so that commit must also remove the class row.

## For the build run's re-ground

- [spec 1](../spec/2026-10-23-spec-PLAY-dOrderedCharter-1.md): rows 29 and 30, U3 and U4. The
  derived default refuses, and the value check's handling of practice tags is unknown.
- [spec 2](../spec/2026-10-23-spec-PLAY-dOrderedCharter-2.md): row 39, U1, U3 and U4.
- [spec 3](../spec/2026-10-23-spec-PLAY-dOrderedCharter-3.md): U1, S7's limits row.
- [spec 4](../spec/2026-10-23-spec-PLAY-dOrderedCharter-4.md): row 31.
- [spec 6](../spec/2026-10-23-spec-PLAY-dOrderedCharter-6.md): row 37, U1 and U2.
- [spec 7](../spec/2026-10-23-spec-PLAY-dOrderedCharter-7.md): row 40, U3 and U4.
- [spec 9](../spec/2026-10-23-spec-PLAY-dOrderedCharter-9.md): row 32 and U4.
- [spec 11](../spec/2026-10-23-spec-PLAY-dOrderedCharter-11.md): row 33, U1 to U4.
- [spec 14](../spec/2026-10-23-spec-PLAY-dOrderedCharter-14.md): row 48.
- [spec 15](../spec/2026-10-23-spec-PLAY-dOrderedCharter-15.md): row 40, U3 and U4.
- [spec 19](../spec/2026-10-23-spec-PLAY-dOrderedCharter-19.md): rows 11 and 46, U3 and U4.
- [spec 20](../spec/2026-10-23-spec-PLAY-dOrderedCharter-20.md),
  [25](../spec/2026-10-23-spec-PLAY-dOrderedCharter-25.md) and
  [26](../spec/2026-10-23-spec-PLAY-dOrderedCharter-26.md): U3 and U4.
- [spec 27](../spec/2026-10-23-spec-PLAY-dOrderedCharter-27.md): row 47.
- [spec 30](../spec/2026-10-23-spec-PLAY-dOrderedCharter-30.md): U6.
- [spec 31](../spec/2026-10-23-spec-PLAY-dOrderedCharter-31.md): rows 3, 6, 10, 12 and 16, U1,
  U2, U7 and U9.
- [spec 32](../spec/2026-10-23-spec-PLAY-dOrderedCharter-32.md): row 43 and U5.
- [spec 33](../spec/2026-10-23-spec-PLAY-dOrderedCharter-33.md): row 18, U3, U4 and U5.
- [spec 34](../spec/2026-10-23-spec-PLAY-dOrderedCharter-34.md): row 36 and U2.
- [spec 35](../spec/2026-10-23-spec-PLAY-dOrderedCharter-35.md): rows 18 and 45, U3 and U4.
- [spec 36](../spec/2026-10-23-spec-PLAY-dOrderedCharter-36.md): row 49.
- [spec 37](../spec/2026-10-23-spec-PLAY-dOrderedCharter-37.md): rows 21, 50 and 51, and U8.
- [spec 46](../spec/2026-10-24-spec-PLAY-dOrderedCharter-46.md): row 44.
- [spec 49](../spec/2026-10-24-spec-PLAY-dOrderedCharter-49.md): row 50, U1 and U7.
- [spec 50](../spec/2026-10-24-spec-PLAY-dOrderedCharter-50.md) and
  [55](../spec/2026-10-24-spec-PLAY-dOrderedCharter-55.md): U1.

Three items need a parent decision, not only a dOrderedCharter edit: row 12 (dSafePassage's unit 9
arm and seed rows), rows 10 and 11 (a `[[shim]]` for a partial re-export), and row 40 (a callable TTY
proof). Specs 30's floor pairing and 37's docs-leg anchors agree as written.
