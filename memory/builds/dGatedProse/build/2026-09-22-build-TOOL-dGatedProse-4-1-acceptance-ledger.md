# The acceptance ledger — M4's precision bound, the method's budget on the owner's figures, and the leg runs owed

**Serves:** journal TOOL-dGatedProse-4

Node `d`, 2026-09-22, the build pass of `TOOL-dGatedProse-4` against spec rev-7, at order 5 on
`branch/spec-prose-gates-b41f7c`. This is the last unit in landing order. The pass base is
`cd0d3cce`, unit 3's closing commit. Two commits carry the work. `5da7d8ad` edits the template,
re-renders the live copy, moves the limits row with its reason paragraph and appends the decision
row. `598c89bd` refreshes the two dossier bullets. By the owner's rule no suite and no gate leg was
run. Every observation below was made by calling the code directly from python files in the session
scratchpad, which are untracked. The size checker was run only inside scratch git repositories built
for the purpose, never over this worktree. Each held a copy of the checker, the edited limits file,
the high-water record and the render.

Every figure the spec predicts reproduced exactly at the commit:

- the render measures 27936 bytes and the template 27961, both 352 lines, CR-stripped and carrying no CR.
- the sentence is 445 bytes, D1 with its space is 197, and the decision row is 293 characters and 295 bytes.
- M4's long line is 1123 characters and 1127 bytes, and M1's history line is 144 characters and 154 bytes.
- the trimmed sentence §4 rejects measures 323 bytes with its joining space.

The kit marker unit 3 stamped, `memory-tree@2.83`, is still line 1 of both carriers, and M4 still
spells `specs-reviewed` in backticks outside every comment. Each staged break named below was
applied to an in-memory copy of the tree's file, and its predicate turned red on it.

Everything a leg observes is OWED to the one run after all five units are built, and each such line
names the break that stages it red. The legs spec section 7 names are owed to that run as a whole.

**Evidences:** TOOL-dGatedProse-4
- AC1 — `**The CHAIN of promotions` — observed directly: the whole sentence, searched as a fixed string, answers exactly one line in each of the render and the template, line 142, between `## M4` at line 114 and `## M5` at line 148. Red when the template drops it, which answers zero there. Red when the trimmed variant lands instead, which also answers zero while its 46-character prefix still answers one.
- AC2 — `render_doc` — observed directly: the renderer, sourced with the kit directory and `tools/` bound, run over the template, printed 27936 bytes byte-identical to the live copy. OWED to the post-build kit/dogfood doc parity run. Red when the template is edited and the live copy is not re-rendered.
- AC3 — `bd44d3ff` — observed directly: D1 with its leading space answers one in each file at `bd44d3ff` and zero in each file in the working tree. The base half answering one is what shows the span was transcribed and not missed.
- AC4 — `THE CONVERGENCE PREDICATE DID NOT TERMINATE` — observed directly: the driver answers one for it. The unattended Skill and its kit template each answer one for the backstop-fired statement and one for the build-README statement, so the deletion is a displacement and loses nothing.
- AC5 — `tools/template-size-limits.txt` — observed directly: the build-method row carries 30720. The 8-line comment paragraph immediately above it carries 2026-09-21, 2026-09-22, `TOOL-dLoggedFlight-35`, 27936 and 2784, and no line spells the old pair figure. Both carriers' `**Budget:` line reads 30720 bytes and 400 lines, and each history carries the 2026-09-22 entry. Red when the paragraph is removed, or when the pair comment spells the old figure again. OWED to the post-build runs of the three unguarded size legs, which read other rows of the same file.
- AC6 — `bash tools/check-template-size.sh memory/guides/BUILD-METHOD.md` — OWED to the post-build build-method size run. Observed directly in a scratch repository: exit 0, the high-water WARN at +995 from 26941, then `template-size OK` at 27936 / 30720, 2784 under. Red when the row stays at 27648 while M1 moves, which exits 6 on check 6. Red when both stay at 27648, which exits 1 on check 2, 288 over.
- AC7 — `**Budget:` — observed directly: both files count 352 lines in the tree and 352 at the base, and both state a line figure of 400. Red when the sentence is wrapped onto its own line, which counts 353. Red when the line figure is left at 350, which leaves 352 over it. No gate reads this half.
- AC8 — `memory/map/features/build-method.md` — observed directly: the M4 bullet names the precision bound on the promotion chain and says no checker enforces it. The budget bullet names the owner's ruling of 2026-09-21 and `TOOL-dLoggedFlight-35`, and the `[claims]` block is byte-identical to the base. Both bullet predicates were red before commit `598c89bd` and green after it. OWED to the post-build codebase-map coverage and freshness run, which reds if a claim key moved.
- AC9 — `memory/DECISIONS.md` — observed directly: the diff against the base adds exactly one row naming `TOOL-dGatedProse-4`, 293 characters. It names both rulings' dates, 30720, 400 and `TOOL-dLoggedFlight-35`, and one row is led by the id. Red when the row is removed, which leaves zero, or duplicated, which leaves two. OWED to the post-build memory hygiene run, whose check 7 grades the entry budget and whose check 20 grades one id per row.
- AC10 — `so part of that figure is headroom the bytes do not grant` — observed directly: each carrier holds it once and holds the `most` wording nowhere. Red when the template carries `most` again.
