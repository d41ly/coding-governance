# PLAY-dOrderedCharter-20 deviation 204 — `--mode symlink` on a host that cannot link, as built

**Serves:** deviation PLAY-dOrderedCharter-20

- **Departs from:** `PLAY-dOrderedCharter-20@rev-9` [Design]
- **Hand-off:** spec-to-code
- **Before:** the spec's migration says rendered bytes do not change, the scopes reproducing today's outputs. On a Windows host with no symlink privilege the shell adopter's `ln -s` under MSYS deep-copied the canonical and reported `(symlink)`, so `--mode symlink` left `CLAUDE.md` a copy of `AGENTS.md`.
- **After:** the renderer's `os.symlink` raises there and takes the fallback the shell adopter already carried for a failed link: a claude alias gets its `@AGENTS.md` import, any other alias a copy, and the run prints the fallback line. Every other mode, and `--mode symlink` on a host that can link, gives the bytes it gave.
- **Cause:** builder discovery
- **Reason:** the difference is MSYS's `ln`, never the adopter's logic: moving the logic into python leaves that emulation behind, and the kit README already promises a fallback where a link cannot be made. Reproducing a deep copy that reports itself as a symlink would write a false line.
- **Evidence:** a scratch script ran the adopter at HEAD and the new one over sixteen scenarios: fifteen agreed on exit, file set, bytes and output, and `symlink` differed on `CLAUDE.md` alone on this host. `.github/copilot-instructions.md` is a copy under both.
- **Risk:** additive
- **Approver:** author, the unit's builder, recorded in this pass commit under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** ask PLAY-dOrderedCharter-38
- **Caused-by:** PLAY-dOrderedCharter-20
