**Serves:** journal TOOL-dSafePassage-13

# TOOL-dSafePassage-13 — acceptance ledger

The unit as built, at spec rev-6. The leg is `tools/govkit/docs_leg.py`: `read_usage_classes` joins
the `[[class]]` rows of the new `tools/govkit/usage.toml` to the step gate's registry
(`read_surface_classes`), `read_usage_rows` takes each class's rows from its `rows` reader
(`read_hook_usage`, `read_policy_usage`, `read_verb_usage` over `VERB_SOURCES`, `read_leg_usage`,
loaded by path through the step gate's `load_class_callable`) and the `[[usage]]` rows, and
`read_docs_state` grades the anchors (`read_page_anchors`, `derive_usage_fingerprint`), the page
commands (`read_page_commands`, `check_page_command`), the links (`check_page_links`) and the
shrink-only list (`read_legacy_rows`, `check_legacy_low_water` over drift-audit's
`derive_low_waters`). `help.enforce` is read once, `gk.read_policy_value("help.enforce", root)`.
`usage.toml` holds the nine classes, the `command:build` row and 28 `script:` rows; the pages under
`help/` carry 39 anchors; `memory/project/docs-undocumented.txt` is seeded with 370 rows from
`--list --undocumented`. The leg row `docs` and its meta-gate rows, the `SHRINK_ONLY` row, the
catalogue row's `summary` and `usage` (drained by `lists --write`), `help/docs-leg.md` and its index
line, and 21 `[dSafePassage-13]` selftest rows are in the pass; the mirror follows in its own commit.

HOW EACH CRITERION WAS OBSERVED. No gate, suite or bar ran in this pass. Each AC was observed on
node d (Windows, Python 3.15) by the leg's own CLI over its fixture or the tree, or a `git grep`.

- AC1 — `--fixture --plant stale-page` exit 1: `docs: STALE help/guide.md:11 fx-verb:tool: the page holds ef26be5a, the row is now af2f8078`; `--plant none` exit 0. Red when, observed: the comparison patched to the page's own fingerprint (`now := fp`) made `stale-page` exit 0; restored from the index.
- AC2 — `python tools/govkit/docs_leg.py` on the tree exit 0: `commands 54 tested, 6 skipped, 0 unrowed`, `0 stale`, `links 19 checked`; `help/roles.md` and `help/measure-legs.md` each carry tested commands (handoff.py render and roster, render_agents.py, adopt-playbook.sh; measure_legs.py and derive-ceilings.py). The scratch-clone respelling is recorded in the line below, after the pass commit.
- AC3 — `--plant bad-flag` exit 1 naming `flag '--section'`; `--plant bad-verb` exit 1 naming `verb 'rendr'`; `--plant unrowed` exit 1 naming `tools/fx/other.py`; the base prints `commands 2 tested, 1 skipped`, the `sort` line skipped.
- AC4 — `--plant broken-link` exit 1 `docs: LINK help/guide.md:13 gone.md`; `--plant broken-fragment` exit 1 naming `#no-such-heading`; `--plant external-link` exit 0 with `links 2 checked, 1 external`. Red when, observed: the fence skip of `check_page_links` patched away made the base exit 1 on the fenced `absent.md` link of `help/more.md`; restored.
- AC5 — `--plant undocumented` exit 1 naming `fx-page:guide`; `--plant drained-row` exit 1 `DRAINED ... row fx-page:guide`; `--plant grown-list` exit 1 `2 rows, above its low-water 1`; `--plant orphan-anchor` exit 1 naming `fx-key:NOPE`. Red when, observed: the low-water comparison patched to `if False:` made `grown-list` exit 0; restored.
- AC6 — `--plant restated-row` exit 1 `RESTATED fx-hook:fx-hook`; `--plant leg-row` exit 1 `STALE help/more.md:6 fx-leg:fx-leg`; `--plant reader-rows` exit 1 `STALE help/more.md:5 fx-mod:thing`.
- AC7 — `--plant unclassed` exit 1 `CLASS fx-extra: a registered class with no [[class]] row`; `--plant empty-class` exit 2 `REFUSED · class fx-key has usage key and no member`; `--plant untested` exit 2 `no page command was tested`; `--plant none-rows` exit 1 naming `fx-none`.
- AC8 — `--plant stale-page --enforce warn` exit 0 with `docs: WARN STALE help/guide.md:11 ...`; `--enforce off` exit 0 printing the one line `docs: help.enforce = off · --enforce`. On the tree the first line is `docs: help.enforce = refuse · default · not set in .governance/policy.toml at 2bd5e10d, origin/main, the landed revision; the catalogue default`; `--list` prints `docs: policy:help.enforce · key · default refuse · values refuse warn off · help/docs-leg.md:59`; `git grep -n -e "^help.enforce$" -- tools/policy/unsummarised-keys.txt` found no line (exit 1); `git grep -n -F 'read_policy_value("help.enforce"' -- tools/govkit/docs_leg.py` found the one read, line 681. `python tools/policy/check_policy.py` is the `policy check` leg's engine and was not run here: owed at the close.
- AC9 — `git grep -n -e "help.enforce" -e "docs_leg" -- help/` finds `help/docs-leg.md` and its `help/README.md` line; AC2's run grades that page green, its two anchors current.
- AC10 — the `git grep` over the five files finds `docs` in each (`tools/gate-legs.json:1463`, `registry.toml:715`, `subject-pins.tsv:36`, `ceiling-evidence.txt:49`, `govkit.md:12`); `drift_signals.py:138` holds the `SHRINK_ONLY` row.
- AC11 — `git grep -n -e "Departs from" -- memory/builds/dSafePassage/build/` lists deviation-51 and deviation-52 of this unit, each departing from `cl-dClosedLoop-0030@274077d4`.

The fixture cases of the new selftest arm were run by a probe that executes that arm's own case
list against the CLI: 21 of 21 held.

OWED AT THE CLOSE: the bar's legs section 7 names; `python tools/policy/check_policy.py` (AC8) and the
`policy check` leg over the mirror; and the two New arms' RED-first observations, the `docs` leg red
on a respelled `help/roles.md` flag and the `[dSafePassage-13]` rows of `tools/govkit/selftest.py`
red on a staged break, green restored.
