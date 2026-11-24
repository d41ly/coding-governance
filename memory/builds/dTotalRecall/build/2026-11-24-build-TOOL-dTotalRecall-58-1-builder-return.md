**Serves:** journal TOOL-dTotalRecall-58
**Caused-by:** TOOL-dTotalRecall-58

# TOOL-dTotalRecall-58 build pass 1 — the builder's return

The gov-builder return for the pass dispatched at `fa67a5614` from [2026-11-24-prompt-TOOL-dTotalRecall-58-build-brief](../prompts/2026-11-24-prompt-TOOL-dTotalRecall-58-build-brief.md), recorded whole; the pass tip is `none`.

## Why

DIVERGENCE: spec §6 AC4 (with §2 S4) cannot hold together with §4 "The rule", §3 and §10. One blocker, two stale phrases and one loose shape.

1. BLOCKER, AC4 against §4/§3/§10. §4 makes the new `id_grammar.py#check_marker_domain(path, text, census)` return one red per line "that `read_kept_reason` reads for `census`". §3 says this unit "calls and leaves as it is" that reader, and §10 places the function beside it.
   - So the built function is a fourth caller of `read_kept_reason`. AC4 runs at the pass tip and requires `git grep -n "read_kept_reason(" -- tools` to list "the definition and the three callers S4 names", Red when "a fourth caller reads one". The pass as designed prints definition plus four calls and is red by its own criterion.
   - The ways round it are not mine to take. Reading `KEPT_MARKER_RE` directly breaks §3, §4 and the one-reader docstring at `id_grammar.py#read_kept_reason`. Spelling the call so the grep misses it (`map(read_kept_reason, ...)`) evades the criterion.
   - What the spec would have to say. In AC4: "lists the definition, the three callers S4 names and `id_grammar.py#check_marker_domain`", Red when "a build-folder script carries a marker, or a caller beyond those four reads one".
   - In S4: keep the three as the pre-pass HEAD measure and add that the pass adds `check_marker_domain` as the fourth. It is the only caller that reads build-folder lines, and it reads them to refuse. S4's sentence "the alias and cause censuses call it on tool-root files alone" is then true of their own calls.

2. Stale, fix in the same revision. S1 names `CAUSE_WRITER_KEPT` ("by `CAUSE_WRITER_KEPT`, by the path-keyed row unit 55 moves it to") and S3 names `ALIAS_COMPARE_KEPT` ("or by unit 56's row after it"). Both are retired at HEAD (`git grep` over `tools` prints nothing). The one keep is `tree_lib.py#CENSUS_KEPT_PATHS`, read through `read_kept_path`.

3. Loose, worth one sentence in the same revision. §4 has `check_marker_domain` return findings naming path, line and remedy, while each census must also print `<census> · <path>:<n> · red · marker in a build folder`.
   - A return of `(line number, finding)` pairs gives the caller `n` without parsing it back out of the finding.
   - §4 also does not say whether a marker red enters the build-folder count line's `N red`. Today that count is of hits (`check_alias_compares`) or census files (`check_cause_writers`), and the drained-row red stays outside it. I would leave marker reds outside too.

## Summary

No product file was edited and nothing is committed. The only tracked change is the main loop's staged memory/builds/dTotalRecall/RUN.md, untouched by me; it already held this unit's brief and dispatch rows, so I ran neither verb again. No draft was made, so there is no patch.

Every other claim I probed at base holds, so after the AC4/S4 revision the unit builds as written.
- **Callers:** `read_kept_reason` has exactly the three callers S4 names.
- **AC4 first half:** `git grep -c "census: kept"` over build-folder code files printed nothing.
- **AC2 first half:** the `git log` subjects contain no dTotalRecall.
- **S2 blobs:** `git hash-object` over all seven pinned instruments equals the packet's Pins list.
- **§3:** the two `slug-grammar` markers outside the tool root are exactly the two files it names.
- **Naming:** `lexicon.py --suggest check_marker_domain --as py.function` answered OK.
- **AC1 baseline:** a `python -c` probe of `record_causes.py#run_fixture` with the marker on the pinned instrument's Serves line exits 0 green at HEAD, marker read at line 13. The new refusal will therefore be the single red.
- **AC3 baseline:** with `FIXTURE_BUILD_ALIAS` rebound to the `check_alias_compares` kept path, `record_kinds.py --fixture --plant unkept-build-alias` exits 0, kept by its row with no other red. The hit sits at line 14.
- **Files touched:** none of the three modules is on the kickoff manifest's `watch:` list.

AC2's second half is SKIPPED, not observed. `packet.py --check dTotalRecall` exceeded a 100 s bound (its `carries.py --report` child was killed with 143); a second background run with a 580 s bound had printed nothing when I returned. The next pass should give it 600000 ms in the background and await the notification, or the close observes it.

Owed to the close after the rebuild: §7's legs and the RED-first observation of both New arms, `marker-in-build-script` (record_causes.py) and `marker-in-kept-script` (record_kinds.py). gotchas.py --for-diff was not run, as there is no commit to read.
