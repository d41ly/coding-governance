# Research: custom instructions outside gov, and how they survive upstream updates

**Serves:** research PLAY-dClosedLoop-1

This is dispatch 120's return, verbatim, except that a title line would be demoted to keep one H1 per record. Its question is in `prompts/2026-10-19-prompt-PLAY-dClosedLoop-1-3-researcher.md`, and its use is in `build/2026-10-19-build-PLAY-dClosedLoop-1-adopter-instructions.md`.

---

I found eight families. My pick combines three of them: adopters keep their own units in their own overlay, they change gov's units through tag-keyed `amends` and `supersedes` edges with a base fingerprint, and level-2 values stay as keyed knobs. All of it is checked at update and at render. It handles S4 worst: an upstream unit under a new tag that contradicts an adopter unit passes every mechanical check silently.

I read every outside source below on 2026-10-19. "S1" to "S7" are your seven scenarios: reword of an amended unit, rename or retire, split, contradicting addition, adopter removal, budget overflow, two harnesses.

## Families

**F1. Layers joined into one text, with the model resolving conflicts.**
- **Mechanism:** each scope adds a file, the files are joined into one context, and position or wording decides between them. No machine decides.
- **Systems:**
  - Claude Code joins its files rather than letting one override another. It says "All discovered files are concatenated into context rather than overriding each other" and "if two instructions contradict each other, Claude may pick one arbitrarily". `@path` imports go at most four hops deep. https://code.claude.com/docs/en/memory
  - Codex reads one file per directory from the root down to the working directory. "Files closer to your current directory override earlier guidance because they appear later." `project_doc_max_bytes` defaults to 32 KiB, and past it Codex "stops adding files". https://learn.chatgpt.com/docs/agent-configuration/agents-md (redirected from developers.openai.com)
  - The AGENTS.md spec says "the closest AGENTS.md to the edited file wins; explicit user chat prompts override everything." https://agents.md/
  - Cursor says "All applicable rules are merged; earlier sources take precedence," in the order Team, Project, User. https://cursor.com/docs/context/rules
  - **Ambiguity:** Codex lets the later file win and Cursor the earlier one, so the direction is not consistent across harnesses.
- **When upstream changes the same item:** both texts load. The conflict surfaces silently; the only help is Claude's advisory `/doctor prompt-audit`.
- **Delta and cost:** the adopter's addition stays readable, but a change to an upstream line can only be written as a contradiction. The cost is low.
- **Against gov:**
  - Loses S1, S4 and S5 silently.
  - Loses S2 with a stale reference.
  - Loses S6 by silent truncation of the last file (Codex), which is the adopter's.
  - Loses S7 because the harnesses disagree on direction.

**F2. Keyed layers with a precedence rule per key, resolved by machine.**
- **Mechanism:** each layer sets keys, and the layer's rank decides each key.
- **Systems:**
  - git config: "last value found taking precedence", but multi-valued keys collect values from every file, and the page documents no general reset. https://git-scm.com/docs/git-config
  - ESLint flat config: "later objects overriding previous objects when there is a conflict", while some properties such as globals are merged. https://eslint.org/docs/latest/use/configure/configuration-files
  - CSS `@layer`: the last-declared layer wins, `!important` reverses the order, and unlayered styles beat layered ones. https://developer.mozilla.org/en-US/docs/Web/CSS/@layer
  - Helm: the chart's values, then a parent chart's, then `-f`, then `--set`, and setting a key to `null` deletes it. https://helm.sh/docs/chart_template_guide/values_files/
  - NixOS: a unique option defined twice is a hard error ("is defined multiple times"), and `mkForce` picks one definition. https://nixos.org/manual/nixos/stable/
- **When upstream changes the same item:** the user's value wins silently and the upstream change is invisible. NixOS is the exception: two definitions at equal priority fail the build.
- **Delta and cost:** the user's layer holds only their keys, so it stays readable. The cost is low.
- **Against gov:**
  - Loses S1 silently.
  - On S2 and S3 the override is orphaned. The sources I read do not say whether a consumer errors on an unknown key.
  - Loses S4 unless the keys collide.
  - Handles S5 (Helm `null`) and S7 (resolution happens before rendering).
  - Has no notion of S6.
  - It fits values, not prose.

**F3. Patches addressed to a path in a base.**
- **Mechanism:** each patch names a target and a path inside it.
- **Systems:**
  - Kustomize: patches apply in order, and a strategic-merge patch finds its target by apiVersion, kind and name. https://kubectl.docs.kubernetes.io/references/kustomize/kustomization/patches/
  - **Ambiguity:** the docs do not say what happens when a target is missing. Forum reports show a hard error ("failed to find unique target for patch"), and one guide claims the patch is silently ignored. https://discuss.kubernetes.io/t/kustomize-failed-to-find-unique-target-for-patch/10582 and https://devopsboys.com/blog/kustomize-patch-not-applying-fix-2026
  - JSON Patch `test` (RFC 6902 §4.6, §5): the target value "MUST be equal" to the given value, and if any operation fails the whole patch fails. This is prior art for pinning a patch to its base. https://www.rfc-editor.org/rfc/rfc6902
  - Jinja: blocks with `super()`, and `required` blocks. **Ambiguity:** the docs do not say what happens to a child block the parent lacks. https://jinja.palletsprojects.com/en/stable/templates/
