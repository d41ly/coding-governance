# The prompt this build was started from

**Serves:** research TOOL-aReapedSpinner-1

Node `a`, 2026-09-08. Handed as `--prompt` with the prose inline. The value carried whitespace and
named no readable file, so by the Skill's resolution table it is the prompt itself and the bytes
below are that value verbatim rather than a reference to a file that could be edited after the run
began.

---

Gate runner has a fatal flaw - it doesn't properly monitor its processes or their children. Another
session did a sweep and found this:

"Your 8-hour tasks are alive. So are a lot of things that should have died.

* Two spin loops of mine, 11.4 hours old, 46,221 CPU-seconds between them — 12.8 core-hours. They're
  `until grep -q ... ; do :; done` with no sleep, waiting on `u10.results`, a file from an A/B I
  superseded hours ago. They will never be satisfied. One of them is pegging a full core right now.
* Nine `check-unattended.test.sh` processes alive. I started one.
* Five Monitor greps from 52–61 hours ago — 2.5 days, parents long dead, still holding pipes.
* The `run-unattended-gates` runner I stopped with TaskStop 7.5 hours ago is still running, along
  with its sweep and kit runners."

Those are just some examples of the hanged tasks. **What every attended AND unattended session needs
both in this repo and its adopters is a proper MONITOR that can identify, report, and KILL hung
up/idle non-progressing tasks and report that to the session**. You need to DESIGN a flexible
solution to this problem that will easily integrate with any adopter and build it.

---

## Reading it

**What the owner asked for, in the order the sentence puts it.** IDENTIFY, REPORT, KILL, and report
THAT to the session. Four acts, not three: the last one is separate, because a kill nobody is told
about leaves the session still believing its job is running.

**Two scopes, both stated: this repo AND its adopters.** That fixes the deliverable's shape before
any design work — it is a KIT under `tools/`, with a descriptor, an adopter and a conf, not a script
wired into this tree's own gate runner. The charter's §12 already says kits are the kind here.

**"Flexible" is read as DECLARED, not as configurable.** The variance between adopters is which
paths their agent work lives under and how aggressive they are willing to be about killing; both are
declarations a target writes once. It is not read as a plugin architecture, which nothing in the
prompt asks for and which would be the over-build.

**The opening sentence names the gate runner, so the gate runner is in scope** — but the four
examples are not gate legs. Three of the four were launched by an agent directly (two spin loops, a
Monitor pipeline, a hand-run suite) and the fourth outlived a `TaskStop`. So the gate runner is one
instance of the class and not the class itself, and a fix scoped to it would leave three of the four
observed failures standing.

## What was NOT asked, and is therefore out

- Any change to how the harness's own `TaskStop` behaves. It is not this repo's code. What is in
  scope is compensating for it, which is what the sweep observation actually demands.
- Scheduling, retrying or restarting anything that was killed. The prompt says identify, report and
  kill; resurrection is a different product.
- A daemon. Nothing here asks for a resident process, and a resident process is the one design that
  would itself become an entry in the population it watches.
