**Serves:** research TOOL-dPlacedRequest-8

# Brief — dPlacedRequest: TOOL-dPlacedRequest-8's divergence, resolved

## The prompt

> /unattended dPlacedRequest

## The brief

### Goal

TOOL-dPlacedRequest-8's builder returned a DIVERGENCE (run `wf_9d18223e-8ce`) and committed nothing: AC4 wants the
seed-write plant's backslash-separated Files-touched path to come out in forward-slash form, but S4 sends write-set
through S5's `--path-tokens` verb, and S5 moves `tools/unattended/unattended.sh#read_files_touched`'s token rule out
unchanged in output; that rule keeps only words of letters, digits, dot, underscore, slash and dash, so a backslash
token never reaches the normalisation (the builder's probe kept the plain and `./` forms only). It also found six
smaller defects. Revise the spec to the main loop's rulings.

### Items

1. F-backslash. Add to §8, resolved: "What does the seed read make of a Files-touched path spelled with backslashes, when S5 moves the token rule out unchanged?" (a) AC4's plant drops the backslash path and keeps the plain path and its `./` duplicate; (b) S5's rule admits a backslash and folds it to a slash, changing what `read_files_touched` reads; (c) the loop reads Files touched itself, which §4 Alternatives already rejects. Mark `RESOLVED (agent, 2026-11-20, delegated): (a), rung 3; the one token rule stays as it is, and a spec's Files touched is written with slashes everywhere in this tree. widens: none · relaxes: none`. Amend AC4 and its plant to it.
2. AC2: count the items of §4's table as the tree has them (thirteen, every one present in `tools/loop/loop.toml`), and pin the figure.
3. AC7: count the paths of §4's Files touched that pass the token test as the list will stand after this revision, and pin the figure.
4. §4's data model: state that the `widens` order is the value set of `seed` and `map` and that no `values` key is written, since `tools/playbook/overlay_rows.py#FIELD_KEYS` allows only `name`, `shape`, `ref`, `fixed-by` and `widens` and `#check_schema_keys` refuses any other key.
5. §4's table: the Actor column for `item.design.reason` reads `role:gov-spec-writer`, as `tools/loop/loop.toml` has it.
6. §4 Files touched gains the paths the change needs: `tools/unattended/SKILL.template.md`, `.claude/skills/unattended/SKILL.md` and `tools/template-size-limits.txt` (check 26 of the unattended kit gate requires the new `--path-tokens` verb in the Skill, with the size row raised under that file's run-raise terms and a DECISIONS row the main loop commits); `tools/unattended/VERBS.template.md` and its render `memory/guides/UNATTENDED-VERBS.md`; `tools/unattended/unattended.test.sh`; and `tools/loop/kit.toml` if S5's new reach from `tools/loop/loop_lib.py` to the driver is one its comment block records (verify against that block).
7. Re-cite `read_files_touched` and `resolve_ask_path` and every other stale line citation in the revised sections as `path#symbol`.

### Acceptance

Spec 8 at its next rev carries the resolved fork, AC2, AC4, AC7 and §4 amended, the added paths in Files touched,
`path#symbol` citations, and one §9 line naming this brief and the divergence; `check-memory-hygiene.sh --only 12,25
--spec` and the spec-token checker over it report nothing.

### Gates

The memory hygiene gate (`--only 12,25 --spec`), the spec-token checker and the naming lexicon; no other.

### Non-goals

No product code, no commit, no index render, no status flip (it stays INPROGRESS), no spec other than
TOOL-dPlacedRequest-8. Pin every figure you write with DERIVED or PINNED, never let a section sign or a section
number stand before a unit word, never write a bare file-stem section reference, and never quote a check's hit
literally in prose.
