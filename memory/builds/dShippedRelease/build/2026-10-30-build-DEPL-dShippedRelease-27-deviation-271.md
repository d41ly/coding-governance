# DEPL-dShippedRelease-27 deviation 271 — `carries` read from the tip before the push, because the clause's range is empty once pushed

**Serves:** deviation DEPL-dShippedRelease-27

- **Departs from:** `cl-dClosedLoop-0437@b595f1f2` [carries range]
- **Hand-off:** design-to-spec
- **Before:** `carries` on the landing record, read over `<current default>..HEAD` with `--no-merges`
- **After:** `carries` on the landing record, read over `<current default>..HEAD` as it stood before the push, which is `<landing_prior_tip>..<landed sha>`, with `--no-merges`, the `landing` native-id class registered with it, a publication recorded as a release per (SHA, artifact environment), a squash handled as `commits.squash` says, re-emitting the union of trailers under `re-emit-union`, refused at the landing under `refuse` and recorded as a lossy landing under `accept-loss`, each value seen on a planted squash, and Codex install targets with their trust step surfaced at install and re-surfaced, as an attended re-trust step or an owner item, by every `update` or `kits.offer` that changes a Codex-installed hook's bytes (P33, P36)
- **Cause:** design defect
- **Reason:** `deploy.record` runs after the push, when the default branch equals the landed SHA, so the clause's range is empty on every landing. The intent is what the landing moved, and the tip before the push is the only base that yields it. Unit 12 records that tip because nothing does today (`tools/push-main.sh:956`, `:1127`). A second node, holding no such record, derives the tip as the SHA's first parent and the value says `prior-derived`, so the field can read less than the clause asks after a take-over. Also follows through as: ask DEPL-dShippedRelease-32.
- **Evidence:** scout B disagreement 8, `memory/builds/dShippedRelease/build/2026-10-30-build-DEPL-dShippedRelease-11-reuse-scout-b.md:105`; `write_lander_marker`'s line at `tools/push-main.sh:392`; shared interface I8 in the spec brief; DEPL-dShippedRelease-27 §8 F1
- **Risk:** editorial
- **Approver:** spec writer, the gov-spec-writer role of dShippedRelease's spec run, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** amends cl-dClosedLoop-0437@b595f1f2
- **Caused-by:** DEPL-dShippedRelease-27