- **When upstream changes the same item:** upstream changes outside the patched path flow through. A change on the patched path is silently overwritten, unless a `test` operation pins it and fails loudly.
- **Delta and cost:** the patch is the delta, so it stays readable. The cost is medium.
- **Against gov:**
  - S1: silent, or loud with a pin.
  - S2 and S3: loud where the missing target errors.
  - Loses S4.
  - Handles S5 (delete directive) and S7.
  - Has no notion of S6.

**F4. Replace or wrap a shipped unit by its id.**
- **Mechanism:** the user ships a unit with the same id. Replacing shadows the shipped unit; wrapping decorates it.
- **Systems:**
  - Docusaurus swizzling: wrapping is "a far safer alternative" to ejecting. Components marked unsafe "may change in a backward-incompatible way between theme minor versions." https://docusaurus.io/docs/swizzling
  - WordPress child themes: a template with the same name replaces the parent's. https://developer.wordpress.org/themes/advanced-topics/child-themes/ Filters attach to a hook name. https://developer.wordpress.org/plugins/hooks/filters/
  - Rails engines: a view at the same path in the application replaces the engine's, and models are decorated with `class_eval`. https://guides.rubyonrails.org/engines.html
  - systemd: drop-ins in `/etc` beat `/usr/lib`, a list is reset by an empty assignment, and a unit is masked by a link to `/dev/null`. https://www.freedesktop.org/software/systemd/man/latest/systemd.unit.html `systemd-delta` reports each file as masked, equivalent, redirected, overridden, extended or unchanged. https://www.freedesktop.org/software/systemd/man/latest/systemd-delta.html
- **When upstream changes the same item:** a replaced unit silently shadows upstream's change; a wrapped one lets it flow through. Surfacing is a report you run on demand, never a failing check.
- **Delta and cost:** a wrap is a delta; a replacement is a full copy. The cost is low to medium.
- **Against gov:**
  - S1: lost silently on replace, handled on wrap.
  - Loses S2 and S3 with a silently inert orphan.
  - Loses S4.
  - Handles S5 (mask) and S7.

**F5. Three-way merge of a vendored copy.**
- **Mechanism:** rebuild the old base, diff it against the user's copy, and replay the diff onto the new version.
- **Systems:**
  - copier: conflicts come as inline markers (the default) or `.rej` files, files the user deleted stay excluded, and migrations run before and after. https://copier.readthedocs.io/en/stable/updating/
  - cruft: `cruft check` exits 1 when the project is behind its template. **Ambiguity:** the page does not document how it merges. https://cruft.github.io/cruft/
  - ucf `--three-way` uses diff3. https://manpages.debian.org/bookworm/ucf/ucf.1.en.html
  - `git merge-file`: the exit value is the number of conflicts. https://git-scm.com/docs/git-merge-file
- **When upstream changes the same item:** conflict markers land inside the file.
- **Delta and cost:** the delta is not kept as a delta; it only exists by re-diffing. The cost is high.
- **Against gov:**
  - S1 and S3 give conflict markers (probe A and A2 below).
  - Loses S4 silently, as a clean merge.
  - S5 conflicts later, when upstream edits the deleted lines.
  - Has no notion of S6.
  - Loses S7, because the edit lives in one harness's rendered document.

**F6. Patch queues re-applied on every update.**
- **Mechanism:** an ordered list of diffs is applied after each upstream install.
- **Systems:**
  - quilt: a series file, `push -f` for forced application, and fuzz up to 2 by default. https://www.man7.org/linux/man-pages/man1/quilt.1.html
  - patch-package: the package version is in the patch's filename, it exits 0 locally by default, and `--error-on-fail` is on by default in CI. https://github.com/ds300/patch-package
- **When upstream changes the same item:** the patch fails loudly, or it fuzzes into the wrong place silently (probe B).
- **Delta and cost:** the patch file is readable. The cost is medium.
- **Against gov:**
  - S1: the patch fails, or fuzzes into the wrong place silently.
  - S2 and S3: loud failure.
  - Loses S4 silently.

