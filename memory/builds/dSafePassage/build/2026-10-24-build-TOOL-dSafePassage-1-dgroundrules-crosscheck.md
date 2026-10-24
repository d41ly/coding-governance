**Serves:** research TOOL-dSafePassage-1

# dSafePassage's specs against dGroundRules' landed specs: a read-only cross-check

Node d, 2026-10-24, base `ed497191d` (origin/main). dSafePassage's spec run landed at `f3a36b576`,
nine hours before dGroundRules' spec run (`d8070f748`), so its 11 specs that name dGroundRules wrote
its interfaces from the design alone. This record compares each assumption with what dGroundRules'
landed specs, every one DEFERRED, actually specify. It is not an audit: no spec was edited, no review
harness ran, and the verdicts feed the build run's re-ground step
([execution plan](../../dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-execution-plan.md), `[phase-2]`).

**Counts:** 42 assumptions · 19 AGREES · 20 MISMATCH · 3 UNKNOWN UNTIL BUILT · plus 8 dGroundRules
surfaces dSafePassage relies on without naming them.

## Method

- Population: `grep -l dGroundRules memory/builds/dSafePassage/spec/*.md` gives 11 specs (1, 2, 4 to 11,
  13); no other spec cites a `TOOL-dGroundRules-<n>` id. Each spec's interface tokens were then listed
  with `grep -oE 'read_policy_key|\.governance/[^ ]+|cl-dClosedLoop-00[0-9]+|...'`.
- dGroundRules side: specs 1 to 7, 9 and 10 read whole in §1 to §4; 8, 15, 17, 19 and 21 read
  where they touch a path or key dSafePassage reads; the BACKLOG ask rows; v2's `[policies]` table
  for the owner cells.
- Aliases: `spN:L` is line L of dSafePassage's `spec/2026-10-23-spec-TOOL-dSafePassage-N.md`;
  `grN:L` is line L of `../../dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-N.md`; `GRB:L` is
  line L of `../../dGroundRules/BACKLOG.md`; `v2:L` is the architecture record
  `../../dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md`.
- What it does not check: anything dGroundRules' build run decides after base `ed497191d`, the
  dGroundRules units promoted from its audits beyond those named above, and whether dSafePassage's
  own specs agree with each other.

## Summary table

