/* speech.js — hands-free narration for lessons, using the browser's built-in
   Web Speech API (window.speechSynthesis). No API keys, no network, no cost:
   it uses the phone's own text-to-speech voices.

   Drop <script src="../assets/speech.js" defer></script> into any lesson and a
   floating audio bar appears. It reads the readable blocks in document order,
   highlights the current one, and remembers your speed between lessons.

   Designed for on-the-road / hands-free use: big tap targets, resilient to the
   mobile "auto-stop after ~15s" bug via a pause/resume heartbeat. */
(function () {
  "use strict";

  var synth = window.speechSynthesis;
  if (!synth) return; // very old browser; no-op (page still readable)

  // Blocks we read, in DOM order. querySelectorAll returns document order,
  // and these selectors don't nest inside one another, so no double-reads.
  var SELECTOR = [
    "header h1", "header .subtitle",
    "main h2", "main h3", "main p", "main li",
    "main .keyidea", "main .mission", "main .note", "main .ask",
    "main .quiz .q", "main .quiz .opt",
    "main table.attn tr",
    "main .artifact .name", "main .artifact .maps", "main .artifact .desc",
    ".card .t", ".card .d"
  ].join(", ");

  var blocks = [];          // { el, text }
  var idx = -1;             // index of block currently/last spoken
  var playing = false;
  var rate = parseFloat(localStorage.getItem("tts-rate") || "1") || 1;
  var voice = null;
  var heartbeat = null;

  function collect() {
    blocks = [];
    document.querySelectorAll(SELECTOR).forEach(function (el) {
      var t = (el.innerText || el.textContent || "")
        .replace(/\s+/g, " ")
        .trim();
      // Read math symbols a touch more naturally for spoken delivery.
      t = t
        .replace(/·/g, " dot ")
        .replace(/Kᵀ/g, "K transpose")
        .replace(/√dₖ|√d_k|√dk/gi, "square root of d k")
        .replace(/dₖ/g, "d k")
        .replace(/Q·K/g, "Q dot K");
      if (t.length > 1) blocks.push({ el: el, text: t });
    });
  }

  function pickVoice() {
    var voices = synth.getVoices() || [];
    if (!voices.length) return null;
    var en = voices.filter(function (v) { return /^en(-|_|$)/i.test(v.lang); });
    var pool = en.length ? en : voices;
    // Prefer a natural-sounding default if present.
    var pref = pool.find(function (v) { return /samantha|daniel|google|natural|siri/i.test(v.name); });
    return pref || pool[0];
  }

  function clearHighlight() {
    blocks.forEach(function (b) { b.el.classList.remove("tts-active"); });
  }

  function highlight(i) {
    clearHighlight();
    if (i < 0 || i >= blocks.length) return;
    var el = blocks[i].el;
    el.classList.add("tts-active");
    try { el.scrollIntoView({ behavior: "smooth", block: "center" }); } catch (e) {}
  }

  function speakFrom(i) {
    if (i >= blocks.length) { stop(); status("Lesson finished ✓ — tap ▶ to replay"); return; }
    idx = i;
    highlight(i);
    var u = new SpeechSynthesisUtterance(blocks[i].text);
    u.rate = rate;
    if (voice) u.voice = voice;
    u.onend = function () { if (playing) speakFrom(idx + 1); };
    u.onerror = function () { if (playing) speakFrom(idx + 1); };
    synth.speak(u);
    status((i + 1) + " / " + blocks.length + " — " + short(blocks[i].text));
  }

  function short(t) { return t.length > 60 ? t.slice(0, 57) + "…" : t; }

  function play() {
    if (!blocks.length) collect();
    if (!voice) voice = pickVoice();
    playing = true;
    setPlayIcon();
    // Resume if paused mid-utterance; otherwise (re)start.
    if (synth.paused && synth.speaking) { synth.resume(); }
    else { synth.cancel(); speakFrom(idx < 0 ? 0 : idx); }
    startHeartbeat();
  }

  function pause() {
    playing = false;
    setPlayIcon();
    if (synth.speaking) synth.pause();
    stopHeartbeat();
    status("Paused — tap ▶ to resume");
  }

  function stop() {
    playing = false;
    setPlayIcon();
    synth.cancel();
    clearHighlight();
    idx = -1;
    stopHeartbeat();
  }

  function next() { if (blocks.length) { synth.cancel(); idx = Math.min(idx + 1, blocks.length - 1); if (playing) speakFrom(idx); else highlight(idx); } }
  function prev() { if (blocks.length) { synth.cancel(); idx = Math.max(idx - 1, 0); if (playing) speakFrom(idx); else highlight(idx); } }

  function setRate(delta) {
    rate = Math.min(2, Math.max(0.6, Math.round((rate + delta) * 10) / 10));
    localStorage.setItem("tts-rate", String(rate));
    speedEl.textContent = rate.toFixed(1) + "×";
    if (playing) { synth.cancel(); speakFrom(idx < 0 ? 0 : idx); } // apply immediately
  }

  // Mobile browsers silently kill long synthesis after ~15s; a periodic
  // pause+resume keeps it alive. Harmless on desktop.
  function startHeartbeat() {
    stopHeartbeat();
    heartbeat = setInterval(function () {
      if (playing && synth.speaking && !synth.paused) { synth.pause(); synth.resume(); }
    }, 12000);
  }
  function stopHeartbeat() { if (heartbeat) { clearInterval(heartbeat); heartbeat = null; } }

  // ── UI ──────────────────────────────────────────────────────────
  var bar, playBtn, statusEl, speedEl;

  function status(t) { if (statusEl) statusEl.textContent = t; }
  function setPlayIcon() { if (playBtn) playBtn.textContent = playing ? "⏸" : "▶"; }

  function buildBar() {
    bar = document.createElement("div");
    bar.className = "tts-bar";
    bar.setAttribute("role", "region");
    bar.setAttribute("aria-label", "Lesson audio player");

    playBtn = mkBtn("▶", "primary", function () { playing ? pause() : play(); });
    playBtn.setAttribute("aria-label", "Play or pause");

    var prevBtn = mkBtn("⏮", "", prev); prevBtn.setAttribute("aria-label", "Previous block");
    var nextBtn = mkBtn("⏭", "", next); nextBtn.setAttribute("aria-label", "Next block");
    var slowBtn = mkBtn("−", "", function () { setRate(-0.1); }); slowBtn.setAttribute("aria-label", "Slower");
    var fastBtn = mkBtn("+", "", function () { setRate(0.1); }); fastBtn.setAttribute("aria-label", "Faster");

    speedEl = document.createElement("span");
    speedEl.className = "tts-speed";
    speedEl.textContent = rate.toFixed(1) + "×";

    statusEl = document.createElement("span");
    statusEl.className = "tts-status";
    statusEl.textContent = "Tap ▶ to have this lesson read aloud";

    bar.appendChild(playBtn);
    bar.appendChild(prevBtn);
    bar.appendChild(nextBtn);
    bar.appendChild(slowBtn);
    bar.appendChild(speedEl);
    bar.appendChild(fastBtn);
    bar.appendChild(statusEl);
    document.body.appendChild(bar);
    document.body.classList.add("has-tts");
  }

  function mkBtn(label, cls, fn) {
    var b = document.createElement("button");
    b.textContent = label;
    if (cls) b.className = cls;
    b.addEventListener("click", fn);
    return b;
  }

  // Voices load asynchronously on most browsers.
  if (typeof synth.onvoiceschanged !== "undefined") {
    synth.onvoiceschanged = function () { if (!voice) voice = pickVoice(); };
  }

  // Stop narration if the user navigates away mid-lesson.
  window.addEventListener("pagehide", stop);

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", function () { collect(); buildBar(); });
  } else { collect(); buildBar(); }
})();
