# Full forward-pass skeleton understood, anchored by the Host's-Evening metaphor

In one extended conversation the user assembled and stress-tested the whole forward-pass
skeleton, driving the questions themselves. Now solidly held:

- **Q/K/V are computed in parallel** from each token's vector, independent of one another; they
  interact only downstream when queries meet keys.
- **Layers**: not one contextual pass but dozens (mix via attention, then digest via a per-token
  feed-forward step), each re-contextualizing the last. Early→surface, late→abstract.
- **Two flow directions**: layers are sequential (a wave up the stack); tokens within a layer are
  fully parallel. Resolved the user's confusion that "left-to-right" had killed parallelism — the
  causal mask constrains *information flow*, not *computation timing*; sequential production only
  happens during decode because future tokens don't exist yet.
- **Causal mask makes caching exact**: a token's state depends only on its left context, so the
  prefix is frozen and losslessly cacheable; later-dependent meaning is resolved by later tokens
  attending back (cheap read), not by recomputing the prefix. Corrected the user's worry that
  cached content could be "conditional on what follows."
- **Prefill is the full stack over all tokens (not layer 1)**; the KV cache saves redoing that full
  pass per generated token. Long context → quadratic prefill, linearly-growing cache memory.

**Evidence:** The user reasoned each step out via probing questions (e.g. derived why precompute is
impossible, spotted the parallel-vs-left-to-right tension, questioned cache validity under forward
dependency) — genuine use, not exposure.

**The metaphor:** The user co-built "The Host's Evening" — a token at a party guided by a wise,
trained Host (the orchestrator = the attention mechanism + learned weights). Saved as
`lessons/0002-the-hosts-evening.html` with each prop as an "artifact" state-card. The user wants to
keep expanding this single metaphor.

**Implications / next:** Teach future topics by *extending the Host's Evening*, not inventing new
frames. Queued expansions (already seeded in Lesson 2): multi-head attention = the Host's
**stewards** (parallel heads, each attuned to a different kind of resonance); **temperature** = the
sharpness/looseness of the room; **context window** = the width of the doorway / guest-list cost.
Multi-head is the natural Lesson 3.
