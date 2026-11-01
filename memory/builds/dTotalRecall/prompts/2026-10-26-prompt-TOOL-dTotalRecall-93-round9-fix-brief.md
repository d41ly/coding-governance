**Serves:** research TOOL-dTotalRecall-93

# Round-9 fix brief — dTotalRecall, the last round's checks and three §8 mark wraps

The round-9 spec audit's disposal (`unattended-build.js` run `wf_5e12f7a3-44e`) wrote the promoted specs
TOOL-dTotalRecall-93 to -100 under `memory/builds/dTotalRecall/spec/` and folded each hands-off edge into the spec it
names. The owner ended the audit chain at round 9
(`memory/builds/dTotalRecall/prompts/2026-10-26-prompt-TOOL-dTotalRecall-1-owner-review-stop.md`), so these are the
last specs this run writes. Clear every finding below, changing nothing else in any spec's design, so that
`python tools/check-spec-tokens.py` prints no dTotalRecall hit, `bash tools/memory-tree/check-memory-hygiene.sh
--only 2,5,12,21,25` prints no FAILED line naming a dTotalRecall file, and the departures instrument reads every §8
mark's `widens:` value whole.

- Units 93 to 100 are uncommitted at rev-1 and unaudited: edit them in place with no rev bump. A spec the disposal
  folded is uncommitted at its new rev: edit it in place at that rev, extending that rev's §9 line.
- Your role admits the hygiene gate and the lexicon only. The files are staged in this worktree, so run the hygiene
  gate in place. Do not commit and do not run the build-index generator.

## F1 · paths in acceptance criteria that do not exist at HEAD

Describe a fixture's example path in prose rather than as a backticked path literal, and cite a not-yet-built file by
basename. The hits:
- unit 100: `69):memory/guides/SESSION-KICKOFF.md"` (a fragment of a backticked command), and
  `memory/builds/dTotalRecall/build/none-deviation-0.md` (a fixture example)
- unit 98: `memory/builds/dTotalRecall/build/x-deviation-1.md` (a fixture example)

## F2 · retirements with no Readers clause

Hygiene check 25 reds unit 100 S14 and unit 98 S2: a §2 item that retires a named thing carries no `**Readers:**`
clause. Write each as `memory/TEMPLATE-SPEC.md` states: `**Readers:**`, then `by name:` and every reader that spells
the name, then `by value:` and the readers of its value, or `NO VALUE READERS` and a reason, each found by
`git grep` over the tree.

## F3 · three §8 marks whose `widens:` value wraps

The departures instrument (`memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-deviations.py`) reads
a §8 RESOLVED mark's `widens:` and `relaxes:` values from one line. In three marks the wrap splits `widens: none ·`
from its `relaxes:`, so the value reads `none ·` and joins no record:
- `TOOL-dTotalRecall-14` §8, the mark near line 243 (`(a), rung 1, the clause's words (brief D6)`)
- `TOOL-dTotalRecall-24` §8, the mark near line 217 (`(a), rung 1, the clause's "once it lands"`)
- `TOOL-dTotalRecall-26` §8, the mark near line 340 (`(c) is the copy I20 forbids … (a), rung 3`)

Re-wrap each so its tail sits on one line as `widens: none · relaxes: none` (or the values it already carries).
This is a whitespace-only edit: nothing the mark decides changes, and the spec takes no rev bump for it.

## Return

The list of files you edited, one line each on what changed, and the last line of the hygiene gate run.
