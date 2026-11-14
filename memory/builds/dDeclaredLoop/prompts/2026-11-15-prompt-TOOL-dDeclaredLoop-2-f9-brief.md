**Serves:** research TOOL-dDeclaredLoop-2

# Brief: rewrite spec TOOL-dDeclaredLoop-2 rev-5 on fork F9's option (b)

## The prompt

> drop spec-audit: from this build's README and from the run's pinned fact; rearm the unattended session and continue

— owner, 2026-11-13. The re-ground writer of TOOL-dDeclaredLoop-2 wrote rev-5 into the working tree with fork F9 recommending
(a), guard-self binding on a live run's branch, which it names as a narrowing of the owner's 2026-11-12 ruling that no file is
owner-only to a run. An unattended run does not narrow an owner ruling, so the run takes F9's option (b): the run admission
precedes guard-self, as the ruling reads.

## The brief

### Goal

Rewrite the uncommitted rev-5 of `memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-2.md` in place so its body
follows F9 option (b), keeping it rev-5 with its one revision-log line, extended to say F9 follows the owner's ruling.

### Items

1. Change every sentence, scope item, acceptance criterion, fixture and section 5 line that rests on F9 (a) so it rests on (b):
   on a live run's branch the run admission precedes guard-self, and a run may change `policy-file.guard`,
   `policy-file.proof`, the `floor` members and the guarded paths list, each with its change record.
2. In section 8, end F9 on `Recommendation (b)` with its reason, the owner's 2026-11-12 ruling, and leave the RESOLVED mark to
   the run. Leave F8, F10 and F11 as they stand.
3. Say in section 5 what (b) leaves unchecked: a live run can switch a floor member off, and only its change record and the
   push check witness it.
4. Keep the unit one mechanism, its carries, its order and its status. Write only that spec file. Do not commit and do not
   regenerate any index. Run the spec-token checker with its spec flag over the spec and fix every hit until none remains. Do
   not run the whole-tree memory hygiene gate, and do not ask any checker for its help text. A by-name reader in a Readers
   clause is a tracked path, never `path#symbol`.
5. Never kill a process you did not start, and never match processes by a script's name to stop them.

### Acceptance

- No sentence of the spec rests on guard-self binding a live run's branch, and the spec-token checker reports no unwaived hit.

### Gates

- memory hygiene and spec tokens, at the close.

### Non-goals

- No product code, no sibling spec, no new unit.
