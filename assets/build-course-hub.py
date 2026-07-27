#!/usr/bin/env python3
"""Assemble all lessons + glossary into one self-contained, interlinked single-page
course (inlines course.css, glossary term styles, and quiz.js; namespaces per-section
ids; rewrites cross-file links to in-page anchors; adds a data-theme bridge).

Published artifact URL: https://claude.ai/code/artifact/e942f7bf-c53f-417d-9579-a1577cf21ea1
To refresh that SAME url after editing lessons: run this script, then call the Artifact
tool with the generated file and url="https://claude.ai/code/artifact/e942f7bf-c53f-417d-9579-a1577cf21ea1".
"""
import re, pathlib, html as _html

ROOT = pathlib.Path("/home/user/road-thoughts")
css = (ROOT/"assets/course.css").read_text()
js  = (ROOT/"assets/quiz.js").read_text()

# glossary head <style> (term rules)
gloss_full = (ROOT/"reference/glossary.html").read_text()
gloss_style = re.search(r"<style>(.*?)</style>", gloss_full, re.S).group(1)

lessons = [
    ("lesson-1", "lessons/0001-attention-as-selection.html"),
    ("lesson-2", "lessons/0002-meaning-as-hub-and-spoke.html"),
    ("lesson-3", "lessons/0003-rider-and-elephant-rebuilt.html"),
]

def extract_body(text):
    # from first <h1 up to the lesson-nav div
    m = re.search(r"(<h1.*?)\s*<div class=\"lesson-nav\"", text, re.S)
    return m.group(1).strip()

def namespace(block, prefix):
    block = re.sub(r'id="([^"]+)"', lambda m: f'id="{prefix}{m.group(1)}"', block)
    block = re.sub(r'aria-labelledby="([^"]+)"', lambda m: f'aria-labelledby="{prefix}{m.group(1)}"', block)
    block = re.sub(r'href="#([^"]+)"', lambda m: f'href="#{prefix}{m.group(1)}"', block)
    block = re.sub(r'url\(#([^)]+)\)', lambda m: f'url(#{prefix}{m.group(1)})', block)
    return block

sections = []
for i,(anchor, rel) in enumerate(lessons, start=1):
    body = extract_body((ROOT/rel).read_text())
    body = namespace(body, f"s{i}-")
    sections.append(f'<section id="{anchor}" class="chapter">\n{body}\n</section>')

# glossary
gbody = extract_body(gloss_full)
gbody = namespace(gbody, "s0-")
sections.append(f'<section id="glossary" class="chapter">\n{gbody}\n</section>')

joined = "\n\n".join(sections)

# rewrite cross-file links to in-page anchors
repl = {
    'href="0001-attention-as-selection.html"': 'href="#lesson-1"',
    'href="0002-meaning-as-hub-and-spoke.html"': 'href="#lesson-2"',
    'href="0003-rider-and-elephant-rebuilt.html"': 'href="#lesson-3"',
    'href="../reference/glossary.html"': 'href="#glossary"',
    'href="../lessons/0001-attention-as-selection.html"': 'href="#lesson-1"',
    'href="../lessons/0002-meaning-as-hub-and-spoke.html"': 'href="#lesson-2"',
    'href="../lessons/0003-rider-and-elephant-rebuilt.html"': 'href="#lesson-3"',
}
for a,b in repl.items():
    joined = joined.replace(a,b)

# theme bridge: make the viewer's data-theme toggle authoritative in both directions.
theme_bridge = """
/* ---- data-theme bridge (artifact viewer toggle) ---- */
:root[data-theme="light"]{
  --ink:#1a1a1a;--paper:#fdfdfb;--muted:#6b6b6b;--rule:#dcdad2;
  --accent:#7a2e2e;--accent-soft:#f3e9e6;--dorsal:#2e5a7a;--ventral:#b5651d;
}
:root[data-theme="light"] .parallel{background:#eef3f7;}
:root[data-theme="light"] .breaks{background:#f7efe6;}
:root[data-theme="light"] .quiz{background:#fff;}
:root[data-theme="light"] .quiz .opt{background:var(--paper);}
:root[data-theme="light"] .primary-source{background:#f4f2ec;}
:root[data-theme="dark"]{
  --ink:#e8e6e0;--paper:#17171a;--muted:#9a988f;--rule:#35343a;
  --accent:#e0928a;--accent-soft:#2c2220;--dorsal:#8fb8d6;--ventral:#e0a76a;
}
:root[data-theme="dark"] .parallel{background:#1b2530;}
:root[data-theme="dark"] .breaks{background:#2a2118;}
:root[data-theme="dark"] .quiz{background:#1e1e22;}
:root[data-theme="dark"] .quiz .opt{background:#17171a;}
:root[data-theme="dark"] .quiz .opt.correct{background:#1c2e22;}
:root[data-theme="dark"] .quiz .opt.wrong{background:#2e1c1c;}
:root[data-theme="dark"] .primary-source{background:#1e1e22;}
"""

