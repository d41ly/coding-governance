# dOrderedCharter — unit 75's builder return

**Serves:** journal PLAY-dOrderedCharter-75

Runs wf_6dd260c0-c46, wf_dda81470-7b0 and wf_accda91f-6da, summarized from their returns.

- The first run was cut off mid-dispatch by an interrupted session, with nothing written.
- The second built spec 75 rev-1 in full, but the pre-commit fork check refused the CLOSED commit: section 8 F2 carried no resolution
  mark. It saved the pass as a patch and restored the tree. Spec 75 rev-2 at `a7d937b25` added the mark and moved no design text.
- The third re-applied the saved pass and committed it as pass commit `8198bad3f`.
- What the unit landed:
  - The tags leg's selects join in `tools/playbook/tag_index.py` grades a namespace only once some unit's `scope` names one of its
    tags, and prints an unarmed line until then.
  - The `unscoped-unit` plant in `tools/playbook/gov_tag.py` with its adopter row, and `help/tags.md` and the playbook README saying
    the new arm.
- Observed by probe: the plant reds with the old arm restored and passes with the new one; the `dead-selector` plant still reds.
- Observed by the main loop after the pass, AC1: `python tools/playbook/gov_tag.py check` exits 0 over the tree, printing the `reader`
  and `practice` joins unarmed and no selector red (DERIVED at 8198bad3f).
- Owed at the close: RED then GREEN for the `unscoped-unit` adopter row, and the legs its gates section lists.
