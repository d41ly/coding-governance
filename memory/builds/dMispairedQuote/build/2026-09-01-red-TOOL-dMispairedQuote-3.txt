# The staged-RED observation for TOOL-dMispairedQuote-3

**Serves:** journal TOOL-dMispairedQuote-3

Every arm below was run against a tree WITHOUT this unit's code, so its failing case was
observed before it landed. Verbatim `bash tools/hooks/agent-cap.test.sh` output.

```text
FAIL no-regress: a backtick inside a regex, above a multi-line cap-50 call -> deny (exit 0, want 2)
FAIL no-regress: an exposed backtick leaks the template mode -> deny (exit 0, want 2)
FAIL no-regress: a quoted URL inside a same-line template -> deny (exit 0, want 2)
FAIL no-regress: control, the same three shapes without the apostrophe -> deny (exit 0, want 2)
FAIL no-regress: a renderShipped* body has drifted from BASE
FAIL no-regress: a denial the BASE hook made is gone
---- 140 passed, 6 failed ----
FAIL no-regress: a backtick inside a regex, above a multi-line cap-50 call -> deny (exit 0, want 2)
FAIL no-regress: an exposed backtick leaks the template mode -> deny (exit 0, want 2)
FAIL no-regress: a quoted URL inside a same-line template -> deny (exit 0, want 2)
FAIL no-regress: a DOUBLE-quoted URL in a template does it without an apostrophe -> deny (exit 0, want 2)
FAIL no-regress: a renderShipped* body has drifted from BASE
FAIL no-regress: a denial the BASE hook made is gone
---- 140 passed, 6 failed ----
```
