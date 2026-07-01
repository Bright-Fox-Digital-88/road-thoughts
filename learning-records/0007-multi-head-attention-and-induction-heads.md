# Multi-head attention understood; induction heads = in-context learning

Taught after the user's perspective shift from token-view to state/board-view (they explicitly
proposed "examine the Host"). Lesson 6 revealed the one simplification the Evening had made — the
Host as a single reader — and completed the attention picture.

Now covered:
- **Multi-head attention**: a layer runs H parallel attentions (heads/"stewards"), each with its own
  Q/K/V in a 1/H-width slice, each forming its own distribution; outputs concatenated and passed
  through a learned output projection (the "chamberlain"). Nearly free because the width is
  partitioned, not added.
- **Why more than one**: a single distribution can't cleanly serve multiple simultaneous relationship
  types (subject-agreement vs meaning vs coreference); separate heads track them without interference.
- **Real, named heads**: previous-token, syntactic, name-mover.
- **Induction heads = in-context learning** (the headline, most practically relevant for the user):
  a previous-token head + an induction head match the current pattern to an earlier occurrence and
  copy what followed — no weight change. This is why few-shot prompting, format-following, and
  in-context examples work. Framed directly for the user's prompt/agent work.

**Captured as:** `lessons/0006-the-hosts-stewards.html` (artifacts: the Council of Stewards, the Two
Stewards Who Learn On The Fly, the Chamberlain). Glossary gained attention head, multi-head attention,
induction head, in-context learning.

**State of the course:** The full forward pass + attention are now complete with no remaining
simplifications. Lessons 1–6 + the CoT side-lesson.

**Implications / next (queued):** (1) training — "how the Host learned his craft" (gradient descent,
loss, backprop; also how heads acquire their specialties — ties back to induction heads); (2)
positional encoding — "where each guest's seat comes from" (attention is order-blind without it; the
Invitation's 'position' was asserted but never explained). Either is a strong next step; training is
the bigger conceptual arc. Keep extending the Host's-Evening metaphor.
