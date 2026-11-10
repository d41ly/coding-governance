Before you return, check each spec you wrote or revised with the spec-token checker's one-spec mode,
where this repository holds `<prefix>/check-spec-tokens.py`, `<prefix>` being its tool root:
`python <prefix>/check-spec-tokens.py --spec <the spec's path>`. That run grades your one spec and is
not a gate leg. The checker run with no `--spec` is the gate leg, and it stays refused to you.
Exit 1 with hits prints one `spec-tokens: <spec path> [<kind>]` row per miss, naming its token,
then a `spec-tokens: <N> unwaived hit(s)` summary. Fix each miss your spec's own text can fix, then
run the check again. A hit your spec's text cannot fix goes in your return, with its row.
A `spec-tokens: REFUSING` line, an exit 2, or an exit 1 with no summary line is the checker
refusing, not a hit: name it in your return.
