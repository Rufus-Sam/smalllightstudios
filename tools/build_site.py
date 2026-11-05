"""Builds the site pages. Run: python3 tools/build_site.py . <PhosAndKin>/store/privacy-policy.md <Finding Life>/store/privacy-policy.md
(needs the markdown package; without the two policy paths the privacy pages are left as they are)."""
import pathlib, sys
site = pathlib.Path(sys.argv[1])
logo = (site / "assets/logo.svg").read_text().replace('<svg ', '<svg aria-hidden="true" ', 1)
play_svg = '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M5 3.5v17a1 1 0 0 0 1.5.86l14-8.5a1 1 0 0 0 0-1.72l-14-8.5A1 1 0 0 0 5 3.5z"/></svg>'
PK = "https://play.google.com/store/apps/details?id=com.rufusam.phosandkin"
FL = "https://play.google.com/store/apps/details?id=com.rufusam.finding_life"
PK_PRIV = "/phosandkin/privacy/"
FL_PRIV = "/findinglife/privacy/"
PIN = '<meta name="p:domain_verify" content="897a5ddaa8d560fddc6f5e8c36b38c08"/>'

def head(title, desc, url, image, icon, extra=""):
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
{PIN}
<link rel="icon" href="{icon}">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="stylesheet" href="/assets/site.css">
<meta property="og:type" content="website">
<meta property="og:url" content="{url}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{image}">
<meta name="twitter:card" content="summary_large_image">
{extra}</head>
<body>
<header class="top"><div class="wrap">
  <a class="brand" href="/">{logo}<span style="display:flex;flex-direction:column;line-height:1.15"><b>SMALL LIGHT</b><span>STUDIOS</span></span></a>
  <nav><a href="/#apps" class="keep">Apps</a><a href="/#about">About</a><a href="/#contact">Contact</a></nav>
</div></header>
'''

footer = f'''<footer><div class="wrap">
  <div class="cols">
    <div><a class="brand" href="/">{logo}<span style="display:flex;flex-direction:column;line-height:1.15"><b style="color:#fff">SMALL LIGHT</b><span>STUDIOS</span></span></a>
      <p style="margin:0">Small lights for everyday life.</p></div>
    <div><h4>Apps</h4><a href="/phosandkin/">Phos &amp; Kin</a><a href="/findinglife/">Finding Life</a></div>
    <div><h4>Studio</h4><a href="/#about">About</a><a href="/#contact">Contact</a><a href="mailto:hello@smalllightstudios.com">hello@smalllightstudios.com</a></div>
    <div><h4>Follow</h4><a href="https://www.youtube.com/@small-light-studios">YouTube</a><a href="https://www.linkedin.com/company/144087423/">LinkedIn</a></div>
  </div>
  <div class="fine">© 2026 Small Light Studios · <a href="{PK_PRIV}" style="display:inline">Phos &amp; Kin privacy</a> · <a href="{FL_PRIV}" style="display:inline">Finding Life privacy</a></div>
</div></footer>
</body>
</html>
'''

home = head("Small Light Studios", "Small lights for everyday life. We make calm, private apps for everyday people.",
            "https://smalllightstudios.com/", "https://smalllightstudios.com/og.jpg", "/favicon.png") + f'''
<section class="hero"><div class="wrap">
  <div>
    <h1>Small lights for everyday life.</h1>
    <p class="lead">We make calm, private apps for everyday people. Complex underneath, simple in your hand.</p>
    <div class="cta"><a class="btn btn-amber" href="#apps">See our apps</a><a class="btn btn-ghost" href="#about">Our story</a></div>
  </div>
  <div class="hero-mark">{logo}</div>
</div></section>

<section id="apps"><div class="wrap">
  <p class="kicker">Our apps</p>
  <h2>Made for the moments that matter</h2>
  <p class="sub">Each app does one thing well, so it fits quietly into your day.</p>
  <div class="products">
    <div class="card phos">
      <img class="icon" src="/phosandkin/icon.png" alt="Phos &amp; Kin icon">
      <h3>Phos &amp; Kin</h3>
      <p class="tag">A little light every day, for you and the people you love.</p>
      <p>Daily quotes, reminders for the birthdays that matter, and greeting and festival cards to send in seconds.</p>
      <div class="actions"><a class="btn btn-white" href="{PK}">{play_svg} Get it on Google Play</a><a class="more" href="/phosandkin/">Learn more →</a></div>
    </div>
    <div class="card life">
      <img class="icon" src="/findinglife/icon.png" alt="Finding Life icon">
      <h3>Finding Life</h3>
      <p class="tag">A quiet companion for new believers and honest seekers.</p>
      <p>The Bible, guided journeys, true stories of faith and help for hard days, for anyone wrestling with doubt.</p>
      <div class="actions"><a class="btn btn-amber" href="{FL}">{play_svg} Get it on Google Play</a><a class="more" href="/findinglife/">Learn more →</a></div>
    </div>
  </div>
