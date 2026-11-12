# dOrderedCharter — unit 76's builder return

**Serves:** journal PLAY-dOrderedCharter-76

Run wf_7e7cc909-b51, summarized from its return.

- Built at rev-1 as pass commit `8b16e46fb`, with no hand-back. The scope is what PLAY-dOrderedCharter-37's spec deferred to a later
  commit, plus unit 37's lint reds; an earlier attempt at it as unit 37's later commit was refused because reopening CLOSED spec 37
  made a token of its acceptance live.
- What the unit landed:
  - The units reference row and page, each reference row's `unit` field, and each reference, concept and task page's unit line.
  - The docs leg's unit-line check, its `unit-lines` plant and its govkit selftest cases.
  - The `unit-usage` class row, and one shared CRLF-safe row removal both unit plants call, with its `row-removal` plant.
  - Both help legs enforcing `principle.p42`, the layers grant for the renderer's docs-leg probe, and the step gate's page pointing at
    the class listing.
- Observed by the main loop after the pass: the layers check, the core meta-check and the tags check each report no red; the reference
  check renders its pages with none drifted; `gov_tag.py show doc.reference.units` resolves; pinned-facts is green (DERIVED at
  8b16e46fb).
- One refusal site has no arm: the unit-line check's refused state when the `unit-usage` class is registered and the `unit` class is
  not. It is owed to the close.
- Owed at the close: RED then GREEN for the docs selftest's `unit-lines` cases, the `unit-usage` step-gate case and the `row-removal`
  plant; the step-gate plant with and without its row; the docs leg over the tree.
