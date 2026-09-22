# The owner's prompt — the memory toolkit and its fully closed records

**Serves:** research TOOL-aThawedCorpus-1

Handed to `/unattended --prompt` on 2026-08-27, node `a`. The value carried whitespace and named no
readable file, so it is the prompt itself and is reproduced VERBATIM below. The bytes travel rather
than a reference: the build folder is the authorization, so it may not point at a file that can be
edited after the run starts.

## Verbatim

> There is a significant issue with the memory toolkit and its handling of the fully closed records.
> Reviewing this project's or the adopters' memory I'm noticing that the last modified date of the
> build dirs is always actual, even if the builds are long closed. This means that the tooling walks
> through the entire corpus every call which is A BUG. Fully closed builds and gate stamped builds
> (eg. that were verified green before) should not be the target of the tooling (cached? frozen?)
> unless they are actually reopened (status changed, specs added, files added, whatever). This
> should cut down tooling execution and gate times and reduce unnecessary load. This needs to be a
> systemic solution that applies to the current and potentially future memory-related tooling, both
> to this repo itself and its adopters.

## What the run read out of it, and what it did not

The ASK is the last sentence: a systemic reduction in what memory-related tooling costs, inherited
by adopters rather than hand-fitted to this repo. That is taken as written.

The MECHANISM is left open — "cached? frozen?" is the owner declining to pick one, which routes this
build through the build method's M12 rather than through a spec that already names a solution.

Two premises in the prompt are engaged with rather than adopted, and the engagement is recorded in
the build README's own words:

- The observation about build-directory mtimes is TRUE and was reproduced. What it implies is the
  opposite of a cache key: git does not preserve mtimes, so every clone, checkout and worktree
  resets them. A mtime-keyed cache is not merely imperfect here, it never hits.
- The inference "therefore the tooling walks the entire corpus every call" is TRUE, and the walk was
  measured. Whether the walk is what the time is SPENT on is a separate question, and this build
  measured it before choosing.

No clarification was asked. Nothing in the prompt left acceptance or gates underivable, and the
prompt path's owner turn is spent only on a gap that would otherwise stall the run.