**F7. Keep-or-replace a whole config file, with a side copy.**
- **Mechanism:** a checksum of the shipped file shows whether the user edited it. If both sides changed, the user is prompted or a forced default applies, and the other version is written beside it.
- **Systems:**
  - Debian conffiles: if both sides changed, "the user is prompted," and a file the user removed is not restored. https://www.debian.org/doc/debian-policy/ap-pkg-conffiles.html
  - dpkg: `confold`, `confnew`, `confdef`, plus `.dpkg-dist` and `.dpkg-old` side files. https://man7.org/linux/man-pages/man1/dpkg.1.html
  - `dpkg-maintscript-helper`: `mv_conffile` leaves a modified file where it is, and `rm_conffile` keeps it as `.dpkg-bak`. Both carry a prior-version argument. https://manpages.debian.org/bookworm/dpkg/dpkg-maintscript-helper.1.en.html
  - RPM `%config(noreplace)`: a locally modified file "is preserved as-is on package updates", and the new one is written as `.rpmnew`. https://rpm-software-management.github.io/rpm/man/rpm-spec.5
  - ucf keeps a cache of past checksums, and `UCF_FORCE_CONFFOLD` "silently retains the installed file."
- **When upstream changes the same item:** interactively, a prompt. Unattended, the user's file is kept silently and upstream's version sits in a side file.
- **Delta and cost:** the delta is not readable; it is the whole file. The cost is low.
- **Against gov:**
  - Loses S1 silently when unattended.
  - Handles S2 through declared maintainer steps.
  - Loses S3 and S4.
  - Handles S5.

**F8. Ejection.**
- **Mechanism:** a one-way copy, after which the user owns everything.
- **Systems:**
  - Create React App: "a one-way operation" and "you're on your own." That updates stop after ejecting is my inference; the page does not say it. https://create-react-app.dev/docs/available-scripts/#npm-run-eject
  - Docusaurus eject (link above).
- **Against gov:** every upstream change is lost. It handles S5 trivially.

## Probes

I ran these in the session scratchpad, never in the repository.

- **Probe A (`git merge-file`).** The adopter amended a rule line and upstream reworded the same line. The result was exit 1 with inline markers.
- **Probe A2.** Upstream split that line into two rules. The result was exit 1, and the markers held both new lines against the adopter's edit.
- **Probe B (GNU `patch`, the same engine quilt uses).** Upstream inserted a section whose context lines matched the patch's. The result was "Hunk #1 succeeded at 1 with fuzz 2" and exit 0, with the adopter's line placed under `## Review` instead of `## Build`. That is silent misplacement.
- **Probe C (a throwaway model of tag-keyed amendments with a pinned base hash and upgrade steps that retarget renames and splits).**

| Scenario | Result |
|---|---|
| S1 reword | RED (base drift) |
| S1b typo-only reword | RED (false positive) |
| S2 rename with a declared step | green |
| S2 rename with no step | RED (dangling edge) |
| S3 split | RED (retarget required) |
| S4 contradicting new unit | **green (missed)** |

## Candidates for gov

1. **K1: additive overlay only.** This is F1 on the design's existing seam: P8 at architecture-v2 line 666 ("each repository's own rules render from its own overlay as a separate project block"), resolved by level.
   - **Losing scenario:** S5, where the adopter wants `core.reuse` gone.
   - **Result:** it loses. The overlay can only add a contradicting unit, and Claude's own docs say the model "may pick one arbitrarily."
2. **K2: tag-keyed amendments with a base fingerprint.** This combines F4's id override (wrap through `amends`, replace through `supersedes`), F3/RFC 6902's `test` pin and Nix's failing check.
   - Rename, split and retire maps ship in gov's existing upgrade steps (P38, line 839), as dpkg's `mv_conffile` does.
   - The renderer applies each amendment on the unit before rendering for each harness.
   - **Losing scenario:** S4.
   - **Result:** it loses S4, which stays green in probe C. Its other cost is noise: a typo fix to an amended unit reds the update (S1b).
3. **K3: three-way merge of rendered documents (F5).**
   - **Losing scenario:** S7.
   - **Result:** rejected. An adopter edit to the Claude render never reaches the Codex render. Conflicts arrive as markers inside an instruction file (probe A). It also breaks the handed fact that units are written only through the guarded command.
4. **K4: patch queue over unit text (F6).**
   - **Losing scenario:** S1 with matching context lines.
   - **Result:** rejected by probe B, which misplaced the patch with exit 0.
5. **K5: keep-or-replace per unit with a side copy (F7).**
   - **Losing scenario:** S1 under unattended runs, which v2 makes the default (line 468).
   - **Result:** rejected. Upstream's reword never lands, and the side copy is silent. If the side copy is made to fail a check instead, it becomes K2.
6. **K6: eject a kit or unit (F8).**
   - **Losing scenario:** any upstream release.
   - **Result:** rejected as the main mechanism. It is kept only as an explicit, recorded state that the update skips.
7. **K7: keyed values (F2).** This is already gov's level-2 knob catalogue.
   - **Losing scenario:** S1 applied to prose.
   - **Result:** right for values only.

