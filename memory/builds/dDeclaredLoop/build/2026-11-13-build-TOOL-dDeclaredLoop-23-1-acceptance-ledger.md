# TOOL-dDeclaredLoop-23 — acceptance ledger

**Serves:** journal TOOL-dDeclaredLoop-23

No merge bar, no self-test suite and no gate leg ran in this pass. The criteria were observed by
scratch probes of the code the pass changed: the reader's own CLI, `python` probes that import the
working tree's modules beside the parent commit's, read out with `git show`, and shell probes that
source the working tree's library beside the parent commit's. The planted repository is the one
`tools/lib/commit_trailers.py#build_fixture` builds, under the system temp directory. The pass base
is `e6da7ba1`.

Owed to the close, each observed by the main loop there: every leg the spec's section 7 names, and
the RED-first observation of its `New arm:` lines, which this pass did not run.

- New arm `tools/memory-tree/routed_commits.py`, covering AC2: the union arms of its self-test now
  run through `tools/memory-tree/routed_commits.py#read_routed_commits` and `derive_attribution`; the
  staged break is `"replace"` passed in `tools/memory-tree/routed_commits.py#check_routed_commits`.
- New arm `tools/lib/resolve-python.test.sh`, covering AC5: the `commit_trailers_py` row of
  `PARITY_ROWS`; the staged break is a one-byte edit to the unattended kit's copy.
- New arm `tools/playbook/edge_grammar.py`, covering AC7: the registry the `prose-pass` plant and
  `--list` read is the shipped `edges.toml`, which now holds rows with no `type`, so it is the
  fixture registry the line names and the pass added no second one; the staged break is the type
  demand restored in `tools/playbook/edge_grammar.py#read_trailer_keys`.

Also owed to the close: the fork counts of `memory/project/fork-ceilings.txt`, which only the spawn
budget leg's counter measures. The pass left that file as it was: neither row's fixture holds a
dispatch row or runs the commit check, so neither reaches a re-pointed reader. The unattended kit's
suites are waived for this landing by the build README's rule, and an arm of theirs that sources the
library with no `resolve_python` defined now meets the reader's named refusal.

**Evidences:** TOOL-dDeclaredLoop-23
- AC1 — `--fixture` — `python commit_trailers.py --fixture`, run in the gov lib directory, printed one
  line per planted commit, oldest first: `union TOOL-tFix-1 · replace TOOL-tFix-1`, then
  `union TOOL-tFix-1 · replace (nothing)`, then `union TOOL-tFix-2 · replace TOOL-tFix-2`, and exited 0.
- AC2 — `read_routed_commits` — the probe imported the working tree's `routed_commits`, read the
  planted repository with `read_routed_commits(repo, ["HEAD"])` and printed
  `derive_attribution(c, "union", build_id_re(["TOOL"]))` as `TOOL-tFix-1`, `TOOL-tFix-1`,
  `TOOL-tFix-2`. Each commit's `sha`, `parents`, `date`, `subject`, `trailer`, `red_fix` and `paths`
  equalled what the parent commit's file returned over the same repository, and over this
  repository's own newest three hundred commits no field differed and the union ids equalled
  `extract_unit_ids` over subject plus trailer. The red case was read in the same probe: under
  `"replace"` the `Pass: none` commit names nothing where `union` names `TOOL-tFix-1`.
- AC3 — `read_attribution_tokens` — with gov's `resolve_python` defined, `read_attribution_tokens HEAD`
  over the planted repository from the parent commit's library and from the working tree's compared
  identical under `cmp` after `tr -d '\r'`, the `PASSTRAILER` lines and the runs of spaces included.
  The same held over this repository's newest four hundred commits and over a `--reverse` range of
  its newest ones. The working tree's raw output held no CR byte, by deviation 233. `pass_commit` from both
  libraries named the same commit for each of four anchor and unit pairs of this build's run state,
  the still-open pass of this unit among them.
