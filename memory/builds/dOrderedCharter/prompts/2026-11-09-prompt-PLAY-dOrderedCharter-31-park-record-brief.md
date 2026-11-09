**Serves:** research PLAY-dOrderedCharter-31

# Brief: spec 31 — record the third hand-back's two blockers as forks for the owner, and end its pass

## The prompt

> why are the specs being reviews (and 11 times at that) instead of building?

— owner, 2026-11-09. Unit 31 was deferred after its third hand-back, but its open dispatch row still reserves eleven paths that
PLAY-dOrderedCharter-37 needs, and `--dispatch` refused unit 37 for it. A pass releases its reservation when a commit carrying its
`Pass:` trailer writes inside its declared set; this revision is that commit's content, and the blockers belong in the spec anyway.

## The brief

### Goal

Record in spec 31's section 8 the two blockers its third hand-back found, each as a fork OPEN for the owner, so the spec says why the
unit stopped and what answers it.

### Items

1. **F10 — the agent-instructions entry leaves while gov's own deploy still selects it.** Removing the kit's registry entry refuses gov's
   own install, because `.governance/deploy.toml` still lists `agent-instructions` among its kits, and that file is guarded against agent
   writes. Options: (a) the owner drops `agent-instructions` from gov's deploy kits before or with the pass; (b) the selection resolver
   reads a retired id through its `[[retired]]` row, a new mechanism; (c) the entry leaves only at the landing. OPEN for the owner.
   Relate it to F4, which already rules who writes gov's `deploy.toml` when the step runs on gov.
2. **F11 — `check-microformats` requires `playbook-render`, which the default selection lacks,** so every default install refuses.
   Options: (a) add `playbook-render` to the default selection; (b) drop `check-microformats` from it; (c) change the leg's subject.
   Each changes what every adopter installs by default. OPEN for the owner.
3. Confirm both against HEAD with a read; cite code as `path#symbol`. Say in F11 that the builder's finished step program and partial
   patch are kept outside the tree for the pass that resumes once F10 and F11 are answered.

In the spec:

- Bump the **Status:** rev by one, dated 2026-11-09, status kept `DEFERRED`, with one revision-log line naming this brief and saying
  no design text moved.
- Edit nothing outside section 8, the Status line and the revision log. Every new fact is pinned, keyed or marked PINNED or DERIVED;
  name a unit by its id. No function name is minted.

### Acceptance

- Spec 31 carries F10 and F11, each OPEN for the owner with its options, and a rev-12 log line; nothing else in the spec moved.

### Gates

None run: the main loop sweeps the spec before its commit.

### Non-goals

- No code, no design change, no edit to any other file.
