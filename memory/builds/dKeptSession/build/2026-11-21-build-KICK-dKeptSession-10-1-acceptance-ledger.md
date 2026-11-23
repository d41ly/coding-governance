# KICK-dKeptSession-10 — acceptance ledger

**Serves:** journal KICK-dKeptSession-10

No merge bar, no self-test suite and no gate leg ran in this pass, and the legs the spec's section 7
names were not run as commands. The criteria were observed on win32 at the pass's base `689698a5`
over the working tree before the commit: by direct CLI runs of `tools/loop/position.py --fixture
--plant <case>`, `tools/loop/loop_transition.py --fixture --plant mail-argv` and
`skills/session-kickoff/card-store.fixture.sh --plant <case>`, by `python -c` probes of
`tools/loop/position.py#read_mail_interrupts` with its two reads rebound in the probe's process, by the
position engine's CLI in this tree, and by the greps, `docs_leg.py --fingerprints` and `policy.py` verbs
AC7 and AC8 state.

Before the first edit the spec's cited code was probed at the base. `derive_interrupts` appended the one
`{"kind": "mailbox", "subject": "unarmed"}` entry; `read_mail_rows` took `(root, build)` and zipped each
row of eleven or more fields with the eleven `MAIL_COLUMNS` (DERIVED, read at `689698a5`);
`write_fixture_gov_ref` pushed to `FIXTURE_REMOTE` alone; `run_card_boundary`'s crossing branch ended at
`run_context_boundary`; `print_mailbox`'s `--open` kept the rows whose fourth column reads `open`;
`len(PLANTS)` read 32 (DERIVED, imported at `689698a5`); `FLOOR_ASSERTIONS` read 441 (DERIVED, its last
assignment at `689698a5`); the `mailbox.reads` catalogue row held no `summary` and its default read
`every-item` through `read_catalogue_row` (DERIVED, that probe); and `docs_leg.py --fingerprints` printed
`script:tools/loop/position.py` at `8d078234` and `policy:mailbox.reads` at `6509cdac` (PINNED, that run
at `689698a5`), as AC7 records. No arm of any suite greps the card-store stub's refusal text this pass
rewords, and no other text the pass changes is grepped by an arm.

## Criteria

