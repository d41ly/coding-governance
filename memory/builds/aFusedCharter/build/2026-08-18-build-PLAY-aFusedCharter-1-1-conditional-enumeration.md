# The conditional-block enumeration — measured against the FOLDED ruleset

**Serves:** journal PLAY-aFusedCharter-1 DEPL-aFusedCharter-1

`PLAY-aFusedCharter-1` S8 makes this enumeration its first deliverable, ahead of writing any fence.
The reason is in the spec: the companion's conditional list cannot be carried over, because S6 moves
seven kit-advertisement bullets out of the ruleset entirely and a row whose block has left has
nothing to fence. Round 2 of the spec audit left the post-fold set explicitly open for this reason.

Measured on the converged file at 43 722 bytes, after S1–S7 and S10.

## What the companion's list said, and what survives

| Companion row | Disposition | Why |
|---|---|---|
| codebase-map lines (four sites) | **fence `kit:codebase-map`** | three sites survive the fold as RULE clauses inside `§1` and `§7`; the `§5` bullet left under S6 |
| memory-recall line | **gone** | it was the `§5` kit bullet, moved to the runbook under S6 |
| unattended-run lines | **fence `kit:unattended`** | the landing clause survives in `§1`; the companion block folded in |
| drift-audit bullet | **gone** | moved under S6; the RULE it left behind names no kit and is unconditional |
| agent-instructions bullet | **gone** | moved under S6; same |
| pytest-parallel-guardrails bullet | **gone** | moved under S6; same |
| gate-lint bullet | **gone** | moved under S6; same |
| govkit bullet | **gone** | moved under S6; same |
| naming-lexicon lines | **fence `kit:lexicon`** | five bullets folded into `§12` from the companion, plus the stub clause |
| `§9` outbound-call / stored-HTML lines | **fence `when:security-outbound`** | no registry entry names a security surface |
| `§11` whole | **fence `when:cross-os`** | no registry entry names an operating system |
| `§4` harness lines, `§13` entirely | **no subject** | both sections are DELETED outright by S2 and S4 |
| `§15` persona | **NOT a fence** | the row is an EDIT instruction, not a drop; a fence would delete the voice section instead of adjusting it |
| memory-tree | **never fenceable** | marked REQUIRED; `§5` and `§6` are written against it |

## The declared set

Three `kit:` names and two `when:` names. Every `kit:` name is a real entry id in
`tools/govkit/registry.toml`; neither `when:` name is, which is why the second namespace exists.

```
kit:codebase-map
kit:unattended
kit:lexicon
when:security-outbound
when:cross-os
```

**Round 1's justification for the second namespace was wrong by half and this table is why.** It
counted four project-property rows. Two of them point at sections this unit deletes outright, so they
have no subject, and a third is an edit instruction that a fence would turn into a deletion. Two
survive.

`DEPL-aFusedCharter-1` S3 declares these five as `[[block]]` rows in the `playbook` descriptor, and
S4 validates every fence in the file against that declaration. A fence naming something absent from
this list is a refusal, and a declared name that fences nothing is a refusal too.
