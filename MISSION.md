# Mission: Understand Attention & Transformers

## The topic
Transformers — and specifically the **attention mechanism** at their core. How a
stream of context (tokens) gets processed inside an LLM: embeddings → query/key/value
→ attention → and onward through the stack.

## Why (the real reason)
The user works heavily with **LLMs and AI agents** and wants a genuine, accurate
mental model of **how context is processed and handled** by the machine. The driving
fascination is *attention itself* — "the concept I'm trying to learn the most about
from a machine perspective." This is **curiosity / general mastery**, not tied to a
single deliverable, but grounded in day-to-day work with LLM systems.

## What success looks like
- Hold an accurate, mechanistic mental model of attention (not just a metaphor).
- Be able to trace a request end-to-end: context in → tokens → embeddings → Q/K/V →
  attention → output, and explain *why* each step exists.
- Connect the theory back to practical LLM/agent work (context windows, why long
  context is expensive, why some tokens "attend" to others).

## Starting point (as of 2026-06-28)
In a prior session the user worked through the high-level pipeline of a request to an
LLM provider, and reached the **core attention mechanic**: embeddings as a lookup,
then the **Query / Key / Value** projections — stopping right at the doorway of the
**softmax** step. Comfortable with: tokens, embedding lookup, that Q/K/V are learned
projections. Next frontier: what softmax actually does to turn Q·K scores into an
attention output.

## Posture
Knowledge-forward (concept/theory), grounded in high-trust sources. Build the
mechanism first, then make it durable with retrieval practice. Tie every lesson back
to "how context is handled."
