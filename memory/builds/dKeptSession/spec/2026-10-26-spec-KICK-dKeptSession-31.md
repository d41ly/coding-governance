# KICK-dKeptSession-31 — the message id derived over its recipient and its content key, so two legitimate notices never share one id

**Status:** OPEN · rev-2 · 2026-10-26 · node a · Tier-2 · base 462d20f3 · streams kickoff · order 16 · advances KICK-dKeptSession-29

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md](../build/2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md) | journal | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-30 KICK-dKeptSession-32 KICK-dKeptSession-33 KICK-dKeptSession-34 KICK-dKeptSession-35 KICK-dKeptSession-36 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-39 KICK-dKeptSession-40 KICK-dKeptSession-41 KICK-dKeptSession-42 KICK-dKeptSession-43 KICK-dKeptSession-44 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-51 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-54 KICK-dKeptSession-55 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-61 KICK-dKeptSession-62 KICK-dKeptSession-63 |
| [2026-10-26-build-KICK-dKeptSession-31-deviation-311.md](../build/2026-10-26-build-KICK-dKeptSession-31-deviation-311.md) | deviation | — |
| [2026-10-26-review-KICK-dKeptSession-30-spec-audit.md](../reviews/2026-10-26-review-KICK-dKeptSession-30-spec-audit.md) | spec-audit | KICK-dKeptSession-33 KICK-dKeptSession-34 KICK-dKeptSession-40 KICK-dKeptSession-32 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-30 KICK-dKeptSession-36 KICK-dKeptSession-39 KICK-dKeptSession-35 KICK-dKeptSession-42 KICK-dKeptSession-43 KICK-dKeptSession-41 KICK-dKeptSession-44 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of this build's spec set
(`memory/builds/dKeptSession/reviews/2026-10-26-review-KICK-dKeptSession-1-spec-audit.md`)
confirmed finding **id 54 at BLOCKER**, report item **B2**. Id 4 is the same defect, found by the
coherence lens at HIGH, item H3, and promoted as `KICK-dKeptSession-35`. Fixing one item fixes the
other, and the two units split the fix: this unit changes the id, and unit 35 changes the notices
that post through it.

`KICK-dKeptSession-22` S2 derives a message id from six fields: build, item, pass, kind, subject and
answers. Neither the recipient nor the content key is one of them. `KICK-dKeptSession-7` S4 posts one
`confirmed` per dependent with one subject and no item or pass, so the second dependent's notice
carries the first one's id and `check_mail_duplicate` refuses it, rc 1. Every `changed` after the
first collides the same way. dKeptSession has two child builds, so this is the main path. This unit
adds the recipient and the content key to the id. It repairs `KICK-dKeptSession-22` and builds one
step after it (order 16).

## 2. Scope (IN)

- **S1** — id 54. The id, eight fields. `derive_message_id <build> <item> <pass> <kind> <subject>
  <answers> <to> <content-key>` in `tools/unattended/unattended.sh`: `derive_gov_id` over the eight in
  that order, each absent one written `none`, so two messages differing only in recipient or only in
  content key carry two ids. It still takes no session and no time. `KICK-dKeptSession-22` S4's act
  joins as the ninth field. Observed by AC1, AC2 and AC4.
- **S2** — id 54. The call. `KICK-dKeptSession-5` S5's `--mail post` passes its `--to` value as
  `<to>` and `none` as `<content-key>`. `KICK-dKeptSession-27` S3 computes the content key from
  `--interface` before the id and passes it as `<content-key>` (§3 Edges). Observed by AC3.
- **S3** — id 54. The retry stays refused. Equal fields, the recipient and key included, are still
  one message, so a post retried after a crash, from this session or another, is refused exactly as
  `KICK-dKeptSession-22` AC3 and AC4 state. Observed by AC4.
- **S4** — id 54. The sibling text superseded by name. `KICK-dKeptSession-22` S2's "six fields" and
  AC2's "any one of the six fields", and `KICK-dKeptSession-5` S5's six-argument call, read eight
  fields from this unit's landing. Each is answered in that unit's acceptance ledger. Observed by AC1.
- **S5** — id 54. The verbs guide's mailbox section, `tools/unattended/VERBS.template.md` and its
  rendered `memory/guides/UNATTENDED-VERBS.md`, names the eight fields. Observed by AC5.

## 3. Non-goals (OUT)

- The notices themselves, their pass and their failure line: `KICK-dKeptSession-35`, the H3 half.
- The content key's computation and the `--interface` option: `KICK-dKeptSession-27`'s.
- The reader's collapse of a cross-ref race: `KICK-dKeptSession-5` S6's, unchanged.
- The report's left-shift checklist entry, that every dedup key names every field telling two
  legitimate messages apart. No clause of this build names that checklist; AC2 is its arm here.

### Edges

- **consumes-from** `KICK-dKeptSession-22` — `derive_message_id` and its six-field derivation, to which this unit adds the recipient and the content key (id 54)
- **consumes-from** `KICK-dKeptSession-5` — `--mail post`'s id step in S5, whose call this unit amends to pass `--to` (id 54)
- **hands-off** `KICK-dKeptSession-27` — the eighth field, `<content-key>`, which that unit's `--interface` computes before the id and passes in place of `none`
- **hands-off** `KICK-dKeptSession-35` — the eight-field id, through which every per-dependent notice lands as its own message
- **hands-off** `KICK-dKeptSession-51` — the eight-field `derive_message_id` and S4's superseded list, which that unit completes with the act's ninth position (id 39)
- **hands-off** `KICK-dKeptSession-56` — the eight-field id, whose act position the batch's S8 observes (id 8)

