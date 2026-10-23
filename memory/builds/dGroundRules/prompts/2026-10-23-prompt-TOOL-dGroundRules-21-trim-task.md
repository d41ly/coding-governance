**Serves:** research TOOL-dGroundRules-21 TOOL-dGroundRules-25 TOOL-dGroundRules-34 TOOL-dGroundRules-64

# Writer task — bring units 21, 25 and 34 under the spec ceiling, and unquote unit 64's suite-shaped tokens

The closing review's binding line adds a generated records row of about 1.2 KB to every spec of this build, and
three specs now exceed the 49152-byte spec ceiling the spec-tokens leg grades: unit 21 at 50726 bytes, unit 25 at
49590 and unit 34 at 50372. Bring each to at most 48800 bytes, measured with `wc -c`, AFTER its rev bump and its §9
line are added. Change no meaning: shorten prose, drop repetition between sections, compress a resolved §8 fork's
discussion to its decision and its reason, and never touch the status header's fields other than the rev, a binding
line, a hands-off or consumes-from edge, an acceptance criterion's command, or the generated records region between
its markers.

Unit 64's §6 also carries three bare `` `selftest.py` `` tokens, which the spec-tokens bar join reads as a suite
invocation. Unquote those three mentions (prose `selftest.py` with no backticks), keeping meaning. Unit 64 is rev-1 and
uncommitted, so it takes no rev bump.

- Write sets: the four spec files named above, and nothing else.
- Do not commit; run no gate but memory hygiene. Temporary files go under `C:/Users/DAILY-~1/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unattended-dgroundrules-0e6f4a/b814b019-d9ae-4d0f-83be-8b1c25fb814d/scratchpad`.
- Return each file's final byte count and rev, and one line per spec on what you shortened.
