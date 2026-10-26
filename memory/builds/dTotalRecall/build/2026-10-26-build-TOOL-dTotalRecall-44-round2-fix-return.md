**Serves:** research TOOL-dTotalRecall-44

# The round-2 fix pass — dTotalRecall, its return

The return of the gov-spec-writer dispatched from `memory/builds/dTotalRecall/prompts/2026-10-26-prompt-TOOL-dTotalRecall-44-1-spec-writer.md` over the round-2 fix brief, run direct/a67853fe9392e3a3c, extracted from its transcript by script.

All three findings are fixed and the hygiene gate is clean. Unit 43 is now 48897 bytes, generated region included, under the 48900 target.

I could not confirm the `check-spec-tokens.py` part of the brief. The scratch-guard hook blocks this role from running that leg (row G1), so the main session needs to run it. As a stand-in I wrote my own copy of its paths rule. Before the edits it found exactly the four F1 hits; after them it finds none in any dTotalRecall spec.

**Hygiene gate**, `bash tools/memory-tree/check-memory-hygiene.sh --only 2,5,12,21,25`: it exits 0 with no FAILED line. Its last line is:
`HYGIENE --only 2,5,12,21,25 ran checks 2 5 12 21 25`
Before the edits it exited 1, because check 12 flagged unit 53's AC9.

**Files edited** (all three are still uncommitted, and I did not re-stage them):
- `C:\projects\coding-governance\.claude\worktrees\unattended-dtotalrecall-4bf827\memory\builds\dTotalRecall\spec\2026-10-26-spec-TOOL-dTotalRecall-52.md` (F1, rev-1, no rev bump): AC3 now reads "`git ls-files memory/project` lists no `legacy-records.txt`". The full path stays in §2 and §4.
- `C:\projects\coding-governance\.claude\worktrees\unattended-dtotalrecall-4bf827\memory\builds\dTotalRecall\spec\2026-10-26-spec-TOOL-dTotalRecall-53.md` (F1 and F2, rev-1, no rev bump):
  - AC18 now reads "`git ls-files tools/playbook` lists no `edge_grammar.py`".
  - AC31 describes the fixture in prose ("a spec path in this build's spec folder") instead of the `x.md` path.
  - AC33 now reads "`grep -c derive_path_key memory_measure.py` runs in the runlog kit".
  - AC9 gets the witness `python record_causes.py --check`, run over the plant `literal-without-cause`. That is the arm the `New arm:` line already says covers AC9.
- `C:\projects\coding-governance\.claude\worktrees\unattended-dtotalrecall-4bf827\memory\builds\dTotalRecall\spec\2026-10-26-spec-TOOL-dTotalRecall-43.md` (F3, edited at rev-2): text outside the criteria is shorter.
  - What changed: §1, the §2 opening and item wording, §3 and its Edges descriptions, §4 Inventory, the Alternatives and batch order, §5, the options in §8, §10, and the one-line §6 preamble. The rev-2 line in §9 now ends "; non-criterion prose cut to the size cap."
  - What stayed: I compared the file before and after. All 59 scope items, every finding id and gap-mem-16 are present. Every AC bullet, the §7 leg line, the `New arm:` lines, the resolved-fork lines with their grants, and the generated `gen:spec-records` region are byte-identical.
  - What was lost: two short explanatory phrases. One was the parenthetical in F3's option (a) naming what each clause changes. The other was "the recall kit's new requirement" wording in an edge description, which I kept as "the kit's `requires`".

Nothing outside `memory/builds/dTotalRecall/spec/` was touched, and I did not commit or regenerate the index.