## 4. Design

### Evidence

- `KICK-dKeptSession-22` S2 lists the six fields, and its §5 risks line says equal fields make one
  message by design (spec-22 lines 35-37, 120-121).
- `KICK-dKeptSession-7` S4 posts `confirmed` to `build:<dependent>` with subject `interfaces <slug>`
  and no `--item` or `--pass`, and S5 posts `landed` with subject `landing <slug>` (spec-7 S4, S5).
- `KICK-dKeptSession-27` S3 adds `content-key` as a record key and never as an id field.
- `KICK-dKeptSession-5` S4's header carries only `gov-mail <slug>/<id>`, so the duplicate check
  cannot tell two recipients apart once their ids agree.

### The cases

| Case | Differs in | Before | After |
|---|---|---|---|
| one Design exit, two dependents | `to` | the second refused, rc 1 | two ids, both posted |
| two Design exits, one dependent | `content-key` | the second `changed` refused | two ids |
| a retried post | nothing | refused | refused |

### Inventory

No identifier is minted. `derive_message_id` gains two positional fields.

### Migration

None. No message exists before this build, so no stored id changes.

### Files touched (estimate)

- `tools/unattended/unattended.sh`: `derive_message_id` and `--mail post`'s call
- `tools/unattended/unattended.test.sh`: the arm in §7
- `tools/unattended/VERBS.template.md`: the id's fields
- `memory/guides/UNATTENDED-VERBS.md`: the rendered guide

### Alternatives rejected

- **The recipient in the subject.** It makes the subject carry routing, and every caller must
  remember it; one field in the derivation covers every caller.
- **A distinguishing `--pass` alone.** It separates exits but not two dependents at one exit unless
  every caller invents a per-recipient pass.

## 5. Production-readiness checklist

- security — the two fields are values the post already validated, `--to` through
  `check_mail_recipient`; neither reaches a ref name.
- perf / scale — two more NUL-terminated fields in one `git hash-object`.
- error / empty / loading states — an absent field is `none`, as for the other six.
- observability — the posted line names the id; a refused duplicate names the ref holding it.
- risks — a caller passing a varying recipient spelling for one recipient mints two ids; the
  recipient is the grammar `check_mail_recipient` admits, one spelling per target.
- testing — the arm in §7, staged against the six-field id.
- migration — none.
- user docs — the verbs guide, S5.

## 6. Acceptance criteria

The fixture is `KICK-dKeptSession-22`'s scratch repository under `%TEMP%`, with a bare origin and
`RUN_CLAIMS=on` for AC3.

- **AC1** — When a probe sources `unattended.sh` and runs `derive_message_id fx none none confirmed
  'interfaces fx' none build:dA none` and the same with `build:dB`, the two 12-hex ids differ; with
  `build:dA` and the content keys `k1` and `k2`, they differ again.
  Red when: the six-field id, as a planted copy shows, prints one id for both recipients.
- **AC2** — When the probe derives ids for the four pairs of `build:dA` and `build:dB` with `k1` and
  `k2`, it prints four distinct ids.
  Red when: any two legitimate notices share an id.
- **AC3** — When `bash tools/unattended/unattended.sh --mail post fx --to build:dA --kind confirmed
  --subject 'interfaces fx' body.txt` runs and then the same post with `--to build:dB`, both exit 0
  printing `mail — posted`, with two different ids.
  Red when: the second post exits 1 with `mail — duplicate`.
- **AC4** — When AC3's first post is run again, unchanged, it exits 1 with `mail — duplicate`.
  Red when: the retry lands, so the added fields broke `KICK-dKeptSession-22`'s refusal.
- **AC5** — When `grep -n "content-key" UNATTENDED-VERBS.md` runs in `memory/guides/`, the mailbox
  section's id paragraph names the recipient and the content key among the eight fields.
  Red when: the guide still lists six.

## 7. Gates

`unattended kit gate` · `recall floor` · `recall floor arms` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/unattended/unattended.test.sh · covers AC1 AC2 AC3 AC4 · two recipients at one exit, two keys to one recipient and an unchanged retry, staged against a copy of the driver carrying the six-field id · `FLOOR_ASSERTIONS` and its shard floor rise by the arm's count, counted off the diff

## 8. Open questions

- **F1 — How are two legitimate notices told apart?** Options: (a) the recipient and the content
  key as id fields; (b) the recipient in the subject and a per-exit `--pass` at every caller; (c) a
  per-recipient ref. (b) repeats the fix at every caller and misses any caller that forgets. (c)
  contradicts `KICK-dKeptSession-5` S1's one ref per writing session. (a) meets AC1 to AC4 at the one
  derivation every caller shares. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the
  skeptic's sound fix. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit's B2 (id 54).
- rev-2 · 2026-10-26 · §3 · the Edges bullets to `KICK-dKeptSession-51`, `KICK-dKeptSession-56`
  mirrored, the other ends of the edges the round-1 promotions' audit's disposal declared

## 10. Reuse audit

The seam extended is `KICK-dKeptSession-22`'s `derive_message_id` over its shared `derive_gov_id`, the
one id derivation every post calls, so no second derivation is minted. `python
tools/codebase-map/reuse_lookup.py "derive a stable id from fields by hashing so a retry is refused
as a duplicate"`, unit 22's own probe, ranked `derive_clause_hash` and `derive_baseline_additions` by
name stem; neither hashes a message, and no mail code exists at this base, so unit 22's spec is the
seam.

Recall terms used: `python tools/memory-recall/query.py "how is a retried mailbox post refused as a
duplicate" --terms "message id derive_message_id recipient content-key duplicate confirmed changed
dependent notice collision"`
