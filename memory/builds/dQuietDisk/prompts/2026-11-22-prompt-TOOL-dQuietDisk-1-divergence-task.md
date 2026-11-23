**Serves:** research TOOL-dQuietDisk-1

# Spec task — dQuietDisk: unit 1's three divergences, and a sweep of every spec for the same two classes

You write specs only, in `memory/builds/dQuietDisk/spec/`. Do not commit. The spec brief
(`memory/builds/dQuietDisk/prompts/2026-11-20-prompt-TOOL-dQuietDisk-1-spec-brief.md`) still binds you.

Unit 1's builder (unit harness run `wf_b8113b9c-ba6`) built nothing and handed back three divergences. Each one
holds, and the first two can hit any spec in the roster.

## 1. Fix TOOL-dQuietDisk-1 (rev-2 → rev-3)

**(a) Names the lexicon refuses.**
- `python tools/lexicon/lexicon.py` reads `P1 verb graded=10978 offenders=1421`, and `.lexicon.conf` pins
  `VERB_OFFENDER_PIN="1421"`. The pin is full, so every name this unit mints must lead with a declared verb.
- The extractor walks methods and shell functions too.
- The refused names are:
  - `open_store`;
  - the store methods `get`, `put` and `prune`;
  - BatchReader's `info`;
  - the eight shell functions `hs_open`, `hs_tip_read`, `hs_lookup`, `hs_store`, `bh_open`, `bh_info`, `bh_read`
    and `bh_close`.
- Rename each one in §4 Inventory and in every S and AC line that spells it. Check each new name with
  `python tools/lexicon/lexicon.py --suggest <name> --as <cell>`, the cell being the one the Inventory names, such as
  `py.function` or `sh.function`. The builder proposed names like `resolve_store`, `read`/`write`, `remove_aged`,
  `read_info`, `init_hs` and `read_hs_tip`; take the verbs `--suggest` admits.
- Units 2, 3 and 4 consume these names. Where their specs spell one, rename it there too, with a rev bump and a
  revision-log line naming this task.

**(b) The budget reading a builder cannot take.**
- S11 and AC12 derive the `history-store selftest` budget from "the builder's direct reading" of
  `python tools/lib/history_store.py --selftest`. A hook refuses a role agent any `--selftest`.
- Make the row a PINNED estimate from a proxy reading: a timed run of the §6 probes, floored at 60 s. Its note says
  it is not a `--selftest` reading.
- The main loop re-prices it from the first measured run at the close, as the `leg-factory selftest` and
  `ratchet selftest` rows already do. Say so in AC12, and mark the re-price as owed to the main loop.

**(c) Files touched.**
- `tools/lib/` is not a kit: there is no `kit.toml`, and `tools/govkit/registry.toml` exempts it. So the new leg is an
  `[[exempt_leg]]` row in `tools/govkit/registry.toml`, as `python resolver (behaviour + inline parity + idiom ban)` is.
- Add `tools/govkit/registry.toml` to Files touched beside `tools/gate-legs.json`, and state that the manifest is
  re-rendered by `python tools/run-gates/leg_factory.py --write`.

## 2. Sweep every other spec for the same two classes

For each of TOOL-dQuietDisk-2 to -19 and -26:

- **Names.** Run `--suggest` on every identifier its §4 Inventory mints: function, method, shell function, constant,
  CLI verb and file. Rename every one the lexicon refuses, everywhere the spec spells it, so the offender pin is not
  exceeded. List what you renamed.
- **Gate readings.** Find every S or AC line that has the builder run a `*.test.sh`, a `--selftest`, a gate leg or
  the bar to derive a figure or observe a criterion. Turn each into one of two things:
  - a proxy probe the builder may run, with the real reading owed to the main loop;
  - a `New arm:` line the main loop observes.
- **Records.** A spec that changes gets a rev bump and a revision-log line naming this task. A spec with no hit
  changes nothing.

## Before you return

- Run `bash tools/unattended/unattended.sh --check-specs dQuietDisk` with every unit id you touched.
- Run `bash tools/memory-tree/check-memory-hygiene.sh --only 12 --spec <path>` on each spec you touched.
- Run `python tools/check-spec-tokens.py --spec <path>` on each spec you touched.
- Fix every finding.

Return: each spec you changed with its new rev and what changed, and each spec you checked and left alone.
