# What `update` does with your edits

**What it is.** `govkit update --write` moves your installed kits to a newer gov vintage. Three cases
used to pass silently; each now keeps your bytes and says what it did.

## A file you edited that gov stopped shipping

Gov retires a file, and your copy carries an edit of yours. `update` reports the row as
**`retired-edited`**, never `patched` and never `forked`, and never writes or deletes your copy,
`--write-withdrawals` included. The receipt records the row's role as `retired-edited`, and the row
keeps that role until gov ships the file again, when it returns to the role gov's kit gives it and is
graded as any file of that role. What happens next is `install.retired-edits` in your <!-- usage: policy:install.retired-edits b88bd05f -->
`.governance/policy.toml`:

| Value | What `update` does |
|---|---|
| `order` (the default) | writes one order, `.governance/outbox/update-retired-edited-<slug>.md`, and the row's line names it |
| `keep` | writes no order; the row's line says `kept, no order (install.retired-edits = keep)` |

```toml
[install]
retired-edits = "keep"
```

The value is read from your **committed** policy at its landed revision, so an uncommitted edit
changes nothing until it lands. An unset key reads `order`. A value other than the two stops the row
with a finding naming the key.

To close the row, move your edit where it belongs, then delete the file: the next `update` sees it
gone. A copy whose edit you revert reads `withdrawn` and is reported only; its role stays
`retired-edited` until your next `apply`.

A seeded file gov stopped shipping takes the same path: edited, it reads `retired-edited` and is
ordered as above; untouched, it reads `withdrawn` and is reported only, never deleted.

## A rendered file you edited since its last render

A kit's rendered file (one its regenerate argv writes) that no longer matches the bytes recorded at
its last render reads **`render-edited`**. `update` holds the whole kit back, so its regenerate does
not run over your edit (you see its `HELD BACK` line), keeps your bytes, and always writes an order,
`.governance/outbox/update-render-edited-<slug>.md`, whatever `install.retired-edits` says. Move the
edit into the kit's template or conf, restore the rendered file, and re-run `update`. A row whose
receipt recorded only the bytes its install left (no `update` has re-rendered it yet) is compared
with those bytes, line endings aside: an edit made before your first `update` is held and ordered
the same way, and a file whose only change is CRLF or LF line endings reads unedited. A rendered
file git cannot hash through its own filters, a required clean filter that fails say,
cannot be proven unedited, so it reads `render-edited` too.

## A hook gov withdrew

When gov stops shipping a hook fragment (`*.fragment.json`), `update --write` takes its entry out of
your `.claude/settings.json` (or the file `GOV_SETTINGS_JSON` names) through your own
`settings-merge.py --unwire`, before anything is deleted, and prints
`hooks: <fragment> unwired, gov no longer ships it`. The fragment file itself is deleted only under
`--write-withdrawals`, and the `withdrawn` order is written either way.

The entry stays wired, the fragment is kept and one line says why when:

- `GOVKIT_RERENDER=0` is exported, since unwiring runs code in your repository; or
- the unwire fails, for example when your receipt names no `settings-merge.py`.

If the same run rolls that kit back, the entry is wired again with the kit's files.

A hook entry you wired by hand, with no fragment row in your receipt, is never touched.