| # | Spec | Assumption about dGroundRules | Verdict | Evidence |
|---|---|---|---|---|
| 1 | sp1 | the policy file is `.governance/policy.toml`, a key is its dotted TOML path (`agents-in-flight = 2` under `[runtime]`) | AGREES | sp1:146, sp1:385-388; gr1:31-35 |
| 2 | sp1 | `runtime.agents-in-flight` defaults to 6 | AGREES | sp1:389; gr1:311-312 |
| 3 | sp1 | the TOML reader is `read_policy_key` (S6 value read, S7 per-cap check, the render's read-back, AC10) | MISMATCH | sp1:147, :242, :248, :255, :386; gr2:19-24, :65-67, :250-253 |
| 4 | sp1 | the reader reads the step's target as it stands, before a commit | MISMATCH | sp1:246-251, :255, :385-388; gr2:34-37 |
| 5 | sp1 | the step writes through dGroundRules' writer where one lands, else its own `render_policy_text` | AGREES | sp1:253-256; gr2:83, gr5:73-74: no writer lands, so the fallback holds |
| 6 | sp1 | one legacy-home parser for `.agent-cap.conf` that the step program can call | MISMATCH | sp1:239-241; gr10:34-44, gr1:105 |
| 7 | sp1 | `FANOUT_CAP` only lowers the key, so the limit reads the same before and after | AGREES | sp1:72-75, :242-244, :519-523; gr10:34-44, gr15:34-38 |
| 8 | sp1 | `.agent-cap.conf`'s by-name readers are the seven S6 types, and dGroundRules re-points the code ones | MISMATCH | sp1:79-85; gr10:65, :94 |
| 9 | sp1 | S5's window population is dGroundRules' legacy-homes list, read through that list's reader | MISMATCH | sp1:68-71, :215, :224; gr7:29, :78-80, :122, gr17:37-43 |
| 10 | sp1 | each `template-size-limits.txt` row becomes `budgets.<row key>` | AGREES | sp1:86-90; gr9:42-44, :138-140 |
| 11 | sp1 | caps are read via `read_policy_key`, and the two size readers keep a legacy branch S8 deletes | MISMATCH | sp1:99-101, :107-108; gr9:46-58, :73-75, :133 |
| 12 | sp1 | the file's four raise conditions travel with the step | AGREES | sp1:88-90; gr9:94-96 |
| 13 | sp1 | the minimal guard admits S8's value-preserving write of gov's policy file | MISMATCH | sp1:495-509; gr6:39-45, :127; GRB:6, :20-21 |
| 14 | sp1 | the ask holds the id `TOOL-dGroundRules-13` | AGREES | sp1:504; GRB:6; gr14:170 |
| 15 | sp2 | the unit reads no policy key and calls no reader | AGREES | sp2:386-388 |
| 16 | sp4 | the same | AGREES | sp4:305-307 |
| 17 | sp5 | the `fanout-cap` plant's `policy` observation reads 2 through the reader in the target | MISMATCH | sp5:141-142, :153, :419-421; gr2:34-37, gr15:34-38 |
| 18 | sp5 | a policy reader runs in the release-0 fixture target | UNKNOWN UNTIL BUILT | sp5:153; gr1:76, :169 |
| 19 | sp6 | the unit adds catalogue rows for `install.deprecation-window` and `install.on-shim-call` | MISMATCH | sp6:63-65, :228-229; gr1:39-41, :50-53, :308-314; v2:1404-1405 |
| 20 | sp6 | the `sh` forwarder reads its key with an inline `read_policy_key` | MISMATCH | sp6:138, :328-336; gr2:65-67, gr21:101-103 |
| 21 | sp6 | the `py` and `js` forwarders read `.governance/policy.json` with their stdlib | MISMATCH | sp6:139-141; gr5:44-49, :59-60, :68-69 |
| 22 | sp6 | the window value is read from gov's policy file via `read_policy_key` | MISMATCH | sp6:163-165; gr2:19-24, :65-67 |
| 23 | sp6 | a JSON mirror of the policy exists for non-TOML readers | AGREES | sp6:96; gr5:20-21 |
| 24 | sp6 | the catalogue file sits where the parent lands it | AGREES | sp6:228; gr1:23 (`tools/policy/catalogue.toml`) |
| 25 | sp7 | the unit reads no policy key and calls no reader | AGREES | sp7:334-336 |
| 26 | sp8 | gov's `.governance/deploy.toml` is under the minimal guard | AGREES | sp8:96-97, :237-238; gr6:23-24, :31 |
| 27 | sp8 | the guard judges the lander's step writes to gov's policy file, and its refusal refuses the landing | MISMATCH | sp8:114, :257-258, :329-331; gr6:105-107 |
| 28 | sp8 | the gov-first walk runs before the landing's regeneration, so the mirror renders the walked file | AGREES | sp8:69-72; gr5:38-40, :187-189 |
| 29 | sp9 | the unit adds a catalogue row for `install.retired-edits` | MISMATCH | sp9:62-65, :229-230; gr1:39-41, :308-314; v2:1406 |
| 30 | sp9 | the mode is read via `read_policy_key` over the target's policy | MISMATCH | sp9:120-123; gr2:65-67 |
| 31 | sp9 | the target carries a runnable reader of its own policy | UNKNOWN UNTIL BUILT | sp9:64-65; gr1:233-241 |
| 32 | sp10 | the `policy` class is every key the catalogue holds | AGREES | sp10:81, :118; gr1:39-41, :118-131 |
| 33 | sp10 | the catalogue is read through `read_policy_key` | MISMATCH | sp10:371-375; gr1:171 |
| 34 | sp10 | the catalogue can be read at a landing's base and at its tip | UNKNOWN UNTIL BUILT | sp10:81, :118; gr1:171 |
| 35 | sp11 | the unit adds a catalogue row for `platforms.provision` | MISMATCH | sp11:84-87; gr1:39-41, :308-314; v2:1403 |
| 36 | sp11 | the reader is `read_policy_key`, shell or Python | MISMATCH | sp11:51-53, :174-181; gr2:19-24, :60-67, gr5:50-53 |
| 37 | sp11 | the key is read at the landed revision (S4) and at `HEAD` (design) | MISMATCH | sp11:52, :174; gr2:60-64 |
| 38 | sp11 | an unset key reads the catalogue default with a reason | AGREES | sp11:52-53; gr3:32-35 |
| 39 | sp13 | the unit adds a catalogue row for `help.enforce` | MISMATCH | sp13:71-73; gr1:39-41, :308-314; v2:1294 |
| 40 | sp13 | a `key` row comes from the catalogue row's allowed values and default | AGREES | sp13:42-47, :167; gr1:118-131 |
| 41 | sp13 | `help.enforce` is read through the reader the reader clause lands | AGREES | sp13:73, :125; gr2:19-24, gr8:94-95 |
| 42 | sp13 | the catalogue file sits where the parent lands it | AGREES | sp13:306; gr1:23 |

## The mismatches, both sides quoted

- **Row 3.** sp1:147 cites "`read_policy_key` (`cl-dClosedLoop-0008`)" as the reader of the TOML
  file. gr2:19-24 builds the reader as `resolve(key, repo=".", rev=None)` and `policy.py get`, "while
  the shell parser and its three byte-identical copies stay as they are for the legacy homes"; gr2:65-67
  and AC8 (gr2:250-253) forbid `read_policy_key` a TOML parse. Change: every read in S6, S7, the
  witness and AC10 goes through `python <prefix>/policy/policy.py get <key> [--rev <rev>]`, or
  `resolve` reached as a subprocess, since gr1:105 forbids a kit importing a sibling kit.
- **Row 4.** sp1:248 checks each row "against the value `read_policy_key` reads for that cap", and
  sp1:255 has the render "refuse its own output unless `read_policy_key` reads the value back", both
  before any commit. gr2:34-37: "Nothing in the module opens the working-tree path"; the reader reads
  the landed revision or `--rev`. Change: the pre-write check and the read-back parse the text the step
  holds (the reader exposes `parse_policy(text)` at gr2:38-42, but only inside the policy kit), and the
  witness and AC10 read `--rev` at a commit the fixture makes.
- **Row 6.** sp1:239-241 parses `.agent-cap.conf` "through the legacy-home parser dGroundRules' reader
  uses for it". gr10:34-44 lands it as `read_legacy_fanout(repo, rev)` in `tools/policy/policy.py`,
  reading the file "at the same revision `resolve` reads", tolerating other lines, the last
  `FANOUT_CAP` line winning. Change: the step reads the target's file itself, or the conf at a
  committed revision; its stricter refusals (any other assignment) stay its own.
- **Row 8.** sp1:79-82 types seven by-name readers, `tools/hooks/agent-cap.js` and
  `check-verifier-fanout.sh` among them. gr10:65 retires `loadDeclaredCap` and `CAP_CONF` from
  agent-cap.js, and gr10:94 retires `--print-cap`; the file's new reader is `read_legacy_fanout` in
  `tools/policy/policy.py`, plus `help/agent-limit.md`. Change: re-derive the list with the spec's own
  `git grep` at the build run's base.
- **Row 9.** sp1:68-71 takes the window's population from "the legacy-homes list dGroundRules derives
  (`cl-dClosedLoop-0013`), read through that list's reader", and closes a member when a step's
  `surfaces` names it (`conf-key:.agent-cap.conf#FANOUT_CAP` at sp1:215,
  `file:{prefix}/template-size-limits.txt` at sp1:224). gr7:29 and gr7:122 land the list as
  `tools/policy/legacy-homes.txt`, rows `<home> <key> <mark>`; its homes are root kit confs,
  `.githooks/gate-env.sh` and the roles house file (gr7:78-80). `template-size-limits.txt` is no home on
  it, gov tracks no `.agent-cap.conf`, and gr17:37-43 withholds the list from every install. The
  list has no reader verb but `lists --write | --check`. Change: either state that neither step closes a
  member of this list and drop S5's tie to it, or define the join from a `surfaces` item to a
  `<home> <key>` row and read the gov-only file directly.
- **Row 11.** sp1:99-101 names "`read_policy_key` reading every `budgets.*` cap ... and through it
  `tools/check-template-size.sh` and `tools/check-spec-tokens.py`'s size join"; sp1:107 deletes "the
  legacy-home branch the two size readers keep for the file". gr9:46-58 reads caps through
  `tools/policy/budgets.py` (`resolve_caps`, `budgets.py resolve | check`), and gr9:73-75 makes the two
  size readers "stop parsing it: `budgets.py` is its one reader". Change: S7's per-cap check reads
  `budgets.py resolve`, and S8 retires `budgets.py`'s `limits:` home branch (gr9:133), rewriting
  `tools/policy/caps.toml`'s seven `limits:` homes (gr9:152-158), in place of a branch in the two
  size readers.
- **Row 13.** sp1:503-506 asks the guard to admit "the one step-write shape whose every `budgets.*`
  value reads unchanged through the reader". gr6:39-45 admits one shape only, a single cap raised, and
  refuses "a key was added" (gr6:127). The ask is filed and DEFERRED until dGroundRules' unit 6
  (GRB:6, :21), so the landed spec does not grant it yet. Change: none in sp1 until unit 6 is
  re-grounded; that re-ground has to name how the guard compares staged values, since the reader reads
  revisions and never the index (gr2:34-37), and that `tools/template-size-limits.txt` leaves in the
  same commit, or the two-homes rule refuses (U3).
- **Row 17.** sp5:153 expects `runtime.agents-in-flight` to read `2` after the walk. The reader reads a
  committed revision (gr2:34-37), and under gr15:34-38 a `FANOUT_CAP=2` conf lowers the key to 2
  whether or not the step ran. Change: commit the walked target and read with `--rev`, and pair the
  observation with `.agent-cap.conf` absent, or it grades nothing.
- **Rows 19, 29, 35 and 39.** sp6:63, sp9:62, sp11:84 and sp13:71 each add a catalogue row. gr1:39-41
  writes "one `[[key]]` table per row of v2's `[policies]` table", with AC2 (gr1:308-314) requiring
  the two name lists equal in order and each owner equal to v2's; v2 holds all five rows with Owner
  dSafePassage (v2:1294, :1403-1406). The rows land without `summary` or `usage` and sit on
  `tools/policy/unsummarised-keys.txt` (gr1:50-53, :74-75). Change: each unit fills `summary` and
  `usage` on the existing row and drains it with `policy.py lists --write` in the same commit (U5).
  A second row breaks AC2's order and count.
- **Row 20.** sp6:138 has the `sh` forwarder carry "the bash reader whose contract
  `cl-dClosedLoop-0008` extends, `read_policy_key`". gr2:65-67 keeps that parser `KEY=value`, which
  cannot read `[install] on-shim-call`; gr21:101-103 records its four copies as legacy-only. Change:
  the `sh` forwarder calls `policy.py get install.on-shim-call` under the resolved Python, or reads the
  mirror through `policy-mirror.js`, keeping the warn-on-failure prelude.
- **Row 21.** sp6:139-141 parses `.governance/policy.json` with `JSON.parse` and `json`. gr5:44-49 lands
  one mirror reader, `readPolicy` in `tools/policy/policy-mirror.js`, reading the landed blob and only
  while its blob ids match; gr5:59-60's `arm_mirror_readers` reds any tracked code outside
  `tools/policy/` that names the mirror; gr5:68-69 sends Python and shell to the reader. Change: `js`
  forwarders call `readPolicy`; `py` forwarders call `policy.py get`.
- **Row 22.** sp6:163-165 reads `install.deprecation-window` "through `read_policy_key`". Change:
  `policy.py get install.deprecation-window` at gov's landed revision, as gr2:60-64's `get` reads by
  default.
- **Row 27.** sp8:114 expects the guard to refuse the lander's step writes, and sp8:257-258 says "If
  dGroundRules' minimal guard refuses that write, gov first refuses the landing". gr6:105-107: "The
  lander never fires pre-commit: `--prepare` writes the merge with `commit-tree` ... and the attended
  path commits with `--no-verify`". The guard never sees a landing. Under sp1 F8 (a) the write happens
  in sp1's own unit commit, where the guard does fire (row 13). Change: drop the edge and the risk line,
  or point them at sp1's unit commit.
- **Row 30.** sp9:120-123 reads `install.retired-edits` "through the parent's reader,
  `read_policy_key`". Change: the target's `policy.py get install.retired-edits`, with the default
  `order` where the target has no policy kit (row 31).
- **Row 33.** sp10:371-372 reads the catalogue "through the reader whose contract
  `cl-dClosedLoop-0008` extends (`read_policy_key`)". The catalogue's loader is `load_catalogue(kit)`
  (gr1:171); `read_policy_key` reads no catalogue. Change: read `tools/policy/catalogue.toml`'s
  `[[key]]` names at each revision (row 34).
- **Row 36.** sp11:51 names `read_policy_key`, and sp11:174-178 branches on whether the landed reader is
  shell or Python. It is Python only (gr2:19-24, `get` at gr2:60-64), so the Python branch holds.
  gr5:50-53's `policy-shim.sh get` runs `resolve_python` itself, so the floor's refusal path must call
  `<candidate> <prefix>/policy/policy.py get platforms.provision` directly, never the shim. Change:
  name the Python call and say how the block locates the policy kit.
- **Row 37.** sp11:52 reads "at the landed revision" and sp11:174 "at `HEAD`". `get` reads the landed
  tip by default and `HEAD` only with `--rev HEAD` (gr2:60-64). Change: pick one and spell the flag.

## dGroundRules surfaces dSafePassage does not name

- **U1** — `arm_limits_readers` (gr9:86-88, made one row of `arm_single_reader` by gr21:153-156 and
  narrowed to real reads by gr21:185-188) reds any tracked script outside `tools/policy/` that reads
  `template-size-limits.txt`. sp1's `tools/govkit/steps/template_size_limits.py` does, so the
  `policy check` leg reds on it.
- **U2** — `tools/policy/caps.toml`'s seven `limits:` homes and `budgets.py`'s read of the file
  (gr9:42-58, :133, :152-158), joined both ways by `arm_cap_census`. sp1:104-110's S8 disposal list
  names neither.
- **U3** — The two-homes rule (gr9:60-63): a cap held in both the policy file and the limits file
  refuses at resolution. An up killed after writing `[budgets]` and before removing the file
  (sp1:228-235) leaves both, so the resumed up's per-cap check (sp1:247-249) reads a refusal.
- **U4** — The mirror. sp1's S8 write stales `.governance/policy.json`; `arm_mirror_parity` (gr5:41-43)
  and the preflight's `regen.py --check` (gr5:38-40) red the branch until a second commit stages the
  regenerated mirror, which the guard admits only when the policy file and catalogue equal HEAD
  (gr19:25-31, :35-40). No dSafePassage spec names the mirror's regeneration.
- **U5** — `tools/policy/unsummarised-keys.txt`, shrink-only, graded both ways by `lists --check`
  (gr1:50-53, :187-195). Filling a row's summary and usage without `lists --write` in that commit reds
  `arm_summaries` as stale.
- **U6** — The reader-coverage arm (gr8:26-34): once every dSafePassage spec is terminal, each of its
  five keys needs a reader in one of gr8:94-95's call shapes, a call with the key literal first, or
  `policy.py get <key>` in shell. A `read_policy_key` call or a JSON subscript matches neither.
- **U7** — `arm_mirror_readers` (gr5:59-60) reds sp6's forwarder templates if they name
  `policy.json` in tracked code outside `tools/policy/`.
- **U8** — `tools/policy/policy-shim.sh` carries the `resolve_python` block inline (gr5:50-53), so the
  parity population sp11:54-56 counts as 69 files grows by one, and sp11's S5 re-sync must include it.

## For the build run's re-ground

- [spec 1](../spec/2026-10-23-spec-TOOL-dSafePassage-1.md) — rows 3, 4, 6, 8, 9, 11 and 13, and U1 to
  U4: the reader is `policy.py get` or `budgets.py resolve` at a revision, the conf parser reads a
  revision, the window's population and join, S8's disposal of `budgets.py`'s `limits:` branch and
  `caps.toml`, the step program outside `arm_limits_readers`, and the mirror's second commit.
- [spec 5](../spec/2026-10-23-spec-TOOL-dSafePassage-5.md) — row 17 and row 18: the `policy`
  observation reads `--rev` at a committed walk, is paired with the conf absent, and needs a reader in
  the target.
- [spec 6](../spec/2026-10-23-spec-TOOL-dSafePassage-6.md) — rows 19 to 22, U5 to U7: fill the
  existing catalogue rows, and every forwarder reads through `policy.py get` or `readPolicy`.
- [spec 8](../spec/2026-10-23-spec-TOOL-dSafePassage-8.md) — row 27: the guard never fires at a
  landing.
- [spec 9](../spec/2026-10-23-spec-TOOL-dSafePassage-9.md) — rows 29 to 31, U5 and U6.
- [spec 10](../spec/2026-10-23-spec-TOOL-dSafePassage-10.md) — rows 33 and 34: the catalogue's loader,
  read at both revisions.
- [spec 11](../spec/2026-10-23-spec-TOOL-dSafePassage-11.md) — rows 35 to 37, U5, U6 and U8.
- [spec 13](../spec/2026-10-23-spec-TOOL-dSafePassage-13.md) — row 39, U5 and U6.

Specs 2, 4 and 7 bind nothing of dGroundRules and need no revision for it.
