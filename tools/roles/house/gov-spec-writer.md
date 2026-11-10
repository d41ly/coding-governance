Before you return, check each spec you wrote or revised with the spec-token checker's one-spec mode,
where this repository holds `<prefix>/check-spec-tokens.py`, `<prefix>` being its tool root:
`python <prefix>/check-spec-tokens.py --spec <the spec's path>`. That run grades your one spec and is
not a gate leg. The checker run with no `--spec` is the gate leg, and it stays refused to you.
Exit 1 prints one `spec-tokens: HIT` row per miss: fix each one your spec's own text can fix, then
run the check again. A hit your spec's text cannot fix goes in your return, with its row.
Exit 2 means the checker refused the path: name the refusal in your return.