</div></section>

<section class="story" id="about"><div class="wrap">
  {logo}
  <div>
    <p class="kicker" style="color:var(--amber)">Our mark</p>
    <h2>One line, from a tangle to a light.</h2>
    <p>We know what we want to make: something simple. Getting there is complex, and that's our job. Our mark is one line that starts as a knot, smooths into an S and ends in a small light. You only ever see the light.</p>
  </div>
</div></section>

<section class="contact" id="contact"><div class="wrap">
  <p class="kicker">Contact</p>
  <h2>Say hello</h2>
  <p class="sub">Questions, ideas or partnerships: we read every message.</p>
  <a class="btn btn-dark" href="mailto:hello@smalllightstudios.com">hello@smalllightstudios.com</a>
</div></section>
''' + footer

phos = head("Phos &amp; Kin: daily quotes, birthday reminders and festival cards",
            "A little light every day, for you and the people you love. Daily quotes, birthday reminders and greeting cards in seconds. Free on Google Play.",
            "https://smalllightstudios.com/phosandkin/", "https://smalllightstudios.com/phosandkin/cover.jpg", "/phosandkin/icon.png",
            '<meta name="twitter:site" content="@phosandkin">\n') + f'''
<section class="p-hero phos"><div class="wrap">
  <div>
    <img class="icon" src="/phosandkin/icon.png" alt="Phos &amp; Kin icon">
    <h1>Phos &amp; Kin</h1>
    <p class="lead">A little light every day, for you and the people you love.</p>
    <a class="btn btn-white" href="{PK}">{play_svg} Get it free on Google Play</a>
  </div>
  <div class="art">
    <div style="width:min(380px,80vw);aspect-ratio:4/5;border-radius:28px;padding:36px;display:flex;flex-direction:column;justify-content:flex-end;background:linear-gradient(160deg,#3bb6d9,#1f7fb8);box-shadow:0 30px 60px rgba(0,0,0,.3)">
      <p style="font:600 13px var(--sans);letter-spacing:.2em;margin:0 0 auto;opacity:.85">TODAY · CALM</p>
      <p style="font:700 30px/1.25 var(--serif);margin:0 0 18px">“Everything does not need to happen today.”</p>
      <p style="margin:0;opacity:.85">Phos &amp; Kin</p>
    </div>
  </div>
</div></section>

<section><div class="wrap">
  <p class="kicker">What it does</p>
  <h2>For you, and for your people</h2>
  <p class="sub">Phos for the light you need each morning. Kin for the people you love, with the least effort.</p>
  <div class="features">
    <div class="feature"><div class="emoji">☀️</div><h3>A quote every morning</h3><p>A new quote each day, read aloud in a voice like family. Save the ones you love and share them as cards.</p></div>
    <div class="feature"><div class="emoji">🎂</div><h3>Never miss a birthday</h3><p>Add the people who matter. On the day, you get a reminder with their card already made.</p></div>
    <div class="feature"><div class="emoji">💌</div><h3>Cards in seconds</h3><p>Birthdays, weddings, new babies, thank-yous and more. Add their name and send it on WhatsApp.</p></div>
    <div class="feature"><div class="emoji">🪔</div><h3>Festivals on their real dates</h3><p>Diwali, Eid, Christmas, Lunar New Year and many more arrive on the right day, with cards to send to everyone.</p></div>
    <div class="feature"><div class="emoji">🌏</div><h3>In your language</h3><p>English, हिन्दी, தமிழ், 中文, 日本語, 한국어, العربية, Deutsch and Français.</p></div>
    <div class="feature"><div class="emoji">🔒</div><h3>Yours, on your phone</h3><p>No account to create. Your people and their dates stay on your phone.</p></div>
  </div>
</div></section>

<section class="band phos"><div class="wrap">
  <h2>A little light, every day</h2>
  <p>Free on Google Play.</p>
  <a class="btn btn-white" href="{PK}">{play_svg} Get Phos &amp; Kin</a>
  <div class="socials">
    <a href="https://www.youtube.com/@phosandkin">YouTube</a><a href="https://www.instagram.com/phosandkin/">Instagram</a>
    <a href="https://www.facebook.com/phosandkin/">Facebook</a><a href="https://whatsapp.com/channel/0029Vb97SZf0lwgmgV94i334">WhatsApp Channel</a>
    <a href="https://pinterest.com/phosandkin">Pinterest</a><a href="https://www.threads.com/@phosandkin">Threads</a><a href="https://x.com/phosandkin">X</a>
  </div>
  <p class="note" style="color:#fff;opacity:.8;margin:24px 0 0"><a href="{PK_PRIV}">Privacy policy</a></p>
