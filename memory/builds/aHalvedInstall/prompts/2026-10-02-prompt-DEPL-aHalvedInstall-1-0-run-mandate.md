# Run mandate — aHalvedInstall

**Serves:** journal DEPL-aHalvedInstall-1

The owner's prompt, verbatim, as handed to `/unattended --prompt` on node `a`, 2026-10-02. The value
carried whitespace and named no readable file, so it is the prompt itself. The bytes travel here
rather than as a reference, because the build folder is the authorization and may not point at a file
that can be edited after the run starts.

## The prompt

> Several kit bugs have been discovered by a session trying to re-render the kit over several repos.
> Review the bug observations below, they are central to this build - you're tasked to fully work them
> out and systemically fix so they do not reoccur in any flexible form. Ground yourself in all
> memories and code relevant to this prompt. Execute to completion by the protocol, do not backlog -
> bring any findings into the build straight away. Do not reinvent any existing functionality - reuse
> and extend first.
>
> ### Observations
>
> * The unattended kit's check misses absent keys. The kit has a hole meant to catch these keys,
>   keepalive-tool-names in tools/unattended/kit.toml:321. Its probe only goes red when a key is still
>   set to the example "<...>" value. If RESUME_SCHEDULE_CREATE/DELETE are missing entirely, it passes,
>   so govkit says nothing until the render refuses. The kit's own hold-floor hole describes exactly
>   this failure as a defect.
> * playbook-render can't survive a renderer change. Neither playbook kit file declares a
>   [[regenerate]] step. So when gov changes the renderer's output, the update never re-renders
>   AGENTS.md, the kit's check sees drift, and the kit rolls back. It will do this on every renderer
>   change for every adopter. Running the render by hand fixed it.
> * govkit installs a kit half-way across a conflict. It landed the new check-protocol-parity.test.sh
>   even though the script it calls, check-verifier-fanout.sh, was left at the old version because of
>   a conflict. The old copy has no --print-cap, so the render breaks. That kit has no check, so
>   nothing rolls it back. Gov's records only cover the flag being introduced, not this.

## No owner turn was taken

Every field the kickoff checker asks for derives from the prompt and the code: each observation names
its own failing behaviour, which is the acceptance, and govkit's `selfcheck` and `selftest` are the
gates. "Do not backlog" is read as: a discovery that qualifies under protocol section 11 is adopted
into this build with `--rescope --act add`, never filed for later.

## What "do not reoccur in any flexible form" is read as

Each observation is one instance of a class, and the build closes the class where gov authors it:

1. A hole probe that only refutes a bad VALUE passes when the subject is ABSENT. The class is any
   discharge that exits 0 against a tree holding nothing; and a `[config]` required-key list that
   nothing reads is the same hole one level up.
2. A kit whose adopter writes a target artifact from engine bytes, and declares no `[[regenerate]]`,
   goes one vintage stale on every engine change. The existing gate's population was kits shipping a
   `rendered` ROW; a kit that renders through its adopter alone was outside it.
3. `update` writes a kit's rows one at a time and refuses a conflicting row alone, so a kit can land
   half its bytes. Only a kit with a `[check]` could be rolled back, and only on a green-to-red
   transition.
