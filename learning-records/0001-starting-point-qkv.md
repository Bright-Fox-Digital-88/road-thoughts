# Established floor: comfortable through Q/K/V, at the softmax doorway

The user arrived having already worked (in a prior session) through the LLM request
pipeline up to the **Query/Key/Value projections**, stopping right before softmax.
They understand tokens, embedding-as-lookup, and that Q/K/V are learned projections.

**Evidence:** Described the pipeline unprompted — "embedding which is a lookup… pull
the lookup of all the tokens… query key and value filters… before you run into the
softmax component."

**Implications:** Do not re-teach embeddings or the existence of Q/K/V. Start teaching
at the softmax / scaled-dot-product step (Lesson 1). The stated north star is
**attention specifically** ("the concept I'm trying to learn the most from a machine
perspective"), grounded in professional LLM/agent work — so tie mechanics back to
context handling, context-window cost, and what attention weights represent.
