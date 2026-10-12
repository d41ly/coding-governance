**Serves:** research KICK-aOrientedCast-1 KICK-aOrientedCast-2 PLAY-aOrientedCast-1 TOOL-aOrientedCast-1 TOOL-aOrientedCast-2 TOOL-aOrientedCast-3 TOOL-aOrientedCast-4 TOOL-aOrientedCast-5 TOOL-aOrientedCast-6 TOOL-aOrientedCast-7 TOOL-aOrientedCast-8

# The M2 cross-read of the eleven specs at 64c4d7ec0, and what the main loop decided from it

A read-only `Plan` agent ran the handoff `prompts/2026-10-11-prompt-TOOL-aOrientedCast-1-3-cross-read.md`
on 2026-10-11, after a first attempt was cut off by the session limit. It found twelve disagreements,
one open fork, three criteria that run a whole gate script, and no `§6` path the token checker would
red. Each finding names the one document that is wrong.

## The twelve disagreements

| # | Axis | Wrong document | Disagreement |
|---|---|---|---|
| 1 | interface | KICK-aOrientedCast-2 | The router's unit dispatch carries no `roles`, so the builder spawns untyped. |
| 2 | interface | TOOL-aOrientedCast-4 | It adds `builder` to `unattended-build`'s pinned keys without raising a fork. |
| 3 | interface | TOOL-aOrientedCast-7 | It has no consumes-from lines for TOOL-4, TOOL-5 and KICK-2. |
| 4 | ordering | TOOL-aOrientedCast-7 | It lands on a precondition no unit delivers: the unattended verbs passing `roles`. |
| 5 | scope | TOOL-aOrientedCast-4 | The build harness's spec-audit call runs untyped, so spec review sits outside role agents. |
| 6 | interface | TOOL-aOrientedCast-1 | `enforced-by` names the spawn guard for `handoff` and `spec-review`, which it never sees. |
| 7 | interface | TOOL-aOrientedCast-6 | Its refusal's render command omits the required `--build`. |
| 8 | interface | TOOL-aOrientedCast-7 | S8's render command omits the required `--build`. |
| 9 | interface | TOOL-aOrientedCast-8 | F1 keeps `review-harness` optional, which the catalogue checker and the agent render both refuse. |
| 10 | interface | TOOL-aOrientedCast-6 | An edge states the builder prompt's conditional behaviour as unconditional. |
| 11 | ordering | TOOL-aOrientedCast-8 | Its header and Rollout say order 8, against the ratified order 7. |
| 12 | acceptance | KICK-aOrientedCast-2 | No criterion runs the attended dry run the build's acceptance names. |

Three criteria run a whole gate script rather than one arm: TOOL-4 AC5 and AC6, and TOOL-5 AC2,
each run `check-protocol-parity.test.sh` in its check mode. TOOL-3 AC9 and TOOL-8 AC9 run
`test_codebase_map.py`. Each is one bar leg, not the bar, and they are kept.

## Decided by the main loop (M3, M2)

- **`PLAY-aOrientedCast-1` F1: option (a)**, the order swap. `TOOL-aOrientedCast-8` builds at 7 and
  `PLAY-aOrientedCast-1` at 8. It moves two headers and no content, so it is the option with the
  fewest open questions.
- **Findings 1, 2 and 4 take one resolution: a new unit, `TOOL-aOrientedCast-9`.** The unattended
  Skill and verbs pass `roles` from `handoff.py harness-args` to every harness call. `unattended-build`
  forwards `builder` through `dispatch.args`, so interface 10 gains that key, and the catalogue's
  stages table and `harness-args` print it. The new unit is inside brief item 5 and the
  owner-confirmed goal, "attended or unattended". Without it, the two guards refuse every untyped
  unattended builder from their landing, gov's own concurrent runs included. It was recorded with
  `--rescope add`.
- **Finding 5: the build harness's audit call forwards `specFinder`, `skeptic` and `synthesis`** to
  `tier2-review`. That is the most feature-rich option, and it puts spec review inside role agents as
  the brief requires.
- **Finding 9: the absent harness becomes a `note` rather than a refusal.** The catalogue checker's
  R9 and the agent render's S3 admit a harness the tree does not hold, with a `note` line naming
  it, rather than making `review-harness` a new requirement of every adopter install. A new install
  requirement for every adopter is a public-surface change that M3's veto 2 reserves for the owner.
- **Every other finding is fixed in the one document the cross-read names.**
