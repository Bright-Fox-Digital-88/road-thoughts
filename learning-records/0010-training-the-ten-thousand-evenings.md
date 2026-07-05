# Training understood: the meaning-space as sediment of prediction, plus the data pipeline

Crystallized the training arc (developed across several poking sessions) into Lesson 9. The user now
holds the full origin story of the meaning-space they'd been exploring.

Covered:
- **The loop**: random init → next-token prediction (self-supervised; data is its own answer key) →
  loss = "surprise" (cross-entropy) → backprop (credit/blame to every weight) → gradient descent (tiny
  nudge, the learning rate) → repeat at scale.
- **Emergence**: understanding is a *byproduct* of getting good at prediction, never a goal — "meaning
  is what precipitates when you get very good at guessing what comes next."
- **Data pipeline**: collect/extract → quality-filter → deduplicate → decontaminate → mix/weight →
  tokenize → pack → shuffle. Plus the deeper points the user reasoned to:
  - Weighting = **sampling proportions**; downweighting-by-subsetting can mean parts are *never seen*.
  - Epochs ≈ 1 (repetition harmful; breadth over re-reading); high-quality subsets upweighted.
  - Shuffling = **de-biasing** (within-doc order = signal/kept; cross-doc order = noise/erased) →
    unbiased gradients, no recency/forgetting, no spurious streaks, smoother descent; annealing
    deliberately re-introduces order-bias at the end.
  - Packing: boundary tokens + intra-doc attention masking; long docs must span (no attention across
    sequences); **best-fit packing** to minimize truncation (fewer truncations → less hallucination) —
    the user re-derived this heuristic independently.
- **Finishing school** (fine-tuning/instruction-tuning/RLHF) shapes behaviour, not knowledge.
- **Frozen Host**: weights locked at inference; the model doesn't learn from prompts — in-context
  adaptation is induction heads (Lesson 6) reading the board, not weights changing.

Also confirmed earlier this session: a token's **Value** is the payload absorbed by tokens attending to
it (Key matches, Value transfers); non-depleting, per-head, causal, self-inclusive.

**Captured as:** `lessons/0009-the-ten-thousand-evenings.html` (artifacts: Blank Host, Guess Who Comes
Next, Measure of Surprise, the Accountant, the Nudge, Structure Precipitates, Weighting the Diet, the
Shuffle, Packing Without Snipping, Finishing School, the Frozen Host). Glossary gained pretraining,
loss/cross-entropy, backpropagation, gradient descent, emergence, fine-tuning/RLHF, frozen weights.

**State of the course:** the full lifecycle is now covered — training (build) → forward pass (use) →
read-out, plus attention in full, two applied side-lessons, and a reflection. Lessons 1–9.

**Queued next:** positional encoding ("where each guest's seat comes from" — the last asserted-but-
unexplained mechanic), and optionally a deeper "what a gradient actually is" (chain rule / loss
landscape). Keep extending the Host's-Evening metaphor.
