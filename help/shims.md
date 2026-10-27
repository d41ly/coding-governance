# Forwarders for a moved path

**What it is.** When gov moves a command, a hook path or a module import, the old path keeps working
for a while as a **forwarder**: a small generated file at the old path that forwards every call to
the new one. Your scripts and hooks keep running while you move them over, and the forwarder tells
you where the surface went. Gov has moved no surface yet, so no forwarder ships today.

## What you see when you call a moved path

The call runs exactly as before: the forwarder passes every argument, your stdin and the target's
exit status through unchanged. What it adds depends on `install.on-shim-call` in your
`.governance/policy.toml`:

| Value | What a call does |
|---|---|
| `warn` (the default) | prints one line on stderr naming the old path, the new path, and that the forwarder is held only until its deprecation window closes; and adds one line to the journal |
| `journal` | adds one line to the journal and prints nothing |

```toml
[install]
on-shim-call = "journal"
```

The value is read from your **committed** policy at its landed revision, never from your working
tree, so an uncommitted edit changes nothing until it lands. An unset key reads `warn`. When the
policy cannot be read (an invalid value with no valid revision behind it, or no policy kit in the
install), the forwarder reads `warn`, its stderr line adds `(the policy could not be read, so this
reads warn)`, and the call still forwards: a forwarder never blocks a call.

## Where the journal is

One JSON object per call, appended to the file `git rev-parse --git-path govkit/shim-calls.jsonl`
names in the repository the call runs in, under the git directory, so a call never dirties your
working tree:

```json
{"utc": "2026-10-23T10:00:00Z", "shim": "memory-tree/hygiene-entry", "from": "tools/memory-tree/check-old.sh", "to": "tools/memory-tree/check-memory-hygiene.sh", "mode": "warn"}
```

It records the time, the forwarder's id, both paths and the mode, and never the call's arguments, so
a secret passed on a command line stays off disk. A call outside a git work tree journals nothing and
says so on stderr.

## How long a forwarder is held

Gov keeps a forwarder until `install.deprecation-window` releases (0, 1, 2 or 4; default 2) have been
cut since the commit that landed it, and holds every forwarder while no release has been cut at all.
No release has been cut yet, so every forwarder is held. Gov's `govkit selfcheck` refuses a forwarder
marked closed before its window allows it. Move your calls to the new path before then: once the
window closes, a later release may take the forwarder away.

## For gov's own maintainers

A moved surface is one `[[shim]]` row in `tools/govkit/shims.toml`; `python tools/govkit/shims.py
--write` renders its forwarder and `--check` reds one edited by hand. `--fixture --plant
<sh|js|py|module|window|parity-edit>` builds a scratch repository and prints what a forwarder did.