hub_style = """
/* ---- course hub ---- */
body{padding:0;}
.wrap{padding:0 1.5rem 6rem;}
.topnav{position:sticky;top:0;z-index:20;background:color-mix(in srgb,var(--paper) 88%,transparent);
  backdrop-filter:blur(8px);border-bottom:1px solid var(--rule);}
.topnav .inner{max-width:60rem;margin:0 auto;display:flex;flex-wrap:wrap;align-items:center;
  gap:.4rem 1.1rem;padding:.7rem 1.5rem;font-family:var(--sans);font-size:.82rem;}
.topnav .brand{font-weight:700;letter-spacing:.02em;margin-right:auto;color:var(--ink);border:none;}
.topnav a{color:var(--muted);border:none;white-space:nowrap;}
.topnav a:hover{color:var(--accent);}
.hero{max-width:44rem;margin:0 auto;padding:4.5rem 0 1rem;}
.hero .eyebrow{font-family:var(--sans);font-size:.72rem;letter-spacing:.16em;text-transform:uppercase;
  color:var(--accent);margin:0 0 1rem;}
.hero h1{font-size:2.9rem;line-height:1.06;text-wrap:balance;margin:0 0 1rem;}
.hero .thesis{font-size:1.3rem;color:var(--muted);font-style:italic;max-width:38rem;}
.toc{max-width:44rem;margin:2.5rem auto 0;display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:1rem;}
.toc a{display:block;border:1px solid var(--rule);border-radius:8px;padding:1rem 1.1rem;background:var(--paper);
  border-bottom:1px solid var(--rule);transition:border-color .15s,transform .15s;}
.toc a:hover{border-color:var(--accent);transform:translateY(-2px);}
.toc .n{font-family:var(--sans);font-size:.7rem;letter-spacing:.12em;text-transform:uppercase;color:var(--muted);}
.toc .t{font-family:var(--sans);font-weight:600;font-size:1rem;margin-top:.35rem;color:var(--ink);display:block;}
.toc .d{font-size:.9rem;color:var(--muted);margin-top:.3rem;}
.chapter{max-width:44rem;margin:0 auto;padding-top:3.5rem;}
.chapter+.chapter{border-top:1px solid var(--rule);margin-top:2rem;}
.chapter h1{font-size:2rem;}
.backtop{font-family:var(--sans);font-size:.8rem;display:inline-block;margin-top:1.5rem;color:var(--muted);border:none;}
@media(max-width:640px){.hero h1{font-size:2.1rem;}.hero{padding-top:3rem;}}
"""

favicon_note = ""

doc = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>The Human Brain · A Mini-Course</title>
<style>
{css}
{gloss_style}
{theme_bridge}
{hub_style}
</style>
</head>
<body>

<nav class="topnav"><div class="inner">
  <a class="brand" href="#top">The Human Brain</a>
  <a href="#lesson-1">1 · Attention</a>
  <a href="#lesson-2">2 · Meaning</a>
  <a href="#lesson-3">3 · Rider &amp; Elephant</a>
  <a href="#glossary">Glossary</a>
</div></nav>

<header id="top" class="hero">
  <p class="eyebrow">A mini-course · the mirror to LLM internals</p>
  <h1>How a human brain attends, means, and wants.</h1>
  <p class="thesis">You already know how a Transformer attends, embeds, and is pulled around.
  This is the other side of the equation — the same three jobs done in wetware, and the exact
  places where the machine analogy quietly breaks.</p>
  <div class="toc">
    <a href="#lesson-1"><span class="n">Lesson 1</span><span class="t">Attention as Selection</span>
      <span class="d">Biased competition, and the scarcity that LLM attention drops.</span></a>
    <a href="#lesson-2"><span class="n">Lesson 2</span><span class="t">Meaning as Hub &amp; Spoke</span>
      <span class="d">Where a concept lives — and why embeddings are a hub with no spokes.</span></a>
    <a href="#lesson-3"><span class="n">Lesson 3</span><span class="t">The Rider &amp; the Elephant</span>
      <span class="d">Control vs reward as real networks — and what ADHD changes.</span></a>
  </div>
</header>

<main class="wrap">
{joined}
<p style="max-width:44rem;margin:3rem auto 0"><a class="backtop" href="#top">↑ Back to top</a></p>
</main>

<script>
{js}
</script>
</body>
</html>
"""

out = pathlib.Path("/home/user/road-thoughts/../scratchpad-course-hub.html")
out.write_text(doc)
print("wrote", out, len(doc), "bytes; sections:", len(sections))
# quick duplicate-id sanity check
ids = re.findall(r'id="([^"]+)"', doc)
dupes = {x for x in ids if ids.count(x) > 1}
print("duplicate ids:", dupes if dupes else "none")
