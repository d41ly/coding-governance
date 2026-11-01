**Serves:** research TOOL-dLinkedLibrary-4 TOOL-dLinkedLibrary-6 TOOL-dLinkedLibrary-7 TOOL-dLinkedLibrary-11 TOOL-dLinkedLibrary-15 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-17 TOOL-dLinkedLibrary-19 TOOL-dLinkedLibrary-23 TOOL-dLinkedLibrary-1

# Fix brief — dLinkedLibrary, the spec set's check findings before its first commit

The SPEC stage of `unattended-build.js` run `wf_1e9f5c74-0bb` authored all 25 specs under
`memory/builds/dLinkedLibrary/spec/`, and its commit stage was refused. The main loop then ran the memory hygiene
gate, `tools/check-spec-tokens.py` and the carries join over the set: coverage is whole (25 of 25 clauses, every owned
node named), and the findings below are the whole remainder. Fix each in the file it names, and nothing else. The
specs are uncommitted rev-1 drafts: edit them in place, with no rev bump and no §9 line, because no revision of them
has been committed or reviewed yet. Do not commit, and do not run the build-index generator.

Read `memory/builds/dLinkedLibrary/prompts/2026-10-26-prompt-TOOL-dLinkedLibrary-1-spec-brief.md` "Every spec" and
"What the last spec runs had to fix" first; each finding below breaks one of its rules.

## Hygiene check 12 and 25 — TOOL-dLinkedLibrary-4

1. `2026-10-26-spec-TOOL-dLinkedLibrary-4.md` carries an unfilled skeleton placeholder. Find it (a template
   placeholder left as written, such as an angle-bracketed template instruction or `TBD`), and fill or delete it.
2. Its scope item S13 names neither an acceptance criterion nor `NOT OBSERVED`. Join S13 to a §6 criterion that
   observes it, or mark it `NOT OBSERVED` with the reason `memory/TEMPLATE-SPEC.md` asks for.
3. Its scope item S10 carries a `**Readers:**` clause whose by-value half names no backticked reader and no `NO VALUE
   READERS` with a reason. Answer it: find the readers by value with `git grep` over the tree and name each in
   backticks, or write `NO VALUE READERS` and the reason.

## Hygiene check 12 — a one-sided §3 edge

4. `TOOL-dLinkedLibrary-15` declares **consumes-from** `TOOL-dLinkedLibrary-4`, and unit 4 declares no
   **hands-off** `TOOL-dLinkedLibrary-15` back. Read unit 15's bullet for its token, then add the matching
   **hands-off** bullet to unit 4's §3 naming the same token in backticks, and make sure unit 4 names that token
   where it defines it.

## check-spec-tokens — hand-off tokens the receiving spec never names

Each bullet hands a token to a sibling whose spec never names it. In the RECEIVING spec, name the token in
backticks where that unit reads or uses it (its §2 item or §4 design, and its **consumes-from** bullet), or, when the
bullet is wrong, correct the sender's bullet to the token the receiver does use. Either way both specs end naming one
spelling.

5. `TOOL-dLinkedLibrary-11` → `TOOL-dLinkedLibrary-7`: `[[ledger]]`.
6. `TOOL-dLinkedLibrary-12` → `TOOL-dLinkedLibrary-7`: `annotations.py check --selftest`.
7. `TOOL-dLinkedLibrary-17` → `TOOL-dLinkedLibrary-7`: `annotations.py check --only span`.
8. `TOOL-dLinkedLibrary-18` → `TOOL-dLinkedLibrary-23`: `splice_region`.
9. `TOOL-dLinkedLibrary-19` → `TOOL-dLinkedLibrary-4`: `gov:feature <tag>`. Unit 4 spells the anchor
   `gov:feature <name>`; pick one spelling for both specs, the brief's I9 reads `gov:feature <tag>`.
10. `TOOL-dLinkedLibrary-4` → `TOOL-dLinkedLibrary-17`: `extract_comment_spans`.
11. `TOOL-dLinkedLibrary-4` → `TOOL-dLinkedLibrary-11`: `derive_defined_ids`.

## check-spec-tokens — paths and legs

12. `TOOL-dLinkedLibrary-19` names `tools/codebase-map/dossier_move.py` where the checker reads it as a path that
    git does not track. A file this unit will create is cited by its basename (`dossier_move.py`) in §6, keeping the
    full path in §2, §4 and Files touched only.
13. `TOOL-dLinkedLibrary-6` names `views/stray.md` as a path git does not track. If it is a planted fixture file,
    describe it without a path-shaped token in §6 (a planted stray view file under the views folder), or cite it as
    the basename `stray.md`.
14. `TOOL-dLinkedLibrary-16`'s files-touched names
    `memory/builds/dLinkedLibrary/build/<date>-build-TOOL-dLinkedLibrary-16-code-replay-verdict.md`, which trips the
    guards of the legs `recall floor` and `recall floor arms`, and its §7 leg line names neither. Add both legs to
    its §7 leg line (`python tools/check-spec-tokens.py --list` prints the legs a path trips).

## The as-built view — the deviation record

15. `memory/builds/dLinkedLibrary/build/2026-10-26-build-TOOL-dLinkedLibrary-1-deviation-11.md` departs from
    `cl-dClosedLoop-0238@36136b48` and carries no `amends` or `supersedes` row, so hygiene check 30 refuses it. Its
    `**Follow-through:**` line must read `amends cl-dClosedLoop-0238@36136b48` (the shape
    `memory/builds/dBoundRoles/build/2026-10-25-build-TOOL-dBoundRoles-10-deviation-101.md` line 14 shows), and its
    `**After:**` must hold no `|` character, because the as-built view renders it as a table cell. Rewrite `**After:**`
    as the clause's full text with only the departure changed, since the view replaces the clause's text with it.

## Then

Run `bash tools/memory-tree/check-memory-hygiene.sh --only 2,12,25` and confirm none of these files is named. Return
each finding's number with what you changed, by file.
