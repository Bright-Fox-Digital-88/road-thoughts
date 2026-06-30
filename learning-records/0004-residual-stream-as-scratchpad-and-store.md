# The residual stream understood: one additive vector that is both store and scratchpad

The user drove to a full, accurate picture of what a token *is* as it moves through the network —
arguably the conceptual core of the whole subject. Now held:

- **A token = one fixed-length vector** (the residual stream), the *only* persistent state. Same
  length every layer. Everything (Q/K/V, feed-forward) is computed from it and added back into it.
  This dissolved the user's "amorphous state management" worry.
- **Additive identity**: residual connections mean each block *adds* to the vector, never
  overwrites. So the token stays continuously itself while deepening; the original token survives as
  a fading, additively-preserved echo (recoverable by probes in early layers, drowned/repurposed
  later).
- **"Erasure" = additive cancellation**: adding a negative-pointing vector nets information to zero.
  The user explicitly challenged the anthropomorphic "the model erases when it wants to"; corrected
  to: a *trained reflex* frozen in weights, no runtime agency.
- **Feed-forward, concretely**: expand (~4×) → non-linear gate (fire selectively) → contract → add.
  It's an associative memory holding much of the model's knowledge. Framing: attention =
  communication (move info between tokens); feed-forward = recall (consult a private library).
- **The vector is both a store of gradual truth AND a scratchpad** — the user independently
  re-derived "the residual stream as a shared communication channel/workspace." Components read/write
  subspaces and leave working notes for each other (composition); durable meaning and transient
  scratch share one finite, superposed page (why interpretability is hard).
- **Trajectory**: bottom layers ≈ "the token," top layers ≈ "a prediction of the next token." The
  representation is repurposed from description into prophecy.

**Evidence:** User generated each step as a question/hypothesis and was usually right before
confirmation (e.g. "you couldn't resolve the originating token because the coordinates moved";
"is this a scratchpad as well as a store of gradual truth").

**Captured as:** `lessons/0003-the-ledger-of-you.html` (artifacts: the Ledger, the Rule, the
Cancelling Line, the Three Thousand Specialists, the Margin Notes, the Last Line). Glossary gained
residual stream, residual connection, additive erasure, communication channel, superposition.

**Implications / next:** The user explicitly wants the close — **how the last page is read out into
an actual next word (the unembedding), where temperature lives**. That is the natural Lesson 4 and
was seeded as "The Reading of the Last Line." Multi-head attention ("the Host's stewards") still
pending. Keep extending the Host's-Evening / Ledger metaphor rather than inventing new frames.
