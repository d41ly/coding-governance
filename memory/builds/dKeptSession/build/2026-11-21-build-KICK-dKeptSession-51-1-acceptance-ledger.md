# KICK-dKeptSession-51 — acceptance ledger

**Serves:** journal KICK-dKeptSession-51

No merge bar, no self-test suite and no gate leg ran in this pass, and the legs the spec's section 7
names were not run as commands. The criteria were observed on win32 at the pass's base `34dd4a35`,
each by the grep, `cmp` or index read the criterion itself states, run over the working tree before
the commit.

Before the first edit the spec's cited code was probed at the base. The comment block above
`tools/unattended/unattended.sh#derive_message_id` names the eight fields unit 31 landed and no act,
so S1 adds its sentence rather than observing one already there. The `--mail` entry of
`tools/unattended/VERBS.template.md` carries the id sentence ending "refused as a duplicate across
the build's session refs.", and the template and `memory/guides/UNATTENDED-VERBS.md` were byte
equal. `memory/builds/dWellOiledMachine/BACKLOG.md` held four asks, none naming `derive_message_id`
(PINNED, read at `34dd4a35`), and no id of that build's `TOOL` family above its ask
TOOL-dWellOiledMachine-130 was held by a roster unit or an ask, so the ask takes
TOOL-dWellOiledMachine-131; the two higher tokens the `ids:` line derives are example ids that unit
specs of that build spell. Units 22 and 31 were CLOSED at the base.

`python tools/lexicon/lexicon.py` exited 1 over the working tree on its verb-offender pin, 1432
offenders over a pin of 1421 (DERIVED, that run), the count unit 31's ledger read at its own base:
this change mints no function, so it adds none. `gen_map.py --write` left
`memory/map/generated/symbols.json` byte-identical, and `writing_practice.py check pinned-facts`
read green.

## Criteria

**Evidences:** KICK-dKeptSession-51
- AC1 — `grep -c -i seventh` — the definition's window, `grep -B3 '^derive_message_id()'` over the driver squeezed by `tr -s ' #\r\n' ' '`, piped into `grep -c 'the ninth field, after the recipient and the content key'` printed `1` and into `grep -c -i seventh` printed `0` (DERIVED, that probe).
- AC2 — `cmp tools/unattended/VERBS.template.md memory/guides/UNATTENDED-VERBS.md` — exited `0`; `tr -s ' \r\n' ' '` over the installed guide piped into `grep -o 'joins as the ninth field, after the recipient and the content key' | wc -l` printed `1`, and `grep -c "seventh field"` over it printed `0` (DERIVED, those probes).
- AC3 — `python tools/memory-tree/gen_build_index.py --asks --build dWellOiledMachine` — listed TOOL-dWellOiledMachine-131 `OPEN` at `HIGH` with no verdict; `grep -n "derive_message_id"` over the child's `BACKLOG.md` printed that one ask row and the `SEV` grep printed its `HIGH` row (DERIVED, that run).
- AC4 — `tr -s ' \r\n' ' '` — over this ledger, piped into `grep -c "a seventh field of S2"` and into `grep -c "joins S2 as a seventh field"`, printed `1` each, and `git diff --cached --name-only` from the pass base listed no spec or ledger of unit 22 or 31 (DERIVED, those probes).

Each line the edit adds to the driver opens `#` (DERIVED, the pass's diff), and a site is read with
its comments stripped, so S1 adds no refusal site; the census at the driver's ceiling (PINNED,
`.memory-tree.conf#REFUSAL_CEILINGS`, 347) is read at the close. The guide's sentence follows its id
sentence and the rest of the entry is re-wrapped to its width, the body bound's figure kept on one
line beside its pin. The child's README `ids:` line and `memory/backlog/TOOL.md` moved only as
`gen_build_index.py --write` rendered them.

## The sibling text superseded (S4)

`KICK-dKeptSession-22` and `KICK-dKeptSession-31` are CLOSED, so neither spec nor either ledger is
written here (F1). Unit 31's S4 superseded four six-field passages of unit 22's spec and left two
standing, which the ninth position supersedes from this unit's landing:

- unit 22's S4, "the act is a seventh field of S2, appended after `answers`": the act is the ninth
  field, after the recipient and the content key, which unit 31 placed after `answers`;
- unit 22's `hands-off external` edge to dWellOiledMachine, "whose act joins S2 as a seventh field":
  the child build's contract is now its ask TOOL-dWellOiledMachine-131, which states the ninth.

## Owed to the close

Every leg the spec's section 7 names: the unattended kit gate (its check 10 holding the guide pair
byte equal), the scratch-guard and tier2-review self-tests, the recall floor and its arms, the
lexicon naming predicates, memory hygiene and spec tokens. The spec declares no `New arm:` line, so
no RED-first observation is owed by this unit.
