# dOrderedCharter — unit 54's builder return

**Serves:** journal PLAY-dOrderedCharter-54

Runs wf_cf2120ed-3f0 and wf_e052e0f1-146, summarized from their returns.

- The first run stood down without writing a product file: a second copy of its own builder, resumed by a main-loop message, was
  writing the same files. That copy built the unit in the tree and was stopped by a session restart before its commit. The second
  run verified that work against spec 54 rev-3, fixed two pinned-facts reds in the records, and committed pass commit `c6c477853`
  with no divergence.
- What landed: the kickoff checker reads the session's transcript path and source from its one stdin read; the card file's owner
  line carries the owner's transcript; another owner is live only while its transcript moved within the bound; a clear successor
  or a dead owner's card is taken over with a printed line, after the rename lands; the suite gains the owner arms.
- Two deviation records (DERIVED at c6c477853) hold the replay arm's card removal and the age tolerance a slow card write needs;
  one more names the spec's tag citations changed to the alias inside the pass.
- Probes it ran, none a gate: the changed checker over fixture repositories with Windows transcript paths, printing each
  criterion's owner line and verdict.
- Owed to the close: every leg on the gates line, the tags check the role hook refused, and the RED-first observation of the new
  owner arms.
