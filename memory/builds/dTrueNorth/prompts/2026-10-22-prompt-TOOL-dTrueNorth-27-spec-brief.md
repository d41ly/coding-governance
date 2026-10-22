**Serves:** research TOOL-dTrueNorth-27

# Spec brief — TOOL-dTrueNorth-27, the nine bar reds the build caused

## The prompt

> The plain merge bar at f4b9849c9, run after every unit closed, reds 9 of 68 legs, each caused by this build's diff. Its log is `memory/builds/dTrueNorth/build/2026-10-22-build-TOOL-dTrueNorth-27-bar1.log`. One unit clears them all before the close.

## The brief

### Goal
Author TOOL-dTrueNorth-27, one Tier-2 unit whose pass turns each of the nine red legs green, fixing the cause in code wherever a fix exists and raising a declared ceiling or pin only where the build's own design makes the count grow. Author only: no product code, no commit, no gate.

### Items
1. `kickoff-manifest ratchet`: `memory/guides/SESSION-KICKOFF.md` check 9, the manifest body unchanged across ten watched commits. Its §B gains the bullets this build makes true (the carries join and coverage region, the deviation record kind and join, the audit pin, the as-built view), each a pointer, and `last-body-change` and `last-audit` advance by the manifest's stamp rule.
2. `shell hygiene (a loop fed by a command substitution)`: `check-memory-hygiene.sh` measures 10 `<<<` sites against a registry of 8. Remove the two new sites rather than raise the row.
3. `shell hygiene (a fork spent on builtin work)`: six registry rows exceeded (check-memory-hygiene.test.sh printf-subst 19 to 22 and var-pipe 48 to 51; unattended.sh pure-fn-subst 41 to 42 and var-pipe 60 to 61; unattended-build.test.sh printf-subst 66 to 68 and var-pipe 62 to 65). Rewrite each new site in its no-fork form.
4. `spawn budget (forks per hot entrypoint)`: memory-hygiene measures 191 forks against a ceiling of 189. Cut the two forks the new checks added; raise the ceiling only if no fork can go, and then by the rule its file declares.
5. `install-prefix (shipped surface)`: the literal kit paths in `tools/check-spec-tokens.py:357`, `tools/check-spec-tokens.test.sh:1633`, `tools/memory-tree/deviation_join.py:1068,1148,1149` and `tools/memory-tree/gen_build_index.py:6122-6206`. Derive each from the file's own location or `resolve_kit_dir`, as the leg's message says; there is no waiver.
6. `harness arms`: `unattended.sh` check 49 branches 23 and 24 carry no positive assertion the arms gate can match (branch 23's message embeds `$(readme_of "$slug")`, whose inner quotes cut the extracted text; branch 24's needs reading), and the driver's census is 323 against `REFUSAL_CEILINGS` 319. Arm both branches; the ceiling rises 319 to 323 only through the retirement review the memory-tree README states, with the dated decision id `TOOL-dTrueNorth-28` (mint its `memory/DECISIONS.md` row), taken under the standing ruling ER:388 (`PLAY-dClosedLoop-6`), `widens: REFUSAL_CEILINGS`, recorded as a deviation.
7. `drift-audit records`: `non_terminal_specs_cited_by_product_source` names `PLAY-dClosedLoop-1`, which product source now cites (the as-built view's head names the instrument's filename); remove the cause without breaking the view's byte parity with the instrument, or, if parity forces the citation, say so and take the narrowest remedy. `cutoff_keys_armed` reads 36 against a pin of 34, the two keys this build adds by design (`SPEC_CARRIES_CUTOFF`, `SPEC_AUDIT_PIN_CUTOFF`): the pin rises to 36 under the same ruling and decision row, recorded as a deviation.
8. `remote literals`: `deviation_join.py:62,140,719,1199` spell `origin`; resolve the remote through the gov lib's ladder, inlined as the leg demands.
9. `govkit selfcheck`: a sentence in `deviation_join.py` says `update` re-renders without naming `GOVKIT_RERENDER`; reword it as the check asks.
10. The spec carries `**Derived:** PLAY-dClosedLoop-2`, `order 11`, Tier-2, status OPEN, path `memory/builds/dTrueNorth/spec/2026-10-22-spec-TOOL-dTrueNorth-27.md`, and one AC per item naming the leg's own command run as a probe on the touched files where a probe exists; the merged bar at the close is what grades the legs.
11. Write the deviation records: `memory/builds/dTrueNorth/build/2026-10-22-build-TOOL-dTrueNorth-27-deviation-28.md` for the unit itself (Departs from `dTrueNorth [roster]`, design-to-spec, builder discovery, additive, spec writer under author-recorded, `new unit TOOL-dTrueNorth-27`, Caused-by `PLAY-dClosedLoop-2`), and one record per raised ceiling or pin (numbers 29 onward), each loosening, approver author citing ER:388 (`PLAY-dClosedLoop-6`) under author-recorded, with `**Surface:**` naming the ceiling.

### Acceptance
`python tools/check-spec-tokens.py` prints no hit on the spec; every AC is a probe a pass can run; every record reads with no malformed field under `python tools/memory-tree/deviation_join.py`.

### Gates
No gate runs in this pass; the spec's §7 names the nine legs and every leg its files trip.

### Non-goals
Any other spec; product code; a raise where a code fix exists; a waiver row; inside §6, an untracked file named by full path inside a backticked token.
