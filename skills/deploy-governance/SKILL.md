---
name: deploy-governance
description: Install this repo's governance kits into a target repository — the playbook, the kickoff manifest and its ratchet, the memory tree, the codebase map, memory-recall, and the rest — using the govkit deployer rather than by following a prose runbook. Use when the owner wants a repo wired for governance, when an existing install needs verifying, or when a partly-adopted target needs finishing. Do NOT use to change what the kits themselves do; that is ordinary work in this repo.
---

# Deploying the governance chain

**Run `govkit`. Do not follow `WIRE-INTO-PROJECT.md` step by step.** That runbook is narrative: it
prescribes destinations for kits that have since moved, and following 66 imperative steps by hand is
how a target ends up with kits in several homes and no record of what it took. The deployer reads the
same facts as DATA, from a registry it asserts against the tree on every run.

Everything below is `python tools/govkit/govkit.py <verb>`.

## The order, and why it is this order

```bash
python tools/govkit/govkit.py selfcheck
```

First, always. It asserts gov's own house before you touch anybody else's: every registry entry has a
descriptor, every declared source exists, every version claim agrees with the repo's own version gate,
every hole carries a runnable discharge probe, and every tracked path in the deployable surface is an
entry, a member of one entry, or an exemption with a reason. If this reds, stop — you are about to
deploy from a tree that disagrees with itself.

```bash
python tools/govkit/govkit.py intake --target <path> [--kits a,b | --all] [--answer key=value ...]
```

Writes `<target>/.governance/deploy.toml` ONCE. It refuses to invent an answer and names the ones it
wants; supply each as `--answer key=value`. It also refuses to overwrite a descriptor that already
exists, because that file is the standing authorization for an unattended re-run — replacing it
silently would replace a decision the owner made with one the tool guessed.

Commit that file. It is the thing that makes the next `apply` reproducible.

```bash
python tools/govkit/govkit.py plan --target <path>
```

Read-only. Lists every destination the install TOUCHES, one row per path, with its role, its mark and
the source commit, and leaves the target byte-identical. **Only a `write` row says govkit puts bytes
there.** `SIDE` means a step `apply` runs produces it, `ORDER` means something outside `apply` must
supply it, `COVER` means a sibling rule writes that same path, `BLOCK` means `apply` refuses the
install over it, and `UNRES.` means the destination still carries an unanswered token and is not a
path. The legend prints above the rows. Read it before applying — this is the last cheap moment to
notice a destination you did not expect, and the last cheap moment to notice one you expected and are
not getting.

```bash
python tools/govkit/govkit.py apply --target <path>
```

Lands kit content from the gov git INDEX at a recorded commit — never from the working tree, which is
what makes the receipt's provenance claim true — then stages everything it wrote, then runs each kit's
adopter. It writes `<target>/.governance/install.json` and a flat `install.sums` a target verifies
with bash alone.

**The receipt is at schema 3, and each landed row carries TWO identities.** `gov_oid` is the git
blob gov shipped at that row's `commit`; `oid` is the blob the target holds, read from its INDEX
rather than from worktree bytes. The pair is what lets `update` tell gov's own file from one
somebody edited, without a stored flag that can go stale: `oid != gov_oid` IS the local-delta
question, asked fresh every run. Reading the index rather than the worktree is what makes this
survive a checkout filter — on a default Windows clone the old worktree comparison reported
almost every row as diverged. Rows gov does not supply whole bytes for carry NEITHER identity:
the synthesized `.gitattributes` row, the `merged` rows that are a gov-owned region inside a file
the target owns, and the unlanded `project-owned` / `generated` / `rendered` rows.

A schema-2 receipt upgrades in place on its first `update`, from gov's blob at each row's own
commit. Nothing back-fills a schema-3 receipt, because filling one in is how a merge result would
be laundered into a provenance claim.

**It does not commit, branch, push, or open a pull request.** That is deliberate and it is your job:
review what it staged, then land it the way that target lands anything.

```bash
python tools/govkit/govkit.py check --target <path>
```

Read-only. Reports each kit as not landed, landed but inert, or adopted, and RUNS every declared
hole's discharge probe. Exit 0 from an adopter means "the adopter ran", never "the kit works", so
`check` reds on an undischarged hole regardless of what any adopter exited with.

## What it will refuse, and what to do about it

| refusal | what it means |
|---|---|
| the target already carries a kit no receipt claims | converging an already-kitted repo is out of scope. A re-run over govkit's OWN receipt is fine and proceeds |
| a `merged` rule cannot be honoured | that entry writes a gov-owned region into a target-owned file, and no writer exists yet. Deselect it, or do that one by hand |
| the selected kits need answer `k` | supply it to `intake`. The tool will not guess |
| `--target` resolves to this repo | deploying into gov itself is out of scope |

## The holes are the work, and they are the point

An install is not finished when `apply` exits 0. Every kit declares its non-mechanical holes —
placeholders to fill, a taxonomy to choose, pins to MEASURE against the target's own corpus — and each
becomes an order under `<target>/.governance/outbox/`. Discharge is decided by RUNNING that hole's
probe, never by deleting the order file.

Inherited numbers are the failure mode to watch for. A pin copied from another repo is either vacuous
or permanently red, and several holes are observed by nothing at all in the target — no adopter fails,
no gate leg reds, and the kit is quietly doing less than it appears to. That is why the probes exist.

## Honest limits

`apply` prints what it could NOT do on every run rather than skipping quietly. Today that is the
`.gitattributes` block write and the gate-runner and CI wiring: neither has an implementation, so wire
those two by hand and treat the runbook as reference for them specifically. `check` cannot prove a
rendered document is CORRECT, only that it matches a fresh render.
