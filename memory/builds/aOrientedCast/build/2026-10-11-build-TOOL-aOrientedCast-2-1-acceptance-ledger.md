# TOOL-aOrientedCast-2 — acceptance ledger

**Serves:** journal TOOL-aOrientedCast-2

Direct checks only; no gate, suite or bar ran in the pass. Every criterion ran in one fixture: a
`git clone --local` of the pass's HEAD at `%TEMP%/t2c`, with the working `handoff.py` copied in and a
committed `zFixtureCast` build (a README naming `ids: TOOL-zFixtureCast-1`, a spec whose H1 defines
it, and a brief record in the kickoff checker's brief shape), a scratch card holding a filled
eight-field `## task`, a `## route` and a READY line, and, for AC6 and AC10, a card the clone's
kickoff checker wrote with `--card --write --session t2fx` and filled with `--card --append` (exit 0,
`0 unverified`). Each arm ran GREEN on the pristine script and RED on a break staged by a patch
script that refuses a replacement matching other than once, restored after each; 18 RED
observations in all. Two arms could not be told apart by their own break, and the lines say so:
AC11's name check is backed by the role-reads check, and AC6's default-card equality cannot go red
on a fixture where a guessed path equals the printed one. At the pass's base no renderer existed.
AC8's first half also ran in the worktree, on the real workflow table. The close owes the
`roles catalogue` leg, `codebase-map coverage + freshness` for the dossier and the regenerated
map, `lexicon naming predicates`, `encoding posture`, `install-prefix`, `python resolver`,
`remote literals`, `spec tokens`, `recall floor`, `recall floor arms` and `memory hygiene`.

**Evidences:** TOOL-aOrientedCast-2
- AC1 — `### card:route` — two `--stdout` renders were identical under `cmp`; line 1 read `**Serves:** journal TOOL-zFixtureCast-1`, the marker named `role=gov-builder` and `unit=TOOL-zFixtureCast-1`, and the blocks ran `input:spec`, `card:route`, `brief:non-goals`, then `charter §3`, `§7`, `§9`, `§11`, `§12`. RED: the reads loop reversed printed `brief:non-goals` first; a timestamp in the opening sentence made two renders differ.
- AC2 — `-2-builder.md` — the first render printed `…-prompt-TOOL-zFixtureCast-1-1-builder.md`, the second `…-1-2-builder.md`, and `check` exited 0 on each, printing both hashes. RED: `<n>` pinned to 1 made a third render print the first file's path, overwriting it.
- AC3 — `task-sha` — a byte edited in the opening sentence exited 1 naming `task-sha`; a byte edited in the role's first sentence exited 1 naming `role-sha`; an unedited copy under another name exited 1 naming `path`. RED: with the comparison removed, the task-edited file exited 0.
- AC4 — `check` — after the file was rewritten with 180 CRLF line endings by the criterion's command, `check` exited 0 and printed the same path and both hashes it printed before. RED: with the read's CRLF fold removed, the same file exited 1, no marker line found.
- AC5 — `brief:goal` — with the brief record moved out, the gov-spec-writer render exited 1 naming `brief:goal`, the four other brief keys, and the `prompts/` folder it searched; the same render without `--stdout` also exited 1 and the folder's listing was unchanged under `cmp`. With a second record carrying both headings, it exited 1 naming both files and `--input prompt=`. RED: refusal disabled exited 0; the ambiguity check disabled exited 0.
- AC6 — `Not supplied, optional:` — with `CLAUDE_CODE_SESSION_ID` unset and no `--card`, the gov-session render exited 0 with one line, `Not supplied, optional: task:todo, card:route — no card: CLAUDE_CODE_SESSION_ID is unset and no --card was given.`; with the variable set to `t2fx`, the output carried `### task:todo` and `### card:route`, and was byte-identical to a render given `--card` with the path the checker's `--card --path` printed. RED: the line suppressed dropped both keys silently. The default-card equality has no separable break here.
- AC7 — `--part task --stdout` — the output equalled the marker line, a blank line and the `## Task` section of a full render taken at the same state, and the criterion's hash probe printed `1b902fcc631a`, the marker's `task-sha`. RED: the part built from the file's head instead compared False.
- AC8 — `skeptic` — `tier2-review`, `unattended-build` and `unattended-unit` printed exactly the three objects the criterion states, in the worktree and the fixture, and `nope` exited 1; with the fixture's `spec-review` entry mapping `skeptic` to `gov-synthesizer`, `tier2-review` exited 1 naming `skeptic`. RED: the conflict check disabled printed an object and exited 0.
- AC9 — `CHARTER` — the `### charter §11` block equalled the 1518-character body `extract_charter_sections` reads from `AGENTS.md`; with the conf's `CHARTER` line deleted, render exited 2 naming `CHARTER`. RED: a block cut to its first line compared False; the charter defaulted instead of resolved exited 0.
- AC10 — `### task:todo` — over the appended card the block held `Render the handoff, then check it.` without its qualifier; with the stored To-do value edited to `…`, the block was absent and `Not supplied, optional: task:todo.` named it; with the clone's gov-session role reading `task:todo` without `?`, render exited 1 naming `task:todo` and the card path. RED: qualifier stripping disabled leaked `(the steps in order, …)` into the block; the placeholder test disabled rendered `…` as a value.
- AC11 — `input:diff` — `--input foo=x` exited 2 naming `foo`; `--input diff=a..b` exited 2 naming `input:diff` as a key gov-builder does not read; `--input spec=` naming a scratch file outside the clone exited 1 naming the path; `--unit TOOL-zOtherCast-1` exited 2 naming the slug mismatch. RED: the reads check disabled exited 0 with `diff`; the slug check disabled exited 0; the containment check disabled died on a ValueError naming no key; the name check disabled still exited 2, caught by the reads check.
