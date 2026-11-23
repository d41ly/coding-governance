# TOOL-dQuietDisk-14 deviation 1 — `steps` stays the receipt's last key, and an empty attested set attests nothing

**Serves:** deviation TOOL-dQuietDisk-14

- **Departs from:** `TOOL-dQuietDisk-14@rev-3` [Scope]
- **Hand-off:** spec-to-code
- **Before:** S5 says the writer sets the receipt's top-level `attestations` key and names no position for it; S3 gives one attestation to every entry whose every `kit` leg holds S2, and names no floor on the size of the attested set.
- **After:** `tools/govkit/govkit.py#write_install_receipt` puts a key new to the document before `steps`, so `steps` stays the receipt's last key, and replaces a key the document already holds in place. `tools/govkit/govkit.py#derive_kit_attestations` gives no attestation to an entry whose attested set of `(source, gov_oid)` pairs is empty, or that has no leg evidence.
- **Cause:** builder discovery
- **Reason:** `tools/govkit/selftest.py` asserts that a first `apply` and a first `adopt --write` write `"steps": []` as the receipt's last key (the `[dSP-3 AC4]` arms), so appending the key would red them while moving no other byte. An attestation over no source would let a consumer hold a leg on bytes nobody compared, and an empty population is never coverage.
- **Evidence:** the pass's scratch probe of `apply` and `adopt --write` read `steps` as the last key of a receipt carrying `attestations`, and with the key removed the `apply` and `update --write` receipts equalled the base engine's byte for byte (PINNED, that run in this pass).
- **Risk:** additive
- **Approver:** author, the builder pass, under the chain's `author-recorded` value
- **Follow-through:** ask TOOL-dQuietDisk-14
- **Caused-by:** TOOL-dQuietDisk-14
