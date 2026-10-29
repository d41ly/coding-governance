# TOOL-dMindYourWords-11 deviation 111 — the stamp's readers named as source shows them, not as the clause names them

**Serves:** deviation TOOL-dMindYourWords-11

- **Departs from:** `cl-dClosedLoop-0272@aac8dd76`
- **Hand-off:** design-to-spec
- **Before:** the vocabulary changed only through the instruction write path, with `ratified` replaced by its record and its readers by value moved with it: the drift signal comparing VERBS and LANGS edits (`drift_signals.py`, `drift_report.py`), `adopt-lexicon.sh --check`, the kit's `lexicon-pins` hole, the scaffold and the lexicon's own reads of it in `lexicon.py` and `lexicon_conf.py`, the leg pack's arm seen red on a planted LANGS change newer than the record, and the `init` row re-justified
- **After:** the vocabulary changed only through the instruction write path, with `ratified` replaced by its record and its readers by value moved with it: the drift signal comparing VERBS and LANGS edits (`drift_signals.py`, `drift_report.py`), `adopt-lexicon.sh --check`, the kit's `lexicon-ratified` hole, and the scaffold that writes the stamp, the lexicon's own reads of the record added in `lexicon.py` and `lexicon_conf.py`, which read no `ratified` today, the kit's `lexicon-pins` hole left to the pin's units, the leg pack's arm seen red on a planted LANGS change newer than the record, and the `init` row re-justified
- **Cause:** design defect
- **Reason:** The clause names two readers source does not hold. The hole that discharges through the stamp is `lexicon-ratified` (`tools/lexicon/kit.toml:177-183`, discharged by `adopt-lexicon.sh --check`); `lexicon-pins` (`:185-191`) discharges through `lexicon.py` and reads the pins, which TOOL-dMindYourWords-14 (d) and TOOL-dMindYourWords-1 rewrite. Neither `lexicon.py` nor `lexicon_conf.py` reads `ratified` by value: the loader parses any scalar generically and the only text is a comment (`lexicon_conf.py:164`), while `lexicon.py`'s three uses of the word mean "a fork was ratified". The clause's intent, every by-value reader moved with the stamp, is carried whole by TOOL-dMindYourWords-11 S5 to S7 over the readers source shows, and the two modules gain the record's reader and check instead. The departure is the names, not the mechanism.
- **Evidence:** the clause, `memory/builds/dMindYourWords/prompts/2026-10-21-prompt-PLAY-dClosedLoop-1-packet.md:31`; scout C's disagreements 1 and 2, `memory/builds/dMindYourWords/build/2026-10-29-build-TOOL-dMindYourWords-11-reuse-scout-c.md:20-21`; `git grep -nw ratified -- tools/ .lexicon.conf` at `ba8b3c8c4`; the new hash, `derive_clause_hash` (`tools/memory-tree/design_lib.py:169`) over the After text, `51d03a52`, which returns `aac8dd76` over the Before text
- **Risk:** editorial
- **Approver:** spec writer, the gov-spec-writer role of dMindYourWords' spec run, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** amends cl-dClosedLoop-0272@aac8dd76
- **Caused-by:** TOOL-dMindYourWords-11