- AC4 — `PASSTRAILER` — `python commit_trailers.py message <file>`, run in the unattended kit's
  directory over the planted commits' messages, printed `TOOL-tFix-1 a subject id no trailer`, then
  `PASSTRAILER`, then `PASSTRAILER TOOL-tFix-2`; the first message with CRLF line ends, a `#` comment
  line naming another id and a body printed the first line again. A second probe compared the commit
  check's old read of a message with its new one over eight planted messages, a `none` beside an id,
  a punctuation-only value, an upper-case key and a comment inside the subject paragraph among them:
  the branch taken and its tokens were the same for each.
- AC5 — `PARITY_ROWS` — `git grep -c "commit_trailers_py" -- tools/lib/resolve-python.test.sh` counted
  the row and its comment, and `git grep -l "^# >>> commit_trailers_py" -- tools` listed the canonical
  and the memory-tree and unattended copies. The parity table's extractor,
  `tools/lib/resolve-python.test.sh#blk`, copied into a probe, read each copy's block identical to
  the canonical's, and a scratch copy with one byte changed read as drifted. The same extractor read
  the `resolve_kit_dir` block of all three files, and the `resolve_python` block of the two legs,
  identical to their canonicals.
- AC6 — `Gov-Nope` — `grep -n 'class = "commit"' namespaces.toml` found the row, and
  `grep -nE 'key = "(Gov-Transition|Gov-Policy|Red-fix)"' edges.toml` found all of its rows, both run
  in the playbook kit's directory; `read_commits` asked for `Gov-Nope` raised a `ValueError` saying the
  trailer key 'Gov-Nope' is not registered, with the table's path. Before the rows landed the same
  call refused `Red-fix` the same way, which is the refusal seen able to fire on a real key.
- AC7 — `edges: trailer` — `python edge_grammar.py --list`, run in the playbook kit's directory, exited
  0 and its `edges: trailer` lines named `Gov-Unit`, `Gov-Item`, `Gov-Act`, `Gov-Session`, `Pass` and
  `Decided` and no other. `python gov_tag.py check` is the tags leg's command and was NOT RUN; in its
  place a probe called `tools/playbook/edge_grammar.py#check_native_classes`, which builds that line,
  over the working tree: it returned no red and the line
  `tags: native · commit (owner dDeclaredLoop) · 8631 members`, PINNED, measured 2026-11-13 at the pass base.
  A probe over scratch registries saw
  `read_trailer_keys` pass over a row with no `type`, refuse a key two rows name where one carries
  none, and refuse a type outside the set.
- AC8 — `resolve_python` — `git grep -c "^# >>> resolve_python" -- tools/unattended/check-pass-order.sh
  tools/unattended/check-brief-recorded.sh` counted one block in each. A scratch shell sourcing the
  working tree's `lib-unattended.sh` with no `resolve_python` defined got status 2 from
  `read_attribution_tokens HEAD`, nothing on stdout, and on stderr the line `lib-unattended:
  read_attribution_tokens found no python launcher, so no commit is attributed`.
- AC9 — `commit` — `grep -n 'commit' help/tags.md` shows the native-ids paragraph saying three classes
  are registered and naming `commit` with its owner dDeclaredLoop, and the sentence listing the words
  no row registers yet names `feature`, `item` and `session`.

Beside the criteria. The shell-hygiene scanners, called as functions over the five shell files at the
parent commit and in the working tree, counted the same sites in every class, so no row of the
spawn-idiom, substitution-loop, temp-name or location-probe registries moves. The encoding scanner
found no site in the new reader or the three changed modules.
`tools/memory-tree/deviation_join.py#read_first_passes` returned the same first passes as the parent
commit's over this repository's newest fifteen hundred commits. Check 23's read of one commit's
attributing text gave the same tokens as the parent commit's lines over the newest forty. One read
through the new shell reader cost about one second on this node against about a quarter of that
before, measured over five calls: the interpreter start the spec's section 5 prices and
`TOOL-dDeclaredLoop-56` bounds.

Deviations recorded by this pass: `2026-11-13-build-TOOL-dDeclaredLoop-23-deviation-233.md`, what the
shell readers do around the CLI, and `2026-11-13-build-TOOL-dDeclaredLoop-23-deviation-234.md`, the
reader's helper names and the routed reader's refusal.
