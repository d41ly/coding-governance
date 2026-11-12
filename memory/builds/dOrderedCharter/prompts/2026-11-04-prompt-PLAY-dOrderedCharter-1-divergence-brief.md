**Serves:** research PLAY-dOrderedCharter-1

# Brief: unit 1's divergence — a render with no policy kit, and three gaps beside it

## The prompt

> execute keeping the build unattended

— owner, 2026-11-03. Unit 1's builder (run wf_7c7b2cc1-8ab) returned `DIVERGENCE:` before writing anything, against rev-7 at
`bf29d6667`. The tree holds only spec 3's two untracked prompt records.

## The brief

### Goal

Revise spec 1 so each conflict below is resolved and its builder can build it as written.

### Items

1. **A target with the renderer and no policy kit.** S4, section 5's error line and AC8 refuse any `PolicyRefused` other than the
   derived default. `read_policy_value` also raises it when no policy kit is found.
   - `tools/govkit/matrix.py#SCRATCH_KITS` installs the playbook kits with no policy kit, and `apply` renders the shipped template
     there. `tools/playbook/kit.toml` requires only `playbook`.
   - So once the template carries `{{PRACTICES}}`, S4 refuses that render, and section 7's `govkit acceptance matrix` and
     `playbook render wiring` legs cannot pass.
   - Decide by the fork rule. The options: (a) S4 and AC8 name "no policy kit found" as a second case taking the `foundation` set
     with its own note, as `read_one_line_cap` keeps its default when no kit exists, with no new dependency; (b) `playbook-render`
     requires `policy` and `SCRATCH_KITS` widens, a new edge on the adoption surface that the build method's second veto may
     reserve to the owner. Recommendation: (a). Record the loser in section 8.
2. **Two more refusals to classify.** The builder's probe saw `refs/heads/main names no commit` from a target that is no git
   repository, and the same line from a repository on `master`; neither is `DERIVED_WHY`.
   - Say whether each counts as "any other" and refuses, or takes the set.
   - Read how `apply` and the matrix's scratch install reach the render before deciding, so the ruling holds on both paths.
   - AC8 names the ruling.
3. **The `cross-os` row.** S6 says the row "gains `legacy`", while section 3's edges to units 41 and 55, and unit 55's S3, say this
   pass lands no such key. The edges are right: `render` refuses a current-major template carrying a legacy block's fence, and the
   template keeps `when:cross-os` around the Toolchain section, so the key would break AC4.
   - S6 drops the clause.
   - Without the key the `retired` path in `render` does not fire, so S6 states how its note is produced, and that a v4.5 template
     with no `cross-os` fence does not take the `no when fence` refusal.
4. **The parity pair.** `tools/check-playbook-parity.sh`'s `verify-agent total` pair reads the `[bound]` digit from the template.
   Once that line moves to `practices.toml` its extraction matches nothing, and `playbook parity`, a section 7 leg, reds.
   - S5 names the stated side's new home, `${PB_DIR}/practices.toml`.
   - Files touched gains `tools/check-playbook-parity.sh` and `tools/check-playbook-parity.test.sh`, whose fixture and AC4 arm plant
     the line in the template.
   - Files touched also gains `.governance/instructions.lock`, whose `template` field moves to v4.5.
5. **The reader's call.** Section 3 and unit 15's hands-off edge say the reader calls `tools/playbook/instructions_edit.py#resolve_practices`,
   but S4 does not. That module loads the memory-tree kit at import, so a set value on an install without memory-tree raises
   `LookupError`. S4 names the call and says how that case refuses.

The builder's probe also settled two questions. `charter.practices = ["practice.yagni"]` committed reads back with source `file`,
so tags are admitted and S8's `usage` need not wait on dGroundRules. `charter.practices = []` refuses with `this set is never
empty`, as AC8 expects. Its script is the scratch file `probe_policy_read.py`; the path is in the run's return.

Read the whole spec before editing, and fix any other clause that reads the old state. Then re-read each item against the tree:
this is the unit's second chance, and a third handback costs a builder.

In the spec:

- Bump the **Status:** rev by one, dated 2026-11-04, with the status kept `DEFERRED`.
- Add one history line naming this brief, with the S and AC ids it touched.
- Each listed `path:line` citation stays byte for byte, and new text cites code as `path#symbol`, outside the acceptance
  bullets. An acceptance bullet spells a plain tracked path, with no `#` and no `HEAD:` prefix.
- A `python -c` path in an acceptance bullet takes spaces around it, as `open( 'a/b' , 'rb')`.
- New text names a section in words, and names a check by what it checks.
- Any retirement word in section 2 owes its Readers clause.

### Acceptance

- Spec 1's rev is 8, and each of the five items is resolved in it, the forks in section 8.
- `tools/check-playbook-parity.sh`, its test and `.governance/instructions.lock` are in Files touched.
- S6 carries no `legacy` clause.

### Gates

The spec-token check before return, as your role runs it. The main loop live-sweeps the spec before its dispatch.

### Non-goals

- No code.
- No edit to any spec but spec 1; name any neighbour a ruling moves in your return.
- Nothing under spec 3, which another writer holds on a scratch copy.
