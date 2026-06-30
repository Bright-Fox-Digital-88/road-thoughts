# Read-out understood: the full forward pass is now complete end-to-end

The user closed the loop from context to next token, resolving the final confusion themselves: how a
dictionary word is compared to "the vector space of the entire context window."

Key resolution (the user's own hinge question): **only the last position's vector is read out — not
all N tokens, not a fresh aggregate.** The paradox dissolves because attention already funnelled the
whole window *into* that summit vector across the layers; the aggregation happened earlier and is
stored there. So read-out = one context-soaked summit vector vs ~50,000 *fixed* dictionary
signatures, one dot product each → logits → softmax → sample.

Also now held:
- **Layer hierarchy** is emergent, not assigned: engineers design scaffold + objective; the
  form→structure→meaning→prediction ladder self-organises. Fuzzy/overlapping, not a clean staircase.
- **Unembedding** as dot-product-against-the-dictionary (same resonance trick as attention).
- **Temperature/sampling** (greedy, top-k, top-p) as the only "boldness" dial, applied at read-out.
- **Weight tying**: input embedding table reused (transposed) as the output unembedding — "the same
  door, read backwards."
- **Autoregressive loop**: predict, append, repeat, reusing the KV cache (ties back to prefill/decode).

Earlier in the same stretch the user also nailed, and had confirmed: Q/K/V projections are linear,
frozen after training, shared across tokens within a layer but **distinct per layer** (not tied
across layers, except in exotic archs like ALBERT); attention is **asymmetric** (separate Q,K
matrices), the give-budget sums to one while received attention is uncapped (cumulative), and causal
attention is acyclic except the self-loop.

**Captured as:** `lessons/0004-the-reading-of-the-last-line.html` (artifacts: the Ascending
Movements, the Summit, the Dictionary of Signatures, the Weighing, the Boldness Dial, the Door Read
Backwards). Glossary gained unembedding, logits, summit, temperature, sampling, autoregressive loop.

**Milestone:** Lessons 1–4 now cover the entire forward pass (embedding → Q/K/V → attention/softmax →
feed-forward → residual stream → layers → unembedding → sampling). The core arc of the course is
complete.

**Implications / next (queued):** (1) multi-head attention — "the Host's stewards" (several parallel
heads, each a different resonance, merged); (2) training — "how the Host learned his craft" (gradient
descent wiring the frozen weights). Keep extending the Host's-Evening / Ledger metaphor.
