# Acceptance ledger — TOOL-dHomedResolver-2

**Serves:** journal TOOL-dHomedResolver-2

Built on `5e5c2692`. The generator's new arms were applied alone to a `git archive` of base
`5a836bf0` and its self-test run there first: the three refusal arms failed, because both verbs ran
over the untracked archive in silence. On this code all five pass. The hygiene suite's new check 9
arm failed against the base kit through the scratchpad probe and passes here.

Before wiring, the predicate (`git ls-files --others --exclude-standard` under `memory/archive/`) ran
read-only over gov, inCMS core and nc: none holds an untracked or an ignored file there, so the guard
reds no innocent tree. `migrate_backlog.py`, the one gov tool that renders after touching archives,
stages every archive it touches through `git checkout` or `git rm`, so it cannot meet the refusal.

**Evidences:** TOOL-dHomedResolver-2
- AC1 — `gen_build_index.py --selftest` — `cmd_write` over an untracked DECISIONS archive raises a refusal naming it and `git add`, and the README is byte-unchanged; red at 5a836bf0
- AC2 — `cmd_check` — over the same fixture raises the same refusal; red at 5a836bf0
- AC3 — `cmd_write` — with only an ignored `notes.scratch` under the archive folder returns rc 0
- AC4 — `check-memory-hygiene.sh` — over the `rotarchive` fixture's half-staged state check 9 names the unstaged ARCH archive and `git add`; red at 5a836bf0
- AC5 — `git grep -n 'check_archives_tracked'` — prints the guard and its two call sites in gen_build_index.py, and the HYGIENE check 9 entry says the generator refuses an untracked archive
