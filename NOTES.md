# Notes

Working notes and user preferences for teaching.

## Preferences
- Learns via voice dictation, on the road ("road-thoughts" workspace) — lessons should
  read well and not assume the user can run code in the moment.
- Works with LLMs and AI agents professionally; relate concepts back to that practice.
- Already comfortable with the request pipeline up to Q/K/V. Don't re-teach embeddings
  from scratch — reference, don't belabor.

## Hands-free / audio
- User learns while driving — wants lessons to **read themselves aloud**, hands-free.
- Solved with `assets/speech.js`: a floating audio player using the browser's
  built-in Web Speech API (window.speechSynthesis). **No API keys, no cost** — uses
  the phone's own TTS voices. Every lesson links it. Big tap targets, play/pause,
  prev/next block, speed control, current-block highlight, mobile auto-stop heartbeat.
- **Implication:** every new lesson MUST stay readable as linear prose (the player
  reads blocks in DOM order). Keep interactive bits self-contained so the spoken
  flow still makes sense without tapping.

## Teaching log
- 2026-06-28: Workspace created. Mission set (attention/transformers, curiosity).
  Starting point: at the softmax doorway, post-Q/K/V. First lesson = Scaled
  Dot-Product Attention (the blend). Added hands-free audio player.