**Evidences:** KICK-dKeptSession-10
- AC1 — `mail-open` — `position.py --fixture --plant mail-open` printed `interrupt — mailbox · a1b2c3d4e5f6 question from fy` then `interrupt — mailbox · b2c3d4e5f6a1 intake from fy · amendment`, no line for the answered question `c3d4e5f6a1b2` or tPos's answer `d4e5f6a1b2c3`, then `plain call interrupt — mailbox · unarmed · ids none` for the same plant's `derive_position`, and `position: fixture · mail-open · held`, exit `0` (DERIVED, that run).
- AC2 — `mail-boundary` — `card-store.fixture.sh --plant mail-boundary` printed three `held` rows: the crossing `boundary — K1 → K2` at line 1 and the planted `interrupt — mailbox · m1 question from fy` at line 4 of the verb's output; the run with the key held printing `boundary — none crossed`, no `interrupt — mailbox` line and no new `--mail-interrupts` row in the stub's log; and, with `mail-delay` at 5 and `CARD_CLAIMS_BOUND=2` (PINNED, the plant's own values), the crossing back to K1 printing `interrupt — mailbox · unarmed · the read passed its 2s bound`; exit `0` (DERIVED, that run). The existing `pointers-boundary` plant, whose crossings now run the step, printed its five rows `held`, exit `0` (DERIVED, that run).
- AC3 — `mail-transitions-only` — the plant printed only `interrupt — mailbox · read at transitions (mailbox.reads: transitions-only)`, then `held`, exit `0` (DERIVED, that run).
- AC4 — `mail-amendments` — the plant printed `interrupt — mailbox · e5f6a1b2c3d4 changed from fy` and `interrupt — mailbox · 1 intake held to the next transition (mailbox.reads: every-item-amendments-at-transitions)`, the held count 1 (PINNED, the plant's one `intake`), then `held`, exit `0` (DERIVED, that run).
- AC5 — `mail-unarmed` — the plant printed one line, `interrupt — mailbox · unarmed · no unattended kit holding unattended.sh in this install: looked in …`, the real locator's words over the empty `.git/fx-empty`, then `held`, exit `0`, and no exception (DERIVED, that run).
- AC6 — `mail-refused` — the plant printed `interrupt — mailbox · mailbox.reads refused, read as every-item:` followed by the policy kit's refusal, which names the policy file's second line, `mailbox.reads: "sometimes" is not one of` the three values, and that no valid revision of the file precedes the fixture commit; then `mail-open`'s two lines and `held`, exit `0` (DERIVED, that run). The default is read through `policy.read_catalogue_row` over `policy.load_catalogue(policy.KIT)`, never typed.
- AC7 — the texts — `grep -n 'mail-interrupts\|mailbox.reads\|intake' help/loop.md` found each in the section "Where a build is, and what runs next", in the new bullet and the fixture sentence; `docs_leg.py --fingerprints` printed `script:tools/loop/position.py` at `c1931acf` and `policy:mailbox.reads` at `6509cdac` (DERIVED, that run after the edit), the fingerprints the two `help/loop.md` anchors carry, the second unmoved since it hashes `allowed` and `default` alone; `grep -c 'policy:mailbox.reads' memory/project/docs-undocumented.txt` printed `0`; `grep -n 'interrupt — mailbox' help/orientation-card.md` found the sentence after the crossing's `boundary —` line (DERIVED, those greps).
- AC8 — the key's row — `python tools/policy/policy.py get mailbox.reads` printed `every-item` in this tree, whose policy file sets no mailbox key; `lists --write` printed `drained 1: mailbox.reads` and `grep -c '^mailbox.reads$' tools/policy/unsummarised-keys.txt` printed `0`; `lists --check` printed `green · 0 finding(s)` (DERIVED, those runs). `mirror --write` refused while the catalogue differed from HEAD, the mirror rendering a revision, so the mirror is re-stamped in the commit after the build commit and `mirror --check` is observed there.
- AC9 — `mail-argv` — `loop_transition.py --fixture --plant mail-argv` printed `loop: fixture · mail-argv · held`, the guard's argv still ending `--mail read tFix` with no `--local` (DERIVED, that run).

S4's pass-through reached the driver: `position.py dKeptSession --mail-interrupts --local` in this tree
printed `interrupt — mailbox · unarmed · mail unknown: --mail read dKeptSession exited 2:` and the
driver's `--mail takes … not --local` refusal, exit `0` (DERIVED, that run), as S4 says until
KICK-dKeptSession-21 lands the flag. A probe with `read_policy_kit` raising LookupError printed the
`mailbox.reads unread, every kind listed:` line and listed an open row sighted `-` after one sighted
at a stamp, a `reply` and an `expired` row unlisted; with `read_mail_rows` raising its ValueError it
printed one `unarmed · mail unknown: …` line (DERIVED, that probe). `ap.error` refused
`--mail-interrupts` with no slug, beside `--json` and beside `--boundary`, and `--local` without it.

The five position plants read 3.84 s, 1.5 s, 2.29 s, 1.43 s and 3.29 s, 12.4 s together (PINNED, one
direct-CLI run each on the run's node at `689698a5`), so the `loop position fixtures` row reads r 80.9 s
and keeps its 432 s; its `plants=` token reads 37 (DERIVED, `len(PLANTS)` after the edit). The
`mail-boundary` plant read 100.4 s (PINNED, one direct-CLI run), so the `manifest-check self-test` row
reads r 3431 s and 5147 s (DERIVED, x1.5 rounded up), under its 6480 s ceiling (PINNED,
`tools/gate-legs.json` at `689698a5`). `FLOOR_ASSERTIONS` reads 442 (DERIVED, base plus the plant's one
ok row). `python tools/lexicon/lexicon.py` exited 1 on its verb-offender pin, 1432 offenders over a pin
of 1421 (DERIVED, that run), the count unit 24's ledger read at its base, and `--offenders` names none
of `read_mail_interrupts`, `check_mail_plant`, `run_mail_interrupts` or the nested `resolve_empty_kit`.
`gen_map.py --write` added those three functions to `memory/map/generated/symbols.json` and moved
nothing else. Both `New arm:` lines' RED-first observations are the close's.
