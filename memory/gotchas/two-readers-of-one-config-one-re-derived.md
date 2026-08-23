---
name: two-readers-of-one-config-one-re-derived
description: one reader of a config file re-parses what the others source, so a legal spelling gives the guard a value nothing can match while it reports itself armed
kind: class
---

# One config, two readers, and only one of them is the file's own language

## Symptom

A config file has a language — it is sourced, or parsed by a library, or read through one helper. One
reader somewhere resolves a key out of it with a private pipeline instead: `sed -n 's/^KEY=//p' | tr -d
'"' | head -1`, a regex, a hand-rolled split.

Every legal spelling the private pipeline does not model is a divergence:

| the line | what the file's language yields | what the pipeline yields |
|---|---|---|
| `KEY='v'` | `v` | `'v'` — `tr -d '"'` strips only double quotes |
| `KEY="v"   # note` | `v` | `v   # note` |
| `KEY=a` then `KEY=b` | `b` — the last wins | `a` — `head -1` takes the first |

None of those is exotic and none of them errors. The guard downstream keeps running, over a value
nothing can ever match, **and reports that it ran**.

## Where it bit

`tools/unattended/check-playbook.sh`, round 7 of `dScriptedRepeat`. `.unattended.conf` is a sourced
shell file; `unattended.sh`, `check-unattended.sh` and `adopt-unattended.sh` all `. "$CONF"`. One line
in the playbook leg resolved `BYPASS_BAN` with `sed | tr -d '"' | head -1`.

With `BYPASS_BAN='--no-verify'` — legal shell, and the spelling a careful author reaches for — the
leg greps every tracked evidence record for the seven-character string `'--no-verify'` including its
quotes. A record literally containing `--no-verify` took the leg from **RC=1 to RC=0**, and it still
printed `bypass scan - 3 tracked evidence record(s) read for the declared flag`. The write-time guard
kept working, because it sources; so the both-ends pair the charter asks for on a guarded surface
silently became one end, and the only signal a reader got said the scan ran.

The kit's threat model makes it worse than a bug: the run being guarded can commit that conf line
itself.

## The fix

Read the key the way the file's own language does. For a shell conf, source it in a subshell so
nothing leaks into the reader's state:

```sh
_conf_key() { [ -f ./.unattended.conf ] || return 0
  ( . ./.unattended.conf >/dev/null 2>&1; eval "printf '%s' \"\${$1:-}\"" ); }
```

If re-parsing is deliberate — a checker that must not execute its subject — keep it AND compare it
against the authoritative read, redding on any difference. Two answers to one question is only safe
when something is asserting they agree.

**Arm the parse as well as the read.** No bypass flag contains whitespace or a `#`; a resolved value
that does is a reader that mis-parsed, and an unarmed predicate must RED rather than print a
population count over a literal nothing can match.

There is **no machine gate** yet. The documented check, and the gate worth writing: enumerate every
reader of a config file in the kit's own source and refuse any that resolves a key by a pipeline
rather than by the file's language. That is the same shape as the parser byte-compare this kit already
runs one file over.
