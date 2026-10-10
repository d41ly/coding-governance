# aRoutedQuill — asks

## Asks
- TOOL-aRoutedQuill-8 · filed 2026-10-10 · run the routed-against-raw trial TOOL-aRoutedQuill-6 specifies, in an attended session: it needs four owner asks and an approved budget, so its own spec never runs it under the unattended driver, and the aRoutedQuill run carried it forward unbuilt · seen `memory/builds/aRoutedQuill/spec/2026-10-09-spec-TOOL-aRoutedQuill-6.md` matching `THE PILOT` · accept the trial's pilot and its full set run in an attended session with the owner's budget, observed by a committed result record under this build's `build/` folder that grades both arms blind
- TOOL-aRoutedQuill-13 · filed 2026-10-10 · the `--dispatch` order gate (check 49) counts a sibling whose spec reads DEFERRED, carried forward by a `--rescope defer` row, as an unfinished earlier step, so a run that carries one unit forward cannot dispatch any unit ordered after it; this run had to re-order four promoted units onto the deferred unit's step to dispatch them · seen `tools/unattended/unattended.sh` matching `neither terminal nor dispatched` · accept a unit ordered after a DEFERRED sibling that carries a rescope defer row dispatches, observed by an unattended suite arm that defers one unit and dispatches a later-ordered one

## Dispositions
- SEV · TOOL-aRoutedQuill-8 · MED · the build's claim that routing improves code stays unmeasured until it runs; no wrong verdict
- KEEP · TOOL-aRoutedQuill-8 · the run handoff of 2026-10-09 rules the trial attended-only, so the unattended run carries it forward under UNATTENDED-STOPS.md section 15
- SEV · TOOL-aRoutedQuill-13 · LOW · costs a re-order and a spec rev per blocked unit; no wrong verdict
- KEEP · TOOL-aRoutedQuill-13 · found by the aRoutedQuill run on 2026-10-10 and declined for adoption: the fix is a gate-semantics change to the unattended kit, outside this build, and its gain is not measured