</div></section>
''' + footer

life = head("Finding Life: a quiet Bible companion for new believers and seekers",
            "Finding Life is a quiet companion for new believers, honest seekers and anyone wrestling with doubt. Free on Google Play.",
            "https://smalllightstudios.com/findinglife/", "https://smalllightstudios.com/findinglife/cover.jpg", "/findinglife/icon.png") + f'''
<section class="p-hero life"><div class="wrap">
  <div>
    <img class="icon" src="/findinglife/icon.png" alt="Finding Life icon">
    <h1>Finding Life</h1>
    <p class="lead">Whoever you are, wherever you've been, whatever you believe right now, you are welcome here.</p>
    <a class="btn btn-amber" href="{FL}">{play_svg} Get it free on Google Play</a>
  </div>
  <div class="art phones">
    <img src="/findinglife/home.jpg" alt="The rose window home screen">
    <img src="/findinglife/6-bible.jpg" alt="Reading the Bible">
    <img src="/findinglife/4-story.jpg" alt="A story of faith">
  </div>
</div></section>

<section><div class="wrap">
  <p class="kicker">Inside the app</p>
  <h2>A quiet companion for the journey</h2>
  <p class="sub">For new believers, honest seekers and anyone wrestling with doubt, built on the Bible and the faith of the Reformation.</p>
  <div class="features">
    <div class="feature"><div class="emoji">🪟</div><h3>The rose window</h3><p>Your home is a stained-glass window. Each pane opens a part of the app, and today's verse shines in the centre.</p></div>
    <div class="feature"><div class="emoji">📖</div><h3>The Holy Bible</h3><p>The complete Bible in your language. Search, save verses and read at the text size you like.</p></div>
    <div class="feature"><div class="emoji">🧭</div><h3>Guided journeys</h3><p>Day-by-day paths for new believers, seekers and doubters, with Scripture, plain teaching and a prayer.</p></div>
    <div class="feature"><div class="emoji">🕯️</div><h3>Stories of faith</h3><p>True lives of martyrs, reformers, missionaries and ordinary believers through the centuries.</p></div>
    <div class="feature"><div class="emoji">🌍</div><h3>How the church grew</h3><p>Turn a globe and travel through 2,000 years of church history, told honestly, including your own land.</p></div>
    <div class="feature"><div class="emoji">🤝</div><h3>Help for hard days</h3><p>Help for anxiety, grief, loneliness and more, with free helplines one tap away if you're in crisis.</p></div>
  </div>
  <p class="note" style="margin-top:32px">Finding Life isn't a substitute for a local church, a pastor, a doctor or emergency help. It's a companion that points you to Christ and to the people God puts around you.</p>
</div></section>

<section class="band life"><div class="wrap">
  <h2>You are welcome here</h2>
  <p>Free on Google Play.</p>
  <a class="btn btn-amber" href="{FL}">{play_svg} Get Finding Life</a>
  <p class="note" style="color:#fff;opacity:.8;margin:24px 0 0"><a href="{FL_PRIV}">Privacy policy</a></p>
</div></section>
''' + footer

# Privacy policies: rendered from each app repo's store/privacy-policy.md (passed as arguments 2 and 3).
import markdown, re
def policy(md_path, app, url, icon):
    text = pathlib.Path(md_path).read_text()
    text = re.sub(r"\A---\n.*?\n---\n", "", text, flags=re.S)
    body = markdown.markdown(text, extensions=["tables"])
    return head(f"{app} privacy policy", f"How {app} handles your information.", url,
                "https://smalllightstudios.com/og.jpg", icon) + f'<section><div class="wrap doc">{body}</div></section>\n' + footer
if len(sys.argv) > 3:
    (site / "phosandkin/privacy").mkdir(exist_ok=True)
    (site / "findinglife/privacy").mkdir(exist_ok=True)
    (site / "phosandkin/privacy/index.html").write_text(policy(sys.argv[2], "Phos &amp; Kin", "https://smalllightstudios.com/phosandkin/privacy/", "/phosandkin/icon.png"))
    (site / "findinglife/privacy/index.html").write_text(policy(sys.argv[3], "Finding Life", "https://smalllightstudios.com/findinglife/privacy/", "/findinglife/icon.png"))

(site / "index.html").write_text(home)
(site / "phosandkin/index.html").write_text(phos)
(site / "findinglife/index.html").write_text(life)
print("built")
