# The night pass two: the owner's seven points, worked unattended

**Serves:** research PLAY-dClosedLoop-1

While two review runs read the last three folds, the owner reviewed the Flow and Role layers' adoption piece, answered
its forks, and then handed over seven points to be worked unattended through the night. This record holds the words,
what the design held on each point, the research, the design worked in, and the forks parked for the owner's return.

## [words] The owner's words, 2026-10-19

> I'm stepping away for the night, you will continue this pass unattended until fully my points are fully reviewed. Go through each of them separately, one after another, understand them and their fit into the current design. Run agents/workflows at medium effort to assist you in research and design, park all the forks for me to go at for when I return.
>
> ### Review points
> 1. Continuing our review of the Flow and Role Layers - how flexible is it to introduce new workflows, processes and roles? Currently, we're designing against a baseline loop scenario of 5 steps (+review) and a set number of Roles doing work across those steps but how flexible the loop is to accomodate for sub-scenarios? Case: an edge case is identified which requires its flow steps to be in different order, new roles added and inserted into the flow. How easy is it for the current design to accomodate? Is it possible to define additional work scenarios in the flow and for the runtime to pick one (or several) based on the work it's driving (eg. one scenario for design work, another for developing a mobile application, third for coding a high-precision data system)? Is it possible to create and adapt scenarios on the fly and record them after? Pick scenarios from a pre-shipped set and build scenario pipelines? Modify and reshape workflows (case: single agent; a set of parallel agents; a workflow of a single step; a workflow of 2 or more steps; a mix or different roles in a workflow; variable agent caps)? 'Lenses' are simple prompt instructions, so how easy it is to add or remove a 'lens'? Does all this functionality converge in a cohesive method?
>
> 2. Another build, aScoutedSeam, has finished running its reuse workflow experiment and merged its findings to Gov's origin/main. Particularly, it was able to achieve 94% test cases solved through two important methods - workflow shape and prompt-writing rules. I believe, its findings can apply to the entire core Gov's layer to improve work accuracy across Flow and Role layers. Read 'memory/builds/aScoutedSeam/prompts/2026-10-19-prompt-DEPL-aScoutedSeam-1-1-session.md' on Gov's origin main, review aScoutedSeam's findings, apply it's best performing workflow shape and prompt writing principles to work in the design.
>
> 3. Instruction and Memory layers - is it time to find a different data format and storage implementation as opposed to the current plaintext/markdown structure? Is there a more efficient, relational structure that would be able to mechanically maintain connections between data points in large adopting repos? If a build was to occur across several nodes at the same time, how would they efficiently coordinate and update each other on completed work, decisions taken, problems encountered in real time? We'd previously decided on a mailbox approach but this isn't a long-term solution, and definitely not an efficient one. Would using an actual relational cloud database be a viable solution? Or is there a more agent-friendly approach?
> 4. In continuation of the previous point - is there a handoff system between agents, between sessions? Effective communication between automated systems and agens is paramount to producing higher-quality work and Gov is being architected exactly for this purpose. How will agents shape and pass data between each other, how will it move between different sessions potentially working on different pieces of the same build?
>
> 5. Instruction caps. Currently, many documents - charter, methods, protocols, prompts, etc.. have caps enforced on them by Gov. The idea is great - to prevent them from growing out of control, bloating the read path. However, this is already a blocking point in many builds, and agents keep relaxing the caps. Let's take a different approach for our design - remove any hard-caps and make them advisory instead of blocking. Row/KB size limit policies can still be owner-defined, but a single enforcing switch is set to WARN by default instead of refuse. Research and recommend a better implementation for this, if there is any.
>
> 6. Gotcha lookup doesn't perform its job currently - it's good for filing gotchas and looking them up but it's purpose - serve gotchas relevant to the ongoing work that an agent or a session may trip isn't served. Agents may call on gotcha orientation several times per session and still never catch the right one. How can this tool take a more useful shape? Can this functionality move to orientation agents? Or runtime? If there is no way to make this more efficient, it's better to retire this functionality.
>
> 7. Tooling issue - agent-cap.js is currently broken and doesn't perform its function (instead of capping agents at 5 max, it limits spawns to 5 every 45 minutes). This tool must be retired, and agent limits must be owner-adjustable by policy, governed by the runtime? or the which layer is appropriate for this task?
>
> ---
>
> Don't stop until you've worked out each point, once you have - prepare a report for me on this and a resulting state of the project, and park all the forks for me to go at once when I return. Run tier2 reviews on the folds twice.

## [method] How the pass runs

- **One point at a time.** Each point gets its own section: what the design already holds, what the research found,
  the design worked in, and its forks. Research runs ahead in waves, since a point's design waits on its returns.
- **Research.** Researchers run at the owner's medium effort, read-only, one question each. Each handoff is in
  `prompts/`, and each return is saved verbatim beside this record. Agent-cap admits five direct spawns at a time, so
  the questions go out in waves of at most five.
- **Forks.** Each fork's first option is the recommendation. The design as folded shows the recommendation, marked
  pending on its fork, as the first night pass did. The `NT` family numbers them.
- **Reviews.** The night's folds are reviewed twice, as two independent Tier-2 runs compared defect by defect, and
  the defects are folded before the report.
- **Bounds.** No product code, no merge and no push, as the build's brief says; the design map and the atlas are
  regenerated after each design change.
