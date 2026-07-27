# Working Notes

## Learner profile
- Sophisticated mental model of LLM internals (attention, context, memory) already in place.
- Thinks philosophically/mechanistically; enjoys the human↔machine parallel and wants it drawn
  explicitly — including, honestly, where it breaks.

## Teaching preferences (update as they emerge)
- Use the LLM parallel as scaffolding, but flag misleading analogies rather than smoothing them over.
- Ground every claim in trusted sources (see RESOURCES.md). No parametric hand-waving.
- Short lessons, one win each.

## Course arc (planned — three concepts from the opening request)
1. **Attention** — biased competition, dorsal/ventral control. → Lesson 1 (done).
2. **Meaning** — hub-and-spoke: distributed feature "spokes" + an ATL integrating hub. Sets up
   a rich contrast with LLM distributed embeddings / the token-vs-meaning philosophy. → Lesson 2 (done).
3. **Control vs reward — rider & elephant, rebuilt + ADHD** (re-scoped from user request). Triple-
   network model (executive / default-mode / salience switch) + reward engine; Sonuga-Barke dual
   pathway + default-mode interference. → Lesson 3 (done).
4. **[Open] The spin-up / hand-off / spin-back-up cycle** — the ORIGINAL concept 3, deferred by the
   user. Working-memory maintenance, goal silencing & reactivation, activity-silent states. Offered
   as Lesson 4. Sources already scouted (Nature Comms 2023 goal-silencing paper).

## Published course URL
- Interlinked single-page course (all 3 lessons + glossary) is published as an artifact:
  https://claude.ai/code/artifact/e942f7bf-c53f-417d-9579-a1577cf21ea1
- Regenerate with `assets/build-course-hub.py`, then re-publish to the SAME url by passing
  `url=` that link to the Artifact tool. (User asked for "Cloudflare" — we used claude.ai hosting;
  if they want their own Cloudflare Pages, the builder's output HTML is fully self-contained and
  deployable as a single file.)

## Mission watch
- ADHD self-understanding has emerged as a real motivating thread (see LR-0002). NOT yet folded into
  MISSION.md — ask the user before formalising. If confirmed, add a success criterion about reasoning
  about their own attention/reward system.

## Community
- Proposed r/neuro, r/cogsci, Cognitive Neuroscience Society. User has NOT yet expressed a
  preference about joining — ask before leaning on communities.
