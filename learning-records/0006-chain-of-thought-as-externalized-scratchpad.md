# Chain-of-thought understood as externalized compute/memory over a frozen past

The user diverged (practically, for their agent work) into *why* chain-of-thought works, and
reasoned to the right model with one correction needed.

Resolved:
- **No mechanical "CoT token" vs "output token."** Every token is generated identically; the
  distinction is content/convention/training, not a switch. (User had imagined a strategic choice of
  token *type*; corrected to behavior expressed through *content*.)
- **The past is frozen under appending — guaranteed, not "probably."** The user's instinct ("all the
  tokens before will probably read exactly the same") was upgraded to a deterministic guarantee via
  causal-mask invariance — the same fact that makes the KV cache valid. The forward pass is
  deterministic; only sampling is random. (Honest caveat noted: floating-point/hardware wobble in
  practice.)
- **What CoT buys:** emitting an intermediate result persists it from the finite internal scratchpad
  (fixed width + fixed depth per step) into the durable token stream, where future passes attend to
  it exactly — buying more serial compute and an external memory. "Showing your work on paper."
- **Forward-only influence:** an appended token shapes later tokens, never earlier ones — so
  reasoning must come *before* the answer.

**Evidence:** User articulated the determinism/"manifestation stack reproduces" intuition unprompted
and asked precisely how it works; clearly connecting it back to the earlier KV-cache/causal-mask
material.

**Captured as:** `lessons/0005-the-pinned-note.html` (side-lesson; artifacts: No Token Has a Type,
the Frozen Past, the Pinned Note, Forward-Only Influence) with practitioner takeaways. Glossary
gained chain-of-thought.

**Note on the user's strengths:** consistently derives mechanisms by reasoning from first principles
and asks for confirmation/correction — teach by validating + sharpening rather than lecturing.
Strongly motivated by ties to real LLM/agent practice. Still queued: multi-head attention (the Host's
stewards) and training (how the Host learned his craft).