## Pick

Take K2 and K1 together, with K7 for values:

- Adopter-new units go in their own overlay, ranked by level.
- Adopters change gov units only through `amends` (preferred, like Docusaurus wrap) or `supersedes`, keyed by tag and carrying the hash of the base unit they were written against.
- Upgrade steps carry the rename, split and retire maps, so a declared rename retargets silently.
- Drift, a dangling edge or a split fails a check at update. The adopter's resolution is recorded, never auto-merged.
- To cut the S1b noise, upstream marks each changed unit as editorial or semantic in the step, and an editorial change rebases the pin. Docusaurus's safe and unsafe labels are the precedent.
- S5 needs a retire or mask operation. The handed facts list `amends` and `supersedes` "among" the edges, and I did not verify whether the closed set has one.
- For S6, the renderer fails naming the overflowing units, never truncating as Codex does.
- For S7, one amended unit renders for both harnesses.
- A `systemd-delta`-style report lists every gov unit as amended, superseded, retired or unchanged.

**It handles S4 worst.** A new upstream unit under a different tag that contradicts an adopter unit trips nothing, as probe C shows. Every family I found loses S4 unless the two sides share a key, as in NixOS. The best available mitigation is advisory only:
- The update lists new units in namespaces or at levels the adopter has amended.
- A contradiction audit like Claude Code's `/doctor prompt-audit` runs over the result.

It cannot be a failing check, because a contradiction is semantic.

The probe files are in `C:\Users\d41ly\AppData\Local\Temp\claude\C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297\1799cb98-0882-4ab8-a308-19495d2a487a\scratchpad\probe\`. The design lines cited are in `C:\projects\coding-governance\.claude\worktrees\gov-architecture-plan-e34297\memory\builds\dClosedLoop\build\2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md`. Nothing in the repository was written.

Sources (all read 2026-10-19):
- [Claude Code memory](https://code.claude.com/docs/en/memory)
- [Codex AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md)
- [AGENTS.md](https://agents.md/)
- [Cursor rules](https://cursor.com/docs/context/rules)
- [git-config](https://git-scm.com/docs/git-config)
- [ESLint configuration files](https://eslint.org/docs/latest/use/configure/configuration-files)
- [MDN @layer](https://developer.mozilla.org/en-US/docs/Web/CSS/@layer)
- [Helm values files](https://helm.sh/docs/chart_template_guide/values_files/)
- [NixOS manual](https://nixos.org/manual/nixos/stable/)
- [Kustomize patches](https://kubectl.docs.kubernetes.io/references/kustomize/kustomization/patches/)
- [Kustomize patchesStrategicMerge](https://kubectl.docs.kubernetes.io/references/kustomize/kustomization/patchesstrategicmerge/)
- [Kubernetes forum: failed to find unique target](https://discuss.kubernetes.io/t/kustomize-failed-to-find-unique-target-for-patch/10582)
- [devopsboys: Kustomize patch not applying](https://devopsboys.com/blog/kustomize-patch-not-applying-fix-2026)
- [RFC 6902](https://www.rfc-editor.org/rfc/rfc6902)
- [Jinja templates](https://jinja.palletsprojects.com/en/stable/templates/)
- [Docusaurus swizzling](https://docusaurus.io/docs/swizzling)
- [WordPress child themes](https://developer.wordpress.org/themes/advanced-topics/child-themes/)
- [WordPress filters](https://developer.wordpress.org/plugins/hooks/filters/)
- [Rails engines](https://guides.rubyonrails.org/engines.html)
- [systemd.unit](https://www.freedesktop.org/software/systemd/man/latest/systemd.unit.html)
- [systemd-delta](https://www.freedesktop.org/software/systemd/man/latest/systemd-delta.html)
- [copier updating](https://copier.readthedocs.io/en/stable/updating/)
- [cruft](https://cruft.github.io/cruft/)
- [ucf(1)](https://manpages.debian.org/bookworm/ucf/ucf.1.en.html)
- [git merge-file](https://git-scm.com/docs/git-merge-file)
- [quilt(1)](https://www.man7.org/linux/man-pages/man1/quilt.1.html)
- [patch-package](https://github.com/ds300/patch-package)
- [Debian policy: conffiles](https://www.debian.org/doc/debian-policy/ap-pkg-conffiles.html)
- [dpkg(1)](https://man7.org/linux/man-pages/man1/dpkg.1.html)
- [dpkg-maintscript-helper](https://manpages.debian.org/bookworm/dpkg/dpkg-maintscript-helper.1.en.html)
- [rpm-spec(5)](https://rpm-software-management.github.io/rpm/man/rpm-spec.5)
- [Create React App eject](https://create-react-app.dev/docs/available-scripts/#npm-run-eject)
