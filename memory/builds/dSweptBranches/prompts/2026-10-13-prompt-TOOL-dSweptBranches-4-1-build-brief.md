# Build brief — TOOL-dSweptBranches-4

**Serves:** journal TOOL-dSweptBranches-4

Built INLINE by the main loop, before unit 3, whose write mode calls this remover.

`remove_worktree` takes git's removal first, GNU `rm -rf` second, and removes a surviving directory
only when a walk that follows no link finds no regular file in it. It spawns no `readlink`, never
reaches for `cmd rmdir` or .NET, and reports a busy directory without failing on it. The arms run
in-process with the module's git and `rm` seams replaced where a failure must be staged. This node
creates symlinks, so the skeleton fixture carries dangling MSYS-style links. No merge bar.
