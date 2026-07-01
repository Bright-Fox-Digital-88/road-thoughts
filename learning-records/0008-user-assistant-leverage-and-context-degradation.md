# User/assistant token dynamics, prompt leverage, and long-context degradation

A rapid applied divergence, largely user-driven and correct; captured as an applied lesson.

Now covered:
- **CoT as "pondering"**: accepted analogy — extra steps before committing — with the caveat that CoT
  genuinely adds compute but is not guaranteed a faithful report of the deciding computation.
- **User/system vs assistant tokens**: user/system are *prefilled, not sampled*; generation starts at
  the assistant turn. Mechanically identical processing — the role split is a *learned convention*
  (chat-template role tokens + fine-tuning) over a uniform machine.
- **Prompt = high leverage** (three mechanical reasons): upstream of everything (max attention reach,
  esp. system prompt at position 0), noise-free anchors (not sampled), and copied by induction heads.
  Framing: "you set the board; the model plays."
- **Deterministic dynamics + one sampling die**: runs diverge in words, usually re-converge in meaning
  (attractor basins); can occasionally cascade at forks / high temperature.
- **Long-context degradation** (the user's "~40% / pattern bandwidth / looping" observation),
  decomposed into four mechanisms: attention dilution (fixed dance-card budget spread thin),
  lost-in-the-middle (positional bias to start/end), out-of-distribution length (positional encoding
  less practised far out), and self-reinforcing induction-head loops (the copy mechanism amplifies
  repetition; self-conditioning echo chamber). "~40%" flagged as rule-of-thumb, not a law.

**Captured as:** `lessons/0007-the-crowded-room.html` (artifacts: Setting the Board, One Uniform Many
Costumes, Deterministic Dynamics One Die, the Finite Heart, Lost in the Middle, A Room Bigger Than
Rehearsal, the Echo That Feeds Itself). Glossary gained chat template/role tokens, attention dilution,
lost in the middle.

**State of the course:** full forward pass + attention complete (Lessons 1–6) plus two applied
side-lessons (5: chain-of-thought; 7: context/leverage). The user consistently reasons from the
mechanics to real practitioner phenomena — the applied lessons land hardest.

**Implications / next (queued):** training ("how the Host learned his craft") and positional encoding
("where each guest's seat comes from" — now doubly motivated, since positional degradation came up
here). Keep extending the Host's-Evening metaphor.
