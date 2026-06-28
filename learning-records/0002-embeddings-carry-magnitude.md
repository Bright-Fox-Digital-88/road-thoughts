# Embeddings carry magnitude, not just direction — and attention uses it

The user previously held the common partial view that embeddings are "about the
cosine angle." Corrected and now understood: an embedding is a point/arrow in space,
so it **always** carries both direction (angle) and length (magnitude); cosine
similarity is a *comparison convention* that normalizes length away, not a property of
the embedding. Magnitude is a real second channel (correlates with strength/confidence/
frequency).

**Evidence:** User reasoned it out themselves — realized the dot product keeps the
"distance from origin" that cosine discards, and asked whether embeddings retain it.

**Implications:**
- This unlocks *why* attention uses the dot product rather than cosine: it gives the
  model a magnitude "volume knob," and the learned Q/K filters can set key magnitudes
  to make a token loud or quiet. Future lessons can lean on this.
- Established earlier in the same conversation and safe to assume going forward:
  the Q/K/V projections are independent/parallel (no ordering, computed agnostically
  from the same embedding); they interact only downstream when queries meet keys.
  Each filter is a distinct learned matrix emphasizing different features.
  In-context repetition shifts the (fixed, sums-to-one) attention "pie" toward the
  repeated token; training-data frequency is a separate mechanism baked into weights.
- Next teaching step the user explicitly queued: what a token *does* with its weighted
  blend of value cards (→ becomes upgraded representation, fed forward, repeated per
  layer). This is the seed for Lesson 2.
