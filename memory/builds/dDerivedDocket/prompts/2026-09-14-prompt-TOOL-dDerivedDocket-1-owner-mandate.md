# Owner mandate — dDerivedDocket

**Serves:** none — this is the owner's verbatim prompt with the questions and rulings that scope it,
the authorization this run asserts. It precedes every spec in the build, so it names no spec id.

## Provenance

Handed to `/unattended` as the `--prompt` value on 2026-09-14, node `d`, as the owner's answer to
"how do you want to proceed" at the end of an attended design session (session `2588f719`). The
value carried whitespace and named no readable file, so it is the prompt ITSELF and is recorded
verbatim below. No path of origin exists to record.

## The prompt, verbatim

> Open build, write specs, execute per the protocol

## What it refers to

The build that session designed and the owner ratified. The design is filed in this build folder as
`build/2026-09-14-build-TOOL-dDerivedDocket-1-design.md`, which maps every design label to a unit id.
The owner's own words that scoped it, verbatim and in order:

1. "Explain to me the entire mechanics of backlog maintenance and management in this repo and its
   adopters - how does it work? Is there any tooling used? What are the instructions?"
2. "How do we make sure that backlog is MECHANICALLY derived and actual backlog entries are stored by
   each build in a non-conflicting session? For example, in the build folders which are later
   mechanically read? How to better manage backlog statuses?"
3. "One risk should be additionally mitigated - pre-adoption Unmerged branches. A guard needs to be
   included that will instruct older branches to relocate their logs appropriately if there are any."
4. "The key part here - old branches exist OUTSIDE of just this node and may be merged LATER."
5. "In addition to your two risks previously described: Ids already defined elsewhere [...] Slugs
   without a build [...] Unattended kit needs to be brought in scope to ensure that there is enough
   information to just point an unattended session (prompt or slug) at the ids/slug to thoroughly
   execute a build to completion."

## The rulings, as the owner answered them

Each was put as a question with options, and the owner chose. "rec" marks the recommended option;
the design record's sections 17, 20 and 22 carry the consequences.

- **Round 1 (2026-09-13).** D1 adopt per-build asks with a derived view (rec). D2 same-id pairs not
  linked by default, owner signs the list (rec). D3 report-only live count (rec). D4 **REOPEN
  allowed**, cancelling a NAMED closing record (rec for the follow-up rule). D5 DEFERRED names a
  release id (rec). D6 **closeout is a gate from the switch-over, retroactive, sweep first**. D7
  **severity rows now, forward-only**. D8 delete the backlog archives after the proof (rec). D9 keep
  grading ask paths (rec). D10 drain unmerged branches first (rec). D11 a pre-adoption straggler
  guard, made fleet-wide and permanent at the owner's emphasis.
- **Round 2 (2026-09-13).** D11-b remote CI plus no squash/rebase PR merges (rec). D11-c keep
  direct-push landing, CI detects after (rec). D12-a **ids runs always start from an owner-landed
  README**. D12-b **asks-disposed is overridable**. D12-c KEEP only after partial work (rec). D12-d
  new asks must be runnable (rec). D12-e probe commands only from an allow-list, shipped empty (rec).
  D12-f a filing-home target builds in a new folder (rec). D12-g check 13's skip only pre-cutoff
  (rec). D12-h **unattended self-tests lifted for the ask-driver units**. D12-i **the kit's own stop
  causes are inside this build**. D12-j authority only from an owner-committed README (rec).
- **Round 3 (2026-09-13/14).** D12-i1 in-place landing (rec). D12-i2 LANDED derived from the
  remote (rec). D12-i3 **keep "land on local main first", with an unattended exception**. D12-i4
  inherited red may land, age-bounded (rec). D12-i5 **ABSORB wider than the write set**. D12-i6 a
  retry pass counts, tracked (rec). D12-i7 **GATE_WALL hand-set**. D12-i8 extend the self-test lift,
  baseline first (rec). D12-i10 adopt the method carriers (rec). D12-i11 self-protection built first
  (rec). D12-i12 CI also runs held suites and publishes verdicts (rec).

## The single owner turn (prompt path, step 2), verbatim answers

- The switch-over needs the D2 signature, the D6 sweep signature and the D10 all-node drain, none of
  which an unattended run can get: **"Delegate to this run"** — the run signs both tables under the
  mechanical rules its spec states, skips the D10 drain, and relies on the permanent transition-merge
  audit for stragglers, so the switch-over lands in this run.
- The workflow file needs a `workflow`-scoped push credential: **"Credential has scope"** — commit
  and push the workflow in this build.
- Auto-resume from HELD, after the earlier answer "opt-in, on by default": **"On everywhere"** — the
  kit ships it ON and adopters opt out. This overrides charter section 9's default-off gate for this
  one feature by owner ruling, and the build records it as a DECISIONS row rather than silently.

## What the run read into it

- "Open build" is ONE build folder, `dDerivedDocket`, holding every ratified unit.
- "write specs" is a spec per roster unit, derived from the design record and audited per the build
  method's M4 before any code.
- "execute per the protocol" is build, close and land unattended under the unattended protocol, with
  the self-protection units first so this run lands through them (D12-i11).

## What the run refused to read into it

- **No adopter migration.** Each adopter moves in a deployer build of its own; none is owed now.
- **No change to GitHub repository settings.** Disallowing squash and rebase merges is the owner's act.
- **No pull-request landing.** D11-c keeps the direct-push lander.
- **No claim on the concurrent adopter-wiring work.** A separate session is fixing how govkit writes
  the merge attribute and how the wiring check probes a flattened install. This build edits those
  arms only where its own merge-attribute addition requires it, and reconciles at landing.
