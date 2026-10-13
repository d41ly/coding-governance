# Acceptance ledger — TOOL-dSweptBranches-5

**Serves:** journal TOOL-dSweptBranches-5

Built on `5bd6ca59`, inline, last. The adopter is the runlog kit's cut down to one token, `KIT_DIR`,
so it needs no python. The template names the CLI only through that token, and the adopter refuses a
literal `tools/` path in it. `govkit selfcheck` first reported two problems, both the adopter name
`inCMS` in shipped files — the README and a CLI comment from unit 4 — and both now read `adopter ic`.

**Evidences:** TOOL-dSweptBranches-5
- AC1 — `adopt-branch-reconcile.sh --check` — exits 0 on the fresh render; exits 1 naming the file after one byte is appended, and exits 1 after a template edit nobody re-rendered; `--scaffold` restored bytes `cmp` reads identical
- AC2 — `SKILL.md` — `grep -cF` finds each of the four trigger phrases, the `## Attended` and `## Unattended` headings, `UNMERGED-LIVE`, `--remote` and the merge offer at least once; the fourth trigger phrase was first missed because the description wrapped it across two lines, and the template now keeps it on one
- AC3 — `govkit.py selfcheck` — 0 problems with the rendered row declared; `check-kit-versions.sh` clean over 16 carriers; `check-kit-placeholders.py` grades the kit's one token against its adopter

## Owed at the close

The `branch-reconcile skill wiring` leg and the spec's §7 legs run in the close's bar.
